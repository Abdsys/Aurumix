# Aurumix Referral System

> **Status:** Phase 2 decision draft, 2026-08-13. Block B5.
> **Depends on:** decision 13 (anti-MLM), decision 20 (behaviour never amount), decision 22 (persistency governs), decision 42 (revenue streams), decision 44 (benefit set closed at five), decision 46 (ICS, and referrals removed from scoring).
> **Supersedes:** nothing. This is the first referral design. The 2026-08-11 scoring version was deleted, not replaced, and this document is what replaces it.

> 🔄 **REVISED 2026-08-13 (Abdur), five changes, and two of them make the design more principled than the version they replace.** **(1) The pool is 30% of the entry fee**, explicitly a placeholder locking against the revenue model. **(2) The USD 75 counting cap is removed** and the reward is computed on whatever the referee actually contributed, which makes it a **constant 19.4% of lifetime value at every ticket size** instead of collapsing to 3% for the best customers. **(3) The reward is credited in grams from launch**, which moves the gram-credit rail into the September build. **(4) There is no cap on how many people a member may refer**, which is what VARA's own referral case study describes, and single level now carries the anti-MLM defence alone. **(5) The agent network is a separate population**, not a rung above this one, so the automatic graduation door is deleted. ⚠ **Removing the counting cap opened one real hole** and it is register item 8: inflate the referee's contributions for exactly six months, then collapse. It is now held by a reserved right rather than by arithmetic, which is the weakest defence in the file.

> ⚠ **This draft has been through an adversarial review and it did not survive intact.** Three independent passes ran against the first version: an arithmetic check, a consistency check against the prior record, and a red team. **They found one false invariant that four separate conclusions were resting on, one rule missing without which decision 46 reopened by the back door, one genuine cash-extractive exploit, one trigger that could never fire for a returning customer, and a privacy disclosure that would have gone into a VARA licence application.** All are fixed and each fix is marked in place with what it replaced, so the reasoning is auditable rather than tidy. **The one thing review could not settle is the size of the reward**, which is a business decision and sits in §5.4 as an explicit three-way choice.

---

## 0. What this document decides, and what it does not

**Decides.** What a successful referral is. What the reward is, in what form, at what size, to whom. Who may refer and how often. How a member referral relates to the agent network. Where the money comes from. Every edge case we could find, and every attack we could think of.

**Does not decide.** The agent commission rates themselves. Those need the revenue model, which is Phase 4, and the client has gated them explicitly: *"Step 1 to this answer is the revenue model of our complete product."* What this document does supply is the **architecture the agent rates must sit inside**, the **budget rule that bounds them**, and the **interface between the two programmes**, all of which are needed before a rate can be set sensibly.

**One thing to read if you read nothing else.** A referral reward is not a benefit and not a score. It is an **acquisition cost**. That single reclassification is what lets the programme exist at all, because the benefit set is closed at five (decision 44) and the score has no room for it (decision 46). Acquisition costs have always come out of the entry fee, and the client has already agreed the principle for agents.

---

## 1. The problem

Three facts collided.

**Fact one: the client ranks referrals second.** Asked to rank the ICS inputs, they answered: *"TOP2: Longer lock in time line and continuous investment, Then reference, and then family plans."* Referrals are their third-highest priority overall and their highest priority outside the two savings behaviours.

**Fact two: their own document caps referrals into irrelevance.** Their §8.2 classes the referral network as *"Supplementary - capped… Cannot dominate the score. Maximum contribution bounded."* A component that is ranked second and simultaneously bounded so it cannot matter is not a specification. It is two instructions that cancel.

**Fact three: we removed referrals from the score entirely** (decision 46, §5 of the scoring draft), for three reasons that all still hold: they corrupt Months, which must mean months you paid or nobody can compute their own score; they are already paid by the agent commission; and a status bonus for recruiting is precisely the MLM shape decision 13 exists to defeat.

So the client wants referrals to matter more, and we made them matter zero. That looks like a straight refusal. It is not, and the resolution is the point of this document.

**The resolution: a score point is worth nothing until it crosses a tier threshold. A gram is worth a gram on the day it lands.** Under their own §8.2 a referral earns a capped supplementary point inside a score that then has to clear a tier boundary before the customer sees a single dirham of difference. Most referrals under that design would have changed nothing at all. Under this design every successful referral pays, immediately, in metal, to both parties.

**The sentence for the client: you asked for referrals to matter more. Scoring them made them matter less. We took them out of the score and paid for them instead.**

### 1.1 What the sector does, and why that matters

Verified across nineteen tokenised-gold protocols plus Glint, Goldmoney, BullionVault and OneGold: **exactly one runs a retail referral programme.** PAXG and XAUT, roughly 97% of the market between them, run none. Kinesis is the sole exception.

This is decision 13 restated with fresh evidence. *Not one of nineteen protocols has a savings plan, a recurring purchase, or a retail referral programme.* Distribution is the moat. A working referral programme is not a nice-to-have bolted onto a gold token; it is one of the two or three things that make this product a different category from PAXG.

**Kinesis is also the cautionary tale.** Its Referrer's Yield pays **7.5% of every referee's transaction fees, monthly, in gold and silver, described as a lifelong share of the fees**, and the referrer *"does not need to be an active system user"* (kinesis.money/referrers-yield, primary, High). Its Partner's Yield pays **up to 25% of a referral network's fees**, which is a downline. Two things follow. First, Kinesis can afford a lifetime revenue share because it earns recurring transaction fees forever on trading, spending and minting; **Aurumix earns a one-time entry fee and retains USD 1.61 on a USD 75 contribution**, so the model does not transfer. Second, a network-level yield is the shape that gets products reclassified, and §7 deals with it.

---

## 2. The architecture

**One budget. Three rings. One door between them.**

| Ring | Who | Paid | Contract | Level |
|---|---|---|---|---|
| **0. Direct** | Customer arrives on their own | Nothing | None | n/a |
| **1. Member referral** | An existing customer introduces someone they know | Once, in grams, at the referee's gate | None. Terms of use only | Single, always |
| **2. Agent network** | A contracted, trained, disclosed intermediary | Upfront share of entry fee plus trailing, vesting with clawback | Agent Agreement | Three, and they are **functions, not depths** (§7.2) |

**The two rings are separate populations, not two rungs of one ladder** (Abdur, 2026-08-13). An agent is a registered, contracted individual and is designed elsewhere. **A member is a customer who told a friend.** There is no automatic promotion from one to the other and no referral count that triggers one; §6.2 keeps only a reserved right to require a proper footing where someone is plainly running a distribution business.

**The line that carries the architecture: a bounty is a thank-you and needs no contract. An annuity is an income and needs one.** The member reward is a single payment per referral, forever. Recurring income lives behind a contract, on the other side of the wall.

That is not a stylistic preference. It is the direct lesson of the sharpest regulatory precedent available, in §7.1.

### 2.1 Why one budget and not two

Because otherwise the same customer gets paid for twice. If a member refers someone who is then booked into an agent's portfolio, or an agent routes a sale through their own customer account to collect both, Aurumix pays two acquisition costs for one acquisition. **One acquisition, one payment** is therefore a hard attribution rule, and it is §9.

It also gives the budget a single ceiling, which is what §8 is for, and which is how the only live comparable regime in the world does it.

---

## 3. What counts as a successful referral

> **A referral succeeds when the referee passes their own Confirmed SIP gate: six consecutive counted contributions, on their own account, under their own KYC, funded from a bank account in their own name.**

Nothing else counts. Not a signup, not a completed KYC, not a first payment, not a declared intention.

### 3.1 Why the gate, and why nothing else

**Because the product already has a definition of a real customer, and inventing a second one would be a mistake.** The Confirmed SIP gate is the same door the score sits behind (decision 46, amendment 1). Using it for referrals too means there is **one idea in the model rather than two**, which is the same argument that shaped the deleted R-scaling rule and the same argument that chose the minimum operator over a weighted sum.

**The gate carries anti-gaming properties we get for free.** From the scoring draft, all already decided, none of them new work:

| Property | Consequence for referrals |
|---|---|
| One counted period per calendar month | The gate cannot be compressed. **Minimum six calendar months between signup and any payout** |
| No revival, no arrears, no backdating | The gate cannot be bought retrospectively |
| Hard USD 20 floor, below which money is rejected and returned | No dust farming |
| Every account passes its own gate; nobody is carried in | A referee cannot inherit qualification from the referrer |
| Separately KYC'd real person | Sybil attacks must survive KYC |
| A regulatory pause freezes the run rather than breaking it | Handled, see §10 |

**Six of eleven gaming attacks are already structurally impossible at that gate.** The referral programme inherits all six and adds no new machinery.

**And it is the honest definition.** Six months of a person's own money, at their own pace, from their own bank account, is what a real customer looks like in a savings product with a 79%-at-month-13 persistency curve. Paying on a signup would pay for noise.

### 3.2 The market agrees, and it is not close

| Product | What triggers payment | Source |
|---|---|---|
| **Jar** (Indian gold micro-SIP, closest analogue) | The referee's **fifth** transaction | myjar.app, Medium |
| **Tanishq Golden Harvest** (gold instalment scheme) | Nothing at all below **six instalments** | tanishqgoldenharvest.co.in, Medium |
| **Mashreq NEO** | Account opened **and AED 3,000 deposited** by a deadline | Mashreq, High |
| **OKX Middle East** (VARA-licensed) | Referee holds **≥ AED 1,000 for a cumulative 30 days in a 90-day window**, else the reward *"may be forfeited, reversed, or otherwise reclaimed"* | OKX UAE referral terms, Medium-High |
| **Kinesis Silver Rewards** | Referee KYCs **and trades ≥ USD 3,000** | Kinesis support, High |

Every serious operator gates on sustained behaviour, and the two gold-savings products gate at five and six periods respectively. Aurumix gating at six consecutive is squarely in the middle of established practice, and it is stricter than all of them because ours cannot be satisfied with a single large deposit.

### 3.3 Attribution: when the link is made, and that it never moves

**The referral link attaches at account creation and is immutable thereafter.** Before KYC, before the first payment. There is no retrospective attribution, no code entered later, no transfer of a referral to a different referrer, and no reassignment on dispute.

Reason: any window in which attribution can still be changed is a window in which it will be sold. It also removes an entire class of support ticket.

**Consequence to accept:** a customer who genuinely was introduced by a friend but did not enter the code loses the reward for both parties. This is stated in the app at signup, once, plainly, and it is not appealable. The alternative is worse.

---

## 4. The reward

> **30% of the entry fee your friend paid in their first six months, split between you, credited as gold.**

Formally: the reward pool is **30% of the entry fee the referee actually paid over the six contributions of their qualifying run**, on whatever they contributed with **no counting cap**, split equally between referrer and referee, **credited in grams** to both accounts **thirty days after the gate resolves**, provided no contribution in the run has been reversed.

