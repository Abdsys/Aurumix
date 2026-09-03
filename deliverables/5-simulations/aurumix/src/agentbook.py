"""
The agent book: the Stage 1 population under continuous acquisition, carrying
per-agent economics - the layer the workbook cannot have.

Answers: the tier mix over time, the ICS ladder cost matrix (tier x benefit),
profit concentration by ticket decile, the rho_quality clustering sweep, and
the rail-mix lever. One sim agent stands for `scale` customers.

The benefit ladder is the blueprint's Part 2 table:
    entry fee paid   5.00 / 4.50 / 4.00 / 3.50 / 3.00 %
    family discount     0 /   10 /   20 /   35 /   50 %
    card FX charged   2.0 /  2.0 /  1.5 / 1.25 /  1.0 %
    credit LTV         50 /   50 /   65 / 72.5 /   80 %
    gold rewards        0 / 0.15 / 0.45 / 0.60 / 0.75 % of card spend
Decision 6: rewards paid to an agent never exceed the revenue that agent
generated - enforceable only at agent level.
"""

import numpy as np

from config import config as C
from src import mechanics as M
from src.entities import build_cohort, AgentPool
from src.detmodel import DetModel

# tier index: 0 none, 1 silver, 2 gold, 3 platinum, 4 sovereign
# ─────────────────────────────────────────────────────────────────────────────
# WHO REFERS
#
# The workbook's referral term is  paying_base x rate/12 x conversion. It gives
# a month-two customer the same voice as a three-year Platinum holder. Two
# corrections, both in the same direction and both structural rather than fitted:
#
#   1. Tenure. Nobody recommends a savings plan in the first quarter. Propensity
#      is zero for three months, then ramps to full by month twelve - roughly the
#      point at which the first year's discipline is visible to the customer.
#   2. Tier. Advocacy tracks what the plan has actually delivered. The ladder
#      already says who got the most; these are the relative referral rates.
#
# Both are judgement, not measurement, and are declared as such. The net effect
# is a multiplier on the workbook's referral term, NORMALISED so that a matured
# book returns 1.0 - see tiermix.py. That keeps `referral_rate` meaning what it
# most likely meant when it was quoted: the rate on an established book, not on
# a book that is 80% new joiners.
REF_TENURE_DEAD = 3        # months before anyone refers
REF_TENURE_FULL = 12       # months to full propensity
REFERRAL_TIER_MULT = np.array([1.00, 1.15, 1.30, 1.50, 1.75])

LADDER = {
    "entry_fee":  np.array([0.050, 0.045, 0.040, 0.035, 0.030]),
    "family_disc": np.array([0.00, 0.10, 0.20, 0.35, 0.50]),
    "fx_margin":  np.array([0.020, 0.020, 0.015, 0.0125, 0.010]),
    "ltv":        np.array([0.50, 0.50, 0.65, 0.725, 0.80]),
    "rewards":    np.array([0.000, 0.0015, 0.0045, 0.0060, 0.0075]),
}


def make_ladder(ceiling_pp=2.0, steepness="linear", breadth=None):
    """
    Generate the 4x5 ladder from the three sweep dials (blueprint sec 5.5).
    ceiling_pp: entry-fee points off base at the top tier (1.0 / 1.5 / 2.0).
    steepness: convex (top-loaded, cheap) | linear | concave (early, expensive).
    breadth: set of benefit names that are laddered; others stay flat at base.
    """
    frac = {"convex": np.array([0, .1, .3, .6, 1.0]),
            "linear": np.array([0, .25, .5, .75, 1.0]),
            "concave": np.array([0, .5, .75, .9, 1.0])}[steepness]
    lad = {}
    lad["entry_fee"] = 0.05 - frac * ceiling_pp / 100.0
    lad["family_disc"] = frac * 0.50
    lad["fx_margin"] = 0.02 - frac * 0.01
    lad["ltv"] = 0.50 + frac * 0.30
    lad["rewards"] = frac * 0.0075
    if breadth is not None:
        for k in lad:
            if k not in breadth:
                lad[k] = np.full(5, {"entry_fee": 0.05, "family_disc": 0.0,
                                     "fx_margin": 0.02, "ltv": 0.50,
                                     "rewards": 0.0}[k])
    return lad


