"""
Stage 1 parameters, from Aurumix_Simulation_Blueprint.md Part 2 and Appendix A.

Every value here is either (a) read from Aurumix_Revenue_Model_calculated.xlsx,
(b) quoted from the mechanism-design corpus, or (c) marked UNSOURCED and swept.
Nothing is invented silently.
"""

from dataclasses import dataclass, field
from typing import Dict

# ─────────────────────────────────────────────────────────────────────────────
# Horizon
# ─────────────────────────────────────────────────────────────────────────────

HORIZON_MONTHS = 84          # primary horizon, matches the workbook's 7 years
DIAGNOSTIC_MONTHS = 120      # extended run: the tier ladder does not mature in 84

# ─────────────────────────────────────────────────────────────────────────────
# The ICS formula — _draft_ics-scoring.md sec 1. EXACT, not approximated.
#
#   ICS = min(Record, Standing) x Retention,  floored at 25 once gated
# ─────────────────────────────────────────────────────────────────────────────

GATE_RUN = 6                 # consecutive counted periods to earn Confirmed SIP
ICS_FLOOR_ONCE_GATED = 25.0

# Exact fractions, not the doc's 4-dp roundings: 4.1667 and 8.3333 leave
# Record(60) = 100.0008 and Standing(12) = 99.9996, so Sovereign (>= 100)
# becomes unreachable by rounding. The doc's own tables show 50/75/100 exactly.
RECORD_SLOPE_EARLY = 50.0 / 12.0     # months <= 12
RECORD_KINK_MONTH = 12
RECORD_AT_KINK = 50.0
RECORD_SLOPE_LATE = 50.0 / 48.0      # 12 < months <= 60
RECORD_CAP_MONTH = 60                # "five years of saving is a complete record"

STANDING_SLOPE = 100.0 / 12.0        # Standing = Recent x (100/12), Recent in 0..12
RECENT_WINDOW = 12

RETENTION_ALLOWANCE = 0.30       # sell up to 30%/yr and nothing happens
RETENTION_SLOPE_DENOM = 0.70     # 1 - (Sold - 30%) / 70%

# Tier thresholds on the ICS score. Four benefit-bearing tiers above "no tier".
TIER_THRESHOLDS = {
    "silver": 25.0,
    "gold": 50.0,
    "platinum": 75.0,
    "sovereign": 100.0,
}
TIER_ORDER = ["none", "silver", "gold", "platinum", "sovereign"]

# ─────────────────────────────────────────────────────────────────────────────
# Payment archetypes — v2.6 Appendix A.
#
# UNSOURCED: the weights are recorded in the brief as "rank 1 load-bearing and a
# confirmed sourcing negative". They are SWEPT, never assumed. The Base mix below
# exists to reproduce v2.6's published figures as a CODE-CORRECTNESS test only.
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Archetype:
    name: str
    weight: float
    pay_prob: float
    own_hazard: float
    pay_decay: float = 1.0      # monthly multiplier on pay_prob; 1.0 = flat
    pay_floor: float = 0.0      # pay_prob never falls below this


ARCHETYPES_BASE = [
    Archetype("perfect",     0.10, 0.995, 0.000),
    Archetype("occasional",  0.35, 0.930, 0.007),
    Archetype("alternating", 0.12, 0.550, 0.018),
    Archetype("reducer",     0.13, 0.970, 0.002),
    # v2.6 says "0.60 falling" but its own published figures (2.6% ever-gate,
    # mean gate M8.6, ~90% gone by M13) are reproduced by a FLAT 0.60 and fit
    # WORSE under any falling variant tested. Flat is used; the discrepancy is
    # in v2.6's prose, not its arithmetic.
    Archetype("early_lapser", 0.30, 0.600, 0.200),
]

ARCHETYPES_AGGRESSIVE = [
    Archetype("perfect",     0.29, 0.995, 0.000),
    Archetype("occasional",  0.26, 0.930, 0.007),
    Archetype("alternating", 0.16, 0.550, 0.018),
    Archetype("reducer",     0.08, 0.970, 0.002),
    Archetype("early_lapser", 0.21, 0.600, 0.200),
]

ARCHETYPES_CONSERVATIVE = [
    Archetype("perfect",     0.14, 0.995, 0.000),
    Archetype("occasional",  0.24, 0.930, 0.007),
    Archetype("alternating", 0.16, 0.550, 0.018),
    Archetype("reducer",     0.10, 0.970, 0.002),
    Archetype("early_lapser", 0.36, 0.600, 0.200),
]

