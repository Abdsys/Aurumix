### 5.1 Perth Mint Gold Token (PMGT)

| Field | Detail |
|---|---|
| Issuer | Trovio Operating Pty Ltd, ACN 622 224 024 / ABN 33 622 224 024, Australia. Registered with ASIC 12 October 2017. Formerly InfiniGold. Branding licence from Gold Corporation |
| Licence covering the token | None identified. No AFS licence; not a registered financial product or managed investment scheme |
| Peak assets under management | About 1,195 tokens (1,195 fine troy ounces, roughly A$3.5M); US$2.54M market capitalisation on 15 March 2023. Residual supply 0.967 PMGT |
| Backing | 1 PMGT = 1 fine troy ounce, via a Perth Mint GoldPass certificate, itself a claim on Gold Corporation, itself backed by metal in Perth Mint vaults |
| Custody fee charged to holders | 0%. No subscription, storage, management or redemption fee at the token layer |
| Yield paid to holders | None |
| Redemption | Burn PMGT for GoldPass certificates, then transact with the Perth Mint for fiat or bullion. Gold never directly redeemable from the token. Downstream GoldPass fees applied |
| Token standard | ERC-20, Ethereum only, with Blacklist and Whitelist contracts behind an upgradeable proxy. `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf` |
| Reserve verification | Live issuer-hosted feed at `pmgt.perthmint.com`, branded "Realtime Audit". No named-firm reserve attestation; no smart contract audit located. Feed now offline |
| Ceased operating | Trading ceased 30 June 2023 on delisting by Independent Reserve. Discontinued 31 October 2023; contract deactivated 1 November 2023 |
| What holders received | Sellers before 30 June 2023 got roughly the gold price. Converters by 31 October 2023 kept a claim on a closing platform. Non-actors were force-sold on 1 November 2023 at that day's price |

#### What it is

PMGT launched in October 2019, issued by InfiniGold, renamed Trovio in February 2021, under a branding licence from The Perth Mint. One token, one fine troy ounce.

The structure wrapped an existing product. The Mint already ran GoldPass, a digital certificate app; Trovio held GoldPass certificates and minted PMGT against them. The Mint stored the gold and issued the certificates. It did not issue the token. That distinction decides everything that follows. The marketing surface said "Perth Mint": government-owned, central-bank-grade vaults, a state guarantee. The legal reality was a small Sydney fintech operating under a licence the Mint could walk away from. It did.

Issuance required a GoldPass account first, so a verified precious metals account, verified ID and a linked Ethereum address. PMGT was never open-access. Its addressable market was capped at roughly 26,700 existing GoldPass accounts, and it converted about 1,195 ounces from that base in four years.

#### Legal structure and regulatory standing

A holder's claim ran through four layers. The token was a claim, not the asset. Beneath it, beneficial ownership of a GoldPass certificate held by Trovio Custodians Pty Ltd (ACN 622 220 517) as custodian and bare trustee under a Custody Deed, with the whitepaper stating certificates were "recorded separately by Trovio Custodians and there is no pooling, combinations or comingling of Certificates". Beneath that, the certificate, a contractual claim on Gold Corporation. Beneath that, metal.

On paper this beats most tokenised gold: a real bare trust, a separate custodian entity, an explicit no-commingling covenant. But there was no independent trustee. Trovio Custodians was a related-party SPV of the issuer, its ACN sequential to the operating company (622 220 517 against 622 224 024). The holder's protection depended on an affiliate of the issuer.

The headline trust signal was the Western Australian government guarantee. The whitepaper says GoldPass certificates are backed by gold "with the weight and purity of every ounce guaranteed by the Government of Western Australia", citing section 22 of the Gold Corporation Act 1987 (WA). The statutory text guarantees "the cash equivalent of gold due, payable and deliverable by Gold Corporation, the Mint or GoldCorp under this Act". Read precisely, the Treasurer guarantees obligations of Gold Corporation. Trovio is not Gold Corporation, and PMGT was not an obligation of Gold Corporation. The Mint's own guarantee page describes cover for "customers and stakeholders of The Perth Mint enterprise" and never mentions tokens. The guarantee attached one layer below the token, reachable only derivatively, and if Trovio failed or declined to act it did nothing for a holder as a holder. No published legal analysis of this question exists.

The regulatory record is empty in both directions. No AFS licence identified, no ASIC enforcement action against any Trovio entity between 2019 and July 2026, and AUSTRAC never touched Trovio: every AUSTRAC step named Gold Corporation. Trovio Operating remains registered and active, next review due 12 October 2026. The issuer is alive and the token is dead. Nothing forced this.

