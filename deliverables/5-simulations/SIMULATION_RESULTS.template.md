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

## Part 1: What the simulation says

### What we set out to answer

Two questions.

#### 1. What has to be true for this business to make money?

Nobody knows yet what a customer costs to win, how long they stay, how much they save, or what a partner is worth. Every one of those is a guess with a range around it.

So we did not ask what will happen. We asked what has to be true. We gave each unknown a range, ran all of them together {{PATHS}} times, and measured which combinations end up making money and which do not.

The answer comes back as conditions to hit, not as a forecast. Part 2 sets them out.

#### 2. What happens when something goes badly wrong?

The first question covers things we can put a range on. It does not cover a single disaster that sits outside every range.

No partner ever signs. The licence takes a year longer. A quarter of customers cash out in one month.

Each of those runs on its own, and each gets the same blunt test: **can more money fix it?** For most of them the answer is yes, and we say how much. For one it is no, and that is the most important sentence in this document. Part 3 sets them out.

#### Everything else follows from these

How much to raise, and how much to give loyal customers back, are not separate questions. They are answers to the first one. Change the conditions and both numbers move. We report them where they belong rather than treating them as findings of their own.

### The base case

These are the plan exactly as written, run {{PATHS}} times over seven years. Every figure is the middle of {{PATHS}} runs unless it says otherwise.

| | |
|:--|--:|
| **Money to raise, safe in 9 runs out of 10** | **{{RAISE90}}** |
| Money to raise, typical run | {{RAISE50}} |
| **Runs that earn it all back by year 7** | **{{BE7}}** |
| Profit in year 7, typical run | {{NP50}} |
| Profit in year 7, a bad run | {{NP10}} |
| Profit in year 7, a good run | {{NP90}} |
| Revenue in year 7, typical run | {{REV50}} |
| Paying customers at month 84 | {{PAY50}} |

Read the two bold rows together. **{{RAISE90}} keeps the business alive in nine runs out of ten. It does not make it profitable: only {{BE7}} of runs have earned that money back by year seven.**

Surviving and earning it back are different things, and the gap between them is the honest story of this plan.

### How much money you need

![Peak funding](aurumix/outputs/charts/peak_funding_hist.png)

| Safe in | You need |
|:--|--:|
| Half of runs | {{RAISE50}} |
| 8 runs out of 10 | {{RAISE80}} |
| **9 runs out of 10** | **{{RAISE90}}** |
| 19 runs out of 20 | {{RAISE95}} |

This is not money you spend on day one. The need builds up over four to five years, and it is two things added together.

First, everything the business loses before it turns a profit. Second, money it holds but cannot spend: gold bars on the shelf, cash held with the card scheme, and capital the licence requires it to keep untouched.

**One warning.** In {{PEAK_AT_HORIZON}} of runs the business still needs more money at month 84. Those runs have not stopped losing money within seven years, so for them this figure is a floor, not a ceiling. They are almost always the runs where partners did not sign.

### When the business earns it back

![Break-even by year](aurumix/outputs/charts/breakeven_by_year.png)

| By the end of | Share of runs that have earned it all back |
|:--|--:|
| Year 4 | {{BE4}} |
| Year 5 | {{BE5}} |
| Year 6 | {{BE6}} |
| Year 7 | **{{BE7}}** |

![Cumulative profit](aurumix/outputs/charts/cum_profit_fan.png)

Read this carefully, because it is easy to mistake.

The typical run loses money for about four years, then starts earning. But it does not finish. At month 84 the typical run is still **{{CUM_M84_MED}}** behind where it started. The runs that do get back to zero mostly do it around month {{BE_MONTH_MED}}.

So the honest summary of the plan today is not "profitable in year seven". It is: **about four runs in ten have paid back what they lost by year seven. The rest are still working on it.**

That is what the three changes in Part 4 are for.

### Where the money comes from

![Revenue with and without partners](aurumix/outputs/charts/revenue_fan_with_without_b2b.png)

