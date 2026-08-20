# Aurumix Revenue Model - Numerical Spine

Generated from the model. Horizon **84 months (7 years)**, computed genuinely monthly, reported on a **29-column view** (M1-M24 monthly, then Y3-Y7 annual).

Every figure on this page is interpolated from the run that produced it. Nothing is typed in.

## 1. Headline, Base scenario

| year | revenue | gross_profit | ebitda | net_profit | live_accounts | holding | aum_usd |
|---|---|---|---|---|---|---|---|
| 1 | 11,477 | 5,237 | -1,376,484 | -1,376,484 | 513 | 689 | 171,961 |
| 2 | 67,469 | 52,500 | -1,552,430 | -1,552,430 | 1,868 | 2,747 | 847,650 |
| 3 | 294,218 | 260,255 | -1,856,014 | -1,856,014 | 4,367 | 6,913 | 2,476,827 |
| 4 | 724,368 | 661,756 | -1,931,704 | -1,931,704 | 7,580 | 13,039 | 5,357,566 |
| 5 | 1,383,153 | 1,283,645 | -1,941,882 | -1,941,882 | 11,323 | 21,089 | 9,588,615 |
| 6 | 2,228,943 | 2,085,598 | -1,919,999 | -1,919,999 | 15,281 | 30,796 | 15,135,084 |
| 7 | 3,337,831 | 3,185,555 | -1,752,631 | -1,752,631 | 19,124 | 41,751 | 21,708,491 |

- Peak funding requirement **USD 13,082,258** at M84
- Minimum cumulative cash **USD -12,673,817** at M84
- Cumulative net profit over 7 years **USD -12,331,144**
- First EBITDA-positive year: **none inside 7 years**

## 2. Revenue by stream

| year | stream1_sip | stream1_spot | stream2 | stream3 | stream4 | stream5 | stream6 | revenue |
|---|---|---|---|---|---|---|---|---|
| 1 | 2,134 | 1,298 | 0 | 1,805 | 0 | 0 | 0 | 11,477 |
| 2 | 15,200 | 10,140 | 7,576 | 7,794 | 8,236 | 7 | 3,547 | 67,469 |
| 3 | 26,998 | 19,700 | 59,110 | 19,623 | 48,679 | 225 | 85,920 | 294,218 |
| 4 | 50,362 | 40,085 | 195,019 | 36,317 | 141,797 | 736 | 197,440 | 724,368 |
| 5 | 77,675 | 66,710 | 433,516 | 56,088 | 302,914 | 1,701 | 345,040 | 1,383,153 |
| 6 | 81,135 | 74,743 | 795,503 | 77,302 | 532,338 | 3,138 | 521,440 | 2,228,943 |
| 7 | 120,751 | 119,002 | 1,298,581 | 98,022 | 830,754 | 5,005 | 713,440 | 3,337,831 |

Share of Y7 revenue:

| Stream | USD | Share of revenue |
|---|---|---|
| Stream 2 card interchange | 1,298,581 | 38.90% |
| Stream 4 cardholder fees | 830,754 | 24.89% |
| Stream 6 B2B platform | 713,440 | 21.37% |
| Stream 1a entry fee, SIP | 120,751 | 3.62% |
| Stream 1b entry fee, spot | 119,002 | 3.57% |
| Stream 3 family plan | 98,022 | 2.94% |
| Stream 5 lending share | 5,005 | 0.15% |

⚠ Streams 1a and 1b are reported at their NET contribution margin; the gross entry fee they are struck on is a larger number. Streams 2 to 6 are reported gross of their own direct costs, which sit in operating cost.

## 3. Cost of revenue - two terms only

D31 removed the payment rail and D32 removed the float cost of capital. What remains in cost of revenue is the fabrication premium and the price gap, and nothing else.

