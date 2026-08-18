"""ICS scoring engine, exactly per _draft_ics-scoring.md.

    Record    = 100/24 * M           for M <= 12          (-> 50 at M=12)
                50 + 100/96 * (M-12) for 12 < M <= 60     (-> 100 at M=60)
                100                  for M > 60
    Standing  = 100/12 * Recent
    Retention = 1                       if Sold <= 30%
                1 - (Sold-30%)/70%      if Sold > 30%
    ICS       = MAX(25, MIN(Record, Standing) * Retention)   [once gated]
    Tier      = lower-bound lookup at 25 / 50 / 75 / 100

EXACT FRACTIONS ARE LOAD-BEARING. With the rounded 8.3333, Standing at
Recent=6 is 49.9998, which falls below the Gold threshold of 50 and silently
misplaces the entire alternating-misser population (12% of the book) into
Silver. Fraction arithmetic makes it exactly 50.

Three mechanisms beyond the bare formula:
  - pre-gate run counter (0-6, an integer, NOT a score)
  - regulatory-block clock freeze: frozen months are skipped entirely and the
    trailing window EXTENDS to reach 12 countable months
  - the floor applies only after the gate; before it there is no score at all
"""
from __future__ import annotations

from fractions import Fraction

from params import (GATE_RUN_REQUIRED, ICS_FLOOR, RECENT_WINDOW, RECORD_CAP,
                    RECORD_SLOPE_EARLY, RECORD_SLOPE_LATE, RETENTION_SLOPE_DENOM,
                    STANDING_CAP, STANDING_SLOPE, TIER_THRESHOLDS,
                    WITHDRAWAL_ALLOWANCE)


def record(months: int) -> Fraction:
    """Tenure component. Never falls, for any reason."""
    if months <= 0:
        return Fraction(0)
    if months <= 12:
        return RECORD_SLOPE_EARLY * months
    if months <= 60:
        return Fraction(50) + RECORD_SLOPE_LATE * (months - 12)
    return Fraction(RECORD_CAP)


def standing(recent: int) -> Fraction:
    """Present-tense component: 100/12 x countable payments in the last 12."""
    return min(Fraction(STANDING_CAP), STANDING_SLOPE * max(0, recent))


def retention(sold: float) -> Fraction:
    """Multiplier with veto power. Flat 1.000 up to the 30% allowance."""
    s = Fraction(sold).limit_denominator(10**9)
    if s <= Fraction(WITHDRAWAL_ALLOWANCE).limit_denominator(100):
        return Fraction(1)
    r = Fraction(1) - (s - Fraction(30, 100)) / Fraction(RETENTION_SLOPE_DENOM
                                                         ).limit_denominator(100)
    return max(Fraction(0), r)


def sold_ratio(grams_now: float, grams_12m_ago: float, grams_acquired: float) -> float:
    """Sold = 1 - held_now / (held_12m_ago + acquired_since).

    Timing-neutral by construction. Denominator zero -> Sold = 0 (a customer
    with nothing cannot have sold anything).
    """
    denom = grams_12m_ago + grams_acquired
    if denom <= 0:
        return 0.0
    return max(0.0, min(1.0, 1.0 - grams_now / denom))


def ics_score(months: int, recent: int, sold: float, gated: bool = True) -> Fraction | None:
    """None means no score at all - the pre-gate state (persona H)."""
    if not gated:
        return None
    raw = min(record(months), standing(recent)) * retention(sold)
    return max(Fraction(ICS_FLOOR), raw)


def tier_of(score: Fraction | None) -> str:
    if score is None:
        return "None"
    for threshold, name in TIER_THRESHOLDS:
        if score >= threshold:
            return name
    return "None"


