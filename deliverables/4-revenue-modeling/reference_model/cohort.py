"""Cohort engine: five-state population machine on two axes, behavioural tracks,
and survival calibration.

TWO AXES (the v1.0 correction):
  Payment axis:  CONTRIBUTING -> REDUCED -> LAPSED, with DORMANT as a hard
                 absorbing boundary at 12 consecutive silent periods.
  Balance  axis: HOLDING (grams > 0) vs CLOSED (grams = 0).

CLOSED is the ONLY true exit from AUM, custody cost and screening cost.
A lapsed account keeps its gold, keeps a permanent ICS floor of 25, stays in
custody, stays in the B2B AUM base and stays in continuous AML screening.

SURVIVAL EMERGES from archetype heterogeneity plus a common background hazard.
A single constant hazard cannot fit a convex-declining 5-point curve; and a
pure mixture of archetype hazards produces a tail that is far too fat. The
two-component form (own hazard + background) is what makes the arithmetic work.
"""
from __future__ import annotations

import numpy as np

# IMPORTANT: import the MODULE, never `from params import NAME`.
# A `from ... import` binds the object into this module's namespace at import
# time, so a scenario override applied with setattr(params, NAME, value) would
# rebind params.NAME while this module kept pointing at the original object.
# That silently made S27 (ARCHETYPE_MIX) inert in the tornado - it reported a
# swing of exactly 0.0 because the flex never reached the cohort engine.
# Every parameter read below goes through P.<NAME> so overrides always apply.
import params as P

# Five population states
STATES = ["CONTRIBUTING", "REDUCED", "LAPSED_HOLDING", "DORMANT", "CLOSED"]

# ---------------------------------------------------------------------------
# Driver map: which population each revenue and cost line scales with.
# Explicit, because the audit found AUM scaling with active accounts.
# ---------------------------------------------------------------------------

DRIVER_MAP = {
    # line                       driver population
    "stream1_entry_fee":        "CONTRIBUTING + REDUCED",
    "stream1_spot":             "CONTRIBUTING + REDUCED + LAPSED_HOLDING",
    "stream2_interchange":      "carded (tier>=Gold), see LAPSED_KEEPS_CARD",
    "stream3_family":           "CONTRIBUTING + REDUCED",
    "stream4_cardholder_fees":  "carded (tier>=Gold), see LAPSED_KEEPS_CARD",
    "stream5_credit":           "carded Gold+ with seasoned collateral",
    "stream6_b2b":              "partner AUM (independent of retail states)",
    "cost_custody":             "ALL HOLDING (incl. LAPSED_HOLDING, DORMANT)",
    "cost_screening":           "ALL HOLDING (continuous AML)",
    "cost_rail":                "CONTRIBUTING + REDUCED (collection events)",
    "cost_redemption":          "ALL HOLDING",
    "aum_grams":                "ALL HOLDING (NOT active accounts)",
}


class ArchetypeTrack:
    """One deterministic behavioural track within a vintage.

    Deliberately deterministic: the payment path is the archetype's expected
    pattern, not a random draw. No RNG anywhere in the core engine.
    """

    def __init__(self, archetype, withdraw_rate: float, withdraw_weight: float):
        self.archetype = archetype
        self.withdraw_rate = withdraw_rate
        self.weight = archetype.weight * withdraw_weight
        self.name = f"{archetype.name}|wd{withdraw_rate:.2f}"

    def pays_in_month(self, m: int) -> bool:
        """Deterministic payment pattern reproducing the archetype's rate."""
        p = self.archetype.pay_prob
        if p >= 0.99:
            return True
        if abs(p - 0.55) < 0.01:          # alternating misser: pay-miss-pay-miss
            return m <= P.GATE_RUN_REQUIRED or (m % 2 == 1)
        # Occasional/reducer/early: spread misses evenly at rate (1-p).
        if p >= 0.90:
            period = max(2, int(round(1.0 / max(1e-9, 1.0 - p))))
            return m <= P.GATE_RUN_REQUIRED or (m % period != 0)
        period = max(2, int(round(1.0 / max(1e-9, 1.0 - p))))
        return m % period != 0

    def hazard(self, m: int) -> float:
        h = self.archetype.own_hazard
        if self.archetype.name == "Early lapser" and m >= P.EARLY_LAPSER_DECAY_MONTH:
            h = P.EARLY_LAPSER_POST_HAZARD
        return h


