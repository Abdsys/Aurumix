# Gold-token issuers: Lode (AUX), AABB Gold (AABBG), Oropocket (ORO)

As of 2026-10-29. I could not run web searches because the session's search budget was used up, so every figure comes from fetching pages directly. Three sources blocked me: OTC Markets, GlobeNewswire and LinkedIn. That means I have no team sizes from LinkedIn and no audited AABB filings.

**Short answer:** none of the three makes enough money from its gold token to cover its costs.
- **Lode**, the only pure-play, is in liquidation.
- **AABBG** survives as a side project of a penny-stock mining company.
- **ORO** is not a gold token, so it should be excluded.

## Prices used in all the sums

| Item | Value | Conf. | Source |
|---|---|---|---|
| Gold | $4,035.5/oz, which is $129.74/g or $0.1297/mg | High | Yahoo GC=F, 29 Oct 2026 (Dec-26 futures) https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| Silver | $52.60/oz, which is $1.691/g | High | Yahoo SI=F https://query1.finance.yahoo.com/v8/finance/chart/SI=F |

---

## 1. Lode Gold (AUX), from LOD3 Finance DAO / LODE (Switzerland) AG

**Correction to the input notes:** the site says each AUX is backed by **1 milligram** of gold, not 1 gram (High) https://lode.one. At 1 g per coin the supply would be worth about $873M, which is not believable for a token this obscure. 1 mg fits the numbers.

**(1) Fees**
- No percentages are published anywhere (High).
- The site lists eight "reward streams": minting, redemption, transfer fees, "Spot Plus/Under" arbitrage, exchange, money market, P2P and account abstraction. It gives no rates (High) https://lode.one
- support.lode.one no longer resolves in DNS, so the fee FAQ is gone (High).

**(2) Revenue estimate**
- AUX supply on Avalanche: 6,733,063.8 AUX (High) https://api.routescan.io/v2/network/mainnet/evm/43114/etherscan/api?module=stats&action=tokensupply&contractaddress=0x68327a91e79f87f501bc8522fc333fb7a72393cb
- Gold behind it, if fully backed: 6,733,064 × 1 mg = 6.73 kg (216.5 oz) × $4,035.5 ≈ **$0.87M** (Med).
- AGX (silver) supply: 882,979 AGX × 1 g = 883 kg × $1.691/g ≈ **$1.49M** (High supply / Med value) https://api.routescan.io/v2/network/mainnet/evm/43114/etherscan/api?module=stats&action=tokensupply&contractaddress=0x13e7bcefdde72492e656f3fa58bae6029708e673
- Total metal held on behalf of token holders: about **$2.37M** (Med).
- If Lode earned a fee equal to 0.5–1% of that per year: $2.37M × 0.5–1% = **$12K–24K a year** (Low; this rate is my assumption).
- Fees from on-chain trading are close to $0:
  - The last 100 AUX transfers run from 21 May to 23 Sep 2026 (High).
  - About 70% move between the same two addresses (0x83cc…, 0xf79a…) (Med).
  - Each moves about 2 AUX, which is roughly $0.26 of gold (High) https://api.routescan.io/v2/network/mainnet/evm/43114/etherscan/api?module=account&action=tokentx&contractaddress=0x68327a91e79f87f501bc8522fc333fb7a72393cb&page=1&offset=100&sort=desc
- The AUX market price shows the peg has collapsed:
  - DEX price is $0.002178 against $0.1297 of gold per coin. That is **1.7% of backing**.
  - Pool liquidity is $332, 24h volume is $0, and there are 598 holders (Med) https://dex.coinmarketcap.com/avalanche/0x9702d06abe17c747e5ae75b0792914412278dddd/
  - Nobody is buying at a 98% discount to redeem for gold. That suggests redemption is not working (Med).

**(3) Cost base**
- The site names these providers: Brinks, Loomis, Bureau Veritas, Fireblocks, Chainlink, The Network Firm, Nuvei and Simplex (High) https://lode.one
- My rough floor for a Swiss company plus vaulting, attestation and custody software: **about $100K–250K a year** (Low). No team size could be checked.
- Revenue of $12K–24K a year cannot cover that.

