---
brand: Tokenomics.net
type: simulation-setup-explainer
source: rewrite
created: 2026-09-02
---

# Aurumix gold savings simulation

**Prepared by**: Tokenomics.net
**Date**: September 2026

---

## 1. What the simulation is for

### The business in one paragraph

Aurumix sells gold by the gram. A customer commits to a monthly amount from USD 20. Every dollar buys allocated physical gold in a Dubai vault. One AURX token is one gram.

The customer pays a 5% entry fee and nothing else. Behind the savings product sit a card, a credit line against the gold, a family plan, and a platform fee from B2B partners who white-label the product.

### What the revenue model already says

The Phase 4 revenue model is a spreadsheet. It says the business makes USD 939k in year seven and needs USD 2.27m of funding at its worst point.

Those are single numbers. They rest on about ninety assumptions. The client has no customer data yet. No waitlist, no pilot, no partner in the pipeline.

### The three questions

The simulation does not ask what will happen. It asks three harder questions.

- What has to be true for this business to be profitable?
- How much can Aurumix afford to give back to loyal customers?
- How much money does it need to raise to still be standing in nine paths out of ten?

### Why a threshold and not a forecast

A forecast built on unsourced inputs is a guess with decimal places. A threshold is different. It says "you need this many paying customers," and that number does not depend on whether the market funnel is right.

I think that is the only honest deliverable at this stage. The document is built around it.

---

## 2. One system, run whole

### The principle

The revenue model is a description of the business. The simulation is the business running.

So every rule in the revenue model lives inside the simulation, executing on simulated customers, month by month. The vault bill is charged on the grams they actually hold. Card fees are earned on what they actually spend. The loyalty discount is priced at the tier each of them actually reached. Nothing is computed as an average customer times a head count.

We call this the twin. One system. There is no simplified copy of the business running beside it.

### What the twin takes from the revenue model

Parameters. Prices, fees, the licence costs, the vault contract, the card economics, the marketing budget, the salary lines. These are facts about the business. Keeping a second copy of them would only create two versions of the truth.

### What the twin refuses to take

The spreadsheet's shortcuts. One average customer multiplied by a count. A single flat churn rate. A blended discount applied to a flat share of the book. And the grid.

The spreadsheet reports twenty-four monthly columns and then one column per year. That is a spreadsheet's shape, not a business's. Section 3 shows why it mattered.

### An admission

An earlier build of this simulation ran two engines: a line-for-line port of the spreadsheet doing the economics, with a population of individual customers running beside it. The stated reason was speed. The claim was that running the population inside every path would take hours.

Measured, it takes a third of a second. The claim was wrong, and it was never checked before being written down. The two-engine build is gone, and this document describes what replaced it.

---

## 3. The clock

| | |
|:--|:--|
| Horizon | 84 months, seven years |
| Month 1 | January 2027 |
| Step | one month, every month |
| Paths | 2,000 |

### Why monthly matters: the trough

The funding requirement is the deepest point of a cash line. You must raise enough to survive the worst month, not the worst year-end.

On the old grid, the last sixty months were five annual observations. A trough that falls between two year-ends is invisible there, so the raise number could only be understated.

Measured monthly, the cash trough falls in **month 39**. That month sits in the middle of an annual column the spreadsheet cannot see inside. Finding it moved the deterministic funding need from USD 2.27m to **USD 2.50m** before any uncertainty is priced at all.

---

## 4. The customer

Each simulated customer carries five things at birth. A region, a monthly ticket, a payment personality, a payment rail, and an entry door.

### Region

One of the UAE, Oman and Bahrain together, or India. Region sets the average ticket, the acquisition cost, and when the market opens. India and the UAE open in month one. Oman and Bahrain open in month thirteen.

### Ticket

The ticket is the amount the customer means to save each month. The revenue model uses one number per region, USD 33.60 in the UAE.

Savings books are not like that. About 30% of the book sits at the USD 20 floor. A thin tail saves far more. So each customer draws a ticket from a curve fitted to two facts, the regional mean and the share at the floor:

$$\text{ticket} = \max\left(20,\; X\right), \qquad X \sim \text{Lognormal}(\mu, \sigma)$$

Where:

- $\mu$ and $\sigma$ are solved so that $P(X \le 20) = 0.30$ and $E[\max(20, X)]$ equals the regional mean
- $20$ is the USD floor, below which a payment is refused

The two facts lock the curve between them. If 30 customers in 100 pay exactly USD 20, that is USD 600 of a USD 3,360 total, so the other 70 must average USD 39.43. The top tenth of customers ends up contributing about a quarter of all money saved.

