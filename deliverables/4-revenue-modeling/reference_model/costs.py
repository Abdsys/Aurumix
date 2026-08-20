"""Cost architecture: Opex(N) as a fitted function, benefit costs, redemption
net-flow logic, card programme fixed minimums, tax with loss carry-forward.

The v1.0 break-even divided opex sized for 500 investors by margin-per-investor
to get 171,911 investors - incoherent, because opex is a function of N. Here
Opex(N) = Fixed + variable x N is fitted to the three anchors and break-even is
solved as a genuine fixed point revenue(N) = Opex(N).
"""
from __future__ import annotations

import numpy as np

import params as P


# ---------------------------------------------------------------------------
# Opex(N)
# ---------------------------------------------------------------------------

def fit_opex_blocks() -> dict:
    """Fit each opex BLOCK separately as fixed + variable x N against its own
    driver population, using the brief's 7.4 anchors.

    The brief's anchors are labelled Y1 (500) / Y3 (12,000) / Y10 (80,000) and
    it publishes a 'cost per investor' row against them. Its own 14 default
    says the Y10 target counts investors STILL CONTRIBUTING, so the anchors are
    read as contributing-account counts. See P.OPEX_ANCHOR_N.

    Blocks are split by driver because they genuinely scale on different
    populations:
      - holding-driven : a lapsed holder is still screened, still holds metal,
                         still contacts support
      - contributing   : headcount and marketing track the paying book
      - fixed          : licences, audit, corporate - do not scale with N
    """
    out = {}
    for block, spec in P.OPEX_BLOCKS.items():
        driver = spec["driver"]
        anchors = spec["anchors"]
        if driver == "fixed":
            # "Fixed" means it does not scale with N, NOT that it is constant
            # over time. VARA supervision, audit and legal all step with the
            # business's age and licence perimeter, so they are carried as a
            # year-indexed step schedule interpolated log-linearly between the
            # brief's own Y1/Y3/Y10 anchors.
            out[block] = {"driver": driver, "fixed": 0.0, "variable": 0.0,
                          "steps": anchors}
            continue
        ns = [P.OPEX_ANCHOR_N[driver][y] for y in (1, 3, 10)]
        cs = [anchors[y] for y in (1, 3, 10)]
        X = np.array([[1.0, n] for n in ns])
        coef, *_ = np.linalg.lstsq(X, np.array(cs), rcond=None)
        fixed, var = float(coef[0]), float(coef[1])
        # A negative fixed component is an artefact of a 3-point fit on a
        # convex cost curve; clamp it and refit the slope through the origin.
        if fixed < 0:
            fixed = 0.0
            var = float(np.dot(ns, cs) / np.dot(ns, ns))
        out[block] = {"driver": driver, "fixed": fixed, "variable": var}
    return out


OPEX_FIT = fit_opex_blocks()


def _step_value(steps: dict, year: int) -> float:
    """Log-linear interpolation between the Y1/Y3/Y10 anchors (F32)."""
    y = min(max(year, 1), 10)
    if y in steps:
        return float(steps[y])
    lo = max(k for k in steps if k < y)
    hi = min(k for k in steps if k > y)
    v_lo, v_hi = float(steps[lo]), float(steps[hi])
    if v_lo <= 0 or v_hi <= 0:
        w = (y - lo) / (hi - lo)
        return v_lo + w * (v_hi - v_lo)
    return v_lo * (v_hi / v_lo) ** ((y - lo) / (hi - lo))


def _y1_ramp(month_in_year: int, uplift: float) -> float:
    """Linear Year-1 hiring ramp, mean exactly 1.0, ending the year at `uplift`.

    Solves a + b*(m-1) with mean 1 over m=1..12 and value `uplift` at m=12:
        b = (uplift - 1) / 5.5,  a = 1 - 5.5*b
    So the Y1 TOTAL is unchanged and only its distribution moves - the December
    run-rate becomes `uplift` x the annual average.
    """
    b = (uplift - 1.0) / 5.5
    a = 1.0 - 5.5 * b
    return max(0.0, a + b * (month_in_year - 1))


def opex_annual_of_n(contributing: float, holding: float,
                     fit: dict | None = None, year: int = 10) -> float:
    """Annualised opex evaluated on the MODEL'S OWN book, block by block.

    N-driven blocks scale with the model's own populations; year-indexed blocks
    (licences, audit, legal) step with the business's age, not with N.
    """
    fit = fit or OPEX_FIT
    total = 0.0
    for block, f in fit.items():
        if f["driver"] == "fixed":
            total += _step_value(f["steps"], year)
        elif f["driver"] == "contributing":
            total += f["fixed"] + f["variable"] * contributing
        else:
            total += f["fixed"] + f["variable"] * holding
    return total


