# Aurumix Simulation — Verification Summary

**Date:** 2026-09-02 · **Status: built and verified, for review before documentation.**
**Code:** `deliverables/5-simulations/aurumix/` · every figure reproducible from fixed seeds.
**Reference of record:** `4-revenue-modeling/tools/Aurumix_Revenue_Model_calculated.xlsx`.

---

## 1. What was built

Three stages, per the blueprint:

| Stage | What it is | Verification gate | Result |
|---|---|---|---|
| **1 — Population engine** | ~200k agents (1 sim agent = 2–4 customers), each with ticket, archetype, rail, door; monthly pay/miss; the run-of-6 gate; **the real ICS formula** `min(Record, Standing) × Retention` | Reproduce v2.6's published figures given v2.6's inputs | **34/34 checks pass** |
| **2 — Full book** | A formula-for-formula Python port of the workbook (all streams, costs, capital, float) + gold GBM + lumpy B2B arrivals + PERT parameter draws anchored on the workbook's own scenario triples | Pinned to Base, reproduce the calculated workbook | **36/36 series match at 0.0000% across all 29 periods** |
| **3 — Solver** | Steady-state profitability threshold, ICS ladder envelope (3 dials), decile concentration, rail sweep, tornado, 7 stress scenarios, 2,000-path Monte Carlo | Internal sanity checks + invariants every step | **All pass** |

**Verification vs validation was kept strict:** Stage 1's targets prove the first-passage arithmetic, not the business; the archetype mix and persistency are swept in the MC, never assumed.

## 2. Bugs found and fixed during self-verification

| # | Defect | Fix |
|---|---|---|
| 1 | The doc's 4-dp slopes (4.1667/8.3333) left Standing(12)=99.9996, making Sovereign unreachable by rounding | Exact fractions 50/12, 100/12 |
| 2 | Ticket noise drew sub-floor amounts and rejected them, double-counting misses against archetype pay-probabilities fitted with no such channel | Declared amount = max(floor, base×noise); paying at all stays the archetype's job |
| 3 | v2.6's "0.60 falling" early-lapser fits its own published figures **worse** the more it falls | Flat 0.60 — reproduces 2.6%/M8.6/~90%-gone almost exactly; discrepancy is in v2.6's prose |
| 4 | First threshold method treated acquisition as a per-customer serving cost | Steady-state: acquisition replaces churn only (N × 45%/yr × blended CAC) |
| 5 | Regulatory-delay stress kept marketing running while unlicensed | Delay costs = standing costs only (licences, insurance, audit, tech build) |
| 6 | Agent book never cancelled family plans (workbook churns them at 7.11%/mo), overstating flat-priced revenue ~3× and flattening decile concentration | Monthly cancellation applied; family revenue now ties to the workbook |
| 7 | ρ_quality didn't load on ticket, so the clustering sweep couldn't move deciles | Gaussian-copula loading, marginals untouched |

**One target was withdrawn, not chased:** v2.6's "Sovereign ≈ 1.2% of tiered" is an artifact of its lookup capping the occasional misser at Platinum. Under the rulebook's actual formula, a clean trailing year + 60 counted months legitimately scores 100. (In the continuously-acquired book Sovereign lands at **1.1%** anyway — the dilution does what the cap faked.)

## 3. Headline results

### Q1 — What does it take to be profitable? *(steady state, no market ceiling involved)*

⚠ **Corrected after self-audit.** My first cut spread B2B revenue per customer. B2B does not scale with customers — it is a fixed block that scales with *partners*. So the fixed cost base ($430k/yr) is covered **either** by N retail customers at their unit margin **or** by K partners. Reporting a blend hides whether retail stands alone. It does not:

Retail revenue **$41**/payer-yr · serving **$13** · churn **45%/yr** · CAC blended **$37** (India-agent heavy) or UAE-only **$55**:

| Contingency | Retail alone, blended CAC | Retail alone, UAE CAC | **or** partners covering fixed costs by themselves |
|---|---|---|---|
| 15% | **76,000** paying | **unreachable** | **3.5** |
| 30% | 283,500 | unreachable | 3.9 |
| 50% | unreachable | unreachable | 4.5 |

