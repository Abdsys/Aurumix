"""
AURX liquidity audit: compute every table, write outputs/results.json.
Charts are drawn separately by charts.py from that file, never by
re-running the pools.

Run: python verify.py && python run.py && python charts.py
"""

import json

import numpy as np
from pathlib import Path

from amm import v2_pool, v3_pool, required_tvl, Pool, INF
from params import (GOLD_PRICE, FEE, V3_TIGHT_SHARE, V3_RANGES,
                    SLIPPAGE_LEVELS, BUDGETS, TRADES, AURUMIX_TRADES,
                    ENTRY_FEE_LAUNCH, GOLD_VOL_ANNUAL, BREACH_HORIZONS_DAYS,
                    SERVICE_STANDARD, SERVICE_STANDARD_HIGH)

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

P, f = GOLD_PRICE, FEE


def designs(fee=f):
    """Pool builders by name, each taking a TVL."""
    d = {"V2": lambda t: v2_pool(t, P, fee)}
    for r in V3_RANGES:
        d[f"V3 ±{r:.0%}"] = (lambda rr: lambda t: v3_pool(t, P, fee, rr, V3_TIGHT_SHARE))(r)
    return d


def clean(x):
    return None if x == INF else round(x, 2)


def curve(pool, sizes):
    """Price impact and all-in cost across trade sizes, both sides."""
    rows = []
    for usd in sizes:
        s_slip, s_imp = pool.sell_cost(usd)
        b_slip, b_imp = pool.buy_cost(usd)
        rows.append({"trade_usd": usd,
                     "sell_impact_pct": clean(s_imp * 100), "sell_allin_pct": clean(s_slip * 100),
                     "buy_impact_pct": clean(b_imp * 100), "buy_allin_pct": clean(b_slip * 100)})
    return rows


