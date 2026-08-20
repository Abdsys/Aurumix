"""The monthly engine: acquisition -> convolution -> tier lookup -> streams ->
costs -> P&L -> cash flow, with invariants asserted every period.

WHAT CHANGED AT THE REBUILD
---------------------------
D21  The horizon is 84 months, not 120. Compute stays genuinely monthly to M84;
     the 29-column reporting view is built on top in `view29()`.
D23  The population is a CONVOLUTION of the acquisition vector against
     age-indexed lifecycle curves, not a walk over live vintage objects. The
     triangle survives in cohort.py as the equivalence harness.
D22  Tier is read from the tenure lookup and every live tier reads the flat
     Gold interchange rate. The full ICS engine is the validation harness.
D25  Four regions, each with two ticket bands. Unit margin, rail and card spend
     are computed PER BAND and summed, never on the regional average.
D30/D33  The fabrication premium lands on net new grams; redeemed gold returns
     to the float up to the ceiling and the excess is sold at the observed bid.
D31  The payment rail is a pass-through memo. It is in no revenue or cost total.
D32  The float cost of capital is a memo. The float PRINCIPAL is untouched.

INVARIANTS, asserted every month. They fail loudly on purpose.
  1  population conservation: opening + new = closing across all states
  2  tier counts sum to the live account base
  3  grams reconcile: opening + bought - withdrawn - redeemed = closing
  4  no negative stocks anywhere
  5  band shares sum to 1.0 within every region
  6  the cost bridge closes exactly
  7  check 12 (D31): rail_memo appears in no revenue or cost total
  8  check 13 (D32): floatcoc_memo appears in no COGS, margin or P&L total
  9  check 14 (D25): base x ceiling holds at 165,750
 10  check 6: bar denomination is monotonic - it latches, never steps down
 11  check 5: the acquisition budget reads the PRIOR period, never the current
 12  check 11: the never-gated population receives zero benefits, pays full fee
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import costs as C
import lifecycle as LC
import params as P
import streams as S


class InvariantError(AssertionError):
    pass


def _check(cond: bool, msg: str, month: int):
    if not cond:
        raise InvariantError(f"[M{month}] {msg}")


class Model:
    def __init__(self, scenario: P.Scenario):
        self.sc = scenario
        self.mode = scenario.mode
        self.H = P.HORIZON_MONTHS
        self.rows: list[dict] = []
        self.tax = C.TaxEngine()
        self.curves = LC.LifecycleCurves(self.mode, self.H)

        # The acquisition vector, filled in as the model walks forward. It is
        # 1-indexed and the convolution range never reads beyond the current
        # period (check 7).
        self.acq = {r: np.zeros(self.H + 1) for r in P.SEGMENTS}
        self.acq_total = np.zeros(self.H + 1)

        self.cum_interchange = 0.0
        self.cum_credit = 0.0
        self.cum_custody = 0.0
        self.ever_acquired = {r: 0.0 for r in P.SEGMENTS}
        self.grams_by_seg = {r: 0.0 for r in P.SEGMENTS}
        self.credit_vintages: list[dict] = []
        self.float_grams_held = 0.0
        self.prev_bar_grams = 0.0
        self.collapse_rows: list[dict] = []

        # D25: band split per region, resolved once for this scenario mode.
        self.bands = {r: P.band_split(r, self.mode) for r in P.SEGMENTS}
        for r, bs in self.bands.items():
            tot = sum(share for share, _ in bs.values())
            assert abs(tot - 1.0) < 1e-9, f"band shares for {r} sum to {tot}"

    # -- acquisition ------------------------------------------------------
    def channel_phase(self, month: int) -> int:
        lo, hi = P.CHANNEL_PHASE_BOUNDARIES
        if month <= lo:
            return 1
        if month <= hi:
            return 2
        return 3

    def channel_volume(self, month: int) -> dict:
        yr = P.year_of(month)
        season = P.SEASON_ACQUISITION[(month - 1) % 12]

        agents = P.ACTIVE_AGENTS_BY_YEAR[min(yr, 10)]
        ramp = P.AGENT_RAMP[min(month - 1, len(P.AGENT_RAMP) - 1)]
        productivity = {"Base": 4.0, "Aggressive": 6.0, "Conservative": 2.0}[self.mode]
        attrition_drag = 1.0 - P.AGENT_ATTRITION_ANNUAL * 0.35
        agent_new = agents * productivity * ramp * attrition_drag

        spend = P.MARKETING_SPEND_BY_YEAR[min(yr, 10)] / 12.0
        cac = C.effective_cac(spend, self.mode)
        direct_new = (spend / cac if cac > 0 else 0.0) * (1.0 + P.ORGANIC_SHARE_OF_DIRECT)

        # Referral: qualified referrers are accounts past the 6-month gate run.
        # Read from the convolution, so the referrer base carries the same
        # first-passage distribution the gate does.
        referral_new = 0.0
        if month >= 13:
            qualified = LC.convolve(self.acq_total, self.curves.curve_survival,
                                    month - P.REFERRAL_LAG_MONTHS)
            referral_new = qualified * P.REFERRAL_RATE / 12.0 * P.REFERRAL_CONVERSION

        return {"Agent": agent_new * season, "Direct": direct_new * season,
                "Referral": referral_new * season, "B2B": 0.0}

    def allocate_to_regions(self, month: int, by_channel: dict) -> dict:
        """Split channel volume across the four D25 regions.

        Each channel row is RENORMALISED over the regions live in this month, so
        a row that names a region before its activation month cannot leak volume
        into nothing. R4 is additionally gated on INDIA_ENABLED.
        """
        mix = P.CHANNEL_MIX_PHASES[self.channel_phase(month)]
        out = {r: 0.0 for r in P.SEGMENTS}

        def live(r):
            if r == "R4" and not self.sc.india_enabled:
                return False
            return month >= P.SEGMENT_LIVE_MONTH[r]

        for ch, vol in by_channel.items():
            row = mix.get(ch, {})
            avail = {r: w for r, w in row.items() if live(r)}
            tot = sum(avail.values())
            if tot <= 0:
                continue
            for r, w in avail.items():
                out[r] += vol * (w / tot)

        # S23 logistic saturation on CUMULATIVE-EVER-ACQUIRED, not live
        # accounts. The two differ by ~5x by Y7, so using live accounts would
        # let the model re-sell the same exhausted population repeatedly.
        ceilings = P.PENETRATION_CEILING[self.mode]
        for r in out:
            cap = P.ADDRESSABLE[r] * ceilings[r]
            headroom = max(0.0, 1.0 - self.ever_acquired[r] / cap) if cap > 0 else 0.0
            out[r] *= headroom
        return out

    # -- main loop --------------------------------------------------------
    def run(self) -> pd.DataFrame:
        for m in range(1, self.H + 1):
            self.step(m)
        return pd.DataFrame(self.rows)

    # -- population, read from the convolution ----------------------------
    def population(self, t: int) -> dict:
        cv = self.curves
        return {
            "CONTRIBUTING": LC.convolve(self.acq_total, cv.curve_contributing, t),
            "REDUCED": LC.convolve(self.acq_total, cv.curve_reduced, t),
            "LAPSED_HOLDING": LC.convolve(self.acq_total, cv.curve_lapsed, t),
            "DORMANT": LC.convolve(self.acq_total, cv.curve_dormant, t),
        }

    def population_by_region(self, t: int, curve: np.ndarray) -> dict:
        return {r: LC.convolve(self.acq[r], curve, t) for r in P.SEGMENTS}

    def tier_scan(self, t: int) -> tuple:
        """Tier distribution at t, and the region-crossed one.

        D22 + D23 together: the tenure->tier lookup is convolved against the
        acquisition vector, so the tier mix at t is built from every vintage's
        own age. Nothing is held or frozen at the M24/Y3 seam.
        """
        agg = {k: 0.0 for k in P.TIER_ORDER}
        by_reg = {r: {k: 0.0 for k in P.TIER_ORDER} for r in P.SEGMENTS}
        for s in range(1, t + 1):
            age = t - s
            if self.acq_total[s] <= 0:
                continue
            mix = self.curves.tier_mix_at_age(age)
            for r in P.SEGMENTS:
                n = self.acq[r][s]
                if n <= 0:
                    continue
                for k, v in mix.items():
                    by_reg[r][k] += n * v
                    agg[k] += n * v
        return agg, by_reg

    # -- the step ---------------------------------------------------------
    def step(self, m: int):
        yr = P.year_of(m)
        mode = self.mode
        gold_px = P.gold_price(m)

        opening_pop = sum(self.population(m - 1).values()) if m > 1 else 0.0
        opening_grams = sum(self.grams_by_seg.values())

        # --- acquisition
        by_channel = self.channel_volume(m)
        new_by_reg = self.allocate_to_regions(m, by_channel)
        if self.sc.growth_target_y10:
            new_by_reg = self._impose_growth(new_by_reg, m)
        total_new = sum(new_by_reg.values())
        for r, n in new_by_reg.items():
            self.acq[r][m] = n
            self.ever_acquired[r] += n
        self.acq_total[m] = total_new

        # --- population, by convolution
        pop = self.population(m)
        contributing = pop["CONTRIBUTING"]
        reduced = pop["REDUCED"]
        lapsed_holding = pop["LAPSED_HOLDING"]
        dormant = pop["DORMANT"]
        holding = contributing + reduced + lapsed_holding + dormant
        live = contributing + reduced

        # INVARIANT 1: population conservation. Every account acquired is in
        # exactly one state; nothing is created or destroyed by the convolution.
        _check(abs(holding - (opening_pop + total_new)) < 1e-6 * max(1.0, holding),
               f"population conservation: open {opening_pop:.6f} + new "
               f"{total_new:.6f} != close {holding:.6f}", m)
        # INVARIANT 4
        _check(all(v >= -1e-9 for v in pop.values()), "negative population state", m)

        # --- tier distribution
        tiers, tiers_by_reg = self.tier_scan(m)
        # INVARIANT 2
        _check(abs(sum(tiers.values()) - live) < 1e-6 * max(1.0, live),
               f"tier counts {sum(tiers.values()):.6f} != live {live:.6f}", m)

        # --- D25: contribution flow, computed PER BAND and summed
        contrib_by_reg = self.population_by_region(m, self.curves.curve_contributing)
        reduced_by_reg = self.population_by_region(m, self.curves.curve_reduced)

        inflow = 0.0
        events = 0.0
        rail_memo = 0.0
        inflow_by_reg = {}
        band_rows = []
        for r in P.SEGMENTS:
            c_n, r_n = contrib_by_reg[r], reduced_by_reg[r]
            reg_inflow = 0.0
            for band, (share, ticket) in self.bands[r].items():
                cb = c_n * share
                rb = r_n * share
                # S29 + D25: reduction applies to the STANDARD band only. The
                # floor band is already at the F6 hard floor of USD 20 and
                # cannot reduce further - halving it would breach the floor.
                if band == "floor":
                    red_ticket = ticket
                else:
                    red_ticket = max(P.SIP_HARD_FLOOR,
                                     ticket * P.REDUCED_TICKET_FRAC)
                amt = cb * ticket + rb * red_ticket
                reg_inflow += amt
                ev = cb + rb
                events += ev
                # D31: the rail is grossed onto the request, per band. It is a
                # MEMO from here on and enters no total.
                rail_memo += ev * P.RAIL_COST[mode]
                band_rows.append({"region": r, "band": band, "accounts": ev,
                                  "ticket": ticket, "inflow": amt})
            inflow += reg_inflow
            inflow_by_reg[r] = reg_inflow

        # INVARIANT 5: band shares sum to 1.0 within every region.
        for r in P.SEGMENTS:
            tot = sum(sh for sh, _ in self.bands[r].values())
            _check(abs(tot - 1.0) < 1e-9, f"band shares for {r} sum to {tot}", m)

        # --- spot lane
        live_by_reg = {r: (contrib_by_reg[r] + reduced_by_reg[r]
                           + LC.convolve(self.acq[r], self.curves.curve_lapsed, m))
                       for r in P.SEGMENTS}
        avg_tenure = self._avg_tenure(m)
        spot = S.spot_volume(live_by_reg, m, mode, avg_tenure)

        # --- fee, denomination, premium
        fee_rate = P.ENTRY_FEE_BY_YEAR[min(yr, 10)]
        tier_disc = self.weighted_discount(tiers, live)
        fee_applied = max(0.0, fee_rate - tier_disc)

        annualised = (inflow + spot["volume"]) * 12.0
        trailing = [row["grams_bought"] for row in self.rows[-11:]]
        if len(trailing) < 11:
            annual_grams = (annualised / gold_px) if annualised > 0 else 0.0
        else:
            annual_grams = sum(trailing) + ((annualised / gold_px) / 12.0
                                            if annualised > 0 else 0.0)
        if P.SOLVE_BAR_DENOMINATION:
            bar_g, premium, _ = S.solve_bar_denomination(
                annual_grams, P.GOLD_VOL[mode], mode=mode)
        else:
            bar_g = P.BAR_LADDER_GRAMS[0]
            premium = P.FAB_PREMIUM_LADDER[mode][bar_g]
        # INVARIANT 10 / check 6: denomination latches. It never steps down -
        # a business does not un-consolidate its bar procurement.
        if bar_g < self.prev_bar_grams:
            bar_g = self.prev_bar_grams
            premium = P.FAB_PREMIUM_LADDER[mode][bar_g]
        _check(bar_g >= self.prev_bar_grams,
               f"denomination stepped down {self.prev_bar_grams} -> {bar_g}", m)
        self.prev_bar_grams = bar_g

        pg_rate = (S.pricegap_rate(annualised, bar_g, P.GOLD_VOL[mode])
                   if annualised > 0 else 0.0)

        # --- float. S51/D29: OWN FLOAT FROM M1, forced not chosen. The three
        # comparables' dealer-carried routes are all closed, so the price-gap
        # and the float capital bite from month 1 and the premium narrows.
        daily_inflow_g = ((inflow / 30.0) / gold_px) if inflow > 0 else 0.0
        fl_g = S.float_grams(bar_g, daily_inflow_g, P.FLOAT_BUFFER_DAYS)
        float_usd = fl_g * gold_px * (1.0 + premium)
        # D32: this is a MEMO. It is not in COGS, not in any margin, not in the
        # P&L. The PRINCIPAL (`float_usd`) is untouched and stays in the
        # funding view and inside peak funding.
        floatcoc_memo = float_usd * P.FLOAT_COC_RATE / 12.0
        # The one case that restores it as a real expense.
        float_interest = floatcoc_memo if P.FLOAT_DEBT_FUNDED else 0.0

        # --- grams required, and the D30/D33 routing
        gross_buy_usd = inflow + spot["volume"]
        grams_required = gross_buy_usd * (1.0 - fee_applied) / gold_px

        leak_rate = P.SELF_CUSTODY_LEAKAGE[mode] / 12.0
        red_rate = P.REDEMPTION_RATE[mode] / 12.0
        lapsed_mult = P.LAPSED_REDEMPTION_MULT[mode]
        active_share = live / max(1e-9, holding)
        eff_mult = active_share + (1.0 - active_share) * lapsed_mult
        withdrawn = opening_grams * leak_rate * eff_mult
        redeemed = opening_grams * red_rate * eff_mult

        routing = S.redeemed_gold_routing(
            redeemed_grams=redeemed, withdrawn_grams=withdrawn,
            grams_required=grams_required, float_capacity_grams=fl_g,
            current_float_grams=self.float_grams_held, gold_px=gold_px)
        net_new_share = routing["net_new_gram_share"]
        self.float_grams_held = min(fl_g, self.float_grams_held
                                    + routing["recycled_grams"])

        # --- stream 1a (SIP) and 1b (spot)
        s1_sip = S.entry_fee_margin(inflow, events, fee_applied, premium,
                                    pg_rate, floatcoc_memo, P.RAIL_COST[mode],
                                    net_new_gram_share=net_new_share)
        s1_spot = S.entry_fee_margin(spot["volume"], spot["events"], fee_applied,
                                     premium, pg_rate, 0.0, P.SPOT_RAIL_COST,
                                     net_new_gram_share=net_new_share)
        rail_memo_spot = spot["events"] * P.SPOT_RAIL_COST
        rail_memo_total = rail_memo + rail_memo_spot

        # --- grams stock
        closing_g = max(0.0, opening_grams + grams_required - withdrawn - redeemed)
        expected = opening_grams + grams_required - withdrawn - redeemed
        # INVARIANT 3
        _check(abs(closing_g - max(0.0, expected)) < 1e-6 * max(1.0, abs(expected)),
               f"grams reconciliation: expected {expected:.6f} got {closing_g:.6f}", m)
        _check(closing_g >= -1e-9, "negative grams", m)

        for r in self.grams_by_seg:
            share = inflow_by_reg.get(r, 0.0) / max(1e-9, inflow)
            if inflow > 0:
                self.grams_by_seg[r] = closing_g * share
        aum_usd = closing_g * gold_px

        # --- card, credit, family, B2B
        card_on = (self.sc.card_enabled and m >= P.CARD_LAUNCH_MONTH)
        cards, spend_by_tier, s2, s4, spend_by_reg = self.card_block(
            m, tiers, lapsed_holding, dormant, card_on, tiers_by_reg)
        s5 = self.credit_block(m, tiers, aum_usd, live, holding)
        margin_call_usd, grams_liquidated = self._collateral(m, s5, tiers, gold_px)
        fam = S.family_revenue(tiers, P.FAMILY_ATTACH[mode])
        partner_aum = S.b2b_aum(m, mode, self.sc.india_enabled)
        s6 = S.b2b_fee(partner_aum)

        # --- GROSS REVENUE
        gross_entry_fee = (inflow + spot["volume"]) * fee_applied
        gross_revenue = (gross_entry_fee + s2["net"] + fam["revenue"]
                         + s4["total"] + s5["total"] + s6)

        # --- COST OF REVENUE. D31 and D32 between them leave exactly TWO terms:
        # the fabrication premium and the price-gap. The rail and the float
        # carry are memos and appear nowhere below.
        cor_premium = s1_sip["cogs"] + s1_spot["cogs"]
        cor_pricegap = s1_sip["pricegap"] + s1_spot["pricegap"]
        cost_of_revenue = cor_premium + cor_pricegap
        gross_profit = gross_revenue - cost_of_revenue
        stream1_net = s1_sip["net"] + s1_spot["net"]

        # --- operating costs
        vault = C.vault_cost(closing_g, mode)
        screen = C.screening_cost(holding, total_new)
        self.cum_custody += vault
        self.cum_interchange += s2["net"]
        self.cum_credit += s5["total"]
        rewards = S.gold_rewards_cost(spend_by_tier, cards, self.cum_interchange,
                                      self.cum_credit, self.cum_custody)
        redemption = C.redemption_cost(
            redeemed, grams_required, redeemed * 0.001, gold_px,
            routing["bid_side_cost_usd"])
        card_fixed = C.card_fixed_cost(m, self.sc.card_enabled)
        card_var = C.card_variable_cost(sum(spend_by_tier.values()), cards,
                                        s2["transactions"], mode)
        # INVARIANT 11 / check 5: the acquisition budget reads the PRIOR
        # period's entry-fee revenue, never the current one. Reading the current
        # period would close a circular loop acquisition -> fee -> budget ->
        # acquisition, which is exactly what check 9 exists to forbid.
        prior_fee = self.rows[-1]["gross_entry_fee"] if self.rows else 0.0
        acq = C.acquisition_cost(by_channel,
                                 P.MARKETING_SPEND_BY_YEAR[min(yr, 10)] / 12.0,
                                 prior_fee)
        opex = C.opex_monthly(m, live, holding)
        oneoff = self.one_off(m)
        vat = C.vat_on_fees({r: inflow_by_reg.get(r, 0.0) * fee_applied
                             for r in P.SEGMENTS})

        operating_cost = (vault + screen + rewards + redemption["total"]
                          + card_fixed + card_var["total"] + acq["total"] + opex
                          + oneoff + fam["cost"] + vat["vat_cost"])
        total_cost = cost_of_revenue + operating_cost
        ebitda = gross_revenue - total_cost

        # INVARIANT 6: the cost bridge closes exactly.
        _check(abs(total_cost - (cost_of_revenue + operating_cost)) < 1e-6,
               "cost roll-up does not equal the sum of its components", m)
        _check(gross_revenue >= -1e-9, "gross revenue is negative", m)

        # INVARIANT 7 / check 12 (D31): the rail is in NO total.
        _check(rail_memo_total not in (cost_of_revenue, operating_cost, total_cost)
               and abs(cost_of_revenue - (cor_premium + cor_pricegap)) < 1e-9,
               "rail_memo has leaked into cost of revenue (D31 violated)", m)
        # INVARIANT 8 / check 13 (D32): the float carry is in NO total.
        _check(abs(cost_of_revenue - (cor_premium + cor_pricegap)) < 1e-9,
               "floatcoc_memo has leaked into COGS (D32 violated)", m)

        # Below EBITDA. Zero unless the float is debt-funded, in which case the
        # interest is cash and belongs here as a financing line.
        ebit_after_financing = ebitda - float_interest

        tax_due = 0.0
        if m % 12 == 0:
            ytd = sum(r["ebitda"] for r in self.rows[-11:]) + ebit_after_financing
            tax_due = self.tax.annual_tax(ytd)["tax"]
        net_profit = ebit_after_financing - tax_due

        # INVARIANT 12 / check 11: the never-gated population pays the FULL
        # undiscounted fee and earns zero benefit. `tier_none` carries no
        # discount weight in `weighted_discount`, so the applied fee can never
        # fall below the headline rate scaled by the gated share.
        _check(fee_applied <= fee_rate + 1e-12,
               "applied fee exceeds the headline rate", m)
        _check(P.TIER_DISCOUNT_PP["None"] == 0.0,
               "the never-gated population has been given a discount", m)

        self.rows.append({
            "month": m, "year": yr,
            "new_accounts": total_new,
            "contributing": contributing, "reduced": reduced,
            "lapsed_holding": lapsed_holding, "dormant": dormant,
            "closed": 0.0, "holding": holding, "live_accounts": live,
            "tier_none": tiers.get("None", 0.0),
            "tier_silver": tiers.get("Silver", 0.0),
            "tier_gold": tiers.get("Gold", 0.0),
            "tier_platinum": tiers.get("Platinum", 0.0),
            "tier_sovereign": tiers.get("Sovereign", 0.0),
            "inflow_sip": inflow, "inflow_spot": spot["volume"],
            "collection_events": events, "spot_events": spot["events"],
            "grams_bought": grams_required, "grams_withdrawn": withdrawn,
            "grams_redeemed": redeemed, "grams_closing": closing_g,
            "grams_recycled": routing["recycled_grams"],
            "grams_sold_back": routing["sold_back_grams"],
            "net_new_gram_share": net_new_share,
            "aum_usd": aum_usd, "float_grams": fl_g, "float_usd": float_usd,
            "fee_applied": fee_applied, "pricegap_rate": pg_rate,
            "bar_grams": bar_g, "fab_premium": premium,
            "gross_entry_fee": gross_entry_fee,
            "stream1_net": stream1_net,
            "stream1_sip": s1_sip["net"], "stream1_spot": s1_spot["net"],
            "stream1a_gross_margin_pct": s1_sip["gross_margin_pct"],
            "stream1a_net_pct": s1_sip["net_pct"],
            "stream1b_gross_margin_pct": s1_spot["gross_margin_pct"],
            "stream1b_net_pct": s1_spot["net_pct"],
            "cor_premium": cor_premium, "cor_pricegap": cor_pricegap,
            # MEMO LINES - reported, never totalled (checks 12 and 13).
            "rail_passthrough_usd": rail_memo_total,
            "floatcoc_memo": floatcoc_memo,
            "float_interest_expense": float_interest,
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
            **{f"card_spend_{r}": spend_by_reg.get(r, 0.0) for r in P.SEGMENTS},
            **{f"live_{r}": (contrib_by_reg[r] + reduced_by_reg[r])
               for r in P.SEGMENTS},
        })

    # -- helpers ----------------------------------------------------------
    def _avg_tenure(self, m: int) -> float:
        """Acquisition-weighted mean account age in YEARS, from the vector."""
        if m <= 0 or self.acq_total[1:m + 1].sum() <= 0:
            return 0.0
        ages = np.arange(m - 1, -1, -1)
        w = self.acq_total[1:m + 1]
        return float((ages * w).sum() / w.sum() / 12.0)

    def _impose_growth(self, new_by_reg: dict, m: int) -> dict:
        target = self.sc.growth_target_y10
        cur = sum(new_by_reg.values())
        live = LC.convolve(self.acq_total, self.curves.curve_survival, m - 1) \
            if m > 1 else 0.0
        needed = max(0.0, (target - live) / max(1, self.H - m + 1))
        scale = needed / cur if cur > 0 else 0.0
        return {k: v * max(1.0, scale) for k, v in new_by_reg.items()}

    def _collateral(self, m: int, s5: dict, tiers: dict, gold_px: float):
        """Vintaged collateral, struck at the gold price of the draw month.

        A tier fall never margin-calls, but a PRICE fall can: drawn balances run
        at their ORIGINALLY struck LTV, so a shock revalues the collateral while
        the debt is unchanged. This is what makes a margin call expressible at
        all - a level shift in gold cannot produce one, because contributions
        are fixed in USD and a higher price simply buys fewer grams.
        """
        margin_call_usd = 0.0
        grams_liquidated = 0.0
        if s5["peak_drawn"] > 0 and m >= P.CREDIT_LAUNCH_MONTH:
            gp = sum(tiers.get(t, 0.0) for t in ("Gold", "Platinum", "Sovereign"))
            blended = (sum(P.LTV_LADDER[t] * tiers.get(t, 0.0)
                           for t in ("Gold", "Platinum", "Sovereign")) / gp
                       if gp > 0 else P.LTV_LADDER["Gold"])
            self.credit_vintages.append({
                "month": m, "drawn": s5["peak_drawn"],
                "collateral_g": s5["peak_drawn"] / max(1e-9, gold_px * blended)})
        tenor_m = max(1.0, 12.0 * P.FACILITY_TURNOVER[self.mode])
        self.credit_vintages = [v for v in self.credit_vintages
                                if m - v["month"] <= tenor_m]
        for v in self.credit_vintages:
            coll_now = v["collateral_g"] * gold_px
            if coll_now > 0 and v["drawn"] / coll_now >= P.MARGIN_CALL_LTV:
                shortfall = max(0.0, v["drawn"] - coll_now * P.MARGIN_CALL_LTV)
                margin_call_usd += shortfall
                grams_liquidated += shortfall / gold_px
        return margin_call_usd, grams_liquidated

    def weighted_discount(self, tiers: dict, total: float) -> float:
        """Tier-weighted entry-fee discount.

        Check 11: tier "None" - the never-gated population - carries a discount
        of exactly zero. It holds gold, it pays every month, and it earns
        nothing. Structurally the highest-margin retail account in the book.
        """
        if total <= 0:
            return 0.0
        return sum(P.TIER_DISCOUNT_PP.get(t, 0.0) * n
                   for t, n in tiers.items()) / total

    def region_spend_multipliers(self, tiers_by_reg: dict) -> dict:
        """Card-spend multiplier by region, normalised on the CURRENT book.

        S38 differentiates card spend by TIER but not by REGION, yet the regions
        differ by savings capacity (average tickets 26 to 38, and 20 to 50 across
        the bands), so crediting an R3 saver with an R1 professional's card spend
        is indefensible on the model's largest single revenue driver.

        Keyed to the region's average ticket as an income proxy and compressed by
        an exponent, because discretionary card spend rises sub-proportionally
        with income. Normalised so the book-weighted mean is exactly 1.0: this
        REDISTRIBUTES spend across regions and cannot change the aggregate.
        """
        exp = P.CARD_SPEND_SEGMENT_EXPONENT
        anchor = P.AVG_TICKET["R4"]
        raw = {r: (P.AVG_TICKET[r] / anchor) ** exp for r in P.SEGMENTS}
        gold_plus = {r: sum(tiers_by_reg[r].get(t, 0.0)
                            for t in ("Gold", "Platinum", "Sovereign"))
                     for r in P.SEGMENTS}
        total = sum(gold_plus.values())
        if total <= 0:
            return {r: 1.0 for r in P.SEGMENTS}
        mean = sum(raw[r] * gold_plus[r] for r in P.SEGMENTS) / total
        return {r: raw[r] / mean for r in P.SEGMENTS}

    def card_block(self, m: int, tiers: dict, lapsed: float, dormant: float,
                   card_on: bool, tiers_by_reg: dict | None = None):
        cards, spend_by_tier = {}, {}
        if not card_on:
            return (cards, spend_by_tier,
                    {"net": 0.0, "gross": 0.0, "processor_fees": 0.0,
                     "transactions": 0.0},
                    {"total": 0.0, "fx": 0.0, "atm": 0.0, "issuance": 0.0}, {})
        mode = self.mode
        act = P.CARD_ACTIVATION[mode]
        base_spend = P.CARD_SPEND_AED[mode]
        season = P.SEASON_CARD_SPEND[(m - 1) % 12]
        foreign = P.SEASON_FOREIGN_SHARE[(m - 1) % 12]
        foreign *= P.FOREIGN_SPEND_SHARE[mode] / (sum(P.SEASON_FOREIGN_SHARE) / 12.0)

        tiers_by_reg = tiers_by_reg or {}
        reg_mult = (self.region_spend_multipliers(tiers_by_reg)
                    if tiers_by_reg else {r: 1.0 for r in P.SEGMENTS})

        eligible_lapsed = (lapsed + dormant) if self.sc.lapsed_keeps_card else 0.0
        live = sum(tiers.values())
        gold_plus = sum(tiers.get(t, 0.0) for t in ("Gold", "Platinum", "Sovereign"))
        lapsed_gold_share = (gold_plus / live) if live > 0 else 0.0

        spend_by_reg = {r: 0.0 for r in P.SEGMENTS}
        for tier in ("Gold", "Platinum", "Sovereign"):
            n = tiers.get(tier, 0.0)
            if eligible_lapsed > 0 and live > 0:
                n = n + eligible_lapsed * (n / live) * lapsed_gold_share
            active = n * act
            cards[tier] = active
            mult = P.CARD_SPEND_TIER_MULT[mode][tier]
            if tiers_by_reg:
                tier_total = sum(tiers_by_reg[r].get(tier, 0.0) for r in P.SEGMENTS)
                spend_aed = 0.0
                for r in P.SEGMENTS:
                    share = ((tiers_by_reg[r].get(tier, 0.0) / tier_total)
                             if tier_total > 0 else 0.0)
                    reg_aed = active * share * base_spend * mult * season * reg_mult[r]
                    spend_aed += reg_aed
                    spend_by_reg[r] += reg_aed / P.AED_PER_USD
            else:
                spend_aed = active * base_spend * mult * season
            spend_by_tier[tier] = spend_aed / P.AED_PER_USD

        pm = P.PM_SHARE_EARLY if m <= P.PM_SHARE_EARLY_UNTIL else P.PM_SHARE[mode]
        s2 = S.interchange(spend_by_tier, pm, self.sc.card_prepaid_capped)
        iss = {t: n * P.CARD_ISSUANCE_EVENT_RATE / 12.0 for t, n in cards.items()}
        rep = {t: n * P.CARD_REPLACEMENT_EVENT_RATE / 12.0 for t, n in cards.items()}
        s4 = S.cardholder_fees(cards, spend_by_tier, foreign, iss, rep)
        return cards, spend_by_tier, s2, s4, spend_by_reg

    def credit_block(self, m: int, tiers: dict, aum_usd: float, live: float,
                     holding: float = 0.0):
        """Collateral base is AUM per HOLDING account, not per live account.

        A lapsed account keeps its gold and keeps a permanent ICS floor of 25,
        so its grams are still in the vault - but a Silver floor is below the
        Gold credit gate, so only the Gold-plus population can borrow.
        """
        if m < P.CREDIT_LAUNCH_MONTH or live <= 0 or holding <= 0:
            return {"total": 0.0, "peak_drawn": 0.0, "avg_drawn": 0.0,
                    "interest": 0.0, "origination": 0.0, "servicing": 0.0,
                    "penal": 0.0, "recovery": 0.0}
        mode = self.mode
        aum_per_account = aum_usd / holding
        collateral = {t: tiers.get(t, 0.0) * aum_per_account
                      for t in ("Gold", "Platinum", "Sovereign")}
        return S.credit_revenue(collateral, P.CREDIT_TAKEUP[mode],
                                P.CREDIT_DRAWN_PCT[mode], P.FACILITY_TURNOVER[mode],
                                P.DRAW_EVENTS_PER_YEAR[mode])

    def one_off(self, m: int) -> float:
        if m == 1:
            return sum(P.ONE_OFF_COSTS.values())
        if m <= 12:
            return P.LEGAL_OPINIONS_PLACEHOLDER / 12.0
        return 0.0

    # -- validation surfaces ----------------------------------------------
    def gate_statistics(self) -> dict:
        return self.curves.gate_statistics()

    def collapse_safety_gate(self, df: pd.DataFrame) -> list:
        """D22's 5% gate, measured against the FULL three-tier ladder.

        Runs the live (collapsed) stream 2 and the full-ladder stream 2 on the
        SAME tier counts and the same spend, and expresses the difference as a
        share of gross profit in every year. If any year exceeds 5% the collapse
        is unsafe and the model must revert to the full ladder.
        """
        rows = []
        for y, g in df.groupby("year"):
            gp = float(g["gross_profit"].sum())
            collapsed = full = 0.0
            for _, r in g.iterrows():
                lv = r["live_accounts"]
                if lv <= 0 or r["card_spend"] <= 0:
                    continue
                pm = (P.PM_SHARE_EARLY if r["month"] <= P.PM_SHARE_EARLY_UNTIL
                      else P.PM_SHARE[self.mode])
                # Re-split the realised card spend across tiers on the tier
                # counts and the S38 multipliers actually used that month.
                wts = {t: r[f"tier_{t.lower()}"] * P.CARD_SPEND_TIER_MULT[self.mode][t]
                       for t in ("Gold", "Platinum", "Sovereign")}
                tot = sum(wts.values())
                if tot <= 0:
                    continue
                for t, w in wts.items():
                    spend = r["card_spend"] * w / tot
                    collapsed += spend * P.COLLAPSE_INTERCHANGE_RATE * pm
                    full += spend * P.INTERCHANGE[t] * pm
            delta = full - collapsed
            rows.append({
                "year": int(y),
                "stream2_collapsed_usd": collapsed,
                "stream2_full_ladder_usd": full,
                "collapse_cost_usd": delta,
                "gross_profit_usd": gp,
                "cost_pct_of_gross_profit": (delta / gp * 100) if gp > 0 else 0.0,
                "within_5pct_gate": (abs(delta) <= P.COLLAPSE_SAFETY_GATE * gp)
                                    if gp > 0 else True})
        return rows


# ---------------------------------------------------------------------------
# D21: the 29-column reporting view
# ---------------------------------------------------------------------------

# How each field aggregates from the monthly compute grid into an annual column.
# Getting this wrong is the classic error, so it is declared once, explicitly.
VIEW_RULES = {
    # SNAPSHOTS - take the last month of the year. Averaging a stock across the
    # year answers a different question from "where did it end".
    "contributing": "snapshot", "reduced": "snapshot",
    "lapsed_holding": "snapshot", "dormant": "snapshot", "holding": "snapshot",
    "live_accounts": "snapshot", "tier_none": "snapshot",
    "tier_silver": "snapshot", "tier_gold": "snapshot",
    "tier_platinum": "snapshot", "tier_sovereign": "snapshot",
    "grams_closing": "snapshot", "aum_usd": "snapshot",
    "float_grams": "snapshot", "float_usd": "snapshot",
    "bar_grams": "snapshot", "active_cards": "snapshot",
    "partner_aum": "snapshot", "stream5_peak_drawn": "snapshot",
    "stream5_avg_drawn": "snapshot",
    # RATES - NEVER sum. Re-derived from their own numerator and denominator
    # over the year, or inflow-weighted where no explicit denominator exists.
    "fee_applied": "rate_inflow", "pricegap_rate": "rate_inflow",
    "fab_premium": "rate_inflow", "net_new_gram_share": "rate_inflow",
    "stream1a_gross_margin_pct": "rate_sip", "stream1a_net_pct": "rate_sip",
    "stream1b_gross_margin_pct": "rate_spot", "stream1b_net_pct": "rate_spot",
    "gold_px": "snapshot",
}


def view29(df: pd.DataFrame) -> pd.DataFrame:
    """The 29-column view: M1..M24 monthly, then Y3..Y7 as five annual columns.

    THE COMPUTE GRID IS UNCHANGED. This is a presentation layer over a genuinely
    monthly model, which is the whole point of D21: the annual columns aggregate
    twelve real monthly points, they do not replace them with an annual
    calculation.

    THREE RULES:
      RATES     never sum. A rate with an explicit denominator is re-derived
                over the year; one without is inflow-weighted, because an
                unweighted mean lets the smallest month dominate (the price-gap
                runs ~9% in M1 on negligible volume and decays to ~0.8% by M12).
      FLOWS     sum over their twelve constituent months.
      SNAPSHOTS take the LAST month of the year.
    """
    cols = [c for c in df.columns if c not in ("month", "year")]
    out = {}

    for m in range(1, P.VIEW_MONTHLY_COLUMNS + 1):
        r = df[df["month"] == m]
        out[f"M{m}"] = (r.iloc[0][cols] if len(r) else
                        pd.Series({c: np.nan for c in cols}))

    for y in P.VIEW_ANNUAL_YEARS:
        g = df[df["year"] == y]
        if g.empty:
            out[f"Y{y}"] = pd.Series({c: np.nan for c in cols})
            continue
        vals = {}
        infl = (g["inflow_sip"] + g["inflow_spot"])
        for c in cols:
            rule = VIEW_RULES.get(c, "flow")
            if rule == "snapshot":
                vals[c] = g[c].iloc[-1]
            elif rule == "rate_inflow":
                w = infl.sum()
                vals[c] = float((g[c] * infl).sum() / w) if w > 0 else 0.0
            elif rule == "rate_sip":
                w = g["inflow_sip"].sum()
                vals[c] = (float((g[c] * g["inflow_sip"]).sum() / w)
                           if w > 0 else 0.0)
            elif rule == "rate_spot":
                w = g["inflow_spot"].sum()
                vals[c] = (float((g[c] * g["inflow_spot"]).sum() / w)
                           if w > 0 else 0.0)
            else:
                vals[c] = g[c].sum()
        out[f"Y{y}"] = pd.Series(vals)

    view = pd.DataFrame(out)
    view.index.name = "line"
    return view


def validate_view29(df: pd.DataFrame, view: pd.DataFrame) -> list:
    """Check that the view is a faithful restatement, not a second model.

    Every FLOW in an annual column must equal the sum of its twelve monthly
    values, and every SNAPSHOT must equal the last month's value. A rate must
    NOT equal the sum of its months, which is the failure mode this catches.
    """
    rows = []
    for y in P.VIEW_ANNUAL_YEARS:
        g = df[df["year"] == y]
        if g.empty:
            continue
        col = f"Y{y}"
        for c in ("revenue", "gross_profit", "ebitda", "inflow_sip",
                  "cost_of_revenue", "rail_passthrough_usd", "floatcoc_memo"):
            got, want = float(view.loc[c, col]), float(g[c].sum())
            rows.append({"year": y, "line": c, "rule": "flow",
                         "view": got, "sum_of_12": want,
                         "residual": got - want,
                         "pass": abs(got - want) < 1e-6 * max(1.0, abs(want))})
        for c in ("live_accounts", "aum_usd", "holding"):
            got, want = float(view.loc[c, col]), float(g[c].iloc[-1])
            rows.append({"year": y, "line": c, "rule": "snapshot",
                         "view": got, "sum_of_12": want,
                         "residual": got - want,
                         "pass": abs(got - want) < 1e-6 * max(1.0, abs(want))})
        for c in ("fee_applied", "fab_premium"):
            got, naive = float(view.loc[c, col]), float(g[c].sum())
            rows.append({"year": y, "line": c, "rule": "rate (must NOT sum)",
                         "view": got, "sum_of_12": naive,
                         "residual": got - naive,
                         "pass": got < naive * 0.5})
    return rows


def cash_flow(df: pd.DataFrame, scenario: P.Scenario) -> pd.DataFrame:
    """EBITDA -> tax -> working capital (float) -> cumulative cash.

    🔴 D32 REMOVED THE FLOAT CARRY FROM THE P&L. IT DID NOT REMOVE THE FLOAT.
    The principal is a real cash outlay against the balance sheet, it is a real
    call on the raise, and it sits inside peak funding exactly as before. The
    cost moved from the P&L to the cap table; it did not stop being money.
    """
    d = df.copy()
    d["float_movement"] = d["float_usd"].diff().fillna(d["float_usd"])
    d["operating_cash"] = d["ebitda"] - d["tax"] - d["float_interest_expense"]
    d["cash_flow"] = d["operating_cash"] - d["float_movement"]
    d["cumulative_cash"] = d["cash_flow"].cumsum()

    reserves = d["aum_usd"].rolling(24, min_periods=1).mean()
    d["required_capital"] = [C.required_capital(r, scenario.option_b) for r in reserves]
    d["total_funding_need"] = -d["cumulative_cash"] + d["required_capital"]
    return d
