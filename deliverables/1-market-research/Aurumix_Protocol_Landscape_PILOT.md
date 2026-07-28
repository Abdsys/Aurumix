# Tokenized Gold Protocol Landscape: Format Pilot

> **This is a format sample, not a deliverable.** One protocol (Pleasing Gold) researched end to end so the structure, depth, and house style can be signed off before the remaining fifteen protocols are run. Research performed 2026-07-28 via Perplexity Sonar Deep Research and Sonar Pro.

## How to read this document

Every protocol is profiled against the same ten headings in the same order, so any two can be compared line by line. Three conventions carry throughout:

| Convention | Meaning |
|---|---|
| **Confidence: High** | Established from a primary source: issuer terms, prospectus, audit report, corporate registry, or on-chain contract. |
| **Confidence: Medium** | Established from issuer marketing or a credible secondary source, without a primary document to confirm it. |
| **Confidence: Low** | Fragmentary or contested. Treat as a lead to verify, not a fact to cite. |
| **Not disclosed** | We looked and found nothing. This is a finding in its own right, and is never filled with a plausible assumption. |

Anything a competitor asserts about itself is reported as an assertion, not adopted as fact. Where marketing and legal documents disagree, both are shown.

---

# Pleasing Gold (PGOLD)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | PGOLD | High |
| Issuer (marketing) | Pleasing International Limited | Medium |
| Issuer (HK registry) | Pleasing International (HK) Limited, private company limited by shares, incorporated 2023 | Medium |
| Platform brand | Pleasing Market (formerly Pleasing Golden) | High |
| Domicile | Hong Kong SAR | High |
| Backing claim | 1 token = 1 troy oz, 99.99% purity, LBMA standard, 1:1 | Medium |
| Chains | Arbitrum, Ethereum, Pharos (issuer, Jun 2026). ApeChain listed earlier and **not** named in the June release: status unclear. | Medium |
| Cross-chain | **Chainlink CCIP** since Jun 2026. LayerZero fully deprecated. | Medium |
| Arbitrum contract | `0x3e76bb02286bfeaa89dd35f11253f2cbce634f91` | High |
| ApeChain contract | `0x64ae250e044688ddd04262f17daca23c28d241c2` | High |
| Supply | 19,505 PGOLD | High |
| Market cap / TVL | Issuer claims ~$90M TVL (Jun 2026). rwa.xyz ~$79.8M. One source shows an unreconciled ~$3.95M FDV. | Low |
| Named officer | Leon Ma, Chief Technology Officer | Medium |
| On-chain liquidity | ~$1.71M (Arbitrum) | Medium |
| 24h volume | Frequently under $20 | Medium |
| Regulatory status | rwa.xyz classifies "Non-Regulated". No licence identified. | Medium |
| Subscription fee | 0% | Medium |
| Ongoing custody fee | **None charged to holders** | Medium |
| Redemption fee | 0.50%, physical redemption only | Medium |
| Advertised yield | "5% Gold Standard Yield" via staking | Medium |

## 1. What it is

A Hong Kong issued, one-troy-ounce gold token that sits inside a broader DeFi platform (spot, perpetuals, options, lending, and a companion stablecoin USDpm) rather than functioning as a standalone custody receipt. Its distinguishing feature against PAXG and XAUT is that it charges holders **no ongoing storage fee** and instead pays holders a staking yield, funding both from platform and physical-operations revenue. Founded 2023, on-chain platform from 2025.

## 2. Legal structure

**Confidence: Medium.** What a PGOLD holder legally owns is **undetermined**, and this is the single most important finding in the profile.

Marketing states PGOLD "provides you ownership of LBMA certified physical gold." The Terms of Use, which are the only accessible legal instrument, contain **no clause conferring title, beneficial interest, trust beneficiary status, creditor status, or a pro rata claim** over any gold. There is no whitepaper, no offering memorandum, no trust deed, and no redemption contract in the public record. The Terms are generic website terms, and they expressly state that access "does not create a client, advisory, fiduciary, brokerage, or customer relationship."

