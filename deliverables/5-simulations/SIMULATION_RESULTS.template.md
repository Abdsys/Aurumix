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

### The question

There is really one question, asked twice.

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

**The plan sits exactly on the frontier.** At today's assumed acquisition cost it needs {{FRONT_PLAN}} partners, and it plans for {{PLAN_PARTNERS}}. That lands at {{PLAN_CELL}} — positive by a rounding error, with no margin for anything going wrong.

Move either axis and the requirement moves hard:

| Cost per customer | Partners needed to clear |
|:--|:--|
| {{CAC_LO_UAE}} in the UAE, the good end of our band | {{FRONT_GOOD}} |
| 54, as assumed | {{FRONT_PLAN}} |
| 64, a 17% overrun | {{FRONT_BAD}} |
| {{CAC_HI_UAE}}, the bad end of our band | does not clear at any partner count tested |

A 17% overrun on acquisition costs three more partners. That is the sensitivity the business actually lives on.

### Only one region pays for itself

The blended acquisition cost of about USD 44 is an average of roughly USD {{UAE_CAC}} in the UAE and USD {{INDIA_CAC}} in India. It describes no actual customer, and averaging the two hid the most useful fact in the engagement.

![Regional economics](aurumix/outputs/charts/regional_economics.png)

| | Revenue per customer | Margin | CAC | Customers needed | Plan builds |
|:--|--:|--:|--:|:--|--:|
| UAE | {{UAE_REV}} | **{{UAE_MARGIN}}** | {{UAE_CAC}} | {{UAE_NEED}} | {{UAE_BUILDS}} |
| Oman and Bahrain | {{GULF_REV}} | **{{GULF_MARGIN}}** | {{GULF_CAC}} | {{GULF_NEED}} | {{GULF_BUILDS}} |
| **India** | {{INDIA_REV}} | **{{INDIA_MARGIN}}** | {{INDIA_CAC}} | **{{INDIA_NEED}}** | **{{INDIA_BUILDS}}** |

**India alone covers the whole company's fixed base with {{INDIA_NEED}} customers, and the plan already builds {{INDIA_BUILDS}} there.** The UAE and the Gulf lose money on every customer they acquire: in the UAE, replacing leavers alone eats USD 27 of USD {{UAE_REV}} in revenue.

Revenue per customer is nearly identical across all three. The entire difference is acquisition, and it is two things at once: cheaper paid reach, and the fact that the whole 420-strong agent network sits in India, where a customer costs a commission rather than a marketing budget.

That is the finding that should change the plan, and Part 4 acts on it.

### Why the retail book still cannot carry the fixed costs on its own

Strip out partners and ask a simple question: at a mature, standing-still book, does one paying customer make money?

![Retail alone](aurumix/outputs/charts/threshold_retail_alone.png)

At a 15% contingency, one customer contributes about **USD {{MARGIN15}} a year** after serving them and after replacing the customers who leave. Covering the fixed base needs **{{NEED15}} paying customers**. The plan builds {{PAY50}}.

The costs behind that number are split by whether they can surprise us, and the contingency buffer lands only on the uncertain half:

| | Certain | Uncertain, buffered |
|:--|--:|--:|
| Per customer per year | USD {{VAR_CERT}} | USD {{VAR_UNC}} |
| Fixed per year | {{FIX_CERT}} | {{FIX_UNC}} |

Contracted rates, published licence fees, a vendor's price per identity check and a loyalty ladder Aurumix sets itself are known, so they carry no buffer. Marketing yield, card scheme fees, technology and insurance are not, so they do.

Raise the contingency on that uncertain half and the answer stops existing. At 30% the margin per customer is nearly gone and the requirement passes every reachable customer in all three regions: **{{NEED30}}**. At 50% the margin turns negative, so no number of customers works at all.

Marketing is about 92% of the cost of winning a customer, so this sweep is very nearly a sensitivity on one number: what it costs to acquire.

**Or {{PARTNERS15}} partners cover the fixed base by themselves.**

That contrast is the finding. A partner's fee arrives almost whole; a retail customer's revenue survives serving cost and replacement cost first, and what remains is small. The two thresholds are never blended, because blending them hides whether the retail leg stands.

### Why the margin is so thin: real customers skip months

The revenue model's paying customers pay every month by construction. The simulation's do not: three of the five payment behaviours miss months on purpose, and the book ends up paying in about **78% of the months it could**.

The effect is direct. Revenue per paying customer falls from roughly $38 a year to **$32**, while serving and replacement costs do not fall at all. That single correction is most of the distance between "retail needs 65,000 customers" and "retail needs {{NEED15}}".

### Why the raise is so large: partners arrive slowly

