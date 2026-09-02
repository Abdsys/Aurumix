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
| Redemption run ×5 | +976k | +1,301k | 2.30m |
| **Zero B2B** | **−713k** | **−4,048k** | **5.50m** |
| Adoption failure | +723k | +254k | 2.37m |
| Regulatory delay 12mo | +847k | +316k | 3.03m |
| Ticket compression | +732k | +662k | 2.30m |
| **Combined tail** | **+125k** | **−1,687k** | **3.18m** |

⚠ **The redemption run showing a profit is a model limitation, not a finding:** returned gold recycles into the float and cuts COGS, and **the two-way buyback spread is not modelled** (open question in the brief §10). Read it as "the P&L doesn't break," not "runs are good." The cash-out mechanics belong to the spread question the client hasn't answered.

## 4. Assumptions made on my own authority (all swept)

| Assumption | Value | Basis |
|---|---|---|
| Gold volatility | 15%/yr, swept 10–22% | Long-run realised gold vol (WGC/LBMA data range) |
| Margin-call line | 85% current LTV, swept 75–95% | Client doc §9.3's own worked example |
| MC parameter distributions | PERT with Base=mode, Agg/Cons≈p10/p90 | The workbook's own scenario triples — spreads the client has already seen |
| B2B arrivals | Poisson on planned net adds, 25% chance of a dead year | Lumpiness judgement; the tornado shows it matters |
| Rail discipline gap | 35% re-draw to disciplined mix, swept | Unsourced by construction; the lever result reads directionally |
| Acquisition noise | 10% CV lognormal | Demand-noise convention |

## 5. What remains before client documentation

1. **Your review of this summary** — especially the B2B finding's framing (escalation rule: it's close to the "structural" line we agreed).
2. `SIMULATION_SETUP.md` + `SIMULATION_RESULTS.md` to the Stockpile standard (charts included).
3. Card dormancy hazard and the interchange gross-vs-effective split — researched, then a re-run (both are second-order against the B2B finding).
4. Phase 4 fix list stands as logged (redemption unit cost $1.85→$3.28, the tiered-vs-spot discount, the payment filter).
