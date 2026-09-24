# Numbers ledger: Aurumix_Revenue_Model_Explainer.md

Source workbook: `tools/Aurumix_Revenue_Model_calculated.xlsx` (Base scenario, cached values). Summary columns D..J = Y1..Y7. Model columns C..Z = M1..M24, AA..AE = Y3..Y7. Assumptions values in column B. "SP" = Scenario Parameters.

Scenario, switch and sensitivity figures (sections 7.2, 7.3, 8) are **not** cached in the workbook. They were produced by copying `tools/Aurumix_Revenue_Model.xlsx`, changing only the stated cell(s), and recalculating with `tools/recalc_py.py` (the Base copy reproduced Summary!J11 and J73 exactly). Rows marked RECALC give the cell changed and the Summary cell read.

## Section 1-2: scope and key results

| Figure in document | Source |
|---|---|
| Entry fee 5% | Assumptions!B8 |
| SIP floor USD 20/month | Assumptions!B41 |
| 29 periods, M1 = Jan 2027 | Cover!C7; Model!C3:AE3 |
| AED peg 3.6725 | Assumptions!B7 |
| Contingency 15% | Assumptions!B225 |
| Y1-Y7 stream revenues (table 2.1) | Summary!D14:J20 |
| Total revenue Y1-Y7; USD 4.49m Y7 | Summary!D11:J11 |
| Revenue USD 14.68m over 7 years | SUM(Summary!D11:J11) = 14,680,631 |
| COGS Y1-Y7 | Summary!D36:J36 |
| Opex Y1-Y7 | Summary!D49:J49 |
| ICS benefit costs Y1-Y7 | Summary!D54:J54 |
| Acquisition costs Y1-Y7 | Summary!D58:J58 |
| Card programme costs Y1-Y7 | Summary!D65:J65 |
| Contingency Y1-Y7 | Summary!D69:J69 |
| Total cost base Y1-Y7 | Summary!D70:J70 |
| Net profit Y1-Y7 | Summary!D73:J73 |
| Cumulative net profit Y1-Y7; trough -1.43m Y3; positive Y6 | Summary!D75:J75 |
| New customers, paying, holders, active cards, grams, gold under custody (table 2.1) | Summary!D101:J101, D102:J102, D103:J103, D105:J105, D106:J106, D107:J107 |
| Y7 mix: B2B 34.7%, SIP 29.5%, card fees 21.2%, family 10.0%, spot 2.4%, interchange 1.3%, lending 1.0% | Summary!J24:J30 (rounded) |
| Region mix Y7: India 30.2%, UAE 28.3%, O&B 6.8%, B2B 34.7% | Summary!J7:J10 / J11 |
| Stream 1 net of premium Y1 USD 20,855; Y7 USD 1.11m (1,433,446 - 321,408) | (Summary!D14+D15-D35); (J14+J15-J35) |
| Gross fee overstates net by 29-39% of net, depending on year (section 5.1) | Premium / (stream 1a + 1b - premium), Summary rows 14, 15, 35: Y1 38.7%, Y2 37.5%, Y3 37.9%, Y4 36.4%, Y5 34.8%, Y6 32.4%, Y7 28.9% |
| Peak funding USD 2.29m at end Y3 | Summary!F84 = Model!AA342 = 2,291,169 |
| Gold under custody Y7 USD 91.1m, 403,565 g | Summary!J107, J106 |
| Constant-price gold under custody Y7 USD 57.1m | Model!AE174 |

## Section 3: customer engine