Year-seven revenue is {{REV50}} in the typical run. {{REV_EX_B2B}} of that comes from direct customers. The rest, **{{B2B_SHARE}}**, comes from a handful of partner contracts.

![Partner dependence](aurumix/outputs/charts/partner_dependence.png)

Profit rises almost in a straight line with the number of partners. It is the strongest relationship in the whole model, and the one with the least evidence behind it.

---

## Part 2: Why the numbers come out that way

Four things explain the base case. Each one is a fact about the business rather than a modelling choice.

### Why so little is left per customer

The revenue model assumes every paying customer pays every month. Real ones do not.

Three of the five customer types in our simulation skip months on purpose. Across the whole book, customers pay in about **78% of the months they could**.

That one correction drops what a customer earns from USD 38 a year to **USD 32**. The cost of serving and replacing them does not drop at all.

### Why direct customers do not cover the bills

Forget partners for a moment. Picture the business standing still: no growth, customers leaving and being replaced, nothing else changing.

Does one customer make money?

![Retail alone](aurumix/outputs/charts/threshold_retail_alone.png)

Barely. One customer leaves **USD {{MARGIN15}} a year** once you have served them and paid to replace them when they leave.

Fixed costs are the bills that do not change no matter how many customers you have: licences, insurance, audits, the technology. Covering them at USD {{MARGIN15}} each needs **{{NEED15}} customers**. The plan reaches {{PAY50}}.

**Or {{PARTNERS15}} partners cover the same bills on their own.**

That is the whole finding. A partner pays a fee and costs almost nothing to serve. A customer pays a fee, then you deduct what it costs to serve them, then what it costs to replace them, and little is left.

We never add the two together. Adding them would hide whether the customer side works, and it does not.

#### About the safety margin

Budgets overrun, so we add a safety margin to costs. But we only add it where costs can actually surprise us.

| | We know these | These could surprise us |
|:--|--:|--:|
| Per customer, per year | USD {{VAR_CERT}} | USD {{VAR_UNC}} |
| Fixed, per year | {{FIX_CERT}} | {{FIX_UNC}} |

Contracted rates, published licence fees, the price a vendor charges per identity check, and the loyalty discounts Aurumix chooses are all known. They get no margin. Advertising costs, card scheme fees, technology and insurance are not known. They get one.

Push that margin from 15% to 30% and the answer disappears: you would need more customers than exist in all three countries combined. At 50%, no number of customers works.

Advertising is 92% of what it costs to win a customer. So really this is one test: **can you keep the cost of winning a customer down?**

### Only India makes money

Aurumix plans to launch in three places. We measured each one separately.

The headline cost of USD 44 to win a customer is an average. The real numbers are USD {{UAE_CAC}} in the UAE and USD {{INDIA_CAC}} in India. No actual customer costs USD 44, and the average was hiding the most useful thing we found.

![Regional economics](aurumix/outputs/charts/regional_economics.png)

| | Earns per year | Costs to win | Left over per year | Customers needed | Plan reaches |
|:--|--:|--:|--:|:--|--:|
| UAE | {{UAE_REV}} | {{UAE_CAC}} | **{{UAE_MARGIN}}** | {{UAE_NEED}} | {{UAE_BUILDS}} |
| Oman and Bahrain | {{GULF_REV}} | {{GULF_CAC}} | **{{GULF_MARGIN}}** | {{GULF_NEED}} | {{GULF_BUILDS}} |
| **India** | {{INDIA_REV}} | {{INDIA_CAC}} | **{{INDIA_MARGIN}}** | **{{INDIA_NEED}}** | **{{INDIA_BUILDS}}** |

Read the "left over" column. In the UAE and the Gulf it is negative. **Every customer you win there loses money.**

India is different. Each Indian customer leaves USD {{INDIA_MARGIN}} a year after everything. India alone would cover the company's entire fixed costs with {{INDIA_NEED}} customers, and the plan already reaches {{INDIA_BUILDS}} there.

