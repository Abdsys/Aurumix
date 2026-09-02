# Aurumix — Simulation Classification

**Date:** 2026-09-02 (v2 — rewritten same day after client-side direction, see §0)
**Phase:** 5 — Simulations. Step 1 of four (classify → blueprint → build → document).
**Inputs read:** `4-revenue-modeling/Aurumix_Revenue_Model_Architecture_Brief_Simplified.md` (v3.0), `Aurumix_Revenue_Model_Architecture_Brief.md` (v2.6, provenance record, §5.9 in particular), `tools/Aurumix_Revenue_Model.xlsx` (built through net profit, 2026-08-31), `0-discovery/Aurumix_Project_Charter.md`, `handoff.md`.

---

## 0. What this version changes, and why

v1 of this document was written against the v3.0 brief. **The brief is stale in one load-bearing place and the workbook already knows it.** Four directions taken on 2026-09-02 reshape the simulation:

| # | Direction | Consequence |
|---|---|---|
| 1 | **The Excel's assumptions are not fixed inputs.** Varying them is the point | The pinned-parameter run is demoted to a one-off *calibration check*, not a constraint on the work |
| 2 | 🔴 **The gate no longer controls card access — anyone can hold a card, spot buyers included. ICS earns discounts, not entry** | The central question stops being *"who qualifies?"* and becomes **"what can we afford to give back?"** |
| 3 | 🔴 **Profitability is the objective**, and specifically *what must be true to reach it* | The simulation is an **inversion** problem, not a forecasting one |
| 4 | **Fabrication premium is a cost to Aurumix. The customer pays 5% and that is the ceiling** | Settled. Matches the workbook. **v3.0 brief §3.3 now contradicts the model and must be corrected** |
| 5 | 🔴 **Discounts must differ BY TIER** — four benefit-bearing tiers above standard | The giveback is **4 tiers × 5 benefits = 20 rates**, not four blended ones. Requires the simulation to compute a tier mix, which is precisely what the 2026-08-26 blend instruction was waiting for (§5) |

**On item 2, the evidence that the workbook already moved.** `Model!B44` reads `Card-eligible base = paying customers + holders × switch` — no gate term. `Model!B45` is labelled *"Reaches an ICS benefit tier (memo — **drives discounts, not access**)"*, and `Assumptions!B149` carries the note *"REPURPOSED 2026-08-26 (CG decision)."* The 55%/M8 pair was moved from card eligibility to benefit entitlement. **The v3.0 brief's §3.1 claim — *"the card streams are ~83% of gross profit and every one of them requires clearing the six-payment gate"* — is withdrawn by that decision and should be struck.**

---

## 1. Does This Protocol Need a Simulation?

**Verdict: Yes — and the reason has changed since v1 of this document.**

It is no longer principally about sourcing two deleted cells. It is that **the three decisions the client most needs to make are all inversions, and a deterministic spreadsheet cannot invert.**

1. **What must be true for this business to be profitable?** The workbook runs forward from ~90 assumptions to one profit line. It cannot run backward from *"profitable"* to the set of configurations that achieve it. At Y3 the book is 16,621 paying customers and loses USD 73k; at Y4 it is 31,586 and makes USD 261k. **Annual break-even sits between those two and has never been located.**
2. **How much can Aurumix afford to give back through ICS?** The four discount rates are typed placeholders. They cost **USD 364k at Y7 against USD 847k of net profit — 43% of profit, at rates nobody derived.**
3. **Where is the profit actually concentrated?** The model carries one ticket per region. It cannot represent a high-ticket customer, so it cannot say whether the business is made by many small savers or few large ones — and the acquisition strategy depends entirely on the answer.

Add the two standing reasons that survive from v1: peak funding of USD 2.29m is a point estimate the founders will raise against, and cumulative break-even lands in Y6 by USD 209k against that year's USD 3.06m cost base — a 6.8% margin reported as a finding.

---

## 2. What Questions Should the Simulation Answer?

Reordered around profitability. **Questions 1–3 are the deliverable; 4–6 are the risk envelope around it.**

| # | Question | Why It Matters | Shape of the Answer |
|---|---|---|---|
| **1** | **What does it take to be profitable?** Minimum book size, mix and timing to cover the cost base — and the cheapest levers that pull it earlier. | The client's stated objective. The workbook brackets break-even between Y3 and Y4 and has never pinned it. | A **threshold plus a lever ranking**, not a forecast |
| **2** | **How much can we afford to give back through ICS, tier by tier?** A swept menu over the **ladder shape** across four tiers × five benefits, against profit, margin and break-even year. | 43% of Y7 profit is currently given away at undesigned rates, collapsed to four blended numbers because the workbook cannot compute a tier mix. | A **cost matrix by tier and benefit**, and an **affordability envelope** — explicitly **not** an optimum (§5) |
| **3** | **Where is the profit concentrated — by ticket size, by region, by entry door?** Including whether a spot-only door is worth opening. | The model has one ticket per region and cannot see high-ticket customers at all. Acquisition strategy, agent commissions and the persona all hang on this. | **Profit contribution by ticket decile**, region and door |
| **4** | **How much do we need to raise?** Distribution of peak funding, and P(need > USD 3m). | USD 2.29m is one number built on ~90 point assumptions. | A **distribution**, with percentiles |
| **5** | **What does a gold drawdown do to the credit book?** | v2.6 limitation L10: gold is a level and a discrete shock, never a process, so the model *cannot* produce a probability. Charter item. The only tail-shaped risk in the design. 🔴 **Depends on the tier engine built for Q2** — liquidation risk is set by the LTV distribution, and LTV is a tier benefit (§5.2). | **Exceedance curves by LTV vintage** |
| **6** | **Which parameters actually decide questions 1–5?** | v3.0 withdrew per-parameter sensitivity by design and moved it here. | **Tornado** |