**(4) Hard evidence**
- The terms of use (effective 16 Feb 2024) name **LODE (Switzerland) AG, CHE-386.915.113** as the operator (High) https://lode.one/terms-of-use/
- The Swiss business register (UID) lists the name as "**LODE (Switzerland) AG in Liquidation**" (High) https://www.uid.admin.ch/Detail.aspx?uid_id=CHE386915113
  - VAT registration was deleted on 13 Oct 2025.
  - The LEI lapsed on 6 Mar 2024.
- North Data shows this timeline (Med) https://www.northdata.com/LODE%20(Switzerland)%20AG%20in%20Liquidation,%20Herisau
  - Registered 23 Sep 2020 with CHF 100K capital.
  - A director was removed on 25 Mar 2025.
  - Provisional liquidation on 15 Oct 2025, liquidation on 17 Oct 2025.
- lodewallet.com is now a parked page saying "This domain may be for sale" (High) https://lodewallet.com/
- The last reward reports are from Dec 2024 and Jan 2025. No attestation or reserve report is published (High).
- The LOD3 governance token still moves on-chain (last transfer about 27 Oct 2026). CoinMarketCap only has a preview page for it, showing 79.7M circulating out of a 770M maximum (Med) https://coinmarketcap.com/currencies/lode-token/

**(5) Parent:** Lode is a pure-play, so there is no other business to fund it.

**(6) Verdict: BURNING, now failed (the operating company is in liquidation). Confidence: High.**
- Evidence: the operating company has been in liquidation since Oct 2025, and the wallet domain is parked.
- Evidence: about $2.4M of claimed metal can yield only around $20K a year, against at least a six-figure cost base.

---

## 2. AABB Gold Token (AABBG), from Asia Broadband Inc. (OTC: AABB)

**Status update:** the token is not fully dormant. It is being relaunched through a new "GoldAxis" wallet on Algorand.

**(1) Fees**
- Mint, redeem, storage and spread fees are not disclosed. The only stated fee is "zero deposit fees" on the AABB Exchange (High) https://aabbgoldtoken.com
- Each token is 0.1 g of gold. The site says the price is "supported at a minimum of 0.1 grams of the spot price of gold". It describes **no physical redemption** (High).
- The GoldAxis wallet site lists AABBG and AABBS (silver) on Algorand. It shows no fees and says the KYC and compliance phases are "not started" (High) https://www.goldaxis.com

**(2) Revenue estimate**
- Algorand asset 1136160962 has a fixed supply of **100,000,000 AABBG** (High) https://mainnet-idx.algonode.cloud/v2/assets/1136160962
- One wallet (QBH7…, created around Mar 2026) holds 98,064,223 AABBG, or **98.1%** (High) https://mainnet-idx.algonode.cloud/v2/assets/1136160962/balances?currency-greater-than=100000000&limit=20
- That leaves at most **1,935,777 AABBG** anywhere else.
  - At 0.1 g each: 1,935,777 × 0.1 g × $129.74/g = **$25.1M at most** (Med).
  - The next two wallets hold 998,500 and 663,144. They look like company or exchange wallets (Low).
  - Without those, holders' float is about 274K AABBG, which is **about $3.6M** (Low).
- At launch in Mar 2021 the company said 5.4M tokens were backed by "$30M" of gold (Med, company claim) https://aabbgoldtoken.com/news
- Activity: about 28 transfers with a non-zero amount between about 13 and 24 Oct 2026. That annualises to roughly 930 a year (Med).
  - The average transfer is about 182 AABBG ($2.4K), from a May 2026 sample.
  - Gross flow is then about $2.2M a year.
- If every transfer were a trade paying a 1–2% spread: **$22K–44K a year, as an upper bound** (Low; the spread is my assumption).

**(3) Cost base**
- No outside vault, audit or attestation is disclosed. The gold is "held by Asia Broadband" itself (High).
- Real costs are wallet development (GoldAxis), Sumsub KYC and support. My guess for a small wallet team is $200–500K a year (Low).
- Token revenue does not cover that.

