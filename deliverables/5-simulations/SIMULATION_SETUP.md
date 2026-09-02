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

## 1. Objective

Aurumix sells gold by the gram. A customer commits to a monthly amount from USD 20. Every dollar buys allocated physical gold in a Dubai vault. One AURX token is one gram. The customer pays a 5% entry fee and nothing else. Behind the savings product sit a card, a credit line against the gold, a family plan, and a platform fee from B2B partners who white-label the product.

The revenue model built in Phase 4 says this business makes USD 847k in year seven and needs USD 2.29m of funding at its worst point. Those are single numbers. They rest on about ninety assumptions, and the client has no customer data yet. None. No waitlist, no pilot, no partner in the pipeline.

So the simulation does not ask "what will happen." It asks three harder questions. What has to be true for this business to be profitable? How much can Aurumix afford to give back to loyal customers? And how much money does it need to raise so that it is still standing in nine paths out of ten?

That framing matters. A forecast built on unsourced inputs is a guess with decimal places. A threshold is different. It says "you need this many paying customers" and that number does not care whether the market funnel is right. I think that is the only honest deliverable at this stage, and the document is built around it.

The simulation runs 2,000 seven-year paths. Each path draws its own customer behaviour, gold price, marketing response and partner deals. Underneath it, 200,000 simulated customers each live their own seven years. The revenue model is the centre case. The simulation is the spread around it, and the source of two numbers the revenue model could not compute for itself.

---

## 2. Two engines, one company

The simulation has two layers and they describe the same company.

The first layer is a line-for-line port of the Phase 4 revenue model into Python. Every stream, every cost, the float and the regulatory capital. With every input pinned to its base value, the port reproduces the workbook's 29 periods to within floating-point error. That test is the reason the rest of the results can be trusted. If the port drifted from the workbook, every stochastic result would be arguing with a number the client has already seen.

The second layer is the population. The revenue model uses one average customer and multiplies. The simulation creates individual customers, each with a ticket, a payment personality, a payment rail and a way in. It runs them month by month. Whether a customer earns a loyalty tier depends on six consecutive payments, and six in a row is a property of one person's history. It cannot be recovered from an average. That is the whole reason to build agents rather than aggregates.

The two layers meet at acquisition. The population engine takes its new customers each month from the ported revenue model, so both layers grow the same book.

---

## 3. The customer

Each simulated customer carries five things at birth. A region, a monthly ticket, a payment archetype, a payment rail, and an entry door.

**Region** is one of the UAE, Oman and Bahrain together, or India. It sets the average ticket, the acquisition cost and when the market opens.

**Ticket** is the amount the customer means to save each month. The revenue model uses one number per region, USD 33.60 in the UAE. Savings books are not like that. Half the book sits at the USD 20 floor and a thin tail saves far more. The simulation draws each customer's ticket from a distribution fitted to two facts, the regional mean and the share at the floor:

$$\text{ticket} = \max\left(20,\; X\right), \qquad X \sim \text{Lognormal}(\mu, \sigma)$$

Where:

- $\mu$ and $\sigma$ are solved so that $P(X \le 20) = 0.50$ and $E[\max(20, X)]$ equals the regional mean
- $20$ is the USD floor, below which a payment is refused

For the UAE that gives $\sigma = 0.87$. The top tenth of customers then contributes about 30% of all money saved. The floor share is not sourced, but it is a defensible shape. Assuming a flat book would be the less credible choice.

The amount is variable month to month with no maximum. A customer at the floor pays exactly the floor. Whether they pay at all is the archetype's job, described next.

**Archetype** is the customer's payment discipline. Five types, taken from the Phase 4 research:

| Archetype | Share | Pays in a given month | Own monthly lapse hazard | Terminal tier |
|:--|--:|--:|--:|:--|
| Perfect payer | 10% | 99.5% | 0.0% | Only type that reaches Sovereign |
| Occasional misser | 35% | 93% | 0.7% | Platinum, sometimes Sovereign |
| Alternating misser | 12% | 55% | 1.8% | Gold for life |
| Reducer | 13% | 97% | 0.2% | By record |
| Early lapser | 30% | 60% | 20.0% | Rarely tiers, mostly gone by month 13 |

