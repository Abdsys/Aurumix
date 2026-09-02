# Aurumix gold savings: simulation results

**Prepared by:** Tokenomics.net
**Date:** September 2, 2026
**Simulation version:** 1.0

---

## Part 1: The question

### Executive summary

**Bottom line:** the retail savings business does not stand on its own at the current design. It needs B2B partners to be profitable, and there are none yet. That is the finding. Everything else in this document is about what to do with it.

At today's unit economics a UAE customer does not pay for their own replacement. The retail book alone needs about 76,000 paying customers to cover fixed costs, and only at a cheap blended acquisition cost. At UAE acquisition cost it never gets there. Three and a half B2B partners cover the same fixed costs by themselves. The revenue model's year-seven profit of USD 847k is real, but a third of its revenue comes from eleven partnerships nobody has started.

| Metric | Value | What it means |
|:--|--:|:--|
| Retail customers to cover fixed costs, on their own | **76,000** | At blended acquisition cost and 15% contingency. Unreachable at UAE cost |
| B2B partners to cover fixed costs, on their own | **3.5** | The partner channel is the profitability plan |
| Safe raise, 90% of paths covered | **USD 4.7m** | The revenue model's USD 2.29m is the median. A coin flip |
| P(cumulative break-even by year 7) | **38%** | The model's year-six crossing happens in 28% of paths |
| ICS giveback, top-loaded ladder at full ceiling | **6.3% of revenue** | Front-loaded, 18.4%. Shape costs three times more than generosity |
| Margin calls at Sovereign's 80% loan-to-value | **Certain** | Over a quarter of the credit book called in the median path |

The recommendation that matters most is to treat the B2B channel as the business and resource it that way now. The recommendations that cost nothing are to build the loyalty ladder top-loaded, default customers to the prefunded balance, size the float from the payment calendar, and reopen the spot door. The float policy moves the raise from USD 4.7m to about USD 4.0m. The ladder shape moves the giveback from 11% of revenue to 6%. One recommendation does cost something, and it is the credit line's top rung.

---

### The core question

The client asked one thing. What does it take for this business to be profitable, and what can we afford to give back to loyal customers along the way?

A spreadsheet cannot answer that. It runs forward from assumptions to a profit line. It cannot run backward from "profitable" to the inputs that get there. And this spreadsheet rests on ninety assumptions with no customer data behind any of them. So the simulation was built to invert the question. It searches for the threshold, the giveback envelope and the raise, and it puts a range around every number the revenue model states as a point.

There is a second reason it exists. The revenue model was simplified in August by taking machinery out and keeping two of its outputs as typed inputs. The share of customers who ever reach a loyalty tier, 55%, and the months it takes them, eight. Those two cells had no source once the machinery was gone. The simulation is where they come from.

**Validation.** The population engine reproduces every Phase 4 research figure when given the Phase 4 inputs, thirty-four checks. The ported revenue model reproduces the calculated workbook across thirty-six series and all twenty-nine periods with zero error. Invariants hold on every step of every path. Seven bugs were found and fixed in self-verification before any result was reported, and they are listed in the verification summary.

---

## Part 2: The discovery

### The initial finding

The first threshold I computed said 17,400 paying customers with B2B and 76,000 without. That looked fine. Then I checked how it was built and it was wrong in a way that hid the real answer. It spread B2B revenue across retail customers as if partners scaled with the book. They do not. A partner is a fixed block of revenue that arrives when a deal closes.

Separate the two and the picture changes. Fixed costs are about USD 430k a year. The retail business has to cover them on its own or partners do.

| Contingency on costs | Retail alone, blended acquisition cost | Retail alone, UAE acquisition cost | Or partners, on their own |
|:--|--:|--:|--:|
| 15% | **76,000 paying** | unreachable | **3.5** |
| 30% | 283,500 | unreachable | 3.9 |
| 50% | unreachable | unreachable | 4.5 |

