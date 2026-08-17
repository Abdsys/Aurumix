# Aurumix — Revenue Model Architecture Brief

**Date:** 2026-08-17
**Version:** 1.0
**Phase:** 4, Revenue and Economic Modeling (repo folder 4; charter Phase 3)
**Status:** Architecture for review. No spreadsheet built yet. Build follows sign-off on Section 3.

> **What this document is.** A complete, implementable plan for the Aurumix revenue and cost model. After reading it, a modeller should be able to build the workbook without asking a question. Every value, formula and structure is specified, and every assumption carries its source and confidence.
>
> **What this document does that a standard revenue brief does not.** Three things, all at Abdur's instruction (2026-08-17). It runs the **full P&L to net profit**, including an operating cost base we construct ourselves because the client has supplied one cost figure in seventeen sections. It **inverts the direction of the model**, solving for the investor count that covers annual expenses rather than projecting revenue from growth targets, which is the client's own item 5 of 2026-07-28. And it **solves for eight parameters** that Phase 2 deliberately parked with the note "locks against the revenue model, Phase 4."

---

## 0. Read this first: the five findings that determine the architecture

Everything below follows from these. If you disagree with one, the model changes shape, not just its numbers.

### 0.1 The entry fee is a price, not a revenue line

On a USD 75 contribution at a 5% fee, Aurumix discloses USD 3.75 and retains **USD 1.61**. The fabrication premium is buried inside the fee. Booking 5% as revenue overstates the top line by 2.3 times.

| Line | USD | % of contribution |
|---|---|---|
| Contribution received | 75.00 | 100.00% |
| Paid to the dealer (0.5037 g at fix, plus 3% fabrication premium) | (73.39) | (97.85%) |
| **Gross margin retained** | **1.61** | **2.15%** |
| Price-gap risk carried by the float | (0.59) | (0.79%) |
| Float cost of capital | (0.37) | (0.49%) |
| Payment rail (AANI push, assumed) | (0.25) | (0.33%) |
| **Net contribution margin** | **0.41** | **0.54%** |

Source: `_draft_purchase-structure.md` §2.2, re-run at verified gold price and volatility. **The model's revenue line for stream 1 is USD 1.61, never USD 3.75.** The difference is cost of goods sold.

### 0.2 The payment rail is a fixed fee per collection, and this is the equation the model turns on

UAE direct debit is priced per debit, not as a percentage. So margin per contribution is:

```
Net = C × (f − c) − R

  C = contribution size
  f = entry fee rate
  c = variable cost rate (fabrication premium + price-gap risk + float cost of capital)
  R = fixed cost of one collection event
```

Source: `_parked_collection-economics-and-minimum-ticket.md` §2.

This is **non-linear in ticket size**, which has one hard consequence for the build: **the model must compute margin per segment at that segment's own ticket, never on a blended average ticket.** A blended USD 40 average across a USD 20 and a USD 75 population produces a materially different and wrong answer, because the fixed rail is spread over different bases.

The rail is also the single largest binary in the model:

| Rail | Cost on USD 75 | Net margin | Status |
|---|---|---|---|
| AANI Request to Pay | assumed USD 0.25 (0.33%) | **+0.54%** | **Unpublished. This is an assumption, not a finding** |
| UAEDDS at AED 5/debit | USD 1.36 (1.81%) | **−0.94%** | Emirates NBD published tariff, Medium confidence |

**At the client's own target ticket, on published tariffs, the SIP loses money on every collection.** The AANI cost is the most valuable unknown number in the engagement.

### 0.3 The entry fee cannot cover the operating cost base at any modelled scale

This is the answer to the client's item 5, and it is not the answer they expect.

| Scale point | Annual opex | Net margin per contribution | Investors needed to break even on entry fee alone |
|---|---|---|---|
| Year 1 (500 investors) | USD 845,800 | USD 0.41 | **171,911** |
| Year 3 (12,000 investors) | USD 2,506,000 | USD 0.75 | **278,444** |
| Year 10 (80,000 investors) | USD 8,495,500 | USD 0.90 | **786,620** |

Opex from Section 7.4. The break-even requirement **grows faster than the business**, because opex scales with investor count while margin per contribution improves only slowly with bar denomination. There is no investor count on the client's roadmap at which the entry fee pays for the company.

### 0.4 Therefore: this is a card business with a gold savings acquisition funnel

Modelled Year 10 revenue stack:

| Stream | USD/yr | Share |
|---|---|---|
| Card interchange, net of programme manager share | 5,900,000 | **53.8%** |
| Cardholder fees (FX margin, ATM) | 1,900,000 | 17.3% |
| B2B platform fee (USD 200m partner book at 60 bps) | 1,200,000 | 10.9% |
| **Entry fee margin** | **864,000** | **7.9%** |
| Credit revenue share | 600,000 | 5.5% |
| Family plan and Digital Will | 500,000 | 4.6% |
| **Total** | **10,964,000** | |
| Opex | (8,495,500) | |
| **Net** | **2,468,500** | |

**The card is 71% of the business.** The gold SIP is the acquisition and retention mechanism that produces cardholders with a collateral balance; it is not, on its own economics, the product that pays.

Two consequences follow immediately, and both are decisions rather than observations:

1. **The programme manager interchange share is the most valuable commercial number in the engagement**, ahead of the dealer spread and the vault quote. It sizes 54% of revenue directly and caps the Gold Rewards ladder. Phase 2 already derived the floor: **36%** at Sovereign, below which Gold Rewards stops self-funding (`_draft_credit-and-card-infrastructure.md` §8.2).
2. **The credit-versus-prepaid decision is not a product choice, it is the business model.** Prepaid caps interchange at 1.00% by CBUAE notice; credit runs 1.80% to 2.30% uncapped. At Year 10 volumes that difference is roughly **USD 3.2m a year**. It must be settled before the September build.

### 0.5 The persistency curve is worse than the corpus assumes, and it governs everything

Decision 22 calls persistency "the number that governs the calibration" and uses Indian life insurance at 79% (month 13) and 38% (month 61). Fresh research says that is the wrong comparator and the wrong basis.

| Source | M13 | M25 | M37 | M49 | M61 | Confidence |
|---|---|---|---|---|---|---|
| Corpus assumption (decision 22) | 79% | — | — | — | 38% | — |
| LIC, **by premium** (what decision 22 used) | 74.8% | 71.0% | 66.1% | 61.5% | 63.1% | Medium-High |
| LIC, **by policy count** (the right basis for a low-ticket product) | 64.1% | 59.3% | 52.7% | 48.8% | 50.3% | **High** (IRDAI Handbook 2024-25, Table 28) |
| AMFI: share of live SIP accounts running past 5 years | — | — | — | — | **10.1%** | Medium |
| **Recommended for the model** | **55%** | **40%** | **30%** | **24%** | **19%** | Derived |

Three adjustments produce the recommendation. Life insurance persistency is propped up by surrender penalties, 80C tax clawbacks and a renewal-commissioned agent chasing payment, **none of which Aurumix has** (decision 19 deleted the lock-in). Against that, **reducing your contribution is free and unscored** (`_draft_sip-rulebook.md` §6.2), which converts affordability lapses into reductions and mainly protects months 1 to 24. And the mode matters: IRDAI's own definition requires **13 consecutive monthly payments** to count as 13-month persistent, against 2 annual payments, so a blended published figure structurally overstates what a monthly product achieves. **No monthly-versus-annual split is published anywhere in Indian data. Confirmed negative.**

**Model consequence: run the base at 55% M13 and the model at the 45% and 65% bounds as a first-class scenario, not a sensitivity footnote.** Lifetime value roughly halves against the corpus assumption, which reprices the referral reward, the agent commission and the acquisition budget ceiling all at once.

---

## 1. Model Overview

| Field | Value |
|---|---|
| **Project** | Aurumix (AURX), a VARA-regulated gold-backed monthly savings product in Dubai. 1 AURX = 1 gram of allocated physical gold. SIP from USD 20/month plus spot purchase, an Investor Conviction Score governing five benefits, a gold-collateralised credit facility and card, and a B2B white-label channel |
| **Revenue Model Type** | Hybrid, and deliberately unbalanced: one inflow-linked stream (entry fee), three activity-linked streams (interchange, cardholder fees, lending), one headcount-linked stream (family and will), one AUM-linked stream (B2B platform fee) |
| **Modeling Approach** | **Bottom-up cohort engine.** Acquisition by channel and segment, monthly survival, deterministic ICS state machine, per-segment unit economics, stock-and-flow AUM |
| **Time Horizon** | 10 years, from an assumed Year 1 start of **January 2027** |
| **Granularity** | **Hybrid: monthly M1 to M60, annual Y6 to Y10** |
| **Total Periods** | **65** (60 monthly + 5 annual) |
| **Currency** | USD primary, AED at the peg 3.6725 |
| **Headline output** | The expense-derived break-even floor, by year, with the client's growth targets as a named scenario measured against it |

**Why the hybrid granularity.** Every event that resolves month by month happens inside the first sixty months: the Confirmed SIP gate at month 6, Gold at 12, Platinum at 36, **Sovereign at 60**, the referral payout lag that makes the channel dark until month 13, and the founding cohort's full climb through the benefit ladder. Monthly resolution is not a nicety in that window, it is the only way the tier distribution can be computed rather than assumed. After month 60 the cohort structure is stable, tiers have saturated, and annual roll-forward loses nothing while keeping the workbook auditable. Monthly precision to month 120 would signal a confidence in year-nine detail that a pre-launch company cannot have.

