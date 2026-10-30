# Aurumix: the case for a gold-secured credit and spending business

## 1. Thesis

- Aurumix sells to digital-gold customers. In digital gold, the money goes to whoever owns the customer's money flow. The token and the 5% entry fee bring customers in, but on savings fees alone each UAE customer loses USD 10.48 a year.
- The richest money in gold comes from lending against it and from card spend. Muthoot earns a net interest margin (NIM) of about 12.6% and a return on equity (ROE) of about 30%. The collateral already sits in a vault held by Aurumix's own trust. The job is to turn 130k holders into a secured credit and spending book, with a lender licensed by the UAE central bank (CBUAE) carrying the loans on its balance sheet.
- Fix distribution through payroll, and fix the cost of serving each customer, first. A USD 73 customer acquisition cost (CAC), and an AED 5 debit fee on a USD 34 payment, will sink any product built on top.

## 2. The moves

### Move 1. Make the gold credit line the profit engine

- **What:** a revolving credit line against the customer's vaulted gold, unlocked after about 6 months of saving. A CBUAE-licensed finance company or bank is the lender. Aurumix finds the borrowers, services the loans, runs the loan-to-value (LTV) engine and acts as collateral agent.
- **Why it makes money:** the collateral is allocated, priced live and held in a vault Aurumix controls. Losses are close to zero and underwriting is cheap. Today the line is about USD 205 per customer and brings in USD 0.52 per paying customer.
- **Unit economics [assumption]:**
  - A borrower holds about USD 2,000 of gold, borrows at 50-60% LTV and has about USD 900 drawn.
  - Priced at 15-18% APR. UAE bank gold loans charge 8-14%, but they need a branch visit and a larger loan.
  - Take off lender funding of about 5-6% [experience, unverified], losses of about 1% and servicing of about 1.5%. That leaves about 8-9% net, or about USD 75 per borrower per year.
  - Aurumix keeps about USD 20 on a 25% referral share, or USD 35-40 on a 45-50% risk share backed by a first-loss deposit.
  - At 20% uptake that is USD 4-8 per paying customer, 8-15 times today's figure.
- **Effort:** 6-9 months to sign a risk-share deal and change the trust deed. Revenue starts around month 9.
- **Dependencies:** a CBUAE-licensed lender. The DIFC trust deed has to allow customers to pledge their share of the gold. The token has to be lockable while it is pledged.
- **Biggest risk: can the pledge be enforced?** An open ERC-20 token can be moved out mid-loan, and nobody has tested a pledge from a DIFC trust to an onshore lender. Gold is down 27% from its January peak, so the line also needs automatic top-up calls and liquidation at preset LTV levels. Counsel should look at this before anything else.

### Move 2. Win the salary: the Gold Card as a payroll card

- **What:** sign an exchange house that acts as a Wage Protection System (WPS) agent (Al Ansari is one) and 2-3 large employers. Salaries land on the Aurumix Gold Card, and a set percentage moves into gold on payday.
- **Why it makes money:**
  - The payday sweep happens inside Aurumix's own ledger, so there is no AED 5 debit fee.
  - Payments happen automatically. In the simulation, prepaid payments already lift the share of accounts passing the 6-payment gate from 50.6% to 59.1%.
  - Salary data helps underwrite Move 1.
  - WPS moves more than AED 35bn a month for more than 5m workers.
- **Unit economics per salary-card customer [assumption]:**

| Line | USD per year |
|---|--:|
| Spend of AED 2,000/month × 0.75% interchange cap × 45% programme share | ~22 |
| FX on USD 1,200 spent abroad at 1.5-2% (banks charge 3.14%) | 18-24 |
| Entry fees on a USD 50/month sweep, with no payment-rail cost | ~30 |
| **Total** | **~70** |

  That compares with USD 32.80 of revenue per customer today. Partner-led acquisition at about USD 10-20 per activated account replaces the USD 73 paid CAC.
- **Effort:** 6-12 months. Selling to employers is slow.
- **Dependencies:** a CBUAE-licensed card issuer, the WPS agent, and employer HR teams.
- **Biggest risk:** the exchange house plugs in O Gold or SafeGold instead. Aurumix has to win on the credit line and family features, and it has to move fast.

### Move 3. Cut the cost of serving each customer

- **Sourcing:** buy kilobars, which trade in Dubai within ±1% of London and usually at or below it. Until volume reaches about 17 kilobars a month, use a dealer's pooled allocated account. Allocate fractions against a list of serial-numbered bars. This removes most of the 1.5% fabrication premium, about USD 3.50 of the USD 4.99 per UAE paying customer.
- **Payment rails:** at AED 5 per UAEDDS debit, the modelled USD 33.60 payment loses USD 0.42 per collection. Breakeven is about USD 49. Use:
  - an AED 250 minimum or quarterly collection
  - Aani for top-ups
  - Jaywan for debit-card acquiring
  - the payroll sweep wherever possible
- **KYC and support:**
  - UAE PASS plus liveness checks cost AED 1.5-4 per check, against AED 80-250 for manual KYC.
  - Use AI-first WhatsApp support in Hindi, Urdu and Malayalam, with a guaranteed route to a human. Klarna cut its cost per transaction from USD 0.32 to USD 0.19 this way.
- **People:** the cost of manual handling ("people touching it") is real, but it does not show in the model because headcount is left out. The Year 3 headcount benchmark alone (USD 1.34m) wipes out Year 7 profit. Automate treasury, reconciliation and buyback handling, then budget for the team that remains.
- **Effort:** 0-3 months, mostly decisions and vendor contracts. **Risk:** low.

