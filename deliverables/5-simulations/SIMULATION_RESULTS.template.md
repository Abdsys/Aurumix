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

**Bottom line: the business works, but not the way the plan describes it. It is a B2B platform whose retail book is the product partners sell. Retail alone does not cover its own fixed costs at any plausible size, and three configuration changes are worth about {{RAISE_SAVED}} off the raise.**

The simulation ran {{PATHS}} versions of the next seven years, each one a full rerun of every customer, month by month, at {{AGENTS}}.

| Metric | Plan as modelled | With the three changes |
|:--|--:|--:|
| Raise needed, 9 paths in 10 | **{{RAISE90}}** | **{{R_RAISE90}}** |
| Raise needed, median path | {{RAISE50}} | {{R_RAISE50}} |
| Odds of clearing the hole by year 7 | **{{BE7}}** | **{{R_BE7}}** |
| Year-seven profit, median | {{NP50}} | {{R_NP50}} |
| Year-seven profit, worst tenth | {{NP10}} | {{R_NP10}} |
| Paying customers at month 84, median | {{PAY50}} | {{R_PAY50}} |

Three findings drive everything else.

**Partners are the business.** They are {{B2B_SHARE}} of year-seven revenue and the top of every sensitivity ranking. Remove them and the seven years lose {{ST_NOB2B_CUM}} and need {{ST_NOB2B_PK}} of funding.

**Retail does not stand alone.** At a 15% contingency the retail book would need {{NEED15}} paying customers to cover the fixed base by itself, against the {{PAY50}} the plan builds. At 30% and above, the margin per customer goes negative and no book size fixes it.

**Gold is not the risk.** A 30% crash leaves cumulative profit at {{ST_GOLD_CUM}} against a base of {{ST_BASE_CUM}}. Customers own the gold; Aurumix earns fees on flows.

### The three questions

1. What has to be true for this business to be profitable?
2. How much can Aurumix afford to give back to loyal customers?
3. How much must be raised to still be standing in nine paths out of ten?

The setup document describes how the simulation answers them. This document is the answers.

---

## Part 2: What the simulation found

### Finding 1: the retail book cannot carry the fixed costs

Strip out partners and ask a simple question: at a mature, standing-still book, does one paying customer make money?

![Retail alone](aurumix/outputs/charts/threshold_retail_alone.png)

At a 15% contingency, one customer contributes about **${{MARGIN15}} a year** after serving them and after replacing the customers who leave. The fixed base is roughly $410,000 a year, so covering it needs **{{NEED15}} paying customers**. The plan builds {{PAY50}}.

Raise the contingency and the answer stops existing. At 30% the margin per customer turns negative, which means no number of customers covers the fixed base: {{NEED30}}. At 50%, the same.

**Or {{PARTNERS15}} partners cover the fixed base by themselves.**

That contrast is the finding. A partner's fee arrives almost whole; a retail customer's revenue survives serving cost and replacement cost first, and what remains is small. The two thresholds are never blended, because blending them hides whether the retail leg stands.

### Finding 2: real customers skip months, and that changes the unit economics

The revenue model's paying customers pay every month by construction. The simulation's do not: three of the five payment behaviours miss months on purpose, and the book ends up paying in about **78% of the months it could**.

The effect is direct. Revenue per paying customer falls from roughly $38 a year to **$32**, while serving and replacement costs do not fall at all. That single correction is most of the distance between "retail needs 65,000 customers" and "retail needs {{NEED15}}".

### Finding 3: partners arrive slowly, and the raise is set while they are still ramping

A signed partner does not deliver its users overnight. Modelling adoption as a 12-to-24-month ramp rather than an instant switch moved the deepest cash moment later, into the window where the first partners are signed but not yet contributing.

![The funding line](aurumix/outputs/charts/funding_line.png)

The consequence is a materially larger raise than an instant-adoption model would show. It is also the most actionable finding in the document: anything that shortens the ramp is worth more than most product levers.

---

## Part 3: The results

### The raise

![Peak funding](aurumix/outputs/charts/peak_funding_hist.png)

| Confidence | Raise needed |
|:--|--:|
| Median path | {{RAISE50}} |
| 8 paths in 10 | {{RAISE80}} |
| **9 paths in 10** | **{{RAISE90}}** |
| 19 paths in 20 | {{RAISE95}} |

{{P_GT3M}} of paths need more than $3m. The number is the deepest point of a monthly cash line, not a year-end figure: cumulative losses plus the capital locked in the gold float, card prefunding and regulatory capital.

