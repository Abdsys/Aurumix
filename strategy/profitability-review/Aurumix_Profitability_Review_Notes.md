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
- **Landscape brief for the 30 Oct CG meeting: section 15.**

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

---

## 15. The full landscape, for the CG meeting (30 Oct)

*Built only from sections 2–13 and `research/`. No new research. Purpose: show CG where the money is and isn't, so the meeting can pick a direction.*

### 15.1 The market in one picture

**Two markets that both say "gold", but sell to different people:**

| | Digital gold | Tokenized gold |
|---|---|---|
| **What the customer holds** | Grams in an account. A company owns the bars for them under a trustee | A crypto token, 1 token = 1 oz (XAUT, PAXG) or 1 g (KAU) |
| **Who buys** | Ordinary savers, first-timers, small tickets | Crypto traders, exchanges, treasuries |
| **Size** | India UPI: about ₹2,450 cr a month (May 2026), about USD 3.4bn a year (L). Jar alone has 35m users; OGold has 1.5m in the UAE | About USD 5.2bn of tokens and 478k holders worldwide. XAUT and PAXG are about 90% of it |
| **Typical ticket** | ₹98 in India. Dh700 average in the UAE, and 64% of buys are under Dh500 | USD 200k minimum to buy direct from Tether. Retail buys on exchanges |
| **How it's used** | Save, gift, turn into jewellery | Trade, hedge inside crypto, collateral. Traded about 16x its size per quarter |
| **What the customer pays** | 2–7% spread in India (+3% GST). 0.5–2% at UAE banks, shown as "AED 0 fee" | 0.125–0.25% to mint or redeem. 0% storage |

**The chain, from mine to customer.** Every player sits in one or two of these seats:

| # | Seat | What happens there | Example players |
|---|---|---|---|
| 1 | Refiner / mint | Melts, purifies, makes bars and coins | PAMP, MMTC-PAMP, Augmont, Emirates Minting, Valcambi |
| 2 | Wholesale and vault | Trades kilobars, stores them insured | Bullion banks, DMCC dealers, Brink's, Transguard, Malca-Amit |
| 3a | Digital-gold backend | Is the legal seller. Quotes price, buys bars, keeps the ledger, handles buyback | SafeGold, Augmont, MMTC-PAMP, OGold |
| 3b | Token issuer | Buys bars, mints tokens 1:1, gets audited monthly | Tether (XAUT), Paxos (PAXG), Kinesis, Comtech |
| 4 | Front end (owns the customer) | The app or bank the customer actually uses | Jar, PhonePe, GPay, Paytm, Botim, e& money, ENBD, Liv; for tokens, Binance and other exchanges |
| 5 | What the gold turns into | Cash, jewellery, a gift, a loan | Malabar, Joyalukkas, Kalyan, Tanishq, Muthoot, UAE banks |

### 15.2 The players, seat by seat, and how each makes money

**Seat 1: Refiners and mints. Huge volume, tiny margin.**

| Player | What it is | How it makes money | Numbers |
|---|---|---|---|
| **PAMP / MKS PAMP** (Switzerland) | One of the world's big refiners and bullion traders, 1,500+ staff. The PAMP brand is on small bars sold in Dubai shops | Refining fees, bar making, trading spreads, vaulting. Its gold token (DGLD) is a side product | DGLD lost CHF 1.54m in 2024; MKS PAMP pays for it (H). In Dubai a PAMP 1 g bar retails at about +20% over gold value, and up to +61% in some shops (L). Most of that is the shop's markup |
| **MMTC-PAMP** (India) | LBMA refiner in India. Backend for Paytm and GPay, plus its own app | Bullion sales; digital gold is a small channel | FY24 revenue ₹37,837 cr, profit ₹477 cr, about 1.3% (L, aggregator) |
| **Augmont** (India) | Refiner, B2B bullion trader, digital-gold backend, and its own "Gold For All" app. IPO filed | Mostly B2B bullion (93–96% of revenue) | FY25 revenue ₹66,231 cr, profit ₹227 cr: **0.34% margin** (M). Real money in absolute terms, on razor-thin percentages |
| **Emirates Minting / Emirates Gold** (UAE) | Local mints | Making charge on small bars | 1 g bar making charge only AED 12.60, about 2.6% (M) |

- **The point:** refiners win on scale (billions of dollars a year). Digital gold is a way to sell more of their bars, not a profit line.

**Seat 3a: Digital-gold backends (the "infrastructure" CG is thinking about). Thinnest seat.**

| Player | What it is | How it makes money | Numbers |
|---|---|---|---|
| **SafeGold** (India, now UAE) | The back office behind PhonePe, Amazon Pay, Axis, Jar, Tanishq and others. In the UAE it is SafeGold Precious Metal **DMCC**, sitting behind the **e& money** wallet since Apr 2026. No VARA licence | A small cut of the spread. Partner app keeps the rest. Plus storage after 2 years, minting and delivery fees | FY25: ₹6,867 cr of gold sold, 0.85% gross, **₹2 cr EBITDA = 0.03%**, net loss ₹12.2 cr (H). Raised only about USD 2.4m |
| **OGold** (UAE) | Both a backend and an app. OGOLD Precious Metals Trading LLC (DMCC). Powers **Botim** (8.5m UAE users) since Aug 2025, partners with **Aspora** (Indian diaspora remittance) | Spread on buys and sells, a gold Mastercard, gift and jewellery marketplace in the app. Advertises about 3% yield in grams | **1.5m users** (Jul 2026), AED 1 minimum, Sharia certified (M). No P&L published. How it funds the 3% is unverified, and its own terms disclaim a guaranteed return |

- **Why this seat is thin:** the partner app owns the customer and can switch backend. The product is identical everywhere. The backend carries the vault, insurance, audit and tech costs.
- **For CG:** this is the "protocol / infrastructure" seat. In the UAE it is **already taken** by SafeGold (e&) and OGold (Botim).

**Seat 3b: Token issuers. Holders pay nothing; almost all are burning cash or carried by a parent.**

| Player | How it makes money | Numbers | Verdict |
|---|---|---|---|
| **Tether (XAUT)** | 0.25% to mint, 0.25% to redeem, 0% storage | About USD 4.3m of fees a year on USD 3.2bn (about 0.13%). Tether made USD 10bn+ in 2025 from interest on its stablecoin reserves | Roughly break-even. A showcase product |
| **Paxos (PAXG)** | Redemption fee 0.125–0.5%; creation fee **waived** until Jan 2027 | Fees about USD 1.5–3.5m (L). Paxos earns its money on stablecoin reserves (PYUSD for PayPal) | Grabbing share, not earning |
| **Kinesis (KAU)** | 0.22% per trade, 0.45% per transfer; gives over half back as "yield" | USD 356m of gold, about USD 2m of fees, 100–195 staff | Likely burning |
| **Small issuers** (Comtech in Dubai, VNX, Aurus, Streamex, Goldfish, DGLD and more) | Same model | Comtech supply fell from 108k g to 24k g, 477 holders. Streamex burns USD 1.1–1.6m a month | Burning, shrinking or shut. Kinka, Lode, CACHE, Perth Mint, Digix are dead |

- **Rule of thumb:** an issuer needs roughly USD 250–500m of gold (some estimates say up to USD 1bn) before fees cover a regulated setup.
- **Who actually earns in tokenized gold:** the **exchanges** (Binance and others), on spot trading and gold perpetuals. Gold perps now trade about USD 4.4bn a day with no vault behind them.

**Seat 4: Front ends that own the customer. This is where the spread goes.**

