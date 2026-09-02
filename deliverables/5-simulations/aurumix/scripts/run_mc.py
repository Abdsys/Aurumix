"""
The Monte Carlo run: 2,000 paths over the ported engine.

Produces outputs/mc_results.csv (one row per path) and outputs/mc_summary.json.
Fixed seeds throughout - every figure is reproducible.

    python scripts/run_mc.py [n_paths]
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pandas as pd

from src.mcmodel import run_path
from src.creditrisk import margin_call_exceedance
from src.detmodel import load_params

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT, exist_ok=True)

N_PATHS = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
BASE_SEED = 20270101


def year_slice(months_col, year):
    return [i for i in range(29)]


def run_all(n_paths=N_PATHS):
    p0 = load_params()
    years = np.array(p0["grid"]["year"])
    rows = []
    called_by_month = np.zeros((n_paths, 84))

    for k in range(n_paths):
        out, eng = run_path(BASE_SEED + k)
        yr_rev = {y: out["revenue"][years == y].sum() for y in range(1, 8)}
        yr_np = {y: out["net_profit"][years == y].sum() for y in range(1, 8)}
        cum = out["cum_profit"]

        # margin calls on the monthly gold path; drawn originations spread from
        # the grid onto months (annual columns / 12)
        drawn_new = np.zeros(84)
        # approximate monthly origination: new cards x limit x drawn share
        cards_new_grid = np.zeros(29)
        for name in ("UAE", "Gulf", "India"):
            cards_new_grid += out["region"][name]["cards_new"]
        lim = np.divide(out["aum"], np.maximum(out["cards"], 1e-9)) * out["_draw"].get("ltv", p0["ltv"]) \
            if False else None
        # per-grid origination USD: new cards x credit limit per card x drawn%
        limit_per_card = np.divide(out["aum"], np.maximum(
            out["paying"] + out["holders"] * p0["sw_holders_keep_card"], 1e-9)) * p0["ltv"]
        orig_grid = cards_new_grid * limit_per_card * out["_draw"].get("drawn_pct", p0["drawn_pct"])
        gm = out.get("_gold_monthly")
        mi = 0
        for i in range(29):
            m = int(p0["grid"]["months"][i])
            for _ in range(m):
                if mi < 84:
                    drawn_new[mi] = orig_grid[i] / m
                    mi += 1
        mc = margin_call_exceedance(gm, drawn_new, struck_ltv=p0["ltv"])
        called_by_month[k] = mc["called_by_month"]

        rows.append({
            "path": k,
            "revenue_y7": yr_rev[7],
            "revenue_y7_ex_b2b": yr_rev[7] - out["s6"][years == 7].sum(),
            "net_profit_y7": yr_np[7],
            "cum_profit_y7": cum[-1],
            "peak_funding": out["peak_funding"][-1],
            "breakeven_year": next((y for y in range(1, 8)
                                    if cum[years == y][-1] > 0), 99),
            "paying_y7": out["paying"][-1],
            "holders_y7": out["holders"][-1],
            "ics_cost_y7": out["ics_cost"][years == 7].sum(),
            "gold_y7": out["gold_price"][-1],
            "b2b_partners_y7": out["_draw"]["b2b_partners"][-1]
                               if "b2b_partners" in out["_draw"] else p0["b2b_partners"][-1],
            "any_margin_call": mc["any_call"],
            "total_called_share": mc["total_called_share"],
            **{f"draw_{k2}": v for k2, v in out["_draw"].items()
               if isinstance(v, (int, float))},
        })
        if (k + 1) % 250 == 0:
            print(f"  {k + 1}/{n_paths} paths")

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT, "mc_results.csv"), index=False)

    q = lambda s, x: float(np.quantile(df[s], x))
    summary = {
        "n_paths": n_paths,
        "seed": BASE_SEED,
        "safe_raise": {f"p{int(x*100)}": q("peak_funding", x)
                       for x in (0.50, 0.80, 0.90, 0.95)},
        "P_peak_funding_gt_3m": float((df.peak_funding > 3e6).mean()),
        "P_cum_breakeven_by": {f"Y{y}": float((df.breakeven_year <= y).mean())
                               for y in range(4, 8)},
        "net_profit_y7": {f"p{int(x*100)}": q("net_profit_y7", x)
                          for x in (0.10, 0.50, 0.90)},
        "revenue_y7": {f"p{int(x*100)}": q("revenue_y7", x)
                       for x in (0.10, 0.50, 0.90)},
        "revenue_y7_ex_b2b_p50": q("revenue_y7_ex_b2b", 0.50),
        "P_any_margin_call": float(df.any_margin_call.mean()),
        "total_called_share_p95": q("total_called_share", 0.95),
        "paying_y7": {f"p{int(x*100)}": q("paying_y7", x)
                      for x in (0.10, 0.50, 0.90)},
    }
    with open(os.path.join(OUT, "mc_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    np.save(os.path.join(OUT, "called_by_month.npy"), called_by_month)

    print(json.dumps(summary, indent=1))
    return df, summary


if __name__ == "__main__":
    run_all()
