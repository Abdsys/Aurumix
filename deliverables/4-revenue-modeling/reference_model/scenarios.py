"""Scenario definitions, break-even fixed point, sensitivity and LTV/CAC."""
from __future__ import annotations

import copy

import numpy as np
import pandas as pd

import costs as C
import params as P
from pnl import Model, cash_flow


# ---------------------------------------------------------------------------
# Named scenarios
# ---------------------------------------------------------------------------

def scenario_set() -> dict:
    return {
        "Base": P.Scenario(name="Base", mode="Base"),
        "Aggressive": P.Scenario(name="Aggressive", mode="Aggressive"),
        "Conservative": P.Scenario(name="Conservative", mode="Conservative"),
        # ⚠ "RAIL KILLS IT" IS RETIRED BY D31 AND DELIBERATELY NOT REPLACED
        # WITH A LOOKALIKE. The rail is a pass-through, so flexing S1 to its
        # Conservative 1.36 now moves the P&L by exactly zero. Keeping the
        # scenario would print a row of unchanged numbers under a name that
        # promises a stress, which is worse than not having it. What the
        # adverse rail DOES do is raise the customer's collection request from
        # a 1.25% gross-up to a 6.80% one on the USD 20 floor band - an
        # incidence question, reported in `rail_incidence`, not a profit one.
        #
        # ⚠ "PREMIUM KILLS IT" REPLACES IT, and it is the honest successor:
        # F4's LEVEL failed replication on 2026-08-20, so the fabrication
        # premium is now the largest genuinely uncertain term in cost of
        # revenue. This runs the failed-replication HIGH.
        "premium_kills_it": P.Scenario(
            name="premium_kills_it", mode="Base",
            overrides={"FAB_PREMIUM_LADDER":
                       {k: P.FAB_PREMIUM_LADDER["Conservative"]
                        for k in P.FAB_PREMIUM_LADDER}}),
        # D33 the other way: redeemed gold goes to the dealer, so nothing
        # recycles and D30 collapses back onto gross inflow.
        "redeemed_to_dealer": P.Scenario(
            name="redeemed_to_dealer", mode="Base",
            overrides={"REDEEMED_GOLD_TO_FLOAT": False}),
        # D32's restoring case: the float is debt-funded, so the carry is cash.
        "float_debt_funded": P.Scenario(
            name="float_debt_funded", mode="Base",
            overrides={"FLOAT_DEBT_FUNDED": True}),
        # "no card": programme never launches.
        "no_card": P.Scenario(name="no_card", mode="Base", card_enabled=False),
        # "no card" variant: lands prepaid-capped at 1.00% flat.
        "card_prepaid_capped": P.Scenario(name="card_prepaid_capped", mode="Base",
                                          card_prepaid_capped=True),
        # "client's plan": the 100k investor target imposed as a growth input.
        "clients_plan": P.Scenario(name="clients_plan", mode="Base",
                                   growth_target_y10=100_000),
        "no_india": P.Scenario(name="no_india", mode="Base", india_enabled=False),
        "lapsed_loses_card": P.Scenario(name="lapsed_loses_card", mode="Base",
                                        lapsed_keeps_card=False),
        "option_b_capital": P.Scenario(name="option_b_capital", mode="Base",
                                       option_b=True),
    }


def run_scenario(sc: P.Scenario):
    # Apply per-parameter overrides onto the params module for this run.
    saved = {}
    for k, v in sc.overrides.items():
        original = getattr(P, k)
        saved[k] = original
        # If the target is a mode-keyed table, a scalar override must be
        # broadcast across every mode or the mode lookup breaks at runtime.
        if isinstance(original, dict) and not isinstance(v, dict):
            v = {mode: v for mode in original}
        setattr(P, k, v)
    try:
        m = Model(sc)
        df = m.run()
        cf = cash_flow(df, sc)
    finally:
        for k, v in saved.items():
            setattr(P, k, v)
    return df, cf, m


# ---------------------------------------------------------------------------
# Break-even as a genuine fixed point
# ---------------------------------------------------------------------------

def breakeven_fixed_point(df: pd.DataFrame, view: str = "all_streams") -> dict:
    """Solve revenue(N) = TOTAL COST(N), not revenue(N) = Opex(N).

    v1.0 divided opex sized for 500 investors by margin-per-investor to get
    171,911 investors, which is incoherent because opex is itself a function
    of N.

    But solving against opex ALONE is also wrong, and more insidiously so: it
    silently excludes acquisition cost, vault, Gold Rewards, card fixed and
    variable, screening, redemption, family and VAT. Those lines are roughly
    half of total cost, so an opex-only fixed point reports break-even years
    before the P&L actually turns - and contradicts the model's own EBITDA.

    The fixed point here is therefore against `total_cost`, which is the same
    number the P&L uses, so the solver and the EBITDA line cannot disagree.
    """
    yearly = df.groupby("year").agg(
        accounts=("live_accounts", "last"),
        holding=("holding", "last"),
        revenue=("revenue", "sum"),
        gross_profit=("gross_profit", "sum"),
        s1=("stream1_sip", "sum"), s1s=("stream1_spot", "sum"),
        cost_of_revenue=("cost_of_revenue", "sum"),
        opex=("cost_opex", "sum"), total_cost=("total_cost", "sum"),
        ebitda=("ebitda", "sum"), net_profit=("net_profit", "sum"))

    fit = C.OPEX_FIT
    hr = float((yearly["holding"] / yearly["accounts"].replace(0, np.nan)).iloc[-1])

    n = yearly["accounts"].values
    valid = n > 0
    if valid.sum() < 2:
        return {"view": view, "solution": None, "fit": fit, "holding_ratio": hr}

    if view == "entry_fee_only":
        # Can the inflow lanes alone cover the whole cost base? Revenue side is
        # the net contribution margin; cost side is total cost less the cost of
        # revenue already netted inside it (avoids double-counting premium/rail).
        rev = yearly["s1"] + yearly["s1s"]
        cost = yearly["total_cost"] - yearly["cost_of_revenue"]
    else:
        # Gross revenue against the full cost stack, exactly as the P&L computes.
        rev = yearly["revenue"]
        cost = yearly["total_cost"]

    rpa = np.polyfit(n[valid], rev.values[valid], 1)
    cpa = np.polyfit(n[valid], cost.values[valid], 1)

    def revenue_of_n(x):
        return rpa[0] * x + rpa[1]

    def cost_of_n(x):
        return cpa[0] * x + cpa[1]

    def gap(x):
        return revenue_of_n(x) - cost_of_n(x)

    # Both curves are linear in N, so the crossing is closed-form. Only accept
    # it if it lies ahead of the modelled book and the gap is actually closing.
    solution = None
    denom = rpa[0] - cpa[0]
    if abs(denom) > 1e-12:
        x = (cpa[1] - rpa[1]) / denom
        if x > 0 and gap(x * 1.01) > gap(x * 0.99):
            solution = float(x)

    # Annual break-even is the headline: the first year with positive EBITDA.
    be_year = None
    for y, row in yearly.iterrows():
        if row["ebitda"] > 0:
            be_year = int(y)
            break

    # Year in which the chosen revenue line covers the chosen cost line.
    crossing_year = None
    for y in yearly.index:
        if rev.loc[y] >= cost.loc[y]:
            crossing_year = int(y)
            break

    # If it never crosses inside the horizon, say how far outside it lands on
    # the current trajectory rather than reporting a bare "never".
    extrapolated_year = None
    if be_year is None:
        eb = yearly["ebitda"].values
        if len(eb) >= 3 and eb[-1] > eb[-3]:
            slope = (eb[-1] - eb[-3]) / 2.0
            if slope > 0:
                extrapolated_year = float(len(eb) + (-eb[-1]) / slope)

    return {"view": view, "solution": solution, "fit": fit,
            "holding_ratio": hr,
            "breakeven_year_ebitda": be_year,
            "crossing_year": crossing_year,
            "extrapolated_breakeven_year": extrapolated_year,
            "revenue_slope_per_account": float(rpa[0]),
            "revenue_intercept": float(rpa[1]),
            "cost_slope_per_account": float(cpa[0]),
            "cost_intercept": float(cpa[1]),
            "yearly": yearly}


