"""
The tornado as paired Monte Carlos, one per assumption end.

    python scripts/run_tornado_mc.py [n_paths]

The single-seed tornado in run_analysis.py holds everything at base and runs
each assumption's two ends once on one shared seed. The pairing cancels most
noise, but a single paired path still carries enough of it that the ordering
of the smaller bars is approximate (client, 2026-09-08: upgrade at
finalization). Here each end is a full Monte Carlo: the assumption is pinned
at its conservative or aggressive end while every other assumption draws as
in the base Monte Carlo, both ends on shared seeds. The bar is the median
across seeds of the paired difference in year-seven net profit.

Derived-parameter handling matches run_analysis.py: pinning persistency also
pins the churn derived from it; pinning a partner component also pins
partner_aum, with the other component at base (the drawn value of the other
component cannot be reached from a static override, and holding it at base is
the tornado's own one-at-a-time convention).

Writes outputs/tornado_mc.json and replaces q6_tornado in outputs/analysis.json
so the chart and the document read the Monte Carlo bars. run_analysis.py
prefers tornado_mc.json when it exists, so a later analysis rerun does not
regress the bars to single runs.
"""

import json
import os
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import load_params
from src.mcmodel import run_path, _match_triples

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
SEED0 = 20270101
WORKERS = 10
CHUNK = 500

p0 = load_params()
TRIPLES = _match_triples(p0)


def pin(key, val):
    """The override set that pins one assumption at one end."""
    ov = {key: val}
    if key == "persistency":
        ov["monthly_churn"] = 1.0 - val ** (1.0 / 12.0)
    if key in ("partner_adopt", "partner_aum_user"):
        pu = p0["partner_users"]
        ov["partner_aum"] = (pu * (val if key == "partner_adopt"
                                   else p0["partner_adopt"])
                             * (p0["partner_aum_user"] if key == "partner_adopt"
                                else val))
    return ov


def run_chunk(task):
    """One (param, end, seed-chunk): a list of (np7, peak_funding) per seed."""
    key, tag, val, k0, k1 = task
    ov = pin(key, val)
    out = []
    for k in range(k0, k1):
        o, _ = run_path(SEED0 + k, extra_overrides=ov)
        out.append((float(o["net_profit"][o["year"] == 7].sum()),
                    float(o["peak_funding"][-1])))
    return key, tag, k0, out


def main():
    ends = {}
    for key, (base, agg, con) in TRIPLES.items():
        lo, hi = (agg, con) if agg < con else (con, agg)
        ends[key] = {"lo": lo, "hi": hi}
    print(f"{len(ends)} assumptions x 2 ends x {N} paths "
          f"= {len(ends) * 2 * N:,} runs")

    tasks = [(key, tag, val, k, min(k + CHUNK, N))
             for key, e in ends.items() for tag, val in e.items()
             for k in range(0, N, CHUNK)]
    res = {key: {"lo": [None] * N, "hi": [None] * N} for key in ends}
    with Pool(WORKERS) as pool:
        for done, (key, tag, k0, chunk) in enumerate(
                pool.imap_unordered(run_chunk, tasks), 1):
            res[key][tag][k0:k0 + len(chunk)] = chunk
            if done % 20 == 0 or done == len(tasks):
                print(f"  chunk {done}/{len(tasks)}")

    tornado = []
    for key in ends:
        lo = np.array(res[key]["lo"])   # (N, 2): np7, funding
        hi = np.array(res[key]["hi"])
        tornado.append({
            "param": key,
            "np7_swing": float(abs(np.median(hi[:, 0] - lo[:, 0]))),
            "np7_lo": float(np.median(lo[:, 0])),
            "np7_hi": float(np.median(hi[:, 0])),
            "funding_swing": float(abs(np.median(hi[:, 1] - lo[:, 1]))),
        })
    tornado.sort(key=lambda d: -d["np7_swing"])

    R = {"tornado": tornado,
         "_meta": dict(n_paths_per_end=N, seed=SEED0,
                       method="paired Monte Carlo per end on shared seeds; "
                              "bar = median paired difference in Y7 net profit")}
    with open(os.path.join(OUT, "tornado_mc.json"), "w") as f:
        json.dump(R, f, indent=1)
    print("\nwrote outputs/tornado_mc.json")

    # replace the single-run bars wherever the chart and the document read them
    ap = os.path.join(OUT, "analysis.json")
    with open(ap) as f:
        A = json.load(f)
    A["q6_tornado"] = tornado[:15]
    A["q6_tornado_method"] = R["_meta"]["method"] + f", {N} paths per end"
    with open(ap, "w") as f:
        json.dump(A, f, indent=1)
    print("updated q6_tornado in outputs/analysis.json")

    print("\nTOP 12, Y7 net profit swing:")
    for t in tornado[:12]:
        print(f"  {t['param']:24} {t['np7_swing']:>12,.0f}   "
              f"[{t['np7_lo']:>12,.0f} .. {t['np7_hi']:>12,.0f}]")


if __name__ == "__main__":
    main()