⚠ **What is deliberately NOT asked.** *"What is the optimal ICS discount?"* — see §5. *"What is the spot-to-SIP conversion rate?"* — a confirmed sourcing negative; the simulation returns the **break-even** conversion rate instead of guessing one.

---

## 3. Classification Summary

| Dimension | Choice | Plain English | Confidence |
|---|---|---|---|
| **Randomness** | **Stochastic** | Whether a customer pays this month, what gold does, whether a partner signs — none of it is knowable in advance, and the range matters more than the midpoint | **High** |
| **Entity** | **Hybrid** — agent-based on customers, aggregate on everything else | Customers differ in ticket, behaviour and entry door, and those differences are where the profit is. Vault fees and licence fees have no behaviour in them | **High** |
| **Time** | **Discrete, monthly, 84 steps** | The product settles monthly, the gate counts consecutive months, and the workbook's grid is monthly | **High** |
| **Approach** | **Monte Carlo, plus a solver layer** | Thousands of runs for the distributions; a search layer on top to answer the inversion questions | **High** |

🆕 **The solver layer is new at v2 and it is what makes questions 1–3 answerable.** Monte Carlo alone produces distributions of outcomes. Questions 1, 2 and 3 ask for the *input configurations* that produce a stated outcome, which is a search over the parameter space with a Monte Carlo evaluation at each point. Architecturally this is a wrapper around the same engine, not a second engine.

---

## 4. Classification Rationale

### 4.1 Randomness: Stochastic

**What this means:** rather than assuming the average customer pays 95% of months and saves USD 33.60, each simulated customer pays or doesn't, at their own ticket, and the aggregate is whatever falls out.

| Uncertain Variable | Why It's Unpredictable | Impact if Wrong |
|---|---|---|
| **Ticket size across the book** 🆕 | Modelled as a point. Real savings books are skewed, and this one is skewed by construction — floor USD 20, target USD 75, **40–60% at the floor** | Decides where profit sits, and therefore who to acquire. Compounds through credit limit, card spend and the ATM threshold |
| **Payment behaviour** (archetype mix, `S27`) | Confirmed sourcing negative — nothing decomposes a savings-lapse curve into behavioural types | Sets tier entitlement and therefore the ICS giveback cost |
| **Gold price** | A traded commodity, held flat in the workbook by design | Collateral value → credit limit → margin calls → AUM-linked revenue |
| **Acquisition arrivals** | Budget-driven point estimates, no launch data. The treadmill (7.52 gross adds per net add at Y7) makes the book highly sensitive | Drives everything |
| **B2B partner arrivals** | A straight line of 1→11. Enterprise deals are lumpy, binary and slow | **33–40% of revenue**, larger than the entire card business |
| **Redemption timing** | A smooth annual rate on AUM. Real redemptions cluster on shocks | Stream 0 is immaterial at Base and material exactly when cash is scarcest |

**Why not deterministic?** Phase 4 already is, and it is good at what it does. A second deterministic model produces a second single number to argue with the first.

⚠ **On v2.6's rejection of Monte Carlo** — *"wrong deliverable for a client Excel workbook, unauditable"* — that was correct, **and it was about the Excel.** The same brief: *"a revenue model that a client signs off on and a simulation that stress-tests it are different artefacts with different standards of evidence."* This is the second artefact.

---

### 4.2 Entity: Hybrid

| Entity | Count | Interchangeable? | Individual state matters? |
|---|---|---|---|
| **Customers** | ~200k ever-acquired by Y7 | **No.** Different ticket, different payment behaviour, different entry door, **different tier** | **Yes** — ticket drives credit limit and card spend; payment history drives tier; tier drives five benefit rates; **decision 6 caps each customer's payout at their own generated revenue**, which no aggregate can express |
| **Cards / credit lines** | ~36k live at Y7 | No — limit is a function of that holder's own accumulated grams **and their tier's LTV rung (50 / 65 / 80)** | **Yes.** Limit, drawn balance and LTV age with the holder, and **liquidation risk is a property of the vintage the loan was struck in and the tier it was struck at** |
| **B2B partners** | 11 by Y7 | **No.** Eleven arrivals cannot be a smooth curve | **Yes** — arrival timing, and whether won at all |
| **Vault, licences, insurance, audit** | One each | Yes | No. Fixed or step costs, no behaviour |
| **Partner end-users** | ~10m notional | Yes | No — only aggregate AUM matters |

🆕 **The deciding factor has changed, and there are now two of them.** In v1 it was the six-payment gate as a *access* test. With the gate demoted to discounts, the two factors that force agent-level representation are **(i) ticket heterogeneity** and **(ii) the tier ladder** — the tier mix cannot be computed from aggregates (§5.3), and every one of the five benefits reads it.