**Monthly-to-annual conversion notes.**
- Annual survival `S` converts to a monthly hazard: `h = 1 − S^(1/12)`.
- Annual withdrawal allowance (30%) is a **trailing-twelve-month** measure and must stay monthly-recomputed even in the annual block; carry the three ledger reads forward as annual snapshots.
- Card spend, interchange and cardholder fees are monthly flows; annual periods sum twelve months at the year's average active-cardholder count.
- The B2B platform fee is invoiced monthly on a stock balance; in annual periods use the average of opening and closing partner AUM.

---

## 2. Model Sketch

### 2.1 Revenue architecture

```
+---------------------------------------------------------------------------+
|                          ACQUISITION LAYER                                 |
+---------------------------------------------------------------------------+
|  Channel mix:  Agent network | Member referral | Direct | B2B partner      |
|       |             |              |              |                        |
|       |             | (dark until  |              | (no ICS, no benefits,  |
|       |             |  month 13)   |              |  partner keeps 70-80%  |
|       |             |              |              |  of entry spread)      |
|       v             v              v              v                        |
|  New accounts per month, BY SEGMENT                                        |
|    S1 UAE NRI professional   (ticket USD 75)                               |
|    S2 UAE NRI white-collar   (ticket USD 40)                               |
|    S3 UAE NRI blue-collar    (ticket USD 20)                               |
|    S4 Oman + Bahrain         (ticket USD 40)  [from M13]                   |
|    S5 India resident         (ticket USD 30)  [SWITCH, see 6.7]            |
|    S6 Other international    (ticket USD 75)  [from M25]                   |
+---------------------------------------------------------------------------+
                                    |
                                    v
+---------------------------------------------------------------------------+
|                    COHORT SURVIVAL ENGINE                                  |
|  Each monthly cohort decays on the hazard curve (0.5).                     |
|  Three states, not two:                                                    |
|     CONTRIBUTING  ->  REDUCED (still pays, smaller)  ->  LAPSED            |
|  Reduction is free and unscored, so it is a real absorbing-delay state     |
+---------------------------------------------------------------------------+
        |                                              |
        v                                              v
+---------------------------+          +-------------------------------------+
|   FLOW: contributions     |          |   STOCK: grams under custody        |
+---------------------------+          +-------------------------------------+
| Contributing x ticket     |          | + grams bought                      |
|         |                 |          | + Gold Rewards grams credited        |
|         v                 |          | - redemptions                       |
|  Net = C x (f-c) - R      |          | - self-custody withdrawal (leakage) |
|  PER SEGMENT, never       |          |         |                           |
|  on a blended ticket      |          |         x gold price (FLAT)         |
|         |                 |          |         v                           |
|         +--> [STREAM 1]   |          |   AUM (USD)                         |
|              Entry fee    |          |    +--> [STREAM 6] B2B fee (bps)    |
|              margin       |          |    +--> custody COST (0.15-0.40%)   |
+---------------------------+          |    +--> credit collateral base      |
        |                              +-------------------------------------+
        v                                              |
+---------------------------------------------------------------------------+
|            ICS STATE MACHINE  (deterministic, an OUTPUT not an input)      |
|   ICS = min(Record, Standing) x Retention,  floor 25 once gate passed      |
|   Gate: 6 consecutive.  Silver M6 | Gold M12 | Platinum M36 | Sovereign M60|
|                                    |                                       |
|   Produces: tier distribution by month  ------+                            |
+---------------------------------------------------------------------------+
                                                |
        +---------------------------------------+---------------------------+
        v                                       v                           v
+------------------+          +--------------------------+   +---------------------------+
| BENEFIT COSTS    |          |  CARD LAYER (Gold+)      |   |  CREDIT LAYER (Gold+)     |
| (contra-revenue) |          +--------------------------+   +---------------------------+
| Entry discount   |          | eligible x activation    |   | eligible x take-up        |
|   0/.4/.8/1.2/1.5|          |   x monthly spend        |   |   x LTV(tier) x drawn%    |
| Gold Rewards     |          |   x interchange(tier)    |   |         |                 |
|   0/0/.15/.45/.75|          |   x PM SHARE  <-- 54% of |   |         v                 |
| Will discount    |          |         |     the model  |   |   [STREAM 5] revenue      |
|   0/10/20/35/50% |          |         v                |   |   share, no credit risk   |
| (LTV + card tier |          |  [STREAM 2] interchange  |   +---------------------------+
|  cost nothing;   |          |  [STREAM 4] FX + ATM     |
|  they are        |          |     net of tier waivers  |   +---------------------------+
|  revenue-        |          +--------------------------+   |  [STREAM 3] family/will   |
|  positive)       |                                          |  accounts x attach x price|
+------------------+                                          +---------------------------+
                                    |
                                    v
+---------------------------------------------------------------------------+
|   ACQUISITION COST      |   OPERATING COST      |   P&L AND BREAK-EVEN     |
|   agent commission      |   headcount (step)    |   Revenue                |
|   referral (6mo lag)    |   VARA + compliance   |   - COGS (in stream 1)   |
|   capped by the         |   vault + attestation |   - benefit costs        |
|   acquisition budget    |   tech + corporate    |   - acquisition          |
|   ceiling (% of         |   marketing           |   - opex                 |
|   entry-fee revenue)    |                       |   = NET PROFIT           |
+---------------------------------------------------------------------------+
                                    |
                                    v
                    SOLVER: minimum investors to cover annual expenses
                    SOLVER: the eight parked parameters (Section 9)
```

### 2.2 Revenue streams at a glance

| # | Stream | Type | Base it scales with | Activates | Y1 est. | Y10 est. | Confidence in the rate |
|---|---|---|---|---|---|---|---|
| 1 | **Entry fee margin** | Inflow | Gross contributions, per segment | M1 | ~USD 2,500 | ~USD 864,000 | Fee is client-stated; cost build-up is ours |
| 2 | **Card interchange** | Activity | Card spend x rate(tier) x PM share | Sponsor bank live, assume **M18** | 0 | ~USD 5,900,000 | Rate **verified** (Visa UAE IRF); **PM share unknown** |
| 3 | **Family plan and Digital Will** | Headcount | Accounts x attach x price | M1 | ~USD 800 | ~USD 500,000 | Price is ours; cost floor verified |
| 4 | **Cardholder fees (FX, ATM)** | Activity | Foreign spend, ATM volume, net of tier waivers | With the card, **M18** | 0 | ~USD 1,900,000 | Market rate ~2%, converged across four comparables |
| 5 | **Lending revenue share** | Activity + stock | Drawn balance and draw events | Lending partner signed, assume **M24** | 0 | ~USD 600,000 | **Every rate unpriced.** Partner term sheet |
| 6 | **B2B platform fee** | **AUM** | Partner-customer AUM x bps | **M24**, build requirement from **M1** | 0 | ~USD 1,200,000 | **Placeholder 0.5-0.75%** |

**There is no seventh stream, and there can never be an exit fee.** VARA Annex 2 Rule III.E.4: an ARVA issuer granting redemption "shall process and complete redemption requests without charging any fees." Verified verbatim at primary source. This is the constraint that shapes the entire design.

**Deliberately excluded, recorded so they are not re-proposed** (`Aurumix_Process_Maps_Revenue_Streams.md`): physical delivery and making charges (client instruction), insurance attach on the loan and SIP (client instruction), gold leasing for yield (refused despite being the largest margin line in the adjacent Indian market), FX margin on contributions (parked; GCC pegs make it thin until the Year 3+ non-pegged perimeter), a secondary-market premium (**decision 7: the premium is zero**, evidenced across nine protocols including two trading at a discount).

---

## 3. The engine, layer by layer

This is the section to argue with. Everything downstream is arithmetic.

### Layer 1 — Acquisition

New accounts per month = `agent-driven + referral-driven + direct + partner-driven`, each allocated across the six segments by a channel-to-segment mix matrix.

- **Agent-driven** = `active agents x productivity (accounts/agent/month) x ramp factor`. The agent network is the client's stated primary distribution channel (`100 G Business_Model.md` §11.1).
- **Referral-driven** = `qualified referrers x referral rate x conversion`. **Structurally zero until month 13**, because a referrer must pass their own six-month gate and the referee must then pass theirs (`_draft_referral-system.md` §5.4). The model must not put referral volume in Year 1.
- **Direct** = marketing spend / CAC, plus organic.
- **Partner-driven** = partner accounts, which **earn no ICS and consume no benefits** (`_draft_ics-scoring.md` §1.9). They are a separate, structurally higher-margin population and must be tracked separately throughout.

### Layer 2 — Cohort survival, with three states not two

Standard subscription models have contributing and churned. Aurumix has a third state that is economically real, because **reducing your contribution is free and scores nothing** (`_draft_sip-rulebook.md` §6.2). The product deliberately converts would-be lapses into reductions.

```
CONTRIBUTING --(reduction rate)--> REDUCED --(hazard)--> LAPSED
      |                                                     ^
      +------------------(hazard)---------------------------+

REDUCED members contribute at the USD 20 floor, still count for ICS,
still hold gold, still spend on the card. They are not churn.
```

