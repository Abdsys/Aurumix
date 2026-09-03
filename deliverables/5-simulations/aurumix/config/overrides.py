"""
Deliberate departures from the Phase 4 workbook.

The ported engine reads its parameters from the calculated workbook, so that
the equivalence test can prove the port is faithful. Anything the simulation
changes ON PURPOSE belongs here, not in params.json, and must be:

  - applied EVERYWHERE except the equivalence test, and
  - listed in the results document as a departure, with its reason.

The equivalence test deliberately ignores this file. That is what keeps
"the port is broken" and "we changed our mind" as separate failures.
"""

MODEL_OVERRIDES = {
    # Persistency at month 13. The workbook carries 0.55, whose validation file
    # was deleted from the repo before Phase 5. Anchored 2026-09-03 to Indian
    # life insurance persistency, measured at the same checkpoints:
    #   IRDAI Handbook on Indian Insurance Statistics 2024-25, via the Ministry
    #   of Finance answer to Rajya Sabha USQ 1040(E): 13th month persistency
    #   across life insurers 59.68% to 83.22%, industry average about 63%.
    # We take the LEVEL (63%) and reject the SHAPE. Indian life curves flatten
    # after year one because surrender penalties punish quitting; a gold saver
    # forfeits nothing, so ours keeps its steeper decline to ~27% at M61.
    "persistency": 0.63,
}

# Scenario band for persistency, same +/-0.10 width as the workbook's own.
# 0.73 sits inside the published IRDAI range; 0.53 sits below its floor, which
# is the right side to err on for the conservative case.
PERSISTENCY_TRIPLE = [0.63, 0.73, 0.53]


def apply(params):
    """Return a copy of params with the deliberate departures applied."""
    p = dict(params)
    p.update(MODEL_OVERRIDES)
    p["monthly_churn"] = 1.0 - p["persistency"] ** (1.0 / 12.0)
    t = dict(p.get("scenario_triples", {}))
    for k in list(t):
        if k.startswith("Persistency"):
            t[k] = PERSISTENCY_TRIPLE
    p["scenario_triples"] = t
    return p