| Player | Where | How it makes money | Numbers |
|---|---|---|---|
| **Jar** | India | Daily ₹10 auto-save. Keeps most of the spread; Nek jewellery on top. Became the legal seller in FY25 | ₹208 cr operating revenue, profitable in Q4 FY25 and Q1 FY26 (company claim). Took about USD 63m and 4 years |
| **PhonePe, GPay, Paytm** | India | Commission on each buy, sell, SIP and redemption from the backend | Spread 4–6% at PhonePe. Gold P&L not disclosed |
| **Botim, e& money** | UAE | Same model: a gold screen in a big app, backend plugged in | Botim + OGold; e& money + SafeGold |
| **UAE banks** (ENBD, Liv, Mashreq, ADCB, FAB, Emirates Islamic) | UAE | Gold is a free feature. They earn a hidden 0.5–2% spread | "AED 0 fee" is the market's anchor price |
| **Goldmoney, BullionVault** | West | Storage fee on big balances (0.12–0.5% a year) plus about 0.5% to trade | BullionVault users hold about USD 80k each. Goldmoney: about C$4.5bn client assets, about C$50m metals income, helped by the gold rally |
| **Revolut** | West | 0.49–0.99% order fee plus a markup. Gold pushes users to paid plans | Feature, not a business |

- **The pattern:** whoever owns the customer's payment habit keeps the margin. Jar got there only with near-zero CAC and huge volume.

**Seat 5: What the gold turns into. The richest seat.**

| Player | How it makes money | Numbers |
|---|---|---|
| **Jewellers** (Malabar: 67 UAE outlets; Joyalukkas: also owns a 34-branch exchange house; Kalyan; Tanishq) | Making charges: 3–12% in Dubai, 7–25% in India. Savings schemes lock customers in for 10–11 months | Titan jewellery gross margin 19.7%, EBIT 11.2%. Coins *lower* Titan's margin |
| **Gold lenders** (Muthoot, Manappuram) | Lend against jewellery at about 20%, borrow at about 7–8% | Muthoot FY26 profit ₹10,134 cr, return on equity about 30% |
| **UAE banks lending on gold** | 8–14% at 70–80% LTV | Minor product; no Muthoot-style lender in the UAE |
| **Exchange houses** (Al Ansari, LuLu) | Use gold as a marketing prize; LuLu collects Muthoot loan repayments from NRIs | Gold is a cost for them, which makes them a buyer of gold products |

### 15.3 Where the money is made (by activity)

| Activity | Margin | Who keeps it | Why they can |
|---|---|---|---|
| Gold loans | About 30% return on equity | Muthoot, banks | Licence + cheap capital + trust |
| Jewellery making charges | 3–25% | Jewellers | Craft, stores, the wedding moment |
| Small bars and gifts (1–10 g) | 5–60% over gold value | Retail shops more than mints | Occasion buying; shelf space |
| Retail digital-gold spread | 0.5–7% | The app that owns the customer | Habit + near-zero CAC |
| Card FX on trips home | USD 7–13 per cardholder a year | Issuing bank / programme | Bank FX fees are 3.14%, so there's room |
| Branded coins (Trump) | About 23% over melt, ~8% from the name | Owner of a scarce sovereign brand | One per household, US Mint |
| Custody | 0–0.25% a year | Nobody much | Priced to zero by XAUT, PAXG, banks |
| B2B infrastructure | 0.03% EBITDA (SafeGold) | Nobody much | Partners switch backends |
| Token issuance | About 0.13–0.25% | Nobody much | Holders pay nothing |

**One sentence for CG:** the money is at the two ends of the chain (owning the customer, and what the gold becomes: jewellery, a gift, a loan). The middle (vault, ledger, token, protocol) earns almost nothing.

### 15.4 Where the money is hard to make for Aurumix (given how we are set up today)

**How we are positioned:** Dubai, NRI savers, USD 20–75 a month, a VARA token planned, no distribution partner signed, no brand, no balance sheet, no lending licence.

| Pool | Why it's hard for us |
|---|---|
| **Token issuance** | Earns 0.13–0.25%. Under VARA ARVA we also can't charge on the way out, and it costs AED 1.5m capital + about AED 300k a year. Every small pure-play issuer is burning |
| **Infrastructure / protocol** | SafeGold earns 0.03%. OGold (Botim) and SafeGold (e&) already sit inside the UAE's biggest apps. The partner holds pricing power |
| **Spread on small tickets** | Average SIP about USD 34; a UAE direct debit costs AED 5. Banks show "AED 0 fee". ARVA makes buyback spread-free, so we earn on one side only |
| **Paid customer acquisition** | CAC USD 73 against USD 33 of revenue a year, and a third leave each year: −USD 10.48 per customer a year |
| **Custody fees** | Competitors charge 0% |
| **Branded bars** | The premium belongs to scarce brands. Our bar would buy back at melt |
| **Leasing customer gold** | VARA bars encumbering reserves; one default wipes out decades of fees; riba issue |
| **Gold loans as a lender** | Needs a CBUAE licence and USD 10–25m. Referral only |
| **Card interchange** | CBUAE cap 0.75%; cashback eats it; loses money after scheme costs |

**Even if everything worked:** each pool we *can* reach pays single-digit to low-teens dollars per saver a year (card FX 7–13, jewellery and gifts 3–8, loan referral about 4–5, spread about 4 net). That is roughly where our USD 33 already sits (L). **So more revenue lines won't fix it. Lower CAC and lower cost will.**

**Where it is still reachable (with the right setup):**
1. **Both sides of the spread** if we launch as digital gold first (DMCC + CBUAE-licensed partner, like SafeGold–e&), token later.
2. **Distribution we don't pay for:** an exchange house, WPS/payroll provider or remittance app brings CAC near zero.
3. **The end use:** jewellery conversion referral, gift grams, loan referral to a UAE bank, card FX for the trip home.

### 15.5 How to put it to CG: the full chain of reasoning

*Ten steps. Each one leads to the next. For each: what to say, the evidence, and what it means for us.*

**Step 1. The market is real. Demand is not the problem.**
- **Say:** "People save in gold, and some companies make good money from it. The question isn't whether the market works. It's where we sit in it."
- **Evidence:**
  - India digital gold through UPI: about USD 3.4bn a year (L).
  - Jar: 35m users, profitable quarters by its own claim.
  - OGold: from 100k+ users (Aug 2025) to 1.5m (Jul 2026).
  - Muthoot: ₹10,134 cr profit in FY26.
  - Every big UAE bank and super-app launched gold in 2025–26 (ENBD, Emirates Islamic, Botim, e& money).

**Step 2. The money sits at the two ends of the chain, not the middle.**
- **Say:** "Gold is the same everywhere. Nobody pays extra for the bar, the vault or the ledger. People pay for convenience at the front, and for what the gold becomes at the end."
- **Evidence:**
  - Ends: gold loans about 30% ROE, jewellery 3–25%, retail spread 0.5–7%.
  - Middle: SafeGold 0.03%, Augmont 0.34%, token issuance 0.13–0.25%, custody priced at 0%.
- **Why:** gold is a commodity; holding it is priced at zero by banks, XAUT and PAXG; and whoever owns the customer can switch suppliers.

**Step 3. Today Aurumix is set up to pay for the middle seats.**
- **Say:** "We are trying to be the vault, the token issuer and the app at once. We carry the full cost of the seats that earn nothing, and we don't yet own a customer channel."
- **Evidence:**
  - About USD 319k a year of fixed cost (VARA and DMCC about 114k; insurance, audits and tech 205k) plus USD 30k for the card platform, before any staff.
  - We run the vault, treasury (an 8.7-day cycle) and attestations ourselves.
  - B2B is 35% of planned revenue, and no partner is signed.

**Step 4. The token is part of the problem, in three ways.**
- **It earns almost nothing:** XAUT makes about USD 4.3m a year on USD 3.2bn, about 0.13%.
- **It costs a lot:** AED 1.5m of capital plus about AED 300k a year under VARA.
- **It cuts our margin in half:** VARA's rules for a gold-backed token (ARVA) forbid a redemption fee, so we can't earn on the sell side (see 16.4).
- **Our customers don't need it.** They are digital-gold customers: Dh700 tickets, an "LIC subscriber" mindset. Token holders worldwide number only 478k, mostly traders. OGold has 1.5m UAE users and no token.
- **There is a working non-token route:** SafeGold DMCC sells through e& money's CBUAE-licensed wallet with no VARA licence.
- **Say:** "The token can come later, as a feature. It shouldn't be the thing we pay for first." *Needs counsel to confirm the digital-gold-first route.*

