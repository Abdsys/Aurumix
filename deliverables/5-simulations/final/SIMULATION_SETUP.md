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

The Phase 4 revenue model is a spreadsheet. It says the business makes USD 847k in year seven and needs USD 2.29m of funding at its worst point.

Those are single numbers. They rest on about ninety assumptions. The client has no customer data yet. No waitlist, no pilot, no partner in the pipeline.

### The three questions

The simulation does not ask what will happen. It asks three harder questions.

- What has to be true for this business to be profitable?
- How much can Aurumix afford to give back to loyal customers?
- How much money does it need to raise to still be standing in nine paths out of ten?

### Why a threshold and not a forecast

A forecast built on unsourced inputs is a guess with decimal places. A threshold is different. It says "you need this many paying customers," and that number does not depend on whether the market funnel is right.

I think that is the only honest deliverable at this stage. The document is built around it.

### What the simulation runs

Two thousand seven-year paths. Each path draws its own customer behaviour, gold price, marketing response and partner deals.

Underneath each path, two hundred thousand simulated customers live their own seven years, month by month.

The revenue model is the centre case. The simulation is the spread around it. It is also the source of two numbers the revenue model could not compute for itself.

---

## 2. Two engines, one company

### The first engine: the revenue model, ported

The first layer is a line-for-line port of the Phase 4 revenue model into Python. Every stream, every cost, the float and the regulatory capital.

With every input pinned to its base value, the port reproduces the workbook's twenty-nine periods to within floating-point error. That test is why the rest of the results can be trusted. If the port drifted from the workbook, every result would be arguing with a number the client has already seen.

### The second engine: individual customers

The revenue model uses one average customer and multiplies. The simulation creates individual customers instead. Each has a ticket, a payment personality, a payment rail and a way in. It runs them month by month.

This matters for one reason. Whether a customer earns a loyalty tier depends on six consecutive payments. Six in a row is a property of one person's history. It cannot be recovered from an average.

### Where the two engines meet

They pass information both ways.

**Forward.** The population engine takes its new customers each month from the ported revenue model, so both layers grow the same book.

**Back.** The population engine sends two things the other way.

The first is the tier mix, month by month, which prices the loyalty giveback. The spreadsheet applies one flat discount rate to a flat share of the book, because it cannot see who is in which tier. That shortcut is wrong in a known direction: nobody has the tenure for Platinum in year two, so a flat rate is too generous early and too mean late.

The computed rate runs at **10.7% of the entry fee at month 12, rising to 17.8% by month 84**, against the spreadsheet's flat 25%.

The second is referral capacity. The spreadsheet counts referrals off the raw paying head count, so a customer in month two is as persuasive as one in year three. They are not. Nobody recommends a savings plan they have barely started, and advocacy rises with what the plan has actually given them.

So propensity is zero for three months, ramps to full by month twelve, and scales up the tier ladder. The population engine knows every customer's tenure and tier, so it can compute what the whole book is worth as a referral source. That figure is **0.35 of the flat assumption in year one and 0.74 by year three**, reaching 1.0 on a matured book. Both corrections are judgement rather than measurement, and are marked as such.

Running the population engine inside all 2,000 paths would take hours. Instead it runs once across a spread of persistency values, producing a lookup the ported engine reads on every path.

---

## 3. The customer

Each simulated customer carries five things at birth. A region, a monthly ticket, a payment archetype, a payment rail, and an entry door. This section takes them in turn.

### Region

One of the UAE, Oman and Bahrain together, or India. Region sets the average ticket, the acquisition cost, and when the market opens. India and the UAE open in month one. Oman and Bahrain open in month thirteen.

### Ticket

The ticket is the amount the customer means to save each month. The revenue model uses one number per region, USD 33.60 in the UAE.

Savings books are not like that. About 30% of the book sits at the USD 20 floor. A thin tail saves far more. So the simulation draws each customer's ticket from a distribution fitted to two facts, the regional mean and the share at the floor:

$$\text{ticket} = \max\left(20,\; X\right), \qquad X \sim \text{Lognormal}(\mu, \sigma)$$

Where:

