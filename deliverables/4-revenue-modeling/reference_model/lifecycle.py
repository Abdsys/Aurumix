"""D23: lifecycle curves and the convolution engine.

THE SHAPE OF THE CHANGE
-----------------------
The old engine carried a VINTAGE TRIANGLE: every acquisition month spawned a
live `Vintage` object holding its own population by behavioural track, and every
period walked every surviving vintage. That is correct but it is O(months^2 x
tracks) and, more importantly, it cannot be transcribed into a spreadsheet - the
workbook this model is a reference for has no way to hold ten thousand objects.

D23 replaces it with a CONVOLUTION. Every lifecycle quantity is expressed as a
pure function of months-since-origination:

    curve(a)  for a = 1 .. HORIZON_MONTHS

and the population at period t is the inner product of the acquisition vector
with the curve, read backwards:

    live(t) = SUM over s = 1..t of  acq(s) x curve(t - s + 1)

THREE PROPERTIES THAT ARE LOAD-BEARING
--------------------------------------
1. THE CURVES READ NO PERIOD-t QUANTITY. A curve is a function of AGE alone.
   The moment a curve reads a period-t quantity - this month's book size, this
   month's tier mix - the convolution stops being a convolution and becomes a
   circular reference. Check 7 asserts the range terminates at t.

2. THE RANGE TERMINATES AT THE CURRENT PERIOD. `acq(s)` for s > t has not
   happened yet. Running the range to the end of the sheet reads future
   acquisition into today's population, which is the single easiest error to
   make in the spreadsheet transcription and the hardest to see.

3. AN ANNUAL COLUMN CONVOLVES AT EACH OF ITS TWELVE MONTHS AND THEN AGGREGATES.
   It NEVER convolves an annual aggregate acquisition figure. Doing that
   collapses twelve first-passage months into one and destroys the gate
   distribution: the run-of-6 gate resolves at a mean of M8.1 with a real spread
   either side, and an annual convolution would place the entire year's intake
   at a single age. Check 8 asserts the decomposition.

EQUIVALENCE
-----------
The vintage triangle is KEPT, in cohort.py, as the equivalence harness. Both
engines must agree; `equivalence_test()` below reports the residual.
"""
from __future__ import annotations

import numpy as np

import params as P


# ---------------------------------------------------------------------------
# The curves: pure functions of months-since-origination
# ---------------------------------------------------------------------------

