---
brand: Tokenomics.net
type: simulation-results
source: template
created: 2026-09-03
---

# Aurumix gold savings simulation: results

**Prepared by**: Tokenomics.net
**Date**: September 2026

---

## Part 1: The question

### Executive summary

**Bottom line: the business works, but not the way the plan describes it. It is a B2B platform whose retail book is the product partners sell. Retail alone does not cover its own fixed costs at any plausible size, and three configuration changes are worth about USD 1.18m off the raise.**

The simulation ran 2,000 versions of the next seven years, each one a full rerun of every customer, month by month, at one agent per customer.

| Metric | Plan as modelled | With the three changes |
|:--|--:|--:|
| Raise needed, 9 paths in 10 | **USD 4.82m** | **USD 3.64m** |
| Raise needed, median path | USD 3.23m | USD 2.67m |
| Odds of clearing the hole by year 7 | **43%** | **65%** |
| Year-seven profit, median | USD 0.69m | USD 0.73m |
| Year-seven profit, worst tenth | -USD 0.19m | -USD 0.16m |
| Paying customers at month 84, median | 88,594 | 85,783 |

Three findings drive everything else.

**Partners are the business.** They are 31% of year-seven revenue and the top of every sensitivity ranking. Remove them and the seven years lose -USD 4.17m and need USD 5.74m of funding.

**Retail does not stand alone.** At a 15% contingency the retail book would need 146,289 paying customers to cover the fixed base by itself, against the 88,594 the plan builds. At 30% and above, the margin per customer goes negative and no book size fixes it.

**Gold is not the risk.** A 30% crash leaves cumulative profit at -USD 0.05m against a base of -USD 0.05m. Customers own the gold; Aurumix earns fees on flows.

### The question

There is one question, asked twice.

**What has to be true for this business to work?** Once under everything we can put a number on, and once under a specific named failure we cannot.

Two things people expect to be separate questions are consequences of that one.

**The money** follows from the conditions: the raise is the depth of the hole you dig on the way to meeting them, so it moves when they move. Part 2 gives the number and shows what it does as the conditions shift.

**The giveback** is not a client-facing question at all. The loyalty ladder costs 6 to 7% of revenue across its entire design range, so it is affordable everywhere and never decides viability. It is an internal pricing decision against a profit target, and the appendix carries the numbers.

The setup document describes how the simulation answers all of this. This document is the answers.

---

## Part 2: What has to be true, under priced uncertainty

### The map

Two things decide whether this works, and only two are both decision-relevant and genuinely unknown: what a customer costs to acquire, and how many partners sign. Everything else is either a decision Aurumix makes, and so priced as a lever in Part 4, or a figure already anchored.

![The conditions map](aurumix/outputs/charts/conditions_map.png)

Read it as a specification, not a menu. Cumulative profit at year seven, with the plan's own position marked.

**The plan sits exactly on the frontier.** At today's assumed acquisition cost it needs 11 partners, and it plans for 11. That lands at USD 0.17m: positive by a rounding error, with no margin for anything going wrong.

Move either axis and the requirement moves hard:

| Cost per customer | Partners needed to clear |
|:--|:--|
| 36 in the UAE, the good end of our band | 8 |
| 54, as assumed | 11 |
| 64, a 17% overrun | 14 |
| 91, the bad end of our band | does not clear at any partner count tested |

A 17% overrun on acquisition costs three more partners. That is the sensitivity the business actually lives on.

### Only one region pays for itself

The blended acquisition cost of about USD 44 is an average of roughly USD 74 in the UAE and USD 13 in India. It describes no actual customer, and averaging the two hid the most useful fact in the engagement.

![Regional economics](aurumix/outputs/charts/regional_economics.png)

| | Revenue per customer | Margin | CAC | Customers needed | Plan builds |
|:--|--:|--:|--:|:--|--:|
| UAE | 32.80 | **-10.48** | 74 | never clears | 31,050 |
| Oman and Bahrain | 28.75 | **-9.20** | 57 | never clears | 9,800 |
| **India** | 32.39 | **+14.92** | 13 | **23,475** | **48,240** |