def main():
    res = {"params": {"gold_price": P, "fee": f, "v3_tight_share": V3_TIGHT_SHARE,
                      "v3_ranges": V3_RANGES, "slippage_levels": SLIPPAGE_LEVELS,
                      "budgets": BUDGETS, "trades": TRADES,
                      "aurumix_trades": {str(k): v for k, v in AURUMIX_TRADES.items()},
                      "entry_fee_launch": ENTRY_FEE_LAUNCH}}
    curve_sizes = sorted(set(TRADES) | {250, 500, 2_500, 7_500, 30_000, 75_000, 100_000})

    for name, build in designs().items():
        d = {}
        # composition of each budget: the two sides the client has to fund
        d["composition"] = []
        for b in BUDGETS:
            pool = build(b)
            aurx, usdc = pool.holdings()
            d["composition"].append({"tvl": b, "usdc": round(usdc, 2), "aurx": round(aurx, 4),
                                     "aurx_usd": round(aurx * P, 2), "gold_kg": round(aurx / 1000, 3)})
        # price impact curve per budget
        d["curves"] = {str(b): curve(build(b), curve_sizes) for b in BUDGETS}
        # max trade per budget and ceiling
        d["max_trade"] = []
        for b in BUDGETS:
            pool = build(b)
            for s in SLIPPAGE_LEVELS:
                d["max_trade"].append({"tvl": b, "slippage_pct": s * 100,
                                       "max_buy_usd": clean(pool.max_trade(s, "buy")),
                                       "max_sell_usd": clean(pool.max_trade(s, "sell"))})
        # required TVL per trade and ceiling; the binding side is the larger
        d["required_tvl"] = []
        for t in TRADES:
            for s in SLIPPAGE_LEVELS:
                rb = required_tvl(build, t, s, "buy")
                rs = required_tvl(build, t, s, "sell")
                d["required_tvl"].append({"trade_usd": t, "slippage_pct": s * 100,
                                          "buy": clean(rb), "sell": clean(rs),
                                          "binding": clean(max(rb, rs))})
        res[name] = d

    # V3 liquidity profile against V2 at the same capital
    ref = 1_000_000
    res["liquidity_profile"] = {"tvl": ref, "designs": {}}
    for name, build in designs().items():
        pool = build(ref)
        pts = []
        for i in range(-150, 151):
            p = P * (1 + i / 1000)
            pts.append({"price": round(p, 4),
                        "L": round(pool.active_L(p ** 0.5, upward=True), 4)})
        res["liquidity_profile"]["designs"][name] = pts

    # capital efficiency: V3 capacity as a multiple of V2 at the same TVL
    res["efficiency"] = []
    for s in SLIPPAGE_LEVELS:
        v2cap = v2_pool(ref, P, f).max_trade(s, "sell")
        row = {"slippage_pct": s * 100, "V2_max_sell": round(v2cap, 2)}
        for r in V3_RANGES:
            cap = v3_pool(ref, P, f, r, V3_TIGHT_SHARE).max_trade(s, "sell")
            row[f"V3 ±{r:.0%}_max_sell"] = round(cap, 2)
            row[f"V3 ±{r:.0%}_multiple"] = round(cap / v2cap, 3)
        res["efficiency"].append(row)

    # fee-tier sensitivity: the 0.05% tier against the 0.30% used throughout
    res["fee_sensitivity"] = []
    for fee in (0.003, 0.0005):
        for name, build in designs(fee).items():
            for s in SLIPPAGE_LEVELS:
                res["fee_sensitivity"].append({
                    "fee_pct": fee * 100, "design": name, "slippage_pct": s * 100,
                    "max_sell_at_1m": round(build(ref).max_trade(s, "sell"), 2)})

    # V3 once gold has left the band: the pool price follows gold (arbitrage),
    # the band holds one asset only, and the full-range third carries the book
    res["out_of_band"] = []
    for r in V3_RANGES:
        base = v3_pool(ref, P, f, r, V3_TIGHT_SHARE)
        for move in (-(r + 0.01), r + 0.01):
            moved = Pool(base.positions, P * (1 + move), f)
            for s in SLIPPAGE_LEVELS:
                res["out_of_band"].append({
                    "design": f"V3 ±{r:.0%}", "gold_move_pct": round(move * 100, 1),
                    "slippage_pct": s * 100,
                    "max_sell_in_band": round(base.max_trade(s, "sell"), 2),
                    "max_sell_out_of_band": round(moved.max_trade(s, "sell"), 2)})

    # how often gold leaves each band: GBM at the twin's volatility, daily
    # steps, first passage (touching the edge counts, not only ending outside)
    rng = np.random.default_rng(20260924)
    n, days = 20_000, max(BREACH_HORIZONS_DAYS)
    sd = GOLD_VOL_ANNUAL / np.sqrt(365)
    logp = np.cumsum(rng.normal(-0.5 * sd * sd, sd, size=(n, days)), axis=1)
    res["breach"] = []
    for r in V3_RANGES:
        lo, hi = np.log(1 - r), np.log(1 + r)
        out = (logp <= lo) | (logp >= hi)
        for h in BREACH_HORIZONS_DAYS:
            res["breach"].append({"design": f"V3 ±{r:.0%}", "days": h,
                                  "prob_pct": round(out[:, :h].any(axis=1).mean() * 100, 1)})

    # the recommended budget: smallest TVL meeting every line of the standard
    res["budget"] = []
    for label, standard in (("Recommended", SERVICE_STANDARD), ("Comfortable", SERVICE_STANDARD_HIGH)):
        for name, build in designs().items():
            lines = []
            for t, s, text in standard:
                # sized on whichever side binds, as in the required-TVL tables
                need_t = max(required_tvl(build, t, s, "sell"), required_tvl(build, t, s, "buy"))
                lines.append({"text": text, "trade_usd": t, "slippage_pct": s * 100,
                              "required_tvl": clean(need_t)})
            need = max(l["required_tvl"] for l in lines)
            pool = build(need)
            aurx, usdc = pool.holdings()
            res["budget"].append({"tier": label, "design": name, "lines": lines,
                                  "tvl": round(need, 2), "usdc": round(usdc, 2),
                                  "aurx": round(aurx, 3), "gold_kg": round(aurx / 1000, 3)})

    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print_summary(res)


def fmt(x):
    if x is None:
        return "n/a"
    return f"${x/1e6:,.2f}m" if x >= 1e6 else f"${x/1e3:,.1f}k"


def print_summary(res):
    for name in designs():
        print(f"\n=== {name} ===")
        print("max sell by TVL / ceiling:")
        for b in BUDGETS:
            rows = [r for r in res[name]["max_trade"] if r["tvl"] == b]
            print(f"  {fmt(b):>9}: " + "  ".join(f"{r['slippage_pct']:.1f}%={fmt(r['max_sell_usd'])}" for r in rows))
        print("required TVL (binding side):")
        for t in TRADES:
            rows = [r for r in res[name]["required_tvl"] if r["trade_usd"] == t]
            print(f"  {fmt(t):>9}: " + "  ".join(f"{r['slippage_pct']:.1f}%={fmt(r['binding'])}" for r in rows))
    print("\nefficiency (max sell at $1m):")
    for r in res["efficiency"]:
        print("  ", r)
    print("\nfee sensitivity (max sell at $1m):")
    for r in res["fee_sensitivity"]:
        print("  ", r)


if __name__ == "__main__":
    main()