**One caveat, and it matters.** In {{PEAK_AT_HORIZON}} of paths the funding line is still rising at month 84. Those paths have not reached their peak inside the seven years, so for them the figure above is a floor, not a ceiling. They are the paths short of partners, and their median raise is already {{RAISE_IF_LATE}} against {{RAISE_IF_EARLY}} for paths that turn the corner in time. Read the raise as the money needed to reach the point where the business funds itself, and note that a fifth of futures do not reach that point within the horizon.

### Getting to profit

![Break-even by year](aurumix/outputs/charts/breakeven_by_year.png)

| Milestone | Share of paths in cumulative profit |
|:--|--:|
| By year 4 | {{BE4}} |
| By year 5 | {{BE5}} |
| By year 6 | {{BE6}} |
| By year 7 | **{{BE7}}** |

![Cumulative profit](aurumix/outputs/charts/cum_profit_fan.png)

The shape matters as much as the odds, and the shape is sobering. The median path digs a hole until about month {{PEAK_MONTH_MED}}, then climbs, but it does not finish the climb: cumulative profit at month 84 sits at **{{CUM_M84_MED}}** on the median path. Among the paths that do clear, the crossing happens around month {{BE_MONTH_MED}}, deep into year six.

So the honest reading of the plan as modelled is not "profitable in year seven". It is "roughly a third of futures have repaid the hole by year seven, and the rest are still climbing out". That is what the three changes in Part 4 are for.

### Where revenue comes from

![Revenue with and without partners](aurumix/outputs/charts/revenue_fan_with_without_b2b.png)

Year-seven revenue runs {{REV50}} at the median, of which {{REV_EX_B2B}} is retail. Partners are **{{B2B_SHARE}}** of the total from a handful of contracts.

![Partner dependence](aurumix/outputs/charts/partner_dependence.png)

Profit tracks the partner count almost linearly. This is the single most important relationship in the model, and it rests on the fewest verified facts.

### The loyalty ladder

By month 84, **{{GATED}}** of the live book has cleared six consecutive payments and holds a tier. Within that group:

| Tier | Share of tiered customers |
|:--|--:|
| Silver | {{T_SILVER}} |
| Gold | {{T_GOLD}} |
| Platinum | {{T_PLAT}} |
| Sovereign | {{T_SOV}} |

![Tier mix](aurumix/outputs/charts/tier_mix_over_time.png)

Sovereign requires a five-year payment record and a near-perfect recent year at the same time. Almost nobody clears it inside seven years, which is what makes it cheap to offer and meaningful to hold.

Priced at each customer's own tier, the giveback costs between **{{GIVE_LO}}** and **{{GIVE_HI}}** of revenue depending on how generous the ladder is. That answers the second question. The ladder is affordable across its whole design range, and its cost is not what decides whether the business works.

### Who the profit comes from

![Profit by ticket decile](aurumix/outputs/charts/profit_by_ticket_decile.png)

The top tenth of customers by monthly saving contributes **{{DEC_TOP}}** of lifetime profit; the top three deciles contribute {{DEC_TOP3}}; the bottom half contributes {{DEC_BOT5}}. A minority of the book carries the economics, which is normal for a savings product and matters for how acquisition is targeted.

### What the answer depends on

![Tornado](aurumix/outputs/charts/tornado.png)

| Rank | Assumption | Swing in year-seven profit |
|:--|:--|--:|
| 1 | {{TOR1}} | {{TOR1_SW}} |
| 2 | {{TOR2}} | {{TOR2_SW}} |
| 3 | {{TOR3}} | {{TOR3_SW}} |
| 4 | {{TOR4}} | {{TOR4_SW}} |
| 5 | {{TOR5}} | {{TOR5_SW}} |

Partner assumptions occupy the top of this list. None of them is measured. One signed letter of intent, with a real user count and a real adoption rate, would narrow this model more than any further modelling work.

### Stress tests

![Stress scenarios](aurumix/outputs/charts/stress_scenarios.png)

| Scenario | Cumulative profit at year 7 | Peak funding |
|:--|--:|--:|
| Base | {{ST_BASE_CUM}} | {{ST_BASE_PK}} |
| Gold crashes 30% | {{ST_GOLD_CUM}} | {{ST_GOLD_PK}} |
| Redemption run, 25% at month 24 | {{ST_RUN_CUM}} | {{ST_RUN_PK}} |
| **No partners at all** | **{{ST_NOB2B_CUM}}** | **{{ST_NOB2B_PK}}** |
| Adoption failure | {{ST_ADOPT_CUM}} | {{ST_ADOPT_PK}} |
| Regulatory delay, 12 months | {{ST_DELAY_CUM}} | {{ST_DELAY_PK}} |
| Ticket compression | {{ST_TICKET_CUM}} | {{ST_TICKET_PK}} |
| Combined tail | {{ST_TAIL_CUM}} | {{ST_TAIL_PK}} |