The floor share is not sourced. It is a defensible shape, set at 30% on client instruction, and it is swept.

### Payment personality

Five types, tuned to reproduce one curve:

| Archetype | Share | Pays in a given month | Own monthly lapse hazard |
|:--|--:|--:|--:|
| Perfect payer | 10% | 99.5% | 0.00% |
| Occasional misser | 35% | 93% | 0.46% |
| Alternating misser | 12% | 55% | 1.19% |
| Reducer | 13% | 97% | 0.13% |
| Early lapser | 30% | 60% | 13.25% |

A background hazard of 1.06% per month applies to everyone on top of their own.

The curve underneath is the **persistency curve**: how many customers are still paying as time passes. Ours runs 63% at month 13, then 49, 41, 34 and 29% at months 25, 37, 49 and 61. The level is anchored to Indian life insurance persistency, published by the regulator at the same checkpoints, industry average about 63% at month 13. We take the level and reject the shape, because an insurance saver who quits forfeits surrender value and a gold saver forfeits nothing, so our curve keeps falling where theirs flattens.

### What the five types buy that a churn rate cannot

The spreadsheet loses customers at one constant rate forever, so a cohort decays to 4% by month 84. In the twin, the early lapsers leave in year one, and the survivors are disproportionately the disciplined types. A cohort settles near 23%.

The other thing a churn rate cannot say: a live customer does not pay every month. The book pays in about **78% of the months it could**. A paying customer contributes about USD 313 a year against USD 403 if nobody ever missed. The spreadsheet's paying customers pay every month by construction, which quietly flatters every revenue line.

### Rail and door

The rail is how the money moves: a standing instruction, or a manual payment each month. Manual payers miss more. The rail mix is a lever the client controls, and section 12 prices it.

The door is how they arrived: marketing, an agent, or a referral.

---

## 5. A month in the system

The core loop. Every month, in this order.

1. **Gold moves** to this month's price.
2. **New customers arrive.** Marketing reach at this month's cost per customer, agents, and referrals from the customers already in the book, all against the addressable ceiling. Section 7 covers each.
3. **Each new customer** is given a region, ticket, personality, rail and door.
4. **Existing customers decide whether to pay.** Their personality sets the odds.
5. **Payments become gold** at this month's price, minus the entry fee at that customer's tier.
6. **Some customers redeem** part of their gold, or take physical delivery.
7. **Streaks update.** Six consecutive payments opens the loyalty gate, once, permanently.
8. **The loyalty score recalculates** from payment record, recent standing, and whether they sold gold.
9. **Tiers reassign** from the score.
10. **Cards, family plans and credit lines** run for whoever holds them, against their own gold.
11. **Some customers leave.** Their own hazard plus the background rate.
12. **Partners** sign or fail to sign.
13. **The ledger closes.** Five revenue streams plus the partner fee, the fabrication premium, the vault bill on the metal actually held, licences, acquisition, the card programme, contingency, profit, and the cash line.

---

## 6. The loyalty ladder

### The gate

Six consecutive monthly payments. One property of one person's history. This is the fact that forces a simulation of individuals: six-in-a-row cannot be recovered from an average.

About **53% of the live book** has opened the gate by month 84. The workbook assumed 55% as a flat input. The twin computes it, and it takes years to get there.

### What a tier buys

| | Untiered | Silver | Gold | Platinum | Sovereign |
|:--|--:|--:|--:|--:|--:|
| Entry fee | 5.0% | 4.5% | 4.0% | 3.5% | 3.0% |
| Family discount | 0% | 10% | 20% | 35% | 50% |
| FX margin | 2.0% | 2.0% | 1.5% | 1.25% | 1.0% |
| Borrow against gold | 50% | 50% | 65% | 72.5% | 80% |
| Card rewards | 0% | 0.15% | 0.45% | 0.60% | 0.75% |

The 5% entry fee is a hard cap. Nobody ever pays more. The ladder only gives back.

### Who actually gets there

Of the customers holding a tier at month 84: 39% Silver, 45% Gold, 15% Platinum, 1.5% Sovereign. Sovereign requires years of near-perfect payment. Almost nobody clears it inside the horizon, which is what makes it cheap to offer and meaningful to hold.

### How the giveback is priced

At each customer's own tier, on each customer's own activity, every month. Not as a blended rate on a flat share of the book. Priced this way, the giveback costs about 6 to 7% of revenue across the seven years.