**Step 5. "Infrastructure" is the thinnest seat, and in the UAE it's already taken.**
- **Evidence:**
  - SafeGold handles about USD 780m of gold a year and keeps 0.03%.
  - Securitize, the tokenization leader, lost USD 7.9m in Q1 2026.
  - The World Gold Council and BCG are proposing shared industry rails, so a new protocol would compete with the industry body.
  - SafeGold sits in e& money and OGold in Botim.
- **The logic:** infrastructure only earns when volume flows through it. Volume comes from whoever owns the customers. So infrastructure without distribution has nothing to process.
- **Say:** "Infrastructure is what you sell once you have volume. It isn't how you get volume."

**Step 6. Today every customer we buy loses money.**
- **Acquisition:**
  - CAC is USD 73, against USD 33 of revenue a year.
  - A third of customers leave each year, which works out to −USD 10.48 per customer a year.
  - Paid marketing is 49% of costs.
- **Ticket size:**
  - The average SIP is USD 34, and an AED 5 direct debit (about USD 1.36) eats 4% of every payment.
  - It only works from about USD 49 a month.
- **The model:**
  - Y7 margin is 18.8% *before* staff and tax; a basic headcount line wipes it out.
  - 43% of paths pay back by Y7, and none do without B2B partners.
  - The p90 funding need is USD 4.8m.
  - Breakeven needs about 146k paying customers on retail alone, against a plan of 88.6k.
- **Say:** "More ads make the loss bigger, not smaller."

**Step 7. There is a ceiling on what one saver is worth.**
- Every reachable line, added up, is roughly tens of dollars a year (L): card FX 7–13, jewellery and gifts 3–8, loan referral 4–5, spread about 4 net.
- **So CAC has to be a few dollars, not 73.** The only way is to borrow someone else's customers: an exchange house, a payroll (WPS) provider or a remittance app.
- **Each transaction also has to cost almost nothing.** A USD 1 manual touch is 2.5% of a USD 40 SIP. That is Tony's "people touching it" point.

**Step 8. That makes the distribution partner the whole game, and the partner holds the power.**
- The partner will compare us with OGold and SafeGold, which are proven and already live.
- **We have to bring something they don't:**
  - an NRI focus: card FX for the trip home
  - jewellery conversion at Indian jewellers in the UAE
  - gift grams for Diwali and Eid, and family gifting
  - support in Hindi, Urdu and Malayalam
- **We must keep the customer account or a co-brand.** Otherwise we fall to SafeGold's 0.03%.
- **Pricing:** about USD 3–5 per active user a year; 2.5 partners cover fixed costs (§5).

**Step 9. The profitable shape: what we would change.**
1. **Launch as digital gold first,** which earns both sides of the spread and removes the VARA cost for now.
2. **Get one distribution partner,** which brings CAC close to zero.
3. **Earn when the gold is used:** a 3–5% jewellery referral out of the making charge, gift grams, loan referral to a UAE bank, and card FX.
4. **Strip out cost:**
   - a pooled allocated account at a dealer
   - a minimum ticket or quarterly collection
   - UAE PASS KYC
   - AI WhatsApp support
5. **Kill rule:** no signed partner LOI by end of Q1 2027 means stop licensing spend.
6. **Fallbacks:** the cash-first ladder (§13) or selling the book (§5).

**Step 10. The answer to CG's fear: "will this ever be profitable?"**
- **The honest answer:** "As designed today (token first, paid ads, small tickets, no partner), probably not, and our own model says the same."
- **The hopeful part:** "In a different shape, yes, it's plausible. Others prove each piece: SafeGold–e& and OGold–Botim for the structure, Malabar and Muthoot for the end-use money, Jar for the savings habit."
- **The caveat:** "It won't be fast or big early. Jar needed USD 63m and 4 years. We get there by being cheap to run and riding someone else's distribution, then adding the higher-margin end uses."

**Likely pushback from CG, and the answer:**

| CG says | Answer |
|---|---|
| "The token is what makes us different." | Customers buy an outcome (the wedding, the trip home), not a token. OGold has 1.5m users without one. Make the token phase 2, once there is volume worth listing |
| "The VARA licence gives us credibility." | It does, at AED 1.5m + AED 300k a year, plus a fee-free buyback. Credibility also comes from a CBUAE-licensed partner, allocated vaulting and Sharia certification, which is OGold's route |
| "Tether makes billions." | From interest on about USD 135bn of Treasuries. XAUT earns about USD 4.3m, roughly 0.05% of Tether's profit. Gold pays no interest, so there is no float to earn on |
| "Infrastructure scales." | Only with volume that someone else brings. SafeGold handles about USD 780m a year and makes 0.03% |
| "AI or automation will fix margins." | It cuts cost, so do it. It doesn't create revenue: people barely pay for advice, and once it makes decisions it needs a licence |
| "A premium Aurumix bar?" | The brand premium belongs to scarce brands (the Trump name adds about 8%). Our bar buys back at melt. Use gifts for retention, not margin |
| "We just need more marketing." | Each paid customer loses USD 10.48 a year. More ads means a bigger loss |

**What we need CG to decide or tell us (from §6):**
1. Is the token a must-have now, or can it follow a digital-gold launch (subject to counsel)?
2. Which exchange houses, payroll providers or jewellers has he actually spoken to?
3. How much runway is funded?
4. Will he accept the Q1 2027 LOI kill rule?
5. What is the headcount plan, and who does the manual work today?

**Directions to choose between in the meeting:**

| Option | What it means | Upside | Risk |
|---|---|---|---|
| **A. Fix the current product** | Digital gold first, token later; one distribution partner; jewellery/gift/card revenue | Keeps the brand and work done | Needs a signed partner by end of Q1 2027 (kill rule) |
| **B. Cash-first ladder** | Gift-gold desk → old gold desk → bank loan desk; app later | Earns from month one, small capital | Small and unglamorous; a different business |
| **C. Stay token-first / build infrastructure** | As planned today | Matches CG's original vision | Lowest-margin seats; model shows no payback without B2B partners |

---

## 16. Follow-up explainers (30 Oct)

### 16.1 How refiners make money at scale

**What a refiner does, in order:**
1. Takes in impure gold: doré bars from mines (gold mixed with silver and other metals), old jewellery, scrap.
2. Melts it, tests it and purifies it to 99.5% or 99.99%.
3. Casts big bars (1 kg, or 400 oz "Good Delivery" bars for banks), or rolls strips for small bars and coins.
4. Hands the gold back, sells it, or stores it.

**Five ways it earns:**

| # | Income | How it works | Size |
|---|---|---|---|
| 1 | Refining fee ("tolling") | The miner still owns the gold. The refiner charges per ounce to clean it and hands it back | USD 10–25/oz, about 0.25–0.6% (L) |
| 2 | Metal kept back ("metal accountability") | The refiner returns slightly less pure gold than it actually recovers, and keeps the difference | 0.1–2% (L) |
| 3 | Making bars and coins | A charge per piece for stamping, testing and packing | Emirates Minting: AED 12.60 per 1 g bar, about 2.6% (M) |
| 4 | Trading spread | Buys a little below market and sells a little above, to jewellers, banks, dealers and apps | Dubai kilobars trade within ±1% of London (M) |
| 5 | Vaulting, logistics, supplying digital-gold backends | Stores and moves metal | Small, but it adds volume |

**Why only scale works:**
- Each income line is a fraction of a percent. The gold itself passes straight through.
- The plant, assay lab, LBMA accreditation, insurance and compliance cost about the same at 1 tonne or 100 tonnes. More volume means more fees on the same fixed cost.

**Example: 1 kg of gold (about USD 130k)** (illustrative, L)

| What the refiner does with it | It earns | % of gold value |
|---|---|---|
| Refines it for a miner | USD 320–800 (32 oz × USD 10–25) | 0.25–0.6% |
| Also keeps back 0.1% of the metal | About USD 130 | 0.1% |
| Or turns it into 1,000 × 1 g bars | About USD 3,400 (1,000 × AED 12.60) | About 2.6% |

