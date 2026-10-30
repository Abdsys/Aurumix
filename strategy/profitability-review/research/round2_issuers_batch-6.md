## Summary

| Issuer | Status (corrected) | Size today | Est. token revenue/yr | Est. cost/yr | Verdict |
|---|---|---|---|---|---|
| HSBC Gold Token (XGT) | Live. Upgraded docs Feb 2026 | Not disclosed (UNKNOWN) | ~$0.75M–7.5M (Low; scenario) | ~$1–3M incremental (Low) | **PROFITABLE at the margin, likely.** Standalone P&L UNKNOWN. Low–Med confidence |
| Meld Gold | Live but shrinking | ~$4.2M (gold ~$1.0M + silver ~$3.2M) (High, on-chain) | ~$5k–80k (Low) | ~$0.25–0.35M (Low) | **BURNING.** Med confidence |
| Zipangcoin (ZPG/ZPGAG/ZPGPT) | **Live and growing, not dormant** (High) | ~¥4.0bn ≈ $25M (30 Jun 2026) (High; USD Med) | ~$0.15–0.6M (Low) | ~$0.5–1.2M (Low) | **SUBSIDISED BY PARENT** (Mitsui & Co.). Med confidence |

**Takeaway:** the gold token only pays where a big parent already owns the customers, the vault and the metal desk (HSBC, Mitsui). A pure-play with under $10M of metal (Meld) cannot cover even a 2–3 person team. Simple breakeven: about $0.3M of fixed cost at a 0.5%/yr fee needs about $60M of AUM. At 0.25% it needs about $120M (Low).

