"""
Every input to the AURX liquidity audit, with where it comes from.

Nothing here is a client figure unless it says so. Change a value, rerun
run.py, and every table and chart follows.
"""

# Price of one AURX. 1 AURX = 1 gram, so this is the gold price per gram.
# The Phase 4/5 figure (5-simulations/aurumix/config/config.py GOLD_PRICE_M1).
# Slippage does not depend on it; only token counts do.
GOLD_PRICE = 141.50

# Pool fee. Uniswap V2 is fixed at 0.30%; V3 is set to the same tier so the
# comparison measures pool shape, not a fee difference.
FEE = 0.003

# The plugin's V3 layout: two thirds of capital in a tight band around the
# gold price, one third full-range as a backstop.
V3_TIGHT_SHARE = 2 / 3
V3_RANGES = [0.05, 0.10]           # +/- band around the gold price

# Slippage ceilings, all-in (fee included). Tighter than the plugin's
# 2 / 5 / 10% because the customer's alternative is the primary door:
# entry fee 5% at launch (decision 9) on the way in, a zero-fee buyback at
# the fix on the way out (Annex 2 III.E.4).
SLIPPAGE_LEVELS = [0.005, 0.01, 0.02, 0.05]

# Pool sizes to test, total value locked (both sides) in USD. There is no
# token raise to derive one figure from, so the audit sweeps a range.
BUDGETS = [100_000, 250_000, 500_000, 1_000_000, 2_500_000]

# Trade sizes, USD. The plugin's grid plus four Aurumix sizes.
PLUGIN_TRADES = [1_000, 5_000, 10_000, 20_000, 50_000]
AURUMIX_TRADES = {
    75: "Target monthly SIP (USD 75)",
    2_000: "Top SIP ticket (USD 2,000)",
    round(100 * GOLD_PRICE): "100 g holder exiting",
    round(1_000 * GOLD_PRICE): "1 kg holder exiting",
}
TRADES = sorted(set(PLUGIN_TRADES) | set(AURUMIX_TRADES))

# Gold volatility, for how often the price leaves a V3 band. The Phase 5
# twin's figure (5-simulations/aurumix/src/mcmodel.py GOLD_VOL_ANNUAL).
GOLD_VOL_ANNUAL = 0.15
BREACH_HORIZONS_DAYS = [7, 30, 90]

# The service standard the recommended budget is sized to. Ours, not the
# client's: which trade sizes must clear, in either direction, inside which
# ceiling (plugin slippage definition). Sized on whichever side binds.
SERVICE_STANDARD = [
    (2_000, 0.005, "Any SIP-sized trade (up to USD 2,000) inside 0.5%"),
    (round(100 * GOLD_PRICE), 0.01, "A 100 g trade inside 1%"),
    (round(1_000 * GOLD_PRICE), 0.05, "A 1 kg trade inside 5%"),
]
SERVICE_STANDARD_HIGH = [
    (round(1_000 * GOLD_PRICE), 0.02, "A 1 kg trade inside 2%"),
]

# The primary door, for positioning.
ENTRY_FEE_LAUNCH = 0.05            # decision 9, top of the 2-5% range
BUYBACK_FEE = 0.0                  # VARA Annex 2 III.E.4: no fee on redemption