### Move 4. Let savers redeem into jewellery

- **What:** savers can redeem grams into jewellery at partner jewellers for weddings and trips home. Malabar alone has 67 UAE outlets. Jewellery goes into India duty-free (20g for men, 40g for women), while bars pay about 6% duty.
- **Economics:**
  - Aurumix earns a 3-5% referral fee out of the jeweller's 8-25% making charge.
  - If 25% of savers redeem 20g every 4 years, that is about USD 5-8 per customer per year.
  - Jar's Nek jewellery line brings in about ₹100 cr of Jar's ₹208 cr operating revenue.
- **Effort:** 2-4 months. It only needs a commercial contract. Counsel must confirm the jeweller's making charge does not count as an Aurumix redemption fee.
- **Risk:** every redemption shrinks the collateral available for Move 1. Market it for the wedding moment only.

### Move 5 (optional). Help families in India borrow against their gold

- **What:** refer the customer's family to Muthoot or Manappuram, and collect loan repayments from the customer's UAE salary card. LuLu Exchange has collected Muthoot repayments since 2022.
- **Economics:** referral fees of about 0.5-1% of the loan [experience, unverified] on loans of about USD 1,100 [experience, unverified] come to USD 5-11 per loan. The revenue is small, but it puts Aurumix into the customer's remittance decisions.
- **Risk:** India is closed for Aurumix retail (decision 27). Counsel must confirm that referrals and repayment collection fall outside that.

## 3. Stop or deprioritise

- **The B2B 0.75% fee on partner gold as 35% of revenue.** No partner is signed. It puts Aurumix in SafeGold's position, and SafeGold earns 0.03% EBITDA. PAXG and XAUT charge 0% storage. Take it out of the base case and offer partners a retention product priced per active user.
- **A protocol or infrastructure layer.** SafeGold makes 0.03% EBITDA, Securitize is losing money, and the World Gold Council is building shared industry rails. Ask CG which he means: (a) issuing tokens for others, (b) an API for partners, or (c) a DeFi collateral protocol. Only (b) fits, and only as a distribution deal.
- **A brand premium on the token.** A token bought back at the LBMA fix cannot hold a premium. Branded 1-10g gifting bars made through a partner can be a retention tool.
- **A paid AI agent.**
  - An agent that makes decisions for the client needs a VARA Management & Investment Services licence or a licence from the UAE securities regulator (SCA).
  - Origin sells its AI advisor at USD 1 for the first year, and about 70% of US adults have little or no confidence in AI money advice.
  - Bundle rule-based automation (sweeps, retries, nudges) into the family plan.
  - We could not identify Tony's "Weaver" and should ask him for the link.
- **Smaller items:**
  - monthly USD 20 direct debits
  - Ethereum mainnet minting (about USD 1.7m a year, against about USD 8.5k on a layer-2 network)
  - Oman and Bahrain marketing before month 13
  - the ATM revenue line, unless the card becomes the customer's salary card
- **Leasing customer gold**, until counsel confirms it does not break allocation.

## 4. What this does to breakeven

The ~45k accounts figure predates decisions D28-D35. The current model says retail alone needs about 146k paying customers, and the plan reaches 88.6k.

| USD per UAE paying customer per year | Today | With the moves [assumption] |
|---|--:|--:|
| Entry fees (SIP + spot) | 18.10 | 18.10 |
| Card fees + interchange | 8.97 | ~17 (30% use it as their salary card) |
| Family plan | 5.21 | 5.21 |
| Lending | 0.52 | ~8 |
| Jewellery referral | 0 | ~3 |
| Serving costs | −10.73 | ~−7.2 |
| Card programme + credit operations | −1.64 | ~−5.5 |
| Replacement marketing | −26.67 | ~−12 (CAC ~USD 42, churn 30%) |
| Contingency | −4.25 | ~−5 |
| **Contribution** | **−10.48** | **~+21** |

- **Like-for-like with the model, which leaves out headcount:** about USD 350k of fixed costs needs about 17k paying customers.
- **With a real team (the USD 1.34m Year 3 benchmark):** about USD 1.7m of fixed costs ÷ USD 21 is about 80k paying customers. That is inside the plan's 88.6k, with no B2B fee in the numbers. Today, no simulation path pays back without B2B partners.
- **Funding:** acquisition is 49% of the Year 7 cost base, so halving blended CAC is the biggest cut. Our rough estimate is a p90 cash burn of about USD 3-3.5m, down from USD 4.8m. If Aurumix takes the risk share, add a first-loss deposit of about USD 0.7m (5% of a book of about USD 14m). That deposit can be recovered. Re-run the Monte Carlo before quoting any of these figures.

## 5. Sixty seconds with the founder

"Gaurav, the gold is your hook and your collateral. On savings fees alone a UAE customer costs you about ten dollars a year, because you pay USD 73 to win them and a third leave every year. Three things change that. First, get salaries paid onto the Gold Card through an exchange house and a few large employers. That cuts what you pay to win a customer, gets rid of the debit fee and makes saving automatic. Second, turn the gold people hold into a credit line with a licensed lender, and share the margin. That is where Muthoot earns 30% on its equity. Third, cut what it costs to buy and handle the gold: kilobars, cheaper payment rails, digital KYC and AI support. Park the protocol, the paid AI agent and the fee on partner gold. Do this and the business breaks even at around 80,000 paying customers with a real team, and it doesn't need a single B2B fee. This quarter, the first jobs are a term sheet with a lender and one payroll pilot."