def opex_monthly(month: int, contributing: float = 0.0,
                 holding: float = 0.0) -> float:
    """Monthly opex charged against the model's own account counts.

    VARA supervision is an annual invoice booked in full in the anniversary
    month, not smoothed - it matters for the cash view.

    S48 (OPEX_Y1_EXIT_UPLIFT) is applied WITHIN Year 1 only. The brief's Y1
    anchor is a build-up year AVERAGE, not a run-rate: the business has not
    finished hiring, so the exit run-rate is ~1.40x the average. Ramping M1->M12
    from below to above the average preserves the Y1 total while making the
    December exit rate the uplift multiple of it - which is what makes an
    early-year break-even honest. Previously this parameter was declared and
    never read, so flexing it in the tornado returned a swing of exactly zero.
    """
    yr = P.year_of(month)
    annual = opex_annual_of_n(contributing, holding, year=yr)
    if yr == 1:
        annual *= _y1_ramp((month - 1) % 12 + 1, P.OPEX_Y1_EXIT_UPLIFT)
    m_in_year = (month - 1) % 12 + 1
    vara_usd = P.VARA_SUPERVISION_AED / P.AED_PER_USD
    smooth = max(0.0, annual - vara_usd) / 12.0
    if m_in_year == 1:
        return smooth + vara_usd
    return smooth


def opex_of_n(n_accounts: float, fit: dict | None = None,
              holding_ratio: float = 1.0, year: int = 10) -> float:
    """Annualised opex at an arbitrary CONTRIBUTING count - break-even input.

    holding_ratio converts contributing -> holding, since the two populations
    diverge sharply (~3x by Y10) and the holding-driven blocks scale on the
    larger one.
    """
    return opex_annual_of_n(n_accounts, n_accounts * holding_ratio, fit, year)


# ---------------------------------------------------------------------------
# Custody / vault - scales with ALL HOLDING accounts, not active ones
# ---------------------------------------------------------------------------

def vault_cost(grams_held: float, mode: str) -> float:
    """Vault cost under ONE pricing regime, selected by P.VAULT_REGIME.

    These are alternative vendor archetypes, not a menu to minimise over:
      'per_kg'     - DGCX-style tariff: USD 0.10/kg/day with a USD 25/day
                     minimum. The minimum binds below ~250 kg.
      'ad_valorem' - BullionVault / GoldMoney style: a percentage of value per
                     year (S14), also with a monthly minimum.
    v1.0 effectively took min(per_kg, ad_valorem), which is not a real quote
    from anyone and understates cost by ~10x at Y10.
    """
    kg = grams_held / 1000.0
    minimum = P.VAULT_MIN_USD_PER_DAY * 30.0
    if P.VAULT_REGIME == "per_kg":
        return max(minimum, kg * P.VAULT_RATE_PER_KG_DAY * 30.0)
    ad_valorem = grams_held * P.GOLD_USD_PER_G * P.VAULT_RATE[mode] / 12.0
    return max(minimum, ad_valorem)


def screening_cost(holding_accounts: float, new_accounts: float) -> float:
    """Continuous AML screening covers every HOLDING account, lapsed included."""
    checks = new_accounts
    variable = checks * P.SUMSUB_PER_CHECK
    return max(P.SUMSUB_MONTHLY_MIN, variable) + holding_accounts * 0.36 / 12.0


# ---------------------------------------------------------------------------
# Redemption - net-flow logic (corpus item 1)
# ---------------------------------------------------------------------------

def redemption_cost(gross_exit_grams: float, gross_inflow_grams: float,
                    events: float, gold_px: float = None,
                    bid_side_cost_usd: float = 0.0) -> dict:
    """Stream 0. VARA Annex 2 III.E.4 forbids any redemption fee, so this is a
    mandatory cost with zero revenue against it.

    Two terms:

    HANDLING, per event: outbound payment 1.00-2.50 + AML re-screen 1.85 +
    handling 1.00-4.50 (F20).

    DEALER DISPOSAL, on net outflow only. In a growing book this is ZERO: gross
    exits do not drive physical sales, because inflow in the same month covers
    them and the metal is simply re-allocated. It bites only in a shrinking
    book.

    ⚠ D33 CHANGES THE RATE THIS IS CHARGED AT. The old model used a symmetric
    1.0% "two-way spread". Correction 35 measured the bid as spot - 1.50%, and
    near-flat across denomination while the ask premium moves ~194bp. So the
    disposal side is charged at the OBSERVED BID, not at half a round trip, and
    `bid_side_cost_usd` from the D33 routing is passed through here rather than
    being netted against the fabrication premium paid on the way in.
    """
    gold_px = P.GOLD_USD_PER_G if gold_px is None else gold_px
    net_flow = gross_inflow_grams - gross_exit_grams
    physical = max(0.0, -net_flow)
    spread_cost = physical * gold_px * P.DEALER_BID_DISCOUNT
    handling = events * P.REDEMPTION_COST_PER_EVENT
    return {"net_flow_grams": net_flow, "physical_sold_grams": physical,
            "spread_cost": spread_cost, "handling": handling,
            "bid_side_cost": bid_side_cost_usd,
            "total": spread_cost + handling + bid_side_cost_usd}


