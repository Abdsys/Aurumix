# Aurumix Revenue Model - Validation

Every check below is executed by the run that writes this file. A failing check is reported as a failure here and, where it is an invariant, aborts the run.

## Summary

| Check | Result |
|---|---|
| ICS personas A-I | 9/9 pass |
| ICS gate mechanics | 7/7 pass |
| D23 convolution vs vintage triangle | max relative residual 4.20e-14% - **PASS** |
| D23 annual decomposition (check 8) | **PASS** |
| D22 collapse safety gate (5%) | **SAFE** |
| 29-column view faithfulness | **PASS** |
| D25 base x ceiling invariant | 165,750.0 vs 165,750.0 - **PASS** |

## 1. D23 equivalence: convolution against the vintage triangle

The convolution is the live engine. The vintage triangle is kept in `cohort.py` purely as the equivalence harness. Both engines are run on the same acquisition vector and the residual is reported.

| Quantity | Max abs residual | Max relative | Mean relative | Convolution terminal | Triangle terminal |
|---|---|---|---|---|---|
| contributing_plus_reduced | 1.819e-12 | 4.203e-14% | 1.257e-14% | 6,152.68 | 6,152.68 |
| holding | 3.638e-12 | 4.177e-14% | 1.325e-14% | 15,489.94 | 15,489.94 |

**Verdict: the two engines agree to floating-point noise.** Max relative residual 4.203e-14%.

⚠ **Two off-by-one errors were found by this test and fixed.** Neither was visible from either engine alone.

1. `Vintage.step_population` computed age as `m - origin + 1`, so the first hazard an account faced belonged to age 2 rather than age 1. That disagreed with `survival_curve` in the same module and shifted every age-dependent hazard one month early.

2. The convolution offset was `t - s + 1` rather than `t - s`. A vintage acquired in month t is observed in month t at age **zero**; it has not yet faced a hazard. The wrong offset aged every cohort by a month, understating the payment axis by about 8% at M1 and about 4% by M20 - worst exactly in the months the view reports monthly.

## 2. D23 annual decomposition (check 8)

Every annual column is the sum of twelve monthly convolutions. It is **never** a single convolution against an annual aggregate acquisition figure, which would collapse twelve first-passage months into one and destroy the gate distribution.

| year | sum_of_12_monthly_convolutions | annual_column | residual | pass | annual_aggregate_would_err_pct |
|---|---|---|---|---|---|
| 3.0000 | 20,709.3183 | 20,709.3183 | 0.0000 | True | -59.1300 |
| 4.0000 | 25,461.4424 | 25,461.4424 | 0.0000 | True | -65.4300 |
| 5.0000 | 29,138.5515 | 29,138.5515 | 0.0000 | True | -69.1200 |
| 6.0000 | 31,994.2780 | 31,994.2780 | 0.0000 | True | -71.4900 |
| 7.0000 | 34,219.0664 | 34,219.0664 | 0.0000 | True | -73.1000 |

Convolving an annual aggregate instead would misstate the population by up to **73.1%**. That is the size of the error the rule prevents.

## 3. D22 collapse safety gate

The live model reads a flat Gold interchange rate of **1.80%** for every tier. The full ladder is 1.80% / 2.05% / 2.10%. The collapse understates stream 2 by the interchange a Platinum or Sovereign cardholder generates above the Gold rate.

**The gate is binding: if any year exceeds 5% of gross profit, the collapse is unsafe and the model must revert to the full ladder.**

| year | stream2_collapsed_usd | stream2_full_ladder_usd | collapse_cost_usd | gross_profit_usd | cost_pct_of_gross_profit | within_5pct_gate |
|---|---|---|---|---|---|---|
| 1.00 | 0.00 | 0.00 | 0.00 | 5,236.62 | 0.00 | True |
| 2.00 | 9,620.39 | 9,620.39 | 0.00 | 52,500.11 | 0.00 | True |
| 3.00 | 71,691.81 | 71,691.81 | 0.00 | 260,254.98 | 0.00 | True |
| 4.00 | 232,139.55 | 234,109.45 | 1,969.90 | 661,755.59 | 0.30 | True |
| 5.00 | 514,010.64 | 524,758.45 | 10,747.80 | 1,283,644.73 | 0.84 | True |
| 6.00 | 939,081.26 | 971,245.90 | 32,164.65 | 2,085,598.15 | 1.54 | True |
| 7.00 | 1,526,027.80 | 1,597,391.13 | 71,363.33 | 3,185,554.55 | 2.24 | True |

