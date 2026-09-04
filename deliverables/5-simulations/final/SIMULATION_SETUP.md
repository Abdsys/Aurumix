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

The Phase 4 revenue model is a spreadsheet. It produces one seven-year projection from about ninety assumptions. There is no customer data yet. No waitlist, no pilot, no partner in the pipeline.

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

Every rule in the revenue model lives inside the simulation, executing on simulated customers, month by month. The vault bill is charged on the grams they actually hold. Card fees are earned on what they actually spend. The loyalty discount is priced at the tier each of them actually reached. Nothing is computed as an average customer times a head count.

We call this the twin. One system, one engine.

### What the twin takes from the revenue model

Parameters. Prices, fees, the licence costs, the vault contract, the card economics, the marketing budget, the salary lines. These are facts about the business. Keeping a second copy of them would only create two versions of the truth.

### What the twin computes for itself

Everything behavioural. Who arrives, who pays, who reaches a tier, who leaves, who refers, what each of them costs and earns. The spreadsheet approximates these with one average customer, one flat churn rate, and one blended discount. The twin replaces each approximation with the individual behaviour underneath it, and the rest of this document describes exactly how.

---

## 3. The frame

| | |
|:--|:--|
| Method | agent-based simulation inside a Monte Carlo |
| Horizon | 84 months, seven years |
| Month 1 | January 2027 |
| Step | one month, every month, for everything |
| Paths | 2,000, each a full rerun of the population |
| Customers per path | not fixed: an outcome of each path, around 170,000 at the median |
| Resolution | one simulated agent per customer in the final run; 1 agent per 10 while iterating |
| Drawn inputs per path | 75 parameters, plus a gold path and a partner history |
| Randomness | fixed seeds, so every run is exactly reproducible |

Agent-based means the unit of computation is one customer, carried through their whole history. Monte Carlo means the entire seven years is rerun 2,000 times, each time under different assumptions drawn from stated ranges. Section 10 covers the drawing. Everything before it covers what happens inside one path.

---

## 4. The customer

Each simulated customer is created with five properties: a region, a monthly ticket, a payment personality, a payment rail, and an entry door. Their whole later life follows from these plus luck.

### Region

One of the UAE, Oman and Bahrain together, or India. Region sets the average ticket, the acquisition cost, and when the market opens. India and the UAE open in month one. Oman and Bahrain open in month thirteen.

### Ticket: how much they mean to save

The revenue model uses one number per region, USD 33.60 in the UAE. Savings books are not like that: most of the book saves little and a thin tail saves a lot. So each customer draws a personal ticket from a curve fitted to two facts, the regional mean and the share at the floor:

$$\text{ticket} = \max\left(20,\; X\right), \qquad X \sim \text{Lognormal}(\mu, \sigma)$$

Where:

- $\mu$ and $\sigma$ are solved numerically so that $P(X \le 20) = 0.30$ and $E[\max(20, X)]$ equals the regional mean
- $20$ is the USD floor, below which a payment is refused

Each region fits its own curve to its own mean; the USD 20 floor and the 30% floor share are common to all three. The two facts lock the curve. If 30 customers in 100 pay exactly USD 20, that is USD 600 of a USD 3,360 total, so the other 70 must average USD 39.43. For the UAE this solves to $\sigma = 0.576$, and the top tenth of customers ends up contributing about a quarter of all money saved.

The amount actually declared in a given month wobbles around the personal ticket:

$$\text{amount}_t = \max\left(20,\; \text{ticket} \times e^{\,0.25\,\varepsilon_t}\right), \qquad \varepsilon_t \sim \mathcal{N}(0,1)$$

A saver at the floor pays exactly the floor. Whether they pay at all is the personality's job, below.

### Payment personality: whether they pay, and whether they stay

Five types. Each type carries a monthly probability of paying and its own monthly hazard of stopping the plan:

| Archetype | Share | Pays in a given month | Own monthly lapse hazard |
|:--|--:|--:|--:|
| Perfect payer | 10% | 99.5% | 0.00% |
| Occasional misser | 35% | 93% | 0.46% |
| Alternating misser | 12% | 55% | 1.19% |
| Reducer | 13% | 97% | 0.13% |
| Early lapser | 30% | 60% | 13.25% |

Each month, every active customer:

- **pays** with probability $p_t = \max(p_0 \cdot d^{\,\text{age}},\; p_{\min})$, where $p_0$ is the type's rate from the table and age their months on the platform. $d$ is a fade dial and $p_{\min}$ its floor. Both are off at base ($d = 1$, $p_{\min} = 0$), so the base case pays at the flat rate; the dials exist for sweeps that test whether enthusiasm wears off
- **leaves** with probability equal to their own hazard plus a background hazard of 1.06% per month that applies to everyone

Together the five types imply the book pays in roughly 78% of the months it could. That single property separates this model from the spreadsheet, whose paying customers pay every month by construction.

### Where the five types come from

They are not observed segments. They are a mixture tuned to reproduce one target curve. A cohort should have 63% still paying at month 13, then 49, 41, 34 and 29% at months 25, 37, 49 and 61. When the Monte Carlo draws a different month-13 persistency, every hazard is rescaled by a single factor so the cohort hits it. One factor, not five free parameters, so the mix and its ordering survive.

### Why the curve keeps falling

The 63% level is anchored to Indian life insurance persistency, published by the regulator at the same checkpoints. But insurance curves flatten after year one, and ours does not, on purpose. An insurance saver who quits forfeits surrender value, so the penalty does the retaining. An Aurumix saver forfeits nothing: the gold is theirs and leaving is free. Easy exit means we should expect weaker long-run retention than a penalty-locked product, so the twin borrows the anchor's level and rejects its flattening. This is a deliberately conservative choice, and persistency is drawn per path in any case.

### Rail: how the money moves

Each customer is assigned a rail at birth: a standing instruction ("set and forget"), or a manual payment each month. At base, 30% of joiners take the standing instruction; the share is swept, and it is a lever Aurumix controls.

The rail changes who the customer is, not just how they pay. A customer on the standing instruction has a 35% chance of being re-drawn from the disciplined types (perfect payer, occasional misser, reducer). That is the modelled link between removing friction and clearing six consecutive payments. Both numbers are unsourced and swept.

### Door

How they arrived: marketing, an agent, or a referral. The door carries the acquisition cost attached to that customer and drives the referral economics in section 7.

### Spot purchases: buying outside the plan

On top of the monthly plan, an active saver can make one-off purchases. Each month, each saver has a chance of one:

$$P(\text{spot this month}) = \text{attach}_r \times m_a \times \frac{\text{freq}}{12}, \qquad \text{amount} = \text{ticket}_r \times m_t \times \text{noise}$$

Where:

- $\text{attach}_r$ is the regional share of savers who spot-buy at all: 12% UAE, 10% Oman and Bahrain, 35% India
- $\text{freq}$ is how often a spot buyer buys, 1.7 times a year at base
- $\text{ticket}_r$ is the regional spot amount: USD 190, 145 and 40
- $m_a$ and $m_t$ are drawn multipliers on attach and amount, and freq is drawn too, so spot behaviour varies per world
- noise spreads individual purchases around the regional average, the same way monthly tickets wobble

A spot purchase pays the entry fee at the customer's tier and becomes gold like any other money in. One simplification to know: spot rides on the existing saver book, per the revenue model's attach structure. A spot-only customer who never opens a plan is not modelled, because no number exists yet for how many there would be.

### What a customer does with their gold

Two exits exist for gold, and neither involves physical delivery, because Aurumix does not offer physical delivery.

- **Redemption**: the customer sells gold back for cash. Each month each customer has a 0.5% chance of redeeming (a 6% annual rate spread across twelve months), and a redemption sells a quarter of their holding. Lapsed customers who still hold gold redeem at 1.6 times that rate, 0.8% a month. Redeemed metal returns to Aurumix and is recycled into the float.
- **Self-custody**: the customer moves AURX tokens to their own wallet. Also a 0.5% monthly chance, also a quarter of the holding. Nothing is redeemed: the gold stays in the vault, the vault bill keeps running on it, and it still counts in AUM. What changes is the account. The ICS score and the credit line are tied to the account, so tokens moved out stop counting toward the score and stop backing the credit line.

Both exits count against the loyalty score, because the score is tied to the account: gold sold back is gone, and tokens moved to your own wallet no longer count toward it. Section 6 shows how.

---

## 5. A month in the system

The core loop. Every month, in this order.