| year | cor_premium | cor_pricegap | cost_of_revenue | rail_passthrough_usd | floatcoc_memo |
|---|---|---|---|---|---|
| 1 | 2,704 | 3,536 | 6,241 | 880 | 2,297 |
| 2 | 11,432 | 3,536 | 14,969 | 3,916 | 2,419 |
| 3 | 30,426 | 3,536 | 33,963 | 10,076 | 3,932 |
| 4 | 59,076 | 3,536 | 62,613 | 19,059 | 6,328 |
| 5 | 95,972 | 3,536 | 99,508 | 30,047 | 9,254 |
| 6 | 139,808 | 3,536 | 143,345 | 42,230 | 12,489 |
| 7 | 116,912 | 35,365 | 152,277 | 54,611 | 25,959 |

🔴 `rail_passthrough_usd` and `floatcoc_memo` are **MEMO LINES**. They appear in no revenue total, no cost total and no margin. Checks 12 and 13 assert this every month and the run fails loudly if either leaks.

## 4. Unit economics

| | USD 75 illustration | Book-weighted ticket |
|---|---|---|
| Ticket | USD 75.00 | USD 31.06 |
| Fee applied | 3.05% | 3.05% |
| Fabrication premium | 0.95% | 0.95% |
| Net new gram share (D30/D33) | 98.66% | 98.66% |
| Price gap | 0.27% | 0.27% |
| **Gross margin** | **USD 1.6039 (2.14%)** | **USD 0.6642 (2.14%)** |
| **Net contribution margin** | **USD 1.3978 (1.86%)** | **USD 0.5788 (1.86%)** |
| Rail memo, NOT deducted | USD 0.25 | USD 0.25 |

### Correction 26, settled by computation

The brief states **0.72%** in section 3 Layer 4 and section 6.1b, and **2.15%** in the section 6.1 waterfall. These cannot both be right.

Implementing the exact identity `C - C(1-f)(1+p)` and letting the model produce the number gives **2.150%** at the v1.0 3.00% premium on a USD 75 contribution at a 5% fee. That reproduces the brief's own audited USD 1.6125 exactly.

**Verdict: the 0.72% figure is arithmetically wrong and the waterfall is right.** At D28's Base premium the same identity gives **2.139%**. Neither figure is hardcoded anywhere in the model.

## 5. D31 - rail incidence on the customer

The rail left Aurumix's P&L. It did not leave the transaction. Aurumix asks for `ticket + rail` and remits it, so the incidence moved wholly onto the customer - and because the rail is a fixed amount per collection and the ticket is not, **it is regressive**.

| region | region_name | band | share_of_region | ticket_usd | rail_usd | request_amount_usd | gross_up_pct_of_ticket | annual_cost_to_customer_usd |
|---|---|---|---|---|---|---|---|---|
| R1 | UAE Indian | floor | 0.400 | 20.000 | 0.250 | 20.250 | 1.250 | 3.000 |
| R2 | UAE other South Asian | floor | 0.600 | 20.000 | 0.250 | 20.250 | 1.250 | 3.000 |
| R4 | India resident | floor | 0.250 | 20.000 | 0.250 | 20.250 | 1.250 | 3.000 |
| R3 | Oman | floor | 0.580 | 20.000 | 0.250 | 20.250 | 1.250 | 3.000 |
| R4 | India resident | standard | 0.750 | 33.333 | 0.250 | 33.583 | 0.750 | 3.000 |
| R3 | Oman | standard | 0.420 | 34.286 | 0.250 | 34.536 | 0.729 | 3.000 |
| R2 | UAE other South Asian | standard | 0.400 | 35.000 | 0.250 | 35.250 | 0.714 | 3.000 |
| R1 | UAE Indian | standard | 0.600 | 50.000 | 0.250 | 50.250 | 0.500 | 3.000 |

The floor band pays **1.25%** of its contribution as rail; R1's standard band pays **0.50%**. That is a **2.5x spread**, against a gross margin of roughly 2.14%.

## 6. Minimum viable entry fee

🔴 **PROVISIONAL.** F4's absolute level failed replication on 2026-08-20 (correction 36). The fabrication premium is the largest surviving term in this calculation, so every figure in this table is conditional on F4 being re-observed.

