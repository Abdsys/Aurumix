### 5.1 Perth Mint Gold Token (PMGT)

| Field | Detail |
|---|---|
| Issuer | Trovio Operating Pty Ltd, ACN 622 224 024 / ABN 33 622 224 024, an Australian private company registered with ASIC on 12 October 2017, main business location NSW 2000. Formerly InfiniGold Operating Pty Ltd. Marketed as "The Perth Mint Gold Token" under a branding licence from Gold Corporation |
| Licence covering the token | None identified. No Australian Financial Services Licence was found for Trovio in respect of PMGT, and PMGT was not registered as a financial product or managed investment scheme. The token was positioned as a non-financial-product utility token |
| Peak assets under management | Approximately 1,195 tokens (1,195 fine troy ounces, about A$3.5M), with a market capitalisation of roughly US$2.54M reported on 15 March 2023. Residual supply today is about 0.967 PMGT |
| Backing | 1 PMGT = 1 fine troy ounce. Each token was backed by a Perth Mint GoldPass digital certificate, itself a contractual claim against Gold Corporation, itself backed by physical gold in Perth Mint vaults in Western Australia |
| Custody fee charged to holders | 0%. No subscription fee, no storage fee, no management fee, no redemption fee at the token layer |
| Yield paid to holders | None |
| Redemption | Burn PMGT, receive GoldPass certificates into a verified GoldPass account, then transact with the Perth Mint to convert to fiat or request bullion. Physical gold was never directly redeemable from the token. No minimum published. No redemption fee at the token layer, though standard GoldPass fees applied downstream |
| Token standard | ERC-20 on Ethereum only, with separate Blacklist and Whitelist contracts governing transfers. Deployed behind an OpenZeppelin upgradeable proxy. Token contract `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf` |
| Reserve verification | A live proof-of-reserve feed at `pmgt.perthmint.com` published the GoldPass certificates backing supply. The issuer branded it "Realtime Audit". No third-party reserve attestation by a named accounting firm was published, and no smart contract audit report was located. The feed is now offline |
| Ceased operating | Trading ceased 30 June 2023 when Independent Reserve delisted the token. The token was formally discontinued on 31 October 2023 and the smart contract was deactivated on 1 November 2023 |
| What holders received | Holders who sold on Independent Reserve before 30 June 2023 realised approximately the gold price against a market maker. Holders who exchanged into GoldPass certificates by 31 October 2023 kept a gold claim into a platform that was itself closing. Holders who did nothing were force-sold on 1 November 2023 at that day's gold price, without consenting, on a date the issuer chose. Stragglers face a manual process: KYC, ID verification, bank verification, proof of Ethereum address control, and "the backdated gold price minus any fees owing" |

#### What it is

PMGT was an Ethereum token launched in October 2019 by InfiniGold, renamed Trovio in February 2021, under a branding licence agreement with The Perth Mint. One token represented one fine troy ounce of gold.

The structure wrapped an existing product rather than creating a gold programme of its own. The Perth Mint already ran GoldPass, a digital gold certificate app. Trovio held GoldPass certificates and minted PMGT against them. The Perth Mint stored the gold and issued the certificates. It did not issue the token.

That distinction is the whole story. The marketing surface said "Perth Mint": a government-owned mint, central-bank-grade vaults, a state guarantee. The legal reality was a small Sydney fintech running a token under a licence the Mint could walk away from. It did.

Issuance was gated on being a GoldPass customer first, which required a verified precious metals account, verified ID and a linked Ethereum address. PMGT was never open-access. Its addressable market was capped at roughly 26,700 existing GoldPass accounts, and it converted about 1,195 ounces from that base over four years.

#### Legal structure and regulatory standing

A PMGT holder's claim ran through four layers. The token was a claim, not the asset. Beneath it sat beneficial ownership of a GoldPass certificate, held by Trovio Custodians Pty Ltd (ACN 622 220 517) as custodian and bare trustee under a Custody Deed. The whitepaper states certificates were "recorded separately by Trovio Custodians and there is no pooling, combinations or comingling of Certificates". Beneath that sat the certificate itself, a contractual claim against Gold Corporation, and beneath that the physical metal.

On paper this is better than most tokenised gold: a real bare trust with a separate custodian entity and an explicit no-commingling covenant, so certificates should have been insolvency-remote from Trovio's operating company. There was, however, no independent trustee. The bare trustee was Trovio Custodians Pty Ltd, a related-party special-purpose vehicle of the issuer, incorporated with an ACN sequential to the operating company (622 220 517 against 622 224 024). No professional third-party trustee was involved at any point. The holder's protection depended on an affiliate of the issuer.

PMGT's central marketing claim was the Western Australian government guarantee. The whitepaper says GoldPass certificates are backed by gold "with the weight and purity of every ounce guaranteed by the Government of Western Australia", citing section 22 of the Gold Corporation Act 1987 (WA). The statutory text guarantees "the cash equivalent of gold due, payable and deliverable by Gold Corporation, the Mint or GoldCorp under this Act". Read precisely, the Treasurer guarantees obligations of Gold Corporation. Trovio is not Gold Corporation, and PMGT was not an obligation of Gold Corporation. The Perth Mint's own government-guarantee page describes the guarantee as covering "customers and stakeholders of The Perth Mint enterprise" and makes no mention of cryptocurrencies, tokens or third-party products.

The guarantee therefore attached one layer below the token, to Gold Corporation's obligation under the certificate. A token holder could reach it only derivatively, through Trovio Custodians and through the certificate. If Trovio failed or simply declined to act, the guarantee did nothing for a holder as a holder. No published legal analysis of this question exists, which is notable given it was the product's headline trust signal.

On the regulatory side, the record is empty in both directions. No AFS licence was identified for the token. No ASIC enforcement action against any Trovio entity was found between 2019 and July 2026. AUSTRAC never took action against Trovio: every AUSTRAC step named Gold Corporation. Trovio Operating remains registered and active on the ASIC register, with its next review due 12 October 2026. The issuer is alive and the token is dead. Nothing forced this outcome.

#### Custody and reserve verification

Gold Corporation held the physical metal in Perth. Trovio Custodians held the certificates as bare trustee. The whitepaper asserts no pooling or commingling of certificates, but whether the underlying vault gold was allocated per certificate was never disclosed, and no serial-numbered bar list was ever published.

PMGT's genuine strength was its reserve feed. A real-time page at `pmgt.perthmint.com` published the GoldPass certificates backing supply, so a holder could verify total token supply against certificates on demand. This was a more useful disclosure than most competitors offered. The issuer branded it "Realtime Audit", and that name was wrong. It was a live self-published data feed from the issuer, not an attestation. No named accounting firm ever signed a report confirming that certificates matched supply. Separately, no smart contract audit report from any named firm was located, although the contracts were open-sourced under an MIT licence.

The feed is now dead. `pmgt.perthmint.com` returns connection refused. A proof-of-reserve system hosted on issuer infrastructure lasts exactly as long as the issuer keeps paying for hosting. Every historical verification claim PMGT made is now unverifiable by anyone.

#### Fees, revenue and redemption

PMGT charged holders nothing. No minting fee, no ongoing custody or storage fee, no redemption fee at the token layer, no transfer fee beyond Ethereum gas. There was no yield to fund and no fee line to fund it with.

That produced a product with no revenue at the token layer at all. Against roughly A$3.5M of assets under management, a zero fee schedule generated approximately nothing for Trovio while consuming engineering, compliance, custody and market-making cost. Trovio's rationale was presumably strategic: build tokenisation infrastructure and expand into other commodities, which was the point of the 2021 rebrand from InfiniGold. When the Perth Mint relationship turned into a liability, no revenue stream existed to defend the product's existence in a strategy meeting.

