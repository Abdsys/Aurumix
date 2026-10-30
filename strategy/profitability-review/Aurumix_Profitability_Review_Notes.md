# Aurumix profitability review: working notes

*Session of 29–30 Oct 2026 (Abdur + Claude). Prep for the call with Tony and the client meeting with Gaurav and CG. Plain-English answers in the order we discussed them. The full research reports are in `research/` (round 1 = market and strategy, round 2 = token issuers, explainers and from-scratch ideas, round 3 = gold leasing and float).*

Confidence tags where they appear: (H) primary source or our model, (M) reputable secondary source, (L) estimate.

---

## 0. Where we left off (read this first on the other PC)

**The question from Tony.** After the call with CG: "right now it's not really profitable." The plan for Friday is a wrap-up plan. Ideas on the table:
1. Manual handling ("people touching it") eats margin.
2. Branding: does a branded or minted product sell for more (the Trump-gold example)?
3. CG is thinking of an infrastructure layer or protocol.
4. An AI agent the customer pays to manage their gold ("Weaver"; we could not identify it, so ask Tony for the link).

**How Abdur wants answers:** in plain terms, in chronological order, as an experienced operator would put them, practical not theoretical. No big paragraphs.

**Questions already answered (sections 2–12 below):**
- Tokenized gold vs digital gold, and where margins are made.
- Why Aurumix loses money and the step-by-step path to profit.
- A verdict on Tony's four ideas.
- How Jar, Muthoot and SafeGold work.
- How the sell-back price works.
- Whether anyone earns on holding or leasing gold.
- Whether the smaller gold-token issuers make money.
- A from-scratch design of a basic profitable gold business.

**Open next steps:**
- Brief Tony. Raise the sensitive finding first: the token is part of the margin problem.
- Ask Tony what "Weaver" is.
- Optionally turn these notes into a one-page brief for Tony, with sources.
- Questions for CG are in section 6.

---

## 1. Project context (one screen)

- **Aurumix** is a Dubai gold savings app.
  - Customers are UAE residents, mostly NRI/South Asian.
  - They save USD 20–75 a month (SIP) or buy spot.
  - The money buys allocated LBMA bars vaulted in Dubai. 1 g = 1 AURX, an open ERC-20.
- **Structure:**
  - A VARA Category 1 issuance licence is planned but not applied for.
  - A DIFC trust holds title to the gold.
  - Lending and the Gold Card run through CBUAE-licensed partners.
  - Buyback is fee-free, because VARA forbids a redemption fee.
- **Revenue model, Base case Y7:**
  - Revenue USD 4.49m, about 18.8% margin before headcount and tax.
  - Largest streams: B2B platform fee 35%, SIP entry fee 5% (30%), card fees 21%.
- **Simulation:**
  - p90 funding need USD 4.8m.
  - 43% of paths pay back by Y7.
  - With no B2B partners, none pay back.
  - Each UAE customer loses about USD 10.48 a year.
- **Repo state:** pulled to `7640428` on 29 Oct. The new `reference/regulatory-benchmarks/` folder holds UAE token documents.

---

## 2. Tokenized gold vs digital gold: two different markets

| | Tokenized gold (XAUT, PAXG) | Digital gold (Jar, PhonePe, SafeGold, OGold) |
|---|---|---|
| **Who buys** | Crypto traders, exchanges, treasuries. About 478k holders, about USD 5bn total | Ordinary savers. Jar has 35m users; OGold has about 1.5m in the UAE |
| **What for** | Trading, hedging inside crypto, collateral | Habit saving, gifting, later jewellery |
| **Fees** | 0.125–0.25% to mint or redeem, 0% storage | 2–7% spread in India (+3% GST); 0.5–2% at UAE banks, shown as "AED 0 fee" |
| **Who profits** | Exchanges, and the issuer's parent business (stablecoin float). Issuance itself is about break-even | Whoever owns the customer |
| **Regulation** | PAXG: US trust bank. XAUT: El Salvador. Dubai: VARA ARVA (AED 1.5m capital, no redemption fee) | India: unregulated (SEBI warning, Nov 2025). UAE: a DMCC entity selling through a CBUAE-licensed partner |

**What it means:** Aurumix's customers are digital-gold customers. The real competitors are OGold, SafeGold and the bank apps, not XAUT.

---

## 3. Where the money is in gold (the activities)

