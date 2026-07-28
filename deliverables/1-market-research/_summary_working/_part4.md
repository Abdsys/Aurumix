### 4.4 Pleasing Gold (PGOLD)

| Field | Detail |
|---|---|
| Issuer | Two similarly named entities appear and are never reconciled: "Pleasing International Limited" in the GitBook and Terms contact block, and "Pleasing International (HK) Limited" in Hong Kong registry data, a private company limited by shares incorporated in 2023. No primary document states which entity issues PGOLD. Platform brand: Pleasing Market, formerly Pleasing Golden. Domicile Hong Kong SAR. Named officer: Leon Ma, Chief Technology Officer |
| Licence covering the token | None identified. The GitBook describes Pleasing Market as a "licensed modular RWA platform" without naming a regulator, jurisdiction, licence type or licence number. No Hong Kong SFC licence, no Dealers in Precious Metals and Stones (DPMS) Category A or B registration with Customs and Excise, no LEI and no CIK identified, and no Hong Kong regulator has published any statement naming this issuer |
| Assets under management | The issuer claimed roughly US$90M TVL in June 2026. Third-party data showed roughly US$79.8M. One source shows an unreconciled ~US$3.95M fully diluted valuation. Supply 19,505 PGOLD. Figures conflict across sources by an order of magnitude and should be treated as an open question |
| Backing | 1 token = 1 troy ounce, 99.99% purity, LBMA standard, 1:1. Marketing states PGOLD "provides you ownership of LBMA certified physical gold." The Terms of Use contain no clause conferring title, beneficial interest, trust beneficiary status, creditor status or a pro rata claim over any gold |
| Custody fee charged to holders | 0%. "There are no ongoing custodian fees." No rebase or gram haircut documented |
| Yield paid to holders | Advertised "5% Gold Standard Yield" via staking, funded from redemption and warehouse fees, institutional gold turnover and onchain trading and derivatives fees |
| Redemption | Physical redemption in Hong Kong only, 0.50% one-time fee, quoted redemption time "Daily," available to "institutional and qualified holders." Neither term is defined anywhere. Bar sizes, minimum thresholds and lead times exist but are not published. No cash redemption or issuer buyback documented |
| Token standard | Plain ERC-20 on Arbitrum (`0x3e76bb02286bfeaa89dd35f11253f2cbce634f91`), Ethereum and Pharos. ApeChain (`0x64ae250e044688ddd04262f17daca23c28d241c2`) was listed earlier and is not named in the June 2026 release. No permissioned standard: no ERC-3643 or T-REX, no ERC-1400, no ERC-1404, no identity registry. Transfers are permissionless, with documentation noting that specific addresses may be restricted or blacklisted in rare cases. Cross-chain via Chainlink CCIP since June 2026, LayerZero fully deprecated |
| Reserve verification | None published. No custodian named, no vault or city named beyond "redemption happens in Hong Kong," no bar serial numbers, no proof-of-reserve feed, no bullion auditor, no accounting firm, no stated frequency. The only audit that exists is a Beosin smart-contract audit of the staking contract, 13 to 16 January 2026, finding 1 medium and 2 low severity issues, all fixed before publication |

#### What it is

PGOLD is a Hong Kong issued, one-troy-ounce gold token that sits inside a broader DeFi platform rather than functioning as a standalone custody receipt. The platform offers spot, perpetuals, options and lending, plus a companion synthetic dollar called USDpm. The business was founded in 2023 and the onchain platform launched in 2025.

What distinguishes it from PAXG and XAU₮ is the combination of no ongoing storage fee and an advertised staking yield, funded from platform and physical-operations revenue. That combination makes it the most instructive negative case in this set for Aurumix specifically.

The scale is small relative to the leaders. Roughly 19,505 tokens are outstanding, and stated market capitalisation sits somewhere between the issuer's claimed US$90M and third-party figures near US$79.8M, with a third source showing a figure two orders of magnitude lower. Nothing in the public record reconciles them.

#### Legal structure and regulatory standing

What a PGOLD holder legally owns is undetermined, and that is the single most important finding in this profile. Marketing states that PGOLD "provides you ownership of LBMA certified physical gold." The Terms of Use, the only accessible legal instrument, contain no clause conferring title, beneficial interest, trust beneficiary status, creditor status or a pro rata claim over any gold. There is no whitepaper, no offering memorandum, no trust deed and no redemption contract in the public record.