If the product converts even a third of would-be lapses into reductions, the **revenue** curve sits materially above the **account survival** curve. This is one of the few genuine structural advantages Aurumix has over the insurance comparator, and the model should show it explicitly rather than bury it in a blended churn rate.

### Layer 3 — Contribution flow

`Gross inflow(segment, month) = contributing(segment) x ticket(segment) + reduced(segment) x 20`

**Never blend the ticket.** See 0.2.

### Layer 4 — Unit margin

Per segment, per month: `Net = C × (f − c) − R`, with `f` reduced by that segment's tier-weighted entry-fee discount.

### Layer 5 — The ICS state machine

This is the layer that makes the model unusual and it is worth stating plainly: **tier distribution is an output, never an assumption.**

```
Months  = counted periods since the qualifying run began. Starts at 6 on gate day.
          Never falls, for any reason.
Recent  = counted periods in the trailing 12 (0 to 12). Rises and falls.
Sold    = 1 − (grams now) / (grams 12 months ago + grams acquired since)

Record   = 4.1667 x Months            for Months <= 12
         = 50 + 1.04167 x (Months−12) for 12 < Months <= 60
         = 100                        for Months > 60
Standing = 8.3333 x Recent
Retention= 1                          for Sold <= 30%
         = 1 − (Sold − 30%) / 70%     for Sold > 30%

ICS = max(25, min(Record, Standing) x Retention)   once the gate is passed
```

Source: `_draft_ics-scoring.md` §1. Tiers: Silver 25, Gold 50, Platinum 75, Sovereign 100. Below the gate there is **no score at all**, which is why the bottom rung is named "No tier".

**Why this matters for the model.** For a saver who never misses, `min(Record, Standing) = Record` at every month of the climb (proved at `_draft_ics-scoring.md` §7.4). So tier follows deterministically from months-contributed and withdrawal behaviour. A cohort engine **computes** the tier distribution; it does not need an assumed split. The only exogenous behavioural inputs are the monthly contribution-success probability and the withdrawal distribution.

Three properties the build must honour:
- **Sovereign is a monthly-recomputed state, not an absorbing one.** It requires Record 100 **and** Recent 12 **and** Sold ≤ 30% simultaneously. One miss drops Standing to 91.7 and the customer out of Sovereign for twelve months. Expect the Sovereign **stock** to sit well below the Sovereign **ever-qualified** count.
- **The alternating misser (pay, miss, pay, miss) is capped at Gold for life**, because Recent holds at 6 forever. That is a real, permanently occupied cell in the distribution.
- **The benefit ladder is time-phased by construction.** Nobody is above Silver in Year 1, so the maximum entry-fee discount outstanding at launch is **0.4pp**. The first Sovereign appears in **month 61**. Launch-year cost of the entire five-benefit ladder is one 0.4pp discount, which is close to nothing.

### Layer 6 — AUM stock, and the leakage driver that hits five streams

```
Grams(t) = Grams(t−1) + bought(t) + rewards_credited(t) − redeemed(t) − self_custody(t)
AUM(t)   = Grams(t) x gold_price   [gold price FLAT, see 8.1]
```

**One leakage driver propagates to five revenue lines.** Decision 50 made AURX an open ERC-20, so a customer can withdraw to self-custody freely, and decision 51 rules that **withdrawal to self-custody counts as a disposal**. A self-custodied gram is outside the family product, outside the credit collateral base, generates no interchange, is outside custody-cost absorption, and is outside the B2B AUM base.

The design puts a bound on it: the **30% annual withdrawal allowance is costless** under the Retention rule, so up to 30%/year leaves with no economic friction at all. **Model leakage once at the AUM level and propagate it. Base 12%/yr, ceiling 30%/yr.**

### Layers 7 to 11

Activity revenue (Section 6), benefit costs (Section 7.2), acquisition cost (7.3), opex (7.4), P&L and solvers (Sections 9 and 12).

---

## 4. Timeline and milestones

| Milestone | Period | Revenue and cost impact |
|---|---|---|
| Client app build complete | Sep 2026 (pre-model) | Multi-tenant capability at register and mint must be in this build or stream 6 is lost |
| **Model Year 1 starts** | **M1 = Jan 2027 (assumption)** | No launch date exists in any client document. This is ours and must be flagged |
| Platform live, UAE only | M1 | Streams 1 and 3 active. Entry-fee discount and will discount live. Nothing else |
| First Confirmed SIP cohort (Silver) | M6 | Benefit ladder begins at 0.4pp |
| **First Gold tier** | **M12** | Credit, card and Gold Rewards become **eligible**, but not yet available |
| Oman and Bahrain open | M13 | Segment 4 activates. Requires local authorisation |
| **Referral channel produces its first payout** | **M13** | Six months for the referrer plus six for the referee. Year 1 pays nothing |
| **Card programme live** (sponsor bank) | **M18, assumed** | **Streams 2 and 4 activate. This is 71% of Year 10 revenue** |
| Lending partner live | M24, assumed | Stream 5 activates |
| **B2B partner live** | **M24, assumed** | Stream 6 activates |
| Other international | M25 | Segment 6 |
| First Platinum | M36 | LTV 65%, Gold Rewards 0.45%, FX 1.5% |
| **First Sovereign** | **M61** | The ladder reaches full cost only in Year 6 |

**Model implication.** Conditional activation on every stream: `=IF(period >= activation_month, calculation, 0)`. The two dates that matter most are the **card programme (M18)** and the **B2B partner (M24)**, because between them they carry 65% of terminal revenue and both are commercial gates outside our control.

---

## 5. Segments

The corpus segments by nationality and KYC document. **Every rule that binds is about country of residence.** Decision 31 is explicit: "the table is segmented by the wrong variable. Re-cut it by country of residence."

| ID | Segment | Ticket | Addressable base | Basis |
|---|---|---|---|---|
| S1 | UAE, Indian professional / entrepreneur | **USD 75** | ~71,000 | 15% of income-qualified, per occupational split |
| S2 | UAE, Indian white-collar non-professional | **USD 40** | ~119,000 | 25% of income-qualified |
| S3 | UAE, Indian blue-collar (qualified half) | **USD 20** | ~285,000 | 60% of income-qualified |
| S4 | Oman + Bahrain | **USD 40** | ~1,014,000 gross | MEA 2025 |
| S5 | **India resident** | **USD 30** | ~12.5m serviceable | See 6.7 |
| S6 | Other international | **USD 75** | not sized | Each needs local licensing |

**The addressable base correction, and it goes in our favour.** Our own decision 31 says the launch perimeter is "~3.5 to 4M". The MEA 2025 primary table gives **4.58M** (UAE 3.57M + Oman 0.69M + Bahrain 0.33M), against 4.30M in the three banking-blocked countries. **We were understating our own perimeter by 15 to 25%.** Correct decision 31.

**But the honest denominator is much smaller.** Filtering the 4.58M for working-age earners, banked status, and an income band that can sustain USD 20/month on top of remittance obligations gives roughly **1.9m income-qualified**, and applying a gold-savings propensity gives **~474,000** (range 0.35m to 0.9m). The propensity filter has **no published source** and is the weakest link in the entire sizing.

**What this does to the client's target.** Year 10 of 60,000 to 100,000 is 1.3% to 2.2% of the headline diaspora, which is how it will be pitched. Against the realistic addressable base it is **12.6% to 21.1%**. Capturing one in five income-qualified, gold-inclined, banked Indians in the UAE, against a bank incumbent, is a demanding number. **Model 60,000 as the defensible case and treat 100,000 as requiring a distribution partnership or perimeter expansion.**

**The incumbent nobody had found.** **Liv Gold, from Emirates NBD**: AED 15 minimum (~USD 4), digital XAU, no maintenance or transfer fees, fractional to 0.001 XAU, **convertible to physical gold with home delivery**, under a CBUAE banking licence, distributed to the installed base of the UAE's largest retail bank. RAKBANK's gold account supports standing instructions, which is functionally a gold SIP already.

**Our USD 20 minimum is five times a bank incumbent's entry point and is not a differentiator.** Differentiation has to rest on allocated title, the ICS benefit ladder, the credit facility, or India-corridor distribution. This belongs in the client conversation before it appears in a revenue projection.

---

## 6. Revenue streams in detail

### 6.1 Stream 1: Entry fee margin

**Type** inflow. **Activation** M1. **Rate** 5.00% Y1, 4.00% Y3, 3.00% Y10 (decision 9), less the tier discount.

**How it materialises.** Contribution clears, entry fee deducted, price struck at the next published LBMA fix, grams struck and transferred out of the float, AURX minted, float drawdown recorded, treasury replenishes on a threshold trigger at one bar denomination.

**Formula.**
```
For each segment s, each period t:
  fee_applied(s,t) = base_fee(t) − tier_weighted_discount(s,t)
  gross_inflow(s,t) = contributing(s,t) x ticket(s) + reduced(s,t) x 20
  cogs(s,t)  = gross_inflow x (1 − fee_applied) x fabrication_premium(t)
  gross_margin(s,t) = gross_inflow − gross_inflow x (1 − fee_applied) x (1 + premium)
  pricegap(s,t) = gross_inflow x pricegap_rate(t)
  floatcoc(s,t) = gross_inflow x float_coc_rate(t)
  rail(s,t)     = collection_events(s,t) x rail_cost_per_event
  STREAM1(s,t)  = gross_margin − pricegap − floatcoc − rail
```

