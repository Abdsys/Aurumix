# Aurumix — Simulation Blueprint

**Date:** 2026-09-02
**Phase:** 5 — Simulations. Step 2 of four (classify → **blueprint** → build → document).
**Preceded by:** `Aurumix_Simulation_Classification.md` (v2), which this implements. Where the two differ, the classification's reasoning governs and this document is wrong.
**Status:** for review. ⛔ **No code is written until this is agreed.**

---

## At a Glance

| Field | Value |
|---|---|
| **Protocol** | AURX — a VARA-regulated gold-backed monthly savings product in Dubai. 1 AURX = 1 gram of allocated physical gold |
| **Architecture** | Stochastic · Hybrid (agent-based customers, aggregate everything else) · Discrete monthly · Monte Carlo **+ solver** |
| **Horizon** | 84 months. M1 = January 2027 |
| **Paths** | 1,000 base; 2,000 for tail metrics |
| **Agents** | Customers (~200k ever-acquired by M84), tracked individually |
| **Regions** | 3 — UAE, Oman & Bahrain, India |
| **Mandate** | 🔴 **PRESCRIPTIVE.** Where the design does not reach profitability, recommend changes and rank the levers by cost. **The entry fee is a lever, not a constraint** (client, 2026-09-02) |
| **Reference of record** | 🔴 **`4-revenue-modeling/tools/Aurumix_Revenue_Model_calculated.xlsx`** — the recalculated workbook, and the **only** source for any figure quoted anywhere in Phase 5. `Aurumix_Revenue_Model.xlsx` carries the formulas but its value cache is not authoritative. Both were verified structurally identical on 2026-09-02 (343 × 31, no label drift) |
| **Deliverables** | Python repo, `SIMULATION_SETUP.md`, `SIMULATION_RESULTS.md`, charts. Branding decided after findings exist |

---

## What This Simulation Does (Plain English)

The Excel model builds one average customer and multiplies them. Every UAE customer saves exactly USD 33.60 a month, and 55% of them eventually reach a benefit tier.

**This simulation builds two hundred thousand different people and lets each one live their own seven years.** Each has their own ticket, their own payment discipline, their own payment rail, and their own way in — a monthly SIP or a one-off purchase. Month by month each decides whether to pay. Some pay for four years. Some pay twice and vanish. Some pay every other month forever and never assemble the six consecutive payments a benefit tier requires.

Then the whole world runs **a thousand more times**, each with its own gold price path, its own marketing response, its own partner deals landing or not landing.

**The Excel answers "what does this look like if our assumptions hold?" This answers "what has to be true for this to work, and how much room is there?"**

---

## Simulation Classification

| Dimension | Choice | Why |
|---|---|---|
| **Randomness** | Stochastic | Payment behaviour, gold, acquisition and partner wins are all unknowable in advance, and the **range** is the deliverable |
| **Entity** | **Hybrid** | Customers differ in ticket, discipline, rail and tier, and every one of those is a threshold input that cannot be averaged. Vault fees and licence fees have no behaviour and stay aggregate |
| **Time** | Discrete, monthly | The product settles monthly; the gate counts **consecutive months**; the ATM allowance is a monthly threshold |
| **Approach** | Monte Carlo **+ solver** | Monte Carlo gives distributions of outcomes. The solver searches for the **inputs** that produce a stated outcome — which is what "what does it take to be profitable" asks |

---

# Part 1: What We're Solving

## Core Questions

Ordered by priority. **Q1–Q3 are the deliverable; Q4–Q6 are the risk envelope around it.**

| # | Question | Answer shape |
|---|---|---|
| **Q1** | **What does it take to be profitable?** Minimum book, mix and timing to cover the cost base — and the cheapest levers that pull it earlier | A **threshold plus a ranked lever list** |
| **Q2** | **How much can we give back through ICS, tier by tier?** | A **cost matrix by tier × benefit**, and an affordability envelope |
| **Q3** | **Where is the profit concentrated** — by ticket, region, rail and entry door? | **Profit contribution by decile** and by segment |
| **Q4** | **How much do we need to raise?** | 🆕 **A single derived number** — *"raise USD X and you are covered in 90% of paths"* — with the percentiles behind it. **Solved for, not assumed**, because no target exists (client, 2026-09-02) |
| **Q5** | **What does a gold drawdown do to the credit book?** | **Exceedance curves by LTV vintage** |
| **Q6** | **Which parameters actually decide Q1–Q5?** | **Tornado** |

⚠ **Q1 splits, and only one half is contaminated by unsourced inputs:**

| | Question | Depends on |
|---|---|---|
| **Q1a** | How many paying customers, at what ticket and rail mix, cover the cost base? | Unit economics and the cost base — **not market size** |
| **Q1b** | Is that number reachable? | The market funnel — **entirely judgement** (§4.3) |

**Q1a is the headline.** It is robust, it is what was asked, and it does not inherit the weakest assumptions in the model. **Q1b is reported as a range with its provenance stated**, cross-checked against the one observed market fact available: **O Gold has 75,000 active users in the UAE.**