Why the gap? Customers earn Aurumix almost the same amount everywhere. The difference is entirely in what they cost to find, and that happens for two reasons.

Advertising is cheaper in India. And all 420 sales agents are based there. An agent costs a commission on what they sell. Advertising costs money whether it works or not.

**Part 4 acts on this.**

### Why the raise is so large

A partner does not switch on overnight. Their users take a year or two to start using the product.

We built that in: a partner reaches full contribution over 12 to 24 months. It pushes the company's worst cash moment later, into exactly the period when the first partners have signed but are barely contributing.

![The funding line](aurumix/outputs/charts/funding_line.png)

This is worth acting on. **Anything that gets a partner's users on board faster is worth more than most product work.**

### Two numbers decide everything

Only two things really move the answer, and nobody knows either of them yet: **what it costs to win one customer**, and **how many partners sign**.

Everything else is either a choice Aurumix makes, which we test as a change in Part 4, or a number we have already pinned down.

So we ran the simulation across a grid of both.

![The conditions map](aurumix/outputs/charts/conditions_map.png)

Each square is a full seven-year run. Green means the business earns back everything it lost by year seven. Red means it does not.

**The plan sits right on the edge.** At the cost per customer we assume today, it needs {{FRONT_PLAN}} partners. It plans for exactly {{PLAN_PARTNERS}}. That is roughly break-even on cumulative profit at month 84, within the noise of a single map cell. The dependable cumulative figure is the one in Part 1: the typical run is still {{CUM_M84_MED}} behind where it started.

There is no room in that. Watch what happens when costs move:

| If one customer costs | You need |
|:--|:--|
| USD {{CAC_LO_UAE}} in the UAE, the cheap end | {{FRONT_GOOD}} partners |
| USD 54, as assumed today | {{FRONT_PLAN}} partners |
| USD 64, only 17% more | {{FRONT_BAD}} partners |
| USD {{CAC_HI_UAE}}, the expensive end | no number of partners we tested makes it work |

**Costs rising 17% means finding three more partners.** That is how tight this is.

### What the answer depends on most

![Tornado](aurumix/outputs/charts/tornado.png)

| | Assumption | How much it swings year-seven profit |
|:--|:--|--:|
| 1 | {{TOR1}} | {{TOR1_SW}} |
| 2 | {{TOR2}} | {{TOR2_SW}} |
| 3 | {{TOR3}} | {{TOR3_SW}} |
| 4 | {{TOR4}} | {{TOR4_SW}} |
| 5 | {{TOR5}} | {{TOR5_SW}} |

Partner assumptions take the top places. **Not one of them has been measured.**

One signed letter of intent would tell you more than any further modelling. It would give you a real user count and a real take-up rate.

---

## Part 3: What breaks it

Part 2 tested everything we could put a range on. This part tests single disasters that no range covers, and asks the same question of each: **can more money fix it?**

Each disaster runs {{ST_PATHS}} times, the same way the rest of this document runs. Every scenario uses the same set of runs as the others, so the same customers, the same gold prices and the same assumptions appear in each. Any difference between two rows is the disaster, not luck.

![Stress scenarios](aurumix/outputs/charts/stress_scenarios.png)

| What goes wrong | Profit after 7 years | Money needed | Runs that earn it back |
|:--|--:|--:|--:|
| Nothing, for comparison | {{ST_BASE_CUM}} | {{ST_BASE_PK}} | {{ST_BASE_BE}} |
| Gold falls 30% | {{ST_GOLD_CUM}} | {{ST_GOLD_PK}} | {{ST_S1_GOLD_CRASH_30_BE}} |
| A quarter of customers cash out at once | {{ST_RUN_CUM}} | {{ST_RUN_PK}} | {{ST_S2_REDEMPTION_RUN_25PCT_M24_BE}} |
| **No partner ever signs** | **{{ST_NOB2B_CUM}}** | **{{ST_NOB2B_PK}}** | **{{ST_S3_ZERO_B2B_BE}}** |
| Customers save less and leave faster | {{ST_ADOPT_CUM}} | {{ST_ADOPT_PK}} | {{ST_S4_ADOPTION_FAILURE_BE}} |
| The licence takes a year longer | {{ST_DELAY_CUM}} | {{ST_DELAY_PK}} | {{ST_S5_REGULATORY_DELAY_BE}} |
| Customers save smaller amounts | {{ST_TICKET_CUM}} | {{ST_TICKET_PK}} | {{ST_S6_TICKET_COMPRESSION_BE}} |
| Several of these at once | {{ST_TAIL_CUM}} | {{ST_TAIL_PK}} | {{ST_S7_COMBINED_TAIL_BE}} |

