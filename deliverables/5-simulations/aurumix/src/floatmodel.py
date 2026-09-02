"""
The float as an inventory system. UNHEDGED - Aurumix owns the metal and
absorbs the variance (client decision 2026-09-02).

Replaces the workbook's rule "1 bar + 10 days of average demand" with a
derived one: daily demand with payday clustering, an order-up-to policy with
dealer lead time and bar lots, safety stock from a service level, netting of
redemptions, sell-back of excess, daily mark-to-market on a gold path, and a
carry cost on float capital.

Everything runs at DAILY resolution inside each month of the 84-month horizon.
Inputs per month come from the ported engine: grams bought, grams redeemed.

Assumptions taken here, all swept:
  lead_days        2   dealer delivery T+2 for 100 g bars in Dubai   (1 / 3 / 5)
  service_level    0.99 no stock-out on 99% of days                   (0.95 / 0.99 / 0.999)
  carry_rate       0.06 per year on float capital                      (0.04 / 0.06 / 0.08)
  payday_share     0.60 of SIP volume lands in a 5-day payday window   (0.40 / 0.60 / 0.80)
  bar_grams        100  lot size, from the workbook
"""

import numpy as np

BAR = 100.0
DAYS = 30                     # model month


def daily_demand_profile(rng, month_grams_sip, month_grams_spot, payday_share=0.60):
    """
    Split a month's SIP grams into a payday cluster (days 1-5) and a flat
    remainder, and scatter spot grams as random arrivals. Returns a 30-day
    vector of grams demanded.
    """
    d = np.zeros(DAYS)
    cluster = month_grams_sip * payday_share
    rest = month_grams_sip - cluster
    d[:5] += cluster / 5.0
    d += rest / DAYS
    if month_grams_spot > 0:
        # spot arrives as ~1.7 events/yr per attacher; at book level it is a
        # Poisson scatter of lumps
        n_lumps = max(1, int(rng.poisson(20)))
        lumps = rng.dirichlet(np.ones(n_lumps)) * month_grams_spot
        days = rng.integers(0, DAYS, size=n_lumps)
        np.add.at(d, days, lumps)
    return d


def run_float(rng, grams_bought_m, grams_redeemed_m, gold_monthly,
              lead_days=2, service_level=0.99, carry_rate=0.06,
              payday_share=0.60, spot_share=0.075, buyback_spread=0.01,
              fab_premium=0.015, gold_vol=0.15):
    """
    Simulate the float day by day across the horizon.

    grams_bought_m, grams_redeemed_m : monthly vectors (len 84) from the engine
    gold_monthly                     : monthly gold path (len 84); a daily GBM
                                       is interpolated inside each month

    Policy: order-up-to S, reviewed daily. S = mean demand over lead time +
    z(service) x sd of demand over lead time, rounded UP to whole bars, floor 2
    bars. Orders arrive after lead_days. Redemptions refill the float; if the
    float exceeds S + 1 bar the excess is sold back at the spread.

    Returns per-month arrays and totals.
    """
    from scipy.stats import norm
    z = norm.ppf(service_level)
    T = len(grams_bought_m)

    # daily gold path: GBM steps inside each month, anchored to the monthly grid
    dt = 1.0 / 365.0
    on_hand = 2 * BAR
    pipeline = []               # (arrival_day_index, grams)
    day_idx = 0

    out = dict(float_end=np.zeros(T), float_avg=np.zeros(T), stockout_days=np.zeros(T),
               grams_ordered=np.zeros(T), grams_soldback=np.zeros(T),
               mtm_pnl=np.zeros(T), carry_cost=np.zeros(T), sellback_cost=np.zeros(T),
               premium_paid=np.zeros(T), unmet_grams=np.zeros(T), S_level=np.zeros(T))

    # demand history for the safety-stock estimate (rolling 90 days)
    hist = []

    for m in range(T):
        sip = grams_bought_m[m] * (1 - spot_share)
        spot = grams_bought_m[m] * spot_share
        dem = daily_demand_profile(rng, sip, spot, payday_share)
        red_daily = grams_redeemed_m[m] / DAYS

        # daily gold inside the month
        g0 = gold_monthly[m]
        g1 = gold_monthly[m + 1] if m + 1 < T else g0 * (1 + 0.081 / 12)
        drift = np.log(g1 / g0)
        steps = rng.normal(drift / DAYS - 0.5 * gold_vol**2 * dt, gold_vol * np.sqrt(dt), DAYS)
        steps += (drift - steps.sum()) / DAYS          # pin month-end to the grid
        gold_d = g0 * np.exp(np.cumsum(steps))

        stockouts = 0; ordered = 0.0; soldback = 0.0; unmet = 0.0
        mtm = 0.0; carry = 0.0; premium = 0.0; float_sum = 0.0

        for d in range(DAYS):
            # arrivals
            arriving = [g for (t, g) in pipeline if t == day_idx]
            pipeline = [(t, g) for (t, g) in pipeline if t != day_idx]
            on_hand += sum(arriving)

            # Order-up-to level, CALENDAR-AWARE. SIP demand is scheduled and
            # known ahead (payment requests are calendared), so the float is
            # sized to the KNOWN demand over the lead time plus a safety stock
            # for the UNSCHEDULED part only - spot lumps and arrears money.
            # A rolling-history rule reacts to the payday cluster after it
            # hits; this one is positioned before it.
            fwd = dem[d + 1: d + 1 + lead_days].sum()
            if d + 1 + lead_days > DAYS:            # look into next month's cluster
                fwd += dem[: (d + 1 + lead_days) - DAYS].sum()
            hist.append(dem[d]); hist = hist[-90:]
            spot_sd = np.std(hist) * spot_share if len(hist) > 5 else dem[d] * spot_share
            S = fwd + z * spot_sd * np.sqrt(max(lead_days, 1)) + BAR
            S = max(2 * BAR, np.ceil(S / BAR) * BAR)
            out["S_level"][m] = S

            # serve demand; redemptions refill
            on_hand += red_daily
            need = dem[d]
            if need > on_hand:
                unmet += need - on_hand
                stockouts += 1
                served = on_hand
            else:
                served = need
            on_hand -= served

            # reorder up to S (inventory position includes pipeline)
            position = on_hand + sum(g for (_, g) in pipeline)
            if position < S:
                qty = np.ceil((S - position) / BAR) * BAR
                pipeline.append((day_idx + lead_days, qty))
                ordered += qty
                premium += qty * gold_d[d] * fab_premium

            # sell back excess above S + 1 bar
            if on_hand > S + BAR:
                ex = on_hand - (S + BAR)
                on_hand -= ex
                soldback += ex
                # cost is the spread on the value sold

            # mark-to-market on what we hold; carry on its value
            if d > 0:
                mtm += on_hand * (gold_d[d] - gold_d[d - 1])
            carry += on_hand * gold_d[d] * carry_rate * dt
            float_sum += on_hand
            day_idx += 1

        out["float_end"][m] = on_hand
        out["float_avg"][m] = float_sum / DAYS
        out["stockout_days"][m] = stockouts
        out["grams_ordered"][m] = ordered
        out["grams_soldback"][m] = soldback
        out["sellback_cost"][m] = soldback * gold_d[-1] * buyback_spread
        out["mtm_pnl"][m] = mtm
        out["carry_cost"][m] = carry
        out["premium_paid"][m] = premium
        out["unmet_grams"][m] = unmet

    out["stockout_rate"] = float(out["stockout_days"].sum() / (T * DAYS))
    return out