A background hazard of 1.6% per month applies to everyone on top of their own. The shares are the weakest input in the whole model. No published source anywhere decomposes a savings-lapse curve into behavioural types. The simulation does not assume them. It sweeps them, and reports what the answer looks like across the plausible range.

**Rail** is how the customer pays. Aurumix launches with two, and they demand different things every month. On Request to Pay the customer taps to approve each payment. On the prefunded balance they load once and the balance draws automatically. The rulebook makes the distinction itself. It only allows "set and forget" to be promised on the prefunded balance. So a prefunded customer draws from a mix tilted toward discipline. Thirty percent of customers start prefunded and 35% of those are re-drawn into the disciplined archetypes. Both numbers are unsourced and both are swept. This is the one lever over payment behaviour that Aurumix actually controls.

**Door** is whether the customer arrived through a monthly SIP or a one-off spot purchase. Spot buyers can now hold a card, so a spot-only customer is worth more than the entry fee alone.

---

## 4. The gate and the score

The loyalty system is called ICS. It decides which benefit tier a customer sits in, and every tier discount reads it.

Nothing happens until the gate. A customer earns Confirmed SIP status on their sixth consecutive counted month. A counted month is one accepted payment at or above the floor. A miss resets the streak to zero. That single rule is why tier arrival is a distribution and not a date. A customer who misses month four cannot qualify before month nine.

Once gated, the score is computed from three facts on the payment and token ledgers. Months is the count of counted periods since the qualifying run began. It starts at six on gate day and never falls. Recent is the count of counted periods in the trailing twelve calendar months. Sold is the share of gold the customer had a year ago that they no longer hold.

Each fact maps to a component:

$$\text{Record}(m) = \begin{cases} m \times \tfrac{50}{12} & m \le 12 \\[4pt] 50 + (m-12)\times\tfrac{50}{48} & 12 < m \le 60 \\[4pt] 100 & m > 60 \end{cases}$$

$$\text{Standing} = \text{Recent} \times \tfrac{100}{12}$$

$$\text{Retention} = \begin{cases} 1 & \text{Sold} \le 0.30 \\[4pt] 1 - \dfrac{\text{Sold} - 0.30}{0.70} & \text{Sold} > 0.30 \end{cases}$$

And the score is the smaller of the first two, scaled by the third:

$$\text{ICS} = \min(\text{Record}, \text{Standing}) \times \text{Retention}, \quad \text{floored at } 25 \text{ once gated}$$

Where:

- $m$ is Months, the counted periods since the run began
- Recent runs from 0 to 12
- Sold runs from 0 to 1, recomputed monthly against the gold held twelve months earlier plus gold bought since

The minimum is the arithmetic of "and". A long record cannot cover a dead year. A good year cannot cover a short record. That is why the alternating misser caps at Gold forever. Their Recent never climbs above six, so Standing never climbs above fifty, and no amount of tenure lifts it. Retention is a veto. Sell more than 30% of your gold in a year and the score falls in proportion, to zero if you empty the account.

Tiers threshold the score at 25, 50, 75 and 100. A perfect payer reaches Silver at month six, Gold at twelve, Platinum at thirty-six and Sovereign at sixty. The Phase 4 model could not carry this formula and used a lookup instead. The lookup put every rung six months late. The simulation computes the real thing.

---

## 5. What a tier buys

Five benefits, each priced by tier. The benefit ladder in the base case:

| Benefit | None | Silver | Gold | Platinum | Sovereign |
|:--|--:|--:|--:|--:|--:|
| Entry fee paid | 5.00% | 4.50% | 4.00% | 3.50% | 3.00% |
| Family plan discount | 0% | 10% | 20% | 35% | 50% |
| Card FX margin charged | 2.0% | 2.0% | 1.5% | 1.25% | 1.0% |
| Credit line, loan to value | 50% | 50% | 65% | 72.5% | 80% |
| Gold rewards, share of card spend | 0 | 0.15% | 0.45% | 0.60% | 0.75% |

