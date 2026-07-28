# Tenbin Gold (tGLD)

> **Read this first.** tGLD is not a gold-backed token in the sense the rest of this document uses the phrase. There is no vault, no bar, no allocated metal and no physical redemption anywhere in the structure. It is a **USD-denominated debt note issued by a BVI segregated portfolio company, collateralised in USDC and hedged with CME gold futures**. Every comparison to PAXG, XAUT or Aurus in this profile is a comparison of economic exposure, not of legal form.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | tGLD (staked variant: stGLD) | **High** |
| Issuer (marketing) | Tenbin Labs, New York | **High** |
| Issuer (registry) | **Tenbin AssetCo (BVI) SPC Ltd.** is the obligor. Sister entities **Tenbin TokenCo (BVI) Ltd.** and **Tenbin ServiceCo (BVI) Ltd.** also appear on the BVI register | **High** |
| Domicile | **British Virgin Islands** (issuing entity). Operating team in New York | **High** |
| Backing claim | USD value of 1 troy ounce of gold at LBMA PM price, via USDC collateral + CME gold futures hedge. **No physical gold** | **High** |
| Chains | Ethereum mainnet. Cross-chain via Chainlink CCIP since May 2026 | **High** |
| Contract address | tGLD `0x6a547b25534234bb79CE6961a23Db13DE154b6F4`; stGLD `0x8d301801d899dC81fEabBDE69407A53b82bdBF19` | **High** |
| Supply | ~258 tGLD | **High** |
| Market cap / TVL | ~$1.05M | **High** |
| Regulatory status | **No licence found in any register.** Listed "Non-Regulated" on RWA.xyz | **Medium** |
| Subscription fee | 0% by default, issuer may vary with market conditions | **Medium** |
| Ongoing custody fee | None (no custody exists to charge for) | **High** |
| Redemption fee | 0% by default; **explicitly higher during off-market hours**, scaled to volatility | **Medium** |
| Advertised yield | 4–6% **gold-denominated**, via JPEG Trading's Euler vault | **Medium** |
| Named officers | Yuki Yuminaga, Co-Founder & CEO | **High** |
| Registration number / incorporation date | **Not disclosed** in any accessible register output | **Not disclosed** |

---

## 0. The naming collision: tGLD is NOT Aurus tGOLD

The task flagged a collision risk. It is real as a *search* problem and resolves cleanly as a *fact* problem. **These are two entirely unrelated projects that happen to abbreviate similarly.** Evidence on every axis:

| Axis | Tenbin tGLD | Aurus tGOLD (TXAU) |
|---|---|---|
| Ticker | tGLD / TGLD | **TXAU** |
| Issuer | Tenbin AssetCo (BVI) SPC Ltd. | Aurus |
| Domicile | British Virgin Islands | **United Kingdom** (per RWA.xyz) |
| Unit | USD value of **1 troy ounce** | **1 gram** of gold |
| Backing | USDC + CME futures, **no metal** | Physical gold, LBMA refineries |
| Chain / contract | Ethereum `0x6a547b25...54b6F4` | Ethereum `0xe4a6f23f...a6c53bf`, plus Polygon |
| Price | ~$4,067 (ounce-scale) | ~$102 (gram-scale) |
| Redemption | USD stablecoin only | Physical delivery or cash |
| Redemption fee | 0% default | 3.00% |
| Founded | Seed round Jan 2026 | Long-established, previously AurusGOLD |

Different tickers, different registries, different countries, different contracts, different units, different backing model, an order-of-magnitude price difference. **Confidence: High** that they are distinct. Aurus TXAU is already profiled separately in wave 1; nothing here should be merged into it.

Two further collision traps worth recording for anyone re-running this research:
- **"Tenbin" is also a 2026 romantic-comedy anime** that premiered in July 2026. It dominates general search results and contaminates recency sweeps.
- Some aggregators render the token as "TGLD" uppercase, which collides with unrelated tickers. Anchor on the contract address, not the symbol.

---

## 1. What it is