| Figure | Source |
|---|---|
| Reachable ceilings 142,637 / 35,978 / 125,000 / 303,615 | Assumptions!B84, B85, B86, B87 |
| Populations 4.36m, 3.46m (1.90/0.84/0.36/0.36), 2.63m, 12.5m | Assumptions!F73:I73 and D73 note |
| UAE-Indian growth ~12% in year to Dec 2024 | Assumptions!D73 note |
| Economically active 80% / 100% | Assumptions!F74:I74 |
| Payment capable 57% | Assumptions!F75 |
| Money capable 40%, USD 240/yr | Assumptions!F76, D76 |
| Penetration ceilings 10% / 6% / 1% | Assumptions!F78:I78 |
| O Gold 75,000 active users | Assumptions!B89 |
| UAE ceiling 1.90x observed | Assumptions!B90 |
| Cumulative / ceiling Y7: India 83.5%, O&B 58.5%, UAE 53.6% | Model!AE121/B86; AE78/B85; AE35/B84 |
| India new customers Y5 26,140, Y7 18,871 | Model!AC117, AE117 |
| Marketing spend 90k...1.65m; total 5.16m | Assumptions!B114:B120; SUM |
| Budget split 74/18/8 | Assumptions!B142:B144 |
| O&B budget share unused in Y1 (region opens M13) | Model!C69:N69 = 0 with Assumptions!B143 = 18% and Model!C272:N272 total 90,000 |
| CAC Y1 85/75/15, Y7 55/45/10 | Assumptions!B136:B141 |
| CAC benchmark ranges (USD 65-220 etc.) | Assumptions!D136 note |
| Organic share 25%; equivalent to 20% lower CAC | Assumptions!B147; 1 - 1/1.25 = 0.20 |
| Referral 0.6/yr, conversion 62%, opens M13 | Assumptions!B145, B146, B55 |
| Agents 40,40,60,177,298,356,420 | Assumptions!B107:B113 |
| Agent productivity 6/month; ramp 60%, 85% | Assumptions!B135, B121, B122 |
| Angel One 42/40/63/186/313; Prudent ~19%/yr; bottom-up ~470 (12%) | Assumptions!D113 note |
| IRDAI 8.65 policies/agent/yr; 1.5-3/month active; Bank Mitra 20-30 free, ~2 with fee | Assumptions!D135 note |
| Agent-driven accounts India Y7 30,240, 51% of raw demand | Model!AE114; AE114/AE115 = 0.507 |
| Seasonality ±25% vs ±33%; Eid moves ~11 days | Assumptions!D61 note |
| Persistency 55% | Assumptions!B133 |
| Monthly churn 4.86% | Assumptions!B134 = 0.048599 |
| Treadmill Y7 7.5 | Summary!J83 = 7.52 |
| Holders 64.7% of ever acquired Y7 | Model!AE160 / AE161 = 130,638 / 201,846 |
| Activation periods (table 3.5) | Assumptions!B47:B57 |
| India ~30% of Y7 revenue | Summary!J9 / J11 = 30.2% |
| SIP ticket 33.60 / 26.00 / 30.00 | Assumptions!B190:B192 |
| Joyalukkas AED 100 (USD 27), Malabar AED 200, AMFI USD 34, segments USD 38/26 | Assumptions!D190 note |
| Gold price M1 USD 141.46/g (USD 4,400/oz) | Assumptions!B6, D6 |
| Gold appreciation 8.1% | Assumptions!B131 |
| Gold price Y7 USD 225.73/g | Model!AE20 |
| Redemption 6%, holder multiplier 1.6, PAXG 5.9% | Assumptions!B152, B153, D152 |
| Gold moved out of control 6% | Assumptions!B151 |
| Collateral-eligible AUM Y7 USD 82.66m | Summary!J109 |

## Section 4: streams