#### Custody and reserve verification

Gold Corporation held the metal in Perth; Trovio Custodians held the certificates as bare trustee. The whitepaper asserts no pooling or commingling of certificates, but whether the underlying vault gold was allocated per certificate was never disclosed, and no serial-numbered bar list was published.

The reserve feed was PMGT's genuine strength. A real-time page at `pmgt.perthmint.com` published the GoldPass certificates backing supply, so a holder could check total supply against certificates on demand: more useful than most competitors offered. The issuer branded it "Realtime Audit", and that name was wrong. It was a live self-published data feed, not an attestation, and no named accounting firm ever signed a report confirming certificates matched supply. No smart contract audit report from any named firm was located either, though the contracts were open-sourced under MIT.

The feed is dead. `pmgt.perthmint.com` returns connection refused. Proof of reserve hosted on issuer infrastructure lasts exactly as long as the issuer keeps paying for hosting, so every historical verification claim PMGT made is now unverifiable by anyone.

#### Fees, revenue and redemption

PMGT charged holders nothing: no minting fee, no storage fee, no redemption fee at the token layer, no transfer fee beyond gas. No yield to fund and no fee line to fund it with. Against roughly A$3.5M of assets under management, that schedule generated approximately nothing while consuming engineering, compliance, custody and market-making cost. When the Perth Mint relationship turned into a liability, no revenue stream existed to defend the product in a strategy meeting.

Redemption required two hops, both KYC-gated, both involving an entity other than the issuer: burn for certificates, then transact with the Mint. The whitepaper carried an explicit continuity assurance: "If the Licence Agreement is terminated, Trovio would no longer be able to issue PMGT. Notwithstanding this, a token holder will still be able to redeem their existing PMGT for Certificates which can then be redeemed for gold with The Perth Mint."

That failed because it assumed GoldPass would outlive PMGT. The Mint shut GoldPass on an overlapping timetable: around 18 April 2023 it closed zero-balance accounts immediately, barred active accounts from transacting at the end of May, and gave holders until the end of November to empty their accounts, warning that physical gold requests faced "significant delays". Holders were told to redeem into a destination being dismantled at the same time.

One fee detail deserves attention. From November 2023, manual redemption pays "the backdated gold price minus any fees owing". Fees advertised as nil throughout the product's life reappear at the exit. Whether it still works in July 2026 is doubtful: `pmgt.io` returns connection refused, and the FAQ warned that after 1 November 2023 Trovio "may no longer be able to assist with manual withdrawals". The Perth Mint's live website still directs holders to pmgt.io. The domain does not resolve.

#### Liquidity and distribution

PMGT peaked at roughly 1,195 tokens and about US$2.54M in March 2023, after three and a half years. Independent Reserve was the primary venue, where an undisclosed market maker provided exit liquidity. Daily volume was never published, but on a US$2.5M capitalisation against a single venue it was necessarily negligible. Residual onchain supply is about 0.967 PMGT.

Distribution was self-serve, gated behind an existing GoldPass account, Australia and the US only. No savings plan, no recurring purchase, no referral scheme, no agent network. PMGT was a conversion utility for people who had already solved the hard problem of buying gold.

Read as an experiment, the result is stark. Four years, a government-owned counterparty, a statutory sovereign guarantee, world-class vaults, a genuine real-time reserve feed and a clean compliance record produced US$2.5M of assets under management. Every trust signal a gold token could want, and the market did not come.

#### The causation, stated plainly

PMGT is widely described as a casualty of AUSTRAC enforcement against the Perth Mint and the Shanghai Gold Exchange doping scandal. The dated record does not support that.

| Event | Date |
|---|---|
| The Perth Mint begins discussions with Trovio to exit PMGT | Early 2022 |
| Internal Mint plan to "fully terminate" GoldPass by August 2023 | May 2022 |
| AUSTRAC's earliest public action: order to appoint an external auditor | 30 August 2022 |
| Trovio announces it will no longer support PMGT | 1 March 2023 |
| ABC *Four Corners* "Tainted Gold" broadcast on the Shanghai Gold Exchange bars | 6 March 2023 |
| AUSTRAC accepts an Enforceable Undertaking from Gold Corporation | 23 November 2023 |
| AUSTRAC concludes the Enforceable Undertaking, the Mint cleared, no fine ever imposed | 22 July 2025 |