Three rows come straight from the mechanism design. The entry-fee row takes the full 2.0 point ceiling the design allows and steps it evenly. The middle rungs of the FX and loan-to-value rows are interpolated.

The whole ladder is generated from three dials so it can be swept. The ceiling is how much the top tier gets. The steepness is how much of that the lower tiers get, from top-loaded to front-loaded. The breadth is which benefits are laddered at all. Three dials are something a client can argue about. Twenty independent rates are not.

Gold rewards carry one rule that only an agent model can enforce. A customer's rewards never exceed the revenue that customer generated. The revenue model applies a rate to aggregate card revenue and cannot see the cap.

The loan-to-value row is different in kind. It is not a discount. It gives leverage. A Sovereign customer borrows against 80% of their gold where a Silver borrows against 50%. That raises revenue and raises risk at the same time, and it is the row that drives the credit-book results in Section 10.

---

## 6. Four independent clocks

The revenue model has one churn rate. A customer stops paying and becomes a holder who keeps their gold. That collapses several behaviours into one, and then needs a switch to say whether holders keep their card.

The simulation separates them. A customer can stop paying the SIP, let the card go dormant, repay the credit line, or redeem the gold. Each has its own clock. Stopping the SIP does not stop the card. This is the client's own framing, that it may be churn of a feature rather than of the platform, and it turns a coin-flip switch into a rate that can be argued about.

Card dormancy has no published rate anywhere. I looked. Not for the UAE, not for the Gulf, not for fintech cards globally. Only definitions exist. So it is carried as an assumption and swept from zero to 2% per month.

---

## 7. Gold, partners and the draws

Three things are random at the path level on top of customer behaviour.

**Gold** follows geometric Brownian motion, sampled monthly:

