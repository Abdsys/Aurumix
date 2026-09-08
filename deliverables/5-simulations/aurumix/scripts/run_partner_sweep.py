"""
Partner dose-response as designed sweeps, not outcome buckets.

    python scripts/run_partner_sweep.py [n_paths]

The first partner-dependence chart binned the base Monte Carlo by how many
partners each path happened to end with. The middle buckets held 150+ runs and
were dependable; the ends held 15 and produced a fake dip at 20 partners that
the client spotted immediately (2026-09-08). Conditioning on an outcome is not
an experiment.

This is the experiment. For each partner count, the PLAN schedule is scaled to
reach that count by year seven, partner arrivals are FIXED to it (no stochastic
draw), and the full Monte Carlo runs on the same seeds as every other sweep.
Each point is the median of n_paths runs that differ from their neighbours in
exactly one respect: the partner count.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import load_params
from src.mcmodel import run_path

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
SEED0 = 20270101
COUNTS = [2, 5, 8, 11, 15, 20]

p0 = load_params()
plan = np.array(p0["b2b_partners"], dtype=float)   # [0, 1, 3, 5, 7, 9, 11]


def schedule(k):
    """The plan's ramp shape, scaled to reach k by year seven. Monotone."""
    s = np.round(plan * k / plan[-1]).astype(int)
    return np.maximum.accumulate(s).tolist()


def main():
    R = {"counts": COUNTS, "schedules": {}, "np7_p50": {}, "np7_p10": {},
         "np7_p90": {}, "cum7_p50": {}, "_meta": {"n_paths": N, "seed": SEED0}}
    for k in COUNTS:
        sched = schedule(k)
        R["schedules"][str(k)] = sched
        np7, cum = [], []
        for i in range(N):
            o, _ = run_path(SEED0 + i, extra_overrides={"b2b_partners": sched},
                            stochastic_partners_on=False)
            np7.append(float(o["net_profit"][o["year"] == 7].sum()))
            cum.append(float(o["cum_profit"][-1]))
        np7, cum = np.array(np7), np.array(cum)
        R["np7_p50"][str(k)] = float(np.median(np7))
        R["np7_p10"][str(k)] = float(np.quantile(np7, .1))
        R["np7_p90"][str(k)] = float(np.quantile(np7, .9))
        R["cum7_p50"][str(k)] = float(np.median(cum))
        print(f"  {k:2d} partners {sched}  NP7 p50 {R['np7_p50'][str(k)]:>12,.0f}")
    with open(os.path.join(OUT, "partner_sweep.json"), "w") as f:
        json.dump(R, f, indent=1)
    print("\nwrote outputs/partner_sweep.json")


if __name__ == "__main__":
    main()
