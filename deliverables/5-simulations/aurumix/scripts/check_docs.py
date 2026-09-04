"""
Do the client documents still agree with the model?

A document quotes a number once and then the model moves. Nothing errors. The
figure just sits there being wrong until someone reads it carefully, and the
someone has so far been the client. Four figures in the threshold section of
SIMULATION_SETUP.md had been wrong since persistency changed from 55% to 63%,
which is two weeks of the document quietly contradicting the code.

This script pulls the live figures out of outputs/ and checks each one appears
in the documents where it is supposed to appear.

    python scripts/check_docs.py

It is deliberately narrow. It checks the load-bearing numbers, not every digit,
because a check that cries wolf gets switched off.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.dirname(HERE)
OUT = os.path.join(HERE, "outputs")

with open(os.path.join(OUT, "analysis.json")) as f:
    A = json.load(f)
with open(os.path.join(OUT, "mc_summary.json")) as f:
    M = json.load(f)
rep = open(os.path.join(OUT, "analysis_report.txt"), encoding="utf-8").read()


def num(pattern, text=rep, cast=float):
    m = re.search(pattern, text)
    return cast(m.group(1).replace(",", "")) if m else None


def money(v):
    """The forms a document might reasonably use for a dollar figure."""
    return {f"{v:,.0f}", f"{v/1e6:.2f}m", f"{v/1e6:.1f}m", f"{v/1e3:.0f}k"}


def pct(v):
    return {f"{v:.0%}", f"{v*100:.0f}%", f"{v:.1%}", f"{v*100:.1f}%"}


# The results document is now GENERATED from the same JSON these checks read
# (scripts/fill_results.py), so drift is structurally impossible for any figure
# that goes through a placeholder. These checks still earn their place: they
# catch a placeholder quietly removed from the template, and they catch the
# document being stale against a newer run.
RESULTS_ON_HOLD = False

# figure -> (set of acceptable renderings, which documents must carry it)
t15 = A["q1_threshold"]["contingency_15"]
RESULT_FIGURES = {
    "retail customers needed, 15% contingency":
        money(t15["blended_cac"]["paying_needed_ex_b2b"]),
    "safe raise p90": money(M["safe_raise"]["p90"]),
    "P(cumulative break-even by Y7)": pct(M["P_cum_breakeven_by"]["Y7"]),
    "median Y7 net profit": money(M["net_profit_y7"]["p50"]),
}

# The setup document explains HOW the simulation works and quotes structural
# figures only; result figures live in the results document (client feedback,
# 2026-09-03). So the setup checks pin structure, and every threshold-style
# figure sits in RESULT_FIGURES against the results document.
import sys as _sys
_sys.path.insert(0, HERE)
from src.mcmodel import _match_triples as _mt
from src.detmodel import load_params as _lp
from src.mechanics import fit_ticket_lognormal as _fit
_n_drawn = len(_mt(_lp()))
_mu, _sigma = _fit(33.60, 0.30)
CHECKS = {
    "drawn parameter count":
        ({f"{_n_drawn} parameters"}, ["SIMULATION_SETUP.md"]),
    "UAE ticket sigma":
        ({f"{_sigma:.3f}"}, ["SIMULATION_SETUP.md"]),
}
RESULT_FIGURES["partners to cover fixed base"] = {f"{t15['partners_to_cover_fixed_alone']:.1f}"}
RESULT_FIGURES["partners to cover fixed base"] = {f"{t15['partners_to_cover_fixed_alone']:.1f}"}
RESULT_FIGURES["gated share at month 84"] = {f"{A['q2_gated_share_m84']*100:.1f}%"}

print("=" * 78)
print("DOCUMENT / MODEL AGREEMENT")
print("=" * 78)

text = {}
for d in {d for _, docs in CHECKS.values() for d in docs}:
    path = os.path.join(DOCS, d)
    text[d] = open(path, encoding="utf-8").read() if os.path.exists(path) else ""

fails = []
for label, (forms, docs) in CHECKS.items():
    for d in docs:
        hit = any(f in text[d] for f in forms)
        if not hit:
            fails.append(f"{d}: {label} -> model says {' or '.join(sorted(forms))}")
        print(f"  [{'PASS' if hit else 'FAIL'}] {d:24} {label}"
              f"  ({sorted(forms)[0]})")

# The branded executive-summary PAGE is built from meta_results.json, not from
# the markdown, so it drifted through every rewrite today while the body moved
# on. It is the first page a reader sees. These checks pin it to the same live
# outputs as everything else.
_meta = os.path.join(DOCS, "_branded_working", "meta_results.json")
if os.path.exists(_meta):
    _mt = open(_meta, encoding="utf-8").read()
    print()
    # the summary page reports the PLAN, not the recommendation. The
    # recommendation lives in Part 4 where the reader can see what it costs.
    for _lbl, _forms in (("raise, plan", money(M["safe_raise"]["p90"])),
                         ("break-even, plan", pct(M["P_cum_breakeven_by"]["Y7"])),
                         ("year-7 profit, plan", money(M["net_profit_y7"]["p50"])),
                         ("partners to cover fixed base",
                          {f"{t15['partners_to_cover_fixed_alone']:.1f}"})):
        _ok = any(f in _mt for f in _forms)
        print(f"  [{'PASS' if _ok else 'FAIL'}] exec summary page      {_lbl}"
              f"  ({sorted(_forms)[0]})")
        if not _ok:
            fails.append(f"meta_results.json exec summary: {_lbl} -> model says "
                         f"{' or '.join(sorted(_forms))}")

res = os.path.join(DOCS, "SIMULATION_RESULTS.md")
if os.path.exists(res):
    rt = open(res, encoding="utf-8").read()
    stale = [k for k, forms in RESULT_FIGURES.items() if not any(f in rt for f in forms)]
    print()
    if RESULTS_ON_HOLD:
        print(f"  SIMULATION_RESULTS.md is ON HOLD by client instruction. "
              f"{len(stale)} of {len(RESULT_FIGURES)} headline figures are stale:")
        for k in stale:
            print(f"    - {k}: model now says {' or '.join(sorted(RESULT_FIGURES[k]))}")
        print("  Set RESULTS_ON_HOLD = False once it is rewritten.")
    else:
        for k, forms in RESULT_FIGURES.items():
            ok = k not in stale
            print(f"  [{'PASS' if ok else 'FAIL'}] SIMULATION_RESULTS.md   {k}"
                  f"  ({sorted(forms)[0]})")
            if not ok:
                fails.append(f"SIMULATION_RESULTS.md: {k} -> model says "
                             f"{' or '.join(sorted(forms))}")

print("=" * 78)
if fails:
    print(f"{len(fails)} figure(s) in the documents no longer match the model:")
    for f in fails:
        print("   ", f)
else:
    print("every checked figure matches")
print("=" * 78)
sys.exit(1 if fails else 0)