- $\mu$ and $\sigma$ are solved so that $P(X \le 20) = 0.30$ and $E[\max(20, X)]$ equals the regional mean
- $20$ is the USD floor, below which a payment is refused

For the UAE that gives $\sigma = 0.576$. The top tenth of customers then contributes about 23% of all money saved.

The two facts lock the answer between them. If 30 customers in 100 pay exactly USD 20, that is USD 600 of a USD 3,360 total, so the other 70 must average USD 39.43. The curve is whatever produces that.

The floor share is not sourced. It is a defensible shape, set at 30% on client instruction, and it is swept. Assuming a flat book would be the less credible choice.

The amount is variable month to month with no maximum. A customer at the floor pays exactly the floor. Whether they pay at all is the archetype's job.

### Archetype

The archetype is the customer's payment discipline. Five types, taken from the Phase 4 research:

| Archetype | Share | Pays in a given month | Own monthly lapse hazard | Terminal tier |
|:--|--:|--:|--:|:--|
| Perfect payer | 10% | 99.5% | 0.00% | Only type that reaches Sovereign |
| Occasional misser | 35% | 93% | 0.46% | Platinum, sometimes Sovereign |
| Alternating misser | 12% | 55% | 1.19% | Gold for life |
| Reducer | 13% | 97% | 0.13% | By record |
| Early lapser | 30% | 60% | 13.25% | Rarely tiers, mostly gone within the year |

A background hazard of **1.06% per month** applies to everyone on top of their own. Add the two for the real monthly chance of leaving: 1.06% for a perfect payer, 14.31% for an early lapser.

### Where these numbers come from, honestly

The five types are not observed customer segments. They are a story built to reproduce a curve.

The curve is the **persistency curve**, which is how many customers are still paying as time passes. Ours runs 63% at month 13, then 49, 41, 34 and 29% at months 25, 37, 49 and 61.

The five types were then tuned until they reproduced that curve together. That is a standard technique, and it is only as good as the curve underneath it.

### What the curve is anchored to

The closest published comparable is **Indian life insurance persistency**, which regulators measure at exactly the same checkpoints.

For FY2024-25, the IRDAI Handbook on Indian Insurance Statistics reports **13th month persistency ranging from 59.68% to 83.22%** across life insurers, with an **industry average of about 63%**.

**We take that 63% as the month-13 anchor.**

| Checkpoint | Indian life insurance | This model |
|:--|:--|--:|
| 13th month | industry average about **63%** | **63%** |
| 61st month | LIC on a policy basis, **49.9%** | **29%** |

### Why we take the level and reject the shape

Indian life persistency barely falls after year one. LIC loses about 36% of policyholders in the first year and only another 14% across the next four.

That flatness is bought by lock-in. Surrender penalties, a death benefit you forfeit, years of sunk premium. Quitting an Indian life policy in year three is expensive.

**Aurumix has none of that.** Stop paying and you keep your gold. No penalty, nothing forfeited. There is no reason our curve should flatten the way theirs does, so ours keeps a steeper decline to 29% at month 61.

### How the hazards were set

Every archetype hazard was multiplied by a single factor, 0.6624, until month-13 persistency hit 63%.

One factor, not five free parameters. Fitting the five weights or the five hazards independently reproduced the curve perfectly and produced a nonsense population, in one case 52% alternating missers and no occasional missers at all. A single scale factor keeps the mix and the ordering between archetypes exactly as they were.

### Rail

The rail is how the customer pays. Aurumix launches with two, and they demand different things every month.

On Request to Pay the customer taps to approve each payment. On the prefunded balance they load once and the balance draws automatically.

The rulebook makes the distinction itself. It only allows "set and forget" to be promised on the prefunded balance. So a prefunded customer draws from an archetype mix tilted toward discipline.

Thirty percent of customers start prefunded. Of those, 35% are re-drawn into the disciplined archetypes. Both numbers are swept.

### Door

The door is whether the customer arrived through a monthly SIP or a one-off spot purchase. Spot buyers can now hold a card, so a spot-only customer is worth more than the entry fee alone.

---

## 4. The gate and the score

The loyalty system is called ICS. It decides which benefit tier a customer sits in. Every tier discount reads it. This section explains how it is computed.

### The gate