![Retail alone](aurumix/outputs/charts/threshold_retail_alone.png)

The dotted line is O Gold's 75,000 active users in the UAE. It is the only observed demand number in the whole model. Retail alone sits right at it, and only at the cheapest acquisition mix, which is India-agent heavy. In the UAE a retail customer generates USD 41 a year, costs USD 13 to serve, and USD 25 a year to replace at 45% churn and USD 55 per acquisition. Add contingency and the margin is negative.

---

### The root cause

The retail unit margin is about six dollars a year. That is the number to sit with.

Revenue per paying customer excluding B2B is USD 41. The entry fee on a USD 33.60 ticket is USD 20 a year. Spot purchases, the card, the family plan and the credit share add another USD 21, spread thinly because only 18% of the book takes a card. Serving costs, the fabrication premium, the loyalty giveback, the card programme, KYC and redemption handling, take USD 13. Replacing the 45% of customers who lapse every year takes USD 17 at blended cost. Fifteen percent contingency on all of it leaves USD 6.50. At UAE acquisition cost it leaves minus USD 2.67.

Three things drive that.

**Churn is 45% a year.** Persistency of 55% at month thirteen means nearly half the book has to be re-acquired annually. The treadmill in the revenue model runs at 7.5 gross acquisitions per net customer added by year seven.

**The entry fee is the business and it is small.** Five percent of a USD 34 ticket is USD 1.68 a month. The card streams that were supposed to carry the business are USD 1.0m in year seven on 36,000 cards, and cardholder fees dwarf interchange because interchange is split three ways and cardholder fees are not.

**B2B has no unit economics at all.** One partner is USD 141,750 a year at the model's assumptions. That is the revenue of 3,500 retail customers, with no acquisition cost, no churn and no giveback. Of course the tornado ranks partner adoption first.

![Tornado](aurumix/outputs/charts/tornado.png)

The four inputs that move the answer most are partner adoption, partner assets per user, facility take-up and the B2B fee. Partner adoption alone swings year-seven profit by USD 1.8m, more than the profit itself. Persistency, the input everyone worried about, ranks eighth.

---

### What changed

This simulation did not end with a fee change. The entry fee is already at the top of the client's range. What it did was rank the levers by what they cost, so the recommendation is a list of things to do in order rather than one number to change. Four of them are free.

| Lever | What it does | Cost to Aurumix |
|:--|:--|:--|
| Treat B2B as the business | Covers fixed costs with 3.5 partners | A sales function, not a model change |
| Top-load the loyalty ladder | Giveback falls from 11.1% to 6.3% of revenue at the same headline | Free |
| Push the prefunded balance | Gate share 47% to 55%, plus about 9,000 paying customers by year seven | Onboarding design |
| Size the float from the calendar | Frees about USD 0.7m of the raise | A procurement process |
| Cap the credit line's top rung | Turns a certain margin call into a coin flip with almost nothing called | Product change, some lending revenue |
| Open the spot door | A spot-only customer pays back in 1.9 years in the UAE | Already built |

The rest of the document shows the evidence for each.

---

> **Key learning: this is what the simulation was for**
>
> The revenue model said year-seven profit is USD 847k. It was right, given its inputs. What it could not say was that a third of that revenue is a channel with no pipeline, that the retail business underneath it has a six-dollar margin, and that the loyalty ladder's cost depends on its shape three times more than its generosity. None of that is visible in a single deterministic path. All of it decides what the client should do next.

---

## Part 3: The results

### The raise

The revenue model's peak funding need is USD 2.29m. Across 2,000 paths, with every uncertain input drawn from the client's own scenario ranges and gold moving, that number is the median. Half the paths need more.

| Metric | Value |
|:--|--:|
| Peak funding, median | USD 2.82m |
| Peak funding, 80% of paths covered | USD 3.93m |
| **Peak funding, 90% of paths covered** | **USD 4.70m** |
| Peak funding, 95% of paths covered | USD 5.15m |
| P(need more than USD 3m) | 43% |