| Activity | Margin | Can Aurumix get it? |
|---|---|---|
| Gold loans | Very high: Muthoot makes about 30% return on equity | Only by referral to a licensed lender |
| Jewellery making charges | 3–12% in Dubai, 8–25% in India | Yes, as a referral fee |
| Small gift bars (1–10 g) | 5–60% over spot | Gifting only |
| Retail buy/sell spread | 0.5–7% | Yes, if we own the customer |
| Card FX on trips home | Net USD 7–13 per cardholder a year | Yes, through a card partner |
| Branded coins (Trump) | About 23% over melt, of which only about 8% comes from the name | No |
| Custody | 0–0.25% | No, it is priced to zero |
| B2B infrastructure | SafeGold: 0.03% EBITDA | Thin |
| Token issuance | About 0.2% or less | Thinnest |

**The pattern:** money is made at the two ends. One end is owning the customer. The other is what the gold turns into: jewellery, a gift or a loan. The middle (vaulting, issuing, plumbing) earns almost nothing.

### What happens in each activity, step by step

Gold is about USD 4,055/oz, or about USD 130/g (28 Oct 2026).

**1. Gold loans**
- You lend cash against gold held in your vault.
- The borrower pays you interest, you pay your own lenders less, and you keep the gap: about 12% a year.
- Losses are tiny because the gold covers the loan.
- Needs a lending licence and cheap capital. Muthoot is covered in section 8.

**2. Jewellery making charges**
- A Dubai jeweller prices a piece as gold weight × today's rate + a making charge + 5% VAT.
- **Example: a 20 g 22K necklace**
  - Gold USD 2,384. This passes straight through.
  - Making charge at AED 40/g: about USD 218, or 9%. This is the jeweller's money; labour is a fraction of it.
  - VAT about USD 130.
- **A second margin on resale:** you lose the making charge entirely, and the jeweller deducts a few percent from the gold value.

**3. Small gift bars**
- A refiner stamps small bars and seals each in an assay card.
- That cost is about the same for 1 g as for 100 g, so it is a large percentage on a 1 g bar. The retailer adds a markup on top.
- **Dubai prices:** a 1 g bar sells at roughly 20–60% over the gold value, a 10 g bar at 5–22%.
- **Online example:** Emirates Minting sells 1 g at AED 498, including AED 12.60 making. Al Fanan's retail price is AED 570.
- Buyback is near melt, so the buyer loses the premium. People pay for the occasion.

**4. Retail digital-gold spread.** See section 9 for how the two prices work.
- The app owns the customer and keeps most of the spread.
- The backend keeps less than 1%; the refiner keeps a fraction.

**5. Card FX on trips home**
- An NRI uses a UAE card in India. Visa or Mastercard converts INR to AED, and the issuer adds a markup.
- **Example: AED 1,000 spent**
  - A typical bank charges 3.14%, or AED 31. About AED 10 goes to the card scheme; the bank keeps about AED 21.
  - A cheaper card at 1.5–2% keeps about AED 5–10.
- UPI from NRE accounts is eating into this.

**6. Branded and collector coins**
- The mint strikes coins several times, limits the mintage, and sells them in a display case at a fixed premium.
- **Trump USD 250 proof:** estimated at about 23% over melt. A normal US Mint proof is already about 15% over, so the name adds about 8%.
- The premium fades at resale. Each household buys once.

**7. Custody**
- Bars sit with Brink's, Loomis or Malca-Amit, insured and audited.
- BullionVault charges 0.12% a year, so USD 10,000 of gold pays USD 12. XAUT, PAXG and UAE banks charge 0%.
- It is a cost to cover, not a profit line.

**8. B2B infrastructure.** SafeGold is the example; see section 10.

**9. Token issuance**
- The customer sends USD, the issuer allocates gold, and tokens are minted 1:1. An auditor attests monthly. On redemption the tokens are burned.
- The issuer earns a one-time fee of 0.125–0.25% and nothing while the customer holds.
- **Example:** USD 10m minted at 0.25% earns USD 25,000. That is less than one audit.

---

## 4. Why Aurumix is not profitable today (from our own model)

1. **Customers cost more than they bring in.**
   - CAC is USD 73 per UAE saver, against USD 33 of revenue a year.
   - About a third leave each year, giving −USD 10.48 per customer a year.
   - Paid marketing is 49% of costs.
2. **The ticket is too small for the payment rail.**
   - The average SIP is about USD 34, and a UAE direct debit costs AED 5.
   - It only works from about USD 49 a month.
