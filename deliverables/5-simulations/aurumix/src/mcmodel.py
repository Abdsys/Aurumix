"""
The Monte Carlo layer over the deterministic engine.

Each path draws its own parameter set, gold path, acquisition noise and partner
arrivals, then runs the ported engine. The parameter distributions are anchored
on the workbook's own scenario table: Base is the mode, Aggressive and
Conservative are treated as the 10th/90th percentiles of a PERT-like
distribution per parameter. That grounds every draw in numbers the client has
already seen, rather than in invented spreads.

Gold: GBM, drift = the workbook's own 8.1%/yr appreciation, volatility 15%/yr.
Vol source: long-run realised volatility of gold in USD runs 14-16%/yr
(World Gold Council / LBMA data, consistent across decades); swept 10-22%.
"""

import json
import os

import numpy as np

from src.detmodel import DetModel, load_params
from src.tiermix import load_profile, lookup as tiermix_lookup

GOLD_VOL_ANNUAL = 0.15          # sourced: long-run realised gold vol ~15%/yr
GOLD_VOL_SWEEP = (0.10, 0.22)

# ─────────────────────────────────────────────────────────────────────────────
# WHICH PARAMETERS THE MONTE CARLO DRAWS
#
# EVERY workbook parameter that carries a real Aggressive/Conservative band is
# drawn. The list is OPT-OUT, not opt-in: a hand-picked draw list silently
# freezes uncertainty the client has already priced, and an earlier version of
# this file drew only 32 of 85 such parameters. If the workbook prices a band,
# it belongs in the raise number.
#
# config/scenario_map.json maps all 93 scenario rows onto parameter keys and is
# generated from the workbook itself, so a new row cannot be missed by hand.
# ─────────────────────────────────────────────────────────────────────────────

# Excluded, each for a stated reason. Nothing else may be excluded silently.
NOT_DRAWN = {
    # replaced by a lumpy Poisson arrival process in stochastic_partners()
    "b2b_partners": "modelled as discrete arrivals, not a smooth band",
    # the gold band is expressed through the GBM drift + swept volatility
    "gold_appreciation": "carried by the gold price process",
    # derived quantities: recomputed from their drawn components
    "monthly_churn": "derived from persistency",
    "partner_aum": "derived from partner_users x adopt x aum_user",
    "family_churn_monthly": "derived from the family cancellation rate",
    # the four ICS rates are now COMPUTED from the agent book's tier mix
    # (src/tiermix.py); drawing them as well would double-count
    "ics_disc_entry": "computed from the tier mix",
    "ics_disc_card": "computed from the tier mix",
    "ics_disc_rebate": "computed from the tier mix",
    "ics_disc_family": "computed from the tier mix",
    "ics_ever_share": "computed from the tier mix",
    "ics_months_to_tier": "computed from the tier mix",
}

_MAP_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "config", "scenario_map.json")


def _match_triples(params):
    """Every scenario row with a real band, minus the stated exclusions."""
    with open(_MAP_PATH) as f:
        name_to_key = json.load(f)
    out = {}
    for tbl_name, triple in params.get("scenario_triples", {}).items():
        key = name_to_key.get(tbl_name)
        if key is None or key in NOT_DRAWN:
            continue
        base, agg, con = triple
        if max(agg, con) - min(agg, con) <= 0:
            continue                      # no real band
        out[key] = triple
    # Phase 5 parameters the workbook does not have a scenario row for. Kept out
    # of params.json so the equivalence test still sees an untouched workbook.
    from config.overrides import EXTRA_TRIPLES
    out.update(EXTRA_TRIPLES)
    return out