![Peak funding](aurumix/outputs/charts/peak_funding_hist.png)

The distribution is skewed right. That is not a modelling choice. The client's own scenario table has a wider downside than upside on most inputs, acquisition cost most of all, and the simulation takes those ranges at face value. The dotted red line is the revenue model. The dashed black line is where nine paths in ten are covered.

The float section below lowers this by about USD 0.7m, to roughly USD 4.0m at the 90% line, because the revenue model holds eight times more gold than a calendar-aware policy needs.

---

### When the business pays for itself

| Milestone | P(cumulative profit positive) |
|:--|--:|
| By year 4 | 4% |
| By year 5 | 14% |
| By year 6 | 28% |
| By year 7 | 38% |

![Break-even by year](aurumix/outputs/charts/breakeven_by_year.png)

The revenue model crosses in year six by USD 209k on a USD 3.06m cost base. In the simulation that happens in 28% of paths. Year-seven net profit has a median of USD 318k and a tenth percentile of minus USD 411k. This is a business that is more likely than not still cumulative-negative at the end of the horizon.

![Cumulative profit](aurumix/outputs/charts/cum_profit_fan.png)

The fan widens after month 24 for the usual reason, compounding variation in acquisition and churn, and for one unusual reason. The partner arrivals are lumpy. A dead year for partner deals moves the whole fan down.

---

### Revenue with and without partners

![Revenue with and without B2B](aurumix/outputs/charts/revenue_fan_with_without_b2b.png)

The left panel is total revenue. The right panel is the same paths with the partner stream removed. The median year-seven figure drops from USD 4.06m to USD 2.92m. That USD 1.1m is the difference between a business with a thin profit and one that runs a loss. Every revenue figure in this document should be read twice, once with partners and once without, because the client currently has none.

---

### The loyalty ladder

The revenue model gives away USD 364k in year seven through tier discounts. That is 43% of net profit, at four blended rates nobody designed, because the model cannot compute who is in which tier.

The simulation can. Here is the tier mix at the end of year seven, among customers who have earned a tier at all:

| Tier | Share of tiered customers |
|:--|--:|
| Silver | 45.4% |
| Gold | 41.8% |
| Platinum | 11.6% |
| Sovereign | 1.1% |

Half the live book, 50.1%, has earned a tier. The revenue model typed 55%.

![Tier mix over time](aurumix/outputs/charts/tier_mix_over_time.png)

Nobody is above Silver before month twelve. Platinum takes three years to appear in any size. Sovereign is a sliver at the top. That shape is the whole argument for how to build the ladder, and the sweep confirms it.

The giveback as a share of revenue, by how much the top tier gets and how the lower tiers share it:

| Top-tier discount | Top-loaded | Linear | Front-loaded |
|:--|--:|--:|--:|
| 1.0 points off | 3.7% | 6.5% | 10.6% |
| 1.5 points off | 5.0% | 8.8% | 14.4% |
| 2.0 points off | **6.3%** | 11.1% | **18.4%** |

![Ladder heatmap](aurumix/outputs/charts/ladder_heatmap.png)

Read the bottom row. The client can advertise "Sovereign pays 3%," the full two-point ceiling, for 6.3% of revenue if the ladder is top-loaded. The same headline costs 18.4% if the lower rungs are generous. Steepness costs three times more than the ceiling does. The marketing headline is nearly free. The early rungs are where the money goes, because that is where the customers are.

This is an affordability envelope, not an optimum. The simulation carries discounts as pure cost. It does not model whether a discount improves retention, because no source exists for that relationship. With cost and no benefit, zero giveback always looks best, and that is a tautology. The right reading is "here is what each shape costs you." Whether the discount buys loyalty is a question the live app will answer.

---

### Where the profit sits

The revenue model has one customer per region. The simulation draws a ticket for each one. Half the book sits at the USD 20 floor. The top tenth saves about USD 100 a month in the UAE.

