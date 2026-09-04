"""
Stress tests as Monte Carlos, not single runs.

    python scripts/run_stress_mc.py [n_paths]

The stress table used to report one deterministic run per scenario while the
rest of the document reported 2,000. Mixing the two invites a comparison that
does not hold: a single run of this model carries about USD 0.7m of noise in
cumulative profit, which is larger than several of the scenario effects it was
being used to measure.

So every scenario now runs the full Monte Carlo, at the same 2,000 paths as the
rest of the document, and every scenario shares the SAME SEEDS. That pairing
matters as much as the path count: scenario and base see identical parameter
draws, identical gold, identical customers, so any difference between them is
the scenario rather than luck.

ON RESOLUTION. These run at one agent per ten customers, while the headline runs
use one agent per customer. That is deliberate and it is nearly free: comparing
the two base runs on file, the p90 raise differs by 0.4% once 2,000 paths are
averaged. Sampling noise inside a path washes out; what does not wash out is
having too few paths. At full resolution this grid would take thirteen hours
instead of ninety minutes, and would buy a fourth decimal place nobody can use.
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
p0 = load_params()

# A run is a JUMP, not a rate: a rate-based outflow converges toward balance
# with inflows and can never overshoot. Contributions pause through a drop in
# payment odds, because a ticket below the USD 20 floor cannot exist.
PANIC = {"panic_period": 24, "panic_share": 0.25, "buyback_spread": 0.01,
         "panic_pay_mult": 0.4, "panic_months": 6,
         "spot_attach_mult": 0.4, "holder_redemption_mult": 2.8}

SCENARIOS = {
    "base": dict(),
    "s1_gold_crash_30": dict(gold_shock=(24, -0.30)),
    "s2_redemption_run_25pct_M24": dict(ov=PANIC),
    "s3_zero_b2b": dict(ov={"b2b_partners": [0] * 7}, no_partner_draw=True),
    "s4_adoption_failure": dict(ov={"persistency": 0.45,
                                    "cac_uae": 140, "cac_gulf": 125, "cac_india": 26}),
    "s5_regulatory_delay": dict(delay=True),
    "s6_ticket_compression": dict(ov={"ticket_uae": 26.5, "ticket_gulf": 21,
                                      "ticket_india": 24}),
    "s7_combined_tail": dict(ov={**PANIC, "b2b_partners": [0, 0, 1, 2, 3, 4, 5]},
                             gold_shock=(24, -0.30), no_partner_draw=True),
}


def one(seed, spec):
    out, _ = run_path(seed, extra_overrides=spec.get("ov"),
                      gold_shock=spec.get("gold_shock"),
                      stochastic_partners_on=not spec.get("no_partner_draw", False))
    cum = out["cum_profit"]
    peak = out["peak_funding"][-1]
    if spec.get("delay"):
        # Twelve months unlicensed. Revenue and growth spend shift right; what
        # keeps running is the cost of existing.
        standing = sum(out["opex_parts"][k] for k in
                       ("vault", "vara", "dmcc", "insurance", "audit",
                        "tech_audit", "oneoff", "launch_audit", "tech_build",
                        "tech_maint"))
        cost = float(standing[:12].sum()) * (1 + p0["contingency"])
        cum = cum - cost
        peak = float(np.maximum.accumulate(
            np.maximum(0, -cum) + out["capital_tied"])[-1])
    return float(cum[-1]), float(peak), float(out["net_profit"][out["year"] == 7].sum())


def main():
    print("=" * 84)
    print(f"STRESS SCENARIOS, {N} paths each, paired on identical seeds")
    print("=" * 84)
    R = {}
    for name, spec in SCENARIOS.items():
        cum, peak, np7 = [], [], []
        for k in range(N):
            c, p, n = one(SEED0 + k, spec)
            cum.append(c); peak.append(p); np7.append(n)
        cum, peak, np7 = map(np.array, (cum, peak, np7))
        R[name] = dict(cum7=float(np.median(cum)),
                       cum7_p10=float(np.quantile(cum, .1)),
                       cum7_p90=float(np.quantile(cum, .9)),
                       peak_funding=float(np.quantile(peak, .9)),
                       peak_funding_p50=float(np.median(peak)),
                       np7=float(np.median(np7)),
                       p_breakeven=float((cum > 0).mean()))
        print(f"  {name:30} cum {R[name]['cum7']:11,.0f}  raise p90 "
              f"{R[name]['peak_funding']:11,.0f}  break-even {R[name]['p_breakeven']:5.1%}")
    R["_meta"] = dict(n_paths=N, seed=SEED0, paired=True)
    with open(os.path.join(OUT, "stress_mc.json"), "w") as f:
        json.dump(R, f, indent=1)
    print(f"\nwrote outputs/stress_mc.json")


if __name__ == "__main__":
    main()