**The retail unit margin at 15% contingency is ~$6 per customer per year.** At UAE acquisition cost it is negative — a UAE retail customer does not pay for their own replacement. The O Gold cross-check (75,000 active users in the UAE) sits *at* the blended-CAC threshold, not comfortably above it.

**Three and a half partners cover the entire fixed base.** Which leads to—

### The single largest finding: the business as modelled is a B2B bet

- Tornado ranks 1–2–4: **partner adoption, partner AUM/user, B2B fee** — partner adoption alone swings Y7 profit by **$1.8m** (more than the entire Y7 profit).
- Stress "zero B2B": Y7 **−$713k**, cumulative **−$4.0m**, peak funding **$5.5m**.
- And the client has **no partner pipeline** (confirmed 2026-09-02). A third of revenue, and the profitability threshold's reachability, rest on deals not yet begun.

### Q4 — The raise (2,000 paths, everything varying at once)

| | |
|---|---|
| **Safe raise (90% of paths covered)** | **$4.70m** |
| p50 / p80 / p95 | $2.82m / $3.93m / $5.15m |
| P(need > $3m) | 43% |
| Workbook's point estimate | $2.29m — **roughly the median, i.e. a coin-flip raise** |
| P(cumulative break-even by Y7) | **38%** (by Y6: 28%) |

### Q2 — Tier mix and the ICS envelope

Tier mix at M84 (the thing the workbook cannot compute): **Silver 45.6% / Gold 41.7% / Platinum 11.5% / Sovereign 1.1%**; gated share 50.4% vs the workbook's typed 55%.

The ladder envelope (cumulative 84-mo cost, % of agent revenue) confirms the shape prediction:

| Ceiling ↓ / Shape → | Convex (top-loaded) | Linear | Concave (generous early) |
|---|---|---|---|
| 1.0pp | 4.7% | 8.2% | 13.4% |
| 1.5pp | 5.6% | 9.8% | 16.2% |
| 2.0pp | **6.5%** | 11.4% | **19.0%** |

**Steepness costs ~3× more than ceiling.** The client can advertise "Sovereign pays 3%" (full 2.0pp ceiling) for 6.5% of revenue if the ladder is convex — versus 19% if it's generous early. The marketing headline is nearly free; the early rungs are where the money goes.

### Q3 — Concentration, the rail, the spot door

- **Top ticket decile = 21.7% of profit; top three = 44.9%** (ρ_quality 0.6 nudges it to 22.4/45.8 — clustering matters less than the ticket spread itself, a useful negative).
- **Survivorship, the structural finding:** early lapsers are 27% of acquisitions and 4.4% of the M84 paying book; the surviving book is **+24% vs the workbook's flat-churn projection**. Heterogeneous churn means the Excel *understates* the mature book.
- **Rail mix is a real lever:** prefunded share 0→75% lifts gate share 47.0%→55.3%, adds ~10k paying at M84 and ~$465k of cumulative entry revenue — at onboarding cost, not marketing cost.
- **Spot door:** with the card open to everyone, a spot-only customer pays back CAC in **1.9 years (UAE) / 0.5 years (India)** on spot economics alone — the 21 Aug deletion (6–8yr payback) is decisively reversed by the 26 Aug card decision.

### Q5 — Gold and the credit book

- **A −30% crash barely moves the P&L** (Y7 −$460): flows repurchase at the new price, so USD-AUM is nearly invariant — v2.6's §14.4a claim, confirmed independently.
- The risk is the **stock**, not the flow — and it is set by the LTV rung. Run at each rung of the ladder (800 paths each, call line 85% current LTV):

| Struck LTV | Rung | Gold move that triggers a call | P(any call in 7 yrs) | Share of originations called, p50 / p90 |
|---|---|---|---|---|
| 50% | Silver / workbook flat | −41% | **4.5%** | 0% / 0% |
| 59% | tier-mix weighted | −31% | 19.5% | 0% / 0.7% |
| 72.5% | Platinum | −15% | 84.6% | 4.5% / 17.1% |
| **80%** | **Sovereign** | **−6%** | **100%** | **28.4% / 43.8%** |