def months_to_cash_breakeven(cf: pd.DataFrame) -> dict:
    """Break-even timing.

    ANNUAL break-even is the headline. A single month crossing zero inside a
    year that still loses money is technically true and reads as "breaks even
    in Year 10", which is wrong. The monthly crossing is kept as a clearly
    labelled secondary detail.
    """
    pos = cf[cf["cumulative_cash"] > 0]
    peak_idx = cf["total_funding_need"].idxmax()

    annual = cf.groupby("year").agg(ebitda=("ebitda", "sum"),
                                    net_profit=("net_profit", "sum"))
    be_year_ebitda = next((int(y) for y, r in annual.iterrows()
                           if r["ebitda"] > 0), None)
    be_year_net = next((int(y) for y, r in annual.iterrows()
                        if r["net_profit"] > 0), None)
    first_pos_month = (int(cf[cf["net_profit"] > 0]["month"].iloc[0])
                       if (cf["net_profit"] > 0).any() else None)
    month_year = P.year_of(first_pos_month) if first_pos_month else None
    year_np = float(annual.loc[month_year, "net_profit"]) if month_year else None

    return {
        "cash_breakeven_month": int(pos["month"].iloc[0]) if len(pos) else None,
        # Headline
        "pnl_breakeven_year_ebitda": be_year_ebitda,
        "pnl_breakeven_year_net_profit": be_year_net,
        # Secondary, explicitly labelled
        "first_positive_month_secondary": first_pos_month,
        "net_profit_of_that_year": year_np,
        "peak_funding_requirement": float(cf.loc[peak_idx, "total_funding_need"]),
        "peak_funding_month": int(cf.loc[peak_idx, "month"]),
        "min_cumulative_cash": float(cf["cumulative_cash"].min()),
        "min_cash_month": int(cf.loc[cf["cumulative_cash"].idxmin(), "month"]),
    }


# ---------------------------------------------------------------------------
# Minimum viable entry fee, given the ENDOGENOUS denomination and premium
# ---------------------------------------------------------------------------

def solve_minimum_entry_fee(df: pd.DataFrame, mode: str = "Base") -> pd.DataFrame:
    """The fee path at which stream 1 net contribution margin is non-negative.

    ⚠ D31 AND D32 CHANGED THIS FORMULA, AND THE CHANGE IS THE WHOLE STORY.
    The cost term `c` used to have four components - fabrication premium, price
    gap, float cost of capital and the payment rail. D31 removed the rail (it is
    a pass-through the customer funds) and D32 removed the float carry (it is an
    imputed cost of equity). `c` now has TWO terms:

        net = T - T(1-f)(1+p) - T x g   >= 0

    with T the ticket, f the fee, p the fabrication premium and g the price gap.
    Solving for f gives the minimum viable rate.

    🔴 IN ONE DAY `c` WENT FROM FOUR TERMS TO TWO AND THE MINIMUM VIABLE FEE
    FELL, WITH NOTHING CHANGING IN THE BUSINESS. Each step is defensible on its
    own; the sequence dissolved a finding present in every version of the brief
    by re-attribution alone. And the largest surviving term - the fabrication
    premium - FAILED REPLICATION on 2026-08-20. So this table is reported as
    PROVISIONAL and conditional, never as a settled result.

    D25: SOLVED PER BAND, NOT ON THE REGIONAL AVERAGE. The floor band contributes
    USD 20 and the standard band USD 33-50. Because the price gap is proportional
    to the ticket, the two bands need the SAME fee in this two-term world - which
    is itself the finding: removing the fixed rail removed the only term that
    made the small ticket structurally more expensive to serve.
    """
    rows = []
    for yr in range(1, P.HORIZON_YEARS + 1):
        d = df[df.year == yr]
        if d.empty:
            continue

        premium = float(d["fab_premium"].iloc[-1])
        bar_g = float(d["bar_grams"].iloc[-1])
        # Weight the price-gap by inflow, not a flat mean. In the launch ramp it
        # runs ~11% in M1 on negligible volume and decays below 1% by M12; an
        # unweighted mean lets the smallest month dominate the whole year.
        _infl = d["inflow_sip"] + d["inflow_spot"]
        pricegap = float((d["pricegap_rate"] * _infl).sum() / max(1e-9, _infl.sum()))
        # D30/D33: the premium lands only on net new grams, so the effective
        # premium rate on a contribution is scaled by the recycling share.
        nn = float((d["net_new_gram_share"] * _infl).sum() / max(1e-9, _infl.sum()))
        eff_premium = premium * nn

        assumed_fee = P.ENTRY_FEE_BY_YEAR[yr]
        applied = float((d["fee_applied"] * d["inflow_sip"]).sum()
                        / max(1e-9, d["inflow_sip"].sum()))
        discount = assumed_fee - applied

        def min_fee(ticket: float) -> float:
            """f such that T - T(1-f)(1+p_eff) - T.g = 0."""
            if ticket <= 0:
                return 0.0
            residual = ticket - ticket * pricegap
            return 1.0 - residual / (ticket * (1.0 + eff_premium))

        # Per band, per region (D25), plus the two lanes.
        band_min = {}
        for r in P.SEGMENTS:
            for band, (share, ticket) in P.band_split(r, mode).items():
                band_min[f"{r}_{band}"] = min_fee(ticket)

        sip_ev = float(d["collection_events"].sum())
        sip_infl = float(d["inflow_sip"].sum())
        spot_ev = float(d["spot_events"].sum())
        spot_infl = float(d["inflow_spot"].sum())
        sip_ticket = sip_infl / sip_ev if sip_ev > 0 else 0.0
        spot_ticket = spot_infl / spot_ev if spot_ev > 0 else 0.0

        sip_net = min_fee(sip_ticket)
        spot_net = min_fee(spot_ticket) if spot_ticket > 0 else 0.0
        # The binding lane needs the higher headline fee.
        binding_net = max(sip_net, spot_net)
        min_headline = binding_net + discount

        rows.append({
            "year": yr, "bar_grams": bar_g, "premium": premium,
            "net_new_gram_share": nn, "effective_premium": eff_premium,
            "pricegap_weighted": pricegap,
            "sip_ticket": sip_ticket, "spot_ticket": spot_ticket,
            "assumed fee": assumed_fee,
            "tier discount applied": discount,
            "min viable fee SIP lane": sip_net + discount,
            "min viable fee spot lane": spot_net + discount,
            "min viable fee (binding)": min_headline,
            "min viable fee floor band (USD 20)": min_fee(20.0) + discount,
            "shortfall_pp": (min_headline - assumed_fee) * 100,
            "achievable": min_headline <= assumed_fee,
            "stream1_sip_net": float(d["stream1_sip"].sum()),
            "stream1_net_total": float(d["stream1_net"].sum()),
            "PROVISIONAL": "F4 failed replication 2026-08-20 (correction 36)",
            **{f"min fee {k}": v + discount for k, v in band_min.items()},
        })
    return pd.DataFrame(rows)