A signed partner does not deliver its users overnight. Modelling adoption as a 12-to-24-month ramp rather than an instant switch moved the deepest cash moment later, into the window where the first partners are signed but not yet contributing.

![The funding line](aurumix/outputs/charts/funding_line.png)

The consequence is a materially larger raise than an instant-adoption model would show. It is also the most actionable finding in the document: anything that shortens the ramp is worth more than most product levers.

---

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

---

## Part 3: What has to be true, under a named failure

Part 2 asked what must hold across everything we can put a number on. This part asks the other half: what happens when a specific thing goes wrong that sits outside every band, and whether money can fix it.

Each scenario runs through the full simulation on its own, with everything else at base, so the damage is attributable.

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

**Partners are the whole risk, and it is the one risk money cannot solve.** Their absence costs {{ST_NOB2B_CUM}} over seven years and pushes funding to {{ST_NOB2B_PK}}, but the deeper point is that no amount of funding converts a partnerless business into a viable one. Every other scenario on this list is a cash problem. This one is a business-model problem.

**A run is survivable.** Cumulative profit falls to {{ST_RUN_CUM}} and funding rises only to {{ST_RUN_PK}}. The gold is allocated and already owned, so a run is an operational and cash-timing event rather than a solvency one. The credit book stays quiet throughout: the chance of ever needing a collateral top-up is **{{PMC}}**, because loans are secured against gold that moves with the same price the loan is measured in.

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

### What to learn first

Nothing here is measured. So the most valuable thing the model can do right now is rank what is worth finding out, by how much it moves the answer against what it costs to buy the answer.

| Learn it | Moves year-seven profit | What it takes |
|:--|--:|:--|
| Card take-up | {{VOI1_SW}} | offer the card to the first cohort |
| The B2B fee | {{VOI2_SW}} | a term sheet |
| Family attach | {{VOI3_SW}} | offer it to the first cohort |
| Partner adoption and size | {{VOI_PARTNER_SW}} | one signed partner, or a serious pilot |
| Cost per customer | {{VOI_CAC_SW}} | a paid test campaign in one region, 6 to 8 weeks |

**Four of the top assumptions are knowable today, not through research but by reading documents you already have.** The vault fee is in the contract. Interchange and ATM rates are in the card scheme's own schedule. Those alone account for {{VOI_FREE_SW}} of profit swing that the model currently carries as uncertainty because nobody has looked them up.

The most valuable single thing remains one signed partner, which resolves the largest uncertainty in the model and costs one conversation rather than a budget.

### When to change your mind

A threshold is only useful if you know the level at which it fires.

| Watch | Today | The line | What crossing it means |
|:--|--:|--:|:--|
| UAE cost per customer | USD {{TRIG_UAE_TODAY}} | USD {{TRIG_UAE}} | below it, the UAE pays for itself; above, every UAE customer is a loss |
| Gulf cost per customer | USD {{TRIG_GULF_TODAY}} | none in range | the Gulf loses money at any reach price tested. Its problem is not the price of reach |
| India | agent-led | not a marketing number | margin moves USD {{TRIG_INDIA_SWING}} across a fourfold change in the marketing rate. Watch agent productivity instead |
| Partners signed by year 7 | plan says {{PLAN_PARTNERS}} | {{FRONT_PLAN}} | below it, the plan does not clear at today's acquisition cost |

The India line is the one to internalise. **Two of these are marketing businesses and one is a distribution business.** They need different dashboards, and reporting a single blended cost per customer across all three hides which is which.

One metric was tested as a trigger and rejected. Payment discipline moves the margin by only USD {{TRIG_PAY_SPAN}} across its whole plausible range, because costs are per customer rather than per payment. It is worth watching as a health signal, but it will not flip a decision.

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

### C. The loyalty ladder, and what it costs

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

### D. Where the profit sits

![Profit by ticket decile](aurumix/outputs/charts/profit_by_ticket_decile.png)

The top tenth of customers by monthly saving contributes **{{DEC_TOP}}** of lifetime profit; the top three deciles contribute {{DEC_TOP3}}; the bottom half contributes {{DEC_BOT5}}. A minority of the book carries the economics, which is normal for a savings product and matters for how acquisition is targeted.

### E. What the model cannot tell you

The simulation prices uncertainty that has been written down. It cannot price what has not.

- **No customer data exists.** Payment behaviour, ticket sizes and the market funnel are structured assumptions, swept across ranges rather than measured.
- **No partner is signed.** The entire partner block rests on four unverified numbers.
- **The marketing budget never flexes.** A real company cuts spend when cash runs short; the model spends the plan on every path, which overstates the burn on bad paths. That is the conservative direction for a raise.
- **Verification is not validation.** Standing checks prove the code does what the setup document says. Nothing proves the assumptions are right until there are customers.

---