**India alone covers the whole company's fixed base with 23,475 customers.** The plan already builds 48,240 there.

The UAE and the Gulf lose money on every customer they acquire. In the UAE, replacing leavers eats USD 27 of USD 32.80 in revenue before anything else is paid for.

Revenue per customer is nearly identical across all three. The entire difference is acquisition, and it is two things at once.

Paid reach is cheaper in India. And the whole 420-strong agent network sits there, where a customer costs a commission instead of a marketing budget.

That is the finding that should change the plan, and Part 4 acts on it.

### Why retail cannot carry the fixed costs

Strip out partners and ask a simple question: at a mature, standing-still book, does one paying customer make money?

![Retail alone](aurumix/outputs/charts/threshold_retail_alone.png)

At a 15% contingency, one customer contributes about **USD 2.39 a year** after serving them and after replacing the customers who leave. Covering the fixed base needs **146,289 paying customers**. The plan builds 88,594.

The costs behind that number are split by whether they can surprise us, and the contingency buffer lands only on the uncertain half:

| | Certain | Uncertain, buffered |
|:--|--:|--:|
| Per customer per year | USD 11.41 | USD 15.95 |
| Fixed per year | USD 114,436 | USD 205,000 |

Contracted rates, published licence fees, a vendor's price per identity check and a loyalty ladder Aurumix sets itself are known, so they carry no buffer. Marketing yield, card scheme fees, technology and insurance are not, so they do.

Raise the contingency on that uncertain half and the answer stops existing. At 30% the margin per customer is nearly gone and the requirement passes every reachable customer in all three regions: **beyond the addressable market**. At 50% the margin turns negative, so no number of customers works at all.

Marketing is 92% of what it costs to win a customer. So this sweep is really a test of one number: acquisition cost.

**Or 2.5 partners cover the fixed base by themselves.**

That contrast is the finding. A partner's fee arrives almost whole; a retail customer's revenue survives serving cost and replacement cost first, and what remains is small. The two thresholds are never blended, because blending them hides whether the retail leg stands.

### Why the margin is so thin: real customers skip months

The revenue model's paying customers pay every month by construction. The simulation's do not: three of the five payment behaviours miss months on purpose, and the book ends up paying in about **78% of the months it could**.

The effect is direct. Revenue per paying customer falls from roughly $38 a year to **$32**, while serving and replacement costs do not fall at all. That single correction is most of the distance between "retail needs 65,000 customers" and "retail needs 146,289".

### Why the raise is so large: partners arrive slowly

A signed partner does not deliver its users overnight. Modelling adoption as a 12-to-24-month ramp rather than an instant switch moved the deepest cash moment later, into the window where the first partners are signed but not yet contributing.

![The funding line](aurumix/outputs/charts/funding_line.png)

The consequence is a materially larger raise than an instant-adoption model would show. It is also the most actionable finding in the document: anything that shortens the ramp is worth more than most product levers.

---

### The raise

![Peak funding](aurumix/outputs/charts/peak_funding_hist.png)

| Confidence | Raise needed |
|:--|--:|
| Median path | USD 3.23m |
| 8 paths in 10 | USD 4.22m |
| **9 paths in 10** | **USD 4.82m** |
| 19 paths in 20 | USD 5.30m |

61% of paths need more than $3m. The number is the deepest point of a monthly cash line, not a year-end figure: cumulative losses plus the capital locked in the gold float, card prefunding and regulatory capital.

**One caveat, and it matters.** In 11.5% of paths the funding line is still rising at month 84. Those paths have not reached their peak inside the seven years, so for them the figure above is a floor, not a ceiling. They are the paths short of partners, and their median raise is already USD 5.03m against USD 3.11m for paths that turn the corner in time. Read the raise as the money needed to reach the point where the business funds itself. A fifth of futures do not reach that point inside seven years.