At a 5% entry fee that is **1.5% of the referee's six-month contributions in total, 0.75% to each side.**

> ⚠ **30% is a placeholder and is marked as one throughout.** It is set here so the mechanism can be reasoned about and worked through; **the number is locked after the revenue model** (Phase 4), alongside the agent commission rate and the acquisition-budget ceiling in §8.3. Everything in this document holds at any percentage. Nothing in it depends on 30 specifically.

> ⚠ **On wording, and it is a compliance point rather than a style one.** An earlier draft said *"one month's entry fee back, each"*, which is the same arithmetic and a misleading sentence. It sounds like a month of saving returned. It is 5% of one contribution, and 0.83% of what the referee actually handed over. **VARA Marketing Regulation I.C.2.l(i) prohibits incentives framed so as to divert focus from proper consideration**, and an incentive described so that it sounds several times larger than it is does exactly that. Describe it as a share of a fee, never as a share of savings.

**Why the thirty days.** It is not a vesting period and it does not test the referee's persistence any further. It exists for one reason: the prefunded balance is refundable on request (rulebook §6.3), so without a short window a customer could prefund six months, pass the gate, collect both halves, and then request the refund, retroactively deleting the run that earned the reward. **The window closes the only genuinely cash-extractive hole in the design.** Any reversal, refund or chargeback touching a contribution in the run voids the reward outright.

### 4.1 Why grams and not cash

| | Cash | Grams |
|---|---|---|
| Cost to Aurumix | Cash outflow | The wholesale gram price, on metal the float already holds |
| Where the value goes | Out of the product | Into the balance, raising the switching cost |
| VAT | Likely a taxable supply of services at 5% (unverified, §12.4) | Structurally further from a commission. Still needs the tax adviser |
| Precedent | Groww, Mashreq | Kinesis pays in KAU and KAG. Jar credits an in-app balance |
| Product fit | A gold savings product paying people cash to introduce people to gold | Consistent |
| VARA | Caught by Marketing Regulation I.C.2.l | **Caught identically.** Non-monetary remuneration is expressly in scope |

**Note the last row.** There is no VARA advantage to paying in metal. The reasons to prefer grams are economic and product reasons, not regulatory ones, and the draft should not claim otherwise.

🔴 **Build consequence, and it is decided rather than deferred (Abdur, 2026-08-13): the reward is credited in grams from launch.**

A gram credit is a title transfer of Aurumix's own metal, which is Gold Rewards machinery, and decision 41 sequences Gold Rewards to ship with the card because it is funded by interchange that does not yet exist. **The referral reward is funded by the entry fee, which exists on day one, so it does not wait for interchange. It does need the rail.**

> **So the gram-credit rail moves into the September build.** It is a smaller job than Gold Rewards proper (no interchange reconciliation, no per-customer revenue cap, no monthly netting) but it is the same primitive: transfer Aurumix metal into a customer holding and record it against the title register. **Raise it with the client alongside the upgradeable-proxy and multi-tenancy notes**, which are the other two build consequences already owed.

An intermediate version had the reward land as a **fee credit** at launch, converting to grams later. It is recorded and not taken. It was cheaper and it was worse: *"you both get gold"* is the product, a fee credit is an accounting entry, and a gold savings product that pays its referral reward in anything other than gold is explaining itself twice. ⚠ **One cost carries over from that version and is now accepted:** §12.4 records that a rebate against a customer's own fees is structurally further from a taxable supply of services than a payment in kind is, so **the gram form is the one that needs the VAT view** (§15, item 7).

### 4.2 Why both sides are paid

Two published findings point the same way and the second one is about products exactly like this one.

- **Gershon, Cryder and John (2020), *Journal of Marketing Research*.** Across two field experiments and an incentive-compatible lab experiment, **recipient-benefiting referrals recruited more new customers than sender-benefiting referrals.** Paying the referee is not generosity, it works better.
- **Dose, Walsh, Beatty and Elsner (2019), *Journal of the Academy of Marketing Science*.** Public referral rewards can **actively backfire for innovative or unfamiliar products**, and the negative effect is **attenuated by rewarding both parties.** A tokenised gold instrument sold to a first-time saver who has never held a wallet is precisely the unfamiliar product in that finding.

There is a third reason and it is the compliance one. A referrer-only reward reads as commission-driven selling, which is the conflict of interest that VARA Marketing Regulation I.C.2.l(i) targets and that IRDAI's 2024 board-policy guidance names directly. **"We both get gold" is a different conversation from "I get paid if you sign."**

And a fourth. Rebating, where an intermediary quietly hands their commission back to the customer to close the sale, is a live problem in the Indian insurance channel this product is modelled on. **The reason rebating exists is that the customer gets nothing. Give the referee half and most of the pressure to rebate disappears.**

### 4.3 The timing is deliberate

The reward lands **at the referee's month six**. That is the moment their score starts, their tier opens at Silver, and their first benefits switch on. It is also, on the Indian life persistency curve, **the point at which the drop-off is steepest**: roughly 79% survive to month 13 and the fall is sharpest in year two.

So the referee's half is not only an acquisition payment. **It is a retention payment delivered at the thinnest month of the curve, and it costs nothing extra because it was already being spent.**

### 4.4 No counting cap, and this is the better answer