| year | premium | effective_premium | pricegap_weighted | sip_ticket | assumed fee | min viable fee (binding) | min viable fee floor band (USD 20) | shortfall_pp | achievable |
|---|---|---|---|---|---|---|---|---|---|
| 1.0000 | 0.0150 | 0.0146 | 0.0181 | 36.3148 | 0.0500 | 0.0327 | 0.0327 | -1.7315 | True |
| 2.0000 | 0.0150 | 0.0145 | 0.0043 | 32.8490 | 0.0500 | 0.0199 | 0.0199 | -3.0057 | True |
| 3.0000 | 0.0150 | 0.0148 | 0.0017 | 31.6885 | 0.0400 | 0.0184 | 0.0184 | -2.1560 | True |
| 4.0000 | 0.0150 | 0.0149 | 0.0009 | 31.2716 | 0.0400 | 0.0184 | 0.0184 | -2.1610 | True |
| 5.0000 | 0.0150 | 0.0149 | 0.0005 | 31.1316 | 0.0400 | 0.0187 | 0.0187 | -2.1297 | True |
| 6.0000 | 0.0150 | 0.0149 | 0.0004 | 31.0781 | 0.0350 | 0.0191 | 0.0191 | -1.5900 | True |
| 7.0000 | 0.0095 | 0.0094 | 0.0027 | 31.0591 | 0.0350 | 0.0165 | 0.0165 | -1.8464 | True |

## 7. Population and tier mix

| year | new_accounts | contributing | reduced | lapsed_holding | dormant | holding | live_accounts |
|---|---|---|---|---|---|---|---|
| 1 | 689 | 510 | 3 | 177 | 0 | 689 | 513 |
| 2 | 2,058 | 1,853 | 15 | 765 | 114 | 2,747 | 1,868 |
| 3 | 4,165 | 4,321 | 46 | 1,900 | 646 | 6,913 | 4,367 |
| 4 | 6,127 | 7,478 | 102 | 3,454 | 2,005 | 13,039 | 7,580 |
| 5 | 8,050 | 11,139 | 184 | 5,221 | 4,545 | 21,089 | 11,323 |
| 6 | 9,707 | 14,992 | 289 | 7,059 | 8,456 | 30,796 | 15,281 |
| 7 | 10,955 | 18,713 | 411 | 8,802 | 13,824 | 41,751 | 19,124 |

| year | tier_none | tier_silver | tier_gold | tier_platinum | tier_sovereign |
|---|---|---|---|---|---|
| 1 | 380 | 133 | 0 | 0 | 0 |
| 2 | 1,170 | 488 | 210 | 0 | 0 |
| 3 | 2,434 | 1,109 | 824 | 0 | 0 |
| 4 | 3,702 | 1,854 | 1,890 | 134 | 0 |
| 5 | 4,970 | 2,648 | 3,183 | 521 | 0 |
| 6 | 6,100 | 3,410 | 4,500 | 1,220 | 50 |
| 7 | 6,992 | 4,058 | 5,780 | 2,067 | 227 |

Gate arrival is a **distribution, not a date**: mean **M8.1**, ever-gate **53.79%**, never-gated **46.21%** of an original vintage.

| archetype | weight | pay_prob | monthly_hazard | ever_gate_prob | mean_gate_month |
|---|---|---|---|---|---|
| Perfect payer | 0.100 | 0.995 | 0.016 | 0.906 | 6.100 |
| Occasional misser | 0.350 | 0.930 | 0.023 | 0.836 | 7.600 |
| Alternating misser | 0.120 | 0.550 | 0.034 | 0.236 | 23.600 |
| Reducer | 0.130 | 0.970 | 0.018 | 0.886 | 6.600 |
| Early lapser | 0.300 | 0.600 | 0.216 | 0.037 | 14.700 |

The never-gated population pays the **full undiscounted entry fee forever** and receives **zero benefits**. It is structurally the highest-margin retail account in the book, and check 11 asserts it carries no discount weight.

## 8. D25 - four regions, two bands each

