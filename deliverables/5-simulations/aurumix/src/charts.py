"""
Charts for SIMULATION_RESULTS.md. Tokenomics.net palette, Stockpile styling.

    python -m src.charts        (from the aurumix/ directory)

Every figure is drawn from the SAVED OUTPUT of the run that produced the
numbers in the document: mc_results.csv, mc_bands.npz, mc_summary.json,
mc_recommended.json, analysis.json, float_results.json. The old chart module re-ran
its own paths, which meant a figure could quietly disagree with the sentence
printed beside it. Nothing here runs the model.
"""

import json
import os

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

GOLD = "#B8956E"; DARK = "#1A1714"; WARM = "#D4CFC8"; MED = "#9A9590"
LIGHT_GOLD = "#C4A77D"; DKGRAY = "#2D2D2D"; CREAM = "#FAF8F5"; RED = "#C44E52"
GREEN = "#5A8F6B"
CAT = [GOLD, DARK, MED, LIGHT_GOLD, RED, DKGRAY]

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTD = os.path.join(HERE, "outputs")
CH = os.path.join(OUTD, "charts")
os.makedirs(CH, exist_ok=True)


def _load(name, default=None):
    p = os.path.join(OUTD, name)
    if not os.path.exists(p):
        return default
    if name.endswith(".json"):
        with open(p) as f:
            return json.load(f)
    if name.endswith(".npz"):
        return np.load(p)
    return pd.read_csv(p)


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
    ax.title.set_color(DARK)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(CH, name), dpi=160, facecolor=CREAM)
    plt.close(fig)
    print("  wrote", name)


def usd(x, _=None):
    if abs(x) >= 1e6:
        return f"${x/1e6:.1f}m"
    if abs(x) >= 1e3:
        return f"${x/1e3:.0f}k"
    return f"${x:.0f}"


def _fan(ax, x, b, key, color, label):
    ax.fill_between(x, b[f"{key}_p10"], b[f"{key}_p90"], color=color, alpha=0.15, lw=0)
    ax.fill_between(x, b[f"{key}_p25"], b[f"{key}_p75"], color=color, alpha=0.28, lw=0)
    ax.plot(x, b[f"{key}_p50"], color=color, lw=2.0, label=label)


