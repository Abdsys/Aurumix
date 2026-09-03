"""
Standing audit for loose ends. Run it after any change to the model.

    python scripts/audit_model.py

These are the classes of defect that do not announce themselves: a parameter the
client priced that the simulation silently freezes, a rule that stops binding, a
derived quantity left at base while its inputs move, a business line that
quietly goes back to being computed on an average. Each one was found by hand at
least once. This script means none of them has to be found by hand again.

The audit was rewritten when the two-engine architecture was removed. Half of
what it used to check was whether one engine's answer reached the other engine,
which is not a question any more.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from config import config as C
from config.overrides import MODEL_OVERRIDES, EXTRA_TRIPLES
from src.agentbook import LADDER
from src.detmodel import load_params
from src.mcmodel import _match_triples, NOT_DRAWN, run_path
from src.twin import Twin, scaled_archetypes

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails, warns = [], []


def check(ok, msg, hard=True):
    if not ok:
        (fails if hard else warns).append(msg)
    print(f"  [{'PASS' if ok else ('FAIL' if hard else 'WARN')}] {msg}")


print("=" * 78)
print("MODEL AUDIT")
print("=" * 78)

p = load_params()
raw = load_params(raw=True)
base = Twin(scale=25.0).run()

# ── 1. every priced band is drawn, or excluded with a reason ─────────────────
print("\n1. Priced uncertainty reaches the Monte Carlo")
with open(os.path.join(HERE, "config", "scenario_map.json")) as f:
    name_to_key = json.load(f)
drawn = set(_match_triples(p))
banded, frozen = set(), []
for tbl, tri in p["scenario_triples"].items():
    key = name_to_key.get(tbl)
    if key is None or max(tri[1], tri[2]) - min(tri[1], tri[2]) <= 0:
        continue
    banded.add(key)
    if key not in drawn and key not in NOT_DRAWN:
        frozen.append((tbl, key))
check(not frozen, f"{len(drawn)} parameters drawn of {len(banded)} banded; "
                  f"{len(NOT_DRAWN)} excluded with a stated reason")
for tbl, key in frozen:
    print(f"        FROZEN WITHOUT REASON: {tbl}  ->  {key}")
check(all(k in drawn for k in EXTRA_TRIPLES),
      f"the Phase 5 bands are drawn ({', '.join(EXTRA_TRIPLES)})")

# ── 2. one engine, on a monthly clock ────────────────────────────────────────
print("\n2. There is one engine, and it runs monthly")
check(len(base["net_profit"]) == C.HORIZON_MONTHS,
      f"the twin produces {C.HORIZON_MONTHS} monthly steps, not a 29-column grid")
trough = int(np.argmax(base["funding"])) + 1
check(trough % 12 not in (0,) or trough <= 24,
      f"peak funding is found at month {trough}, a month the old annual grid "
      f"could not observe" if trough % 12 else
      f"peak funding lands on month {trough}")
check(abs(base["peak_funding"][-1] - np.max(base["funding"])) < 1.0,
      "peak funding is the true maximum of the monthly cash line")
src_mc = open(os.path.join(HERE, "src", "mcmodel.py")).read()
check("DetModel" not in src_mc,
      "the Monte Carlo runtime does not import the workbook port")
src_twin = open(os.path.join(HERE, "src", "twin.py")).read()
check("DetModel" not in src_twin,
      "and neither does the twin: the port survives only in the reconciliation")

# ── 3. the business runs on customers, not on averages ──────────────────────
print("\n3. Customer-dependent lines are computed on customers")
flat = {k: np.full(5, v[0]) for k, v in LADDER.items()}
no_ladder = Twin(scale=25.0, ladder=flat).run()
yrs = base["year"]
check(no_ladder["ics_cost"][yrs == 7].sum() < 1.0,
      "flattening the ladder removes the giveback entirely, so it is priced from "
      "the tier each customer actually holds")
check(no_ladder["s2"][yrs == 7].sum() != base["s2"][yrs == 7].sum(),
      "and it changes card revenue, because the loan-to-value a customer borrows "
      "at is their own tier's")
check(base["qual_share"][-1] > 0.2,
      f"the twin counts who actually tiered ({base['qual_share'][-1]:.1%}), rather "
      f"than applying the workbook's flat share")
check(base["orig_usd"].sum() > 0 and len(base["orig_usd"]) == C.HORIZON_MONTHS,
      "credit originations are a real monthly series, so the margin-call model "
      "no longer spreads a year's lending evenly across it")

# ── 4. persistency drives behaviour, not a book-average rate ─────────────────
print("\n4. Persistency moves the simulation")
lo = Twin(scale=25.0, overrides={"persistency": 0.53}).run()
hi = Twin(scale=25.0, overrides={"persistency": 0.73}).run()
check(lo["paying"][-1] < base["paying"][-1] < hi["paying"][-1],
      f"drawing persistency changes the book ({lo['paying'][-1]:,.0f} / "
      f"{base['paying'][-1]:,.0f} / {hi['paying'][-1]:,.0f} at 53/63/73%)")
a53 = scaled_archetypes(0.53)
a73 = scaled_archetypes(0.73)
check(all(x.own_hazard >= y.own_hazard for x, y in zip(a53, a73)),
      "it does so by rescaling every archetype hazard by one factor, preserving "
      "the mix and the ordering")

# ── 5. derived quantities follow what they are derived from ─────────────────
print("\n5. Derived quantities follow their inputs")
o, _ = run_path(20270101)
d = o["_draw"]
check(abs(d["monthly_churn"] - (1 - d["persistency"] ** (1 / 12))) < 1e-9,
      "monthly churn follows the drawn persistency")
check(abs(d["partner_aum"] - d.get("partner_users", p["partner_users"])
          * d["partner_adopt"] * d["partner_aum_user"]) < 1.0,
      "partner AUM follows its drawn components")

# ── 6. deliberate departures are declared ───────────────────────────────────
print("\n6. Departures from the workbook are declared")
for k, v in MODEL_OVERRIDES.items():
    check(raw.get(k) != v, f"'{k}' departs from the workbook ({raw.get(k)} -> {v}) "
                           f"and is declared in config/overrides.py")

# ── 7. every parameter the engine reads exists ──────────────────────────────
print("\n7. Every parameter the twin reads exists")
hard = set(re.findall(r'(?<![A-Za-z_])p\["([a-z0-9_]+)"\]', src_twin))
optional = set(re.findall(r'(?<![A-Za-z_])p\.get\("([a-z0-9_]+)"', src_twin))
missing = sorted(r for r in hard - optional if r not in p and not r.startswith("_"))
check(not missing, f"{len(hard)} required references resolve; {len(optional)} "
                   f"optional hooks may be absent by design")
for m in missing:
    print(f"        MISSING: {m}")

# ── 8. the ladder is internally consistent ──────────────────────────────────
print("\n8. The benefit ladder is internally consistent")
check(all(len(v) == 5 for v in LADDER.values()), "every row has five rungs")
check(LADDER["entry_fee"][0] == C.ENTRY_FEE,
      f"the untiered entry fee equals the workbook's {C.ENTRY_FEE:.0%}")
check(all(np.all(np.diff(LADDER[k]) <= 1e-12) for k in ("entry_fee", "fx_margin")),
      "prices charged fall monotonically up the ladder")
check(all(np.all(np.diff(LADDER[k]) >= -1e-12) for k in ("family_disc", "ltv", "rewards")),
      "benefits given rise monotonically up the ladder")

# ── 9. acquisition responds to the model ────────────────────────────────────
print("\n9. Acquisition responds to the model, not to a fixed formula")
wide = Twin(scale=25.0, overrides={"ceiling_mult": 2.0}).run()
check(wide["cum_ever"][-1] > base["cum_ever"][-1] * 1.02,
      f"the addressable ceiling binds ({base['cum_ever'][-1]:,.0f} acquired, "
      f"{wide['cum_ever'][-1]:,.0f} if the market is twice as big)")
noconv = Twin(scale=25.0, overrides={"cac_conv_coef": 0.0}).run()
check(base["cum_ever"][-1] < noconv["cum_ever"][-1] * 0.99,
      f"CAC convexity is live: the same budget buys {base['cum_ever'][-1]:,.0f} "
      f"customers, not {noconv['cum_ever'][-1]:,.0f}")
check(base["ref_acq"][:12].sum() == 0 and base["ref_acq"][-12:].sum() > 0,
      "referrals start only when the programme does, then come from the book")

print("\n" + "=" * 78)
print(f"{'AUDIT PASSED' if not fails else 'AUDIT FAILED'}  "
      f"({len(fails)} failures, {len(warns)} warnings)")
print("=" * 78)
sys.exit(1 if fails else 0)