The redemption design required two hops, both KYC-gated, both involving an entity other than the token issuer. Burn PMGT for certificates, then transact with the Mint. The whitepaper carried an explicit continuity assurance: "If the Licence Agreement is terminated, Trovio would no longer be able to issue PMGT. Notwithstanding this, a token holder will still be able to redeem their existing PMGT for Certificates which can then be redeemed for gold with The Perth Mint."

That assurance failed, because it assumed GoldPass would outlive PMGT. The Perth Mint shut GoldPass down on an overlapping timetable. Around 18 April 2023 it closed zero-balance accounts immediately, barred active accounts from further transactions at the end of May, and gave holders until the end of November to empty their accounts, warning that physical gold requests faced "significant delays" subject to stock availability. Holders were being told to redeem into a destination that was being dismantled at the same time.

One fee detail deserves attention. From November 2023, manual redemption pays "the backdated gold price minus any fees owing". Fees advertised as nil throughout the product's life reappear at the exit. Whether manual redemption still functions in July 2026 is doubtful: `pmgt.io` returns connection refused, and the FAQ language was conditional, warning that after 1 November 2023 Trovio "may no longer be able to assist with manual withdrawals". The Perth Mint's live website still directs PMGT holders to visit pmgt.io. The domain does not resolve.

#### Liquidity and distribution

PMGT peaked at roughly 1,195 tokens and a market capitalisation of about US$2.54M in March 2023, after three and a half years of operation. Independent Reserve in Australia was the primary venue, where an undisclosed PMGT market maker provided the exit liquidity. Typical daily volume was never published, but on a US$2.5M capitalisation against a single primary venue it was necessarily negligible. Residual onchain supply is about 0.967 PMGT.

Distribution was self-serve and gated behind an existing GoldPass account, in Australia and the US only. There was no savings plan, no recurring purchase mechanism, no referral scheme and no agent network of any kind. PMGT was a conversion utility offered to people who had already solved the hard problem of buying gold.

Read as an experiment, the result is stark. Four years of operation, a government-owned counterparty, a statutory sovereign guarantee, world-class vaults, a genuine real-time reserve feed and a clean compliance record produced US$2.5M of assets under management. Every trust signal a gold token could want, and the market did not come.

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

The Perth Mint decided to exit PMGT in early 2022, before any public AUSTRAC action and roughly a year before the Shanghai Gold Exchange broadcast. The enforcement action that supposedly killed the token began after the exit decision and concluded on 22 July 2025 with AUSTRAC satisfied that Gold Corporation had met its obligations, roughly 70,000 customer accounts remediated, and no penalty at any stage. The Shanghai Gold Exchange matter produced no recall.

The cause was commercial abandonment. A revenue-free product that a state-owned licensor decided it no longer wanted was discontinued at a moment when the licensor was distracted by unrelated compliance problems. The regulatory and reputational events were accelerant and cover story. The strongest evidence is Trovio's own conduct: its 1 March 2023 statement blamed "ongoing investigations into alleged breaches [by Perth Mint] with AUSTRAC and US State Regulation", and that statement was subsequently edited to say the decision was made "due to several factors after a number of years in operation". The second version is closer to the truth.

No wind-down plan existed in advance. The only continuity provision was the single whitepaper sentence promising redemption to certificates, and it depended on GoldPass surviving. No insolvency provision, contingency plan, wind-down procedure or trigger framework was published before March 2023 in the whitepaper, the terms and conditions or the FAQ. Deadlines were set after the decision, by the parties who made the decision, and at least one deadline structure was published a month after the exit announcement.

#### Relevance to Aurumix

PMGT is the sharpest control experiment in this landscape. It had everything Aurumix is trying to buy with custody quality: a government-owned counterparty, a statutory sovereign guarantee, central-bank-grade vaults, a bare trust with no commingling, a live proof-of-reserve feed and a clean compliance record of its own. It died anyway, in four months, because it had no revenue and depended on someone else's platform.

**A revenue line is a survival feature.** PMGT charged nothing at any point, so it had no profit and loss line, no internal advocate and no defence when the licensor lost interest. This is the strongest available argument against charging holders nothing and recovering cost elsewhere. Aurumix's SIP-plus-fee model gives someone inside the business a reason to fight for the product in a budget meeting. PMGT had no such person, and the product that reached US$2.5M in four years with a sovereign guarantee behind it is the evidence.

**Redemption that routes through a third party is not redemption.** PMGT's whitepaper promised holders could always redeem to certificates and then to gold. That promise was void the moment the Mint wound down GoldPass. Aurumix's exit is a cash buyback and the buyback obligor is Aurumix itself, which is more honest than a two-hop chain but concentrates the entire exit path on one balance sheet. Aurumix should answer in writing: who executes the buyback if Aurumix stops operating, and out of what? PMGT's answer was "GoldPass", and GoldPass closed.

**A named sovereign or institutional guarantee probably does not reach token holders.** Section 22 guaranteed Gold Corporation's obligations, not Trovio's, and the Mint's own guarantee page never mentioned tokens. If Aurumix ever cites a vault operator's, insurer's or authority's standing in marketing, it should state precisely whose obligation is guaranteed and confirm that it is the obligation owed to the token holder.

Four further transfers:

- **Custody excellence does not create demand. Distribution does.** PMGT had best-in-class custody and no savings plan, no agent network and no referral scheme. Aurumix's agent network and monthly SIP are the parts of its model this landscape most supports. Do not let the gold infrastructure build crowd out the distribution build.
- **Do not call a data feed an audit.** PMGT branded issuer self-publication as "Realtime Audit", published no reserve attestation from a named firm, and lost the feed with its hosting. Aurumix should commission a named third-party attestation, publish a bar list, and host attestation artefacts somewhere that survives the company: IPFS with onchain content hashes, a registry filing, or the attestor's own site.
- **Appoint an independent professional trustee, not a related-party SPV.** PMGT's bare trustee was an affiliate of the issuer with a sequential company number. That structure looks like protection and is not.
- **Never force-convert holders to cash without an election period.** Non-acting PMGT holders were sold out on 1 November 2023 at that day's price, without consent, on a date the issuer chose. They were made economically whole only because gold rose through 2023. The same mechanism in a drawdown converts savers to cash at the bottom and removes their ability to wait. Holders lost optionality, and the fact that it did not cost them was a market outcome, not a governance one. If forced conversion is ever unavoidable for Aurumix, the pricing methodology should be agreed in advance rather than the date being picked by the issuer.

A permissioned architecture is also worth reading carefully here. PMGT ran an upgradeable OpenZeppelin proxy plus address-level Blacklist and Whitelist contracts, so the issuer held unilateral technical control from deployment in 2019. When Trovio deactivated the contract on 1 November 2023, it was exercising powers it had held for four years. Aurumix's ERC-3643 lean gives it the same powers. The design question is not whether to hold them, but what binds the issuer's use of them, because the code plainly will not.

---

### 5.2 Digix Gold Token (DGX) and DigixDAO (DGD)