Nothing happens until the gate. A customer earns Confirmed SIP status on their sixth consecutive counted month.

A counted month is one accepted payment at or above the floor. A miss resets the streak to zero.

That single rule is why tier arrival is a distribution and not a date. A customer who misses month four cannot qualify before month nine.

### The three facts

Once gated, the score is computed from three facts on the payment and token ledgers.

**Months** is the count of counted periods since the qualifying run began. It starts at six on gate day. It never falls.

**Recent** is the count of counted periods in the trailing twelve calendar months. It runs from zero to twelve.

**Sold** is the share of gold the customer had a year ago that they no longer hold.

### Record, from Months

Record rewards how long the customer has been saving. Two linear segments with a kink at month twelve:

$$\text{Record}(m) = \begin{cases} m \times \tfrac{50}{12} & m \le 12 \\[4pt] 50 + (m-12)\times\tfrac{50}{48} & 12 < m \le 60 \\[4pt] 100 & m > 60 \end{cases}$$

Where:

- $m$ is Months, the counted periods since the run began

In one sentence. The first year takes you to 50. The next four years take you from 50 to 100.

### Standing, from Recent

Standing rewards whether the customer is saving now. One straight line:

$$\text{Standing} = \text{Recent} \times \tfrac{100}{12}$$

Twelve of the last twelve months scores 100. Six of twelve scores 50.

### Retention, from Sold

Retention is a multiplier, not a component. It has veto power:

$$\text{Retention} = \begin{cases} 1 & \text{Sold} \le 0.30 \\[4pt] 1 - \dfrac{\text{Sold} - 0.30}{0.70} & \text{Sold} > 0.30 \end{cases}$$

Where:

- Sold runs from 0 to 1, recomputed monthly against the gold held twelve months earlier plus gold bought since

Sell up to 30% of your gold in a year and nothing happens. Past that, the score falls in proportion, to zero if you empty the account.

### The score

The score is the smaller of Record and Standing, scaled by Retention:

$$\text{ICS} = \min(\text{Record}, \text{Standing}) \times \text{Retention}, \quad \text{floored at } 25 \text{ once gated}$$

The minimum is the arithmetic of "and". A long record cannot cover a dead year. A good year cannot cover a short record.

That is why the alternating misser caps at Gold forever. Their Recent never climbs above six. So Standing never climbs above fifty. No amount of tenure lifts it.

### The tiers

Tiers threshold the score at 25, 50, 75 and 100. A perfect payer reaches Silver at month six, Gold at twelve, Platinum at thirty-six and Sovereign at sixty.

The Phase 4 model could not carry this formula. It used a lookup instead, and the lookup put every rung six months late. The simulation computes the real thing.

---

## 5. What a tier buys

### The benefit ladder

Five benefits, each priced by tier. The base case:

| Benefit | None | Silver | Gold | Platinum | Sovereign |
|:--|--:|--:|--:|--:|--:|
| Entry fee paid | 5.00% | 4.50% | 4.00% | 3.50% | 3.00% |
| Family plan discount | 0% | 10% | 20% | 35% | 50% |
| Card FX margin charged | 2.0% | 2.0% | 1.5% | 1.25% | 1.0% |
| Credit line, loan to value | 50% | 50% | 65% | 72.5% | 80% |
| Gold rewards, share of card spend | 0 | 0.15% | 0.45% | 0.60% | 0.75% |

Three rows come straight from the mechanism design. The entry-fee row takes the full 2.0 point ceiling the design allows and steps it evenly. The middle rungs of the FX and loan-to-value rows are interpolated.

### Three dials

The whole ladder is generated from three dials so it can be swept.

**Ceiling** is how much the top tier gets.

**Steepness** is how much of that the lower tiers get. Top-loaded, linear, or front-loaded.

**Breadth** is which benefits are laddered at all.

Three dials are something a client can argue about. Twenty independent rates are not.

### The reward cap

Gold rewards carry one rule that only an agent model can enforce. A customer's rewards never exceed the revenue that customer generated.

The revenue model applies a rate to aggregate card revenue. It cannot see the cap.

### Loan-to-value is different in kind

The loan-to-value row is not a discount. It gives leverage. A Sovereign customer borrows against 80% of their gold. A Silver borrows against 50%.