An earlier version counted each qualifying month only up to the USD 75 target, so a USD 500 referee generated the same reward as a USD 75 one. **That was wrong and the reason is worth stating, because it inverts the argument for the cap** (Abdur's call, 2026-08-13).

**The cap broke the one property the ratio exists to deliver.** With no cap, the reward is a **constant share of the referred customer's lifetime value at every ticket size**, because both the reward and the value scale with the contribution:

| Referee ticket | Reward pool | Contribution-margin LTV | **Reward as % of LTV** |
|---|---|---|---|
| USD 20/month | USD 1.80 | ~USD 9.30 | **19.4%** |
| USD 75/month | USD 6.75 | ~USD 34.80 | **19.4%** |
| USD 500/month | USD 45.00 | ~USD 232 | **19.4%** |

Under the cap that last row paid **19.4% of the value of a USD 75 customer for a USD 500 customer, which is about 3% of what they are worth.** The cap systematically underpaid for the most valuable introductions the programme could produce. **Paying a constant fraction of value is what a commission is.** The cap was a conduct control wearing a pricing rule's clothes, and it was a bad pricing rule.

**On "behaviour, never amount" (decision 20).** That rule governs a customer's return on their **own** capital: no benefit's *rate* may scale with the customer's own money, because that is a return proportional to investment. **An acquisition payment to a third party for a service performed is not a return on anyone's capital**, and agent commission as a share of the entry fee scales with amount by construction. The rule is not engaged. Worth saying explicitly, because at first glance it looks as though it is.

> 🔴 **What the cap was accidentally defending, and it needs a different defence.** The SIP amount is **variable month to month by design**. So a referee can contribute heavily for exactly the six qualifying months and then collapse to the USD 20 floor.
>
> **Worked:** USD 2,000/month for six months is USD 12,000 of contributions, USD 600 of entry fee, and a **USD 180 reward pool, USD 90 a side**. Aurumix retains `12,000 × 0.85% = USD 102` of net margin on that run, so it is **USD 78 down on day one**. The customer then drops to USD 20/month, earning about **USD 0.17 a month**, so the gap takes 458 months to close. It never closes.
>
> This is the household-capture case of §5.2 with the brake removed. It is not fraud, nobody lies, and the money is real gold the customer wanted. **It is simply a way to buy a large gold position at an effective 3.5% entry fee instead of 5%, by splitting it over six months and having a friend enter a code.**

**The defence is a reserved right, not a cap**, which is the same instrument the design already uses for round-tripping (rulebook §9.3: a reserved right, exercised on review, with a stated appeal path):

> **Where a referee's average contribution in the six months after the gate falls below one third of their average during the qualifying run, the reward is placed under review before it is credited.** Nothing is deducted, the gold and the tier are untouched, and there is an appeal path.

This bites the collapse pattern and nothing else. A genuine large saver who keeps saving is paid in full, immediately, which is the whole point of removing the cap. ⚠ **The one-third threshold and the six-month window cannot be calibrated without data.** Set conservatively, review with the round-trip thresholds, and note this pushes the credit date out for the flagged minority only.

---

## 5. The economics, and a claim this document withdrew

> ⚠ **Read this section before any other. An earlier draft of it was wrong, the error was load-bearing, and the correction changes what the programme is.**

### 5.0 The withdrawn claim

The first draft asserted an invariant: *the reward is always smaller than the gross margin the qualifying run generated, so the programme funds itself inside the six months.* It tested the reward against a "gross margin" of 2.15%.

**That 2.15% is contribution less gold cost only. It has not yet paid for price-gap risk, the float cost of capital, or the payment rail**, which together are a further 1.15pp. Against the real cost stack the comparison inverts:

| | Entry fee | Full cost base | **Net margin** | **Reward** (30% of fee) | Headroom on the run |
|---|---|---|---|---|---|
| Year 1 | 5.00% | 4.15% | **0.85%** | **1.50%** | **−0.65pp** |
| Year 3 | 4.00% | 2.76% | **1.24%** | **1.20%** | +0.04pp |
| Year 10 | 3.00% | 1.71% | **1.29%** | **0.90%** | +0.39pp |

**At Year 1 the reward is nearly double the net margin on the run that generated it.** The invariant was false, and every conclusion resting on it fell with it.

⚠ **Note the Year 3 row: at 30% the reward and the margin are the same number to within 0.04pp.** That is not a designed property, it is a coincidence of two placeholders, and it means **30% is roughly the highest rate at which the qualifying run washes its own face from Year 3 onward.** Useful when the rate is locked against the revenue model.

**The claim is withdrawn rather than repaired, because it should never have been made.** No acquisition programme in any industry recovers its cost inside the acquired customer's first six months. Customer acquisition is an investment recovered over a lifetime, and dressing it up as self-funding was an attempt to make a cost line look like a free lunch. What follows is the honest version, and the programme survives it.

### 5.1 What a referred customer is actually worth

Modelling the Indian life persistency curve (79% contributing at month 13, 38% at month 61) as a constant hazard fitted to both points gives about **37 paying months over five years.**

Applying the Schmitt, Skiera and Van den Bulte (2011) findings for referred customers specifically (about **18% slower churn** and **at least 16% more value**, from roughly 10,000 tracked bank accounts over 33 months, *Journal of Marketing* 75(1)) gives about **40 paying months at a 16% higher margin.**

| Referee ticket | Net margin per month | Expected paying months | **Contribution-margin LTV** | Reward paid | **Reward as % of LTV** |
|---|---|---|---|---|---|
| USD 20/month | USD 0.20 | ~40 | **~USD 9.30** | USD 1.80 | **19.4%** |
| USD 75/month | USD 0.75 | ~40 | **~USD 34.80** | USD 6.75 | **19.4%** |
| USD 500/month | USD 5.00 | ~40 | **~USD 232** | USD 45.00 | **19.4%** |

**The ratio is identical at every ticket size**, because both the reward and the lifetime value scale with the contribution. **This holds all the way up only because §4.4 removed the counting cap**; with the cap the third row paid 3% of value instead of 19.4%.

> **The total acquisition payment is a constant 19.4% of the referred customer's contribution-margin lifetime value, whatever they contribute.**

Roughly a fifth of lifetime value spent on acquisition is an ordinary, healthy ratio, and it excludes every downstream stream: card interchange, credit fees, and the will and family plan are all additional and none is counted here.

**Payback, and an earlier version of this line was too pessimistic.** It said payback took ten months *after the gate*, which silently discarded the margin already earned during the qualifying run. That margin is real money, already collected, and it counts.

Cumulative net margin at month `N` is `1.00% × C × N`. The reward is `9% × C` (1.5% of six contributions), paid once at the gate. Setting them equal:

> **The referred customer is cumulatively cash-positive at month 9, which is about three months after the reward lands.** Not month 16.

At the target ticket: net margin USD 0.75 a month, so month 6 sits at USD 4.50 collected against USD 6.75 paid, a gap of USD 2.25, and that gap closes by month 9. **About 79% of savers are still contributing at month 13**, so the large majority of referred customers repay their own acquisition comfortably, before any of the Schmitt uplift is counted.

⚠ **On the 0.85% net-margin figure instead of 1.00%, payback is month 11 rather than month 9.** The two figures come from different derivations in `_draft_allocation-and-float.md` and have never been reconciled. **Quote the range, not a point**, until the rail cost settles which is right.

> 🔴 **The condition that breaks all of this, and it is not hypothetical.** Every figure above uses the ~1.00% net contribution margin from `_draft_allocation-and-float.md`. **`_parked_collection-economics-and-minimum-ticket.md` records flatly that this number is wrong: it is −0.67% on a USD 75 contribution at AED 5 per debit.** Not at the USD 20 floor. At the target ticket, which is the case worked through above.
>
> If net margin is negative, payback is never, and no referral reward on any ticket can be justified at all. UAEDDS is dropped and the AANI Request to Pay per-request cost is unpublished, so the true figure is unknown. **The rail cost does not merely size this programme. It decides whether it should exist.** It is a PSP conversation, not desk research, and it sits alongside the dealer and the vault quote.

### 5.2 Self-referral is unprofitable, but only against an attacker who did not want the gold

To farm one reward with a second identity you must put six months of your own money through the product and pay the entry fee on all of it. As the sole beneficiary of a self-referral you collect **both** halves, so you receive one third of the fee you paid.

| Referee ticket | Fee paid over the run | Whole pool recovered | **Net to a self-referrer** |
|---|---|---|---|
| USD 20/month (the floor) | USD 6.00 | USD 1.80 | **−USD 4.20** |
| USD 75/month (the target) | USD 22.50 | USD 6.75 | **−USD 15.75** |
| USD 500/month | USD 150.00 | USD 45.00 | **−USD 105.00** |

**You pay 5% to receive 1.5%, and you wait six months to do it.** The loss now scales with the ticket rather than flattening, because there is no counting cap, so **the bigger the farm the bigger the loss.**

> ⚠ **The exact limit of that proof, stated because the first draft overstated it.** It holds against an attacker with **no independent demand for gold**. It does not hold against a household that was going to buy anyway.
>
> A husband already saving refers his wife, who intended to start regardless. Both halves land inside one budget, so the household recovers the **whole** pool: on a USD 75 run, USD 6.75 back against USD 22.50 of fee, an **effective entry fee of 3.50% instead of 5.00%** for that account's first six months. **The discount is 30% of the fee at any ticket size**, which is the same proportion whether the household puts in USD 120 or USD 120,000. §4.4's reserved right is what bounds the absolute number.
>
> **This is not leakage and it is not an exploit. It is the programme working.** She was not a customer and now she is, separately KYC'd, separately funded, with her own gate and her own lifetime value. Intra-household introductions will be a large share of volume in an NRI and GCC savings product and they are the volume we want. Edge case 13 rules it valid deliberately.
>
> What must **not** happen is the framing that invites a comparison to the discount ladder, where Sovereign's 30% is earned over five flawless years. The referral returns one sixth of six months of fee, once. It is a smaller thing and it must be described as one, which is why §4 no longer says *"a month's fee back."*

### 5.3 Worked example: Rajesh introduces Meera

Rajesh has been contributing USD 75 a month since January and passed his own gate in June. In August he sends Meera his code. She opens an account, completes KYC, and contributes from September. She varies the amount, which is allowed.

| Month | Meera contributes | Her run |
|---|---|---|
| Sep | USD 75 | 1 of 6 |
| Oct | USD 75 | 2 of 6 |
| Nov | USD 50 | 3 of 6 |
| Dec | USD 75 | 4 of 6 |
| Jan | USD 75 | 5 of 6 |
| **Feb** | **USD 75** | **6 of 6, gate passes** |

> ⚠ **Rajesh sees none of this.** He sees "referral in progress" and, later, "referral completed". He is never shown Meera's payments, her amounts, her misses or a countdown. See §10.3.

Thirty days after Meera's gate resolves and no contribution in her run has been reversed:

- Contributions over the run: `75 + 75 + 50 + 75 + 75 + 75 = USD 425`
- Fee she paid: `USD 425 × 5% = USD 21.25`
- Reward pool: `USD 21.25 × 30% = USD 6.38`
- Each side: `USD 3.19`, which at USD 109.31/g is **0.0292 g each, credited as gold**

Meera's score started at Silver 25 on the day her gate resolved and her entry-fee discount switched on then. The gold lands a month later. Neither party gets a score point, a badge, a tier, or a status.

**What Aurumix has:** USD 425 collected, USD 21.25 of disclosed fee, and USD 6.38 paid out. On the full Year 1 cost base that run generated `425 × 0.85% = USD 3.61` of net margin, so **the acquisition is USD 2.77 underwater when the gold is credited and closes about four months later**, on the analysis in §5.1 and subject to the rail-cost warning in it.

### 5.4 What this means for the size of the reward

Two things are now true at once and they pull against each other.

**At the persona's ticket the reward is small.** USD 3.19 a side on a target-ticket referee, USD 0.90 a side at the USD 20 floor, seven months after the introduction. Against Mashreq NEO's AED 100 on a single AED 3,000 deposit, that is roughly a tenth of the money for six times the work. Anyone assessing it as payment for effort will find it derisory, and they will be right.

**But removing the counting cap changed the shape of that problem, and this is the part worth noticing.** The reward is now unbounded above:

| Referee ticket | Referrer receives | In grams |
|---|---|---|
| USD 20/month | USD 0.90 | 0.008 g |
| USD 75/month | USD 3.19 | 0.029 g |
| USD 500/month | USD 22.50 | 0.206 g |
| USD 2,000/month | USD 90.00 | 0.823 g |

So the honest statement is no longer *"this is too small to matter."* It is: **the reward is negligible at the floor, modest at the target, and genuinely material for a serious saver.** A member who introduces three USD 500/month savers in a year earns USD 67.50 in gold. That is not an income, and it is no longer nothing.

**And it still cannot be raised much as a rate.** It is already 19.4% of contribution-margin lifetime value, and §5.0 shows 30% is roughly where the qualifying run stops washing its own face from Year 3. The lever that made the reward meaningful was **removing the cap, not raising the rate**, which is the more interesting result: the money was always there, the cap was refusing to pay it to the customers who had earned it.

**The positioning that follows: this is a thank-you that scales with what you actually brought.** It is worth the tap that shares the code. It is not payment for the hour that sells the product, and it is not meant to be.

> 🔴 **The open decision this creates, and it is Abdur's, not ours.** Three coherent positions:
>
> **(a) Ship it as designed.** A small two-sided thank-you at a defensible 21.7% of LTV, with the agent network doing the heavy distribution.
>
> **(b) Size it as real acquisition spend.** Roughly USD 12 to 15 a side, funded from capital as a deliberate Year 1 to 3 investment rather than from the margin on the run. This is the only version that competes with a bank's referral offer. It requires the entry fee to rise or capital to be allocated, and it makes §8.4's collision the central client conversation.
>
> **(c) Attribution only at launch, priced later.** Capture who introduced whom from day one and pay nothing until there is a year of data. It costs almost nothing, keeps the option, and has one large advantage: **with no incentive there is no incentive to approve, so the programme leaves VARA's I.C.2.l critical path and stops being a licensing dependency** (§12.1). It also removes the reward rail from the September build.
>
> **The case for (c) is stronger than it first looks**, because the first reward cannot be paid before roughly **month 13 in any version** (six months for a referrer to qualify, six more for the referee), so Year 1 pays out nothing whatever we choose. The cost of (c) is that an unannounced programme generates no referrals, and the client has ranked referrals second.
>
> **Our recommendation is (a) with the reward announced at launch and attribution live from day one**, which keeps the flywheel and gets the VARA confirmation done inside the licence application that has to be made anyway. Reconsider against (b) once the rail cost lands.

---

## 6. The cap, and the door it opens

> **There is no cap. A member may refer as many people as they can, and every successful referral is paid.**

Set that way deliberately (Abdur, 2026-08-13). An earlier version capped payment at five per rolling year and forced anyone above it toward an agent contract. **The cap is removed and the graduation door with it.**

### 6.1 Why uncapped is defensible, and the best support is VARA's own document

The instinct behind a cap was that an uncapped reward becomes an income, and an income earned by introducing people to a financial product without a contract is close to the fact pattern in §7.1 that a regulator has acted on. That instinct is not wrong. **But it was answering a risk that single level already answers, and it was paying a real price to do it.**

**The strongest evidence is VARA's own worked example.** The Guidance case study (Part II, Section F) describes a licensed VASP that *"allows existing users to share referral codes with any person, **with no maximum number of referrals**"*, and pays the referrer out of what those users generate. VARA does not call it unlawful, a pyramid, or an unlicensed activity. **Its only stated consequence is prior approval and compliance with conditions.** An uncapped, code-based, revenue-linked referral programme is expressly contemplated by the regulator we are applying to.

**What the cap was costing.** It went blind at exactly the wrong moment. Consider who actually distributes a savings product in this community: a mosque or temple committee member, a WhatsApp group admin, an employer with sixty Indian staff in Dubai. Under a cap, referrals six through two hundred paid nothing, so the design switched off the only people who could move volume cheaply and pushed all of it into the expensive contracted channel.

**What still carries the anti-MLM defence, and it is now carrying it alone: single level** (§7). Every reclassification case retrieved (Forsage, BitConnect, OneCoin, Karatbars) turned on **downline compensation**, not on referral volume. Nobody has been reclassified for referring too many people at one level. **The count was never the risky dimension. The depth was.**

### 6.2 What replaces the cap: two reserved rights, no automatic cutoff

Neither is a limit and neither fires on a counter. Both are the same instrument as the round-trip flag (rulebook §9.3: a reserved right, exercised on review, with a stated appeal path).

1. **The contribution-collapse review** (§4.4). Where a referee's contribution falls away immediately after the gate, the reward is reviewed before it is credited. This bounds the split-a-large-purchase pattern that removing the counting cap opened.
2. **The volume review.** Aurumix reserves the right, where one identity is introducing at a volume that is plainly a distribution business rather than a personal network, to require that the relationship be put on a proper footing before further rewards are paid. **No threshold is published**, because a published threshold is a target and because the honest trigger is a pattern rather than a number.

**Neither right is exercised by an algorithm and neither is surfaced to the customer as a counter.** That was the other lesson of the removed version: an app that automatically offers a contract at a fixed count creates an unbounded operational liability triggered by customer behaviour rather than by our capacity to supervise.

**And the honest statement about motivation, because an earlier draft contained both halves of a contradiction.** It argued in §4.2 that the reward shape drives behaviour, and then argued that people above the cap would keep referring for nothing. Both cannot be true. The resolution: **the reward lowers the friction on an introduction someone was already inclined to make. It does not manufacture one.** With the cap gone, it now also scales with what the introduction was worth (§5.4), which is the first version of this mechanism where the reward and the value point in the same direction all the way up.

### 6.3 Rewards accrue to the verified identity, not the account

Exactly as the score does (SIP rulebook §9.1, item 7: *the score attaches to the verified identity, not the account*). With no cap this no longer rations anything, but it still matters: it is what makes the volume review in §6.2 see one person rather than four accounts, and it is what keeps a single individual from appearing as several referrers in the book.

A joint account's referrals attribute to **both** holders; a corporate or trust account may not refer (§10, case 26).

**The household check is deliberately soft.** We match on identity, not on address, because the NRI persona routinely shares an address with several unrelated working adults. Matching on address would reject the referral pattern the product most wants.

### 6.4 What is still true with the cap gone

Two things the removed cap was doing that other rules now do, so nothing was lost with it:

- **Bounding the loss on a gamed referral.** Previously the cap bounded it at five a year. It is now bounded by §5.2's arithmetic instead, which holds at any volume: a farmer pays 5% to recover 1.5%, so more attempts means more loss, not more profit. **The cap was never the thing making farming unprofitable.**
- **Identifying distribution businesses.** Previously the counter did it. The volume review in §6.2 does it now, on a pattern rather than a number, and without publishing a target.

⚠ **Recorded, not solved:** with no cap and no automatic graduation, a person can build a substantial unregistered referral income over time and there is no point at which the design forces the conversation. **The volume review is a right, and a right that is never exercised is a rule that does not exist.** It needs an owner and a review cadence, which is an operations question rather than a mechanism question, and it belongs in the compliance monitoring plan.

### 6.4 What is deliberately not in the programme

| Rejected | Why |
|---|---|
| **Leaderboards, contests, top-referrer recognition** | A tournament for financial rewards is a compliance surface, and the scoring draft §1.7 already rejected relative measures for this reason. The client's own 80/20 dividend was this pathology |
| **Time-limited multipliers, "double gold this weekend"** | **Prohibited independently by VARA.** Marketing Regulation I.C.2.h forbids marketing that states or implies urgency or creates a fear of missing out, and I.C.2.l(ii) requires incentives to run for an adequate period |
| **A referral badge, status or title** | A status for recruiting is the MLM shape decision 46 removed from the score. Reintroducing it outside the score changes nothing about how it reads |
| **Escalating rates: more per referral as you refer more** | The defining feature of a recruitment-driven plan. Every reward is the same size as every other |
| **Any reward for a referral that does not reach the gate** | §3. There is no partial credit and no consolation payment |

Note the convergence in row two: our own principle and VARA's rule arrive at the same prohibition from different directions. Where that happens, say so, because it is the cheapest kind of compliance argument.

---

## 7. Single level, and this one is not negotiable

> **If A introduces B and B introduces C, A receives nothing from C. Ever. In any form.**

In the terms, in the app, in the whitepaper, and in the VARA submission.

### 7.1 The precedent that decides it

**On 15 August 2024 the NSE prohibited brokers from paying referral commissions to anyone not registered as an Authorised Person. Zerodha stopped paying its 10% brokerage share on 25 August 2024 and kept only a 300-point non-cash reward. Most leading Indian brokerages discontinued their programmes.** (business-standard.com, Medium; the circular was reportedly held in abeyance as of 11 March 2025.)

Read what the regulator objected to. Not referral. Not incentives. **A share of ongoing revenue paid to an unregistered person.** The one-off bounty survived. The annuity did not.

This is the closest available precedent because it is the same regulator family, the same retail persona, and the same channel that the agent network is modelled on. It is why the member reward is a **single payment** and why recurring income lives behind a contract.

**It also condemns two designs we might otherwise have copied:** Kinesis's 7.5% lifetime share of a referee's fees, and Jar's 1% trailing commission on every subsequent investment. Both pay ongoing revenue to unregistered persons.

### 7.2 The reclassification evidence

Across every case retrieved, the trigger is the same and it is not referral itself.

| Case | What the authority acted on |
|---|---|
| **Forsage** (SEC and CFTC, 2022) | Matrix positions with smart-contract-automated **downline payouts**; earnings driven primarily by recruitment |
| **BitConnect** (SEC, 2021) | Commissions tied to **downline investment growth**, returns funded by recruitment |
| **OneCoin** (DOJ) | Recruitment-driven **multi-tier commissioning** on packages, no real tradable coin |
| **Karatbars** (BaFin, 2020) | Misrepresentation and unlicensed offering, with **downline-style multi-level commissions attached to token sales** |

**Karatbars is the one to notice.** A gold-backed token sold through a multi-level structure is the nearest reputational adjacency Aurumix has, and it is the comparison a sceptical journalist or regulator will reach for first. A single-level cap written into the terms is very cheap insurance against a comparison that is otherwise free to make.

**And UAE law here is unverified, which is itself the argument.** We could not retrieve primary UAE statutory text expressly naming pyramid schemes or network marketing: uaelegislation.gov.ae returns HTTP 403 to automated access, and the Ministry of Economy PDFs refused connection. Secondary sources indicate the conduct is charged as **fraud under Article 451 of Federal Decree-Law 31/2021** rather than under a standalone pyramid-selling offence. **Multi-level compensation could not be verified as lawful in the UAE under any licence.** Designing around an unverified permission is not a trade worth making for a mechanic we do not need.

### 7.3 So what about the three-tier agent network

The client's three tiers survive. **They are functions, not depths, and that distinction is load-bearing.**

Decision 13's anti-MLM answer, taken from Aurus, is: *pay each tier for a function performed, not for recruitment depth, with graduation instead of overrides.* Applied:

- A Principal Agent does **not** earn on a Sub-Agent's sales because the Sub-Agent sits beneath them.
- A Principal Agent earns a **supervision fee for supervision actually performed**: training delivered, compliance sign-off given, first-line complaints handled, mis-selling remediated.
- The fee is **payable only while the supervised book is in force and the supervision is documented.**

That converts an override into a service fee, which is the same reframe that makes the member reward a commission rather than a distribution. **It is testable in a way an override never is: no documented supervision, no fee.**

> ⚠ **A finding for the client, and their superseded document had the better answer.** Their V3 §11.1 says Level 1 takes the *"Largest share"*, Level 2 *"Mid"*, Level 3 *"Smallest"*. Their V2 §13.3, the only numeric table ever written, splits a full three-level chain **4% / 5% / 6%**, so the front-line Associate earns the **most** and the Principal the least. The two documents specify **inverted gradients**, and V2 also contradicts its own description of Level 1 as the *"maximum accountability tier"*.
>
> **We recommend the V2 gradient: the person closest to the customer earns most.** It is the anti-MLM shape, it prices the work where the work is, and it removes the incentive to stop selling and start recruiting. The client will need to hear that their current document has it the wrong way round.

---

## 8. Funding, and the ceiling that bounds it

### 8.1 Where the money comes from, and why the classification argument goes second

**Revenue stream 1, the entry fee.**

The first draft led with a classification argument: `_draft_ics-benefits.md` §7 fixes that **no benefit may lean on stream 1 except benefit 1's uplift**, and the referral reward escapes it because it is not a benefit. **That argument is correct on the text and it should not be led with**, because it answers the wrong question.

The rule exists because **stream 1 is thin.** At Year 1 the entry fee is 5.00% against a 4.15% cost base, so the whole line is **0.85pp wide**, and it is already claimed by the entry-fee discount ladder and by agent commission. **That constraint does not care what the draw is called.** A reader who watches a cost re-labelled its way out of a rule is entitled to be suspicious, and a sceptical client will read the reclassification as a way of avoiding reopening decision 44's closed benefit set.

**So, in order:**

1. **The arithmetic first.** Stream 1 cannot fund everything currently pointed at it, and §8.4 is that conversation. It is a client decision, not a drafting choice.
2. **The classification second, and it does hold.** §7's rule is scoped to benefit ceilings in a checklist governing the five-benefit table. A cost line is not a benefit ceiling, the benefit set stays closed at five, and acquisition costs have always come out of the entry fee. The client has already agreed the principle for agents: *"a direct share of the initial fee for agents instead of the whole revenue line."*

The reclassification still has to be written down, or somebody will read this as a sixth benefit and start applying the benefit rules to it. It just does not solve the funding problem, and this draft no longer implies that it does.

### 8.2 Does it break the no-pool rule

`_draft_ics-benefits.md` §0.1 rejected a pooled rebate on a three-part test. Applied here, in full, because the referral reward superficially looks like the thing that was rejected:

| The test | Referral reward |
|---|---|
| **Must not redistribute across customers** | ⚠ **Passes only on an amended reading of the rule, and the amendment must be recorded rather than assumed.** §0.1's operative words are *"recycles investor fees into investor payouts"* and *"breaks the capped-at-what-you-generated rule"*. On the face of it the referrer's half does both: it moves 0.83% of the referee's contribution to a different customer, and it is sized by what the **referee** generated, not the referrer. The distinction that saves it is real but it is **not in §0.1 as written**: *a distribution is paid for holding, a commission is paid for doing.* The rejected pool paid passive holders by tier and by gram, which is a return on capital. This pays a named person once for a completed act. **We are proposing an amendment to §0.1, not merely applying it**, and §16 carries it as a change |
| **Must not scale with capital** | **Passes.** The reward does not move with the referrer's holdings at all, and the referee's side is capped at the USD 75 target |
| **Must not duplicate a lever funded from the same source** | **Passes, but only just.** Benefit 1's discount ladder also draws on stream 1. §8.3 is the collision |

**The distinction that carries it: a distribution is paid for holding, a commission is paid for doing.** The dividend problem was *you give us money, we run a business, we share our profits with you, and your share is bigger if you gave us more.* None of those four clauses describes this.

### 8.3 The ceiling, copied from the only live regime that does this properly

> **Total acquisition spend, meaning member referral rewards plus all agent commission at every level, is capped as a percentage of entry-fee revenue in any financial year. The policy is board-approved, reviewed at least annually by the audit committee, and any excess is borne by shareholders rather than recovered from customers.**

That is not invented. It is the structure of the **IRDAI (Expenses of Management, including Commission, of Insurers) Regulations, 2024**, gazetted F. No. IRDAI/Reg/2/196/2024 on 22 January 2024, effective 1 April 2024, supplemented by Master Circular IRDAI/F&I/CIR/79/5/2024 of 15 May 2024. Its features, all of which transfer:

- **An overall expense ceiling replaces product-wise commission caps.** General insurers 30% of gross written premium, health 35%, life a sum of segment-wise allowances.
- **A first-year versus renewal asymmetry as the brake on front-loading.** For regular-premium life business with a term of ten years or more: **80% of first-year premium, 17.5% of renewal.**
- **Every insurer must have a board-approved commission policy**, and the Master Circular's operative test is qualitative: the structure *"shall be reasonable and not result in excessive compensation for intermediaries at the expenses of customers or the insurer"* and must be *"commensurate with the efforts required to acquire and sustain that type of business."*
- **Excess expense is charged to the Profit and Loss Account**, borne by shareholders, with enforcement running as far as removal of managerial personnel.

**Copy the shape: one ceiling, board-owned, annually reviewed, front-loading braked, excess on shareholders.** Set the number in Phase 4 when the revenue model exists. It is exactly the artefact the client said had to come first.

### 8.4 🔴 The arithmetic the client has not been shown

Their V3 §11.1 states: *"Agent commission is paid from Aurumix's fee revenue. It is not an additional charge to investors."*

**Both halves of that cannot be true at a 5% entry fee.**

| Year 1, per USD 75 contribution | |
|---|---|
| Entry fee, disclosed | 5.00%, USD 3.75 |
| Cost before margin (fabrication 3.00 + price gap 0.36 + float 0.49 + rail 0.30) | 4.15%, USD 3.11 |
| **Gross margin available for everything** | **0.85pp, USD 0.64** |
| V2's agent share, 15% of the fee, if transplanted to the entry fee | 0.75pp, USD 0.56 |
| **Left for Aurumix** | **0.10pp, USD 0.08** |

**The single agent commission number the client has ever written down consumes 88% of Year 1 gross margin.** And the entry-fee discount ladder draws on the same line, and now so does the referral reward.

There are exactly three honest resolutions and the client picks one:

1. **The entry fee rises**, in which case investors do pay for distribution and the sentence in §11.1 has to change.
2. **Acquisition is funded from capital in the early years**, which is normal, which is what an EOM regime assumes, and which means it is a budgeted investment rather than a margin line.
3. **There is no paid distribution channel**, which contradicts calling the agent network the *"primary distribution channel"*.

⚠ Note also that the V2 15% is **orphaned**, not merely superseded: its base was the Algorithmic Growth Fee, and that fee no longer exists in the current model. It cannot be carried forward as a number even if the client wants to.

**Related, and it softens the ask:** decision 46 already found that the entry-fee discount ladder is time-phased by construction, so nobody is above Silver in Year 1 and the maximum discount outstanding at launch is 0.4pp. The ladder's Year 1 cost is close to zero. **The Year 1 collision on stream 1 is therefore acquisition against margin, not acquisition against the ladder.**

---

## 9. Attribution: one acquisition, one payment

> **Every account is attributed to exactly one origination channel at creation, and the attribution never changes.**

| Channel | Acquisition payment |
|---|---|
| Direct | None |
| Member referral | The §4 reward, once |
| Agent | Agent commission per the Agent Agreement |
| B2B partner (stream 6) | The partner's own economics. **Neither ICS nor referral rewards apply** |

**The rules that follow, and each closes a specific double-dip:**

1. **An agent may not earn a member referral reward on any account in their own agent book.** They are paid the other way.
2. **Contracted agents are excluded from the member programme entirely**, on their own account and on any account they control. Not capped. Excluded.
3. **A member-referred account is not later assignable to an agent's book** for commission purposes. Service can be transferred; the acquisition payment cannot be earned twice.
4. **Partner-channel customers can neither refer nor be referred.** Consistent with the scoring draft §1.9, which gives them no gate, no score and no tier, for reasons that apply identically here: the behaviour is not observable to us, and the partner has already been paid at the till.
5. **Family sub-accounts within one portfolio cannot refer one another**, and the portfolio head earns nothing on their own sub-accounts. Family is already paid by the will and family discount ladder, which was reason two for removing referrals from the score.

**The test that resolves the family edge case cleanly is funding independence.** A genuinely separate family member who opens their own account, passes their own gate, and funds it from **their own bank account in their own name** is a real customer and a valid referral, whatever the surname. A sub-account funded by the head is not. The own-name funding requirement is already a hard product rule, so no new machinery is needed.

---

## 10. Edge cases

Every one of these was found by walking the mechanism rather than by imagining it. Each has a ruling.

| # | Case | Ruling | Reasoning |
|---|---|---|---|
| 1 | **The referrer lapses before the referee's gate** | **Pays.** The referrer must have passed their own gate and hold an open account, but need not be currently contributing | The service was performed. Withholding it for a quiet month makes the reward a status benefit, which §1 removed |
| 2 | **The referrer closes and exits entirely before the gate** | **Does not pay.** No account, nowhere to credit metal, no relationship | |
| 3 | **The referrer has not passed their own gate at payout** | **Does not pay** until they do. The reward is held, not forfeited, and lands when they pass | See §10.1. In practice this almost never bites |
| 4 | **The referee's run is frozen by a regulatory pause** | **The run freezes and resumes where it stopped.** A saver at 4 of 6 resumes at 4 of 6 | Directly inherited from the 2026-08-13 rule. Months in which Aurumix refuses the customer's money do not count against anyone, including the referrer |
| 5 | **The referee is permanently blocked and exits** | **No reward.** Nothing was earned | |
| 6 | **The referee misses a month at 4 of 6** | **The run breaks and restarts.** The referral is not lost; the clock restarts with it | There is no revival anywhere in this design and there is none here |
| 7 | **The referee never strings six together** | **Never pays.** However many scattered payments they make | The same cost the score already accepts, stated in decision 46: persona H accrues nothing. Consistent, and it must be stated rather than discovered |
| 8 | **The referee pays six, takes the reward, liquidates everything** | **Reward stands. No clawback.** | §10.2. This is a deliberate omission with arithmetic behind it |
| 9 | **Does the reward touch the score** | 🔴 **No, and it takes an explicit rule to make that true.** Reward grams are excluded from **both** sides of the Retention ratio: they are not "grams held now" and not "grams acquired since". See §10.4 | Without the exclusion the answer is yes, and decision 46 reopens |
| 10 | **Does the reward create a counted period** | **No.** Not Months, not Recent, not the gate | A credit arriving in a balance looks like activity and the engine must not treat it as such |
| 11 | **The referee is referred by two people** | **First code entered at account creation wins.** No split, no dispute path | §3.3. Attribution is immutable |
| 12 | **The referee enters no code but names a friend later** | **No reward, not appealable** | §3.3, with the trade-off stated |
| 13 | **Both parties are the same household, different real people, independently funded** | **Valid** | §9, funding independence |
| 14 | ~~**The referrer hits the cap mid-run**~~ | 🔄 **Moot. There is no cap** (§6) | The general principle survives and applies to any future rule change: a referral already attributed completes on the terms in force when it was attributed (case 27) |
| 15 | **A referred customer later becomes an agent** | **Fine.** Their own historic referral reward stands; they earn no further member rewards from the date of contracting | §9 rule 2 |
| 16 | **The gold price moves between the gate and the credit** | The pool is fixed in **USD** at the gate. If it is credited in grams, it converts at **the next published fix after the thirty-day window closes** | Decision 34's settled principle applies: the price is always the next fix nobody has seen yet, because anywhere either side can pick between two known prices, that side holds a free option. ⚠ **The AM-or-PM resolution is NOT settled.** handoff §7 records the pricing rule as inconsistent across three drafts with *"next published fix, AM or PM, whichever comes first"* as **our recommendation, not a decision.** An earlier draft of this file adopted it as though it were a rule. It is flagged, not assumed |
| 17 | **The referee dies before the gate** | **No reward.** The Digital Will governs the gold; the referral simply does not complete | Recorded because it will happen and support needs an answer |
| 18 | **The referrer dies before the gate** | **The reward lapses.** It is not an asset of the estate | It is a contingent payment for a service, not an accrued entitlement. ⚠ Confirm with counsel |
| 19 | **A referee in a jurisdiction the programme does not cover** | **They may open an account if the perimeter permits it; no referral reward is paid either way** | §12.5. The programme is geo-fenced more tightly than the product |
| 20 | **Reward would land on a compliance-blocked account** | **Held, not forfeited, and released when the block clears** | Joins the existing counsel batch on whether a Gold Rewards gram credit may land on a blocked account. Same question, same answer needed |
| 21 | 🔴 **The referee is a returning customer who already passed the gate years ago** | **The trigger is six consecutive counted contributions from the referred account's activation**, which for a first-time customer is exactly their Confirmed SIP gate and for a returner is a fresh six | **This was a real hole.** Confirmed SIP is permanent and never re-earnable (rulebook §4.1), so a trigger worded as *"passes their Confirmed SIP gate"* can never fire for a returner, and the referral would hang unresolved forever. Win-back of lapsed savers is one of the highest-value referral cases in a product with this persistency curve, and it was silently paying zero |
| 22 | 🔴 **A contribution in the run is refunded, reversed or charged back after the gate** | **The reward is void.** This is what the thirty-day window in §4 exists for | The prefunded balance is refundable on request (rulebook §6.3). Without this rule: prefund six, pass the gate, collect, request the refund. **The only genuinely cash-extractive hole found in review** |
| 23 | **The entry fee changes mid-run**, 5% to 4% at the Year 3 transition | **The pool is one third of the fee actually paid, month by month.** No single rate is applied to the run | Thousands of runs will straddle the transition. The actual-fee rule is the only one that needs no transitional provision |
| 24 | **Rounding and dust.** A USD 20 referee generates about 9 milligrams a side | **Compute and store the reward in currency, convert at credit time, and round to the token's full precision, never to two decimals of a gram** | At 2dp a 9mg reward rounds either to 0.01 g, which is free money and farmable, or to zero, which silently deletes the reward for the exact saver the product exists to serve. **The token's decimal precision is undefined anywhere in our drafts and this is the second place it now bites** |
| 25 | **An Aurumix employee refers** | **Ineligible**, on their own account and any account they control | §9 excluded contracted agents and said nothing about staff, who have the strongest information advantage and the clearest conflict |
| 26 | **Joint and corporate accounts** | A joint account may refer; the referral counts against **both** holders' caps. **A corporate or trust account may not refer** | The cap attaches to a verified identity (§6.3). A joint account has two and a corporate account has beneficial owners, so the natural reading gave a joint account ten and a company an unbounded number |
| 27 | **The programme is withdrawn or amended with runs in flight** | **Every referral already attributed completes on the terms in force when it was attributed.** Changes apply to new attributions only | **VARA I.C.2.l(ii) requires incentives to be available for an adequate period**, so unilateral mid-run termination is likely non-compliant as well as unfair. The terms need an express run-off clause |
| 28 | **FX movement between the run and the credit** | The pool is computed in **USD**, the product's pricing currency, and converted once at credit time | Contributions are USD-priced, savers earn in AED or INR, the fix is USD. Fixing the pool in USD keeps one currency in the mechanism |

### 10.1 Why edge case 3 costs almost nothing

Requiring the referrer to have passed their own gate looks like it would delay the whole programme by six months. It does not, and the reason is timing.

The referee takes **at least six calendar months** to qualify. A referrer who joined today and referred tomorrow has those same six months to pass their own gate. **The two clocks run in parallel**, so the requirement bites only on someone who lapses during it.

What it buys is the best mis-selling control available and it is free: **every referrer has personally held the product, with their own money, for six consecutive months before their recommendation pays anything.** Nobody is paid to recommend a product they have not lived with.

**The residual cost, stated:** in the first six months after launch there are no qualified referrers, so the referral channel is dark until roughly month seven. Year 1 acquisition is agents and direct. That is a real gap and it belongs in the launch plan rather than in a footnote.

### 10.2 Clawback: what was withdrawn, what replaced it, and what stays

The first draft argued that no clawback was needed because the withdrawn invariant guaranteed every run was profitable. **It did not, and the honest position is worse and simpler.**

A referee who contributes six months at USD 75 and exits immediately has paid **USD 22.50 in fee** and generated, on the full cost base, `450 × 0.85% = USD 3.83` of net margin. Aurumix paid **USD 7.50**. **That is a loss of about USD 3.67 per gamed referral**, and capped at five a year it is a maximum exposure of roughly USD 18 per identity per year.

**So the position is: the loss is real, it is bounded, it is not worth a mechanism, and it is disclosed rather than defended.** What earned its place instead is the much narrower rule in §4 and edge case 22: a **thirty-day window and voidance on reversal**, which exists for the refund hole rather than for the cycler. That is one rule doing one job it is actually needed for, rather than a vesting schedule doing a job the arithmetic does not require.

**The agent clawback is different and it stays.** Agent commission is a negotiated share paid upfront on a whole book with no cap of this kind, and register item 12 names it the sharpest cycling exploit precisely because it *"extracts real cash from Aurumix."* See §13.1, which contains a correction we owe ourselves about where that clawback comes from.

### 10.3 What the referrer is allowed to see, which is almost nothing

The first draft's worked example showed the referrer a live *"1 of 6"* counter on the referee's account. **That is a disclosure of a named person's payment behaviour to an unlicensed third party, and it was wrong on two independent grounds.**

**Design.** The *"4 of 6, three months to go"* countdown in the scoring draft §1.6a is the **account holder's own** mitigation for the zero-benefit pre-gate months. Nothing decided it could be read across accounts, and the build note in decision 46's amendment tracks the run for the account, not for observers.

**Privacy.** A referrer would learn, month by month, whether a named person is paying into a financial product and whether they missed. There is no consent mechanism for that anywhere in the design, and §12.1 has just established that this programme goes into a VARA licence application. A payment-behaviour leak to an unlicensed third party is a poor thing to put in one.

> **So: the referrer sees "in progress", then "completed" or "not completed". No amounts, no months, no misses, no countdown, and no notification when a run breaks.**

The referee is told at signup, once, that their referrer will be told only whether the referral completed. That is the entire disclosure and it needs the referee's acknowledgement at account creation.

### 10.4 Reward grams and the Retention denominator, which needed a rule

Retention reads `Sold = 1 − (grams held now ÷ [grams held 12 months ago + grams acquired since])`.

A credited gram is an acquisition, so it enlarges the denominator. Work it through for an account that has sold something: holding 2.0 g of 3.0 g acquired gives Sold = 0.3333 and Retention 0.9524. Credit 0.0324 g and hold it, and Sold falls to 0.3298 and **Retention rises to 0.9575.**

> 🔴 **So a credited gram, held, strictly improves the Retention of any account with Sold above zero. Left alone, referrals would raise the score, and decision 46 would be reopened by the back door.**

**The rule: reward grams are excluded from both sides of the Retention ratio.** They are neither "grams held now" nor "grams acquired since". The customer keeps the metal; the score does not see it.

⚠ **And this is a latent error in the prior record, not only here.** Scoring §1.5's denominator table says Gold Rewards grams *"enlarge the denominator, so a reward never creates or reduces a penalty. Sold clamps at 0 either way."* **That is true only for a customer with Sold already at zero.** For anyone who has sold, a Gold Rewards credit strictly reduces their Sold figure too. Same bug, same fix, and it is in §16.

---

## 11. Anti-gaming register

Layered the same way as the SIP rulebook's §9: make it unprofitable first, detect second.

| # | The play | The prize | The defence | Class |
|---|---|---|---|---|
| 1 | **Self-referral** with a second identity | The whole pool | **Unprofitable by arithmetic, against an attacker with no independent demand for gold.** Pay 5% to receive 1.67%, wait six months, survive KYC (§5.2). ⚠ **Does not hold against a household that was buying anyway**, which recovers the full pool for an effective 3.33% fee. That case is intended, not defended: it is a real new customer (§5.2) | **Structural, with a stated limit** |
| 2 | **Sybil farming** at volume | Many halves | Same arithmetic, multiplied. Each fake identity must survive KYC, fund from a bank account in its own name, and lose money for six months | **Structural** |
| 3 | **Signup farming** | A bounty per registration | **There is no bounty for a registration.** Nothing pays before the gate | **Structural** |
| 4 | **Dust farming**, many tiny contributions | Cheap qualifying runs | The **hard USD 20 floor**: below it money is rejected and returned, never partially credited | **Structural** |
| 5 | **Compressing the run**, prepaying six months at once | A fast payout | **One counted period per calendar month.** No revival, no arrears, no backdating | **Structural** |
| 6 | **Referring cyclers** who pay six months then withdraw | Rewards on customers worth nothing | **Priced, not prevented.** About **USD 3.67 of loss per gamed referral**, bounded by the cap at roughly USD 18 per identity per year. Judged not worth a mechanism, and disclosed rather than defended (§10.2) | **Accepted, bounded** |
| 7 | **Recruiting a downline** | Second-tier earnings | **They do not exist** (§7). There is nothing to build | **Structural** |
| 8 | 🔴 **Inflate the referee's contributions for exactly the six qualifying months, then collapse to the floor** | A large reward on a customer with almost no remaining value. **USD 90 a side on a USD 2,000/month run, against USD 102 of margin, then USD 0.17 a month forever** | 🔄 **The counting cap that blocked this was removed (§4.4).** Replaced by the **contribution-collapse review**: where average contribution in the six months after the gate falls below a third of the run average, the reward is reviewed before crediting. ⚠ **A reserved right, not arithmetic. This is the weakest defence in the register** | **Rule, uncalibrated** |
| 9 | **Agent double-dip**, routing a sale through a personal customer account | Commission and bounty on one acquisition | **One acquisition, one payment** (§9). Agents excluded from the member programme | **Rule** |
| 10 | ~~**Cap evasion** via a spouse's or child's account~~ | ~~More than five paid referrals a year~~ | 🔄 **Moot. There is no cap to evade** (§6). Rewards still accrue to the verified identity rather than the account, so the volume review sees one person rather than four | **Removed** |
| 11 | **Household farming**, one person opening accounts for relatives | Rewards on accounts they fund | **Own-name bank funding** is already a hard product rule (§9) | **Rule** |
| 12 | **Rebating**, the referrer privately hands their half to the referee to close the sale | A larger effective inducement | **Not defended, and largely defused by design.** Rebating exists because the referee gets nothing; paying the referee half removes most of the pressure. Amounts are trivial and policing is not practical | **Accepted** |
| 13 | **Volume abuse patterns**: device sharing, IP velocity, PII collisions | Industrial farming | Standard controls as a second line: device fingerprinting, IP and velocity checks, PII matching against the whole book, manual review above a threshold. **Second line, not first** | **Detection** |
| 14 | 🔴 **Prefund six months, pass the gate, collect, then request the refund** | The whole pool, with the money returned | **Thirty-day window and voidance on any reversal** (§4, edge case 22). **This was the only genuinely cash-extractive hole found in review** and it was missed by the first draft | **Rule** |
| 15 | **Rounding the reward up at scale** on tiny referees | Free grams | Compute in currency, convert at credit, round to full token precision (edge case 24) | **Rule** |
| 16 | **Referring to game the score** rather than for the reward | A Retention improvement from credited grams | **Reward grams excluded from both sides of the Retention ratio** (§10.4). Without that rule this attack works | **Rule** |

**Seven of sixteen are structurally impossible rather than defended against**, and the ratio is lower than the first draft claimed because two of its structural defences turned out to rest on a withdrawn invariant. What holds them up now is that the gate cannot be rushed and the reward is bounded by the fee that funded it.

> ⚠ **Do not reconcile this register with the scoring draft's.** §3.1's *"six of eleven attacks structurally impossible"* refers to the score's register in `_draft_ics-scoring.md` §8. They are different registers counting different things.

**One residual, named rather than solved:** the round-trip flag in SIP rulebook §9.3 (a redemption within 30 days of a contribution, in 4 or more months of any rolling 12) already freezes tier progression pending review. **Extend it: an account under round-trip review earns and generates no referral rewards while the review is open.** Nothing is deducted, nothing already paid is reversed.

---

## 12. Compliance screen

### 12.1 🔴 VARA: this is a marketing incentive, and it needs approval before it launches

**Verified verbatim from the primary rule text**, Marketing Regulations I.C.2.l, at rulebooks.vara.ae (VARA_EN_419_VER1.pdf):

> "**l. Incentives.** Entities offering any monetary or non-monetary incentive in relation to any Virtual Asset or any product and/or service related to any VA Activity must ensure all such monetary or non-monetary incentives —
> i. are not used in such a way that they are likely to divert or mislead investors' focus from the proper consideration of the risks associated with the Virtual Asset…;
> ii. are available for an adequate period of time…; and
> iii. **must receive a compliance confirmation from VARA**, and comply with all conditions or restrictions notified by VARA at the time of approval or at a later date."

Limb (iii) is a hard gate. And **VARA's own Guidance contains a referral case study that is close to this design**: a licensed VASP letting existing users share referral codes with no maximum, paying the referrer a share of the referees' fees. VARA does not call it unlawful, a pyramid, or an unlicensed activity. Its stated outcome is that the programme *"would need to be approved by VARA as part of its licensing application"* and must comply with any conditions imposed.

**Three consequences, and the first is a schedule consequence:**

1. 🔴 **The referral programme is part of the licence application, not a post-launch marketing decision.** It has to be designed before the application goes in. That is why this document exists now rather than in Phase 4, and it should be said to the client in those terms.
2. **Aurumix stays liable for what its referrers say.** Rule I.C.5 puts responsibility on the instructing entity, and the third party *"will be held liable for breach"* too. This requires a controlled asset kit, approved copy, an express prohibition on improvising claims or giving advice, and a takedown route.
3. **Referrers must disclose the remunerated arrangement** when they promote. Non-monetary remuneration is expressly included, so **paying in grams is caught exactly as cash is.** There is no influencer or journalistic exemption available here.

Also binding: **no urgency or fear-of-missing-out framing** (I.C.2.h), incentives must run for an **adequate period** (I.C.2.l(ii)), and **all marketing records are retained for eight years** (I.C.4).

### 12.2 Does a referrer need a licence

**Probably not, on the rule text, and the design is built to keep it that way.**

Schedule 1 of the Virtual Assets and Related Activities Regulations 2023, verified verbatim: **VA Broker-Dealer Services** covers *"arranging orders for the purchase and sale of Virtual Assets"* and *"soliciting or accepting orders"*. **VA Advisory Services** covers *"a personal recommendation… in respect of one or more actions or transactions"*.

**Both are order-centric or advice-centric. The word "introducing" does not appear**, and there is no UK-style generic "arranging deals" perimeter and no introducer exemption to be found.

⚠ **Correction worth recording:** a search model initially reported the broker-dealer definition as covering *"arranging, introducing, soliciting or otherwise making arrangements for another person to deal."* **That wording is not in the rule.** It was caught by reading the primary text. Do not let it back in.

**So the design keeps referrers away from both perimeters, by rule:**

- A referrer shares a code. They do not relay, solicit or accept orders.
- A referrer gives no personal recommendation on how much gold to buy, when to buy, or whether it suits the other person's circumstances.
- The referee transacts directly with Aurumix throughout.
- **The moment someone is doing more than that, they belong in the agent network** (§6.3), where they are contracted, trained and disclosed. The graduation door is a compliance mechanism as much as a commercial one.

### 12.3 UAE pyramid and MLM law: the honest state of knowledge

**We could not verify the primary statute, and this is a reported negative, not a gap we are papering over.** uaelegislation.gov.ae returns HTTP 403 to automated access for the Consumer Protection Law 15/2020 and Cabinet Decision 66/2023; moet.gov.ae PDFs refused connection. Federal Decree-Law 15/2020 retrieved from moj.gov.ae turns out to be a five-page amending decree to the 1987 Penal Code with zero occurrences of "fraud", "pyramid" or "network".

What is reasonably supported, secondary, Medium confidence: the UAE appears to have **no standalone pyramid-selling offence** and prosecutes the conduct as **fraud under Article 451 of Federal Decree-Law 31/2021**. Secondary claims that Cabinet Decision 66/2023 "entirely prohibits" network marketing are **unverified and must not be relied on**.

⚠ A second correction: the commonly cited test that lawful programmes reward sales to end users while pyramids reward recruitment per se comes from the **US FTC**, not from UAE authority. It is a sound design heuristic. It is not UAE law and must never be presented as such.

**This is precisely why §7 is absolute.** Single level is what a design does when the permission for multi-level cannot be verified.

### 12.4 Tax

All secondary, Low to Medium confidence, and this is a checklist for the tax adviser rather than a conclusion.

- **VAT:** a referral or introducer commission is generally a taxable supply of services at **5%**, separate from the underlying supply. **A rebate against the referrer's own fees is structurally less likely to be a supply than a cash commission**, which is a real reason to prefer a rebate-shaped reward if the tax adviser confirms it. A gram credit sits between the two and needs a view.
- **Withholding:** the UAE applies **0% withholding** on UAE-source income of non-residents, so paying an overseas referrer creates no UAE withholding.
- **Corporate tax:** commissions are generally deductible if wholly and exclusively for business. No FTA passage naming referral commissions expressly was found.
- **Consumer protection:** a separate **Dubai DET or consumer-protection promotion permit** may be required for a discount or prize-style promotion, on top of the VARA confirmation. Check it.

### 12.5 Cross-border, and the perimeter is tighter than the product's

The material risk is **outbound**: paying a resident of another state to introduce that state's residents can be unlicensed promotion or solicitation **in that state**, whatever UAE law says.

> **Launch perimeter: UAE residents only, both sides.** Then Bahrain and Oman with local authorisation, in step with the product perimeter in decision 31.

**Excluded at launch, and each for a reason already established:** India, on the two independent bars in decision 27, and because paid solicitation of Indian residents adds a SEBI and FEMA surface on top; Saudi Arabia, Kuwait and Qatar, because their central banks restrict institutions from processing virtual-asset transactions, so those customers cannot be served in the first place.

**Precedent worth knowing:** the Binance referral terms expressly **disqualify Binance FZE (Dubai) users from participating** in its global referral programme. A major VASP has looked at exactly this question in exactly this jurisdiction and chosen to carve the UAE out. Ours goes the other way, deliberately, with VARA confirmation as the condition.

### 12.6 AML

No VARA rule was found tying referral payments to source-of-funds obligations. The referral reward is an outflow of the firm's own metal to an already-KYC'd customer, so it runs through ordinary monitoring. **The real financial-crime surface here is fraud rather than laundering**, and it is §11.

---

## 13. The interface with the agent network

This document defines the boundary. It does not set agent rates.

### 13.1 🆕 The IRDAI blocker is resolved, and the answer is not the one the drafts assume

The IRDAI 2023 commission caps have been flagged as unretrieved and blocking agent economics in **four separate places** across the SIP rulebook and the scoring draft. They are now retrieved, and the finding is structural.

> **The product-wise commission caps no longer exist. The IRDAI (Payment of Commission) Regulations, 2023 were repealed and replaced by the IRDAI (Expenses of Management, including Commission, of Insurers) Regulations, 2024**, gazetted 22 January 2024, effective 1 April 2024, with Master Circular IRDAI/F&I/CIR/79/5/2024 of 15 May 2024.

**There is no number to retrieve because the regime stopped using one.** It moved to an overall Expenses of Management ceiling with a board-approved policy underneath it. §8.3 is built on that structure.

> 🔴 **And a correction we owe ourselves. The Master Circular contains no clawback-on-early-lapse provision and no overriding-commission provision.** Our drafts state that commission vests over 12 months with clawback because *"this is the standard insurance early-lapse clawback and the agent network is already built on that model."* **The regulation does not supply that.** An automated summary claimed both provisions existed; reading the eleven-page primary PDF showed otherwise.
>
> The clawback is still the right design and it must stay. But it is **a contractual choice we are making, not a regulatory inheritance we are copying**, and the drafts must be corrected to say so. The only structural brake IRDAI actually supplies is the **80% first-year versus 17.5% renewal asymmetry** and the qualitative test that commission be *"commensurate with the efforts required to acquire and sustain that type of business."*

**What survives, and it is the more useful half:** the *"acquire and sustain"* test is exactly the principle behind trailing commission payable only while the book is in force, which is what decision 13's anti-MLM defence needs. The regime supports the shape; it just does not hand us the number.

### 13.2 What the agent block still owes

| Item | Status |
|---|---|
| The commission split across the three levels | **Open.** Client-gated on the revenue model. §7.3 recommends the gradient; the rates are Phase 4 |
| The acquisition budget ceiling as a percentage of entry-fee revenue | **Open**, same gate. Structure decided in §8.3 |
| Whether the fee must rise to fund distribution | 🔴 **Open, and it is a client decision.** §8.4 |
| Vesting shape: linear, cliff or pro-rata | **Undesigned.** "Vests over 12 months" is all any draft says |
| Agent qualification, training, suitability, termination | **Entirely absent** from every client document and every draft of ours. Real work, not a caveat |
| Whose behaviour is scored when an agent invests for a client | **Left open deliberately** (scoring §10). Unchanged by this document |
| The cycler-plus-agent combination | **Left open deliberately**, defended only by the clawback, which §13.1 has just reclassified as contractual |

---

## 14. What goes to the client

Four departures and three findings. The departures are choices they can overrule; the findings are things they do not yet know.

**Departures from their documents:**

1. **Referrals leave the score and become a paid programme.** Framed as promotion, not demotion, using §1's argument: a capped supplementary point that cannot dominate is by construction a point that changes nothing, while a gram is worth a gram on the day it lands.
2. **Single level, absolutely, for member referrals.** Their V2 risk register named *"the referral + status + masterclass structure"* as a possible pyramid classification. **Their V3 dropped that risk entry from both the compliance table and the risk register while keeping the three-level cap and deleting the stated reason for it.** We are putting the risk back.
3. **A successful referral means six consecutive contributions by the referee.** Not a signup, not a KYC. Their V2 tracked at KYC confirmation.
4. **Five per year, then you are offered a contract.** No leaderboards, no escalating rates, no time-limited bonuses.

**Findings they have not been told:**

5. 🔴 **"Agent commission is paid from fee revenue and is not an additional charge to investors" cannot be true at a 5% fee against a 4.15% cost base.** §8.4, with the three resolutions and the observation that their only commission number consumes 88% of Year 1 gross margin on a fee base that no longer exists.
6. 🔴 **The referral programme must be approved by VARA as part of the licensing application.** §12.1. This is a schedule item on the critical path, not a marketing task.
7. ⚠ **Their two documents specify inverted commission gradients**, and the superseded one has the better answer. §7.3.

**One more for the call, cheap and useful:** V3 §11.1 says the three-level cap is *"enforced by smart contract"*, but V3's nine core contracts contain **no agent or referral contract**. V2 named a Contract 13 in an Annexure 8.2A that is not in the repo. Either the contract exists and we have not seen it, or the claim needs removing.

---

## 15. Open items

| # | Item | Owner | Gates |
|---|---|---|---|
| 1 | 🔴 **AANI Request to Pay per-request cost.** If net margin on a USD 20 contribution is negative, the reward on a USD 20 referee never repays | PSP conversation | The **sizing** of the whole programme (§5.4) |
| 2 | 🔴 **VARA compliance confirmation** under I.C.2.l(iii), and what conditions VARA has imposed on comparable programmes | Counsel, then VARA | **Launch** |
| 3 | ✅ **The shape is settled (Abdur, 2026-08-13): 30% of the fee, no counting cap, no referral cap, paid in grams, half each.** | Settled | — |
| 3b | 🔴 **The 30% itself is a placeholder and locks against the revenue model**, with the agent rate and the §8.3 acquisition ceiling. §5.0 notes 30% is roughly the ceiling at which the qualifying run still washes its own face from Year 3 | Phase 4 | Nothing. The mechanism holds at any rate |
| 3c | **The contribution-collapse review thresholds** (§4.4): a third of the run average, over six months. Uncalibratable without data | Us, review with the round-trip thresholds | Nothing, but it is the only defence on register item 8 |
| 4 | Whether the gram-credit rail is built at launch or the reward ships as a discount | Build, September | §4.1. Raise with the proxy and multi-tenancy notes |
| 5 | Whether a reward may land on a compliance-blocked account | Counsel batch | Nothing. Joins the existing Gold Rewards question, same answer serves both |
| 6 | Whether a contingent referral reward survives the referrer's death | Counsel | Nothing. Edge case 18 |
| 7 | VAT treatment of a gram credit versus a fee rebate | Tax adviser | Possibly the **form** of the reward (§12.4) |

**Counsel questions, phrased to forward verbatim:**

1. Does a customer who shares a referral code, without handling orders or giving personal recommendations, fall outside "VA Broker-Dealer Services" (defined as *arranging orders*, *soliciting or accepting orders*) and outside "VA Advisory Services" (*a personal recommendation*) in Schedule 1 of the Virtual Assets and Related Activities Regulations 2023? At what point does a paid referrer cross into either activity, and does the answer change if they are unpaid, paid in kind, paid cash, or engaged as a contracted agent with targets?
2. Is there any introducer or appointed-representative exemption in the VARA framework, equivalent to the UK FCA Article 33 introducer exclusion? We found none and would like that confirmed.
3. What is the procedural route and expected timeline for a compliance confirmation under Marketing Regulation I.C.2.l(iii) for a referral incentive, given a Category 1 VA Issuance application? Must it be filed as part of the application, and what conditions has VARA imposed on comparable programmes?
4. Please provide the operative UAE statutory text on pyramid selling, network marketing and multi-level marketing, with article numbers. We could not access the primary text; uaelegislation.gov.ae returns 403 to automated access.
5. Is multi-level compensation, meaning paying a customer on the activity of customers introduced by their own referees, lawful in the UAE, and if so under what licence or Ministry of Economy registration? If not, please confirm that strictly single-tier is the maximum permissible.
6. Does UAE law distinguish between a cash payment to a referrer, a discount on the referrer's own fees, a credit of gold, and loyalty points, for consumer-protection, VAT or licensing purposes?
7. Does paying a referral reward to a resident of India, Saudi Arabia, Kuwait or Qatar constitute unlicensed solicitation in that jurisdiction? We propose to geo-fence to UAE residents at launch.
8. Is a separate Dubai DET or consumer-protection promotion permit required for a referral reward or fee rebate, in addition to the VARA confirmation?

---

## 16. Corrections owed to other files

| File | Correction |
|---|---|
| `_draft_sip-rulebook.md` §9.2 item 12, §9.4, §12 | 🔴 **The 12-month clawback is a contractual choice, not an inheritance from Indian insurance regulation.** The IRDAI 2024 text contains no clawback provision. Reword *"the standard insurance early-lapse clawback and the agent network is already built on that model"* |
| `_draft_sip-rulebook.md` §14 sources table | The row *"IRDAI 2023 caps still unretrieved and still block agent economics"* is **resolved**. Replace with the 2024 EOM regime, and note there is no number to retrieve |
| `_draft_ics-scoring.md` §10 | The two open agent items are unchanged in substance, but the note that they wait *"pending the same IRDAI retrieval"* is now wrong. **The retrieval has happened. They wait on the revenue model instead** |
| `_draft_ics-scoring.md` §5 | Reason 2 for removing referrals from scoring says they are *"already paid by the 3-tier agent commission."* **That was true only for agent-originated customers.** It is now true for member referrals too, via this document. Strengthen the sentence rather than change the decision |
| `_draft_ics-benefits.md` §0.1 | 🔴 **Amend the no-pool test, do not merely cite it.** Its first limb reads *"recycles investor fees into investor payouts"*, which on its face catches any commission. Restate the operative distinction as **paid for holding versus paid for doing**, so the rule catches pools and not acquisition costs. §8.2 explains why. **This is a change to a settled rule and it needs Abdur's sign-off** |
| `_draft_ics-benefits.md` §7 | Add the note that the referral reward draws on stream 1 and is not a benefit, so the funding-test rule is unbroken. Say it explicitly or someone will read it as a sixth benefit |
| 🔴 `_draft_ics-scoring.md` §1.5, denominator rules table | **A latent arithmetic error, and it is not ours alone.** The table says Gold Rewards grams *"enlarge the denominator, so a reward never creates or reduces a penalty. Sold clamps at 0 either way."* **True only where Sold is already zero.** For any account with Sold above zero, a credited gram held strictly reduces Sold and raises Retention. **Exclude reward grams from both sides of the ratio**, for Gold Rewards and referral rewards alike. §10.4 |
| `handoff.md` decision 13 | *"Combine with the IRDAI trailing-commission structure for two independent structural defences"* is now **one structural defence plus one contractual choice**, per §13.1. The IRDAI clawback is not regulatory |
| `_draft_ics-scoring.md` §1.6a | The *"4 of 6"* countdown is the account holder's own display. **Record that it is not readable across accounts**, or the referral build will export it. §10.3 |
| Token specification, wherever it lands | 🔴 **AURX decimal precision is undefined in every draft.** It now binds in two places: reward rounding (edge case 24) and the register invariant `sum(register sub-accounts) = tokens_outstanding`. Raise with the September build |
| `handoff.md` §7, pricing rule | Unchanged, but note it is now load-bearing in a fourth place. **The AM-or-PM question needs deciding**, not recommending |
| `Aurumix_Process_Maps_Revenue_Streams.md` | Acquisition spend is a **cost line against stream 1**, and it is the same budget for agents and members. Currently unrepresented |
| `_draft_allocation-and-float.md` | The entry-fee build-up has **no acquisition-cost line at all**. At Year 1 that is the difference between a 0.85pp margin and a negative one (§8.4) |
| handoff.md §6 | New decision 47. §7's "IRDAI caps unretrieved" entries resolve |

---

## 17. Sources and confidence

| Claim | Source | Type | Confidence |
|---|---|---|---|
| VARA Marketing Regulation I.C.2.l, incentives need compliance confirmation | rulebooks.vara.ae, VARA_EN_419_VER1.pdf, verbatim | Primary | **High** |
| VARA Guidance referral case study | rulebooks.vara.ae/entiresection/14 | Primary, expressly non-binding | **High** |
| Broker-dealer and advisory definitions are order and advice centric | rulebooks.vara.ae, Schedule 1, verbatim | Primary | **High** |
| Third-party marketing liability, I.C.5 | Same | Primary | **High** |
| No UAE introducer exemption found | Searched, negative result | — | Medium |
| UAE pyramid statute | **Not retrieved.** Portals return 403 | — | **Unverified** |
| Pyramid conduct charged as fraud, Art 451 of Decree-Law 31/2021 | Lexology | Secondary | Medium |
| IRDAI EOM Regulations 2024 repealed the 2023 commission regulations | Master Circular PDF read directly, 11 pages, plus the consolidated gazette list | Primary | **High** |
| No clawback or overriding-commission provision in the 2024 text | Read the primary PDF | Primary, negative | **High** |
| Life EOM 80% first-year / 17.5% renewal, general 30%, health 35% | taxguru reproduction cross-checked against the Master Circular | Secondary, cross-checked | Medium-High |
| NSE prohibited referral commissions to unregistered persons, Aug 2024 | business-standard.com, Zerodha Z-Connect | Secondary | Medium |
| Kinesis Referrer's Yield 7.5% for life, single level; Partner's Yield up to 25% of a network | kinesis.money, own pages | Primary | **High** |
| No referral programme at 19 other gold protocols and 4 adjacent products | Searched each, negative result | — | Medium-High |
| Jar pays at the 5th transaction plus 1% trailing | myjar.app blog, 403 to automated fetch, search-index sourced | Secondary | Medium |
| Tanishq Golden Harvest: no discount below 6 instalments | tanishqgoldenharvest.co.in terms | Primary | Medium |
| OKX UAE referral terms: 90-day lock, AED 1,000 for 30 days, sub-accounts excluded | okx.com UAE referral terms, blocks automated fetch | Primary, index-sourced | Medium-High |
| Mashreq NEO: AED 100, AED 3,000 deposit, 20-referral cap | Mashreq | Primary | **High** |
| Binance FZE users disqualified from the global referral programme | Binance referral terms PDF | Primary | **High** |
| Referred customers worth 16%+ more, churn ~18% slower, EUR 25 bonus returned ~60% ROI over 6 years | Schmitt, Skiera and Van den Bulte, *Journal of Marketing* 75(1), 2011 | Peer-reviewed | **High** |
| Recipient-benefiting referrals recruit more | Gershon, Cryder and John, *JMR*, 2020 | Peer-reviewed | Medium-High |
| Referral rewards can backfire for unfamiliar products, attenuated by rewarding both sides | Dose, Walsh, Beatty and Elsner, *JAMS*, 2019 | Peer-reviewed | Medium-High |
| Forsage, BitConnect, OneCoin, Karatbars reclassified on downline compensation | SEC, CFTC, DOJ, BaFin releases | Secondary on the releases | Medium |
| Entry-fee build-up, gross margin, USD 1.61 retained, persistency curve | Our own drafts, decisions 9, 22, 34 | Internal | As per those files |

⚠ **Two claims corrected during research and recorded so they do not return:** the invented VARA broker-dealer wording covering *"introducing"*, and a UAE pyramid test that was actually sourced from the US FTC.

⚠ **Deliberately excluded:** the widely quoted fintech referral benchmarks, referral CAC of USD 20 to 60 against paid CAC of USD 100 to 300, referrals as 25 to 40% of fintech new users, and the Wise, Wealthsimple and Nubank figures. **Every one of them traces to referral-software vendor blogs rather than company disclosures.** They are not in this document and they must not reach the client as fact.
