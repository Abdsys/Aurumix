"""Entry point: runs every scenario, writes CSVs + headline JSON, prints a summary."""
from __future__ import annotations

import json
import os

import numpy as np
import pandas as pd

import cohort
import lifecycle
import costs as C
import ics
import params as P
import scenarios as SC

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)


def _j(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, pd.DataFrame):
        return o.to_dict("records")
    return str(o)


def annual_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("year").agg(
        new_accounts=("new_accounts", "sum"),
        contributing=("contributing", "last"),
        reduced=("reduced", "last"),
        lapsed_holding=("lapsed_holding", "last"),
        dormant=("dormant", "last"),
        closed=("closed", "last"),
        holding=("holding", "last"),
        live_accounts=("live_accounts", "last"),
        tier_none=("tier_none", "last"), tier_silver=("tier_silver", "last"),
        tier_gold=("tier_gold", "last"), tier_platinum=("tier_platinum", "last"),
        tier_sovereign=("tier_sovereign", "last"),
        inflow_sip=("inflow_sip", "sum"), inflow_spot=("inflow_spot", "sum"),
        aum_usd=("aum_usd", "last"), grams=("grams_closing", "last"),
        bar_grams=("bar_grams", "last"), fab_premium=("fab_premium", "last"),
        gross_entry_fee=("gross_entry_fee", "sum"),
        cost_of_revenue=("cost_of_revenue", "sum"),
        gross_profit=("gross_profit", "sum"),
        cor_pricegap=("cor_pricegap", "sum"),
        cor_premium=("cor_premium", "sum"),
        # MEMO LINES (D31, D32). Reported alongside the P&L, in no total.
        rail_passthrough_usd=("rail_passthrough_usd", "sum"),
        floatcoc_memo=("floatcoc_memo", "sum"),
        float_interest_expense=("float_interest_expense", "sum"),
        stream1_net=("stream1_net", "sum"),
        operating_cost=("operating_cost", "sum"),
        stream1_sip=("stream1_sip", "sum"), stream1_spot=("stream1_spot", "sum"),
        stream2=("stream2", "sum"), stream2_gross=("stream2_gross", "sum"),
        stream3=("stream3", "sum"), stream4=("stream4", "sum"),
        stream5=("stream5", "sum"), stream6=("stream6", "sum"),
        revenue=("revenue", "sum"),
        cost_opex=("cost_opex", "sum"), cost_acquisition=("cost_acquisition", "sum"),
        cost_vault=("cost_vault", "sum"), cost_rewards=("cost_rewards", "sum"),
        cost_card_fixed=("cost_card_fixed", "sum"),
        cost_card_variable=("cost_card_variable", "sum"),
        cost_screening=("cost_screening", "sum"),
        cost_redemption=("cost_redemption", "sum"),
        cost_oneoff=("cost_oneoff", "sum"), cost_family=("cost_family", "sum"),
        cost_vat=("cost_vat", "sum"),
        total_cost=("total_cost", "sum"),
        ebitda=("ebitda", "sum"), tax=("tax", "sum"), net_profit=("net_profit", "sum"),
        active_cards=("active_cards", "last"), card_spend=("card_spend", "sum"),
        partner_aum=("partner_aum", "last"),
    )


