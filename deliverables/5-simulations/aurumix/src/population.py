"""
The Stage 1 monthly loop: pay/miss -> streak -> gate -> score -> tier.

Blueprint Part 2, "Order within a step". Stage 1 runs a single cohort so the
lifecycle can be measured cleanly against v2.6's published figures; Stage 2
wraps this in acquisition, revenue and cost.
"""

import numpy as np

from config import config as C
from src import mechanics as M
from src.entities import build_cohort


def step(pool, month, rng, redemption_on=True, gold_price=C.GOLD_PRICE_M1):
    """
    Advance one month. Order matters and follows the blueprint.

    A miss resets the streak to zero. That single line is why gate arrival is a
    distribution rather than a date: a customer who misses month 4 cannot gate
    before month 9.
    """
    live = pool.alive & pool.sip_active

    # ── 1. does the customer intend to pay this month? ───────────────────────
    age = np.maximum(month - pool.born_month, 0)
    p = np.maximum(pool.pay_prob0 * pool.pay_decay ** age, pool.pay_floor)
    intends = live & (rng.random(pool.n) < p)

    # ── 2. how much? the customer chooses, floored at USD 20 ─────────────────
    amount = M.monthly_ticket(rng, pool.ticket_base)
    counted = intends

    # ── 3. streak, gate ──────────────────────────────────────────────────────
    pool.streak = np.where(counted, np.minimum(pool.streak + 1, C.GATE_RUN), 0).astype(np.int8)
    newly_gated = (~pool.gated) & (pool.streak >= C.GATE_RUN)
    pool.gate_month[newly_gated] = month
    pool.gated |= newly_gated

    # Months starts at 6 on the day the gate opens, then rises by 1 per counted
    # period. It NEVER falls, for any reason (_draft_ics-scoring.md sec 1.1).
    pool.months_counted[newly_gated] = C.GATE_RUN
    post_gate = counted & pool.gated & ~newly_gated
    pool.months_counted[post_gate] += 1

    # ── 4. the trailing-12 window ────────────────────────────────────────────
    pool.recent.push(counted)

    # ── 5. gold in ───────────────────────────────────────────────────────────
    bought = amount * (1.0 - C.ENTRY_FEE) / gold_price
    pool.grams += np.where(counted, bought, 0.0)
    pool.grams_acquired_ytd += np.where(counted, bought, 0.0)

    # ── 6. gold out — this is what couples redemption to tier via Retention ──
    if redemption_on:
        holders = pool.alive & ~pool.sip_active
        rate = np.where(holders,
                        C.REDEMPTION_RATE_ANNUAL * C.HOLDER_REDEMPTION_MULTIPLIER,
                        C.REDEMPTION_RATE_ANNUAL) / 12.0
        pool.grams = np.maximum(0.0, pool.grams - pool.grams * rate * pool.alive)

    # ── 7. the score ─────────────────────────────────────────────────────────
    denom = pool.grams_year_open + pool.grams_acquired_ytd
    sold = np.where(denom > 0, 1.0 - pool.grams / np.maximum(denom, 1e-12), 0.0)
    pool.ics = M.ics_score(pool.months_counted, pool.recent.recent(), sold, pool.gated)
    pool.tier = M.tier_index(pool.ics)

    # roll the Retention denominator once a year
    if month % 12 == 0:
        pool.grams_year_open = pool.grams.copy()
        pool.grams_acquired_ytd[:] = 0.0

    # ── 8. attrition — SIP lapse. The customer keeps their gold and their card ─
    lapsing = live & (rng.random(pool.n) < pool.hazard)
    pool.sip_active &= ~lapsing

    return {
        "month": month,
        "paying": int((pool.alive & pool.sip_active).sum()),
        "holders": int((pool.alive & ~pool.sip_active).sum()),
        "gated": int(pool.gated.sum()),
        "counted": int(counted.sum()),
        "contributions": float(np.where(counted, amount, 0.0).sum()),
        "grams": float(pool.grams.sum()),
        "tier_counts": np.bincount(pool.tier[pool.alive], minlength=5).tolist(),
    }


def run_cohort(n=200_000, months=C.HORIZON_MONTHS, seed=20270101,
               archetypes=None, background=None, redemption_on=True,
               prefunded_share=C.RAIL_PREFUNDED_SHARE,
               discipline_shift=C.RAIL_DISCIPLINE_SHIFT,
               ticket_sigma=C.TICKET_SIGMA_MONTH, region_idx=0):
    """Run one acquisition cohort for `months` and return (pool, history)."""
    archetypes = archetypes or C.ARCHETYPES_BASE
    background = C.BACKGROUND_HAZARD["base"] if background is None else background

    rng = np.random.default_rng(seed)
    pool = build_cohort(rng, n, archetypes, background, region_idx=region_idx,
                        born_month=1, prefunded_share=prefunded_share,
                        discipline_shift=discipline_shift)

    prev_sigma = C.TICKET_SIGMA_MONTH
    C.TICKET_SIGMA_MONTH = ticket_sigma
    try:
        history = [step(pool, m, rng, redemption_on=redemption_on)
                   for m in range(1, months + 1)]
    finally:
        C.TICKET_SIGMA_MONTH = prev_sigma

    return pool, history
