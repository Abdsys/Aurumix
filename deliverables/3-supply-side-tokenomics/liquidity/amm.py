"""
Pool arithmetic for the AURX liquidity audit.

One swap engine serves both pool designs. A Uniswap V2 pool is a single
position spanning every price; a V3 pool is a set of positions, each live
only inside its own price range. Inside any stretch of price where the
active liquidity L is constant, both behave as a constant-product curve, so
one piecewise walker covers both. This is the plugin's arithmetic
(lib/tokenomics_audit/analyses/v2_* and v3_*) generalised so that a trade
may cross a range edge instead of being capped at it.

Conventions
-----------
- Price P is USDC per AURX. AURX is 1 gram, so P is the gold price per gram.
- Work in sqrt price s = sqrt(P), as Uniswap does.
- Fee f is taken from the input amount before it touches the curve.
- "Slippage ceiling" follows the plugin exactly: a ceiling s leaves s - f
  for price impact, and price impact is the move in the pool's marginal
  price (max_trade_size_analysis.py, liquidity_required_analysis.py).
  The plugin's V3 module lets the price move by the full s instead; that
  would flatter V3 against V2, so the V2 rule is applied to both here.
- The average fill against P0, fee included, is also reported ("all-in
  cost"). It is always gentler than the ceiling definition.

Everything is linear in liquidity: double the capital and every trade size
at a given slippage doubles. The audit leans on that to turn one unit-sized
pool into required-budget figures.
"""

import math
from dataclasses import dataclass
from typing import List, Tuple

INF = float("inf")


@dataclass
class Position:
    """A liquidity position live for pa <= P < pb, with liquidity L."""
    pa: float
    pb: float
    L: float

    @property
    def sa(self) -> float:
        return math.sqrt(self.pa)

    @property
    def sb(self) -> float:
        return math.sqrt(self.pb) if self.pb < INF else INF

    def amounts(self, p0: float) -> Tuple[float, float]:
        """(AURX, USDC) this position holds at price p0."""
        s = min(max(math.sqrt(p0), self.sa), self.sb)
        usdc = self.L * (s - self.sa)
        aurx = self.L * (1 / s - (1 / self.sb if self.sb < INF else 0.0))
        return aurx, usdc


