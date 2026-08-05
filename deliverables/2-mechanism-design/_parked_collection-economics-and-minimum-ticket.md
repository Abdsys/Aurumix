# PARKED: Collection Economics and the Minimum Ticket

> **Status: parked 2026-08-06 at Abdur's instruction.** Extracted from `_draft_purchase-structure.md` so that draft stays on SIP and spot mechanics. **Nothing here is retracted.** The research is verified to the confidence levels stated and this reopens whenever the minimum ticket is back in scope.
>
> **Why it was parked, not deleted:** it changes a number in `_draft_allocation-and-float.md` that is currently wrong, and it removes a payment rail the client's document still assumes. Both will resurface in Phase 4.

## 1. The finding

`_draft_allocation-and-float.md` assumes a payment rail costing **0.30% of the contribution**. UAE direct debit is not priced as a percentage. It is priced as a **fixed fee per debit**, published by Emirates NBD at **AED 5 per item** for an originator collecting up to 2,000 items a month, falling to AED 3 and then AED 2 at higher monthly volumes.

On a USD 75 contribution AED 5 is **1.81%, not 0.30%**. On USD 20 it is 6.8%. The build-up understates the rail by a factor of 6 at the target ticket and more than 20 at the minimum.

## 2. The equation

> **Net = C × (f − c) − R**
>
> **C_min = R ÷ (f − c)**
>
> **C** contribution, **f** entry fee rate, **c** variable cost rate (fabrication premium + price-gap risk + float cost of capital), **R** fixed cost of one collection event.

| Term | Y1 | Y3 | Y10 |
|---|---|---|---|
| **f** entry fee | 5.00% | 4.00% | 3.00% |
| **c** fabrication premium | 3.00% | 2.00% | 0.75% |
| **c** price-gap risk (1σ) | 0.36% | 0.15% | 0.28% |
| **c** float cost of capital | 0.49% | 0.31% | 0.38% |
| **f − c** margin available for the rail | **1.15%** | **1.54%** | **1.59%** |

**Break-even contribution:**

| Per-debit price | USD | Y1 | Y3 | Y10 |
|---|---|---|---|---|
| AED 2 | 0.54 | **USD 47** | USD 35 | USD 34 |
| AED 3 | 0.82 | USD 71 | USD 53 | USD 51 |
| AED 5 | 1.36 | **USD 118** | USD 88 | USD 86 |
| AED 10.50 | 2.86 | **USD 249** | USD 186 | USD 180 |
| AED 1 (negotiated) | 0.27 | USD 24 | USD 18 | USD 17 |

**At the client's stated numbers, Year 1, AED 5 per debit:**

| Contribution | Margin at 1.15% | Rail | Net | % of contribution |
|---|---|---|---|---|
| USD 20 (stated minimum) | 0.23 | (1.36) | **(1.13)** | **(5.66%)** |
| USD 75 (stated target) | 0.86 | (1.36) | **(0.50)** | **(0.67%)** |
| USD 100 | 1.15 | (1.36) | (0.21) | (0.21%) |
| USD 118 | 1.36 | (1.36) | 0.00 | break-even |
| USD 150 | 1.73 | (1.36) | 0.36 | 0.24% |

> 🔴 **At the client's own target contribution, own fee ceiling and own Year 1 investor count, the SIP loses money on every collection.** Not at the minimum. At the target.

## 3. Card is not expensive, it is arithmetically impossible

UAE card acceptance runs about **2.2% to 2.9% plus AED 1**. The percentage component alone (about 2.55%) is more than double the 1.15% margin available at Year 1, so the coefficient on C is negative and **the loss grows with ticket size**.

| Contribution | Margin | Card cost | Net |
|---|---|---|---|
| USD 75 | 0.86 | (2.19) | (1.32) |
| USD 500 | 5.75 | (13.02) | (7.27) |
| USD 5,000 | 57.50 | (127.77) | (70.27) |

An entry fee of **6.4% or more** would be needed before a card-funded purchase breaks even at Year 1. That is outside the client's stated 2 to 5% range.

**Conclusion: card is not a funding rail for either lane.** It survives as the Gold Card (payments out) and as a credit product. This is stronger than the existing "cards must not be the SIP default" in `_explainer_how-we-take-money.md` §6.

⚠ The only route that would keep card alive is surcharging the customer. Card scheme rules generally prohibit it and CBUAE has a view. **Unchecked.**

## 4. The eight factors that set a minimum