- Small bars earn the most per kg, but demand for 1 g bars is limited. Most volume is big bars at fractions of a percent.

**Real numbers:**
- **Augmont FY25:** ₹66,231 cr of sales (about USD 7.5bn) and ₹227 cr profit (about USD 26m), or 0.34%.
- **MMTC-PAMP FY24:** ₹37,837 cr of sales and ₹477 cr profit, about 1.3% (L).
- **MKS PAMP:** 1,500+ staff across refining, PAMP bars, trading and vaulting.
- **Note:** gold companies book the full gold value as "revenue", so the percentages look tiny. The absolute profit is real because the volume is huge.

**For Aurumix:** refining is a capital and scale game. We are a refiner's customer, not a competitor.

### 16.2 Refiner vs mint vs digital-gold backend vs token issuer

**"Minting" has two meanings:**
- **Physical minting:** stamping gold into coins or small bars, each with a design, weight and serial number. A "mint" is the factory that does it. Refiners often own one (PAMP, Valcambi, Emirates Gold).
- **Token minting:** creating new tokens on a blockchain when gold is added to the reserve. "Burning" is the reverse. Nothing is stamped; it's a ledger entry.
- When Aurumix talks about "minting AURX", it means the second.

| | Refiner / mint | Digital-gold backend | Token issuer |
|---|---|---|---|
| **Makes** | Physical gold: purifies, casts, stamps | A record of who owns how many grams | One token per gram or ounce |
| **Has a factory** | Yes | No | No |
| **Buys gold from** | Mines, scrap, banks | Refiners and dealers | Refiners and dealers |
| **Sells to** | Banks, dealers, jewellers, backends | Customers, through partner apps | Institutions, who then sell on exchanges |
| **Keeps customer records** | No | Yes, a milligram ledger | Yes, on the blockchain |
| **Earns from** | Refining fees, metal kept back, making charges, trading | A cut of the buy/sell spread, delivery, storage | Mint and redeem fees |
| **Margin** | 0.3–1.3% net | 0.03% (SafeGold) | About 0.13–0.25% |
| **Examples** | PAMP, MMTC-PAMP, Augmont, Emirates Minting | SafeGold, OGold, Augmont | Tether, Paxos, Kinesis |

- **A backend is a dealer + a vault account + software.** It never melts anything.
- **Some groups sit in several seats:** Augmont is a refiner, a backend and an app; MKS PAMP is a refiner and a token issuer (DGLD); MMTC-PAMP is a refiner and a backend.
- **Aurumix as planned is a backend, a token issuer and an app at once.**

### 16.3 Who earns in tokenized gold

**How a gold token moves:**
1. A large institution buys tokens direct from the issuer (USD 200k minimum at Tether) and pays 0.25%.
2. It sells them on exchanges such as Binance.
3. Traders buy and sell among themselves on the exchange, many times over. The issuer earns nothing on these trades.
4. Eventually someone redeems and pays 0.25%.
- **The issuer gets paid at the door, twice. The exchange gets paid on every trade in between.**

| Who | How they earn | Size |
|---|---|---|
| Exchanges, spot | A fee on every XAUT/PAXG buy and sell | USD 90.7bn traded in Q1 2026 alone. At an assumed 0.05–0.1% fee, USD 45–90m in one quarter (L, our arithmetic) |
| Exchanges, perpetuals | A fee each time a gold perp position opens or closes | USD 4.4bn traded in a one-day snapshot. At an assumed 0.02–0.05%, USD 0.9–2.2m a day (L) |
| Arbitrage desks and market makers | Buy from the issuer and sell on exchanges when prices drift apart; quote both sides | Not measured |
| Lenders | Lend stablecoins against XAUT/PAXG (Antalpha, Ledn; Aave, Morpho) | Small: USD 63m on Aave and Morpho |
| The issuer | 0.25% in, 0.25% out | XAUT about USD 4.3m a year, about USD 1.1m a quarter |

- **The rough comparison:** exchanges probably earn 40–80× in one quarter on spot what XAUT earns in fees (L).

**What a gold perpetual ("perp") is:**
- A contract that tracks the gold price. It has no expiry date and no gold behind it.
- Traders bet up or down, often with borrowed money.
- The exchange earns a fee on every open and close. It needs no vault, no audit and no custody.
- Traders who want price moves rather than metal are moving here, which takes trading away from the tokens.
- Binance launched its gold perp on 5 Jan 2026 and had 34.5% of gold perp volume in the snapshot.

**Tether itself** earns from interest on about USD 135bn of Treasuries and from gains on its own ~148 t of gold. XAUT fees are about 0.05% of its profit (L).

**Pleasing Gold (PGOLD): Pleasing International, a Hong Kong dealer**
- **The token:**
  - USD 79m on paper. 0% to mint and 0% to hold.
  - The only fee is 0.5% on physical redemption (1 kg minimum, collected in Hong Kong), and it goes to people who stake PGOLD, not to Pleasing.
- **Activity:**
  - 9 active addresses and USD 167 of transfers in a month.
  - USD 0 of exchange volume.
  - No third-party gold audit found.
- **So:** the token earns Pleasing about zero. Most likely it is the dealer's own stock wrapped as a token.
- **Where the parent tries to earn:**
  1. Its physical metals dealing (no figures published).
  2. USDpm, a token that takes in crypto dollars and lends them to metals dealers, vaults and refiners to finance their stock, targeting 6–10% a year. In effect, cheap financing for the trade.
  3. Selling "tokenization as a service" to others: setup fees and revenue share. No clients disclosed.
- **Verdict:** the token is a shop window; the group's profit is unknown.

**Matrixdock (XAUm): part of Matrixport, now rebranded BIT**
- **The parent** is a crypto financial firm with USD 6bn+ under custody and management and USD 7bn+ of monthly trading. It earns from trading, structured products, lending, custody and funds.
- **The token:**
  - USD 70m.
  - The mint fee is waived until the token reaches USD 100m, there is no storage fee, and redemption costs 0.25%.
  - The quoted buy/sell prices are about 0.76% apart. USD 10k minimum.
- **The economics:**
  - About USD 0.07–0.13m of revenue a year, against about USD 1–2.5m of cost: vaults, Bureau Veritas audits, trustee, 6+ chains and staff (L).
  - Trading on KuCoin (about USD 451k a day) earns Matrixdock nothing, because transfers are free.
- **Reserves are clean:** audits match tokens to bars almost to the ounce. 65k holders, probably from campaigns.
- **Why they keep it:** it's a collateral product and a customer magnet for the group's trading and lending, which is where the group earns.

**Lesson:** every surviving token is a loss-leader inside a business that earns elsewhere. Aurumix has no "elsewhere" yet.

### 16.4 What "spread" means

**The buy/sell spread:** a gold seller quotes two prices around the market price.
- A **buy price** (what you pay), a bit above market.
- A **sell-back price** (what you get back), a bit below market.
- The **gap between them is the spread.** It's the seller's margin, built into the price instead of shown as a fee.

**UAE example, market at AED 478.8/g (spot USD 4,055, 28 Oct):**

| | AED per gram |
|---|---|
| Market price | 478.8 |
| App's buy price (+1%) | 483.6 |
| App's sell-back price (−1%) | 474.0 |
| **Spread** | **9.6, about 2%** |

- Buy AED 1,000 of gold and sell it back the same day: you get about AED 980.
- That's how UAE banks can advertise "AED 0 fee": the money is in the spread.
- In India the spread is wider: 2–7%, plus 3% GST (§9).

**Fee vs spread:**
- A **fee** is a visible line, like Aurumix's "5% SIP entry fee". Customers notice it and compare it.
- A **spread** is inside the price. That's why §5 recommends pricing through the spread.

**Why it matters for Aurumix:** under VARA's ARVA rules, buyback must be at market with no fee. Aurumix can earn only on the buy side, which is half the spread. A digital-gold seller earns on both sides.