class Pool:
    def __init__(self, positions: List[Position], p0: float, fee: float):
        self.positions = positions
        self.p0 = p0
        self.fee = fee
        edges = {0.0, INF}
        for pos in positions:
            edges.add(pos.sa)
            edges.add(pos.sb)
        self.edges = sorted(edges)

    # ---- capital -------------------------------------------------------
    def holdings(self) -> Tuple[float, float]:
        aurx = sum(p.amounts(self.p0)[0] for p in self.positions)
        usdc = sum(p.amounts(self.p0)[1] for p in self.positions)
        return aurx, usdc

    def tvl(self) -> float:
        aurx, usdc = self.holdings()
        return usdc + aurx * self.p0

    def scaled(self, factor: float) -> "Pool":
        return Pool([Position(p.pa, p.pb, p.L * factor) for p in self.positions],
                    self.p0, self.fee)

    # ---- liquidity profile --------------------------------------------
    def active_L(self, s: float, upward: bool) -> float:
        """Liquidity in force just above s (upward) or just below s."""
        total = 0.0
        for p in self.positions:
            if upward and p.sa <= s < p.sb:
                total += p.L
            if not upward and p.sa < s <= p.sb:
                total += p.L
        return total

    # ---- swaps ---------------------------------------------------------
    def buy(self, usdc_in: float) -> Tuple[float, float]:
        """Spend usdc_in on AURX. Returns (AURX out, final price).
        AURX out is None if the pool runs dry before the order fills."""
        remaining = usdc_in * (1 - self.fee)
        s = math.sqrt(self.p0)
        out = 0.0
        while remaining > 1e-12:
            L = self.active_L(s, upward=True)
            nxt = next(e for e in self.edges if e > s + 1e-15)
            if L <= 0:
                if nxt == INF:
                    return None, INF
                s = nxt
                continue
            ds_needed = remaining / L
            if nxt == INF or s + ds_needed <= nxt:
                s1 = s + ds_needed
                out += L * (1 / s - 1 / s1)
                remaining = 0.0
                s = s1
            else:
                out += L * (1 / s - 1 / nxt)
                remaining -= L * (nxt - s)
                s = nxt
        return out, s * s

    def sell(self, aurx_in: float) -> Tuple[float, float]:
        """Sell aurx_in for USDC. Returns (USDC out, final price).
        USDC out is None if the pool runs dry before the order fills."""
        remaining = aurx_in * (1 - self.fee)
        s = math.sqrt(self.p0)
        out = 0.0
        while remaining > 1e-15:
            L = self.active_L(s, upward=False)
            prv = max(e for e in self.edges if e < s - 1e-15)
            if L <= 0:
                if prv <= 0:
                    return None, 0.0
                s = prv
                continue
            # moving down: 1/s rises by remaining / L
            inv1 = 1 / s + remaining / L
            s1 = 1 / inv1
            if s1 >= prv:
                out += L * (s - s1)
                remaining = 0.0
                s = s1
            else:
                out += L * (s - prv)
                remaining -= L * (1 / prv - 1 / s)
                s = prv
        return out, s * s

    # ---- trade cost ----------------------------------------------------
    def buy_cost(self, usd: float) -> Tuple[float, float]:
        """(slippage, price impact) for a buy of `usd` USDC."""
        out, p1 = self.buy(usd)
        if out is None or out <= 0:
            return INF, INF
        avg = usd / out
        return avg / self.p0 - 1, p1 / self.p0 - 1

    def sell_cost(self, usd: float) -> Tuple[float, float]:
        """(slippage, price impact) for a sale of `usd` worth of AURX at P0."""
        aurx = usd / self.p0
        out, p1 = self.sell(aurx)
        if out is None or out <= 0:
            return INF, INF
        avg = out / aurx
        return 1 - avg / self.p0, 1 - p1 / self.p0

    def max_trade(self, slip: float, side: str) -> float:
        """Largest trade (USD) inside a slippage ceiling, plugin definition:
        the marginal price may move by at most slip - fee. Sell size is
        valued at P0, as the plugin does (max_sell_tokens * price)."""
        budget = slip - self.fee
        if budget <= 0:
            return 0.0
        cost = self.buy_cost if side == "buy" else self.sell_cost
        lo, hi = 0.0, self.tvl()
        while cost(hi)[1] <= budget:
            hi *= 2
            if hi > 1e15:
                return INF
        for _ in range(200):
            mid = (lo + hi) / 2
            if cost(mid)[1] <= budget:
                lo = mid
            else:
                hi = mid
        return lo


# ---- pool shapes, each built to a target TVL ---------------------------

def v2_pool(tvl: float, p0: float, fee: float) -> Pool:
    """Constant product across all prices: half USDC, half AURX by value."""
    L = (tvl / 2) / math.sqrt(p0)
    return Pool([Position(0.0, INF, L)], p0, fee)


def v3_pool(tvl: float, p0: float, fee: float, range_pct: float,
            tight_share: float) -> Pool:
    """The plugin's V3 shape: tight_share of capital in a +/- range_pct band
    around p0, the rest spread full-range as a backstop so the pool never
    runs dry when gold moves outside the band."""
    tight = Position(p0 * (1 - range_pct), p0 * (1 + range_pct), 1.0)
    full = Position(0.0, INF, 1.0)
    tight_tvl_per_L = Pool([tight], p0, fee).tvl()
    full_tvl_per_L = Pool([full], p0, fee).tvl()
    tight.L = tvl * tight_share / tight_tvl_per_L
    full.L = tvl * (1 - tight_share) / full_tvl_per_L
    return Pool([tight, full], p0, fee)


def required_tvl(builder, trade_usd: float, slip: float, side: str) -> float:
    """TVL needed for a trade of trade_usd to clear at or under slip.
    Uses linearity: capacity scales one-for-one with capital."""
    unit = builder(1_000_000.0)
    cap = unit.max_trade(slip, side)
    if cap <= 0:
        return INF
    return 1_000_000.0 * trade_usd / cap