| # | Factor | Effect | Binding? |
|---|---|---|---|
| 1 | Fixed cost per collection event | Sets C_min directly. AED 2 to 10.50 moves it USD 47 to USD 249 | **Yes, dominant** |
| 2 | Entry fee headroom (f − c) | The divisor. 1.15% at Y1 | **Yes** |
| 3 | Per-account fixed costs: KYC, screening, statements | Amortised over customer life, not per contribution. **Unquantified** | Probably |
| 4 | Custody as a charge on stock | Grows with balance, not ticket. Argues for a minimum *balance* | Indirect |
| 5 | Bar denomination and the float | **None.** The float exists to remove this constraint | **No** |
| 6 | Token divisibility | **None.** 18 decimals | **No** |
| 7 | Market anchor | Indian MF SIP minimum ₹500 (~USD 6), micro-SIPs ₹100. Digital gold from ₹1 to ₹10. **USD 20 is already 3x the Indian norm** | Sets the credible ceiling |
| 8 | The ICS constraint in the SIP draft §6.20 | "A USD 20/month saver who never misses must reach the top tier." Raising the minimum rewrites this test | **Yes, on the design** |

Factors 5 and 6 are the intuitive answers and both are wrong. The float already solved lumpiness. **The minimum is a bank-tariff constraint, not a gold-market constraint.**

## 5. The recommendation that was parked

Keep **USD 20 per month** as the minimum contribution and the marketing headline. Set a **minimum collection event of USD 60**, collecting quarterly below that so one rail event buys three periods of gold.

> 🔴 **The contingency, which is the weak joint.** USD 60 monthly clears break-even **only at AED 2 per debit**, and AED 2 is the 10,001-items-per-month band that Year 1 at 500 investors will not reach. On published tariffs alone there is no viable monthly UAEDDS collection below about **USD 118** at launch. The USD 60 recommendation rests on either a negotiated rate at launch volumes or the AANI path, and **neither is confirmed**.

⚠ **The product cost of quarterly collection, stated honestly.** One quarterly purchase carries roughly 1.7x the timing dispersion of three monthly ones at 15% annualised gold volatility. **That removes the dollar-cost-averaging benefit which is the entire point of a SIP.** It disappears entirely on a near-zero-cost rail.

## 6. Open items this parks with it

**[BANK] Not answerable at a desk.**
- Actual per-debit price for a UAEDDS originator at 500 to 15,000 small items a month. Moves the viable minimum from USD 47 to USD 249.
- What AANI costs a business to receive, via which PSP or bank. Undisclosed everywhere.
- When AANI **electronic direct debit** goes live. Announced, not shipped.

**[CLIENT]**
- Per-account fixed costs: KYC unit cost, ongoing screening, support per account. Factor 3 is the last unquantified input.
- Acceptance that card is not a funding rail.

**[US]**
- **Verify the Emirates NBD UAEDDS tariff by hand.** Two research passes returned different figures for the same schedule: AED 26.25 versus AED 315 for mandate registration, AED 5 per item versus AED 10.50 per record. The per-item volume bands are internally coherent and were used as the planning figure, but this is **Medium confidence and the whole minimum rests on it.**
- Pull two more UAE bank business tariffs. Only Emirates NBD publishes.
- Confirm whether card surcharging is permitted under CBUAE and scheme rules.

## 7. Sources

| Claim | Source | Confidence |
|---|---|---|
| ENBD UAEDDS: AED 3,150 CBUAE registration; AED 5 / 3 / 2 per item by volume band; AED 50 reversal | Emirates NBD Business Banking Schedule of Charges | **Medium.** Two passes disagreed on adjacent lines |
| UAE card acceptance 2.2 to 2.9% + AED 1 | UAE merchant pricing guides, 2026 | **Medium.** Consistent with the ~4.25% already in decision 28 |
| UAE domestic debit interchange capped at 1.00% / AED 50 | Network International published fee structure | **Medium-High** |
| Indian MF SIP minimum ₹500, micro-SIPs ₹100 | Multiple Indian platform sources | **High** |
| AANI merchant pricing | **Not published anywhere.** Assumed materially below UAEDDS on how instant A2A schemes price globally | **Assumption, not a finding** |

## 8. What stays owed to other drafts when this reopens

- [ ] `_draft_allocation-and-float.md`: replace the flat **0.30% payment rail** line with a per-channel fixed cost, and re-run the worked example and the Y1/Y3/Y10 fee table.
- [ ] `_draft_allocation-and-float.md`: the Year 1 net contribution margin of **~1.00% on USD 75 is wrong**. It is **−0.67%** at AED 5 per debit.
- [ ] `_explainer_how-we-take-money.md` §6: card is removed as a funding rail entirely, not demoted from default.
