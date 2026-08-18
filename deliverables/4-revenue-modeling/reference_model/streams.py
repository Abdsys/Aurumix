"""Revenue streams 1-6 plus the spot lane.

Stream 1 : entry fee margin (SIP) + spot sub-stream
Stream 2 : card interchange - NET of the per-transaction processor fee, which
           is a regressive tax on the lowest tier and stacks multiplicatively
           with the PM share
Stream 3 : family plan and digital will
Stream 4 : cardholder fees (FX, ATM over-allowance, issuance)
Stream 5 : lending revenue share, with the S40 turnover correction
Stream 6 : B2B platform fee (AUM only - never entry spread, per SafeGold)
"""
from __future__ import annotations

import math

import params as P


# ---------------------------------------------------------------------------
# Price-gap: recomputed, never hard-coded (it moves with scale and volatility)
# ---------------------------------------------------------------------------

def pricegap_rate(annual_purchase_usd: float, bar_grams: float, vol: float) -> float:
    if annual_purchase_usd <= 0:
        return 0.0
    bar_value = bar_grams * P.GOLD_USD_PER_G
    annual_grams = annual_purchase_usd / P.GOLD_USD_PER_G
    cycles = max(1e-9, annual_grams / bar_grams)
    window_days = 365.0 / cycles
    sigma_win = vol * math.sqrt(window_days / 365.0)
    return (bar_value * sigma_win * math.sqrt(cycles)) / annual_purchase_usd


def float_grams(bar_g: float, daily_inflow_g: float, buffer_days: int) -> float:
    """Corpus rule: float >= 1 bar + N days trailing inflow; 2 bars at launch."""
    return max(P.FLOAT_BARS_LAUNCH * bar_g, bar_g + buffer_days * daily_inflow_g)


def solve_bar_denomination(annual_grams: float, vol: float,
                           coc: float = None) -> tuple:
    """T3 solved ENDOGENOUSLY against the model's own volume.

    v1.0 hard-codes 100g -> 1kg at Y3 -> 12.4kg at Y8, a schedule indexed to a
    volume trajectory (80,000 investors, ~509 kg/yr) that the corrected model
    never reaches. At the real volume that denomination is simply wrong: filling
    a 12.4 kg Good Delivery bar only ~9 times a year is a large unhedged carry,
    and the price-gap term swamps the premium saving.

    Applies the brief's own T3 rule: upgrade only when
        (annual grams x premium saved per gram)
            > (incremental float x cost of capital) + incremental price-gap risk

    Returns (bar_grams, premium_rate, decision_log).
    """
    coc = P.FLOAT_COC_RATE if coc is None else coc
    ladder = P.BAR_LADDER          # [(grams, premium), ...] ascending
    chosen = ladder[0]
    log = []
    for nxt in ladder[1:]:
        cur_g, cur_prem = chosen
        nxt_g, nxt_prem = nxt
        if annual_grams <= 0:
            break
        premium_saved = annual_grams * P.GOLD_USD_PER_G * (cur_prem - nxt_prem)
        # Incremental float capital tied up by the larger bar.
        inc_float = (P.FLOAT_BARS_LAUNCH * (nxt_g - cur_g)) * P.GOLD_USD_PER_G
        inc_float_cost = inc_float * coc
        annual_usd = annual_grams * P.GOLD_USD_PER_G
        pg_cur = pricegap_rate(annual_usd, cur_g, vol) * annual_usd
        pg_nxt = pricegap_rate(annual_usd, nxt_g, vol) * annual_usd
        inc_pricegap = pg_nxt - pg_cur
        benefit = premium_saved
        cost = inc_float_cost + inc_pricegap
        clears = benefit > cost
        log.append({"from_g": cur_g, "to_g": nxt_g,
                    "premium_saved": premium_saved,
                    "incremental_float_cost": inc_float_cost,
                    "incremental_pricegap": inc_pricegap,
                    "clears": clears})
        if clears:
            chosen = nxt
        else:
            break
    return chosen[0], chosen[1], log