### Getting to profit

![Break-even by year](aurumix/outputs/charts/breakeven_by_year.png)

| Milestone | Share of paths in cumulative profit |
|:--|--:|
| By year 4 | 2% |
| By year 5 | 12% |
| By year 6 | 28% |
| By year 7 | **43%** |

![Cumulative profit](aurumix/outputs/charts/cum_profit_fan.png)

The shape matters as much as the odds, and the shape is sobering. The median path digs a hole until about month 52, then climbs. It does not finish the climb. Cumulative profit at month 84 sits at **-USD 0.45m**. Among the paths that do clear, the crossing happens around month 68, deep into year six.

So the honest reading of the plan as modelled is not "profitable in year seven". It is "roughly a third of futures have repaid the hole by year seven, and the rest are still climbing out". That is what the three changes in Part 4 are for.

### Where revenue comes from

![Revenue with and without partners](aurumix/outputs/charts/revenue_fan_with_without_b2b.png)

Year-seven revenue runs USD 4.26m at the median, of which USD 2.93m is retail. Partners are **31%** of the total from a handful of contracts.

![Partner dependence](aurumix/outputs/charts/partner_dependence.png)

Profit tracks the partner count almost linearly. This is the single most important relationship in the model, and it rests on the fewest verified facts.

### What the answer depends on

![Tornado](aurumix/outputs/charts/tornado.png)

| Rank | Assumption | Swing in year-seven profit |
|:--|:--|--:|
| 1 | partner adopt | USD 1.57m |
| 2 | partner aum user | USD 1.07m |
| 3 | facility takeup | USD 0.82m |
| 4 | ceiling mult | USD 0.79m |
| 5 | b2b fee | USD 0.72m |

Partner assumptions occupy the top of this list. None of them is measured. One signed letter of intent, with a real user count and a real adoption rate, would narrow this model more than any further modelling work.

---

## Part 3: What has to be true, under a named failure

Part 2 asked what must hold across everything we can put a number on. This part asks the other half: what happens when a specific thing goes wrong that sits outside every band, and whether money can fix it.

Each scenario runs through the full simulation on its own, with everything else at base, so the damage is attributable.

### Stress tests

![Stress scenarios](aurumix/outputs/charts/stress_scenarios.png)

| Scenario | Cumulative profit at year 7 | Peak funding |
|:--|--:|--:|
| Base | -USD 0.05m | USD 2.87m |
| Gold crashes 30% | -USD 0.05m | USD 2.86m |
| Redemption run, 25% at month 24 | -USD 0.12m | USD 2.89m |
| **No partners at all** | **-USD 4.17m** | **USD 5.74m** |
| Adoption failure | -USD 0.90m | USD 3.06m |
| Regulatory delay, 12 months | -USD 0.74m | USD 3.56m |
| Ticket compression | -USD 0.42m | USD 2.90m |
| Combined tail | -USD 2.50m | USD 4.08m |

### What each failure would take to survive

A table of damage is not an answer. The useful question is the same one Part 2 asked: what would have to be true to still work, and can money buy it?

| Scenario | Verdict | What it would take |
|:--|:--|:--|
| Gold crashes 30% | **Not a risk** | nothing. Customers hold the price exposure; Aurumix earns fees on flows |
| Redemption run | **Fundable** | already inside the planned raise. Needs operational readiness, not capital |
| Ticket compression | **Fundable** | already inside the planned raise |
| Regulatory delay | **Fundable** | about USD 0.4m more, to cover twelve months of standing costs while unlicensed |
| Adoption failure | **Fundable, barely** | survives on the planned raise but never repays. Needs the Part 4 levers to recover |
| **No partners at all** | **Not fundable** | retail alone would need more customers than exist in all three markets. No raise fixes this |
| Combined tail | **Not fundable** | the no-partner case with worse timing |

Three readings follow.