| Field | Detail |
|---|---|
| Issuer | A group of Singapore entities, all now struck off. Legal title to the gold sat in Digix Physicals Pte. Ltd., UEN 201724269N, incorporated 25 August 2017 under SSIC 52101 "General Warehousing" with stated activity "HOLD PHYSICAL ASSETS". Parent: Digix Holdings Private Limited, UEN 201724450M, incorporated 28 August 2017. Also Digix Markets Pte. Ltd. (UEN 201906348R), Digix Technologies Private Limited (UEN 201713056E) and Digix Core (UEN 53369203B). All shared one address at 6 Eu Tong Sen Street, #06-09, The Central, Singapore 059817 |
| Licence covering the token | None identified. Digix Holdings withdrew its Payment Services Act licensing in September 2022. The licence class and any MAS reference number were never disclosed, so whether Digix held a full licence, an exemption, or a transitional exemption pending application cannot be established |
| Peak assets under management | 122,700 DGX (roughly 122.7 kg of gold, about US$6.0M) in January 2020, after five years of operation. Today 15,400 DGX remain outstanding across roughly 2,103 holders, nominally 15.4 kg of gold |
| Backing | 1 DGX = 1 gram of 99.99% LBMA-standard gold in cast bar form, divisible to 0.001g. Specific 100g and 1kg bars, individually identified. Sourced through ValueMax, a listed Singapore pawnbroker, and stored with The Safe House in Singapore, with a Canadian vault added in 2019. Digix Physicals maintained legal title to the vaulted gold, and title transferred to the holder only on physical collection |
| Custody fee charged to holders | 0.60% per annum demurrage, accrued daily and deducted in gold from token balances, split 0.40% to DigixGlobal and 0.20% to DigixDAO. Switched off for the first year of operation, then zeroed permanently in 2019 and never reinstated. A separate transfer fee of 0.13% per transfer, also deducted in gold, went entirely to DigixDAO |
| Yield paid to holders | DGX holders: none. DGD holders who staked and voted received a share of DGX fee revenue, paid quarterly: all of the transfer fee and one third of the demurrage |
| Redemption | Minimum 100 DGX (a 100g bar) or 1,000 DGX (a 1kg bar), 100g and 1kg cast bars only. 1% recast fee charged in gold, so a 100g redemption needed at least 101 DGX in the wallet. Collection in person at the vault in Singapore, later also Canada, within 30 days, with government ID and current proof of address presented at collection. Uncollected bars were automatically re-minted into DGX. Eligibility was open, with no "qualified holder" gate |
| Token standard | ERC-20 on Ethereum only, deliberately non-standard in behaviour: balances decrease without transfer events and fees are deducted from the amount sent. Freely transferable, no whitelist. DGX: `0x4f3AfEC4E5a3F2A6a1A411DEF7D7dFe50eE057bF`. DGD refund contract: `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f` |
| Reserve verification | Proof of Provenance (PoP), an onchain and IPFS asset record tracking each bar from vendor to vault with serial numbers, assay certificates and vault receipts. Arguably the first real onchain proof-of-reserve in tokenised gold, and issuer-operated. No periodic reserve attestation by a named accounting firm was ever published. The smart contracts were audited by Yaron Velner and Loi Luu between 21 May and 18 June 2017 |
| Ceased operating | Digix Holdings withdrew its Payment Services Act licensing and announced it would take no further transactions in September 2022. Operations ceased 21 March 2023, with redemption handed to NexusGold FZC. Digix Physicals and Digix Markets were struck off 4 September 2023. Digix Holdings was struck off 19 July 2026 |
| What holders received | DGD holders received a permanent, permissionless claim of 0.193054178 ETH per DGD through the "Acid" refund contract, with no deadline. Roughly 12,491 ETH remains unclaimed. DGX holders received nothing: no formal notice that redemption had ended, no final reconciliation, and no public account of what became of the gold. The redemption portal at nexusone-dgx.com and the website at digix.global both return connection refused |

#### What it is

Digix was founded in Singapore in December 2014 and is the oldest serious tokenised gold project. DGX predates PAXG by roughly four years and XAUT by five. Digix ran the first significant Ethereum ICO in March 2016, selling DGD for 466,648 ETH, worth about US$5.5M at the time.

The architecture split two jobs across two tokens. DGX was the asset token: one gram of gold, no governance rights, no yield. DGD was the governance and revenue-share token, with a fixed supply of 2,000,000, whose stakers received a share of DGX fee revenue for voting.

Digix built close to the structure Aurumix is considering: a clean gold token, a separate instrument carrying governance and revenue rights, real vaulted metal, onchain provenance, and genuine physical redemption. It was better engineered than most of its successors. It still failed, and understanding why is the value of this profile.

The contract is still deployed and still functional. It was never paused and never self-destructed. Holders can still transfer DGX to each other today. The token outlived every company that gave it meaning.

#### Legal structure and regulatory standing

The Singapore register describes the custody arrangement more precisely than the marketing did. Digix Physicals Pte. Ltd. was incorporated under SSIC 52101, "General Warehousing", with its stated principal activity recorded as "HOLD PHYSICAL ASSETS". That is a warehousing company. It is not a trustee and not a regulated custodian.

Digix Physicals maintained legal title to the gold bullion in the vault, meaning the company owned the vaulted gold and the holder's position resembled a relationship with a bank. Title transferred to the holder only on physical collection. So a DGX holder held an unsecured contractual claim against a Singapore warehousing company, not beneficial title to gold. No trust deed, no bare trust and no independent trustee appears anywhere in the Digix structure.

Set that against PMGT, which for all its faults had a real bare trust, a separate custodian entity and an explicit no-commingling covenant. Digix, the older and more celebrated project, gave holders weaker protection than the product already classified as a failure.

The consequence is now live. Digix Physicals was struck off on 4 September 2023. When a Singapore company is struck off, its remaining property vests in the state as bona vacantia. If gold was still held in that company's name at strike-off, the holder's counterparty no longer exists and the claim runs against a dissolved entity. No filing describing the actual disposition of the gold has been published.

The regulatory finding is the absence of a regulatory finding. No regulator shut Digix down. No MAS enforcement action was ever brought, between 2014 and July 2026, and no regulator anywhere took action. The Payment Services Act withdrawal was voluntary and self-initiated, and it arrived alongside the announcement that the company was ceasing all business activities, not before it. The licence did not kill the business. The business gave up the licence on the way out. The Payment Services Act regime arriving in 2020 raised the cost of staying compliant for a business that by then had no revenue to pay for compliance. That is a cost-versus-revenue problem, not an enforcement problem.

#### Custody and reserve verification

Gold sat with The Safe House in Singapore, an ISO 9001 certified vault, with a Canadian vault added in 2019. Metal was sourced through ValueMax, a listed Singapore pawnbroker. Backing was allocated in substance: specific 100g and 1kg cast bars, individually identified.

The Proof of Provenance protocol was genuinely strong for its era. Each bar's documentation was recorded onchain and on IPFS, with bar serial numbers, assay certificates and vault receipts, tracking metal from vendor to vault. It was arguably the first real onchain proof-of-reserve in tokenised gold.

The two verification categories must be kept apart, because Digix scored well on one and not at all on the other. Digix was smart-contract audited by serious cryptographers, Yaron Velner and Loi Luu, between 21 May and 18 June 2017. It was never reserve-attested by an accounting firm. Proof of Provenance was the issuer telling you about its own gold, cryptographically. When the servers and the IPFS pinning went away, the verification went with them.

The 2017 audit also found real problems, and both were in the fee mechanism itself. It identified a critical bug allowing self-transfers to increase balances, and a finding that the demurrage fee calculation incentivised strategic dummy operations, meaning the fee logic could be gamed by timing transactions. The demurrage design was not merely economically awkward. It was hard to implement correctly, and competent auditors found exploitable defects in it.

#### Fees, revenue and redemption

Digix charged four fee lines, three of which were denominated in gold.

| Fee line | Rate | Denominated in | Recipient |
|---|---|---|---|
| Demurrage (storage) | 0.60% per annum, accrued daily | Gold, deducted from token balance | 0.40% to DigixGlobal, 0.20% to DigixDAO |
| Transfer fee | 0.13% per transfer, originally capped at 1 gram, cap later removed | Gold, deducted from the amount sent | 100% to DigixDAO |
| Recast (redemption) | 1% | Gold | DigixGlobal |
| Minting | None to the depositor | Not applicable | Not applicable |

The 0.13% figure is a per-transfer charge, not an annual demurrage rate. The two are frequently conflated. The annual storage drag was 0.60%, and the transfer fee sat on top of it as a separate, event-driven, gold-denominated charge.

The mechanics of demurrage matter, because they determine whether the mechanism is peg-safe. Digix did not change the token count on its internal ledger. It changed what `balanceOf` returned. The contract stored an actual balance in nanograms, then computed the effective balance returned to any caller by subtracting accrued demurrage:

```text
b = (a / m) * (r * t)
```

Where:

- *b* = demurrage owed, netted off the effective DGX balance in nanograms, which is what `balanceOf` returns
- *a* = actual DGX balance in nanograms on the internal ledger
- *m* = minimum balance unit for the demurrage calculation, a constant of 1 milligram
- *r* = daily demurrage per 1 milligram
- *t* = number of days since the last demurrage deduction

The implementation used `demurrage_base = 10,000,000` and `demurrage_rate = 165`, applied per whole day elapsed:

```text
demurrage_fees = days_elapsed * user_balance * demurrage_rate / demurrage_base
days_elapsed   = (current_time - last_demurrage_payment_timestamp) / ONE_DAY_DURATION_IN_SECONDS
```

Partial days did not trigger a charge. The contract advanced `last_demurrage_payment_timestamp` by exactly `days_elapsed` and left the remainder to accrue. Accrual was linear rather than exponential, which the auditors specifically criticised. The transfer fee used the same in-kind pattern, `transfer_fees = transfer_amount * 13 / 10,000`, deducted from the amount sent, so a recipient of a 100 DGX transfer received 99.87 DGX. The audit report notes this behaviour "is non-standard in ERC20 token contracts, however is needed to support Digix business model."

What this did to the gold ratio decides whether the mechanism is safe for Aurumix. It did not break the 1 DGX = 1 gram peg. It burned the holder's tokens instead. A holder with 100 DGX had 99.4 DGX a year later, and each of those 99.4 tokens was still exactly 1 gram of gold. The vault held less gold, the ledger held proportionally fewer tokens, and the ratio never moved. That is the opposite of the Paxos approach, where the issuer reserves the right to mint new tokens to itself pro rata, holding the holder's token count constant while diluting grams per token.

Redemption was genuinely functional while it ran, and two design points stand out. Worth copying: uncollected bars were automatically re-minted into DGX after 30 days, which resolves abandoned redemptions without ever leaving the peg unbacked. Worth avoiding: redemption required physical presence in Singapore, which put it out of reach of almost the entire holder base. A redemption right you must fly to Singapore to exercise is a marketing feature, not a liquidity feature.

No DGX holder can redeem today. On 21 March 2023 Digix ceased operations and handed redemption facilities to NexusGold FZC, described as an overseas partner with licence number 4306536.01. The redemption portal at nexusone-dgx.com returns connection refused. So does digix.global. The Digix support portal returns 403 Forbidden. NexusGold FZC could not be verified in any UAE free-zone register against that licence number, so its jurisdiction, registration status and continued existence are all unestablished. A recency sweep covering February 2025 to July 2026 found zero announcements, redemption notices, filings or partnership news for Digix, DGX, DGD or NexusGold FZC. Holders were never told redemption had ended. It simply stopped answering.

What happened to the physical gold is not disclosed, and that is the most damning fact in the profile. There is no final audit, no reconciliation, no closing Proof of Provenance report, no ACRA or MAS filing describing disposition, and no statement on whether the gold was liquidated, transferred to NexusGold FZC, or remains at The Safe House under different ownership. 15,400 DGX remain outstanding, nominally representing 15.4 kg of gold worth roughly US$1.5M at July 2026 prices, with no public account of where that metal is. The bar list that Proof of Provenance once published went offline with the infrastructure that served it.

#### Liquidity and distribution

DGX today has 15,400 tokens outstanding across roughly 2,103 holders, an onchain market value near US$278k, a price tracking gold at about $18.52 per gram, and 24-hour trading volume of nil. Price trackers show stale timestamps from May 2026 against a July 2026 date, the signature of an asset with no trades to update it. Bitfinex delisted DGX on 18 June 2021 and no major exchange lists it today. At peak in January 2020 the token had 122,700 units, a US$6.0M market capitalisation, US$172,274 of daily volume, 1,751 holders and listings on 12 exchanges. DGD trades near US$0.067 against an all-time high of US$1,291, a 99.99% decline, with zero 24-hour volume, which is the correct price for a token whose only remaining function is to be burned for its ETH claim.

Distribution ran direct through the Digix marketplace plus exchange listings, reaching 12 exchanges by the end of 2019, with DEX integrations through AirSwap and Tokenlon/imToken and trading pairs in seven quote currencies. Geographically Digix pushed into Indonesia and Vietnam, adding IDR and VND pairs, and opened a China marketplace in 2019. It is the closest geographic analogue in this landscape to Aurumix's India and NRI target: retail-oriented and focused on emerging Asian markets.

The gap is the finding. Digix reached that audience through exchange listings, which is a passive channel that waits for people who already hold crypto. It built no acquisition mechanism, no recurring contribution, no savings plan and no commissioned distribution. Over eight years it accumulated roughly US$6M of peak assets under management.

#### Why it wound down

The causal chain runs in seven steps.

1. DGX never achieved scale. Peak assets under management were about US$6M after five years.
2. Because DGX had no scale, its fees could not fund the company. Full-rate demurrage on the peak base was worth roughly US$36,000 a year gross, of which Digix kept two thirds: about US$24,000 a year. The transfer fee, on US$172k of daily volume at 0.13%, was worth a few hundred dollars a day at best and went entirely to the DAO, not the company.
3. PAXG launched in September 2019 with a zero storage fee, into the same market. Digix could not defend a visible, itemised 0.60% annual charge against a free competitor. In 2019 it zeroed its demurrage permanently, stating in its own year-in-review: "We zeroed DGX demurrage fee so DGX holders do not have to pay the extra dollars when holding on to our gold-backed token." It gave up a revenue line worth about US$24,000 a year and took on an uncapped, gold-price-linked storage and insurance liability, permanently. At that moment the DGX business had no revenue line of its own at all.
4. The company had been living on its ICO treasury rather than on revenue. DGD's price tracked the ETH in the treasury almost exactly, which told the market the operating business was contributing no independent value.
5. Holders noticed and voted the treasury away. Kai Cheng Chng published the "Project Ragnarok" dissolution proposal on 29 November 2019, stating that "Digix is against the dissolution" but that the company would "respect and adhere to the collective opinion [of] DGD holders". On 20 January 2020 the vote passed with over 95% support on only 52 votes cast, against roughly 11,000 DGD addresses. The treasury held approximately 386,428 ETH, worth about US$64M. Digix the company opposed the dissolution and abstained.
6. A revenue-free company minus its treasury has no runway.
7. Wind-down followed. Payment Services Act licence withdrawn and business ceased in September 2022, operations ended and redemption outsourced offshore in March 2023, the title-holding entity struck off in September 2023, the parent struck off on 19 July 2026.

The DAO dissolution was the trigger, not the wind-down mechanism. A well-executed structured treasury return to one class of holders was, from the other class's perspective, the removal of the subsidy that kept their gold redeemable.

#### Relevance to Aurumix

Digix is the most instructive failure here because it did the engineering well and the business badly.

**The case against demurrage is not arithmetic.** Aurumix's peg is vault grams divided by tokens. A Digix-style demurrage burns tokens pro rata while the vault pays the storage bill in gold, so numerator and denominator fall together and the price per token is unchanged. On the arithmetic, Digix-style demurrage is peg-neutral for Aurumix. If Aurumix defends its decision to rule out gram-denominated fees on the grounds that "gram deduction breaks the peg", that reasoning will not survive scrutiny from a technical reader. The real reasons are stronger:

- It is non-standard ERC-20 and it breaks integrations. A `balanceOf` that decreases with no transfer event violates every assumption exchanges, wallets, accounting systems and custodians make. Digix had to build a separate wrapper token, LiteDGX, purely to present a normal fee-free, non-decaying face to the rest of the market. Digix built a second token to undo its own fee mechanism. Aurumix's token carries ICS standing, dividend entitlement and credit eligibility, and every one of those systems reads a balance.
- It is hard to implement safely. Auditors found a critical balance-inflation bug and a gameable fee-timing exploit, both in the fee logic.
- It is retail-hostile. A savings product sold to Indian and NRI retail on a monthly SIP cannot easily explain why the number in the app went down when the customer did nothing. A decrementing balance fights the accumulation narrative every month.
- It is visible and itemised in a market where competitors charge nothing. That is what actually killed it.

