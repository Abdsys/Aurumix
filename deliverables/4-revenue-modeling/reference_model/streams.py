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


def redeemed_gold_routing(redeemed_grams: float, withdrawn_grams: float,
                          grams_required: float, float_capacity_grams: float,
                          current_float_grams: float, gold_px: float,
                          to_float: bool = None) -> dict:
    """D33: where redeemed gold goes, and therefore what the premium lands on.

    ⚠ THIS DECISION DID NOT EXIST. Correction 30 found that D30 (charge the
    fabrication premium on net new grams, not gross inflow) holds ONLY if
    redeemed gold comes back to the float. If it goes to the dealer there is
    nothing to recycle and the premium lands on gross inflow after all. Nobody
    had written down which. D33 settles it:

        Redeemed grams return to the float up to the float ceiling. Any excess
        is sold back to the dealer at the observed bid of spot - 1.50%.

    🔴 THE TWO SIDES ARE NOT SYMMETRIC AND MUST NOT BE NETTED AS IF THEY WERE.
    Correction 35 measured the dealer BID as near-flat across denomination while
    the ASK premium moves ~194bp. Fabrication is paid on the way IN and is not
    recovered on the way OUT. So the model pays the full premium to acquire and
    takes the full bid discount to dispose; it never books the difference as a
    round-trip spread, which would flatter both sides.

    SELF-CUSTODY WITHDRAWALS DO NOT RECYCLE. A withdrawal to self-custody takes
    the metal off the platform entirely - it is not available for re-allocation,
    so it never reduces the premium base.

    Returns the net-new-gram share the premium is charged on, plus the bid-side
    disposal cost.
    """
    if to_float is None:
        to_float = P.REDEEMED_GOLD_TO_FLOAT

    redeemed_grams = max(0.0, redeemed_grams)
    if not to_float:
        # Everything redeemed goes straight back to the dealer. Nothing is
        # recycled, so D30 collapses and the premium lands on gross inflow.
        return {"recycled_grams": 0.0, "sold_back_grams": redeemed_grams,
                "net_new_grams": grams_required,
                "net_new_gram_share": 1.0,
                "bid_side_cost_usd": redeemed_grams * gold_px
                                     * P.DEALER_BID_DISCOUNT,
                "routing": "dealer"}

    headroom = max(0.0, float_capacity_grams - current_float_grams)
    recycled = min(redeemed_grams, headroom, grams_required)
    sold_back = max(0.0, redeemed_grams - recycled)
    net_new = max(0.0, grams_required - recycled)
    share = (net_new / grams_required) if grams_required > 0 else 1.0
    return {"recycled_grams": recycled, "sold_back_grams": sold_back,
            "net_new_grams": net_new, "net_new_gram_share": share,
            "bid_side_cost_usd": sold_back * gold_px * P.DEALER_BID_DISCOUNT,
            "routing": "float"}