Taking ticket first, the non-linearities keyed to it:

| Mechanism | Why it breaks under an average |
|---|---|
| Credit limit = accumulated gold × LTV | A high-ticket customer crosses a *useful* limit years earlier |
| Card spend keyed to ticket as an income proxy | Spends more → more interchange and FX |
| Free ATM allowance is a hard AED 1,000 threshold | The brief already documents this as a Jensen error in miniature |
| KYC (USD 1.85) and card production (USD 4) are flat per head | Same cost, several times the revenue |
| **CAC is identical across tickets** (USD 85 UAE) | **LTV:CAC differs by an order of magnitude, and the model cannot see it** |

**Worked illustration.** Mean USD 33.60 with 50% of the book at the USD 20 floor forces the other half to average USD 47.20. If that half is skewed the way savings books are, **the top decile contributes ~30% of all contributions against the flat model's 10% — a 3× understatement**, before any of the effects above.

**Calibration, and why this is a fit rather than a guess.** Two corpus facts pin the distribution: the regional mean, and *"40 to 60% of the book sits at the floor."* Two constraints, two parameters. Dispersion **shape** is then swept low/medium/high; the direction of the result is robust, since dispersion always concentrates profit.

**Why not fully agent-based?** The VARA supervision fee gains nothing from an agent identity. ~60% of the workbook's cost rows are contractual or regulatory and stay as formulas over the aggregated population.

**Why not fully aggregate?** That is Phase 4, which states its own limits: *"no cohort resolution… no behavioural heterogeneity. One churn rate."*

---

### 4.3 Time: Discrete, monthly

| Event / Cycle | Frequency | Why It Matters |
|---|---|---|
| SIP collection | Monthly | The atomic event |
| The six-payment gate | Consecutive months | Run-length advances or resets monthly. **Now sets discount entitlement, not access** |
| Card settlement, interchange, ATM allowance | Monthly, allowance **not** rolling | Stream 4's ATM component is generated by a monthly threshold |
| Spot purchases | Ad hoc, ~1.7/yr | Sampled monthly as an arrival probability |
| Vault, licence, insurance, audit | Annual, charged monthly | Step costs, some with minimums that bite early |
| Gold price | Continuous in reality | Sampled monthly; the credit book is not margin-called intraday in this design |

**Recommended step: one month, 84 steps (M1 = January 2027)**, aggregated onto the workbook's **29-column grid** for every comparison.

**Why not event-driven?** Nothing arrives irregularly enough to justify it. If question 5 proves sensitive to sampling frequency, the price path alone can be refined inside a monthly step — a blueprint decision, not a classification one.

---

### 4.4 Approach: Monte Carlo + solver

**Two layers.**

**Layer 1 — Monte Carlo.** A few thousand runs, each with its own ticket draws, archetype mix, gold path, acquisition noise and partner arrivals. Produces questions 4, 5, 6.

**Layer 2 — the solver.** A search over inputs, evaluating Layer 1 at each point, answering *"what has to be true for X?"* Produces questions 1, 2, 3.

| Question | Search form |
|---|---|
| 1 — profitability threshold | Find the **boundary** in (book size × mix × cost base) where cumulative profit turns positive |
| 2 — ICS affordability | **Sweep** the four discount rates; report profit, margin and break-even year at each level |
| 3 — spot door | Find the **break-even spot→SIP conversion rate** at which a paid spot funnel beats spending the same money on SIP acquisition |

⚠ **The break-even-value pattern is deliberate and it recurs.** Where an input has no source — spot conversion, retention response — the simulation returns **the value at which the decision flips**, never a guessed point estimate. That converts an unanswerable question into a judgeable one, and into something an experiment can settle post-launch.

---

## 5. The ICS Giveback — the tier ladder, the sweep, and the trap

🆕 **Two directions taken 2026-09-02.** (a) **Do not model a relationship between discounts and retention** — discounts are carried as **pure cost** and swept. (b) 🔴 **Discounts must differ BY TIER.** There are **four benefit-bearing tiers** (Silver / Gold / Platinum / Sovereign) above the "No tier" standard.

### 5.1 It is twenty rates, not four

The workbook carries four blended discount rates. The mechanism design defines **five benefits across four tiers**. The corpus ladders already exist and are currently collapsed:

| # | Benefit | Family | Corpus ladder | In the workbook as |
|---|---|---|---|---|
| 1 | Entry-fee discount | Price | **1.5–2.0pp off base** at the top tier, stepped by tier | One blended 25% (`Scen!B109`) |
| 2 | **Credit LTV ladder** | Leverage | **50 / 65 / 80%** | 🔴 **Absent. Flat 0.50 — the bottom rung, for everyone** (`Assumptions!B31`) |
| 3 | Card tier | Service / waiver | **FX 2.0 / 1.5 / 1.0%**; ATM allowance rises with tier; issuance waived above base | One blended 20% (`Scen!B110`) |
| 4 | Gold Rewards rate | Payout | % of card revenue, **capped per customer at the revenue that customer generated** (decision 6) | One blended 5% of *aggregate* card revenue (`Scen!B111`) |
| 5 | Family / Digital Will | Price | **0 / 10 / 20 / 35 / 50%** by tier, plus a per-beneficiary discount from Platinum | One blended 20% (`Scen!B112`) |

