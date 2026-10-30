# Gold-token issuers: can they sustain margins?

All three issuers are small, and none of them covers its costs from the gold token alone. Gold DAO's own paper gives the clearest numbers: fee revenue covered about one fifth of its basic running costs, and two partner companies paid the rest.

Gold price used below: about $4,030/oz today (High; implied by [ONSG](https://api.coingecko.com/api/v3/coins/token-teknoloji-a-s-ons-gold) at $4,034.59 and [TGLD](https://www.coingecko.com/en/coins/tenbin-gold) at $4,032). ONSG's all-time high was $5,718 on 2026-03-03, so gold looks about 29% below its March peak (Med; based on token prices, not a gold benchmark). A lower gold price shrinks any fee charged on assets held.

## 1. Gold DAO / GLDT (ICP; gold in a Zurich vault)

**Status:** live, but wound down as a DAO product.
- The docs now say ["GLDT has been merged into ORIGYN"](https://docs.gold-dao.org/tokens/gldt.md) and ["GLDT staking has been discontinued"](https://docs.gold-dao.org/resources/gldt-staking.md) (High).
- The roadmap planned to "hand over GLDT related canisters to ORIGYN" in Q1 2026 ([roadmap](https://docs.gold-dao.org/resources/roadmap.md), High).
- Bity, DEF (Cecil) and ORIGYN merged their teams into "ORIGYN Venture" to cut costs ([Chapter 2.0 PDF](https://fjdhj-uyaaa-aaaai-q4fma-cai.icp0.io/GoldDAO_Chapter2.0.pdf), High).
- The last code commit, on 2026-10-27, was titled "retire token_metrics and super_stats canisters" ([repo](https://github.com/GoldDAO/gold-dao), High).

**(1) Fees**

| Fee | Amount | Source |
|---|---|---|
| Ledger transfer | 0.1 GLDT, about $0.13 | [ICRC ledger API](https://icrc-api.internetcomputer.org/api/v1/ledgers/6c7su-kiaaa-aaaar-qaira-cai), High |
| Swap GLDT back to a gold NFT | 1 GLDT, about $1.30 | `REVERSE_GLDT_TX_FEE` in [repo](https://github.com/GoldDAO/gold-dao), High |
| Swap NFT to GLDT | Not found | — |
| Storage | None charged to holders found | Med |
| Gold purchase markup | Bity earns a 2.5% gross margin on selling the gold | Chapter 2.0 PDF, High |
| Physical redemption | Handled by Bity support; fee not published | [redeem page](https://docs.gold-dao.org/how-to/redeem-physical-gold.md), Med |

Fees are sent to buy back and burn the GOLDAO token. The code job is named `TRANSFER_FEES_FOR_BUYBACK_BURN`. So fee income did not go toward running costs (High).

**(2) Revenue**
- GLDT supply is 593,400 GLDT, which is 5.93 kg of gold, about $771K (High, ledger API).
- The team's own disclosure: "with about USD 1 million in gold in circulation… the fees generate USD 1,000 per month". That is about $12K a year, or roughly 1.2% of the gold held (High, PDF).
- Cross-check: $12K ÷ $0.13 per transfer is about 92K transfers a year, or about 250 a day. Today the DEX trades about $2.6K a day, so current revenue is probably $5–12K a year (Low).
- Bity's 2.5% markup on gold sales is one-off income. On about $771K of gold that is about $19K (Med).

**(3) Costs**
- Gold sits at Loomis in Zurich, with KPMG checking the vault on site every quarter. Bity holds three Swiss licences (asset tokenisation, crypto custody, crypto brokerage) (High, PDF).
- Their own figure: they need "about five times" the fee income, so about $60K a year, just for storage, security audits and basic operations. Staff are extra (High).
- Bity says its 2.5% margin "doesn't even cover one-fifth of the real costs" per year. That puts real costs above about $125K a year per CHF 1M of gold (Med).
- The DAO also paid its team 56,746 ICP from its treasury (High).
- **Fee income covers about 20% of basic costs.**

**(4) Hard financials**
- The DAO raised 783,722 ICP in December 2023, about $7.8M at the time. 548,603 ICP is locked for 8 years and 100,000 ICP went into WTN (High, PDF).
- GOLDAO trades at $0.0053, for a $3.6M market cap. That is down 93.9% from its high ([CoinGecko](https://www.coingecko.com/en/coins/gold-dao), High).
- They dropped their planned gold-backed stablecoin, USDG, after FINMA and other regulators tightened the rules from Q4 2024 (High).
- Their stated break-even path needs about $100M of GLDT in circulation to earn at least $100K a month (High). Today they have about $0.77M.

**(5) How the parents make money**
- Bity and ORIGYN paid for the gold, vault, legal work, audits and insurance (High, PDF).
- Most third parties would not go through KYC to buy gold for the project, so the partners bought most of it themselves (High).

**(6) Verdict: BURNING / SUBSIDISED BY PARENT. Confidence: High.**
- "Fees from all GLDT transactions averaged 1,000 CHF per month. We would need about five times that amount" ([PDF](https://fjdhj-uyaaa-aaaai-q4fma-cai.icp0.io/GoldDAO_Chapter2.0.pdf)).

## 2. Tenbin Gold / TGLD (Tenbin Labs)

**This is not vaulted gold.**
- TGLD is backed by USDC plus long gold futures on CME. About 75% or more of the collateral sits on-chain earning yield, and the rest is futures margin ([primer](https://tenbinlabs.xyz/blog/tenbin-primer), High).
- The legal docs describe the tokens as "a debenture or similar unsecured debt instrument". Only whitelisted, KYC'd users can mint, and US persons are excluded ([legal page](https://docs.tenbinlabs.xyz/legal-and-transparency/legal-and-regulatory.md), High).
- Legal entities: Tenbin AssetCo (BVI) SPC Ltd and Tenbin Foundation (Cayman). The input said "not verified"; this is now confirmed (High).
- Private beta went live on 2026-02-26 ([blog](https://tenbinlabs.xyz/blog/private-beta), High).

**(1) Fees**
- Default mint and redeem fees are 0%. Execution costs of "a few basis points" are passed through to users ([pricing](https://docs.tenbinlabs.xyz/solution-overview/minting-and-redemption/protocol-pricing.md), High).
- The website shows a spread under 3 bps ([site](https://tenbinlabs.xyz), High).
- A "Conditional Market Adjustment Fee" applies only when markets are under stress (High).
- There is a fee for skipping the staking cooldown. The amount is not published (High).

**(2) Revenue**
- Revenue comes from yield on the USDC collateral plus the futures basis, and it is "shared with staked asset holders" ([revenue](https://docs.tenbinlabs.xyz/solution-overview/protocol-revenue.md), High).
- TGLD supply is 137.87 tokens on-chain (High, my own on-chain check). At $4,032 that is about $556K.
- Yield side: $417K on-chain × about 4.4% (e.g. Steakhouse USDC) ≈ $18K a year.
- Cost side: gold futures roll cost of about 4% a year × $556K ≈ $22K a year.
- Net: roughly −$4K to +$5K a year (Low).
- Tenbin's own example shows the same thing. A 4% financing cost needs 4.44% on-chain yield just to break even. **The gold product is built to earn close to zero margin.**
- Whole protocol on CoinGecko: TGLD $0.56M + [TMXN](https://www.coingecko.com/en/coins/tenbin-mexican-peso) $0.49M + [TBRL](https://www.coingecko.com/en/coins/tenbin-brazilian-real) $1.56M ≈ $2.6M (High).
- Even a generous 2% net take on that is about $52K a year (Low). Most of that would come from the higher Brazilian real interest rate on TBRL, not from gold.

**(3) Costs**
- Three smart-contract audits (Spearbit, Verilog, Fuzzland) and a LlamaRisk economic audit (July 2026) ([audit page](https://docs.tenbinlabs.xyz/resources/economic-audit.md), High).
- Chainlink proof of reserves on Base, updated daily ([PoR](https://docs.tenbinlabs.xyz/hedging-and-risk/proof-of-reserves.md), High).
- Ripple Prime acts as custodian, plus an unnamed futures broker ([custody](https://docs.tenbinlabs.xyz/custody-and-partners/future-commission-merchants-and-custodians.md), High).
- BVI and Cayman entities, plus a team of unknown size.
- I estimate $1M+ a year (Low). Revenue covers well under 10%.

**(4) Hard financials**
- The website lists backers: Galaxy Digital, GSR, Fenbushi, Uniswap, Bankless, Primitive, Alpen (High). The round size was not found.
- DEX prints swing widely: a high of $7,070 on 2026-04-07 and a low of $3,504 on 2026-05-06. These come from very thin liquidity, not real gold moves (Med).
- Volume is about $20 a day (High).

**(5) How the parent makes money**
- Gold is one of three products and about 21% of tracked supply.
- The business case is FX carry trades (BRL, MXN), not gold.
- Their blog has a post titled ["Why On-Chain Gold is a Trap"](https://tenbinlabs.xyz/blog) (Nov 2025).

**(6) Verdict: BURNING (VC-funded, before scale). Confidence: Med.**
- 0% fees, a spread under 3 bps and a gold yield that only breaks even cannot pay for audits, entities and staff at $0.56M of supply.

## 3. Gram Gold / ONS Gold (GRAMG / ONSG), Token Teknoloji A.Ş.

**Correction to the input: this is not a pure-play gold-token company.**
- Token Teknoloji sells B2B services: stablecoin development, token launches, asset tokenisation, smart contracts, exchange listing support. It also runs the TokenX trading app ([services](https://token.com.tr/hizmetlerimiz), High).
- Its LinkedIn page lists 2–10 employees, Istanbul, founded 2021 ([LinkedIn](https://linkedin.com/company/tokencomtr), High).

**Supply also differs from the input.**
- GRAMG total supply on Avalanche is **48,000** tokens with 18 decimals, which equals 48 kg of gold, about $6.2M (High, my own on-chain check). CoinGecko shows 48, which looks like a data error.
- All 48,000 sit in 4 wallets (52%, 31%, 10%, 6%) (High, Routescan holders).
- There have been only 42 on-chain transfers ever, from Aug 2023 to the last one on 2026-06-05 (High).
- The Polygon supply is 0 (High).
- ONSG supply is 100 oz, about $403K (Med, CoinGecko).
- So customers trade on the Bitlo exchange's own books, off-chain. The on-chain tokens act as an inventory record. **I found no reserve attestation, so the 48 kg cannot be verified.**

**(1) Fees**
- ONSG advertises "no storage costs" ([CoinGecko API](https://api.coingecko.com/api/v3/coins/token-teknoloji-a-s-ons-gold), High).
- No mint, redeem or transfer fee schedule was found.
- Bitlo bid-ask spreads: GRAMG 0.46–0.67%, ONSG 0.51–0.64% (High, CoinGecko tickers).

**(2) Revenue**
- Volume: GRAMG $4.4K + ONSG $5.6K ≈ $10K a day, or about $3.65M a year (High).
- If the issuer captures 0.3–0.6% of that spread, it earns about $11–22K a year (Low).
- There is no fee on gold held, because storage is free.

**(3) Costs**
- A team of 2–10 in Turkey: roughly $100–300K a year (Low).
- If the 48 kg is really vaulted, storage and insurance cost roughly $6–12K a year, with no storage income to offset it (Low).
- Licence status under Turkey's 2024 crypto law (Law 7518) was not found.
- **Revenue does not cover the team.**

**(4) Hard financials**
- No filings, funding rounds or attestations were found.
- Volume is micro-scale and trading is on one venue (Bitlo).

**(5) How the parent makes money**
- Most likely through B2B tokenisation and consulting work, which would cover the gold tokens' costs (Low; inferred from the services page).

**(6) Verdict: SUBSIDISED BY PARENT (best guess) / UNKNOWN. Confidence: Low.**
- About $10–20K a year of spread income cannot pay even a 2-person team.
- The reserves have no attestation, and the on-chain activity looks like an inventory ledger rather than customer use.

## Takeaway for the user's question

- **Pure gold-token issuance does not pay for itself at small scale.** Gold DAO's real figures show a take of about 1.2% a year on the gold held, against basic costs of about $60K a year before staff. Break-even needs roughly $5M of gold for bare operations and likely $10M+ once staff are included.
- Every small player here is held up by something else:
  - Gold DAO: Bity's gold-sale margin and ORIGYN's money.
  - Tenbin: VC money and FX carry products.
  - Token Teknoloji: B2B tokenisation services.
- The one dependable profit point seen in this set is the **markup when the customer buys gold** (Bity's 2.5%). A further 0.5% comes from the buy/sell spread on Bitlo. Transfer fees and custody fees are tiny at this scale.

Searching was limited: the web-search budget was already used up, so I fetched known pages directly and checked supplies on-chain myself. The Tenbin round size, Token Teknoloji's licences and fees, and the GLDT NFT-to-GLDT swap fee are still unverified.