Governing law is Hong Kong SAR, with disputes going to confidential HKIAC arbitration, single arbitrator, class and representative actions waived.

Two similarly named entities appear and are never reconciled: "Pleasing International Limited" (in the GitBook and Terms contact block) and "Pleasing International (HK) Limited" (in Hong Kong registry data). **No primary document anywhere states who issues PGOLD.**

rwa.xyz tags account segregation as "Bankruptcy Remote," but Pleasing's own documents never use the words trust, SPV, segregated client accounts, or bankruptcy remote. That label is a third-party classification with no custody agreement or trust deed behind it.

## 3. Regulatory and compliance posture

**Confidence: Low.** The GitBook describes Pleasing Market as a "licensed modular RWA platform." **No regulator, jurisdiction, licence type, or licence number is given anywhere.**

Checked and not found:

- **Hong Kong SFC licence:** none identified, no licence number.
- **DPMS registration** (Dealers in Precious Metals and Stones, Customs and Excise Department, under the Anti-Money Laundering Ordinance): no Category A or Category B registration named. A Category B registrant would carry customer due diligence and record-keeping duties comparable to a financial institution.
- **LEI, CIK:** none.
- Any statement from SFC, Customs and Excise, or another Hong Kong regulator naming this issuer: none.

Cutting directly against the "licensed" claim, the Terms of Use state the site is not directed to persons in any jurisdiction where use would subject Pleasing to "licensing/registration **it does not hold**." That is close to an admission of unlicensed status in at least some markets.

Whether PGOLD is a security, a commodity, or an unregulated token under Hong Kong law cannot be established from public sources. There is a Prohibited Jurisdictions and Sanctions Policy and generic AML language, but **no documented KYC workflow**.

## 4. Custody and proof of reserve

**Confidence: Low to Medium.** This is the weakest area of the entire profile.

| Question | Answer |
|---|---|
| Custodian | **Not disclosed.** No vaulting company, bank, or dealer named. |
| Vault and city | **Not disclosed.** Only that redemption happens "in Hong Kong." |
| Allocated and segregated? | **Not confirmed.** No statement distinguishing bar-level allocation from an unallocated pool. |
| Bar serial numbers | **Not published.** |
| Proof of reserve feed | **None.** No on-chain attestation linking the 19,505 token supply to any custodian balance. |
| Reserve audit or attestation | **None.** No bullion auditor, no accounting firm, no stated frequency. |
| Smart contract audit | Beosin, 13 to 16 January 2026, on the **staking contract only**: 1 medium and 2 low severity issues, all fixed pre-publication. |

The distinction in that last row carries the weight: the only audit that exists assesses smart-contract security, **not the existence or sufficiency of the gold**. A reader skimming "audited" would draw the wrong conclusion.

## 5. Issuance

**Confidence: Low.** Subscription is in USDT, quoted as instant, with a minimum investment of 0 USDT and a 0% subscription fee.

Beyond that the mechanism is opaque. Not established: who may mint and on what authority; whether minting is permissioned to the issuer or triggered by user deposit; whether tokens are minted on demand or drawn from a pre-minted pool; and critically, **whether USDT subscription proceeds are actually used to buy physical gold, or how long any lag between subscription and physical backing runs.**

## 6. Redemption

**Confidence: Medium.** Physical redemption in Hong Kong, 0.50% one-time fee, quoted redemption time "Daily," with broader APAC logistics described as forthcoming.

The material restriction: redemption is available to "**institutional and qualified holders**," and **neither term is defined anywhere**. It is therefore unknown whether retail holders can redeem at all, or whether their only exit is selling into a secondary market that trades under $20 on a typical day. rwa.xyz confirms that bar sizes, minimum redemption thresholds, and lead times exist, but publishes none of them. No cash redemption or issuer buyback is documented.