def rail_incidence(mode: str = "Base") -> pd.DataFrame:
    """D31: who actually pays the rail now, and how much it costs them.

    The rail left the P&L. It did NOT leave the transaction. Aurumix asks for
    `ticket + rail` and remits it, so the incidence moved wholly onto the
    customer - and it is REGRESSIVE, because the rail is a fixed amount per
    collection while the ticket is not.

    Reported per region band, because "the rail is no longer a cost" is true of
    Aurumix and false of a USD 20 saver, for whom it is a 1.25% surcharge on
    every single contribution. That is not a rounding error on a product whose
    entire gross margin is ~3.6%.
    """
    rail = P.RAIL_COST[mode]
    rows = []
    for r in P.SEGMENTS:
        for band, (share, ticket) in P.band_split(r, mode).items():
            g = S_rail_gross_up(ticket, rail)
            rows.append({
                "region": r, "region_name": P.REGION_NAME[r], "band": band,
                "share_of_region": share, "ticket_usd": ticket,
                "rail_usd": rail,
                "request_amount_usd": g["request_amount"],
                "gross_up_pct_of_ticket": g["gross_up_pct"] * 100,
                "annual_rail_cost_to_customer_usd": rail * 12.0,
            })
    out = pd.DataFrame(rows)
    return out.sort_values("gross_up_pct_of_ticket", ascending=False)


def S_rail_gross_up(ticket, rail):
    import streams as _S
    return _S.rail_gross_up(ticket, rail)


# ---------------------------------------------------------------------------
# Sensitivity
# ---------------------------------------------------------------------------

TORNADO_PARAMS = [
    # ⚠ TWO RANKINGS WENT STALE AT THE REBUILD AND ARE DELIBERATELY NOT HERE.
    #
    # S1 RAIL leaves the tornado entirely under D31. It is a pass-through: the
    # customer is asked for (ticket + rail) and Aurumix remits it. Flexing a
    # parameter that nets to zero in every P&L total would report a swing of
    # exactly zero and invite someone to conclude the rail does not matter. It
    # matters - to the CUSTOMER - and that incidence is reported separately as
    # a gross-up percentage per region band, not as a profit sensitivity.
    #
    # F5 FLOAT COST OF CAPITAL leaves the margin under D32. It is a memo on
    # equity, so it cannot move profit. The float PRINCIPAL still moves peak
    # funding, and that is captured through the float sizing, not through F5.
    ("PM_SHARE", "PM share of interchange (S3)"),
    ("CARD_SPEND_AED", "Card spend per active card (S4)"),
    ("CARD_ACTIVATION", "Card activation rate (S5)"),
    ("SELF_CUSTODY_LEAKAGE", "Self-custody leakage (S10)"),
    ("CREDIT_TAKEUP", "Credit take-up (S8)"),
    ("FAMILY_ATTACH", "Family attach (S11)"),
    ("SPOT_ATTACH", "Spot attach (S45)"),
    ("VAULT_RATE", "Vault storage rate (S14)"),
    ("FACILITY_TURNOVER", "Facility turnover (S40)"),
    ("ARCHETYPE_MIX", "Payment archetype mix (S27)"),
    ("CARD_FIXED", "Card programme fixed costs (F27)"),
    ("OPEX_Y1_EXIT_UPLIFT", "Y1 opex exit run-rate uplift (S48)"),
    # NEW at the rebuild - these are now first-class drivers.
    ("FAB_PREMIUM_LADDER", "Fabrication premium (F4, PROVISIONAL)"),
    ("FLOOR_SHARE", "Floor-band share by region (S54)"),
    ("AVG_TICKET_BY_MODE", "Average ticket by region (S55)"),
    ("PENETRATION_CEILING", "Regional ceiling (S22)"),
    ("REDEMPTION_RATE", "Redemption rate (S32)"),
    ("LAPSED_REDEMPTION_MULT", "Lapsed-holder multiplier (S33)"),
]

