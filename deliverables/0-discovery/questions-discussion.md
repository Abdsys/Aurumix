# Aurumix — Questions & Discussion Points

> **Questions** = clarifications we need directly from the client/founders (a definite answer resolves it).
> **Discussion Points** = items that need design, research, or strategic analysis on our side — usually with a recommendation — not a one-line answer.

> **Status:** answers below come from two sources: (a) the client's written replies in `Aurumix reply .docx` (red-marked text), and (b) the client call on **2026-07-24**. Each question is tagged:
> **[ANSWERED]** resolved by client · **[OURS]** client handed the decision to us · **[OPEN]** still needs client input.
>
> **Last updated:** 2026-07-24

---

## Status at a glance

| # | Question | Status |
|---|---|---|
| 1 | SIP amount, lock granularity | ANSWERED |
| 2 | Missed SIP participation | ANSWERED |
| 3 | Token denomination | OURS |
| 4 | ICS scoring weights | ANSWERED (priority) + OURS (formula) |
| 5 | Agent network commission | OURS (deferred to revenue model) |
| 6 | ICS spot lane eligibility | ANSWERED (partial) |
| 7 | Pledged gold earning ICS | ANSWERED |
| 8 | Mining Events goal | ANSWERED (substance) + OURS (framing) |
| 9 | Custody fee accrual vs peg | OURS |
| 10 | Sovereign credit 110% | ANSWERED |
| 11 | Dividend as recycled fees | ANSWERED (acknowledged) + OURS (fix) |
| 12 | Lock-in double count | ANSWERED |
| 13 | Physical redemption | ANSWERED |
| 14 | Voice of customer / objectives | **OPEN** |
| 15 | Current project stage | ANSWERED |

---

## Questions (clarify with client)

### 1. SIP amount and lock granularity — **[ANSWERED]**

*$75 a month is just the target investment right? Minimum is $20 and max is not capped. Is this amount going to be fixed each month or is it upto the investor? Does each monthly purchase start its own 6-month lock, or does one lock cover the whole SIP?*

**Client answer:**
- **$75 = target average** contribution per investor, not a fixed figure. **$20 = minimum.** **No maximum cap.**
- **The monthly amount is not fixed.** An investor can contribute any amount in any month, but the amount and consistency feed the ICS score.
- **The "lock" is a contribution commitment, not a token lock.** If a user selects a 6 month lock, they are committing to pay the SIP in each of those 6 months. One commitment covers the whole SIP period; individual monthly purchases do not each start their own lock.
- **Missing a payment is not forced or penalised financially.** The user simply loses ICS score. The purpose of the lock is behavioural consistency, explicitly modelled on Indian life and health insurance premium schedules.
- A **minimum timeline is mandatory**; the **maximum is chosen by the investor** at the time of investment, and **longer commitments carry more benefits**.
- There are **two investment types**: SIP and spot. Spot tokens are immediately sellable. Spot capacity opens monthly in proportion to SIP funds received that month, with preference to higher ICS tiers.

**Supporting precedent (researched 2026-07-24, Perplexity Sonar):**
The Indian analogy splits two ways, and Aurumix is deliberately taking one half of each:

- **Insurance (life and health):** persistency is enforced. IRDAI sets a grace period of 15 days for monthly mode and 30 days for yearly, half-yearly and quarterly modes; health insurance commonly uses 30 days. Pay within the grace period and cover continues, normally without penalty. Miss it and the policy **lapses** or is treated as discontinued, and **persistency-linked benefits such as no-claim bonus and loyalty additions are reduced or forfeited**. A lapsed policy can be revived within the insurer's revival window by paying overdue premiums plus interest, subject to insurer acceptance.
- **Mutual fund SIP:** the opposite. An SIP is a standing instruction, not a contract with a grace period. A missed installment is simply **skipped**; the SIP continues on future dates. There is **no lapse, no paid-up status, no revival, and no forfeiture of benefits**. The only cost is fewer units bought and disrupted rupee cost averaging.