The Mint decided to exit in early 2022, before any public AUSTRAC action and roughly a year before the broadcast. The enforcement action that supposedly killed the token began after the exit decision and concluded on 22 July 2025 with AUSTRAC satisfied that Gold Corporation had met its obligations, roughly 70,000 customer accounts remediated, and no penalty at any stage. The Shanghai Gold Exchange matter produced no recall.

The cause was commercial abandonment: a revenue-free product that a state-owned licensor no longer wanted, discontinued while the licensor was distracted by unrelated compliance problems. The regulatory and reputational events were accelerant and cover story. The strongest evidence is Trovio's own conduct. Its 1 March 2023 statement blamed "ongoing investigations into alleged breaches [by Perth Mint] with AUSTRAC and US State Regulation", and was later edited to say the decision was made "due to several factors after a number of years in operation". The second version is closer to the truth.

No wind-down plan existed in advance. The only continuity provision was that single whitepaper sentence, and it depended on GoldPass surviving. No insolvency provision, contingency plan, wind-down procedure or trigger framework appeared in the whitepaper, terms or FAQ before March 2023. Deadlines were set after the decision, by the parties who made it, and at least one deadline structure was published a month after the exit announcement.

#### Relevance to Aurumix

PMGT is the sharpest control experiment available. It had everything Aurumix is trying to buy with custody quality: a government-owned counterparty, a statutory sovereign guarantee, central-bank-grade vaults, a bare trust with no commingling, a live proof-of-reserve feed, a clean compliance record. It died anyway, in four months, because it had no revenue and depended on someone else's platform.

**A revenue line is a survival feature.** PMGT charged nothing at any point, so it had no profit and loss line, no internal advocate and no defence when the licensor lost interest. This is the strongest available argument against charging holders nothing and recovering cost elsewhere. Aurumix's SIP-plus-fee model gives someone inside the business a reason to fight for the product in a budget meeting. PMGT had no such person, and a product that reached US$2.5M in four years with a sovereign guarantee behind it is the evidence.

**Redemption that routes through a third party is not redemption.** The whitepaper promised holders could always redeem to certificates and then to gold. That promise was void the moment the Mint wound down GoldPass. Aurumix's exit is a cash buyback and the obligor is Aurumix itself, which is more honest than a two-hop chain but concentrates the entire exit path on one balance sheet. Aurumix should answer in writing: who executes the buyback if Aurumix stops operating, and out of what? PMGT's answer was "GoldPass", and GoldPass closed.

**A named sovereign or institutional guarantee probably does not reach token holders.** Section 22 guaranteed Gold Corporation's obligations, not Trovio's, and the Mint's own guarantee page never mentioned tokens. If Aurumix cites a vault operator's, insurer's or authority's standing in marketing, it should state precisely whose obligation is guaranteed and confirm it is the obligation owed to the token holder.

Four further transfers:

- **Custody excellence does not create demand. Distribution does.** PMGT had best-in-class custody and no savings plan, no agent network, no referral scheme. Aurumix's agent network and monthly SIP are the parts of its model this research most supports.
- **Do not call a data feed an audit.** PMGT branded issuer self-publication as "Realtime Audit", published no attestation from a named firm, and lost the feed with its hosting. Aurumix should commission a named third-party attestation, publish a bar list, and host the artefacts somewhere that survives the company: IPFS with onchain content hashes, a registry filing, or the attestor's own site.
- **Appoint an independent professional trustee, not a related-party SPV.** PMGT's bare trustee was an affiliate of the issuer with a sequential company number. That structure looks like protection and is not.
- **Never force-convert holders to cash without an election period.** Non-acting holders were sold out on 1 November 2023 at that day's price, without consent, on a date the issuer chose. They were made economically whole only because gold rose through 2023. The same mechanism in a drawdown converts savers to cash at the bottom and removes their ability to wait. Holders lost optionality, and the fact that it did not cost them was a market outcome, not a governance one. If forced conversion is ever unavoidable for Aurumix, the pricing methodology should be agreed in advance rather than the date picked by the issuer.

The permissioned architecture is worth reading carefully too. PMGT ran an upgradeable proxy plus address-level Blacklist and Whitelist contracts, so the issuer held unilateral technical control from deployment in 2019. Deactivating the contract on 1 November 2023 exercised powers it had held for four years. Aurumix's ERC-3643 lean gives it the same powers. The design question is not whether to hold them, but what binds the issuer's use of them, because the code plainly will not.