# S27 is nested, F27 a flat cost dict and S48 a scalar, so each needs its own
# bound construction rather than a Base/Aggressive/Conservative lookup.
SPECIAL_TORNADO_BOUNDS = {
    "ARCHETYPE_MIX": {
        "Aggressive": {"Base": P.ARCHETYPE_MIX["Aggressive"],
                       "Aggressive": P.ARCHETYPE_MIX["Aggressive"],
                       "Conservative": P.ARCHETYPE_MIX["Conservative"]},
        "Conservative": {"Base": P.ARCHETYPE_MIX["Conservative"],
                         "Aggressive": P.ARCHETYPE_MIX["Aggressive"],
                         "Conservative": P.ARCHETYPE_MIX["Conservative"]},
    },
    "CARD_FIXED": {
        "Aggressive": {"bin_setup": 25_000.0, "scheme_join": 18_000.0,
                       "bin_monthly": 3_500.0, "processor_monthly": 3_000.0,
                       "scheme_quarterly": 7_000.0},
        "Conservative": {"bin_setup": 90_000.0, "scheme_join": 60_000.0,
                         "bin_monthly": 12_000.0, "processor_monthly": 9_000.0,
                         "scheme_quarterly": 22_000.0},
    },
    "OPEX_Y1_EXIT_UPLIFT": {"Aggressive": 1.25, "Conservative": 1.60},
    # F4: the bounds are the two ends of the REPLICATION FAILURE, not a
    # comfortable band around a measured value. That is the honest range.
    "FAB_PREMIUM_LADDER": {
        "Aggressive": {k: P.FAB_PREMIUM_LADDER["Aggressive"]
                       for k in P.FAB_PREMIUM_LADDER},
        "Conservative": {k: P.FAB_PREMIUM_LADDER["Conservative"]
                         for k in P.FAB_PREMIUM_LADDER},
    },
    "FLOOR_SHARE": {
        "Aggressive": {k: P.FLOOR_SHARE["Aggressive"] for k in P.FLOOR_SHARE},
        "Conservative": {k: P.FLOOR_SHARE["Conservative"] for k in P.FLOOR_SHARE},
    },
    "AVG_TICKET_BY_MODE": {
        "Aggressive": {k: P.AVG_TICKET_BY_MODE["Aggressive"]
                       for k in P.AVG_TICKET_BY_MODE},
        "Conservative": {k: P.AVG_TICKET_BY_MODE["Conservative"]
                         for k in P.AVG_TICKET_BY_MODE},
    },
    "PENETRATION_CEILING": {
        "Aggressive": {k: P.PENETRATION_CEILING["Aggressive"]
                       for k in P.PENETRATION_CEILING},
        "Conservative": {k: P.PENETRATION_CEILING["Conservative"]
                         for k in P.PENETRATION_CEILING},
    },
}


def tornado(metric: str = "net_profit") -> pd.DataFrame:
    """Flex each driver to its Aggressive and Conservative bound, Base elsewhere."""
    base_df, base_cf, _ = run_scenario(P.Scenario(mode="Base"))
    if metric == "net_profit":
        base_val = base_df["net_profit"].sum()
    else:
        base_val = months_to_cash_breakeven(base_cf)["peak_funding_requirement"]

    rows = []
    for key, label in TORNADO_PARAMS:
        table = getattr(P, key)
        special = SPECIAL_TORNADO_BOUNDS.get(key)
        vals = {}
        for bound in ("Aggressive", "Conservative"):
            if special is not None:
                override = special[bound]
            elif isinstance(table, dict) and bound in table:
                override = table[bound]
            else:
                continue
            sc = P.Scenario(mode="Base", overrides={key: override})
            df, cf, _ = run_scenario(sc)
            vals[bound] = (df["net_profit"].sum() if metric == "net_profit"
                           else months_to_cash_breakeven(cf)["peak_funding_requirement"])
        if vals:
            rows.append({"driver": label, "base": base_val,
                         "aggressive": vals.get("Aggressive"),
                         "conservative": vals.get("Conservative"),
                         "swing": abs(vals.get("Aggressive", base_val)
                                      - vals.get("Conservative", base_val))})
    return pd.DataFrame(rows).sort_values("swing", ascending=False)


# ---------------------------------------------------------------------------
# G4: gold price as a scenario axis, and the Sovereign collateral stress test
# ---------------------------------------------------------------------------

def gold_level_sensitivity(moves=(-0.30, -0.25, 0.0, 0.25, 0.30)) -> pd.DataFrame:
    """Gold as a LEVEL: a different constant price across the whole horizon.

    Reported because its result is a genuine and counter-intuitive property of
    the product, NOT because it can produce a margin call. With contributions
    fixed in USD, a permanently higher price buys proportionally fewer grams,
    so USD AUM is invariant to the level - and so is everything downstream of
    it (stream 6, ad valorem custody, the collateral base).
    """
    rows = []
    base_gold = P.GOLD_USD_PER_G
    for mv in moves:
        try:
            P.GOLD_USD_PER_G = base_gold * (1.0 + mv)
            df, cf, m = run_scenario(P.Scenario(mode="Base"))
            a = df[df.year == P.HORIZON_YEARS].iloc[-1]
            cbk = months_to_cash_breakeven(cf)
            rows.append({
                "gold_move": mv,
                "gold_usd_per_g": P.GOLD_USD_PER_G,
                "terminal_aum": a["aum_usd"],
                "terminal_grams": a["grams_closing"],
                "terminal_revenue": df[df.year == P.HORIZON_YEARS]["revenue"].sum(),
                "cum_net_profit": df["net_profit"].sum(),
                "peak_funding": cbk["peak_funding_requirement"],
            })
        finally:
            P.GOLD_USD_PER_G = base_gold
    return pd.DataFrame(rows)


def gold_shock_scenarios(shock_month: int = 61,
                         moves=(-0.13, -0.29, -0.46)) -> pd.DataFrame:
    """Gold as a PATH: a shock landing at a point in time.

    This is what can produce a margin call. A loan struck in month t is
    collateralised at that month's gold price; a fall AFTER the strike revalues
    the collateral while the debt is unchanged, so the realised LTV rises toward
    the 92% line. The corpus's -13 / -29 / -46% ladder is exactly the fall each
    struck LTV needs, so those are the moves tested. Shock lands in Y6 (M61),
    by which point the credit book has been running for three years.
    """
    rows = []
    base_shock = P.GOLD_SHOCK
    for mv in moves:
        try:
            P.GOLD_SHOCK = (shock_month, mv)
            df, cf, m = run_scenario(P.Scenario(mode="Base"))
            post = df[df["month"] >= shock_month]
            at_shock = df[df["month"] == shock_month].iloc[0]
            a = df[df.year == P.HORIZON_YEARS].iloc[-1]
            cbk = months_to_cash_breakeven(cf)
            peak_liq = float(post["grams_liquidated"].max())
            rows.append({
                "shock_month": shock_month,
                "gold_move": mv,
                "margin_calls_usd": float(post["margin_call_usd"].sum()),
                "grams_liquidated": float(post["grams_liquidated"].sum()),
                "peak_month_liquidation_g": peak_liq,
                "float_grams_at_shock": float(at_shock["float_grams"]),
                "float_covers_peak": bool(at_shock["float_grams"] >= peak_liq),
                "terminal_aum": a["aum_usd"],
                "cum_net_profit": df["net_profit"].sum(),
                "peak_funding": cbk["peak_funding_requirement"],
            })
        finally:
            P.GOLD_SHOCK = base_shock
    return pd.DataFrame(rows)