| Region | Name | Addressable | Ceiling | Ceiling accounts | Avg ticket | Floor share | Floor band | Standard band | Activation | UAE resident |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | UAE Indian | 640,000.0000 | 0.0950 | 60,800.0000 | 38.0000 | 0.4000 | 20.0000 | 50.0000 | 1.0000 | 1.0000 |
| R2 | UAE other South Asian | 620,000.0000 | 0.0600 | 37,200.0000 | 26.0000 | 0.6000 | 20.0000 | 35.0000 | 7.0000 | 1.0000 |
| R3 | Oman | 600,000.0000 | 0.0400 | 24,000.0000 | 26.0000 | 0.5800 | 20.0000 | 34.2857 | 13.0000 | 0.0000 |
| R4 | India resident | 12,500,000.0000 | 0.0035 | 43,750.0000 | 30.0000 | 0.2500 | 20.0000 | 33.3333 | 13.0000 | 0.0000 |

**Reconciliation invariant (check 14):** base x ceiling = **165,750.0** against a target of **165,750.0**. Asserted at import; the model will not start if it drifts.

### Named, sized, deliberately not modelled

| Region | Size | Why not modelled |
|---|---|---|
| Bahrain | 259,000 | CBB Crypto-Asset Module binds; no reverse-solicitation exemption; entry would require a CBB pre-application. |
| Emirati | 1,330,000 | Wrong persona: no remittance driver, and already served by Liv Gold inside ENBD/ADIB. |
| Western expat | 550,000 | No gold-savings behaviour. Sized 500-600k; midpoint carried. |

## 9. Scenarios

| Scenario | Y7 revenue | Y7 gross profit | Y7 live accounts | Cumulative net profit | Peak funding | Peak month |
|---|---|---|---|---|---|---|
| Base | 3,337,831 | 3,185,555 | 19,124 | -12,331,144 | 13,082,258 | 84 |
| Aggressive | 12,506,514 | 11,997,649 | 32,825 | 1,323,821 | 6,271,428 | 53 |
| Conservative | 559,175 | 414,768 | 9,880 | -14,929,221 | 15,438,094 | 84 |
| premium_kills_it | 3,337,831 | 2,883,447 | 19,124 | -13,188,856 | 13,948,184 | 84 |
| redeemed_to_dealer | 3,337,831 | 3,183,968 | 19,124 | -12,340,409 | 13,091,523 | 84 |
| float_debt_funded | 3,337,831 | 3,185,555 | 19,124 | -12,393,825 | 13,144,938 | 84 |
| no_card | 1,208,497 | 1,056,220 | 19,124 | -14,096,962 | 14,848,076 | 84 |
| card_prepaid_capped | 2,659,597 | 2,507,320 | 19,124 | -13,789,756 | 14,540,870 | 84 |
| clients_plan | 11,367,715 | 10,857,059 | 69,947 | -11,480,867 | 12,757,860 | 84 |
| no_india | 2,856,837 | 2,706,641 | 18,045 | -13,398,591 | 14,139,934 | 84 |
| lapsed_loses_card | 2,676,033 | 2,523,757 | 19,124 | -13,060,566 | 13,811,679 | 84 |
| option_b_capital | 3,337,831 | 3,185,555 | 19,124 | -12,331,144 | 13,082,258 | 84 |

## 10. Tornado

⚠ **Two rankings went stale at the rebuild and are deliberately absent.** S1 (rail) left the tornado entirely under D31 - it is a pass-through, so flexing it reports a swing of exactly zero and would invite the reader to conclude the rail does not matter. It matters to the customer, and that incidence is in section 5. F5 (float cost of capital) left the margin under D32 and cannot move profit; the float PRINCIPAL still moves peak funding, through the float sizing rather than through F5.

### Cumulative net profit