# ---------------------------------------------------------------------------
# Stream 1 - entry fee margin, SIP and spot
# ---------------------------------------------------------------------------

def entry_fee_margin(inflow_usd: float, collection_events: float,
                     fee_rate: float, premium: float, pricegap: float,
                     float_coc_usd: float, rail_cost: float) -> dict:
    """Net = C x (f - c) - R.

    float_coc is passed as an ABSOLUTE cost derived from the sized float, not
    as a flat % of inflow (F5 has no derivation; the corpus says so).
    """
    if inflow_usd <= 0:
        return {"gross_margin": 0.0, "cogs": 0.0, "pricegap": 0.0,
                "float_coc": 0.0, "rail": 0.0, "net": 0.0}
    net_of_fee = inflow_usd * (1.0 - fee_rate)
    cogs = net_of_fee * premium
    gross_margin = inflow_usd - net_of_fee * (1.0 + premium)
    pg = inflow_usd * pricegap
    rail = collection_events * rail_cost
    return {"gross_margin": gross_margin, "cogs": cogs, "pricegap": pg,
            "float_coc": float_coc_usd, "rail": rail,
            "net": gross_margin - pg - float_coc_usd - rail}


# ---------------------------------------------------------------------------
# Stream 2 - card interchange, net of per-transaction fees
# ---------------------------------------------------------------------------

def effective_pm_share(tier: str, pm_share: float, avg_txn_aed: float) -> float:
    """The correction the brief flagged and did not run.

    A flat USD 0.10 per authorised transaction is 0.199% of a AED 185 ticket
    against a 1.80% gross rate = 11.0% of gross interchange at Gold, but only
    5.6% at Sovereign. So the EFFECTIVE PM share on small tickets is materially
    below the contracted PM share, and it must be computed per tier.
    """
    gross_rate = P.INTERCHANGE[tier]
    txn_usd = avg_txn_aed / P.AED_PER_USD
    if txn_usd <= 0:
        return pm_share
    fee_as_pct = (P.PER_TXN_PROCESSOR_FEE * (1.0 + P.DECLINE_UPLIFT)) / txn_usd
    net_rate = gross_rate * pm_share - fee_as_pct
    return net_rate / gross_rate if gross_rate > 0 else 0.0


def interchange(spend_by_tier: dict, pm_share: float, prepaid_capped: bool = False) -> dict:
    """Gross and net interchange, with the per-transaction fee broken out."""
    gross = net = txn_fees = 0.0
    txn_count = 0.0
    for tier, spend_usd in spend_by_tier.items():
        if spend_usd <= 0:
            continue
        rate = P.INTERCHANGE_PREPAID_CAP if prepaid_capped else P.INTERCHANGE[tier]
        g = spend_usd * rate
        spend_aed = spend_usd * P.AED_PER_USD
        n = spend_aed / P.AVG_TXN_SIZE_AED[tier] * (1.0 + P.DECLINE_UPLIFT)
        f = n * P.PER_TXN_PROCESSOR_FEE
        gross += g
        txn_fees += f
        txn_count += n
        net += g * pm_share - f
    return {"gross": gross, "processor_fees": txn_fees, "net": max(0.0, net),
            "transactions": txn_count}


def gold_rewards_cost(spend_by_tier: dict, cards_by_tier: dict,
                      cum_interchange: float, cum_credit: float,
                      cum_custody: float) -> float:
    """Capped at the customer-generated revenue net of custody. Never independent.

    F13's USD 3,000/month qualifying-spend cap is PER CARDHOLDER, so it must be
    applied to per-card spend and then multiplied by the card count. Applying it
    to a tier's aggregate spend understates the cost by roughly the cardholder
    count - a ~1000x error at scale.
    """
    raw = 0.0
    for tier, spend_usd in spend_by_tier.items():
        n = cards_by_tier.get(tier, 0.0)
        if n <= 0 or spend_usd <= 0:
            continue
        per_card = spend_usd / n
        qualifying = min(per_card, P.GOLD_REWARDS_SPEND_CAP) * n
        raw += qualifying * P.GOLD_REWARDS_RATE.get(tier, 0.0)
    ceiling = max(0.0, cum_interchange + cum_credit - cum_custody)
    return min(raw, ceiling)