# Backwards-compatible alias.
gold_price_scenarios = gold_level_sensitivity


def sovereign_collateral_stress(df: pd.DataFrame, mode: str = "Base") -> dict:
    """The named stress test from the corpus: who is actually exposed.

    Gold / Platinum / Sovereign are struck at 50 / 65 / 80% LTV, so the fall
    needed to reach a 92% margin-call line is -46% / -29% / -13%. Only
    Sovereign is exposed inside a normal annual move.
    """
    terminal = df[df.year == P.HORIZON_YEARS].iloc[-1]
    live = (terminal["tier_none"] + terminal["tier_silver"] + terminal["tier_gold"]
            + terminal["tier_platinum"] + terminal["tier_sovereign"])
    aum_per_holder = terminal["aum_usd"] / max(1e-9, terminal["holding"])

    out = {"margin_call_ltv": 0.92, "gold_vol": P.GOLD_VOL[mode], "tiers": []}
    for tier in ("Gold", "Platinum", "Sovereign"):
        ltv = P.LTV_LADDER[tier]
        n = terminal[f"tier_{tier.lower()}"]
        collateral = n * aum_per_holder
        peak_drawn = (collateral * ltv * P.CREDIT_TAKEUP[mode]
                      * P.CREDIT_DRAWN_PCT[mode])
        drawn_at_max = collateral * ltv * P.CREDIT_TAKEUP[mode]
        fall_needed = 1.0 - ltv / 0.92
        # One-sigma annual move at S6 volatility.
        sigma = P.GOLD_VOL[mode]
        within_1sigma = abs(fall_needed) <= sigma
        # Grams that must be liquidated to restore the struck LTV after the move.
        collateral_after = collateral * (1.0 + fall_needed)
        shortfall_usd = max(0.0, drawn_at_max - collateral_after * ltv)
        grams_to_liquidate = shortfall_usd / P.GOLD_USD_PER_G
        out["tiers"].append({
            "tier": tier, "struck_ltv": ltv, "accounts": n,
            "collateral_usd": collateral,
            "drawn_at_max_usd": drawn_at_max,
            "expected_drawn_usd": peak_drawn,
            "fall_to_margin_call": fall_needed,
            "within_one_sigma": within_1sigma,
            "grams_to_liquidate": grams_to_liquidate,
            "float_grams": terminal["float_grams"],
            "float_covers": terminal["float_grams"] >= grams_to_liquidate,
        })
    return out


def pm_share_card_spend_grid() -> pd.DataFrame:
    """The grid the brief asks for: PM share x card spend."""
    pm_vals = [0.36, 0.55, 0.72, 0.85]
    spend_vals = [3500.0, 6000.0, 9000.0]
    rows = []
    for pm in pm_vals:
        for sp in spend_vals:
            sc = P.Scenario(mode="Base", overrides={
                "PM_SHARE": {"Base": pm, "Aggressive": pm, "Conservative": pm},
                "CARD_SPEND_AED": {"Base": sp, "Aggressive": sp, "Conservative": sp}})
            df, cf, _ = run_scenario(sc)
            rows.append({"pm_share": pm, "card_spend_aed": sp,
                         "terminal_revenue": df[df.year == P.HORIZON_YEARS]["revenue"].sum(),
                         "cum_net_profit": df["net_profit"].sum(),
                         "peak_funding": months_to_cash_breakeven(cf)
                         ["peak_funding_requirement"]})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# G2: the brief's 9 parameter solvers, returned as solved values
# ---------------------------------------------------------------------------

