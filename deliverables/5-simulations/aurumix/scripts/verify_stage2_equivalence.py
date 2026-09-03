"""
Stage 2 equivalence: the deterministic port against the CALCULATED workbook.

Blueprint sec 4.1: with every stochastic input pinned to Base, reproduce
Aurumix_Revenue_Model_calculated.xlsx's 29-column output to within rounding.
Tested row by row across the grid, not just at Y7.

This proves the port is faithful. It is NOT a constraint on assumptions.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import openpyxl

from src.detmodel import DetModel, load_params

WB = os.path.normpath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "..", "..", "4-revenue-modeling", "tools",
    "Aurumix_Revenue_Model_calculated.xlsx"))

# Model-sheet row -> engine output key. The load-bearing series.
ROWS = {
    159: ("paying", "PAYING CUSTOMERS"),
    160: ("holders", "HOLDERS"),
    161: ("cum_ever", "Cumulative ever acquired"),
    162: ("new", "NEW CUSTOMERS"),
    163: ("cards", "ACTIVE CARDS"),
    164: ("grams_held", "GRAMS HELD"),
    165: ("grams_cust", "GRAMS UNDER CUSTODY"),
    166: ("grams_bought", "Grams purchased"),
    167: ("aum", "COLLATERAL-ELIGIBLE AUM"),
    168: ("tiered", "Reaches an ICS benefit tier"),
    169: ("sip", "SIP contributions"),
    170: ("spot", "Spot purchase volume"),
    171: ("card_spend", "Card spend"),
    189: ("s1a", "Stream 1a"),
    190: ("s1b", "Stream 1b"),
    191: ("s2", "Stream 2"),
    192: ("s3", "Stream 3"),
    193: ("s4", "Stream 4"),
    194: ("s5", "Stream 5"),
    195: ("redeem_ev", "Redemption events"),
    196: ("auths", "Card authorisations"),
    197: ("revenue", "TOTAL NET REVENUE"),
    206: ("float_grams", "FLOAT REQUIRED grams"),
    209: ("float_usd", "FLOAT REQUIRED USD"),
    214: ("prefund", "CARD SETTLEMENT PREFUNDING"),
    224: ("net_new_grams", "Net new grams"),
    228: ("cogs", "TOTAL COGS"),
    255: ("opex", "TOTAL OPEX"),
    267: ("ics_cost", "TOTAL ICS BENEFIT COSTS"),
    282: ("acq_cost", "TOTAL ACQUISITION COSTS"),
    298: ("card_cost", "TOTAL CARD PROGRAMME COSTS"),
    304: ("cost_total", "TOTAL COST BASE"),
    326: ("net_profit", "NET PROFIT"),
    329: ("cum_profit", "CUMULATIVE NET PROFIT"),
    341: ("funding", "Funding required to date"),
    342: ("peak_funding", "PEAK FUNDING NEED"),
}

REL_TOL = 5e-3   # 0.5% relative...
ABS_TOL = 2.0    # ...or USD/unit 2 absolute, whichever forgives


def main():
    wb = openpyxl.load_workbook(WB, data_only=True)
    m = wb["Model"]

    # RAW workbook parameters: this test proves the PORT is faithful, so the
    # deliberate departures in config/overrides.py are excluded on purpose.
    eng = DetModel(p=load_params(raw=True))
    eng.run()

    print("=" * 88)
    print("STAGE 2 EQUIVALENCE - deterministic port vs Aurumix_Revenue_Model_calculated.xlsx")
    print(f"{len(ROWS)} series x 29 periods, tol {REL_TOL:.1%} rel or {ABS_TOL} abs")
    print("=" * 88)

    n_pass = n_fail = 0
    for row, (key, label) in ROWS.items():
        excel = np.array([m.cell(row, c).value or 0.0 for c in range(3, 32)], dtype=float)
        ours = eng.out[key]
        diff = np.abs(ours - excel)
        rel = diff / np.maximum(np.abs(excel), 1e-9)
        bad = (diff > ABS_TOL) & (rel > REL_TOL)
        worst = int(np.argmax(np.where(bad, rel, 0)))
        if bad.any():
            n_fail += 1
            print(f"  [FAIL] R{row:<3} {label:34} {int(bad.sum())}/29 off; worst "
                  f"P{worst+1}: ours {ours[worst]:,.2f} vs excel {excel[worst]:,.2f} "
                  f"({rel[worst]:.2%})")
        else:
            n_pass += 1
            print(f"  [PASS] R{row:<3} {label:34} max rel {rel.max():.4%}")

    print("=" * 88)
    print(f"{n_pass}/{n_pass + n_fail} series match")
    print("=" * 88)
    sys.exit(0 if n_fail == 0 else 1)


if __name__ == "__main__":
    main()
