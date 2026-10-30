# Aurumix: the distribution and infrastructure case

## 1. Thesis

1. Aurumix's customers buy digital gold, and the token earns almost nothing: XAUT takes about USD 5m a year on a float of about USD 2.5bn. In gold, the money goes to whoever owns the saver, and to whatever the saved gold becomes, such as jewellery or a loan.
2. Aurumix cannot afford to buy customers in the UAE. CAC is USD 73, churn is 36.5%, and each customer loses USD 10.48 a year. It should rent its product to companies that already handle NRI pay and remittances: exchange houses, WPS agents, employers and jewellers.
3. A broad gold protocol is the thinnest-margin seat in the chain (SafeGold makes 0.03% EBITDA). A startup can win a narrow corridor version: priced per active user, carrying setup fees, and linked to jewellery and gold loans, the two big margin pools Aurumix can reach without its own balance sheet.

## 2. The moves

### Move 1: White-label gold savings for exchange houses and WPS agents
- **What it is:** SIP, spot buy, nominee and family features, the credit hook and buyback, placed inside apps and payroll flows such as Al Ansari, LuLu and Joyalukkas Exchange. The partner keeps its brand and the customer. Aurumix runs the metal, the ledger, compliance and servicing.
- **Why it makes money:** it removes CAC, which is 49% of the Year 7 cost base. Exchange houses already spend on gold as prizes (Al Ansari gives weekly 8g coins, LuLu runs ComTech draws), so that marketing budget already exists and can pay for a retention product. A payday top-up inside WPS also avoids the AED 5 direct-debit charge.
- **Unit economics (proposed pricing):** USD 0.50–1.00 per active saver per month, plus 0.5–1pp of a 1.5–2% customer spread (UAE banks charge 0.5–2%). For a USD 40/month saver that is USD 6–12 in fees plus USD 2.4–4.8 of spread. Serving cost is about USD 3: vault 0.12% on a USD 1,500 balance is USD 1.80, plus support. That leaves about **USD 6–14 contribution per active user with zero CAC**. Market evidence on AUM-fee pricing suggests about USD 4, and the model assumes USD 11.
- **Effort and time to revenue:** the product mostly exists. Expect 6–12 months to first revenue [experience, unverified: onboarding at CBUAE-regulated exchange houses usually takes 2–3 quarters].
- **Licence dependency:** partners need a regulated supplier. VARA has not been applied for. Counsel should test whether a DMCC-licensed allocated gold ledger can serve the first partner, as SafeGold appears to do inside e& money [experience, unverified].
- **Biggest risk:** OGold (1.5m users, with Botim and Aspora) and SafeGold (200+ partners) pitch the same partners with a proven product. The partner holds the pricing power and can push Aurumix down toward SafeGold's margin.

### Move 2: Redeem-to-jewellery, plus savings-scheme rails for jewellers
- **What it is:** savers convert grams into jewellery at Malabar (67 UAE outlets), Joyalukkas or Kalyan. Jewellers also get a digital rail for their own 10–11 month savings schemes.
- **Why it makes money:** this is where the "shaped and branded gold" premium actually exists. Dubai making charges run 3–12%, and Titan earns 11.2% EBIT. The NRI wedding purchase is jewellery bought in the UAE: India lets 20g (men) or 40g (women) of jewellery in duty-free, bars pay about 6% duty, and Dubai is 8–12% cheaper. Jar's Nek jewellery line brings in about ₹100 cr of Jar's ₹208 cr operating revenue.
- **Unit economics:** a 3–5% referral paid out of the making charge. A 20g redemption (about USD 2,600) earns USD 78–130, which averages USD 5–8 per saver per year.
- **Effort:** 3–6 months, through commercial agreements. Counsel must confirm that a making charge is not treated as a redemption fee under VARA.
- **Biggest risk:** jewellers can run their own schemes, and Joyalukkas already owns both an exchange house and a jewellery business.

### Move 3: Sell access to the NRI corridor to gold lenders
- **What it is:** referral and repayment flows for family gold loans in India through Muthoot or Manappuram. LuLu has collected Muthoot repayments since 2022. The UAE gold-backed credit line also stays, through the CBUAE partner.
- **Why it makes money:** gold lending is the largest profit pool in the chain (Muthoot: ROE about 30%, NIM about 12.6%). Aurumix brings the audience and the lender carries the balance sheet.
- **Unit economics:** USD 27–32 per borrower a year at a 25% revenue share, or USD 4–5 averaged across all savers at 15% uptake. Today lending is USD 44.5k, 1% of revenue, because credit limits average about USD 205.
- **Effort:** 6–9 months. Aurumix's own product route into India is closed, so counsel needs to check FEMA and RBI rules on cross-border loan sourcing [experience, unverified].
- **Biggest risk:** lender appetite, and reputational exposure if a family loan goes bad.