**Gold is not the risk.** The crash scenario is almost indistinguishable from base.

**Partners are the whole risk, and the only one money cannot solve.** Their absence costs -USD 4.17m over seven years and pushes funding to USD 5.74m.

But the number is not the point. No amount of funding turns a partnerless business into a viable one. Every other scenario here is a cash problem. This one is a business-model problem.

**A run is survivable.** Cumulative profit falls to -USD 0.12m and funding rises only to USD 2.89m. The gold is allocated and already owned, so a run is an operational and cash-timing event rather than a solvency one. The credit book stays quiet throughout. The chance of ever needing a collateral top-up is **4.1%**, because loans are secured against gold that moves with the price the loan is measured in.

---

## Part 4: What to do

### What the three changes are worth

Same 2,000 worlds, same dice, only the configuration moved.

![Plan versus recommended](aurumix/outputs/charts/plan_vs_recommended.png)

| | Plan | Recommended |
|:--|--:|--:|
| Raise, 9 in 10 | USD 4.82m | **USD 3.64m** |
| Break-even by year 7 | 43% | **65%** |
| Year-seven profit, median | USD 0.69m | USD 0.73m |
| Year-seven profit, worst tenth | -USD 0.19m | -USD 0.16m |
| Cumulative profit at year 7, median | | USD 0.95m |

### Recommendations

#### 1. Trim the loyalty ladder to a 1.5-point ceiling, back-loaded

The top tier pays 3.5% entry rather than 3.0%, and the benefits concentrate near the top instead of stepping evenly. This is the largest single lever. A harsher 1.0-point ceiling was tested. It buys almost nothing more, and costs real ground in the middle of the ladder.

#### 2. Push the standing-instruction rail toward 75% of joiners

Customers on autopay miss fewer months and reach tiers faster. The gated share rises from 50.6% to 59.1%, and the paying book from 85,110 to 96,190. One caveat: the model prices the benefit and carries no cost for winning that adoption, because none is known.

#### 3. Move marketing from 74/18/8 to 50/15/35 across the regions

The current split concentrates spend in the smallest and dearest market. The reallocation holds up across the full range of market-size assumptions, so it does not depend on the funnel being right.

### What to learn first

Nothing here is measured. So the most valuable thing the model can do is rank what is worth finding out: how much each answer moves the result, against what it costs to buy.

| Learn it | Moves year-seven profit | What it takes |
|:--|--:|:--|
| Card take-up | USD 0.82m | offer the card to the first cohort |
| The B2B fee | USD 0.72m | a term sheet |
| Family attach | USD 0.47m | offer it to the first cohort |
| Partner adoption and size | USD 1.57m | one signed partner, or a serious pilot |
| Cost per customer | USD 0.25m | a paid test campaign in one region, 6 to 8 weeks |

**Four of the top assumptions are knowable today, not through research but by reading documents you already have.** The vault fee is in the contract. Interchange and ATM rates are in the card scheme's own schedule. Those alone account for USD 0.89m of profit swing that the model currently carries as uncertainty because nobody has looked them up.

The most valuable single thing remains one signed partner, which resolves the largest uncertainty in the model and costs one conversation rather than a budget.

### When to change your mind

A threshold is only useful if you know the level at which it fires.

| Watch | Today | The line | What crossing it means |
|:--|--:|--:|:--|
| UAE cost per customer | USD 74.19 | USD 58.58 | below it, the UAE pays for itself; above, every UAE customer is a loss |
| Gulf cost per customer | USD 56.99 | none in range | the Gulf loses money at any reach price tested. Its problem is not the price of reach |
| India | agent-led | not a marketing number | margin moves USD 1.03 across a fourfold change in the marketing rate. Watch agent productivity instead |
| Partners signed by year 7 | plan says 11 | 11 | below it, the plan does not clear at today's acquisition cost |

The India line is the one to internalise. **Two of these are marketing businesses. One is a distribution business.** They need different dashboards, and a single blended cost per customer hides which is which.