Source: `_draft_ics-benefits.md` §0.1 and the `Assumptions` source notes.

### 5.2 Benefit 2 is missing, and it is the one that couples to question 5

**The LTV ladder is not a discount.** It gives *leverage*, not money back — a Sovereign borrows against 80% of their gold where a Silver borrows against 50%. It is therefore the only benefit that is **revenue-positive and risk-increasing simultaneously**: a larger limit means more drawdown, more lending revenue and more card spend, on a position materially closer to a margin call.

The workbook grants everyone the bottom rung, so it **understates both the revenue and the risk of the credit book.**

🔴 **This merges two questions that §2 lists separately.** Question 5 asks what share of the book is margin-called in a drawdown. That depends on the **LTV distribution**, which depends on the **tier mix**. **Question 5 is not answerable without the tier engine built for question 2.** They are one workstream.

### 5.3 Why the workbook blends, and why the simulation unblocks it

The blend was a deliberate client instruction, and the stated reason is exact:

> *"Client instruction 2026-08-26: model one blended discount on the qualifying population instead of splitting Silver / Gold / Platinum / Sovereign, **because no tier DISTRIBUTION exists in this model** — the ICS rows are binary, qualified or not — and **inventing one would put a fabricated mix underneath every benefit number.**"*

**That was the correct call for a spreadsheet that cannot compute a tier mix.** v3.0 §11 records the same limit: *"Tier mix is not computed. The model runs on a flat Gold rate throughout."*

**The simulation computes the tier mix as a by-product** — it carries each agent's payment history, so tier membership falls out rather than being asserted. ⚠ **This is not a reversal of the 26 August instruction. It is the condition the instruction was waiting on**, and the classification should be presented to the client that way.

### 5.4 Two consequences of the tier mix, expected before the run

**(a) Top-tier generosity is nearly free; bottom-tier generosity is where the money goes.** The ladder is steeply bottom-weighted — **Sovereign is ~1.2% of tiered accounts**, requiring a near-perfect record surviving to ~M61; Platinum requires gate+36. Most of the tiered book sits at Silver and Gold. A headline of *"Sovereign pays 3% instead of 5%"* therefore costs very little, while moving Silver by two points is expensive. **Implication: the ladder can probably be made substantially more generous at the top at the same total cost — a marketing asset currently unclaimed.**

**(b) A flat blended rate is wrong in a known direction, because the mix moves.** In Y1–Y2 no account has the tenure for Platinum, so the tiered population is almost entirely Silver. By Y6–Y7 the surviving book is heavily tenured and the mix is far richer. **A time-invariant blend therefore overstates the giveback in the early years and understates it in the late ones.** The early years are the loss-making, funding-hungry years, so this feeds directly into peak funding (question 4).

⚠ **A rough check supports the blend as a mature-book estimate, not as a constant.** Blending the family ladder (10 / 20 / 35 / 50 across the qualifying tiers) over a plausible mature mix lands near **20%** — the workbook's figure. The blend looks well chosen *for a mature book*; what it cannot do is be right in Y2 and Y7 at once.

### 5.5 How the sweep is parameterised — three dials, not twenty

Sweeping twenty independent rates produces a result nobody can act on. Sweep the **shape of the ladder**, which generates all twenty:

| Dial | Controls | Sweep |
|---|---|---|
| **Ceiling** | What the top tier receives | e.g. entry fee 1.0 / 1.5 / 2.0pp off base |
| **Steepness** | How much of the ceiling the lower tiers receive | Convex (generous only at the top — cheap) → linear → concave (generous early — expensive) |
| **Breadth** | Which of the five benefits are laddered at all | On / off per benefit |

Three interpretable dials, matching how the mechanism design already specifies the ladder — *"stepped, by tier"*, ceiling *"1.5 to 2.0 percentage points off the base."*

**Headline output: a cost matrix — what each tier costs, per benefit, per year.** That is the artefact that answers *"what can we afford."*

**One rule the agent model picks up for free.** Decision 6 caps each customer's Gold Rewards payout at the revenue **that customer** generated. The workbook applies a rate to *aggregate* card revenue and cannot express a per-head cap. In the simulation the cap binds for high-tier, low-spend customers — those who climbed the ladder on discipline rather than spending.

### 5.6 The trap, named so it is not misread

**Why no elasticity is modelled.** Closing the loop — discount → better continuity → more revenue → more affordable discount — requires a retention elasticity. **Nothing in the corpus, the market research or the comparables supplies one.** Modelling it would put an invented number under the client's largest discretionary spend.

🔴 **The consequence, stated plainly.** With discounts as pure cost and no benefit modelled, **the arithmetic will always show zero giveback as most profitable.** That is a tautology, not a finding.

**Therefore the output is an AFFORDABILITY ENVELOPE, never an optimum.** The permitted sentence is *"here is what each giveback level costs you and what survives it."* The forbidden sentence is *"the model recommends reducing ICS discounts."* ⚠ **This must appear in `SIMULATION_RESULTS.md` at the point the chart appears**, because it is exactly the line that gets lifted into a board deck without its qualifier.

**What would close the loop later:** a measured elasticity from the live app. Until then the affordability envelope is the honest half of the question, and it is the half the client asked for.

---

## 6. The Spot Door — rationale