def build_tracks(mode: str = "Base") -> list[ArchetypeTrack]:
    """Cross payment archetypes with withdrawal buckets.

    Withdrawal buckets are collapsed to three cells straddling the 30% kink so
    total tracks stay tractable (5 archetypes x 3 buckets = 15 per segment,
    close to the ~12 target and far below 5 x 6 = 30).
    """
    mix = P.ARCHETYPE_MIX[mode]
    buckets = P.WITHDRAWAL_BUCKETS[mode]

    # Collapse to below-kink / at-kink / above-kink.
    below = [(r, w) for r, w in buckets if r <= 0.10]
    at = [(r, w) for r, w in buckets if 0.10 < r <= 0.30]
    above = [(r, w) for r, w in buckets if r > 0.30]

    def collapse(group):
        wt = sum(w for _, w in group)
        if wt <= 0:
            return (0.0, 0.0)
        rate = sum(r * w for r, w in group) / wt
        return (rate, wt)

    collapsed = [collapse(below), collapse(at), collapse(above)]
    collapsed = [(r, w) for r, w in collapsed if w > 0]

    tracks = []
    for a in mix["archetypes"]:
        for rate, wt in collapsed:
            tracks.append(ArchetypeTrack(a, rate, wt))
    return tracks


def survival_curve(mode: str = "Base", horizon: int = 120,
                   background: float | None = None,
                   weights: dict | None = None) -> np.ndarray:
    """Aggregate survival that EMERGES from the archetype mix.

    Returns S[0..horizon] where S[0] = 1.0. Survival here is the share of the
    vintage still on the payment axis (CONTRIBUTING or REDUCED) - i.e. not
    LAPSED. It is NOT the share still holding gold, which is far higher.
    """
    mix = P.ARCHETYPE_MIX[mode]
    bg = mix["background_hazard"] if background is None else background

    surv = np.zeros(horizon + 1)
    surv[0] = 1.0
    alive = {a.name: (weights or {}).get(a.name, a.weight) for a in mix["archetypes"]}

    for m in range(1, horizon + 1):
        total = 0.0
        for a in mix["archetypes"]:
            own = a.own_hazard
            if a.name == "Early lapser" and m >= P.EARLY_LAPSER_DECAY_MONTH:
                own = P.EARLY_LAPSER_POST_HAZARD
            h = min(0.999, own + bg)
            alive[a.name] *= (1.0 - h)
            total += alive[a.name]
        surv[m] = total
    return surv


def fit_survival(mode: str = "Base", anchors: dict | None = None,
                 horizon: int = 120):
    """Calibrate archetype weights + background hazard to the survival anchors.

    Calibration order per the parameter file (the three levers are close to
    orthogonal in this order):
      1. early-lapser weight   <- M13
      2. background hazard     <- M49/M61
      3. perfect-payer weight  <- M37 midpoint

    Returns (fitted_weights, fitted_background, fit_table).
    """
    from scipy.optimize import minimize

    anchors = anchors or P.SURVIVAL_ANCHORS
    mix = P.ARCHETYPE_MIX[mode]
    names = [a.name for a in mix["archetypes"]]
    w0 = np.array([a.weight for a in mix["archetypes"]])
    bg0 = mix["background_hazard"]

    def unpack(x):
        w = np.abs(x[:len(names)])
        w = w / w.sum()
        return dict(zip(names, w)), abs(x[-1])

    def loss(x):
        w, bg = unpack(x)
        s = survival_curve(mode, horizon, background=bg, weights=w)
        return sum((s[m] - t) ** 2 for m, t in anchors.items())

    x0 = np.concatenate([w0, [bg0]])
    res = minimize(loss, x0, method="Nelder-Mead",
                   options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-14})
    w, bg = unpack(res.x)

    s = survival_curve(mode, horizon, background=bg, weights=w)
    s0 = survival_curve(mode, horizon)
    fit = [{"anchor_month": m, "target": t,
            "sourced_weights": round(float(s0[m]), 4),
            "calibrated": round(float(s[m]), 4),
            "residual_pp": round(float(s[m] - t) * 100, 2),
            "sourced_residual_pp": round(float(s0[m] - t) * 100, 2)}
           for m, t in sorted(anchors.items())]
    return w, bg, fit