**Verdict: SAFE.** Peak cost **2.24%** of gross profit at Y7, against a 5% gate.

Check 15: the full ladder is read **only** on this validation path. Nothing in the live model references it, because doing so would silently un-do the collapse.

## 4. ICS personas A-I

The full exact-fraction ICS engine is retained as the validation harness for D22's collapsed lookup. All nine personas must pass before the model ships. H and I are the rows a naive build fails.

| persona | description | exp_ics | got_ics | exp_tier | got_tier | got_record | got_standing | got_retention | pass |
|---|---|---|---|---|---|---|---|---|---|
| A | USD 20/mo, perfect, never sells, month 60 | 100.000 | 100.000 | Sovereign | Sovereign | 100.000 | 100.000 | 1.000 | True |
| B | As A but missed one month in the last year | 91.700 | 91.667 | Platinum | Platinum | 98.958 | 91.667 | 1.000 | True |
| C | USD 2,000/mo, perfect, never sells, month 60 | 100.000 | 100.000 | Sovereign | Sovereign | 100.000 | 100.000 | 1.000 | True |
| D | Cycler: contributes and redeems every month | 25.000 | 25.000 | Silver | Silver | 100.000 | 100.000 | 0.000 | True |
| E | Withdrew half at month 36, kept saving | 53.600 | 53.571 | Gold | Gold | 75.000 | 100.000 | 0.714 | True |
| F | Withdrew everything at month 36, kept saving | 25.000 | 25.000 | Silver | Silver | 75.000 | 100.000 | 0.000 | True |
| G | Withdrew 30% at month 36 (inside the allowance) | 75.000 | 75.000 | Platinum | Platinum | 75.000 | 100.000 | 1.000 | True |
| H | Scattered payer: 6 payments over 3 years, never 6 in a row | n/a | n/a | None | None | n/a | n/a | n/a | True |
| I | Late opener: paid 1-3, missed 4, paid 5-7, missed 8, ran 9-14 | 25.000 | 25.000 | Silver | Silver | 25.000 | 50.000 | 1.000 | True |

## 5. ICS gate mechanics

Behavioural checks the closed-form persona table cannot express.

| check | expected | got | pass |
|---|---|---|---|
| Persona I gate fires at M14 with Months=6, Recent=6 | gated=True months=6 recent=6 tier=Silver | gated=True months=6 recent=6 tier=Silver | True |
| Persona H never gates (no score, no tier, ever) | gated=False tier=None | gated=False tier=None | True |
| Regulatory block freezes the pre-gate run (4-of-6 resumes at 4-of-6) | run_length=4 after 6 frozen months | run_length=4 (was 4) | True |
| Frozen months are skipped entirely on both clocks | months unchanged at 6 | months=6 | True |
| Dormancy absorbs at 12 consecutive silent periods | dormant=True | dormant=True silent=12 | True |
| Exact fractions: Standing(Recent=6) reaches Gold, not Silver | Standing=50 exactly -> Gold | exact=50.0 (naive 8.3333x6=49.9998 -> Silver) | True |
| Alternating misser is permanently capped at Gold | tier=Gold | months=66 recent=6 tier=Gold | True |

## 6. Survival fit on the D21 horizon

All five anchors (M13/M25/M37/M49/M61) still fall inside 84 months, so **the anchors survive D21 intact**. The fit DOMAIN shrank from 120 to 84 months, so the residuals are **re-reported here rather than carried over** from the ten-year fit. Carrying the old residuals would be claiming a fit that was never run.

| anchor_month | target | modelled | residual_pp | inside_horizon | rmse_pp |
|---|---|---|---|---|---|
| 13.0000 | 0.5500 | 0.5429 | -0.7060 | True | 1.3040 |
| 25.0000 | 0.4000 | 0.4165 | 1.6490 | True | 1.3040 |
| 37.0000 | 0.3000 | 0.3211 | 2.1100 | True | 1.3040 |
| 49.0000 | 0.2400 | 0.2486 | 0.8590 | True | 1.3040 |
| 61.0000 | 0.1900 | 0.1932 | 0.3150 | True | 1.3040 |

## 7. The 29-column view is a faithful restatement