The Terms are generic website terms and expressly state that access "does not create a client, advisory, fiduciary, brokerage, or customer relationship." Governing law is Hong Kong SAR, with disputes going to confidential HKIAC arbitration before a single arbitrator, and class and representative actions waived.

Set that against the three protocols above. XAU₮ asserts undivided ownership of specified bars inside a reasonable-assurance attestation. PAXG defines beneficial ownership of a pro rata portion of allocated gold in its terms. Kinesis writes legal and beneficial title in the holder with the issuer as bailee. PGOLD asserts ownership in marketing and confers nothing in the binding document. One third-party data provider tags account segregation as "bankruptcy remote," but Pleasing's own documents never use the words trust, SPV, segregated client accounts or bankruptcy remote, so that label rests on a classification with no custody agreement or trust deed behind it.

The regulatory position is similarly unsupported. The GitBook describes Pleasing Market as a "licensed modular RWA platform," and no regulator, jurisdiction, licence type or licence number appears anywhere. No SFC licence was identified and no licence number is given. No DPMS registration was named, which matters because a Category B registrant under the Anti-Money Laundering Ordinance would carry customer due diligence and record-keeping duties comparable to a financial institution. No LEI or CIK exists. No statement from the SFC, Customs and Excise or any other Hong Kong regulator names this issuer.

Cutting directly against the "licensed" claim, the Terms of Use state that the site is not directed to persons in any jurisdiction where use would subject Pleasing to "licensing/registration it does not hold." That is close to an admission of unlicensed status in at least some markets. Whether PGOLD is a security, a commodity or an unregulated token under Hong Kong law cannot be established from public sources. There is a Prohibited Jurisdictions and Sanctions Policy and generic AML language, but no documented KYC workflow.

#### Custody and reserve verification

This is the weakest area of the profile and there is very little to describe, which is itself the finding.

No custodian is disclosed. No vaulting company, bank or dealer is named. No vault or city is named beyond the statement that redemption happens in Hong Kong. There is no statement distinguishing bar-level allocation from an unallocated pool, so whether the gold is allocated and segregated is not confirmed. No bar serial numbers are published. There is no proof-of-reserve feed and no onchain attestation linking the 19,505 token supply to any custodian balance. There is no reserve audit or attestation of any kind: no bullion auditor, no accounting firm, no stated frequency.

The only audit that exists is a smart-contract audit by Beosin, conducted 13 to 16 January 2026, covering the staking contract only. It found 1 medium and 2 low severity issues, all fixed before publication. That is legitimate work and it assesses smart-contract security, not the existence or sufficiency of the gold. A reader skimming the word "audited" would draw exactly the wrong conclusion, and the issuer does nothing to prevent that.

One detail from the June 2026 infrastructure migration sharpens the point. Pleasing adopted Chainlink CCIP for bridging and Chainlink Data Streams for pricing, and did not adopt Chainlink Proof of Reserve. Proof of Reserve is the one product in that suite that would directly address the issuer's largest disclosure gap. Pleasing integrated the parts that enable distribution and skipped the part that would enable verification.

Issuance is equally opaque. Subscription is in USDT, quoted as instant, with a minimum investment of 0 USDT and a 0% subscription fee. Beyond that, it is not established who may mint and on what authority, whether minting is permissioned to the issuer or triggered by user deposit, whether tokens are minted on demand or drawn from a pre-minted pool, or, most importantly, whether USDT subscription proceeds are actually used to buy physical gold and how long any lag between subscription and physical backing runs.

#### Fees, revenue and redemption

| Fee line | PGOLD |
|---|---|
| Subscription / mint | 0%. Third-party analysis references unquantified percentage fees |
| Ongoing custody / storage | None. "There are no ongoing custodian fees" |
| Gold deducted from backing | No. No rebase or gram haircut documented |
| Physical redemption | 0.50% one-time, redistributed to PGOLD stakers |
| Transfer | None beyond network gas |

Stated issuer revenue streams are physical redemption and warehouse fees, institutional gold turnover from B2B circulation, onchain trading and derivatives fees, and a Tokenization-as-a-Service and liquidity-sharing programme. Holders can stake PGOLD for an advertised 5% Gold Standard Yield, funded from those same pools. Whether the backing gold is lent, leased or otherwise encumbered to generate yield is never addressed by any source. That is a silent gap rather than a negative finding: nothing establishes that the gold is encumbered, and nothing establishes that it is not.

