"""
What has to be true. The conditions map.

    python scripts/run_conditions.py

The rest of the analysis answers "what happens if the assumptions hold". With
almost nothing measured, that is the less useful question. This script answers
the one the engagement actually asked: what must be true for this business to
work, and how far is that from where the plan sits?

It is deliberately a SPECIFICATION, not a menu of scenarios. Every axis is
bounded by the Aggressive-to-Conservative band established in Phase 4 revenue
modelling - our own research, not figures anyone supplied - and the plan's
position is plotted on every map. A reader should come away knowing which
conditions they must hit, not which scenario they prefer.

Two axes survive the test of being both decision-relevant and genuinely unknown:

  cost per acquired customer   the largest lever on retail, and 92% of what it
                               costs to win one. Swept across the CAC band from
                               Phase 4.
  partners signed by year 7    the largest lever on the company, and the least
                               evidenced number in the engagement.

Everything else is either a decision (the ladder, the marketing split, the entry
fee, the rail) or already anchored (persistency). Decisions are priced as levers
elsewhere; they do not belong on an axis.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import load_params
from src.twin import Twin

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
SCALE = 10.0
SEED = 20270101

p0 = load_params()

# CAC axis bounded by the Phase 4 year-7 band, expressed as a multiplier on
# base so all three regions move together and stay comparable. The band is our
# estimate; nobody has measured what a customer costs to acquire here.
CAC_BASE = {"uae": p0["cac_uae_y7"], "gulf": p0["cac_gulf_y7"], "india": p0["cac_india_y7"]}
CAC_LO = p0["scenario_triples"]["Marketing CAC at Y7 - UAE"][1] / CAC_BASE["uae"]   # aggressive
CAC_HI = p0["scenario_triples"]["Marketing CAC at Y7 - UAE"][2] / CAC_BASE["uae"]   # conservative
CAC_MULT = np.round(np.linspace(CAC_LO, CAC_HI, 7), 3)
PARTNERS = [0, 2, 4, 6, 8, 11, 14]


def at(cac_mult, partners):
    """Run the twin with a CAC multiplier and a flat partner plan."""
    ov = {}
    for r in ("uae", "gulf", "india"):
        ov[f"cac_{r}"] = p0[f"cac_{r}"] * cac_mult
        ov[f"cac_{r}_y7"] = p0[f"cac_{r}_y7"] * cac_mult
    # partners arrive on the plan's shape, scaled to the target count
    shape = np.array(p0["b2b_partners"], dtype=float)
    ov["b2b_partners"] = (shape / shape[-1] * partners).round().tolist() if shape[-1] else [0] * 7
    o = Twin(scale=SCALE, seed=SEED, overrides=ov).run()
    return dict(cum=float(o["cum_profit"][-1]),
                peak=float(o["peak_funding"][-1]),
                np7=float(o["net_profit"][o["year"] == 7].sum()),
                paying=float(o["paying"][-1]))


def main():
    print("=" * 78)
    print("WHAT HAS TO BE TRUE")
    print("=" * 78)
    print(f"\nCAC axis: {CAC_LO:.2f}x to {CAC_HI:.2f}x base, the Phase 4 "
          f"Aggressive-to-Conservative band (our estimate, unmeasured)")
    print(f"  UAE {CAC_BASE['uae']*CAC_LO:.0f} to {CAC_BASE['uae']*CAC_HI:.0f}, "
          f"India {CAC_BASE['india']*CAC_LO:.0f} to {CAC_BASE['india']*CAC_HI:.0f} at year 7")
    print(f"Partner axis: {PARTNERS[0]} to {PARTNERS[-1]} by year 7 (the plan says 11)\n")

    grid = np.zeros((len(CAC_MULT), len(PARTNERS)))
    peak = np.zeros_like(grid)
    for i, cm in enumerate(CAC_MULT):
        for j, k in enumerate(PARTNERS):
            r = at(float(cm), k)
            grid[i, j] = r["cum"]
            peak[i, j] = r["peak"]
        print(f"  CAC {cm:.2f}x done")

    print(f"\nCUMULATIVE PROFIT AT YEAR 7, USD millions")
    print(f"{'CAC':>6} " + "".join(f"{k:>9}p" for k in PARTNERS))
    for i, cm in enumerate(CAC_MULT):
        row = "".join(f"{grid[i, j]/1e6:>10.2f}" for j in range(len(PARTNERS)))
        print(f"{cm:>5.2f}x {row}")

    # the frontier: fewest partners that clear, at each CAC
    print("\nTHE CONDITION, read off the map:")
    front = {}
    for i, cm in enumerate(CAC_MULT):
        ok = [PARTNERS[j] for j in range(len(PARTNERS)) if grid[i, j] > 0]
        front[f"{cm:.2f}"] = min(ok) if ok else None
        cacs = f"UAE {CAC_BASE['uae']*cm:.0f} / India {CAC_BASE['india']*cm:.0f}"
        print(f"  CAC {cm:.2f}x ({cacs:>24}): "
              + (f"needs {min(ok)} partners" if ok else "does not clear at any partner count tested"))

    R = {"cac_mult": CAC_MULT.tolist(), "partners": PARTNERS,
         "cum_profit": grid.tolist(), "peak_funding": peak.tolist(),
         "frontier_partners_needed": front,
         "cac_band": {"lo_mult": float(CAC_LO), "hi_mult": float(CAC_HI),
                      "base": CAC_BASE},
         "plan_position": {"cac_mult": 1.0, "partners": int(p0["b2b_partners"][-1])}}
    with open(os.path.join(OUT, "conditions.json"), "w") as f:
        json.dump(R, f, indent=1)
    print(f"\nwrote outputs/conditions.json")


if __name__ == "__main__":
    main()
