"""
The ICS score, the gate, the tier ladder, and the ticket distribution fit.

Blueprint Part 2, "The ICS score - COMPUTED, not looked up".

v2.6 collapsed the score to a months-since-gate lookup because Excel could not
carry the formula. That lookup put Gold at gate+12, which for a perfect payer
gating at M6 lands Gold at M18 - six months late against the rulebook's ladder.
An agent model has no such constraint, so this implements the real formula and
the discrepancy dissolves.

Everything here is vectorised over agents. No per-agent Python objects.
"""

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm, lognorm

from config import config as C


# ─────────────────────────────────────────────────────────────────────────────
# The three facts -> the three components -> the score
# ─────────────────────────────────────────────────────────────────────────────

def record(months_counted):
    """
    Record from Months. Two-segment linear, capped at 60 months.

        m x 4.1667                  m <= 12
        50 + (m - 12) x 1.04167     12 < m <= 60
        100                         m > 60

    "Your first year of payments takes you to 50; the next four take you to 100."
    Months NEVER falls - it is a historical fact about what the customer did.
    """
    m = np.asarray(months_counted, dtype=np.float64)
    early = m * C.RECORD_SLOPE_EARLY
    late = C.RECORD_AT_KINK + (m - C.RECORD_KINK_MONTH) * C.RECORD_SLOPE_LATE
    out = np.where(m <= C.RECORD_KINK_MONTH, early, late)
    return np.minimum(out, 100.0)


def standing(recent_12):
    """Standing from Recent. One straight line; each of the last 12 months equal."""
    return np.minimum(np.asarray(recent_12, dtype=np.float64) * C.STANDING_SLOPE, 100.0)


def retention(sold):
    """
    Retention from Sold. A multiplier with veto power, not a gate.

        1                            Sold <= 30%
        1 - (Sold - 30%) / 70%       Sold > 30%

    "You can take out up to a third of your gold in a year and nothing happens.
    Past that, every further 7% you sell costs you 10% of your score."

    This is what couples REDEMPTION to TIER. They are not independent.
    """
    s = np.clip(np.asarray(sold, dtype=np.float64), 0.0, 1.0)
    out = np.where(
        s <= C.RETENTION_ALLOWANCE,
        1.0,
        1.0 - (s - C.RETENTION_ALLOWANCE) / C.RETENTION_SLOPE_DENOM,
    )
    return np.clip(out, 0.0, 1.0)


def ics_score(months_counted, recent_12, sold, gated):
    """
    ICS = min(Record, Standing) x Retention, floored at 25 once gated.

    min() is the arithmetic of AND: a long record cannot cover a dead year, and
    a good year cannot cover a short record. The alternating misser's Gold cap
    is EMERGENT from this, never hard-coded.
    """
    raw = np.minimum(record(months_counted), standing(recent_12)) * retention(sold)
    scored = np.where(gated, np.maximum(raw, C.ICS_FLOOR_ONCE_GATED), 0.0)
    return np.where(gated, scored, 0.0)


def tier_index(ics):
    """
    Tier as an integer index into C.TIER_ORDER. Thresholds 25 / 50 / 75 / 100.

    A perfect payer reaches Silver M6, Gold M12, Platinum M36, Sovereign M60 -
    Record(6)=25, Record(12)=50, Record(36)=75, Record(60)=100 - which
    reproduces the rulebook's stated arrival schedule exactly.
    """
    s = np.asarray(ics, dtype=np.float64)
    idx = np.zeros(s.shape, dtype=np.int8)
    idx[s >= C.TIER_THRESHOLDS["silver"]] = 1
    idx[s >= C.TIER_THRESHOLDS["gold"]] = 2
    idx[s >= C.TIER_THRESHOLDS["platinum"]] = 3
    idx[s >= C.TIER_THRESHOLDS["sovereign"]] = 4
    return idx


# ─────────────────────────────────────────────────────────────────────────────
# The ticket distribution
# ─────────────────────────────────────────────────────────────────────────────