tGLD is a synthetic, yield-bearing gold exposure token aimed at institutions and DeFi collateral markets, not at retail savers. Tenbin Labs is a New York tokenization protocol that raised a **$7M seed led by Galaxy Ventures** announced **27 January 2026**, with Wintermute Ventures, FalconX, GSR, Nascent, Variant, Archetype and Bankless Ventures participating ([PR Newswire](https://www.prnewswire.com/news-releases/tenbin-raises-7-million-led-by-galaxy-ventures-to-transform-onchain-capital-markets-via-new-asset-tokenization-protocol-302671218.html)).

The core design choice is a deliberate rejection of the custody-wrapper model. Rather than buying bullion and issuing a receipt, Tenbin holds USDC and takes long CME gold futures. Its own framing: tokenization "only works if onchain assets become more useful than their off-chain equivalents" (Yuminaga). The practical consequences are ~30-second mint and redemption (roughly 3 Ethereum blocks), zero fees under normal conditions, and a **yield generated from futures basis and carry** that a physically-backed token structurally cannot produce.

tGLD has a sibling FX product line on the same architecture: tBRL (Brazilian real) and tMXN (Mexican peso), each with a staked variant.

**Correction to the task framing.** This protocol was graded THIN, and one Perplexity recency sweep returned "not found" across the board and concluded tGLD "is not yet broadly live or trading publicly." **That is wrong.** The token is deployed, verifiable on-chain, has a live audit trail, a public GitHub repository, a dated May 2026 infrastructure migration and a dated June 2026 institutional integration. The opacity here is real but narrow: it sits almost entirely in the **legal documentation layer** (terms of issue, registry particulars, jurisdiction exclusions), not in the technical layer, which is unusually well documented. Do not read "small" as "dormant."

## 2. Legal structure

**What a holder owns: a creditor claim, not gold.** tGLD is described as a debt note of Tenbin AssetCo (BVI) SPC representing the USD value of one troy ounce of gold ([Pharos](https://pharos.watch/stablecoin/tgld-tenbin/)). The holder is an unsecured-or-otherwise-ranked creditor of a BVI SPC. They have no title to metal, because no metal exists in the structure.

The structure is reportedly built on **UCC Article 12 controllable electronic records**, the US legal framework for negotiable digital assets, which is a genuinely more modern legal wrapper than most gold tokens use.

**The segregated portfolio company point matters and is under-documented.** A BVI SPC ring-fences the assets and liabilities of each segregated portfolio from every other portfolio and from the company's general assets. In principle this means tGLD noteholders have recourse to the gold portfolio's assets and are insulated from losses in the tBRL or tMXN portfolios. That is a genuine structural protection and, if properly executed, is better than the single-balance-sheet exposure most token issuers offer.

**But we could not verify it.** No Tenbin terms of issue, token terms, or offering document setting out the nature of the claim, the ranking of creditors on insolvency, or the operation of the segregation was found in public sources. The SPC segregation effect described above is **general BVI law inference, not a Tenbin disclosure**. For a product whose entire investor protection story rests on portfolio segregation, the absence of a published constitutional document is the single largest gap in this profile. **Confidence: Low** on how segregation actually operates in practice.

Three BVI entities appear on the register (`AssetCo`, `TokenCo`, `ServiceCo`) alongside `TenB International Ltd`. The division of function between them is **Not disclosed**. Which entity employs staff, which holds IP, and which contracts with the prime broker all bear on what a noteholder can actually reach in a failure.

## 3. Regulatory and compliance posture

**No licence or registration was found in any register.** RWA.xyz classifies the asset's regulatory framework as **"Non-Regulated"**. Specifically checked and not found: BVI FSC licence, SEC registration, CFTC registration, FinCEN MSB registration.

This is not necessarily evasive. A BVI SPC issuing notes to KYC-approved institutional counterparties is a well-trodden structure that can sit outside licensing perimeters by design. But it means the compliance perimeter is **contractual, not supervisory**: enforcement runs through the KYC gate and the restriction registry, not through a regulator.

Compliance is enforced technically. Mint and redemption are KYC-gated through a `Controller` contract and a backend signer holding the on-chain minter role. A `RestrictedRegistry` contract lists "accounts which cannot interact with the controller," checked against both `payer` and `recipient` on every order.

**Not disclosed:** which jurisdictions are excluded, and whether US persons may hold or redeem. For a New York-headquartered team issuing a futures-hedged instrument, whether the note is offered to US persons is a first-order question with commodity-pool and securities implications, and there is no public answer.

## 4. Custody and proof of reserve

The standard table barely applies, which is itself the finding.

| Item | Status |
|---|---|
| Custodian | Hidden Road / Ripple Prime (prime brokerage); StoneX also reported. **Confidence: Medium** |
| Vault / city | **None. No vault exists.** |
| Allocated? | **Not applicable. No physical gold.** |
| Bar list | **Not applicable.** |
| Collateral | USDC, held on-chain by a `CollateralManager` and at prime broker as CME futures margin |
| PoR feed | Chainlink tGLD/USD blended **price** feed. This is a price oracle, **not** a proof-of-reserve feed |
| Reserve attestation | **None found.** No independent third-party attestation |
| Smart contract audit | **Yes, extensive.** 22 Jan 2026: 0xleastwood, Spearbit, Fuzzland. 12 Apr 2026: Zellic, Fuzzland, Cantina |

**This is the fourth-plus instance of the "audited" trap flagged in the brief, and Tenbin is a particularly sharp example.** Tenbin has an unusually strong smart-contract audit record: two rounds, six-plus firms, including top-tier names. A reader skimming "four audits" concludes the reserves are verified. **They are not.** There is no independent reserve attestation at all. What partially compensates is that USDC collateral is on-chain and therefore directly observable in a way vaulted bullion never is. But the **futures margin leg sits at a prime broker and is not publicly observable**, and that leg is what actually delivers the gold exposure. So the collateral is half-transparent by construction and half-opaque, with no attestation covering the opaque half.

**Novel risk this structure introduces that vaulted tokens do not have:** basis risk and margin risk. If gold gaps and futures margin is called, the ability to meet the call determines whether the hedge survives. There is no public disclosure of margin buffers, stress testing, or what happens on a failed margin call.

## 5. Issuance

Mint is permissioned: available only to **KYC-approved counterparties**, executed via signed orders through the `Controller`, with the backend signer holding the minter role. Settlement is atomic and takes roughly 30 seconds. Reported **no minimum transaction size**. Mint fee 0% by default, subject to change with market conditions.

Economically, minting delivers USDC to the protocol, which posts margin and adds futures exposure. Issuance is therefore constrained by the depth of the CME gold futures market, which is enormous. **This is the one genuinely scalable issuance model in the set**: it does not require sourcing, refining, shipping or vaulting metal.

## 6. Redemption

**Redemption is in USD stablecoin. There is no physical redemption and none is contemplated.** ~30 seconds, no stated minimum, 0% fee by default.

One disclosed term deserves emphasis: **redemptions during off-market hours carry a higher fee, set dynamically according to the asset's recent volatility**. This is honest and economically coherent, since the protocol cannot adjust its CME hedge when the exchange is closed and must price that risk. But it means **the redemption cost is not knowable in advance** and is set unilaterally by the issuer. The "0% fees" headline holds only during CME trading hours.

Eligibility beyond "KYC-approved counterparties" is **Not disclosed**. This is exactly the undefined-qualified-holder pattern the brief warns about: a retail-scale holder acquiring tGLD on Uniswap has no documented path to redeem at all, and would be dependent on secondary market liquidity that is currently near zero (§9).

## 7. Fees and revenue model

| Fee line | Amount | Notes |
|---|---|---|
| Mint | 0% default | Issuer may vary with market conditions |
| Redemption (market hours) | 0% default | Issuer may vary |
| Redemption (off-hours) | **Dynamic, volatility-scaled** | Amount not published in advance |
| Ongoing custody / management | **None charged to holders** | No custody exists |
| Protocol revenue | Futures basis, carry, and stablecoin yield on USDC collateral | Routed via a `RevenueModule` |

**This is the cleanest answer to design question 1 in the entire set, and it is the third option the brief hypothesised.** Tenbin charges holders nothing, ongoing or upfront, and does not need to: the collateral itself is productive. USDC earns a stablecoin rate and the futures position earns or pays basis. The protocol takes its cut from that yield stream before passing the remainder to stakers. **The asset pays for its own custody.** Aurumix's vaulted gold cannot do this, because bullion sitting in a vault generates nothing and costs money to store. That asymmetry is the point (see §12).

## 8. Token architecture

Verified directly from the public repository ([tenbinlabs/tenbin-contracts](https://github.com/tenbinlabs/tenbin-contracts)). **Confidence: High.**

- **Standard:** `AssetToken` is a **non-upgradeable ERC-20** with owner and minter roles. `StakedAsset` is **ERC-4626** (vault standard).
- **Permissioned?** Partially, and the design is instructive. The **token itself is a plain transferable ERC-20**, so it can sit in a Uniswap pool or an Euler vault without friction. Permissioning is applied at the **mint/redeem boundary** via the `Controller` and the `RestrictedRegistry`, not on ordinary transfers. Restricted accounts cannot stake, unstake, or transfer staked tokens, and **an admin can burn a restricted holder's tokens.**
- **Upgradeability:** `AssetToken` non-upgradeable (good). `CollateralManager` and `StakedAsset` use **UUPS proxies**, with documentation noting the upgrade feature "can be permanently disabled."
- **Admin keys:** Owner (multisig, controls minter assignment), Minter (the Controller), Curator (vault deposits/withdrawals), Keeper (custodian transfers and revenue ops), Restricter (sets restricted addresses). This is a **substantially centralised trust model** with a live admin burn power.
- **Bridge:** Chainlink CCIP exclusively, since May 2026. LayerZero deprecated.

**This hybrid permissioning model is directly relevant to Aurumix's design question 3** and is discussed in §12.

## 9. Liquidity and market

Per the brief, one paragraph, as one more data point on a settled question.

~258 tGLD outstanding, ~$1.05M market cap, price ~$4,067 (tracking the gold ounce). The **only** public market is a Uniswap V4 tGLD/USDC pool on Ethereum, which turned over **$10.35 in 24 hours** and was flagged "Inactive: no trades in the last 3 hours" ([CoinGecko](https://www.coingecko.com/en/coins/tenbin-gold)). Effectively **zero secondary liquidity**, and aggregator prices are stale by hours or days. It trades at gold, because the KYC-gated 0-fee 30-second mint/redeem channel is a far tighter arbitrage rail than any DEX pool, so institutional participants have no reason to let a premium or discount persist. Consistent with the settled conclusion: another protocol where a premium cannot exist, here because primary redemption is instant and free rather than because the market is deep.

Note this is **private beta**, not decline. Supply grew from ~54 tGLD (~$232K) at an earlier snapshot to ~258 tGLD (~$1.05M), roughly 4.5x. The trajectory is up from a tiny base.

## 10. Distribution

**No retail distribution of any kind.** No savings plan, no recurring purchase, no referral, no affiliate, no agent network, no consumer app. Per the brief, this is the expected finding and it holds here more strongly than for most: Tenbin is not merely lacking retail features, it is **architecturally institutional**, gating mint/redeem behind KYC counterparty approval.

Its distribution strategy is **DeFi composability and institutional credit**, a genuinely different channel from anything else in this landscape:

- **Prime brokers / market makers:** Hidden Road, Ripple Prime, StoneX reported.
- **Curated lending vaults:** on **22 June 2026**, quantitative trading firm **JPEG Trading** launched an RWA curation business with **tGLD as its first curated asset**, in vaults on **Euler**. JPEG stated it will **hold tGLD on its own balance sheet**, on the principle that "the strongest underwriting comes from curators who are willing to stand behind their analysis with their own capital" (Kevin March, Cofounder). The vault targets **gold-denominated yields of 4–6%** ([PR Newswire](https://www.prnewswire.com/news-releases/proprietary-trading-firm-jpeg-trading-launches-rwa-curation-business-302806462.html)).

The strategy is to make tGLD useful as *collateral* rather than attractive as a *holding*. Distribution is B2B2C at best, and currently just B2B.

## 11. Recent developments

- **22 June 2026:** JPEG Trading launches RWA curation business, **tGLD its first curated asset**, vaults on Euler, targeting 4–6% gold-denominated yield; JPEG takes balance-sheet exposure.
- **18 May 2026:** Tenbin **deprecates LayerZero and migrates to Chainlink CCIP exclusively** for all tokenized assets (tGLD, tBRL, tMXN), following an internal security audit prompted by industry cross-chain incidents. Cited CCIP's 16 independent node operators and SOC 2 Type 2 certification. Part of a broader migration wave (over $7.2bn moved from LayerZero to CCIP by 9 July 2026).
- **12 April 2026:** Second audit round completed: Zellic, Fuzzland, Cantina.
- **10 February 2026:** tGLD goes live on Ethereum mainnet, private beta.
- **27 January 2026:** $7M seed led by Galaxy Ventures announced; Wintermute Ventures, FalconX, GSR, Nascent, Variant, Archetype, Bankless Ventures participating.
- **22 January 2026:** First audit round: 0xleastwood, Spearbit, Fuzzland.

No security incidents, exploits, or regulatory/enforcement actions found. The LayerZero migration was **precautionary**, prompted by third-party incidents, not by a Tenbin breach.

## 12. Relevance to Aurumix

Tenbin is the **structural opposite** of Aurumix on almost every axis: institutional not retail, synthetic not physical, BVI not UAE, composable not permissioned, no distribution network at all. It is not a competitor for the same customer. Its value to this engagement is that it answers the client's hardest open question by demonstrating a mechanism Aurumix cannot copy, and the reason it cannot copy it is the most useful thing in this profile.

**On question 2, dividend funding: this is the second documented real-yield precedent, and it is a cleaner one than gold leasing.**

The brief records that wave 1 found gold leasing (Monetary Metals / Streamex) as the candidate precedent for real external yield, with the AgaBullion default of 26 January 2026 as a live warning that "title remains with the lessor" resolves to litigating in a foreign court. **Tenbin funds a comparable yield without lending anyone the gold, because it never holds gold.** The yield comes from futures basis, carry, and stablecoin rates on the USDC collateral. There is no lessee, no counterparty default risk of the AgaBullion type, and no encumbrance on physical metal, for the simple reason that the physical metal does not exist.

Do the arithmetic the brief demands. The advertised **4–6% is gold-denominated**, and unlike Kinesis (~0.10% actual against ~20x advertised) or PGOLD (5% on recycled redemption fees), the disclosed source is **structurally capable of funding it**: USDC collateral earning a stablecoin rate plus gold futures basis are real, external, market-sized yield streams that do not come from other investors' fees. **This is what a fundable yield promise looks like**, and it is the correct benchmark against which to test Aurumix's ICS Dividend. **Confidence: Medium**, since the 4–6% figure comes from a partner's launch announcement rather than realised performance data, and the vault launched only weeks ago.

**The catch, which is the decisive point for Aurumix.** This yield is available *because* the structure is synthetic. Aurumix's entire proposition is that 100% of every dollar buys physical LBMA gold. Physical gold in a vault produces **no** yield and **costs** money to store. Tenbin's collateral produces yield precisely because it is USDC and margin rather than bullion. **Aurumix therefore cannot have both "100% physical gold" and "a yield funded by the asset itself."** That is not a design gap to be engineered around, it is an arithmetic identity. The client's realistic options remain: (a) encumber the gold via leasing and accept counterparty risk, (b) fund the dividend from operating profit and accept the securities-classification and value-story problems, or (c) hold a portion of reserves in a yield-bearing form and stop claiming 100% physical. **Tenbin's existence is the cleanest available evidence for putting that trilemma to the client explicitly.**

**On question 3, token standard: Tenbin offers a third path Aurumix has not considered.** The client is weighing permissioned ERC-3643 base plus ERC-20 wrapper. Tenbin does something cheaper: a **plain, freely transferable, non-upgradeable ERC-20**, with permissioning enforced **only at the mint/redeem boundary** through a Controller and a RestrictedRegistry, plus an admin power to burn restricted holders' balances. The token composes anywhere (Uniswap, Euler) while the issuer still controls who enters and exits the primary market. For Aurumix this is a real option worth evaluating: ICS standing, dividend entitlement and credit eligibility could be tracked in a registry contract keyed to holder identity rather than baked into transfer restrictions on the token. It is less robust than ERC-3643 (an anonymous DEX buyer holds a token carrying no entitlements, which creates a two-tier market and a mispricing risk) but far cheaper to build and integrate. **Flagging the tradeoff, not recommending it.**

**On question 5, redemption:** Tenbin is a mirror-image lesson. Aurumix offers no physical redemption but claims physical backing, which the brief already concedes is a real gap. Tenbin also offers no physical redemption, but it **does not claim physical backing**, so its story is internally consistent. The lesson is not about redemption mechanics, it is about **alignment between the backing claim and the exit mechanism.** Aurumix's exposure is that it makes a stronger backing claim than its exit terms support. Tenbin shows that the gap is closable from either end, and closing it from the disclosure end is free.

Also note Tenbin's **volatility-scaled off-hours redemption fee**. Aurumix's cash buyback faces the same underlying problem: honouring exits when the client cannot transact in the underlying. Tenbin's answer (charge for it, disclose that you charge for it, set it dynamically) is a workable template for Aurumix's buyback terms.

**On question 7, proof of reserve:** Tenbin is the sharpest "audited ≠ attested" example in the set. Six-plus audit firms across two rounds, and **zero reserve attestation.** Aurumix should expect this conflation to be the industry norm and can differentiate cheaply by publishing both separately and labelling them clearly.

**On question 9, wind-down:** **Not disclosed**, consistent with every other protocol examined. But Tenbin comes closer than most by accident: the SPC structure implies portfolio-level segregation on insolvency. It just never publishes the constitutional documents that would let a holder rely on it. The lesson for Aurumix is that **having a protective structure and being able to prove you have one are different things**, and the cheap differentiation is publishing the document, not merely having the structure.

**Questions it does not speak to:** 6 (premium, settled), 8 (distribution: nothing to learn, it has none), 4 (regulatory route: BVI is not a live option for a UAE retail product).

**No contradictions found** with anything in the brief. Tenbin **extends** the wave-1 finding on real yield rather than contradicting it: the brief's standing position was that no properly documented real-yield precedent existed, then Streamex's SEC-filed lease emerged as a candidate. Tenbin is a second, different, and arguably cleaner mechanism, and it does not depend on the lease-default question the AgaBullion incident exposed.

## 13. Open items for verification

- [ ] Obtain the BVI registry particulars for **Tenbin AssetCo (BVI) SPC Ltd.**: company number, incorporation date, status, registered agent. Also **TokenCo**, **ServiceCo** and **TenB International Ltd**, and establish the role of each. Registry search returns names but not particulars; a paid document request via i-bvi.com or a BVI FSC search will resolve it.
- [ ] Locate the **terms of issue / note terms** for tGLD. Confirm the nature of the claim, creditor ranking on insolvency, and **how the segregated portfolio actually operates**. This is the biggest single gap in the profile and everything in §2 is inference without it.
- [ ] Determine whether **US persons** are permitted to mint or hold, and which jurisdictions are excluded. Material given the New York team and the futures-based structure (commodity pool implications).
- [ ] Verify the **4–6% gold-denominated yield** against realised performance in the JPEG Trading Euler vault once several months of data exist. Currently a launch-announcement figure only.
- [ ] Establish the **revenue split** between protocol and stGLD stakers. The `RevenueModule` and `StakedAsset` contracts implement it; read the deployed parameters on-chain.
- [ ] Determine **margin management policy**: buffer levels, stress testing, and the failure mode on a failed CME margin call during a gold gap. This is the structure's distinctive risk and is entirely undisclosed.
- [ ] Confirm whether the **UUPS upgrade capability** on `CollateralManager` and `StakedAsset` has been permanently disabled, or remains live and under whose multisig.
- [ ] Confirm current **prime broker** arrangements: Hidden Road, Ripple Prime and StoneX are all reported, with the Hidden Road / Ripple Prime relationship unclear following that acquisition.
- [ ] Check whether **stGLD** has meaningful TVL, and whether tGLD has exited private beta.