3. **The token setup gives away half the spread.**
   - The VARA ARVA buyback must be fee-free, so we earn only on the way in.
   - It also means AED 1.5m of capital plus about AED 300k a year in fees.
4. **The biggest revenue line rests on unsigned deals.**
   - B2B is 35% of revenue, with zero partners signed.
   - Interchange loses money after scheme costs.
5. **Staff costs are missing.** A basic headcount line wipes out the Y7 profit. This is where "people touching it" hides.
6. **The only profitable region is closed.**
   - India made +USD 14.92 per customer, and it is excluded.
   - The p90 funding need is USD 4.8m.
- **Do not quote the "~45k accounts" breakeven.** It is stale. The current figure is about 146k paying customers on retail alone, against the plan's 88.6k.

---

## 5. Path to profitability, step by step

1. **Stop the cash going out (weeks 0–6).**
   - Pause VARA spend until counsel confirms a digital-gold-first launch: a DMCC entity plus a CBUAE-licensed partner, with the token later. SafeGold already does this in the UAE through e& money.
   - Stop paid UAE ads, and stop Oman and Bahrain marketing until those markets open.
2. **Fix the cost base (months 0–3).**
   - Buy through a dealer's pooled allocated account, saving USD 3–4 per customer.
   - Use quarterly collection or a minimum ticket, with Aani top-ups.
   - Use UAE PASS KYC.
   - Run AI-first WhatsApp support in Hindi, Urdu and Malayalam.
   - Price through the spread instead of a visible 5% fee.
3. **Earn when the gold is used (months 3–6).**
   - Sign one UAE Indian jeweller to take saved grams, with a 3–5% referral out of the making charge.
   - Launch gift grams for Eid, Diwali and Akshaya Tritiya.
   - Expect about USD 3–8 per saver a year.
4. **Get one distribution partner (months 6–12).**
   - An exchange house or WPS provider brings CAC near zero.
   - Charge about USD 3–5 per active user a year. 2.5 partners cover fixed costs.
   - **Kill rule:** no signed LOI by end of Q1 2027 means stop licensing spend.
5. **Position the card for the trip home.** Earn on FX; drop the cashback race and the ATM revenue line.
6. **Credit by referral only (later).**
7. **Fallback:** sell the book to Joyalukkas or Al Ansari.

---

## 6. Tony's four ideas: verdict

| Idea | Verdict | Why |
|---|---|---|
| Automate manual work | Do it | Real and cheap, but it saves cost and creates no margin. Pair it with the CAC and payment-rail fixes |
| Branding / Trump-style | Only narrowly | The name adds about 8%, and our bar buys back at melt. Use gifts and jewellery conversion to lift ticket size and retention |
| CG's infrastructure / protocol | Park | The lowest-margin seat (SafeGold 0.03%). Rent someone else's rails and own the NRI customer |
| Paid AI agent | Feature, not product | People barely pay for it, and once it makes decisions it needs a licence. Use it for support, nudges and payment retries |

**Questions for CG:**
1. Does "infrastructure" mean issuing tokens for others, an API for partners, or a DeFi protocol?
2. Is the token a must-have, or can it come after a digital-gold launch?
3. Which exchange houses, payroll providers or jewellers has he actually spoken to?
4. Who does the manual work today, and what is the real headcount plan?
5. How much runway is funded?
6. Will he accept a kill criterion tied to a partner LOI by end of Q1 2027?
7. Is Sharia certification planned? OGold has it.

**Talking point:** "The token earns almost nothing. Tether's customer fees on a USD 3bn token are a few million at most. Under VARA the token also stops us charging on the way out."

---

## 7. How Jar makes money (and the jewellery correction)

**The journey:**
1. A user saves ₹10 a day by UPI autopay.
2. The backend (SafeGold or Augmont) buys and vaults the gold with Brink's, under a trustee.
3. The user can sell back for cash, take coins, or convert to Nek jewellery, paying the making charge plus GST.

**What Jar did not build:**
- No gold licence: digital gold in India is unregulated.
- No vault.
- No payment licence: it uses UPI partners.

**What Jar did build:** the app, the habit, the brand and Nek. In FY25 it became the seller, buying from the backend and reselling.

**What it cost:** about USD 63m and about 4 years to reach quarterly profit.

**The numbers (FY25):**
- Filed revenue ₹2,448 cr (full gold value). Gold bought ₹2,334 cr.
- Jar's own "operating revenue" ₹208 cr.
- Net loss ₹50.5 cr. Profitable in Q4 FY25 and Q1 FY26, by the company's own claim.

