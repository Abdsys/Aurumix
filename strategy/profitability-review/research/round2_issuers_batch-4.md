**Short answer:** none of the three small gold tokens earns enough from its own fees to pay its costs. Kinka has already been shut down by its parent because it lost money. Comtech Gold is shrinking fast and looks like it is losing money. Herculis is new and is almost certainly being paid for by its parent group.

Web search was used up for this session, so everything below comes from primary sources: the issuers' own sites, PDFs and code, on-chain supply reads, CoinGecko's price history and a Tokyo Stock Exchange filing. I did not check LinkedIn headcounts.

| Token | Gold behind it today | Token revenue per year (estimate) | Cost per year (estimate) | Verdict |
|---|---|---|---|---|
| Comtech Gold (CGO) | 24,000 g, about $3.1M (High) | One-off $65–140K in the last 12 months. Under $30K a year going forward (Low) | $0.4–0.7M (Low) | **BURNING**, Medium confidence |
| Herculis Gold Coin (XAUH) | 15.5 kg, about $2.0M (High) | $10–75K to date (Low) | $0.25–0.6M (Low) | **SUBSIDISED BY PARENT**, Medium-Low confidence |
| Kinka (XNK) | 482 oz, about $1.9M (High) | Filed revenue of about $170 in FY3/2026 (High) | Filed loss of about $40K, with more cost carried by the parent (High) | **SHUT DOWN** (it was burning and parent-funded), High confidence |

---

## 1. Comtech Gold (CGO): UAE

