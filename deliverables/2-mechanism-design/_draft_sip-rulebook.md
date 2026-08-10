# The SIP Rule Book

> **Status: decision draft, 2026-08-06.** Settles the SIP mechanism end to end: how SIP and spot coexist on one account, how the eligibility gate works, what a missed payment costs, and how the cycling exploit is closed. Resolves the two items left open in `handoff.md` §7. Component weights are proposed here as defaults for B4, clearly marked, and remain open.
>
> 🔄 **Revised 2026-08-10 with Abdur, five changes:** (1) the floor is a hard gate: payments below USD 20 are rejected, never partially credited, which deletes the top-up window and the monthly-total test; (2) grace shortens from 15 days to 5; (3) **UAEDDS direct debit is dropped entirely**: launch rails are AANI Request to Pay plus a prefunded balance, with AANI electronic direct debit adopted when live; (4) the declared pause is deleted; the regulatory pause survives as one automatic rule and dormancy as housekeeping; (5) the ENBD bounce-fee figure is corrected from AED 105 to AED 26.25 (see §14). Sections 0, 2, 3, 6, 7, 8, 9, 12, 13 and 14 amended in place.

## 0. The whole thing in ten lines

1. **One account, one identity, one score, one pot of gold.** SIP and spot are two ways to buy, not two kinds of customer. **You earn your tier by saving monthly, and you spend it on everything you buy.**
2. **A period is a calendar month.** One counted contribution per month, maximum.
3. **A period counts** if a contribution of at least the product floor cleared inside the month or its 5-day grace window. Below the floor is rejected at the door, never partially credited.
4. **Confirmed SIP** arrives after **six consecutive counted periods**. It unlocks benefits. It is permanent once earned.
5. **The score accrues from period one and vests at Confirmed SIP.** Nothing is granted before month six; nothing is wasted either.
6. **The score is made of three things you do**: continuity (your streak), tenure (your total), and capped supplementaries.
7. **All of it is scaled by Retention**: the share of the gold you have bought that you have actually kept, weighted by time.
8. **A miss halves your streak.** It never touches your tenure, your retention or your gold.
9. **The gram count only ever rises.** Every consequence falls on tier, fee or credit ratio.
10. **Retention is what makes cycling pointless.** You cannot fake gold sitting still.

---

## 1. How SIP and spot coexist

The same person is both. That is the normal case, not an edge case.

| | SIP contribution | Spot purchase |
|---|---|---|
| What triggers it | A schedule the investor declared | A one-off order |
| Earns ICS | **Yes** | **No** |
| Counts toward Confirmed SIP | Yes | No |
| Entry fee | Base rate, **discounted by tier** | Base rate, **discounted by the same tier**. See §1.1 |
| Credit, card, family features | Yes, by tier | Not earned by spot, but applies to all grams once earned |
| Counts in Retention | **Yes, both sides** | **Yes, both sides** |
| **The gold** | **Identical** | **Identical** |

**Three rules govern the interaction and they close every question about the boundary.**

- **Earning and spending are separate.** Only SIP contributions *earn* tier. Once earned, the tier is an account attribute and it *applies* to everything the account does. That is why the credit ratio reaches all grams (decision 41) without spot earning anything.
- **Extra money inside a month is a spot purchase.** It buys gold, it counts in Retention, it earns no period. This is what stops twelve payments in January becoming twelve periods.
- **Spot neither helps nor hurts the score.** Spot grams enter Retention on both sides of the ratio, so buying spot cannot raise your rate and holding it cannot lower it.

### 1.1 The entry-fee discount applies to every purchase, spot included

> **Decision.** The tier's entry-fee discount applies to **any** purchase the account makes. ICS accrual stays SIP-only, and spot continues to earn no score, no credit ratio, no card tier and no family features. **Spot does not earn the tier. It is simply priced at the tier the account already earned.**

This closes the tension recorded in `handoff.md` §7: a top-tier saver adding a lump sum currently pays the newcomer rate for giving Aurumix more money.

**Four reasons, and the second is the one that settles it.**

**1. It is the earn-and-spend rule, already applied everywhere else.** The tier is earned by monthly saving and nothing else. Where it is *spent* is a separate question, and the answer is already "everywhere" for the other levers: decision 41 puts the credit ratio on **all** grams at the tier rate, spot included, and the card tier is an account attribute. The entry-fee discount is the only lever earned one way and then fenced off from part of the account, and no reasoning was ever recorded for the difference.

| Lever | Earned by | Applies to |
|---|---|---|
| Credit ratio | SIP only | All grams, spot included. Decision 41 |
| Card tier | SIP only | The account |
| **Entry-fee discount** | SIP only | **All purchases. Corrected here** |
| ICS itself | SIP only | Not spendable. It is the thing being spent |

**2. The distinction is already unenforceable, so it only taxes the unsophisticated.** The declared SIP amount is **variable with no maximum**. A tier-7 saver wanting to add USD 50,000 can simply declare it as this month's contribution and receive the discount. Under §2 it counts as one contribution in one calendar month, exactly like a USD 20 payment, so there is no score advantage either. **The same money, from the same person, on the same day, gets two different prices depending on which button they press, and the customer controls the button.** A rule that a customer can defeat by relabelling a payment is not a control. It is a penalty on the customers who did not think of it.

**3. A discount cannot leak, because it is a price and not a payout.** Run the round trip: buy at NAV plus the discounted fee, exit at the buyback, which is NAV with **no fee at all** under III.E.4. The net result is minus the fee, negative for any fee above zero. It turns positive only if the fee goes negative or the exit pays above NAV, and neither exists. **The most anyone extracts from the discount is the discount, and the only way to extract it is to actually buy gold and keep it.**

This sorts the three levers permanently, and the taxonomy is worth keeping:

| Lever | Shape | Self-limiting | What it needs |
|---|---|---|---|
| **Entry-fee discount** | A **price** reduction | **Yes.** Bounded by money the customer hands over | Nothing |
| **Gold Rewards** | A **payout** in grams | No | Capped at what that customer generated |
| **Credit LTV** | **Leverage** against a position | No | 90-day seasoning, LTV struck at the draw date |

**Price levers are safe to make channel-blind. Payout and leverage levers are not.** Spot stays excluded from the other two.

