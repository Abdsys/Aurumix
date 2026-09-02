"""
The credit book under a moving gold price: margin calls by vintage.

Blueprint Q5. Liquidation risk is a property of WHEN a position was struck and
at what tier's LTV - not of the average LTV. So drawn balances are tracked as a
vintage matrix: origination month x outstanding balance, each vintage carrying
the gold price it was struck at.

Thresholds: the loan is struck at LTV_struck (50% flat in the workbook; the
tier ladder runs 50/65/80). A margin call fires when the CURRENT loan-to-value
- drawn / (collateral grams x current price) - breaches CALL_LTV. The
mechanism-design corpus flags warning/liquidation spacing as still open; the
client's own document works its example at 85%, which is used as the call line
and swept.
"""

import numpy as np

CALL_LTV = 0.85          # client doc sec 9.3 worked example; swept 0.75-0.95


def margin_call_exceedance(monthly_gold, drawn_new_by_month, struck_ltv,
                           repay_monthly=0.08, call_ltv=CALL_LTV):
    """
    Vintage-resolved margin-call test over an 84-month gold path.

    drawn_new_by_month : new drawn balance originated each month (USD), already
                         net of take-up and utilisation. Each vintage amortises
                         at repay_monthly (facility turnover expressed monthly).
    struck_ltv         : LTV at origination (scalar or per-month array).

    A vintage struck at price P0 with LTV L is called in month t when
        P_t / P0  <  L / call_ltv.
    Collateral grams are fixed at origination (the gold backing the draw), so
    the current LTV is L x (P0 / P_t).

    Returns dict with per-month called balance, the exceedance curve
    P(any call by month t), and the share of the book called at peak.
    """
    T = len(monthly_gold)
    struck = np.broadcast_to(np.asarray(struck_ltv, dtype=float), (T,))
    called = np.zeros(T)
    outstanding_total = np.zeros(T)

    # vintage matrix: origination month -> outstanding, struck price, struck LTV
    out = np.zeros(T)
    p0 = np.zeros(T)
    l0 = np.zeros(T)

    for t in range(T):
        # age existing vintages
        out *= (1.0 - repay_monthly)
        # originate
        out[t] = drawn_new_by_month[t]
        p0[t] = monthly_gold[t]
        l0[t] = struck[t]
        # test every live vintage against the current price
        live = out > 1e-9
        if live.any():
            ratio = monthly_gold[t] / p0[live]
            breach = ratio < (l0[live] / call_ltv)
            if breach.any():
                idx = np.where(live)[0][breach]
                called[t] += out[idx].sum()
                out[idx] = 0.0   # called positions are closed (forced sale)
        outstanding_total[t] = out.sum()

    total_originated = float(np.sum(drawn_new_by_month))
    return {
        "called_by_month": called,
        "outstanding": outstanding_total,
        "any_call": bool(called.sum() > 0),
        "peak_called_share": float(called.max() / max(outstanding_total.max(), 1e-9)),
        "total_called_share": float(called.sum() / max(total_originated, 1e-9)),
    }