def solve_bar_denomination(annual_grams: float, vol: float,
                           coc: float = None, mode: str = "Base") -> tuple:
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
    # D28 retired the 12.4kg Good Delivery rung: Dubai's standard bar is 1kg and
    # the 12.4kg rung was never a real procurement option at this volume, so
    # carrying it let the model claim a premium saving it could never realise.
    # The ladder is now scenario-resolved because F4's LEVEL failed replication
    # (correction 36) even though its denomination SHAPE is corroborated.
    ladder = P.bar_ladder(mode)    # [(grams, premium), ...] ascending
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
                     float_coc_usd: float, rail_cost: float,
                     net_new_gram_share: float = 1.0) -> dict:
    """STREAM1 = gross_margin - pricegap.   (D31, D32)

    THE FORMULA, AND WHY IT IS NOT HARDCODED
    ----------------------------------------
    Correction 26 is a live self-contradiction in the brief: §3 Layer 4 and
    §6.1b both state a stream-1 gross margin of 0.72%, while §6.1's own
    waterfall gives 2.15%. The exact identity is

        gross_margin = C - C(1-f)(1+p)

    on a contribution C at fee f with fabrication premium p. That is what is
    implemented. The model PRODUCES the number; neither figure is typed in.

    D30 / D33 - THE PREMIUM LANDS ON NET NEW GRAMS
    ----------------------------------------------
    The fabrication premium is paid to the dealer only on metal Aurumix
    actually procures. Grams recycled out of a redemption are re-allocated
    without re-paying fabrication, so the premium base is scaled by

        net_new_gram_share = net_new_grams / grams_required

    `net_new_gram_share = 1.0` reproduces the old gross-inflow treatment.

    D31 - THE RAIL IS NOT DEDUCTED
    ------------------------------
    `rail_cost` is still accepted and still returned, but ONLY as a memo. It is
    not in `net`. Aurumix asks the customer for (ticket + rail), remits the rail
    to the PSP and books zero margin on it. Putting it in the margin charged
    Aurumix for a third party's fee.

    D32 - THE FLOAT CARRY IS NOT DEDUCTED
    -------------------------------------
    `float_coc_usd` is likewise returned as a memo only. It is an imputed cost
    of equity; nothing invoices Aurumix for it, and a statutory P&L does not
    book an equity cost of capital inside cost of goods sold. The float
    PRINCIPAL is untouched and stays in the funding view.
    """
    if inflow_usd <= 0:
        return {"gross_margin": 0.0, "cogs": 0.0, "pricegap": 0.0,
                "float_coc_memo": 0.0, "rail_memo": 0.0, "net": 0.0,
                "gross_margin_pct": 0.0, "net_pct": 0.0}

    net_of_fee = inflow_usd * (1.0 - fee_rate)
    premium_base = net_of_fee * max(0.0, min(1.0, net_new_gram_share))
    cogs = premium_base * premium
    # The exact identity, with the premium landing only on net new grams.
    gross_margin = inflow_usd - net_of_fee - cogs
    pg = inflow_usd * pricegap
    rail_memo = collection_events * rail_cost
    net = gross_margin - pg
    return {"gross_margin": gross_margin, "cogs": cogs, "pricegap": pg,
            # MEMO LINES. Neither appears in `net`, and check 12/13 assert that
            # neither appears in any revenue or cost total.
            "float_coc_memo": float_coc_usd, "rail_memo": rail_memo,
            "net": net,
            "gross_margin_pct": gross_margin / inflow_usd,
            "net_pct": net / inflow_usd}


def rail_gross_up(ticket_usd: float, rail_cost: float) -> dict:
    """D31: what the customer is actually asked for, and what that costs them.

    Aurumix requests `ticket + rail` and remits the rail. Aurumix books nothing,
    so the P&L is unaffected - but the INCIDENCE moved onto the customer, and it
    is regressive: a fixed USD 0.25 is 1.25% of a USD 20 floor-band contribution
    and only 0.50% of a USD 50 standard-band one. Carried and reported per band,
    because "the rail left the P&L" is not the same as "the rail went away".
    """
    if ticket_usd <= 0:
        return {"request_amount": 0.0, "gross_up_pct": 0.0}
    return {"request_amount": ticket_usd + rail_cost,
            "gross_up_pct": rail_cost / ticket_usd}


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


def interchange(spend_by_tier: dict, pm_share: float, prepaid_capped: bool = False,
                collapsed: bool = None) -> dict:
    """Gross and net interchange, with the per-transaction fee broken out.

    D22: under the collapsed ladder EVERY live tier reads the FLAT GOLD RATE of
    1.80%. The full 1.80 / 2.05 / 2.10 ladder survives only on the validation
    path, for the 5% safety gate (check 15). Reading `P.INTERCHANGE[tier]` here
    would silently un-do the collapse, which is precisely the failure the check
    exists to catch.
    """
    if collapsed is None:
        collapsed = P.COLLAPSE_TIER_LADDER
    gross = net = txn_fees = 0.0
    txn_count = 0.0
    for tier, spend_usd in spend_by_tier.items():
        if spend_usd <= 0:
            continue
        if prepaid_capped:
            rate = P.INTERCHANGE_PREPAID_CAP
        elif collapsed:
            rate = P.COLLAPSE_INTERCHANGE_RATE
        else:
            rate = P.INTERCHANGE[tier]
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