**4. It does not touch the classification argument.** What must never be true is that putting in more capital buys a better rate. It still cannot: the tier is earned by counted periods, and a USD 50,000 purchase earns exactly zero of them.

> ⚠ **The discount must be funded by an uplift to the base rate, not out of margin, and this decides whether the lever exists at all.** On decision 9's Year 1 build-up (fabrication 3.0% + price-gap 0.36% + float 0.49% + rail 0.30% = **4.15%**), a 5% fee leaves **0.85 percentage points**. A seven-tier ladder funded from that is about 0.12pp per tier, which no customer will notice. **The client's stated "2 to 5%" cannot be a tier ladder at Year 1**, because a 2% fee is loss-making by more than two percentage points, which decision 9 already says in cash terms. Set the base rate above the top-tier price so the ladder has somewhere to come from. **This is the same funding question already flagged against the tenure rebate, and it should be settled once for both.**

⚠ **One honest cost.** §9.2 lists the entry fee as an unavoidable toll on every cycle. Extending the discount lowers that toll at high tiers. It matters little, because Retention stops a cycler reaching a high tier at all and the toll was never the primary defence, but the interaction is real and belongs in the record.

---

## 2. Vocabulary, because the edge cases live here

Almost every unresolved SIP question in the drafts turns out to be a definitions problem. These seven definitions are load-bearing.

| Term | Definition | Why it is defined this way |
|---|---|---|
| **Period** | A **calendar month**. Not the investor's date | If the period ran from the contribution date, moving the date backwards would squeeze two periods into one month. The calendar month cannot be shuffled |
| **Contribution date** | The investor's chosen day of the month. A collection convenience | Spreads collection load. Changing it can never create or destroy a period |
| **Counted period** | A month in which a cleared contribution of **at least the floor** arrived, within the month or its 5-day grace window | One accepted payment settles the period. Below the floor is rejected at the door (§3), so no top-up window or monthly-total test exists |
| **The floor** | A single product-wide minimum: **USD 20** or the local equivalent. **A hard gate: payments below it are rejected, not partially credited** | See §3. This replaces the per-customer "declared minimum" |
| **Declared amount** | The amount on the monthly payment request. Variable | The collection instruction. It is not a promise and it is never scored |
| **Payment request** | The AANI Request to Pay message sent on the contribution date | The investor approves with one tap. An unanswered request expires: no fee, no bank charge, no retry machinery |
| **Retention (R)** | The time-weighted share of all grams ever acquired that are still held | §5. The anti-cycling mechanism |

---

## 3. Delete the declared minimum

**The problem.** `_draft_purchase-structure.md` §3.1 carries two fields: a declared amount and a **declared minimum**, the floor below which a payment does not count. It exists to make "counted period" well defined when the amount varies.

**It is a self-set exam.** An investor declaring USD 500 a month can set their own minimum at USD 20 and pay USD 20 forever, scoring identically to the USD 20 saver. There is no cost to setting it low, so everyone will, and a field on which every rational investor selects the same value carries no information. That is precisely the argument that deleted the commitment period in `_draft_sip-spot-and-ics.md` §3, applied one level down.

**The solution. One product-wide floor. Delete the customer-set field.**

A period counts if the month's cleared contributions total at least USD 20. Nothing else about the amount is tested anywhere in the model.

**Why this is safe rather than a loophole.** The binding constraint on the whole design is that a USD 20 saver who never misses must reach the top tier (`_draft_sip-spot-and-ics.md` §4). A USD 500 declarer who pays USD 20 is behaving exactly like the USD 20 saver, and receives exactly what the USD 20 saver receives: the same rate, on one twenty-fifth of the gold. **The amount already sized the base. This is the design working, not the design leaking.**

**This also answers "what happens on a payment below the minimum", which `handoff.md` §7 records as undefined.** 🔄 **Revised 2026-08-10: a payment below USD 20 is rejected, never accepted.** The interface will not take it, and if a transfer below the floor lands anyway it is returned with no gold allocated. On the push rail an under-payment can barely arise (the request is for the declared amount and the pay screen enforces the floor), so the rejection rule mostly exists for stray bank transfers. This deletes the partial-payment state, the top-up window and the monthly-total test in one move: a period counts when one accepted payment clears, and there is no partial state to administer.

> **Rejected on the way:** the 2026-08-06 design, which allocated the gold from a sub-floor payment immediately and gave the investor a top-up window (more states, no information); and treating an under-payment as a pause (the pause state itself is deleted in §8).

---

## 4. The lifecycle: day one to Confirmed SIP and beyond

**The eligibility gate, stated precisely.**

| Stage | When | What is true |
|---|---|---|
| **Declared** | Day 0 | Amount, date, rail and optional goal set. No benefits. Score accrues |
| **Contributing** | Periods 1 to 5 | Gold allocated from period 1. Score accrues and is visible. **No benefit is granted** |
| **Confirmed SIP** | On the **6th consecutive counted period** | The score vests. Entry-fee discount, the credit ladder and card eligibility switch on |
| **Accruing** | Period 7 onward | Tier climbs. Credit ladder climbs with it |

**Accrual and vesting are different things, and separating them is worth real money.**

The client's model, and the way this is usually described, is that the score starts at month six. If that is literally true, the first five months are dead time in the interface, and the first year is exactly where six in ten customers are lost (`handoff.md` decision 22). **Show the score accruing from period one and show the milestone it unlocks.** No benefit is granted early, so it costs nothing, and the investor watches a number they have earned move toward a gate they can see. This is the cumulative-bonus shape from health insurance: it accrues through the year and it appears at renewal.

**Six consecutive, not six total.** Consecutive is the client's own figure, and it is the only version that means anything: six payments spread over three years is not evidence of a savings habit.

### 4.1 Is Confirmed SIP re-earnable? Resolved: it is permanent

`handoff.md` §7 records this as genuinely undefined and blocking B4. The drafts say the status "suspends" on a broken streak and is "restored" by revival, and never say what happens if the investor does not revive.

> **Decision: Confirmed SIP, once earned, is never lost. Nothing suspends it. The tier does all the punishing.**

Three reasons, and they converge.