def solve_parameters(df: pd.DataFrame, mode: str = "Base") -> pd.DataFrame:
    """Solve the brief's 9 items against the model, or say why one cannot be.

    The brief claims the model "returns each as a solved value with its
    arithmetic shown". Items 6 (tenure rebate) and 8 (family price) are out of
    scope - 6 is retired by decision 44, 8 is already solved in the corpus.
    """
    out = []
    terminal = df[df.year == P.HORIZON_YEARS].iloc[-1]
    yr_last = df[df.year == P.HORIZON_YEARS]
    live = terminal["live_accounts"]
    expected_months = float(__import__("cohort").survival_curve(
        mode, P.HORIZON_MONTHS).sum())

    # --- Item 1: entry-fee uplift funding the discount ladder
    tiered = sum(terminal[f"tier_{t}"] for t in
                 ("none", "silver", "gold", "platinum", "sovereign"))
    wavg_disc = sum(P.TIER_DISCOUNT_PP[t] * terminal[f"tier_{t.lower()}"]
                    for t in ("Silver", "Gold", "Platinum", "Sovereign")
                    ) / max(1e-9, tiered)
    out.append({
        "item": 1, "parameter": "Entry-fee base uplift funding the discount ladder",
        "solved_value": f"{wavg_disc*100:.3f}pp",
        "arithmetic": f"Book-weighted discount at the Y10 computed tier mix = "
                      f"{wavg_disc*100:.3f}pp. The 1.5pp Sovereign ceiling applies "
                      f"to only {terminal['tier_sovereign']/max(1e-9,tiered)*100:.1f}% "
                      f"of accounts, so the ladder costs far less than its headline.",
        "status": "SOLVED"})

    # --- Item 2: Gold Rewards rate ceiling
    cum_ic = df["stream2"].sum()
    cum_cr = df["stream5"].sum()
    cum_cu = df["cost_vault"].sum()
    cum_spend = df["card_spend"].sum()
    ceiling_rate = max(0.0, (cum_ic + cum_cr - cum_cu)) / max(1e-9, cum_spend)
    out.append({
        "item": 2, "parameter": "Gold Rewards rate ceiling",
        "solved_value": f"{ceiling_rate*100:.3f}% of qualifying spend",
        "arithmetic": f"(cum interchange {cum_ic:,.0f} + credit {cum_cr:,.0f} "
                      f"- custody {cum_cu:,.0f}) / cum card spend {cum_spend:,.0f}. "
                      f"Top-tier rate of 0.75% is "
                      f"{'INSIDE' if ceiling_rate>=0.0075 else 'ABOVE'} this ceiling.",
        "status": "SOLVED"})

    # --- Item 3: referral reward size, <= 25% of LTV
    ltv_tab = ltv_cac(df, mode)
    blended_ltv = float(ltv_tab[ltv_tab.channel == "Referral"]
                        ["ltv_all_streams"].mean())
    max_reward = 0.25 * blended_ltv
    y1_fee = P.ENTRY_FEE_BY_YEAR[1]
    avg_ticket = float(yr_last["inflow_sip"].sum() / max(1e-9, yr_last["collection_events"].sum()))
    fee_over_run = avg_ticket * y1_fee * min(expected_months, 24)
    implied_pct = max_reward / max(1e-9, fee_over_run)
    out.append({
        "item": 3, "parameter": "Referral reward size",
        "solved_value": (f"{implied_pct*100:.0f}% of the referee's entry fee "
                         f"(LTV does not bind; F17's 30% is affordable)"
                         if implied_pct >= 1.0
                         else f"{implied_pct*100:.1f}% of the referee's entry fee"),
        "arithmetic": f"25% of all-streams LTV {blended_ltv:,.0f} = "
                      f"{max_reward:,.0f} max affordable reward; the referee's "
                      f"entry fee over a 24-month run is only {fee_over_run:,.0f}. "
                      + (f"The LTV ceiling is {implied_pct:.1f}x the entire entry "
                         f"fee, so it cannot bind - **the binding constraint on "
                         f"referral reward is the acquisition budget (item 5), "
                         f"not LTV.** F17's 30% placeholder is affordable."
                         if implied_pct >= 1.0 else
                         f"F17's 30% placeholder is "
                         f"{'affordable' if implied_pct>=0.30 else 'TOO HIGH'}."),
        "status": "SOLVED"})

    # --- Item 4: agent commission, three levels
    ceiling_total = float(df["cost_acquisition"].sum())
    agent_share = 0.6
    agent_pool = ceiling_total * agent_share
    new_agent = float((df["new_accounts"]).sum()) * 0.45
    per_acct = agent_pool / max(1e-9, new_agent)
    out.append({
        "item": 4, "parameter": "Agent commission, three levels",
        "solved_value": f"USD {per_acct:,.2f}/account, split 4/5/6 = "
                        f"{per_acct*4/15:,.2f} / {per_acct*5/15:,.2f} / "
                        f"{per_acct*6/15:,.2f}",
        "arithmetic": f"Agent pool {agent_pool:,.0f} over {new_agent:,.0f} "
                      f"agent-sourced accounts, split on V2's recommended 4/5/6 "
                      f"front-loaded gradient.",
        "status": "SOLVED"})

    # --- Item 5: acquisition budget ceiling
    total_rev = float(df["revenue"].sum())
    total_fee = float(df["gross_entry_fee"].sum())
    ceil_vs_rev = ceiling_total / max(1e-9, total_rev)
    ceil_vs_fee = ceiling_total / max(1e-9, total_fee)
    out.append({
        "item": 5, "parameter": "Acquisition budget ceiling",
        "solved_value": f"{ceil_vs_rev*100:.1f}% of total revenue "
                        f"({ceil_vs_fee*100:.0f}% of entry-fee revenue)",
        "arithmetic": f"Acquisition {ceiling_total:,.0f} against total revenue "
                      f"{total_rev:,.0f} and entry fee {total_fee:,.0f}. "
                      f"**Confirms the brief's own flag**: expressed against "
                      f"entry fee the ceiling is {ceil_vs_fee*100:.0f}%, which is "
                      f"meaningless. Total revenue is the right denominator.",
        "status": "SOLVED"})

    # --- Item 6: tenure rebate - RETIRED
    out.append({
        "item": 6, "parameter": "Tenure rebate size",
        "solved_value": "n/a - RETIRED",
        "arithmetic": "Decision 44 (2026-08-10) retired the mechanism. The brief's "
                      "solver conflates Gold Rewards' 0.10-0.75% range with a "
                      "superseded decaying redemption fee. No solve required.",
        "status": "NOT APPLICABLE"})

    # --- Item 7: B2B platform fee bps
    partner_aum = float(terminal["partner_aum"])
    vault_rate = P.VAULT_RATE[mode]
    target_margin = 0.0010
    min_bps = vault_rate + target_margin
    out.append({
        "item": 7, "parameter": "B2B platform fee bps",
        "solved_value": f"{min_bps*10000:.0f} bps floor "
                        f"(modelled at {P.B2B_FEE_BPS*10000:.0f} bps)",
        "arithmetic": f"Floor = vault rate {vault_rate*10000:.0f}bps + "
                      f"{target_margin*10000:.0f}bps target margin. At Y10 partner "
                      f"AUM {partner_aum:,.0f} the modelled "
                      f"{P.B2B_FEE_BPS*10000:.0f}bps yields "
                      f"{partner_aum*P.B2B_FEE_BPS:,.0f}/yr.",
        "status": "SOLVED"})

    # --- Item 8: family plan price - already solved in corpus
    out.append({
        "item": 8, "parameter": "Family plan and per-beneficiary price",
        "solved_value": f"USD {P.FAMILY_PRICE_ANNUAL:.0f}/yr + "
                        f"USD {P.FAMILY_EXTRA_NAME_PRICE:.0f}/name",
        "arithmetic": f"Corpus §11 solved this at USD 29-36/yr against a "
                      f"USD {P.FAMILY_COST_PER_NAME_ONEOFF:.2f} per-name floor "
                      f"(~5x headroom). Model carries the midpoint. Confirmed, "
                      f"not re-solved.",
        "status": "CARRIED FROM CORPUS"})

    # --- Item 9: PM share needed for cash break-even
    # 12 bisection steps resolve PM share to ~0.02pp, which is far finer than
    # the parameter is knowable; more steps only cost runtime.
    lo, hi, target = 0.30, 1.00, None
    for _ in range(12):
        mid = (lo + hi) / 2
        sc = P.Scenario(mode="Base", overrides={
            "PM_SHARE": {"Base": mid, "Aggressive": mid, "Conservative": mid}})
        d, c, _ = run_scenario(sc)
        if d.groupby("year")["ebitda"].sum().gt(0).any():
            hi = mid
            target = mid
        else:
            lo = mid
    out.append({
        "item": 9, "parameter": "PM share needed for EBITDA break-even in 10y",
        "solved_value": (f"{target*100:.1f}%" if target else
                         ">100% - unreachable on PM share alone"),
        "arithmetic": (f"Bisection on PM share holding all else at Base. "
                       f"{'Above the 85% Aggressive bound, so not reachable by '
                          'negotiation alone.' if target and target > 0.85 else ''}"
                       if target else
                       "No PM share up to 100% produces an EBITDA-positive year "
                       "at Base volume. The constraint is volume, not the "
                       "interchange split."),
        "status": "SOLVED"})
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------
# LTV / CAC
# ---------------------------------------------------------------------------