# ---------------------------------------------------------------------------
# Stream 4 - cardholder fees
# ---------------------------------------------------------------------------

def atm_over_allowance_aed(allowance_aed: float) -> float:
    """Distributional, not mean-based.

    Applying 2% to max(0, mean - allowance) gives ZERO at the Base mean of
    AED 940 against a AED 1,000 Gold allowance. The revenue is generated
    entirely by a small high-cash tail, so the distribution must be used.
    """
    return sum(w * max(0.0, draw - allowance_aed) for draw, w in P.ATM_DISTRIBUTION)


def cardholder_fees(cards_by_tier: dict, spend_by_tier: dict,
                    foreign_share: float, issuance_events: dict,
                    replacement_events: dict) -> dict:
    fx = atm = fees = 0.0
    for tier, n in cards_by_tier.items():
        if n <= 0:
            continue
        fx += spend_by_tier.get(tier, 0.0) * foreign_share * P.FX_MARGIN[tier]
        over_aed = atm_over_allowance_aed(P.ATM_FREE_ALLOWANCE_AED[tier])
        atm += n * over_aed * P.ATM_OVER_FEE / P.AED_PER_USD
        fees += (issuance_events.get(tier, 0.0) * P.CARD_ISSUANCE_FEE_AED[tier]
                 + replacement_events.get(tier, 0.0) * P.CARD_REPLACEMENT_FEE_AED[tier]
                 ) / P.AED_PER_USD
    return {"fx": fx, "atm": atm, "issuance": fees, "total": fx + atm + fees}


# ---------------------------------------------------------------------------
# Stream 5 - lending, with the S40 turnover correction
# ---------------------------------------------------------------------------

def credit_revenue(eligible_collateral_usd: dict, takeup: float, drawn_pct: float,
                   turnover: float, draw_events_per_year: float) -> dict:
    """v1.0 computes PEAK drawn and prices it as though it persisted.

    Manappuram's realised tenor is 71 days against a 6-12 month product, so the
    average balance is ~0.42x peak. Applying S40 to the interest component
    roughly halves stream 5. Origination is per-EVENT and therefore rises with
    turnover, so it is deliberately left un-discounted.
    """
    peak = avg = 0.0
    for tier, collateral in eligible_collateral_usd.items():
        if collateral <= 0:
            continue
        limit = collateral * P.LTV_LADDER[tier]
        peak += limit * takeup * drawn_pct
    avg = peak * turnover

    interest = avg * P.CREDIT_INTEREST_SHARE_PP
    borrowers = 0.0
    draw_vol = peak * draw_events_per_year
    orig_rate, orig_share = P.CREDIT_ORIGINATION
    origination = draw_vol * orig_rate * orig_share
    srv_rate, srv_share = P.CREDIT_SERVICING
    servicing = avg * srv_rate * srv_share
    pen_rate, pen_share = P.CREDIT_PENAL
    penal = avg * 0.02 * pen_rate * pen_share      # ~2% of balances late
    rec_rate, rec_share = P.CREDIT_RECOVERY
    recovery = 0.0 if rec_share == 0 else avg * 0.001 * rec_rate * rec_share

    return {"peak_drawn": peak, "avg_drawn": avg, "interest": interest / 12.0,
            "origination": origination / 12.0, "servicing": servicing / 12.0,
            "penal": penal / 12.0, "recovery": recovery / 12.0,
            "total": (interest + origination + servicing + penal + recovery) / 12.0}