Reference prices on 29 Oct 2026: gold $4,028.60/oz (High, https://www.kitco.com/charts/gold), silver $52.26/oz (High, https://www.kitco.com/charts/silver).

---

## 1. HSBC Gold Token (XGT), Hong Kong

**(1) Fees** (all High, from the Key Facts Statement effective 4 Feb 2026: https://www.hsbc.com.hk/content/dam/hsbc/hk/docs/investments/gold-token/key-facts-statement-v2.pdf)
- No separate fees. That covers mint, redeem, ledger fees and gift transfers.
- All revenue comes from the "Bank Margin" built into the buy and sell price:
  - Up to **2% each way** in gold trading hours (Mon 07:00 to Fri 24:00 HKT).
  - Up to **5% each way** outside those hours.
  - So the most a customer pays on a round trip is about 4% in hours and about 10% out of hours.
- No storage fee.
- 1 token = 0.001 oz of Loco London gold, about $4.03 (High). The maximum trade is 5,000 oz.
- Customers can place orders 24/7. Settlement is T+1.
- The product is an SFC-authorised "paper gold scheme". It sits on HSBC's private permissioned ledger (HSBC Orion). HK says it is neither a "virtual asset" nor a stablecoin.
- The gold is **allocated**: it is the holder's legal property. It sits in HSBC Bank plc's vault in England and Wales. Customers cannot take physical delivery.

**(2) Revenue estimate.** HSBC does not publish holdings, and XGT is absent from https://app.rwa.xyz/commodities (High). So this is a scenario, not data:
- Formula: AUM × turnover × 2 sides × realised margin. Assumptions: turnover 1x a year and 0.75% per side (Low).
- $50M AUM: $50M × 1 × 2 × 0.75% = **$0.75M**
- $200M AUM: **$3.0M**
- $500M AUM: **$7.5M**

**(3) Cost base** (Low)
- The vault belongs to an HSBC affiliate and the insurance comes under HSBC Group's policy (High, KFS). The extra custody cost is close to zero.
- The Orion platform is shared with HSBC's digital bonds, so most of the tech cost is already sunk.
- Distribution costs nothing extra: the product sells through the existing HSBC HK app and online banking.
- Main ongoing costs are product, compliance and SFC upkeep, about 5–15 shared staff, so roughly $1–3M a year (Low).
- At the mid case or above, revenue covers this.

**(4) Hard data**
- Launched 27 Mar 2024. HSBC called it the "first tokenised RWA issued by a bank for retail" (High, https://www.about.hsbc.com.hk/-/media/hong-kong/en/news-and-media/240412-introducing-hsbc-gold-token-en.pdf).
- It grew out of HSBC's institutional gold tokenisation, launched Nov 2023 (High, https://www.ledgerinsights.com/hsbc-tokenizes-gold/).
- The documents were updated in Feb 2026 to v2. They now include a gift-transfer function, which looks like a newer feature (Med).
- The HSBC group is investing more in tokenised gold: Hang Seng Investment listed a gold ETF on 29 Jan 2026 with plans to tokenise its units (Med, https://www.ledgerinsights.com/hsbcs-hang-seng-investment-to-launch-gold-etf-with-tokenized-shares/).
- No figures on holders or AUM have been published.

**(5) How the parent makes money.** HSBC earned $64.4bn revenue and $23.1bn net income in 2025 (Med, https://en.wikipedia.org/wiki/HSBC). XGT is a spread product for customers HSBC already has. It also keeps HK retail gold demand on HSBC's own book. Its economics are immaterial to the group.

**(6) Verdict: PROFITABLE at the margin (likely); standalone P&L UNKNOWN. Confidence Low–Med.**
- Evidence: a 2–5% spread with no outside custodian or customer acquisition cost covers small incremental costs at almost any volume.
- Evidence: HSBC upgraded the product in Feb 2026 instead of winding it down.

---

## 2. Meld Gold (Australia, pure-play)

**(1) Fees**
- No mint, redeem, storage or transfer fees are published (High that nothing is posted: https://www.meld.gold/tokens).
- Physical redemption goes through Imperial Bullion. The site shows fabrication premiums of **1.9–6% for gold bars**, 6–18% for silver bars and up to 100% for coins, with logistics extra. These look like charges paid to the bullion partner (High, https://www.meld.gold/convert).
- Tokens: GOLD$ and SILVER$, 1 gram each, issued on Algorand (assets 246516580 and 246519683) (High).

**(2) Size and revenue** (supply is High, read on-chain from https://mainnet-idx.algonode.cloud/v2/assets/246516580 and the issuer's reserve account on 29 Oct 2026)
- GOLD$ outstanding: 100,000,000,000 g total minus 99,999,992,178.4 g in reserve = **7,821.6 g**.
  - 7,821.6 g ÷ 31.1035 = 251.5 oz; × $4,028.6 = **$1.01M**
- SILVER$ outstanding: **1,896,212 g** = 60,965 oz; × $52.26 = **$3.19M**
- Total about **$4.2M**.
- Holders (High): 455 addresses hold at least 0.01 g of gold and 123 hold at least 1 g. The top holder has 51% of the gold float. One app-operator account holds 67% of the silver.
- Flows, measured as transfers into and out of the issuer reserve (High):
  - 2025, gold: 606 g minted, 1,375 g redeemed.
  - 2026 YTD, gold: **0 g minted, 34,918 g redeemed**, including 20,000 g and 12,136 g on 5–6 Oct 2026. Gold float fell about 82%, from about 42.7 kg to 7.8 kg.
  - Silver: 90,617 g minted and 93,570 g redeemed in 2025; 0 minted and 112,536 g redeemed in 2026.
- Revenue assumptions: a 0.5–1% fee on flows plus at most 0.5% a year on AUM (Low).
  - 2025 flows were about $440k, which gives $2–4k.
  - 2026 flows were about $5M, which gives $25–50k, almost all of it one-off exit fees.
  - A custody fee would add $20–30k.
  - Total: **about $5k–80k a year** (Low).

**(3) Cost base**
- The site names a CEO (Michael Cotton) and a CTO (Dominic Hawton), plus one advisor (High, https://www.meld.gold/about). Two salaries come to about US$200–260k (Low).
- Vaults at Imperial Vaults Brisbane and MKS PAMP Geneva: about $4–12k for roughly $4M of metal (Low).
- BDO is listed as a partner, so an audit or attestation would cost about $15–40k (Low).
- Infrastructure and legal: about $20–50k (Low).
- Total about **$0.25–0.35M**. Revenue covers roughly 2–30% of it.

**(4) Hard data and red flags**
- No published financials, funding amounts or licence numbers (AFSL or AUSTRAC) (High, https://www.meld.gold/contact). Apollo Capital is listed as a partner/investor (Med).
- **Attestation gap:** the "Live Audit" page shows "Loading" for Algorand and "Coming Soon" for XRPL. No holdings, auditor or date are shown (High, https://www.meld.gold/audit).
- The XRPL launch announced in 2024 does not appear to be live (Med).
- Meld is not tracked on CoinGecko, CMC or rwa.xyz (High).
- Large holders are leaving in 2026 (High, on-chain).

**(5) Parent:** none. Pure-play, so nothing cross-subsidises it.

**(6) Verdict: BURNING (or a founder/investor-funded zombie). Confidence Med.**
- Evidence: about $4.2M of float, with no mints and about $5M of redemptions in 2026. At any normal fee rate, that cannot pay even two salaries.
- Evidence: there has been no live attestation since at least the current site version.

---

## 3. Zipangcoin (ZPG), Mitsui & Co. Digital Commodities, Japan

**Correction:** ZPG is **live and expanding**.
- The bare domain zipangcoin.com fails, but https://www.zipangcoin.com/au/ and https://www.mitsuidc.com/ both work (High).
- The issuer files quarterly disclosures. The latest is dated 15 Jul 2026 and covers data to 30 Jun 2026.

**(1) Fees** (High, whitepaper v12.0.0 dated 31 Aug 2026: https://www.zipangcoin.com/pdf/zpg_whitepaper.pdf, plus the FAQ at https://www.zipangcoin.com/au/)
- 1 ZPG = 1 g of gold, priced in yen.
- Price = London OTC gold price plus a spread that **each exchange sets itself**. The spread level is not disclosed.
- **No storage fee.**
- No physical redemption.
- Transfers are restricted to whitelisted addresses.
- Silver (ZPGAG) and platinum (ZPGPT) launched Jul 2023 on the same terms.

**(2) Size and revenue** (issuer disclosures, High)

| Date | ZPG gold (g) | ZPGAG silver (g) | ZPGPT platinum (g) | Total value |
|---|---|---|---|---|
| Dec 2022 | 29,410 | – | – | ~¥0.24bn |
| Dec 2023 | 47,706 | 28,800 | 214 | ~¥0.5bn |
| Dec 2024 | 96,187 | 389,900 | 10,068 | ~¥1.4bn |
| Dec 2025 | 141,745 | 1,638,200 | 34,685 | ~¥3.0bn |
| Mar 2026 | 147,832 | 2,374,700 | 35,180 | ~¥3.8bn |
| Jun 2026 | **143,623** | 2,240,800 | 33,401 | **~¥4.0bn** |

- Sources: Jun 2026 https://f339c3a6-c614-4372-9442-136f2257cd07.usrfiles.com/ugd/dbc4cc_9e53e42d9d56479b8c470c69319b00ca.pdf, Dec 2025 …/dbc4cc_adf1a7856da54a13944586542ea49a42.pdf, Dec 2024 …/dbc4cc_873f6de02cea440caa37a2e70f239287.pdf.
- In USD at today's spot: gold 4,617.6 oz × $4,028.6 = **$18.6M**; silver 72,043 oz × $52.26 = **$3.8M**; platinum about $2.5M (paid-in used as a proxy). Total about **$25M** (Med).
- Q2 2026 was a small net outflow: gold down 4,209 g (−2.8%) (High).
- How MDC earns (High, whitepaper):
  - Money from token buyers is used to buy gold **from Mitsui & Co.**
  - That gold is then **leased straight back to Mitsui & Co.**, which uses it in the gold market.
  - MDC earns (a) a trading margin on issuance and buybacks and (b) **lease income**.
- Lease income: about $25M × 0.5–2% = **$0.12–0.5M** (rate is Low).
- Trading margin:
  - Cumulative paid-in rose from ¥2.95bn to ¥3.96bn in H1 2026, which works out to about ¥2bn (about $13M) of gross subscriptions a year.
  - Paid-in appears to be cumulative gross, since it rose while grams fell (Med).
  - At a 0.2–0.5% margin, that is **$26–65k**.
- Total **about $0.15–0.6M a year** (Low). The exchanges, not MDC, keep the retail spread.

**(3) Cost base**
- Capital is ¥167.6M (High).
- Officers are Mitsui & Co. staff. MDC uses Mitsui's existing metal-trading infrastructure (High, whitepaper).
- Vault cost to MDC is effectively zero because the metal is leased to Mitsui.
- Main costs (all Low):
  - Bank guarantee on about ¥4bn at 0.3–0.5%: about $75–125k.
  - Fireblocks, miyabi and OP infrastructure: $0.1–0.3M.
  - 3–6 staff: $0.25–0.6M.
  - Legal and JVCEA: $50–150k.
- Total **about $0.5–1.2M**. That is probably more than standalone revenue.

**(4) Hard data**
- Listed on 8 Japanese exchanges, all with dates (High, whitepaper):
  - DAMS (Feb 2022)
  - bitFlyer (Dec 2022)
  - Mercury/CoinTrade (Mar 2024)
  - SBI VC Trade (May 2024)
  - Zaif (Dec 2024)
  - BitTrade (Mar 2025)
  - GMO Coin (Apr 2026)
  - Coincheck (Aug 2026)
- Multi-chain launch on 17 Apr 2026 on OP Mainnet via Fireblocks, with Solana planned (High, https://f339c3a6-c614-4372-9442-136f2257cd07.usrfiles.com/ugd/dbc4cc_f5565164e2304f2dbb8287d370ac8ad2.pdf). Only 3,754 ZPG is on OP Mainnet so far; most of the supply is still on the private miyabi chain (High, on-chain).
- Targets keep rising: ¥2bn, then ¥4.5bn, now **¥13.4bn by Mar 2029** against about ¥4.0bn today, so about 30% of target (High). The issuance cap is ¥39bn.
- If MDC fails, a bank guarantee pays holders the market value, held in a trust account (High).

**(5) How the parent makes money.** Mitsui & Co. earned ¥834bn net income in FY to Mar 2026 (Med, https://en.wikipedia.org/wiki/Mitsui_%26_Co.). Mitsui gets leased metal funded by retail buyers for its trading book, plus a strategic digital-commodities position. That is the cross-subsidy.

**(6) Verdict: SUBSIDISED BY PARENT. Confidence Med.**
- Evidence: about $25M of metal earns MDC only a lease spread plus a thin margin, against a staffed, bank-guaranteed, multi-chain operation.
- Evidence: the business keeps expanding (8 exchanges, new chains, 3x target), which only makes sense as a Mitsui strategic and funding play.

---

**Limits of this check**
- The web-search budget was used up partway through. Everything above comes from direct fetches of issuer documents and on-chain reads.
- I found no LinkedIn headcounts and no 2025–26 press figures for HSBC XGT volumes.
- The USD/JPY rate available to me was stale (about ¥158), so I valued ZPG mainly from metal quantities at today's spot prices.