| driver | base | aggressive | conservative | swing |
|---|---|---|---|---|
| Card spend per active card (S4) | -12,331,144 | -10,566,840 | -13,785,318 | 3,218,478 |
| Card activation rate (S5) | -12,331,144 | -11,673,992 | -13,208,202 | 1,534,210 |
| Card programme fixed costs (F27) | -12,331,144 | -11,882,644 | -13,306,144 | 1,423,500 |
| PM share of interchange (S3) | -12,331,144 | -11,741,775 | -13,101,858 | 1,360,082 |
| Fabrication premium (F4, PROVISIONAL) | -12,331,144 | -12,337,853 | -13,188,856 | 851,002 |
| Spot attach (S45) | -12,331,144 | -12,101,842 | -12,492,203 | 390,361 |
| Payment archetype mix (S27) | -12,331,144 | -12,192,164 | -12,559,146 | 366,983 |
| Family attach (S11) | -12,331,144 | -12,117,313 | -12,473,699 | 356,386 |
| Regional ceiling (S22) | -12,331,144 | -12,399,720 | -12,206,873 | 192,847 |
| Average ticket by region (S55) | -12,331,144 | -12,258,410 | -12,397,546 | 139,137 |
| Vault storage rate (S14) | -12,331,144 | -12,291,144 | -12,394,625 | 103,481 |
| Redemption rate (S32) | -12,331,144 | -12,300,047 | -12,381,958 | 81,911 |
| Self-custody leakage (S10) | -12,331,144 | -12,350,561 | -12,289,539 | 61,023 |
| Lapsed-holder multiplier (S33) | -12,331,144 | -12,326,219 | -12,339,546 | 13,327 |
| Credit take-up (S8) | -12,331,144 | -12,323,937 | -12,337,151 | 13,214 |
| Facility turnover (S40) | -12,331,144 | -12,329,016 | -12,333,109 | 4,092 |
| Y1 opex exit run-rate uplift (S48) | -12,331,144 | -12,330,295 | -12,332,277 | 1,982 |
| Floor-band share by region (S54) | -12,331,144 | -12,331,207 | -12,331,082 | 125 |

### Peak funding

| driver | base | aggressive | conservative | swing |
|---|---|---|---|---|
| Card spend per active card (S4) | 13,082,258 | 11,317,953 | 14,536,431 | 3,218,478 |
| Card activation rate (S5) | 13,082,258 | 12,425,106 | 13,959,316 | 1,534,210 |
| Card programme fixed costs (F27) | 13,082,258 | 12,633,758 | 14,057,258 | 1,423,500 |
| PM share of interchange (S3) | 13,082,258 | 12,492,889 | 13,852,971 | 1,360,082 |
| Fabrication premium (F4, PROVISIONAL) | 13,082,258 | 13,088,899 | 13,948,184 | 859,285 |
| Family attach (S11) | 13,082,258 | 12,868,426 | 13,224,812 | 356,386 |
| Spot attach (S45) | 13,082,258 | 12,852,955 | 13,115,960 | 263,005 |
| Payment archetype mix (S27) | 13,082,258 | 13,002,334 | 13,263,180 | 260,846 |
| Regional ceiling (S22) | 13,082,258 | 13,165,832 | 12,931,581 | 234,251 |
| Vault storage rate (S14) | 13,082,258 | 13,042,257 | 13,145,738 | 103,481 |
| Redemption rate (S32) | 13,082,258 | 13,051,161 | 13,133,071 | 81,911 |
| Self-custody leakage (S10) | 13,082,258 | 13,101,675 | 13,040,652 | 61,023 |
| Average ticket by region (S55) | 13,082,258 | 13,052,515 | 13,108,708 | 56,194 |
| Lapsed-holder multiplier (S33) | 13,082,258 | 13,077,333 | 13,090,659 | 13,327 |
| Credit take-up (S8) | 13,082,258 | 13,075,050 | 13,088,264 | 13,214 |
| Facility turnover (S40) | 13,082,258 | 13,080,130 | 13,084,222 | 4,092 |
| Y1 opex exit run-rate uplift (S48) | 13,082,258 | 13,081,409 | 13,083,390 | 1,982 |
| Floor-band share by region (S54) | 13,082,258 | 13,082,266 | 13,082,250 | 16 |

## 11. D33 - where redeemed gold goes

D30 charges the fabrication premium on net new grams. That holds only if redeemed gold returns to the float. **Nobody had written down which** (correction 30). D33 settles it: redeemed grams return to the float up to the float ceiling, and the excess is sold back at the observed bid of spot **-1.50%**.

