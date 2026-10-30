**Verdict up front:** None of the three makes money from the gold token alone. Two are kept alive by a parent company. One is a listed pure-play that is clearly burning cash.

Confidence tags: (H) high, (M) medium, (L) low. WebSearch was out of budget for this run, so everything below comes from pages fetched directly: issuer docs, rwa.xyz, CoinGecko and SEC EDGAR.

---

## Summary table

| Issuer | Market cap | Fees it actually charges | Est. revenue/yr from the token | Est. cost/yr | Verdict | Conf. |
|---|---|---|---|---|---|---|
| Pleasing Gold (PGOLD) | $79M (H) | 0% mint, 0% management. 0.5% on physical redemption only, and that fee goes to stakers | About $0 kept by Pleasing (M) | $0.1M+ (L) | SUBSIDISED BY PARENT | Low–Med |
| Matrixdock (XAUm) | $70M (H) | Mint fee waived until $100M TVL. 0% management. 0.25% redemption | $0.07–0.13M (L) | $1–2.5M (L) | SUBSIDISED BY PARENT | Med |
| Streamex (GLDY) | $12.4–13.7M (H) | 0.25% subscription, 2% redemption, +4% for physical, 0% management | About $0.6M, mostly lease income on its own gold (M) | About $13M cash burn (H) | BURNING | High |

---

## 1. Pleasing Gold (PGOLD): Pleasing International, Hong Kong

**(1) Fees**
- 0% management, 0% subscription, 0.50% redemption (H). Source: https://app.rwa.xyz/assets/PGOLD
- The redemption fee applies only when someone takes physical gold. It "is redistributed back to PGOLD stakers," so Pleasing keeps none of it (H). Source: https://pleasing.gitbook.io/docs/tokenized-gold-pgold/how-pgold-works.md
- Minimum physical redemption is 32.15 PGOLD, which is one 1 kg bar, collected in Hong Kong (H). Source: https://pleasing.gitbook.io/docs/user-guide/redeem-physical-gold.md
- The terms point to a "Fee Schedule" for mint, redeem and handling fees. That schedule is not published (H). Source: https://pleasing.gitbook.io/docs/legal/terms-of-sale-and-service.md

