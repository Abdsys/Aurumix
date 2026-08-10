# ICS Benefits: The Definition Layer

> **Status: decision draft, 2026-08-10.** Defines the five ICS benefits fixed in decision 44 mechanically, one by one, before the score formula, the tier count or the thresholds are designed. **Tier is an abstract input throughout**: this file assumes only that tiers exist, are ordered, and are recalculated monthly. How many there are and where they sit is the scoring step's job (B4), and this file ends with the exact list of numbers that step must supply.
>
> Companion to `_draft_sip-rulebook.md`, which settles how the score is earned. This file settles what the score buys. Where a number appears below it is a **placeholder marked as an input**, never a decision.

## 0. Why this layer exists

**The problem.** Decision 44 closed the benefit set at five, but each benefit is one line in a decision log. The scoring step cannot start from that: a tier threshold is a price point, and you cannot place a price point on a benefit whose floor, ceiling, funding and failure modes are undefined. Designed in the wrong order, the thresholds get set first and the benefits get bent to fit them, which is how the client's own document ended up with credit activating at month 6 in every row of a table that offered six different commitment terms.

**The solution.** Define each benefit as a machine: what the customer gets, what range it moves across, who pays for it, what stops it being gamed, and what happens at every edge the SIP rulebook already recognises. Then hand the scoring step a closed shopping list: for each benefit, a value function over tiers, with the floor and ceiling already fixed here.

**The reasoning.** This is the same order the rulebook forced on the score itself: structure first, numbers second, so the numbers can be tested against constraints instead of debated in the abstract. The binding tests are already known and they bind the benefits, not just the score: **a USD 20 saver who never misses must be able to reach every benefit's ceiling**, and a cycler must reach none of them.

### 0.1 The five, sorted by what kind of lever each one is

This extends the taxonomy in rulebook §1.1 from three levers to five. The family a benefit belongs to decides what protection it needs, and that is why the table exists.

| # | Benefit | Family | Earned by | Applies to | Cannot exist without |
|---|---|---|---|---|---|
| 1 | Entry-fee discount | **Price** | SIP only | **Every purchase, spot included** (rulebook §1.1) | Nothing. Live at launch |
| 2 | Credit LTV ladder | **Leverage** | SIP only | All grams, as an account attribute | The CBUAE-licensed lending partner |
| 3 | Card tier | **Service and waiver** | SIP only | The account | The BIN sponsor bank |
| 4 | Gold Rewards rate | **Payout** | SIP only | Card spend | The card, so the sponsor bank |
| 5 | Digital Will and family services discount | **Price** | SIP only | Stream 3 fees, as an account attribute | Nothing for the plan fee; the will partner for execution |

**Price levers are self-limiting** (bounded by money the customer hands over), which is why benefit 1 is safe to apply to spot and benefit 5 needs no anti-gaming machinery. **The payout lever needs a cap, the leverage lever needs seasoning, and the service lever needs a partner**, which is the rest of this file.

### 0.2 Rules that bind all five

These are already decided. They are restated here because every section below leans on them.

| Rule | Content | Source |
|---|---|---|
| **The gate** | Confirmed SIP (the 6th consecutive counted period) switches benefits on. It is permanent once earned. Nothing is granted before it; the score accrues visibly from period 1 | Rulebook §4 |
| **The clock** | Tier is recalculated **once a month, at period close**. No benefit reads the live score | Rulebook §10 |
| **Behaviour, never amount** | No benefit's *rate* may scale with capital. Amount sizes the base; behaviour sets the rate | Decision 20 |
| **The exit is untouchable** | No benefit may charge, deduct, withhold or penalise at redemption. VARA Rule III.E.4 | Decision 32 |
| **Payouts capped at generated** | Any benefit that pays out is capped at the revenue that customer generated | Decision 6 |
| **Step-down is prospective** | A tier fall reprices future events only. Nothing already delivered is clawed back, and **a step-down never triggers a margin call** | Rulebook §10 |
| **Grams are fungible** | No benefit may require tagging grams by channel | Decision 41 |
| **Partner terms** | Where a partner holds the licence, **the structure is ours and the pricing is theirs**. Card and lending run through CBUAE-licensed partners | Decisions 44, §5 of `handoff.md` |

### 0.3 The tier of record, defined once so five benefits can read it

**The problem.** "Recalculated monthly at period close" hides a race. A period can be settled by a grace payment up to 5 days after the contribution date, and grace crosses the month boundary (rulebook §7.2). A recalculation that runs at midnight on the last day of the month would score a grace payer down and then correct itself, and a benefit priced in that window would be wrong.

**The solution.**

> **Tier of record: the tier computed the last time one of the account's periods resolved.** A period resolves at the earlier of (a) a qualifying payment clearing, or (b) grace expiry. Revival (arrears clearing inside 12 months) is a second resolution event and recalculates immediately.
>
> Every benefit reads the tier of record and nothing else. Between resolutions the tier of record cannot move, whatever the live score does.

**The reasoning.** One account, one number, one update rule. Benefits that flicker are unusable (rulebook §10), and a single strike source means no benefit can disagree with another about what tier the customer was. It also makes the round-trip flag legible, because tier history is a monthly series, not a tick stream.

