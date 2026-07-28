### 5.1 Perth Mint Gold Token (PMGT)

| Field | Detail |
|---|---|
| Issuer | Trovio Operating Pty Ltd, ACN 622 224 024, Australia. Formerly InfiniGold. Branding licence from Gold Corporation |
| Licence covering the token | None identified. No AFS licence; not a registered financial product or managed investment scheme |
| Peak assets | About 1,195 tokens (1,195 fine troy ounces); US$2.54M market capitalisation on 15 March 2023 |
| Backing | 1 PMGT = 1 fine troy ounce, via a Perth Mint GoldPass certificate, itself a claim on Gold Corporation, itself backed by metal in Perth Mint vaults |
| Custody fee charged to holders | 0%. No subscription, storage, management or redemption fee at the token layer |
| Yield paid to holders | None |
| Redemption | Burn PMGT for GoldPass certificates, then transact with the Perth Mint for fiat or bullion. Gold never directly redeemable from the token |
| Token standard | ERC-20, Ethereum only, upgradeable OpenZeppelin proxy with Blacklist and Whitelist contracts. `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf` |
| Reserve verification | Issuer-hosted live feed at `pmgt.perthmint.com`, branded "Realtime Audit". No named-firm attestation located. Feed now offline |

#### What it is

PMGT launched in October 2019 as a wrapper around a product the Perth Mint already sold: GoldPass, a digital gold certificate app. Trovio, known as InfiniGold until February 2021, held the certificates and minted one token per fine troy ounce against them, under a branding licence the Mint was free to withdraw.

#### Structure and standing

- **The marketing surface said Perth Mint. The issuer was a Sydney fintech.** Government ownership, state vaults and a statutory guarantee all sat with Gold Corporation, one layer below the token.
- **The bare trust was real but related-party.** Trovio Custodians Pty Ltd held the certificates under a Custody Deed with a no-commingling covenant. It was an SPV of the issuer, with a sequential ACN. No independent trustee.
- **The sovereign guarantee did not reach holders.** Section 22 of the Gold Corporation Act 1987 (WA) guarantees obligations of Gold Corporation. Trovio is not Gold Corporation.
- **Minting required a GoldPass account first.** That capped the addressable market at roughly 26,700 accounts in two countries.
- **The proof-of-reserve feed was genuinely ahead of its peers,** publishing certificates against supply on demand. It was self-published data, not an attestation, and it now returns connection refused.

#### Why it stopped operating

- **The exit predates the enforcement story.** The Mint began discussions with Trovio to wind down PMGT in early 2022, before any public AUSTRAC action.
- **AUSTRAC cleared the Mint anyway.** The enforceable undertaking accepted from Gold Corporation concluded on 22 July 2025, with the Mint cleared and no fine ever imposed. Every AUSTRAC step named Gold Corporation, not the token issuer.
- **Trovio's own account shifted.** Its 1 March 2023 statement blamed "AUSTRAC and US State Regulation", then was edited to attribute the decision to "several factors after a number of years in operation".
- **Zero fees meant zero revenue.** No mint fee, no storage fee, no redemption fee. With no profit and loss line, nobody inside either company had a reason to defend the product.
- **Four years of trust signals produced US$2.5M.** The token was discontinued on 31 October 2023. The cause reads as commercial abandonment and no distribution, not enforcement.

> **Relevance to Aurumix.** PMGT is close to a control experiment. It had a sovereign guarantee, state vaults, a real bare trust and a live reserve feed, and it still went nowhere, which suggests trust signals were never the binding constraint. Distribution was, and PMGT had none.

- **Charge something.** A product with no revenue has no internal advocate when the licensor loses interest. This is the strongest available argument for the SIP-plus-fee model.
- **Redemption routed through a third party is not redemption.** Aurumix should state in writing who executes the buyback if Aurumix stops operating, and out of what.
- **Name whose obligation a guarantee covers.** Section 22 guaranteed Gold Corporation's, not the token holder's, and the marketing never made that distinction.

### 5.2 Digix and CACHE Gold

Digix ran from 2014, CACHE Gold from February 2020. Both held real vaulted metal, both offered working physical redemption, and both ended the way PMGT did: no regulator, no hack, just an asset base too small to pay for the vault.

| Field | Digix (DGX / DGD) | CACHE Gold (CGT) |
|---|---|---|
| Issuer and domicile | Digix Physicals Pte. Ltd. held title, parent Digix Holdings Private Limited, Singapore | CACHE Private Limited, Singapore, incorporated 8 August 2018 |
| Ceased | Payment Services Act licence voluntarily withdrawn September 2022, no regulator having acted; operations ended March 2023; parent struck off 19 July 2026 | Ceased to be backed by gold 30 September 2025; redemption closed 31 October 2025 |
| Peak assets | 122,700 DGX (about 122.7 kg, roughly US$6.0M) in January 2020 | Roughly US$12.3M. Final supply 100,771 grams |
| Backing and custody | 1 DGX = 1 gram of 99.99% LBMA gold in identified bars, The Safe House Singapore plus a Canadian vault. Legal title with the issuer; no trustee | 1 CGT = 1 gram allocated gold in third-party vaults. Clause 1.2.3 removes any ownership right; no trustee |
| Fee model | 0.60% per annum demurrage plus 0.13% per transfer, in gold. Demurrage zeroed permanently in 2019 to match PAXG's fee-free launch | 0.25% per annum storage, up to 0.10% per transfer, 0.50% per annum inactivity after 3 years, all collected only on a transaction |
| Redemption | Minimum 100 DGX, cast bars only, 1% recast fee, collected in person in Singapore within 30 days | Vault collection, insured shipping or dealer sale under Clause 5.2. Minimums from 100 grams, KYC and a Linked Ethereum Address required |
| Reserve verification | Proof of Provenance, an onchain and IPFS bar record. Contracts audited 2017. Never reserve-attested | GramChain published per-bar photographs, weight, purity and vault. No named-firm attestation. `explorer.cache.gold` now returns 404 |
| Why it stopped | Zeroing demurrage left the gold business no revenue while it lived on its ICO treasury. Holders voted that treasury away on 20 January 2020, over 95% on 52 votes, roughly 386,428 ETH (about $64M) | Ran its Clause 5A plan as written: three months' notice across five channels including Etherscan, a redemption window, default settlement in PAXG at a clean weight ratio. Settled 2.3% of the gold |
| Lesson for Aurumix | Demurrage burned tokens rather than grams, so the gold-per-token ratio never moved. Peg-safe and still commercially fatal: a visible itemised fee cannot be defended against a zero-fee competitor | Two payments totalling 2,362.8 g against 100,771 g outstanding left about 98,408 g (roughly $12.0M) unaccounted for in public sources. 100,771 CGT sit unburned across 136 addresses, one holding 96.03% with no ETH to move them |

> **The takeaway.** All three died of revenue starvation and absent distribution rather than regulators or hacks. CACHE adds the second lesson: publishing a wind-down plan is necessary and nowhere near sufficient, because an anonymous bearer token cannot be wound down at all. There is no holder registry to deliver notice to, and no burn on redemption keeping supply equal to claims.
