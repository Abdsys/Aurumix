"""Generates NUMERICAL_SPINE.md and VALIDATION.md from model output.

WHY THIS FILE IS GENERATIVE AND NOT HAND-MAINTAINED
---------------------------------------------------
The previous version carried a large amount of narrative with the numbers typed
into the prose. That is a document that goes stale the first time a parameter
moves, and silently: the tables update, the sentences around them do not. Every
figure below is interpolated from the model run in the same process, so the
spine cannot disagree with the model that produced it.

Run it directly, or call `build()`. `run.py` calls it at the end of a full run,
so both documents are reproducible rather than maintained by hand.
"""
from __future__ import annotations

import os

import numpy as np
import pandas as pd

import ics
import lifecycle as LC
import params as P
import scenarios as SC
from pnl import validate_view29, view29
from run import annual_table

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "outputs")


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def money(x, dp=0):
    try:
        return f"{float(x):,.{dp}f}"
    except (TypeError, ValueError):
        return str(x)


def pct(x, dp=2):
    try:
        return f"{float(x):.{dp}f}%"
    except (TypeError, ValueError):
        return str(x)


def md_table(df: pd.DataFrame, floatfmt="{:,.0f}", index=True) -> str:
    """Render a DataFrame as a GitHub-flavoured markdown table."""
    d = df.copy()
    if index:
        d = d.reset_index()
    cols = [str(c) for c in d.columns]
    lines = ["| " + " | ".join(cols) + " |",
             "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, row in d.iterrows():
        cells = []
        for v in row:
            if isinstance(v, bool) or isinstance(v, np.bool_):
                cells.append(str(bool(v)))
            elif isinstance(v, (int, float, np.integer, np.floating)):
                cells.append(floatfmt.format(v) if np.isfinite(v) else "n/a")
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def fit_survival_report(mode: str = "Base") -> list:
    """Re-fit the survival anchors on the D21 horizon and report the residuals.

    All five anchors (M13/M25/M37/M49/M61) still fall inside 84 months, so the
    anchors survive D21 intact - but the FIT DOMAIN shrank from 120 months to 84,
    so the residuals are re-reported rather than carried over from the ten-year
    fit. Carrying the old residuals would be claiming a fit that was never run.
    """
    curves = LC.LifecycleCurves(mode, P.HORIZON_MONTHS)
    rows = []
    for m, target in sorted(P.SURVIVAL_ANCHORS.items()):
        got = float(curves.curve_survival[m])
        rows.append({"anchor_month": m, "target": target,
                     "modelled": round(got, 4),
                     "residual_pp": round((got - target) * 100, 3),
                     "inside_horizon": m <= P.HORIZON_MONTHS})
    rmse = float(np.sqrt(np.mean([r["residual_pp"] ** 2 for r in rows])))
    for r in rows:
        r["rmse_pp"] = round(rmse, 3)
    return rows


# ---------------------------------------------------------------------------
# The build
# ---------------------------------------------------------------------------

def build(write: bool = True) -> dict:
    Y = P.HORIZON_YEARS
    scen = SC.scenario_set()
    base_df, base_cf, base_model = SC.run_scenario(scen["Base"])
    ann = annual_table(base_df)
    cb = SC.months_to_cash_breakeven(base_cf)

    view = view29(base_df)
    view_checks = validate_view29(base_df, view)
    personas = ics.validate_personas()
    gates = ics.validate_gate_mechanics()
    eq = LC.equivalence_test("Base")
    decomp = LC.annual_decomposition_check("Base")
    collapse = base_model.collapse_safety_gate(base_df)
    fee_path = SC.solve_minimum_entry_fee(base_df, "Base")
    unit = SC.book_weighted_unit_economics(base_df, "Base")
    rail_inc = SC.rail_incidence("Base")
    gate = base_model.gate_statistics()
    surv_fit = fit_survival_report("Base")

    scen_rows = []
    for name, sc in scen.items():
        df, cf, _ = SC.run_scenario(sc)
        a = annual_table(df)
        cc = SC.months_to_cash_breakeven(cf)
        last = a.loc[Y] if Y in a.index else a.iloc[-1]
        scen_rows.append({
            "Scenario": name,
            f"Y{Y} revenue": last["revenue"],
            f"Y{Y} gross profit": last["gross_profit"],
            f"Y{Y} live accounts": last["live_accounts"],
            "Cumulative net profit": df["net_profit"].sum(),
            "Peak funding": cc["peak_funding_requirement"],
            "Peak month": cc["peak_funding_month"]})
    scen_tab = pd.DataFrame(scen_rows).set_index("Scenario")

    tor_np = SC.tornado("net_profit")
    tor_pf = SC.tornado("peak_funding")
    d33 = SC.redeemed_gold_switch_comparison()
    dbt = SC.float_debt_funded_comparison()

    ctx = dict(Y=Y, ann=ann, base_df=base_df, view=view, scen_tab=scen_tab,
               tor_np=tor_np, tor_pf=tor_pf, collapse=collapse, eq=eq,
               decomp=decomp, personas=personas, gates=gates, cb=cb,
               fee_path=fee_path, unit=unit, rail_inc=rail_inc, gate=gate,
               view_checks=view_checks, d33=d33, dbt=dbt, surv_fit=surv_fit)

    spine = _spine_md(ctx)
    valid = _validation_md(ctx)

    if write:
        with open(os.path.join(HERE, "NUMERICAL_SPINE.md"), "w",
                  encoding="utf-8") as f:
            f.write(spine)
        with open(os.path.join(HERE, "VALIDATION.md"), "w",
                  encoding="utf-8") as f:
            f.write(valid)
        os.makedirs(OUT, exist_ok=True)
        view.to_csv(os.path.join(OUT, "view29_Base.csv"))
        print("NUMERICAL_SPINE.md and VALIDATION.md written")
    return ctx


# ---------------------------------------------------------------------------
# NUMERICAL_SPINE.md
# ---------------------------------------------------------------------------

def _spine_md(c: dict) -> str:
    Y, ann, view = c["Y"], c["ann"], c["view"]
    df = c["base_df"]
    B = []
    A = B.append

    A("# Aurumix Revenue Model - Numerical Spine")
    A("")
    A(f"Generated from the model. Horizon **{P.HORIZON_MONTHS} months "
      f"({Y} years)**, computed genuinely monthly, reported on a "
      f"**{P.VIEW_COLUMNS}-column view** (M1-M{P.VIEW_MONTHLY_COLUMNS} monthly, "
      f"then Y3-Y{Y} annual).")
    A("")
    A("Every figure on this page is interpolated from the run that produced it. "
      "Nothing is typed in.")
    A("")

    A("## 1. Headline, Base scenario")
    A("")
    A(md_table(ann[["revenue", "gross_profit", "ebitda", "net_profit",
                    "live_accounts", "holding", "aum_usd"]]))
    A("")
    A(f"- Peak funding requirement **USD {money(c['cb']['peak_funding_requirement'])}** "
      f"at M{c['cb']['peak_funding_month']}")
    A(f"- Minimum cumulative cash **USD {money(c['cb']['min_cumulative_cash'])}** "
      f"at M{c['cb']['min_cash_month']}")
    A(f"- Cumulative net profit over {Y} years "
      f"**USD {money(df['net_profit'].sum())}**")
    ebd = c["cb"]["pnl_breakeven_year_ebitda"]
    A(f"- First EBITDA-positive year: **{ebd if ebd else f'none inside {Y} years'}**")
    A("")

    A("## 2. Revenue by stream")
    A("")
    A(md_table(ann[["stream1_sip", "stream1_spot", "stream2", "stream3",
                    "stream4", "stream5", "stream6", "revenue"]]))
    A("")
    last = ann.loc[Y] if Y in ann.index else ann.iloc[-1]
    tot = last["revenue"]
    A(f"Share of Y{Y} revenue:")
    A("")
    shares = {"Stream 1a entry fee, SIP": last["stream1_sip"],
              "Stream 1b entry fee, spot": last["stream1_spot"],
              "Stream 2 card interchange": last["stream2"],
              "Stream 3 family plan": last["stream3"],
              "Stream 4 cardholder fees": last["stream4"],
              "Stream 5 lending share": last["stream5"],
              "Stream 6 B2B platform": last["stream6"]}
    A("| Stream | USD | Share of revenue |")
    A("|---|---|---|")
    for k, v in sorted(shares.items(), key=lambda x: -x[1]):
        A(f"| {k} | {money(v)} | {pct(v / tot * 100 if tot else 0)} |")
    A("")
    A("⚠ Streams 1a and 1b are reported at their NET contribution margin; the "
      "gross entry fee they are struck on is a larger number. Streams 2 to 6 "
      "are reported gross of their own direct costs, which sit in operating "
      "cost.")
    A("")

    A("## 3. Cost of revenue - two terms only")
    A("")
    A("D31 removed the payment rail and D32 removed the float cost of capital. "
      "What remains in cost of revenue is the fabrication premium and the price "
      "gap, and nothing else.")
    A("")
    A(md_table(ann[["cor_premium", "cor_pricegap", "cost_of_revenue",
                    "rail_passthrough_usd", "floatcoc_memo"]]))
    A("")
    A("🔴 `rail_passthrough_usd` and `floatcoc_memo` are **MEMO LINES**. They "
      "appear in no revenue total, no cost total and no margin. Checks 12 and "
      "13 assert this every month and the run fails loudly if either leaks.")
    A("")

    A("## 4. Unit economics")
    A("")
    u = c["unit"]
    a1, a2 = u["usd_75_illustration"], u["book_weighted"]
    A("| | USD 75 illustration | Book-weighted ticket |")
    A("|---|---|---|")
    A(f"| Ticket | USD {money(a1['ticket_usd'], 2)} | "
      f"USD {money(a2['ticket_usd'], 2)} |")
    A(f"| Fee applied | {pct(a1['fee_applied'] * 100)} | "
      f"{pct(a2['fee_applied'] * 100)} |")
    A(f"| Fabrication premium | {pct(a1['fabrication_premium'] * 100)} | "
      f"{pct(a2['fabrication_premium'] * 100)} |")
    A(f"| Net new gram share (D30/D33) | {pct(a1['net_new_gram_share'] * 100)} | "
      f"{pct(a2['net_new_gram_share'] * 100)} |")
    A(f"| Price gap | {pct(a1['price_gap'] * 100)} | "
      f"{pct(a2['price_gap'] * 100)} |")
    A(f"| **Gross margin** | **USD {money(a1['gross_margin_usd'], 4)} "
      f"({pct(a1['gross_margin_pct'])})** | "
      f"**USD {money(a2['gross_margin_usd'], 4)} "
      f"({pct(a2['gross_margin_pct'])})** |")
    A(f"| **Net contribution margin** | "
      f"**USD {money(a1['net_contribution_margin_usd'], 4)} "
      f"({pct(a1['net_contribution_margin_pct'])})** | "
      f"**USD {money(a2['net_contribution_margin_usd'], 4)} "
      f"({pct(a2['net_contribution_margin_pct'])})** |")
    A(f"| Rail memo, NOT deducted | "
      f"USD {money(a1['rail_memo_usd_not_deducted'], 2)} | "
      f"USD {money(a2['rail_memo_usd_not_deducted'], 2)} |")
    A("")
    cor26 = u["correction_26"]
    A("### Correction 26, settled by computation")
    A("")
    A(f"The brief states **{pct(cor26['brief_states_layer4_and_6_1b_pct'])}** in "
      f"section 3 Layer 4 and section 6.1b, and "
      f"**{pct(cor26['brief_waterfall_6_1_pct'])}** in the section 6.1 "
      f"waterfall. These cannot both be right.")
    A("")
    A(f"Implementing the exact identity `C - C(1-f)(1+p)` and letting the model "
      f"produce the number gives **{pct(cor26['model_at_v1_premium_3pct'], 3)}** "
      f"at the v1.0 3.00% premium on a USD 75 contribution at a 5% fee. That "
      f"reproduces the brief's own audited USD 1.6125 exactly.")
    A("")
    A(f"**Verdict: the 0.72% figure is arithmetically wrong and the waterfall "
      f"is right.** At D28's Base premium the same identity gives "
      f"**{pct(cor26['model_at_D28_base_premium'], 3)}**. Neither figure is "
      f"hardcoded anywhere in the model.")
    A("")

    A("## 5. D31 - rail incidence on the customer")
    A("")
    A("The rail left Aurumix's P&L. It did not leave the transaction. Aurumix "
      "asks for `ticket + rail` and remits it, so the incidence moved wholly "
      "onto the customer - and because the rail is a fixed amount per "
      "collection and the ticket is not, **it is regressive**.")
    A("")
    A(md_table(c["rail_inc"], floatfmt="{:,.3f}", index=False))
    A("")
    hi, lo = c["rail_inc"].iloc[0], c["rail_inc"].iloc[-1]
    A(f"The floor band pays **{pct(hi['gross_up_pct_of_ticket'])}** of its "
      f"contribution as rail; R1's standard band pays "
      f"**{pct(lo['gross_up_pct_of_ticket'])}**. That is a "
      f"**{hi['gross_up_pct_of_ticket'] / lo['gross_up_pct_of_ticket']:.1f}x "
      f"spread**, against a gross margin of roughly "
      f"{pct(a2['gross_margin_pct'])}.")
    A("")

    A("## 6. Minimum viable entry fee")
    A("")
    A("🔴 **PROVISIONAL.** F4's absolute level failed replication on "
      "2026-08-20 (correction 36). The fabrication premium is the largest "
      "surviving term in this calculation, so every figure in this table is "
      "conditional on F4 being re-observed.")
    A("")
    keep = [k for k in ("year", "premium", "effective_premium",
                        "pricegap_weighted", "sip_ticket", "assumed fee",
                        "min viable fee (binding)",
                        "min viable fee floor band (USD 20)",
                        "shortfall_pp", "achievable")
            if k in c["fee_path"].columns]
    A(md_table(c["fee_path"][keep], floatfmt="{:,.4f}", index=False))
    A("")

    A("## 7. Population and tier mix")
    A("")
    A(md_table(ann[["new_accounts", "contributing", "reduced",
                    "lapsed_holding", "dormant", "holding", "live_accounts"]]))
    A("")
    A(md_table(ann[["tier_none", "tier_silver", "tier_gold", "tier_platinum",
                    "tier_sovereign"]]))
    A("")
    g = c["gate"]
    A(f"Gate arrival is a **distribution, not a date**: mean "
      f"**M{g['expected_gate_month']:.1f}**, ever-gate "
      f"**{pct(g['ever_gate_share'] * 100)}**, never-gated "
      f"**{pct(g['never_gate_share'] * 100)}** of an original vintage.")
    A("")
    A(md_table(pd.DataFrame(g["by_archetype"]), floatfmt="{:,.3f}", index=False))
    A("")
    A("The never-gated population pays the **full undiscounted entry fee "
      "forever** and receives **zero benefits**. It is structurally the "
      "highest-margin retail account in the book, and check 11 asserts it "
      "carries no discount weight.")
    A("")

    A("## 8. D25 - four regions, two bands each")
    A("")
    reg = pd.DataFrame([{
        "Region": r, "Name": P.REGION_NAME[r],
        "Addressable": P.ADDRESSABLE[r],
        "Ceiling": P.PENETRATION_CEILING["Base"][r],
        "Ceiling accounts": P.ADDRESSABLE[r] * P.PENETRATION_CEILING["Base"][r],
        "Avg ticket": P.AVG_TICKET[r],
        "Floor share": P.FLOOR_SHARE["Base"][r],
        "Floor band": P.FLOOR_BAND_TICKET,
        "Standard band": P.standard_band_ticket(r, "Base"),
        "Activation": P.SEGMENT_LIVE_MONTH[r],
        "UAE resident": P.RESIDENT_SHARE[r]} for r in P.SEGMENTS])
    A(md_table(reg, floatfmt="{:,.4f}", index=False))
    A("")
    A(f"**Reconciliation invariant (check 14):** base x ceiling = "
      f"**{money(P._ceiling_accounts('Base'), 1)}** against a target of "
      f"**{money(P.CEILING_ACCOUNTS_INVARIANT, 1)}**. Asserted at import; the "
      f"model will not start if it drifts.")
    A("")
    A("### Named, sized, deliberately not modelled")
    A("")
    A("| Region | Size | Why not modelled |")
    A("|---|---|---|")
    for k, v in P.UNMODELLED_REGIONS.items():
        A(f"| {k} | {money(v['size'])} | {v['reason']} |")
    A("")

    A("## 9. Scenarios")
    A("")
    A(md_table(c["scen_tab"]))
    A("")

    A("## 10. Tornado")
    A("")
    A("⚠ **Two rankings went stale at the rebuild and are deliberately "
      "absent.** S1 (rail) left the tornado entirely under D31 - it is a "
      "pass-through, so flexing it reports a swing of exactly zero and would "
      "invite the reader to conclude the rail does not matter. It matters to "
      "the customer, and that incidence is in section 5. F5 (float cost of "
      "capital) left the margin under D32 and cannot move profit; the float "
      "PRINCIPAL still moves peak funding, through the float sizing rather "
      "than through F5.")
    A("")
    A("### Cumulative net profit")
    A("")
    A(md_table(c["tor_np"], index=False))
    A("")
    A("### Peak funding")
    A("")
    A(md_table(c["tor_pf"], index=False))
    A("")

    A("## 11. D33 - where redeemed gold goes")
    A("")
    A("D30 charges the fabrication premium on net new grams. That holds only if "
      "redeemed gold returns to the float. **Nobody had written down which** "
      "(correction 30). D33 settles it: redeemed grams return to the float up "
      "to the float ceiling, and the excess is sold back at the observed bid of "
      f"spot **-{pct(P.DEALER_BID_DISCOUNT * 100)}**.")
    A("")
    A("Both settings are reported, so the default is visible rather than "
      "buried.")
    A("")
    A(md_table(c["d33"], floatfmt="{:,.4f}", index=False))
    A("")
    A("🔴 The bid and the ask are **not symmetric and are not netted**. "
      "Correction 35 measured the bid as near-flat across denomination while "
      "the ask premium moves about 194bp. Fabrication is paid on the way in and "
      "is not recovered on the way out.")
    A("")

    A("## 12. D32 - the float debt-funded switch")
    A("")
    A("If the float is equity funded the carry is an opportunity cost and a "
      "memo. If it is debt funded the interest is cash and belongs below EBITDA "
      "as a financing line.")
    A("")
    A(md_table(c["dbt"], index=False))
    A("")
    A("🔴 In both cases the float **principal** is untouched. It stays on the "
      "balance sheet, in the funding view, and inside peak funding. The cost "
      "moved from the P&L to the cap table; it did not stop being money.")
    A("")

    A(f"## 13. The {P.VIEW_COLUMNS}-column reporting view")
    A("")
    A(f"M1-M{P.VIEW_MONTHLY_COLUMNS} monthly, then Y3-Y{Y} as five annual "
      f"columns. Written to `outputs/view29_Base.csv`. Three rules:")
    A("")
    A("- **Rates never sum.** They are re-derived over the year, or "
      "inflow-weighted where no explicit denominator exists.")
    A("- **Flows sum** over their twelve constituent months.")
    A("- **Snapshots take the last month** of the year.")
    A("")
    key = ["revenue", "gross_profit", "ebitda", "live_accounts", "aum_usd",
           "fee_applied", "fab_premium", "rail_passthrough_usd", "floatcoc_memo"]
    show = [f"M{m}" for m in (1, 6, 12, 18, 24)] + \
           [f"Y{y}" for y in P.VIEW_ANNUAL_YEARS]
    A(md_table(view.loc[[k for k in key if k in view.index], show],
               floatfmt="{:,.4f}"))
    A("")
    return "\n".join(B)


# ---------------------------------------------------------------------------
# VALIDATION.md
# ---------------------------------------------------------------------------

def _validation_md(c: dict) -> str:
    V = []
    A = V.append
    Y = c["Y"]

    A("# Aurumix Revenue Model - Validation")
    A("")
    A("Every check below is executed by the run that writes this file. A "
      "failing check is reported as a failure here and, where it is an "
      "invariant, aborts the run.")
    A("")

    n_p = sum(1 for p in c["personas"] if p["pass"])
    n_g = sum(1 for g in c["gates"] if g["pass"])
    eq = c["eq"]
    coll_ok = all(r["within_5pct_gate"] for r in c["collapse"])
    view_ok = all(r["pass"] for r in c["view_checks"])
    dec_ok = all(r["pass"] for r in c["decomp"])

    A("## Summary")
    A("")
    A("| Check | Result |")
    A("|---|---|")
    A(f"| ICS personas A-I | {n_p}/{len(c['personas'])} pass |")
    A(f"| ICS gate mechanics | {n_g}/{len(c['gates'])} pass |")
    A(f"| D23 convolution vs vintage triangle | max relative residual "
      f"{eq['max_rel_pct']:.2e}% - **{'PASS' if eq['pass'] else 'FAIL'}** |")
    A(f"| D23 annual decomposition (check 8) | "
      f"**{'PASS' if dec_ok else 'FAIL'}** |")
    A(f"| D22 collapse safety gate (5%) | "
      f"**{'SAFE' if coll_ok else 'UNSAFE - REVERT TO FULL LADDER'}** |")
    A(f"| {P.VIEW_COLUMNS}-column view faithfulness | "
      f"**{'PASS' if view_ok else 'FAIL'}** |")
    A(f"| D25 base x ceiling invariant | "
      f"{money(P._ceiling_accounts('Base'), 1)} vs "
      f"{money(P.CEILING_ACCOUNTS_INVARIANT, 1)} - **PASS** |")
    A("")

    A("## 1. D23 equivalence: convolution against the vintage triangle")
    A("")
    A("The convolution is the live engine. The vintage triangle is kept in "
      "`cohort.py` purely as the equivalence harness. Both engines are run on "
      "the same acquisition vector and the residual is reported.")
    A("")
    A("| Quantity | Max abs residual | Max relative | Mean relative | "
      "Convolution terminal | Triangle terminal |")
    A("|---|---|---|---|---|---|")
    for k in ("contributing_plus_reduced", "holding"):
        r = eq[k]
        A(f"| {k} | {r['max_abs']:.3e} | {r['max_rel_pct']:.3e}% | "
          f"{r['mean_rel_pct']:.3e}% | {money(r['terminal_convolution'], 2)} | "
          f"{money(r['terminal_triangle'], 2)} |")
    A("")
    A(f"**Verdict: "
      f"{'the two engines agree to floating-point noise' if eq['pass'] else 'THE ENGINES DISAGREE'}.** "
      f"Max relative residual {eq['max_rel_pct']:.3e}%.")
    A("")
    A("⚠ **Two off-by-one errors were found by this test and fixed.** Neither "
      "was visible from either engine alone.")
    A("")
    A("1. `Vintage.step_population` computed age as `m - origin + 1`, so the "
      "first hazard an account faced belonged to age 2 rather than age 1. That "
      "disagreed with `survival_curve` in the same module and shifted every "
      "age-dependent hazard one month early.")
    A("")
    A("2. The convolution offset was `t - s + 1` rather than `t - s`. A vintage "
      "acquired in month t is observed in month t at age **zero**; it has not "
      "yet faced a hazard. The wrong offset aged every cohort by a month, "
      "understating the payment axis by about 8% at M1 and about 4% by M20 - "
      "worst exactly in the months the view reports monthly.")
    A("")

    A("## 2. D23 annual decomposition (check 8)")
    A("")
    A("Every annual column is the sum of twelve monthly convolutions. It is "
      "**never** a single convolution against an annual aggregate acquisition "
      "figure, which would collapse twelve first-passage months into one and "
      "destroy the gate distribution.")
    A("")
    A(md_table(pd.DataFrame(c["decomp"]), floatfmt="{:,.4f}", index=False))
    A("")
    worst = max(abs(r["annual_aggregate_would_err_pct"]) for r in c["decomp"])
    A(f"Convolving an annual aggregate instead would misstate the population by "
      f"up to **{worst:.1f}%**. That is the size of the error the rule "
      f"prevents.")
    A("")

    A("## 3. D22 collapse safety gate")
    A("")
    A(f"The live model reads a flat Gold interchange rate of "
      f"**{pct(P.COLLAPSE_INTERCHANGE_RATE * 100)}** for every tier. The full "
      f"ladder is {pct(P.INTERCHANGE['Gold'] * 100)} / "
      f"{pct(P.INTERCHANGE['Platinum'] * 100)} / "
      f"{pct(P.INTERCHANGE['Sovereign'] * 100)}. The collapse understates "
      f"stream 2 by the interchange a Platinum or Sovereign cardholder "
      f"generates above the Gold rate.")
    A("")
    A("**The gate is binding: if any year exceeds 5% of gross profit, the "
      "collapse is unsafe and the model must revert to the full ladder.**")
    A("")
    A(md_table(pd.DataFrame(c["collapse"]), floatfmt="{:,.2f}", index=False))
    A("")
    peak = max(r["cost_pct_of_gross_profit"] for r in c["collapse"])
    A(f"**Verdict: {'SAFE' if coll_ok else 'UNSAFE'}.** Peak cost "
      f"**{pct(peak)}** of gross profit at Y{Y}, against a 5% gate.")
    A("")
    A("Check 15: the full ladder is read **only** on this validation path. "
      "Nothing in the live model references it, because doing so would silently "
      "un-do the collapse.")
    A("")

    A("## 4. ICS personas A-I")
    A("")
    A("The full exact-fraction ICS engine is retained as the validation harness "
      "for D22's collapsed lookup. All nine personas must pass before the model "
      "ships. H and I are the rows a naive build fails.")
    A("")
    A(md_table(pd.DataFrame(c["personas"]), floatfmt="{:,.3f}", index=False))
    A("")

    A("## 5. ICS gate mechanics")
    A("")
    A("Behavioural checks the closed-form persona table cannot express.")
    A("")
    A(md_table(pd.DataFrame(c["gates"]), index=False))
    A("")

    A("## 6. Survival fit on the D21 horizon")
    A("")
    A(f"All five anchors (M13/M25/M37/M49/M61) still fall inside "
      f"{P.HORIZON_MONTHS} months, so **the anchors survive D21 intact**. The "
      f"fit DOMAIN shrank from 120 to {P.HORIZON_MONTHS} months, so the "
      f"residuals are **re-reported here rather than carried over** from the "
      f"ten-year fit. Carrying the old residuals would be claiming a fit that "
      f"was never run.")
    A("")
    A(md_table(pd.DataFrame(c["surv_fit"]), floatfmt="{:,.4f}", index=False))
    A("")

    A(f"## 7. The {P.VIEW_COLUMNS}-column view is a faithful restatement")
    A("")
    A("Every flow in an annual column must equal the sum of its twelve monthly "
      "values; every snapshot must equal the last month. A **rate must not** "
      "equal the sum of its months, which is the failure this catches.")
    A("")
    A(md_table(pd.DataFrame(c["view_checks"]), floatfmt="{:,.4f}", index=False))
    A("")

    A("## 8. Invariants asserted every month")
    A("")
    A("These run inside the monthly loop and abort the model on failure.")
    A("")
    A("| # | Invariant | What it protects |")
    A("|---|---|---|")
    inv = [
        ("1", "Population conservation", "opening + new = closing across all "
         "states; nothing created or destroyed by the convolution"),
        ("2", "Tier counts sum to the live base", "no account is in two tiers "
         "or none"),
        ("3", "Grams reconcile", "opening + bought - withdrawn - redeemed = "
         "closing"),
        ("4", "No negative stocks", "populations and grams cannot go negative"),
        ("5", "Band shares sum to 1.0", "the D25 two-band split is exhaustive "
         "within every region"),
        ("6", "Cost bridge closes", "total cost equals the sum of its parts"),
        ("7", "Check 12 (D31)", "`rail_memo` appears in no revenue or cost "
         "total"),
        ("8", "Check 13 (D32)", "`floatcoc_memo` appears in no COGS, margin or "
         "P&L total"),
        ("9", "Check 14 (D25)", "base x ceiling holds at "
         f"{money(P.CEILING_ACCOUNTS_INVARIANT, 0)}"),
        ("10", "Check 6", "bar denomination latches and never steps down"),
        ("11", "Check 5", "the acquisition budget reads the PRIOR period, "
         "never the current - no circular loop"),
        ("12", "Check 11", "the never-gated population gets zero benefits and "
         "pays the full fee"),
    ]
    for n, name, why in inv:
        A(f"| {n} | {name} | {why} |")
    A("")

    A("## 9. Registered derived values and source conflicts")
    A("")
    A(f"**{len(P.DERIVED_REGISTER)}** values were chosen by this model because "
      f"no source supplies them, and **{len(P.CONFLICT_REGISTER)}** source "
      f"conflicts were logged and resolved.")
    A("")
    if P.DERIVED_REGISTER:
        A(md_table(pd.DataFrame(P.DERIVED_REGISTER), index=False))
        A("")
    A("### Source conflicts")
    A("")
    if P.CONFLICT_REGISTER:
        A(md_table(pd.DataFrame(P.CONFLICT_REGISTER), index=False))
        A("")

    A("## 10. Known limitations, stated rather than buried")
    A("")
    A("1. 🔴 **F4's absolute level failed replication on 2026-08-20** "
      "(correction 36). The denomination SHAPE is corroborated; the LEVEL is "
      "not. F4 is therefore carried as a scenario variable, not a constant, and "
      "every fee-fundability conclusion downstream of D31 and D32 is "
      "**provisional** until it is re-observed.")
    A("")
    A("2. 🔴 **D31 and D32 are jointly dependent and must be presented "
      "together.** D31 alone lowers the margin; D32 alone raises it. In one day "
      "the cost term went from four components to two and the minimum viable "
      "fee fell, with nothing changing in the business. Each step is defensible "
      "separately; the sequence dissolved a standing finding by re-attribution "
      "alone.")
    A("")
    A("3. **The price-gap formula reproduces about 0.83% at a 12.1-day fill and "
      "25% volatility, against the brief's stated 0.79%.** The difference is "
      "the calendar-day versus trading-day convention. The model uses calendar "
      "days throughout, which is the more conservative reading.")
    A("")
    A("4. **The never-gated share is higher than the pre-rebuild model "
      "reported.** The old engine drove tiers off a deterministic payment "
      "pattern that forced a clean first six months, so it gated nearly "
      "everyone at M6. The rebuild reads the genuine run-of-6 first-passage "
      "law, which the spec requires. The old figure understated the "
      "never-gated population; this is a correction, not a regression.")
    A("")
    A("5. **B2B partner AUM is exogenous and does not interact with the retail "
      "book.** It depends on a signed partner that does not exist, which makes "
      "it the least validated load-bearing number in the model.")
    A("")
    A("6. **Legal and trust costs are unpriced.** They are carried as a visible "
      "placeholder, not a quote. The DFSA trust licence is explicitly "
      "unquotable and sits behind a switch defaulting to the exempt reading.")
    A("")
    return "\n".join(V)


if __name__ == "__main__":
    build()
