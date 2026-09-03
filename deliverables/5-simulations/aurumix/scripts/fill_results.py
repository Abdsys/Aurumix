"""
Render SIMULATION_RESULTS.md from its template and the run's own outputs.

    python scripts/fill_results.py

The results document quotes about sixty numbers. Typing them by hand once is
error-prone; typing them again after every re-run is how a document ends up
contradicting the model it describes, which has happened here before. So the
prose lives in SIMULATION_RESULTS.template.md with {{placeholders}}, and this
script fills them from mc_summary.json, mc_cfg15.json, analysis.json and
float_results.json.

A placeholder with no value is a hard error. A silently blank figure in a
client document is worse than a crash.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.dirname(HERE)
OUT = os.path.join(HERE, "outputs")


def j(name):
    with open(os.path.join(OUT, name)) as f:
        return json.load(f)


S = j("mc_summary.json")
C = j("mc_cfg15.json")
A = j("analysis.json")
try:
    F = j("float_results.json")
except FileNotFoundError:
    F = {}

t15 = A["q1_threshold"]["contingency_15"]
t30 = A["q1_threshold"]["contingency_30"]
t50 = A["q1_threshold"]["contingency_50"]
st = A["stress"]
tor = sorted(A["q6_tornado"], key=lambda d: -abs(d["np7_swing"]))


def m(v):
    """USD, millions with two decimals."""
    return f"{v/1e6:.2f}m"


def k(v):
    return f"{v/1e3:,.0f}k"


def n(v):
    return f"{v:,.0f}"


def pc(v, d=0):
    return f"{v*100:.{d}f}%"


def need(row):
    v = row["blended_cac"]["paying_needed_ex_b2b"]
    return n(v) if v and v > 0 else "unreachable"


V = {
    # scale of the run
    "PATHS": n(S["n_paths"]),
    "SCALE": f"{S.get('scale', 10):.0f}",
    "AGENTS": "one agent per customer" if S.get("scale", 10) == 1
              else f"one agent per {S.get('scale', 10):.0f} customers",

    # the raise, plan
    "RAISE50": m(S["safe_raise"]["p50"]),
    "RAISE80": m(S["safe_raise"]["p80"]),
    "RAISE90": m(S["safe_raise"]["p90"]),
    "RAISE95": m(S["safe_raise"]["p95"]),

    # the raise, recommended
    "R_RAISE50": m(C["safe_raise"]["p50"]),
    "R_RAISE90": m(C["safe_raise"]["p90"]),
    "R_RAISE95": m(C["safe_raise"]["p95"]),
    "RAISE_SAVED": m(S["safe_raise"]["p90"] - C["safe_raise"]["p90"]),

    # break-even
    "BE4": pc(S["P_cum_breakeven_by"]["Y4"]),
    "BE5": pc(S["P_cum_breakeven_by"]["Y5"]),
    "BE6": pc(S["P_cum_breakeven_by"]["Y6"]),
    "BE7": pc(S["P_cum_breakeven_by"]["Y7"]),
    "R_BE7": pc(C["P_cum_breakeven_by_Y7"]),

    # profit
    "NP10": m(S["net_profit_y7"]["p10"]),
    "NP50": m(S["net_profit_y7"]["p50"]),
    "NP90": m(S["net_profit_y7"]["p90"]),
    "R_NP10": m(C["net_profit_y7"]["p10"]),
    "R_NP50": m(C["net_profit_y7"]["p50"]),
    "R_NP90": m(C["net_profit_y7"]["p90"]),
    "R_CUM50": m(C["cum_profit_y7_p50"]),

    # book
    "PAY10": n(S["paying_y7"]["p10"]),
    "PAY50": n(S["paying_y7"]["p50"]),
    "PAY90": n(S["paying_y7"]["p90"]),
    "R_PAY50": n(C["paying_y7_p50"]),

    # revenue
    "REV50": m(S["revenue_y7"]["p50"]),
    "REV10": m(S["revenue_y7"]["p10"]),
    "REV90": m(S["revenue_y7"]["p90"]),
    "REV_EX_B2B": m(S["revenue_y7_ex_b2b_p50"]),
    "B2B_SHARE": pc(1 - S["revenue_y7_ex_b2b_p50"] / S["revenue_y7"]["p50"]),

    # thresholds
    "NEED15": need(t15),
    "NEED30": need(t30),
    "NEED50": need(t50),
    "MARGIN15": f"{t15['blended_cac']['margin_per_customer']:.2f}",
    "PARTNERS15": f"{t15['partners_to_cover_fixed_alone']:.1f}",
    "PARTNERS30": f"{t30['partners_to_cover_fixed_alone']:.1f}",
    "PARTNERS50": f"{t50['partners_to_cover_fixed_alone']:.1f}",

    # tiers
    "GATED": pc(A["q2_gated_share_m84"], 1),
    "T_SILVER": pc(A["q2_tier_mix_m84"]["silver"], 1),
    "T_GOLD": pc(A["q2_tier_mix_m84"]["gold"], 1),
    "T_PLAT": pc(A["q2_tier_mix_m84"]["platinum"], 1),
    "T_SOV": pc(A["q2_tier_mix_m84"]["sovereign"], 1),

    # stress
    "ST_BASE_CUM": m(st["base"]["cum7"]),
    "ST_BASE_NP": m(st["base"]["np7"]),
    "ST_BASE_PK": m(st["base"]["peak_funding"]),
    "ST_GOLD_CUM": m(st["s1_gold_crash_30"]["cum7"]),
    "ST_GOLD_PK": m(st["s1_gold_crash_30"]["peak_funding"]),
    "ST_RUN_CUM": m(st["s2_redemption_run_25pct_M24"]["cum7"]),
    "ST_RUN_PK": m(st["s2_redemption_run_25pct_M24"]["peak_funding"]),
    "ST_NOB2B_CUM": m(st["s3_zero_b2b"]["cum7"]),
    "ST_NOB2B_NP": m(st["s3_zero_b2b"]["np7"]),
    "ST_NOB2B_PK": m(st["s3_zero_b2b"]["peak_funding"]),
    "ST_ADOPT_CUM": m(st["s4_adoption_failure"]["cum7"]),
    "ST_ADOPT_PK": m(st["s4_adoption_failure"]["peak_funding"]),
    "ST_DELAY_CUM": m(st["s5_regulatory_delay"]["cum7"]),
    "ST_DELAY_PK": m(st["s5_regulatory_delay"]["peak_funding"]),
    "ST_TICKET_CUM": m(st["s6_ticket_compression"]["cum7"]),
    "ST_TICKET_PK": m(st["s6_ticket_compression"]["peak_funding"]),
    "ST_TAIL_CUM": m(st["s7_combined_tail"]["cum7"]),
    "ST_TAIL_NP": m(st["s7_combined_tail"]["np7"]),
    "ST_TAIL_PK": m(st["s7_combined_tail"]["peak_funding"]),

    # tornado, top five
    **{f"TOR{i+1}": tor[i]["param"].replace("_", " ") for i in range(5)},
    **{f"TOR{i+1}_SW": m(tor[i]["np7_swing"]) for i in range(5)},

    # margin calls
    "PMC": pc(S["P_any_margin_call"], 1),
    "P_GT3M": pc(S["P_peak_funding_gt_3m"], 0),
}

# concentration
dec = A["q3_decile_share"].get("rho_0.4") or list(A["q3_decile_share"].values())[0]
V["DEC_TOP"] = pc(dec[-1], 1)
V["DEC_TOP3"] = pc(sum(dec[-3:]), 1)
V["DEC_BOT5"] = pc(sum(dec[:5]), 1)

# rail
rail = A.get("q3_rail", {})
if "prefunded_0" in rail and "prefunded_75" in rail:
    V["RAIL0_GATE"] = pc(rail["prefunded_0"]["gated_share_m84"], 1)
    V["RAIL75_GATE"] = pc(rail["prefunded_75"]["gated_share_m84"], 1)
    V["RAIL0_PAY"] = n(rail["prefunded_0"]["paying_m84"])
    V["RAIL75_PAY"] = n(rail["prefunded_75"]["paying_m84"])

# ladder envelope: cheapest and dearest giveback as a share of revenue
env = A.get("q2_envelope", {})
if env:
    lo = min(env.items(), key=lambda kv: kv[1]["giveback_share"])
    hi = max(env.items(), key=lambda kv: kv[1]["giveback_share"])
    V["GIVE_LO"] = pc(lo[1]["giveback_share"], 1)
    V["GIVE_HI"] = pc(hi[1]["giveback_share"], 1)
    V["GIVE_LO_CFG"] = lo[0].replace("c", "ceiling ").replace("_", ", ")
    V["GIVE_HI_CFG"] = hi[0].replace("c", "ceiling ").replace("_", ", ")

# float
if F.get("mtm"):
    V["FLOAT_RAISE_WB"] = m(F["mtm"]["safe_raise_90_workbook_float"])
    V["FLOAT_RAISE_INV"] = m(F["mtm"]["safe_raise_90_inventory_float"])
    V["FLOAT_CARRY"] = k(F["mtm"]["carry_p50"])
    V["FLOAT_MTM_WORST"] = k(F["mtm"]["worst_year_p10"])


def main():
    tpl_path = os.path.join(DOCS, "SIMULATION_RESULTS.template.md")
    with open(tpl_path, encoding="utf-8") as f:
        tpl = f.read()

    missing = sorted(set(re.findall(r"\{\{(\w+)\}\}", tpl)) - set(V))
    if missing:
        print("MISSING VALUES for placeholders:", ", ".join(missing))
        sys.exit(1)

    out = re.sub(r"\{\{(\w+)\}\}", lambda mo: V[mo.group(1)], tpl)
    dest = os.path.join(DOCS, "SIMULATION_RESULTS.md")
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    unused = sorted(set(V) - set(re.findall(r"\{\{(\w+)\}\}", tpl)))
    print(f"wrote {dest}")
    print(f"  {len(V) - len(unused)} figures injected"
          + (f"; {len(unused)} available but unused" if unused else ""))


if __name__ == "__main__":
    main()