### Move 4: Cut the cost stack before pitching partners
- **Sourcing:** buy kilobars or use a dealer's pooled allocated account. This saves 2–2.5pp, about USD 15 per customer a year at USD 50/month, which is more than the USD 10.48 loss.
- **Payment rails:** the AED 5 debit costs 7.2% of a USD 20 ticket, and the breakeven ticket is about USD 49. Move to WPS payday top-ups, Aani for spot buys, quarterly debits and an AED 250 minimum.
- **KYC:** UAE PASS with liveness checks costs AED 1.5–4 a check. Manual checks cost AED 80–250.
- **AI:** first-line WhatsApp support in Hindi, Urdu and Malayalam, with a guaranteed route to a human (Klarna cut cost per transaction from USD 0.32 to 0.19). Add rule-based nudges and retries of failed debits to lift the 53.5% pass rate at the 6-payment gate. These automations only follow rules the user sets and make no decisions for the client, which keeps them out of discretionary-management licensing.
- **Minting:** use a layer-2 network (USD 8.5k a year) instead of Ethereum mainnet (about USD 1.7m a year).
- **On "people touching it":** manual handling is real, but the model hides it in headcount it does not include. The Year 3 headcount figure alone takes Year 7 profit from USD 0.85m to about −USD 0.02m. Partners will push prices toward SafeGold's level, so automation is a condition of the B2B model.
- **Effort and risk:** 3–6 months of vendor contracts. Kilobar allocation needs about 17 bars a month at scale, and it still has to satisfy DIFC trust allocation and attestation.

### Move 5: CG's infrastructure idea, narrowed to a paid API
- **What it is:** Move 1 sold as an API: buy and sell, SIP, proof of allocation, buyback, family and will. Leave out issuing tokens for others and any DeFi collateral protocol.
- **Why it makes money:** setup fees bring cash in early, which lowers the funding need. Monthly minimums cover partners who sign and never launch.
- **Unit economics:** USD 50–100k setup plus USD 5–25k a year (tokenization-as-a-service benchmarks; Goldwise also charges B2B setup fees). Five partners bring USD 250–500k upfront.
- **Biggest risk:** the WGC/BCG Standard Gold Unit is building shared rails, and Paxos is waiving PAXG creation fees until January 2027. CGO is still about USD 20m after years of trying. Build only for partners who have signed.

## 3. Stop or deprioritise

- **Paid retail acquisition in the UAE.** It drives the whole −USD 10.48 per customer.
- **Oman and Bahrain marketing from month 1.** It takes 18% of the budget, but the region opens at month 13.
- **A 0.75%/yr AUM fee for partners.** PAXG and XAUT charge 0%, and Gulf storage runs 0.12–0.5%. Price per active user instead.
- **Monthly USD 20 direct debits.**
- **Counting on USD 570k of ATM fees.** Card spend is only USD 215 per card a year.
- **Mainnet minting, an exchange listing, or leading the partner pitch with the token.**
- **A standalone paid AI wealth manager.** Origin sells at USD 1 for the first year, 70% of US adults have little or no confidence in AI advice, and discretionary management needs a VARA M&IS licence.
- **Aurumix-branded bars as a profit line.** Buyback at melt minus under 1% wipes out the premium. The Trump coin's 23% comes from US Mint scarcity. Keep Eid, Diwali and Akshaya Tritiya gifting SKUs for retention only.

## 4. Effect on breakeven

**Today:**
- The 9-in-10 funding need is USD 4.82m, and 43% of simulated runs pay back by Year 7.
- With zero partners, no runs pay back and the need rises to USD 7.09m.
- Retail alone needs **146,289 paying customers**, against 88,594 in the plan.
- The ~45k figure comes from the older ten-year v2 run, before decisions D28–D35. Do not quote it on Friday.

**After the moves, the threshold is measured as partners × active users per partner:**
- **Fixed base:** about USD 350k (VARA, DMCC, insurance, audit, tech, card platform) plus a lean team of USD 0.6–1.3m (brief anchors: USD 588k in Year 1, USD 1.34m in Year 3). Total USD 1.0–1.7m a year.
- **Contribution per active embedded saver:** USD 15–25, made up of Move 1 (USD 6–14), jewellery (USD 5–8) and credit (USD 4–5). The low end assumes referral income is shared with the partner.
- **Breakeven:** about **40k–110k active embedded savers, midpoint about 65–70k.** That is roughly 20k per partner across 3–4 partners, or about 45 active savers per Al Ansari branch. WPS covers 5m+ workers. These numbers are plausible but unproven.
- **Funding:** cutting UAE paid acquisition (USD 1.79m a year by Year 7) and collecting setup fees could bring the 9-in-10 need toward the workbook's ~USD 2.3m. My estimate depends on the first partner going live within 12 months, because the simulation shows the 12–24 month B2B ramp is what doubles the need. Re-run the Monte Carlo with UAE CAC near zero, per-user pricing, kilobar sourcing and setup fees.
- **Honest caveat:** this concentrates the risk. With zero partners there is still zero payback. Set a kill criterion: no signed letter of intent by the end of Q1 2027 means no further VARA spend.

## 5. Sixty seconds with the founder

"Customers like the product, but the business model loses money. We pay USD 73 to win a UAE saver who brings in about USD 33 a year, and a third of them leave every year. In gold, only Jar has made that work, and it needed 35 million users. The token won't carry us either: Tether makes about USD 5m on a USD 2.5bn token. The money in gold goes to whoever owns the customer's payday, and to what the gold turns into, which is jewellery and loans. So we stop buying customers. In the next 90 days we sign one exchange house or WPS agent and one jeweller, and charge them per active user plus a setup fee. We fix bar sourcing and payment rails so we can compete with SafeGold on price, and we refer credit to lenders who carry the balance sheet. CG's infrastructure becomes the API we sell to those partners. If we can't get a signed letter of intent by the end of Q1, we stop spending on VARA."