**Strike rules, per family.** Price levers (1 and 5) strike at the event: the discount applied is the tier of record on the day the price is struck. The leverage lever (2) strikes at the draw and holds to term. The service lever (3) applies from the next card statement cycle after a tier change. The payout lever (4) computes at period close over the period just ended.

---

## 1. Entry-fee discount

**The problem.** The entry fee is the product's one unavoidable toll (rulebook §9.2) and its largest revenue line. A discount ladder on it is the most visible thing the score buys, and the only benefit a customer meets on day one of eligibility. But an undefined ladder threatens the margin: decision 9 puts the Year 1 build-up at 4.15% against a 5% fee, so a carelessly funded ladder is loss-making before it retains anyone.

### 1.1 Mechanism

| Question | Answer |
|---|---|
| What the customer gets | A reduction, in percentage points, off the base entry-fee rate on **every purchase the account makes**: SIP contributions and spot alike (rulebook §1.1) |
| What triggers it | Any purchase. The discount is part of the price, applied in the same breath as the fee itself |
| When granted | From the first purchase after Confirmed SIP. Before the gate, every purchase pays the base rate |
| Tier applied | The **tier of record on the day the price is struck**, which is the day the fix is applied to cleared funds (decision 34). Price and discount strike together, always |
| Recalculated | Monthly, at period resolution (§0.3). A purchase never waits for a recalculation and never triggers one |

### 1.2 Shape

| Parameter | Value | Status |
|---|---|---|
| Base rate | Top of the client's stated range at launch, ~5% at Year 1, falling with bar denomination (decision 9: ~4% Y3, ~3% Y10). **Must be set above the top-tier price**, so the ladder is funded by uplift, not margin | Structure decided (rulebook §1.1); the funding split is the **client's decision**, still open (rulebook §13) |
| Floor of the benefit | 0 percentage points: the base rate, paid by every pre-Confirmed account and by the lowest benefit-bearing tier if B4 sets it so | Fixed here |
| Ceiling of the benefit | **Placeholder: 1.5 to 2.0 percentage points off the base** at the top tier. Bounded above by the uplift the client authorises, bounded below by noticeability: a ladder of 0.12pp steps (all that margin alone funds) is decorative | ⚠ Input to B4 and to the client funding decision |
| Smooth or stepped | **Stepped, by tier.** A price must be quotable before the customer pays: the app shows "your rate: X%", receipts carry it, and disclosure documents list it. A smooth curve makes every customer's price unique and unauditable | Decided here |

### 1.3 Funding line

**Stream 1, the entry fee itself, through the base-rate uplift.** No other stream touches it and it touches no other stream. Decision 44 already simplified this: with the tenure rebate retired, the discount ladder is the only draw on the uplift. The funding question is therefore one number: how far above the top-tier price the base rate sits.

### 1.4 Caps and guards

| Guard | Why |
|---|---|
| None needed against extraction | A price reduction cannot leak. The round trip (buy at discounted fee, exit at NAV with no fee) nets to minus the fee, negative at every tier. Proven in rulebook §1.1 and recorded as register item 15 |
| The cycler-toll interaction, monitored not blocked | The fee is the cycler's per-cycle toll and the discount lowers it at high tiers. Acceptable because Retention keeps a cycler at the bottom of the ladder, so the toll they actually pay is the top-of-range rate (rulebook §9.2). No new register row |
| The customer-generated cap | **Not applicable.** Nothing is paid out |

### 1.5 Edge cases

| Case | Behaviour |
|---|---|
| Step-down mid-cycle | The next purchase prices at the new tier of record. Purchases already struck keep their price. Nothing retroactive |
| Pledged gold | Irrelevant. The discount prices new money; pledge status of existing grams does not enter |
| Regulatory block | No purchases are possible, so no discount events occur. The tier is frozen (rulebook §8), so the rate is intact the day the block lifts |
| Dormancy | Hold-only means scheduled requests stop, not that the account is dead. **A spot purchase by a dormant account is permitted and prices at the decayed tier of record.** It is also the most natural way back in |
| A returner resuming | Prices at the decayed tier from the first purchase, immediately: Confirmed SIP is permanent, so there is no re-gate. The rate climbs as the tier rebuilds |
| Partial withdrawal (Retention falls) | R falls smoothly, the tier may step down at the next resolution, and future purchases price at the lower tier. No cliff, no effect on past purchases |

### 1.6 Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No.** The rate is set by tier, earned by counted periods only. A USD 50,000 spot purchase earns zero periods and moves no tier (rulebook §1.1) |
| Touches the exit? | **No.** It is a price at entry. III.E.4 untouched |
| Payout capped at generated? | n/a, no payout |
| Partner-dependent? | **No.** The one benefit entirely inside Aurumix's own pricing |

---

## 2. Credit LTV ladder

**The problem.** Credit is the largest prize in the product and therefore the sharpest gaming surface (register item 11: roughly USD 45,000 of extra credit on a USD 100,000 position between bottom and top LTV). It is also the one benefit where a wrong edge case breaks the product's central promise: a missed USD 20 payment that forced a liquidation would convert "no financial penalty for a miss" into a lie. And it is not fully Aurumix's to give: the lender is a CBUAE-licensed partner, and the ceiling of the ladder is ultimately the partner's risk appetite, not our design.

