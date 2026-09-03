"""
Charts for SIMULATION_RESULTS.md. Tokenomics.net brand palette, same style as
the Stockpile deliverable. One axis per chart, thin marks, recessive grid.

RETIRED PENDING REBUILD. Every chart here reads the two-engine build and its
29-column grid, both of which are gone. Running it would produce charts that
contradict the model, so it refuses instead. It gets rebuilt against the twin's
monthly output together with the results document, because the chart choices
follow that document's story.
"""

raise SystemExit(
    "visualize.py targets the retired two-engine build. It is rebuilt with the "
    "results document. See the module docstring.")

import json
import os

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.detmodel import DetModel, load_params
from src.mcmodel import run_path
from src.agentbook import run_book
from src.floatmodel import run_float
from config import config as C

GOLD = "#B8956E"; DARK = "#1A1714"; WARM = "#D4CFC8"; MED = "#9A9590"
LIGHT_GOLD = "#C4A77D"; DKGRAY = "#2D2D2D"; CREAM = "#FAF8F5"; RED = "#C44E52"
CAT = [GOLD, DARK, MED, LIGHT_GOLD, RED, DKGRAY]

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "outputs", "charts")
os.makedirs(OUT, exist_ok=True)
p0 = load_params()
YEARS = np.array(p0["grid"]["year"])
PER = np.array(p0["grid"]["period"])
XLAB = [f"M{i}" for i in range(1, 25)] + [f"Y{y}" for y in range(3, 8)]


def style(ax, fig):
    ax.set_facecolor(CREAM); fig.patch.set_facecolor(CREAM)
    ax.grid(True, alpha=0.2, color=MED)
    for s in ax.spines.values():
        s.set_color(WARM)
    ax.tick_params(colors=DARK)
    ax.xaxis.label.set_color(DARK); ax.yaxis.label.set_color(DARK); ax.title.set_color(DARK)


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)
    print("  wrote", name)


def usd(x, _=None):
    return f"${x/1e6:.1f}M" if abs(x) >= 1e6 else f"${x/1e3:.0f}k"


# ── gather Monte Carlo panels ────────────────────────────────────────────────
def mc_panels(n=1000):
    rev, rev_ex, cum, pay, peak, be = [], [], [], [], [], []
    for k in range(n):
        o, _ = run_path(20270101 + k)
        rev.append(o["revenue"]); rev_ex.append(o["revenue"] - o["s6"])
        cum.append(o["cum_profit"]); pay.append(o["paying"]); peak.append(o["peak_funding"][-1])
        be.append(next((y for y in range(1, 8) if o["cum_profit"][YEARS == y][-1] > 0), 99))
    return (np.array(rev), np.array(rev_ex), np.array(cum), np.array(pay),
            np.array(peak), np.array(be))


def annualise(arr):
    """29-grid -> 7 annual sums per path."""
    return np.stack([arr[:, YEARS == y].sum(axis=1) for y in range(1, 8)], axis=1)


def fan(ax, x, data, color=GOLD, label="Median"):
    p5, p25, p50, p75, p95 = np.percentile(data, [5, 25, 50, 75, 95], axis=0)
    ax.fill_between(x, p5, p95, alpha=0.12, color=color, label="5th-95th")
    ax.fill_between(x, p25, p75, alpha=0.25, color=color, label="25th-75th")
    ax.plot(x, p50, color=color, linewidth=2.5, label=label)


