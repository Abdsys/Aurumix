"""
The digital twin: one system, eighty-four monthly steps.

This replaces the two-engine architecture. There used to be a port of the Phase 4
workbook running the business on averages across a 29-column grid, with a
population of individual customers running alongside it and a lookup table
passing values between them. That split existed for two reasons, and neither
survived inspection:

  - "the workbook's numbers are what the client approved, so keep them as the
    centre case." Fair, but that is an argument for a reconciliation report, not
    for a second copy of the business inside the runtime.
  - "running the population inside every path would take hours." Measured: 0.3
    seconds. The whole Monte Carlo is about ten minutes. The claim was wrong and
    it was never checked.

The workbook is the DESCRIPTION of the system. The twin is the system RUNNING.
So every rule in the workbook lives here, and the rule is:

    Anything that depends on a customer is computed ON CUSTOMERS.
    Anything that is a genuine fixed company cost is a monthly schedule.
    Nothing is ever computed as an average customer times a head count.

That distinction is the whole design. The vault bill is charged on the grams the
agents actually hold. Interchange is earned on what they actually spend. The
loyalty giveback is priced at the tier each of them actually reached. The
fabrication premium is paid on the grams actually bought net of the grams
actually redeemed. None of it passes through an average.

What is still taken from the workbook: PARAMETERS. Prices, fees, the VARA and
DMCC licence costs, the vault contract, the interchange rate, salary lines,
the marketing budget. Those are facts about the business and keeping a second
copy of them would only create drift.

The 29-period grid is gone. It was a spreadsheet's column count. It mattered
because peak funding is the deepest point of a cash line, and on that grid the
last sixty months were five observations, so the true trough was invisible and
the raise number could only be understated.
"""

import numpy as np

from config import config as C
from src.detmodel import load_params
from src.entities import build_cohort
from src import mechanics as M
from src.agentbook import LADDER, REF_TENURE_DEAD, REF_TENURE_FULL, REFERRAL_TIER_MULT

REGION_NAMES = ("UAE", "Gulf", "India")
REGION_KEYS = (
    dict(cac0="cac_uae", cac7="cac_uae_y7", mkt="mkt_share_uae", agents="agents_uae",
         ceiling="ceiling_uae", ticket="ticket_uae", spot_ticket="spot_ticket_uae",
         spot_attach="spot_attach_uae", opens="act_0"),
    dict(cac0="cac_gulf", cac7="cac_gulf_y7", mkt="mkt_share_gulf", agents="agents_gulf",
         ceiling="ceiling_gulf", ticket="ticket_gulf", spot_ticket="spot_ticket_gulf",
         spot_attach="spot_attach_gulf", opens="act_gulf"),
    dict(cac0="cac_india", cac7="cac_india_y7", mkt="mkt_share_india", agents="agents_india",
         ceiling="ceiling_india", ticket="ticket_india", spot_ticket="spot_ticket_india",
         spot_attach="spot_attach_india", opens="act_india"),
)

# Referral capacity is now a per-customer property, so `referral_rate` has to be
# read as the rate for ONE fully-tenured customer rather than for the book
# average. This constant converts between the two: it is the average weight of a
# matured book, so dividing by it keeps the workbook's quoted number meaning what
# it meant at the point it was quoted. Verified against the run: the book-average
# weight settles near this value by month 84.
REF_MATURE_WEIGHT = 1.30


def scaled_archetypes(persistency, background=None):
    """
    Rescale every archetype hazard by ONE factor so that a cohort's month-13
    persistency lands on the target.

    One factor, not five free parameters. Fitting the hazards independently
    produced a "perfect payer" who never left and an "alternating misser" who
    made up half the book: a better fit to one number and a worse description of
    anything. The mix and the ordering are preserved; only the level moves.
    """
    from scipy.optimize import brentq
    bg = C.BACKGROUND_HAZARD["base"] if background is None else background
    w = np.array([a.weight for a in C.ARCHETYPES_BASE])
    tot = np.array([a.own_hazard for a in C.ARCHETYPES_BASE]) + bg

    def surv13(k):
        return float((w * (1 - np.clip(tot * k, 0, 0.99)) ** 12).sum())

    k = brentq(lambda k: surv13(k) - float(persistency), 0.05, 5.0)
    A = type(C.ARCHETYPES_BASE[0])
    return [A(a.name, a.weight, a.pay_prob,
              max(0.0, (a.own_hazard + bg) * k - bg * k),
              a.pay_decay, a.pay_floor) for a in C.ARCHETYPES_BASE]