![Profit by ticket decile](aurumix/outputs/charts/profit_by_ticket_decile.png)

The top tenth of customers by ticket contributes 21.7% of profit. The top three tenths contribute 44.9%. The floor half contributes 38.2%. The revenue model attributes 10% to each tenth and cannot see any of this.

The consequence is for acquisition. Every customer costs the same USD 85 to acquire in the UAE. A floor saver returns USD 12 a year in entry fees. A top-decile saver returns USD 60 and carries a bigger credit line, more card spend, and the same flat KYC cost. The cheapest route to profitability may be fewer, better customers, and the revenue model's engine can only buy more of the same one.

I tested whether the good behaviours cluster in the same people, since a perfect payer who also spends more and redeems less would concentrate profit further. Sweeping that correlation from zero to 0.6 moves the top decile from 21.7% to 22.4%. Clustering matters less than the ticket spread itself. A useful negative.

---

### The rail

Aurumix launches with two ways to pay. Request to Pay, where the customer taps every month. The prefunded balance, where they load once and forget. The rulebook only allows "set and forget" to be promised on the second one.

| Share on the prefunded balance | Reach a tier | Paying at year 7 | Entry fees, 7 years |
|:--|--:|--:|--:|
| 0% | 47.4% | 85,060 | USD 3.65m |
| 25% | 49.9% | 88,492 | USD 3.78m |
| 50% | 52.5% | 91,088 | USD 3.99m |
| 75% | **55.0%** | **93,916** | **USD 4.04m** |

![Rail mix](aurumix/outputs/charts/rail_mix.png)

Moving three quarters of customers onto the prefunded balance lifts the tier-earning share by eight points and adds about 9,000 paying customers by year seven. Nothing else in the model buys retention at onboarding cost rather than marketing cost. The size of the discipline gap between rails is unsourced and swept, so read the direction, not the decimal.

---

### The float

The revenue model holds one bar plus ten days of average demand. At year seven that is 3,400 grams, about USD 780k, with no cost in the profit and loss and no line for what happens when gold moves.

The inventory model sizes the float from the payment calendar instead. Sixty percent of the month lands in the five days after payday. Because that is scheduled, the float can be positioned before it.

| | Revenue model rule | Inventory model |
|:--|--:|--:|
| Float at year 7 | 3,406 grams | 441 grams on average, 2,750 before payday |
| Days with no gold to allocate | not measured | 0.3% |
| Carry cost, seven years | none | USD 24k |
| Mark-to-market, seven years, median | none | +USD 27k |
| Worst single year, tenth percentile | none | minus USD 15k |

![Float](aurumix/outputs/charts/float_workbook_vs_inventory.png)

The gold line is what the policy actually holds on average. The grey line is where it tops up to before payday. The red line is the revenue model. The model holds about eight times more gold than the policy needs, and that is USD 0.7m of the raise.

The client chose to leave the float unhedged. At this size that costs almost nothing. A worst year of minus USD 15k against a year-seven profit of USD 847k. The real input is the dealer. Lead time of one day needs 335 grams. Five days needs 718. A dealer who delivers weekly or has a minimum order changes the answer, and the dealer is still unnamed.

---

### The spot door

In August the spot-only customer was deleted from the revenue model. A spot buyer was worth the entry fee on 1.7 purchases a year, USD 16 in the UAE, against the USD 120 acquisition cost the model carried at the time. Six to eight years to pay back.

That calculation priced the spot buyer on the entry fee alone. Since then the card has been opened to everyone.

| Region | Spot-only value per year | Acquisition cost | Payback |
|:--|--:|--:|--:|
| UAE | USD 44 | USD 85 | 1.9 years |
| India | USD 31 | USD 15 | 0.5 years |

A spot buyer with a card pays back in under two years on spot economics alone, before any conversion to a monthly plan. The deletion was right on 21 August and wrong by 26 August, and the door is worth reopening.

---

### The credit book