# ---------------------------------------------------------------------------
# Stream 6 - B2B platform fee, AUM only
# ---------------------------------------------------------------------------

def b2b_aum(month: int, mode: str, india_enabled: bool) -> float:
    """Per-partner S-curve on each partner's own clock.

    Partners signed in Y7 are still ramping at Y10, so the terminal figure comes
    from a few mature partners plus a tail of immature ones.
    """
    if month < P.B2B_LAUNCH_MONTH:
        return 0.0
    schedule = P.B2B_PARTNERS_BY_YEAR[mode]
    terminal = P.B2B_TERMINAL_AUM_PER_PARTNER[mode]
    if not india_enabled:
        # S16's B2B row is 60% S5; the post-SEBI partner set is Indian wallets.
        terminal *= 0.40

    ramp_pts = sorted(P.B2B_RAMP.items())

    def ramp(age_m):
        if age_m <= 0:
            return 0.0
        if age_m >= ramp_pts[-1][0]:
            return ramp_pts[-1][1]
        prev = (0, 0.0)
        for pt in ramp_pts:
            if age_m < pt[0]:
                span = pt[0] - prev[0]
                w = (age_m - prev[0]) / span if span else 0.0
                return prev[1] + w * (pt[1] - prev[1])
            prev = pt
        return ramp_pts[-1][1]

    # Reconstruct each partner's go-live month from the annual count schedule.
    total = 0.0
    prev_count = 0
    for yr in sorted(schedule):
        count = schedule[yr]
        new = count - prev_count
        golive = (yr - 1) * 12 + 1
        for _ in range(max(0, new)):
            total += terminal * ramp(month - golive)
        prev_count = count
    return total


def b2b_fee(aum_usd: float) -> float:
    return aum_usd * P.B2B_FEE_BPS / 12.0


# ---------------------------------------------------------------------------
# Stream 3 - family plan
# ---------------------------------------------------------------------------

def family_revenue(accounts_by_tier: dict, attach: float) -> dict:
    rev = cost = 0.0
    names = 0.0
    for tier, n in accounts_by_tier.items():
        attached = n * attach
        if attached <= 0:
            continue
        price = P.FAMILY_PRICE_ANNUAL * (1.0 - P.FAMILY_DISCOUNT.get(tier, 0.0))
        extra = max(0.0, P.FAMILY_AVG_NAMES - P.FAMILY_NAMES_INCLUDED)
        rev += attached * (price + extra * P.FAMILY_EXTRA_NAME_PRICE) / 12.0
        names += attached * P.FAMILY_AVG_NAMES
        cost += attached * P.FAMILY_AVG_NAMES * P.FAMILY_COST_PER_NAME_ANNUAL / 12.0
    return {"revenue": rev, "cost": cost, "names": names}


# ---------------------------------------------------------------------------
# Spot lane
# ---------------------------------------------------------------------------

def spot_volume(live_accounts_by_seg: dict, month: int, mode: str,
                tenure_years: float) -> dict:
    """Spot is priced at the account's earned tier (rulebook 1.1 + decision 44),
    earns no ICS, and counts in Retention on both sides.

    Structurally the highest-margin inflow: same fee, ~8x the ticket, ONE rail
    event. It is the only inflow-linked flow that survives the adverse rail.
    """
    attach = P.SPOT_ATTACH[mode]
    ticket = P.SPOT_TICKET[mode]
    freq = P.SPOT_FREQ[mode]
    uplift = min(2.0, 1.0 + P.SPOT_TENURE_UPLIFT_PER_YEAR * tenure_years)
    vol = 0.0
    events = 0.0
    for seg, n in live_accounts_by_seg.items():
        if n <= 0:
            continue
        seg_ticket = ticket * P.SPOT_SEGMENT_SCALE.get(seg, 1.0)
        ev = n * attach * uplift * freq / 12.0
        vol += ev * seg_ticket
        events += ev
    return {"volume": vol, "events": events}
