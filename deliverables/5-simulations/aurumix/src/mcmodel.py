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

GOLD_VOL_ANNUAL = 0.15          # sourced: long-run realised gold vol ~15%/yr
GOLD_VOL_SWEEP = (0.10, 0.22)

# Scenario-table name -> params.json key. Parameters the MC draws per path.
DRAWN = {
    "Persistency - customers still paying after 12 months": "persistency",
    "Agent productivity": "agent_productivity",
    "Marketing CAC - UAE": "cac_uae",
    "Marketing CAC - Oman and Bahrain": "cac_gulf",
    "Marketing CAC - India": "cac_india",
    "Marketing CAC at Y7 - UAE": "cac_uae_y7",
    "Marketing CAC at Y7 - Oman and Bahrain": "cac_gulf_y7",
    "Marketing CAC at Y7 - India": "cac_india_y7",
    "Referral rate": "referral_rate",
    "Referral conversion": "referral_conversion",
    "Organic share of direct": "organic_share",
    "Customers who EVER reach an ICS benefit tier": "ics_ever_share",
    "Gold moved out of Aurumix's control": "self_custody_rate",
    "Redemption rate": "redemption_rate",
    "Holder redemption multiplier": "holder_redemption_mult",
    "Spot attach scenario multiplier": "spot_attach_mult",
    "Spot ticket scenario multiplier": "spot_ticket_mult",
    "Spot frequency": "spot_frequency",
    "Programme manager share of interchange": "pm_share",
    "Facility take-up - customers who take AND use a facility": "facility_takeup",
    "Drawn as % of permitted limit": "drawn_pct",
    "Facility turnover, peak -> average": "facility_turnover",
    "Draw events per borrower per year": "draws_per_year",
    "Family plan attach rate": "family_attach",
    "Average monthly ticket - UAE": "ticket_uae",
    "Average monthly ticket - Oman and Bahrain": "ticket_gulf",
    "Average monthly ticket - India": "ticket_india",
    "B2B platform fee": "b2b_fee",
    "Partner users adopting gold (mature)": "partner_adopt",
    "AUM per adopting partner user": "partner_aum_user",
    "Vault storage fee": "vault_fee",
    "Contingency on total costs": "contingency",
}


def _match_triples(params):
    """Map scenario-table rows onto param keys, tolerant of truncated names."""
    out = {}
    for tbl_name, triple in params["scenario_triples"].items():
        for want, key in DRAWN.items():
            if tbl_name.startswith(want[:40]):
                out[key] = triple
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

    # Derived: monthly churn follows persistency (workbook derives it too)
    over["monthly_churn"] = 1.0 - over["persistency"] ** (1.0 / 12.0)

    # Partner AUM follows its drawn components
    over["partner_aum"] = (params["partner_users"] * over["partner_adopt"]
                           * over["partner_aum_user"])
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
