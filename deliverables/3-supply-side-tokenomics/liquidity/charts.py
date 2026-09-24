"""
Charts for the AURX liquidity audit, drawn only from outputs/results.json.
Nothing here builds a pool, so a figure cannot disagree with the table
printed beside it. Tokenomics.net palette, styled as the Phase 5 charts.

Run: python charts.py
"""

import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

GOLD = "#B8956E"; DARK_GOLD = "#96734A"; LIGHT_GOLD = "#D4B896"
DARK = "#1A1714"; WARM = "#D4CFC8"; MED = "#9A9590"; CREAM = "#FAF8F5"
RED = "#A94442"; GREEN = "#4A7C59"; AMBER = "#C4813D"
BUDGET_COLORS = [LIGHT_GOLD, GOLD, DARK_GOLD, MED, DARK]
DESIGN_COLORS = {"V2": MED, "V3 ±10%": GOLD, "V3 ±5%": DARK}

HERE = Path(__file__).parent
R = json.loads((HERE / "outputs" / "results.json").read_text(encoding="utf-8"))
CH = HERE / "outputs" / "charts"
CH.mkdir(parents=True, exist_ok=True)

PAR = R["params"]
FEE = PAR["fee"] * 100
CEILINGS = [s * 100 for s in PAR["slippage_levels"]]
BUDGETS = PAR["budgets"]
AURUMIX = {int(k): v for k, v in PAR["aurumix_trades"].items()}


def style(ax, fig):
    ax.set_facecolor(CREAM)
    fig.patch.set_facecolor(CREAM)
    ax.grid(True, alpha=0.18, color=MED, linewidth=0.7)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(WARM)
    ax.tick_params(colors=DARK, labelsize=9)
    ax.xaxis.label.set_color(DARK)
    ax.yaxis.label.set_color(DARK)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(CH / name, dpi=160, facecolor=CREAM)
    plt.close(fig)
    print("  wrote", name)


def usd(x, _=None):
    if abs(x) >= 1e6:
        return f"${x/1e6:.1f}m".replace(".0m", "m")
    if abs(x) >= 1e3:
        return f"${x/1e3:.0f}k"
    return f"${x:.0f}"


def pct(x, _=None):
    return f"{x:g}%"


def ceiling_lines(ax, horizontal=True):
    for c in CEILINGS:
        if horizontal:
            ax.axhline(c, color=MED, lw=0.8, ls="--", zorder=1)
            ax.text(ax.get_xlim()[1], c, f" {c:g}% ceiling", va="center", ha="left",
                    fontsize=8, color=MED)


def impact_chart(design, name, budgets=BUDGETS):
    """Sell-side price impact plus fee against trade size, one line per budget.
    Impact + fee is the plugin's slippage measure, so the ceilings read off
    directly."""
    fig, ax = plt.subplots(figsize=(9, 5.2))
    style(ax, fig)
    for b, col in zip(budgets, BUDGET_COLORS):
        rows = [r for r in R[design]["curves"][str(b)] if r["sell_impact_pct"] is not None]
        x = [r["trade_usd"] for r in rows]
        y = [r["sell_impact_pct"] + FEE for r in rows]
        ax.plot(x, y, color=col, lw=2, marker="o", ms=3.5, label=f"{usd(b)} pool")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylim(0.3, 60)
    ax.set_xlim(60, 200_000)
    ax.xaxis.set_major_formatter(FuncFormatter(usd))
    ax.yaxis.set_major_formatter(FuncFormatter(pct))
    ax.set_yticks([0.3, 0.5, 1, 2, 5, 10, 20, 50])
    ax.set_xlabel("Size of sale (USD)")
    ax.set_ylabel("Slippage: price impact + 0.3% fee (log scale)")
    ceiling_lines(ax)
    for t, lab in AURUMIX.items():
        ax.axvline(t, color=WARM, lw=0.8, zorder=0)
        ax.text(t, 0.32, " " + lab.split(" (")[0], rotation=90, va="bottom", ha="right",
                fontsize=7.5, color=MED,
                bbox=dict(facecolor=CREAM, edgecolor="none", pad=0.5, alpha=0.85))
    ax.legend(loc="lower right", fontsize=8.5, frameon=False)
    save(fig, name)


def max_trade_chart(design, name):
    """Largest sale inside each ceiling, grouped by pool budget."""
    fig, ax = plt.subplots(figsize=(9, 5))
    style(ax, fig)
    n = len(BUDGETS)
    w = 0.8 / n
    x = np.arange(len(CEILINGS))
    for i, (b, col) in enumerate(zip(BUDGETS, BUDGET_COLORS)):
        vals = [next(r["max_sell_usd"] for r in R[design]["max_trade"]
                     if r["tvl"] == b and r["slippage_pct"] == c) for c in CEILINGS]
        bars = ax.bar(x + (i - (n - 1) / 2) * w, vals, w, color=col, label=f"{usd(b)} pool")
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, v * 1.08, usd(v), ha="center",
                    va="bottom", fontsize=6.5, color=DARK, rotation=90)
    ax.set_yscale("log")
    ax.set_ylim(50, 5e6 if design != "V2" else 3e5)
    ax.yaxis.set_major_formatter(FuncFormatter(usd))
    ax.set_xticks(x)
    ax.set_xticklabels([f"{c:g}% ceiling" for c in CEILINGS])
    ax.set_ylabel("Largest sale that fits (USD, log scale)")
    ax.legend(fontsize=8.5, frameon=False, ncol=5, loc="upper left")
    save(fig, name)


