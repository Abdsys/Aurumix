"""The monthly engine: acquisition -> cohorts -> ICS -> streams -> costs -> P&L
-> cash flow, with invariants asserted every period.

Invariants (fail loudly, checked every month):
  1. cohort conservation: opening + new - transfers - lapses = closing
  2. tier counts sum to accounts
  3. grams reconcile: opening + bought + rewards - redeemed - withdrawn = closing
  4. no negative stocks anywhere
  5. population conservation across the five states
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import costs as C
import params as P
import streams as S
from cohort import STATES, Vintage, build_tracks
from ics import tier_of


class InvariantError(AssertionError):
    pass


def _check(cond: bool, msg: str, month: int):
    if not cond:
        raise InvariantError(f"[M{month}] {msg}")


class Model:
    def __init__(self, scenario: P.Scenario):
        self.sc = scenario
        self.mode = scenario.mode
        self.tracks = build_tracks(self.mode)
        self.vintages: list[Vintage] = []
        self.rows: list[dict] = []
        self.tax = C.TaxEngine()
        self.invariant_log: list[dict] = []
        self.cum_interchange = 0.0
        self.cum_credit = 0.0
        self.cum_custody = 0.0
        self.ever_acquired = {s: 0.0 for s in P.SEGMENTS}
        self.grams_by_seg = {s: 0.0 for s in P.SEGMENTS}
        self.grams_hist: list[dict] = []
        self.credit_vintages: list[dict] = []

    # -- acquisition ------------------------------------------------------
    def channel_phase(self, month: int) -> int:
        if month <= 12:
            return 1
        if month <= 24:
            return 2
        return 3

    def channel_volume(self, month: int) -> dict:
        yr = P.year_of(month)
        season = P.SEASON_ACQUISITION[(month - 1) % 12]

        agents = P.ACTIVE_AGENTS_BY_YEAR[min(yr, 10)]
        ramp = P.AGENT_RAMP[min(month - 1, len(P.AGENT_RAMP) - 1)]
        productivity = {"Base": 4.0, "Aggressive": 6.0, "Conservative": 2.0}[self.mode]
        # Gross up for attrition: replacements re-enter the ramp at 0.20.
        attrition_drag = 1.0 - P.AGENT_ATTRITION_ANNUAL * 0.35
        agent_new = agents * productivity * ramp * attrition_drag

        spend = P.MARKETING_SPEND_BY_YEAR[min(yr, 10)] / 12.0
        cac = C.effective_cac(spend, self.mode)
        direct_new = spend / cac if cac > 0 else 0.0
        direct_new *= (1.0 + P.ORGANIC_SHARE_OF_DIRECT)

        referral_new = 0.0
        if month >= 13:
            qualified = sum(v.total_in(["CONTRIBUTING", "REDUCED"])
                            for v in self.vintages if month - v.origin >= 6)
            referral_new = qualified * P.REFERRAL_RATE / 12.0 * P.REFERRAL_CONVERSION

        b2b_new = 0.0
        return {"Agent": agent_new * season, "Direct": direct_new * season,
                "Referral": referral_new * season, "B2B": b2b_new}

    def allocate_to_segments(self, month: int, by_channel: dict) -> dict:
        phase = self.channel_phase(month)
        mix = P.CHANNEL_MIX_PHASES[phase]
        out = {s: 0.0 for s in P.SEGMENTS}
        for ch, vol in by_channel.items():
            for seg, share in mix.get(ch, {}).items():
                if not self.sc.india_enabled and seg == "S5":
                    continue
                if month < P.SEGMENT_LIVE_MONTH[seg]:
                    continue
                out[seg] += vol * share
        # S23 logistic saturation on CUMULATIVE-EVER-ACQUIRED, not live accounts.
        ceilings = P.PENETRATION_CEILING[self.mode]
        for seg in out:
            cap = P.ADDRESSABLE[seg] * ceilings[seg]
            headroom = max(0.0, 1.0 - self.ever_acquired[seg] / cap) if cap > 0 else 0.0
            out[seg] *= headroom
        return out

    # -- main loop --------------------------------------------------------
    def run(self) -> pd.DataFrame:
        for m in range(1, P.HORIZON_MONTHS + 1):
            self.step(m)
        return pd.DataFrame(self.rows)

    def step(self, m: int):
        yr = P.year_of(m)
        mode = self.mode

        opening_pop = sum(v.total_in(STATES) for v in self.vintages)
        opening_grams = sum(self.grams_by_seg.values())

        # --- acquisition
        by_channel = self.channel_volume(m)
        new_by_seg = self.allocate_to_segments(m, by_channel)
        if self.sc.growth_target_y10:
            new_by_seg = self._impose_growth(new_by_seg, m)
        total_new = sum(new_by_seg.values())
        for seg, n in new_by_seg.items():
            if n > 0:
                self.ever_acquired[seg] += n
                self.vintages.append(Vintage(seg, m, n, self.tracks, mode))

        # --- population transitions
        flows = {"to_reduced": 0.0, "to_lapsed": 0.0, "to_dormant": 0.0}
        for v in self.vintages:
            if v.origin == m:
                continue
            f = v.step_population(m)
            for k in flows:
                flows[k] += f[k]

        pop = {s: 0.0 for s in STATES}
        for v in self.vintages:
            for t in self.tracks:
                for st in STATES:
                    pop[st] += v.pop[t.name][st]

        # INVARIANT 1 & 5: population conservation.
        closing_pop = sum(pop.values())
        _check(abs(closing_pop - (opening_pop + total_new)) < 1e-6,
               f"population conservation: open {opening_pop:.6f} + new {total_new:.6f} "
               f"!= close {closing_pop:.6f}", m)
        _check(all(pop[s] >= -1e-9 for s in STATES), "negative population state", m)

        contributing, reduced = pop["CONTRIBUTING"], pop["REDUCED"]
        lapsed_holding, dormant = pop["LAPSED_HOLDING"], pop["DORMANT"]
        # Every account that is not CLOSED still holds gold.
        holding = contributing + reduced + lapsed_holding + dormant

        # --- tier distribution, genuinely computed from archetype tracks
        tiers, tiers_by_seg = self._tier_scan(m)
        active_for_tier = contributing + reduced
        # INVARIANT 2: tier counts sum to accounts.
        _check(abs(sum(tiers.values()) - active_for_tier) < 1e-6,
               f"tier counts {sum(tiers.values()):.6f} != accounts {active_for_tier:.6f}", m)

        # --- contribution flow
        inflow = events = 0.0
        inflow_by_seg = {}
        for v in self.vintages:
            act = v.total_in(["CONTRIBUTING"])
            red = v.total_in(["REDUCED"])
            tk = P.TICKET[v.segment]
            red_tk = max(P.SIP_HARD_FLOOR, tk * P.REDUCED_TICKET_FRAC)
            amt = act * tk + red * red_tk
            inflow += amt
            events += act + red
            inflow_by_seg[v.segment] = inflow_by_seg.get(v.segment, 0.0) + amt

        # --- spot lane
        live_by_seg = {}
        for v in self.vintages:
            live_by_seg[v.segment] = live_by_seg.get(v.segment, 0.0) + \
                v.total_in(["CONTRIBUTING", "REDUCED", "LAPSED_HOLDING"])
        avg_tenure = np.mean([(m - v.origin) / 12.0 for v in self.vintages]) \
            if self.vintages else 0.0
        spot = S.spot_volume(live_by_seg, m, mode, avg_tenure)

        # --- stream 1
        fee_rate = P.ENTRY_FEE_BY_YEAR[min(yr, 10)]
        tier_disc = self.weighted_discount(tiers, active_for_tier)
        fee_applied = max(0.0, fee_rate - tier_disc)

        # T3 solved endogenously against the model's own volume, not read from
        # v1.0's assumed schedule (which is indexed to a volume never reached).
        # Solved on TRAILING-12-MONTH volume so a seasonal trough cannot flip
        # the denomination; a bar decision is an annual procurement decision.
        gold_px = P.gold_price(m)
        annualised = (inflow + spot["volume"]) * 12.0
        trailing = [r["grams_bought"] for r in self.rows[-11:]]
        annual_grams = sum(trailing) + (annualised / gold_px
                                        if annualised > 0 else 0.0) / 12.0
        if len(trailing) < 11:      # ramp-up: annualise what we have
            annual_grams = (annualised / gold_px) if annualised > 0 else 0.0
        if P.SOLVE_BAR_DENOMINATION:
            bar_g, premium, bar_log = S.solve_bar_denomination(
                annual_grams, P.GOLD_VOL[mode])
        else:
            bar_g = P.BAR_GRAMS_BY_YEAR[min(yr, 10)]
            premium = P.FAB_PREMIUM_BY_YEAR[min(yr, 10)]
            bar_log = []
        pg_rate = S.pricegap_rate(annualised, bar_g, P.GOLD_VOL[mode]) if annualised > 0 else 0.0

        daily_inflow_g = (inflow / 30.0) / gold_px if inflow > 0 else 0.0
        fl_g = S.float_grams(bar_g, daily_inflow_g, P.FLOAT_BUFFER_DAYS)
        dealer_carried = yr < P.DEALER_CARRIED_UNTIL_YEAR
        float_usd = 0.0 if dealer_carried else fl_g * gold_px * (1 + premium)
        float_coc = float_usd * P.FLOAT_COC_RATE / 12.0
        pg_cost_rate = 0.0 if dealer_carried else pg_rate

        s1_sip = S.entry_fee_margin(inflow, events, fee_applied, premium,
                                    pg_cost_rate, float_coc, P.RAIL_COST[mode])
        s1_spot = S.entry_fee_margin(spot["volume"], spot["events"], fee_applied,
                                     premium, pg_cost_rate, 0.0, P.SPOT_RAIL_COST)

        # --- grams
        gross_buy_usd = inflow + spot["volume"]
        grams_bought = gross_buy_usd * (1.0 - fee_applied) / gold_px

        leak_rate = P.SELF_CUSTODY_LEAKAGE[mode] / 12.0
        red_rate = P.REDEMPTION_RATE[mode] / 12.0
        lapsed_mult = P.LAPSED_REDEMPTION_MULT[mode]
        active_share = (contributing + reduced) / max(1e-9, holding)
        lapsed_share = 1.0 - active_share
        eff_mult = active_share + lapsed_share * lapsed_mult

        opening_g = opening_grams
        withdrawn = opening_g * leak_rate * eff_mult
        redeemed = opening_g * red_rate * eff_mult
        closed_frac = 0.0
        closing_g = max(0.0, opening_g + grams_bought - withdrawn - redeemed)

        # INVARIANT 3: grams reconcile.
        expected = opening_g + grams_bought - withdrawn - redeemed
        _check(abs(closing_g - max(0.0, expected)) < 1e-6,
               f"grams reconciliation: expected {expected:.6f} got {closing_g:.6f}", m)
        _check(closing_g >= -1e-9, "negative grams", m)

        for seg in self.grams_by_seg:
            share = inflow_by_seg.get(seg, 0.0) / max(1e-9, inflow)
            self.grams_by_seg[seg] = closing_g * share if inflow > 0 else \
                self.grams_by_seg[seg]
        aum_usd = closing_g * gold_px

        # --- card
        card_on = (self.sc.card_enabled and m >= P.CARD_LAUNCH_MONTH)
        cards, spend_by_tier, s2, s4, spend_by_seg = self.card_block(
            m, tiers, lapsed_holding, dormant, card_on, tiers_by_seg)
        # --- credit
        s5 = self.credit_block(m, tiers, aum_usd, active_for_tier, holding)

        # --- collateral vintages, struck at the gold price of the draw month.
        # A tier fall never margin-calls, but a PRICE fall can: existing drawn
        # balances run at their ORIGINALLY struck LTV, so a shock revalues the
        # collateral while the debt is unchanged. This is what makes a margin
        # call expressible - a level shift in gold cannot produce one.
        margin_call_usd = 0.0
        grams_liquidated = 0.0
        if s5["peak_drawn"] > 0 and m >= P.CREDIT_LAUNCH_MONTH:
            blended_ltv = sum(P.LTV_LADDER[t] * tiers.get(t, 0.0)
                              for t in ("Gold", "Platinum", "Sovereign"))
            gp = sum(tiers.get(t, 0.0) for t in ("Gold", "Platinum", "Sovereign"))
            blended_ltv = (blended_ltv / gp) if gp > 0 else P.LTV_LADDER["Gold"]
            self.credit_vintages.append({
                "month": m, "drawn": s5["peak_drawn"],
                "collateral_g": s5["peak_drawn"] / max(1e-9, gold_px * blended_ltv)})
        # Retire vintages beyond the average tenor implied by S40 turnover.
        tenor_m = max(1.0, 12.0 * P.FACILITY_TURNOVER[mode])
        self.credit_vintages = [v for v in self.credit_vintages
                                if m - v["month"] <= tenor_m]
        for v in self.credit_vintages:
            coll_now = v["collateral_g"] * gold_px
            if coll_now > 0 and v["drawn"] / coll_now >= P.MARGIN_CALL_LTV:
                shortfall = v["drawn"] - coll_now * P.MARGIN_CALL_LTV
                margin_call_usd += max(0.0, shortfall)
                grams_liquidated += max(0.0, shortfall) / gold_px
        # --- family
        fam = S.family_revenue(tiers, P.FAMILY_ATTACH[mode])
        # --- b2b
        partner_aum = S.b2b_aum(m, mode, self.sc.india_enabled)
        s6 = S.b2b_fee(partner_aum)

        # --- GROSS REVENUE (never negative: fees earned, before cost of revenue)
        gross_entry_fee = (inflow + spot["volume"]) * fee_applied
        gross_revenue = (gross_entry_fee + s2["net"] + fam["revenue"]
                         + s4["total"] + s5["total"] + s6)

        # --- COST OF REVENUE (the contra-costs that sit inside stream 1)
        cor_premium = s1_sip["cogs"] + s1_spot["cogs"]
        cor_pricegap = s1_sip["pricegap"] + s1_spot["pricegap"]
        cor_float = s1_sip["float_coc"] + s1_spot["float_coc"]
        cor_rail = s1_sip["rail"] + s1_spot["rail"]
        cost_of_revenue = cor_premium + cor_pricegap + cor_float + cor_rail
        gross_profit = gross_revenue - cost_of_revenue

        # Net contribution margin is a reported METRIC, not the revenue line.
        stream1_net = s1_sip["net"] + s1_spot["net"]

        # --- operating costs
        vault = C.vault_cost(closing_g, mode)
        screen = C.screening_cost(holding, total_new)
        self.cum_custody += vault
        self.cum_interchange += s2["net"]
        self.cum_credit += s5["total"]

        rewards = S.gold_rewards_cost(spend_by_tier, cards, self.cum_interchange,
                                      self.cum_credit, self.cum_custody)
        redemption = C.redemption_cost(redeemed, grams_bought,
                                       redeemed / max(1e-9, 1.0) * 0.001)
        card_fixed = C.card_fixed_cost(m, self.sc.card_enabled)
        card_var = C.card_variable_cost(sum(spend_by_tier.values()), cards,
                                        s2["transactions"], mode)
        acq = C.acquisition_cost(by_channel,
                                 P.MARKETING_SPEND_BY_YEAR[min(yr, 10)] / 12.0,
                                 gross_entry_fee)
        # Opex charged against the MODEL'S OWN book, block by block.
        opex = C.opex_monthly(m, contributing + reduced, holding)
        oneoff = self.one_off(m)

        vat = C.vat_on_fees({s: inflow_by_seg.get(s, 0.0) * fee_applied
                             for s in P.SEGMENTS})

        operating_cost = (vault + screen + rewards + redemption["total"]
                          + card_fixed + card_var["total"] + acq["total"] + opex
                          + oneoff + fam["cost"] + vat["vat_cost"])
        total_cost = cost_of_revenue + operating_cost
        ebitda = gross_revenue - total_cost

        # INVARIANT 6: the cost bridge must close exactly.
        _check(abs(total_cost - (cost_of_revenue + operating_cost)) < 1e-6,
               "cost roll-up does not equal the sum of its components", m)
        _check(gross_revenue >= -1e-9, "gross revenue is negative", m)

        tax_due = 0.0
        if m % 12 == 0:
            ytd = sum(r["ebitda"] for r in self.rows[-11:]) + ebitda
            tax_due = self.tax.annual_tax(ytd)["tax"]
        net_profit = ebitda - tax_due

        self.rows.append({
            "month": m, "year": yr,
            "new_accounts": total_new,
            "contributing": contributing, "reduced": reduced,
            "lapsed_holding": lapsed_holding, "dormant": dormant,
            "closed": pop["CLOSED"], "holding": holding,
            "live_accounts": contributing + reduced,
            "tier_none": tiers.get("None", 0.0), "tier_silver": tiers.get("Silver", 0.0),
            "tier_gold": tiers.get("Gold", 0.0), "tier_platinum": tiers.get("Platinum", 0.0),
            "tier_sovereign": tiers.get("Sovereign", 0.0),
            "inflow_sip": inflow, "inflow_spot": spot["volume"],
            "collection_events": events, "spot_events": spot["events"],
            "grams_bought": grams_bought, "grams_withdrawn": withdrawn,
            "grams_redeemed": redeemed, "grams_closing": closing_g,
            "aum_usd": aum_usd, "float_grams": fl_g, "float_usd": float_usd,
            "fee_applied": fee_applied, "pricegap_rate": pg_rate,
            "bar_grams": bar_g, "fab_premium": premium,
            "gross_entry_fee": gross_entry_fee,
            "stream1_net": stream1_net,
            "stream1_sip": s1_sip["net"], "stream1_spot": s1_spot["net"],
            "cor_premium": cor_premium, "cor_pricegap": cor_pricegap,
            "cor_float": cor_float, "cor_rail": cor_rail,
            "cost_of_revenue": cost_of_revenue, "gross_profit": gross_profit,
            "stream2": s2["net"], "stream2_gross": s2["gross"],
            "stream2_processor_fees": s2["processor_fees"],
            "stream3": fam["revenue"], "stream4": s4["total"],
            "stream5": s5["total"], "stream5_peak_drawn": s5["peak_drawn"],
            "stream5_avg_drawn": s5["avg_drawn"],
            "stream6": s6, "partner_aum": partner_aum,
            "revenue": gross_revenue,
            "cost_vault": vault, "cost_screening": screen, "cost_rewards": rewards,
            "cost_redemption": redemption["total"], "cost_card_fixed": card_fixed,
            "cost_card_variable": card_var["total"], "cost_acquisition": acq["total"],
            "cost_opex": opex, "cost_oneoff": oneoff, "cost_family": fam["cost"],
            "cost_vat": vat["vat_cost"], "operating_cost": operating_cost,
            "total_cost": total_cost,
            "ebitda": ebitda, "tax": tax_due, "net_profit": net_profit,
            "gold_px": gold_px,
            "margin_call_usd": margin_call_usd,
            "grams_liquidated": grams_liquidated,
            "active_cards": sum(cards.values()),
            "card_spend": sum(spend_by_tier.values()),
            **{f"card_spend_{s}": spend_by_seg.get(s, 0.0) for s in P.SEGMENTS},
            **{f"live_{s}": sum(v.total_in(["CONTRIBUTING", "REDUCED"])
                                for v in self.vintages if v.segment == s)
               for s in P.SEGMENTS},
        })

    # -- helpers ----------------------------------------------------------
    def _impose_growth(self, new_by_seg: dict, m: int) -> dict:
        """'Client's plan': impose the 100k investor target as a growth input."""
        target = self.sc.growth_target_y10
        cur = sum(new_by_seg.values())
        live = sum(v.total_in(["CONTRIBUTING", "REDUCED"]) for v in self.vintages)
        needed = max(0.0, (target - live) / max(1, P.HORIZON_MONTHS - m + 1))
        scale = needed / cur if cur > 0 else 0.0
        return {k: v * max(1.0, scale) for k, v in new_by_seg.items()}

    def _tier_scan(self, m: int) -> tuple:
        """Single pass over vintages x tracks, returning both the aggregate tier
        distribution and the segment-crossed one.

        Computed together because the scan is the hot loop: it is O(vintages x
        tracks) per month, and the ICS tier lookup inside it is exact-fraction
        arithmetic. Doing it twice per period doubled total runtime.
        """
        agg = {t: 0.0 for t in P.TIER_ORDER}
        by_seg = {s: {t: 0.0 for t in P.TIER_ORDER} for s in P.SEGMENTS}
        for v in self.vintages:
            seg = by_seg[v.segment]
            pops = v.pop
            icss = v.ics
            for t in self.tracks:
                p = pops[t.name]
                n = p["CONTRIBUTING"] + p["REDUCED"]
                if n <= 0:
                    continue
                tier = icss[t.name].tier(min(1.0, t.withdraw_rate))
                agg[tier] += n
                seg[tier] += n
        return agg, by_seg

    def tier_distribution(self, m: int) -> dict:
        """Weighted sum over archetype tracks - genuinely computed, not a
        threshold applied to a cohort average (which is wrong by Jensen).

        Tier "None" is the NEVER-GATED population (persona H): accounts that
        pay, hold gold and pay the FULL UNDISCOUNTED entry fee but never
        complete six consecutive periods, so they never earn a score, a tier or
        any benefit. Structurally the highest-margin retail account in the book.
        """
        return self._tier_scan(m)[0]

    def tier_distribution_by_segment(self, m: int) -> dict:
        """Tier counts crossed with segment, for segment-differentiated spend."""
        return self._tier_scan(m)[1]

    def gate_statistics(self) -> dict:
        """G1: run-of-6 first passage by archetype.

        The gate is a DISTRIBUTION, not a date. An account that misses month 4
        cannot reach Silver before month 9, so every downstream ladder date
        (Gold at M12, card eligibility, credit, Sovereign at M61) shifts right
        by the expected gate delay. v1.0 treats month 6 as universal.

        This deliberately does NOT use ArchetypeTrack.pays_in_month, whose
        deterministic pattern forces a clean first six months as a modelling
        convenience and would report every archetype gating at exactly M6. The
        first-passage law is solved as a Markov chain on the run-length state
        (0..6) from each archetype's payment PROBABILITY, which is the honest
        question: given this payment behaviour, when does a run of six actually
        complete? Survival is applied per month, so an account that lapses
        before completing a run never gates - which is what generates the
        never-gated population (persona H).
        """
        bg = P.ARCHETYPE_MIX[self.mode]["background_hazard"]
        rows = []
        for a in P.ARCHETYPE_MIX[self.mode]["archetypes"]:
            p = a.pay_prob
            haz = min(0.999, a.own_hazard + bg)
            state = [0.0] * P.GATE_RUN_REQUIRED     # P(alive, run length k)
            state[0] = 1.0
            gated_mass = 0.0
            exp_month = 0.0
            for mm in range(1, P.HORIZON_MONTHS + 1):
                surv = 1.0 - haz
                nxt = [0.0] * P.GATE_RUN_REQUIRED
                newly = 0.0
                for k, mass in enumerate(state):
                    if mass <= 0.0:
                        continue
                    alive = mass * surv
                    if k + 1 >= P.GATE_RUN_REQUIRED:
                        newly += alive * p              # run completes
                    else:
                        nxt[k + 1] += alive * p
                    nxt[0] += alive * (1.0 - p)         # miss resets the run
                state = nxt
                gated_mass += newly
                exp_month += newly * mm
            mean_gate = (exp_month / gated_mass) if gated_mass > 1e-12 else None
            rows.append({"archetype": a.name, "weight": a.weight,
                         "pay_prob": p, "monthly_hazard": round(haz, 4),
                         "ever_gate_prob": round(gated_mass, 4),
                         "mean_gate_month": (round(mean_gate, 1)
                                             if mean_gate else None)})
        ever = sum(r["weight"] * r["ever_gate_prob"] for r in rows)
        exp_gate = (sum(r["weight"] * r["ever_gate_prob"] * r["mean_gate_month"]
                        for r in rows if r["mean_gate_month"])
                    / max(1e-9, ever))
        return {"by_archetype": rows, "ever_gate_share": ever,
                "never_gate_share": 1.0 - ever, "expected_gate_month": exp_gate}

    def weighted_discount(self, tiers: dict, total: float) -> float:
        if total <= 0:
            return 0.0
        return sum(P.TIER_DISCOUNT_PP.get(t, 0.0) * n for t, n in tiers.items()) / total

    def segment_spend_multipliers(self, tiers_by_seg: dict) -> dict:
        """Segment card-spend multipliers, normalised on the CURRENT book.

        Keyed to the SIP ticket as an income proxy and compressed by an
        exponent. Normalised so the book-weighted mean is exactly 1.0, which
        makes this a pure redistribution across segments: it cannot change
        aggregate card spend, only who is credited with it.
        """
        exp = P.CARD_SPEND_SEGMENT_EXPONENT
        anchor = P.TICKET["S2"]      # the AED 6,000 anchor segment
        raw = {s: (P.TICKET[s] / anchor) ** exp for s in P.SEGMENTS}
        gold_plus = {s: sum(tiers_by_seg[s].get(t, 0.0)
                            for t in ("Gold", "Platinum", "Sovereign"))
                     for s in P.SEGMENTS}
        total = sum(gold_plus.values())
        if total <= 0:
            return {s: 1.0 for s in P.SEGMENTS}
        mean = sum(raw[s] * gold_plus[s] for s in P.SEGMENTS) / total
        return {s: raw[s] / mean for s in P.SEGMENTS}

    def card_block(self, m: int, tiers: dict, lapsed: float, dormant: float,
                   card_on: bool, tiers_by_seg: dict | None = None):
        cards = {}
        spend_by_tier = {}
        if not card_on:
            return cards, spend_by_tier, {"net": 0.0, "gross": 0.0,
                                          "processor_fees": 0.0, "transactions": 0.0}, \
                   {"total": 0.0, "fx": 0.0, "atm": 0.0, "issuance": 0.0}, {}
        mode = self.mode
        act = P.CARD_ACTIVATION[mode]
        base_spend = P.CARD_SPEND_AED[mode]
        season = P.SEASON_CARD_SPEND[(m - 1) % 12]
        foreign = P.SEASON_FOREIGN_SHARE[(m - 1) % 12]
        foreign *= P.FOREIGN_SPEND_SHARE[mode] / (sum(P.SEASON_FOREIGN_SHARE) / 12.0)

        tiers_by_seg = tiers_by_seg or {}
        seg_mult = (self.segment_spend_multipliers(tiers_by_seg)
                    if tiers_by_seg else {s: 1.0 for s in P.SEGMENTS})

        eligible_lapsed = (lapsed + dormant) if self.sc.lapsed_keeps_card else 0.0
        live = sum(tiers.values())
        gold_plus = sum(tiers.get(t, 0.0) for t in ("Gold", "Platinum", "Sovereign"))
        lapsed_gold_share = (gold_plus / live) if live > 0 else 0.0

        spend_by_seg = {s: 0.0 for s in P.SEGMENTS}
        for tier in ("Gold", "Platinum", "Sovereign"):
            n = tiers.get(tier, 0.0)
            if eligible_lapsed > 0 and live > 0:
                n = n + eligible_lapsed * (n / live) * lapsed_gold_share
            active = n * act
            cards[tier] = active
            mult = P.CARD_SPEND_TIER_MULT[mode][tier]

            # Split this tier's cards across segments, then apply each
            # segment's income-proxy multiplier before re-aggregating.
            if tiers_by_seg:
                tier_total = sum(tiers_by_seg[s].get(tier, 0.0) for s in P.SEGMENTS)
                spend_aed = 0.0
                for s in P.SEGMENTS:
                    share = ((tiers_by_seg[s].get(tier, 0.0) / tier_total)
                             if tier_total > 0 else 0.0)
                    seg_aed = active * share * base_spend * mult * season * seg_mult[s]
                    spend_aed += seg_aed
                    spend_by_seg[s] += seg_aed / P.AED_PER_USD
            else:
                spend_aed = active * base_spend * mult * season
            spend_by_tier[tier] = spend_aed / P.AED_PER_USD

        pm = P.PM_SHARE_EARLY if m <= P.PM_SHARE_EARLY_UNTIL else P.PM_SHARE[mode]
        s2 = S.interchange(spend_by_tier, pm, self.sc.card_prepaid_capped)

        iss = {t: n * P.CARD_ISSUANCE_EVENT_RATE / 12.0 for t, n in cards.items()}
        rep = {t: n * P.CARD_REPLACEMENT_EVENT_RATE / 12.0 for t, n in cards.items()}
        s4 = S.cardholder_fees(cards, spend_by_tier, foreign, iss, rep)
        return cards, spend_by_tier, s2, s4, spend_by_seg

    def credit_block(self, m: int, tiers: dict, aum_usd: float, live: float,
                     holding: float = 0.0):
        """Collateral base is AUM per HOLDING account, not per live account.

        A lapsed account keeps its gold and keeps a permanent ICS floor of 25,
        so its grams are still in the vault - but a Silver floor is below the
        Gold credit gate, so only the Gold+ population can borrow. The base is
        therefore (Gold+ accounts) x (AUM per holding account), which is a very
        different number from (Gold+ share) x (total AUM) whenever the lapsed
        book is large - and at 19% M61 persistency it always is.
        """
        if m < P.CREDIT_LAUNCH_MONTH or live <= 0 or holding <= 0:
            return {"total": 0.0, "peak_drawn": 0.0, "avg_drawn": 0.0,
                    "interest": 0.0, "origination": 0.0, "servicing": 0.0,
                    "penal": 0.0, "recovery": 0.0}
        mode = self.mode
        aum_per_account = aum_usd / holding
        collateral = {}
        for tier in ("Gold", "Platinum", "Sovereign"):
            collateral[tier] = tiers.get(tier, 0.0) * aum_per_account
        return S.credit_revenue(collateral, P.CREDIT_TAKEUP[mode],
                                P.CREDIT_DRAWN_PCT[mode], P.FACILITY_TURNOVER[mode],
                                P.DRAW_EVENTS_PER_YEAR[mode])

    def one_off(self, m: int) -> float:
        if m == 1:
            return sum(P.ONE_OFF_COSTS.values())
        if m <= 12:
            return P.LEGAL_OPINIONS_PLACEHOLDER / 12.0
        return 0.0


def cash_flow(df: pd.DataFrame, scenario: P.Scenario) -> pd.DataFrame:
    """EBITDA -> tax -> working capital (float) -> cumulative cash.

    Reports peak funding requirement and the month it occurs, plus regulatory
    capital. v1.0 has no cash view at all yet charges a float cost of capital.
    """
    d = df.copy()
    d["float_movement"] = d["float_usd"].diff().fillna(d["float_usd"])
    d["operating_cash"] = d["ebitda"] - d["tax"]
    d["cash_flow"] = d["operating_cash"] - d["float_movement"]
    d["cumulative_cash"] = d["cash_flow"].cumsum()

    reserves = d["aum_usd"].rolling(24, min_periods=1).mean()
    d["required_capital"] = [C.required_capital(r, scenario.option_b) for r in reserves]
    d["total_funding_need"] = -d["cumulative_cash"] + d["required_capital"]
    return d