def lapse_split(mode: str, m: int, track: ArchetypeTrack, background: float):
    """Split a track's monthly attrition into reduction-capture vs true lapse.

    Reduction capture applies ONLY to affordability-driven lapse (the
    occasional-misser and reducer archetypes) - never to the early lapser and
    never to the background hazard, per S28.
    """
    own = track.hazard(m)
    capture = P.REDUCTION_CAPTURE[mode]
    affordability = track.archetype.name in ("Occasional misser", "Reducer")
    to_reduced = own * capture if affordability else 0.0
    to_lapsed = (own - to_reduced) + background
    return to_reduced, min(0.999, to_lapsed)


class Vintage:
    """One acquisition vintage of one segment, tracked by behavioural track.

    Carries the five-state population and the grams stock. Conservation is
    asserted every period by the caller.
    """

    def __init__(self, segment: str, origin_month: int, size: float,
                 tracks: list[ArchetypeTrack], mode: str):
        self.segment = segment
        self.origin = origin_month
        self.mode = mode
        self.tracks = tracks
        self.bg = P.ARCHETYPE_MIX[mode]["background_hazard"]
        # Population by track and state
        self.pop = {t.name: {"CONTRIBUTING": size * t.weight, "REDUCED": 0.0,
                             "LAPSED_HOLDING": 0.0, "DORMANT": 0.0, "CLOSED": 0.0}
                    for t in self.tracks}
        self.grams = {t.name: 0.0 for t in self.tracks}
        self.grams_history: dict[str, list[float]] = {t.name: [] for t in self.tracks}
        self.acquired_12m: dict[str, list[float]] = {t.name: [] for t in self.tracks}
        self.ics = {}
        from ics import ICSAccount
        for t in self.tracks:
            self.ics[t.name] = ICSAccount()

    @property
    def age(self) -> int:
        return 0

    def total_in(self, states) -> float:
        return sum(sum(self.pop[t.name][s] for s in states) for t in self.tracks)

    def step_population(self, m: int) -> dict:
        """Advance the payment axis one month. Returns the flow record.

        AGE CONVENTION, and it was wrong before D23 found it.
        `step_population` is first called in the month AFTER origination, so the
        first hazard an account ever faces belongs to age 1, not age 2. The old
        `m - origin + 1` made that first step age 2, which shifted every
        age-dependent hazard one month earlier than `survival_curve` in this
        same module applied it. The two disagreed by ~8% on the payment axis by
        M84 - invisible until the D23 convolution was tested against the
        triangle, because the mismatch only bites where a hazard is a function
        of age (the early-lapser decay at M13).
        """
        age = m - self.origin
        flows = {"to_reduced": 0.0, "to_lapsed": 0.0, "to_dormant": 0.0}
        red_mult = P.REDUCED_HAZARD_MULT[self.mode]

        for t in self.tracks:
            p = self.pop[t.name]
            to_red_rate, to_lapse_rate = lapse_split(self.mode, age, t, self.bg)

            # CONTRIBUTING -> REDUCED / LAPSED_HOLDING
            c = p["CONTRIBUTING"]
            mv_red = c * to_red_rate
            mv_lapse = c * to_lapse_rate
            p["CONTRIBUTING"] = c - mv_red - mv_lapse

            # REDUCED carries elevated hazard (S30) but cannot re-reduce.
            r = p["REDUCED"]
            r_lapse = r * min(0.999, to_lapse_rate * red_mult)
            p["REDUCED"] = r - r_lapse + mv_red

            p["LAPSED_HOLDING"] += mv_lapse + r_lapse
            flows["to_reduced"] += mv_red
            flows["to_lapsed"] += mv_lapse + r_lapse

            # Dormancy: hard absorbing boundary at 12 consecutive silent periods.
            # A lapsed account is silent by definition, so a fixed share of the
            # lapsed stock crosses the boundary each month once past 12 months.
            if age > 12:
                d = p["LAPSED_HOLDING"] / 12.0
                p["LAPSED_HOLDING"] -= d
                p["DORMANT"] += d
                flows["to_dormant"] += d

            # ICS clock advances for accounts still on the payment axis.
            self.ics[t.name].step(t.pays_in_month(age))
        return flows