🆕 **Direction taken 2026-09-02: build it in the simulation; decide on the Excel afterwards.**

**History that must not be lost.** The two-door architecture was fully specified at **v2.6 §5.9 (decision D35)** — *"one population, two doors, spot-only is the residual"* — and **deleted at v3.0 on 2026-08-21** on this economics: a spot-only buyer is worth `1.7 × ticket × 5%` a year, USD 16 in the UAE, against a USD 120 CAC — a 6–8 year payback, dominated by simply acquiring a SIP customer.

🔴 **That calculation priced a spot buyer on the entry fee alone, and the 2026-08-26 card decision invalidated it.** With card access open to everyone, a spot-only buyer also carries interchange, FX margin, ATM fees and issuance — roughly **USD 28 per active card per year** on the current book. That moves them from ~USD 16/yr to ~USD 44/yr and the payback from 6–8 years to under three. **The deletion was correct on 21 August and wrong by 26 August, and it has not been re-run.**

**Four reasons for one population with two doors, rather than two audiences:**

1. **They are the same people.** A UAE South Asian saver buying USD 190 of gold once is drawn from the same population as one committing USD 33.60/month. Two models double-count the market.
2. **The conversion arrow only exists inside one model.** The mechanism design calls spot *"the entry point for new investors"*; the brief calls the conversion rate *"the strategy question in numerical form."*
3. **The spot door roughly doubles the addressable base — 1.87×, already measured** (v3.0 §8). A spot purchase needs an *account*; a SIP needs a *standing mandate*. A large share of the target population holds a WPS payroll card with no IBAN — able to push once, unable to authorise a debit. **Today's model cannot see those people at all.**
4. **Different risk, not merely a different ticket.** A spot buyer carries **no persistency risk** — no mandate to lapse from — and **frequency risk** instead. A different failure mode, cheap to represent as a behaviour block inside the same agent framework.

**Relationship to §4.2.** The spot door is a *special case* of ticket heterogeneity — spot buyers are an observed instance of a high-ticket customer. **Ticket dispersion is the larger fix; the spot door rides on it.**

### 6.1 🔴 The payment-capability filter is wrong, and the spot argument is rebased

**Corrected 2026-09-02 on client-side challenge, then verified against `_draft_sip-rulebook.md`.** The rulebook's 2026-08-10 revision, recorded against Abdur, states: *"**UAEDDS direct debit is dropped entirely**: launch rails are **AANI Request to Pay** plus a **prefunded balance**, with AANI electronic direct debit adopted when live"*, and *"it deletes the mandate machinery. No mandate, no ceiling, no amendment flow."*

🔴 **The launch product has two push rails and no pull rail. The Phase 4 funnel filters the population on *"Payment capable (IBAN able to carry a mandate)"* at 0.57 — screening for a requirement the product removed three weeks before the funnel was built.** v2.6 §5.9 and v3.0 §8 both inherit it.

**Consequences:**

1. **The reachable SIP ceiling is understated, and the correct filter sits near the 0.857 Findex account-ownership anchor rather than 0.57.** ⚠ **This is a Phase 4 finding.** Cumulative-ever reaches 201,846 at Y7 against a 303,615 ceiling — **66.5% penetration, deep into the saturation brake** — so a higher ceiling materially changes the late-horizon curve.
2. ⚠ **The "1.87× widening" figure is withdrawn.** It was computed off the bad filter. **The spot door's justification is now the MONEY filter, not the payment filter:** a spot buyer needs *USD 190 once, when they have it*; a SIP customer needs *USD 20 every month, reliably*. That is the profile of irregular income, and it is a stronger argument than the IBAN one. **Revised widening ≈ 1.5×.**

### 6.2 🆕 Rail mix is a first-order driver of the gate — and Aurumix controls it

The rulebook distinguishes the two rails by friction, and carries a marketing rule enforcing the distinction: *"On Request to Pay, say **'one tap a month'** and mean it. **'Set and forget' may only be promised on the prefunded balance**."*

| Rail | Monthly customer action | Effect on a six-consecutive streak |
|---|---|---|
| **Request to Pay** | Taps to approve, every month | Twelve chances a year to forget |
| **Prefunded balance** | Loads once, draws automatically | Set and forget |

🔴 **This is the most consequential item in this document.** The archetype mix — the input nothing can source (§4.1) — is **substantially determined by rail mix, and rail mix is a lever Aurumix controls.** Therefore:

- **The payment-discipline sweep runs CONDITIONED ON RAIL**, not as one blended mix.
- **The adoption bridge becomes concrete and answerable:** *what share of the book do we move onto the prefunded balance, and what is each conversion worth?* Actionable in the onboarding flow, measurable once the app is live.
- **AANI electronic direct debit — announced, not live** — restores true pull collection when it lands. A scenario axis, not a guess.

### 6.3 ✅ The collection cost is ZERO — resolved at primary source, and the minimum-ticket problem dies with it

**Researched and settled 2026-09-02.** Aurumix banks with **Zand** (VARA-licensed for custody Dec 2024, CBUAE-regulated). Zand's published corporate schedule:

> **Local Inward Transfers — Free — Within Zand and Local Banks**

**A customer approving an Aani Request to Pay causes their own bank to push funds to Aurumix's Zand account — a local inward transfer, charged at nothing.** There is no per-collection fee and no percentage.