That raises revenue and raises risk at the same time. It is the row that drives the credit-book results in Section 10.

---

## 6. Four independent clocks

### One churn rate in the revenue model

The revenue model has one churn rate. A customer stops paying and becomes a holder who keeps their gold.

That collapses several behaviours into one. It then needs a switch to say whether holders keep their card.

### Four clocks in the simulation

The simulation separates them. A customer can do four things independently.

- Stop paying the SIP.
- Let the card go dormant.
- Repay the credit line.
- Redeem the gold.

Each has its own clock. Stopping the SIP does not stop the card.

This is the client's own framing, that it may be churn of a feature rather than of the platform. It turns a coin-flip switch into a rate that can be argued about.

### Card dormancy has no source

Card dormancy has no published rate anywhere. I looked. Not for the UAE, not for the Gulf, not for fintech cards globally. Only definitions of inactivity exist.

So it is carried as an assumption and swept from zero to 2% per month.

---

## 7. Gold, partners and the draws

Three things are random at the path level, on top of customer behaviour.

### Gold

Gold follows geometric Brownian motion, sampled monthly:

$$P_{t+1} = P_t \cdot \exp\left[(\mu - \tfrac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\cdot Z_t\right]$$

Where:

- $P_t$ is the gold price in USD per gram at month $t$, starting at 141.50
- $\mu = 8.1\%$ is the annual drift, the same appreciation the revenue model uses
- $\sigma = 15\%$ is the annual volatility, the long-run realised figure for gold, swept from 10% to 22%
- $\Delta t = 1/12$
- $Z_t$ is a standard normal draw

There is one gold path per run. It hits every customer at once.

The client chose not to hedge. Aurumix owns the price variance on the gold it holds.

### Partners

Partner arrivals replace the revenue model's straight line of one to eleven B2B partners.

Each year's planned net adds become a Poisson draw, with a 25% chance of a dead year. Eleven enterprise deals cannot be a smooth curve, and the client has no pipeline yet.

### Everything else

Every other uncertain input is drawn once per path from a distribution anchored on the revenue model's own scenario table.

The base value is the mode. The Aggressive and Conservative values are treated as the tenth and ninetieth percentiles of a PERT distribution.

That grounds every draw in a range the client has already seen and signed. It also means the median path lands below base, because the client's own ranges are wider on the downside. That is not a modelling choice. It is what their scenario table says.

### Which inputs are drawn

**Seventy-four parameters.** Every input in the workbook that carries an Aggressive and Conservative value is drawn. Persistency, the three regional acquisition costs, referral behaviour, spot behaviour, the whole card programme, every fixed cost, the licence fees, the vault contract, and the contingency.

The rule is opt-out rather than opt-in. If the client has priced a range for something, that range belongs in the raise number. Eleven parameters are excluded and each carries a written reason, mostly because they are computed elsewhere: the partner count is a discrete arrival process, the gold band is carried by the price process, and the four loyalty discount rates are computed from the tier mix.

---

## 8. What happens each month

This is the core loop. Every month, in this order.

### The twelve steps

1. **The gold price advances** one step along the path.
2. **New customers arrive** from the acquisition engine: marketing reach at that month's cost per customer, agents, and referrals scaled by the book's referral capacity, all against the addressable ceiling. Each is assigned a region, ticket, archetype, rail and door.
3. **Each living customer decides whether to pay**, at their archetype's probability.
4. **Each paying customer decides how much**, around their ticket, floored at USD 20.
5. **The streak updates.** A payment adds one. A miss resets to zero. Anyone reaching six passes the gate.
6. **The score and tier are recomputed** from Months, Recent and Sold.
7. **Gold accumulates** at the current price, net of the entry fee at the customer's tier rate.
8. **Cards are taken up** by a share of the eligible book. Spend runs against the credit limit at the tier's loan-to-value. Rewards are paid up to the cap.
9. **Family plans attach** on new customers and cancel at the workbook's rate.
10. **Redemptions and moves to self-custody** drain gold.
11. **The four clocks tick.** SIP lapse, card dormancy, credit repayment, exit.
12. **The aggregates flow through the ported revenue model.** Revenue by stream, the fabrication premium, the vault, the licences, acquisition cost, the card programme, contingency, net profit, capital tied up, and the funding line. The loyalty giveback is priced from that month's computed tier mix rather than a flat rate.

### Two rules on redemption

Money paid after the five-day grace is a spot purchase, not a late contribution. It earns the fee. It buys gold at that day's price. It does not restore the streak.

Redeemed gold refills the float. Any excess above what new buyers absorb that month is sold back to the dealer at a two-way spread. The spread is swept at 0.5%, 1% and 2%.

---

## 9. The float as inventory

### Why the float exists

Aurumix has to own gold before customers do, so that a gram is allocated the moment a payment lands.

The revenue model sizes that float as one bar plus ten days of average demand. The ten is a guess. The float earns no line in the profit and loss.

### How the simulation sizes it

The simulation treats the float as an inventory problem at daily resolution.

Sixty percent of a month's SIP volume lands in the five days after payday. Spot purchases arrive as random lumps.

Because SIP payments are scheduled, the float is positioned before the payday cluster. It reads the calendar rather than reacting to history:

$$S_d = \sum_{k=1}^{L} D_{d+k} \;+\; z_{0.99}\,\sigma_{\text{spot}}\sqrt{L} \;+\; 100, \quad \text{rounded up to whole bars}$$

Where:

- $S_d$ is the order-up-to level in grams on day $d$
- $D_{d+k}$ is the scheduled SIP demand $k$ days ahead
- $L = 2$ is the dealer's delivery lead time in days, swept from 1 to 5
- $z_{0.99}$ is the normal quantile for a 99% service level
- $\sigma_{\text{spot}}$ is the standard deviation of the unscheduled spot demand
- $100$ is one bar, held as a buffer

### The rules around it

Orders arrive after the lead time, in 100 gram bars. The float never falls below two bars.

It is marked to market daily on the gold path. It carries a cost of 6% a year, swept from 4% to 8%. Unhedged.

### What the first version got wrong

A first version of this policy used a rolling history for safety stock. It ran out of gold on 7% of days, because it reacted to payday after payday hit.

The calendar version runs out on 0.3% of days.

---

## 10. The credit book under a moving price

### Vintages

Margin calls are a property of when a loan was struck and at what loan-to-value.

So drawn balances are tracked by vintage. Each vintage carries the gold price on the day it was drawn.

### The call condition

A vintage is called when the current price falls far enough that the loan exceeds 85% of the collateral's value:

$$\frac{P_t}{P_0} < \frac{\text{LTV}_{\text{struck}}}{0.85}$$

Where:

- $P_0$ is the gold price when the vintage was drawn
- $P_t$ is the price now
- $\text{LTV}_{\text{struck}}$ is the tier's loan-to-value at origination
- $0.85$ is the call line, taken from the client's own worked example and swept from 0.75 to 0.95

### What it implies

The arithmetic is simple and the consequence is not.

At 50% loan-to-value a call needs gold to fall 41% from the strike. At 80%, the Sovereign rung, it needs 6%.

---

## 11. The threshold

### Steady state

The question the client asked is what it takes to be profitable. The simulation answers it at steady state, where the book is flat and acquisition only replaces churn.

### Retail and partners, kept apart

The fixed cost base has to be covered by retail customers or by B2B partners. The two are computed separately:

$$N^* = \frac{k \cdot F}{r - k\,(s + c \cdot \text{CAC})} \qquad\qquad K^* = \frac{k \cdot F}{A \cdot f}$$

Where:

- $N^*$ is the number of paying retail customers that covers fixed costs on their own
- $K^*$ is the number of B2B partners that covers fixed costs on their own
- $F$ is the annual fixed cost base, about USD 430k
- $k$ is one plus the contingency, swept at 15%, 30% and 50%
- $r$ is retail revenue per paying customer per year, about USD 38 excluding B2B
- $s$ is the serving cost per customer, about USD 11
- $c$ is annual churn, 37%
- CAC is the cost to replace one customer, USD 40 blended or USD 55 in the UAE alone
- $A$ is assets under management per partner and $f$ is the platform fee

### Why apart

Blending B2B revenue into a per-customer figure hides whether the retail business stands on its own. It does not. Part 2 of the results document is about that.

---

## 12. Stress scenarios

Seven scenarios, each run against the base.

**Gold crash.** A 30% fall from month 24 onward. Tests the credit book and the collateral base.

**Redemption run.** A quarter of custody exits in month 24 while existing customers cut contributions to 40% of normal. A run is a jump, not a rate. A rate-based redemption model converges toward balance with inflows and never overshoots, so the run has to be built as a discrete event.

**Zero B2B.** No partners, ever. Tests whether the retail business stands alone.

**Adoption failure.** Persistency at 45%, acquisition costs at the conservative end, and fewer customers reaching a tier.

**Regulatory delay.** Twelve months of licences, insurance, audit and technology build with no revenue. VARA publishes no approval timeline.

**Ticket compression.** Every regional ticket at its conservative value.

**Combined tail.** The crash, the run and a B2B slump together.

---

## 13. What was verified and how

Two gates had to pass before any result was reported.

### Gate one: the population engine reproduces the research

The population engine reproduces the Phase 4 research figures when given the Phase 4 inputs. The alternating misser's 24% chance of ever reaching six in a row. The mean gate month of 8.1. The persistency curve at every anchor. Thirty-four checks.

That proves the code is right. It proves nothing about Aurumix, because those figures came from the same unsourced archetype mix.

### Gate two: the port reproduces the workbook

The ported revenue model reproduces the calculated workbook. Thirty-six series, all twenty-nine periods, zero error.

That is what makes the simulation an extension of the model rather than a rival to it.

### The standing audit

Two gates prove the model is right on the day it is built. They do not stop a later change from quietly breaking something.

So a third check runs after every change. It asserts that every priced range reaches the Monte Carlo, that the tier mix reaches the pricing engine, that derived quantities move when their inputs move, that departures from the workbook are declared, that the benefit ladder is internally consistent, and that the acquisition block still responds to the model rather than to a fixed formula.

It exists because each of those failed at least once during the build, and none of them announced itself.

### One figure deliberately not chased

The Phase 4 research put Sovereign at 1.2% of tiered accounts. That number came from the lookup that capped the occasional misser at Platinum by construction.

Under the real formula a clean trailing year plus sixty counted months scores 100, and it should. In the simulated book Sovereign lands at 1.1% anyway.

---

## 14. Assumptions and limits

### The demand side is judgement

The cost side is well sourced. VARA and DMCC fee schedules, the KYC provider's price list, the Visa interchange schedule, Zand's banking tariff.

The demand side is weaker. The market funnel filters are made up. No client data exists.

The persistency curve is anchored to the Indian life insurance industry average at month 13, measured at the same checkpoints. Its decline after year one is ours, and is steeper than a life curve because Aurumix has no surrender penalty. The split of that curve into five behavioural types remains unsourced and is swept.

Every one of those is swept rather than assumed. The profitability threshold is built so that it does not depend on the funnel at all.

### Contingency stands in for headcount

Staff, legal, security and tax are not modelled. A 15% contingency on all costs is the placeholder. It is swept to 50% so the threshold can be read against the cost that is not yet built.

### B2B is a straight line with noise

Partner economics rest on one observed anchor, O Gold's 75,000 active users, and a lumpy arrival process. There is no pipeline to calibrate to.

### The buyback spread is second order

It is in the model and swept. At every run size tested it costs a few thousand dollars. What hurts in a run is customers pausing their contributions.

### Gold volatility is from general knowledge

Fifteen percent is the long-run realised figure. It is not a fetched citation. It is swept.

### Not modelled

No competitive response. No regulatory change. No intra-month price moves, so margin calls are tested monthly. No hedging, by client decision. The supply side is a separate phase.

---

## 15. Running the simulation

### The commands

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

### What each does

The first script reads every parameter from the calculated workbook into a JSON file, so the port cannot drift by transcription.

The two verification scripts must pass before the rest means anything.

The remaining scripts run the Monte Carlo, the analysis, the float model, and the charts.

### Reproducibility

Every script uses fixed seeds. Every figure in the results document can be regenerated.

Outputs are written to `outputs/`, charts to `outputs/charts/`. Total runtime is under ten minutes.