**The cost build-up, re-derived.** The corpus carries 4.15%. Two components are wrong.

| Component | Corpus | **Corrected** | Why |
|---|---|---|---|
| Fabrication premium + dealer spread | 3.00% | 3.00% | Unchanged. **Estimated, not quoted. Blocked on the dealer** |
| Price-gap risk (1σ) | 0.36% | **0.79%** | Volatility 25% not 15%, and higher gold price lengthens the bar fill window from 8.7 to 12.1 days |
| Float cost of capital | 0.49% | 0.49% | **No derivation exists anywhere in the corpus.** Flagged, carried |
| Payment rail | 0.30% flat | **per-event fixed** | Formally retracted. UAE DD is a fixed fee per debit |
| **Total before rail** | 3.85% | **4.28%** | |
| Gross margin at a 5% fee | 1.15% | **0.72%** | Before rail |

**Key uncertainties.** The dealer quote sets 70% of the cost base and is unnamed. The rail cost decides the sign of the margin. Volatility at 30% rather than 25% pushes price-gap to ~0.95% and gross margin before rail to 0.56%.

### 6.2 Stream 2: Card interchange (54% of terminal revenue)

**Type** activity. **Activation** M18 assumed. **Gate** Gold tier, i.e. month 12 of a clean run.

**The verified interchange ladder** (Visa UAE IRF schedule effective 18 Oct 2025; CBUAE Notice 1998/2024 cap on debit and prepaid effective 1 Oct 2024). Confidence **High, primary scheme document.**

| ICS tier | Card level | Visa product | Interchange | Gold Rewards rate |
|---|---|---|---|---|
| Gold | L1 | Platinum | **1.80%** | 0.15% |
| Platinum | L2 | Signature | **2.05%** | 0.45% |
| Sovereign | L3 | Infinite | **2.10%** | 0.75% |
| *(prepaid, all products)* | — | — | *1.00% flat, capped* | — |

**Formula.**
```
eligible(t)        = accounts at Gold tier or above
active_cards(t)    = eligible x card_activation_rate
spend(t)           = active_cards x monthly_spend_per_active_card
gross_interchange  = SUM over tiers of [ spend(tier) x interchange_rate(tier) ]
STREAM2(t)         = gross_interchange x PM_SHARE
```

**The one number that sizes the business.** `PM_SHARE`, the programme manager's retained share of gross interchange. **No UAE or MENA split is published anywhere. Confirmed negative across two independent research passes.** The best available derivation:

Marqeta's FY2025 10-K states it receives **all** interchange from its customers' programmes and pays the programme manager out of it as revenue share, recorded as a reduction to net revenue. So Marqeta's net revenue take rate is what the **processor keeps**, and the residual is the programme manager's.

```
FY2025 net revenue / TPV = 624,884k / 382,513m = 16.34 bps of volume
At UAE credit interchange of 1.80% to 2.30%, that implies the programme
manager retains 90.9% to 92.9%.
```

That upper bound is not transferable: Marqeta's blended rate is set by Block/Cash App, its dominant customer with maximum leverage. Flooring it with the Polymath BIN-sponsorship benchmark (sponsor takes 25 to 50%, so PM retains 50 to 75%) gives the modelling range.

**Recommended: Base 72%, High 85%, Low 55%.** Use **Low for M18 to M30** (sub-scale, novel collateral profile) and step to Base thereafter.

**The floor that Phase 2 already established: 36%.** Below a 36% PM share, Gold Rewards at 0.75% stops self-funding at Sovereign (`_draft_credit-and-card-infrastructure.md` §8.2). Take 36% into the NymCard and sponsor conversations as the walk-away.

**Two gaps that bound the estimate.** Cross-border interchange sits above domestic and outside the cap, and for an expatriate base cross-border is the norm rather than the tail, but **no cross-border rate is published** so the model carries only domestic and is conservative by an unknown margin. And **per-transaction processor fees are not modelled**: at Stripe Issuing's published USD 0.10 per transaction, a AED 200 ticket costs 0.18% of value against a 1.80% gross rate, so small-ticket spend may be loss-making. Add a per-transaction fee line once a term sheet exists.

**Spend per active cardholder.** No official UAE per-card figure exists; CBUAE collects BIN-level data and publishes none. Best available: a survey of UAE expatriates gives a distribution with a computed mean of **AED 6,170/month**. Independent cross-check: **Kinesis calibrated its gold cashback cap at USD 2,000/month (AED 7,345)**, and Kinesis is the only tokenised-gold card in existence.

**Recommended: Base AED 6,000, High AED 9,000, Low AED 3,500.** **Weight the Low case heavily in the first two years**, because a new entrant's card is a secondary card until it is not.

**Card activation rate.** No named primary source publishes activation (activated ÷ issued) or a 12-month dormancy curve for any fintech programme. Triangulated from PULSE debit active rate (68.2%) and Monzo MAU/total (68%), both of which are mature-portfolio equilibrium rates rather than new-cohort activation. **Base 65%, High 80%, Low 45%.** Use the **High case** if the card is issued only to customers with a funded gold balance, which is the Aurumix design: intent is already demonstrated.

### 6.3 Stream 3: Family plan and Digital Will

**Type** headcount. **Activation** M1. **Not tier-gated**: open to everyone who pays; tier only prices it.

**Verified cost floor** (`_draft_family-and-succession.md` §11):

| Line | One-off | Annual |
|---|---|---|
| Identity verification | USD 1.25-1.85 | — |
| AML / PEP / sanctions at onboarding | USD 0.35-1.05 | — |
| Continuous screening per name | — | USD 0.36 |
| **Per-name floor** | **USD 1.80-2.90** | **USD 0.36** |

Two costs bind harder than the per-check rate. The **monitoring tail**: a registered beneficiary stays screened for 20 to 40 years, roughly **USD 7 to 14 per name undiscounted**, and no provider publishes multi-decade terms. And the **platform minimum**: Sumsub's Compliance plan is **USD 299/month verified from its own pricing page**, and it binds until ~162 verifications a month. At launch volumes the marginal name is nearly free and the fixed minimum is what hurts.

**Recommended pricing** (`_draft_family-and-succession.md` §11, awaiting client sign-off): **USD 29-36/year including up to 4 beneficiaries**, **USD 20 per additional name capped at ~USD 60 per household**, charged at registration and never at the transfer event. A Sovereign at the deepest discount pays ~USD 15-18/year against a USD 2.90 floor, so there is 5x headroom.

**Attach rate: nothing is stated anywhere in the corpus.** Exogenous assumption, flagged. **Base 20%, High 35%, Low 10%.**

**One leg is a mandatory cost centre.** For an India-resident beneficiary the estate must settle to cash, cash settlement is probably a redemption, and III.E.4 forbids a fee on redemption. **It is the most operationally expensive leg and it carries zero revenue by construction.**

### 6.4 Stream 4: Cardholder fees

**Type** activity. **Activation** with the card, M18. Three bases: FX margin on foreign spend, ATM withdrawals beyond the free monthly allowance, and issuance/replacement events.

Market rate for the FX margin is **~2.0%**, converged across Nexo, Crypto.com and Wirex. The sector has also converged hard on a **2% over-allowance ATM fee** with a ~USD 200/month free tier at entry level.

**This stream nets against stream 2 by design.** Every card benefit is a **waiver of stream 4 revenue funded by the stream 2 interchange the same spender generates**. So the model must forecast spend **by tier**, not in aggregate:

```
STREAM4(t) = SUM over tiers of [
    foreign_spend(tier) x fx_margin(tier)
  + max(0, atm_volume(tier) − free_allowance(tier)) x 0.02
  + issuance_events(tier) x issuance_fee(tier) ]
```

Tier ladder: FX margin 2.0% / 1.5% / 1.0% at Gold / Platinum / Sovereign; free ATM allowance AED 1,000 / 2,500 / 5,000 per month, not rolling.

⚠ **VAT is unresolved and touches every fee line.** 5% standard-rated for UAE residents, possibly zero-rated for non-resident customers under export-of-services rules. Given the base is deliberately NRI and GCC, this may be a **structural margin advantage rather than a cost**. Worth a tax opinion before pricing hardens.

### 6.5 Stream 5: Lending revenue share

**Type** activity and stock. **Activation** M24 assumed. **Gate** Gold tier. **Aurumix takes no credit risk**: the lender of record advances the money and owns the book. A VARA Lending licence cannot advance fiat against gold, so partnering is confirmed rather than merely likely.

```
eligible_collateral(t) = grams seasoned 90 days, unpledged, held by Gold+ accounts
facility_limit(t)      = eligible_collateral x gold_price x LTV(tier)
drawn(t)               = facility_limit x take_up_rate x drawn_pct_of_limit
STREAM5(t)             = drawn x aurumix_share_of_interest
                       + draw_events x origination_fee
                       + drawn x servicing_fee
```

**Every one of the five fee heads is unpriced in the corpus.** Origination, servicing, penal, recovery and interest share are named as components with no rates. They are partner term-sheet inputs.

**The behavioural drivers, which the corpus also lacks entirely, are now benchmarked:**