def main():
    df = _load("mc_results.csv")
    S = _load("mc_summary.json")
    # The recommended configuration exists only once a set is agreed with the
    # client and run through mc_config.py, then promoted to this name. Absent
    # file means every chart draws the plan alone (client, 2026-09-04: no
    # recommended bars until a set is agreed).
    C = _load("mc_recommended.json")
    A = _load("analysis.json")
    B = _load("mc_bands.npz")
    F = _load("float_results.json")
    CD = _load("conditions.json")
    STM = _load("stress_mc.json")
    m = np.arange(1, 85)
    print("charts ->", CH)

    # 1. the raise ------------------------------------------------------------
    if df is not None:
        fig, ax = plt.subplots(figsize=(10, 5.5))
        style(ax, fig)
        ax.hist(df.peak_funding, bins=60, color=GOLD, alpha=0.75, edgecolor=CREAM, lw=0.4)
        for q, c, ls in ((0.5, DARK, "--"), (0.9, RED, "-")):
            v = float(np.quantile(df.peak_funding, q))
            ax.axvline(v, color=c, ls=ls, lw=1.6)
            ax.text(v, ax.get_ylim()[1] * (0.94 if q == 0.9 else 0.84), f" p{int(q*100)}  {usd(v)}",
                    color=c, fontsize=9, va="top")
        ax.xaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Peak funding need over seven years")
        ax.set_ylabel("Paths")
        ax.set_title("How much must be raised, across 2,000 futures", fontsize=12, pad=12)
        save(fig, "peak_funding_hist.png")

    # 2. cumulative profit fan ------------------------------------------------
    if B is not None:
        fig, ax = plt.subplots(figsize=(10, 5.5))
        style(ax, fig)
        _fan(ax, m, B, "cum_profit", GOLD, "Median path")
        ax.axhline(0, color=DARK, lw=1.1)
        i = int(np.argmin(B["cum_profit_p50"]))
        ax.annotate(f"deepest point, month {i+1}\n{usd(B['cum_profit_p50'][i])}",
                    xy=(i + 1, B["cum_profit_p50"][i]), xytext=(i + 6, B["cum_profit_p50"][i] * 0.55),
                    color=DARK, fontsize=9,
                    arrowprops=dict(arrowstyle="->", color=MED, lw=1))
        ax.yaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Month")
        ax.set_ylabel("Cumulative net profit")
        ax.set_title("The hole, and how it fills. Shaded: middle 50% and middle 80% of paths",
                     fontsize=12, pad=12)
        ax.legend(frameon=False, fontsize=9)
        save(fig, "cum_profit_fan.png")

    # 3. revenue with and without B2B ----------------------------------------
    if B is not None:
        fig, ax = plt.subplots(figsize=(10, 5.5))
        style(ax, fig)
        _fan(ax, m, B, "revenue", GOLD, "Total revenue")
        retail = {f"revenue_{q}": B[f"revenue_{q}"] - B[f"s6_{q}"]
                  for q in ("p10", "p25", "p50", "p75", "p90")}
        _fan(ax, m, retail, "revenue", DARK, "Retail only, no partners")
        ax.yaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Month")
        ax.set_ylabel("Monthly revenue")
        ax.set_title("The gap between the two lines is the partner business", fontsize=12, pad=12)
        ax.legend(frameon=False, fontsize=9)
        save(fig, "revenue_fan_with_without_b2b.png")

    # 4. break-even odds, plan vs recommended --------------------------------
    if S is not None:
        fig, ax = plt.subplots(figsize=(9, 5.2))
        style(ax, fig)
        yrs = ["Y4", "Y5", "Y6", "Y7"]
        plan = [S["P_cum_breakeven_by"][y] for y in yrs]
        x = np.arange(len(yrs))
        w = 0.38 if C else 0.55
        ax.bar(x - (w / 2 if C else 0), plan, w, color=GOLD, label="Plan as modelled")
        if C:
            rec = [np.nan, np.nan, np.nan, C["P_cum_breakeven_by_Y7"]]
            ax.bar(x + w / 2, rec, w, color=DARK, label="Recommended configuration")
        for xi, v in zip(x, plan):
            ax.text(xi - (w / 2 if C else 0), v + 0.012, f"{v:.0%}", ha="center",
                    color=DARK, fontsize=9)
        if C:
            ax.text(x[-1] + w / 2, C["P_cum_breakeven_by_Y7"] + 0.012,
                    f"{C['P_cum_breakeven_by_Y7']:.0%}", ha="center", color=DARK, fontsize=9)
        ax.set_xticks(x); ax.set_xticklabels(["Year 4", "Year 5", "Year 6", "Year 7"])
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
        ax.set_ylabel("Share of paths in cumulative profit")
        ax.set_title("Odds of having repaid the hole", fontsize=12, pad=12)
        ax.legend(frameon=False, fontsize=9)
        save(fig, "breakeven_by_year.png")

    # 5. what moves profit ----------------------------------------------------
    if A and "q6_tornado" in A:
        t = A["q6_tornado"]
        items = sorted(t, key=lambda d: -abs(d["np7_swing"]))[:12][::-1]
        fig, ax = plt.subplots(figsize=(10, 6))
        style(ax, fig)
        names = [d["param"].replace("_", " ") for d in items]
        sw = [d["np7_swing"] for d in items]
        ax.barh(names, sw, color=[GOLD if s > 0 else MED for s in sw], height=0.68)
        ax.xaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Swing in year-seven net profit across the assumption's range")
        ax.set_title("What the answer depends on", fontsize=12, pad=12)
        save(fig, "tornado.png")

    # 6. stress scenarios -----------------------------------------------------
    if STM is not None:
        s = {k: v for k, v in STM.items() if not k.startswith("_")}
        labs = {"base": "Base", "s1_gold_crash_30": "Gold crashes 30%, savers panic",
                "s2_redemption_run_25pct_M24": "Redemption run",
                "s3_zero_b2b": "No partners at all",
                "s4_adoption_failure": "Adoption failure",
                "s5_regulatory_delay": "Regulatory delay",
                "s6_ticket_compression": "Ticket compression",
                "s7_combined_tail": "Combined tail"}
        keys = [k for k in labs if k in s]
        fig, ax = plt.subplots(figsize=(10, 5.6))
        style(ax, fig)
        vals = [s[k]["cum7"] for k in keys]
        lo = [s[k]["cum7"] - s[k]["cum7_p10"] for k in keys]
        hi = [s[k]["cum7_p90"] - s[k]["cum7"] for k in keys]
        cols = [GREEN if v > 0 else RED for v in vals]
        cols[0] = DARK
        y = np.arange(len(keys))[::-1]
        ax.barh(y, vals, color=cols, height=0.62,
                xerr=[lo, hi], error_kw=dict(ecolor=MED, elinewidth=1.1, capsize=3))
        ax.set_yticks(y); ax.set_yticklabels([labs[k] for k in keys])
        ax.axvline(0, color=DARK, lw=1)
        ax.xaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Profit after seven years. Bar is the typical run, whiskers the middle 80%")
        n_p = STM["_meta"]["n_paths"]
        ax.set_title(f"Seven things going wrong, each across {n_p} runs", fontsize=12, pad=12)
        save(fig, "stress_scenarios.png")

    # 7. the retail threshold -------------------------------------------------
    if A and "q1_threshold" in A and S is not None:
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        style(ax, fig)
        conts, needs = [], []
        for c in (15, 30, 50):
            row = A["q1_threshold"].get(f"contingency_{c}", {})
            n = row.get("blended_cac", {}).get("paying_needed_ex_b2b")
            conts.append(f"{c}%")
            needs.append(n if n and n > 0 else np.nan)
        x = np.arange(3)
        ax.bar(x, needs, 0.5, color=GOLD)
        built = S["paying_y7"]["p50"]
        ax.axhline(built, color=DARK, ls="--", lw=1.5)
        ax.text(2.42, built, f" book actually built: {built:,.0f}", color=DARK,
                fontsize=9, va="bottom", ha="right")
        for xi, v in zip(x, needs):
            ax.text(xi, (v if np.isfinite(v) else 0) * 1.02,
                    f"{v:,.0f}" if np.isfinite(v) else "unreachable",
                    ha="center", color=DARK, fontsize=9)
        ax.set_xticks(x); ax.set_xticklabels([f"contingency {c}" for c in conts])
        ax.set_ylabel("Paying customers needed, retail alone")
        ax.set_title("What retail would have to reach without partners", fontsize=12, pad=12)
        save(fig, "threshold_retail_alone.png")

    # 8. tier mix over time ---------------------------------------------------
    if A and "q2_tier_mix_m84" in A:
        mix = A["q2_tier_mix_m84"]
        fig, ax = plt.subplots(figsize=(8.6, 5.2))
        style(ax, fig)
        names = list(mix.keys())
        vals = [mix[k] for k in names]
        ax.bar([n.title() for n in names], vals, 0.55,
               color=[LIGHT_GOLD, GOLD, DKGRAY, DARK][:len(names)])
        for i, v in enumerate(vals):
            ax.text(i, v + 0.008, f"{v:.1%}", ha="center", color=DARK, fontsize=9)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
        ax.set_ylabel("Share of tiered customers at month 84")
        ax.set_title("Where the loyalty book ends up, seven years in", fontsize=12, pad=12)
        save(fig, "tier_mix_over_time.png")

    # 9. profit concentration -------------------------------------------------
    if A and "q3_decile_share" in A:
        sh = A["q3_decile_share"].get("rho_0.4") or list(A["q3_decile_share"].values())[0]
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        style(ax, fig)
        ax.bar(np.arange(1, 11), sh, 0.6, color=GOLD)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
        ax.set_xticks(np.arange(1, 11))
        ax.set_xlabel("Customers ranked by monthly saving, lowest tenth to highest")
        ax.set_ylabel("Share of lifetime profit")
        ax.set_title("A minority of the book carries the economics", fontsize=12, pad=12)
        save(fig, "profit_by_ticket_decile.png")

    # 10. partner dependence --------------------------------------------------
    if df is not None and "b2b_partners_y7" in df:
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        style(ax, fig)
        g = df.groupby("b2b_partners_y7").net_profit_y7.median()
        g = g[g.index <= 20]
        ax.plot(g.index, g.values, color=GOLD, lw=2, marker="o", ms=4)
        ax.axhline(0, color=DARK, lw=1)
        ax.yaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Partners signed by year seven")
        ax.set_ylabel("Median year-seven net profit")
        ax.set_title("Profit tracks the partner count almost linearly", fontsize=12, pad=12)
        save(fig, "partner_dependence.png")

    # 11. the funding line ----------------------------------------------------
    if B is not None:
        fig, ax = plt.subplots(figsize=(10, 5.5))
        style(ax, fig)
        _fan(ax, m, B, "funding", GOLD, "Median path")
        i = int(np.argmax(B["funding_p90"]))
        ax.plot(m, B["funding_p90"], color=RED, lw=1.4, ls="--", label="90th percentile")
        ax.axvline(i + 1, color=MED, lw=1, ls=":")
        ax.text(i - 30, B["funding_p90"][i] * 0.97,
                "the 90th percentile is still rising at the horizon",
                color=DARK, fontsize=9)
        ax.yaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_xlabel("Month")
        ax.set_ylabel("Money that must have been raised by this month")
        ax.set_title("The funding line, and where it peaks", fontsize=12, pad=12)
        ax.legend(frameon=False, fontsize=9)
        save(fig, "funding_line.png")

    # 12. plan vs recommended -------------------------------------------------
    if S is not None and C is not None:
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        style(ax, fig)
        labels = ["Raise needed\n(9 in 10)", "Median year-seven\nprofit"]
        plan = [S["safe_raise"]["p90"], S["net_profit_y7"]["p50"]]
        rec = [C["safe_raise"]["p90"], C["net_profit_y7"]["p50"]]
        x = np.arange(2); w = 0.36
        ax.bar(x - w / 2, plan, w, color=MED, label="Plan as modelled")
        ax.bar(x + w / 2, rec, w, color=GOLD, label="Recommended configuration")
        for xi, (a, b) in enumerate(zip(plan, rec)):
            ax.text(xi - w / 2, a, f" {usd(a)}", ha="center", va="bottom", color=DARK, fontsize=9)
            ax.text(xi + w / 2, b, f" {usd(b)}", ha="center", va="bottom", color=DARK, fontsize=9)
        ax.set_xticks(x); ax.set_xticklabels(labels)
        ax.yaxis.set_major_formatter(FuncFormatter(usd))
        ax.set_title("What the recommended changes are worth", fontsize=12, pad=12)
        ax.legend(frameon=False, fontsize=9)
        save(fig, "plan_vs_recommended.png")

    # 13. the conditions map ---------------------------------------------------
    if CD is not None:
        g = np.array(CD["cum_profit"]) / 1e6
        cm = np.array(CD["cac_mult"])
        pr = CD["partners"]
        fig, ax = plt.subplots(figsize=(10, 5.8))
        style(ax, fig)
        lim = np.abs(g).max()
        im = ax.imshow(g, cmap="RdYlGn", vmin=-lim, vmax=lim, aspect="auto", origin="lower")
        ax.set_xticks(range(len(pr))); ax.set_xticklabels(pr)
        base = CD["cac_band"]["base"]
        ax.set_yticks(range(len(cm)))
        ax.set_yticklabels([f"{m:.2f}x  (UAE {base['uae']*m:.0f})" for m in cm])
        for i in range(len(cm)):
            for j in range(len(pr)):
                ax.text(j, i, f"{g[i, j]:.1f}", ha="center", va="center",
                        color=DARK, fontsize=8.5)
        # the plan's own position
        pi = int(np.argmin(np.abs(cm - 1.0)))
        pj = pr.index(CD["plan_position"]["partners"]) if CD["plan_position"]["partners"] in pr else None
        if pj is not None:
            ax.add_patch(plt.Rectangle((pj - .5, pi - .5), 1, 1, fill=False,
                                       edgecolor=DARK, lw=2.2))
            ax.annotate("the plan sits here", xy=(pj + .5, pi), xytext=(pj + 1.15, pi + 1.15),
                        color=DARK, fontsize=9, ha="center",
                        arrowprops=dict(arrowstyle="->", color=DARK, lw=1.2))
        ax.set_xlabel("Partners signed by year seven")
        ax.set_ylabel("Cost per acquired customer")
        ax.set_title("What has to be true. Cumulative profit at year seven, USD millions",
                     fontsize=12, pad=12)
        ax.grid(False)
        save(fig, "conditions_map.png")

    # 14. per-region unit economics -------------------------------------------
    if CD is not None and CD.get("regions"):
        R = CD["regions"]
        names = [r.upper() for r in R]
        marg = [R[r]["margin"] for r in R]
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        style(ax, fig)
        cols = [GREEN if v > 0 else RED for v in marg]
        ax.bar(names, marg, 0.5, color=cols)
        ax.axhline(0, color=DARK, lw=1.2)
        for i, (r, v) in enumerate(zip(R, marg)):
            ax.text(i, v + (0.6 if v > 0 else -1.4),
                    "%+.2f\nCAC %.0f" % (v, R[r]["cac"]), ha="center",
                    color=DARK, fontsize=9)
        ax.set_ylabel("Margin per customer per year, USD")
        ax.set_title("Only one region pays for itself", fontsize=12, pad=12)
        save(fig, "regional_economics.png")

    print("done")


if __name__ == "__main__":
    main()