**Fees** (from the cgold.ae fee table, https://cgold.ae/):
- Mint ("transaction fee"): none (High).
- Custody and insurance: none for the first 24 months, then a "nominal fee" (High; [FAQ PDF](https://cgold.ae/assets/pdf/ComTech_Gold_FAQ_Final.pdf)).
- Transfer: 0.50% (High).
- Physical redemption: 0.50%, with a 1 kg minimum (High; [T&C, 23 Aug 2022](https://cgold.ae/assets/pdf/Terms_and_Conditions.pdf)).
- Spread: in-app buy and sell is spot price plus a "nominal commission". The amount is not published.
- The 0.50% transfer fee is not built into the token itself. The contract on the XDC chain is a plain token with mint, burn and blacklist functions and no fee code (Med; [contract code](https://xdcscan.com/address/0x8f9920283470f52128bf11b0c14e798be704fd15#code)). So the $860K a day of trading on Bitrue and LBank earns the issuer nothing (Med).

**Hard facts:**
- **Supply fell 78% in 2026.** It went from about 108,000 g to 69,000 g (17–22 Feb), then 39,000 g (18 Mar), then 24,000 g (4 Aug) (High; [CoinGecko 1-year history](https://api.coingecko.com/api/v3/coins/comtech-gold/market_chart?vs_currency=usd&days=365) and [XDCScan: 24,000 supply, 477 holders](https://xdcscan.com/token/0x8f9920283470f52128bf11b0c14e798be704fd15)). The drop came while gold was near its high of $166/g. That points to large holders cashing out.
- **CoinMarketCap's 141,000 supply is out of date.** It matches the 144 kg in the March 2025 vault report. The real on-chain supply is 24,000 (High).
- **The main site is closed.** comtechgold.com shows "Site Under Maintenance" and sends visitors to cgold.ae, a retail "Digital Gold" app with coin delivery, gifting and promotions (High). That suggests a shift toward selling gold through an app.
- **Reserve reports are thin.** The only one posted is a DMCC Tradeflow screenshot dated 21 Mar 2025: 144 kg under warrant, worth AED 31.67M (High; [Routine_audit.pdf](https://cgold.ae/assets/pdf/Routine_audit.pdf)). Nothing has been posted since the supply fell. cgold.ae also shows "Current gold supply: 3,000 g", which does not match the chain (Low; unexplained).
- **Shariah certificate:** a new fatwa from Sabiq dated 31 Mar 2026 is linked on the site (High). Your notes listed Amanie, so this is a change.
- **Licences:** DAFZA and DMCC (ComTech FZCO). No VARA licence is shown (Med). The vault is Transguard (Med; FAQ PDF).

**Revenue estimate:**
- About 84,000 g left the token (108k − 24k). At roughly $150/g that is about $12.6M (Med).
- If all of it was redeemed for physical gold at 0.50%, the fee was about $63K. If it was sold back to the issuer at an assumed 1% spread, about $126K. Either way it was a one-off (Low).
- Minting earned nothing: there is no mint fee and supply did not grow (Med).
- Custody earns nothing now. Even an assumed 0.5% a year on $3.1M would be about $15.5K a year (Low).

**Cost estimate:**
- Five people are named on the site: Founder & CEO Jignesh Ved, COO Ritika Bhardwaj, Chief Advisor Lim Say Cheong, a marketing specialist and an admin executive. At $60–100K each, that is $300–500K a year (Low).
- Vault and insurance: $3–30K (Low).
- Licences, the JLT office, the fatwa, the CertiK review and exchange listing or market making: about $100–200K (Low).
- **Total: about $0.4–0.7M a year against at most about $0.14M of revenue.**

**Who pays:** no parent company is disclosed, so the founders or investors cover the shortfall (Low).

**Verdict: BURNING, Medium confidence.** Supply is down 78% in 2026 and the token charges no mint or custody fees. The main site is closed and the last reserve report is from March 2025.

---

## 2. Herculis Gold Coin (XAUH): Panama issuer, gold held in Switzerland

**Issuer:** Herculis Tokens SA in Panama City. It reports to Panama's Financial Analysis Unit (UAF), which is an anti-money-laundering registration and not a licence. It belongs to the Herculis Group, a Swiss investment boutique founded in 2009 (High; [llms-full.txt](https://xauh.gold/llms-full.txt), [whitepaper v4.0, 21 May 2026](https://xauh.gold/whitepaper.pdf)).

**Fees** ([T&C v1.1, effective 24 Sep 2026](https://xauh.gold/xauh-terms-and-conditions.pdf)):
- Mint: 0.30%, for institutions tokenizing their own bars.
- Redemption: 1% for 1 kg or more, 3% for 500 g, plus delivery. The minimum is 500 g.
- Custody and insurance: none.
- Transfer: 0.02%, only on the JAMTON protocol.
- Buying gold directly: 2% for 1 kg or more, 3% below that.
- Retail buyers come through Wert (card), ChangeNOW and Changelly. The markup on those routes is not published.

**Hard facts:**
- **Gold held, from KPMG reports:** 3.5 kg (14 Jan 2026), 11.5 kg (11 May), 15.5 kg (26 Aug) (High; [Jan](https://xauh.gold/audit-reports/01-21-2026.pdf), [May](https://xauh.gold/audit-reports/05-13-2026.pdf), [Aug](https://xauh.gold/audit-reports/08-28-2026.pdf)). That is about 12 kg of new gold in 7.5 months.
- **Weak spots in the KPMG reports** (High):
  - They are agreed-upon-procedures reports. KPMG states it gives "no assurance".
  - The gold is owned "by one entity of the group". It is not shown as held for token holders.
  - For 10 of the 18 bars, the invoices could not be linked to the bars.
  - The reports never compare the gold to the token supply.
  - The T&C also hedge on whether the gold is truly segregated.
- **On-chain supply is lower than claimed.** I found 10,509 XAUH: 4,049.2 on Ethereum, 3,290.4 on TON (504 holders) and 3,169.4 on TRON. CoinGecko shows 15,500 (Med; [TON](https://tonapi.io/v2/jettons/EQCMk4_OujCnk46jApHnIRbmTtYTkSmfujV9X8Ye0qvsHVKh), ETH and TRON read directly; I assumed TRON uses 18 decimals). The rest may sit on the JAMTON chain or not be issued yet.
- **It is very new.** CoinGecko data starts on 25 Aug 2026 (High; [CoinGecko](https://www.coingecko.com/en/coins/herculis-gold-coin)). About $150K a day trades, 78% of it on Biconomy, which is a low-tier exchange.
- There are no public financial filings, since it is a private Panama company.

**Revenue estimate:**
- About 15.5 kg sold × about $140/g ≈ $2.17M of gold (Med).
- At the 0.3% mint fee, that is about $6.5K. At an assumed 2–3% retail markup, about $43–65K (Low).
- The transfer fee is capped at about $11K a year ($152K × 365 × 0.02%). That assumes all trading runs on JAMTON, which it does not, since exchange trades pay nothing (Low).
- There have been no redemptions; supply has only grown.
- **Total to date: about $10–75K.**

**Cost estimate:**
- Four KPMG reports in 2026.
- A Swiss vault (named as Herculis House, Brinks or Loomis) and insurance.
- Listings on BTSE and Biconomy, and integrations with Wert, ChangeNOW and x402.
- Marketing across seven social channels.
- **Total: about $250–600K a year (Low).** The team size is not disclosed.

**Verdict: SUBSIDISED BY PARENT (early stage), Medium-Low confidence.** It charges no custody fee on $2M of gold, so fee income is tiny against KPMG, vault and listing costs. The gold is booked as a group asset.

---

## 3. Kinka (XNK): Japan. Being closed now.

**Issuer:** Kinka (BVI) Ltd, 100% owned by unbanked Inc. (TSE Standard 8746), the former Daiichi Commodities. The filing names no Crowdbank entity (High).

**Fees** ([whitepaper v2](https://kinka-gold.com/wp-content/uploads/2024/01/Kinka_white-paper_ver2.pdf)):
- No custody fee, no management fee, and no transaction fee beyond gas.
- Physical redemption has a fee that varies by location, with a minimum of 321.5 XNK (10 kg) (High).

**Hard facts, from the [TSE filing of 16 Oct 2026](https://tdnet-pdf.kabutan.jp/20261016/140120261016552360.pdf)** (High):
- The board decided to close the crypto business and wind up three subsidiaries by Mar 2027.
- The buyback and gold-exchange deadline is **30 Oct 2026**. All tokens bought back will then be burned. Kinka was delisted from BitMart (26 Aug) and CoinW (24 Aug) ([kinka-gold.com](https://kinka-gold.com/)).
- **Kinka (BVI) results** (yen, converted at about ¥150/$):

  | | FY3/2024 | FY3/2025 | FY3/2026 |
  |---|---|---|---|
  | Revenue | ¥9K | ¥725K (~$4.8K) | ¥26K (~$170) |
  | Operating loss | −¥17.9M (~$119K) | −¥7.4M | −¥5.9M (~$40K) |
  | Net assets | | | −¥31.0M |

- The losses are understated. A parent employee runs the subsidiary, and the parent does its accounting and website work.
- Kinka sales were under 0.1% of the parent's ¥8,043M gold segment, so under about ¥8M.
- **The company's stated reasons:**
  - Sales stayed weak because "the leading competitor products had an overwhelming share".
  - The planned exchanges would not handle the USDA stablecoin used to buy the Cardano version.
  - Selling on decentralized exchanges carried legal risk.
  - The new management, in place from 30 Sep 2026, judged it "difficult to secure profitability".
- The 167 XNK on Cardano were **never sold** and will be burned. Real public demand was at most the 315 XNK on Ethereum, about $1.26M (High; on-chain read).
- **The parent is losing money too.** unbanked FY3/2026: revenue ¥9,394M (about $63M), operating loss −¥2,792M, net loss −¥3,808M. Market cap is ¥1.78B, about $11M (High; [Kabutan](https://kabutan.jp/stock/finance?code=8746)). Kinka is not the main cause; its subsidiary lost only ¥5.9M.

**Verdict: SHUT DOWN (BURNING, and funded by the parent until it closed), High confidence.** The filed accounts show revenue of about $170 against a loss of about $40K, and the parent's own filing says it could not be made profitable.

---

## What this means for Aurumix
- **None of these three can live on fees.** All three charge nothing for custody. Their only income is mint, redemption or spread fees, and those only come in when money moves in or out.
- **The scale needed is out of reach.** As an illustration: covering a $0.5M cost base with a 0.25% yearly fee needs about $200M of gold. These three each hold $2–3M (Low; my own illustration).
- **Kinka's own filing names the problem.** Two big players dominate the market, and a small token cannot win distribution. That is the same conclusion as in your earlier notes: whoever owns the customer makes the money.