**At Sovereign's 80% LTV a margin call is certain within the horizon and over a quarter of the book gets called in the median path.** The LTV ladder is the credit-risk decision of the whole design — and it is the one benefit the workbook does not carry (flat 50% for everyone). The counter-argument is that Sovereign is 1.1% of tiered accounts; the response is that they are also the largest balances.

### Stress table (Y7 profit | cumulative | peak funding)

| Scenario | Y7 | Cum Y7 | Peak funding |
|---|---|---|---|
| Base | +847k | +1,055k | 2.29m |
| Gold crash −30% | +846k | +1,053k | 2.29m |
| **Redemption run** — 25% of custody exits at M24, contributions pause to 40%, sell-back at 1% | **+472k** | **−254k** | 2.34m |
| **Zero B2B** | **−713k** | **−4,048k** | **5.50m** |
| Adoption failure | +723k | +254k | 2.37m |
| Regulatory delay 12mo | +847k | +316k | 3.03m |
| Ticket compression | +732k | +662k | 2.30m |
| **Combined tail** — crash + run + B2B slump | **−379k** | **−3,231k** | **4.22m** |

**The redemption run, resolved (client challenge 2026-09-02).** The first cut showed a run *raising* profit. Decomposed line by line, the client's intuition was right on every line it named — card and lending revenue −$60k, handling +$124k, AUM −39% — but one line swamped them: **COGS −$212k**, because the workbook pays the fabrication premium only on net-new grams and treats every redeemed gram as a bar it need not make. Three things were then established and are now in the model:

1. **A rate-based redemption model cannot produce a run.** Redemptions are a rate on the stock; the stock is built from the flow; the two converge and never overshoot. Even at 5× redemptions and 40% contributions, a growing book buys more gold than it returns (48k vs 44k grams at Y7). **A run is a jump, not a rate** — now a discrete "share of custody exits in one month" hook, swept 10/25/40%.
2. **Excess redemptions are sold back to the dealer at a swept two-way spread** (0.5/1.0/2.0%), the recycling credit capped at that month's purchases. Equivalence at base is untouched (36/36).
3. **The spread is second-order and the pause is the damage.** At every run size and spread tested, sell-back costs $0.7k–6k cumulative; the run's −$375k Y7 hit is lost contributions and AUM. Even a late-horizon worst case — 25% of a 200k-gram book exiting against ~10k of monthly purchases, at 2% — is ~$160k, under 4% of Y7 revenue. **The buyback-spread question the brief marks CRITICAL is real for cash management and immaterial for the P&L; what matters is whether customers keep paying.**

### The float — rebuilt as inventory, unhedged (client decision 2026-09-02)

**Why.** The workbook holds `1 bar + 10 days of average demand`. The 10 is a guess, demand is not smooth, the float is unhedged gold with no P&L line for price moves, and there is no carry cost.

**What was built.** Daily resolution inside every month. Payday clustering (60% of SIP volume in 5 days). Spot as random lumps. An **order-up-to policy that reads the SIP calendar forward** — scheduled demand is known ahead, so the float is positioned *before* the payday cluster, with safety stock only for the unscheduled spot part. Dealer lead time 2 days, 100 g bars, 99% service level. Redemptions refill; excess is sold back at the spread. Daily mark-to-market on the gold path. Carry at 6%/yr. **No hedge — Aurumix owns the variance.**

⚠ **A first version with a rolling-history safety stock ran 6.9% stock-out days** — it reacted to the payday cluster after it hit. A stock-out here means a customer has paid and their gram is not allocated. The calendar-aware policy cuts that to **0.28%** (about one day a year).

| | Workbook rule | Inventory model |
|---|---|---|
| Float at Y7 | **3,406 g** (~$780k) | **441 g average**, peaking at 2,750 g just before payday |
| Stock-out days | not measured | 0.28% |
| Carry cost, 7 yrs cumulative | 0 (not modelled) | ~$24k |
| Mark-to-market P&L, 7 yrs (400 paths) | not modelled | p10 +$1k · p50 +$27k · p90 +$69k; worst single year p10 **−$15k** |
| **Safe raise p90** (same 400 paths) | $4.52m | **$3.81m** |

