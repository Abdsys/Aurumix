"""
Reconciliation: the twin against the Phase 4 revenue model.

This replaces the equivalence test, and it is a weaker guarantee on purpose.

The equivalence test proved that a Python port reproduced the client's
spreadsheet to within rounding. That was worth having while the port WAS the
simulation. It is meaningless now: the twin is not a port, it runs the business
on individual customers on a monthly clock, so of course it does not reproduce a
model built on one average customer across 29 columns.

What matters instead is that every difference is EXPLAINED. A twin that lands
near the approved numbers by accident is no better than one that lands far from
them. So this script prints the gap line by line and names the cause of each.

    python scripts/reconcile.py

Run it after any change to the twin. If a difference appears that is not in
EXPLANATIONS below, that is the finding: either the twin has a bug, or it has
learned something about the business that nobody has written down yet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from src.detmodel import DetModel, load_params
from src.twin import Twin

# Differences that are understood, with the reason. Anything outside the band
# given here is reported as unexplained.
EXPLANATIONS = {
    "paying": (0.05, 0.30,
               "the workbook applies ONE constant monthly churn rate forever, so a "
               "cohort decays to 4% by month 84. The twin runs five payment "
               "behaviours: the early lapsers leave in year one and the survivors "
               "are disproportionately disciplined, so a cohort settles near 23%. "
               "The mixture is the standard mover-stayer result and the constant "
               "rate is the thing that is wrong."),
    "cum_ever": (-0.15, 0.02,
                 "acquisition now responds to the book. Referrals come from who is "
                 "actually in it, cost per customer rises with spend, and the "
                 "market ceiling is uncertain rather than fixed."),
    "s1b": (-0.05, 0.20,
            "spot purchases are drawn per customer rather than applied as an "
            "average, so the share who buy and the amount they buy move together."),
    "s2": (-0.02, 0.25,
           "card spend is secured against each cardholder's OWN gold at their OWN "
           "tier's loan-to-value. Cardholders hold more gold than the book average "
           "and sit higher up the ladder, which an average cannot see."),
    "s3": (-0.10, 0.25,
           "family subscribers are individuals who can cancel the plan OR stop "
           "saving, and the twin tells those apart. The workbook bundles them into "
           "one constant rate, so the subscriber base decays the same way its "
           "customer base does. This line therefore inherits the mover-stayer "
           "effect from `paying` almost exactly: +17% here against +14% there."),
    "s4": (-0.18, 0.10,
           "card fees follow the actual cardholder population and its tier mix."),
    "s5": (-0.05, 0.25,
           "credit is written against real holdings, not an average limit."),
    "cogs": (-0.05, 0.25,
             "the fabrication premium is paid on grams actually bought net of "
             "grams actually redeemed, by customers whose holdings differ."),
    "opex": (-0.15, 0.10,
             "the vault bill is charged on the metal actually held, and "
             "redemption handling on events that actually happened."),
    "ics_cost": (-0.35, 0.10,
                 "the giveback is priced at the tier each customer reached, not as "
                 "one blended 25% on a flat 55% of the book. Three effects, in "
                 "opposite directions. The flat rate overstates: nobody has the "
                 "tenure for the top tiers early, so the workbook overpays for "
                 "years. Against that, two workbook errors understate: CARD "
                 "REWARDS multiply a percentage-of-SPEND rate by card REVENUE, "
                 "about twenty times too small, and the FX DISCOUNT is applied to "
                 "card fees that contain no FX margin. Net, the twin's giveback "
                 "runs about a fifth below the workbook's."),
    "redeem_ev": (-0.35, 0.10,
                  "redemptions are drawn per customer, and self-custody "
                  "withdrawals are counted separately rather than folded in."),
    "revenue": (-0.12, 0.15, "the sum of the above."),
    "cost_total": (-0.15, 0.10,
                   "the sum of the above, plus a change in how contingency is "
                   "applied. The workbook buffers the whole cost base by a flat "
                   "percentage. The twin buffers only the lines that can "
                   "surprise us - marketing yield, card programme, technology, "
                   "insurance, audits - and leaves contracted rates, published "
                   "licence fees and the loyalty ladder unbuffered, because "
                   "pricing doubt about a number nobody doubts is not prudence."),
    "net_profit": (-0.45, 0.35, "the sum of the above."),
    "peak_funding": (0.0, 0.45,
                     "THE ONE THAT MATTERS. Peak funding is the deepest point of a "
                     "cash line. On the workbook's grid the last sixty months are "
                     "five observations, so a trough between two year-ends is "
                     "invisible and the number can only be understated. The twin "
                     "measures all 84."),
    "s6": (-0.25, 0.02,
           "partners ramp: a signed partner's users adopt over 12 to 24 months, "
           "so late signers are below full power at year seven. The workbook "
           "starts every partner at full adoption on day one. Partner sizes also "
           "vary per world around the same mean."),
    "cards": (-0.15, 0.10, "card take-up is a per-customer draw, once each."),
    "grams_held": (-0.10, 0.20, "grams are the sum of what customers actually hold."),
    "card_cost": (-0.10, 0.20, "follows the card population and its spend."),
    "acq_cost": (-0.10, 0.10, "marketing is a budget; commission follows real revenue."),
}

ROWS = [("paying", True), ("cards", True), ("cum_ever", True), ("grams_held", True),
        ("s1a", False), ("s1b", False), ("s2", False), ("s3", False), ("s4", False),
        ("s5", False), ("s6", False), ("revenue", False), ("cogs", False),
        ("opex", False), ("ics_cost", False), ("acq_cost", False), ("card_cost", False),
        ("cost_total", False), ("net_profit", False), ("redeem_ev", False)]


def main():
    p = load_params()
    tw = Twin(scale=10.0, seed=20270101).run()
    # The baseline is the workbook's OWN logic: flat rates, one average customer,
    # its grid. tiermix=False is explicit because DetModel used to attach the
    # computed tier mix through a module that no longer exists, and its silent
    # fallback quietly changed this baseline once already.
    dm = DetModel(tiermix=False)
    dm.run()
    dyr = np.array(p["grid"]["year"])
    tyr = tw["year"]

    def agg(o, k, yrs, y, last):
        v = np.asarray(o[k])[yrs == y]
        return float(v[-1] if last else v.sum())

    print("=" * 92)
    print("RECONCILIATION - the twin against the Phase 4 revenue model, year 7")
    print("=" * 92)
    print(f"{'line':16} {'TWIN':>14} {'WORKBOOK':>14} {'diff':>9}   status")
    print("-" * 92)

    unexplained = []
    for key, last in ROWS:
        a = agg(tw, key, tyr, 7, last)
        b = agg(dm.out, key, dyr, 7, last)
        d = (a / b - 1.0) if b else 0.0
        band = EXPLANATIONS.get(key)
        if band is None:
            status = "matches" if abs(d) < 0.05 else "UNEXPLAINED"
            if abs(d) >= 0.05:
                unexplained.append((key, d, "no explanation on record"))
        else:
            lo, hi, _ = band
            ok = lo <= d <= hi
            status = "explained" if ok else "OUTSIDE THE EXPLAINED BAND"
            if not ok:
                unexplained.append((key, d, f"expected {lo:+.0%} to {hi:+.0%}"))
        print(f"{key:16} {a:14,.0f} {b:14,.0f} {d:8.1%}   {status}")

    # the funding line, which is the whole reason the grid had to go
    a, b = tw["peak_funding"][-1], dm.out["peak_funding"][-1]
    d = a / b - 1.0
    lo, hi, _ = EXPLANATIONS["peak_funding"]
    ok = lo <= d <= hi
    if not ok:
        unexplained.append(("peak_funding", d, f"expected {lo:+.0%} to {hi:+.0%}"))
    print("-" * 92)
    print(f"{'peak_funding':16} {a:14,.0f} {b:14,.0f} {d:8.1%}   "
          f"{'explained' if ok else 'OUTSIDE THE EXPLAINED BAND'}")
    tm = int(np.argmax(tw["funding"])) + 1
    print(f"\n  The twin's cash trough falls in MONTH {tm}. On the workbook's grid the "
          f"months around it\n  are inside one annual column, so the trough itself "
          f"could not be observed.")

    print("\n" + "=" * 92)
    print("WHY EACH LINE DIFFERS")
    print("=" * 92)
    for key, _ in ROWS + [("peak_funding", False)]:
        if key in EXPLANATIONS:
            print(f"\n  {key}")
            for line in _wrap(EXPLANATIONS[key][2], 84):
                print(f"    {line}")

    print("\n" + "=" * 92)
    if unexplained:
        print(f"{len(unexplained)} DIFFERENCE(S) NOT EXPLAINED:")
        for k, d, why in unexplained:
            print(f"   {k}: {d:+.1%}, {why}")
    else:
        print("Every difference is accounted for.")
    print("=" * 92)
    sys.exit(1 if unexplained else 0)


def _wrap(text, width):
    words, line, out = text.split(), "", []
    for w in words:
        if len(line) + len(w) + 1 > width:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        out.append(line)
    return out


if __name__ == "__main__":
    main()