A 30% gold crash barely moves the profit and loss. Year-seven profit falls by USD 460. That sounds wrong and it is not. Contributions are in dollars, so when gold falls the same dollars buy more grams, and the dollar value of the book is nearly unchanged. Phase 4 predicted this and the simulation confirms it independently.

The risk is in the stock, not the flow, and it is set by the loan-to-value rung.

| Struck loan-to-value | Rung | Gold move that triggers a call | P(any call in 7 years) | Share of book called, median |
|:--|:--|--:|--:|--:|
| 50% | Silver, and the revenue model | minus 41% | 4.5% | 0% |
| 59% | Tier-mix weighted | minus 31% | 19.5% | 0% |
| 72.5% | Platinum | minus 15% | 84.6% | 4.5% |
| **80%** | **Sovereign** | **minus 6%** | **100%** | **28.4%** |

![Margin calls by LTV](aurumix/outputs/charts/margin_calls_by_ltv.png)

At Sovereign's 80% a margin call is certain within the horizon. Over a quarter of the credit book is called in the median path, and 44% in the tenth-worst. The revenue model gives everyone the 50% rung and never sees this. Sovereign is 1.1% of tiered accounts, so the exposure is small in count. They are also the largest balances. The loan-to-value ladder is the credit-risk decision in the whole design, and it is worth revisiting before a lending partner prices it.

---

### Stress tests

Each scenario against the base. Year-seven profit, cumulative profit at year seven, and peak funding.

| Scenario | Year 7 profit | Cumulative at year 7 | Peak funding |
|:--|--:|--:|--:|
| Base | +847k | +1,055k | 2.29m |
| Gold crash, minus 30% | +846k | +1,053k | 2.29m |
| Redemption run | +472k | minus 254k | 2.34m |
| **Zero B2B** | **minus 713k** | **minus 4,048k** | **5.50m** |
| Adoption failure | +723k | +254k | 2.37m |
| Regulatory delay, 12 months | +847k | +316k | 3.03m |
| Ticket compression | +732k | +662k | 2.30m |
| **Combined tail** | **minus 379k** | **minus 3,231k** | **4.22m** |

![Stress scenarios](aurumix/outputs/charts/stress_scenarios.png)

Two scenarios break the business. Both are about partners.

**Zero B2B** is the worst single thing that can happen, and it is the current state of the pipeline. Without partners the business loses USD 713k in year seven, is USD 4m cumulative-negative, and needs USD 5.5m of funding.

**The redemption run** was the one the client pushed on, and rightly. A first version showed a run raising profit, because the revenue model pays the fabrication premium only on net-new grams and treats every redeemed gram as a bar it need not make. Chasing that down established that a rate-based redemption model cannot produce a run at all. It converges toward balance with inflows and never overshoots. A run is a jump, a quarter of custody leaving in one month, with existing customers pausing their contributions. Built that way it costs USD 375k of year-seven profit and pushes cumulative profit negative. The buyback spread on the excess gold is a few thousand dollars at any size tested. What hurts is customers pausing.

**The regulatory delay** costs USD 739k in standing costs and adds USD 0.74m to the raise. VARA publishes no approval timeline, so this is not a tail scenario. It is a planning case.

**The gold crash does nothing** to the profit and loss, for the reason given above. It does everything to the credit book at high loan-to-value.

---

## Part 4: The implications

### The bottom line

The question was what it takes to be profitable. The answer has two parts, and they are not the same size.

| Question | Answer |
|:--|:--|
| Does the retail business stand alone? | **No.** Six dollars of margin per customer, negative at UAE acquisition cost |
| What does profitability rest on? | **B2B partners.** Three and a half cover fixed costs. There are none yet |
| How much to raise? | **USD 4.7m** for nine paths in ten. About USD 4.0m with the float fixed |
| What can we give back? | **Six percent of revenue** at the full headline if the ladder is top-loaded. Eighteen if it is not |
| What is the credit risk? | **The Sovereign rung.** An 80% loan-to-value makes a margin call certain |
| What is free? | The ladder shape, the rail default, the float policy and the spot door. The loan-to-value cap costs some lending revenue |