def run_book(seed=20270101, scale=2.0, months=C.HORIZON_MONTHS,
             prefunded_share=C.RAIL_PREFUNDED_SHARE,
             discipline_shift=C.RAIL_DISCIPLINE_SHIFT,
             rho_quality=0.0, ladder=None, archetypes=None,
             region_weights=None, card_dormancy_monthly=0.0):
    """
    Run the full 84-month book with continuous acquisition. Acquisition per
    month comes from the ported deterministic engine's own new-customer series,
    so the agent book and the workbook describe the same company.

    rho_quality: a single latent factor. Each agent draws q ~ N(0,1); with
    loading rho, q shifts card spend, spot propensity, family attach and
    redemption in the SAME direction as their payment discipline. 0 = today's
    independent model.

    Returns (pool, panel) where panel holds monthly aggregates and per-agent
    annual economics at the horizon.
    """
    rng = np.random.default_rng(seed)
    ladder = ladder or LADDER
    p = DetModel().p
    det = DetModel()
    det.run()

    # monthly new customers per region off the det engine (annual cols / 12)
    grid_new = {n: det.out["region"][n]["new"] for n in ("UAE", "Gulf", "India")}
    months_in = np.array(p["grid"]["months"], dtype=int)
    monthly_new = {n: [] for n in grid_new}
    for i, m in enumerate(months_in):
        for n in grid_new:
            monthly_new[n].extend([grid_new[n][i] / m] * m)

    arche_by_region = archetypes or C.ARCHETYPES_BASE
    pools = []
    panel = []

    pool = None
    for t in range(1, months + 1):
        # ── acquire ──────────────────────────────────────────────────────────
        for ri, name in enumerate(("UAE", "Gulf", "India")):
            n_new = int(round(monthly_new[name][t - 1] / scale))
            if n_new <= 0:
                continue
            cohort = build_cohort(rng, n_new, arche_by_region,
                                  C.BACKGROUND_HAZARD["base"], region_idx=ri,
                                  born_month=t, prefunded_share=prefunded_share,
                                  discipline_shift=discipline_shift,
                                  ticket_mean=[33.60, 26.00, 30.00][ri])
            pool = cohort if pool is None else _merge(pool, cohort)

        if pool is None:
            continue

        # quality factor, drawn once per agent. With rho_quality > 0 it is
        # CORRELATED WITH TICKET by a Gaussian-copula partial reorder within the
        # new cohort - ticket is an income proxy, and the latent factor loads on
        # income like everything else. Marginals are untouched.
        if not hasattr(pool, "quality") or pool.quality.shape[0] != pool.n:
            q_old = getattr(pool, "quality", np.empty(0))
            n_new_agents = pool.n - q_old.shape[0]
            q_new = rng.normal(size=n_new_agents)
            if rho_quality > 0 and n_new_agents > 1:
                sl = slice(pool.n - n_new_agents, pool.n)
                t_rank = np.argsort(np.argsort(pool.ticket_base[sl]))
                z_ticket = (t_rank + 0.5) / n_new_agents
                z_ticket = np.clip(z_ticket, 1e-6, 1 - 1e-6)
                from scipy.stats import norm as _norm
                q_new = (rho_quality * _norm.ppf(z_ticket)
                         + np.sqrt(1 - rho_quality**2) * q_new)
            pool.quality = np.concatenate([q_old, q_new])

        # ── the Stage 1 month ────────────────────────────────────────────────
        live = pool.alive & pool.sip_active
        age = np.maximum(t - pool.born_month, 0)
        pay_p = np.maximum(pool.pay_prob0 * pool.pay_decay ** age, pool.pay_floor)
        if rho_quality > 0:
            # tilt pay probability with the latent factor, renormalised
            pay_p = np.clip(pay_p + rho_quality * 0.05 * pool.quality, 0.01, 0.999)
        counted = live & (rng.random(pool.n) < pay_p)

        amount = M.monthly_ticket(rng, pool.ticket_base)
        pool.streak = np.where(counted, np.minimum(pool.streak + 1, C.GATE_RUN), 0).astype(np.int8)
        newly = (~pool.gated) & (pool.streak >= C.GATE_RUN)
        pool.gate_month[newly] = t
        pool.gated |= newly
        pool.months_counted[newly] = C.GATE_RUN
        pool.months_counted[counted & pool.gated & ~newly] += 1
        pool.recent.push(counted)

        contrib = np.where(counted, amount, 0.0)
        entry_rate = ladder["entry_fee"][pool.tier]
        bought = contrib * (1 - entry_rate) / C.GOLD_PRICE_M1
        pool.grams += bought
        pool.grams_acquired_ytd += bought

        # redemption; quality tilts it DOWN for good agents
        red = C.REDEMPTION_RATE_ANNUAL / 12 * np.where(pool.sip_active, 1.0,
                                                       C.HOLDER_REDEMPTION_MULT
                                                       if hasattr(C, "HOLDER_REDEMPTION_MULT")
                                                       else C.HOLDER_REDEMPTION_MULTIPLIER)
        if rho_quality > 0:
            red = np.clip(red * (1 - 0.5 * rho_quality * pool.quality), 0.0, 1.0)
        pool.grams *= (1 - red * pool.alive)

        denom = pool.grams_year_open + pool.grams_acquired_ytd
        sold = np.where(denom > 0, 1 - pool.grams / np.maximum(denom, 1e-12), 0.0)
        pool.ics = M.ics_score(pool.months_counted, pool.recent.recent(), sold, pool.gated)
        pool.tier = M.tier_index(pool.ics)
        if t % 12 == 0:
            pool.grams_year_open = pool.grams.copy()
            pool.grams_acquired_ytd[:] = 0.0

        lapse = live & (rng.random(pool.n) < pool.hazard)
        pool.sip_active &= ~lapse

        # ── economics this month, per agent ──────────────────────────────────
        if not hasattr(pool, "econ"):
            pool.econ = {}
        _ensure(pool, "rev_entry"); _ensure(pool, "rev_card"); _ensure(pool, "rev_family")
        _ensure(pool, "cost_ics"); _ensure(pool, "rev_spot"); _ensure(pool, "card_spend")
        _ensure(pool, "contrib_total")

        pool.econ["rev_entry"] += contrib * entry_rate
        pool.econ["contrib_total"] += contrib

        # cards: open to the whole book; take-up as a one-time draw at t>=13
        if t >= int(p["act_2"]):
            if not hasattr(pool, "card_drawn_flag"):
                pool.card_drawn_flag = np.zeros(pool.n, dtype=bool)
            if pool.card_drawn_flag.shape[0] != pool.n:
                pool.card_drawn_flag = np.concatenate(
                    [pool.card_drawn_flag,
                     np.zeros(pool.n - pool.card_drawn_flag.shape[0], dtype=bool)])
            fresh = pool.alive & ~pool.card_active & ~pool.card_drawn_flag
            take = p["facility_takeup"]
            if rho_quality > 0:
                take = np.clip(take * (1 + 0.4 * rho_quality * pool.quality), 0, 1)
                got = fresh & (rng.random(pool.n) < take)
            else:
                got = fresh & (rng.random(pool.n) < take)
            pool.card_active |= got
            pool.card_drawn_flag |= fresh
            # Card dormancy - an INDEPENDENT clock from SIP lapse (blueprint
            # Q9). Researched 2026-09-02 via Perplexity: no published dormancy
            # or attrition RATE exists for consumer cards - UAE, GCC, global or
            # fintech - only inactivity DEFINITIONS (90 days to 12 months).
            # Confirmed sourcing negative; carried as a swept assumption.
            dorm = card_dormancy_monthly
            if dorm > 0:
                gone = pool.card_active & (rng.random(pool.n) < dorm)
                pool.card_active &= ~gone

            # card spend keyed to ticket as income proxy, at the tier's FX/rewards
            limit = pool.grams * C.GOLD_PRICE_M1 * ladder["ltv"][pool.tier]
            spend = np.where(pool.card_active & pool.alive,
                             limit * p["drawn_pct"] * p["draws_per_year"] / 12, 0.0)
            if rho_quality > 0:
                spend *= np.clip(1 + 0.3 * rho_quality * pool.quality, 0.2, 3.0)
            pool.econ["card_spend"] += spend
            ic = p["interchange"] * (1 - p["pm_share"])
            fx = ladder["fx_margin"][pool.tier] * p["foreign_spend_mean"]
            card_rev = spend * (ic + fx)
            pool.econ["rev_card"] += card_rev
            # rewards, capped per agent at revenue generated (decision 6)
            reward = spend * ladder["rewards"][pool.tier]
            cap = (pool.econ["rev_entry"] + pool.econ["rev_card"]
                   + pool.econ["rev_family"] - pool.econ["cost_ics"])
            reward = np.minimum(reward, np.maximum(cap, 0.0))
            pool.econ["cost_ics"] += reward

        # family plan on the fixed attach; discounted by tier
        fam_price = (p["family_price"] + max(0.0, p["beneficiaries"] - 1)
                     * p["beneficiary_fee"]) / 12
        if t >= int(p["act_3"]):
            if not hasattr(pool, "family_flag"):
                pool.family_flag = np.zeros(pool.n, dtype=bool)
            if pool.family_flag.shape[0] != pool.n:
                pool.family_flag = np.concatenate(
                    [pool.family_flag,
                     np.zeros(pool.n - pool.family_flag.shape[0], dtype=bool)])
            newagents = pool.born_month == t
            att = p["family_attach"]
            join = newagents & (rng.random(pool.n) < att)
            pool.family_flag |= join
            # subscribers churn at the workbook's combined monthly rate
            cancel = pool.family_flag & (rng.random(pool.n) < p["family_churn_monthly"])
            pool.family_flag &= ~cancel
            fam_rev = np.where(pool.family_flag & pool.alive,
                               fam_price * (1 - ladder["family_disc"][pool.tier]), 0.0)
            disc = np.where(pool.family_flag & pool.alive,
                            fam_price * ladder["family_disc"][pool.tier], 0.0)
            pool.econ["rev_family"] += fam_rev
            pool.econ["cost_ics"] += disc

        # entry-fee discount vs the 5% base is ICS cost
        pool.econ["cost_ics"] += contrib * (0.05 - entry_rate)

        # ── monthly aggregates ───────────────────────────────────────────────
        alive = pool.alive
        # Referral capacity. The workbook refers off the raw paying head count,
        # so a customer in month two counts as much as one in year three. They
        # do not: you cannot recommend a savings plan you have barely started,
        # and advocacy rises with what the plan has actually given you.
        payers = alive & pool.sip_active
        ramp = np.clip((t - pool.born_month - REF_TENURE_DEAD)
                       / float(REF_TENURE_FULL - REF_TENURE_DEAD), 0.0, 1.0)
        w = ramp * REFERRAL_TIER_MULT[pool.tier]
        panel.append({
            "month": t,
            "paying": int(payers.sum()) * scale,
            "holders": int((alive & ~pool.sip_active).sum()) * scale,
            "tier_mix": np.bincount(pool.tier[alive], minlength=5) * scale,
            "gated_share": float(pool.gated[alive].mean()) if alive.any() else 0.0,
            "ref_weight": float(w[payers].sum()) * scale,
        })

    return pool, panel, scale


def _ensure(pool, key):
    if key not in pool.econ:
        pool.econ[key] = np.zeros(pool.n)
    elif pool.econ[key].shape[0] != pool.n:
        pool.econ[key] = np.concatenate(
            [pool.econ[key], np.zeros(pool.n - pool.econ[key].shape[0])])


def _merge(a: AgentPool, b: AgentPool) -> AgentPool:
    """Append cohort b to pool a."""
    import numpy as _np
    kw = {}
    for f in ("region", "archetype", "rail", "door", "born_month", "ticket_base",
              "pay_prob0", "pay_decay", "pay_floor", "hazard", "months_counted",
              "streak", "gated", "grams", "grams_year_open", "grams_acquired_ytd",
              "sip_active", "card_active", "alive", "ics", "tier"):
        kw[f] = _np.concatenate([getattr(a, f), getattr(b, f)])
    out = AgentPool(**kw)
    out.recent = a.recent
    out.recent.grow(b.n)
    out.gate_month = _np.concatenate([a.gate_month, b.gate_month])
    for attr in ("quality", "card_drawn_flag", "family_flag"):
        if hasattr(a, attr):
            setattr(out, attr, getattr(a, attr))
    if hasattr(a, "econ"):
        out.econ = a.econ
    return out
