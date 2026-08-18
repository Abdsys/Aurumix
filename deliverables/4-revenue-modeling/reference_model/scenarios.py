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
        # "rail kills it": conservative rail ONLY, everything else Base.
        "rail_kills_it": P.Scenario(
            name="rail_kills_it", mode="Base",
            overrides={"RAIL_COST": {k: P.RAIL_COST["Conservative"]
                                     for k in P.RAIL_COST}}),
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

    v1.0's fee ladder falls 5% -> 4% -> 3% BECAUSE the fabrication premium was
    assumed to fall 3.00% -> 2.00% -> 0.75% as the business moved onto Good
    Delivery bars. Those two schedules are physically coupled: the premium is a
    function of bar denomination, and denomination is a function of volume.

    The model solves denomination endogenously and Good Delivery never clears,
    so the premium holds at 2.00%. A 3% fee less the tier-weighted discount is
    then BELOW COST. This solver reports the fee the arithmetic actually
    permits, year by year.

    Per contribution, with fee f, premium p, price-gap g, float c, rail R,
    ticket T and collection events E = 1 per contribution:

        net = T - T(1-f)(1+p) - T*g - c - R  >= 0

    Solving for f gives the minimum viable rate at that year's premium, mix and
    rail. Reported as a CONSTRAINT, not a recommendation.
    """
    rows = []
    for yr in range(1, 11):
        d = df[df.year == yr]
        if d.empty:
            continue

        premium = float(d["fab_premium"].iloc[-1])
        bar_g = float(d["bar_grams"].iloc[-1])
        # Weight the price-gap by inflow, not a flat mean. In the launch ramp
        # it runs 9.0% in M1 on negligible volume and decays to 0.8% by M12;
        # an unweighted mean lets the first, smallest month dominate the year.
        _infl = d["inflow_sip"] + d["inflow_spot"]
        pricegap = float((d["pricegap_rate"] * _infl).sum() / max(1e-9, _infl.sum()))
        assumed_fee = P.ENTRY_FEE_BY_YEAR[yr]
        applied = float((d["fee_applied"] * d["inflow_sip"]).sum()
                        / max(1e-9, d["inflow_sip"].sum()))
        discount = assumed_fee - applied

        # Solve each lane on ITS OWN ticket. A blended ticket mixes a ~USD 49
        # SIP contribution with a ~USD 690 spot order and represents neither;
        # the fixed rail is the whole point and it does not blend.
        lanes = {}
        for lane, infl_col, ev_col, rail_rate in (
                ("sip", "inflow_sip", "collection_events", P.RAIL_COST[mode]),
                ("spot", "inflow_spot", "spot_events", P.SPOT_RAIL_COST)):
            infl = float(d[infl_col].sum())
            ev = float(d[ev_col].sum())
            if infl <= 0 or ev <= 0:
                lanes[lane] = None
                continue
            ticket = infl / ev
            # Float cost is carried by the SIP lane only (spot is a single push).
            per_float = (float(d["cor_float"].sum()) / ev) if lane == "sip" else 0.0
            per_pg = ticket * pricegap
            residual = ticket - per_pg - per_float - rail_rate
            min_net = 1.0 - residual / (ticket * (1.0 + premium))
            lanes[lane] = {"ticket": ticket, "min_net": min_net,
                           "min_headline": min_net + discount}

        sip, spot = lanes.get("sip"), lanes.get("spot")
        # The binding constraint is the lane that needs the higher fee - the
        # SIP lane, always, because the fixed rail is spread over a far smaller
        # ticket. That is exactly the 0.2 non-linearity.
        binding = max((l for l in (sip, spot) if l), key=lambda l: l["min_headline"])
        min_headline = binding["min_headline"]

        rows.append({
            "year": yr,
            "bar_grams": bar_g,
            "premium": premium,
            "sip_ticket": sip["ticket"] if sip else None,
            "spot_ticket": spot["ticket"] if spot else None,
            "v1.0 assumed fee": assumed_fee,
            "tier discount applied": discount,
            "min viable fee SIP lane": sip["min_headline"] if sip else None,
            "min viable fee spot lane": spot["min_headline"] if spot else None,
            "min viable fee (binding)": min_headline,
            "shortfall_pp": (min_headline - assumed_fee) * 100,
            "achievable": min_headline <= assumed_fee,
            "stream1_sip_net": float(d["stream1_sip"].sum()),
            "stream1_net_total": float(d["stream1_net"].sum()),
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Sensitivity
# ---------------------------------------------------------------------------

TORNADO_PARAMS = [
    ("RAIL_COST", "Rail cost per collection (S1)"),
    ("PM_SHARE", "PM share of interchange (S3)"),
    ("CARD_SPEND_AED", "Card spend per active card (S4)"),
    ("CARD_ACTIVATION", "Card activation rate (S5)"),
    ("SELF_CUSTODY_LEAKAGE", "Self-custody leakage (S10)"),
    ("CREDIT_TAKEUP", "Credit take-up (S8)"),
    ("FAMILY_ATTACH", "Family attach (S11)"),
    ("SPOT_ATTACH", "Spot attach (S45)"),
    ("VAULT_RATE", "Vault storage rate (S14)"),
    ("FACILITY_TURNOVER", "Facility turnover (S40)"),
    # G3: the three the brief ranks as load-bearing that were never flexed.
    ("ARCHETYPE_MIX", "Payment archetype mix (S27)"),
    ("CARD_FIXED", "Card programme fixed costs (F27)"),
    ("OPEX_Y1_EXIT_UPLIFT", "Y1 opex exit run-rate uplift (S48)"),
]

# S27 is a nested structure, F27 a flat dict of costs and S48 a scalar, so each
# needs its own bound construction rather than a Base/Aggressive/Conservative
# lookup. Bounds are the parameter file's own stated alternatives.
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
            a = df[df.year == 10].iloc[-1]
            cbk = months_to_cash_breakeven(cf)
            rows.append({
                "gold_move": mv,
                "gold_usd_per_g": P.GOLD_USD_PER_G,
                "y10_aum": a["aum_usd"],
                "y10_grams": a["grams_closing"],
                "y10_revenue": df[df.year == 10]["revenue"].sum(),
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
            a = df[df.year == 10].iloc[-1]
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
                "y10_aum": a["aum_usd"],
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
    y10 = df[df.year == 10].iloc[-1]
    live = (y10["tier_none"] + y10["tier_silver"] + y10["tier_gold"]
            + y10["tier_platinum"] + y10["tier_sovereign"])
    aum_per_holder = y10["aum_usd"] / max(1e-9, y10["holding"])

    out = {"margin_call_ltv": 0.92, "gold_vol": P.GOLD_VOL[mode], "tiers": []}
    for tier in ("Gold", "Platinum", "Sovereign"):
        ltv = P.LTV_LADDER[tier]
        n = y10[f"tier_{tier.lower()}"]
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
            "float_grams": y10["float_grams"],
            "float_covers": y10["float_grams"] >= grams_to_liquidate,
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
                         "y10_revenue": df[df.year == 10]["revenue"].sum(),
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
    y10 = df[df.year == 10].iloc[-1]
    yr10 = df[df.year == 10]
    live = y10["live_accounts"]
    expected_months = float(__import__("cohort").survival_curve(
        mode, P.HORIZON_MONTHS).sum())

    # --- Item 1: entry-fee uplift funding the discount ladder
    tiered = sum(y10[f"tier_{t}"] for t in
                 ("none", "silver", "gold", "platinum", "sovereign"))
    wavg_disc = sum(P.TIER_DISCOUNT_PP[t] * y10[f"tier_{t.lower()}"]
                    for t in ("Silver", "Gold", "Platinum", "Sovereign")
                    ) / max(1e-9, tiered)
    out.append({
        "item": 1, "parameter": "Entry-fee base uplift funding the discount ladder",
        "solved_value": f"{wavg_disc*100:.3f}pp",
        "arithmetic": f"Book-weighted discount at the Y10 computed tier mix = "
                      f"{wavg_disc*100:.3f}pp. The 1.5pp Sovereign ceiling applies "
                      f"to only {y10['tier_sovereign']/max(1e-9,tiered)*100:.1f}% "
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
    avg_ticket = float(yr10["inflow_sip"].sum() / max(1e-9, yr10["collection_events"].sum()))
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
    partner_aum = float(y10["partner_aum"])
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
    from cohort import survival_curve
    surv = survival_curve(mode, P.HORIZON_MONTHS)
    expected_months = float(surv.sum())

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
    for seg in P.SEGMENTS:
        ticket = P.TICKET[seg]
        fee = P.ENTRY_FEE_BY_YEAR[1]
        premium = P.FAB_PREMIUM_BY_YEAR[1]
        gross = ticket - ticket * (1 - fee) * (1 + premium)
        net_per_month = gross - P.RAIL_COST[mode]
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
                "segment": seg, "channel": ch, "ticket": ticket,
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


def unit_economics_by_segment(mode: str = "Base") -> pd.DataFrame:
    """Net margin per contribution by segment AND year.

    v1.0 applied the top segment's USD 75 ticket to the whole population. At
    USD 20 the margin is negative. This shows the real per-segment picture.
    """
    rows = []
    for yr in range(1, 11):
        fee = P.ENTRY_FEE_BY_YEAR[yr]
        premium = P.FAB_PREMIUM_BY_YEAR[yr]
        for seg in P.SEGMENTS:
            ticket = P.TICKET[seg]
            gross = ticket - ticket * (1 - fee) * (1 + premium)
            for rail_name in ("Base", "Conservative"):
                rail = P.RAIL_COST[rail_name]
                rows.append({"year": yr, "segment": seg, "ticket": ticket,
                             "rail_case": rail_name,
                             "gross_margin": round(gross, 4),
                             "rail_cost": rail,
                             "net_margin": round(gross - rail, 4),
                             "net_margin_pct": round((gross - rail) / ticket * 100, 3)})
    return pd.DataFrame(rows)