⚠ **Two earlier positions are withdrawn.** (a) The **AED 5 per item** in `_parked_collection-economics-and-minimum-ticket.md` is ENBD's **UAEDDS originator** price — a rail the SIP rulebook dropped on 2026-08-10; it was never the launch rail's price. (b) A ~1% ad valorem estimate from a payments vendor's comparison page is superseded by the bank's own schedule. **Al Etihad Payments sets no scheme fee** — *"fees will be determined by licensed financial institutions and payment service providers"* — so the bank's schedule is the governing document, and it charges zero.

✅ **THE MINIMUM-TICKET PROBLEM IS RESOLVED.** With a zero collection cost and the margin stack improved ~3× since the parked file (fabrication premium 3.00%→1.50% at D28; float cost of capital deleted at v3.0), **the USD 20 floor clears comfortably.** The parked file's headline — *"at the client's own target contribution the SIP loses money on every collection"* — **no longer holds at the target or at the floor.** `_parked_collection-economics-and-minimum-ticket.md` can be closed rather than reopened.

🔴 **But the mirror image is real, and it lands where there is no revenue.** Same schedule, next line:

> **Local Outward Transfers — AED 5 + CBUAE charges + VAT**

**Money going OUT costs ~USD 1.43 per payment, and the only routine outbound flow is a redemption** — the one transaction where **VARA forbids any fee whatsoever** (Annex 2 III.E.4).

| Redemption cost | Per event |
|---|---|
| **Modelled today** — Sumsub AML rescreening only, verified against `_calculated.xlsx` (USD 31,105.40 ÷ 16,813.73 events at Y7) | **USD 1.85** |
| **Missing: outward transfer** (AED 5 + VAT, CBUAE charges additional) | **+USD 1.43** |
| **Corrected** | **USD 3.28 — 77% higher** |

At Y7 (**16,814 events**) that is **~USD 24k** — **immaterial at base rates, which is the reassuring finding.** It scales in the **redemption-run** stress, when volume spikes against income that is zero by law.

⚠ **A workbook documentation defect found while verifying this.** `Model` row 250 annotates the line as *"USD 3.20 per event: Sumsub AML RE-SCREENING at 1.85 plus operational handling"*, but `Assumptions!B43` carries **1.85** and the cost row computes on 1.85. **The operational-handling component is described but not charged.** Either the note is stale or the cost is understated by a further USD 1.35; the note's own history (*"CUT TWICE, AND BOTH CUTS WERE DELIBERATE"*) suggests the value is right and the note was not updated. **Confirm before quoting either figure.**

⚠ **RtP origination fees: out of scope by client instruction 2026-09-02.** Carried at zero, not flagged.

**One capital note from the same schedule:** Zand requires an **AED 250,000 average monthly balance** (else AED 500 + VAT/month). Aurumix will exceed it on float, card prefunding and paid-up capital alone, so it does not bite — but it is a floor on operating cash and belongs in the capital block.