## Output Metrics

### Primary

| Metric | Definition | Serves |
|---|---|---|
| `threshold_customers` | Paying customers at which monthly profit turns positive, at a given contingency | Q1a |
| `threshold_month` | First month the base path reaches `threshold_customers` | Q1a |
| `P(cum_profit > 0 | month)` | Share of paths cumulative-positive at M12/24/36/48/60/72/84 | Q1, Q4 |
| `peak_funding` | Running maximum of (cumulative P&L deficit + capital tied up) | Q4 |
| 🆕 `safe_raise_90` | **The headline.** `quantile(peak_funding, 0.90)` — the raise that survives 9 paths in 10. Reported with `safe_raise_50/80/95` beside it | Q4 |
| `P(peak_funding > X)` | Exceedance curve behind the headline | Q4 |
| `ics_cost_by_tier_benefit` | 4 × 5 matrix, per year | Q2 |
| `profit_share_by_ticket_decile` | Contribution to profit by ticket decile | Q3 |
| `P(margin_call | month)` | Share of the credit book called, by LTV vintage | Q5 |

### Diagnostic

| Metric | Why it is tracked |
|---|---|
| `tier_mix[t]` | Silver/Gold/Platinum/Sovereign shares over time. **Drives every ICS cost** and is the thing the Excel cannot compute |
| `ever_gate_share`, `mean_gate_month` | **Outputs, not targets** (§4.1). Replace two unsourced Excel cells |
| `churn_by_behaviour` | SIP lapse, card dormancy, credit repayment, redemption — reported **separately** |
| `treadmill` | Gross acquisitions per net customer added. Excel shows 7.52 at Y7 |
| `ltv_cac_by[region, channel, decile]` | Which customers are worth acquiring |
| `rail_mix[t]` | Prefunded vs Request-to-Pay share, and its effect on gate arrival |
| `spot_only_share` | Size and value of the second door |
| `revenue_ex_b2b` | **Every revenue figure is reported with and without Stream 6** (§4.3) |

---

# Part 2: How We Model It

## System Overview

```
                        ┌──────────────── MARKET (per region) ────────────────┐
                        │  population × filters × ceiling = reachable          │
                        │  ⚠ ENTIRELY JUDGEMENT — swept, and Q1a avoids it     │
                        └──────────────────────┬───────────────────────────────┘
                                               │ saturation brake
                                               │ (on cumulative-ever, not live)
        ┌──────────────────────────────────────┴───────────────────────────────┐
        │                          ACQUISITION                                  │
        │   salesforce (India only) + paid marketing + referrals                │
        │   × seasonality × saturation                                          │
        └──────────────────────────────────────┬───────────────────────────────┘
                                               │
                      ┌────────────────────────┴────────────────────────┐
                      │  TWO DOORS                                       │
                      │  SIP door  ──────────────►  ┐                    │
                      │  Spot door ──► converts ──► │  ONE POPULATION    │
                      └─────────────────────────────┴────────────────────┘
                                               │
        ┌──────────────────────────────────────▼───────────────────────────────┐
        │                       THE AGENT — one per customer                    │
        │                                                                        │
        │   attributes: region · ticket · archetype · rail · door                │
        │                                                                        │
        │   each month:   pay? ──► streak ──► GATE (6 in a row) ──► TIER         │
        │                   │                                        │           │
        │                   ▼                                        ▼           │
        │              grams accumulate ──► credit limit    5 benefits priced    │
        │                   │                    │            by tier            │
        │                   ▼                    ▼                                │
        │              FOUR INDEPENDENT STATES, four clocks:                     │
        │              SIP active/lapsed · card active/dormant ·                 │
        │              credit drawn/clear · gold held/redeemed                   │
        └──────────────────────────────────────┬───────────────────────────────┘
                                               │ aggregate
        ┌──────────────────────────────────────▼───────────────────────────────┐
        │   REVENUE  1a 1b 2 3 4 5   +   6 (B2B, non-agent, reported separately)│
        │   COST     COGS · opex · ICS giveback · acquisition · card · capital  │
        │   CASH     float · card prefunding · peak funding                     │
        └───────────────────────────────────────────────────────────────────────┘
                                               ▲
                    GOLD PRICE (GBM) ──────────┘  revalues grams, credit limits,
                                                   COGS and margin calls
```

## Entities

| Entity | Representation | Count | Why |
|---|---|---|---|
| **Customer** | **Agent** | ~200k cumulative | Ticket, discipline, rail and tier are all individual, and all feed thresholds |
| **Credit position** | **Agent attribute, vintage-stamped** | ~36k live | Liquidation risk is a property of **when the loan was struck and at what tier's LTV** |
| **B2B partner** | **Discrete arrival process** | 11 by Y7 | Eleven lumpy binary events cannot be a smooth curve |
| **Gold price** | Single stochastic path per run | 1 | Common shock across all agents |
| **Vault, licences, insurance, audit, tech** | Aggregate formulas | — | Fixed or step costs, no behaviour |
| **Partner end-users** | Aggregate AUM | ~10m notional | Only the total matters |