1. **Gold moves** to this month's price.
2. **New customers arrive**, channel by channel, against the market ceiling (section 7).
3. **Each new customer** is created with region, ticket, personality, rail and door.
4. **Existing customers decide whether to pay**, at their personality's odds.
5. **Monthly payments and any spot purchases become gold** at this month's price, minus the entry fee at that customer's tier.
6. **Some customers redeem for cash, some move tokens to their own wallet**, per the rates above.
7. **Streaks update.** Six consecutive payments opens the loyalty gate, once, permanently.
8. **The loyalty score recalculates** for everyone (section 6).
9. **Tiers reassign** from the score.
10. **Cards, family plans and credit lines** run for whoever holds them, each against that customer's own gold.
11. **Some customers leave**, at their own hazard plus the background rate.
12. **Partners sign**, or fail to (section 8).
13. **The ledger closes**: five revenue streams plus the partner fee, the fabrication premium on net new metal, the vault bill on all metal held, licences, acquisition costs, the card programme, contingency on the uncertain costs, profit, and the cash line.

---

## 6. The loyalty ladder

### The gate

Six consecutive monthly payments. One property of one person's history, which is the fact that forces a simulation of individuals: six-in-a-row cannot be recovered from an average. The gate opens once and never closes.

### The score

Once gated, a customer's Integrated Continuity Score is recomputed every month from three ingredients:

$$\text{Score} = \min(\text{Record},\; \text{Standing}) \times \text{Retention}$$

Where:

- **Record** rewards accumulated history: it climbs by $\tfrac{50}{12}$ per counted month to 50 at one year, then by $\tfrac{50}{48}$ per month to 100 at five years. Five years of saving is a complete record.
- **Standing** rewards the recent twelve months: the count of paid months in the last twelve, times $\tfrac{100}{12}$.
- **Retention** penalises gold leaving the account, whether sold back or moved to the customer's own wallet. Up to 30% in a year and nothing happens; beyond that, $\text{Retention} = 1 - \frac{\text{sold} - 0.30}{0.70}$.
- Once gated, the score never falls below 25.

The $\min$ means neither a long history nor a good recent year can substitute for the other. Tiers follow fixed cutoffs: Silver at 25, Gold at 50, Platinum at 75, Sovereign at 100. Sovereign therefore requires a five-year record and a perfect recent year at once, which makes it nearly unreachable inside the horizon by construction: expensive to earn, cheap to offer.

### What a tier buys

| | Untiered | Silver | Gold | Platinum | Sovereign |
|:--|--:|--:|--:|--:|--:|
| Entry fee | 5.0% | 4.5% | 4.0% | 3.5% | 3.0% |
| Family discount | 0% | 10% | 20% | 35% | 50% |
| FX margin | 2.0% | 2.0% | 1.5% | 1.25% | 1.0% |
| Borrow against gold | 50% | 50% | 65% | 72.5% | 80% |
| Card rewards | 0% | 0.15% | 0.45% | 0.60% | 0.75% |

The 5% entry fee is a hard cap. Nobody ever pays more; the ladder only gives back. The ladder itself is a swept design object: its ceiling, its steepness and its breadth are all dials the simulation prices.

### How the giveback is charged

Every component is priced per customer per month, as activity times the gap between the standard price and that customer's tier price:

- entry discount: contributions $\times$ (5.0% $-$ tier entry fee)
- FX discount: foreign card spend $\times$ (2.0% $-$ tier FX margin)
- rewards: card spend $\times$ tier rewards rate
- family discount: family fee $\times$ tier discount

### The cashback cap

One rule applies to the gold cashback, and to the cashback only: it is capped against the customer's own card transactions. Cashback on a transaction never exceeds what that transaction earns Aurumix, which is the interchange net of the scheme's share plus the FX margin.

At quoted rates the structure satisfies this by itself. A dollar of spend earns Aurumix 1.1 to 1.4 cents and the top cashback tier pays 0.75 cents, so the cap never binds in the base case. It sits in the simulation as a safety rail: when a sweep makes the ladder more generous or a path draws interchange low, this is what stops the model from paying customers to spend.

---

## 7. How customers arrive

Three channels and a brake decide each region's new customers each month:

$$\text{new}_t = \Big(\underbrace{\tfrac{B_t}{\text{CAC}_t}(1 + o)}_{\text{marketing}} + \underbrace{W_t \cdot \tfrac{\rho}{12} \cdot v}_{\text{referrals}} + \underbrace{a_t \cdot g \cdot r_t}_{\text{agents}}\Big) \times \underbrace{\Big(1 - \tfrac{\text{acquired so far}}{\text{ceiling} \times m}\Big)}_{\text{saturation}} \times \text{season}_t$$

### Marketing

$B_t$ is the region's slice of the monthly marketing budget and $o$ an organic uplift of 25%. $\text{CAC}_t$, the cost of reaching one customer, has two parts:

$$\text{CAC}_t = \underbrace{\left[c_1 + (c_7 - c_1)\tfrac{y-1}{6}\right]}_{\text{planned ramp}} \times \underbrace{\left[1 + \kappa \left(\tfrac{B_t}{60{,}000}\right)^{0.7}\right]}_{\text{channel exhaustion}}$$

The ramp is the plan: UAE cost falls from USD 85 to USD 55 by year seven as the brand matures. The second term pushes back: spend rises eighteen-fold over the horizon, cheap channels exhaust, and each further customer costs more to reach. $\kappa$ is 0.35 at base and is drawn between 0.15 and 0.60, so the raise prices not knowing how strong the exhaustion is.

### Referrals

$W_t$ is the book's referral capacity: every paying customer's individual propensity, summed. A customer's propensity is zero for their first three months, ramps linearly to full by month twelve, and is multiplied up the tier ladder (1.0 untiered rising to 1.75 at the top). $\rho$ is the referral rate, 0.6 per fully established customer per year, and $v$ the 62% conversion of referrals into customers.

So a young book refers at about a third of the rate its head count suggests; a matured book at the full rate. Referrals also cost money: the reward is 30% of the referee's first six months of entry fees.

### Agents

$a_t$ field agents (the plan runs them mostly in India), each converting $g = 6$ customers a month, times a productivity ramp $r_t$ that starts at 60% in year one.

### Saturation and the calendar

Each region has an addressable ceiling, an estimate of how many people can ever be reached, built from population filter assumptions. Acquisition scales down linearly as the region fills. A number that binding does not get to be a point estimate. The multiplier $m$ is drawn between 0.6 and 1.55 per path, so every result already prices the market being two-thirds or one-and-a-half times the estimate. Finally the calendar: a twelve-month seasonality shape from the revenue model, following the year's savings and spending events, normalised so a year sums to twelve, with a further 10% random monthly wobble per path.

---

## 8. Partners

### What a partner is worth

A B2B partner white-labels the product. Its yearly value is four numbers multiplied:

$$V = U \times a \times h \times f$$

Where:

- $U$ is the partner's user base, 900,000 at base
- $a$ is the share of those users who adopt the product, 6%
- $h$ is the average gold value an adopter holds, USD 350
- $f$ is the platform fee on the total, 0.75% a year

At base: $900{,}000 \times 0.06 \times 350 \times 0.0075 =$ **USD 141,750 per partner per year**. All four numbers carry Aggressive and Conservative ranges in the revenue model and all four are drawn per path. On top of the world's draw, each partner that signs gets a personal size factor with mean one, applied to its combined gold under management, so a book can hold one whale and three minnows around the same average. Whether a big partner is big through more users or keener ones is not separated: the fee only ever sees the product.

A signed partner does not arrive at full power: its users adopt over time. Revenue climbs linearly to full over a ramp of about 18 months, drawn between 12 and 24 per path. The monthly stream is then each signed partner's gold under management, scaled by how far through its ramp it is:

$$s_{6,t} = \sum_{i\,\text{signed}} \text{AUM}_i \times \min\!\left(1,\ \tfrac{t - t_i + 1}{\text{ramp}}\right) \times \frac{f}{12}$$

where $t_i$ is partner $i$'s signing month. The ramp matters more than it looks: the funding trough falls exactly when the first partners are mid-ramp, so assuming instant adoption would understate the raise.

### How partners arrive

The plan says eleven partners by year seven: cumulative targets of 0, 1, 3, 5, 7, 9, 11 by year end. In the twin they arrive as discrete signings, not a straight line. For each year $y$ with $\Delta_y$ planned additions:

$$\text{signed}_y = \begin{cases} 0 & \text{with probability } 0.25 \quad \text{(a dead year)} \\ \text{Poisson}\!\left(\Delta_y / 0.75\right) & \text{with probability } 0.75 \end{cases}$$