**Other places these notes use "spread":**
- **Lending spread:** interest earned minus interest paid. Muthoot earns about 20% and pays about 7.4%.
- **Leasing spread:** the fee a jeweller pays minus what the gold owner receives.
- **Wholesale spread:** a dealer's price on kilobars, within ±1% of London.

### 16.5 The commercial chain of gold, mine to customer

*Rows marked (G) use general industry knowledge, not this session's research.*

**The flow:**

```
Mine ──doré──> Secure transport ──> Refiner ──bars──> Bullion banks / dealers <──> Vaults
                                                        │
                    ┌───────────────────────────────────┼───────────────────────────────┐
                    ▼                                   ▼                               ▼
          Mints & jewellery makers            ETFs, digital-gold backends,        Central banks,
                    │                         token issuers                       big investors
                    ▼                                   ▼
          Jewellers, bullion shops            Apps, banks, exchanges
                    └──────────────> Customer <─────────┘
                                        │
                     Old-gold buyers, pawn/gold lenders ──> back to the refiner (recycling)
```

| # | Stage | What happens | Main players | How they earn | Margin |
|---|---|---|---|---|---|
| 1 | **Mining** | Dig ore and process it into doré bars (roughly 60–90% gold) | Newmont, Barrick, Agnico Eagle; small and artisanal miners; royalty and streaming financiers such as Franco-Nevada and Wheaton (G) | Sell the gold at market price; keep the gap over their cost | Wide while gold is high. Large miners' all-in cost is roughly USD 1,500–2,000/oz against USD 4,055 (G, L) |
| 2 | **Secure transport** | Move doré and bars | Brink's, Loomis, Malca-Amit, Transguard (UAE) | Per-shipment fees plus insurance | Service fee |
| 3 | **Refining** | Purify to 99.5–99.99% and cast bars | Valcambi, PAMP, Argor-Heraeus, Metalor (Switzerland, G); MMTC-PAMP, Augmont (India); Emirates Gold (UAE) | Refining fee plus metal kept back (§16.1) | 0.25–0.6% fee + 0.1–2% metal (L) |
| 4 | **Wholesale trading** | Big bars change hands between banks and dealers. The world price is set here | Bullion banks (JPMorgan, HSBC, UBS, G); the London market (LBMA price, twice a day); COMEX futures in New York; Shanghai Gold Exchange (G); DMCC dealers in Dubai | Trading spread, financing, leasing | Under 1%. Dubai kilobars trade within ±1% of London |
| 5 | **Vaulting** | Store bars, insured and audited | Brink's, Loomis, Malca-Amit, bank vaults | Storage fee | 0–0.25% a year |
| 6 | **Fabrication** | Turn bars into jewellery, coins and small bars | Jewellery manufacturers; mints (US Mint, Royal Mint, Emirates Minting) | Making charge per piece | About 2.6% on a 1 g bar at the mint |
| 7a | **Retail, physical** | Sell metal to the public | Jewellers (Malabar, Joyalukkas, Kalyan, Tanishq), bullion shops, souk dealers, banks | Making charges; markup on small bars | Jewellery making 3–25%; small bars 5–60% over gold value |
| 7b | **Retail, paper and digital** | Sell ownership without handing over metal | ETFs (GLD); digital-gold apps and their backends (Jar and PhonePe on SafeGold, Augmont and MMTC-PAMP; Botim on OGold); tokens (XAUT, PAXG); bank gold accounts | Spread, yearly fees, mint and redeem fees | Spread 0.5–7%; GLD 0.40% a year; tokens about 0.2% |
| 8 | **After-market** | Gold comes back: sold, pawned or melted | Old-gold buyers, gold lenders (Muthoot, UAE banks), refiners re-refining scrap | Buy-back spread; loan interest | Buy-back 1–3% below market; Muthoot about 30% ROE |

**Three things to notice:**
1. **The price is set in the middle (London, New York, Shanghai).** Everything else is quoted as "market plus or minus". India also adds about 6% duty on bars and 3% GST.
2. **The money sits at the edges, plus mining when prices are high.** Miners keep the gold-price upside. Jewellers, apps and lenders earn from the customer. Refining, trading and vaulting earn fractions of a percent on huge volume.
3. **Dubai is a hub.** Doré and scrap come in, DMCC refiners and dealers process and trade them, and much of it goes on to India as bars and jewellery (G).

**Where Aurumix sits:** it buys bars from a DMCC dealer or refiner (stage 4), stores them with a vault (stage 5) and sells to savers through an app (stage 7b). The higher-margin moves are reaching into stage 7a (jewellery conversion) and stage 8 (loan referral) through partners.

### 16.6 Is gold more expensive in India than in the UAE?

**Yes, but say it as a range with a reason, not as one number.**

**Prices on 29 Oct 2026 (24K, per gram; Angel One, M):**

| | AED/g | vs world price |
|---|---|---|
| World price (spot, USD 4,055/oz) | 478.8 | n/a |
| Dubai shop board rate | 488 | +1.9% |
| India rate (₹14,415, before 3% GST, at AED 1 = ₹25.89) | 556.8 | +16% |

- India was about 14% above Dubai; put the other way, Dubai was about 12–13% cheaper. Round-1 sources said 8–12%. **Safe line: "about 8–14% cheaper in Dubai, depending on the day."**

**Why India costs more:**
1. **Import duty on gold.** Our files use about 6%, but the skeptic marked that unsourced, and one cited headline says India has *hiked* import duty. Check the current rate.
2. **3% GST** on every purchase.
3. **A local premium** that moves with demand, the rupee and wedding season.
- In the UAE, investment gold (99%+) carries 0% VAT, and Dubai is a low-cost trading hub.

**Four caveats so it isn't misquoted:**
1. **It is a tax and premium gap, not different gold.** The world price is the same.
2. **For jewellery the gap is smaller,** because the UAE adds 5% VAT on jewellery. Example: 40 g of 22K with the same 10% making charge costs about AED 20,870 in Dubai (with VAT) against about AED 23,130 in India (with GST), so about 10% cheaper (L, illustrative). Dubai making charges are also often lower (3–12% against 7–25%).
3. **Taking it home:** jewellery goes in duty-free up to 20 g (men) or 40 g (women), by weight. Bars and coins pay duty from the first gram, which wipes out most of the saving.
4. **Check the size before quoting it.** The 29 Oct India rate is about 16% above the world price, yet duty and GST explain only about 6–9%. Either India was at an unusually high local premium, the duty has gone up, or the source's rate and FX don't match. If India were priced at world price plus duty only, the jewellery saving after UAE VAT would shrink to about 1–2%.

**For Aurumix:**
- The gap is the NRI hook: buy wedding jewellery in Dubai and carry it home within the allowance. That supports jewellery conversion (§5 step 3).
- It cuts the other way for "send gold to India" gifts, because the sender sees India's higher price.

**Line for the meeting:** "Gold is usually cheaper in Dubai than in India, recently by around 8–14% on the gold rate, mainly because of India's import duty and GST. For jewellery the saving is smaller after UAE VAT, and only jewellery within the duty-free allowance goes home without duty."

### 16.7 Every digital-gold platform we discussed, by type

*Tokens (XAUT, PAXG, Kinesis and others) are not here; see §12 and §16.3.*

**The six types at a glance:**

| Type | What it is | How it earns | Who |
|---|---|---|---|
| 1. Backend (B2B) | The legal seller behind other apps: buys bars, vaults them, keeps the gram ledger | A small cut of the spread | SafeGold, Augmont, MMTC-PAMP, OGold |
| 2. Savings app | Its own app and brand, built around a saving habit | Most of the spread, plus jewellery | Jar, OGold's own app |
| 3. Payment / super-app | A gold screen inside an app people already use | A commission from the backend | PhonePe, GPay, Paytm, Botim, e& money |
| 4. Bank gold account | Gold as a free feature of a bank account | A hidden spread | ENBD, Liv, Mashreq, ADCB, FAB, Emirates Islamic |
| 5. Western vault platform | Stores gold for wealthier savers | Storage fee + trading fee | Goldmoney, BullionVault, Glint, Vaulted, Revolut, Goldwise |
| 6. Jeweller savings scheme | Monthly saving that must end in jewellery | Making charges + lock-in | Tanishq, Malabar, Kalyan, Joyalukkas |