| Figure | Source |
|---|---|
| Stream 1a Y7 1,326,088 | Summary!J14 |
| Stream 1b Y7 107,358 | Summary!J15 |
| Spot tickets 190 / 145 / 40; AED 700; AED 781; 0.77x; INR 3,300 | Assumptions!B32:B34 and notes |
| Spot attach 12% / 10% / 35% | Assumptions!B35:B37 |
| Spot frequency 1.7; INR 838 vs INR 281 (3x) | Assumptions!B156, D156 |
| Spot multipliers 0.70/1.00/1.35 and 0.50/1.00/1.70 | SP!C43:E43, C42:E42 |
| Stream 2 Y7 56,241; spend USD 7.81m | Summary!J16; Model!AE171 |
| Interchange 1.80% | Assumptions!B14 |
| Tier ladder 1.80/2.05/2.10, ~2% effect | Assumptions!D14 note |
| PM share 60%, range 36-85% | Assumptions!B157, D157 |
| Aurumix keeps 0.72% of spend | 1.80% x (1-0.60); check Summary!J16 / Model!AE171 = 0.0072 |
| Card-eligible base Y7 201,846 | Model!AE161 (= sum of rows 44, 87, 130) |
| Active cards Y7 36,332; take-up 18% | Summary!J105; Assumptions!B158 |
| Credit limit ~USD 205 book-wide Y7 | Model!AE167 / AE161 x Assumptions!B31 = 204.76 |
| LTV 50%, drawn 50%, 2.1 draws, 4 txns/draw | Assumptions!B31, B171, B173, B159 |
| Avg transaction Y7 AED 101 UAE, AED 92 India | Model!AE54, AE140 |
| Stream 3 Y7 448,317 | Summary!J17 |
| Subscribers Y7 7,599; 10.7% of paying | Model!AE59+AE102+AE145 = 7,598.6; / Summary!J102 |
| Plan price USD 50; beneficiary fee USD 6; 2.5 beneficiaries | Assumptions!B25, B26, B176 |
| Trust & Will 199+49; Farewill GBP 100+10; Epilogue CAD 139; 14% of annual saving | Assumptions!D25 note |
| Household sizes 4.4 / 4.5 / 6.8 | Assumptions!D176 note |
| Attach 15%; cancellation 25%/yr (~2.4%/month); combined 7.11%/month | Assumptions!B174, B175, B177 |
| Stream 4 Y7 952,508 | Summary!J18 |
| Stream 4 split ATM 59.8%, issuance 18.5%, reissue/replacement 16.1%, FX 5.6% | Derived from Model!AE171 (spend), AE163 (cards), AE288 (new cards) with Assumptions!B17, B160, B163:B170, B18:B21, B161:B162: FX 53,117; ATM 569,841; issuance 176,208; events 153,343; sum 952,508 |
| ATM fee ~AED 4.80/cardholder/month | (0.12 x 1,250 + 0.03 x 3,000) x 2% = AED 4.80 |
| FX 2%; foreign share 34%; ATM allowance AED 1,000; fee 2% | Assumptions!B17, B160, B18, B19 |
| ATM distribution 60/25/12/3 | Assumptions!B163:B166 |
| Issuance AED 75; replacement AED 100; reissue 6%; replacement 11% | Assumptions!B20, B21, B161, B162 |
| Stream 5 Y7 44,524; origination ~39k; servicing ~5k | Summary!J19; servicing = (Model!AE62+AE105+AE148) x 0.5% x 70% = 5,468; origination = 44,524 - 5,468 = 39,056 |
| Origination 1%, share 50%; servicing 0.5%, share 70%; turnover 0.42; 71 days | Assumptions!B27:B30, B172, D172 |
| Stream 6 Y7 1,559,250; partner AUM USD 207.9m | Summary!J20; Model!AE154 |
| Partners 0,1,3,5,7,9,11 | Assumptions!B178:B184 |
| Per-partner AUM 18.9m = 900,000 x 6% x 350 | Assumptions!B189, B186, B187, B188 |
| Botim 1.7m active; O Gold 4.4%; maturation 1.4x; USD 363; USD 302 | Assumptions!D186, D187, D188 notes |
| B2B fee 0.75%; band 0.5-0.75%; aggressive 0.90% | Assumptions!B185; SP!D79, E79 |
| One partner worth USD 141,750/yr | 18.9m x 0.75% = Summary!E20 |

## Section 5: cost base

| Figure | Source |
|---|---|
| COGS Y7 321,408 | Summary!J36 |
| Premium 1.5%; +1.71%, PAMP 1.75, Valcambi 1.67, 25 bp | Assumptions!B9, D9 |
| Opex Y7 549,459; Y1 648,974 | Summary!J49, D49 |
| Vault 0.12%, USD 25/day, Y7 110,238 | Assumptions!B193, B194; Summary!J37 |
| VARA AED 400,000 = USD 108,918 | Assumptions!B195; Summary!J39 |
| DMCC AED 20,265 = USD 5,518 | Assumptions!B197; Summary!J40 |
| KYC USD 1.85, min 299/month, Y7 88,680 | Assumptions!B199, B226; Summary!J41 |
| Insurance 45,000; audit 25,000 (5,400 + 20,000); pen test 15,000 | Assumptions!B203, B204 (+note), B205; Summary!J42:J44 |
| Buyback handling USD 1.85/event, Y7 31,105 | Assumptions!B43; Summary!J45 |
| Tech build 350k/150k; maintenance 120k | Assumptions!B222:B224; Summary!D46, E46, J47 |
| One-off Y1 84,121 (AED 150,000, AED 12,035, USD 40,000) | Summary!D48; Assumptions!B196, B198, B206 |
| ICS costs Y7 364,168 = 8.1% of revenue | Summary!J54; J54/J11 |
| ICS qualification 55%, 8 months | Assumptions!B149, B150 |
| Entry discount 25%, Y7 182,337; break-even 71.5% | Assumptions!B207, D207; Summary!J50 |
| Card discount 20%, Y7 104,776 | Assumptions!B208; Summary!J51 |
| Rebate 5%, Y7 27,741; 0.36% of spend | Assumptions!B209; Summary!J52; Model!AE265 = 0.00355 |
| Family discount 20%, Y7 49,315 | Assumptions!B210; Summary!J53 |
| Acquisition Y7 1,787,063; marketing 1.65m | Summary!J58, J55 |
| Agent commission 10% (0.5% of contribution), Y7 70,000; 15% conservative | Assumptions!B211; SP!E113; Summary!J56 |
| Referral reward 30%, Y7 67,063; USD 3.02 | Assumptions!B212, D212; Summary!J57 |
| Blended cost per new customer Y7 USD 37; Y4 USD 21 | Summary!J67, G67 |
| Card costs Y7 149,822; 14.9% of card revenue | Summary!J65, J66 |
| Card costs Y2 91,599 vs card revenue 81,989 | Summary!E65; Summary!E16+E18 |
| NymCard 30,000; setup 50,000 (Y2) | Assumptions!B213, B214; Summary!J59, E60 |
| Production USD 4, Y7 34,513 | Assumptions!B215; Summary!J61 |
| Authorisation USD 0.03, Y7 9,705; ~323,500 auths; 6% declines | Assumptions!B216, B16; Summary!J62; Model!AE196 = 323,503 |
| Fraud 0.08%, Y7 6,249 | Assumptions!B217; Summary!J63 |
| Cross-border 1.40%, Y7 69,355; UAE 10% abroad | Assumptions!B218, B219; Summary!J64 |
| Contingency Y7 475,788; Y1 112,367; headcount ~USD 588,000 | Summary!J69, D69; Assumptions!D225 note |
| Minting ~855,000 events; ~USD 8,500 L2; ~USD 1.7m mainnet | Assumptions!D224 note |
| Premium on gross switch worth USD 165,755 | Assumptions!D230 note |