Three readings.

**Gold is not the risk.** The crash scenario is almost indistinguishable from base. Customers hold the price exposure; Aurumix earns fees.

**Partners are the whole risk.** Their absence costs {{ST_NOB2B_CUM}} over seven years and pushes the funding need to {{ST_NOB2B_PK}}. No other single scenario comes close.

**A redemption run is survivable.** Cumulative profit falls to {{ST_RUN_CUM}} and funding rises only to {{ST_RUN_PK}}. The gold is allocated and already owned, so a run is an operational and cash-timing event, not a solvency one. The credit book stays quiet through all of this: the chance of ever needing a collateral top-up is **{{PMC}}**, because loans are secured against gold that rises with the same price the loan is measured in.

---

## Part 4: What to do

### What the three changes are worth

Same 2,000 worlds, same dice, only the configuration moved.

![Plan versus recommended](aurumix/outputs/charts/plan_vs_recommended.png)

| | Plan | Recommended |
|:--|--:|--:|
| Raise, 9 in 10 | {{RAISE90}} | **{{R_RAISE90}}** |
| Break-even by year 7 | {{BE7}} | **{{R_BE7}}** |
| Year-seven profit, median | {{NP50}} | {{R_NP50}} |
| Year-seven profit, worst tenth | {{NP10}} | {{R_NP10}} |
| Cumulative profit at year 7, median | | {{R_CUM50}} |

### Recommendations

#### 1. Trim the loyalty ladder to a 1.5-point ceiling, back-loaded

The top tier pays 3.5% entry rather than 3.0%, and the benefits concentrate near the top instead of stepping evenly. This is the largest single lever. A harsher 1.0-point ceiling was tested and buys very little more, at a real cost to the mid-ladder proposition.

#### 2. Push the standing-instruction rail toward 75% of joiners

Customers on autopay miss fewer months and reach tiers faster. The gated share rises from {{RAIL0_GATE}} to {{RAIL75_GATE}}, and the paying book from {{RAIL0_PAY}} to {{RAIL75_PAY}}. One caveat: the model prices the benefit and carries no cost for winning that adoption, because none is known.

#### 3. Move marketing from 74/18/8 to 50/15/35 across the regions

The current split concentrates spend in the smallest and dearest market. The reallocation holds up across the full range of market-size assumptions, so it does not depend on the funnel being right.

### What would change the answer most

**Sign one partner.** Not for the revenue: for the information. Partner assumptions are the top of the sensitivity table and none of them is measured. A real user base, a real adoption rate and a real ramp would collapse most of the uncertainty in this document.

**Shorten the adoption ramp.** The raise is set while early partners are still warming up. Launching inside a partner's existing app, or pre-committing distribution at signing, attacks the funding need directly.

**Watch payment discipline from month one.** The share of months actually paid is the number the retail economics live on, and it is currently a modelled assumption rather than an observation. It will be measurable within two months of launch.

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
| Paths | {{PATHS}} |
| Resolution | {{AGENTS}} |
| Horizon | 84 months, monthly steps, starting January 2027 |
| Drawn inputs per path | 75 parameters, plus a gold path and a partner history |
| Randomness | fixed seeds; every result reproduces exactly |

### B. How to read the numbers

**Raise at 9 in 10** is the deepest point of the monthly funding line, at the 90th percentile across paths. It covers cumulative losses plus capital locked in the float, card prefunding and regulatory capital.

**Break-even by year 7** is the share of paths whose cumulative profit is positive at month 84. It is not a statement about a single year's profit.

**Retail customers needed** is a steady-state threshold: the book is flat, and acquisition only replaces the customers who leave. It answers what the business must reach, not what it will reach.

**Percentiles** describe the spread across paths, not confidence in the model. A p90 raise means nine of ten simulated futures survived on that money, given the assumptions.

### C. What the model cannot tell you

The simulation prices uncertainty that has been written down. It cannot price what has not.

- **No customer data exists.** Payment behaviour, ticket sizes and the market funnel are structured assumptions, swept across ranges rather than measured.
- **No partner is signed.** The entire partner block rests on four unverified numbers.
- **The marketing budget never flexes.** A real company cuts spend when cash runs short; the model spends the plan on every path, which overstates the burn on bad paths. That is the conservative direction for a raise.
- **Verification is not validation.** Standing checks prove the code does what the setup document says. Nothing proves the assumptions are right until there are customers.

---
