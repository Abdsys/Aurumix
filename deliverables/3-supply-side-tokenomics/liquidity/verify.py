"""
Checks the swap engine against closed forms before any figure is used.

1. V2 marginal-price trades match the plugin's formulas
   (max_trade_size_analysis.py: y(sqrt(1+pi)-1)/(1-f), x(sqrt(1/(1-pi))-1)/(1-f)).
2. V2 all-in slippage matches the direct constant-product closed form.
3. A V3 trade that stays inside its band matches a V2 pool on the
   band's virtual reserves.
4. Capacity is linear in capital.
5. The V3 builder hits its target TVL and splits capital as asked.

Run: python verify.py   (exits non-zero on any failure)
"""

import math
import sys

from amm import v2_pool, v3_pool, required_tvl, Position, Pool
from params import GOLD_PRICE, FEE, V3_TIGHT_SHARE

failures = []


def close(name, got, want, tol=1e-7):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got:,.6f} want {want:,.6f}")
    if not ok:
        failures.append(name)


P, f = GOLD_PRICE, FEE
pool = v2_pool(1_000_000, P, f)
aurx, usdc = pool.holdings()
x, y = aurx, usdc

# 1. plugin closed forms, marginal price move of pi
for pi in (0.005, 0.02, 0.05):
    buy_usdc = y * (math.sqrt(1 + pi) - 1) / (1 - f)
    _, p1 = pool.buy(buy_usdc)
    close(f"V2 buy moves price by {pi:.1%}", p1 / P - 1, pi)
    sell_tok = x * (math.sqrt(1 / (1 - pi)) - 1) / (1 - f)
    _, p1 = pool.sell(sell_tok)
    close(f"V2 sell moves price by {pi:.1%}", 1 - p1 / P, pi)

# 2. plugin max-trade and min-TVL formulas at each ceiling (pi = s - f)
for s in (0.005, 0.01, 0.02, 0.05):
    pi = s - f
    want_buy = y * (math.sqrt(1 + pi) - 1) / (1 - f)
    close(f"V2 max buy at {s:.1%} ceiling (plugin)", pool.max_trade(s, "buy"), want_buy, 1e-6)
    want_sell = x * (math.sqrt(1 / (1 - pi)) - 1) / (1 - f) * P
    close(f"V2 max sell at {s:.1%} ceiling (plugin)", pool.max_trade(s, "sell"), want_sell, 1e-6)
    want_tvl = 2 * (1 - f) * 10_000 / (math.sqrt(1 + pi) - 1)
    got_tvl = required_tvl(lambda t: v2_pool(t, P, f), 10_000, s, "buy")
    close(f"V2 min TVL for $10k buy at {s:.1%} (plugin)", got_tvl, want_tvl, 1e-6)

# 3. V3 inside the band equals V2 on virtual reserves
band = Position(P * 0.95, P * 1.05, 50_000.0)
v3 = Pool([band], P, f)
v2_virtual = Pool([Position(0.0, float("inf"), band.L)], P, f)
for usd in (1_000, 10_000):
    close(f"V3 in-band buy of ${usd:,} = V2 virtual", v3.buy(usd)[0], v2_virtual.buy(usd)[0])
    close(f"V3 in-band sell of ${usd:,} = V2 virtual", v3.sell(usd / P)[0], v2_virtual.sell(usd / P)[0])

# 4. linearity
a = v3_pool(1_000_000, P, f, 0.05, V3_TIGHT_SHARE).max_trade(0.01, "sell")
b = v3_pool(3_000_000, P, f, 0.05, V3_TIGHT_SHARE).max_trade(0.01, "sell")
close("capacity triples when capital triples", b / a, 3.0, 1e-6)

# 5. V3 builder
v3p = v3_pool(1_000_000, P, f, 0.05, V3_TIGHT_SHARE)
close("V3 builder TVL", v3p.tvl(), 1_000_000)
tight_tvl = Pool([v3p.positions[0]], P, f).tvl()
close("V3 tight share of capital", tight_tvl / 1_000_000, V3_TIGHT_SHARE)

print()
if failures:
    print(f"{len(failures)} FAILED: {failures}")
    sys.exit(1)
print("All checks pass.")