| Input | Base | High | Low | Basis |
|---|---|---|---|---|
| Take-up among eligible | **18%** | 30% | 8% | Indian gold-loan penetration is **<10% of gold-owning households at a point in time**, derived from organised AUM ÷ household gold stock. Aurumix's population is pre-selected (already chose to hold gold with us) so take-up should exceed the base rate, but competes against 6.5-7.5% APR unsecured UAE personal credit |
| Drawn as % of permitted limit | **50%** | 70% | 30% | Where the ceiling is high and access revolving (Coinbase, 75% cap), borrowers sit at 30-40%, i.e. 40-55% of permitted. Where the ceiling is 50%, they cluster near it |
| Realised LTV | **57%** | — | — | Manappuram actual, Q4 FY26, against a 75% cap. **Not the 80% ceiling** |

**Two structural effects to build in.** Manappuram's realised tenor is **71 days** against a 6 to 12 month product: gold borrowers redeem fast, so drawn balances are **episodic, not persistent**, and the annual average sits well below peak drawn. And the Finance House Key Facts Statement shows **bullet repayment generating 1.83x the interest of EMI** on identical principal, rate and term (AED 6,400 vs AED 3,503 on AED 20,000 over 24 months at 16%). A revolving non-amortising facility earns closer to bullet economics, which materially favours the revolving design.