**Design implication:** Aurumix uses the **SIP wrapper** (familiar, low friction, no forced payment) but bolts on the **insurance persistency penalty** (ICS decay on missed contributions). That is a coherent hybrid and it will read as familiar to the Indian target audience. It also gives us a clean design question for the ICS build: does Aurumix need a **grace period** and a **revival mechanic** (pay in arrears to restore lost ICS), both of which the insurance precedent supports and which would soften churn.

---

### 2. Missed SIP participation and orphaned allocation — **[ANSWERED]**

*What happens if the SIP investors commit the allocation but dont participate? Where does that allocation go?*

**Client answer:**
- **There is no collective fixed SIP date.** SIPs can arrive any day of the month. Because contributions are not synchronised, there is no shared allocation pool for SIP that can be orphaned.
- Missing a contribution changes **only the ICS score and everything attached to it** (allocation priority, spot access, credit ratio, dividend share). The commercial job is to make ICS attractive enough that people do not want to miss.
- **The spot event is different.** It runs on a **fixed date**, and the **spot cap is set as a percentage of the month's total new investment**.

---

### 3. Token denomination / measurement — **[OURS]**

*Are we sure/flexible on the token measurement, i understand its done to make it look accessible (the token count climbing) but it makes the calculation a bit confusing for the comms and customer. 1 token = 1 gram is clean.*

**Client answer:** *"We want to make it less than a gram. The basic thought process is how will we make the token in points; a gram can be in points, but a token in point percentage. We are open to your suggestion."*

**Confirmed on the call:** **fully ours to recommend.** The decision stays open and we will resolve it in an upcoming deliverable.

**Tension to resolve:** the written reply pushes for a **sub-gram** unit (current V3 spec: 1 AURX = 0.01 g) on accessibility grounds, but on the call **CG suggested 10 gram units as more practical for the Indian market** than ounces. These are not necessarily in conflict (one may refer to the token unit and the other to the retail quoting or purchase convention), but the two need reconciling explicitly rather than assumed.

