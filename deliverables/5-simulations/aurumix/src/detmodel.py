"""
The deterministic engine: a formula-for-formula port of
Aurumix_Revenue_Model_calculated.xlsx onto the 29-period grid.

Purpose (blueprint Part 4.1): with every stochastic input pinned to Base, this
must reproduce the calculated workbook to within rounding. It is the CENTRE
CASE and the equivalence reference for the Monte Carlo engine - it is NOT the
simulation itself.

Row references in comments are Model-sheet rows of the workbook. Parameters
come from config/params.json, extracted directly from the workbook, so the
port cannot drift by transcription.
"""

import json
import os

import numpy as np

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_params(path=None):
    with open(path or os.path.join(_HERE, "config", "params.json")) as f:
        return json.load(f)


class DetModel:
    """One deterministic run over the 29-period grid. Mirrors the Model sheet."""

    N = 29  # 24 monthly + 5 annual

    def __init__(self, p=None, overrides=None):
        self.p = dict(load_params() if p is None else p)
        if overrides:
            self.p.update(overrides)
        g = self.p["grid"]
        self.period = np.array(g["period"], dtype=float)       # R2
        self.year = np.array(g["year"], dtype=float)           # R5
        self.cal_month = np.array(g["cal_month"], dtype=int)   # R6 (0 = annual)
        self.months = np.array(g["months"], dtype=float)       # R7
        self.out = {}

    # ── helpers ──────────────────────────────────────────────────────────────

    def _year_index(self, i):
        return int(self.year[i]) - 1

    def _season(self, raw, amplitude):
        """R11/R12: (1 + (v-1)*amp) * 12 / sum(1 + (v-1)*amp). Sums to 12 exactly."""
        v = np.array(raw, dtype=float)
        scaled = 1.0 + (v - 1.0) * amplitude
        return scaled * 12.0 / scaled.sum()

    # ── the run ──────────────────────────────────────────────────────────────

    def run(self):
        p, N = self.p, self.N
        o = self.out
        yr = self.year.astype(int) - 1
        mo = self.months
        per = self.period

        # R11-R17 seasonality
        acq_vec = self._season(p["season_acq"], p["seasonality_amplitude"])
        card_vec = self._season(p["season_card"], p["seasonality_amplitude"])
        foreign_vec = (np.array(p["season_foreign"], dtype=float)
                       / np.mean(p["season_foreign"]) * p["foreign_spend_mean"])

        season_acq = np.where(mo == 1, acq_vec[np.maximum(self.cal_month - 1, 0)], 1.0)
        season_card = np.where(mo == 1, card_vec[np.maximum(self.cal_month - 1, 0)], 1.0)
        foreign = np.where(mo == 1, foreign_vec[np.maximum(self.cal_month - 1, 0)],
                           foreign_vec.mean())

        # R20 gold price rises by year - unless the MC layer supplies a path
        if "_gold_grid" in p:
            gold = np.array(p["_gold_grid"], dtype=float)
        else:
            gold = p["gold_price_m1"] * (1.0 + p["gold_appreciation"]) ** (self.year - 1)
        o["gold_price"] = gold

        # ── three regions (R24-R151) ─────────────────────────────────────────
        regions = {
            "UAE": dict(cac0="cac_uae", cac7="cac_uae_y7", mkt="mkt_share_uae",
                        agents="agents_uae", ceiling="ceiling_uae",
                        ticket="ticket_uae", spot_ticket="spot_ticket_uae",
                        spot_attach="spot_attach_uae", opens=1),
            "Gulf": dict(cac0="cac_gulf", cac7="cac_gulf_y7", mkt="mkt_share_gulf",
                         agents="agents_gulf", ceiling="ceiling_gulf",
                         ticket="ticket_gulf", spot_ticket="spot_ticket_gulf",
                         spot_attach="spot_attach_gulf", opens=p["act_gulf"]),
            "India": dict(cac0="cac_india", cac7="cac_india_y7", mkt="mkt_share_india",
                          agents="agents_india", ceiling="ceiling_india",
                          ticket="ticket_india", spot_ticket="spot_ticket_india",
                          spot_attach="spot_attach_india", opens=p["act_india"]),
        }

        R = {}
        for name, rg in regions.items():
            paying = np.zeros(N); holders = np.zeros(N); cum = np.zeros(N)
            new = np.zeros(N); churn = np.zeros(N)
            grams_elig = np.zeros(N); grams_cust = np.zeros(N)
            sip = np.zeros(N); spot = np.zeros(N); bought = np.zeros(N)
            cards = np.zeros(N); cards_new = np.zeros(N); fam = np.zeros(N)
            card_spend_usd = np.zeros(N); auths = np.zeros(N)
            s1a = np.zeros(N); s1b = np.zeros(N); s2 = np.zeros(N)
            s3 = np.zeros(N); s4 = np.zeros(N); s5 = np.zeros(N)
            redeem_ev = np.zeros(N); tiered = np.zeros(N)
            agent_acq = np.zeros(N); ref_acq = np.zeros(N)
            cred_limit = np.zeros(N); drawn_bal = np.zeros(N); aum = np.zeros(N)

            churn_m = p["monthly_churn"]
            for i in range(N):
                y, m = yr[i], mo[i]
                open_gate = 1.0 if per[i] >= rg["opens"] else 0.0

                # R25 CAC ramp
                cac = p[rg["cac0"]] + (p[rg["cac7"]] - p[rg["cac0"]]) * (self.year[i] - 1) / 6
                # R26 direct (organic uplift); UAE has no opens gate (always 1)
                direct = (p["marketing_spend"][y] * p[rg["mkt"]] / 12 * m / cac
                          * (1 + p["organic_share"]) * (open_gate if name != "UAE" else 1.0))
                # R27 referral off own paying base, from act_referral
                prev_pay = paying[i - 1] if i else 0.0
                ref = (prev_pay * p["referral_rate"] / 12 * p["referral_conversion"] * m
                       if per[i] >= p["act_referral"] else 0.0)
                # R28 agents
                agents = (p[rg["agents"]][y] * p["agent_productivity"]
                          * p["agent_ramp"][y] * m * (open_gate if name != "UAE" else 1.0))
                raw = direct + ref + agents
                # R30 saturation on prior cumulative-ever
                prev_cum = cum[i - 1] if i else 0.0
                sat = max(0.0, 1.0 - prev_cum / p[rg["ceiling"]])
                # R31 new
                new[i] = raw * sat * season_acq[i]
                agent_acq[i] = agents; ref_acq[i] = ref
                # R32 paying: survivors + half-period on new
                prev = paying[i - 1] if i else 0.0
                paying[i] = prev * (1 - churn_m) ** m + new[i] * (1 - churn_m) ** (m / 2)
                # R33-R35
                churn[i] = prev + new[i] - paying[i]
                holders[i] = (holders[i - 1] if i else 0.0) + churn[i]
                cum[i] = prev_cum + new[i]

                # R36 SIP, R37 spot
                if per[i] >= p["act_1a"]:
                    sip[i] = paying[i] * p[rg["ticket"]] * m
                if per[i] >= p["act_1b"]:
                    spot[i] = (paying[i] * p[rg["spot_attach"]] * p["spot_attach_mult"]
                               * p["spot_frequency"] * p[rg["spot_ticket"]]
                               * p["spot_ticket_mult"] / 12 * m)
                # R38 grams bought (premium divisor off when Aurumix bears it)
                bought[i] = ((sip[i] + spot[i]) * (1 - p["entry_fee"]) / gold[i]
                             / (1 + p["fab_premium"] * (1 - p["sw_premium_aurumix"])))

                # R39-R42 decay and gram stocks
                base_mix = (1.0 if paying[i] + holders[i] == 0 else
                            (paying[i] + holders[i] * p["holder_redemption_mult"])
                            / (paying[i] + holders[i]))
                decay_elig = (p["self_custody_rate"] + p["redemption_rate"] * base_mix) * m / 12
                decay_cust = p["redemption_rate"] * base_mix * m / 12
                # REDEMPTION PANIC hook (stress s2/s7). A run is a JUMP, not a
                # rate: a share of custody leaves in one period. A rate-based
                # model converges toward inflow/outflow balance and never
                # overshoots, so it cannot represent a run on its own.
                if p.get("panic_period") is not None and per[i] == p["panic_period"]:
                    decay_elig = min(1.0, decay_elig + p["panic_share"])
                    decay_cust = min(1.0, decay_cust + p["panic_share"])
                grams_elig[i] = (grams_elig[i - 1] if i else 0.0) * (1 - decay_elig) + bought[i]
                grams_cust[i] = (grams_cust[i - 1] if i else 0.0) * (1 - decay_cust) + bought[i]
                aum[i] = grams_elig[i] * gold[i]

                # R44-R47 cards
                elig = paying[i] + holders[i] * p["sw_holders_keep_card"]
                if per[i] >= p["act_2"]:
                    cards[i] = elig * p["facility_takeup"]
                cards_new[i] = max(0.0, cards[i] - (cards[i - 1] if i else 0.0))

                # R45 tiered memo: annual cols use elig directly; monthly lag
                if m > 1:
                    tiered[i] = elig * p["ics_ever_share"]
                elif per[i] > p["ics_months_to_tier"]:
                    j = int(per[i] - p["ics_months_to_tier"]) - 1
                    elig_j = paying[j] + holders[j] * p["sw_holders_keep_card"]
                    tiered[i] = elig_j * p["ics_ever_share"]

                # R49-R55 credit and card spend
                cred_limit[i] = 0.0 if elig == 0 else aum[i] / elig * p["ltv"]
                draw_yr = cred_limit[i] * p["drawn_pct"] * p["draws_per_year"]
                spend_pcpm = draw_yr / 12 * season_card[i]
                card_spend_usd[i] = cards[i] * spend_pcpm * m
                auths[i] = (cards[i] * p["draws_per_year"] * p["txn_per_draw"]
                            * m / 12 * (1 + p["decline_uplift"]))

                # streams
                s1a[i] = sip[i] * p["entry_fee"]
                s1b[i] = spot[i] * p["entry_fee"]
                ic_rate = (min(p["interchange"], 0.01) if p["sw_prepaid"] == 1
                           else p["interchange"])
                s2[i] = card_spend_usd[i] * ic_rate * (1 - p["pm_share"])

                # R59-R60 family
                if per[i] >= p["act_3"]:
                    prev_f = fam[i - 1] if i else 0.0
                    fam[i] = (prev_f * (1 - p["family_churn_monthly"]) ** m
                              + new[i] * p["family_attach"]
                              * (1 - p["family_churn_monthly"]) ** (m / 2))
                s3[i] = (fam[i] * (p["family_price"]
                         + max(0.0, p["beneficiaries"] - 1) * p["beneficiary_fee"]) / 12 * m)

                # R61 stream 4: FX + ATM distribution + issuance/replacement
                if per[i] >= p["act_4"]:
                    atm = sum(p[f"atm_share_{k}"]
                              * max(0.0, p[f"atm_mid_{k}"] - p["atm_allowance_aed"])
                              for k in (1, 2, 3, 4))
                    s4[i] = (card_spend_usd[i] * foreign[i] * p["fx_margin"]
                             + cards[i] * atm * p["atm_fee"] / p["aed_usd"] * m
                             + cards_new[i] * p["card_issuance_aed"] / p["aed_usd"]
                             + cards[i] * (p["reissue_rate"] * p["card_issuance_aed"]
                                           + p["replacement_rate"] * p["card_replacement_aed"])
                             / 12 / p["aed_usd"] * m)

                # R62-R63 stream 5
                if per[i] >= p["act_5"]:
                    drawn_bal[i] = (cards[i] * cred_limit[i] * (1 - p["sw_prepaid"])
                                    * p["drawn_pct"] * p["facility_turnover"])
                    s5[i] = ((drawn_bal[i] * p["credit_serv_gross"] * p["credit_serv_share"]
                              + cards[i] * draw_yr * (1 - p["sw_prepaid"])
                              * p["credit_orig_gross"] * p["credit_orig_share"]) * m / 12)

                # R64 redemption events
                if per[i] >= p["act_0"]:
                    redeem_ev[i] = ((paying[i] + holders[i] * p["holder_redemption_mult"])
                                    * p["redemption_rate"] * m / 12)
                    if p.get("panic_period") is not None and per[i] == p["panic_period"]:
                        redeem_ev[i] += p["panic_share"] * (paying[i] + holders[i])

            R[name] = dict(paying=paying, holders=holders, cum=cum, new=new,
                           grams_elig=grams_elig, grams_cust=grams_cust,
                           bought=bought, sip=sip, spot=spot, cards=cards,
                           cards_new=cards_new, fam=fam, tiered=tiered,
                           card_spend=card_spend_usd, auths=auths, aum=aum,
                           s1a=s1a, s1b=s1b, s2=s2, s3=s3, s4=s4, s5=s5,
                           redeem_ev=redeem_ev, agent_acq=agent_acq, ref_acq=ref_acq,
                           subtotal=s1a + s1b + s2 + s3 + s4 + s5)

        # ── non-regional and totals (R154-R199) ──────────────────────────────
        partner_aum = np.where(per >= p["act_6"],
                               np.array([p["b2b_partners"][y] for y in yr]) * p["partner_aum"],
                               0.0)
        s6 = partner_aum * p["b2b_fee"] * mo / 12

        def T(key):
            return sum(R[n][key] for n in R)

        o.update({f"s{k}": T(f"s{k}") for k in ("1a", "1b", "2", "3", "4", "5")})
        o["s6"] = s6
        o["revenue"] = T("subtotal") + s6
        o["paying"] = T("paying"); o["holders"] = T("holders")
        o["cum_ever"] = T("cum"); o["new"] = T("new")
        o["cards"] = T("cards"); o["grams_held"] = T("grams_elig")
        o["grams_cust"] = T("grams_cust"); o["grams_bought"] = T("bought")
        o["aum"] = T("aum"); o["tiered"] = T("tiered")
        o["sip"] = T("sip"); o["spot"] = T("spot")
        o["card_spend"] = T("card_spend"); o["auths"] = T("auths")
        o["redeem_ev"] = T("redeem_ev")
        o["region"] = R

        # ── float (R205-R216) ────────────────────────────────────────────────
        daily = o["grams_bought"] / (mo * 365 / 12)
        float_req = np.maximum(2 * p["bar_grams"],
                               p["bar_grams"] + p["float_buffer_days"] * daily)
        o["float_grams"] = float_req
        o["float_usd"] = float_req * gold * (1 + p["fab_premium"])
        cash_float = np.maximum(0.0, np.diff(float_req, prepend=0.0))
        cash_float[0] = float_req[0]
        o["float_cash"] = cash_float * gold * (1 + p["fab_premium"])
        o["prefund"] = np.where(per >= p["act_2"],
                                np.maximum(p["prefund_min"],
                                           o["card_spend"] / 365 * p["prefund_days"]), 0.0)

        # ── COGS (R222-R228) ─────────────────────────────────────────────────
        prev_cust = np.concatenate([[0.0], o["grams_cust"][:-1]])
        returned = np.maximum(0.0, prev_cust + o["grams_bought"] - o["grams_cust"])
        net_new = np.maximum(0.0, o["grams_bought"] - returned * (1 - p["sw_premium_gross"]))
        o["net_new_grams"] = net_new
        fab = net_new * gold * p["fab_premium"] * p["sw_premium_aurumix"]

        # SELL-BACK (added 2026-09-02, client-agreed). The recycling credit is
        # bounded by demand: redeemed grams above what new purchases absorb
        # cannot sit in the float unpriced - they are sold back to the dealer
        # at a two-way spread. Zero at base rates (redemptions < purchases);
        # a real cash cost in a redemption run. Spread swept 0.5/1.0/2.0%.
        excess = np.maximum(0.0, returned - o["grams_bought"])
        o["excess_redeemed_grams"] = excess
        o["sellback_cost"] = excess * gold * p.get("buyback_spread", 0.01)
        o["cogs"] = fab + o["sellback_cost"]

        # ── opex (R232-R255) ─────────────────────────────────────────────────
        metal = o["grams_cust"] + float_req
        vault = np.maximum(p["vault_min_daily"] * mo * 365 / 12,
                           p["vault_fee"] * metal * gold * mo / 12)
        jan = (self.cal_month == 1) | (self.cal_month == 0)
        vara = np.where(jan, p["vara_supervision_aed"] / p["aed_usd"], 0.0)
        dmcc = np.where(jan, p["dmcc_licence_aed"] / p["aed_usd"], 0.0)
        kyc = np.maximum(p["kyc_monthly_min"] * mo, p["kyc_per_check"] * o["new"])
        oneoff = np.where(per == 1,
                          (p["vara_application_aed"] + p["dmcc_incorporation_aed"])
                          / p["aed_usd"] + p["launch_audit"], 0.0)
        insurance = p["insurance"] * mo / 12
        audit = p["audit"] * mo / 12
        tech_audit = p["tech_audit"] * mo / 12
        redemption_handling = o["redeem_ev"] * p["redemption_unit_cost"]
        tech_build = np.where(self.year == 1, p["tech_build_y1"] / 12 * mo,
                              np.where(self.year == 2, p["tech_build_y2"] / 12 * mo, 0.0))
        tech_maint = np.where(self.year >= 3, p["tech_maint"] / 12 * mo, 0.0)
        o["opex"] = (vault + vara + dmcc + kyc + oneoff + insurance + audit
                     + tech_audit + redemption_handling + tech_build + tech_maint)
        o["opex_parts"] = dict(vault=vault, vara=vara, dmcc=dmcc, kyc=kyc,
                               oneoff=oneoff, insurance=insurance, audit=audit,
                               tech_audit=tech_audit, redemption=redemption_handling,
                               tech_build=tech_build, tech_maint=tech_maint)

        # ── ICS giveback (R259-R267) ─────────────────────────────────────────
        book = o["paying"] + o["holders"]
        qual = np.where(book > 0, o["tiered"] / np.maximum(book, 1e-12), 0.0)
        o["qual_share"] = qual
        ics_entry = o["s1a"] * qual * p["ics_disc_entry"]
        ics_card = o["s4"] * qual * p["ics_disc_card"]
        ics_rebate = (o["s2"] + o["s4"]) * qual * p["ics_disc_rebate"]
        ics_family = o["s3"] * qual * p["ics_disc_family"]
        o["ics_cost"] = ics_entry + ics_card + ics_rebate + ics_family
        o["ics_parts"] = dict(entry=ics_entry, card=ics_card,
                              rebate=ics_rebate, family=ics_family)

        # ── acquisition costs (R272-R283) ────────────────────────────────────
        mkt = np.array([p["marketing_spend"][y] for y in yr]) / 12 * mo
        agent_now = T("agent_acq")
        cum_agent = np.cumsum(agent_now)
        agent_share = np.where(o["cum_ever"] > 0, cum_agent / o["cum_ever"], 0.0)
        agent_comm = (o["s1a"] + o["s1b"]) * agent_share * p["agent_commission"]
        ref_reward = ((R["UAE"]["ref_acq"] * p["ticket_uae"]
                       + R["Gulf"]["ref_acq"] * p["ticket_gulf"]
                       + R["India"]["ref_acq"] * p["ticket_india"])
                      * 6 * p["entry_fee"] * p["referral_reward"])
        o["acq_cost"] = mkt + agent_comm + ref_reward
        o["acq_parts"] = dict(marketing=mkt, agent_comm=agent_comm, referral=ref_reward)

        # ── card programme (R288-R298) ───────────────────────────────────────
        cards_new_t = T("cards_new")
        platform = np.where(per >= p["act_2"], p["card_platform_fee"] * mo / 12, 0.0)
        setup = np.where(per == p["act_2"], p["card_setup"], 0.0)
        production = cards_new_t * p["card_per_card"]
        auth_cost = o["auths"] * p["card_per_auth"]
        fraud = o["card_spend"] * p["card_fraud"]
        xborder = ((R["Gulf"]["card_spend"] + R["India"]["card_spend"]
                    + R["UAE"]["card_spend"] * p["uae_spend_abroad"]) * p["xborder_fee"])
        o["card_cost"] = platform + setup + production + auth_cost + fraud + xborder

        # ── totals (R301-R342) ───────────────────────────────────────────────
        o["cost_modelled"] = o["cogs"] + o["opex"] + o["ics_cost"] + o["acq_cost"] + o["card_cost"]
        o["contingency"] = o["cost_modelled"] * p["contingency"]
        o["cost_total"] = o["cost_modelled"] + o["contingency"]
        o["net_profit"] = o["revenue"] - o["cost_total"]
        o["cum_profit"] = np.cumsum(o["net_profit"])

        capital = (p["capital_issuance_aed"] + p["capital_activities_aed"]) / p["aed_usd"]
        o["capital_tied"] = o["float_usd"] + capital + o["prefund"]
        o["funding"] = np.maximum(0.0, -o["cum_profit"]) + o["capital_tied"]
        o["peak_funding"] = np.maximum.accumulate(o["funding"])
        return o

    # ── annual aggregation for Summary comparison ────────────────────────────

    def annual(self, key, how="sum"):
        v = self.out[key]
        years = self.year.astype(int)
        out = []
        for y in range(1, 8):
            mask = years == y
            out.append(v[mask].sum() if how == "sum" else v[mask][-1])
        return np.array(out)