def required_chart(design, name):
    """The plugin's minimum-TVL chart: required pool size against ceiling,
    one line per trade size."""
    fig, ax = plt.subplots(figsize=(9, 5.4))
    style(ax, fig)
    trades = PAR["trades"]
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("brand", [LIGHT_GOLD, GOLD, DARK_GOLD, DARK])
    for i, t in enumerate(trades):
        rows = [r for r in R[design]["required_tvl"] if r["trade_usd"] == t]
        lab = f"{usd(t)} ({AURUMIX[t].split(' (')[0]})" if t in AURUMIX else usd(t)
        ax.plot([r["slippage_pct"] for r in rows], [r["binding"] for r in rows],
                marker="o", ms=4, lw=1.8, color=cmap(i / (len(trades) - 1)), label=lab)
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_xticks(CEILINGS)
    ax.xaxis.set_major_formatter(FuncFormatter(pct))
    ax.xaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))
    ax.yaxis.set_major_formatter(FuncFormatter(usd))
    ax.set_xlabel("Slippage ceiling")
    ax.set_ylabel("Pool size needed, both sides (USD, log scale)")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left", bbox_to_anchor=(1.01, 1))
    save(fig, name)


def coverage_chart(design, name):
    """Which trade sizes each budget supports, and at what ceiling."""
    trades = PAR["trades"]
    grid = np.zeros((len(trades), len(BUDGETS)))
    labels = [["" for _ in BUDGETS] for _ in trades]
    for i, t in enumerate(trades):
        rows = {r["slippage_pct"]: r["binding"] for r in R[design]["required_tvl"] if r["trade_usd"] == t}
        for j, b in enumerate(BUDGETS):
            met = [c for c in CEILINGS if rows[c] is not None and rows[c] <= b]
            if met:
                grid[i, j] = len(CEILINGS) - CEILINGS.index(min(met))
                labels[i][j] = f"≤{min(met):g}%"
            else:
                labels[i][j] = f">{CEILINGS[-1]:g}%"
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap([CREAM, "#EFE3D2", LIGHT_GOLD, GOLD, DARK_GOLD])
    fig, ax = plt.subplots(figsize=(8, 5.2))
    fig.patch.set_facecolor(CREAM)
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=4, aspect="auto")
    for i in range(len(trades)):
        for j in range(len(BUDGETS)):
            ax.text(j, i, labels[i][j], ha="center", va="center", fontsize=9,
                    color=CREAM if grid[i, j] >= 3 else DARK)
    ax.set_xticks(range(len(BUDGETS)))
    ax.set_xticklabels([f"{usd(b)} pool" for b in BUDGETS], fontsize=9)
    ax.set_yticks(range(len(trades)))
    ax.set_yticklabels([f"{usd(t)}" + (f"  {AURUMIX[t].split(' (')[0]}" if t in AURUMIX else "")
                        for t in trades], fontsize=8.5)
    ax.set_xlabel("Pool size, both sides")
    ax.set_ylabel("Size of sale")
    for s in ax.spines.values():
        s.set_visible(False)
    save(fig, name)


def profile_chart(name):
    """Where each design puts its liquidity, at the same USD 1m of capital."""
    fig, ax = plt.subplots(figsize=(9, 4.6))
    style(ax, fig)
    gp = PAR["gold_price"]
    for d, pts in R["liquidity_profile"]["designs"].items():
        x = [(p["price"] / gp - 1) * 100 for p in pts]
        y = [p["L"] for p in pts]
        v2 = R["liquidity_profile"]["designs"]["V2"][0]["L"]
        ax.step(x, [v / v2 for v in y], where="post", color=DESIGN_COLORS[d], lw=2.2, label=d)
    ax.set_yscale("log")
    ax.set_xlabel("AURX price against the gold price (%)")
    ax.set_ylabel("Depth, as a multiple of V2 (log scale)")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:+.0f}%"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}×"))
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    save(fig, name)