I want to be direct about the first row because it is easy to soften. The retail economics as designed do not cover their own acquisition in the home market. That is not a parameter problem. It is the shape of a business that charges 5% on a USD 34 ticket and loses 45% of its customers a year. The partner channel fixes it, and the partner channel is a sales plan, not a modelling assumption.

---

### Strategic implications

| Finding | Implication |
|:--|:--|
| Retail alone needs 76,000 paying customers, or is unreachable | The B2C plan is a funnel for B2B, not a business. Resource partnerships first |
| 3.5 partners cover fixed costs | The first four partner deals matter more than the first 40,000 customers |
| Safe raise USD 4.7m against a model of USD 2.29m | Do not raise against the median. The revenue model's figure is a coin flip |
| P(break-even by year 7) is 38% | Investors should hear "probably not cumulative-positive in seven years" from us, not discover it |
| Giveback cost depends on shape three to one over ceiling | Build the ladder top-loaded. Keep the Sovereign headline, cut the Silver and Gold rungs |
| Prefunded rail lifts tier share eight points | Default new customers to the prefunded balance at onboarding |
| Float over-held eight times | Size procurement from the payment calendar. Name the dealer and get the lead time |
| Sovereign 80% loan-to-value is a certain margin call | Cap the top rung at 65% before a lender prices it. Moving the call line alone does not fix it |
| Spot buyer pays back in 1.9 years | Reopen the spot door as a second entry route |
| Regulatory delay adds USD 0.74m | Plan the raise on a 12-month licence delay, not a launch date |

---

### Recommendations

#### 1. Treat B2B as the business and staff it now

**Finding:** partner adoption moves the answer more than any other input. Three and a half partners cover the fixed cost base. Zero partners is a USD 4m cumulative loss. The pipeline is empty.

**Recommendation:** put a partnerships lead in place before launch, not after. Target the first two signed partners inside year one, not year two as the model assumes. Treat each retail region as proof for the partner pitch rather than as the revenue plan.

**Rationale:** one partner is worth the revenue of 3,500 retail customers with no acquisition cost, no churn and no giveback. Nothing on the retail side comes close.

---

#### 2. Build the loyalty ladder top-loaded

**Finding:** at the full two-point ceiling the giveback is 6.3% of revenue if the lower rungs get little, and 18.4% if they get a lot. The tier mix is 45% Silver and 42% Gold. Sovereign is 1.1%.

**Recommendation:** keep the headline. Sovereign pays 3%. Set Silver at 4.75% and Gold at 4.5% rather than 4.5% and 4.0%. Do the same on the family and FX rows.

**Rationale:** the headline is what the marketing uses and it costs almost nothing, because almost nobody reaches it. The early rungs are where the book is and where the money goes. The ladder can look more generous than it costs.

---

#### 3. Default customers to the prefunded balance

**Finding:** moving 75% of customers onto the prefunded balance lifts the tier-earning share from 47% to 55% and adds about 9,000 paying customers by year seven.

**Recommendation:** make the prefunded balance the default at onboarding, with Request to Pay as the fallback. Fund it by bank transfer only. A card-funded top-up costs 2.2% to 2.9% and is arithmetically impossible against a 5% fee.

**Rationale:** this is the only lever over payment behaviour that Aurumix controls, and it works at onboarding cost rather than marketing cost.

---

#### 4. Cap the credit line's top rung

**Finding:** at 80% loan-to-value a margin call is certain within seven years and over a quarter of the credit book is called in the median path. At 65% the chance of any call falls to 43%, the median share called is zero, and the tenth-worst path calls 4.5%. Moving the call line does not rescue the 80% rung. Even at a 95% call line the trigger is a 16% gold fall and a call arrives in four paths out of five.