Both settings are reported, so the default is visible rather than buried.

| REDEEMED_GOLD_TO_FLOAT | routing | mean_net_new_gram_share_final_year | terminal_year_gross_profit | cumulative_premium_cost | cumulative_redemption_cost | cumulative_net_profit | peak_funding |
|---|---|---|---|---|---|---|---|
| True | float, excess sold at bid | 0.9853 | 3,185,554.5518 | 456,330.3816 | 76,461.5419 | -12,331,144.3787 | 13,082,257.8837 |
| False | all to dealer | 1.0000 | 3,183,967.5712 | 460,503.3180 | 81,553.2564 | -12,340,409.0296 | 13,091,522.5346 |

🔴 The bid and the ask are **not symmetric and are not netted**. Correction 35 measured the bid as near-flat across denomination while the ask premium moves about 194bp. Fabrication is paid on the way in and is not recovered on the way out.

## 12. D32 - the float debt-funded switch

If the float is equity funded the carry is an opportunity cost and a memo. If it is debt funded the interest is cash and belongs below EBITDA as a financing line.

| FLOAT_DEBT_FUNDED | treatment | cumulative_ebitda | cumulative_float_interest | cumulative_net_profit | peak_funding |
|---|---|---|---|---|---|
| False | memo, equity funded | -12,331,144 | 0 | -12,331,144 | 13,082,258 |
| True | financing line below EBITDA, debt funded | -12,331,144 | 62,680 | -12,393,825 | 13,144,938 |

🔴 In both cases the float **principal** is untouched. It stays on the balance sheet, in the funding view, and inside peak funding. The cost moved from the P&L to the cap table; it did not stop being money.

## 13. The 29-column reporting view

M1-M24 monthly, then Y3-Y7 as five annual columns. Written to `outputs/view29_Base.csv`. Three rules:

- **Rates never sum.** They are re-derived over the year, or inflow-weighted where no explicit denominator exists.
- **Flows sum** over their twelve constituent months.
- **Snapshots take the last month** of the year.

| line | M1 | M6 | M12 | M18 | M24 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|---|---|---|---|---|---|---|---|---|---|
| revenue | 160.6644 | 927.0847 | 1,702.0400 | 5,130.0821 | 12,651.3922 | 294,217.8702 | 724,368.4919 | 1,383,152.8206 | 2,228,942.8421 | 3,337,831.1231 |
| gross_profit | -172.2787 | 413.5505 | 1,008.2596 | 3,942.7522 | 10,890.7192 | 260,254.9768 | 661,755.5881 | 1,283,644.7335 | 2,085,598.1455 | 3,185,554.5518 |
| ebitda | -234,536.1531 | -97,216.0463 | -135,967.2246 | -131,435.9338 | -129,569.4400 | -1,856,013.8948 | -1,931,703.9510 | -1,941,882.2962 | -1,919,998.8168 | -1,752,630.8754 |
| live_accounts | 49.7010 | 269.6918 | 512.5530 | 1,216.8008 | 1,867.7915 | 4,366.9883 | 7,580.0591 | 11,322.9613 | 15,280.7454 | 19,124.3475 |
| aum_usd | 2,548.9862 | 51,176.1568 | 171,960.8210 | 432,695.0714 | 847,650.2450 | 2,476,827.3916 | 5,357,566.1716 | 9,588,614.7234 | 15,135,084.1723 | 21,708,490.8114 |
| fee_applied | 0.0500 | 0.0500 | 0.0490 | 0.0487 | 0.0481 | 0.0378 | 0.0371 | 0.0365 | 0.0310 | 0.0305 |
| fab_premium | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0150 | 0.0095 |
| rail_passthrough_usd | 12.6717 | 69.1061 | 131.9980 | 313.5673 | 482.7010 | 10,076.3694 | 19,059.0082 | 30,046.7297 | 42,230.1532 | 54,611.4021 |
| floatcoc_memo | 191.4425 | 191.4425 | 191.4425 | 191.4425 | 232.4285 | 3,932.4675 | 6,328.3749 | 9,254.4264 | 12,489.3943 | 25,959.3898 |