One rule caps it per customer: rewards paid to a customer never exceed the revenue that customer has generated. That cap can only be enforced at customer level, which is one more reason the business runs on customers.

---

## 7. How customers arrive

Three channels, then a brake.

### Marketing

The client's budget, divided by the cost of reaching one customer. That cost is not flat. The budget rises eighteen-fold over seven years, and cheap channels exhaust. So cost per customer rises with spend intensity in each region. This curve existed in the revenue model's own design notes and was switched off there; the simulation switches it on and sweeps its strength.

### Referrals, from the book itself

The spreadsheet counts referrals off the raw paying head count, so a customer in month two is as persuasive as one in year three. They are not. In the twin, each customer's referral capacity is zero for three months, ramps to full by month twelve, and rises with tier. A young book refers at about a third of its mature rate. Referrals also cost money: the reward is a share of the referred customer's entry fees.

### Agents

Field agents, mostly in India. Headcount times productivity times a ramp.

### The brake

Each region has an addressable ceiling built from population filters the client has confirmed are unsourced. India reaches 85% of its ceiling by year seven, so this number nearly binds the whole model. The twin treats it as uncertain and draws it, from 0.6 to 1.55 times the estimate. It turns out to be one of the four biggest drivers of profit in the entire simulation. A number that important does not get to be a point estimate.

---

## 8. Partners

B2B partners white-label the product and pay a platform fee on the assets their users hold. The plan says eleven by year seven.

### What one partner is worth

A partner brings a user base. Some share of those users adopt the product, each holding some average value in gold, and Aurumix earns the platform fee on the total. At base assumptions that is about USD 142k a year, every year, per partner. All three ingredients carry client-priced ranges and all three are drawn.

### How they arrive

Partners are entities in the twin, not a straight line. In each path they arrive lumpily: a year can sign nobody, and when a year does sign, it can sign more than planned. The process is centred on the client's plan. The lumpiness widens the range of outcomes without quietly moving the middle, because doubting the plan itself is a position that must be declared, not smuggled inside a noise process.

### Why this section is short and matters most

Partner assumptions are the top three bars of the sensitivity tornado. In fixed-cost coverage, one partner does the work of roughly 40,000 retail customers, because a retail customer's margin survives serving cost and replacement while a partner's fee arrives nearly whole. There is nothing else to model, and that is the point: the business's biggest driver has the fewest moving parts and no evidence behind it yet. A signed letter of intent would do more for the raise than any refinement of this simulation.

---

## 9. Gold and the float

### The price

One gold price for the whole system, following geometric Brownian motion:

$$S_{t+1} = S_t \exp\!\left[\left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\; \varepsilon_t\right], \qquad \varepsilon_t \sim \mathcal{N}(0,1)$$

Where:

- $\mu$ is the drift, 8.1% a year, the revenue model's own appreciation assumption
- $\sigma$ is volatility, 15% a year, the long-run realised figure for gold in USD, swept 10 to 22%
- $\Delta t$ is one month

Gold barely moves the business. Customers own the gold; Aurumix earns fees on flows. A 30% crash costs the base case almost nothing. This surprises people, and it is one of the most useful things the simulation shows.

### The float

Aurumix keeps a working inventory of gold so that purchases settle instantly. A separate daily model sizes it with a standard inventory policy: order up to a level that covers expected demand over the delivery lead time plus a safety margin, in whole bars. It runs on the twin's own monthly purchases, which carry the seasonality the old annual columns averaged away.

---

## 10. Two thousand worlds

Each path is one version of the next seven years. Three things are drawn per path.

**Seventy-nine parameters.** Every input the client priced with an Aggressive and a Conservative value is drawn from a distribution peaked at Base with those two as the tails. The rule is opt-out, not opt-in: if the client priced a range, it belongs in the raise number. Eleven parameters are excluded, each with a written reason, mostly because the twin computes them from behaviour instead. The blended loyalty discount is the clearest example: the twin prices each customer at their own tier, so a blended rate has nothing left to describe.

**A gold path**, from section 9.

**A partner history**, from section 8.

On top of these, demand gets a monthly wobble, and every path reruns the full population from scratch: who arrives, who pays, who gates, who leaves.

---

## 11. What comes out

Stack 2,000 paths and read the spread.

| Output | Meaning |
|:--|:--|
| Safe raise | the funding trough deep enough to survive 9 paths in 10 |
| Break-even odds | share of paths whose cumulative profit turns positive by year 7 |
| Profit spread | year-seven net profit at the 10th, 50th and 90th percentile |
| Book size | paying customers at month 84 |
| Margin call odds | chance the credit book ever needs collateral topped up |