**Correction:** "half of Jar's revenue is jewellery" was wrong. It divided full-price Nek sales (₹100 cr+) by net revenue. Jewellery is probably **5–15% of what Jar keeps**; the savings spread is most of it.

**UAE difference:** CBUAE Article 62 licenses even *facilitating or promoting* financial products. The UAE version of Jar needs a licensed partner underneath, as with SafeGold DMCC and e& money.

---

## 8. How Muthoot makes money

**The journey:**
1. The borrower walks into one of Muthoot's 4,968 branches with jewellery. It is appraised in minutes.
2. The loan is up to 85% LTV for loans up to ₹2.5 lakh (RBI rules from 1 Apr 2026). Muthoot's own target is about 57%.
3. Cash is paid the same day. The rate is about 12–24%, averaging about 20%.
4. The borrower repays or renews within 12 months. Unpaid loans go to auction at a minimum of 90% of market value.

**On a ₹1,00,000 loan for one year:**

| Line | ₹ |
|---|---|
| Interest earned (20.3%) | +20,300 |
| Interest paid to its own lenders | −7,400 |
| Branches, staff, vaults, losses | −2,900 |
| Tax | −2,600 |
| **Profit** | **7,500** |
| Muthoot's own money in the loan | ~24,400 |
| **Return** | **~31%** |

**FY26:** gold AUM ₹1.54 lakh cr standalone; PAT ₹10,134 cr standalone (₹10,607 cr consolidated).

**Why it works:** the gold is worth far more than the loan, it is easy to sell, and borrowers repay to get family gold back.

**Why it is hard to copy:**
- You need a licence, cheap funding at scale, and trusted branches.
- Rupeek lost ₹281 cr in one year, and its valuation fell 60%.
- Indiagold needed about 5 years and its own NBFC licence.

**The UAE:**
- Lending needs a CBUAE licence. Banks lend against gold at 8–14% and treat it as a minor product. There is no Muthoot-style lender.
- LuLu Exchange has collected Muthoot repayments from NRIs since 2022.

### Can we partner with Muthoot and take a % of interest?

In principle yes, but the economics are weak.
- **Muthoot doesn't need deals.** It has about 5,000 branches, and its AUM grew 50% last year.
- **Indian lenders pay a fixed one-time sourcing fee, not a share of interest.** A generous 1% on ₹1 lakh is ₹1,000, about USD 11.
- **The borrower is in India.** It is usually the family member, not our UAE customer.
- **Promoting a lender in the UAE can need a CBUAE licence.**
- **A better pitch** goes to a UAE bank: our customers' gold is already vaulted and verified, so lend against it in one tap and pay us referral and servicing fees.

---

## 9. Why the sell-back price is below market

It works like a currency exchange counter. Every gold seller quotes two prices: a buy price above market and a sell price below. The gap is the margin, and it is not shown as a fee.

**India example, with the market at ₹10,000/g:**

| | ₹ per gram |
|---|---|
| Buy price (+3%) | 10,300 |
| GST at 3% | +309 |
| **You pay** | **10,609** |
| **Sell-back price (−2%)** | **9,800** |

- **Round trip:** about 7–8% lost, including GST. Gold must rise about 8% just to break even.
- **UAE:** investment gold carries no VAT, and spreads are about 0.5–2%.

**Why the sell price is lower:**
1. The app has to resell the gold wholesale.
2. Prices move during the day.
3. It covers running costs.
4. Profit.

**For Aurumix:** the ARVA rules force buyback at LBMA with no spread, so Aurumix earns on one side only.

---

## 10. How SafeGold works

SafeGold is the back office for other companies' gold shops.

**What it does:**
1. Buys big bars wholesale.
2. Vaults them with Brink's, under an independent trustee.
3. Records milligram ownership for each customer.
4. Plugs into apps (PhonePe, Amazon Pay, banks, Tanishq) through an API.
5. Handles buyback, coin delivery and jewellery conversion.

**₹1,000 bought on PhonePe:**
- The gold is worth about ₹970 wholesale, plus a spread of about ₹30.
- The customer pays ₹1,000 plus ₹30 GST.
- SafeGold keeps about ₹8–9 (0.85% of the flow); PhonePe keeps the rest (the split is estimated).

**FY25:** revenue ₹6,867 cr against gold cost ₹6,809 cr, giving EBITDA of ₹2 cr (0.03%).

