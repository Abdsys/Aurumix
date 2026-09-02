"""
Invariants, asserted every step of every path.

Blueprint Part 4.4. These are the properties that must hold no matter what the
parameters do. An invariant that fires is a bug, never a finding.
"""

import numpy as np

from config import config as C
from src import mechanics as M


class InvariantError(AssertionError):
    pass


def check(pool, prev_months_counted=None):
    """Run every Stage 1 invariant against the pool. Raises on the first failure."""
    fails = []

    # 4 - streak bounds; gated is permanent
    if not ((pool.streak >= 0) & (pool.streak <= C.GATE_RUN)).all():
        fails.append("streak left [0, 6]")

    # 5 - months_counted never decreases, for any reason
    if prev_months_counted is not None:
        if (pool.months_counted < prev_months_counted).any():
            fails.append("months_counted decreased - it is a historical fact and cannot fall")

    # 5a - the score is exactly the formula, and floored at 25 once gated
    denom = pool.grams_year_open + pool.grams_acquired_ytd
    sold = np.where(denom > 0, 1.0 - pool.grams / np.maximum(denom, 1e-12), 0.0)
    expect = M.ics_score(pool.months_counted, pool.recent.recent(), sold, pool.gated)
    if not np.allclose(pool.ics, expect, atol=1e-9):
        fails.append("ics != min(Record, Standing) x Retention")
    if (pool.gated & (pool.ics < C.ICS_FLOOR_ONCE_GATED - 1e-9)).any():
        fails.append("a gated agent scored below the floor of 25")
    if ((~pool.gated) & (pool.ics > 0)).any():
        fails.append("an ungated agent carries a score")

    # 5c - an agent whose Recent never exceeds 6 must never exceed Gold.
    #      Emergent from min(), never hard-coded - so it is worth asserting.
    rec = pool.recent.recent()
    capped = pool.gated & (rec <= 6)
    if (pool.tier[capped] > 2).any():
        fails.append("an agent with Recent <= 6 exceeded Gold - min() is not binding")

    # 5d - amount never affects score
    if (pool.tier > 0).any():
        tiered = pool.tier > 0
        if np.corrcoef(pool.ticket_base[tiered], pool.ics[tiered])[0, 1] > 0.05:
            fails.append("ticket size correlates with score - amount must be irrelevant")

    # gold is never negative
    if (pool.grams < -1e-9).any():
        fails.append("negative grams")

    if fails:
        raise InvariantError("; ".join(fails))


def check_clean_climb():
    """
    5b - Standing >= Record at every month of a clean climb.

    "For a saver who never misses, Standing never binds." The score of a good
    customer is purely their Record, and Standing only appears when something
    has gone wrong. Verified in _draft_ics-scoring.md sec 7.4; asserted here
    because it is the one property the formula has to prove.
    """
    m = np.arange(1, 121)
    rec = M.record(np.maximum(m, 0))
    stand = M.standing(np.minimum(m, 12))
    bad = m[(stand < rec - 1e-9) & (m >= 6)]
    if bad.size:
        raise InvariantError(f"Standing binds a clean saver at months {bad.tolist()[:8]}")
    return True