Every flow in an annual column must equal the sum of its twelve monthly values; every snapshot must equal the last month. A **rate must not** equal the sum of its months, which is the failure this catches.

| year | line | rule | view | sum_of_12 | residual | pass |
|---|---|---|---|---|---|---|
| 3.0000 | revenue | flow | 294,217.8702 | 294,217.8702 | 0.0000 | True |
| 3.0000 | gross_profit | flow | 260,254.9768 | 260,254.9768 | 0.0000 | True |
| 3.0000 | ebitda | flow | -1,856,013.8948 | -1,856,013.8948 | 0.0000 | True |
| 3.0000 | inflow_sip | flow | 1,234,202.5148 | 1,234,202.5148 | 0.0000 | True |
| 3.0000 | cost_of_revenue | flow | 33,962.8934 | 33,962.8934 | 0.0000 | True |
| 3.0000 | rail_passthrough_usd | flow | 10,076.3694 | 10,076.3694 | 0.0000 | True |
| 3.0000 | floatcoc_memo | flow | 3,932.4675 | 3,932.4675 | 0.0000 | True |
| 3.0000 | live_accounts | snapshot | 4,366.9883 | 4,366.9883 | 0.0000 | True |
| 3.0000 | aum_usd | snapshot | 2,476,827.3916 | 2,476,827.3916 | 0.0000 | True |
| 3.0000 | holding | snapshot | 6,912.5641 | 6,912.5641 | 0.0000 | True |
| 3.0000 | fee_applied | rate (must NOT sum) | 0.0378 | 0.4540 | -0.4162 | True |
| 3.0000 | fab_premium | rate (must NOT sum) | 0.0150 | 0.1800 | -0.1650 | True |
| 4.0000 | revenue | flow | 724,368.4919 | 724,368.4919 | 0.0000 | True |
| 4.0000 | gross_profit | flow | 661,755.5881 | 661,755.5881 | 0.0000 | True |
| 4.0000 | ebitda | flow | -1,931,703.9510 | -1,931,703.9510 | 0.0000 | True |
| 4.0000 | inflow_sip | flow | 2,296,427.4601 | 2,296,427.4601 | 0.0000 | True |
| 4.0000 | cost_of_revenue | flow | 62,612.9039 | 62,612.9039 | 0.0000 | True |
| 4.0000 | rail_passthrough_usd | flow | 19,059.0082 | 19,059.0082 | 0.0000 | True |
| 4.0000 | floatcoc_memo | flow | 6,328.3749 | 6,328.3749 | 0.0000 | True |
| 4.0000 | live_accounts | snapshot | 7,580.0591 | 7,580.0591 | 0.0000 | True |
| 4.0000 | aum_usd | snapshot | 5,357,566.1716 | 5,357,566.1716 | 0.0000 | True |
| 4.0000 | holding | snapshot | 13,039.0943 | 13,039.0943 | 0.0000 | True |
| 4.0000 | fee_applied | rate (must NOT sum) | 0.0371 | 0.4457 | -0.4086 | True |
| 4.0000 | fab_premium | rate (must NOT sum) | 0.0150 | 0.1800 | -0.1650 | True |
| 5.0000 | revenue | flow | 1,383,152.8206 | 1,383,152.8206 | 0.0000 | True |
| 5.0000 | gross_profit | flow | 1,283,644.7335 | 1,283,644.7335 | 0.0000 | True |
| 5.0000 | ebitda | flow | -1,941,882.2962 | -1,941,882.2962 | 0.0000 | True |
| 5.0000 | inflow_sip | flow | 3,593,691.6479 | 3,593,691.6479 | 0.0000 | True |
| 5.0000 | cost_of_revenue | flow | 99,508.0871 | 99,508.0871 | 0.0000 | True |
| 5.0000 | rail_passthrough_usd | flow | 30,046.7297 | 30,046.7297 | 0.0000 | True |
| 5.0000 | floatcoc_memo | flow | 9,254.4264 | 9,254.4264 | 0.0000 | True |
| 5.0000 | live_accounts | snapshot | 11,322.9613 | 11,322.9613 | 0.0000 | True |
| 5.0000 | aum_usd | snapshot | 9,588,614.7234 | 9,588,614.7234 | 0.0000 | True |
| 5.0000 | holding | snapshot | 21,089.0064 | 21,089.0064 | 0.0000 | True |
| 5.0000 | fee_applied | rate (must NOT sum) | 0.0365 | 0.4384 | -0.4018 | True |
| 5.0000 | fab_premium | rate (must NOT sum) | 0.0150 | 0.1800 | -0.1650 | True |
| 6.0000 | revenue | flow | 2,228,942.8421 | 2,228,942.8421 | 0.0000 | True |
| 6.0000 | gross_profit | flow | 2,085,598.1455 | 2,085,598.1455 | 0.0000 | True |
| 6.0000 | ebitda | flow | -1,919,998.8168 | -1,919,998.8168 | 0.0000 | True |
| 6.0000 | inflow_sip | flow | 5,027,913.8936 | 5,027,913.8936 | 0.0000 | True |
| 6.0000 | cost_of_revenue | flow | 143,344.6966 | 143,344.6966 | 0.0000 | True |
| 6.0000 | rail_passthrough_usd | flow | 42,230.1532 | 42,230.1532 | 0.0000 | True |
| 6.0000 | floatcoc_memo | flow | 12,489.3943 | 12,489.3943 | 0.0000 | True |
| 6.0000 | live_accounts | snapshot | 15,280.7454 | 15,280.7454 | 0.0000 | True |
| 6.0000 | aum_usd | snapshot | 15,135,084.1723 | 15,135,084.1723 | 0.0000 | True |
| 6.0000 | holding | snapshot | 30,795.8916 | 30,795.8916 | 0.0000 | True |
| 6.0000 | fee_applied | rate (must NOT sum) | 0.0310 | 0.3719 | -0.3409 | True |
| 6.0000 | fab_premium | rate (must NOT sum) | 0.0150 | 0.1800 | -0.1650 | True |
| 7.0000 | revenue | flow | 3,337,831.1231 | 3,337,831.1231 | 0.0000 | True |
| 7.0000 | gross_profit | flow | 3,185,554.5518 | 3,185,554.5518 | 0.0000 | True |
| 7.0000 | ebitda | flow | -1,752,630.8754 | -1,752,630.8754 | 0.0000 | True |
| 7.0000 | inflow_sip | flow | 6,479,233.3689 | 6,479,233.3689 | 0.0000 | True |
| 7.0000 | cost_of_revenue | flow | 152,276.5714 | 152,276.5714 | 0.0000 | True |
| 7.0000 | rail_passthrough_usd | flow | 54,611.4021 | 54,611.4021 | 0.0000 | True |
| 7.0000 | floatcoc_memo | flow | 25,959.3898 | 25,959.3898 | 0.0000 | True |
| 7.0000 | live_accounts | snapshot | 19,124.3475 | 19,124.3475 | 0.0000 | True |
| 7.0000 | aum_usd | snapshot | 21,708,490.8114 | 21,708,490.8114 | 0.0000 | True |
| 7.0000 | holding | snapshot | 41,751.0305 | 41,751.0305 | 0.0000 | True |
| 7.0000 | fee_applied | rate (must NOT sum) | 0.0305 | 0.3658 | -0.3353 | True |
| 7.0000 | fab_premium | rate (must NOT sum) | 0.0095 | 0.1140 | -0.1045 | True |

