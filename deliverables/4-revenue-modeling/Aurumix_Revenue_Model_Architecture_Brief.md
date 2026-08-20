# Aurumix — Revenue Model Architecture Brief

**Date:** 2026-08-19
**Version:** 2.4 (draft — structural sections)
**Phase:** 4, Revenue and Economic Modeling (repo folder 4; charter Phase 3)
**Status:** Architecture for review. No spreadsheet built yet. Build follows sign-off on Section 3.
**Supersedes:** v2.0 (2026-08-18) and v1.0 (2026-08-17, commit `668e0d5`). Every architecture change through v2.0 is recorded in `_working_architecture-decisions-v2.md` as decisions D1–D20 and is cited here at the point of use. **v2.1 carries three client decisions on top of that record: D21 the 7-year, 29-column basis; D22 the collapse of the score machinery to a tenure→tier lookup; D23 cohorts as a convolution rather than a triangle.**

> ⚠ **Figures in this document are from the v2.0 ten-year model run and are illustrative of the architecture, not final.** The architecture below is what is being reviewed. Once it is signed off, the reference model is rebuilt to the 7-year, 29-column basis and every figure is re-cut. Expect levels to move; the structural findings in §0 are not expected to.
>
> **What this document is.** A complete, implementable plan for the Aurumix revenue and cost model. After reading it, a modeller should be able to build the workbook without asking a question. Every value, formula and structure is specified, and every assumption carries its source and confidence.
>
> **What changed at v2.0, in one paragraph.** v1.0's research and sourcing survived audit intact. Its *architecture* did not. Five audits — arithmetic, corpus fidelity, structural, benchmark and buildability — established that the three-state population machine drops 81% of the terminal book out of the model, that tier distribution cannot be computed from cohort averages, that a single constant hazard cannot reproduce the persistency curve v1.0 itself recommends, that a model with no cash flow cannot answer "when do we make money," and that the break-even figures in §0.3 were divisions of an opex base sized for 500 investors by a margin figure that could never meet it. v2.0 rebuilds the engine around a six-state population, five behavioural archetypes, a pre-gate block, a net-flow redemption term, and a cash and funding layer. **The findings v1.0 reached are, if anything, strengthened. The numbers it reached are withdrawn.**
>
> 🆕 **What changed at v2.6, in one paragraph.** One decision (D32, 2026-08-20, Abdur), and it is an accounting correction rather than a re-pricing. **The float cost of capital (F5, 0.49%) leaves the margin waterfall and becomes a memo line.** The reasoning: it is an **opportunity cost on equity, not a cash expense** — nobody invoices Aurumix for it — and booking an imputed equity cost inside **COGS** is not something a statutory P&L does. ⚠ **This is also an internal-consistency fix: §7.6 already treats the VARA locked-capital escalator exactly this way** — *"report the escalator as an opportunity cost, not a P&L line… as a memo line"* — and F5 was the one place the brief broke its own rule. **Net contribution margin on a USD 75 ticket 2.30% → 2.79%; minimum viable entry fee ~2.74% → ~2.26%.** 🔴 **What this does NOT mean is that the float is free.** The float **principal** is real cash — **USD 29k at Y1 rising to USD 3.6M at Y10** — it stays on the balance sheet, it stays in the funding view, and it stays inside the USD 15.1m peak-funding figure. **It stopped being a P&L line; it did not stop being money.** ⚠ **And the premise that "they hold the gold anyway" does not hold: the trust holdings are the CUSTOMER's gold and cost Aurumix no capital; the float is AURUMIX's own inventory bought with Aurumix's own money. Two different piles of metal with two different owners.** See D32.
>
> 🔴 **A pattern worth naming, since it has now run twice in one day.** D31 removed the rail and D32 removed the float carry. Each is individually defensible. **Cumulatively, the minimum viable entry fee has fallen 3.07% → 2.74% → 2.26% without one thing changing in the business** — the costs were re-attributed, not reduced. ⚠ **§0.3, a finding present in every version of this brief, has been dissolved by reclassification. That is a legitimate outcome and it is also exactly how a model talks itself into a number. Before this reaches the client, the remaining cost base — premium plus price-gap — should be adversarially re-checked, and the premium's replication failure (correction 36) makes that urgent rather than optional.**
>
> 🆕 **What changed at v2.5, in one paragraph.** One decision, and it is the client's (D31, 2026-08-20, Abdur). **The payment rail leaves the entry-fee build-up.** The principle: *the entry fee comprises only what Aurumix itself charges.* The rail is a third-party bank/PSP cost, so it is **grossed up onto the collection request and passed through** — Aurumix requests `ticket + rail`, remits the rail to the PSP, and books zero margin on it. `STREAM1a` and `STREAM1b` lose their `− rail` term. **Four consequences, and three reverse a stated finding.** ⚠ **(1) §0.3 FLIPS at the Base rail:** minimum viable entry fee falls from ~3.07% to **~2.74%**, so the 3% target becomes **fundable with ~0.26pp of headroom** rather than sitting at break-even. ⚠ **(2) The minimum-ticket problem dissolves as a margin problem** — `C_min = R ÷ (f − c)` with `R = 0` has no solution, so *every* ticket is margin-positive wherever `f > c`. ⚠ **(3) Spot stops being "structurally the highest-margin inflow"** — SIP and spot converge to an identical **2.79%**, because the entire gap between them *was* the fixed rail spread over a larger base. 🔴 **(4) S1 collapses out of the tornado**, where it ranked 6th at USD 1,607,643 of swing on cumulative net profit. **What this does NOT do is make the customer better off: the cost moved, it did not vanish, and the incidence is regressive — at the Conservative rail the gross-up is +6.8% on a USD 20 saver against +1.8% on a USD 75 one.** Full argument and the three risks it carries: D31 in `supporting/_working_architecture-decisions-v2.md`.
>
> 🆕 **What changed at v2.4, in one paragraph.** Three decisions, all from one research pass recorded in `supporting/_working_dealer-premium-and-comparables-research.md`. **D28: F4, the fabrication premium, is measured rather than guessed** — 100 g at **1.50%** and 1 kg at **0.95%**, from a same-page dealer pair where the rate and the bar prices are struck at the same moment, less a published bulk gradient. The ladder was **one denomination too pessimistic at every rung**, and Good Delivery is retired as a rung because Dubai's own standard is a 1 kg bar. **D29: S51 flips to own float from M1**, because all three routes the comparables use to avoid carrying metal are closed to Aurumix. **D30: the premium is charged on net new grams, not gross inflow**, because redeemed gold returns to the float. ⚠ **Net contribution margin on a USD 75 ticket rises from 0.54% to 1.97% and the break-even ticket falls from ~USD 29 to USD 10.90 — but §0.3 survives with a different cause: the 3% fee is now short by ~0.07pp rather than 0.79pp, and the binding cost is no longer the premium, it is the 1.28% of price-gap and float capital that D29 moves onto Aurumix's book from launch.** 🔴 **The same pass found that DMCC Tradeflow cannot carry fractional customer interests and that no LBMA approved-vault network exists — corrections 26 to 30.**
>
> 🆕 **What changed at v2.3, in one paragraph.** One decision, and it is presentational rather than structural. **D26: the workbook is delivered on the firm's standard five-sheet architecture — Cover, Assumptions, Scenario Parameters, Model, Summary — with the machinery moved to five working sheets placed after them and hidden.** The former Opex & P&L sheet folds into Model as a second row band, so a reader can trace one visible sheet from accounts acquired to net profit and cash. Checks hides, and its master flag is mirrored to the Cover as a link. **Nothing about what is computed, or in what order, changes.** ⚠ **One real consequence: the acyclicity rule was written as "no sheet may reference a sheet to its right," and hiding inverts tab order against logical order. The test is now by sheet NAME against the §3.x.1 order, which is written onto the Cover so it cannot be lost** (§3.x.1, §3.x.4).
>
> 🆕 **What changed at v2.2, in one paragraph.** Two decisions. **(1) The bottom-up engine was deliberately reopened and confirmed** (D24): when most inputs are unknown, a top-down model concentrates the whole answer in one unfalsifiable penetration share, cannot produce a tornado to tell you which unknown to resolve first, and cannot see that only 53.5% of accounts ever reach the gate that unlocks 83% of the profit. The five findings in §0 are structural, so they survive a wholesale re-cut of the parameter set. **(2) §5 is rewritten** (D25): six occupational segments become **four regional ones**, and the population is re-cut from Indian to **South Asian**, after three research streams against primary sources. Each region now carries an **average ticket plus a floor share**, which derives two ticket bands and preserves both the fixed-rail-cost and the card-spend non-linearities that a single blended average would have destroyed. **Bahrain leaves the model** on the CBB Crypto-Asset Module and becomes a sized note. 🔴 **The book-weighted ticket falls from ~40 to ~31.5, so §0.3's minimum viable entry fee rises. The reference model has NOT been re-run: every output figure below still reflects the pre-D25 segmentation.**
>
> **What changed at v2.1, in one paragraph.** Three decisions, all taken by the client and none re-openable here. **(1) The horizon is 7 years on 29 columns — 24 monthly plus 5 annual** — matching the firm's DRODE precedent, whose Model sheet was 29 columns on exactly this split (D21, §1). **(2) The per-period score arithmetic collapses to a tenure→tier lookup plus one heavy-seller haircut** (D22, §3 Layer 5); the eligibility gate, the survival engine and the never-gated population stay as a live engine, because measurement says the rate ladder is second-order and eligibility is first-order. **(3) Cohorts become a convolution** — five monthly lifecycle curves computed to M84 on an input sheet, convolved against the monthly acquisition vector (D23, §3 Layer 2). **The workbook must not contain a cohort triangle.** The engine's shape changes; none of its findings do.
>
> **How to read the figures.** Every figure that is an *output* of the model is filled from the reference implementation in `reference_model/`, and none is carried over from v1.0 — v1.0's headline figures were proved wrong, and reusing one in a slot that belongs to the model would be worse than leaving it visibly empty. Every figure that is an *input* — the F-, S- and T-series values, corpus-sourced constants, published rates — is written out in full, because those are real. **A small number of slots remain marked `{{UNFILLED: … }}`. Each one is a figure the reference model does not compute, with the reason stated in the marker. They are open items, not oversights.** ⚠ **Every output figure is on the ten-year basis and is superseded by the rebuild.** Where a figure belongs to Y8–Y10 it is now labelled as beyond the new horizon at the point of use.

---

## 0. Read this first: the five findings that determine the architecture

Everything below follows from these. If you disagree with one, the model changes shape, not just its numbers.

> ⚠ **Figures in this section are from the v2.0 ten-year model run and are illustrative of the architecture, not final.** Once the architecture is signed off, the reference model is rebuilt to the 7-year, 29-column basis and every figure is re-cut. **Expect levels to move; the structural findings below are not expected to.**

**Every figure in this section is model output**, generated by the reference implementation in `reference_model/` and reproducible by running it. That is the first difference from v1.0, whose headline stack could not be rebuilt from its own stated drivers — an audit found the Year 10 interchange line was 23–32% below what its own assumptions produced. Nothing here is asserted.

---

### 0.1 The card is not 71% of the business. It is 83%.

v1.0 concluded that Aurumix is a card business with a gold savings funnel. That was right, and it was understated.

| Stream | Y10, USD | Share of gross profit |
|---|---|---|
| Card interchange, net of PM share and per-transaction fees | 4,156,380 | **54.3%** |
| Cardholder fees (FX, ATM, issuance) | 2,226,204 | **29.1%** |
| B2B platform fee | 1,221,200 | 15.9% |
| Family plan and Digital Will | 111,065 | 1.5% |
| Credit revenue share | 12,135 | 0.2% |
| **Entry fee margin — SIP** | **(80,548)** | **(1.1%)** |
| Entry fee margin — spot | 10,771 | 0.1% |
| **Gross profit** | **7,657,206** | 100.0% |

**Streams 2 and 4 together are USD 6,382,584 — 83.4% of gross profit.** Remove the card and Year 10 revenue falls from 8,150,081 to 1,767,497. The savings product is not merely the acquisition funnel; on these numbers it does not pay for itself at all.

Note the sign on the entry fee. **The SIP lane loses money at Year 10.** That is finding 0.3.

⚠ One reassurance about the denominator. Interchange at **54.3% of gross profit** independently reproduces v1.0's "54% of terminal revenue" claim — arrived at from a completely different account trajectory and cost base. Two of v1.0's structural instincts survive contact with a working model; its arithmetic did not.

---

### 0.2 Nearly half the book never earns a score at all

The six-consecutive-payment gate is a **run-of-6 first-passage problem**, not a date. v1.0 treats month 6 as universal. Solved as a Markov chain on run length with survival applied monthly:

| Archetype | Weight | P(ever gates) | Mean gate month |
|---|---|---|---|
| Perfect payer | 10% | 90.6% | 6.1 |
| Occasional misser | 35% | 83.6% | 7.6 |
| **Alternating misser** | 12% | **24.0%** | **24.9** |
| Reducer | 13% | 88.6% | 6.6 |
| Early lapser | 30% | 2.6% | 8.6 |

- **Expected gate month: 8.1**, not 6.
- **Ever-gate share: 53.5%.**
- At Year 10, **4,047 accounts — 18.7% of the live book — have never held a tier.**

**The alternating misser is the row to look at.** Paying every other month, it has a 24% chance of ever assembling six consecutive periods. v1.0 has that entire cell at Silver in month 6 and Gold by month 12. In reality three-quarters of it never scores.

Two consequences, and they pull in opposite directions:

1. **Every ladder date shifts right.** Gold, card eligibility, credit and Sovereign all move by the expected gate delay. The card — 83% of the business — starts later than v1.0 assumes.
2. **The never-gated are the highest-margin retail accounts in the book.** They pay the **full undiscounted entry fee** and consume **zero benefits, ever**: no tier discount, no Gold Rewards, no card, no credit, no family discount. v1.0 has no cell for them, which simultaneously understates stream 1 margin and overstates benefit cost.

The corpus called persona H "the row to be honest about." It is 18.7% of the book.

---

### 0.3 The planned entry-fee cut to 3% is not fundable — ⚠ REVERSED AT v2.5, CONDITIONALLY

> 🆕 🔴 **D31 REVERSES THIS FINDING AT THE BASE RAIL. It survived v2.4 with a changed cause; at v2.5 it does not survive at all — provided the rail pass-through holds.**
>
> 🆕 **At v2.6 the cost base is `1.50% premium + 0.79% price-gap` and NOTHING else** — the rail passed through at D31, the float carry became a memo line at D32. **Minimum viable entry fee at a USD 75 ticket: ~2.26%.** Against the client's 3.00% target that is **0.74pp of headroom**, where v2.4 had none and v1.0 was short 0.79pp. *(v2.5 read ~2.74% and 0.26pp; superseded.)*
>
> 🔴 **Read that with the pattern in view.** The fee became fundable across two turns of reclassification, not because any cost fell. **Two of the four cost lines were re-attributed in a single day and the third — the premium — failed replication the same day.** ⚠ **The finding is not "the fee cut works." The finding is "the fee cut works if the premium is really 1.50% and if customers accept a grossed-up collection request," and neither of those is established.**
>
> ⚠ **Three conditions on the reversal, and they are the whole of it.**
> 1. **It is fundable because the customer now pays the rail separately, not because any cost was removed.** All-in customer cost is unchanged. Do not present this to the client as a cost saving; it is a re-attribution.
> 2. **It holds only if the pass-through is actually collectable.** If a USD 20 saver refuses a USD 21.36 request at the Conservative rail, the rail returns to Aurumix's book as churn, not as a cost line — and it lands on the segment the model can least afford to lose. **This is now the live risk, and it replaces the fee-fundability risk rather than cancelling it.**
> 3. **The fee ladder table below has NOT been re-run**, and it was built on the pre-D28 premium as well. The ~2.74% is a single-ticket calculation; the year-by-year schedule needs the reference-model rebuild.
>
> 🔴 **What does NOT reverse: §0.3's structural point.** The fee schedule and the denomination schedule remain physically coupled, and the fee still cannot fall below the premium plus the float costs. **The constraint moved; it did not disappear.**
>
> 🆕 🔴 **AND A COUNTERVAILING FINDING LANDED THE SAME DAY.** The 2026-08-20 research pass **failed to replicate D28's 1.71% / 0.93% Dubai ask premiums** — goldtrade.ae's rate page moved 6 bp overnight while its store moved 241 bp, so the two pages do not share a clock and the pair is not simultaneous. **If F4 reverts toward 3.00%, the ~2.74% becomes ~4.2% and this reversal is itself reversed.** See `supporting/_working_dealer-bid-side-and-vaulting-research.md` §5. **Do not carry the 0.26pp of headroom to the client until F4 is re-observed.**
>
> **The v2.4 note is retained below as the audit trail.**
>
> 🆕 🔴 **THIS FINDING SURVIVES v2.4, BUT ITS CAUSE HAS CHANGED AND THE TABLE BELOW IS SUPERSEDED** (D28, D29).
>
> **The premium is no longer the binding cost.** F4 is now measured, not assumed: **100 g at 1.50%, 1 kg at 0.95%**, against the 3.00 / 2.00 / 0.75 ladder this section was written on. The ladder was **one denomination too pessimistic at every rung**, and the Good Delivery argument below targeted the wrong object — **Dubai's own Good Delivery standard is a 1 kg bar, not a 400 oz bar** (research record §7.1).
>
> **What binds instead: the 1.28% of price-gap risk and float cost of capital that D29 moves onto Aurumix's own book from M1.** The minimum viable fee at a USD 75 ticket falls from **4.96% to ~3.07%**, so **the 3% target now sits essentially AT break-even rather than 0.79pp below it.** It is still not funded, and it now has no headroom at all rather than a large deficit.
>
> ⚠ **Two things follow for how this is said to the client.** First, *"the fee cut is unfundable"* becomes *"the fee cut breaks even and leaves nothing for anything else"* — a materially different conversation. Second, **the lever moved: it is no longer the dealer's premium, it is the pricing convention.** The 0.79% price-gap exists because the price is struck at the next LBMA fix, hours away; Paxos reduces the same exposure to near zero with a 5-second quote hedged instantly with a named dealer (research record §4.2). **That trade-off — neutral pricing versus price-gap cost — is now a live decision worth ~0.79pp and it has never been framed as one.**
>
> **The table and text below are the v2.0 position, retained until the reference model is re-run at F4 = 1.50%.**

v1.0's fee ladder falls 5% → 4% → 3%. That was justified by the fabrication premium falling 3.00% → 2.00% → 0.75%, which requires Good Delivery bars. **Solved endogenously against the model's own volume, Good Delivery never clears** — at ~126 kg/year a 12.4 kg bar fills roughly ten times a year and the price-gap carry swamps the premium saving. 1 kg clears at Year 5, not Year 3.

So the premium holds at 2.00%, and:

| Year | v1.0 assumed fee | Minimum viable fee | Fundable? |
|---|---|---|---|
| 1–2 | 5.0% | 4.96% / 3.99% | Yes |
| 3–4 | 4.0% | 4.18% | **No** |
| 5 | 4.0% | 3.78% | Yes |
| 6–7 | 3.5% | 3.79% / 3.74% | **No** |
| 8–10 | 3.0% | 3.74% / 3.76% / 3.79% | **No — short 0.79pp at Y10** |

**Seven of ten years are priced below cost.** The binding lane is always SIP, never spot (3.79% vs 2.87% at Y10) — which is v1.0's own fixed-rail non-linearity restated: *the fee floor is set by the smallest ticket carrying a fixed collection event.*

Stated as a constraint rather than a recommendation: **the entry fee cannot fall below roughly 3.8% unless volume justifies a larger bar or the rail cost falls.** A larger bar needs about four times the modelled Year 10 gram volume. The rail is a live PSP negotiation. **The fee schedule and the denomination schedule are physically coupled, and v1.0 decoupled them.**

The model runs T1 on v1.0's assumed 5/4/3 deliberately, so the P&L shows the consequence of the client's actual plan rather than silently repricing it.

---

### 0.4 The client's Year 10 target is met or missed by a factor of three, depending on a definition nobody has fixed

v1.0 §14 asks, as an open question, whether the 60,000–100,000 target counts accounts opened or investors still contributing, and guesses they differ by about 5×.

| Measure | Y10 | vs a 60,000 target |
|---|---|---|
| **Accounts holding gold** | **64,197** | **107% — met** |
| **Still contributing** | **20,990** | **36% — missed** |

The gap is **3.06×**. This is not a presentational choice: the two populations drive different lines. **AUM, custody cost, the B2B fee base and the credit collateral base follow the holding count. Contribution flow, rail cost and entry-fee margin follow the contributing count.** A model that treats lapsed accounts as gone — as v1.0 does — loses three-quarters of the population that carries the balance sheet.

This needs settling with the client before any target is agreed, because both answers are defensible and they describe different businesses.

---

### 0.5 The two most valuable questions in the engagement are not research questions

v1.0 ranked the payment rail as "the single most important unknown in the model." The tornado says otherwise. On cumulative net profit:

| Rank | Driver | Swing, USD |
|---|---|---|
| 1 | Card spend per active card | **14,177,704** |
| 2 | Card activation rate | 6,539,376 |
| 3 | PM share of interchange | 6,359,822 |
| 4 | Card programme fixed costs | 2,125,500 |
| 5 | Payment archetype mix (persistency) | 1,906,962 |
| 6 | Rail cost per collection | 1,607,643 |

**The card triple takes the top three and outweighs everything else by roughly seven to one.** Persistency — which v1.0 called "the number that governs the calibration" and which genuinely does drive the tier distribution and is what makes the tier mix computable at all — still ranks only fifth on profit, because on this cost base the card drivers dominate it.

**And the rail is sixth.** At Year 10 the adverse rail costs USD 283,428 against 8.15m of revenue. It is a Year 1–3 survival problem, not a terminal-value driver, and v1.0 pointed the client at a PSP conversation when the money is elsewhere.

Two questions are worth more than any further research:

**1. Does a lapsed customer keep the card? Worth USD 3,393,774 a year — 42% of Year 10 revenue.** Nobody has ever asked. It decides whether the largest revenue stream decays with persistency or is immune to it, and at 19% five-year persistency that is close to deciding the business. v1.0 silently assumed immunity by treating lapsed accounts as gone from everything *except*, implicitly, nothing at all.

**2. What programme manager share can be negotiated? On the ten-year run, the smallest share producing any EBITDA-positive year was 77.5%.** Base assumes 72%; the researched range is 55–85% with a hard floor at 36% below which Gold Rewards stops self-funding. **A few points of PM share is the difference between a business that turns and one that does not, and it is a negotiation rather than a research question.** ⚠ The 77.5% solve is a ten-year figure; on a 7-year horizon the required share is higher, and the rebuild will state it.

Both are commercial conversations. Neither can be closed by more desk research, and both are worth more than every unresolved research question in §16 combined.

---

### 0.6 What moved from v1.0, and why

| Figure | v1.0 | v2.0 | Driver of the change |
|---|---|---|---|
| Y10 net profit | +2,468,500 | **(367,051)** | Real opex on the model's own book; entry fee below cost; stream 5 collapse |
| Break-even | Y7–Y9 | **None in ten (~Y10.9)** | Fixed point against total cost, not opex |
| Investors to break even, entry fee only | 171,911 / 278,444 / 786,620 | **No solution at any N** | Opex made a function of N |
| Peak funding | *absent* | **15,076,460** | Cash flow and float funding added |
| Card share | 71% | **83.4% of gross profit** | Correct denominator; per-transaction fees; segment card spend |
| Y10 opex | 8,495,500 | **3,219,856** | Charged against 20,990 contributing, not an assumed 80,000 |
| Y10 AUM | ~404,500,000 implied | **39,790,584** | Reconciled to cumulative contributions |
| Y10 entry fee | 3.0% assumed | **3.79% minimum viable** | Denomination solved endogenously |
| Stream 5 | ~600,000 | **12,135** | Collateral base per holding account (2.96×) × turnover (1.88×) |
| Tier mix | assumed (T4/T5) | **computed** | Archetype tracks replace cohort averaging |
| Accounts at gate | all at M6 | **53.5% ever, mean M8.1** | First-passage solve |

**What did not move, and matters.** The fee waterfall in §6.1, the rail equation, every ICS constant, the 36% PM floor, the VARA III.E.4 constraint and all ten cited decision numbers were checked against the corpus and are correct. The research underneath v1.0 was sound. **What failed was the architecture built on top of it, and the arithmetic that architecture produced.**

**Validation.** The persistency curve reproduces all five published anchors at 0.919pp RMSE using weights derived independently of those anchors — a genuine cross-validation rather than a fit. All nine ICS personas reproduce, including the two v1.0's architecture provably could not. Every invariant is asserted each period and the cost bridge closes to zero. Details in `reference_model/VALIDATION.md`.

---

> **Footnote — break-even and funding, demoted at v2.1.** v2.0 carried these as finding 0.4. **They are not a finding to lean on**, at client instruction: the cost base, the fee schedule and the card terms are all expected to change materially before the model is final, and both outputs are dominated by exactly those inputs. **Neither break-even nor peak funding falls inside a 7-year window on any run to date.** For the record, on the v2.0 ten-year run: no profitable year in ten, Y10 net profit **(367,051)** against v1.0's +2,468,500, peak funding **USD 15,076,460** at M114 with a range of USD 6.0m to 25.4m across scenarios, and the fixed point `revenue(N) = total_cost(N)` solving at **45,102 accounts on all streams** and **at no N at all on the entry fee alone** — the entry-fee margin slope in N is negative, so adding investors makes it worse. **That last result is structural and survives any horizon**: it is the reason v1.0's three precise figures (171,911 / 278,444 / 786,620) were withdrawn. The method is specified at §14 and stands; the levels are not to be quoted. ⚠ M114, M115 and the Y10 figures all fall **beyond the new 7-year horizon**.

---

## 1. Model Overview

| Field | Value |
|---|---|
| **Project** | Aurumix (AURX), a VARA-regulated gold-backed monthly savings product in Dubai. 1 AURX = 1 gram of allocated physical gold. SIP from USD 20/month **plus a spot purchase lane**, an Investor Conviction Score governing five benefits, a gold-collateralised credit facility and card, and a B2B white-label channel |
| **Revenue Model Type** | Hybrid, and deliberately unbalanced: one inflow-linked stream with two sub-lanes (entry fee on SIP and on spot), three activity-linked streams (interchange, cardholder fees, lending), one headcount-linked stream (family and will), one AUM-linked stream (B2B platform fee), and **one mandatory zero-revenue cost stream (redemption)** |
| **Modeling Approach** | **Lifecycle-curve convolution with heterogeneous behavioural archetypes.** Acquisition by channel and segment produces a monthly vector; five payment-archetype lifecycle curves, computed once to M84 on an input sheet, carry alive / contributing / reduced / gated / tier / grams / card-active / spend per month-since-origination; the book in any period is the **convolution** of the acquisition vector against those curves. Eligibility is a live engine (the run-of-6 gate); the rate ladder is a **tenure→tier lookup** (D22, D23) |
| **Time Horizon** | **7 years**, from an assumed Year 1 start of **January 2027** |
| **Granularity** | **Hybrid: monthly M1 to M24, annual Y3 to Y7** |
| **Total Periods** | **29** (24 monthly + 5 annual) — D21 |
| **Currency** | USD primary, AED at the peg 3.6725 |
| **Headline outputs** | (1) contribution margin per cohort by month since acquisition — read straight off a lifecycle curve, not a triangle; (2) **LTV:CAC by channel × segment**; (3) revenue mix over time; (4) the funding trajectory, **reported as a shape rather than a level** (§14). The investor-count break-even is **kept as a named finding**, not as the headline — D16 |

**Why 29 periods, 24 monthly + 5 annual.** This is the firm's DRODE precedent, whose Model sheet was 29 columns on exactly this split. It replaces v2.0's 76 columns (72 monthly + 4 annual), which is withdrawn (D21).

**The monthly window must cover everything that needs month-level resolution, and it does.** Three dates decide that, and all three land inside 24 months:

| Event | Period | Why it needs monthly resolution |
|---|---|---|
| **The gate resolves** | **around M8** | Gate arrival is a run-of-6 first-passage distribution with a cohort-weighted mean of **M8.1** (§0.2). Eligibility is the first-order driver of the whole card stack, and it is settled inside the monthly block |
| **The card launches** | **M18** | Streams 2 and 4 activate — the majority of terminal revenue — and F27 programme fixed costs begin **M15**, three months earlier. Both sit inside the monthly block, so the ramp is resolved month by month rather than smeared across a year |
| **Gold arrives** | **around M20** | Gold is the eligibility threshold for card, credit and Gold Rewards. The earliest arrival is M12; the gate-delayed mean lands around M20. **The tier that carries the eligibility decision is resolved monthly** |

**Platinum and above fall in the annual block, and that is acceptable *precisely because* the tier ladder was collapsed** (D22). Platinum is earliest at M36 and Sovereign at M61 — both beyond M24. Under v2.0 that would have been a defect, because the per-period `Record`/`Standing`/`Retention` arithmetic priced every tier separately and the top of the ladder carried the highest interchange, the deepest waivers and the largest rewards. **Under the collapse, the rate ladder is a flat Gold rate with a measured cost of ~2% of gross profit at Y7** (§3 Layer 5), so resolving Platinum and above annually costs almost nothing. **The two decisions reinforce each other: shortening the monthly window is safe because the ladder collapsed, and collapsing the ladder is safe because eligibility — the part that is first-order — is still resolved monthly.**

**B2B activates at M24, exactly on the boundary.** Place it at the **start of the annual block (Y3), not as a single stub month at M24.** A one-month stub inside the monthly block would give stream 6 a twelfth of a year's revenue in a column that then has to be reconciled against a full annual column beside it, which is the seam error §10.5 exists to prevent. **Stream 6 is zero through M24 and starts on the Y3 column** (§4).

⚠ **The lifecycle table stays monthly to M84 even though the Model sheet is 29 columns.** This is the resolution that makes the shape work and it must not be collapsed for tidiness: the curves are an **input sheet**, computed monthly out to M84 so that a Y7 annual column can still be built from twelve genuine monthly lifecycle points. **The Model sheet is 29 columns; the Lifecycle Curves sheet is 84.** See §3 Layer 2 and §12.

**What happens in the annual block, stated rather than fudged.** From Y3 onward the Model sheet carries annual aggregates. **Nothing is frozen** — that was v2.0's M72 hold rule and it is no longer needed, because the lifecycle curves run monthly to M84 and an annual column is the sum or average of twelve of their monthly points. **The annual block loses column resolution, not engine resolution.**

**Monthly-to-annual conversion notes.**

| Quantity | Conversion rule |
|---|---|
| Archetype survival | Already monthly by construction, on the lifecycle curve (D3, D23). An annual column reads the curve at each of its twelve months and aggregates. **No `^12` shortcut is needed or permitted** — the curve is tabulated. |
| Lifecycle beyond M84 | The curves are computed to **M84**, which covers a Y7 annual column for the M1 cohort. **No cohort in a 7-year model has more than 84 months of life**, so no extrapolation rule is required — the v2.0 M120 extension is withdrawn. |
| Tier mix | Read off the tenure→tier lookup at each monthly point, convolved against acquisition, then aggregated. **Not held, not frozen.** |
| Heavy-seller haircut | A single multiplier on the tier mix, applied identically in both blocks (D22, §3 Layer 5). |
| Card spend, interchange, cardholder fees | Monthly flows on the curve. An annual column sums twelve convolved monthly values. |
| B2B platform fee | Invoiced monthly on a stock. **Activates at the start of the annual block (Y3).** In annual periods use the average of opening and closing partner AUM. Each partner runs its own maturity clock (S43). |
| Seasonality (S52a, S52b, S53) | Applies to the monthly block only. In the annual block it cancels by construction, since all three vectors normalise to exactly 12.00. |
| Tax | **Booked annually, in the final month of the financial year, never monthly** (F33–F35). |

### 1.1 Sheet index

🆕 **Five visible sheets and five hidden working sheets** (D26, revising D18 and D23). **The five visible sheets are the firm's standard revenue-model architecture and their names and order are fixed by the `revenue-modeler` skill: Cover, Assumptions, Scenario Parameters, Model, Summary.** Everything that is machinery rather than argument is a working sheet, placed after the five and **hidden in the delivered file**. Full row bands, freeze panes and colour legend at §12.

**Visible — the five, in tab order:**

| # | Sheet | Purpose | Depends on |
|---|---|---|---|
| 1 | **Cover** | Title, version, scope, colour legend, period-count statement, **the logical dependency order (§3.x.1), and the master check cell** | Checks |
| 2 | **Assumptions** | F-, S-, T-series with unit, basis, confidence, source URL, source category, sheet location | — |
| 3 | **Scenario Parameters** | Global switch, per-parameter override, named narrative scenarios, binary switches | Assumptions |
| 4 | **Model** | The convolution, contribution flow, spot lane, unit margin, AUM stock, all six revenue streams, benefit costs, **then opex, acquisition cost, EBITDA, tax, working capital, cash and funding**. **29 columns, ~280 rows** | Lifecycle Curves, Acquisition, Time Series |
| 5 | **Summary** | Annual roll-ups, revenue mix, unit economics, break-even views, tornado inputs | Model |

**Hidden — the five working sheets, placed after the visible five:**

| # | Sheet | Purpose | Depends on |
|---|---|---|---|
| 6 | **Time Series** | **29** period headers, activation flags, seasonality vectors, gold price, fee ladder, bar denomination | Assumptions, Scenario |
| 7 | **Lifecycle Curves** *(new at v2.1)* | **Monthly to M84.** Five archetype curves carrying alive / contributing / reduced / gated / tier / grams / card-active / spend per month-since-origination. **The only monthly-to-M84 sheet in the workbook** | Assumptions, Scenario |
| 8 | **Acquisition** | Acquisition by channel × segment → the **monthly acquisition vector**, with segment scalars and the S4/S5/S6 offsets | Time Series |
| 9 | **ICS Validation** *(demoted from Engine)* | The full ICS formula and the nine-persona test set, run as a **validation artefact** against the collapsed lookup, plus the 5% safety gate (§3 Layer 5) | Lifecycle Curves |
| 10 | **Checks** | Conservation and sanity tests, all returning TRUE/FALSE, **including the D22 collapse-safety gate** | All |

🆕 **Two placement decisions inside D26, both deliberate:**

1. **Opex and P&L fold into the Model sheet rather than hiding.** A reader must be able to trace one visible sheet from accounts acquired to net profit and cash without unhiding anything. **The cost is height, not complexity: ~200 rows becomes ~280.** ⚠ This also resolves the inconsistency §12 records in v1.0, which listed an Opex sheet in one section and put opex rows on the Model sheet in another. **There is now one answer: opex rows live on Model.**
2. **Checks hides, but its master flag is promoted to the Cover.** **The Checks sheet is still where this build exceeds the benchmark**, which has none (D18) — but sixteen TRUE/FALSE rows are a working artefact, not a presentation one. **Cover carries a single `ALL CHECKS PASS` cell reading the Checks master row, red on FALSE.** The signal survives; the clutter does not.

⚠ **Hiding a sheet changes nothing about what it computes or when.** The dependency order at §3.x.1 is unchanged by D26. **What D26 does change is how that order is enforced — see the warning at §3.x.1 about tab position, which now runs backwards against the logical order and must not be used as the test.**

---

## 2. Model Sketch

### 2.1 Revenue architecture

```
+=============================================================================+
|                            ACQUISITION LAYER                                 |
+=============================================================================+
| Channel:  Agent | Referral (dark to M13) | Direct (paid + organic) | B2B     |
|              |          |                       |                    |        |
|  agents x    | qualified|   spend / effective   |  partners x        |        |
|  S12 x ramp  | referrers|   CAC (S25 curve)     |  AUM ramp (S43)    |        |
|  S17, net of | x S19    |   + organic S26       |  60% -> S5 (S16)   |        |
|  attrition   | x S20    |                       |                    |        |
|  S18         |          |                       |                    |        |
|              v          v                       v                    v        |
|         CHANNEL-TO-SEGMENT MIX MATRIX (S16, three phases)                     |
|              |                                                                |
|              v      x  LOGISTIC SATURATION (S23) on cumulative-ever-acquired  |
|                        against base(s) x ceiling(s) (S22)                     |
|              v                                                                |
|      New accounts/month BY SEGMENT  x  SEASONALITY (S52a)                     |
|        S1 UAE professional  USD 75   S4 Oman+Bahrain  USD 40  [M13]           |
|        S2 UAE white-collar  USD 40   S5 India         USD 30  [SWITCH]        |
|        S3 UAE blue-collar   USD 20   S6 Other intl    USD 75  [M25]           |
|                                                                               |
|   ==> THE MONTHLY ACQUISITION VECTOR  a(s,t),  t = 1..24 monthly then Y3..Y7  |
|       Later-activating segments S4/S5/S6 are handled by OFFSETTING a(s,t),    |
|       NEVER by a new lifecycle curve  (D23)                                    |
+=============================================================================+
                                    |
                                    |  convolve  (SUMPRODUCT)
                                    v
+=============================================================================+
|   LIFECYCLE CURVES  --  INPUT SHEET, MONTHLY TO M84, FIVE CURVES  (D23)      |
|   one per payment archetype; computed ONCE; the workbook has NO cohort       |
|   triangle                                                                   |
+=============================================================================+
|            | Perfect | Occas.  | Altern. | Reducer | Early lapser |          |
|  weight    |   10%   |   35%   |   12%   |   13%   |     30%      |          |
|  pay prob  | p=.995  | p=0.93  | p=0.55  | p=0.97  | 0.60 falling |          |
|                                                                              |
|  EACH CURVE CARRIES, PER MONTH-SINCE-ORIGINATION m = 1..84:                  |
|     alive(m)         survival, from the archetype hazard                     |
|     contributing(m)  pays at full ticket                                     |
|     reduced(m)       pays at S29 reduced ticket                              |
|     gated(m)         cumulative share that has passed the run-of-6 gate      |
|                      == THE FIRST-ORDER TERM.  Stays a LIVE first-passage    |
|                         solve, NOT a lookup  (D22)                            |
|     never_gated(m)   persona H, the complement.  Full fee, zero benefit      |
|     tier(m)          from the TENURE -> TIER LOOKUP (D22):                    |
|                        Gold      at gate + 12                                |
|                        Platinum  at gate + 36                                |
|                        Sovereign  -- in the annual block only                |
|     grams(m)         cumulative, net of S31 / S32 / S33 leakage              |
|     card_active(m)   Gold+ and past M18, x S5 activation                     |
|     spend(m)         card spend base, before the segment multiplier          |
+=============================================================================+
                                    |
                                    v
+=============================================================================+
|   THE CONVOLUTION  --  this is the whole population engine  (D23)           |
|                                                                              |
|     book(s, X, t) = SUM over a of  weight(a)                                 |
|                     x SUMPRODUCT( acq(s, 1..t) , curve_a(X, t..1) )          |
|                     x segment_scalar(s, X)                                   |
|                                                                              |
|   SEGMENTS SCALE THE SAME CURVES.  Ticket and card-spend multipliers only.   |
|   No segment gets its own curve.  No cohort gets its own row.               |
+=============================================================================+
       |                              |                              |
       | contributing + reduced       | holding_not_contributing     |
       v                              v                              |
+---------------------------+   +----------------------------------+ |
|  FLOW: SIP contributions  |   |  STOCK: grams under custody      | |
+---------------------------+   +----------------------------------+ |
| contributing x ticket(s)  |   | + grams bought (SIP)             | |
| + reduced x reduced(s)    |   | + grams bought (SPOT)            | |
|   [S29, NOT hard-coded 20]|   | + Gold Rewards grams credited    | |
|            +              |   | - self-custody withdrawal (S31)  | |
+---------------------------+   | - redemption (S32, x S33 if      | |
|  FLOW: SPOT lane          |   |   lapsed-and-holding)            | |
+---------------------------+   |         |                        | |
| live x S45 attach x S47   |   |         v                        | |
|   freq x S46 ticket(s)    |   |    NET FLOW = inflow - outflow   | |
| + arrears-as-spot         |   |         |                        | |
| priced at the SAME tier   |   |         +--> MAX(0,-net) x price |  |
|   discount (D9)           |   |              x dealer spread     | |
| ONE rail event, no        |   |              = REDEMPTION COST   | |
|   collection failure      |   |              (zero when growing) |  |
|            |              |   |         |                        | |
|            v              |   |         x gold price (FLAT F1)   | |
|   Net = C x (f - c) - R   |   |         v                        | |
|   PER SEGMENT, PER LANE   |   |    AUM (USD)                     | |
|            |              |   |     +--> [STREAM 6] B2B fee      | |
|            +--> [STREAM 1]|   |     +--> custody COST (S14)      | |
|                 1a SIP    |   |     +--> credit collateral base  | |
|                 1b SPOT   |   |     +--> AML screening base      | |
+---------------------------+   +----------------------------------+ |
            |                                    |                   |
            v                                    |                   |
+=============================================================================+
|      SCORE MACHINERY  --  COLLAPSED AT v2.1  (D22)                          |
+=============================================================================+
|                                                                             |
|  LIVE ENGINE  --  eligibility is FIRST-ORDER, keep it exact:                |
|     run_length in [0,6]; +1 on a counted period; RESET to 0 on a miss;      |
|     FROZEN (not reset) during a regulatory block.                           |
|     Gate fires at run_length = 6.                                           |
|     ==> GATE ARRIVAL IS A DISTRIBUTION, NOT A DATE.  Run-of-6 first-passage |
|     ==> NEVER-GATED POPULATION (persona H) falls out of the same solve      |
|     Survival by payment archetype, monthly, on the lifecycle curve          |
|                                                                             |
|  COLLAPSED  --  the rate ladder is SECOND-ORDER:                            |
|     TENURE -> TIER LOOKUP, keyed on months since gate                       |
|         gate + 12  -> Gold                                                  |
|         gate + 36  -> Platinum                                              |
|         above      -> annual block only                                     |
|     x  ONE HEAVY-SELLER HAIRCUT, replacing the per-account Sold ratio       |
|                                                                             |
|     GONE: per-period Record / Standing / Retention arithmetic               |
|     GONE: the 1.80 / 2.05 / 2.10 rate ladder -> a FLAT GOLD RATE            |
|     MEASURED COST: 3.1% of gross profit at Y10, ~2% at Y7                   |
|                                                                             |
|  DEMOTED, NOT DELETED  --  the ICS Validation sheet:                        |
|     the FULL ICS formula and the NINE-PERSONA test set still specified,     |
|     still run, still must PASS.  The collapse is PROVED equivalent,         |
|     never assumed.                                                          |
|     5% SAFETY GATE: if the collapsed lookup's tier mix moves stream 2 by    |
|     more than 5% of gross profit in ANY year, the collapse is UNSAFE and    |
|     MUST BE REVERTED.                                                       |
+=============================================================================+
                                     |
        +----------------------------+----------------------------+
        v                            v                            v
+------------------+   +----------------------------+  +------------------------+
| BENEFIT COSTS    |   |  CARD LAYER (Gold+, M18)   |  | CREDIT LAYER (Gold+,M24)|
| (contra-revenue) |   +----------------------------+  +------------------------+
| Entry discount   |   | eligible x activation(S5)  |  | eligible x take-up(S8) |
|   0/.4/.8/1.2/1.5|   |   x spend x S38 tier mult  |  |   x LTV(tier) x S9     |
| Gold Rewards     |   |   x seasonality S52b       |  |   = PEAK drawn         |
|   -/-/.15/.45/.75|   |   x FLAT GOLD RATE 1.80%  |  |   x S40 TURNOVER 0.42  |
|                  |   |     (ladder collapsed,D22)|  |                        |
| Will discount    |   |   x PM_SHARE(S3)           |  |   = AVERAGE drawn      |
|   0/10/20/35/50% |   |   - F24 per-txn fee        |  |   VINTAGED BY STRUCK   |
| (LTV + card tier |   |     (11% of gross at Gold) |  |   LTV (D12)            |
|  cost nothing)   |   |   - S39 fraud, F25 dispute |  |         |              |
+------------------+   |   - F27 programme fixed    |  |         v              |
                       |         |                  |  |   [STREAM 5] 4 fee     |
                       |         v                  |  |   heads + interest     |
                       |  [STREAM 2] interchange    |  |   share, no credit risk|
                       |  [STREAM 4] FX(S34,S53)    |  +------------------------+
                       |    + ATM over-allowance    |
                       |    + issuance/replacement  |  +------------------------+
                       +----------------------------+  | [STREAM 3] family/will |
                                                       | accounts x S11 x price |
                                                       +------------------------+
                                     |
                                     v
+=============================================================================+
|  ACQUISITION COST  |  OPERATING COST   |  P&L            |  CASH & FUNDING  |
|  agent commission  |  10 blocks, F32   |  Revenue        |  EBITDA          |
|  referral (6mo lag)|  log-linear within|  - COGS         |  - tax (F33-F35) |
|  capped by the     |  block, step vs   |  - benefit costs|  -/+ float move  |
|  acquisition       |  scale classified |  - redemption   |  = free cash     |
|  budget ceiling    |  + legal & trust  |  - acquisition  |  = cumulative    |
|  (% of stream 1)   |  (D15, split out) |  - opex         |  = PEAK FUNDING  |
|                    |                   |  = EBITDA       |    and its month |
+=============================================================================+
                                     |
                                     v
     SOLVER 1: the fixed point revenue(N) = Opex(N) -- and the diverging-curve
               chart for the case where no crossing exists (D6)
     SOLVER 2: the SEVEN parked parameters (Section 9) -- not eight (D8)
```

### 2.2 Revenue streams at a glance

| # | Stream | Type | Base it scales with | Activates | Y1 est. | Y10 est. | Confidence in the rate |
|---|---|---|---|---|---|---|---|
| **1a** | **Entry fee margin — SIP** | Inflow | Gross SIP contributions, per segment | M1 | USD 2,630 | **USD −80,548** | Fee is client-stated; cost build-up is ours |
| **1b** | **Entry fee margin — SPOT** | Inflow | Spot volume, per segment | M1 | USD 1,294 | USD 10,771 | Attach/ticket/frequency all judgement (S45–S47); pricing rule corpus-settled |
| 2 | **Card interchange** | Activity | Spend × rate(tier) × PM share, **less per-txn fee** | **M18** assumed | 0 | USD 4,156,380 | Rate **verified** (Visa UAE IRF); **PM share unknown**; per-txn fee now modelled |
| 3 | **Family plan and Digital Will** | Headcount | Accounts × attach × price | M1 | USD 1,791 | USD 111,065 | Price is ours; cost floor verified |
| 4 | **Cardholder fees (FX, ATM, issuance)** | Activity | Foreign spend, ATM tail, events, net of tier waivers | **M18** | 0 | USD 2,226,204 | Market rate ~2%, converged across four comparables; foreign share is judgement |
| 5 | **Lending revenue share** | Activity + stock | **Average** drawn (peak × S40) and draw events | **M24** assumed | 0 | USD 12,135 | **Every rate unpriced.** Partner term sheet. **Falls 49× vs v1.0 — see §6.5** |
| 6 | **B2B platform fee** | **AUM** | Partner-customer AUM × bps | **M24**, build requirement from **M1** | 0 | USD 1,221,200 | **Placeholder 0.5–0.75%**; coupled to `INDIA_ENABLED` |
| **0** | **Redemption** | **Cost, mandatory** | Redemption events + net-outflow spread | M1 | (USD 0.19) | (USD 158) | F20 components sourced; VARA forbids any offsetting fee |
| | **Gross profit** *(the columns above sum here, not to gross revenue)* | | | | **USD 5,716** | **USD 7,657,206** | |
| | **Gross revenue** *(fees earned, before cost of revenue)* | | | | USD 13,212 | USD 8,150,081 | |
| | **Opex** | | | | (USD 1,031,907) | (USD 3,219,856) | |
| | **Net profit after tax** | | | | **USD −1,376,075** | **USD −367,051** | |

⚠ **The per-stream figures above are NET, so they sum to gross profit (USD 7,657,206 at Y10), not to gross revenue (USD 8,150,081).** The USD 492,875 difference is cost of revenue — fabrication premium, price-gap, float and rail — which sits inside stream 1. **Every share-of-revenue percentage in this brief is taken on gross profit for that reason; taking them on gross revenue puts them on the wrong denominator and they stop summing to 100%.**

**Stream 0 is new and it is a finding, not a line item.** v1.0 lists six revenue streams and no negative one. Redemption is a **mandatory, uncapped, zero-revenue cost line that scales with AUM**: VARA Annex 2 Rule III.E.4 forbids charging any fee on it, verified verbatim, so no offsetting revenue exists or can exist (`_working_parameter-completion-set.md` F20). At Base rates it is immaterial against terminal revenue — which is the reassuring finding. **It becomes material only in a stress scenario where the redemption rate spikes, and that is exactly when cash is scarcest.**

**There is no seventh revenue stream, and there can never be an exit fee.** VARA Annex 2 Rule III.E.4: an ARVA issuer granting redemption "shall process and complete redemption requests without charging any fees." Verified verbatim at primary source, correctly located in Annex 2 Part III.E clause 4. This is the constraint that shapes the entire design.

**Deliberately excluded, recorded so they are not re-proposed** (`Aurumix_Process_Maps_Revenue_Streams.md`): physical delivery and making charges (client instruction), insurance attach on the loan and SIP (client instruction), gold leasing for yield (refused despite being the largest margin line in the adjacent Indian market), FX margin on contributions (parked; GCC pegs make it thin until the Year 3+ non-pegged perimeter), a secondary-market premium (**decision 7: the premium is zero**, evidenced across nine protocols including two trading at a discount). **Added at v2.0:** the tenure rebate is **retired** by decision 44 and must not be re-proposed as a revenue or cost line (D8).

---

## 3. The engine, layer by layer

This is the section to argue with. Everything downstream is arithmetic. **Sign-off on this section is the gate on the build.**

Twelve layers at v2.0, against v1.0's eleven-in-name-and-six-in-substance. Layers 1–6 are rewritten; 7–10 are extended; 11–12 are new.

### Layer 1 — Acquisition

New accounts per month = `agent-driven + referral-driven + direct + partner-driven`, each allocated across the six segments by the **three-phase channel-to-segment mix matrix (S16)**, then subjected to logistic saturation and seasonality.

| Channel | Formula | Source | Note |
|---|---|---|---|
| **Agent** | `active_agents(t) × S12 × S17_ramp(months_since_joining)` | `100 G Business_Model.md` §11.1 (client's stated primary channel); ramp shape from insurance-agency practice | **Agent stock must be grossed up for attrition.** T7 gives 5→15→40→90→200 *active* agents. At S18 = 45%/yr, holding 200 active requires ~90 recruits/yr, each re-entering the ramp at 0.20. **v1.0 omits this entirely and overstates agent output by 15–20% at steady state** |
| **Referral** | `qualified_referrers(t) × S19 ÷ 12 × S20` | `_draft_referral-system.md` §5.4, §6 | **Structurally zero until M13.** A referrer must pass their own six-month gate and the referee must then pass theirs. **Two six-month gates in series means the channel does not reach steady state until roughly M25** |
| **Direct** | `monthly_spend(t) ÷ S15 + organic` | S24, S25, S26 | 🆕 **CAC is LINEAR in this model** (D27). `effective_CAC = S15`, a flat USD 120. **The convexity curve is retired to a scenario switch defaulting OFF and its calibration moves to Phase 5.** The brake on unbounded growth is the **saturation ceiling below**, not the CAC curve — see the note after this table |
| **Partner** | `partner_AUM(t)`, no account-level acquisition | S42, S43, S44 | Partner accounts **earn no ICS and consume no benefits** (`_draft_ics-scoring.md` §1.9). Track separately throughout — structurally the highest-margin book |

**The saturation rule, and it is the single most important structural fill in this layer** (S23):

```
new(s,t) = raw_demand(s,t)
         × [1 − cumulative_ever_acquired(s,t) ÷ (base(s) × ceiling(s))]
         × seasonality(month_of_year)                        [S52a]
```

**Use cumulative-ever-acquired, never live accounts, in the numerator.** A lapsed customer is a burnt lead, not a returned one. The two denominators diverge steadily with tenure — the ten-year run put the gap at roughly **5× by Year 10** — and the correct one is the mechanism that stops the model producing an implausible late-horizon hockey stick.

**Layer 1's output is a vector, not a triangle** (D23). This layer terminates in `a(s,t)` — new accounts by **region** by period — and nothing else. 🆕 **The regions that activate late (R2 at M7, R3 at M13, R4 on the switch) are handled by offsetting `a(s,t)`, never by giving them their own lifecycle curve.** A region that opens at M13 has zeros in `a(s,1..12)`; the convolution at Layer 2 then places its whole book 12 months to the right automatically. **Regions differ by ticket band and card-spend multiplier only. They do not differ by behaviour, and giving them separate curves would assert that they do without evidence.**

🆕 **R2's M7 activation is argued, not assumed** (D25, §5.4). Two reasons, both datable: the agent network is Indian and must recruit non-Indian agents before it reaches R2 at all, and CBUAE's Universal Account rollout is what makes the lowest band collectable. **Track the Universal Account as a dependency with a date rather than as a background assumption.**

**Three structural rules the S16 matrix encodes, which matter more than its cells:**

1. **The agent row must always be the most floor-weighted row.** Agents earn a percentage of a fee on a ticket, so on pure economics they should chase the standard band. They will not, because the floor band is where the accessible density is: labour accommodation, community organisations, employer payroll clusters. **This collides directly with §0.2: the agent channel delivers the band on which the fixed rail cost is spread over the smallest ticket. If the rail lands at UAEDDS pricing, the agent channel is the loss-making channel, and the model must be able to show that.** 🔴 **D25 adds a prior question: §5.4 finds that band may not have a direct-debit-capable account at all.**
2. **The B2B row is 60% R4.** Stream 6's natural partner set after the SEBI caution is Indian wallets and neobanks. **If `INDIA_ENABLED` is OFF, stream 6 must fall by roughly 60%, not stay flat.** v1.0 leaves the two switches independent and they are not.
3. 🆕 **No channel currently reaches R2, and the matrix must say so rather than imply otherwise** (D25). Until a non-Indian agent recruitment assumption is set, R2 arrives through direct and referral only, at a materially lower rate than R1.

🆕 **Why linear CAC is safe here, and where the risk actually moved** (D27). The failure mode a convex CAC guards against is a model that buys unlimited growth with money. **That brake is the saturation term above, not the CAC curve** — `new` is multiplied by remaining headroom against `base × ceiling`, so spend cannot manufacture accounts that the perimeter does not contain. The two mechanisms guard the same failure and the saturation one is sourced while the CAC one is not. **One genuine consequence remains and must be stated wherever the output appears: direct-channel LTV:CAC at high spend is an UPPER BOUND under linear CAC.** Promoted output 2 (§14.3) is LTV:CAC by channel × segment, so **the direct-channel cells carry that caveat explicitly**, and the `CAC_CONVEXITY` switch exists so the sensitivity can be shown on request. **CAC uncertainty still reaches the tornado through S15's own range (80 / 120 / 200), which is a level the tornado can rank rather than a shape it cannot.**

Seasonality is applied on a vector normalised to exactly **12.00** (S52a). **This is a hard build requirement: an un-normalised seasonality vector silently changes the model's annual answer**, which is one of the more common ways a monthly model goes wrong. Check formula at §12.

### Layer 2 — Lifecycle curves and the convolution

**This is the largest single change at v2.1, and it changes the engine's shape without changing a single one of its states** (D23).

#### 2a. The rule: no cohort triangle

⚠ **The workbook must not contain a cohort triangle.** v2.0 specified a six-state roll-forward **per segment × cohort × archetype** — 6 × 5 × 6 = 180 state rows, replicated once per acquisition month. On a 72-month monthly block that is a triangle of 72 cohorts, and it is the single largest reason v2.0's Model sheet ran to 600 rows × 76 columns. **It is also unnecessary**, because every cohort of a given archetype follows an *identical* path — the six-state machine is time-invariant in month-since-origination. **A triangle re-computes the same 84 numbers 72 times.**

#### 2b. Five lifecycle curves, monthly to M84

Compute each archetype's path **once**, on an input sheet, as a function of `m` = months since origination, for `m = 1..84`. Five curves, one per payment archetype (S27). Each curve carries eight series:

| Series | Contents | Driven by |
|---|---|---|
| `alive(m)` | Survival, all non-CLOSED states | Archetype hazard + background hazard (D3) |
| `contributing(m)` | Share paying at full ticket | The six-state machine at §2c |
| `reduced(m)` | Share paying at the S29 reduced ticket | S28 diversion, S30 multiplier |
| `gated(m)` | **Cumulative share that has passed the run-of-6 gate** | Run-of-6 first-passage solve. **A live engine, not a lookup** (D22) |
| `tier(m)` | Tier, from the tenure→tier lookup | Gate + 12 → Gold; gate + 36 → Platinum (D22, Layer 5) |
| `grams(m)` | Cumulative grams held, net of S31/S32/S33 leakage | Layer 6 |
| `card_active(m)` | Share Gold+, past M18, activated | S5 activation |
| `spend(m)` | Card spend base per active card, before the segment multiplier | S4, S38, S52b |

**M84 is the binding number and it is not arbitrary.** The M1 cohort reaches month 84 at the end of Y7. **No cohort in a 7-year model lives longer than 84 months**, so the curves need no extrapolation rule and v2.0's M120 extension is withdrawn. **The Lifecycle Curves sheet is the only monthly-to-M84 sheet in the workbook; the Model sheet is 29 columns** (§1).

#### 2c. The convolution — this is the population engine

The book in any period is the acquisition vector convolved against the curves:

```
book(s, X, t) = Σ_a  weight(a)
                     × SUMPRODUCT( acq(s, 1..t) , REVERSE( curve_a(X, 1..t) ) )
                     × segment_scalar(s, X)

  X            any of the eight series above
  acq(s,1..t)  the monthly acquisition vector for segment s, from Layer 1
  curve_a      archetype a's lifecycle curve, read backwards so that the
               OLDEST cohort meets the LATEST month-since-origination
  weight(a)    the S27 archetype weight
  segment_scalar(s,X)  ticket multiplier for flow series,
                       card-spend multiplier for spend series,
                       1.00 for every population series
```

**In Excel this is one `SUMPRODUCT` per series per period.** Worked example and the exact reversal convention at §10.4 Pattern 1.

**Three properties that make this equivalent to the triangle rather than an approximation of it:**

1. **Time-invariance.** Every state transition in §2d depends on `m`, never on `t`. Nothing in the six-state machine reads a calendar date. The one apparent exception is the card at M18, and it is handled on the *convolved* result — `card_active` is masked by `IF(t ≥ 18, …)` at the Model sheet, not inside the curve.
2. **Linearity.** Every series aggregates by addition across cohorts. A convolution is exactly the sum a triangle would take, in one row instead of 72.
3. **Regions scale, they do not diverge.** Regions differ by ticket band and card spend, both of which are multiplicative on the curve. **A region never gets its own curve**, and a later-activating region is handled by offsetting `acq(s,t)` (Layer 1). **If a future decision makes a region behave differently rather than merely spend differently, this equivalence breaks and the curve set must expand — say so at that point rather than quietly adding a scalar.**

🆕 **D25 changes what `segment_scalar` reads.** It is now a **band** scalar: each region contributes two ticket bands (S54, S55, §5.2), and the ticket and card-spend multipliers attach to the band, not to the region. **Eight bands across four regions, against v2.1's six segments, so the scalar count barely moves while both non-linearities are preserved.** ⚠ **Never apply a scalar built from a regional average ticket** — that is the specific error §5.2 exists to prevent, and it would flatten the card line by roughly 3×.

#### 2d. The six states, unchanged

**The states below are what the curves are computed *from*. Nothing in this taxonomy changes at v2.1** — the convolution is a change of representation, not of behaviour (D1 stands in full).

v1.0 ran `CONTRIBUTING → REDUCED → LAPSED`, with LAPSED terminal. **A lapsed account keeps its gold.** It holds a permanent ICS floor of 25 (`_draft_ics-scoring.md` §1.6 — "once you have made six payments, your score never falls below 25"), stays in the AUM stock, the custody-cost base, the B2B AUM base and the collateral base, and stays in continuous AML screening at USD 0.36/name/year indefinitely. **At the corrected persistency roughly 81% of every cohort sits in v1.0's "terminal" state by M61 — and the share is already above two thirds by M25, well inside the monthly block. v1.0 models the economics of the minority** (D1).

The real structure, recovered from `_draft_sip-rulebook.md` §8:

| State | Trigger | Gold | Clocks | Contributes | In AUM | In custody cost | In screening |
|---|---|---|---|---|---|---|---|
| `PRE-GATE` | run length 0–6, gate not passed | Held | **Run counter only. No score** | Yes, at full undiscounted fee | Yes | Yes | Yes |
| `CONTRIBUTING` | gate passed, paying | Held | Both advance | Yes | Yes | Yes | Yes |
| `REDUCED` | contribution cut — **free and unscored** | Held | Both advance | Yes, at S29 reduced ticket | Yes | Yes | Yes |
| `REGULATORY BLOCK` | compliance blocks the account | Held | **Both frozen; window extends** | No | Yes | Yes | Yes |
| `STOPPED` | investor cancels | Held | `Recent` decays, `Months` held | No | **Yes** | **Yes** | **Yes** |
| `DORMANT` | **12 consecutive silent periods**; SIP auto-cancels | Held | `Recent` decayed then held | No | **Yes** | **Yes** | **Yes** |
| `CLOSED` | grams = 0 | None | — | No | No | No | No |

**`CLOSED` is the only true absorbing state and the only exit from AUM, custody and screening.** Everything above it is revenue-bearing or cost-bearing or both.

**Five consequences to build:**

1. **A `holding_not_contributing` population** that feeds AUM but not contribution flow. Its omission **understates streams 2, 4, 5 and 6 in v1.0 and overstates nothing.**
2. **A hard absorbing boundary at 12 silent periods.** No account may decay through it. *"Dormancy is housekeeping, not a protection"* (`_draft_sip-rulebook.md` §8). **The single-hazard engine cannot express this.**
3. **A restart rate** from `DORMANT`/`STOPPED` back to `CONTRIBUTING`, **resuming at the decayed score.** *"Restarting is never a reset. A dormant or stopped account that restarts resumes from wherever decay left it. Nothing is re-earned, and nothing is forgiven either."*
4. **Split the hazard into voluntary and involuntary.** Corpus: **involuntary is 20–40% of total subscription churn, base 30%** (`_draft_sip-rulebook.md` §7.3). The two have different recovery behaviour — an involuntary lapse has a restart probability, a decided stop does not.
5. **The reduction diversion.** `S28` diverts 33% of would-be lapse events into `REDUCED`, **applied only to affordability-driven lapse** — the occasional-misser and reducer archetypes — **never to the early lapser or the background hazard.** Diverted accounts carry hazard multiplier `S30` = 1.35× (they have revealed affordability stress, but also revealed they would rather pay less than quit).

> 🔴 **The open client question this creates, and nobody has decided it: does a lapsed customer keep the card and the facility?**
>
> It determines whether **the card streams — 83.4% of Y10 gross profit — decay with persistency or are immune to it.** Measured: the switch moves **Y10 revenue by USD 3,393,774, a 42% swing** (8,150,081 → 4,756,308), and **cumulative net profit by USD 5,242,051.** v1.0 silently assumes immunity by never asking. Model as switch `LAPSED_KEEPS_CARD`, default ON (the design says nothing revokes it), and **report both.** This is the highest-value question in §16.

⚠ **Do not fold in these stale mechanics.** `_draft_sip-rulebook.md` §7.1 rows 4–5 and §7.2 bullets 3–7 carry pre-decision-46 vocabulary: **continuity-halving, arrears, revival, and "Tenure" as a score component are all dead** per decisions 46 and 46a. A miss now costs **8.33 points of Standing** and returns when the 12-month window rolls; there is no halving. *"A missed period is permanently missed, there is no arrears mechanism, and money arriving after grace is offered as a spot purchase."* Those sections are audit trail, not spec — see correction 18 at §15.

**Still live from §7.1/§7.2 and required in the build:** the 5-day grace with weekend-rolling; the month-boundary rule (*"a payment on 3 March for a 28 February date closes February. March still needs its own payment. A late payment can never close two periods."*); the "one accepted payment settles the period" convention; and the **hard USD 20 floor rejection** — a payment below the floor is *rejected and returned, nothing allocated*, and the request stays open for the full amount (F6).

### Layer 3 — Contribution flow, and the spot lane

Two lanes, not one. **v1.0 models no spot volume at all** — its Layer 3 is `contributing × ticket + reduced × 20` — while its own §9 asks the model to solve against "spot margin" (D9).

```
SIP lane, per segment s, period t:
  reduced_ticket(s)  = MAX(20, 0.50 × ticket(s))               [S29, NOT hard-coded 20]
  sip_inflow(s,t)    = contributing(s,t) × ticket(s)
                     + reduced(s,t)      × reduced_ticket(s)
  sip_events(s,t)    = contributing(s,t) + reduced(s,t)          [one rail event each]

SPOT lane, per segment s, period t:
  attaching(s,t)     = live_accounts(s,t) × S45 × tenure_uplift(s,t)
  spot_events(s,t)   = attaching(s,t) × S47 ÷ 12 × seasonality_spot(month)
  spot_inflow(s,t)   = spot_events(s,t) × S46 × segment_scalar(s)
                     + arrears_events(s,t) × ticket(s)           [arrears ARE spot]
```

**The reduced ticket is per-segment, not USD 20.** v1.0 hard-codes the floor. `S29`: reduction goes to **50% of prior ticket, floored at USD 20** — so S1 → USD 38, S2 → USD 20 (floored), S3 → USD 20, S4 → USD 20. **A USD 75 saver under affordability pressure halves to USD 40 far more often than they cut by 73%.** The floor is the *hard* minimum (F6), not the *observed* landing point. This raises reduced-state inflow ~40% for S1 against v1.0's treatment, and it moves margin: a USD 38 reduced ticket clears the S1 rail comfortably; a USD 20 one does not at Conservative rail cost. Correction 15 at §15.

**Spot pricing is settled, and it went the other way from v1.0's silence.** `_draft_sip-rulebook.md` §1.1 is authoritative on three independent grounds — it is a **self-labelled correction** that names what it fixes (*"a top-tier saver adding a lump sum currently pays the newcomer rate for giving Aurumix more money"*), it is **six days later** than `_draft_purchase-structure.md` §4.3, and **decision 44 ratifies it**. So:

| Attribute | Spot |
|---|---|
| Price | Base entry fee **less the account's tier discount** — identical to SIP |
| Earns ICS / counts to Confirmed SIP | **No** (`_draft_sip-spot-and-ics.md` §1) |
| Counts in Retention | **Yes, both numerator and denominator** |
| Credit LTV, card tier, family features | Not earned by spot; **applies to all grams once earned via SIP** |
| Exit | Buyback at the fix, no fee (III.E.4) |
| Time lever | **None. Retired** (decision 44) |
| Rail | Push or bank transfer, **no mandate, no collection-failure exposure** |

`_draft_purchase-structure.md` §4.1 ("flat, top of range") and §4.3 ("no entry-fee discount") are **superseded** — correction 14 at §15.

**Arrears money is spot volume, and this is a corpus rule not an assumption.** `_draft_sip-rulebook.md` §1 and §7.1: extra money inside a month is a spot purchase, and late money after grace is offered as a spot purchase. Size it from the archetype mix — occasional and alternating missers (47% of the base combined) generate ~0.9 missed periods per account-year between them, of which roughly 25–35% are made good. That is **~0.11 arrears events per live account per year at Base**, at the segment's own ticket. Small in value, free volume on an existing rail.

**Never blend the ticket across segments or lanes.** See §0.2. A blended USD 40 average across a USD 20 and a USD 75 population produces a materially different and wrong answer, because the fixed rail is spread over different bases.

### Layer 4 — Unit margin, per segment and per lane

🆕 **Re-cut at D31. The `− R` term is gone, and with it the non-linearity that shaped most of this section.**

```
Net = C × (f − c)                            [D31: the − R term is RETIRED]

  C = ticket size for this lane and segment
  f = entry fee rate, less this segment's TIER-WEIGHTED discount
  c = fabrication premium + price-gap risk        ** TWO terms at v2.6 **

  NOT in c, and why:
    payment rail (R)      -> grossed up onto the request and remitted.
                             Zero P&L effect.                      [D31]
    float cost of capital -> an OPPORTUNITY cost on equity, not a cash
                             expense.  Memo line, never COGS.      [D32]

  Collection request issued to the customer = C + R
```

🔴 **`c` has gone from four terms to two in one day. Both removals are defensible and neither reduced a real cost** — see the pattern note in the front matter. **Treat `c = 2.29%` as the most fragile number in this brief**, not the most settled one.

Source: `_parked_collection-economics-and-minimum-ticket.md` §2, **with its `R` term retired by D31.**

🔴 **This is the single largest simplification D31 buys, and it deserves stating plainly: unit margin is now LINEAR in ticket size.** The whole reason the model computes margin per segment at that segment's own ticket was `R` — a fixed cost spread over a variable base. **With `R` at zero, margin as a percentage is identical at every ticket**, and a USD 20 saver is exactly as profitable per dollar as a USD 75 one.

⚠ **Do not delete the per-segment margin computation on the strength of this.** Two other non-linearities survive and still require it: the **tier-weighted discount** varies by segment through the archetype mix, and **card spend** is keyed to ticket as an income proxy (D25 built the ticket bands on *both* the rail and the card non-linearity — only the first one dies here). **§5.2's two-band structure stands on the card leg alone now, which is a thinner justification than it had, and §5 should say so.**

**The spot lane and the SIP lane now earn the same percentage margin.** At the Y1 5% fee:

| Line | SIP, USD 75 | Spot, USD 620 |
|---|---|---|
| 🆕 Gross margin (5% fee less **1.50%** premium, 0.79% price-gap) — **re-cut at D28, D32** | **2.79% → USD 2.09** | **2.79% → USD 17.30** |
| 🆕 Rail — **PASSED THROUGH, not deducted** (D31) | — | — |
| 🆕 Float cost of capital — **MEMO LINE, not deducted** (D32) | — | — |
| **Net margin** | **USD 2.09** | **USD 17.30** |
| **Net margin as % of ticket** | **2.79%** | **2.79%** |
| 🆕 **At Conservative rail (S1 = USD 1.36)** | **unchanged — USD 2.09** | **unchanged — USD 17.30** |

🔴 🆕 **D31 REVERSES the headline claim of this subsection, and D28 had already reversed it once.** The sequence is worth keeping straight because it has now moved twice:

| | Claim about spot | Status |
|---|---|---|
| **v1.0 / v2.0** | *"Spot is the only inflow-linked flow that survives the adverse rail"* — the SIP went negative at −USD 0.82 | **Withdrawn by D28** |
| **v2.4** | *"Spot remains structurally the highest-margin inflow in the business"* — 2.25% vs 1.96% | 🔴 **Withdrawn by D31** |
| **v2.5** | **Spot and SIP earn an identical 2.79%.** The entire gap between them *was* the fixed rail over an 8.3× larger base, and it was never a property of spot itself | **Current** |

**The rail is no longer a scenario axis for stream 1 at all.** Base, Aggressive and Conservative S1 now produce identical stream 1 margin. ⚠ **S1 does not leave the model — it moves from a margin driver to an adoption-risk driver** (§13.3, `RAIL_PASSTHROUGH`), and that is a real relocation rather than a deletion: at the Conservative rail the customer is asked for USD 21.36 instead of USD 20.00, and whether they say yes is now the question.

Two qualifications that keep this honest. **Spot earns no ICS**, so it builds no tier, no card eligibility and no credit eligibility — **it is margin without a funnel**, and v1.0's §0.4 conclusion that the SIP is an acquisition mechanism for the card still holds. And spot volume is lumpy and seasonal, so it cannot be relied on to cover a fixed cost base. **Spot improves the margin on stream 1; it does not change what the business is.**

**Two spot constraints to build as rules, not costs.** Above roughly one bar denomination, **procure directly rather than drawing the float** — *"a single order larger than the float would breach the backing invariant and halt minting for everyone else"* (`_draft_purchase-structure.md` §4.2). At a Year 1 float of ~USD 28k, a USD 100,000 order **breaches it by 3.5×**, so the two-step quote mechanism is live from launch, not a Year 3 concern. And the **AED 50,000 AANI per-transaction cap** routes large tickets to domestic transfer or wire, with enhanced due diligence and source of funds — a different cost and a different friction from the SIP rail. Travel Rule data applies above AED 3,500.

### Layer 5 — The gate as a live engine, the score collapsed to a lookup

**The measurement that decides this layer, and it is why the collapse is safe** (D22). Replacing the full tier ladder — interchange at 1.80% Gold / 2.05% Platinum / 2.10% Sovereign — with a **flat Gold rate** moves stream 2 by **3.1% of gross profit at Y10**, and by only **~2% at Y7**, because Sovereign is **1.2% of tiered accounts** at that point. Doing the same thing to *eligibility* — assuming 100% of live accounts are Gold+ when the computed figure is **63%** — **overstates the business by ~59%.**

🔴 **The rate ladder is second-order. Eligibility is first-order.** That asymmetry, not a preference for simplicity, is the entire argument for what follows.

| | Kept as a live engine | Collapsed to a lookup | Demoted to validation |
|---|---|---|---|
| **What** | Survival by payment archetype; the six-consecutive-payment gate as a run-of-6 first-passage solve; months-since-gate driving **Gold at +12** and **Platinum at +36**; the never-gated population (persona H) | The per-period `Record` / `Standing` / `Retention` arithmetic → a **tenure→tier lookup**, plus **a single haircut for heavy sellers** replacing the per-account `Sold` ratio | The **full ICS formula** and the **nine-persona test set** |
| **Why** | It sets who is eligible, and eligibility is worth ~59% of the business | It sets the rate within eligibility, and that is worth ~2% at Y7 | So the collapse is **proved** equivalent rather than assumed |
| **Where** | Lifecycle Curves sheet, monthly to M84 (Layer 2) | Lifecycle Curves sheet, `tier(m)` series | **ICS Validation sheet** (§12) |

#### 5a. What was wrong with cohort averaging, and why it still matters

**v1.0's proudest claim — "tier distribution is an output, never an assumption" — is false as specified** (D2). ICS is `MAX(25, MIN(Record, Standing) × Retention)` followed by a **threshold lookup** at 25/50/75/100. Tier is a non-linear step function of an *individual's* history. v1.0 computes one set of values per segment-cohort — the cohort's *average* `Recent` and *average* `Sold`, thresholded. **By Jensen's inequality that is wrong, and biased upward.**

Worked, in one line: a cohort half perfect payers (`Recent` = 12) and half alternating missers (`Recent` = 6). **Average-then-threshold** gives mean `Recent` 9 → Standing 75 → **100% Platinum**. **Threshold-then-average** gives **50% Platinum and 50% Gold-capped-for-life**. v1.0's own text names the alternating misser as *"a real, permanently occupied cell in the distribution"* and then specifies a structure with no cell to put it in.

⚠ **The collapse at v2.1 is not a return to cohort averaging, and the difference is the whole point.** Cohort averaging averages *behaviour* and then thresholds it, which destroys the heterogeneity that decides eligibility. **The tenure→tier lookup is applied per archetype curve, then weighted** — the D2 rule, "threshold per track then weight," is preserved exactly. What is dropped is the per-period arithmetic *inside* each track, which is deterministic given tenure and therefore adds nothing a lookup cannot carry. **Averaging across archetypes remains forbidden.**

#### 5b. The pre-gate block — kept in full, unchanged

`_draft_ics-scoring.md` §1.6a: *"the engine tracks the **current run length** (0–6) before the gate, not a score and not Months. Months and Recent both begin at the first month of the qualifying run (§1.6), so on opening day they are 6 and 6 by construction."*

```
run_length ∈ [0,6],  integer, PER ARCHETYPE CURVE  (not per cohort — D23)
  +1        on a counted period
  RESET 0   on a miss
  FROZEN    during a regulatory block  (not reset — D5)
  GATE      fires when run_length = 6

gated(a, m)  = cumulative share of archetype a that has gated by month m
             = the run-of-6 FIRST-PASSAGE solve in p(a), applied with survival
```

**The structural consequence v1.0 misses entirely.** Under v1.0, everyone surviving to month 6 is Silver at month 6. Under the real rule, a member who misses month 4 does not gate until **month 9 at the earliest**. **Gate arrival is a distribution, not a date** — a run-of-6 first-passage problem in the monthly payment probability `p`. The model must compute it, not assume it. **This shifts every downstream ladder date right: Gold, card eligibility and credit eligibility all move by the expected gate delay.** See §10.3 for the worked first-passage table by archetype.

🔴 **This is the first-order term and it is the one thing in this layer that must not be simplified.** The cohort-weighted mean gate month is **M8.1** and the ever-gate share is **53.5%** — against v1.0's assumption that everyone gates at M6. **Assuming universal gating overstates the business by ~59%**, which is roughly thirty times the cost of collapsing the rate ladder. **`gated(a,m)` is computed, never assumed, and it is computed monthly.** It resolves inside the monthly block (§1).

**Two populations v1.0 has no cell for:**

- **Never-gated (persona H).** *"Six real payments, three years of intermittent saving, and the account has no score and no tier because no six landed in a row."* This account pays the **full undiscounted entry fee**, holds gold, generates AUM and custody cost, and consumes **zero benefits, forever.** **Structurally these are the highest-margin retail accounts in the book.** v1.0 understates stream 1 margin and overstates benefit cost by omitting them.
- **The zero-benefit paying window.** Months 1–5 pay the full fee and receive nothing — no score, no tier, no discount — and longer if the run breaks. **Report months of full-fee revenue per cohort before the first discount is outstanding.** Accepted at `_draft_ics-scoring.md` §10.

**The asymmetry to reproduce:** *"pre-run gold counts in Retention's denominator, while pre-run payments score nothing."* Grams bought before the gate enter Retention's denominator, so selling them later costs score that those purchases never earned.

#### 5c. The collapse — a tenure→tier lookup and one haircut

**What runs in the live model** (D22):

```
TENURE -> TIER LOOKUP,  keyed on months since gate,  PER ARCHETYPE CURVE

  months_since_gate < 12          ->  Silver
  months_since_gate >= 12         ->  Gold
  months_since_gate >= 36         ->  Platinum
  above Platinum                  ->  resolved in the ANNUAL block only

  not gated                       ->  NO TIER    (persona H, no benefits, full fee)

Then, once, on the resulting mix:

  HEAVY-SELLER HAIRCUT  =  a single multiplier demoting the share of the book
                           that sells past the 30% allowance,
                           replacing the per-account `Sold` ratio entirely
```

**What that removes.** The per-period `Record`, `Standing`, `Retention` and `ICS` rows are gone from the live model — four rows per track per period, which on a 30-track engine was the largest single row band in v2.0's workbook (§10.1). **They are gone because, given the archetype and the tenure, every one of them is deterministic.** A lookup carries the same information in one row.

**What that changes, measured, not asserted:**

| Effect | Y10 | Y7 | Why |
|---|---|---|---|
| Flat Gold rate replacing the 1.80/2.05/2.10 ladder, on stream 2 | **3.1% of gross profit** | **~2%** | **Sovereign is 1.2% of tiered accounts at Y7.** There is very little at the top of the ladder to mis-price |
| Assuming 100% Gold+ eligibility instead of computing it | — | **overstates the business by ~59%** | **63% of live accounts are Gold+.** This is why eligibility stays a live engine |

**One archetype-specific consequence to keep.** The alternating misser's `Recent` pins at 6 forever, so under the full formula it is **capped at Gold for life** — it never reaches Platinum however long it survives. **The lookup must reproduce that cap**, which it does by keying the archetype's own curve rather than a blended tenure: the alternating-misser curve's `tier(m)` returns Gold from gate + 12 and never advances. **A single blended tenure→tier table across archetypes would lose this and would drift the mix upward, which is the D2 error in a new costume.**

⚠ **The heavy-seller haircut is an aggregate, and it is looser than the rule it replaces.** The real `Retention` term is per account and kinks at 30%; a single multiplier on the mix cannot represent the kink. This is accepted as limitation **L11** (§3.y.3) and it is the reason the 5% safety gate below exists.

#### 5d. Demoted, not deleted — the ICS Validation sheet and the 5% safety gate

🔴 **The full ICS formula and the nine-persona test set are not removed from the specification. They move from the engine to the validation layer, and they must still pass.** The collapse is *proved* equivalent, never assumed.

**The full formula, still specified, still built, on the ICS Validation sheet:**

```
Months  = counted periods since the qualifying run began. Starts at 6 on gate day.
          Never falls, for any reason.
Recent  = counted periods in the trailing 12 countable months (0 to 12).
Sold    = 1 − (grams now) ÷ (grams 12 countable months ago + grams acquired since)

Record   = (100/24)  × Months                for Months ≤ 12
         = 50 + (100/96) × (Months − 12)     for 12 < Months ≤ 60
         = 100                               for Months > 60
Standing = (100/12)  × Recent
Retention= 1                                 for Sold ≤ 30%
         = 1 − (Sold − 30%) ÷ 70%            for Sold > 30%

ICS = MAX(25, MIN(Record, Standing) × Retention)      once the gate is passed
```

Source: `_draft_ics-scoring.md` §1.3, §1.4, §1.5. Tiers: Silver 25, Gold 50, Platinum 75, Sovereign 100. Below the gate there is **no score at all**, which is why the bottom rung is named "No tier."

⚠ **Use exact fractions, never the rounded decimals.** `8.3333 × 6 = 49.9998`, which falls below the Gold threshold of 50 and **silently misfiles the entire alternating-misser population into Silver** — 12% of the book, and the cell that carries the most profitable card economics. Write `100/12` and `100/24`, not `8.3333` and `4.1667` (D4). **This is a validation-sheet requirement now rather than a Model-sheet one, and it is exactly as binding**: the collapse is checked against this formula, so an error here corrupts the check rather than the answer, which is worse.

**Four rules the Sold denominator forces** (`_draft_ics-scoring.md` §1.5), all cheap and all required on the validation sheet:

| Case | Rule |
|---|---|
| Denominator is zero (no gold, none acquired) | `Sold = 0`, `Retention = 1` |
| Grams credited by **Gold Rewards** | Count as **acquired**. They enlarge the denominator, so a reward never creates or reduces a penalty |
| **Transfers to a family sub-account or under the Digital Will** | **Not a sale.** Excluded from the numerator; arrives in the recipient's account as an acquisition |
| **Lender liquidation on a margin call** | ✅ **Counts as a sale** (settled 2026-08-13). The alternative makes borrowing a route around Retention |

**The nine personas A–I still run and still must return the corpus's stated Record, Standing, Retention, ICS and Tier. Nine TRUEs or the build does not ship.** Personas H and I remain the two a naive build fails.

> 🔴 **THE 5% SAFETY GATE — the condition under which this collapse must be reverted.**
>
> ```
> FOR EACH YEAR y IN Y1..Y7:
>   stream2_collapsed(y)  = stream 2 on the tenure->tier lookup
>   stream2_full(y)       = stream 2 on the full ICS formula, same book
>   delta(y)              = ABS( stream2_collapsed(y) - stream2_full(y) )
>                           / gross_profit(y)
>
> GATE:  MAX over y of delta(y)  <=  5%
> ```
>
> **If the collapsed lookup's tier mix moves stream 2 by more than 5% of gross profit in any year, the collapse is unsafe and must be reverted** to the per-period ICS engine. **This is a workbook check, not a review item** — it lives on the Checks sheet, it returns TRUE/FALSE, and it is included in the master flag (§10.6, §12).
>
> **The measured headroom is comfortable but not large.** The ladder collapse costs 3.1% of gross profit at Y10 and ~2% at Y7 against a 5% tolerance. **The gate is therefore live rather than ceremonial**, and the parameter most likely to trip it is anything that enriches the top of the tier mix — a higher perfect-payer weight, a lower background hazard, or an Aggressive archetype mix. **Run the gate under Base, Aggressive and Conservative.**

#### 5e. The archetype tracks — what the curves are computed from

Five payment archetypes (S27), each with its own **deterministic lifecycle curve**, crossed with the withdrawal split (S31) that straddles the 30% Retention kink. **Threshold each track, then weight. Never average then threshold** — the D2 rule survives the collapse in full (§5a).

| Archetype | Weight (Base) | Monthly pay prob. | Own hazard | Total monthly attrition | Terminal tier |
|---|---|---|---|---|---|
| **Perfect payer** | 10% | 0.995 | 0.000 | 0.016 | **Sovereign-capable — the only one.** Earliest arrival M61, so **resolved in the annual block** under the collapsed ladder (D22) |
| **Occasional misser** | 35% | 0.93 | 0.007 | 0.023 | **Platinum ceiling.** Misses ~1 month a year; Standing halves and rebuilds |
| **Alternating misser** | 12% | 0.55 | 0.018 | 0.034 | **Gold, capped for life.** `Recent` holds at 6 forever |
| **Reducer** | 13% | 0.97 at reduced ticket | 0.002 | 0.018 | By payment record. **Lowest attrition of any non-perfect archetype** — the point of the free unscored reduction |
| **Early lapser** | 30% | 0.60 falling | 0.200 | 0.216 | Silver floor or never gated. ~90% gone by M13 |

**Aggressive mix** (fits 65% M13): Perfect 29%, Occasional 26%, Alternating 16%, Reducer 8%, Early lapser 21%; background hazard **1.1%/month**.
**Conservative mix** (fits 45% M13): Perfect 14%, Occasional 24%, Alternating 16%, Reducer 10%, Early lapser 36%; background hazard **2.4%/month**.

**The alternating misser is a revenue-relevant cell, not a curiosity.** At 12% of the book with a Gold-for-life cap, it is roughly a quarter of the steady-state Gold population — spending at the **lowest interchange rate (1.80%)** and the **highest FX margin (2.0%)**, i.e. **the most profitable card cell in the book, because it generates stream 4 revenue that the higher tiers have waived.** ⚠ **Under the collapsed ladder its interchange rate is the flat Gold rate, which is the rate it was already on** — the cell that carries the most card profit is the one the collapse touches least. That is a large part of why the measured cost is 3.1% and not more.

**Rejected: Monte Carlo.** Wrong deliverable for a client Excel workbook, unauditable, and unnecessary once the archetypes are discrete and deterministic (D2).

#### 5f. Regulatory block re-indexes both clocks

`_draft_ics-scoring.md` §1.9 and §10 sub-decision 3 (settled): *"**Frozen months are skipped entirely and the window extends to reach twelve countable months** … on both clocks and on both sides of the gate."*

**This is not pause-and-resume, it is re-indexing.** `Months` and `Recent` advance on **countable** months only; the trailing window looks back until it has accumulated 12 countable months, however many calendar months that spans. It applies pre-gate too: *"a saver at 4-of-6 who enters a compliance pause resumes at 4-of-6."*

**Materially an S5 (India) input** — the block fires on the returning-NRI event. Needs a repatriation rate; **nothing in the corpus sizes it.** Flag as exogenous.

> 🔴 **Open decision, live, as a switch.** `_draft_ics-scoring.md` §10 sub-decision 2, left open at Abdur's instruction 2026-08-13: *"a compliance-forced exit (the returning NRI, decision 31) drives Retention to zero for something the customer did not choose."*
>
> **OFF (current design):** a forced exit drives Retention to 0 → ICS to the Silver floor of 25 → strips card, credit and Gold Rewards eligibility. **On the segment most likely to be forced out, the model destroys the tier distribution.**
> **ON (proposed extension):** the grams leave, the score does not move.
>
> **Model OFF as base and report the S5 tier-distribution delta under ON as the client's decision cost:** `{{UNFILLED: S5 tier-distribution delta, sub-decision 2 ON vs OFF, Y10 — not in spine}}`.

Note the design inconsistency the corpus itself flags: a **forced sale** and a **margin-call liquidation** are both sales the customer did not pick the day of, and the design currently answers them differently. If the client resolves sub-decision 2, settled item 1 may move too — and a margin-call liquidation currently costs the borrower three tiers, which feeds back into streams 2, 4 and 5.

### Layer 6 — AUM stock, with the redemption and self-custody taxonomy

```
Grams(t) = Grams(t−1)
         + sip_grams(t) + spot_grams(t) + rewards_credited(t)
         − self_custody_out(t)                  [S31 distribution, NOT an aggregate]
         − redeemed_grams(t)                    [S32, × S33 for lapsed holders]

net_flow_grams(t) = sip_grams(t) + spot_grams(t)
                  − self_custody_out(t) − redeemed_grams(t)

AUM(t)   = Grams(t) × gold_price                [gold price FLAT, F1 — see §8.1]

redemption_spread_cost(t) = MAX(0, −net_flow_grams(t)) × gold_price × dealer_two_way_spread
redemption_handling(t)    = redemption_events(t) × F20
```

**The taxonomy, to state once and never conflate again** (D10):

| Event | What moves | Cost to Aurumix | Hits ICS `Sold`? |
|---|---|---|---|
| **Redemption** | gold → cash | **No fee permitted** (III.E.4). Dealer spread on **net** outflow only, plus F20 per event | **Yes** |
| **Self-custody withdrawal** | gold → customer wallet | Gas only. Free to Aurumix | **Yes — identically** |
| **Lapse** | nothing | Zero. **The balance is unaffected** | **No** |

**v1.0 has `− redeemed(t)` in the stock equation with no driver anywhere in the assumptions register, so the term evaluates to zero.** `_draft_purchase-structure.md` §5.4 supplies the logic that replaces it: *"The obvious objection to III.E.4 is that Aurumix must pay the dealer's bid-ask spread on every exit and cannot charge for it. **That objection assumes gross exits drive physical sales. They do not.**"*

| Book state | Inflow | Gross exits | Net | Physical gold sold |
|---|---|---|---|---|
| **Growing** | 8% of AUM | 3% | +5% | **None.** Float absorbs |
| **Flat** | 4% | 4% | 0% | **None.** Float absorbs |
| **Shrinking** | 2% | 6% | −4% | Yes, on the 4% net only |
| **Run** | 1% | 25% | −24% | Yes, in size, at bid, into a falling market |

*"In the first two rows, which is where a growing product lives, the zero-fee rule costs nothing. The cost of the redemption promise is the dealer spread on **net** outflow, not on gross exits, and it is bounded by the float's capacity to warehouse the difference."*

The mechanism behind it, §5.3 stage 8: *"**Stage 8 is the point of the whole design.** An exit does not sell gold. It returns grams to the float. The next buyer consumes them. The treasury only touches the physical market when the float breaches a band."*

**So: a new P&L line, `MAX(0, −net_flow) × gold_price × dealer_two_way_spread`, zero in every month the book grows.** The four book states become a first-class scenario axis (§13); **the Run row is a stress test, not a scenario.**

⚠ **Two conditions v1.0 does not carry.** The §5.4 affordability argument **assumes Aurumix owns the float** — under the recommended dealer-carried launch (S51) it requires *"a second commitment"* from the dealer to take grams back on demand. And §5.1 leaves the spread incidence to counsel: *"III.E.1 says 'equal value.' The safe reading is the full prevailing value of the underlying grams with no haircut. An arguable reading is realisable value, that is, the dealer's bid. **The difference is the entire two-way spread and it decides who absorbs it on every exit.**"* Model the safe reading; expose the switch (§16).

**The lapsed-holder decay term, which v1.0 has no line for at all.** At 19% M61 persistency, **81% of ever-acquired accounts are lapsed by Year 6.** A lapsed holder has no accruing tier to protect — their `Record` is frozen, their `Standing` has decayed — so the Retention penalty costs them nothing they still value. *"The one thing holding them in is inertia, and inertia is not a 10-year assumption."* Apply `S33` = 2.2× to both S31 and S32 for this population. **The lapsed book, not the contributing book, is the dominant AUM decay term from roughly Year 4** — and AUM drives stream 6, custody absorption and the entire credit collateral base. `Aurumix_Process_Maps_Custody_Fee.md` identifies exactly this population as the one that *"still holds gold, still costs money to store, and the cash touchpoint is gone."*

**Leakage must be a distribution, not a rate.** An aggregate leakage rate cannot produce a Retention distribution: 12% of AUM leaving could be 100% of accounts withdrawing 12% (Retention 1.000 for everyone, **zero** tier impact) or 12% of accounts withdrawing 100% (those accounts to the floor). **Same S10, completely different tier distribution.** So the model carries S31's six buckets, deliberately straddling the 30% kink:

| Bucket | Base weight | Aggressive | Conservative | Midpoint used |
|---|---|---|---|---|
| 0% (never withdraws) | 48% | 60% | 26% | 0.00 |
| 1–10% | 22% | 21% | 17% | 0.05 |
| 11–30% (**at or below the kink**) | 16% | 12% | 19% | 0.19 / 0.18 / 0.22 |
| 31–60% (**Retention starts falling**) | 9% | 5% | 19% | 0.44 / 0.42 / 0.45 |
| 61–99% | 3.5% | 1.5% | 13% | 0.78 / 0.75 / 0.80 |
| 100% (full exit) | 1.5% | 0.5% | 6% | 1.00 |
| **Weighted aggregate leakage** | **12.3%** | **6.9%** | **30.0%** | vs S10 target 12 / 6 / 30 |
| **Share above the kink** (Retention < 1.0) | **14%** | **7%** | **38%** | — |

**The output that matters is the last row, not the aggregate. Only 14% of the base takes any Retention haircut at Base, so the Retention multiplier is close to inert in the Base case and is a genuine tier-suppressant only in the Conservative case.** That is a finding: **the 30% allowance is set generously enough that Retention does almost no work at Base assumptions.** If the client wants Retention to bind, the allowance has to come down — but that is a design change, not a modelling one.

### Layer 7 — Activity revenue

Three streams fire off the tier distribution and the card/credit populations, all conditionally activated. Detail at §6.2, §6.4, §6.5.

```
eligible_card(t)   = accounts at Gold tier or above,  from M18
active_cards(t)    = eligible_card × S5 activation
spend(t,tier)      = active_cards(tier) × S4 × S38_tier_multiplier(tier)
                     × S52b seasonality(month)
gross_interchange  = Σ_tier [ spend(tier) × F12_rate(tier) ]
txn_count(t,tier)  = spend(t,tier) ÷ F23_avg_ticket(tier) × 1.06   [+6% declines]
STREAM2(t)         = gross_interchange × S3 PM_SHARE
                     − txn_count × F24                              [per-txn fee]
                     − spend × S39 fraud bps
                     − disputes × F25
                     − F27 programme fixed costs                    [contra, not opex]
```

**The per-transaction fee is the largest single correction in the card block, and v1.0 flagged it without closing it.**

| Tier | Avg ticket (F23) | F24 as % of value | Gross rate (F12) | **Per-txn fee as % of gross interchange** |
|---|---|---|---|---|
| Gold | AED 185 | 0.199% | 1.80% | **11.0%** |
| Platinum | AED 240 | 0.153% | 2.05% | **7.5%** |
| Sovereign | AED 310 | 0.118% | 2.10% | **5.6%** |

**The processor fee is a regressive tax on the lowest tier, and it stacks the wrong way with PM share.** At the Conservative 55% PM share, Gold's net interchange is `1.80% × 0.55 − 0.199% = 0.791%`, which is **44% of gross rather than the headline 55%. The effective PM share on small tickets is materially below the contracted PM share, and the model must compute it per tier rather than applying S3 flat** — on **54.3% of terminal gross profit.**

**Tier spend multipliers must be applied, not blended away** (S38). Interchange rates differ by tier *and* FX margins differ by tier *and* ATM allowances differ by tier. Applying a blended spend to a blended rate double-counts the mix effect in stream 2 and **gets the sign wrong in stream 4, because the tier that spends most is the tier whose fees are most waived.** Normalisation check at the Y10 tier mix (Gold 55% / Platinum 30% / Sovereign 15% of cardholders): blend = 1.018, i.e. AED 6,108 against the AED 6,000 target — **1.8% over, within tolerance.** At the Y5 mix (62/38/0) it reads AED 5,604 and at Y3 (78/22/0) AED 5,316, which is the correct direction: **early-year blended spend must sit below the terminal blend because the mix is bottom-heavy.** v1.0's flat AED 6,000 across all years overstates Y3–Y5 interchange by roughly 8–12%.

**Stand-in fraud is bounded and computable, and it cannot be closed.** `_draft_credit-and-card-infrastructure.md` §5.1: two independent fallbacks approve transactions **with no collateral check at all** — the processor's Commando Mode (invoked when Aurumix is unreachable, from pre-agreed static rules we write) and the network's STIP (invoked when the processor is unreachable, unilaterally, notifying afterwards). *"In both paths we learn about the spend after the fact. **This is an unavoidable, permanent hole in a collateral-backed card programme.**"*

The recommended Commando Mode caps — **USD 250/txn, max 3 transactions, USD 500 cumulative, no ATM, no cross-border** — make the per-account worst case deterministic. Only the incident rate is unknown. `stand_in_loss(t) = exposed_accounts × USD 500 × incident_rate`. ⚠ Note the caps also **remove ATM and cross-border from stand-in**, which slightly reduces stream 4.

**Credit carries vintages, not a balance** (D12). `_draft_credit-and-card-infrastructure.md` §6.4: *"A term loan matures. A card balance revolves indefinitely. Without a review, a customer struck at Sovereign 80% who has since fallen to Silver keeps borrowing at 80% forever, and the tier ladder stops binding on the largest benefit in the product."* The recommendation is an **annual facility review**: the limit re-strikes to the current tier of record, but **existing drawn balances run to term at the originally struck LTV**, preserving the no-margin-call-on-a-tier-fall promise. So the model carries a **vintage of drawn balances by struck LTV**, not one balance at the current tier — and Layer 5 says Sovereign is "rented by conduct," so the tier moves constantly.

**Turnover is one of two corrections, and it is the smaller one.** v1.0's `drawn(t) = facility_limit × take_up × drawn_pct` computes **peak** drawn and then applies an annual interest rate as though the balance persisted. **Manappuram's realised tenor is 71 days against a 6–12 month product**, so a borrower who draws to 50% of limit holds that balance for ~2.3 months, not 12. `S40 = 0.42` converts peak to average: 71 ÷ 365 = 0.195 of a year per draw event, × S41 = 2.1 draws/yr gives 0.41, rounded up to 0.42 because a revolving card-style facility sits somewhat above a pawnbroker's episodic pattern. **Origination fees are per-event and therefore rise with turnover, so they are not scaled by S40.** Correction 16 at §15.

🔴 **The larger correction is the collateral base, and it is easy to miss.** Only Gold+ accounts can borrow, but **AUM is spread across all HOLDING accounts** — and at 19% M61 persistency the holding book is roughly **3× the live book.** v1.0 credits the Gold+ population with a share of *total* AUM, as though the lapsed book's gold were theirs to pledge. Computing the collateral base per holding account instead is a **2.96× fall**, against turnover's 1.88×. **Together they take stream 5 from USD 70,035 to USD 12,582 at Y10; the gap from there to v1.0's ~USD 600,000 is v1.0's own AUM overstatement.**

⚠ **S40 and S41 must not be flexed independently.** Raising S41 raises origination revenue linearly but also raises S40, so the two move together.

### Layer 8 — Benefit costs (contra-revenue)

Detail at §7.2. Five benefits, three of which are real cash costs and two of which are revenue-positive.

**The pre-gate block changes this layer's arithmetic.** Never-gated accounts (persona H) consume **zero benefits forever** while paying the **full undiscounted fee**. The zero-benefit paying window — months 1 to 5, longer if the run breaks — means every cohort has a period of full-fee revenue before its first discount is outstanding. **v1.0 has no cell for either and therefore overstates benefit cost and understates stream 1 margin.**

**Gold Rewards is capped at the interchange and credit revenue that customer generated, net of their custody cost**, so if `PM_SHARE ≥ 36%` it can never exceed its funding line by construction (`_draft_credit-and-card-infrastructure.md` §8.2, arithmetic verified: 0.75 ÷ 2.10 = 35.7%). Model it as a **haircut on stream 2**, not as an independent cost. The Checks sheet must verify the cap never goes negative.

**The launch-year cost of the entire five-benefit ladder is one 0.4pp Silver discount**, and even that only on the share of the founding cohort that actually gates. Time-phasing is doing enormous work here and should be shown to the client explicitly, because it is the reason a generous-looking benefit set is affordable (`_draft_ics-scoring.md` §6.1: *"the ladder's cost curve and the business's cost curve are the same curve, offset the right way"*).

**A second benefit that is nearly costless, and it should be added to the client-facing story.** Under the S35 ATM distribution — 60% of cardholders draw AED 0–500, 25% draw 500–1,500, 12% draw 1,500–3,000, 3% draw 3,000+ — raising the free allowance from AED 1,000 at Gold to AED 5,000 at Sovereign waives revenue from only the **top ~3% of cardholders. The ATM allowance ladder costs almost nothing and looks generous.** Same argument as the discount ladder, applied to a second benefit.

⚠ **Model ATM as a distribution, not as a mean.** The mean draw is ~AED 940, which sits **deliberately just below** the Gold free allowance of AED 1,000. Applying `2% × MAX(0, 950 − 1,000)` returns **zero**. The distribution returns materially more, generated almost entirely by a small high-cash tail. **The mean is the wrong statistic for a threshold benefit** — this is the same Jensen error as D2, in miniature, and it points the other way.

### Layer 9 — Acquisition cost

Detail at §7.3. Agent commission, referral reward at a six-month lag, and marketing spend, all bounded by the acquisition budget ceiling — which is a **Phase 4 output**, solver item 2 at §9.

**One arrow that must be wired and is not in v1.0.** At S18 = 45% annual agent attrition, holding T7's active-agent stock requires a **recruit flow** that carries onboarding and training cost and re-enters the S17 ramp at 0.20. To hold 200 active agents requires roughly 90 recruits a year. Model recruits explicitly as a cost line and as a productivity drag.

### Layer 10 — Operating expenses

Detail at §7.4. Ten blocks (eleven once Legal and trust is split out), classified **step vs scale**, interpolated **log-linear within block** on the Y1/Y3/Y10 anchors — never on the total.

```
v(y) = v(anchor_low) × (v(anchor_high) ÷ v(anchor_low)) ^ ((y − y_low) ÷ (y_high − y_low))
```

Log-linear rather than straight-line because **every block anchor pair implies a growth rate, not a growth increment**; straight-line interpolation between Y3 and Y10 puts Y4 opex ~13% too high. Marketing uses straight-line from a zero Y1 base, because log-linear is undefined at zero.

⚠ **Y1 opex is not a running rate.** Y2 at USD 1,478,420 against Y1 at USD 894,800 is a 65% step, and Y3 against Y2 is another 68%. **The Y1 figure is a partial year of a business that has not finished hiring.** Carry an explicit Y1 hire schedule (preferable), or apply S48 and flag that the Y1 figure **understates the exit run-rate by roughly 40%. A break-even calculation run against an understated Y1 cost base flatters the early years** — which is precisely what v1.0's §0.3 did before dividing by it.

### Layer 11 — P&L to net profit after tax

**v1.0 runs "the full P&L to net profit" and stops before tax. That is not net profit** (D14).

```
Revenue        = Σ streams 1a, 1b, 2, 3, 4, 5, 6
  less  COGS                       [inside stream 1: premium, price-gap, float CoC, rail]
  less  benefit costs              [entry discount, Gold Rewards, will discount]
  less  redemption cost            [stream 0: F20 per event + net-outflow spread]
  less  acquisition cost           [agent, referral, marketing, recruitment]
  less  opex                       [ten blocks + legal and trust]
  =     EBITDA
  less  depreciation / amortisation  [default zero; no capitalised build assumed]
  =     accounting_profit
  less  tax                          [annual, final month of the financial year]
  =     NET PROFIT AFTER TAX
```

**The tax rule, stated for the build** (F33, F34, F35):

```
taxable_income(y)   = accounting_profit(y) − loss_bf_utilised(y)
loss_bf_utilised(y) = MIN( loss_pool(y−1), 0.75 × MAX(0, accounting_profit(y)) )
tax(y)              = 0.09 × MAX(0, taxable_income(y) − 375,000)
loss_pool(y)        = loss_pool(y−1) − loss_bf_utilised(y) + MAX(0, −accounting_profit(y))
```

Federal Decree-Law No. 47 of 2022, Article 37: indefinite carry-forward, **utilisation capped at 75% of the taxable income of the year in which it is used**, subject to ownership-continuity and business-continuity tests. With a large accumulated loss pool from the loss-making years, **the 75% cap means Aurumix pays real cash tax from its first profitable year even though it is cumulatively loss-making.** It cannot shelter the full profit. **This is a genuine cash-flow finding v1.0 has no line for**, and the omission is not even conservative — v1.0 omits both the tax and the shelter, and the shelter is worth less than the tax.

**QFZP: assume the adverse case, and the reasoning is modelling hygiene rather than a tax opinion** (F35). Three reasons. **(a)** Qualifying Income is essentially income from transactions with other Free Zone Persons plus a defined activity list; **Aurumix's revenue is retail customer income, which is the paradigm case of non-qualifying income.** **(b)** The de minimis relief tolerates non-qualifying revenue only up to the lower of 5% of total revenue or AED 5 million; Aurumix's non-qualifying share would be close to 100%. **(c)** The asymmetry of the error is severe: a QFZP that loses its status loses it for the tax period **and the four following tax periods**, and **a QFZP does not get the AED 375,000 zero band on its non-qualifying income** — so a failed QFZP is taxed *worse* than a plain mainland company. **Modelling 0% and being wrong is a five-year, no-safety-net error; modelling 9% and being wrong is upside.** Carry the 0% case as an upside sensitivity — **but on the Base path it is worth exactly USD 0.** The model books **zero tax in every modelled year** because no year is profitable, so QFZP status changes nothing inside the horizon — and shortening the horizon to 7 years can only reinforce that, since the loss-making years are the early ones. 🔴 **v1.0's "~USD 220k/yr at Y10" is unsupported: it presupposes a profitable Y10 that the corrected model does not produce, and Y10 is now beyond the horizon in any case.** The relief becomes worth something only in the scenarios that do turn profitable — Aggressive was EBITDA-positive from Y5 on the ten-year run, which is inside the new window — and it should be sized there, not at Base.

**VAT is a residency question, and on this base it is probably an advantage.** 5% standard-rated for UAE residents (F36), 0% for non-residents under export-of-services (F37). The split falls straight out of §5's own segmentation (S49), because decision 31 re-cut the segments by country of residence precisely so that residence-dependent rules could bind. **The non-resident share of the book rises from 0% in Y1 to roughly 42% by Y10.** Worth `{{UNFILLED: Y10 VAT advantage on fee lines from non-resident share, USD — not in spine; the model books cost_vat of USD 7,421 at Y10 but does not decompose a non-resident saving}}` against a competitor set that is UAE-resident-facing and pays 5% on all of it.

⚠ **Two cautions that keep it honest.** Input-VAT recoverability is affected by the mix of zero-rated and standard-rated supplies, so the benefit is not a clean 5% — model at 5% and **haircut by 20% for input-VAT drag**. And **investment-grade precious metals may be zero-rated in the UAE regardless of residence** (`_draft_entities-licensing-and-payments.md`): if the entry fee is characterised as part of a supply of gold rather than a supply of services, the resident/non-resident distinction may not matter for stream 1 at all. **Three separate corpus files flag VAT as unresolved. It belongs in the tax opinion, not in a modelling assumption.**

### Layer 12 — Cash and funding (entirely new)

**v1.0 has zero occurrences of cash flow, balance sheet, working capital or funding requirement** — in a model whose stated purpose is to tell the client when they make money (D7).

Four compounding problems, and they are not independent:

1. **§0.1 charges a float cost of capital (F5, 0.49%) as a P&L cost, and the float principal is never sized or funded.** You cannot charge a cost of capital on a balance that appears on no balance sheet.
2. **T3, the bar denomination upgrade, is a capital allocation decision with no capital account.** It justifies the Year 3 upgrade as "USD 135k/yr for USD 1.2m of extra float" — a return on capital the model does not carry.
3. **F15's AED 1.5m is "locked, not expensed"** — correct for the P&L, and exactly why the missing balance sheet matters.
4. **The business is loss-making for years. Cumulative losses + float + regulatory capital is the fundraise, and the model does not produce it.**

```
free_cash(t)      = EBITDA(t)
                  − tax(t)                          [annual, in the FY-end month]
                  − Δ float_capital(t)              [working capital movement]
                  − one-off launch spend(t)
cumulative(t)     = cumulative(t−1) + free_cash(t)

PEAK FUNDING      = − MIN over all t of cumulative(t)
MONTH OF PEAK     = ARGMIN over all t of cumulative(t)
CASH BREAK-EVEN   = first t where free_cash(t) > 0 for three consecutive periods
TOTAL FUNDING     = PEAK FUNDING + AED 1.5m regulatory capital + float principal
                    [subject to the offset counsel question at §7.6]
```

**Outputs.** ⚠ **All of these are from the v2.0 ten-year run and every one of them lands beyond the new 7-year horizon.** They are recorded so the layer's outputs are named, not so the levels are quoted (§0 footnote, §14).

| Output | Value on the ten-year run | Status under the 7-year basis |
|---|---|---|
| Peak funding requirement | **USD 15,076,460** | **Beyond horizon.** The 7-year model reports the trough *within* its own window, which is not the peak |
| Month it occurs | **M114** | **Beyond horizon** — M114 is Y9.5 |
| Months to cash break-even | **Never within 120 months** | **Not reached.** Also not reached in 84 |
| Months to P&L break-even | **No year within the ten-year horizon.** The first individual month with positive net profit is M115, but the year containing it still loses USD 367,051 | **Beyond horizon.** M115 is Y9.6 |
| Total funding need incl. capital and float | **USD 15,076,460** (cumulative cash deficit plus the USD 408,441 locked regulatory capital) | **Beyond horizon** |

🔴 **The layer is kept in full and its outputs are demoted.** The cash mechanics above are correct and must be built — the float double-count below is a genuine error that only a cash layer can catch. **What is not to be built on is the level of any figure in that table**, because break-even and peak funding both fall outside a 7-year window and because the client has instructed that profitability is not to be leaned on until the cost base settles (§0 footnote). **Report the funding trajectory as a shape — the direction, the slope and the fact it has not turned — never as a headline number.**

**Report months-to-cash-breakeven separately from P&L breakeven.** They are different questions, and the gap between them is the working-capital story.

**The float double-count, which is a genuine error and not a sensitivity** (D7, correction 12). v1.0 charges **both** the float cost of capital **and** the full dealer fabrication premium. Under **dealer-carried** float — the corpus's working launch recommendation — working capital is **zero**, F5 is **zero**, and price-gap risk is the dealer's, paid for in a **wider premium**. Under **own float**, the capital is posted and F5 and price-gap bite, but the **premium is narrower**. **Charging both double-counts under either regime.** Add the switch (S51); it is not a sensitivity, it is an error.

---

## 3.x Calculation cascade and acyclicity proof

**This section exists because a multi-sheet model with a gate engine, an archetype split, a contra-revenue layer and two solvers will produce circular references unless the execution order is fixed in advance.** The benchmark has no equivalent and it should. A circular reference with iterative calculation off returns zeros silently; with it on, it returns garbage silently. Neither failure announces itself.

**The convolution makes this proof stronger, not weaker** (D23). A cohort triangle has 72 blocks that each read the block above; a convolution has one row per series that reads a fixed lookup table. **The number of edges in the dependency graph falls by roughly two orders of magnitude, and the one edge that could close a loop is now visible in a single formula.**

### 3.x.1 Sheet execution order

🆕 **This is a LOGICAL order, and after D26 it is no longer the tab order.** Read the warning below the diagram before using it as a test.

```
  [1] Assumptions            no inbound dependencies                    VISIBLE
        |
  [2] Scenario Parameters    reads Assumptions (Base/Aggressive/         VISIBLE
        |                    Conservative columns)
        |
  [3] Time Series            reads Assumptions + Scenario; produces 29  hidden
        |                    period headers, activation flags,
        |                    seasonality, gold price, fee ladder,
        |                    bar denomination, opex interpolation
        |
  [4] Lifecycle Curves       reads Assumptions + Scenario ONLY.         hidden
        |                    MONTHLY TO M84.  Five archetype curves:
        |                    alive / contributing / reduced / gated /
        |                    tier / grams / card-active / spend.
        |                    ** READS NO PERIOD-t QUANTITY FROM ANYWHERE. **
        |                    It is a pure function of month-since-origination.
        |
  [5] Acquisition            reads Time Series; produces the monthly    hidden
        |                    acquisition vector acq(s,t) by channel
        |                    x segment, with the S4 / S5 / S6
        |                    activation offsets
        |
  [6] ICS Validation         reads Lifecycle Curves ONLY.  Writes into  hidden
        |                    the model NOWHERE.  Produces the nine
        |                    persona results and the 5% collapse-safety
        |                    delta.  A LEAF, not a link.
        |
  [7] Model                  reads Lifecycle Curves + Acquisition +     VISIBLE
        |                    Time Series; performs the convolution,
        |                    then flows, AUM stock, six streams,
        |                    benefit costs, THEN opex, acquisition cost,
        |                    EBITDA, tax, working capital, cash, funding.
        |                    29 columns.  (D26 folds the former
        |                    [8] Opex & P&L into this sheet.)
        |
  [8] Summary                reads Model; annual roll-ups,              VISIBLE
        |                    unit economics, break-even views
        |
  [9] Checks                 reads everything; writes nothing.          hidden
        |                    Its master row is mirrored to Cover.
        |
 [10] Cover                  reads Checks (master flag only).           VISIBLE
                             Otherwise static.
```

**The rule to enforce: no sheet may reference a sheet later in the numbered order above.** There is exactly one exception and it is handled at §3.x.3 item 1.

🆕 ⚠ **D26 breaks the physical form of this test and the replacement must be built deliberately.** The old rule read *"no sheet may reference a sheet to its right"*, which was a tab-position test. **With five sheets visible and the working sheets hidden behind them, tab position now runs backwards against the logical order**: Model sits at tab 4 and legitimately reads Time Series, Lifecycle Curves and Acquisition at tabs 6, 7 and 8. **A tab-position test would fail a correct workbook, and worse, a modeller who "fixes" it by reordering tabs breaks the standard five-sheet layout instead.**

**So the test is by NAME, against the numbered order above, and the order is written on the Cover sheet so it cannot be lost.** Two consequences for the build:

- **Cover is logically last, not first.** It is tab 1 and it reads the Checks master flag, so it is the one visible sheet with an inbound dependency. That is intentional and it is the only edge into Cover — **nothing else on Cover may reference any other sheet.**
- **Hiding is a presentation step, applied last.** Build every sheet visible, pass all sixteen checks, then hide the five working sheets. **Never hide a sheet that has not yet passed its checks**, because a hidden sheet with a FALSE in it is exactly the failure §3.x exists to prevent.

⚠ **The ICS Validation sheet is a leaf and must stay one.** It reads the Lifecycle Curves and it is read only by Checks. **If any Model formula ever references it, the collapse has been silently un-done** and the row map at §10.1 no longer describes the workbook. Add this to the left-to-right dependency test at §3.x.4.

### 3.x.2 The acquisition → curve → benefits → stream 1 chain has no loop

The chain that *looks* circular is:

```
tier distribution → entry-fee discount → fee applied → stream 1 revenue
                 → acquisition budget ceiling (% of stream 1)
                 → marketing spend → new accounts → acquisition vector
                 → convolution → tier distribution
```

**It is not a loop, because of a one-period lag and a separation of the curve from the vector. The proof is in three parts, and the middle one is now trivial rather than argued.**

**(a) The lifecycle curves are a pure function of month-since-origination.** `tier(a,m)`, `gated(a,m)` and every other series depend on `m` and on the archetype's parameters. **No series reads a revenue, cost, population or price figure from any period `t`.** The Lifecycle Curves sheet reads Assumptions and Scenario Parameters and nothing else. **Under v2.0 this had to be proved cohort by cohort; under the convolution it is a property of the sheet, verifiable by inspecting its inbound references.** One direction, no return path.

**(b) The discount applies to a book the acquisition vector cannot retroactively change.** `fee_applied(s,t) = base_fee(t) − tier_weighted_discount(s,t)` reduces revenue in period `t`. Reduced revenue changes the acquisition budget in period `t+1`, which changes `acq(s, t+1)` — **a later element of the vector.** The convolution at period `t` reads `acq(s, 1..t)` only. **The arrow that would close the loop points at a vector element that has not been written yet**, and the `SUMPRODUCT` range makes that visible: it terminates at `t`.

**(c) The lag is explicit and must be built as such.** `acquisition_budget(t) = ceiling% × stream1_revenue(t−1)`. **Write the lag. Do not write `stream1_revenue(t)`.** With the lag, the dependency graph on the Model sheet is strictly lower-triangular in the period index and Excel resolves it left to right in a single pass.

**A fourth chain that also looks circular and is not.** Gold Rewards is capped at the customer's own generated revenue net of their custody cost. That cap reads stream 2 and stream 5 in the **same** period, and Gold Rewards is a haircut *on* stream 2. Resolution: **compute gross stream 2 first, then the cap, then the net, in three separate row bands on the Model sheet in that physical order.** Gross interchange does not depend on Gold Rewards; only net does. The ordering is the resolution.

### 3.x.3 The two genuine circularities, named, with their resolution

There are exactly two, and both are real.

| # | Circularity | Why it is genuine | Resolution |
|---|---|---|---|
| **1** | **The acquisition ceiling.** Marketing and agent spend is capped as a percentage of entry-fee revenue; entry-fee revenue depends on the accounts that spend bought. | Within a single period these are mutually determining. Unlike the curve chain there is no separation of vector from lookup — the spend and the revenue are in the same period. | **A one-period lag.** `budget(t) = ceiling% × stream1_revenue(t−1)`, with `budget(1)` set from a hardcoded launch allocation. **Do not enable iterative calculation.** A lagged budget is also the operationally honest model: a board approves this quarter's spend against last quarter's revenue. Test by running the ceiling at ±5pp and confirming the model is not sensitive to the lag itself. ⚠ **In the annual block the lag is one *annual* column, i.e. twelve months, not one month.** Say so in the formula bar; a lag that silently changes length at the M24/Y3 seam is the seam error §10.5 warns about. |
| **2** | **T3, the bar denomination.** The denomination sets the fabrication premium (F4) and the float size; the float size and the inflow rate determine when an upgrade is affordable; affordability depends on margin, which depends on the premium, which depends on the denomination. | A genuine fixed point in a capital allocation decision. The upgrade rule is a threshold on a quantity the upgrade itself changes. | **Resolve as a step function on a trailing measure, not as a simultaneity.** `bar_grams(t) = threshold_lookup( trailing_12m_avg_daily_inflow_grams(t−1) )`. Period `t`'s premium is set by periods `t−12` to `t−1`. **Additionally, latch the step:** once upgraded, the denomination never steps back down even if trailing inflow falls — you do not sell a kilobar to buy 100 g bars. The latch removes chatter at the threshold and matches physical reality. |

**A third candidate that is not a circularity but is often mistaken for one.** The redemption spread cost depends on net flow; net flow depends on inflow; inflow depends on accounts; accounts depend on nothing downstream of redemption. **Redemption reduces grams, grams reduce AUM, and AUM drives stream 6 — but stream 6 revenue does not feed back into redemption behaviour.** S32 and S33 are exogenous rates on the AUM stock. Straight line, no return arrow.

**A fourth candidate, new at v2.1, and it is the one a modeller will get wrong.** The convolution at an *annual* column looks as though it needs the annual column's own result to know which lifecycle months to read. **It does not.** An annual column `Y` covers a known, fixed set of twelve calendar months; the convolution is performed **at each of those twelve monthly points against the M84 curve table** and only then aggregated into the column. **The annual column is an output of twelve monthly convolutions, never an input to them.** ⚠ **Do not attempt to convolve an annual acquisition figure against an annual curve point.** That collapses twelve first-passage months into one and destroys the gate distribution, which is the first-order term (§3 Layer 5). **This is the single most likely way to break the D23 architecture while appearing to implement it.**

### 3.x.4 What the Checks sheet must verify about the cascade

- **Circular-reference canary.** A named cell that reports the workbook's iterative-calculation setting. Iterative calculation is a workbook property and a modeller can enable it by accident; the canary makes that visible on the Checks sheet rather than invisible in a dialog box.
- 🆕 **Dependency-order test, by sheet NAME and not by tab position** (D26). For each sheet, confirm no formula references a sheet later in the §3.x.1 numbered order. **Including: no Model formula may reference the ICS Validation sheet, and nothing on Cover may reference any sheet other than Checks.** ⚠ **Do not implement this as a left-to-right tab scan.** After D26 the five visible sheets sit ahead of the working sheets they depend on, so a positional test fails a correct workbook (§3.x.1).
- 🆕 **Hidden-sheet inventory** (D26). A row listing the five sheets that must be hidden in the delivered file — Time Series, Lifecycle Curves, Acquisition, ICS Validation, Checks — and the five that must be visible. **A working sheet left visible is a cosmetic defect; a required sheet hidden is a real one.**
- 🆕 **Cover master-flag integrity** (D26). Confirm the Cover's `ALL CHECKS PASS` cell reads the Checks master row and is not a typed value. **A hardcoded TRUE on the Cover is the single worst failure this workbook can ship**, because it hides a hidden sheet's failure behind a visible green cell.
- **Lag integrity.** Confirm `acquisition_budget` in every period references the prior period and never the current one, **and that the lag is one month in the monthly block and one year in the annual block.**
- **Denomination monotonicity.** Confirm `bar_grams(t) ≥ bar_grams(t−1)` for all `t` — the latch.
- **Convolution range integrity.** Confirm every `SUMPRODUCT` in the convolution band terminates its acquisition range at the current period and never beyond it, and that the curve range is reversed against it. **A range that runs one column too far reads an acquisition figure the model has not derived yet, which is the loop §3.x.2(b) rules out.**
- **Annual-column decomposition.** Confirm each annual column's population equals the sum of twelve monthly convolutions and not a single convolution on an annual aggregate. **The third candidate above, tested.**

---

## 3.y The modelling approach: what was chosen, what was rejected, and what this model cannot do

This section exists so that a reviewer can judge the *approach* before arguing with the *numbers*. Everything above is the design. This is its boundary.

### 3.y.1 The choice

**A deterministic lifecycle-curve convolution with behavioural archetype tracks.** Five archetype lifecycle curves are computed once, monthly to M84, as a pure function of month-since-origination. Acquisition by channel into segments produces a monthly vector. The book in any period is the convolution of the two. Revenue and cost are computed per archetype and summed. **Eligibility — the run-of-6 gate — is solved exactly; the rate ladder within eligibility is a tenure→tier lookup.** Nothing is drawn from a distribution at runtime.

Four properties made this the right shape rather than a default:

1. **Eligibility drives the card stack and cannot be assumed.** 63% of live accounts are Gold+; assuming 100% overstates the business by ~59%. Interchange, cardholder fees and credit are all gated on Gold+, and so are Gold Rewards cost, FX waivers, ATM allowances and LTV. **Any approach that takes eligibility as an input is assuming most of the answer.** *(v1.0 put the card at 71% of revenue; the corrected figure is higher, and on gross profit rather than gross revenue.)*
2. **Eligibility is a threshold function of an individual's payment history**, so the model must carry heterogeneity explicitly. Averaging first and thresholding after is wrong by Jensen's inequality (D2), and wrong in the direction that flatters the business. **The convolution preserves this exactly** — it weights per-archetype curves, it does not blend them.
3. **The rate ladder within eligibility is second-order and was collapsed on measurement, not preference** (D22). A flat Gold rate against the full 1.80/2.05/2.10 ladder moves stream 2 by ~2% of gross profit at Y7. **The saving is not the arithmetic; it is that the top of the ladder no longer needs monthly resolution, which is what makes a 24-month monthly block viable** (§1).
4. **The deliverable is an auditable Excel workbook for a pre-launch company.** That rules out anything a client cannot open, trace and argue with cell by cell. **A cohort triangle is technically auditable and practically not** — 72 near-identical blocks is where a reviewer stops reading, which is why D23 removes it.

### 3.y.2 Alternatives considered and rejected

| Approach | Why it was rejected |
|---|---|
| **Aggregate roll-forward** (one population, average tenure, assumed mix) | Cannot compute eligibility or a tier distribution, so it must assume one. **Assuming 100% Gold+ overstates the business by ~59%.** It is the approach v1.0 effectively specified while claiming otherwise |
| **An explicit cohort triangle** (v2.0's shape: a six-state block per segment × cohort × archetype) | **Rejected at v2.1 and it must not return** (D23). It re-computes the same 84-number path once per acquisition month, and it was the single largest driver of v2.0's 600 × 76 Model sheet. **The convolution is not an approximation of it — it is the same sum, because the state machine is time-invariant in month-since-origination and every series aggregates by addition** (§3 Layer 2c). The triangle costs two orders of magnitude in dependency edges and buys nothing |
| **The full per-period ICS engine as the live model** | **Demoted, not rejected** (D22). It remains fully specified and it still runs — as a validation artefact against which the collapsed lookup is proved, with a 5% safety gate that reverts the collapse if it fails (§3 Layer 5d). The argument for demoting it is measured, not aesthetic: ~2% of gross profit at Y7 |
| **Monte Carlo over payment and withdrawal behaviour** | Statistically the most defensible and the wrong deliverable. Not reproducible cell by cell, not auditable by a client, and it converts a sourcing argument into a distributional one that none of our inputs can support. Unnecessary once archetypes are discrete and deterministic |
| **Full Markov chain over the ICS state space** | Strictly more general than archetypes, and genuinely tempting. Rejected on tractability: the state is `(Months × Recent 0–12 × Sold bucket × payment state)`, which is tens of thousands of cells per segment before any revenue line. Archetype curves are the Excel-representable approximation to the same object — a mover-stayer mixture rather than a full transition matrix |
| **Agent-based simulation** | This is Phase 5's deliverable, not Phase 4's. A revenue model that a client signs off on and a simulation that stress-tests it are different artefacts with different standards of evidence. Building one in place of the other loses both |
| **Top-down market-share model** | Would sidestep every mechanism the engagement exists to price. It is also how the client's own 60,000–100,000 target was produced, and testing that target is the point |

### 3.y.3 What this model cannot do — stated, not discovered

Each of these is a deliberate boundary, not an oversight. A reviewer should push back on any they think is wrongly drawn.

| # | Limitation | Why it is accepted | What it would cost to remove |
|---|---|---|---|
| L1 | **Archetypes are fixed at origination.** A customer cannot migrate from occasional misser to perfect payer | Real behaviour migrates; the mixture reproduces the *aggregate* survival curve to under 1pp at all five anchors, which is what the revenue lines consume. Migration mostly reshuffles members between tracks whose economics are already modelled | A transition matrix between archetypes — i.e. the Markov approach, at Markov cost |
| L2 | **Gold price is flat in the base case** | Deliberate: it makes every revenue change attributable to the business rather than the metal. Held as a **scenario**, not a one-cell sensitivity (D14) | Nothing — it is already a scenario axis. The limitation is only that the *base* is flat |
| **L3** | **The tier rate ladder is collapsed to a flat Gold rate** (D22). The model cannot price a Platinum or Sovereign account's interchange, waivers or Gold Rewards at that tier's own rate | **Measured, not assumed: ~2% of gross profit at Y7, 3.1% at Y10.** Sovereign is 1.2% of tiered accounts at Y7, so there is very little at the top of the ladder to mis-price. **Eligibility, which is worth ~59%, is not collapsed** | Restoring the per-period ICS engine — which is still fully specified on the ICS Validation sheet, so the cost is re-linking it, not rebuilding it. **The 5% safety gate (§3 Layer 5d) forces exactly this if the cost ever exceeds tolerance** |
| **L3a** | **Platinum and above are resolved annually, not monthly.** Platinum is earliest at M36 and Sovereign at M61; the monthly block ends at M24 | Acceptable **precisely because of L3**: with the ladder collapsed, the rate difference between Gold and the tiers above it is the ~2% already counted. **Under the uncollapsed ladder this would be a defect** — the two decisions are only jointly safe (§1) | A longer monthly block, which is what v2.0 had at 72 columns and what D21 withdrew |
| **L3b** | **Archetype lifecycle curves are fixed at origination and identical across segments.** A segment scales a curve by ticket and card spend; it cannot bend one | The archetype mix already carries the behavioural heterogeneity, and **no source decomposes behaviour by segment** — S27's decomposition is a confirmed negative (§8.2). Scaling is an assertion the evidence supports; bending is not | A curve set per segment — 30 curves rather than 5. **If a future decision makes a segment behave differently rather than merely spend differently, this limitation becomes a defect and the curve set must expand.** Say so at that point rather than quietly adding a scalar |
| **L11** | **The heavy-seller haircut is an aggregate multiplier, not a per-account `Sold` ratio** (D22). The 30% Retention kink cannot be represented | The real term kinks per account; a mix-level multiplier smooths it. This is the same class of error as L4 and it is bounded by the same 5% gate | The per-account `Sold` denominator, i.e. the per-period ICS engine — L3's remedy, at L3's cost |
| L4 | **Per-account cumulative caps are applied at archetype level, not per account** — Gold Rewards specifically | `Σ MIN(individual) ≠ MIN(Σ)`, so an aggregate cap is looser than the real rule. The approximation is safe *only because* the cap is proved non-binding at any PM share above the 36% floor (§9). It is not safe below it | Per-account state, which a column model cannot carry |
| L5 | **Acquisition is deterministic.** No competitive response, no channel saturation shock, no viral dynamics beyond the referral lag | A pre-launch company has no basis for any of these. Segment saturation caps prevent the hockey stick, which is the failure mode that actually matters | Phase 5 |
| L6 | **The B2B partner book is top-down.** Partner AUM is an input ramp, not an engine of partner accounts | Partner customers earn no ICS and consume no benefits, so they need no state machine. Their economics are a fee on a stock | A seventh segment with its own lifecycle curve |
| L7 | **No stochastic shocks**: no rail outage, no partner default, no regulatory stop. A gold crash is carried, but only as a *discrete* shock — see L10 | Named scenarios and the stress tests carry the ones we can size; the rest are unquantifiable pre-launch | Phase 5 |
| L8 | **Credit is modelled as a revenue share on an average drawn balance**, with drawn-balance vintages by struck LTV but no loan-level book | Aurumix is not the lender of record and takes no credit risk. Every fee head is a partner term-sheet input that does not yet exist | A term sheet |
| L9 | **The model prices India as a market. It does not assert a compliant payment route exists** | Decision 27 stands. The `INDIA_ENABLED` switch exists so the client can see what the payment problem costs them, not to imply it is solved | Not ours to remove |
| **L10** | **Gold is modelled as a level and as a discrete shock, never as a stochastic process.** So the model answers *"what if gold falls X% in Year 6"* and **cannot answer** *"what is the probability of a margin call over the horizon"* | A level axis proves the USD-AUM invariance (§14.4a) and a dated shock against struck-LTV vintages proves what actually margin-calls (§14.4b). Neither needs a price process, and a pre-launch company has no basis for calibrating one | A stochastic gold path — Phase 5. It would turn §14.4's stress rows into exceedance probabilities, which is the one thing this view cannot currently produce |

### 3.y.4 The honest summary of confidence

**The architecture is sound and the arithmetic is now reproducible.** What remains uncertain is not the shape of the model but five inputs, three of which are commercial conversations rather than research: the rail cost per collection, the programme manager's share of interchange, the dealer's fabrication premium, the vault quote, and the credit partner's fee heads. §8.4 ranks them; §17.2 says what to measure post-launch to retire each.

⚠ **A model of a pre-launch company is a structured argument, not a forecast.** The value of this one is that it makes every assumption visible, sourced and switchable, and that it produces the same number twice. It is not evidence that the business will perform as the base case says. The scenario spread in §14 is wide on purpose, and the width is itself the finding.

---

## 4. Timeline and milestones

| Milestone | Period | Revenue and cost impact |
|---|---|---|
| Client app build complete | Sep 2026 (pre-model) | **Multi-tenant capability at register and mint must be in this build or stream 6 is lost.** Shares the requirement with composability Stage 1 — **one build, two dependencies, do not double-count** (D15) |
| **Model Year 1 starts** | **M1 = Jan 2027 (assumption)** | **No launch date exists in any client document.** This is ours and must be flagged |
| Platform live, UAE only | M1 | Streams 1a, 1b and 3 active. Entry-fee discount and will discount live. Nothing else. **Redemption cost (stream 0) is live from M1** |
| First cohort's **earliest** gate | M6 | **Not a date — the start of a distribution.** Only members who paid six consecutive months gate here |
| Card programme fixed costs begin | **M15** | BIN sponsorship setup and scheme certification, three months before go-live (F27). **Contra-costs on stream 2, not opex** |
| **First Gold tier — earliest** | **M12** | Credit, card and Gold Rewards become **eligible**, not yet available. Late gaters reach Gold at M15, M18 or later |
| Oman and Bahrain open | M13 | Segment 4 activates. Requires local authorisation |
| **Referral channel produces its first payout** | **M13** | Six months for the referrer plus six for the referee. Year 1 pays nothing. **Steady state not before ~M25** |
| **Card programme live** (sponsor bank) | **M18, assumed** | **Streams 2 and 4 activate. This is the majority of terminal revenue** |
| **Gold arrives — cohort-weighted** | **~M20** | **The eligibility threshold for card, credit and Gold Rewards.** Earliest M12; the gate delay pushes the weighted arrival to roughly M20. **Inside the monthly block, and this is the reason the monthly block is 24 columns** (§1) |
| **Monthly block ends** | **M24** | **24 monthly columns, then five annual** (D21). Nothing is frozen at the seam — the lifecycle curves run monthly to M84 and an annual column aggregates twelve of their points (§1, §10.5) |
| Lending partner live | **M24, assumed → booked at the start of the annual block (Y3)** | Stream 5 activates |
| **B2B partner live** | **M24, assumed → booked at the START OF THE ANNUAL BLOCK (Y3)** | Stream 6 activates. Partner 1 starts its own S43 maturity clock here. 🔴 **M24 falls exactly on the monthly/annual boundary. Place stream 6 at the start of the annual block so it does not get a single stub month** — a one-twelfth-year column sitting beside a full annual column is the seam error §10.5 exists to prevent |
| Other international | M25 | Segment 6. **First period of the annual block**, handled by offsetting the acquisition vector, not by a new lifecycle curve (D23) |
| First Platinum — earliest | M36 | LTV 65%, Gold Rewards 0.45%, FX 1.5%. **In the annual block** — acceptable because the rate ladder is collapsed (D22, §1, L3a) |
| **First Sovereign — earliest** | **M61** | **In the annual block.** Under the uncollapsed ladder this would need monthly resolution; under the flat Gold rate it costs ~2% of gross profit at Y7, because **Sovereign is 1.2% of tiered accounts by then** (D22) |
| **Horizon ends** | **Y7** | 29 columns total (D21) |

### 4.1 Gate arrival is a distribution, and it moves every date in this table

Under v1.0's Layer 5 the ladder dates above were dates. **They are not.** A member who misses month 4 does not gate until month 9 at the earliest, and the whole ladder shifts right with them. What the table records is the **earliest possible** arrival — the perfect payer's path. What the model computes is the **share of each cohort arriving in each month**, as a run-of-6 first-passage problem in the archetype's monthly payment probability (D4).

| Archetype | Monthly pay prob. | **Expected month of first six-in-a-row** | Share ever gating |
|---|---|---|---|
| Perfect payer | 0.995 | **6.1** | **90.6%** |
| Occasional misser | 0.93 | **7.6** | **83.6%** |
| Alternating misser | 0.55 | **24.9** | **24.0%** |
| Reducer | 0.97 | **6.6** | **88.6%** |
| Early lapser | 0.60 falling | **8.6** | **2.6%** — **most never gate** |
| **Cohort-weighted** | — | **8.1** | **53.5%** |

🔴 **The alternating misser is the row that changes the ladder.** Paying every other month, it has only a **24.0%** chance of ever assembling six consecutive periods, and when it does the mean arrival is **month 24.9**. v1.0 has it Silver at M6 and Gold at M12; in reality three-quarters of that cell never scores at all. **This is the single largest correction the first-passage solve makes to the ladder's timing** — and it lands on the cell §3 Layer 5c identifies as the most profitable card cell in the book.

**The never-gated share is a revenue-positive population, not a failure statistic.** They pay the full undiscounted fee, hold gold, generate AUM, and consume no benefits, forever. The corpus states the customer-facing consequence plainly and the model must reproduce it: *"A saver who never completes six in a row accrues nothing at all: no score, no tier, no benefits, however many scattered payments they make"* (`_draft_ics-scoring.md` §1.6).

**Model implication.** Conditional activation on every stream: `=IF(period >= activation_month, calculation, 0)`, with activation months held on the Time Series sheet and **never hardcoded inside a formula**. The two dates that matter most are the **card programme (M18)** and the **B2B partner (M24)**, because between them they carry the majority of terminal revenue and **both are commercial gates outside our control.** The Checks sheet must verify that every activation flag fires in the right period.

⚠ **The two dates sit on opposite sides of the seam and must be built differently.** The card at **M18** is inside the monthly block, so its ramp is resolved month by month and the F27 fixed costs beginning at **M15** land three columns earlier, as they should. The B2B partner at **M24** is on the boundary, so **stream 6 is zero through the whole monthly block and first appears in the Y3 column** — not as a stub month at M24. **Stream 5 follows the same rule for the same reason.** Check 7 (§10.6) must test both conventions, not just the flag.

---

## 5. Segments

> 🆕 **REWRITTEN 2026-08-19 (D25). Six occupational segments become four regional ones, and the population is re-cut from Indian to South Asian.** Three research streams were run against primary sources: Oman's NCSI monthly bulletin, Bahrain's Social Insurance wage dataset, the CBB Crypto-Asset Module text, CBUAE's Financial Stability Report 2025, AMFI July 2026 and the Abu Dhabi 2024 census. **v2.1's segment table is superseded in full.** The prior version is preserved in `supporting/_working_architecture-decisions-v2.md` at D25.

### 5.0 The three findings that forced the re-cut

**1. The market is South Asian, not Indian, and this is the single largest correction in §5.** In Oman, Bangladeshi workers (605,486) outnumber Indian workers (515,361). In the UAE, non-Indian South Asians (~3.4m) outnumber Indians (~3.5m) to within the error bar. **The MEA overseas-Indians table we sized on counts PIO/OCI and historic diaspora, and omits Bangladeshis and Pakistanis entirely.** It is the wrong instrument. National statistics authorities count live visas and are both more current and more complete.

⚠ **This reaches past Phase 4.** The charter persona is "the NRI saver" and the agent network in Layer 1 is modelled on Indian insurance-agency practice. Both are narrower than the market. See §15 corrections 21 and 22.

**2. Segmenting by occupation was solving the wrong problem.** Occupation was a proxy for ticket size. Ticket size is now carried directly by two numbers per region (§5.2), which reproduces the same economics without asserting an occupational split that rests on an uncited tertiary source. **Region is the better cut because region is what the rules and the channels attach to**, exactly as decision 31 argued.

**3. Bahrain is not an easy adjacency and our own client agenda has the sequencing backwards.** The CBB Crypto-Asset Module binds and a VARA licence does not passport in. See §5.3.

### 5.1 The four modelled regions

| ID | Region | Addressable base | Ceiling (S22) | Implied max accounts | Avg ticket | **Floor share (S54)** | Activation | UAE-resident (S49) |
|---|---|---|---|---|---|---|---|---|
| R1 | **UAE, Indian** | ~640,000 | 9.5% | 60,800 | **USD 38** | **40%** | M1 | **100%** |
| R2 | **UAE, other South Asian** | ~620,000 | 6.0% | 37,200 | **USD 26** | **60%** | **M7** | **100%** |
| R3 | **Oman** | ~600,000 | 4.0% | 24,000 | **USD 26** | **58%** | M13 | **0%** |
| R4 | **India resident** | ~12.5m | 0.35% | 43,750 | **USD 30** | **25%** | `INDIA_ENABLED` | **0%** |
| | **Total** | | | **165,750** | | | | |

**R2 is new and it is the largest single addition to the model's perimeter.** Pakistani, Bangladeshi, Sri Lankan and Nepali residents of the UAE, ~3.4m gross. It is added because the gold-savings culture, the ticket structure and the agent channel all transfer, which is exactly what does not transfer to the populations in §5.3.

**The reconciliation check that matters: the total is 165,750 against v2.1's 164,900.** The re-cut moves where the accounts come from without inflating how many there could ever be. **A re-cut that raised the ceiling would be a re-cut that proved nothing**, so this equality is deliberate and should be preserved if any row is re-tuned.

**One method now applies to every row** (this was not true before, and the two UAE rows were not comparable):

```
population  →  economically active (0.80)  →  direct-debit-capable IBAN (0.57)
            →  discretionary capacity for USD 20/month after remittances (0.40)
```

⚠ **The unsourced gold-savings propensity filter is deleted.** It was flagged Low confidence and named "the weakest link in the entire sizing" in v2.1, and it had no published source for Indians, let alone for Pakistanis. It is replaced by the banking filter, which has a stated mechanism behind it (§5.4). **Consequence: the R1 base rises from 474,000 to ~640,000 and its ceiling falls from a blended 12.7% to 9.5%.** Base and ceiling moved together on purpose. **`base × ceiling` is the invariant, not `base`.** Changing one without the other silently re-scales the model, and the Checks sheet should assert the product.

Oman's row skips the 0.80 filter because NCSI counts **expat workers**, who are working-age and economically active by definition. Applying a labour-force filter to them would double-count.

R4 remains on its own basis (AMFI gold ETF folios intersected with active digital-gold holders, §6.7) because it is behavioural rather than demographic, and behavioural is better. **It is the only row not produced by the funnel above, and that is a deliberate exception, not an inconsistency.**

### 5.2 Ticket and floor share: two numbers, two bands

**A single average ticket per region would have destroyed two separate non-linearities**, and this is the load-bearing mechanic of the whole re-cut.

- **Rail cost is a fixed fee per collection, not a percentage.** A USD 20 saver and a USD 50 saver pay the same collection cost, so margin is not linear in ticket. This is §0.3's fee floor restated.
- **Card spend is keyed to ticket as an income proxy**, compressed by an exponent of 0.55. The card is 83.4% of Y10 gross profit. Blending to one average would have collapsed the card-spend spread from 3.75× to roughly 1.3× and quietly flattened the largest revenue line in the model.

So each region carries **average ticket** and **share sitting at the USD 20 floor**, from which two bands are derived with no additional inputs:

```
floor band     = USD 20                                  at floor_share
standard band  = (avg_ticket − floor_share × 20) ÷ (1 − floor_share)
```

| Region | Avg ticket | Floor share | → Floor band | → Standard band |
|---|---|---|---|---|
| R1 UAE Indian | 38 | 40% | USD 20 | **USD 50** |
| R2 UAE other South Asian | 26 | 60% | USD 20 | **USD 35** |
| R3 Oman | 26 | 58% | USD 20 | **USD 34** |
| R4 India | 30 | 25% | USD 20 | **USD 33** |

**Unit margin, rail cost and card spend are computed per band and summed, never on the regional average** (Layer 4). `S29`, the reduced ticket, applies to the standard band only; the floor band is already at the floor and cannot reduce, which is the F6 hard-gate rule doing its work.

🔴 **This makes §0.3 worse, not better, and the direction should be stated before the model is re-run.** The book-weighted average ticket falls from roughly USD 40 to **USD 31.5**. Lower tickets against a fixed per-collection rail means **the minimum viable entry fee rises above the 3.79% in §0.3.** The re-cut does not rescue the fee schedule; it tightens it. How much is a model question and is not yet answered.

**Where the ticket numbers come from.** Anchored on savings capacity rather than remittance volume, because remittance is a committed obligation and not discretionary. A recurring gold debit realistically captures 10 to 15% of monthly savings capacity. Cross-checks: Joyalukkas has already price-discovered **AED 100 (USD 27)** as the viable mass-market monthly instalment for this exact demographic; Malabar sits at AED 200. The blended USD 27 to 34 lands **below** AMFI's USD 34 Indian retail SIP average, which is the correct direction, since AMFI reflects domestic urban investors with materially more discretionary income than a Gulf blue-collar book.

⚠ **AMFI is confirmed current at July 2026** (₹31,961 crore across 10.63 crore contributing accounts = ₹3,007/month = USD 34). It remains an **upper bound and not a proxy.**

### 5.3 Named, sized, and deliberately not modelled

**Excluding these is a decision with a number attached, not an oversight.** Each line states what it would take.

| Population | Size | Why not modelled | What would change it |
|---|---|---|---|
| **Bahrain** | ~259,000 addressable (0.51m South Asian residents, filtered on Bahrain's own wage distribution) | 🔴 **The CBB Crypto-Asset Module binds and VARA does not passport in.** Digital tokens are securities under Art. 1 of the CBB Law (CRA-B.1.3); CRA-15.1.1 prohibits offering without written CBB approval; CRA-15.1.9 requires BD 50,000 paid-up capital and escrow at a CBB-licensed retail bank; offers must run through a **CBB-licensed digital token advisor** (CRA-15.1.22). **The 246-page text contains no reverse-solicitation exemption** | A CBB pre-application discussion under CRA-15.1.6, which is the only route to a "jurisdiction acceptable to the CBB" determination under 15.1.9(a) |
| **Emirati** | ~1.33m | Wrong persona, not small. No remittance driver, banked with ENBD and ADIB, and Liv Gold already sits inside that relationship | A different product and a different channel. Not a marketing decision |
| **Western expat** | ~500,000 to 600,000 | No gold-savings behaviour to build on | Nothing on the current roadmap |

🔴 **The Bahrain finding reverses our own client agenda.** Item 6b currently says *"agree the launch perimeter is the UAE, then Bahrain and Oman."* **Oman is the accessible one and Bahrain is the hard one.** Oman has no VASP regime in force: FSA Decision E/35/2023 bites on local establishment and is silent on inbound marketing, which is a regulatory gap and **not a permission**. Note also that Oman's regulator is the **FSA, not the Central Bank**, which changes who the client approaches.

### 5.4 Two findings that are not sizing findings

**1. 🔴 The lowest-income segment may not have a payment rail at all.** Findex reports 85.7% UAE account ownership, but for low-wage workers that account is typically a **WPS payroll card with no IBAN**, which cannot carry a mandate or a debit. Our rail is AANI Request to Pay plus prefunding (decision 43), and that still needs a real account.

This collides with something already in the model. Layer 1 states that the agent channel delivers disproportionately into the lowest-ticket segment, and §0.3 states that this is the segment where the fixed rail cost destroys margin. **There is now a prior question: can that segment be collected from at all?** Belongs in the Phase 2 payment work, not only here. See §15 correction 23.

Moving in our favour, on a datable timeline: **CBUAE's Universal Account** is rolling out now, zero minimum balance, real IBAN, targeted explicitly at earners of **AED 5,000/month or less**. FAB Payit live May 2026, Botim IBAN wallets launched. **This is the primary justification for R2's M7 activation rather than M1**, and it should be tracked as a dependency with a date rather than assumed.

**2. 🔴 CBUAE has stated it will launch digital savings and investment products for low-income earners within one to two years.** That is the central bank entering our segment directly. It is a stronger argument for speed than Liv Gold, and it belongs in the client conversation.

### 5.5 What this does to the client's target

Year 10 of 60,000 to 100,000 is 1.3% to 2.2% of the headline diaspora, which is how it will be pitched. Against the **implied maximum of 165,750** in §5.1 it is **36% to 60% of every account the model believes could ever exist.** That is a demanding number against a bank incumbent, and it is a more honest framing than either the diaspora percentage or v2.1's 12.6% to 21.1%.

**Model 60,000 as the defensible case and treat 100,000 as requiring a distribution partnership or perimeter expansion.** The 100k target stays a named narrative scenario at §13, imposed as an input and measured against the floor, never assumed as an output.

### 5.6 Competitive position, corrected in both directions

**In the UAE our floor is not a differentiator.** Liv Gold (Emirates NBD) runs AED 15, digital XAU, no maintenance or transfer fees, fractional to 0.001 XAU, convertible to physical with home delivery, under a CBUAE banking licence and distributed to the largest retail bank's installed base. **Botim's O Gold is at AED 10 (~USD 2.70) and sits on an 8.5m user base that is precisely our persona.** RAKBANK supports standing instructions, which is functionally a gold SIP already.

**But nobody is marketing to this segment.** Across every UAE product found, positioning is investment or lifestyle aimed at mass-affluent customers, and **not one is marketed at low-income migrant workers or at any non-Indian expatriate community.** Emirates Islamic's Sharia positioning is the closest incidental fit for Pakistani and Bangladeshi Muslims and is not framed that way. **This is a positioning and distribution gap, not a product gap**, which is consistent with decision 13.

**In Oman the picture reverses and it is genuinely favourable.** KFH Bahrain and NBO Oman offer gold accounts at a **1-gram minimum (~USD 110)** with **no recurring purchase feature**. A USD 20 monthly recurring floor is real differentiation there, not a me-too.

⚠ **One conversion benchmark worth carrying, because it is sobering.** Botim's O Gold: 775,000 users explored the feature against 45,000 transactions, roughly **6% conversion**, at an average ticket of AED 700 with **64% buying under AED 500**. Those are ad-hoc purchases, not monthly commitments, so a recurring debit converts to a materially lower number.

### 5.7 What could not be sourced, stated as findings

1. **No official UAE nationality breakdown exists.** FCSC and MoFAIC publish totals and the Emirati/non-Emirati split only. **Every nationality figure in public circulation traces to one unsourced private compilation**, which explicitly describes itself as the compiler's own research. Pakistan's and Bangladesh's own governments were the only independent checks obtained and both came in slightly below it. ⛔ **Do not present these as multiple corroborating sources in any client document.**
2. **No payroll-card versus IBAN split is published.** This is the most important unknown in the funnel and the highest-value item to commission primary research on. A survey of 200 workers would move the estimate more than any further desk research.
3. **No central bank in the set publishes average remittance transaction size or frequency.** World Bank RPW's "USD 200" is a methodological benchmark for fee comparison and **must not be cited as an observed average.**
4. **CBUAE dropped the destination-country remittance breakdown from the 2025 FSR.** Country shares in circulation are FSR 2024 or 2022 vintage, and are quoted against the total rather than the personal line. Anyone mixing them is mixing vintages.
5. **Nepal's UAE stock is unresolved**, 360k versus 700k depending on source, with Nepal's own government at the high end.
6. **No Omani expat wage distribution is published.** Oman's ticket is inferred from Bahrain's actual distribution plus a composition argument.
7. **No nationality-disaggregated UAE savings survey exists** for Pakistani, Bangladeshi or Sri Lankan workers. The only worker-level savings distribution found is Indian-only on 2013 wages. **This is the weakest link in the ticket estimates in §5.2.**
8. **UN DESA 2024 migrant stock by origin was not extracted** and would give a genuine primary replacement for the UAE nationality spine. Worth doing before client delivery.

### 5.8 Residency, the VAT argument, and the ceiling gradient

**The residency split is definitional, not a judgement call** (S49). Decision 31 re-cut by country of residence precisely so that residence-dependent rules could bind, and VAT is a residence-dependent rule (D14). **R1 and R2 are UAE-resident by construction; R3 and R4 are non-resident by construction.** High confidence on the split; low confidence on the VAT consequence, which is a tax-opinion item and is treated as one at §16.

**What the split buys, and the client has not heard this argument.** If the export-of-services zero-rating holds, **VAT is not a cost on the non-resident share of fee revenue**, against a competitor set that is UAE-resident-facing and pays 5% on all of it. On this base the international perimeter is a **VAT advantage and not merely a licensing cost**, which is an argument for prioritising R3 and R4 that has nothing to do with market size.

⚠ **The 42% Y10 non-resident share carried at v2.1 is withdrawn pending the re-run.** It was computed with Bahrain and "other international" inside the perimeter, and both are now out (§5.3). **Expect the corrected share to be lower.** Do not quote 42%.

**The ceiling gradient is deliberate and each step has a reason** (S22):

| Region | Ceiling | Why it sits there |
|---|---|---|
| R1 UAE Indian | **9.5%** | Highest smartphone and banking penetration, established agent channel, lowest sensitivity to the floor. Re-based from a blended 12.7% when the propensity filter was deleted, so that `base × ceiling` held |
| R2 UAE other South Asian | **6.0%** | Same product fit, but **no channel reaches them yet** and the propensity evidence is qualitative rather than nationality-specific. Deliberately below R1 |
| R3 Oman | **4.0%** | No entity, no local presence, a later activation, and a regulatory gap rather than a permission |
| R4 India | **0.35%** | An order of magnitude tighter than the GCC rows because the route is unresolved. **Even so it is 43,750 accounts, most of the client's Y10 target on its own**, which is why the India switch is load-bearing |

**⚠ Correct decision 31 a second time, and on a different basis than the first correction.** Decision 31 said "~3.5 to 4M"; v2.1 corrected it to 4.58M on the MEA table. **MEA is the wrong instrument** (§5.0). The defensible perimeter is now built from national statistics authorities, is South Asian rather than Indian, and is both larger in gross population and smaller in filtered addressable base. See §15 correction 21.

### 5.9 The spot-only buyer, and why the base has been sizing one lane out of two

🆕 **D35, 2026-08-20, raised by Abdur.** An architecture gap, not a re-pricing. Full reasoning in `supporting/_working_architecture-decisions-v2.md`.

**The finding, in one line: in the model as built, no account can exist before it starts a SIP.**

Stream 1b computes spot as `attaching(s,t) = live_accounts(s,t) × S45 × tenure_uplift(s,t)`, where `live_accounts` is CONTRIBUTING + REDUCED + LAPSED_HOLDING. Every one of those is a state of an account acquired through one of the four SIP channels, and S45 is denominated **"% of live accounts/yr"**. There is no spot acquisition channel, no spot state, no spot archetype, no spot addressable base, and §6.1b says so outright: *"there is no independent spot ceiling."* **Spot is exclusively a behaviour of SIP accounts.**

Three things make that a defect rather than a simplification.

1. 🔴 **The mechanism design says the opposite.** `_draft_sip-spot-and-ics.md` opens with a section titled *"Separating the SIP investor from the spot buyer"*, names them *"two named customer types"*, describes spot as *"the entry point for new investors"*, and calls spot-to-SIP conversion *"the growth funnel"*. **The model runs that arrow only backwards.**
2. 🔴 **The §5.1 funnel is SIP-specific and is applied to both lanes.** Two of its three filters (direct-debit-capable IBAN at 0.57, USD 20/month discretionary at 0.40) are recurring-mandate tests, under the claim *"One method now applies to every row."* **This brief states at §6.1b that spot needs neither**: *"One push or bank transfer, and therefore no collection-failure exposure at all."* The two facts sit on adjacent pages and were never joined.
3. **It is flagged nowhere.** Not in L1 to L11, not in corrections 1 to 38, not in §3.y.2, not in §16. Correction 22 audited the persona for narrowness on the **nationality** axis and found a real defect; the **product** axis was never examined.

⚠ **The defect is not that spot's number is too small.** Spot already reaches 49.6% of Y7 inflow because S45 to S47 are set aggressively. The defect is that **spot volume is analytically bounded by the SIP book at every parameter setting.** A walk-up buyer with a card and no IBAN is not merely un-sized, it is inexpressible.

#### 5.9.1 The architecture: one population, two doors

**Spot does not get its own population. It gets a wider gate through the same one.** This preserves D24's bottom-up commitment (real people, real funnel, real ceiling, no unfalsifiable single penetration share) and it prevents the double-count that a parallel fifth region would create, because **everyone who can fund a SIP can also buy spot**. The spot-capable base is a **superset**, and the spot-only population is the **residual**.

```
                    ┌── Door 1: SIP  ──► existing lifecycle, unchanged
  regional          │
  population  ──────┤
                    └── Door 2: SPOT ──► HOLDER state
                                          - no ICS, no tier, no card, no credit
                                          - pays the full undiscounted entry fee
                                          - sits in AUM, custody and screening
                                          - ──► converts to SIP at S59
```

**The HOLDER state is not new machinery.** A holder who pays nothing monthly but remains in AUM, custody cost and AML screening is `LAPSED_HOLDING` with a different entry route. §5.9 reuses the state; it does not add one.

#### 5.9.2 The two funnels, side by side

| Filter | SIP lane (unchanged) | Spot lane | Why it differs |
|---|---|---|---|
| Economically active | 0.80 | **0.80** | Unchanged. Income is needed either way |
| Payment capability | **0.57** (IBAN able to carry a mandate) | **S56** | A one-off push needs an account, not a standing authority. A WPS payroll card can push once |
| Money capability | **0.40** (USD 20 *every month*) | **S57** | One spot ticket is ~USD 190 once. A USD 20 SIP is USD 240/yr. **Spot asks for less money, less reliably** |

**Worked, on R1 (UAE Indian), to show the method is identical rather than new.** SIP: `3.5m × 0.80 × 0.57 × 0.40 = 638,400`, which reproduces §5.1's ~640,000. Spot: `3.5m × 0.80 × S56 × S57`. **Spot-only population = spot-capable − SIP-capable.**

⚠ **S56 and S57 are `{{UNFILLED}}` and must not be guessed into the model.** This is precisely the failure mode §5.1 corrected when it deleted the unsourced gold-propensity filter. See §5.9.4 for what is and is not sourced.

#### 5.9.3 Two acquisition routes, priced differently

- **Direct spot.** Aurumix's own app, Aurumix's own CAC, through the existing four channels. Slow, and owned.
- **Distributed spot.** Through a consumer wallet. 🆕 **This belongs inside stream 6's existing structure**, which already models volume without account-level acquisition and grants no ICS or benefits (L6). ✅ **Second benefit: stream 6 is currently ~60% dependent on R4, and §6.7 requires it to fall by roughly 60% if `INDIA_ENABLED` is OFF. A UAE wallet partner breaks that single-geography dependency.**

#### 5.9.4 Calibration: what is observed, and what is not

**Botim is the only observed spot funnel in the launch market**, and it is a spot funnel in the strict sense: it has **no recurring purchase facility at all** (verified 2026-08-20 against its own gold FAQ, product page and all launch coverage). Its buyers are one-off buyers by construction.

| Input | Value | Basis | Confidence |
|---|---|---|---|
| Trades since launch | **128,000** | Vendor-disclosed at the Feb 2026 silver launch | Medium-High |
| Total value | **AED 100m+** | Same disclosure | Medium-High |
| Average ticket | **~AED 780** (~USD 212) | `100m ÷ 128,000` | Medium-High |
| Conversion at exposure | **~6%** (775,000 explored → 45,000 transacted) | Carried in this brief at §5.6 | Medium |
| Demographic | **96% blue/grey collar** (65% / 31%) | Botim press release. ⚠ Vendor-published, no methodology | Medium |
| Repeat rate | **~2.8 purchases per buyer**, ≈1.9/yr | ⚠ **INFERRED**, assumes 45,000 = unique buyers and 128,000 = trades | **Low** |

✅ **One useful validation: the inferred ~1.9 events/yr sits close to S47's unsourced 1.7**, which is the first external check that parameter has ever had. ⚠ It is an inference from two disclosures of different vintage and must not be presented as observed.

🔴 **Three calibration traps, each of which would produce a wrong number.**

1. ⛔ **Botim's 8.5m → 775,000 step is NOT transferable.** That is a **9.1% in-app discovery rate** off a shelf inside an app the user already opens daily. Aurumix has no equivalent placement. **Do not reuse it as a reach assumption.**
2. ⛔ **The 6% is a conversion-at-exposure rate, not a penetration ceiling.** S58 is `reach × conversion`, and only the second term is observed. Treating 6% as the ceiling silently assumes total reach.
3. ⚠ **§5.6 currently cites the 6% as a discount to apply to a SIP base** (*"a recurring debit converts to a materially lower number"*). **For the spot lane it applies at full strength, undiscounted.** The brief is currently using its most relevant number backwards. See correction 39.

#### 5.9.5 Two findings from the same pass that land outside this section

1. ✅ 🔴 **The §5.4 payment-rail risk has a dated mitigant, and it has already shipped.** §5.4 flags that the lowest-income segment may have no usable rail, WPS payroll cards carrying no IBAN, and cites CBUAE's Universal Account as a **future** remedy. **Botim launched virtual IBAN wallets on 2026-06-22 under the CBUAE Universal Accounts Framework**: no minimum salary, no minimum balance, no monthly fee, AANI transfers, onboarding under three minutes, to a base that is 96% blue and grey collar. **That converts a hoped-for mitigant into a dated one.** ⚠ It does not close §5.7 item 2, because no payroll-card-versus-IBAN split is published and adoption is unmeasured.
2. ⚠ **The competitor's own binding terms are a differentiator for Aurumix.** Botim is a **distribution front-end, not the gold principal**: the principal is **OGOLD Precious Metals Trading LLC** (DMCC). OGold's marketing says "fully allocated"; its binding T&Cs say metal *"may be held in pooled custody arrangements"* and disclaim any guaranteed return, against Botim marketing "~3% guaranteed". Vault operator, custodian, spread and storage fee are **all unpublished**. **Allocated, serial-numbered, segregated metal is a real and checkable differentiator.** ⚠ **Registry-first caveat: no regulator register entry or licence number was retrieved for either entity.** All licensing rests on company self-description and press. **Close before any commercial dependency.**

#### 5.9.6 What this breaks, stated before it is built

🔴 **The `base × ceiling` invariant changes meaning.** §5.1's 165,750 is the **SIP** ceiling and it stays intact, but it stops being *the* ceiling. It must be **re-labelled** and sit alongside a separate, larger spot ceiling. ⚠ **The Checks-sheet assertion at §5.1 needs rewriting regardless**, because its stated v2.1 anchor of 164,900 does not match the reference model's actual pre-D25 total of 167,900 (the gap is exactly the S6 row, which the brief appears to drop and the model includes). **Reconcile that before the assertion is built, or it fails as written.**

⚠ **The client persona conversation gains a third axis.** It is already being widened on nationality (Indian to South Asian, correction 22). This widens it on **product**. **Deliver as one conversation, not two.**

⚠ **S59 is a new Low-confidence, load-bearing parameter with no source anywhere.** It must be named as an assumption and carried into the tornado, not buried. **It is also the most decision-relevant number in this section** (§5.9.7).

⛔ **India is not a spot target.** SafeGold's 55m customers are Indian residents and decision 27 stands on four independent bars, sharpened by SEBI's 2025-11-08 caution on digital gold. **SafeGold and the NPCI UPI series are behavioural evidence that the one-off gold-buying habit exists at scale; they are not a reachable book.** Size R4's spot lane behind `INDIA_ENABLED` exactly as its SIP lane already is, so the switch shows the client what the India problem costs. **The reachable version of that population is the same people in the Gulf, where they are already R1 and R2.**

#### 5.9.7 Why this matters to §14, and it is the reason to build it

Break-even is **45,102 live accounts** (§14.1). The SIP-only ceiling is 165,750 **cumulative-ever-acquired**, and at the model's own computed 2.96× cumulative-to-live ratio, break-even needs **~133,500 cumulative-ever, or about 80% of every account the model believes could ever exist** — in a region where the S23 headroom term has throttled acquisition to 20% of raw demand. ⚠ **That estimate is optimistic on three counts**: the ratio is still rising at Y10, the solver regresses total revenue including account-free stream 6 on retail live accounts (inflating revenue per account and pulling break-even earlier than it should be), and D25's ticket re-cut pushes the required N up.

**Widening the gate roughly doubles the base the ceiling is applied to.** It does not guarantee break-even, which depends entirely on S58. **It changes the question from "can we win 80% of everything possible" into one with room in it.**

🔴 **And it reframes the adoption bridge.** The strategic problem has been stated as *"how do we sell a monthly commitment to a life-insurance-policyholder mindset."* **The sharper version is that the only door into the book requires a monthly mandate from people who may not hold an IBAN.** A spot door is a lower-friction entry that the mechanism design already anticipated and the model deleted. **S59, the spot-to-SIP conversion rate, is therefore not a modelling detail: it is the strategy question in numerical form, and it is the one an experiment could actually answer.**

---

## 6. Revenue streams in detail

One shape per stream, applied without exception: **Quick Facts | What It Is | How It Materialises | Drivers | Formula — Monthly | Formula — Annual | Growth Logic | Key Uncertainties.** Spot is a **sub-stream of 1**, not a seventh stream, because it is the same fee on the same gold at the same tier discount through a different rail (D9).

---

### Stream 1a: Entry fee margin — SIP

**Quick Facts**

| Field | Value |
|---|---|
| Type | Inflow-linked |
| Activation | **M1** |
| Rate | 5.00% Y1 / 4.00% Y3 / 3.00% Y10 (decision 9, F3), **less the tier discount** |
| Revenue basis | **Gross margin retained, never the headline fee** |
| Sheet location | Model, rows 200–239 |

**What It Is**

The fee deducted from a monthly SIP contribution before gold is bought. **It is a price, not a revenue line.** On a USD 75 contribution at a 5% fee, Aurumix discloses USD 3.75 and retains **USD 1.61**, because the fabrication premium is buried inside the fee. **Booking 5% as revenue overstates the top line by 2.3 times.**

🆕 **Re-cut at D28's observed premium of 1.50%.** The 3.00% column is retained beside it because it is now the **Conservative scenario**, and because every output figure elsewhere in this brief was generated at 3.00% and has not yet been re-run.

| Line | **At F4 = 1.50% (Base)** | % | At F4 = 3.00% (Conservative) | % |
|---|---|---|---|---|
| Contribution received | 75.00 | 100.00% | 75.00 | 100.00% |
| Paid to the dealer (0.5037 g at fix, plus premium) | (72.32) | (96.42%) | (73.39) | (97.85%) |
| **Gross margin retained** | **2.68** | **3.58%** | **1.61** | **2.15%** |
| Price-gap risk carried by the float | (0.59) | (0.79%) | (0.59) | (0.79%) |
| 🆕 Float cost of capital — **MEMO LINE, not deducted** (D32) | — | — | — | — |
| 🆕 Payment rail — **PASSED THROUGH, not deducted** (D31) | — | — | — | — |
| **Net contribution margin** | **2.09** | **2.79%** | **1.03** | **1.36%** |

> 🆕 **D31: the rail leaves this waterfall.** The customer is asked for **USD 75.25** (Base) or **USD 76.36** (Conservative); Aurumix remits the rail to the PSP and books nothing on it. **The entry fee comprises only what Aurumix itself charges — premium, price-gap, float and margin.** ⚠ **Neither column is a customer-cost figure any more. All-in customer cost is unchanged; only the attribution moved.**

🆕 **Four consequences, and the fourth is the one to carry into the client conversation.**

1. **Net contribution margin rises ~2.05×** at the measured premium, from 1.36% to **2.79%** — and it is now **identical at every ticket size and in both lanes.**
2. 🔴 **The minimum-ticket problem dissolves as a margin problem, entirely and at both rails.** `C_min = R ÷ (f − c)` with `R = 0` has no solution: **every ticket clears wherever `f > c`.** The USD 29 / USD 66 / USD 118 / USD 249 break-even ladder is **retired**. ⚠ **What replaces it is not nothing — it is an adoption question. Will a USD 20 saver approve a USD 21.36 request?** That is the new form of the same problem and it is unmodellable pre-launch; carry it as a named risk, not a parameter.
3. 🔴 **The fee-ladder finding REVERSES.** Minimum viable entry fee at USD 75 falls from ~3.07% to **~2.26%** across D31 and D32, so the 3% target clears with **~0.74pp of headroom.** §0.3's conclusion no longer holds; its structural point does. ⚠ **Both steps were reclassifications, not cost reductions — read this with the front-matter pattern note.**
4. ⚠ **The incidence is regressive and it lands on the segment the model is built around.** The gross-up is **1.25% of a USD 20 ticket and 0.33% of a USD 75 one at the Base rail — 6.8% versus 1.8% at the Conservative rail.** The floor band is **40–60% of the book** and is precisely the population D25 found may lack an IBAN-capable account at all. **Aurumix's margin improved by making the poorest customer's deal worse, and the client should hear it in those words.**

⚠ **What the rail pass-through does NOT touch:** redemption. **VARA Annex 2 III.E.4 forbids charging any fee on the way out**, so `F20` (USD 4.20/event) stays absorbed by Aurumix in Stream 0. 🔴 **The asymmetry is now sharp and is worth a line to counsel: Aurumix may pass through the cost of taking money in but is forbidden from passing through the cost of paying it out.**

⚠ **Both columns assume the premium is paid on gross inflow. Under D30 it is paid on net new grams, which lowers COGS further as the book ages and churn builds.** Neither column reflects that yet.

Source: `_draft_purchase-structure.md` §2.2, re-run at the verified gold price and volatility. **Verified clean under audit:** the fabrication premium is on the correct base, and `C − C(1−f)(1+p)` returns the identical USD 1.6125. **The model's revenue line for stream 1a is USD 1.61, never USD 3.75.** The difference is cost of goods sold.

⚠ **Under the dealer-carried float switch (S51), lines 4 and 5 go to zero and the premium in line 2 widens.** v1.0 charges both simultaneously, which double-counts under either regime (correction 12).

**How It Materialises**

1. **Contribution request issued.** Push rail, no mandate — UAEDDS was dropped (`_draft_sip-rulebook.md` §6.2). One rail event per contributing or reduced account per month.
2. **Grace window.** 5 calendar days (F8), rolling forward off weekends and public holidays. **Grace crosses the month boundary and settles the period it was due; a late payment can never close two periods.**
3. **Floor test.** A payment below USD 20 (F6) is **rejected and returned. Nothing is allocated**, and the request stays open for the full amount. This is a hard reject, never a partial credit.
4. **Fee applied.** `base_fee(t) − tier_weighted_discount(s,t)`. Pre-gate and never-gated accounts pay the **full undiscounted rate**.
5. **Price struck at the next published LBMA fix.** Neither side selects the fix — same convention as redemption.
6. **Grams struck and transferred out of the float; AURX minted; float drawdown recorded.** Treasury replenishes on a threshold trigger at one bar denomination.
7. **Margin recognised** in the contribution month. There is no deferral: the fee is consumed at the point of sale.

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Base entry fee | 5.0 / 4.0 / 3.0 (Y1/Y3/Y10) | Decision 9 (F3) — client range + our arithmetic | % |
| Tier entry-fee discount ladder | 0 / 0.4 / 0.8 / 1.2 / 1.5 | `_draft_ics-scoring.md` §6, verified against the master benefit matrix | pp |
| 🆕 Fabrication premium | **1.50 / 0.95** | **100 g / 1 kg (F4, D28). OBSERVED on a same-page dealer pair, Moderate confidence.** Good Delivery retired as a rung. Conservative scenario holds 3.00 | % |
| Price-gap risk (1σ) | **0.79** | Volatility 25% (S6) and a 12.1-day bar fill window at F1 | % |
| 🆕 Float cost of capital — **MEMO LINE, not a margin deduction** | 0.49 / 0.31 / 0.38 | F5 (D32). Opportunity cost on equity, not a cash expense. **No derivation exists in the corpus**; derived from the sized float, §7.5. **The float PRINCIPAL stays on the balance sheet** | % |
| 🆕 Rail cost per event — **PASS-THROUGH, memo only** | **0.25** Base / 0.10 Agg / **1.36** Cons | S1 (D31). AANI unpublished; UAEDDS at AED 5 is Emirates NBD's published tariff. **Grossed up onto the request; drives no margin line** | USD |
| Ticket, per segment | 75 / 40 / 20 / 40 / 30 / 75 | §5 | USD/month |
| Reduced ticket, per segment | MAX(20, 0.50 × ticket) | S29 — **not the hard-coded 20** | USD/month |
| Gold price (flat) | **141.46** | F1, USD 4,400/oz verified 2026-08-17 | USD/g |

**Formula — Monthly (M1–M24)**

```
For each segment s, each period t:

  reduced_ticket(s)      = MAX(20, 0.50 × ticket(s))                      [S29]
  fee_applied(s,t)       = base_fee(t) − tier_weighted_discount(s,t)
    where tier_weighted_discount = Σ_tier [ share(s,t,tier) × discount(tier) ]
    and the PRE-GATE and NEVER-GATED shares carry discount = 0

  sip_inflow(s,t)        = contributing(s,t) × ticket(s)
                         + reduced(s,t)      × reduced_ticket(s)

  net_of_fee(s,t)        = sip_inflow(s,t) × (1 − fee_applied(s,t))

  🆕 D30 — THE PREMIUM IS PAID ON NET NEW GRAMS, NOT GROSS INFLOW.
     Redeemed gold returns to the float and is re-allocated without
     paying the premium a second time.  Only the NET addition to the
     book is procured from the dealer.

  recycled_grams(t)      = grams returned to the float by redemption
                           and self-custody exit in period t
  net_new_grams(t)       = MAX(0, grams_required(t) − recycled_grams(t))
  premium_base(s,t)      = net_of_fee(s,t) × [net_new_grams(t) ÷ grams_required(t)]

  cogs(s,t)              = premium_base(s,t) × fabrication_premium(t)
  gross_margin(s,t)      = sip_inflow(s,t) − net_of_fee(s,t) − cogs(s,t)

  pricegap(s,t)          = sip_inflow(s,t) × pricegap_rate(t) × float_mode
    where float_mode = 0 under DEALER_CARRIED, 1 under OWN_FLOAT             [S51]

  🆕 D32 — THE FLOAT COST OF CAPITAL IS A MEMO LINE, NOT A COGS LINE.
     It is an opportunity cost on equity, not a cash expense.  Booking an
     imputed equity charge inside COGS is not what a P&L does, and §7.6
     already treats locked regulatory capital exactly this way.
     ** The float PRINCIPAL is unaffected: it stays on the balance sheet
        and in the funding view.  Only the imputed CARRY leaves. **

  floatcoc_memo(t)       = float_capital(t) × cost_of_capital ÷ 12   [§7.5]
                           ** reported on Summary, never in a margin **

  🆕 D31 — THE RAIL IS PASSED THROUGH, NOT DEDUCTED.
     The entry fee comprises only what Aurumix charges.  The rail is a
     third-party PSP cost: it is grossed up onto the collection request
     and remitted.  It nets to ZERO in the P&L and must NOT appear in
     STREAM1a.  Compute it as a MEMO row only.

  rail_memo(s,t)         = [ contributing(s,t) + reduced(s,t) ] × S1
  request_amount(s,t)    = ticket(s) + S1        [what the customer is asked for]

  STREAM1a(s,t)          = gross_margin − pricegap
```

⚠ **Keep `rail_memo` as a live row rather than deleting it, for three reasons:** it is the disclosure figure the client must publish alongside the fee; it sizes the pass-through-refusal risk in §13.3; and if D31 is ever reversed the row is already there. **It must not feed the P&L.** The Checks sheet should assert `rail_memo` appears in no revenue or cost total.

**Formula — Annual (Y3–Y7)**

```
For each segment s, each year y:

  contributing(s,y)      = SUM over the 12 constituent months of the CONVOLUTION
                           at each month against the M84 lifecycle curves    [D23]
                           ** NOT a compounded annual hazard, and NOT one
                              convolution on an annual acquisition figure **
  tier_weighted_discount(s,y) = COMPUTED at each of the 12 months from the
                           tenure->tier lookup, then weighted.  Nothing is held
                           or frozen at the seam                            [D21, D22]

  sip_inflow(s,y)        = Σ over the 12 months of [ contributing(s,m) × ticket(s)
                                + reduced(s,m) × reduced_ticket(s) ]
  rail_memo(s,y)         = Σ over the 12 months of
                             [ contributing(s,m) + reduced(s,m) ] × S1
                           ** MEMO ONLY — passed through, never deducted [D31] **

  All rate-based lines are identical to the monthly form applied to the annual base.
  Seasonality does NOT apply — S52a normalises to 12.00 and cancels over a full year.

  STREAM1a(s,y)          = gross_margin − pricegap
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | Compounding on the live-account base, **decaying per account** as the tier ladder deepens the discount |
| What drives growth | Account count × ticket × fee rate. Account count compounds; **fee rate steps down** at Y3 and Y10 with bar denomination; **discount deepens** as the book ages |
| Ceiling | `base(s) × ceiling(s)` under logistic saturation on cumulative-ever-acquired (S22, S23) |
| Lag | None on revenue. **The margin improves with bar denomination**, which lags inflow by 12 months under the trailing-average latch (§3.x.3) |
| Counter-force | **Three at once**: the fee steps down, the discount steps up, and the never-gated share is the only population paying full freight |

**Key Uncertainties**

- 🔴 🆕 **The dealer quote now sets essentially the ENTIRE cost base, and the dealer is unnamed.** With the rail passed through (D31), F4 plus the two float costs are all that remain — so **F4's share of stream 1 cost rises from ~70% to ~54% of a smaller base, but its share of the *controllable* risk rises to nearly all of it.** ⚠ **And F4 got weaker, not stronger, on 2026-08-20: the D28 measurement FAILED REPLICATION** (`supporting/_working_dealer-bid-side-and-vaulting-research.md` §5). The 1.71% / 0.93% Dubai readings came from a dealer rate page that moved 6 bp overnight while its own store moved 241 bp — the two pages do not share a clock. **The 1 kg-vs-100 g step of ~0.78pp reproduced and is independently corroborated; the absolute level did not. Treat F4's level as Low confidence again and the ladder's shape as Observed.**
- 🆕 **The rail no longer decides the sign of the margin — it decides whether the customer says yes.** At S1 Conservative the customer is asked for USD 21.36 rather than USD 20.00. **The AANI cost is still the most valuable unknown number in the engagement, but it is now an adoption input rather than a margin input**, and it moves churn rather than unit economics. ⚠ **This is a harder thing to model, not an easier one:** a margin hit is arithmetic, a refusal rate is behavioural and there is no source for it. **Carry it as a named risk in §13.3, not as a parameter with a Base value.**
- Volatility at 30% rather than 25% pushes price-gap to ~0.95% and gross margin before rail to 0.56%.
- **F5 has no derivation anywhere in the corpus.** v2.0 derives it from the sized float (§7.5) rather than carrying it as a rate, which is the fix — but the underlying cost-of-capital rate is still ours.
- The tier-weighted discount depends entirely on the archetype mix (S27). **If the archetype weights are wrong, the discount is wrong, and it is wrong in the direction of understating cost** if the mix is more disciplined than assumed.

---

### Stream 1b: Entry fee margin — SPOT

**Quick Facts**

| Field | Value |
|---|---|
| Type | Inflow-linked, **lumpy and seasonal** |
| Activation | **M1** |
| Rate | Identical to 1a: base fee **less the account's earned tier discount** |
| Revenue basis | Gross margin retained on spot volume |
| Sheet location | Model, rows 240–264 |
| Status in v1.0 | **Entirely absent.** This is a structural omission, not a missing number |

**What It Is**

A one-off gold purchase outside the SIP schedule. **The gold is identical, the fix is identical, the receipt is identical, the settlement is identical** (`_draft_purchase-structure.md` §4.1) — the only mechanical difference is that stage 1 is an order rather than a schedule.

**The pricing conflict is resolved and it resolved against v1.0's implicit assumption.** `_draft_sip-rulebook.md` §1.1 is authoritative on three independent grounds: it is a **self-labelled correction** that names the tension it fixes (*"a top-tier saver adding a lump sum currently pays the newcomer rate for giving Aurumix more money"*), it is **six days later** than `_draft_purchase-structure.md` §4.3, and **decision 44 ratifies it** (*"entry-fee discount by tier, on every purchase including spot"*). So:

> **"Spot does not earn the tier. It is simply priced at the tier the account already earned."**

`_draft_purchase-structure.md` §4.1's "flat, top of range" and §4.3's "no entry-fee discount" are **superseded** (correction 14). `_draft_sip-spot-and-ics.md` is the oldest of the three and its table still shows a decaying buyback fee that decision 32 killed — **do not use it for spot pricing.**

**How It Materialises**

1. **Order placed.** No mandate, no schedule. **One push or bank transfer, and therefore no collection-failure exposure at all.**
2. **Ticket-band routing.** Below AED 3,500 standard flow; above it Travel Rule data applies; **above AED 50,000 the order exceeds the AANI per-transaction cap** and routes to domestic transfer or wire with enhanced due diligence and source of funds.
3. **Float invariant test.** Above roughly one bar denomination, **procure directly rather than drawing the float**: *"a single order larger than the float would breach the backing invariant and halt minting for everyone else."* Above the threshold, the purchase is quoted as a **two-step: price indication, then execution against a same-day dealer purchase.**
4. **Fee applied at the account's earned tier discount** — the same ladder as SIP.
5. **Price struck at the next fix. Grams allocated. AURX minted.**
6. **Score effects.** `Months` and `Recent` do **not** move. `Sold`'s denominator **does** — spot grams enter Retention on both sides, so buying spot cannot raise the rate and holding it cannot lower it.
7. **Arrears money lands here.** Late money after grace is offered as a spot purchase (`_draft_sip-rulebook.md` §7.1) and buys gold at the fix on the day it clears.

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Spot attach rate | **14%** Base / 24% Agg / 7% Cons | S45. Rises with tenure — a 3-year account is ~2× as likely to buy spot as a 6-month account | % of live accounts/yr |
| Average spot ticket | **620** Base / 1,100 Agg / 320 Cons | S46. **Scale by segment: S1/S6 ×1.6, S2/S4 ×1.0, S3 ×0.45, S5 ×0.7** | USD/event |
| Spot frequency among attachers | **1.7** Base / 2.4 Agg / 1.2 Cons | S47 | events/attaching account/yr |
| Spot seasonality | ~45% of volume in the Akshaya Tritiya (Apr/May) and Diwali (Oct/Nov) windows | S47, S52a | multiplier |
| Arrears-as-spot | ~0.11 events/live account/yr at Base | Derived from the archetype miss rate × a 25–35% make-good rate | events/yr |
| 🆕 Rail cost per event — **PASS-THROUGH, memo only** | **0.25** Base (S1) — **one transfer, not a collection.** Grossed up onto the order; no margin effect (D31) | S1 | USD |
| Large-ticket threshold | one bar denomination (T3) | `_draft_purchase-structure.md` §4.2 | grams |

**Formula — Monthly (M1–M24)**

```
For each segment s, each period t:

  tenure_uplift(s,t)   = 1 + 0.5 × MIN(1, avg_account_age_months(s,t) ÷ 36)
  attaching(s,t)       = live_accounts(s,t) × S45 × tenure_uplift(s,t)
  spot_events(s,t)     = attaching(s,t) × S47 ÷ 12 × spot_seasonality(month_of(t))
                       + arrears_events(s,t)

  spot_ticket(s)       = S46 × segment_scalar(s)
  spot_inflow(s,t)     = attaching(s,t) × S47 ÷ 12 × spot_seasonality × spot_ticket(s)
                       + arrears_events(s,t) × ticket(s)

  fee_applied(s,t)     = SAME as stream 1a — the account's earned tier discount
  gross_margin(s,t)    = spot_inflow − spot_inflow × (1 − fee_applied) × (1 + premium)
  pricegap             = as stream 1a, × float_mode                          [S51]
  floatcoc             = MEMO ONLY — opportunity cost, not COGS        [D32]
  rail_memo(s,t)       = spot_events(s,t) × S1   [MEMO — passed through, D31]

  STREAM1b(s,t)        = gross_margin − pricegap

  FLOAT INVARIANT TEST (a check, not a cost):
    breach(t) = COUNT of orders where spot_ticket ÷ gold_price > float_grams(t)
    → must route to the two-step quote. Report breaches; never net them off.
```

**Formula — Annual (Y3–Y7)**

```
  attaching(s,y)     = live_accounts(s,y) × S45 × tenure_uplift(s,y)
  spot_events(s,y)   = attaching(s,y) × S47 + arrears_events(s,y)
                       [no seasonality term — it cancels over a full year]
  spot_inflow(s,y)   = spot_events(s,y) × spot_ticket(s)
  rail_memo(s,y)     = spot_events(s,y) × S1     [MEMO — passed through, D31]
  STREAM1b(s,y)      = gross_margin − pricegap
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | Compounding on the live base, **amplified by tenure** — the attach rate rises with account age, so the stream grows faster than the account base |
| What drives growth | Live accounts × attach × frequency × ticket. **All four rise together**, which is why the stream is convex in book maturity |
| Ceiling | The same segment ceilings as acquisition; there is no independent spot ceiling |
| Lag | None, but **heavily seasonal**: two festival peaks carry ~45% of annual volume |
| Counter-force | The fee steps down and the discount deepens, exactly as in 1a |

**The finding this stream carries, and it is a strong one.**

Take a USD 620 spot ticket against a USD 75 SIP contribution, both at the Y1 5% fee, on the §0.1 build-up:

| Line | SIP, USD 75 | Spot, USD 620 |
|---|---|---|
| 🆕 Gross margin at 5% less **1.50%** premium, 0.79% price-gap (D28, D32) | **2.79% → USD 2.09** | **2.79% → USD 17.30** |
| 🆕 Rail — **PASSED THROUGH** (D31) · Float CoC — **MEMO** (D32) | — | — |
| **Net margin** | **USD 2.09** | **USD 17.30** |
| **Net margin as % of ticket** | **2.79%** | **2.79%** |
| 🆕 **At the Conservative rail (S1 = USD 1.36)** | **unchanged** | **unchanged** |

🔴 🆕 **THE FINDING THIS STREAM CARRIED IS WITHDRAWN BY D31.** It said *"spot remains structurally the highest-margin inflow in the business."* **It is not, and it never was a property of spot.** The 2.25%-vs-1.96% gap was **entirely** the fixed rail spread over an 8.3× larger base. Remove the rail from the margin and the two lanes are **identical at 2.79%**.

**What survives, and it is the honest version:** spot is **larger per event** (USD 17.30 against USD 2.09), so it is worth having and worth modelling. But **it is not better per dollar**, and any argument that leans on spot's superior margin — the referral economics, the fee-ladder defence, the case for pushing spot in the app — **must be re-checked against 2.79%, not 2.25% versus 1.96%.**

**This claim has now moved twice in three days.** v2.0: *spot is the only lane that survives the adverse rail* (withdrawn by D28 — the SIP clears it at +USD 0.36). v2.4: *spot is structurally the highest-margin inflow* (withdrawn by D31 — the lanes are equal). ⚠ **Both withdrawals ran the same way: a claim about spot turned out to be a claim about the rail wearing spot's clothes. Treat any remaining spot-superiority argument in this brief as suspect until re-derived.**

⚠ **The two qualifications below are untouched by this and now carry the whole case for the lane.** Spot earns no ICS, and spot volume is lumpy and seasonal.

Two qualifications keep it honest. **Spot earns no ICS**, so it builds no tier, no card eligibility and no credit eligibility — **it is margin without a funnel**, and the conclusion that the SIP is an acquisition mechanism for the card still stands. And spot volume is lumpy and seasonal, so it **cannot be relied on to cover a fixed cost base. Spot improves the margin on stream 1; it does not change what the business is.**

**Key Uncertainties**

- **S45, S46 and S47 are all Low confidence with no published source.** There is no spot-attach benchmark for any comparable gold or savings product anywhere.
- **The float invariant is live from launch, not a Year 3 concern.** At a Y1 float of ~USD 28k, a single USD 100,000 order **breaches backing by 3.5×.** The two-step quote must exist at M1.
- **Spot and SIP now differ on one lever, not two.** With the price lever extended to spot (decision 44) and the time lever retired (D8), only credit — with its companions, card tier and family features — differentiates them. **The corpus's own open item says two; it is out of date in the direction of understating the problem.** §16 carries the decision; **this stream's output is what sizes it.**

---

### Stream 2: Card interchange

**Quick Facts**

| Field | Value |
|---|---|
| Type | Activity-linked |
| Activation | **M18 assumed** (sponsor bank live) |
| Gate | **Gold tier**, i.e. month 12 of a clean run at the earliest |
| Rate | 1.80 / 2.05 / 2.10% by tier (F12), **× PM share, less per-transaction fee** |
| Sheet location | Model, rows 300–349 |
| Share of terminal revenue | The largest single stream. **54.3% of Y10 gross profit** (USD 4,156,380 of USD 7,657,206). With cardholder fees it is **83.4%** |

**What It Is**

Aurumix's share of the interchange a merchant's acquirer pays on every card transaction, retained through the programme manager relationship. **This is the business.**

**The verified interchange ladder** (Visa UAE IRF schedule effective 18 Oct 2025; CBUAE Notice 1998/2024 cap on debit and prepaid effective 1 Oct 2024). Confidence **High, primary scheme document.**

| ICS tier | Card level | Visa product | Interchange | Gold Rewards rate | Spend multiplier (S38) | Avg ticket (F23) |
|---|---|---|---|---|---|---|
| Gold | L1 | Platinum | **1.80%** | 0.15% | 0.82× | AED 185 |
| Platinum | L2 | Signature | **2.05%** | 0.45% | 1.12× | AED 240 |
| Sovereign | L3 | Infinite | **2.10%** | 0.75% | 1.54× | AED 310 |
| *(prepaid, all products)* | — | — | *1.00% flat, capped* | — | — | — |

**How It Materialises**

1. **Tier reached.** Gold or above, from the **convolved tenure→tier lookup** (D22), per archetype curve, thresholded then weighted. ⚠ **Eligibility is what this step delivers and it is a live engine; the rate that follows is flat** — see step 4.
2. **Card issued and activated.** `S5` activation rate on eligible accounts. Plastic is sticky — **never downgrades** — and upgrades on **3 consecutive months** at the qualifying tier before reissue (`_draft_ics-scoring.md` §6.3).
3. **Spend occurs**, at that tier's multiplier and that month's seasonality (S52b).
4. **Gross interchange accrues at the FLAT GOLD RATE** on the transaction value (D22). ⚠ **Not at the tier's own rate.** The 1.80 / 2.05 / 2.10 ladder is collapsed; the measured cost is **3.1% of gross profit at Y10 and ~2% at Y7**, because Sovereign is 1.2% of tiered accounts by Y7. **The full ladder survives on the ICS Validation sheet, where the 5% safety gate is computed against it** (§3 Layer 5d).
5. **The programme manager retains its contracted share (S3); the processor takes a per-transaction fee (F24) on top.**
6. **Fraud, disputes and programme fixed costs net off** (S39, F25, F27).
7. **Gold Rewards is haircut off the net**, capped at the customer's own generated revenue net of custody.

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Interchange rate by tier | 1.80 / 2.05 / 2.10 | **Visa UAE IRF schedule, 18 Oct 2025. Primary** (F12) | % |
| **PM share of gross interchange** | **72** Base / 85 Agg / **55** Cons | S3. **No UAE or MENA split is published anywhere. Confirmed negative across two research passes** | % |
| PM share by contract maturity | 55% Y2–Y3, stepping to 72% Y5+ | T6. **Use Low for M18–M30** — sub-scale, novel collateral profile | % |
| Monthly spend per active card | **6,000** Base / 9,000 Agg / **3,500** Cons | S4. Expat survey mean AED 6,170; Kinesis cap implies AED 7,345 | AED |
| Spend tier multiplier | 0.82 / 1.12 / 1.54 | S38. Normalises to 1.018 at the Y10 mix — 1.8% over target, within tolerance | × S4 |
| Card activation rate | **65** Base / 80 Agg / 45 Cons | S5. Triangulated from PULSE (68.2%) and Monzo (68%). **Use High if issued only to funded balances** | % |
| **Per-transaction processor fee** | **0.10** Base / 0.05 Agg / 0.15 Cons | F24. **Stripe Issuing's published rate.** Authorisation-based, so **add 6% for declines** | USD/txn |
| Average transaction size | 185 / 240 / 310 | F23. Implies ~27 / 28 / 30 transactions/month | AED |
| Fraud and chargeback loss | **9** Base / 5 Agg / 22 Cons | S39. Visa's published global average is ~8 bps; Base sits slightly above for a new BIN | bps of spend |
| Dispute handling | 22 / 14 / 40 at 0.9 cases per 1,000 txns | F25 | USD/case |
| Programme fixed costs | **180,000** Base / 106,000 Agg / **340,000** Cons annualised from M18 | F27 | USD/yr |
| Spend seasonality | Normalised to exactly 12.00 | S52b | multiplier |

**Formula — Monthly (M18–M24)**

```
For each tier k ∈ {Gold, Platinum, Sovereign}, each period t:

  eligible(t,k)      = accounts at tier k, from the CONVOLVED tenure->tier
                       lookup (D22, D23) — eligibility is computed, never assumed
  active_cards(t,k)  = eligible(t,k) × S5
  spend(t,k)         = active_cards(t,k) × S4 × S38(k) × S52b(month_of(t))
  gross_ic(t,k)      = spend(t,k) × F12_GOLD ÷ AED_per_USD
                       ** FLAT GOLD RATE, not F12(k). Ladder collapsed, D22 **

  txns(t,k)          = spend(t,k) ÷ F23(k) × 1.06                [+6% declines]
  txn_fee(t,k)       = txns(t,k) × F24

  net_ic(t,k)        = gross_ic(t,k) × PM_SHARE(t) − txn_fee(t,k)

  EFFECTIVE PM SHARE(t,k) = net_ic(t,k) ÷ gross_ic(t,k)          [REPORT THIS ROW]

  fraud(t)           = Σ_k spend(t,k) × S39 ÷ 10,000
  disputes(t)        = Σ_k txns(t,k) × 0.0009 × F25
  fixed(t)           = F27 monthly run-rate, from M18
                     + F27 one-offs booked in M15

  gold_rewards(t,k)  = MIN( spend(t,k) capped at F13 × rate(k),
                            net_ic(t,k) + stream5_attributable(t,k)
                            − custody_cost(t,k) )                [cap, never negative]

  STREAM2(t) = Σ_k [ net_ic(t,k) − gold_rewards(t,k) ] − fraud − disputes − fixed
```

**Formula — Annual (Y3–Y7)**

```
  active_cards(y,k)  = average of opening and closing counts at the tier mix
                       COMPUTED at each of the year's 12 months.  Nothing held
  spend(y,k)         = Σ over the 12 months of active_cards(m,k) × S4 × S38(k)
                       [no S52b — it normalises to 12.00 and cancels]
  txns(y,k)          = spend(y,k) ÷ F23(k) × 1.06
  All other lines are the monthly forms applied to the annual base.
  fixed(y)           = 12 × monthly minimums + 4 × quarterly scheme assessments
  STREAM2(y)         = Σ_k [ net_ic − gold_rewards ] − fraud − disputes − fixed
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | **Step at M18, then compounding on two multiplying bases** — cardholder count and tier mix |
| What drives growth | Gold+ population × activation × spend × rate. **The tier mix is the second engine**: as the book ages, mix shifts up, and the rate rises with it |
| Ceiling | Gold+ share of the live book × activation. Bounded above by the archetype mix — **only 10% of the book can ever reach Sovereign** |
| Lag | **18 months of zero.** Then a 12-month PM-share step at ~M30 as the contract matures (T6) |
| Counter-force | **The per-transaction fee is regressive** and hits hardest in the early years when the mix is bottom-heavy. **F27 fixed costs bind at low volume**, running the programme at a loss for its first 12–18 months in the Conservative case |

**Key Uncertainties**

- 🔴 **`PM_SHARE` is the most valuable commercial number in the engagement.** No UAE or MENA split is published anywhere. The best derivation: Marqeta's FY2025 10-K states it receives **all** interchange and pays the PM out of it as a revenue share recorded as a reduction to net revenue — so its net take rate is what the **processor keeps**. `624,884k ÷ 382,513m = 16.34 bps of volume`; at UAE credit interchange of 1.80–2.30% that implies **the PM retains 90.9% to 92.9%.** That upper bound is not transferable — Marqeta's blended rate is set by Block/Cash App, its dominant customer with maximum leverage. Flooring with the Polymath BIN-sponsorship benchmark (sponsor takes 25–50%) gives the range. **Recommended: Base 72%, High 85%, Low 55%.**
- **The floor Phase 2 already established is 36%.** Below a 36% PM share, Gold Rewards at 0.75% stops self-funding at Sovereign (`_draft_credit-and-card-infrastructure.md` §8.2; 0.75 ÷ 2.10 = 35.7%, verified). **Take 36% into the NymCard and sponsor conversations as the walk-away.**
- 🔴 **The credit-versus-prepaid decision is not a product choice, it is the business model.** Prepaid caps interchange at 1.00% by CBUAE notice; credit runs 1.80–2.30% uncapped. **It must be a binary switch in the model** (§13), not a footnote — v1.0 cannot represent it at all.
- **Cross-border interchange sits above domestic and outside the cap, and no cross-border rate is published.** For an expatriate base cross-border is the norm rather than the tail, so **the model carries domestic only and is conservative by an unknown margin on stream 2** — while S34 correctly sizes the same exposure on stream 4. **The asymmetry should be flagged, not fixed.**
- **No official UAE per-card spend figure exists.** CBUAE collects BIN-level data and publishes none. **Weight the Low case heavily in the first two years**, because a new entrant's card is a secondary card until it is not.

---

### Stream 3: Family plan and Digital Will

**Quick Facts**

| Field | Value |
|---|---|
| Type | Headcount-linked |
| Activation | **M1** |
| Gate | **None.** Open to everyone who pays; **tier only prices it** |
| Rate | USD 29–36/yr including up to 4 beneficiaries; USD 20 per additional name, capped ~USD 60/household |
| Sheet location | Model, rows 350–369 |

**What It Is**

An annual plan fee for registering beneficiaries and a Digital Will over the customer's gold. Charged **at registration and never at the transfer event** — which matters, because the transfer event is the one that costs money.

**How It Materialises**

1. **Account holder opts in.** Attach rate S11 on live accounts, any tier including none.
2. **Beneficiaries registered.** Identity verification and AML/PEP/sanctions screening at onboarding, per name.
3. **Plan fee charged annually**, discounted by the tier ladder (0 / 10 / 20 / 35 / 50%) plus a per-beneficiary discount (0 / 0 / 0 / 10 / 20%) starting only at Platinum.
4. **Continuous screening runs for the life of the registration** — 20 to 40 years — at USD 0.36/name/year.
5. **On death, transfer executes.** Gold moves inside the product to the beneficiary's account. **Not a sale, so it does not touch Retention** (`_draft_ics-scoring.md` §1.5).

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Attach rate | **20** Base / 35 Agg / 10 Cons | S11. **Nothing stated anywhere in the corpus** — pure assumption, flagged | % of live accounts |
| Plan price | 29–36 | `_draft_family-and-succession.md` §11, **awaiting client sign-off** | USD/yr |
| Additional name | 20, capped ~60/household | Same | USD |
| Tier plan-fee discount | 0 / 10 / 20 / 35 / 50 | `_draft_ics-scoring.md` §6.5 | % |
| Per-beneficiary discount | 0 / 0 / 0 / 10 / 20 | Same — **starts only at Platinum**, so the cheaper lever does the early work | % |
| Identity verification | 1.25–1.85 | `_draft_family-and-succession.md` §11 | USD one-off |
| AML/PEP/sanctions at onboarding | 0.35–1.05 | Same | USD one-off |
| Continuous screening | **0.36** | Same. **Per name, per year, for 20–40 years** | USD/yr |
| Platform minimum | **299 + 1.85/check** | F16, **Sumsub's own pricing page.** Binds below 162 checks/month | USD/mo |

**Formula — Monthly (M1–M24)**

```
For each segment s, each period t:

  plans(s,t)        = live_accounts(s,t) × S11
  names(s,t)        = plans(s,t) × avg_beneficiaries       [4 included, tail above]
  price(s,t)        = plan_price × [1 − tier_weighted_plan_discount(s,t)]
                    + extra_names(s,t) × 20 × [1 − tier_weighted_name_discount(s,t)]

  STREAM3(s,t)      = new_plans(s,t) × price(s,t)                 [charged annually]
                    + renewing_plans(s,t) × price(s,t)            [at each anniversary]

  COST (to §7.2, not netted here):
    onboarding(t)   = new_names(t) × (identity + aml)
    screening(t)    = cumulative_registered_names(t) × 0.36 ÷ 12
    platform(t)     = MAX(299, 1.85 × kyc_checks(t))              [F16 floor]
```

**Formula — Annual (Y3–Y7)**

```
  plans(s,y)        = average live accounts × S11
  STREAM3(s,y)      = plans(s,y) × price(s,y)          [every plan renews once a year]
  screening(y)      = cumulative_registered_names(y) × 0.36
  platform(y)       = 12 × MAX(299, 1.85 × monthly_kyc_checks(y))
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | **Linear on the live account base**, decaying per unit as the tier mix deepens the discount |
| What drives growth | Live accounts × attach rate × names per plan. **No compounding mechanism** — this is the only stream with none |
| Ceiling | The attach rate itself. There is no second engine |
| Lag | None. Live from M1, the only card-independent stream besides 1a and 1b |
| Counter-force | **The screening tail.** Every registered name is a 20-to-40-year liability at USD 0.36/yr; the cost base grows with cumulative registrations while revenue grows with live ones |

**Key Uncertainties**

- **The attach rate is a pure assumption with nothing behind it.** It is the single loosest input in the stream and it scales the whole thing linearly.
- **Two costs bind harder than the per-check rate.** The **monitoring tail** — a registered beneficiary stays screened for decades, roughly **USD 7 to 14 per name undiscounted**, and **no provider publishes multi-decade terms.** And the **platform minimum** — USD 299/month binds until ~162 verifications a month, so **at launch volumes the marginal name is nearly free and the fixed minimum is what hurts.** This is the same minimum-commitment pattern as the DGCX vault and the F27 card programme; **§7.4 should name it as a pattern, because it is the third instance.**
- **Headroom is real but not enormous.** A Sovereign at the deepest discount pays ~USD 15–18/year against a USD 2.90 per-name floor — 5× headroom, before the screening tail.
- 🔴 **One leg is a mandatory cost centre with zero revenue by construction.** For an India-resident beneficiary the estate must settle to cash; **cash settlement is probably a redemption; and III.E.4 forbids a fee on redemption. It is the most operationally expensive leg and it carries no revenue and can carry none.**

---

### Stream 4: Cardholder fees (FX, ATM, issuance)

**Quick Facts**

| Field | Value |
|---|---|
| Type | Activity-linked |
| Activation | **M18**, with the card |
| Gate | Gold tier |
| Three bases | FX margin on foreign spend; ATM withdrawals beyond the free allowance; issuance and replacement events |
| Sheet location | Model, rows 370–399 |

**What It Is**

The fee revenue a cardholder pays directly, as opposed to the interchange a merchant pays. **This stream nets against stream 2 by design: every card benefit is a waiver of stream 4 revenue funded by the stream 2 interchange the same spender generates.**

**How It Materialises**

1. **Foreign-currency spend occurs.** FX margin applied at the tier rate.
2. **ATM withdrawal occurs.** Free up to the tier allowance, then 2% on the excess. **Allowance is monthly and does not roll.**
3. **Card issued or replaced.** Fee at the tier rate, waived at upper levels.
4. **Every one of the three is tier-waived**, so the model must forecast **by tier, never in aggregate.**

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| FX margin by tier | **2.0 / 1.5 / 1.0** | `_draft_ics-scoring.md` §6.3. Market rate ~2.0%, converged across Nexo, Crypto.com, Wirex | % |
| Free ATM allowance by tier | **1,000 / 2,500 / 5,000** | Same. Monthly, **not rolling** | AED/mo |
| Over-allowance ATM fee | 2.0 | Sector converged, with a ~USD 200/month free tier at entry level | % |
| Foreign spend share | **34** Base / 45 Agg / 24 Cons | S34, **applied as a seasonal vector (S53), not a constant** | % of spend |
| Foreign-spend seasonal vector | 30/30/30/32/34/**55**/**60**/**56**/36/42/40/32, rescaled to hold the 34% mean | S53 | % by month |
| ATM draw distribution | 60% draw AED 0–500; 25% 500–1,500; 12% 1,500–3,000; **3% 3,000+** | S35. Mean ~AED 940 | % of cardholders |
| Issuance fee | 75 / waived / waived | F21. `_draft_ics-benefits.md`: *"issuance and replacement charged at base level, waived at upper levels"* | AED |
| Replacement fee | 100 / 50 / waived | F22 | AED |
| Issuance event rate | 1.00 at activation, **+0.06/yr thereafter** | S36. Renewal churn plus **tier upgrades, which force a physical reissue** | events/card/yr |
| Replacement event rate | 0.11 Base / 0.07 Agg / 0.18 Cons | S37 | events/card/yr |
| Card production unit cost | 4.50 / 7.00 / 14.00 | F26. **At Sovereign, production cost exceeds the AED 0 issuance fee by construction** | USD/card |

**Formula — Monthly (M18–M24)**

```
For each tier k, each period t:

  foreign_share(t)   = S53(month_of(t))      [seasonal, NOT flat S34]
  foreign_spend(t,k) = spend(t,k) × foreign_share(t)
  fx_rev(t,k)        = foreign_spend(t,k) × fx_margin(k)

  ATM — computed over the S35 DISTRIBUTION, never on the mean:
  atm_rev(t,k) = active_cards(t,k)
               × Σ_bucket [ weight(bucket)
                          × MAX(0, midpoint(bucket) − allowance(k)) × 0.02 ]

  issue_rev(t,k)     = issuance_events(t,k) × F21(k) + replacement_events(t,k) × F22(k)
  issue_cost(t,k)    = (issuance + replacement events) × F26(k)     [contra]

  STREAM4(t) = Σ_k [ fx_rev + atm_rev + issue_rev − issue_cost ] ÷ AED_per_USD
```

**Formula — Annual (Y3–Y7)**

```
  foreign_share(y)  = S34 annual mean (34%)   [S53 normalises out over a full year]
  foreign_spend(y,k)= spend(y,k) × S34
  atm_rev(y,k)      = Σ over the 12 months of the monthly distribution formula,
                      each at that month's own convolved card count and tier mix.
                      Nothing held or frozen at the seam                 [D21]
  issue events      = active_cards(y,k) × (S36 + S37)
  STREAM4(y)        = Σ_k [ fx_rev + atm_rev + issue_rev − issue_cost ] ÷ AED_per_USD
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | Tracks stream 2's cardholder base, **but with the opposite tier gradient** |
| What drives growth | Cardholders × foreign share × spend. **Summer travel is the single largest month by FX revenue even though it is the weakest total-spend month** |
| Ceiling | Same Gold+ population as stream 2 |
| Lag | 18 months of zero, identical to stream 2 |
| Counter-force | 🔴 **The tier that spends most is the tier whose fees are most waived.** As the book matures upward, **stream 4 revenue per cardholder falls** even as stream 2's rises. **These two streams must never be blended** |

**Key Uncertainties**

- 🔴 **The summer sign error, and it is a build instruction not a number.** Total spend dips June–August (fewer people in-country) but **foreign spend share spikes to 55–60%**, and FX margin is a revenue line. **A flat foreign-share assumption applied to a seasonalised spend vector gets the sign of the summer effect backwards.** Apply S34 as the S53 vector.
- **The ATM allowance is deliberately set above the median draw**, so **at Base the median Gold cardholder never breaches it** and over-allowance revenue comes almost entirely from a small high-cash tail. **Applying 2% to `MAX(0, 950 − 1,000)` returns exactly zero.** The distributional treatment is the important part.
- **F21, F22, S36 and S37 are cosmetic.** A few AED per card per year against AED 6,000/month of spend — rounding error. Get them roughly right and move on.
- **VAT touches every line in this stream** and the resident/non-resident split (S49) decides how much of it bites. See §7.6.

---

### Stream 5: Lending revenue share

**Quick Facts**

| Field | Value |
|---|---|
| Type | Activity **and** stock |
| Activation | **M24 assumed** (lending partner signed) |
| Gate | Gold tier |
| Risk | **Aurumix takes no credit risk.** The lender of record advances the money and owns the book |
| Sheet location | Model, rows 400–439 |

**What It Is**

A revenue share on a gold-collateralised credit facility originated by Aurumix and funded by a partner. **A VARA Lending licence cannot advance fiat against gold, so partnering is confirmed rather than merely likely.** Five heads: interest share, origination, servicing, penal and recovery.

**How It Materialises**

1. **Collateral seasons.** 90 days (F10), unpledged, held by a Gold+ account.
2. **Facility struck** at the tier's LTV: 50 / 65 / 80% (F11, settled 2026-08-13).
3. **Customer draws.** Draw event fires the origination fee.
4. **Balance revolves and repays.** Realised tenor ~71 days, so **peak drawn ≠ average drawn** (S40).
5. **Annual facility review.** Limit re-strikes to the current tier; **existing drawn balances run to term at the originally struck LTV.** The model carries a **vintage of drawn balances by struck LTV**, not a single balance.
6. **On a margin call, the float absorbs the sale** — the float's fifth job (`_draft_credit-and-card-infrastructure.md` §6.6), flowing into the same net-flow calculation as redemptions rather than a separate physical sale.

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| LTV ladder | **50 / 65 / 80** | F11, settled 2026-08-13. **No longer contingent on the partner** | % |
| Collateral seasoning | 90 | F10, benefits draft §2.5 | days |
| Take-up among eligible | **18** Base / 30 Agg / 8 Cons | S8. Indian gold-loan penetration <10% at a point in time; pre-selection uplift, but competes against 6.5–7.5% APR unsecured UAE credit | % |
| Drawn as % of permitted | **50** Base / 70 Agg / 30 Cons | S9. Revolving facilities draw 40–55% of permitted | % |
| Realised LTV | 57 | Manappuram actual, Q4 FY26, against a 75% cap. **Not the 80% ceiling** | % |
| **Peak-to-average conversion** | **0.42** Base / 0.55 Agg / 0.30 Cons | S40. Derived: 71 ÷ 365 = 0.195/draw × S41 = 2.1 draws/yr → 0.41, rounded for the revolving design | × peak |
| Draw events/borrower/yr | 2.1 Base / 3.2 Agg / 1.3 Cons | S41. **Moves with S40 — do not flex independently** | events/yr |
| Origination fee — gross / Aurumix share | **1.00% of draw / 50%** | F28. **Finance House's UAE gold loan Key Facts Statement carries a 1% processing fee** — the one gross rate with a real UAE anchor. The split is term-sheet | % / % |
| Servicing fee — gross / share | 0.50%/yr of drawn / **70%** | F29. Share set **highest of the four heads**: servicing is where Aurumix does the actual work — app, statements, collateral monitoring, LTV recalculation, margin-call triggering | % / % |
| Penal fee — gross / share | 2.00% per late event / **40%** | F30. Share set **low on purpose**: penal income belongs economically to whoever bears the credit risk, and **Aurumix bears none** | % / % |
| Recovery fee — gross / share | 1.50% of recovered / **0%** | F31. 🔴 **Modelled at zero. See below** | % / % |
| Pricing corridor | 9% reducing (Emirates Money) to 16% (Finance House) | Two actual UAE gold products | % APR |

**Formula — Annual block only (Y3–Y7); zero through M24, no stub month**

```
For each tier k, each period t, each vintage v:

  eligible_collateral(t,k) = grams seasoned 90 days, unpledged, held by tier-k accounts
  facility_limit(t,k)      = eligible_collateral(t,k) × gold_price × F11(k)
  borrowers(t,k)           = eligible_accounts(t,k) × S8

  peak_drawn(t,k)          = facility_limit(t,k) × S8 × S9
  avg_drawn(t,k)           = peak_drawn(t,k) × S40                  [THE CORRECTION]

  VINTAGING — carry drawn balances by the LTV they were STRUCK at, not the current tier:
    avg_drawn(t, struck_ltv=v) rolls forward on its own amortisation to term;
    only NEW draws in period t are struck at the CURRENT tier's F11.

  draw_events(t,k)         = borrowers(t,k) × S41 ÷ 12

  interest_share(t)   = Σ_v avg_drawn(t,v) × aurumix_interest_share ÷ 12
  origination(t)      = Σ_k draw_events(t,k) × avg_draw_size(k) × F28_gross × F28_share
                        [PER EVENT — NOT scaled by S40; rises with turnover]
  servicing(t)        = Σ_v avg_drawn(t,v) × F29_gross × F29_share ÷ 12
  penal(t)            = Σ_k overdue_balance(t,k) × F30_gross × F30_share
  recovery(t)         = 0                                           [F31, see below]

  STREAM5(t) = interest_share + origination + servicing + penal + recovery
```

**Formula — Annual (Y3–Y7)**

```
  avg_drawn(y,v)     = average of opening and closing vintage balances
  draw_events(y,k)   = borrowers(y,k) × S41
  interest_share(y)  = Σ_v avg_drawn(y,v) × aurumix_interest_share
  servicing(y)       = Σ_v avg_drawn(y,v) × F29_gross × F29_share
  origination(y)     = Σ_k draw_events(y,k) × avg_draw_size(k) × F28_gross × F28_share
  STREAM5(y) = interest_share + origination + servicing + penal + 0
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | Compounding on the collateral base, which compounds on AUM |
| What drives growth | Eligible collateral × LTV × take-up × drawn% × **turnover**. The LTV ladder rises with the tier mix, so **the benefit ladder is revenue-positive here** — a rare case |
| Ceiling | Gold+ collateral × 80% at the very top. Bounded hard by the Sovereign share, which the archetype mix caps at ~10% |
| Lag | **24 months of zero**, then a 90-day seasoning lag on every new gram |
| Counter-force | 🔴 **Turnover.** The stream is sized on *average* drawn, not peak, and the two differ by 2.4× |

**Two structural effects to build in, both empirically anchored.** Manappuram's realised tenor is **71 days against a 6–12 month product**: gold borrowers redeem fast, so drawn balances are **episodic, not persistent**. And the Finance House Key Facts Statement shows **bullet repayment generating 1.83× the interest of EMI** on identical principal, rate and term (AED 6,400 vs AED 3,503 on AED 20,000 over 24 months at 16%). **A revolving non-amortising facility earns closer to bullet economics, which materially favours the revolving design.**

**Combined fee-head check.** At Base and a USD 20,000 average facility drawn at 50%: origination `USD 100 × 50% = USD 50` per draw event; servicing `USD 10,000 × 0.50% × 70% = USD 35/yr`; penal ~USD 4/yr expected; recovery USD 0. **Against an interest share of ~4pp on a USD 10,000 average drawn balance = USD 400/yr, the four fee heads add roughly USD 90–110/yr, i.e. a 20–25% uplift on the interest share. Material but not transformative — which is the right expectation to set before the partner conversation, because it says the fee heads are not where stream 5 is won.**

**Key Uncertainties**

- 🔴 **Stream 5 falls 49× against v1.0, and S40 is only the smaller half of why.** v1.0 books peak drawn as though persistent *and* credits Gold+ accounts with a share of total AUM. Correcting both **takes stream 5 from roughly USD 600k to USD 12,135 at Y10** — decomposed: v1.0's basis gives USD 70,035; applying S40 = 0.42 to the interest component gives USD 37,290 (a **1.88×** fall); computing the collateral base **per HOLDING account** gives USD 12,582 (a further **2.96×** fall); the residual to USD 600k is v1.0's AUM overstatement. **The collateral-base correction dominates, not turnover.** **This makes v1.0's own §0.4 headline stronger, not weaker: the card is an even larger share of the business than v1.0 states.** It should be corrected rather than defended.
- 🔴 **Model Aurumix's recovery-fee share at ZERO in Base and Conservative, and treat any recovery income as upside only.** *"Counsel question, not raised anywhere previously: is an enforcement sale a 'redemption' under VARA III.E.4? If it is, no fee may be charged on it, and **the recovery costs in stream 5 become unchargeable.** Our view is that a secured creditor's enforcement sale is not a customer-exercised redemption right. **It has not been tested.**"* **Aurumix is precisely the party exposed to the recharacterisation risk** — it holds the gold and executes the sale — while the partner, charging a recovery fee on its own loan under its own licence, is not. **The conservative reading is that Aurumix's recovery fee is the one fee head it structurally cannot charge. Recording that as zero is a finding, not a gap**, and it costs almost nothing because recovery events are rare.
- ⚠ **Check whether a penal charge on a gold-collateralised facility survives an Islamic-finance sponsor.** The corpus flags that this becomes binding if the sponsor is ADIB.
- ⚠ **Aurumix would be valuer, collateral agent and buyer simultaneously.** The cure is mandating the **LBMA fix with zero discretion**, disclosed at the draw, with the sale price and gram count reported to the customer. Nothing to price, but *"without that, this is the line a regulator or a claimant pulls on"* — it belongs in the risk register at §14.
- **Every one of the five fee heads is unpriced in the corpus.** F28–F31 are our constructions, with only F28's gross rate carrying a real UAE anchor.
- **The collateral chain is two links open, three designed**, not three open. `_draft_credit-and-card-infrastructure.md` §7's header says *"Two are strong, three are open"* but the table marks **two open** (a valid security interest; the sale) and **three resolved** (immobilisation, valuation-and-trigger, cure). **The table is operative; the header is stale.** Correction 19 at §15.

---

### Stream 6: B2B platform fee

**Quick Facts**

| Field | Value |
|---|---|
| Type | **AUM-linked** |
| Activation | **M24 assumed**, with a **Week 1 build requirement** |
| Gate | None — partner accounts earn no ICS |
| Rate | **Placeholder 0.5–0.75%/yr**, invoiced monthly in cash |
| Sheet location | Model, rows 440–459 |

**What It Is**

**The only line in the model that scales directly with assets under management, and it costs no customer acquisition.** A white-label platform fee charged to a distribution partner on the AUM of that partner's own customer book.

**How It Materialises**

1. **Partner signs** and integrates against the multi-tenant register and mint.
2. **Partner's customers accumulate gold** on that partner's own clock — each partner runs its own S43 maturity ramp from its own go-live.
3. **Aurumix invoices monthly, in cash**, on the closing AUM stock.
4. **Partner-channel accounts earn no ICS** (`_draft_ics-scoring.md` §1.9), so they **consume none of the five benefit costs. Structurally the highest-margin book in the model.**

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Partner count by year (Y2/Y3/Y4/Y5/Y7/Y10) | **1 / 2 / 3 / 4 / 6 / 8** Base; 1/3/5/7/11/15 Agg; 1/1/1/2/2/3 Cons | S42. Enterprise sales cadence for a pre-revenue infrastructure vendor | partners |
| Per-partner AUM ramp | **8 / 25 / 48 / 70 / 85 / 100%** at M6/M12/M24/M36/M48/M60 of *that partner's* maturity | S43. Standard enterprise-integration adoption: slow first two quarters, steep M12–M30, asymptotic after | % of terminal |
| Terminal AUM per partner | **32** Base / 45 Agg / 22 Cons | S44. Reconciles to S13's USD 200m at Y10 | USD m |
| Total partner AUM at Y10 | **200** Base / 400 Agg / 50 Cons | S13 | USD m |
| Platform fee rate | **0.50–0.75** | Placeholder. Worked corpus example: USD 100m at 60 bps = USD 600,000/yr recurring | %/yr |

**Formula — Annual block only (Y3–Y7); zero through M24, no stub month**

```
For each partner p, each period t:

  maturity(p,t)      = t − go_live_month(p)
  ramp(p,t)          = S43_lookup( maturity(p,t) )       [interpolated between anchors]
  partner_AUM(p,t)   = S44_terminal(p) × ramp(p,t) × india_factor

    where india_factor = 1 if INDIA_ENABLED, else 0.40
    [the B2B row is 60% S5 per S16 — the two switches are NOT independent]

  STREAM6(t) = Σ_p partner_AUM(p,t) × bps_rate ÷ 12

  ZERO entry-spread revenue from the partner channel. See below.
```

**Formula — Annual (Y3–Y7)**

```
  partner_AUM(p,y)   = average of opening and closing AUM for partner p
  STREAM6(y)         = Σ_p partner_AUM(p,y) × bps_rate
```

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | **Stacked S-curves.** Each partner runs its own 60-month ramp from its own go-live |
| What drives growth | Partner count × per-partner terminal AUM × each partner's own maturity |
| Ceiling | S13's total partner AUM. **Reconciliation check: partners 1–4 at 85–100% of USD 32m ≈ USD 122m; partners 5–8 at 8–48% ≈ USD 68m; total ≈ USD 190m against the S13 target of 200m** |
| Lag | **24 months of zero, then a further 12–24 months per partner before the first partner is material.** Partners signed in Y7 are still ramping at Y10 |
| Counter-force | **The terminal figure is reached by a small number of mature partners plus a tail of immature ones**, never by all partners at full size |

**Key Uncertainties**

- 🔴 **The SafeGold warning must be encoded, not merely noted.** SafeGold — the closest analogue, B2B2C digital gold through 100+ partner apps, 55m customers, ₹6,867 cr of gold transacted in FY25 — runs an **EBITDA margin of 0.03%.** Roughly ₹2 crore of EBITDA on ₹6,867 crore of volume. **Distributing grams on the spread is not a business at Indian retail scale.** So the model must book **zero entry-spread revenue from the partner channel** and take stream 6 revenue **only from the AUM platform fee.** The partner keeps 70–80% of the entry spread, and the remaining 20–30% does not survive the fabrication premium and rail on the partner's own ticket sizes. **If the model books partner entry-fee margin, it is reproducing exactly the error SafeGold's accounts disprove.**
- 🔴 **Stream 6 is coupled to the India switch and v1.0 leaves them independent.** Per S16, the B2B row is **60% S5** — the post-SEBI-caution partner set is wallets and neobanks, and the largest of those are Indian. **If `INDIA_ENABLED` is OFF, S44 falls to roughly 40% of Base and S42 falls to the Conservative path. Wire the dependency.**
- 🔴 **Build consequence with a hard date.** Stream 6 is a Year 2–3 revenue line with a **Week 1 build requirement**: the September build must be **multi-tenant capable at the register and the mint**. If it is not, **this stream is lost for the rebuild cycle.** It shares this requirement with composability Stage 1 — **one build, two dependencies, do not double-count the cost** (D15).
- **The rate is a placeholder.** 0.5–0.75%/yr is our range, not a quoted term.

---

### Stream 0: Redemption (a mandatory cost, and there can be no offsetting revenue)

**Quick Facts**

| Field | Value |
|---|---|
| Type | **Cost.** Scales with AUM |
| Activation | **M1** |
| Rate | **Zero. VARA Annex 2 III.E.4 forbids charging any fee on redemption** |
| Sheet location | Model, rows 460–474 |

**What It Is**

Burn-and-pay-cash. **A mandatory, uncapped, zero-revenue cost line that scales with AUM.** v1.0 lists six revenue streams and no negative one; this is the seventh line and it points down.

**How It Materialises** (`_draft_purchase-structure.md` §5.3, eight stages)

1. **Request submitted.** ⚠ A **48-hour hold applies to any redemption request from an account with an active card facility** (§5.2) — an operational constraint on timing, not a cost.
2. **Price struck at the next fix after the request.** *"Same convention as entry. Neither side can select the fix."*
3. **Grams burned.** Burn-on-redemption is **not optional** — it is the specific operational failure that stranded 96% of Cache Gold's supply.
4. **Payout T+1, target**, with the §5.5 settlement window tiers by size.
5. **Grams return to the float. The next buyer consumes them.** *"An exit does not sell gold… The treasury only touches the physical market when the float breaches a band."*
6. **Physical sale only on net outflow**, and only when the float band breaches.

**Drivers**

| Driver | Value | Source | Unit |
|---|---|---|---|
| Redemption rate | **8** Base / 4 Agg / 16 Cons | S32. Set **below** the self-custody rate because the on-chain route is frictionless (decision 50), so the marginal exiter transfers rather than redeems | % of AUM/yr |
| Lapsed-holder multiplier | **2.2×** Base / 1.6 Agg / 3.5 Cons | S33. Applied to S32 **and** to S31 | × |
| Cost per redemption event | **4.20** Base / 2.50 Agg / 9.00 Cons | F20: outbound AED payment 1.00–2.50 + Sumsub sanctions re-screen 1.85 (F16) + operational handling 1.00–4.50 | USD/event |
| Dealer two-way spread | On net outflow only | `_draft_purchase-structure.md` §5.4 | % |
| Settlement windows | Small → next business day; Medium → up to 3; Large → up to 5 | §5.5. **Thresholds deliberately unset — they depend on float size, which depends on the dealer** | days |
| PAXG turnover comparator | 5.9% | `_draft_allocation-and-float.md`. **A token-turnover figure, not a redemption figure.** The only comparator in the corpus | %/yr |

**Formula — Monthly (M1–M24)**

```
  redemption_grams(t) = [ contributing_AUM_grams(t) × S32
                        + lapsed_holding_grams(t)   × S32 × S33 ] ÷ 12
  redemption_events(t)= redemption_grams(t) ÷ avg_redemption_size

  net_flow_grams(t)   = sip_grams(t) + spot_grams(t)
                      − self_custody_out(t) − redemption_grams(t)

  STREAM0(t) = redemption_events(t) × F20
             + MAX(0, −net_flow_grams(t)) × gold_price × dealer_two_way_spread
             [the second term is ZERO in every month the book grows]
```

**Formula — Annual (Y3–Y7)** — identical, on annual grams, without the ÷ 12.

**Growth Logic**

| Aspect | Value |
|---|---|
| Pattern | Linear on AUM, **but accelerating** as the lapsed-holding share of AUM rises |
| What drives growth | AUM × rate, with the lapsed share carrying a 2.2× multiplier |
| Ceiling | None. **It is uncapped by construction** |
| Lag | None |
| Counter-force | **The float absorbs it entirely while the book grows.** The spread term switches on only when net flow turns negative |

**Key Uncertainties**

- **At Base rates this is immaterial against terminal revenue — and that is the reassuring finding.** **USD 158 against USD 8,150,081 of Y10 gross revenue — 0.002%.** **It becomes material only in a stress scenario where the redemption rate spikes, and that is exactly when cash is scarcest. Worth a stress row, not a headline.**
- ⚠ **The §5.4 affordability argument assumes Aurumix owns the float.** Under the recommended dealer-carried launch (S51) it requires **a second dealer commitment to take grams back on demand.** *"Flag as a Year-1 assumption, not a finding."*
- 🔴 **The "equal value" counsel question decides who absorbs the spread on every exit.** *"III.E.1 says 'equal value.' The safe reading is the full prevailing value of the underlying grams with no haircut. An arguable reading is realisable value, that is, the dealer's bid. **The difference is the entire two-way spread and it decides who absorbs it on every exit.**"* Model the safe reading (Aurumix absorbs); expose the switch.
- **Settlement-window thresholds are unset** pending float size pending the dealer. **Carry the tiers as structure with the thresholds as inputs.**

---

## 7. Cost architecture

### 7.1 Cost of goods sold

🆕 **Inside stream 1, and there are now TWO, not four: fabrication premium and price-gap risk.** See §6.1. **Not an opex line.**

🆕 **The float cost of capital left this list at D32.** It is an **opportunity cost on equity, not a cash expense**, and an imputed equity charge does not belong in COGS — §7.6 already applies exactly that rule to locked regulatory capital, and F5 was the one place the brief broke it. It is now `floatcoc_memo`, reported on Summary. 🔴 **The float PRINCIPAL is untouched: USD 29k at Y1 rising to USD 3.6M at Y10, on the balance sheet and inside the USD 15.1m peak-funding figure. The carry stopped being a P&L line; the float did not stop being money.** ⚠ **And it is NOT the customer's gold held anyway — the trust holdings are the customer's and cost Aurumix no capital. The float is Aurumix's own inventory, bought with Aurumix's own money, held BEFORE any customer owns it.**

🆕 **The payment rail left this list at D31.** It is a third-party PSP charge, not something Aurumix charges, so it is grossed up onto the collection request and remitted — **a pass-through with zero P&L effect, carried as `rail_memo` only.** ⚠ **It must not reappear in COGS, in opex, or in any margin denominator.** The Checks sheet asserts this.

⚠ **One asymmetry to hold in view, because it is a regulatory constraint and not a choice.** Aurumix may pass through the cost of collecting money but **may not pass through the cost of returning it: VARA Annex 2 III.E.4 forbids charging any fee on redemption.** So `F20` (USD 4.20/event) stays absorbed in Stream 0 while the equivalent inbound cost does not. **The cost architecture is deliberately lopsided and the client should know it is lopsided by rule, not by design.**

⚠ **Two of the four are conditional on the float carry mode (S51) and v1.0 charges them unconditionally.** Under dealer-carried, price-gap risk and float cost of capital are **zero** and the fabrication premium is **wider**. Under own float, all four bite but the premium narrows. **Charging both the float cost of capital and the full dealer premium double-counts under either regime** — correction 12.

### 7.2 Benefit costs (contra-revenue)

| Benefit | Cost type | Funded by | Model treatment |
|---|---|---|---|
| Entry-fee discount (0 / 0.4 / 0.8 / 1.2 / 1.5 pp) | **Real, reduces stream 1** | Stream 1 base-rate uplift | Reduce `f` by the tier-weighted discount. **Pre-gate and never-gated carry zero** |
| Credit LTV ladder (— / — / 50 / 65 / 80%) | **Zero cash cost. Revenue-positive** | Stream 5 | Higher LTV raises drawn balances |
| Card tier (FX 2.0 / 1.5 / 1.0%, ATM allowance) | **Waived stream 4 revenue** | Stream 2 interchange | Net against stream 4, **do not double count** |
| Gold Rewards (— / — / 0.15 / 0.45 / 0.75%) | **Real unit cost per event** | Stream 2 + stream 5, net of custody | Haircut on stream 2, capped at customer-generated revenue |
| Will and family discount (0 / 10 / 20 / 35 / 50%) | **Real, reduces stream 3** | Stream 3 price headroom | Reduce the stream 3 price by tier |
| Per-beneficiary discount (0 / 0 / 0 / 10 / 20%) | **Real, reduces stream 3** | Stream 3 price headroom | Starts only at Platinum |

**Gold Rewards is capped at the interchange and credit revenue that customer generated, net of their custody cost.** So if `PM_SHARE ≥ 36%` it can never exceed its funding line by construction (`_draft_credit-and-card-infrastructure.md` §8.2; 0.75 ÷ 2.10 = 35.7%, arithmetic verified). Model it as a **haircut on stream 2**, never as an independent cost. The Checks sheet must verify the cap never goes negative.

**The launch-year cost of the entire ladder is one 0.4pp Silver discount, on the share of the founding cohort that actually gates.** Time-phasing is doing enormous work and should be shown to the client explicitly, because it is the reason a generous-looking benefit set is affordable. `_draft_ics-scoring.md` §6.1: *"the ladder's cost curve and the business's cost curve are the same curve, offset the right way — so holding the headline at 5% may fund the entire ladder with no uplift at all."*

**Two benefits are nearly costless and both should be in the client-facing story.** The ATM allowance ladder waives revenue from only the top ~3% of cardholders under the S35 distribution. And the **never-gated population consumes zero benefits forever while paying the full undiscounted fee** — v1.0 has no cell for them and therefore **overstates benefit cost.**

⚠ **The one arithmetic conflict Phase 2 left unresolved, and v2.0 changes its answer.** The discount ceiling is 1.5pp at Sovereign against a Year 1 gross margin of 0.72% before rail: **the ceiling exceeds the available margin.** v1.0 framed this as its single unresolved conflict. **Decision 44 halves the funding question** — retiring the tenure rebate means *"the entry-fee uplift now funds only the discount ladder"* — and §6.1 of the scoring draft says holding the headline at 5% **may fund the entire ladder with no uplift at all. Solver item 1's answer may be zero.** See §9.

### 7.3 Acquisition cost

**Member referral.** 30% of the entry fee the referee paid over their six qualifying contributions, split equally, credited in grams. At a 5% fee that is **1.50% of the referee's six-month contributions**, or USD 6.75 at the target ticket. Paid at the referee's gate, so **no earlier than month 13 from launch in any version** — and under D4, **later than that for any referee who is not a perfect payer**, because the gate is a distribution.

The self-funding claim was **withdrawn, not repaired** (`_draft_referral-system.md` §5.0): the reward was tested against a 2.15% gross margin that had not yet paid for price-gap, float or rail. Against the real Year 1 net margin the reward is roughly **double** the margin on the run that generated it. The honest frame is CAC vs LTV.

⚠ **v1.0's own LTV figure is stale and it says so.** That calculation used ~40 paying months from the 79%/38% persistency curve. **At the corrected curve (55% M13, 19% M61) expected paying months are 31.2** — lower than v1.0's ~40, but not the "roughly 22" an earlier draft of this section assumed. Recomputed LTV, payback and reward-as-%-of-LTV are at §7.8 — **do not reuse v1.0's 19.4% or its month 9-to-11 payback.**

🔴 **And the conclusion this paragraph used to draw is now the wrong way round.** At 31.2 paying months and an all-streams LTV of USD 552–949, the solver finds the referral reward affordable at up to **399% of the referee's entry fee** — F17's 30% placeholder is not merely payable, **LTV does not bind on it at all.** The binding constraint is the acquisition budget (§9.1 item 2), not lifetime value. **The argument for the small-thank-you option has to be made on cash timing and on the entry-fee lane — where a 30% reward is roughly USD 14 against an S3 contribution-margin LTV of USD 5.62 — not on all-streams LTV, which comfortably covers it.**

**Agent commission.** The client's only ever written number is **15% of the fee**, whose base (the Algorithmic Growth Fee) no longer exists. Transplanted to the entry fee, 15% consumes **0.75pp of 0.85pp — 88% of Year 1 gross margin. The client has not seen this arithmetic**, and it is one of the promoted outputs at §14.

**Agent recruitment, which v1.0 omits entirely.** At S18 = 45% annual attrition, holding 200 active agents requires roughly **90 recruits a year**, each re-entering the S17 ramp at 0.20. Model recruits as an explicit cost line and an explicit productivity drag. **Without it the model overstates agent output by 15–20% at steady state.**

**The acquisition budget ceiling** is one board-approved cap covering member rewards plus all agent commission at every level, expressed as a percentage of entry-fee revenue, modelled on IRDAI's Expenses of Management regime — overall ceiling, front-loading braked, excess borne by shareholders. **The number is a Phase 4 output.** See §9 item 2. **Apply it with a one-period lag** (§3.x.3).

### 7.4 Operating expenses

Constructed from benchmarks. The client supplied one figure. **Salary lines are Low-Medium confidence** and should be replaced with a purchased UAE salary guide before the model is presented as final. Loading is **1.10× on quoted total cash**, not 2.0×, because UAE salary guides already quote base plus allowances; applying the base-salary multiplier to a total-cash figure double counts.

| Block | Y1 (500) | Y3 (12,000) | Y10 (80,000) | **Step or scale** | Interpolation | Confidence |
|---|---|---|---|---|---|---|
| Headcount | 588,000 | 1,340,000 | 4,600,000 | **Step** | Hire plan, quarterly steps; log-linear between anchors then round to whole FTE | Low-Med |
| MLRO (outsourced Y1–Y2, in-house Y3+) | 49,000 | 163,000 | incl. above | **Step, then folds in** | Flat Y1–Y2; **decay the standalone line to zero linearly Y3→Y10** as it merges into Headcount | Medium |
| VARA supervision | 54,500 | 94,500 | 110,000 | **Step** | Flat AED 200,000 (F14) until an activity is added. **Booked in full in the licence anniversary month** — it is an annual invoice | **High, VARA's own rulebook** |
| Audit + reserve attestation | 35,000 | 60,000 | 180,000 | **Step** | Tech audit in the anniversary month; **attestation in months 6 and 12 of each year** | Med / Judgement |
| Compliance tooling + KYC | 31,600 | 97,200 | 255,500 | **Scale, with a floor** | `MAX(299, 1.85 × checks)` — **the minimum binds below 162 checks/month** (F16) | **High** on Sumsub |
| Vault and metal | 12,000 | 150,000 | 800,000 | **Scale, with a floor** | `MAX(USD 25/day, 0.10/kg/day × kg)` — **the minimum binds below ~250 kg** | Medium |
| Technology | 34,000 | 115,000 | 600,000 | **Scale** | Log-linear on account count | Low |
| Corporate (licence, office, visas) | 20,700 | 60,000 | 350,000 | **Step** | **DMCC licence in the incorporation anniversary month**; office steps at headcount thresholds | **High, DMCC's own schedule** |
| Security | 10,000 | 35,000 | 200,000 | **Step** | Log-linear, rounded to annual steps | Med |
| Marketing | incl. below | 250,000 | 1,200,000 | **Scale — a decision variable, not a cost** | **Set by the acquisition plan and the S25 CAC curve.** Straight-line from a zero Y1 base | Judgement |
| **Legal and trust** *(new at v2.0)* | see §7.7 | see §7.7 | see §7.7 | **Step** | Log-linear, rounded to annual steps | **Unpriced in the corpus** |
| Insurance and contingency *(residual of the old lump)* | see §7.7 | see §7.7 | see §7.7 | **Step** | Insurance in the policy anniversary month | Judgement |
| **Total annual opex** | **894,800** | **2,484,700** | **8,695,500** | | | |

**Interpolated years, block-level log-linear, Base** (F32). Reconcile Y3 and Y10 to the published anchors by a **proportional plug on the Marketing block only** — Marketing is the one block that is a decision variable, so it is the correct place to absorb the 0.9% and 2.4% residuals. Do not adjust the others.

| Year | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **A. Anchor schedule, at v1.0's assumed counts** | 894,800 | 1,478,420 | 2,484,700 | 2,929,793 | 3,475,359 | 4,143,676 | 4,962,115 | 5,964,336 | 7,191,778 | 8,695,500 |
| *contributing accounts assumed* | *500* | — | *12,000* | — | — | — | — | — | — | *80,000* |
| **B. Opex the model actually charges** | **1,031,907** | **1,192,011** | **1,475,189** | **1,671,282** | **1,911,078** | **2,178,469** | **2,455,768** | **2,728,412** | **2,984,591** | **3,219,856** |
| *contributing accounts modelled* | *508* | *1,805* | *4,146* | *7,035* | *10,238* | *13,421* | *16,285* | *18,607* | *20,186* | *20,990* |

🔴 **Read row B, not row A, as this model's operating cost.** Row A is the *benchmark schedule* — the block build above, evaluated at the investor counts v1.0 assumed (500 / 12,000 / 80,000). Row B is `Opex(N)` evaluated at the counts the acquisition engine actually produces. **They diverge by 2.7× at Year 10**, because the model reaches 20,990 contributing accounts and not 80,000.

**This divergence is the single largest correction v2.0 makes to v1.0's P&L, and it cuts in the client's favour.** v1.0 charged row A against a revenue line built on its own much smaller book — revenue on one trajectory, cost on another. Correcting it removes roughly USD 5.5m of Year 10 cost. It is also why v1.0's break-even arithmetic was incoherent rather than merely wrong: dividing an opex sized for 500 investors by margin per investor to solve for 171,911 investors (§14.1).

**Marketing must not appear twice.** v1.0 has it in the opex table *and* as an acquisition driver. **It is an input to acquisition, not an output of an opex table.** Set it on the Scenario sheet, feed it to Layer 1, and let the opex block reference it — one source, two consumers.

**One-off Year 1, additional:** VARA application AED 100,000 (USD 27,200), tier-1 smart contract audit USD 75,000, DMCC incorporation USD 3,280, **DIFC SPV USD 1,900 — not ADGM** (correction 17), licensing support USD 20,000, **plus the legal and trust one-offs at §7.7 which are unpriced.**

**Four corrections to how the corpus treats costs, carried forward from v1.0 and still live:**

1. **The USD 75,000 audit is not a one-off.** VARA mandates an annual tech audit and penetration test by a qualified independent third party, **plus one before every new system or product launch** (Technology Rulebook). Budget tier-1 for the launch audit and mid-tier (USD 15,000–25,000) for annual re-audits.
2. **ARVA reserve audit is required every six months.** Kinesis uses Bureau Veritas biannually and Paxos uses KPMG monthly, which confirms the cadence is market-normal. **No issuer discloses what it costs. Get a Bureau Veritas quote; it is the single biggest unpriced line.**
3. **The vault minimum binds at launch.** DGCX publishes USD 0.10/kg/day with a **USD 25/day minimum**, i.e. USD 9,125/year regardless of volume. At Year 1 AUM the per-kg charge would be USD 646, so the minimum applies and the **effective rate is 0.37%, not 0.026%.** It decays to immateriality around 250 kg.
4. **The model may be under-scoped on VARA activities.** Category 1 Issuance alone may not cover distributing or redeeming the token. Broker-Dealer and VA Transfer & Settlement each add AED 80,000–200,000/year plus extension fees. **Confirm with VARA before the cost base locks.**

**The minimum-commitment pattern, named because this is now the third instance.** The DGCX vault minimum (USD 25/day), the Sumsub platform minimum (USD 299/month) and the **F27 card programme minimums** (BIN sponsorship, processor platform, Visa scheme assessments) are all **minimum-commitment structures that bind at low volume and decay to immateriality at scale.** They are the reason early-year unit economics look worse than the steady state, and **the model must show all three as a class rather than as three unrelated lines.**

**The competitive fact that governs custody pricing.** Every major comparator charges holders **zero** storage: PAXG 0%, XAUT 0%, Kinesis 0%, Comtech 0% for 24 months. **The client's 0.8–1.0% custody fee is not viable against this field, and it is also roughly 3 to 6 times the real cost.** Verified allocated storage clusters at **0.12–0.40%** (BullionVault 0.12% with a USD 4/month minimum; GoldMoney 0.25%; SGPMX 0.40–0.50%). Our internal 0.15–0.40% estimate is **vindicated**; the client's assumption is not. Decision 42 — retail storage free forever, recovered via Gold Rewards netting and the B2B platform fee — is confirmed correct.

⚠ Worth copying: **PAXG's terms reserve the right to introduce a storage fee via dilutive token issuance on 30 days' notice.** That accrues a charge without an invoice and is already market-accepted.

### 7.5 Working capital and the float

**New at v2.0.** v1.0 charges a float cost of capital as a P&L line and never sizes the principal it is a cost of (D7). This subsection sizes it.

> 🆕 🔴 **D32 finishes what D7 started, and inverts its remedy.** D7's fix was *size the principal so the charge is defensible.* **D32's fix is: size the principal and then stop charging it at all.** The float carry is an **opportunity cost on equity, not a cash expense** — no counterparty invoices Aurumix for it — so it is reported as `floatcoc_memo` on Summary and appears in no margin, no COGS line and no P&L total.
>
> **This subsection is now MORE load-bearing, not less.** With the carry out of the P&L, the float's entire financial expression is the **principal** sized here: **USD 29k at Y1, USD 437k at Y3, USD 3.6M at Y10**, sitting on the balance sheet and inside the USD 15.1m peak-funding requirement. ⚠ **If a reader concludes from D32 that the float is free, they have misread it — the cost moved from the P&L to the cap table.**
>
> 🔴 **One case where the carry becomes a REAL expense and must be restored:** if the float is ever **debt-funded** — a gold-backed working-capital facility, or dealer credit — the interest is cash, not opportunity, and it belongs in the P&L as a financing line. **D32 assumes equity funding. Make that assumption explicit on the Assumptions sheet, and put a `FLOAT_DEBT_FUNDED` switch behind it.**

**The corpus sizing rule, verbatim from `_draft_allocation-and-float.md`:**

> **`float ≥ one bar denomination + a buffer of N days' trailing inflow.` Two bars is the launch setting.**

```
float_grams(t)    = MAX( 2 × bar_grams(t),
                         bar_grams(t) + S50 × daily_inflow_grams(t) )
float_capital(t)  = float_grams(t) × gold_price × (1 + fabrication_premium(t))
float_coc_cost(t) = float_capital(t) × cost_of_capital ÷ 12
```

| Parameter | Value | Source | Confidence |
|---|---|---|---|
| Float sizing rule (F38) | `MAX(2 bars, 1 bar + N days trailing inflow)` | **`_draft_allocation-and-float.md`, "Sizing", verbatim. A corpus-settled rule, not an assumption** | **High** |
| Buffer days N (S50) | **10** Base / 6 Agg / 20 Cons | The rule states N without setting it. 10 days ≈ the Y1 fill window (12.1 days at F1) | Low-Med |
| Float carry mode (S51) | **Dealer-carried at launch; own float from the Y3 denomination upgrade** | Corpus working recommendation: *"launch dealer-carried, migrate to an own float once volume makes internalising the spread worth the capital"* | **High** on the fork existing, **Low** on which side is taken |

**Float capital by year, at the corrected gold price.** ⚠ **Every float dollar figure in the corpus is stale — all of them are computed at USD 109.31/g.** At F1 = 141.46 they rise by **29.4%**:

| | Grams | **Corpus figure (at 109.31/g)** | **Corrected (at F1 = 141.46)** |
|---|---|---|---|
| Y1 | 200 g (2 × 100 g) | ~USD 22k | **~USD 29k** |
| Y3 | 3 kg | ~USD 330k | **~USD 437k** |
| Y10 | 24.8 kg | ~USD 2.7M | **~USD 3.6M** |
| Tradeflow 1 kg launch | 2 kg | ~USD 220k | **~USD 285k** |

This is correction 1 propagating into a table §13 of v1.0 does not currently list — correction 13 at §15.

**Three things the model must not do with the float — two corpus rules and one from D32:**

- 🆕 **Do not charge the float carry to any margin, unit-economics or COGS line.** Memo only (D32). **The Checks sheet asserts `floatcoc_memo` appears in no total.**

- **Do not run float capital through the P&L.** It is a balance-sheet item. Only the *cost of carrying* it hits the P&L. This mirrors F15's treatment of the AED 1.5m minimum: *"Locked, not expensed. Do not run through P&L."*
- **Do not net the float against the VARA minimum capital without counsel.** *"[COUNSEL] whether allocated gold inventory can sit inside that requirement."* If it can, the true incremental capital need at Y1 is roughly zero, because AED 1.5m (~USD 408k) is posted anyway and dwarfs a USD 29k float. **If it cannot, the two stack.** At Y1 immaterial; **at Y10 the float is USD 3.6m against an AED 1.5m minimum and the question is worth a real answer.**

**The dealer-carried / own-float fork, which v1.0 omits entirely:**

| | Dealer-carried | Own float |
|---|---|---|
| Working capital | **Zero** | ~USD 29k Y1, ~USD 437k Y3, ~USD 3.6M Y10 |
| Price-gap risk | Dealer's | Aurumix's, under 0.4% |
| Float cost of capital (F5) | **Zero** | 0.49 / 0.31 / 0.38% |
| Fabrication premium | **Wider** | Narrower once at scale |
| Risk | **Single-counterparty dependency; the dealer can withdraw** | Operational and capital |
| Zero-fee redemption argument | **Requires a second dealer commitment to take grams back on demand** | Holds as written |

🔴 **Charging both the float cost of capital and the full dealer premium double-counts under either regime. This is an error, not a sensitivity** (correction 12).

**The Tradeflow binary, as a scenario.** DMCC Tradeflow specifies eligible collateral as **1 kg 999.9 bars**. If warrants are wanted from launch, 1 kg becomes the effective floor and the launch float rises from ~USD 29k to **~USD 285k — a 10× launch capital step.** *"Real trade-off, and a client decision."*

**The float has five jobs, and stream 5 supplies the fifth.** It buys the wholesale price (bar size is the margin dial and float size unlocks bar size); it absorbs lumpiness in inflow; it warehouses net redemption outflow; it absorbs large spot orders up to one bar denomination; and per `_draft_credit-and-card-infrastructure.md` §6.6 it **absorbs margin-call liquidations** — *"Recommended. Fastest, best price, no dealer call on a bad day. This is the float's fifth job, and the same argument that made zero-fee redemption survivable."*

**Float as a share of AUM falls as the business scales. It is a fixed operational requirement, not a proportional drag.**

### 7.6 Regulatory capital and the funding view

**New at v2.0.** The AED 1.5m minimum is correctly excluded from the P&L (F15) and appears nowhere else in v1.0 — including in a funding view, because v1.0 has none.

```
required_capital(t) = MAX( AED 1,500,000,
                           0.02 × trailing_24m_avg_reserve_assets(t) × OPTION_B )
```

**`OPTION_B` defaults OFF, and that is the point.** The 2%-of-Reserve-Assets escalator attaches to **Option B only** — the stable-value ARVA with Reserve Assets. Under the chosen Option A (direct ownership) *"there are arguably no Reserve Assets to take 2% of, so the floor stays at AED 1.5M."* With the switch OFF the row is **flat at every period, which is precisely what the client should see.**

Turning it ON shows the counterfactual: *"At the Year 10 target of 60,000 to 100,000 investors, reserves could plausibly reach USD 200M. Two percent of that is USD 4M of permanently locked capital… **This is a multi-million dollar difference and it is a second, financial reason to choose direct ownership.**"*

⚠ **Cross-check the USD 200M against the model's own computed Y10 AUM rather than quoting it as a constant.** **The model reaches USD 39,790,584 of Y10 AUM against the corpus's USD 200M assumption — roughly 5× lower.** At that AUM, 2% of reserves is **USD 795,812** against the AED 1.5m floor of USD 408,441 — i.e. **1.95× the floor. The escalator BITES**, and it is the binding constraint from the year reserves pass **USD 20,422,056**. The corpus's USD 4M figure does not arise at this scale, but **the direction of its finding is confirmed, not overturned**: Option B roughly doubles locked capital.

| Basis | Locked capital | Note |
|---|---|---|
| Option A floor (AED 1.5m) | **USD 408,441** | Flat at every period — the point of choosing Option A |
| Option B at Y10 reserves | **USD 795,812** | **1.95× the floor** |
| **Incremental capital under Option B** | **USD 387,371** | Additional permanently locked capital, earning nothing |

**Report the escalator as an opportunity cost, not a P&L line.** Locked capital does not hit the P&L, but it earns nothing: `(required_capital − AED 1.5m) × cost_of_capital` as a **memo line** — **about USD 30,990/yr** on the USD 387,371 increment. The scenario run confirms the shape: `option_b_capital` leaves Y10 revenue and cumulative net profit identical to Base and moves only peak funding, from USD 15,076,460 to **USD 15,321,068.**

**The funding view, distinct from the P&L:**

| Component | Treatment |
|---|---|
| AED 1.5m VARA minimum paid-up capital | **Locked, not expensed.** Posted at launch |
| Float principal | **Balance sheet.** Zero under dealer-carried; §7.5 table under own float |
| One-off launch spend | Cash, Year 1: application, audit, incorporation, DIFC SPV, licensing support, **plus unpriced legal** |
| Cumulative operating losses | The dominant term. **On the ten-year run, USD 14,110,495 of cumulative net loss with cumulative cash reaching USD −14,541,529 at Y10.** ⚠ **Ten-year figures, superseded by the rebuild.** The structural point holds on either horizon: **break-even is never reached inside the modelled period, so this is the loss to the end of the horizon rather than the loss to break-even, and it must not be presented as a total funding need** (§14) |
| **Total funding requirement** | **USD 15,076,460** under Option A · **USD 15,321,068** under Option B |

**Reconciliation against the corpus's own launch estimate, because the two figures look contradictory and are not.** The corpus §3.5 says *"approximately **USD 550,000 to 750,000 of capital and fees before any build cost**, and six to nine months minimum"* — that is **USD 408k locked capital + USD 27k application + USD 75k audit + USD 200k/yr supervision + the vehicle and unpriced legal opinions.** v1.0's USD 127,380 is **cash spent, one-off, excluding locked capital and excluding annual fees** — a different and correct measure for a P&L. **Both are right; they measure different things, and the funding view is where they meet.** ⚠ **VARA publishes no approval timeline.**

**VAT sits here too, because it is a margin question not a cost question on this base.** See Layer 11 and S49. `{{UNFILLED: Y10 VAT advantage from the non-resident share, USD — not in spine; the model books a Y10 cost_vat of USD 7,421 but does not split the resident/non-resident saving}}`, haircut 20% for input-VAT drag.

### 7.7 Legal and trust

**New at v2.0. v1.0 has no legal or counsel line in one-off cost and none in opex** — the "Legal, insurance, contingency" lump absorbs it invisibly, which reads as if legal cost were zero (D15).

The corpus is unusually direct: *"Legal opinions: title transfer, token classification, India perimeter — **NOT ESTABLISHED. Budget generously.**"*

| Line | Type | Priced? | Note |
|---|---|---|---|
| DIFC trustee company setup | One-off | **No** | Route 2 settled as **DIFC**, not ADGM (decision 50; `_draft_credit-and-card-infrastructure.md` §7.1: taking security *"breaks the tie decisively toward DIFC"*) |
| **DIFC trustee company annual maintenance** | **Recurring** | **No** | **The line the brief is most clearly missing.** A recurring cost with no home in v1.0 at all |
| Trust deed drafting | One-off | **No** | *"a drafting exercise, not a structuring one, and it is **the only genuinely new legal work this creates**"* |
| Counsel batches | One-off, staged | **No** | Six re-cut questions in the composability draft, three in the purchase-structure draft, two in the credit draft, three named in the licensing draft |
| **DFSA trust licence** | **Contingent** | **🔴 Explicitly unquotable** | See below |
| Wind-down provision (VARA Company Rulebook Part VII.A) | Recurring, mandatory | **No** | The corpus gives the shape — claim window, burn-on-redemption, freeze role — but no cost |
| Insurance | Recurring | Judgement | Booked in the policy anniversary month |
| Contingency | Recurring | Judgement | The residual of v1.0's lump after the above are split out |

🔴 **The DFSA trust licence question must carry a visible placeholder, not an implied zero.** The DFSA Rulebook *appears* to exempt from the Licensing Rules a person who is *"a Trustee of a single trust"* or *"a non-commercial Trustee"*. If that holds, a single-purpose DIFC trustee company holding one trust needs no DFSA trust licence. **Confidence: Medium — retrieved from a rulebook mirror, not DFSA primary text, and the primary page could not be fetched. Verify before it reaches the client, because it materially changes the cost of route 2.** Counsel question 5 states the modelling consequence outright: *"**This is a cost question and we cannot quote the client a number without it.**"*

**Model as:** `legal_trust(t) = base_recurring(t) + IF(DFSA_LICENCE_REQUIRED, licence_cost, 0)`, with `licence_cost` = `{{UNFILLED: DFSA trust licence annual cost — UNPRICED, client/counsel input — not in spine, and unpriceable by the model by construction}}` and the switch defaulting to the exempt reading.

**Composability must not appear as a new expense line, and this is a cost reduction the model should show.** The Stage 1 September build is *"no added cost, and it removes cost"* — the transfer hook ships as a **blocklist**, which is *"less code than the allowlist currently planned."* **Net technology cost at the September build should be flat or slightly down, not up.** And Stage 1 requires **multi-tenant capability at register and mint**, which is the same Week-1 requirement stream 6 already carries: **one build, two dependencies. Do not double-count.**

**Two build constraints from this block that carry no cost but must be recorded.** **Burn-on-redemption is not optional** — it is the specific operational failure that stranded 96% of Cache Gold's supply, and *"the failure was operational, not architectural."* And the **monthly cash touchpoint with the direct-channel book means the majority of holders are contactable by construction** — a wind-down cost mitigant and a genuine differentiator, worth a line in the client narrative rather than a line in the model.

**A cost that was expected and may not have to be paid, worth stating because the corpus flags it retrospectively.** *"Note what this retrospectively justifies: decision 6 killed the profit-share dividend on securities grounds, and it turns out to have also protected the vehicle from fund classification. Keep it dead."* Allocated gold that produces no income, is not managed, and where each customer's grams are fixed, does not meet DIFC Law No. 2 of 2010 Art 11. **No fund-classification cost, on the current design only.**

### 7.8 Unit economics

**New at v2.0.** v1.0 flags its own LTV as stale and never replaces it, and buries the fact that agent commission consumes 88% of Year 1 gross margin in §7.3 prose. **This is the section that promotes both to first-class outputs** (D16).

**Every cell here is a model output. None of v1.0's figures may be reused** — its LTV was computed off a persistency curve its own §0.5 withdraws.

**By segment (all streams, at the Base scenario):**

| Segment | Ticket | Paying months (expected) | Contribution-margin LTV | Blended CAC | **LTV:CAC** | Payback (months) |
|---|---|---|---|---|---|---|
| S1 UAE professional | USD 75 | 31.2 | **USD 949.04** all streams · USD 42.55 entry fee only | `{{UNFILLED: S1 blended CAC, USD — spine gives CAC by channel only (Agent 72.00, Referral 42.00, Direct 120.00, B2B 0) and no channel-mix weights to blend them}}` | **13.18** Agent · 22.60 Referral · 7.91 Direct (all streams) — **0.59 / 1.01 / 0.35** entry fee only | 52.8 / 30.8 / 88.1 (entry fee only) |
| S2 UAE white-collar | USD 40 | 31.2 | **USD 734.03** all streams · USD 19.05 entry fee only | `{{UNFILLED: S2 blended CAC, USD — spine gives CAC by channel only, no mix weights}}` | **10.20** Agent · 17.48 Referral · 6.12 Direct (all streams) — **0.27 / 0.45 / 0.16** entry fee only | 118.0 / 68.9 / 196.7 (entry fee only) |
| S3 UAE blue-collar | USD 20 | 31.2 | **USD 551.72** all streams · USD 5.62 entry fee only | `{{UNFILLED: S3 blended CAC, USD — spine gives CAC by channel only, no mix weights}}` | **7.66** Agent · 13.14 Referral · 4.60 Direct (all streams) — **0.08 / 0.13 / 0.05** entry fee only | 400.0 / 233.3 / 666.7 (entry fee only) |
| S4 Oman + Bahrain | USD 40 | 31.2 | **USD 691.40** all streams · USD 19.05 entry fee only | `{{UNFILLED: S4 blended CAC, USD — spine gives CAC by channel only, no mix weights}}` | **9.60** Agent · 16.46 Referral · 5.76 Direct (all streams) — **0.27 / 0.45 / 0.16** entry fee only | 118.0 / 68.9 / 196.7 (entry fee only) |
| S5 India resident | USD 30 | 31.2 | **USD 625.72** all streams · USD 12.34 entry fee only | `{{UNFILLED: S5 blended CAC, USD — spine gives CAC by channel only, no mix weights}}` | **8.69** Agent · 14.90 Referral · 5.21 Direct (all streams) — **0.17 / 0.29 / 0.10** entry fee only | 182.3 / 106.3 / 303.8 (entry fee only) |
| S6 Other international | USD 75 | 31.2 | **USD 939.34** all streams · USD 42.55 entry fee only | `{{UNFILLED: S6 blended CAC, USD — spine gives CAC by channel only, no mix weights}}` | **13.05** Agent · 22.36 Referral · 7.83 Direct (all streams) — **0.59 / 1.01 / 0.35** entry fee only | 52.8 / 30.8 / 88.1 (entry fee only) |

**All-streams LTV now varies by segment, and the spread is the argument.** USD 949 at S1 down to **USD 552 at S3 — a 1.72× spread**, driven by card spend scaling sub-proportionally with ticket (the `card_spend_segment_exponent` of 0.55 compresses a 3.75× ticket spread into roughly 2.1× of card spend). **The blue-collar segment is not a bad customer on the card; it is a smaller one.** Contrast the entry-fee-only LTV, where the same segments differ by **7.6×** — the inflow lane is where the segment mix really bites.

**By channel (blended across segments at that channel's own S16 mix):**

| Channel | CAC | LTV at that channel's mix | **LTV:CAC** | Payback | Note |
|---|---|---|---|---|---|
| Agent | USD 72.00 | **USD 552–949** all streams by segment · USD 5.62–42.55 entry fee only | **7.66 (S3) to 13.18 (S1)** all streams · **0.08–0.59** entry fee only | 52.8 (S1/S6) to 400.0 (S3), entry fee only | 🔴 **The channel most exposed to the rail.** Its S16 mix is the most blue-collar-weighted, so its tickets are the smallest and the fixed rail is spread over the smallest base |
| Referral | USD 42.00 | **USD 552–949** all streams by segment · USD 5.62–42.55 entry fee only | **13.14 (S3) to 22.60 (S1)** all streams · **0.13–1.01** entry fee only | 30.8 (S1/S6) to 233.3 (S3), entry fee only | Payback is **structurally ≥13 months** — the reward is not paid until the referee gates. **The best ratio of any paid channel at every segment** |
| Direct (paid) | USD 120.00 (the spine's modelled direct CAC; it does not publish a separate Y10-spend effective CAC) | **USD 552–949** all streams by segment · USD 5.62–42.55 entry fee only | **4.60 (S3) to 7.91 (S1)** all streams · **0.05–0.35** entry fee only | 88.1 (S1/S6) to 666.7 (S3), entry fee only | **CAC rises with spend** under the S25 curve — the ratio degrades as the channel scales |
| Direct (organic) | ~0 | **USD 552–949** all streams — the spine does not model organic separately from paid direct | n/a | immediate | S26. The only channel with no acquisition cost |
| B2B partner | 0 | **USD 552–949** all streams, at CAC = 0 — the spine carries a B2B row per segment with **CAC 0 and payback `never` on the entry-fee basis** | **Undefined — the ratio divides by zero CAC** | immediate | **No customer acquisition cost and no benefit cost.** Structurally the highest-margin book. ⚠ The spine's `never` payback on this row is an artefact of a zero denominator, not a finding |

**Cross-cutting checks the table must answer:**

| Question | Answer |
|---|---|
| Does **any** channel × segment cell have LTV:CAC below 1.0? | **On the entry-fee-only basis, sixteen of the eighteen paid cells — every channel × segment pair except S1 Referral and S6 Referral, which clear at 1.01. On the all-streams basis, none: the lowest is S3 Direct at 4.60.** The two bases give opposite answers, which is the finding |
| At the **Conservative rail (S1 = 1.36)**, does the agent channel go negative? | **Yes on every segment except S1 and S6.** At the Conservative rail net margin per contribution is USD 0.34 for S1/S6 but **−0.45 (S2/S4), −0.68 (S5) and −0.91 (S3)** at Y10 — and the agent channel's mix is the most S3-weighted, so **its dominant cells are loss-making on every collection** |
| What share of Year 1 gross margin does agent commission consume? | **The solved commission is USD 175.68/account.** Against Y1 gross profit of **USD 5,716** across 687 accounts acquired — roughly **USD 8.32 of gross margin per account** — commission at USD 175.68 is **21× the Y1 gross margin it is paid out of.** ⚠ **This is not v1.0's 88%; it is far worse, and the client has seen neither figure.** The commission is affordable only against all-streams LTV (USD 552–949), never against the entry fee |
| Referral reward as % of contribution-margin LTV | **The reward does not bind on LTV at all.** The solve returns **399% of the referee's entry fee** as affordable — 25% of blended all-streams LTV (USD 749) is USD 187 of headroom against a referee entry fee of only USD 47 over a 24-month run. 🔴 **On contribution-margin LTV the picture inverts: F17's 30% reward is roughly USD 14 against an S3 entry-fee-only LTV of USD 5.62 — 250% of it.** v1.0's 19.4% was computed at ~40 paying months against a blended LTV; **the corrected 31.2 months and the per-segment split make the reward unaffordable on the inflow lane and comfortably affordable on the card** |
| **Margin per investor, best to worst cell** | **7.6× on entry-fee margin** (net margin per contribution USD 1.454 at S1/S6 against USD 0.204 at S3 at Y10; identically 7.6× on entry-fee-only LTV, USD 42.55 against USD 5.62) **and 1.72× on all-streams LTV** (USD 949.04 at S1 against USD 551.72 at S3). **v1.0's ~50× estimate is wrong on both bases.** The argument survives the correction but changes shape: **the segment spread is severe in the inflow lane and mild once the card is counted**, which is a sharper version of the same conclusion — an investor-count break-even averages over a 7.6× spread in exactly the lane that is loss-making |

**How LTV is computed, stated so it can be checked:**

```
LTV(s, channel) = Σ over t of [ contribution_margin(s,t) + stream2..6 margin attributable(s,t) ]
                  × survival(s,t)                         [from the archetype mix, D3]
                  ÷ (1 + discount_rate)^(t/12)

  where survival(s,t) is the ARCHETYPE-WEIGHTED survival for that channel's own
  mix — referral-sourced accounts carry an S20 uplift, so channel LTV differs
  even at identical segment mix.
```

⚠ **LTV must include the card.** v1.0's referral analysis computes LTV on contribution margin alone, which for a business where the card is the majority of revenue **understates LTV by a large multiple and therefore overstates the reward as a share of it.** Report both — contribution-margin LTV (the conservative frame, correct if the card never ships) and all-streams LTV — and **say which one the reward is being judged against.**

---

## 8. Assumptions register

Three tables, merged with the ~50 new parameters from `_working_parameter-completion-set.md`. **Every row now carries a Source URL, a Source Category and a Sheet Location** (D19), and the category counts are audited at §8.5.

Source categories: **CITED** (a named primary or secondary source with a retrievable reference) · **DERIVED** (computed from a cited value by arithmetic stated in this brief) · **TRIANGULATED** (bounded by two or more independent cited sources, neither of which states it directly) · **CLIENT INPUT** (supplied by the client) · **ASSUMPTION** (judgement, no source).

### 8.1 Fixed inputs

| ID | Assumption | Value | Unit | Source category | Source | Sheet location | Confidence |
|---|---|---|---|---|---|---|---|
| F1 | Gold price (flat) | **141.46** | USD/g | CITED | USD 4,400/oz, verified 2026-08-17. **Held flat by design: every revenue change is then attributable to the business, not the metal.** Sensitivity axis, not a scenario variable | Assumptions!B4 | High |
| F2 | AED/USD peg | 3.6725 | — | CITED | CBUAE peg | Assumptions!B5 | High |
| F3 | Entry fee, Y1/Y3/Y10 | 5.0 / 4.0 / 3.0 | % | CLIENT INPUT + DERIVED | Decision 9. Falls with bar denomination | Assumptions!B6 | Client range + our arithmetic |
| **F4** | 🆕 **Fabrication premium, by denomination** (D28) | **1.50 / 0.95** | % | **OBSERVED** | 🆕 **100 g / 1 kg. Good Delivery RETIRED as a rung** (§7.1 of the research record). Measured on a same-page dealer pair, goldtrade.ae 19 Aug 2026 19:52: 100 g at **+1.71%** (PAMP 1.75, Valcambi 1.67), 1 kg at **+0.93%** (Emirates 0.98, Etihad 0.87). Less the published **25 bp bulk gradient** at 5+ bars → **1.50% / 0.95%.** Full record and method in `supporting/_working_dealer-premium-and-comparables-research.md`. ⚠ **The genuine 10–50 bar tier is unpublished and still needs the dealer** | Assumptions!B7 | **Moderate** |
| F5 | 🆕 **Float cost of capital — MEMO ONLY (D32)** | 0.49 / 0.31 / 0.38 | % | ASSUMPTION | 🆕 **Removed from COGS at v2.6.** An opportunity cost on equity, not a cash expense; §7.6 already treats locked capital this way and F5 was the one place the brief broke its own rule. **No derivation exists in the corpus.** ⚠ **Do not read this as the float being free — the principal is USD 29k at Y1 rising to USD 3.6M at Y10 and it sits inside peak funding** | Assumptions!B8 | **Low** |
| F6 | SIP hard floor | 20 | USD/month | CITED | Rejected outright below; **never partially credited** | Assumptions!B9 | High |
| F7 | Confirmed SIP gate | 6 | consecutive periods | CLIENT INPUT | Client's own figure | Assumptions!B10 | High |
| F8 | Grace period | 5 | calendar days | CITED | `_draft_sip-rulebook.md` §7.2, revised 2026-08-10. **Rolls off weekends and holidays; crosses the month boundary; never closes two periods** | Assumptions!B11 | High |
| F9 | Withdrawal allowance (Retention = 1.000) | 30 | % per rolling 12m | CITED | Decision 46; `_draft_ics-scoring.md` §1.5 | Assumptions!B12 | High |
| F10 | Collateral seasoning | 90 | days | CITED | Benefits draft §2.5 | Assumptions!B13 | High |
| F11 | LTV ladder, Gold/Platinum/Sovereign | 50 / 65 / 80 | % | CITED | `_draft_ics-scoring.md` §6.2, settled 2026-08-13. **No longer contingent on the partner** | Assumptions!B14 | High |
| F12 | Interchange, Gold/Platinum/Sovereign | 1.80 / 2.05 / 2.10 | % | **CITED, PRIMARY** | **Visa UAE IRF schedule, 18 Oct 2025** | Assumptions!B15 | **High, primary** |
| F13 | Gold Rewards monthly qualifying-spend cap | 3,000 | USD/month | TRIANGULATED | Kinesis-comparable (its cap is USD 2,000) | Assumptions!B16 | Medium |
| F14 | VARA annual supervision, Cat 1 | 200,000 | AED/yr | **CITED, PRIMARY** | **VARA's own rulebook** | Assumptions!B17 | **High** |
| F15 | Minimum paid-up capital | 1,500,000 | AED | **CITED, PRIMARY** | **Locked, not expensed. Do not run through P&L.** Now also appears in the §7.6 funding view | Assumptions!B18 | High |
| F16 | Sumsub Compliance plan | 299 + 1.85 | USD/mo + per check | **CITED, PRIMARY** | **Sumsub's own pricing page.** Minimum binds below 162 checks/mo | Assumptions!B19 | **High** |
| F17 | Referral reward | 30 | % of referee's entry fee over the run | CITED shape, ASSUMPTION value | Shape settled; **the 30 is a placeholder** | Assumptions!B20 | Settled shape |
| F18 | Referral payout lag | 6 | months after referee signup | CITED | Gate cannot be compressed. **Under D4, effectively longer** | Assumptions!B21 | High |
| F19 | Salary loading | 1.10 | × quoted total cash | DERIVED | Not 2.0×. Guides quote base + allowances | Assumptions!B22 | Medium |
| **F20** | **Cost per redemption event** | **4.20** / 2.50 / 9.00 | USD | DERIVED | Outbound AED payment 1.00–2.50 + Sumsub re-screen 1.85 (F16) + operational handling 1.00–4.50. **VARA III.E.4 forbids any offsetting fee, so 100% absorbed** | Assumptions!B23 | **Medium** |
| **F21** | **Card issuance fee** (G/P/S) | 75 / waived / waived | AED, one-off | CITED structure, ASSUMPTION rate | `_draft_ics-benefits.md`: *"issuance and replacement charged at base level, waived at upper levels"* | Assumptions!B24 | Low on rate, **High on structure** |
| **F22** | **Card replacement fee** (G/P/S) | 100 / 50 / waived | AED, per event | ASSUMPTION | Market-normal UAE replacement is AED 75–150 | Assumptions!B25 | Low |
| **F23** | **Average transaction size** (G/P/S) | 185 / 240 / 310 | AED | ASSUMPTION | The tier multiplier splits ~65% into ticket size and 35% into frequency. Implies ~27 / 28 / 30 txns/month | Assumptions!B26 | **Low** |
| **F24** | **Per-transaction processor fee** | **0.10** / 0.05 / 0.15 | USD/authorised txn | **CITED** | **Stripe Issuing's published rate.** Authorisation-based, so **add 6% for declines**. Whether NymCard prices the same way is a term-sheet question | Assumptions!B27 | **Medium** |
| **F25** | **Dispute handling cost** | 22 / 14 / 40 | USD/case | ASSUMPTION | At 0.9 disputes per 1,000 txns Base (1.5 Cons). Includes scheme representment and internal handling | Assumptions!B28 | Low |
| **F26** | **Card production unit cost** (G/P/S) | 4.50 / 7.00 / 14.00 | USD/card | ASSUMPTION | Metal/premium plastic at Infinite. **At Sovereign the production cost exceeds the AED 0 issuance fee by construction** — a real contra-revenue line | Assumptions!B29 | Low-Med |
| **F27** | **Card programme fixed costs** | see below | USD | ASSUMPTION | **No UAE BIN-sponsorship price list is published — confirmed negative.** Structure well-attested, quantum ours | Assumptions!B30–35 | **Low** |
| **F28** | **Origination fee** — gross / Aurumix share | **1.00% of draw / 50%** | % / % | **CITED gross**, ASSUMPTION split | **Finance House UAE gold loan Key Facts Statement carries a 1% processing fee** — the one gross rate with a real UAE anchor | Assumptions!B36 | Medium / Low |
| **F29** | **Servicing fee** — gross / share | 0.50%/yr of drawn / **70%** | % / % | ASSUMPTION | Share highest of the four heads: **servicing is where Aurumix does the actual work** | Assumptions!B37 | Low |
| **F30** | **Penal fee** — gross / share | 2.00% per late event / **40%** | % / % | ASSUMPTION | Share **low on purpose**: penal income belongs to whoever bears the credit risk, and **Aurumix bears none** | Assumptions!B38 | Low |
| **F31** | **Recovery fee** — gross / share | 1.50% of recovered / **0%** | % / % | ASSUMPTION | 🔴 **Zero in Base and Conservative.** Aurumix is the party exposed to the III.E.4 recharacterisation risk | Assumptions!B39 | Low-Med |
| **F32** | **Opex interpolation form** | Log-linear within block on Y1/Y3/Y10 anchors | — | DERIVED | The **step/scale classification** is the substantive fill; the interpolation is arithmetic | Assumptions!B40 | Medium |
| **F33** | **UAE corporate tax rate** | **9%** above AED 375,000; 0% at or below | % | **CITED, PRIMARY** | **Federal Decree-Law No. 47 of 2022** | Assumptions!B41 | **High** |
| **F34** | **Loss carry-forward** | Indefinite; **utilisation capped at 75% of the year's taxable income** | — | CITED | **Article 37, Federal Decree-Law No. 47 of 2022.** Subject to ownership- and business-continuity tests | Assumptions!B42 | Medium-High |
| **F35** | **QFZP treatment** | **Assume NOT a QFZP. Tax at 9% from first profitability** | — | DERIVED | Three reasons at Layer 11. **Modelling 0% and being wrong is a five-year, no-safety-net error** | Assumptions!B43 | Low-Med on eligibility, **High on the recommendation** |
| **F36** | **VAT — resident rate** | 5% standard-rated | % | CITED | UAE VAT standard rate, on service fee lines to UAE residents | Assumptions!B44 | **High** on the rate, Low on line characterisation |
| **F37** | **VAT — non-resident** | 0% (export of services) | % | ASSUMPTION | **Unverified. Three corpus files flag it as needing a tax opinion** | Assumptions!B45 | **Low** |
| **F38** | **Float sizing rule** | `MAX(2 bars, 1 bar + N days trailing inflow)` | grams | **CITED, corpus-settled** | `_draft_allocation-and-float.md`, "Sizing", verbatim. **A rule, not an assumption** | Assumptions!B46 | **High** |

**F27 detail — the card programme fixed cost stack:**

| Line | Base | Aggressive | Conservative | Unit | When booked |
|---|---|---|---|---|---|
| BIN sponsorship setup | 45,000 | 25,000 | 90,000 | USD one-off | **M15** |
| Scheme joining / certification | 30,000 | 18,000 | 60,000 | USD one-off | **M15** |
| BIN sponsorship monthly minimum | 6,000 | 3,500 | 12,000 | USD/month | M18 onward |
| Processor platform monthly minimum | 5,000 | 3,000 | 9,000 | USD/month | M18 onward |
| Visa scheme quarterly minimum | 12,000 | 7,000 | 22,000 | USD/quarter | M18 onward, quarter-end |
| **Annualised run-rate from M18** | **180,000** | **106,000** | **340,000** | USD/yr | |

**The volume at which the minimum stops binding, which is the number that matters.** At Base, USD 180,000/yr against Gold-tier net interchange of ~0.79% of transaction value requires roughly **USD 22.8m of annual card spend — about 290 active cards at AED 6,000/month.** On a Y2 book with a 65% activation rate the programme is roughly at or just past that threshold when it launches at M18. **So the card programme's fixed cost is approximately break-even at launch and immaterial thereafter — but only at Base assumptions.** At Conservative (USD 340,000/yr, 55% PM share, AED 3,500 spend) the required active-card count is roughly **1,100**, which the model will not reach until well into Y3. **The card programme runs at a loss for its first 12–18 months in the Conservative case, and v1.0's break-even table does not carry that drag.**

⚠ **Book F27 against stream 2 activation, not against opex.** It is a contra-cost that only exists if the card exists; burying it in the opex block hides the conditionality.

### 8.2 Scenario variables

| ID | Parameter | Base | Aggressive | Conservative | Unit | Source category | Why it varies | Sheet |
|---|---|---|---|---|---|---|---|---|
| **S1** | 🆕 **Rail cost per collection event — PASS-THROUGH (D31)** | **0.25** | 0.10 | **1.36** | USD | TRIANGULATED | 🆕 **No longer a margin driver.** Grossed up onto the request and remitted; drives `rail_memo` and the §13.3 refusal risk only. AANI unpublished; UAEDDS at AED 5 is Emirates NBD's published tariff. ⚠ **It leaves the tornado, where it ranked 6th at USD 1,607,643 of swing** — that swing does not move elsewhere, it ceases to exist in the P&L and reappears as unmodelled churn risk. **Still the number most worth a phone call, for a different reason: it sets what the customer is asked to accept** | Scen!A |
| **S2** | **Persistency, M13 survival** | **55** | 65 | 45 | % | DERIVED | 🔴 Governs LTV, referral economics and agent commission at once. **At v2.0 it is an OUTPUT of S27, not an input** — carried here as the calibration target | Scen!A |
| **S3** | **PM share of gross interchange** | **72** | 85 | 55 | % | TRIANGULATED | 🔴 Sizes the largest stream. **No UAE/MENA figure published. Floor is 36%** | Scen!C |
| S4 | Monthly card spend per active card | 6,000 | 9,000 | 3,500 | AED | TRIANGULATED | Expat survey mean AED 6,170; Kinesis cap implies AED 7,345 | Scen!C |
| S5 | Card activation rate | 65 | 80 | 45 | % | TRIANGULATED | PULSE 68.2%, Monzo 68%. **No primary source exists.** Use High if issued only to funded balances | Scen!C |
| S6 | Gold volatility | 25 | 20 | 35 | % annualised | CITED | Drives price-gap risk. ~30% trailing 12m, 17% 20-year average | Scen!A |
| S7 | Fabrication premium (Y1) | 3.00 | 2.00 | 4.50 | % | ASSUMPTION | **Dealer-blocked. Four research passes returned nothing** | Scen!A |
| S8 | Credit take-up among eligible | 18 | 30 | 8 | % | DERIVED | Indian gold-loan penetration <10% at a point in time; pre-selection uplift | Scen!D |
| S9 | Drawn as % of permitted limit | 50 | 70 | 30 | % | TRIANGULATED | Revolving facilities draw 40–55% of permitted | Scen!D |
| S10 | Self-custody leakage | 12 | 6 | 30 | % of AUM/yr | ASSUMPTION | **At v2.0 this is the aggregate S31 reconciles to, not an independent input** | Scen!B |
| S11 | Family plan attach rate | 20 | 35 | 10 | % | ASSUMPTION | **Nothing stated in the corpus.** Pure assumption | Scen!E |
| S12 | Agent productivity | 4 | 6 | 2 | accounts/agent/month | TRIANGULATED | Insurance agency comparator | Scen!A |
| S13 | B2B partner AUM by Y10 | 200 | 400 | 50 | USD m | ASSUMPTION | Requires a signed partner | Scen!E |
| S14 | Vault storage rate | 0.25 | 0.15 | 0.40 | % of AUM/yr | CITED | Verified range. **Minimum binds below ~250 kg** | Scen!F |
| S15 | Marketing CAC (base) | 120 | 80 | 200 | USD | ASSUMPTION | **No UAE gold-product benchmark.** Modified by the S25 curve | Scen!A |
| **S16** | **Channel-to-region mix matrix** 🆕 **re-cut to R1–R4 (D25)** | three-phase tables | Direct/referral +8pp toward R1 | Agent +10pp toward the floor band | % of channel volume | ASSUMPTION | **No published channel-mix data for any comparable product.** Two structural rules matter more than the cells (§3 Layer 1). ⚠ **The agent row now needs a non-Indian recruitment assumption to reach R2 at all** | Scen!A |
| **S17** | **Agent ramp factor** M1–M6/M7-12/M13+ | .20/.40/.60/.75/.85/.95 / 1.00 / 1.05 | .35→1.15 | .10→0.95 | × S12 | ASSUMPTION | Insurance-agency ramp. **Six months to full productivity happens to match the Confirmed SIP gate** — an agent cannot credibly sell the tier ladder until a client has passed it | Scen!A |
| **S18** | **Agent annual attrition** | **45** | 30 | 60 | %/yr | TRIANGULATED | Indian life-agency attrition runs 40–60% in year one. **Missing from T7 entirely** | Scen!A |
| **S19** | **Referral rate** | **0.45** | 0.90 | 0.18 | referrals/qualified referrer/yr | ASSUMPTION | Cap removed deliberately, so the distribution is right-skewed. **Model the mean, not the median** | Scen!A |
| **S20** | **Referral conversion** | **62** | 72 | 48 | % | DERIVED | Exactly the M7 survival of the referred cohort, uplifted ~1.1× off our own fitted curve | Scen!A |
| **S21** | Referral-driven accounts | `qualified_referrers × S19 ÷ 12 × S20` | | | accounts/month | DERIVED | **Two six-month gates in series → steady state not before ~M25** | Model |
| **S22** | **Regional penetration ceiling** R1–R4 🆕 **re-cut (D25)** | **9.5 / 6.0 / 4.0 / 0.35** | 14 / 9 / 6 / 0.60 | 6 / 3.5 / 2.5 / 0.15 | % of the §5.1 base | ASSUMPTION | Applied to the **active, IBAN-capable, income-qualified** base. The unsourced gold-propensity filter is deleted (§5.1). **`base × ceiling` is the invariant: 165,750 total, held equal to v2.1's 164,900 on purpose.** R4 at 0.35% of 12.5m is ~43,750 accounts | Scen!A |
| **S23** | **Saturation functional form** | Logistic on remaining headroom | | | — | DERIVED | **Use cumulative-ever-acquired, not live accounts.** ~5× difference by Y10. **The single most important structural fill in Block A** | Model |
| **S24** | Marketing → accounts | `spend ÷ effective_CAC` | | | accounts | DERIVED | S15 must not be flat — see S25 | Model |
| **S25** | 🆕 **CAC diminishing returns — RETIRED to a switch, default OFF** (D27) | **OFF. `effective_CAC = S15`, linear** | OFF | OFF | — | **DEMOTED, not deleted** | **The live model is linear.** The curve `S15 × [1 + 0.35 × (spend ÷ 60,000)^0.7]` is preserved on Scenario Parameters as `CAC_CONVEXITY`, default OFF, with its v2.2 flexes (exp 0.5 / div 100,000 and exp 0.9 / div 35,000) intact. **Reason for retirement: §18 item 11 — the functional form is defensible, the constants are not, and there is no UAE benchmark to calibrate them against.** Convexity is a *dynamic*, and dynamics are Phase 5's deliverable. ⚠ **Turn the switch ON before quoting direct-channel LTV:CAC at high spend** | Scen!A |
| **S26** | Organic share of direct | 12 | 20 | 5 | % of direct | ASSUMPTION | Kept separate so the CAC curve is not applied to it | Scen!A |
| **S27** | **Payment archetype weights + hazards** | 10/35/12/13/30 + background | see §3 Layer 5c | see §3 Layer 5c | % / monthly hazard | DERIVED (aggregate), **ASSUMPTION (decomposition)** | 🔴 **Rank 1 load-bearing.** Fitted to reproduce §0.5. **No source decomposes a lapse curve into payment archetypes — confirmed negative** | Scen!B |
| **S28** | **Reduction capture rate** | **33** | 50 | 18 | % of would-be lapses | ASSUMPTION | **Base is set at v1.0's own illustrative third, deliberately, so v2.0 does not silently invent a different number.** Apply only to affordability-driven lapse | Scen!B |
| **S29** | **Reduction depth** | **MAX(20, 50% of prior ticket)** | 65% of prior | Straight to 20 | USD/month | ASSUMPTION | **Corrects a real v1.0 error.** The floor is the *hard* minimum, not the *observed* landing point. 🆕 **D25: applies to the standard band only.** The floor band is already at the floor and cannot reduce, per the F6 hard gate | Scen!B |
| **S30** | **Hazard multiplier, REDUCED** | **1.35×** | 1.15× | 1.75× | × monthly hazard | ASSUMPTION | **Must be well above 1.0 or REDUCED becomes a free retention machine; well below the pure-lapse case or the state does no work** | Scen!B |
| **S31** | **Withdrawal-behaviour distribution** | six buckets, §3 Layer 6 | as tabled | as tabled | % of population | ASSUMPTION | Buckets deliberately straddle the 30% kink. **Reconciles to S10 within 0.3pp in all three scenarios** | Scen!B |
| **S32** | **Redemption rate** | **8** | 4 | 16 | % of AUM/yr | ASSUMPTION | **A different event from S10/S31 and a separate line.** PAXG turnover of 5.9% is the only comparator and it is a token-turnover figure | Scen!B |
| **S33** | **Lapsed-holder redemption multiplier** | **2.2×** | 1.6× | 3.5× | × contributing rate | ASSUMPTION | 🔴 **Rank 4 load-bearing.** At 19% M61 persistency, **81% of ever-acquired accounts are lapsed by Y6** and this governs the dominant AUM decay term from ~Y4. **v1.0 has no lapsed-holder decay term at all** | Scen!B |
| **S34** | **Foreign spend share** | **34** | 45 | 24 | % of card spend | ASSUMPTION | **Apply as the S53 seasonal vector, not as a constant** | Scen!C |
| **S35** | **ATM withdrawal per cardholder** | 950 mean, **six-bucket distribution** | 1,600 | 500 | AED/month | ASSUMPTION | **Set deliberately just below the Gold allowance of AED 1,000 — that is the finding.** The distributional treatment is the important part | Scen!C |
| **S36** | Card issuance event rate | 1.00 at activation, **+0.06/yr** | +0.04 | +0.10 | events/card/yr | ASSUMPTION | **A tier upgrade forces a physical reissue** — a real cost v1.0 does not carry | Scen!C |
| **S37** | Card replacement event rate | 0.11 | 0.07 | 0.18 | events/card/yr | ASSUMPTION | Industry-normal loss/theft/damage sits around 8–15% annually | Scen!C |
| **S38** | **Card spend tier multipliers** | **0.82 / 1.12 / 1.54** | 0.85/1.10/1.45 | 0.78/1.15/1.70 | × S4 | DERIVED | Normalises to 1.018 at the Y10 mix. **v1.0's flat AED 6,000 overstates Y3–Y5 interchange by 8–12%** | Scen!C |
| **S39** | **Card fraud and chargeback** | **9** | 5 | 22 | bps of spend | CITED + ASSUMPTION | Visa's published global average ~8 bps. **No UAE issuer fraud rate is published — confirmed negative** | Scen!C |
| **S40** | **Facility turnover, peak→average** | **0.42** | 0.55 | 0.30 | × peak drawn | DERIVED | **Cuts stream 5 by 1.88×** — an arithmetic correction, not a sensitivity, derived from Manappuram's 71-day realised tenor. ⚠ **The larger cut is the collateral base per holding account, at 2.96×.** On the tornado S40 ranks **11th of 13** by swing, not 2nd | Scen!D |
| **S41** | Draw events/borrower/yr | 2.1 | 3.2 | 1.3 | events/yr | DERIVED | **Moves with S40. Do not flex independently** | Scen!D |
| **S42** | **Partner count by year** | 1/2/3/4/6/8 | 1/3/5/7/11/15 | 1/1/1/2/2/3 | partners | ASSUMPTION | Enterprise cadence for a pre-revenue infrastructure vendor | Scen!E |
| **S43** | **Per-partner AUM ramp** | 8/25/48/70/85/100% at M6/12/24/36/48/60 | 100% by M42 | 100% by M84 | % of terminal | ASSUMPTION | **Each partner runs its own clock from its own go-live** | Scen!E |
| **S44** | **Terminal AUM per partner** | **32** | 45 | 22 | USD m | DERIVED | Reconciles to S13 within ~5% on all three paths | Scen!E |
| **S45** | **Spot attach rate** | **14** | 24 | 7 | % of live accounts/yr | ASSUMPTION | 🔴 **Rank 8 load-bearing — because it is missing, not because it is large** | Scen!B |
| **S46** | **Average spot ticket** | **620** | 1,100 | 320 | USD/event | ASSUMPTION | Scale by segment: S1/S6 ×1.6, S2/S4 ×1.0, S3 ×0.45, S5 ×0.7 | Scen!B |
| **S47** | **Spot frequency** | **1.7** | 2.4 | 1.2 | events/attacher/yr | ASSUMPTION | ~45% of volume in the two festival windows. 🆕 **First external check: Botim's disclosed 128,000 trades against ~45,000 buyers implies ~2.8 purchases each, ≈1.9/yr** (D35, §5.9.4). ⚠ **INFERRED from two disclosures of different vintage; supportive, not confirmatory** | Scen!B |
| 🆕 **S56** | **Spot payment-capability filter** | `{{UNFILLED: spot lane payment filter — see §5.9.2}}` | | | share of economically active | **ASSUMPTION, unsourced** | 🆕 **D35.** Replaces the SIP lane's 0.57 IBAN filter for the spot lane only. A one-off push needs an account, not a standing mandate, so a WPS payroll card qualifies here and does not qualify for SIP. **Candidate anchor: Findex UAE account ownership 85.7%** (§5.4), which is the same figure §5.4 warns must not be read as mandate-capable. ⛔ **Do not fill by inference: §5.1 deleted the unsourced propensity filter for exactly this reason** | Scen!A |
| 🆕 **S57** | **Spot money-capability filter** | `{{UNFILLED: spot lane discretionary filter — see §5.9.2}}` | | | share of payment-capable | **ASSUMPTION, unsourced** | 🆕 **D35.** Replaces the SIP lane's 0.40 filter. **Directionally above 0.40**: one spot ticket is ~USD 190 once, against USD 240/yr for a USD 20 SIP, so spot asks for less money less reliably. 🔴 **No published source exists**, and §5.7 item 7 (no nationality-disaggregated UAE savings survey) blocks the obvious route | Scen!A |
| 🆕 **S58** | **Spot penetration ceiling** R1–R4 | `{{UNFILLED: spot ceiling by region — see §5.9.4}}` | | | % of the spot-only base | **ASSUMPTION, unsourced** | 🆕 **D35.** Decomposes as **`reach × conversion`**. ✅ Conversion is observed at **~6%** (Botim, 775k explored → 45k transacted). 🔴 **Reach is NOT observed and Botim's 8.5m → 775k step must not be reused**: it is a 9.1% in-app discovery rate off a shelf Aurumix does not have. ⛔ **Treating the 6% as the ceiling silently assumes total reach** | Scen!A |
| 🆕 **S59** | **Spot-to-SIP conversion rate** | `{{UNFILLED: no source exists anywhere — see §5.9.7}}` | | | % of spot holders/yr | **ASSUMPTION, unsourced** | 🔴 🆕 **D35. The load-bearing parameter of the whole section, and the most decision-relevant number in the brief.** The mechanism design calls this arrow *"the growth funnel"* (`_draft_sip-spot-and-ics.md`); the model currently runs it only backwards. **It is the adoption-bridge question in numerical form and the one an experiment could actually answer.** ⚠ **Must be carried into the tornado, not buried** | Scen!A |
| **S48** | **Y1 exit-run-rate uplift** | **1.40×** | 1.25× | 1.60× | × Y1 booked opex | ASSUMPTION | **The Y1 figure is a build-up year average, not a run-rate** | Scen!F |
| **S49** | **Resident share by region** 🆕 **R1–R4 (D25)** | **100 / 100 / 0 / 0** | same | same | % UAE-resident | **DERIVED, definitional** | **Falls straight out of decision 31's re-cut by country of residence.** ⚠ The Y10 non-resident share must be re-computed; the 42% at v2.1 is withdrawn (§5.8) | Scen!F |
| 🆕 **S54** | **Floor share by region** | **40 / 60 / 58 / 25** | 30/50/48/18 | 50/70/68/33 | % of the region's book paying the USD 20 floor | ASSUMPTION | 🆕 **D25. The parameter that saves two non-linearities** (rail cost and card spend, §5.2). With S55 it derives two bands per region, so **no unit economic is ever computed on a regional average.** Anchored on Bahrain's published wage distribution and Joyalukkas' AED 100 price discovery; **weakest link is the absence of any nationality-disaggregated UAE savings survey** (§5.7 item 7) | Scen!A |
| 🆕 **S55** | **Average monthly ticket by region** | **38 / 26 / 26 / 30** | 46/32/32/36 | 30/21/21/24 | USD/month | TRIANGULATED | 🆕 **D25.** Savings-capacity anchored, not remittance anchored. Cross-checked against Joyalukkas AED 100 and Malabar AED 200, and sits **below** AMFI's USD 34, which is the correct direction. 🔴 **Book-weighted average falls from ~40 to ~31.5, which pushes the §0.3 minimum viable entry fee UP** | Scen!A |
| **S50** | **Float buffer days (N)** | **10** | 6 | 20 | days of trailing inflow | ASSUMPTION | The corpus rule states N without setting it | Scen!F |
| **S51** | 🆕 **Float carry mode** (D29) | 🔴 **OWN FLOAT FROM M1** | dealer-carried throughout | own float from M1 | — | **DERIVED** (the side is now forced, not chosen) | 🆕 **Aurumix cannot avoid carrying metal, because all three routes its comparables use are closed to it: it cannot run briefly unbacked (the `trust ≥ tokens` invariant and decision 34), it cannot decline a repurchase obligation (VARA III.E.4 plus the formulaic buyback), and it cannot lean on a named dealer filling instantly because no dealer exists.** So price-gap and float capital **bite from M1**, and the premium **narrows** — which is what F4's re-base reflects. ⚠ **Charging the wide dealer-carried premium AND both float costs double-counts under either regime — correction 12** | Scen!F |
| **S52** | **Seasonality vectors** (a) acquisition (b) card spend | tables at §12 | amplitude ×1.4 | amplitude ×0.6 | multiplier, **normalised to 12.00** | CITED drivers, ASSUMPTION amplitudes | Festival timing is not in dispute; **how much a Dubai savings signup responds to Dhanteras is** | Scen!F |
| **S53** | **Foreign-spend seasonal vector** | 30/30/30/32/34/**55**/**60**/**56**/36/42/40/32, rescaled to a 34% mean | — | — | % of monthly spend | ASSUMPTION | **The summer travel season is the model's single largest stream-4 month even though it is the weakest total-spend month** | Scen!C |

### 8.3 Time-evolving inputs

| ID | Parameter | Y1 | Y2 | Y3 | Y5 | Y10 | Pattern | Source category |
|---|---|---|---|---|---|---|---|---|
| T1 | Entry fee base rate | 5.0% | 5.0% | 4.0% | 4.0% | 3.0% | Step, with bar denomination | CLIENT INPUT |
| T2 | Fabrication premium | 3.00% | 3.00% | 2.00% | 2.00% | 0.75% | Step, with bar denomination | ASSUMPTION |
| T3 | 🆕 Bar denomination | 100 g | 100 g | 1 kg | 1 kg | **1 kg** | **Threshold rule on trailing 12m inflow, latched** — §3.x.3. 🆕 **The 12.4 kg rung is RETIRED** (D28): Dubai's own Good Delivery standard is a 1 kg bar, so the ladder tops out at 1 kg and the endogenous solve now has two rungs, not three | DERIVED |
| T4 | Tier mix: share at Gold+ | 0.0% | 15.7% | 25.0% | 41.2% | **63.0%** | **Computed by the ICS engine per archetype track, then weighted** | **OUTPUT** |
| T5 | Tier mix: share at Sovereign | 0% | 0% | 0% | 0% | **4.4%** | **First Sovereign at M61. At v2.0 this is genuinely computed** — v1.0 carried it as an input, contradicting T4's own note | **OUTPUT** |
| T6 | PM share (contract maturity) | — | 55% | 55% | 72% | 72% | Steps at scale | ASSUMPTION |
| T7 | Active agents | 5 | 15 | 40 | 90 | 200 | **Stock. Must be grossed up by S18 attrition into a recruit flow** | CLIENT INPUT |
| **T8** | **Non-resident share of the book** | 0% | `{{UNFILLED: Y2 non-resident share — not in spine}}` | `{{UNFILLED: Y3 non-resident share — not in spine}}` | `{{UNFILLED: Y5 non-resident share — not in spine}}` | ~42% | **Computed from the segment ramp × S49** | **OUTPUT** |
| **T9** | **Float capital (own-float case)** | ~29k | `{{UNFILLED: Y2 float capital, USD — not in spine; the model runs dealer-carried to Y3, so float capital is booked at zero through Y2}}` | ~437k | **~USD 291k** (float capital at M60; the model's own-float path reaches USD 334k at M72 and USD 431k at M120, far below the brief's ~3.6M Y10 own-float figure) | ~3.6M | **Computed from F38 × T3 × F1** | DERIVED |
| **T10** | **Cumulative-ever-acquired ÷ live** | ~1.1× | `{{UNFILLED: Y2 cumulative-to-live ratio — not in spine; the spine tabulates holding:live, not cumulative-ever-acquired:live}}` | `{{UNFILLED: Y3 cumulative-to-live ratio — not in spine}}` | `{{UNFILLED: Y5 cumulative-to-live ratio — not in spine}}` | **~5×** | **The saturation denominator. Report it — it is the sanity check on S23** | **OUTPUT** |

### 8.4 Dependency map

```
Agents (T7) ──gross up──> Recruits (S18) ──> Ramp (S17) ──> Productivity (S12)
   │                                                              │
Referrers ──S19──> Referrals ──S20──> │                          │
   │                                   │                          │
Marketing spend ──S25 CAC curve──> Paid ──+ S26 organic──> │      │
   │                                                        │      │
Partners (S42) ──S43 ramp──> Partner AUM ──────────┐        │      │
                                                    │        v      v
                                                    │   S16 CHANNEL→SEGMENT MIX
                                                    │        │
                                                    │        v
                                                    │   S23 SATURATION on
                                                    │   cumulative-ever-acquired
                                                    │   ÷ (S22 ceiling × §5 base)
                                                    │        │
                                                    │        v  × S52a seasonality
                                                    │   NEW ACCOUNTS by segment
                                                    │        │
                                                    │        v
                                                    │   S27 ARCHETYPE SPLIT (5 tracks)
                                                    │        │
                                                    │        v
                                                    │   SIX-STATE MACHINE
                                                    │   PRE-GATE│CONTRIB│REDUCED
                                                    │   REG-BLOCK│STOPPED│DORMANT
                                                    │   (S28 capture, S29 depth,
                                                    │    S30 hazard, 12-period
                                                    │    absorbing boundary)
                                                    │        │
                             ┌──────────────────────┼────────┴────────┐
                             │                      │                 │
                             v                      v                 v
                   contributing + reduced    holding_not_          PRE-GATE
                             │               contributing         + NEVER-GATED
                             │                      │                 │
                             v                      │            full fee, ZERO
                   SIP + SPOT INFLOW                │            benefits, forever
                   (S45,S46,S47)                    │                 │
                             │                      │                 │
                             v                      v                 │
                   ┌─── AUM STOCK ◄─────────────────┘                 │
                   │         │                                        │
                   │         ├── S31 self-custody ──┐                 │
                   │         ├── S32 × S33 redemption ┤                │
                   │         │                        │                │
                   │         │                        v                │
                   │         │            🔴 THE ARROW v1.0 OMITS:     │
                   │         │            LEAKAGE → Sold → RETENTION   │
                   │         │                        │                │
                   │         │                        v                │
                   │         │            ICS ENGINE ◄─────────────────┘
                   │         │            run_length → gate → Record,
                   │         │            Standing, Retention
                   │         │                        │
                   │         │                        v
                   │         │            THRESHOLD PER TRACK, THEN WEIGHT
                   │         │                        │
                   │         │                        v
                   │         │                 TIER DISTRIBUTION
                   │         │                        │
                   │    ┌────┴───────┬───────────┬────┴──────┬──────────┐
                   │    v            v           v           v          v
                   │  STREAM 6   custody     collateral   ENTRY-FEE   CARD +
                   │  (AUM×bps)   cost        base        DISCOUNT    CREDIT
                   │              (S14)       │           (benefit    ELIGIBILITY
                   │                          v            cost)      │
                   │                       STREAM 5 ◄── S40 turnover  v
                   │                                              STREAMS 2 & 4
                   └── NET FLOW ──> MAX(0,−net) × spread              │
                                    = STREAM 0 cost              F24 per-txn,
                                                                 S39 fraud,
                                                                 F27 fixed
```

🔴 **The arrow v1.0 omits, and it is a live bug.** v1.0's §8.4 shows `Leakage (S10) → AUM → streams 2,3,5,6` and **omits the arrow to `Sold → Retention → tier` entirely.** `Sold` is computed on grams held versus 12 months ago plus acquisitions, and **makes no distinction between redemption and self-custody withdrawal — both hit the numerator identically.** So leakage drives `Sold` → `Retention` → tier → **benefit costs and interchange rate.** Setting S10 to its Conservative 30% puts the average customer **exactly at the Retention kink**, which would cascade tier downgrades across the book — and nothing in v1.0 says so (D11).

**Load-bearing assumptions, ranked by measured swing in cumulative net profit.** 🔴 **This ranking is now the tornado's, not the a-priori list's.** §13.5 states the rule — *if the tornado disagrees with the ranking, the tornado is right and the ranking gets updated* — and it disagreed, so it has been updated.

| Rank | ID | Swing in cumulative net profit | Why it carries |
|---|---|---|---|
| **1** | **S4 — card spend per active card** | **USD 14,177,704** | Larger than the next two combined. **No PM share saves the business at AED 3,500 of card spend and every PM share works at AED 9,000** — which inverts v1.0's ranking of S3 above S4 |
| **2** | **S5 — card activation rate** | **USD 6,539,376** | How many eligible accounts actually carry a live card. Triangulated from PULSE and Monzo; no primary source exists |
| **3** | **S3 — PM share of interchange** | **USD 6,359,822** | Sizes the largest single stream. **No UAE/MENA figure is published anywhere.** Floor 36%; **77.5% was the smallest share producing any EBITDA-positive year on the ten-year run.** ⚠ On a 7-year horizon the required share is higher; the rebuild re-solves it |
| **4** | **F27 — card programme fixed costs** | **USD 2,125,500** | Runs the card at a loss for its first 12–18 months in the Conservative case — drag v1.0's break-even does not carry. **Flexed for the first time this round and it lands 4th** |
| **5** | **S27 — payment archetype mix** | **USD 1,906,962** | 🔴 **Genuinely load-bearing, and not first.** It *is* the persistency curve and it *is* what makes the tier distribution computable. But on this cost base the card triple outweighs it by roughly **seven to one**, because a book that persists better simply carries more of the same loss-making inflow lane |
| **6** | **S1 — rail cost per collection** | **USD 1,607,643** | Decides the sign of stream 1's margin, and whether the agent channel is viable at all. **A Year 1–3 survival problem, not a terminal-value driver** |
| 7 | **S11 — family attach** | USD 694,515 | Scales stream 3 linearly off a pure assumption |
| 8 | **S14 — vault storage rate** | USD 359,350 | Ad valorem on the holding book |
| 9 | **S45 — spot attach** | USD 167,891 | **Load-bearing because it was missing, not because it is large** |
| 10 | **S10 — self-custody leakage** | USD 149,353 | Drives `Sold` → Retention → tier, the arrow v1.0 omits |
| 11 | **S8 — credit take-up** | USD 56,569 | Stream 5 is immaterial at every modelled scale |
| 12 | **S40 — facility turnover** | USD 17,519 | **Ranked 2nd a priori and 12th on measurement.** It is a real arithmetic correction, but a small one against a stream that is 0.2% of gross profit |
| 13 | **S48 — Y1 opex exit run-rate** | USD 1,975 | Last, and the measurement understates the concern — see below |

⚠ **S48 ranks last, and that is not the reassurance it looks like.** The Y1 opex base is roughly 12% of the ten-year cost stack, so flexing its exit run-rate cannot move a *cumulative* total much regardless of whether the underlying concern is real. **VALIDATION §6 item 2 still stands: the Y1 figure is a partial year of a business that has not finished hiring, and early-year break-even is flattered by roughly 40% of the Y1 cost base.** A ten-year cumulative is the wrong horizon on which to measure a first-year timing problem.

**The a-priori ranking, kept for contrast, because the disagreement is itself the finding:** S27 (1), S40 (2), F24+F23 (3), S33 (4), S23+S22 (5), F27 (6), S16 (7), S45–S47 (8), F35 (9), S28+S29+S30 (10). **Three of the tornado's top four — S4, S5 and S3 — do not appear on the a-priori list at all**, while its own top two land 5th and 12th. The a-priori list ranked parameters by *how much of the model's structure they touch*; the tornado ranks them by *how much money moves*. **Both are legitimate questions and they have different answers — but for a client conversation about what to negotiate, the tornado is the right list.** ⚠ **F24+F23, S33, S23+S22 and S16 were never flexed in either tornado**, so their absence from the measured ranking is untested, not disproved.

**Cosmetic — get them roughly right and move on:** F21, F22, S36, S37 (a few AED per card per year against AED 6,000/month of spend — rounding error on stream 4); F25 (~0.9 cases per 1,000 transactions at USD 22); F26 (a one-off USD 4.50–14.00 against a multi-year relationship); **F20** (interesting as a *structural* finding — a mandatory zero-revenue cost line — but not as a number); F30 (expected value ~USD 4/borrower/yr; **the reasoning for setting the share low is worth more than the number**); S26; **S52b** (normalised to 12.00, so it cannot change the annual total — it matters for cash-flow timing and nothing else); **F31** (a parameter set to zero for a defensible legal reason is not a sensitivity); **S18** (load-bearing-adjacent, but it acts on S12 and S17 which are already flexed — **flexing all three independently double-counts**).

### 8.5 Sourcing audit

**New at v2.0** (D19). Counts across §8.1–§8.3 — 38 fixed inputs, 53 scenario variables, 10 time-evolving inputs, **101 parameters in total.**

| Category | Count | % of total | What it means |
|---|---|---|---|
| **CITED** | `**25**` | `**24.8%**` | A named primary or secondary source with a retrievable reference |
| **DERIVED** | `**19**` | `**18.8%**` | Computed from a cited value by arithmetic stated in this brief |
| **TRIANGULATED** | `**8**` | `**7.9%**` | Bounded by two or more independent cited sources, none stating it directly |
| **CLIENT INPUT** | `**3**` | `**3.0%**` | Supplied by the client |
| **ASSUMPTION** | `**42**` | `**41.6%**` | Judgement, no source. ⚠ **The spine's own audit surface is a different and narrower count: 10 `DERIVED_BY_MODEL` parameters (VALIDATION §5) and 9 resolved source conflicts (VALIDATION §4). Neither maps onto this five-way split of 101 register rows** |
| **OUTPUT** | **4** | **4.0%** | Computed by the model, not an input. T4/T5 (tier mix), T10 and the gate-arrival distribution. ⚠ **v1.0 carried T4/T5 in this register as assumptions while claiming the tier mix was computed. At v2.0 they are genuinely outputs and are marked as such** |
| **Total** | **101** | 100% | |

**What the audit is for, and it is not decoration.** Three things should be read off it before the model is presented:

1. **The CITED share concentrates in the regulatory and rate parameters** — VARA fees, the Visa IRF schedule, the corporate tax rate, the Sumsub pricing page — and **thins out sharply in the behavioural block.** That is the honest shape of a pre-launch model and it should be stated rather than smoothed.
2. **Six of the top ten load-bearing parameters are ASSUMPTION-category.** S27, S33, S16, S45–S47, S28–S30 all carry judgement values. **The model's most consequential inputs are its least sourced ones, which is a structural feature of modelling a product that does not exist yet — but the client should hear it once, plainly.**
3. **Confirmed negatives are a category of finding, not a gap.** Where no source exists we say so and record the search: no UAE/MENA interchange split, no CBUAE card-level data, no UAE issuer fraud rate, no BIN-sponsorship price list, no published channel mix for a comparable product, no monthly-versus-annual persistency split in Indian data, and **no decomposition of any savings or insurance lapse curve into payment-behaviour archetypes.** Seven confirmed negatives, listed at §18.

---

## 9. The parameter solver

Phase 2 parked eight parameters with the note *"locks against the revenue model, Phase 4."* **Seven of them are live. The eighth is retired** (D8).

### 9.1 The seven

| # | Parameter | What Phase 2 says | What the model solves for |
|---|---|---|---|
| **1** | **Entry-fee base-rate uplift to fund the discount ladder** | 🆕 The ceiling is 1.5pp at Sovereign against a Y1 net contribution margin of **2.79% at the measured premium** (was 0.72%, D28/D31/D32). ⚠ **"The ceiling exceeds the available margin" no longer holds and the item must be re-solved** | **0.696pp** — the book-weighted discount at the Y10 computed tier mix. The 1.5pp Sovereign ceiling touches only 4.4% of accounts, so the ladder costs **less than half its headline.** See §9.2 |
| **2** | **Acquisition budget ceiling** | One board-approved cap covering member rewards plus all agent commission at every level, as a % of entry-fee revenue. Modelled on IRDAI's Expenses of Management regime | **29.1% of TOTAL revenue** (acquisition 8,458,460 against total revenue 29,032,342, cumulative). 🔴 **Expressed against entry-fee revenue as this row asks, the ceiling is 338% — which is meaningless, and confirms the brief's own flag. Total revenue is the right denominator.** The front-loading brake schedule is still unsolved |
| **3** | **Referral reward size** | Shape settled at 30% of the referee's entry fee over six contributions, split equally, in grams. **The 30 is a placeholder** | **399% of the referee's entry fee** — i.e. **LTV does not bind and F17's 30% placeholder is affordable.** 25% of all-streams LTV (749 blended) is USD 187 of headroom against a referee entry fee of only USD 47 over a 24-month run. 🔴 **The binding constraint on the referral reward is the acquisition budget (item 2), not LTV** |
| **4** | **Agent commission rate** | The client's only written number is 15% of a fee whose base no longer exists. Transplanted, it consumes **88% of Y1 gross margin** | **USD 175.68/account**, split across three levels on a 4/5/6 front-loaded gradient = **46.85 / 58.56 / 70.27.** Derived from an agent pool of USD 5,075,076 over 28,889 agent-sourced accounts. Subject to the item 2 ceiling |
| **5** | **B2B platform fee rate** | Placeholder 0.5–0.75%/yr. The SafeGold precedent says the margin cannot come from the entry spread | **35 bps floor** (vault rate 25bps + 10bps target margin); **modelled at 60 bps**, which on Y10 partner AUM of USD 215,306,667 yields **USD 1,291,840/yr.** The placeholder range survives the solve — 60bps sits comfortably above the floor |
| **6** | **Family plan and Digital Will price** | USD 29–36/yr including 4 beneficiaries, awaiting client sign-off, against a USD 1.80–2.90 per-name floor plus a 20-to-40-year screening tail | **USD 32/yr + USD 20/name** — the corpus midpoint, against a USD 2.35 per-name floor (~5× headroom). **Carried from the corpus and confirmed, not re-solved** |
| **7** | **Minimum viable PM share** | Phase 2 derived the floor: **36%** at Sovereign, below which Gold Rewards stops self-funding | **The floor is already derived and verified (0.75 ÷ 2.10 = 35.7%).** The model solves the *commercial* number by bisection: on the ten-year run, **77.5% PM share was the smallest share producing any EBITDA-positive year**, against the Base assumption of 72% and the Aggressive case of 85%. 🔴 **The result that matters and that a shorter horizon only strengthens: no PM share in the researched 55–85% range reaches cash break-even by Y7.** ⚠ **The 77.5% figure is a ten-year solve and must be re-solved on the 7-year basis; expect it to rise.** ⚠ **The 36% floor is computed against the 2.10% Sovereign rate and therefore survives the D22 collapse untouched** — the ladder is retired from the live model but is still carried on Assumptions, which is where this floor reads it |
| ~~8~~ | ~~**Tenure rebate size**~~ | — | 🔴 **STRUCK. RETIRED by decision 44. No solve required.** See §9.3 |
| **+** | **Gold Rewards rate ceiling** *(solved but not on the brief's original list)* | Not a Phase 2 parked item; the brief carries the 36% PM-share floor instead | **1.148% of qualifying spend** = (cum interchange 13,192,568 + credit 46,347 − custody 388,102) ÷ cum card spend 1,119,222,206. **The top-tier 0.75% rate sits inside this ceiling**, so §7.2's self-funding claim holds at Base |

### 9.2 Item 1, revised — the answer is 0.696pp, not the 1.5pp headline

**v1.0 frames item 1 as its one unresolved arithmetic conflict.** v2.0 changes the framing on two independent corpus grounds.

**First, decision 44 halves the question.** Retiring the tenure rebate *"**halves the funding question: the entry-fee uplift now funds only the discount ladder.**"* v1.0's item 1 was implicitly funding two mechanisms; it now funds one.

**Second, the ladder may already be funded at the headline rate.** `_draft_ics-scoring.md` §6.1, verbatim: *"the ladder is time-phased by construction. Nobody is above Silver in Year 1, so the maximum discount outstanding at launch is 0.4pp. **The first Sovereign appears at month 60**, by which time decision 9 has bar denomination improving and cost falling toward ~3%. The ladder's cost curve and the business's cost curve are the same curve, offset the right way — so **holding the headline at 5% may fund the entire ladder with no uplift at all.**"*

**Third, and this is v2.0's own addition: the pre-gate block makes the ladder cheaper still.** The never-gated population pays the **full undiscounted fee forever** — **18.7% of the live book at Y10** — and the zero-benefit paying window runs to the **mean gate month of 8.1**, not v1.0's assumed 6. **v1.0 has no cell for either, so its estimate of the ladder's cost is too high before any uplift is even considered.**

**What the solve returns.** The book-weighted discount at the Y10 computed tier mix is **0.696pp** — not zero, but **less than half the 1.5pp headline ceiling**, because that ceiling applies only to the 4.4% of accounts at Sovereign. So the answer is neither v1.0's "the ceiling exceeds the margin" nor the hoped-for zero: **the ladder costs about 0.7pp of fee, and at the Y1 headline of 5.0% against a 4.96% minimum viable fee it is already covered.** The problem is not the ladder — it is that the fee ladder itself steps down below cost from Y3 (§8.3).

**What the model must produce:**

| Output | Value |
|---|---|
| Required uplift to the base rate, Y1 | **Zero.** The minimum viable Y1 fee is **4.96%** against the assumed 5.0% headline — a 0.04pp margin of headroom, so the ladder is funded at Y1 with no uplift |
| Required uplift, at the deepest ladder cost (first full Sovereign year, Y6) | **+0.29pp.** Y6 needs **3.79%** against v1.0's assumed 3.5% |
| **Is the answer zero at Base?** | **TRUE at Y1 and Y2 only.** The ladder self-funds at the 5% headline while the headline is 5%. It stops self-funding the moment the fee steps down: **Y3, Y4, Y6, Y7, Y8, Y9 and Y10 are all unfundable**, worst at Y10 where the fee needs 3.79% against 3.0% assumed — short by **0.79pp.** The binding constraint is the SIP lane throughout; the spot lane clears at roughly 2.87% |
| Never-gated share of stream 1 revenue | **32.7% at Y5** (3,404 of 10,411 live accounts), falling to **18.7% at Y10** as the book matures and more of it gates |
| Months of full-fee revenue per cohort before the first discount | **8.1 months to the mean gate**, against v1.0's assumed 6. The 2.1-month difference is full-fee revenue v1.0 does not book — and for the alternating misser the mean is **24.9 months** |
| **Solved uplift funding the whole ladder** | **0.696pp** — the book-weighted discount at the Y10 computed tier mix. ⚠ **This is the solver's answer and it is not zero.** It does not contradict the Y1 row above: at Y1 the 5.0% headline already covers the 4.96% minimum viable fee, so no uplift is *needed then*; 0.696pp is what the ladder costs once the mix has matured. The 1.5pp Sovereign ceiling applies to only 4.4% of accounts, which is why the book-weighted cost is less than half the headline ceiling |

### 9.3 Item 8, struck — three errors compounded

v1.0's solver item 6 (renumbered) is wrong three ways, and the third is the one that ends it:

| Element | v1.0 says | Actual |
|---|---|---|
| "Rebate room is 0.10–0.75%" | The rebate's size range | **That is the Gold Rewards range**, decision 6 — a different, card-funded benefit. Its settled ladder is now 0.15% → 0.75% |
| "~1.5%" | A rebate size | **That is the superseded, prohibited decaying redemption fee**, from a column literally headed *"Old design (prohibited)"*. It was never a rebate size |
| The mechanism | Unsized, to be solved | **Retired.** Decision 44: *"the tenure rebate is retired… its job (rewarding holding) is now structural, because holding keeps R at 1.00, which keeps the tier, which prices everything else, and every flip already pays the entry-fee toll."* `_draft_purchase-structure.md` §5.2 is dated four days earlier and is **audit trail** |

**Two build consequences of the retirement, both savings.**

- **Do not build FIFO lot accounting.** Decision 41 makes grams fungible: *"FIFO lot accounting is no longer required while the rebate is parked, since the rebate was the only thing FIFO decided. Grams are fungible for settlement. Reinstate only if the rebate returns."* **No lot-level tracking is needed anywhere in the model.** This is a real build-scope saving.
- **The freed capacity goes to item 1**, which is what §9.2 records.

**One contingency note, kept because the empty-lever decision at §16 could revive it.** If the rebate is ever reinstated it must be made **channel-agnostic and driven off lot date** (decision 41), or every gram must be tagged by channel for the life of the account — and reviving it **un-does decision 44's funding relief**, so items 1 and 8 must be decided together.

### 9.4 Solve order, and the 3/4/5 dependency loop

The seven do not solve independently. Three of them are mutually constrained and the loop has to be broken deliberately.

**The loop.** Item 2 (the acquisition budget ceiling) is a cap on the *sum* of items 3 (referral reward) and 4 (agent commission). But the ceiling itself is set as a percentage of entry-fee revenue, which depends on item 1 (the uplift) and on the volume that items 3 and 4 buy. And item 5 (the B2B rate) competes for the same board attention but not for the same budget — it is in the loop only because **v1.0's §9 lists 3, 4 and 5 as if they were independent solves and they are not.**

**Break it in this order, and the reason for each step:**

| Step | Solve | Why here | Depends on |
|---|---|---|---|
| **1** | **Item 1 — the uplift** | It is **upstream of everything**: it sets the fee, which sets stream 1 revenue, which is the base the item 2 ceiling is a percentage of. And per §9.2 the answer may be **zero**, which collapses the rest of the problem | Nothing in the solver |
| **2** | **Item 7 — the PM share floor** | Already derived at 36% and verified. **It is a constraint, not a variable**, and it must be fixed before items 3–5 because it bounds the revenue those items are spending against | Nothing in the solver |
| **3** | **Item 2 — the acquisition ceiling** | Set as a percentage of the now-fixed stream 1 revenue, using the **lagged** form (§3.x.3). Set it from the LTV:CAC target at §7.8, not from a rule of thumb | Items 1, 7 |
| **4** | **Items 3 and 4 — jointly, never separately** | 🔴 **This is where v1.0's structure fails.** The referral reward and the agent commission are **alternative uses of the same capped pound.** Solve them as an allocation problem inside the item 2 ceiling, not as two independent rates | Item 2 |
| **5** | **Item 5 — the B2B rate** | Outside the ceiling entirely, because the partner channel **costs no customer acquisition.** It is solved last because it is solved against a different constraint: the SafeGold margin precedent, not the acquisition budget | Nothing above |
| **6** | **Item 6 — the family plan price** | Solved against its own cost floor plus the screening tail, independent of everything above | Nothing above |

**How to solve step 4, stated concretely.** Compute LTV:CAC by channel at §7.8 under a grid of `(referral_reward, agent_commission)` pairs summing to the item 2 ceiling. **The optimum is the pair that maximises accounts acquired subject to every channel's LTV:CAC remaining above 1.0 at the Base rail.** Report the frontier, not a point: **the solve returns a corner, not an interior optimum.** The agent commission lands at **USD 175.68/account** (46.85 / 58.56 / 70.27 across three levels) out of an acquisition pool of USD 5,075,076 over 28,889 agent-sourced accounts, while the referral reward is **unconstrained by LTV — affordable at up to 399% of the referee's entry fee against F17's 30% placeholder.** 🔴 **So the two do not trade off against each other the way this step assumes: the referral reward is cheap enough that the ceiling binds almost entirely on agent commission.** `{{UNFILLED: the full (referral_reward, agent_commission) frontier at the Base and Conservative rails — not in spine; the model solves each at its own constraint rather than sweeping the pair}}`. ⚠ **Report the same frontier at the Conservative rail**, because that is where the agent channel may fail the constraint entirely.

**One check on the whole solve.** Items 3 and 4 together must satisfy `total_acquisition_cost(t) ≤ ceiling% × stream1_revenue(t−1)` in **every** period, not on average. The Checks sheet must verify the ceiling is never breached — a solved-on-average ceiling breaches in the ramp months, which is exactly when cash is tightest.

---

## 10. Calculation reference

### 10.1 Row map for the new structure

**The row map shrinks substantially at v2.1** (D21, D22, D23). v2.0 specified a Cohort Engine of ~320 rows and an ICS Engine of ~340, both replicated across 76 columns. **The convolution removes the first, the collapse removes most of the second, and the horizon removes 47 columns.** The Model sheet drops from ~520 rows × 76 columns to **~200 rows × 29 columns**.

Column layout is common to the Time Series, Acquisition and Model sheets (**including Model's opex and P&L band**, D26):

```
Col A: Row label      Col B: Unit      Col C: Source/note
Col D–AA  (24 cols):  M1 … M24   (monthly)
Col AB–AF ( 5 cols):  Y3 … Y7    (annual)
                      ─────────────────────
                      29 data columns
```

⚠ **The Lifecycle Curves sheet does NOT use this layout.** It is indexed by **month-since-origination, not by period**, and it runs `m = 1..84`. **Nothing on it has a calendar date.** Confusing the two indices is the most likely way to build the convolution backwards.

**Sheet 5 — Lifecycle Curves** *(new at v2.1; the only monthly-to-M84 sheet)*

```
Col A: Series label   Col B: Archetype   Col C: Unit / note
Col D–CG  (84 cols):  m = 1 … 84   (months since origination)
```

| Band | Rows | Contents |
|---|---|---|
| Headers | 1–3 | `m` index, gate-window marker, notes. **No calendar dates** |
| Gate solve | 5–14 | Per archetype: run-of-6 first-passage `gated(a,m)`, `never_gated(a,m)`. **The live engine — computed, never assumed** (D22) |
| Survival | 16–25 | Per archetype: `alive(a,m)` from the archetype hazard plus background hazard |
| Payment states | 27–41 | Per archetype: `contributing(a,m)`, `reduced(a,m)`, `holding_not_contributing(a,m)` |
| **Tenure→tier lookup** | 43–57 | Per archetype: `tier(a,m)` — Silver / Gold at gate+12 / Platinum at gate+36 / No tier. **A lookup, not an arithmetic chain** (D22) |
| Stock and card | 59–78 | Per archetype: `grams(a,m)` net of S31/S32/S33; `card_active(a,m)`; `spend(a,m)` before the segment multiplier |
| Heavy-seller haircut | 80–84 | The single multiplier replacing the per-account `Sold` ratio (D22) |
| Curve integrity | 86–92 | Per archetype, per `m`: states sum to 1.000; `alive` monotone non-increasing; `tier` monotone non-decreasing. **Feeds Checks** |

**Sheet 6 — Acquisition**

| Band | Rows | Contents |
|---|---|---|
| Headers | 1–4 | Period number, label, type (Monthly/Annual), calendar month index for seasonality |
| Channel volume | 6–29 | Active agents, recruits (S18 gross-up), ramp factor (S17), agent output; qualified referrers, referral output (S19, S20); marketing spend, effective CAC (S25 curve), paid output, organic (S26); partner count (S42) |
| Channel→segment | 31–52 | S16 matrix by phase; raw demand by segment |
| Saturation | 54–64 | Cumulative-ever-acquired by segment; headroom `base(s) × S22`; logistic factor (S23); **T10 cumulative-to-live ratio, reported** |
| **The acquisition vector** | 66–74 | `acq(s,t)` — seasonalised new accounts by segment (× S52a), **with the S4 (M13) / S5 (switch) / S6 (M25) activation offsets written as leading zeros in the vector, not as separate curves** (D23) |
| Conservation | 76–80 | Cumulative-ever-acquired ties to the running sum of `acq(s,t)`. **Feeds Checks** |

**Sheet 7 — ICS Validation** *(demoted from Engine — a leaf, read by Checks only)*

| Band | Rows | Contents |
|---|---|---|
| Headers | 1–3 | |
| **Full ICS formula** | 5–34 | Per archetype, on the M84 index: `Months`, `Recent`, `Sold`, `Record`, `Standing`, `Retention`, `ICS`. **Exact fractions `100/12` and `100/24`, never `8.3333`** (D4) |
| Tier from full ICS | 36–45 | Threshold per archetype, then weight — the D2 rule, run on the full formula |
| **Collapse delta** | 47–58 | Per year Y1–Y7: stream 2 on the lookup, stream 2 on the full formula, `ABS(delta) ÷ gross_profit`. **The 5% safety gate** (§3 Layer 5d) |
| **Persona validation** | 60–76 | The nine hard-coded persona paths A–I, returning Record/Standing/Retention/ICS/Tier. **Pass/fail, not a chart.** H and I are the two a naive build fails |

🔴 **Nothing on this sheet may be referenced by the Model sheet.** It is a leaf (§3.x.1). If a Model formula ever points here, the collapse has been silently un-done.

**Sheet 8 — Model** *(~200 rows × 29 columns)*

| Band | Rows | Contents |
|---|---|---|
| Headers | 1–4 | Period number, label, type (Monthly/Annual), calendar month index |
| **The convolution** | 6–29 | One `SUMPRODUCT` row per series per segment-group: live, contributing, reduced, gated, holding-not-contributing, never-gated, tier shares, grams, active cards, spend. **This band replaces v2.0's 320-row Cohort Engine and 310 rows of ICS Engine** (D23). Formula pattern and worked example at §10.4 Pattern 1 |
| Fee and discount | 31–44 | Base fee (T1), tier-weighted discount by segment off the convolved tier shares, **zero for pre-gate and never-gated**, `fee_applied` |
| Stream 1a — SIP | 46–66 | Reduced ticket (S29), gross inflow, net of fee, COGS, gross margin, price-gap × float_mode, float CoC × float_mode, rail events, rail cost, **STREAM 1a** |
| Stream 1b — Spot | 68–82 | Attach, tenure uplift, events, seasonality, ticket by segment, inflow, margin, rail, **STREAM 1b**, float-invariant breach counter |
| AUM stock | 84–100 | Grams bought SIP, bought spot, rewards credited, self-custody out (S31 buckets), redemption out (S32 × S33), **net flow**, closing grams, AUM USD, custody cost |
| Stream 2 — Interchange | 102–128 | Eligible (Gold+, from the convolved `gated` × `tier`), active cards (S5), spend (S4 × S38 × S52b), gross interchange **at the flat Gold rate** (D22), txn count (F23, +6%), per-txn fee (F24), **effective PM share — report it**, fraud (S39), disputes (F25), fixed (F27), Gold Rewards cap and haircut, **STREAM 2** |
| Stream 3 — Family/Will | 130–140 | Plans, names, tier-discounted price, new + renewal revenue, **STREAM 3**; onboarding, screening, platform floor (F16) |
| Stream 4 — Cardholder fees | 142–156 | Foreign share (S53 vector), foreign spend, FX, **ATM over the S35 distribution by bucket**, issuance/replacement events and fees, production cost (F26), **STREAM 4** |
| Stream 5 — Credit | 158–174 | Eligible collateral, facility limit, borrowers (S8), peak drawn (S9), **× S40 = average drawn**, **vintage rows by struck LTV**, draw events (S41), interest share, origination, servicing, penal, recovery = 0, **STREAM 5**. **Zero through M24; first non-zero column is Y3** |
| Stream 6 — B2B | 176–186 | Per-partner maturity, ramp (S43), terminal (S44), **india_factor**, partner AUM, **STREAM 6**. **Zero through M24; first non-zero column is Y3 — no stub month** (§4) |
| Stream 0 — Redemption | 188–194 | Redemption grams, events, F20 handling, net-flow spread cost, **STREAM 0** |
| Benefit costs | 196–204 | Entry discount value, Gold Rewards value and cap, will discount value; **total contra-revenue** |
| Revenue summary | 206–216 | All streams, total revenue, mix %, period-over-period growth |

⚠ **Rows 102–128 must be physically ordered gross interchange → Gold Rewards cap → net interchange**, per §3.x.2. The ordering is the resolution of the apparent circularity.

🆕 **Model sheet, band 2 — opex and P&L** (D26 folds the former sheet 9 into Model). ⚠ **The row numbers below are band-local and must be offset by the end of the revenue band when built.** Keep the band order and the internal spacing exactly as listed; only the origin moves.

| Band | Rows | Contents |
|---|---|---|
| Opex blocks | 6–60 | Eleven blocks, step vs scale, log-linear interpolation (F32), booked in the stated month |
| Acquisition cost | 62–80 | Agent commission, recruitment, referral (6-month lag), marketing; **ceiling test on `t−1` revenue** |
| P&L | 82–100 | Revenue, COGS, benefit costs, stream 0, acquisition, opex, **EBITDA** |
| Tax | 102–112 | Accounting profit, loss pool, `loss_bf_utilised` (75% cap), taxable income, **tax booked in the FY-end month only** |
| Working capital | 114–126 | Float grams (F38), float capital (T9), **Δ float**, one-off spend |
| Cash | 128–140 | Free cash, cumulative, **peak funding, month of peak, cash break-even** |
| Capital memo | 142–150 | AED 1.5m, `OPTION_B` escalator, opportunity cost memo line |

### 10.2 The lifecycle curves worked, months 1–13

**Setup.** A notional **1,000 accounts at origination**, Base archetype mix (S27), traced by month-since-origination. ⚠ **Read this as a derivation of the curve, not as a cohort block.** The live model computes this once, to M84, on the Lifecycle Curves sheet, and then convolves it against the acquisition vector (D23). **The workbook does not contain 72 of these.** Segment S3's USD 20 ticket is used where a ticket is needed, but the population arithmetic is segment-independent — segments scale the curve, they do not have their own (§3 Layer 2c).

**Step 1 — split the origination population into archetype curves.**

| Track | Weight | Accounts at M1 | Monthly pay prob. | Total monthly attrition |
|---|---|---|---|---|
| Perfect | 10% | 100 | 0.995 | 0.016 |
| Occasional | 35% | 350 | 0.93 | 0.023 |
| Alternating | 12% | 120 | 0.55 | 0.034 |
| Reducer | 13% | 130 | 0.97 | 0.018 |
| Early lapser | 30% | 300 | 0.60 falling | 0.216 |
| **Total** | 100% | **1,000** | | |

**Step 2 — roll each track forward.** Survival per track is `S(a, t) = (1 − total_attrition(a))^(t−1)`, with the early lapser's own hazard declining after M13 as its population exhausts.

```
survivors(a, t) = accounts(a, M1) × (1 − h_total(a))^(t−1)
```

| Month | Perfect | Occasional | Alternating | Reducer | Early lapser | **Total live** | **% of M1** |
|---|---|---|---|---|---|---|---|
| M1 | 100.0 | 350.0 | 120.0 | 130.0 | 300.0 | **1,000.0** | 100.0% |
| M2 | 98.4 | 341.9 | 115.9 | 127.7 | 235.2 | **919.1** | 91.9% |
| M3 | 96.8 | 334.1 | 111.9 | 125.4 | 184.4 | **852.6** | 85.3% |
| M4 | 95.3 | 326.4 | 108.1 | 123.1 | 144.6 | **797.5** | 79.7% |
| M5 | 93.8 | 318.9 | 104.4 | 120.9 | 113.3 | **751.3** | 75.1% |
| M6 | 92.3 | 311.5 | 100.8 | 118.7 | 88.9 | **712.2** | 71.2% |
| M7 | 90.8 | 304.4 | 97.4 | 116.6 | 69.7 | **678.9** | 67.9% |
| M8 | 89.4 | 297.4 | 94.1 | 114.5 | 54.6 | **650.0** | 65.0% |
| M9 | 88.0 | 290.5 | 90.9 | 112.4 | 42.8 | **624.6** | 62.5% |
| M10 | 86.6 | 283.8 | 87.8 | 110.4 | 33.6 | **602.2** | 60.2% |
| M11 | 85.2 | 277.3 | 84.8 | 108.4 | 26.3 | **582.0** | 58.2% |
| M12 | 83.8 | 270.9 | 81.9 | 106.5 | 20.6 | **563.7** | 56.4% |
| **M13** | **82.5** | **264.7** | **79.1** | **104.6** | **16.2** | **547.1** | **54.7%** |

✅ **M13 lands at 54.7% against the §0.5 target of 55%.** Error 0.3pp. **The curve is not fitted; it emerges from the mix.**

**Step 3 — the reduction diversion (S28).** In each period, 33% of would-be lapse events **among the occasional-misser and reducer tracks only** divert to REDUCED instead of leaving. Diverted accounts then carry hazard × S30 = 1.35×.

```
would_be_lapse(occasional, M2) = 350.0 × 0.023 = 8.05
diverted(M2)                   = 8.05 × 0.33   = 2.66  →  REDUCED
actual_lapse(M2)               = 8.05 − 2.66   = 5.39  →  STOPPED
```

⚠ **Never apply S28 to the early lapser or to the background hazard.** The early lapser is not leaving for affordability reasons, and the background hazard is by construction voluntary exit unrelated to payment ability. **Applying S28 to them makes REDUCED a free retention machine and overstates persistency.**

**Step 4 — split lapses into voluntary and involuntary.** 30% involuntary (`_draft_sip-rulebook.md` §7.3), which carries a restart probability back to CONTRIBUTING at the decayed score; 70% voluntary, which does not.

```
involuntary(M2) = 5.39 × 0.30 = 1.62   → STOPPED, restart-eligible
voluntary(M2)   = 5.39 × 0.70 = 3.77   → STOPPED, no restart
```

**Step 5 — the 12-period absorbing boundary.** Any account in STOPPED for 12 consecutive silent periods transitions to DORMANT. **First DORMANT arrivals from this cohort appear in M14** (M2's stops, twelve silent periods later). **No account may sit in a silent state beyond 12 periods.**

**Step 6 — contribution flow.** Only CONTRIBUTING and REDUCED pay.

```
M6:  contributing = 712.2 − reduced_stock(M6)
     reduced_stock(M6) ≈ 12.4   [cumulative diversions, decayed at 1.35× hazard]
     contributing(M6)  ≈ 699.8

     reduced_ticket(S3) = MAX(20, 0.50 × 20) = 20        [at the floor]
     sip_inflow(S3, M6) = 699.8 × 20 + 12.4 × 20 = USD 14,244
     rail_events(M6)    = 699.8 + 12.4 = 712.2
     rail_cost(M6)      = 712.2 × 0.25 = USD 178.05
```

**Step 7 — the populations that pay nothing and cost something.** By M13, **452.9 of the original 1,000 are no longer contributing** — and under the six-state machine **every one of them still holds gold.**

| Population at M13 | Accounts | In AUM? | In custody cost? | In screening? | Contributes? |
|---|---|---|---|---|---|
| CONTRIBUTING + REDUCED | 547.1 | Yes | Yes | Yes | **Yes** |
| STOPPED + DORMANT (holding, not contributing) | ~452.9 | **Yes** | **Yes** | **Yes** | No |
| CLOSED (grams = 0) | ~0 at M13 | No | No | No | No |

**This is D1 in one table.** v1.0's LAPSED state drops all 452.9 out of AUM, custody, screening and the collateral base. **By M25 — the first period of the annual block — the same table already reads roughly 400 contributing against 600 holding-not-contributing, and v1.0 models the 400.** The gap widens with tenure and reaches roughly 183 against 817 at M61.

### 10.3 ICS engine worked, at M1 / M6 / M12 / M36 / M60 / M61, including pre-gate

**The perfect payer track** (`p = 0.995`), which is the only track that can reach Sovereign.

| Period | `run_length` | Gated? | `Months` | `Recent` | `Record` | `Standing` | `Sold` | `Retention` | **ICS** | **Tier** |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 1 | No | — | — | — | — | — | — | **none** | **No tier** |
| M5 | 5 | No | — | — | — | — | — | — | **none** | **No tier** |
| **M6** | **6** | **Yes** | **6** | **6** | 25.00 | 50.00 | 0 | 1.000 | **25.00** | **Silver** |
| M12 | — | — | 12 | 12 | 50.00 | 100.00 | 0 | 1.000 | **50.00** | **Gold** |
| M36 | — | — | 36 | 12 | 75.00 | 100.00 | 0 | 1.000 | **75.00** | **Platinum** |
| M60 | — | — | 60 | 12 | 100.00 | 100.00 | 0 | 1.000 | **100.00** | **Sovereign** |
| M61 | — | — | 61 | 12 | 100.00 | 100.00 | 0 | 1.000 | **100.00** | **Sovereign** |

**The arithmetic, shown so it can be checked:**

```
M6:   Record   = (100/24) × 6  = 25.00        [Months ≤ 12 branch]
      Standing = (100/12) × 6  = 50.00
      ICS      = MAX(25, MIN(25.00, 50.00) × 1.000) = 25.00   → Silver ✅

M12:  Record   = (100/24) × 12 = 50.00
      Standing = (100/12) × 12 = 100.00
      ICS      = MAX(25, MIN(50.00, 100.00) × 1.000) = 50.00  → Gold ✅

M36:  Record   = 50 + (100/96) × (36 − 12) = 50 + 25.00 = 75.00
      Standing = 100.00
      ICS      = MIN(75.00, 100.00) = 75.00                   → Platinum ✅

M60:  Record   = 50 + (100/96) × 48 = 50 + 50.00 = 100.00
      ICS      = 100.00                                        → Sovereign ✅
```

✅ **Ladder arrival reproduces the corpus exactly: Silver M6, Gold M12, Platinum M36, Sovereign M60.** `Record` binds at every step and `Standing` never does — which is the property `_draft_ics-scoring.md` §7.4 proves must hold for a clean saver, and the model reproduces it rather than assuming it.

⚠ **The exact-fraction test, and it is why §3 insists on it.** At `Standing = 8.3333 × 6 = 49.9998` the M12 ICS would be `MIN(50.00, 49.9998) = 49.9998`, which is **below the Gold threshold of 50.** The account files as Silver. **Write `100/12`.**

**The alternating misser track** (`p = 0.55`, pay-miss-pay-miss), which is the cell v1.0 has nowhere to put.

| Period | `run_length` | Gated? | `Months` | `Recent` | `Record` | `Standing` | **ICS** | **Tier** |
|---|---|---|---|---|---|---|---|---|
| M1–M11 | 1, 0, 1, 0, … | **No** | — | — | — | — | **none** | **No tier** |
| M12–M23 (first six-in-a-row, whenever it lands) | 6 | Yes | 6 | 6 | 25.00 | 50.00 | **25.00** | **Silver** |
| +12 months | — | — | 18 | **6** | 66.25 | **50.00** | **50.00** | **Gold** |
| +36 months | — | — | 42 | **6** | 81.25 | **50.00** | **50.00** | **Gold** |
| +60 months | — | — | 66 | **6** | 100.00 | **50.00** | **50.00** | **Gold** |
| **M120** | — | — | 120 | **6** | 100.00 | **50.00** | **50.00** | **Gold — forever** |

**`Recent` holds at 6 forever, so `Standing` holds at 50.00 forever, so `MIN(Record, Standing)` is pinned at 50.00 from the moment `Record` passes it. The alternating misser is capped at Gold for life, and no amount of tenure moves them.**

**Why this cell is worth money, and it is counter-intuitive.** At 12% of the book it is roughly a quarter of the steady-state Gold population — **spending at the lowest interchange rate (1.80%) and the highest FX margin (2.0%) and the lowest ATM allowance (AED 1,000).** It is **the most profitable card cell in the book, because it generates stream 4 revenue that the higher tiers have waived.**

⚠ **This is the cell Jensen's inequality destroys.** Averaged into a cohort with perfect payers, `mean(Recent) = 9` → `Standing = 75` → the whole cohort files as Platinum, the alternating misser's stream 4 revenue is waived away, and the highest-margin card cell in the model vanishes into an average.

**Pre-gate, worked for two corpus personas the naive build fails.**

**Persona I — the late opener.** Paid months 1–3, missed 4, paid 5–7, missed 8, ran 9–14.

| Month | Payment | `run_length` | Note |
|---|---|---|---|
| 1, 2, 3 | ✓ ✓ ✓ | 1, 2, 3 | Building |
| 4 | ✗ | **0** | **Reset. Not decremented — reset** |
| 5, 6, 7 | ✓ ✓ ✓ | 1, 2, 3 | Rebuilding from zero |
| 8 | ✗ | **0** | Reset again |
| 9–14 | ✓ × 6 | 1, 2, 3, 4, 5, **6** | **GATE FIRES at M14** |
| **M14** | | | `Months := 6`, `Recent := 6`, `Record = 25.00`, `Standing = 50.00`, **ICS = 25 → Silver** |

✅ **Nine paid months across fourteen calendar months, and the door opens on Silver at exactly 25 — the same place a flawless month-6 saver opens.** *"The six pre-run payments bought gold and bought no score."*

**Persona H — the scattered payer.** Six real payments over three years, never six in a row.

| Month | Cumulative payments | `run_length` (max reached) | ICS | Tier |
|---|---|---|---|---|
| M12 | 2 | 2 | **none** | **No tier** |
| M24 | 4 | 3 | **none** | **No tier** |
| M36 | 6 | 3 | **none** | **No tier** |
| M120 | 6 | 3 | **none** | **No tier — forever** |

✅ **Six real payments, three years of intermittent saving, and the account has no score and no tier because no six landed in a row.** *"H is the cost of the consecutive gate, and it is the row to be honest about."*

**And here is the revenue consequence v1.0 cannot see.** Persona H **pays the full undiscounted entry fee on every one of those six payments, holds the gold forever, generates AUM and custody cost forever, and consumes zero benefits forever.** **18.7% of the live book at Y10 — 4,047 accounts** — behaves this way, and they contribute the same **18.7%** of stream 1 inflow. **Structurally these are the highest-margin retail accounts Aurumix has.**

⚠ **Two different never-gated numbers exist and they answer different questions.** **46.5%** of all accounts ever acquired never gate — but most of that number is early lapsers who left before they could complete a run, and they are not on the book to earn margin. **18.7%** is the share of the *live* book that is never-gated at Y10, and that is the figure the margin argument needs. Use 46.5% only when describing the gate's selectivity, never when sizing revenue.

**The Retention personas, worked, because they set the S31 bucket boundaries.**

| Persona | `Months` | `Recent` | `Sold` | `Record` | `Standing` | `Retention` | **ICS** | **Tier** |
|---|---|---|---|---|---|---|---|---|
| **D.** Cycler: contributes and redeems every month | 60 | 12 | ~100% | 100 | 100 | **0** | 0 → floor **25** | Silver |
| **E.** Withdrew half at M36, kept saving | 36 | 12 | 50% | 75 | 100 | **0.714** | **53.6** | Gold |
| **F.** Withdrew everything at M36, kept saving | 36 | 12 | 100% | 75 | 100 | **0** | 0 → floor **25** | Silver |
| **G.** Withdrew 30% at M36 — **inside the allowance** | 36 | 12 | 30% | 75 | 100 | **1.000** | **75** | **Platinum, no change** |

```
E:  Retention = 1 − (0.50 − 0.30) ÷ 0.70 = 1 − 0.2857 = 0.7143
    ICS       = MIN(75, 100) × 0.7143 = 53.57   → Gold ✅
G:  Sold = 30% is AT the allowance, not past it → Retention = 1.000 exactly
    ICS  = 75.00 → Platinum, unchanged ✅
```

**G is the row that proves the S31 finding.** At exactly 30% the multiplier is **1.000, not 0.9998** — the hard allowance was chosen precisely so a Sovereign, who has no buffer because Record and Standing both cap at 100, does not lose the top tier on a 21% withdrawal. **And it is why only 14% of the base takes any Retention haircut at Base: the kink is set generously.**

**Persona validation is a pass/fail test set, not a chart.** All nine rows A–I are hard-coded input paths on the **ICS Validation** sheet, and **the full ICS formula must return the stated Record, Standing, Retention, ICS and Tier for every one.** H and I are the two that fail a naive build, which is exactly why they are the valuable rows. 🔴 **Demoting the score machinery to a validation artefact does not weaken this test — it is the reason the test exists.** The collapsed lookup is proved against a formula that itself has to pass nine independent corpus checks, so an error in the formula corrupts the proof rather than the answer, which is worse and harder to see (§3 Layer 5d).

⚠ **`_draft_ics-scoring.md` §7.1's heading reads "Six personas" and its table has nine rows, A–I.** The heading is stale — correction 20 at §15.

### 10.4 Formula patterns, with evaluated examples

**Pattern 1 — The convolution (this is the population engine, D23)**

**On the Model sheet, one row per series per segment-group.** The acquisition vector runs left to right across the period columns; the lifecycle curve runs left to right across `m = 1..84` on its own sheet. **The convolution reads the acquisition range forwards and the curve range backwards**, so that the oldest cohort meets the largest month-since-origination.

```
book(s, X, t) = Σ_a  weight(a)
                     × SUMPRODUCT( acq(s, 1..t) , curve_a(X, t..1) )
                     × segment_scalar(s, X)
```

**In Excel, for series `X`, segment `s`, at period column `t`:**

```
=SUMPRODUCT( Acquisition!$D5:INDEX(Acquisition!5:5, COLUMN()) ,
             INDEX('Lifecycle Curves'!$D12:$CG12, 1, COLUMN()-3) : 'Lifecycle Curves'!$D12 )
     × S27_weight_a
     × segment_scalar
```

⚠ **The reversal is the whole formula and it is the thing that gets built wrong.** The acquisition range is anchored at its first column and extends to the current one. The curve range is anchored at its *first* column too, but written so the range runs from the current offset **back** to it. `SUMPRODUCT` pairs element 1 of the first range with element 1 of the second, so anchoring both at column D and letting the curve range run backwards pairs `acq(1)` with `curve(t)` — **the M1 cohort at `t` months of age, which is correct.** Building both ranges forwards pairs `acq(1)` with `curve(1)`, which ages every cohort by one month regardless of when it was acquired. **The model still runs, the totals still look plausible, and every ladder date is wrong.** Check formula at §10.6, check 14.

**Evaluated, `contributing`, one segment, at M4.** Acquisition 100 / 120 / 140 / 160 accounts in M1–M4. Base archetype mix, so the weighted `contributing(m)` curve reads 1.000 / 0.919 / 0.853 / 0.797 at `m` = 1 / 2 / 3 / 4 (the §10.2 total-live column, which at these months is all contributing):

```
Pair the M1 cohort with m=4, the M2 cohort with m=3, and so on:

  acq(M1) = 100  ×  curve(m=4) = 0.797   =  79.7
  acq(M2) = 120  ×  curve(m=3) = 0.853   = 102.4
  acq(M3) = 140  ×  curve(m=2) = 0.919   = 128.7
  acq(M4) = 160  ×  curve(m=1) = 1.000   = 160.0
                                          ───────
  SUMPRODUCT                              = 470.8  contributing at M4
```

**The wrong pairing, shown so it can be recognised:**
```
  100 × 1.000 + 120 × 0.919 + 140 × 0.853 + 160 × 0.797  =  457.4
```
**13.4 accounts apart at M4 and diverging** — and the error is entirely in *which cohort is how old*, so it corrupts the gate distribution, every ladder date and the tier mix, not merely the headcount. **A 3% headcount gap is what this failure looks like from the outside. That is why it needs a check rather than an eyeball.**

**At an annual column**, perform the convolution **at each of the twelve constituent months against the M84 curve, then aggregate** — flows sum, stocks average opening and closing. ⚠ **Never convolve an annual acquisition figure against an annual curve point** (§3.x.3, fourth candidate). That collapses twelve first-passage months into one and destroys the gate distribution, which is the first-order term.

**Pattern 1a — The six-state roll-forward that produces the curve (monthly, on the Lifecycle Curves sheet only)**

**This is how a curve is *derived*. It runs once per archetype across `m = 1..84`, not once per cohort.**

```
PRE_GATE(a,m)        = PRE_GATE(m−1) + new(m) − gated(m) − lapsed_pregate(m)
CONTRIBUTING(t)      = CONTRIBUTING(t−1) + gated(t) + restarts(t)
                       − diverted_to_reduced(t) − lapsed(t) − blocked(t)
REDUCED(t)           = REDUCED(t−1) + diverted_to_reduced(t)
                       − REDUCED(t−1) × h_total(a) × S30
REG_BLOCK(t)         = REG_BLOCK(t−1) + blocked(t) − unblocked(t)
STOPPED(t)           = STOPPED(t−1) + lapsed(t) + lapsed_pregate(t)
                       − restarts(t) − to_dormant(t)
DORMANT(t)           = DORMANT(t−1) + to_dormant(t) − restarts_from_dormant(t)
CLOSED(t)            = CLOSED(t−1) + closures(t)      [grams reach zero]

to_dormant(t)        = accounts entering STOPPED in period (t−12)
                       that have not restarted        [HARD BOUNDARY]

CONSERVATION (Checks): PRE_GATE + CONTRIBUTING + REDUCED + REG_BLOCK
                     + STOPPED + DORMANT + CLOSED = 1.000, at every m
                     [a share of origination, not a headcount — the curve is
                      normalised, and the headcount arrives at the convolution]
```

**Evaluated, occasional-misser curve, m = 2** (shown on a notional 350 at origination so it reads against §10.2):
```
CONTRIBUTING(m=1) = 350.0
h_total          = 0.023
would_be_lapse   = 350.0 × 0.023            = 8.05
diverted         = 8.05 × 0.33 (S28)        = 2.66  → REDUCED
lapsed           = 8.05 − 2.66              = 5.39  → STOPPED
  of which involuntary = 5.39 × 0.30        = 1.62  (restart-eligible)
CONTRIBUTING(m=2) = 350.0 − 2.66 − 5.39     = 341.95
REDUCED(m=2)      = 0 + 2.66                = 2.66
Check: 341.95 + 2.66 + 5.39 = 350.00 ✅
```

**Pattern 2 — Pre-gate run counter (on the curve, indexed by m — the live engine, D22)**

```
run_length(m) = IF( frozen(m),         run_length(m−1),
                IF( paid(m),           MIN(6, run_length(m−1) + 1),
                                       0 ) )
gated(a,m)    = share of archetype a reaching run_length = 6 at month m
                [a run-of-6 first-passage problem in p(a)]
```

🔴 **This pattern is not collapsed and must not be.** It is the first-order term: the cohort-weighted mean gate is M8.1 and the ever-gate share 53.5%, against a naive assumption of universal gating at M6 that overstates the business by ~59% (§3 Layer 5b).

⚠ **Note `0`, not `run_length(t−1) − 1`. A miss resets the run; it does not decrement it.** And `frozen` **holds** the counter — it does not reset it. *"A saver at 4-of-6 who enters a compliance pause resumes at 4-of-6."*

**Pattern 3 — The tenure→tier lookup (on the curve, indexed by m — this is what the live model runs, D22)**

```
months_since_gate(a,m) = MAX(0, m - gate_month(a))

tier(a,m)  = IF( NOT gated(a,m),                 "No tier",
             IF( months_since_gate(a,m) >= 36,   "Platinum",
             IF( months_since_gate(a,m) >= 12,   "Gold",
                                                 "Silver" ) ) )

  capped archetypes override:  the alternating misser returns "Gold" from
  gate+12 and NEVER advances, because its Recent pins at 6 forever.
  The cap is a property of the archetype's own curve, never of a blend.
```

**Evaluated, perfect payer, gate at m = 6, read at m = 42:** `months_since_gate = 36` → **Platinum.** ✅
**Evaluated, alternating misser, gate at m = 25, read at m = 84:** `months_since_gate = 59`, which would return Platinum on the generic ladder — **the archetype cap overrides it to Gold.** ✅ **This override is the D2 rule surviving the collapse; without it the mix drifts upward** (§3 Layer 5c).

**Pattern 3v — Record, Standing, Retention, ICS (ICS VALIDATION SHEET ONLY, D22)**

⚠ **This pattern no longer runs in the live model. It runs on the validation sheet, and the collapsed Pattern 3 is proved against it.**

```
Record(m)    = IF( Months(m) <= 12, (100/24) * Months(m),
               IF( Months(m) <= 60, 50 + (100/96) * (Months(m) - 12),
                                    100 ) )
Standing(m)  = (100/12) * Recent(m)
Sold(m)      = 1 - grams_now(m) / ( grams_12_countable_ago(m)
                                  + grams_acquired_since(m) )
Retention(m) = IF( Sold(m) <= 0.30, 1, 1 - (Sold(m) - 0.30) / 0.70 )
ICS(m)       = MAX( 25, MIN(Record(m), Standing(m)) * Retention(m) )
Tier(m)      = LOOKUP( ICS(m), {0, 25, 50, 75, 100},
                       {"No tier","Silver","Gold","Platinum","Sovereign"} )
```

**Evaluated, perfect payer at m = 36:** `Record = 50 + (100/96) × 24 = 75.00`; `Standing = (100/12) × 12 = 100.00`; `ICS = MAX(25, MIN(75, 100) × 1) = 75.00` → **Platinum.** ✅ **Which is what Pattern 3 returns at the same point, and that agreement is the collapse being proved rather than assumed.**

**Pattern 3g — The 5% collapse-safety gate (annual, on the ICS Validation sheet)**

```
delta(y) = ABS( stream2_lookup(y) - stream2_full_ICS(y) ) / gross_profit(y)

GATE     = MAX over y in Y1..Y7 of delta(y)  <=  0.05
```

🔴 **FALSE reverts the collapse.** Measured headroom: 3.1% of gross profit at Y10, ~2% at Y7, against a 5% tolerance. **Run under Base, Aggressive and Conservative** — an Aggressive archetype mix enriches the top of the tier ladder and is the most likely to trip it.

**Pattern 4 — Threshold then weight (the D2 correction, and it survives the collapse)**

```
WRONG  (v1.0):  Tier = LOOKUP( MIN( AVG(Record), AVG(Standing) ) × AVG(Retention) )
RIGHT  (v2.1):  share(tier k, t) = Σ_a [ weight(a)
                                        × convolved( IF(tier(a,m) = k, 1, 0), t ) ]
```

⚠ **The collapse changes what is inside the `IF`, never the order of operations.** Pattern 3 is applied **per archetype curve**, and only then weighted and convolved. **A single blended tenure→tier table across archetypes would be the D2 error in a new costume** (§3 Layer 5a).

**Evaluated, the two-track worked example:**
```
Cohort: 50% perfect (Recent = 12), 50% alternating (Recent = 6)

WRONG:  AVG(Recent) = 9 → Standing = (100/12)×9 = 75 → 100% PLATINUM
RIGHT:  perfect     → Standing = 100 → ICS = MIN(Record,100) → PLATINUM  (50%)
        alternating → Standing = 50  → ICS = 50            → GOLD       (50%)
        Result: 50% Platinum, 50% Gold-capped-for-life ✅
```

**The difference is not a rounding artefact. It is an entire tier for half the cohort, and it is biased upward every time.**

**Pattern 5 — Effective PM share (monthly, on the flat Gold rate — D22)**

```
gross_ic(t)  = spend(t) × F12_gold ÷ 3.6725       [FLAT GOLD RATE, ladder collapsed]
txns(t)      = spend(t) ÷ F23 × 1.06
net_ic(t)    = gross_ic(t) × S3 − txns(t) × F24
eff_PM(t)    = net_ic(t) ÷ gross_ic(t)            [REPORT THIS ROW]
```

⚠ **`F12` is now a scalar, not a per-tier vector.** The 1.80 / 2.05 / 2.10 ladder is retired from the live model and its cost is measured at 3.1% of gross profit at Y10, ~2% at Y7 (§3 Layer 5). **It remains in the Assumptions register as an input, because the ICS Validation sheet reads it to compute the 5% gate.**

**Evaluated, Gold tier, AED 6,000 spend at S38 = 0.82, Conservative PM share:**
```
spend      = 6,000 × 0.82                       = AED 4,920
gross_ic   = 4,920 × 1.80% ÷ 3.6725             = USD 24.11
txns       = 4,920 ÷ 185 × 1.06                 = 28.19
txn_fee    = 28.19 × 0.10                       = USD 2.82
net_ic     = 24.11 × 0.55 − 2.82                = USD 10.44
eff_PM     = 10.44 ÷ 24.11                      = 43.3%
```
**Against a contracted 55%. The effective share is 11.7pp below the headline, on the tier that carries the most cardholders.**

**Pattern 6 — Peak-to-average drawn (monthly)**

```
peak_drawn(t,k)  = eligible_collateral(t,k) × F1 × F11(k) × S8 × S9
avg_drawn(t,k)   = peak_drawn(t,k) × S40
```

**Evaluated, Gold tier, USD 1,000,000 of eligible collateral:**
```
facility_limit = 1,000,000 × 0.50                = USD 500,000
peak_drawn     = 500,000 × 0.18 × 0.50           = USD 45,000
avg_drawn      = 45,000 × 0.42                   = USD 18,900
interest share at 4pp = 18,900 × 0.04            = USD 756/yr
  [v1.0 would have booked 45,000 × 0.04 = USD 1,800/yr — 2.4× too high]
origination: draw_events = borrowers × S41, PER EVENT, NOT scaled by S40
```

**Pattern 7 — ATM over-allowance across the distribution (monthly, per tier)**

```
atm_rev(t,k) = active_cards(t,k)
             × Σ_bucket [ w(bucket) × MAX(0, mid(bucket) − allowance(k)) × 0.02 ]
```

**Evaluated, Gold (allowance AED 1,000), 1,000 active cards:**
```
bucket 0–500      w=0.60  mid=250    MAX(0, 250−1000)   = 0        → 0
bucket 500–1,500  w=0.25  mid=1,000  MAX(0, 1000−1000)  = 0        → 0
bucket 1,500–3,000 w=0.12 mid=2,250  MAX(0, 2250−1000)  = 1,250    → 0.12 × 1,250 = 150
bucket 3,000+     w=0.03  mid=4,500  MAX(0, 4500−1000)  = 3,500    → 0.03 × 3,500 = 105
Σ = AED 255 per card → × 0.02 = AED 5.10 per card per month
atm_rev = 1,000 × 5.10 = AED 5,100/month

  [Applying the MEAN instead: MAX(0, 940 − 1,000) × 0.02 = AED 0.00. ZERO.]
```
**The mean returns zero and the distribution returns AED 5,100. This is the same Jensen error as D2, in miniature.**

**Pattern 8 — Redemption cost on net flow (monthly)**

```
net_flow(t) = sip_grams + spot_grams − self_custody_out − redemption_grams
spread_cost(t) = MAX(0, −net_flow(t)) × F1 × dealer_two_way_spread
```

**Evaluated, two book states, 10,000 g of AUM, 2% two-way spread:**
```
GROWING (8% in, 3% out annually):
  monthly in  = 10,000 × 0.08 ÷ 12 = 66.7 g
  monthly out = 10,000 × 0.03 ÷ 12 = 25.0 g
  net_flow    = +41.7 g  →  spread_cost = MAX(0, −41.7) × … = USD 0.00 ✅

SHRINKING (2% in, 6% out):
  net_flow    = 16.7 − 50.0 = −33.3 g
  spread_cost = 33.3 × 141.46 × 0.02 = USD 94.25/month
```
**Zero in every month the book grows. That is the whole §5.4 argument, and it is why the cost line is structural rather than proportional.**

**Pattern 9 — Log-linear opex interpolation (annual)**

```
v(y) = v(low) × ( v(high) ÷ v(low) ) ^ ( (y − y_low) ÷ (y_high − y_low) )
```

**Evaluated, Technology block, Y3 = 115,000 → Y10 = 600,000, at Y5:**
```
v(Y5) = 115,000 × (600,000 ÷ 115,000) ^ ((5 − 3) ÷ (10 − 3))
      = 115,000 × 5.2174 ^ 0.2857
      = 115,000 × 1.6034
      = USD 184,391
  [Straight-line would give 115,000 + (485,000 × 2/7) = USD 253,571 — 37% higher]
```

**Pattern 10 — Tax with the 75% cap (annual only)**

```
loss_bf_utilised(y) = MIN( loss_pool(y−1), 0.75 × MAX(0, accounting_profit(y)) )
tax(y)              = 0.09 × MAX(0, accounting_profit(y) − loss_bf_utilised(y) − 375,000)
```

**Evaluated, first profitable year: profit USD 1,000,000, loss pool USD 5,000,000:**
```
loss_bf_utilised = MIN( 5,000,000, 0.75 × 1,000,000 ) = USD 750,000
taxable_income   = 1,000,000 − 750,000                = USD 250,000
tax              = 0.09 × MAX(0, 250,000 − 375,000)   = USD 0
```
**Here the zero band absorbs the residual. At a USD 3m profit against the same pool:**
```
loss_bf_utilised = MIN(5,000,000, 2,250,000)          = USD 2,250,000
taxable_income   = 750,000
tax              = 0.09 × (750,000 − 375,000)         = USD 33,750
```
**Real cash tax paid in a year the business is cumulatively USD 2m in the red.** That is the finding.

### 10.5 The monthly→annual transition at M24 / Y3

**This is the highest-risk seam in the workbook and it must be built deliberately.** It moves from M72/M73 to **M24/Y3** at v2.1 (D21).

🔴 **The seam is far less dangerous than v2.0's, and for a structural reason worth stating.** v2.0's seam was a **change of engine**: at M73 the tier distribution and `Recent` stopped being computed and started being *held*, so the annual block ran on a frozen snapshot. **The v2.1 seam is only a change of column width.** The lifecycle curves run monthly to M84 regardless of how the Model sheet is columned, so an annual column is built from **twelve genuine monthly convolutions** aggregated (§3.x.3, fourth candidate). **Nothing is frozen, nothing is held, and no simplification is taken at the seam itself.**

| Quantity | At M24 (last monthly column) | At Y3 (first annual column) |
|---|---|---|
| **Period length** | 1 month | 12 months |
| **Population** | One convolution | **Twelve convolutions, aggregated.** Never one convolution on an annual acquisition figure |
| **Tier distribution** | From the tenure→tier lookup, convolved | **Identical mechanism.** Read at each of the twelve months, then aggregated. **Not held, not frozen** |
| **Gate arrival** | From the first-passage solve on the curve | **Identical mechanism.** The gate has substantially resolved by M8, so by Y3 the distribution is nearly settled — but it is still read, not assumed |
| **Heavy-seller haircut** | A single multiplier on the mix | **Identical multiplier.** It does not vary by block |
| **Seasonality (S52a, S52b, S53)** | Applied | **Not applied.** All three normalise to 12.00 and cancel over a full year |
| **Flows** | Monthly value | **Sum of the twelve monthly values**, each at its own convolved population. **Not `12 ×` a single month** |
| **Stocks (AUM, drawn, partner AUM)** | Closing balance | **Average of opening and closing** |
| **Acquisition-budget lag** | `t−1` = one month | **`t−1` = one annual column, i.e. twelve months.** Write it explicitly (§3.x.3 item 1) |
| **Tax** | Booked in the FY-end month only | Booked once per annual column |
| **Card programme fixed costs** | Monthly minimums + quarterly assessments in the quarter-end month | `12 × monthly + 4 × quarterly` |
| **Streams 5 and 6** | **Zero.** Both activate at M24, on the boundary | **First non-zero column.** Booked at the start of the annual block, **never as a stub month at M24** (§4) |

**Four checks on the seam, all on the Checks sheet:**

1. **Continuity.** `live_accounts(Y3 opening) = live_accounts(M24 closing)`. A mismatch means the convolution range is wrong at the seam.
2. **Decomposition.** The Y3 population must equal the sum of twelve monthly convolutions at M25–M36, **not** a single convolution on an annual figure. This is the check that protects the gate distribution.
3. **Revenue continuity.** `revenue(Y3) ÷ 12` should sit within ±15% of `revenue(M24)`. A larger jump means a flow has been treated as a stock or vice versa. **This single check catches most transition errors.** ⚠ **Exclude streams 5 and 6 from this test at the Y3 column** — they are zero at M24 by design and would fail a continuity test that is measuring the wrong thing.
4. **No stub month.** `stream5(M24) = 0` and `stream6(M24) = 0`, with both non-zero at Y3.

⚠ **The one thing the seam still costs, and it is the column resolution, not the engine.** Within an annual column the model reports a single number for twelve months, so it cannot show *when inside Y3* something happened. **Everything that needs a when — the gate at M8, the card at M18, Gold at M20 — is inside the monthly block by design** (§1). What falls in the annual block is Platinum at M36 and Sovereign at M61, and that is acceptable **because the rate ladder was collapsed** (D22, limitation L3a).

### 10.6 Check formulas

All nine live on the Checks sheet and all return **TRUE/FALSE**, never a number to be eyeballed.

| # | Check | Formula | Why |
|---|---|---|---|
| **1** | **Curve conservation, and book conservation** | On the curve: `PRE_GATE + CONTRIBUTING + REDUCED + REG_BLOCK + STOPPED + DORMANT + CLOSED = 1.000` at every `m`, **per archetype** — 5 tests × 84 months. On the Model sheet: `Σ_states book(s,t) = cumulative_ever_acquired(s,t)`, per segment, every period | Catches any state transition that creates or destroys accounts, **and** any convolution that loses or duplicates a cohort |
| **2** | **Tier counts sum to accounts** | `Σ_tier share(s,t,tier) = 1.000` and `Σ_tier count = gated_accounts(s,t)`, ± 1e-9 | Catches a tenure→tier lookup that misses a boundary. ⚠ **On the ICS Validation sheet the same test also catches the `49.9998` failure**, which the collapsed lookup cannot produce but the validation formula still can |
| **3** | **Grams reconciliation** | `grams(t−1) + bought + rewards − self_custody − redeemed = grams(t)`, every period | Catches double-counted leakage, the most likely stock error |
| **4** | **Non-negativity** | `MIN` over every population row, every revenue row and every stock row `≥ 0` | A negative population is the classic symptom of a hazard applied to a base it has already been applied to |
| **5** | **Gold Rewards cap never negative** | `MIN over t,k of [ net_ic(t,k) + stream5_attributable(t,k) − custody_cost(t,k) ] ≥ 0` | If it goes negative the benefit is being funded from profit, which decision 6 forbids |
| **6** | **Acquisition ceiling never breached** | `total_acquisition_cost(t) ≤ ceiling% × stream1_revenue(t−1)`, **every period, not on average** | A ceiling solved on average breaches in the ramp months, which is when cash is tightest |
| **7** | **Activation flags fire on the right period, and on the right side of the seam** | `stream2(t) = 0 for all t < 18`; **`stream5(M24) = 0` and `stream6(M24) = 0`, both first non-zero at Y3**; `referral_payout(t) = 0 for all t < 13`; `F27 one-offs booked only in M15` | Catches a hardcoded activation month that drifted from the Time Series sheet, **and the M24 stub-month error** (§4) |
| **8** | **Scenario-switch canary** | A cell that returns the active scenario name **and** a hash of all Base/Aggressive/Conservative selections, so a partially-flipped state is visible | **Under per-parameter override (D17) a mixed state is legitimate — the canary shows *which* mixed state** |
| **9** | **Seasonality normalisation** | `SUM(S52a) = 12.000` and `SUM(S52b) = 12.000`, exactly | 🔴 **An un-normalised seasonality vector silently changes the model's annual answer.** This is one of the more common ways a monthly model goes wrong |

**Seven additional checks specific to this build:**

| # | Check | Formula |
|---|---|---|
| **10** | **Iterative-calculation canary** | Reports the workbook's iterative-calculation setting. Must read OFF |
| **11** | **Denomination monotonicity** | `bar_grams(t) ≥ bar_grams(t−1)` for all `t` — the T3 latch |
| **12** | **Persona validation** | All nine personas A–I return the corpus's stated Record, Standing, Retention, ICS and Tier, **on the ICS Validation sheet**. **Nine TRUEs or the build does not ship** |
| **13** | **M24/Y3 seam** | The four continuity tests at §10.5 |
| **14** | 🔴 **Convolution pairing** | For a synthetic acquisition vector of `(1, 0, 0, …, 0)` — one account at M1 and nothing after — the convolved book at period `t` must equal `curve(m = t)` exactly, for every series and every `t`. **A single impulse is the only test that isolates the pairing.** If the ranges are built forwards, this returns `curve(m = 1)` at every `t` and the failure is unmistakable (§10.4 Pattern 1) |
| **15** | 🔴 **The 5% collapse-safety gate** | `MAX over y in Y1..Y7 of ABS( stream2_lookup(y) − stream2_full_ICS(y) ) ÷ gross_profit(y) ≤ 0.05`. **FALSE means the collapse is unsafe and must be reverted** to the per-period ICS engine (§3 Layer 5d). Measured headroom: ~2% at Y7 against a 5% tolerance |
| **16** | **ICS Validation is a leaf** | No formula on the Model sheet references the ICS Validation sheet. **If it does, the collapse has been silently un-done** (§3.x.1) |

**Sign-off rule: the build is not complete until all sixteen return TRUE simultaneously under Base, Aggressive and Conservative.** Checks 1, 5, 9 and 12 are the ones most likely to fail first, and each corresponds to a specific v1.0 defect. **Checks 14 and 15 are new at v2.1 and each guards one of the two architecture decisions** — 14 the convolution, 15 the collapse. 🔴 **Neither may be waived. A convolution built backwards and a collapse that has drifted past tolerance both produce a model that runs, reconciles and is wrong.**

---

## 11. Growth Logic Summary

**New at v2.0.** Required by the `revenue-model-architecture` skill and absent from v1.0 (D19).

| Driver | Pattern | Start → End | Ceiling | Formula approach |
|---|---|---|---|---|
| **New accounts/month** | Ramp, then logistic decay against headroom | **49.7** → **620.5** | `base(s) × S22` per segment, **against cumulative-ever-acquired** | Channel volume × S16 mix × S23 saturation × S52a seasonality |
| **Active agents** | Step, **net of 45% annual attrition** | 5 (Y1) → 200 (Y10) as a **stock** | Recruitment capacity | T7 stock grossed up by S18 into a recruit flow; each recruit re-enters the S17 ramp at 0.20 |
| **Referral volume** | **Zero to M13**, then compounding on the qualified-referrer base | 0 → `{{UNFILLED: Y10 referral accounts/month — not in spine; new accounts are published in total, not by channel}}` | Qualified referrers × S19 | **Two six-month gates in series. Steady state not before ~M25** |
| **Live accounts** | Compounding, **decelerating** as saturation and lapse bite | **511** → **21,661** | Sum of segment ceilings | **Convolution of the acquisition vector against the `alive` curves** (D23); only CLOSED exits |
| **Holding-not-contributing** | **Compounding faster than the live base** | **176** → **42,536** (64,197 holding less 21,661 live) | **None** — it is the residual of everything ever acquired minus CLOSED | 🔴 **Reaches ~81% of ever-acquired by M61. The population v1.0 deletes** |
| **Tier mix at Gold+** | S-curve, saturating as the archetype mix binds | 0% (Y1) → **63.0%** | **Bounded by the archetype mix**, not by time | Threshold each archetype track, then weight (D2) |
| **Sovereign share** | **Zero to M61**, then a slow climb | 0% → **4.4%** (954 accounts) | **~10% — only the perfect-payer track can ever reach it** | Requires Record 100 AND Recent 12 AND Sold ≤ 30% **simultaneously, monthly** |
| **AUM (grams)** | Compounding on inflow, **decaying on an accelerating leakage base** | **USD 204,262** → **USD 39,790,584** | Inflow minus S31 and S32×S33 outflow | Stock-and-flow; **the lapsed-holder decay term dominates from ~Y4** |
| **Stream 1a — SIP fee** | Compounding on accounts, **decaying per unit** | **USD 2,630** → **USD −80,548** | Segment ceilings | **Three counter-forces at once**: the fee steps down, the discount steps up, the never-gated are the only ones paying full freight |
| **Stream 1b — Spot** | Compounding **and convex in book maturity** | **USD 1,294** → **USD 10,771** | Same segment ceilings | Attach rises with tenure, so the stream grows faster than the account base. **~45% of volume in two festival windows** |
| **Stream 2 — Interchange** | **Step at M18**, then compounding on two multiplying bases | 0 → **USD 4,156,380** | Gold+ population × S5 activation | Cardholder count **and** tier mix both rise. **Offset by the regressive per-txn fee and the F27 minimums** |
| **Stream 3 — Family/Will** | **Linear.** The only stream with no compounding mechanism | **USD 1,791** → **USD 111,065** | The attach rate itself | Live accounts × S11 × tier-discounted price. **Cost base grows with cumulative registrations while revenue grows with live ones** |
| **Stream 4 — Cardholder fees** | Tracks stream 2's base, **with the opposite tier gradient** | 0 → **USD 2,226,204** | Same Gold+ population | 🔴 **The tier that spends most is the tier whose fees are most waived.** Revenue per cardholder falls as the book matures upward |
| **Stream 5 — Credit** | Compounding on collateral, **cut 49× against v1.0 — mostly by the collateral base, not by turnover** | 0 → **USD 12,135** | Gold+ collateral × 80% at the very top, bounded by the ~10% Sovereign cap | Peak drawn × **S40 = 0.42** (1.88× fall), vintaged by struck LTV — but the **collateral base per HOLDING account is the larger correction at 2.96×.** Origination is per-event and rises with turnover |
| **Stream 6 — B2B** | **Stacked S-curves**, one per partner | 0 → **USD 1,221,200** | S13 total partner AUM | Each partner runs its own 60-month S43 ramp. **Partners signed in Y7 are still ramping at Y10** |
| **Stream 0 — Redemption cost** | Linear on AUM, **accelerating** as the lapsed share rises | **(USD 0.19)** → **(USD 158)** | **None. Uncapped by construction** | F20 per event + `MAX(0, −net_flow) × spread`. **Zero spread cost in every month the book grows** |
| **Opex** | **Step within block, scale within block** — never on the total | 894,800 → 8,695,500 | None | Log-linear within block (F32), booked in the stated month |
| **Marketing spend** | Decision variable, **not a cost output** | 0 (Y1) → 1,200,000 (Y10) | The acquisition budget ceiling (§9 item 2) | **One source, two consumers.** Feeds acquisition; referenced by opex |
| **Effective CAC** | 🆕 **FLAT at S15** (D27) | **120, constant** | **The saturation ceiling, not the CAC curve** | `effective_CAC = S15`. **Convexity retired to the `CAC_CONVEXITY` switch, default OFF; calibration moves to Phase 5** (§3 Layer 1, S25). ⚠ **Direct-channel LTV:CAC at high spend is an upper bound** |
| **Float capital** | Step with bar denomination, **latched** | ~29k → ~3.6M | None | `MAX(2 bars, 1 bar + S50 days)`. **Falls as a share of AUM — a fixed operational requirement, not a proportional drag** |
| **Cumulative cash** | **Down throughout, flattening but never turning up inside the horizon** | 0 → **USD −14,541,529** on the ten-year run | — | ⚠ **Report the shape, not the level** (§14). On the ten-year run it bottomed at **USD −14,668,019 in M114** and was still USD −14,541,529 at M120 — **both beyond the new horizon.** A 7-year model reports a within-horizon minimum, **which is not the peak and must not be labelled as the fundraise** |

**Five structural insights the table is meant to make visible:**

1. **Two of the six streams do not exist for the first 18 to 24 months, and between them they carry the majority of terminal revenue.** Everything before M18 is streams 1a, 1b and 3 against a full cost base. **The shape of the early years is set by what is absent, not by what is growing.**
2. **The holding-not-contributing population grows faster than the live one and never stops growing.** It is the residual of everything ever acquired minus the few accounts that reach grams = 0. **It bears cost in every period and revenue in some — and v1.0 has no row for it at all.**
3. **Streams 2 and 4 move in opposite directions per cardholder as the tier mix rises.** Blending them hides the trade and gets the sign of the benefit ladder wrong. **They must never be reported as one number.**
4. **Stream 1's per-unit margin degrades on three fronts simultaneously** — a stepping-down fee, a deepening discount, and the exhaustion of the never-gated full-freight population as the book matures. **Volume growth has to outrun all three.**
5. **The only stream with no compounding mechanism is stream 3**, and the only stream with no acquisition cost is stream 6. **They are the two the client thinks least about and they behave least like the others.**

---

## 12. Excel structure map

🆕 **Five visible sheets and five hidden working sheets** (D26, revising D18 and D23). **The visible five are fixed by the firm's `revenue-modeler` standard: Cover, Assumptions, Scenario Parameters, Model, Summary, in that order.** The working sheets are added after them and hidden. Full index and the two placement decisions at §1.1.

**Why the machinery is not simply put on one tab.** A 6-segment × 5-archetype cohort engine with an ICS state machine, six streams, a contra-revenue layer and two solvers lands near **600 rows × 76 columns ≈ 45,000 formulas on one tab.** That is not a workbook, it is a hazard. **D26 does not reverse that argument — it separates presentation from computation rather than merging them.** The machinery still lives on its own sheets; those sheets are simply not the ones a reader opens.

⚠ **v1.0's §11 was internally inconsistent with its own §10.1** — §11 listed an Opex sheet while §10.1 put opex rows on the Model sheet. **D26 settles it in §10.1's favour: opex, P&L, tax, working capital and cash are row bands on the Model sheet, and there is no separate Opex sheet.**

**The structure shrinks substantially at v2.1, and it is worth showing the arithmetic:**

| | v2.0 | v2.1 | Driver |
|---|---|---|---|
| Model sheet | ~520 rows × 76 cols ≈ 39,500 cells | **~200 rows × 29 cols ≈ 5,800 cells** | D21 horizon, D22 collapse, D23 convolution |
| Cohort Engine | ~320 rows × 76 cols | **Gone.** Replaced by a 24-row convolution band on the Model sheet | D23 |
| ICS Engine | ~340 rows × 76 cols | **Gone as an engine.** Survives as a ~76-row **ICS Validation** leaf sheet | D22 |
| Lifecycle Curves | — | **New: ~92 rows × 84 cols ≈ 7,700 cells, computed once** | D23 |
| **Net** | | **Roughly an 80% reduction in live formula cells** | |

⚠ **The Lifecycle Curves sheet is the one place the workbook gets *wider*, and that is deliberate.** 84 columns on an input sheet is the price of 29 columns on the Model sheet. **Do not shorten it to match the Model sheet** — a Y7 annual column needs twelve genuine monthly lifecycle points for the M1 cohort, which reaches `m = 84` (§1).

**Colour legend — the same convention on every sheet:**

```
BLUE text     = hardcoded input                 (only ever on Assumptions and Scenario)
BLACK text    = in-sheet formula
GREEN text    = cross-sheet link
YELLOW fill   = scenario-variable input
GREY fill     = section header / not a data cell
RED text      = a check that is currently FALSE
```

**The Assumptions indirection convention, and it is a hard rule.** **No formula anywhere in the workbook may contain a numeric literal other than 0, 1, 12 or 100.** Every parameter is referenced by its named range — `F1_gold_price`, `S27_perfect_weight`, `S40_turnover`. Named ranges live on Assumptions and Scenario Parameters only. **A modeller must be able to change any input in exactly one place.** The Checks sheet cannot verify this automatically; it is enforced at review.

### Cover

```
SECTION          ROWS    CONTENTS
────────────────────────────────────────────────────────────────────
Title            1–5     Aurumix Revenue Model — Hybrid Monthly + Annual
Version          7       V2.1 — Six streams + redemption cost
                         29 periods (24 monthly M1–M24 + 5 annual Y3–Y7)
                         Lifecycle Curves sheet is monthly to M84 — NOT 29
Date             8       August 2026
Scope            10–15   Full P&L to net profit after tax, plus cash and funding.
                         Lifecycle-curve convolution, five payment archetypes,
                         live run-of-6 gate, tenure->tier lookup,
                         spot lane, vintaged credit.
Colour legend    17–23   As above
Read-me          25–32   Pointer to §3 sign-off, the SIXTEEN Checks,
                         the placeholder convention, and — first —
                         the 5% collapse-safety gate at check 15
Master check     34      ALL CHECKS PASS:  =Checks!<master row>     [D26]
                         GREEN on TRUE, RED fill on FALSE.
                         A LINK, never a typed value.  This is the only
                         inbound reference Cover is permitted to carry.
Dependency order 36–46   The §3.x.1 logical sheet order, written out, so
                         that the by-name dependency test survives the
                         five hidden working sheets.               [D26]
Sheet map        48–52   The five visible sheets, then a note naming the
                         five hidden working sheets and why they are
                         hidden.  A reader must never conclude that a
                         number came from nowhere.                 [D26]
```

🆕 ⚠ **The Cover carries the only honesty obligation D26 creates.** Hiding the machinery is a presentation choice, and it becomes a misrepresentation the moment a reader cannot find out that the machinery exists. **The sheet map at rows 48–52 is not optional**, and it must say plainly that five working sheets are present and hidden, name them, and say that unhiding them is expected rather than discouraged.

### Assumptions

```
SECTION          ROWS    CONTENTS
────────────────────────────────────────────────────────────────────
Fixed inputs     3–46    F1–F38. Columns:
                           A: ID    B: Value    C: Unit
                           D: Source category (CITED/DERIVED/TRIANGULATED/
                              CLIENT INPUT/ASSUMPTION)
                           E: Source detail with URL
                           F: Confidence
                           G: Sheet location where consumed
F27 detail       48–55    Card programme fixed cost stack, six lines,
                          with the "when booked" column
Time-evolving    57–120   T1–T10 across all 29 period columns.
                          T3 carries the threshold rule AND the latch.
                          T4, T5, T8, T10 are OUTPUTS — GREEN, linked
                          back from the Model sheet, never typed.
                          ⚠ F12's tier ladder (1.80/2.05/2.10) STAYS as an
                          input even though the live model reads only the
                          Gold rate — the ICS Validation sheet needs the
                          full ladder to compute the 5% gate (D22)
Named ranges     122+     The full named-range index, ID → range name → address
```

**Freeze panes:** at **C3** — ID, value and unit columns stay visible while scrolling the source and confidence detail.

### Scenario Parameters

```
SECTION              ROWS    CONTENTS
────────────────────────────────────────────────────────────────────
LAYER 1 — Global     3–8     D6 = "Base" (dropdown: Base / Aggressive /
  bounding case              Conservative / CUSTOM)
                             E6 = CHOOSE index
                             ⚠ Label reads "BOUNDING CASE, not a forecast"
LAYER 2 — Per-       10–14   For each parameter row: an OVERRIDE column.
  parameter override         If populated, it wins over the global switch
                             and D6 flips to "CUSTOM"
LAYER 3 — Named      16–30   Six narrative scenarios (§13), each a stored
  narrative scenarios        vector of per-parameter overrides
Binary switches      32–44   INDIA_ENABLED, LAPSED_KEEPS_CARD,
                             PREPAID_VS_CREDIT, OPTION_B, DEALER_CARRIED,
                             SUBDECISION_2, DFSA_LICENCE_REQUIRED,
                             ENFORCEMENT_SALE_IS_REDEMPTION,
                             EQUAL_VALUE_FULL_PREVAILING, TRADEFLOW_1KG
Group A: Acquisition 46–72   S1, S2, S12, S15–S26
Group B: Behavioural 74–104  S27–S33, S45–S47  (archetypes, states, leakage, spot)
Group C: Card        106–124 S3–S5, S34–S39, S53
Group D: Credit      126–134 S8, S9, S40, S41
Group E: B2B/Family  136–144 S11, S13, S42–S44
Group F: Cost/Cap    146–160 S6, S7, S10, S14, S48–S52
Tornado control      162–175 Per-parameter ±X% flex driver for §13.4
```

**Freeze panes:** at **C10**. **Every yellow cell on this sheet is an input; nothing else in the workbook is.**

### Time Series

```
SECTION              ROWS    COLUMNS
────────────────────────────────────────────────────────────────────
                             Col A: label  Col B: unit
                             Col D–AA: M1–M24   Col AB–AF: Y3–Y7
Period headers       1–5     Number, label, type, calendar month index,
                             financial-year-end flag
Activation flags     7–20    Card M18, S4 M13, referral M13, F27 one-off M15
                             — all inside the MONTHLY block.
                             Credit and B2B: START OF THE ANNUAL BLOCK (Y3),
                             NOT a stub month at M24.  S6 at M25 = Y3.
                             ⚠ EVERY activation month lives here and NOWHERE else
Seasonality          22–28   S52a, S52b, S53 vectors, plus the
                             SUM = 12.000 verification row
Price and fee ladder 30–40   F1 gold price, T1 entry fee, T2 premium,
                             T3 bar denomination (threshold + latch)
Opex interpolation   42–70   Per block: Y1/Y3/Y7 anchors, step-or-scale flag,
                             F32 log-linear interpolation, booked-month rule,
                             Marketing reconciliation plug
Float                72–82   F38 sizing rule, S50 buffer, float grams,
                             float capital (T9), float_mode from S51
```

**Freeze panes:** at **D5**.

### Lifecycle Curves *(new at v2.1 — the only monthly-to-M84 sheet)*

```
SECTION              ROWS    COLUMNS
────────────────────────────────────────────────────────────────────
                             Col A: series  Col B: archetype  Col C: unit
                             Col D–CG: m = 1 … 84
                             ⚠ MONTHS SINCE ORIGINATION, NOT PERIODS.
                                No calendar date appears on this sheet.
Row bands at §10.1
```

**Freeze panes:** at **D4**. **Group the five archetypes so a reviewer can collapse four and read one curve end to end** — that is how this sheet is checked, and it is the reason it is a separate tab rather than a block on the Model sheet.

🔴 **This sheet is computed once and never varies by period, segment or scenario-of-time.** It varies by scenario only through the archetype weights and hazards (S27), which is exactly one dependency. **If anything on this sheet acquires a period reference, the architecture has been broken** (§3.x.2a).

### Acquisition

Row bands at §10.1. **Freeze panes at D5.** The acquisition vector band (rows 66–74) is the sheet's only output and **must be a clean rectangle of one row per segment** — the convolution's `SUMPRODUCT` ranges read it directly, and a merged or interrupted row breaks them silently.

### ICS Validation

Row bands at §10.1. **Freeze panes at D4.** The persona validation block sits at the bottom deliberately, so **its nine TRUEs are the last thing on the sheet**, with the 5% collapse-safety gate immediately above them.

🔴 **This sheet is a leaf.** It reads the Lifecycle Curves; it is read by Checks. **No Model formula may reference it** (§3.x.1, check 16).

### Model

Row bands at §10.1. **Freeze panes at D5.** Stream blocks are ordered by stream number so a reader can navigate by §6.

⚠ **Rows 6–29 are the convolution band and every other row on the sheet depends on it.** Put it at the top, above the fee block, and **group it** — it is 24 rows of near-identical `SUMPRODUCT` and a reviewer needs to check three of them, not all 24. **The three to check are `alive`, `gated` and `tier`**, because the first tests the pairing, the second tests the first-order term and the third tests the collapse.

⚠ **Rows 102–128 must be physically ordered gross interchange → Gold Rewards cap → net interchange**, per §3.x.2. The ordering is the resolution of the apparent circularity, so it is structural rather than cosmetic.

#### Model, continued — the opex and P&L band 🆕

**D26 folds the former Opex & P&L sheet into Model as a second row band.** Row bands at §10.1, renumbered to continue after the benefit-cost block rather than restarting at row 1. **Freeze panes at D5, one set for the whole sheet.** The tax block computes in **every** column but writes a non-zero value **only in financial-year-end months** — the `IF(FY_end_flag, …, 0)` guard comes off the Time Series sheet.

⚠ **Put a banner row and a page break between the revenue band and the opex band.** The sheet is now ~280 rows and it carries two distinct arguments: what the business earns, and what it costs. **A reader must be able to see where one ends and the other begins**, and the printed version must not split a stream block across the boundary.

### Summary

```
SECTION              ROWS    CONTENTS
────────────────────────────────────────────────────────────────────
Headers              1–3     Columns: Label, Y1…Y7, 7-Yr Total
                             Y1 = SUM(M1:M12), Y2 = SUM(M13:M24),
                             Y3–Y7 = direct reference to the annual columns
Revenue by stream    5–16    1a, 1b, Stream 1 total, 2, 3, 4, 5, 6,
                             Stream 0 (negative), TOTAL REVENUE
Revenue mix          18–26   Each stream as % of total
Cost summary         28–40   COGS, benefit costs, acquisition, opex,
                             EBITDA, tax, NET PROFIT AFTER TAX
Cash and funding     42–52   Free cash, cumulative, the WITHIN-HORIZON trough
                             and its period, total funding requirement.
                             ⚠ Label the trough as a within-horizon minimum,
                             NOT as peak funding — the peak falls outside
                             a 7-year window (§14, §0 footnote)
Key metrics          54–80   Live accounts (EOY), holding-not-contributing,
                             never-gated, tier distribution, AUM,
                             active cards, borrowers, partner count,
                             revenue per account, opex per account,
                             opex as % of AUM
Unit economics       82–100  §7.8 LTV/CAC/payback by segment and by channel
Break-even views     102–120 §14: the fixed point, the diverging curves,
                             promoted outputs
Tornado data         122–140 Per-parameter ±X% net profit and peak funding deltas
```

### Checks

```
SECTION              ROWS    CONTENTS
────────────────────────────────────────────────────────────────────
Master flag          3       =AND(all SIXTEEN). ONE cell. Green or red.
Structural (1–4)     5–12    Curve conservation (5 archetypes x 84 months)
                             AND book conservation per segment,
                             tier counts sum to accounts,
                             grams reconciliation, non-negativity
Economic (5–6)       14–18   Gold Rewards cap ≥ 0,
                             acquisition ceiling never breached
Timing (7, 9)        20–26   Activation flags fire on the right period AND on
                             the right side of the seam (no M24 stub month),
                             seasonality vectors sum to exactly 12.000
Scenario (8)         28–32   Scenario canary: active name + selection hash,
                             so a partially-flipped CUSTOM state is visible
Build integrity      34–44   Iterative-calculation canary (must read OFF),
  (10–11, 13, 16)            denomination monotonicity (the T3 latch),
                             M24/Y3 seam: continuity, decomposition,
                             revenue continuity ±15%, no stub month,
                             ICS Validation is a leaf (no Model reference)
ARCHITECTURE (14–15) 46–54   🔴 CONVOLUTION PAIRING: the (1,0,0,...) impulse
                             test returns curve(m=t) at every t.
                             🔴 THE 5% COLLAPSE-SAFETY GATE: max annual
                             stream-2 delta ≤ 5% of gross profit.
                             FALSE on 15 REVERTS THE COLLAPSE.
                             These two guard the two v2.1 decisions and
                             neither may be waived.
Persona set (12)     56–68   All nine personas A–I, each returning
                             Record / Standing / Retention / ICS / Tier
                             against the corpus's stated values.
                             ⚠ H and I are the two a naive build fails
```

**The Checks sheet is where this build exceeds the benchmark, which has none.** **Row 3 is the sign-off cell: the build does not ship until it reads TRUE under Base, Aggressive and Conservative.**

---

## 13. Scenario architecture

**New section at v2.0** (D17). v1.0 has one `CHOOSE()` across fifteen parameters. **Flipping to Conservative sets all fifteen simultaneously — a joint state with probability near zero**, which is why v1.0's §12 reports the Conservative break-even as "never" and why **v1.0 has exactly one usable scenario: Base.** It also imposes an implicit correlation matrix of all +1 on parameters that are genuinely correlated in different directions — a Conservative rail and a Conservative PM share have nothing to do with each other, and a Conservative persistency and an Aggressive spot attach are not even the same sign of surprise.

### 13.1 Three layers

| Layer | What it is | How it is used |
|---|---|---|
| **1. Global switch** | Base / Aggressive / Conservative across all scenario parameters | **Relabelled honestly as a bounding case, not a forecast.** It answers "what is the widest plausible envelope," and nothing else. The label on the sheet must say so |
| **2. Per-parameter override** | Any single parameter can be set independently; the global switch flips to CUSTOM | The working mode. **This is how a real question gets asked** — "what if the rail is bad but everything else holds?" |
| **3. Named narrative scenarios** | Stored vectors of per-parameter overrides, each with a name and a story | What goes in front of the client. **A scenario the client can repeat back is worth more than a scenario that is merely internally consistent** |

### 13.2 The named narrative scenarios

| Name | The story | Parameters overridden | The question it answers |
|---|---|---|---|
| **Rail kills it** | AANI is unavailable or priced at UAEDDS levels, and the SIP loses money on every collection | S1 → 1.36 (Conservative). **Everything else Base** | Does spot volume (1b) save stream 1, and is the agent channel viable at all? **The whole scenario costs USD 1,416,257 of cumulative net profit (−15,526,752 against Base's −14,110,495) and pushes peak funding from USD 15,076,460 to USD 16,387,738, its month from 114 to 118. Y10 revenue is unchanged at USD 8,150,081 because the rail sits in cost of revenue, not revenue.** ⚠ The spine does not publish a Y5 stream 1 net margin under this scenario; the Base Y5 figure is USD 30,741 |
| **Card works, savings doesn't** | The card programme lands well; the SIP persists badly | S2 → 45%, S27 → Conservative mix. S3, S4, S5 → Base or better | **The most likely real outcome**, and the one v1.0 cannot express. Does the card carry a shrinking book? |
| 🔴 **No card** | The sponsor bank does not sign, or the programme is prepaid-only at a 1.00% capped rate | `PREPAID_VS_CREDIT` → prepaid; or card activation → 0 | **The most important missing scenario. It removes the majority of revenue and it is a real commercial risk.** v1.0 cannot represent it at all, because prepaid-vs-credit is not a variable |
| **Distribution fails** | Agents underperform and referral never compounds | S12 → 2, S17 → Conservative, S18 → 60%, S19 → 0.18, S25 → Conservative | Does the model still reach any meaningful scale on paid direct alone, and at what CAC? |
| **Client's plan** | The client's own 100,000-investor Y10 target, **imposed as an input** | Account count forced to the client's trajectory; **everything else Base** | **Measured against the floor, never assumed as an output.** What would have to be true, and what does it cost to get there? **On the ten-year run the `clients_plan` scenario reached 169,756 ever-acquired but only 54,010 live, lifted Y10 revenue to USD 17,668,003 and cut cumulative net loss to USD 7,218,254 with a funding trough of USD 10,468,829 at M113. It turned EBITDA-positive only in Year 10 — by brute-forcing volume in the final year.** ⚠ **Y10 and M113 both fall beyond the new 7-year horizon, so on the rebuild this scenario does not turn inside the window at all. Aggressive, which turned in Y5, still does.** 🔴 **The finding is unchanged and is if anything sharpened: the target is reachable on acquisition and does not fix the unit economics.** `{{UNFILLED: marketing spend implied by the client's 100k target — not in spine; the scenario imposes the account trajectory directly rather than solving the spend that buys it}}` |
| **India closed** | The payment route is never solved | `INDIA_ENABLED` → OFF, **and S44/S42 fall with it** (they are coupled, §6.6) | What does the payment problem cost? **Y10 revenue falls from USD 8,150,081 to USD 6,118,450 — a delta of USD 2,031,631, or 24.9%.** Live accounts fall to 16,700, holding to 50,715, Y10 AUM to USD 33,187,620, and cumulative net loss deepens from USD 14,110,495 to USD 17,746,327 with peak funding rising to USD 18,534,329 |

⚠ **The India scenario must move stream 6 as well as the S5 segment.** Per S16 the B2B row is 60% S5, so **turning India off must reduce S44 to ~40% of Base and S42 to the Conservative path.** v1.0 leaves the two switches independent and they are not.

### 13.3 Binary switches

Not scenarios. **Structural forks where the model has two different shapes**, and each defaults to the conservative or current-design reading.

| Switch | Default | ON does what | Why it is a switch and not a sensitivity |
|---|---|---|---|
| `PREPAID_VS_CREDIT` | **Credit** | Caps interchange at 1.00% and removes the credit facility entirely | *"Not a product choice, it is the business model."* **Worth USD 2,304,921 of Y10 revenue** (8,150,081 → 5,845,160) **and USD 7,254,180 of cumulative net profit** |
| `LAPSED_KEEPS_CARD` | **ON** | Lapsed holders retain card and facility | 🔴 **Nobody has decided.** **Worth USD 3,393,773 of Y10 revenue** (8,150,081 → 4,756,308, a 42% swing) **and USD 5,242,051 of cumulative net profit.** Determines whether the majority of revenue decays with persistency or is immune to it |
| `INDIA_ENABLED` | **ON** | S5 segment live; stream 6 at full S44 | The model prices India as a market; it does not assert a route exists |
| `OPTION_B` | **OFF** | Applies the 2%-of-Reserve-Assets capital escalator | Under Option A the row is flat, **which is the point** |
| `DEALER_CARRIED` | **ON at launch, OFF from Y3** | Float capital zero, F5 zero, price-gap zero, **premium wider** | 🔴 **Charging both sides double-counts. This is an error, not a sensitivity** |
| `SUBDECISION_2` | **OFF** | Compliance-forced exit does not drive Retention to zero | Report the S5 tier delta as **the client's decision cost** |
| `DFSA_LICENCE_REQUIRED` | **OFF** (the exempt reading) | Adds an unpriced annual licence cost | *"A cost question and we cannot quote the client a number without it"* |
| `ENFORCEMENT_SALE_IS_REDEMPTION` | **ON** (the conservative reading) | Recovery fee → 0 | Already modelled at zero in Base; the switch prices the upside |
| `EQUAL_VALUE_FULL_PREVAILING` | **ON** (the safe reading) | Aurumix absorbs the two-way spread on every exit | *"The difference is the entire two-way spread and it decides who absorbs it on every exit"* |
| `TRADEFLOW_1KG` | **OFF** | Launch bar denomination forced to 1 kg | **A 10× launch capital step**, ~USD 29k → ~USD 285k |

### 13.4 The book-state axis

A fourth, orthogonal axis specific to redemption, using the corpus's own figures (`_draft_purchase-structure.md` §5.4):

| Book state | Inflow | Gross exits | Net | Status |
|---|---|---|---|---|
| **Growing** | 8% of AUM | 3% | +5% | **The Base case.** Spread cost = 0 |
| **Flat** | 4% | 4% | 0% | Scenario. Spread cost = 0 |
| **Shrinking** | 2% | 6% | −4% | Scenario. Spread cost on the 4% net |
| **Run** | 1% | 25% | −24% | 🔴 **A stress test, not a scenario** |

**Under Run, the model must report three things and not a revenue number:** the **float breach**, the **settlement-window tier that fires**, and the **spread cost on the 24% net**. `{{UNFILLED: spread cost and float breach under the Run stress — not in spine; the Run book state is not among the ten scenarios run}}`.

### 13.5 Tornado specification

**Two tornados, because the two questions have different answers.**

| Tornado | Output axis | Parameters flexed | Why |
|---|---|---|---|
| **1. Net profit at Y10** | Net profit after tax | All scenario parameters, one at a time, at their own Aggressive/Conservative bounds | **This is what actually evidences the "load-bearing assumptions" claim rather than asserting it** |
| **2. Peak funding** | Peak cumulative cash deficit | Same set | 🔴 **A different ranking.** Parameters that hurt terminal profit and parameters that deepen the funding hole are **not the same parameters** — timing matters for one and not the other |

**Flex each parameter at its own stated bounds, never at a uniform ±20%.** A uniform flex is a statement that every parameter is equally uncertain, which the confidence column contradicts on every row.

**Tornado 1, measured — swing in cumulative net profit:** **S4 card spend (USD 14,177,704), S5 card activation (6,539,376), S3 PM share (6,359,822), F27 card programme fixed costs (2,125,500), S27 archetype mix (1,906,962), S1 rail cost (1,607,643), S11 family attach (694,515), S14 vault rate (359,350), S45 spot attach (167,891), S10 self-custody leakage (149,353), S8 credit take-up (56,569), S40 facility turnover (17,519), S48 Y1 opex uplift (1,975).** **The §8.4 ranking was the prediction; the tornado disagreed and §8.4 has been rewritten to this order** — the top three are all card parameters, F27 enters at 4th on its first flex, and §8.4's own top two (S27, S40) land 5th and 12th.

**Tornado 2, measured — swing in peak funding:** **S4 card spend (USD 10,736,219), S5 card activation (5,865,131), S3 PM share (5,648,857), F27 (2,013,397), S1 rail cost (1,483,384), S27 archetype mix (1,440,687), S11 family attach (628,047), S14 vault rate (310,652), S45 spot attach (175,220), S10 self-custody leakage (123,995), S8 credit take-up (49,005), S40 facility turnover (15,176), S48 (1,975).**

✅ **The two tornados rank differently, as this section predicted.** The orders agree through the top four and then diverge: **S27 is 5th on profit and 6th on funding; S1 rail cost is the reverse — 6th on profit and 5th on funding.** The mechanism is the one predicted: the rail bites from month 1 on every collection, so it deepens the funding hole faster than it damages terminal profit, while persistency compounds into the later years where terminal profit is decided. **A parameter's rank depends on which question is asked, which is the whole reason for running two tornados rather than one.**

⚠ **One part of the prediction was unmet on the ten-year run, and the shorter horizon is expected to fix it.** F27 ranked 4th on both axes rather than materially higher on funding, and S48 ranked last on both. For S48 the cause was measurement rather than substance: it flexes the exit run-rate of a Y1 base that was ~12% of the ten-year cost stack, and **the funding trough landed at M114 — nine and a half years in — so an early-biting parameter had almost the whole horizon to be diluted before the trough arrived.** 🔴 **On a 7-year horizon the trough sits far closer to the ramp and the Y1 base is a much larger share of the cost stack, so the early-biting parameters should rank higher. If they do not, the funding tornado is not reading the cash rows.** A tornado on *the funding trough within the first 36 months* remains the cleanest test of the early-cost hypothesis.

---

## 14. Break-even and risk architecture

> 🔴 **What is kept and what is demoted at v2.1, stated before the section rather than inside it.**
>
> **KEPT — the method, in full.** The fixed point solved against **total cost**, not opex. The **two views** reported separately — entry-fee-only and all-streams — because they answer different questions and the client asked the first one. The **diverging-curves chart**, which makes the point where no crossing exists and needs no solver. All three are correct, all three must be built, and the argument for each is unchanged.
>
> **DEMOTED — the conclusions.** ⚠ **Break-even and peak funding both fall outside a 7-year window.** On the v2.0 ten-year run there was no profitable year in ten and the funding trough landed at M114, which is Y9.5. **Neither of those is a finding a 7-year model can report, and neither is a figure to build narrative on** — the client has instructed that profitability is not to be leaned on because the cost base, the fee schedule and the card terms will all change materially (§0 footnote).
>
> **So: report the mechanism, the shape and the direction. Do not report a break-even year, a break-even account count as a headline, or a peak funding number as a fundraise ask.** Where a figure below is quoted it is from the ten-year run and is illustrative of the method, not of the answer.

### 14.1 The fixed point, and why v1.0's three numbers were wrong

v1.0 divides Year 1 opex — **sized for 500 investors** — by Year 1 margin per contribution to get **171,911 investors.** The answer is **344× the input's own scale.** The same error produces 278,444 at Y3 and 786,620 at Y10 (D6).

**Fitting `Opex(N) = Fixed + steps(N) + variable × N` to v1.0's own three anchors gives marginal opex of USD 93.40/investor/year against a maximum entry-fee margin of USD 10.80/investor/year. The curves diverge. No solution exists at any N.**

**v1.0's prose conclusion was right — "no, at any modelled scale" — and the three precise numbers beside it were not.** v2.0 keeps the conclusion and deletes the numbers.

**Solve the genuine fixed point:**

```
FIND N such that  revenue(N) = Opex(N)

  where Opex(N) = Fixed + Σ steps(N) + variable × N
  and   revenue(N) is computed by the model at that N, NOT extrapolated linearly
```

⚠ **The table below is from the ten-year run. It shows what the solver produces and in what shape. The levels are superseded by the rebuild** (§0 footnote).

| Output | Entry fee only | All streams |
|---|---|---|
| Does a crossing exist? | 🔴 **FALSE. No solution exists at any N** — the two curves diverge rather than cross, because the SIP lane's net contribution margin per collection turns negative with tenure. **This result is structural and does not depend on the horizon: it is a statement about slopes, not about years** | **TRUE**, but outside the modelled book |
| If yes, at what N? | **n/a — there is no crossing.** ⚠ **Entry-fee-only must never be reported as breaking even.** The `extrapolated_year` the model carries against this view belongs to the all-streams trajectory and does not belong to it | **45,102 contributing accounts** on the ten-year run — against the 21,661 the Base path reached by Year 10. ⚠ **Both figures are ten-year. The crossing sits outside the book on either horizon, and it sits further outside on seven years** |
| Marginal opex per investor/yr | **USD 304** (the cost slope against which the fixed point is solved) | same |
| Marginal margin per investor/yr | **Negative and falling**: net margin per contribution ran USD 0.77 at Y1 to USD −0.32 at Y10 on the ten-year run. **The sign change is the finding; the terminal level is not** | **USD 346** |
| Gap | 🔴 **The gap does not close at any N. It widens.** Revenue per account is negative on this basis while the cost slope is positive. **A widening gap is horizon-independent** | **USD 42/investor/yr in revenue's favour**, which is why a crossing exists at all |

**Report entry-fee-only and all-streams separately.** They answer different questions and the client asked the first one.

🔴 **The one conclusion in this subsection that survives the demotion, because it is a statement about slopes rather than about years: the entry-fee lane has no break-even at any N, and adding investors makes it worse.** That is the answer to the client's item 5 and it does not become more or less true on a shorter horizon. **Everything else here is a level, and every level is provisional.**

### 14.2 The diverging-curves chart

**Where no crossing exists, plot the two curves. A chart makes the point unanswerably and needs no solver.**

```
USD/yr
  ▲
  │                                                    ╱ Opex(N)
  │                                              ╱
  │                                        ╱  ← slope ≈ USD 93/investor/yr
  │                                  ╱
  │                            ╱
  │                      ╱
  │                ╱
  │          ╱
  │    ╱                        ────────── Entry-fee revenue(N)
  │╱              ──────────────            slope ≈ USD 10.80/investor/yr
  └────────────────────────────────────────────────────────────▶  N investors
```

**Two curves, both straight, never meeting. That is the answer to the client's item 5, and the chart says it in one glance where three wrong numbers said it badly.**

⚠ **Plot the all-streams line on the same axes.** If it crosses and the entry-fee line does not, **the chart also demonstrates why the business is a card business — visually, without an argument.**

🔴 **This chart is kept unchanged and it is the right artefact under the demotion, because it is the one break-even output that carries no year in it.** It plots against `N`, not against time. **A chart of two diverging slopes is exactly as true on a 7-year model as on a ten-year one**, and it says what §14.1 says without inviting anyone to read a break-even date off it. **Where §14 has to give the client one thing, give them this.** ⚠ **The slope annotations on the sketch above are from the ten-year run and must be re-cut with the rest.**

### 14.3 The promoted outputs

**v1.0 sets "the expense-derived break-even floor, by year" as the headline and then concludes on its own evidence that "break-even is not a function of how many savers you sign up."** An investor-count break-even is right only for a business with roughly constant margin per unit. **Here margin per investor varies 7.6× across segments on the entry-fee lane and 1.72× on all-streams LTV, and opex steps with N** (D16). **v1.0's own ~50× estimate is not supported on either basis** — but the conclusion is unchanged, because the 7.6× spread sits in precisely the lane that loses money.

**Keep** the investor-count break-even as a **named finding** — it answers the client's item 5 and the answer is a valuable "no."

**Promote these four:**

| # | Promoted output | Value | Why it is the better headline |
|---|---|---|---|
| **1** | **Contribution margin per cohort by month since acquisition** | **Now read straight off a lifecycle curve rather than reconstructed from a triangle** (D23) — this output is *easier* at v2.1, not harder. `{{UNFILLED: contribution margin curve by cohort month, months 1–84 — not in spine; margin is published by year and by segment, not by cohort month}}`. The annual blended figure the spine gives ran **USD 0.77 per contribution at Y1, turning negative from Y3 (−0.08)** on the ten-year run | It shows **when** a cohort pays back, which is the question a board actually asks |
| **2** | **LTV:CAC by channel × segment** | See §7.8 | **The variance is the whole point — 7.6× on the entry-fee lane, 1.72× on all streams.** A single break-even number averages away the one fact that decides where to spend |
| **3** | ⚠ **DEMOTED at v2.1 — the funding trajectory as a shape, not a level** | **Report the direction and the slope of cumulative cash, and state plainly that it does not turn inside the horizon.** ⚠ **Do not report a peak funding figure.** On the ten-year run cash break-even was never reached within 120 months and the trough was USD 15,076,460 at M114 — **both beyond a 7-year window.** A 7-year model can report its own within-horizon minimum, and **that minimum is not the peak and must not be labelled as one** | The mechanism is still worth having — v1.0 produces no cash flow at all. **The number is not, until the cost base settles** (§0 footnote) |
| **4** | **Revenue mix over time** | **On the ten-year run, Y1 → Y10 as a share of GROSS PROFIT: SIP 46.0% → −1.1%; spot 22.6% → 0.1%; card interchange 0.0% → 54.3%; family 31.3% → 1.5%; cardholder fees 0.0% → 29.1%; credit 0.0% → 0.2%; B2B 0.0% → 15.9%. Each year sums to exactly 100.0%. Card interchange overtook every other line by Y5 — inside the new horizon — and the two card streams together carried 83.4% of Y10 gross profit, which is beyond it** | It shows the business changing shape at M18 and M24, which no single number can. **The crossover at Y5 is the part of this that a 7-year model can still show** |

**Two supporting facts that belong beside them, both already in v1.0's own arithmetic and both buried:**

- **Agent commission at the solved USD 175.68/account is 21× the Year 1 gross margin per account it is paid out of.** Y1 gross profit is USD 5,716 across 687 accounts acquired — about USD 8.32 each — against total Y1 acquisition cost of USD 71,807, itself **12.6× Y1 gross profit.** v1.0's figure is 88% of Y1 gross margin; **the real number is far worse, and the client has seen neither.** The commission is only rational against all-streams LTV of USD 552–949.
- **The referral reward does not bind on LTV, and that is the finding.** The solve puts the affordable reward at **399% of the referee's entry fee** — F17's 30% placeholder is comfortably payable — because 25% of blended all-streams LTV (USD 749) is USD 187 against a referee entry fee of only USD 47. **On contribution-margin LTV alone it inverts: a 30% reward is roughly USD 14 against an S3 entry-fee-only LTV of USD 5.62.** v1.0's 19.4% was computed at ~40 paying months; **the corrected curve gives 31.2, and the per-segment LTV split is what actually changes the answer.**

### 14.4 The risk view — gold as a level, gold as a path, and the collateral stress

**v1.0's §12 has three views and all three are break-even views. None is a risk view.** This is the risk view.

🔴 **The distinction that organises this whole section: a permanently higher or lower gold price cannot produce a margin call. Only a move landing *after* a loan is struck can.** F1 holds gold flat by design — correct for revenue attribution, because it makes every revenue change attributable to the business rather than the metal — so gold has to be run two separate ways to say anything useful.

#### 14.4a Gold as a LEVEL — and the invariance finding

⚠ **The table below is the ten-year run, so its Y10 column is beyond the new horizon. The invariance it demonstrates is not** — it follows from contributions being fixed in USD, which holds at any period and on any horizon. **Re-cut the levels; the finding stands.**

| Gold move | USD/g | Y10 grams | Y10 AUM | Cumulative net profit | Peak funding |
|---|---|---|---|---|---|
| −30% | 99 | 401,836 | **39,790,584** | (14,008,700) | 14,938,379 |
| −25% | 106 | 375,047 | **39,790,584** | (14,025,482) | 14,961,210 |
| **±0%** | **141** | **281,285** | **39,790,584** | **(14,110,495)** | **15,076,460** |
| +25% | 177 | 225,028 | **39,790,584** | (14,190,599) | 15,186,789 |
| +30% | 184 | 216,373 | **39,790,584** | (14,205,879) | 15,208,113 |

🔴 **USD AUM is invariant to the level of the gold price, and that is a real property of the product rather than a modelling artefact.** Contributions are fixed in USD, so a permanently higher price simply buys proportionally fewer grams: **Y10 grams fall from 401,836 to 216,373 across the −30% to +30% range while USD AUM holds at 39,790,584 throughout.**

Everything downstream of USD AUM inherits the invariance — stream 6, ad valorem custody and the collateral base. Cumulative net profit moves only **1.4%** across the whole range, through second-order effects on bar denomination and price-gap, and it moves *against* a rising price rather than with it. **A DCA gold product is close to indifferent to the level of the gold price, and the client should be told this** — it is counter-intuitive for a business whose product is gold, and it is a genuine structural strength.

#### 14.4b Gold as a PATH — the shock that can actually margin-call

A margin call comes from a move **after** the loan is struck. Drawn balances are carried as vintages at their originally struck LTV, so a shock revalues the collateral while leaving the debt unchanged. The shock lands at **M61 (Y6)**, by which point the credit book has run three years.

| Shock at M61 | Margin calls, USD | Grams liquidated | Peak single month, g | Float at shock, g | Float covers peak? |
|---|---|---|---|---|---|
| −13% | **0** | 0 | 0 | 2,204 | yes |
| −29% | **0** | 0 | 0 | 2,476 | yes |
| **−46%** | **67,584** | **884.7** | **280.3** | **2,940** | **yes** |

**Only the −46% shock triggers anything: USD 67,584 of margin calls and 884.7 g liquidated.** **The float absorbs it entirely** — peak single-month liquidation is 280.3 g against a float of 2,940 g at the shock month, so **the liquidation never reaches the physical market.** This is the float's fifth job, and it is the same argument that makes zero-fee redemption survivable.

⚠ **Why −13% does not margin-call here, and why that does not contradict the corpus.** The corpus's −13% figure is correct **for a Sovereign account drawn to its 80% maximum** — and that is a small cell (954 accounts at Y10, 4.4% of the live book). The model's *realised* book is **Gold-weighted**, and Gold is struck at 50% LTV, so the blended realised LTV sits far below the Sovereign ceiling and a 13% fall passes through without a call. **The two statements describe different populations and both are true. Do not present this as the corpus figure being wrong.**

#### 14.4c Who is exposed — the static analytical ladder

⚠ **This table is an analytical statement, not a scenario result.** For an account struck at each tier's LTV *and drawn to its maximum*, it is the fall needed to reach the 92% margin-call line. It binds only on customers who max out at the top tier. **The "fall to margin call" column is pure arithmetic on the struck LTV and is horizon-independent; the account counts are ten-year figures and will fall on the rebuild** — which makes the exposure smaller, not larger.

| Tier | Struck LTV | Accounts (Y10) | Collateral USD | Drawn at max | Fall to margin call | Within 1σ? |
|---|---|---|---|---|---|---|
| Gold | 50% | 7,955 | 4,930,822 | 443,774 | **−46%** | no |
| Platinum | 65% | 4,739 | 2,937,464 | 343,683 | **−29%** | no |
| **Sovereign** | **80%** | **954** | **591,422** | **85,165** | **−13%** | **YES** |

> *"The ladder only binds on customers who max out at the top tier. **This is the most reassuring fact in the whole design and it should be presented.**"*
>
> ⚠ *"**A 13% gold fall is roughly a one-sigma annual move.** Sovereign borrowers at maximum draw are genuinely exposed, and the design must not pretend otherwise."*

**The exposure is real, small, and mitigated twice.** USD 85,165 of drawn balance at maximum draw, against a 954-account population that is the most disciplined in the book — only the perfect-payer track reaches Sovereign at all — with **two warnings and 14 days** before anything is sold. **The −13% one-sigma sensitivity is the honest headline; the USD 85k it puts at risk is why it is not an emergency.**

⚠ **The caveat that bounds all of the above.** This is a **single-shock path, not a stochastic price process.** It answers *"what happens if gold falls X% in Year 6"* — which is inside the 7-year window — and it cannot answer *"what is the probability of a margin call over the horizon."* The latter needs a price process, which is out of scope here and is recorded as limitation L10 at §3.y.3. For the same reason the two rows below stay open:

| Output | Value |
|---|---|
| Probability of a −13% annual move at σ = 25% | `{{UNFILLED: probability of a −13% annual gold move — not in spine; gold is modelled as a discrete level axis and a discrete shock path, never as a distribution, so no exceedance probability exists}}` |
| Probability-weighted expected exposure | `{{UNFILLED: probability-weighted exposed balance, USD — not in spine; requires the exceedance probability above}}` |

**Three further risk items belonging in this view, none of which is a revenue number:**

| Risk | Model treatment |
|---|---|
| **Stand-in fraud** | Bounded and computable: `exposed_accounts × USD 500 cap × incident_rate`. **The caps make the per-account worst case deterministic; only the incident rate is unknown.** *"An unavoidable, permanent hole in a collateral-backed card programme"* |
| **The self-dealing exposure** | **Not a cost. A compliance requirement.** LBMA fix with zero discretion, disclosed at the draw, sale price and gram count reported. *"Without that, this is the line a regulator or a claimant pulls on"* |
| **The Run book state** | Float breach, settlement-window tier fired, spread cost on the net. See §13.4 |

---

## 15. Corrections owed to Phase 2

v1.0's ten, plus ten new ones from the v2.0 decision record.

| # | Target | Correction |
|---|---|---|
| 1 | Corpus-wide | **Gold price.** Every figure computed at USD 109.31/g must be re-run at F1 = 141.46. Propagates into the float table, the price-gap calculation and the §4.2 spot example (915 g → ~672 g) |
| 2 | `_draft_purchase-structure.md` §2.2 | **Price-gap risk is 0.79%, not 0.36%.** Volatility 25% not 15%, and the higher gold price lengthens the bar fill window from 8.7 to 12.1 days |
| 3 | `_parked_collection-economics-and-minimum-ticket.md` | **The payment rail is a fixed fee per debit, not a 0.30% rate.** Formally retracted. The 0.30% flat treatment must not reappear |
| 4 | Decision 22 | **Persistency at 79%/38% is the wrong comparator on the wrong basis.** Use 55% M13 / 19% M61, by policy count not by premium, adjusted for the absence of surrender penalties, 80C clawbacks and renewal-commissioned agents |
| 5 | Decision 31 | **The launch perimeter is 4.58M, not 3.5–4M.** We were understating our own addressable base by 15–25% |
| 6 | Decision 31 | **Segments must be re-cut by country of residence**, which decision 31 itself instructs and the segment table did not implement |
| 7 | `_draft_referral-system.md` §5.0 | **The self-funding claim was withdrawn, not repaired.** The reward was tested against a 2.15% gross margin that had not paid for price-gap, float or rail |
| 8 | Client's `100 G Business_Model.md` | **The 15% agent commission has no surviving base.** The Algorithmic Growth Fee no longer exists. Transplanted to the entry fee it consumes 88% of Y1 gross margin |
| 9 | Client's custody assumption | **0.8–1.0% custody is not viable and is 3–6× the real cost.** Every major comparator charges holders zero |
| 10 | `_draft_entities-licensing-and-payments.md` | **The USD 75,000 smart contract audit is not a one-off.** VARA mandates an annual tech audit plus one before every new system or product launch |
| **11** | **v1.0 §9 item 6** | **The tenure rebate is retired (decision 44), not merely unsized.** The "0.10–0.75%" is Gold Rewards' range; the "~1.5%" is the superseded prohibited redemption fee. **Strike the solver item** |
| **12** | **v1.0 §0.1 / §6.1 / F5** | **Double-count:** the float cost of capital and the full dealer fabrication premium are charged simultaneously. **They are alternatives under the dealer-carried / own-float fork** |
| **13** | **`_draft_allocation-and-float.md`** | **Every float dollar figure is computed at USD 109.31/g.** Correction 1 propagates: **float capital rises 29.4% at every year.** Y1 ~USD 29k, Y3 ~USD 437k, Y10 ~USD 3.6M, Tradeflow launch ~USD 285k |
| **14** | **`_draft_purchase-structure.md` §4.1 / §4.3** | **Superseded by `_draft_sip-rulebook.md` §1.1 and decision 44 — spot does receive the tier entry-fee discount.** The "flat, top of range" treatment is dead |
| **15** | **v1.0 §3 Layer 3** | **The reduced ticket is hard-coded at USD 20 for all segments.** Should be per-segment: ~50% of prior ticket, floored at 20 |
| **16** | **v1.0 §6.5** | **Stream 5 computes peak drawn and prices it as persistent.** Applying the realised 71-day tenor as S40 = 0.42 **roughly halves the stream** |
| **17** | **v1.0 §7.4 one-off** | **ADGM → DIFC.** Route 2 is settled as DIFC (decision 50; *"taking security breaks the tie decisively toward DIFC"*). The USD 1,900 ADGM SPV line is the wrong vehicle |
| **18** | **`_draft_sip-rulebook.md` §7.1 / §7.2 / §8** | **Carries pre-decision-46 vocabulary** — continuity halving, revival, arrears, "Tenure" as a component. **Should be marked superseded in the corpus itself**, not merely worked around downstream |
| **19** | **`_draft_credit-and-card-infrastructure.md` §7** | **Header says three of five collateral-chain links are open; the table marks two open and three designed.** The table is operative; the header is stale |
| **20** | **`_draft_ics-scoring.md` §7.1** | **Heading reads "Six personas"; the table has nine rows, A–I.** The heading is stale, and the count matters because the build's validation set is nine tests |
| 🆕 **21** | **Decision 31, and correction 5 above** | 🔴 **Correction 5 is itself wrong and must be superseded.** The MEA overseas-Indians table is the wrong instrument: it counts PIO/OCI and historic diaspora, and **omits Bangladeshis and Pakistanis entirely**. National statistics authorities count live visas. **Oman's Indian count is ~515k not 690k; Bahrain's is ~299k not 330k; but Oman's Bangladeshi count alone is 605k.** Rebuild the perimeter from NCSI, LMRA/iGA and sending-government sources (D25, §5.0) |
| 🆕 **22** | **`Aurumix_Project_Charter.md`, and Layer 1's agent channel** | 🔴 **The persona is too narrow. The market is South Asian, not Indian.** Non-Indian South Asians outnumber Indians in Oman outright and match them in the UAE. The charter's "NRI saver" and the Indian insurance-agency channel model both need widening. **This is a client conversation, not a text edit** (D25, §5.0) |
| 🆕 **23** | **`_draft_sip-rulebook.md` §6.2, `_explainer_how-we-take-money.md`** | 🔴 **The lowest-income segment may have no usable payment rail.** Findex's 85.7% UAE account ownership counts **WPS payroll cards with no IBAN**, which cannot carry a mandate or a debit. AANI R2P still needs a real account. **The payment design has never tested itself against the segment the agent channel actually delivers.** Mitigant with a date: CBUAE's Universal Account (D25, §5.4) |
| 🆕 **24** | **Client call agenda item 6b, `_draft_entities-licensing-and-payments.md`** | 🔴 **"UAE, then Bahrain and Oman" has the sequencing backwards.** Bahrain's CBB Crypto-Asset Module binds, treats the token as a security, requires written CBB approval, BD 50,000 paid-up capital, escrow at a CBB-licensed retail bank and a CBB-licensed digital token advisor, **and contains no reverse-solicitation exemption**. Oman has no VASP regime in force and its regulator is the **FSA, not the Central Bank** (D25, §5.3) |
| 🆕 **25** | **Phase 1 competitive set** | **Botim's O Gold is a closer competitor than Liv Gold and appears nowhere in the corpus.** AED 10 minimum, 8.5m UAE users who are precisely our persona, AED 100m+ traded. Also add **CBUAE's stated intent to launch digital savings and investment products for low-income earners within one to two years**, which is the regulator entering the segment (D25, §5.6) |
| 🆕 **26** | **This brief, §3 Layer 4 and §6.1b** | 🔴 **The brief contradicts itself on gross margin before rail.** §6.1's waterfall gives **2.15%** gross retained (audited clean against `C − C(1−f)(1+p)` = USD 1.6125), which nets to **0.87%** after price-gap and float. But §3 Layer 4 and §6.1b both state **0.72%** for the same quantity, implying a 2.00% gross that the exact formula does not produce. **The 0.87% line is the correct one.** ⚠ **It moves the break-even ticket by ~USD 6 (28.7 vs 34.7 at the old premium), so it must be settled before the reference model is rebuilt, not after** |
| 🆕 **27** | **`_draft_allocation-and-float.md`, decision 11, and the open item pricing the exit** | 🔴 **There is no "LBMA approved vault network." LBMA does not approve vaults** — verbatim, Good Delivery List Rules Annex A; the Approved Weighers List covers weighing only. The operative mechanism is **vault manager acceptance discretion**. **Re-cut the open item "do GD bars lose chain-of-integrity status when vaulted outside the approved network" — it is built on a network that does not exist.** Correct framing: **loss of at-sight London acceptance**, not loss of accreditation. Sharpens decision 11 |
| 🆕 **28** | **Decision 26, `_draft_purchase-structure.md`, the ownership construct** | 🔴 **DMCC Tradeflow cannot carry fractional or sub-account customer interests, and the one Dubai tokenised-gold product does not use it as a registry.** "Tradeflow" and "warrant" appear **zero times** in Comtech's binding T&Cs; DMCC's own model is *"each warrant represents a specific item"* and *"legal title remains with the holder of the warrant."* Comtech holds the warrant and grants customers a contractual undivided interest as **agent in possession**. **Decision 26's preference for Tradeflow as the title record needs re-examining.** ✅ **One positive to carry to the client: Comtech's construct is bailment; Aurumix's is a trust, which is materially stronger on insolvency — counsel batch 1 question 2** |
| 🆕 **29** | **`_draft_allocation-and-float.md` §, the fee-ladder justification** | **The premium ladder was one denomination too pessimistic at every rung** (D28). Observed Dubai: 100 g **1.71%**, 1 kg **0.93%**. The model carried 3.00 / 2.00 / 0.75. ⚠ **Also: Dubai's own Good Delivery standard is a 1 kg bar at 995+, not a 400 oz bar. DGD is itself superseded by the UAE Good Delivery standard (Cabinet Resolution 2/16 of 2020).** The ladder's third rung targeted the wrong object; **drop Good Delivery as a rung.** ⚠ **Every gold-price and premium figure in that draft is stale on both counts** |
| 🆕 **30** | **`_draft_purchase-structure.md`, `_draft_allocation-and-float.md`, and this brief §3 Layer 3** | 🔴 **Undesigned and now load-bearing: does redeemed gold return to the float, or go back to the dealer?** D30 charges the fabrication premium on **net new grams**, which is only correct if recycled metal stays in the float. **Nobody has written this down.** It interacts with the buyback mechanics and with the `trust ≥ tokens` invariant. **Settle it before the D30 correction is built** |
| 🆕 **31** | **`_draft_allocation-and-float.md` §, `_parked_collection-economics-and-minimum-ticket.md`, `_explainer_how-we-take-money.md`, `_draft_sip-rulebook.md` §6** | 🔴 **THE ENTRY-FEE BUILD-UP LOSES ITS RAIL TERM** (D31). The build-up is now **premium + price-gap + float CoC + margin**, and the 0.30%-of-contribution rail line comes out. ⚠ **The parked file's entire §2 apparatus — `C_min = R ÷ (f − c)`, the break-even table at AED 1/2/3/5/10.50, and the "no viable collection below USD 118" finding — is RETIRED, not re-run.** With `R = 0` there is no minimum ticket from margin. 🔴 **But do not delete that file: its arithmetic becomes the sizing tool for the pass-through instead of the fee**, i.e. how much the customer is asked for at each rail price. **The SIP rulebook needs a disclosure line: the collection request is `commitment + rail`, and the customer must be told the rail amount before they authorise** |
| 🆕 **32** | **`_draft_referral-system.md` §5.0 and §5.4, `_draft_allocation-and-float.md`** | **The referral payback arithmetic runs on a net margin that has now moved twice.** §5.0 tested the reward against 2.15% gross, was corrected to ~0.85–1.00% net, and D28+D31+D32 move it to **2.79%.** ⚠ **The reward is 1.67% of contribution against a 2.79% margin — it is no longer "roughly double the margin," it is roughly three-fifths of it.** The self-funding claim was withdrawn and should **stay** withdrawn (no programme recovers CAC in six months), but **§5.4's open decision on reward size must be re-taken at 2.79%, and the "quote the range, not a point" instruction in §276 can now be closed** |
| 🆕 **33** | **This brief §5.2, and D25's justification** | ⚠ **The ticket-band structure loses one of its two supporting non-linearities.** D25 built two bands per region to preserve *"both the fixed-rail-cost and the card-spend non-linearities."* **D31 kills the first.** The bands still stand on card spend and on the tier-weighted discount, but **§5.2 currently states a justification that is half false and must be re-worded.** ⚠ **This is a documentation fix, not a re-cut — do not collapse the bands** |
| 🆕 **34** | **`_draft_allocation-and-float.md`, this brief §7.4 and S14, `Aurumix_Process_Maps_Custody_Fee.md`** | 🔴 **CUSTODY SHOULD NOT BE AD VALOREM.** Retrieved DGCX/DCCC vaulting tariffs (via Wayback, the live domain is Cloudflare-walled) price **every** line **per kilogram**: in/out USD 2.00/kg, storage USD 0.40/kg per 7 days, minimum charge at 25 kg. **Nothing is a percentage of value.** Annualised that is ~USD 20.86/kg/yr — **3.24 bp at USD 2,000/oz gold but 1.44 bp at today's price.** ⚠ **A bp-of-AUM custody charge therefore inflates cost as gold rises, against a real charge that does not move.** Re-specify as **per-gram with a floor.** ⚠ **The retrieved tariff is 2007 vintage: the STRUCTURE is the finding, the RATE must not be quoted to the client.** Record in `supporting/_working_dealer-bid-side-and-vaulting-research.md` §4 |
| 🆕 **35** | **This brief, Stream 0's "Dealer two-way spread" driver; `_draft_purchase-structure.md` §5.4** | **THE EMPTY PARAMETER IS NOW FILLED, AND THE BID IS NOT THE ASK RUN BACKWARDS.** Observed on a simultaneous bid/ask pair with a denominator cross-validated two ways: **bid sits at spot −1.50% (1 kg) and −1.60% (100 g)** — i.e. **near-flat across denomination, while the ask premium moves ~194 bp across the same range.** 🔴 **So fabrication cost is paid on the way in and NOT recovered on the way out, and any model that nets the two symmetrically misprices the round trip at both ends of the ladder.** Model input: **1.50% observed, 1.5–3.0% UAE uncertainty band, plan at 2.0%.** ⚠ **Plus a 0.5–4% condition haircut that is ZERO if metal never leaves the vault — which raises the priority of correction 30, not lowers it** |
| 🆕 **36** | **This brief §0.3, §6.1a, §8.1 F4, §16, and D28 itself** | 🔴 **D28's PREMIUM MEASUREMENT FAILED REPLICATION ON 2026-08-20 AND ITS LEVEL MUST BE TREATED AS WITHDRAWN.** Re-running the same-page capture 24 hours later returned 4.14% / 3.37% against the prior day's 1.75% / 0.98%. **Diagnostic: goldtrade.ae's rate page moved 6 bp overnight while its own store moved 241 bp — the two pages share a domain but not a clock.** ⚠ **What survives is the SHAPE: the curve is monotonic on both days and the 1 kg-vs-100 g step held at 0.77–0.78pp, independently corroborated at 1.16–1.74pp on a third source. The denomination ladder is sound; its absolute level is not.** 🔴 **Every figure re-cut at F4 = 1.50% — including §0.3's 0.26pp of headroom — is provisional until a third observation. Do NOT take the fee-fundability reversal to the client on this evidence.** **Method addendum: a same-page pair must also be a same-CLOCK pair; validate by re-fetching and checking both sides moved comparably** |
| 🆕 **37** | **This brief §3 Layer 4, §6.1a, §6.1b, §7.1, §7.5, §11 P&L, F5; `_draft_allocation-and-float.md` entry-fee build-up** | 🔴 **THE FLOAT COST OF CAPITAL LEAVES COGS AND BECOMES A MEMO LINE** (D32). It is an **opportunity cost on equity, not a cash expense**, and §11 currently books it inside COGS — which means stream 1's "net contribution margin" charges a cost the P&L never pays and does not tie to the cash flow. ⚠ **This is an internal-consistency fix as much as an accounting one: §7.6 already states the rule** — *"report the escalator as an opportunity cost, not a P&L line… as a memo line"* — **and F5 was the single place the brief broke it.** 🔴 **What must NOT be inferred: that the float is free.** The **principal** is unaffected — USD 29k at Y1 to USD 3.6M at Y10, on the balance sheet, inside peak funding. ⚠ **Restore the charge as a real financing expense if the float is ever debt-funded; add a `FLOAT_DEBT_FUNDED` switch** |
| 🆕 **38** | **This brief §0.3, §14 break-even, §13.5 tornado, and any client-facing summary** | 🔴 **THE CUMULATIVE-RECLASSIFICATION RISK, recorded so it is not lost.** In one day D31 and D32 removed two of the four terms in `c`, and the minimum viable entry fee fell **3.07% → 2.74% → 2.26%** with **nothing changing in the business.** Each step is individually defensible; **the sequence dissolved §0.3, a finding present in every version of this brief, by re-attribution alone.** ⚠ **Compounding this, the third term — the fabrication premium — failed replication the same day (correction 36).** 🔴 **Before any of this reaches the client: adversarially re-check the two surviving cost terms, re-observe F4, and state the fee reversal as conditional. The break-even and tornado outputs must ALL be re-run — S1 leaves the tornado entirely and F5 leaves the margin, so the existing rankings are stale in two places at once** |

| 🆕 **39** | **This brief §5.1, §6.1b, Layer 1, Layer 2, the L-table, and `_draft_sip-spot-and-ics.md`** | 🔴 **SPOT IS MODELLED AS A BEHAVIOUR OF SIP ACCOUNTS, NOT AS A CUSTOMER** (D35, §5.9). Stream 1b drives spot off `live_accounts`, S45 is denominated *"% of live accounts/yr"*, and §6.1b states *"there is no independent spot ceiling"*, so **no account can exist before it starts a SIP.** ⚠ **The §5.1 funnel compounds it:** two of its three filters (IBAN at 0.57, USD 20/month at 0.40) are recurring-mandate tests applied under the claim *"One method now applies to every row"*, while §6.1b states spot needs neither (*"one push or bank transfer"*). **The two facts sit on adjacent pages and were never joined.** 🔴 **The defect is not the level (spot is already 49.6% of Y7 inflow) but that spot is analytically bounded by the SIP book at every parameter setting.** **Flagged nowhere: not in L1–L11, corrections 1–38, §3.y.2 or §16. Correction 22 audited the persona on nationality and did not examine the product axis.** **Resolution specified at §5.9. Adds S56–S59 and re-labels the 165,750 invariant as the SIP ceiling** |
| 🆕 **40** | **This brief §5.6, and correction 25** | ⚠ **THE BOTIM FIGURES ARE STALE AND THE MOST RELEVANT ONE IS USED BACKWARDS.** Current disclosure is **128,000 trades and AED 100m+ since the Aug 2025 launch** (stated at the Feb 2026 silver launch), implying **~AED 780 per trade** against the AED 700 carried at §5.6. 🔴 **More important than the level: §5.6 cites the ~6% conversion as a DISCOUNT to apply to a SIP base** (*"a recurring debit converts to a materially lower number"*). **Botim has no recurring purchase facility at all**, verified against its own gold FAQ, product page and all launch coverage, **so its buyers are one-off buyers by construction and the 6% applies to the SPOT lane at full strength, undiscounted** (§5.9.4). ⚠ **Three further facts belong in the competitive set:** Botim is a **distribution front-end, not the gold principal** (the principal is **OGOLD Precious Metals Trading LLC**, DMCC); **OGold's own app carries a full SIP from AED 2** which Botim has not surfaced; and OGold's binding T&Cs say metal *"may be held in pooled custody arrangements"* against marketing that says "fully allocated", **making allocated segregated metal a checkable differentiator.** ⚠ **Registry-first gap: no register entry or licence number was retrieved for either entity** |

---

## 16. Open questions and defaults

| Question | Impact if wrong | Default used | Priority |
|---|---|---|---|
| **AANI Request to Pay cost per collection** | 🔴 **Decides the sign of stream 1's margin.** ±USD 1.11/collection | S1 = USD 0.25 | **CRITICAL — the most valuable unknown number in the engagement** |
| **Programme manager interchange share** | 🔴 Sizes the largest stream directly | S3 = 72%, floor 36% | **CRITICAL — take 36% into the sponsor conversation as the walk-away** |
| 🆕 **Dealer fabrication premium and spread** | Sets 70% of stream 1's cost base | **F4 = 1.50% (100 g), 0.95% (1 kg)** | 🆕 **DOWNGRADED from CRITICAL to MODERATE** (D28). Measured on a same-page dealer pair rather than guessed: 100 g at +1.71%, 1 kg at +0.93%, less a published 25 bp bulk gradient. ⚠ **What remains open is the genuine 10–50 bar tier and whether the deal strikes on the fix or the dealer's own tick — worth 20–30 bp. Still needs the dealer, but no longer sets the sign of the answer** |
| 🆕 **The two-way spread on buyback** | 🔴 **Prices every exit, and stream 0 has no offsetting revenue** | Not modelled separately | 🔴 **CRITICAL, and it replaces the premium at the top of the dealer agenda.** The premium is now observed; **the bid side is not, and it is a separate commitment from carrying inventory.** Neither PAXG nor XAUT accepts a repurchase obligation at all. ⚠ **The zero-fee-exit promise rests entirely on this number** |
| **Prepaid versus credit** | **USD 2,304,921 of Y10 revenue and USD 7,254,180 of cumulative net profit** | Credit | **CRITICAL — "not a product choice, it is the business model." Must be settled before the September build** |
| **Launch date** | Shifts every date in the model | M1 = Jan 2027 | **HIGH — no launch date exists in any client document** |
| 🔴 **Does a lapsed customer keep the card and the facility?** | **Determines whether the majority of revenue decays with persistency or is immune to it** | `LAPSED_KEEPS_CARD` = ON | **CRITICAL — nobody has decided, and v1.0 silently assumes immunity by never asking** |
| 🔴 **§10 sub-decision 2: does a compliance-forced exit drive Retention to zero?** | **Destroys the tier distribution on the segment most likely to be forced out** | OFF (current design) | **HIGH — left open at Abdur's instruction 2026-08-13. Report the S5 tier delta as the client's decision cost** |
| 🔴 **"Equal value" under III.E.1 — full prevailing value or realisable value?** | *"The difference is the entire two-way spread and it decides who absorbs it on every exit"* | Full prevailing value (Aurumix absorbs) | **HIGH — counsel** |
| 🔴 **Is an enforcement sale a "redemption" under III.E.4?** | **Recovery costs in stream 5 become unchargeable.** Aurumix is precisely the exposed party | Aurumix recovery share = **0%** | **HIGH — counsel. Modelling it at zero is the defensible position** |
| 🔴 **Does a single-purpose DIFC trustee company need a DFSA trust licence?** | *"A cost question and we cannot quote the client a number without it"* | Exempt reading; **visible placeholder, not an implied zero** | **HIGH — verify at DFSA primary text. Current source is a rulebook mirror, Medium confidence** |
| **Settlement-window thresholds (small / medium / large)** | Decides when a redemption requires a dealer sale | **Deliberately unset** — they depend on float size, which depends on the dealer | **MEDIUM — carry the tiers as structure, the thresholds as inputs** |
| **FEMA s.6(4): may a returning NRI keep contributing from funds acquired abroad?** | Sizes how often the regulatory-block state fires | Assume the block fires; needs a repatriation rate, **which nothing in the corpus sizes** | **MEDIUM — counsel. If counsel says yes, the state simply fires less often** |
| **QFZP eligibility** | **USD 0 at Base** — no year is profitable, so no tax is booked and the relief has nothing to relieve. v1.0's ~USD 220k/yr assumes a profitable Y10 the model does not reach | **Assume NOT a QFZP; tax at 9%** | **LOW at Base, MEDIUM in the profitable scenarios — the conservative call is clearly correct and the risk is one-directional upside** |
| **VAT: is the entry fee a supply of services or part of a supply of gold?** | May make the resident/non-resident split irrelevant for stream 1 | 5% resident / 0% non-resident, haircut 20% for input-VAT drag | **MEDIUM — three separate corpus files flag it. Tax opinion, not a modelling assumption** |
| **Can allocated gold inventory sit inside the AED 1.5m VARA minimum?** | At Y1 immaterial; **at Y10 the float is USD 3.6m against the minimum** | Assume it cannot; the two stack | **MEDIUM — counsel** |
| **Can the 2%-of-Reserve-Assets escalator bite where no Reserve Assets exist?** | *"Potentially several million dollars"* | `OPTION_B` = OFF | **MEDIUM — counsel. Under Option A the row is flat, which is the point** |
| **The empty lever: spot and SIP now differ on ONE lever, not two** | Decides whether the differentiation question has money behind it | Accept one lever; **the model's contribution is sizing the thing being argued about** | **MEDIUM — spot is 39.6% of total inflow at Y5 (USD 2,929,673 of USD 7,398,528), rising to 45.2% by Y10. That sizes the stakes; then hand the client the decision** |
| **Family plan attach rate** | Scales stream 3 linearly | S11 = 20% | **MEDIUM — nothing is stated anywhere in the corpus** |
| **Tradeflow: 100 g or 1 kg at launch?** | **A 10× launch capital step**, ~USD 29k → ~USD 285k | 100 g | **MEDIUM — a real trade-off and a client decision** |
| **Is the model under-scoped on VARA activities?** | Broker-Dealer and VA Transfer & Settlement each add AED 80,000–200,000/yr | Category 1 Issuance only | **MEDIUM — confirm with VARA before the cost base locks** |
| **Reserve attestation cost** | *"The single biggest unpriced line"* | Included in the audit block at judgement | **MEDIUM — get a Bureau Veritas quote** |
| **Referral reward size** | Shape settled; the 30% is a placeholder | F17 = 30% | **MEDIUM — solver item 3** |
| **VARA approval timeline** | Shifts M1 and everything after it | Six to nine months minimum | **LOW to model, HIGH to plan — VARA publishes no approval timeline** |

---

## 17. Data and proxy recommendations

### 17.1 Market-sizing sources

| Data needed | Source | How it anchors the model |
|---|---|---|
| UAE / Oman / Bahrain Indian diaspora counts | MEA (Ministry of External Affairs, India) 2025 population tables | §5's 4.58M perimeter, replacing decision 31's understated 3.5–4M |
| Indian life insurance persistency by policy count | IRDAI Handbook on Indian Insurance Statistics 2024-25, Table 28 — `irdai.gov.in` | §0.5's M13–M61 curve, **by policy count not by premium**, which is the right basis for a low-ticket product |
| SIP account counts, contributions and average ticket | AMFI monthly data — `amfiindia.com` | S5 sizing: 106.3m contributing SIP accounts at ₹3,008/month = USD 34, **which sits squarely inside the USD 20–75 band** |
| Gold ETF folio counts | AMFI, Apr 2026 | The 12.48m Indians holding gold as a **financial** instrument — the S5 serviceable base |
| Visa UAE interchange reimbursement fee schedule | Visa UAE IRF, effective 18 Oct 2025 | **F12, primary. The only High-confidence rate in the card block** |
| CBUAE Notice 1998/2024 | Central Bank of the UAE | The 1.00% debit and prepaid cap, which sizes the `PREPAID_VS_CREDIT` switch |
| DMCC company setup and licence schedule | `dmcc.ae` | The Corporate opex block, **High confidence, DMCC's own schedule** |
| VARA rulebooks (Company, Technology, Issuance) | `rulebooks.vara.ae` | F14 supervision fee, the annual tech audit requirement, the Part VII.A wind-down obligation, **and the Annex 2 III.E.4 no-fee-on-redemption rule** |
| Sumsub pricing | `sumsub.com/pricing` | **F16, primary. USD 299/month + USD 1.85/check, binding below 162 checks/month** |
| Stripe Issuing pricing | `stripe.com/issuing/pricing` | **F24, the USD 0.10/txn processor fee** — the input that closes v1.0's largest open card gap |
| Federal Decree-Law No. 47 of 2022 | UAE Ministry of Finance | F33 (9% rate, AED 375,000 threshold) and **F34 (Article 37, 75% loss-utilisation cap)** |
| DGCX vault tariff | DGCX published schedule | The USD 0.10/kg/day rate **and the USD 25/day minimum that binds below ~250 kg** |
| Manappuram and Muthoot quarterly reporting | Company filings | S40's 71-day realised tenor and the 57% realised LTV — **the two figures that halve stream 5** |
| Finance House gold loan Key Facts Statement | Finance House UAE | **F28's 1% processing fee — the only fee-head gross rate with a real UAE anchor**, plus the bullet-vs-EMI 1.83× interest comparison |
| Emirates Money gold loan terms | Emirates Money UAE | The 9%-reducing end of the pricing corridor at 80% LTV |
| Liv Gold / RAKBANK gold account terms | Emirates NBD, RAKBANK | **The incumbent nobody had found.** AED 15 minimum against our USD 20 |
| SafeGold financials | Company filings / Indian registry | **The 0.03% EBITDA margin that governs stream 6's design** |
| PAXG, XAUT, Kinesis, Comtech terms | Issuer terms pages | The zero-storage-fee competitive fact, **and PAXG's dilutive-issuance storage-fee reservation** |
| SEBI caution on digital gold, 8 Nov 2025 | `sebi.gov.in` | The S5 distribution constraint, and the positioning argument that **a VARA licence is the answer to the SEBI notice** |
| BullionVault / GoldMoney / SGPMX storage rates | Provider pricing pages | The verified 0.12–0.40% allocated storage band that vindicates our internal estimate |

### 17.2 Post-Launch Validation

**What to instrument from M1, what each metric validates, and what it should read.** This is what turns the model from a forecast into a calibrated instrument.

| Metric to track | Validates assumption ID | Target value |
|---|---|---|
| **Share of month-6 cohort that has gated** | **D4 gate-arrival distribution, S27** | 🔴 **The single highest-value validation.** If materially above the archetype-implied share, the mix is too pessimistic; if below, the consecutive gate is costing more than modelled |
| Monthly contribution success rate, by cohort month | S27 archetype payment probabilities | Cohort-weighted ~0.83 at M1–M6, rising as early lapsers exhaust |
| **M13 cohort survival** | **S2, S27** | **55%.** The single anchor the whole archetype mix is fitted to |
| M25 / M37 cohort survival | S27 background hazard | 40% / 30%. **These two calibrate the background hazard, not the archetype weights** |
| **Share of lapses that are involuntary** | `_draft_sip-rulebook.md` §7.3 | **20–40%, base 30%.** Requires logging delivery and open events, which is itself a build requirement |
| Reduction-versus-lapse split | **S28** | 33% of affordability-driven lapse events divert to REDUCED |
| **Observed reduced ticket** | **S29** | ~50% of prior ticket, floored at 20. **If it lands at the floor for S1, v1.0's treatment was right and S29 is wrong** |
| Rail cost per collection, actual | **S1** | 🔴 **USD 0.25 or the model changes sign on stream 1.** Instrument from the first collection |
| Spot attach rate and average ticket | **S45, S46** | 14% of live accounts/yr at USD 620. **Currently zero in v1.0 — any observation is new information** |
| Share of spot volume in the two festival windows | S47, S52a | ~45% |
| **Self-custody withdrawal distribution** | **S31** | **Track the distribution, not the aggregate.** The number that matters is the share above the 30% kink: 14% at Base |
| Redemption rate, and the lapsed-versus-contributing split | **S32, S33** | 8%/yr, with lapsed holders at 2.2× |
| **Net flow sign, monthly** | Stream 0 | **Positive in every month. The first negative month is when the spread cost becomes real** |
| Effective PM share, per tier, from the first settlement file | **S3, F24** | 🔴 **Gold ~43% against a contracted 55%.** If the settlement file shows the headline rate, the per-txn fee is being billed elsewhere and must be found |
| Average transaction size by tier | F23 | AED 185 / 240 / 310 |
| Card activation rate | S5 | 65%, **and use the High case if issuance is restricted to funded balances** |
| **ATM draw distribution** | **S35** | **Six buckets, not a mean.** 60% below AED 500; only ~3% above AED 3,000 |
| Foreign spend share, by month | **S34, S53** | 34% annual mean, **55–60% in June–August** |
| Card fraud loss | S39 | 9 bps. **A fresh BIN attracts enumeration testing in the first months** |
| Realised draw tenor | **S40** | **71 days.** If it runs materially longer, stream 5 is understated by up to 2.4× |
| Draw events per active borrower per year | S41 | 2.1. **Moves with S40 — validate them together** |
| Credit take-up among eligible | S8 | 18% |
| Agent accounts per month, by tenure month | **S12, S17** | 4/month at full ramp; 6 months to reach it |
| **Agent 12-month attrition** | **S18** | **45%.** Missing from T7 entirely; the recruit flow is 15–20% of steady-state output |
| Referral rate per qualified referrer | S19 | 0.45/yr. **Right-skewed — track the mean and the tail separately** |
| Effective CAC against monthly spend | **S25** | **Plot the curve, not the point.** At USD 60k/month spend, USD 162 not USD 120 |
| Family plan attach rate | S11 | 20%. **Nothing in the corpus predicts this; the first month of data is the first evidence that exists** |
| Partner AUM ramp, per partner from its own go-live | S43 | 8% at M6, 25% at M12 of that partner's clock |
| **Y1 exit run-rate against Y1 average opex** | **S48** | **1.40×. If the exit rate is at the average, the hire plan slipped** |

---

## 18. Data provenance and confirmed negatives

**Confirmed negatives are findings, not gaps.** Each one below represents a completed search that returned nothing, and each is recorded so it is not re-searched and not silently filled with a plausible number.

| # | What does not exist | Consequence for the model |
|---|---|---|
| 1 | **No UAE or MENA programme-manager interchange split is published anywhere.** Confirmed across two independent research passes | S3 is triangulated from Marqeta's 10-K take rate and the Polymath BIN-sponsorship benchmark, bounding 55–85%. **The single largest input uncertainty in the model** |
| 2 | **CBUAE collects BIN-level card data and publishes none** | No official UAE per-card spend figure exists. S4 rests on an expat survey mean and the Kinesis cap |
| 3 | **No cross-border interchange rate is published for the UAE** | The model carries domestic only and is **conservative by an unknown margin on stream 2**, while S34 correctly sizes the same exposure on stream 4. The asymmetry is flagged, not fixed |
| 4 | **No named primary source publishes card activation or a 12-month dormancy curve for any fintech programme** | S5 is triangulated from PULSE (68.2%) and Monzo (68%), both mature-portfolio equilibrium rates rather than new-cohort activation |
| 5 | **No UAE issuer fraud rate is published** | S39 rests on Visa's published global average of ~8 bps, adjusted upward for a new BIN |
| 6 | **No UAE BIN-sponsorship price list is published** | F27's structure is well-attested; its quantum is a judgement call |
| 7 | **No monthly-versus-annual persistency split is published anywhere in Indian insurance data** | IRDAI's own definition requires **13 consecutive monthly payments** to count as 13-month persistent, against 2 annual payments, so **a blended published figure structurally overstates what a monthly product achieves.** This is one of the three adjustments producing §0.5's recommendation |
| 8 | **No provider publishes multi-decade AML screening terms** | The stream 3 monitoring tail — 20 to 40 years at USD 0.36/name/year, roughly USD 7–14 undiscounted — is extrapolated from annual pricing |
| 9 | **No published gold-savings propensity filter exists for any diaspora population** | §5's ~474,000 addressable base rests on it, and **it is the weakest link in the entire sizing.** S22 then multiplies a Low-confidence number by another Low-confidence number |
| 10 | **No published channel-mix data exists for any comparable product** | S16 is judgement, anchored on three corpus facts about how each channel reaches people |
| 11 | **No published CAC benchmark exists for any UAE gold or savings product** | S15 and the S25 curve are both judgement. The functional form is defensible; the constants are not |
| 12 | **No insurer or SIP platform publishes a downgrade-versus-lapse split** | S28 is set at v1.0's own illustrative third, deliberately, so v2.0 does not silently invent a different number |
| 13 | **No source splits card spend by loyalty tier** | S38's ratios are ours; only the normalisation arithmetic is checkable |
| 14 | **No issuer discloses what a reserve attestation costs** | Kinesis uses Bureau Veritas biannually and Paxos uses KPMG monthly — **the cadence is confirmed market-normal, the price is not.** *"The single biggest unpriced line"* |
| 15 | **The tenure rebate has no published sizing anywhere in the corpus** | Moot — the mechanism is retired (D8). Recorded so the search is not repeated |
| **16** | 🔴 **No published source decomposes a savings-product or insurance lapse curve into payment-behaviour archetypes** | **New at v2.0.** Aggregate curves are published in quantity (IRDAI, AMFI); **the behavioural decomposition underneath them is published by nobody.** The S27 archetype table is a **construction fitted to a researched aggregate and must be labelled as one** — Medium confidence on the aggregate it reproduces, **Low on the decomposition** |

**What this means for how the model is presented.** Sixteen confirmed negatives concentrated in the behavioural and card-economics blocks, against High-confidence primary sources in the regulatory and rate blocks. **The model is well-sourced where the rules are and thinly sourced where the behaviour is** — which is the honest shape of a pre-launch model, and it should be said once, plainly, rather than smoothed over by presenting every parameter in the same typeface.

**Verified clean under audit and carried forward unchanged:** the §0.1 fee waterfall (the fabrication premium is on the correct base; `C − C(1−f)(1+p)` returns the identical USD 1.6125); the §0.2 rail equation and both rail cases; **every ICS constant** against `_draft_ics-scoring.md`; the 36% PM-share floor and its arithmetic (0.75 ÷ 2.10 = 35.7%); the VARA III.E.4 quote, verbatim and correctly located in Annex 2 Part III.E clause 4; and **all ten cited decision numbers — no misattribution, which is the error class most expected and it is clean.**

---

## 19. Glossary and notation key

| Term | Meaning |
|---|---|
| **AURX** | The token. 1 AURX = 1 gram of allocated physical gold |
| **ARVA** | Asset-Referenced Virtual Asset — the VARA category Aurumix is licensed under |
| **ICS** | Investor Conviction Score. `MAX(25, MIN(Record, Standing) × Retention)` once gated |
| **Record** | The tenure component. Rises with `Months`, **never falls, for any reason** |
| **Standing** | The recency component. `(100/12) × Recent`. Rises and falls |
| **Retention** | The holding multiplier. 1.000 up to 30% sold; falls linearly to 0 at 100% sold. **A multiplier with veto power, not a gate** |
| **Months** | Counted periods since the qualifying run began. Starts at 6 on gate day |
| **Recent** | Counted periods in the trailing **12 countable** months (0–12) |
| **Sold** | `1 − grams_now ÷ (grams_12_countable_ago + grams_acquired_since)` |
| **Countable month** | A month that is not frozen by a regulatory block. **Frozen months are skipped entirely and the window extends** |
| **The gate / Confirmed SIP** | Six **consecutive** qualifying contributions. Everybody opens at exactly Silver, whether the run was months 1–6 or 9–14 |
| **`run_length`** | The pre-gate counter, 0–6. **+1 on a counted period, RESET to 0 on a miss, FROZEN during a regulatory block** |
| **Never-gated** | An account that never completes six in a row. **Pays the full undiscounted fee, holds gold, consumes zero benefits forever.** Persona H |
| **Tier** | No tier / Silver 25 / Gold 50 / Platinum 75 / Sovereign 100 |
| **Sovereign** | The top tier. **Monthly-recomputed, never absorbing** — requires Record 100 AND Recent 12 AND Sold ≤ 30% simultaneously. *"Rented by conduct, never owned"* |
| **Archetype** | One of five deterministic payment-behaviour tracks (S27) into which every cohort is split |
| **Background hazard** | Voluntary exit unrelated to payment ability, applied across all archetypes. **Roughly half of terminal attrition** |
| **SIP** | Systematic Investment Plan. The scheduled monthly contribution lane |
| **Spot** | A one-off purchase. **Same gold, same fix, same tier discount; earns no ICS; counts in Retention on both sides** |
| **Reduction** | Cutting the contribution. **Free, instant and unscored.** A delay state, not an exit |
| **Redemption** | Gold → cash. **No fee permitted (III.E.4).** Dealer spread on **net** outflow only |
| **Self-custody withdrawal** | Gold → customer wallet. Gas only. **Hits `Sold` identically to a redemption** |
| **Lapse** | Stops paying. **The balance is unaffected.** Not an exit from AUM |
| **Leakage** | Self-custody withdrawal as a share of AUM. **Modelled as the S31 distribution, never as a rate** |
| **The float** | Aurumix's working inventory of grams. **Five jobs**: buys the wholesale price, absorbs inflow lumpiness, warehouses net redemption outflow, absorbs large spot orders, absorbs margin-call liquidations |
| 🆕 **Bar denomination** | **100 g → 1 kg. Good Delivery retired as a rung** (D28) — Dubai's own Good Delivery standard is a 1 kg bar, not a 400 oz bar, so the third rung targeted the wrong object. **The margin dial: float size unlocks bar size, bar size sets the fabrication premium** |
| 🆕 **Fabrication premium** | The dealer's charge above the fix. 🆕 **OBSERVED in Dubai on a same-page dealer pair: 9.75% at 1 g, 3.07% at 10 g, 1.71% at 100 g, 0.93% at 1 kg** (D28). Modelled at **1.50 / 0.95** after a published 25 bp bulk gradient |
| **Price-gap risk** | The 1σ gold move over the bar fill window, carried by whoever owns the float |
| **The rail** | The payment collection mechanism. **A fixed fee per event, which is why margin is non-linear in ticket size** |
| **PM share** | The programme manager's retained share of gross interchange. **Floor 36%** |
| **Effective PM share** | The PM share **after** the per-transaction processor fee. **Materially below the contracted share on small tickets** |
| **Peak drawn** | The maximum permitted drawn balance. **Not what the borrower holds** |
| **Average drawn** | `peak_drawn × S40`. **What the borrower actually holds, and what earns interest** |
| **Vintage (credit)** | A drawn balance carried at the LTV it was **struck** at, not at the current tier's |
| **Stand-in** | Processor Commando Mode or network STIP. **Approves transactions with no collateral check at all.** A permanent, unclosable hole |
| **Book state** | Growing / Flat / Shrinking / Run. **A first-class scenario axis, because the redemption cost is zero in the first two** |
| **`{{SPINE: …}}`** | A model output not yet computed. **Never a v1.0 figure** |
| **CITED / DERIVED / TRIANGULATED / CLIENT INPUT / ASSUMPTION** | The five source categories, audited at §8.5 |
| **⚠** | A caution: something that is true and easy to get wrong |
| **🔴** | A finding or open item that changes a decision, not just a number |

---

## 20. Build sequence

### 20.1 Pre-build sign-off checklist

**Do not open Excel until every one of these is signed off.** Each maps to a section of this brief, and each is a decision the build cannot proceed without.

| # | Item | Signed off by | Where |
|---|---|---|---|
| 1 | **The twelve layers of §3** — especially the lifecycle curves, the convolution and the live gate engine | Abdur | §3 |
| 2 | **The acyclicity proof and the two resolved circularities**, including the fourth non-circularity at the annual block | Modeller | §3.x |
| **3** | 🔴 **29 periods, 24 monthly + 5 annual, 7-year horizon** (D21) — **and the M8 / M18 / M20 argument for why 24 monthly columns is sufficient** | **Client — taken. Not open** | §1 |
| **3a** | 🔴 **The lifecycle table stays monthly to M84 while the Model sheet is 29 columns.** These are different sheets with different indices and the distinction is load-bearing | Modeller | §1, §10.1 |
| **3b** | 🔴 **The score collapse** (D22): tenure→tier lookup plus one heavy-seller haircut; the gate, survival and persona H stay live; **the full ICS formula and the nine personas are demoted to validation and must still pass**; **the 5% safety gate reverts the collapse if it fails** | **Client — taken. Not open** | §3 Layer 5 |
| **3c** | 🔴 **Cohorts are a convolution. The workbook must not contain a cohort triangle** (D23). Segments scale the curves; later-activating segments offset the acquisition vector | **Client — taken. Not open** | §3 Layer 2 |
| **3d** | **B2B and credit activate at the start of the annual block (Y3), not as a stub month at M24** | Modeller | §4, §10.5 |
| 4 | 🆕 **Five visible sheets and five hidden working sheets** (D26), the logical execution order, **the by-name dependency test replacing the tab-position one**, and that **ICS Validation is a leaf** | **Abdur — taken 2026-08-19. Not open** | §1.1, §3.x.1, §12 |
| 4a | 🆕 **Opex and P&L are a row band on Model, not a sheet. Checks hides and its master flag is mirrored to Cover as a link** | **Abdur — taken 2026-08-19. Not open** | §1.1, §12 |
| 5 | **The archetype weights and the background hazard** as the calibration starting point, not settled values | Abdur | §3 Layer 5e |
| 6 | **Spot is in scope** and is a sub-stream of 1, not a seventh stream | Abdur | §6 |
| 7 | **Stream 0 exists** and there is no offsetting revenue | Abdur | §6 |
| 8 | **The solver is seven items, not eight**, and item 1's answer may be zero | Abdur | §9 |
| **9** | **The promoted outputs replace the investor-count headline — and output 3 is now a shape, not a level.** Break-even and peak funding both fall outside the horizon and are not to be built on | Abdur | §14, §0 footnote |
| 10 | **Every binary switch's default** | Abdur | §13.3 |
| 11 | **The placeholder convention**: no v1.0 figure may occupy a `{{SPINE}}` slot | Modeller | §0 |
| 12 | **The Assumptions indirection rule**: no numeric literals in formulas | Modeller | §12 |
| **13** | ⚠ **Every output figure in this brief is from the v2.0 ten-year run and is re-cut on the rebuild.** Sign-off is on the architecture, not on the levels | Abdur | Front matter, §0 |

### 20.2 Build sequence

| Step | Build | Verify before proceeding |
|---|---|---|
| **1** | **Assumptions and Scenario Parameters.** All 101 parameters with source category, source, confidence and sheet location. Named ranges for every one | Every named range resolves. The scenario canary reads Base cleanly |
| **2** | **Time Series.** **29 period headers (24 monthly + 5 annual)**, all activation flags, the three seasonality vectors, the fee and denomination ladders, opex interpolation, float sizing | **Check 9: both seasonality vectors sum to exactly 12.000.** Check 11: the denomination latch is monotone. **Verify credit and B2B are flagged at the start of the annual block, not at M24** |
| **3** | 🔴 **Lifecycle Curves, ONE archetype, monthly to M84.** Get the six-state roll-forward and the run-of-6 gate solve right on a single curve before replicating. **This is the build's foundation and everything downstream reads it** | **Check 1 on that one curve.** States sum to 1.000 at every `m`. `alive` monotone non-increasing |
| **4** | **Replicate to all five archetypes.** 5 curves × ~92 rows × 84 columns | **Check 1 across all five.** Weighted M13 survival lands at 54.7% ± 1pp against the §0.5 target of 55%. **Weighted gate arrival lands at M8.1 and ever-gate at 53.5%** |
| **5** | **The tenure→tier lookup on each curve.** Gold at gate+12, Platinum at gate+36, **the alternating-misser Gold cap** | **Verify the archetype cap overrides the generic ladder.** A blended lookup here is the D2 error returning (§3 Layer 5c) |
| **6** | **Acquisition sheet.** Channel volume, S16 mix, saturation, and **the acquisition vector as a clean rectangle** — with S4/S5/S6 as leading zeros, not as new curves | Vector ties to cumulative-ever-acquired. **No segment has its own curve** |
| **7** | 🔴 **THE CONVOLUTION, on one series, with the impulse test.** Build `alive` first and nothing else | 🔴 **Check 14: for an acquisition vector of `(1,0,0,…)`, the convolved book at period `t` equals `curve(m=t)` exactly, for every `t`.** **Do not build a second series until this passes.** A convolution built backwards runs, reconciles and is wrong (§10.4 Pattern 1) |
| **8** | **Replicate the convolution to all series and all segments.** Segment scalars on ticket and card spend only | **Check 1 book conservation per segment.** Check 4: nothing negative |
| **9** | **ICS Validation sheet.** The full ICS formula, the nine personas, **and the 5% collapse delta** | 🔴 **Personas H and I return the corpus's stated values.** **Check 12: all nine pass.** **Verify the exact-fraction test — `100/12`, not `8.3333`.** **Check 16: nothing on the Model sheet references this sheet** |
| **10** | 🔴 **Check 15, the 5% collapse-safety gate, under Base** | 🔴 **Max annual stream-2 delta ≤ 5% of gross profit. If it fails, STOP — the collapse is unsafe and must be reverted before any further build** (§3 Layer 5d) |
| **11** | **Model: streams 1a and 1b, and the AUM stock.** The two inflow lanes and the stock-and-flow | **Check 3: grams reconcile every period.** Check 4: nothing negative. **Verify spot margin exceeds SIP margin per ticket, at both rail cases** |
| **12** | **Model: stream 0 and the net-flow term** | **Spread cost is exactly zero in every growing month.** Verify against the four book states |
| **13** | **Model: streams 2 and 4, on the flat Gold rate, with the per-txn fee and the ATM distribution** | **Check 7: nothing before M18.** Verify the effective-PM-share row: ~43% at the Conservative contracted 55%. **Verify the ATM distribution returns non-zero where the mean returns zero** |
| **14** | **Model: streams 3, 5 and 6.** Credit vintaged by struck LTV; partners on their own clocks | **Check 7: streams 5 and 6 are zero at M24 and first non-zero at Y3 — no stub month.** Verify stream 5 average drawn = peak × 0.42. Verify stream 6 reconciles to S13 within ~5% |
| **15** | **Model: benefit costs, including the Gold Rewards cap** | **Check 5: the cap never goes negative.** Verify the launch-year ladder cost is one 0.4pp Silver discount |
| **16** | 🆕 **Model band 2: opex and P&L, through EBITDA** (D26 — a row band on Model, not a separate sheet) | Verify the log-linear interpolation reproduces the §7.4 year table, and that the Marketing plug ties Y3 and **Y7** to the anchors, **re-cut from the published Y3/Y10 pair.** **Verify the band banner and page break sit between the revenue and opex bands** |
| **17** | **Tax, with the 75% cap** | **Verify the mechanism on a synthetic profitable year**, since no modelled year is profitable. Verify tax writes only in FY-end months |
| **18** | **Cash and funding.** Working capital, cumulative cash, the within-horizon trough | **Check 6: the acquisition ceiling is never breached, in any period, with the lag one month in the monthly block and one year in the annual block.** ⚠ **Label the trough as a within-horizon minimum, never as peak funding** (§14) |
| **19** | **Extend to the annual block, Y3–Y7** | **Check 13: all four M24/Y3 seam tests**, including the decomposition test that each annual column is twelve monthly convolutions. Revenue continuity within ±15%, excluding streams 5 and 6 at Y3 |
| **20** | **Summary, unit economics and the break-even views** | Verify LTV:CAC populates for every channel × segment cell, **including the loss-making ones — those are the answer, not an error.** Verify the diverging-curves chart renders |
| **21** | **Scenario architecture: all three layers plus the ten binary switches** | **Check 8: the canary distinguishes Base from CUSTOM.** Verify `INDIA_ENABLED = OFF` moves **both** S5 and stream 6. 🔴 **Re-run check 15 under Aggressive and Conservative — an Aggressive archetype mix enriches the top of the ladder and is the most likely to trip the gate** |
| **22** | **Checks sheet: all sixteen** | 🔴 **Row 3 reads TRUE under Base, Aggressive and Conservative. The build does not ship otherwise** |
| **25** | 🆕 **PRESENTATION PASS, LAST (D26).** Mirror the Checks master flag to Cover as a **link**; write the §3.x.1 logical order and the sheet map onto Cover; then **hide Time Series, Lifecycle Curves, Acquisition, ICS Validation and Checks** | 🔴 **Run every check again after hiding.** **Confirm the Cover flag is a formula and not a typed TRUE** (§3.x.4). **Confirm five sheets visible in the standard order and five hidden.** ⚠ **Never hide a sheet before its checks pass** |
| **23** | **Solvers.** Items 1–7 in the §9.4 order, with 3 and 4 solved jointly | Verify item 1 against the possible zero-uplift answer. Verify the 3/4 frontier at both rail cases |
| **24** | **Tornados, both of them** | Verify the two rankings **differ.** If they are identical, the funding tornado is not reading the cash rows. **Reference model, ten-year run: they differed at ranks 5 and 6 — S27 archetype mix 5th on profit and 6th on funding, S1 rail cost the reverse.** ⚠ **On a 7-year horizon expect the early-biting parameters to rank higher on funding than they did**, because the trough now sits much closer to the ramp. ⚠ **A parameter returning a swing of exactly zero is a wiring failure, not a finding** — check the flex actually reaches the model (S27 was dead until a `from params import` binding was fixed, and S48 until it was read by any model code) |

### 20.3 Post-build validation checklist

**Run all of these before the model is presented, and record the answer to each.**

| # | Validation | Expected |
|---|---|---|
| 1 | **All sixteen checks TRUE under all three global scenarios** | 🔴 **Non-negotiable** |
| **1a** | 🔴 **Check 14, the convolution impulse test, passes** | For `(1,0,0,…)`, the book at `t` equals `curve(m=t)` exactly, every series, every `t`. **A backwards convolution is invisible in the totals and fatal in the ladder dates** |
| **1b** | 🔴 **Check 15, the 5% collapse-safety gate, passes under all three scenarios** | Max annual stream-2 delta ≤ 5% of gross profit. **Failure reverts the collapse — it is not a warning** |
| **1c** | **The workbook contains no cohort triangle** | Grep the sheet list. **One Lifecycle Curves sheet, one Model sheet, no per-cohort blocks anywhere** (D23) |
| **1d** | **The Model sheet is 29 columns and the Lifecycle Curves sheet is 84** | **Two different indices, deliberately.** If the curve sheet has been shortened to 29, a Y7 annual column cannot be built from twelve genuine monthly points |
| 2 | **Nine personas pass, on the ICS Validation sheet** | Nine TRUEs |
| 3 | **Aggregate survival against the §0.5 anchors inside the horizon** | 55 / 40 / 30 / 24% ± 1pp at M13 / M25 / M37 / M49. ⚠ **The M61 anchor at 19% falls at Y6 and is still testable; there is no M73+ anchor to test** |
| 4 | **Ladder arrival for a clean saver** | Silver M6, Gold M12 — **both inside the monthly block, where it matters.** Platinum M36 and Sovereign M60 resolve inside annual columns |
| 5 | **`Record` binds and `Standing` never does, for a clean saver** | The §7.4 property, reproduced not assumed, **on the ICS Validation sheet** |
| 6 | **Tier distribution is genuinely computed** | T4 and T5 are GREEN links from the Model sheet's convolution band, **not typed values.** This is the claim v1.0 made and could not support. ⚠ **The collapse does not weaken this — the lookup is applied per archetype and weighted, so the mix is still an output** |
| **6a** | **The gate distribution is genuinely computed** | Weighted mean gate M8.1, ever-gate 53.5%. 🔴 **This is the first-order term. If it reads M6 and 100%, the live engine has been collapsed along with the ladder and the model overstates the business by ~59%** |
| 7 | **The alternating-misser curve is capped at Gold at M84** | Never advances past Gold, however long it survives. **The archetype cap, not a blended ladder** |
| 8 | **Never-gated accounts appear and carry zero benefit cost** | A non-zero population with a zero discount |
| 9 | **Holding-not-contributing reaches ~81% of ever-acquired by M61** | The D1 correction, visible in a row. **Already ~60% by M25, inside the first annual column** |
| 10 | **Spot margin per ticket exceeds SIP margin per ticket at both rail cases** | Including the Conservative rail, where SIP is negative and spot is not |
| 11 | **Stream 5 is roughly half v1.0's figure** | The S40 correction, visible |
| 12 | **Effective PM share is below the contracted share** | ~43% against 55% at the flat Gold rate, Conservative |
| 13 | **Redemption spread cost is exactly zero in every growing month** | The §5.4 argument, reproduced |
| **14** | ⚠ **The funding trajectory populates and is labelled as a within-horizon trough** | **It must NOT be labelled peak funding.** The peak falls outside a 7-year window (§14, §0 footnote). **If the workbook reports a "peak funding requirement," that label is the error, not the number** |
| 15 | **Cash break-even and P&L break-even are both reported as not reached** | ⚠ **Neither turns inside the horizon.** If either reports a date, the cash rows or the extrapolation are wrong |
| 16 | **The diverging-curves chart renders and the two lines do not meet on the entry-fee-only basis** | The answer to the client's item 5, **and the one break-even artefact that carries no year in it** |
| 17 | **Every `{{SPINE}}` placeholder in this brief has a populated cell reference** | No orphans in either direction |
| 18 | **No numeric literal other than 0, 1, 12 or 100 appears in any formula outside Assumptions and Scenario** | Spot-check twenty formulas across four sheets, **including five in the convolution band** |
| 19 | **The two tornados produce different rankings** | Timing-sensitive parameters rank higher on funding, **and on a 7-year horizon they should rank higher than they did on ten**, because the trough sits much closer to the ramp. **No parameter may return a swing of exactly zero** — that is a wiring failure |
| 20 | **Sourcing audit counts tie to the register** | §8.5 totals to 101 |
| **21** | ⚠ **Every figure carried forward from this brief has been re-cut on the 7-year basis** | **No output figure in the workbook may be a v2.0 ten-year value.** The brief's figures are illustrative of the architecture; the workbook's are the answer |

**One final instruction, and it is the reason this brief is 2,000 lines rather than 700.** **The model's job is not to produce a number. It is to make a small number of decisions visible: the rail, the PM share, the prepaid-versus-credit fork, whether a lapsed customer keeps the card, and whether the entry fee funds the ladder at all.** Every structural choice above exists to keep one of those five questions answerable rather than averaged away.