### 2.1 Mechanism

| Question | Answer |
|---|---|
| What the customer gets | A **maximum loan-to-value ratio** at which new draws can be struck against their gold. Tier sets the rate; grams set the base. Borrowing headroom = seasoned, unpledged grams × the fix × LTV(tier) |
| What triggers it | A draw request. Aurumix originates against its ladder; the partner advances the money and owns the loan |
| When granted | At Confirmed SIP, as a **climbing ladder, not a switch** (decision 21): the floor LTV at the gate, rising with tier |
| Struck when | **At the draw.** The LTV, the collateral valuation and the tier are all read on the draw date and hold for the term of that draw |
| Recalculated | Headroom reprices monthly at period resolution and continuously with the fix. **Existing draws never reprice.** Only new draws see a new tier |

### 2.2 Shape

| Parameter | Value | Status |
|---|---|---|
| Floor | **Placeholder: 50%** at the first credit-bearing tier | ⚠ Input to B4 |
| Ceiling | **min(partner maximum, 90 to 95%)**. The 90 to 95% is the client's own corrected figure (from the incoherent 110%) and is retained as the design ceiling, but see §2.3: it sits above every observed comparable, so **the partner maximum will almost certainly bind first** | ⚠ Input to B4, gated by the partner conversation |
| Smooth or stepped | **Stepped, by tier.** An LTV is a term in a loan document and a disclosure; it must be quotable, and the warning and liquidation thresholds must be spaced above each step. A smooth curve would give every draw a unique threshold stack | Decided here |
| Threshold spacing | Warning and liquidation thresholds sit above the struck LTV of each draw and are the **partner's machinery**. Owed re-spacing against the corrected ceiling (`handoff.md` §7) | Partner + Phase 4 |

**One distinction the drafting must never blur: a tier fall can never margin-call, a price fall can.** The no-margin-call rule protects the customer from the score. It does not, and cannot, protect them from the gold price: if the fix falls far enough against a struck draw, the partner's warning and liquidation ladder fires, and register item under §10 of the rulebook already prices that honestly (liquidation reduces R). Write the promise precisely: *your score can never cost you your gold; the market can, only if you borrow against it, and only past the thresholds you were shown at the draw.*

### 2.3 What lenders actually allow, checked 2026-08-10

The ceiling is not ours to assert, so it was checked against the market. Run via sonar-pro, registry-first rule applied; primary RBI text not yet pulled, so Medium-High until it is.

| Segment | Finding | Source, confidence |
|---|---|---|
| India, regulatory cap | RBI **Lending Against Gold and Silver Collateral Directions, 2025** (June 2025, effective 1 April 2026): tiered maximum of **85%** (loans up to INR 2.5 lakh), **80%** (2.5 to 5 lakh), **75%** (above 5 lakh). Before that, a uniform 75% | Muthoot, Upstox, Shriram, Poonawalla summaries, convergent. **Medium-High**; pull the RBI direction itself before this reaches the client |
| India, large NBFCs | Muthoot and Manappuram advertise at the regulatory cap, not above it; Manappuram states 75% | Manappuram guideline page. **Medium-High** |
| UAE | **No UAE bank or CBUAE-licensed finance company was found publishing a loan-against-physical-gold product with an LTV.** A negative result, consistent with the pattern: this closes only in the partner conversation | Desk sweep. **The number does not exist publicly** |
| Tokenised gold as collateral | Fringe Finance: PAXG at **50%**. Clapp Finance: PAXG at **80%**. Nexo and Crypto.com accept PAXG but publish no LTV. No XAUT lender found with a published figure | Platform pages via sweep. **Medium** |

**What this means for the ladder.** Every observed comparable sits between 50% and 85%, and the regulator of the world's largest gold-loan market caps retail gold lending at 75 to 85%. A 90 to 95% ceiling is beyond all of it. Three consequences: (a) keep 90 to 95% as the design ceiling so the structure survives a generous partner, (b) **B4 must place its tier values so the ladder still differentiates if the partner maximum lands at 75 to 85%**, which is the likely case, and (c) tell the client the ceiling is a partner outcome, not a promise, before it appears in any customer-facing material. Note in passing that the RBI's own 2025 structure is a ladder tiered by loan size; Aurumix's is tiered by behaviour, which is the shape the whole product argues for.

### 2.4 Funding line

**Stream 5, lending fees.** The benefit costs Aurumix no cash: a higher LTV is risk capacity, and the risk sits on the partner's book, which is exactly why the ceiling is theirs. What the ladder does to stream 5 is grow it: origination, servicing and the negotiated interest share all scale with drawn balances, and drawn balances scale with permitted LTV. The benefit and its funding are the same event.

### 2.5 Caps and guards