## 8. Invariants asserted every month

These run inside the monthly loop and abort the model on failure.

| # | Invariant | What it protects |
|---|---|---|
| 1 | Population conservation | opening + new = closing across all states; nothing created or destroyed by the convolution |
| 2 | Tier counts sum to the live base | no account is in two tiers or none |
| 3 | Grams reconcile | opening + bought - withdrawn - redeemed = closing |
| 4 | No negative stocks | populations and grams cannot go negative |
| 5 | Band shares sum to 1.0 | the D25 two-band split is exhaustive within every region |
| 6 | Cost bridge closes | total cost equals the sum of its parts |
| 7 | Check 12 (D31) | `rail_memo` appears in no revenue or cost total |
| 8 | Check 13 (D32) | `floatcoc_memo` appears in no COGS, margin or P&L total |
| 9 | Check 14 (D25) | base x ceiling holds at 165,750 |
| 10 | Check 6 | bar denomination latches and never steps down |
| 11 | Check 5 | the acquisition budget reads the PRIOR period, never the current - no circular loop |
| 12 | Check 11 | the never-gated population gets zero benefits and pays the full fee |

## 9. Registered derived values and source conflicts

**11** values were chosen by this model because no source supplies them, and **10** source conflicts were logged and resolved.

| parameter | value | rationale | confidence |
|---|---|---|---|
| F4_provisional_flag | True | F4's absolute level failed replication on 2026-08-20 (correction 36). The denomination shape is corroborated; the level is not. Every conclusion that depends on the level - the minimum viable entry fee above all - is PROVISIONAL until F4 is re-observed against a dealer whose rate page and store page share a clock. | Low |
| REDEEMED_GOLD_TO_FLOAT | True | D33. Correction 30 found that D30 (premium on net new grams) has an UNDESIGNED DEPENDENCY: it holds only if redeemed gold returns to the float, and no source settles which. Default set to True - redeemed grams return to the float up to the F38 ceiling, excess sold back at the observed bid. PROVISIONAL: a defensible default settled by the modeller, not a decision the client has taken. Both settings are run and reported. | Low |
| marketing_spend_by_year | {1: 60000, 2: 150000, 3: 250000, 4: 320000, 5: 400000, 6: 480000, 7: 560000, 8: 640000, 9: 720000, 10: 800000} | The opex table treats Marketing as a cost block but S48/G1 says it is a decision variable and an INPUT to acquisition. Neither source gives a monthly path. Anchored on the brief's Y1/Y3/Y10 opex marketing line and interpolated straight-line (log-linear is undefined from a zero base). | Low |
| early_lapser_post_gate_hazard | 0 | S27 gives the early lapser a 0.200 own hazard and says '~90% gone by M13' but does not say what the residual does afterwards. Holding 0.200 forever drives the archetype to zero and removes it from the M25+ mix entirely, which over-thins the tail. Decayed to 0.030 from M13. | Low |
| card_spend_segment_exponent | 1 | No source splits card spend by customer income band. Ticket is used as an income proxy, compressed by an exponent of 0.55, turning the 3.75x S3->S1 ticket spread into a ~2.1x card-spend spread. Consumption rises sub-proportionally with income (Engel-curve behaviour) and 0.55 sits mid the 0.4-0.7 range usually fitted to it. Normalised so the book-weighted mean equals the AED 6,000 S4 anchor: it redistributes, never rescales. | Low |
| credit_apr | 0 | BRIEF 6.5 gives a UAE pricing corridor of 9% (Emirates Money) to 16% (Finance House) but never picks a point. Midpoint 12.5%; Aurumix takes CREDIT_INTEREST_SHARE_PP of it, not the whole rate. | Medium |
| family_avg_names | 3 | Pricing includes up to 4 beneficiaries; no source gives the observed mean. 3.2 assumes most households register spouse + 2 children and a minority add a parent. | Low |
| spot_tenure_uplift | 0 | S45 says a 3-year account is 'roughly 2x as likely' to buy spot as a 6-month account but gives no functional form. Linear +30%/yr of tenure, capped at 2.0x, reproduces that ratio at 3 years. | Low |
| vault_pricing_regime | ad_valorem | S14 and the brief's 7.4 verified range are both stated as a PERCENTAGE of value, so ad valorem is the sourced regime. The DGCX USD 0.10/kg/day tariff is a different vendor archetype quoted for wholesale bar storage. v1.0 took the cheaper of the two, which is not a quote anyone offers and understates Y10 vault cost by roughly 10x. | Medium |
| opex_anchor_holding_ratio | {1: 1.35, 3: 1.9, 10: 3.0} | The brief's opex anchors are contributing counts (7.4 'cost per investor' row + 14 default). Blocks that scale with the HOLDING book need a holding count at those same anchors, which v1.0 never computed because it treated LAPSED as terminal. Ratios are taken from this model's own computed contributing:holding trajectory (1.35x at Y1 rising to ~3.0x at Y10). | Medium |
| legal_opinions_and_trust_deed | 150,000 | Corpus says 'NOT ESTABLISHED. Budget generously' and names 3 opinions plus a trust deed and 6 counsel batches. The brief carries ZERO legal cost, which reads as if legal is free. USD 150k one-off is a visible placeholder, NOT a quote. Booked M1-M12. | Low |