**Recommendation:** cap Sovereign at 65% loan-to-value. Settle this before a lending partner prices the facility.

**Rationale:** Sovereign holders are few and they are the largest balances. A certain margin call on your best customers is a reputational event, not a credit event.

---

#### 5. Size the float from the payment calendar

**Finding:** the revenue model holds 3,400 grams at year seven. A calendar-aware policy holds 441 on average and runs out on 0.3% of days. The difference is about USD 0.7m of the raise.

**Recommendation:** name the bullion dealer and get the delivery lead time in writing. Build procurement around the payday cluster. Hold two bars minimum, order up to the next two days of scheduled demand plus a bar.

**Rationale:** the float is a procurement discipline, not a capital item. Every day of dealer lead time is roughly 200 grams of gold Aurumix has to own.

---

#### 6. Raise against the ninetieth percentile, planned on a licence delay

**Finding:** peak funding is USD 2.29m in the revenue model and USD 4.7m for nine paths in ten. A twelve-month regulatory delay adds USD 0.74m. The float fix removes about USD 0.7m.

**Recommendation:** plan the raise at USD 4.0m to 4.5m, not USD 2.3m. Assume the licence takes a year.

**Rationale:** the revenue model's figure is the median. Raising the median means a one-in-two chance of going back to investors.

---

### Key metrics to monitor

The simulation's inputs have no data behind them. The first year of operation will supply it. These are the numbers that decide whether the model was right.

**The adoption bridge:**

| Metric | Simulation assumes | Watch for |
|:--|--:|:--|
| Persistency at month 13 | 55% | At 50% year-seven profit falls by about USD 90k. The raise barely moves |
| Share reaching a tier by month 12 | 50% | Below 40% means the archetype mix is worse than assumed |
| Share on the prefunded balance | 30% | This is the lever. Push it toward 75% |
| Mean months to first tier | 8 | Above 10 means Request to Pay is dominating |

**The partner channel:**

| Metric | Simulation assumes | Watch for |
|:--|--:|:--|
| Signed partners by end of year 2 | 1 | Zero means the business is the zero-B2B stress case |
| Assets per adopting partner user | USD 350 | This is the second-ranked input. It has one observed anchor |

**The credit book:**

| Metric | Simulation assumes | Watch for |
|:--|--:|:--|
| Facility take-up | 18% of eligible | Third-ranked input |
| Share of drawn balances above 65% loan-to-value | small | Any material share is margin-call exposure |

**Cash:**

| Metric | Simulation assumes | Watch for |
|:--|--:|:--|
| Days with no gold to allocate | 0.3% | Above 1% means the dealer lead time is longer than 2 days |
| Redemptions as share of purchases | ~20% | Above 100% in any month is a run |

---

## Part 5: Appendix

### Appendix A: Simulation configuration

**Customer behaviour:**

| Parameter | Value | Notes |
|:--|--:|:--|
| Archetype shares | 10 / 35 / 12 / 13 / 30% | Perfect, occasional, alternating, reducer, early lapser. Swept |
| Background lapse hazard | 1.6% per month | Derived from Phase 4 attrition figures |
| Persistency at month 13 | 55% | Drawn per path, 45% to 65% |
| Ticket floor share | 50% | Swept 40% to 60% |
| Prefunded rail share | 30% | Swept 0 to 75% |
| Card dormancy | 0 per month | Swept to 2%. No published rate exists |

**The loyalty system:**

| Parameter | Value |
|:--|--:|
| Gate | 6 consecutive counted months |
| Tier thresholds | 25 / 50 / 75 / 100 |
| Record cap | 60 months |
| Retention allowance | 30% of gold sold per year |
| Entry-fee ceiling | 2.0 points off 5% at Sovereign |

**Gold and the float:**