## State Variables

### Per agent

| Variable | Type | Notes |
|---|---|---|
| `region` | {UAE, OmanBahrain, India} | Fixed at acquisition |
| `ticket_base` | float | **Drawn from a regional distribution** (§4.3) |
| `ticket_this_month` | float | 🆕 **The amount is VARIABLE month to month with no maximum** (rulebook §6.1, client-confirmed). Only the USD 20 floor is tested. **`ticket_base` is a centre, not a constant** |
| `archetype` | {perfect, occasional, alternating, reducer, early_lapser} | **Conditioned on `rail`** |
| `rail` | {prefunded, request_to_pay} | **Can convert** — a modelled lever |
| `door` | {sip, spot} | Entry route. Spot-only agents may convert to SIP |
| `streak` | int 0–6 | Consecutive counted periods. **Resets to 0 on a miss** |
| `gated` | bool | True once `streak` reaches 6. **Permanent** |
| 🆕 `months_counted` | int | **Counted periods since the qualifying run began. Starts at 6 at the gate. NEVER falls, for any reason** |
| 🆕 `recent_12` | int 0–12 | **Counted periods in the trailing 12 calendar months.** Rolls, self-heals |
| 🆕 `grams_12mo_ago`, `grams_acquired_since` | float | Denominator of the `Sold` ratio |
| 🆕 `ics` | float 0–100 | **Computed, not looked up** — `min(Record, Standing) × Retention`, floored at 25 once gated |
| `tier` | {none, silver, gold, platinum, sovereign} | **Thresholded off `ics` at 25 / 50 / 75 / 100** |
| `grams` | float | Accumulated, net of redemption |
| `grams_self_custody` | float | Left the collateral base, still in the vault |
| `sip_active` | bool | |
| `card_active` | bool | **Independent clock** |
| `credit_drawn` | float | |
| `ltv_vintage` | (month, ltv_rate) | Stamped at draw, held to term |
| `alive` | bool | False only on full redemption and exit |

### Global

`month`, `gold_price`, `cum_ever_acquired[region]`, `partners`, `cash`, `cum_pnl`, `peak_funding`, `float_grams`

## Key Relationships

```
grams_bought        = (contribution × (1 − entry_fee)) / gold_price
credit_limit        = grams × gold_price × LTV(tier)          ← tier-dependent, NOT flat 0.50
card_spend          = f(ticket)   [income proxy]
interchange         = card_spend × 1.80% × (1 − PM_share)
entry_fee_earned    = contribution × entry_fee_rate(tier)     ← tier-dependent
fabrication_cost    = net_new_grams × gold_price × 1.50%      ← AURUMIX BEARS IT (settled)
margin_call         = gold_price × grams × LTV_struck < drawn × threshold
```

