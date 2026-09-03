"""
The join between the two engines.

The agent book knows which tier every customer is in, month by month. The
ported engine, which is what the Monte Carlo runs, was inheriting the
workbook's shortcut: one blended discount rate on a flat share of the book.

That shortcut is the one place where the aggregate engine loses information
that the agent engine has. It is also wrong in a known direction: nobody has
the tenure for Platinum in year two, so a flat rate is too generous early and
too mean late.

This module removes it. The agent book is run once across a spread of
persistency values, producing a lookup of

    persistency  ->  (tier share by month, effective discount by month)

The ported engine reads that lookup on every path. Ten minutes to build the
profile, then free on every path, instead of hours running agents inside the
Monte Carlo loop.

Cached to outputs/tiermix_profile.json; delete that file to force a rebuild.
"""

import json
import os

import numpy as np

from config import config as C

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(_HERE, "outputs", "tiermix_profile.json")

# persistency values to profile; the MC draws inside this range
GRID = [0.45, 0.53, 0.58, 0.63, 0.68, 0.73, 0.80]


def _scaled_archetypes(persistency):
    """Rescale every hazard by one factor so month-13 persistency hits target."""
    from scipy.optimize import brentq
    w = np.array([a.weight for a in C.ARCHETYPES_BASE])
    own = np.array([a.own_hazard for a in C.ARCHETYPES_BASE])
    bg = C.BACKGROUND_HAZARD["base"]
    tot = own + bg

    def surv13(k):
        return float((w * (1 - np.clip(tot * k, 0, 0.99)) ** 12).sum())

    k = brentq(lambda k: surv13(k) - persistency, 0.05, 5.0)
    A = type(C.ARCHETYPES_BASE[0])
    arche = [A(a.name, a.weight, a.pay_prob, max(0.0, (a.own_hazard + bg) * k - bg * k),
               a.pay_decay, a.pay_floor) for a in C.ARCHETYPES_BASE]
    return arche, bg * k


def build_profile(scale=8.0, seed=20270101, verbose=True):
    """Run the agent book at each persistency on the grid; return the lookup."""
    from src.agentbook import run_book, LADDER
    prof = {"grid": GRID, "months": C.HORIZON_MONTHS, "entries": {}}
    for pers in GRID:
        arche, bg = _scaled_archetypes(pers)
        pool, panel, sc = run_book(seed=seed, scale=scale, archetypes=arche)
        series = {k: [] for k in ("tier_share", "entry", "card", "family", "rebate")}
        for row in panel:
            tm = np.array(row["tier_mix"], dtype=float)
            live, tiered = tm.sum(), tm[1:].sum()
            series["tier_share"].append(float(tiered / live) if live else 0.0)
            if tiered > 0:
                w = tm[1:] / tiered            # mix WITHIN the tiered population
                # each expressed the way the workbook expresses it, so the
                # ported engine can use them in place of its four flat rates
                series["entry"].append(float((w * (0.05 - LADDER["entry_fee"][1:])).sum() / 0.05))
                series["card"].append(float((w * (0.02 - LADDER["fx_margin"][1:])).sum() / 0.02))
                series["family"].append(float((w * LADDER["family_disc"][1:]).sum()))
                series["rebate"].append(float((w * LADDER["rewards"][1:]).sum()))
            else:
                for k in ("entry", "card", "family", "rebate"):
                    series[k].append(0.0)
        prof["entries"][f"{pers:.2f}"] = series
        if verbose:
            print(f"  persistency {pers:.2f}: tiered {series['tier_share'][-1]:.1%} | "
                  f"entry disc M12 {series['entry'][11]:.1%} -> M84 {series['entry'][-1]:.1%} | "
                  f"card {series['card'][-1]:.1%} | family {series['family'][-1]:.1%}")
    return prof


def load_profile(rebuild=False, **kw):
    if not rebuild and os.path.exists(CACHE):
        with open(CACHE) as f:
            return json.load(f)
    prof = build_profile(**kw)
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w") as f:
        json.dump(prof, f)
    return prof


def lookup(prof, persistency, grid_months, grid_periods):
    """
    Interpolate the profile to a persistency, then aggregate the monthly
    series onto the engine's 29-period grid.

    Returns a dict of five arrays on the 29-period grid: tier_share, and the
    four effective benefit rates expressed exactly as the workbook expresses
    its four flat rates, so they are drop-in replacements.
    """
    g = np.array(prof["grid"], dtype=float)
    p = float(np.clip(persistency, g[0], g[-1]))
    lo = int(np.searchsorted(g, p, side="right") - 1)
    lo = min(max(lo, 0), len(g) - 2)
    frac = (p - g[lo]) / (g[lo + 1] - g[lo])

    def blend(key):
        a = np.array(prof["entries"][f"{g[lo]:.2f}"][key], dtype=float)
        b = np.array(prof["entries"][f"{g[lo + 1]:.2f}"][key], dtype=float)
        return a + frac * (b - a)

    keys = ("tier_share", "entry", "card", "family", "rebate")
    monthly = {k: blend(k) for k in keys}
    out = {k: np.zeros(29) for k in keys}
    mi = 0
    for i, m in enumerate(grid_months):
        m = int(m)
        for k in keys:
            seg = monthly[k][mi:mi + m]
            out[k][i] = seg.mean() if seg.size else 0.0
        mi += m
    return out