def fit_ticket_lognormal(target_mean, floor_share, floor=C.TICKET_FLOOR_USD):
    """
    Fit X ~ Lognormal(mu, sigma) such that, with ticket = max(floor, X):

        P(X <= floor)      = floor_share      (the mass that lands on the floor)
        E[max(floor, X)]   = target_mean

    Two constraints, two parameters. This is a FIT, not a guess - which matters,
    because the floor share is itself unsourced and the fit makes the assumption
    explicit rather than burying it in a chosen sigma.

    Returns (mu, sigma).
    """
    # P(X <= floor) = floor_share pins mu given sigma:
    #   ln(floor) = mu + sigma * z   where z = Phi^-1(floor_share)
    z = norm.ppf(floor_share)

    def mean_given_sigma(sigma):
        mu = np.log(floor) - sigma * z
        # E[max(f, X)] = f * P(X<=f) + E[X * 1(X>f)]
        # E[X * 1(X>f)] = exp(mu + s^2/2) * Phi((mu + s^2 - ln f) / s)
        tail = np.exp(mu + sigma**2 / 2) * norm.cdf((mu + sigma**2 - np.log(floor)) / sigma)
        return floor * floor_share + tail

    lo, hi = 1e-3, 3.0
    if mean_given_sigma(lo) > target_mean:
        raise ValueError(
            f"Infeasible: floor {floor} at {floor_share:.0%} already implies a mean "
            f"above {target_mean}. Lower the floor share or raise the mean."
        )
    sigma = brentq(lambda s: mean_given_sigma(s) - target_mean, lo, hi, xtol=1e-10)
    mu = np.log(floor) - sigma * z
    return mu, sigma


def draw_tickets(rng, n, target_mean, floor_share, floor=C.TICKET_FLOOR_USD):
    """Draw n ticket_base values reproducing the regional mean and floor share."""
    mu, sigma = fit_ticket_lognormal(target_mean, floor_share, floor)
    x = rng.lognormal(mean=mu, sigma=sigma, size=n)
    return np.maximum(floor, x)


def monthly_ticket(rng, ticket_base, sigma_month=None):
    """
    The declared amount this month. Variable, no maximum (rulebook sec 6.1).

    The customer CHOOSES the number on this month's request, and knows the
    floor: a saver at the USD 20 floor pays exactly 20, they do not roll a die
    and get rejected. So the declared amount is max(floor, base x noise), and
    whether they pay at all is the ARCHETYPE's job - modelling sub-floor draws
    as rejections would double-count misses against pay probabilities that were
    fitted to the persistency curve with no such channel.

    sigma_month is read from config at call time (not def time) so sweeps work.
    """
    if sigma_month is None:
        sigma_month = C.TICKET_SIGMA_MONTH
    if sigma_month <= 0.0:
        return ticket_base.copy()
    draw = ticket_base * rng.lognormal(mean=-0.5 * sigma_month**2, sigma=sigma_month,
                                       size=ticket_base.shape)
    return np.maximum(C.TICKET_FLOOR_USD, draw)


# ─────────────────────────────────────────────────────────────────────────────
# Trailing-12 window
# ─────────────────────────────────────────────────────────────────────────────

class RecentWindow:
    """
    Circular buffer of the last 12 months' counted periods, per agent.

    Recent = counted periods in the trailing 12 calendar months, 0..12. It rises
    and falls as the window rolls and is self-healing over 12 months, which is
    what replaces the old strike schedule entirely.
    """

    def __init__(self, n_agents, window=C.RECENT_WINDOW):
        self.buf = np.zeros((n_agents, window), dtype=np.uint8)
        self.window = window
        self.pos = 0

    def push(self, counted):
        """Write this month's counted flag and advance the cursor."""
        self.buf[:, self.pos] = counted.astype(np.uint8)
        self.pos = (self.pos + 1) % self.window

    def recent(self):
        return self.buf.sum(axis=1)

    def grow(self, n_new):
        """Extend for newly acquired agents; their window starts empty."""
        if n_new <= 0:
            return
        self.buf = np.vstack([self.buf, np.zeros((n_new, self.window), dtype=np.uint8)])
