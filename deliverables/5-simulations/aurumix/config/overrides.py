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

    # CAC convexity, switched ON. The workbook's D27 left cost per customer
    # LINEAR and retired the convexity curve to "a scenario switch defaulting
    # OFF, calibration deferred to Phase 5". This is Phase 5.
    #
    # Left off, the model spends 90k in year one and 1.65m in year seven while
    # cost per acquired customer FALLS by a third. That is only true while the
    # cheap channels last. Past them, reach costs more per head: the marginal
    # customer is further from the message and slower to convert.
    #
    #   cac_effective = cac_ramp x [1 + coef x (monthly regional spend / ref)^exp]
    #
    # Form and constants carried over from the workbook's own retired curve
    # (coef 0.35, ref 60,000, exponent 0.7), applied to each region's own spend
    # because you exhaust UAE channels by spending in the UAE. The coefficient
    # is banded and drawn, so the raise number prices the uncertainty rather
    # than the point estimate. This is judgement, not measurement.
    "cac_conv_coef": 0.35,
    "cac_conv_ref": 60000.0,
    "cac_conv_exp": 0.7,

    # Addressable-market ceiling. The workbook's three ceilings are a funnel of
    # population x banked x interested x reachable, and the client has confirmed
    # the filter percentages are unsourced. India already runs to 85% of its
    # ceiling by year seven, so this number is close to binding on the whole
    # model and cannot stay a point estimate. Multiplier, drawn per path.
    "ceiling_mult": 1.0,
}

# Three compounding unsourced filters. A 0.60x to 1.55x band on their product
# is the honest spread, not a tight one. Aggressive is the wider market.
CEILING_TRIPLE = [1.0, 1.55, 0.60]

# Convexity strength. Aggressive means the cheap channels last longer.
CAC_CONV_TRIPLE = [0.35, 0.15, 0.60]

# Bands that exist only because Phase 5 added the parameter. They are NOT in
# the workbook's scenario table and must not be written into it, because that
# table is what the equivalence test reads. The Monte Carlo picks them up from
# here instead, so they are drawn like any other banded parameter.
EXTRA_TRIPLES = {
    "ceiling_mult": CEILING_TRIPLE,
    "cac_conv_coef": CAC_CONV_TRIPLE,
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
