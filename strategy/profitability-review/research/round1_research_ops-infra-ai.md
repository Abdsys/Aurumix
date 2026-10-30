# Aurumix: what gets it to profit (research for the Friday prep)

*Research date 29 Oct 2026. Every number has a confidence tag: (H) high, (M) medium, (L) low.*

## Bottom line

- **Staff handling is not where most of the margin goes. The bar-buying cost and the payment rails are.** Our own entry-fee build-up puts **3.0% into the fabrication premium** on 100 g bars, out of a 4.15% total. One price aggregator quotes 100 g bar premiums of **0.13–1.31% over 30 days** (L, [search summary](https://findbullionprices.com/p/100-gram-gold-bars/)). Dubai Good Delivery kilobars usually trade at or below London, and the discount reached **$10–30/oz** during the March 2026 disruption (M, [Kitco](https://www.kitco.com/news/off-the-wire/2026-03-09/dubai-gold-trades-discount-london-due-flight-disruptions), [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-06/gold-stuck-in-dubai-is-being-sold-at-a-discount-as-war-widens)).
  - Buying kilobars wholesale and giving each holder a fractional share against a serial-numbered bar list (the PAXG/XAUT approach) could take **about 2–2.5pp** off cost.
  - At a USD 50/month average saver that is **about USD 15/customer/yr**. That is more than the USD 10.48 the Monte Carlo says each UAE customer loses.
- **Retail-only is very hard at small tickets.** Nubank, the benchmark for cheap retail banking, spends **USD 0.80 per active customer per month**, about USD 9.60/yr (H, [Nu Q2'25](https://international.nubank.com.br/company/nu-holdings-ltd-reports-second-quarter-2025-financial-results/)). A USD 20/month saver brings in USD 12/yr in entry fees.
- **The margin in gold comes from credit and from physical products.** Holding and wholesaling the metal earns very little (table in section 3).
- **An AI agent works best as a feature that keeps people paying.** It is a weak paid product, and an agent that decides for the client needs a licence.
- **A generic gold "infrastructure" layer is already taken in the UAE.** SafeGold sits inside e& money and O Gold sits inside Botim. A seed-stage company can win a narrow distribution niche. It cannot win a broad protocol.

## 1. Operating costs and what automation fixes

| Cost line | Benchmark | Effect on Aurumix | Fix |
|---|---|---|---|
| UAEDDS direct debit | **AED 5 + VAT per collection**, about AED 6,000/yr setup (L, [directdebit.ae summary](https://www.directdebit.ae/)) | **7.2% of a USD 20 ticket**, 1.9% of USD 75. At USD 20/month, 12 debits cost **USD 17/yr against USD 12 of fee revenue** | Collect quarterly (2.4%), set an AED 250 minimum, or add on to a spot buy |
| Card acquiring | Stripe UAE **2.9% + AED 1** (M, [Stripe](https://stripe.com/ae/pricing)). CBUAE caps domestic debit interchange at **0.75% in person / 1.00% online** from Oct 2024 (M, [exploretech](https://news.exploretech.io/en/what-you-need-to-know-about-uaes-new-interchange-fee-rules)) | 4.26% at USD 20, which matches our "card rail 4.25%" finding | Negotiate debit-only acquiring priced near the cap. Route through Jaywan, live 20 Jul 2026 with no extra merchant fee (M, [The National](https://www.thenationalnews.com/business/money/2026/07/20/uae-starts-issuing-jaywan-cards-to-banks-and-financial-institutions/)) |
| Aani | 12.5m users, 74 FIs, about 774k merchants (Apr 2026). Pricing is set by each bank (M, [PaymentExpert](https://paymentexpert.com/2026/10/21/uae-fintech-hub-open-finance-2026/)) | Near zero for one-off top-ups. A recurring mandate is only "planned" (L) | Use for spot buys and payday top-ups now. Use mandates when they go live |
| KYC | Digital: **AED 1.5–4 per check** at runtime. Manual: **AED 80–250** (L, vendor estimates, [Skyline](https://skylineat.ae/blog/digital-onboarding-uae-ai-biometrics-guide)). UAE PASS integration about AED 44–92k (L) | With **53.5% passing the 6-payment gate**, each retained account effectively costs double the KYC | UAE PASS plus liveness checks. Never use manual KYC except for exceptions |
| Support | Klarna's AI handles about two-thirds of chats. Cost per transaction fell **$0.32 → $0.19**. Klarna re-hired humans in 2025 after quality dropped (M, [Twig](https://www.twig.so/blog/klarna-ai-customer-support-efficiency)). Median tier-1 deflection 41%, top quartile 59% (L) | Diaspora customers expect WhatsApp support in their own language | AI first-line support in Hindi, Urdu and Malayalam, with a guaranteed route to a human |
| Allocation and reconciliation | Fabrication premium of 3.0% in our build-up versus a wholesale kilobar near London (M) | The biggest single line | A kilobar is about USD 129k at $4,024/oz. At 45k accounts × USD 50 that is about 17 kilobars a month. Before that scale, buy through a dealer's pooled allocated account |

**Practical read:** the quickest way to profit is a cheaper cost stack (sourcing, rails, ticket size), not more features.

## 2. Tokenized gold and digital gold are different markets

| | Tokenized (on-chain) | Digital gold (app ledger) |
|---|---|---|
| Size | About **$5.1–5.5bn**. XAUT about **$3.26bn**, PAXG about **$1.78bn**, together about 90%+ (M, [altii](https://www.altii.de/the-altii-gold-report-2026-10-27/), [CMC](https://coinmarketcap.com/view/tokenized-gold/)) | India UPI digital gold peaked at **₹3,172 cr across 254m transactions in Mar 2026**, about ₹125 (about USD 1.4) per transaction (M, [FinanceOutlook](https://www.financeoutlookindia.com/news/digital-gold-purchases-via-upi-hits-record-254m-transactions-in-march-nwid-7966.html)) |
| Buyer | Crypto-native users, exchanges, people borrowing against it | First-time savers on mass apps |
| Pricing | PAXG **0.02%**, waived to 1 Jan 2027, no storage fee (M, [Paxos/search](https://www.paxos.com/pax-gold)). XAUT 0.25% | Spreads of about **2–3% + 3% GST** in India (L). Gulf apps quote 0.5–1.5% each way (L, [DahabPulse](https://dahabpulse.com/blog/digital-gold-apps-in-the-gulf-fees-custody-real-costs)) |
| What wins | Liquidity and exchange listings. Smaller tokens stay small: Comtech CGO (Dubai) about **$15–24m** (M), Matrixdock about $54–72m (M), Kinesis about $348m (M) | Distribution. 90%+ of Indian digital gold goes through UPI apps (M, [Business Standard topic](https://www.business-standard.com/amp/topic/digital-gold)) |
| UAE players | Fasset × Tether Visa card with up to **6% cashback in XAUT**, funded by **$1m from Tether** (M, [CryptoBriefing](https://cryptobriefing.com/tether-gold-backed-visa-card-fasset/)) | O Gold: **1.5m users**, gold Mastercard, Aspora (diaspora) and Valura.ai partnerships (M, [Gulf News](https://gulfnews.com/business/corporate-news/ogold-crosses-15-million-users-as-digital-gold-and-silver-investing-surges-1.500621515)). Botim × O Gold: Dh22m volume, Dh700 average ticket (M, [Khaleej Times](https://www.khaleejtimes.com/business/digital-gold-rush-uae-invest-through-apps)). e& money × SafeGold from **Dh10** (M, [Arabian Business](https://www.arabianbusiness.com/finance/uaes-e-money-launches-digital-gold-trading-with-aed10-entry-point)) |

**Aurumix sits between the two markets.** It carries VARA-level cost but sells to digital-gold customers. Competitors already target its NRI segment (O Gold with Aspora) and its cashback feature (Fasset's subsidised 6%, against our interchange-funded rewards that are capped near 1%).

## 3. Where the margins are made

| Layer | Evidence | Margin |
|---|---|---|
| Wholesale and infrastructure | SafeGold FY25: EBITDA **₹2 cr on ₹6,867 cr** (**0.03%**) (M, [Entrackr](https://entrackr.com/fintrackr/safegold-clocks-rs-6867-cr-in-gold-transactions-in-fy25-turns-ebitda-positive-10814304)). Augmont FY26 EBITDA **0.41%** (M, [TradeBrains](https://tradebrains.in/augmont-enterprises-ipo-from-gold-refining-to-digital-gold-what-exactly-is-this-business/)) | Very thin; a volume business |
| Consumer gold app | Jar FY25: **₹208 cr operating revenue on ₹2,450 cr** of gold sold (about 8.5%, including jewellery). Profitable only from H2, after **35m users** (M, [TechCrunch](https://techcrunch.com/2025/09/18/indian-fintech-jar-turns-profitable-by-helping-millions-save-in-gold/)) | Works only at very large scale |
| Gold-backed credit | Muthoot FY26 PAT **₹10,134 cr (+95%)**, gold-loan AUM **₹1.65 lakh cr**, NIM about **12.7%** (M, [SMEStreet](https://smestreet.in/banking/muthoot-finance-fy26-profit-rises-98-to-10607-crore-11840960), [AngelOne](https://www.angelone.in/news/market-updates/muthoot-finance-q1-fy26-earnings-results-reported-37-percent-rise-in-loan-aum)) | **The largest profit pool** |
| Physical and branded products | 1 g PAMP bar **25–40%** over spot against about 0.8% for 1 oz (L, [MintBuilder](https://mintbuilder.com/blog/gold-premiums)). Trump ¼ oz rounds **11.7% to 61%** over melt (M, [FindBullionPrices](https://findbullionprices.com/p/donald-trump-quarter-oz-gold-coin/)). Dubai making charges **AED 8–20/g**, about 2–4% of 24K (M, [goldratesindubai](https://goldratesindubai.com/news/joyalukkas-malabar-kalyan-gold-rate-dubai-today)) | High, but only on the physical item |
| Robo / AI | Wealthfront FY25 revenue **$309m**: about **75% from cash management**, about 10% from advisory (H, [MostlyMetrics](https://www.mostlymetrics.com/p/wealthfront-ipo-s1-breakdown)). Cleo 2025 revenue **$254m**: **62% from cash-advance fees**, 35% from subscriptions (M, [Sacra](https://sacra.com/c/cleo/)) | The AI product brings users in; credit and float earn the money |

**On branding:** a token that must be bought back at the LBMA fix cannot hold a brand premium. The premium can be earned on minted Aurumix 1–10 g gifting bars or coins for weddings, Diwali, Eid and Akshaya Tritiya. Counsel must confirm that a making charge on a minted item is not treated as a redemption fee, which VARA forbids.

## 4. AI agents ("Weaver")

**"Weaver" does not match any consumer gold or wealth agent we could find (L).** The candidates are:
1. **Weaver**, a Tquila × You.com joint venture launched in June 2026. It is a fixed-fee enterprise AI integrator ([Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/weaver-launches-ai-native-systems-110000050.html)).
2. **Weaver AI**, an enterprise agent platform with 50+ pre-built finance, HR and procurement agents ([weaver.com.co](https://weaver.com.co/blog/weaver-ai-agent-designer-enterprise-intelligent-automation-platform/)).
3. **Weavr.io**, embedded-finance APIs marketed as the way AI agents execute payments ([Weavr](https://www.weavr.io/blog/two-roads-to-growth-ai-and-embedded-finance/)).
4. **Wayfinder (PROMPT)**, crypto agents that operate wallets ([Nansen](https://www.nansen.ai/post/what-is-ai-wayfinder)).
5. An open-source "weaver" crypto portfolio tracker ([GitHub](https://github.com/ibis01/weaver)).

**We should ask Tony for the link.**

**Paid AI money products that exist:**
- **Origin**, an SEC-registered AI advisor: $12.99/month or $99/yr, sold at **$1 for the first year** (M, [Spendalyst](https://spendalyst.com/blog/origin-financial-review)). The promotion suggests weak willingness to pay.
- **Robinhood:** Cortex is bundled into the $5 Gold plan. Strategies costs 0.25%, capped at $250/yr (M, [Finder](https://www.finder.com/stock-trading/robinhood-review)).
- **Giza** (DeFi agent): AUM above **$40m**, takes **10% of yield**. Its ARMA agent was retired in March 2026 (M, [KuCoin](https://www.kucoin.com/blog/what-is-giza-), [OwnYourMind](https://ownyourmind.ai/projects/giza/)).
- **Sarwa (UAE):** 0.85% down to 0.40%, with a **$7/month minimum**. About **$1bn AUM across about 300k users**, profitable since 2024 (M, [BrokerMatch](https://www.brokermatch.ae/reviews/sarwa-uae-review), [Economy ME](https://economymiddleeast.com/news/sarwa-surpasses-1-billion-client-aum-first-uae-fintech-milestone/)).

**Do people trust AI to manage money?** In 2026 Gallup found about 20% of US adults use AI for financial advice, but about **70% have little or no confidence in it** (M, [Fortune](https://fortune.com/2026/08/08/financial-advisers-trust-ai-usage-gap-gallup/)).

**Regulation:**
- **SCA (2025):** robo-advisory is allowed only for **licensed portfolio managers** (M, [The National](https://www.thenationalnews.com/business/money/2025/07/04/uae-investing-robo-advisory/)).
- **VARA:** discretionary management of virtual assets needs a **Management & Investment Services** licence. Sources conflict on capital, from AED 280k to AED 1.5m (L, [10 Leaves](https://10leaves.ae/publications/blockchain-crypto/guide-to-vara-management-and-investment-services-licenses)).
- **DFSA:** this falls under Advising or Managing Assets (M).
- **Safe zone:** automation that only follows rules the user sets (SIP timing, round-ups, payday top-ups, retrying failed debits, nudges) does not make decisions for the client. Counsel needs to confirm this.

**Verdict:** use AI as a **persistence and servicing engine**. Its job is to lift the 53.5% gate pass rate and cut support cost. Bundle it into the family plan rather than selling it on its own.

## 5. Infrastructure or protocol plays

- **SafeGold** has **200+ partners** and **80m+ investors**. It offers app-within-app integration or REST APIs and covers buy/sell, SIP, delivery and leasing. It entered the UAE through e& money in April 2026 (M, [SafeGold](https://www.safegold.com/blog/digital-gold/safegold-partners-apps-india-complete-list/), [TechAfrica](https://techafricanews.com/2026/04/13/e-money-launches-digital-gold-investment-platform-in-uae-with-safegold-partnership/)).
- **Augmont** has 180+ partners and a ₹800 cr IPO filing (M, [Business Standard](https://www.business-standard.com/markets/ipo/augmont-enterprises-files-drhp-with-sebi-for-800-cr-ipo-promoters-to-sell-180-cr-stake-125100100669_1.html)).
- **Tokenization-as-a-service:**
  - Platforms charge about **$50–100k upfront**, plus $5–25k/yr for transfer-agent services (L, [TokenizeStartup](https://tokenizestartup.com/platforms/tokenization-platform-fees/)).
  - VARA Category 1 issuance costs **AED 100k to apply and AED 200k/yr in supervision** (L, same source).
  - A Year-1 VARA RWA launch costs about **AED 0.5–1.2m** (L, [Neos Legal](https://neoslegal.co/rwa-tokenization-guide/)).
- **Pricing gap:** our B2B fee of **0.75%/yr** on partner gold compares with **0% storage at PAXG/XAUT**. Gulf storage benchmarks run **0.12–0.5%** (L). Partners will pay 0.75% only if it comes bundled with SIP, card, credit and KYC. **We should stress-test that 35% revenue line.**

**What winning infrastructure takes:** bullion inventory and hedging lines (a balance sheet), a live licence (we have not applied), dozens of distribution partners, and an all-in price around 0.1–0.5%. SafeGold earns 0.03% EBITDA even at its scale.

**A niche a startup could win:** a white-label "SIP + gold credit line + family/will" stack for **exchange houses and WPS agents** serving NRI corridors.
- Al Ansari has 225–280 branches and acts as a WPS agent (M, [dailysuae](https://dailysuae.com/al-ansari-exchange/)).
- WPS moves **more than AED 35bn a month for 5m+ workers** (L, [UAE payroll guide](https://whichpayroll.com/countries/uae/global-payroll)).
- This is a **distribution partnership**, not a protocol.

## 6. What to put on the table Friday (ranked)

1. **Fix the cost stack first:**
   - Wholesale kilobars with fractional allocation: about 2–2.5pp saved.
   - Quarterly or minimum-ticket collection, with debit/Jaywan/Aani rails.
   - UAE PASS KYC.
   - AI-first support.
2. **Go B2B2C through exchange houses, WPS agents and employers,** and price the platform fee against SafeGold and XAUT.
3. **Make the gold-backed credit line the profit engine,** with gold as the hook and the collateral. The Muthoot and Cleo numbers support this.
4. **Build the AI agent around persistence, staying non-discretionary,** and bundle it into the subscription.
5. **Earn brand premiums on physical gifting SKUs,** not on the token.
6. **Avoid an open protocol or token-infrastructure layer** unless a partner brings the balance sheet. XAUT and PAXG hold about 90% of the tokenized market, and CGO is about $20m after years of trying.

**Question for CG:** does "infrastructure" mean (a) issuing tokens for others, (b) an API for partners, or (c) a DeFi collateral protocol? Each one needs a different licence and a different balance sheet.