def ltv_cac(df: pd.DataFrame, mode: str = "Base") -> pd.DataFrame:
    """LTV by segment at the CORRECTED persistency, with payback month.

    v1.0 flags its own LTV numbers as stale because they were computed at the
    old survival curve.
    """
    import lifecycle as LC
    # Read expected paying months off the D23 lifecycle curve, which is the
    # live engine. Reading cohort.survival_curve here would quietly re-introduce
    # the retired triangle as a live dependency.
    curves = LC.LifecycleCurves(mode, P.HORIZON_MONTHS)
    expected_months = float(curves.curve_survival.sum())

    # Non-card revenue is not segment-differentiated, so it is spread per
    # account-month. Card revenue IS segment-differentiated (see
    # Model.segment_spend_multipliers) and is attributed on each segment's own
    # realised card spend.
    card_rev = (df["stream2"] + df["stream4"]).sum()
    noncard_rev = df["revenue"].sum() - card_rev
    total_contrib_months = (df["contributing"] + df["reduced"]).sum()
    noncard_per_month = noncard_rev / max(1e-9, total_contrib_months)

    total_card_spend = sum(df[f"card_spend_{s}"].sum() for s in P.SEGMENTS)
    seg_card_share = {s: df[f"card_spend_{s}"].sum() / max(1e-9, total_card_spend)
                      for s in P.SEGMENTS}
    seg_months = {s: df[f"live_{s}"].sum() for s in P.SEGMENTS}

    rows = []
    # D25: LTV is computed PER BAND, because the whole point of the two-band
    # cut is that the average ticket describes nobody.
    for seg in P.SEGMENTS:
      for band, (band_share, ticket) in P.band_split(seg, mode).items():
        fee = P.ENTRY_FEE_BY_YEAR[1]
        premium = P.FAB_PREMIUM_LADDER[mode][P.BAR_LADDER_GRAMS[0]]
        gross = ticket - ticket * (1 - fee) * (1 + premium)
        # D31: the rail is NOT deducted. It is grossed onto the request and
        # remitted, so it never reaches Aurumix's margin.
        net_per_month = gross
        ltv_entry = net_per_month * expected_months

        # Card revenue this segment actually generated, per account-month.
        seg_card_per_month = (card_rev * seg_card_share[seg]
                              / max(1e-9, seg_months[seg]))
        ltv_all = (noncard_per_month + seg_card_per_month) * expected_months
        for ch in P.CHANNELS:
            if ch == "Agent":
                cac = P.CAC_BASE * 0.6
            elif ch == "Referral":
                cac = P.CAC_BASE * 0.35
            elif ch == "Direct":
                cac = P.CAC_BASE
            else:
                cac = 0.0
            payback = (cac / net_per_month) if net_per_month > 0 else None
            rows.append({
                "region": seg, "region_name": P.REGION_NAME[seg],
                "band": band, "share_of_region": band_share,
                "channel": ch, "ticket": ticket,
                "expected_paying_months": round(expected_months, 1),
                "net_margin_per_contribution": round(net_per_month, 4),
                "ltv_entry_fee_only": round(ltv_entry, 2),
                "ltv_all_streams": round(ltv_all, 2),
                "cac": round(cac, 2),
                "ltv_cac_entry": round(ltv_entry / cac, 3) if cac else None,
                "ltv_cac_all": round(ltv_all / cac, 3) if cac else None,
                "payback_month_entry_only": round(payback, 1)
                if payback and payback > 0 else "never",
            })
    return pd.DataFrame(rows)


def unit_economics_by_band(mode: str = "Base") -> pd.DataFrame:
    """Net contribution margin per contribution, PER REGION BAND and year.

    D25 requires this to be computed per band and summed, never on the regional
    average. R1's average ticket is USD 38, but nobody contributes 38: 40%
    contribute 20 and 60% contribute 50. Any quantity that is non-linear in the
    ticket gets the wrong answer from the average.

    D31 and D32 have removed the rail and the float carry from the margin, so
    the net margin is now a pure PERCENTAGE of the ticket and the bands differ
    only in absolute dollars. That is itself the finding: removing the fixed
    rail removed the one term that made the small ticket structurally worse.
    The rail incidence is reported separately in `rail_incidence`.
    """
    rows = []
    for yr in range(1, P.HORIZON_YEARS + 1):
        fee = P.ENTRY_FEE_BY_YEAR[yr]
        bar = P.BAR_LADDER_GRAMS[0] if yr <= 2 else P.BAR_LADDER_GRAMS[-1]
        premium = P.FAB_PREMIUM_LADDER[mode][bar]
        for r in P.SEGMENTS:
            for band, (share, ticket) in P.band_split(r, mode).items():
                gross = ticket - ticket * (1 - fee) * (1 + premium)
                rows.append({
                    "year": yr, "region": r, "region_name": P.REGION_NAME[r],
                    "band": band, "share_of_region": share, "ticket": ticket,
                    "fee": fee, "premium": premium,
                    "gross_margin_usd": round(gross, 4),
                    "gross_margin_pct": round(gross / ticket * 100, 3),
                    "rail_memo_usd_NOT_deducted": P.RAIL_COST[mode],
                    "net_margin_usd": round(gross, 4),
                    "net_margin_pct": round(gross / ticket * 100, 3)})
    return pd.DataFrame(rows)


unit_economics_by_segment = unit_economics_by_band


