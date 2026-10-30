# Aurumix's own economics: where the margin goes

**Source keys.** EXP = `deliverables/4-revenue-modeling/Aurumix_Revenue_Model_Explainer.md`. LED = `.../4-revenue-modeling/_explainer_numbers_ledger.md`. B3 = `.../Aurumix_Revenue_Model_Architecture_Brief_Simplified.md`. B26 = `.../Aurumix_Revenue_Model_Architecture_Brief.md`. BUILD = `.../tools/build_revenue_model.py`. ALLOC = `deliverables/2-mechanism-design/_draft_allocation-and-float.md`. PARK = `.../_parked_collection-economics-and-minimum-ticket.md`. MONEY = `.../_explainer_how-we-take-money.md`. SIM = `deliverables/5-simulations/final/SIMULATION_RESULTS.md` (same content as the root copy). P5 = `.../PHASE5_STATE.md`. HO = `handoff.md`. COND = `5-simulations/aurumix/outputs/conditions.json`. I re-ran `run_conditions.region_only()` read-only to split it line by line, and it reproduced COND exactly. No project file was edited.

## (a) Cost stack

### Per USD 75 SIP debit (Year 1)

| Line | Rate | USD | Source | In the Phase 4 P&L? |
|---|---|--:|---|---|
| Entry fee (revenue) | 5% | +3.75 | EXP §4.1 | Yes |
| Fabrication premium, 100 g bars | 1.5% on the 95% | −1.07 | EXP §5.1; HO §9 D28 | Yes. Booked as cost of goods sold; Aurumix pays it by default |
| Price gap from striking at the next LBMA fix | 0.79% | −0.59 | HO §9 D29 | **No** |
| Float cost of capital | 0.49% | −0.37 | ALLOC "Worked example" | **No**. Deleted (B3 §4); the float appears only as capital tied up |
| Payment rail, UAEDDS published tariff | AED 5 per debit | −1.36 | PARK §1 | **No**. Passed to the customer (BUILD redemption note, "the rail, D31") |
| Payment rail as drafted | 0.30% | −0.23 | ALLOC build-up table | Never corrected |
| ICS entry-fee discount, tiered customer | 25% of fee | −0.94 | EXP §5.2 | Yes |
| Agent commission, India only | 10% of fee | −0.38 | LED §5 (Assumptions!B211) | Yes |
| **Net, untiered customer, rail absorbed** | | **+0.73** | | |
| **Net, tiered customer, rail absorbed** | | **−0.21** | | |

- **The original 4.15% build-up** was 3.00 premium + 0.36 price gap + 0.49 float + 0.30 rail (ALLOC). D28 halved the premium. D29 more than doubled the price gap.
- **The modelled average ticket is USD 33.60, not 75** (EXP §3.6). At that ticket the debit nets 1.68 − 0.48 − 0.27 − 1.36 = **−USD 0.42 before any ICS discount**.
- **Break-even ticket at AED 5 per debit** is about **USD 49** (1.36 ÷ 2.785%), or **USD 89** for a tiered customer.
- **Per-account and per-stock items:** KYC USD 1.85 per check, a USD 1.85 AML re-screen on each buyback, and vault 0.12% a year of metal held (EXP §5.1).

### Per paying customer per year (Year 7 steady state, SIM Part 2 and COND)

| | UAE | India |
|---|--:|--:|
| Revenue | 32.80 (SIP fee 16.35, card fees 8.31, family 5.21, spot 1.75, interchange 0.66, lending 0.52) | 32.39 |
| Serving costs we know: premium 4.99, ICS 3.11, KYC 1.00, vault 1.00, buyback 0.21, referral 0.42 | −10.73 | −12.10 |
| Card programme | −1.64 | −2.51 |
| Replacement marketing (CAC × churn) | −26.67 (USD 73 × 36.5%) | −2.16 |
| 15% contingency on uncertain lines | −4.25 | −0.70 |
| **Left over** | **−10.48** | **+14.92** |
| Fixed costs per payer at this scale (VARA 3.51, tech 3.86, insurance 1.45, audit and other 1.47) | ≈ −10.29 | ≈ −6.6 |

## (b) Where margin leaks

1. **It leaks through acquisition, not through serving.** Serving a UAE customer costs USD 10.73 a year. Replacing the ones who leave costs USD 30.67 including contingency.
   - Acquisition is USD 1.79m, **49% of the Year 7 cost base** (EXP §2.1).
   - Year 7 needs 7.5 new customers for each net addition (EXP §5.5).
   - The UAE loss is purely CAC. The UAE line is USD 58.58 against USD 74.19 today (SIM Part 5).
2. **Revenue comes from money flowing in. Costs come from the gold held.**
   - At Year 7 there are 130,638 holders against 71,208 payers: 64.7% of the book (EXP §2.1, §3.4).
   - Holders pay no entry fee. Storage is free (decision 42, BUILD storage note). An exit fee is forbidden (EXP §6.6).
   - Yet holders stay in vault cost and AML screening indefinitely (B3 §3.2).
   - Nothing charges for the gold held except B2B.
