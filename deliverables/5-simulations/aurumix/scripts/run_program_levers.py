"""
The four customer-behaviour programs, measured with explicit magnitudes.

    python scripts/run_program_levers.py [n_paths]

Part 4's program table published values whose measured magnitudes were never
recorded (client caught it, 2026-09-08). This re-measures all four with the
change stated, so each ceiling reads "if the behaviour reaches X, worth up
to Y" instead of a bare number.

Each target is the AGGRESSIVE end of the behaviour's own researched band, so
the ceiling means "the value of reaching the optimistic end of the range".
Method: one common base side (plain draws, exactly the base Monte Carlo), one
side per lever with the behaviour fixed at its target, all on shared seeds.
The value is the median across seeds of the paired difference in cumulative
seven-year profit.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.mcmodel import run_path

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
SEED0 = 20270101

P73_CHURN = 1.0 - 0.73 ** (1.0 / 12.0)

LEVERS = {
    # take-up of the gold-backed card, base 18%, aggressive 30%
    "card_activation": dict(ov={"facility_takeup": 0.30},
                            change="card take-up 18% to 30%"),
    # regional average tickets to their aggressive values (about +20%)
    "savings_amount": dict(ov={"ticket_uae": 41.0, "ticket_gulf": 32.0,
                               "ticket_india": 36.0},
                           change="average monthly saving up about 20%: UAE 33.60 to 41, Gulf 26 to 32, India 30 to 36"),
    # share of joiners on the set-and-forget prefunded rail, base 30%
    "automatic_payments": dict(kw={"prefunded_share": 0.75},
                               change="standing instruction share 30% to 75%"),
    # persistency at month 13, base 63%, aggressive 73%; churn re-derived
    "retention": dict(ov={"persistency": 0.73, "monthly_churn": P73_CHURN},
                      change="thirteen-month persistency 63% to 73%"),
}


def run_side(seed, spec):
    o, _ = run_path(seed, extra_overrides=spec.get("ov"), **spec.get("kw", {}))
    return float(o["cum_profit"][-1]), float(o["net_profit"][o["year"] == 7].sum())


def main():
    base = [run_side(SEED0 + k, {}) for k in range(N)]
    print(f"base side done, {N} paths")
    R = {"_meta": dict(n_paths=N, seed=SEED0,
                       method="median paired difference vs common base side")}
    for name, spec in LEVERS.items():
        d_cum, d_np7 = [], []
        for k in range(N):
            c, n7 = run_side(SEED0 + k, spec)
            d_cum.append(c - base[k][0])
            d_np7.append(n7 - base[k][1])
        R[name] = dict(change=spec["change"],
                       cum7_delta_p50=float(np.median(d_cum)),
                       np7_delta_p50=float(np.median(d_np7)))
        print(f"  {name:20} {spec['change']}")
        print(f"  {'':20} cum7 +{R[name]['cum7_delta_p50']:,.0f}  "
              f"np7 +{R[name]['np7_delta_p50']:,.0f}")
    with open(os.path.join(OUT, "program_levers.json"), "w") as f:
        json.dump(R, f, indent=1)
    print("\nwrote outputs/program_levers.json")


if __name__ == "__main__":
    main()