**Type 1: Backends (the "infrastructure" seat)**

| Platform | Where | How it operates | How it makes money | Numbers |
|---|---|---|---|---|
| **SafeGold** | India; UAE since Apr 2026 | Buys big bars, vaults at Brink's under a trustee, keeps a milligram ledger, plugs into 50+ partner apps by API, handles buyback, coins and jewellery conversion (Tanishq, CaratLane, Kalyan). In the UAE it is SafeGold DMCC behind e& money | About 0.85% of flow (₹8–9 of ₹1,000 bought on PhonePe; the partner keeps the rest). UAE: service fee, storage after 2 years, minting and delivery fees | ₹6,867 cr sold, **0.03% EBITDA**, net loss ₹12.2 cr (FY25). 50m have bought, only 9m still hold. Raised just USD 2.4m |
| **Augmont** | India | Refiner and bullion trader first. Also a backend for 180+ partners and its own "Gold For All" app | Mostly B2B bullion volume (93–96% of revenue). Digital gold adds demand for its bars | ₹66,231 cr revenue, ₹227 cr profit, **0.34%** (FY25). IPO filed |
| **MMTC-PAMP** | India | LBMA refiner. Backend for Paytm and GPay, plus its own app | Bullion sales; 3–4% spread on its own app | About ₹477 cr profit on ₹37,837 cr, **about 1.3%** (FY24, L) |
| **OGold** | UAE (DMCC) | **Hybrid:** its own app (AED 1 minimum) *and* the backend inside Botim. Partners with Aspora (Indian diaspora remittance). Gold Mastercard, gift-card and jewellery marketplace, Sharia certified | Spread on buys and sells, the card, the marketplace. Advertises about 3% yield in grams (its terms disclaim any guarantee; funding unverified) | **1.5m users** (Jul 2026), up from 100k+ in Aug 2025. No P&L published |

**Type 2: Savings apps that own the customer**

| Platform | Where | How it operates | How it makes money | Numbers |
|---|---|---|---|---|
| **Jar** | India | Daily ₹10 auto-save by UPI. Backend is SafeGold/Augmont; gold vaulted at Brink's. Users sell back, take coins, or convert to Nek jewellery. Became the legal seller in FY25 | Most of the spread; Nek jewellery is about 5–15% of what it keeps | 35m users, 95% first-time savers. ₹208 cr operating revenue, net loss ₹50.5 cr (FY25); profitable Q4 FY25 and Q1 FY26 (company claim). Took USD 63m and 4 years |
| **OGold app** | UAE | See Type 1 | See Type 1 | The closest direct competitor to Aurumix: same city, same diaspora, already live |

**Type 3: Payment and super-apps with a gold screen**

| Platform | Where | Backend | How it makes money | Numbers |
|---|---|---|---|---|
| **PhonePe** | India | SafeGold | Commission on each buy, sell, SIP and redemption, plus volume incentives | Spread about 4–6%. 35% of digital-gold purchases (2020). Gold P&L not disclosed |
| **GPay, Paytm** | India | MMTC-PAMP | Same | Spread about 5%; buyback 1.5–3% below the IBJA rate |
| **Botim** | UAE | OGold (Aug 2025) | Partner share (terms not public) | 8.5m UAE users, from 0.1 g |
| **e& money** | UAE (CBUAE-licensed wallet) | SafeGold DMCC (Apr 2026) | Partner share (terms not public) | From AED 10, home delivery. Leasing yield and jeweller redemption planned |

- **India overall:** UPI digital gold runs at about ₹2,450 cr a month, average ticket ₹98. Customers start 5–7% under water (spread + 3% GST).

**Type 4: UAE bank gold accounts**