**Sources:** [Zand Fees & Charges](https://www.zand.ae/files/Zand-Fees-&-Charges.pdf); [Zand — VARA public register](https://www.vara.ae/en/licenses-and-register/public-register/zand-bank-pjsc/); [Al Etihad Payments — Aani Help](https://aep.ae/en/services/aani-help/).

**What survives of the prefunded-balance argument.** The cost leg is gone, but the **retention** leg stands untouched (§6.2): *"set and forget"* versus *"one tap a month"* is a persistence difference, and persistence is what the six-consecutive-payment gate measures. **The prefunded balance is a retention lever, not a cost lever.**

---

## 7. What This Means in Practice

### Build order — three stages, each standing alone

**Stage 1 — the population engine.** Agents with a ticket drawn from the fitted regional distribution, an archetype, an entry door, and a monthly pay/miss decision. The run-of-6 gate simulated as a first passage.

🔴 **VERIFICATION IS NOT VALIDATION, AND v2.6'S ANCHORS ARE ONLY GOOD FOR THE FIRST.** Corrected 2026-09-02 on client-side challenge. v2.6's 53.5% ever-gate and M8.1 mean arrival are **outputs of a Markov solve over the five archetype weights** — and that mix is the input the brief itself records as *"rank 1 load-bearing and a confirmed sourcing negative."* **Calibrating the simulation to reproduce them would prove only that it was fed the same assumption.** That is agreement, not evidence.

| | What it tests | Are v2.6's figures usable? |
|---|---|---|
| **Verification** | Feed the engine v2.6's exact archetype parameters; it must return 53.5% / M8.1 | **Yes — as a unit test on the first-passage arithmetic.** It says nothing about Aurumix |
| **Validation** | Does the real book behave this way? | **No.** Same unsourced input; it can only agree with itself |

**Verification targets — code-correctness tests only, never presented as findings:**

| Target | v2.6 figure |
|---|---|
| Mean gate arrival / ever-gate share, given v2.6's mix | M8.1 / 53.5% |
| P(ever gates), alternating misser | 24.0% |
| Holding-not-contributing at M61 | ~81% |
| Tier mix — Sovereign share of tiered accounts | ~1.2%; Gold from gate+12, Platinum from gate+36; alternating misser capped at Gold for life |
| 🆕 Ticket distribution | Mean reproduces the regional input; floor share lands in 40–60% |

**What is SWEPT rather than assumed.** The archetype mix, **and persistency itself** — the 55% is called *"the single most load-bearing input in the model"* and its validation file is absent from the repo (§10 item 8). Both become swept inputs; **gate share and mean arrival become outputs carrying a range**, e.g. *"across the plausible behaviour space, ever-tier share runs 38–62%."* ⚠ **Sweep wider than v2.6's three mixes** — those were fitted to hit three persistency targets and inherit the same sourcing problem.

✅ **The payoff is in the tornado.** If profit proves **insensitive** to the mix, the sourcing negative is harmless and we can say so with evidence rather than apologise for it. If it proves **sensitive**, we have located the highest-value experiment to run at launch and can specify it. Either result beats an unsourceable point estimate.

**Stage 2 — the full book.** Wrap Stage 1 in the revenue, cost, capital and float layers, ported from the workbook formula-for-formula. Add the gold price process and stochastic partner arrivals. Run Monte Carlo. Answers questions 4, 5, 6.

**Calibration check, once:** with every stochastic input pinned to its Base point value, Stage 2 must reproduce the workbook's 29-column output to within rounding. ⚠ **This is a test that the port is faithful — it is not a constraint on the assumptions.** Once it passes, every parameter is free to move, and moving them is the work.

**Stage 3 — the solver.** The search layer over Stage 2. Answers questions 1, 2, 3 — the profitability threshold, the ICS affordability envelope, and the profit-concentration and spot-door findings.

### For the project team

- Results arrive as ranges, thresholds and menus. *"Peak funding is USD 2.29m"* becomes *"USD 2.3m is the middle; a 1-in-5 outcome needs USD 3.4m."*
- Where the simulation disagrees with the workbook, the calibration check decides which to trust: if the pinned run reproduces Excel and the stochastic run does not, the gap **is** the value of the heterogeneity.
- 🆕 **"Churn" is reported per behaviour, not as one number.** Stopping a SIP, letting the card go dormant, repaying the credit line and redeeming the gold are four separate events on four clocks (§10 item 4). Expect this to show **SIP lapse costing less revenue than the current model implies**, because the card keeps earning after the mandate stops.
- One client decision remains open and is carried as a switch, **run and reported both ways**: *prepaid or credit*.

### Compared to the revenue model

The workbook answers *"what does this business look like if our assumptions hold?"*, is auditable cell by cell, and is the artefact the client signs. The simulation answers *"what has to be true for this to work, and how much room is there?"* It is not auditable cell by cell and must never be presented as though it were. **The workbook is the centre case; the simulation is the boundary, the tail, and the affordability envelope.**

---

## 8. Comparable Architectures

⚠ **No gold-token issuer publishes a simulation architecture.** Recorded as a confirmed negative, consistent with the registry-first method of Phase 1 — the 19 protocols in `Aurumix_Protocol_Landscape.md` disclose reserves and audits, never models. The analogues below come from the three domains this product actually is.

| Domain | Why it is the right analogue | Architecture there | Lesson carried across |
|---|---|---|---|
| **Life-insurance persistency modelling** | The closest analogue to a SIP with a lapse curve, and the client's agent network is built on the Indian insurance agency model | Cohort survival with heterogeneous lapse; mover-stayer mixtures | The archetype split **is** a mover-stayer mixture; v2.6 reached it independently |
| **Credit-card portfolio models** | Streams 2, 4 and 5 are a card programme | Agent-level, monthly, Monte Carlo on spend and utilisation | Spend, ticket and utilisation are **correlated**. Drawing them independently understates the tails |
| **Collateralised-lending liquidation models** | Question 5 exactly | Stochastic price path against per-position LTV vintages | Liquidation risk is a property of **when a position was struck**, not of the average LTV |

---

## 9. Alternative Considered

**Refine the deterministic engine instead — more archetypes, ticket bands rather than a distribution, finer curves, no randomness.**

Genuine merit, and not a straw man. Phase 4 is deterministic on purpose; determinism is why the client can audit it. v2.6's D25 in fact *had* two ticket bands per region, which v3.0 collapsed — so restoring bands would be a return to something that already existed and would capture part of §4.2's argument.

**Rejected on two grounds.** First, questions 1 and 2 are **searches over a parameter space**, and a hand-built deterministic sheet cannot search — you would be re-running the workbook by hand hundreds of times and reading off a boundary. Second, questions 4 and 5 are probability questions that no deterministic engine produces at any resolution.

**What is kept from it:** the deterministic engine is not discarded. Stage 1's validation gate *is* its answer; Stage 2's calibration check *is* the workbook. Both remain the reference the stochastic model must reproduce before it is permitted to disagree with anything.

---

## 10. Carried Into the Blueprint

| # | Item | Status |
|---|---|---|
| 1 | ✅ **Fabrication premium — SETTLED 2026-09-02.** Aurumix bears it as a cost; the customer pays 5% and that is the ceiling. Matches `Scenario Parameters!B132`. **v3.0 brief §3.3 contradicts this and must be corrected** | Settled; doc fix owed |
| 2 | 🔴 **v3.0 brief §3.1 is withdrawn by the 2026-08-26 card decision.** The card no longer requires the gate. The brief still says it does | Correction owed |
| 3 | **Stream 4 exceeds Stream 2**, inverting v2.6's ordering. Open question in brief §10 — does the programme-manager share apply to gross? | Open, client |
| 4 | ✅ **"Does a lapsed customer keep the card?" — RESOLVED 2026-09-02, and the switch is deleted.** Client-side framing: *"it may be churn of a feature rather than of the platform."* Correct. The workbook collapses several independent behaviours into one churn rate and then patches it with a binary switch worth ~42% of terminal revenue. **Agents now carry independent states — SIP active/lapsed, card active/dormant, credit drawn/not, gold held/redeemed** — each on its own clock. Churn is reported per behaviour. **Card dormancy is genuinely sourceable** from card-industry data, unlike most behavioural inputs here | Structural change; supersedes the switch |
| 5 | **Stream 6 has no behavioural content** — a straight line to 11 partners carrying a third of revenue. Expect this to widen the funding distribution more than any customer-side input | To model as discrete arrivals |
| 6 | **Ticket distribution shape** has no direct source; fitted from mean + floor share, then swept | Method agreed, values to fit |
| 6a | 🔴 **The credit LTV ladder (50 / 65 / 80) is absent from the workbook** — flat 0.50 for everyone. It is benefit 2 of five, it is revenue-positive and risk-increasing, and it is the link between questions 2 and 5 | To build; carry back to Excel if material |
| 6b | **The blended ICS rates are time-invariant**, so they are wrong early and roughly right late (§5.4b). Direction known, magnitude not | Quantify in Stage 3 |
| 6c | ⚠ **`_draft_ics-benefits.md` is written against seven tiers** and owes a tier-count pass to five. §3.1's card mapping and 4-level variant are moot | Pre-existing Phase 2 debt; blueprint must use the five-tier ladder |
| 6d | ✅ **Entry-fee base rate — SETTLED 2026-09-02: flat 5% throughout.** Decision 9's declining base (5→4→3%) does not apply; only ICS tiers discount off it | Settled |
| 6e | 🔴 **The payment-capability filter (0.57, "IBAN able to carry a mandate") contradicts the SIP rulebook's 2026-08-10 rail decision.** Understates the reachable ceiling; saturation is biting at 66% penetration, so it moves the curve | **Phase 4 finding.** Rebase on the AANI Request to Pay / prefunded-balance rails (§6.1) |
| 6f | ✅ **Collection cost RESOLVED AT ZERO** (§6.3). Zand: local inward transfers free. **The minimum-ticket problem is closed and the parked file can be retired.** ⚠ **But redemption cost is understated: USD 1.85 → USD 3.28** per event (+77%, ~USD 24k at Y7), on the one flow VARA forbids charging for | **Phase 4 finding.** Correct the redemption unit cost; delete the rail-cost sweep |
| 6h | ⚠ **`Model` row 250 documents USD 3.20 per redemption but the model charges USD 1.85.** The "operational handling" component is described and not charged | **Phase 4 finding.** Reconcile the note to the value, or the value to the note |
| 6i | ⚠ **The ICS entry-fee discount should apply to SPOT purchases too.** Benefit 1 covers *"every purchase, spot included"* (benefits doc §0.1, citing rulebook §1.1) — spot **earns** no score, but a scored customer still **spends** their tier on it. `Assumptions!B207` restricts it to stream 1a, **understating the giveback** | **Phase 4 finding.** Extend the discount to stream 1b |
| 6k | ⚠ **`Assumptions!B14` "Interchange – Gold 1.8%" is a Visa UAE PLATINUM rate.** Visa UAE IRF eff. 19 Dec 2024 (primary): Gold 1.15%, Platinum 1.80%. Immaterial to profit (stream 2 is ~$56k at Y7) but the label is wrong, and the tier ladder's card-product mapping should carry 1.15 / 1.80 / 2.05 by rung | **Phase 4 finding.** Relabel or reprice |
| 6j | ✅ **Tier-timing discrepancy RESOLVED, no client input needed.** v2.6's `months-since-gate` lookup (Gold at gate+12) put every rung ~6 months late against the rulebook's ladder. **The simulation implements the real formula** — `min(Record, Standing) × Retention`, thresholds 25/50/75/100 — which reproduces the stated M6/M12/M36/M60 schedule exactly. The lookup was an Excel workaround with no reason to survive into an agent model | Closed |
| 6g | 🆕 **Rail mix (Request to Pay vs prefunded balance) drives payment discipline and is client-controlled.** The archetype sweep must be conditioned on rail | Core to the adoption-bridge answer (§6.2) |
| 7 | **The charter's Phase 4 wishlist is half-retired** — spot capacity vs secondary premium, and dividend concentration, belong to the dead V3 pricing formula. Gold GBM and the liquidation cascade survive | Charter anticipates this |
| 8 | `reference_model/VALIDATION.md` **is not in the working tree**, so the persistency anchors cannot be evidenced on request | ⚠ **Not fixable by reproduction** (§7). Persistency is **swept**, and the tornado reports whether the missing source matters |

---

**Next step:** review. On agreement, step 2 is `Aurumix_Simulation_Blueprint.md` — agents, state, decision rules, the ticket-distribution fit, **the five-tier benefit ladder and its three sweep dials**, stochastic processes, the solver specification, invariants and build sequence. **No code before the blueprint is agreed.**