Profit is the typical run. Money needed is what covers 9 runs in 10, the same measure used everywhere else in this document.

### Can money fix it?

| What goes wrong | Verdict | What you would do |
|:--|:--|:--|
| Gold falls 30% | **Not a problem** | nothing. Customers own the gold, so they carry the price |
| A quarter cash out at once | **Money fixes it** | already covered by the planned raise. You need to be operationally ready, not richer |
| Customers save smaller amounts | **Money fixes it** | already covered by the planned raise |
| Licence delayed a year | **Money fixes it** | roughly USD 0.4m more, to pay the bills while you wait |
| Customers save less and leave faster | **Money just about fixes it** | survives, but never earns it back. Needs the Part 4 changes |
| **No partner ever signs** | **Money does not fix it** | you would need more customers than exist in all three countries |
| Several at once | **Money does not fix it** | the no-partner case, arriving at a worse time |

Three things to take from this.

**Gold is not the risk.** A 30% crash looks almost the same as a normal year.

**Partners are the whole risk.** Losing them costs {{ST_NOB2B_CUM}} over seven years and pushes the money you need to {{ST_NOB2B_PK}}.

But the number is not the point. **No amount of money turns a business with no partners into a working one.** Every other problem on this list is a cash problem. This one is not.

**A rush to cash out is survivable.** Profit falls to {{ST_RUN_CUM}} and the money you need rises only to {{ST_RUN_PK}}. The gold already belongs to customers, so this is an operations and timing problem, not a solvency one.

Loans stay safe too. The chance of ever having to ask a borrower for more collateral is **{{PMC}}**. The gold backing a loan rises in value with the same price the loan is measured in.

---

---

## Part 4: What to do about it

*This part is being rebuilt around the levers that create the most profit, and will be reissued with its own Monte Carlo. The base case and stress results above are final.*

---

## Part 5: What to learn next

### What to find out first

Nothing in this model has been measured. So the most useful thing we can give you is a list of what to go and learn, in order.

We ranked each one by how much the answer would move the result, against what it costs to find out.

| Find out | Moves year-seven profit by | How |
|:--|--:|:--|
| How many customers take the card | {{VOI1_SW}} | offer it to your first customers |
| What a partner pays | {{VOI2_SW}} | one term sheet |
| How many take the family plan | {{VOI3_SW}} | offer it to your first customers |
| What a partner is really worth | {{VOI_PARTNER_SW}} | one signed partner, or a serious pilot |
| What a customer costs to win | {{VOI_CAC_SW}} | one paid test campaign, 6 to 8 weeks |

**Four of the biggest unknowns can be settled this week, by reading documents you already have.** The vault fee is in your contract. The card rates are in the card scheme's published schedule. Together they account for {{VOI_FREE_SW}} of swing that this model still treats as uncertain.

The single most valuable thing remains one signed partner. It settles the biggest unknown in the model and costs a conversation, not a budget.

### When to change your mind

A target is only useful if you know when you have missed it.

| Watch | Today | The line | What crossing it means |
|:--|--:|--:|:--|
| Cost to win a UAE customer | USD {{TRIG_UAE_TODAY}} | USD {{TRIG_UAE}} | below it the UAE pays for itself; above it every UAE customer loses money |
| Cost to win a Gulf customer | USD {{TRIG_GULF_TODAY}} | no line | the Gulf loses money at every advertising price we tested |
| India | agents, not advertising | not an advertising number | advertising cost barely matters there. Watch how many customers each agent brings |
| Partners signed by year 7 | plan says {{PLAN_PARTNERS}} | {{FRONT_PLAN}} | below it the plan does not work at today's costs |