class Twin:
    """
    One run of the whole business, month by month.

    Every output is an 84-length array on a true monthly clock. Nothing is
    aggregated to years until a report asks for it.
    """

    def __init__(self, p=None, overrides=None, seed=20270101, scale=25.0,
                 ladder=None, archetypes=None, gold_monthly=None,
                 rho_quality=0.0, prefunded_share=C.RAIL_PREFUNDED_SHARE,
                 discipline_shift=C.RAIL_DISCIPLINE_SHIFT,
                 card_dormancy_monthly=0.0, months=C.HORIZON_MONTHS):
        self.p = dict(p if p is not None else load_params())
        if overrides:
            self.p.update(overrides)
        self.seed = int(seed)
        self.rng = np.random.default_rng(seed)
        self.scale = float(scale)
        self.months = int(months)
        self.ladder = ladder or LADDER
        self.archetypes = archetypes or scaled_archetypes(
            self.p.get("persistency", 0.63))
        self.rho = float(rho_quality)
        self.prefunded_share = prefunded_share
        self.discipline_shift = discipline_shift
        self.card_dormancy = float(card_dormancy_monthly)
        self.gold_monthly = gold_monthly
        self.pool = None

    # ── helpers ──────────────────────────────────────────────────────────────

    def _year(self, t):
        """Calendar year index 0..6 for month t (1-based)."""
        return min((t - 1) // 12, 6)

    def _cal_month(self, t):
        """1..12, for seasonality. Month 1 is January 2027."""
        return ((t - 1) % 12) + 1

    def _gold(self, t):
        if self.gold_monthly is not None:
            return float(self.gold_monthly[t - 1])
        return self.p["gold_price_m1"] * (1.0 + self.p["gold_appreciation"]) ** ((t - 1) / 12.0)

    def _season(self, raw, amplitude, cal_month):
        """The workbook's seasonality shape, normalised so a year sums to 12."""
        v = np.array(raw, dtype=float)
        adj = 1.0 + (v - 1.0) * amplitude
        adj = adj * 12.0 / adj.sum()
        return float(adj[cal_month - 1])

    # ── acquisition: how many customers arrive this month ────────────────────

    def _acquire_count(self, t, region_idx, cum_ever_region, paying_weight_region):
        """
        New customers in one region this month.

        Three channels, then the market brake:

            direct   = regional marketing spend / cost per customer
            referral = the book's own referral capacity, per customer
            agents   = field agents x productivity x ramp

        Cost per customer is NOT flat. The workbook ramps it down as spend rises
        eighteen-fold over the horizon, which is only true while cheap channels
        last. Past them the marginal customer costs more to reach, so cost rises
        with regional spend intensity (workbook D27, retired to Phase 5).
        """
        p, rg = self.p, REGION_KEYS[region_idx]
        y = self._year(t)
        if t < int(p[rg["opens"]]):
            return 0.0

        spend_m = p["marketing_spend"][y] * p[rg["mkt"]] / 12.0
        cac = p[rg["cac0"]] + (p[rg["cac7"]] - p[rg["cac0"]]) * y / 6.0
        if p.get("cac_conv_coef"):
            cac *= (1.0 + p["cac_conv_coef"]
                    * (spend_m / p.get("cac_conv_ref", 60000.0)) ** p.get("cac_conv_exp", 0.7))
        direct = spend_m / cac * (1.0 + p["organic_share"])

        ref = 0.0
        if t >= int(p["act_referral"]):
            # paying_weight_region is the summed per-customer referral weight,
            # so this is the book referring at its own rate, not a head count
            # multiplied by an average.
            ref = (paying_weight_region * p["referral_rate"] / REF_MATURE_WEIGHT
                   / 12.0 * p["referral_conversion"])

        agents = p[rg["agents"]][y] * p["agent_productivity"] * p["agent_ramp"][y]

        raw = direct + ref + agents
        ceiling = p[rg["ceiling"]] * p.get("ceiling_mult", 1.0)
        sat = max(0.0, 1.0 - cum_ever_region / ceiling)
        return raw * sat * self._season(p["season_acq"], p["seasonality_amplitude"], self._cal_month(t))

    # ── the run ──────────────────────────────────────────────────────────────

    def run(self):
        p, rng = self.p, self.rng
        T, scale = self.months, self.scale
        lad = self.ladder

        def z():
            return np.zeros(T)

        o = {k: z() for k in (
            "gold_price", "new", "paying", "holders", "cum_ever", "cards", "cards_new",
            "grams_held", "grams_cust", "grams_bought", "aum", "tiered", "sip", "spot",
            "card_spend", "auths", "redeem_ev", "selfcustody_ev", "family_subs",
            "s1a", "s1b", "s2", "s3", "s4", "s5", "s6", "revenue",
            "cogs", "opex", "ics_cost", "acq_cost", "card_cost", "contingency",
            "cost_modelled", "cost_certain", "cost_uncertain", "cost_total",
            "net_profit", "cum_profit",
            "float_grams", "float_usd", "prefund", "capital_tied", "funding",
            "peak_funding", "net_new_grams", "sellback_cost", "excess_redeemed_grams",
            "qual_share", "partners", "ref_acq", "agent_acq", "direct_acq",
            "orig_usd", "credit_limit", "lapsed", "grams_redeemed")}
        o["ics_parts"] = {k: z() for k in ("entry", "card", "rebate", "family")}
        o["tier_mix"] = np.zeros((T, 5))          # live book by tier, each month
        o["gated_share"] = z()                    # share who have opened the gate
        o["opex_parts"] = {k: z() for k in (
            "vault", "vara", "dmcc", "kyc", "oneoff", "launch_audit", "insurance", "audit",
            "tech_audit", "redemption", "tech_build", "tech_maint")}
        o["acq_parts"] = {k: z() for k in ("marketing", "agent_comm", "referral")}
        o["region"] = {n: {k: z() for k in ("new", "paying", "cum", "card_spend")}
                       for n in REGION_NAMES}

        cum_ever_r = np.zeros(3)
        pool = None
        # Partners are individual entities: each carries its own signing month
        # and its own size. Sizes draw from a dedicated RNG stream so adding a
        # partner never perturbs the customer dice.
        partner_book = []          # list of (sign_month, aum_of_this_partner)
        rng_partner = np.random.default_rng(self.seed + 777)
        prev_cards = 0.0
        prev_grams_cust = 0.0
        agent_acquired_cum = 0.0

        # per-month referral weight of the book, by region, from last month
        ref_weight_r = np.zeros(3)

        for t in range(1, T + 1):
            gold = self._gold(t)
            o["gold_price"][t - 1] = gold
            y, cm = self._year(t), self._cal_month(t)

            # ── 1. acquisition ───────────────────────────────────────────────
            new_by_region = np.zeros(3)
            for r in range(3):
                n = self._acquire_count(t, r, cum_ever_r[r], ref_weight_r[r])
                new_by_region[r] = n
                cum_ever_r[r] += n
                o["region"][REGION_NAMES[r]]["new"][t - 1] = n
                o["region"][REGION_NAMES[r]]["cum"][t - 1] = cum_ever_r[r]
            o["new"][t - 1] = new_by_region.sum()
            o["cum_ever"][t - 1] = cum_ever_r.sum()

            for r in range(3):
                k = int(round(new_by_region[r] / scale))
                if k <= 0:
                    continue
                cohort = build_cohort(
                    rng, k, self.archetypes, C.BACKGROUND_HAZARD["base"],
                    region_idx=r, born_month=t, prefunded_share=self.prefunded_share,
                    discipline_shift=self.discipline_shift,
                    ticket_mean=[p["ticket_uae"], p["ticket_gulf"], p["ticket_india"]][r])
                pool = cohort if pool is None else _merge(pool, cohort)

            if pool is None:
                continue
            self._grow_flags(pool)

            # ── 2. who pays, and what that buys ──────────────────────────────
            live = pool.alive & pool.sip_active
            age = np.maximum(t - pool.born_month, 0)
            pay_p = np.maximum(pool.pay_prob0 * pool.pay_decay ** age, pool.pay_floor)
            # Payment discipline is the number the retail margin lives on: the
            # book pays in ~78% of the months it could, and no source pins that
            # figure. The persistency anchor pins who LEAVES, not how often the
            # stayers pay. So discipline is swept like any other unsourced
            # driver, as one multiplier on every archetype's pay probability.
            pay_p = np.clip(pay_p * p.get("pay_prob_mult", 1.0), 0.005, 0.999)
            # A run pauses CONTRIBUTIONS as well as pulling gold out. The old
            # engine faked the pause by cutting the average ticket to $13, which
            # the twin cannot do because a ticket below the $20 floor cannot
            # exist. A customer who pauses does not pay less, they skip months,
            # and skipping is a pay-probability event.
            if (p.get("panic_period") is not None
                    and 0 <= t - int(p["panic_period"]) < int(p.get("panic_months", 6))):
                pay_p = pay_p * p.get("panic_pay_mult", 1.0)
            if self.rho > 0:
                pay_p = np.clip(pay_p + self.rho * 0.05 * pool.quality, 0.01, 0.999)
            counted = live & (rng.random(pool.n) < pay_p)

            amount = M.monthly_ticket(rng, pool.ticket_base)
            contrib = np.where(counted, amount, 0.0)

            pool.streak = np.where(counted, np.minimum(pool.streak + 1, C.GATE_RUN),
                                   0).astype(np.int8)
            newly = (~pool.gated) & (pool.streak >= C.GATE_RUN)
            pool.gate_month[newly] = t
            pool.gated |= newly
            pool.months_counted[newly] = C.GATE_RUN
            pool.months_counted[counted & pool.gated & ~newly] += 1
            pool.recent.push(counted)

            # ── 3. spot purchases, drawn per customer ────────────────────────
            spot_val = np.zeros(pool.n)
            if t >= int(p["act_1b"]):
                attach = np.array([p["spot_attach_uae"], p["spot_attach_gulf"],
                                   p["spot_attach_india"]])[pool.region]
                sticket = np.array([p["spot_ticket_uae"], p["spot_ticket_gulf"],
                                    p["spot_ticket_india"]])[pool.region]
                prob = np.clip(attach * p["spot_attach_mult"] * p["spot_frequency"] / 12.0,
                               0.0, 1.0)
                if self.rho > 0:
                    prob = np.clip(prob * (1 + 0.3 * self.rho * pool.quality), 0.0, 1.0)
                hit = (pool.alive & pool.sip_active & (rng.random(pool.n) < prob))
                # Amounts vary per purchase the way SIP tickets vary per month:
                # a mean-preserving lognormal wobble, so the regional average
                # holds while individual purchases spread around it.
                noise = np.exp(0.25 * rng.normal(size=pool.n) - 0.5 * 0.25 ** 2)
                spot_val = np.where(hit, sticket * p["spot_ticket_mult"] * noise, 0.0)

            # ── 4. money becomes gold, at that customer's tier ───────────────
            entry_rate = lad["entry_fee"][pool.tier]
            gross = contrib + spot_val
            prem_div = 1.0 + p["fab_premium"] * (1.0 - p["sw_premium_aurumix"])
            bought_g = gross * (1.0 - entry_rate) / gold / prem_div
            pool.grams += bought_g
            pool.grams_acquired_ytd += bought_g

            # ── 5. redemption and self-custody, per customer ─────────────────
            hold_mult = np.where(pool.sip_active, 1.0, C.HOLDER_REDEMPTION_MULTIPLIER)
            red_p = p["redemption_rate"] / 12.0 * hold_mult
            if p.get("panic_period") is not None and t == int(p["panic_period"]):
                red_p = np.minimum(1.0, red_p + p.get("panic_share", 0.0))
            if self.rho > 0:
                red_p = np.clip(red_p * (1 - 0.5 * self.rho * pool.quality), 0.0, 1.0)
            redeemed = pool.alive & (rng.random(pool.n) < red_p)
            # a redemption takes a slice of the holding, not all of it
            red_g = np.where(redeemed, pool.grams * p.get("redemption_frac", 0.25), 0.0)
            pool.grams -= red_g
            # SELF-CUSTODY IS A TOKEN WITHDRAWAL, NOT A DELIVERY. Aurumix offers
            # no physical delivery (client instruction, 2026-09-03). A customer
            # moving AURX to their own wallet still owns vaulted metal: the
            # vault bill keeps running on it, and no handling event happens.
            # What changes is visibility: off-platform tokens leave the
            # collateral base, so the credit line and the AUM figure shrink.
            self_cust = pool.alive & (rng.random(pool.n) < p["self_custody_rate"] / 12.0)
            selfc_g = np.where(self_cust, pool.grams * p.get("redemption_frac", 0.25), 0.0)
            pool.grams -= selfc_g
            pool.grams_self += selfc_g

            # ── 6. score and tier ────────────────────────────────────────────
            # Retention watches gold kept ON THE PLATFORM (client rule,
            # 2026-09-03): selling back AND moving tokens to your own wallet
            # both reduce it. The score rewards keeping your savings where the
            # relationship is, not merely owning gold somewhere.
            denom = pool.grams_year_open + pool.grams_acquired_ytd
            sold = np.where(denom > 0, 1 - pool.grams / np.maximum(denom, 1e-12), 0.0)
            pool.ics = M.ics_score(pool.months_counted, pool.recent.recent(), sold, pool.gated)
            pool.tier = M.tier_index(pool.ics)
            if t % 12 == 0:
                pool.grams_year_open = pool.grams.copy()
                pool.grams_acquired_ytd[:] = 0.0

            # ── 7. lapse ─────────────────────────────────────────────────────
            lapse = live & (rng.random(pool.n) < pool.hazard)
            pool.sip_active &= ~lapse
            o["lapsed"][t - 1] = lapse.sum() * scale

            alive = pool.alive
            paying = alive & pool.sip_active
            holders = alive & ~pool.sip_active

            # ── 8. cards ─────────────────────────────────────────────────────
            card_spend = np.zeros(pool.n)
            auths = np.zeros(pool.n)
            new_cards = np.zeros(pool.n, dtype=bool)
            if t >= int(p["act_2"]):
                fresh = alive & ~pool.card_active & ~pool.card_drawn_flag
                take = p["facility_takeup"]
                if self.rho > 0:
                    take = np.clip(take * (1 + 0.4 * self.rho * pool.quality), 0, 1)
                new_cards = fresh & (rng.random(pool.n) < take)
                pool.card_active |= new_cards
                pool.card_drawn_flag |= fresh
                if self.card_dormancy > 0:
                    pool.card_active &= ~(pool.card_active
                                          & (rng.random(pool.n) < self.card_dormancy))
                has_card = pool.card_active & alive
                limit = pool.grams * gold * lad["ltv"][pool.tier]
                sc = self._season(p["season_card"], p["seasonality_amplitude"], cm)
                card_spend = np.where(
                    has_card, limit * p["drawn_pct"] * p["draws_per_year"] / 12.0 * sc, 0.0)
                if self.rho > 0:
                    card_spend *= np.clip(1 + 0.3 * self.rho * pool.quality, 0.2, 3.0)
                auths = np.where(has_card, p["draws_per_year"] * p["txn_per_draw"] / 12.0
                                 * (1 + p["decline_uplift"]), 0.0)

            # ── 9. family plan ───────────────────────────────────────────────
            fam_price = (p["family_price"] + max(0.0, p["beneficiaries"] - 1)
                         * p["beneficiary_fee"]) / 12.0
            fam_rev = np.zeros(pool.n)
            if t >= int(p["act_3"]):
                joiners = (pool.born_month == t) & (rng.random(pool.n) < p["family_attach"])
                pool.family_flag |= joiners
                # CANCELLATION only. The workbook's family_churn_monthly bundles
                # cancelling the plan WITH lapsing the SIP, because it has no way
                # to know which subscribers are still on the platform. The twin
                # knows: the `alive` mask below already removes the ones who left.
                # Using the bundled rate here would kill them twice.
                fam_cancel_m = 1.0 - (1.0 - p["family_cancel"]) ** (1.0 / 12.0)
                pool.family_flag &= ~(pool.family_flag
                                      & (rng.random(pool.n) < fam_cancel_m))
                fam_rev = np.where(pool.family_flag & alive & pool.sip_active, fam_price, 0.0)

            # ── 10. the revenue streams, all per customer ────────────────────
            # Streams are booked at the STANDARD price. The tier discount is a
            # cost line (section 11), never a reduction here, or it lands twice.
            s1a = contrib * C.ENTRY_FEE
            s1b = spot_val * C.ENTRY_FEE

            ic_rate = min(p["interchange"], 0.01) if p["sw_prepaid"] == 1 else p["interchange"]
            s2 = card_spend * ic_rate * (1 - p["pm_share"])

            s3 = fam_rev

            atm_excess = sum(p[f"atm_share_{k}"]
                             * max(0.0, p[f"atm_mid_{k}"] - p["atm_allowance_aed"])
                             for k in (1, 2, 3, 4))
            has_card = pool.card_active & alive
            s4 = np.zeros(pool.n)
            if t >= int(p["act_4"]):
                s4 = (card_spend * p["foreign_spend_mean"] * p["fx_margin"]
                      + np.where(has_card, atm_excess * p["atm_fee"] / p["aed_usd"], 0.0)
                      + np.where(new_cards, p["card_issuance_aed"] / p["aed_usd"], 0.0)
                      + np.where(has_card,
                                 (p["reissue_rate"] * p["card_issuance_aed"]
                                  + p["replacement_rate"] * p["card_replacement_aed"])
                                 / 12.0 / p["aed_usd"], 0.0))

            s5 = np.zeros(pool.n)
            if t >= int(p["act_5"]):
                limit = pool.grams * gold * lad["ltv"][pool.tier]
                drawn_bal = np.where(has_card, limit * (1 - p["sw_prepaid"])
                                     * p["drawn_pct"] * p["facility_turnover"], 0.0)
                draw_yr = np.where(has_card, limit * p["drawn_pct"] * p["draws_per_year"], 0.0)
                s5 = (drawn_bal * p["credit_serv_gross"] * p["credit_serv_share"]
                      + draw_yr * (1 - p["sw_prepaid"]) * p["credit_orig_gross"]
                      * p["credit_orig_share"]) / 12.0
                # New credit written this month, in dollars, from the actual
                # holdings it is secured against. The margin-call model used to
                # reconstruct this from annual aggregates and spread it evenly
                # across the year, which cannot see a bad quarter.
                o["orig_usd"][t - 1] = (draw_yr / 12.0).sum() * scale
                o["credit_limit"][t - 1] = limit[has_card].sum() * scale

            # ── 11. the loyalty giveback, at the tier each customer reached ──
            g_entry = contrib * (C.ENTRY_FEE - entry_rate)
            g_card = card_spend * p["foreign_spend_mean"] * (0.02 - lad["fx_margin"][pool.tier])
            g_rebate = card_spend * lad["rewards"][pool.tier]
            g_family = np.where(pool.family_flag & alive & pool.sip_active,
                                fam_price * lad["family_disc"][pool.tier], 0.0)
            # THE CASHBACK CAP (client rule, corrected 2026-09-03): the gold
            # cashback is capped against the customer's OWN card transactions,
            # not against their whole relationship. The net take on a dollar of
            # spend (interchange net of the scheme's share, plus the FX margin)
            # runs about twice the top cashback rate, so at quoted rates the
            # structure satisfies the cap by itself and it never binds at base.
            # It stays enforced anyway: a generous ladder sweep or a low
            # interchange draw can push rewards past the per-transaction take,
            # and this is the rail that stops a path from paying customers to
            # spend.
            card_take = s2 + card_spend * p["foreign_spend_mean"] * lad["fx_margin"][pool.tier]
            g_rebate = np.minimum(g_rebate, card_take)
            pool.econ_rev += (s1a + s1b + s2 + s3 + s4 + s5)
            pool.econ_give += (g_entry + g_card + g_family + g_rebate)

            # ── 12. partners: individual sizes, adoption that ramps ──────────
            # Each partner is its own entity. Size = the world's systematic draw
            # times a personal lognormal factor with mean one, so a book can
            # hold a whale and three minnows around the same average. Revenue
            # climbs linearly to full power over partner_ramp_months, because
            # a signed partner's users do not adopt overnight - and the ramp is
            # the expensive kind of honesty: it moves B2B money later while the
            # raise is set by the early years.
            if t >= int(p["act_6"]):
                target = int(p["b2b_partners"][y])
                sg = p.get("partner_size_sigma", 0.5)
                while len(partner_book) < target:
                    size = (p["partner_aum"]
                            * rng_partner.lognormal(-0.5 * sg * sg, sg))
                    partner_book.append((t, size))
            ramp_m = float(p.get("partner_ramp_months", 18.0))
            s6 = sum(aum * min(1.0, (t - m0 + 1) / ramp_m)
                     for m0, aum in partner_book) * p["b2b_fee"] / 12.0
            o["partners"][t - 1] = len(partner_book)

            # ── 13. book aggregates, summed from real customers ──────────────
            S = scale
            n_pay = paying.sum() * S
            n_hold = holders.sum() * S
            n_card = has_card.sum() * S
            grams_total = (pool.grams[alive].sum()) * S
            grams_cust_t = ((pool.grams + pool.grams_self)[alive].sum()) * S
            grams_bought_t = bought_g.sum() * S
            # only REDEEMED metal comes back to Aurumix for recycling; a token
            # withdrawal moves nothing physical anywhere
            returned_g = red_g.sum() * S
            o["grams_redeemed"][t - 1] = returned_g

            o["paying"][t - 1] = n_pay
            o["holders"][t - 1] = n_hold
            o["cards"][t - 1] = n_card
            o["cards_new"][t - 1] = new_cards.sum() * S
            o["grams_held"][t - 1] = grams_total
            o["grams_cust"][t - 1] = grams_cust_t
            o["grams_bought"][t - 1] = grams_bought_t
            # AUM counts ALL customer gold under custody, self-custodied tokens
            # included: the metal is vaulted and unredeemed (client rule,
            # 2026-09-03). What is account-tied is the ICS score and the credit
            # collateral, which read platform-held grams only.
            o["aum"][t - 1] = grams_cust_t * gold
            o["tiered"][t - 1] = (alive & (pool.tier > 0)).sum() * S
            o["qual_share"][t - 1] = (float((pool.tier[alive] > 0).mean())
                                      if alive.any() else 0.0)
            o["tier_mix"][t - 1] = np.bincount(pool.tier[alive], minlength=5) * S
            o["gated_share"][t - 1] = (float(pool.gated[alive].mean())
                                       if alive.any() else 0.0)
            o["sip"][t - 1] = contrib.sum() * S
            o["spot"][t - 1] = spot_val.sum() * S
            o["card_spend"][t - 1] = card_spend.sum() * S
            o["auths"][t - 1] = auths.sum() * S
            o["redeem_ev"][t - 1] = redeemed.sum() * S
            o["selfcustody_ev"][t - 1] = self_cust.sum() * S
            o["family_subs"][t - 1] = (pool.family_flag & alive & pool.sip_active).sum() * S

            for key, arr in (("s1a", s1a), ("s1b", s1b), ("s2", s2),
                             ("s3", s3), ("s4", s4), ("s5", s5)):
                o[key][t - 1] = arr.sum() * S
            o["s6"][t - 1] = s6
            o["revenue"][t - 1] = sum(o[k][t - 1] for k in
                                      ("s1a", "s1b", "s2", "s3", "s4", "s5", "s6"))

            for key, arr in (("entry", g_entry), ("card", g_card),
                             ("rebate", g_rebate), ("family", g_family)):
                o["ics_parts"][key][t - 1] = arr.sum() * S
            o["ics_cost"][t - 1] = sum(o["ics_parts"][k][t - 1]
                                       for k in ("entry", "card", "rebate", "family"))

            for r in range(3):
                m_r = alive & (pool.region == r)
                o["region"][REGION_NAMES[r]]["paying"][t - 1] = (m_r & paying).sum() * S
                o["region"][REGION_NAMES[r]]["card_spend"][t - 1] = card_spend[m_r].sum() * S
                w = _ref_weight(pool, t, m_r & paying)
                ref_weight_r[r] = w * S

            # ── 14. the float, sized off real purchases ──────────────────────
            daily = grams_bought_t / (365.0 / 12.0)
            float_req = max(2 * p["bar_grams"],
                            p["bar_grams"] + p["float_buffer_days"] * daily)
            o["float_grams"][t - 1] = float_req
            o["float_usd"][t - 1] = float_req * gold * (1 + p["fab_premium"])
            o["prefund"][t - 1] = (max(p["prefund_min"],
                                       o["card_spend"][t - 1] / 365 * p["prefund_days"])
                                   if t >= int(p["act_2"]) else 0.0)

            # ── 15. cost of goods, on real grams ─────────────────────────────
            net_new = max(0.0, grams_bought_t - returned_g * (1 - p["sw_premium_gross"]))
            o["net_new_grams"][t - 1] = net_new
            fab = net_new * gold * p["fab_premium"] * p["sw_premium_aurumix"]
            excess = max(0.0, returned_g - grams_bought_t)
            o["excess_redeemed_grams"][t - 1] = excess
            o["sellback_cost"][t - 1] = excess * gold * p.get("buyback_spread", 0.01)
            o["cogs"][t - 1] = fab + o["sellback_cost"][t - 1]

            # ── 16. operating costs: real where they scale, schedule where not
            metal = grams_cust_t + float_req
            vault = max(p["vault_min_daily"] * 365 / 12,
                        p["vault_fee"] * metal * gold / 12)
            jan = 1 if cm == 1 else 0
            parts = o["opex_parts"]
            parts["vault"][t - 1] = vault
            parts["vara"][t - 1] = jan * p["vara_supervision_aed"] / p["aed_usd"]
            parts["dmcc"][t - 1] = jan * p["dmcc_licence_aed"] / p["aed_usd"]
            parts["kyc"][t - 1] = max(p["kyc_monthly_min"],
                                      p["kyc_per_check"] * o["new"][t - 1])
            # split so the launch audit, which is a quote rather than a fee
            # schedule, can carry contingency while the statutory fees do not
            parts["oneoff"][t - 1] = ((p["vara_application_aed"] + p["dmcc_incorporation_aed"])
                                      / p["aed_usd"]) if t == 1 else 0.0
            parts["launch_audit"][t - 1] = p["launch_audit"] if t == 1 else 0.0
            parts["insurance"][t - 1] = p["insurance"] / 12
            parts["audit"][t - 1] = p["audit"] / 12
            parts["tech_audit"][t - 1] = p["tech_audit"] / 12
            parts["redemption"][t - 1] = o["redeem_ev"][t - 1] * p["redemption_unit_cost"]
            parts["tech_build"][t - 1] = (p["tech_build_y1"] / 12 if y == 0 else
                                          p["tech_build_y2"] / 12 if y == 1 else 0.0)
            parts["tech_maint"][t - 1] = p["tech_maint"] / 12 if y >= 2 else 0.0
            o["opex"][t - 1] = sum(v[t - 1] for v in parts.values())

            # ── 17. acquisition cost, attributed to who it bought ────────────
            ap = o["acq_parts"]
            ap["marketing"][t - 1] = p["marketing_spend"][y] / 12
            agent_new = sum(p[REGION_KEYS[r]["agents"]][y] * p["agent_productivity"]
                            * p["agent_ramp"][y] for r in range(3))
            agent_acquired_cum += agent_new
            ashare = (agent_acquired_cum / o["cum_ever"][t - 1]
                      if o["cum_ever"][t - 1] > 0 else 0.0)
            ap["agent_comm"][t - 1] = ((o["s1a"][t - 1] + o["s1b"][t - 1])
                                       * min(ashare, 1.0) * p["agent_commission"])
            ref_new = (ref_weight_r.sum() * p["referral_rate"] / REF_MATURE_WEIGHT / 12.0
                       * p["referral_conversion"]) if t >= int(p["act_referral"]) else 0.0
            o["ref_acq"][t - 1] = ref_new
            o["agent_acq"][t - 1] = agent_new
            mean_ticket = (o["sip"][t - 1] / n_pay) if n_pay > 0 else 0.0
            ap["referral"][t - 1] = (ref_new * mean_ticket * 6 * p["entry_fee"]
                                     * p["referral_reward"])
            o["acq_cost"][t - 1] = sum(v[t - 1] for v in ap.values())

            # ── 18. card programme ───────────────────────────────────────────
            if t >= int(p["act_2"]):
                xb_spend = (o["region"]["Gulf"]["card_spend"][t - 1]
                            + o["region"]["India"]["card_spend"][t - 1]
                            + o["region"]["UAE"]["card_spend"][t - 1] * p["uae_spend_abroad"])
                o["card_cost"][t - 1] = (p["card_platform_fee"] / 12
                                         + (p["card_setup"] if t == int(p["act_2"]) else 0.0)
                                         + o["cards_new"][t - 1] * p["card_per_card"]
                                         + o["auths"][t - 1] * p["card_per_auth"]
                                         + o["card_spend"][t - 1] * p["card_fraud"]
                                         + xb_spend * p["xborder_fee"])

            # ── 19. the ledger ───────────────────────────────────────────────
            # ── CONTINGENCY, APPLIED ONLY WHERE THERE IS UNCERTAINTY ─────────
            # The revenue model buffers the entire cost base by a flat
            # percentage. That prices doubt about costs nobody doubts: the
            # fabrication premium and the vault rate are contracted, the
            # licences are published fee schedules, the KYC cost is a vendor
            # price, and the loyalty giveback is a ladder we choose. Buffering
            # those inflates the retail threshold by roughly 100,000 customers
            # on nothing.
            #
            # So contingency now lands only on lines that can genuinely surprise
            # us: marketing yield, the card programme, technology, insurance and
            # audits. It concentrates the uncertainty where it belongs, which is
            # mostly on cost per acquired customer.
            certain = (o["cogs"][t - 1]              # contracted premium and spread
                       + o["ics_cost"][t - 1]        # a ladder we set
                       + ap["agent_comm"][t - 1] + ap["referral"][t - 1]
                       + sum(parts[k][t - 1] for k in
                             ("vault", "vara", "dmcc", "kyc", "oneoff", "redemption")))
            uncertain = (o["card_cost"][t - 1]
                         + ap["marketing"][t - 1]
                         + sum(parts[k][t - 1] for k in
                               ("insurance", "audit", "tech_audit", "launch_audit",
                                "tech_build", "tech_maint")))
            o["cost_certain"][t - 1] = certain
            o["cost_uncertain"][t - 1] = uncertain
            o["cost_modelled"][t - 1] = certain + uncertain
            o["contingency"][t - 1] = uncertain * p["contingency"]
            o["cost_total"][t - 1] = o["cost_modelled"][t - 1] + o["contingency"][t - 1]
            o["net_profit"][t - 1] = o["revenue"][t - 1] - o["cost_total"][t - 1]

            prev_cards = n_card
            prev_grams_cust = grams_total

        # ── the cash line, on a true monthly clock ───────────────────────────
        o["cum_profit"] = np.cumsum(o["net_profit"])
        capital = (p["capital_issuance_aed"] + p["capital_activities_aed"]) / p["aed_usd"]
        o["capital_tied"] = o["float_usd"] + capital + o["prefund"]
        o["funding"] = np.maximum(0.0, -o["cum_profit"]) + o["capital_tied"]
        o["peak_funding"] = np.maximum.accumulate(o["funding"])
        o["month"] = np.arange(1, T + 1)
        o["year"] = np.minimum((o["month"] - 1) // 12 + 1, 7)
        self.pool = pool
        self.out = o
        return o

    # ── plumbing ─────────────────────────────────────────────────────────────

    def _grow_flags(self, pool):
        """Keep the optional per-agent arrays the same length as the pool."""
        for name, dtype in (("quality", float), ("card_drawn_flag", bool),
                            ("family_flag", bool), ("econ_rev", float),
                            ("econ_give", float), ("grams_self", float)):
            cur = getattr(pool, name, None)
            if cur is None:
                setattr(pool, name, np.zeros(pool.n, dtype=dtype))
            elif cur.shape[0] < pool.n:
                pad = np.zeros(pool.n - cur.shape[0], dtype=dtype)
                if name == "quality":
                    pad = self.rng.normal(size=pool.n - cur.shape[0])
                setattr(pool, name, np.concatenate([cur, pad]))
        if self.rho > 0 and not getattr(pool, "_q_init", False):
            pool.quality = self.rng.normal(size=pool.n)
            pool._q_init = True


def _ref_weight(pool, t, mask):
    """
    The book's referral capacity: each customer's own propensity, summed.

    Zero for the first three months, full by twelve, rising up the tier ladder.
    A customer in month two cannot recommend a savings plan they have barely
    started, and advocacy tracks what the plan has actually delivered.
    """
    if not mask.any():
        return 0.0
    ramp = np.clip((t - pool.born_month - REF_TENURE_DEAD)
                   / float(REF_TENURE_FULL - REF_TENURE_DEAD), 0.0, 1.0)
    return float((ramp * REFERRAL_TIER_MULT[pool.tier])[mask].sum())


def _merge(a, b):
    from src.agentbook import _merge as m
    return m(a, b)