# Background hazard applies to every archetype on top of its own.
# Derived, not typed: v2.6 gives total monthly attrition per archetype, and
# perfect payer has own_hazard 0.000 against a total of 0.016.
BACKGROUND_HAZARD = {"base": 0.016, "aggressive": 0.011, "conservative": 0.024}

# ─────────────────────────────────────────────────────────────────────────────
# Rails — _draft_sip-rulebook.md sec 6.2.
#
# Launch rails are AANI Request to Pay ("one tap a month") and the prefunded
# balance ("set and forget"). The rulebook enforces that distinction in a
# marketing rule, so the two carry different payment discipline.
#
# UNSOURCED: the size of the discipline gap. Swept.
# ─────────────────────────────────────────────────────────────────────────────

RAIL_PREFUNDED_SHARE = 0.30      # UNSOURCED, swept 0.0 -> 0.75
# A prefunded agent draws from a mix shifted toward discipline. Implemented as a
# probability of being re-drawn into a better archetype, not as a pay_prob bump,
# so the archetype remains the single behavioural primitive.
RAIL_DISCIPLINE_SHIFT = 0.35     # UNSOURCED, swept

# ─────────────────────────────────────────────────────────────────────────────
# Regions and tickets — Assumptions!B190:B192 of the calculated workbook.
#
# The ticket is VARIABLE month to month with no maximum (rulebook sec 6.1);
# only the USD 20 floor is tested. ticket_base is a centre, not a constant.
# ─────────────────────────────────────────────────────────────────────────────

TICKET_FLOOR_USD = 20.0

@dataclass(frozen=True)
class Region:
    name: str
    ticket_mean: float
    opens_month: int


REGIONS = [
    Region("UAE", 33.60, 1),
    Region("OmanBahrain", 26.00, 13),
    Region("India", 30.00, 1),
]

# UNSOURCED but defensible as shape: savings books sit heavy at the floor.
# Handoff sec 9: "40 to 60% of the book sits at the floor". Swept.
TICKET_FLOOR_SHARE = 0.50

# Month-to-month variation around ticket_base. UNSOURCED, swept.
# The declared amount is max(floor, base x noise): a floor saver pays exactly
# the floor. Whether they pay at all is the archetype's job - modelling
# sub-floor draws as rejections would double-count misses.
TICKET_SIGMA_MONTH = 0.25

# ─────────────────────────────────────────────────────────────────────────────
# Gold and redemption — needed in Stage 1 only because Retention reads grams.
# ─────────────────────────────────────────────────────────────────────────────

GOLD_PRICE_M1 = 141.50           # USD/g, Assumptions!B6
ENTRY_FEE = 0.05                 # Assumptions!B8. The customer's ceiling.
REDEMPTION_RATE_ANNUAL = 0.06    # Assumptions!B152
SELF_CUSTODY_RATE_ANNUAL = 0.06  # Assumptions!B151
HOLDER_REDEMPTION_MULTIPLIER = 1.6

# ─────────────────────────────────────────────────────────────────────────────
# Verification targets — v2.6's published figures.
#
# CODE-CORRECTNESS TESTS ONLY. These are outputs of a Markov solve over an
# unsourced archetype mix. Reproducing them proves the first-passage logic is
# right; it is NOT evidence about Aurumix. See blueprint sec 4.1.
# ─────────────────────────────────────────────────────────────────────────────

VERIFY = {
    "persistency": {13: 0.55, 25: 0.40, 37: 0.30, 49: 0.24, 61: 0.19},
    "ever_gate_share": 0.535,
    "mean_gate_month": 8.1,
    "alternating_ever_gate": 0.240,
    "holding_not_contributing_m61": 0.81,
    # NOTE: v2.6's "sovereign share ~1.2%" is NOT a verification target. It is
    # an output of the lookup that capped the occasional misser at Platinum by
    # construction. Under the real formula an occasional misser with 60 counted
    # months and a clean trailing year legitimately scores 100 - Sovereign's
    # zero tolerance IS the trailing window, and they bounce in and out of it.
    # The simulation's higher share is a consequence of implementing the
    # rulebook's formula instead of the Excel workaround. Reported, not fixed.
    "per_archetype_ever_gate": {
        "perfect": 0.906,
        "occasional": 0.836,
        "alternating": 0.240,
        "reducer": 0.886,
        "early_lapser": 0.026,
    },
    "per_archetype_mean_gate": {
        "perfect": 6.1,
        "occasional": 7.6,
        "alternating": 24.9,
        "reducer": 6.6,
        "early_lapser": 8.6,
    },
}

TOLERANCE = 0.02      # absolute, on shares
TOLERANCE_MONTHS = 0.6