3. **The bank rail charges a fixed fee per debit on a small ticket.** C_min = R ÷ (f − c) (PARK §2). The model passes the rail to the customer. A USD 33.60 saver then pays about 4% on top of the 5% fee, and no customer-facing number shows it.
4. **Payment gaps.** Customers pay in 78% of eligible months. That cuts revenue per customer from USD 38 to 32, while costs stay the same (SIM Part 2).
5. **Fixed versus variable costs.**
   - Fixed: USD 319,436 a year (VARA plus DMCC 114,436, plus insurance, audits and tech 205,000; SIM Part 2), plus USD 30k card platform.
   - Variable: USD 11.41 per customer known and USD 15.95 uncertain (SIM Part 2).
6. **Manual operations are not priced. They hide in the missing headcount.**
   - Buyback handling was cut from USD 3.20 to 1.85 a buyback. The removed ~USD 1.35 of staff handling is "assumed to sit inside headcount" (BUILD, `redemption_cost` note), and headcount is not modelled.
   - Agent recruitment and management are not priced (P5 §5). At 45% attrition, holding 200 agents takes about 90 recruits a year (B26 §7.3).
   - Partner sales and integration are not priced (SIM Part 4).
   - Support cost per account is "unquantified" (PARK §4, factor 3).
   - Treasury runs a bar purchase about every 8.7 days in Year 1, plus monthly allocation reports and attestations (ALLOC).
7. **The loyalty ladder** costs USD 364k, 8.1% of revenue (EXP §5.2). Depending on design it ranges from 5.1% to 16.8% (SIM Appendix C).

## (c) Revenue streams ranked (Year 7 Base, EXP §2.1)

| Stream | USD | Share | Weakness |
|---|--:|--:|---|
| B2B platform fee | 1,559,250 | 34.7% | Zero partners signed. The fee sits at the top of the cited 0.5–0.75% band (BUILD `b2b_fee`). Charged in full from signing (EXP §6.5). **No vault cost on partner gold**: vault metal = customer gold + float only (BUILD `storage_grams`). At 0.12% on USD 207.9m that is ~USD 250k, if Aurumix vaults it |
| SIP entry fee | 1,326,088 | 29.5% | Gross figure. Stream 1 net of premium is USD 1.11m (EXP §2.2); less the ICS discount it is ~USD 0.93m. Entry fees alone never break even (HO §9) |
| Cardholder fees | 952,508 | 21.2% | 59.8% is ATM fees (~USD 570k). See (f)5 |
| Family plan | 448,317 | 10.0% | The 15% attach rate is a client instruction with no evidence (EXP §4.3) |
| Spot entry fee | 107,358 | 2.4% | Little volume |
| Interchange | 56,241 | 1.3% | Aurumix keeps 1.80% × 40% = 0.72% of spend. The cross-border scheme assessment alone is 0.89% of spend (EXP §5.3), so **the stream is negative after scheme costs**. Spend is about USD 215 per card a year (USD 7.81m ÷ 36,332) |
| Lending revenue share | 44,524 | 1.0% | Credit limit is about USD 205 per customer (EXP §4.2). Origination brings in 39k, servicing 5k (LED §4) |

## (d) Levers that move breakeven

| Lever | Effect | Source |
|---|---|---|
| Partner adoption / gold per user / B2B fee | Year 7 profit swings of USD 1.50m / 1.03m / 0.71m | SIM Part 2 tornado |
| Partner count | 2.5 partners cover fixed costs. Zero partners: 0% of runs pay back, USD 7.09m needed. 14 partners are needed at today's CAC; the plan has 11 | SIM Parts 2–3 |
| Card take-up 18% → 30% | +USD 1.32m | SIM Part 4 |
| CAC | At 1.66× cost, no partner count works. A cost 17% lower lets 11 partners clear | SIM Part 2 |
| Marketing split moved to India (40/10/50) | +USD 688k, but see (f)1 | SIM Part 4 |
| Faster partner onboarding / 3 more partners | +USD 517k / +415k | SIM Part 4 |
| Ticket +20% / retention +10pp / automatic payments 30→75% | +374k / +270k / +217k | SIM Part 4 |
| Six-payment gate | Weak lever. Payment discipline moves only USD 1.02 per customer (SIM Part 5). Decision 57 opened the card to everyone, so the gate now unlocks mainly ICS costs. Prefunded payments lift the gate share from 50.6% to 59.1% and entry revenue by 16% | SIM Part 5; HO §6 decision 57; `outputs/analysis_report.txt` Q3/Q6 |
| Contingency 15% → 30% | Retail alone would need more customers than exist | SIM Part 2 |
| Gold price | ~USD 5k, effectively nothing | SIM Part 3 |

