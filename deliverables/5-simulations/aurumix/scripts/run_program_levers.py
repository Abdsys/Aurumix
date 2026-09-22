"""
All eight Part 4 levers, measured with explicit magnitudes.

    python scripts/run_program_levers.py [n_paths]

Part 4's tables published values whose measured magnitudes were never
recorded (client caught it, 2026-09-08). The four customer-behaviour programs
were re-measured that day; the four decision-and-work levers (marketing split,
ladder trim, three more partners, faster onboarding) still traced to the same
unrecorded run. This measures all eight identically, so every Part 4 number
has one recorded producer.

Method: one common base side (plain draws, exactly the base Monte Carlo), one
side per lever with the change applied, all on shared seeds. The value is the
median across seeds of the paired difference in cumulative seven-year profit.

Program targets are the AGGRESSIVE end of the behaviour's own researched band,
so each ceiling means "the value of reaching the optimistic end of the range".
Decision levers are the client-approved Part 4 changes as specified there.

Partner arrivals stay a stochastic draw in BOTH sides of every pair; the
three-more-partners lever raises the PLAN the arrivals are drawn around,
exactly as mc_config.py does. Onboarding is frozen at the managed target
(a managed target is not an unknown, so the drawn 12-24 band no longer
applies to it), again matching mc_config.py.
"""

import json
import os
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import load_params
from src.mcmodel import run_path

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
SEED0 = 20270101
WORKERS = 10
CHUNK = 250

P73_CHURN = 1.0 - 0.73 ** (1.0 / 12.0)

LEVERS = {
    # ── decisions Aurumix can take now ──────────────────────────────────────
    "marketing_split": dict(ov={"mkt_share_uae": 0.40, "mkt_share_gulf": 0.10,
                                "mkt_share_india": 0.50},
                            group="decision",
                            change="marketing budget UAE/Gulf/India 74/18/8 to 40/10/50"),
    "ladder_trim": dict(ladder_args=(1.5, "convex"),
                        group="decision",
                        change="loyalty ladder capped at 1.5pp, convex (top-loaded)"),
    # ── work worth doing ────────────────────────────────────────────────────
    "three_more_partners": dict(partners_extra=3,
                                group="work",
                                change="partner plan raised 11 to 14 by year seven, arrivals still stochastic"),
    "halve_onboarding": dict(ov={"partner_ramp_months": 9.0},
                             group="work",
                             change="partner onboarding fixed at 9 months instead of 18"),
    # ── programs worth funding up to a ceiling ──────────────────────────────
    # take-up of the gold-backed card, base 18%, aggressive 30%
    "card_activation": dict(ov={"facility_takeup": 0.30},
                            group="program",
                            change="card take-up 18% to 30%"),
    # regional average tickets to their aggressive values (about +20%)
    "savings_amount": dict(ov={"ticket_uae": 41.0, "ticket_gulf": 32.0,
                               "ticket_india": 36.0},
                           group="program",
                           change="average monthly saving up about 20%: UAE 33.60 to 41, Gulf 26 to 32, India 30 to 36"),
    # share of joiners on the set-and-forget prefunded rail, base 30%
    "automatic_payments": dict(kw={"prefunded_share": 0.75},
                               group="program",
                               change="standing instruction share 30% to 75%"),
    # persistency at month 13, base 63%, aggressive 73%; churn re-derived
    "retention": dict(ov={"persistency": 0.73, "monthly_churn": P73_CHURN},
                      group="program",
                      change="thirteen-month persistency 63% to 73%"),
}


def raised_plan(extra):
    """The plan with one extra signing in each of the last `extra` years."""
    p0 = load_params()
    sched = list(p0["b2b_partners"])
    for i in range(extra):
        yr = len(sched) - 1 - (i % min(extra, len(sched) - 1))
        for y in range(yr, len(sched)):
            sched[y] += 1
    return {**p0, "b2b_partners": sched}


def run_chunk(task):
    """One (side, seed-chunk): a list of (cum7, np7) per seed."""
    name, k0, k1 = task
    spec = LEVERS[name] if name != "_base" else {}
    kw = dict(spec.get("kw", {}))
    if "ladder_args" in spec:
        from src.agentbook import make_ladder
        kw["ladder"] = make_ladder(*spec["ladder_args"])
    params = raised_plan(spec["partners_extra"]) if "partners_extra" in spec else None
    out = []
    for k in range(k0, k1):
        o, _ = run_path(SEED0 + k, params=params,
                        extra_overrides=spec.get("ov"), **kw)
        out.append((float(o["cum_profit"][-1]),
                    float(o["net_profit"][o["year"] == 7].sum())))
    return name, k0, out


def main():
    sides = ["_base"] + list(LEVERS)
    tasks = [(s, k, min(k + CHUNK, N)) for s in sides for k in range(0, N, CHUNK)]
    res = {s: [None] * N for s in sides}
    with Pool(WORKERS) as pool:
        for done, (name, k0, chunk) in enumerate(
                pool.imap_unordered(run_chunk, tasks), 1):
            res[name][k0:k0 + len(chunk)] = chunk
            print(f"  chunk {done}/{len(tasks)} ({name} {k0})")

    base = res["_base"]
    R = {"_meta": dict(n_paths=N, seed=SEED0,
                       method="median paired difference vs common base side")}
    for name, spec in LEVERS.items():
        d_cum = [res[name][k][0] - base[k][0] for k in range(N)]
        d_np7 = [res[name][k][1] - base[k][1] for k in range(N)]
        R[name] = dict(group=spec["group"], change=spec["change"],
                       cum7_delta_p50=float(np.median(d_cum)),
                       np7_delta_p50=float(np.median(d_np7)))
        print(f"  {name:20} {spec['change']}")
        print(f"  {'':20} cum7 {R[name]['cum7_delta_p50']:+,.0f}  "
              f"np7 {R[name]['np7_delta_p50']:+,.0f}")
    with open(os.path.join(OUT, "program_levers.json"), "w") as f:
        json.dump(R, f, indent=1)
    print("\nwrote outputs/program_levers.json")


if __name__ == "__main__":
    main()