**(2) Revenue estimate**
- Supply has stayed at 19,505 PGOLD (H). In the last 30 days there were 9 active addresses, 240 transfers and **$167 of transfer volume** (H, rwa.xyz). There were 419–427 holders (H; https://arbiscan.io/token/0x3e76BB02286BFeAA89DD35f11253f2CbCE634F91). 24h exchange volume was $0 (H; https://www.coingecko.com/en/coins/pleasing-gold).
- Example: if 10% of supply were redeemed physically in a year, the fee would be 1,950 oz × $4,030 × 0.5% = **$39K**. That money goes to stakers, so Pleasing keeps **about $0** (M).
- Primary mint and redeem spread: not disclosed (L).

**(3) Cost base**
- Vaulting about $79M of gold in Hong Kong at 0.05–0.12% a year comes to **$40–95K** (L, industry rate assumption). If this is the dealer's own stock, it pays that cost anyway.
- Other costs: smart-contract audits (Beosin is a listed partner), Chainlink price feed, LayerZero and Arbitrum deployment. Team size is unknown.
- PGOLD staking pays rewards in PGOLD. The APY is not published and the docs do not say who funds it (H that it is undisclosed; https://pleasing.gitbook.io/docs/user-guide/pgold-staking.md). This could be a hidden cost.
- Revenue cannot cover even vault costs. The token is a cost centre.

**(4) Hard data and red flags**
- I found no third-party gold reserve attestation. The "audit report" and "reserve report" pages are only file embeds I could not read. The proof-of-reserve page covers only USDpm, is self-reported, and says reserves are "exclusively TRC20 USDT on TRON" (H; https://pleasing.gitbook.io/docs/precious-metal-usd-usdpm/proof-of-reserve.md).
- The token contract is an upgradeable proxy (EIP-1967), so the admin can change it (H, Arbiscan).
- No funding round or financial statements were found. The custodian is "log in to unlock" on rwa.xyz (H).
- The $79M market cap is supply × spot price. Almost nothing trades. It is most likely the dealer's own inventory, or a few large holders, wrapped as a token (M).

**(5) How the parent makes money**
- **Dealer business:** physical metal spreads. No numbers are published (L).
- **USDpm, a synthetic dollar:** it takes in USDT/USDC to finance metals inventory for "operators" (vaults, refiners, dealers). It targets a 6–10% APR, paid from operators' "fees/spreads/financing income" (H; https://pleasing.gitbook.io/docs/precious-metal-usd-usdpm/how-usdpm-works.md). In effect this is cheap inventory finance for the dealer.
- **Tokenization-as-a-Service:** setup fees, mint/burn "flow fees" and revenue share (H; https://pleasing.gitbook.io/docs/solutions/tokenization-as-a-service-taas.md). No clients are disclosed.

**(6) Verdict: SUBSIDISED BY PARENT (Low–Med)**
- The token charges 0% and passes its one fee to stakers. Supply is flat and there is $167 of monthly transfer volume.
- PGOLD is a shop window and collateral wrapper for a dealer whose finances nobody can see. Whether the whole group burns cash is UNKNOWN.

---

## 2. Matrixdock Gold (XAUm): Matrixport group, now rebranded "BIT"

**(1) Fees**
- **Mint fee "waived until TVL reaches $100 million"** (H as published, M that it still applies because the FAQ is undated). Redemption is **0.25%** per order. There is **no management or storage fee**, though they may add one with 30 days' notice. Transfers are free (H). Source: https://matrixdock.gitbook.io/matrixdock-docs/english/gold-token-xaum/faq.md
- Quoted mint price was $4,048.40 and redeem price $4,017.80. That is about a **0.76% round trip**, which includes the 0.25% fee and "currency fees" (M; https://www.matrixdock.com/xaum).
- Minimum investment is $10K. Physical redemption needs at least 32.148 XAUm (1 kg). Non-US investors only (H; https://app.rwa.xyz/assets/XAUm, https://matrixdock.gitbook.io/matrixdock-docs/english/gold-token-xaum/minting-and-redeeming.md).

**(2) Revenue estimate**
- **Supply:** 17,360 XAUm across 540 bars (H, Oct 2026; matrixdock.com). It was 16,331 oz across 508 bars in July 2026 (H; https://www.manilatimes.net/2026/07/21/tmt-newswire/pr-newswire/reserve-transparency-built-through-continuous-operation-matrixdock-marks-two-years-of-independent-verification/2388158), and about 482 bars (≈15,500 oz) at the H2 2025 audit (M). Net growth is about 2,500 oz a year (M).
- **Assumed gross flows:** mints of 4,000–6,000 oz a year ($16–24M) and redemptions of 1,500–3,500 oz ($6–14M) (L).
  - Mint fee: $0.
  - Redemption fee: 0.25% × $6–14M = **$15–35K**.
  - Spread beyond the stated fee, about 0.25% a side × $22–38M = **$55–95K**. Part of this only covers the cost of sourcing bars and FX (L).
  - **Total: about $70–130K a year (L).**
- Secondary trading earns Matrixdock nothing because transfers are free. KuCoin XAUM/USDT did about $451K in 24h, out of $513K total (H; https://www.coingecko.com/en/coins/matrixdock-gold).
- Benchmark: even a 0.25% management fee on $70M would bring in only $175K a year.

**(3) Cost base**
- Brink's HK/SG and Malca-Amit SG vaults: 0.08–0.15% × $70M = **$55–105K** (L). Brink's insurance of up to $50M is included (H; https://matrixdock.gitbook.io/matrixdock-docs/english/gold-token-xaum/physical-gold-custody.md).
- Bureau Veritas audits twice a year: about $20–50K (L).
- Appleby trustee and Hamilton enforcer: about $30–80K (L).
- Deployment on 6+ chains (Ethereum, BNB, Solana, Sui, Stellar, Plume), plus integrations and audits: about $50–150K (L).
- Staff: assume 5–10 FTE shared with STBT in Singapore/Hong Kong, about **$0.8–2M** (L).
- 65,243 holders, falling (H, rwa.xyz). That count points to airdrop or campaign marketing, cost unknown (L).
- **Total about $1–2.5M a year against about $0.1M of revenue (L).** Revenue does not cover cost.

**(4) Hard data and red flags**
- Reserves are clean. Bureau Veritas has done four audits in a row and the last matched 16,331.184 oz to 16,331.179 tokens (H).
- Market cap is down about 3% over 30 days (H, rwa.xyz).
- Matrixdock's T-bill token STBT has shrunk to **$15.5M** with 39 holders. At a 0.30% management fee that earns **$46.5K a year** (H arithmetic; https://app.rwa.xyz/assets/STBT). Total Matrixdock distributed value is $70.7M (H; https://app.rwa.xyz/platforms/matrixdock).
- Matrixdock has dropped XAUm support on Polygon, HashKey Chain and Tron, which looks like cost trimming (M; docs announcements index).
- Matrixport history: about $100M Series C at more than $1B in 2021, and staff cuts in 2022. **I did not re-check this in this session (L).**

**(5) How the parent makes money**
- matrixport.com now redirects to bit.com, "Formerly Matrixport." It reports **$6B+ assets under custody and management and $7B+ monthly trading volume** (H; https://www.bit.com/about).
- Its income comes from trading, structured products, lending, Cactus Custody and its funds.
- XAUm is a collateral product and a way to win customers. The gold line is too small to matter in the group's numbers.

**(6) Verdict: SUBSIDISED BY PARENT (Med)**
- The mint fee is waived and there is no management fee, so $70M of gold brings in an estimated $0.1M a year. The audits, vaults and team are paid for by a group with $6B+ in assets.

---

## 3. Streamex Gold Yield (GLDY): Streamex Corp (Nasdaq: STEX)

**(1) Fees**
- 0.25% subscription. **2.00% redemption**, quarterly, with a $163K minimum. **+4% for physical**. 0% management and performance fees. $25K minimum subscription. Accredited and professional investors only (H; https://app.rwa.xyz/assets/GLDY).
- Streamex also gets a share of Orca pool protocol fees and GLDY transfer fees (H; SEC 8-K 2026-05-27, https://www.sec.gov/Archives/edgar/data/1530766/000149315226025606/0001493152-26-025606.txt).
- Target yield is about 3.5%, paid in gold, from Monetary Metals' leasing programme (H; https://www.streamex.com/products/gldy/).

**(2) Revenue estimate**
- **Reported revenue:** Q2 2026 revenue was **$146K, all "gold lease income," from a single counterparty**. It was "immaterial" and the company's first revenue (H; 10-Q, https://www.sec.gov/Archives/edgar/data/1530766/000149315226038293/form10-q.htm). Annualised that is about **$0.58M** (M).
- That income is mostly lease yield on **Streamex's own gold**. The 10-Q says the company "holds a significant ownership interest in Streamex Ltd. in the form of GLDY tokens" and plans to sell some of it (H). It holds $15.5M of gold at cost (H).
- **Third-party fee income:** GLDY has only 24 holders and 3,361 tokens (H). If $3–8M belongs to outsiders (L):
  - Subscription fee: 0.25% × $3–8M = **$8–20K, one-off**.
  - Lease spread of about 0.5% (assumes ~4% gross vs 3.5% paid) × $13M = **about $65K a year** (L).
- **Total about $0.6–0.7M a year (M).**

**(3) Cost base**
- Q2 2026 G&A was **$13.8M**, including $3.2M of stock compensation. H1 2026 G&A was $48.1M (H, 10-Q).
- The company says operating cash burn was **$1.6M a month in Q2**, including $0.5M of one-offs, and guides to **$1.1M a month in Q3** (H; https://www.sec.gov/Archives/edgar/data/1530766/000149315226039547/0001493152-26-039547.txt). That is about **$13M a year**.
- GAAP operating cash flow in Q2 was -$11.7M (M; https://stockanalysis.com/stocks/stex/financials/?p=quarterly&type=cash-flow-statement). This is much more than the company's own burn figure, and I did not resolve the gap.
- Headcount is 6 full-time staff plus 4 consultants (H; 10-K, https://www.sec.gov/Archives/edgar/data/1530766/000149315226014376/form10-k.htm).
- Service providers: Asahi Refining USA (custodian), Anchorage (crypto custody), EisnerAmper (auditor) (H, rwa.xyz).
- **Revenue covers about 4–5% of cash burn.**

**(4) Hard data and red flags**
- **Losses:** net loss of $500.9M over the last 12 months, mostly non-cash. Q4 2025 alone was -$424M, cause not confirmed. H1 2026 net loss was $61.2M (H).
- **Liquidity at 30 June 2026:** $41.8M total, made up of $18.5M cash and securities, $6.0M USDC and $15.5M physical gold (H). The company sold $26.4M of gold in H1. It also raised $37.2M of equity in January 2026 and paid off $38.9M of convertible debt (H).
- **Runway:** about 2 years at the guided burn if gold is excluded, about 3 years if the gold is sold. That gold is GLDY backing, so selling it shrinks the product.
- **Financing:** the $1B standby equity facility was **terminated in January 2026 with no draws** (H, 10-K).
- **Share price:** $0.41, down 91.5% over 52 weeks. Share count is up 789% year on year (H; https://stockanalysis.com/stocks/stex/statistics/).
- **Nasdaq:** a minimum bid price deficiency notice on 2026-10-09, with a deadline of 2027-04-05 (H; https://www.sec.gov/Archives/edgar/data/1530766/000149315226046604/form8-k.htm).
- **Governance:** the Interim Executive Chairman resigned on 2026-09-30 (H). The auditor changed in July 2026 (8-K Item 4.01) (H).
- **Product:** GLDY CIMA registration is still pending (H). CoinGecko says GLDY "stopped trading on all exchanges" (H; https://www.coingecko.com/en/coins/streamex-gldy).
- **Counterparty risk:** all yield depends on one party, Monetary Metals, and the gold may be commingled with other lessors' gold (H, 10-K).

**(5) How the parent makes money**
- It is a pure play with no other business. The old BioSig medical-device shell has been effectively replaced.
- Losses are funded by equity raises and by selling its gold.

**(6) Verdict: BURNING (High)**
- Q2 2026 revenue was $146K against $13.8M of G&A and about $1.1–1.6M a month of cash burn. The stock is down 91%, there is a Nasdaq deficiency notice, and the GLDY holder base is mostly the company itself.

---

## What this means for the "from scratch" question

- **The fees are too small.** All three charge 0% management, and two of them waive or skip the mint fee. At $10–80M of AUM, even a 0.25–0.4% all-in take rate earns only $25–320K a year.
- **Break-even needs scale.** With a minimum cost base of about $1–1.5M a year (vault, audit, trustee, legal, chains, a small team) and a 0.3–0.4% take rate, a gold token needs roughly **$250–500M AUM** to break even (L–M). None of these three is close.
- **Who survives:**
  - Players with a profitable parent that uses the token to win customers or as collateral (Matrixdock, Pleasing).
  - Players that make money from what the gold does (financing, leasing) rather than from holding it. Streamex tried this, but its corporate overhead swamps the lease spread.
- **Data gaps:**
  - Pleasing: the fee schedule, reserve attestation and parent financials are all missing.
  - Matrixdock: gross mint and redeem flows and team size are missing, and its cost lines are estimates.
  - Streamex: the cause of the Q4 2025 loss, and the gap between GAAP cash flow and the company's own burn figure, are unresolved.