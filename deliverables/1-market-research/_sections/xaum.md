# Matrixdock Gold (XAUm)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | XAUm | **High** |
| Issuer (marketing) | Matrixdock, "a brand wholly-owned by Matrixport" | **High** |
| Issuer (registry) | **Matrix Mining Limited**, an SPV held under a special purpose trust. **Not located in any searchable company register.** Domicile reported as British Virgin Islands by rwa.xyz, not confirmed against a register | **Low** |
| Trustee / enforcer | Appleby Global Services (trustee); Hamilton Services (enforcer). Jurisdiction of the trust not stated anywhere in issuer docs | **Medium** |
| Domicile | BVI (secondary source only). Gold and operations sit in Singapore and Hong Kong | **Low** |
| Backing claim | 1 token = 1 troy oz of 99.99% purity LBMA-accredited gold, 1kg bars | **High** |
| Chains | Ethereum, BNB Chain, Solana, Polygon, TRON, Sui, Stellar, Plume, HashKey | **High** |
| Contract address (Ethereum) | `0x2103E845C5E135493Bb6c2A4f0B8651956eA8682` (MTokenMain, ERC-20) | **High** |
| Supply | 12,882.21 XAUm | **High** |
| Reserves held | 16,299.036 troy oz (over-collateralised vs supply: see §4) | **High** |
| Market cap / TVL | ~$52.7M | **High** |
| Regulatory status | **No licence in the issuer's own name.** rwa.xyz classifies it "Non-Regulated". Group affiliates hold unrelated licences | **Medium** |
| Subscription fee | 0.25%, **currently waived** until TVL reaches $100M | **High** |
| Ongoing custody fee | **0%, but explicitly reversible on 30 days' notice** | **High** |
| Redemption fee | 0.25% (charged in token: see §6) | **High** |
| Advertised yield | **None.** No yield, no APY, no leasing disclosed | **High** |
| Named officers | **Not disclosed.** No director or officer named for Matrix Mining Limited | **High** |

---

## 1. What it is

XAUm is a tokenized gold product from Matrixdock, the RWA platform of Matrixport. Each token represents one troy ounce of 99.99% LBMA-accredited gold held in 1kg bars in Brink's and Malca-Amit vaults in Singapore and Hong Kong. It launched September 2024 and now sits at roughly $52.7M across nine chains ([rwa.xyz](https://app.rwa.xyz/assets/XAUm)).

The grading premise for this protocol was that it out-documents much larger competitors, and that is correct, with one important qualification. On **mechanics** (fees, custody, audit, contract architecture, cross-chain reserve accounting) XAUm's disclosure is the strongest in this cohort, and materially better than PGOLD or ORO. On **legal identity** it is no better and arguably worse: the issuing entity cannot be found in any register, and no officer is named anywhere. The disclosure is deep on operations and thin on who is legally responsible.

Its structural distinction versus Aurumix is that it is an **institutional bullion instrument wearing a token**, sized in 1kg bars and priced for wholesale. It has no retail savings mechanic of any kind.

## 2. Legal structure