**Why it is thin:** partners can switch backends, and the gold flowing through inflates "revenue".

**In the UAE:** SafeGold DMCC sits behind the e& money wallet.

---

## 11. Does anyone earn on holding or leasing gold?

**Short answer:** yes, but leasing is the thin, risky way to do it. The clean earners charge a small fee on gold they hold.

| Company | How | Working? |
|---|---|---|
| Goldmoney | Storage fee paid in gold; no lending | Yes. About C$50m of metals income, a record (C$, not USD) |
| GLD ETF | 0.40% a year; leasing is forbidden | Yes. About USD 363m in fees |
| Bullion banks | Use clients' unallocated gold as funding | Yes. The client is an unsecured creditor |
| Monetary Metals (US) | Leases investor gold to jewellers at 2–4% | Running, but **a borrower (AgaBullion) defaulted in Jan 2026** |
| India GMS | Government paid 2.25–2.5% | **Closed** to new medium and long-term deposits in 2025 |
| XAUT, PAXG | Earn nothing on reserves | They choose not to lease |
| Celsius, BlockFi | Paid interest on gold tokens | Bankrupt in 2022 |
| OGold (UAE) | Advertises about 3% | Structure unverified |

**How a lease works:**
1. A jeweller borrows your gold, usually for 90–180 days.
2. The bar is no longer yours. You hold a promise of metal back.
3. The jeweller pays a fee, usually in gold.

**Example: 1 kg, about USD 135k**
- Leased at 3% to a jeweller: USD 4,050.
- After insurance and costs, you keep about 1%, or USD 1,350.
- One default loses USD 135,000, about 100 years of earnings.
- The wholesale lease rate is usually under 1%.

**For a Dubai startup:**
- Allocated gold needs explicit opt-in consent to be lent.
- VARA rule III.C.3.b bars encumbering token reserves.
- Pooling and lending gold points to a CBUAE licence.
- A fixed return raises Sharia (riba) issues.
- Realistic upside: about 0.5–1% on the opt-in slice. On USD 10m, that is USD 50–100k a year.

**Better options:**
1. A custody fee charged in grams (the Goldmoney model).
2. Cash lending against the gold through a licensed partner.

---

## 12. Do the smaller gold-token companies make money?

**No.** No company whose main business is a gold token is proven profitable. They are burning cash, closing, or carried by a parent.

| Token | Size | Main business? | Verdict |
|---|---|---|---|
| Kinesis (KAU) | $356m | Yes | Likely burning: free storage, 100–195 staff, about $2m of fees, no accounts |
| Goldfish (GGBR) | $82m on paper | Yes | Burning. Supplier lost $2.9m and has a going-concern warning; backed by gold in the ground |
| Streamex (GLDY) | $12m | Yes | Burning $1.1–1.6m a month. Stock down 91% |
| VNX Gold | $6m | Yes | Burning and shrinking; pivoted to B2B tech |
| Aurus | $6m | Yes | Near shutdown. UK strike-off notice, Sep 2026 |
| Comtech Gold (Dubai) | $3m | Mostly | Likely burning. Supply fell from 108k g to 24k g; 477 holders |
| Matrixdock (XAUm) | $70m | No (Matrixport) | Carried by parent |
| DGLD | $10m | No (MKS PAMP) | Carried by parent. Lost CHF 1.5m in 2024 |
| Zipangcoin | $25m | No (Mitsui) | Carried by parent; gold leased back to Mitsui |
| HSBC Gold Token | Not disclosed | No | Possibly profitable: HSBC owns the customer and vault, and charges up to 2% each way |
| XAUT | $3.2bn | No (Tether) | About $4.3m of fees a year, about 0.13%. Roughly break-even |

**Dead:**
- **Kinka (Japan):** closing; final buyback 30 Oct 2026. Its owner cited competitors' "overwhelming share".
- **Lode:** in liquidation.
- **CACHE Gold:** no longer gold-backed since Sep 2025.
- **Perth Mint PMGT:** discontinued.
- **Digix, GoldMint, OneGram:** faded or collapsed.
- **Royal Mint Gold:** shelved before launch.

**Lessons:**
1. Holders pay the issuer nothing.
2. Break-even needs roughly $250–500m of gold. Gold DAO earned CHF 1,000 a month, a fifth of its costs.
3. The survivors are side products of companies that already own the customer, the vault or the gold desk.
4. The money sits around the token: the purchase markup, lending, and jewellery.

---