# ---------------------------------------------------------------------------
# Card programme fixed cost stack (F27)
# ---------------------------------------------------------------------------

def card_fixed_cost(month: int, card_enabled: bool) -> float:
    """A contra-cost on stream 2, NOT opex - burying it in opex hides that it
    only exists if the card exists."""
    if not card_enabled:
        return 0.0
    c = 0.0
    if month == P.CARD_SETUP_MONTH:
        c += P.CARD_FIXED["bin_setup"] + P.CARD_FIXED["scheme_join"]
    if month >= P.CARD_LAUNCH_MONTH:
        c += P.CARD_FIXED["bin_monthly"] + P.CARD_FIXED["processor_monthly"]
        if month % 3 == 0:
            c += P.CARD_FIXED["scheme_quarterly"]
    return c


def card_variable_cost(spend_usd: float, cards_issued: dict, txn_count: float,
                       mode: str) -> dict:
    fraud = spend_usd * P.CARD_FRAUD_BPS[mode] / 10_000.0
    disputes = txn_count / 1000.0 * P.DISPUTES_PER_1000_TXN * P.DISPUTE_COST_USD
    production = sum(n * P.CARD_PRODUCTION_COST_USD[t] for t, n in cards_issued.items())
    return {"fraud": fraud, "disputes": disputes, "production": production,
            "total": fraud + disputes + production}


# ---------------------------------------------------------------------------
# Acquisition cost
# ---------------------------------------------------------------------------

def acquisition_cost(new_by_channel: dict, marketing_spend: float,
                     entry_fee_revenue: float) -> dict:
    """Agent commission + referral reward + paid marketing."""
    agent_n = new_by_channel.get("Agent", 0.0)
    referral_n = new_by_channel.get("Referral", 0.0)
    agent_cost = agent_n * P.CAC_BASE * 0.6
    referral_cost = referral_n * P.CAC_BASE * 0.35
    return {"agent": agent_cost, "referral": referral_cost,
            "marketing": marketing_spend,
            "total": agent_cost + referral_cost + marketing_spend}


def effective_cac(monthly_spend: float, mode: str) -> float:
    """S25: a flat CAC lets the model buy unlimited growth at a constant price,
    which makes the break-even year an artefact of the marketing budget."""
    base = P.CAC_BASE
    if monthly_spend <= 0:
        return base
    return base * (1.0 + P.CAC_UPLIFT * (monthly_spend / P.CAC_DIVISOR) ** P.CAC_EXPONENT)


# ---------------------------------------------------------------------------
# Tax - annual, in the final month of the financial year
# ---------------------------------------------------------------------------

class TaxEngine:
    """UAE corporate tax with indefinite loss carry-forward capped at 75%.

    The 75% cap means Aurumix pays real cash tax from its first profitable year
    even though it is cumulatively loss-making - it cannot shelter the full
    profit. v1.0 has no line for this.
    """

    def __init__(self):
        self.loss_pool = 0.0

    def annual_tax(self, accounting_profit: float) -> dict:
        if P.ASSUME_QFZP:
            return {"tax": 0.0, "loss_used": 0.0, "loss_pool": self.loss_pool,
                    "taxable": 0.0}
        used = min(self.loss_pool, P.LOSS_CARRYFORWARD_CAP * max(0.0, accounting_profit))
        taxable = accounting_profit - used
        threshold = P.CORP_TAX_THRESHOLD_AED / P.AED_PER_USD
        tax = P.CORP_TAX_RATE * max(0.0, taxable - threshold)
        self.loss_pool = self.loss_pool - used + max(0.0, -accounting_profit)
        return {"tax": tax, "loss_used": used, "loss_pool": self.loss_pool,
                "taxable": max(0.0, taxable)}


def vat_on_fees(fee_revenue_by_segment: dict) -> dict:
    """5% standard-rated for UAE residents; export-of-services zero-rating for
    non-residents, haircut 20% for input-VAT drag."""
    resident = nonresident = 0.0
    for seg, rev in fee_revenue_by_segment.items():
        share = P.RESIDENT_SHARE.get(seg, 1.0)
        resident += rev * share
        nonresident += rev * (1.0 - share)
    cost = resident * P.VAT_RATE
    benefit = nonresident * P.VAT_RATE * (1.0 - P.VAT_INPUT_DRAG)
    return {"vat_cost": cost, "zero_rating_benefit": benefit,
            "nonresident_share": nonresident / max(1e-9, resident + nonresident)}


# ---------------------------------------------------------------------------
# Regulatory capital
# ---------------------------------------------------------------------------

def required_capital(trailing_24m_avg_reserves: float, option_b: bool) -> float:
    """Option A returns the AED 1.5m floor at every period - which is the point.
    Option B's 2% escalator reaches ~USD 4m at USD 200m of reserves."""
    floor = P.MIN_CAPITAL_AED / P.AED_PER_USD
    if not option_b:
        return floor
    return max(floor, P.RESERVE_CAPITAL_PCT * trailing_24m_avg_reserves)