**Our position going in:** keep a sub-gram unit, because the accessibility psychology is real and peer evidence supports it (PAXG's 1 oz unit visibly hurts retail optics; Kinesis uses 1 KAU = 1 g). Size it so the arithmetic stays clean. The 0.01 g vs 0.001 g trade-off, and the interaction with a 10 g retail quoting convention, goes in the B1 (Token Architecture) write-up.

**Related:** Tony raised a **PAXG-style burn mechanism** as a thought experiment on the call: reducing supply while holding the same gold backing would raise value per token over time. This interacts directly with the denomination decision and with the custody fee question (#9), since a burn is one way to settle fees without breaking the peg arithmetic. To be assessed together.

---

### 4. ICS scoring weights and calculation — **[ANSWERED]** (priority) + **[OURS]** (formula)

*I am assuming we have to work on the ICS scoring thoroughly as a lot of the perks like (credit and dividends) depend on it. As of now we have the tiers and components that would define the ICS score but exact calculation of the score still has to be done. Of all the ICS inputs (continuity, lock-in, tenure, value, referrals, Masterclass, family) do we have any preference of weighting among each factor? Like whats more preferred vs whats less*

**Client answer — stated priority order:**
1. **Longer lock-in timeline** and **continuous investment** (joint top two)
2. **Referrals**
3. **Family plans**

Remaining components (tenure, value, Masterclass) exist but rank below these. The client confirmed the **exact calculation still has to be done**.

**Confirmed on the call:** the **ICS formula is fully ours to build, with no further constraints**. We keep their priority order as the anchor.

**Scope of the build:** score range, component weights, tier thresholds (7 tiers, Green to Sovereign), **decay rate on missed SIP contributions**, caps to prevent any single component dominating, and any grace/revival mechanic (see #1). This is now load-bearing for four things: allocation priority, spot access, credit ratio, and dividend share. After the Dividend Multiplier was dropped (#12), ICS carries the dividend weighting on its own, which raises the calibration stakes.

---

### 5. Agent network commission and split — **[OURS]** (deferred to revenue model)

*What percentage of revenue goes to the agent network, and how is it split across the 3 levels? Need to clear this because usually agent commissions are tied to the value of investors they bring. We can have a direct share from the initial fee for agents instead of the whole revenue line.*

**Client answer:** agreed in principle that agents can take **a direct share of the entry fee rather than the whole revenue line**, then made it conditional: *"Step 1 to this answer is the revenue model of our complete product."* They want the full revenue model, fee structure, fixed costs and net profit before setting agent economics.

**Clarified on the call:** the **percentages are not defined yet**. The client's actual goal with this question was to have us **understand the agent system**, which is modelled on the **Indian insurance agent network** and on **mutual fund advisors / wealth managers**.

**From the meeting:**
- **Three layer agent hierarchy.** Advisors onboard clients and invest **on their behalf**, but advisors **cannot withdraw or sell tokens** from the platform. This is an important control: the agent holds the relationship, not the assets.
- Target channel is Indian **financial advisors and wealth managers**, who already intermediate a significant share of Indian retail investment.
- Tony flagged, from a comparable medical provider system, that **maintaining the customer relationship and a consistent payment schedule is what reduces churn** as the base scales.
- Tony proposed a **forward option: replace human advisors with AI agents**, eliminating commission leakage and retaining more value in the platform. Logged as a future consideration, not a current design input.

**Client ask attached to this:** they want to see **our silver-based product's revenue model and forecast** as a calibration reference, including the debit card revenue line and fixed costs down to net profit. Their stated target: work out **what share of net profit is required to deliver a 2 to 3 percent uplift on the gold return for the top 10 to 15 percent of investors**.
> ⚠ Not yet confirmed whether we are actually sharing the silver model, or only using it internally to inform our recommendation. **Needs a decision on our side.**

**Supporting research (2026-07-24, Perplexity Sonar) — Indian life agency structure:**
- **Hierarchy:** LIC runs Central Office → Zonal (8) → Divisional (~113) → Branch (~2,048) → Agents, with **Development Officers** as the field supervisory layer above agents. Agents are not on payroll. Private insurers use agency managers rather than the DO title, but the same IRDAI commission rules apply to all insurers.
- **Front-loaded plus trailing split:** higher **first year commission**, lower **renewal commission**, and renewal is payable **only while the policy stays in force**. Agent income is therefore tied to persistency, not to the one-off sale.
- **Upline override:** Development Officers earn **overriding commission** on business written by the agents they recruited, and club/status progression is judged on the team's aggregate **including renewal business**.
- **Regulatory caps:** the **IRDAI (Payment of Commission) Regulations, 2023** set insurer-wide caps by product category, explicitly designed to stop excessive upfront payout and to force long-term persistency.

**How this maps to Aurumix:** agent earns a share of the **entry fee** (first year equivalent) plus a **trailing share tied to the investor's continued SIP contributions** (renewal equivalent, which dies if the investor stops contributing). The three tiers are the override layer, capped. This solves the anti-MLM problem **structurally rather than by decree**: if trailing income depends on downline investors actually continuing to contribute, recruitment for its own sake stops paying.

> ⚠ **Sourcing caveat:** Sonar confirmed the *structure* but explicitly could **not** retrieve the IRDAI 2023 percentage tables or the statutory override caps. Pull the regulation text directly before citing any figures.

---

### 6. ICS spot lane eligibility — **[ANSWERED]** (partial)

*Is ICS Spot Lane eligibility the same as Confirmed SIP status (6 consecutive events), or a separate higher ICS threshold? The doc seems to use both but its not clear if they are the same gate. If they are different, what ICS level makes someone spot-eligible?*

**Client answer:** *"Spot buyers don't get any ICS points."*

**Reading:** this resolves the direction of causation but not the threshold. Spot access is **gated by ICS tier** (preference goes to higher tiers), while **spot purchases themselves earn no ICS**. So ICS is earned through SIP behaviour and spent on spot access; it is not a loop.

**Still to define:** the precise threshold, and whether it is identical to Confirmed SIP status (6 consecutive events) or a separate higher bar. This falls inside the **ICS formula build (#4)** and is ours to specify.

---

### 7. Pledged gold and ICS/dividend accrual — **[ANSWERED]**

*Does pledged gold still earn ICS and dividend while it is encumbered as credit collateral?*

**Client answer:** **Yes.** Pledged gold continues to earn ICS. Pledging makes no difference, and the client's view is that pledgers should arguably get **more** advantage, because pledging means longer retention and the credit line generates additional revenue.

---

### 8. Goal of the Mining Events — **[ANSWERED]** (substance) + **[OURS]** (framing)

*Since the token price is now purely gold, buying at one event vs. the next gets gold at the same day's price either way, and every confirmed SIP investor is guaranteed their allocation. So is the "oversubscription / mining" framing now just a retention/FOMO device rather than a real economic mechanism? Should we keep the heavy mining framing or simplify to "gold DCA + tier-earned spot access"? Also we will be limiting our AUM/market cap growth in a way because we are limiting oversubscription.*

**Client answer:** the client engaged the consequence rather than the framing, and confirmed **the scarcity is intentional and is the core of the design**:
- Restricting supply is expected to produce a **3 to 8 percent premium on exchanges**, which is what keeps both the spot market and SIP demand alive. Investors buying at base rate in spot gain that advantage.
- They accept the **downside**: AUM and market cap growth are throttled, and **institutional investors are restricted** by the limited monthly spot capacity, which also gives preference to SIP investors.
- Premium drivers they cite: the credit facility, and the dividend paid to the top 10 to 20 percent of investors funded from 15 to 20 percent of total profit from commission and the credit card business. Money earned from 100 percent of users flows to roughly 10 to 20 percent, which they consider the core incentive.

**Allocation math, now reconciled (call, 2026-07-24).** The percentages that previously did not sum were **nested denominators**, and the figures are **not yet final**:

```
Month's total SIP inflow (100%)
   └─ Spot capacity = 20–40% of SIP inflow      [range, not final]
         ├─ 80% → ICS spot lane (tier-gated)
         └─ 20% → external spot lane
```

So the **external spot lane is only 4 to 8 percent of monthly SIP inflow**, and the **ICS spot lane is 16 to 32 percent**. That tight external allocation is precisely the lever generating the intended exchange premium, and equally the constraint on institutional participation the client flagged as the downside.

**The 20 to 40 percent figure is the headline tunable parameter** for later simulation: it trades AUM growth directly against secondary market premium.

**Framing decision:** ours to recommend, and the client is **open to dropping the "mining" language entirely** if we make the case. Our leaning: keep the mechanic, since it is load-bearing, but drop the mining metaphor, which implies a proof-of-work or emissions story that a 100 percent gold token does not have and which invites the wrong regulatory reading.

**From the meeting:**
- **Abdur** argued for allowing continuous uncapped gold purchases to maximise market cap, since more market cap increases monetisation through issuance, trading velocity and credit card revenue.
- **Tony** advised balancing reserves as **inventory**: gold should neither sit idle nor be insufficient to fill orders. Apply lean principles, predict demand, hold optimal reserves.
- **Abdur flagged a regulatory constraint: the premium cannot be predetermined.** It must be market driven, or it hands regulators a security characteristic. This constrains how we are allowed to *market* the 3 to 8 percent expectation.
- **CG's three premium drivers:** the cost of obtaining locked tokens, limited availability tied to monthly SIP inputs, and utility features (gold ownership plus future credit access).
- Tony proposed a **subscription / pre-allocation model** for a month-long token sale event: investors pre-commit funds in advance and receive allocation proportional to their contribution. This makes demand predictable and prevents running out of tokens, mirroring a guaranteed SIP. **CG's concern:** how this reconciles with the current model where spot investors may not receive full allocation.
- **Excess subscription handling** discussed: refund a portion (example given: $250,000) and redirect those investors into the SIP at better pricing.

---

### 9. Custody fee accrual vs the peg — **[OURS]**

*Custody and management fees in actual funds don't work on a snapshot. They accrue daily on the balance held that day, then settle periodically. Each day, accrue 1%/365 of that day's grams. Settle the accrued total at the anniversary (or at transfer/redemption, whichever comes first). However in the case of gold tokens its different because the peg may get affected.*

**Client answer:** the client bounced this back to us, asking how our **silver-based token** handled the same problem: *"Will be helpful to conclude."*

**Confirmed on the call:** **ours to recommend**, to be solved in an upcoming deliverable.

**Our position (carried from prior analysis):**
- The custody fee must **not** be deducted in grams, which is the current V3 design. Peg = grams ÷ tokens, so removing grams mechanically drops the ratio and breaks the 1 AURX = fixed-grams promise.
- Charge the fee **in cash**, skimmed from SIP inflow and at entry/redemption gates, never touching the gold. This keeps the peg exact (the PAXG and XAUT approach) and removes secondary-market fee leakage. **Accrue daily, settle cash periodically.**
- Secondary point: **custody fee is cost recovery, not revenue.** Only the spread above true custodian cost is margin. Booking gross custody as profit inflates the dividend, which is paid from "operating profit", and that is a VARA and audit red flag.
- **Alternative to assess:** the PAXG-style **burn mechanism** Tony raised (see #3) as a non-cash settlement route.

**Also pending:** CG agreed to share **Google Drive access** containing the **differential fee structure for spot vs SIP** investments. Needed before we finalise fee design.

---

### 10. Sovereign credit tier at 110% LTV — **[ANSWERED]**

*Sovereign credit category is 110% of gold value, lending more than the collateral is unusual, we need to make sinks to cover the shortfall. Whats is the thinking here?*

**Client answer:** *"90-95% is max it goes, not 110%."*

**Action:** the V3 document's 110 percent figure is **incorrect and should be corrected to a 90 to 95 percent ceiling**. This removes the undercollateralisation problem entirely, so no shortfall sink is required. LTV warning and liquidation thresholds still need setting relative to the new ceiling (currently 80 percent warning / 100 percent liquidation, which no longer sit sensibly around a 90 to 95 percent max and must be re-spaced).

---

### 11. Dividend funded by recycled fees — **[ANSWERED]** (acknowledged) + **[OURS]** (fix)

*The dividend is paid from operating profit, but that profit is just the fees investors pay (entry, custody, credit). Also now there is no external yield source, so is the ICS Dividend actual value creation or just investors' own fees recycled back to them and concentrated into the top 10%? This needs to be thought through and we need to add more revenue streams, probably designed around product features.*

**Client answer:** the client **accepted the critique as accurate**: *"As of now what you are saying above is true. It's what we earn from the investors. Since we are not using their money to do any other business, which also is not legal to do."* They then asked us directly for **more revenue options**, noting that current streams are entry fee, annual fee, custody and credit card, and adding that **credit card income also comes from the retail/merchant side** (interchange charged to retailers), which is genuinely external.

**Confirmed on the call:** **ours to recommend**, in upcoming deliverables.

**Our direction:**
- The core problem is that a dividend funded purely by investor fees is both a **weak value story** and a **securities classification risk**, since a profit share tied to enterprise performance looks like a security.
- **Market research surfaced the answer:** the Dubai peer **ORO** funds real gold yield via **Monetary Metals**, a gold leasing partner that pays interest on gold, in gold. That is genuine external yield on the asset, not recycled fees, and it can be framed as **asset yield rather than enterprise profit share**, which is the compliant framing.
- **Trade-off:** leasing encumbers the gold, denting the "100 percent allocated and unencumbered" claim. Needs caps, disclosure and active risk management.
- **Merchant interchange** is the one existing stream that is genuinely externally funded and should be emphasised accordingly.

---

### 12. Lock-in double count in the dividend — **[ANSWERED]**

*Lock-in duration appears to affect the dividend twice (double dependency). It is a component of the ICS score, and it also sets the standalone Dividend Multiplier, and the ICS-Weighted Score = ICS Score × Investment Value × Dividend Multiplier. So lock-in is counted once inside ICS and again as the multiplier on top — a compounding (lock-in²) effect that can let long lock-ins dominate the 80/20 pool over the stated "primary driver" of continuity. Is this an intentional super-weighting of long lock-ins, or an unintended double-count?*

**Client answer (confirmed on the call):** **unintended. Drop the standalone Dividend Multiplier.**

**Resolved formula:**

```
ICS-Weighted Score = ICS Score × Investment Value
```

Lock-in now lives in exactly **one** channel, as a component inside the ICS score. This removes the compounding effect, preserves **continuity as the genuine primary driver**, and makes the top 10 percent pool materially easier to calibrate and simulate.

---

### 13. Physical redemption of gold — **[ANSWERED]**

*Physical redemption isn't mentioned anywhere — the only exit is the cash buyback (net grams × LBMA price, in USDT/AED). Is physical delivery intentionally excluded, or should we offer it (e.g. for higher tiers / above a minimum gram threshold)? Peers like PAXG and Kinesis allow it, and we market hard on "you own physical gold."*

**Client answer:** **intentionally excluded.** *"We need to exclude. We want longer lock in and hold the money and give credit. We are giving buyback so no need physical delivery."*

**Note for us:** this is a deliberate commercial choice (retention and credit revenue over optionality), but it creates a **marketing and compliance tension** with the "you own physical gold" positioning, since peers offering redemption use exactly that to substantiate the claim. The messaging needs care: the gold is allocated and audited, but not deliverable. Flag for the compliance layer of the MD.

---

### 14. Voice of customer / engagement objectives — **[OPEN]**

*What are your objectives with this engagement in specific and the project in general?*

**Client answer:** *"Didn't get you."* The question was not understood in writing, and it **was not covered in the 2026-07-24 call either** (confirmed against the meeting summary, which records our deliverables but never their objectives).

**Why it matters:** this sets what the MD optimises for. The plausible objectives pull in materially different directions:
- a **VARA-approvable design** (optimise for classification safety),
- an **investor raise document** (optimise for narrative and returns),
- a **build spec** for the September app (optimise for technical precision),
- **credibility for partnerships** (optimise for external validation).

The only indirect signal is that Tony framed the deliverable as an **investor-grade model with sensitivity scenarios**, but that is our framing rather than their stated goal.

**Action: ask directly on the Wednesday call**, phrased concretely rather than as "objectives" (which did not land). Suggested phrasing: *"When this Data Room is finished, what is the first thing you will do with it, and who is the first person outside your team who will read it?"*

---

### 15. Current project stage — **[ANSWERED]**

*What's the current standing with the idea, in terms of what's built, what integrations, etc. Is there a legal advisor on board?*

**Client answer:**
- **Legal:** in talks with a **legal team in Dubai**, who are also handling **VARA compliance**.
- **Build:** design work and **front-end app development expected complete by early September**.
- **Then:** API integration and various back-end partnerships.

---

## Discussion Points (design / research / strategy)

### 1. Credit facility structure and risk engine

Is the credit revolving (like a card) or a fixed-term loan? Is there a repayment deadline? The credit system needs to be thought through end to end: LTV, liquidation thresholds, credit extension types, and how lending partners offer it.

**Updated by client input:**
- Maximum LTV is **90 to 95 percent**, not 110 percent (see Q10). Warning and liquidation thresholds must be re-spaced around this ceiling.
- **Pledged gold continues to earn ICS and dividend** (see Q7), and the client wants pledgers *advantaged*, since pledging drives retention and credit revenue.
- Credit is one of the three stated **premium drivers** (see Q8) and one of the four things ICS governs.

### 2. AURX classification

We need to research and establish how AURX gets classified (commodity, security, fund, and so on), which determines the structure and our opinion on secondary market trading.

**Sharpened by client input:**
- The **gold core is a clean ARVA under VARA** (retail friendly). The **ICS Dividend and the credit facility are what push it toward HYBRID**, risking dual regulation (VARA plus CMA securities plus a lending regime), which fights the mass-retail model.
- Working direction: keep the **token** pure gold, and deliver **dividend and credit off-token via licensed structures**.
- The **external gold yield route** (Q11) supports this, because asset yield is a materially safer framing than enterprise profit share.
- **Constraint identified on the call:** the **3 to 8 percent premium cannot be predetermined or promised**. It must be market driven, otherwise it hands regulators a security characteristic. This limits how we may market it.
- Token standard implication: fee, KYC, credit, dividend and buyback rights all fail to survive a permissionless ERC-20 DEX transfer, arguing for a **permissioned base (ERC-3643)** plus an optional ERC-20 wrapper with rights suspended until re-registration.

### 3. Treasury, liquidity and OTC lane — **[NEW, from 2026-07-24 call]**

- A **treasury wallet** is needed for liquidity management.
- A potential **fourth investment type**: large, locked investments via **OTC deals**, funded from the treasury wallet, requiring their own compliance process.
- Market structure discussed: **DEX for smaller purchases, CEX for larger**, mirroring how PAXG operates.
- Investments are made in **stablecoins**.
- **Reserve management as inventory** (Tony): gold should not sit idle, nor be insufficient to fill orders. Lean demand prediction to hold optimal reserves.

### 4. Multi-SIP user experience and fund-handling compliance — **[NEW, from 2026-07-24 call]**

- Users may hold **multiple concurrent SIPs with different timelines**, with lock periods anywhere from **6 months to 25 years**. The UX for managing several different lock periods simultaneously is an open design problem.
- **Compliance requirements for handling user funds** were flagged and need specification.

### 5. Supply reduction / burn mechanism — **[NEW, from 2026-07-24 call]**

Tony raised a **PAXG-style burn** as a thought experiment: reducing token supply while holding the same gold backing would raise gold per token over time. Interacts with the denomination decision (Q3) and offers a possible non-cash route for custody fee settlement (Q9). To be assessed alongside both.

### 6. AI advisor replacing human agents — **[NEW, from 2026-07-24 call]**

Tony proposed replacing human financial advisors with **AI agents**, eliminating commission leakage, retaining value in the platform and improving scalability. Logged as a **future consideration**, not a current design input, but it bears on how much agent commission we bake in structurally.

---

## Outstanding items

**From the client:**
- [ ] **Google Drive access** (CG) containing additional documentation, including the **differential fee structure for spot vs SIP**. Blocks final fee design (Q9).
- [ ] **Voice of customer / engagement objectives** (Q14). Ask on the Wednesday call.
- [ ] Final percentages for **spot capacity** (currently a 20 to 40 percent range).

**On our side:**
- [ ] Decide whether the **silver product revenue model** is shared with the client or used internally only (Q5).
- [ ] Pull the **IRDAI (Payment of Commission) Regulations 2023** text directly for actual commission caps (Q5).
- [ ] Reconcile **sub-gram token unit vs 10 gram retail convention** (Q3).
- [ ] Correct the **110 percent to 90 to 95 percent** LTV in the V3 documentation, and re-space warning/liquidation thresholds (Q10).

**Next meeting:** Wednesday, 9 a.m. CST.
> ⚠ The meeting summary is internally inconsistent on this: the Next Steps section says **Wednesday**, the closing summary says **Thursday**. Confirm with the client.

**Deliverable split agreed:** Abdur on market research and the initial revenue model; Tony on the project charter.