### Source conflicts

| topic | corpus | param_file | brief | resolution |
|---|---|---|---|---|
| F4 fabrication premium level | goldtrade.ae same-page capture 2026-08-19: 1.71 / 0.93% | D28 states 1.50 / 0.95% | T2 carries 3.00 / 2.00 / 0.75% by year, assumed not observed | F4 made SCENARIO-VARIABLE (correction 36). The level failed replication 2026-08-20 (4.14 / 3.37% on the same page 24h later); only the 0.77pp denomination STEP is corroborated. Base carries D28's 1.50/0.95, Conservative the failed-replication high, Aggressive the low observation. Registered PROVISIONAL: every fee-fundability reversal downstream of D31 and D32 is conditional on F4 being re-observed. |
| Monthly hazard root convention | n/a | n/a | 1.0 says h=1-S^(1/12); 10.2 says h=1-S13^(1/13) | Used 1/12. The M13 anchor spans 12 hazard opportunities. Per task spec. |
| Reduced-state ticket | n/a | S29: 50% of prior ticket floored at USD 20 | 3 Layer 3 hard-codes reduced x 20 | Used S29. The brief's hard-coded 20 is a real error; the floor is the hard minimum (F6), not the observed landing point. |
| LAPSED is terminal | extract item 2: STOPPED/DORMANT retain gold, AUM, custody, card | S33 lapsed-holder redemption multiplier | Layer 2 treats LAPSED as dropping out of everything | Used corpus. LAPSED-HOLDING stays in AUM, custody, screening and (per the LAPSED_KEEPS_CARD switch) the interchange base. |
| Spot entry-fee discount | _draft_sip-rulebook.md 1.1 + decision 44: tier discount on ALL purchases | Block F prices spot at the tier discount | brief models no spot lane at all | Used corpus. _draft_purchase-structure.md 4.1/4.3 ('flat, top of range') is superseded - six days older and overridden by decision 44. |
| Tenure rebate | decision 44 (2026-08-10) RETIRED it | not carried | 9 solver item 6 asks the model to size it | Struck. No rebate is modelled and no FIFO lot accounting is built (decision 41 makes grams fungible). |
| Float cost of capital double-count | extract item 5: charging float CoC AND the full dealer premium double-counts under either regime | S51 dealer-carried at launch | F5 charges 0.49% float CoC as a flat % of inflow with no derivation | Float CoC is DERIVED from the sized float, and set to zero while the float is dealer-carried (to Y3). The flat F5 rate is not used. |
| Stream 5 drawn balance | Manappuram realised tenor 71 days | S40 turnover factor 0.42 | 6.5 computes peak drawn and prices it as persistent | Applied S40 to the interest component only; origination is per-event and rises with turnover. Roughly halves stream 5. |
| Collateral chain open links | table marks 2 open (links 1,5), 3 designed | n/a | header says 'three are open' | Recorded as 2 open / 3 designed. Header is stale; the table is operative. |
| ADGM vs DIFC holding vehicle | decision 50 + composability draft settle route 2 as DIFC | n/a | 7.4 one-off table lists an ADGM SPV | Booked as DIFC SPV. Same cost, corrected label. |