1. **Un-earning it is incoherent with its own definition.** `_draft_sip-spot-and-ics.md` §3 is emphatic that the status is backward-looking: after six consecutive contributions have actually been made, the status exists, and the investor never agreed to anything. "This person made six consecutive contributions in 2026" is a historical fact. A fact cannot stop being true because of something that happened in 2029.
2. **Requiring six fresh consecutive periods is a reset**, and the governing rule of the whole model is step-down, never reset. It would also be the harshest reset in the design, because it strips benefits wholesale rather than by a step.
3. **It would be double jeopardy.** The same missed payment already costs the streak, the tier, the fee discount and the credit ladder's progress. Adding a fourth consequence to one event does no extra retention work; it just raises the odds the customer leaves.

**What suspends instead:** the tier steps down, the credit ladder stops climbing, and the entry-fee discount falls with the tier. That is the entire consequence, and it is already proportionate.

**Correction owed:** `_draft_sip-spot-and-ics.md` §5 and `_draft_purchase-structure.md` §3.4 both say "Confirmed SIP suspends" in the no-payment row. Replace with "the tier steps down and the credit ladder stops climbing."

**The residual risk, checked and small.** A customer who contributes six times, is Confirmed, then stops forever, keeps a permanent key to a door that leads nowhere: their tier has decayed, their credit ratio is whatever the decayed tier gives, and their collateral is whatever they hold. Permanence is worth almost nothing to a lapsed customer and it is worth a great deal to a returning one.

---

## 5. Retention: the rule that makes cycling pointless

This is the core of the rule book. Everything else is administration.

### 5.1 The exploit, stated honestly

The score measures behaviour, and the only behaviour it measures is whether payments arrive. So an investor can contribute USD 20, redeem the gold two days later, and repeat. The streak is perfect, the tenure accrues, the tier climbs, and they hold nothing. The obvious version of this is a nuisance. **The version that costs money is the second half: reach a top tier for a few dollars, then buy a large position and borrow against it at 95% instead of 50%.** On a USD 100,000 position, the difference between the bottom and top LTV is roughly USD 45,000 of credit, obtained for the price of twelve cycled contributions.

**And Aurumix cannot price it out at the exit, because VARA Rule III.E.4 prohibits charging any fee on redemption.** The normal commercial answer to churn behaviour is unavailable by law. **The score has to do all of the work.** This is worth saying out loud to the client: the regulatory constraint is what forces the scoring design.

**Why the previous proposal failed.** "A period counts only if the gram balance at period end exceeds the balance at period start" is defeated by keeping a token fraction: redeem 0.169 of the 0.17 grams, keep 0.001, and the balance rose. Any test that looks at a *direction* can be satisfied by a rounding error. The test has to look at a *proportion*.

### 5.2 The mechanism

> **ICS is earned by two things: payments made, and gold-months held.**
>
> **Retention (R) = (gram-months you actually held) ÷ (gram-months you would have held if you had never sold).**

Both figures are running totals over the life of the account. Each day, add the day's closing gram balance to the numerator, and the account's cumulative-grams-ever-acquired to the denominator. Two counters and one division.

**The score is then scaled by it:**

```
ICS  =  ( Continuity + Tenure + Supplementaries )  x  R_applied

R_applied  =  min( 1 ,  R / 0.80 )
```

**The 0.80 is the holding allowance, and it is the sentence the customer reads:** *you can take out up to a fifth of everything you have ever bought without touching your score.*

### 5.3 Why this works where the other proposals did not

| Property | Consequence |
|---|---|
| **It is a proportion, not a direction** | Keeping a token fraction does nothing. The threshold scales with everything you have ever contributed |
| **It is weighted by time** | You cannot buy back the day before a tier review. A one-day position adds one day |
| **It is scale-free** | A USD 20 saver who never sells and a USD 2,000 saver who never sells both score R = 1.00. **The binding constraint survives exactly** |
| **It measures a decision, not a capacity** | Keeping is a behaviour. This is not amount re-entering the score by the back door |
| **It degrades smoothly** | Withdrawing 30% costs a fraction of a tier, not a streak. No cliffs |
| **It rebuilds slower than it decays, arithmetically** | Lost gram-months are gone from the numerator forever, so R recovers asymptotically. The rule the client asked for falls out of the arithmetic instead of being bolted on |
| **It needs no channel tagging** | Two account-level counters. **Decision 41 survives: grams stay fungible and no ordering rule is needed on a partial exit** |
| **It starts at 1.00** | A new investor is never penalised for being new. R is defined as 1.00 when the denominator is zero |

### 5.4 It is a reward for holding, not a penalty for redeeming, and that distinction is a compliance point

III.E.4 prohibits fees on redemption. A rule that said "redeem and lose your status" is not a fee, but it is a penalty attached to the act of redeeming, and it invites the argument that it impairs the redemption right in substance.

**Retention is built the other way round.** Gold-months earn score. Grams that leave simply stop earning. Nothing is deducted, nothing is triggered, and no event fires on the redemption itself. **Write it and describe it in exactly that direction**, because a cliff-shaped rule and a smooth accrual rule with the same economics are not the same rule in front of a regulator.

### 5.5 What Retention does not catch, stated plainly

**A large holder with a static position can cycle a small SIP alongside it and R will not notice**, because the ballast keeps the ratio near 1.00. This is real and it is not fixable by any balance-based test.

**It is also not worth fixing, and the reasoning matters.** Cycling is attractive only when the contribution is large relative to the exploiter's means. For someone holding a kilogram of gold, honest compliance costs USD 20 a month and the cycling saves nothing worth having. They hold real metal for real time, which is the behaviour the product wants. The cost to Aurumix is the rail fees on twelve debits and twelve payouts a year.

**They are caught by Layer 3 anyway** (§9), which exists precisely for the residue.

**Foolproof means unprofitable, not impossible.** No scoring rule is unbreakable. The test that matters is whether the cheapest way to obtain the benefit is to do the thing the benefit exists to reward, and after §9 it is.

---

## 6. Paying: rails, mandates, limits and variable amounts

### 6.1 Frequency is fixed monthly. Amount is variable

**Frequency is fixed** because the score counts periods. Mixed frequencies make tenure farmable and make tier ladders non-comparable between customers. Someone who wants to add money mid-month makes a spot purchase.