def v3_max_chart(name):
    """V3 capacity at USD 1m, both bands, against V2."""
    fig, ax = plt.subplots(figsize=(9, 5))
    style(ax, fig)
    designs = ["V2", "V3 ±10%", "V3 ±5%"]
    x = np.arange(len(CEILINGS))
    w = 0.26
    eff = R["efficiency"]
    for i, d in enumerate(designs):
        key = "V2_max_sell" if d == "V2" else f"{d}_max_sell"
        vals = [row[key] for row in eff]
        bars = ax.bar(x + (i - 1) * w, vals, w, color=DESIGN_COLORS[d], label=d)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, v * 1.1, usd(v), ha="center", va="bottom",
                    fontsize=7.5, color=DARK)
    ax.set_yscale("log")
    ax.set_ylim(200, 2e6)
    ax.yaxis.set_major_formatter(FuncFormatter(usd))
    ax.set_xticks(x)
    ax.set_xticklabels([f"{c:g}% ceiling" for c in CEILINGS])
    ax.set_ylabel("Largest sale that fits, USD 1m pool (log scale)")
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    save(fig, name)


def breach_chart(name):
    """How often gold leaves each band, first passage, at 15%/yr volatility."""
    fig, ax = plt.subplots(figsize=(8, 4.4))
    style(ax, fig)
    rows = R["breach"]
    days = sorted({r["days"] for r in rows})
    x = np.arange(len(days))
    w = 0.36
    for i, d in enumerate(["V3 ±10%", "V3 ±5%"]):
        vals = [next(r["prob_pct"] for r in rows if r["design"] == d and r["days"] == h) for h in days]
        bars = ax.bar(x + (i - 0.5) * w, vals, w, color=DESIGN_COLORS[d], label=d)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v:.0f}%", ha="center",
                    fontsize=9, color=DARK)
    ax.set_xticks(x)
    ax.set_xticklabels([f"Within {h} days" for h in days])
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(FuncFormatter(pct))
    ax.set_ylabel("Chance gold touches the band edge")
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    save(fig, name)


def compare_impact_chart(name, tvl=1_000_000):
    fig, ax = plt.subplots(figsize=(9, 5))
    style(ax, fig)
    for d in ["V2", "V3 ±10%", "V3 ±5%"]:
        rows = [r for r in R[d]["curves"][str(tvl)] if r["sell_impact_pct"] is not None]
        ax.plot([r["trade_usd"] for r in rows], [r["sell_impact_pct"] + FEE for r in rows],
                color=DESIGN_COLORS[d], lw=2.2, marker="o", ms=3.5, label=d)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(60, 200_000)
    ax.set_ylim(0.3, 60)
    ax.set_yticks([0.3, 0.5, 1, 2, 5, 10, 20, 50])
    ax.xaxis.set_major_formatter(FuncFormatter(usd))
    ax.yaxis.set_major_formatter(FuncFormatter(pct))
    ax.set_xlabel("Size of sale (USD)")
    ax.set_ylabel("Slippage: price impact + 0.3% fee (log scale)")
    ceiling_lines(ax)
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    save(fig, name)


def budget_chart(name):
    """Pool needed to meet the service standard, by design, split by side."""
    fig, ax = plt.subplots(figsize=(9, 4.6))
    style(ax, fig)
    # side-by-side, not stacked: a stacked bar on a log axis misstates the split
    rows = [r for r in R["budget"] if r["tier"] == "Recommended"]
    names = [r["design"] for r in rows]
    usdc = [r["usdc"] for r in rows]
    gold = [r["tvl"] - r["usdc"] for r in rows]
    y = np.arange(len(rows))
    h = 0.36
    ax.barh(y - h / 2, usdc, h, color=MED, label="USDC side")
    ax.barh(y + h / 2, gold, h, color=GOLD, label="AURX side (gold minted against the vault)")
    for yi, r, u, g in zip(y, rows, usdc, gold):
        ax.text(u * 1.05, yi - h / 2, usd(u), va="center", fontsize=8.5, color=DARK)
        ax.text(g * 1.05, yi + h / 2, f"{usd(g)}  ({r['gold_kg']:.2f} kg)", va="center",
                fontsize=8.5, color=DARK)
        ax.text(1.05e5, yi - 0.46, f"Total {usd(r['tvl'])}", fontsize=8.5, color=DARK,
                fontweight="bold", va="bottom")
    ax.set_xscale("log")
    ax.set_xlim(1e5, 1e8)
    ax.xaxis.set_major_formatter(FuncFormatter(usd))
    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.invert_yaxis()
    ax.set_xlabel("Pool size needed for the service standard (USD, log scale)")
    ax.legend(fontsize=8.5, frameon=False, loc="lower right")
    save(fig, name)


if __name__ == "__main__":
    impact_chart("V2", "01_v2_price_impact.png")
    max_trade_chart("V2", "02_v2_max_trade.png")
    required_chart("V2", "03_v2_required_tvl.png")
    coverage_chart("V2", "04_v2_coverage.png")
    profile_chart("05_v3_liquidity_profile.png")
    impact_chart("V3 ±10%", "06_v3_price_impact.png")
    v3_max_chart("07_v3_max_trade.png")
    coverage_chart("V3 ±10%", "08_v3_coverage.png")
    breach_chart("09_v3_band_breach.png")
    compare_impact_chart("10_cmp_price_impact.png")
    required_chart("V3 ±10%", "11_v3_required_tvl.png")
    budget_chart("12_cmp_budget.png")