| Guard | Content | Register |
|---|---|---|
| **90-day collateral seasoning** | Grams enter the borrowing base only after 90 days held. Redeemed-then-rebought grams restart the clock. Inbound transferred grams start a fresh clock | Item 11 |
| **LTV struck at draw** | No draw ever reprices to a later, higher tier; no step-down ever reprices it lower | Item 11, and the no-margin-call rule |
| **No pledge stacking** | Headroom counts **seasoned, unpledged** grams only. A pledged gram supports one draw | Stated here; implicit before |
| **Retention** | A cycler cannot reach a high tier at all, which removes the prize before the seasoning is even tested | §5 of the rulebook |
| **Round-trip flag** | Freezes tier progression pending review for the residue Layer 1 cannot see | §9.3 |
| Customer-generated cap | n/a. Credit is not a payout; it is bounded by collateral, which is the customer's own gold |

### 2.6 Edge cases

| Case | Behaviour |
|---|---|
| Step-down mid-cycle | **Never a margin call.** Existing draws run to term at the struck LTV. New draws use the new tier of record. Headroom for further borrowing shrinks; nothing outstanding is touched |
| Pledged gold | Still earns ICS and counts in Retention in full (rulebook §10, client's stated intent). It cannot leave (exit pledge check) and cannot support a second draw |
| Regulatory block | Existing credit runs to term; **no new draws** (rulebook §8). The tier freezes, so the day the block lifts, headroom is what it was |
| Dormancy | No credit meaning of its own. A dormant account with seasoned unpledged grams may request a draw at its decayed tier of record, subject to the partner's own KYC refresh |
| A returner resuming | Draws at the decayed tier immediately; the ladder climbs as the tier rebuilds. No re-qualification: Confirmed SIP is permanent and the seasoning clock on continuously-held grams never restarted |
| Partial withdrawal (Retention falls) | Only unpledged grams can leave. R falls, the tier may fall at next resolution, future headroom falls with it. Existing draws unaffected |
| Collateral liquidated on default | The partner's machinery, disclosed at the draw. The liquidation reduces R (rulebook §10), which is honest: the gold left |

### 2.7 Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No, and this is the founding principle made concrete: grams are the base, tier is the rate** (decision 41). Two savers with identical behaviour get identical LTV percentages on very different gram counts |
| Touches the exit? | **No.** The pledge check at exit is a lien question, not a fee. III.E.4 untouched |
| Payout capped at generated? | n/a, no payout |
| Partner-dependent? | **Yes, flag it: structure ours, pricing theirs.** The ladder, seasoning and strike rules are Aurumix's origination policy. The maximum LTV, the interest rate, the warning and liquidation thresholds and the licence are the partner's. Interest-rate-by-tier was already rejected in decision 44 for exactly this reason. ⚠ Also open: whether the facility advances dirhams (CBUAE finance company, AED 150M capital) or tokens (VARA lending licence, AED 500k). Counsel question, already first in the queue |

---

## 3. Card tier

**The problem.** The score's first two benefits pay off only at a purchase (the discount) or only if you borrow (the LTV). A disciplined saver who does neither climbs the ladder and feels nothing, which is a retention failure in the exact population the product most wants to keep. Card benefits are the fix (they pay off weekly, in something visible), but the card is a partner programme: Aurumix cannot mint card levels the sponsor bank has not agreed to operate.

### 3.1 Mechanism

| Question | Answer |
|---|---|
| What the customer gets | A card programme level, set by tier, controlling: the **FX margin** on foreign-currency spend, the **free ATM withdrawal allowance** per month, and **issuance and replacement fee waivers** |
| What triggers it | Confirmed SIP switches card eligibility on (rulebook §4). The level then tracks the tier of record |
| When granted | Card issued on request after the gate. Level changes apply **from the next statement cycle** after a tier change, never mid-cycle: an allowance that shrinks mid-month is a trap, not a benefit |
| Recalculated | Tier monthly at period resolution; the card level follows at the statement boundary |

**The mapping is many-to-few and that is fine.** Sponsor banks operate a handful of programme levels, typically three or four, and B4 may define more tiers than that. The mapping from tiers to card levels must be **monotone and onto**: a higher tier never gets a worse card, and every card level is reachable. Benefits are allowed to plateau across adjacent tiers; the scoring step should know that when placing thresholds.

### 3.2 Shape

| Parameter | Value | Status |
|---|---|---|
| FX margin | From **~2.0%** at the base level (the market clearing rate: Nexo, Crypto.com and Wirex all land on it independently) down to a **placeholder 0.75 to 1.0%** at the top level | ⚠ Input to B4 and to the sponsor contract |
| Free ATM allowance | From a base monthly allowance to a larger one; **placeholder AED 1,000 to AED 5,000 per month** across the range, ~2% beyond it | ⚠ Input, partner-gated |
| Issuance and replacement | Charged at base level, waived at upper levels | ⚠ Input |
| Smooth or stepped | **Stepped, necessarily.** Card levels are discrete products at the sponsor bank; there is no such thing as a continuum of card configurations | Forced by the rail |
| Annual and monthly fees | **None at any level.** The market has moved off both and Kinesis charges zero-zero-zero. Not a tier lever | Decided (revenue streams map 4) |

### 3.3 Funding line

**Streams 2 and 4 together.** Every card benefit is a **waiver of stream 4 revenue** (FX margin conceded, ATM fees not charged, issuance waived), funded by the **stream 2 interchange** the same spender generates: the customer who uses the allowances is by definition the customer generating interchange. This is the cheap benefit: a fee you waive rather than cash you hand over, and it cannot be consumed without producing the revenue that pays for it.

### 3.4 Caps and guards

| Guard | Content |
|---|---|
| Allowances are per-month and reset at cycle | An unused allowance does not roll. Rolling allowances become a bankable asset and an accounting liability |
| Bounded by the customer's own activity | A waiver is worth only what the customer would otherwise have paid. There is no payout to farm, so no register row is needed |
| The mapping is contractual | Levels, margins and allowances live in the sponsor-bank contract. Aurumix cannot unilaterally sweeten them, which is itself a guard |

No new anti-gaming surface: the register's card-adjacent risk is the Gold Rewards payout, capped in §4. Spending money to enjoy a waiver is not an exploit; it is the business.

### 3.5 Edge cases

| Case | Behaviour |
|---|---|
| Step-down mid-cycle | Level falls **at the next statement cycle**. Mid-cycle spend keeps the current level's terms. **The card itself is never cancelled by a step-down**: once Confirmed, the base level is the floor |
| Pledged gold | If the card draws on the credit facility (it should: build it as credit, not prepaid), card spend is a draw and follows §2's rules, including the struck LTV of the facility. Pledge status does not change card level |
| Regulatory block | Tier freezes. Whether the card keeps working is the **partner's regulatory call, not ours**: flag to the sponsor conversation. Design default: card suspended alongside contributions, existing balance runs down under §2's run-to-term rule |
| Dormancy | The card keeps working at the decayed tier's level. A dormant saver who still spends is generating interchange: revenue, and a live touchpoint back |
| A returner resuming | Level recovers with the tier of record, statement cycle by statement cycle. No re-application |
| Partial withdrawal (Retention falls) | Tier may fall, level follows at the next cycle. If the withdrawn grams were unpledged, the card's credit line is untouched; pledged grams could not leave anyway |

### 3.6 Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No.** Level follows tier; tier follows behaviour. A large balance buys no level |
| Touches the exit? | **No** |
| Payout capped at generated? | n/a here; the card's payout side is Gold Rewards, capped in §4 |
| Partner-dependent? | **Yes, flag it: structure ours, pricing theirs.** The level count, the FX floor, the allowance economics and the BIN all sit with the sponsor bank (CBUAE holds the sole right to issue BINs; precedent ADIB + Al Fardan). ⚠ And the single largest open choice is not a tier question at all: **credit, not prepaid**, or interchange is capped at 0.75/1.0% forever |

---

## 4. Gold Rewards rate

**The problem.** Gold Rewards exists because the ICS Dividend was a profit share and forced a security classification (decision 6). Its replacement must pay real grams to real customers without ever being fundable by other customers' fees, without scaling with holdings, and without acquiring a name or a shape a regulator could call yield. The design answer has been fixed for weeks (a fee rebate in grams, capped at what the customer generated); what is undefined is the machine: when it computes, at what price grams strike, what the tier actually varies, and what happens at the edges.

### 4.1 Mechanism

| Question | Answer |
|---|---|
| What the customer gets | A monthly rebate, **credited in grams**, equal to **rate(tier) × qualifying card spend** for the period, subject to the cap in §4.4 |
| What triggers it | Card spend during the period. No spend, no reward, at any tier |
| When granted | **Computed at period close** over the period just ended, at the tier of record that governed that period. Grams are credited in one monthly event, not per transaction |
| Price struck | Reward value converts to grams at **the next published fix after period close** (decision 34's one pricing rule: the price is always the next fix nobody has seen). One strike per month, same for everyone |
| Recalculated | The rate follows the tier of record monthly. The credit, once made, is the customer's gold, full stop |
| Ships when | **With the card.** It is funded by interchange that does not exist until the card does (decision 41) |

The gram credit is a title transfer of Aurumix's own metal into the customer's holding, which is why it is the one benefit with a real unit cost per event, and why it launches second (the entry-fee discount, arithmetically identical at the moment of purchase, is nearly free to run and launches first: decision 41).

### 4.2 Shape

| Parameter | Value | Status |
|---|---|---|
| Floor | **Placeholder: 0.10%** of qualifying spend at the first benefit-bearing tier | ⚠ Input to B4 (decision 6's launch sizing) |
| Ceiling | **Placeholder: 0.75%** at the top tier at launch. The category ceiling is the Kinesis card: 2% back in gold, capped at USD 2,000 of spend per month, the one benefit precedent worth copying (decision 44). Kinesis runs it as a cost centre; Aurumix must run it inside interchange, so the launch ceiling sits well below 2% until the sponsor share is known | ⚠ Input to B4, bounded by the contracted interchange share |
| Smooth or stepped | **Stepped, by tier.** A rewards rate is a marketing claim ("0.5% back in gold"); a smooth curve cannot be advertised or reconciled by the customer | Decided here |
| Spend cap | **Placeholder: a monthly qualifying-spend cap in the region of USD 2,000 to 5,000**, Kinesis-comparable. Secondary protection; the revenue cap in §4.4 is the real one | ⚠ Input |

### 4.3 Funding line

**Stream 2 (interchange, primary) plus stream 5 (the credit revenue share), netted of that customer's custody cost (stream 6a arithmetic, decision 42).** Never stream 1: no saver's entry fee funds another saver's reward, which is the entire point of the redesign. The netting line means the most engaged customers quietly cover their own storage inside a cap they never hit the edge of.

### 4.4 Caps and guards

| Guard | Content | Register |
|---|---|---|
| **The customer-generated cap** | Cumulative rewards credited ≤ cumulative (interchange + credit revenue) that this customer generated, **minus that customer's custody cost**. Computed per account, monthly, as a running total | Item 14; decisions 6 and 42 |
| Rewards grams cannot inflate the score | A Gold Rewards credit adds to **both sides** of Retention: neutral by construction | Rulebook §10 |
| Rewards grams earn no periods | Not a contribution; nothing about the credit touches continuity or tenure | Rulebook §2 |
| Fresh seasoning | Credited grams enter the credit borrowing base only after the standard 90 days | §2.5 |
| Wash-spend economics | Spending to farm rewards pays the customer ≤ rate × spend and pays Aurumix the interchange share, with rate set below the share. Farming loses money at every tier. Merchant-category exclusions (cash-like MCCs: quasi-cash, money transfer, gambling) as standard partner hygiene | ⚠ MCC list is partner boilerplate, note only |

### 4.5 Edge cases

| Case | Behaviour |
|---|---|
| Step-down mid-cycle | The period's spend earns at the tier of record that governed the period; the change lands on the next period. Grams already credited are never clawed back |
| Pledged gold | No interaction. Rewards are computed off spend, not holdings, and the credit lands as new unpledged grams |
| Regulatory block | Card suspends with the block (§3.5), so accrual stops with it. Spend already made before the block computes normally at period close. ⚠ **One flagged question: whether a gram credit may land on a blocked account**, since it is a new acquisition by someone the product refuses money from. Design default: the credit is held pending and lands when the block lifts, or settles inside the cash buyback at exit. Consequential counsel item, not blocking; it joins the Option A batch (Gold Rewards grams are already on that list) |
| Dormancy | A dormant saver who keeps spending keeps earning at the decayed tier's rate. Deliberate: it is revenue, and a monthly gram credit is the best re-engagement message the product has |
| A returner resuming | Rate recovers with the tier of record. Nothing to restore: the cap's running totals never stopped counting |
| Partial withdrawal (Retention falls) | Future rate may fall with the tier. Credited grams are the customer's gold and leave only if the customer sends them out, which is then an ordinary outflow in R |

### 4.6 Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No, twice over.** The rate is set by tier (behaviour); the base is spend (behaviour). Holdings appear nowhere in the formula. This is what makes it a rebate and not a dividend |
| Touches the exit? | **No.** Credits happen at period close; nothing computes, vests or forfeits at redemption |
| Payout capped at generated? | **Yes, and it is the load-bearing rule.** State it in every description: funded by the merchant and the borrower, capped at what this customer generated, never called a yield |
| Partner-dependent? | **Yes, flag it: structure ours, pricing theirs.** The interchange share (unpublished, sponsor-negotiated) is the hard ceiling on the rate table. B4 can set relative tier spacing now; absolute rates harden only after the sponsor conversation |

---

## 5. Digital Will and family services discount

**The problem.** The Family Portfolio and Digital Will are the only features in the category with no competitor at all, and they were about to be given away free while carrying real recurring cost (every name is a KYC file, a register entry and a succession instruction). Pricing them (revenue streams map 3) fixed that and broke the §9.5 circularity. But pricing them flat leaves the score with nothing to say about the product's most differentiated feature. Decision 44 added the fifth benefit: a tier discount on those prices. What is undefined is what the discount applies to and how deep it can go before it un-prices the cost driver.

### 5.1 Mechanism

| Question | Answer |
|---|---|
| What the customer gets | A percentage discount, by tier, on **stream 3 prices**: the annual family plan fee, and (shallower) the one-off per-beneficiary registration fee |
| What triggers it | A billing event: annual plan renewal, first subscription, or a beneficiary registration |
| When granted | From the first billing event after Confirmed SIP. The feature itself is **open to everyone at every tier, gated by payment, never by tier** (rulebook §9.5): the discount is a price, not a gate |
| Tier applied | The tier of record on the billing date. An annual fee already paid is paid; a mid-term tier change waits for renewal |
| Recalculated | Monthly at period resolution, read at each billing event |

### 5.2 Shape

| Parameter | Value | Status |
|---|---|---|
| Plan-fee discount | From **0%** at base to a **placeholder ceiling of 40 to 50%** at the top tier | ⚠ Input to B4 |
| Per-beneficiary fee discount | **Shallower, placeholder ceiling 0 to 20%**, possibly flat at 0 | ⚠ Input to B4, with the reasoning fixed here: the per-beneficiary fee prices the actual cost driver (ten beneficiaries is ten times the work), so discounting it deeply re-creates the unfunded-cost problem name by name |
| Never 100% | The ceiling stays below free. A free ceiling would make the feature costless exactly for the customers using it most, reintroducing an unrecovered recurring cost, and would rebuild the §9.5 tier-gate in mirror image (the feature would again be "what a top tier gets") | Decided here |
| Smooth or stepped | **Stepped, by tier.** Published subscription prices | Decided here |
| Base prices | No published comparable anywhere in the set or the wider survey. **Price on cost**, client decision, Phase 4 | Open, client |

### 5.3 Funding line

**Stream 3 itself, through its own base-price headroom.** Same logic as the entry fee: set the base price so that the ceiling-discounted price still clears the real cost (KYC, register, succession instruction, the will-execution partner's charge). The ladder then gives away margin, never cost recovery. One number decides the room, and it is the same shape as the vault quote: the per-beneficiary cost of the will partner.

### 5.4 Caps and guards

| Guard | Content |
|---|---|
| Self-limiting | A price lever: bounded by money the customer hands over. There is nothing to extract and no register row is needed |
| No circularity with the score | Family sub-account contributions earn capped supplementary points (rulebook §9.5); the discount prices the plan. Score rewards the behaviour, price covers the cost, discount rewards the tier. Three separate wires, none forming a loop: the discount is not a gate, so the §9.5 deadlock cannot re-form |
| Cost floor | The ceiling discount must keep the discounted per-beneficiary fee at or above the will partner's per-name cost. This is the one hard arithmetic check B4 inherits |

### 5.5 Edge cases

| Case | Behaviour |
|---|---|
| Step-down mid-cycle | Nothing mid-term. The next billing event prices at the new tier of record |
| Pledged gold | No interaction with billing. One real touchpoint: succession over pledged grams transfers them subject to the lien; that is Digital Will mechanics (the holding-vehicle work in `handoff.md` §7), not a discount question |
| Regulatory block | Service fees are fees for services, not contributions, so billing may continue; and succession is the one feature a blocked account arguably needs most (the India inheritance carve-out is already counsel batch 1, question 3, with the design answer: settle to cash for any India-resident beneficiary). Discount applies at the frozen tier |
| Dormancy | The plan runs while paid, at the decayed tier's price on renewal. Lapsed payment lapses the plan on its own terms, not the SIP's |
| A returner resuming | Next renewal prices at the recovered tier. Nothing to re-earn |
| Partial withdrawal (Retention falls) | Renewal may price at a lower tier. Beneficiary designations and the plan itself are untouched: the will follows the person, not the balance |

### 5.6 Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No.** The discount follows tier; the fee itself is flat per plan and per name, not per gram, so neither the price nor the discount reads the balance |
| Touches the exit? | **No.** Succession is a transfer on death, not a redemption, and the discount touches only fees charged in life. ⚠ Whether estate settlement to cash constitutes a redemption for III.E purposes is part of the Digital Will counsel work, noted, not created by this benefit |
| Payout capped at generated? | n/a, no payout |
| Partner-dependent? | **Partially, flag it:** the will-execution partner's per-name cost floors the per-beneficiary fee and therefore caps that fee's discount ceiling. The plan-fee side is Aurumix's own pricing |

---

## 6. What exists on day one

Benefits do not all switch on together, and the scoring step should not assume they do.

| Benefit | Live when | Gated by |
|---|---|---|
| Entry-fee discount | **Launch** | Nothing: Aurumix's own pricing |
| Digital Will and family discount | **Launch**, with the paid feature itself | Base prices set (client, Phase 4); will partner for execution |
| Credit LTV ladder | Lending partner signed | The CBUAE partner and the dirhams-or-tokens counsel answer |
| Card tier | Card programme live | Sponsor bank |
| Gold Rewards | **With the card**, not before | Sponsor bank; funded by interchange that does not exist earlier (decision 41) |

A customer Confirmed before the card exists has earned the tier; the benefit arrives when the rail does. Communicate the tier as the durable thing and the benefits as what it currently buys, so shipping a new benefit is a gift to existing tiers rather than a migration.

**One boundary question, recorded not designed:** whether **partner-channel customers** (stream 6, the B2B books) earn ICS and its benefits at all, or hold gold only. The register is multi-tenant; the loyalty programme has only ever been designed for the direct channel. Phase 4 and the partner contract. Nothing in this file assumes either answer.

---

## 7. Handoff to the scoring step: every number B4 must supply

This is the closed list. The structure above holds whatever these numbers become; nothing else about the benefits is open.

**Global, set once:**

- [ ] **Tier count** and **threshold values** (lower bounds, never ranges: rulebook §11).
- [ ] **The first benefit-bearing tier per benefit**: whether the lowest tier above Confirmed SIP carries a nonzero value of each benefit, or some benefits start higher. All five must be monotone non-decreasing in tier.
- [ ] Confirmation that the tier-of-record resolution rule (§0.3) is the recalculation the formula assumes.

**Benefit 1, entry-fee discount:**

- [ ] The discount value per tier, floor 0pp, **ceiling placeholder 1.5 to 2.0pp**.
- [ ] Jointly with the **client's funding decision** (rulebook §13): the base-rate uplift that funds the ceiling. The ladder cannot be sized before the uplift is.

**Benefit 2, credit LTV ladder:**

- [ ] The LTV per tier, **floor placeholder 50%**, ceiling **min(partner max, 90 to 95%)**.
- [ ] A second version of the table that still differentiates if the partner maximum lands at **75 to 85%**, the likely case per §2.3.
- [ ] External input, not B4's to invent: **the partner maximum** (partner conversation) and the warning/liquidation spacing above each step (partner).

**Benefit 3, card tier:**

- [ ] The tier-to-card-level mapping (monotone, onto), against a level count of **3 to 4** until the sponsor says otherwise.
- [ ] FX margin per level (**2.0% base to placeholder 0.75 to 1.0% top**), ATM allowance per level (**placeholder AED 1,000 to 5,000/month**), waiver set per level.
- [ ] External input: the sponsor bank's level count and floor economics.

**Benefit 4, Gold Rewards:**

- [ ] The rate per tier, **floor placeholder 0.10%, ceiling placeholder 0.75%** of qualifying spend.
- [ ] The monthly qualifying-spend cap, **placeholder USD 2,000 to 5,000** (Kinesis comp: 2% capped at USD 2,000).
- [ ] External inputs: the contracted **interchange share** (hard ceiling on the whole table) and the **vault quote** (sets the custody netting line inside the cap).

**Benefit 5, Digital Will and family discount:**

- [ ] Plan-fee discount per tier, floor 0%, **ceiling placeholder 40 to 50%**.
- [ ] Per-beneficiary discount per tier, **ceiling placeholder 0 to 20%**, flat-zero permitted.
- [ ] External inputs: stream 3 base prices (client, cost-based) and the will partner's per-name cost, which floors the discounted fee.

**The tests every candidate table must pass before it ships:**

- [ ] **The USD 20 test, per benefit:** the USD 20 saver who never misses reaches the ceiling value of all five. The rulebook's §11.1 trajectory reaches the top tier at month 56 on contributions alone; every benefit table must pay its ceiling at that tier.
- [ ] **The cycler test:** persona D (rulebook §11.2, ICS 0.3) sits at or below the first benefit-bearing tier on all five.
- [ ] **The withdrawal test:** personas E and F lose tiers, never benefits already delivered: no retroactive repricing, no margin call, no clawback of credited grams.
- [ ] **The funding test:** each ceiling is payable from its own funding line at the placeholder rates (uplift for 1, partner book for 2, interchange for 3 and 4, stream 3 headroom for 5). No benefit may lean on stream 1 except benefit 1's uplift.

---

## 8. What this file changes elsewhere

- [ ] `_draft_sip-spot-and-ics.md` §1: the three-lever framing (price, credit, time) is superseded by the five-benefit set and the family taxonomy in §0.1 here. The time lever's retirement is already recorded (decision 44); the card and will levers are new.
- [ ] `Aurumix_Process_Maps_Revenue_Streams.md` reconciliation list: "ICS gains a fourth benefit lever, card allowances" is **done here** (§3), as tier-mapped programme levels rather than a free-standing lever.
- [ ] Credit design (B-block): inherits §2 wholesale, including the no-pledge-stacking rule stated here for the first time and the partner-bound ceiling from §2.3.
- [ ] Counsel batches: one consequential addition flagged, not sent: whether a Gold Rewards gram credit may land on a regulatorily blocked account (§4.5). Joins the existing Option A consequential list, does not gate anything.
- [ ] Client conversation: the LTV ceiling must be repositioned as a partner outcome before any customer-facing material quotes 90 to 95% (§2.3).

## 9. Sources for this file

| Claim | Source | Confidence |
|---|---|---|
| RBI tiered LTV 85/80/75 by loan size, effective 1 April 2026 | RBI Lending Against Gold and Silver Collateral Directions, 2025, via convergent secondary summaries (Muthoot, Upstox, Shriram, Poonawalla) | **Medium-High.** Pull the RBI primary text before client use |
| Indian NBFCs lend at the regulatory cap, not above | Manappuram guideline page | **Medium-High** |
| No UAE lender publishes a loan-against-physical-gold LTV | Desk sweep, negative result | **The number is not public.** Partner conversation only |
| Tokenised gold collateral: Fringe 50%, Clapp 80%, Nexo/Crypto.com accept PAXG without published LTV | Platform pages via sweep; Paxos partner announcement | **Medium** |
| Kinesis card: 2% back in gold, capped at USD 2,000/month spend, zero fees | Protocol Landscape (Phase 1), reconfirmed in decision 44 | **High** |
| FX margin market rate ~2% (Nexo, Crypto.com, Wirex) | Revenue streams map 4 | **Medium-High** |
| UAE debit/prepaid interchange capped 0.75%/1.00% since 1 Oct 2024; credit uncapped | Revenue streams map 2; credit-card exemption still to confirm with CBUAE | **Medium-High**, one open verification |
| True allocated vault cost 0.15 to 0.40%/yr | Decision 42, research-derived, pending the vault quote | **Medium** |