Thresholds:
- **Retail alone needs 146,289 paying customers.** The plan reaches 88,594, and the reachable market is 303,615 (SIM Part 2; EXP §3.2).
- **The older "~45,102 contributing accounts" figure (HO §9) predates D28–D35 and comes from the ten-year v2.0 run.** Do not quote it alongside 146,289.

## (e) Fixed cost base and what is missing

**Modelled, Year 7** (EXP §5.1, §5.3, §5.6):
- VARA USD 108,918 and DMCC 5,518.
- Insurance 45,000, audit 25,000, tech audit 15,000, tech maintenance 120,000.
- Card platform 30,000.

**One-off:** tech build USD 350k in Year 1 and 150k in Year 2. Year 1 licensing USD 84,121. Card setup 50k.

**Capital tied up:**
- Regulatory capital USD 571,818.
- Float USD 780k at Year 7.
- Card prefunding USD 100k.

**Not modelled:** headcount, legal and trust, security, office and visas, tax, on-chain minting.
- The brief benchmarks headcount at **USD 588k in Year 1, 1.34m in Year 3 and 4.6m in Year 10** (B26 §7.4), plus an MLRO at USD 49k in Year 1.
- The 15% contingency covers "a fifth of one missing block" (BUILD `cost_contingency` note).
- **Swapping the contingency for just the Year 3 headcount anchor turns Year 7 profit from USD 0.85m to about −USD 0.02m** (846,578 + 475,788 − 1,340,000).

**Funding gap.** The workbook's peak funding need is USD 2.29m (EXP §5.6). The simulation's 9-in-10 figure is USD 4.82m, and only 43% of runs pay back by Year 7 (SIM Part 1).

## (f) Internal contradictions

1. **India.**
   - India is 30.2% of Year 7 revenue (EXP §6.5; LED Summary!J9/J11).
   - It is the only region that makes money per customer (+USD 14.92; SIM Part 2).
   - It holds all 420 agents.
   - Moving marketing there is the top recommended decision (SIM Part 4).
   - Yet MONEY §5 and §7 say "Closed… four independent bars… Delete the row", and decision 27 agrees.
   - The model simply "assumes the route is solved" (B3 §4).
   - **Without India, every retail region loses money per customer:** UAE −10.48, Oman and Bahrain −9.20.
2. **Oman and Bahrain.**
   - 18% of marketing is spent from month 1, but the region opens at month 13 (EXP §6.6).
   - Bahrain needs CBB approval, BD 50k of capital and a locally licensed advisor (HO §5).
3. **Who pays the fabrication premium.**
   - B3 §1 and §3.3 say the customer bears it, through fewer grams. EXP §1.1 and §6.2 default to Aurumix bearing it. Flipping the switch moves Year 7 profit from USD 0.85m to 1.22m.
   - Separately, "100% of every dollar buys gold" (HO §4) conflicts with "5% fee, 95% buys gold" (EXP §1.1).
4. **Rail.** ALLOC still carries 0.30%. PARK puts the published tariff at 1.81% on USD 75 and 6.8% on USD 20. The model passes the rail to the customer (D31). Decision 55 keeps the USD 20 floor "conditional on the rail price".
5. **ATM fees.**
   - About USD 570k (12.7% of total revenue) comes from cash withdrawals. 15% of cardholders are assumed to draw AED 2,250–4,000 a month (BUILD ATM rows).
   - Against that, the credit limit is about USD 205 and card spend about USD 215 a year.
   - This only holds if the Gold Card becomes the customer's main salary card. HO §9 lists that as an open question.
6. **Card rewards defect.** The rewards cost is understated about twentyfold, and the FX discount is applied to fees that contain no FX. Both were logged and never fixed (HO §9, Phase 5 note 1).
7. **Minting.** The whitepaper says ERC-20 on Ethereum (HO §0). Minting costs about USD 8.5k a year on a layer-2 network against about **USD 1.7m a year on mainnet** (EXP §5.4; ~855k mint events, LED §5). Neither number is in the cost base.
8. **B2B ramp.** The workbook has no ramp. The simulation uses 12–24 months, which is part of why its funding need is about twice the workbook's (SIM Part 2).
9. **Credit terms.** Decision 57 sets a 40% LTV base, but the workbook uses 50% (EXP §4.2). Decision 54's lapsed-cardholder check is still owed (P5 §0).
10. **Persistency.** The 55% persistency anchors cannot be traced back to a source; `VALIDATION.md` was deleted (B3 §0).

**Bottom line for the Friday meeting:**
- The retail product is a way to acquire customers whose cost is not recovered outside India, and India is legally closed.
- Serving and manual costs are small in the model only because the people doing that work (headcount) are left out.
- Profit rests on B2B partner fees with no partner signed, and on cardholder fees, most of which come from an ATM assumption that does not fit the card's credit limit.