The India line is the one to remember. **Two of your three markets are advertising businesses. One is a sales-agent business.** They need different dashboards, and one blended cost per customer hides which is which.

We also tested whether missed payments should be a warning sign. They should not. Payment discipline moves what is left per customer by only USD {{TRIG_PAY_SPAN}} across its whole realistic range, because costs follow customers, not payments. Worth watching as a health check. It will not change a decision.

### What to watch in year one

| Measure | Why | Warning level |
|:--|:--|:--|
| Partners signed against plan | the business case rests on it | behind plan at month 24 |
| Months paid out of months due | what customer economics rest on | below 70% |
| Share reaching a loyalty tier | the cost of the ladder, and the promise | below 40% by month 36 |
| Cost to win one customer | rises as easy channels run out | above USD 60 blended |
| Cash against the plan | the raise | tracking below the typical run |

---

## Part 6: Appendix

### A. What we simulated

| | |
|:--|:--|
| Runs | {{PATHS}} |
| Detail | {{AGENTS}} |
| Length | 84 months, one month at a time, starting January 2027 |
| Assumptions varied per run | 75, plus a gold price path and a partner history |
| Repeatability | fixed seeds, so any run can be reproduced exactly |

### B. How to read the numbers

**Money to raise, 9 runs in 10** is the deepest point of the monthly cash line, at the ninth run out of ten. It covers everything lost so far plus money held but unspendable: gold on the shelf, card float, regulatory capital.

**Earned it back by year 7** means the run's total profit turned positive by month 84. It is not the same as making a profit in year seven, which happens earlier.

**Customers needed** assumes a business standing still: no growth, and just enough new customers to replace the ones who leave. It says what you must reach, not what you will reach.

**Runs out of ten** describes the spread of outcomes, not confidence in the model. Nine runs in ten surviving on a given sum assumes our assumptions are broadly right.

### C. The loyalty ladder, and what it costs

Priced at the tier each customer actually reaches, the ladder costs between **{{GIVE_LO}}** and **{{GIVE_HI}}** of revenue depending on how generous it is.

By month 84, **{{GATED}}** of live customers have made six payments in a row and hold a tier. Of those:

| Tier | Share of those with a tier |
|:--|--:|
| Silver | {{T_SILVER}} |
| Gold | {{T_GOLD}} |
| Platinum | {{T_PLAT}} |
| Sovereign | {{T_SOV}} |

![Tier mix](aurumix/outputs/charts/tier_mix_over_time.png)

Sovereign needs five years of near-perfect payments. Almost nobody reaches it within seven years, which is what makes it cheap to offer and worth holding.

The ladder is affordable in every version we tested. It is a pricing decision against your own profit target, not something that decides whether the business works.

### D. Where the profit sits

![Profit by ticket decile](aurumix/outputs/charts/profit_by_ticket_decile.png)

Rank customers by how much they save each month. The top tenth produce **{{DEC_TOP}}** of lifetime profit. The top three tenths produce {{DEC_TOP3}}. The bottom half produce {{DEC_BOT5}}.

A minority of customers carry the economics. That is normal for savings products, and it matters for who you target.

### E. What this model cannot tell you

It prices uncertainty that has been written down. It cannot price what has not.

- **No customer data exists.** How customers pay, how much they save and how many can be reached are all structured guesses, tested across ranges rather than measured.
- **No partner has signed.** The entire partner case rests on four unverified numbers.
- **Advertising spend never flexes.** A real company cuts spending when cash runs short. This model keeps spending the plan in every run, which makes bad runs look worse than they would be. For a fundraising number, that is the safe direction.
- **Checking is not proving.** Standing tests confirm the code does what the setup document says. Nothing confirms the assumptions are right until you have customers.

---