def main():
    print("=" * 78)
    print("AURUMIX REFERENCE REVENUE MODEL")
    print("=" * 78)

    # -- validation -------------------------------------------------------
    personas = ics.validate_personas()
    gates = ics.validate_gate_mechanics()
    n_pass = sum(1 for p in personas if p["pass"])
    n_gate = sum(1 for g in gates if g["pass"])
    print(f"\nICS personas A-I : {n_pass}/{len(personas)} pass")
    print(f"ICS gate mechanics: {n_gate}/{len(gates)} pass")

    # -- survival ---------------------------------------------------------
    print("\nSURVIVAL CALIBRATION (Base)")
    s_sourced = lifecycle.LifecycleCurves("Base", P.HORIZON_MONTHS).curve_survival
    w, bg, fit = cohort.fit_survival("Base")
    for f in fit:
        print(f"  M{f['anchor_month']:>3}: target {f['target']:.3f} | "
              f"sourced {f['sourced_weights']:.4f} ({f['sourced_residual_pp']:+.2f}pp) | "
              f"calibrated {f['calibrated']:.4f} ({f['residual_pp']:+.2f}pp)")
    rmse_src = float(np.sqrt(np.mean([f["sourced_residual_pp"] ** 2 for f in fit])))
    rmse_cal = float(np.sqrt(np.mean([f["residual_pp"] ** 2 for f in fit])))
    print(f"  RMSE sourced {rmse_src:.3f}pp vs calibrated {rmse_cal:.3f}pp")
    print(f"  M{P.HORIZON_MONTHS} survival (sourced): {s_sourced[P.HORIZON_MONTHS]:.4f}")

    surv_rows = [{"month": m, "sourced": float(s_sourced[m])}
                 for m in range(P.HORIZON_MONTHS + 1)]
    for mode in ("Aggressive", "Conservative"):
        s = lifecycle.LifecycleCurves(mode, P.HORIZON_MONTHS).curve_survival
        for i, r in enumerate(surv_rows):
            r[mode.lower()] = float(s[i])
    pd.DataFrame(surv_rows).to_csv(f"{OUT}/survival_curves.csv", index=False)

    # -- scenarios --------------------------------------------------------
    results = {}
    all_scen = SC.scenario_set()
    print("\nSCENARIOS")
    for name, sc in all_scen.items():
        df, cf, model = SC.run_scenario(sc)
        ann = annual_table(df)
        ann.to_csv(f"{OUT}/annual_{name}.csv")
        if name == "Base":
            df.to_csv(f"{OUT}/monthly_base.csv", index=False)
            cf.to_csv(f"{OUT}/cashflow_base.csv", index=False)
        cb = SC.months_to_cash_breakeven(cf)
        terminal = (ann.loc[P.HORIZON_YEARS]
                    if P.HORIZON_YEARS in ann.index else ann.iloc[-1])
        results[name] = {
            "terminal_revenue": float(terminal["revenue"]),
            "terminal_accounts_live": float(terminal["live_accounts"]),
            "terminal_holding": float(terminal["holding"]),
            "terminal_aum": float(terminal["aum_usd"]),
            "cumulative_net_profit": float(df["net_profit"].sum()),
            "terminal_net_profit": float(terminal["net_profit"]),
            **cb,
        }
        print(f"  {name:<22} Y{P.HORIZON_YEARS} rev ${terminal['revenue']:>12,.0f}  "
              f"peak fund ${cb['peak_funding_requirement']:>11,.0f} @M{cb['peak_funding_month']:<3} "
              f"cum NP ${df['net_profit'].sum():>13,.0f}")

    # -- break-even -------------------------------------------------------
    base_df, base_cf, base_model = SC.run_scenario(all_scen["Base"])
    be_all = SC.breakeven_fixed_point(base_df, "all_streams")
    be_fee = SC.breakeven_fixed_point(base_df, "entry_fee_only")
    print("\nBREAK-EVEN (fixed point revenue(N) = TOTAL COST(N))")
    for be in (be_fee, be_all):
        sol = be["solution"]
        print(f"  {be['view']:<16} solution N = "
              f"{(f'{sol:,.0f} accounts') if sol else 'NONE EXISTS'}"
              f"   EBITDA-positive year = {be['breakeven_year_ebitda'] or f'none in {P.HORIZON_YEARS}'}")
        if be["extrapolated_breakeven_year"]:
            print(f"                   -> extrapolates to Y"
                  f"{be['extrapolated_breakeven_year']:.1f} on the current trajectory")

    print("\nMINIMUM VIABLE ENTRY FEE (given endogenous denomination + premium)")
    fee_path = SC.solve_minimum_entry_fee(base_df, "Base")
    fee_path.to_csv(f"{OUT}/minimum_entry_fee_path.csv", index=False)
    for _, r in fee_path.iterrows():
        flag = "" if r["achievable"] else "  <== NOT FUNDABLE"
        print(f"  Y{int(r['year']):<2} assumed {r['assumed fee']*100:.1f}%  "
              f"min viable {r['min viable fee (binding)']*100:.2f}%  "
              f"({r['shortfall_pp']:+.2f}pp){flag}")
    print("  Opex(N), block by block (driver | fixed | variable per account):")
    for blk, f in be_all["fit"].items():
        if f["driver"] == "fixed":
            print(f"    {blk:<22} year-indexed step (does not scale with N)")
        else:
            print(f"    {blk:<22} {f['driver']:<13} {f['fixed']:>10,.0f} + "
                  f"{f['variable']:>7.2f} x N")
    print(f"  holding:contributing ratio at Y10 = {be_all['holding_ratio']:.2f}x")

    # -- sensitivity ------------------------------------------------------
    print("\nTORNADO (cumulative net profit)")
    t_np = SC.tornado("net_profit")
    t_np.to_csv(f"{OUT}/tornado_net_profit.csv", index=False)
    for _, r in t_np.head(6).iterrows():
        print(f"  {r['driver']:<38} swing ${r['swing']:>13,.0f}")

    t_pf = SC.tornado("peak_funding")
    t_pf.to_csv(f"{OUT}/tornado_peak_funding.csv", index=False)

    grid = SC.pm_share_card_spend_grid()
    grid.to_csv(f"{OUT}/grid_pm_share_x_card_spend.csv", index=False)

    # -- G2 parameter solvers ---------------------------------------------
    solved = SC.solve_parameters(base_df, "Base")
    solved.to_csv(f"{OUT}/solved_parameters.csv", index=False)
    print("\nPARAMETER SOLVERS (brief 9)")
    for _, r in solved.iterrows():
        print(f"  [{r['status']:<18}] item {int(r['item'])}: {r['solved_value']}")

    # -- G4 gold price axis and collateral stress -------------------------
    gold = SC.gold_level_sensitivity()
    gold.to_csv(f"{OUT}/gold_level_sensitivity.csv", index=False)
    shock = SC.gold_shock_scenarios()
    shock.to_csv(f"{OUT}/gold_shock_scenarios.csv", index=False)
    print("\nGOLD LEVEL (invariant USD AUM) vs SHOCK at M61")
    for _, r in shock.iterrows():
        print(f"  shock {r['gold_move']*100:+.0f}%: margin calls "
              f"${r['margin_calls_usd']:,.0f}, {r['grams_liquidated']:,.0f} g "
              f"liquidated, float covers peak: {r['float_covers_peak']}")
    stress = SC.sovereign_collateral_stress(base_df, "Base")
    pd.DataFrame(stress["tiers"]).to_csv(f"{OUT}/collateral_stress.csv", index=False)
    print("\nCOLLATERAL STRESS (fall needed to reach a 92% margin call)")
    for t in stress["tiers"]:
        print(f"  {t['tier']:<10} LTV {t['struck_ltv']:.0%}  needs "
              f"{t['fall_to_margin_call']*100:>6.1f}%   within 1 sigma: "
              f"{t['within_one_sigma']}")

    # -- G1 gate arrival ---------------------------------------------------
    gate = base_model.gate_statistics()
    pd.DataFrame(gate["by_archetype"]).to_csv(f"{OUT}/gate_arrival.csv", index=False)
    print(f"\nGATE ARRIVAL: expected month {gate['expected_gate_month']:.1f}, "
          f"ever-gate {gate['ever_gate_share']*100:.1f}%, never-gated "
          f"{gate['never_gate_share']*100:.1f}%")

    ltv = SC.ltv_cac(base_df, "Base")
    ltv.to_csv(f"{OUT}/ltv_cac.csv", index=False)
    ue = SC.unit_economics_by_band("Base")
    ue.to_csv(f"{OUT}/unit_economics_by_band.csv", index=False)

    # -- rebuild artefacts -------------------------------------------------
    from pnl import validate_view29, view29
    import lifecycle as LC

    view = view29(base_df)
    view.to_csv(f"{OUT}/view29_Base.csv")
    vchecks = validate_view29(base_df, view)
    pd.DataFrame(vchecks).to_csv(f"{OUT}/validation_view29.csv", index=False)
    print("")
    print(f"{P.VIEW_COLUMNS}-COLUMN VIEW: {view.shape[0]} lines x "
          f"{view.shape[1]} columns, "
          f"{sum(1 for r in vchecks if r['pass'])}/{len(vchecks)} checks pass")

    eq = LC.equivalence_test("Base")
    pd.DataFrame([{"quantity": k, **v} for k, v in eq.items()
                  if isinstance(v, dict)]).to_csv(
        f"{OUT}/validation_convolution_equivalence.csv", index=False)
    print(f"D23 EQUIVALENCE (convolution vs vintage triangle): "
          f"max relative residual {eq['max_rel_pct']:.3e}%  -> "
          f"{'PASS' if eq['pass'] else 'FAIL'}")

    decomp = LC.annual_decomposition_check("Base")
    pd.DataFrame(decomp).to_csv(f"{OUT}/validation_annual_decomposition.csv",
                                index=False)
    print(f"D23 ANNUAL DECOMPOSITION (check 8): "
          f"{sum(1 for r in decomp if r['pass'])}/{len(decomp)} pass; "
          f"convolving an annual aggregate would err up to "
          f"{max(abs(r['annual_aggregate_would_err_pct']) for r in decomp):.1f}%")

    collapse = base_model.collapse_safety_gate(base_df)
    pd.DataFrame(collapse).to_csv(f"{OUT}/validation_collapse_gate.csv",
                                  index=False)
    coll_ok = all(r["within_5pct_gate"] for r in collapse)
    peak_c = max(r["cost_pct_of_gross_profit"] for r in collapse)
    print(f"D22 COLLAPSE SAFETY GATE: peak cost {peak_c:.2f}% of gross profit "
          f"-> {'SAFE' if coll_ok else 'UNSAFE, REVERT TO FULL LADDER'}")

    rail = SC.rail_incidence("Base")
    rail.to_csv(f"{OUT}/rail_incidence.csv", index=False)
    print("D31 RAIL INCIDENCE (pass-through, regressive):")
    for _, r in rail.iterrows():
        print(f"  {r['region']} {r['band']:<9} ticket {r['ticket_usd']:>6.2f} "
              f"-> request {r['request_amount_usd']:>6.2f} "
              f"({r['gross_up_pct_of_ticket']:.3f}% of ticket)")

    unit = SC.book_weighted_unit_economics(base_df, "Base")
    with open(f"{OUT}/unit_economics_headline.json", "w") as f:
        json.dump(unit, f, indent=2, default=_j)
    print("UNIT ECONOMICS:")
    for k in ("usd_75_illustration", "book_weighted"):
        u = unit[k]
        print(f"  {k:<22} ticket {u['ticket_usd']:>7.2f}  gross "
              f"{u['gross_margin_pct']:>6.3f}%  net contribution "
              f"{u['net_contribution_margin_pct']:>6.3f}%")
    print(f"  CORRECTION 26: model produces "
          f"{unit['correction_26']['model_at_v1_premium_3pct']:.3f}% at the "
          f"v1.0 3.00% premium (brief states 0.72% AND 2.15%)")

    d33 = SC.redeemed_gold_switch_comparison()
    d33.to_csv(f"{OUT}/d33_redeemed_gold_switch.csv", index=False)
    print("D33 REDEEMED_GOLD_TO_FLOAT, both settings:")
    for _, r in d33.iterrows():
        print(f"  {str(r['REDEEMED_GOLD_TO_FLOAT']):<5} ({r['routing']:<28}) "
              f"cum premium ${r['cumulative_premium_cost']:>12,.0f}  "
              f"cum NP ${r['cumulative_net_profit']:>13,.0f}  "
              f"peak fund ${r['peak_funding']:>12,.0f}")

    dbt = SC.float_debt_funded_comparison()
    dbt.to_csv(f"{OUT}/d32_float_debt_funded.csv", index=False)
    print("D32 FLOAT_DEBT_FUNDED, both settings:")
    for _, r in dbt.iterrows():
        print(f"  {str(r['FLOAT_DEBT_FUNDED']):<5} ({r['treatment']:<42}) "
              f"cum NP ${r['cumulative_net_profit']:>13,.0f}  "
              f"interest ${r['cumulative_float_interest']:>10,.0f}")

    pd.DataFrame(personas).to_csv(f"{OUT}/validation_personas.csv", index=False)
    pd.DataFrame(gates).to_csv(f"{OUT}/validation_gate_mechanics.csv", index=False)
    pd.DataFrame(fit).to_csv(f"{OUT}/validation_survival_fit.csv", index=False)
    pd.DataFrame(P.DERIVED_REGISTER).to_csv(f"{OUT}/derived_parameters.csv", index=False)
    pd.DataFrame(P.CONFLICT_REGISTER).to_csv(f"{OUT}/source_conflicts.csv", index=False)

    # -- headline JSON ----------------------------------------------------
    ann_base = annual_table(base_df)
    headline = {
        "scenarios": results,
        "survival_fit": {"anchors": fit, "rmse_sourced_pp": rmse_src,
                         "rmse_calibrated_pp": rmse_cal,
                         "m84_survival": float(s_sourced[P.HORIZON_MONTHS]),
                         "calibrated_weights": {k: float(v) for k, v in w.items()},
                         "calibrated_background_hazard": float(bg)},
        "personas_pass": f"{n_pass}/{len(personas)}",
        "gate_mechanics_pass": f"{n_gate}/{len(gates)}",
        "breakeven": {
            "basis": "revenue(N) = total_cost(N), not opex alone",
            "entry_fee_only": {
                "solution_accounts": be_fee["solution"],
                "breakeven_year_ebitda": be_fee["breakeven_year_ebitda"],
                "extrapolated_year": be_fee["extrapolated_breakeven_year"]},
            "all_streams": {
                "solution_accounts": be_all["solution"],
                "breakeven_year_ebitda": be_all["breakeven_year_ebitda"],
                "extrapolated_year": be_all["extrapolated_breakeven_year"]},
            "minimum_entry_fee_path": fee_path.to_dict("records"),
            "opex_blocks": {k: dict(v) for k, v in be_all["fit"].items()},
            "holding_to_contributing_ratio": be_all["holding_ratio"],
        },
        "terminal_revenue_stack": {
            "stream1_sip": float(ann_base.loc[P.HORIZON_YEARS, "stream1_sip"]),
            "stream1_spot": float(ann_base.loc[P.HORIZON_YEARS, "stream1_spot"]),
            "stream2_card_interchange": float(ann_base.loc[P.HORIZON_YEARS, "stream2"]),
            "stream3_family": float(ann_base.loc[P.HORIZON_YEARS, "stream3"]),
            "stream4_cardholder_fees": float(ann_base.loc[P.HORIZON_YEARS, "stream4"]),
            "stream5_credit": float(ann_base.loc[P.HORIZON_YEARS, "stream5"]),
            "stream6_b2b": float(ann_base.loc[P.HORIZON_YEARS, "stream6"]),
            "total": float(ann_base.loc[P.HORIZON_YEARS, "revenue"]),
        },
        "aum_reconciliation": {
            "terminal_aum": float(ann_base.loc[P.HORIZON_YEARS, "aum_usd"]),
            "terminal_cumulative_contributions": float(
                (base_df["inflow_sip"] + base_df["inflow_spot"]).sum()),
        },
        "derived_parameter_count": len(P.DERIVED_REGISTER),
        "source_conflict_count": len(P.CONFLICT_REGISTER),
    }
    with open(f"{OUT}/headline_results.json", "w") as f:
        json.dump(headline, f, indent=2, default=_j)

    # -- the spine and validation documents, regenerated from THIS run ----
    # build_spine used to be an orphan: nothing imported it and nothing called
    # it, so NUMERICAL_SPINE.md and VALIDATION.md drifted away from the model
    # the moment any parameter moved. Calling it here makes both documents
    # reproducible rather than hand-maintained.
    import build_spine
    build_spine.build(write=True)

    print(f"\nOutputs written to {OUT}")
    print(f"  DERIVED_BY_MODEL parameters: {len(P.DERIVED_REGISTER)}")
    print(f"  Source conflicts logged    : {len(P.CONFLICT_REGISTER)}")
    return headline


if __name__ == "__main__":
    main()