One metric was tested as a trigger and rejected. Payment discipline moves the margin by only USD 1.02 across its whole plausible range, because costs are per customer rather than per payment. It is worth watching as a health signal, but it will not flip a decision.

### What would change the answer most

**Sign one partner.** Not for the revenue: for the information. Partner assumptions are the top of the sensitivity table and none of them is measured. A real user base, a real adoption rate and a real ramp would collapse most of the uncertainty in this document.

**Shorten the adoption ramp.** The raise is set while early partners are still warming up. Launching inside a partner's existing app, or pre-committing distribution at signing, attacks the funding need directly.

**Watch payment discipline from month one.** The share of months actually paid is what the retail economics live on, and today it is a modelled assumption. Two months of launch will make it an observation.

### What to monitor

| Metric | Why it matters | Warning level |
|:--|:--|:--|
| Partners signed against plan | the business case | behind plan at month 24 |
| Months paid as a share of months due | retail unit economics | below 70% |
| Share reaching a tier | the giveback's cost and the loyalty promise | below 40% by month 36 |
| Cost per acquired customer | rises as channels exhaust | above $60 blended |
| Cumulative cash against the funding line | the raise | tracking below the median path |

---

## Part 5: Appendix

### A. What was simulated

| | |
|:--|:--|
| Paths | 2,000 |
| Resolution | one agent per customer |
| Horizon | 84 months, monthly steps, starting January 2027 |
| Drawn inputs per path | 75 parameters, plus a gold path and a partner history |
| Randomness | fixed seeds; every result reproduces exactly |

### B. How to read the numbers

**Raise at 9 in 10** is the deepest point of the monthly funding line, at the 90th percentile across paths. It covers cumulative losses plus capital locked in the float, card prefunding and regulatory capital.

**Break-even by year 7** is the share of paths whose cumulative profit is positive at month 84. It is not a statement about a single year's profit.

**Retail customers needed** is a steady-state threshold: the book is flat, and acquisition only replaces the customers who leave. It answers what the business must reach, not what it will reach.

**Percentiles** describe the spread across paths, not confidence in the model. A p90 raise means nine of ten simulated futures survived on that money, given the assumptions.

### C. The loyalty ladder, and what it costs

By month 84, **53.4%** of the live book has cleared six consecutive payments and holds a tier. Within that group:

| Tier | Share of tiered customers |
|:--|--:|
| Silver | 40.4% |
| Gold | 43.9% |
| Platinum | 14.3% |
| Sovereign | 1.4% |

![Tier mix](aurumix/outputs/charts/tier_mix_over_time.png)

Sovereign requires a five-year payment record and a near-perfect recent year at the same time. Almost nobody clears it inside seven years, which is what makes it cheap to offer and meaningful to hold.

Priced at each customer's own tier, the giveback costs between **5.1%** and **16.8%** of revenue depending on how generous the ladder is. That answers the second question. The ladder is affordable across its whole design range, and its cost is not what decides whether the business works.

### D. Where the profit sits

![Profit by ticket decile](aurumix/outputs/charts/profit_by_ticket_decile.png)

The top tenth of customers by monthly saving contributes **16.3%** of lifetime profit; the top three deciles contribute 38.6%; the bottom half contributes 41.3%. A minority of the book carries the economics, which is normal for a savings product and matters for how acquisition is targeted.

### E. What the model cannot tell you

The simulation prices uncertainty that has been written down. It cannot price what has not.

- **No customer data exists.** Payment behaviour, ticket sizes and the market funnel are structured assumptions, swept across ranges rather than measured.
- **No partner is signed.** The entire partner block rests on four unverified numbers.
- **The marketing budget never flexes.** A real company cuts spend when cash runs short; the model spends the plan on every path, which overstates the burn on bad paths. That is the conservative direction for a raise.
- **Verification is not validation.** Standing checks prove the code does what the setup document says. Nothing proves the assumptions are right until there are customers.

---