| Parameter | Value | Notes |
|:--|--:|:--|
| Gold price, month 1 | USD 141.50 per gram | |
| Drift | 8.1% per year | The revenue model's appreciation |
| Volatility | 15% per year | Swept 10% to 22%. Not a fetched citation |
| Dealer lead time | 2 days | Swept 1 to 5 |
| Service level | 99% | |
| Carry cost | 6% per year | Swept 4% to 8% |
| Buyback spread | 1% | Swept 0.5% to 2% |
| Hedging | none | Client decision |

**The credit book:**

| Parameter | Value |
|:--|--:|
| Loan-to-value by tier | 50 / 50 / 65 / 72.5 / 80% |
| Call line | 85% current loan-to-value, swept 75% to 95% |
| Facility take-up | 18% of eligible book |

**Simulation settings:**

| Parameter | Value |
|:--|--:|
| Monte Carlo paths | 2,000 |
| Horizon | 84 months, from January 2027 |
| Simulated customers | ~200,000 |
| Random seed | 20270101 |

Every other parameter is read directly from the calculated Phase 4 workbook.

---

### Appendix B: Chart reference

| Chart | Shows |
|:--|:--|
| `threshold_retail_alone.png` | Paying customers needed for retail to cover fixed costs alone, by contingency |
| `tornado.png` | Year-seven profit swing per input across its scenario range |
| `peak_funding_hist.png` | Distribution of peak funding across 2,000 paths |
| `breakeven_by_year.png` | Probability of cumulative break-even by year |
| `cum_profit_fan.png` | Cumulative profit percentile bands over the horizon |
| `revenue_fan_with_without_b2b.png` | Annual revenue with and without the partner stream |
| `tier_mix_over_time.png` | Share of tiered customers in each tier, monthly |
| `ladder_heatmap.png` | Giveback as share of revenue by ladder ceiling and shape |
| `profit_by_ticket_decile.png` | Share of profit by customer ticket rank |
| `rail_mix.png` | Tier-earning share by prefunded balance adoption |
| `float_workbook_vs_inventory.png` | Float held under the revenue model rule versus the inventory policy |
| `margin_calls_by_ltv.png` | Margin call probability and share called by loan-to-value rung |
| `stress_scenarios.png` | Cumulative profit and peak funding by stress scenario |

All charts live in `aurumix/outputs/charts/`.

---

### Appendix C: Methodology notes

**Verification before validation.** The population engine reproduces the Phase 4 research figures given the Phase 4 inputs. That is a test of the code, not of the business, because those figures came from an unsourced archetype mix. The mix is swept in every result.

**The ported engine is exact.** Thirty-six series across all twenty-nine periods match the calculated workbook with zero error. Parameters are extracted from the workbook programmatically, so the port cannot drift by transcription.

**Base is the mode.** Each drawn parameter uses a PERT distribution with the revenue model's base value as the mode and its Aggressive and Conservative values as the tenth and ninetieth percentiles. The client's ranges are wider on the downside, so the median path lands below base. That is their scenario table speaking, not the simulation.

**B2B partners arrive lumpily.** Each year's planned net adds become a Poisson draw with a 25% chance of a dead year. This is a judgement, and the tornado says it is the one that matters most.

**A run is a jump.** A rate-based redemption model converges toward balance with inflows. The run scenario is a discrete share of custody leaving in one month.

**Seven bugs were found in self-verification.** Rounding in the score formula that made Sovereign unreachable. Ticket noise that double-counted misses. A threshold that spread partner revenue per customer. A delay scenario that kept marketing running while unlicensed. An agent book that never cancelled family plans. A float policy that reacted to payday rather than anticipating it. A clustering parameter that did not load on ticket. All fixed before any number in this document was reported.

**What is not modelled.** Headcount, legal, security and tax, carried as a swept contingency. Competitive response. Regulatory change. Intra-month gold moves. Hedging, by client decision. The supply side, by scope.

**What should be validated in year one.** Persistency. The share reaching a tier and when. The prefunded rail's real effect on payment discipline. Whether any partner signs. The dealer's lead time. Every one of those is an input the simulation had to assume, and every one becomes observable the month the app launches.