The results document carries the numbers and what they mean for the raise. This document stops at how they are produced.

---

## 12. What it takes to be profitable

The client's question is a threshold, and it is computed at steady state, where the book is flat and acquisition only replaces the customers who leave.

$$N^* = \frac{k \cdot F}{r - k\,(s + c \cdot \text{CAC})} \qquad\qquad K^* = \frac{k \cdot F}{A \cdot f}$$

Where:

- $N^*$ is paying customers needed for retail to stand alone, $K^*$ is B2B partners needed to cover the fixed base by themselves
- $F$ is the fixed cost base, about USD 412k a year
- $r$ is retail revenue per paying customer per year, about USD 32 excluding B2B
- $s$ is the serving cost per customer, about USD 11
- $c$ is annual churn, 32%, measured from the twin's own mature book rather than assumed
- CAC is the cost to replace one customer, USD 44 blended or USD 55 in the UAE alone
- $A$ is assets under management per partner, $f$ is the platform fee
- $k$ is the contingency multiplier

### The honest answer

At 15% contingency, retail alone needs about **140,000 paying customers**. The base case builds 90,000 by month 84. At 30% contingency and above, no retail book clears the bar at all: the margin per customer goes negative before the count matters.

**Or 3.3 partners cover the fixed base by themselves.**

Retail alone is thinner than the spreadsheet made it look, for one honest reason: real customers skip months. Revenue per paying customer is USD 32, not the USD 38 an always-pays book produces, and more than half of it is consumed by replacing churn. The business case runs through B2B, and the retail book's job is to be the product those partners white-label.

The levers that move the retail margin, in order of effect: trim the ladder's generosity, push the standing-instruction rail, and reallocate marketing away from the dearest region. Together they roughly quadruple cumulative profit at year seven. The results document prices each.

---

## 13. Stress tests

Seven deliberate bad days, run separately through the twin.

| Scenario | Y7 profit | Cumulative at Y7 | Peak funding |
|:--|--:|--:|--:|
| Base | $797k | $518k | $2.50m |
| Gold crashes 30% at M24 | $797k | $519k | $2.49m |
| Redemption run, 25% at M24 | $740k | $336k | $2.53m |
| No B2B at all | −$763k | −$4.59m | $6.17m |
| Adoption failure | $564k | −$430k | $2.69m |
| Regulatory delay, 12 months | $797k | −$221k | $3.24m |
| Ticket compression | $700k | $207k | $2.51m |
| Combined tail | −$111k | −$2.64m | $4.17m |

Two readings. Gold is not the risk: the crash scenario is indistinguishable from base. **B2B is the whole risk**: remove it and the business loses USD 4.6m over seven years and needs USD 6.2m of funding.

One stress had to be rebuilt for the twin. "Customers pause contributions" used to be modelled by cutting the average ticket to USD 13. The twin refused: a ticket below the USD 20 floor cannot exist. A pause is customers skipping months, so it is now a six-month cut to payment odds. The old trick also ran the cut for all seven years instead of during the run, which overstated the damage.

---

## 14. How we know it is not lying

### Reconciliation, not equivalence

The old build proved its port reproduced the spreadsheet to within rounding. The twin is not a port, so that proof means nothing here.

What replaces it is a reconciliation: every line of year seven, twin against spreadsheet, with the cause of every difference written down. A difference without a recorded cause fails the run. All twenty-one lines are currently accounted for. The largest: the twin carries 14% more paying customers, because survivors are disciplined; and it books 10% more funding need, because it can see the trough.

### What the twin found in the spreadsheet

Running the same rules on individuals exposed two defects in the revenue model itself. Card rewards are computed by multiplying a percentage-of-spend rate by card revenue rather than card spend, which understates that cost roughly twenty-fold. And the FX discount is applied to card fees that contain no FX margin. Both are logged for the Phase 4 fix list.

### The standing audit

Twenty-seven checks run after every change. Every priced range reaches the Monte Carlo. The giveback vanishes if the ladder is flattened, proving it is priced from real tiers. Persistency moves the book. Peak funding is the true maximum of a monthly line. The Monte Carlo does not import the old port. Each check exists because its failure happened once.

### Verification is not validation

All of this proves the code does what this document says. None of it proves the assumptions are right. Nothing can, until there are customers. That is why the deliverable is a threshold and a spread, not a forecast.

---