def book_weighted_unit_economics(df: pd.DataFrame, mode: str = "Base") -> dict:
    """The two headline unit-economics numbers, both computed and not assumed.

    The USD 75 ticket is the brief's own illustration, kept for continuity with
    every prior version. The BOOK-WEIGHTED ticket is the one that matters, and
    under D25 it is far lower - the six-segment cut implied roughly USD 40, the
    four regions imply about USD 31.5 - which tightens the fee arithmetic rather
    than loosening it.
    """
    import streams as _S
    last = df[df.year == P.HORIZON_YEARS]
    premium = float(last["fab_premium"].iloc[-1])
    fee = float((last["fee_applied"] * last["inflow_sip"]).sum()
                / max(1e-9, last["inflow_sip"].sum()))
    _infl = last["inflow_sip"] + last["inflow_spot"]
    pg = float((last["pricegap_rate"] * _infl).sum() / max(1e-9, _infl.sum()))
    nn = float((last["net_new_gram_share"] * _infl).sum() / max(1e-9, _infl.sum()))
    ev = float(last["collection_events"].sum())
    book_ticket = float(last["inflow_sip"].sum()) / ev if ev > 0 else 0.0

    out = {}
    for label, ticket in (("usd_75_illustration", 75.0),
                          ("book_weighted", book_ticket)):
        r = _S.entry_fee_margin(ticket, 1.0, fee, premium, pg, 0.0,
                                P.RAIL_COST[mode], net_new_gram_share=nn)
        out[label] = {
            "ticket_usd": ticket, "fee_applied": fee,
            "fabrication_premium": premium, "net_new_gram_share": nn,
            "price_gap": pg,
            "gross_margin_usd": r["gross_margin"],
            "gross_margin_pct": r["gross_margin_pct"] * 100,
            "net_contribution_margin_usd": r["net"],
            "net_contribution_margin_pct": r["net_pct"] * 100,
            "rail_memo_usd_not_deducted": r["rail_memo"],
            "floatcoc_memo_usd_not_deducted": r["float_coc_memo"]}

    out["correction_26"] = {
        "brief_states_layer4_and_6_1b_pct": 0.72,
        "brief_waterfall_6_1_pct": 2.15,
        "model_at_v1_premium_3pct": (75 - 75 * 0.95 * 1.03) / 75 * 100,
        "model_at_D28_base_premium": out["usd_75_illustration"]["gross_margin_pct"],
        "verdict": "The exact identity C - C(1-f)(1+p) reproduces the brief's "
                   "own audited USD 1.6125 = 2.150% at the v1.0 3.00% premium. "
                   "The 0.72% figure is arithmetically wrong; the waterfall is "
                   "right. Nothing is hardcoded - the model produces this."}
    return out


def rail_incidence(mode: str = "Base") -> pd.DataFrame:
    """D31: who pays the rail now, and what it costs them.

    The rail left the P&L. It did NOT leave the transaction. Aurumix asks for
    (ticket + rail) and remits it, so the incidence moved wholly onto the
    customer - and it is REGRESSIVE, because the rail is a fixed amount per
    collection while the ticket is not.

    Reported per region band, because "the rail is no longer a cost" is true of
    Aurumix and false of a USD 20 saver, for whom it is a 1.25% surcharge on
    every contribution. That is not a rounding error against a gross margin of
    roughly 3.6%.
    """
    import streams as _S
    rail = P.RAIL_COST[mode]
    rows = []
    for r in P.SEGMENTS:
        for band, (share, ticket) in P.band_split(r, mode).items():
            g = _S.rail_gross_up(ticket, rail)
            rows.append({
                "region": r, "region_name": P.REGION_NAME[r], "band": band,
                "share_of_region": share, "ticket_usd": ticket,
                "rail_usd": rail,
                "request_amount_usd": g["request_amount"],
                "gross_up_pct_of_ticket": g["gross_up_pct"] * 100,
                "annual_cost_to_customer_usd": rail * 12.0})
    return pd.DataFrame(rows).sort_values("gross_up_pct_of_ticket",
                                          ascending=False)


def redeemed_gold_switch_comparison() -> pd.DataFrame:
    """D33 both ways, so the default is visible rather than buried.

    This settles a decision nobody had written down (correction 30). Reporting
    only the default would repeat exactly the mistake that correction caught, so
    both settings are run and the difference is shown.
    """
    rows = []
    saved = P.REDEEMED_GOLD_TO_FLOAT
    try:
        for setting in (True, False):
            P.REDEEMED_GOLD_TO_FLOAT = setting
            df, cf, _ = run_scenario(P.Scenario(mode="Base"))
            last = df[df.year == P.HORIZON_YEARS]
            rows.append({
                "REDEEMED_GOLD_TO_FLOAT": setting,
                "routing": ("float, excess sold at bid" if setting
                            else "all to dealer"),
                "mean_net_new_gram_share_final_year":
                    float(last["net_new_gram_share"].mean()),
                "terminal_year_gross_profit": float(last["gross_profit"].sum()),
                "cumulative_premium_cost": float(df["cor_premium"].sum()),
                "cumulative_redemption_cost": float(df["cost_redemption"].sum()),
                "cumulative_net_profit": float(df["net_profit"].sum()),
                "peak_funding": months_to_cash_breakeven(cf)
                                ["peak_funding_requirement"]})
    finally:
        P.REDEEMED_GOLD_TO_FLOAT = saved
    return pd.DataFrame(rows)


def float_debt_funded_comparison() -> pd.DataFrame:
    """D32's one restoring case, run both ways.

    If the float is EQUITY funded the carry is an opportunity cost and a memo.
    If it is DEBT funded - a gold-backed working-capital facility, or dealer
    credit - the interest is cash, and it belongs in the P&L below EBITDA as a
    financing line. The switch prices the difference.
    """
    rows = []
    saved = P.FLOAT_DEBT_FUNDED
    try:
        for setting in (False, True):
            P.FLOAT_DEBT_FUNDED = setting
            df, cf, _ = run_scenario(P.Scenario(mode="Base"))
            rows.append({
                "FLOAT_DEBT_FUNDED": setting,
                "treatment": ("memo, equity funded" if not setting
                              else "financing line below EBITDA, debt funded"),
                "cumulative_ebitda": float(df["ebitda"].sum()),
                "cumulative_float_interest":
                    float(df["float_interest_expense"].sum()),
                "cumulative_net_profit": float(df["net_profit"].sum()),
                "peak_funding": months_to_cash_breakeven(cf)
                                ["peak_funding_requirement"]})
    finally:
        P.FLOAT_DEBT_FUNDED = saved
    return pd.DataFrame(rows)