class ICSAccount:
    """Deterministic ICS state machine for one behavioural track.

    Tracks the two clocks (Months, Recent) plus the pre-gate run counter.
    Both clocks advance on COUNTABLE months only; a frozen month is skipped
    entirely, as though it never existed, and the Recent window extends to
    reach 12 countable months.
    """

    def __init__(self):
        self.run_length = 0          # 0-6, pre-gate. An integer, not a score.
        self.gated = False
        self.months = 0              # countable periods since the gate opened
        self.payment_history: list[bool] = []   # countable months only
        self.silent_periods = 0
        self.dormant = False

    def step(self, paid: bool, frozen: bool = False) -> None:
        """Advance one calendar period."""
        if frozen:
            # Neither clock advances. The run freezes but never breaks.
            return
        if self.dormant:
            return

        if paid:
            self.silent_periods = 0
        else:
            self.silent_periods += 1
            if self.silent_periods >= 12:
                self.dormant = True

        if not self.gated:
            # Pre-gate: track the current run length, reset on a miss.
            self.run_length = self.run_length + 1 if paid else 0
            if self.run_length >= GATE_RUN_REQUIRED:
                # Gate fires. Months and Recent are 6 and 6 by construction.
                self.gated = True
                self.months = GATE_RUN_REQUIRED
                self.payment_history = [True] * GATE_RUN_REQUIRED
            return

        # Post-gate: Months never falls; Recent is a trailing-12 count.
        self.months += 1
        self.payment_history.append(paid)

    @property
    def recent(self) -> int:
        return sum(self.payment_history[-RECENT_WINDOW:])

    def score(self, sold: float = 0.0) -> Fraction | None:
        return ics_score(self.months, self.recent, sold, self.gated)

    def tier(self, sold: float = 0.0) -> str:
        """Memoised on (months, recent, gated, sold).

        Exact-fraction arithmetic is the inner loop of the monthly tier scan
        (O(vintages x tracks) per period). The state only changes on step(), so
        caching is safe and does not alter any result - the same inputs return
        the same exact Fraction-derived tier.
        """
        key = (self.months, self.recent, self.gated, sold)
        cached = _TIER_CACHE.get(key)
        if cached is not None:
            return cached
        val = tier_of(self.score(sold))
        _TIER_CACHE[key] = val
        return val


# Module-level memo shared across accounts: the tier is a pure function of
# (months, recent, gated, sold), so identical states resolve identically.
_TIER_CACHE: dict = {}


# ---------------------------------------------------------------------------
# Persona validation set A-I (_draft_ics-scoring.md 7.1)
# ---------------------------------------------------------------------------

PERSONAS = {
    "A": dict(desc="USD 20/mo, perfect, never sells, month 60",
              months=60, recent=12, sold=0.0, gated=True,
              exp_record=100, exp_standing=100, exp_ret=1.00,
              exp_ics=100, exp_tier="Sovereign"),
    "B": dict(desc="As A but missed one month in the last year",
              months=59, recent=11, sold=0.0, gated=True,
              exp_record=99.0, exp_standing=91.7, exp_ret=1.00,
              exp_ics=91.7, exp_tier="Platinum"),
    "C": dict(desc="USD 2,000/mo, perfect, never sells, month 60",
              months=60, recent=12, sold=0.0, gated=True,
              exp_record=100, exp_standing=100, exp_ret=1.00,
              exp_ics=100, exp_tier="Sovereign"),
    "D": dict(desc="Cycler: contributes and redeems every month",
              months=60, recent=12, sold=1.0, gated=True,
              exp_record=100, exp_standing=100, exp_ret=0.0,
              exp_ics=25, exp_tier="Silver"),
    "E": dict(desc="Withdrew half at month 36, kept saving",
              months=36, recent=12, sold=0.50, gated=True,
              exp_record=75, exp_standing=100, exp_ret=0.714,
              exp_ics=53.6, exp_tier="Gold"),
    "F": dict(desc="Withdrew everything at month 36, kept saving",
              months=36, recent=12, sold=1.0, gated=True,
              exp_record=75, exp_standing=100, exp_ret=0.0,
              exp_ics=25, exp_tier="Silver"),
    "G": dict(desc="Withdrew 30% at month 36 (inside the allowance)",
              months=36, recent=12, sold=0.30, gated=True,
              exp_record=75, exp_standing=100, exp_ret=1.00,
              exp_ics=75, exp_tier="Platinum"),
    "H": dict(desc="Scattered payer: 6 payments over 3 years, never 6 in a row",
              months=6, recent=2, sold=0.0, gated=False,
              exp_record=None, exp_standing=None, exp_ret=None,
              exp_ics=None, exp_tier="None"),
    "I": dict(desc="Late opener: paid 1-3, missed 4, paid 5-7, missed 8, ran 9-14",
              months=6, recent=6, sold=0.0, gated=True,
              exp_record=25, exp_standing=50, exp_ret=1.00,
              exp_ics=25, exp_tier="Silver"),
}