Run the arithmetic on the yield. A 5% yield on roughly US$79M of assets is about US$4M a year. The disclosed funding sources are redemption fees on redemptions restricted to undefined "institutional and qualified holders," warehouse fees on an undisclosed vaulting arrangement, and trading fees on a market frequently doing under US$20 a day. A 0.50% redemption fee would require roughly US$800M of annual redemptions to fund US$4M on its own. There is no published figure for institutional turnover. The disclosed sources cannot plausibly fund the promised yield, and because nothing material is disclosed, the claim cannot be tested.

Redemption is physical only, in Hong Kong, at a 0.50% one-time fee, with a quoted redemption time of "Daily" and broader APAC logistics described as forthcoming. The material restriction is that redemption is available to "institutional and qualified holders" and neither term is defined anywhere. It is therefore unknown whether retail holders can redeem at all, or whether their only exit is selling into a secondary market that trades under US$20 on a typical day. No cash redemption or issuer buyback is documented.

#### Liquidity and distribution

The numbers do not sit comfortably together and should be treated as a live question rather than a settled fact. Roughly US$79M of stated market cap is supported by about US$1.71M of onchain liquidity and a 24h volume frequently under US$20. That is an essentially dormant secondary market. Market cap figures conflict across sources by an order of magnitude. No market maker is disclosed, and no split of DEX against CEX against OTC volume is published.

The reported token price sits well above what the sources treat as spot, but with volume this thin the print is not a reliable premium signal and would need independent verification against the LBMA fix on the day.

The base token trades on DEXs with no separate wrapper. The most active venue is Uniswap V3 on Arbitrum, pair PGOLD/USDT0, with nine trading pairs in total. No centralised exchange listing was confirmed. Contract upgradeability, admin key and multisig composition, and whether pause, mint, burn or forced-transfer roles exist and who holds them, are all unverified.

Distribution runs direct through the Pleasing Market platform and dapp, through DeFi partner integrations and a tiered liquidity-sharing programme, and through institutional and OTC channels in Hong Kong. Target segments are crypto-native retail savers and traders, active DeFi participants, and precious-metals professionals such as vaults, refiners, dealers and market makers. Geography is Hong Kong and APAC, with Dubai named as an expansion target. No retail referral or affiliate programme is documented, and no savings plan, recurring purchase or systematic investment feature exists.

On 3 June 2026 Pleasing deprecated LayerZero and migrated to Chainlink CCIP as exclusive cross-chain infrastructure for PGOLD and USDpm, also adopting Chainlink Data Streams for pricing. The source is a Pleasing Market press release, so the fact of the migration is reliable while the framing is issuer marketing. The release states roughly US$90M in TVL and names chains as Arbitrum, Ethereum and Pharos.

The stated trigger for that migration deserves scrutiny, because it illustrates the issuer's disclosure habits. The release cites "the recent $292 million LayerZero exploit." The underlying event was the KelpDAO rsETH bridge exploit of 18 April 2026, in which attackers forged a cross-chain message, causing the Ethereum-side adapter to release 116,500 rsETH from escrow with no corresponding burn, then borrowed against it on Aave. Root cause was a 1-of-1 Decentralized Verifier Network configuration plus compromised RPC infrastructure, attributed to Lazarus Group. Independent analysis by OpenZeppelin and Chainalysis found no smart contract bug: the failure was architectural and operational. LayerZero's core protocol was not breached, and LayerZero subsequently banned single-DVN configurations outright. Describing this as "the LayerZero exploit" implies a protocol breach when it was an application-layer misconfiguration in someone else's bridge. Same pattern as the "licensed platform" claim: technically anchored to something real, phrased to carry more weight than the underlying fact supports.

Two further observations from that release. The TVL figure moved from roughly US$79.8M to a claimed US$90M with no reconciliation, and ApeChain quietly disappeared from the chain list without any statement that the deployment was retired.

#### Relevance to Aurumix

PGOLD is the live example of the anti-pattern Aurumix risks repeating, and the closest structural analogue to Aurumix's proposed combination of zero custody fee plus advertised yield plus limited redemption. Four things here are directly load-bearing.

**A third option on the custody fee, with a caveat attached.** The custody fee has been treated as a binary: charge in grams and break the peg, or charge in cash. PGOLD takes a third route, charging holders nothing and recovering custody cost from redemption fees, institutional turnover and trading revenue. That belongs on the table alongside the cash-settlement recommendation. The caveat is that it depends on having a trading business attached, which Aurumix does not have. PGOLD's version also carries a specific weakness the leaders do not share: XAU₮ and PAXG fund free storage from large, verifiable adjacent businesses, whereas PGOLD funds it from revenue lines that are not disclosed in any quantified form. Same shape, entirely different evidence base.

