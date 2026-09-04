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

# company-wide fixed base, split the way the threshold splits it
FIXED_C = 108918.0 + 5518.0                      # VARA + DMCC, published schedules
FIXED_U = 120000.0 + 45000.0 + 25000.0 + 15000.0  # tech, insurance, audits
ADDRESSABLE_R = {"uae": p0["ceiling_uae"], "gulf": p0["ceiling_gulf"],
                 "india": p0["ceiling_india"]}


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

    # ── per-region unit economics ────────────────────────────────────────────
    print()
    print("=" * 78)
    print("DOES ANY REGION CARRY ITSELF?")
    print("=" * 78)
    print(f"{'':8} {'rev/cust':>9} {'certain':>9} {'uncertain':>10} {'margin':>8} "
          f"{'CAC':>7} {'churn':>7} {'needed':>12} {'builds':>9}")
    regions = {}
    for r in REGIONS:
        u = unit_economics(region_only(r))
        if u is None:
            continue
        marg = u["rev"] - (u["v_cert"] + u["v_unc"] * 1.15)
        need = (FIXED_C + FIXED_U * 1.15) / marg if marg > 0 else None
        if need is not None and need > ADDRESSABLE_R[r]:
            need = None
        u["margin"] = marg
        u["needed"] = need
        u["own_ceiling"] = ADDRESSABLE_R[r]
        regions[r] = u
        ns = f"{need:,.0f}" if need else "beyond region"
        print(f"  {r.upper():6} {u['rev']:9.2f} {u['v_cert']:9.2f} {u['v_unc']:10.2f} "
              f"{marg:8.2f} {u['cac']:7.2f} {u['churn']:7.1%} {ns:>12} {u['paying']:9,.0f}")
    print()
    print("  'needed' is customers in that region alone to cover the WHOLE company's")
    print("  fixed base; 'builds' is what the plan's budget share actually reaches there.")

    R = {"regions": regions,
         "cac_mult": CAC_MULT.tolist(), "partners": PARTNERS,
         "cum_profit": grid.tolist(), "peak_funding": peak.tolist(),
         "frontier_partners_needed": front,
         "cac_band": {"lo_mult": float(CAC_LO), "hi_mult": float(CAC_HI),
                      "base": CAC_BASE},
         "plan_position": {"cac_mult": 1.0, "partners": int(p0["b2b_partners"][-1])}}
    with open(os.path.join(OUT, "conditions.json"), "w") as f:
        json.dump(R, f, indent=1)
    print(f"\nwrote outputs/conditions.json")


# ═════════════════════════════════════════════════════════════════════════════
# PER-REGION UNIT ECONOMICS
#
# The blended CAC of about USD 44 is a weighted average of roughly USD 85 in the
# UAE and USD 15 in India. It describes no actual customer, and it hides the
# most useful fact available: whether any region carries itself on its own.
#
# Method: run the twin once per region with the other two switched off, and with
# that region's marketing budget cut to its own share. Cutting the budget keeps
# SPEND INTENSITY identical to the blended run, so the channel-exhaustion curve
# bites exactly as it does in the full model. Without that, a single-region run
# would concentrate the whole budget in one market and invent a CAC penalty that
# the plan never incurs.
#
# The fixed base is company-wide, so "customers needed" here means: how many
# customers IN THIS REGION ALONE would cover the whole company's fixed costs.
# ═════════════════════════════════════════════════════════════════════════════

REGIONS = ("uae", "gulf", "india")


def region_only(r):
    ov = {}
    share = p0[f"mkt_share_{r}"]
    ov["marketing_spend"] = [x * share for x in p0["marketing_spend"]]
    for q in REGIONS:
        ov[f"mkt_share_{q}"] = 1.0 if q == r else 0.0
        if q != r:
            ov[f"agents_{q}"] = [0] * 7
    return Twin(scale=SCALE, seed=SEED, overrides=ov).run()


def unit_economics(o):
    """Same split as the threshold: certain and uncertain, per customer."""
    yr = o["year"]; Y = yr == 7
    npay = o["paying"][-1]
    if npay <= 0:
        return None
    P_, AQ = o["opex_parts"], o["acq_parts"]
    rev = float((o["revenue"][Y].sum() - o["s6"][Y].sum()) / npay)
    v_cert = float((o["cogs"][Y].sum() + o["ics_cost"][Y].sum()
                    + P_["kyc"][Y].sum() + P_["redemption"][Y].sum()
                    + P_["vault"][Y].sum()) / npay)
    v_unc = float(o["card_cost"][Y].sum() / npay)
    new = float(o["new"][Y].sum())
    churn = float(o["lapsed"][Y].sum() / o["paying"][Y][0])
    if new > 0:
        v_cert += churn * float(AQ["agent_comm"][Y].sum() + AQ["referral"][Y].sum()) / new
        v_unc += churn * float(AQ["marketing"][Y].sum()) / new
    cac = float(o["acq_cost"][Y].sum() / new) if new else float("nan")
    return dict(rev=rev, v_cert=v_cert, v_unc=v_unc, churn=churn, cac=cac,
                paying=float(npay), built=float(o["cum_ever"][-1]))


if __name__ == "__main__":
    main()