🔴 **Two incidence rules settled 2026-09-02 and hard-coded, not switched:**
1. **The customer pays 5% and nothing more.** The fabrication premium is **Aurumix's cost**, taken as COGS. The customer receives the full metal their money buys at spot.
2. **Collections are free** (Zand: local inward transfers free). **Redemptions cost USD 3.28** — Sumsub rescreen **1.85** (the workbook's actual charge, verified at USD 31,105.40 ÷ 16,813.73 events at Y7) + **AED 5 outward transfer (~1.43)** — against **zero permitted fee income** (VARA Annex 2 III.E.4). ⚠ `Model` row 250's note says USD 3.20; the model charges 1.85. Logged for Phase 4.

## Mechanics

### The gate

```
each month:  pay?  ──yes──►  streak += 1  ──► if streak == 6 and not gated:  gated = True
             │                                    (permanent, never revoked)
             └──no───►  streak = 0        ← the whole point. A miss at month 4
                                             means the earliest gate is month 9
```

⛔ **Revival is deleted.** A missed period is permanently uncounted. **Money paid after the 5-day grace is a SPOT PURCHASE**, not a late contribution (rulebook §4).

### 🔴 The ICS score — COMPUTED, not looked up

**Resolved 2026-09-02.** v2.6 collapsed the score to a `months-since-gate → tier` lookup **because Excel could not carry the formula**. It put Gold at gate+12 and Platinum at gate+36 — which for a perfect payer gating at M6 lands Gold at M18, **six months later than the rulebook's ladder at every rung.**

**An agent model has no such constraint, so it implements the real formula and the discrepancy dissolves.** From `_draft_ics-scoring.md` §1:

```
Months    = counted periods since the qualifying run began.  Starts at 6 at the gate.  NEVER falls.
Recent    = counted periods in the trailing 12 calendar months, 0–12.
Sold      = 1 − grams_now ÷ (grams_12mo_ago + grams_acquired_since)

Record    = m × 4.1667                     m ≤ 12
          = 50 + (m − 12) × 1.04167        12 < m ≤ 60
          = 100                            m > 60

Standing  = Recent × 8.3333

Retention = 1                              Sold ≤ 30%
          = 1 − (Sold − 30%) ÷ 70%         Sold > 30%

ICS       = min(Record, Standing) × Retention,   floored at 25 once gated
```

**Tiers threshold off the score at 25 / 50 / 75 / 100.** A perfect payer therefore reaches Silver at M6, Gold at M12, Platinum at M36, Sovereign at M60 — `Record(6)=25`, `Record(12)=50`, `Record(36)=75`, `Record(60)=100`. **This reproduces the rulebook's stated arrival schedule exactly**, which the lookup did not.

**Three properties the formula gives us for free, and the lookup could not:**

1. 🆕 **Redemption feeds back into tier.** `Retention` is a multiplier with veto power — sell more than 30% of your gold in a year and your score falls proportionately, to zero if you empty the account. **Redemption and tier are NOT independent**, and my earlier draft wrongly treated them as two unrelated flat rates.
2. **`min()` is the arithmetic of AND.** A long record cannot cover a dead year, and a good year cannot cover a short record. **The alternating misser caps at Gold for life** because its `Recent` never clears — an emergent property, not a rule to hard-code.
3. **Sovereign requires `Record = 100` AND `Standing = 100`** — 60+ counted months and 12 of the last 12. Over an 84-month horizon only agents acquired in the first ~24 months with near-perfect records can reach it, which is where v2.6's ~1.2% comes from.

⚠ **Amount is irrelevant to the score.** A counted period is one calendar month with one accepted contribution at or above the USD 20 floor. **USD 20 and USD 2,000 count identically** — the design's core fairness property, and it must not be broken by the variable-ticket logic below.

### The benefit ladder — 4 tiers × 5 benefits

| Benefit | None | Silver | Gold | Platinum | Sovereign | Source |
|---|---|---|---|---|---|---|
| **Entry fee paid** | 5.00% | 4.50% | 4.00% | 3.50% | **3.00%** | Corpus ceiling 1.5–2.0pp; 2.0pp taken, stepped linearly |
| **Family / Will discount** | 0% | 10% | 20% | 35% | **50%** | Corpus, firm |
| **Card FX margin charged** | 2.0% | 2.0% | 1.5% | 1.25% | **1.0%** | Corpus 2.0/1.5/1.0; middle rungs interpolated |
| **Credit LTV** | 50% | 50% | 65% | 72.5% | **80%** | Corpus 50/65/80; middle rungs interpolated |
| **Gold Rewards** (% of card spend) | 0% | 0.15% | 0.45% | 0.60% | **0.75%** | Corpus ladder, referenced in the workbook |

**Decision 6 — payout cap, enforced per agent:** Gold Rewards paid to a customer may not exceed the revenue **that customer** generated. ⚠ **Only an agent model can apply this**; the workbook applies a rate to aggregate card revenue.

### Revenue streams

| # | Stream | Driver | Activates |
|---|---|---|---|
| 1a | Entry fee — SIP | contribution × `entry_fee_rate(tier)` | M1 |
| 1b | Entry fee — spot | spot volume × `entry_fee_rate(tier)`. ⚠ **The discount DOES apply to spot** — benefit 1 applies to *"every purchase, spot included"* (benefits doc §0.1, citing rulebook §1.1). Spot **earns** no score; a scored customer still **spends** their tier on it. **The workbook applies the discount to stream 1a only, and so understates the giveback.** Logged for Phase 4 | M1 |
| 2 | Card interchange | card spend × 1.80% × (1 − PM share) | M13 |
| 3 | Family plan + Will | subscribers × (USD 50 + 1.5 × USD 6)/12 | M7 |
| 4 | Cardholder fees | FX margin + ATM over-allowance + issuance/replacement | M13 |
| 5 | Lending revenue share | drawn balance × servicing × 70% + draws × origination × 50% | M13 |
| **6** | **B2B platform fee** | partners × AUM/partner × 0.75% | M13 |
| **0** | **Redemption — MANDATORY COST** | events × USD 3.28 (1.85 modelled + 1.43 outward transfer). **No fee permitted, ever** | M1 |

🔴 **Stream 6 is reported separately from every revenue total.** It is 33–40% of revenue, rests on **eleven partnerships with no pipeline** (client, 2026-09-02), and is uncertain in a different way from the rest of the model.

## Time Dynamics

**84 monthly steps. M1 = January 2027.** Reported natively monthly **and** aggregated onto the workbook's 29-column grid (24 monthly + Y3–Y7) for comparison.

### Order within a step

1. Advance gold price (GBM)
2. Compute acquisition → assign attributes → add agents
3. **Each agent decides: pay / miss** → update streak, gate, tier
4. Spot purchase draws (Bernoulli per agent)
5. Grams accumulate; revalue at the new price
6. Card and credit behaviour; **stamp LTV vintages on new draws**
7. **Margin-call test** against struck vintages
8. Redemption and self-custody draws
9. Independent state transitions: card dormancy, credit repayment, SIP lapse
10. Aggregate → revenue → ICS giveback → costs → cash → funding

⚠ **The margin-call test (7) runs before redemption (8)** so that a call and a voluntary redemption in the same month are not double-counted.

## Uncertainty and Randomness

| Source | Distribution | Notes |
|---|---|---|
| **Gold price** | GBM, drift 8.1%/yr, vol `{{UNFILLED — source at build}}` | ⛔ **Do not guess the volatility.** Source it or state it as assumed |
| **Ticket** | Lognormal per region, fitted to **mean + floor share** | Shape swept low/med/high (§4.3) |
| **Archetype** | Categorical, **conditioned on rail** | Mix **swept**, not fixed |
| **Payment** | Bernoulli(p_archetype) monthly | |
| **Spot purchase** | Bernoulli(attach × frequency / 12) | |
| **Acquisition** | Poisson around the channel mean | |
| **B2B partners** | **Discrete arrivals**, with a real probability of zero in a year | Replaces the straight line |
| **Redemption** | Bernoulli on AUM rate; **holders at 1.6×** | Clusters under stress |
| **Card dormancy** | Hazard, `{{UNFILLED — source at build}}` | Genuinely sourceable from card-industry data |

### Correlations

| Pair | Treatment |
|---|---|
| ticket ↔ card spend | **Correlated** — spend is keyed to ticket as an income proxy |
| ticket ↔ persistency | **Independent by default, with a correlation sweep.** No source either way, and it materially changes Q3 |
| gold ↔ redemption | **Correlated in stress scenarios only** — a crash triggers redemptions |
| rail ↔ archetype | **Correlated by construction.** This is the lever |
| 🔴 **behaviour ↔ behaviour** | **A single `ρ_quality` parameter, swept 0 → 0.6.** See below |

### 🆕 The cross-behaviour correlation, and why it is its own parameter

The archetypes describe **one axis — SIP payment discipline.** Seven other behaviours (spot buying, card spend, card dormancy, credit take-up, redemption, family attach, referrals) are currently flat rates applied uniformly.

🔴 **If the good behaviours cluster in the same people, profit concentration is far more extreme than ticket dispersion alone implies** — the perfect payer who also spends more, refers more, redeems less and buys more spot is worth a multiple of what eight independent flat rates predict. **That is Q3's core question and it cannot be answered with independent draws.**

**No source exists for these correlations.** Treatment is the standard one: a **single latent "quality" factor** loading on all eight behaviours, with `ρ_quality` **swept from 0 (fully independent, today's model) to 0.6 (strongly clustered)**, reporting how far the profit-by-decile answer moves across that range. One interpretable dial rather than 28 pairwise correlations nobody can defend.

## Agent Decision Rules

| Decision | Rule |
|---|---|
| **Pay this month?** | `Bernoulli(p)` where `p` comes from the archetype, conditioned on rail. **Prefunded agents draw from a higher-discipline mix** |
| 🆕 **How much?** | `ticket_base × lognormal(σ_month)`, floored at USD 20, **no ceiling** (rulebook §6.1). A rejected sub-floor payment is **not** a counted period |
| 🆕 **The lump button** | 🔴 A tiered saver may declare a large one-off as *this month's contribution* and collect the tier discount on it — the rulebook names this and declines to police it: *"a rule a customer can defeat by relabelling a payment is not a control."* **Modelled as a low-probability large draw among gated agents, and solved for as a hurdle** (§3 sweeps), never guessed |
| **Buy spot?** | `Bernoulli(attach × freq / 12)`, at the regional spot ticket |
| 🆕 **Arrears become spot** | Money arriving after the 5-day grace is **spot volume, not a contribution** (rulebook §4). It earns the entry fee, buys gold at that day's fix, and **does not restore the streak.** v2.6 sizes it at ~0.11 events per live account per year |
| **Take a card?** | Facility take-up 18% of the eligible base. **No gate — open to the whole book** (client, 2026-08-26) |
| **Draw credit?** | 50% of permitted limit, 2.1 events/yr, turnover 0.42 |
| **Let the card go dormant?** | Independent hazard, own clock. **Does not follow SIP lapse** |
| **Redeem?** | Bernoulli on the AUM rate; holders at 1.6×; **rises sharply under a gold crash** |
| **Lapse the SIP?** | Archetype hazard + background hazard |
| **Convert spot → SIP?** | `{{UNFILLED — confirmed sourcing negative}}`. **Solved for as a break-even rate, never guessed** |

---

# Part 3: What We Test

## Base Case

Every parameter at its workbook Base value, **except** those the classification moved to swept inputs: archetype mix, persistency, ticket dispersion, market ceiling.

**Reported:** the six primary metrics, with and without Stream 6, and against the workbook's 29-column output.

## Stress Scenarios

| # | Scenario | Shock | What it tests |
|---|---|---|---|
| **1** | **Gold crash** | −30% over 3 months, at M36 and again at M60 | Collateral revaluation, margin calls by vintage. Charter item |
| **2** | 🔴 **Redemption run** | Redemption rate ×5 for 6 months | **Cash out, gold sold, and ZERO fee income permitted by law.** The one flow with no offset |
| **3** | **Zero B2B** | `partners = 0` throughout | Does the core business stand without a third of its revenue |
| **4** | **Adoption failure** | Conservative persistency + conservative archetype mix + **100% Request-to-Pay rail** | The pessimistic behaviour corner, with rail mix included |
| **5** | **Regulatory delay** | Revenue starts at M13; **the cost base starts at M1 regardless** | VARA publishes no approval timeline. Twelve months of fees, insurance, audit and tech with no income |
| **6** | **Ticket compression** | Floor share to 75%, dispersion narrowed | If the book is poorer than assumed |
| **7** | 🔴 **Combined tail** | **1 → 2 chained**: crash → margin calls → redemption run → forced sales into a falling market | The realistic tail. Correlated, not independent |

⚠ **Scenario 7 is the one to build carefully.** The failure mode is not any single shock; it is that a gold crash devalues collateral, fires margin calls, frightens customers into redeeming, and forces gold sales into a falling market — **while VARA forbids charging a fee on any of it.**

## Sensitivities

### High-leverage parameters — hypotheses to test, not conclusions

| Parameter | Expected leverage | Why |
|---|---|---|
| B2B partner count | **Very high** | A third of revenue, no pipeline |
| Persistency / archetype mix | **High** | Drives book size, tier mix and giveback together |
| Rail mix | **High** | Drives the gate, and it is controllable |
| Ticket dispersion | **High** | Decides where profit sits, and who to acquire |
| Contingency (headcount proxy) | **High** | The cost base is incomplete by construction |
| Entry fee | **High** | Now a lever |
| Market ceiling | Medium | Saturation binds late; Q1a avoids it |
| Gold volatility | Medium | Concentrated in Q5 |

### Recommended sweeps

| Sweep | Range | Serves |
|---|---|---|
| **Contingency** | 15% / 30% / 50% | Q1 — the threshold as a function of the cost we have not modelled |
| **ICS ladder — ceiling** | 1.0 / 1.5 / 2.0pp at top tier | Q2 |
| **ICS ladder — steepness** | convex / linear / concave | Q2 — convex is generous at the top and cheap |
| **ICS ladder — breadth** | each of the 5 benefits on/off | Q2 |
| **Entry fee** | 3% / 4% / 5% / 6% | Q1 — a prescriptive lever |
| **Rail mix** | 0% / 25% / 50% / 75% prefunded | Q1, Q3 |
| **Archetype mix** | wider than v2.6's three | Q6 |
| **Ticket dispersion** | low / medium / high | Q3 |
| **2-D: entry fee × persistency** | heatmap | Q1 — the profitable region |
| **2-D: ticket dispersion × CAC** | heatmap | Q3 — who is worth acquiring |
| 🆕 **`ρ_quality`** | 0 / 0.2 / 0.4 / 0.6 | Q3 — do the good behaviours cluster |
| 🆕 **Lump-button rate** | Solved as a **hurdle**: at what take-up does the entry-fee ladder cost more than it earns? | Q2 — sizes an unpoliced design hole |
| 🆕 **Monthly ticket variance** `σ_month` | low / med / high | Q1 — sub-floor rejections break streaks, so variance destroys tiers |

---

# Part 4: How We Validate

## 4.1 🔴 Verification is not validation

**v2.6's published figures are usable for the first and worthless for the second.** Its 53.5% ever-gate and M8.1 mean arrival are **outputs of a Markov solve over the five archetype weights** — and that mix is recorded as *"rank 1 load-bearing and a confirmed sourcing negative."* Calibrating to reproduce them would prove only that the simulation was fed the same assumption.

**Verification targets — code-correctness tests, never reported as findings:**

| Target | Figure |
|---|---|
| Mean gate arrival / ever-gate share, **given v2.6's mix** | M8.1 / 53.5% |
| P(ever gates), alternating misser | 24.0% |
| Persistency M13/M25/M37/M49/M61, given v2.6's parameters | 55 / 40 / 30 / 24 / 19% |
| Holding-not-contributing at M61 | ~81% |
| Sovereign share of tiered accounts | ~1.2% |
| **Excel equivalence** | With every stochastic input pinned to Base, reproduce **`Aurumix_Revenue_Model_calculated.xlsx`**'s 29-column output to within rounding. ⚠ **Test against the calculated workbook, never the formula-only one** |

⚠ **The Excel equivalence test proves the port is faithful. It is NOT a constraint on assumptions** — once it passes, every parameter is free to move, and moving them is the work.

## 4.2 Scope

### In scope
Customer lifecycle and heterogeneity · the gate and the five-tier ladder · all seven revenue streams · the full cost base including capital and float · gold as a stochastic process · the two doors · rail mix · multi-state churn · redemption as a mandatory cost.

### Deliberately out of scope

| Excluded | Why |
|---|---|
| **Supply-side / free float** | Client instruction 2026-09-02. Phase 3 scoped separately |
| **RtP origination fees** | Client instruction 2026-09-02. Carried at zero |
| **Headcount as a modelled line** | No org assumptions exist. Handled as the swept contingency |
| **Competitive response** | No basis pre-launch |
| **Intra-month price movement** | Margin calls tested monthly |
| **India regulatory route** | Assumed solved, per v3.0 |
| 🆕 **The regulatory pause** (returning-NRI freeze; frozen months skipped, window extended) | A real rulebook state, but *"materially an India input… nothing in the corpus sizes it."* No repatriation rate exists. **Excluded and logged**, not silently dropped |
| 🆕 **Ticket escalation over tenure** | The amount is variable upward as well as downward, but no source describes savers ramping. `σ_month` is symmetric by default; **an escalation drift is available as a sweep if Q3 proves sensitive** |

## 4.3 🔴 Critical assumptions — and the honest state of the evidence

**The cost side is well-evidenced. The demand side is almost entirely judgement.** This asymmetry shapes what the simulation may claim.

| Input | Status |
|---|---|
| VARA/DMCC fees, Sumsub, insurance, audit, Visa IRF, Zand schedule, gold price, AED peg | ✅ **Sourced primary** |
| Spot tickets (Botim AED 700; Augmont ₹3,300) | ✅ Observed, proxy for India |
| O Gold 75,000 active UAE users | ✅ **The only observed demand fact in the model** |
| Market funnel filters (0.57 / 0.40 etc.) | ⛔ **Made up** (client, 2026-09-02). Swept; **Q1a avoids them** |
| Archetype mix | ⛔ **Confirmed sourcing negative.** Swept |
| Persistency 55% | ⛔ Validation file deleted from the repo. Swept |
| Ticket floor share 40–60% | ⛔ Unsourced, but **defensible as shape** — savings books sit heavy at the floor |
| Spot attach, spot→SIP conversion | ⛔ Confirmed sourcing negatives. Solved for, not guessed |
| B2B partner trajectory | ⛔ **No pipeline exists.** Reported separately |
| **Client observed data** | ⛔ **None. No waitlist, no pilot, no pre-registrations** |

⚠ **The payment-capability filter also contradicts the SIP rulebook** — it screens for a mandate the product dropped on 2026-08-10. Logged for Phase 4, not fixed here (client instruction).

## 4.4 Invariants — asserted every step, every path

| # | Invariant |
|---|---|
| 1 | `paying + holders == cumulative_ever_acquired` |
| 2 | `grams_under_custody >= grams_collateral_eligible` |
| 3 | `trust_holdings >= tokens_outstanding` |
| 4 | `streak ∈ [0,6]`; `gated` never reverts to False |
| 5 | `months_counted` **never decreases, for any reason** (§1.1 — "what you contributed" is a historical fact) |
| 5a | `ics == min(Record, Standing) × Retention`, and `ics >= 25` for every gated agent |
| 5b | `Standing >= Record` at every month of a clean climb — **a clean saver is never bound by Standing** (scoring §7.4) |
| 5c | An agent whose `Recent` never exceeds 6 **never exceeds Gold** — emergent, must not be hard-coded |
| 5d | **Amount never affects score.** Two agents with identical payment months and different tickets have identical `ics` |
| 6 | Gold Rewards paid to an agent ≤ revenue that agent generated (decision 6) |
| 7 | **Stream 0 is never positive.** No fee on redemption, in any scenario |
| 8 | `cumulative_ever_acquired <= market_ceiling` per region |
| 9 | Streams 2, 4, 5, 6 are zero before M13; stream 3 before M7 |
| 10 | `float_grams >= 2 bars` |
| 11 | Entry fee charged never exceeds 5% — **the customer's ceiling** |

## 4.5 Sanity checks

- Zero acquisition → zero revenue, costs continue, funding need equals cumulative cost
- Perfect payers only → ever-gate ≈ 100%, mean arrival ≈ M6
- Alternating missers only → ever-gate ≈ 24%
- Zero churn → paying == cumulative-ever, holders == 0
- Flat gold → grams and USD AUM move only with flows
- Zero discounts → ICS cost == 0 and profit rises by exactly the prior giveback

---

# Part 5: How We Build It

## Initial State (t = 0)

| Variable | Value |
|---|---|
| Customers | 0 |
| Gold price | USD 141.50/g |
| AED/USD | 3.6725 |
| Partners | 0 |
| Paid-up capital | AED 2.1m (1.5m issuance + 0.6m activities) |
| Regions open | UAE M1, India M1, **Oman & Bahrain M13** |

## Build Sequence

**Stage 1 — Population engine.** Agents, tickets, archetypes, rails, doors, the pay/miss loop, the gate, the tier ladder. **Gate: the §4.1 verification tests must pass.** Delivers Q2's tier mix and Q3's concentration.

**Stage 2 — Full book.** Port revenue, cost, capital and float from the workbook formula-for-formula. Add the gold process, discrete partner arrivals, multi-state churn. **Gate: the Excel equivalence test.** Then Monte Carlo. Delivers Q4, Q5.

**Stage 3 — Solver.** Search over inputs for the threshold, the ICS affordability envelope, and the break-even spot conversion rate. Sweeps and tornado. Delivers Q1, Q6, and the **prescriptive lever ranking**.

**Stage 2b — The float as inventory (added 2026-09-02, client decision: UNHEDGED).** The workbook's `1 bar + 10 days` rule is replaced by a daily inventory model: payday-clustered SIP demand, spot as random lumps, a calendar-aware order-up-to policy with dealer lead time and 100 g lots, safety stock from a service level, redemption netting, sell-back of excess, daily mark-to-market on the gold path, and a carry cost. Aurumix owns the price variance. Outputs: float size at service level, stock-out rate, carry, MTM P&L distribution, and the effect on the raise. `src/floatmodel.py`, `scripts/run_float.py`.

⚠ **Each stage ships something standalone.** Stage 1 answers the tier and concentration questions even if Stage 3 is never reached.

## Data Requirements

| Need | Source | Status |
|---|---|---|
| Gold volatility | General knowledge of long-run realised gold vol (~15%/yr); **not a fetched citation** | ⚠ Assumed, swept 10–22% |
| Card dormancy hazard | 🔴 **Researched 2026-09-02: CONFIRMED SOURCING NEGATIVE.** No published dormancy or attrition *rate* for consumer cards — UAE, GCC, global or fintech — only inactivity *definitions* (90 days to 12 months). My earlier note "genuinely sourceable" was wrong | Swept assumption, 0 / 1 / 2 %/month |
| Interchange split, gross vs effective | ✅ **Researched 2026-09-02.** Visa UAE IRF (eff. 19 Dec 2024, primary source): prepaid consumer 1.00% cap AED 50 — **the workbook's prepaid cap is exact**; credit Classic 1.15 / Gold **1.15** / Platinum **1.80** / Signature 2.05 / Infinite 2.10%. ⚠ **The workbook's "Gold 1.8%" is a Platinum rate under a Gold label.** Published BaaS splits (Sacra 2021 model): brand keeps ~0.28% of spend after network, sponsor and PM — vs the workbook's 0.72%. Sensitivity through the engine: at 0.28% take, Y7 profit −$33k. **Stream 2 is too small for the split to matter; stream 4's 17× dominance is structural** (FX and fees are not subject to the split) | Settled. Tier-label mismatch logged for Phase 4 |
| Everything else | Workbook + corpus | ✅ Available |

## 🔴 Escalation protocol — agreed 2026-09-02

The mandate is **prescriptive**, so where the design does not reach profitability the deliverable recommends changes and ranks the levers. **But if no plausible configuration reaches profitability at all**, the recommendation stops being a parameter change and becomes a structural one.

> **In that case: STOP and bring it to Abdur before it goes into any document.** Framing is agreed first, and the client hears it in the way and order Abdur chooses. **Do not let a structural finding surface for the first time inside a finished deliverable.**

This mirrors the handoff's standing position — *"the deliverable will look different from the proposal, and the client should hear that from us before he notices it."*

⚠ **This is a rule about sequencing, not about softening.** The finding is written plainly whenever it is written. What is agreed first is how and when it lands.

## Technical

Plain Python, numpy/pandas, vectorised across agents. No ABM framework. **Fixed recorded seeds** so every reported figure is reproducible. Internal use only — no packaging bar. Outputs as CSV + JSON + charts, all regenerable.

---

# Appendix A: Archetypes (v2.6, for verification)

| Archetype | Weight | Monthly pay p | Own hazard | P(ever gates) | Mean gate | Terminal tier |
|---|---|---|---|---|---|---|
| Perfect payer | 10% | 0.995 | 0.000 | 90.6% | M6.1 | **Sovereign-capable — the only one** |
| Occasional misser | 35% | 0.93 | 0.007 | 83.6% | M7.6 | Platinum ceiling |
| **Alternating misser** | 12% | 0.55 | 0.018 | **24.0%** | **M24.9** | **Gold, capped for life** |
| Reducer | 13% | 0.97 | 0.002 | 88.6% | M6.6 | By record |
| Early lapser | 30% | 0.60 falling | 0.200 | 2.6% | M8.6 | Silver floor or never |

**Aggressive mix** 29/26/16/8/21, background hazard 1.1%/mo · **Conservative mix** 14/24/16/10/36, background hazard 2.4%/mo. ⚠ **Sweep wider than these three.**

# Appendix B: Question → Metric → Scenario Map

| Question | Primary metric | Scenarios | Stage |
|---|---|---|---|
| Q1 Profitability threshold | `threshold_customers`, `threshold_month` | Base, 3, 4, 5, 6 | 3 |
| Q2 ICS affordability | `ics_cost_by_tier_benefit` | Base + ladder sweeps | 1 → 3 |
| Q3 Profit concentration | `profit_share_by_ticket_decile` | Base, 6 | 1 → 2 |
| Q4 Funding need | `peak_funding`, `P(> X)` | All | 2 |
| Q5 Credit risk | `P(margin_call)` by vintage | 1, 7 | 2 |
| Q6 What matters | Tornado | All sweeps | 3 |

---

**Next step:** review. On agreement, Stage 1 begins. ⛔ **No code before then.**