| Bank | How it operates | How it makes money |
|---|---|---|
| **Emirates NBD** | Electronic gold balance; no physical delivery | "AED 0 fee", no storage fee; earns the spread on live rates |
| **Liv** (ENBD's digital bank) | From 0.001 oz | Spread in the rate; delivery and making charges if you take metal |
| **Mashreq Gold & Silver Edge** | **Unallocated** (you are a creditor, not an owner); price reset twice a day | Spread |
| **ADCB, FAB** | Gold accounts | Spread, typically 0.5–2% |
| **Emirates Islamic** | First Sharia-compliant in-app gold and silver (Apr 2026) | Not disclosed |

- **Why it matters:** banks give gold away as a feature to hold deposits. "AED 0 fee" is the price every UAE app is compared with.

**Type 5: Western vault platforms (wealthier savers, fee on balances)**

| Platform | How it makes money | Numbers |
|---|---|---|
| **Goldmoney** (Canada, listed) | 0.5% to buy or sell; storage 0.25–0.5% a year, charged in metal; no lending | About C$4.5bn client assets, about C$50m metals income (about 1.1%), boosted by the gold rally |
| **BullionVault** (UK) | 0.5% commission, falling to 0.05% on large trades; storage 0.12% a year | 130k users holding about USD 80k each. Private |
| **Glint** (UK) | 0.5% to exchange, 0.5% FX, card interchange, small storage fee | Gold debit card. Revenue under £1m (2023, L) after raising USD 26.8m: spending gold hasn't caught on |
| **Vaulted** (US) | 1.8% per trade; 0.40% a year storage | Private |
| **Revolut** | 0.49–0.99% order fee + 0.25–1% markup | A feature that nudges users to paid plans |
| **Goldwise** (UK, 2026) | 0.5% per trade, 0.15% a year storage, B2B setup fees | Startup |

- **Lesson:** a storage fee works only on big balances. At USD 80k it pays about USD 100–400 per user a year; at Aurumix's balances it pays cents to a few dollars.

**Type 6: Jeweller savings schemes (the most profitable gold savings product)**

| Scheme | How it operates | How it makes money |
|---|---|---|
| **Tanishq Golden Harvest** (India) | 10 monthly payments; bonus of about 7.5%; must redeem in jewellery within 400 days | Making charges on the jewellery, a year of interest-free cash, customer lock-in. About 20–25% of Titan's jewellery sales |
| **Malabar, Kalyan, Joyalukkas** | Similar plans. Malabar's UAE "gold purchase plan" terms sit behind a form; Gulf jewellers lean on advance bookings | Making charges (3–12% in Dubai, 7–25% in India) |

- India's deposit rules keep these schemes under 365 days; in the UAE such a plan may count as deposit-taking, so get counsel first.

**What the six types tell us:**
1. **Profitable:** jewellers (Titan EBIT 11.2%), refiner-backends (Augmont, MMTC-PAMP, on volume), and Goldmoney (big balances + rally).
2. **Just about:** Jar (after USD 63m and 4 years), SafeGold (0.03%).
3. **Unknown:** OGold, PhonePe and the super-apps' gold lines.
4. **Features, not businesses:** UAE banks, Revolut.
5. **Aurumix's real competitors are OGold, SafeGold-in-e& and the bank accounts.** Aurumix today is trying to be Type 1 + Type 2 at once (plus a token) without the volume of either.

### 16.8 Where the money is made, and the practical trade-offs

**Part 1. Where the money is made, by activity**

| Tier | Activity | Margin | What you must own to earn it |
|---|---|---|---|
| **High** | Gold lending | About 30% ROE (Muthoot); interest margin about 12.6% | A lending licence, cheap funding, appraisers, trust |
| **High** | Jewellery | Making charges 3–25%; Titan jewellery EBIT 11.2% | Stores, stock, craftsmen, decades of trust |
| **High** | Jeweller savings schemes | About 7.5% bonus, earned back through making charges + a year of free cash | Your own jewellery counter |
| **High %, small $** | Small bars and gifts | 5–60% over gold value | Shelf space, or corporate buyers and an occasion |
| **High %, unreachable** | Branded / collector coins | About 23% over melt | A scarce sovereign brand |
| **Wide while gold is high** | Mining (G) | Big gap between cost and price | Mines, capital, decades |
| **Medium** | Retail spread (owning the customer) | India 2–7%, UAE 0.5–2% | The customer's habit at near-zero CAC |
| **Medium** | Card FX on trips home | USD 7–13 per cardholder a year | A card programme |
| **Medium-low** | Old-gold buying | About 2% per ticket | Appraisers, a refiner contract, footfall |
| **Thin** | Refining, bullion trading, vaulting, B2B infrastructure, token issuance, leasing | 0.03–1% | Only works at huge volume |

**Part 2. The high-margin businesses: trade-offs**

| Business | Margin | What it takes | Time to profit | Main risk | Aurumix route |
|---|---|---|---|---|---|
| **Own gold-loan book** | About 30% ROE | CBUAE licence, USD 10–25m equity, branches, appraisers | Years (Indiagold about 5) | Fake gold, gold-price falls, rate wars (Manappuram's yield fell from 20.7% to 17.3%), riba. Rupeek lost ₹281 cr in a year | **Partner:** a loan desk or referral with a UAE bank, only on a term sheet paying us ≥6% a year for servicing |
| **Own jewellery brand** | Gross 3–25%; net about 7–11% | Stores, gold stock, designers, trust | Long | Stock price risk; competing with Malabar's 67 UAE outlets | **Referral:** 3–5% of the jeweller's making charge |
| **Jeweller-style savings plan** | About 7.5% bonus recovered via making + float + lock-in | A jewellery counter at the end | Medium | May count as deposit-taking in the UAE (fines from AED 1m) | **Redeem-to-jewellery** with partner jewellers, structured as an outright purchase, not a deposit |
| **Retail savings app** | Spread 0.5–7% | Near-zero CAC and scale | Jar: 4 years, USD 63m | CAC; banks' "AED 0 fee"; trust shocks (India's SEBI warning tripled withdrawals) | **Through a distribution partner** (exchange house, payroll, remittance app) |
| **Corporate gift desk** | About AED 6,000 per 300-bar order | A mint supplier and corporate contacts | Months; break-even about 40 orders a year | Seasonal, no moat, small | **Do it directly.** USD 0.1–0.3m, paid upfront, no stock |
| **Card FX** | USD 7–13 per cardholder | A card programme partner | Medium | UPI from NRE accounts eats it; cashback races | **Through a card partner**, positioned for the trip home |
| **Branded coins** | About 23% over melt | A scarce brand | n/a | Premium vanishes at resale | No |
| **Leasing** | About 1% net | Creditworthy jewellers, insurance | n/a | One default wipes out about 100 years of fees | No |

**Part 3. What this means practically**

1. **High margin is rent on something scarce.** Lenders own a licence and a balance sheet. Jewellers own stores, stock and trust. Mints own a scarce brand. Apps own a habit. Without the scarce thing, you don't get the margin; you get a referral fee.
2. **A margin percentage is not dollars.** A 1 g bar at a 20% markup earns about AED 94. A gold-loan book at 30% ROE needs USD 10m+ of equity before the profit matters. Judge each idea by dollars per order or per customer, and by capital needed.
3. **Margin follows the risk you carry.** Jewellers carry stock, lenders carry credit risk, apps carry acquisition cost. Referral models carry none of these, so they earn less, but they need almost no capital.
4. **For a USD 1–3m Dubai startup, the realistic order is:**
   - **Now:** what pays upfront or holds no stock: the corporate gift desk, jewellery referral, card FX via a partner.
   - **Next:** what builds appraisal skill and trust: the old-gold desk.
   - **Then:** the big pool through a bank: a gold-loan desk or servicing.
   - **Throughout:** the savings app is the funnel, sold through a partner, not the profit centre.
   - **Avoid:** token, infrastructure, custody fees, leasing, own-brand bars and own-brand jewellery.
5. **The trade-off to put to CG:** "Big, slow and capital-heavy (own lending, own jewellery), or small, fast and capital-light (referrals, gifting, partner distribution) that can grow into the big pool through a bank?" On 2 Oct CG asked for a narrower, lower-risk model, so the capital-light route matches what he asked for.

**Simple grid:**

| | Easy to start | Hard to start |
|---|---|---|
| **Good margin** | Corporate gifting (small dollars); jewellery referral (a share of someone else's margin); card FX via partner | Own gold-loan book; own jewellery brand; branded coins |
| **Thin margin** | Old-gold desk; retail spread through a partner | Token; infrastructure; refining; vaulting |

### 16.9 The practical order, explained (the "ladder")

*Expands §13 and §16.8 point 4. All numbers come from `research/round2_check_skeptic.md`, `round2_judge_*.md`, `round2_ideate_*.md` and §5. Most are estimates (L) until we have real quotes.*

**The idea in one line:** start with businesses that pay us before we spend anything, use them to build the relationships, skills and trust a bank wants, then move into the big profit pool (gold loans) using the bank's money, not ours.

**Why this order:**
1. **Cash first.** A startup with USD 1–3m can't wait two years for revenue. The first steps earn on every order from month one.
2. **Each step builds what the next needs.** Gift orders open doors to exchange houses and employers. Buying old gold builds appraisers, testing kit and family trust. Those are exactly what a bank wants to see before letting us run gold-loan desks.
3. **Losses are capped.** Every step has a cheap test and a kill rule before real money goes in.
4. **It matches what CG asked for on 2 Oct:** narrower and lower risk.

#### Step 1 (months 0–6): businesses that pay upfront or hold no stock

**1a. Corporate gift desk**
- **In plain terms:** companies buy small gold bars as gifts for staff or customers (Eid, Diwali, long-service awards, exchange-house prize draws). We take the order, buy from the mint, and deliver bars in a logo card.
- **How one order works (300 × 1 g bars):**
  1. The company pays us 100% upfront: AED 540 a bar, AED 162,000.
  2. The same day we buy from the mint: about AED 508 a bar including card and delivery. We never hold stock, so a price move can't hurt us.
  3. We keep AED 32 a bar = AED 9,600. After sales time and handling, **about AED 6,000 (USD 1,630) per order**.
- **Why companies would buy from us:** the mint sells plain bars online at AED 498; jewellers charge AED 570. We sit in between, with design, logo, delivery on a fixed date and a printed buyback promise (spot minus 1%).
- **What it needs:** a Dubai trade licence for gold, dealer (DPMS) registration with goAML anti-money-laundering reporting, VAT registration. **No CBUAE, VARA or CMA licence**, because it's a plain sale of goods. Capital USD 0.1–0.3m.
- **Break-even:** about 40 orders a year (fixed cost about AED 250k: founders selling plus one operations hire).
- **Test before scaling:** 5 signed purchase orders for Eid al-Fitr (about 9–10 Mar 2027) paying at least AED 35 a bar over mint cost. Diwali on 8 Nov is too close; first revenue is realistically Jan 2027 (year-end awards) or Mar 2027 (Eid).
- **Honest limits:** no moat (anyone can buy from the mint), seasonal, small. Its real value is cash plus a working relationship with every exchange house and HR team we sell to.

**1b. Jewellery referral**
- **In plain terms:** when a saver wants to turn their gold into wedding jewellery, we send them to a partner Indian jeweller in the UAE (Malabar has 67 outlets). The jeweller pays us a fee out of its making charge.
- **Example:** a saver converts 20 g into a 22K necklace, roughly AED 10,000 with making charges. At a 1–5% referral we earn about AED 100–500.
- **Why the jeweller would pay:** we bring a ready buyer with the gold already saved, and the jeweller still earns the making charge.
- **Honest point:** on a plain piece with an 8% making charge, a 3–5% referral is half the jeweller's margin. Expect the low end (1–2%) until we bring volume. Heavy bridal pieces (15–25% making) can afford more. No jeweller has agreed a rate yet.
- **Worth per saver:** about USD 3–8 a year with gifting (§5), because people only convert every few years.
- **Needs:** no capital; one signed jeweller.

**1c. Card FX on trips home, through a card partner**
- **In plain terms:** NRIs spend in India on UAE cards, and banks add a 3.14% FX fee. A card priced at 1.5–2% is cheaper for them and still leaves a margin.
- **Example:** AED 1,000 spent in India. A bank keeps about AED 21 after about AED 10 goes to Visa/Mastercard. A cheaper card keeps about AED 5–10.
- **Worth per cardholder:** about USD 7–13 a year, net of scheme costs.
- **Needs:** a licensed card-issuing partner; about USD 30k a year of card-platform cost. Setting it up takes months, so it starts in Step 1 but pays later.
- **Risks:** NRIs can now pay by UPI from NRE accounts, which skips the card. Don't join the cashback race.

#### Step 2 (months 3–9): an old-gold buying desk

- **In plain terms:** a kiosk inside an exchange-house branch buys families' old 22K jewellery. The purity test happens in front of them, the price is on screen, and they're paid by bank transfer in 15 minutes (or the money goes straight home through the exchange house).
- **How one ticket works (25 g of 22K = 22.9 g of pure gold, worth AED 10,965):**
  1. We pay the customer 97.5%: AED 10,691.
  2. At the same moment we lock a sale to a refiner at about 99.4%: AED 10,899.
  3. Gap AED 208 (1.9%). After testing, transfer, insurance and a community referral fee, **about AED 136 (USD 37) per ticket**.
- **Why the exchange house hosts us:** it earns its FX margin when customers send the money home.
- **What it needs:** the same licence and dealer registration as Step 1, an XRF purity analyser, two appraisers, a refiner contract and a payout float of AED 1–1.5m. Capital USD 0.35–0.6m.
- **Break-even:** 7–9 tickets a day.
- **The catch:** souk buyers may already pay about 98%. If we must match them, we earn only AED 30–80 a ticket and need 15–40 tickets a day. Volume also drops when gold prices fall, as now.
- **Test before signing a lease:** mystery-shop 10 souk buyers and run a 2-week pilot. Go only if we trend to 9+ tickets a day, the refiner pays at least 99%, and souk buyers pay under 98.5%.
- **The one hard rule:** never pay cash against gold with a right to buy it back. That is a loan, and doing it without a licence carries fines from AED 1m.
- **Why it matters beyond its own profit:** it builds the appraisers, testing, refiner relationship and family trust a bank needs before backing Step 3.

#### Step 3 (months 9–18): a gold-loan desk, funded by a bank

- **In plain terms:** the Muthoot model, but the bank lends and we run the counter. A family pledges jewellery and gets cash in 30 minutes; we test and value the gold, run the software and service the loan; the bank's money funds it.
- **Why customers want it:** selling jewellery loses about 14% at once (making charge and VAT are never returned). Borrowing keeps the family gold.
- **How one loan works:**
  1. A customer pledges 25 g of 22K (worth AED 10,965) and borrows AED 7,000 (65%) for 4 months.
  2. They pay the bank 16% a year plus a 1% fee: AED 443 in total.
  3. The bank pays us the AED 70 fee plus a servicing fee of 6% a year on the loan: **about AED 210 per loan**, or about AED 145 after our costs.
  4. The bank still makes about a 33% pre-tax return on its capital, so the split can work for it.
- **Break-even:** about 8 loans a day per desk (a book of about AED 5m). The whole company needs a book of AED 41–49m (USD 11–13m) across about 5 desks.
- **What it needs:** a CBUAE-licensed bank partner; USD 1.2–1.8m (legal, pilot desks, head office, possibly a 3–5% first-loss deposit for the bank). **No loan book on our balance sheet.**
- **The big risk:** everything depends on what the bank agrees to pay us. There is no UAE precedent for a 9% share, and Rupeek in India lost ₹281 cr in a year on this model. If the bank pays only 4%, break-even jumps to a book of AED 13–26m per desk.
- **Legal point:** UAE law (CBUAE Article 62) licenses anyone who *facilitates* lending. Staffed loan desks probably need CBUAE approval through the bank, so get counsel's view first.
- **Rule:** spend at most USD 50k on counsel and talks with 3 banks while Step 2 runs. **Move only on a signed term sheet paying us at least 6% a year.** No term sheet within 6 months → stay a trading business.

#### Throughout: the savings app is the funnel, not the profit centre

- **What the app does:** it keeps customers saving small amounts, and it feeds the businesses that pay: jewellery conversions, gift orders and, later, loan referrals.
- **Why it can't be the profit centre:** each saver is worth tens of dollars a year at most (§16.8), so it only works if acquisition is nearly free.
- **How it's sold:** inside a partner's channel (exchange house, payroll provider, remittance app), at about USD 3–5 per active user a year from the partner. No paid ads.
- **How it's structured:**
  - Digital gold first: a DMCC entity plus a CBUAE-licensed partner, as SafeGold does with e& money. Token later.
  - Each top-up is an outright gold purchase, never a deposit. Jar is under a police case in Karnataka (Jan 2026) for exactly this.
- **Note:** if we were starting from zero, the app would come last (§13). Aurumix has already designed it, so it can run alongside, but only through a partner.

#### Avoid, and why (in one line each)

| Avoid | Why |
|---|---|
| The token | Earns about 0.13%, costs AED 1.5m + AED 300k a year, and blocks our sell-side spread |
| Infrastructure / protocol | SafeGold makes 0.03%; OGold and SafeGold already sit in the big UAE apps |
| Custody fees | Competitors charge 0%; on small balances it's cents |
| Leasing customer gold | Earns about 1%; one default wipes out about 100 years of fees; VARA and riba problems |
| Own-brand bars | Brand premiums belong to famous mints; ours would buy back at melt |
| Own-brand jewellery or wedding plan | Needs stock and decades of trust against Malabar; the plan may count as deposit-taking |
| Own lending company | Needs USD 10–25m and its own CBUAE licence; a phase-3+ idea at best |

#### How the steps connect

| Shared piece | Used by |
|---|---|
| One trade licence + dealer (DPMS/goAML) registration + one compliance officer | Gift desk, old-gold desk |
| One mint / refiner / DMCC dealer relationship | Gift desk (buying), old-gold desk (selling), app (buying gold) |
| Exchange-house and employer relationships | Gift orders → kiosk hosts → app distribution → loan desk locations |
| Appraisers, XRF testing, family trust | Old-gold desk → loan desk |
| Customers who already know us | App savers → jewellery conversion → loans |

#### Money and timing summary

| Step | Starts | Capital | Earns | Break-even | Go / no-go test |
|---|---|---|---|---|---|
| Gift desk | Month 0; first revenue Jan–Mar 2027 | USD 0.1–0.3m | About AED 6,000 an order | About 40 orders a year | 5 signed Eid orders at ≥ AED 35 a bar margin |
| Jewellery referral | Month 0 | About zero | About AED 100–500 a conversion | n/a | One jeweller signs |
| Card FX | Month 0; pays later | Partner + about USD 30k a year | USD 7–13 per cardholder a year | Depends on partner terms | Signed card partner |
| Old-gold desk | Months 3–9 | USD 0.35–0.6m | About AED 136 a ticket (AED 30–80 in the bad case) | 7–9 tickets a day (15–40 bad case) | 2-week pilot: 9+ a day, refiner ≥ 99%, souk < 98.5% |
| Gold-loan desk | Months 9–18 | USD 1.2–1.8m, no loan book | About AED 145 a loan after costs | About 8 loans a day a desk; AED 41–49m company book | Bank term sheet ≥ 6% a year within 6 months |

- Steps 1 and 2 together need about USD 0.6–0.8m, leaving most of a USD 1–3m seed for Step 3.

**How to say it to CG:** "Start small and paid-upfront, learn the customers and the gold, and let a bank carry the loan book. Every step pays for itself or gets stopped early. Steps 1 and 2 are small, real businesses. The scale comes from lending and from owning distribution, not from the token."