def main():
    print("charts ->", OUT)
    det = DetModel(); det.run()
    rev, rev_ex, cum, pay, peak, be = mc_panels(2000)

    # 1. peak funding histogram - the raise
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(peak / 1e6, bins=40, color=GOLD, edgecolor=CREAM, alpha=0.85)
    p50, p90 = np.percentile(peak, [50, 90]) / 1e6
    ax.axvline(p50, color=LIGHT_GOLD, lw=2, label=f"Median ${p50:.2f}M")
    ax.axvline(p90, color=DARK, lw=2, ls="--", label=f"90% covered ${p90:.2f}M")
    ax.axvline(det.out["peak_funding"][-1] / 1e6, color=RED, lw=2, ls=":",
               label=f"Workbook ${det.out['peak_funding'][-1]/1e6:.2f}M")
    ax.set_xlabel("Peak funding need (USD millions)"); ax.set_ylabel("Number of paths")
    ax.set_title("How much to raise: peak funding across 2,000 paths")
    ax.legend(); style(ax, fig); save(fig, "peak_funding_hist.png")

    # 2. P(cumulative break-even by year)
    fig, ax = plt.subplots(figsize=(9, 5))
    ys = np.arange(3, 8); probs = [(be <= y).mean() for y in ys]
    bars = ax.bar([f"Y{y}" for y in ys], probs, color=GOLD, edgecolor=CREAM, width=0.6)
    for b, v in zip(bars, probs):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.0%}", ha="center", color=DARK)
    ax.set_ylim(0, 1); ax.set_ylabel("Share of paths cumulative-positive")
    ax.set_title("When does the business pay back everything spent?")
    style(ax, fig); save(fig, "breakeven_by_year.png")

    # 3. revenue with and without B2B - two panels, one axis each
    yl = [f"Y{y}" for y in range(1, 8)]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
    fan(axes[0], yl, annualise(rev) / 1e6); axes[0].set_title("Total revenue, USD M")
    fan(axes[1], yl, annualise(rev_ex) / 1e6, color=DARK); axes[1].set_title("Revenue without B2B, USD M")
    for ax in axes:
        style(ax, fig); ax.set_xlabel("Year")
    axes[0].legend(loc="upper left"); save(fig, "revenue_fan_with_without_b2b.png")

    # 4. cumulative profit fan
    fig, ax = plt.subplots(figsize=(12, 6))
    fan(ax, np.arange(29), cum / 1e6)
    ax.axhline(0, color=RED, ls="--", lw=1.5, label="Break-even")
    ax.set_xticks(np.arange(0, 29, 2)); ax.set_xticklabels(XLAB[::2], rotation=45)
    ax.set_ylabel("Cumulative net profit, USD M"); ax.set_title("Cumulative profit across 2,000 paths")
    ax.legend(); style(ax, fig); save(fig, "cum_profit_fan.png")

    # 5. tornado
    A = json.load(open(os.path.join(HERE, "outputs", "analysis.json")))
    t = A["q6_tornado"][:10][::-1]
    base_np7 = float(det.out["net_profit"][YEARS == 7].sum())
    fig, ax = plt.subplots(figsize=(11, 6))
    names = [d["param"].replace("_", " ") for d in t]
    lo = np.array([d["np7_lo"] for d in t]) / 1e6; hi = np.array([d["np7_hi"] for d in t]) / 1e6
    ax.barh(names, hi - base_np7 / 1e6, left=base_np7 / 1e6, color=GOLD, edgecolor=CREAM)
    ax.barh(names, lo - base_np7 / 1e6, left=base_np7 / 1e6, color=DARK, edgecolor=CREAM)
    ax.axvline(base_np7 / 1e6, color=RED, ls="--", lw=1.5, label=f"Base ${base_np7/1e6:.2f}M")
    ax.set_xlabel("Year 7 net profit, USD M"); ax.set_title("Which inputs move the answer")
    ax.legend(); style(ax, fig); save(fig, "tornado.png")

    # 6. stress scenarios - two small multiples
    S = A["stress"]; labels = {"base": "Base", "s1_gold_crash_30": "Gold -30%",
                               "s2_redemption_run_25pct_M24": "Redemption run", "s3_zero_b2b": "Zero B2B",
                               "s4_adoption_failure": "Adoption fails", "s5_regulatory_delay": "Licence +12mo",
                               "s6_ticket_compression": "Ticket squeeze", "s7_combined_tail": "Combined tail"}
    keys = list(labels)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    v1 = [S[k]["cum7"] / 1e6 for k in keys]; v2 = [S[k]["peak_funding"] / 1e6 for k in keys]
    cols = [RED if v < 0 else GOLD for v in v1]
    axes[0].barh([labels[k] for k in keys], v1, color=cols, edgecolor=CREAM)
    axes[0].axvline(0, color=DARK, lw=1); axes[0].set_title("Cumulative profit at Y7, USD M")
    axes[1].barh([labels[k] for k in keys], v2, color=GOLD, edgecolor=CREAM)
    axes[1].set_title("Peak funding need, USD M")
    for ax in axes:
        style(ax, fig); ax.invert_yaxis()
    save(fig, "stress_scenarios.png")

    # 7. tier mix over time (agent book)
    pool, panel, sc = run_book(seed=20270101, scale=2.0)
    months = np.array([r["month"] for r in panel])
    tm = np.array([r["tier_mix"] for r in panel])       # (T,5) counts
    tiered = tm[:, 1:].sum(axis=1); tiered[tiered == 0] = 1
    shares = (tm[:, 1:] / tiered[:, None]).T
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(months, shares, labels=["Silver", "Gold", "Platinum", "Sovereign"],
                 colors=[WARM, GOLD, DARK, RED], alpha=0.9)
    ax.set_xlabel("Month"); ax.set_ylabel("Share of tiered customers"); ax.set_ylim(0, 1)
    ax.set_title("Who is in which tier, and when")
    ax.legend(loc="upper left"); style(ax, fig); save(fig, "tier_mix_over_time.png")

    # 8. ladder envelope heatmap
    E = A["q2_envelope"]; ceilings = ["1.0", "1.5", "2.0"]; shapes = ["convex", "linear", "concave"]
    M = np.array([[E[f"c{c}_{s}"]["giveback_share"] for s in shapes] for c in ceilings])
    fig, ax = plt.subplots(figsize=(8, 6))
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("brand", [CREAM, LIGHT_GOLD, GOLD, RED], N=256)
    im = ax.imshow(M, cmap=cmap, vmin=0, vmax=0.20)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f"{M[i,j]:.1%}", ha="center", va="center", color=DARK, fontsize=12)
    ax.set_xticks(range(3)); ax.set_xticklabels(["Top-loaded", "Linear", "Front-loaded"])
    ax.set_yticks(range(3)); ax.set_yticklabels([f"{c}pp off at top" for c in ceilings])
    ax.set_title("ICS giveback as % of revenue, by ladder shape"); fig.patch.set_facecolor(CREAM)
    ax.title.set_color(DARK); save(fig, "ladder_heatmap.png")

    # 9. decile profit share
    D = A["q3_decile_share"]["rho_0.0"]
    # The bottom five deciles are all floor savers at exactly USD 20, so their
    # individual order is arbitrary. Show them as one group.
    vals = [sum(D[:5])] + D[5:]
    labs = ["Floor savers\n(bottom 50%)", "D6", "D7", "D8", "D9", "D10\n(top 10%)"]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labs, vals, color=[MED] + [LIGHT_GOLD] * 2 + [GOLD] * 3, edgecolor=CREAM)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.006, f"{v:.0%}", ha="center", color=DARK, fontsize=10)
    ax.set_xlabel("Customers ranked by monthly ticket"); ax.set_ylabel("Share of profit")
    ax.set_title("Where the profit sits"); style(ax, fig); save(fig, "profit_by_ticket_decile.png")

    # 10. rail mix
    R = A["q3_rail"]; keys = ["prefunded_0", "prefunded_25", "prefunded_50", "prefunded_75"]
    fig, ax = plt.subplots(figsize=(9, 5))
    x = ["0%", "25%", "50%", "75%"]; g = [R[k]["gated_share_m84"] for k in keys]
    bars = ax.bar(x, g, color=GOLD, edgecolor=CREAM, width=0.6)
    for b, v in zip(bars, g):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:.1%}", ha="center", color=DARK)
    ax.set_xlabel("Share of customers on the prefunded balance"); ax.set_ylabel("Share who reach a tier")
    ax.set_ylim(0.4, 0.6); ax.set_title("The rail decides who earns a tier")
    style(ax, fig); save(fig, "rail_mix.png")

    # 11. margin calls by LTV rung
    MC = json.load(open(os.path.join(HERE, "outputs", "margin_calls_by_ltv.json")))
    rungs = [("0.5", "Silver 50%"), ("0.59", "Mix 59%"), ("0.725", "Platinum 72.5%"), ("0.8", "Sovereign 80%")]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].bar([r[1] for r in rungs], [MC[r[0]]["P_any_call"] for r in rungs], color=[GOLD, GOLD, LIGHT_GOLD, RED], edgecolor=CREAM)
    axes[0].set_ylim(0, 1.05); axes[0].set_title("Chance of at least one margin call in 7 years")
    axes[1].bar([r[1] for r in rungs], [MC[r[0]]["called_share_p50"] for r in rungs], color=[GOLD, GOLD, LIGHT_GOLD, RED], edgecolor=CREAM)
    axes[1].set_title("Share of the credit book called, median path")
    for ax in axes:
        style(ax, fig)
        for tick in ax.get_xticklabels():
            tick.set_rotation(15)
    save(fig, "margin_calls_by_ltv.png")

    # 12. float: workbook rule vs inventory model
    grid_m = np.array(p0["grid"]["months"], dtype=int)
    def to_m(v):
        o = []
        for i, m in enumerate(grid_m):
            o.extend([v[i] / m] * m)
        return np.array(o[:84])
    bought = to_m(det.out["grams_bought"])
    prev = np.concatenate([[0.0], det.out["grams_cust"][:-1]])
    red = to_m(np.maximum(0, prev + det.out["grams_bought"] - det.out["grams_cust"]))
    gold_m = np.concatenate([np.repeat(det.out["gold_price"], grid_m)[:84], [det.out["gold_price"][-1]]])
    f = run_float(np.random.default_rng(10), bought, red, gold_m, gold_vol=0.0)
    wb = np.repeat(det.out["float_grams"], grid_m)[:84]
    fig, ax = plt.subplots(figsize=(12, 5.5))
    ax.plot(np.arange(1, 85), wb, color=RED, lw=2, ls="--", label="Workbook rule (1 bar + 10 days)")
    ax.plot(np.arange(1, 85), f["float_avg"], color=GOLD, lw=2.5, label="Inventory model, monthly average")
    ax.plot(np.arange(1, 85), f["S_level"], color=MED, lw=1.2, label="Order-up-to level before payday")
    ax.set_xlabel("Month"); ax.set_ylabel("Grams held in the float")
    ax.set_title("How much gold Aurumix needs to own"); ax.legend(); style(ax, fig)
    save(fig, "float_workbook_vs_inventory.png")

    # 13. threshold - retail alone vs partners
    T = A["q1_threshold"]
    fig, ax = plt.subplots(figsize=(9, 5))
    conts = ["15%", "30%", "50%"]
    vals = [T[f"contingency_{c}"]["blended_cac"]["paying_needed_ex_b2b"] or 0 for c in (15, 30, 50)]
    bars = ax.bar(conts, [v / 1e3 for v in vals], color=[GOLD, LIGHT_GOLD, RED], edgecolor=CREAM, width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, (v / 1e3) + 3, f"{v/1e3:,.0f}k" if v else "unreachable",
                ha="center", color=DARK)
    ax.axhline(75, color=DARK, ls=":", lw=1.5, label="O Gold's active UAE users (75k)")
    ax.set_xlabel("Contingency on the cost base"); ax.set_ylabel("Paying customers needed, thousands")
    ax.set_title("Retail alone: customers needed to cover fixed costs"); ax.legend()
    style(ax, fig); save(fig, "threshold_retail_alone.png")

    print("done")


if __name__ == "__main__":
    main()
