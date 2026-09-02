"""
Stage 3: the solver layer. Produces the answers to Q1-Q6.

    python scripts/run_analysis.py

Writes outputs/analysis.json and prints the findings. Fixed seeds throughout.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from config import config as C
from src.detmodel import DetModel, load_params
from src.agentbook import run_book, make_ladder
from src.mcmodel import _match_triples

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT, exist_ok=True)
A = {}
p0 = load_params()
years = np.array(p0["grid"]["year"])


def annual(out, key, y):
    return float(np.asarray(out[key])[years == y].sum())


print("=" * 78)
print("STAGE 3 ANALYSIS")
print("=" * 78)

# ═════════════════════════════════════════════════════════════════════════════
# Q1a. THE PROFITABILITY THRESHOLD - no market ceiling involved
#
# Method: at the mature cost structure (Y5-Y7 average), how many paying
# customers cover the cost base? Revenue per paying customer and the
# scale-variable costs both come from the ported engine, so the threshold
# inherits its exact unit economics. Contingency swept 15/30/50%.
# ═════════════════════════════════════════════════════════════════════════════

det = DetModel()
det.run()
o = det.out

# STEADY-STATE method. At the threshold the book is flat: acquisition only
# replaces churn, so acquisition cost = N x annual churn x blended CAC - it is
# NOT a per-customer serving cost. Serving costs (COGS premium, ICS, card
# programme, KYC-on-replacement, redemption handling) scale with N; licences,
# vault minimum, insurance, audit and tech do not.

npay7 = o["paying"][-1]
rev_pc = annual(o, "revenue", 7) / npay7
rev_pc_ex = (annual(o, "revenue", 7) - annual(o, "s6", 7)) / npay7

fixed = float(sum(o["opex_parts"][k][years == 7].sum()
                  for k in ("vault", "vara", "dmcc", "insurance", "audit",
                            "tech_audit", "tech_maint")))
serve_y7 = (annual(o, "cogs", 7) + annual(o, "ics_cost", 7)
            + annual(o, "card_cost", 7)
            + float(o["opex_parts"]["kyc"][years == 7].sum())
            + float(o["opex_parts"]["redemption"][years == 7].sum()))
serve_pc = serve_y7 / npay7

churn_annual = 1 - (1 - p0["monthly_churn"]) ** 12
blended_cac = annual(o, "acq_cost", 7) / annual(o, "new", 7)
replace_pc = churn_annual * blended_cac        # per paying customer per year

# B2B is NOT per-customer revenue: it is a fixed block that scales with
# partners. So the fixed cost base is covered EITHER by N retail customers at
# their unit margin OR by K partners at AUM/partner x fee. Report both, never
# a blend - blending hides that the retail business may not stand alone.
b2b_per_partner = p0["partner_aum"] * p0["b2b_fee"]

# replacement CAC: blended (Y7 mix, India-agent heavy) vs UAE-marketing-only
cac_uae_only = p0["cac_uae_y7"]
A["q1_threshold"] = {}
for cont in (0.15, 0.30, 0.50):
    k = 1 + cont
    row = {}
    for tag, cac in (("blended_cac", blended_cac), ("uae_cac", cac_uae_only)):
        margin_ex = rev_pc_ex - k * (serve_pc + churn_annual * cac)
        row[tag] = {"margin_per_customer": float(margin_ex),
                    "paying_needed_ex_b2b": float(k * fixed / margin_ex)
                    if margin_ex > 0 else None}
    row["partners_to_cover_fixed_alone"] = float(k * fixed / b2b_per_partner)
    A["q1_threshold"][f"contingency_{int(cont*100)}"] = row

print(f"\nQ1a. PROFITABILITY THRESHOLD - steady state (acquisition replaces churn only)")
print(f"  retail revenue/payer ${rev_pc_ex:.0f} | serve ${serve_pc:.0f} | churn {churn_annual:.0%}/yr"
      f" | CAC blended ${blended_cac:.0f} / UAE-only ${cac_uae_only:.0f}")
print(f"  fixed cost base ${fixed:,.0f}/yr | one B2B partner = ${b2b_per_partner:,.0f}/yr")
for cont in (15, 30, 50):
    t = A["q1_threshold"][f"contingency_{cont}"]
    b = t["blended_cac"]["paying_needed_ex_b2b"]; u = t["uae_cac"]["paying_needed_ex_b2b"]
    bs = f"{b:,.0f}" if b else "unreachable"; us = f"{u:,.0f}" if u else "unreachable"
    print(f"  contingency {cont}%: RETAIL ALONE needs {bs} paying (blended CAC) / {us} (UAE CAC)"
          f"  |  OR {t['partners_to_cover_fixed_alone']:.1f} B2B partners cover fixed costs by themselves")
print(f"  (cross-check: O Gold runs 75,000 active users in the UAE alone)")

# ═════════════════════════════════════════════════════════════════════════════
# Q2. THE ICS LADDER - tier mix, cost matrix, envelope
# ═════════════════════════════════════════════════════════════════════════════

pool, panel, scale = run_book(seed=20270101, scale=2.0)
tm = panel[-1]["tier_mix"]
tiered = tm[1:].sum()
A["q2_tier_mix_m84"] = {n: float(tm[i] / tiered) for i, n in
                        enumerate(C.TIER_ORDER) if i > 0}
A["q2_gated_share_m84"] = panel[-1]["gated_share"]
print(f"\nQ2. TIER MIX at M84 (the thing the workbook cannot compute):")
for n, v in A["q2_tier_mix_m84"].items():
    print(f"  {n:10} {v:6.1%}")
print(f"  gated share of live book: {A['q2_gated_share_m84']:.1%}"
      f"  (workbook input: 55%)")

# the ladder envelope: ceiling x steepness, full breadth
A["q2_envelope"] = {}
base_np7 = annual(o, "net_profit", 7)
for ceiling in (1.0, 1.5, 2.0):
    for steep in ("convex", "linear", "concave"):
        lad = make_ladder(ceiling, steep)
        pl, pn, sc = run_book(seed=20270101, scale=4.0, ladder=lad)
        ics = float(pl.econ["cost_ics"].sum() * sc)
        rev = float((pl.econ["rev_entry"] + pl.econ["rev_card"]
                     + pl.econ["rev_family"]).sum() * sc)
        A["q2_envelope"][f"c{ceiling}_{steep}"] = {
            "ics_cost_cum": ics, "agent_rev_cum": rev,
            "giveback_share": ics / rev,
        }
print("\nQ2. LADDER ENVELOPE (cumulative 84-month ICS cost, % of agent revenue):")
for k, v in A["q2_envelope"].items():
    print(f"  {k:14} ICS {v['ics_cost_cum']:>12,.0f}  = {v['giveback_share']:5.1%} of revenue")

# ═════════════════════════════════════════════════════════════════════════════
# Q3. PROFIT CONCENTRATION - deciles, rho_quality, rail mix
# ═════════════════════════════════════════════════════════════════════════════

def decile_shares(pool):
    rev = (pool.econ["rev_entry"] + pool.econ["rev_card"]
           + pool.econ["rev_family"] - pool.econ["cost_ics"])
    order = np.argsort(pool.ticket_base, kind="stable")
    csum = rev[order].cumsum()
    total = csum[-1]
    cuts = (np.arange(1, 10) * pool.n // 10)
    shares = np.diff(np.concatenate([[0.0], csum[cuts - 1], [total]])) / total
    return shares

A["q3_decile_share"] = {}
for rho in (0.0, 0.2, 0.4, 0.6):
    pl, _, sc = run_book(seed=20270101, scale=4.0, rho_quality=rho)
    sh = decile_shares(pl)
    A["q3_decile_share"][f"rho_{rho}"] = sh.tolist()
    print(f"\nQ3. profit share by ticket decile (rho_quality={rho}):"
          f"  top decile {sh[-1]:.1%}, top three {sh[-3:].sum():.1%}, "
          f"bottom five {sh[:5].sum():.1%}")

A["q3_rail"] = {}
for pf in (0.0, 0.25, 0.50, 0.75):
    pl, pn, sc = run_book(seed=20270101, scale=4.0, prefunded_share=pf)
    A["q3_rail"][f"prefunded_{int(pf*100)}"] = {
        "gated_share_m84": pn[-1]["gated_share"],
        "paying_m84": float(pn[-1]["paying"]),
        "entry_rev_cum": float(pl.econ["rev_entry"].sum() * sc),
    }
print("\nQ3/Q6. RAIL MIX (prefunded share -> gate share, book size):")
for k, v in A["q3_rail"].items():
    print(f"  {k:14} gated {v['gated_share_m84']:5.1%}  paying M84 {v['paying_m84']:>9,.0f}"
          f"  entry rev {v['entry_rev_cum']:>12,.0f}")

# ═════════════════════════════════════════════════════════════════════════════
# Q3b. SPOT DOOR BREAK-EVEN CONVERSION
#
# A spot-only customer is worth (attach-free) 1.7 x ticket x fee + card economics
# per year. Acquiring one at CAC_spot only beats putting the same money into SIP
# acquisition if conversion to SIP exceeds the break-even below.
# ═════════════════════════════════════════════════════════════════════════════

sip_ltv_pc = rev_pc_ex - serve_pc        # net value of one paying SIP customer-yr
spot_val = {"UAE": 1.7 * 190 * 0.05 + 28, "India": 1.7 * 40 * 0.05 + 28}
A["q3_spot_breakeven"] = {}
for regn, cac in (("UAE", p0["cac_uae"]), ("India", p0["cac_india"])):
    v = spot_val[regn]
    # value of spot-only forever vs SIP value; conversion c makes them equal:
    # cac_spot payback = v + c * sip_value_stream. Break-even c where
    # spot CAC / value ratio matches SIP CAC / value ratio.
    sip_ratio = cac / max(sip_ltv_pc, 1e-9)
    be = max(0.0, (cac - v * sip_ratio) / max(sip_ltv_pc * sip_ratio, 1e-9)) \
        if sip_ltv_pc > 0 else None
    A["q3_spot_breakeven"][regn] = {
        "spot_only_value_yr": v, "cac": cac,
        "spot_payback_years_no_conversion": cac / v,
    }
print("\nQ3b. SPOT-ONLY CUSTOMER (with the card now open to them):")
for regn, d in A["q3_spot_breakeven"].items():
    print(f"  {regn:6} value ~${d['spot_only_value_yr']:.0f}/yr vs CAC ${d['cac']:.0f}"
          f" -> payback {d['spot_payback_years_no_conversion']:.1f} yrs on spot alone")

# ═════════════════════════════════════════════════════════════════════════════
# Q6. TORNADO - one-at-a-time p10/p90 through the ported engine
# ═════════════════════════════════════════════════════════════════════════════

triples = _match_triples(p0)
tornado = []
for key, (base, agg, con) in triples.items():
    lo, hi = (agg, con) if agg < con else (con, agg)
    res = {}
    for tag, val in (("lo", lo), ("hi", hi)):
        overrides = {key: val}
        if key == "persistency":
            overrides["monthly_churn"] = 1 - val ** (1 / 12)
        if key in ("partner_adopt", "partner_aum_user"):
            pu = p0["partner_users"]
            overrides["partner_aum"] = (pu * (val if key == "partner_adopt"
                                              else p0["partner_adopt"])
                                        * (p0["partner_aum_user"] if key == "partner_adopt"
                                           else val))
        e = DetModel(overrides=overrides); e.run()
        res[tag] = (annual(e.out, "net_profit", 7), float(e.out["peak_funding"][-1]))
    tornado.append({
        "param": key,
        "np7_swing": abs(res["hi"][0] - res["lo"][0]),
        "np7_lo": res["lo"][0], "np7_hi": res["hi"][0],
        "funding_swing": abs(res["hi"][1] - res["lo"][1]),
    })
tornado.sort(key=lambda d: -d["np7_swing"])
A["q6_tornado"] = tornado[:15]
print("\nQ6. TORNADO - Y7 net profit swing, scenario-range width per parameter:")
for t in tornado[:12]:
    print(f"  {t['param']:24} {t['np7_swing']:>12,.0f}   "
          f"[{t['np7_lo']:>12,.0f} .. {t['np7_hi']:>12,.0f}]")

# ═════════════════════════════════════════════════════════════════════════════
# STRESS SCENARIOS (blueprint Part 3)
# ═════════════════════════════════════════════════════════════════════════════

def run_stress(name, overrides=None, gold_shock=None, redemption_mult=1.0,
               revenue_delay=False):
    ov = dict(overrides or {})
    if redemption_mult != 1.0:
        ov["redemption_rate"] = p0["redemption_rate"] * redemption_mult
    e = DetModel(overrides=ov)
    if gold_shock:
        month0, size = gold_shock
        g = p0["gold_price_m1"] * (1 + p0["gold_appreciation"]) ** (years - 1)
        per = np.array(p0["grid"]["period"])
        g = np.where(per >= month0, g * (1 + size), g)
        e.p["_gold_grid"] = g.tolist()
    out = e.run()
    if revenue_delay:
        # 12 months unlicensed: revenue AND scale-driven spend shift right;
        # what continues is the standing cost of existing - fixed opex, the
        # one-off application, insurance, audit and the tech build. Marketing
        # does not run while there is nothing to sell.
        standing = sum(out["opex_parts"][k] for k in
                       ("vault", "vara", "dmcc", "insurance", "audit",
                        "tech_audit", "oneoff", "tech_build", "tech_maint"))
        delay_cost = float(standing[:12].sum()) * (1 + p0["contingency"])
        cum = out["cum_profit"] - delay_cost
        funding = np.maximum(0, -cum) + out["capital_tied"]
        return {"np7": annual(out, "net_profit", 7),
                "cum7": float(cum[-1]),
                "peak_funding": float(np.maximum.accumulate(funding)[-1]),
                "delay_cost_12mo": delay_cost}
    return {"np7": annual(out, "net_profit", 7),
            "cum7": float(out["cum_profit"][-1]),
            "peak_funding": float(out["peak_funding"][-1])}

A["stress"] = {
    "base": run_stress("base"),
    "s1_gold_crash_30": run_stress("crash", gold_shock=(24, -0.30)),
    "s2_redemption_run_x5": run_stress("run", redemption_mult=5.0),
    "s3_zero_b2b": run_stress("no_b2b", {"b2b_partners": [0] * 7}),
    "s4_adoption_failure": run_stress("adopt", {
        "persistency": 0.45, "monthly_churn": 1 - 0.45 ** (1 / 12),
        "cac_uae": 140, "cac_gulf": 125, "cac_india": 26,
        "ics_ever_share": 0.45}),
    "s5_regulatory_delay": run_stress("delay", revenue_delay=True),
    "s6_ticket_compression": run_stress("ticket", {
        "ticket_uae": 26.5, "ticket_gulf": 21, "ticket_india": 24}),
    "s7_combined_tail": run_stress("tail", {
        "b2b_partners": [0, 0, 1, 2, 3, 4, 5]},
        gold_shock=(24, -0.30), redemption_mult=5.0),
}
print("\nSTRESS SCENARIOS (Y7 net profit | cumulative at Y7 | peak funding):")
for k, v in A["stress"].items():
    print(f"  {k:24} {v['np7']:>12,.0f} | {v['cum7']:>12,.0f} | {v['peak_funding']:>12,.0f}")

with open(os.path.join(OUT, "analysis.json"), "w") as f:
    json.dump(A, f, indent=1, default=float)
print(f"\nwrote {os.path.join(OUT, 'analysis.json')}")