Charge in cash.

**A revenue line is a survival feature, and this is the second confirmation.** PMGT launched with zero fees and had no internal advocate. Digix started with fees, could not defend them against a zero-fee competitor, and cut them to nil in 2019. Then it died. The near-universal zero-custody-fee norm across this sector is not really a norm. It is the equilibrium of a price war that no small issuer survives, because your fee is visible and itemised while the competitor's is zero.

Aurumix's escape route is that it is not selling a custody product. It is selling a savings plan with ICS tiers, credit access and a dividend. Fees should attach to those distinguishing services, where no zero-fee competitor exists, and not to the storage of gold, where one does.

**An anonymous claim on a dissolved counterparty cannot be wound down.** Follow the metal. 15,400 DGX still exist, nominally 15.4 kg of gold worth about US$1.5M. The company holding legal title was struck off on 4 September 2023. No public record exists of what happened to the metal: no final audit, no reconciliation, no disposition filing. Holders received no formal notice that redemption had ended. The redemption agent it was handed to cannot be verified in any register. This is the documented answer to "what happens if the issuer fails": the gold vanishes from the public record and the holder is left with a live token, a dead counterparty and no forum.

Aurumix should commit ex ante to a named successor custodian, a defined notice period, a final published reconciliation, and a mechanism that survives issuer strike-off. It should also copy one Digix mechanism directly: the automatic re-mint of uncollected gold, which resolves abandoned redemptions without ever leaving the token unbacked.

**Cap and privately place any dividend instrument.** Digix ran the two-token split, a clean asset token plus a separate revenue-share token, eight years before Kinesis ran the same structure with KVT. The structure is sound. The discipline was not. Kinesis capped KVT at 300,000 units and sold it under an Offering Memorandum as a private placement. Digix sold DGD to the public in an unrestricted ICO, creating a liquid, publicly traded claim on a corporate treasury held by roughly 11,000 addresses who could vote to seize it, and did, on 52 votes. If Aurumix separates its dividend right into a distinct instrument, it should cap it, place it privately, and give it no governance power over treasury assets. The lean toward a permissioned base is well supported.

**Copy the DGD refund contract's properties, and note who it did not protect.** The "Acid" refund contract at `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f` lets a holder approve DGD and call `burn()`, which permanently burns the DGD and sends ETH pro rata at a fixed 0.193054178 ETH per DGD. Exchanges including Binance, Bittrex and Gate applied the identical ratio for their users. There is no deadline, the claim is permissionless and still open, and roughly 12,491 ETH remains unclaimed six years later. It is the only well-executed wind-down mechanism found anywhere in this landscape: a fixed formula, an open-source contract, no expiry and no issuer discretion.

Note what it protected and what it did not. DGD holders, the governance class, got a clean, precise, permanent exit. DGX holders, whose tokens were backed by actual gold, got a dead website. Aurumix must ensure its wind-down protections attach to the gold-holding retail saver, not to whichever class happens to hold the governance rights.

---

### 5.3 CACHE Gold (CGT)

| Field | Detail |
|---|---|
| Issuer | CACHE Private Limited, Singapore UEN 201827110K, incorporated 8 August 2018. Registered office at 6 Changi South Street 3, #01-01 BOXPARK @ Chai Chee, Singapore 486128. The company remains a live company on the ACRA register as at 28 July 2026: not struck off, not dissolved, no liquidator appointed, ten months after it ceased honouring its tokens |
| Licence covering the token | None. CACHE holds Singapore Precious Stones and Precious Metals (PSPM) Dealer registration PS20190001508, verified live on the Ministry of Law register of registered dealers. That is an anti-money-laundering registration, not a financial services or capital markets licence. No Monetary Authority of Singapore licence of any kind was held: no Payment Services Act licence, no Capital Markets Services licence, no Recognised Market Operator status, no MAS-approved prospectus |
| Peak assets under management | Roughly US$12.3M. Final supply was 100,771 grams (about 100.8 kg) at a 2025 gold price near $3,800 per ounce. A dated 2020 walkthrough put supply at 34,301 grams, so the token roughly tripled over five years and never reached scale |
| Backing | 1 CGT = 1 gram of allocated fine gold in an Approved Vault, until 30 September 2025. Clause 1.1.1 describes "beneficial ownership" of that gram and then reduces it to "the economic value" of the gold. Clause 1.2.3 removes any ownership right entirely. Gold sat in third-party vaults under arrangements between CACHE and the vault operators, to which the token holder was not a party |
| Custody fee charged to holders | 0.25% per annum storage fee, deducted in CGT tokens onchain, collected only when a transaction is initiated on the holding address (Clause 6.2.1). Plus a transfer fee of up to 0.10% of CGT transferred, in CGT, onchain (Clause 6.1.1). Plus an inactivity fee of 0.50% per annum on addresses with no CGT transaction for 3 years, in CGT, in lieu of the storage fee (Clauses 6.3.1 to 6.3.2) |
| Yield paid to holders | None. Clause 1.2.3 expressly denies any dividend, revenue share, voting right or participation right |
| Redemption | Three routes under Clause 5.2: in-person collection from an Approved Vault, insured shipping to a linked residential address, or sale to a participating gold dealer for fiat. Minimums as small as 100 grams for physical bars, materially more retail-accessible than PAXG or XAUT. Eligibility was open, not restricted to undefined "qualified holders". Frictions: a Marketplace account and full KYC were required, the transaction had to land within 10 minutes of the order to hold the locked price (Clause 5.3), it had to come from the Linked Ethereum Address (Clause 5.4), and VAT, GST, customs and shipping fell on the holder |
| Token standard | Plain ERC-20 with 8 decimals, Ethereum mainnet only, contract `0xf5238462e7235c7b62811567e63dd17d12c2eaa0`, deployed 17 February 2020. No bridge, no multi-chain deployment. Unpermissioned: free transfer to any address. Transfer, storage and inactivity fees were enforced in the token contract itself |
| Reserve verification | GramChain published per-bar photographs, gross weight, purity, brand, serial number and vault location, refreshed by the vault personnel physically handling the bars and broadcast to Ethereum. The best bar-level transparency in this landscape. No reserve attestation by a named audit firm was ever published, on any date. No smart contract audit report from any named firm was located. The bar explorer at `explorer.cache.gold` now returns HTTP 404 |
| Ceased operating | CGT ceased to be backed by gold at 30 September 2025, 23:59:59 Singapore time, the Compulsory Redemption Date under Clause 5A.4. Manual redemption closed 26 September 2025. The remedy window for eligible holders who received nothing closed 31 October 2025 |
| What holders received | Two addresses were paid, and only two: 60.180957 PAXG (1,871.8 g) on 1 October 2025 and 15.785912 PAXG (491.0 g) on 17 November 2025, totalling 75.9669 PAXG or 2,362.8 grams. That is 2.3% of the 100,771 grams outstanding. The remaining 98,408 grams (98.4 kg, roughly US$12.0M at 2025 prices) went to holders who received nothing. No tokens were burned: total supply today is identical to the supply immediately before the snapshot |

#### What it is

CACHE Gold was an Ethereum token, each unit representing one gram of allocated fine gold held in third-party vaults, issued by CACHE Private Limited of Singapore. The contract deployed on 17 February 2020.

Its distinguishing pitch was bar-level transparency. The GramChain asset-tracking system published per-bar photographs, gross weight, purity, brand, serial number and vault location, refreshed by the vault personnel physically handling the bars and broadcast onchain. Redemption came in three forms: collection in person from a vault, insured shipping to a verified residential address, or sale to a participating gold dealer for fiat.

CACHE is the best test case in this landscape precisely because it did the disclosure work properly. If bar serial numbers and a documented redemption right are worth anything at the moment an issuer stops operating, this is where that value should have shown up.