**A live example of the exact anti-pattern flagged for the ICS Dividend.** PGOLD advertises a 5% yield on roughly US$79M of assets, which is about US$4M a year, funded from redemption fees on rare and restricted redemptions plus trading fees on a market doing under US$20 a day. A 0.50% redemption fee alone would need roughly US$800M of annual redemptions to cover that US$4M, against redemptions restricted to undefined "institutional and qualified holders." The disclosed sources cannot plausibly fund the promised yield, and because nothing is disclosed, the claim is unfalsifiable. This is precisely the recycled-fees critique of the ICS Dividend, running in public, on a product with the same architecture Aurumix is proposing.

Read PGOLD and Kinesis together and the picture is complete. Kinesis is honest about the mechanism and misleading about the headline: its fee sources genuinely fund what it pays, because what it pays is only about 0.10% against an advertised 2.05%. PGOLD is unclear about both the mechanism and the headline. The anti-pattern is not fee-recycling as such. It is fee-recycling combined with a headline percentage the fees cannot support. Fund any Aurumix dividend from a source it can evidence, which points to external yield or the credit facility spread rather than recycled platform fees.

There is a second-order risk worth naming. The gap PGOLD leaves open, whether backing gold is lent, leased or encumbered to generate the advertised yield, is exactly the question a regulator or a journalist will ask Aurumix about the ICS Dividend. Answer it before it is asked, in writing, and be able to point to an attestation confirming the reserves are unencumbered. XAU₮ and PAXG both leave their gold unencumbered and pay nothing. PGOLD promises a return and says nothing about encumbrance. Aurumix cannot occupy the middle without disclosure.

**Evidence against the premium thesis.** PGOLD shows that a gold token can accumulate roughly US$79M of AUM while having no functioning secondary market at all. Accumulating assets and having a liquid market that produces a reliable premium are separate problems, and the second does not follow from the first. Its reported price sits above spot, but on sub-US$20 daily volume that print carries no information. If Aurumix's revenue model depends on a 3–8% exchange premium, PGOLD shows what the illiquid end of the spectrum actually produces: an unverifiable price on a dormant market. XAU₮ and PAXG show what the liquid end produces: par. Neither end delivers a durable, evidenced premium.

**Confirmation of the token standard reasoning.** PGOLD gets away with a plain permissionless ERC-20 because the token carries essentially no rights beyond a redemption claim most holders probably cannot exercise, so there is nothing to lose on transfer. Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous DEX transfer. PGOLD is not a counter-example to the ERC-3643 recommendation. It is a demonstration of what the loose end of the spectrum costs.

**One caution on positioning, and it is the most transferable lesson in the profile.** PGOLD calls itself "licensed" without naming a regulator while its own terms concede it lacks licensing somewhere. It describes an application-layer bridge misconfiguration as a protocol exploit. It asserts ownership of physical gold in marketing while conferring no rights in its binding terms. Each claim is anchored to something real and phrased to carry more weight than the underlying fact supports. Aurumix should describe its VARA status with precision at every stage, in every channel, including agent scripts, because that gap between marketing and legal language is exactly what diligence finds and exactly what a mis-selling complaint is built on.

Takeaways for Aurumix:

- Do not advertise a yield percentage the disclosed revenue lines cannot fund. PGOLD's 5% on US$79M requires roughly US$4M a year from redemption and trading revenue that does not visibly exist.
- Publish the funding source and the denominator for any distribution, and state in writing whether the reserve gold is encumbered, lent or leased.
- Never let marketing confer rights the terms do not. PGOLD claims ownership of LBMA gold and its Terms of Use confer no title, no beneficial interest and no pro rata claim.
- Define every eligibility term used in a redemption or buyback clause. "Institutional and qualified holders" is undefined in PGOLD's documents, which makes the redemption right unusable and unassessable.
- Keep smart-contract audits and reserve attestations separately and visibly labelled. PGOLD has one Beosin audit of a staking contract and no reserve verification of any kind, and the word "audited" does the work of both.
- Integrate proof of reserve, not only the infrastructure that enables distribution. Adopting Chainlink for bridging and pricing while skipping Chainlink Proof of Reserve is a visible choice, and it reads exactly as it looks.
- State the VARA position precisely everywhere, including agent-facing material. Imprecise licensing language is the single most consistent tell across this profile.

---