class LifecycleCurves:
    """All age-indexed curves for one scenario mode, computed once to M84.

    Every array is indexed [age] with age = 1..H, and index 0 is a zero pad so
    the arithmetic reads naturally. No curve point is held, frozen or
    extrapolated: M84 is the maximum tenure any cohort can have in a seven-year
    model, so the curve is computed to exactly that and no further.
    """

    def __init__(self, mode: str = "Base", horizon: int | None = None,
                 weights: dict | None = None, background: float | None = None):
        self.mode = mode
        self.H = horizon or P.HORIZON_MONTHS
        mix = P.ARCHETYPE_MIX[mode]
        self.archetypes = mix["archetypes"]
        self.bg = mix["background_hazard"] if background is None else background
        self.weights = {a.name: (weights or {}).get(a.name, a.weight)
                        for a in self.archetypes}
        self._build()

    # -- archetype state curves ------------------------------------------
    def _build(self):
        H = self.H
        names = [a.name for a in self.archetypes]
        capture = P.REDUCTION_CAPTURE[self.mode]
        red_mult = P.REDUCED_HAZARD_MULT[self.mode]

        # Per-archetype population on the payment axis, split by state.
        self.contributing = {n: np.zeros(H + 1) for n in names}
        self.reduced = {n: np.zeros(H + 1) for n in names}
        self.lapsed = {n: np.zeros(H + 1) for n in names}
        self.dormant = {n: np.zeros(H + 1) for n in names}

        for a in self.archetypes:
            n = a.name
            w = self.weights[n]
            c, r, l, d = w, 0.0, 0.0, 0.0
            self.contributing[n][0] = c
            affordability = n in ("Occasional misser", "Reducer")
            for age in range(1, H + 1):
                own = a.own_hazard
                if n == "Early lapser" and age >= P.EARLY_LAPSER_DECAY_MONTH:
                    own = P.EARLY_LAPSER_POST_HAZARD
                to_red = own * capture if affordability else 0.0
                to_lapse = min(0.999, (own - to_red) + self.bg)

                mv_red = c * to_red
                mv_lapse = c * to_lapse
                c = c - mv_red - mv_lapse
                r_lapse = r * min(0.999, to_lapse * red_mult)
                r = r - r_lapse + mv_red
                l += mv_lapse + r_lapse
                # Dormancy: a hard absorbing boundary at 12 silent periods. A
                # lapsed account is silent by definition, so a fixed share of
                # the lapsed stock crosses each month once past age 12.
                if age > 12:
                    mv_d = l / 12.0
                    l -= mv_d
                    d += mv_d
                self.contributing[n][age] = c
                self.reduced[n][age] = r
                self.lapsed[n][age] = l
                self.dormant[n][age] = d

        # Aggregate curves, weighted across archetypes.
        self.curve_contributing = sum(self.contributing.values())
        self.curve_reduced = sum(self.reduced.values())
        self.curve_lapsed = sum(self.lapsed.values())
        self.curve_dormant = sum(self.dormant.values())
        self.curve_holding = (self.curve_contributing + self.curve_reduced
                              + self.curve_lapsed + self.curve_dormant)
        # Survival on the payment axis: contributing + reduced.
        self.curve_survival = self.curve_contributing + self.curve_reduced

        self._build_gate()
        self._build_tier()

    # -- the gate ---------------------------------------------------------
    def _build_gate(self):
        """Run-of-6 FIRST-PASSAGE distribution, per archetype, by age.

        This is the one piece D22 explicitly does NOT collapse. The gate decides
        who gets a tier AT ALL, and it is a distribution, not a date: an account
        that misses month 4 cannot complete a run of six before month 9. The
        never-gated population (persona H) falls straight out of it and pays the
        full undiscounted fee forever.

        Solved as a Markov chain on the run-length state 0..5 from each
        archetype's payment PROBABILITY, with survival applied each month so an
        account that lapses before completing a run never gates.
        """
        H = self.H
        R = P.GATE_RUN_REQUIRED
        self.gated_share = {}          # [age] unconditional: ever-gated mass
        self.gated_of_survivors = {}   # [age] P(gated | still alive at age)
        self.gate_arrivals = {}        # [age] newly-gated mass, for the mean

        for a in self.archetypes:
            p = a.pay_prob
            # Joint state over (run length 0..R-1) for the not-yet-gated, plus a
            # single absorbing pool for the already-gated. Both pools face the
            # SAME hazard, so survival and gating are tracked together and the
            # conditional share falls out directly rather than being recovered
            # by dividing two unconditional quantities - which is what produced
            # gated shares above 1.0 (5.1x for the occasional misser at M84).
            ungated = np.zeros(R)
            ungated[0] = 1.0
            gated_alive = 0.0
            gated_ever = 0.0
            g_uncond = np.zeros(H + 1)
            g_cond = np.zeros(H + 1)
            arrivals = np.zeros(H + 1)

            for age in range(1, H + 1):
                own = a.own_hazard
                if a.name == "Early lapser" and age >= P.EARLY_LAPSER_DECAY_MONTH:
                    own = P.EARLY_LAPSER_POST_HAZARD
                surv = 1.0 - min(0.999, own + self.bg)

                nxt = np.zeros(R)
                newly = 0.0
                for k in range(R):
                    mass = ungated[k]
                    if mass <= 0.0:
                        continue
                    alive = mass * surv
                    if k + 1 >= R:
                        newly += alive * p          # the run completes here
                    else:
                        nxt[k + 1] += alive * p
                    nxt[0] += alive * (1.0 - p)     # a miss resets the run
                ungated = nxt
                gated_alive = gated_alive * surv + newly
                gated_ever += newly

                alive_total = float(ungated.sum()) + gated_alive
                g_uncond[age] = gated_ever
                g_cond[age] = (gated_alive / alive_total) if alive_total > 1e-12 else 0.0
                arrivals[age] = newly

            self.gated_share[a.name] = g_uncond
            self.gated_of_survivors[a.name] = g_cond
            self.gate_arrivals[a.name] = arrivals

        # Book-level: share of an ORIGINAL vintage that has gated by each age.
        self.curve_gated = sum(self.weights[a.name] * self.gated_share[a.name]
                               for a in self.archetypes)

    # -- D22: the tenure -> tier lookup -----------------------------------
    def _build_tier(self):
        """Tier by (ARCHETYPE x WITHDRAWAL BUCKET) by TENURE, then weighted.

        This is D22's collapsed lookup and it is the LIVE path.

        WHAT IT PRESERVES, because dropping any of these changes the answer:

        1. THE GATE. An account below the gate has no tier at all ("None"),
           pays the full undiscounted fee and earns no benefit. That population
           is first-order - ~46% of a vintage never gates and ~17% of the live
           book at M84 is still ungated - and it is read straight off the
           run-of-6 first-passage curve, never assumed at M6.

        2. PER-ARCHETYPE COMPUTATION. Tier is computed for each archetype and
           THEN weighted. Averaging the score and applying the threshold second
           is wrong by Jensen: the threshold is a step function, so the mean of
           the tiers is not the tier of the mean.

        3. THE WITHDRAWAL DIMENSION. Retention is a MULTIPLIER with veto power:
           a saver who sells more than the 30% allowance has the whole score cut
           proportionally, and the cut is large enough to move tiers. Building
           the lookup on payment behaviour alone promoted 62% of the M84 book to
           Platinum and 19% to Sovereign against the brief's own T4/T5 of 63%
           Gold-plus and 4.4% Sovereign. The buckets straddling the 30% kink
           (S31) are therefore crossed into the lookup, not averaged out.

        WHAT IT DROPS: the exact-fraction score arithmetic itself, and the
        month-by-month trailing-12 payment pattern. Those stay in ics.py as the
        validation harness. The rung ages below are READ OFF that harness - each
        (archetype, bucket) cell is run through the full ICS engine once and the
        first month it reaches each tier is recorded - so the lookup is a
        compression of the full engine, not an independent guess at it.
        """
        H = self.H
        from cohort import build_tracks
        from ics import ICSAccount

        self.cells = []          # (archetype_name, weight_within_archetype, ladder)
        by_arch: dict = {}
        for tr in build_tracks(self.mode):
            acct = ICSAccount()
            rungs = {}
            for m in range(1, H + 1):
                acct.step(tr.pays_in_month(m))
                t = acct.tier(min(1.0, tr.withdraw_rate))
                if t != "None" and t not in rungs:
                    rungs[t] = m
            # Deterministic patterns gate every track at M6, so the ladder ages
            # are measured from M6 - the gate offset itself comes from the
            # first-passage curve at read time, which is the honest source.
            ladder = sorted(((max(0, m - P.GATE_RUN_REQUIRED), t)
                             for t, m in rungs.items()), key=lambda x: x[0])
            by_arch.setdefault(tr.archetype.name, []).append(
                (tr.weight / max(1e-12, tr.archetype.weight), ladder))
        self.tier_cells = by_arch

        # Flatten to tier-share-by-tenure per archetype, so the read is O(1).
        self.tier_by_tenure = {}
        for name, cells in by_arch.items():
            arr = []
            for since in range(H + 1):
                shares = {t: 0.0 for t in P.TIER_ORDER}
                for w, ladder in cells:
                    tier = "Silver" if ladder else "Silver"
                    tier = "None"
                    for at, t in ladder:
                        if since >= at:
                            tier = t
                    if tier == "None":
                        tier = "Silver"      # gated but not yet at a rung
                    shares[tier] += w
                arr.append(shares)
            self.tier_by_tenure[name] = arr

    def tier_mix_at_age(self, age: int) -> dict:
        """Tier shares of an ORIGINAL vintage at `age`, summing to the survivors.

        Gated: the ungated share of each archetype sits in tier "None" - it
        holds gold, it pays the full fee, and it earns nothing. Structurally the
        highest-margin retail account in the book.
        """
        age = max(0, min(age, self.H))
        out = {t: 0.0 for t in P.TIER_ORDER}
        for a in self.archetypes:
            alive = (self.contributing[a.name][age] + self.reduced[a.name][age])
            if alive <= 0:
                continue
            share_gated = self.gated_of_survivors[a.name][age]
            gate_age = self.mean_gate_age(a.name)
            since = max(0, age - int(round(gate_age)))
            shares = self.tier_by_tenure[a.name][min(since, self.H)]
            for t, w in shares.items():
                out[t] += alive * share_gated * w
            out["None"] += alive * (1.0 - share_gated)
        return out

    def mean_gate_age(self, archetype_name: str) -> float:
        newly = self.gate_arrivals[archetype_name]
        tot = float(newly.sum())
        if tot <= 1e-12:
            return float(self.H)
        ages = np.arange(len(newly))
        return float((newly * ages).sum() / tot)

    def gate_statistics(self) -> dict:
        rows = []
        for a in self.archetypes:
            ever = float(self.gated_share[a.name][self.H])
            rows.append({
                "archetype": a.name, "weight": self.weights[a.name],
                "pay_prob": a.pay_prob,
                "monthly_hazard": round(min(0.999, a.own_hazard + self.bg), 4),
                "ever_gate_prob": round(ever, 4),
                "mean_gate_month": round(self.mean_gate_age(a.name), 1)})
        ever = sum(r["weight"] * r["ever_gate_prob"] for r in rows)
        exp_gate = (sum(r["weight"] * r["ever_gate_prob"] * r["mean_gate_month"]
                        for r in rows) / max(1e-9, ever))
        return {"by_archetype": rows, "ever_gate_share": ever,
                "never_gate_share": 1.0 - ever, "expected_gate_month": exp_gate}