The token is defunct. The issuer's notice dated 1 October 2025 states that CGT "ceased to be backed by gold as of 30 September 2025, 23:59:59 (Singapore Time)". The contract is still live, not paused and not self-destructed. Transfers still execute: three occurred as recently as 26 July 2026, all zero-value spam. The token functions perfectly. It just represents nothing.

#### Legal structure and regulatory standing

A holder owned an economic claim against the issuer, not title to gold and not a trust interest. That single fact determined the outcome.

The Terms of Service effective 19 June 2025 draw the line in two clauses that sit uncomfortably together. Clause 1.1.1 reads: "CGT is an ERC-20 token on the Ethereum blockchain, representing the beneficial ownership of one (1) pure gram of Allocated Gold stored in an Approved Vault. A Token Holder therefore holds the economic value of the gold a CGT represents." Clause 1.2.3 reads: "A Token Holder shall not have any other rights in relation to CACHE other than the economic value of 1 gram of Gold per CGT. CGT does not represent or confer any ownership right or governance right or stake, share or security or equivalent right, or any right to receive any dividend, share in revenue or any form of voting right or participation right in CACHE."

Both are worth reading side by side, because they disagree. The marketing-facing sentence offers beneficial ownership of an identified allocated bar. The operative sentence delivers a contractual value claim. When the issuer decided to close, the operative sentence governed. Holders had no proprietary interest they could assert over specific serial-numbered bars. Clause 1.1.2 further disclaims that CGT is "a security token, a digital payment token, derivative, commodity, a share or security, an interest in a managed investment scheme, or any kind of financial instrument", and notes it "is not covered by any national deposit insurance scheme".

There was no trustee. A full-text search of the 22-page Terms returns no instance of "trustee", "trust deed", "bankruptcy remote" or any equivalent. No bankruptcy-remote vehicle, no security interest. Because there was no trust and no trustee, at the moment CACHE chose to stop honouring the tokens there was no independent fiduciary with a duty to holders and standing over the bars. The serial numbers identified gold that nobody was obliged, to the holder, to deliver.

The PSPM dealer registration is real and was verified against the official government dataset rather than accepted on the issuer's assertion. Querying the Ministry of Law "List of Registered Dealers" dataset on data.gov.sg for "CACHE" returns exactly one record: CACHE PRIVATE LIMITED, registration number PS20190001508. It remains listed as at 28 July 2026.

What that registration is and is not matters. A PSPM dealer registration is an anti-money-laundering registration under the Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019. It obliges the holder to do KYC, record-keeping and suspicious transaction reporting when dealing in precious metals. It confers no prudential supervision, no client-asset segregation requirement, no capital requirement and no conduct regime for token issuance. Clause 7.1(b) claims the registration means CACHE "is qualified to buy, sell, store, and issue precious metals or precious metals backed tokens like CGT". That is the issuer's characterisation. An AML dealer registration is not an authorisation to issue investment products, and the claim should be read as marketing.

No MAS enforcement action, reprimand or supervisory notice against CACHE Private Limited or CACHE Gold was found. No regulator compelled or supervised the wind-down. The closure was a commercial decision executed under the issuer's own contract terms, and there was no authority with jurisdiction to ask where the gold went.

#### Custody and reserve verification

Custodians were reported as Brink's, Loomis, Dillon Gage IDS (International Depository Services) and The Safe House, with partner vaults across Singapore, Dubai, Frankfurt, Dallas and Zurich. The per-custodian city mapping was never published.

While the protocol operated, GramChain published per-bar photographs, gross weight, purity, brand, serial number and vault location, updated by the vault personnel handling the bars. That is the best bar-level transparency in this landscape.

Neither verification category was satisfied by an independent party. No reserve attestation was ever published by a named audit firm on a stated date, and no smart contract audit report from any named firm was located. The strongest available statement is that the vaults themselves "are also independently audited and insured", which is an assertion about the vault operators' own general audit arrangements. It names no firm, gives no date, and is not an attestation over the CGT gold reserve. A vault operator being audited as a business is not the same as an independent accountant confirming that a specific quantity of gold backing a specific token supply existed on a specific date.

So the transparency stack was very strong on granular bar data and entirely absent on independent verification. GramChain showed photographs and serial numbers supplied by the same commercial chain that had an interest in them being right. No third party ever signed a report saying the total matched the token supply.

The stack is now gone. Verified live on 28 July 2026: `explorer.cache.gold`, `/whitepaper`, `/cache-supply`, `/cache-gold-fees`, `/sell-your-gold` and `/build` all return HTTP 404. Only the homepage wind-down notice and the Terms of Service still resolve. The Terms still in force on the live site cite URLs the issuer has deleted: Clause 1.1.1 directs holders to `https://cache.gold/whitepaper` and Clause 6.3.4 to `https://cache.gold/storage-fee-methodology`. Both are 404. The contract governing tokens that 136 addresses still hold points at documentation that no longer exists.

GramChain itself outlived CACHE. `gramchain.net` still resolves. Clause 9.5.2 explains why the two can be separated: the GramChain intellectual property belongs to Little Bit Pte Ltd, a different company. The tracking technology was licensed in, so it did not die with the issuer, but the CGT-specific bar records it hosted are no longer reachable through any CACHE endpoint.

CACHE published bar-level serial numbers for years. Today there is no public record of which bars backed CGT, because the only interface mapping tokens to bars has been taken down by the issuer. The serial numbers were real while they did not matter, and unreachable the moment they would have.

#### Fees, revenue and redemption

CACHE charged. That distinguishes it from every other protocol in this landscape except a small handful, and it is why the outcome is so instructive.

| Fee line | Rate | How collected |
|---|---|---|
| Transfer fee | Up to 0.10% of CGT transferred | In CGT tokens, automatically onchain, whenever a transfer is initiated (Clause 6.1.1) |
| Storage fee | 0.25% per annum | In CGT tokens, collected "every time a transaction is initiated on the Ethereum Address holding the CGT tokens" (Clause 6.2.1) |
| Inactivity fee | 0.50% per annum on addresses with no CGT transaction for 3 years | In CGT tokens, on the balance as at the date of inactivity, in lieu of the storage fee (Clauses 6.3.1 to 6.3.2) |
| Redemption and marketplace fees | Variable, quoted in the Marketplace | Cash, or deducted from proceeds (Clause 6.4.1) |
| Yield | None | Clause 1.2.3 expressly denies any dividend or revenue share |

The collection mechanism made the storage fee largely theoretical, and this is the finding that matters most for Aurumix. Read Clause 6.2.1 closely: the storage fee accrues at 0.25% per annum but is only actually collected when a transaction is initiated on the address holding the tokens. A holder who bought CGT and never moved it paid nothing, indefinitely, no matter how much storage cost accrued in the meantime. Revenue was a function of transaction frequency, not of assets under management.

That is exactly backwards for a gold savings product. The behaviour a gold token is designed to attract, buying and holding for years, is the behaviour that generated zero revenue while consuming real vault cost every single day. CACHE's own inactivity fee, a 0.50% per annum charge on addresses dormant for three years, is the tell: it was a patch bolted on to reach precisely the holders the storage-fee mechanism could never touch. And it too could only be realised on a transaction.

The arithmetic shows what that produced. Total supply at the end was 100,771 grams, roughly 100.8 kg, worth about US$12.3M at 2025 prices. A 0.25% annual storage fee on US$12.3M is roughly US$31,000 a year gross, and CACHE only collected the fraction of that triggered by actual transactions. The contract shows 10,200 transfers over its entire five-and-a-half-year life, an average of about five per day. Against Singapore staffing, four vault relationships across multiple countries, insurance, KYC compliance under the PSPM Act and the GramChain licence from Little Bit Pte Ltd, a five-figure annual gross fee take is not a business.