The stack, as disclosed: token holders hold XAUm; **Matrix Mining Limited** is the issuer SPV; the SPV is owned by a **special purpose trust**; the trust holds the gold via custodians. Matrixdock states this "[follows] STBT's innovative bankruptcy-remote design" and that gold ownership belongs to "the asset holder entity under Matrixdock's SPV at all times" ([physical gold custody](https://matrixdock.gitbook.io/matrixdock-docs/english/gold-token-xaum/physical-gold-custody.md)).

**What the holder actually owns is not stated.** This is the central gap. Issuer materials describe holders as having "the rights to redeem the underlying physical gold" and the token as "backed by" gold. Neither formulation is a statement of legal title. No public document says whether a holder is:

- a beneficiary under the purpose trust,
- the owner of specific bars, or
- an unsecured contractual claimant against Matrix Mining Limited.

The trust deed and token terms are not public. The GitBook index lists an "XAUm Terms and Conditions" page, but the document itself is an embedded file that does not render as text. **Confidence: Low** on the legal characterisation, and this should be read as "not disclosed", not as "probably a trust interest".

A note on the trust's purpose. A purpose trust with an *enforcer* (Hamilton Services) is the classic BVI/Cayman orphan-SPV structure. Its function is to make the issuer bankruptcy-remote from the sponsor: it stops Matrixport's creditors reaching the gold. It does **not** automatically confer any beneficial interest on token holders. Orphan structures are usually set up so that *nobody* is a beneficiary, which is precisely why an enforcer is needed. So the structure that reads as investor protection is, on its face, sponsor-insolvency protection. Whether it also protects holders depends entirely on the undisclosed deed. **Confidence: Medium** on the reading, **Low** on the outcome.

## 3. Regulatory and compliance posture

**The XAUm issuer holds no financial services licence in its own name.** rwa.xyz records the product as "Non-Regulated" ([rwa.xyz](https://app.rwa.xyz/assets/XAUm)), and no XAUm document claims any authorisation.

Registers and sources checked, with results:

| Register / check | Result |
|---|---|
| Company register search for "Matrix Mining Limited" | **No match** tied to Matrixdock/Matrixport in any searchable jurisdiction |
| BVI FSC | No licence found for the issuer |
| MAS (Singapore) financial institutions directory | No listing for the issuer |
| Hong Kong SFC public register | No listing for the issuer |
| Cayman CIMA / Dubai VARA / ADGM FSRA | No listing for the issuer |

**Licences that exist belong to other entities and do not cover XAUm.** This distinction matters because it is easy to misread. Matrixport group holdings include a Hong Kong trust/money lender licence, a US money services licence, a Swiss FINMA asset management licence, and an MAS Major Payment Institution licence granted to subsidiary **Fly Wing Technologies Pte Ltd** in March 2025 ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/03/05/3037067/0/en/Matrixport-Subsidiary-Fly-Wing-Receives-Major-Payment-Institution-License-from-MAS-in-Singapore.html)). Separately, InvestaX, which distributes XAUm, is MAS-licensed in its own right. **None of these licences attach to Matrix Mining Limited or to XAUm as a product.** A reader who sees "Matrixport is MAS-licensed" next to XAUm draws a false conclusion.

The Terms of Use carry a standard disclaimer that nothing constitutes "an offer or a solicitation of an offer to buy or sell any products or services, including but not limited to any securities" ([terms of use](https://matrixdock.gitbook.io/matrixdock-docs/english/legal/terms-of-use.md)), plus a prohibited-countries list.

Compliance is therefore delivered through **KYC and gated mint/redeem access**, not through a product licence. Every mint and redeem requires a Matrixdock account, KYC verification and a bound wallet.

## 4. Custody and proof of reserve

| Item | Disclosed position | Confidence |
|---|---|---|
| Custodians | Brink's (primary), Malca-Amit | **High** |
| Vaults / cities | Brink's Hong Kong, Brink's Singapore, Malca-Amit Singapore (Le Freeport) | **High** |
| Allocated? | Bars are specific and individually weighed, but ERC-20 holders have **dynamic** allocation, not a fixed bar. Fixed allocation requires converting to a BullionNFT (see §8) | **High** |
| Bar list published | **No public bar list with serial numbers.** The transparency page's asset-statement table currently renders "No results" | **High** |
| Reserve audit | **Bureau Veritas**, semi-annual, physical count. First January 2025; second covered 421 x 1kg bars = 13,534.308 oz, published 31 July 2025. Four report files are posted | **High** |
| Audit method | "Each bar was individually weighed and measured to verify the accuracy of its physical specifications and to confirm its consistency with recorded vault data" ([Matrixdock](https://matrixdock.substack.com/p/matrixdock-publishes-its-second-independent)) | **High** |
| PoR feed | On-chain PoR Oracle on Ethereum mainnet, gating a Global and per-chain Local Mint Budget | **High** |
| Smart contract audits | BlockSec (EVM), Zellic (Sui), Accretion and Sec3 (Solana) | **High** |
| Insurance | Brink's coverage stated at US$50M as of 29 November 2024 | **Medium** |

**This is the strongest reserve-verification setup in the cohort, and it is worth being precise about why.** Three separate things exist here that issuers usually blur into one word, "audited":

1. A **reserve attestation**: Bureau Veritas physically counting and weighing bars, semi-annually.
2. A **smart contract code audit**: four firms, on the code only, saying nothing about gold.
3. A **PoR oracle**: an on-chain supply cap enforcing that summed supply across nine chains cannot exceed the attested reserve.

Item 3 is the genuinely interesting engineering, and it is the piece almost nobody else has. Multi-chain gold tokens usually risk minting more tokens than gold because each chain accounts separately. XAUm's Global Mint Budget makes cross-chain over-issuance a contract-level impossibility rather than a promise.

Two caveats worth carrying forward. First, **the insurance is smaller than the reserve**: $50M of stated Brink's cover against ~$52.7M of gold, a gap that widens as it grows, though vault insurance terms are usually more nuanced than a single headline number. **Confidence: Medium.** Second, **no bar list is public**, so the Bureau Veritas count is a trusted third-party assertion, not something a holder can independently reconcile.

The reserve/supply gap is notable and favourable: **16,299.036 oz held against 12,882.21 tokens outstanding**, roughly 26% over-collateralisation. Matrixdock does not explain this. The most likely reading is unsold inventory pre-positioned in the vault to support minting, not surplus backing per token. Do not present it as a 126% backing ratio without confirmation.

## 5. Issuance

Mint via the Matrixdock web app: create an account, complete KYC, bind a Web3 wallet, subscribe with USDC or USDT. Delivery is **T+3**. Order window runs 6:00 PM to 5:00 PM+1 New York time on working days, i.e. it tracks bullion market hours, not crypto's 24/7.

Fee is 0.25%, **currently waived**: "from November 8, 2024, XAUm is offering a limited-time promotion: minting fees will be waived until the Total Value Locked (TVL) reaches $100 million." At ~$52.7M the waiver is roughly half-way to expiry.

**No minimum mint size is disclosed.** Not found in any issuer document.

## 6. Redemption

Two paths, and unlike Aurumix, physical redemption genuinely works and has been executed.

**Stablecoin redemption**: USDC/USDT, T+3, 0.25% fee. No minimum disclosed.

**Physical redemption**: minimum **32.148 XAUm = one 1kg LBMA bar**, available in Singapore and Hong Kong only, to KYC-verified users, requested at least T+3 in advance, collected in person or by secured delivery.

Matrixdock executed the first physical redemption on **22 April 2025** at Malca-Amit's Le Freeport vault in Singapore: one 1kg bar, redeemed by an unnamed "seasoned crypto investor", who transferred **32.22837 XAUm** to receive 32.148 oz of gold, the difference being the 0.25% fee ([Matrixdock](https://www.matrixdock.com/blog/announcements/matrixdock-completes-first-ever-physical-redemption-of-tokenized-gold)).

Two observations. The redemption fee is **taken in token, not cash**: the user hands over more XAUm than the gold they receive. That is the in-kind deduction model, and it works here precisely because XAUm's peg is defined per-token (1 token = 1 oz) rather than as a pool ratio. Second, the ~$4,000 gold price makes the 1kg minimum roughly a **$130,000 ticket**. Physical redemption is real but wholesale-only; a small holder's exit is the secondary market.

Eligibility is defined by KYC and geography, not by an undefined "qualified holder" category. That is cleaner than several peers.

## 7. Fees and revenue model

| Fee line | Rate | Notes |
|---|---|---|
| Minting / subscription | 0.25% | **Waived** until TVL hits $100M |
| Redemption (stablecoin) | 0.25% | Active |
| Redemption (physical) | 0.25% | Active, charged in token |
| Ongoing management | **0%** | Reversible: see below |
| Storage / custody | **0%** | Reversible: see below |
| Physical delivery / shipping | **Not disclosed** | Secured delivery offered, cost not published |

**This is the finding that matters most for Aurumix, so it deserves to be stated exactly.** XAUm markets zero storage and management fees. But its own documentation reserves the right to change that: "any change will be communicated via official channels and at least 30 days advance notice will be provided."

So the correct characterisation is **not** "XAUm has solved custody costs". It is: **XAUm is currently subsidising custody, and has explicitly retained the contractual right to stop.** Right now it is running with *both* the mint fee waived *and* no custody fee, meaning the only live revenue line is the 0.25% on redemptions, and redemptions are the one activity the business does not want to encourage.

The arithmetic is worth doing. At ~$52.7M of gold, commercial allocated vault-and-insure cost runs on the order of 0.1–0.5%/yr, so call it **$50k–260k a year**. Monthly transfer volume is ~$28.7M, but transfers are not mints or redeems and generate no fee. Redemption fee income at 0.25% would need **$20M–100M of annual redemptions** to cover custody alone. That is not plausible. **The gap is being funded by Matrixport, not by the product.**

That is a coherent strategy: Matrixport is a large group, XAUm is a strategic RWA reserve asset it invested $3M into directly, and buying market share in tokenized gold with a fee waiver is rational. But it is a **parent-subsidised land-grab, not a self-funding fee model**, and the 30-day notice clause is the issuer telling you so in writing.

## 8. Token architecture

**Standard: plain ERC-20**, plus BEP-20, SPL/Token-2022 on Solana, TRC-20 on TRON, and native formats on Sui and Stellar. **Not ERC-3643, not permissioned at the transfer layer.** Anyone can hold and transfer XAUm on a DEX without KYC. The permissioning sits entirely at the **mint/redeem gateway**, not on the token.

This is a deliberate and instructive trade. XAUm gets full DeFi composability, nine-chain reach and free secondary liquidity, and gives up any ability to know or control who holds it. It can afford that because **the token carries no rights beyond redemption**: no yield, no governance, no tier standing. There is nothing that breaks when it moves to an anonymous wallet, because the wallet's only privilege (redeeming) is re-gated by KYC at the counter.

Notable architecture:

- **BullionNFT (ERC-721)**, deployed on Ethereum, BSC, Plume and HashKey. ERC-20 XAUm has **dynamic** allocation to the gold pool; converting the right quantity into an NFT gives **fixed allocation to one specific 1kg bar**, which "cannot be redeemed by another". This is a two-tier ownership model: fungible by default, specifically-allocated on request.
- **`controllerTransfer`**: an admin function letting the issuer move tokens without holder consent. This is not theoretical. Matrixdock used it on sibling product STBT after the March 2025 Zoth hack, transferring 2,819,088.62 wSTBT from a frozen vault to a new address on 3 July 2025 ([Matrixdock notice](https://matrixdock.gitbook.io/matrixdock-docs/english/announcements/other-announcements/notice-wstbt-transfer-on-request-from-zoth)). The XAUm contracts expose comparable controller powers. So XAUm is **transfer-free but not owner-sovereign**: the issuer can move your tokens.
- **Cross-chain messengers** (`MTokenMessengerV3`, LayerZero variants) moving mint budget between chains under the PoR cap.
- Upgradeability and admin key custody (multisig vs EOA, timelock) are **not disclosed** in documentation and were not verified on-chain.

## 9. Liquidity and market

- Market cap: **~$52.7M**, up 7.14% over 30 days.
- Supply: **12,882.21 XAUm**.
- Holders: **52,858**, down 0.22% over 30 days.
- Monthly transfer volume: **$28,717,225** across 14,639 transfers.
- 30-day active addresses: **643**.
- Venues: KuCoin spot, HTX, InvestaX, plus DEX liquidity across chains.

The transfer-volume-to-market-cap ratio (~0.54x monthly) is far healthier than PGOLD's sub-$20/day, so **XAUm is a real market rather than a parked balance**. But read the holder figure carefully: **52,858 holders against 643 monthly active addresses and a 1kg physical redemption minimum**. Those holders are overwhelmingly small, passive, secondary-market buyers who could never redeem physically. The distribution is retail; the product design is institutional.

The premium question relevant to Aurumix: XAUm's public mint/redeem quotes were $4,051.73 mint and $4,020.97 redeem, a **spread of $30.76, about 0.76%**. This is the important number. XAUm has a continuously operating two-way primary window at a sub-1% spread. **That is a hard ceiling on any secondary premium**: no arbitrageur will pay 3–8% over spot for a token they can mint at +0.38%. A tight primary window and a sustained premium cannot coexist.

## 10. Distribution

- **Channels**: direct via the Matrixdock web app (KYC-gated); centralised exchanges (KuCoin, HTX); InvestaX, an MAS-licensed tokenization platform, for accredited/institutional flow; DeFi and cross-chain deployment (Plume, HashKey, Stellar, Solana).
- **Target segment**: crypto-native and institutional buyers. The 1kg physical minimum, T+3 settlement and bullion-hours trading window all point wholesale.
- **Geography**: Asia-centric (Singapore, Hong Kong), with a prohibited-countries list.
- **Savings plan / recurring purchase / referral / affiliate / agent commissions**: **None found.** No recurring-buy feature, no SIP, no referral programme, no agent tier.

Distribution strategy is **chain expansion and venue listings**, i.e. being present wherever crypto capital already sits, rather than recruiting new savers. It is a liquidity strategy, not an acquisition strategy. This is the near-universal pattern across the cohort and confirms the brief's expectation.

## 11. Recent developments

- **2 July 2026**: Matrixport Ventures invested **US$3M into XAUm** as a strategic allocation ([MEXC News](https://www.mexc.com/news/matrixport-ventures-has-invested-3-million-in-tokenized-gold-xaum/30826)). The parent is buying its own product.
- **24 June 2026**: XAUm **deployed on Stellar** ([AAP](https://aapnews.aap.com.au/aapreleases/cision20260624AE89919)).
- **17 March 2026**: **KuCoin listing** of XAUm ([Cryptonomist](https://en.cryptonomist.ch/2026/03/17/tokenized-gold-kucoin-listing/)).
- **10 September 2025**: Matrixport and **HKUST Institute for Financial Research** published a joint report on gold tokenisation ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/09/10/3147655/0/en/Matrixport-and-HKUST-Institute-for-Financial-Research-Release-Joint-In-Depth-Report-on-Gold-Tokenisation.html)).
- **31 July 2025**: **Second Bureau Veritas audit published**: 421 x 1kg bars, 13,534.308 oz, confirming a semi-annual cadence ([Matrixdock](https://matrixdock.substack.com/p/matrixdock-publishes-its-second-independent)).
- **10 July 2025**: Matrixport announced a **Strategy XAUm Reserve**, holding XAUm on its own balance sheet ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/07/10/3113587/0/en/Matrixport-Establishes-Strategy-XAUm-Reserve-Remains-Bullish-on-the-Future-of-Tokenized-Real-World-Assets.html)).
- **3 July 2025**: `controllerTransfer` used to move 2,819,088.62 wSTBT after the Zoth incident. **Sibling product, not XAUm**, but it proves the admin power is live and exercised.
- **22 April 2025**: **First physical redemption**: 1kg bar at Le Freeport, Singapore.
- **21 March 2025**: Zoth hack; Matrixdock's wSTBT vault frozen as a precaution. Zoth lost ~$8.4M overall ([Halborn](https://www.halborn.com/blog/post/explained-the-zoth-hack-march-2025)). **XAUm unaffected.**
- **5 March 2025**: Matrixport subsidiary **Fly Wing Technologies** received an MAS Major Payment Institution licence.
- **January 2025**: First Bureau Veritas audit published.
- **8 November 2024**: Mint fee waiver begins, running until $100M TVL.

**No security incident, depeg, or enforcement action against XAUm was found in the period.** Its only brush with an incident was through a sibling product, and it was handled by freezing and reissuing.

## 12. Relevance to Aurumix

XAUm is the closest thing in this cohort to a **well-run control group**: same asset, opposite strategy. It answers five of the nine design questions with unusual clarity, and its answers are mostly *warnings* rather than templates, because it monetises the opposite end of the market from Aurumix.

**Q1, custody fee mechanism (directly answered, and the single most useful finding).** XAUm charges **no custody fee and currently no mint fee**, funding vaulting from the Matrixport balance sheet, while reserving the right to change with **30 days' notice**. This is the brief's "third option" (charge nothing, recover elsewhere) observed live, and the lesson is that even the best-capitalised operator in the category **would not commit to it permanently in writing**. If Aurumix ever markets "no storage fees", copy the 30-day notice clause verbatim; it is cheap, honest, and preserves the option. Note also that XAUm never faces Aurumix's peg problem: because 1 token = 1 fixed ounce rather than a share of a pool, XAUm *can* deduct fees in gold (and does, on redemption) without breaking anything. **Aurumix's grams-per-token design is what makes in-kind fees destructive.** The fee mechanism follows from the peg design, so that choice should be made first.

**Q2, dividend funding (answered by absence, and it is the strongest possible corroboration).** XAUm pays **zero yield**. No APY, no leasing, no lending, no rehypothecation. The most institutionally sophisticated issuer here, with LBMA supply chains, Brink's vaults, real bullion-desk relationships and a large parent balance sheet, is the one that pays holders nothing. That is not an oversight; it is what unencumbered allocated gold actually returns. It corroborates the brief's PGOLD finding from the opposite direction: PGOLD promises 5% and cannot fund it, XAUm could plausibly attempt leasing and declines to. **Any Aurumix yield story has to explain why it can do what Matrixport chose not to.**

**Q3, token standard (a clean and quotable contrast).** XAUm uses **plain ERC-20 across nine chains, permissioned only at the mint/redeem gate**. It can do this because the token confers no rights that survive a transfer. Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous transfer. **The rule the comparison establishes: permissioning is required in proportion to how much off-chain entitlement the token carries.** XAUm carries none, so it pays nothing for freedom. Aurumix carries four, which is the actual argument for ERC-3643, and it is a stronger argument than "compliance". Separately, `controllerTransfer` is worth copying on its own merits: an issuer that can freeze and reissue after a hack is materially safer, and Matrixdock has proven the capability in production.

**Q5, redemption (a direct rebuttal to one Aurumix assumption).** XAUm offers **real physical redemption, executed and documented**, but with a 1kg minimum (~$130k) in two cities. The lesson is not "Aurumix must offer redemption". It is that **physical redemption can be offered at a threshold no retail saver will ever reach**, which preserves the "you own real gold" claim honestly. That is strictly better positioning than Aurumix's flat no-redemption stance, at near-zero operational cost, since the population able to present $130k of tokens is tiny. Aurumix should consider a high-threshold physical option purely as a credibility asset.

**Q6, premium and liquidity (this weakens the client's thesis).** XAUm runs a continuous two-way primary window at a **0.76% spread**. A competitor offering mint-and-redeem at under 1% caps what any tokenized gold product can sustain as a premium, because arbitrage is trivially available to anyone with a KYC account. **The 3–8% premium assumption should be re-examined against this.** Aurumix's premium, to the extent it exists, has to come from the savings-plan wrapper and switching costs, not from gold scarcity. Note this is a *different* argument from the PGOLD illiquidity finding: PGOLD shows a premium can't be sustained in a thin market, XAUm shows it can't be sustained in a liquid one either.

**Q7, proof of reserve (the benchmark to beat).** Semi-annual Bureau Veritas physical counts with individual bar weighing, four published reports, a PoR oracle capping cross-chain supply, and four separate smart contract audits, with the reserve attestation and code audits kept clearly distinct. **This is the disclosure standard Aurumix should target**, and it is achievable: it is procurement, not innovation. The one place Aurumix can beat it cheaply is the **published bar list with serial numbers**, which XAUm does not provide (its transparency page currently renders empty).

**Q8, distribution (confirms Aurumix's actual moat).** No savings plan, no recurring purchase, no referral, no agent commissions. XAUm distributes by listing on venues where crypto money already is. It has 52,858 holders but only 643 monthly active addresses, i.e. it accumulated a passive retail base **without any acquisition machinery**, and cannot deepen those relationships. **Aurumix's agent network and SIP are genuinely differentiated**, and this is the clearest evidence in the cohort that the differentiation is real rather than assumed.

**Q9, wind-down (partial, and better than peers).** No published wind-down plan for the token. But XAUm has two structural protections nobody else here has: a **bankruptcy-remote purpose trust** isolating gold from Matrixport's creditors, and a **contractual custodian obligation** that on custodian failure it "shall promptly arrange for the return and delivery of all underlying gold in accordance with Matrixdock's instructions". This covers *custodian* failure and *sponsor* failure. It does not say what holders get if the **issuer SPV** fails, which is the case that matters. So the brief's finding holds: **still no published wind-down plan**, and Aurumix committing to one remains cheap differentiation.

**Q4, regulatory route (answered, with a caution about the wrong lesson).** XAUm operates **unlicensed**, compliant-by-KYC rather than by authorisation, from an offshore SPV, selling into Asia. Aurumix cannot copy this: the ICS dividend and the credit facility are exactly the features that make a product regulated, and they are the features XAUm does not have. **XAUm's unlicensed status is purchased by product simplicity, not by clever structuring.** It is evidence for the brief's existing view that the hybrid design drives the regulatory cost, and that each bolt-on feature should be priced against the licensing burden it triggers.

**One contradiction to record.** The brief's framing is that this cohort's documentation is uniformly poor. XAUm partially contradicts that on operations: its custody, audit and contract disclosure is genuinely strong and should not be lumped in with PGOLD or ORO. But the contradiction only goes so far, and the shape of the gap is itself the insight: **XAUm discloses everything about the gold and almost nothing about the company.** The issuer does not appear in any register we could search, no officer is named, and the token terms and trust deed are not public. Excellent operational transparency and unverifiable legal identity coexist comfortably, which is a useful warning against reading "well documented" as "well accountable".

## 13. Open items for verification

- [ ] Locate **Matrix Mining Limited** in a company register (BVI FSC via paid search, or Cayman/HK/Singapore). Obtain registration number, incorporation date and registered agent. **The BVI domicile currently rests on a single secondary source (rwa.xyz) and is unverified.**
- [ ] Obtain the **XAUm Terms and Conditions** file from the GitBook embed (`/files/NNRBHwIkWnfMwjjxoYDa`) and determine whether holders are trust beneficiaries, bar owners, or unsecured creditors.
- [ ] Obtain the **purpose trust deed** or confirm its governing jurisdiction. Establish whether token holders are beneficiaries at all, or whether the trust is a pure orphan structure benefiting nobody.
- [ ] Confirm the roles of **Appleby Global Services** (trustee) and **Hamilton Services** (enforcer), and the jurisdiction each operates in. Sourced from Matrixdock's custody page only; not independently confirmed and not found by secondary search.
- [ ] Download the four **Bureau Veritas** reports from the vault audit page and confirm whether individual **bar serial numbers** are listed, and whether scope is full physical count or sampling.
- [ ] Verify **admin key custody** for the Ethereum contract `0x2103E845C5E135493Bb6c2A4f0B8651956eA8682`: multisig or EOA, timelock, and upgradeability. Confirm whether XAUm exposes `controllerTransfer` (confirmed on STBT, inferred for XAUm).
- [ ] Reconcile the **reserve/supply gap** (16,299.036 oz held vs 12,882.21 tokens). Confirm whether the surplus is unsold vault inventory rather than excess backing per token.
- [ ] Confirm current **Brink's insurance limit**. The US$50M figure is dated 29 November 2024 and is now below the ~$52.7M reserve value.
- [ ] Establish whether the **mint fee waiver** has expired, and monitor for any 30-day notice introducing a custody or management fee. This is the single most decision-relevant thing to watch.
- [ ] Confirm **minimum mint size** and **minimum stablecoin redemption size**, neither of which is disclosed.
- [ ] Obtain **physical delivery/shipping costs** for redemption, not published anywhere.
- [ ] Verify the mint/redeem **spread** (observed 0.76%) over time, to test how hard a ceiling it places on any secondary premium.