# ---------------------------------------------------------------------------
# The convolution
# ---------------------------------------------------------------------------

def convolve(acq: np.ndarray, curve: np.ndarray, t: int) -> float:
    """SUM over s=1..t of acq(s) x curve(t - s).

    `acq` is 1-indexed with acq[0] unused; `curve` is indexed by AGE with
    curve[0] the state at origination.

    ⚠ THE AGE OFFSET IS `t - s`, NOT `t - s + 1`. A vintage acquired in month t
    is observed in month t at age ZERO - it has not yet faced a hazard. Using
    `t - s + 1` ages every cohort by one month, which understated the payment
    axis by ~8% at M1 decaying to ~4% by M20 in the equivalence test. The error
    is largest early, exactly where the acquisition ramp is steepest and where
    the gate has not yet resolved, so it is worst in the months the 29-column
    view reports monthly.

    RANGE TERMINATES AT t (check 7): the slice acq[1:t+1] cannot reach a month
    that has not happened, and the curve is reversed against it so the oldest
    vintage reads the highest age.
    """
    if t <= 0:
        return 0.0
    a = acq[1:t + 1]
    c = curve[0:t][::-1]
    return float(np.dot(a, c))


def convolve_path(acq: np.ndarray, curve: np.ndarray, horizon: int) -> np.ndarray:
    """The whole convolution path, 1-indexed, one call per period.

    Written as an explicit loop rather than np.convolve so the range-termination
    property is visible in the code and testable, which is the point: this
    function is the reference for a spreadsheet SUMPRODUCT.
    """
    out = np.zeros(horizon + 1)
    for t in range(1, horizon + 1):
        out[t] = convolve(acq, curve, t)
    return out