**The date is flexible** (the investor's own anniversary), because the period is the calendar month and the date therefore cannot affect counting. It spreads collection load across the month.

**The amount is variable month to month**, client-confirmed. Only the floor is tested.

### 6.2 The rails: push only at launch. UAEDDS is dropped

> 🔄 **Decision, 2026-08-10, Abdur.** Direct debit is dropped from the launch design entirely. The launch rails are **AANI Request to Pay** (default) and the **prefunded balance** (§6.3). **AANI electronic direct debit is adopted when it goes live**, which restores true pull collection on a better rail than UAEDDS ever was.

**What AANI is, for the record.** AANI is the UAE's national instant-payments platform, operated by Al Etihad Payments, a subsidiary of the Central Bank, and built on the same technology as India's UPI (Al Etihad Payments partnered with NPCI International to build it). Transfers are account to account, real time, around the clock. **Request to Pay** is its collection feature: Aurumix sends a payment request on the contribution date, the investor gets a notification in their own banking app and approves with one tap, and the money moves instantly. An unanswered request simply expires. Nothing bounces, nothing is returned, and no bank fee is triggered, because nothing was ever presented against an account without authority. The UPI lineage also means the target customer, the Indian-origin saver, already knows exactly how this works.

| Rail | Investor action | On failure | Use |
|---|---|---|---|
| **AANI Request to Pay** | One tap per month | Nothing. The request expires. No fee | **Default** |
| **Prefunded balance** (§6.3) | One transfer covering several months | A draw against an empty balance is just a miss | **The honest "set and forget"** |
| **AANI electronic direct debit** | None | Unknown, check at go-live | Target state. Announced, not live |

**Why the pull rail is dropped, three reasons, each sufficient:**

1. **It deletes the mandate machinery.** No mandate, no ceiling, no amendment flow, no ceiling-versus-declared-amount failure case. The declared amount is just the number on this month's request, freely variable.
2. **It deletes the bounce-fee problem.** A returned UAEDDS debit costs the investor a bank charge (AED 26.25 at ENBD, see the correction below); a failed Request to Pay costs nothing. The entire no-re-presentment policy, the failure ladder's debit rows and the push-switch machinery become unnecessary.
3. **It deletes the single largest unverified dependency.** Whether UAEDDS supports variable-amount mandates under a ceiling was §13's first item and blocked the amount-variable decision. The question is now moot.

> 🔄 **Fee correction, 2026-08-10, and it stands recorded even though the rail is dropped.** The drafts carried **AED 105** as the returned-debit charge, sourced to the ENBD Schedule of Charges. Verified against the ENBD Personal Banking Schedule of Charges (November 2023, read in full): the line for a bank-account collection failure is **"Failed Standing Instruction and DDS: AED 26.25"** inclusive of VAT, on every account package. **AED 105 is the returned-cheque charge and the credit-card direct debit return fee**, a different line. So decision 35's "143% of a USD 20 contribution per bounce" overstated it; the true figure was ~36%. The no-blind-retry conclusion was right anyway, and is now moot.

**Rules that survive the rail change:**

- **Reducing your amount is free, instant and never scored.** This is a retention rule, not an administrative one: the alternative to reducing is quitting, and insurance lapse data says people choose quitting when reducing feels like failure.
- **Nudges, not retries.** The request stays open through grace, with reminders on days 1, 3 and 5. Push carries no failure fee, so nudge freely.
- ⚠ **Marketing rule.** On Request to Pay, say **"one tap a month"** and mean it. **"Set and forget" may only be promised on the prefunded balance** until AANI electronic direct debit is live.

> ⚠ **New commercial unknown, replacing the old one.** Which acquiring bank or PSP will originate merchant Request to Pay collections for a gold-token merchant, and at what per-request cost? Non-public onboarding criteria, same class as the PSP question in `handoff.md` §7. The per-request cost also feeds the Phase 4 rail-cost line (the parked collection-economics file assumed UAEDDS pricing).

### 6.3 Prefunding, which the drafts do not have and the persona needs

🔄 **2026-08-10: prefunding is promoted to first-class, not a side feature.** With the pull rail dropped it is the only rail on which automatic saving can honestly be promised, so the signup flow should prompt **"fund three months at once"** as a default suggestion, not bury it in settings.

An NRI paying USD 75 a month by international wire can pay USD 15 to 50 in wire fees on each transfer. Twelve wires a year is indefensible.

> **Allow a prefunded contribution balance.** The investor remits once. The money sits as **client money** in the designated Client Account, is drawn monthly at the declared amount, and each draw counts as one period, priced at the fix on the draw date.

**Why this is not the twelve-payments-in-January exploit.** Periods count as money is drawn and converted to gold, one per calendar month. Prefunding is *more* commitment, not less, and the undrawn balance is refundable on request because it is still the investor's money and has bought nothing.

**Compliance note:** an undrawn balance is client money under VARA Part IV throughout. It is not revenue, it is not a deposit, and it must sit in the Client Account until the moment title transfers.

---

## 7. What happens when a payment is missed

### 7.1 The ladder

| Case | Gold | Score | Rail action |
|---|---|---|---|
| Contribution at or above the floor, on time | Allocated | **Accrues** | None |
| Contribution at or above the floor, paid **late but inside 5-day grace** | Allocated at the fix on the day funds clear | **Unaffected** | Request stays open. Nudges on days 1, 3 and 5 |
| **Payment below the floor** | **Rejected and returned. Nothing allocated** | Not a contribution. The period stands or falls on an accepted payment | The request stays open for the full amount |
| **Nothing cleared by the end of grace** | **Untouched** | **Continuity halves. Tenure, Retention and gold untouched** | Request expires. Next month's request unaffected |
| **Arrears cleared inside 12 months** | Allocated at the fix on the day arrears clear | **Restored per the §11 revival rule** | Normal |
| Spot purchase | Allocated | **No period** | n/a |

### 7.2 The rules underneath the table

- **Grace is 5 days** from the contribution date. 🔄 **Revised 2026-08-10 from 15, Abdur's call.** The push rail needs no bounce-recovery window, so grace only covers being busy or away, and 5 days does that. Two build rules: calendar days, and **grace never expires on a weekend or public holiday**, it rolls to the next business day, or a Friday failure eats half the window. ⚠ A deliberate departure from the IRDAI 15-day standard; revisit if field data shows late payments clustering just past day 5.
- **Grace crosses the month boundary and settles the period it was due.** A payment on 3 March for a 28 February date closes February. **March still needs its own payment.** A late payment can never close two periods.
- **The step-down halves the streak. It does not reset it, and it never touches tenure.** A saver at 24 months of streak drops to 12, which is roughly one tier. They keep every period they ever paid.
- **Rebuild is slower than decay, without a special rule.** The loss is instant and the streak rebuilds at one point per period, so a halved 24-month streak takes twelve months to restore.
- **Repeated misses grind, they do not zero.** Halving twice takes 24 to 6. Tenure is the floor under the whole score, which is why continuity and tenure must stay as two components.
- **Arrears are one payment, not instalments.** Partial revival is a state the tier ladder cannot represent.
- **Arrears buy gold at the fix on the day they clear**, never at the missed period's fix. Otherwise revival is a free one-directional look-back option on gold, exercised only after the price has risen.
- **The step-down applies at grace expiry and reverses on revival.** No separate rule is needed for someone who pays on day 20.

> **The governing promise, unchanged and worth repeating in these words:**
> **You can lose your status. You can never lose your gold.**

### 7.3 A failure and a decision are different events

Involuntary churn runs 20% to 40% of total subscription churn. Of the six in ten investors gone by month 61, a quarter to a third never decided to leave: a payment failed and the product treated it as a choice.

🔄 **Revised 2026-08-10: dropping the pull rail solved most of this section's problem at the rail layer.** There is no bounced debit to masquerade as a decision any more. What remains is smaller but real: a request the investor never saw (phone lost, app notification broken, travelling) versus one they saw and declined. **Log delivery and open events on every request from day one**, so calibration can still separate "never saw it" from "chose not to", and keep the two categories in the data model.

---

## 8. The parallel states

> 🔄 **Revised 2026-08-10: the declared pause is deleted.** A free tap-to-pause is a free option: every sophisticated customer about to miss taps it, the unsophisticated take the step-down, and a field on which every rational customer does the same thing carries no information. That is the same argument that deleted the commitment period, the declared minimum and the customer-set floor, applied one more time. Its removal also deletes the cap-tracking (3 periods per 12 months) that came with it. A customer who needs a break simply misses, and the step-down is already mild by design: that is what "miss-tolerant scoring" is for.

Two rules and one housekeeping state remain, and none of them involves a request or a review.

| State | Trigger | Gold | Continuity | Tenure | Retention | Confirmed SIP |
|---|---|---|---|---|---|---|
| **Regulatory block** | Compliance blocks the account (e.g. the investor becomes India-resident). **A system event, not a request** | Retained | **Frozen** | Frozen | Keeps running normally | Retained |
| **Stop** | The investor cancels | Retained | Decays as normal | Held | Keeps running normally | **Retained** |
| **Dormant** | 12 consecutive silent periods. The SIP instruction auto-cancels; account goes hold-only | Retained | Held at its decayed level | Held | Keeps running normally | **Retained** |

**The regulatory block is one line of logic: months in which Aurumix refuses the investor's money do not count against them.** Nobody applies for it and nobody verifies it: the same compliance event that blocks contributions freezes the clock. Scoring someone down for payments the product itself refused would punish them for obeying a rule Aurumix enforced, which is incoherent in front of a customer and worse in front of a regulator. Existing credit runs to term; no new draws. Whether a returning NRI may keep contributing from funds acquired abroad (FEMA s.6(4)) is an open counsel question; if counsel says yes, this state simply fires less often.

**Dormancy is housekeeping, not a protection.** It only says: after 12 silent periods, stop sending requests and close the SIP as an instruction. It has no score meaning, because the score has already decayed on its own by then.

**Retention needs no special rule in any of these states**, which is a useful property of measuring holding rather than paying. A blocked investor who holds their gold keeps R = 1.00 automatically.

**Restarting is never a reset.** A dormant or stopped account that restarts resumes from wherever decay left it. Nothing is re-earned, and nothing is forgiven either.

---

## 9. The anti-gaming register

Three layers. Layer 1 is arithmetic and closes the exploit. Layer 2 removes the prize. Layer 3 catches the residue.

### 9.1 Layer 1: the score itself

| # | The play | What they hope to win | What stops it |
|---|---|---|---|
| 1 | Contribute, redeem two days later, repeat | Tier without capital | **Retention.** R falls to about 0.015 in the first year and 0.003 by year five |
| 2 | Keep a token fraction so the balance "rose" | Defeat a direction test | R is a **proportion** of lifetime purchases, not a direction |
| 3 | Sell out, buy back the day before tier review | Window-dress the snapshot | R is **time-weighted over the account's life**. A one-day position adds one day |
| 4 | Pay twelve months upfront | Twelve periods at once | **One counted period per calendar month.** Prefunded money is drawn monthly |
| 5 | Split one payment into five small ones | Five periods | **One counted period per calendar month**, and sub-floor payments are rejected at the door |
| 6 | Move the contribution date backwards | Squeeze in an extra period | **The period is the calendar month.** The date is a collection convenience |
| 6b | Tap "pause" just before missing, to shield the streak | A free miss, on demand | **The pause state no longer exists** (§8). A miss is a miss, priced by the step-down |
| 7 | Cancel and reopen to escape a decayed streak | A fresh streak | **The score attaches to the verified identity, not the account.** The permissioned token already requires identity, so this costs nothing to enforce |
| 8 | Transfer grams to a spouse instead of redeeming | Extract value, keep R | **An outbound transfer is an outflow.** For the receiver, inbound grams add to **both** sides, so nothing is created |
| 9 | Revive arrears only after gold rises | A free look-back option | **Arrears price at the fix on the day they clear** |
| 10 | Declare USD 500, pay USD 20 | A cheap tier | **Not an exploit. This is the design.** They get the same rate on one twenty-fifth of the gold |

### 9.2 Layer 2: remove the prize

| # | The prize | Why it is worth taking | The defence |
|---|---|---|---|
| 11 | **Credit.** Cycle to a top tier, then buy a large spot position and borrow at 95% | The largest single payoff in the product. Roughly USD 45,000 of extra credit on a USD 100,000 position | **90-day collateral seasoning**: grams count toward the borrowing base only after 90 days held, and redeemed-then-rebought grams start again. **The LTV is struck at the tier on the day of the draw.** Plus Retention |
| 12 | **Agent commission.** An agent coaches clients to cycle, and earns on each contribution | **The sharpest version, because it extracts real cash from Aurumix** | **Commission vests over 12 months and claws back if the grams are redeemed inside the window.** This is the standard insurance early-lapse clawback and the agent network is already built on that model |
| 13 | **Referrals.** Sign up dormant referees | Supplementary score points | **Referral points accrue per counted period of the referee**, not per signup, and are capped |
| 13b | **Referrals, second order.** Recruit cyclers, who do pay every month | Referral points from referees who are worth nothing to Aurumix | **Each referee's contribution is scaled by that referee's own Retention.** §9.4 |
| 14 | **Gold Rewards** | A grams payout | Already **capped at what that customer generated** in interchange and credit revenue. Self-limiting by construction |
| 15 | **Entry-fee discount**, now applying to spot as well | A cheaper purchase | **Not exploitable.** A price reduction is bounded by the money handed over and there is no payout to farm. Round trip proved in §1.1 |

> **Note what the entry fee already does.** A cycler pays the fee on every cycle and recovers nothing on the way out, because III.E.4 leaves the exit free. The fee is an unavoidable per-cycle toll and it is the only part of the economics still standing. ⚠ **§1.1 lowers that toll at high tiers.** Retention is what makes this acceptable: a cycler never reaches a high tier, so the toll they actually pay is the top-of-range rate.

### 9.3 Layer 3: the anti-abuse right

**A round-trip flag.** A redemption within 30 days of a contribution, occurring in 4 or more months out of any rolling 12, marks the account: **tier progression freezes pending review**, nothing is deducted, and the gold and the existing tier are untouched.

This is not a fee and not a penalty. It is the review right that every platform holds, and it exists for the case Layer 1 provably cannot see (§5.5) and for whatever nobody has thought of yet. `_draft_purchase-structure.md` §5.3 already wants a rapid in-and-out pattern flag as an exit check; this is the same signal, used once.

**Write it into the terms as a reserved right, exercised on review, with a stated appeal path.** An automatic punishment on this signal would catch real customers with real emergencies.

### 9.4 Referrals: you earn from a referee to the extent that referee is real

Referral points accrue **per counted period of the referee**, never per signup, which stops someone farming registrations. That leaves one gap, and it is the cycling exploit reappearing one level out: **a cycler does pay every month**, so they generate counted periods, so an agent could recruit ten cyclers and collect referral points on customers who are worth nothing to Aurumix.

> **Rule. Each referee's contribution to your referral points is multiplied by that referee's own Retention.**
>
> `Your referral points = capped sum over referees of ( their counted periods x their R_applied )`

**Why this is the right shape.** It applies the same test to the referrer that the referrer's own score already faces, so there is one idea in the model rather than two. You cannot earn from someone else's behaviour by more than that behaviour is worth. And it needs no new data: R is already computed for every account.

**It also closes the score half of an exploit whose cash half is already closed.** Agent commission vests over 12 months with clawback on early redemption (§9.2, item 12). That protects Aurumix's cash. This protects the score. **Same exploit, two currencies, and both now covered.**

Referral points are therefore recalculated monthly along with everything else, since a referee's R moves.

⚠ **Check this against the agent commission design when the IRDAI 2023 caps are finally retrieved.** The agent network is the one place where scoring and cash incentives sit on the same event, and they must not pull in opposite directions.

### 9.5 Family portfolios, which were circular

Family portfolios currently appear as **both** a capped ICS input and a tier-gated benefit, so you need the tier to unlock the thing that raises your tier. That is the same bootstrap deadlock the two-class model had at the front door.

> **Fix: open to everyone, and it scores.** The behaviour wanted is more family members contributing, and gating it behind a tier suppresses exactly that. It also removes a regressive component.

**No double counting.** A sub-account's contribution earns a full period for **the sub-account's own score**, plus capped supplementary points for the head. One payment never earns two full scores. Sub-accounts are separately KYC'd real people, which the permissioned token already requires.

---

## 10. Withdrawal, exit and transfer: what each one costs

| Event | Gold | Continuity | Tenure | Retention | Notes |
|---|---|---|---|---|---|
| Partial redemption | Leaves | Untouched | Untouched | **Falls, in proportion and over time** | Free of charge, always, by law |
| Full redemption, still contributing | Leaves | Untouched | Untouched | **Falls toward zero over time** | They keep climbing, from a scaled score |
| Full exit and close | Leaves | Held at its level | Held | Held | **Score persists against the identity.** A returner resumes, never restarts |
| Outbound transfer | Leaves | Untouched | Untouched | **Falls, same as a redemption** | Otherwise transferring to a spouse dodges R |
| Inbound transfer | Arrives | Untouched | Untouched | **Neutral.** Adds to both sides | Received grams start a fresh seasoning clock for credit |
| Gold Rewards paid in grams | Arrives | Untouched | Untouched | **Neutral.** Adds to both sides | Cannot be used to inflate R |
| Pledged as collateral | Stays owned | Untouched | Untouched | **Counts in full** | Pledged gold still earns. Client's stated intent |
| **Collateral liquidated on default** | Leaves | Untouched | Untouched | **Falls** | Real and must be disclosed in the credit terms |

**Two rules that are easy to get wrong and expensive to get wrong.**

1. **A tier step-down must never trigger a margin call.** Existing drawings run to term at the LTV they were struck at. Only new draws use the new tier. Without this rule, a missed USD 20 payment could force a liquidation, which would convert "no financial penalty for a miss" into a lie.
2. **Tier is recalculated once a month, at period close.** Benefits that flicker daily are unusable, and a daily recalculation would make the round-trip flag much harder to read.

---

## 11. Proposed parameters

> ⚠ **These are proposed defaults for B4, not settled decisions.** The structure above does not depend on them. They are set here so the design can be tested rather than debated in the abstract.

| Component | Proposal | Reasoning |
|---|---|---|
| **Tenure** | 1 point per counted period, **capped at 60** | Five years. Makes the ceiling reachable and stable |
| **Continuity** | 1 point per consecutive counted period, **capped at 24** | Two clean years maxes it, so the step-down stays meaningful for life |
| **Supplementaries** | **Capped at 15 total**: referrals 8, family 5, Masterclass 2 | About 15% of the maximum. Enough to matter, not enough to substitute for saving. If they were large, the top tier would go to the best recruiter rather than the best saver |
| **Referral points** | Referee's counted periods **x that referee's own Retention**, capped at 8 | §9.4. You earn from a referee to the extent that referee is real |
| **Maximum base** | 99 | |
| **Retention** | `R_applied = min(1, R / 0.80)` | The 20% holding allowance |
| **Step-down** | Continuity **halves**, rounded down | Instant loss, one point per period to rebuild |
| **Revival** | 🔴 **OPEN. Deferred to B4 with the formula.** Full restoration was the working default and it does not survive scrutiny | **It contradicts §9.1 item 4.** If arrears fully restore the record, eleven months of arrears paid as one lump produces a perfect eleven month record, which is the prepayment exploit arriving backwards. **Likely answer: arrears restore total periods but never the streak**, since paying late does not make it untrue that you were late. **Do not build against full restoration** |

**Tier thresholds, defined as lower bounds:** T1 at 0, T2 at 10, T3 at 20, T4 at 35, T5 at 50, T6 at 65, **T7 at 80**.

⚠ **Define these as lower bounds, never as ranges.** ICS is a real number because it is multiplied by Retention, so bands written as "65 to 79" leave a score of 79.2 in no tier at all. This is a build note, and it is the kind of thing that ships.

### 11.1 Testing it against the binding constraint

A **USD 20** saver, never misses, no referrals, never sells:

| Month | Tenure | Continuity | R | ICS | Tier |
|---|---|---|---|---|---|
| 6 | 6 | 6 | 1.00 | 12 | **T2.** Confirmed SIP |
| 12 | 12 | 12 | 1.00 | 24 | T3 |
| 24 | 24 | 24 | 1.00 | 48 | T4 |
| 36 | 36 | 24 | 1.00 | 60 | T5 |
| 48 | 48 | 24 | 1.00 | 72 | T6 |
| **56** | 56 | 24 | 1.00 | **80** | **T7** |

**The constraint is satisfied at month 56 on contributions alone, with no referrals and no family.** A USD 2,000 saver on the same record reaches T7 on the same day, with a hundred times the gold. That is the founding principle made arithmetic, and it is the single most useful sentence in the whole model when a regulator asks whether the benefit scales with capital.

### 11.2 Six people at month 60

| Persona | Tenure | Continuity | R | R_applied | ICS | Tier |
|---|---|---|---|---|---|---|
| **A.** USD 20, perfect, never sells | 60 | 24 | 1.00 | 1.00 | 84 | **T7** |
| **B.** As A, plus 2 referrals and a family sub-account | 60 | 24 | 1.00 | 1.00 | 94 | **T7** |
| **C.** USD 2,000, perfect, never sells | 60 | 24 | 1.00 | 1.00 | 84 | **T7** |
| **D.** Cycler: contributes and redeems every month | 60 | 24 | 0.0033 | 0.004 | **0.3** | **T1** |
| **E.** Withdrew half at month 36, kept saving | 60 | 24 | 0.754 | 0.943 | 79.2 | T6 |
| **F.** Withdrew everything at month 36, kept saving | 60 | 24 | 0.508 | 0.635 | 53.4 | T5 |

**Read D against A.** Identical payment records. Identical continuity, identical tenure, both Confirmed SIP since month six. **Six tiers apart**, on one number that cannot be faked.

**Read E and F against A.** A legitimate 50% withdrawal at year three costs **exactly one tier**. A full liquidation costs two. Both keep every gram they still hold, both keep climbing, and neither loses their Confirmed SIP status or their history.

> **Retention has a memory, and a late withdrawal costs less than an early one.** The same 50% withdrawal taken at month 24 instead of month 36 lands at almost the same place by month 60 (R = 0.757), because what is being measured is the whole life of the account. A customer who held perfectly for five years and then sold everything takes roughly two years to fall two tiers. **That asymmetry is deliberate.** It is the mirror of rebuild-slower-than-decay, and it is what makes the score worth accumulating rather than worth restarting.

> **The one calibration dial left.** The holding allowance is set at 0.80. Raising it toward 0.90 makes the design stricter on legitimate withdrawals and does almost nothing to the cycler, who sits more than two orders of magnitude below the threshold either way. **Recommend 0.80 at launch and revisit only if field data shows partial withdrawals are common and are costing tiers.**

---

## 12. What this changes in the existing drafts

- [ ] `_draft_purchase-structure.md` §3.1: **delete the declared minimum** as a customer-set field. Replace with the product floor.
- [ ] `_draft_sip-spot-and-ics.md` §5 and `_draft_purchase-structure.md` §3.4: **"Confirmed SIP suspends" is wrong.** Replace with "the tier steps down and the credit ladder stops climbing."
- [ ] `_draft_sip-spot-and-ics.md` §4: **add Retention** to the component table as a multiplier, not a component.
- [ ] `_draft_sip-spot-and-ics.md` §5: the step-down is now specified as **halving the streak**, and the miss table gains the partial-payment and debit-rejected rows.
- [ ] `_draft_sip-spot-and-ics.md` §1 and §2: **lever 3 is still owed.** The decaying spot redemption fee is prohibited and the tenure rebate that replaced it is parked.
- [ ] `_draft_sip-spot-and-ics.md` §4: **family portfolios must stop being tier-gated.**
- [ ] `_draft_sip-spot-and-ics.md` §1 table and `_draft_purchase-structure.md` §4.1 table: **"Flat, top of range, no discount" is superseded.** Spot is priced at the account's earned tier. §1.1.
- [ ] `_draft_purchase-structure.md` §4.3: the list of what spot deliberately does not get **keeps ICS, credit, card and family, and loses the entry-fee discount.** The heading claim "restrict benefits, not supply" is unchanged and still correct.
- [ ] Entry-fee design (B-block): **the base rate must sit above the top-tier price** so the ladder is funded by uplift rather than margin. Same question as the parked tenure rebate, and it should be answered once.
- [ ] Both drafts: **the period is the calendar month**, stated nowhere at present, and several edge cases depend on it.
- [ ] Credit design (B-block, not yet written): **90-day collateral seasoning**, **LTV struck at the draw date**, and **a tier step-down must never trigger a margin call.**
- [ ] `_draft_sip-spot-and-ics.md` §4: **referral points are earned per counted period of the referee, scaled by that referee's Retention**, never per signup. The component table currently says only "investors onboarded", which is the farmable version.
- [ ] Agent economics (blocked on the IRDAI 2023 caps): **commission vests over 12 months with clawback on early redemption.** This is the defence against the sharpest version of the cycling exploit and it must be designed in, not added later.
- [ ] Client's document §6.3: "six consecutive events at the same monthly commitment" resolves to **six consecutive calendar months in which a cleared contribution of at least the floor arrived.**

**Added 2026-08-10, from the payment-layer revision:**

- [ ] `_draft_purchase-structure.md` §3 and §6: **UAEDDS is dropped.** The SIP failure ladder loses its debit-rejected and re-presentment rows; grace is 5 days, not 15; the declared minimum and the partial-payment state are deleted; the three-SIP-states table loses the declared pause. The money-in stage descriptions need re-cutting onto AANI Request to Pay and the prefunded balance.
- [ ] `_draft_sip-spot-and-ics.md` §5: the five-case miss table is superseded by §7.1 here (grace 5 days, below-floor rejected, no debit rows). The "pays less, at or above the declared minimum" row no longer exists.
- [ ] `_explainer_how-we-take-money.md` and `Aurumix_Process_Maps_Payments.md`: **UAEDDS as the domestic collection default is superseded.** Launch collection is AANI Request to Pay plus prefunding. The four-payment-paths diagram needs a revision pass.
- [ ] `Aurumix_Process_Maps_SIP_Structure.md` and `Aurumix_Process_Maps_SIP_Spot_ICS.md`: revision pass owed for the same five changes (hard floor, 5-day grace, no UAEDDS, no declared pause, AED 26.25).
- [ ] `_parked_collection-economics-and-minimum-ticket.md` (reopens Phase 4): the rail-cost line assumed UAEDDS per-debit pricing. Recompute on AANI Request to Pay per-request pricing once a provider quotes it.
- [ ] `handoff.md` decisions 21, 35 and 36: revised in the same pass as this edit; decision 43 added.

---

## 13. Still open

| Item | Owner | Why it matters |
|---|---|---|
| ~~**Does UAEDDS support variable-amount mandates under a ceiling?**~~ | ✅ **MOOT 2026-08-10** | The rail is dropped (§6.2). The question no longer exists |
| **Which bank or PSP will originate merchant AANI Request to Pay for a gold-token merchant, and at what per-request cost?** | Us, then the client's bank conversations | The new load-bearing rail unknown, replacing the UAEDDS one. Non-public onboarding criteria; the cost feeds the Phase 4 rail-cost line |
| **AANI electronic direct debit go-live date and terms** | Us, watch | It is the target state that restores true automatic collection |
| The **weights and thresholds** in §11 | Us, B4 | Proposed, not settled. The structure holds whatever the numbers become |
| **How the discount ladder is funded**: uplift to the base rate, or out of margin | **Client.** Their revenue | §1.1. At Year 1 margin is 0.85pp, so a margin-funded ladder is about 0.12pp per tier and the lever is decorative. 🔄 2026-08-10: the ladder is now the only draw on the uplift, since the tenure rebate is retired (decision 44) |
| **The ICS benefit set is CLOSED at five** (decision 44): entry-fee discount, credit LTV ladder, card tier, Gold Rewards rate, Digital Will and family services discount | ✅ Decided 2026-08-10 | The tenure rebate is retired: Retention now does its job structurally. B4 prices these five and nothing else |
| The **differential fee structure** for spot versus SIP | **Client.** Sits in the Google Drive folder we still cannot access | Already listed as blocking fee design in `handoff.md` §7. §1.1 makes the two rates equal for a given tier, which is the input this needs |
| The **holding allowance** at 0.80 | Us, revisit post-launch | The single calibration dial |
| **Referral and family caps** | Us, B4 | Must stay small enough that they cannot substitute for saving |
| Whether the **round-trip flag** thresholds (30 days, 4 in 12) are right | Us, post-launch | Cannot be calibrated without data. Set conservatively and review |

---

## 14. Sources and precedent

| Claim | Source | Confidence |
|---|---|---|
| No fee may be charged on redemption | VARA Rulebook Annex 2, Rule III.E.4, verified verbatim | **High.** Primary source |
| 15-day grace, monthly mode | IRDAI Master Circular, clause 8(a) | **High.** Verified. 🔄 Aurumix departs from it deliberately: grace set to 5 days on 2026-08-10, Abdur's call, because the push rail needs no bounce-recovery window |
| Cumulative bonus shape: earned slowly, capped, lost by a specific event, base never touched | Indian health insurance | **High** |
| Commission clawback on early lapse | Indian life insurance standard practice | **High** on the practice. ⚠ **The IRDAI 2023 caps are still unretrieved and still block agent economics** |
| Persistency: ~79% at month 13, ~38% at month 61 | Indian life insurance | **High** |
| Involuntary churn is 20% to 40% of total churn | ProfitWell; Forrester 34% | **Medium** |
| ~~ENBD returned direct debit fee AED 105~~ 🔄 **CORRECTED 2026-08-10: "Failed Standing Instruction and DDS" is AED 26.25 incl. VAT, all account packages. AED 105 is the returned-cheque charge and the credit-card direct debit return fee, a different line** | ENBD Personal Banking Schedule of Charges, November 2023, read in full; corroborated against the ADCB Schedule of Fees | **High.** Primary source. The earlier Medium-High figure was a conflation |
| Direct debit failure 2-3%, recurring card 10-15% | Recurly, GoCardless | **Medium.** Context only now: the pull rail is dropped |
| ~~UAEDDS variable-amount mandates under a ceiling~~ | **Moot 2026-08-10**: rail dropped | n/a |
| AANI: Al Etihad Payments (CBUAE subsidiary), built with NPCI International on UPI technology; Request to Pay live, electronic direct debit announced not live | Al Etihad Payments / CBUAE public announcements | **Medium-High.** Re-verify eDDA status at build time |
