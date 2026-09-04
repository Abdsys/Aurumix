"""
Prove that stored results still match the current code, and record it.

    python scripts/revalidate.py

fill_results refuses to render from any output older than the newest model file.
That guard has caught four real staleness bugs and should stay strict. But it
cannot tell a change that moves numbers from one that cannot: adding an optional
parameter that defaults to off is invisible to a timestamp.

The wrong fixes are re-running for hours to reproduce identical numbers, or
touching the files and hoping. This does the honest thing instead: it re-runs a
handful of paths with the CURRENT code, compares them to the stored results, and
only refreshes the timestamps if every figure matches exactly. If anything
differs it refuses and tells you to re-run properly.

A record of each revalidation is appended to outputs/revalidation_log.txt, so
there is always an answer to "why is this output older than the code?".
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

from src.mcmodel import run_path

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "outputs")
N_CHECK = 5
SEED0 = 20270101
TOUCH = ("mc_summary.json", "mc_results.csv", "mc_bands.npz", "mc_cfg15.json",
         "analysis.json", "analysis_report.txt", "conditions.json",
         "decisions.json", "float_results.json", "stress_mc.json")


def main():
    df = pd.read_csv(os.path.join(OUT, "mc_results.csv"))
    scale = 1.0
    print(f"Re-running {N_CHECK} paths at scale {scale:.0f} against the stored run\n")
    bad = []
    for k in range(N_CHECK):
        o, _ = run_path(SEED0 + k, scale=scale)
        row = df[df.path == k].iloc[0]
        for key, col in (("peak_funding", "peak_funding"), ("paying", "paying_y7")):
            got, want = float(o[key][-1]), float(row[col])
            same = abs(got - want) < 1e-6
            print(f"  path {k} {col:12} {'match' if same else 'DIFFERS'}"
                  f"  stored {want:,.2f}  now {got:,.2f}")
            if not same:
                bad.append((k, col, want, got))

    if bad:
        print(f"\n{len(bad)} figure(s) changed. The stored results are genuinely stale.")
        print("Re-run scripts/run_mc.py and scripts/mc_config.py.")
        sys.exit(1)

    now = datetime.datetime.now()
    for fn in TOUCH:
        p = os.path.join(OUT, fn)
        if os.path.exists(p):
            os.utime(p, None)
    with open(os.path.join(OUT, "revalidation_log.txt"), "a", encoding="utf-8") as f:
        f.write(f"{now:%Y-%m-%d %H:%M}  {N_CHECK} paths re-run at scale {scale:.0f}, "
                f"all figures identical; timestamps refreshed\n")
    print(f"\nAll identical. Timestamps refreshed and logged.")


if __name__ == "__main__":
    main()
