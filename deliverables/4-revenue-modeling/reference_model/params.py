"""Aurumix revenue model - all parameters in one place.

Precedence order, per the standing instruction:
    corpus (2-mechanism-design/_draft_*.md)  >  parameter completion set  >  v1.0 brief

Every parameter carries a `src` tag:
    CORPUS   - settled in a primary _draft_*.md file
    PARAM    - from _working_parameter-completion-set.md
    BRIEF    - from the v1.0 architecture brief
    DERIVED  - chosen by this model because no source states it. These are
               collected by audit_derived() and printed into VALIDATION.md.

No magic numbers anywhere else in the codebase.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction

# ---------------------------------------------------------------------------
# Audit registry
# ---------------------------------------------------------------------------

DERIVED_REGISTER: list[dict] = []
CONFLICT_REGISTER: list[dict] = []


def derived(name: str, value, why: str, confidence: str = "Low"):
    """Register a value this model chose because no source supplies it."""
    DERIVED_REGISTER.append(
        {"parameter": name, "value": value, "rationale": why, "confidence": confidence}
    )
    return value


def conflict(topic: str, corpus: str, param: str, brief: str, resolution: str):
    """Log a disagreement between the three sources and how it was resolved."""
    CONFLICT_REGISTER.append(
        {"topic": topic, "corpus": corpus, "param_file": param,
         "brief": brief, "resolution": resolution}
    )


# ---------------------------------------------------------------------------
# Horizon
# ---------------------------------------------------------------------------

HORIZON_MONTHS = 120
MONTHS_PER_YEAR = 12

# ---------------------------------------------------------------------------
# ICS engine - CORPUS, _draft_ics-scoring.md
# Exact fractions, not the rounded decimals. 8.3333*6 = 49.9998 < 50 would
# silently misplace the alternating-misser population into Silver.
# ---------------------------------------------------------------------------

RECORD_SLOPE_EARLY = Fraction(100, 24)   # 4.16666...  months 1-12  -> 50 at m=12
RECORD_SLOPE_LATE = Fraction(100, 96)    # 1.041666... months 13-60 -> 100 at m=60
STANDING_SLOPE = Fraction(100, 12)       # 8.33333...  x Recent     -> 100 at 12
RECORD_CAP = 100
STANDING_CAP = 100

ICS_FLOOR = 25                  # MAX(25, ...) once gated
WITHDRAWAL_ALLOWANCE = 0.30     # F9, decision 46
RETENTION_SLOPE_DENOM = 0.70    # 1 - (Sold-30%)/70%
GATE_RUN_REQUIRED = 6           # F7, consecutive periods
DORMANCY_SILENT_PERIODS = 12    # corpus extract item 2
RECENT_WINDOW = 12              # trailing countable months

# Tier thresholds - lower-bound lookup (_draft_ics-scoring.md 2.3)
TIER_THRESHOLDS = [(100, "Sovereign"), (75, "Platinum"), (50, "Gold"), (25, "Silver")]
TIER_ORDER = ["None", "Silver", "Gold", "Platinum", "Sovereign"]

# ---------------------------------------------------------------------------
# Fixed inputs (F-series) - BRIEF 8.1 unless noted
# ---------------------------------------------------------------------------

GOLD_USD_PER_G = 141.46         # F1, verified 2026-08-17. Held flat by design.

# Gold as a PATH, not only a level. A level shift cannot produce a margin call:
# with contributions fixed in USD, a permanently higher price buys
# proportionally fewer grams, so USD AUM is unchanged. A margin call comes from
# a move AFTER a loan is struck, so the shock must land at a point in time and
# revalue holdings already accumulated.
# None = flat at F1. Otherwise (shock_month, pct_move), e.g. (61, -0.13).
GOLD_SHOCK = None


def gold_price(month: int) -> float:
    """Gold price in `month`, honouring any scheduled shock."""
    if GOLD_SHOCK is None:
        return GOLD_USD_PER_G
    shock_month, move = GOLD_SHOCK
    return GOLD_USD_PER_G * (1.0 + move) if month >= shock_month else GOLD_USD_PER_G


AED_PER_USD = 3.6725            # F2
SIP_HARD_FLOOR = 20.0           # F6
GRACE_DAYS = 5                  # F8
COLLATERAL_SEASONING_DAYS = 90  # F10

LTV_LADDER = {"Gold": 0.50, "Platinum": 0.65, "Sovereign": 0.80}          # F11
MARGIN_CALL_LTV = 0.92   # corpus: the line at which collateral is sold
INTERCHANGE = {"Gold": 0.0180, "Platinum": 0.0205, "Sovereign": 0.0210}   # F12 primary
INTERCHANGE_PREPAID_CAP = 0.0100                                          # F12
GOLD_REWARDS_RATE = {"Gold": 0.0015, "Platinum": 0.0045, "Sovereign": 0.0075}
GOLD_REWARDS_SPEND_CAP = 3000.0    # F13, USD/month qualifying
VARA_SUPERVISION_AED = 200_000.0   # F14
MIN_CAPITAL_AED = 1_500_000.0      # F15 - locked, NOT expensed
SUMSUB_MONTHLY_MIN = 299.0         # F16
SUMSUB_PER_CHECK = 1.85            # F16
REFERRAL_REWARD_SHARE = 0.30       # F17, placeholder shape
REFERRAL_LAG_MONTHS = 6            # F18
SALARY_LOADING = 1.10              # F19

# Entry fee / premium step schedule (T1/T2/T3)
ENTRY_FEE_BY_YEAR = {1: .05, 2: .05, 3: .04, 4: .04, 5: .04, 6: .035, 7: .035,
                     8: .03, 9: .03, 10: .03}
FAB_PREMIUM_BY_YEAR = {1: .03, 2: .03, 3: .02, 4: .02, 5: .02, 6: .015, 7: .015,
                       8: .0075, 9: .0075, 10: .0075}
BAR_GRAMS_BY_YEAR = {1: 100, 2: 100, 3: 1000, 4: 1000, 5: 1000, 6: 1000,
                     7: 1000, 8: 12400, 9: 12400, 10: 12400}   # v1.0 ASSUMED

# The denomination ladder as (grams, fabrication premium). T3 is solved against
# the model's own volume rather than read from BAR_GRAMS_BY_YEAR, because v1.0's
# schedule is indexed to a volume trajectory the corrected model never reaches.
BAR_LADDER = [(100, 0.0300), (1000, 0.0200), (12400, 0.0075)]
SOLVE_BAR_DENOMINATION = True     # set False to reproduce v1.0's fixed schedule

# Tier entry-fee discount ladder, percentage POINTS (BRIEF 7.2)
TIER_DISCOUNT_PP = {"None": 0.0, "Silver": 0.004, "Gold": 0.008,
                    "Platinum": 0.012, "Sovereign": 0.015}

# Cardholder fee ladder (BRIEF 6.4)
FX_MARGIN = {"Gold": 0.020, "Platinum": 0.015, "Sovereign": 0.010}
ATM_FREE_ALLOWANCE_AED = {"Gold": 1000.0, "Platinum": 2500.0, "Sovereign": 5000.0}
ATM_OVER_FEE = 0.02

# Card fees (F21/F22, PARAM) in AED
CARD_ISSUANCE_FEE_AED = {"Gold": 75.0, "Platinum": 0.0, "Sovereign": 0.0}
CARD_REPLACEMENT_FEE_AED = {"Gold": 100.0, "Platinum": 50.0, "Sovereign": 0.0}
CARD_PRODUCTION_COST_USD = {"Gold": 4.50, "Platinum": 7.00, "Sovereign": 14.00}  # F26
AVG_TXN_SIZE_AED = {"Gold": 185.0, "Platinum": 240.0, "Sovereign": 310.0}        # F23
PER_TXN_PROCESSOR_FEE = 0.10       # F24, Stripe Issuing published
DECLINE_UPLIFT = 0.06              # F24 note: declines also bill
DISPUTE_COST_USD = 22.0            # F25
DISPUTES_PER_1000_TXN = 0.9        # F25

# Card programme fixed cost stack (F27, PARAM)
CARD_FIXED = {
    "bin_setup": 45_000.0, "scheme_join": 30_000.0,
    "bin_monthly": 6_000.0, "processor_monthly": 5_000.0,
    "scheme_quarterly": 12_000.0,
}
CARD_SETUP_MONTH = 15
CARD_LAUNCH_MONTH = 18

# Credit fee heads (F28-F31, PARAM) - (gross_rate, aurumix_share)
CREDIT_ORIGINATION = (0.0100, 0.50)   # F28
CREDIT_SERVICING = (0.0050, 0.70)     # F29 - %/yr of average drawn
CREDIT_PENAL = (0.0200, 0.40)         # F30
CREDIT_RECOVERY = (0.0150, 0.00)      # F31 - ZERO by design (III.E.4 risk)
CREDIT_INTEREST_SHARE_PP = 0.04       # BRIEF 6.5: ~4pp share of interest
CREDIT_LAUNCH_MONTH = 24

# Redemption (F20, PARAM)
REDEMPTION_COST_PER_EVENT = 4.20
DEALER_TWO_WAY_SPREAD = derived(
    "dealer_two_way_spread", 0.010,
    "Corpus gives the net-flow spread mechanism but never a spread rate. 1.0% "
    "two-way is a mid-market bullion dealer round-trip on 100g-1kg bars, "
    "consistent with the 3% fabrication premium on smaller denominations.",
    "Low")

# Tax (F33-F35, PARAM)
CORP_TAX_RATE = 0.09
CORP_TAX_THRESHOLD_AED = 375_000.0
LOSS_CARRYFORWARD_CAP = 0.75
ASSUME_QFZP = False              # F35 - conservative call

VAT_RATE = 0.05                  # F36
VAT_INPUT_DRAG = 0.20            # PARAM: haircut the zero-rating benefit 20%
RESIDENT_SHARE = {"S1": 1.0, "S2": 1.0, "S3": 1.0, "S4": 0.0, "S5": 0.0, "S6": 0.0}

# Float (F38/S50/S51, CORPUS _draft_allocation-and-float.md)
FLOAT_BARS_LAUNCH = 2
FLOAT_BUFFER_DAYS = 10           # S50
FLOAT_COC_RATE = 0.08            # see conflict log - annualised cost of capital
DEALER_CARRIED_UNTIL_YEAR = 3    # S51

# Regulatory capital
RESERVE_CAPITAL_PCT = 0.02       # 2% of trailing-24m reserves (Option B only)
OPTION_B = False                 # default OFF - Option A is the chosen route

# ---------------------------------------------------------------------------
# Segments (BRIEF 5)
# ---------------------------------------------------------------------------

SEGMENTS = ["S1", "S2", "S3", "S4", "S5", "S6"]
TICKET = {"S1": 75.0, "S2": 40.0, "S3": 20.0, "S4": 40.0, "S5": 30.0, "S6": 75.0}
ADDRESSABLE = {"S1": 71_000, "S2": 119_000, "S3": 285_000,
               "S4": 1_014_000, "S5": 12_500_000, "S6": 50_000}
SEGMENT_LIVE_MONTH = {"S1": 1, "S2": 1, "S3": 1, "S4": 13, "S5": 13, "S6": 25}

# S22 penetration ceilings
PENETRATION_CEILING = {
    "Base":         {"S1": .22, "S2": .16, "S3": .09, "S4": .06, "S5": .0035, "S6": .06},
    "Aggressive":   {"S1": .32, "S2": .24, "S3": .14, "S4": .10, "S5": .0060, "S6": .10},
    "Conservative": {"S1": .12, "S2": .09, "S3": .05, "S4": .03, "S5": .0015, "S6": .03},
}
S6_CEILING_NOTE = derived(
    "S6 penetration ceiling", 0.06,
    "S22 leaves S6 as 'n/a' and BRIEF 5 does not size the S6 base. Set the S6 "
    "addressable base at 50,000 and its ceiling equal to S4's, since both are "
    "small international perimeters requiring local licensing.",
    "Low")

# S29 reduction depth: reduced ticket by segment
REDUCED_TICKET_FRAC = 0.50       # of prior ticket, floored at SIP_HARD_FLOOR

# ---------------------------------------------------------------------------
# Channels (S16, PARAM) - rows sum to 100% of that channel's volume
# ---------------------------------------------------------------------------

CHANNELS = ["Agent", "Referral", "Direct", "B2B"]

CHANNEL_MIX_PHASES = {
    1: {  # M1-M12
        "Agent":    {"S1": .15, "S2": .40, "S3": .45},
        "Referral": {},
        "Direct":   {"S1": .45, "S2": .40, "S3": .15},
        "B2B":      {},
    },
    2: {  # M13-M24
        "Agent":    {"S1": .12, "S2": .33, "S3": .38, "S4": .10, "S5": .07},
        "Referral": {"S1": .18, "S2": .38, "S3": .33, "S4": .06, "S5": .05},
        "Direct":   {"S1": .38, "S2": .33, "S3": .12, "S4": .07, "S5": .10},
        "B2B":      {},
    },
    3: {  # M25+
        "Agent":    {"S1": .10, "S2": .28, "S3": .32, "S4": .12, "S5": .16, "S6": .02},
        "Referral": {"S1": .16, "S2": .34, "S3": .30, "S4": .08, "S5": .10, "S6": .02},
        "Direct":   {"S1": .32, "S2": .28, "S3": .10, "S4": .08, "S5": .16, "S6": .06},
        "B2B":      {"S1": .05, "S2": .15, "S3": .10, "S4": .05, "S5": .60, "S6": .05},
    },
}

AGENT_RAMP = [0.20, 0.40, 0.60, 0.75, 0.85, 0.95] + [1.00] * 6 + [1.05]  # S17
AGENT_ATTRITION_ANNUAL = 0.45     # S18
ACTIVE_AGENTS_BY_YEAR = {1: 5, 2: 15, 3: 40, 4: 65, 5: 90, 6: 115,
                         7: 140, 8: 165, 9: 185, 10: 200}   # T7
REFERRAL_RATE = 0.45              # S19 per qualified referrer per year
REFERRAL_CONVERSION = 0.62        # S20
ORGANIC_SHARE_OF_DIRECT = 0.12    # S26

# S25 CAC diminishing returns
CAC_BASE = 120.0                  # S15
CAC_UPLIFT = 0.35
CAC_DIVISOR = 60_000.0
CAC_EXPONENT = 0.7

MARKETING_SPEND_BY_YEAR = derived(
    "marketing_spend_by_year",
    {1: 60_000, 2: 150_000, 3: 250_000, 4: 320_000, 5: 400_000,
     6: 480_000, 7: 560_000, 8: 640_000, 9: 720_000, 10: 800_000},
    "The opex table treats Marketing as a cost block but S48/G1 says it is a "
    "decision variable and an INPUT to acquisition. Neither source gives a "
    "monthly path. Anchored on the brief's Y1/Y3/Y10 opex marketing line and "
    "interpolated straight-line (log-linear is undefined from a zero base).",
    "Low")

# ---------------------------------------------------------------------------
# Behavioural archetypes (S27, PARAM) - the load-bearing fill
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Archetype:
    name: str
    weight: float
    pay_prob: float       # monthly probability a contribution clears
    own_hazard: float     # payment-driven attrition
    reduces: bool = False


ARCHETYPE_MIX = {
    "Base": {
        "background_hazard": 0.016,
        "archetypes": [
            Archetype("Perfect payer",     0.10, 0.995, 0.000),
            Archetype("Occasional misser", 0.35, 0.930, 0.007),
            Archetype("Alternating misser",0.12, 0.550, 0.018),
            Archetype("Reducer",           0.13, 0.970, 0.002, reduces=True),
            Archetype("Early lapser",      0.30, 0.600, 0.200),
        ],
    },
    "Aggressive": {
        "background_hazard": 0.011,
        "archetypes": [
            Archetype("Perfect payer",     0.29, 0.995, 0.000),
            Archetype("Occasional misser", 0.26, 0.930, 0.007),
            Archetype("Alternating misser",0.16, 0.550, 0.018),
            Archetype("Reducer",           0.08, 0.970, 0.002, reduces=True),
            Archetype("Early lapser",      0.21, 0.600, 0.200),
        ],
    },
    "Conservative": {
        "background_hazard": 0.024,
        "archetypes": [
            Archetype("Perfect payer",     0.14, 0.995, 0.000),
            Archetype("Occasional misser", 0.24, 0.930, 0.007),
            Archetype("Alternating misser",0.16, 0.550, 0.018),
            Archetype("Reducer",           0.10, 0.970, 0.002, reduces=True),
            Archetype("Early lapser",      0.36, 0.600, 0.200),
        ],
    },
}

# Early-lapser hazard decays: "~90% gone by M13" then the survivors behave
EARLY_LAPSER_DECAY_MONTH = 13
EARLY_LAPSER_POST_HAZARD = derived(
    "early_lapser_post_gate_hazard", 0.030,
    "S27 gives the early lapser a 0.200 own hazard and says '~90% gone by M13' "
    "but does not say what the residual does afterwards. Holding 0.200 forever "
    "drives the archetype to zero and removes it from the M25+ mix entirely, "
    "which over-thins the tail. Decayed to 0.030 from M13.",
    "Low")

# Survival anchors (BRIEF 0.5) - the calibration target
SURVIVAL_ANCHORS = {13: 0.55, 25: 0.40, 37: 0.30, 49: 0.24, 61: 0.19}
SURVIVAL_ANCHORS_S2 = {
    "Aggressive":   {13: 0.65, 25: 0.517, 37: 0.423, 49: 0.349, 61: 0.289},
    "Conservative": {13: 0.45, 25: 0.294, 37: 0.201, 49: 0.139, 61: 0.097},
}

# Withdrawal behaviour buckets (S31) - straddle the 30% Retention kink
WITHDRAWAL_BUCKETS = {
    "Base":         [(0.00, .480), (0.05, .220), (0.19, .160),
                     (0.44, .090), (0.78, .035), (1.00, .015)],
    "Aggressive":   [(0.00, .600), (0.05, .210), (0.18, .120),
                     (0.42, .050), (0.75, .015), (1.00, .005)],
    "Conservative": [(0.00, .260), (0.05, .170), (0.22, .190),
                     (0.45, .190), (0.80, .130), (1.00, .060)],
}

REDUCTION_CAPTURE = {"Base": 0.33, "Aggressive": 0.50, "Conservative": 0.18}  # S28
REDUCED_HAZARD_MULT = {"Base": 1.35, "Aggressive": 1.15, "Conservative": 1.75}  # S30
INVOLUNTARY_CHURN_SHARE = 0.30   # corpus extract item 2

# Redemption / leakage
SELF_CUSTODY_LEAKAGE = {"Base": 0.12, "Aggressive": 0.06, "Conservative": 0.30}  # S10
REDEMPTION_RATE = {"Base": 0.08, "Aggressive": 0.04, "Conservative": 0.16}       # S32
LAPSED_REDEMPTION_MULT = {"Base": 2.2, "Aggressive": 1.6, "Conservative": 3.5}   # S33

# ---------------------------------------------------------------------------
# Card drivers
# ---------------------------------------------------------------------------

CARD_SPEND_AED = {"Base": 6000.0, "Aggressive": 9000.0, "Conservative": 3500.0}  # S4
CARD_ACTIVATION = {"Base": 0.65, "Aggressive": 0.80, "Conservative": 0.45}       # S5
PM_SHARE = {"Base": 0.72, "Aggressive": 0.85, "Conservative": 0.55}              # S3
PM_SHARE_EARLY = 0.55            # BRIEF 6.2: use Low for M18-M30
PM_SHARE_EARLY_UNTIL = 30
PM_SHARE_FLOOR = 0.36            # walk-away

CARD_SPEND_TIER_MULT = {  # S38
    "Base":         {"Gold": 0.82, "Platinum": 1.12, "Sovereign": 1.54},
    "Aggressive":   {"Gold": 0.85, "Platinum": 1.10, "Sovereign": 1.45},
    "Conservative": {"Gold": 0.78, "Platinum": 1.15, "Sovereign": 1.70},
}
FOREIGN_SPEND_SHARE = {"Base": 0.34, "Aggressive": 0.45, "Conservative": 0.24}   # S34

# Segment card-spend multiplier. S38 differentiates card spend by TIER but not
# by SEGMENT, yet segments are defined by income capacity (USD 20-75/month, a
# 3.75x spread), so crediting an S3 saver with an S1 professional's card spend
# is indefensible on the model's largest revenue driver.
# Keyed to the SIP ticket as an income proxy and compressed by an exponent,
# because discretionary card spend rises sub-proportionally with income.
# Normalised at run time so the book-weighted mean still equals S4's AED 6,000,
# so this REDISTRIBUTES spend across segments and cannot change the aggregate.
CARD_SPEND_SEGMENT_EXPONENT = derived(
    "card_spend_segment_exponent", 0.55,
    "No source splits card spend by customer income band. Ticket is used as an "
    "income proxy, compressed by an exponent of 0.55, turning the 3.75x S3->S1 "
    "ticket spread into a ~2.1x card-spend spread. Consumption rises "
    "sub-proportionally with income (Engel-curve behaviour) and 0.55 sits mid "
    "the 0.4-0.7 range usually fitted to it. Normalised so the book-weighted "
    "mean equals the AED 6,000 S4 anchor: it redistributes, never rescales.",
    "Low")
ATM_DISTRIBUTION = [(250.0, .60), (1000.0, .25), (2250.0, .12), (4000.0, .03)]   # S35
CARD_ISSUANCE_EVENT_RATE = 0.06      # S36, per active card per year after first
CARD_REPLACEMENT_EVENT_RATE = 0.11   # S37
CARD_FRAUD_BPS = {"Base": 9.0, "Aggressive": 5.0, "Conservative": 22.0}          # S39

LAPSED_KEEPS_CARD = True   # OPEN CLIENT QUESTION - switch per the task spec

# ---------------------------------------------------------------------------
# Credit drivers
# ---------------------------------------------------------------------------

CREDIT_TAKEUP = {"Base": 0.18, "Aggressive": 0.30, "Conservative": 0.08}   # S8
CREDIT_DRAWN_PCT = {"Base": 0.50, "Aggressive": 0.70, "Conservative": 0.30}  # S9
FACILITY_TURNOVER = {"Base": 0.42, "Aggressive": 0.55, "Conservative": 0.30}  # S40
DRAW_EVENTS_PER_YEAR = {"Base": 2.1, "Aggressive": 3.2, "Conservative": 1.3}  # S41
CREDIT_APR = derived(
    "credit_apr", 0.125,
    "BRIEF 6.5 gives a UAE pricing corridor of 9% (Emirates Money) to 16% "
    "(Finance House) but never picks a point. Midpoint 12.5%; Aurumix takes "
    "CREDIT_INTEREST_SHARE_PP of it, not the whole rate.",
    "Medium")

# ---------------------------------------------------------------------------
# Family plan (stream 3)
# ---------------------------------------------------------------------------

FAMILY_ATTACH = {"Base": 0.20, "Aggressive": 0.35, "Conservative": 0.10}   # S11
FAMILY_PRICE_ANNUAL = 32.0        # BRIEF 6.3: USD 29-36/yr midpoint
FAMILY_NAMES_INCLUDED = 4
FAMILY_EXTRA_NAME_PRICE = 20.0
FAMILY_DISCOUNT = {"None": 0.0, "Silver": 0.10, "Gold": 0.20,
                   "Platinum": 0.35, "Sovereign": 0.50}
FAMILY_COST_PER_NAME_ONEOFF = 2.35   # midpoint of USD 1.80-2.90
FAMILY_COST_PER_NAME_ANNUAL = 0.36
FAMILY_AVG_NAMES = derived(
    "family_avg_names", 3.2,
    "Pricing includes up to 4 beneficiaries; no source gives the observed mean. "
    "3.2 assumes most households register spouse + 2 children and a minority "
    "add a parent.",
    "Low")

# ---------------------------------------------------------------------------
# B2B (stream 6)
# ---------------------------------------------------------------------------

B2B_PARTNERS_BY_YEAR = {  # S42
    "Base":         {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 7, 10: 8},
    "Aggressive":   {2: 1, 3: 3, 4: 5, 5: 7, 6: 9, 7: 11, 8: 13, 9: 14, 10: 15},
    "Conservative": {2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3},
}
B2B_TERMINAL_AUM_PER_PARTNER = {"Base": 32e6, "Aggressive": 45e6, "Conservative": 22e6}
B2B_RAMP = {6: .08, 12: .25, 24: .48, 36: .70, 48: .85, 60: 1.00}   # S43
B2B_FEE_BPS = 0.0060              # solver item 7: 60bps in the 50-75 range
B2B_INDIA_SHARE = 0.60            # S16 B2B row is 60% S5
B2B_LAUNCH_MONTH = 24

# ---------------------------------------------------------------------------
# Spot lane (S45-S47, PARAM)
# ---------------------------------------------------------------------------

SPOT_ATTACH = {"Base": 0.14, "Aggressive": 0.24, "Conservative": 0.07}
SPOT_TICKET = {"Base": 620.0, "Aggressive": 1100.0, "Conservative": 320.0}
SPOT_FREQ = {"Base": 1.7, "Aggressive": 2.4, "Conservative": 1.2}
SPOT_SEGMENT_SCALE = {"S1": 1.6, "S2": 1.0, "S3": 0.45, "S4": 1.0, "S5": 0.7, "S6": 1.6}
SPOT_TENURE_UPLIFT_PER_YEAR = derived(
    "spot_tenure_uplift", 0.30,
    "S45 says a 3-year account is 'roughly 2x as likely' to buy spot as a "
    "6-month account but gives no functional form. Linear +30%/yr of tenure, "
    "capped at 2.0x, reproduces that ratio at 3 years.",
    "Low")
ARREARS_EVENTS_PER_ACCOUNT_YEAR = 0.11   # S47 note

# ---------------------------------------------------------------------------
# Rail (S1) - the single most important unknown
# ---------------------------------------------------------------------------

RAIL_COST = {"Base": 0.25, "Aggressive": 0.10, "Conservative": 1.36}
SPOT_RAIL_COST = 0.25             # one push, no mandate

# Price-gap (recomputed, not hard-coded)
GOLD_VOL = {"Base": 0.25, "Aggressive": 0.20, "Conservative": 0.35}   # S6

# Vault (S14)
VAULT_RATE = {"Base": 0.0025, "Aggressive": 0.0015, "Conservative": 0.0040}
VAULT_MIN_USD_PER_DAY = 25.0
VAULT_RATE_PER_KG_DAY = 0.10
# Which vendor archetype is being bought. These are ALTERNATIVE pricing models,
# not a menu to minimise over. 'ad_valorem' is the conservative and more
# defensible read: the brief's own 7.4 verifies allocated storage at 0.12-0.40%
# of value (BullionVault 0.12%, GoldMoney 0.25%, SGPMX 0.40-0.50%) and S14 is
# stated as a percentage of AUM, so the percentage regime is the sourced one.
VAULT_REGIME = derived(
    "vault_pricing_regime", "ad_valorem",
    "S14 and the brief's 7.4 verified range are both stated as a PERCENTAGE of "
    "value, so ad valorem is the sourced regime. The DGCX USD 0.10/kg/day "
    "tariff is a different vendor archetype quoted for wholesale bar storage. "
    "v1.0 took the cheaper of the two, which is not a quote anyone offers and "
    "understates Y10 vault cost by roughly 10x.",
    "Medium")

# ---------------------------------------------------------------------------
# Opex anchors (BRIEF 7.4) and interpolation (F32/G1, PARAM)
# ---------------------------------------------------------------------------

OPEX_ANCHORS = {1: 894_800.0, 3: 2_484_700.0, 10: 8_695_500.0}
OPEX_PUBLISHED = {1: 845_800.0, 3: 2_506_000.0, 10: 8_495_500.0}
OPEX_INTERPOLATED = {  # G1 table, block-level log-linear
    1: 894_800.0, 2: 1_478_420.0, 3: 2_484_700.0, 4: 2_929_793.0,
    5: 3_475_359.0, 6: 4_143_676.0, 7: 4_962_115.0, 8: 5_964_336.0,
    9: 7_191_778.0, 10: 8_695_500.0,
}
OPEX_Y1_EXIT_UPLIFT = 1.40        # S48

# The investor counts the brief's 7.4 anchors are stated against.
# The brief labels them "Y1 (500) / Y3 (12,000) / Y10 (80,000)" and publishes a
# "cost per investor" row on them; its own 14 default says the Y10 target counts
# investors STILL CONTRIBUTING. So the anchors are contributing counts.
# Holding counts are inferred by applying the model's own contributing:holding
# ratio, which v1.0 could not compute because it treated LAPSED as terminal.
OPEX_ANCHOR_CONTRIBUTING = {1: 500, 3: 12_000, 10: 80_000}
OPEX_ANCHOR_HOLDING_RATIO = derived(
    "opex_anchor_holding_ratio", {1: 1.35, 3: 1.9, 10: 3.0},
    "The brief's opex anchors are contributing counts (7.4 'cost per investor' "
    "row + 14 default). Blocks that scale with the HOLDING book need a holding "
    "count at those same anchors, which v1.0 never computed because it treated "
    "LAPSED as terminal. Ratios are taken from this model's own computed "
    "contributing:holding trajectory (1.35x at Y1 rising to ~3.0x at Y10).",
    "Medium")
OPEX_ANCHOR_N = {
    "contributing": OPEX_ANCHOR_CONTRIBUTING,
    "holding": {y: OPEX_ANCHOR_CONTRIBUTING[y] * OPEX_ANCHOR_HOLDING_RATIO[y]
                for y in OPEX_ANCHOR_CONTRIBUTING},
}

# Block-level opex anchors, verbatim from the brief 7.4 table.
# `driver` assigns each block the population it genuinely scales with.
OPEX_BLOCKS = {
    "Headcount":            {"driver": "contributing",
                             "anchors": {1: 588_000, 3: 1_340_000, 10: 4_600_000}},
    "MLRO":                 {"driver": "fixed",
                             "anchors": {1: 49_000, 3: 163_000, 10: 0}},
    "VARA supervision":     {"driver": "fixed",
                             "anchors": {1: 54_500, 3: 94_500, 10: 110_000}},
    "Audit + attestation":  {"driver": "fixed",
                             "anchors": {1: 35_000, 3: 60_000, 10: 180_000}},
    "Compliance + KYC":     {"driver": "holding",
                             "anchors": {1: 31_600, 3: 97_200, 10: 255_500}},
    "Vault and metal":      {"driver": "holding",
                             "anchors": {1: 12_000, 3: 150_000, 10: 800_000}},
    "Technology":           {"driver": "holding",
                             "anchors": {1: 34_000, 3: 115_000, 10: 600_000}},
    "Corporate":            {"driver": "contributing",
                             "anchors": {1: 20_700, 3: 60_000, 10: 350_000}},
    "Security":             {"driver": "fixed",
                             "anchors": {1: 10_000, 3: 35_000, 10: 200_000}},
    "Legal + insurance":    {"driver": "fixed",
                             "anchors": {1: 60_000, 3: 120_000, 10: 400_000}},
}
# Marketing is deliberately EXCLUDED from the opex blocks: it is a decision
# variable and an INPUT to acquisition via the CAC curve (G1). v1.0 carries it
# in both places, which double-counts it. It is booked once, in acquisition cost.

ONE_OFF_COSTS = {   # BRIEF 7.4 + corpus extract item 6
    "vara_application": 27_200.0,
    "smart_contract_audit": 75_000.0,
    "dmcc_incorporation": 3_280.0,
    "difc_spv": 1_900.0,          # corrected from ADGM per corpus extract item 6
    "licensing_support": 20_000.0,
    "legal_opinions": 0.0,        # UNPRICED - see derived note below
    "trust_deed": 0.0,            # UNPRICED
}
LEGAL_OPINIONS_PLACEHOLDER = derived(
    "legal_opinions_and_trust_deed", 150_000.0,
    "Corpus says 'NOT ESTABLISHED. Budget generously' and names 3 opinions plus "
    "a trust deed and 6 counsel batches. The brief carries ZERO legal cost, "
    "which reads as if legal is free. USD 150k one-off is a visible placeholder, "
    "NOT a quote. Booked M1-M12.",
    "Low")

# ---------------------------------------------------------------------------
# Seasonality (S52) - MUST normalise to exactly 12.0
# ---------------------------------------------------------------------------

SEASON_ACQUISITION = [1.05, .95, .95, 1.20, .90, .85, .80, .85, 1.05, 1.30, 1.20, .90]
SEASON_CARD_SPEND = [1.10, .95, .95, 1.00, .90, .85, .90, .95, 1.00, 1.10, 1.15, 1.15]
SEASON_FOREIGN_SHARE = [.30, .30, .30, .32, .34, .55, .60, .56, .36, .42, .40, .32]  # S53

# ---------------------------------------------------------------------------
# Book-state scenarios (corpus extract item 1)
# ---------------------------------------------------------------------------

BOOK_STATES = {
    "growing":   (0.08, 0.03),
    "flat":      (0.04, 0.04),
    "shrinking": (0.02, 0.06),
    "run":       (0.01, 0.25),
}

# ---------------------------------------------------------------------------
# Scenario container
# ---------------------------------------------------------------------------

@dataclass
class Scenario:
    """A resolved parameter set. `overrides` applies any per-parameter change."""
    name: str = "Base"
    mode: str = "Base"                       # Base | Aggressive | Conservative
    india_enabled: bool = True
    lapsed_keeps_card: bool = LAPSED_KEEPS_CARD
    card_enabled: bool = True
    card_prepaid_capped: bool = False        # "no card" narrative -> 1.00% flat
    option_b: bool = False
    growth_target_y10: float | None = None   # "client's plan" -> impose 100k
    overrides: dict = field(default_factory=dict)

    def g(self, key: str, default=None):
        """Resolve a scenario-mode-keyed parameter, honouring overrides."""
        if key in self.overrides:
            return self.overrides[key]
        table = globals().get(key)
        if isinstance(table, dict) and self.mode in table:
            return table[self.mode]
        return table if table is not None else default


def year_of(month: int) -> int:
    return (month - 1) // MONTHS_PER_YEAR + 1


def step_by_year(table: dict, month: int):
    return table[min(year_of(month), 10)]


# ---------------------------------------------------------------------------
# Source conflicts, logged at import so VALIDATION.md is always current
# ---------------------------------------------------------------------------

conflict(
    "Monthly hazard root convention",
    "n/a",
    "n/a",
    "1.0 says h=1-S^(1/12); 10.2 says h=1-S13^(1/13)",
    "Used 1/12. The M13 anchor spans 12 hazard opportunities. Per task spec.")

conflict(
    "Reduced-state ticket",
    "n/a",
    "S29: 50% of prior ticket floored at USD 20",
    "3 Layer 3 hard-codes reduced x 20",
    "Used S29. The brief's hard-coded 20 is a real error; the floor is the "
    "hard minimum (F6), not the observed landing point.")

conflict(
    "LAPSED is terminal",
    "extract item 2: STOPPED/DORMANT retain gold, AUM, custody, card",
    "S33 lapsed-holder redemption multiplier",
    "Layer 2 treats LAPSED as dropping out of everything",
    "Used corpus. LAPSED-HOLDING stays in AUM, custody, screening and (per "
    "the LAPSED_KEEPS_CARD switch) the interchange base.")

conflict(
    "Spot entry-fee discount",
    "_draft_sip-rulebook.md 1.1 + decision 44: tier discount on ALL purchases",
    "Block F prices spot at the tier discount",
    "brief models no spot lane at all",
    "Used corpus. _draft_purchase-structure.md 4.1/4.3 ('flat, top of range') "
    "is superseded - six days older and overridden by decision 44.")

conflict(
    "Tenure rebate",
    "decision 44 (2026-08-10) RETIRED it",
    "not carried",
    "9 solver item 6 asks the model to size it",
    "Struck. No rebate is modelled and no FIFO lot accounting is built "
    "(decision 41 makes grams fungible).")

conflict(
    "Float cost of capital double-count",
    "extract item 5: charging float CoC AND the full dealer premium "
    "double-counts under either regime",
    "S51 dealer-carried at launch",
    "F5 charges 0.49% float CoC as a flat % of inflow with no derivation",
    "Float CoC is DERIVED from the sized float, and set to zero while the "
    "float is dealer-carried (to Y3). The flat F5 rate is not used.")

conflict(
    "Stream 5 drawn balance",
    "Manappuram realised tenor 71 days",
    "S40 turnover factor 0.42",
    "6.5 computes peak drawn and prices it as persistent",
    "Applied S40 to the interest component only; origination is per-event and "
    "rises with turnover. Roughly halves stream 5.")

conflict(
    "Collateral chain open links",
    "table marks 2 open (links 1,5), 3 designed",
    "n/a",
    "header says 'three are open'",
    "Recorded as 2 open / 3 designed. Header is stale; the table is operative.")

conflict(
    "ADGM vs DIFC holding vehicle",
    "decision 50 + composability draft settle route 2 as DIFC",
    "n/a",
    "7.4 one-off table lists an ADGM SPV",
    "Booked as DIFC SPV. Same cost, corrected label.")