## 7. Fees and revenue model

**Confidence: Medium.**

| Fee line | PGOLD |
|---|---|
| Subscription / mint | 0% (third-party analysis references unquantified percentage fees) |
| Ongoing custody / storage | **None.** "There are no ongoing custodian fees." |
| Gold deducted from backing | **No.** No rebase or gram haircut documented. |
| Physical redemption | 0.50% one-time, redistributed to PGOLD stakers |
| Transfer | None beyond network gas |

Stated issuer revenue streams: physical redemption and warehouse fees, institutional gold turnover from B2B circulation, on-chain trading and derivatives fees, and a Tokenization-as-a-Service and liquidity-sharing programme.

Holders can stake PGOLD for an advertised "5% Gold Standard Yield," funded from those same three fee pools. Whether the backing gold is lent, leased, or otherwise encumbered to generate yield is **never addressed by any source**. That is a silent gap, not a negative finding.

## 8. Token architecture

**Confidence: Medium.** Plain **ERC-20**. No permissioned standard: no ERC-3643 or T-REX, no ERC-1400, no ERC-1404, no identity registry.

Transfers are **permissionless** on supported chains, with documentation noting that specific addresses may be restricted or blacklisted in rare cases for security or legal compliance. Compliance is enforced at the **redemption** gate through KYC, not at the transfer layer.

Cross-chain movement ran on **LayerZero's OFT standard until June 2026**, when Pleasing deprecated LayerZero entirely and moved to **Chainlink CCIP** as exclusive interoperability infrastructure, also adopting **Chainlink Data Streams** for pricing. See Recent developments below.

The base token itself trades on DEXs. There is no separate wrapper. The most active venue is Uniswap V3 on Arbitrum, pair PGOLD/USDT0, with nine trading pairs in total. No centralised exchange listing was confirmed.

Not verified: whether the contract is upgradeable, admin key and multisig composition, and whether pause, mint, burn, or forced-transfer roles exist and who holds them.

## 9. Liquidity and market

**Confidence: Low.** The numbers do not sit comfortably together and should be treated as a live question rather than a settled fact.

Roughly $79M of stated market cap is supported by about $1.71M of on-chain liquidity and a 24h volume frequently under $20. That is an essentially dormant secondary market. Market cap figures also conflict across sources by an order of magnitude. No market maker is disclosed, and no split of DEX against CEX against OTC volume is published. Reported token price sits well above what the sources treat as spot, but with volume this thin the print is not a reliable premium signal and needs independent verification against the LBMA fix.

## 10. Distribution

**Confidence: Medium.** Direct through the Pleasing Market platform and dapp, through DeFi partner integrations and a tiered liquidity-sharing programme, and through institutional and OTC channels in Hong Kong. Target segments are crypto-native retail savers and traders, active DeFi participants, and precious-metals professionals such as vaults, refiners, dealers and market makers. Geography is Hong Kong and APAC, with Dubai named as an expansion target.

**No retail referral or affiliate programme, and no savings plan, recurring purchase, or systematic investment feature is documented.**

## 11. Recent developments

**3 June 2026: LayerZero deprecated, migrated to Chainlink CCIP.** Source is a Pleasing Market press release, so treat the framing as issuer marketing while the fact of the migration is reliable. CCIP becomes the exclusive cross-chain infrastructure for PGOLD and the USDpm synthetic dollar, with Chainlink Data Streams adopted for pricing. The release states roughly **$90M in TVL** and names chains as **Arbitrum, Ethereum, Pharos**. Named officer: **Leon Ma, CTO**.

**Context on the stated trigger.** The release cites "the recent $292 million LayerZero exploit." The underlying event was the **KelpDAO rsETH bridge exploit of 18 April 2026**: attackers forged a cross-chain message, causing the Ethereum-side adapter to release 116,500 rsETH from escrow with no corresponding burn, then borrowed against it on Aave. Root cause was a **1-of-1 DVN configuration** plus compromised RPC infrastructure, attributed to Lazarus Group. Independent analysis (OpenZeppelin, Chainalysis) found **no smart contract bug**: the failure was architectural and operational. LayerZero's core protocol was not breached, and LayerZero subsequently banned single-DVN configurations outright.