## Section 6: unit economics, funding, capital

| Figure | Source |
|---|---|
| Net profit Y1 -829,064; Y4 260,844; Y7 846,578; margin 18.8% | Summary!D73, G73, J73, J74 |
| Profit before acquisition Y7 USD 2.63m | Summary!J78 |
| Contribution per paying customer Y3 USD 19, Y7 USD 37 | Summary!F79, J79 |
| Payback 15.6 / 8.9 / 8.4 / 9.9 / 12.1 months | Summary!F82:J82 |
| Y1, Y2 annual contribution negative | Derived: Summary!D78 / average Model!C159:N159 = -511; Summary!E78 / average Model!O159:Z159 = -40 |
| Treadmill 1.8 / 2.1 / 3.5 / 7.5 | Summary!D83, F83, I83, J83 |
| Peak funding 2,291,169 = 1,426,757 + 864,412 | Summary!F84; -Summary!F75; Summary!F92 |
| Paid-up capital AED 1.5m = USD 408,441; AED 600,000 = USD 163,376; total 571,818 | Assumptions!B200, B201; Summary!J87:J89 |
| Net liquid assets 1.2x; Y7 54,946 | Assumptions!B202; Summary!J90 |
| Float buffer 10 days | Assumptions!B132 |
| Float M1 200 g, USD 28,716 | Model!C206, C209 |
| Float Y7 3,406 g, USD 780,282 | Summary!J95, J96 |
| Cumulative float cash Y7 622,153 | Summary!J98 |
| Prefunding 100,000; 2 days of Y7 spend ~43,000 | Assumptions!B221, D221 note; Summary!J91 |
| Capital tied up Y7 1,452,099 | Summary!J92 |

## Section 7: scenarios and switches (RECALC)

| Figure | Cell changed | Read from |
|---|---|---|
| Conservative Y7 revenue 0.89m, NP -2.75m, cumulative -12.76m, peak 14.32m, paying 34,951, custody 21.42m | SP!B6 = "Conservative" | Summary!J11 894,803; J73 -2,751,701; J75 -12,764,159; J84 14,322,521; J102 34,951; J107 21,421,179 |
| Aggressive Y7 revenue 20.83m, NP 16.20m, cumulative 56.70m, peak 1.65m, paying 102,176, custody 276.36m | SP!B6 = "Aggressive" | Summary!J11 20,825,423; J73 16,198,070; J75 56,700,815; J84 1,654,251; J102 102,176; J107 276,360,074 |
| Conservative payback undefined | SP!B6 = "Conservative" | Summary!J82 blank; J79 = -30 |
| Holders keep card OFF: revenue 3.88m (-13.7%), NP 0.58m; whole fall in stream 4 (953k to 338k), streams 2 and 5 unchanged | SP!C131 = "OFF" | Summary!J11 3,879,534; J73 577,435; J16+J18+J19 = 438,520 vs Base 1,053,273; J16 56,241 and J19 44,524 unchanged, so J18 = 337,755 vs Base 952,508 (fall 614,753 = 4,494,287 - 3,879,534) |
| Prepaid: revenue 4.42m, NP 0.78m | SP!C130 = "Prepaid" | Summary!J11 4,424,766; J73 777,849 |

