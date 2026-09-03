"""
Monte Carlo for a candidate configuration of the levers.

The base MC answers "what does the plan look like under uncertainty". This one
answers "what does a RECOMMENDED configuration look like under the same
uncertainty", so the two are comparable path for path: same seeds, same draws,
only the levers moved.

    python scripts/mc_config.py <tag> <ladder_ceiling> <steepness> <rail> <uae> <gulf> <india> [n]

Writes outputs/mc_<tag>.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.agentbook import make_ladder
from src.mcmodel import run_path

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")

tag = sys.argv[1]
ceiling, steep = float(sys.argv[2]), sys.argv[3]
rail = float(sys.argv[4])
uae, gulf, india = float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])
n = int(sys.argv[8]) if len(sys.argv) > 8 else 2000
scale = float(sys.argv[9]) if len(sys.argv) > 9 else 10.0

lad = make_ladder(ceiling, steep)
alloc = {"mkt_share_uae": uae, "mkt_share_gulf": gulf, "mkt_share_india": india}

peak, cum, np7, be, pay = [], [], [], [], []
for k in range(n):
    o, _ = run_path(20270101 + k, extra_overrides=alloc,
                    ladder=lad, prefunded_share=rail, scale=scale)
    peak.append(o["peak_funding"][-1])
    cum.append(o["cum_profit"][-1])
    np7.append(o["net_profit"][o["year"] == 7].sum())
    be.append(o["cum_profit"][-1] > 0)
    pay.append(o["paying"][-1])
    if (k + 1) % 250 == 0:
        print(f"  {k + 1}/{n}")

q = lambda v, x: float(np.quantile(v, x))
S = {
    "tag": tag, "n_paths": n, "scale": scale,
    "config": {"ladder_ceiling": ceiling, "steepness": steep, "rail": rail,
               "alloc": [uae, gulf, india]},
    "safe_raise": {f"p{int(x*100)}": q(peak, x) for x in (.5, .8, .9, .95)},
    "P_cum_breakeven_by_Y7": float(np.mean(be)),
    "net_profit_y7": {f"p{int(x*100)}": q(np7, x) for x in (.1, .5, .9)},
    "cum_profit_y7_p50": q(cum, .5),
    "paying_y7_p50": q(pay, .5),
}
with open(os.path.join(OUT, f"mc_{tag}.json"), "w") as f:
    json.dump(S, f, indent=1)
print(json.dumps(S, indent=1))