## 10. Known limitations, stated rather than buried

1. 🔴 **F4's absolute level failed replication on 2026-08-20** (correction 36). The denomination SHAPE is corroborated; the LEVEL is not. F4 is therefore carried as a scenario variable, not a constant, and every fee-fundability conclusion downstream of D31 and D32 is **provisional** until it is re-observed.

2. 🔴 **D31 and D32 are jointly dependent and must be presented together.** D31 alone lowers the margin; D32 alone raises it. In one day the cost term went from four components to two and the minimum viable fee fell, with nothing changing in the business. Each step is defensible separately; the sequence dissolved a standing finding by re-attribution alone.

3. **The price-gap formula reproduces about 0.83% at a 12.1-day fill and 25% volatility, against the brief's stated 0.79%.** The difference is the calendar-day versus trading-day convention. The model uses calendar days throughout, which is the more conservative reading.

4. **The never-gated share is higher than the pre-rebuild model reported.** The old engine drove tiers off a deterministic payment pattern that forced a clean first six months, so it gated nearly everyone at M6. The rebuild reads the genuine run-of-6 first-passage law, which the spec requires. The old figure understated the never-gated population; this is a correction, not a regression.

5. **B2B partner AUM is exogenous and does not interact with the retail book.** It depends on a signed partner that does not exist, which makes it the least validated load-bearing number in the model.

6. **Legal and trust costs are unpriced.** They are carried as a visible placeholder, not a quote. The DFSA trust licence is explicitly unquotable and sits behind a switch defaulting to the exempt reading.