That distinction matters for how we read Pleasing. Describing it as "the LayerZero exploit" implies a protocol breach when it was an application-layer misconfiguration in someone else's bridge. It is the same pattern as the "licensed platform" claim: technically anchored to something real, phrased to carry more weight than the underlying fact supports.

Two observations worth carrying forward:

- **They adopted Chainlink for bridging and for price feeds, but not Chainlink Proof of Reserve.** Chainlink PoR is the one product in that suite that would directly address this issuer's largest disclosure gap. They integrated the parts that enable distribution and skipped the part that would enable verification.
- **The TVL figure moved from ~$79.8M to a claimed ~$90M** with no reconciliation, and ApeChain quietly disappears from the chain list. Both need checking against on-chain data rather than the release.

## 12. Relevance to Aurumix

Four things here are directly load-bearing for our design work.

**A third option on the custody fee.** We have been treating the custody fee as a binary: charge in grams and break the peg, or charge in cash. PGOLD takes a third route, charging holders **nothing** and recovering custody cost from redemption fees, institutional turnover, and trading revenue. That is worth putting on the table alongside our current cash-settlement recommendation, though note it depends on having a trading business attached, which Aurumix does not yet have.

**A live example of the exact anti-pattern we have flagged.** PGOLD advertises 5% yield on roughly $79M of assets, which is about $4M a year, funded from redemption fees on rare redemptions plus trading fees on a market doing under $20 a day. **The disclosed sources cannot plausibly fund the promised yield**, and because nothing is disclosed, the claim is unfalsifiable. This is precisely the "recycled fees" critique we have levelled at the ICS Dividend, running in public. It strengthens the case for the ORO and Monetary Metals real-yield route (handoff §6 item 8) and for funding any Aurumix dividend from a source we can actually evidence.

**Evidence against the premium thesis.** The client is banking on a 3 to 8% exchange premium to sustain spot and SIP demand (handoff §6 item 5). PGOLD demonstrates that a gold token can accumulate roughly $79M of AUM while having **no functioning secondary market at all**. Accumulating assets and having a liquid market that produces a reliable premium are separate problems, and the second does not follow from the first.

**Confirmation of the token standard reasoning.** PGOLD gets away with a plain permissionless ERC-20 because the token carries essentially no rights beyond a redemption claim, so there is nothing to lose on transfer. Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous DEX transfer. PGOLD is therefore not a counter-example to our ERC-3643 recommendation (handoff §6 item 7). It is a demonstration of what the loose end of the spectrum costs you.

**One caution on positioning.** PGOLD calls itself "licensed" without naming a regulator while its own terms concede it lacks licensing somewhere. Aurumix should describe its VARA status with precision at every stage, because that gap between marketing and legal language is exactly what diligence finds.

## 13. Open items for verification

- [ ] Resolve which entity issues PGOLD, and pull the full Companies Registry record from the Hong Kong government registry rather than a scraper site.
- [ ] Confirm the CCIP migration and current chain list against verified contract source and Chainlink's own integration registry, not the press release.
- [ ] Establish whether ApeChain deployment was retired or simply omitted from the June announcement.
- [ ] Verify contract upgradeability, admin keys and multisig composition on Arbiscan.
- [ ] Reconcile the market cap discrepancy (~$79M against a reported ~$3.95M FDV).
- [ ] Verify the price against the LBMA fix on the day to establish whether a real premium exists.
- [ ] Retrieve the GitBook "Audit Report" page contents, which sat behind a dynamic endpoint.
- [ ] Establish whether "qualified holder" is defined anywhere, including in the dapp onboarding flow.
