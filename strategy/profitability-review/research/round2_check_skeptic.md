# Gold-token issuers: can they sustain margins? And the best basic offering to build from scratch

Date: 2026-10-29. Confidence tags: (H) high, (M) medium, (L) low.

**Search note:** web search was already used up for this session (200 of 200). I spot-checked by opening primary sources directly: CoinGecko's API, SEC EDGAR, the Tokyo Stock Exchange (TSE) filing PDF, the DGLD MiCA white paper PDF, the Gold DAO Chapter 2.0 PDF, DefiLlama and XDCScan. Everything marked "re-verified" below was read from the source today.

---

## PART A. Gold-token issuers

### A1. Spot-checks done this run

| Issuer | What I re-verified | Result |
|---|---|---|
| All listed tokens | Market caps on CoinGecko today ([API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=tokenized-gold)) | **Confirmed (H).** XAUT $3,249M, PAXG $1,795M, KAU $356M, GGBR $82M, PGOLD $79M, XAUM $70M, GLDY $12.4M, DGLD $9.7M, VNXAU $5.7M, XGZ $5.0M, CGO $3.1M, XAUH $2.0M, XNK $1.9M, GLDT $0.77M, TGLD $0.56M. PGOLD and GLDY show $0 volume in 24h. |
| Streamex (GLDY) | Q2-26 8-K ([SEC](https://www.sec.gov/Archives/edgar/data/1530766/000149315226039547/0001493152-26-039547.txt)) | **Confirmed (H).** Burn was $1.6M a month (including $0.5M of one-offs), guided to $1.1M a month for Q3. Revenue was $0.1M of gold lease income, "its first income". Liquidity was $41.8M, of which $15.5M is physical gold. |
| Goldfish / I-ON Digital | FY25 10-K ([R4](https://www.sec.gov/Archives/edgar/data/1580490/000149315226016842/R4.htm)) | **Confirmed (H).** Revenue $433,012. Operating costs $3,198,874. Net loss $2,883,992 (FY24 loss: $1,910,013). |
| Kinka | TSE filing, 16 Oct 2026 ([PDF](https://tdnet-pdf.kabutan.jp/20261016/140120261016552360.pdf)) | **Confirmed (H).** Kinka (BVI) revenue was ¥9K, ¥725K and ¥26K in FY3/24, FY3/25 and FY3/26. Operating losses were ¥17.9M, ¥7.4M and ¥5.9M. Stated reasons: the leading competitors had an "overwhelming share" and new management judged the business "difficult to secure profitability". Last day for buyback or gold exchange is **30 Oct 2026, 17:00 JST**. The Cardano tokens were never sold and are being burned. |
| DGLD | MiCA white paper ([PDF](https://files.dgld.ch/dgld-white-paper.pdf)) | **Confirmed (H).** Net loss was CHF 1,542,188 in 2024 and CHF 123,156 in 2025. Total assets CHF 452,850. MKS PAMP is the sole shareholder. Creation and burning fees are 0.20% each. |
| Gold DAO (GLDT) | Chapter 2.0 PDF ([PDF](https://fjdhj-uyaaa-aaaai-q4fma-cai.icp0.io/GoldDAO_Chapter2.0.pdf)) | **Confirmed (H), word for word:** "fees from all GLDT transactions averaged 1,000 CHF per month. We would need about five times that amount to cover storage costs, security audits…". Also: "USD 100 million could generate at least 100k per month". And Bity's 2.5% margin "doesn't even cover one-fifth of the real costs". |
| Comtech Gold (CGO) | XDCScan ([token](https://xdcscan.com/token/0x8f9920283470f52128bf11b0c14e798be704fd15)) | **Confirmed (H).** On-chain supply is 24,000 with 477 holders. The 141,000 "circulating" figure is stale. |
| XAUT (benchmark) | DefiLlama ([fees](https://api.llama.fi/summary/fees/tether-gold)) | **Fees of $4.26M a year (M).** That is about 0.13% of a $3.25B supply, and it includes Tether's own treasury mints. |
| Kinesis | Yields and holders-yield pages | **Not re-verified.** The pages did not render the fee split or the monthly figures. The verdict still rests on the July profile and one month of data. |

### A2. Where I challenge the verdicts

- **Kinesis, "BURNING".** Revenue comes from one month of holder yield. Cost comes from LinkedIn headcount times an assumed salary. No accounts exist. **I downgraded it to "Likely burning" (L–M).** The direction is believable: free storage, $64K a day of volume, KVT down 81%, and fee share moving to KVT. The size of the loss is a guess.
- **Goldfish, "BURNING".** This is High only for the supplier, I-ON. GGBR Inc. itself is unseen. The $82M market cap is misleading because the token is backed by **gold still in the ground**, and probably only $5–23M was ever sold for cash (L). Treat it as a mining-claim token, not vaulted gold.
- **Pleasing, "SUBSIDISED BY PARENT".** No parent financials were seen. **Changed to UNKNOWN** (most likely a dealer's cost centre). Volume was $0 in 24h (H), and there is no gold attestation.
- **HSBC XGT, "PROFITABLE at the margin".** It is a pure scenario: AUM, holders and volume are all undisclosed. **Changed to UNKNOWN, likely profitable at the margin** (L). It is the only plausible winner here, because HSBC already owns the customer, the vault and the app.
- **Comtech, "BURNING".** The supply collapse is High (108k g to 24k g). The cost base (5 staff) is a guess. **Likely burning (M).**
- **Gram Gold / ONS Gold.** CoinGecko now shows a $0 market cap. On-chain activity looks like an inventory ledger. **UNKNOWN (L).**
- **XAUT.** My own view is that fees of $4.26M a year against Swiss vaulting on $3.2B of gold (about $1.6–3.2M at 0.05–0.10%, L) leave a thin token-level margin. Tether's stablecoin business carries everything else.
- **Dead-list conflict.** The census says DigixDAO dissolved in 2020. The idea notes say "Digix in 2022". The DAO dissolution vote was in 2020, but DGX lingered after that. The year it died is M.

### A3. Final table: live issuers

"Pure-play" means the gold token is the company's main business.

| Issuer | Ticker | Market cap | Pure-play? | Est. token revenue / yr | Verdict | One-line reason |
|---|---|---|---|---|---|---|
| Tether Gold | XAUT | $3,249M (H) | No (Tether) | $4.26M (M, [DefiLlama](https://api.llama.fi/summary/fees/tether-gold)) | BREAK-EVEN to thin profit; parent carries it (L) | 0.25% buy and redeem fee and 0% storage, so about 0.13% of supply a year. |
| PAX Gold | PAXG | $1,795M (H) | No (Paxos) | Not verified (DefiLlama returned an error) | UNKNOWN (L) | A side product of a stablecoin and custody company. |
| Kinesis | KAU / KAG | $356M (H) | **Yes** | ~$1.5–2.4M kept (L–M) | **Likely BURNING** (L–M) | Free storage and a team of 100–195 against about $2M of fees. No accounts. |
| Goldfish | GGBR | $82M (H; misleading) | Yes | $0 to supplier in Q2-26 (H) | **BURNING** (H for I-ON) | Supplier lost $2.88M in FY25 and carries a going-concern warning. Backing is gold in the ground. |
| Pleasing Gold | PGOLD | $79M (H) | No (HK dealer) | ~$0 kept (M) | UNKNOWN (L) | 0% fees, the one fee goes to stakers, $0 volume, no attestation. |
| Matrixdock | XAUm | $70M (H) | No (Matrixport/BIT) | ~$0.07–0.13M (L) | SUBSIDISED BY PARENT (M) | Mint fee waived and no management fee. A group with $6B+ in assets pays the costs. |
| AZ Gold Reserve | AZG | ~$125M (issuer API, M) | No (mining finance) | ≤$1.25M if the fee is charged (L) | UNKNOWN (L) | Real profit or loss sits in its mining-loan book. Bar cover fell to 26% (H). |
| Zipangcoin | ZPG | ~$25M (M) | No (Mitsui & Co.) | ~$0.15–0.6M (L) | SUBSIDISED BY PARENT (M) | Gold is leased back to Mitsui. Growing, on 8 exchanges. |
| Streamex | GLDY | $12.4M (H) | **Yes** | ~$0.6M, mostly lease income on its own gold (H/M) | **BURNING** (H) | $1.1–1.6M a month of burn. Stock down 91%. Nasdaq deficiency notice. 24h volume $0. |
| DGLD | DGLD | $9.7M (H) | No (MKS PAMP) | $13–39K (M) | SUBSIDISED BY PARENT (H) | Lost CHF 1.54M in 2024 and CHF 0.12M in 2025. 0% custody fee. |
| VNX Gold | VNXAU | $5.7M (H) | **Yes** | $4–30K (L) | **BURNING, retrenching** (M–H) | Closed its exchange, cut 6 chains and pivoted to selling B2B technology. |
| GoldZip | XGZ | $5.0M (H) | No (HKGX group) | <$5K (M) | BURNING, carried by group (M) | 95% of supply in one wallet. No reserve report. Moved its issuer to the BVI. |
| Aurus | tGOLD | $5.65M at NAV (M) | **Yes** | $0 to the company (M) | **BURNING, near shutdown** (H) | UK compulsory strike-off notice on 15 Sep 2026. Trades 51% below its gold value. |
| Meld Gold | GOLD$ | ~$4.2M incl. silver (H) | **Yes** | $5–80K (L) | **BURNING** (M) | No mints in 2026. Gold float down 82%. No live attestation. |
| Comtech Gold | CGO | $3.1M (H) | **Yes** | <$30K going forward (L) | **Likely BURNING** (M) | Supply down 78% in 2026 (H). Main site closed. Last reserve report March 2025. |
| Herculis | XAUH | $2.0M (H) | No (Herculis Group) | $10–75K to date (L) | SUBSIDISED BY PARENT (M–L) | KPMG procedures-only reports give "no assurance". The gold is booked as a group asset. |
| WisdomTree Gold | WTGOLD | $1.98M (M) | No (WisdomTree) | $5–80K (L) | SUBSIDISED BY PARENT (H) | 0.001% of the parent's AUM. The CEO says the digital arm is "not currently making money". |
| Gold DAO | GLDT | $0.77M (H) | No (Bity/ORIGYN) | ~$12K (H, own paper) | BURNING / SUBSIDISED (H) | Fees cover about 1/5 of basic costs. Merged into ORIGYN. |
| Tenbin Gold | TGLD | $0.56M (H) | No (FX-carry protocol) | ~$0 net (L) | BURNING, VC-funded (M) | Futures-backed, not vaulted. Built to earn close to zero margin. |
| AABB Gold | AABBG | ≤$25M, float ~$3.6M (L) | No (OTC miner) | ≤$22–44K (L) | SUBSIDISED BY PARENT (M) | Old wallet and domains are dead or hijacked. The parent stock is down 94%. |
| Gram / ONS Gold | GRAMG / ONSG | $0 on CoinGecko; ~$6.2M on-chain (L) | No (B2B tech house) | $11–22K (L) | UNKNOWN (L) | 4 wallets hold everything. No attestation. |
| HSBC Gold Token | XGT | Undisclosed | No (HSBC) | Scenario: $0.75–7.5M (L) | UNKNOWN, likely profitable at the margin (L) | Up to 2% each way, no extra custody or acquisition cost, upgraded in Feb 2026. |

*Excluded:* Oropocket ORO. It is not a gold token. It is now an Indian digital-gold app (H).

### A4. Dead issuers and why they died

| Issuer | Pure-play? | Died | Why |
|---|---|---|---|
| **Kinka (XNK)** | No (unbanked Inc., TSE) | Closing now. Final buyback 30 Oct 2026; entities wound up by Mar 2027 (H) | Revenue never above ¥725K a year. Competitors had an "overwhelming share". Its stablecoin route on Cardano failed. DEX sales were legally risky ([TSE PDF](https://tdnet-pdf.kabutan.jp/20261016/140120261016552360.pdf)). |
| **Lode (AUX/AGX)** | Yes | Operator in liquidation since Oct 2025 (H, [UID register](https://www.uid.admin.ch/Detail.aspx?uid_id=CHE386915113)) | About $2.4M of metal earning about $20K a year against a six-figure cost base. The token trades at 1.7% of its gold value. |
| **CACHE Gold (CGT)** | Yes (inside a vault group) | Stopped being gold-backed 30 Sep 2025 (H) | Storage fee charged only on transactions, about $12M AUM and 4 vaults. Only 2.3% of supply was airdropped PAXG. |
| **Perth Mint (PMGT)** | No (state mint) | Discontinued. 115 tokens left (H, [CMC](https://coinmarketcap.com/currencies/perth-mint-gold-token/)) | Even a state mint could not justify running it. |
| **Digix (DGX)** | Yes | DAO dissolved 2020. 0 circulating (M) | First-generation pure play. Fee model never reached scale. |
| **GoldMint** | Yes | Down 99.9%, $0 volume (H, [CMC](https://coinmarketcap.com/currencies/goldmint/)) | ICO-era 2018 project that collapsed. |
| **Royal Mint Gold (RMG)** | No (UK mint + CME) | Shelved in 2018 before launch (M) | A big institution walked away before launch. |
| **OneGram (OGC)** | Yes | No activity found (L) | An early Dubai Shariah token that faded. |
| *Near-dead:* Aurus | Yes | Strike-off notice 15 Sep 2026 (H) | Takes 0% of its own fees by design. Pivoted to gold in the ground. |

### A5. Plain lessons: can a pure gold-token issuer sustain margins?

1. **No pure-play issuer here is proven profitable.** Of the pure plays, 4 are dead and 6 are burning, retrenching or likely burning. Kinesis, the only one at scale, publishes no accounts (H on the pattern).
2. **Savers who hold earn the issuer nothing.** Almost everyone charges 0% storage, and exchanges keep the trading fees. Even XAUT earns only about 0.13% of supply a year (M).
3. **Break-even needs roughly $250–500M of gold** (L–M). Gold DAO's own numbers say the same thing: $1M of gold makes about $1K a month, and $100M would make about $100K a month (H). Only XAUT, PAXG and maybe Kinesis are above that line.
4. **The tokens that survive are side products.** Tether, Paxos, HSBC, Mitsui, MKS PAMP, WisdomTree and Matrixport each already own the customer, the vault or the metal desk. For them the token is a channel or collateral, not a profit centre.
5. **The money is in what happens around the gold:**
   - the markup when a customer buys (Bity 2.5%, HSBC up to 2% each way);
   - lending or leasing the gold (Mitsui's lease-back);
   - jewellery making charges.

   This is why the from-scratch shortlist below drops token issuance.

---

## PART B. The best basic offering to build from scratch

### B1. Where the two judges agree

- **Best: a B2B Festival & Rewards Gold Desk.** This merges the Gift Gold and Rewards Desk ideas.
- **Runner-up: an Old Gold Desk**, opened only if a two-week price test passes.
- Both run on one dealer licence, one compliance setup and one mint or refiner relationship.
- **Do not fund at seed:** a gold token, the lease desk, either wedding plan, or our own finance company.
- **Keep the Gold Loan Desk as phase 2.** It is the biggest profit pool. Muthoot's ROE is 31% (H, [Screener](https://www.screener.in/company/MUTHOOTFIN/)). But it needs a bank partner and a structure that satisfies the central bank's (CBUAE's) rules.

### B2. Best offering: B2B Festival & Rewards Gold Desk

- **Customer:** UAE companies with South Asian staff or customers.
  - Their HR teams buy long-service, Eid and Diwali gifts.
  - Their marketing teams run prize campaigns. Exchange houses already do this: LuLu gave about 1,000 g in one campaign (H, [LuLu](https://luluexchange.com/promotion/send-win/)) and Al Ansari gave up to 9 coins in its Diwali promo (H, [Al Ansari](https://alansariexchange.com/promotions/)).
  - Community associations are a third buyer.
- **What they buy:** 1 g (also 2.5 g and 10 g) minted 24K bars in a logo card with an Eid, Diwali or long-service design. Delivery is on a fixed date and the price is fixed on the purchase order. The card prints a buyback promise of spot minus 1%.
- **How we make money on day one:**
  - The client pays 100% upfront by bank transfer.
  - We buy from the mint the same day, so we hold no stock and carry no price risk.
  - We keep the gap between our price and the mint's price.
- **Worked example: 300 × 1 g bars for an employer**
  - Mint price: AED 498.25 per bar, including AED 12.60 making (H, [Emirates Minting](https://emiratesminting.ae/product/E27461532M-1-gram-gold-bar/gold/gold-bar)). Add card, box and delivery of about AED 10 (L). **Our cost is about AED 508 per bar.**
  - **Our price is AED 540 per bar** (L). That is about 8% above the mint's plain bar and 5% below jeweller retail of AED 570 (M, [Al Fanan](https://www.alfanan.ae/collections/24k-gold-bar)).
  - Gross is AED 32 per bar × 300 = **AED 9,600** (about 6%).
  - Less sales time and handling of about AED 3,500 (L). **About AED 6,000 (USD 1,630) is left per order.**
- **Break-even:** fixed cost is about AED 250K a year with the founders selling and 1 operations hire. That needs **about 40 orders a year** (L).
- **Licence and partners:**
  - Dubai mainland (DED) trade licence for trading gold and precious metals.
  - Ministry of Economy registration as a Dealer in Precious Metals and Stones (DPMS), with goAML reporting and an AML officer.
  - VAT registration. Bars of 99% purity or more are zero-rated (M, [PBZ](https://www.pbz.ae/insights/vat-for-gold-and-jewellery-traders-uae-reverse-charge)).
  - No CBUAE, VARA (crypto regulator) or CMA (securities regulator) licence, because this is a sale of goods.
  - Partners: a UAE mint (Emirates Minting) or a DMCC dealer, and an insured courier.
  - Counsel to confirm: VAT on custom packs, and that any reward codes are closed-loop (redeemable only for our goods, never for cash).
- **Capital:** USD 0.1–0.3M (L).
- **Honest limits:**
  - There is no moat. A mint sells the same bar to anyone online.
  - Demand is seasonal.
  - Exchange-house prize campaigns earn only about 1.5%.
  - It is a cash wedge and a door-opener to exchange houses, not a big business on its own.

### B3. Runner-up: Old Gold Desk (kiosk inside an exchange-house branch)

- **Customer:** NRI households selling old, broken or unworn 22K jewellery. They sell for school fees, debts, leaving the UAE, or to swap into new pieces.
- **What they buy:** "See your price, watch the test, get paid in 15 minutes."
  - A purity test (XRF analyser) done in front of them, with the weight and live price on screen.
  - Payment by instant bank transfer, or sent straight home through the host exchange house.
- **How we make money on day one:** we lock our sale to a refiner at the same moment we buy. We earn the gap between what we pay the customer and what the refiner pays us.
- **Worked example: 25 g of 22K, which is 22.9 g of fine gold**
  - Fine value at spot of AED 478.8/g is AED 10,965 (H, derived from [Fortune](https://fortune.com/article/current-price-of-gold-10-28-2026/)).
  - **We pay the customer 97.5%: AED 10,691**, about AED 428/g of 22K. The 22K shop selling rate is AED 451.75 (M, [AngelOne](https://www.angelone.in/news/commodities/gold-rate-dubai-vs-india-gold-prices-on-october-29-2026)).
  - **The refiner pays us about 99.4%: AED 10,899** (L; needs a written quote).
  - Gross is AED 208 (1.9%).
  - Less about AED 22 for KYC, transfer, insurance and assay, and an AED 50 community referral. **About AED 136 (USD 37) is left per ticket** (L).
- **Break-even:** fixed cost of about AED 330–451K a year means **about 7–9 tickets a day** (L).
- **The catch:** souk buyers may already pay about 98% of fine value (L–M, [Himmath](https://himmathgold.com/how-to-sell-gold-in-dubai-buyback-rates-spreads-and-what-youll-actually-be-paid/)). If we have to match that, contribution falls to about AED 30–80 per ticket and break-even rises to **15–40 tickets a day**.
- **Licence and partners:**
  - The same DED licence and DPMS/goAML registration as B2.
  - ID on every ticket, and reports on cash or linked deals of AED 55,000 or more.
  - Partners: a Dubai refiner, and an exchange house that hosts the kiosk and earns FX margin on payouts sent home.
  - **Never** pay cash against gold with a right to buy it back. That is lending, and doing it without a licence carries fines of at least AED 1M (M, [Muhami](https://muhami.ae/articles/do-you-need-a-cbuae-licence-before-16-september-2026-a-simple-guide-to-the-new-uae-central-bank-law/)).
- **Capital:** USD 0.35–0.6M, including an AED 1–1.5M payout float (L).
- **Why it matters later:** it builds the appraisers, XRF testing, refiner relationship and family trust a bank would want to see before backing a gold-loan desk.

### B4. First 90 days for both (from 1 Nov 2026)

- **Days 1–30**
  - File the DED licence and start DPMS/goAML registration and the bank account.
  - Get written quotes from the mint, 2 DMCC dealers and 2 refiners. **A refiner must pay at least 99%.**
  - Mystery-shop 10 souk buyers and jewellers for their 22K cash price.
  - Pitch 20 employers and exchange houses for year-end awards and **Eid al-Fitr (about 9–10 Mar 2027, L)**.
  - Commission a USD 10–20K counsel memo covering VAT on packs, closed-loop reward codes, and the Gold Loan Desk routes.
- **Days 31–60**
  - Licence expected (4–8 weeks, L).
  - Design dies and packs.
  - Sign the refiner contract and a letter of intent for one exchange-house kiosk.
  - **Kill test 1:** 5 signed purchase orders paying at least AED 35 per bar over mint cost.
- **Days 61–90**
  - Deliver the first year-end orders and lock Eid orders with deposits.
  - Run Old Gold as a 2-week pilot in borrowed or appointment space, with no lease yet.
  - **Kill test 2:** at least 9 tickets a day trending, the refiner at 99% or more, and our payout competitive with souk buyers below 98.5%.
  - Open talks with 3 CBUAE-licensed lenders about the Gold Loan Desk, capped at USD 50K. **Move it up only on a term sheet that pays us at least 6% a year servicing** (Rupeek is the warning, H: [Entrackr](https://entrackr.com/2024/05/exclusive-rupeek-raises-fresh-funds-at-60-valuation-cut/)).
- **Realistic first revenue:** Jan 2027 (year-end awards) or Mar 2027 (Eid). Diwali on 8 Nov 2026 is too close.

### B5. Where the judges disagreed

| Point | Judge 1 | Judge 2 | Reconciled |
|---|---|---|---|
| Top-ranked of the two gift ideas | Gift Gold B2B | Rewards Desk | They are the same business, so they are merged. |
| Price per 1 g bar | AED 539 | Spot + AED 65, about AED 544 | AED 540 |
| Capital for the gift desk | USD 0.2–0.3M | USD 0.1–0.25M | USD 0.1–0.3M |
| Old Gold payout | About 5.4% under board, about AED 427/g | 97.5% of fine value, about AED 428/g | 97.5%. They are effectively the same. |
| Old Gold break-even | About 11 a day (no rent) | 9 a day, but **about 40 a day if forced to pay 98%** | 7–9 a day in the base case, 15–40 a day if forced to pay 98%. The mystery-shop test decides. |
| Gold Loan Desk | Open bank talks in month 1; stop if no term sheet in 6 months | Counsel memo plus 3 lenders, at most USD 50K; needs at least 6% servicing | Both, with the 6% floor. |
| Licence scores | Send Gold Home 3, own-brand Wedding Plan 2 | 4 and 3 | Does not change the top two. |
| Own finance company, margin score | 4 | 5 | Both see it as phase 2 only. |

### B6. Corrections to carry into the reply to the user

- **The Jar claim is wrong.** "About half of Jar's revenue comes from jewellery" is not supported by [TechCrunch](https://techcrunch.com/2025/09/18/indian-fintech-jar-turns-profitable-by-helping-millions-save-in-gold/). The article gives operating revenue of ₹2.08bn (FY24), says the Nek jewellery line "crossed ₹1bn last year", and gives no share of revenue. The "half" came from dividing figures from different years and different kinds of revenue (M). The defensible point is narrower: Jar is building a jewellery line, because jewellery margins are fatter than digital-gold spreads.
- **Old Gold Desk margin:** the original idea's 2.4% spread is untested. Plan on 1.4–1.9% (L).
- **Gift desk margin:** the original idea's 10.9% assumed charging retail price. Plan on about 6% (L).