"""
Float inventory model: verification, base run, sweeps, and the effect on the
raise number. Unhedged.

    python scripts/run_float.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import DetModel, load_params
from src.floatmodel import run_float, BAR
from src.mcmodel import run_path

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
p0 = load_params()
grid_m = np.array(p0["grid"]["months"], dtype=int)
R = {}


def to_monthly(v):
    """Spread the 29-grid onto 84 months (annual columns / 12)."""
    out = []
    for i, m in enumerate(grid_m):
        out.extend([v[i] / m] * m)
    return np.array(out[:84])


# ── A. verification ──────────────────────────────────────────────────────────
print("A. Float model verification")
rng = np.random.default_rng(1)
z = np.zeros(84)
f = run_float(rng, z, z, np.full(85, 141.5))
ok1 = abs(f["float_end"].mean() - 2 * BAR) < 1e-9 and f["stockout_rate"] == 0.0
print(f"  [{'PASS' if ok1 else 'FAIL'}] zero demand -> float sits at 2 bars, no stock-outs")

flat = np.full(84, 3000.0)
f = run_float(np.random.default_rng(2), flat, z, np.full(85, 141.5),
              payday_share=0.0, spot_share=0.0, service_level=0.99)
ok2 = f["stockout_rate"] < 0.02
print(f"  [{'PASS' if ok2 else 'FAIL'}] flat demand at 99% service -> stock-out rate {f['stockout_rate']:.2%} (<2%)")

f95 = run_float(np.random.default_rng(3), flat, z, np.full(85, 141.5), service_level=0.95)
f999 = run_float(np.random.default_rng(3), flat, z, np.full(85, 141.5), service_level=0.999)
ok3 = f999["float_avg"].mean() >= f95["float_avg"].mean()
print(f"  [{'PASS' if ok3 else 'FAIL'}] higher service level holds more float "
      f"({f95['float_avg'].mean():,.0f} g at 95% vs {f999['float_avg'].mean():,.0f} g at 99.9%)")

# ── B. base run on the engine's own flows, flat gold (no MTM) ────────────────
det = DetModel(); det.run()
bought = to_monthly(det.out["grams_bought"])
prev = np.concatenate([[0.0], det.out["grams_cust"][:-1]])
redeemed = to_monthly(np.maximum(0.0, prev + det.out["grams_bought"] - det.out["grams_cust"]))
gold_flat = np.concatenate([to_monthly(det.out["gold_price"]) * 0 + np.repeat(det.out["gold_price"], grid_m)[:84], [det.out["gold_price"][-1]]])

print("\nB. Base run - engine flows, deterministic gold")
f = run_float(np.random.default_rng(10), bought, redeemed, gold_flat, gold_vol=0.0)
wb_float_y7 = float(det.out["float_grams"][-1])
R["base"] = dict(float_avg_y7=float(f["float_avg"][-12:].mean()), float_end_m84=float(f["float_end"][-1]),
                 workbook_float_y7=wb_float_y7, stockout_rate=f["stockout_rate"],
                 carry_cost_cum=float(f["carry_cost"].sum()), sellback_cum=float(f["sellback_cost"].sum()),
                 S_level_y7=float(f["S_level"][-12:].mean()))
print(f"  workbook float at Y7      {wb_float_y7:8,.0f} g  (rule: 1 bar + 10 days avg demand)")
print(f"  inventory model, Y7 avg   {R['base']['float_avg_y7']:8,.0f} g  order-up-to {R['base']['S_level_y7']:,.0f} g  stock-out days {f['stockout_rate']:.2%}")
print(f"  carry cost cumulative     ${R['base']['carry_cost_cum']:10,.0f}   sell-back cum ${R['base']['sellback_cum']:,.0f}")

# ── C. sweeps ────────────────────────────────────────────────────────────────
print("\nC. Sweeps (Y7 average float grams | stock-out rate | cumulative carry)")
R["sweeps"] = {}
for lab, kw in [("lead 1d", dict(lead_days=1)), ("lead 3d", dict(lead_days=3)), ("lead 5d", dict(lead_days=5)),
                ("service 95%", dict(service_level=0.95)), ("service 99.9%", dict(service_level=0.999)),
                ("payday 40%", dict(payday_share=0.40)), ("payday 80%", dict(payday_share=0.80)),
                ("carry 4%", dict(carry_rate=0.04)), ("carry 8%", dict(carry_rate=0.08))]:
    f = run_float(np.random.default_rng(10), bought, redeemed, gold_flat, gold_vol=0.0, **kw)
    R["sweeps"][lab] = dict(float_avg_y7=float(f["float_avg"][-12:].mean()), stockout=f["stockout_rate"],
                            carry_cum=float(f["carry_cost"].sum()))
    print(f"  {lab:14} {R['sweeps'][lab]['float_avg_y7']:8,.0f} g | {f['stockout_rate']:6.2%} | ${R['sweeps'][lab]['carry_cum']:9,.0f}")

# ── D. unhedged mark-to-market across MC gold paths ──────────────────────────
print("\nD. Unhedged float across 400 Monte Carlo gold paths (mark-to-market P&L)")
N = 400
mtm_cum = []; mtm_worst_year = []; carry = []; peak = []; peak_wb = []
for k in range(N):
    out, eng = run_path(20270101 + k)
    b = to_monthly(out["grams_bought"])
    pv = np.concatenate([[0.0], out["grams_cust"][:-1]])
    r = to_monthly(np.maximum(0.0, pv + out["grams_bought"] - out["grams_cust"]))
    gm = np.concatenate([out["_gold_monthly"], [out["_gold_monthly"][-1]]])
    f = run_float(np.random.default_rng(500 + k), b, r, gm)
    yrs = np.repeat(np.arange(1, 8), 12)
    mtm_y = np.array([f["mtm_pnl"][yrs == y].sum() for y in range(1, 8)])
    mtm_cum.append(f["mtm_pnl"].sum()); mtm_worst_year.append(mtm_y.min()); carry.append(f["carry_cost"].sum())
    # raise: replace workbook float USD with inventory float, add carry + MTM to P&L
    float_usd_m = f["float_avg"] * out["_gold_monthly"] * (1 + p0["fab_premium"])
    float_usd_grid = np.array([float_usd_m[:24][i] if i < 24 else float_usd_m[24 + (i - 24) * 12: 24 + (i - 23) * 12].mean() for i in range(29)])
    extra_grid = np.array([(f["carry_cost"] - f["mtm_pnl"])[:24][i] if i < 24 else (f["carry_cost"] - f["mtm_pnl"])[24 + (i - 24) * 12: 24 + (i - 23) * 12].sum() for i in range(29)])
    cum = np.cumsum(out["net_profit"] - extra_grid)
    cap = float_usd_grid + (p0["capital_issuance_aed"] + p0["capital_activities_aed"]) / p0["aed_usd"] + out["prefund"]
    peak.append(np.maximum.accumulate(np.maximum(0, -cum) + cap)[-1]); peak_wb.append(out["peak_funding"][-1])
mtm_cum = np.array(mtm_cum); mtm_worst_year = np.array(mtm_worst_year); peak = np.array(peak); peak_wb = np.array(peak_wb)
R["mtm"] = dict(cum_p10=float(np.quantile(mtm_cum, .1)), cum_p50=float(np.quantile(mtm_cum, .5)), cum_p90=float(np.quantile(mtm_cum, .9)),
                worst_year_p10=float(np.quantile(mtm_worst_year, .1)), carry_p50=float(np.median(carry)),
                safe_raise_90_inventory_float=float(np.quantile(peak, .9)), safe_raise_90_workbook_float=float(np.quantile(peak_wb, .9)),
                safe_raise_50_inventory_float=float(np.quantile(peak, .5)))
print(f"  MTM P&L over 7 yrs: p10 ${R['mtm']['cum_p10']:,.0f} | p50 ${R['mtm']['cum_p50']:,.0f} | p90 ${R['mtm']['cum_p90']:,.0f}")
print(f"  worst single year (p10 across paths): ${R['mtm']['worst_year_p10']:,.0f}")
print(f"  carry cost cumulative, median: ${R['mtm']['carry_p50']:,.0f}")
print(f"  safe raise p90: workbook float ${R['mtm']['safe_raise_90_workbook_float']:,.0f} -> inventory float ${R['mtm']['safe_raise_90_inventory_float']:,.0f}")

json.dump(R, open(os.path.join(OUT, "float_results.json"), "w"), indent=1)
print("\nwrote outputs/float_results.json")
