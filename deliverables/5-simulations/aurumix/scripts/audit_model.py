"""
Standing audit for loose ends. Run it after any change to the model.

These are the classes of defect that do not announce themselves: a parameter
the client priced that the Monte Carlo silently freezes, a value the agent
engine computes that the aggregate engine ignores, a derived quantity left at
base while its inputs move. Each one was found by hand at least once. This
script means none of them has to be found by hand again.

    python scripts/audit_model.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from config import config as C
from config.overrides import MODEL_OVERRIDES
from src.detmodel import DetModel, load_params
from src.mcmodel import _match_triples, NOT_DRAWN, run_path
from src.tiermix import load_profile, lookup

fails, warns = [], []


def check(ok, msg, hard=True):
    (fails if hard else warns).append(msg) if not ok else None
    print(f"  [{'PASS' if ok else ('FAIL' if hard else 'WARN')}] {msg}")


print("=" * 78)
print("MODEL AUDIT")
print("=" * 78)

p = load_params()
raw = load_params(raw=True)

# ── 1. every priced band is drawn, or excluded with a reason ─────────────────
print("\n1. Priced uncertainty reaches the Monte Carlo")
with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "config", "scenario_map.json")) as f:
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
check(not frozen, f"{len(drawn)} of {len(banded)} banded parameters drawn; "
                  f"{len(NOT_DRAWN)} excluded with a stated reason")
for tbl, key in frozen:
    print(f"        FROZEN WITHOUT REASON: {tbl}  ->  {key}")

# ── 2. the two engines agree on what they share ──────────────────────────────
print("\n2. The agent engine's tier mix reaches the aggregate engine")
prof = load_profile()
tm = lookup(prof, p["persistency"], p["grid"]["months"], p["grid"]["period"])
e_on = DetModel(); e_on.p["_tiermix"] = tm; e_on.run()
e_off = DetModel(tiermix=False); e_off.run()
yrs = np.array(p["grid"]["year"])
g_on = float(e_on.out["ics_cost"][yrs == 7].sum())
g_off = float(e_off.out["ics_cost"][yrs == 7].sum())
check(abs(g_on - g_off) > 1.0,
      f"tier mix changes the giveback (flat {g_off:,.0f} vs computed {g_on:,.0f})")
o, _ = run_path(20270101)
check(isinstance(o["ics_rates"]["entry"], np.ndarray),
      "the Monte Carlo path uses the computed rates, not the flat ones")
check(isinstance(DetModel().out.get("x", None), type(None))
      and "_tiermix" in DetModel().p,
      "a plain DetModel() carries the tier mix, so no call site can forget it")
check("_tiermix" not in DetModel(p=load_params(raw=True), tiermix=False).p,
      "the equivalence test's engine deliberately does not")

# ── 3. derived quantities move with their inputs ─────────────────────────────
print("\n3. Derived quantities follow what they are derived from")
d = o["_draw"]
check(abs(d["monthly_churn"] - (1 - d["persistency"] ** (1 / 12))) < 1e-9,
      "monthly churn follows the drawn persistency")
check(abs(d["partner_aum"] - d.get("partner_users", p["partner_users"])
          * d["partner_adopt"] * d["partner_aum_user"]) < 1.0,
      "partner AUM follows its drawn components, including a drawn user base")
# asserted against the WORKBOOK's own definition, reproduced at its base values,
# not against the reconstruction formula - otherwise the check only proves the
# code agrees with itself. This is how a dropped term survived one audit pass.
_fam_m = 1 - (1 - d["family_cancel"]) ** (1 / 12)
check(abs(d["family_churn_monthly"] - (1 - (1 - _fam_m) * (1 - d["monthly_churn"]))) < 1e-6,
      "family churn combines cancellation AND SIP lapse, as the workbook does")
_rawp = load_params(raw=True)
_rm = 1 - (1 - _rawp["family_cancel"]) ** (1 / 12)
check(abs((1 - (1 - _rm) * (1 - _rawp["monthly_churn"])) - _rawp["family_churn_monthly"]) < 1e-4,
      "that definition reproduces the workbook's own value at its base inputs")

# ── 4. deliberate departures are declared, and excluded from equivalence ─────
print("\n4. Departures from the workbook are declared")
for k, v in MODEL_OVERRIDES.items():
    check(raw.get(k) != v, f"'{k}' departs from the workbook ({raw.get(k)} -> {v}) "
                           f"and is declared in config/overrides.py")
check(raw["persistency"] == 0.55,
      "the equivalence test still sees the untouched workbook value")

# ── 5. no parameter is referenced by the engine but absent ───────────────────
print("\n5. Every parameter the engine reads exists")
import re
src = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "src", "detmodel.py")).read()
hard = set(re.findall(r'p\["([a-z0-9_]+)"\]', src))
optional = set(re.findall(r'p\.get\("([a-z0-9_]+)"', src))
# a key read anywhere through .get() has a default and may be absent by design
# (the stress hooks: buyback_spread, panic_period, panic_share)
refs = hard | optional
missing = sorted(r for r in hard - optional if r not in p and not r.startswith("_"))
check(not missing, f"{len(hard)} required parameter references resolve; {len(optional)} optional hooks may be absent by design")
for m in missing:
    print(f"        MISSING: {m}")

# ── 6. the ladder and the workbook rates describe the same thing ─────────────
print("\n6. The benefit ladder is internally consistent")
from src.agentbook import LADDER
check(all(len(v) == 5 for v in LADDER.values()),
      "every ladder row has five rungs (none + four tiers)")
check(LADDER["entry_fee"][0] == C.ENTRY_FEE,
      f"the untiered entry fee equals the workbook's {C.ENTRY_FEE:.0%}")
check(all(np.all(np.diff(LADDER[k]) <= 1e-12) for k in ("entry_fee", "fx_margin")),
      "prices charged fall monotonically up the ladder")
check(all(np.all(np.diff(LADDER[k]) >= -1e-12) for k in ("family_disc", "ltv", "rewards")),
      "benefits given rise monotonically up the ladder")

# ── 7. the acquisition block is simulated, not inherited ────────────────────
print("\n7. Acquisition responds to the model, not to a spreadsheet formula")
from config.overrides import EXTRA_TRIPLES
from src.tiermix import SERIES

check(all(k in drawn for k in EXTRA_TRIPLES),
      f"the Phase 5 acquisition bands are drawn ({', '.join(EXTRA_TRIPLES)})")

# the ceiling must actually bind: doubling it must move cumulative acquisition
base_cum = float(DetModel().run()["cum_ever"][-1])
wide = DetModel(overrides={"ceiling_mult": 2.0}).run()["cum_ever"][-1]
check(wide > base_cum * 1.02,
      f"the addressable ceiling binds ({base_cum:,.0f} ever acquired, "
      f"{wide:,.0f} if the market is twice as big)")

# convexity must actually raise cost per customer at scale
flat = DetModel(overrides={"cac_conv_coef": 0.0}).run()
conv = DetModel().run()
check(conv["cum_ever"][-1] < flat["cum_ever"][-1] * 0.99,
      f"CAC convexity is live: same spend buys {conv['cum_ever'][-1]:,.0f} "
      f"customers, not {flat['cum_ever'][-1]:,.0f} (workbook D27, was retired to Phase 5)")

# referral capacity must reach the engine and must bite early
check("ref_mult" in SERIES and "ref_mult" in tm,
      "the agent book's referral capacity reaches the aggregate engine")
rm = np.asarray(tm["ref_mult"], dtype=float)
check(rm[:12].mean() < 0.85,
      f"a young book refers less than a mature one (first year at {rm[:12].mean():.2f} "
      f"of the workbook's flat assumption)")
check(abs(rm[-1] - 1.0) < 0.25,
      f"and the multiplier normalises to about 1.0 at maturity ({rm[-1]:.2f}), so "
      f"referral_rate keeps its quoted meaning")
det_ref = float(sum(DetModel().run()["region"][n]["ref_acq"].sum() for n in ("UAE", "Gulf", "India")))
flat_ref = float(sum(DetModel(tiermix=False).run()["region"][n]["ref_acq"].sum()
                     for n in ("UAE", "Gulf", "India")))
check(det_ref < flat_ref * 0.99,
      f"and it changes referral acquisition ({det_ref:,.0f} vs {flat_ref:,.0f} flat)")

print("\n" + "=" * 78)
print(f"{'AUDIT PASSED' if not fails else 'AUDIT FAILED'}  "
      f"({len(fails)} failures, {len(warns)} warnings)")
print("=" * 78)
sys.exit(1 if fails else 0)
