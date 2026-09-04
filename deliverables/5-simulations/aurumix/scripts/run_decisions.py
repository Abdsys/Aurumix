"""
The two things a model owes a team that has not launched yet.

    python scripts/run_decisions.py

WHAT TO LEARN FIRST. The simulation knows which assumptions move the answer.
Ranking those swings against what it costs to actually find each one out turns
the sensitivity table into a spending plan for discovery. A team with a fixed
pre-launch budget should know which question to buy the answer to first, and
that is a more useful output right now than any single number in the results.

WHEN TO CHANGE YOUR MIND. A threshold is only actionable if you know the level
at which it fires. For each metric the team can observe early, this computes the
value at which the plan stops working, so the number arrives as a decision rule
rather than as a description.

The impact figures come from the model. The cost and timing of learning each one
is judgement, stated as such, because no simulation can tell you what a pilot
campaign costs to run.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import load_params
from src.twin import Twin
from scripts.run_conditions import (region_only, unit_economics, REGIONS,
                                    FIXED_C, FIXED_U, ADDRESSABLE_R, SCALE, SEED)

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
p0 = load_params()
K = 1.15


# ─────────────────────────────────────────────────────────────────────────────
# How each assumption could actually be found out. Judgement, not model output.
# "cost" is what it takes to buy the answer; "when" is how soon you would know.
# ─────────────────────────────────────────────────────────────────────────────
HOW_TO_LEARN = {
    "partner_adopt":     ("one signed partner, or a serious pilot with one", "low", "on signing"),
    "partner_aum_user":  ("same conversation as adoption", "low", "on signing"),
    "partner_users":     ("public, per candidate partner", "none", "now"),
    "b2b_fee":           ("a term sheet", "none", "on signing"),
    "ceiling_mult":      ("a paid test campaign measuring reach, not installs", "medium", "2-3 months"),
    "cac_uae":           ("a paid test campaign in one region", "medium", "6-8 weeks"),
    "cac_india":         ("a paid test campaign in one region", "medium", "6-8 weeks"),
    "cac_uae_y7":        ("only observable at scale; infer from the early curve", "high", "year 2+"),
    "cac_conv_coef":     ("only observable at scale; infer from the early curve", "high", "year 2+"),
    "facility_takeup":   ("card take-up among the first cohort", "none", "3 months after card launch"),
    "persistency":       ("month-6 and month-13 payment records", "none", "6-13 months"),
    "family_attach":     ("offer it to the first cohort", "none", "3 months"),
    "contingency":       ("actual costs against budget", "none", "6 months"),
    "vault_fee":         ("the vault contract itself", "none", "now"),
    "interchange":       ("the card scheme's own schedule", "none", "now"),
    "referral_rate":     ("first cohort's referral behaviour", "none", "6 months"),
    "spot_attach_india": ("first cohort's spot behaviour", "none", "3 months"),
    "atm_share_3":       ("card scheme data", "none", "now"),
    "atm_share_4":       ("card scheme data", "none", "now"),
}
COST_RANK = {"none": 0, "low": 1, "medium": 2, "high": 3}


def value_of_information():
    with open(os.path.join(OUT, "analysis.json")) as f:
        A = json.load(f)
    rows = []
    for d in A["q6_tornado"]:
        k = d["param"]
        how, cost, when = HOW_TO_LEARN.get(k, ("not identified", "unknown", "unknown"))
        rows.append(dict(param=k, swing=d["np7_swing"], how=how, cost=cost, when=when,
                         cost_rank=COST_RANK.get(cost, 9)))
    # cheap first, then by how much it moves the answer
    rows.sort(key=lambda r: (r["cost_rank"], -r["swing"]))
    return rows


def margin_at(region, mult):
    """Region-only margin per customer at a marketing-CAC multiplier."""
    ov = {f"cac_{region}": p0[f"cac_{region}"] * mult,
          f"cac_{region}_y7": p0[f"cac_{region}_y7"] * mult}
    share = p0[f"mkt_share_{region}"]
    ov["marketing_spend"] = [x * share for x in p0["marketing_spend"]]
    for q in REGIONS:
        ov[f"mkt_share_{q}"] = 1.0 if q == region else 0.0
        if q != region:
            ov[f"agents_{q}"] = [0] * 7
    o = Twin(scale=SCALE, seed=SEED, overrides=ov).run()
    u = unit_economics(o)
    if u is None:
        return None
    u["margin"] = u["rev"] - (u["v_cert"] + u["v_unc"] * K)
    u["new_y7"] = float(o["new"][o["year"] == 7].sum())
    return u


def cac_trigger(region):
    """
    What marketing cost per customer would this region need to stop losing money?

    Swept, not bisected. Pushing the multiplier to extremes makes marketing buy
    almost nobody, at which point cost-per-customer divides by a vanishing
    denominator and the arithmetic explodes. So the sweep stays inside a range
    where the region still functions, and reports honestly when the crossing is
    not inside it.

    Two regions answer differently in KIND, not just level. India's acquisition
    is agent-led: raising the marketing rate there simply means marketing buys
    fewer people while agents keep delivering at commission cost, so the realised
    blended cost falls toward the agent cost and the margin hardly moves. The
    number to watch in India is agent productivity, not a marketing rate.
    """
    MULTS = (0.25, 0.4, 0.55, 0.7, 0.85, 1.0, 1.3, 1.6, 2.0)
    pts = []
    for mu in MULTS:
        u = margin_at(region, mu)
        if u is None or u["new_y7"] < 500:      # region has stopped functioning
            continue
        pts.append((mu, u["margin"], u["cac"]))
    if not pts:
        return None
    base = next((p for p in pts if abs(p[0] - 1.0) < 1e-9), pts[len(pts) // 2])
    span = max(p[1] for p in pts) - min(p[1] for p in pts)

    if span < 3.0:
        return dict(kind="insensitive", base_margin=base[1], base_cac=base[2],
                    swing=span, points=pts)
    # walk from cheapest upward for the first crossing into loss
    cross = None
    for (m0, g0, c0), (m1, g1, c1) in zip(pts, pts[1:]):
        if g0 > 0 >= g1:
            w = g0 / (g0 - g1)
            cross = c0 + w * (c1 - c0)
            break
    if cross is None:
        kind = "always" if pts[0][1] > 0 and pts[-1][1] > 0 else "never"
        return dict(kind=kind, base_margin=base[1], base_cac=base[2], points=pts)
    return dict(kind="threshold", cac=cross, base_cac=base[2],
                base_margin=base[1], points=pts)


def pay_through_probe():
    """
    Does payment discipline work as a trigger? Measured: no.

    Revenue falls when customers skip months, but almost every cost is per
    CUSTOMER rather than per PAYMENT, and the customer is still there. So the
    margin barely moves and there is no level at which a decision flips. It is
    reported as a non-trigger, because offering a threshold that does not bind
    would be worse than offering none.
    """
    out = []
    for mult in (1.0, 0.9, 0.8, 0.7, 0.6):
        o = Twin(scale=SCALE, seed=SEED, overrides={"pay_prob_mult": mult}).run()
        yr = o["year"]; Y = yr == 7
        npay = o["paying"][-1]
        P_, AQ = o["opex_parts"], o["acq_parts"]
        rev = float((o["revenue"][Y].sum() - o["s6"][Y].sum()) / npay)
        vc = float((o["cogs"][Y].sum() + o["ics_cost"][Y].sum() + P_["kyc"][Y].sum()
                    + P_["redemption"][Y].sum() + P_["vault"][Y].sum()) / npay)
        vu = float(o["card_cost"][Y].sum() / npay)
        new = float(o["new"][Y].sum())
        churn = float(o["lapsed"][Y].sum() / o["paying"][Y][0])
        vc += churn * float(AQ["agent_comm"][Y].sum() + AQ["referral"][Y].sum()) / new
        vu += churn * float(AQ["marketing"][Y].sum()) / new
        out.append(dict(mult=mult,
                        pay_through=float(o["sip"][Y].sum() / npay / (p0["ticket_uae"] * 12)),
                        margin=rev - (vc + vu * K)))
    return out


def main():
    print("=" * 78)
    print("WHAT TO LEARN FIRST")
    print("=" * 78)
    voi = value_of_information()
    print(f"{'assumption':22} {'moves Y7 profit':>16} {'cost to learn':>14}  when / how")
    for r in voi[:14]:
        print(f"  {r['param']:20} {r['swing']:16,.0f} {r['cost']:>14}  {r['when']} - {r['how']}")

    print("\n" + "=" * 78)
    print("WHEN TO CHANGE YOUR MIND")
    print("=" * 78)
    trig = {}
    print("\nCost per acquired customer, per region:")
    for r in REGIONS:
        t = cac_trigger(r)
        if t is None:
            continue
        trig[f"cac_{r}"] = t
        if t["kind"] == "insensitive":
            print(f"  {r.upper():6} marketing cost is NOT the lever. Margin USD {t['base_margin']:+.2f},"
                  f" moving only USD {t['swing']:.2f}")
            print(f"         across a 4x change in the marketing rate: acquisition here is agent-led.")
        elif t["kind"] == "never":
            print(f"  {r.upper():6} loses money across the whole range tested. Margin USD "
                  f"{t['base_margin']:+.2f} today.")
        elif t["kind"] == "always":
            print(f"  {r.upper():6} profitable across the whole range tested. Margin USD "
                  f"{t['base_margin']:+.2f} today.")
        else:
            print(f"  {r.upper():6} break-even at USD {t['cac']:.2f}, today USD {t['base_cac']:.2f}"
                  f"  ->  needs a {1 - t['cac']/t['base_cac']:.0%} reduction")

    print("\nPayment discipline: tested as a trigger, and it is not one.")
    pt = pay_through_probe()
    trig["pay_through"] = pt
    for row in pt:
        print(f"  book pays in {row['pay_through']:5.1%} of months  ->  margin "
              f"USD {row['margin']:6.2f}")
    span = max(r["margin"] for r in pt) - min(r["margin"] for r in pt)
    print(f"  Margin moves USD {span:.2f} across that whole range. Costs are per customer,")
    print(f"  not per payment, so skipping months barely changes them.")

    R = {"value_of_information": voi, "triggers": trig}
    with open(os.path.join(OUT, "decisions.json"), "w") as f:
        json.dump(R, f, indent=1)
    print("\nwrote outputs/decisions.json")


if __name__ == "__main__":
    main()