## Section 8: one-at-a-time sensitivities (RECALC)

Each run sets SP column C (Base) of the listed rows to that row's column E (Conservative) or D (Aggressive) value, selector at Base. Read Summary!J73 (Y7 net profit) and Summary!J84 (peak funding).

| Input | SP rows | NP cons | NP aggr | Peak cons |
|---|---|---|---|---|
| Partner adoption | 81 | 66,953 | 1,886,078 | 2,948,234 |
| Partner user base | 80 | 153,578 | 1,712,828 | 2,802,326 |
| B2B partners | 72:78 | -3,922 | 1,697,078 | 3,231,734 |
| AUM per partner user | 82 | 267,428 | 1,514,828 | 2,662,290 |
| B2B fee | 79 | 326,828 | 1,158,428 | 2,613,690 |
| Contingency | 127 | 370,790 | 1,005,174 | 2,783,321 |
| Facility take-up | 49 | 422,643 | 1,355,301 | 2,438,166 |
| CAC (all six) | 18:23 | 552,154 | 1,087,422 | 2,401,076 |
| Persistency | 15 | 607,114 | 1,144,389 | 2,316,234 |
| Family attach | 68 | 663,829 | 1,107,649 | 2,359,043 |
| Technology | 124:126 | 731,578 | 904,078 | 2,878,440 |
| Referral rate | 27 | 760,674 | 946,651 | 2,313,315 |
| PM share | 48 | 812,539 | 879,256 | 2,295,483 |
| Gold appreciation | 10 | 839,638 | 850,246 | 2,288,971 |
| Persistency: paying customers Y7 54,457 / 92,706 | 15 | Summary!J102 | | |

Band values quoted in the table headings: SP!D and E columns of the rows above (e.g. partners Y7 SP!E78 = 5, D78 = 17; adoption E81 3%, D81 10%; users E80 500,000, D80 1,400,000; AUM/user E82 220, D82 500; fee E79 0.50%, D79 0.90%; contingency E127 30%, D127 10%; take-up E49 8%, D49 30%; persistency E15 45%, D15 65%; family attach E68 8%, D68 25%; referral E27 0.25, D27 1.1; PM share E48 85%, D48 36%; gold E10 0%, D10 12%).

## Section 9-11

| Figure | Source |
|---|---|
| 2,000 simulation runs | 5-simulations/SIMULATION_RESULTS.md, Appendix A |
| 219 checks | verify_model.py (per task brief) |
| Switch rows 130-133; selector B6 | SP!A130:C133; SP!B6 |
| Activation rows 47-57; marketing rows 114-120; agent rows 93-113; B8; B25; SP row 79; SP row 10 | Assumptions / SP as cited |

## Added after the independent QC pass (2026-09-24)

| Figure in document | Source / derivation |
|---|---|
| Premium on gross: Y7 net profit USD 0.75m (746,385); premium +USD 183,024 and net profit -USD 210,478 over seven years | Recalculated copy, Scenario Parameters!C133 = Gross |
| Premium borne by customer: Y7 net profit USD 1.22m (1,217,232); peak funding USD 2.14m | Recalculated copy, Scenario Parameters!C132 = Customer |
| INR 1,960 a year per Indian paying customer | 0.35 attach x 1.7 purchases x INR 3,300 ticket = INR 1,963.5 |
| Roughly seven times Augmont's INR 281 | 1,963.5 / 281 = 7.0 |
| Holders outnumber paying customers from Y5 | Summary: Y4 27,756 < 31,586; Y5 53,471 > 50,383 |
| Cross-border assessment 0.89% of all card spend at Y7 | Summary Y7 assessment 69,355 / Y7 card spend |
| FX margin USD 53k at Y7 | Model stream 4 FX component, Y7 (53,117) |
| About USD 31 a month | Book-weighted SIP ticket at Y7, USD 31.04 |
| Higher interchange tiers add at most about 0.2% of total revenue | Stream 2 share 1.25% x (2.10 / 1.80 - 1) = 0.21% |
| ICS discounts cost roughly half the headline rate | 55% qualifying share: 104,776 / 952,508 = 11.0% (20% x 0.55); 27,741 / 1,008,749 = 2.75% (5% x 0.55) |
| Conservative facility take-up 8% | Scenario Parameters, facility take-up, Conservative column |
| CAC band UAE at launch USD 140 / 85 / 55; Y1 technology build USD 600k / 350k / 200k | Scenario Parameters, Conservative / Base / Aggressive columns |