## 13. From scratch: what basic offer makes money?

**The brief:**
- A Dubai team with NRI networks, compliance and dev skills, and USD 1–3m.
- Four teams proposed businesses (simple trade, lending, B2B, crypto-native).
- Two judges, an operator and an investor/regulator, scored 13 ideas.

| Rank | Idea | One line |
|---|---|---|
| 1 | **Gift gold for companies** | Paid upfront, no stock, simple licence |
| 2 | Gold rewards desk | Merged into #1 |
| 3 | **Old gold buying desk** | Earns per ticket, easy licence, thin spread |
| 4 | Send gold home | About AED 56 per order |
| 5 | Crypto-to-gold-bar desk | Banks may refuse crypto money |
| 6 | **Gold loan desk (a bank lends)** | Biggest pool; we earn what the bank pays us |
| 6 | Stablecoin gold loans | Needs VARA and about a USD 37m book |
| 8 | Own-brand wedding gold plan | Can't beat Malabar; may count as deposit-taking |
| 8 | Own gold-loan finance company | Needs USD 10–25m and its own licence |
| 10 | Gold credit line with a vault fee | Rests on an untested fee |
| 10 | Wedding plan inside payroll apps | About AED 44 per saver; OGold and SafeGold are already there |
| 12 | Gold leasing desk | One default wipes out decades |
| 13 | **Issue a gold token** | **Last.** Loses about USD 0.3m a year |

### Winner: a gift-gold desk for companies

- **The offer:** 1 g, 2.5 g and 10 g logo bars for Eid and Diwali gifts, long-service awards, and exchange-house prize campaigns (LuLu and Al Ansari already do these).
- **How it makes money:** the company pays 100% upfront, we buy from the mint the same day (no stock, no price risk), and we keep the gap.
- **Example: 300 × 1 g bars**
  - Cost about AED 508 a bar (mint AED 498 plus about 10 for card and delivery). Price AED 540.
  - Gross AED 9,600. After sales time and handling, about **AED 6,000 (USD 1,630) per order**.
- **Break-even:** about 40 orders a year.
- **Licence:** a DED gold-trading licence, DPMS/goAML registration and VAT. No VARA, CBUAE or CMA licence.
- **Capital:** USD 0.1–0.3m.
- **Limits:** no moat, seasonal demand, small scale.

### Runner-up: an old gold buying desk

- **The offer:** a kiosk in an exchange house buying NRI families' old 22K jewellery. Purity is tested in front of the customer and payment arrives in 15 minutes.
- **How it makes money:** we lock the sale to a refiner at the same moment we buy.
- **Example: 25 g of 22K**
  - We pay the customer 97.5% of the gold value; the refiner pays us about 99.4%.
  - About **AED 136 per ticket**. Break-even is 7–9 tickets a day.
- **The catch:** souk buyers may already pay about 98%. Then it is AED 30–80 per ticket and 15–40 tickets a day. A two-week test decides.
- **Never** give cash against gold with a right to buy it back. That is lending, and fines start at AED 1m.

### Phase 2: a gold loan desk with a CBUAE bank

- This is the Muthoot pool: we run appraisal and branches, the bank lends.
- Only proceed on a term sheet that pays us at least 6% a year for servicing. Rupeek is the warning case.

### The operator's ladder

1. **Months 0–6: gift desk.** Cash from day one, and a way in with employers and exchange houses.
2. **Months 3–9: old gold desk.** It builds appraisal skills, trust and a refiner relationship.
3. **Months 9–18: gold loan desk with a bank.** The big profit pool.
4. **Only then: an app and savings product,** sold to customers we already serve.

**Be honest with the client:** steps 1 and 2 are small, real businesses. Scale comes from lending and from owning distribution, not from the token.

---

## 14. Corrections made during the session

- **Gold price:** about USD 4,055 on 28 Oct 2026, roughly 25–28% below the January record. The record is quoted as USD 5,405 or USD 5,627 depending on source.
- **Jar:** "half of revenue from jewellery" is wrong; it is about 5–15% of what Jar keeps.
- **Goldmoney:** its figures are in Canadian dollars.
- **XAUT fees:** the widely quoted USD 5.2m included Tether's own treasury mints. DefiLlama now shows about USD 4.26m.
- **Regulator:** the CMA replaced the SCA on 1 Jan 2026. CBUAE Article 62 now licenses even facilitating financial activity.
- **Breakeven:** "~45k accounts" is stale; use about 146k paying customers on retail alone.