**(4) Hard evidence**
- Stock price $0.0094. Market cap **$41.5M** (4.42B shares). 52-week range $0.0062–$0.0414. 42 employees (Med) https://stockanalysis.com/quote/otc/AABB/
- The stock is **down 94%** from $0.156 at the end of Q4 2021 (High) https://query1.finance.yahoo.com/v8/finance/chart/AABB?range=5y&interval=3mo
- Company headline from 12 Aug 2026: "Production Revenues … Q2 2026 Reaching $14.9 Million, Exceeding Total 2025 Revenues … $30 Million In 2026". This is the company's own unaudited claim (Low–Med). Release list: https://stockanalysis.com/quote/otc/AABB/
- An earlier article put Q1 2024 production revenue at $1.4M. That article was **paid promotion**: "RazorPitch has been retained and compensated…" (High) https://markets.financialcontent.com/stocks/article/newsdirect-2024-7-11-asia-broadband-inc-otcaabb-a-gold-and-digial-asset-duel-threat
- Shares are being issued as payment, which dilutes holders: "$23.5M share deal" for the rGO gold-recovery system on 31 Jul 2025, and a stock dividend in Jul 2025 (Med).
- Signs the old token setup was abandoned (High):
  - asiabroadband.com redirects to a GoDaddy for-sale page. The current company site is asiabroadbandinc.com, which does not mention AABBG (Med) https://www.asiabroadbandinc.com
  - The old AABB Wallet returns 404 on both the App Store and Google Play.
  - aabbgoldtoken.com is frozen with 2022 content. Its /aabbg/ page now shows an Indonesian gambling site, which looks like a compromised or abandoned WordPress site.
  - payaabb.com is now an unrelated site.
- Silver token pre-registration and the GoldAxis wallet were announced on 19 Feb 2026 (Med, headline only).

**(5) How the parent makes money**
- Mining and ore processing in Jalisco, Mexico, plus issuing shares.
- The token is a marketing and loyalty add-on paid for by the parent.

**(6) Verdict: SUBSIDISED BY PARENT. Confidence: Med.**
- Evidence: the token publishes no fees and no third-party custody or audit, and the old wallet, app and domains are dead or hijacked.
- Evidence: the parent is a $41M OTC miner whose stock is down 94% and which pays for growth with new shares.

---

## 3. Oropocket ORO, from Oropocket / OpenDeFi

**Not a gold token. Exclude it.**
- The ORO ERC-20 (0xc3Eb…B466) is the governance token of the "Open Finance" protocol (High).
  - Supply 98.1M, 3,531 holders, price $0.002491, on-chain value about $244K.
  - **Zero transfers in the last 24h** (High) https://etherscan.io/token/0xc3Eb2622190c57429aac3901808994443b64B466
- Its whitepaper lists no gold token, custody or fees (Med) https://openfinance.oropocket.com/llms.txt
- CoinMarketCap shows only a preview page, tagged as a DeFi/RWA token, with no gold backing (Med) https://coinmarketcap.com/currencies/oro/
- CoinGecko's "ORO" (oro-2) is an unrelated daily-claim meme token on World Chain with a $330K market cap (High) https://api.coingecko.com/api/v3/coins/oro-2

**What Oropocket actually is now:** an Indian "digital gold" app, not a token (High) https://oropocket.com
- Gold comes from Augmont and is held in Sequel vaults.
- No storage fee. The buy/sell spread is "small" and not disclosed.
- "Up to 5% Bitcoin cashback" on transactions.
- Claims "50,000+" users.
- Site disclaimer: "Digital gold is not regulated by SEBI."

**Rough sums**
- 50K users × ₹2,000–5,000 average balance ≈ ₹10–25 crore, which is **$1.1–2.9M**.
- If the net spread is 1–2% and the whole balance turns over about once a year: **$11K–58K a year** (Low; all assumptions).
- Paying up to 5% cashback could cost more than that spread earns.

**Verdict: UNKNOWN, probably promo-subsidised or founder-funded. Confidence: Low.**
- Evidence: the fees are not disclosed, while the app advertises up to 5% cashback.
- Evidence: no legal entity, funding or team is shown anywhere on the site.

---

## What this means for the margin question

**Revenue grows with assets held; costs mostly don't.**
- A custodial gold token earns on holdings: a fee per year on holdings or spreads on flows.
- Its costs are mostly fixed: vault, attestation, licence, KYC, team.
- At $2–5M of holdings (Lode, AABBG), even a 1% fee yields under $50K a year (Med).

**Rough break-even:** with fixed costs of $0.5–1M a year and a fee of 0.25–0.5% a year, a gold token needs about **$100–400M** of holdings (Low; assumption-driven). Only PAXG and XAUT are clearly above that.

**What happens below that scale:** the business closes (Lode), is carried by a parent company (AABB), or moves away from tokens to app distribution with cashback (Oropocket).

No files were written.