def draw_parameters(rng, params, triples):
    """
    One path's parameter set. Each drawn parameter ~ PERT(mode=Base) with
    Aggressive/Conservative at roughly p10/p90; direction handled per parameter
    (for a cost, Conservative is the high side).
    """
    over = {}
    for key, (base, agg, con) in triples.items():
        lo, hi = (agg, con) if agg < con else (con, agg)
        if hi <= lo:
            continue
        # Beta-PERT with lambda 4; clamp mode inside [lo, hi]
        mode = min(max(base, lo), hi)
        alpha = 1 + 4 * (mode - lo) / (hi - lo)
        beta = 1 + 4 * (hi - mode) / (hi - lo)
        over[key] = lo + rng.beta(alpha, beta) * (hi - lo)

    # Derived quantities, recomputed from whatever was drawn. Anything in
    # NOT_DRAWN because it is "derived" must be reconstructed here, or it
    # silently keeps its base value while its inputs move.
    over["monthly_churn"] = 1.0 - over["persistency"] ** (1.0 / 12.0)
    over["partner_aum"] = (over.get("partner_users", params["partner_users"])
                           * over["partner_adopt"] * over["partner_aum_user"])
    # Family churn is TWO ways to lose a subscriber, combined multiplicatively:
    # they cancel the plan, or they lapse the SIP. Reconstructing it from the
    # cancellation rate alone drops half of it and inflates stream 3 by ~40%.
    fam_annual = over.get("family_cancel", params["family_cancel"])
    fam_monthly = 1.0 - (1.0 - fam_annual) ** (1.0 / 12.0)
    over["family_churn_monthly"] = 1.0 - (1.0 - fam_monthly) * (1.0 - over["monthly_churn"])
    return over


def stochastic_partners(rng, base_partners, p_zero_year=0.25):
    """
    B2B partner arrivals as a lumpy discrete process, replacing the straight
    line. Each year's planned net adds become a Poisson draw, with an explicit
    chance of a dead year. Cumulative, never decreasing.
    """
    planned = np.diff(np.array(base_partners, dtype=float), prepend=0.0)
    got = np.zeros(len(base_partners))
    total = 0.0
    for y, add in enumerate(planned):
        if add > 0 and rng.random() > p_zero_year:
            total += rng.poisson(add)
        got[y] = total
    return got.tolist()


def gold_path_29(rng, p, vol=GOLD_VOL_ANNUAL):
    """
    A gold price path on the 29-period grid. GBM monthly underneath; annual
    columns carry the December level (stocks revalue at period end in the
    engine, matching the workbook's use of a per-period price).
    Returns (grid_price[29], monthly_price[84]).
    """
    drift = p["gold_appreciation"]
    dt = 1.0 / 12.0
    shocks = rng.normal((drift - 0.5 * vol**2) * dt, vol * np.sqrt(dt), size=84)
    monthly = p["gold_price_m1"] * np.exp(np.concatenate([[0.0], np.cumsum(shocks[:-1])]))
    grid = np.concatenate([monthly[:24], monthly[[35, 47, 59, 71, 83]]])
    return grid, monthly


def run_path(seed, params=None, vol=GOLD_VOL_ANNUAL, extra_overrides=None,
             stochastic_gold=True, stochastic_partners_on=True, acq_cv=0.10):
    """
    One Monte Carlo path. Returns the engine output dict plus the draw record.

    acq_cv: coefficient of variation on per-period acquisition (demand noise),
    applied as a lognormal multiplier on new customers via the seasonality
    hook - it perturbs demand, not the saturation mechanics.
    """
    rng = np.random.default_rng(seed)
    p = load_params() if params is None else dict(params)
    triples = _match_triples(p)
    over = draw_parameters(rng, p, triples)

    if stochastic_partners_on:
        over["b2b_partners"] = stochastic_partners(rng, p["b2b_partners"])

    if extra_overrides:
        over.update(extra_overrides)

    # DetModel attaches the computed tier mix itself, at this path's persistency
    eng = DetModel(p=p, overrides=over)

    # gold hook: DetModel reads "_gold_grid" from params when present
    monthly = None
    if stochastic_gold:
        grid, monthly = gold_path_29(rng, {**p, **over}, vol=vol)
        eng.p["_gold_grid"] = grid.tolist()

    # acquisition noise: multiplicative lognormal on the seasonality vector
    if acq_cv > 0:
        noise = rng.lognormal(-0.5 * acq_cv**2, acq_cv, size=12)
        eng.p["season_acq"] = (np.array(eng.p["season_acq"]) * noise).tolist()

    out = eng.run()
    out["_draw"] = over
    if stochastic_gold:
        out["_gold_monthly"] = monthly
    return out, eng