The diagnosis is therefore sharper than "it charged nothing". CACHE died charging a fee that its own collection mechanism prevented it from actually collecting, on an asset base far too small to support the operation. No enforcement action, no hack, no reserve shortfall, no scandal, no regulator. Commercial non-viability.

The in-kind mechanism is also worth noting. CACHE deducted fees in grams of gold by taking CGT tokens, not in cash. For a one-token-one-gram product, that reduces the holder's gram count. Aurumix's peg is grams divided by tokens, so an in-kind deduction that burns tokens and gold proportionally would be peg-neutral. CACHE's specific design is a template of how not to fund custody: it taxes exactly the activity a savings product wants to encourage, and exempts exactly the behaviour that costs the issuer money.

The redemption right, which was genuinely good while it ran, was extinguished by contract on 30 September 2025. Clause 5.1 opens "You may, at any time, subject to clause 5A, redeem your CGT tokens." Clause 5A is the kill switch.

#### Liquidity and distribution

CACHE was a very small protocol. Final supply was 100,771 grams across 136 holders, with 10,200 transfers over its entire life, about five per day. Listings were thin: NBX (Norwegian Block Exchange) is the one confirmed venue, and Silver Bullion Singapore offered it. No meaningful DEX liquidity was located and no daily volume data is published for its final two years. There is no price feed today. Its problem was never pricing. It was that US$12M of assets under management cannot pay for four vault relationships in five cities.

Distribution ran direct to consumer through the CACHE Marketplace, plus exchange listings and bullion-dealer partnerships with Silver Bullion Singapore and Dillon Gage as a participating dealer. The target segment was gold investors wanting bar-level provenance, plus business-to-business tokenisation-as-a-service for other asset issuers.

There was no savings plan, no recurring-purchase or SIP mechanism, no referral programme, no affiliate scheme, no agent network and no tiering. For CACHE the absence is doubly relevant, because a recurring-contribution product generates recurring transactions, and recurring transactions were the only thing that triggered its storage fee. A savings-plan distribution model would have partially fixed its revenue problem by accident.

The remaining distribution is grotesquely concentrated. One address holds 96.03% of the entire remaining supply.

#### The wind-down, and what it proves

CACHE published a contractual compulsory-redemption mechanism at Clause 5A of its Terms of Service, effective 19 June 2025, and then followed it. It is the only protocol in this landscape that documented its own wind-down in advance and executed the document as written.

The plan was well designed. Clause 5A.2 required at least three months' notice through five channels, including explicitly "public blockchain channels, including but not limited to the CGT token page on Etherscan", specifically to reach non-account holders. The notice period was honoured to the letter: 19 June to 30 September 2025 is three months and eleven days. A manual redemption window for physical gold or fiat stayed open to 26 September 2025. A default settlement was provided, a PAXG airdrop, so a passive holder was converted into the most liquid equivalent gold token available at a clean weight-based ratio with no discretionary price applied, the notice stating that "No fiat or market price valuation will apply". A post-hoc remedy window ran to 31 October 2025 for eligible holders who received nothing.

The execution can be verified onchain, and this is where it comes apart. Scanning every PAXG transfer event emitted from the CACHE owner address `0xb779efee...` across blocks 23,350,000 to 23,950,000, covering September 2025 through January 2026, returns six log entries, four of which are zero-value Paxos fee-address entries. The entire compulsory redemption consisted of two real payments: 60.180957 PAXG on 1 October 2025 and 15.785912 PAXG on 17 November 2025. Total distributed: 75.9669 PAXG, or 2,362.8 grams of gold, against 100,771 grams outstanding. That is 2.3% of the supply. The remaining 98,408 grams, roughly 98.4 kg and about US$12.0M at 2025 prices, went to holders who received nothing.

Total supply never moved. `totalSupply()` at block 23,479,000, immediately before the 30 September snapshot, was 100,771.01. At the current block it is 100,771.01. Identical. The tokens were never burned. CACHE did not retire the supply it had de-backed. It stopped recognising the tokens and left them circulating.

Where the unsettled gold went cannot be established from public sources. There is no statement by CACHE of what was done with the physical bars backing the un-redeemed 98 kg: the notice says only that tokens "ceased to be backed by gold" and never says what happened to the gold. There is no bar list, final reserve statement or closing GramChain snapshot, because the explorer is 404. There is no liquidator's or trustee's report, because there is no liquidation and there was never a trustee. There is no independent attestation of the reserve at any point, including at wind-down. There is no MAS or Ministry of Law filing about the disposition of the assets.

Three readings are all consistent with the public record and nothing distinguishes them. The bars may have been sold to fund the 2,362.8 grams of PAXG bought for the airdrop, with the remainder retained by CACHE. The bars may have been sold and the proceeds retained. Or a large fraction of the supply may have already been redeemed by holders before the deadline, with the tokens left in circulation unburned. The last is quite plausible and would be the benign reading, but it cannot be confirmed, because CACHE never burned redeemed tokens and never published a final reconciliation. The issuer's own choice not to burn and not to publish makes it impossible for anyone outside to tell whether holders were made whole. A protocol that published bar serial numbers for five years has left no way to answer the only question that ultimately mattered.

100,771.01 CGT remain outstanding across 136 addresses with no redemption path, and Clause 5A.7 has already extinguished their right to complain:

> "5A.7 By continuing to hold CGT tokens, Token Holders (including Tokens Holders who are not eligible to be airdropped PAXG tokens...) expressly agree to this compulsory redemption mechanism as set out in this clause 5A and waive any right to further redemption, refund, or legal claim against CACHE following the Compulsory Redemption Date. For the avoidance of doubt, this waiver shall apply to all Token Holders, including those who do not have a CACHE Marketplace Account."

The waiver was drafted to bind precisely the people the issuer knew it could not reach. CACHE acknowledged this in the same clause: Clause 5A.2 refers to "Token Holders who do not have a CACHE Marketplace Account" and states that "CGT is a public bearer token". Minting was permissioned and fully KYC'd, requiring name, corporate information on shareholders, beneficial owners and directors, email, phone, residential address, date of birth, government ID, proof of address and in some cases source of funds or wealth. The token in circulation was then an anonymous bearer instrument: Clause 1.2.1 states "You become a CGT Token Holder by controlling the private key of an address holding CGT." CACHE knew, in its own contract, that it had holders it could not identify or contact. It wrote the notice provisions around that fact rather than solving it.

The single largest casualty is visible onchain. Address `0xd4033ea2ec53a26d6295f6f375d5c6afbe788660` holds 96,771.41 CGT: 96.03% of the entire remaining supply, about 96.8 kg of gold, roughly US$11.8M at 2025 prices. Its history is that of a patient accumulator: 29 separate purchases from a single counterparty between 2022 and 15 January 2025, then nothing. It received no PAXG. It holds zero ETH, so it cannot even pay gas to move the worthless tokens. It has been silent since January 2025, five months before the wind-down notice was published in June 2025.

That address is the whole lesson. A holder who did exactly what a gold savings product tells you to do, buy steadily and hold, stopped checking in eight months before the notice and lost the entire position. Clause 5A.2's notice mechanism, publication on the website, in the marketplace, by email to Verified Users, on Etherscan and on social media, was contractually impeccable and operationally useless against a bearer holder who was not watching. Notice published is not notice received.

Whether that address belongs to a person who lost US$11.8M, an exchange or custodian omnibus wallet, or an entity that had already redeemed the underlying gold off-chain and abandoned the tokens cannot be determined from public sources. The distinction is enormous, and it is unresolvable for the same reason as everything else here: CACHE did not burn redeemed tokens.

#### Relevance to Aurumix

CACHE is the most valuable failure in this landscape for Aurumix, because it is the only one that tried to do this properly. Its lessons are about execution, not intent.

**A fee that only bites on transactions is no revenue line at all in a savings product.** CACHE's 0.25% per annum storage fee was collected only when a transaction was initiated on the holding address. A five-year buy-and-hold customer, which is the ideal customer for a gold savings plan, paid nothing while costing the issuer vault fees every day. The 0.50% inactivity fee was an admission of the flaw, and it too could only be realised on a transaction. Aurumix's users are buy-and-hold savers by design, which makes this a direct hit. Three implications follow:

- **The recurring SIP is a revenue asset, not just a distribution mechanism.** A monthly contribution is a recurring, predictable touchpoint at which a cash fee can be assessed. CACHE had no such touchpoint. Aurumix does, and should design the custody fee to be collected at contribution time.
- **Charge in cash.** CACHE deducted fees in grams by taking tokens. Aurumix's grams-divided-by-tokens peg tolerates in-kind deduction better, but the cash route avoids the argument entirely and is collectable at the SIP moment.
- **Model the assets-under-management floor and treat it as a go or no-go threshold, not a milestone.** CACHE ran four vault relationships across five cities on roughly US$12M and could not survive. Aurumix should compute the level at which its own custody, compliance and agent-commission costs are covered. The failure mode for a gold token is not a hack. It is being too small to pay for the vault, and that is now two of two failures in this set, alongside PMGT, that died of it.

**An anonymous bearer token cannot be wound down.** This is the second lesson, and CACHE proves it more cleanly than any other case available. The differentiator for Aurumix is not "publish a wind-down plan": everyone can copy a clause, and CACHE's clause was better than anyone else's. The differentiator is publishing a wind-down plan that is architecturally capable of working, which requires four things CACHE lacked:

1. **A trustee or equivalent independent fiduciary holding title to the gold**, so the issuer's decision to stop operating does not extinguish the holder's claim. CACHE had none, and Clause 1.2.3 reduced "beneficial ownership" to "economic value" the moment it was tested.
2. **A holder registry, so notice can be delivered rather than published.** CACHE knew its holders at mint through full KYC, source of funds and beneficial ownership, then deliberately issued them a bearer instrument that severed that knowledge. When it needed to reach those people it could not. It drafted around the gap rather than closing it, and the drafting did not save the holders.
3. **Burn on redemption, always**, so that outstanding supply is a truthful measure of outstanding claims. CACHE's failure to burn is the single reason nobody can now tell whether its holders were made whole.
4. **A final published reconciliation**: bars in, tokens out, gold disposed, at wind-down. CACHE deleted its bar list instead.

With a permissioned register, Aurumix's wind-down is a mailing list and a pro-rata distribution to known wallets. With a bearer token, it is a website notice and a 96% orphan rate. That is the decisive argument for a permissioned base such as ERC-3643, and it also supports Aurumix's existing decision on cash-only buyback with no physical redemption: a cash buyback to a KYC'd holder of record is a wind-down mechanism that actually reaches people. Aurumix should commit to all four items above, and should say plainly that it is doing so because the best-documented wind-down in the sector still failed without them.

**Serial numbers are a liveness feature, not a solvency guarantee.** CACHE had the best bar-level transparency in this landscape and no independent reserve attestation, ever, and all of it went offline the moment the issuer stopped paying for hosting. Three rules follow. A bar list is not an attestation: CACHE's bar data came from the commercial chain that had an interest in it being right, so Aurumix needs a named firm, a stated scope, a stated date and a recurring schedule, published alongside the bar list and never blurred with it in marketing. Transparency hosted by the issuer dies with the issuer, so Aurumix should place its bar list and attestations with a trustee, on an auditor's own site, or on IPFS with content hashes committed onchain. And supply must equal claims, or the transparency is decorative.

**An AML registration is not a licence, and nobody supervised the exit.** CACHE's PSPM registration is real and verified, but it carried no client-asset segregation, no capital requirement, no conduct regime, and it gave no regulator any standing to ask where the gold went. The relevant point for Aurumix's VARA cost-benefit is that the expensive licence buys something specific: a supervisor with standing over the assets at the moment of failure. CACHE had none, which is why its wind-down was answerable to nobody and why the 98 kg is untraceable. That is worth pricing into the application fee and the annual supervision cost, and worth stating to the board in exactly those terms.

CACHE offers no read on the ICS Dividend question: it paid no yield and Clause 1.2.3 expressly denied any dividend or revenue share. It had a single token and no separate security, so it says nothing about the instrument split. And it built no savings plan, referral scheme or agent network, which is consistent with every other protocol in this landscape.

---

## SOURCES: Perth Mint Gold Token (PMGT)

- https://abr.business.gov.au/ABN/View?abn=33622224024
- https://creditorwatch.com.au/credit/profile/33622224024
- https://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/wa/consol_act/gca1987188/s22.html
- https://www.perthmint.com/about/government-guarantee/
- https://www.perthmint.com/invest/goldpass/perth-mint-gold-token-pmgt/
- https://www.perthmint.com/news/media-announcements/corporate/austrac-concludes-the-perth-mints-enforceable-undertaking/
- https://www.perthmint.com/news/media-announcements/corporate/the-perth-mint-welcomes-austrac-outcome/
- https://www.perthmint.com/news/media-announcements/corporate/response-to-abc-tv-allegations/
- https://www.austrac.gov.au/news-and-media/media-release/austrac-deems-perth-mint-free-enforceable-undertaking
- https://www.austrac.gov.au/news-and-media/media-release/austrac-orders-audit-gold-corporations-compliance-financial-crime-laws
- https://www.readkong.com/page/perth-mint-gold-token-whitepaper-in-collaboration-with-2803720
- https://medium.com/pmgt/technical-update-perth-mint-gold-token-contract-is-live-da745a494f99
- https://medium.com/pmgt/the-perth-mint-gold-token-pmgt-is-being-discontinued-d27971f8eb3d
- https://github.com/DeFi-Coder-News-Letter/pmgt-contracts
- https://etherscan.io/token/0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf
- https://thewest.com.au/politics/state-politics/perth-mint-shuts-controversial-goldpass-mobile-app-effective-immediately--c-10510953
- https://www.inkl.com/news/company-running-perth-mint-cryptocurrency-withdraws-support-but-questions-linger-over-future-of-goldpass-app

## SOURCES: Digix Gold Token (DGX) and DigixDAO (DGD)

- https://recordowl.com/company/digix-holdings-private-limited
- https://opengovsg.com/corporate/201724450M
- https://opencorpdata.com/sg/201724269N
- https://etherscan.io/token/0x4f3AfEC4E5a3F2A6a1A411DEF7D7dFe50eE057bF
- https://etherscan.io/address/0x23Ea10CC1e6EBdB499D24E45369A35f43627062f
- https://gist.github.com/loiluu/0363070e1bada977f6192c8e78348438
- https://gist.github.com/mrenoon/2582fba7b4d457d80f7d37520aabbc08
- https://medium.com/@Digix/digix-faq-deaf53fcc1e8
- https://medium.com/digix/dev-updates-jan-15-1cd14df2426f
- https://medium.com/digix/proposal-announcement-project-ragnarok-integrating-a-dissolution-mechanism-for-digixdao-354fd871e3e0
- https://support.bitfinex.com/hc/en-us/articles/360008482333-Digix-Gold-Delisted
- https://iq.wiki/wiki/digix-gold-token

## SOURCES: CACHE Gold (CGT)

- https://cache.gold/
- https://cache.gold/assets/media/CACHE-Terms-of-Service-Effective-19th-June-2025.pdf
- https://cache.gold/terms-of-service
- https://data.gov.sg/datasets/d_e643dd525fb927ee16f54f093c73b490/view
- https://opengovsg.com/corporate/201827110K
- https://recordowl.com/company/cache-private-limited
- https://etherscan.io/token/0xf5238462e7235c7b62811567e63dd17d12c2eaa0
- https://etherscan.io/address/0xd4033ea2ec53a26d6295f6f375d5c6afbe788660
- https://etherscan.io/address/0xb779efeeda6cf887b80bc386e7eb9fdced6753f6
- https://gramchain.net/
- https://web.archive.org/web/20250116193557/https://cache.gold/cache-supply