**Pricing corridor, empirically anchored in two actual UAE gold products:** Emirates Money at **9% reducing** (80% LTV, AED 30,000 minimum, DMCC vault with Brink's) to Finance House at **16%** (75% LTV, 1% processing, 1% insurance).

⚠ **Recovery costs may be unchargeable.** If an enforcement sale is a "redemption" under III.E.4, no fee may be charged on it. Counsel question.

### 6.6 Stream 6: B2B platform fee

**Type** AUM. **The only line in the model that scales directly with assets under management, and it costs no customer acquisition.**

```
STREAM6(t) = partner_customer_AUM(t) x bps_rate / 12     [invoiced monthly, in cash]
```

Rate is a **placeholder at 0.5 to 0.75%/yr**. Worked example from the corpus: a USD 100m partner book at 60 bps is USD 600,000 a year, recurring.

**Partner-channel accounts earn no ICS**, so they consume none of the five benefit costs. **Structurally the highest-margin book in the model.**

**But the Indian precedent is a serious warning.** SafeGold, the closest analogue to this exact model (B2B2C digital gold distributed through 100+ partner apps, 55m customers, ₹6,867 cr of gold transacted in FY25), runs an **EBITDA margin of 0.03%**. Roughly ₹2 crore of EBITDA on ₹6,867 crore of volume. **Distributing grams on the spread is not a business at Indian retail scale.** If there is margin in a partner channel it has to come from the platform fee on the stock, which is precisely what stream 6 is, and not from the entry spread, of which the partner keeps 70 to 80% anyway.

🔴 **Build consequence with a hard date.** Stream 6 is a Year 2-3 revenue line with a **Week 1 build requirement**: the September build must be multi-tenant capable at the register and the mint. If it is not, this stream is lost for the rebuild cycle.

### 6.7 The India segment (S5)

**Treatment, per Abdur's instruction (2026-08-17): India is modelled as a market. The payment route is the client's problem, not ours.**

Implementation: **a full segment with its own adoption curve, behind an explicit `INDIA_ENABLED` switch, default ON, with the regulatory gate stated in the assumption note rather than silently priced in.** The model must never imply we have solved the funding route.

**Sizing, bottom-up from revealed behaviour rather than a hand-waved TAM:**

| Filter | Value | Source | Confidence |
|---|---|---|---|
| Indians holding gold as a **financial** instrument (gold ETF folios) | **12.48m**, +74.6% y/y | AMFI, Apr 2026 | **High** |
| Indians running a recurring monthly auto-debit investment | **106.3m** contributing SIP accounts | AMFI, Jul 2026 | **High** |
| …at an average ticket of | **₹3,008/month = USD 34** | Derived from AMFI | **High** |
| Active digital-gold holders (balance retention ~18%) | ~17.4m | SafeGold-derived | Medium |
| **Serviceable base** | **~12.5m**, ~20m including active digital-gold holders | Intersection | Medium-High |

**The USD 34 average Indian SIP ticket sits squarely inside the USD 20-75 band.** 106 million Indians already auto-debit approximately this amount monthly. That is the strongest single validation of the price point anywhere in the research.

**Three India-specific findings that change the model:**

1. **SEBI issued a public caution on digital gold on 8 November 2025**, stating it is neither a notified security nor a regulated commodity derivative and operates entirely outside SEBI's purview with no investor protection. **SEBI-registered brokers and RIAs cannot sell or recommend it.** This closes the highest-trust distribution channel and confines any Indian partner set to wallets, neobanks and jewellers. It also cuts the other way: a **VARA licence is the answer to the SEBI notice** and should be front and centre of positioning.
2. **Tax disadvantage.** AURX would attract physical-gold treatment: 24-month long-term threshold at 12.5%, against 12 months for a gold ETF. A 12-month disadvantage against the incumbent.
3. **Sovereign Gold Bonds are effectively dead** (last tranche Feb 2023, Gold Reserve Fund collapsing from ₹28,813 cr to ₹697 cr). **The government's own retail gold savings product has vacated the field with no replacement.**

⚠ **The model prices India as a market. It does not assert a compliant route exists.** Decision 27 stands: India is closed to residents on multiple independent bars. The switch exists so the client can see the size of what the payment problem is costing them.

---

## 7. Cost architecture

### 7.1 Cost of goods sold

Inside stream 1: fabrication premium, price-gap risk, float cost of capital, payment rail. See 6.1. **Not an opex line.**

### 7.2 Benefit costs (contra-revenue)

| Benefit | Cost type | Funded by | Model treatment |
|---|---|---|---|
| Entry-fee discount (0 / 0.4 / 0.8 / 1.2 / 1.5 pp) | **Real, reduces stream 1** | Stream 1 base-rate uplift | Reduce `f` by tier-weighted discount |
| Credit LTV ladder (— / — / 50 / 65 / 80%) | **Zero cash cost. Revenue-positive** | Stream 5 | Higher LTV raises drawn balances |
| Card tier (FX 2.0 / 1.5 / 1.0%, ATM allowance) | **Waived stream 4 revenue** | Stream 2 interchange | Net against stream 4, do not double count |
| Gold Rewards (— / — / 0.15 / 0.45 / 0.75%) | **Real unit cost per event** | Stream 2 + stream 5, net of custody | Haircut on stream 2, capped at customer-generated revenue |
| Will and family discount (0 / 10 / 20 / 35 / 50%) | **Real, reduces stream 3** | Stream 3 price headroom | Reduce stream 3 price by tier |

**Gold Rewards is capped at the interchange and credit revenue that customer generated, net of their custody cost.** So if `PM_SHARE ≥ 36%` it can never exceed its funding line by construction. Model it as a haircut on stream 2, not as an independent cost.

**The launch-year cost of the entire ladder is one 0.4pp Silver discount.** Time-phasing is doing enormous work here and should be shown to the client explicitly, because it is the reason a generous-looking benefit set is affordable.

⚠ **The one arithmetic conflict Phase 2 left unresolved.** The discount ceiling is 1.5pp at Sovereign, against a Year 1 gross margin of 0.72% before rail. **The ceiling exceeds the available margin.** Either the base rate rises above 5% (outside the client's stated range) or the ladder is loss-making at the top. Section 9 solves this.

### 7.3 Acquisition cost

**Member referral.** 30% of the entry fee the referee paid over their six qualifying contributions, split equally, credited in grams. At a 5% fee that is **1.50% of the referee's six-month contributions**, or USD 6.75 at the target ticket. Paid at the referee's gate, so **no earlier than month 13 from launch in any version**.

The self-funding claim was **withdrawn, not repaired** (`_draft_referral-system.md` §5.0): the reward was tested against a 2.15% gross margin that had not yet paid for price-gap, float or rail. Against the real Year 1 net margin the reward is roughly **double** the margin on the run that generated it. Honest frame is CAC vs LTV: the reward is a constant **19.4% of contribution-margin LTV at every ticket size**, with payback at **month 9 to 11**.

⚠ **That LTV calculation used ~40 paying months from the 79%/38% persistency curve. At the corrected curve (55% M13, 19% M61) paying months fall to roughly 22, LTV nearly halves, and the reward becomes ~35% of LTV.** This must be re-run, and it is the strongest single argument for sizing the reward at option (a), the small thank-you, rather than option (b) at USD 12-15 a side.

**Agent commission.** The client's only ever written number is **15% of the fee**, whose base (the Algorithmic Growth Fee) no longer exists. Transplanted to the entry fee, 15% consumes **0.75pp of 0.85pp, or 88% of Year 1 gross margin.** The client has not seen this arithmetic.

**The acquisition budget ceiling** is one board-approved cap covering member rewards plus all agent commission at every level, expressed as a percentage of entry-fee revenue, modelled on IRDAI's Expenses of Management regime (overall ceiling, front-loading braked, excess borne by shareholders). **The number is a Phase 4 output.** See Section 9.

### 7.4 Operating expenses

Constructed from benchmarks. The client supplied one figure. **Salary lines are Low-Medium confidence** and should be replaced with a purchased UAE salary guide before the model is presented as final. Loading is **1.10x on quoted total cash**, not 2.0x, because UAE salary guides already quote base plus allowances; applying the base-salary multiplier to a total-cash figure double counts.

| Block | Y1 (500) | Y3 (12,000) | Y10 (80,000) | Confidence |
|---|---|---|---|---|
| Headcount | 588,000 | 1,340,000 | 4,600,000 | Low-Med (salary guides via secondaries) |
| MLRO (outsourced Y1, in-house from Y3) | 49,000 | 163,000 | incl. above | Medium |
| VARA supervision | 54,500 | 94,500 | 110,000 | **High, VARA's own rulebook** |
| Audit + reserve attestation | 35,000 | 60,000 | 180,000 | Med / **Judgement on attestation** |
| Compliance tooling + KYC | 31,600 | 97,200 | 255,500 | **High** on Sumsub, Med on the rest |
| Vault and metal | 12,000 | 150,000 | 800,000 | Medium |
| Technology | 34,000 | 115,000 | 600,000 | Low |
| Corporate (licence, office, visas) | 20,700 | 60,000 | 350,000 | **High, DMCC's own schedule** |
| Security | 10,000 | 35,000 | 200,000 | Med |
| Marketing | incl. below | 250,000 | 1,200,000 | Judgement |
| Legal, insurance, contingency | 60,000 | 120,000 | 400,000 | Judgement |
| **Total annual opex** | **845,800** | **2,506,000** | **8,495,500** | |
| Cost per investor | USD 1,692 | USD 209 | USD 106 | |
| **Opex as % of AUM** | **33.8%** | **4.2%** | **2.1%** | |

**One-off Year 1, additional:** VARA application AED 100,000 (USD 27,200), tier-1 smart contract audit USD 75,000, DMCC incorporation USD 3,280, ADGM SPV USD 1,900, licensing support USD 20,000. **Total USD 127,380.** Year 1 all-in ≈ **USD 973,000**.

**Four corrections to how the corpus treats costs:**

1. **The USD 75,000 audit is not a one-off.** VARA mandates an annual tech audit and penetration test by a qualified independent third party, **plus one before every new system or product launch** (Technology Rulebook). Budget tier-1 for the launch audit and mid-tier (USD 15,000-25,000) for annual re-audits.
2. **ARVA reserve audit is required every six months.** Kinesis uses Bureau Veritas biannually and Paxos uses KPMG monthly, which confirms the cadence is market-normal. **No issuer discloses what it costs. Get a Bureau Veritas quote; it is the single biggest unpriced line.**
3. **The vault minimum binds at launch.** DGCX publishes USD 0.10/kg/day with a **USD 25/day minimum**, i.e. USD 9,125/year regardless of volume. At Year 1 AUM the per-kg charge would be USD 646, so the minimum applies and the **effective rate is 0.37%, not 0.026%.** It decays to immateriality around 250 kg.
4. **The model may be under-scoped on VARA activities.** Category 1 Issuance alone may not cover distributing or redeeming the token. Broker-Dealer and VA Transfer & Settlement each add AED 80,000-200,000/year plus extension fees. **Confirm with VARA before the cost base locks.**

**The competitive fact that governs custody pricing.** Every major comparator charges holders **zero** storage: PAXG 0%, XAUT 0%, Kinesis 0%, Comtech 0% for 24 months. **The client's 0.8-1.0% custody fee is not viable against this field, and it is also roughly 3 to 6 times the real cost.** Verified allocated storage clusters at **0.12-0.40%** (BullionVault 0.12% with a USD 4/month minimum; GoldMoney 0.25%; SGPMX 0.40-0.50%). Our internal 0.15-0.40% estimate is **vindicated**; the client's assumption is not. Decision 42 (retail storage free forever, recovered via Gold Rewards netting and the B2B platform fee) is confirmed as correct.

⚠ Worth copying: **PAXG's terms reserve the right to introduce a storage fee via dilutive token issuance on 30 days' notice.** That accrues a charge without an invoice and is already market-accepted.

---

## 8. Assumptions register

### 8.1 Fixed inputs

| ID | Assumption | Value | Unit | Rationale | Confidence |
|---|---|---|---|---|---|
| F1 | Gold price (flat) | **141.46** | USD/g | USD 4,400/oz, verified 2026-08-17. **Held flat by design: every revenue change is then attributable to the business, not the metal.** Sensitivity axis, not a scenario variable | High |
| F2 | AED/USD peg | 3.6725 | — | Pegged | High |
| F3 | Entry fee, Y1 / Y3 / Y10 | 5.0 / 4.0 / 3.0 | % | Decision 9. Falls with bar denomination | Client range + our arithmetic |
| F4 | Fabrication premium, Y1 / Y3 / Y10 | 3.00 / 2.00 / 0.75 | % | 100 g / 1 kg / Good Delivery. **Estimated. Blocked on the dealer** | **Low** |
| F5 | Float cost of capital | 0.49 / 0.31 / 0.38 | % | **No derivation exists in the corpus.** Carried, flagged | **Low** |
| F6 | SIP hard floor | 20 | USD/month | Rejected outright below, never partially credited | High |
| F7 | Confirmed SIP gate | 6 | consecutive periods | Client's own figure | High |
| F8 | Grace period | 5 | calendar days | Revised 2026-08-10 | High |
| F9 | Withdrawal allowance (Retention = 1.000) | 30 | % per rolling 12m | Decision 46 | High |
| F10 | Collateral seasoning | 90 | days | Benefits draft §2.5 | High |
| F11 | LTV ladder, Gold/Platinum/Sovereign | 50 / 65 / 80 | % | Settled 2026-08-13 | High |
| F12 | Interchange, Gold/Platinum/Sovereign | 1.80 / 2.05 / 2.10 | % | **Visa UAE IRF schedule, 18 Oct 2025** | **High, primary** |
| F13 | Gold Rewards monthly qualifying-spend cap | 3,000 | USD/month | Kinesis-comparable (its cap is USD 2,000) | Medium |
| F14 | VARA annual supervision, Cat 1 | 200,000 | AED/yr | **VARA's own rulebook** | **High** |
| F15 | Minimum paid-up capital | 1,500,000 | AED | **Locked, not expensed. Do not run through P&L** | High |
| F16 | Sumsub Compliance plan | 299 + 1.85 | USD/mo + per check | **Sumsub's own pricing page.** Minimum binds below 162 checks/mo | **High** |
| F17 | Referral reward | 30 | % of referee's entry fee over the run | Shape settled; **the 30 is a placeholder** | Settled shape |
| F18 | Referral payout lag | 6 | months after referee signup | Gate cannot be compressed | High |
| F19 | Salary loading | 1.10 | x quoted total cash | Not 2.0x. Guides quote base + allowances | Medium |

### 8.2 Scenario variables

| ID | Parameter | Base | Aggressive | Conservative | Unit | Why it varies |
|---|---|---|---|---|---|---|
| **S1** | **Rail cost per collection event** | **0.25** | 0.10 | **1.36** | USD | 🔴 **The single most important unknown in the model.** AANI Request to Pay cost is unpublished; UAEDDS at AED 5 is the adverse case. **Conservative makes the SIP loss-making at the target ticket** |
| **S2** | **Persistency, M13 survival** | **55** | 65 | 45 | % | 🔴 Governs LTV, referral economics and agent commission simultaneously. See 0.5 |
| **S3** | **PM share of gross interchange** | **72** | 85 | 55 | % | 🔴 Sizes 54% of terminal revenue. **No UAE/MENA figure published. Floor is 36%** |
| S4 | Monthly card spend per active card | 6,000 | 9,000 | 3,500 | AED | Expat survey mean AED 6,170; Kinesis cap implies AED 7,345 |
| S5 | Card activation rate | 65 | 80 | 45 | % | No primary source exists. Use High if issued only to funded balances |
| S6 | Gold volatility | 25 | 20 | 35 | % annualised | Drives price-gap risk. ~30% trailing 12m, 17% 20-year average |
| S7 | Fabrication premium (Y1) | 3.00 | 2.00 | 4.50 | % | Dealer-blocked. Four research passes returned nothing |
| S8 | Credit take-up among eligible | 18 | 30 | 8 | % | Indian gold-loan penetration <10% at a point in time; pre-selection uplift |
| S9 | Drawn as % of permitted limit | 50 | 70 | 30 | % | Revolving facilities draw 40-55% of permitted |
| S10 | Self-custody leakage | 12 | 6 | 30 | % of AUM/yr | Free up to the 30% allowance. Hits five streams |
| S11 | Family plan attach rate | 20 | 35 | 10 | % | **Nothing stated in the corpus.** Pure assumption |
| S12 | Agent productivity | 4 | 6 | 2 | accounts/agent/month | Insurance agency comparator |
| S13 | B2B partner AUM by Y10 | 200 | 400 | 50 | USD m | Requires a signed partner |
| S14 | Vault storage rate | 0.25 | 0.15 | 0.40 | % of AUM/yr | Verified range. **Minimum binds below ~250 kg** |
| S15 | Marketing CAC | 120 | 80 | 200 | USD | No UAE gold-product benchmark |

### 8.3 Time-evolving inputs

| ID | Parameter | Y1 | Y2 | Y3 | Y5 | Y10 | Pattern |
|---|---|---|---|---|---|---|---|
| T1 | Entry fee base rate | 5.0% | 5.0% | 4.0% | 4.0% | 3.0% | Step, with bar denomination |
| T2 | Fabrication premium | 3.00% | 3.00% | 2.00% | 2.00% | 0.75% | Step, with bar denomination |
| T3 | Bar denomination | 100 g | 100 g | 1 kg | 1 kg | 12.4 kg | Threshold rule, see below |
| T4 | Tier mix: share at Gold+ | 0% | 28% | 45% | 52% | 55% | Computed by the ICS engine, not assumed |
| T5 | Tier mix: share at Sovereign | 0% | 0% | 0% | 0% | 8% | **First Sovereign at M61** |
| T6 | PM share (contract maturity) | — | 55% | 55% | 72% | 72% | Steps at scale |
| T7 | Active agents | 5 | 15 | 40 | 90 | 200 | Client input required |
| T8 | Segments live | S1-S3 | +S4, S5 | +S6 | all | all | Perimeter expansion |

**T3, the denomination upgrade rule** (`_draft_allocation-and-float.md`): upgrade when `(annual gram volume × premium saved per gram) > (incremental float × cost of capital) + incremental price-gap risk`. Worked at Year 3, moving 1 kg to Good Delivery saves ~1.25% on USD 10.8m of annual purchases (~USD 135k/yr) for ~USD 1.2m of extra float, an ~11% return on incremental capital. It clears at Year 3 and fails at Year 1, which is why 100 g is right at launch.

### 8.4 Dependency map

```
Rail cost (S1) -----------------------------> sign of stream 1 margin
    |                                              |
    +--> minimum viable ticket ---> segment mix ---+--> referral viability
                                                   |
Persistency (S2) --> paying months --> LTV --------+--> referral reward size (Sec 9)
    |                                              +--> agent commission (Sec 9)
    +--> surviving accounts --> ICS tier mix (T4/T5)
                                    |
                                    +--> benefit costs (contra-revenue)
                                    +--> credit eligibility --> stream 5
                                    +--> card eligibility ----> streams 2 and 4
                                              |
PM share (S3) ----------------------------------+--> stream 2 (54% of revenue)
                                                +--> Gold Rewards ceiling (Sec 9)
Gold price (F1, flat) --> AUM --> stream 6, custody cost, collateral base
Leakage (S10) --------> AUM --> streams 2,3,5,6 and custody absorption
```

**The five load-bearing assumptions, ranked by cascade impact:** S1 rail cost, S3 PM share, S2 persistency, S7 fabrication premium, S4 card spend. **Three of the five are commercial conversations, not research.**

---

## 9. The parameter solver

Eight numbers were parked across Phase 2 with the note "locks against the revenue model." The model returns each as a solved value with its arithmetic shown, not as an input.

| # | Parameter | Constraint it solves against | Method |
|---|---|---|---|
| 1 | **Entry-fee base uplift funding the discount ladder** | Top-tier discount (1.5pp) must be payable from the uplift, not from margin | `uplift = 1.5pp x (steady-state share of contributions at Sovereign)`, then verify margin at every tier remains positive. **Currently the 1.5pp ceiling exceeds the 0.72% margin, so either the uplift is real or the ceiling falls** |
| 2 | **Gold Rewards rate ceiling** | `cumulative rewards <= cumulative (interchange + credit) − custody cost`, per account | Solve the top-tier rate at the modelled PM share. At 72% and 2.10% interchange the ceiling is comfortably above 0.75%; **at the 36% floor it binds exactly** |
| 3 | **Referral reward size** | Reward as % of contribution-margin LTV, at the corrected persistency | Solve for the rate at which reward ≤ 25% of LTV. **At the corrected curve, 30% of the fee is ~35% of LTV, so the answer is likely 20-22%, not 30%** |
| 4 | **Agent commission, three levels** | Total acquisition ≤ the budget ceiling; gradient front-loaded per V2's 4/5/6 | Solve the total pool from the ceiling, then split on the recommended gradient |
| 5 | **Acquisition budget ceiling** | Net profit ≥ 0 at the target scale, IRDAI-style first-year vs renewal asymmetry | Solve as % of entry-fee revenue. **Note: if entry-fee revenue is only 8% of the business, a ceiling expressed against it is the wrong denominator. Recommend re-expressing against total revenue** |
| 6 | **Tenure rebate size** | Must be funded by an entry-fee uplift on the spot lane, not from margin | Solve against spot margin. **Rebate room is 0.10-0.75%; the old decaying fee it replaced was ~1.5%. These cannot both be true** |
| 7 | **B2B platform fee bps** | Must cover custody absorption on the partner book plus a margin | Solve `bps ≥ vault rate + target margin`. At a 0.25% vault rate, **50 bps is the floor and 60-75 bps is the range** |
| 8 | **Family plan and per-beneficiary price** | Discounted price at Sovereign ≥ verified per-name cost floor | Already solved in `_draft_family-and-succession.md` §11: **USD 29-36/yr and USD 20/name** gives 5x headroom. Confirm against the contracted KYC rate |

**Item 5 deserves a flag to the client.** The corpus expresses the acquisition ceiling as a percentage of entry-fee revenue, following IRDAI's premium-based logic. But if entry fee is 8% of terminal revenue and interchange is 54%, a ceiling anchored to entry fee will either strangle distribution or be meaningless. **Recommend re-anchoring to total net revenue.**

---

## 10. Calculation reference

### 10.1 Model sheet row structure

```
Rows 1-5      TIME:      period #, month #, year #, monthly-or-annual flag, activation flags
Rows 8-40     ACQUISITION: new accounts by channel x segment
Rows 42-90    COHORT ENGINE: one block per segment
                 opening contributing / reduced
                 + new  − reduction transfers  − lapses
                 closing contributing / reduced
Rows 92-120   FLOW:      gross inflow by segment; collection events by segment
Rows 122-150  STREAM 1:  gross margin, price-gap, float CoC, rail, net (per segment)
Rows 152-190  ICS ENGINE: Months, Recent, Sold, Record, Standing, Retention, ICS, tier counts
Rows 192-215  AUM STOCK:  grams opening, bought, rewards, redeemed, leakage, closing, USD
Rows 217-250  CARD:      eligible, active, spend by tier, gross interchange, PM share, STREAM 2
Rows 252-275  CARDHOLDER FEES: FX, ATM, issuance, net of tier waivers, STREAM 4
Rows 277-300  CREDIT:    eligible collateral, facility limit, drawn, STREAM 5
Rows 302-315  FAMILY:    accounts, attach, names, price net of discount, STREAM 3
Rows 317-330  B2B:       partner AUM, bps, STREAM 6
Rows 332-350  BENEFIT COSTS: discount, Gold Rewards (capped), will discount
Rows 352-375  ACQUISITION COST: agent, referral (lagged), ceiling test
Rows 377-420  OPEX:      by block
Rows 422-450  P&L:       revenue, COGS, benefits, acquisition, opex, EBITDA, net
Rows 452-470  BREAK-EVEN: cumulative net, months to breakeven, required investors
```

### 10.2 Key formula patterns

```
Cohort survival (monthly hazard from an annual survival input):
  h = 1 − S13^(1/13)                     [fitted to the M13 anchor]
  closing = opening x (1 − h) + new − reduction_transfers

Unit margin, per segment (the core equation):
  = inflow − inflow x (1 − fee_applied) x (1 + premium)
    − inflow x pricegap − inflow x float_coc
    − collection_events x rail_cost

Price-gap rate (recompute, do not hard-code, it moves with scale and vol):
  cycles      = annual_grams / bar_grams
  window_days = 365 / cycles
  sigma_win   = vol x SQRT(window_days / 365)
  pricegap    = (bar_value x sigma_win x SQRT(cycles)) / annual_purchases

ICS, per cohort:
  Record    = IF(M<=12, 4.1667*M, IF(M<=60, 50+1.04167*(M−12), 100))
  Standing  = 8.3333 * Recent
  Retention = IF(Sold<=0.30, 1, 1−(Sold−0.30)/0.70)
  ICS       = MAX(25, MIN(Record, Standing) * Retention)
  Tier      = lower-bound lookup at 25 / 50 / 75 / 100

Interchange:
  = SUMPRODUCT(active_cards_by_tier, spend, interchange_rate_by_tier) * PM_SHARE

Gold Rewards, capped (never an independent line):
  = MIN( SUMPRODUCT(spend_capped_at_3000, reward_rate_by_tier),
         cumulative_interchange + cumulative_credit − cumulative_custody_cost )

Referral cost, lagged 6 months and ceiling-tested:
  = MIN( referred_gates_resolving(t) x reward_per_referral,
         acquisition_ceiling(t) − agent_commission(t) )

Conditional activation:
  = IF(period >= activation_month, calculation, 0)
```

### 10.3 Break-even solver

```
Required investors(year) = annual_opex(year) / annual_margin_per_investor(year)

where annual_margin_per_investor =
      12 x net_contribution_margin_per_month
    + card_eligible_probability x activation x annual_interchange_per_card
    + annual_cardholder_fees_per_card
    + credit_eligible x take_up x annual_credit_revenue_per_borrower
    + family_attach x annual_family_revenue
```

Report **two** figures per year and the gap between them is the finding:
- **Entry-fee-only break-even** (the pessimistic bound, and the honest answer to "can the savings product pay for itself")
- **All-streams break-even** (the real answer, which depends on card attach far more than on investor count)

---

## 11. Excel structure map

Five sheets, standard colour coding: **blue inputs, black formulas, green cross-references.**

- **Cover** — purpose, version, scenario selector, headline outputs, the five load-bearing assumptions, source and confidence key
- **Assumptions** — F-series, by block, each with rationale, source URL and confidence
- **Scenario Parameters** — S-series with Base/Aggressive/Conservative and a `CHOOSE()` selector at D6; plus the `INDIA_ENABLED` switch and the `GOLD_PRICE` sensitivity cell
- **Model** — 65 columns (60 monthly + 5 annual), rows per 10.1
- **Opex** — headcount and cost stack, its own sheet because it is the headline denominator
- **Summary** — P&L by year, break-even table, tier distribution chart, revenue mix chart, the eight solved parameters, and the sensitivity grid on S1/S2/S3

---

## 12. Break-even architecture (the headline output)

Three views, in this order.

**View 1: the entry fee alone.** Answers "does the savings product pay for itself?" Answer: **no, at any modelled scale.** 171,911 investors at Year 1 costs, rising to 786,620 at Year 10 costs.

**View 2: all streams.** Answers "when does the company make money?" Break-even lands where card attach and spend cross the opex curve, modelled around **Year 7 to 9** in the base case, and **never** in the Conservative case if the PM share lands at 55% and card spend at AED 3,500.

**View 3: the sensitivity that matters.** A grid on the three assumptions that carry the model:

|  | PM share 55% | PM share 72% | PM share 85% |
|---|---|---|---|
| **Card spend AED 3,500** | never | Y10+ | Y9 |
| **Card spend AED 6,000** | Y9 | **Y8 (base)** | Y7 |
| **Card spend AED 9,000** | Y8 | Y6 | Y6 |

**The sentence this model exists to produce:** *"Break-even is not a function of how many savers you sign up. It is a function of how many of them carry your card and how much they spend on it. On the entry fee alone the business does not break even at any investor count on your roadmap."*

---

## 13. Corrections owed to Phase 2

The model surfaced these. Each is a real error, not a caveat.

| # | Target | Correction | Severity |
|---|---|---|---|
| 1 | Every worked example in the corpus | Gold at **USD 141.46/g, not 109.31**. USD 75 buys **0.5037 g, not 0.6518 g**. Bar values, float sizing and fill windows all move | 🔴 **Filing-grade** |
| 2 | `_draft_allocation-and-float.md`, decision 9 | Price-gap risk is **0.79%, not 0.36%**, at 25% volatility and the corrected fill window. Cost build-up before rail is **4.28%, not 3.85%** | 🔴 |
| 3 | Decision 22, `_draft_sip-rulebook.md` §14 | Persistency should be **~55% M13 / ~19% M61**, and the 79%/38% figures are LIC **by premium**; the right basis for a low-ticket product is **by policy count (64%/50%)**, then adjusted downward for the absence of a lock-in | 🔴 |
| 4 | Decision 31, `_explainer_how-we-take-money.md` §5 | The launch perimeter is **4.58M, not 3.5-4M**. MEA 2025 primary. We understated ourselves | ⚠ |
| 5 | Market research, competitive set | **Liv Gold (Emirates NBD) at AED 15 with physical redemption** is a direct incumbent and appears nowhere in Phase 1 or 2 | 🔴 |
| 6 | `_draft_entities-licensing-and-payments.md` §3.2 | VARA licence extension: the corpus says "+50% of the lower application fee"; **verify against Schedule 2, which the credit draft reads as AED 200,000 flat.** The two drafts disagree | ⚠ |
| 7 | `_draft_family-and-succession.md` §11 vs `_draft_ics-scoring.md` §6.5 | Per-beneficiary discount at Platinum: **20% vs 10%.** Scoring file is later and settled. Use 10% | ⚠ |
| 8 | `_draft_referral-system.md` §5.4 vs §5.1 | Reward as share of LTV stated as **21.7% and 19.4%** in the same document. Use 19.4% (visible arithmetic) | ⚠ |
| 9 | Client document §2.2 | The client's own entry fee row says "2% to 5%" but works the example at **USD 1.50 to 2.25 on USD 75, which is 2% to 3%.** Their range and their example disagree | ⚠ |
| 10 | Cost planning | **The USD 75,000 audit is recurring**, not one-off. VARA requires an annual tech audit plus one before each product launch, and a **six-monthly ARVA reserve audit** | 🔴 |

---

## 14. Open questions and defaults

| Question | Owner | Default used | Impact if wrong |
|---|---|---|---|
| 🔴 **AANI Request to Pay cost per collection** | PSP conversation | USD 0.25 | **Decides the sign of stream 1.** At AED 5 the SIP loses USD 0.70 per contribution |
| 🔴 **Programme manager share of interchange** | NymCard / sponsor term sheet | 72% | **Sizes 54% of terminal revenue.** Floor is 36% |
| 🔴 **Dealer: fabrication premium, two-way spread, will they carry the float** | Dealer conversation | 3.00% premium, dealer-carried | 70% of the Year 1 cost base |
| 🔴 **Vault quote** | Vault conversation | 0.25%/yr, USD 25/day minimum | Validates retail absorption and prices stream 6 |
| 🔴 **Credit or prepaid** | Client, before the September build | **Credit** | ~USD 3.2m/yr at Year 10 |
| **Reserve attestation cost** | Bureau Veritas quote | USD 13,200/yr Y1 | Biggest unpriced opex line |
| **Does the Y10 target count accounts opened or investors still contributing?** | Client | Still contributing | At 19% M61 persistency these differ by ~5x |
| **Lending partner: five fee rates** | Partner term sheet | Interest share 4pp of a 12% facility | Stream 5 entirely |
| **Family plan attach rate** | Nothing exists | 20% | Stream 3 entirely |
| **Launch date** | Client | **Jan 2027** | Shifts everything |
| **Agent productivity and headcount plan** | Client | 4 accounts/agent/month | Acquisition volume |
| **VAT on fees** | Tax opinion | 5% resident, 0% non-resident | Touches every fee line; may be a margin advantage |

---

## 15. Data provenance

**High confidence, primary source read directly:** Visa UAE interchange schedule; VARA Schedule 2 fee table and Technology/Company Rulebooks; IRDAI Handbook 2024-25 Table 28; AMFI monthly SIP and gold ETF data; Marqeta FY2025 10-K and Q4 earnings release; Sumsub pricing page; DMCC schedule of charges; ADGM SPV fees; BullionVault tariff; Perth Mint fees; CBUAE Financial Stability Report 2024 (WPS wages, remittance corridors); Al Ansari Financial Services Annual Report 2025; Finance House Gold Loan Key Facts Statement; Kalyan Jewellers RHP; Manappuram Annual Reports FY23/FY24; Liv Gold product page; Kinesis card page and audit archive; Paxos transparency page.

**Medium:** MEA overseas Indians table (via mirror; **mea.gov.in refused all connections, recommend manual verification of the six rows before client delivery**); RBI Sixth Remittances Survey (rbi.org.in returns 403); SEBI digital gold caution (sebi.gov.in refused; verified via NSDL circular reproducing it and two independents); gold price (triangulated across three sources at USD 4,388-4,414, one outlier at 4,528 discarded); UAE salary guides via secondaries.

**Low, and flagged as such throughout:** the 65/20/15 blue/white/professional occupational split of UAE Indians (uncited tertiary); the gold-savings propensity filter in the addressable funnel (**no published source exists**); cloud cost per user; all marketing and CAC assumptions.

**Confirmed negatives, each a finding rather than a search failure:**
- No monthly-versus-annual persistency split exists in Indian public data.
- No UAE or MENA programme-manager interchange split is published anywhere.
- No survey quantifies the share of gold-owning households that have **ever** taken a gold loan.
- No named primary source publishes a card activation rate or 12-month dormancy curve.
- CBUAE publishes no POS/ATM series and no card-type breakdown; no domestic-versus-cross-border split of UAE card spend exists.
- No Indian or Gulf jeweller publishes a savings-scheme completion or subscriber figure.
- No Dubai vault operator publishes a custody rate card. **This is the highest-value phone call in the engagement.**
- No gold-token issuer discloses what reserve attestation costs.

---

## 16. Build sequence

1. **Client and Abdur sign off Section 3** (the engine) and the Section 8.2 scenario values.
2. Build **Opex** sheet first. It is the denominator of the headline output.
3. Build the **cohort engine** for one segment, validate against the Rajesh worked example, then replicate.
4. Build the **ICS state machine** and verify the tier distribution reproduces the nine personas in `_draft_ics-scoring.md` §7.1.
5. Layer revenue streams in activation order: 1, 3, then 2 and 4 at M18, then 5 and 6 at M24.
6. Add benefit costs, then acquisition cost with its lag and ceiling.
7. Wire the **break-even solver** and the **parameter solver**.
8. Run the S1/S2/S3 sensitivity grid.
9. Explainer document (separate deliverable, `revenue-model-explainer` skill).

**Depth benchmark:** `DRODE_Revenue_Model_Architecture_Brief_V2.1.md`, 1,791 lines, and its V3 workbook.