$$P_{t+1} = P_t \cdot \exp\left[(\mu - \tfrac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\cdot Z_t\right]$$

Where:

- $P_t$ is the gold price in USD per gram at month $t$, starting at 141.50
- $\mu = 8.1\%$ is the annual drift, the same appreciation the revenue model uses
- $\sigma = 15\%$ is the annual volatility, the long-run realised figure for gold, swept from 10% to 22%
- $\Delta t = 1/12$
- $Z_t$ is a standard normal draw

There is one gold path per run and it hits every customer at once. The client chose not to hedge. Aurumix owns the price variance on the gold it holds.

**Partner arrivals** replace the revenue model's straight line of one to eleven B2B partners. Each year's planned net adds become a Poisson draw, with a 25% chance of a dead year. Eleven enterprise deals cannot be a smooth curve, and the client has no pipeline yet.

**Every other uncertain input** is drawn once per path from a distribution anchored on the revenue model's own scenario table. The base value is the mode. The Aggressive and Conservative values are treated as the tenth and ninetieth percentiles of a PERT distribution. That grounds every draw in a range the client has already seen and signed. It also means the median path lands below base, because the client's own ranges are wider on the downside. That is not a modelling choice. It is what their scenario table says.

Thirty-two parameters are drawn this way. Persistency, the three regional acquisition costs, referral rate and conversion, spot behaviour, the programme manager's share of interchange, facility take-up, family attach, partner economics, and the contingency on the cost base.

---

## 8. What happens each month

Every month, in this order.

The gold price advances. New customers arrive from the ported acquisition engine and are assigned their region, ticket, archetype, rail and door. Each living customer decides whether to pay, at their archetype's probability, and how much, around their ticket. The streak updates, the gate fires for anyone reaching six, and the score and tier are recomputed. Gold accumulates at the current price, net of the entry fee. Cards are taken up by a share of the eligible book, spend runs against the credit limit at the tier's loan-to-value, and rewards are paid up to the cap. Family plans attach on new customers and cancel at the workbook's rate. Redemptions and moves to self-custody drain gold. Then the four clocks tick. SIP lapse, card dormancy, credit repayment, exit.

The aggregates then flow through the ported revenue model. Revenue by stream, the fabrication premium, the vault, the licences, the ICS giveback, acquisition cost, the card programme, contingency, net profit, capital tied up and the funding line.

Redemption has one rule worth stating. Money paid after the five-day grace is a spot purchase, not a late contribution. It earns the fee, buys gold at that day's price, and does not restore the streak. Redeemed gold refills the float. Any excess above what new buyers absorb that month is sold back to the dealer at a two-way spread, swept at 0.5%, 1% and 2%.

---

## 9. The float as inventory

Aurumix has to own gold before customers do, so that a gram is allocated the moment a payment lands. The revenue model sizes that float as one bar plus ten days of average demand. The ten is a guess and the float earns no line in the profit and loss.

The simulation treats the float as an inventory problem at daily resolution. Sixty percent of a month's SIP volume lands in the five days after payday. Spot purchases arrive as random lumps. Because SIP payments are scheduled, the float is positioned before the payday cluster, using the calendar rather than reacting to history:

$$S_d = \sum_{k=1}^{L} D_{d+k} \;+\; z_{0.99}\,\sigma_{\text{spot}}\sqrt{L} \;+\; 100, \quad \text{rounded up to whole bars}$$

Where:

- $S_d$ is the order-up-to level in grams on day $d$
- $D_{d+k}$ is the scheduled SIP demand $k$ days ahead
- $L = 2$ is the dealer's delivery lead time in days, swept from 1 to 5
- $z_{0.99}$ is the normal quantile for a 99% service level
- $\sigma_{\text{spot}}$ is the standard deviation of the unscheduled spot demand
- $100$ is one bar, held as a buffer

Orders arrive after the lead time in 100 gram bars. The float never falls below two bars. It is marked to market daily on the gold path and carries a cost of 6% a year, swept from 4% to 8%. Unhedged. A first version of this policy used a rolling history for safety stock and ran out of gold on 7% of days, because it reacted to payday after payday hit. The calendar version runs out on 0.3% of days.

---

## 10. The credit book under a moving price

Margin calls are a property of when a loan was struck and at what loan-to-value. So drawn balances are tracked by vintage, each carrying the gold price on the day it was drawn. A vintage is called when the current price falls far enough that the loan exceeds 85% of the collateral's value:

$$\frac{P_t}{P_0} < \frac{\text{LTV}_{\text{struck}}}{0.85}$$

Where:

- $P_0$ is the gold price when the vintage was drawn
- $P_t$ is the price now
- $\text{LTV}_{\text{struck}}$ is the tier's loan-to-value at origination
- $0.85$ is the call line, taken from the client's own worked example and swept from 0.75 to 0.95

The arithmetic is simple and the consequence is not. At 50% loan-to-value a call needs gold to fall 41% from the strike. At 80%, the Sovereign rung, it needs 6%.

---

## 11. The threshold

The question the client asked is what it takes to be profitable. The simulation answers it at steady state, where the book is flat and acquisition only replaces churn. Then the fixed cost base has to be covered by retail customers or by B2B partners, and the two are kept apart:

$$N^* = \frac{k \cdot F}{r - k\,(s + c \cdot \text{CAC})} \qquad\qquad K^* = \frac{k \cdot F}{A \cdot f}$$

Where:

- $N^*$ is the number of paying retail customers that covers fixed costs on their own
- $K^*$ is the number of B2B partners that covers fixed costs on their own
- $F$ is the annual fixed cost base, about USD 430k
- $k$ is one plus the contingency, swept at 15%, 30% and 50%
- $r$ is retail revenue per paying customer per year, about USD 41 excluding B2B
- $s$ is the serving cost per customer, about USD 13
- $c$ is annual churn, 45%
- CAC is the cost to replace one customer, USD 37 blended or USD 55 in the UAE alone
- $A$ is assets under management per partner and $f$ is the platform fee

Keeping the two apart matters. Blending B2B revenue into a per-customer figure hides whether the retail business stands on its own. It does not, and Section 3 of the results document is about that.

---

## 12. Stress scenarios

Seven, each run against the base.

**Gold crash.** A 30% fall from month 24 onward. Tests the credit book and the collateral base.

**Redemption run.** A quarter of custody exits in month 24 while existing customers cut contributions to 40% of normal. A run is a jump, not a rate. A rate-based redemption model converges toward balance with inflows and never overshoots, so the run has to be built as a discrete event.

**Zero B2B.** No partners, ever. Tests whether the retail business stands alone.

**Adoption failure.** Persistency at 45%, acquisition costs at the conservative end, and fewer customers reaching a tier.

**Regulatory delay.** Twelve months of licences, insurance, audit and technology build with no revenue, because VARA publishes no approval timeline.

**Ticket compression.** Every regional ticket at its conservative value.

**Combined tail.** The crash, the run and a B2B slump together.

---

## 13. What was verified and how

Two gates had to pass before any result was reported.

The population engine reproduces the Phase 4 research figures when given the Phase 4 inputs. The alternating misser's 24% chance of ever reaching six in a row, the mean gate month of 8.1, the persistency curve at every anchor. Thirty-four checks. That proves the code is right. It proves nothing about Aurumix, because those figures came from the same unsourced archetype mix.

The ported revenue model reproduces the calculated workbook. Thirty-six series, all 29 periods, zero error. That is what makes the simulation an extension of the model rather than a rival to it.

One published figure was deliberately not chased. The Phase 4 research put Sovereign at 1.2% of tiered accounts. That number came from the lookup that capped the occasional misser at Platinum by construction. Under the real formula a clean trailing year plus sixty counted months scores 100, and it should. In the simulated book Sovereign lands at 1.1% anyway.

---

## 14. Assumptions and limits

**The demand side is judgement.** The cost side is well sourced. VARA and DMCC fee schedules, the KYC provider's price list, the Visa interchange schedule, Zand's banking tariff. The demand side is not. The market funnel filters are made up. The archetype mix has no source. Persistency's validation file is missing from the repository. No client data exists. Every one of those is swept rather than assumed, and the profitability threshold is built so that it does not depend on the funnel at all.

**Contingency stands in for headcount.** Staff, legal, security and tax are not modelled. A 15% contingency on all costs is the placeholder, and it is swept to 50% so the threshold can be read against the cost that is not yet built.

**B2B is a straight line with noise, not a business.** Partner economics rest on one observed anchor, O Gold's 75,000 active users, and a lumpy arrival process. There is no pipeline to calibrate to.

**The buyback spread is second order.** It is in the model and swept. At every run size tested it costs a few thousand dollars. What hurts in a run is customers pausing their contributions.

**Gold volatility is from general knowledge.** Fifteen percent is the long-run realised figure. It is not a fetched citation. It is swept.

**No competitive response, no regulatory change, no intra-month price moves.** Margin calls are tested monthly.

**The supply side is out of scope.** Circulating supply and free float are a separate phase.

---

## 15. Running the simulation

The simulation is a Python project using NumPy, SciPy and Pandas. From the `aurumix/` directory:

```bash
pip install -r requirements.txt
python scripts/extract_params.py
python scripts/verify_stage1.py
python scripts/verify_stage2_equivalence.py
python scripts/run_mc.py 2000
python scripts/run_analysis.py
python scripts/run_float.py
python -m src.visualize
```

The first script reads every parameter from the calculated workbook into a JSON file, so the port cannot drift by transcription. The two verification scripts must pass before the rest means anything. Every script uses fixed seeds. Every figure in the results document can be regenerated.

Outputs are written to `outputs/`, charts to `outputs/charts/`. Total runtime is under ten minutes.