**Findings.**
1. **The workbook holds ~8× more float than a calendar-aware policy needs.** That is ~$0.7m of the raise that a procurement process can release.
2. **Unhedged is fine at this size.** The float is small, so the price variance is small — a worst year around −$15k against a Y7 profit of $847k. The decision to own the variance costs almost nothing.
3. **The float is a procurement discipline, not a capital item.** What matters is delivery reliability: lead time 1 → 5 days moves the float from 335 g to 718 g, still a fraction of the workbook's figure.

**Assumptions taken, all swept:** lead 2 days (1/3/5), service 99% (95/99/99.9), payday share 60% (40/80), carry 6% (4/8). ⚠ **Dealer terms are the unverified input** — the bullion dealer is still unnamed. A weekly-delivery or minimum-order dealer raises the float materially.

## 4. Assumptions made on my own authority (all swept)

| Assumption | Value | Basis |
|---|---|---|
| Gold volatility | 15%/yr, swept 10–22% | Long-run realised gold vol (WGC/LBMA data range) |
| Margin-call line | 85% current LTV, swept 75–95% | Client doc §9.3's own worked example |
| MC parameter distributions | PERT with Base=mode, Agg/Cons≈p10/p90 | The workbook's own scenario triples — spreads the client has already seen |
| B2B arrivals | Poisson on planned net adds, 25% chance of a dead year | Lumpiness judgement; the tornado shows it matters |
| Rail discipline gap | 35% re-draw to disciplined mix, swept | Unsourced by construction; the lever result reads directionally |
| Acquisition noise | 10% CV lognormal | Demand-noise convention |

## 4b. The two researches, closed 2026-09-02 (Perplexity sonar-pro, then primary-source verification)

**Card dormancy — confirmed sourcing negative.** No published dormancy or attrition *rate* exists for consumer cards in the UAE, GCC, globally, or for fintech-issued cards; only inactivity *definitions* (90 days to 12 months). My blueprint claim that it was "genuinely sourceable" is retracted. Carried as a swept assumption (0 / 1 / 2 % per month) on an independent clock from SIP lapse. **Swept through the agent book:** 2%/month dormancy cuts active cards at M84 by 40% (36,104 → 21,748) and cumulative card revenue by 40%, but total agent revenue by only **0.9%** — the card is a small stream next to the entry fee, so the missing source is harmless to the profitability answer. What it does change is the *credit book*: fewer active cards means fewer margin-callable positions.

**Interchange — settled at primary source.** Visa UAE interchange schedule, effective 19 December 2024:

| Product | Domestic gross rate |
|---|---|
| Prepaid consumer | **1.00%** cap AED 50 — the workbook's prepaid-switch cap is exact |
| Credit Classic / **Gold** | 1.15% / **1.15%** |
| Credit **Platinum** | **1.80%** |
| Credit Signature / Infinite | 2.05% / 2.10% |

⚠ **The workbook's "Interchange – Gold 1.8%" is a Platinum rate under a Gold label.** Logged for Phase 4. The only published brand-share benchmark (Sacra's BaaS unit-economics model, 2021) leaves the brand ~0.28% of spend after network, sponsor bank and programme manager — the workbook keeps 0.72%. Run through the engine, the most conservative take costs **$33k of Y7 profit**. **Stream 2 is too small for the split to matter, and stream 4's 17× dominance is structural** — FX margin and cardholder fees are charged to the customer and never enter the interchange split. Mastercard's UAE schedule is bot-blocked at source and unverified.

## 5. What remains before client documentation

1. **Your review of this summary** — especially the B2B finding's framing (escalation rule: it's at the "structural" line we agreed). **Client documents are paused on your instruction.**
2. `SIMULATION_SETUP.md` + `SIMULATION_RESULTS.md` to the Stockpile standard (charts included), once released.
3. Phase 4 fix list stands as logged (redemption unit cost $1.85→$3.28, the tiered-vs-spot discount, the payment filter, and now the Gold/Platinum interchange label).