def annual_convolution(acq: np.ndarray, curve: np.ndarray, year: int,
                       rule: str = P.VIEW_RULE_FLOW) -> float:
    """An annual column, built from its TWELVE CONSTITUENT MONTHS.

    NEVER convolves an annual aggregate. Check 8 asserts that this equals the
    sum (flow) or last (snapshot) of the twelve monthly convolutions, and
    `annual_aggregate_error()` below measures what the wrong way would cost.
    """
    months = range((year - 1) * 12 + 1, year * 12 + 1)
    vals = [convolve(acq, curve, t) for t in months]
    if rule == P.VIEW_RULE_SNAPSHOT:
        return vals[-1]
    return float(sum(vals))


def annual_aggregate_error(acq: np.ndarray, curve: np.ndarray,
                           year: int) -> dict:
    """What convolving an annual aggregate acquisition figure would cost.

    Reported, not used. The wrong form places the entire year's intake at a
    single age, which collapses twelve first-passage months into one.
    """
    right = annual_convolution(acq, curve, year, P.VIEW_RULE_SNAPSHOT)
    lo, hi = (year - 1) * 12 + 1, year * 12
    annual_acq = float(acq[lo:hi + 1].sum())
    mid_age = max(1, hi - (lo + hi) // 2 + 1)
    wrong = annual_acq * curve[min(mid_age, len(curve) - 1)]
    return {"year": year, "correct": right, "annual_aggregate": wrong,
            "error_abs": wrong - right,
            "error_pct": (wrong - right) / right * 100 if right else 0.0}


# ---------------------------------------------------------------------------
# Equivalence harness: convolution vs the vintage triangle
# ---------------------------------------------------------------------------

def equivalence_test(mode: str = "Base", horizon: int | None = None) -> dict:
    """Run both engines on the same acquisition vector and report the residual.

    The triangle walks live Vintage objects month by month; the convolution
    reads age-indexed curves. If D23 is a faithful restatement they agree to
    floating-point noise. If they do not, D23 has changed the answer and the
    difference is the thing to explain.
    """
    from cohort import Vintage, build_tracks

    H = horizon or P.HORIZON_MONTHS
    rng = np.random.default_rng(20260820)
    acq = np.zeros(H + 1)
    acq[1:] = 100.0 * (1.0 + 0.02 * np.arange(H)) * (
        1.0 + 0.15 * rng.standard_normal(H))
    acq = np.maximum(acq, 0.0)

    curves = LifecycleCurves(mode, H)
    tracks = build_tracks(mode)

    # Triangle
    vintages = []
    tri_contrib = np.zeros(H + 1)
    tri_hold = np.zeros(H + 1)
    for t in range(1, H + 1):
        if acq[t] > 0:
            vintages.append(Vintage("R1", t, float(acq[t]), tracks, mode))
        for v in vintages:
            if v.origin == t:
                continue
            v.step_population(t)
        tri_contrib[t] = sum(v.total_in(["CONTRIBUTING", "REDUCED"])
                             for v in vintages)
        tri_hold[t] = sum(v.total_in(["CONTRIBUTING", "REDUCED",
                                      "LAPSED_HOLDING", "DORMANT"])
                          for v in vintages)

    con_contrib = convolve_path(acq, curves.curve_survival, H)
    con_hold = convolve_path(acq, curves.curve_holding, H)

    def resid(a, b):
        den = np.maximum(np.abs(b[1:]), 1e-9)
        rel = np.abs(a[1:] - b[1:]) / den
        return {"max_abs": float(np.max(np.abs(a[1:] - b[1:]))),
                "max_rel_pct": float(np.max(rel) * 100),
                "mean_rel_pct": float(np.mean(rel) * 100),
                "terminal_convolution": float(a[H]),
                "terminal_triangle": float(b[H])}

    out = {"contributing_plus_reduced": resid(con_contrib, tri_contrib),
           "holding": resid(con_hold, tri_hold)}
    out["max_rel_pct"] = max(out["contributing_plus_reduced"]["max_rel_pct"],
                             out["holding"]["max_rel_pct"])
    out["pass"] = out["max_rel_pct"] < 1e-6
    return out


def annual_decomposition_check(mode: str = "Base") -> list:
    """Check 8, run explicitly: every annual column decomposes into 12 months."""
    H = P.HORIZON_MONTHS
    curves = LifecycleCurves(mode, H)
    acq = np.zeros(H + 1)
    acq[1:] = 100.0
    rows = []
    for y in P.VIEW_ANNUAL_YEARS:
        months = range((y - 1) * 12 + 1, y * 12 + 1)
        monthly = [convolve(acq, curves.curve_survival, t) for t in months]
        col = annual_convolution(acq, curves.curve_survival, y,
                                 P.VIEW_RULE_FLOW)
        err = annual_aggregate_error(acq, curves.curve_survival, y)
        rows.append({
            "year": y,
            "sum_of_12_monthly_convolutions": sum(monthly),
            "annual_column": col,
            "residual": col - sum(monthly),
            "pass": abs(col - sum(monthly)) < 1e-9,
            "annual_aggregate_would_err_pct": round(err["error_pct"], 2)})
    return rows


# ---------------------------------------------------------------------------
# D22 collapse-safety gate: the collapsed lookup against the full ICS ladder
# ---------------------------------------------------------------------------

def collapse_cost(tier_counts_by_year: dict, spend_share_by_tier: dict,
                  gross_profit_by_year: dict, activation: float,
                  spend_per_card_usd: float, pm_share_by_year: dict) -> list:
    """Measure what D22's flat-Gold collapse costs, year by year.

    THE MEASUREMENT. The live model reads a flat 1.80% Gold interchange rate for
    every tier. The full ladder is 1.80 / 2.05 / 2.10%. The collapse therefore
    UNDERSTATES stream 2 by exactly the interchange a Platinum or Sovereign
    cardholder generates above the Gold rate:

        cost(y) = SUM over tiers of spend(y, tier) x [F12(tier) - 1.80%] x PM

    expressed as a share of that year's GROSS PROFIT, because that is the
    denominator the 5% gate is stated against.

    THE VERDICT IS BINDING. If any year exceeds 5%, the collapse is unsafe and
    the model must revert to the full ladder. This function returns the rows;
    the caller asserts.

    ⚠ The full ladder lives on the validation path ONLY (check 15). Nothing in
    the live model may read it, or the collapse would be silently un-done.
    """
    rows = []
    for y in sorted(tier_counts_by_year):
        counts = tier_counts_by_year[y]
        gp = gross_profit_by_year.get(y, 0.0)
        pm = pm_share_by_year.get(y, P.PM_SHARE["Base"])
        collapsed = full = 0.0
        for tier in ("Gold", "Platinum", "Sovereign"):
            n = counts.get(tier, 0.0) * activation
            spend = n * spend_per_card_usd * P.CARD_SPEND_TIER_MULT["Base"][tier] * 12.0
            collapsed += spend * P.COLLAPSE_INTERCHANGE_RATE * pm
            full += spend * P.INTERCHANGE[tier] * pm
        delta = full - collapsed
        rows.append({
            "year": y,
            "stream2_collapsed_usd": collapsed,
            "stream2_full_ladder_usd": full,
            "collapse_cost_usd": delta,
            "gross_profit_usd": gp,
            "cost_pct_of_gross_profit": (delta / gp * 100) if gp > 0 else 0.0,
            "within_5pct_gate": (abs(delta) <= P.COLLAPSE_SAFETY_GATE * gp) if gp > 0
                                else True,
        })
    return rows
