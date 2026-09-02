"""
Stage 1 verification.

Blueprint Part 4.1: VERIFICATION IS NOT VALIDATION. Reproducing v2.6's figures
proves the first-passage arithmetic is right. It says nothing about Aurumix,
because those figures are outputs of a Markov solve over an archetype mix that
is itself a confirmed sourcing negative.

Nothing printed by this script is a finding.

    python scripts/verify_stage1.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from config import config as C
from src import mechanics as M
from src import invariants as I
from src.population import run_cohort, step
from src.entities import build_cohort

N = 300_000
results = []


def report(name, got, want, tol, unit=""):
    ok = abs(got - want) <= tol
    results.append(ok)
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] {name:44} got {got:8.3f}{unit}  want {want:7.3f}{unit}  (+/-{tol})")


print("=" * 78)
print("STAGE 1 VERIFICATION  -  code-correctness tests, NOT findings")
print("=" * 78)

# ── A. the formula reproduces the rulebook's stated arrival schedule ─────────
print("\nA. The ICS ladder, for a perfect payer (rulebook: Silver M6, Gold M12,")
print("   Platinum M36, Sovereign M60). v2.6's lookup put Gold at gate+12 = M18.")
for m, want_tier in [(6, "silver"), (12, "gold"), (36, "platinum"), (60, "sovereign")]:
    r = float(M.record(np.array([m]))[0])
    t = C.TIER_ORDER[int(M.tier_index(np.array([r]))[0])]
    ok = t == want_tier
    results.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] Record({m:2}) = {r:6.2f} -> {t:10} "
          f"want {want_tier}")

# ── B. Standing never binds a clean saver ───────────────────────────────────
print("\nB. Standing never binds a clean saver (scoring sec 7.4)")
try:
    I.check_clean_climb()
    results.append(True)
    print("  [PASS] Standing >= Record at every month of a clean climb")
except I.InvariantError as e:
    results.append(False)
    print(f"  [FAIL] {e}")

# ── C. the ticket fit ───────────────────────────────────────────────────────
print("\nC. Ticket distribution - a FIT to mean + floor share, not a chosen sigma")
rng = np.random.default_rng(7)
for reg in C.REGIONS:
    mu, sigma = M.fit_ticket_lognormal(reg.ticket_mean, C.TICKET_FLOOR_SHARE)
    t = M.draw_tickets(rng, 400_000, reg.ticket_mean, C.TICKET_FLOOR_SHARE)
    at_floor = float((t <= C.TICKET_FLOOR_USD + 1e-9).mean())
    report(f"{reg.name}: mean ticket", float(t.mean()), reg.ticket_mean, 0.30, " USD")
    report(f"{reg.name}: share at the floor", at_floor, C.TICKET_FLOOR_SHARE, 0.02)
    top = np.sort(t)[int(0.9 * t.size):]
    print(f"         sigma={sigma:.3f}  top decile mean USD {top.mean():6.2f}  "
          f"= {top.sum() / t.sum():5.1%} of all contributions")

# ── D. per-archetype first passage ──────────────────────────────────────────
print("\nD. Per-archetype gate arrival (v2.6 sec 0.2). Redemption OFF to isolate.")
for i, a in enumerate(C.ARCHETYPES_BASE):
    pool, _ = run_cohort(n=N, months=C.HORIZON_MONTHS, seed=1000 + i,
                         archetypes=[type(a)(a.name, 1.0, a.pay_prob, a.own_hazard,
                                             a.pay_decay, a.pay_floor)],
                         redemption_on=False, prefunded_share=0.0, ticket_sigma=0.0)
    ever = float(pool.gated.mean())
    gm = pool.gate_month[pool.gated]
    mean_gate = float(gm.mean()) if gm.size else float("nan")
    report(f"{a.name}: P(ever gates)", ever,
           C.VERIFY["per_archetype_ever_gate"][a.name], 0.03)
    report(f"{a.name}: mean gate month", mean_gate,
           C.VERIFY["per_archetype_mean_gate"][a.name], 1.5, " M")

# ── E. whole-book anchors ───────────────────────────────────────────────────
print("\nE. Whole-book anchors at the Base mix. Redemption OFF, ticket variance OFF,")
print("   so the run is comparable with v2.6's deterministic solve.")
pool, hist = run_cohort(n=N, months=C.HORIZON_MONTHS, seed=42,
                        redemption_on=False, prefunded_share=0.0, ticket_sigma=0.0)

for m, want in C.VERIFY["persistency"].items():
    if m <= C.HORIZON_MONTHS:
        got = hist[m - 1]["paying"] / N
        report(f"persistency M{m}", got, want, 0.025)

report("ever-gate share", float(pool.gated.mean()), C.VERIFY["ever_gate_share"], 0.03)
gm = pool.gate_month[pool.gated]
report("mean gate month", float(gm.mean()), C.VERIFY["mean_gate_month"], C.TOLERANCE_MONTHS, " M")

h61 = hist[60]
report("holding-not-contributing at M61",
       h61["holders"] / (h61["paying"] + h61["holders"]),
       C.VERIFY["holding_not_contributing_m61"], 0.03)

tc = np.array(hist[-1]["tier_counts"], dtype=float)
tiered = tc[1:].sum()
sov = float(tc[4] / tiered) if tiered else 0.0
print(f"\n   Sovereign share of tiered: {sov:.1%} - REPORTED, NOT A TARGET.")
print("   v2.6's ~1.2% came from the lookup that capped the occasional misser")
print("   at Platinum by construction; the real formula lets a clean trailing")
print("   year plus 60 counted months score 100. Expected deviation, documented.")

print(f"\n   Tier mix at M{C.HORIZON_MONTHS}, share of TIERED accounts:")
for name, cnt in zip(C.TIER_ORDER[1:], tc[1:]):
    print(f"      {name:10} {cnt / tiered:6.2%}" if tiered else f"      {name:10}   n/a")

# ── F. invariants ───────────────────────────────────────────────────────────
print("\nF. Invariants over a full live run (redemption ON, ticket variance ON)")
rng = np.random.default_rng(99)
pool = build_cohort(rng, 60_000, C.ARCHETYPES_BASE, C.BACKGROUND_HAZARD["base"])
prev = pool.months_counted.copy()
try:
    for m in range(1, C.HORIZON_MONTHS + 1):
        step(pool, m, rng, redemption_on=True)
        I.check(pool, prev_months_counted=prev)
        prev = pool.months_counted.copy()
    results.append(True)
    print(f"  [PASS] all invariants held for {C.HORIZON_MONTHS} months")
except I.InvariantError as e:
    results.append(False)
    print(f"  [FAIL] {e}")

# ── G. sanity checks ────────────────────────────────────────────────────────
print("\nG. Sanity checks")
p_perf = type(C.ARCHETYPES_BASE[0])("perfect", 1.0, 1.0, 0.0)
pool, _ = run_cohort(n=20_000, months=24, seed=5, archetypes=[p_perf],
                     background=0.0, redemption_on=False, prefunded_share=0.0,
                     ticket_sigma=0.0)
report("never-miss, no-hazard: ever-gate", float(pool.gated.mean()), 1.0, 1e-9)
report("never-miss, no-hazard: mean gate month",
       float(pool.gate_month[pool.gated].mean()), 6.0, 1e-9, " M")

p_none = type(C.ARCHETYPES_BASE[0])("never_pays", 1.0, 0.0, 0.0)
pool, _ = run_cohort(n=20_000, months=24, seed=6, archetypes=[p_none],
                     background=0.0, redemption_on=False, prefunded_share=0.0,
                     ticket_sigma=0.0)
report("never-pays: ever-gate", float(pool.gated.mean()), 0.0, 1e-9)
report("never-pays: grams", float(pool.grams.sum()), 0.0, 1e-9)

print("\n" + "=" * 78)
print(f"{sum(results)}/{len(results)} checks passed")
print("=" * 78)
sys.exit(0 if all(results) else 1)