def validate_personas(tol: float = 0.05) -> list[dict]:
    """Reproduce all nine personas. H and I are the rows a naive build fails."""
    results = []
    for key, p in PERSONAS.items():
        if not p["gated"]:
            got_ics, got_tier = None, tier_of(None)
            got_rec = got_std = got_ret = None
            ok = (got_tier == p["exp_tier"])
        else:
            rec = record(p["months"])
            std = standing(p["recent"])
            ret = retention(p["sold"])
            sc = ics_score(p["months"], p["recent"], p["sold"], True)
            got_rec, got_std = float(rec), float(std)
            got_ret, got_ics = float(ret), float(sc)
            got_tier = tier_of(sc)
            ok = (abs(got_ics - p["exp_ics"]) <= tol
                  and got_tier == p["exp_tier"]
                  and abs(got_rec - p["exp_record"]) <= tol
                  and abs(got_std - p["exp_standing"]) <= tol
                  and abs(got_ret - p["exp_ret"]) <= 0.001)
        results.append({
            "persona": key, "description": p["desc"],
            "exp_ics": p["exp_ics"], "got_ics": got_ics,
            "exp_tier": p["exp_tier"], "got_tier": got_tier,
            "got_record": got_rec, "got_standing": got_std, "got_retention": got_ret,
            "pass": ok,
        })
    return results


def validate_gate_mechanics() -> list[dict]:
    """Behavioural checks the closed-form persona table cannot express."""
    out = []

    # Persona I as a live path: paid 1-3, missed 4, paid 5-7, missed 8, ran 9-14.
    a = ICSAccount()
    for paid in [True, True, True, False, True, True, True, False] + [True] * 6:
        a.step(paid)
    out.append({"check": "Persona I gate fires at M14 with Months=6, Recent=6",
                "expected": "gated=True months=6 recent=6 tier=Silver",
                "got": f"gated={a.gated} months={a.months} recent={a.recent} "
                       f"tier={a.tier(0.0)}",
                "pass": a.gated and a.months == 6 and a.recent == 6
                        and a.tier(0.0) == "Silver"})

    # Persona H: 6 payments over 3 years, never 6 consecutive -> never gated.
    h = ICSAccount()
    pattern = ([True, False, False, False, False, False] * 6)[:36]
    for paid in pattern:
        h.step(paid)
    out.append({"check": "Persona H never gates (no score, no tier, ever)",
                "expected": "gated=False tier=None",
                "got": f"gated={h.gated} tier={h.tier(0.0)}",
                "pass": (not h.gated) and h.tier(0.0) == "None"})

    # Regulatory block: a saver at 4-of-6 resumes at 4-of-6.
    f = ICSAccount()
    for _ in range(4):
        f.step(True)
    before = f.run_length
    for _ in range(6):
        f.step(False, frozen=True)
    out.append({"check": "Regulatory block freezes the pre-gate run (4-of-6 resumes at 4-of-6)",
                "expected": "run_length=4 after 6 frozen months",
                "got": f"run_length={f.run_length} (was {before})",
                "pass": f.run_length == 4})

    # Frozen months do not advance Months/Recent post-gate.
    g = ICSAccount()
    for _ in range(6):
        g.step(True)
    m_before = g.months
    for _ in range(12):
        g.step(True, frozen=True)
    out.append({"check": "Frozen months are skipped entirely on both clocks",
                "expected": f"months unchanged at {m_before}",
                "got": f"months={g.months}",
                "pass": g.months == m_before})

    # Dormancy is a hard absorbing boundary at 12 consecutive silent periods.
    d = ICSAccount()
    for _ in range(6):
        d.step(True)
    for _ in range(12):
        d.step(False)
    out.append({"check": "Dormancy absorbs at 12 consecutive silent periods",
                "expected": "dormant=True",
                "got": f"dormant={d.dormant} silent={d.silent_periods}",
                "pass": d.dormant})

    # The exact-fraction check: Standing at Recent=6 must be exactly 50 (Gold),
    # not 49.9998 (Silver). This is the alternating misser's permanent cell.
    std6 = standing(6)
    naive = 8.3333 * 6
    out.append({"check": "Exact fractions: Standing(Recent=6) reaches Gold, not Silver",
                "expected": "Standing=50 exactly -> Gold",
                "got": f"exact={float(std6)} (naive 8.3333x6={naive:.4f} -> "
                       f"{tier_of(Fraction(naive).limit_denominator(10**9))})",
                "pass": std6 == 50 and tier_of(std6) == "Gold"})

    # Alternating misser (pay-miss-pay-miss) holds Recent=6 forever -> Gold cap.
    alt = ICSAccount()
    seq = [True, True, True, True, True, True] + [False, True] * 30
    for paid in seq:
        alt.step(paid)
    out.append({"check": "Alternating misser is permanently capped at Gold",
                "expected": "tier=Gold",
                "got": f"months={alt.months} recent={alt.recent} tier={alt.tier(0.0)}",
                "pass": alt.tier(0.0) == "Gold"})

    return out