The Poisson mean is grossed up by the dead-year odds, so the expected signings equal the plan: $\mathbb{E}[\text{signed}_y] = \Delta_y$. Dead years and clusters widen the range of outcomes without quietly moving the middle. Doubting the plan itself would be an assumption, and assumptions get declared, not hidden inside noise.

Once signed, a partner's fee runs every month from its signing month.

---

## 9. Gold and the float

### The price

One gold price for the whole system, following geometric Brownian motion:

$$S_{t+1} = S_t \exp\!\left[\left(\mu - \tfrac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\; \varepsilon_t\right], \qquad \varepsilon_t \sim \mathcal{N}(0,1)$$

Where:

- $\mu$ is the drift, 8.1% a year, the revenue model's own appreciation assumption
- $\sigma$ is volatility, 15% a year, the long-run realised figure for gold in USD, swept 10 to 22%
- $\Delta t$ is one month

Every part of the system reads this same path: purchases, the vault bill, collateral values, credit limits, the float.

### The float

Aurumix keeps a working inventory of gold so purchases settle instantly while replacement bars are in transit. Inside each path the requirement is one bar plus enough to cover a buffer of days at that month's actual purchase rate, with a two-bar minimum.

A separate daily study prices the policy properly, as a standard inventory problem: order up to a level $S$ covering expected demand over the delivery lead time plus a safety margin,

$$S = \mathbb{E}[\text{demand over lead time}] + z \cdot \sigma_d \sqrt{L} + \text{bar},$$

rounded up to whole bars, where $z$ sets the service level and $L$ is the lead time. It runs on the twin's own monthly purchase series, including paydays and seasonality, and prices carry cost and unhedged mark-to-market on the same gold paths.

---

## 10. Two thousand worlds

Each path is one version of the next seven years. What varies between paths, and how.

### Seventy-five drawn parameters

Every input the revenue model prices with an Aggressive and a Conservative value is drawn. The distribution is Beta-PERT: Base is the most likely value, and Aggressive and Conservative bracket the range,

$$x \sim \text{lo} + \text{Beta}(\alpha, \beta) \times (\text{hi} - \text{lo}), \qquad \alpha = 1 + 4\tfrac{\text{mode} - \text{lo}}{\text{hi} - \text{lo}}, \quad \beta = 1 + 4\tfrac{\text{hi} - \text{mode}}{\text{hi} - \text{lo}}$$

This grounds every draw in the revenue model's own scenario table rather than in invented spreads. The rule is opt-out, not opt-in: any input with a priced range is drawn, so the raise number carries it. Eleven parameters are excluded, each with a written reason in the code, in three groups:

- **replaced by structure**: the partner count (a discrete arrival process now), the gold band (the price process carries it)
- **derived**: quantities recomputed from their drawn components each path, so they move with their inputs
- **superseded by behaviour**: the workbook's blended loyalty rates and "share who ever tier". The twin prices each customer at their own tier, so a blended rate has nothing left to describe.

Three Phase 5 parameters have no workbook row and carry their own declared bands: the market ceiling multiplier (0.6 to 1.55), the channel-exhaustion strength (0.15 to 0.60), and the partner adoption ramp (12 to 24 months).

### And per path

A fresh gold path, a fresh partner history, a fresh demand wobble, and a full rerun of the population: who arrives, who pays, who gates, who refers, who leaves. Nothing is reused between paths except the fixed seeds that make every result reproducible.

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

The funding line itself is monthly: cumulative losses plus the capital tied up in the float, card prefunding and regulatory capital, with the raise sized off its deepest point. The results document carries the numbers. This document stops at how they are produced.

---

## 12. What it takes to be profitable

The profitability question is a threshold, and it is computed at steady state, where the book is flat and acquisition only replaces the customers who leave.

$$N^* = \frac{F_c + k F_u}{r - \left(v_c + k\,v_u\right)} \qquad\qquad K^* = \frac{F_c + k F_u}{A \cdot f}$$

Where:

- $N^*$ is paying customers needed for retail to stand alone, $K^*$ is B2B partners needed to cover the fixed base by themselves
- $r$ is retail revenue per paying customer per year, taken from the twin's own mature book, so it already reflects missed months
- $v_c$ and $v_u$ are the per-customer costs, split by whether they can surprise us
- $F_c$ and $F_u$ are the yearly fixed costs, split the same way
- $A$ is assets under management per partner, $f$ the platform fee
- $k$ is the contingency multiplier, reported at 1.15, 1.30 and 1.50

Per-customer costs include each customer's share of replacing the ones who leave: annual churn, measured from the twin's own mature book, times the cost of winning a replacement.

### Why contingency lands on only half the costs

Contingency is a buffer against costs nobody has thought of. Applying it to every line, as a flat percentage of the whole cost base, prices doubt about things nobody doubts. So each cost is classified once:

| | Certain, no buffer | Uncertain, buffered |
|:--|:--|:--|
| **Per customer** | fabrication premium, vault fee, KYC checks, redemption handling, loyalty giveback, agent commission, referral rewards | marketing to replace leavers, card programme |
| **Fixed** | VARA and DMCC licences | technology build and maintenance, insurance, audits |

The logic is simple. A contracted premium, a published licence fee, a vendor's price per identity check and a ladder Aurumix sets itself are known. A marketing yield, a card scheme's fees, and what technology and insurance really cost are not.

This matters more than it sounds: buffering the certain half as well was moving the retail threshold by roughly a hundred thousand customers on nothing.

It also concentrates the uncertainty where it belongs. Marketing is about 92% of the cost of winning a customer, so once the certain lines are excluded, sweeping contingency is very nearly a sensitivity test on cost per acquired customer alone.

One reclassification came out of this. The vault contract has a daily minimum, but at this book size the minimum does not bind: the bill is the percentage fee on metal held, which rises with the book. The vault is a per-customer cost, not a fixed one.

The two thresholds are reported separately and never blended, because blending them would hide whether the retail business stands alone. A threshold larger than every reachable customer in all three regions is reported as beyond the market rather than as a number, because such a number invites someone to treat it as a target. The values, and the levers that move them, are the results document's job.

---

## 13. Stress tests

Seven deliberate bad days. Each is a named scenario run through the full twin with everything else held at base, so the damage is attributable. What each one is, and how the twin models it:

| Scenario | What happens | How it is modelled |
|:--|:--|:--|
| Gold crash | the gold price falls 30% and stays there | the GBM path is replaced by a step: down 30% at month 24 |
| Redemption run | a quarter of custody leaves at once | a one-month jump redeems 25% of holdings at month 24; for six months payment odds drop to 40% of normal; excess metal beyond what new purchases absorb is sold back at a 1% spread |
| No B2B | no partner ever signs | the partner schedule is zeroed for all seven years |
| Adoption failure | the product lands badly everywhere | persistency at 45%, every acquisition cost at its Conservative value, tier take-up compressed |
| Regulatory delay | the licence takes a year longer | revenue and growth spend shift right twelve months; the standing costs of existing (licences, insurance, audits, the technology build) keep running |
| Ticket compression | customers save less than planned | regional average tickets cut to USD 26.50 / 21 / 24, refitting each ticket curve against the USD 20 floor |
| Combined tail | run + crash + weak B2B together | the redemption run and gold crash at month 24, on a partner schedule cut roughly in half |

Two modelling notes. A redemption run is a jump, not a rate: a rate-based outflow converges toward balance with inflows and can never overshoot, so it cannot represent a run. And a customer pause is a payment-odds event, not a ticket cut: tickets cannot fall below the USD 20 floor, so "saving less for a while" means skipping months.

---

## 14. How we know it is not lying

### Reconciliation against the revenue model

The twin is deliberately not a copy of the spreadsheet, so it is not tested by matching it. It is tested by explanation: every year-seven line, twin against revenue model, with the cause of every difference written down and bounded. If a difference appears whose cause is not on record, the check fails and the work stops until it is either a documented insight or a fixed bug. Differences have exactly two legitimate sources: behaviour the spreadsheet cannot represent, and declared assumption changes.

### The standing audit

Twenty-seven checks run after every change to the model. Among them: every priced range reaches the Monte Carlo; the giveback vanishes if the ladder is flattened, proving it is priced from real tiers; drawing persistency moves the book; peak funding is the true maximum of the monthly cash line; every parameter the engine reads exists. Each check exists because the defect it catches is the kind that never announces itself.

### Verification is not validation

All of this proves the code does what this document says. None of it proves the assumptions are right. Nothing can, until there are customers. That is why the deliverable is a threshold and a spread, not a forecast.

---
