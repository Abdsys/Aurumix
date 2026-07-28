# Tokenized Gold: Protocol Landscape

**Prepared for Aurumix by Tokenomics.net. Research completed 28 July 2026.**

Nineteen protocols profiled end to end against the same thirteen headings: sixteen live products and three that failed. Every profile was built registry-first, meaning the issuing entity was verified against a company register before any claim about jurisdiction, licensing or structure was accepted.

That method changed the answers. **Eleven conclusions carried in our earlier research and working notes turned out to be wrong**, including three that were load-bearing for the mechanism design. They are listed in full below, before the findings, because knowing what we had wrong is more useful than knowing what we had right.

---

## How to read this document

Every protocol is profiled against the same thirteen headings in the same order, so any two can be compared line by line. Four conventions carry throughout.

| Convention | Meaning |
|---|---|
| **Confidence: High** | Established from a primary source: issuer terms, prospectus, audit report, corporate registry, or on-chain contract. |
| **Confidence: Medium** | Established from issuer marketing or a credible secondary source, without a primary document to confirm it. |
| **Confidence: Low** | Fragmentary or contested. Treat as a lead to verify, not a fact to cite. |
| **Not disclosed** | We looked and found nothing. This is a finding in its own right, and is never filled with a plausible assumption. |

Anything a competitor asserts about itself is reported as an assertion, not adopted as fact. Where marketing and legal documents disagree, both are shown. That gap between the two turned out to be the single most productive thing to look for.

---

## What this document overturns

Eleven corrections. The first three change design decisions that were already made.

| # | We believed | Actually | Where |
|---|---|---|---|
| 1 | ORO is a **Dubai** peer running a compliant real-yield structure worth copying | **Oro Labs PTE Ltd, Singapore**, UEN 202434484G, ACRA activity "software development". No licence in any jurisdiction. Its own terms disclaim issuance to unnamed third parties | ORO |
| 2 | Comtech shows a **DMCC route around VARA**, so VARA may not be the only door | ComTech issues on a **DAFZA** bullion licence (05069). The DMCC licence covers **IT consultancy only**. Neither permits public token issuance, and both display as **expired**. There is no lawful route around VARA here, only an unlicensed gap | Comtech |
| 3 | PMGT was killed by **AUSTRAC enforcement** plus the Shanghai Gold Exchange scandal | Killed by **commercial abandonment**. The Mint began exit discussions in early 2022, before any public AUSTRAC action. The AUSTRAC undertaking concluded 22 July 2025 with **no fine ever imposed**. A zero-fee model meant no revenue and no internal advocate | PMGT |
| 4 | Deducting a fee **in gold breaks a grams ÷ tokens peg**, so demurrage is unavailable to us | Digix's demurrage **burned tokens, not grams**. The gold-per-token ratio was untouched. It is **arithmetically peg-neutral for Aurumix**. The real objections are different and stronger (see Finding 3) | Digix |
| 5 | **No failed gold token published a wind-down plan** | **Cache Gold did**, at Clause 5A: three months' notice across five channels, a redemption window, a default settlement in PAXG. **DGLD has one too.** Cache Gold followed its plan and still stranded 96% of supply, which is a far more useful finding | Cache Gold, DGLD |
| 6 | **No documented real-yield gold-leasing precedent exists**, so re-anchor the dividend elsewhere | **Half of one exists.** Streamex filed the executed agreement with the SEC (8-K, 8 Sep 2025, accession 0001641172-25-026853, Exhibit 10.1), including a 3% net floor and two layers of insurance. What does **not** exist anywhere is holder-level protection | Streamex |
| 7 | PAXG is **NYDFS**-regulated | **OCC**. Paxos converted to a national trust bank charter on 12 December 2025. Paxos's own transparency page still says NYDFS, so the stale fact keeps propagating | PAXG |
| 8 | A 3–8% exchange premium can be engineered and relied on | Dead from nine independent directions. See Finding 1 | All |
| 9 | Digix charged **0.13%** demurrage | **0.60% per year**. The 0.13% figure is a separate per-transfer fee | Digix |
| 10 | DGLD is a **dormant RSK** sidechain token | Ran on **Ocean (CommerceBlock)**, not RSK. **Live, not dead**: MKS PAMP bought the issuer outright on 20 November 2025 and redeployed on Base | DGLD |
| 11 | WisdomTree WTGOLD is a **tokenised fund share** recorded by a transfer agent | An **electronic document of title under NY UCC Articles 1, 2 and 7**. No SEC registration, no transfer agent, ownership recorded on the blockchain exclusively | WTGOLD |

⚠ **A note on where the errors came from.** Our protocol list, and much of the metadata behind these mistakes, came from **rwa.xyz**. Its issuer metadata proved unreliable on at least five protocols: it names a "Gold Issuance Inc." for ORO that exists in no register, attributes four incorrect fields to AZG including a fabricated auditor and a non-existent ASIC licence, labels both Midas XGZ and PGOLD "Bankruptcy Remote" with nothing in either issuer's documents supporting it, and degrades DGLD's SRO membership into "supervised by FINMA", which is false. **Use rwa.xyz to enumerate the market, never to characterise an issuer.**

---

## The nine findings

### Finding 1: The premium thesis is dead, from both ends of the liquidity spectrum

The client's model assumes a 3–8% exchange premium will sustain spot and SIP demand. **Nine protocols say it cannot.**

| Protocol | AUM | Liquidity signal | Price vs spot |
|---|---|---|---|
| Tether XAUT | ~$2.465bn | ~$130M/day, ~5.3% turnover | At gold |
| PAXG | ~$1.79bn | ~$105.6M/day, ~5.9% turnover | At par |
| Matrixdock XAUm | ~$52.7M | Continuous two-way primary window | Capped by a 0.76% spread |
| VNX VNXAU | ~$5.7M | ~$36k/day | ~0.7% over |
| Comtech CGO | ~$5.04M | ~$213/day genuine DEX liquidity | Parity, 0.42% spread |
| Aurus tGOLD | ~$5.6M | ~$211/day after seven years | Capped at NAV + 0.5% by provider arbitrage |
| Midas XGZ | ~$5.06M | 264 holders | **1.4% discount** |
| ORO | ~$2.45M | 33% liquidity-to-AUM, 16x PGOLD's | **Slight discount** |
| PGOLD | ~$79–90M | Under $20/day | No functioning market |

The mechanism is now clear and it is a pincer. **Where a market is liquid, arbitrage closes any premium.** Where it is illiquid, there is no market to express one. The two protocols that do trade away from spot trade at a **discount**, and Midas XGZ explains why: a permissioned primary market with a 1 kg redemption floor against an average holding of 148 grams means arbitrage cannot close a discount either.

**Implication.** Model the premium at **zero**. If Aurumix's closed redemption does produce a price above NAV, that is a product of blocking arbitrage, not of demand, and it is not a revenue line anyone should plan around. This retires the last economic justification for the "mining event" mechanic, which §6.5 of the working notes already reduced to a framing question.

### Finding 2: Nobody charges holders a custody fee, and the reason Aurumix cannot copy the funding model is structural

Zero ongoing custody fee is the category norm: PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, WTGOLD, DGLD and PGOLD all charge holders nothing. But the funding underneath splits three ways, and none of the three is available to Aurumix.

- **Velocity taxes** (Kinesis 0.45% transfer, Aurus 0.5% mint / 1.5% burn, Comtech ~1% commission plus spread). These fund storage out of **churn**. A monthly SIP savings product is the lowest-velocity product imaginable, so this model **inverts** for us: our users hold, they do not trade.
- **Parent cross-subsidy** (XAUT from Tether's stablecoin reserve income, XAUm from Matrixport, WTGOLD from a $150bn listed manager, PAXG from its stablecoin business). Aurumix has no parent.
- **Deferral**, which is the honest one. Comtech charges nothing for 24 months and then reserves "a nominal fee", and XAUm reserves the right to start charging on 30 days' notice. **Both concede that transaction-margin funding fails for buy-and-hold**, which is exactly our case.

**The two mechanisms worth taking forward are both peg-neutral for us and both were misunderstood in our earlier work.**

**PAXG's dilution clause.** Paxos reserves the right to take storage fees "by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens pro rata". Paxos has never used it, because its peg is 1 token = 1 ounce and minting breaks it. **Aurumix's peg is grams ÷ tokens, so minting to treasury lowers price per token and leaves the identity intact.** It collects nothing from a $20 SIP saver in cash, and it reaches holders who never log in. It now has an OCC-supervised precedent for the drafting.

**Digix's demurrage.** It burned tokens rather than grams, so the gold-per-token ratio never moved. **Also peg-neutral for us.** Correction 4 above retires our stated reason for ruling it out, but three better reasons survive: a non-standard ERC-20 broke integrations so badly that Digix built its own wrapper to undo its own fee, auditors found a critical bug and a timing exploit in the fee logic, and **a balance that visibly decrements every day is indefensible in a retail monthly-savings product** aimed at customers whose reference point is a life insurance premium.

### Finding 3: The dividend is a trilemma, not a design problem

This is the most important finding in the document for Phase 2.

Every well-regulated, well-documented protocol in the set pays **zero** yield, and does so deliberately: PAXG, XAUT, XAUm, VNXAU, WTGOLD, DGLD, Midas XGZ, Comtech. Two of those are the largest gold tokens in the world. WisdomTree owns a registered transfer agent, a broker-dealer and a fund adviser, holds allocated gold at HSBC, and still pays nothing. Midas XGZ sits inside a 115-year-old exchange group with better bullion-leasing access than Aurumix will ever have, and leaves the gold idle.

Every protocol that **does** advertise a yield fails the arithmetic:

| Protocol | Advertised | Actual or implied | Gap |
|---|---|---|---|
| Kinesis | 2.05% | **$26,326 paid in June 2026 on $310M AUM = ~0.10% annualised** | ~20x |
| PGOLD | 5% on ~$79–90M (~$4M/yr) | Funded from redemption fees on rare redemptions plus a market trading under $20/day | Unfundable |
| MG999 / Theo | 2.3% net | Borrows gold at 2.5% gross, pays a 1.00% management fee before platform, trustee, admin and audit costs | Arithmetically impossible |
| ORO | 3–4% APY | External leasing, real, but no legal documentation of holder claims | Real source, no protection |

**Tenbin tGLD supplies the identity that explains all of it.** It pays a genuine 4–6% gold-denominated yield, funded by futures basis plus stablecoin rates. It can do that precisely **because its collateral is USDC and margin, not bullion**. Vaulted gold yields nothing and costs money to store. So the client's position resolves into a trilemma with no fourth option:

1. **Encumber the gold** (lease it), and give up "100% allocated and unencumbered", inheriting lessee credit risk on the very asset that backs the token.
2. **Fund from operating profit**, and accept that the dividend is a profit share, which is the securities-classification risk we have flagged from the start.
3. **Stop claiming a dividend**, and compete on the SIP, the credit facility and the inheritance features, which is where the actual differentiation lives anyway.

**This should be put to the client as an explicit choice at the next call.** It is not a problem we can design around, because it is arithmetic.

### Finding 4: Real gold-leasing yield is documentable. Holder protection is not.

Streamex partially reverses our conclusion that no documented precedent exists. The agreement is real, executed, and public: **SEC 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1.** It carries a **3% net-after-origination-fees floor**, absolute discretion to reject any lease, and two layers of insurance including a Lloyd's DIC/DIL policy covering lessee fraud and mysterious disappearance at 110% of value. That is a copyable yield-generation template and it is more than we thought existed.

What it does **not** do is protect a token holder. There is no security interest, no title-retention clause, no risk-of-loss allocation, no subordination and no waterfall. The insurance loss payee is **Monetary Metals "wherever possible"**, a best-efforts phrase rather than a covenant. Streamex's own 10-K concedes holders "may face delays, partial recovery, or **total loss**" and that other lessors in the commingled pool "may receive more favorable terms or priority in enforcement scenarios". Liability is capped at the lesser of six months' fees or $500,000. A GLDY holder sits four entities away from the metal.

**And the risk is not hypothetical.** On **26 January 2026 the AgaBullion lessee defaulted**, Turkish authorities seized the leased gold, and Monetary Metals' remedy was Istanbul counsel plus an insurance claim. "Title remains with the lessor" means "we will litigate abroad."

Two things follow. First, **the yield-generation half of §6.8 should be amended rather than abandoned**: the template exists, it is public, and it can be copied. Second, **no protocol in this landscape names token holders as an insurance loss payee or publishes a default waterfall.** Being the first to do so is cheap, unoccupied differentiation. Note the audience gap though: Streamex sells this risk to accredited investors at a $200,000 minimum. Aurumix would be selling the same risk to a $20-a-month saver, and that difference is the whole regulatory argument.

### Finding 5: Protocols die of revenue starvation, not of regulators or hacks

All three failures, plus the six-year dormancy of a fourth, share one cause, and it is not the one anybody expects.

- **PMGT** charged nothing: no mint fee, no custody fee, no redemption fee. It reached ~US$2.5M in four years with sovereign guarantee, state-owned vaults, a real bare trust and a live proof-of-reserve feed. **Nobody inside the Perth Mint had a reason to fight for it.**
- **Digix** zeroed its own 0.60% demurrage in 2019 to match PAXG's fee-free launch, leaving the gold business with no revenue line at all. It had been living on its ICO treasury. When holders voted that treasury away (**20 January 2020, >95% on 52 votes, ~386,428 ETH / $64M**), the runway ended. No regulator acted: the licence was **voluntarily withdrawn**.
- **Cache Gold** did charge, but Clause 6.2.1 only collected the storage fee **when a transaction was initiated**. Buy-and-hold savers paid nothing while consuming vault cost every day. It died charging a fee it had architected itself out of collecting.

Not one died of enforcement, a hack, or a reserve shortfall.

**Implication, and it cuts against instinct.** Custody quality does not create demand and it does not create survival. **A revenue line is a survival feature**, and a fee that only bites on transactions is no revenue line at all in a savings product. This is a direct warning about any Aurumix design where the fee schedule depends on user activity, and it is an argument for the SIP-inflow-skim and dilution mechanisms in Finding 2, both of which collect from a dormant holder.

### Finding 6: A wind-down plan is necessary and nowhere near sufficient

Our working note said no failed gold token published a wind-down plan. Cache Gold did, and its example is far more instructive than the absence would have been.

Clause 5A required three months' notice across five channels including Etherscan, a manual redemption window to 26 September 2025, a default settlement in PAXG at a clean weight ratio, and a remedy window to 31 October 2025. The issuer followed it.

**Only 2.3% of the gold was settled.** Scanning every PAXG transfer from the CACHE owner address returns two real payments totalling **2,362.8 g against 100,771 g outstanding**. The fate of the remaining ~98,408 g (roughly $12.0M) cannot be established from public sources. **100,771 CGT remain outstanding across 136 addresses and were never burned**, so total supply today is byte-identical to before the wind-down. One address holds **96.03%** of it, received no settlement, holds no ETH to even move the tokens, and went silent five months before the notice was published. Clause 5A.7 pre-emptively waives their claims. There was never a trustee.

**The lesson upgrades the recommendation.** "Publish a wind-down plan" is too weak. The plan must be **architecturally capable of executing**, which requires four things Cache Gold lacked: a **trustee holding title**, a **holder registry** so notice is delivered rather than merely published, **burn-on-redemption** so supply always equals claims, and a **final published reconciliation**.

**An anonymous bearer token cannot be wound down.** That is now the strongest argument in this document for Aurumix's permissioned ERC-3643 base, and it is stronger than the rights-survival argument we have been making. Note the counter-example that proves it: **DGLD's holders own the gold outright at law** (Swiss co-ownership and possession, with the terms expressly disclaiming any debt or equity claim), which is exactly why six years of total neglect harmed nobody and a restart was possible in 2025.

### Finding 7: The category operates almost entirely outside the regulatory perimeter, and hides it the same way every time

Of nineteen protocols, the ones holding an actual licence covering the token they issue are: **PAXG** (OCC national trust bank), **XAUT** (CNAD El Salvador, EME-0004), **WTGOLD** (NYDFS limited purpose trust), and **MG999** (MAS CMS, held by the platform and the fund manager). That is four.

Everything else operates on one of three patterns:

1. **The software company.** The operating entity is registered for "development of software and applications", not financial services or precious metals. This is true of **ORO** (ACRA), **Aurus** (SIC 62012), **Midas GoldZip** (both entities, ACRA) and **Libeara's holding company**. The regulated acts (owning metal, custody, KYC, retail sale, redemption) are pushed onto partners, or simply performed unlicensed.
2. **The adjacent licence, described as the real one.** Comtech's DAFZA bullion trade licence and Midas's Singapore MinLaw PSPM dealer registration are both **AML or trade registrations**, and both are marketed as authorisation to issue tokens to the public. Comtech's licences are additionally **displayed expired**.
3. **The halo.** Kinesis describes a **conditional** CIMA approval as regulatory status while a CIMA register search returns no entity of that name. rwa.xyz turns DGLD's SRO membership into "supervised by FINMA". Libeara's Standard Chartered connection is venture equity two removes away, with SC appearing nowhere in the MG999 stack as issuer, manager, custodian, auditor, administrator or guarantor.

**The finding that matters most for B1**: **there is no cheap compliant door.** The DMCC hypothesis is dead. Everyone who looks like they found a shortcut is either unlicensed, licensed for something else, or subsidised by a parent that already holds a banking or trust charter. Two live leads remain worth checking with counsel: the **ADGM Accepted Spot Commodity** route, and **Universal Digital Intl Limited's ADGM FSRA permission No. 250089** with CBUAE PTSR registration, though the latter is scoped to fiat-referenced tokens for professional clients.

And a caution from Libeara that inverts the usual assumption: **the licence is what buys the opacity, not what removes it.** MG999 holds a real MAS licence and publishes less legally operative detail than tiny VNX, because selling only to accredited investors removes the prospectus obligation. "Regulated therefore transparent" has the causation backwards. That route is closed to Aurumix anyway at $20 a month.

### Finding 8: "Audited" almost never means the gold was checked

This caught us on six protocols and it is the most reliable single tell in the sector. The published audit is a **smart-contract** audit; the **reserve attestation** is absent, stale, or self-signed.

| Protocol | What "audit" means there |
|---|---|
| PGOLD | Beosin, staking contract only. No reserve attestation at all |
| Aurus | NonceBlox smart-contract audit. Chainlink PoR announced but not live. Self-reported 73,398.5 g does not obviously reconcile to 43,322 tokens |
| ORO | Cantina and Adevar Labs, smart contracts. RSM reserve frequency stated **three inconsistent ways**, no document published |
| Comtech | **Self-signed letters on company letterhead**, last one 21 March 2025 and 16 months stale, showing reserves down 23%. No bar list, no smart-contract audit |
| WTGOLD | No bar list, no PoR feed, no reserve attestation and no smart-contract audit |
| AZG | No contract audit, source not even verified on-chain, no attestation |

The strongest in the set is **XAUT's ISAE 3000 (Revised) reasonable assurance** opinion from BDO Italia, and even there the custodian is unnamed and no bar list exists. **DGLD, PAXG and VNXAU** are the only protocols with credible independent reserve examination. Note VNX's sting: its auditor states the basis of a holder's property right is **VNX's own internal holder register**, then expressly refuses to opine on it.

### Finding 9: Distribution is the universal gap, and it is Aurumix's actual moat

**No protocol in this landscape has a savings plan, a recurring purchase mechanism, or a retail referral programme.** Not one of nineteen. PMGT reached $2.5M in four years and its post-mortem names zero distribution as the cause. The category has spent seven years perfecting custody and ignoring demand.

The one partial exception is instructive. **Aurus runs a partner network** paid from a fee pool split 50% to ecosystem token holders, 25% to vault partners, 25% to provider partners. The reseller tier gets **0% of the pool**: they earn only their own markup, plus preferential bulk redemption and a **graduation path** to a higher tier. No commission, no override, no residual, nothing paid for recruitment. It is a merchant-margin supply chain, not an MLM.

**That is the anti-MLM answer we have been looking for, and it is structural rather than cosmetic.** Recast Aurumix's three tiers so each is **paid for a function performed** (capital committed, custody provided, servicing delivered) rather than for recruitment depth, and use graduation rather than overrides to motivate top agents. Combined with the insurance-style trailing commission tied to **continued contributions** already logged at §6.10, this gives two independent structural defences against the MLM read.

One caveat carried from Aurus: its partner economics live in a **whitepaper**, the only legal document on the site is a four-page website terms page naming no entity and no governing law, and the split has changed three times under upgradeable contracts with "adjustable fees". Copy the structure, not the paperwork.

---

## Comparison tables

### Live protocols by assets under management

| Protocol | AUM | Domicile (registry-verified) | Licence covering the token | Custody fee | Yield | Token standard |
|---|---|---|---|---|---|---|
| Tether Gold (XAUT) | ~$2.465bn | El Salvador (from BVI, Jan 2025) | CNAD EME-0004 | 0% | None | ERC-20 + TRC-20 + LayerZero OFT |
| Pax Gold (PAXG) | ~$1.79bn | United States | OCC national trust bank | 0% | None | ERC-20 (upgradeable proxy) |
| Kinesis (KAU) | ~$310M | Cayman (six entities) | **None granted.** CIMA conditional only | 0% | 15% of fee pool, ~0.10% realised | Permissioned Stellar fork + ERC-20 wrapper |
| Pleasing Gold (PGOLD) | ~$79–90M | Hong Kong | None identified | 0% | "5%", unfundable | ERC-20 |
| AZG | ~$65M claimed | Nevis, **unverifiable** | None | 1% (secondary source only) | 15% to miners, not holders | ERC-20 |
| Matrixdock (XAUm) | ~$52.7M | BVI, **unverified** | None in issuer's name | 0%, reversible on 30 days | None | ERC-20 + BullionNFT |
| MG999 (Libeara) | ~$12.44M | Singapore | MAS CMS (platform and manager) | 1.00% management | ~2.3% net, arithmetically impossible | Not published |
| Streamex (GLDY) | 3,133 tokens, **98.5% held by parent** | Cayman (issuer) | None. Reg D 506(c) exemption | Not disclosed | 3.50%, paid in GLDY | Not published |
| DGLD | ~$8.1M | Switzerland (Geneva) | **None.** VQF SRO affiliation only | 0% | None | ERC-20 on Ethereum + Base |
| Aurus (tGOLD) | ~$5.6M | **United Kingdom** | None | 0% | None on tGOLD | ERC-20 |
| VNX (VNXAU) | ~$5.73M disputed | Liechtenstein | TVTG **registrations**, no Token Issuer | 0% | None | ERC-20 with transfer-provider hook |
| Midas (XGZ) | ~$5.06M | Singapore | PSPM dealer registration only | Not disclosed | None | ERC-20 + 0.01% transfer fee |
| Comtech (CGO) | ~$5.04M | Dubai (**DAFZA**, not DMCC) | **None.** Trade licences only, displayed expired | 0% for 24 months | None on token | ERC-20 |
| ORO (GOLD) | ~$2.45M | **Singapore**, not Dubai | **None anywhere** | 0% | 3–4%, undocumented | SPL, freeze authority null |
| WisdomTree (WTGOLD) | ~$2.0–2.5M | United States (NY) | NYDFS limited purpose trust | 0% | None | Document of title, NY UCC Art. 7 |
| Tenbin (tGLD) | ~$1.05M | BVI | None | None (no custody) | 4–6%, synthetic | ERC-20 |

### Failed and wound-down

| Protocol | Died | Actual cause | Wind-down plan | What holders got |
|---|---|---|---|---|
| PMGT | 31 Oct 2023 | **Commercial abandonment.** Zero fees, zero revenue, zero distribution | One sentence, and it failed: the redemption destination was closing at the same time | Made whole by luck of timing. Non-actors force-sold at the 1 Nov 2023 price without consent |
| Digix (DGX/DGD) | Mar 2023 operations, parent struck off **19 Jul 2026** | Zeroed its own demurrage to match PAXG, then lost its treasury to a 52-vote poll | None for DGX | **DGD holders:** 0.193054178 ETH each, permanent permissionless claim, ~12,491 ETH still unclaimed. **DGX holders:** a dead website |
| Cache Gold (CGT) | Redemption ended 31 Oct 2025 | Charged a fee it only collected on transactions, so savers paid nothing | **Yes, Clause 5A**, and it was followed | **2.3% settled.** ~98,408 g unaccounted. 100,771 CGT still outstanding, never burned |

---

## What this changes for Phase 2

Four items go directly into B1 and B5.

1. **The dividend trilemma (Finding 3) needs a client decision, not a design.** Put the three options to CG on Wednesday. Our recommendation is option 3 for launch, with option 1 available later once the credit book is real and counsel has ruled on the leasing structure.
2. **B1's regulatory options narrowed.** The DMCC route is dead (Correction 2). VARA, ADGM Accepted Spot Commodity, or a licensed partner are what remain. **No cheap door exists**, and every protocol that appears to have found one is unlicensed.
3. **The ERC-3643 recommendation is now argued from wind-down, not from rights survival** (Finding 6). Cache Gold is the evidence: an anonymous bearer token cannot be wound down even by an issuer that publishes a plan and follows it.
4. **The custody fee has two peg-neutral mechanisms available** that we had wrongly excluded (Finding 2), both with live precedent. This should be settled in B2 alongside the cash-skim recommendation.

Two items need work before they can be used.

- **The Streamex lease documentation** should go to the client's Dubai counsel as a worked example, with the explicit question of whether the holder-protection layer that Streamex omits can be built in a VARA or ADGM context.
- **The Aurus partner structure** should be modelled properly in Phase 4 against the IRDAI trailing-commission structure already logged, since the two together are the anti-MLM design.

---

## Sourcing note

Research was performed 28 July 2026 using Perplexity Sonar Pro via OpenRouter, combined with direct retrieval from company registers (ACRA, Companies House, ASIC and ABR, ACRA, the Liechtenstein FMA register, the MAS Financial Institutions Directory, the Swiss commercial register, the BVI register, DAFZA and DMCC), regulator registers (VARA, DFSA, ADGM FSRA, CIMA, OCC, NYDFS, CNAD El Salvador, MinLaw Singapore), SEC EDGAR full-text search, and on-chain data from Etherscan, Solana RPC, Basescan and DefiLlama.

Two research-integrity notes are worth recording, because both nearly entered the document as fact. **A Perplexity response fabricated a Stellar issuer address for WTGOLD with a confident inline citation; the address does not exist on mainnet.** And every Stellar asset currently named "WTGOLD" or "WisdomTree" is a **spoof**, published from domains including `wisdomtree.xlmhq.org` and `wisdomtree.com.co`, with no `stellar.toml` at any genuine WisdomTree domain. Assertions in this document that could be checked against a register or a chain were checked. Where they could not be, the confidence label says so.

---

# Part 1: Live protocols

---

# Tether Gold (XAUT)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | XAU₮ / XAUT (base ERC-20); XAUt0 (omnichain wrapper) | **High** |
| Issuer (marketing) | "Tether Gold", presented under the Tether brand umbrella | **High** |
| Issuer (registry) | **TG Commodities, S.A. de C.V.**, an El Salvador *Sociedad Anónima de Capital Variable* | **High** |
| Domicile | **El Salvador**, relocated from the **British Virgin Islands in January 2025** | **High** |
| Prior domicile | British Virgin Islands (as "TG Commodities Limited") | **High** |
| Parent | Wholly owned by Tether Holdings, S.A. de C.V. and Tether Operations, S.A. de C.V. | **Medium** |
| Backing claim | 1 XAU₮ = 1 fine troy ounce of LBMA London Good Delivery gold, vaulted in Switzerland | **High** |
| Chains | Ethereum (canonical ERC-20), Tron (TRC-20), plus XAUt0 omnichain on TON, Solana, Avalanche, Polygon, Conflux, BNB Chain | **Medium** |
| Contract address (Ethereum) | `0x68749665ff8d2d112fa859aa293f07a622782f38` | **High** |
| Supply | 612,823 XAU₮ circulating / 707,747 XAU₮ total minted | **High** |
| Market cap | ~**US$2.465bn** (at ~US$4,021/oz, July 2026) | **High** |
| 24h volume | ~US$130.4m | **High** |
| Regulatory status | Registered stablecoin issuer, **CNAD El Salvador, register no. EME-0004** (19 May 2025); FinCEN MSB registrant | **High** |
| Subscription fee | 0.25% on direct purchase from issuer; minimum 50 XAU₮ | **Medium** |
| **Ongoing custody fee** | **Zero. No recurring storage or management fee is charged to holders.** | **High** |
| Redemption fee | 0.25%, plus logistics/insurance/handling; physical delivery in Switzerland only | **Medium** |
| Advertised yield | **None.** XAU₮ pays no yield, interest or dividend | **High** |
| Named officers | **Giancarlo Devasini, Sole Administrator** (signs the reserves report) | **High** |
| Reserve attestation | BDO Italia S.p.A., **ISAE 3000 (Revised) reasonable assurance**, quarterly | **High** |
| Custodian | **Not disclosed.** Referred to only as "the Custodian" | **High** |

---

## 1. What it is

Tether Gold is the largest tokenized gold product in existence, at roughly **US$2.46bn** market capitalisation and about **612,823 troy ounces** in circulation (approximately 19 tonnes of gold behind the circulating float). Each XAU₮ token represents one fine troy ounce of gold on a specific London Good Delivery bar held in a Swiss vault.

Its scale is the point for this exercise. XAU₮ is roughly **25 to 30 times the size of PGOLD** and orders of magnitude larger than ORO, yet its public documentation set is thinner in several important respects than protocols a fraction of its size. It publishes a genuinely strong quarterly reserves attestation and almost nothing else. There is no whitepaper of substance, no published bar list, no named custodian, and no wind-down plan. **Size and documentation quality are uncorrelated here, and XAU₮ is the proof.**

The commercial model is unusual and directly relevant to Aurumix: XAU₮ charges holders **nothing** to store their gold. There is no annual custody fee at all. This is the single most important commercial fact in this profile.

## 2. Legal structure

The reserves report is unusually explicit for a crypto issuer, and the language matters:

> "The physical gold bars held in the Gold Reserves meet the quality assurance requirements of 'London Good Delivery' set by the London Bullion Market Association. The Gold Reserves are vaulted in Switzerland. **The Gold Reserves are owned by the XAU₮ token holders, not by the Company.**"
> ([Reserves Report as of 30 June 2025](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_30.06.2025_RC187322025BD0179.pdf))

And:

> "Tether Gold (XAU₮) tokens are digital tokens that represent ownership of physical gold. **Holders of XAU₮ tokens have undivided ownership rights to gold on specified gold bars.** XAU₮s are created only following receipt of the corresponding gold by the Custodian."

This is a stronger ownership assertion than most tokenized gold products make. It claims a **direct undivided property interest in identified bars**, not a creditor claim against the issuer, and it positions the Company as a non-owner. The gold is stated to be held by the Custodian "as representative of the XAU₮ token holders". **Confidence: High** that this is the issuer's stated position, because it appears inside a document subject to reasonable assurance by BDO Italia.

Two important caveats, and they are material:

- **The assertion is not tested by the auditor as a legal conclusion.** BDO opines that the reserves report is "fairly presented in accordance with the criteria, including Management's Key Accounting Policies, set out therein". That is an accounting conclusion about quantities and valuation, not a legal opinion that title has effectively passed to token holders under Salvadoran or Swiss law. No trust deed, declaration of trust, bailment agreement or custody agreement is published. **Confidence: High** (this follows from the text of the opinion itself).
- **"Undivided ownership rights to gold on specified gold bars" is internally tense.** Undivided co-ownership of a pool and ownership of a *specified* bar are different legal constructs. With 611 bars of 12.5kg backing hundreds of thousands of tokens, holders plainly cannot each own a specified bar. Which construct governs on an insolvency is **Not disclosed**.

**What happens if TG Commodities fails is Not disclosed.** No published wind-down plan, no resolution procedure, no statement of how the Custodian would act, and no explanation of how a token holder would assert the claimed ownership right against a Swiss custodian without the issuer's cooperation. For an entity of this size this is a striking gap, and it matches the brief's observation that no gold token has published one.

## 3. Regulatory and compliance posture

**Verified against the register, and the widely repeated figure is wrong.**

The El Salvador CNAD public register lists:

| Register | Entity | Number | Date | Category |
|---|---|---|---|---|
| Issuers ([cnad.gob.sv/issuers](https://cnad.gob.sv/issuers/)) | **TG Commodities S.A. de C.V.** | **EME-0004** | 19/5/2025 | Issuer of Public Offerings of Stablecoins |
| Issuers | Tether International S.A. de C.V. | EME-0003 | 19/5/2025 | Issuer of Public Offerings of Stablecoins |

**Contradiction flagged.** Multiple secondary sources, and Tether's own Relevant Information Document as summarised in search results, state the registration number is **"PSAD-0032"**. Against the register, PSAD-0032 is a *Digital Asset Service Provider* number from a separate register (the PSAD register), and I could **not** locate TG Commodities in the PSAD list on the CNAD site. The number that verifies for the issuance activity is **EME-0004** on the issuer register. Both may be true simultaneously (El Salvador's LEAD requires an issuer to have a PSAD registered for placement and marketing), but anyone citing a single number for XAU₮ should cite **EME-0004** for the issuance and treat PSAD-0032 as unverified against the live register. **Confidence: High** on EME-0004, **Confidence: Low** on PSAD-0032.

Other regulatory facts, from the reserves report:

- Authorised as a **Stablecoin Issuer and Digital Assets Service Provider under the Digital Asset Issuance Law (LEAD) of El Salvador**, subject to the **National Commission of Digital Assets (CNAD)**.
- Registered as a **Money Services Business with FinCEN**, U.S. Department of the Treasury.
- Reports to the **Financial Investigation Unit of El Salvador**.

**The jurisdictional finding is the headline.** The largest tokenized gold product in the world is regulated by a stablecoin regime in **El Salvador**, a jurisdiction that created a bespoke digital-asset law to attract exactly this business, having moved there from the **British Virgin Islands in January 2025**. Note what it is *not*: it is not authorised by a securities regulator, not by a commodities regulator, and not by any major-market financial regulator. It is registered under a stablecoin law, and a gold token is being accommodated within a "stablecoin" category.

Also note it is **not** licensed by VARA, DFSA or ADGM despite marketing heavily into the Gulf (see §11 on the Shariah certification targeting the GCC). It reaches those markets through exchange listings and certification, not local licensing.

**No enforcement action against TG Commodities specific to XAU₮ was found.** Reputational risk is inherited from the Tether group rather than generated by the gold product.

## 4. Custody and proof of reserve

| Item | Status | Detail |
|---|---|---|
| Custodian | **Not disclosed** | Named only as "the Custodian" throughout every primary document. Secondary sources speculate Brink's/Loomis; **no primary source names it.** |
| Vault location | Switzerland | Country only. No city, no facility, no address. **Confidence: High** (stated in reserves report) |
| Allocated? | Yes, asserted | "undivided ownership rights to gold on specified gold bars"; bars are itemised by size and count |
| **Bar list** | **Not published** | Only an aggregate breakdown by bar size. No serial numbers, no refiner names, no per-bar assay data |
| PoR feed | Daily transparency page | gold.tether.to publishes daily, "updated at least once per day", with a stated lag between issuance and display |
| **Reserve attestation** | **Quarterly, BDO Italia S.p.A., ISAE 3000 (Revised) reasonable assurance** | This is genuinely strong. See below |
| Smart contract audit | Fragmentary | No first-party published audit located. **Confidence: Low** |

**The attestation deserves credit, and precision about what it does and does not say.**

The brief asks for a sharp distinction between a smart-contract audit and a reserve attestation. XAU₮ is a case where the reserve attestation is **better than the tokenized-gold norm**, and the smart-contract audit position is worse.

What the attestation actually attests to, from the [30 June 2025 BDO opinion](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_30.06.2025_RC187322025BD0179.pdf):

- It is a **reasonable assurance** engagement under **ISAE 3000 (Revised)**. Reasonable assurance is the higher of the two ISAE 3000 tiers, materially stronger than the limited-assurance or agreed-upon-procedures reports common in this sector. BDO states: "In our opinion, the TGRR ... is, in all material respects, fairly presented."
- Procedures included **physical inventory procedures** ("performing inventory procedures in order to confirm the existence of fine troy ounces"), reconciliation of the accounting ledger against "the ledgers on the various blockchains relating to liabilities", and **reports from a specialised provider on inventory and quality testing, on a sample basis**. Quarterly confirmatory assay testing of a **sample** of bars by a qualified independent third party is disclosed.

What it explicitly does **not** cover, and BDO says so directly:

- **"The reporting date is limited to a point in time as of 30 June 2025. We did not perform procedures or provide any assurance at any other date or time in this report."** A quarterly point-in-time snapshot says nothing about the other 89 days.
- **"The TGRR is prepared by Management for transparency purposes. As a result, the TGRR may not be suitable for another purpose."** It is not an audit of the company, not a financial statement audit, and not a legal opinion on title.
- Assay testing is **sample basis**, not every bar.
- It is not an opinion on solvency, on the adequacy of custody arrangements, or on the enforceability of holder ownership rights.

Net: **the reserve attestation is the strongest in the tokenized-gold set reviewed, and it is still only a quarterly point-in-time accounting opinion, from a firm whose Tether engagements have themselves drawn scrutiny.** The correct summary is "quarterly reasonable-assurance attestation with sampled assay testing, no bar list, unnamed custodian".

**The minted-versus-sold gap is a genuine subtlety.** As of 30 June 2025: 246,524.33 XAU₮ minted, of which **186,879.51 sold** and **59,644.82 "available for sale"**, held by **Alpha Group Commodities, S.A. de C.V.**, an affiliate that also relocated from the BVI to El Salvador in January 2025. As of 31 March 2026: **707,747.139 oz** in reserve against **559,598.64 XAU₮ sold**. So roughly **21% of minted supply is unsold affiliate inventory.** Anyone reading "market cap" off a supply figure is mixing customer-owned tokens with issuer-affiliate inventory. Circulating supply (612,823) and total supply (707,747) differ for this reason. **Confidence: High.**

## 5. Issuance

- Gold arrives first: "The Company issues XAU₮ tokens after physical gold bars containing a corresponding number of fine troy ounces of gold have completed the Custodian's intake procedure." Mint-after-delivery, not mint-then-fund. **Confidence: High.**
- **Minimum direct purchase: 50 XAU₮**, roughly US$200,000 at July 2026 prices. **Confidence: Medium.**
- Direct issuance is **full-KYC/AML gated**. **Confidence: Medium.**
- A pre-minted inventory held by affiliate Alpha Group Commodities allows direct customers to be filled from stock rather than triggering a fresh mint. **Confidence: High.**

**The practical consequence: XAU₮ has no retail primary market.** A 50-ounce minimum puts direct issuance out of reach of every retail saver. Retail buys XAU₮ on exchanges, in the secondary market, at whatever the market price is. The issuer's direct channel is wholesale-only in practice even if not in stated policy.

## 6. Redemption

- **Physical redemption minimum: approximately 430 XAU₮**, corresponding to one London Good Delivery bar (~US$1.73m at July 2026 prices). **Confidence: Medium**, from secondary sources; not confirmed against the issuer's own terms, which I could not retrieve (gold.tether.to is JavaScript-rendered and blocks direct fetching).
- **Redemption fee: 0.25%**, plus logistics, insurance and handling borne by the redeemer. **Confidence: Medium.**
- **Delivery is to a holder-nominated address in Switzerland.** Taking gold out of Switzerland is the holder's problem. **Confidence: Medium.**
- Full KYC/AML required. Sanctions and jurisdictional screening apply; the excluded-country list is **Not disclosed**.
- **Cash redemption from the issuer: Not disclosed.** No documented issuer-operated fiat redemption window was found. Cash exit is by selling on the secondary market.

**This is the gap between the ownership claim and the practical reality.** XAU₮ tells holders they have "undivided ownership rights to gold on specified gold bars", but exercising that right requires ~US$1.73m of tokens, a Swiss delivery address and a full KYC file. For any holder below one bar, the ownership right is economically theoretical: the only real exit is selling the token to someone else. The claim is legally stronger than most competitors and practically inaccessible to almost all holders, at the same time.

## 7. Fees and revenue model

| Fee line | Amount | Paid by | Confidence |
|---|---|---|---|
| Direct purchase / creation | 0.25% | Buyer | **Medium** |
| **Ongoing custody / storage** | **0.00%. None.** | n/a | **High** |
| Management fee | **None** | n/a | **High** |
| Redemption (to physical) | 0.25% + logistics, insurance, handling | Redeemer | **Medium** |
| Cash redemption from issuer | **Not disclosed** | n/a | n/a |
| On-chain transfer | Network gas only, no issuer-imposed transfer fee | Sender | **Medium** |
| Cross-chain (XAUt0) | Bridge/LayerZero costs, set by the bridge not the issuer | User | **Medium** |

**The zero-custody-fee model, and what actually funds it.**

XAU₮ charges holders nothing to store their gold, permanently. This is its central marketing differentiator against gold ETFs (which charge 0.15–0.40% per year) and against PAXG. The storage cost is real and someone pays it.

The disclosed fee lines (0.25% in, 0.25% out) cannot plausibly fund perpetual Swiss vaulting on their own for a long-duration holder. A holder who buys and holds for ten years pays 0.25% once and consumes ten years of allocated storage, insurance and quarterly assay testing. The arithmetic only works because of what is *not* in the fee table:

1. **Tether group cross-subsidy.** Tether Holdings earns very large returns on its USDT reserve portfolio. Vaulting ~19 tonnes of customer gold is a rounding error against that, and XAU₮ functions as a strategic product for the group rather than a standalone profit centre. **Confidence: Medium** (inferred from group structure; Tether does not publish XAU₮ segment economics).
2. **Float on unsold inventory.** ~21% of minted tokens sit as affiliate inventory. The group holds gold exposure on its own book alongside customer gold. Tether's total gold position has been reported at 140–162 tonnes, far exceeding the ~19 tonnes backing circulating XAU₮.
3. **Spread.** The issuer sells from inventory at a spread, which is not a disclosed "fee" but is a revenue line.

**Confidence: High** that no custody fee is charged. **Confidence: Medium** on the funding mechanism, which is inferred, not disclosed. **The issuer has never published a statement explaining what funds free perpetual storage.**

## 8. Token architecture

**Base token.** Standard **ERC-20** on Ethereum at `0x68749665ff8d2d112fa859aa293f07a622782f38`, six decimals, plus a **TRC-20** deployment on Tron. It is **not** a permissioned standard: it is a plain, freely transferable ERC-20. Anyone can hold it, anyone can send it to anyone, and the token carries no identity or eligibility logic.

**Admin controls.** Reporting is contested. Some analyses describe a transparent-proxy pattern with upgradeable logic and USDT-style freeze/blacklist powers held by Tether; automated audit tooling reports no blacklist or pause function present and does not classify it as a standard upgradeable proxy. **No address is known to have been frozen on the XAU₮ contract.** Tether has previously executed a contract upgrade/migration for XAU₮. Net: **Confidence: Low** on the precise admin surface. This is an open item, and notable in itself: for a US$2.5bn instrument, whether the issuer can freeze your gold token should not require inference.

**XAUt0, the omnichain layer, and why it matters.** In June 2025 Tether launched **XAUt0** via the **USDT0** infrastructure using **LayerZero's OFT (Omnichain Fungible Token)** standard, first on **TON**, then **Solana (Oct 2025)**, **Avalanche (Nov 2025)**, **Polygon**, **Stable**, **Conflux (Apr 2026)** and **BNB Chain (Mar 2026)**.

This creates a **two-tier claim structure that the documentation does not address**:

- XAU₮ on Ethereum is the canonical token carrying the stated undivided ownership right in Swiss gold.
- XAUt0 on seven-plus other chains is, under the standard OFT design, a **bridged representation** backed by canonical XAU₮ locked in a lockbox contract.

**Whether an XAUt0 holder on Solana or TON has the same legal claim on physical gold as an Ethereum XAU₮ holder is Not disclosed.** No published redemption path exists for XAUt0 without first bridging back to canonical XAU₮. Who controls the lockbox, and what happens to XAUt0 holders if the LayerZero bridge fails or is exploited, is **Not disclosed**. An XAUt0 holder is exposed to gold price risk, issuer risk, custodian risk **and** bridge risk, with the last of these entirely undocumented. Multi-chain reach was bought at the cost of claim clarity.

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Market cap | ~US$2.465bn |
| Circulating supply | 612,823 XAU₮ |
| Total supply | 707,747 XAU₮ |
| 24h volume | ~US$130.4m |
| Volume / market cap | **~5.3% daily turnover** |
| Price | ~US$4,021.73 (tracking gold) |
| Top venues | Binance XAUT/USDT ~US$12.5m; Gate ~US$11.7m; Bybit ~US$9.0m; OKX ~US$6.9m; XT.COM ~US$6.3m |

**This is the direct counter-example to the PGOLD data point in the brief, and it is important for Aurumix's premium thesis.**

PGOLD: ~US$79–90m AUM, ~US$1.7m liquidity, sub-US$20 daily volume. XAU₮: ~US$2.46bn AUM with ~US$130m daily volume, roughly **5.3% of market cap turning over every day** across five or more major venues each doing US$6m+.

So the brief's finding stands but needs refinement: **AUM does not produce liquidity, but scale plus tier-1 exchange listings does.** XAU₮ is genuinely liquid. It is also, precisely because it is liquid and arbitrageable against spot gold on major venues, **the protocol least likely to sustain a premium**. It trades at gold, not above it. Deep liquidity and a durable retail premium are opposed outcomes, not complementary ones.

Market share: XAU₮ has been reported at 54–60% of the entire gold-backed token market.

## 10. Distribution

- **Channels:** centralised exchange listings (Binance, OKX, Bybit, Gate, Bitfinex and many others), direct issuance for large tickets, and increasingly DeFi/collateral integrations.
- **Geography:** global via exchanges; explicit targeting of Indonesia (Mobee listing, July 2025) and, following the July 2026 Shariah certification, the **GCC, South Asia and parts of Africa**.
- **Savings plan / SIP / recurring purchase: None.** No systematic investment plan, no recurring contribution product, no fractional accumulation programme from the issuer.
- **Referral or affiliate programme: None found.** No agent network, no multi-tier commission structure, no distributor incentives.
- **Target segment:** effectively institutional, treasury and high-net-worth. A 50-ounce direct minimum and a 430-ounce redemption minimum define the customer.

**The finding here is stark and it is the brief's expectation confirmed at the top of the market.** The largest tokenized gold product on earth has **no retail distribution mechanism of its own**. It has no savings plan, no recurring purchase, no agent network and no referral programme. It acquires its US$2.46bn entirely through exchange listings, brand and institutional relationships. It is a wholesale product with a liquid secondary market, not a savings product.

## 11. Recent developments

- **27 July 2026:** XAU₮ receives **Shariah certification from Amanah Advisors**, led by **Mufti Faraz Adam**. The review covered "the token's ownership model, reserve transparency, physical backing, and compliance with Islamic rules governing gold transactions", confirming real ownership of physical gold, absence of riba, no leverage and no speculative derivatives. Tether explicitly targets the **GCC, South Asia and parts of Africa**. ([Tether](https://tether.io/news/xaut-tethers-gold-backed-digital-asset-receives-shariah-certification-unlocking-new-pathways-for-islamic-banks-institutions-and-individuals-worldwide/))
- **3 July 2026:** CoinGecko launches an RWA transparency tool featuring XAU₮'s peg to physical gold. **Confidence: Low.**
- **29 June 2026 (announced ~18 June 2026):** **Ledn partnership**: XAU₮ accepted as collateral for loans denominated in USDT and USAT, letting holders borrow against bullion without selling. Ledn states a **1:1 collateral policy with no rehypothecation**. **Not available in the EU or Canada.** ([Cryptobriefing](https://cryptobriefing.com/tether-ledn-tokenized-gold-xaut/))
- **April 2026:** XAUt0 launches on **Conflux**.
- **~31 March 2026 (Q1 2026 attestation):** Reserves reach **707,747.139 fine troy ounces**, value above **US$3.3bn**, a **36% quarter-on-quarter increase**; tokens sold 559,598.64 XAU₮. ([Tether](https://tether.io/news/tether-gold-surpasses-3-3-billion-as-reserves-surge-36-in-q1-driven-by-flight-to-hard-assets/))
- **26 March 2026:** XAU₮ listed on **BNB Chain** via the USDT0 infrastructure layer, described as unified liquidity across 12+ chains. ([Tether](https://tether.io/news/tether-gold-the-worlds-leading-tokenized-gold-product-to-be-listed-on-bnb-chain/))
- **26 January 2026:** Tether announces XAU₮ **surpasses US$4bn in value** and accounts for **more than half** of the gold-backed stablecoin market. (Note: this figure exceeds the ~US$2.46bn market cap observed in July 2026; the US$4bn likely reflects total minted supply at a peak gold price rather than circulating market cap. **Treat the US$4bn as a marketing figure.**)
- **26 December 2025:** Reuters reports Tether bought **~27 tonnes of gold in Q4 2025**, holding **~162 tonnes** across the group, of which only a minority backs circulating XAU₮.
- **24 November 2025:** XAUt0 deploys on **Avalanche**.
- **28 October 2025:** Attestation shows **375,572.297 fine troy ounces** against 375,572.247 XAU₮, ~US$2bn.
- **16 October 2025:** XAUt0 deploys on **Solana**.
- **21 July 2025:** XAU₮ listed on **Mobee** (Indonesia).
- **June 2025:** **XAUt0 launched on TON** via USDT0 and LayerZero OFT, the first omnichain deployment.
- **19 May 2025:** **TG Commodities registered with CNAD as issuer EME-0004.** ([CNAD](https://cnad.gob.sv/issuers/))
- **Q1 2025:** First public XAU₮ attestation released, >7.7 tonnes backing circulating tokens.
- **January 2025:** **TG Commodities, S.A. de C.V. and Alpha Group Commodities, S.A. de C.V. relocate from the British Virgin Islands to El Salvador.** The single most consequential structural event in the period.

**No depeg, incident, exploit, sustained discount or enforcement action specific to XAU₮ was found in the period.**

## 12. Relevance to Aurumix

**Q1. Custody fee mechanism. This is the most directly useful finding in the profile.**

XAU₮ takes the third option the brief identifies: **charge holders nothing and recover the cost elsewhere.** No custody fee, no management fee, no grams deducted, ever. It never faces Aurumix's peg-breakage problem because it never touches the gold to pay for storage.

The reason it can do this is a cross-subsidy Aurumix does not have. Free storage is funded by a group earning enormous returns on a separate US$100bn+ stablecoin reserve book, by spread on affiliate inventory, and by a group gold position (140–162 tonnes) many times larger than the ~19 tonnes backing circulating XAU₮. **Aurumix cannot copy the zero-fee model without a comparable external subsidy, and it should not assume one.**

But the strategic lesson transfers cleanly and it is worth stating plainly: **the market leader charges zero ongoing custody fee.** Any Aurumix custody fee is a competitive disadvantage against XAU₮ on a like-for-like basis, and must be justified by the savings-plan wrapper, the agent servicing and the credit facility rather than by the gold storage itself. If Aurumix charges in cash (the leaning in the brief), the messaging problem is that XAU₮ charges nothing. Aurumix's answer has to be that it is selling a savings programme with distribution and credit attached, not a cheaper vault.

**Q2. Dividend funding. XAU₮ pays nothing, and that is the cleanest available evidence for the securities argument.**

The largest, best-capitalised, most liquid tokenized gold product in the world, sitting inside a group with one of the largest profit pools in crypto, **pays its gold-token holders zero yield.** No dividend, no staking, no APY. Its Shariah certification explicitly rests on the **absence of interest-based mechanisms, leverage and speculative derivatives**.

Tether could trivially afford to pay a yield on 19 tonnes of gold. It does not. The most plausible reading is that paying holders a return on a passive asset converts a commodity token into something that looks like an investment contract, and the issuer has chosen not to take that risk even though it has the money. **This is the strongest external support in the set for the brief's concern about the ICS Dividend.** Aurumix should note that its two nearest reference points diverge completely: PGOLD promises 5% it cannot fund, XAU₮ promises nothing and is the market leader. Yield is not what wins this category.

Where XAU₮ *does* let holders monetise without selling is **credit, not dividend**: the Ledn partnership (June 2026) allows borrowing against XAU₮ collateral, explicitly with **no rehypothecation**. **This directly validates Aurumix's credit facility and Gold Card as the better-designed value-add than the dividend.** It provides holder utility, generates issuer revenue, does not encumber the gold, and does not create a securities-classification problem. Note also that Ledn excludes the EU and Canada, which is a useful precedent for jurisdictional gating of a credit product.

**Q3. Token standard. XAU₮ is a plain ERC-20, and its choice cost it nothing because it has nothing to protect.**

XAU₮ carries no tier standing, no dividend entitlement, no credit eligibility and no buyback right. It is a bearer claim on an ounce of gold. A plain ERC-20 is therefore exactly correct for it: maximum transferability, maximum exchange listability, maximum liquidity, no compliance logic needed at the token layer. Its US$130m daily volume is a direct product of that choice.

**This confirms rather than challenges Aurumix's ERC-3643 lean, and it also prices it.** XAU₮ demonstrates what permissionless buys: deep liquidity, universal listings, ~5.3% daily turnover. Aurumix's ICS, dividend, credit eligibility and buyback rights all break on an anonymous transfer, so it cannot have that. The tradeoff should be made with eyes open: **choosing ERC-3643 means accepting that Aurumix will never have XAU₮-like secondary liquidity, and therefore that the cash buyback is the only real exit.** That is coherent, but it means the buyback must be resourced properly, because there is no deep market to fall back on.

The XAUt0 experience is a second, subtler warning. Tether extended to seven-plus chains via a LayerZero wrapper and in doing so created a class of holders whose legal claim on the gold is undocumented. **If Aurumix ever wraps a permissioned base token into a transferable ERC-20 for liquidity, it will create exactly this problem: a wrapper holder who has the economic exposure but none of the ICS standing, dividend entitlement or credit eligibility.** Aurumix must decide in advance what a wrapped AURX holder actually owns, and write it down. XAU₮ did not, and at US$2.5bn it still has not.

**Q4. Regulatory route. A large, sophisticated issuer chose a bespoke small-jurisdiction regime over a major-market licence.**

TG Commodities moved from the BVI to El Salvador in January 2025 and registered under the LEAD as **CNAD issuer EME-0004**. It is licensed by a purpose-built digital-asset regulator in a small jurisdiction, not by a securities or commodities regulator, and **not by VARA, DFSA or ADGM**, despite now actively marketing into the GCC.

This is directly instructive for Aurumix's cost/benefit on VARA. The market leader concluded that a light-touch bespoke regime plus global exchange distribution beat an expensive major-market licence. **However, the analogy has a hard limit that Aurumix must not gloss over:** XAU₮ is a pure custody receipt with no yield, no credit and no retail savings plan, so it fits a "stablecoin issuer" box cleanly. Aurumix's hybrid (dividend + credit + SIP + agent network) does not fit any single box anywhere, which is precisely why its regulatory problem is harder than XAU₮'s despite being 1/100th the size. XAU₮'s route is available to Aurumix only if Aurumix strips back to the gold core.

Also note the **Shariah certification (July 2026)** as a distribution instrument rather than a licence. Tether reached the GCC and South Asia through certification plus exchange listings, without local licensing. **For a product targeting India, the UAE and NRIs, Shariah certification is a cheap, fast, high-leverage credential that Aurumix should price into its plan.** Amanah Advisors and Mufti Faraz Adam are a named, checkable precedent. Aurumix's gold core should certify easily; its **ICS Dividend and its 90–95% LTV credit facility are the parts that will attract scrutiny**, since riba and leverage are exactly what the XAU₮ certification confirmed were absent. That is a second, independent reason to be cautious about the dividend.

**Q5. Redemption. XAU₮ has physical redemption on paper and effectively none in practice.**

A ~430 XAU₮ minimum (~US$1.73m), Swiss-only delivery, full KYC, 0.25% plus logistics. Aurumix should take real comfort here: **the market leader's redemption right is inaccessible to essentially every retail holder.** The gap between "you own physical gold" and "you can get it" is not unique to Aurumix, it is the industry norm.

The honest differentiator is disclosure, not the right itself. XAU₮ asserts strong ownership language while gating redemption at 1.73 million dollars. **Aurumix saying plainly "no physical redemption, cash buyback only" is more transparent than XAU₮'s position, and Aurumix should say so rather than treating it as a weakness to hide.** The brief already identifies this as a gap; the XAU₮ evidence suggests it is better framed as candour.

**Q6. Premium and liquidity. XAU₮ is the strongest evidence yet against the 3–8% premium thesis.**

XAU₮ has ~US$2.46bn AUM and ~US$130m daily volume, ~5.3% turnover, across five-plus venues each doing US$6m+. It is arbitraged continuously against spot gold and **trades at gold, not above it.**

This sharpens the brief's PGOLD finding into a general rule: **liquidity and premium are inversely related.** PGOLD has no liquidity and no reliable premium. XAU₮ has excellent liquidity and no premium, because arbitrage kills it. **A durable 3–8% premium cannot survive a liquid market.** If Aurumix's premium thesis depends on AURX trading above NAV, that premium can only exist in a market too thin or too closed to arbitrage, which is in tension with any liquidity ambition and makes the premium fragile and hard to defend to a regulator. **Aurumix should stress-test the revenue model with the premium set to zero.** The permissioned/ERC-3643 route, by limiting free transfer, is arguably the only structure in which a controlled premium is sustainable at all, and if so that should be stated as a deliberate design choice rather than a side effect.

**Q7. Proof of reserve. XAU₮ sets the benchmark Aurumix should aim at, and it is achievable.**

Quarterly **ISAE 3000 (Revised) reasonable assurance** by a Big Four-adjacent firm (BDO Italia), including physical inventory procedures, sampled third-party assay testing, and reconciliation of the ledger against on-chain liabilities, plus a daily transparency page. That is meaningfully better than the tokenized-gold norm and it is the standard a serious UAE retail product should match.

The remaining gaps tell Aurumix where cheap differentiation is: **no published bar list, no named custodian, sampled rather than full assay, point-in-time quarterly snapshots.** **Naming its custodian and publishing a bar list would put Aurumix ahead of a US$2.5bn incumbent on transparency at near-zero cost.**

Also carry forward the sharp distinction the brief asks for: XAU₮'s reserve attestation is strong, its **smart-contract audit position is weak and largely unverifiable**. The two are not the same thing and XAU₮ is a good example of an issuer being much better at one than the other. Aurumix should publish both, separately labelled.

**Q8. Distribution. This is where Aurumix's actual moat is, and XAU₮ proves it.**

XAU₮ has **no savings plan, no recurring purchase, no referral programme, no agent network** and a US$200,000 direct minimum. It is a wholesale product. **The largest tokenized gold product in the world does not compete with Aurumix for the retail monthly saver at all.** It is not a distribution competitor; it is a liquidity venue and a benchmark.

The strategic read: XAU₮ owns institutional and treasury demand and will keep owning it. The US$20-a-month Indian or NRI saver is a market it has made no attempt to serve. **Aurumix's SIP and 3-tier agent network are not a weaker version of XAU₮'s model, they are a different business.** The correct competitive posture is not to out-vault XAU₮ but to out-distribute it, and to be honest internally that Aurumix's product risk is a distribution and compliance risk (agent network, commissions, mis-selling, KYC at scale), not a gold-custody risk.

Note also the Shariah certification targeting **"GCC, South Asia and parts of Africa"**: XAU₮ is now aiming marketing at Aurumix's exact geographies, even though its product cannot serve a retail saver. Aurumix should expect XAU₮ brand presence in its markets without direct product competition.

**Q9. Wind-down. XAU₮ has none, at US$2.5bn.**

No published wind-down plan, no resolution procedure, no statement of what happens to the gold or how holders would assert their claimed ownership rights against an unnamed Swiss custodian if TG Commodities failed. This confirms the brief's finding at the very top of the market.

**Aurumix committing to a published wind-down plan would differentiate it against the US$2.5bn category leader, not just against failed micro-caps.** That reframes the cheap-differentiation argument considerably: it is not a courtesy to a sceptical retail buyer, it is a gap that literally nobody in the category has filled.

### Contradictions and corrections to the brief

1. **The brief's PGOLD-derived premium/liquidity finding needs refining, not overturning.** "AUM does not imply liquidity" is right, but XAU₮ shows that scale plus tier-1 listings does produce real liquidity (~5.3% daily turnover), and that this liquidity **eliminates** the premium. The sharper statement is that **premium and liquidity are inversely related**, which is a more useful and more uncomfortable finding for Aurumix's revenue model than the PGOLD case alone.
2. **The task brief describes the issuer as "TG Commodities Limited or successor".** The current issuer is **TG Commodities, S.A. de C.V.**, an El Salvador entity, following relocation from the **British Virgin Islands in January 2025**. "TG Commodities Limited" is the superseded BVI name and should not be used for anything current. This is the same class of jurisdiction error the brief warns about with ORO, and it collapsed against the register in the same way.
3. **The widely cited registration number "PSAD-0032" does not verify against the CNAD register for issuance.** The verified issuer entry is **EME-0004**, dated 19 May 2025. Cite EME-0004.
4. **"MODERATE documentation" is the right grade but for a counterintuitive reason.** XAU₮'s *reserve attestation* is the best in the set (ISAE 3000 reasonable assurance, quarterly, with physical inventory and sampled assay). Its *legal and structural* documentation is among the weakest: no retrievable public terms of service, no named custodian, no bar list, no wind-down plan, no clear XAUt0 claim structure, and an admin-key surface that cannot be established from public sources. **It is excellent at proving the gold exists and poor at explaining what you own and what happens if things go wrong.** A protocol 250x smaller documenting itself better is not a paradox: scale removes the pressure to explain yourself, because liquidity and brand substitute for disclosure. Aurumix, without that brand, has to explain itself.

## 13. Open items for verification

- [ ] Retrieve the actual **Tether Gold Terms of Sale / Terms of Service** from `https://gold.tether.to/legal` (JS-rendered; use a headless browser or archive snapshot). Confirm the 430 XAU₮ redemption minimum, the 0.25% fees and the 50 XAU₮ purchase minimum against the issuer's own terms rather than secondary sources.
- [ ] Confirm whether the Terms contain **any insolvency, wind-down or resolution clause**, and how holder ownership rights would be asserted against the custodian if TG Commodities failed.
- [ ] Retrieve the full **Relevant Information Document** PDF (`https://gold.tether.to/Relevant Information Document - TG Commodities, S.A. de C.V..pdf`) and extract the exact registration number(s) it cites, to resolve the **EME-0004 vs PSAD-0032** discrepancy.
- [ ] Search the **CNAD PSAD register** page by page for TG Commodities to confirm or eliminate PSAD-0032.
- [ ] Determine the **actual admin surface of the Ethereum XAU₮ contract**: read the verified source directly for blacklist/freeze/pause functions, proxy pattern and the owner address. Resolve the conflict between the automated audits and the secondary reporting.
- [ ] Identify **who controls the XAUt0 lockbox** and whether any published document states that an XAUt0 holder has the same claim on physical gold as a canonical XAU₮ holder.
- [ ] Establish whether the **physical gold custodian** is named in any filing, insurance certificate or Salvadoran regulatory submission. Test the Brink's/Loomis attribution, which currently rests only on secondary sources.
- [ ] Confirm the **cash redemption** position: does TG Commodities operate a fiat redemption window at all, or is the secondary market the only cash exit?
- [ ] Obtain the **Q2 2026 attestation** (expected ~July 2026) to confirm current tonnage and the minted-versus-sold gap.
- [ ] Reconcile the **January 2026 "US$4bn" claim** against the ~US$2.46bn July 2026 market cap. Determine whether the difference is gold price movement, total-versus-circulating supply, or marketing.
- [ ] Obtain the **Amanah Advisors Shariah certificate** itself and check the reasoning on gold ownership and constructive possession (*qabd*), which will be directly reusable for Aurumix's own certification, and note what it says about leverage that may bear on Aurumix's credit facility.
- [ ] Locate any **first-party smart-contract audit** commissioned by Tether for XAU₮, to confirm whether one exists at all.

---

# Pax Gold (PAXG)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | PAXG | **High** |
| Issuer (marketing) | Paxos, "Paxos Trust Company" | **High** |
| Issuer (registry) | **Paxos Trust Company, National Association**: a US federally chartered uninsured national trust bank. Converted from a NYDFS limited-purpose trust company on 12 December 2025 ([OCC NR 2025-125](https://www.occ.gov/news-issuances/news-issuances/news-releases/2025/nr-occ-2025-125.html), [Paxos newsroom](https://www.paxos.com/newsroom/occ-approves-paxos-application-to-convert-to-occ-trust-paxos-to-complete-conversion-imminently-to-become-a-federally-regulated-blockchain-infrastructure-provider)) | **High** |
| Domicile | United States (national charter; Paxos HQ New York) | **High** |
| Backing claim | 1 PAXG = 1 fine troy ounce of an LBMA London Good Delivery bar, allocated, serial-numbered | **High** |
| Chains | Ethereum (primary); Solana added ~25 June 2026 | Ethereum **High**, Solana **Medium** |
| Contract address(es) | Ethereum: `0x45804880de22913dafe09f4980848ece6ecbaf78`. Solana mint: **Not disclosed** in any Paxos primary source found | Ethereum **High** |
| Supply | ~444,808 PAXG ≈ 444,808 fine troy oz ([CoinGecko, 28 Jul 2026](https://www.coingecko.com/en/coins/pax-gold)) | **Medium** |
| Market cap / TVL | ~$1.79bn at ~$4,027/token | **Medium** |
| Regulatory status | OCC-supervised national trust bank; PAXG issued "pursuant to specific approval from the OCC" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). No OCC licence *number* published | **High** |
| Subscription fee | Tiered 1.000% down to 0.125% by order size; **currently waived** on creations under a promotion ([Paxos fee page](https://support.paxos.com/articles/2899561282-pax-gold-fees)) | **High** |
| Ongoing custody fee | **Zero at present.** "Paxos does not charge gold storage fees to its customers at this time" | **High** |
| Redemption fee | Same tiered 1.000%–0.125% destruction schedule; physical bar delivery fee stated only in the User Guide | Tiers **High**, bar fee **Low** |
| Advertised yield | **None. PAXG pays no yield of any kind.** | **High** |
| Named officers | **Not disclosed** on PAXG product or terms pages (Charles Cascarilla is publicly Paxos CEO, but no officer is named as responsible for PAXG) | **Medium** |

---

## 1. What it is

PAXG is a gold-denominated token issued by Paxos Trust Company, N.A. Each token represents one fine troy ounce of a specific, serial-numbered London Good Delivery bar held in LBMA-approved vaults in London ([paxos.com/pax-gold](https://www.paxos.com/pax-gold)). It launched in September 2019 and is the largest tokenized-gold product by market capitalisation other than Tether Gold.

The product is deliberately narrow. It is a **custody receipt with an on-chain wrapper**, nothing more. There is no savings plan, no yield, no tiering, no credit facility, no referral network. Everything Aurumix layers on top of a gold core, PAXG has consciously omitted. That is the point of comparison: PAXG is what the regulated-minimum version of this product looks like, and it has reached ~$1.79bn doing only that.

## 2. Legal structure

This is the strongest disclosure of any protocol in this landscape, and the language is unusually precise.

The PAXG Terms and Conditions state that "**Your PAXG tokens are akin to a warehouse receipt representing your beneficial ownership of a pro rata portion of Allocated Gold**" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). **Confidence: High.**

Three things follow, and they matter:

- **Beneficial ownership, not legal title.** The holder does not hold legal title to a bar. Paxos holds the bars; the holder has a beneficial interest in a pro rata share of the allocated pool. Paxos expressly reserves the right to **reallocate** which specific bars back which holders "for operational efficiency". So the serial number you look up is real but not permanently yours.
- **Allocated, not unallocated.** The terms define Allocated Gold as "a specific gold bar held in an LBMA-approved security carrier vault, identifiable by a unique serial number, weighting and purity percentage," and separately define Unallocated Gold as "a liability of such institution whereby the holder of unallocated gold owns a claim to an equivalent balance of gold." PAXG is backed by the former. This is the distinction most gold tokens blur, and Paxos does not blur it.
- **Bankruptcy remoteness is claimed but asymmetrically documented.** The Paxos blog asserts "We're required to hold all customer funds in segregated, bankruptcy remote accounts" and "your gold bars will always be yours, even in the unlikely case something happens to Paxos" ([Paxos blog](https://www.paxos.com/blog/pax-gold-the-safest-way-to-own-gold-today)). **Confidence: Medium**, because that is a marketing page. **The terms themselves contain no Paxos-insolvency clause.** They do contain a detailed clause disclaiming liability for a *Clearing Bank* insolvency ("Paxos is not responsible for any losses associated with any default by a Clearing Bank... including but not limited to, insolvency, default, or operational error") but nothing comparable governing the failure of Paxos Trust Company itself. **The marketing makes a bankruptcy-remoteness promise the legal document does not restate.** That gap is worth noting precisely because Paxos is otherwise the best-documented issuer here.

Counterweight: the OCC national trust charter is itself the substantive protection. A national trust bank holds fiduciary assets off its own balance sheet by operation of banking law, which is a stronger structural claim than any contract clause. Paxos is relying on the charter rather than on drafting.

## 3. Regulatory and compliance posture

**This is the finding that contradicts the working brief.** The task framing (and most secondary sources still in circulation) describes PAXG as sitting under a **NYDFS trust charter**. That has not been true since December 2025.

- **11 August 2025:** Paxos filed to convert its NYDFS limited-purpose trust charter to a national trust charter ([Paxos newsroom](https://www.paxos.com/newsroom/paxos-to-pursue-national-trust-charter-with-the-office-of-the-comptroller-of-the-currency)). **Confidence: High.**
- **12 December 2025:** the OCC conditionally approved five national trust bank charters, including the conversion of Paxos Trust Company into an uninsured national trust bank. The other four were Ripple National Trust Bank and First National Digital Currency Bank (de novo), plus BitGo Bank & Trust, N.A. and Fidelity Digital Assets, N.A. (conversions) ([OCC NR 2025-125](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-125.html)). **Confidence: High.**
- Paxos completed the conversion the same day, and states "all of Paxos Trust Company's US-based activity will be subject to OCC supervision." The entity is now styled **Paxos Trust Company, N.A.** **Confidence: High.**
- The PAXG terms now say "Paxos Trust issues PAXG pursuant to specific approval from the OCC." **Confidence: High.**

**Regulator: OCC. Licence: national trust bank charter (uninsured), granted 12 December 2025.** No public charter number was found on the OCC release or on Paxos pages. **Not disclosed.**

Residual inconsistency to flag: the PAXG transparency page still describes NYDFS as the body approving the choice of auditor ([paxg-transparency](https://www.paxos.com/paxg-transparency)). Paxos has not uniformly updated its own site post-conversion, so **any source dated before December 2025, and some of Paxos's own pages, will state the wrong regulator.**

What was checked and not found: no VARA, ADGM, DFSA, MAS or EU/MiCA authorisation for PAXG was located. The recency sweep returned "not found" on all of these. **Not disclosed.** PAXG appears to be a purely US-chartered product distributed globally through exchanges.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian (legal) | Paxos Trust Company, N.A. | **High** |
| Vault operator | **Brink's**, London. Paxos's own blog: "We store gold reserves with Brink's bullion vaults in London" ([Paxos blog](https://www.paxos.com/blog/pax-gold-the-safest-way-to-own-gold-today)). Note the PAXG product page says only "LBMA vaults in London" | **High** (blog is a Paxos primary page) |
| Vault city | London | **High** |
| Allocated? | Yes: specific serial-numbered LBMA Good Delivery bars, with a contractual right for Paxos to reallocate | **High** |
| Bar list | **Partial.** There is a per-address **allocation lookup**: enter your Ethereum address and see the serial number, value and physical characteristics of your bars. There is **no full public bar list** of all bars backing total supply | Lookup **High**; absence of full list **Medium** |
| PoR feed | **Not disclosed.** No Chainlink or other on-chain proof-of-reserve oracle for PAXG was found | **Medium** |
| Reserve attestation | **Monthly**, by **KPMG LLP** since February 2025, previously WithumSmith+Brown, under AICPA attestation standards. Published at [paxos.com/paxg-transparency](https://www.paxos.com/paxg-transparency), reports listed through June 2026 | **High** |
| Annual physical bar audit | Claimed by one secondary source (Bureau Veritas). **Could not be confirmed against Paxos or Bureau Veritas primary sources: treat as unverified** | **Low** |
| Smart contract audit | Ethereum contract audited pre-launch; the Solana deployment was audited by **Zellic**. No PAXG-specific audit PDF was located on paxos.com | **Medium** |

**The attestation/audit distinction, stated plainly:** PAXG has a genuine *reserve attestation* (monthly, Big Four, AICPA standards, published as a time series) **and** separately a *smart contract audit*. These are two different things and Paxos is one of the few issuers that does both and does not conflate them in its own copy. For Aurumix, KPMG monthly is the benchmark a retail buyer will have seen; anything less frequent or less credentialed will read as a downgrade.

The honest gap: **a per-address lookup is not a bar list.** A holder can verify their own slice but cannot independently sum the pool. Total-supply verification still depends on trusting KPMG's monthly snapshot. Between snapshots there is no continuous on-chain proof.

## 5. Issuance

Tokens are created only when gold is purchased and vaulted, on a 1:1 basis with fine troy ounces. Issuance runs through a verified Paxos account: "Only verified Customers may purchase PAXG from us or convert or redeem PAXG from us" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). Full KYC at the mint and redeem boundary; free circulation in between.

Minimum purchase is **0.03 PAXG** (roughly $120 at July 2026 prices), driven by a 0.02 PAXG internal conversion cost. The token is divisible to 18 decimals, and there is no minimum holding. So the *minting* minimum is meaningfully above Aurumix's $20 SIP floor, but the *holding* minimum is effectively zero: small buyers are expected to acquire PAXG on the secondary market rather than mint it.

## 6. Redemption

PAXG offers three exits, and this is the most complete redemption stack in the landscape:

1. **To USD**, at market, at any time, via a Paxos account.
2. **To Unallocated Gold** by wire to a bullion account. Marketing frames this as institutional.
3. **To physical Allocated Gold bars.** Minimum **430 PAXG plus the fee set out in the Paxos User Guide, per London Good Delivery bar**. Conversions to USD round down to the nearest 1/100th of a troy ounce.

At ~$4,027/oz, a 430 PAXG bar redemption is roughly **$1.73m**. Physical delivery is therefore real but structurally out of reach for retail: it is a credibility mechanism for the peg, not a retail feature. Paxos also pushes delivery risk onto the holder: "You are responsible for delivery and once your bars are in the possession of the delivery service you choose, then Paxos will have been deemed to have fulfilled its obligation for delivery."

Eligibility is defined by KYC verification, not by an undefined "qualified holder" test. That is cleaner than several peers.

**A serious asymmetry to carry forward:** the terms give Paxos sweeping discretionary power over both token and metal. In capitals: "WE MAY FREEZE, TEMPORARILY OR PERMANENTLY, YOUR USE OF, AND ACCESS TO, PAXG OR THE LONDON GOOD DELIVERY GOLD BARS BACKING YOUR PAXG, WITH OR WITHOUT ADVANCE NOTICE." And on illegality: PAXG "AND THE ASSETS BACKING SUCH PAX MAY BE FORFEITED," and may "BECOME WHOLLY AND PERMANENTLY UNRECOVERABLE AND UNUSABLE." So the beneficial-ownership claim in §2 is real but conditional on Paxos's compliance discretion.

## 7. Fees and revenue model

| Fee line | Amount | Notes | Confidence |
|---|---|---|---|
| Creation (mint) | Tiered by order size: 0.02 PAXG flat for 0.03–2 PAXG; 1.000% (2–25); 0.750% (25–50); 0.500% (50–75); 0.250% (75–200); 0.150% (200–800); 0.125% (800+) | **Currently waived** on creations under a promotion running to a date the page renders as "09/31/26" (a typo; September has 30 days) | **High** |
| Destruction (redeem) | Same tiered schedule, not waived | Applies only through the Paxos wallet, **not** on exchange order-book trades | **High** |
| Storage / custody | **$0.00.** "Paxos does not charge gold storage fees to its customers at this time" | See below: the terms reserve the right to start | **High** |
| On-chain transfer fee | Contract supports a fee, historically 0.02%. Currently understood to be **set to zero**; users pay gas only | **Medium**: fee parameter state not independently read on-chain | **Medium** |
| Inactivity fee | **US$2.00/month** after 12 months with a non-zero balance and no issuance or redemption activity | **High** |
| Banking fees | Passed through at cost | **High** |
| Physical bar delivery fee | Stated only in the User Guide; secondary sources cite $20 domestic / $30 international, unconfirmed | **Low** |

**This is the single most decision-relevant part of the profile for Aurumix, and it answers design question 1 directly.**

PAXG's answer to the custody-fee problem is **option three from the brief: charge holders nothing recurring and recover cost elsewhere.** The ongoing storage fee is zero. Revenue comes from *transaction* events (destruction fees on redemption, creation fees when the promo lapses, the $2 inactivity fee) plus, critically, Paxos's ability to cross-subsidise from a much larger stablecoin and infrastructure business. PAXG does not have to pay for itself.

**But the terms document the fallback mechanism, and it is exactly the mechanism Aurumix has ruled out.** If Paxos ever does charge storage, it will do so like this: "Paxos may charge storage fees to all token holders by **issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens**. The storage fee will be in line with industry practice, and such storage fee will be passed on to all PAXG token holders on a pro rata basis" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). **Confidence: High.**

Read that against Aurumix's peg. PAXG's peg is *one token = one ounce*, so minting new tokens against an unchanged gold pool **breaks the 1:1 claim**: after a dilution event, one PAXG is backed by slightly less than one ounce. Paxos has reserved the right to break its own headline promise, disclosed it in the terms, and then never used it.

Aurumix's peg is *price = grams ÷ tokens*, which is the arithmetic inverse: Aurumix can mint dilutively without breaking its peg formula (the price simply falls), whereas deducting **grams** breaks it. So **the Paxos mechanism is actually peg-compatible for Aurumix and peg-breaking for Paxos.** Minting new AURX to the treasury reduces price-per-token exactly like a fee, keeps the grams-to-tokens identity intact, requires no cash collection from a SIP saver, and is enforceable against holders who never interact with the platform. It is the cleanest available answer to design question 1, and there is a Big Four-attested, OCC-supervised precedent for the drafting.

## 8. Token architecture

- **Standard: plain ERC-20** on Ethereum at `0x45804880de22913dafe09f4980848ece6ecbaf78`, 18 decimals. **Not** ERC-3643 or any permissioned standard. **Confidence: High.**
- **Permissioned?** No, at the transfer layer. Anyone can hold and transfer PAXG; permissioning applies only at mint and redeem, where KYC is mandatory. This is the "KYC at the boundary, free in the middle" model.
- **Upgradeability:** proxy pattern with a separate implementation contract. **Confidence: Medium.**
- **Admin keys:** the contract defines an owner/admin, a **supply controller** (mint/burn), a **fee controller** (sets transfer fee rate and recipient), and an **asset protection role** able to **freeze accounts and wipe balances**. The freeze-and-wipe capability is what makes the §6 forfeiture language enforceable on-chain. **Confidence: Medium** on the exact role names, **High** that freeze/seize capability exists (the terms assert it in capitals).
- **Solana:** added around 25 June 2026 using **Token-2022**, which carries native compliance extensions, with Zellic as auditor, Sunrise DeFi as DeFi integration partner and LayerZero Stargate for bridging. **Confidence: Medium.** The mint address is **Not disclosed** in any Paxos primary source found; a "Portal"-wrapped PAXG also exists on Solana and should not be confused with the Paxos issuance.

**What this choice buys and costs, for design question 3.** PAXG chose maximum composability: an anonymous ERC-20 lists on any exchange, enters any DEX pool, and collateralises any lending market without integration work. That is precisely how it got to $105m of daily volume. The cost is that PAXG can carry no holder-level state whatsoever, and Paxos accepted that cost because PAXG has no holder-level state to carry: no tier, no dividend, no credit standing.

Aurumix cannot make the same trade, because ICS standing, dividend entitlement, credit eligibility and buyback rights are all holder-level state that an anonymous transfer destroys. **The relevant lesson is not "copy the ERC-20", it is that Paxos's freedom to use a plain ERC-20 is a direct consequence of its product minimalism.** Note also that Paxos, having chosen an open standard, then bolted freeze-and-wipe admin powers onto it: it wanted permissioned control without a permissioned standard. The Solana move to Token-2022 (compliance extensions built in) suggests that where a compliance-native standard is available, Paxos now takes it. That is mild support for Aurumix's ERC-3643 lean.

## 9. Liquidity and market

As at 28 July 2026 ([CoinGecko](https://www.coingecko.com/en/coins/pax-gold)). **Confidence: Medium** (market aggregator, not issuer):

- Price ~**$4,027** per token
- Market cap ~**$1.79bn**
- 24h volume ~**$105.6m**
- Circulating supply ~**444,808** tokens ≈ 444,808 fine troy oz (~13.8 tonnes)
- All-time high $5,619.09 (January 2026); ATH is a gold-price artefact, not a premium event

**Volume/AUM ratio ≈ 5.9% per day.** Set that against the brief's PGOLD benchmark: ~$79–90m AUM on sub-$20 daily volume, a ratio near zero. PAXG turns over more value in a day than PGOLD holds in total.

**This is the direct evidence on design question 6, and it argues against the premium thesis.** PAXG is the most liquid tokenized gold product with a genuine physical redemption channel, and it trades **at or extremely near NAV**, not at a 3–8% premium. That is not an accident: deep liquidity plus a credible (if high-minimum) arbitrage path is exactly what *destroys* a premium. Any 430-PAXG-plus holder can arbitrage a persistent premium away by minting.

The uncomfortable conclusion for Aurumix: **a sustained 3–8% premium and a liquid market are not merely separate problems, they are in tension.** A premium survives only where arbitrage is blocked, which in practice means thin liquidity or closed redemption. Aurumix has no physical redemption at all, so it *can* in principle sustain a premium; but the mechanism sustaining it would be the absence of an arbitrage path, and that is a fragile and hard-to-defend basis for a retail value story. PAXG is the counter-example that shows what "liquid and credible" actually prices at: par.

## 10. Distribution

- **Channels:** direct via paxos.com / Paxos wallet (KYC'd), plus very broad third-party exchange listings (Binance, Kraken, Coinbase, Gemini, Backpack, BitMart and others), and now Solana DeFi via Sunrise DeFi.
- **Target segment:** self-directed crypto-native investors and institutions seeking gold exposure. Marketing leans on cost comparison against ETFs and physical dealers.
- **Geography:** global via exchanges; direct minting constrained by Paxos's US-chartered KYC perimeter. No India, UAE or NRI-specific channel found.
- **Savings plan / recurring purchase:** **Not disclosed.** No systematic investment plan, no recurring buy, no premium schedule.
- **Referral / affiliate / agent network:** **Not disclosed.** No commission-based distribution of any kind was found.
- **Anti-feature worth naming:** PAXG runs a **$2/month inactivity fee** on dormant balances. It actively penalises the buy-and-hold, low-engagement saver, which is exactly Aurumix's target customer.

Design question 8, answered: **PAXG has no savings-plan, recurring-purchase, referral or affiliate mechanism at all, and charges dormant holders a fee.** The brief predicted most protocols would not; PAXG not only does not, it leans the other way. Aurumix's agent-network SIP is genuinely unoccupied ground among the credible issuers. The flip side is that Paxos reached $1.79bn without any distribution machinery, by being the compliance-credible default that exchanges list. Those are two different businesses: Paxos let distribution come to it, Aurumix must go and buy it.

## 11. Recent developments

Reverse chronological. Recency sweep run 28 July 2026 covering ~18 months. The sweep returned a large volume of routine itBit exchange maintenance notices, which are excluded as non-material.

- **~13 July 2026:** Paxos Labs' Amplify Transit reported to have moved ~$30m between Ethereum and Robinhood Chain within two weeks of launch. Stablecoin infrastructure; **no PAXG involvement identified**. **Confidence: Low.**
- **1 July 2026:** Amplify Transit goes live alongside Robinhood Chain mainnet: a "universal adapter" converting USDC, USDG and PYUSD via one API. **Not a gold product.** **Confidence: Low.**
- **~25 June 2026:** **PAXG launches on Solana** using the Token-2022 standard, with Sunrise DeFi as ecosystem partner, LayerZero Stargate for bridging from Ethereum, and Zellic as smart contract auditor ([Crypto Times](https://www.cryptotimes.io/2026/06/25/gold-goes-onchain-paxos-launches-paxg-on-solana/)). **Confidence: Medium.** This is the most material PAXG-specific event in the window.
- **12 December 2025:** **OCC conditionally approves Paxos Trust Company's conversion to a national trust bank; Paxos completes the conversion the same day.** Entity becomes Paxos Trust Company, N.A. NYDFS limited-purpose trust charter surrendered ([OCC](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-125.html), [Paxos](https://www.paxos.com/newsroom/occ-approves-paxos-application-to-convert-to-occ-trust-paxos-to-complete-conversion-imminently-to-become-a-federally-regulated-blockchain-infrastructure-provider)). **Confidence: High.** The single most important development for this profile.
- **11 August 2025:** Paxos files its OCC national trust charter conversion application ([Paxos](https://www.paxos.com/newsroom/paxos-to-pursue-national-trust-charter-with-the-office-of-the-comptroller-of-the-currency)). **Confidence: High.**
- **February 2025:** **KPMG LLP replaces WithumSmith+Brown** as attestor for the monthly PAXG reserve reports ([paxos.com/paxg-transparency](https://www.paxos.com/paxg-transparency)). **Confidence: High.**
- **Date not established:** Paxos Securities Settlement Company registered with the SEC as a clearing agency. Adjacent to PAXG, not part of it. **Confidence: Low.**
- **Date not established:** Paxos Labs closed a $12m strategic round led by Blockchain Capital. **Confidence: Low.**

**Explicitly not found** across the sweep, and each absence is itself a finding: no PAXG depeg, no security incident or exploit, no PAXG-related lawsuit or enforcement action, no change to PAXG custody arrangements, no EU/MiCA, MAS, VARA or ADGM authorisation, and no gold-token competitor launched by Paxos.

## 12. Relevance to Aurumix

**Contradiction to flag loudly, per the brief's instruction.** The task premise (and the bulk of secondary coverage still circulating) treats PAXG as a **NYDFS**-chartered product. It is not, and has not been since **12 December 2025**. PAXG is now issued by **Paxos Trust Company, N.A.** under an **OCC national trust bank charter**. Anything in the Aurumix data room asserting NYDFS supervision of PAXG must be corrected. Paxos's own transparency page still refers to NYDFS approving its auditor, so this error will propagate. Second, note the brief's list of tokenized-gold comparables treats PAXG as Ethereum-only: it has been live on **Solana since June 2026**.

Taking the nine design questions in order of how much PAXG actually moves the needle:

**1. Custody fee: PAXG gives Aurumix its answer, and it is not the one the client expected.** PAXG charges **zero** ongoing custody fee and funds the vault from transaction fees plus cross-subsidy from a far larger stablecoin business. Aurumix has no such adjacent business, so straight imitation is not available. But the *fallback* Paxos drafted is the transferable asset: charge storage **by minting new tokens to the issuer and diluting holders pro rata**. For Paxos this would break a 1:1 ounce peg, which is why it has never been used. For Aurumix, whose price is grams ÷ tokens, dilution is peg-*neutral* by construction: mint to treasury, price per token falls by the fee, the grams-to-tokens identity survives untouched. It needs no cash collection from a $20/month saver, it reaches holders who never log in, and there is now an OCC-supervised, KPMG-attested issuer with the clause on the page. **Recommend adopting the mechanism and copying the disclosure discipline: state the rate, state that it is charged by issuance, and commit to advance notice.**

**2. Dividend funding: PAXG pays nothing, and that is the evidence.** The largest, best-regulated, most liquid gold token in the market at $1.79bn AUM offers **zero yield** and grew anyway. Its gold is unencumbered, sitting allocated at Brink's, doing nothing. This is a powerful negative datapoint for the ICS Dividend: **gold-token AUM does not require a yield to accumulate**, and the issuer with the most regulatory latitude to construct one has declined to. Paxos, an OCC-supervised trust bank, will not lend or lease customer gold to manufacture a return, which speaks to how a serious prudential regulator views encumbering allocated client metal. If Aurumix needs the ICS Dividend, PAXG offers no funding template: it demonstrates the opposite, that the compliant path is to promise no yield at all.

**6. Premium and liquidity: PAXG is the counter-evidence to the 3–8% premium thesis.** $1.79bn AUM against $105.6m daily volume (≈5.9% turnover), a genuine mint/redeem arbitrage channel, and it trades **at par**. The brief already has PGOLD as the illiquid extreme; PAXG is the liquid extreme, and neither sustains a premium. Deep liquidity plus open arbitrage equals NAV. Aurumix's closed redemption is the only thing that could hold a premium, which means the premium is a product of the exit restriction, not of demand. That should be said out loud to the client before it is built into revenue.

**7. Proof of reserve: PAXG sets the retail benchmark.** Monthly **KPMG** attestation under AICPA standards, published as a dated time series, plus a per-address bar lookup showing serial number and physical characteristics, plus a separately-audited smart contract. Aurumix should assume a sophisticated retail buyer or agent has seen this. Match the cadence (monthly) and the credential tier, and keep attestation and contract audit visually and verbally separate. **Do note PAXG's own gap: there is no full public bar list and no on-chain PoR oracle.** Publishing a complete bar list or a live PoR feed would put Aurumix *ahead* of the category leader on one dimension at modest cost.

**5. Redemption: physical redemption can be real and still be retail-irrelevant.** PAXG's 430 PAXG minimum is ~$1.73m per bar. It functions as an arbitrage backstop and a marketing proof point, not a consumer feature. **Aurumix should stop treating "no physical redemption" as a pure weakness.** The honest framing is that PAXG's physical redemption is also unavailable to a $75/month saver; the difference is that Paxos can say "redeemable for physical gold" in a headline. If Aurumix wants that headline without the operational burden, a high-minimum, fee-bearing physical option (deliberately priced out of retail reach) is the industry-standard construction. If it stays with cash-only buyback, it must not claim "you own physical gold" without qualification: Paxos earns that claim with allocated serial numbers and a real, if remote, delivery path.

**3. Token standard: PAXG's plain ERC-20 is a consequence of having no holder state.** Paxos got composability, exchange listings and the resulting liquidity by making the token anonymous and stateless, then retrofitted freeze-and-wipe admin powers to regain compliance control. Aurumix cannot copy this, because ICS tier, dividend entitlement, credit standing and buyback rights are all holder state that an anonymous DEX transfer destroys. The supporting signal for the ERC-3643 lean is Paxos's *newest* deployment: on Solana it chose **Token-2022 with native compliance extensions** rather than the barest standard available. Given the choice today, the most conservative issuer in the category picks the compliance-native token.

**4. Regulatory route: PAXG is not a UAE comparable and should not be used as one.** No VARA, ADGM, DFSA or MiCA authorisation was found. It is a US national trust bank product distributed globally through exchange listings. The transferable insight is structural: Paxos put the **entity** under a prudential fiduciary regulator and kept the **product** deliberately simple, so the token needed no separate securities analysis. Aurumix's hybrid (gold core plus dividend plus credit) is what forces dual regulation. The Paxos precedent argues for **severability**: license the gold core cleanly as an ARVA and place the dividend and credit facility in a separate, separately-regulated entity, rather than seeking one licence that covers a hybrid.

**8. Distribution: the gap is real and it is Aurumix's actual differentiator.** No SIP, no recurring buy, no referral, no affiliate, no agent tier. Plus a **$2/month inactivity fee** that penalises exactly the dormant retail saver Aurumix courts. Nothing in the credible end of this market is competing for the monthly-contribution customer.

**9. Wind-down: partially, and better than any peer, but still not a plan.** Paxos's marketing asserts segregated, bankruptcy-remote accounts and that "your gold bars will always be yours, even in the unlikely case something happens to Paxos", and the OCC trust charter gives that real structural force. But **the PAXG terms contain no issuer-insolvency clause**, only a Clearing Bank default disclaimer, and there is **no published wind-down procedure**: no trustee, no sequence, no distribution mechanic. The brief's observation holds even against the best-documented issuer in the category. **A concrete, ex ante wind-down plan remains unclaimed ground, and Aurumix can take it cheaply.**

## 13. Open items for verification

- [ ] Read the PAXG ERC-20 contract state directly on-chain (`feeRate` / `feeParts` on `0x45804880de22913dafe09f4980848ece6ecbaf78`) to confirm the transfer fee is currently zero, and enumerate the actual admin role names and their current holders. Etherscan blocked automated fetch during this pass.
- [ ] Obtain the **Paxos User Guide / Pricing Supplement** referenced throughout the T&Cs. It contains the physical bar redemption fee, which is nowhere on the public fee page. The $20/$30 figures in circulation are secondary-source only.
- [ ] Confirm the **Solana PAXG mint address** from a Paxos primary source, and confirm whether Solana PAXG is natively issued or bridged. The Paxos newsroom Solana post found is from December 2023 and covers USDP only. Distinguish it from the "Portal"-wrapped PAXG already on Solana.
- [ ] Download one recent **KPMG attestation report PDF** (e.g. June 2026) and record the exact ounces attested, the attestation standard cited, and whether KPMG confirms allocation and serial numbers or only aggregate weight.
- [ ] Verify the claimed **annual Bureau Veritas physical bar audit** against a Bureau Veritas or Paxos primary source. Currently Confidence: Low and possibly a secondary-source invention.
- [ ] Retrieve the **OCC conditional approval order** for Paxos Trust Company, N.A. (the PDF linked from NR 2025-125) and record the charter number, capital and liquidity conditions, and any operating agreement restricting non-fiduciary activity.
- [ ] Confirm whether **Brink's** is still the vault operator post-OCC-conversion, and whether more than one vault operator is used. The Brink's naming sits on a Paxos blog post, not in the terms.
- [ ] Establish the current status of the **creation fee waiver** (the page renders an impossible date, "09/31/26") and whether standard creation tiers have resumed.
- [ ] Confirm whether the **$2/month inactivity fee** applies to on-chain holders or only to Paxos account holders with custodied balances.
- [ ] Check whether Paxos has published any **wind-down or resolution plan** as a condition of the OCC charter (national trust banks may face resolution-planning expectations that are not in the customer terms).

---

# Kinesis Money (KAU)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | KAU (gold, 1 KAU = 1 gram). Sister token KAG (silver, 1 KAG = 1 ozt). Equity-like token KVT | **High** |
| Issuer (marketing) | "Kinesis" / Kinesis Money | **High** |
| Issuer (registry) | **Kinesis Cayman** (Cayman Islands exempted company, C/O Stuarts Corporate Services, 36A Dr Roy's Drive, Grand Cayman KY1-1104). Company number **not disclosed** on any public register we could reach | **Medium** |
| Other entities in the stack | **UAB Kinesis Money Lithuania** (code 305992161, Vilnius); **Kinesis Global Pty Ltd** (ACN 656 201 660, Brisbane); **Kinesis Money Panama S.A.** (155727241); **KMS Labs S.A.** (Panama, 155772003, issues the ERC-20); **Allocated Bullion Exchange / ABX** (ACN 149 681 489, Brisbane); historically **Kinesis AG** (Vaduz, Liechtenstein) | **High** ([Terms of Use](https://kinesis.money/about-us/documents/terms-of-use/)) |
| Domicile | Cayman Islands for the contracting entity; operations spread across Australia, Lithuania, Panama, Liechtenstein | **High** |
| Backing claim | 1 KAU = 1 gram allocated physical gold, held by Kinesis **as bailee**, with legal and beneficial title in the holder | **High** (Terms of Use cl. 5.1.1, 7.1.1) |
| Chains | Kinesis Blockchain Network (a Stellar fork). Secondary **ERC-20 wrapper** on Ethereum issued by KMS Labs S.A. | **High** |
| Contract address | ERC-20 KAU `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52` | **Medium** (Etherscan blocked our fetch; address from KMS Labs/search) |
| Supply | 2.386 million KAU circulating (= 2.386 tonnes of gold) | **Medium** ([CoinGecko](https://www.coingecko.com/en/coins/kinesis-gold), 28 Jul 2026) |
| Market cap / TVL | ~$310.2M market cap; $519.1M FDV | **Medium** (CoinGecko) |
| Regulatory status | Cayman **CIMA VASP: conditional approval only, not granted**. Australia: AUSTRAC DCE100865184-001 + IND100865184-001. Lithuania: FNTT-era registration; Bank of Lithuania lists it only as an **e-money distributor**, not a CASP | **High** for the conditional-approval claim; **Medium** on register confirmation |
| Subscription fee | Mint trade execution **0.45%**; mint deposit from platform $25, external $0 | **High** ([fees page](https://kinesis.money/fees/)) |
| **Ongoing custody fee** | **0% (zero). Explicitly "0% fee" for both KAU and KAG storage** | **High** (fees page) |
| Redemption fee | Physical: **0.45% + $100 + delivery**, case-by-case at Kinesis's discretion | **High** |
| Advertised yield | Holder's Yield = **15% of the Master Fee Pool**. Realised aggregated 12-month yield **2.05%** gold, **0.07%** silver | **High** |
| Named officers | **Thomas Richard Archer Coughlin** (CEO/founder; manager of record of UAB Kinesis Money Lithuania). Other directors **not disclosed** on reachable registers | **Medium** |

---

## 1. What it is

Kinesis is a gold-and-silver monetary system, not a bare custody receipt. KAU is a 1-gram allocated-gold token on the Kinesis Blockchain Network (a fork of Stellar), wrapped around a full retail stack: an in-house exchange, a debit/virtual card, a merchant directory, a multi-asset payroll product, and (this is the part that matters to Aurumix) a **four-way fee-sharing yield system** that pays out to holders, minters, depositors and referrers.

Kinesis has been live since 2018 and is one of the very few gold tokens that actually pays a recurring, disclosed, contractually documented distribution to ordinary token holders. It is the closest live analogue to the ICS Dividend that exists.

## 2. Legal structure

This is the strongest legal-title language of any protocol in this batch, and it is worth reading closely.

The [Terms of Use](https://kinesis.money/resources/Kinesis-Terms-and-Conditions.pdf) (48 pages) state at clause 5.1.1 and again at 7.1.1:

> "Legal and beneficial title in the Allocated Bullion backing the Kinesis Currency will remain with the Kinesis Currency holder until such time as all or part of the corresponding Kinesis Currency is transferred to another Kinesis Address."

And clause 4.1.2:

> "Kinesis will store that Bullion as bailee on behalf of all holders of that particular Kinesis Currency, whereby each holder of that Kinesis Currency has an undivided interest in the total pool of Bullion in proportion to the amount of Kinesis Currency held."

So the native-chain holder owns the gold outright, with Kinesis as **bailee** (not trustee, not debtor). Definition 1.1.4 confirms "Allocated" means "Bullion to which a natural or legal person has legal title, with Kinesis holding it on that person's behalf as bailee". Bailment is the right structure: bailed property is not the bailee's asset and does not fall into its insolvency estate. That is a genuinely strong position, materially stronger than a creditor claim.

**But there is a sharp catch, and it is the most important structural finding in this profile.** The ERC-20 wrapper is a completely different legal animal. [KMS Labs' terms](https://kmslabs.money/kms-labs-tcs/) state:

> "Holders of the Tokens acknowledge and agree that they have no legal, equitable or beneficial right, title or interest in or to the Reserves."

and

> "KMS Labs is entitled to and may retain all net returns, interest, and other income earned on Reserve assets."

**The ERC-20 KAU holder owns no gold and earns no yield.** They hold an unsecured claim against a Panamanian company (KMS Labs S.A., 155772003) redeemable only into native KAU, at KMS Labs' discretion. The moment a KAU leaves the permissioned Kinesis chain for Ethereum, both the property right and the income right evaporate. Marketing does not make this distinction; only the two separate legal documents do.

## 3. Regulatory and compliance posture

| Jurisdiction | Regulator | Status | Confidence |
|---|---|---|---|
| Cayman Islands | CIMA | **Conditional approval only** for a VASP licence, per Kinesis's own Feb 2026 update. Not a granted licence | **High** (issuer's own words) |
| Cayman Islands | CIMA public register | Searched the [CIMA regulated-entities search](https://www.cima.ky/search-entities-cima). **No entity named "Kinesis" returned.** Reference 1877923 could not be resolved to a register entry | **High** (we checked; it is a null result) |
| Australia | AUSTRAC | DCE100865184-001 (digital currency exchange) and IND100865184-001 (remittance) for Kinesis Global Pty Ltd, ACN 656 201 660 | **Medium** (issuer disclosure; AUSTRAC register not directly confirmed by us) |
| Lithuania | FNTT | Historic virtual-currency exchange/wallet registration for UAB Kinesis Money Lithuania | **Medium** |
| Lithuania | Bank of Lithuania | Register entry exists but lists the company **only** under "Persons distributing e-money of an EMI established in the Republic of Lithuania". **No MiCA CASP authorisation found** | **High** ([lb.lt entry](https://www.lb.lt/en/sfi-financial-market-participants/uab-kinesis-money-lithuania)) |
| UK | FCA | **Not authorised.** kinesis.money was voluntarily deactivated for UK users in late 2025; the [UK notice](https://kinesis.money/uk-fca-info/) says "This website and any information materials within are not intended to be accessed by UK-based persons" | **High** |
| UAE / Dubai | VARA / SCA / DMCC | **Not disclosed / not found.** Kinesis lists a Dubai office and a Dubai vault but we found no UAE licence | **High** as a null result |

Three things are material here.

**First, "registered with CIMA" is doing a lot of work in Kinesis's marketing and in third-party write-ups, and it overstates the position.** Kinesis's own [Q4 2025/Q1 2026 update](https://kinesis.money/company-news/q4-2025-q1-2026-quarterly-update/) says only: "Kinesis has received conditional approval for a Virtual Asset Service Provider (VASP) license from the Cayman Islands Monetary Authority (CIMA)." Conditional approval is not a licence. Secondary sources that assert flat "registered VASP, reference 1877923" are repeating a claim we could not verify on CIMA's own register.

**Second, the MiCA gap.** Lithuania's legacy FNTT virtual-currency registrations were superseded by MiCA CASP authorisation across 2025–2026. Kinesis's Lithuanian entity appears on the Bank of Lithuania register only as an e-money *distributor*, which is a different and much narrower permission. We found no CASP authorisation. If Kinesis is serving EU retail on the strength of a lapsed FNTT registration, that is a live exposure.

**Third, note the disclosure inside the legal document itself.** Schedule 6, clause 2.1 of the Terms of Use is remarkably candid:

> "We are seeking, or we plan to seek registrations with various regulatory bodies in countries which we may operate... If we fail to qualify for registrations under any of these authorities, we may be unable to execute on some or all aspects of our business plan as a provider of financial services."

After eight years of operation, the yield schedule still describes the regulatory position in the future tense.

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian / vault operators | **Brink's** and **Loomis** (Zurich named). Kinesis markets vaults in London, New York, Zurich, Dubai, Singapore, Hong Kong, Sydney, Brisbane | **Medium** |
| Allocated? | Yes, and contractually so: bailment with legal title in the holder (cl. 5.1.1) | **High** |
| Bar list | **Not disclosed.** No published serial-number bar list found | **High** as a null result |
| Reserve attestation | **Bureau Veritas / Inspectorate International**, **twice yearly**. Most recent referenced: April 2026. The 17 Oct 2025 audit reported **2,393,328.835 g gold** and **3,729,719.331 ozt silver** | **High** ([audit page](https://kinesis.money/audit/), quarterly update) |
| PoR feed | A live [blockchain explorer](https://explorer.kinesis.money/) shows tokens in existence. This is a **supply** feed, not a reserve feed: it proves how many KAU exist, not how much gold is in the vault | **High** |
| Smart contract audit | **Not disclosed.** No published smart-contract audit found for the ERC-20 wrapper or the chain | **High** as a null result |

Kinesis is one of the better performers in this batch on reserves: a named, credible, independent commodity inspector (Bureau Veritas is the industry standard) on a fixed semi-annual cadence, with absolute gram figures published. Cross-checking the 17 Oct 2025 audit figure of 2,393,328.835 g against 2.386M KAU circulating in July 2026 gives near-exact 1:1 correspondence, which is a good sign.

The two gaps are the **absence of a bar list** and the **absence of a real-time PoR feed**. Between the semi-annual audits there is a six-month window in which the reserve position is unverified. And note the blur risk flagged in the brief: the "live record of all Kinesis currencies in existence" is an explorer, not proof of reserve, and a skimming reader will conflate them.

## 5. Issuance

Two routes. **Mint with cash:** buy KAU through the Kinesis Mint, paying a 0.45% mint execution fee, and Kinesis "will cause an equivalent amount of Bullion to be purchased on your behalf" (cl. 4.1.1). **Exchange of Physical for Digital (EPD):** deliver your own LBMA-conforming bars into a Kinesis vaulting account and mint KAU against them at 1000 KAU per kg (cl. 6.7.1). EPD is case-by-case and Kinesis "may temporarily or permanently disallow deposits for any reason or no reason" (cl. 6.4).

There is no hard supply cap: KAU is minted on demand against deposited or purchased metal, exactly the model Aurumix proposes.

## 6. Redemption

Kinesis **does** offer physical redemption, which distinguishes it from Aurumix and from PGOLD. Clause 8.1.1.1: "At any point in time, you may request for your Kinesis Currency to be redeemed into Allocated Bullion." Redemption is at 1000 KAU per 1 kg gold bar (cl. 8.1.1.10), costing **0.45% + $100 + delivery**.

The qualifications matter, though. Each redemption request "shall be managed on a case by case" basis, Kinesis "may at its ultimate discretion, prescribe reasonable minimum withdrawal quantities", and redemption is satisfied only in bars "of a Prescribed Form" (cl. 8.1.1.3, 8.1.1.5). In practice the minimum practical increment is a 1 kg bar, roughly $130,000 at current prices. So physical redemption is real and legally documented, but it is economically out of reach for the retail saver, which is precisely Aurumix's target customer. **This is the "qualified holders" pattern the brief warns about, expressed through economics rather than eligibility language.**

## 7. Fees and revenue model

| Fee line | Rate | Note |
|---|---|---|
| **Annual storage / custody** | **0%** | Explicitly stated as "0% fee" for both KAU and KAG |
| Mint (subscription) | 0.45% | Plus $25 if funding from platform balance |
| Mint spread | ~0.23% | Buy/sell spread at the Mint |
| Exchange trade execution | 0.22% | Market and limit orders alike |
| Send KAU to another Kinesis account | 0.45% | This is the core yield-funding fee |
| Send KAU to external wallet | 0.45% | |
| Physical redemption | 0.45% + $100 + delivery | |
| Fiat withdrawal | $25–$90 | Currency dependent |
| Card sign-up / monthly / transaction | $0 / $0 / 0% | Cashback 2% in gold up to $2,000/mo |
| Card purchase via third-party rails | 1.99%–5.99% | Banxa and others |

**The zero-storage-fee model is the headline.** Kinesis charges holders nothing to store gold and covers vaulting and insurance out of transaction-fee revenue plus its ABX vaulting relationship. Kinesis says it redistributes **57.5% of every fee taken** to users as yields, implying the residual ~42.5% funds operations including vaulting.

Note what this means structurally: Kinesis's revenue is a **velocity tax, not an assets tax**. It earns on movement, not on stock. A user who buys KAU and never moves it generates essentially zero revenue for Kinesis and costs it real money in vaulting. The entire design is therefore oriented toward making gold circulate: the card, the payroll product, the merchant directory, the Minter's and Depositor's yields that pay only when currency is *used*. This is a coherent and deliberate business model, and it is the opposite of the AUM-fee model most gold tokens run.

## 8. Token architecture

**Native chain.** KAU lives on the Kinesis Blockchain Network, a fork of Stellar. It is **not an ERC-20 and not ERC-3643**. It is a permissioned, KYC-gated ledger controlled by Kinesis, with root and emission accounts referenced throughout the Terms. Every address is tied to a KYC'd account. Kinesis can and does condition yield on that identity link.

**ERC-20 wrapper.** `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52`, issued by KMS Labs S.A. (Panama). Per KMS Labs' terms, holding is limited to "Eligible Users" (not resident in Restricted Jurisdictions, not Sanctioned Persons), and KMS Labs may "freeze, blacklist, or otherwise restrict access to any the Tokens" without advance notice. So even the ERC-20 is permissioned in substance, via freeze/blacklist rather than a transfer-restriction standard.

**The architectural lesson for Aurumix is precise and valuable.** Kinesis faced exactly the problem Aurumix faces (entitlements that break on anonymous transfer) and solved it by **keeping the entitlement on the permissioned ledger and stripping it from the wrapper**. The ERC-20 gets composability; it does not get the gold title or the yield. That is a legitimate design choice, but it means the two tokens are not fungible in any economic sense despite sharing a ticker, and Kinesis's marketing does not make that clear.

Upgradeability and admin keys: **not disclosed**. We found no published smart-contract audit.

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Market cap | ~$310.2M |
| Circulating supply | 2.386M KAU (2.386 tonnes gold) |
| Price | $130.01 (28 Jul 2026) |
| 24h volume | **$219,282** |
| Venue concentration | Kinesis's own exchange **98.5%** (KAU/C1USD $212,814 = 96.93%; KAU/USDT $3,455 = 1.57%). Emirex KAU/USDT $1,398 = 0.64% |

Volume is **0.07% of market cap per day**. That is thin, but it is an order of magnitude better than PGOLD's sub-$20/day against $79–90M, so the brief's premium thesis is not uniformly refuted: Kinesis shows that a captive in-house exchange can generate real, if modest, turnover.

The dominant fact is that **98.5% of all KAU liquidity is on Kinesis's own venue**. There is essentially no independent external market. KAU trades at the gold price because Kinesis operates the market and the mint, not because arbitrageurs enforce it. For Aurumix, which is banking on a 3–8% exchange premium, this is the key observation: **Kinesis has ~$310M of AUM and still could not bootstrap third-party liquidity in eight years.** Venue-controlled pricing is achievable; an independent liquid market producing a reliable premium is a different and much harder problem, and Kinesis has not solved it.

## 10. Distribution

Kinesis is the one protocol in this batch with a **genuine, contractually documented referral network**, and this maps directly onto Aurumix's 3-tier agent model.

- **Recruiter Yield** (Schedule 6, cl. 8): registered recruiters get a unique tracking link and earn a percentage of the execution fees generated by every user they introduce. The worked example in the Terms uses **7.5%**. The entitlement is perpetual and runs on the referred user's *transaction fees*, not on their deposits.
- **Depositor Yield** (cl. 7): rewards large initial deposits, paid on velocity, "forever on the Kinesis coins they bought and then used."
- **Minter's Yield** (cl. 5): rewards creating currency and then circulating it.
- Retail channels: virtual/debit card, merchant directory, multi-asset payroll, Banxa card/bank on-ramps.
- Geography: global ex-UK (voluntarily withdrawn), with offices claimed in Brisbane, London, Lithuania, Dubai, USA and Istanbul.

What Kinesis does **not** have is a recurring monthly savings plan (SIP). There is no auto-debit contribution schedule. Its recurring mechanic is transactional velocity, not periodic accumulation. So Aurumix's SIP remains a genuine differentiator; the agent network does not.

## 11. Recent developments

- **Early/mid 2026 (undated formally):** Founder Thomas Coughlin announced an **"Earn Programme"** proposing to cut **Holder's Yield from 15% to 5%** of the Master Fee Pool while **raising the KVT entitlement from 20% to 30%**, with 5% added to the pool. Announced in a "Live from the Vault" video interview, **not in an amended legal document**. No effective date given. ([Ep. 280](https://www.youtube.com/watch?v=rw1ne5cASIQ))
- **9 February 2026:** Kinesis Virtual Card US Beta launched to 250 community members; public US launch targeted March 2026, full card launch later slipped to early August 2026 on a new Visa requirement.
- **2 February 2026:** [Q4 2025/Q1 2026 quarterly update](https://kinesis.money/company-news/q4-2025-q1-2026-quarterly-update/) published: **CIMA conditional VASP approval** confirmed; UK site deactivation confirmed; Bureau Veritas audit results published.
- **February 2026:** Coughlin states Kinesis is "in negotiations right now to acquire two banks."
- **Late 2025:** kinesis.money **voluntarily deactivated for UK users** as a compliance precaution; working with an FCA-licensed compliance provider on a compliant UK site.
- **17 October 2025:** Bureau Veritas / Inspectorate International audit: 2,393,328.835 g gold, 3,729,719.331 ozt silver, 1:1 backing confirmed.
- **Q4 2025:** Multi-asset payroll solution launched; Kinesis Merchant Directory went live.
- **Throughout 2025–2026:** No regulator warning-list entries, enforcement actions, litigation, security incidents, or suspensions of withdrawals or yield payments found. **Not found**, and we looked.

## 12. Relevance to Aurumix

Kinesis is the most directly instructive protocol in this batch for Aurumix, because it has been running the ICS Dividend concept for eight years and we can therefore check the arithmetic against reality rather than against a pitch deck.

**Q1, Custody fee: Kinesis is the live proof that option three works.** It charges **0% storage** and recovers vaulting cost from transaction fees. This is the cleanest available answer to Aurumix's peg problem: deducting the fee in grams breaks price = grams ÷ tokens, charging cash is friction, and Kinesis simply does neither. Critically, this is only possible because Kinesis monetises **velocity**, not **assets**. Aurumix's product is the opposite: a buy-and-hold SIP with no physical redemption, explicitly designed so gold never moves. **A zero-fee model cannot be copied onto a zero-velocity product.** If Aurumix wants zero custody fees, it must build a genuine transactional layer (the Gold Card is the obvious candidate) or accept that the cost has to come from the credit facility spread.

**Q2, Dividend funding: this is where Kinesis pays for itself as a case study, and the arithmetic is brutal.**

The mechanism, from Schedule 6 of the Terms of Use, is a Master Fee Pool per currency, funded by the 0.45% transfer/mint fees and 0.22% exchange fees, split:

| Recipient | Share of fee pool | Basis |
|---|---|---|
| **KVT holders** | **20%** | Equity-like token, 300,000 cap, sold under an Offering Memorandum |
| **Holder's Yield** | **15%** | Pro-rata daily on KAU held, KYC'd holders |
| Velocity / Depositor Yield | 10% | On initial deposit, paid on velocity |
| Minter's Yield | 5% | Minted-and-then-used |
| Recruiter Yield | 7.5% (worked example) | Of referred users' execution fees |
| **Total redistributed** | **~57.5%** | Kinesis retains ~42.5% |

Now the reality check. Kinesis publishes its actual payouts. **June 2026 Holder's Yield on gold: $26,326.32 (180.14 g)** against a **$310.2M** market cap.

- That is **0.0085% for the month**, or roughly **0.10% annualised**.
- Kinesis's own headline figure is a **2.05% aggregated 12-month yield**, and all-time gold payouts of $12.14M.
- **The two numbers are irreconcilable by a factor of about 20.** The 2.05% is almost certainly a per-holder compounding figure computed on a subset of eligible balances, not a yield on total AUM. A retail buyer reading "2.05%" will not get 2.05% on their holding, and the June payout proves it.

Work backwards. A $26,326 monthly payout at a 15% share implies a **total monthly KAU fee pool of ~$175,500**, or **~$2.1M/year**. At the 0.45% transfer fee, that implies annual fee-generating volume of **~$468M, about 1.5x AUM**. That is a real, functioning economy: Kinesis genuinely turns over its asset base one and a half times a year. It is not a fake.

**And it still only produces a tenth of a percent.**

Now apply this to Aurumix. To pay a **5% distribution on $310M** you would need **$15.5M/year to holders**. At a 15% pool share that requires a **$103M annual fee pool**, which at 0.45% requires **$23 billion of annual transaction volume, roughly 74x AUM**. Even if Aurumix routed 100% of the fee pool to holders rather than 15%, it would still need ~11x AUM in annual velocity.

**This is the single most important number in this profile: a well-run, eight-year-old, genuinely transactional gold platform turning over 1.5x its AUM per year pays its holders about 0.10%.** Aurumix's ICS Dividend promises 15–20% of operating profit with 80% concentrated on the top 10% of holders. Concentrating a small pool on few holders can make *those* headline numbers look respectable, but the total distributable amount is governed by the arithmetic above, and for a buy-and-hold SIP with no redemption and therefore near-zero velocity, the fee pool is close to nil. **Fee-recycling cannot fund a meaningful dividend. Kinesis is the strongest available evidence, and it is evidence against, not for.** If Aurumix wants a real dividend it must come from external yield (gold leasing, as ORO does) or from the credit facility spread, which is genuine external revenue and is Aurumix's most promising untapped source.

**The securities point is even sharper, and Aurumix should study it closely.** Kinesis did not pretend the fee-share was not a security. It **split the instrument in two**: KAU (the commodity, holds gold title, gets a modest 15% yield share) and **KVT (the security: 300,000 capped supply, 20% of all fees, sold to accredited investors under a formal Offering Memorandum through a private placement targeting $200M+)**. The Offering Memorandum states the Company "shall distribute an aggregate sum equal to 20% of the transaction fees" to KVT holders pro rata. That is a revenue-share security, documented and sold as one. **This is a directly transplantable structure for Aurumix: keep AURX as a clean ARVA commodity token under VARA, and if you want a profit-share, issue it as a separate, capped, privately-placed instrument to a small accredited base rather than bolting a dividend onto a mass-retail token.** That single move could dissolve the hybrid-regulation problem in Q4.

**Q3, Token standard.** Kinesis chose a **permissioned proprietary chain**, not ERC-3643. The yield attaches to the **KYC'd account**, not to the token: Schedule 6 cl. 6.2.1.1 requires that "A Holder has passed all identification and onboarding requirements." This validates Aurumix's instinct toward a permissioned base. But note the elegant refinement Kinesis found: **the entitlement follows the account, not the bearer instrument, so it survives even when tokens sit in a linked external wallet.** Kinesis explicitly confirms that KAU "held in external wallets are also applicable for the yield, as long as they are linked to your Kinesis account." Aurumix can get the same result: register ICS standing against the *account*, allow tokens to move, and simply pay entitlements only to linked, KYC'd accounts. That is cheaper than ERC-3643 and preserves optionality. The cost, as Kinesis shows, is that the ERC-20 wrapper becomes a stripped instrument with neither gold title nor yield.

**Q4, Regulatory route.** Kinesis holds **no UAE licence** despite a Dubai office and Dubai vault. Its actual regulatory anchor is an AUSTRAC registration in Australia (an AML registration, not a financial-services licence), a lapsed-looking Lithuanian registration, and **conditional-only** CIMA approval after eight years of trading. That is a thin position for a platform holding $310M of client gold. The lesson is not to imitate it: it is that **the "we're registered with CIMA" formulation is exactly the kind of claim Aurumix will be tempted to make and should not.** Note also that Kinesis withdrew from the UK entirely rather than seek FCA registration, which tells you what a serious retail regulator costs relative to this revenue model.

**Q5, Redemption.** Kinesis offers physical redemption at 0.45% + $100 + delivery, but in 1 kg bars (~$130,000). It is legally real and practically inaccessible to retail. Aurumix's no-redemption stance is more honest than this, and Aurumix should say so plainly rather than treating it purely as a weakness: "cash buyback only" is clearer to a $75/month saver than a theoretical right to a $130,000 bar.

**Q6, Premium and liquidity.** $310M AUM, $219k daily volume, **98.5% of it on Kinesis's own exchange**. Eight years of operation produced almost no independent third-party market. **Evidence against the premium thesis**, though less damning than PGOLD: Kinesis proves a captive venue can generate meaningful turnover, but not that an external market will price your token at a premium.

**Q7, Proof of reserve.** Best-in-batch on attestation (Bureau Veritas, semi-annual, absolute gram figures published, reconciles to supply). Still no bar list and no live PoR feed, and the "live record" explorer is a supply feed that a casual reader will mistake for reserve proof. **Aurumix can beat this cheaply**: publish a bar list and a monthly attestation and you are ahead of the sector leader.

**Q8, Distribution.** The Recruiter Yield (~7.5% of referred users' fees, perpetual, documented in the legal terms) is the closest live analogue to Aurumix's 3-tier agent network, and it is notable that Kinesis pays agents from **transaction fees, not from deposits**. Aurumix's commission comes out of contributions, which is a materially different and more dangerous structure (it is the shape regulators associate with distribution-heavy schemes). Kinesis has no SIP, so Aurumix's monthly savings plan remains genuinely differentiated.

**Q9, Wind-down.** No wind-down plan published. However, Kinesis has something better than a plan: the **bailment structure** means the bullion is legally the holders' property and not Kinesis's asset, so it should not fall into the insolvency estate. That is a structural protection rather than a documented procedure. **Aurumix should copy the bailment language into its own terms.** It costs nothing, it is far stronger than the creditor-claim wording most gold tokens use, and combined with a published wind-down plan it would make Aurumix the best-protected product in the sector on paper.

### Contradictions with the brief

- The brief warns that PGOLD's recycled-fee model is an anti-pattern because "the disclosed sources cannot fund the promise." **Kinesis does not contradict this; it confirms it with better data.** Kinesis's sources *do* honestly fund what it pays, because what it pays is only ~0.10%. The anti-pattern is not fee-recycling per se, it is fee-recycling combined with a headline percentage the fees cannot support. Kinesis is honest about the mechanism and misleading about the headline (2.05% vs 0.10% realised on AUM); PGOLD is misleading about both.
- **New finding not anticipated by the brief:** the yield entitlement, though written into a legal schedule, is **fully revocable at the issuer's sole discretion, including retroactively**. Schedule 6, cl. 3.1: Kinesis may "amend, suspend or terminate any Yield offering to You individually at any time whatsoever and howsoever... for any reason or without reason, including but not limited to your citizenship, residency, domicile, location **and any previously accrued Yields shall no longer be payable with immediate and irrevocable effect**." This is not theoretical: the 2026 Earn Programme proposes cutting Holder's Yield from 15% to 5% while raising the KVT (insider/investor) share from 20% to 30%. **A "documented entitlement" that can be cancelled at will, with accrued amounts clawed back, and that is being reallocated from retail holders to security holders, is a warning about how Aurumix should draft the ICS Dividend.** If Aurumix writes the same discretion into its terms, the dividend is not a value proposition; if it does not, Aurumix has created a fixed liability against a variable revenue stream.

## 13. Open items for verification

- [ ] Obtain the Kinesis Cayman company number and incorporation date from the Cayman Islands General Registry (paid search); the public Terms disclose only a registered-office address.
- [ ] Resolve CIMA reference **1877923** against CIMA directly (written enquiry). Confirm whether it is a VASP licence, a transitional registration, or merely an application reference, and whether the conditional approval has since been granted.
- [ ] Confirm on the AUSTRAC public register that DCE100865184-001 and IND100865184-001 are current for ACN 656 201 660.
- [ ] Confirm whether UAB Kinesis Money Lithuania holds any MiCA CASP authorisation, or whether its FNTT registration lapsed in the 2025–2026 transition. Establish what permission it relies on to serve EU retail today.
- [ ] Determine whether Kinesis operates in the UAE and under what licence, given the Dubai office and Dubai vault but no VARA/SCA/DMCC registration found.
- [ ] Obtain the actual Bureau Veritas audit report PDF (not the summary page) and check scope: is it a full physical count with serial numbers, or a sampling exercise?
- [ ] Establish whether the Earn Programme (Holder's Yield 15%→5%, KVT 20%→30%) has been formally enacted, and whether Schedule 6 of the Terms of Use has been amended accordingly. Get the effective date.
- [ ] Reconcile the advertised "2.05% aggregated 12-month yield" against the $26,326 June payout on $310M. Obtain Kinesis's calculation methodology and the eligible-balance denominator.
- [ ] Verify the ERC-20 contract `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52` on Etherscan: total supply, holder count, verified source, proxy/upgradeability, and freeze/blacklist functions. (Our fetch was blocked by a 403.)
- [ ] Determine how much of the 2.386M KAU sits in the ERC-20 wrapper, i.e. how many holders have unknowingly surrendered gold title and yield rights by bridging.
- [ ] Obtain the full KVT Offering Memorandum terms: how many of the 300,000 KVT were sold, to whom, and whether the 20% entitlement is contractually fixed or amendable like the Holder's Yield.
- [ ] Confirm the exact Recruiter Yield percentage currently paid (Terms use 7.5% in a worked example, not as a stated rate).
- [ ] Establish whether any vaulted metal is leased, encumbered or rehypothecated, given Kinesis's claim of 0% storage fees plus the ABX relationship.

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

---

# AZ Gold Reserve (AZG)

> **Scope warning, read first.** AZG is listed on rwa.xyz under "Commodities" next to PAXG and XAUT, and at ~$66M it screens as a mid-sized tokenized gold product. It is not one. By the issuer's own live API, **62% of AZG's "gold reserve" is gold still in the ground**, not bullion in a vault. AZG is a mining-finance instrument wearing a tokenized-gold label. The single most useful thing in this profile is the arithmetic in §4 and §5, and the fact that rwa.xyz's own classification and metadata are wrong in at least three verifiable respects. This is a **THIN** profile by design: much of what a reader wants does not exist, and the absence is the finding.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | AZG (on-chain name "AZ Gold"). Sister token AZS ("AZ Silver") | High (on-chain) |
| Issuer (marketing) | Arizore / "AZ Reserves". rwa.xyz names **"AZ Reserves Ltd"**, a name that appears in no register and on no Arizore page | Low |
| Issuer (registry) | **Not verified in any register.** Arizore's own terms say "Arizore LTD is a corporation established under the laws of Nevis". No registration number, no incorporation date, no register entry obtainable | **Not disclosed** |
| Domicile | Nevis (St Kitts and Nevis) per issuer's own terms. Nevis has no free public company search, so this is an unverifiable self-assertion, not a confirmed fact | Medium (assertion only) |
| Backing claim | "Tokenised gold reserve... including bullion, **in-ground reserves and tailings**" (rwa.xyz). Live API: **62.0% in-ground, 0% tailings, 38.0% bullion** | High (issuer API) |
| Chains | Ethereum mainnet | High (on-chain) |
| Contract address | AZG `0x45334126815c77be657c7906bf52c0f441a8831c`; AZS `0xee7eddf7793c1399407ba0b858852f64830f37a6` | High (on-chain) |
| Supply | **16,167.34 AZG** (18 decimals) | High (on-chain, 28 Jul 2026) |
| Market cap / TVL | Issuer API: **$64,993,677**. rwa.xyz: $66,171,313 | High (as reported) |
| Holders | **21** | High (Blockscout) |
| Lifetime transfers | **61**, all between 11 Mar 2026 and 10 Jul 2026 | High (Blockscout) |
| On-chain liquidity | **Zero.** No DEX pool, no exchange listing, no quoted market | High (negative search) |
| Regulatory status | **No licence found anywhere.** Not on ASIC, FCA, MAS, SFC, SEC or any register checked. Terms concede tokens "may be characterized as security tokens" | High (negative search) |
| Subscription fee | Minimum investment 100,000 USDT (rwa.xyz). Not stated in any issuer document | Low |
| Ongoing custody fee | 1.00% management fee (rwa.xyz only). Not stated in any issuer document | Low |
| Redemption fee | rwa.xyz claims 0.50%, "instant", 5,000 USDT minimum. **Issuer terms flatly contradict this**: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways" | High (contradiction) |
| Advertised yield | Not to token holders. **Up to 15.00% annual yield in USDT to mining participants**, behind a password gate | High (issuer page) |
| Named officers | **One person only: George Boot, Chief Marketing Officer.** No CEO, no directors, no beneficial owners disclosed anywhere | High |
| Auditor | rwa.xyz names **KPMG**. No KPMG engagement, report or reference exists on any Arizore page or in any public source | Low / unverified |
| Custodian | rwa.xyz names **"Gold Corporation" (LEI 213800HQZYBMURES6D84)**, i.e. the Perth Mint. **No corroboration anywhere.** See §4 | Low / unverified |

---

## 1. What it is

AZG is an ERC-20 token on Ethereum issued under the "AZ Reserve" framework operated by the Arizore brand. rwa.xyz classifies it as tokenized gold, describing it as "a tokenised gold reserve asset designed to provide digital access to verified gold resources, including bullion, in-ground reserves and tailings" ([rwa.xyz/assets/AZG](https://app.rwa.xyz/assets/AZG)).

That description is the tell, and it is accurate. AZG is not a claim on vaulted metal. It is a claim on a **pooled "reserve" whose majority component is unmined mineral resource**. Arizore's own live reserve API returns, as at 28 July 2026:

```
totalGoldReservesOz:  21,050
azgComposition:       inGround 62.00% | tailings 0% | bullion 38.00%
totalAZGTokensInCirculation: 16,167.34
azgCurrentTokenValue: 4,020.06
azgReserveValue:      64,993,676.84
lastUpdatedIso:       null
```
([arizore-reserve-backend.vercel.app/api/azg-reserve](https://arizore-reserve-backend.vercel.app/api/azg-reserve))

Arizore describes AZG on its own site not as gold but as a "**Gold-linked reserve participation instrument**. Supports interaction with the gold reserve framework." That phrasing is doing a lot of work, and it is materially more honest than the rwa.xyz listing.

The business model is mining finance, not savings. Arizore onboards mining projects and bullion providers; miners **pledge in-ground resources or tailings via forward contracts**, valued after "haircuts... from 25% to 55%, depending on the region and resource type", and receive capital. AZG is the instrument that carries that pooled reserve to investors. In Arizore's own words the purpose is "turning verified reserves into usable collateral" and letting miners "access liquidity without surrendering ownership."

**This is the opposite of Aurumix's product.** Aurumix promises that 100% of every dollar buys physical LBMA gold. AZG promises exposure to a reserve that is mostly not yet gold.

---

## 2. Legal structure

**What does a holder actually own? On the published record: nothing that is defined.**

This is not rhetorical. There is **no whitepaper, no offering memorandum, no terms of issue, and no token documentation of any kind** for AZG. The only legal documents Arizore publishes are a website Terms of Service and a Privacy Policy, both dated 27 November 2025, and both are site-usage documents rather than instrument terms.

The Terms of Service contain the entire published legal description of the token, in a section headed "Token Disclosures":

> "Arizore's ecosystem includes asset-backed digital tokens associated with verified reserves of in-ground resources, tailings, or vaulted bullion. **These tokens may be characterized as security tokens under various regulatory frameworks.**"

and, critically:

> "**The existence of a token does not imply rights beyond those expressly documented and contractually provided.**"

Read those together. The token is "associated with" a reserve. The word used is association, not ownership, title, trust or claim. And the rights are whatever a separate, unpublished contract says: "Any tokens issued as part of a pathway reflect audited and verified reserve structures and **are subject to separate agreements**."

So the holder's actual entitlement lives in bilateral agreements that are not public. A reader cannot determine whether AZG is a title claim, a trust beneficiary interest, an unsecured creditor claim, or a purely contractual exposure. **Not disclosed**, and the gap is total.

The issuing entity is named as **Arizore LTD**, "a corporation established under the laws of Nevis", registered address The Provident House, Central Government Road, Charlestown, Nevis, W.I., legal contact `admin@azreserves.com`. Governing law and exclusive jurisdiction are Nevis.

Note the naming inconsistency, which matters for anyone trying to serve process: the terms say **Arizore LTD**; the contact domain is **azreserves.com**; rwa.xyz names the issuer **AZ Reserves Ltd**; the Bocana filings say **Arizore Ltd.**; and the Nevada JV vehicle is **Arizore LLC**. These are at least three different legal persons and the published materials do not say which one issues AZG.

### Registry verification: attempted, and it failed

Per the brief's registry-first rule, this was checked before anything else:

- **Nevis FSRC corporate registry** (`registry.fsrc.kn`): unreachable, connection refused on both HTTP and HTTPS. The Nevis FSRC states that records may be examined only by a person "who has paid the prescribed fee... during normal hours" ([nevisfsrc.com/faqs](https://www.nevisfsrc.com/faqs/)). **There is no free public search of the Nevis register.** This is a deliberate feature of the jurisdiction, not an accident.
- **UK Companies House**: "No results" for both "Arizore" and "AZ Reserves" ([find-and-update.company-information.service.gov.uk](https://find-and-update.company-information.service.gov.uk/)).
- **Nevada Secretary of State** (for Arizore LLC): entity search sits behind an Imperva/Incapsula bot wall; no programmatic verification possible.
- ASIC, ACRA (Singapore), HK Companies Registry, BVI: no entries found for any Arizore or AZ Reserves name.

**Conclusion, stated plainly: the jurisdiction claim cannot be verified against a register.** Unlike ORO (where a Singapore UEN collapsed the Dubai story in one minute) or Comtech (where DAFZA licence 05069 was retrievable), Nevis is a jurisdiction chosen precisely so that this check cannot be performed by a member of the public. **That choice is itself the finding.** An issuer that wanted to be verified would not incorporate where verification is impossible.

The **one** genuinely register-adjacent corroboration is indirect, and it is worth more than everything on Arizore's own website: Arizore Ltd is named in the continuous-disclosure filings of a Canadian reporting issuer. See §11.

---

## 3. Regulatory and compliance posture

**No licence, registration or authorisation was found in any jurisdiction.** Checked and not found:

- ASIC (Australia): no AFSL for Arizore Ltd, AZ Reserves Ltd, Arizore LLC, Black Tie Holdings or Black Tie Digital. This matters because rwa.xyz asserts AZG sits under an "Australian Financial Services License" via ASIC. **No such licence was located on the ASIC registers.** Treat the rwa.xyz regulatory field as unsubstantiated.
- FCA (UK), MAS (Singapore), SFC (Hong Kong), SEC and CFTC (US), BVI FSC: no registrations, no filings, no exemption notices naming AZG, AZS, Arizore or AZ Reserves.
- No prospectus, offering memorandum, or private-placement exemption filing found anywhere.

Equally, and this should be recorded fairly: **no regulator has issued a warning, alert or enforcement action naming any of these entities.** They are absent from ASIC's and the FCA's warning lists. The posture is not "sanctioned"; it is **entirely outside the regulatory perimeter in both directions**.

The compliance position the issuer itself takes is the striking part. Arizore's terms **concede the securities characterisation rather than denying it**: tokens "may be characterized as security tokens under various regulatory frameworks." Most unlicensed issuers argue strenuously that their token is not a security. Arizore accepts it might be, publishes no prospectus, and manages the exposure by restricting distribution instead: the press release states AZG and AZS "are not investment products, are not yield bearing, and are **not intended for retail distribution or public trading**", and portal access is granted "exclusively to individuals and entities that have completed a meet-and-greet call or preliminary verification phase."

That is a coherent, if aggressive, private-placement-by-obscurity strategy. It also means **AZG is not a retail product and is not a competitor to Aurumix in any market sense.**

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | rwa.xyz names "Gold Corporation" (LEI 213800HQZYBMURES6D84). **Arizore names no custodian anywhere.** Terms refer only to generic "Vaulting and bullion partners" | Low / contradicted |
| Vault / city | **Not disclosed** | Not disclosed |
| Allocated? | **Not disclosed.** Terms say bullion providers "relinquish ownership of the bullion" on transfer into the reserve, implying the reserve is pooled and unallocated to holders | Medium |
| Bar list | **Not disclosed.** No bar list, no serial numbers, no assay certificates published | Not disclosed |
| PoR feed | A JSON endpoint returning six numbers. **`lastUpdatedIso` is `null`.** No cryptographic proof, no third-party signature, no on-chain oracle | High |
| Reserve attestation | **None found.** No attestation, no auditor's report, no engagement letter | Not disclosed |
| Smart contract audit | **None found. Contract source is not even verified on-chain** | High |

### The Perth Mint custody claim: unsupported and implausible

rwa.xyz's custodian field carries an LEI. Resolving it against GLEIF gives an unambiguous answer:

> LEI `213800HQZYBMURES6D84` = **GOLD CORPORATION**, trading name **THE PERTH MINT REFINERY**, 310 Hay Street, East Perth, WA 6004, Australia. Category: **RESIDENT_GOVERNMENT_ENTITY**, legal form "STATE GOVERNMENT ENTITY", registered as ABN 98 838 298 431. Status ACTIVE ([GLEIF API](https://api.gleif.org/api/v1/lei-records/213800HQZYBMURES6D84)).

So rwa.xyz is asserting that a Western Australian state-owned mint custodies the reserve behind an unlicensed Nevis token. **No corroboration exists.** The Perth Mint has made no statement, announcement or annual-report disclosure naming Arizore, AZ Reserves, AZG or AZS. Arizore's own website never mentions the Perth Mint, Gold Corporation, or Australia.

This claim should be treated as **false until the issuer produces a custody agreement**, for a reason the wave-1 research already established: the Perth Mint is the entity behind **PMGT**, and it exited tokenization through commercial abandonment. A state-government entity that wound down its own gold token is a deeply improbable custodian for an unregistered Nevis instrument. Note also the Australian thread that makes the claim superficially plausible: Black Tie Digital is Australian-based, and the Arizore launch release is datelined **Sydney**. A plausible explanation is that an Australian connection got laundered into a Perth Mint custody attribution somewhere in the data pipeline.

**Flag for the assembled document: rwa.xyz metadata for AZG is unreliable on issuer name, auditor, custodian and regulatory status.** Given wave 1 already found rwa.xyz naming a non-existent "Gold Issuance Inc." as ORO's issuer, this is now a **pattern**, not a one-off. rwa.xyz should not be treated as a primary source for issuer facts in this landscape.

### Audit versus attestation

Per the brief's standing instruction, separating the two: **neither exists.** rwa.xyz names KPMG as auditor. No KPMG report, engagement or reference appears on any Arizore page or in any public source. Arizore's terms use the word "audited" once ("tokens issued as part of a pathway reflect audited and verified reserve structures") without naming an auditor, a standard, or a date. And the smart contract is **not source-verified on Etherscan or Blockscout**, so there is no contract audit either. The word "audited" here is unbacked in both senses simultaneously.

What replaces verification is **geological reporting**: the Bocana JV release commits to "technical reports and studies compliant with **NI 43-101**". NI 43-101 is a genuine and rigorous Canadian standard, but it certifies *mineral resource estimates*, not vaulted bullion. Using it as the verification backbone for a product sold as "tokenised gold" is a category substitution, and it is the substitution the whole structure rests on.

---

## 5. Issuance

Issuance is by invitation and the mechanics are not published. Access requires "a meet-and-greet call or preliminary verification phase"; Arizore "retains full discretion to refuse, delay, or terminate onboarding for any reason." rwa.xyz states a **100,000 USDT minimum**, which is not confirmed by any issuer document but is consistent with the private-placement posture.

Two supply routes are described in the terms:

1. **Mining projects** pledge in-ground resources or tailings under **forward contracts**, subject to geological assessment, with valuation haircuts of **25–55%** and conservative LTV ratios, and undertake "delivery of refined bullion upon satisfaction of contract terms."
2. **Bullion providers** "sell vaulted bullion into the AZ Reserve through verified transfer pathways. Upon transfer, bullion providers relinquish ownership of the bullion."

### The backing arithmetic, which is the core finding

Using the issuer's own API figures against spot gold of **$4,019.80/oz** on 28 July 2026 ([gold-api.com](https://api.gold-api.com/price/XAU)):

| Measure | Value |
|---|---|
| AZG token value (issuer) | $4,020.06 |
| Spot gold, same day | $4,019.80 |
| **Ratio** | **1.0001, i.e. one token is priced as exactly one ounce of gold** |
| Stated reserve | 21,050 oz across 16,167.34 tokens = 1.3020 oz "backing" per token |
| Implied value of reserve per stated ounce | $64,993,677 ÷ 21,050 = **$3,087.59/oz, i.e. 76.8% of spot** |
| **Bullion component only** | 38.0% × 21,050 = **8,000 oz**, worth **$32.16M** |
| **Actual bullion per token** | **0.4948 oz = $1,989 = 49.5% of the token's own stated price** |

Three things follow, and they are arithmetic rather than opinion.

**First, the token is priced at one ounce of gold while holding roughly half an ounce of gold.** The other half is a discounted claim on ore that has not been mined, by a counterparty that is not named, under a forward contract that is not published.

**Second, the 76.8%-of-spot implied reserve value is the haircut showing through.** The structure is internally consistent (tokens × token value = stated reserve value, to the cent), which tells you the "reserve value" is a *derived* figure, not an independently measured one. Reserve value is computed from the token price, not the other way around. **The published "proof of reserve" is a restatement of the issuer's own valuation assumptions.**

**Third, and most important for a gold-savings comparison: AZG's holder carries mining execution risk, and Aurumix's holder must not.** If a pledged deposit is not mined, or is mined at higher cost, or the miner defaults, the in-ground 62% does not become gold. There is no disclosed remedy, no insurance, no over-collateralisation beyond the haircut, and no statement of where a token holder ranks against the miner or against Arizore's other creditors.

The composition figures are stable across repeated API calls and `lastUpdatedIso` is `null`, meaning the "live" reserve feed carries **no timestamp of its own**. A reserve feed that cannot say when it was last updated is not a proof of reserve.

---

## 6. Redemption

**There is no redemption right, and the two published sources directly contradict each other.**

rwa.xyz states redemption is "**Instant**", with a 5,000 USDT minimum and a 0.50% fee. The issuer's own Terms of Service state the opposite:

> "Arizore does not guarantee liquidity, market access, **convertibility, or redemption pathways**."

Where marketing and legal documents disagree, the brief says show both. Here the "marketing" is a third-party data aggregator and the legal document is the issuer's own binding terms, so the terms govern: **there is no committed redemption at all**, in metal or in cash. There is no minimum increment, no eligibility rule, no settlement window, and no fee schedule, because there is no redemption obligation to attach them to.

Note this is a *harder* position than Aurumix's. Aurumix has no physical redemption but does commit to a cash buyback. AZG commits to neither. The word "redemption" appears exactly once in Arizore's entire published corpus, and it appears in a sentence disclaiming it.

---

## 7. Fees and revenue model

| Fee line | Stated by issuer | Stated by rwa.xyz |
|---|---|---|
| Subscription / mint | Not disclosed | Minimum investment 100,000 USDT |
| Ongoing management / custody | Not disclosed | 1.00% per annum |
| Redemption | Not disclosed (redemption itself disclaimed) | 0.50%, 5,000 USDT minimum |
| Miner-side fee | Implicit in the **25–55% valuation haircut** and the LTV spread | n/a |

**Arizore publishes no fee schedule of any kind.** Every fee figure above comes from rwa.xyz, whose metadata for this asset is demonstrably wrong on other fields, so all three should be treated as unverified.

The economically real revenue line is not a token fee at all. It is the **haircut**: Arizore takes in-ground resource at 45–75% of assessed value and issues against it at spot-linked pricing. That spread, plus the interest on "up to USD $60,000,000 in secured funding loans" to the Bocana JV (§11), is the business. **AZG holders are the funding source for a mining-finance book.**

Per the wave-1 addendum, question 1 is settled and is not re-argued: AZG's ongoing custody fee to holders is **not disclosed**, and if the 1.00% figure is real it is an outlier against a field (PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, PGOLD) that uniformly charges holders nothing.

---

## 8. Token architecture

Verified directly against Ethereum mainnet on 28 July 2026:

| Property | AZG | AZS |
|---|---|---|
| Address | `0x45334126815c77be657c7906bf52c0f441a8831c` | `0xee7eddf7793c1399407ba0b858852f64830f37a6` |
| Name / symbol | AZ Gold / AZG | AZ Silver / AZS |
| Standard | ERC-20, 18 decimals | ERC-20, 18 decimals |
| Total supply | 16,167.341725201783541025 | 130,420.61 |
| Holders | **21** | **5** |
| Lifetime transfers | **61** | **6** |
| Proxy type | **EIP-1967 beacon proxy** (upgradeable) | **EIP-1967 beacon proxy** (upgradeable) |
| Implementation | `0x0c7f3724A477B13a73BF931B3cE2ee7148DFBd44` | not resolved |
| Source verified? | **No** | **No** |
| `owner()` | `0x664e6443786ded0bf91de57143200356d7ef6be0` (EOA, 8 lifetime txs, holds 0 AZG) | `0x0fD369b78E604400d2172615A7bDeeb6D27eBf90` |
| `paused()` | `false` (so the contract **is** pausable) | `false` |
| Contract created | **10 July 2026**, tx `0xdf679627...`, creator `0xF2d5748Df14E3112ae693d4C9778809127D48Ed4` | 2026 |

Four things matter here.

**It is a plain permissionless ERC-20, not ERC-3643.** For an instrument the issuer concedes "may be characterized as security tokens", not intended "for retail distribution or public trading", there is **no on-chain transfer restriction, no whitelist, and no identity gating**. Compliance is enforced entirely off-chain at onboarding. Anyone holding AZG can send it to anyone. This is the exact failure mode the brief's question 3 is about, and AZG is the cautionary case: **the legal restriction and the technical capability do not match.**

**It is upgradeable via a beacon proxy, and the source is unverified.** Both together are severe. The beacon owner can swap the implementation for every token at once, and because the source is not published, a holder cannot read what the current implementation does, let alone what a future one might. There is a `paused()` function, so transfers can be frozen. Admin-key custody is a single EOA with 8 lifetime transactions and no multisig evidence.

**The contract was deployed on 10 July 2026, eighteen days ago**, and it is *not* the contract that was minted in February 2026. Arizore's own February release said "all tokens have been minted, issued, and confirmed on-chain." The current AZG contract post-dates that by five months. So there has been an undisclosed redeployment or migration, and the 61 transfers recorded against this address run from 11 March 2026, i.e. **earlier than the contract's own creation date**, which means the Blockscout history is being served through the beacon/proxy lineage rather than a single clean deployment. Either way, **the on-chain history does not reconcile with the issuer's public statements**, and no migration was ever announced.

**No bridge, no second chain.** Ethereum only.

---

## 9. Liquidity and market

Reported as one data point per the wave-1 instruction; the premium thesis is settled and is not re-argued.

AZG has **~$65–66M of stated AUM and literally zero market**. There is no DEX pool, no CEX listing, no order book, no quoted bid, and no price discovery. The "price" of $4,020.06 is a number the issuer computes and serves from its own API; it is not a market price and no one has traded at it. Lifetime on-chain activity is **61 transfers among 21 holders**, all between 11 March and 10 July 2026, with the largest holder at 6,177 AZG (38.2% of supply) and the top two at **76.9%**.

Against the settled conclusion, AZG is the terminal case of the illiquid end: PGOLD had ~$79–90M AUM on sub-$20 daily volume; ORO had 33% liquidity-to-AUM and traded at a discount; **AZG has a liquidity-to-AUM ratio of exactly zero**. It cannot express a premium or a discount because it has no market at all. Its price is definitionally at "spot" because the issuer sets it to spot.

For Aurumix this is a clean negative data point: **AUM without a market is not evidence of anything.** A $66M headline figure on rwa.xyz sits alongside 21 holders and 61 lifetime transactions.

---

## 10. Distribution

**No savings plan, no recurring purchase, no referral programme, no affiliate network, no agent tier, and no retail channel of any kind.** Distribution is: a meet-and-greet call, manual due diligence, a password-gated portal (`azreservesaccountportal.zite.so`), and a reported 100,000 USDT minimum. The stated target is mining operators, bullion providers, liquidity partners and institutions. The press release explicitly says the tokens are "not intended for retail distribution or public trading."

Secondary access is said to run through the **BTX marketplace** operated by **Black Tie Holdings / Black Tie Digital** (an Australian group with offices in Singapore and Hong Kong, which built Arizore's infrastructure), where "BTX and Black Tie Holdings independently operate the BTX marketplace environment, including onboarding, KYC verification, settlement processes... AZReserves provides reserve infrastructure and related reserve-linked asset framework components only." No licence was found for any Black Tie entity either, and the 61 lifetime transfers indicate the marketplace has produced essentially no secondary trading.

**Direct answer to question 8: AZG speaks to it only by opposite example.** It is the purest institutional-private-placement model in the landscape, and it is worth noting what that buys and costs. It buys a $66M book with 21 holders and no regulatory attention. It costs any possibility of the retail flywheel Aurumix depends on.

---

## 11. Recent developments

Reverse chronological, dated.

- **~14 July 2026.** Privately held **London Gold LLC** moves toward a **US$25M (C$35M) cash-and-stock acquisition of Bocana Resources** ([Northern Miner](https://www.northernminer.com/news/london-gold-offers-25m-for-bolivia-focused-bocana/1003893172/), [Mining.com](https://www.mining.com/london-gold-offers-25m-for-bolivia-focused-bocana/)). No public statement addresses what happens to the Arizore JV or to AZG's in-ground backing if Bocana changes hands. **This is an unresolved and material overhang.**
- **10 July 2026.** Current AZG and AZS contracts deployed to Ethereum mainnet (tx `0xdf679627476db05becd07a301a3aca9e4b6be11e21a7f74dc64fcb509cfcf746`). Undisclosed: no announcement of a redeployment or migration was made.
- **30 June 2026, 08:42 ET.** **CIRO halts trading in BOCA, reason "Pending News"** ([CIRO](https://iiroc.mediaroom.com/2026-06-30-Canadian-Investment-Regulatory-Organization-Trading-Halt-BOCA)). Trading subsequently resumed. The halt precedes the London Gold bid.
- **11 March – 4 June 2026.** The 61 lifetime AZG transfers occur, clustered in short bursts (11 Mar, 8–14 Apr, 20–31 May, 2–4 Jun), consistent with manual allocation to onboarded parties rather than trading.
- **30 March 2026.** Black Tie Digital publishes a case study, "Enabling Real-World Asset Collateralisation: Blacktie x Arizore", confirming Black Tie built "the AZ Reserve ledger layer, token issuance infrastructure (AZG & AZS tokens), and a pooled asset-backed token model" ([blacktie.digital](https://blacktie.digital/enabling-real-world-asset-collateralisation-blacktie-x-arizore/)). No chain, token standard, custodian, auditor or regulator is named in it.
- **22 February 2026 (datelined Sydney).** Arizore announces "$50.1M Live Reserve as AZG and AZS Mint Completes On-Chain": AZG reserve value $40,000,000, AZS $10,134,688, combined $50,134,688. Quoted: **George Boot, Chief Marketing Officer** ([arizore.io](https://arizore.io/reserve-room/written/live-reserve)). The stated AZG reserve has since grown to $64.99M, +62.5%.
- **~January 2026.** Bocana corporate update: the JV "is advancing the development of reserve and ledger architecture", the platform is "in its chain completion and registration phase", preliminary launch "anticipated by the end of January 2026."
- **27 November 2025.** Arizore Terms of Service and Privacy Policy last updated. These remain the only legal documents published.
- **5 November 2025.** Bocana corporate update: "The recently announced joint venture agreement between Bocana and Arizore, Ltd. continues to evolve as plans to create an umbrella joint venture agreement are in the planning stages" ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/11/05/3181268/0/en/bocana-resources-corp-provides-corporate-update.html)).
- **14 October 2025 (agreement dated 23 September 2025).** **Bocana Resources Corp. (TSXV: BOCA; Frankfurt: VC1) announces a 50/50 JV with Arizore Ltd. of Nevis, West Indies, forming Arizore LLC in Nevada.** Arizore Ltd. to provide **up to USD $60,000,000 in secured funding loans**, with no obligation on Bocana to contribute equity capital. Tokenization IP jointly owned. Bocana CEO named as **Tim Turner** ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/10/14/3166721/0/en/Bocana-Resources-Corp-Announces-Joint-Venture-with-Arizore-Ltd-to-Form-Arizore-LLC.html)).

**No regulator anywhere has issued a warning, alert, enforcement action or blacklist entry naming Arizore, AZ Reserves, AZG, AZS, Black Tie Holdings, Black Tie Digital, BT Asset Hub or BTX.** Checked: ASIC, FCA, SEC, CFTC, MAS, SFC, OSC.

### The $60M question

Bocana's market capitalisation at the time of the JV was approximately **$2.17M**. An unregistered Nevis entity with no published accounts, no named directors, no auditor and no licence committed **up to $60,000,000 in secured loans** to a JV with a shell roughly 1/28th that size. Where that money comes from is not disclosed. AZG's entire stated reserve is $65M. **The commitment is of the same order as the token programme it sits beside**, which suggests AZG token subscriptions are the intended funding source for the mining loans. If so, AZG holders are lending to junior mining projects while being marketed a gold reserve.

Live or dormant? **Live but barely moving.** Contracts are deployed and unpaused, the API responds, the site is maintained, and there is genuine third-party corroboration through a TSXV reporting issuer. But there are 21 holders, 61 lifetime transfers, no trading in the last 36 days, and no open roles ("No open positions at this time"). It is an operating private placement, not a functioning market.

---

## 12. Relevance to Aurumix

**Headline: AZG is not a competitor and should not be benchmarked as one. Its value to this engagement is as a boundary case that shows where "gold-backed" stops meaning gold-backed, and as proof that a headline AUM figure on rwa.xyz can be structurally hollow.** If the client sees AZG on a tokenized-gold league table and asks about it, the answer is in §5.

Taking the nine design questions in turn.

**Q1, custody fee: no usable signal.** Arizore publishes no fee schedule. The 1.00% management fee is a third-party claim from a source shown to be wrong on other fields. Settled question, nothing added.

**Q2, dividend funding: this is where AZG earns its place, and it is a warning.** Arizore does not pay yield to AZG holders. It pays yield to the *miners* on the other side, through a password-gated **"Mining Participation Program"** promising **"up to a maximum Annual Yield of 15.00%"**, distributed **quarterly in USDT** after a **45-day deferment**, allocated by a "Contribution Index" scored on reserve contribution, commitment duration and delivery performance, with the largest weight on **Delivery Performance** (volume delivered against contract, and timing against schedule). Under-delivery in a quarter "will result in the forfeiture of that quarter's Annual Yield allocation."

Two lessons, one good and one bad.

The *good* one is the mechanism Aurumix should actually steal: **the yield is conditional on a real external performance obligation, and it is forfeited if the obligation is missed.** This is the structural opposite of the PGOLD/Kinesis anti-pattern. Kinesis paid ~0.10% annualised against advertised figures ~20x higher because the yield was funded by recycled investor fees and promised unconditionally. Arizore's 15% is funded from "reserve profits" generated by bullion deliveries, and it *switches off automatically* when deliveries fail. **A forfeiture condition tied to a verifiable external event is a cheap, powerful and largely absent feature in this landscape, and it directly addresses the client's biggest open problem.** Aurumix's ICS Dividend could adopt exactly this shape: pay from a defined external source, and make the entitlement lapse when that source underperforms, rather than promising a percentage the fee base cannot fund.

The *bad* one is that Arizore does not do the disclosure work that would make the promise credible: no disclosed revenue, no accounts, no attestation, no statement of the profit pool's size, and the whole page sits behind a password. **A conditional yield is only better than an unconditional one if the condition is publicly verifiable.** That is the design note: take the forfeiture mechanic, but publish the numerator.

Also worth carrying to the STREAMEX workstream: this is a **second** structure (after Monetary Metals) where gold-related yield derives from a real external counterparty obligation rather than recycled fees. Unlike Streamex, Arizore's is undocumented, so it is not the precedent the client needs. But it does further weaken the earlier conclusion that no real-yield gold structures exist. It shifts the question from "does real-yield gold exist" to "which real-yield gold structures publish enforceable, ranked terms". Arizore's does not, and **nowhere does Arizore state how a token holder ranks if a miner defaults.**

**Q3, token standard: AZG is the negative case study, and it is a clean one.** The issuer concedes the token "may be characterized as security tokens", declares it "not intended for retail distribution or public trading", and then deploys a **plain, unrestricted, permissionless ERC-20 with unverified source behind an upgradeable beacon proxy**. All compliance is off-chain at onboarding; nothing stops a holder transferring to anyone. This is precisely the mismatch the client is trying to avoid by leaning to an ERC-3643 base. **Use AZG as the concrete example of what "we will handle it at onboarding" looks like once tokens are live: 21 holders, no transfer control, and a legal restriction that the code cannot enforce.** It also demonstrates the upgradeability risk the client should decide on explicitly: a single EOA controls a beacon that can replace the token logic for every holder simultaneously.

**Q4, regulatory route: relevant as the null option.** AZG has no UAE nexus and uses neither VARA nor the ADGM "Accepted Spot Commodity" route. Its answer to hybrid regulation is to have no licence at all and restrict distribution by hand. That is available to a 21-holder private placement and is **categorically unavailable to Aurumix**, which needs mass retail through an agent network. The instructive part is the cost: Arizore's obscurity strategy is why nothing about it can be verified, and why a data aggregator was able to attach a false custodian and a false regulator to it without contradiction. **Opacity is not free; it destroys the issuer's own ability to be believed.** For a savings product selling to Indian and NRI retail on a trust proposition, that trade is fatal.

**Q5, redemption: AZG is worse than Aurumix and usefully so.** Aurumix offers no physical redemption but does commit to cash buyback. Arizore commits to nothing: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways", while a third-party aggregator advertises "instant" redemption at 0.50%. **This is a live example of the gap the brief warns about, with the marketing claim living on rwa.xyz and the disclaimer living in the terms.** The lesson for Aurumix is defensive: when the client publishes buyback terms, publish them where the aggregators scrape them, because third-party listings will otherwise invent terms and the issuer will be held to them.

**Q6, premium and liquidity: one data point, conclusion not re-argued.** ~$65–66M stated AUM, **zero** on-chain liquidity, zero daily volume, 21 holders, 61 lifetime transfers, price set by the issuer at spot because no market exists. It is the extreme illiquid endpoint of the settled finding.

**Q7, proof of reserve: the most transferable warning in the profile.** Arizore publishes a live JSON "reserve" API and calls the result transparency. But it has **no timestamp** (`lastUpdatedIso: null`), no signature, no oracle, no attestation, no bar list, and no named auditor, and its `azgReserveValue` is **arithmetically identical to tokens × the issuer's own token price**, meaning the "proof" is a restatement of the issuer's assumptions rather than an independent measurement. Meanwhile rwa.xyz shows "KPMG" in an auditor field with nothing behind it, and the contract is not even source-verified. **Aurumix's PoR must therefore do three specific things AZG does not: carry a timestamp, be signed or attested by a named third party, and state the metal quantity independently of the token price.** If reserve value is derived from token price, it proves nothing.

**Q8, distribution: speaks to it only by contrast.** No savings plan, no recurring purchase, no referral, no affiliate, no agent tier. Confirms the brief's expectation that almost nothing in this landscape does recurring retail distribution, which remains Aurumix's genuine differentiator.

**Q9, wind-down: nothing, and the omission is now unanimous.** No wind-down plan, no insolvency provision, no statement of what happens to the reserve if Arizore fails, and no disclosure of holder ranking against the miners or against Arizore's creditors. AZG is materially worse than the failed protocols on this point, because a majority of its reserve is in-ground resource that **cannot be distributed to holders at all** in a wind-up: you cannot deliver an unmined ounce. Add the live overhang that Bocana, the JV counterparty, is under a $25M takeover offer with no public statement on the JV's fate. **AZG makes the client's cheap-differentiation argument for them: ten protocols now, none with a wind-down plan.**

### The one structural idea worth stealing

Strip away the opacity and there is a genuine mechanism here: **yield paid from a real external obligation, scored on verifiable delivery performance, and automatically forfeited when delivery fails.** That is the shape of a dividend that survives a securities-classification argument better than "we pay you a share of the fees you paid us", and it is the shape the client's ICS Dividend currently lacks. Arizore fails to make it credible only because it publishes no numbers. Aurumix can take the mechanic and add the disclosure.

### The one thing to make sure the client never does

Blend an asset the holder can verify with one they cannot, and price the blend as if it were all the verifiable one. AZG charges one ounce of gold for half an ounce of gold plus a discounted claim on a mine. Aurumix's entire pitch is "100% of every dollar buys physical LBMA gold", and its peg is grams ÷ tokens. **Any future temptation to admit non-vaulted assets into the reserve, whether gold leases, receivables or forward purchases, breaks that sentence and the peg formula at the same time.** AZG is the fully worked example of where that ends: a $66M headline that is 38% metal, with no market, no attestation and no redemption.

---

## 13. Open items for verification

- [ ] Obtain the **Nevis FSRC company search report for Arizore LTD** via a paid agent (the register is not publicly searchable). Confirm registration number, incorporation date, status and registered agent. Establish whether **AZ Reserves Ltd** exists as a separate legal person or is only a trading name.
- [ ] Determine which entity legally issues AZG: Arizore LTD (Nevis), AZ Reserves Ltd (per rwa.xyz), or Arizore LLC (Nevada). Search the **Nevada SOS register for Arizore LLC** (blocked by bot protection in this pass) for entity number, managers and status.
- [ ] **Put the Perth Mint custody claim directly to Gold Corporation.** rwa.xyz asserts LEI 213800HQZYBMURES6D84 as AZG's custodian with zero corroboration. A one-line confirmation or denial from the Perth Mint settles it and is worth having on the record.
- [ ] **Ask KPMG whether any engagement exists** in relation to Arizore, AZ Reserves, AZG or AZS. rwa.xyz names KPMG as auditor with no supporting document anywhere.
- [ ] Report the rwa.xyz metadata errors (issuer name, auditor, custodian, ASIC/AFSL regulatory status, "instant" redemption) to `team@rwa.xyz`. **Second confirmed instance of fabricated issuer metadata after ORO's "Gold Issuance Inc."** Decide whether rwa.xyz remains a citable source in the assembled document.
- [ ] Pull **Bocana Resources' SEDAR+ filings** (material change reports, MD&A, annual financials) for the Arizore JV agreement itself: security granted over the $60M loan facility, drawdown to date, interest rate, and any auditor commentary. This is the only continuous-disclosure window onto Arizore and it is the highest-value remaining thread.
- [ ] Establish whether the **London Gold LLC acquisition of Bocana** proceeds and what becomes of the Arizore JV, the jointly owned tokenization IP, and the in-ground resource pledged into the AZG reserve.
- [ ] Identify the **62% in-ground component**: which specific deposits, which operators, which NI 43-101 technical reports, and whether the pledged resources are measured, indicated or inferred. Inferred resources backing a spot-priced gold token would be a further material finding.
- [ ] Obtain the **forward contract template and the "separate agreements"** referenced in the terms, to determine what an AZG holder legally owns and where they rank against miners and against Arizore's creditors on default.
- [ ] Obtain the full **Mining Participation Program** page (password-gated): the size of the profit pool, the definition of "reserve profits", the historical distributions actually paid, and whether any quarterly USDT distribution has ever occurred.
- [ ] Verify the AZG **beacon implementation contract** `0x0c7f3724A477B13a73BF931B3cE2ee7148DFBd44` (unverified source): check for mint, burn, pause, blacklist and upgrade authority, and identify who controls the beacon.
- [ ] Explain the **contract deployment date (10 July 2026) against the February 2026 "mint completes on-chain" announcement**. Establish whether an undisclosed migration occurred and what happened to the original token holders.
- [ ] Identify **any officer other than George Boot (CMO)**. No CEO, director or beneficial owner of Arizore is named in any public source.
- [ ] Establish the legal entity and licence status of the **BTX marketplace / BT Asset Hub operator** (Black Tie Holdings / Black Tie Digital, Australia), which performs KYC and settlement for AZG secondary access.

---

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

---

# MG 999 On-Chain Gold Fund (MG999), tokenized by Libeara

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | MG999. Wrapped for DeFi as **thGOLD** by a third party, Theo | **High** |
| Issuer (marketing) | "Libeara", presented as "the tokenisation platform incubated by Standard Chartered's SC Ventures" | **High** |
| Issuer (registry) | **Three separate entities.** Fund manager and issuer of record: **FundBridge Capital Pte. Ltd.** Tokenisation platform: **Libeara (Singapore) Pte. Ltd.**, UEN **202302950G**. Borrower / gold provider: **Mustafa Gold Pte. Ltd.**, UEN **202529232Z**. Libeara is **not** the issuer of MG999 | **High** |
| Domicile | Singapore, all three entities | **High** |
| Backing claim | **The fund holds no gold.** MG999 is a **secured private credit fund** whose assets are loans to gold retailers, secured on the borrower's gold inventory. Token value is intended to "correlate to the spot price of gold" ([Libeara](https://libeara.com/)) | **High** |
| Chains | Ethereum (all live supply), Arbitrum (zero supply), Avalanche C-Chain ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). thGOLD separately on Ethereum, Arbitrum and Stable | **High** |
| Contract address(es) | **Not disclosed publicly.** rwa.xyz gates contract addresses behind a login; Libeara and FundBridge publish none | **High** (that they are undisclosed) |
| Supply | **95,983.65 MG999** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)) | **High** |
| Market cap / TVL | **~$12.44M**, down 7.08% over 30 days. NAV **$130.00/token** | **High** |
| Holders | **2.** Trailing 30-day active addresses: 1. Monthly transfer count: **0** | **High** |
| Regulatory status | **Libeara (Singapore) Pte. Ltd. holds a live MAS Capital Markets Services licence**: Dealing in Capital Markets Products (Securities; Collective Investment Schemes). Verified on the [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution/detail/431842-LIBEARA-SINGAPORE-PTE-LTD). **FundBridge Capital Pte. Ltd.** separately holds CMS (Fund Management; Dealing in CIS) plus Exempt Financial Adviser ([MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/218507-FUNDBRIDGE-CAPITAL-PTE-LTD)). **Mustafa Gold Pte. Ltd. holds no financial licence** | **High** |
| Subscription fee | **0%** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)) | **Medium** |
| Ongoing custody fee | **No gold custody fee, because there is no gold to store.** Management fee **1.00%/yr** | **High** |
| Redemption fee | **0%**, daily subscription/redemption frequency | **Medium** |
| Advertised yield | **~2.0% to 2.3% net** to thGOLD holders ([Fortune, 27 Jan 2026](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)). MG999 itself publishes no target yield | **High** |
| Named officers | **Gwak Yun Seok (Aaron Gwak)**, CEO, Libeara (Singapore) Pte. Ltd. (MAS FID). **Lim Sue Lynn (Lin Shuling)**, CEO, FundBridge Capital (MAS FID). **Mustaq Ahmad**, founder, Mustafa Group | **High** |
| Custodian | **Perpetual (Asia) Limited** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). This is a **fund trustee/custodian, not a bullion vault** | **High** |
| Administrator / Auditor | **Vistra Alternative Investments** / **KPMG** | **Medium** |
| Eligibility | **Accredited, institutional and non-US investors only.** No retail | **High** |

---

## 1. What it is

MG999 is not a gold token. It is a **tokenised private credit fund that lends money to a jeweller**.

This is the single most important sentence in this profile, and it is the reason MG999 sits in this landscape at all. Every other protocol in this set is some version of a custody receipt: you give the issuer cash, the issuer buys metal, the metal sits in a vault, the token points at the metal. MG999 inverts that. Investors put up cash, the cash is lent to **Mustafa Gold**, a Singapore jewellery retailer, and the loan is secured on Mustafa's shop inventory. The token's value is *engineered* to track the gold spot price because the loan is denominated in gold, not because a gram of gold exists anywhere on the fund's balance sheet.

The launch coverage is blunt about this where the marketing is not. "MG 999 does not possess physical bullion. Instead, the tokens are crafted to replicate gold's market performance, offering a synthetic exposure method" ([crypto.news, Dec 2025](https://crypto.news/standard-chartered-backed-libeara-rolls-out-mg-999-tokenized-gold-fund-in-singapore/)). FundBridge's own framing is that the structure "eliminates traditional vaulting and logistics costs while maintaining price exposure."

The mechanism, per Libeara's CEO Aaron Gwak and The Edge Singapore's reporting ([Jan 2026](https://people.duke.edu/~charvey/Media/2026/E_January_29_2026.pdf)):

> "Mustafa pledges its physical gold assets for loans and gold tokens are issued based on the value of the pledged gold. Investors put up cash, which is loaned to Mustafa at a specified interest rate and tenure... During the loan tenure, Mustafa pays interest to investors... monthly pricing refreshes the pricing and the interest rate that Mustafa has to pay, i.e., a variable interest rate. At the end of the tenure, Mustafa pays back the loan in full."

This is a very old trade. Jewellers have borrowed metal rather than cash for centuries, precisely so that their inventory financing cost is not exposed to the gold price. What is new is wrapping the lender side in a token and selling it as gold exposure.

**Scale reality check.** MG999 is **$12.44M of AUM with two holders and zero transfers in the last thirty days**. It was announced at a $15M fund size in December 2025 and has shrunk. It is by some distance the smallest and least-used product in this landscape. Its value to us is entirely structural, not commercial.

## 2. Legal structure

**What a holder owns: units in a collective investment scheme whose asset is a loan receivable.**

Not gold. Not a claim on gold. Not even a claim on the pledged collateral directly. The chain of claim runs:

1. Token holder owns a **tokenised unit** in the MG999 fund (a CIS under the Singapore Securities and Futures Act 2001).
2. The fund's asset is a **secured loan to Mustafa Gold Pte. Ltd.**
3. The loan is secured by a **charge or pledge over Mustafa's gold inventory**.
4. That inventory sits in Mustafa's retail business, being sold to shoppers.

So the holder is **three legal steps away from any metal**, and the metal at the end of the chain is working inventory in a shop on Serangoon Road, not sealed bullion in a vault. Gwak's own description confirms the collateral is live trading stock: interest and pricing reset monthly "due to stock depletion and replenishment."

**What is not disclosed, and it is a lot.** Across Libeara's site, FundBridge's site, Theo's documentation and every news source we could reach, none of the following is published:

- The **exact legal form of the fund vehicle**. Singapore VCC? Cayman company? Sub-fund of an umbrella? **Not disclosed.** rwa.xyz gives the domicile as Singapore and the governing statute as the SFA 2001, but not the vehicle type or a registration number.
- Whether **legal title** to the pledged gold passes to the fund or remains with Mustafa subject to a security interest. **Not disclosed.**
- Whether the collateral is **perfected**, registered, and against what. **Not disclosed.**
- The **default waterfall**: how unit holders rank, who enforces, in what forum. **Not disclosed.**
- Whether the pledged inventory is **insured**, and who is loss payee. **Not disclosed.**
- Any **offering document, PPM, prospectus or factsheet** in the public domain. **Not disclosed.**

That last one is the headline. For a product whose entire selling proposition is institutional pedigree, **there is no public offering document at all**. We checked Libeara's site, its Terms and Conditions, FundBridge's site, Theo's docs subdomain and the launch press releases. What is publicly available is a press release and a data-aggregator row.

**Contrast with the direct-holding protocols.** VNX publishes signed ISRS 4400 reserve reports and terms that define co-ownership down to the 1/1000th of a bar. Whatever VNX's internal inconsistencies, a reader can find out what they own. For MG999 a reader cannot, from public sources, establish the vehicle type, let alone the enforcement mechanics.

## 3. Regulatory and compliance posture

**This is where MG999 genuinely beats the crypto-native field, and it should be credited for it.** Two of the three entities are real MAS licensees, verified on the register.

**Libeara (Singapore) Pte. Ltd.** UEN 202302950G.
- **Capital Markets Services Licensee.** Regulated activity: **Dealing in Capital Markets Products, sub-categories Securities and Collective Investment Schemes.** Status: active. CEO of record: **Gwak Yun Seok (Aaron Gwak)**. Address: 9 Raffles Place #18-21, Republic Plaza.
- Verified directly on the [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution/detail/431842-LIBEARA-SINGAPORE-PTE-LTD), record last updated 22 April 2026. **Confidence: High.**
- Granted **March 2026**, following an in-principle approval in **July 2025** ([Libeara](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/), [Ledger Insights](https://www.ledgerinsights.com/stancharts-libeara-tokenization-platform-lands-singapore-cms-license/)).
- **The MAS record displays no licence number.** MAS's FID does not surface CMS licence numbers in this view. Our check is by name and record ID (431842). We could not obtain a numeric licence ID from any public source: **Not disclosed.**

**FundBridge Capital Pte. Ltd.**
- **Capital Markets Services Licensee** and **Exempt Financial Adviser**. Regulated activities: **Fund Management**; **Dealing in Capital Markets Products (Collective Investment Schemes)**; Arranging of Life Policies. CEO: **Lim Sue Lynn (Lin Shuling)**. Address: 39 Duxton Hill #04-01. Status: active, record updated 16 July 2026 ([MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/218507-FUNDBRIDGE-CAPITAL-PTE-LTD)). **Confidence: High.**

**Mustafa Gold Pte. Ltd.**
- **No financial licence, and it does not need one**: it is a borrower, not a financial intermediary. But its registry record deserves attention. See §4.

### ⚠️ Registry finding: there are two "Libeara" companies and the wrong one is widely cited

ACRA holds **two** distinct Libeara entities:

| Entity | UEN | Incorporated | SSIC | Role |
|---|---|---|---|---|
| **LIBEARA PTE. LTD.** | **202300566N** | **4 January 2023** | 64201, *Bank/financial holding companies* | Holding company. **Not the licensee.** |
| **LIBEARA (SINGAPORE) PTE. LTD.** | **202302950G** | 2023 | not published | **The MAS CMS licensee.** The operating entity named in Libeara's own [Terms and Conditions](https://libeara.com/terms-and-conditions/) |

Almost every secondary source, and several company-data aggregators, resolve "Libeara" to **202300566N**, the holding company, which holds no licence. A reader doing a casual check would either find a holding company with no MAS record and conclude Libeara is unlicensed, or find the licence and attribute it to the wrong entity. **The licence is real. It is just not in the company most people will look up.** Confidence: **High**, both entities confirmed against ACRA-derived records and the licensee confirmed against MAS directly.

Note also that a plain name search for "Libeara" in the MAS FID returns nothing useful: the directory's name filter did not surface the record in our testing, and we reached it only via the direct institution-detail URL. This is a MAS UI limitation, not a licensing gap, but it is worth knowing if anyone repeats the check.

### What the CMS licence does and does not cover

This distinction matters more than the licence itself.

- Libeara's CMS permits **dealing** in securities and CIS. That is a distribution and intermediation permission. It says nothing about the merits of any product Libeara tokenises.
- FundBridge's CMS permits **fund management**. FundBridge is the entity actually responsible for MG999.
- **Neither licence is a product approval.** MG999 has not been authorised or recognised by MAS as a retail CIS. It is a **restricted scheme sold to accredited and institutional investors only**, which is precisely the exemption route that means MAS does not vet the offering document. The absence of a public offering document and the accredited-investor restriction are the same fact viewed from two sides.

**No non-Singapore licence was found for Libeara.** Aaron Gwak has flagged **Hong Kong** as an expansion target ([Blockhead, 13 Mar 2026](https://www.blockhead.co/2026/03/13/libeara-secures-singapore-dealer-licence-clearing-path-to-distribute-tokenised-assets-directly/)), but we found **no SFC registration, no UAE registration and no US registration**. Libeara's marketing has at times been read as claiming multi-jurisdictional standing on the strength of prototype work for the Hong Kong government, Ghana and the Philippines ([Libeara IPA release](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/)). **Government prototype work is not a licence.** On the evidence: **Singapore only.** Confidence: **High** for Singapore, **High** that nothing else was found.

## 4. Custody and proof of reserve

There is no reserve, so there is nothing to attest. This section is therefore about **collateral**, and the disclosure here is the weakest part of the whole structure.

| Item | MG999 |
|---|---|
| Bullion custodian | **None. The fund holds no bullion.** |
| Fund custodian / trustee | **Perpetual (Asia) Limited** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). A corporate trustee, not a vault |
| Fund administrator | **Vistra Alternative Investments** |
| Auditor | **KPMG**. Scope, and whether any audited financial statements exist yet for a fund launched Dec 2025, **not disclosed** |
| Vault / city | **Not applicable.** Collateral is Mustafa's retail inventory, Singapore |
| Allocated? | **No.** The collateral is fungible, actively-traded shop stock that depletes and replenishes monthly |
| Bar list | **None, and none is possible.** Jewellery inventory is not serialised Good Delivery bars |
| PoR feed | **None** |
| Reserve attestation | **None.** Gwak states Mustafa's "inventory undergoes strict auditing processes to ensure it complies with Singapore's AML/CFT laws." That is an **AML control statement, not a collateral valuation attestation**, and the two should not be conflated |
| Smart contract audit | **Not found.** No audit report published by Libeara, FundBridge or Theo |
| Collateral insurance | **Not disclosed** |
| Loan-to-value ratio | **Not disclosed** |

**Separating "audited" from "attested", as the brief requires.** MG999 names **KPMG** as auditor. That is a *fund* auditor, examining financial statements. It is not a reserve attestation, because there is no reserve, and it is not a smart-contract audit, of which we found none published. Anyone reading "KPMG-audited, Standard Chartered-backed" and inferring that a Big Four firm has verified gold in a vault would be wrong on both halves.

**The credit protection that is disclosed: a 20% first-loss buffer.** Theo's own launch article states that investors are protected by "security over gold inventory and a **20% first-loss buffer held by the fund sponsor**" ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you)).

This is a genuinely meaningful credit enhancement and better than anything the crypto-native gold-yield products offer. **But every operative detail is missing.** Who is "the fund sponsor"? Is it FundBridge, Mustafa, or Libeara? Is the buffer funded in **cash or in gold**? Is it **segregated** or a mere contractual undertaking? Is it **topped up** as the loan book grows? Is there any published document evidencing it? On every one of those questions: **Not disclosed.** A 20% first-loss buffer that exists only in a marketing blog post is a promise, not a structure.

### ⚠️ Registry finding: the gold provider is five months old and has $0 paid-up capital

The counterparty on which this entire fund's credit risk rests is **Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025** ([ACRA-derived record](https://recordowl.com/company/mustafa-gold-pte-ltd)).

- **Entity type:** Exempt Private Company Limited by Shares
- **SSIC:** 47731, but classified as **"Other holding companies"**
- **Paid-up capital: $0**
- **Officers: 1. Shareholders: 1.**
- **Employees: 1 at incorporation, 2 by October 2025, 3 by May 2026**
- **No auditor appointed, no financial statements on record**

The fund launched on **11 December 2025**, five months after this entity was incorporated. The Mustafa Group itself is a real, substantial 35-year-old business: Mohamed Mustafa & Samsuddin Co. Pte Ltd (UEN 198900680Z, incorporated 21 February 1989), roughly **$550M of revenue** and **~2 tonnes of gold turnover a year** ([Fortune](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)). But the *borrower of record* is a newly-formed, zero-capital, three-employee entity described in the register as a holding company. Press coverage calls Mustafa Gold "an associate of the Mustafa Group" ([The Edge Singapore](https://people.duke.edu/~charvey/Media/2026/E_January_29_2026.pdf)), which is a weaker word than subsidiary.

**We found no published parent guarantee from the operating Mustafa entity.** The reputational weight of the Mustafa name is doing work in the marketing that the borrower's balance sheet does not do in the registry. Confidence: **High** on the registry facts. Confidence: **High** that no guarantee is publicly documented.

## 5. Issuance

Subscription is **daily**, in cash (USD base currency), with a **0% subscription fee** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). Eligibility is **accredited investors, institutional investors and non-US persons**. There is no retail channel and no minimum published.

Units are then minted on **Libeara's platform** onto Ethereum as ERC-20. Cash raised is deployed into the secured loan. Because the loan reprices monthly against Mustafa's fluctuating inventory, the fund is effectively rolling a variable-rate revolver rather than holding a static asset.

**Minimum subscription: Not disclosed.** **Capacity: capped.** Theo describes thGOLD as "launching with capped early access while the fund scales to full capacity", which is a polite way of saying the loan book cannot yet absorb much money. That is consistent with the $12.44M AUM.

## 6. Redemption

**There is no physical redemption and there never can be.** The fund owns no gold. This is not an omission in the terms; it is a structural impossibility.

Cash redemption is stated as **daily frequency with a 0% redemption fee** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). That figure deserves scepticism, and it is the sharpest unresolved question in this profile.

**Daily liquidity against an illiquid asset is a classic maturity mismatch.** The fund's only asset is a term loan to a jeweller, secured on shop inventory. Loans of that kind cannot be liquidated on a day's notice. A fund offering daily redemption on such a book is either (a) holding a large cash buffer, which drags the yield, (b) relying on the sponsor to warehouse redemptions, or (c) reserving gating powers that are not disclosed. **Which of these applies is Not disclosed.** No lock-up, notice period, gate, side-pocket or suspension provision appears in any public source, and no offering document exists to consult.

With **two holders and zero transfers in thirty days**, this has never been tested.

## 7. Fees and revenue model

| Fee line | MG999 / thGOLD | Source | Confidence |
|---|---|---|---|
| Subscription fee | **0%** | rwa.xyz | Medium |
| Redemption fee | **0%** | rwa.xyz | Medium |
| Management fee | **1.00% per annum** | rwa.xyz | Medium |
| Performance fee | **0%** | rwa.xyz | Medium |
| Ongoing gold custody fee | **None. There is no gold to store.** This is the product's stated selling point: "eliminating traditional storage fees" | Launch coverage | High |
| Libeara platform fee | **Not disclosed** | | High (undisclosed) |
| Theo wrapper fee on thGOLD | **Not disclosed** | | High (undisclosed) |
| Fund admin / trustee / audit costs | **Not disclosed** | | High (undisclosed) |

**Where the revenue comes from.** Unusually, and importantly for Aurumix: **the investor is not the source of revenue. The borrower is.** Mustafa pays loan interest. That interest funds both the yield to holders and (partly) the 1% management fee. This is the cleanest example in the entire landscape of a gold product funded by an **external operating counterparty** rather than by recycling fees back from the people it is paying.

### The arithmetic, and it does not close

The brief requires that any advertised yield be tested against disclosed revenue. Here is the test, and it produces a real problem.

**Disclosed gross rate.** Aaron Gwak, comparing Libeara's cost of gold financing with the Korean market, said: **"we borrow gold at 2.5% [annually]"** while traditional Korean merchants "borrow gold at 1%" per month, i.e. 12% annualised ([Fortune, 27 Jan 2026](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)).

**Disclosed net yield.** Theo's Ari Pingle: thGOLD holders "can expect to receive an annual yield of **2.3%**" net of fees (same source). Theo's own article says "**approximately 2%**" ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you)).

**The gap: 2.5% gross minus 2.3% net = 0.20 percentage points.**

That 0.20pp is supposed to cover:
- FundBridge's **1.00% management fee** (which alone is five times the entire available spread)
- Libeara's platform fee
- Theo's wrapper fee
- Perpetual (Asia) trustee fees
- Vistra administration
- KPMG audit
- Funding cost of the 20% first-loss buffer

**It cannot.** The 1% management fee alone consumes 1.00pp of a 2.50pp gross spread, which mathematically caps the maximum net yield at **1.5%** before any other cost, and lower once platform, wrapper, trustee, admin and audit fees are paid. A 2.3% net yield is arithmetically impossible from a 2.5% gross loan rate.

**Possible reconciliations, none of them confirmed:**
1. The 2.5% figure was Gwak describing a market rate or a different transaction, not MG999's actual coupon to Mustafa.
2. The actual coupon to Mustafa is materially higher than 2.5%: plausibly 4% to 6% to leave room for the stack.
3. Theo's 2.3% is subsidised, promotional, or blends in the delta-neutral gold-futures basis strategy Theo separately describes ([PR Newswire, 27 Jan 2026](https://www.prnewswire.com/news-releases/theo-brings-yield-bearing-gold-onchain-via-regulated-tokenized-fund-structure-302671228.html)), in which case it is **not purely lending yield** and the "secured gold lending" story is incomplete.
4. The 1% management fee is waived during the ramp.

**On the disclosed numbers, the yield promise does not reconcile.** This is the same failure mode the brief documents for Kinesis (advertised yield ~20x actual disclosed revenue) and PGOLD, but arriving by a different route: not recycled fees, but an undisclosed gross rate that makes the arithmetic uncheckable. **Confidence: High** that the published figures are mutually inconsistent. **Confidence: Low** on which reconciliation is correct, because the actual loan coupon is **Not disclosed**.

Note also the honest 2025 backtest figure buried in Theo's launch: "the strategy produced an average annual return of about **8.27% during 2025**". That is a **gold-price-inclusive** total return, not a lending yield, and mixing the two in the same paragraph as "2.3% yield" is exactly the kind of blur the brief warns about.

## 8. Token architecture

- **Standard: ERC-20** on Ethereum ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). Also deployed to Arbitrum (zero supply) and Avalanche C-Chain.
- **Contract addresses: Not disclosed.** rwa.xyz gates them behind a login; neither Libeara, FundBridge nor Theo publishes them. For a product marketed on institutional transparency, **the inability to independently verify the token on-chain is a substantive gap.**
- **Permissioning: almost certainly whitelisted, but not documented.** With **2 holders**, **1 active address in 30 days** and **0 transfers in a month**, and an accredited-investor-only mandate, transfer control must exist. But whether it is enforced via ERC-3643, a transfer-agent allowlist on a plain ERC-20, or purely off-chain at the subscription gate is **Not disclosed**. No token-standard documentation was published.
- **Admin keys, minting authority, upgradeability: Not disclosed.**
- **Smart contract audit: Not found.**

**The wrapper split, and it is the interesting bit.** MG999 the fund unit is locked to accredited investors. **thGOLD**, issued by **Theo** (a separate firm founded by ex-Optiver and ex-IMC traders), is a wrapper that takes MG999 exposure onto **Hyperliquid, Uniswap, Morpho and Pendle** ([The Block](https://www.theblock.co/post/385152/theo-launches-yield-bearing-tokenized-gold-built-work-defi)). Theo's own disclaimer still restricts access to "Accredited Investors and Institutional Investors", so this is not a retail bypass on paper. But the structural pattern is clear: **a permissioned regulated fund unit at the base, a freely-composable DeFi token on top, and a legal relationship between the two that is nowhere documented.** Is a thGOLD holder a beneficial owner of MG999 units, a creditor of Theo, or a derivative counterparty? **Not disclosed.** Theo goes further still with **thUSD**, a "gold-backed stablecoin" backed by thGOLD, targeting $1bn of deposits ([PR Newswire, 17 Apr 2026](https://www.prnewswire.com/news-releases/theos-gold-backed-stablecoin-held-steady-through-global-disruption-now-targets-1b-in-deposits-302745928.html)).

That is **three layers of wrapper on a $12.4M loan to a jeweller**: MG999 unit, thGOLD, thUSD. Each layer adds a counterparty and a fee, and only the bottom one is inside a MAS-licensed perimeter.

## 9. Liquidity and market

Reporting as one data point, per the wave-1 addendum, not re-arguing the settled conclusion.

**MG999 has no market at all.** AUM **$12.44M**, supply **95,983.65** tokens, NAV **$130.00**, **2 holders**, **1 active address** in 30 days, **0 transfers** in a month ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). There is no secondary market, no exchange listing, no on-chain liquidity pool and therefore no price against spot to measure. NAV is struck by the administrator, not discovered by a market. The 30-day figure is **down 7.08%**, tracking the gold price move rather than any flow.

thGOLD is the layer intended to create tradability, and CoinGecko reports **THGOLD is not currently tradeable on any exchange it lists**. So as of today, neither layer trades.

This is the **furthest extreme** of the illiquidity end of the premium spectrum: a product with fewer holders than a family WhatsApp group. It adds nothing to the premium question except a final confirmation that accumulating assets and having a market are unrelated problems.

## 10. Distribution

**No savings plan, no recurring purchase, no referral scheme, no affiliate programme, no agent network.** Confidence: **High**, nothing of the kind appears anywhere.

Distribution is entirely **B2B institutional**:
- **Libeara's CMS dealing licence** is itself the distribution strategy. The March 2026 licence was explicitly framed as letting Libeara move "from a technology platform provider to a regulated financial institution", enabling it to distribute tokenised products directly rather than only build rails for others.
- **Theo** provides the DeFi distribution layer (Hyperliquid, Uniswap, Morpho, Pendle).
- Geography: Singapore-centred, with stated ambitions in **Hong Kong** and **Korea** (the Kyobo Life and Kaia investments in the June 2026 round are explicitly Korea-facing).
- Segment: accredited and institutional only. **Retail is structurally excluded**, which is the mirror image of Aurumix.

The interesting distribution insight is the **borrower** side, not the investor side. Libeara's growth constraint is not raising money; it is **finding creditworthy gold retailers to lend to**. Gwak's comparison of a 2.5% offered rate against Korean jewellers paying 12% annualised is a pitch to *borrowers*, and it explains the Korean investor base in the funding round. **This is a two-sided marketplace disguised as a fund.**

## 11. Recent developments

Dated, reverse chronological.

- **23 June 2026.** Libeara closes a **$14M strategic funding round led by GSR**, with **Openspace Capital, Kyobo Life Insurance Group, AlloyX, Kaia Investment Partners, Simsan Ventures and Monk's Hill Ventures** ([SC Ventures](https://scventures.io/libeara-raises-14m-in-gsr-led-strategic-round-to-scale-infrastructure-for-regulated-digital-assets), [Ledger Insights](https://www.ledgerinsights.com/stanchart-backed-libeara-raises-14m-from-gsr-kyobo-life-others-for-tokenization/)). Notably, **Standard Chartered / SC Ventures is not listed as participating**, and no post-round shareholding is disclosed. Platform cumulative total: **over $1bn of regulated assets tokenised**.
- **~5 May 2026.** SC Ventures makes a **strategic investment into GSR** at a reported ~$1bn valuation ([BanklessTimes](https://www.banklesstimes.com/articles/2026/05/05/standard-chartereds-sc-ventures-backs-crypto-market-maker-gsr/)). GSR then leads Libeara's round the following month. Two SC Ventures portfolio companies investing in each other is worth flagging: it makes the "GSR-led round" a weaker external validation signal than it appears.
- **22 April 2026.** MAS FID record for Libeara (Singapore) Pte. Ltd. last updated; licence active.
- **17 April 2026.** Theo announces **thUSD**, a gold-backed yield-bearing stablecoin backed by thGOLD. $100M Genesis programme sold out in 24 hours; targets $300M TVL by end-April and **$1bn by year-end**. Chains: Arbitrum, Ethereum, Stable, via LayerZero ([PR Newswire](https://www.prnewswire.com/news-releases/theos-gold-backed-stablecoin-held-steady-through-global-disruption-now-targets-1b-in-deposits-302745928.html)). Yield described as coming from **two** sources: physical gold lending **and gold futures basis (delta-neutral)**. The second source is not part of the MG999 lending story.
- **8 April 2026.** GSR-led round first announced ([Blockhead](https://www.blockhead.co/2026/04/08/gsr-leads-funding-round-for-tokenisation-platform-libeara/)); closed 23 June.
- **13 March 2026.** **MAS grants Libeara (Singapore) Pte. Ltd. its full CMS licence** for dealing in CIS and securities ([Blockhead](https://www.blockhead.co/2026/03/13/libeara-secures-singapore-dealer-licence-clearing-path-to-distribute-tokenised-assets-directly/)). Standard Chartered's Margaret Harwood-Jones calls it "proof of the robustness of Libeara's framework." Hong Kong flagged as next target.
- **March 2026.** Gold price volatility event. Theo claims thUSD held its peg while gold ETFs drew down.
- **~27 January 2026.** **Theo launches thGOLD**, wrapping MG999 for DeFi, advertising **~2.0–2.3% net yield** and disclosing the **20% first-loss buffer** ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you), [Fortune](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)).
- **11 December 2025.** **MG999 launch announced.** FundBridge Capital as manager, Libeara as tokenisation platform, **Mustafa Gold as inaugural borrower**. Initial fund size **$15M** ([Caproasia](https://www.caproasia.com/2025/12/11/standard-chartered-bank-sc-ventures-incubated-singapore-tokenisation-platform-libeara-announced-digital-infrastructure-launch-of-tokenized-secured-private-credit-gold-fund-mg-999-on-chain-gold-fu/), [Blockhead, 9 Dec 2025](https://www.blockhead.co/2025/12/09/singapores-fundbridge-launches-tokenized-gold-linked-private-credit-fund/)).
- **3 December 2025.** Libeara and FundBridge launch **ULTRA**, a tokenised US Treasury strategy with **Wellington Management**, for which **Standard Chartered provides custody**. Relevant because it is the one product where SC's role is operational rather than reputational.
- **24 September 2025.** MoU with EQBR Holdings on tokenised RWAs.
- **21 August 2025.** Libeara announces **MAS in-principle approval** (received July 2025) ([Libeara](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/)).
- **7 July 2025.** **Mustafa Gold Pte. Ltd. incorporated**, UEN 202529232Z, $0 paid-up capital.

**No enforcement action, no incident, no security breach and no regulatory criticism** was found against Libeara, FundBridge, Mustafa Gold or Theo in the period. AUM shrinking from a $15M target to $12.44M is the only negative signal, and that is partly gold-price movement.

## 12. Relevance to Aurumix

### The pedigree question, answered directly

**The Standard Chartered link is substantive on the licensing and platform side, and reputational on the product side.** Both halves matter.

**Substantive:**
- Libeara (Singapore) Pte. Ltd. **really does hold a live MAS CMS licence**, verified on the register, with a named CEO in the MAS record. Of the eleven protocols now profiled, this is one of the very few where a name search against a regulator produces a real, current, correctly-scoped authorisation. Comtech's Dubai licences display as expired and cover the wrong activities; ORO is unlicensed everywhere; VNX holds registrations, not licences.
- FundBridge's fund-management CMS is separately real.
- On the **ULTRA** treasury product, Standard Chartered provides actual **custody**. That is a bank doing bank work.

**Reputational:**
- **Standard Chartered is nowhere in the MG999 stack.** It is not the issuer, not the manager, not the custodian, not the trustee, not the auditor and not the borrower's guarantor. It is a shareholder in a portfolio company that provides tokenisation software. The custodian is Perpetual (Asia); the auditor is KPMG; the administrator is Vistra. Every phrase like "Standard Chartered-backed gold fund" in the coverage is describing a **venture equity relationship two removes from the product**.
- SC Ventures did **not** participate in the June 2026 round, and **no shareholding percentage has ever been disclosed**. Whether SC still holds a majority, a minority or a token stake is **Not disclosed**, and after a $14M external round it has necessarily been diluted.
- The GSR-led round is weaker validation than it looks, because SC Ventures had invested in GSR a month earlier.

**Now the payload finding, and it is the answer to the question this profile was commissioned to settle:**

> **The bank-affiliated platform produced a better licence than the crypto-natives. It did not produce better paperwork.**

Libeara has a real MAS licence and no public offering document, no published contract address, no smart-contract audit, no disclosed loan coupon, no disclosed LTV, no disclosed default waterfall, no disclosed insurance and no evidence for its headline 20% first-loss buffer beyond a sentence in a partner's blog post. **VNX Commodities AG, a tiny Liechtenstein operator holding 13 kg of gold, publishes more legally operative detail about what a holder owns than a Standard Chartered-incubated platform does.**

The reason is structural, not cultural, and it is the transferable lesson: **the accredited-investor exemption is what removes the disclosure obligation.** By selling only to accredited and institutional investors, MG999 avoids prospectus registration, and with it the requirement to publish anything. The licence and the opacity are not in tension. **The licence is what buys the opacity.** An institutional wrapper is a disclosure *reduction* technology, not a disclosure *enhancement* technology, and any Aurumix positioning that assumes "regulated therefore transparent" has the causation backwards.

### Against the nine design questions

**Q1, custody fee.** Speaks to it from an unusual angle and is worth taking seriously. MG999 charges **no gold custody fee because it holds no gold**, and it is explicit that removing "vaulting, insurance and storage" cost is the product's raison d'être. It replaces the storage cost with **credit risk on a jeweller**. That is a real trade, honestly stated, and it is a live third option beyond the brief's cash-versus-grams framing: *don't hold the metal at all*. It is **not available to Aurumix**, whose whole promise is that 100% of every dollar buys physical LBMA gold and whose token price is defined as vault grams ÷ tokens. Aurumix has a vault, so it has a storage cost, so it must be recovered in cash. **MG999 confirms the cash-recovery conclusion by showing that the only way to avoid the cost entirely is to abandon physical backing.**

**Q2, dividend funding. This is the section that earns the profile, and it is a genuine partial answer to the client's biggest open problem.**

MG999 is the **first structure in this landscape where the yield is paid by an external commercial counterparty rather than recycled from investor fees**. Mustafa Gold pays interest because it gets working capital cheaper than a bank would lend it. That is real economic value creation, not circular flow. It is exactly the category of thing Aurumix needs for its ICS Dividend.

Three things to take from it and one to be careful about.

*Take:* **The credit-enhancement pattern.** A **20% first-loss buffer held by the sponsor** is a straightforwardly good idea and Aurumix should consider an analogue. If Aurumix ever deploys gold or cash into any yield-generating arrangement, a first-loss tranche funded by the operator, sitting ahead of holders, converts "trust us" into a quantified subordination. It is cheap to describe and powerful in a disclosure document. **Do it better than Libeara did: fund it, segregate it, size it against the book, and publish the evidence.** Their version exists only as a sentence.

*Take:* **The two-sided-marketplace insight.** Libeara's real scarce resource is **creditworthy borrowers**, not investors. Gwak's 2.5%-versus-12% comparison is a borrower pitch. If Aurumix ever wants external yield, the binding constraint will be the same: finding counterparties who will pay for gold liquidity and who are good for it. Aurumix's India and UAE markets are full of jewellers who currently borrow at Muthoot-style rates. **That is a more accessible yield source for a Dubai/India operator than institutional gold leasing, and it is on Aurumix's doorstep.**

*Take:* **The arithmetic discipline.** As shown in §7, the published 2.5% gross against 2.3% net **does not close** once a 1% management fee is applied. This is now the **third** protocol (after Kinesis and PGOLD) where the advertised yield cannot be reconciled with disclosed revenue. The pattern is not a crypto-native failing; a Standard Chartered-incubated, MAS-licensed, KPMG-audited structure does it too. **Aurumix must publish its gross source rate, its full fee stack and its net-to-holder number in the same table, or it will be indistinguishable from these.**

*Careful about:* **This is a partial answer to the Streamex/Monetary Metals question, not a replacement for it.** MG999 is documented *worse* than the Streamex lease the brief flags as the highest-value lead. The brief's live stress test still applies with force here. The AgaBullion default (26 January 2026) showed that when a gold lessee fails, "title remains with the lessor" means litigating abroad. **MG999's collateral is retail jewellery inventory on a shop floor in Singapore**, which is worse collateral than vaulted bullion: it depletes, it is fungible, it is hard to perfect a security interest over, and it is being sold to customers by the borrower in the ordinary course. **How MG999 unit holders rank on a Mustafa default is not disclosed anywhere.** Do not treat this as the documented precedent the client needs. **Chase Streamex.**

**Q3, token standard.** MG999 is a plain **ERC-20** with, presumably, off-chain or allowlist transfer control that is nowhere documented. But the structure is a live demonstration of a pattern directly relevant to Aurumix: **a restricted regulated unit at the base, and a freely-composable wrapper on top issued by a different firm** (Theo's thGOLD, then thUSD). That is architecturally similar to the ERC-3643-base-plus-ERC-20-wrapper design Aurumix is leaning toward. **The warning from MG999 is that the legal relationship between the two layers must be documented, and here it is not.** Nobody can say from public sources whether a thGOLD holder owns fund units, has a claim on Theo, or holds a derivative. Aurumix will face the identical question about ICS standing, dividend entitlement and buyback rights on a wrapped token, and must answer it in writing at design time.

**Q4, regulatory route.** MG999 is Singapore, not UAE, so it does not bear on VARA or the ADGM Accepted Spot Commodity route. **It does bear on the hybrid-regulation problem, and helpfully.** Note what MAS licensed: **Libeara's dealing activity** and **FundBridge's fund management**. It did **not** approve the product. MG999 avoids product-level scrutiny by being a **restricted scheme for accredited investors**. That escape hatch is unavailable to Aurumix, which is by definition mass-retail at $20/month. **The lesson is precisely inverted: the institutional route's cost is that you cannot sell to retail, and Aurumix's entire thesis is retail.** Aurumix cannot borrow MG999's regulatory posture, only its licensing discipline.

**Q5, redemption.** **MG999 offers no physical redemption and cannot**, because there is no gold. It is the one protocol in this set with less physical redemption than Aurumix, and it is sold to institutions on that basis without apology. It is a modest defensive data point: **a Standard Chartered-incubated, MAS-licensed gold product with zero metal and zero physical redemption is being sold to accredited investors today.** Aurumix's no-physical-redemption stance is not an outlier. The difference is that Aurumix actually holds the metal, which makes its position strictly stronger than MG999's, and it should say so. Separately, MG999's claimed **daily redemption against a term loan book** is a maturity mismatch Aurumix should not copy; Aurumix's cash-buyback design should state its settlement window and its funding source honestly.

**Q6, premium.** One data point, no new argument: **$12.44M AUM, 2 holders, 0 transfers in 30 days, no exchange listing, no measurable price against spot.** The extreme illiquid end.

**Q7, proof of reserve.** **No reserve, therefore no attestation, therefore no bar list, therefore no PoR feed.** And the "audited" trap appears in its most complete form: MG999 can truthfully say it is **KPMG-audited** (fund financials) and **Standard Chartered-backed** (venture equity), and a reader will hear "a Big Four firm and a global bank have verified the gold." **There is no gold.** This is the strongest example in the landscape of institutional-sounding assurance language attaching to nothing in the vault, and it is Aurumix's clearest opportunity: **a genuine, frequent, published reserve attestation with a bar list is a differentiator even against bank-affiliated competitors.**

**Q8, distribution.** **None of the mechanisms Aurumix uses.** No SIP, no recurring purchase, no referral, no affiliate, no agent tiers. Purely B2B institutional plus a DeFi wrapper. Confirms the running finding that recurring-contribution retail distribution is genuinely unoccupied territory in tokenised gold.

**Q9, wind-down.** **No wind-down plan published.** Given the structure, the questions are sharper than for a vaulted product: on a FundBridge failure, who administers the loan book? On a Libeara failure, who can mint, burn and transfer the tokens, and does the register survive? On a Mustafa default, who enforces the charge and in what order do unit holders rank? **None of this is documented.** Eleven protocols in, **still no protocol in this landscape has published a wind-down plan**, including the bank-affiliated one with a CMS licence. The cheap-differentiation conclusion holds.

### Contradictions with the brief

**None.** Nothing here contradicts an established finding. Two extensions worth recording:

1. The brief's Kinesis finding ("any protocol advertising a yield: do the arithmetic") now applies to a **licensed, bank-incubated** issuer, not just crypto-natives. The failure to reconcile advertised yield with disclosed revenue is **not correlated with regulatory status**.
2. The brief's rule that **"audited" usually means smart-contract-audited, not reserve-attested** needs a third category after this profile: **fund-audited**. MG999 has a Big Four *fund* auditor, no smart-contract audit and no reserve attestation. Three different things, one word.

## 13. Open items for verification

- [ ] Obtain the MG999 **offering document / PPM / factsheet** from FundBridge Capital directly. Nothing is public. Everything in §2, §6 and §7 that reads "Not disclosed" is likely answered inside it.
- [ ] Establish the **actual interest coupon Mustafa Gold pays**. The published 2.5% gross against 2.3% net cannot support a 1% management fee. Resolve which figure is wrong.
- [ ] Establish the **loan-to-value ratio** applied to pledged jewellery inventory and how the inventory is valued and revalued monthly.
- [ ] Obtain documentary evidence of the **20% first-loss buffer**: who the sponsor is, cash or gold, segregated or contractual, sized against what, and any executed document. Currently sourced only to a Theo blog post.
- [ ] Determine the **legal form of the MG999 vehicle** (Singapore VCC? sub-fund? Cayman?) and its registration number, via ACRA or the MAS VCC register.
- [ ] Determine whether **legal title to the pledged gold passes to the fund** or remains with Mustafa under a security interest, and whether that interest is **registered and perfected**.
- [ ] Obtain the **default waterfall**: enforcement trigger, who enforces, ranking of unit holders, and forum.
- [ ] Establish whether the pledged inventory is **insured** and who is loss payee. Compare against the 110% jeweller's block insurance reportedly in the Streamex/Monetary Metals lease.
- [ ] Obtain a **parent guarantee, keepwell or comfort letter** from Mohamed Mustafa & Samsuddin Co. Pte Ltd (UEN 198900680Z) in favour of the fund. The borrower of record, Mustafa Gold Pte. Ltd. (UEN 202529232Z), has **$0 paid-up capital** and was incorporated five months before launch.
- [ ] Obtain the **MG999 contract addresses** on Ethereum and Avalanche and verify supply, transfer controls and admin roles on-chain. rwa.xyz gates them; the issuer publishes none.
- [ ] Determine the **token standard and permissioning mechanism**: ERC-3643, allowlisted ERC-20, or off-chain-only control. Who holds mint, burn, freeze and upgrade authority.
- [ ] Obtain any **smart-contract audit** of the Libeara token contracts. None found.
- [ ] Establish the **legal relationship between a thGOLD holder and an MG999 unit**: beneficial ownership, creditor claim on Theo, or derivative. And the same question again for **thUSD**, which is a wrapper on a wrapper.
- [ ] Establish **Standard Chartered's / SC Ventures' actual shareholding percentage in Libeara** post the June 2026 $14M round, and whether Libeara is consolidated in Standard Chartered plc's accounts. Never disclosed.
- [ ] Confirm whether MG999 truly offers **daily redemption**, and obtain the gating, notice, lock-up and suspension provisions. Daily liquidity against a term loan book is a maturity mismatch that has never been tested at 2 holders.
- [ ] Obtain the **MAS CMS licence number** for Libeara (Singapore) Pte. Ltd. The FID record confirms the licence but displays no numeric ID.
- [ ] Check whether Libeara has since applied for or obtained any **Hong Kong SFC** licence, flagged as the next target in March 2026.

---

# Streamex (GLDY)

> **Wave-1 lead resolved.** The SEC-filed Monetary Metals agreement is **real**: Exhibit 10.1 to an 8-K filed 8 September 2025, accession **0001641172-25-026853**. But it is **not a gold lease agreement**. It is a commercial *tokenization partnership* agreement between two corporates. The actual leases, and the entire question of how a holder ranks on lessee default, are governed by "Lease Documentation" that Section 3.03 says will be "developed and mutually agreed by the Parties" and which **is not filed with the SEC and is not public**. See §2 and §12. This materially qualifies, but does not fully reverse, our standing conclusion that no properly documented real-yield gold-leasing precedent exists.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | GLDY (token); STEX (Nasdaq parent) | **High** |
| Listed parent | **Streamex Corp.**, Delaware, CIK 0001530766, Nasdaq: STEX. Formerly BioSig Technologies, Inc. (BSGM); renamed 12 Sep 2025 | **High** |
| Operating company | **Streamex Exchange Corporation**, incorporated **British Columbia, Canada, 5 April 2024**; acquired 28 May 2025 | **High** |
| Token issuer | **Streamex Ltd.**, a **Cayman Islands exempted company**, formed **February 2026**; consolidated as a VIE | **High** |
| Servicer | GLDY ServiceCo, LLC (Delaware), wholly owned by parent | **High** |
| Domicile (marketing) | "Streamex", Vancouver / Los Angeles / Winter Park FL | **High** |
| Domicile (token issuer, registry) | Cayman Islands | **High** |
| Backing claim | 1 GLDY = 1 fine troy ounce of gold held by the SPV | **High** |
| Chains | **Base** (primary, ERC-20); Solana via Chainlink CCIP | **High** |
| Contract address | Gated behind login on rwa.xyz; not published by issuer | **Not disclosed** |
| Supply | 3,133.44 GLDY (rwa.xyz, Jul 2026); 3,064.674268 redeemable tokens at 31 Mar 2026 (attestation) | **High** |
| AUM | ~$12.84M (rwa.xyz, Jul 2026); $15.225M gold at cost on balance sheet 31 Mar 2026 | **High** |
| Holders | **19** (rwa.xyz, Jul 2026) | **Medium** |
| Parent-held share of token | **~98.5% held by Streamex Corp. itself at 31 Mar 2026** | **High** |
| Regulatory status | **No licence.** Sold under **Rule 506(c) of Regulation D**, an exemption, not an authorisation | **High** |
| Subscription fee | Not disclosed | **Not disclosed** |
| Ongoing custody fee | Not disclosed as a holder charge; expenses borne inside the SPV | **Low** |
| Redemption fee | Not disclosed | **Not disclosed** |
| Advertised yield | "up to 4%" (Sep 2025 / Nov 2025); **3.50% APY** shown on rwa.xyz Jul 2026; paid **in additional GLDY, not cash** | **High** |
| Minimum investment | $200,000 individual / $300,000 joint / $1,000,000 institution | **Medium** |
| Named officers | Henry (Karl Henry) McPhie, CEO; Morgan Lekstrom, Executive Chairman; Mitch Williams, CIO. Counterparty: Keith Weiner, CEO, Monetary Metals & Co. | **High** |

---

## 1. What it is

GLDY is a **gold-backed security token that pays a yield sourced from real third-party gold leasing**, issued by a Cayman SPV whose ultimate parent is a Nasdaq-listed company. Each token is intended to correspond to one fine troy ounce of physical gold held by the SPV, and yield accrues because the SPV's gold is placed into Monetary Metals' commercial gold-leasing programme rather than sitting idle in a vault.

This is the single most relevant protocol in the landscape to Aurumix's dividend problem, for one reason: it is the only one where the yield-generating arrangement is **described in a document filed with a securities regulator** rather than asserted in marketing. ORO advertises 3–4% from the same counterparty (Monetary Metals) with nothing published at all. Streamex has put paper on the record.

The critical qualification, developed in §2, is that the filed paper covers the *commercial relationship between Streamex and Monetary Metals*. It does not cover the *lease* itself, and it says nothing whatsoever about what a token holder gets if a lessee runs off with the gold.

Note the reverse-merger history: this is a former medical device company (BioSig Technologies, PURE EP cardiac signal platform, SIC code 3845 "Electromedical Apparatus", which EDGAR still shows) that acquired a Vancouver blockchain startup in May 2025 and repurposed the listing. The legacy medical business is still on the books.

## 2. Legal structure

**What a holder actually owns:** "Each GLDY token represents a non-voting digital share of Streamex Ltd., a Cayman Islands special purpose vehicle" ([GlobeNewswire, 10 Nov 2025](https://www.globenewswire.com/news-release/2025/11/10/3184594/22558/en/Streamex-Corp-NASDAQ-STEX-Announces-Launch-of-100-000-000-USD-GLDY-Pre-Sale-A-Gold-Backed-Yield-Generating-Stablecoin-Offering-Institutional-Yield-on-Physical-Gold-Bullion.html)). So: **an equity interest in a Cayman company**, not title to gold and not a trust beneficial interest. Confidence: **High**.

The chain of entities, each verified against the SEC filings themselves rather than secondary sources:

| Layer | Entity | Domicile | Evidence |
|---|---|---|---|
| Listed parent | Streamex Corp. (fka BioSig Technologies, Inc.) | Delaware (orig. Nevada Feb 2009, reincorporated DE Apr 2011) | 10-K FY2025, CIK 0001530766 |
| Intermediate | ExchangeCo | British Columbia ULC | 10-K FY2025 |
| Operating co | Streamex Exchange Corporation | British Columbia, inc. 5 Apr 2024 | 10-K FY2025 |
| **Token issuer** | **Streamex Ltd.** | **Cayman Islands exempted company** | 10-Q Q1 2026, Note 9 |
| Servicer | GLDY ServiceCo, LLC | Delaware | 10-Q Q1 2026 |
| Lease counterparty | Monetary Metals & Co. | Delaware corporation | Ex-10.1 preamble |
| Actual lessee vehicle | "a designated series of a Delaware series limited liability company managed by Monetary Metals" | Delaware | 10-K FY2025 risk factors |

**Contradiction flagged.** The brief and most coverage treat "Streamex" as a single thing. It is not: the marketing name spans a Delaware listed parent, a *Canadian* operating company, and a *Cayman* token issuer. Anyone describing GLDY as a US-issued token is wrong; the issuer is Cayman. Anyone describing Streamex as Canadian is describing the operating subsidiary, not the issuer. This is the fourth domicile mismatch in the batch.

### The filed agreement: what it is and what it is not

**The document is real.** Form 8-K filed 8 September 2025 by BioSig Technologies, Inc., accession **0001641172-25-026853**, Item 1.01 Entry into a Material Definitive Agreement. **Exhibit 10.1** is the complete executed text (~55,000 characters, 20 pages, signed by Henry McPhie and Keith Weiner, PhD). Direct link: [ex10-1.htm](https://www.sec.gov/Archives/edgar/data/1530766/000164117225026853/ex10-1.htm). It is re-listed as Exhibit 10.22 to the FY2025 10-K, confirming it remains in force.

Its actual title is the **"Tokenized Yield Partnership Agreement"** between "BioSig Technologies, Inc. d/b/a StreamEx" and "Monetary Metals & Co." Governing law: Delaware; disputes go to **AAA arbitration seated in Chicago**, single arbitrator, jury trial waived.

**What it governs** is the commercial relationship: exclusivity, volume commitments, fee rebates and revenue share. Read the operative purpose clause:

> "Section 3.02 StreamEx's Supply of Gold. StreamEx shall supply physical gold to the MM SPV. The manner in which StreamEx shall supply the MM SPV **will be documented in the Lease Documentation**."

> "Section 3.03 Lease Documentation. All Products in which StreamEx will participate **will be documented in written agreements, order forms, and other documentation that will be developed and mutually agreed by the Parties** (the 'Lease Documentation'). In the event that the Parties cannot agree on the form of the Lease Documentation within three (3) months of the Effective Date, either party may terminate this Agreement with immediate effect."

That is the whole answer to Priority 1. **The lease agreement is not in the filing.** What is filed is an agreement to enter into lease documentation later. There is also a separate "Precious Metals Lease Program Agreement" referenced in passing in Section 3.01(b) which is likewise **not filed**. Section 14.13 confirms the leases live under a different legal regime: "StreamEx hereby acknowledges that the Lease Documentation and all other document relating directly to MM's Lease origination and account agreements are governed by, and constructed in accordance with, the substantive laws of the **State of New York**."

**What the agreement does not contain, verified by exhaustive text search of the full exhibit:**

- **No security interest.** The words "security interest", "lien", "collateral", "pledge" appear nowhere in an operative sense.
- **No title retention clause.** There is no "title to the gold remains with the lessor" language anywhere. The only uses of "title" in the document are about intellectual property.
- **No risk-of-loss allocation.** The phrase does not appear.
- **No subordination or loss waterfall.** Nothing on ranking of claims.
- **No default provisions relating to lessees.** "Default" appears once, in a boilerplate representation about not breaching other contracts.
- **No fiduciary duty.** Section 14.19 affirmatively disclaims it: "Nothing in this Agreement shall be construed as creating any agency, joint venture, partnership, or other form of joint enterprise, employment, or **fiduciary relationship** between the Parties."

And the liability cap is severe. Section 13.02: StreamEx's aggregate liability "SHALL NOT EXCEED THE TOTAL OF THE AMOUNTS PAID BY MM TO STREAMEX PURSUANT TO THIS AGREEMENT IN THE SIX MONTH PERIOD PRECEDING THE EVENT GIVING RISE TO THE CLAIM **OR $500,000, WHICHEVER IS LESS**." Section 13.01 excludes consequential and indirect damages both ways. Section 12.04 makes indemnification the sole and exclusive remedy.

Finally, Monetary Metals explicitly refuses any securities responsibility for the token (Section 3.04): "StreamEx hereby acknowledges that **MM accepts no responsibility for securities laws and regulations** with respect to such Tokenized Yield Products in any jurisdiction where StreamEx offers such Products."

### How token holders rank on lessee default (Priority 2)

They rank **nowhere in the filed document**, because the filed document is not between them and anyone. The structure interposes at least four layers between a GLDY holder and the gold:

```
GLDY holder
  └─ non-voting share in Streamex Ltd. (Cayman SPV)
       └─ SPV leases gold to a designated series of a Delaware series LLC managed by Monetary Metals
            └─ that series COMMINGLES the gold with other participants' gold
                 └─ and leases it on to the ultimate lessee (a jeweller, mint, refiner)
```

The 10-K describes this as a "back-to-back" structure and, to the company's credit, states the consequences plainly in its own risk factors:

> "The SPV's gold leasing activities are conducted through a 'back-to-back' structure pursuant to agreements with Monetary Metals, whereby the SPV leases gold to a designated series of a Delaware series limited liability company managed by Monetary Metals, which then **may commingle the SPV's gold with gold from other participants** and lease it to the ultimate lessee."

> "The SPV's gold may be commingled with gold from other lessors in Monetary Metals' leasing program, and **other lessors may receive more favorable terms or priority in enforcement scenarios**."

> "**Tokenholders do not benefit from FDIC or SIPC protections, and may face delays, partial recovery, or total loss in the event of SPV insolvency or service provider failure.**"

> "tokenholders are subject to the credit and operational risk of gold lessees under the SPV's gold leasing program. If a lessee fails to return leased gold or make required payments-whether due to financial distress, operational failure, fraud, or other events-**tokenholders may experience reduced recoveries upon redemption**. ... While leases may include independent insurance coverage, collateral, guarantees, or inspections, **these measures vary by lease and may be insufficient to prevent losses**."

A GLDY holder is therefore **an equity holder in a Cayman company that has a contractual claim against a Delaware series LLC that has a claim against a lessee**. It is the most remote position in the entire landscape, and it is subordinate not only to the SPV's own creditors but potentially to other lessors in the same commingled pool.

Confidence: **High** (the issuer's own 10-K says all of this).

## 3. Regulatory and compliance posture

**GLDY holds no licence from any regulator anywhere.** It is sold under an exemption.

| Item | Finding | Confidence |
|---|---|---|
| Securities exemption | **Rule 506(c) of Regulation D**, verified accredited investors and institutions only, including non-US persons | **Medium** |
| Regulator + licence no. | **None.** No VARA, no ADGM, no MAS, no FCA, no CIMA licence identified | **Not disclosed** |
| Cayman issuer regulation | No CIMA registration found for Streamex Ltd. | **Not disclosed** |
| Parent regulation | Nasdaq listing + SEC reporting obligations. This regulates the *parent's shares*, not the token | **High** |
| Form D filing | Not located on EDGAR under CIK 0001530766 for the GLDY offering | **Not disclosed** |

The important nuance for Aurumix: **SEC-reporting is not the same as SEC-approved, and it is not the same as the token being regulated.** Streamex Corp. files 10-Ks because its *equity* is listed on Nasdaq. The GLDY token is a private placement into a Cayman vehicle. The rich disclosure quality we rely on in §2 is a *by-product* of the parent's listing obligations, not of any regulation of the token.

The company anticipates the classification issue candidly in its 10-K: "the tokenization of gold-linked instruments **is expected to be treated as the issuance of securities in most jurisdictions**". It treats GLDY as a security from the outset. This is the opposite of the ORO/Comtech posture.

**Material weakness disclosure.** The 10-K and the 13 July 2026 8-K both report unremediated material weaknesses in internal control over financial reporting: inadequate identification and recording of stock-based compensation, ineffective period-end review, and inadequate segregation of duties. For a business whose entire pitch is custody and verification integrity, this is a real flag.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian | "an LBMA-accredited custodian" (10-K). **Not named in any SEC filing.** | **Not disclosed** |
| Vault / city | Not disclosed | **Not disclosed** |
| Allocated? | **No. Explicitly may be unallocated** | **High** |
| Bar list | **None published** | **Not disclosed** |
| PoR feed | Chainlink Proof of Reserve feed referenced; issuer states in 10-K it has **not yet fully implemented** a live PoR dashboard | **Medium** |
| **Reserve attestation** | **Yes, genuine.** EisnerAmper LLP examination under AICPA attestation standards, as of 31 Mar 2026, announced 1 Jul 2026. Monthly thereafter (intended) | **High** |
| Smart contract audit | Not found | **Not disclosed** |

The 10-K is unusually blunt about the custody weakness:

> "With respect to GLDY, **gold may be held on an unallocated basis, and there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars.** As a result of these operational hurdles, physical redemption for underlying assets may only be available under certain conditions, **We have not yet fully implemented a live proof-of-reserves dashboard or public confirmation of 1:1 gold backing for tokens**, and we are in the process of implementing an independent audit process for bullion holdings on a defined timeline."

**Separating the two things the brief warns about (§4 discipline):**

- **Reserve attestation: YES, and it is a real one.** EisnerAmper LLP performed an *examination* under AICPA attestation standards of management's assertion about gold held for the benefit of GLDY token holders. Result as of 31 March 2026: **3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces**, a surplus of 0.2416423 oz ([GlobeNewswire, 1 Jul 2026](https://www.globenewswire.com/news-release/2026/07/01/3320524/22558/en/streamex-corp-announces-first-independent-reserve-attestation-by-eisneramper-for-gldy.html)). Notably the examination is stated to cover **gold in reserve *and gold on lease*** which is the correct scope for a leasing structure.
- **Smart-contract audit: not found.** No published audit of the Base ERC-20 contract or the CCIP integration.

This is one of the few protocols in the set where the *attestation* exists and the *contract audit* does not, the reverse of the usual pattern. Worth stating plainly: an attestation on ~3,065 ounces where the issuer holds 98.5% of the tokens is an attestation of the issuer's own inventory more than a protection for third-party holders.

**Conflict flag.** EisnerAmper was engaged as the parent's **statutory auditor** on 8 July 2026 (8-K accession 0001493152-26-033083), one week after issuing the GLDY reserve attestation announced 1 July 2026. The same firm now audits the parent and attests the token reserves.

## 5. Issuance

Subscriptions are accepted through app.streamex.com from verified accredited investors under Rule 506(c). A **$100,000,000 pre-sale** was announced 10 November 2025; GLDY formally launched and opened for subscriptions on **25 February 2026** (10-K). Minimums are $200,000 individual, $300,000 joint, $1,000,000 institutional.

Gold is acquired by the parent and placed into Streamex Ltd. The Q1 2026 10-Q records the SPV acquiring approximately **$15.225 million** of gold bullion, carried at cost as a non-current asset because "management does not expect to liquidate the gold within" the year, given "the long-term GLDY Token program and related leasing activities."

**The number that matters most in this profile:**

> "As of March 31, 2026, **the Company held approximately 98.5% of outstanding GLDY Tokens.** Two related party officers of the Company subscribed for an aggregate of approximately **$225** [thousand] of GLDY Tokens during March 2026." (10-Q Q1 2026, Note 9)

So at the end of Q1 2026, third-party ownership of GLDY was roughly **1.5%**, and a material portion of even that was two of the company's own officers. Against rwa.xyz's **19 holders** in July 2026, GLDY should be read as **a corporate treasury position that has been tokenized, with a nascent third-party investor base**, not a distributed product. The "over $100 million in initial institutional interest" cited in Q1 earnings commentary is *interest*, not subscriptions, and should not be reported as AUM.

## 6. Redemption

**Redemption exists, on paper, and is broader than most peers.** Tokens are redeemable on **90 days' prior written notice**, with proceeds payable in **physical gold, stablecoins, select digital assets, or US dollars** ([GlobeNewswire, 10 Nov 2025](https://www.globenewswire.com/news-release/2025/11/10/3184594/22558/en/Streamex-Corp-NASDAQ-STEX-Announces-Launch-of-100-000-000-USD-GLDY-Pre-Sale-A-Gold-Backed-Yield-Generating-Stablecoin-Offering-Institutional-Yield-on-Physical-Gold-Bullion.html)). Confidence: **Medium** (press release, no redemption terms document located).

Three qualifications, all from the issuer's own filings:

1. It is subject to undisclosed "certain limitations", exactly the "qualified holders" pattern the brief warns about.
2. The 10-K states physical redemption "may only be available under certain conditions" because gold may be unallocated with no bar-level linkage.
3. **The 90-day notice is not a courtesy, it is a structural necessity.** The gold is on lease to third parties. It cannot be returned on demand. The notice period is the liquidity mismatch made explicit, and it is the honest design consequence of encumbering the gold to generate yield.

Redemption fee: **Not disclosed.**

## 7. Fees and revenue model

| Fee line | Amount | Who pays | Confidence |
|---|---|---|---|
| Subscription fee | Not disclosed | | **Not disclosed** |
| Ongoing custody/management fee | Not disclosed as a separate holder charge; expenses borne within the SPV, reducing net yield | Holder, indirectly | **Low** |
| Redemption fee | Not disclosed | | **Not disclosed** |
| MM purchase fee to Streamex | Tiered **0.75% down to 0.20%** by quarterly volume, rebated quarterly in cash | Streamex pays MM | **High** |
| MM revenue share to Streamex | **0.35% to 0.50%** sliding by total kilograms leased | MM pays Streamex | **High** |
| Token issuance / platform fees | Stated intent; "**Streamex has not yet generated material revenue from its fee models**" (10-K) | | **High** |

Exhibit 10.1 Section 6.01 sets out the purchase-fee ladder verbatim: 0–$250K at 0.75%, $250K–$1M at 0.55%, $1M–$5M at 0.40%, $5M–$25M at 0.30%, $25M–$50M at 0.25%, and >$50M at 0.20%, with a quarterly cash rebate reconciling fees actually paid to the aggregate-volume tier.

**Yield arithmetic (per brief instruction).** GLDY advertises "up to 4%", currently displaying 3.50% APY. Unlike PGOLD and Kinesis, **this promise is arithmetically fundable**, because it is not recycled from investor fees. The Tokenized Yield Partnership Agreement defines a "Passing Lease" as one that "generates a net yield of at least three percent (3%) per annum after origination fees" (Article I). Streamex is contractually only obliged to accept leases clearing that 3% net hurdle, and it can reject any individual lease "in its absolute and sole discretion" (Section 3.01(b)). So the yield comes from an external commercial counterparty paying to borrow gold, with a contractual floor, not from other holders' subscriptions.

**This is the structural point Aurumix has been looking for, and it is worth stating precisely: the yield is real and externally sourced, and the price of that is that the gold is encumbered, commingled, and unrecoverable on demand.** The 3% floor is a *screening criterion*, not a guarantee to holders; and the yield reaching the holder is net of SPV expenses and Streamex's spread.

**Yield is paid in scrip, not cash.** Monthly "scrip dividends automatically reinvested as new GLDY tokens". The 10-K flags the consequence: "The SPV does not pay cash distributions; yield is paid as additional Tokens (scrip dividends), **which limits liquidity for investors** who may not be able to easily convert their investment to cash."

## 8. Token architecture

| Item | Finding | Confidence |
|---|---|---|
| Standard | **ERC-20 on Base** (rwa.xyz) | **Medium** |
| Cross-chain | **Chainlink CCIP** across Base and Solana mainnets | **Medium** |
| Permissioned? | **Yes, effectively.** Whitelisted digital security; KYC/AML-verified accredited investors only | **Medium** |
| Oracle | Chainlink, appointed official oracle provider 28 Oct 2025 | **Medium** |
| Upgradeability / admin keys | **Not disclosed** | **Not disclosed** |
| Contract address | **Not published by issuer**; gated behind login on rwa.xyz | **Not disclosed** |
| Smart contract audit | Not found | **Not disclosed** |

Note the discrepancy worth recording: rwa.xyz lists GLDY as **Base/ERC-20**, while the 27 May 2026 8-K describes secondary liquidity built with **Orca, an AMM on Solana**. Both are true because of the CCIP deployment across both chains, but any single-chain description of GLDY is incomplete. That an SEC-reporting issuer does not publish its own token's contract address is itself a finding.

Architecturally this is the closest analogue in the set to Aurumix's intended design: a **permissioned, whitelist-gated compliance token** rather than a freely transferable bearer instrument, chosen because the instrument is openly treated as a security.

## 9. Liquidity and market

One paragraph, per the wave-1 instruction not to re-argue the premium thesis. GLDY has approximately **$12.84M** of assets against **19 holders** (rwa.xyz, July 2026), of which roughly 98.5% of tokens were held by the issuer's own parent at 31 March 2026. Streamex announced ~$12M of liquidity infrastructure across three venues and a 24/7 secondary AMM with Orca on Solana (8-K, 27 May 2026), but **no public daily volume figure exists**, and as a whitelisted Reg D security GLDY cannot trade on open venues to non-accredited buyers anyway. There is no observable market price against spot to report. GLDY is therefore **not a data point for or against the premium thesis**: it is a private placement with a nominal secondary venue, and it confirms the wave-1 conclusion from the extreme illiquid end. The parent's own equity (STEX) traded around **$1.25 in early July 2026** against a $3.00 January 2026 offering price, and the board authorised a **10,000,000 share buyback at up to $2.00** on 7 July 2026.

## 10. Distribution

Institutional and accredited only, and this is the sharpest contrast with Aurumix in the entire profile.

- **No savings plan, no SIP, no recurring purchase mechanism.** Minimum ticket is $200,000.
- **No referral, affiliate or agent-commission network** disclosed.
- Channels: direct via app.streamex.com; a distribution partnership with **Siebert** wealth-management and institutional channels (Medium confidence); Nasdaq-listed parent as the credibility vehicle.
- Geography: US accredited investors plus non-US persons under Reg S-style carve-outs.
- **The agreement itself excludes much of Aurumix's target market.** Exhibit 10.1 defines "Restricted Nation" as "**any country located in Africa**, any Sanctioned Territory, plus the following nations: Afghanistan, **Bangladesh**, Belarus, El Salvador, Haiti, Honduras, Iraq, Lebanon, Myanmar (Burma), Nicaragua, **Pakistan**, Russia, **Turkey**, Ukraine, Venezuela, and Yemen." This restricts *ultimate lessee* location, not investor location, but it is a direct read on where Monetary Metals will and will not place gold. India and the UAE are not excluded; Pakistan, Bangladesh and the whole of Africa are.

## 11. Recent developments

- **13 Jul 2026:** 8-K (0001493152-26-033083) reports dismissal of CBIZ CPAs P.C. and engagement of **EisnerAmper LLP** as statutory auditor, effective 8 Jul 2026. No disagreements; unremediated material weaknesses restated.
- **7 Jul 2026:** Board authorises buyback of up to **10,000,000 shares at up to $2.00** over 12 months. Shares traded around $1.25. (Medium confidence, press coverage.)
- **1 Jul 2026:** **First independent reserve attestation** by EisnerAmper announced, as of 31 Mar 2026: 3,064.674268 GLDY outstanding vs 3,064.915910 fine troy oz, surplus 0.2416423 oz. Covers gold in reserve *and on lease*. Monthly attestations intended.
- **27 May 2026:** 8-K (0001493152-26-025606) announces **24/7 secondary liquidity infrastructure with Orca**, an AMM on Solana.
- **26 May 2026:** Kori Handy appointed VP of Product and Design.
- **14 May 2026:** Q1 2026 10-Q filed. Discloses **98.5% of GLDY held by the Company**, ~$15.225M gold at cost, working capital ~$42.6M, net loss ~$46.7M for the quarter.
- **26–27 Mar 2026:** Insider **lock-up agreements** signed by McPhie and Lekstrom for one year, and a press release issued "to clarify and formally refute a series of third-party posts which referenced the purported expiration of certain lock-up agreements" (8-K 0001493152-26-013084). Evidence of a public short/bear thesis circulating.
- **31 Mar 2026:** FY2025 10-K filed. Material weaknesses in internal control reported.
- **25 Feb 2026:** **GLDY officially launched**; app.streamex.com opens for subscriptions.
- **Feb 2026:** **Streamex Ltd.** (Cayman) formed and capitalised; becomes consolidated VIE. GLDY ServiceCo, LLC formed.
- **26–27 Jan 2026:** Underwritten public offering with Needham & Company closes: 11,666,667 shares at $3.00 plus 1,750,000 over-allotment, **$40.25M gross**. Proceeds used to repay ~$38.5M of secured convertible debentures.
- **Nov 2025:** A **former advisor filed a Notice of Civil Claim in the Supreme Court of British Columbia** against the Company, Streamex Exchange Corporation and certain officers and directors, alleging breach of contract, unjust enrichment and civil conspiracy over equity interests pre-acquisition. Company disputes; no liability recorded.
- **10 Nov 2025:** **$100,000,000 GLDY pre-sale** announced under Rule 506(c).
- **28 Oct 2025:** Chainlink appointed official oracle provider; CCIP across Base and Solana.
- **12 Sep 2025:** Name change BioSig Technologies → **Streamex Corp.**; ticker BSGM → **STEX** on Nasdaq Capital Market.
- **8 Sep 2025:** **Tokenized Yield Partnership Agreement with Monetary Metals & Co. executed and filed** as Exhibit 10.1 to 8-K, accession **0001641172-25-026853**.
- **28 May 2025:** Acquisition of **Streamex Exchange Corporation** (British Columbia, inc. 5 Apr 2024) completed via exchangeable-share structure. McPhie becomes CEO.

## 12. Relevance to Aurumix

**This is the most important section in the batch for the client, and the answer is nuanced rather than the clean reversal the wave-1 note hoped for.**

### On the standing conclusion (Q2, dividend funding)

Our prior conclusion was that **no properly documented real-yield gold-leasing precedent exists anywhere**. That should now be **amended, not abandoned**, and split into two claims:

- **"A real, externally-funded gold-leasing yield structure exists and is contractually documented at the commercial level": TRUE.** Exhibit 10.1 to accession 0001641172-25-026853 is a genuine, executed, publicly filed agreement with an explicit **3% per annum net yield floor** defining a qualifying lease, a defined insurance standard, and real economics (0.20–0.75% purchase-fee ladder, 0.35–0.50% revenue share). Aurumix now has a **precedent it can point to and copy** for structuring a leasing relationship. That is genuinely new and it is more than ORO ever published.
- **"A properly documented structure protecting *token holders* against lessee default exists": STILL FALSE.** The filed agreement contains no security interest, no title-retention clause, no risk-of-loss allocation, no subordination, no loss waterfall, and no default ranking. The lease documents that would contain such terms are expressly deferred to a later, unfiled, New-York-law "Lease Documentation" set. **The gap our client's dividend design needs to fill is still open.**

So: the *yield-generation* precedent exists. The *holder-protection* precedent does not. Streamex has documented the revenue side and left the risk side to private paper.

### On the insurance (Priority 2)

The 110% jeweller's block insurance is **verified verbatim** in Schedule 1 of the filed exhibit, and it is more sophisticated than reported. There are **two layers**:

1. **Primary:** the *lessee* must maintain a jeweller's block policy at its own expense covering "no less than one hundred ten percent (110%) of the U.S. dollar value of the Total Lease Amount", adjusted as gold prices or ounces rise, from an insurer rated **A.M. Best A- or better**.
2. **Supplemental (this is the part worth stealing):** **MM itself** must obtain, at its own expense, a **DIC/DIL (Difference in Conditions / Difference in Limits) policy through a Lloyd's of London broker**, which "shall provide coverage in the event that the primary lessee insurance fails or refuses to pay a claim, or is otherwise insufficient to cover a loss", and which "must also provide coverage for both **mysterious disappearance and 'bad acts' by the lessee's management and owners, including but not limited to fraud, misappropriation, or other willful misconduct**", also at 110%.

That second layer is a genuinely good piece of design and directly addresses the AgaBullion failure mode: it is insurance against the *lessee's own fraud* and against the primary insurer refusing to pay.

**But the beneficiary answer is the one the client needs, and it is unfavourable.** Both layers say: "**MM shall require the insured to name MM as a loss payee and additional insured wherever possible.**" Three problems:

- The loss payee is **Monetary Metals**, not Streamex, not Streamex Ltd., and emphatically **not the token holder**.
- "**Wherever possible**" is not a covenant. It is best-efforts, and it means there will be leases where MM is *not* named.
- There is **no obligation anywhere** to name StreamEx, the SPV, or holders as loss payee, additional insured, or third-party beneficiary.

**Answering the question as posed: a token holder is not a beneficiary. A token holder is someone with an equity interest in a Cayman company, which has a claim against a Delaware series LLC, which has a claim against a lessee and possibly against an insurer.** Insurance proceeds land at Monetary Metals and then have to travel back down a chain of contracts, through a commingled pool in which "other lessors may receive more favorable terms or priority in enforcement scenarios", before any of it reaches a holder. Streamex's paper is **better documented** than the AgaBullion situation, but it does not change the fundamental position: recovery is a litigation and contract-chain problem, not an entitlement.

### On whether GLDY holders are exposed to the lease at all (Priority 3)

**Yes, fully and by design.** This is not a separate business line. Streamex Ltd. exists to hold gold *and place it into the leasing programme*; the 10-Q says the gold is classified as non-current precisely because it supports "the long-term GLDY Token program and **related leasing activities**". The yield is the product. Holders carry the lessee credit risk directly, as the 10-K risk factors state. There is no ring-fenced unleased tranche.

### Direct answers to the nine design questions

**Q1 Custody fee.** No disclosed holder-facing custody fee. Costs are absorbed inside the SPV and paid out of lease income before yield reaches holders. This is the third option from the brief (charge holders nothing, recover cost elsewhere) executed cleanly: **the external yield pays for the custody**. That is the most attractive single idea here for Aurumix, and it is peg-neutral because it never touches grams.

**Q2 Dividend funding. The headline answer.** Real external yield is achievable and documentable, with a contractual net-yield floor as the screening mechanism. Copy the **3% net-after-origination-fees "Passing Lease" definition** and the **absolute discretion to reject any individual lease**: those two clauses together let an issuer advertise a yield range honestly without guaranteeing it. But Streamex proves the cost as well as the benefit: to get 3–4%, the gold must leave your control, be commingled with strangers' gold, become unreturnable for 90 days, and expose your holders to a jeweller's credit. **For a mass-retail SIP product sold to first-time savers in India and the UAE, that trade is materially worse than it is for a $200,000-minimum accredited investor.** Aurumix's ICS Dividend is promised to retail; Streamex's yield is sold to professionals who can price counterparty risk. If Aurumix adopts leasing, the disclosure burden and the wind-down implications scale accordingly.

**Q3 Token standard.** Confirms the client's instinct. Streamex, treating the instrument as a security from day one, went **permissioned and whitelisted** (ERC-20 on Base but KYC-gated, CCIP for cross-chain). It bought compliance and cost them any real secondary market: 19 holders. Aurumix's ERC-3643 lean is directionally right; the lesson is that permissioning and liquidity are a genuine trade, not a free win.

**Q4 Regulatory route.** No licence anywhere. The route is a **US private-placement exemption (Reg D 506(c)) into a Cayman SPV**, with credibility borrowed from the parent's Nasdaq listing. **This route is unavailable to Aurumix**: it is accredited-investor-only by construction, which is the exact opposite of a $20/month retail SIP. Nothing here provides an alternative to VARA, and nothing here touches the ADGM Accepted Spot Commodity route. What it *does* provide is the observation that a **listed parent produces high-quality public disclosure as a by-product**, which is a reputational asset Aurumix cannot replicate cheaply.

**Q5 Redemption.** GLDY offers what Aurumix does not: redemption in physical gold, stablecoins, digital assets or USD. But it is **90 days' notice, "subject to certain limitations", and hedged in the 10-K as possibly unavailable because the gold is unallocated**. Useful for the client: **once you lease the gold, instant redemption becomes structurally impossible.** Aurumix's no-physical-redemption stance is at least internally consistent with a yield-bearing design, and Streamex's 90-day notice is the honest form of the same constraint. The presentational risk is identical: advertising "you own physical gold" while operating a notice-period claim on a commingled leased pool.

**Q6 Premium.** One data point at the illiquid extreme, already covered in §9. No premium observable, no re-argument needed.

**Q7 Proof of reserve.** A model to imitate on scope and a warning on sequencing. The **EisnerAmper AICPA examination explicitly covers gold in reserve *and gold on lease***, which is exactly the right scope for a leasing structure and is the thing Aurumix must specify if it ever leases. But note the order of operations: Streamex launched the token in **February 2026** and produced its first attestation in **July 2026**, having disclosed in the interim that it had no live PoR dashboard and no bar-level linkage. And the attestation is over ~3,065 ounces that are ~98.5% owned by the issuer. **Attest before you sell, not after**, and be careful that an attestation over your own inventory is not mistaken for holder protection.

**Q8 Distribution.** Speaks to it only by contrast, which is itself the finding: **no savings plan, no SIP, no referral, no agent network, $200,000 minimum.** GLDY is the anti-Aurumix on distribution. It confirms yet again that the recurring-contribution agent model is unoccupied in tokenized gold.

**Q9 Wind-down.** **No wind-down plan published.** Worse, the 10-K states holders "may face delays, partial recovery, or **total loss** in the event of SPV insolvency or service provider failure", and concedes that other lessors in the commingled pool "may receive more favorable terms or priority in enforcement scenarios". So the failure mode is disclosed but unplanned. This *strengthens* the wind-down differentiation thesis: even the best-documented protocol in the set, with a Nasdaq-listed parent and Big-Four-adjacent auditors, has not said what happens to the gold if it fails.

### The single most useful finding

**Real, externally-funded gold yield is documentable, and Streamex has filed the document. But the filed document protects the two corporates and stops there.** The 110% two-layer insurance (including DIC/DIL cover for lessee fraud through a Lloyd's broker) is genuinely good design worth copying almost verbatim, yet the loss payee is **Monetary Metals, "wherever possible"**, and the token holder is four entities away from the gold with no security interest, no waterfall and an explicit disclaimer of any fiduciary duty. **If Aurumix builds a leasing-funded dividend, the differentiating move is not the lease itself: it is being the first to name the token holders (or a trustee acting for them) as loss payee and to publish the default waterfall.** That gap is currently unoccupied by every protocol we have profiled, including this one, and it is available cheaply.

## 13. Open items for verification

- [ ] Obtain the **"Lease Documentation"** and the separately referenced **"Precious Metals Lease Program Agreement"** (Ex-10.1 §§3.01(b), 3.03). Neither is filed. Request via SEC correspondence review or check for later 10-K/10-Q exhibit filings. **This is where every default, title and waterfall term actually lives.**
- [ ] Confirm whether any **Form D** was filed for the GLDY 506(c) offering, and under which entity (Streamex Corp., Streamex Ltd., or neither). Not located under CIK 0001530766.
- [ ] Verify **Streamex Ltd.** against the **Cayman Islands General Registry**, and check for any CIMA registration or exemption. Registry search not completed.
- [ ] Verify **Streamex Exchange Corporation** against the **BC Registry** (stated: incorporated 5 April 2024) and confirm current status.
- [ ] **Name the LBMA-accredited custodian.** Unnamed in every SEC filing. Secondary sources suggesting Anchorage / Coinbase Prime / tZERO and administrator Zedra are **unverified and low confidence**; do not carry them forward without a primary source.
- [ ] Obtain the **full EisnerAmper attestation report**, not the press release, and confirm the split between gold in vault and gold on lease as of 31 March 2026.
- [ ] Assess the **independence question**: EisnerAmper issued the GLDY reserve attestation (announced 1 Jul 2026) and was engaged as the parent's statutory auditor on 8 Jul 2026.
- [ ] Obtain the **GLDY subscription agreement / offering memorandum** to establish subscription, management and redemption fees, all currently Not disclosed, and the "certain limitations" qualifying redemption.
- [ ] Establish the **GLDY contract address on Base** and any Solana mint, and whether any **smart-contract audit** exists. Issuer does not publish the address.
- [ ] Determine whether **any GLDY gold has actually been placed on lease yet**, the number of live leases, and whether any lessee is in default. The attestation's coverage of "gold on lease" implies yes; quantum unknown.
- [ ] Confirm current **third-party holder percentage** post-Q1 2026. The 98.5% parent-held figure is as of 31 March 2026; a Q2 10-Q should update it.
- [ ] Track the **BC Supreme Court civil claim** (filed Nov 2025) for any disclosure about the pre-acquisition structure of Streamex Exchange.
- [ ] Check whether **Monetary Metals** has published anything on the **AgaBullion default (26 Jan 2026)** recovery outcome, and whether the DIC/DIL Lloyd's layer actually paid. That is the live test of whether this insurance design works.

---

# Digital Gold (DGLD)

**Status: LIVE, and this is a correction to the task premise.** DGLD was not a protocol that quietly died. It was a protocol that quietly died and then was **bought out of dormancy and relaunched**, which is a materially different and more useful story. MKS PAMP acquired 100% of the issuer on 20 November 2025, redeployed the token on Base on 16 December 2025, survived a **$250k bridge exploit on 23 February 2026**, and is trading today with a live 1-gram physical redemption path.

The dormancy was real: roughly **six years of near-total inactivity** between the 2019 launch and the November 2025 relaunch, described by MKS PAMP's own CEO as a launch that was "too early" ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)). So the failure the task anticipated did happen. What did not happen is the wind-down. **DGLD is the only protocol in the set that failed and came back, and the reason it could come back is the most transferable finding in this profile.** See §12.

**Second correction: the chain was not RSK.** The task brief states DGLD used RSK. It did not. It launched on **Ocean, a Bitcoin sidechain built by CommerceBlock** on the Blockstream Liquid codebase. This matters because Ocean's failure mode is specific to it, not generic to Bitcoin sidechains. See §8.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | DGLD | **High** |
| Issuer (marketing) | "Gold Token SA (GTSA), the tokenization arm of MKS PAMP" | **High** |
| Issuer (registry) | **Gold Token SA, CHE-287.630.262**, société anonyme, incorporated **8 August 2018**, seat **Carouge, Geneva** (moved from Geneva 26 May 2025), share capital **CHF 3,401,100** (reduced from CHF 4,668,500 on 11 Apr 2024), status **Active** ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)) | **High** |
| Parent | **MKS PAMP SA, CHE-105.871.847**. Acquired 100% of GTSA 20 Nov 2025 ([dgld.ch](https://dgld.ch/about-us)) | **High** |
| Domicile | **Switzerland (Canton of Geneva)**. Governing law Swiss, courts of Geneva | **High** |
| Backing claim | 1 DGLD = **1 fine troy ounce** of LBMA-certified PAMP gold, allocated, in MKS PAMP Swiss vaults | **High** |
| Chains | **Ethereum + Base**. Originally Ocean (Bitcoin sidechain), migrated Nov 2022 | **High** |
| Contract address(es) | Ethereum `0xA9299C296d7830A99414d1E5546F5171fA01E9c8`; Base `0xe908475f8Beb7A138B0dc6eb5A05cb27068ffB9A`. **Both redeployed March 2026 post-exploit** | **High** |
| Supply | **~2,004.85 DGLD** (~2,005 oz): 1,603.69 on Ethereum, 401.16 on Base ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)) | **High** |
| Market cap / AUM | **~$8.1M** | **High** |
| Daily volume | **~$12k–19k** across three Uniswap V4 / Aerodrome pools ([CoinGecko](https://www.coingecko.com/en/coins/gold-token-sa-dgld-tokenized-gold)) | **High** |
| Holders | ~3,025 (Ethereum) / ~3,962 (all chains), +32.5% over 30 days | **Medium** |
| Regulatory status | **No FINMA licence.** AML affiliation to **VQF**, a FINMA-supervised SRO. Membership number **Not disclosed** | **High** |
| Subscription fee | **0.20%** ("Creation Fee") | **High** |
| Ongoing custody fee | **Zero.** "Embedded in DGLD... Tokenholders are not charged any separate or additional fees" | **High** |
| Redemption fee | **0.20%** ("Burning Fee") + third-party shipping/insurance/customs at cost | **High** |
| Minimum redemption | **1 gram** | **High** |
| Minimum direct subscription | **400 XAU (~$1.6M)**, accredited institutions only | **Medium** |
| Advertised yield | **None.** T&Cs expressly disclaim "any financial return, interest, dividend" | **High** |
| Named officers | **James Emmett** (President/board), **Kurt Hemecker** (CEO, GTSA), **Roman Peter Schnider** (board), per register as of 12 Jan 2026 | **High** |

---

## 1. What it is

DGLD is a 1-token-1-troy-ounce gold token issued by Gold Token SA, a Geneva company that is now the wholly owned tokenisation arm of **MKS PAMP**, one of the largest precious-metals refining and vaulting groups in the world. The gold is PAMP-refined, LBMA-certified, allocated to specific bars, and vaulted in Switzerland.

Its history splits cleanly into three phases:

1. **2019–2022, the consortium era.** Launched 15 October 2019 by a consortium of **CoinShares International**, **MKS SA** and **Blockchain.com**, on the **Ocean** Bitcoin sidechain ([CoinDesk](https://www.coindesk.com/markets/2019/10/15/coinshares-blockchain-launch-gold-token-network-on-a-bitcoin-sidechain/)). Backed by ~$20M of gold at launch. Each token was **one-tenth of a troy ounce** at this stage, not one ounce ([The Block](https://www.theblock.co/post/43306/coinshares-jointly-rolls-out-a-gold-token-dgld-built-on-the-bitcoin-network)).
2. **2022–2025, dormancy.** Migrated off the sidechain to Ethereum in November 2022. Then essentially nothing for three years.
3. **Nov 2025–present, the MKS PAMP relaunch.** Full acquisition, Base deployment, professional market-making, a live retail redemption path.

The distinguishing feature, and the reason this profile is worth reading despite an $8M market cap, is that **DGLD's legal structure is the strongest in the entire landscape set**: genuine co-ownership of specific bars under Swiss property law, not a creditor claim. See §2.

## 2. Legal structure

**This is the best-documented and strongest holder position we have found across ten protocols, and it is worth quoting exactly.** From the [General Terms & Conditions](https://dgld.ch/legal/general-terms-conditions-dgld-2):

> "The DGLD token qualifies as a title of proof (art. 8 CC)."

> Holders acquire **"co-ownership rights (art. 646 CC) and indirect possession (art. 919 CC) over the Gold."**

> **"Title to and ownership in Gold shall at all times remain with the Tokenholder."**

And the negative limb, equally explicit:

> "DGLD does not however represent claims such as a debt or equity claim or other financial claim against GTSA" and "does not confer any financial return, interest, dividend, claim for repayment."

**Confidence: High.** This is a primary legal document, not marketing.

Read carefully, this is a genuinely different instrument from most of the set. A DGLD holder is **not a creditor of the issuer**. They are a **co-owner of a pool of specific gold bars** under Swiss Civil Code articles 646 (co-ownership) and 919 (possession), with GTSA and the custodian holding as **indirect possessors** on their behalf. Transfer of the token is constructed as a transfer of the co-ownership right under property law, with the custodian "deemed to be validly notified of the transfer... via the change of records in the Blockchain."

**Why this matters more than it sounds.** In an insolvency of GTSA, a creditor claim ranks with other unsecured creditors and the gold is an asset of the estate. A **co-ownership right is not an asset of the estate at all**: it is third-party property that must be segregated out. That is the whole ballgame for a gold token, and DGLD is one of the few that has actually documented it in enforceable terms rather than asserting "your gold is safe."

**Caveats, stated plainly:**

- rwa.xyz describes DGLD as **"bankruptcy-remote under Swiss law"** and cites the Swiss DLT Act with FINMA supervision ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). The **T&Cs themselves contain no insolvency clause** and do not cite the DLT Act, DLT-TEF, or **art. 242a of the Debt Enforcement and Bankruptcy Act** (the provision that actually governs segregation of crypto-based assets in a Swiss bankruptcy). Perplexity searching also found no such citation. So the bankruptcy-remoteness claim rests on the **inference** from arts. 646/919 rather than an express contractual or statutory recital. **Confidence: Medium** on bankruptcy remoteness as a legal conclusion; **High** on the co-ownership language it is built from.
- rwa.xyz's statement that GTSA is "supervised by FINMA" is **wrong**, or at best a compression. GTSA is an SRO member. See §3.
- Co-ownership is of a **pool**, not of a nominated bar per holder, notwithstanding the per-bar verification tool. Whether a holder can compel delivery of a **specific** serial-numbered bar is **Not disclosed**.

## 3. Regulatory and compliance posture

| What we checked | Result |
|---|---|
| FINMA licence (bank, securities firm, fund manager) held by GTSA | **Not found.** No FINMA authorisation identified or claimed |
| SRO affiliation | **VQF**, a FINMA-supervised self-regulatory organisation ([dgld.ch](https://dgld.ch/about-us)) |
| VQF membership number | **Not disclosed.** Not published by GTSA and not located on VQF registers |
| Swiss commercial register | **Active**, CHE-287.630.262, Carouge GE ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)) |
| Registered purpose covers token issuance | **Yes**, expressly: "l'émission et la commercialisation de jetons virtuels... adossés à des matières premières physiques" |
| Enforcement action against GTSA or MKS PAMP | **None found** |
| EU/EEA marketing | **Expressly disclaimed**: "Gold Token SA does not target or solicit EU/EEA persons"; EU/EEA access permitted on reverse solicitation only |

**The key distinction, and it is the same trap as "audited".** VQF membership is an **anti-money-laundering** affiliation. It is what a Swiss financial intermediary joins instead of being directly supervised by FINMA for AML purposes. **It is not a licence, it does not involve FINMA approving the product, and it says nothing about prudential soundness, reserve adequacy or investor protection.** GTSA's own phrasing, "regulated through VQF, a FINMA-supervised SRO," is accurate but engineered to put "FINMA" in the sentence. rwa.xyz then compressed it into "supervised by FINMA," which is false. **This is the "regulated in Switzerland" halo effect in action, and the compression happened within one hop of the issuer's own wording.**

Notably, the registered corporate purpose **does** expressly authorise commodity-backed token issuance, which is more than can be said for Comtech's DAFZA licence. GTSA is lawfully doing what its register entry says it does. It just is not prudentially licensed for it, and it does not claim to be.

**Relevance to design question 4:** DGLD is the Swiss analogue of the "cheap route" Aurumix is hunting for. An SRO affiliation plus a well-drafted property-law structure, at a fraction of a VARA licence's cost. The trade is that **the protection comes from Swiss property law and the courts of Geneva, not from a regulator**. That works precisely because Swiss law has a strong, tested doctrine of co-ownership in fungible custody pools. **It is not obviously portable to the UAE**, and Aurumix should not assume it is.

## 4. Custody and proof of reserve

| Element | DGLD |
|---|---|
| Gold custodian | **MKS PAMP SA** vault facilities, Switzerland (PAMP SA refinery at Castel San Pietro) |
| Vault city | Switzerland; specific vault site **Not disclosed** |
| Allocated? | **Yes**, asserted as allocated LBMA-certified PAMP bars with co-ownership at law |
| Bar list | **Yes, and this is genuinely strong.** The `dgld.ch/verify` tool takes a wallet address and returns **specific PAMP bar serial numbers, refinery dates and vault locations** for that holder's position, from 0.001 DGLD upward ([step-by-step guide](https://dgld.ch/news/dgld-complete-step-by-step-guide-november-2025)) |
| PoR feed | Per-wallet verification tool rather than an oracle feed. No Chainlink PoR identified |
| Reserve attestation | **Contested. rwa.xyz names KPMG as auditor** ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). **We could not confirm this from any GTSA source, and a dedicated search found no DGLD reserve attestation report, no named attestor and no stated frequency.** GTSA's verify tool refers to "latest signed audits" without naming the signer. **Confidence: Low** on KPMG; **the absence of a downloadable, dated, named-firm reserve attestation is the finding** |
| Smart contract audit | **Yes, and now unusually well evidenced: Hacken and Halborn**, both engaged post-exploit, both reports stated to be publicly released, March 2026 ([post-incident report](https://dgld.ch/news/post-incident-report-february-2026-exploit)) |
| Token infrastructure custody | **Utila Inc** per rwa.xyz. Unconfirmed from GTSA sources. **Confidence: Low** |

**Apply the brief's rule precisely here, because DGLD inverts the usual pattern.** Most protocols in this set have a smart-contract audit and no reserve attestation, while implying the reverse. DGLD **also** has the strong smart-contract audits and the unconfirmed reserve attestation, but it compensates with something better than most attestations: **a per-holder, serial-number-level bar lookup**. A retail holder can check their own specific bars. That is more useful to an individual than a quarterly PDF saying the aggregate balances.

**But it is not a substitute for an attestation, and the distinction is exactly the one the brief warns about.** The verify tool is **issuer-published data**. It proves GTSA's records are internally consistent with the chain. It does not prove an independent third party physically counted the bars. And per PMGT: **an issuer-hosted verification tool has exactly the lifespan of the issuer's hosting bill.** DGLD's six dormant years are direct evidence of how quickly issuer infrastructure can go quiet.

## 5. Issuance

**Two-tier, and the tiers are very far apart.**

- **Primary (direct minting with GTSA):** restricted to **accredited institutions**. MKS PAMP issues DGLD only to accredited institutions, who then sell on secondary crypto exchanges ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)). Minimum subscription reported as **400 XAU**, roughly **$1.6M** at current prices ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). **Confidence: Medium** (single source; not published in the T&Cs). Creation fee **0.20%**.
- **Secondary (everyone else):** buy on Uniswap V4 (Ethereum) or Aerodrome (Base). **No KYC at all.** GTSA's own guide states KYC "is entirely optional and only triggers" on a physical delivery request.

MKS PAMP's **trading arm purchases tokens and provides liquidity on exchanges**, so the group is both issuer and principal market maker. The February 2026 incident report confirms this directly: GTSA bore the large majority of the ~$250k loss "as we serve as the principal liquidity provider."

**This is a materially different distribution model from Aurumix's and worth noting: a $1.6M primary minimum with a zero-KYC secondary market.** Retail is served, but only ever as a price-taker on a DEX, never as a primary subscriber.

## 6. Redemption

**DGLD has the most retail-accessible physical redemption in the entire landscape set, and by a wide margin.**

- **Minimum: 1 gram.** Not 1 ounce, not a 400oz Good Delivery bar, not "qualified holders." One gram, from a $4,000-per-token instrument.
- **Fee: 0.20% flat**, plus actual third-party shipping, insurance and customs at cost. GTSA "does not currently charge any separate fee or surcharge" on delivery.
- **Process:** email `support@dgld.ch` with wallet address, grams and shipping address; receive a quote within hours; complete **one-time KYC (ID + selfie, 5–10 minutes)**; transfer DGLD and pay; receive shipped bars. Europe 3–7 business days by insured post, other regions on request.
- **Eligibility, from the T&Cs:** any entity demonstrating "power of disposal over the relevant DGLD may request the delivery of the corresponding Gold."

**That eligibility clause is the important one.** Compare the brief's warning about eligibility limited to undefined "qualified holders." DGLD's test is **control of the tokens**, full stop. It is not limited to the original subscriber, not limited to accredited investors, and not limited to a minimum ounce count. **A holder who bought $130 of DGLD on Uniswap with no KYC can convert it into a physical gram of PAMP gold shipped to their door.**

GTSA reserves rights to "refuse, suspend or postpone a Delivery" for KYC/AML failure, ownership conflicts, suspected unlawful activity, or where "Delivery would otherwise be contrary to applicable law." These are ordinary and narrowly drawn.

**Direct answer to design question 5.** DGLD is the sharpest possible counter-example to Aurumix's no-physical-redemption design. It demonstrates that gram-level retail physical delivery is **operationally solvable at 0.20%** by an issuer that happens to own the refinery. That is the honest comparison: MKS PAMP can do this cheaply because it *is* PAMP. Aurumix cannot replicate the cost base. But Aurumix should stop treating "no physical redemption" as an industry norm it is merely conforming to. **It is a deliberate retention and credit-revenue choice, and DGLD is the proof that the alternative exists at retail scale.**

## 7. Fees and revenue model

| Fee line | DGLD |
|---|---|
| Subscription / creation | **0.20%** |
| Ongoing custody / storage | **Zero to the holder.** "Embedded in DGLD. Accordingly, Tokenholders are not charged any separate or additional fees" |
| Redemption / burning | **0.20%** |
| Re-issuance | Amount "determined by GTSA before the process begins", unquantified |
| Physical delivery | Third-party transport, insurance, customs at cost. No GTSA surcharge "currently" |
| Transfer | None from issuer (gas only) |
| Yield paid to holders | **None**, expressly disclaimed |

**Per the wave-1 addendum, question 1 is settled, so just the two things that are actually novel here.**

**First, the funding mechanism is the cleanest in the set.** Most zero-custody-fee protocols leave "what funds the vault?" unanswered. DGLD's answer is structural and credible: **MKS PAMP owns the vaults and the refinery.** Storage is marginal cost on infrastructure the group already runs for its core bullion business. This is not cross-subsidy from investor fees, it is genuine vertical integration. **This is the one protocol in the set whose zero-fee promise is economically self-evident.**

**Second, watch the word "embedded."** The T&Cs say storage and administration costs are "embedded in DGLD." That phrasing is doing unexamined work. If it means the cost is absorbed by MKS PAMP, fine. If it ever comes to mean the cost is recovered **from the gold backing each token**, then the ounce-per-token ratio drifts below 1 and DGLD's central claim breaks. **We found no clause specifying which.** For a 1-token-1-ounce product that would be peg-breaking. **For Aurumix, whose peg is grams ÷ tokens, an in-kind deduction is peg-neutral** (the same logic as the PAXG minting clause flagged in the addendum). Worth quoting to the client as a second precedent for in-kind fee recovery, with the caveat that DGLD has not disclosed that this is what it does.

**Also note the "currently" in the delivery-fee clause.** GTSA "does not *currently* charge any separate fee or surcharge." That is a reserved right to start charging, exactly the pattern the addendum flags as the interesting case.

## 8. Token architecture

- **Standard:** ERC-20 on Ethereum and Base. **Not permissioned.** Freely transferable, no whitelist, no KYC gate on transfer.
- **Original chain: Ocean, a Bitcoin sidechain developed by CommerceBlock**, built on the **Blockstream Liquid codebase**. CommerceBlock claimed Ocean removed Liquid's federated second layer of trust ([CoinDesk](https://www.coindesk.com/markets/2019/10/15/coinshares-blockchain-launch-gold-token-network-on-a-bitcoin-sidechain/), [Bitcoin Magazine](https://bitcoinmagazine.com/technical/coinshares-blockchain-launches-digital-gold-token-on-bitcoin-sidechain)). **This is not RSK, and the brief's premise should be corrected.**
- **Migration:** moved to Ethereum in **November 2022**. The original sidechain DGLD **ceased to exist**, and the wrapped `wDGLD` tokens that had existed on Ethereum since 2020 were replaced by the new native ERC-20 DGLD.
- **Upgradeability / admin keys:** GTSA can **pause** both contracts (exercised February 2026), **redeploy** them, and **reset balances to a pre-exploit snapshot** (exercised March 2026). These are extensive unilateral powers. Precise role architecture **Not disclosed**.
- **Bridge:** a native Ethereum↔Base bridge. **This is what was exploited.**
- **Audits:** Hacken and Halborn, March 2026.

### What the Bitcoin-sidechain choice actually cost it

This is the question the task asked, and the answer is unusually clean because DGLD ran the experiment and then reversed it.

**The direct costs of Ocean, 2019–2022:**

1. **No composability, which was the entire point of being on-chain.** In 2019–2021 the whole tokenised-asset thesis was DeFi: collateral in lending markets, AMM pairs, yield strategies. Ocean had none of that. There was no Uniswap, no Aave, no Curve. A gold token on Ocean was a database entry with extra steps.
2. **No wallet support.** GTSA had to build and maintain its own **`ocean-wallet`** ([GitHub](https://github.com/goldtokensa)). Every holder needed bespoke software. Compare today: paste a contract address into Uniswap. **The GitHub repo's last commit is October 2020**, which dates the abandonment of the sidechain effort a full two years before the formal Ethereum migration.
3. **They had to build a bridge to Ethereum anyway.** By November 2020, barely a year after launch, the consortium had shipped **`wDGLD`, a wrapped ERC-20 on Ethereum**, because that was where the users were ([Blockchain.com/Medium](https://medium.com/blockchain/wrapped-dgld-brings-swiss-vault-held-gold-to-ethereum-2a4a8cae81b1)). **The sidechain strategy was conceded within 13 months.** The wrapper then added its own trust layer, so holders got the sidechain's illiquidity *and* a bridge's risk.
4. **No exchange listings.** Listing a Bitcoin-sidechain asset requires a CEX to integrate a bespoke node. Almost none did. The addressable venue set was near zero.
5. **The security narrative did not convert into users.** "Secured by the Bitcoin network" was the pitch. Bitcoin holders are, in practice, the population *least* interested in holding a non-BTC asset, and the population most averse to unfamiliar sidechains.

**Net cost: roughly three years and the first-mover position.** DGLD launched October 2019 with ~$20M of gold, blue-chip partners and real Swiss vaulting. PAXG had launched only about a month earlier, in September 2019, on Ethereum. **PAXG is ~$1.79bn today. DGLD is ~$8M.** The custody quality was comparable. The chain choice was not. That is close to a controlled experiment, and it is the single most quantified answer to "what does the wrong chain cost."

**The counter-observation that keeps it honest:** the chain was necessary but not sufficient. DGLD migrated to Ethereum in November 2022 and **still stayed dormant for three more years**. Getting onto the right chain did not revive it. What revived it was **an owner with a commercial reason to push it**. See §12.

### The February 2026 exploit

Documented candidly by GTSA ([post-incident report, 21 March 2026](https://dgld.ch/news/post-incident-report-february-2026-exploit)):

- **23 February 2026.** An edge case in **legacy code** in the Ethereum contract's `transferFrom` "could report successful execution without enforcing the expected token movement." Via the Ethereum↔Base bridge this permitted fraudulent minting on Base.
- **Over 100 million unbacked DGLD minted on Base**, against a legitimate Base circulation of about **70.8 tokens**. A ratio of roughly 1.4 million to one.
- Contracts paused and the bridge frozen within about **2 hours 25 minutes**.
- Economic impact **~$250,000**, "in very large majority borne by us, as we serve as the principal liquidity provider."
- **All physical gold reserves unaffected.** All pre-exploit holders on both chains unaffected and retained their holdings.
- Remediation: pre-exploit balance reset 11 March, Ethereum relaunch 12 March, Base relaunch 17 March, Hacken and Halborn audits published, 45-day goodwill claims process from 11 March for **180 affected addresses across 7,000+ trades**.

**Three lessons, all of which transfer.**

1. **"Legacy code" means the 2022-era contract carried a latent flaw for over three years.** The relaunch bolted a new bridge onto old code. **The audits came after the exploit, not before.** For Aurumix: audit before deploying, and re-audit specifically at the seam whenever new infrastructure is attached to existing contracts.
2. **The property-law structure held under live stress.** 100 million fake tokens existed and **the gold was never at risk**, because the fake tokens conferred no co-ownership in anything. Token supply and gold title are separate legal facts. This is a real vindication of the §2 structure, tested in the wild rather than argued on paper.
3. **The issuer took the loss and disclosed it.** GTSA absorbed ~$250k because it was the market maker, published a detailed report a month later, and ran a claims process. **Compare PMGT, whose issuer edited the stated reason for its exit.** This is the best incident disclosure in the landscape set.

## 9. Liquidity and market

Per the wave-1 addendum, the premium thesis is settled, so this is one paragraph of data.

**~$8.1M AUM / ~2,005 tokens. Daily volume ~$12k–19k.** Liquidity sits in three pools: Uniswap V4 DGLD/USDC (~$9.4k daily) and DGLD/XAUT (~$9.4k) on Ethereum, and Aerodrome/Uniswap DGLD/USDC on Base (~$27). Monthly transfer volume ~$3.8M across 3,323 transfers, ~113 active addresses. Price **$4,045–4,081** against LBMA/spot gold of **~$4,004 (LBMA PM, 20 July 2026) to ~$4,090 (spot, 27 July 2026)**. **DGLD trades at or marginally below spot: no premium.** Turnover is roughly **0.2% of AUM daily**, thin even by this set's standards, and the market is sustained by MKS PAMP's own trading arm plus **Arrakis Finance**, which actively manages the Aerodrome position around the real-world gold price to minimise slippage.

**One more data point for the settled conclusion, from a new angle: a professionally market-made, vertically integrated, refinery-owned gold token with a 1-gram redemption right still trades at no premium.** Note also that holder count is rising fast (+32.5% in 30 days) while volume stays tiny, which says accumulation, not trading.

**Flagging a contradiction for the record:** a Sonar Pro response in this research asserted DGLD trades at a "significant premium," derived by comparing DGLD's live ~$4,166 price against a **stale ~$2,400/oz gold price from model memory**. Gold is ~$4,000–4,090/oz in July 2026. **The premium was an artefact of an out-of-date gold price, not a market observation.** Recorded because the same error would be easy to repeat elsewhere in this landscape.

## 10. Distribution

- **Channels:** DEX only for retail (Uniswap V4 on Ethereum, Aerodrome on Base). Direct primary issuance to accredited institutions. Previously listed on **Bitstamp** during the Ethereum era.
- **Target segments:** explicitly, per CEO James Emmett, **crypto-wealthy individuals** ("If you've made your money in crypto, you're very keen on having tokenized gold" and want to "stake it or leverage it") and institutional funds.
- **Geography:** Switzerland-issued, global secondary access, **EU/EEA expressly not solicited**.
- **Savings plan / SIP / recurring purchase:** **None found.**
- **Referral / affiliate / agent network:** **None found.**
- **Commission structure:** **None found.**

**Direct answer to design question 8: DGLD has no distribution mechanism of the kind Aurumix is building.** Its strategy is to be liquid where crypto capital already is (Base has ~8M monthly active users) and to let market makers do the work. It is a **liquidity-placement** strategy, not a **customer-acquisition** strategy.

This is now the near-universal finding across the set, and DGLD sharpens it: an issuer with 60 years of brand, its own refinery, its own vaults, and a genuinely best-in-class redemption right has accumulated **~$8M**. It has no mechanism to reach a saver who does not already hold crypto. **The distribution gap Aurumix is targeting is real, and DGLD is further evidence that incumbents with every asset advantage are not addressing it.**

## 11. Recent developments (dated, reverse chronological)

**28 July 2026 (today):** DGLD live and trading. ~2,005 tokens, ~$8.1M, both chains operational post-redeployment. Holder count +32.5% over 30 days. Redemption path advertised as live at 1 gram.

**21 March 2026:** GTSA publishes the [post-incident report](https://dgld.ch/news/post-incident-report-february-2026-exploit) on the February exploit. Confirms **Hacken and Halborn** audits complete with no remaining critical or high findings, and that full audit reports were released.

**17 March 2026:** Base contract relaunched.

**12 March 2026:** Updated Ethereum contract relaunched.

**11 March 2026:** Pre-exploit balance reset executed. 45-day goodwill claims process opens for **180 affected addresses across 7,000+ trades**.

**23 February 2026:** **Exploit.** Legacy `transferFrom` edge case abused via the Ethereum↔Base bridge to mint **>100 million unbacked DGLD on Base**. Contracts paused within ~2h25m. Impact **~$250k**, mostly borne by GTSA as principal liquidity provider. **Physical gold unaffected; pre-exploit holders unaffected.**

**12 January 2026:** Swiss register records current board composition: **James Emmett (President), Kurt Hemecker, Roman Peter Schnider** ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)).

**16 December 2025:** **DGLD launches on Base via Aerodrome**, with liquidity managed by **Arrakis Finance** ([PR Newswire](https://www.prnewswire.com/news-releases/dgld-the-only-gold-token-backed-by-60-years-of-swiss-precious-metals-heritage-launches-on-base-network-via-aerodrome-302643330.html)). Kurt Hemecker named as **CEO of Gold Token SA**.

**20 November 2025:** **MKS PAMP SA acquires full ownership of Gold Token SA.** CEO **James Emmett** tells Bloomberg the 2019 launch was "too early" and that the token had been **mostly dormant for six years**. Relaunch model: MKS PAMP's trading arm buys tokens and provides exchange liquidity; issuance restricted to accredited institutions ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)).

**19 November 2025:** GTSA publishes its [step-by-step guide](https://dgld.ch/news/dgld-complete-step-by-step-guide-november-2025) covering purchase, per-bar verification and 1-gram physical redemption.

**30 July 2025:** GTSA announces physical delivery **from just one gram**.

**26 May 2025:** Registered seat moves from Geneva to **Carouge GE**.

**11 April 2024:** Share capital **reduced** from CHF 4,668,500 to **CHF 3,401,100**. A capital reduction during the dormant period is consistent with returning capital as the venture wound down in substance.

**~2022–2025: dormancy.** No material announcements. Volume and attention negligible.

**November 2022:** DGLD **migrates from the Ocean Bitcoin sidechain to Ethereum** as a native ERC-20. Original sidechain DGLD ceases to exist; `wDGLD` replaced by the new token.

**November 2020:** **`wDGLD` launches on Ethereum**, a wrapped ERC-20, as Blockchain.com extends its partnership with CoinShares. **The sidechain strategy is effectively conceded ~13 months after launch.**

**October 2020:** Last commit to the `ocean-wallet` and `config` repos ([GitHub](https://github.com/goldtokensa)). Sidechain tooling abandoned.

**September 2020:** Consortium announces physical bullion redemption for DGLD ([PR Newswire](https://www.prnewswire.com/news-releases/coinshares-dgld-consortium-allows-investors-to-redeem-gold-tokens-for-physical-bullion-301152528.html)).

**15 October 2019:** **DGLD launches** on the **Ocean Bitcoin sidechain** (CommerceBlock, Liquid codebase), by **CoinShares International, MKS SA and Blockchain.com**. ~$20M of gold, vaulted at PAMP. **1 DGLD = 1/10 troy ounce** at launch.

**8 August 2018:** **Gold Token SA incorporated**, Geneva, CHE-287.630.262.

### What happened to the original backers

**CoinShares and Blockchain.com are both out.** Neither appears in any GTSA material after the November 2025 acquisition, and MKS PAMP now holds **100%**. **No exit announcement, date or terms were published by any party. Confidence on the fact of exit: High** (MKS PAMP owns the whole company). **Confidence on when and how: Not disclosed.** The 11 April 2024 capital reduction is the only dated public trace of the ownership unwinding, and it is circumstantial.

### Was there a wind-down plan? Yes, and this is the exception in the set

**DGLD is the first protocol we have profiled that publishes an ex-ante wind-down clause.** Verbatim from the [T&Cs](https://dgld.ch/legal/general-terms-conditions-dgld-2):

> "If the operation of the Platform is terminated (for any reason), GTSA will inform the Tokenholders of such termination via the GTSA website. Thereafter, each Tokenholder shall choose one of the following options: requesting the Delivery as described in Section 8; or instructing GTSA to sell the Gold represented by the DGLD at its own discretion and to distribute the remaining net proceeds of sale, after deduction of any applicable fees, costs, charges and expenses incurred in connection with such sale, to the Tokenholder. If GTSA does not receive an instruction from the Tokenholder within 2 months of the communication on the GTSA/DGLD website mentioning the termination of the Platform, GTSA reserves the right to proceed with a sale according to the second option above."

**This directly contradicts the brief's claim that "no failed gold token published a wind-down plan," and the contradiction should be recorded loudly.** DGLD did publish one, before the fact, in its binding terms. It is not merely a continuity assurance of the PMGT one-sentence type: it specifies notice, a holder election, two named options, a deadline and a default.

**Now grade it honestly, because it is good but not a model to copy wholesale:**

*Strengths:* holders get a **genuine election**, and critically **physical delivery is one of the two options**, so a holder can exit into metal rather than being force-converted. There is a **defined 2-month window**. The default is stated in advance rather than improvised.

*Weaknesses, and they are the same ones that stranded PMGT holders:*
- **Notice is by website only.** No email, no on-chain notice, no registered communication. **PMGT's entire lesson is that issuer websites do not survive the issuer.** A holder who stops checking `dgld.ch` for two months is force-sold. Given DGLD sat dormant for six years, "check the website" is a demanding assumption.
- **"Sell the Gold... at its own discretion."** No pricing methodology, no reference fix, no requirement to sell at or near the LBMA price. Compare PMGT's force-sale, which was benign only because gold happened to be rising.
- **"After deduction of any applicable fees, costs, charges and expenses."** Uncapped and unquantified. Same reappearing-fees pattern PMGT displayed at exit.
- **No trigger definition.** "Terminated (for any reason)" is entirely at GTSA's option. No insolvency trigger, no minimum-AUM trigger, no notice period before termination is declared.

**Net: the best wind-down clause in the set, and still deficient in exactly the ways that matter most.** That combination is what makes it valuable to Aurumix, because it maps the gap precisely.

## 12. Relevance to Aurumix

### The headline finding: dormancy is survivable, and the reason is structural

The task asked whether DGLD had quietly died and, if so, to profile it as a failure. The accurate answer is more useful than either alternative: **DGLD died commercially and then recovered, and the recovery was possible because of decisions made at launch.**

Six years dormant. Backers gone. Capital reduced. Then bought and restarted. Now compare **PMGT**, which under the same commercial pressure was switched off permanently, and **Cache Gold** and **Digix**, which wound down. What made DGLD recoverable when they were not?

1. **The gold was never encumbered or dissipated**, because holders owned it outright at law. There was no unwinding problem: dormant DGLD was just gold sitting in a vault with valid title. A restart required no one's permission.
2. **The custodian and the issuer ended up as the same economic group.** MKS PAMP could buy the whole issuer and instantly own the full stack.
3. **The token never lost its backing during dormancy**, so old holders were not wiped out and the brand was not poisoned.

**The transferable lesson: a gold token's survivability is determined by whether the gold's legal position is independent of the operating company's fortunes.** DGLD's arts. 646/919 co-ownership meant six years of corporate neglect did not damage holders. **Aurumix should ask, of its own structure: if the operating company goes quiet for three years, what happens to the gold and to holders?** If the answer depends on Aurumix being an operating, solvent, willing counterparty (and with cash-buyback-only exit it currently does), then Aurumix has PMGT's fragility, not DGLD's resilience.

### Answers to the live design questions

**Q2, dividend funding. DGLD is a clean negative data point, and a useful one.** It pays **nothing**, and its T&Cs go out of their way to disclaim "any financial return, interest, dividend, claim for repayment." That disclaimer is not accidental. It is what lets GTSA characterise DGLD as **property (a title of proof under art. 8 CC) rather than a financial claim**, which is precisely what keeps it outside securities and collective-investment regulation and lets it live on an SRO affiliation instead of a FINMA licence. **The most sophisticated legal structure in the set bought its regulatory simplicity by disclaiming yield.** Aurumix's ICS Dividend is the exact feature DGLD deliberately refused. That does not make it wrong, but it prices it: **the dividend is what converts a property instrument into a financial one, and the hybrid-regulation problem follows from that single choice.**

**Q3, token standard.** Plain ERC-20, freely transferable, no permissioning. It works for DGLD **only because the token carries no rights that break on anonymous transfer**: co-ownership travels with the token, and there is nothing else attached. The T&Cs even construct transfer as a property-law conveyance with the custodian deemed notified by the chain state. **This is the cleanest illustration of the principle behind Aurumix's ERC-3643 lean.** DGLD can be a permissionless ERC-20 precisely because it has no ICS standing, no dividend entitlement, no credit eligibility. Aurumix has all three, so it cannot copy this. **The rule: permissionless works if and only if the token's entire content is transferable property.**

**Q5, redemption.** Covered in §6. **1 gram, 0.20%, KYC only at delivery, eligibility by control of tokens.** This is the benchmark Aurumix's no-redemption model will be measured against by any sophisticated reader, and Aurumix should meet the comparison head-on rather than implying redemption is generally unavailable in this market.

**Q7, proof of reserve.** DGLD offers **per-wallet, serial-number-level bar verification**, which is more useful to a retail holder than a quarterly aggregate PDF. **But it is issuer-published, and we could not confirm any named third-party attestor** (the KPMG reference is single-sourced to rwa.xyz and unconfirmed by GTSA). **Recommendation: Aurumix should copy the per-holder bar lookup, which is a real differentiator and cheap, and additionally commission the named attestation DGLD appears to lack.** Doing both is a defensible market-leading position.

**Q8, distribution.** No SIP, no referral, no agent network, no recurring purchase. §10.

**Q9, wind-down.** DGLD **has a published clause**, contradicting the brief. §11 grades it. **Aurumix can beat it cheaply on four specific points**, which is the most actionable output of this profile:

- [ ] **Notice by durable channel, not website.** Email plus on-chain notification plus a durable artefact (IPFS, registry filing). DGLD's website-only notice would have failed during its own dormancy.
- [ ] **A stated pricing methodology for any forced liquidation.** DGLD sells "at its own discretion." Aurumix should pre-commit to a reference fix (e.g. LBMA PM on a defined date) so the price is not the issuer's choice.
- [ ] **A cap on wind-down fees.** DGLD deducts uncapped "fees, costs, charges and expenses." Both DGLD and PMGT reappear with unquantified exit fees after advertising low or zero fees during life.
- [ ] **Defined triggers.** DGLD's termination is "for any reason," at will. Aurumix should define what events start the wind-down, and a minimum notice period before the election window opens.

### Two further transfers

**1. "Regulated in Switzerland" is a halo, and it degraded within one hop.** GTSA says "regulated through VQF, a FINMA-supervised SRO," which is true. rwa.xyz renders this as "supervised by FINMA," which is false. **VQF affiliation is AML self-regulation, not a licence, and involves no product approval or prudential oversight.** This is the same pattern as PAXG's stale NYDFS claim and the "audited" conflation: **a technically accurate issuer statement engineered to be misread, then misread.** Aurumix will face the identical temptation with VARA and ADGM terminology. Note also the parallel to Comtech: where Comtech had an unlicensed gap, **GTSA's registered corporate purpose expressly authorises commodity-backed token issuance**, so it is lawfully doing what it says. The gap is prudential, not existential.

**2. The chain choice cost roughly three years and the category lead, but it was not the cause of death.** PAXG launched about a month before DGLD with comparable custody, chose Ethereum, and is ~220x larger. That is the cost of the sidechain (§8). **But DGLD migrated to Ethereum in 2022 and stayed dormant three more years anyway.** Correct infrastructure was necessary and nowhere near sufficient. What revived it was an owner with a commercial reason to push. **For Aurumix: infrastructure choices set your ceiling, but a committed distribution owner determines whether you approach it.** This reinforces the PMGT lesson from the other direction. PMGT had no revenue line and therefore no internal advocate, and died. DGLD had no advocate for six years and merely slept, because its structure let it sleep. **Aurumix needs both: a structure that survives neglect, and a P&L that prevents it.**

## 13. Open items for verification

- [ ] **Confirm or kill the KPMG reserve attestation.** Named on [rwa.xyz](https://app.rwa.xyz/assets/DGLD), unconfirmed by any GTSA source and not found by dedicated search. Establish whether KPMG performs a **reserve attestation of the gold** or merely a **statutory financial audit of Gold Token SA**, and obtain a dated report. This is the single most important open item, since it decides whether DGLD's reserve verification is genuinely independent or issuer-published only.
- [ ] **Obtain the Hacken and Halborn audit reports.** Stated as publicly released in the March 2026 incident report but not located. Confirm scope, dates, and specifically whether the bridge was in scope.
- [ ] **Verify the 400 XAU (~$1.6M) minimum subscription** against a GTSA primary document. Currently single-sourced to rwa.xyz and absent from the published T&Cs.
- [ ] **Confirm whether Utila Inc provides token-infrastructure custody**, and obtain the admin-key/multisig architecture for both contracts. Given GTSA demonstrated power to pause, redeploy and reset balances, the key-control model is material.
- [ ] **Establish the legal basis for the "bankruptcy-remote" claim.** Obtain any legal opinion citing the Swiss DLT Act / DLT-TEF or **art. 242a DEBA**. The T&Cs rely on arts. 646/919 CC without an express insolvency recital.
- [ ] **Determine what "storage and administration costs embedded in DGLD" means operationally.** Specifically: is any cost recovered from the gold backing, which would push the ounce-per-token ratio below 1? Request the ratio history since November 2022.
- [ ] **Obtain the VQF membership number** for Gold Token SA and confirm it against the VQF member register.
- [ ] **Establish when and on what terms CoinShares International and Blockchain.com exited.** No public announcement located. Check CoinShares' annual reports and any disclosure around the 11 April 2024 capital reduction.
- [ ] **Test the redemption path end to end.** Email `support@dgld.ch` requesting a 1-gram quote to a non-EU address and record the actual quote, KYC burden, total landed cost and delivery time. This is the highest-value practical test for benchmarking Aurumix's exit design, and it is cheap.
- [ ] **Confirm whether a holder can compel delivery of a specific serial-numbered bar**, or only of an equivalent quantity from the pool. The verify tool implies specificity; art. 646 co-ownership implies a pool.
- [ ] **Obtain the outcome of the 45-day goodwill claims process** (opened 11 March 2026, ~180 addresses): how many claimed, how much was paid, and on what basis.
- [ ] **Verify current DGLD supply and per-chain split directly on Etherscan and Basescan** rather than via aggregators, given the March 2026 contract redeployment means older addresses and supply figures may be stale.

---

# Aurus (tGOLD / tXAU)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | tGOLD (tXAU). Formerly AurusGOLD (AWG), renamed 9 Nov 2022. Siblings: tSILVER (tXAG), tPLATINUM (tXPT). Ecosystem tokens: AurusX (AX), migrating to $AURUS | **High** |
| Issuer (marketing) | "Minted by independent refineries and brokers in the Aurus Ecosystem", not by Aurus. Aurus positions itself as a technology provider, not an issuer | **High** |
| Issuer (registry) | **AURUS TECHNOLOGIES LTD, company no. 11703940, England and Wales**, incorporated 29 Nov 2018, previously **AURUSGOLD LTD** (to 26 Feb 2020). Registered office 5 Brayford Square, London E1 0SG. SIC 62012 (business and domestic software development) ([Companies House](https://find-and-update.company-information.service.gov.uk/company/11703940)) | **High** |
| Second entity | **AURUS FOUNDATION, company no. 14194058**, England and Wales, incorporated 24 Jun 2022, company limited by guarantee. **Active proposal to strike off**; accounts overdue ([Companies House](https://find-and-update.company-information.service.gov.uk/company/14194058)) | **High** |
| Domicile | **United Kingdom.** No Aurus issuing entity is registered in the UAE on any register located. Secondary sources list the issuer as Dubai-based: see §3, this is contradicted by the register | **High** |
| Backing claim | 1 tGOLD = 1 gram of 99.99% LBMA-accredited gold, sourced from LBMA / DMCC / LPPM accredited refineries, held by independent Vault Partners | **High** (issuer whitepaper) |
| Chains | Ethereum and Polygon. $AURUS launching on Base | **High** |
| Contract address(es) | tGOLD Ethereum `0xe4a6f23fb9e00fca037aa0ea0a6954de0a6c53bf`; tGOLD Polygon `0xa6da8c8999c094432c77e7d318951d34019af24b`; tSILVER Ethereum `0x34abce75d2f8f33940c721dca0f562617787bff3`; AurusX Ethereum `0xcb0d82f4dfa503c9e3b8abc7a3caa01175b2da39` ([CEX.IO migration notice](https://support.cex.io/en/articles/6701340-important-updates-for-aurus-tokens-awg-aws-awx)) | **High** |
| Supply | 43,322 tGOLD (43,322 g gold, ~1.39 tonnes… see §9 for the reconciliation problem) | **High** (on-chain) |
| Market cap / TVL | **$7.10M total protocol TVL** (28 Jul 2026), of which tGOLD ~$5.6M and tSILVER ~$1.5M ([DefiLlama](https://api.llama.fi/protocol/aurus)) | **High** |
| Regulatory status | **No licence found on any register.** Not FCA authorised or FCA cryptoasset-registered. No VARA, DMCC, ADGM, MAS or MiCA authorisation found. See §3 | **High** (as a negative finding) |
| Subscription fee | **0.5% minting/tokenization fee** on tGOLD (1.0% for tSILVER/tPLATINUM). Paid by the Provider Partner minting, not by the retail buyer | **High** |
| Ongoing custody fee | **Zero.** "No storage fees for Aurus tokens", explicit in the whitepaper. This is a deliberate design choice: see §7 and §12 | **High** |
| Redemption fee | **1.5% burn fee for tGOLD** (3% for tSILVER/tPLATINUM), paid by the Provider Partner executing the vault extraction, plus that Provider's own margin and the vault's shipping/handling. Retail redemption cost is therefore **not a published number** | **High** on the burn fee, **Not disclosed** on the all-in retail cost |
| Advertised yield | Not on tGOLD. tGOLD holders earn nothing. Yield is on the **separate** ecosystem token (AX/$AURUS), funded by tGOLD fees | **High** |
| Named officers | **Guido Jean-Paul van Stijn** (director from 29 Nov 2018, Dutch, **resident in the UAE**, correspondence address Marina Plaza 2307, Dubai); **Mark Nicolas Gesterkamp** (director from 3 Jan 2020, Dutch, resident Netherlands); **Dan Cristian Cearnau** (secretary from 4 Jan 2020, Romania) ([Companies House officers](https://find-and-update.company-information.service.gov.uk/company/11703940/officers)) | **High** |

---

## 1. What it is

Aurus is a **tokenization protocol that does not itself issue tokens**. It supplies smart contracts, an app and an API to licensed bullion businesses, who mint tGOLD, tSILVER and tPLATINUM against metal they own and place with an approved vault. Each tGOLD is 1 gram of 99.99% LBMA-accredited gold.

The whitepaper is explicit that this is the point of difference: "Aurus provides Tokenization-as-a-Service... to qualified commodity providers who account for an estimated 30% of the precious metals market. Now, these established businesses can mint and distribute their own precious metal-backed tokens, earning passive rewards from the trading activity."

Three partner roles exist, and the distinction between them matters more than any other fact in this profile:

- **Provider Partners** (bullion traders): supply and own the metal, initiate minting, run arbitrage, and execute redemptions.
- **Vault Partners** (vaults): custody and insure the bullion, audit intake, authorise minting.
- **Distributor Partners** (physical bullion retailers, i.e. the reseller tier): sell tokens to end customers through APIs and website plugins.

Aurus itself is a software vendor. The value proposition to the market is that a local bullion dealer keeps its own customers, brand and pricing rather than losing them to a centralised competitor like PAX Gold. That is the closest structural analogue to Aurumix's agent network in this landscape, which is why §10 and §12 carry the weight here.

## 2. Legal structure

**What a holder owns is asserted clearly, but nowhere contractually.** This is the central legal gap.

The whitepaper asserts unallocated-to-allocated title in strong terms: "Aurus company has no claim on precious metals allocated to the system. Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders. The bullion is stored physically by independent Vault Partners on behalf of the token holder. Token holders have the right to withdraw their bullion from a Vault Partner."

The problem is the document carrying that promise. The only legal document published on aurus.org is a four-page **Terms and Conditions dated 6 November 2024** ([PDF](https://aurus.org/Terms%20and%20Conditions%2012Nov2024.pdf)), and it is a **website terms of use, not terms of issue**. Read in full, it:

- **Names no contracting entity at all.** No company name, no number, no registered address anywhere in the document.
- **Contains no governing law or jurisdiction clause.**
- **Says nothing about gold, title, vaults, redemption, or fees.** Not one of these words appears.
- Disclaims custody generally: "AURUS itself does not custody or control user tokens."
- Disclaims the partners who actually do the work: "The website includes information, products, and services offered by third-party companies building on the AURUS ecosystem. Each product or service may be subject to separate terms and conditions. AURUS does not take responsibility for the content or accuracy of these third-party offerings."
- States: "**AURUS tokens are not securities, digital currencies, or any other form of financial instrument as defined by applicable laws.**" That is a self-serving legal conclusion asserted by an unnamed party, not a regulatory determination.
- Describes Aurus as "a decentralized DeFi platform" whose operations "align with DAO principles."

So the chain of title runs: holder → (no contract) → Provider Partner who owns the metal → (no published contract) → Vault Partner. **The holder's claim on the gold rests on a marketing whitepaper and on bilateral agreements between Aurus and its partners that are not published.** Where the whitepaper and the legal document disagree, the legal document does not merely disagree, it is silent, and silence gives the holder nothing to sue on.

**Confidence: High** that no terms of issue exist. Searched aurus.org, the whitepaper, the T&C PDF, and the tGOLD product page.

**Not disclosed:** the Provider Partner agreement, the Vault Partner agreement, and the Distributor Partner agreement. These are the documents that would actually govern the network, and none is public.

## 3. Regulatory and compliance posture

**No licence was found on any register.** Specifically checked and not found:

- **UK FCA:** no authorisation and no cryptoasset (MLR) registration for Aurus Technologies Ltd or Aurus Foundation. Aurus Technologies Ltd files at Companies House under SIC 62012, **software development**, which is consistent with a firm that has deliberately structured itself as a technology vendor rather than a financial institution.
- **UAE VARA, DMCC, ADGM:** no registration found. The whitepaper's only DMCC reference is that metal is sourced from *DMCC-accredited refineries*, which is a refinery accreditation, not a licence held by Aurus.
- **MAS, EU MiCA:** none found.

**Contradiction to flag.** The RWA data platform readi.fi records the tGOLD issuer as located in **Jumeirah, Dubai, UAE** ([readi.fi](https://readi.fi/asset/commodities-tgold-tgold-by-aurus/)). The corporate register says otherwise: the operating entity is an English company at 5 Brayford Square, London. The likely explanation is the founder-director Guido van Stijn's UAE residency and Dubai correspondence address on the Companies House record. **This is exactly the failure mode the brief warns about (the ORO case): a Dubai-appearing protocol that is in fact registered elsewhere.** Treat any "Aurus is a Dubai gold token" claim as false at entity level, while noting that its most senior director does operate from Dubai.

**The regulatory perimeter is the business model.** Aurus's answer to regulation is not to hold a licence but to **push the regulated activity onto its partners**. The regulated acts (owning bullion, custody, selling to consumers, KYC/AML, physical redemption) are all performed by "established and licensed" Provider, Vault and Distributor Partners in their own jurisdictions under their own licences. Aurus supplies the code. This is a coherent structure and it is cheap, but it means **no single regulator supervises the tGOLD product end to end**, and no regulator has approved the "you own the gold" claim in §2.

**Aurus Foundation is not an independent standards body.** It markets itself as the "global advocate for the international tokenized precious metals standards of tXAU and tXAG" and as the certifier of Distributor Partners. The register shows it is a company limited by guarantee whose **person with significant control is Aurus Technologies Ltd** (PSC filing 3 Jul 2025), i.e. a wholly controlled subsidiary, and that it received a **first Gazette notice for compulsory strike-off on 2 June 2026**, suspended on 16 July 2026, with accounts overdue since 31 March 2026 ([filing history](https://find-and-update.company-information.service.gov.uk/company/14194058/filing-history)). A certification body that is (a) owned by the company it certifies for and (b) two weeks from dissolution is not a governance safeguard.

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | Multiple independent "Vault Partners", deliberately decentralised. **No vault company is named anywhere in the whitepaper or on the site.** | **Not disclosed** (names) |
| Vault / city | "Partnered, fully-audited, and insured vaults across the globe." No country or city list published. One secondary source mentions Switzerland as an example. | **Not disclosed** |
| Allocated? | Asserted: bullion "will always remain legal ownership of the token holders", stored "on behalf of the token holder", with tokens "backed by individual gold, silver and platinum bars linked to unique serial numbers". No trust deed or bailment agreement published. | **Medium** (issuer assertion only) |
| Bar list | **Not published.** The whitepaper says bars are linked to unique serial numbers internally; no public bar list exists. | **Not disclosed** |
| PoR feed | **Chainlink Proof of Reserve is announced but NOT live.** The tGOLD page says Aurus "is collaborating with Chainlink oracle to implement Proof-of-Reserves"; the Aurus Foundation site describes it as "in the works and coming soon". No PoR feed address found on Chainlink's data feeds. The site does display a self-reported "Current reserve" figure. | **High** (that it is not live) |
| Reserve audit | **No named auditor, no attestation report, no frequency.** The whitepaper requires that bullion "is audited, stored and accepted by approved Vault Partners" and mentions "an independent auditor" confirming quality on deposit, but no attestation is published and no audit firm is named. | **Not disclosed** |
| Smart contract audit | **NonceBlox**, in connection with the November 2022 contract migration. The report itself is not linked publicly. | **Medium** |

**The audit/attestation distinction matters here and Aurus blurs it.** The word "audited" appears repeatedly across Aurus marketing ("fully-audited and insured vaults", "audited smart contracts"). A reader skims that and concludes reserves are independently verified. They are not. What exists is: (a) a smart-contract audit by NonceBlox, which says nothing about gold, and (b) vault-level internal audit obligations imposed by contract on unnamed partners, with no public output. **There is no independent reserve attestation for tGOLD.** For a $5.6M gold product this is arguably proportionate, but it is a real gap versus Tether Gold's BDO reasonable-assurance engagement.

## 5. Issuance

Issuance is partner-driven and permissioned at the business layer, not the token layer:

1. A **Provider Partner** (a licensed bullion trader, vetted by Aurus, described as "professional bullion traders of the highest integrity") sends bullion from an LBMA/DMCC/LPPM-accredited refinery to an approved **Vault Partner**.
2. The Vault Partner receives, audits and accepts the bullion, and authorises minting. Minting cannot occur without vault confirmation.
3. tGOLD is minted 1 token per gram. A **0.5% tokenization fee** is charged at mint (1.0% for silver and platinum).
4. The Provider Partner, who owns the metal and now the tokens, sells them into the market or through Distributor Partners.

Supply is therefore elastic and provider-led, and expands only when a bullion trader judges tGOLD to be trading at or above NAV plus 0.5%. Retail buyers never mint: they buy existing tokens from a distributor or exchange. Aurus explicitly states it "does not supply precious metals to the ecosystem nor sell tokens to end consumers."

## 6. Redemption

**Physical redemption exists and is a genuine product feature**, in contrast to Aurumix. Terms:

- The holder burns tokens and requests a vault extraction through a **Provider Partner** or an Aurus-partnered dealer, choosing from bars or coins on offer.
- **Burn fee: 1.5% for tGOLD**, 3% for tSILVER/tPLATINUM. The whitepaper is precise that this is charged to the **Provider** executing the extraction, not directly to the user: "For users, the fees for users redeeming physical gold, silver or platinum is dependent on the Provider Partner that is facilitating the exchange."
- Plus shipping and handling charged by the vault.
- **KYC/AML is performed by the Vault Partner** before withdrawal.
- The older AWG whitepaper documented a 10-day claim window with a bilateral "handshake" signature between holder and vault, after which the transaction auto-cancels and tokens return, fees non-refundable.

**Two caveats worth carrying into §12.** First, the *retail* redemption cost is undisclosed and unbounded: the user pays whatever the Provider Partner chooses to charge, so the 1.5% is a wholesale floor, not a consumer price. One RWA platform records a **3.00% redemption fee** for tGOLD ([rwa.xyz](https://app.rwa.xyz/assets/TXAU)), roughly double the whitepaper's burn fee, which is consistent with the Provider adding margin. Second, the whitepaper openly states that **Distributor Partners can redeem large quantities at lower per-unit fees than retail holders and resell** (§4.4.4). Redemption economics are explicitly tiered in favour of the trade.

**Minimum redemption increment: Not disclosed.** In practice it is bounded by the smallest bar or coin a given dealer offers.

## 7. Fees and revenue model

Fees are levied on the metal tokens; the ecosystem token (AX/$AURUS) carries none.

| Fee line | Rate | Paid by | Received by |
|---|---|---|---|
| Tokenization / minting (tGOLD) | **0.5%** | Provider Partner at mint | Fee pool, then split (below) |
| Tokenization / minting (tSILVER, tPLATINUM) | **1.0%** | Provider Partner | Fee pool |
| Transaction fee | **0.18%** | Initiator of each transfer | Fee pool |
| Storage / custody | **0%** | Nobody | n/a |
| Burn / withdrawal (tGOLD) | **1.5%** | Provider Partner executing extraction | Fee pool |
| Burn / withdrawal (tSILVER, tPLATINUM) | **3%** | Provider Partner | Fee pool |
| Retail redemption markup | **Not disclosed**, set by each Provider Partner | End user | Provider Partner directly |
| Vault extra services (delivery etc.) | **Not disclosed**, vault's own price, payable in tokens or fiat | End user | Vault Partner directly |
| Distributor spread | **Not disclosed**, distributor sets its own retail price | End user | Distributor Partner directly |
| Gas | Network rate | Transferor | Validators |

**The distribution of the fee pool is the most useful disclosure Aurus makes.** From the whitepaper, verbatim: "All accumulated transaction, minting and burning fees are distributed back to the ecosystem as follows: **50% of tGOLD fees to AurusX holders, and 50% to Aurus minting partners (25% Vaults, 25% Providers)**. With tSILVER and tPLATINUM **30% goes to AurusX holders, and 70% to minting partners (35% Vaults, 35% Providers)**."

Vault rewards are paid **quarterly, in metal tokens**, pro rata to grams stored, by published formula: `Vault reward = Total quarterly fees × (grams stored by vault ÷ total supply) × 0.25`.

Two things follow, and both are important for Aurumix:

1. **Aurus Technologies Ltd takes no disclosed share of the fee pool.** 100% of tGOLD fees are accounted for: 50% + 25% + 25%. How the software vendor is funded is **Not disclosed**. Candidates are partner onboarding/licence fees, an AX treasury allocation, or equity funding, but none is published. This is a genuine hole in the disclosed model.
2. **The split has changed at least three times.** Documented versions: 70% AWX / 15% providers / 15% vaults (2019–2020 AWG era); 50% AWX / 25% / 25% for gold (current whitepaper); and a March 2021 press description of "50% (25% each) to providers and vaults, 50% to AurusDeFi holders." The whitepaper reserves the right to keep changing it: "All fees on the Aurus ecosystem are subject to change... Fees will be reviewed on a regular basis and can be amended accordingly", with only a soft promise that values will be "capped through Smart Contracts". The 2022 migration to **upgradeable contracts** explicitly enabled "adjustable fees". **Partner economics here are revocable by the operator.**

## 8. Token architecture

- **Standard: plain ERC-20**, 18 decimals, on Ethereum and Polygon. The whitepaper states "All Aurus metal tokens are ERC-20 tokens 1:1 backed by 1 gram." Aurus explicitly compares itself favourably to competitors on free transferability.
- **Permissioned? No.** No whitelist, no ERC-3643, no transfer restrictions found. Tokens move freely between anonymous wallets and trade on a DEX. **Permissioning sits entirely at the fiat on-ramp and the redemption gate** (KYC by the distributor at purchase, KYC by the Vault Partner at withdrawal), not in the token contract.
- **Upgradeability: yes, and material.** The November 2022 migration deliberately moved to "upgradeable smart contracts, enabling the seamless implementation of features such as proof-of-reserves, governance, and **adjustable fees**." Admin keys and multisig arrangements are **Not disclosed**. Combined with §7, the operator can change partner revenue shares by contract upgrade.
- **Inheritance feature:** a multisig mechanism lets holders transfer tokens to heirs via lawyers acting as trustees or under power of attorney, with a reversal window. Directly comparable to Aurumix's Digital Will.
- **Bridge:** Ethereum ↔ Polygon; $AURUS is launching on Base. Bridge design and custody are **Not disclosed**.
- **Historic:** the original AWG design also used **ERC-721 "Gold Bullion Tokens"** mapped 1:1 to physical bars with LBMA serial numbers, metadata on IPFS. Whether this survives in the current tGOLD contracts is **Not disclosed**, and no public bar list is exposed from it.

## 9. Liquidity and market

This is where the model looks weakest, and it replicates the PGOLD pattern the brief already established.

- **Protocol TVL: $7.10M** (28 Jul 2026), Ethereum only, split ~$5.6M tGOLD and ~$1.5M tSILVER ([DefiLlama](https://api.llama.fi/protocol/aurus)). TVL has drifted down over the last three days ($7.24M → $7.14M → $7.10M).
- **tGOLD Ethereum total supply: 43,322 tokens = 43.3 kg of gold.** Holders: 466 ([rwa.xyz](https://app.rwa.xyz/assets/TXAU)).
- **On-chain DEX liquidity is effectively zero.** The only live pools found: TGOLD/USDT0 with **$3,126 of liquidity and $211 of 24h volume**, and a Solana TGOLD/SOL pool with **$1.71 of liquidity and $0 volume** (GeckoTerminal API, 28 Jul 2026). The Ethereum tGOLD contract shows **$0.00 24h volume** and only ~$59 of pooled reserve.
- Trading is therefore essentially **off-chain and dealer-mediated**: CEX.IO (centralised), QuickSwap, and bullion distributors Direct Bullion, Aurica Group and AgaBullion.

**Reconciliation problem to flag.** The aurus.org tGOLD page displayed a "current reserve" of **73,398.5 g** while the Ethereum contract shows **43,322 tokens**. The gap is plausibly Polygon supply plus tSILVER/tPLATINUM accounting, or a stale figure, but **the issuer publishes no reconciliation** and there is no live PoR feed to settle it. A ~30 kg discrepancy in a self-reported reserve number, with no attestation, is exactly the kind of item a PoR feed exists to close.

**Verdict on the premium thesis: Aurus is evidence against it.** Roughly $5.6M of gold has been accumulated over seven years (since 2018) with a market so thin that a $211 daily volume is the *main* on-chain pool. Aurus's own answer is not exchange liquidity at all: it is Provider Partner arbitrage against the OTC bullion market. That works to hold the peg *at NAV*, but by construction it **destroys any sustained premium**, because any premium above NAV + 0.5% is immediately minted into by a provider. Aurus is architecturally designed to trade at par, not at a premium.

## 10. Distribution

This is the section most relevant to the client, and Aurus is the only protocol in this set with a formal multi-tier reseller network.

**Channel structure.** Three contracted tiers (Provider, Vault, Distributor) plus exchanges. **Distributor Partners** are the reseller tier: "established and licensed physical bullion retailers that consumers trust." They are certified by the Aurus Foundation (see §3 for what that certification is actually worth).

**What distributors get.** From whitepaper §4.4:

- **APIs and plugins.** A REST API and a website plugin so a dealer can buy and sell tGOLD from its own site to its own client list. Aurus supplies the rails; the dealer keeps the customer relationship.
- **Own pricing.** "All Aurus Distributor Partners certified by the Aurus Foundation will be able to integrate Plugins and APIs that allow them to **buy and sell Aurus tokens at their own prices** and according to their own supplies."
- **Preferential redemption.** They can withdraw large amounts at lower per-unit fees than retail holders, then resell, and can offer delivery services at their own price.
- **Upgrade path.** A Distributor can graduate to Provider Partner, tokenize its own inventory and access the arbitrage and the 25% fee share.

**How distributors are compensated: this is the finding.** **Distributor Partners receive no share of the protocol fee pool.** The tGOLD split is 50% AurusX holders / 25% Vaults / 25% Providers, which is fully allocated. The reseller tier earns **only its own retail markup and its own service charges**, set by itself, disclosed by nobody. There is **no commission, no override, no residual, and no multi-level structure**: a Distributor's earnings do not depend on recruiting other Distributors, and no partner earns from another partner's volume. Compensation is a **merchant margin model, not an agent commission model.**

**Recurring purchase / savings plan: none found.** No SIP, no monthly contribution plan, no auto-invest, no direct debit. Purchases are one-off, dealer-mediated. Consistent with the brief's expectation that most protocols lack this.

**Referral / affiliate: none found** at the protocol level for retail users.

**Rewards, but not for gold holders.** Aurus does pay recurring income, just not to the people who own the gold. AX holders receive **monthly** distributions in tGOLD and tSILVER from the fee pool. The migration to $AURUS (see §11) restructures this toward staking and liquidity-pool incentives on Base.

**Target segments and geography.** B2B2C. Aurus sells to bullion businesses; those businesses sell to their own retail clients. Named partners span the UK (Direct Bullion), Chile (Aurica), Spain (Sempsa JP, an LBMA refinery), Singapore (Indigo Precious Metals), Turkey, and AgaBullion. **Excluded jurisdictions are significant**: the T&C bars users from the USA and its territories, Russia, Belarus, Cuba, Iran, Iraq, North Korea, Syria, Sudan, South Sudan, Yemen, Zimbabwe, Myanmar, DRC and Crimea, and imposes a UK-specific gate requiring users to confirm they are "Professional Investors" or high-net-worth individuals to access certain features. **India is not excluded.**

## 11. Recent developments

- **28 July 2026 (today):** protocol TVL $7.10M, declining slightly over the preceding three days. tGOLD Ethereum 24h DEX volume $0.00. Aurus remains operating ([DefiLlama](https://api.llama.fi/protocol/aurus)).
- **16 July 2026:** Companies House records **"Compulsory strike-off action has been suspended"** (DISS16(SOAS)) for Aurus Foundation ([filing history](https://find-and-update.company-information.service.gov.uk/company/14194058/filing-history)).
- **17 June 2026:** Aurus Technologies Ltd confirmation statement became **overdue** (due 17 June 2026) ([Companies House](https://find-and-update.company-information.service.gov.uk/company/11703940)).
- **2 June 2026:** **First Gazette notice for compulsory strike-off** issued against Aurus Foundation, the body that certifies Distributor Partners.
- **31 March 2026:** Aurus Foundation accounts for period ending 30 June 2025 became overdue; still not filed.
- **Q1 2026:** sector context only. Tokenized gold reached ~$5.6B market cap, adding ~$1.3B in the quarter ([CEX.IO Q1 2026 report](https://blog.cex.io/ecosystem/tokenized-gold-q1-2026-report-35490)). Aurus's ~$5.6M tGOLD is roughly **0.1% of that sector**, i.e. Aurus did not participate in the sector's growth.
- **22 May 2025:** **Omega Minerals partnership** to tokenize up to **1 million troy ounces of unmined, in-ground gold** at the Alice Creek property, British Columbia, as a **CGR token**, launching with 1M tokens against 25,000 troy oz, priced at $35 (COMEX spot less all-in sustaining cost). Sold via pre-sale to accredited/HNW investors at aurus.org/omega, with a 0.5% minting fee to the Aurus Protocol Vault ([OurCryptoTalk](https://ourcryptotalk.com/news/aurus-to-tokenize-1-6b-gold)). **This is a categorically different and much riskier product than tGOLD: it is tokenized mineral reserve, not vaulted metal**, and it should not be conflated with tGOLD's backing.
- **~March–April 2025:** **$AURUS Token Generation Event** and migration from AurusX (AX), on the **Base** network. Two-thirds of AX supply (20,000,000 tokens) burned in weekly 5,000,000 tranches down to 9,999,999 AX. Staked AX earns tiered $AURUS: 15 $AURUS per AX for the first 2M staked, 8 for the second 2M, 4 above 4M. AX must be staked before TGE to keep claiming monthly gold/silver rewards ([Mitrade, 6 Mar 2025](https://www.mitrade.com/insights/news/live-news/article-3-680539-20250306); [aurus.org/aurusx](https://aurus.org/aurusx)).
- **$AURUS model change (undated, current on site):** the new token introduces "algorithmic token issuance", automated burns, 50% of supply distributed in the first 24 months, single-staking, and **Core Protocol Fees collected in a new "cGOLD" token** from minting/burning and transfer fees, directed partly to liquidity pools ([aurus.org/$aurus](https://aurus.org/$aurus)). **This appears to redirect fee flows away from the clean 50/25/25 whitepaper split toward LP incentives, but no updated whitepaper documents the new split.**
- **6 November 2024:** current Terms and Conditions published (the four-page website terms discussed in §2).
- **9 November 2022:** network upgrade. AWG→tGOLD, AWS→tSILVER, AWX→AurusX, migrated 1:1 to new **upgradeable** contracts audited by **NonceBlox**, adding proof-of-reserves capability, governance and **adjustable fees**.

**Not found:** any confirmed live Chainlink PoR feed; any reserve attestation; any enforcement action against Aurus; any security incident or exploit.

## 12. Relevance to Aurumix

Aurus is the closest structural analogue to Aurumix's distribution model in this landscape, and it is instructive mostly by contrast. It answers questions 1, 3, 5, 6, 7, 8 and 9.

**Q8, distribution: the single most useful finding. A multi-tier partner network can be built without a commission structure, and Aurus's tiers are compensated for capital and custody, not for selling.** The three tiers are *functional*, not *hierarchical*: Providers supply metal, Vaults hold it, Distributors sell it. Fees flow to the first two (25%/25%) and to token holders (50%). **The selling tier gets nothing from the pool.** It earns its own markup on its own client list, and Aurus's pitch to it is defensive ("you will lose customers to PAX Gold if you don't") rather than an income promise.

This cuts directly at the Aurumix design. Aurumix's 3-tier agent network is a *recruitment and commission* hierarchy where agents earn from downstream volume: economically an MLM, and regulators treat it as one. Aurus's is a *supply-chain* network where each tier is paid for a distinct economic function it actually performs. **The implication: if Aurumix can re-cast its tiers so each is paid for a function (capital introduction, custody, servicing) rather than for recruitment depth, it gets most of the distribution reach with materially less classification risk.** Aurus also shows the upgrade path (Distributor → Provider) as an alternative to override commissions for motivating the top tier: let the best agents graduate into a higher-margin role rather than paying them a slice of their recruits.

Note also what Aurus does *not* have: **no savings plan, no recurring contribution, no SIP, no auto-invest, no referral scheme.** Aurumix's monthly SIP remains genuinely differentiated. Aurus's absence of it is likely why it accumulated only ~$5.6M in seven years: dealer-mediated one-off purchases do not compound. **The SIP is Aurumix's real edge, and this profile is evidence for that, not against it.**

**Q1, custody fee: Aurus is the live example of "option three", charge holders nothing and recover cost elsewhere.** Storage is explicitly 0%. It is funded by **transaction and mint/burn fees paid predominantly by the trade, not by holders**: 0.5% at mint and 1.5% at burn, both borne by Provider Partners, plus 0.18% per transfer. The vault is compensated out of that pool (25%, quarterly, pro rata to grams stored, by published formula) rather than by deducting metal. **This is a clean, working answer to the peg-breaking problem: the custodian is paid from a fee pool in tokens, so no grams are ever deducted from the backing and price = grams ÷ tokens never breaks.** Aurumix should look hard at this. The caveat is that it only works if minting and redemption churn is high enough to fund the vault. With Aurus's volumes it plainly is not, which is why the model is being restructured around LP incentives and a new cGOLD fee token. **A buy-and-hold savings product like Aurumix generates almost no transaction fees by design, so Aurus's funding mechanism does not transplant directly: Aurumix's churn will be even lower than Aurus's.**

**Q2, dividend funding: Aurus confirms the anti-pattern, but is more honest about it than PGOLD.** Aurus pays recurring income (monthly, in metal) funded entirely from investor and trade fees, exactly the recycled-fees structure the brief flags. Two mitigations Aurumix should note: (a) the yield is paid on a **separate ecosystem token (AX/$AURUS)**, not on the gold token, so tGOLD is never marketed as yield-bearing and the gold product stays clean; and (b) Aurus never promises a rate. There is no "5% APY" claim to fail. It distributes a *share of whatever fees actually arrive* (50% of tGOLD fees), which is structurally honest and cannot be arithmetically falsified. **If Aurumix keeps the ICS Dividend, expressing it as "X% of realised operating profit" rather than a headline yield, and separating the entitlement from the gold token, follows Aurus's safer path.** Aurumix's current design already does the first; it does not do the second, because ICS standing rides on the gold token itself.

**Q3, token standard: Aurus is the counter-example.** Plain ERC-20, freely transferable, no permissioning, and it works precisely because a tGOLD token carries **nothing but a claim on a gram of gold**. All the identity-dependent logic (KYC, eligibility, redemption rights) sits at the dealer and vault boundary, off-chain. Aurumix cannot copy this: AURX carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous transfer. **This strengthens the case for a permissioned base (ERC-3643).** But Aurus also shows the cost of that choice: free transferability is what lets Provider Partners arbitrage tGOLD to NAV. A permissioned Aurumix token cannot be arbitraged by third parties, so **Aurumix must be the market maker of last resort for its own token, and should budget for it.**

**Q5, redemption: Aurus offers physical redemption and it is a real gap for Aurumix, but a smaller one than it appears.** Aurus's redemption is genuine (burn, extract, KYC by vault) yet costs 1.5% wholesale, ~3% as observed retail, plus shipping, plus an undisclosed Provider markup, and requires collection or delivery from an unnamed vault in an undisclosed city. **The lesson: a redemption right whose all-in cost is undisclosed and set by an intermediary is not obviously superior to Aurumix's honest "cash buyback only".** Aurumix's position is defensible if stated plainly. What Aurus does better is that *someone* will hand you metal; Aurumix should be careful never to imply the same. Also note Aurus's explicit tiering of redemption economics in favour of the trade: that is a fairness disclosure Aurumix would be criticised for.

**Q6, premium: Aurus is further evidence against the 3–8% premium thesis, and explains the mechanism.** $5.6M of gold, 466 holders, and $211 of daily on-chain volume after seven years. More importantly, Aurus's peg is *maintained by design* through provider arbitrage against OTC bullion, which structurally caps the price at NAV plus the 0.5% mint fee. **Any tokenized gold product with an open mint path cannot sustain a premium**: the premium is the arbitrage signal that creates new supply. Aurumix's premium thesis therefore depends on *not* having an open mint, i.e. on supply discipline, which sits uneasily with "no hard cap" and continuous SIP inflows. This deserves explicit attention in mechanism design.

**Q7, proof of reserve: a cautionary example of "audited" doing too much work.** Aurus says "fully-audited and insured vaults" and "audited smart contracts" while having no named reserve auditor, no attestation, no bar list, no live PoR feed, and a self-reported reserve number (73,398.5 g) that does not obviously reconcile to on-chain supply (43,322). **Aurumix should publish a named attestor, a frequency, and a reconciliation from day one**, because this is cheap differentiation against exactly this pattern, and because the on-chain-supply-versus-claimed-grams reconciliation *is* the peg for a price = grams ÷ tokens design.

**Q9, wind-down: Aurus is the only protocol in this set with anything resembling a documented failure plan, and it is worth copying.** Two provisions: (a) **vault exit**, "If a Vault Partner is unable to continue being a Vault Partner, they are required to transport all bullion to another partner vault. Said Bullions will continue to belong to token holders during this process"; and (b) **issuer failure**, "Aurus company has no claim on precious metals allocated to the system. Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders." That is a genuine ex-ante answer to "what happens to the gold if the issuer fails", and it is **more than PMGT, Digix or Cache Gold ever published**. The weakness is that it lives in a whitepaper, not in the terms, and there is no trust deed to enforce it. **The lesson for Aurumix: the commitment is cheap and differentiating, but it must sit in the terms of issue with a named trustee, not in a whitepaper.** Aurumix has an additional problem Aurus does not: Aurus's gold is owned by Provider Partners and held bankruptcy-remote from the software company by design, whereas Aurumix intends to own the vault gold itself and lend against it at 90–95% LTV, so Aurumix creditors would rank against the same gold. **Aurus's structural separation of the technology company from the metal owner is the single cleanest idea in this profile.**

**Contradictions to record.** Nothing here contradicts the established findings on PGOLD, ORO, PMGT, Digix or Cache Gold. Two corrections to inherited framing about Aurus specifically: (1) **Aurus is a UK company, not a Dubai one**, despite at least one RWA data platform recording it as Jumeirah, Dubai, and despite its founder-director residing in Dubai. Same failure mode as ORO. (2) **Aurus does not issue tGOLD**, so describing it as a competing gold-token issuer is wrong; it is a software vendor to issuers, and its "AUM" is its partners' metal.

## 13. Open items for verification

- [ ] Obtain a **Distributor Partner agreement** and a **Provider Partner agreement**. These are the documents that would show whether resellers receive any commission beyond markup, and whether Aurus charges partners an onboarding or licence fee. Approach via a listed distributor (Direct Bullion, AgaBullion, Aurica Group) rather than Aurus.
- [ ] Determine **how Aurus Technologies Ltd is actually funded**, given it takes 0% of the disclosed fee pool. Check the Companies House accounts filed for period ending 30 November 2024 for revenue lines and related-party income.
- [ ] Confirm whether the **$AURUS / cGOLD restructuring changed the 50/25/25 split** and whether Vault and Provider Partners still receive 25% each. Request the current $AURUS tokenomics paper; the site describes LP-directed fee flows with no published split.
- [ ] Verify whether a **Chainlink PoR feed for tXAU is live** as at Q3 2026, and if so capture the feed address and update frequency.
- [ ] Reconcile the **73,398.5 g self-reported reserve against 43,322 tGOLD on Ethereum**. Obtain the Polygon supply and confirm whether the site figure aggregates metals or is stale.
- [ ] Identify at least one **named Vault Partner and its city**, and establish whether any independent reserve attestation is provided to partners privately even though it is not published.
- [ ] Check the **FCA register directly** (register.fca.org.uk was not machine-readable in this pass) for any Aurus entity, and check whether any UK Distributor Partner holds FCA cryptoasset registration that effectively covers tGOLD sales.
- [ ] Monitor **Aurus Foundation (14194058)**: strike-off was suspended 16 July 2026 and accounts are overdue. If it dissolves, the body that certifies Distributor Partners disappears. Establish who then certifies resellers.
- [ ] Establish the **actual all-in retail redemption cost** by requesting a quote from a Distributor Partner for a small redemption (e.g. 100 g), to test the gap between the 1.5% burn fee and the ~3% recorded figure.
- [ ] Obtain the **NonceBlox smart-contract audit report** and confirm admin key / upgrade authority arrangements on the upgradeable tGOLD contracts, specifically who can change fees.
- [ ] Clarify the status of the **Omega Minerals CGR token** (in-ground gold): whether it launched, whether it is marketed alongside tGOLD, and whether any tGOLD reserve is or could be commingled with mineral-reserve backing.

---

# VNX Gold (VNXAU)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | VNXAU | **High** |
| Issuer (marketing) | "VNX", with vnx.io now fronting **VNX Global Ltd.** (Bermuda) | **High** |
| Issuer (registry) | **VNX Commodities AG**, Liechtenstein commercial register **FL-0002.654.271-8**, Dr. Grass-Strasse 12, 9490 Vaduz. Still the named issuer on the 31 Dec 2025 reserve report ([FMA register](https://register.fma-li.li/), [reserve report](https://vnx.li/wp-content/uploads/2026/03/VNX_Examination_on_Management_Assertions_VNXAU_31_12_2025_signiert.pdf)) | **High** |
| Domicile | Liechtenstein for the gold token. A **second Bermuda entity (VNX Global Ltd.) took a DABA licence on 12 May 2026** ([notice](https://vnx.li/vnx-notes-bermuda-licence-obtained-by-group-entity/)) | **High** |
| Backing claim | 1 VNXAU = 1 gram LBMA-standard gold, "brutto grams", held in Liechtenstein | **High** |
| Chains | Ethereum, Solana, Base, Q, Polygon (Polygon now deprecated). Avalanche, Arbitrum, XRPL, Fraxtal, Concordium discontinued May 2026 | **High** |
| Contract address(es) | ETH `0x6d57b2e05f26c26b549231c866bdd39779e4a488`; Base `0xAc3FE22294beaED9d1FD752323a6d06D12Ff3098`; Polygon `0xC8bB8eDa94931cA2F20EF43eA7dBD58E68400400`; Solana `9TPL8droGJ7jThsq4momaoz6uhTcvX2SeMqipoPmNa8R`; Q `0xe4fadBBF24F118b1E63d65f1aAC2A825A07F7619` | **High** |
| Supply | **13,100.00 VNXAU** attested at 31 Dec 2025 = 13.1 kg gold. Down from 15,100 g at 31 Dec 2023 | **High** |
| Market cap / TVL | **~$5.73M** at $130.04/token (CoinGecko, 28 Jul 2026). Note this implies ~44,400 g, which **cannot be reconciled** with the 13.1 kg attested. See §9 | **Low** (the discrepancy is the finding) |
| Regulatory status | TVTG **registration** (not licence) with FMA Liechtenstein as Token Generator, TT Depositary, TT Identity Service Provider. **No Token Issuer registration.** TT Exchange Service Provider **expired 2 July 2026** | **High** |
| Subscription fee | "Starting from 0.1% for generation" (marketing). Platform exchange fee 0.1–0.3% by tier | **Medium** |
| Ongoing custody fee | **Zero. Advertised as "zero storage fees"** | **High** |
| Redemption fee | Not disclosed as a percentage. Physical delivery "at your own expense and risk" | **Medium** |
| Advertised yield | **None.** No staking, no APY, no leasing disclosed | **High** |
| Named officers | **Alexander Tkachenko** (signs the reserve report, listed as VNX contact in the FMA register). Dr. iur. Siegfried Herzog on the board per third-party registry data | **High** |
| Auditor / attestor | **AREVA General Auditing and Trust Company Ltd**, Vaduz (Reg. FL-0001.076.904-3) | **High** |
| Custodian | **Philoro Edelmetallhandel AG, Eschen** (as of 31 Dec 2025). **Changed from OZL Offenes Zollfreilager** during 2024–25 | **High** |

---

## 1. What it is

VNX Gold is a gram-denominated gold token issued by a small Liechtenstein operator under the world's first purpose-built token statute. Each VNXAU is asserted to be one gram of LBMA-standard gold held in a Liechtenstein vault.

It is the smallest protocol in this landscape by an order of magnitude: **13.1 kg of gold**, roughly $1.7M of genuinely attested metal. For scale, that is about one and a half London Good Delivery bars. Tether Gold and PAX Gold each hold over $1.7bn.

The reason it is worth a full profile despite its size is that it is the **best-documented protocol in the set**. VNX publishes signed ISRS 4400 reserve reports, a named custodian, a real smart-contract audit, and terms of business that spell out the ownership construct in unusual detail. That documentation is what makes it useful: it shows precisely where a well-intentioned, properly registered gold token still leaves the holder exposed, and it does so in the issuer's own words rather than ours.

It is also, as of this month, a protocol in visible retreat. See §11.

## 2. Legal structure

This is the most valuable section of this profile, because VNX has written down what most issuers leave vague, and what it has written down is **internally inconsistent**.

**What the marketing says.** VNX Gold "represents ownership in specified physical gold bars purchased and stored in a highly secured professional vault," and "VNX Gold token holder is the only lawful owner of the underlying gold" ([reserve report notes](https://vnx.li/wp-content/uploads/2026/03/VNX_Examination_on_Management_Assertions_VNXAU_31_12_2025_signiert.pdf), Note 1). The website adds that each bar is "stamped by its own serial number and linked to VNX Gold tokens" ([vnx.li/gold](https://vnx.li/gold/)).

**What the terms of business say.** The FRT Terms and Conditions state the opposite:

> "VNX Gold generated by VNX represents **co-ownership in physical gold. One VNX Gold corresponds to 1/1000 co-ownership in a gold bar of 1 kilogram**, which corresponds to 1 gram."
> ([VNX FRT Terms](http://vnx-terms.s3.amazonaws.com/VNX-FRT-Terms.pdf), s.2)

**These are different legal animals.** "Specified bars with serial numbers linked to your tokens" is allocated, individuated title. "1/1000 co-ownership of a 1 kg bar" is an undivided fractional interest in a pool. A holder cannot point to a bar; they hold a fraction alongside 999 strangers. The reserve report itself uses the pooled framing throughout, calling the holding a **"Collective Token Holders Commodity Deposit."** Confidence: **High** that the terms, not the marketing, govern.

**Who holds title.** VNX Commodities AG holds the gold at the custodian **"as the vicarious owner, registrar and depository for the VNXAU-token holders."** The custody account at Philoro is in **VNX's name** (customer number 2001517), not in holders' names. So the chain of title runs: Philoro holds for VNX; VNX holds as fiduciary for holders.

**What actually evidences your claim.** Not the token. AREVA states plainly:

> "This report does not express an opinion about the accuracy and completeness of **the register of the single token holders which VNX Commodities AG is keeping and which is deemed to be the basis to assert a property right**."

Read that carefully. The **basis of the property right is VNX's own internal register**, not the blockchain and not the auditor's work. The auditor expressly declines to verify it. A holder's legal claim therefore rests on a private database the attestor refuses to opine on. This is the single sharpest disclosure in the whole landscape.

**Insolvency.** VNX asserts bankruptcy remoteness:

> "The Collective Token Holders Commodity Deposit does not form part of the assets of VNX Commodities AG and ... ownership rights ... remain intact irrelevant of an eventual liquidation, dissolution or insolvency of VNX Commodities AG."

That is a real and well-drafted structure, and it is better than most competitors offer. But note two things. First, it is **management's assertion in a section explicitly headed "No Assurance Provided by the Independent Auditor on These Notes."** Second, AREVA's own 2023 report said of the *fiat* reserves that segregation in bankruptcy is **"a legally not defined case, due to the lack of court rulings in Liechtenstein."** The gold deposit is structured more robustly than the fiat reserve, but the same untested-jurisdiction caveat hangs over both: no Liechtenstein court has ruled on it.

## 3. Regulatory and compliance posture

**Verified against the FMA register.** I queried the Liechtenstein FMA register API directly (`register.fma-li.li`, backend `ws-api.llv.li/fire-wsapi`). One entity matches: **VNX Commodities AG, CRM 310339, reg. FL-0002.654.271-8**. Six grants, all under the TVTG, **all of type "Registration" and none of type "Licence"**:

| Role | Type | Registered | Status |
|---|---|---|---|
| Token Generator | Registration | 18 Oct 2021 | **Active** |
| TT Identity Service Provider | Registration | 18 Oct 2021 | **Active** |
| TT Depositary | Registration | 1 Feb 2024 | **Active** |
| TT Token Depositary | Registration | 18 Oct 2021 | Expired 31 Jan 2024 (merged into TT Depositary by LGBl. 2024 No. 42) |
| TT Key Depositary | Registration | 18 Oct 2021 | Expired 31 Jan 2024 (merged into TT Depositary) |
| **TT Exchange Service Provider** | Registration | 18 Oct 2021 | **EXPIRED 2 JULY 2026** |

Three findings follow, and they are the reason Liechtenstein mattered for this assignment.

**(a) Registration is not authorisation, and the FMA says so.** The FMA's own guidance states the TVTG registration assessment has "both a more limited scope and a lesser depth than the licensing procedure under financial market law," and that the FMA does **not** verify the content or accuracy of token issuers' basic information, nor evaluate "token issuer legitimacy or business model viability" ([FMA](https://www.fma-li.li/en/media-public/client-protection/safeguarding-client-protection-in-different-sectors/tt-service-providers)). TVTG registration is a fitness-and-technical-suitability gate on the *service provider*, not a product approval and not prudential supervision. Any protocol citing "regulated in Liechtenstein" as a proxy for investor protection is overstating what the regime delivers.

**(b) VNX is not registered as a Token Issuer.** The TVTG register carries distinct categories for **Token Issuer (Art. 12(1))** and **Token Issuer (Art. 12(2))**. VNX holds **neither**. It holds *Token Generator*, which is the technical role of creating tokens on a TT system, not the issuance role that attracts the basic-information/prospectus-style duties. VNX's own documentation lists its five roles and Token Issuer is absent from that list too. Whether VNX ought to hold one is a legal question outside our scope, but the gap is a matter of public record and is not something the marketing surfaces.

**(c) The exchange registration lapsed 26 days ago, under MiCAR.** The register annotates the expiry: *"Expired pursuant to Section II, paragraph 2 of LGBl. No. 2025.113 (MiCAR transitional period)."* Liechtenstein is EEA, so MiCAR displaced the TVTG exchange role and the grandfathering window closed on 2 July 2026. **I found no MiCAR/CASP authorisation for VNX in any register.** VNX's response was not to obtain one but to **shut the exchange down** (§11). This is a live worked example of a purpose-built national token law being overridden by EU-level regulation, and of a small issuer choosing exit over re-licensing.

Also holds a business (trade) licence from the Liechtenstein Office of National Economy. Bermuda: **VNX Global Ltd.** holds a Class M digital asset licence under the Bermuda DABA 2018, granted 12 May 2026. Note the Bermuda notice is careful to call it "a VNX Group entity" and says **nothing** about VNX Commodities AG or the gold. Confidence **High** that Bermuda covers the group's fiat/stablecoin and flow business, **Low/not disclosed** that it covers VNXAU.

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian (current) | **Philoro Edelmetallhandel AG, 9492 Eschen, Liechtenstein**, account no. 2001517 | **High** |
| Custodian (prior) | **OZL Offenes Zollfreilager in Liechtenstein AG**, client no. 1708, per the 31 Dec 2023 report | **High** |
| Custodian change | Unannounced. Surfaced only by comparing the 2023 and 2025 reports | **High** |
| Vault / city | Eschen, Liechtenstein | **High** |
| Allocated? | **Pooled co-ownership** (1/1000 of a 1 kg bar), held in VNX's name. Marketed as segregated/allocated | **High** |
| Bar list | **Not disclosed.** No serial-numbered bar list is published despite the "each bar stamped by its own serial number" claim | **High** |
| PoR feed | **None.** No live oracle, no dashboard | **High** |
| Reserve attestation | **Annual, ISRS 4400 agreed-upon procedures**, by AREVA. Latest 31 Dec 2025, signed 23 Mar 2026 | **High** |
| Smart contract audit | **University of Luxembourg SnT/SEDAN, v1.0.2, 26 Oct 2021** | **High** |
| Insurance | "Full insurance" claimed; insurer and policy **not disclosed** | **Medium** |

**The attestation is real but is weaker than the word "audit" implies, and VNX's own auditor says so.** AREVA states: *"This Agreed-Upon Procedures engagement is not a reasonable or limited assurance engagement. Accordingly, we do not express an opinion or an assurance conclusion."* It further discloses that it is **"not required to be independent for the purpose of this engagement"** and that it is also VNX's financial-statement auditor. And the procedures did **not include physically observing the gold**:

> "while we did obtain confirmation of gold balances from the third-party custodian(s) Philoro, our procedures did not include **the observation of gold held by these custodian(s)** and did not include **any validation of the quality of gold**."

So: an annual reconciliation of on-chain supply against a custodian's paper statement, by a non-independent firm, with no bar inspection and no assay. That is meaningfully more than most competitors publish, and it is still not what a retail reader hears in the word "audited."

**The distinction the brief asks us to draw sharply.** The 2021 SnT audit is a **smart-contract security review**, entirely unrelated to whether gold exists. It found 1 major and 68 minor issues; by v1.0.2, the major issue (DGR contract exceeding the 24,576-byte limit) was fixed, but **19 minor issues remained unfixed**, mostly naming-convention items. It is genuine academic work. It is also **five years old**, predates the Base/Solana/Q deployments entirely, and is published under a March 2026 URL on the transparency page, where a skimming reader would reasonably assume it is current. Note the audit covers contracts named "DGR" (Digital Gold Receipt) which the report says was **renamed to "Commodity Token"** in Oct 2021.

**A real discrepancy in the 2025 attestation.** AREVA found a **1.13 token mismatch** on Solana (6,449.13 asserted vs 6,448.00 on-chain), explained as holders burning tokens directly from wallets. Small, honestly disclosed, and it means on-chain supply can drift **below** issued supply. Worth noting that this makes the gold slightly over-collateralised, not under.

## 5. Issuance

Retail buys on the VNX Platform (invest.vnx.li) with EUR or BTC/ETH/USDC; VNX then buys physical gold from professional dealers. **No minimum purchase**, fractional grams supported: the one genuinely retail-friendly feature in the design. Generation fee "starting from 0.1%."

For the fiat-referenced tokens, institutional mint/redeem is **verified customers only with a CHF/GBP 100,000 minimum** ([GitBook](https://vnx.gitbook.io/vnx-global/institutional/products/minting-and-redemption)). No equivalent institutional gold facility is documented.

On-chain, minting is `increaseSupply` restricted to a **SupplyController role**; burning is `decreaseSupply`. Both are role-gated, not open.

## 6. Redemption

Three exits, per VNX's own notes:

1. **Physical gold**: collect at the Liechtenstein vault or request delivery to an address, **minimum 1 kg**, at the holder's "own expense and risk."
2. **Cash**: instruct VNX to sell and receive fiat or crypto.
3. **Sell on a third-party exchange** "(subject to availability)."

Conditional in all cases on registration, identification and AML clearance on the VNX Platform.

**The 1 kg minimum is the substantive gate, and it is severe.** At ~$129/gram that is **~$129,000 of gold** to exercise physical redemption. A holder of 1,000 VNXAU (~$130,000) is right at the threshold. VNX's entire attested reserve is 13.1 kg, so **the whole protocol supports at most 13 simultaneous physical redemptions**. The "collect your gold from the vault or have it delivered anywhere in the world" pitch on the homepage is, for essentially every retail holder, unreachable. This is the same shape of gap as Aurumix's, but concealed by a threshold rather than stated openly.

**Route 1 and route 2 both now require the platform, and route 3 just narrowed.** Since exchange operations closed on 30 June 2026 (§11), the sell-to-VNX path is impaired. Withdrawals to whitelisted wallets and banks were open only **until 31 July 2026, 18:00 CET: three days from today.** Any holder who misses that window is left with route 3 on a market doing ~$36k/day.

## 7. Fees and revenue model

| Fee line | Amount | Source |
|---|---|---|
| Generation / issuance | "Starting from **0.1%**" | [vnx.li/gold](https://vnx.li/gold/) |
| **Ongoing storage / custody** | **0% ("zero storage fees")** | [vnx.li/gold](https://vnx.li/gold/) |
| Platform exchange fee | **0.3%** base, **0.2%** >EUR 100k/12m, **0.1%** >EUR 1M/12m | FRT Terms Annex I |
| Crypto withdrawal | EUR 3 (ETH), EUR 0.5 (Base), EUR 1.5 (other chains) | FRT Terms Annex I |
| Fiat withdrawal | EUR 10 SEPA; EUR/CHF 30 SWIFT; GBP 40 SWIFT | FRT Terms Annex I |
| Card top-up | **2.5%**, min EUR 10 | FRT Terms Annex I |
| **Inactivity fee** | **EUR 10/month on dormant accounts**, until balance reaches zero | FRT Terms Annex I |
| Physical delivery | Holder's "own expense and risk", not quantified | Reserve report Note 1 |
| On-chain transfer fee | Contract **supports** `setFeeRate`/`setFeeRecipient`; **currently not observed as charged** | SnT audit + on-chain |

**Correction to a widely repeated error.** Several aggregators report VNX's storage cost as "0.18–2% per annum" or "0.25–1% per annum." Those are the **competitor columns** in VNX's own comparison table (ETFs/ETCs and metal accounts respectively). VNX's column reads "Effective costs: starting from 0.1% for generation." One of my own Perplexity passes made exactly this mistake before I read the page directly. Anyone citing a VNX annual storage fee is misreading the marketing table.

**What funds zero storage.** VNX does not say. Not disclosed. But the arithmetic is instructive for Aurumix. Vaulting and insuring 13.1 kg at a commercial rate of roughly 0.3–0.5%/yr costs on the order of **$3,000–6,000 a year** against ~$1.7M of metal. That is a rounding error, comfortably absorbed by generation fees, exchange fees, card fees and the inactivity fee, and by the far larger stablecoin business the gold token sits beside. **Zero storage fees are affordable here precisely because the gold book is tiny and is a loss-leader for something else.** That does not scale: at $500M of gold the same promise costs $1.5–2.5M/yr and must come from somewhere real.

Note the **EUR 10/month inactivity fee** is the quiet counterweight. A dormant retail holder is drained to zero over time. It is a storage fee in all but name, charged only to the disengaged, and it is the closest thing in this landscape to a cash-denominated custody charge that does not touch the gram peg.

## 8. Token architecture

**Not a plain ERC-20, despite being labelled one everywhere including by VNX.** I read the Ethereum contract directly on-chain and cross-checked against the SnT audit. Findings:

- **Upgradeable proxy.** EIP-1967 transparent proxy. Implementation `0x1c17d67706423735b8bbf5b234d63b872bd584c4`; proxy admin slot resolves to `0xc8bb...0400`. The logic can be replaced.
- **Every transfer is gated by an external Transfer Provider.** The bytecode carries the revert string **`Declined by TP!`**. The audit confirms a pluggable `ITransferProvider` with three implementations: `AnyTransferProvider` (permissive), `WhitelistTransferProvider` (**whitelist gating**), and `AdminTransferProvider`. `changeTransferProvider` can swap which one is live. **VNX can convert VNXAU from open to whitelist-only transfer without redeploying.**
- **Freeze and seize.** `freeze(address)`, `unfreeze(address)`, and **`reclaimTokensFromFrozenAddress(address)`**, gated by an **AssetProtectionRole**. That last function is confiscation: an admin can move tokens out of a frozen wallet. The T&Cs match: VNX "may freeze such FRT ... and you may forfeit any rights."
- **Pausable.** `pause()`/`unpause()`, guarded by `Only AP!`. Currently `paused() == false`.
- **Built-in transfer fee.** `setFeeRate`, `setFeeRecipient`, `getFeeFor`, with a `Fee rate>100%` bound check. Dormant, but present.
- **RBAC.** A separate `Manager` contract with runtime-configurable roles: SupplyController, AssetProtection, and admin roles (`Only Admin role`, `Only SC!`, `Only AP!`).
- **ERC20Permit** (EIP-2612 gasless approvals), and 18 decimals on EVM chains, **9 on Solana**.

**The relevance to Aurumix's question 3 is direct.** VNX shows there is a **third option** between a plain ERC-20 and full ERC-3643. It is a standard-looking ERC-20 with a **swappable compliance hook** on every transfer. Wallets, explorers and DEXs treat it as vanilla; the issuer retains whitelist, freeze, seize, pause and fee powers, and can tighten them by changing one address. It gets ERC-20 composability today with ERC-3643-grade control in reserve.

That is architecturally clever and it is also the honesty problem. **Nothing in VNX's public-facing material discloses these powers.** The reserve report says VNX Gold tokens "are freely transferrable." They are freely transferable *until the Transfer Provider is switched*. A holder reading the marketing would not know that seize and whitelist functions exist. Only the 2021 audit PDF and the bytecode reveal them.

## 9. Liquidity and market

Measured 28 July 2026:

| Metric | Value |
|---|---|
| Price | **$130.04** |
| Market cap (CoinGecko) | **$5.73M** |
| 24h volume | **~$36,000** |
| Holders | ~2,440 ([rwa.xyz](https://app.rwa.xyz/assets/VNXAU)) |
| Venues | XT.COM (CEX), Raydium, Orca, Aerodrome (DEX) |
| Attested gold (31 Dec 2025) | **13.1 kg** |
| Live EVM supply (on-chain, today) | ETH 582.67 + Base 1,846.90 + Polygon 107.74 = **2,537.31** |

**A supply figure that does not reconcile, and it matters.** CoinGecko reports 44,100 tokens circulating; rwa.xyz reports 12,886 across four chains and **$1.69M** AUM. The audited figure at 31 Dec 2025 was **13,100**. The $5.73M market cap implies ~44,400 grams, i.e. **~44 kg, versus 13.1 kg attested**. rwa.xyz's number is the one consistent with the attestation and with my own on-chain reads.

I am not alleging under-collateralisation: the plain reading is that **CoinGecko is triple-counting a multichain token**, and VNX publishes no consolidated supply dashboard to correct it. But note the consequence: **the headline market cap that every aggregator, and any casual analyst, will quote for VNXAU is roughly 3.4x the gold that its own auditor confirmed exists.** For a protocol whose entire pitch is verifiable backing, the absence of a live supply feed is a self-inflicted wound. Confidence **High** on the attested 13.1 kg; **Low** on any aggregator market cap.

**On the premium thesis (Aurumix question 6), this is decisive evidence against.** Spot via XAUT/PAXG is ~$129.11–129.22/gram. VNXAU trades at $130.04: a **premium of ~0.7%**, not 3–8%. And it is thinly traded enough that the print is nearly meaningless: **$36k/day against $5.7M cap is ~159 days to turn over the float**, versus ~17 days for PAXG. A single $10k order moves this book.

So the pattern the brief established with PGOLD repeats with a *better-run, better-documented, fully registered* issuer: **regulatory quality does not produce a premium.** VNX has a named custodian, a signed annual attestation, a real audit and a purpose-built legal regime, and the market pays it 0.7% over a Cayman-issued competitor. The premium thesis does not survive contact with either data point.

## 10. Distribution

- **No savings plan.** No SIP, no recurring purchase, no DCA product. Not disclosed anywhere.
- **No referral or affiliate programme.** Not found on vnx.li, the docs or the FAQ.
- **No agent network.** Distribution is direct platform plus exchange listings plus B2B integrations.
- **Geography**: EEA-centric, "supported jurisdictions shown during registration." Liechtenstein law, exclusive Liechtenstein jurisdiction, and the terms explicitly note **FRT is not covered by deposit insurance**.
- **B2B white-label is the real channel.** VNX supplied the gold rails for **BlocPal's BPG1** token (26 Nov 2025), backed one ounce per token. VNX's growth motion is infrastructure-for-others, not retail acquisition.
- **VNXLU / VNX Token**: a utility token usable to pay platform fees at a floor of EUR 0.25. A "VNX Community Hub" governance/utility token was announced 26 Mar 2025. Current status **not disclosed**. No revenue share or yield found.

**This confirms the brief's expectation.** Another gold protocol with no recurring-contribution mechanism and no commission network. Across this landscape, the savings-plan-plus-agent-network model remains genuinely unoccupied.

## 11. Recent developments

Reverse chronological. Dated from primary sources.

- **28 July 2026 (today)**: **three days remain** before the 31 July withdrawal deadline for VNX Platform balances.
- **2 July 2026**: **TT Exchange Service Provider registration EXPIRED** on the FMA register, annotated to the MiCAR transitional period under LGBl. 2025 No. 113. ([FMA register](https://register.fma-li.li/))
- **30 June 2026, 18:00 CET**: **Exchange operations on the VNX Platform suspended.** Bridging services ceased. Token withdrawals restricted to the chain the tokens already sit on. Withdrawals to whitelisted wallets/banks permitted only until **31 July 2026, 18:00 CET**. ([notice](https://vnx.li/important-notice-upcoming-suspension-of-exchange-operations-on-the-vnx-platform/))
- **12 May 2026**: **VNX Global Ltd. obtains a Bermuda DABA 2018 digital asset licence** (Class M). Framed as improving "fiat-to-digital asset flows" and "liquidity infrastructure." Silent on VNX Commodities AG and on the gold. ([notice](https://vnx.li/vnx-notes-bermuda-licence-obtained-by-group-entity/))
- **11 May 2026**: **Chain consolidation.** Retained: Ethereum, Solana, Stellar, ICP, Base, Celo, Etherlink/Tezos, Q (VNXAU). **Discontinued: Polygon, Avalanche, Arbitrum, XRPL, Fraxtal, Concordium.** Holders told to swap out by 31 May. ([notice](https://vnx.li/strategic-focus-on-supported-blockchains/))
- **22 April 2026**: VNX Commodities AG announces discontinuation of exchange activities for certain assets.
- **23 March 2026**: AREVA signs the **31 Dec 2025 gold reserve report**: 13,100 g, custodian now **Philoro**, a 1.13-token Solana discrepancy disclosed.
- **26 November 2025**: **BlocPal partnership**, gold-backed BPG1 token, one ounce per token.
- **21 August 2025**: VEUR/VCHF/VGBP live on Base.
- **11 July 2025**: **VNXAU live on Base**, marketed as the first gold-backed token on Base.
- **20 May 2025**: VEUR/VCHF/VGBP on Concordium (chain since discontinued).
- **26 March 2025**: VNX Community Hub launches a governance/utility token.
- **31 Dec 2023 → 31 Dec 2025**: gold under custody **fell from 15,100 g to 13,100 g (-13%)** and the custodian **changed from OZL to Philoro**, neither announced.

**The shape of this timeline is the story.** A protocol that shrank its gold book, silently changed custodian, cut six chains, let its exchange registration lapse rather than seek MiCAR authorisation, shut its exchange, and moved its licensing centre of gravity to Bermuda. This is not a wind-down of the token: VNXAU still exists, is still attested, and the gold is still there. But it is an **orderly retreat of the Liechtenstein retail venue**, and the flagship product's own distribution channel just closed.

## 12. Relevance to Aurumix

**On Q1, custody fee mechanism.** VNX charges **zero ongoing custody fee and deducts nothing in grams**, so its 1 token = 1 gram peg holds exactly: the attestation reconciles 13,100 tokens to 13,100 grams, cleanly. This is a working proof that the "charge nothing, recover elsewhere" option preserves the peg. But look at what funds it: a ~$1.7M gold book whose real vaulting cost is a few thousand dollars a year, cross-subsidised by a stablecoin business and by transaction fees. **Aurumix cannot copy this.** At scale the promise costs real money. What Aurumix *should* copy is the **EUR 10/month inactivity fee**: a cash-denominated charge that falls only on dormant accounts, never touches the gram balance, and quietly solves the cost of carrying disengaged holders. That is a clean answer to the peg problem and it is sitting in VNX's fee annex.

**On Q2, dividend funding.** VNX pays **nothing**: no yield, no APY, no staking, and no disclosure that the gold is leased. It is a pure custody-and-title product. This is the **cleanest counter-example in the landscape to PGOLD and ORO**. It demonstrates that a compliant, registered gold token with real attestations does not offer yield, and the reason is visible in its own documents: the gold is asserted to sit **outside VNX's balance sheet** in a segregated collective deposit. You cannot simultaneously claim bankruptcy-remote segregation and generate return from the metal. **Encumbering the gold and claiming it is ring-fenced are mutually exclusive.** If Aurumix wants both the ICS Dividend and a credible "your gold is safe if we fail" story, it must fund the dividend from something that is not the gold, and say so explicitly.

**On Q3, token standard.** The most transferable finding in this profile. VNX runs a **standard-looking ERC-20 with a swappable transfer-provider hook**, plus freeze, seize, pause, fee and upgrade powers. It gets DEX and wallet composability while retaining the ability to whitelist by changing one address. For Aurumix, whose ICS standing, dividend entitlement and credit eligibility all break on an anonymous DEX transfer, this is a genuine **middle path between ERC-20 and ERC-3643**, and cheaper to build than full ERC-3643. Two cautions. First, it is discretionary control dressed as an open token, and VNX **does not disclose it**; if Aurumix takes this route it should document the admin powers openly, because the gap between "freely transferrable" and `reclaimTokensFromFrozenAddress` is exactly the kind of thing that destroys trust when discovered. Second, a hook that gates transfers does not by itself carry ICS state; Aurumix still needs the registry.

**On Q4, regulatory route.** This is the assignment's central lesson and it cuts against the intuition that a purpose-built token law is the easy answer. Liechtenstein's TVTG is the most bespoke token statute in existence, and VNX holds six registrations under it. Yet: (i) **registration is not a licence**, and the FMA explicitly does not vet the product or the business model; (ii) VNX holds **no Token Issuer registration** despite issuing tokens; and (iii) the TVTG exchange role was **overridden by MiCAR and expired on 2 July 2026**, and VNX responded by **closing the exchange rather than seeking MiCAR authorisation**. A bespoke national regime bought VNX five years of legitimacy and then evaporated under supranational law. **Read across to VARA:** the temptation to find a cheaper, more accommodating regime than VARA's ~AED 100k + 200k/yr + AED 1.5M capital is real, but VNX shows the failure mode. Cheap registration regimes are cheap because they supervise less, and they are vulnerable to being superseded. Aurumix should also note the **dual-entity hedge**: VNX kept the regulated issuer in Liechtenstein and put the new licence in a second Bermuda entity. That is a legitimate structural answer to the hybrid-regulation problem the brief flags, and worth modelling.

**On Q5, redemption.** VNX offers physical redemption and Aurumix does not, but the honest comparison is closer than it looks. VNX's **1 kg minimum (~$129,000)** puts physical delivery out of reach of every retail holder, and its entire reserve would satisfy 13 such requests. The brief warned to watch for eligibility limited to undefined "qualified holders"; VNX's gate is not vague wording but a hard weight threshold, which is arguably more honest and equally exclusionary. **The read-across: Aurumix's no-physical-redemption stance is more defensible than it feels, provided it is stated plainly.** A stated "cash buyback only" is better than an advertised physical redemption that 99% of holders cannot use. Aurumix's real exposure is the "you own physical gold" pitch, not the absence of delivery. Say cash-only, prominently, and the gap closes.

**On Q6, premium and liquidity.** **VNXAU trades at ~0.7% over spot on ~$36k/day.** A fully registered, independently attested, named-custodian gold token with a five-year track record commands essentially no premium and has a market that turns over its float once every ~159 days. Combined with PGOLD's sub-$20/day, this is now two independent data points. **The 3–8% exchange premium thesis has no support anywhere in this landscape.** Aurumix should not model demand on it. If a premium is required for the economics to work, the economics need rework, not the marketing.

**On Q7, proof of reserve.** VNX is the **benchmark for what "good" looks like at this size, and it is still not enough.** It publishes named-custodian annual ISRS 4400 attestations signed by a real firm. And yet: the auditor is **not independent** (it is also the statutory auditor) and says so; the procedures **exclude physically observing the gold** and exclude assay; there is **no bar list** despite the serial-number claim; there is **no live PoR feed**; the reporting is **annual with a three-month lag**; and the auditor **expressly declines to opine on the holder register that is the actual basis of the property right**. Meanwhile a **five-year-old smart-contract audit** sits on the same transparency page under a 2026 URL. If Aurumix wants genuine differentiation, the bar to clear is low and specific: **publish a bar list, use an attestor that is not your statutory auditor, report quarterly or better, and never let a contract audit and a reserve attestation share a page without labelling which is which.**

**On Q8, distribution.** No savings plan, no referral, no affiliate, no agent network. VNX grows through **B2B white-label** (BlocPal) instead. Confirms the pattern: the recurring-contribution retail channel is empty across this entire landscape, and it remains Aurumix's clearest structural advantage.

**On Q9, wind-down.** VNX has published **no wind-down plan**, consistent with every other protocol reviewed. But it has done something no failed predecessor did: it has **executed a partial, orderly, publicly-noticed retreat**, with dated notices, a 30-day withdrawal window, and explicit instructions. That is a *de facto* wind-down playbook for a venue closure, and it is worth studying as a template even though it was never committed to ex ante. It also exposes the weakness of not committing in advance: the withdrawal window is **31 days**, announced **11 days** before the exchange closed, and any holder who was travelling, ill or simply inattentive is now stuck with an illiquid token and no issuer venue. **Aurumix committing ex ante to a defined wind-down window (say 180 days) is cheap, differentiating, and directly answerable to what just happened here.**

**The single most useful finding.** VNX's auditor states that the basis of a holder's property right is **VNX's own internal register of token holders, and then expressly refuses to opine on it**. Meanwhile the terms say holders get **1/1000 co-ownership of a kilo bar**, while the marketing says they own **specified serial-numbered bars**. Aurumix is building a product whose entire promise is "you own physical gold," sold to retail savers through agents. **The token is not the title. The register is the title.** Whatever Aurumix builds, the holder register must be the audited artefact, its integrity must be independently verified, and the ownership construct in the terms must match the words on the landing page. VNX is the best-documented operator in this landscape and it still fails that test in its own paperwork.

## 13. Open items for verification

- [ ] Confirm whether **any MiCAR/CASP authorisation** has been granted to VNX Commodities AG or VNX Global Ltd in any EEA state; check ESMA's central CASP register, not just the Liechtenstein FMA.
- [ ] Establish whether VNX intends to **re-register the TT Exchange role** or has exited EEA exchange activity permanently.
- [ ] Verify the **Bermuda Class M licence** for VNX Global Ltd directly on the BMA register, and establish whether its scope covers VNXAU or only fiat-referenced tokens and flow business.
- [ ] Determine why **gold under custody fell from 15,100 g to 13,100 g** between Dec 2023 and Dec 2025: net redemptions, or migration losses during the custodian change.
- [ ] Establish **when and why custody moved from OZL to Philoro**, and whether holders were notified at the time.
- [ ] Reconcile the **13,100 attested vs 44,100 CoinGecko vs 12,886 rwa.xyz** supply figures; confirm the aggregator triple-count hypothesis with VNX or via a full multichain sweep including Q, Solana, Etherlink and Tezos.
- [ ] Obtain the **Commodity Token Terms and Conditions** (the master agreement; only the FRT annex was retrievable) and confirm the gold redemption fee schedule and the physical delivery cost basis.
- [ ] Confirm whether **`WhitelistTransferProvider` is currently the live transfer provider** on any chain by reading `transferProvider()` on each deployment.
- [ ] Identify the holders of the **SupplyController, AssetProtection and ProxyAdmin** roles and whether any multisig or timelock governs contract upgrades.
- [ ] Confirm whether a **31 Dec 2026 interim or quarterly attestation** is planned, or whether annual remains the cadence.
- [ ] Check the status of **VNXLU and the VNX Community Hub token** after the platform exchange closure, since VNXLU's stated use was paying platform fees.
- [ ] Determine what happened to holders who **missed the 31 July 2026 withdrawal deadline**, and what recourse VNX offers. This is the live wind-down lesson.
- [ ] Verify the **insurance policy and insurer** for the Philoro-vaulted gold; currently an unevidenced marketing claim.

---

# Midas Labs / GoldZip (XGZ)

> **Scope correction, read this first.** This profile was commissioned as "Midas mXGZ / XGZ (Midas, the tokenized-yield issuer)" on the premise that Midas issues a yield-bearing gold product under a European issuer-SPV note programme. **That premise is wrong on three counts, and the corrections are the most valuable output of this profile.** See §0.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | **XGZ** ("GoldZip", on-chain token name "GoldZip Gold") | High (on-chain) |
| Does "mXGZ" exist? | **No. Not found anywhere**: not on the issuer's docs, HKGX, CoinGecko, CoinMarketCap, rwa.xyz, or any exchange | High (negative search) |
| Issuer (marketing) | "GoldZip", a subsidiary of the Hong Kong Gold Exchange (HKGX). HKGX names **GoldZip Pte. Ltd.**; the token's own site and CoinMarketCap name **GoldZip Digital Pte. Ltd.** The two conflict | High (that they conflict) |
| Issuer (registry) | **GoldZip Pte. Ltd., UEN 202119587H** and **GoldZip Digital Pte. Ltd., UEN 202119588Z**, both incorporated **3 June 2021**, Singapore. ACRA principal activity for both: **development of software and applications (except games and cybersecurity)** | High (ACRA) |
| Domicile | **Singapore** (issuer). Gold and vaults in **Hong Kong**. Parent HKGX is Hong Kong | High |
| Backing claim | 1 XGZ = 1 gram of 99.99% fine gold in "HKGX recognised" vaults | Medium (issuer assertion) |
| Chains | Ethereum only | High (on-chain) |
| Contract address | `0x69af64f409c08E9076bF7f3ed9Db3a7409717161`, 8 decimals | High (on-chain) |
| Supply | **39,000 XGZ = 39.0 kg gold** | High (Ethplorer, 28 Jul 2026) |
| Market cap / TVL | **~$5.06M** at $129.68/token | High |
| 24h volume | **~$113k**, of which **92.4% is a single MEXC XGZ/USDT pair**. Uniswap V4 pairs combined: **under $320/day** | High (CoinGecko) |
| Holders | **264** | High (on-chain) |
| Price vs spot | **$129.68 vs ~$131.50/g spot: a ~1.4% DISCOUNT** | High |
| Regulatory status | **No financial-services licence anywhere.** Claimed status is a Singapore MinLaw **PSPM Act dealer registration**, which is an AML/CFT registration, not a licence to issue investment products. No MAS licence found | High |
| Subscription fee | Not disclosed | Not disclosed |
| Ongoing custody fee | **Not disclosed**, and who pays vault cost is **not disclosed** | Not disclosed |
| Transfer fee | **0.01% of transaction amount, paid by sender**, levied on-chain | High (issuer docs) |
| Redemption fee | "Standard settlement timelines and **handling fees apply**": amount **not disclosed** | High (that it is undisclosed) |
| Advertised yield | **None. XGZ pays no yield of any kind** | High |
| Named officers | **Barry Ip**, Director / Head of Digital Innovation, HKGX. **Juha Viitala**, SEO of Universal Digital (MoU counterparty) | High |

---

## 0. Three corrections to the task premise

**Correction 1: there are two unrelated companies called "Midas", and this profile is about the smaller one.**

- **Midas / midas.app** is a Berlin RWA tokenization platform issuing mTBILL, mBASIS, mBTC and mXRP through **Midas Software GmbH** (Germany, created 30 June 2023, Kurfürstendamm 15, Berlin), a subsidiary of **Midas Protocol Limited, UK Companies House number 15217097**, incorporated 17 October 2023 ([readi.fi issuer profile](https://readi.fi/issuer/tokenized-real-world-assets-issuer-midas/), [Companies House](https://find-and-update.company-information.service.gov.uk/search?q=Midas+Protocol+Limited)). This is the entity the task description actually describes: European issuer SPV, prospectus-based note programme.
- **Midas Labs** (midaslabs.xyz) is GoldZip's **Web3 development contractor**. It is not an issuer of anything ([PR Newswire via Manila Times](https://www.manilatimes.net/2026/07/02/tmt-newswire/pr-newswire/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/2377222)).
- **No source establishes any corporate relationship between them.** Sonar Pro, searching UK Companies House and public profiles, returned "not found" for any ownership, subsidiary or common-parent link and concluded they are separate, unrelated entities. Midas Labs' own jurisdiction and registration number are **not found in any register**: a notable gap for a company being named as strategic infrastructure partner to a 115-year-old exchange.

**Correction 2: the Midas that does have the European prospectus wrapper issues no gold product at all.**

Midas Software GmbH's disclosed product suite is US Treasuries (mTBILL), a crypto basis trade (mBASIS), mBTC and mXRP, with stated future expansion into corporate bonds and structured credit. **No gold-backed or gold-linked token, confirmed explicitly** ([readi.fi](https://readi.fi/issuer/tokenized-real-world-assets-issuer-midas/), [rwa.xyz platform page](https://app.rwa.xyz/platforms/midas)). So the specific thing the task asked for, a Midas gold product under a note programme, **does not exist**.

**Correction 3: "mXGZ" does not exist.** Two independent Sonar Pro sweeps plus direct searches of the issuer GitBook, HKGX, CoinGecko, CoinMarketCap, rwa.xyz, Etherscan and exchange listings return **no token, product or ticker called mXGZ**. The real token is plain **XGZ**, and it is a non-yielding 1g gold token. The "m" prefix belongs to the other Midas's naming convention (mTBILL, mBASIS, mXRP), which is almost certainly how the two got conflated.

**Net effect for Aurumix: the yield-bearing-gold-under-a-prospectus precedent that this profile was commissioned to find does not exist here.** That is a real finding, not a research failure. It is documented in §12.

---

## 1. What it is

XGZ is a gold-backed ERC-20 token on Ethereum. One token represents one gram of 99.99% fine gold held in vaults accredited by the Hong Kong Gold Exchange ([GoldZip GitBook](https://goldzip-1.gitbook.io/goldzip/goldzip-xgz/what-is-usdxgz)). It launched **23 December 2025** ([Decrypt](https://decrypt.co/353315/hkgx-backed-goldzip-launches-xgz-asias-first-gold-token-supported-by-a-leading-gold-exchange)).

Its distinguishing pitch is institutional parentage: HKGX (formerly the Chinese Gold & Silver Exchange Society) is Hong Kong's sole recognised gold exchange, over 100 years old, and GoldZip is marketed as "Asia's first gold token supported by a leading gold exchange." Midas Labs is the outsourced Web3 builder, named strategic partner on **19 May 2026** ([cointrust](https://www.cointrust.com/market-news/goldzip-and-midas-labs-advance-digital-gold-ecosystem)).

It is very small: **39 kg of gold, ~$5.06M, 264 holders**. That is roughly two-thirds the size of ORO by value and it has one-thirty-seventh as many holders. The distribution is institutional-shaped, not retail-shaped, which is the mirror image of ORO (9,700 holders sharing 19 kg).

---

## 2. Legal structure

**What a holder actually owns is not documented.** This is the central gap.

The GitBook, HKGX's product page, and every listing describe XGZ as "backed by" gold and give holders a **redemption right** subject to KYC/AML. None of them state whether the holder has:

- legal title to identified bars, or
- a beneficial interest under a declared trust, or
- a bailment, or
- an unsecured contractual claim against the issuer.

**No prospectus, base prospectus, terms and conditions of notes, final terms, offering memorandum or published terms of issue exists for XGZ.** Searched: the issuer's site, the GitBook (whose full page index was retrieved via `llms.txt`), HKGX's site, and rwa.xyz. **Not found in any of them.** The GoldZip website footer references "Terms & Conditions", "Rules" and "Legal Policy" pages, but no operative gold-title or insolvency provision could be retrieved from them.

**What happens to holders on issuer insolvency is Not disclosed.** There is no segregation statement, no trust account, no ranking in a winding-up, no wind-down plan.

**On "bankruptcy remote":** rwa.xyz's data sheet carries the label "Account Segregation: Bankruptcy Remote" for XGZ. **Nothing in the issuer's own documentation supports it.** There is no named trustee, no trust deed, no declaration of trust, no jurisdiction for a segregation structure. This is the identical pattern to ORO's unverifiable "ORO Foundation": a third-party data aggregator surfacing a legal conclusion that has no published instrument behind it. **Treat it as unsupported.**

Absent any of that, the defensible reading is that an XGZ holder has a **contractual redemption claim against a Singapore private limited company whose registered business activity is software development**. Confidence: Medium on that characterisation, High that no better-documented structure is published.

**Confidence: High** that no prospectus or note terms exist. **Not disclosed** on insolvency ranking.

---

## 3. Regulatory and compliance posture

**No financial-services licence in any jurisdiction.**

| Register / claim | Result |
|---|---|
| Singapore MinLaw, PSPM Act regulated dealer | **GoldZip Digital Pte. Ltd. appears on the registered dealers list.** HKGX instead attributes this registration to GoldZip **Pte. Ltd.** The two claims conflict |
| MAS Capital Markets Services licence | **Not found** |
| MAS Payment Services / DPT licence | **Not found** |
| Hong Kong SFC | **Not found**, and XGZ is explicitly **not available to Hong Kong residents** |
| rwa.xyz regulatory status field | Lists XGZ as **"Non-Regulated"** |

**The PSPM Act point is the one that matters and it is routinely misread.** Registration as a regulated dealer under Singapore's Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019 is an **AML/CFT registration administered by the Ministry of Law**, applying to jewellers, bullion traders, pawnbrokers and auction houses ([MinLaw ACD](https://acd.mlaw.gov.sg/list-of-registered-dealers/), [GoBusiness licence directory](https://licensing.gobusiness.gov.sg/licence-directory/minlaw/registration-of-precious-stones-and-precious-metals-dealers)). It is **not** a prudential licence, **not** a securities or capital-markets authorisation, and it confers **no** permission to issue an investment product, hold client assets, or offer tokens to the public.

Marketing compresses this into "regulated by the Ministry of Law (MinLaw) in Singapore" (on goldzip.info and repeated verbatim by CoinMarketCap) and, in the July 2026 MoU release, into GoldZip **"holding a full regulatory compliance license in Singapore."** That last phrasing is materially misleading: there is no such licence. **This is the same category error as Comtech's DAFZA precious-metals licence: a trade/AML registration being presented as authorisation to issue a token.**

**The registry check adds a third problem.** ACRA records the principal activity of **both** GoldZip entities as *development of software and applications (except games and cybersecurity)*. Neither carries a precious-metals or financial-services activity code. Both were incorporated **3 June 2021**, two and a half years before the token launched.

**Confidence: High.**

---

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian | **Not disclosed by the issuer.** GitBook says only "licensed gold vaults accredited by HKGX". rwa.xyz asserts **Brink's Global Services**: unconfirmed by any issuer document | Low (Brink's) / High (issuer silence) |
| Vault / city | **Not disclosed.** Implied Hong Kong via HKGX depositories; never stated | Not disclosed |
| Allocated? | **Not disclosed.** No allocation or segregation language anywhere | Not disclosed |
| Bar list | **None published.** Docs refer generically to "GoldZip Eligible Gold Bars" and "selected specified brands" | High (negative) |
| PoR feed | **None.** No Chainlink or other on-chain PoR oracle | High (negative) |
| Reserve attestation | **Promised, not delivered.** GitBook: *"Periodic attestation reports by accredited auditors."* No auditor named, no cadence, no report published, no URL | High |
| Smart contract audit | GitBook's smart-contract page **links an audit file and a GitHub commit**, but no auditor name or findings were retrievable, and no published report was found in any audit-firm index | Low |
| Insurance | Claimed as "insured vaults" in secondary coverage only. No insurer, policy or limit disclosed | Low |

**Applying the brief's rule on conflating the two audit types:** GoldZip is on the correct side of the wording but the wrong side of substance. It uses the precise phrase "attestation reports by accredited auditors" (correctly reserve language) **but has published none**. Meanwhile the only artefact that appears to exist is a smart-contract audit file. **So the one thing plausibly audited is the code, and the 39 kg of gold has no published attestation at all.** For a token whose entire proposition is exchange-grade custodial credibility, that is the single largest evidentiary hole in the product.

---

## 5. Issuance

Minting is **not open**. rwa.xyz states that **only HKGX members, all KYB-verified, can mint XGZ** by depositing physical gold into the vault. The GitBook describes a three-step process: accept gold from trusted refineries meeting specification, conduct international assay verification of fineness, then issue XGZ on-chain for distribution through exchanges and distributors.

Eligible metal is tightly specified: **minimum 1 kilogram bars of 999.9 fine gold** from selected brands. Minimum mint size and mint fees: **Not disclosed**.

This is a **wholesale, members-only primary market**. Retail participation exists only on the secondary market (MEXC, Uniswap). The practical consequence for the peg is in §9.

---

## 6. Redemption

**Redemption is documented but not yet operational.** The GitBook's redemption page states delivery is available "from **1,000 XGZ per delivery bar**" (i.e. a 1 kg minimum), that "standard settlement timelines and **handling fees apply**", and that fulfilment is by "pickup or delivery via authorized partners, subject to KYC/AML and jurisdictional rules."

Then it says this:

> *"Step-by-step instructions, forms, and venue details will be published when redemption windows open."*

**Redemption windows have not opened.** Seven months after launch, the issuer has published no process, no forms, no venues, no fee schedule and no timeline. Redemption is a stated intention, not a live facility.

**The eligibility arithmetic is brutal.** Minimum redemption is 1,000 XGZ (~$129,700). Total supply is 39,000 XGZ across **264 holders**, an average holding of ~148 XGZ (~$19,200). **The average holder is roughly 6.8x below the redemption floor.** Combined with a members-only mint, XGZ is for most holders a one-way instrument with no primary-market exit at all.

This is exactly the "eligibility limited to undefined qualified holders" pattern the brief warns about, in a harder form: eligibility is limited by a bar-sized minimum plus unpublished "jurisdictional rules", and Hong Kong residents are excluded outright.

---

## 7. Fees and revenue model

| Fee line | Amount | Source |
|---|---|---|
| Mint / subscription | **Not disclosed** | n/a |
| On-chain transfer fee | **0.01% of transfer amount, paid by sender** | GitBook specifications |
| Ongoing custody / storage | **Not disclosed** whether any is charged | n/a |
| Redemption | "**Handling fees apply**", amount **Not disclosed** | GitBook redemption page |
| Management / performance | **0% / 0%** | rwa.xyz |
| Yield to holders | **None** | High |

**The transfer fee is the one genuinely unusual mechanism here and it is worth Aurumix's attention.** XGZ levies a **protocol-level 0.01% fee on every on-chain transfer**, taken from the sender. Almost no gold token does this: PAXG, XAUT, XAUm, VNXAU and Comtech all charge zero on transfer. It converts velocity into revenue rather than taxing the balance.

**Who pays for the vault is Not disclosed.** With 0% management fee, no disclosed storage fee, and a mint fee that is also undisclosed, the only visible recurring revenue line is 0.01% of transfer volume. Against ~39 kg of gold, that is negligible: even at $113k of daily on-chain-equivalent turnover, 0.01% is roughly **$11 a day, about $4,100 a year**. Real vaulting, insurance and assay costs for 39 kg exceed that comfortably. **The economics only work because HKGX is absorbing the cost as a strategic loss-leader**, which is an inference, not a disclosure, and it is exactly the fragility that killed PMGT (zero fees, zero revenue, no internal advocate).

---

## 8. Token architecture

- **Chain:** Ethereum only. **Standard:** ERC-20, 8 decimals. Not ERC-3643 or any permissioned standard.
- **Contract:** `0x69af64f409c08E9076bF7f3ed9Db3a7409717161`, owner address `0xd173e69192b9ff22069aa913ef6e6e94b19f0778`.
- **Transfers:** freely transferable at the contract level. **No whitelist, no on-chain permissioning.**
- **Upgradeability, proxy pattern, pause / freeze / blacklist / forced-transfer functions, admin key custody (multisig vs single key): Not disclosed** in issuer documentation.

**The architecture directly contradicts the compliance posture, and this is the structurally interesting part.** The primary market is locked to KYB-verified HKGX members and redemption requires KYC plus "jurisdictional rules", yet the token itself is a **plain permissionless ERC-20**. Once minted, it moves to anyone, anywhere, including into the hands of the Hong Kong residents the issuer says are excluded. **The compliance perimeter exists only at mint and redeem; the middle is entirely open.** The one enforcement mechanism actually implemented on-chain is a 0.01% fee, not a transfer restriction.

---

## 9. Liquidity and market

**~$5.06M market cap, ~$113k daily volume (2.2% turnover), 264 holders, and it trades at a ~1.4% DISCOUNT to spot** ($129.68 vs ~$131.50/g on 27–28 July 2026).

Liquidity is almost entirely custodial, not on-chain: **92.4% of volume is the MEXC XGZ/USDT pair** ($104k), BitKan adds ~$8.2k, and the two **Uniswap V4 pairs combined turn over under $320 a day**. All-time high $162.73 (7 July 2026) against an all-time low of $126.60 (30 June 2026) is a 28% range in five weeks for an instrument that should track a metal that moved a fraction of that: evidence of a thin, gappy market rather than a tracking one.

One more data point for the settled premium thesis, and it lands where the brief predicts: **XGZ is a discount case, like ORO**. The mechanism is visible here. Arbitrage cannot close the discount because **you cannot mint unless you are an HKGX member and you cannot redeem below 1 kg**, so no ordinary participant can buy the discount and redeem into metal. **The permissioned primary market is precisely what prevents the discount from closing.** Question 6 remains dead; XGZ shows a new reason why.

---

## 10. Distribution

**No savings plan, no recurring purchase, no referral programme, no affiliate scheme, no agent network. None found.**

Distribution is: HKGX member institutions at the primary level, then a MEXC listing and a Uniswap pool for everyone else, plus the "exchanges and distributors" the GitBook mentions without naming. Target segment is Asian institutional and semi-professional gold traders already inside the HKGX orbit. Geography excludes Hong Kong residents.

The one distribution-shaped initiative is the **UAE corridor MoU** (§11), which is a B2B liquidity partnership, not a retail channel.

**For Aurumix this protocol contributes nothing on question 8 except further confirmation that the recurring-contribution model is unoccupied ground.** Nine profiles in, still no competitor has built one.

---

## 11. Recent developments

- **2 July 2026:** MoU between **Universal Digital Intl Limited** (ADGM-based issuer of the USDU stablecoin), **Midas Labs**, and **GoldZip Digital Pte. Ltd.** to explore linking the UAE's regulated stablecoin ecosystem with Asian digital gold. Universal Digital holds **ADGM FSRA financial services permission No. 250089** to issue Fiat-Referenced Tokens **to Professional Clients**, and is registered with the **Central Bank of the UAE as a Foreign Payment Token issuer under the Payment Token Services Regulation (PTSR)**. The MoU is **explicitly exploratory**: it "establishes a framework for further dialogue", with no binding commitment and no product. Quotes from Barry Ip (GoldZip Director) and Juha Viitala (Universal SEO) ([Manila Times / PR Newswire](https://www.manilatimes.net/2026/07/02/tmt-newswire/pr-newswire/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/2377222), [Macau Business](https://macaubusiness.com/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/)).
- **7 July 2026:** XGZ all-time high of $162.73, ~24% above gold parity, on a market with under $320/day of DEX liquidity.
- **30 June 2026:** XGZ all-time low of $126.60.
- **19 May 2026:** GoldZip names **Midas Labs** its strategic Web3 development partner, "responsible for building the underlying digital architecture", with a stated one-to-two-year build horizon ([cointrust](https://www.cointrust.com/market-news/goldzip-and-midas-labs-advance-digital-gold-ecosystem), [TMCnet / PR Newswire](https://www.tmcnet.com/usubmit/-hong-kong-gold-exchange-subsidiary-goldzip-names-midas-labs-as-strategic-web3-/2026/05/18/10384806.htm)).
- **H1 2026 (forward-looking claim):** GoldZip projects a **US$300M gold reserve by H1 2026**, which it says would make XGZ the third-largest gold token after XAUT and PAXG ([goldzip.info/news](https://goldzip.info/news/)). **Actual reserve as at 28 July 2026: ~$5.06M, i.e. 1.7% of target.** The claim should be treated as marketing.
- **23 December 2025:** XGZ launches, listing on MEXC and Uniswap ([Decrypt](https://decrypt.co/353315/hkgx-backed-goldzip-launches-xgz-asias-first-gold-token-supported-by-a-leading-gold-exchange)).
- **Not found:** any yield/earn/staking/lending product on XGZ; any exchange delisting; any exploit, depeg or redemption failure; any published PoR or attestation; any funding round or executive change at the GoldZip entities.

---

## 12. Relevance to Aurumix

**Question 2, dividend funding: this is a negative result, and it is the most decision-relevant thing in the profile.**

The task assumed XGZ was a yield-bearing gold product wrapped in an issuer-SPV note programme, which would have made it the documented precedent Aurumix's dividend design needs. It is not. **XGZ pays no yield, the gold is not lent or leased, and there is no note programme.** Meanwhile the Midas that *does* have the European prospectus wrapper (Midas Software GmbH, Liechtenstein FMA-approved prospectus, passported across the EEA) **issues no gold product at all**.

That is worth stating plainly to the client: **an exchange-owned gold issuer with a 115-year-old parent, sitting on real vaulted metal, chose not to generate yield on it.** HKGX has better access to bullion-leasing counterparties than Aurumix ever will, and it left the gold idle. That is evidence about the risk-adjusted attractiveness of encumbering reserve gold, from the most credible institutional operator in the comparison set. It strengthens, rather than weakens, the case that **Kinesis's instrument split** (sell the yield as a separate capped security, keep the gold token clean) is the leading structural answer. **The Streamex SEC filing remains the only live lead for a documented gold-leasing precedent.**

**Question 4, regulatory route: a UAE lead worth chasing, and a warning.**

The 2 July 2026 MoU surfaces **Universal Digital Intl Limited, ADGM FSRA permission No. 250089**, plus **CBUAE registration as a Foreign Payment Token issuer under the PTSR**. This is a concrete, verifiable UAE authorisation adjacent to the ADGM route flagged in the brief. Two caveats before anyone gets excited: the permission is to issue **Fiat-Referenced Tokens to Professional Clients**, which is the opposite of Aurumix's mass-retail gold product, and the MoU is non-binding with no product behind it. **Useful as a register lead and a named comparator; not a template.**

The warning is the mirror of Comtech. GoldZip presents a **MinLaw AML dealer registration** as "full regulatory compliance license in Singapore." **Aurumix must not adopt that framing.** A precious-metals trade/AML registration is not authorisation to issue a token to the public, and the gap between the two is exactly where enforcement risk lives. If Aurumix is tempted to lean on a DMCC/DAFZA/free-zone trade licence in lieu of VARA, this is now the **second** documented example of that framing being unsupportable.

**Question 3, token standard: XGZ is the cleanest illustration of why Aurumix should not use a bare ERC-20.**

GoldZip wants a permissioned perimeter (members-only mint, KYC redemption, Hong Kong residents excluded) but implemented a **plain transferable ERC-20**. The result is a compliance regime that binds at the edges and evaporates in the middle: excluded persons can hold it, and nothing on-chain stops them. Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, **all of which break on exactly the anonymous transfer XGZ permits**. XGZ is what Aurumix's design looks like if the permissioning is deferred. It supports the ERC-3643 base.

**Question 5, redemption: a sharper version of Aurumix's own gap.**

Aurumix's honest weakness is no physical redemption. XGZ's is arguably worse and less honest: it **advertises** physical redemption while the process, forms, venues, fees and timeline "will be published when redemption windows open", seven months post-launch. Layered on a 1 kg minimum against a ~148 XGZ average holding, **~all holders are ineligible in practice**. Aurumix's cash-buyback-only design, clearly stated up front, is more defensible than a redemption promise that cannot be exercised. **Do not soften Aurumix's disclosure to match competitor marketing; the competitor marketing is the liability.**

**Question 7, proof of reserve:** GoldZip promises "periodic attestation reports by accredited auditors" and has published none, while apparently having a smart-contract audit. For Aurumix, whose entire retail pitch is "100% of every dollar buys physical gold", **shipping the attestation before the marketing is a cheap and genuine differentiator.** Four protocols in this set now blur code audits with reserve attestations; XGZ makes five.

**Question 9, wind-down:** **Not disclosed.** No insolvency provision, no segregation, no trustee, no wind-down plan. Ten profiles, still zero competitors with a published wind-down plan. **The differentiation opportunity the brief identified is confirmed and still unoccupied.**

**Question 1, custody fee:** the interesting variant is the **0.01% sender-paid transfer fee**, a velocity tax rather than a balance tax. It is peg-neutral for Aurumix's grams ÷ tokens formula since it does not touch the gram count, and it does not punish long-term holders. But the arithmetic (~$4k/yr against 39 kg) shows it cannot fund custody at small scale, which is the same revenue-starvation trap that killed PMGT.

**Question 6, premium:** one more data point, discount side. Recorded in §9, conclusion not re-argued.

---

## 13. Open items for verification

- [ ] Resolve which entity actually issues XGZ: **GoldZip Pte. Ltd. (202119587H)** per HKGX, or **GoldZip Digital Pte. Ltd. (202119588Z)** per goldzip.info and CoinMarketCap. Pull both ACRA business profiles for current directors, shareholders, share capital and any secondary SSIC codes.
- [ ] Confirm against the MinLaw regulated-dealers list which of the two entities holds the PSPM registration, and obtain the registration number. Direct scraping of `acd.mlaw.gov.sg` returned 404/403 in this pass.
- [ ] Retrieve the goldzip.info "Terms & Conditions", "Rules" and "Legal Policy" pages in full and check for any gold-title, trust, segregation or insolvency clause. These were referenced in the site footer but not retrievable here.
- [ ] Retrieve the smart-contract audit file and GitHub commit linked from the GitBook smart-contract page. Identify the auditor and whether the report covers mint authority, pause/freeze/blacklist and upgradeability.
- [ ] Inspect the verified contract source at `0x69af64f409c08E9076bF7f3ed9Db3a7409717161` on Etherscan for proxy pattern, owner privileges, and any forced-transfer or blacklist function. Determine whether owner `0xd173e6...0778` is an EOA or a multisig.
- [ ] Establish Midas Labs' jurisdiction and company registration number. It is unregistered in every source checked, despite being the named infrastructure partner to an HKGX subsidiary and a signatory to the ADGM MoU.
- [ ] Verify **ADGM FSRA permission No. 250089** for Universal Digital Intl Limited on the FSRA public register, and confirm the CBUAE PTSR Foreign Payment Token registration. This is the live UAE lead.
- [ ] Confirm whether GoldZip has published any reserve attestation since 28 July 2026, and whether redemption windows have opened.
- [ ] Confirm the Brink's custody claim on rwa.xyz against a primary source. No issuer document names any custodian.
- [ ] Check whether XGZ's exclusion of Hong Kong residents is driven by SFC virtual-asset rules or by the HKGX parent's own licensing constraints, and whether any equivalent carve-out would apply to a UAE issuer selling into India/UAE/NRI markets.

---

# Comtech Gold (CGO)

> **⚠ OUR WORKING ASSERTION WAS HALF WRONG, AND THE HALF THAT WAS WRONG IS THE HALF WE BUILT A HYPOTHESIS ON.**
>
> **We asserted: "Comtech operates from Dubai on a DMCC trade licence with no VARA or ADGM authorisation."**
>
> **The "no VARA" half is CORRECT and now verified against the register directly: Comtech does not appear anywhere on VARA's public register of 52 licensed VASPs, nor on the DFSA or ADGM FSRA registers.**
>
> **The "DMCC trade licence" half is WRONG, and the correction matters more than the error. The token issuer is `ComTech FZCO (DAFZA)`, a Dubai Airport Free Zone company, licence number **05069**, activity **"GOLD AND OTHER PRECIOUS METALS TRADING"**, issued 21-Feb-2022. There is a *separate* `ComTech FZCO (DMCC)` entity, licence **DMCC-889799**, but its registered activities are **IT consultancy, network consultancy, internet consultancy and software house**: it is a tech-services licence and cannot issue gold tokens either. Neither licence authorises issuing a virtual asset to the public.**
>
> **So there is no "DMCC gold-token path that routes around VARA." There is no authorised path here at all. What Comtech demonstrates is not a lawful alternative route: it is a pre-VARA-regime incumbent that has never been brought onto the register. Do not model Aurumix on it.**
>
> **Also: both licences shown on Comtech's own registration page are displayed EXPIRED (DAFZA expiry 20-Feb-2024; DMCC expiry 25-Jun-2024). See §3.**
>
> **Two further corrections to inherited framing: the Shariah certifier is no longer Amanie Advisors (superseded by Sābiq Advisory on 31 March 2026, §4), and there is no monthly proof of reserve (§4).**

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | CGO | **High** |
| Issuer (marketing) | "ComTech Gold" | **High** |
| Issuer (registry) | **ComTech FZCO (DAFZA)**, licence 05069, Dubai Airport Free Zone, issued 21-Feb-2022. Separate **ComTech FZCO (DMCC)**, licence DMCC-889799 / cert DMCC197166, formed 31-May-2023 | **High** |
| Parent | Trade Fintech Ltd, DIFC private company, registered number **5102**, incorporated 4 Oct 2021 (per whitepaper) | **Medium** |
| Cash-collecting entity | **COMTECH CORE TRADING FZCO**, ZAND Bank AED a/c 1002169010000001 (from the live app API, a third name) | **High** |
| Domicile | Dubai, UAE (DAFZA primary; DMCC secondary) | **High** |
| Backing claim | 1 CGO = 1 g gold, 999.9 fineness, standardised 1 kg bars | **High** |
| Chains | XDC / XinFin only | **High** |
| Contract address | `xdc8f9920283470f52128bf11b0c14e798be704fd15` (EVM `0x8f99...fd15`), 18 decimals | **High** (on-chain) |
| Supply | **39,000 CGO** on-chain `totalSupply` = 39 kg implied | **High** (on-chain) |
| Last published reserve | **111 kg** as at 21 Mar 2025 | **High** |
| Market cap | ~$5.04M | **High** |
| 24h volume | ~$815k, of which ~$814k is a single Bitrue pair | **High** |
| Regulatory status | **No VARA licence. No DFSA. No ADGM FSRA.** Free-zone trade licences only | **High** |
| Subscription fee | Website: "Transaction Fees: Nil". App API: buy commission **1.0125%** + payment charges + 5% VAT | **High** (contradiction, §7) |
| Ongoing custody fee | Website: "Custody Fees: Nil". FAQ: free for **first 24 months**, then "a nominal fee" | **High** (contradiction) |
| Redemption fee | 0.50% physical redemption; 0.50% transfer | **High** |
| Advertised yield | None on the token. A separate opt-in gold-financing facility exists (T&C Part B) | **High** |
| Named officers | Jignesh Ved (Founder & CEO); Lim Say Cheong (Chief Advisor, Digital Assets & Islamic Finance); Gagandeep Singh (Marketing). Navin D'Souza, CEO in the 2022 DMCC release, no longer listed | **Medium** |

## 1. What it is

A 1 gram = 1 token gold product issued from Dubai on the XDC (XinFin) network, live since 2022, sold both as a tradeable token (CGO) and as an app-based "ComTech Digital Gold" savings/buying product in AED. It is Shariah-certified and its main public credential is a 2022 partnership with DMCC under which gold bars are registered on **DMCC Tradeflow** warrants ([dmcc.ae](https://dmcc.ae/latest-news/dmcc-digitises-gold-trading-through-tokenisation-comtech-gold-bullion-backed-dmccs-tradeflow-platform), 10 Dec 2022).

Two things make it the most relevant comparator in this batch: it is the closest thing to a direct UAE precedent for what Aurumix wants to do, and it is the clearest evidence of how a Dubai gold token has actually handled (or avoided) the licensing question.

Note the dual-product structure. The `comtechgold.com` domain now redirects to **`cgold.ae`**, a retail app site with an AED price feed, KYC onboarding and a bank account: a retail deposit-taking-shaped business, not just a token.

## 2. Legal structure

What a holder owns, from the **Terms & Conditions dated 23 August 2022** ([cgold.ae/assets/pdf/Terms_and_Conditions.pdf](https://cgold.ae/assets/pdf/Terms_and_Conditions.pdf)), which is the only primary legal document published:

- **Clause 3.2:** each unit "represents undivided ownership and specific interest in one (1) gram of at least 999 purity gold in the Gold Reserves." So the claim is **direct co-ownership of an undivided interest**, not a creditor claim and not a trust. **Confidence: High.**
- **Clause 3.6:** the holder "expressly and irrevocably appoint[s] and authorize[s] the Digitization Entity for an indefinite period of time to be custodian, administrator and holder of the specific interest... by acting as **agent in possession** for You." Bailment/agency, indefinite and irrevocable.
- **Clause 3.4:** "Digital Gold is not intended to be a 'security'." An assertion of the issuer's intent, with no regulator having ruled on it. Report as assertion.
- **Clause 3.5** contains a striking carve-out: 100% backing is promised "however in rare cases wherein due to holiday or logistical issues, the Digitalization Entity is not able to back it up with Gold Reserves, **it can do so subject to a maximum limit of 10kgs** and it shall ensure to back it up... within 24 hours of the next business day." **A contractually permitted 10 kg unbacked float.** Against a last-published reserve of 111 kg that is a permitted ~9% under-backing window. This directly contradicts the "100% backed at all times" marketing.
- **Clause 15.4:** total issuer liability "shall in no circumstances exceed the fees received by the Digitization Entity." The ownership claim in 3.2 is therefore capped, in the event of a dispute, at fees collected.
- **Governing law: English law. Arbitration: LCIA, seat DIFC, one arbitrator, English** (17.6, 17.7). A UAE retail buyer's remedy is an individual LCIA arbitration, which is prohibitively expensive for a small retail holder. This is a material consumer-protection gap.

**Critically, clause 3.6 gives the issuer indefinite custody, and the entity holding that role is a DAFZA precious-metals trader with no financial-services authorisation and no client-money regime.**

## 3. Regulatory and compliance posture

This is the section the profile exists for. Here is exactly what was checked and what was found.

| Register checked | Searched for | Result |
|---|---|---|
| **VARA public register** (52 licensed VASPs) | Comtech, ComTech Gold, ComTech FZCO | **Not present.** No licence, no provisional permit, no registration |
| **DFSA / DIFC** | ComTech FZCO, Trade Fintech Ltd | **No DFSA financial services licence found.** Trade Fintech Ltd appears only as a DIFC-registered private company (non-regulated), per the whitepaper's own account |
| **ADGM FSRA** | Comtech, Trade Fintech | **Not found.** No FSP, no recognition. (For contrast, Tether Gold obtained ADGM Accepted Spot Commodity recognition in July 2026: that route exists and Comtech has not used it) |
| **DAFZA / DIEZ** | ComTech FZCO (DAFZA) | **Found. Licence 05069.** Activity: GOLD AND OTHER PRECIOUS METALS TRADING. Issued 21-Feb-2022, **expiry shown 20-Feb-2024** |
| **DMCC** | ComTech FZCO (DMCC) | **Found. Licence DMCC-889799**, cert/reg DMCC197166, a/c 407812. Activities: IT consultants, network consultancies, internet consultancy, software house. Formed 31-May-2023, issued 26-Jun-2023, **expiry shown 25-Jun-2024** |

Source for both licences is Comtech's own Company Registration page, [cgold.ae/companyregistration](https://cgold.ae/companyregistration). **Confidence: High** (issuer-published registry extract, self-certified).

**The findings that matter:**

1. **Neither licence permits token issuance to the public.** A DAFZA licence for "gold and other precious metals trading" authorises trading bullion. A DMCC licence for "software house / IT consultancy" authorises writing software. Neither is a virtual-asset authorisation. VARA's remit covers the Emirate of Dubai **including all free zones except DIFC**, which expressly includes DAFZA and DMCC. Issuing and offering a virtual asset to the public is a VARA-regulated activity. **So the answer to "does a DMCC trade licence permit token issuance to the public" is no, and neither does the DAFZA one. There is no separate authorisation we were missing: there is an absent authorisation.**

2. **Our hypothesis of a "Dubai gold-token path that routes around VARA" is not supported.** Comtech is not evidence of a legitimate alternative route. It is evidence that an operator which launched in 2022 (before VARA's regime bit) has continued operating without ever appearing on the register. That is an unremediated exposure, not a template. **Aurumix must not treat this as precedent.** Anyone advising that "Comtech does it on a DMCC licence, so we can too" is relying on a factual error about which licence, and a legal error about what it permits.

3. **The licences shown are expired.** The issuer's own page displays DAFZA expiry 20-Feb-2024 and DMCC expiry 25-Jun-2024, both long past as of 28 July 2026. The most likely explanation is that the page was simply never updated after renewal, which is the charitable and probably correct reading. But it is published as-is on the live site of a business currently taking retail deposits, and we cannot confirm current good standing from the public record. **Confidence: High that this is what is published; Not disclosed as to actual current licence status.**

4. **The FAQ makes an affirmative regulatory claim that is misleading.** It states: *"Is ComTech Gold regulated? Yes, ComTech Gold is regulated by Dubai Airport Free Zone Authority (DAFZA) and endorsed by local UAE government body DMCC... We strictly follow the regulatory guidelines towards the capital reserve, consumer protection, compliance, and anti-money laundering"* ([FAQ PDF](https://cgold.ae/assets/pdf/ComTech_Gold_FAQ_Final.pdf)). A free zone authority is a **company registrar and licensor, not a financial regulator**; it imposes no capital reserve or consumer-protection regime on a bullion trader. Telling retail customers this constitutes being "regulated" with "the highest form of protection" is the single most material disclosure problem found in this profile. **This is exactly the marketing-vs-legal gap the brief asks us to surface.**

5. **A third entity handles the money.** The live app configuration endpoint (`appapi.comtechgold.com/api/setting`) returns bank details in the name of **COMTECH CORE TRADING FZCO** at ZAND Bank. Customer funds are therefore received by an entity whose name appears on neither the DAFZA nor the DMCC certificate published on the site, and whose licence we could not locate. **Confidence: High** that this is the named account holder; **Not disclosed** as to that entity's licence and its relationship to the issuer.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian / vault | **Transguard** (Emirates Group company), UAE. T&C 4.1 permits storage "in the UAE **or elsewhere**" and via affiliates "anywhere in the world" | **High** |
| Allocated / segregated | T&C 4.2: segregated, not commingled. Whitepaper: 1 kg bars, 999 purity, identifiable by bar number | **High** (as contractual promise) |
| Published bar list | **Not disclosed.** No bar-number list is published anywhere. The whitepaper says bars "would be distinctly identifiable through their bar number"; no such list exists publicly | **High** (verified absent) |
| PoR feed | **None.** No Chainlink PoR, no oracle, no live attestation feed | **High** |
| Reserve attestation | **Self-issued letters on Comtech letterhead, signed "For ComTech FZCO". Not an independent auditor's report** | **High** |
| Latest attestation | **21 March 2025**, stating 111 × 1 kg bars: 19 kg on DMCC Tradeflow + 92 kg with "Vaulting Partner" | **High** |
| Smart contract audit | **Not disclosed.** No published smart-contract audit found | **High** |

**On the "monthly proof of reserve with published bar lists" in our working notes: that claim does not survive contact with the evidence. It is wrong on all three counts.**

The reserve history published on the site is not monthly, is not independent, and has stopped. Full published series:

| From | To | Opening | Deposit | Withdrawal | Closing |
|---|---|---|---|---|---|
| 01 May 2022 | 25 May 2022 | 0 kg | 100 kg | 0 kg | 100 kg |
| 26 May 2022 | 06 Jun 2022 | 100 kg | 4 kg | 0 kg | 104 kg |
| 07 Jun 2022 | 12 Jul 2022 | 104 kg | 17 kg | 0 kg | 121 kg |
| 13 Jul 2022 | 30 Aug 2022 | 121 kg | 1 kg | 0 kg | 122 kg |
| 31 Aug 2022 | 04 Jan 2023 | 122 kg | 2 kg | 0 kg | 124 kg |
| 05 Jan 2023 | 08 Mar 2023 | 124 kg | 17 kg | 0 kg | 141 kg |
| 09 Mar 2023 | 11 Oct 2023 | 141 kg | 3 kg | 0 kg | 144 kg |
| **12 Oct 2023** | **21 Mar 2025** | **144 kg** | **29 kg** | **62 kg** | **111 kg** |

Three observations:

1. **Frequency is irregular and lengthening**, from ~3 weeks to a single 17-month period. Calling this "monthly" is not defensible.
2. **The last period shows the first ever withdrawals: 62 kg out, a 23% net decline.** Gold left the vault. Nothing published explains why.
3. **Nothing has been published since 21 March 2025: over 16 months of silence** as of today. For a product whose entire value proposition is verifiable backing, a 16-month attestation gap is the finding.

**The reserve/supply mismatch.** Last published reserve is **111 kg**. On-chain `totalSupply` today is **39,000 CGO = 39 kg**. These do not reconcile, and the gap runs in the *over*-collateralised direction (72 kg more gold than tokens). The benign reading, which is probably right, is that the app-based "Digital Gold" book is unminted (customers hold ledger entries, not tokens), so vault gold backs both the 39 kg of tokens and a larger off-chain retail book. **But that reading is itself the problem: it means the majority of Comtech's customer liability is an off-chain database entry with no on-chain verifiability at all**, and the published reserve letters do not split the two. **Confidence: High** on both numbers; **Not disclosed** as to the reconciliation.

**Shariah certification (our notes said Amanie Advisors: now superseded).** The original certification was issued by **Amanie Advisors Ltd** in September 2022, making CGO the first Shariah-certified gold token in MENA ([Businesswire, 26 Sep 2022](https://www.businesswire.com/news/home/20220926005591/en/ComTech-Gold-%24CGO-Becomes-the-First-100-Gold-Backed-Token-to-Receive-Shariah-Certification-in-the-MENA-Region)). That is no longer the operative certification. The current document is a **fatwa dated 31 March 2026 from Sābiq Advisory**, signed by Dr Mohamed Ali Elgari (Chairman), Dr Muhammad Amin Ali Qattan and Dr Osama Al Dereai, which states expressly: *"This Fatwa supersedes the earlier fatwa dated 6 September 2022 issued by the previous Shariah Advisor and applies prospectively from the date of our appointment"* ([fatwa PDF](https://cgold.ae/assets/pdf/SABIQ%20FATWA%20-%20STANDARDIZED%20GOLD%20TOKEN%20PRODUCT%20(%E2%80%9CCGO%E2%80%9D)%20BY%20COMTECH%20FZCO.pdf)). **Confidence: High.** Two caveats: the fatwa **expressly excludes** "any distinct financing, leverage, or yield-generation mechanics" from its scope; and T&C 14.3 disclaims any warranty of Shariah compliance and makes the holder responsible for their own determination, while 18.1 bars the holder from ever challenging Shariah compliance. The certification is real; the contract makes it non-actionable.

## 5. Issuance

- Minting is centralised and discretionary. Token creation follows gold deposit; bars are registered on **DMCC Tradeflow warrants** and (per the March 2025 letter) split between Tradeflow-registered and vaulting-partner holdings.
- Retail issuance is via the ComTech Gold app after KYC. **Minimum purchase 0.5 g** (app API), with the FAQ elsewhere saying "as low as 0.5 gm". The whitepaper's older claim was 1 g.
- Institutional/wholesale route: gold suppliers named in the whitepaper as under discussion (StoneX); StoneX appears as a partner logo on the site.
- Pricing is issuer-quoted, not oracle-driven: the app API returns a buy rate and a sell rate in AED set by Comtech (at capture: buy 131.18, sell 128.89 AED/g, a **~1.8% round-trip spread**).
- **The permitted 10 kg unbacked issuance window (T&C 3.5) is an issuance mechanic, not just a disclosure**: the issuer may mint ahead of gold.

## 6. Redemption

**There is a direct and unresolved contradiction between the binding legal document and the marketing.**

| Source | Minimum redemption | Status |
|---|---|---|
| **T&C clause 8.1** (binding) | **1 kilogram**, and "in further denominations of one kilogram each" | **High** |
| FAQ + website | **10 grams**, thereafter multiples of 1 gram | **High** |
| Whitepaper §3.4 | 1 kg (1000 tokens) | **High** |
| Whitepaper §4.7 | 10 g "at a later stage... through Redemption Partners" | **High** |

The reconciliation is that 1 kg is the **contractual** right to bar delivery, while 10 g is a **discretionary retail** service delivered as minted coins (with making charges) or via "Authorized Partners" (jewellers, T&C clause 9, minimum 1 g exchange for jewellery). The retail 10 g route is a commercial accommodation, not a contractual entitlement. **A holder's enforceable redemption right is 1 kg: at ~$129/g that is roughly $129,000, which excludes essentially every retail holder.** For Aurumix this is the standard pattern: headline retail redemption that is not the legal right.

Other terms:
- Redemption fee **0.50%**, plus making charges and delivery at holder's cost.
- Collection in person at the vault or delivery; outside UAE, delivery is only to "the nearest Airport" with the customer handling customs.
- Orders are **irrevocable**: purchase, sale and delivery requests cannot be cancelled once placed (FAQ).
- Only the holder may redeem; on death, legal heirs may claim with death certificate and proof of heirship (a genuine parallel to Aurumix's Digital Will).
- **T&C 16.2 lets the issuer suspend redemption entirely** for force majeure "or on account of any technical issue faced **or otherwise**." "Or otherwise" is an unlimited discretionary suspension right.

## 7. Fees and revenue model

The published fee table and the live app disagree, and the difference is the whole revenue model.

**Website fee table** ([cgold.ae](https://cgold.ae) Fee Structure):

| Line | Rate |
|---|---|
| Transaction Fees | **Nil** |
| Custody Fees | **Nil** |
| Insurance Fees | **Nil** |
| Transfer Fees | 0.50% |
| Physical Gold Redemption Fees | 0.50% |

**Live app API** (`appapi.comtechgold.com/api/setting`, captured 28 Jul 2026):

| Line | Rate |
|---|---|
| Buy commission | **1.0125%** |
| Sell commission | **0.9950%** |
| Quoted buy/sell spread | ~1.8% round trip |
| AED payment charge | 1% |
| Card / Google Pay / Apple Pay | 2.4% |
| USD charge | 0.27% |
| VAT | 5% |

**So "Transaction Fees: Nil" is not what a customer pays.** A retail buyer pays roughly 1% commission plus up to 2.4% payment charge plus VAT plus the ~1.8% spread. The revenue model is **spread and commission at the point of sale**, not a custody fee. **Confidence: High** (live production endpoint).

**On custody specifically, which is Aurumix design question 1:** the marketing says "Custody Fees: Nil", but the FAQ discloses that custody is *"without charge for the first 24 months, and thereafter... a nominal fee to cover storage costs,"* with advance notice and the option to sell or take delivery. T&C 11.1.6 lists "Storage fees, which will include costs for the Vaults and insurance" as a chargeable line, and 11.4 lets Comtech change fees unilaterally, effective on posting, with continued use constituting acceptance.

**This is the single most useful data point in the profile for Aurumix.** Comtech resolves the grams-vs-cash custody dilemma by **choosing the third option: charge the holder nothing for custody and recover the cost in the buy/sell spread and commission at transaction time.** That keeps 1 token = 1 gram exactly intact (no peg drift, which is precisely the failure mode Aurumix identified), and it funds storage from transaction margin. The cost is that revenue is volume-dependent, which for a buy-and-hold savings product is thin, and Comtech has visibly hedged by reserving the right to introduce a storage fee after 24 months.

**Yield: none on the token.** But T&C **Part B, clause 20** (expressly outside Shariah certification) describes a **gold-financing facility**: Comtech may lease pooled gold reserves to "commercial parties in the gold and jewellery business" for up to 6 months in return for a "Margin". Holders opt in, their tokens are locked, the underlying gold is released to the financed party, and critically: *"The Digitization Entity will not be liable to the Financed Party or the Participating Digital Gold Holder and will simply facilitate the transaction. **The Participating Digital Gold Holders will take the risk** under the proposed transaction."* This is the same structure as ORO's Monetary Metals leasing, disclosed more honestly: the holder, not the issuer, eats a default. Whether it is live is **Not disclosed**.

## 8. Token architecture

- **Standard: plain ERC-20 equivalent (XRC-20) on XDC.** 18 decimals, name "Comtech Gold", symbol "CGO". Verified on-chain.
- **Not permissioned.** No ERC-3643, no whitelist/identity layer, no transfer restriction observed. Anyone can hold and transfer. This is the opposite of the direction Aurumix is leaning.
- **Contract:** `0x8f9920283470f52128bf11b0c14e798be704fd15`, bytecode ~8KB. Includes a `paused()` function, so **transfers are pausable by the issuer**.
- **Admin keys:** the `owner()` is `0xc639b48ea44e94f1a69da11974a29e6ddb8c6fa1`, held via an intermediate **contract** at `0x21f74fbf81d68291704805d085982000babbf096` (36KB bytecode). It did not respond to Gnosis Safe interface calls (`getOwners`, `getThreshold`), so it is **not a standard Safe multisig**. It is a custom ownership/admin contract. **Whether control is genuinely multi-party is Not disclosed**, and it cannot be established from the interface. For a token whose entire risk sits with the issuer, unverifiable admin control is a real gap.
- **Single chain, no bridge.** XDC only. This is a strategic weakness: XDC has thin DeFi and thin liquidity, which shows in §9.
- **No published smart-contract audit.** Note the blur the brief warns about: Comtech's marketing says it is "regularly audited", which refers to gold-stock letters, not code. **There is neither an independent reserve audit nor a smart-contract audit.**

## 9. Liquidity and market

Data as at 28 July 2026 (CoinGecko):

| Metric | Value |
|---|---|
| Price | ~$129.31 (tracks ~1 g gold) |
| Market cap | ~$5.04M |
| Circulating = total supply | 39,000 CGO |
| 24h volume | ~$814,566 |

Venue breakdown, which is the real story:

| Venue | Pair | 24h volume | Spread |
|---|---|---|---|
| **Bitrue** | CGO/USDT | **$814,072 (99.94%)** | 0.42% |
| BitMart | CGO/USDT | $280 | 3.17% |
| XSwap V3 (DEX) | CGO/USDC | $213 | 2.21% |

**Essentially all liquidity is one pair on one exchange.** Genuine on-chain DEX liquidity is roughly **$213 a day**. If Bitrue delists or halts, the market is gone.

**This is a second independent data point against the client's premium thesis (design question 6), and it is stronger than the PGOLD one.** PGOLD showed a big book with no market. Comtech shows the same pattern at smaller scale: a ~$5M token whose decentralised market is ~$200/day. Note also that CGO trades *at* gold parity with a tight 0.42% spread on its main venue: **there is no 3–8% sustained premium here.** A commodity token with real redeemability and market makers trades at parity, because arbitrage closes any gap. **Aurumix's 3–8% premium assumption is not supported by the one UAE gold token with a functioning market; if anything this is evidence that a working market actively prevents such a premium.**

Also note supply has *contracted*: reserves fell from 144 kg to 111 kg, and on-chain supply is 39 kg. This is not a growing book.

## 10. Distribution

- **App-first retail**, iOS and Android ("ComTech Gold", app v3.08), AED-denominated, KYC'd, 0.5 g minimum. This is closer to Aurumix's retail model than any other protocol in the batch.
- **Jeweller redemption network:** "Authorized Partners" (T&C 9), with **Kalyan Jewellers** as a named partner and its store locator linked from the site. Kalyan is a major India/GCC jeweller serving exactly the Indian-expat/NRI segment Aurumix targets. **This is the most directly transferable distribution asset in the profile.**
- **Referral mechanism: yes, and it is live.** The app config carries an active referral code (`LULU25`), which points to a tie-up with the Lulu retail group, another India/GCC mass-market channel. **Confidence: Medium** on the Lulu interpretation; **High** that a referral-code system exists in production.
- **Banking:** ZAND Bank (UAE digital bank) accounts in AED and USD. Getting a UAE bank to serve a gold-token business is non-trivial and is a genuine achievement to note.
- **Savings plan / SIP: none found.** There is no recurring-contribution or systematic investment product. The FAQ explicitly says there is **no lock-in** and **no joint accounts**. **So on Aurumix's core differentiator, Comtech does not compete: it sells one-off purchases, not a premium schedule.** The brief's expectation holds.
- **No agent/commission tier structure** found. Distribution is app + jeweller partners + referral codes, not a 3-tier network.
- Geography: UAE-centric (AED pricing, 800 COMTECH phone line, UAE doorstep delivery), with international delivery degraded to airport collection.

## 11. Recent developments

A dedicated recency sweep (Perplexity Sonar Pro, 18-month window) returned **no dated announcements, no regulatory developments, no listings or delistings, no incidents, no enforcement actions, and no partnerships** for Jan 2025 to Jul 2026. That null result is corroborated by the site itself: there is no news or announcements section with dated entries. Reverse chronological, what can be dated:

- **31 March 2026:** New Shariah fatwa issued by **Sābiq Advisory** (Dr Mohamed Ali Elgari, Dr Muhammad Amin Ali Qattan, Dr Osama Al Dereai), expressly superseding the 6 September 2022 Amanie fatwa and applying prospectively. Confirms a Shariah audit for FYE 2024 was completed by the previous board. **The change of Shariah advisor was not announced publicly anywhere we could find: it is only discoverable by reading the PDF.** **Confidence: High.**
- **21 March 2025:** Last published gold-stock letter. Reserves **111 kg**, down from 144 kg, reflecting 62 kg of withdrawals over the period from 12 Oct 2023. Split 19 kg on DMCC Tradeflow, 92 kg with vaulting partner. **Confidence: High.**
- **Since 21 March 2025 (16+ months):** No further reserve attestation published. **Confidence: High** (verified absent).
- **Undated, but current:** primary domain `comtechgold.com` now redirects to **`cgold.ae`**, and leadership has changed: **Navin D'Souza**, named as Comtech CEO in the December 2022 DMCC release, is no longer listed; **Jignesh Ved** is Founder & CEO. **Confidence: Medium** (site content, no dated announcement).
- **25 June 2024 / 20 February 2024:** Expiry dates displayed for the DMCC and DAFZA licences respectively on the live registration page.
- **Reported plans (issuer marketing, undated, unverified):** vault diversification to Singapore and Switzerland, gold-backed NFTs, listings on KuCoin and Gate.io. **Confidence: Low.** None corroborated.

**The pattern is a project that has gone quiet.** Reserves down 23%, attestations stopped, no announcements in 18 months, leadership turnover, expired licence dates on the site, and a live app still taking retail money. That combination deserves to be stated plainly.

## 12. Relevance to Aurumix

**Comtech is the closest UAE analogue to Aurumix that exists, and its main lesson is a negative one about regulatory strategy.**

**Question 4, regulatory route (the one we came for).** Comtech is *not* a viable precedent for avoiding VARA. It issues a gold token to the public from Dubai on a **DAFZA bullion-trading licence (05069)** and a **DMCC IT-consultancy licence (DMCC-889799)**, neither of which authorises virtual-asset issuance, and it appears on no regulator's register. The "Dubai gold-token path that routes around VARA" is not a path: it is a gap that has not yet been closed. Anyone proposing Aurumix replicate it should be shown that Comtech's own FAQ tells retail customers they are "regulated by DAFZA" with "the highest form of protection", which is the kind of statement that attracts enforcement rather than deflecting it. **Aurumix's ARVA-under-VARA plan, expensive as it is (~AED 100k application, 200k/yr, AED 1.5M capital, 6–9 months), remains the defensible route.** The cheaper-looking alternative is cheap because the bill has not arrived. If we want a genuinely lower-cost regulated route, the live option is **ADGM**, where Tether Gold obtained Accepted Spot Commodity recognition in July 2026: that is worth its own scoping, and it is a real finding from this pass.

**Question 1, custody fee mechanism (the most useful positive finding).** Comtech takes **option three**: custody is free to the holder, and cost is recovered from a ~1% buy/sell commission plus a ~1.8% quoted spread at transaction time. **The peg stays clean at exactly 1 token = 1 gram because nothing is ever deducted in grams.** This validates Aurumix's instinct to avoid gram-denominated fees. But note the catch, and it is severe for Aurumix specifically: **transaction-margin funding only works if people transact.** Aurumix is a buy-and-hold monthly SIP designed to discourage exit, so it would collect that margin once on the way in and then carry storage cost indefinitely with no further revenue. Comtech has visibly felt this, which is why the FAQ reserves a storage fee after 24 months. **Aurumix should assume it will need an explicit cash custody fee or a contribution-loaded charge, and should model storage cost against a holder who contributes $75/month and never sells.**

**Question 2, dividend funding.** Comtech pays **no yield on the token**, which is itself instructive: the closest UAE comparator concluded it could not or should not promise one. Its Part B gold-financing facility is the compliant-ish alternative Aurumix has been weighing, and its terms are worth copying in one respect and avoiding in another. Copy: it is **opt-in**, tokens are **locked** while lent, and terms are disclosed per-deal (counterparty, amount, tenor, margin). Avoid: it dumps counterparty default risk entirely on the holder while the issuer "will simply facilitate". Also note the Sābiq fatwa **expressly carves financing and yield generation out of Shariah approval**: for a Shariah-facing product, a yield mechanism is not covered by the gold certification and needs its own ruling. That is a direct constraint on Aurumix's ICS Dividend if it wants Islamic-market credibility.

**Question 3, token standard.** Comtech uses a plain, non-permissioned XRC-20 with a pausable contract and opaque admin control. It buys exchange listability (Bitrue) and costs any ability to enforce holder-level rights. **Aurumix's rights bundle (ICS standing, dividend entitlement, credit eligibility, buyback rights) would be destroyed by exactly this architecture on the first anonymous transfer.** Comtech is a clean illustration of why Aurumix's ERC-3643-plus-wrapper instinct is right: Comtech can afford ERC-20 precisely because its token carries no rights beyond "1 gram".

**Question 5, redemption.** Direct support for Aurumix's position, from an unexpected direction. Comtech advertises 10 g retail redemption but its **binding contractual minimum is 1 kg (~$129,000)**. So its "you own real gold, take it home" pitch is, legally, available only to holders roughly 1,700x larger than Aurumix's $75/month target customer. **Aurumix's no-physical-redemption stance is more honest than Comtech's, and should be framed that way**: we are explicit about cash-only exit rather than advertising a delivery right that the terms restrict to institutions. Also copy the death/succession handling (heir claims with death certificate and proof of heirship), which maps onto the Digital Will.

**Question 6, premium and liquidity.** Strong evidence against the 3–8% premium thesis, and it now has two independent legs. PGOLD showed AUM without a market. Comtech shows the sharper point: **where a gold token does have a functioning market with market makers and real redeemability, it trades at parity with a 0.42% spread.** A durable 3–8% premium is not a feature of healthy tokenised gold; it is a symptom of illiquidity or capital controls. Meanwhile Comtech's decentralised liquidity is ~$213/day against a $5M cap. **Aurumix should not build revenue projections on a sustained exchange premium.**

**Question 7, proof of reserve.** The cautionary tale. Comtech's attestations are **self-signed letters on company letterhead**, not independent audits, they were never monthly, no bar list was ever published despite the whitepaper promising bar-number identifiability, and they **stopped 16 months ago** after showing a 23% reserve decline. Yet the marketing says "regularly audited by independent third parties". **Aurumix can differentiate cheaply and credibly here**: a genuine independent attestation on a fixed published cadence, a real bar list, and a clear separation of "smart-contract audit" from "reserve attestation". Comtech proves the bar is low. It also proves that PoR practice **decays**: whatever cadence Aurumix commits to must be sustainable for years, because a lapsed schedule is worse than a modest one.

**Question 8, distribution.** The most transferable material in this profile. Comtech reaches Aurumix's exact target segment through **jeweller partnerships (Kalyan Jewellers)** and a **live referral-code system** (`LULU25`, apparently Lulu), plus a UAE banking relationship with **ZAND**. But it has **no savings plan, no SIP, no recurring contribution and no agent tiers**, and explicitly no lock-in. **Aurumix's monthly-premium SIP with a 3-tier agent network is therefore genuinely differentiated in this market**, not a copy of the incumbent. The competitive question is not whether Comtech does SIP (it does not) but whether Aurumix can win the same jeweller and retail-group channels Comtech already occupies.

**Question 9, wind-down.** Comtech has no wind-down plan, consistent with every other protocol in the batch. What it has is worse than silence: an FAQ answer asserting that because "every movement of Gold is endorsed and approved by... DMCC", then "in any unlikely adverse event happening to Company, the gold... will not be affected." **That is a reassurance without a mechanism.** A Tradeflow warrant records title to bullion; it does not create a bankruptcy-remote structure, and T&C 15.4 caps the issuer's total liability at fees received. There is no trustee, no security trustee, no independent custodian holding for holders. **Aurumix committing to a real ex-ante wind-down plan (named trustee, defined waterfall, pre-agreed liquidation agent) remains cheap and genuine differentiation, and Comtech's hand-waving answer is the perfect foil to quote against.**

**One additional cross-cutting warning.** The **contractually permitted 10 kg unbacked issuance window** (T&C 3.5) sits underneath a "100% backed at all times" headline. Aurumix will face the same operational temptation (settlement lag between customer payment and bullion purchase) and should decide *now* whether to disclose a float, size it, and cap it, rather than burying permission for it in clause 3.5.

## 13. Open items for verification

- [ ] Obtain current DAFZA licence 05069 and DMCC licence DMCC-889799 status directly from DIEZ/DAFZA and DMCC registrars: are both renewed and in good standing after the 2024 expiry dates published on the site?
- [ ] Identify **COMTECH CORE TRADING FZCO** (the ZAND Bank account holder): free zone, licence number, activities, and its legal relationship to ComTech FZCO. Customer money flows here.
- [ ] Confirm **Trade Fintech Ltd (DIFC 5102)** current status and shareholding of ComTech FZCO directly on the DIFC public register; confirm it holds no DFSA licence.
- [ ] Ask VARA (or confirm via a UAE counsel note) whether a pre-2022 free-zone gold-token issuer has any transitional relief, or whether Comtech is simply unlicensed. This determines whether our "no lawful route around VARA" conclusion is absolute.
- [ ] Scope the **ADGM FSRA Accepted Spot Commodity** route (as used by Tether Gold, July 2026) as a possible lower-cost alternative to VARA for the gold core. This may be the most valuable follow-up in the batch.
- [ ] Obtain any reserve attestation dated after 21 March 2025; if none exists, treat the 16-month gap as confirmed and note reserves last stood at 111 kg after a 23% decline.
- [ ] Reconcile 111 kg published reserve against 39 kg on-chain supply: confirm the off-chain app ledger explanation and establish how large the unminted retail book is and what evidences it.
- [ ] Establish control of admin contract `0x21f74fbf81d68291704805d085982000babbf096` (owner `0xc639b4...6fa1`): is it multi-party or a single key wrapper? Not a Gnosis Safe.
- [ ] Confirm whether the Part B gold-financing/leasing facility has ever been activated, and on what terms and counterparties.
- [ ] Verify the `LULU25` referral code is a Lulu Group commercial tie-up and obtain the commission terms; same for the Kalyan Jewellers redemption arrangement.
- [ ] Obtain the Sābiq annual Shariah compliance certificate for FYE 2025/2026 (the fatwa is conditional on annual recertification).
- [ ] Confirm whether any smart-contract audit exists for `0x8f99...fd15`.

---

# ORO / Oro Finance (GOLD)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | GOLD (also written $GOLD; rwa.xyz lists it as "Orogold") | High |
| Issuer (marketing) | ORO / Oro Finance / ORO Labs; legal title asserted to sit with an unnamed "ORO Foundation" | Medium |
| Issuer (registry) | **Oro Labs PTE Ltd, UEN 202434484G**, incorporated 22 August 2024, 68 Circular Road, Singapore. ACRA activity: other holding companies / software development | High |
| Domicile | **Singapore** (registry). Marketed and staffed from Dubai/UAE. rwa.xyz separately names the issuer "Gold Issuance Inc.", an entity we could not locate in any register | High (registry) / Low (Gold Issuance Inc.) |
| Backing claim | 1 GOLD = 1 troy ounce of LBMA and UAE GD certified 99.99% physical gold, vaulted with Brinks | Medium (issuer assertion) |
| Chains | Solana only. SPL Token (legacy Token program), 6 decimals | High (on-chain) |
| Contract address | `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A` | High (on-chain) |
| Supply | **608.418838 GOLD = 608.42 troy oz** (~18.92 kg) | High (Solana RPC, 28 Jul 2026) |
| Market cap / TVL | **~$2.45M** at ~$4,033/oz. rwa.xyz shows $2,490,203 | High |
| On-chain liquidity | ~$736k in the main Meteora GOLD/USDC pool; ~$812k across all pools | High |
| 24h volume | ~$56.8k, of which sells ~$55.2k vs buys ~$1.6k | High |
| Holders | 9,732 (Jupiter) / 9,809 (rwa.xyz). Top holders ~61.85% | High |
| Regulatory status | **No licence found in any jurisdiction.** Not on MAS, VARA, ADGM FSRA, DFSA or Labuan FSA registers | High (negative search) |
| Subscription fee | 0.50% mint (1.00% off-hours) | High (issuer docs) |
| Ongoing custody fee | **Zero charged to holder.** Funded by the leasing spread and mint/redeem fees | Medium |
| Redemption fee | 0.50% (1.00% off-hours); **+1.5% for USDC settlement** | High (issuer docs) |
| Advertised yield | 3–4% APY on front page; docs say "typically in the 3 to 5% APY range"; requires a **12-month lockup** | High |
| Named officers | Usman Saleem (founder/CEO). **Juan Marchetto, co-founder and CTO: CONFIRMED but has since departed** | High |

---

## 1. What it is

ORO is a tokenized gold protocol on Solana. One GOLD token represents one troy ounce of certified physical gold. Its distinguishing pitch against PAXG and XAUT is that the gold is not merely parked: holders can stake GOLD into an institutional gold leasing programme and earn 3–4% APY paid in more GOLD, so the position compounds in metal rather than in fiat.

The operating company is Oro Labs PTE Ltd, a Singapore holding company. The product is marketed from Dubai, and the founder's contact details are UAE-based. It raised a $1.5M pre-seed in March 2025 led by 468 Capital with participation from Fasset ([Wamda](https://www.wamda.com/2025/03/oro-labs-secures-1-5-million-pre-seed-backed-468-capital), [Enterprise Times](https://www.enterprisetimes.co.uk/2025/03/17/oro-labs-raises-1-5-million-to-redefine-gold-markets/)).

It is small. 608 ounces, about 18.9 kg of gold, roughly $2.45M. For scale, that is one order of magnitude below PGOLD and three below PAXG. **Nearly ten thousand holders share 608 ounces**, an average of 0.0625 oz (~$252) each. This is a retail-distribution product with a retail-sized balance sheet, which makes it the closest structural analogue in this landscape to what Aurumix intends to build.

**Note on scope:** the brief flagged ORO / Oro Finance / ORO Labs / orogold.com / orogold.app / the rwa.xyz "Orogold" listing as one project. Confirmed, and there is now a further consolidation: **orogold.app 301-redirects to oro.finance**. The primary domain has moved.

---

## 2. Legal structure

This is the weakest documented part of the protocol and the part most relevant to Aurumix.

**What ORO asserts.** The docs state that "Legal title is held by a foundation, making the structure bankruptcy remote" ([audits page](https://orogold-1.gitbook.io/oro/8.-audits-and-security.md)), and name it the "**ORO Foundation**", describing holders as having "beneficial ownership of all underlying physical assets" via a trust structure, and GOLD as "a digital bearer instrument for ownership of real gold" ([legal page](https://orogold-1.gitbook.io/oro/7.-legal-risk-and-trust.md)).

**What can be verified: nothing.** The ORO Foundation is **not identifiable in any register we searched**: Cayman Islands General Registry, Panama Public Registry, ADGM, Labuan, Liechtenstein Stiftungsregister, and Singapore ACRA all return no match. **No jurisdiction is stated anywhere in ORO's own documentation.** No foundation charter, trust deed, or declaration of trust is published. The word "foundation" appears in the docs and in a Solana ecosystem article ([Solana](https://solana.com/news/tokenizing-gold-inside-oro-s-vertically-integrated-bet)) and nowhere else.

So the chain of title runs: holder → beneficial interest → a trust → a foundation that cannot be shown to exist. **"Bankruptcy-remote" is an unverifiable adjective here, not a documented structure.** Bankruptcy remoteness is a conclusion that follows from a specific entity in a specific jurisdiction with specific constitutional documents. None of the three is disclosed.

Compounding this: the terms disclaim issuance to unnamed "independent Third-Party Service Providers", and the docs simultaneously insist "$GOLD is not a security, derivative, or speculative token" and that ORO is "a non-custodial platform, not a bank, broker, or investment adviser": self-characterisations with no regulator having tested them.

**Confidence: Low** on the foundation existing as described. **Confidence: High** that it is not publicly identifiable.

---

## 3. Regulatory and compliance posture

**No licence found in any jurisdiction.** Checked and not found:

| Register | Result |
|---|---|
| MAS Financial Institutions Directory / PSA (DPT) lists, Singapore | Not found |
| Dubai VARA public register | Not found |
| ADGM FSRA public register | Not found |
| DFSA (DIFC) public register | Not found |
| **Labuan FSA licensed entities**, Malaysia | **Not found** |
| Labuan FSA unregulated/unauthorised warning list | Not found (also no adverse listing) |

**Contradiction flagged.** Secondary write-ups circulate the claim that "ORO's token is regulated by Labuan FSA". **This is refuted.** No entity named ORO, Oro Finance, Oro Labs or Orogold appears on any Labuan FSA licence category (money broking, credit token, digital asset exchange, or otherwise). Nor does Fasset. Anyone repeating "regulated by Labuan FSA" is repeating an unsourced secondary claim, and Aurumix should not treat ORO as a licensed precedent.

**ADGM.** ORO is reported to have signed a **Memorandum of Understanding** at ADGM regarding expanding tokenized gold adoption in the UAE. An MoU is not a licence, confers no authorisation, and no ADGM press release or register entry confirming it could be located. **Confidence: Low.**

**The KYC contradiction (material).** The docs state "Only KYC/KYB whitelisted wallets can mint, convert, and redeem" and "All redemption options are available only to KYC/KYB whitelisted wallets". But on-chain, **the mint's freeze authority is `null`**. There is no transfer restriction, no permissioning, no whitelist enforceable at the token layer. GOLD is a plain SPL token that anyone can buy on Jupiter or Meteora with no KYC whatsoever, and secondary coverage advertises exactly that ("swap into $GOLD on Jupiter and Meteora without KYC"). The gate exists only at the mint/redeem boundary with the issuer, not on the asset. This is a coherent design, but the documentation's phrasing invites the reader to believe the token is permissioned when it is not.

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | Brinks, asserted. "Brinks handles the physical vaulting, not Oro" | Medium (no custody agreement published) |
| Vault / city | **Not disclosed** | n/a |
| Allocated? | Implied by "1:1 backed" and trust framing, never stated as allocated and segregated | Low |
| Bar list | **Not disclosed.** No serial numbers, no weights, no refiner list | n/a |
| PoR feed | **None.** No on-chain proof-of-reserve oracle, no Chainlink PoR feed, no live reserve dashboard | High |
| Reserve attestation | RSM named. **No attestation document is published for download** | High |
| Smart contract audit | Cantina (Spearbit Labs Inc.), March 2026; Adevar Labs, April 2025. Both downloadable | High |

**The audit/attestation blur is present and it is severe.** The transparency page headline reads "Independently Verified Reserves", and the only two documents actually downloadable from it are **smart-contract security audits**. A smart-contract audit says the Solana program does what the code says. It says nothing whatsoever about whether 608 ounces of gold exist in a vault. A reader who skims "audited" draws precisely the wrong conclusion, which is the pattern the brief warns about.

**Frequency is also inconsistent across ORO's own surfaces**: the front page and transparency page say reserves are "verified **quarterly** by RSM"; the FAQ refers to "**monthly** audit reports from third-party vault and assurance providers"; and the Solana ecosystem article says "**Monthly** audits from RSM". Three different frequencies from the same issuer, with zero published documents to settle it. **Not disclosed** is the correct answer on ORO's actual reserve attestation, and that is a finding.

---

## 5. Issuance

Mint by swapping USDC in the app; GOLD is minted 1:1 minus a 0.50% fee (1.00% off-hours). Identity verification is required to mint: government ID plus liveness for individuals, business registration and signatory verification for entities. **No minimum purchase amount is stated** in the docs.

On-chain, the mint authority is `HKMT2i4kGzktb4AVo4fKkHK4AmpxVyvGEAfotVX3tML4`, a 45-byte non-executable PDA owned by program `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop`. So minting is program-controlled rather than sitting on a bare EOA, which is the better of the two designs, though the program's upgrade authority was not verified. Mint authority is **live** (not renounced), as it must be for an expandable gold token. Token created 27 April 2025; first liquidity pool 21 May 2025.

---

## 6. Redemption

Two routes, both **KYC/KYB whitelist-gated**:

| Route | Terms |
|---|---|
| To USDC | 0.50% redemption fee (1.00% off-hours) **plus ~1.5% USDC settlement charge**. Up to 48 hours. Price locked at request against live spot |
| To physical gold | Minimum increments of **1g**; typical formats 10g+, 100g, 1oz, 1kg bars. Delivery, insurance and a market premium over spot may apply, **quoted before confirmation, percentages not disclosed**. Typically 3–7 business days |

**Eligibility is restricted in two ways** worth flagging: redemption requires KYC/KYB whitelisting, and **physical pickup is currently available only in the UAE**. Redemption "may be unavailable in restricted jurisdictions", which are not enumerated. So a holder in, say, India, who bought GOLD KYC-free on Jupiter, has no assured physical exit.

**On the previously reported "~$85 increment with a 1-day lock": partly real, now stale.** Both figures trace to the **18 December 2024 launch press release**, which stated "Tokens can be redeemed for physical gold starting at $85 increments" ([GlobeNewswire](https://www.globenewswire.com/news-release/2024/12/18/2999238/0/en/ORO-Launches-as-First-App-Built-on-Fasset-s-L2-Network-Unlocking-1B-of-Tokenized-Gold-On-Chain.html)). That release predates the actual Solana launch. **Current documentation states 1g minimum increments, not $85** (1g is ~$130 at today's ~$4,033/oz). The "1-day lock" does not appear in the press release or in current docs. What current docs do specify is a **48-hour USDC processing window and a 12-month staking lockup**, which is a materially different and much longer commitment. Treat "$85 / 1-day" as **superseded**.

---

## 7. Fees and revenue model

| Fee line | Amount | Notes |
|---|---|---|
| Mint | 0.50% (1.00% off-hours) | |
| Redeem to gold or USDC | 0.50% (1.00% off-hours) | |
| USDC redemption settlement | 1.50% | Charged on top of the redemption fee |
| Ongoing custody / management | **Zero to the holder** | Not deducted in grams, not billed in cash |
| Staking | Free | 12-month lockup |
| Claiming yield | Free | |
| Unstaking after 12 months | Free | |

**Directly relevant to Aurumix design question 1.** ORO takes **option three**: it charges the holder no ongoing custody fee at all and recovers cost elsewhere. This preserves a clean 1 token = 1 ounce peg, exactly the property Aurumix needs (price = grams ÷ tokens breaks if you deduct in grams). ORO funds custody from (a) the spread on the leasing programme and (b) mint/redeem fees.

**Whether that arithmetic works at this size: it does not.** 608 oz at ~$4,033 is ~$2.45M of AUM. Allocated vaulted gold custody and insurance runs roughly 0.10–0.50%/yr, call it $2.5k–$12k. Against that, ORO must also pay a 3–5% yield to stakers, which requires the leasing programme to earn more than 3–5% gross. Institutional gold lease rates have historically sat well below that in normal conditions. At $2.45M of AUM, the entire fee base is trivial: even 1% round-trip on the full supply turning over once a year is ~$25k. **ORO's disclosed sources cannot fund a $1.5M-pre-seed operating team; the venture round is funding the operation, not the fee model.** That is survivable for a startup and unremarkable, but it means ORO is not yet evidence that a zero-custody-fee, yield-paying gold token is self-sustaining. Aurumix should not cite it as proof that the model closes.

---

## 8. Token architecture

- **Standard:** SPL Token, legacy Token program (`TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA`), **not** Token-2022. So **no transfer hooks, no confidential transfers, no permanent delegate, no transfer-fee extension.**
- **Decimals:** 6. With 1 token = 1 troy ounce, the smallest unit is 0.000001 oz (~$0.004), so fractional retail purchases are not constrained by precision.
- **Permissioned?** **No.** `freezeAuthority: null`. There is no whitelist, blacklist or transfer restriction at the token layer, despite the docs' KYC/whitelist language.
- **Mint authority:** live, held by PDA `HKMT2i4kGzktb4AVo4fKkHK4AmpxVyvGEAfotVX3tML4` under program `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop`.
- **Upgradeability / admin keys:** program upgrade authority **not disclosed** in docs and not verified here. This is the single most important unverified technical control.
- **Bridge:** none. Solana only.

**Directly relevant to Aurumix design question 3.** ORO chose the fully fungible, permissionless base. What that **buys** it is real DEX liquidity: it is quotable on Jupiter, poolable on Meteora, Orca and Raydium, and pairable against XAUt0 and GLDx. Roughly $812k of pooled liquidity against $2.45M of supply is a 33% liquidity-to-AUM ratio, which is dramatically healthier than PGOLD's ~2%. What it **costs** ORO is that every compliance claim in its documentation is unenforceable on the asset. Anyone can hold GOLD; ORO can only gate the mint and redeem doors. For Aurumix, whose ICS standing, dividend entitlement, credit eligibility and buyback rights all break on an anonymous DEX transfer, **ORO is a direct demonstration of the tradeoff**: it got liquidity precisely by giving up the control Aurumix cannot give up.

---

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Supply | 608.418838 oz |
| Price | ~$4,032.71 |
| Market cap / FDV | ~$2.45M |
| Pooled liquidity (all DEXs) | ~$812k |
| Main pool | Meteora GOLD/USDC, ~$736k liquidity, ~$54.8k 24h volume |
| Other pools | XAUt0/GOLD ~$70.5k (Meteora), GLDx/GOLD ~$3.2k, Orca XAUt0/GOLD ~$1.2k, plus dust pools |
| 24h volume | ~$56.8k total |
| Holders | ~9,732–9,809 |
| Top-holder concentration | ~61.85% |
| Jupiter organic score | **Low** |
| Jupiter tags | commodities, rwa, verified, moonshot-verified, community-assist |

**Directly relevant to Aurumix design question 6.** This is the most useful liquidity datapoint in the landscape, and it cuts **against** the client's premium thesis. ORO has a 33% liquidity-to-AUM ratio, sixteen times better than PGOLD's ~2%, and **it still does not produce a premium**. GOLD trades at ~$4,032–4,041 across pools while XAUt0 prints ~$4,079 in the paired pool: ORO is trading at a slight *discount* to another tokenized gold token, not a premium to spot. Volume is also one-directional: **~$55.2k of sells against ~$1.6k of buys in 24 hours**, roughly 34:1, with liquidity down 14.3% on the day.

The lesson for Aurumix: **liquidity depth does not manufacture a premium.** A well-arbitraged gold token converges to spot minus friction, because gold is the most efficiently arbitraged commodity on earth and any premium is immediately minted away by an issuer with a live mint authority. The 3–8% exchange premium Aurumix is banking on is not observable at either end of the liquidity spectrum: not in PGOLD's illiquid market, and not in ORO's liquid one. That is now two independent observations pointing the same way.

---

## 10. Distribution

- **Channels:** direct app (app.oro.finance), plus permissionless DEX access via Jupiter, Meteora, Orca, Raydium.
- **Target segments and geography:** the December 2024 launch material named UAE, Indonesia, Turkey, Malaysia, EU, Pakistan and India, with an explicit focus on **Muslim-majority markets** and Asia/Middle East. This overlaps Aurumix's India/UAE/NRI target almost exactly.
- **Referral / points:** yes. A "**Nuggets**" points programme rewards early users, and an airdrop is widely anticipated across airdrop-tracking sites. There is also a separate "Grail" product line (docs.grail.oro.finance) and an ecosystem page.
- **Savings plan / recurring purchase / SIP:** **Not disclosed.** No monthly contribution plan, no systematic investment feature, no agent or commission network.
- **Agent network:** none.

So ORO's retail growth engine is a **points-and-airdrop farm**, not a savings plan. That is the finding: it has assembled ~9,800 holders averaging $252 each, which is a genuinely retail distribution, but it did so with speculative airdrop incentives rather than recurring contributions. Points programmes produce holders who leave when the airdrop lands, which is a plausible reading of the 34:1 sell/buy ratio. **Aurumix's SIP plus 3-tier agent model remains unmatched by any protocol in this landscape.**

---

## 11. Recent developments

- **28 July 2026 (today):** on-chain state verified. Supply 608.418838 oz, ~$2.45M cap, ~9,732 holders, freeze authority null, mint authority live. 24h volume ~$56.8k skewed ~34:1 to sells; liquidity down 14.3% on the day.
- **~2026 (undated):** **orogold.app now 301-redirects to oro.finance.** Primary domain and brand consolidated onto oro.finance.
- **26 January 2026:** **Monetary Metals issued a public statement on the AgaBullion default.** Turkish authorities arrested principals at AgaBullion Kiymetli Madenler A.Ş. and affiliated Aleks Metal Refinery, and **some leased gold was seized**. Monetary Metals stated legal title remains with lessors, that it is working with Istanbul counsel and the US Consulate, and that it "carries supplemental insurance on leased metals and will file claims when and if appropriate" ([Monetary Metals](https://www.monetary-metals.com/about-us/newsroom/monetary-metals-statement-regarding-agabullion/)). **This is the live stress test of the exact structure ORO's yield depends on. See §12.**
- **March 2026:** Cantina (Spearbit Labs Inc.) smart-contract audit published.
- **May 2025:** Monetary Metals partnership announced. Confirmed by both parties in **marketing only**; no legal document names ORO.
- **21 May 2025:** first GOLD liquidity pool created on Solana.
- **27 April 2025:** GOLD mint created on Solana.
- **April 2025:** Adevar Labs smart-contract audit published.
- **17–18 March 2025:** $1.5M pre-seed led by 468 Capital, with participation from **Fasset** and angels from Phantom, Jupiter and Helium ([Wamda](https://www.wamda.com/2025/03/oro-labs-secures-1-5-million-pre-seed-backed-468-capital), [Enterprise Times](https://www.enterprisetimes.co.uk/2025/03/17/oro-labs-raises-1-5-million-to-redefine-gold-markets/)).
- **18 December 2024:** launch press release: "ORO Launches as First App Built on Fasset's L2 Network, Unlocking $1B of Tokenized Gold On-Chain" ([GlobeNewswire](https://www.globenewswire.com/news-release/2024/12/18/2999238/0/en/ORO-Launches-as-First-App-Built-on-Fasset-s-L2-Network-Unlocking-1B-of-Tokenized-Gold-On-Chain.html)).
- **22 August 2024:** Oro Labs PTE Ltd incorporated in Singapore, UEN 202434484G.

### Status of the previously reported Fasset "Own" L2 and $1B target: both STALE

**Both claims are real but obsolete, and the framing was wrong.** The 18 December 2024 press release announced ORO as "the first application built on Fasset's Ethereum Layer 2 network, Own", in partnership with "The Own Foundation", targeting "$1 billion of yield-bearing gold to be tokenized within the first year".

What actually happened: **ORO shipped on Solana, not on Own.** The mint was created on Solana on 27 April 2025, the docs state "$GOLD is an SPL token" and "built on Solana for speed, scale, and low fees", and there is no bridge and no deployment on Own or any EVM L2. Fasset's role has since been reported only as an **investor** in the March 2025 pre-seed, not as the host chain. No announcement of the Own deployment being cancelled was ever made; it was simply abandoned silently.

The **$1B first-year target** was set in December 2024. First year would have ended December 2025. **Actual result: ~$2.45M**, or about **0.245% of target**, and that is on a ~19-month clock rather than 12. This is a ~408x miss. "The Own Foundation" is likewise not locatable in any register.

Aurumix should treat this as a caution about the genre: tokenized gold launch press releases carry AUM targets that miss by two to three orders of magnitude, and the chain named at launch is frequently not the chain shipped.

### Co-founder "Juan Marchetto": CONFIRMED, and he has since left

**Verified, contradicting the assumption that this was unreliable.** The 18 December 2024 launch release states the company was "Founded in 2024 by Usman Saleem and Juan Marchetto", naming him **ORO Co-Founder**. His own GitHub profile independently confirms it: "At Oro.finance I designed and shipped a gold-backed stablecoin protocol on Solana as CTO, raised $1.5M" ([github.com/JuanMarchetto](https://github.com/JuanMarchetto)).

**But he has departed.** His profile lists Oro.finance under "Before" and states "Now: founding engineer at Nora Finance, building cross-border payment rails and stablecoin settlement in Rust". So **ORO's technical co-founder and CTO, the person who built the Solana protocol, has left for another company.** No departure announcement was made by ORO, and current ORO and press materials name only Usman Saleem, describing the company as "founded in 2024 by Usman Saleem" with Marchetto written out. Note also that most March 2025 funding coverage already omitted him.

**Confidence: High** that he was co-founder and CTO. **Confidence: Medium-High** that he has left (self-reported, uncontradicted, consistent with ORO's own current materials).

---

## 12. Relevance to Aurumix

ORO is the most instructive protocol in this landscape for Aurumix, because it is the only one attempting the same combination Aurumix is attempting: **retail-scale distribution, a yield on top of gold, and no custody fee charged to the holder.** It is also, on the single question Aurumix's dividend design hinges on, a cautionary tale.

**Design question 2 (dividend funding), the decisive finding.** Aurumix's central hope is that real external asset yield (gold leasing) is the compliant alternative to a fee-recycled dividend. ORO is the live test of that hope, and **the test result is that the legal plumbing does not exist**.

Nothing is published on how GOLD holders rank if a lease counterparty defaults. Specifically, and after direct searching:
- No Oro–Monetary Metals lease agreement, master lease or term sheet is published anywhere: **not found**.
- No subordination, security interest, collateral or priority provision naming GOLD holders: **not found**.
- No loss waterfall allocating a lessee default between token holder, ORO and Monetary Metals: **not found**.
- No Monetary Metals legal document names ORO at all. The partnership exists in marketing only.

ORO's docs assert the conclusion without the mechanism: "In case of lessee insolvency, leased gold is not part of their estate", the gold "legally remains your property even while leased", and "All gold under leases is insured against theft and damage". These are **assertions about a legal outcome with no published instrument creating it**, and they are made by ORO about a counterparty relationship ORO is not obviously a party to.

**The contrast that makes this concrete.** Monetary Metals *has* published a proper tokenized lease agreement, just not with ORO: the **Tokenized Yield Partnership Agreement with StreamEx, filed with the SEC** ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1530766/000164117225026853/ex10-1.htm)). It specifies that the lessee must maintain a jeweller's block policy at **≥110% of gold value**, with Monetary Metals as **loss payee and additional insured**, from an A-rated or better insurer. Monetary Metals separately describes requiring **corporate guarantees, UCC filings and sometimes personal guarantees** ([Monetary Metals](https://www.monetary-metals.com/how-we-protect-client-gold-and-silver/)). **So the standard of disclosure exists and is achievable. ORO simply has not met it.**

**And the risk is not theoretical.** On 26 January 2026 Monetary Metals disclosed the **AgaBullion** default: Turkish authorities arrested the lessee's principals and **seized some of the leased gold**. Monetary Metals' response was to assert that title remains with lessors, retain Istanbul counsel, approach the US Consulate, and consider insurance claims. That is a multi-year, cross-border, uncertain recovery. **"Legal title remains with the lessor" turns out to mean "we will litigate in Turkey", not "your gold is safe".** Note also the ordering: the loss payee on the lessee's insurance is Monetary Metals, not the token holder, so recovery proceeds flow to the platform first and reach the end holder only by whatever contract exists between them, which for ORO is unpublished.

**The direct implication for Aurumix's ICS Dividend:** if Aurumix funds its dividend from gold leasing to avoid the securities-classification risk of a fee-funded dividend, it inherits **lessee credit risk on the very gold that backs the token**, and it must publish the loss waterfall or it will be in ORO's position: promising a yield whose downside is undocumented. The encumbrance is real. Leased gold is gold that is not in the vault. Aurumix should decide explicitly whether a defaulting lessee's loss lands on (a) all holders pro rata, breaking the peg, (b) only stakers who opted in, or (c) the issuer's balance sheet, and should say so in writing before launch. **Publishing that waterfall would be genuine differentiation: neither ORO nor anyone else in this landscape has done it.**

**Design question 1 (custody fee): ORO validates the third option.** It charges holders nothing ongoing, preserving an exact 1 token = 1 oz peg, and funds custody from the leasing spread plus mint/redeem fees. This is the model Aurumix should copy in *structure*. But per §7 the arithmetic does not yet close at $2.45M of AUM: venture capital is subsidising it. Aurumix should adopt the mechanism and be honest internally that it needs scale (or a genuinely profitable adjacent revenue line, which for Aurumix is the credit facility and Gold Card) to fund it.

**Design question 3 (token standard): ORO is the counterfactual.** It runs a plain SPL token with **freeze authority null**, no permissioning at all. It thereby earns a 33% liquidity-to-AUM ratio and genuine DEX quotability, and pays for it by having every KYC claim in its docs be unenforceable on the asset. Aurumix cannot make this trade, because ICS standing, dividend entitlement, credit eligibility and buyback rights all die on an anonymous transfer. **ORO is the evidence for why Aurumix's ERC-3643-style permissioned base is the right call**, and simultaneously the evidence for what that will cost: expect materially thinner secondary liquidity than ORO's, and plan the buyback as the primary exit rather than hoping a DEX market appears.

**Design question 5 (redemption): ORO does what Aurumix refuses to do, and it is still geographically hollow.** ORO offers physical redemption from 1g, which sounds like a decisive advantage over Aurumix's cash-only buyback. But **physical pickup is available only in the UAE**, redemption requires KYC/KYB whitelisting, and delivery premiums are undisclosed until quoted. For ORO's actual holder base (Indonesia, Turkey, Malaysia, Pakistan, India) the physical option is largely notional. Aurumix's cash-buyback-only position is more honest than ORO's, provided Aurumix never claims physical redeemability. The reputational risk is in the mismatch, not in the absence.

**Design question 6 (premium): see §9.** ORO refutes the premium thesis from the liquid end, as PGOLD refutes it from the illiquid end. **Aurumix should stop treating a 3–8% exchange premium as a modelling input.** No tokenized gold token in this landscape sustains one, and structurally none can while the issuer holds a live mint authority.

**Design question 7 (proof of reserve): ORO is the anti-pattern to name.** "Independently Verified Reserves" as a headline, with two smart-contract audits as the only downloadable evidence, three mutually inconsistent attestation frequencies, no bar list, no PoR feed and no attestation document. Aurumix can beat this cheaply: publish one real attestation with a bar list, on a stated cadence, and it immediately out-discloses a venture-backed competitor.

**Design question 8 (distribution): unmatched.** ORO has no savings plan, no recurring purchase, no agent network. Its retail base came from a points-and-airdrop programme, which buys holders who sell on the unlock. Aurumix's SIP plus 3-tier agent network remains the genuine structural differentiator across this entire landscape.

**Design question 9 (wind-down): fails, and worse than most.** ORO documents nothing about what happens to the gold if the issuer fails. It gestures at a "bankruptcy-remote foundation" that **cannot be found in any register in any jurisdiction**, which is arguably weaker than saying nothing, because it invites reliance on a protection that cannot be verified to exist. Combined with the departure of the CTO who built the protocol, and a program upgrade authority that is not disclosed, ORO has key-person and key-control risk with no published contingency. **Aurumix committing ex ante to a named entity, a named jurisdiction, a published charter and a wind-down waterfall remains cheap, and remains unoccupied ground.**

---

## 13. Open items for verification

- [ ] Identify the ORO Foundation: obtain its jurisdiction, registration number and constitutional documents. Absent these, treat "bankruptcy-remote" as marketing and do not cite ORO as precedent for a foundation structure.
- [ ] Resolve "Gold Issuance Inc.", the issuer name rwa.xyz shows for the GOLD listing. It matches no entity we can find. Determine whether it is the missing issuing SPV, a data error, or a third entity in the stack.
- [ ] Obtain the Solana program upgrade authority for `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop` and determine whether it is a multisig, a single key, or immutable. This is the most important unverified technical control over the token.
- [ ] Request the RSM reserve attestation directly and establish its true frequency (quarterly per the front page, monthly per the FAQ and Solana article). Determine whether any attestation has ever been issued.
- [ ] Confirm whether Brinks has a written custody agreement with ORO or the Foundation, and whether gold is allocated and segregated or held on an unallocated basis.
- [ ] Obtain the ORO Terms of Use and Privacy Policy. The docs reference them; oro.finance/terms returned 404 at the time of research. Read the "independent Third-Party Service Providers" issuance clause in full.
- [ ] Establish whether ORO is a direct Monetary Metals client, a sub-participant, or merely a marketing partner. This determines whether GOLD holders have any contractual path to lease recovery proceeds at all.
- [ ] Track the AgaBullion recovery through 2026–27. It is the best available empirical read on what "legal title remains with the lessor" is actually worth in a cross-border seizure, and it directly prices the risk Aurumix would take on by funding a dividend from leasing.
- [ ] Confirm Juan Marchetto's departure date and whether any technical continuity plan exists at ORO.
- [ ] Verify whether the ADGM MoU exists as a document and what, if anything, it commits either party to.
- [ ] Monitor whether the anticipated "Nuggets" airdrop lands, and measure holder retention and the sell/buy ratio afterward. This is a free natural experiment on whether points-farmed retail holders persist, directly relevant to Aurumix's retention assumptions.

---

# WisdomTree Gold Token (WTGOLD)

> ⚠️ **Read this first: the brief's premise for this protocol is wrong, and the correction is the most valuable thing in this profile.**
>
> WTGOLD was assigned to us as "a transfer-agent-recorded fund share rather than a bearer custody receipt," on the theory that it is a regulated fund wrapper offering a third path against the ARVA-commodity-token route. **It is not.** WisdomTree runs **two structurally unrelated tokenised businesses** and the inherited framing has fused them:
>
> 1. **WT Gold (WTGOLD)** is a **bearer document of title** under **Articles 1, 2 and 7 of the New York UCC**, issued by a bailee. It is not a fund, not a security, not registered with the SEC, and has **no transfer agent**. It is, in legal substance, a **digital warehouse receipt**: closer to Comtech or Cache Gold than to anything in the fund world.
> 2. **WisdomTree Digital Funds** (WTGXX and ~14 siblings) *are* 1940 Act registered mutual funds whose shares are recorded by a registered transfer agent with a blockchain mirror. **None of them is a gold fund.** A full-text search of the entire 374,000-character WisdomTree Digital Trust prospectus returns **zero occurrences of the word "gold."**
>
> The transfer-agent-recorded-fund-share model the brief wants assessed **does exist and is genuinely the best answer in the landscape to the securities-classification problem**, but WisdomTree has deliberately **not** applied it to gold. Why it did not is the actual finding, and it is developed in §12.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | WTGOLD (marketed in-app as "Gold" / "Digital Gold") | High |
| Issuer (marketing) | "WisdomTree" / WisdomTree Prime | High |
| Issuer (legal, per User Agreement) | **WisdomTree Digital Trust Company, LLC ("WT TrustCo")** acts as **bailee and issuer of the document of title**; **WisdomTree Digital Movement, Inc.** is the Delaware counterparty operating the app | High |
| Ultimate parent | WisdomTree, Inc. (NYSE: WT), SEC CIK 0000880631 | High |
| Domicile | WT TrustCo: New York limited purpose trust company. WT Digital Movement: Delaware corporation. Both at 250 West 34th Street, 3rd Floor, New York, NY 10119 | High |
| Backing claim | 1 token = 1 troy ounce of LBMA Good Delivery gold, allocated and serial-numbered | High |
| **Legal wrapper** | **Electronic document of title under NY UCC Articles 1, 2 and 7. Bailment. NOT a fund, NOT a security** | High |
| **SEC registration** | **None. No registration and no exemption relied upon. Zero SEC filings of any kind mention "WisdomTree Gold Token"** | High |
| **Who records ownership** | **The blockchain itself, exclusively. There is no transfer agent and no book-entry official record** | High |
| Chains | Stellar (primary) and Ethereum | High |
| Contract address(es) | **Not disclosed** by the issuer. See §8: every on-chain asset named "WTGOLD"/"WisdomTree" that we could locate is a **spoof** | High |
| Supply | ~483 tokens (~483 oz) per RWA.xyz; issuer publishes no supply figure | Low |
| Market cap / TVL | ~$2.0M–$2.5M (RWA.xyz, figures inconsistent between snapshots) | Low |
| Regulatory status | NYDFS limited purpose trust charter granted **22 March 2024** to WT TrustCo; state money transmitter licences for the app | High |
| Subscription fee | 0% | Medium |
| Ongoing custody fee | **0%** to the holder | Medium |
| Redemption fee | **Greater of (i) the price of one troy ounce of gold, or (ii) 2% of the amount surrendered**, plus taxes and shipping | High |
| Advertised yield | **None.** WisdomTree advertises no yield on WTGOLD | High |
| Named officers | Jonathan Steinberg (CEO, WisdomTree, Inc.); Will Peck (Head of Digital Assets). No WT TrustCo officer list published | Medium |
| Wind-down plan | **Not disclosed** as a plan, but a **Substitute Bailee** mechanism exists (§2) | High |

---

## 1. What it is

WTGOLD ("WT Gold") is a token on Stellar and Ethereum, each unit representing one troy ounce of LBMA Good Delivery gold held at HSBC Bank plc in London. It is sold to US retail consumers through the **WisdomTree Prime** mobile app, and is one of several "WT Digital Assets" alongside WT Dollar (a dollar token) and hosted crypto.

It launched **22 September 2022** (RWA.xyz) and remains available as of July 2026.

The framing that matters: WisdomTree is a $150bn+ AUM NYSE-listed asset manager that has built a genuinely sophisticated tokenised-fund business. WTGOLD is **not part of it**. WTGOLD sits in the separate, much smaller consumer wallet business. At roughly $2M it is a rounding error against WisdomTree's ~$770M of tokenised AUM, and a vanishing one against the parent's $150bn. This asymmetry is itself analytically important (§12).

## 2. Legal structure

**Confidence: High.** This is from the operative contract, the WisdomTree Prime User Agreement, last updated **31 March 2026** (https://dataspanapi.wisdomtree.com/pdr/documents/USER_AGREEMENT/WDM/US/EN-US/PRIME/).

The holder owns an **electronic document of title**, and the agreement says so in terms. Section 9:

> "User agrees that WT Gold and any other WT Digital Asset so designated on the Digital Assets Schedule represent an 'electronic document of title' to LBMA Gold or the other goods designated on the Digital Assets Schedule, as the case may be, for purposes of Articles 1, 2 and 7 of the New York Uniform Commercial Code as in effect from time to time (the 'UCC')."

The definition at §1(m) is equally explicit:

> "'WT Gold' means a digital token recorded on a blockchain (e.g., the Stellar blockchain or other supported blockchains) representing an electronic document of title to and ownership of one-troy ounce of physical gold meeting the good delivery requirements set by the London Bullion Market Association ('LBMA Gold')."

Note the phrase **"and ownership of."** This is stronger than most tokens in the set. The holder is asserted to own the gold, not merely to hold a claim against the issuer.

The bailment relationship is named. Section 9(j):

> "WT TrustCo acts as the bailee which issued the electronic document of title."

And critically, §9(d):

> "User is the bearer and holder of the electronic documents of title represented by the WT Digital Assets held in User's Wallet."

**This is a bearer instrument.** The gitbook gloss describes it as "a contract with, not an interest in, the bailee" (https://wisdomtree.gitbook.io/wisdomtree-gold-token), which is the classic bailment formulation: the bailee never takes title, so the goods are not the bailee's property and in principle are not available to the bailee's general creditors.

**Substitute Bailee clause.** §9(j) continues:

> "User further agrees that WT TrustCo may transfer its obligations with respect to WT Digital Assets and substitute as bailee a direct or indirect affiliate of WT TrustCo (a 'Substitute Bailee'). WT TrustCo covenants that the Substitute Bailee will be duly authorized and licensed to act as bailee for such WT Digital Assets and as the issuer of the electronic document of title represented thereby. User consents to such substitution and agrees that, upon notice thereof at the WisdomTreePrime.com website, User will look solely to the Substitute Bailee for the transfer or delivery of LBMA Gold."

So the bailee can be swapped for an affiliate, by website notice, without holder consent, and the holder's recourse then runs **solely** to the substitute. This is the nearest thing to a wind-down provision in the document (§12, question 9), and it is a continuity mechanism rather than a liquidation plan.

**Note the deliberate contrast within the same contract.** §10 is titled "Security Entitlements" and applies **Article 8** of the UCC, treating hosted **crypto** (BTC, ETH) as "financial assets" credited to a "securities account" with WisdomTree Digital as "securities intermediary." WT Gold is expressly **not** in §10: it is in §9, under **Article 7**. WisdomTree's lawyers drew an explicit line between an Article 8 intermediated security entitlement and an Article 7 bearer document of title, and put gold on the Article 7 side. That is a considered choice, not an accident.

**What a WT Digital Fund holder owns, by contrast** (relevant because this is what the brief thought WTGOLD was): a share of beneficial interest in a Delaware statutory trust series registered under the 1940 Act, recorded by a registered transfer agent. Entirely different instrument. See §12.

## 3. Regulatory and compliance posture

**Confidence: High on what exists, High on the negatives (we checked and they are absent).**

| Item | Finding |
|---|---|
| NYDFS limited purpose trust charter | **Granted 22 March 2024** to WisdomTree Digital Trust Company, LLC. Permits digital asset custody and stablecoin issuance, and allowed Prime to launch in New York. (https://www.businesswire.com/news/home/20240322928015/en/) |
| NYDFS charter number | **Not disclosed** in any source we located |
| State money transmitter licences | Asserted. User Agreement §23(j): "WisdomTree maintains certain licenses to engage in money transmission activities as set forth in the WisdomTree State License Disclosure, available at www.wisdomtreeprime.com/disclosures." **The disclosure page returned HTTP 403 to us and we could not read the licence list.** Specific state list and NMLS numbers: **Not disclosed** to us |
| SEC registration of WTGOLD | **None.** No registration statement, no exemption claimed |
| SEC exemption relied on for WTGOLD | **None claimed.** The token document states "Gold Tokens and this document have not been registered pursuant the securities or commodity laws of any country" |
| EDGAR full-text search, "WisdomTree Gold Token" | **0 hits, all form types, all dates.** Verified directly against efts.sec.gov |
| EDGAR full-text search, "Gold Digital Fund" | **0 hits** |
| CFTC registration | **Not disclosed / none found** |
| Broker-dealer | WisdomTree Securities, Inc. is an SEC-registered broker-dealer, but it is involved **only** in WT Digital Fund Share transactions (User Agreement §8), **not** in WT Gold. CRD number **not disclosed** in the product documents |

**The compliance logic is coherent and worth stating plainly.** WisdomTree did not obtain a securities exemption for WTGOLD because on its own analysis **it does not need one**: a document of title to a physical commodity is not a security. The regulatory perimeter it does occupy is the **money transmission / virtual currency** perimeter (NYDFS trust charter plus state MTLs), which is the perimeter for holding customer assets and moving value, not for issuing investment products.

This is the same "it's a commodity, not a security" position that Aurumix's ARVA route takes. **WisdomTree, with a large US legal budget and a public listing to protect, reached the same conclusion Aurumix has.** That is meaningful supporting evidence, and it is the opposite of what the brief expected to find.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian | **HSBC Bank plc** | High |
| Vault / city | **London** | High |
| Allocated? | **Yes, asserted.** "HSBC has contractually committed to maintain a continuous allocation (i.e., segregation) process whereby each gold bar associated with a Gold Token is segregated within the gold custodian's vaults with a serial number in accordance with LBMA's good delivery standards" (https://wisdomtree.gitbook.io/wisdomtree-gold-token) | Medium (issuer assertion; the HSBC agreement is not published) |
| Published bar list | **Not disclosed.** We looked and found none | High |
| PoR feed | **Not disclosed.** No Chainlink or equivalent proof-of-reserve oracle found | High |
| **Reserve attestation** | **Not disclosed.** No periodic independent attestation of the gold, no named auditor, no frequency, no report. The gitbook has a page titled "Independent Audits" but we could not retrieve any actual attestation document from it | High |
| **Smart contract audit** | **Not disclosed.** No auditor, no report | High |

**Applying the wave-1 rule (§152 of the brief) explicitly: for WTGOLD we found neither a reserve attestation nor a smart-contract audit.** The gitbook's "Independent Audits" heading is exactly the kind of language that a skimming reader converts into "audited." There is nothing behind it that we could retrieve.

**However.** The materiality of this gap is lower here than for any other protocol in the set, for a reason that does not apply elsewhere: **the parent is an SEC-reporting NYSE-listed company** whose consolidated financial statements are audited annually and whose 10-K describes the Prime business. And the custodian is HSBC, not an unnamed vault operator. The risk is not "does the gold exist"; it is "the holder has no independent, contemporaneous, per-token way to verify it," which is a transparency failure rather than a solvency signal. Distinguish those two things when this profile is read.

## 5. Issuance

Purchase is **exclusively inside the WisdomTree Prime app**, US retail, after KYC/AML ("Verification Procedures," User Agreement §1(g)). Funding is by USD from a linked external account, converted to **WT Dollars** (WisdomTree's own dollar token), which are then used to buy WT Gold. Approved third-party stablecoins can also fund the wallet (§7(b)).

The token is divisible: §9(h) allows a User to "subdivide a WT Digital Asset into smaller denominations," so retail can buy fractional ounces despite the 1-token-1-ounce definition. Minimum purchase: **Not disclosed** to us.

There is no public mint, no primary market for institutions, no authorised participant structure. Contrast this with essentially every other token in the set.

## 6. Redemption

**This is one of only two protocols in the set where we can quote the physical redemption terms verbatim from the operative contract.** User Agreement §5(h).

**Requirements**, §5(h)(i):
1. User must hold **a minimum of one (1) full ounce** of WT Gold.
2. Contact WisdomTree Digital Customer Support during business hours, 9am–9pm EST.
3. Submit a completed **WT Gold Retrieval Form** to DAOps@wisdomtree.com.
4. Identity and delivery address verified by WisdomTree Digital.
5. Accept the terms of the independent **"Metal Agent"** facilitating delivery.
6. Agree to pay all applicable fees, taxes and shipping.

Residual value below a whole ounce is returned as **WT Dollars** at the LBMA price at the time of retrieval, not as metal.

**Fees**, §5(h)(ii), quoted exactly:

> "In connection with retrieving LBMA Gold by surrendering WT Gold, User agrees to pay WisdomTree Digital a fee, as required by the Metal Agent, of the greater of: (i) the price of one-troy ounce of LBMA Gold; or (ii) 2% of the total value of WT Gold to be surrendered."

**Read that carefully, because it is severe and it is easy to misread.** The floor is not 2%. The floor is **the entire price of one ounce of gold**, roughly $2,400 or more at current prices. The 2% only becomes the binding term once the redemption exceeds **50 ounces**, because 2% of 50 oz = 1 oz.

So the effective redemption cost curve is:

| Redemption size | Fee | Effective cost |
|---|---|---|
| 1 oz (the minimum) | 1 oz | **100%** |
| 2 oz | 1 oz | 50% |
| 5 oz | 1 oz | 20% |
| 10 oz | 1 oz | 10% |
| 25 oz | 1 oz | 4% |
| **50 oz** | 1 oz | **2% (crossover)** |
| 100 oz+ | 2% | 2% |

**A retail holder redeeming the one-ounce minimum surrenders one ounce and pays one ounce, and receives nothing.** Physical redemption is nominally universal (no "qualified holder" gate, which is a genuine plus against the eligibility trap the brief flags in question 5), but it is **economically unavailable below roughly 10–25 ounces**, i.e. $24,000–$60,000. For a retail savings product, that is redemption in name only.

This is worth stating in the assembled document as a general pattern: **"universal eligibility, prohibitive economics" is a functionally equivalent substitute for "qualified holders only," and it reads better in marketing.**

Note also §5(g): tokens surrendered for exchange are **immediately cancelled** and "User will not be entitled to return of any WT Digital Assets so transferred for exchange and cancellation."

## 7. Fees and revenue model

| Fee line | Amount | Source / confidence |
|---|---|---|
| Subscription / minting | 0% | RWA.xyz. Medium |
| **Ongoing custody / storage / management** | **0% to the holder** | RWA.xyz lists 0% management, 0% performance. No storage fee found in the User Agreement. Medium |
| Buy/sell spread in-app | **Not disclosed.** No numeric spread published anywhere we looked | High (that it is undisclosed) |
| **Physical redemption** | **Greater of 1 oz of gold or 2%**, plus taxes and shipping | High (contract) |
| On-chain transfer out | Pass-through of gas plus a WisdomTree fee "designed to cover" network costs, disclosed pre-trade (§7(d)) | High |
| Fee change notice | **48 hours by email** (§6). WisdomTree may update the Digital Assets Schedule at its discretion, prospectively | High |
| Dormancy | Reserved right to "deduct an administrative fee" on unclaimed property escheatment (§23) | High |

**What funds the zero custody fee (brief question 1).** Three answers, and only the third is durable:

1. **The undisclosed buy/sell spread.** This is almost certainly the primary revenue line, and the fact that it is nowhere published is the single biggest disclosure gap in the product.
2. **Float on WT Dollars.** WT TrustCo holds the WT Dollar reserve in T-bills, reverse repo, government MMFs and bank deposits (§11(b)). Users must convert USD to WT Dollars to buy gold, so gold purchases generate dollar-token float, and at 2026 rates that float earns real money. **The gold is loss-leading for the dollar token.**
3. **Strategic subsidy from a $150bn parent.** WisdomTree can run a $2M gold product at a loss indefinitely because it is a customer-acquisition and optionality play for the tokenised-fund business, which is the actual strategy.

**Reason 3 is the one Aurumix cannot replicate, and it is the reason the zero-fee norm is a trap.** Eight protocols now show zero ongoing custody fee, but for PAXG/XAUT it is funded by billions in float, and for WisdomTree it is funded by a listed parent's strategic budget. Aurumix has neither. Recording "the norm is zero" without recording "and here is the balance sheet that pays for it" would be the wrong lesson.

**No dilutive or in-kind fee mechanism.** Unlike PAXG (brief §144), WisdomTree reserves **no** right to take fees by minting tokens to itself. Nothing analogous found.

## 8. Token architecture

- **Chains:** Stellar (primary) and Ethereum. Stellar is the native issuance chain.
- **Standard:** Stellar native asset (not ERC-20 on the primary chain). Stellar assets carry issuer-level **authorization flags**, which give the issuer permissioning and clawback capability at the protocol level without a custom token standard. This is the functional equivalent of ERC-3643 permissioning, obtained for free from the ledger design.
- **Permissioned:** **Yes, effectively.** User Agreement §7(a) and §8(e) restrict on-chain transfers to wallets "registered with WisdomTree," and §7(e) reserves the right to "suspend, cancel, reject or delay any Onchain Transfer." A holder cannot freely send WTGOLD to an arbitrary address.
- **Upgradeability / admin keys:** **Not disclosed.**
- **Bridge:** Stellar↔Ethereum mechanism **Not disclosed.**

**🔴 Contract addresses: not disclosed by the issuer, and the on-chain namespace is populated by impostors.**

We attempted direct on-chain verification. WisdomTree publishes **no** contract or issuer address in its token document, gitbook, or User Agreement, and serves **no** `stellar.toml` at wisdomtreeprime.com, wisdomtree.com or www.wisdomtree.com (all 404). Absent a `stellar.toml`, there is **no cryptographic way for a holder to verify which Stellar issuer account is genuinely WisdomTree's.**

What is in that vacuum, verified by us against Horizon and stellar.expert on 28 July 2026:

- Two Stellar assets with code `WTGOLD` exist. The larger, issuer `GBSCY7XCPOJEUGRQU77SIXYNXCOUKF33EZ7L27W2XXZXSS6N667N7E37`, has **home_domain `wisdomtree.xlmhq.org`** (not a WisdomTree domain), supply 1,511,450,381 units, **4 trustlines and 4 payments**, and **all authorization flags set to false** (no `auth_required`, no `auth_revocable`, no clawback). A genuine regulated bailee issuing a permissioned document of title would not leave those flags off.
- A broader search for "wisdomtree" on Stellar returns a **cluster of spoofed assets** on domains including `wisdomtree.com.co`, `wisdomtree.bond`, `cadence.wisdomtree-stellar.com`, `micron.wisdomtree-stellar.com`, `globaltoken-stellar.com` and `stocks.kraken.com.bz`, impersonating real WisdomTree ETF tickers (DXJ, DFJ, WTMF, AIVL, NTSE, QSIG) with absurd supplies (1.8 quadrillion units).
- Also worth flagging: **the Stellar issuer address supplied to us by Perplexity, `GBKKR9J5DOEBVHO4CEB5NQRUGNMLFJOPBY57DDYZLQZKSSJTZ3OI4SYZ`, does not exist on Stellar mainnet.** Horizon returns no account. It was fabricated with a confident inline citation. This is a live example of why the brief's citation rule exists, and it should be treated as a caution for the whole research pass: **on-chain claims must be verified on-chain, not accepted from a language model.**

**Conclusion for §8: we could not identify a genuine WTGOLD contract address from any source, and everything findable on-chain under that name appears fraudulent.** For a bearer document of title whose entire legal theory rests on §9(e) of the User Agreement, that the blockchain "will be the exclusive means of delivering and determining who has control," this is a serious gap: the issuer has made the ledger legally dispositive while publishing nothing that lets a holder identify the correct ledger entry.

## 9. Liquidity and market

Per the wave-1 addendum, one paragraph, no re-argument.

WTGOLD has **AUM of roughly $2.0M–$2.5M** (RWA.xyz reports ~483 tokens and a total asset value of ~$1.97M in one snapshot and a NAV of ~$2.52M in another; the inconsistency is unresolved and the issuer publishes nothing), across **~660 holder addresses**. **On-chain liquidity and daily volume are effectively zero, and not because the market is thin but because there is no market at all:** WTGOLD has no DEX pool, no CEX listing, and no secondary venue. It is buyable and sellable **only inside the WisdomTree Prime app, against WisdomTree as principal, at a spread WisdomTree does not publish.** Price is therefore administered, not discovered, and the question of a premium to spot does not arise: there is no independent market to express one. WTGOLD is the **limiting case** of the settled wave-1 conclusion. Where PGOLD showed an illiquid market with no premium, WTGOLD shows that a fully closed-loop distribution model removes the premium question entirely, at the cost of removing price discovery too.

## 10. Distribution

- **Channel:** single, proprietary, closed. The WisdomTree Prime mobile app (iOS/Android). No exchange listings, no broker distribution, no B2B API for gold.
- **Segment:** US retail consumers.
- **Geography:** US only. State availability is gated by money transmitter licensing; the specific included/excluded state list is **Not disclosed** to us (the disclosures page 403'd). Non-US eligibility: **Not disclosed**.
- **Savings plan / recurring purchase / SIP:** **Not disclosed / none found.** No monthly contribution feature documented for WTGOLD.
- **Referral / affiliate / agent network / commission tiers:** **None found.** As a US-regulated entity, a multi-tier commission structure of the kind Aurumix plans would raise broker-dealer registration questions that WisdomTree has clearly avoided.
- **Distinctive feature:** the **"gold you can spend"** thesis. WisdomTree's own token document is subtitled "DRIVING TOWARD GOLD YOU CAN SPEND," and coverage of the NYDFS charter referenced a Visa card letting customers "pay for coffee with digital gold tokens." WTGOLD's differentiation is payments utility, not yield and not savings discipline.

**Answer to brief question 8: WTGOLD has no savings-plan, recurring-purchase, referral or affiliate mechanism whatsoever.** It is another data point for the finding that this is Aurumix's genuinely uncontested ground.

## 11. Recent developments

Dated, reverse chronological. Sweep run 28 July 2026.

- **24 July 2026** WisdomTree Digital Trust files Form 485BXT (new effective date for a post-effective amendment), the most recent of a continuous 2026 stream of fund registration activity. The **fund** business is in active expansion. (EDGAR CIK 0001859001)
- **~Q2 2026** WisdomTree reports **tokenised AUM of ~$770M**, described as a 25-fold increase since 2024, with the digital asset business characterised as a core business nearing profitability. (https://finance.yahoo.com/news/wisdomtree-firm-150-billion-assets-234020262.html)
- **23 February 2026** **SEC grants exemptive relief**, Investment Company Act Release No. **35968**, File No. **812-15788**, to WisdomTree Digital Trust, WisdomTree Securities Inc., WisdomTree Digital Management Inc. and **WisdomTree Transfers, Inc.** Order under **sections 6(c) and 17(d)** and rule 17d-1, exempting from **section 22(d) and rule 22c-1** to permit affiliated dealers to transact **WisdomTree Government Money Market Digital Fund** shares on a **principal basis at a stable $1.00 per share** rather than next-calculated NAV. Application filed 8 May 2025, amended 16 January 2026. (https://www.sec.gov/files/rules/ic/2026/ic-35968.pdf) **This is the single most important regulatory event in WisdomTree's tokenised business and it concerns funds, not gold.**
- **28 January 2026** Notice of the above application published in the Federal Register. (https://www.federalregister.gov/documents/2026/01/28/2026-01691/)
- **26 January 2026** SEC issues notice of filing, Investment Company Act Release No. 35912.
- **3 February 2026** Jonathan Steinberg states at the Ondo Summit that the digital asset business is "in line of sight" of profitability, that WTGXX launched in 2023, and that WisdomTree now has **14 tokenized funds**. (https://www.marketsmedia.com/wisdomtree-digital-asset-business-near-profitability/)
- **December 2025** Launch of the **WisdomTree Equity Premium Income Digital Fund**, distributed to retail via Prime and to institutions via Connect.
- **3 June 2025** WisdomTree wins "Best Digital Asset Processing Solution" for its blockchain-enabled transfer agent. The award citation notes **WisdomTree Transfers maintains transfer agent functions across WisdomTree Prime and WisdomTree Connect with over $241 million of tokenized AUM**, with records "held in both traditional book-entry form and digitized on the Ethereum, Arbitrum, Avalanche, Base and Optimism blockchains." (https://ir.wisdomtree.com/news-events/press-releases/detail/737/)
- **31 March 2026** WisdomTree Prime User Agreement last updated (the version quoted throughout this profile).
- **22 March 2024** **NYDFS grants WisdomTree Digital Trust Company, LLC a New York limited purpose trust company charter**, enabling digital asset custody, the WisdomTree Dollar Token, and the launch of Prime in New York. (https://www.businesswire.com/news/home/20240322928015/en/)
- **22 September 2022** WTGOLD inception (RWA.xyz).

**Status check.** WTGOLD is **not** discontinued and remains purchasable as of July 2026; the Prime app still markets "Digital Gold." But note the shape of this timeline: **every dated development since 2024 concerns the funds, the transfer agent, the stablecoin or the platform. There is not one WTGOLD-specific announcement in 18 months.** No new chains, no new features, no attestation, no partnership, no AUM milestone. Against a fund business that went 25x, the gold token is static at ~$2M. This looks like a **maintained legacy product, not an invested one** and it is the early-stage signature of exactly the **PMGT commercial-abandonment pattern** the brief tells us to test for (zero holder revenue means no internal advocate). WisdomTree differs from Perth Mint in that it has an unrelated strategic reason to keep the product alive (payments optionality, brand), but the revenue logic is the same.

**No enforcement actions, incidents, outages or breaches** concerning WisdomTree's digital asset business were found in the sweep window. That is a clean record and, in this set, unusual.

## 12. Relevance to Aurumix

**This is the section the assignment turns on, and the answer inverts the question.**

### 12.1 The premise correction, and why it still matters

The brief asked us to assess "a regulated fund wrapper with tokenised share records" as a third path against the ARVA-commodity-token route, on the belief that WTGOLD is one. **WTGOLD is not a fund and has no transfer agent.** But the model is real, WisdomTree operates it, and it is worth assessing properly, because the *fact that WisdomTree did not use it for gold* is more informative than a hypothetical assessment would have been.

**The two structures, side by side:**

| | **WT Gold (WTGOLD)** | **WT Digital Funds (WTGXX et al.)** |
|---|---|---|
| Legal wrapper | Electronic document of title, NY UCC Art. 1/2/7 | Series of a Delaware statutory trust, shares of beneficial interest |
| Is it a security? | **No** (issuer's position) | **Yes**, expressly |
| SEC registration | **None** | **1940 Act File No. 811-23659; 1933 Act File No. 333-255575** |
| Who records ownership | **The blockchain, exclusively** | **WisdomTree Transfers, Inc.**, SEC-registered transfer agent |
| Authoritative record | The ledger (User Agreement §9(e)) | **The book-entry record.** Blockchain is secondary |
| Underlying asset | Physical gold at HSBC | Securities |
| Investor protections | Contract and bailment law | 1940 Act: board oversight, custody rules, daily NAV, prospectus |
| Ongoing fee | 0% | **0.44%** management fee (Equity Premium Income Digital Fund) |
| Distribution | Proprietary app only | Prime (retail) + Connect (institutional) + broker-dealer |
| Exemptive relief | None | **6(c), 17(d), rule 17d-1** (Release 35968) |

### 12.2 The record-authority clause, and what it costs

The brief asked what it means that ownership is recorded on the transfer agent's books with the blockchain as a secondary record. On the fund side, this is answered verbatim in the WisdomTree Digital Trust prospectus (filed 13 November 2025, https://www.sec.gov/Archives/edgar/data/1859001/000121465925016424/wtd111225485bpos.htm):

> "WisdomTree Transfers, Inc., the Fund's transfer agent ('WisdomTree Transfers' or 'Transfer Agent'), maintains the official record of share ownership through an integrated recordkeeping system with records in book-entry form and digital representations of Fund shares that are recorded – or tokenized – on the applicable blockchain. A transfer of the record on the blockchain can act as an information source for the Transfer Agent to register a transaction in its book-entry records. The Transfer Agent will reconcile book-entry and blockchain transactions on at least a daily basis... **The Transfer Agent's book-entry records constitute the official record of share ownership.**"

The User Agreement §8(b) says the same to consumers, defining the book-entry record as the "**Official Record**."

**Read the direction of authority.** The blockchain "can act as an **information source**" for the transfer agent. The transfer agent's book **is** the record. **The token is a mirror, not the asset.** If the two disagree, the book wins and the token is corrected.

**This solves the securities-classification problem completely, and the price is the entire premise of a token.** You get a fully regulated, unambiguously legal instrument, and in exchange:

- The token cannot be a bearer instrument. Possession of the token is not ownership.
- Transfers must be to wallets known to the transfer agent, which must reconcile them into the book. Permissionless transfer is impossible **by legal design**, not by technical choice.
- Every holder must be a KYC'd shareholder of record.
- You inherit the full 1940 Act cost base: board, independent trustees, daily NAV, prospectus, annual audit, CCO, exemptive applications taking (in WisdomTree's case) **9.5 months from filing to order**.

**And decisively for Aurumix: the 1940 Act path is not available for a gold product at all.** A vehicle holding physical gold is not an investment company under the 1940 Act (gold is not a security), which is precisely why US physical gold ETFs such as GLD are **1933 Act grantor trusts** with no 1940 Act registration and no 1940 Act protections. So "become a registered fund" is not a route Aurumix could take for a gold-backed savings product even if it wanted the cost base.

**This is why WisdomTree, which owns a registered transfer agent, a broker-dealer, a fund adviser and a registered trust, still structured its gold product as a UCC Article 7 document of title.** Not oversight. The fund wrapper does not fit gold. **The "third path" the brief hoped for does not exist for this asset class**, and a firm with every possible incentive and capability to find it did not.

### 12.3 The finding that actually helps: WisdomTree independently validates the commodity-token route

Strip away the wrapper confusion and this is what is left, and it is genuinely useful:

**A NYSE-listed, SEC-reporting, NYDFS-chartered US asset manager with $150bn AUM, in the most litigious securities jurisdiction on earth, structured its retail gold token as a non-security document of title to a physical commodity, and did not register it with the SEC or claim any exemption.**

That is the strongest available third-party validation of Aurumix's core thesis that **a pure gold-backed token is not a security**. It is worth more than any of the offshore precedents in the set, because WisdomTree has a public share price, an audit committee and a legal budget that make an aggressive position unaffordable.

**But note precisely what is validated: the bare gold core, and nothing else.** WisdomTree's product pays **no yield**, has **no dividend**, offers **no credit facility**, has **no tiered allocation system** and **no agent network**. It is the clean case. Every feature Aurumix layers on top (ICS, ICS Dividend, Gold Card, credit at 90–95% LTV) is a feature WisdomTree does **not** have, and the difference is not capability. WisdomTree could build any of it in a quarter. **It chose the clean commodity perimeter and stayed inside it.**

That is the shape of the warning. WisdomTree's structure is evidence **for** the ARVA gold core and evidence **against** the hybrid. It tells Aurumix that the base layer is defensible and that the superstructure is where the classification risk actually lives, which is what the brief already suspected (question 4) and now has a serious precedent for.

### 12.4 The instrument-split question (wave-1 live lead)

The brief flags Kinesis's split (clean asset token + separately capped security, KVT) as the leading structural answer to hybrid regulation, and asks whether other protocols separate a yield or governance instrument from the asset token.

**WisdomTree does separate its instruments, and more cleanly than Kinesis, but it is not the same manoeuvre.** WisdomTree runs the **non-security gold document of title** and the **registered fund shares** as entirely distinct instruments with distinct legal wrappers, distinct regulators, distinct record-keeping systems and distinct distribution rails, side by side in one app. A user can hold both in one wallet, and the wrapper never blends.

The lesson for Aurumix is architectural rather than legal: **the app can be unified while the instruments stay legally severed.** A single retail experience does not require a single legal object. If Aurumix wants a savings core plus a yield instrument, the WisdomTree pattern says put them in different legal wrappers under different licences and unify them only in the UX layer. Kinesis says the same thing from a different starting point. **Two independent protocols now converge on instrument separation, which materially strengthens it as our recommended answer.**

### 12.5 Direct answers to the nine design questions

1. **Custody fee.** 0% to the holder. Funded by an **undisclosed in-app spread**, by float on the WT Dollar reserve (T-bills, repo, MMFs, deposits), and ultimately by strategic subsidy from a $150bn listed parent. **No dilutive or in-kind fee mechanism**, and no reserved right to introduce one. Aurumix cannot copy the funding model; the fee level is only meaningful alongside the balance sheet behind it.
2. **Dividend funding.** **WTGOLD pays no yield of any kind.** WisdomTree, holding allocated gold at HSBC and possessing every capability to run a lending programme, **does not lease the gold and pays holders nothing.** For the client's dividend problem this is a negative data point of real weight: the most conservatively regulated issuer in the set looked at yield on gold and declined. No contradiction to the Streamex lead (§141), but no support for it either.
3. **Token standard.** Stellar native asset with issuer-level authorization flags, plus Ethereum. **Permissioned by contract** (transfers only to WisdomTree-registered wallets, §7(a)/§8(e), with a reserved right to block). Relevant to Aurumix's ERC-3643 lean: WisdomTree gets equivalent permissioning from Stellar's built-in flags rather than a specialised standard, which is cheaper. But note the cost it accepted: **zero external liquidity**, because a permissioned token with no venue is a closed loop. That is the honest price of the ERC-3643 route and Aurumix should price it in.
4. **Regulatory route.** **NYDFS limited purpose trust charter, granted 22 March 2024**, plus state money transmitter licences. **Not a securities licence.** The perimeter is custody and value transfer, not investment products. The structural read-across is that a **trust-company charter, not a securities licence, is the natural home for a gold custody token** and the same logic supports the VARA/ARVA framing for the Aurumix core.
5. **Redemption.** Physical redemption exists, is **not** gated to "qualified holders" (good), 1 oz minimum, but costs **the greater of 1 oz or 2%**, which is **100% of value at the minimum** and only reaches 2% above 50 oz. **Universal eligibility with prohibitive economics.** Aurumix's honest "no physical redemption" is arguably a better disclosure posture than a redemption right that cannot rationally be exercised by the customers it is offered to, and this comparison is worth making explicitly in client materials.
6. **Premium and liquidity.** ~$2.0–2.5M AUM, ~660 holders, **no secondary market at all**. Settled question; one more data point at the extreme end.
7. **Proof of reserve.** **No bar list, no PoR feed, no reserve attestation, and no smart-contract audit found.** Both halves of the wave-1 distinction fail here. Mitigated, though not cured, by HSBC as custodian and an SEC-reporting audited parent.
8. **Distribution.** **No savings plan, no recurring purchase, no referral, no affiliate, no agent network.** Single proprietary app. Aurumix's SIP-plus-agent-network model remains unmatched across the entire set.
9. **Wind-down.** No published wind-down plan. But the **Substitute Bailee clause (§9(j))** is the closest thing any protocol in the set has to a documented continuity mechanism: the bailee's obligations transfer to a licensed affiliate on website notice, and holders then look solely to the substitute. Worth borrowing the *idea* (name a successor mechanism ex ante) while noting the defect (affiliate-only, no consent, no external trustee, no independent insolvency protection).

### 12.6 What to take from this profile

- **Use WTGOLD as the flagship precedent for the non-security gold core.** A NYSE-listed, NYDFS-chartered US manager reached the same classification conclusion Aurumix has. That is the best validation available anywhere in this landscape.
- **Do not present it as a fund-wrapper alternative.** It is not one, and the fund wrapper is legally unavailable for physical gold. Retire that hypothesis.
- **Take the instrument-separation lesson.** WisdomTree and Kinesis independently converge on it. Unify the app, sever the wrappers.
- **Read the redemption maths as a warning about disclosure integrity**, not as a feature to copy.
- **Note the abandonment signature.** A zero-revenue gold product inside a fast-growing fund business has received no development in 18 months. Aurumix's gold core must generate revenue for someone internally, or it becomes PMGT.

## 13. Open items for verification

- [ ] Obtain the **WisdomTree State License Disclosure** at https://www.wisdomtreeprime.com/disclosures (returned HTTP 403 to us): full state money transmitter list, NMLS IDs, and the states where WTGOLD is unavailable.
- [ ] Obtain the **NYDFS charter number** for WisdomTree Digital Trust Company, LLC from the NYDFS licensed-entity register, and confirm the charter is current as of 2026.
- [ ] Obtain the **WisdomTree Digital Assets Schedule** (referenced throughout the User Agreement as the operative fee document, never published alongside it). It should contain the **buy/sell spread**, the minimum purchase, and the definitive fee table. **Highest-value missing document.**
- [ ] Identify the **genuine Stellar issuer account and Ethereum contract address** for WTGOLD via the Prime app or WisdomTree investor relations. Confirm authorization flags. **Report the spoofed asset cluster (`wisdomtree.com.co`, `wisdomtree.bond`, `wisdomtree.xlmhq.org`, `stocks.kraken.com.bz`) to WisdomTree** as a brand-protection matter; it is also a live consumer-harm risk.
- [ ] Confirm whether WisdomTree publishes **any** independent attestation of the HSBC gold, or whether the gitbook "Independent Audits" page has substance behind the heading.
- [ ] Obtain the **HSBC custody agreement** or its material terms: is allocation contractual only, or is there a segregated account title? Is there insurance, and who is loss payee?
- [ ] Identify the **"Metal Agent"** named in User Agreement §5(h). The redemption fee is stated to be set by this third party, not by WisdomTree.
- [ ] Resolve the **AUM discrepancy** in RWA.xyz snapshots (~$1.97M total asset value vs ~$2.52M NAV vs 483.28 tokens at $2,400). Obtain an issuer-published supply figure if one exists.
- [ ] Check WisdomTree, Inc.'s most recent **10-K and 10-Q** for segment disclosure on Prime: revenue, and whether WT Gold is separately identified or has been quietly deprecated.
- [ ] Confirm whether **WisdomTree Digital Movement, Inc. holds a NYDFS BitLicense** in addition to the WT TrustCo trust charter, or whether it operates solely under the charter plus state MTLs.
- [ ] Determine whether the **issuer role migrated** from WisdomTree Digital Holdings, Inc. to WisdomTree Digital Movement, Inc. as the gitbook says was planned, and reconcile against the User Agreement which names **WT TrustCo** as bailee. **Three different WisdomTree entities have been described as the WTGOLD issuer across sources; establish which one is contractually liable today.**

---

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

---

---

# Part 2: Failed and wound-down protocols

Three protocols that stopped operating. All three are profiled against the same thirteen headings, with section 11 as a dated wind-down timeline and section 12 drawing the lesson.

---

# Perth Mint Gold Token (PMGT)

**Status: DISCONTINUED.** Trading ceased 30 June 2023. Smart contract deactivated 1 November 2023. This is a failure profile, and the most instructive one in the set, because the token worked exactly as designed right up until the moment it was switched off.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | PMGT | **High** |
| Issuer (marketing) | "The Perth Mint Gold Token", branded as a Perth Mint product | **High** |
| Issuer (registry) | **Trovio Operating Pty Ltd, ACN 622 224 024 / ABN 33 622 224 024**, Australian Private Company, registered with ASIC 12 October 2017, main business location NSW 2000. Formerly INFINIGOLD OPERATING PTY LTD ([ABN Lookup](https://abr.business.gov.au/ABN/View?abn=33622224024), [CreditorWatch](https://creditorwatch.com.au/credit/profile/33622224024)) | **High** |
| Custodian / bare trustee (registry) | **Trovio Custodians Pty Ltd, ACN 622 220 517** | **High** |
| Gold obligor | Gold Corporation (trading as The Perth Mint), a WA state-owned corporation established by the [Gold Corporation Act 1987 (WA)](https://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/wa/consol_act/gca1987188/s22.html) | **High** |
| Domicile | Australia (NSW). **Note:** ABC News described Trovio as "a Singaporean-based technology company"; the ASIC/ABR registry does not support this. Trovio opened a Singapore office, but the issuing entity is Australian ([International Finance](https://internationalfinance.com/australian-fintech-trovio-expands-apac-office-singapore/)) | **High** |
| Backing claim | 1 PMGT = 1 fine troy ounce, backed 1:1 by a Perth Mint **GoldPass digital certificate**, itself backed by physical gold in Perth Mint vaults | **High** |
| Chains | Ethereum only | **High** |
| Contract address | Token `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf`; Blacklist `0xdE40A3c26F3af423E0d0EcC30ead42B140E16B51`; Whitelist `0x21860dE6d3ba2fAC843f6864a0FAE8e97387bF66` ([contracts repo](https://github.com/DeFi-Coder-News-Letter/pmgt-contracts)) | **High** |
| Peak supply | ~1,195 tokens = ~1,195 oz, ~A$3.5M, at the time of the March 2023 announcement ([ABC via inkl](https://www.inkl.com/news/company-running-perth-mint-cryptocurrency-withdraws-support-but-questions-linger-over-future-of-goldpass-app)). Residual supply today ~0.967 PMGT | **Medium** |
| Market cap | ~US$2.54M reported 15 March 2023; $0 today | **Medium** |
| Regulatory status | **No licence held by Trovio for PMGT was identified.** PMGT was positioned as a non-financial-product utility token. See §3 | **Medium** |
| Subscription fee | None charged by issuer | **Medium** |
| Ongoing custody fee | **None.** No storage or management fee | **Medium** |
| Redemption fee | None at token layer; standard GoldPass fees applied downstream | **Medium** |
| Advertised yield | **None.** PMGT never paid yield | **High** |
| Named officers | **Not disclosed** in PMGT documentation | Not disclosed |

---

## 1. What it is

PMGT was an Ethereum ERC-20 token launched in October 2019 by InfiniGold (renamed Trovio in February 2021) under a **branding licence agreement** with The Perth Mint. Each token represented one fine troy ounce of gold.

The structure was a wrapper around an existing product, not a gold programme in its own right. The Perth Mint already ran **GoldPass**, a digital gold certificate app. PMGT tokenised GoldPass certificates: Trovio held certificates and minted tokens against them. The Perth Mint's role was limited to storing the gold and issuing the certificates. It did not issue the token.

That distinction is the whole story. The marketing surface said "Perth Mint": government-owned mint, central-bank-grade vaults, state guarantee. The legal reality was a small Sydney fintech operating a token under a licence that the Mint could walk away from, and did.

**Correction to the brief's framing.** The brief states PMGT "died of adjacent risk (AUSTRAC AML enforcement against Perth Mint plus the Shanghai Gold Exchange doping scandal), not token defect." The second half is right and the first half is **materially wrong on causation and sequence**. The dates do not support it. See §11 and §12.

## 2. Legal structure

What a holder actually owned, working outward:

1. **PMGT token** on Ethereum: a claim, not the asset.
2. **Beneficial ownership of a GoldPass certificate**, held by **Trovio Custodians Pty Ltd (ACN 622 220 517)** as **custodian and bare trustee** under a **Custody Deed**. The whitepaper states certificates were "recorded separately by Trovio Custodians and there is no pooling, combinations or comingling of Certificates" ([whitepaper](https://www.readkong.com/page/perth-mint-gold-token-whitepaper-in-collaboration-with-2803720)).
3. **The GoldPass certificate**: a contractual claim against Gold Corporation.
4. **Physical gold** in Perth Mint vaults.

**Confidence: High.** This is genuinely better than most tokenised gold: a real bare trust with a separate custodian entity and no commingling, so certificates should be insolvency-remote from Trovio's operating company.

**But note who the trustee is not.** The task brief asked about "Trust Company (Trustee)" status. **We found no evidence that The Trust Company (the Perpetual-owned professional trustee) or any independent third-party professional trustee was involved in PMGT.** The bare trustee was **Trovio Custodians Pty Ltd, a related-party special-purpose vehicle of the issuer**, incorporated with sequential ACN to the operating company (622 220 517 vs 622 224 024). That is a self-appointed affiliate, not an independent trustee. **Confidence: High** on the registry facts; the absence of an independent trustee is a finding, not an inference.

**The critical structural weakness: the holder had no direct claim on gold.** A PMGT holder's claim ran through Trovio Custodians to a GoldPass certificate. If the GoldPass layer were removed, the chain broke. It was removed. See §11.

### The Western Australian government guarantee, and whether it reached token holders

PMGT marketing leaned hard on this. The whitepaper says GoldPass certificates are backed by gold "with the weight and purity of every ounce guaranteed by the Government of Western Australia," citing section 22 of the Gold Corporation Act 1987.

The actual statutory text ([AustLII](https://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/wa/consol_act/gca1987188/s22.html)) guarantees:

> "(a) the cash equivalent of gold due, payable and deliverable by Gold Corporation, the Mint or GoldCorp under this Act; and (b) all moneys due and payable by Gold Corporation in respect of the exercise of the power to buy, borrow or otherwise acquire and to sell, lend or otherwise dispose of, deal in and hold Australian and foreign currency, is guaranteed by the Treasurer, in the name and on behalf of the Crown in right of the State."

Read it precisely. The Treasurer guarantees **obligations of Gold Corporation**. Trovio is not Gold Corporation. PMGT is not an obligation of Gold Corporation.

The Perth Mint's own government-guarantee page describes the guarantee as covering "customers and stakeholders of The Perth Mint enterprise" and makes **no mention of cryptocurrencies, tokens, or third-party products** ([Perth Mint](https://www.perthmint.com/about/government-guarantee/)).

**Assessment: the WA guarantee did not reach PMGT token holders directly.** It attached one layer down, to Gold Corporation's obligation under the GoldPass certificate. A token holder could only reach it derivatively: via Trovio Custodians, via the certificate. If Trovio failed, or simply declined to act, the guarantee did nothing for the token holder as a token holder. **Confidence: High** on the statutory reading and the Mint's own scoping. **Confidence: Medium** that no counter-analysis exists: we found no published legal analysis of this question, which is itself notable given the guarantee was PMGT's central marketing claim.

This is the single most transferable legal finding in the profile: **a sovereign guarantee named in token marketing was, on its own terms, a guarantee of somebody else's obligation.**

## 3. Regulatory and compliance posture

| What we checked | Result |
|---|---|
| AFSL held by Trovio Operating for PMGT | **Not found.** No AFS licence identified for the token |
| ASIC enforcement against Trovio entities | **None found**, 2019 to July 2026 |
| Registration of PMGT as a financial product / MIS | **Not found** |
| AUSTRAC action against Trovio | **None found.** All AUSTRAC action was against **Gold Corporation** |
| Corporate status of Trovio Operating (July 2026) | **Registered and Active.** Next ASIC review 12 October 2026 ([CreditorWatch](https://creditorwatch.com.au/credit/profile/33622224024)) |

**The regulatory story is entirely about the Mint, not the token.** AUSTRAC's actions named Gold Corporation. Trovio was never the enforcement target. Nonetheless, Trovio's first public reason for exiting cited Perth Mint's regulatory problems (§11).

**Note for §12 relevance:** the issuer is still alive and trading. The token is dead. Failure here was not insolvency. Nothing forced this. It was a commercial decision by a solvent licensor and a solvent issuer.

## 4. Custody and proof of reserve

| Element | PMGT |
|---|---|
| Custodian (gold) | Gold Corporation / The Perth Mint, Perth, Western Australia |
| Custodian (certificates) | Trovio Custodians Pty Ltd, ACN 622 220 517, as bare trustee |
| Allocated? | Whitepaper asserts no pooling or commingling of certificates. Whether the underlying vault gold was allocated per certificate: **Not disclosed** |
| Published bar list | **Not found.** No serial-numbered bar list was published |
| PoR feed | **Yes**, and this was PMGT's genuine strength: a real-time feed at `pmgt.perthmint.com` publishing GoldPass certificates backing the supply, so a holder could verify total supply against certificates on demand ([technical update](https://medium.com/pmgt/technical-update-perth-mint-gold-token-contract-is-live-da745a494f99)) |
| Reserve attestation by named audit firm | **Not found.** No periodic third-party attestation (no Big Four, no equivalent). The "Realtime Audit" was **issuer self-publication**, not an attestation |
| Smart contract audit | **Not found.** Contracts were open-sourced under MIT, but no named audit firm or published audit report was identified |

**Two cautions, both directly relevant to client design question 7.**

First, PMGT labelled its reserve feed "Realtime Audit." It was not an audit. It was a live self-published data feed. This is exactly the blurring the brief warns about, and PMGT did it in the product's own naming.

Second, **the PoR feed is now dead.** `pmgt.perthmint.com` returns connection refused. A proof-of-reserve system that lives on issuer infrastructure has exactly the lifespan of the issuer's willingness to pay the hosting bill. Every historical verification claim PMGT made is now unverifiable.

## 5. Issuance

Holders deposited GoldPass certificates with Trovio Custodians and received PMGT 1:1. Required: a verified GoldPass account, verified ID, and a linked Ethereum address. **No minting fee** charged by the issuer.

Issuance was therefore gated on being a Perth Mint GoldPass customer first. PMGT was never open-access: the on-ramp was a KYC'd Australian/US precious metals account. This capped the addressable market severely and helps explain the tiny supply (~1,195 oz peak).

## 6. Redemption

**Design (pre-wind-down):** burn PMGT, receive GoldPass certificates into a verified GoldPass account, then use GoldPass to convert to fiat or request physical bullion. **No redemption fee** at the token layer.

**Physical gold was never directly redeemable from the token.** Physical delivery required exiting to GoldPass first and then transacting with the Mint. Two hops, both KYC-gated, both requiring an account with an entity other than the token issuer.

The whitepaper contained an explicit continuity assurance:

> "If the Licence Agreement is terminated, Trovio would no longer be able to issue PMGT. Notwithstanding this, a token holder will still be able to redeem their existing PMGT for Certificates which can then be redeemed for gold with The Perth Mint."

**This assurance failed.** It assumed GoldPass would outlive PMGT. The Perth Mint wound down GoldPass on an overlapping timetable (§11), so the redemption route the whitepaper promised was being dismantled at the same time holders were being told to use it. **Confidence: High** on the whitepaper text; **Confidence: Medium** on the precise degree of overlap, since the GoldPass account-closure dates come from press reporting rather than a Mint notice.

**Redemption in practice, from November 2023:** manual only. Lodge a support ticket, complete KYC, ID verification, bank account verification, and prove control of the Ethereum address holding the position. Holders receive "the backdated gold price minus any fees owing." Note that "minus any fees owing" appears only at the wind-down stage: fees that were advertised as nil during the product's life reappear at exit. **Confidence: Medium** (the primary FAQ page is offline; text survives via aggregator mirrors).

**Whether manual redemption still works in July 2026: unverified and doubtful.** `pmgt.io` returns connection refused. The Perth Mint's live PMGT page still says "For more information visit pmgt.io" ([Perth Mint](https://www.perthmint.com/invest/goldpass/perth-mint-gold-token-pmgt/)), directing stranded holders to a domain that no longer resolves. The FAQ language was itself conditional: after 1 November 2023 Trovio "may no longer be able to assist with manual withdrawals."

## 7. Fees and revenue model

| Fee line | PMGT |
|---|---|
| Subscription / minting | None |
| Ongoing custody / storage | **None** |
| Redemption | None at token layer; GoldPass fees downstream |
| Transfer | None from issuer (Ethereum gas only) |
| Exit fees at wind-down | "Minus any fees owing", unquantified |

**PMGT had no visible revenue model at the token layer.** It charged holders nothing: no mint fee, no custody fee, no redemption fee, no yield to fund. This is the "option three" in the client's design question 1: charge holders nothing and recover cost elsewhere.

**It is also, on the evidence, why the token died.** With ~1,195 oz (~A$3.5M) under management and a zero fee schedule, PMGT generated approximately nothing for Trovio while consuming engineering, compliance, custody and market-making cost. Trovio's revenue thesis was presumably strategic: build tokenisation infrastructure, expand into other commodities (the point of the 2021 InfiniGold to Trovio rebrand). When the Perth Mint relationship became a liability, there was no revenue stream defending the product's existence.

**Direct answer to client design question 1: a zero-fee gold token is not a neutral choice. It removes the economic constituency that fights to keep the product alive.** A fee-paying product has a P&L line someone defends in a strategy meeting. PMGT had none.

## 8. Token architecture

- **Standard:** ERC-20.
- **Permissioning:** **Permissioned.** The deployed system included dedicated **Blacklist** and **Whitelist** contracts at separate addresses. Transfers were subject to these lists. PMGT was not a freely transferable ERC-20 despite presenting as one.
- **Upgradeability:** **Yes.** Implemented as "a standard proxy contract from OpenZeppelin" ([technical update](https://medium.com/pmgt/technical-update-perth-mint-gold-token-contract-is-live-da745a494f99)), so the implementation could be replaced by the proxy admin.
- **Admin keys:** owner/admin roles plus blacklist and whitelist administration. The issuer could block addresses and swap implementation logic.
- **Bridge:** none. Ethereum only.
- **Audit:** **Not found** (see §4).

**This matters more than it first appears.** The combination of upgradeable proxy plus address-level blocking meant the issuer retained unilateral technical control over the token for its entire life. When Trovio "deactivated the smart contract" on 1 November 2023, it was exercising powers it had held since deployment in 2019.

**Direct answer to client design question 3:** PMGT shows that a permissioned architecture buys real control, and that the control is not symmetric. It protected the issuer's ability to comply and to wind down in an orderly way. It did nothing for holders when the issuer chose to shut the product. Aurumix's ERC-3643 lean gives it the same powers. The design question is not whether to hold them, but **what binds the issuer's use of them**, since the code plainly will not.

## 9. Liquidity and market

- Peak: ~1,195 tokens (~1,195 oz, ~A$3.5M) at March 2023. Market cap ~US$2.54M reported 15 March 2023.
- Primary venue: **Independent Reserve** (Australia), where a **PMGT market maker** provided the exit liquidity. The market maker's identity is **not disclosed**.
- Residual on-chain supply: ~0.967 PMGT.
- Typical daily volume: **Not found**, but on a US$2.5M cap against a single primary venue it was necessarily negligible.

**PMGT is a second data point against the client's premium thesis (design question 6), and a harsher one than PGOLD.** PGOLD at least accumulated ~$79 to 90M of AUM with thin liquidity. PMGT never accumulated AUM at all: four years of operation, backed by a government-owned mint with a sovereign guarantee, world-class vaults and a genuine real-time reserve feed, produced **US$2.5M**. Every trust signal a gold token could want, and the market did not come.

**The uncomfortable read for Aurumix:** PMGT proves that custody quality and sovereign backing do not by themselves generate demand. Distribution does. PMGT had essentially none: no savings plan, no recurring purchase, no agent network, no referral scheme (§10). It waited for existing GoldPass customers to opt in.

## 10. Distribution

- **Channels:** self-serve, gated behind an existing Perth Mint GoldPass account. Listed on Independent Reserve.
- **Geography:** Australia and the US.
- **Savings plan / SIP / recurring purchase:** **None found.**
- **Referral / affiliate / agent network:** **None found.**
- **Target segment:** existing precious metals investors already holding GoldPass certificates.

**Direct answer to client design question 8: PMGT had no distribution mechanism whatsoever.** It was a conversion utility for an existing customer base, offered to people who had already solved the hard problem of buying gold. It added a blockchain wrapper to a base of ~26,700 GoldPass accounts and converted roughly 1,195 ounces.

This is the sharpest available evidence for the client's core strategic bet. PMGT is the control experiment: a gold token with excellent custody and zero distribution. It reached US$2.5M in four years.

## 11. Wind-down timeline (dated, reverse chronological)

**22 July 2025**: AUSTRAC formally concludes the Enforceable Undertaking. AUSTRAC "is satisfied Gold Corporation has met its obligations," following a final external auditor progress report in May 2025. Remediation delivered on schedule against the 30 April 2025 deadline; ~70,000 customer accounts remediated. **No fine imposed at any stage** ([Perth Mint](https://www.perthmint.com/news/media-announcements/corporate/austrac-concludes-the-perth-mints-enforceable-undertaking/), [AUSTRAC](https://www.austrac.gov.au/news-and-media/media-release/austrac-deems-perth-mint-free-enforceable-undertaking)). **The AML matter ended with the Mint cleared, two years after the token it supposedly killed was already dead.**

**1 November 2023**: **PMGT smart contract deactivated.** All remaining PMGT holdings sold, locking in the gold price on that date. Remaining holders can only lodge a manual redemption request, receiving "the backdated gold price minus any fees owing." **Confidence: Medium** (primary FAQ offline; text preserved via aggregator mirrors).

**31 October 2023**: PMGT formally discontinued. Deadline to exchange PMGT for GoldPass certificates.

**23 November 2023** *(after the token was already dead)*: AUSTRAC accepts an **Enforceable Undertaking** from Gold Corporation. Failings cited: inaccurate customer risk identification, ineffective transaction monitoring, and reporting failures. Remediation to conclude 30 April 2025. **No fine** ([Perth Mint](https://www.perthmint.com/news/media-announcements/corporate/the-perth-mint-welcomes-austrac-outcome/)).

**30 June 2023, 10am AEST**: Independent Reserve delists PMGT. End of exchange trading and of the market maker exit route.

**~18 April 2023**: The Perth Mint shuts down **GoldPass**. Zero-balance accounts closed immediately; active accounts barred from further transactions at the end of May; holders given until the end of November to empty accounts. Holders seeking physical gold warned of "significant delays," with redemption subject to stock availability ([The West](https://thewest.com.au/politics/state-politics/perth-mint-shuts-controversial-goldpass-mobile-app-effective-immediately--c-10510953)). **This is the decisive event for holders: the destination they were told to redeem into was being closed on an overlapping schedule.**

**4 April 2023**: PMGT publishes the formal discontinuation notice, setting the two deadlines: trade out via the market maker on Independent Reserve by **30 June 2023**, or exchange for GoldPass Certificates by **31 October 2023** ([Medium](https://medium.com/pmgt/the-perth-mint-gold-token-pmgt-is-being-discontinued-d27971f8eb3d)).

**March 2023**: WA Premier Mark McGowan states he has no recollection of the cryptocurrency and was not informed it was ending. Opposition Leader Shane Love calls it "far from a storm in a teacup." ABC reports internal Mint documents showing that **as of May 2022 the Mint planned to "fully terminate" GoldPass by August 2023**, and that the Mint decided to shut down both products without telling customers until Trovio's statement ([ABC via inkl](https://www.inkl.com/news/company-running-perth-mint-cryptocurrency-withdraws-support-but-questions-linger-over-future-of-goldpass-app)).

**8 March 2023**: The Perth Mint responds to the ABC allegations: SGE required the non-gold 0.01% component contain no more than 50 ppm silver; some bars exceeded this. The Mint maintains all bars contained at least 99.99% gold "as per their specifications," and that new refining processes took effect December 2021. **No recall occurred** ([Perth Mint](https://www.perthmint.com/news/media-announcements/corporate/response-to-abc-tv-allegations/)).

**6 March 2023**: ABC *Four Corners* "Tainted Gold" airs, alleging potential recall exposure of ~A$9bn of "doped" one-kilogram bars sold to the Shanghai Gold Exchange, and that the Mint tried to cover it up. **The Mint had known since September 2021.**

**1 March 2023**: **Trovio announces it will no longer support PMGT.** The original statement cites "ongoing investigations into alleged breaches [by Perth Mint] with AUSTRAC and US State Regulation." **This statement was subsequently edited** to say the decision was made "due to several factors after a number of years in operation." The move is understood to have surprised the Mint. PMGT at this point: ~1,195 tokens, ~A$3.5M.

**Early 2022**: **The Perth Mint initiates discussions with Trovio to exit the PMGT product.** This is the actual origin of the wind-down, confirmed by the Mint itself.

**30 August 2022**: AUSTRAC directs Gold Corporation to appoint an **external auditor** ([AUSTRAC](https://www.austrac.gov.au/news-and-media/media-release/austrac-orders-audit-gold-corporations-compliance-financial-crime-laws)). Audit runs November 2022 to July 2023. **This is the earliest public AUSTRAC action, and it postdates the Mint's decision to exit PMGT.**

**March 2021**: Perth Mint's AML remediation programme begins.

**September 2021**: Perth Mint becomes aware some 1kg bars do not meet SGE non-gold specifications.

**October 2019**: PMGT launches on Ethereum, issued by InfiniGold (later Trovio) under licence.

### Was there a wind-down plan published in advance?

**No.** This is the clearest finding in the profile, and it is unambiguous.

- The only pre-existing continuity provision was the whitepaper sentence promising that if the licence terminated, holders could still redeem PMGT for certificates and then for gold. That is a **one-sentence assurance, not a plan**, and it failed because it depended on GoldPass surviving. GoldPass did not.
- **No insolvency provision, contingency plan, wind-down procedure, or trigger framework was published before March 2023.** We looked in the whitepaper, the terms and conditions and the FAQ. The original terms text is now inaccessible (`pmgt.io` is offline), so we record this as **Confidence: Medium** on the terms specifically and **Confidence: High** overall, since no source in four years of coverage refers to any such plan.
- The wind-down was **announced, not executed against a pre-agreed framework**: deadlines were set after the decision, by the parties who made the decision, and at least one deadline structure was published a month after the exit announcement.
- Holders learned of the product's end from **the issuer's press statement**, and that statement was **subsequently edited** to remove the stated cause. Even the reason given was not stable.

**This corroborates the brief's claim that no failed gold token published a wind-down plan, and PMGT is the strongest case for it**, because PMGT is the one that most looked like it should have had one: state-owned counterparty, sovereign guarantee, professional custody structure, real-time reserve feed.

### What did holders actually recover?

**On the evidence, holders were made economically whole, and it was luck of timing rather than design.**

- Holders exiting via Independent Reserve before 30 June 2023 sold at market against the market maker, so they realised approximately the gold price. **Confidence: Medium.**
- Holders exchanging into GoldPass certificates by 31 October 2023 retained a gold claim, but into a platform that was itself being wound down and where physical redemption carried "significant delays."
- Holders who did nothing had their positions **force-sold on 1 November 2023 at that day's gold price**. They were not expropriated; they were converted to cash without consenting, at a date chosen by the issuer. **Confidence: Medium.**
- Stragglers face manual redemption: KYC, ID verification, bank verification, proof of Ethereum address control, "minus any fees owing," and no guarantee of assistance after 1 November 2023.

**No reported holder losses, complaints, or litigation were found.** No regulator supervised the wind-down itself.

**Do not read that as success.** Three qualifications matter more than the headline:

1. **The float was tiny (~A$3.5M) and the holder base was small and already KYC'd.** A wind-down of this shape at $100M with retail holders across multiple jurisdictions would not resemble this at all.
2. **Gold rose through 2023.** Force-selling at spot on 1 November 2023 was benign because the price was favourable. The same mechanism in a drawdown converts holders to cash at the bottom and removes their ability to wait for recovery. **Holders lost optionality, and the fact that it did not cost them is a market outcome, not a governance one.**
3. **The absence of complaints is partly an absence of evidence.** `pmgt.io` is gone; the FAQ, support portal and terms are all offline. A stranded holder in 2026 following the Perth Mint's own live instructions arrives at a dead domain.

## 12. Relevance to Aurumix

### First, correct the inherited framing. Loudly.

The brief records PMGT as having "died of adjacent risk (AUSTRAC AML enforcement against Perth Mint plus the Shanghai Gold Exchange doping scandal)." The task also asked us to test the thesis that AUSTRAC enforcement plus the SGE scandal killed PMGT. **The dated record does not support this, and the sequence is decisive:**

| Event | Date |
|---|---|
| **Perth Mint begins discussions to exit PMGT** | **Early 2022** |
| Internal Mint plan to "fully terminate" GoldPass by Aug 2023 | **May 2022** |
| AUSTRAC's earliest public action (external auditor order) | 30 August 2022 |
| Four Corners SGE broadcast | 6 March 2023 |
| Trovio announces exit | 1 March 2023 |
| AUSTRAC Enforceable Undertaking | 23 November 2023 |
| AUSTRAC concludes EU, Mint cleared, **no fine ever** | 22 July 2025 |

**The Perth Mint decided to exit PMGT in early 2022: before any AUSTRAC public action, and roughly a year before the SGE scandal broadcast.** The enforcement action that supposedly killed the token began after the exit decision and concluded in July 2025 with **no penalty at all**. The SGE matter produced **no recall**.

The honest causal account is: **PMGT was killed by commercial abandonment.** It was a strategically interesting, revenue-free product that a state-owned licensor decided it no longer wanted, at a moment when the licensor was distracted by unrelated compliance problems. The AUSTRAC and SGE events were **accelerant and cover story**, not cause. The strongest evidence is Trovio's own conduct: it announced AUSTRAC and US regulation as the reason, then **edited that statement** to "several factors after a number of years in operation." The second version is closer to the truth.

**The brief's conclusion "not token defect" is correct and worth keeping.** Its stated cause is not.

### The lesson, and it is the sharpest one in the landscape

**Aurumix's greatest structural risk is not a run on the gold, a hack, or a regulator. It is that a counterparty it does not control decides the product is not worth continuing.**

PMGT had everything the client is trying to buy with custody quality: a government-owned counterparty, a statutory sovereign guarantee, central-bank-grade vaults, a bare trust with no commingling, a real-time proof-of-reserve feed, and a clean compliance record of its own. **It died anyway, in four months, because it had no revenue and depended on someone else's platform.**

Six specific transfers:

**1. Redemption that routes through a third party is not redemption (design question 5).** PMGT's whitepaper promised holders could always redeem to certificates and then to gold. That promise was void the moment the Mint wound down GoldPass. Aurumix's exit is **cash buyback only**, and the buyback obligor is Aurumix itself. That is more honest than PMGT's two-hop chain, but it concentrates the entire exit path on one balance sheet. **The question Aurumix must answer in writing: who executes the buyback if Aurumix stops operating, and out of what?** PMGT's answer was "GoldPass," and GoldPass closed.

**2. A named sovereign or institutional guarantee probably does not reach your holders.** Section 22 guaranteed Gold Corporation's obligations, not Trovio's, and the Mint's own page never mentioned tokens. If Aurumix ever cites a vault operator's, insurer's, or authority's standing in marketing, **state precisely whose obligation is guaranteed and confirm it is the obligation owed to the token holder.** PMGT's central marketing claim was, on its own terms, a guarantee of somebody else's promise.

**3. Zero fees killed it (design question 1).** PMGT charged nothing: no subscription, no custody, no redemption. It therefore had no P&L, no internal advocate and no defence when the licensor lost interest. This is the strongest available argument **against** the client's "option three" (charge holders nothing, recover cost elsewhere). **A gold product needs a revenue line that makes someone inside the business fight for it.** Aurumix's SIP-plus-fee model is, on this evidence, a survival feature, not just a monetisation choice.

**4. Custody excellence does not create demand; distribution does (design questions 6 and 8).** PMGT is the control experiment: best-in-class custody, sovereign guarantee, real PoR, **no savings plan, no agent network, no referral scheme**. Result: ~US$2.5M in four years. Aurumix's agent network and SIP are the parts of the model this landscape most supports. **Do not let the gold infrastructure crowd out the distribution build.**

**5. "Realtime Audit" was not an audit, and it is now offline (design question 7).** PMGT branded a self-published issuer data feed as an audit. There was **no reserve attestation by a named firm and no smart contract audit**. Worse, the feed died with the company's hosting, so every historical verification claim is now unverifiable. **Aurumix should commission a named third-party attestation, publish a bar list, and host attestation artefacts somewhere that survives the company:** IPFS, a registry filing, or the attestor's own site.

**6. The wind-down commitment is cheap and genuinely differentiating (design question 9).** PMGT confirms the pattern. Holders got: an announcement whose stated reason was then edited, deadlines set after the fact, an exit route that was itself closing, a force-sale on a date they did not choose, and a support site that no longer resolves. Aurumix can pre-commit, in the terms, to specifics PMGT never offered:

- **A minimum notice period** (PMGT gave ~4 months to the trading deadline, but the redemption destination was closing simultaneously).
- **A named successor or backup redemption agent**, so the exit does not depend on one platform.
- **An independent professional trustee**, not a related-party SPV. PMGT's bare trustee was an affiliate of the issuer with a sequential ACN. **Confirming there was no independent trustee is one of this profile's most decisive findings**, given the task brief's expectation of one.
- **A commitment that holders are never force-converted to cash without an election period**, or, if forced conversion is unavoidable, a stated pricing methodology agreed in advance rather than a date picked by the issuer.
- **A durable-artefact undertaking**: reserve records and redemption instructions must survive the issuer's domain registration.

That last item costs nothing and is the most vivid failure here. **In July 2026, The Perth Mint's live website still tells stranded PMGT holders to visit pmgt.io. The domain does not resolve.**

## 13. Open items for verification

- [ ] Obtain the original PMGT terms and conditions and FAQ (offline at `pmgt.io`) from a web archive to confirm definitively whether any insolvency, contingency or forced-liquidation clause pre-dated March 2023, and whether the terms permitted unilateral termination and force-sale. Archive.org has a 23 Nov 2023 snapshot at `web.archive.org/web/20231123224936/https://www.pmgt.io/` that this environment could not fetch.
- [ ] Confirm the 1 November 2023 force-sale mechanism against a primary Trovio or Perth Mint source. Currently **Confidence: Medium**, sourced via aggregator mirrors of the PMGT FAQ. Establish who executed the sale, at what gold fix, and where proceeds are held.
- [ ] Verify the current ASIC status of **Trovio Custodians Pty Ltd (ACN 622 220 517)** via a paid ASIC extract. We confirmed Trovio Operating is active; the custodian entity's status was not independently confirmed.
- [ ] Obtain the **Custody Deed** between Trovio Custodians and token holders to confirm the bare trust's terms, and whether holders had any direct enforcement right against the custodian.
- [ ] Confirm whether any unredeemed PMGT gold remains, where it sits, and whether it has escheated as unclaimed property under WA or NSW law. No source addresses this.
- [ ] Confirm the exact GoldPass account-closure dates from a Perth Mint primary notice rather than press reporting, to pin down the overlap with the PMGT redemption window.
- [ ] Retrieve the Gold Corporation Statement of Corporate Intent tabled in WA Parliament (`parliament.wa.gov.au` tabled paper 2088 (2023)) for the official wording on the GoldPass and PMGT "orderly winddown" and any provisions taken.
- [ ] Retrieve the Perth Mint 2023-24 annual report (PDF at `perthmint.com/globalassets/assets/documents/annual-reports/perth-mint-annual-report-23-24.pdf`, not text-extractable here) for financial provisions relating to SGE, AUSTRAC remediation cost, and the GoldPass/PMGT exit.
- [ ] Test whether manual PMGT redemption is still honoured in 2026 by contacting Trovio directly. This is the single most decision-relevant open item for the client's §9 wind-down commitment.
- [ ] Seek any legal analysis of whether the section 22 guarantee could have been enforced by a PMGT holder. We found none, despite it being PMGT's central marketing claim.
- [ ] Confirm peak PMGT supply and market cap from historical on-chain data rather than press estimates.
- [ ] Identify the PMGT market maker on Independent Reserve, and on what terms it was obliged to bid during the wind-down.

---

# Digix Gold Token (DGX) and DigixDAO (DGD)

**Status: WOUND DOWN.** The DAO was dissolved by token-holder vote in January 2020. The company stopped taking new business in September 2022 and ceased operations on 21 March 2023. Every Digix entity on the Singapore register is now struck off, the last on **19 July 2026, nine days before this profile was written.** The DGX contract still runs on Ethereum and 15,400 tokens still exist, but there is no reachable issuer, no reachable redemption agent, and no live website.

This is a failure profile, and it is the most important one in the set for two reasons. First, it is the **only live example of the demurrage mechanism the client has already ruled out**, so §7 documents it at contract level. Second, it repeats the PMGT pattern precisely: **Digix switched its own revenue off before it died.**

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Tickers | DGX (gold token), DGD (DAO / governance token) | **High** |
| Issuer (marketing) | "Digix" / "DigixGlobal", Singapore | **High** |
| Issuer (registry) | A **group of separate Singapore entities, all now struck off**. Gold title sat in **DIGIX PHYSICALS PTE. LTD., UEN 201724269N** (inc. 25 Aug 2017, SSIC 52101 General Warehousing, stated activity "HOLD PHYSICAL ASSETS"). Parent **DIGIX HOLDINGS PRIVATE LIMITED, UEN 201724450M** (inc. 28 Aug 2017), **struck off 19 July 2026** ([RecordOwl](https://recordowl.com/company/digix-holdings-private-limited), [OpenGov SG](https://opengovsg.com/corporate/201724450M), [OpenCorpData](https://opencorpdata.com/sg/201724269N)) | **High** |
| Other group entities | **DIGIX MARKETS PTE. LTD.** UEN 201906348R (inc. 27 Feb 2019, "Fund management activities n.e.c."), **DIGIX TECHNOLOGIES PRIVATE LIMITED** UEN 201713056E (inc. 11 May 2017), **DIGIX CORE** UEN 53369203B (ceased registration). All struck off or ceased | **High** |
| Domicile | Singapore. All entities shared one address: 6 Eu Tong Sen Street, #06-09, The Central, Singapore 059817 | **High** |
| Backing claim | 1 DGX = 1 gram of 99.99% LBMA-standard gold cast bar, divisible to 0.001g | **High** |
| Chains | Ethereum only | **High** |
| Contract address | DGX: `0x4f3AfEC4E5a3F2A6a1A411DEF7D7dFe50eE057bF`. DGD refund ("Acid"): `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f` | **High** |
| Supply | DGX: **15,400** tokens (~15.4 kg gold nominal), ~2,103 holders. Peak was 122,700 DGX (Jan 2020). DGD: 1,999,999 total | **High** |
| Market cap / volume | DGX: ~$278k on-chain, **24h volume nil**. DGD: ~$0.067, 24h volume **$0** | **Medium** |
| Regulatory status | **No licence held.** Digix Holdings **withdrew its Payment Services Act licensing in September 2022**. See §3 | **Medium** |
| Subscription fee | Minting free to the depositor; Digix earned its margin on gold purchase | **Medium** |
| Ongoing custody fee | **0.60% per annum demurrage, deducted in gold from token balances.** **Switched off (set to zero) in 2019 and never switched back on.** See §7 | **High** |
| Transfer fee | **0.13% of every transfer**, deducted in gold. This is the "0.13%" figure, not the demurrage rate. See the correction below | **High** |
| Redemption fee | **1% recast fee**, in gold, on 100g / 1kg bar redemption in Singapore | **High** |
| Advertised yield | DGX: none. DGD: a share of DGX fee revenue, paid quarterly to stakers who voted | **High** |
| Named officers | Kai C. Chng (co-founder, CEO), Anthony Eufemio (co-founder, CTO), Shaun Djie (co-founder) | **Medium** |

---

## ⚠ Three corrections to the brief, one of them material

**1. The "0.13% demurrage" premise in the task is wrong, and the error matters mechanically.** The task states Digix "charged a demurrage fee deducted in gold (reportedly 0.13% per year)." Those are two different fees conflated:

- **Demurrage: 0.60% per annum**, accrued daily against the holder's balance.
- **Transfer fee: 0.13% per transfer**, an event-driven charge, not annual.

Both were denominated in gold, so the client's concern is right, but the annual drag was **4.6x larger** than assumed and there was a second, separate gold-denominated charge on top of it. **Confidence: High** ([Digix FAQ](https://medium.com/@Digix/digix-faq-deaf53fcc1e8), [fee calculation gist](https://gist.github.com/mrenoon/2582fba7b4d457d80f7d37520aabbc08)).

**2. The brief's causal framing is half right and half wrong, in the same way PMGT's was.** The brief says "Digix dissolved its DAO via a structured treasury return while DGX went illiquid." Both halves are factually true. But the framing implies the DAO dissolution was Digix's chosen wind-down mechanism. It was not. **Digix the company opposed the dissolution and abstained from the vote.** It was done *to* the company by its token holders, over management's objection, and it removed the funding base that had subsidised DGX. See §11 and §12.

**3. The wind-down is more complete than "went illiquid" suggests.** DGX did not merely go quiet. The issuer withdrew from regulation, ceased business, handed redemption to an offshore party that is now unreachable, and **every Singapore entity has been struck off the register**, the parent as recently as **19 July 2026**. There is no counterparty left to sue.

---

## 1. What it is

Digix was founded in Singapore in December 2014 and is the **oldest serious tokenized gold project**: DGX predates PAXG by roughly four years and XAUT by five. It ran the first significant Ethereum ICO in March 2016, selling DGD for **466,648 ETH** (~$5.5M at the time).

The architecture had two tokens doing two jobs, which is precisely the "instrument split" the brief flags as a live lead:

- **DGX**: the asset token. 1 DGX = 1 gram of gold. No governance rights, no yield.
- **DGD**: the governance and revenue-share token. 2,000,000 fixed supply. Holders who staked and voted received a share of DGX fee revenue.

Gold was tracked through the **Proof of Provenance (PoP)** protocol, an on-chain asset and supply-chain record using Ethereum plus IPFS, tracking bars from vendor to vault. Gold was sourced through **ValueMax** (a listed Singapore pawnbroker) and stored with **The Safe House** in Singapore, later with an additional Canadian vault ([FintechNews Singapore](https://fintechnews.sg/835/blockchain/digix-digital-tokens-representing-legal-ownership-assets/)).

For the client, the important observation is that **Digix built almost exactly the structure Aurumix is considering**: a clean gold token, a separate instrument carrying governance and revenue rights, real vaulted metal, on-chain provenance, and genuine physical redemption. It was better-engineered than most of its successors. It still failed. Understanding why is the whole value of this profile.

## 2. Legal structure

What a DGX holder actually owned:

The registry gives the answer more precisely than the marketing did. **DIGIX PHYSICALS PTE. LTD. (UEN 201724269N)** was incorporated under SSIC **52101, "General Warehousing"**, with its stated principal activity recorded as **"HOLD PHYSICAL ASSETS"** ([OpenCorpData](https://opencorpdata.com/sg/201724269N)). That is a warehousing company, not a trustee and not a regulated custodian.

Third-party analysis of DGX's structure describes the position bluntly: Digix Physicals **maintained title to the gold bullion in the vault**, meaning the company legally owned the vaulted gold, and the holder's relationship with Digix was analogous to a relationship with a bank. Title transferred to the holder only on physical collection.

**So a DGX holder held an unsecured contractual claim against a Singapore warehousing company, not beneficial title to gold.** There is **no trust deed, no bare trust, and no independent trustee** anywhere in the Digix structure that we could locate. **Confidence: Medium** on the title analysis (secondary source, no primary custody agreement published); **Confidence: High** on the registry facts.

Compare PMGT, which for all its faults had a real bare trust with a separate custodian entity and an explicit no-commingling covenant. Digix, the older and more celebrated project, had **weaker holder protection than the product we already classified as a failure**.

**Why this matters now.** Digix Physicals is struck off. When a Singapore company is struck off, its remaining property vests in the state as *bona vacantia*. If gold was still held in that company's name at strike-off, the holder's counterparty no longer exists and the claim runs against an entity that has been dissolved. **Confidence: Medium** on the legal consequence (general Singapore company law; we found no filing describing the actual disposition of the gold).

## 3. Regulatory and compliance posture

| What we checked | Result |
|---|---|
| MAS Payment Services Act licence | **Withdrawn by the company.** Digix Holdings announced withdrawal of its PSA licensing in **September 2022** ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)) |
| Licence or exemption class, MAS reference number | **Not disclosed.** We could not establish whether Digix held a full licence, an exemption, or only a transitional exemption pending application |
| Any MAS enforcement action against Digix | **None found**, 2014 to July 2026 |
| Any regulator action anywhere | **None found** |
| Current entity status | **All struck off.** Parent struck off 19 July 2026 |
| Securities characterisation of DGD | Never tested by a regulator |

**The regulatory finding is the absence of a regulatory finding.** No regulator shut Digix down. No enforcement action was ever brought. The PSA withdrawal was **voluntary and self-initiated**, and it came *with* the announcement that the company was ceasing all business activities, not before it. The licence did not kill the business; the business gave up the licence on the way out.

This is directly analogous to the wave-1 PMGT correction. **A project can look like it was regulated out of existence when in fact it walked away.** For Digix, the PSA regime arriving in 2020 raised the cost of staying compliant for a business that, by then, had no revenue to pay for compliance. That is a cost-of-compliance-versus-revenue problem, not an enforcement problem.

## 4. Custody and proof of reserve

| Element | Digix |
|---|---|
| Custodian | **The Safe House**, Singapore (ISO 9001 certified vault). A Canadian vault added in 2019 |
| Vault / city | Singapore (primary), Canada (secondary) |
| Gold supplier | **ValueMax**, a listed Singapore pawnbroker |
| Allocated? | Yes in substance: specific 100g and 1kg cast bars, individually identified |
| Published bar list | **Yes, and this was genuinely strong.** Each bar's documentation was recorded on-chain and on IPFS via the Proof of Provenance protocol, with bar serial numbers, assay certificates and vault receipts |
| PoR feed | **Yes**, via PoP. Arguably the first real on-chain proof-of-reserve in tokenized gold |
| Reserve attestation by named audit firm | **Not found.** No periodic third-party reserve attestation by a named accounting firm was identified. PoP was an issuer-operated provenance record, not an independent attestation |
| Smart contract audit | **Yes, and unusually credible.** Audited by **Yaron Velner and Loi Luu**, 21 May to 18 June 2017 ([audit report](https://gist.github.com/loiluu/0363070e1bada977f6192c8e78348438)) |

**The audit/attestation distinction, one more time.** Digix was *smart-contract* audited by serious cryptographers. It was **not** reserve-attested by an accounting firm. Digix's PoP protocol was a much better provenance system than most competitors have today, but it was still the issuer telling you about its own gold, cryptographically. When the issuer's servers and IPFS pinning went away, so did the verification.

**And the audit found real problems.** The 2017 report identified a **critical bug allowing self-transfers to increase balances**, plus a finding that **the demurrage fee calculation incentivised strategic dummy operations**: the fee logic could be gamed by timing transactions. Both flaws were *in the fee mechanism itself*. This is worth noting for the client: the demurrage design was not just economically awkward, it was **hard to implement correctly**, and competent auditors found exploitable defects in it.

## 5. Issuance

Gold was purchased and vaulted, PoP recorded the bar, and DGX was minted against it. Minting for the depositor was free; Digix's margin came from the spread on gold sales through its marketplace. Retail users bought DGX with ETH or fiat via the Digix marketplace or exchanges.

Issuance was **not open-access minting**: creation was controlled by Digix. Supply peaked at ~122,700 DGX (~122.7 kg, ~$6.0M) in January 2020 and stands at **15,400 today**. That peak is the real story: **after five years of operation, the oldest tokenized gold project in the world had accumulated about $6 million of gold.** For scale, PAXG holds ~$1.79bn and XAUT ~$2.46bn.

## 6. Redemption

Digix's redemption ("recast") was **genuinely functional**, which makes its disappearance more instructive.

| Term | Detail |
|---|---|
| Minimum | **100 DGX** (100g bar) or **1,000 DGX** (1kg bar) |
| Fee | **1% recast fee, in gold.** A 100g redemption required **at least 101 DGX** in the wallet |
| Denominations | 100g and 1kg cast bars only |
| Collection | **In person, at the vault, in Singapore** (later also Canada) |
| Window | Physical presence required within **30 days**; uncollected bars were **automatically re-minted into DGX** |
| KYC | Valid government ID plus current proof of address, presented in person at collection |
| Eligibility | Open, subject to the above. No "qualified holder" gate |

Two design points worth stealing and one worth avoiding. Worth stealing: the **automatic re-mint of uncollected bars**, an elegant solution to abandoned redemptions that never leaves the peg unbacked. Worth avoiding: **redemption required physical presence in Singapore**, making it inaccessible in practice to almost the entire holder base. A redemption right you must fly to Singapore to exercise is a marketing feature, not a liquidity feature.

### Can a DGX holder redeem today?

**Tested concretely. The answer is effectively no.**

- On **21 March 2023**, Digix ceased operations and handed redemption facilities to **NexusGold FZC**, described as an overseas partner, with licence number **4306536.01** ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)).
- The redemption portal at **nexusone-dgx.com** is **unreachable** (connection refused on both HTTPS and HTTP, tested 28 July 2026).
- **digix.global** is **unreachable** (connection refused, tested 28 July 2026).
- The Digix Zendesk support portal returns **403 Forbidden**.
- We could **not verify NexusGold FZC in any UAE free-zone register.** "FZC" indicates a UAE free-zone company (commonly Sharjah/Hamriyah), but searches against that licence number returned nothing. **Its jurisdiction, its registration status, and whether it still exists are all: Not found.**
- A dedicated recency sweep covering February 2025 to July 2026 found **zero** announcements, redemption notices, filings or partnership news for Digix, DGX, DGD or NexusGold FZC.
- Every Digix Singapore entity is **struck off**.

**Assessment: there is no live redemption path.** The gold-title company is dissolved, the redemption agent is unreachable and unverifiable, and no live channel exists through which a holder could initiate a claim. **Confidence: High** that no functioning public redemption path exists as of 28 July 2026. **Confidence: Medium** that redemption is permanently impossible: we found **no formal notice terminating redemption**, which is itself the finding. Holders were never told it ended. It simply stopped answering.

### What happened to the physical gold

**Not disclosed, and this is a serious finding.** There is no public record of what became of the metal:

- No final audit, reconciliation or PoP report covering the closure period.
- No ACRA or MAS filing describing disposition of the gold reserves.
- No statement on whether gold was liquidated, transferred to NexusGold FZC, or remains at The Safe House under different ownership.

**15,400 DGX remain outstanding, nominally representing ~15.4 kg of gold (roughly $1.5M at July 2026 prices), with no public account of where that metal is.** The bar list that PoP once published is gone with the infrastructure that served it. This is the single most damning fact in the profile, and it is the one to put in front of the client when discussing wind-down commitments.

## 7. Fees and revenue model

**This section is the one the client asked for. Read it as the specification of the mechanism Aurumix has ruled out.**

### The fee lines

| Fee line | Rate | Denominated in | Who received it |
|---|---|---|---|
| **Demurrage (storage)** | **0.60% per annum**, accrued daily | **Gold, deducted from token balance** | 0.40% to DigixGlobal, **0.20% to DigixDAO** |
| **Transfer fee** | **0.13% per transfer** (originally capped at 1 gram, cap later removed) | **Gold, deducted from the transferred amount** | **100% to DigixDAO** |
| **Recast (redemption)** | **1%** | **Gold** | DigixGlobal |
| **Minting** | None to depositor | n/a | n/a |

So DGD holders received **all** of the transfer fee plus **one third** of the demurrage. That is a real, external-facing, fee-funded revenue share: not recycled subscription fees, but a genuine usage-based cut.

### How demurrage worked mechanically

This is the part that matters, and it is worth being exact because Aurumix's peg is grams ÷ tokens.

**Digix did not change the token count. It changed what `balanceOf` returned.**

The DGX contract stored an **actual balance in nanograms** on its internal ledger, then computed the **effective balance** returned to any caller by subtracting accrued demurrage:

```
b = (a / m) * (r * t)
```

where:
- `b` = demurrage owed, netted off the effective DGX balance in nanograms (what `balanceOf` returns)
- `a` = actual DGX balance in nanograms on the internal ledger
- `m` = minimum balance unit for demurrage calculation (constant, 1 milligram)
- `r` = daily demurrage per 1 milligram
- `t` = number of days since the last demurrage deduction

The implementation used the constants `demurrage_base = 10,000,000` and `demurrage_rate = 165`, applied per **whole day** elapsed:

```
demurrage_fees = days_elapsed * user_balance * demurrage_rate / demurrage_base
days_elapsed   = (current_time - last_demurrage_payment_timestamp) / ONE_DAY_DURATION_IN_SECONDS
```

Partial days did not trigger a charge: the contract advanced `last_demurrage_payment_timestamp` by exactly `days_elapsed`, leaving the remainder to accrue. Linear accrual, not exponential, which the auditors specifically criticised.

The transfer fee used the same in-kind pattern: `transfer_fees = transfer_amount * 13 / 10,000`, **deducted from the amount sent**, so a recipient of a 100 DGX transfer received 99.87 DGX. The audit report notes this explicitly: *"fees are reduced from sent amount, and users should take this into account when using the token for payment. This behavior is non-standard in ERC20 token contracts, however is needed to support Digix business model."*

### What it did to the gold ratio: the crucial point

**It did not break the 1 DGX = 1 gram peg. It broke the holder's balance instead.**

This distinction is everything for the client. Digix preserved the invariant "1 DGX = 1 gram" by making the **number of DGX you own shrink over time**. A holder with 100 DGX had, a year later, 99.4 DGX. Each of those 99.4 tokens was still exactly 1 gram of gold. The vault held less gold, the ledger held proportionally fewer tokens, and the ratio was untouched.

That is the opposite architectural choice from Paxos, which (per the wave-1 PAXG finding) reserves the right to **mint new tokens to itself pro rata**, holding the holder's token count constant while diluting grams-per-token. Two mechanisms, opposite directions:

| | Digix demurrage | Paxos mint-to-self |
|---|---|---|
| Token count per holder | **Shrinks** | Constant |
| Grams per token | Constant | **Shrinks** |
| Effect on a 1:1 peg | Peg preserved | **Peg broken** |
| Effect on an Aurumix-style grams ÷ tokens peg | **Peg preserved** | **Peg preserved** |

**This changes the advice to the client.** The client's stated reason for ruling out gram-denominated fees is that "gram deduction breaks it [the peg]." On the Digix mechanism specifically, **that reasoning does not hold**. Aurumix's price is (vault grams ÷ tokens). If a Digix-style demurrage burns tokens pro rata while the vault pays the storage bill in gold, both numerator and denominator fall together and **the price per token is unchanged**. Digix-style demurrage is arithmetically peg-neutral for Aurumix, exactly as the wave-1 brief notes the PAXG mint-clause is.

**So the case against demurrage for Aurumix is not arithmetic. It is everything else**, and the real reasons are stronger than the stated one:

1. **It is non-standard ERC-20 and it breaks integrations.** A `balanceOf` that decreases with no transfer event violates every assumption exchanges, wallets, accounting systems and custodians make. Digix needed a separate wrapper token (**LiteDGX**) purely to present a normal ERC-20 face to the ecosystem, whose stated purpose was "No transfer fees, No demurrage fees." **Digix had to build a second token to undo its own fee mechanism.** For Aurumix, whose token additionally carries ICS standing, dividend entitlement and credit eligibility, a silently mutating balance is a direct hazard: every one of those systems reads a balance.
2. **It is hard to implement safely.** Competent auditors found a critical balance-inflation bug and a gameable fee-timing exploit, both in the fee logic.
3. **It is retail-hostile.** A savings product sold to Indian and NRI retail on a monthly SIP cannot easily explain why the number in the app went down when the customer did nothing. Aurumix's whole pitch is accumulation. A decrementing balance fights the product narrative every month.
4. **It is a visible, itemised charge on a product whose competitors charge nothing.** See §12.

Point 4 is what actually killed it.

### Did it ever generate revenue? The PMGT pattern, confirmed

**Test result: yes, Digix repeated the PMGT pattern, and did it more explicitly.**

- **Demurrage was switched off during the first year of operation** ("For the first one year, global demurrage is turned off"), so the storage fee earned nothing at launch.
- Then, in **2019, Digix zeroed it permanently.** Its own year-in-review states: *"We zeroed DGX demurrage fee so DGX holders do not have to pay the extra dollars when holding on to our gold-backed token"* ([Dev Updates, 15 January 2020](https://medium.com/digix/dev-updates-jan-15-1cd14df2426f)). Digix absorbed all storage and insurance costs itself.
- At the point of that decision, the entire fee base was **122,700 DGX**. Even at the full 0.60%, demurrage on that base was worth about **$36,000 a year gross**, of which Digix kept two thirds: **roughly $24,000 a year.** The transfer fee, on $172k of daily volume at 0.13%, was worth a few hundred dollars a day at best and went entirely to the DAO, not the company.
- So Digix gave up a revenue line worth ~$24k/yr and took on an uncapped, gold-price-linked storage and insurance liability, **permanently**.

**The arithmetic is the finding.** The demurrage fee was never large enough to fund the business, because the AUM was never large enough. Digix faced competitors (PAXG launched September 2019, the same year) charging **zero** storage. It could not hold a visible 0.60% annual charge against a zero-fee competitor, so it matched them to nil. And at that moment the DGX business had **no revenue line of its own at all**: no storage fee, no minting fee, transfer fees assigned to the DAO, and only an occasional 1% recast fee from a redemption process requiring physical presence in Singapore.

**Digix therefore entered its final phase in exactly PMGT's position: a working gold token with no revenue and no internal advocate.** The difference is that PMGT launched that way, while Digix *chose* it in 2019 under competitive pressure. Both died of the same thing.

## 8. Token architecture

- **Standard**: ERC-20, but **deliberately non-standard in behaviour**. Balances decrease without transfer events; fees are deducted from sent amounts. The 2017 audit flags this as needed "to support Digix business model."
- **LiteDGX wrapper**: a separate ERC-677/ERC-20 wrapper existed specifically to give integrators a clean, fee-free, non-decaying token. The **DGX/LiteDGX rate appreciated over time** as demurrage ate the underlying DGX held by the wrapper contract. The wrapper thus converted a *shrinking balance* into an *appreciating exchange rate*, the same economics in a form ordinary software could handle.
- **Permissioned?** No. DGX was freely transferable, no whitelist, no transfer restrictions.
- **Admin keys / upgradeability**: Digix ran a controller-based architecture (TokenTransferController, TokenApprovalController and similar), giving the operator meaningful control over token behaviour, including the ability to set demurrage to zero, which it exercised. **Confidence: Medium** on the precise key custody arrangements, which were never fully published.
- **Bridge**: none. Ethereum only, for its entire life.
- **Current on-chain state**: the contract is **still deployed and still functional**. No pause, no self-destruct. Holders can still transfer DGX to each other. **The token outlived every company that gave it meaning.**

**The DGD instrument split.** DGD was a genuinely separate governance and revenue-share token (2,000,000 fixed supply, sold in the 2016 ICO), while DGX stayed a clean asset token. This is the structure the brief identifies as our leading answer to the hybrid-regulation problem, and Digix ran it **eight years before Kinesis's KVT**. The difference: **Kinesis capped KVT at 300,000 units and sold it under an Offering Memorandum as a private placement. Digix sold DGD to the public in an unrestricted ICO.** Same structure, opposite regulatory discipline. See §12.

## 9. Liquidity and market

One paragraph, per the wave-1 instruction not to re-argue the premium thesis.

DGX today: **15,400 tokens outstanding** (~15.4 kg gold), ~2,103 holders, ~$278k on-chain market value, price tracking gold at ~$18.52/g, and **24-hour trading volume of nil**. Trackers show stale price stamps from May 2026 against a July 2026 date, the signature of an asset with no trades to update it. Bitfinex delisted DGX on **18 June 2021**; no major exchange lists it today. At peak (January 2020) DGX had 122,700 tokens, ~$6.0M market cap, $172,274 daily volume, 1,751 holders and listings on 12 exchanges. DGD trades at ~$0.067 against an all-time high of $1,291, a **99.99% decline**, with **$0** 24-hour volume: the correct price for a token whose only remaining function is to be burned for its ETH claim. **Digix adds a terminal data point to the settled conclusion: no premium, and eventually no market at all.**

## 10. Distribution

- **Channels**: direct via the Digix marketplace, plus exchange listings (12 by end-2019) and DEX integrations (AirSwap, Tokenlon/imToken). Trading pairs in 7 quote currencies (ETH, USD, IDR, USDT, DAI, BTC, VND).
- **Geography**: Singapore base, with a documented push into **Indonesia and Vietnam** (IDR and VND pairs) and a China marketplace opening in 2019. Notably retail-oriented and **Asian-emerging-market focused**, which is the closest geographic analogue in the set to Aurumix's India/NRI target.
- **Savings plan / recurring purchase**: **None found.** No SIP, no auto-invest, no recurring contribution mechanism.
- **Referral / affiliate / agent network**: **None found.**
- **Target segment**: crypto-native holders wanting gold exposure, not savers.

**The finding for the client is the gap.** Digix reached emerging-market Asian retail through **exchange listings**, which is a passive channel: it waits for people who already hold crypto. It built no acquisition mechanism, no recurring contribution, and no commissioned distribution. Over eight years it accumulated ~$6M peak AUM. **Aurumix's agent network and SIP are, on this evidence, the genuinely differentiated part of its design**, and Digix is the cautionary case for what happens without them: a technically excellent product with no engine to acquire customers.

## 11. Wind-down timeline

Dated, reverse chronological.

| Date | Event |
|---|---|
| **19 July 2026** | **DIGIX HOLDINGS PRIVATE LIMITED (UEN 201724450M) struck off the Singapore register**, having been gazetted 6 April 2026. The last Digix entity to go ([RecordOwl](https://recordowl.com/company/digix-holdings-private-limited)) |
| **6 April 2026** | Digix Holdings gazetted for strike-off by ACRA |
| **Feb 2025 – Jul 2026** | **Total silence.** A dedicated recency sweep found no announcements, filings, redemption notices, incidents or partnership news for Digix, DGX, DGD or NexusGold FZC anywhere in this window |
| **28 July 2026 (tested)** | digix.global: **connection refused**. nexusone-dgx.com: **connection refused**. Digix Zendesk: **403 Forbidden**. No live redemption channel exists |
| **4 September 2023** | **DIGIX MARKETS PTE. LTD. (201906348R) and DIGIX PHYSICALS PTE. LTD. (201724269N) struck off** by ACRA Final Gazette. **The entity holding legal title to the gold ceased to exist** |
| **4 July 2023** | ACRA First Gazette: Digix Markets and Digix Physicals notified for striking off |
| **21 March 2023** | **Digix ceases operations.** Redemption facilities handed to **NexusGold FZC** (licence 4306536.01), an overseas partner whose jurisdiction and current status we could not verify |
| **September 2022** | **Digix Holdings withdraws its Payment Services Act licensing in Singapore** and announces: *"We regret to inform you that we will not be taking any more new transactions and would be ceasing all business activities"* ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)) |
| **18 June 2021** | **Bitfinex delists DGX**, trading ceased 12:00 UTC ([Bitfinex](https://support.bitfinex.com/hc/en-us/articles/360008482333-Digix-Gold-Delisted)) |
| **March 2020** | **"Acid" refund contract deployed** at `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`. DGD holders burn DGD for ETH at a fixed **0.193054178 ETH per DGD**. No deadline |
| **12 May 2020** | Bittrex snapshot of DGD balances for exchange-side distribution. Binance, Gate and others distribute ETH to holders at the same fixed ratio |
| **~February 2020** | DGD unstaked at the start of the following Digix quarter; ETH distributions begin |
| **20 January 2020** | **DigixDAO votes to dissolve.** "Project Ragnarok" passes with **>95% support on only 52 votes cast** (against ~11,000 DGD addresses). Treasury: **~386,428 ETH, ~$64M**. **Digix the company opposed the dissolution and abstained** ([CoinDesk](https://www.coindesk.com/markets/2020/01/20/digixdao-votes-to-liquidate-64m-treasury)) |
| **29 November 2019** | **Kai Cheng Chng publishes the Project Ragnarok proposal**, offering a quarterly dissolution vote in response to demands for "a mechanism for dissatisfied DGD token holders to make a clean break." States: *"Digix is against the dissolution"* and will abstain, but will *"respect and adhere to the collective opinion [of] DGD holders"* ([proposal](https://medium.com/digix/proposal-announcement-project-ragnarok-integrating-a-dissolution-mechanism-for-digixdao-354fd871e3e0)) |
| **2019** | **Digix zeroes the DGX demurrage fee permanently**, absorbing storage and insurance costs itself. The DGX business loses its only recurring revenue line |
| **September 2019** | PAXG launches with zero storage fee, into the same market |
| **March 2016** | DGD ICO raises **466,648 ETH** (~$5.5M) in the first major Ethereum token sale |
| **December 2014** | Digix founded in Singapore |

### What actually drove the wind-down

The causal chain, stated plainly:

1. **DGX never achieved scale.** Peak AUM ~$6M after five years. The gold token was a product almost nobody bought.
2. **Because DGX had no scale, its fees could not fund the company.** Full-rate demurrage on peak AUM was ~$24k/yr to Digix.
3. **Competitive pressure from zero-fee entrants (PAXG, September 2019) forced the fee to zero in 2019.** Digix could not defend a visible 0.60% charge against a free competitor, so it eliminated its own revenue and absorbed the storage cost.
4. **The company had been living on the ICO treasury, not on revenue.** DGD's price tracked the ETH in the treasury almost exactly, which told the market the operating business was contributing no independent value. As one analysis put it: *"if DGD's total market cap mirrors the total value of ETH in the DigixDAO treasury, the money spent from the treasury must be getting wasted."*
5. **Holders noticed and voted to take the treasury back.** Ragnarok passed over management's objection on 52 votes. **~$64M left the ecosystem.**
6. **A revenue-less company minus its treasury has no runway.** DGX had no fees, no scale, and now no subsidy.
7. **Wind-down followed**: PSA licence withdrawn and business ceased (Sept 2022), operations ended and redemption outsourced offshore (March 2023), title-holding entity struck off (Sept 2023), parent struck off (July 2026).

**The DAO dissolution was not the wind-down mechanism. It was the trigger.** The brief's framing has this backwards, and the correction matters: a well-executed structured treasury return to one class of holders was, from the other class's perspective, the removal of the subsidy that kept their gold redeemable.

## 12. Relevance to Aurumix

Digix is the most instructive failure in the set because it did the engineering well and the business badly.

### 1. The demurrage question, answered precisely (client design question 1)

**The client's stated reason for ruling out gram-denominated fees is wrong, but the conclusion is right for better reasons.** Digix-style demurrage burns tokens pro rata, holding grams-per-token constant. Against Aurumix's grams ÷ tokens peg it is **arithmetically neutral**. If the client is defending this decision to a technical reader, "gram deduction breaks the peg" will not survive scrutiny. **Use these reasons instead**: it makes `balanceOf` non-standard and breaks every downstream integration (Digix needed a whole second token, LiteDGX, to work around its own mechanism, and Aurumix's ICS, dividend and credit systems all read balances); competent auditors found a critical bug and a timing exploit in the fee logic itself; and a decrementing balance is indefensible in a monthly-SIP savings product sold to retail. **Charge in cash.**

### 2. The zero-fee trap, now confirmed twice (client design question 1)

PMGT launched with zero fees and had no internal advocate. **Digix started with fees, could not defend them against a zero-fee competitor, and cut them to nil in 2019.** Then it died. The wave-1 conclusion that "zero ongoing custody fee is the near-universal norm" now has a mechanism attached: **it is not a norm, it is the equilibrium of a price war that no small issuer survives, because the fee is visible and itemised while the competitor's is zero.**

The strategic read for Aurumix is that a **visible, itemised custody fee on a commodity gold product is competitively indefensible**. Aurumix's escape route is that **it is not selling a custody product**. It is selling a savings plan with ICS tiers, credit access and a dividend. Fees should be attached to those distinguishing services, where there is no zero-fee competitor, and not to the storage of gold, where there is. This is the strongest available argument for the client's "recover cost elsewhere" option.

### 3. Wind-down: the most valuable finding in this profile (client design question 9)

**Digix is the proof of the client's cheapest differentiator.** Follow the metal:

- 15,400 DGX still exist, nominally ~15.4 kg of gold, ~$1.5M.
- The company that held legal title to that gold was **struck off on 4 September 2023**.
- **No public record exists of what happened to the metal.** No final audit, no reconciliation, no disposition filing.
- Holders received **no formal notice that redemption had ended**. The portal simply stopped responding.
- The redemption agent it was handed to cannot be verified in any register.

This is the concrete, documented answer to "what happens if the issuer fails." **The gold vanishes from the public record and the holder is left with a live token, a dead counterparty, and no forum.** Aurumix committing ex ante to a wind-down protocol (a named successor custodian, a defined notice period, a final published reconciliation, and a mechanism that survives issuer strike-off) costs nothing at design time and is a genuine differentiator against every protocol in this landscape.

**Add one Digix mechanism directly**: the **automatic re-mint of uncollected gold**. It solves abandoned redemptions without ever leaving the token unbacked, and it is the kind of detail that signals real operational thinking.

### 4. The instrument split, with the regulatory lesson attached (client design questions 2 and 3)

Digix ran the two-token split (clean DGX asset token, separate DGD revenue-share token) **eight years before Kinesis**. It validates the structure the brief calls our leading answer to hybrid regulation, but it adds the essential caveat.

**Kinesis capped KVT at 300,000 and sold it privately under an Offering Memorandum. Digix sold DGD to the public in an unrestricted ICO. Same structure, opposite discipline, opposite outcome.** DGD became a liquid, publicly traded claim on a corporate treasury held by ~11,000 addresses who could vote to seize it, and did.

**The direct warning for the ICS Dividend**: if Aurumix's dividend entitlement is freely transferable and publicly traded, it becomes an instrument whose holders can act collectively against the operating company. Digix's management lost control of $64M of its own balance sheet to a 52-vote poll. If Aurumix separates its dividend right into a distinct instrument, **cap it, place it privately, and do not give it governance power over treasury assets.** The client's lean toward a permissioned base (ERC-3643) is well supported here.

### 5. The DGD treasury return: what holders actually got (client's specific question)

**Mechanism**: the "Acid" refund contract at `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`. A holder approves DGD to the contract and calls `burn()`, which **permanently burns the DGD** and sends ETH pro rata.

**Ratio**: **0.193054178 ETH per DGD**, fixed. Applied identically on-chain and by exchanges (Binance, Bittrex, Gate) that ran the conversion for their users.

**Voluntary or governed?** **Both, in sequence, and the distinction is the interesting part.** It was governed by a formal on-chain governance document (the Project Ragnarok proposal, 29 November 2019) and executed through DigixDAO's standard project-voting machinery with quota and quorum requirements. But the **company opposed it and abstained**, and complied because it had pre-committed to respect the outcome. The *claim* is then voluntary and perpetual: **no deadline, still open, and ~12,491 ETH remains unclaimed** six years later.

**Two observations.** First, this is the **only well-executed wind-down mechanism found anywhere in this landscape**: a fixed ratio, an open-source contract, no deadline, and no discretion left with the issuer. It is a good model, and Aurumix should copy its properties (fixed formula, permissionless claim, no expiry, no issuer discretion) for its own wind-down commitment. Second, note what it protected and what it did not: **DGD holders got a clean, precise, permanent exit. DGX holders, whose tokens were backed by actual gold, got a dead website.** The governance token holders were made whole; the asset token holders were abandoned.

**That asymmetry is the lesson.** Aurumix must ensure its wind-down protections attach to the **gold-holding retail saver**, not to whichever class happens to hold the governance rights.

### 6. Not applicable

Digix paid **no yield to DGX holders** (question 2 is not directly addressed beyond the DGD fee share, which was genuine external usage revenue, not recycled subscriptions). It had **no savings plan, referral or agent distribution** (question 8: the finding is the absence, and it is a large part of why Digix never scaled). It **held no licence** to compare on question 4.

## 13. Open items for verification

- [ ] **Locate the physical gold.** Contact The Safe House Singapore to establish whether gold formerly held for Digix Physicals Pte Ltd remains in the vault and in whose name. This is the single highest-value unresolved fact.
- [ ] **Verify NexusGold FZC** against UAE free-zone registers (Hamriyah, SAIF Zone, Sharjah Media City, RAKEZ, Ajman) using licence number **4306536.01**. Establish its jurisdiction, current status, and whether it ever operated a DGX redemption facility.
- [ ] Determine the **bona vacantia position** of assets held by Digix Physicals Pte Ltd at strike-off (4 September 2023), and whether any application to restore the company to the register has been made.
- [ ] Obtain the **actual MAS Payment Services Act record** for Digix Holdings: licence class, application status, and the formal disposition of the September 2022 withdrawal.
- [ ] Confirm the **current ETH balance of the Acid refund contract** (`0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`) directly on-chain; the ~12,491 ETH unclaimed figure needs a dated on-chain check.
- [ ] Retrieve the **DGX custody agreement or terms of issue** from web archives to confirm the legal-title analysis in §2 against a primary document rather than secondary commentary.
- [ ] Verify the **exact date and text of the Digix tweet** announcing cessation of business activities (September 2022); we have the quote via IQ.wiki but not the primary post.
- [ ] Pull the **PoP / bar-list records from IPFS** if any pinning survives, to establish the last published bar inventory before shutdown.
- [ ] Check whether **DGD's 0.193054178 ETH/DGD ratio** was ever challenged or litigated, and whether unclaimed ETH has any escheatment exposure.
- [ ] Establish whether **Digix Markets Pte Ltd** (SSIC "fund management activities n.e.c.", incorporated Feb 2019) ever conducted regulated fund management, which would be a separate MAS licensing question.

---

# CACHE Gold (CGT)

> **Correction to our own working note, stated up front.** Our standing brief says Cache Gold "wound down quietly with no post-mortem and the fate of residual gold unverified," and Part 3 of the landscape brief lists it alongside PMGT and Digix as a protocol that never published a wind-down plan. **Both statements are wrong and should be struck.** CACHE published a contractual compulsory-redemption mechanism (Clause 5A of its Terms of Service, effective 19 June 2025), gave at least three months' notice through defined channels, ran a redemption window, and executed a migration into PAXG. It is, on paper, **the only protocol in our entire set that documented its own wind-down in advance and then followed the document.** That makes it far more useful to Aurumix than a quiet death would have been: it is a live test of whether a well-drafted wind-down clause actually protects holders.
>
> The second finding is that it largely did not. **100,771.01 CGT remain outstanding today across 136 addresses, and the total supply has not moved by a single unit since before the snapshot.** The redemption paid out to two addresses. The rest is a claim on nothing.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | CGT | **High** |
| Status | **Wound down.** Ceased to be gold-backed 30 September 2025, 23:59:59 SGT | **High** |
| Issuer (marketing) | CACHE / CACHE Gold | **High** |
| Issuer (registry) | **CACHE PRIVATE LIMITED, Singapore UEN 201827110K, incorporated 8 August 2018** | **High** |
| Register status today | **LIVE COMPANY.** Not struck off, not dissolved, not in liquidation | **High** |
| Domicile | Republic of Singapore. Registered office 6 Changi South Street 3, #01-01 BOXPARK @ Chai Chee, Singapore 486128 | **High** |
| Backing claim | 1 CGT = 1 gram allocated fine gold in an Approved Vault (until 30 Sep 2025) | **High** |
| Chains | Ethereum mainnet only | **High** |
| Contract address | `0xf5238462e7235c7b62811567e63dd17d12c2eaa0` (ERC-20, 8 decimals) | **High** |
| Supply today | **100,771.01 CGT**, unchanged since before the wind-down snapshot | **High** |
| Holders today | **136 addresses** | **High** |
| Market cap / TVL | **Zero.** Tokens are contractually unbacked; no price feed | **High** |
| Regulatory status | Singapore **PSPM Dealer, Registration No. PS20190001508**, verified live on the MinLaw register | **High** |
| Subscription fee | Not disclosed (marketplace pricing, spread-based) | **Not disclosed** |
| Ongoing custody fee | **0.25% p.a. storage fee, deducted in CGT tokens on-chain** | **High** |
| Transfer fee | **Up to 0.10% of CGT transferred, deducted in CGT on-chain** | **High** |
| Inactivity fee | **0.50% p.a. on addresses dormant 3 years, in CGT** | **High** |
| Redemption fee | Marketplace-variable; plus VAT/GST and shipping at holder's cost | **Medium** |
| Advertised yield | **None.** Terms expressly deny any dividend or revenue share | **High** |
| Named officers | Gregor Gregersen (Director/CEO), Nizam Ismail (Director) reported; 4 officers on register | **Low** |
| Trustee | **None. No trustee, no bankruptcy-remote structure anywhere in the Terms** | **High** |

---

## 1. What it is

CACHE Gold was an Ethereum ERC-20 token, each unit representing one gram of allocated fine gold held in third-party vaults, issued by CACHE Private Limited of Singapore. The contract was deployed on **17 February 2020**. Its distinguishing pitch was bar-level transparency: the **GramChain** asset-tracking system published per-bar photographs, gross weight, purity, brand, **serial number** and vault location, refreshed by the vault personnel physically handling the bars, and broadcast to Ethereum. Redemption was offered in three forms: collection in person from a vault, insured shipping to a verified residential address, or sale to a participating gold dealer for fiat.

It is the best test case in our set precisely because it did the disclosure work properly. If bar serial numbers and a documented redemption right are worth anything at the moment an issuer stops operating, CACHE is where that value should show up.

The token is now defunct. Per the issuer's own notice dated **1 October 2025**, CGT "ceased to be backed by gold as of 30 September 2025, 23:59:59 (Singapore Time)" (https://cache.gold/).

---

## 2. Legal structure

**What a holder actually owned: an economic claim against the issuer, not title to gold, and not a trust interest.** This is the single most important structural fact about CACHE, and it is what determined the outcome.

The Terms of Service effective 19 June 2025 (https://cache.gold/assets/media/CACHE-Terms-of-Service-Effective-19th-June-2025.pdf) draw the line in two clauses that sit uncomfortably together:

> "1.1.1. CGT is an ERC-20 token on the Ethereum blockchain, representing the **beneficial ownership** of one (1) pure gram of Allocated Gold stored in an Approved Vault. A Token Holder therefore holds **the economic value** of the gold a CGT represents."

> "1.2.3. A Token Holder shall not have any other rights in relation to CACHE **other than the economic value of 1 gram of Gold per CGT**. CGT does not represent or confer any ownership right or governance right or stake, share or security or equivalent right, or any right to receive any dividend, share in revenue or any form of voting right or participation right in CACHE."

Clause 1.1.1 says "beneficial ownership" and then immediately reduces it to "the economic value." Clause 1.2.3 removes any ownership right at all. **Show both, because they disagree**: the marketing-facing sentence offers beneficial ownership of an identified allocated bar, and the operative sentence delivers a contractual value claim. When the issuer decided to close, the operative sentence governed. Holders had no proprietary interest they could assert over specific serial-numbered bars.

Clause 1.1.2 further disclaims that CGT is "a security token, a digital payment token, derivative, commodity, a share or security, an interest in a managed investment scheme, or any kind of financial instrument," and notes it "is not covered by any national deposit insurance scheme."

**No trustee. No bankruptcy-remote vehicle. No security interest.** A full-text search of the 22-page Terms returns no instance of "trustee," "trust deed," "bankruptcy remote," or any equivalent. The gold sat in third-party vaults under arrangements between CACHE and the vault operators, to which the token holder was not a party. **Confidence: High** (primary document, negative search recorded).

This is the structural difference between CACHE and a custody arrangement that would have survived the issuer. Because there was no trust and no trustee, at the moment CACHE chose to stop honouring the tokens there was no independent fiduciary with a duty to the holders and standing over the bars. The serial numbers identified gold that nobody was obliged, to the holder, to deliver.

---

## 3. Regulatory and compliance posture

**Regulator and licence, verified against the register:** CACHE PRIVATE LIMITED holds Singapore **Precious Stones and Precious Metals (PSPM) Dealer registration PS20190001508**, under the Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019, administered by the Registrar of Regulated Dealers at the Ministry of Law.

I verified this directly against the official government dataset rather than accepting the issuer's assertion. Querying the MinLaw "List of Registered Dealers" dataset on data.gov.sg (resource `d_e643dd525fb927ee16f54f093c73b490`, https://data.gov.sg/datasets/d_e643dd525fb927ee16f54f093c73b490/view) for "CACHE" returns exactly one record:

```
{'name': 'CACHE PRIVATE LIMITED', 'registration_number': 'PS20190001508'}
```

The issuer's self-description in Clause 7.1(b) is therefore accurate. **Confidence: High.**

**What that licence is and is not.** A PSPM dealer registration is an **anti-money-laundering registration**, not a financial services or capital markets licence. It obliges the holder to do KYC, record-keeping and suspicious transaction reporting when dealing in precious metals. It confers no prudential supervision, no client-asset segregation requirement, no capital requirement, and no conduct regime for token issuance. Clause 7.1(b) claims the registration means CACHE "is qualified to buy, sell, store, and issue precious metals or precious metals backed tokens like CGT." That is the issuer's characterisation; an AML dealer registration is not an authorisation to issue investment products, and the claim should be read as marketing.

**What I checked and did not find:**
- **No Monetary Authority of Singapore licence of any kind.** CGT was expressly structured to fall outside the Payment Services Act by disclaiming digital payment token status (Clause 1.1.2). No MAS Capital Markets Services licence, no Recognised Market Operator status, no MAS-approved prospectus.
- **No MAS enforcement action, reprimand or supervisory notice against CACHE Private Limited or CACHE Gold.** Searched; not found.
- **No regulator compelled or supervised the wind-down.** The closure was a commercial decision executed under the issuer's own contract terms.

**This matters for §12: CACHE was not killed by a regulator, and no regulator oversaw its exit.** There was no authority with jurisdiction to ask where the gold went.

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodians | **Brink's, Loomis, Dillon Gage IDS (International Depository Services), The Safe House** | **Medium** |
| Vault cities | Partner vaults reported across **Singapore, Dubai, Frankfurt, Dallas, Zurich**; per-custodian city mapping never published | **Low** |
| Allocated? | Yes, claimed: "Allocated Gold stored in an Approved Vault" (Clause 1.1.1) | **High** (as a claim) |
| Bar list with serial numbers | **Yes, published while operating.** Per-bar photos, gross weight, purity, brand, serial number, location via GramChain | **High** |
| Bar list today | **OFFLINE.** `explorer.cache.gold` returns HTTP 404 | **High** |
| PoR feed | GramChain, described as real-time, updated by vault personnel | **Medium** |
| **Reserve attestation** | **Never published by a named audit firm on a stated date. Not found.** | **High** (negative finding) |
| **Smart contract audit** | No published report located from any named auditor | **High** (negative finding) |

**The attestation gap, stated sharply.** Per the wave-1 correction that "audited" almost always means smart-contract audited and not reserve attested, I separate the two here, and for CACHE **neither is evidenced**. The strongest statement located is that the vaults themselves "are also independently audited and insured," which is an assertion about the vault operators' own general audit arrangements, not an attestation over the CGT gold reserve, and it names no firm and gives no date. A vault operator being audited as a business is not the same as an independent accountant confirming that a specific quantity of gold backing a specific token supply exists on a specific date.

So the transparency stack was: **very strong on granular bar data, entirely absent on independent verification.** GramChain showed you photographs and serial numbers supplied by the same commercial chain that had an interest in them being right. No third party ever signed a report saying the total matched the token supply.

**The transparency stack is now gone.** Verified live on 28 July 2026:

| URL | Status |
|---|---|
| `https://explorer.cache.gold/` | **404** |
| `https://cache.gold/whitepaper` | **404** |
| `https://cache.gold/cache-supply` | **404** |
| `https://cache.gold/cache-gold-fees` | **404** |
| `https://cache.gold/sell-your-gold` | **404** |
| `https://cache.gold/build` | **404** |
| `https://cache.gold/` | 200: wind-down notice only |
| `https://cache.gold/terms-of-service` | 200 |

**The Terms of Service still in force on the live site cite URLs that no longer exist.** Clause 1.1.1 directs holders to `https://cache.gold/whitepaper` and Clause 6.3.4 to `https://cache.gold/storage-fee-methodology`. Both are 404. The contract governing the tokens 136 addresses still hold points at documentation the issuer has deleted.

**GramChain itself outlived CACHE.** `gramchain.net` still resolves and serves (HTTP 403 to an automated request, indicating a live bot-protected host). Clause 9.5.2 explains why the two can be separated: the GramChain intellectual property belongs to **Little Bit Pte Ltd**, a different company, not to CACHE. The tracking technology was licensed in, so it did not die with the issuer, but the CGT-specific bar records it hosted are no longer reachable through any CACHE endpoint.

**Net effect on the serial numbers.** CACHE published bar-level serial numbers for years. Today there is no public record of which bars backed CGT, because the only interface that mapped tokens to bars has been taken down by the issuer. **The serial numbers were real while they did not matter, and unreachable the moment they would have.**

---

## 5. Issuance

Issuance ran through the **CACHE Marketplace**, a permissioned platform requiring registration and full KYC as a "Verified User" (Clauses 2.1.1 and 2.1.2: name, corporate information on shareholders/beneficial owners and directors, email, phone, residential address, date of birth or incorporation, government ID, proof of address, and in some cases source of funds or source of wealth). A Verified User delivered gold, or bought it from a participating dealer, and CGT was minted against it.

Note the asymmetry that runs through the whole design and drives the final outcome: **minting was permissioned and KYC'd, but the token itself was an anonymous bearer instrument.** Clause 1.2.1: "You become a CGT Token Holder by controlling the private key of an address holding CGT." Clause 5A.2 acknowledges this directly, referring to "Token Holders who do not have a CACHE Marketplace Account" and describing "CGT is a public bearer token."

CACHE knew, in the contract, that it had holders it could not identify or contact. It wrote the notice provisions around that fact rather than around solving it.

Reported venture funding of ~$17M in a Q3 2021 private round with Dillon Gage and Palisades Goldcorp named as backers appears on an ICO aggregator (https://icodrops.com/cache-gold/). No primary confirmation located, and Perplexity searching the issuer's own materials found none. **Confidence: Low.** Dillon Gage's confirmed role was as a vault operator (IDS) and participating gold dealer; whether it was also an equity investor is **not established**.

---

## 6. Redemption

While operating, redemption terms were genuinely good, and better than most of the set:

- **Three exit routes** (Clause 5.2): (a) in-person collection from an Approved Vault, (b) insured shipping to a linked residential address, (c) sale to a participating gold dealer for fiat.
- **Minimums as small as 100 grams** for physical bars, materially more retail-accessible than PAXG's or XAUT's practical thresholds.
- **Eligibility was open**, not restricted to undefined "qualified holders." This is a favourable contrast with several protocols in the set.
- **Frictions**: redemption required a Marketplace account and full KYC, so a bearer holder had to onboard first; the redemption transaction had to land within 10 minutes of the order to hold the locked price (Clause 5.3); it had to come from the Linked Ethereum Address (Clause 5.4); and VAT/GST, customs and shipping costs fell on the holder (Clauses 5.5.3, 5.6.3).

**The redemption right was extinguished by contract on 30 September 2025.** Clause 5.1 opens "You may, at any time, **subject to clause 5A**, redeem your CGT tokens." Clause 5A is the kill switch, examined in §11.

---

## 7. Fees and revenue model

**This section is the direct answer to the wave-1 instruction to test CACHE for the PMGT commercial-abandonment pattern. The answer is that the pattern does not fit, and the reason it does not fit is more interesting than if it had.**

| Fee line | Rate | How collected | Confidence |
|---|---|---|---|
| Transfer fee | Up to **0.10%** of CGT transferred | **In CGT tokens, automatically on-chain**, whenever a transfer is initiated (Clause 6.1.1) | **High** |
| Storage fee | **0.25% per annum** | **In CGT tokens**, collected "every time a transaction is initiated on the Ethereum Address holding the CGT tokens" (Clause 6.2.1) | **High** |
| Inactivity fee | **0.50% per annum** on addresses with no CGT transaction for 3 years, in lieu of the storage fee | **In CGT tokens**, on the balance as at the date of inactivity (Clauses 6.3.1–6.3.2) | **High** |
| Redemption / marketplace fees | Variable, quoted in the Marketplace | Cash / deducted from proceeds (Clause 6.4.1) | **Medium** |
| Advertised yield | **None** | Clause 1.2.3 expressly denies any dividend or revenue share | **High** |

**CACHE did charge, and PMGT did not. That is the key contrast.** PMGT died of commercial abandonment under a zero-fee model: no revenue meant no internal advocate. CACHE ran a **0.25% p.a. storage fee plus a 0.10% transfer fee plus a 0.50% p.a. inactivity fee**, which on the face of it is a real revenue model, and it is close to the *only* protocol in our set that charged an ongoing custody fee at all. The wave-1 finding that "zero ongoing custody fee is the near-universal norm" holds across PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus and PGOLD. **CACHE is the exception that charged, and it is also the one that closed.**

**But the collection mechanism made the fee largely theoretical, and this is the finding that matters most for Aurumix's Question 1.** Read Clause 6.2.1 carefully: the storage fee accrues at 0.25% per annum but **is only actually collected "every time a transaction is initiated on the Ethereum Address holding the CGT tokens."** A holder who bought CGT and never moved it paid nothing, indefinitely, no matter how much storage cost accrued in the meantime. Revenue was therefore a function of **transaction frequency, not assets under management.**

That is exactly backwards for a gold savings product. The behaviour a gold token is designed to attract, buy and hold for years, is the behaviour that generates zero revenue while consuming real vault cost every single day. CACHE's own inactivity fee, a 0.50% p.a. charge on 3-year-dormant addresses, is the tell: it is a patch bolted on to reach precisely the holders the storage-fee mechanism could never touch. And it too could only be realised on a transaction.

Now run the arithmetic on what that produced. Total supply at the end was **100,771 grams**, roughly 3.24 tonnes... no: 100.77 kg. At a gold price around $3,800/oz in 2025, that is roughly **$12.3M of AUM**. A 0.25% annual storage fee on $12.3M is about **$31,000 per year gross**, and CACHE only collected the fraction of that triggered by actual transactions. The contract shows **10,200 transfers over its entire five-and-a-half-year life**, an average of about five per day. Against Singapore staffing, four vault relationships across multiple countries, insurance, KYC compliance under the PSPM Act, and the GramChain licence from Little Bit Pte Ltd, a five-figure annual gross fee take is not a business.

**So the corrected diagnosis is this: CACHE did not die of charging nothing, like PMGT. It died of charging a fee that its own collection mechanism prevented it from actually collecting, on an asset base far too small to support the operation.** The disease is the same, revenue that could never cover the cost of custody. The mechanism differs, and the difference is instructive: **having a fee on paper is not the same as having revenue.** No enforcement action, no hack, no reserve shortfall, no scandal, and no regulator involved. Commercial non-viability, confirmed.

**The in-kind fee mechanism is directly relevant to Aurumix's Question 1 and to the PAXG dilution clause from wave 1.** CACHE deducted its fees **in grams of gold** by taking CGT tokens, not in cash. For a 1-token-1-gram product, this is peg-breaking in the same way the Paxos mint-to-self clause is: the fee reduces the holder's gram count rather than the gold-per-token ratio. Aurumix's peg is grams ÷ tokens, so an in-kind deduction that burns tokens and gold proportionally would be peg-neutral, but CACHE's specific design, deducting tokens on transfer, is a template of how *not* to fund custody: it taxes exactly the activity a savings product wants to encourage and exempts exactly the behaviour that costs the issuer money.

---

## 8. Token architecture

- **Standard**: plain **ERC-20**, 8 decimals, Ethereum mainnet only, contract `0xf5238462e7235c7b62811567e63dd17d12c2eaa0`, deployed **17 February 2020**. No bridge, no multi-chain deployment.
- **Permissioned?** **No.** Free transfer to any address. Minting and redemption were permissioned and KYC-gated at the marketplace layer, but the token in circulation was an anonymous bearer instrument. **This is the architectural decision that produced the orphaned supply in §11.**
- **Fee logic in the contract**: the transfer, storage and inactivity fees were enforced in the token contract itself, deducting CGT on transfer. Clauses 6.1.2 and 6.2.2 construct this as an obligation that runs with the token: "By acquiring CGT tokens, Token Holder agrees to assign the obligation to pay such fees to subsequent Token Holders... Likewise, by receiving transfers of CGT tokens, Token Holders agree to accept the assignment of such obligation." An elegant piece of drafting that binds a bearer holder who never signed anything, and CACHE relied on the same bearer-consent theory for the compulsory redemption in Clause 5A.7.
- **Admin keys**: the contract has an owner at `0xb779efeeda6cf887b80bc386e7eb9fdced6753f6`, which is the same address that executed the PAXG airdrop. **No published smart contract audit located from any named firm.**
- **Contract still live**: not paused, not self-destructed. Transfers still execute. Three transfers occurred as recently as **26 July 2026**, two days ago (all zero-value spam). The token functions perfectly; it just represents nothing.

---

## 9. Liquidity and market

One paragraph, per the wave-1 instruction not to re-argue the premium thesis.

CACHE was a very small protocol. Final supply was **100,771 grams (~100.8 kg, ~$12.3M at 2025 prices)**, and a dated 2020 audit walkthrough put supply at only 34,301 grams, so the token roughly tripled over five years and never reached scale. **136 holders.** **10,200 transfers over its entire life**, about five per day. Listings were thin: NBX (Norwegian Block Exchange) is the one confirmed venue, and Silver Bullion Singapore offered it. No meaningful DEX liquidity was located; no daily volume data is published for its final two years. There is no price feed today. CACHE adds one more data point at the far illiquid end of the spectrum, consistent with the settled conclusion: it had no market capable of expressing a premium, and its problem was never pricing but that ~$12M of AUM cannot pay for four vault relationships in five cities. **The distribution is now grotesquely concentrated: one address holds 96.03% of the entire remaining supply.**

---

## 10. Distribution

Direct-to-consumer through the CACHE Marketplace, plus exchange listings and bullion-dealer partnerships (Silver Bullion Singapore, Dillon Gage as a participating dealer). Target segment was gold investors wanting bar-level provenance, and B2B tokenization-as-a-service for other asset issuers.

**No savings plan, no recurring-purchase or SIP mechanism, no referral programme, no affiliate scheme, no agent network, no tiering.** Searched the Terms and all surviving materials; none found. This is consistent with the wave-1 pattern: **no protocol in the set has built anything resembling Aurumix's monthly-contribution agent-network model.** For CACHE the absence is doubly relevant, because a recurring-contribution product generates recurring transactions, and recurring transactions were the only thing that triggered CACHE's storage fee. A savings-plan distribution model would have partially fixed its revenue problem by accident.

---

## 11. Wind-down timeline

Dated, reverse chronological. On-chain facts verified directly against Ethereum mainnet via RPC and the Ethplorer API on 28 July 2026.

| Date | Event | Source / verification |
|---|---|---|
| **28 July 2026 (today)** | **CGT total supply: 100,771.01 tokens across 136 holders. Unchanged.** Contract live and transferable. Tokens are contractually unbacked and worthless | `eth_call totalSupply()` at current block |
| **26 July 2026** | Three zero-value spam transfers, the most recent activity on the contract | Ethplorer token history |
| **28 July 2026** | **Cache Private Limited remains a LIVE COMPANY on the ACRA register.** Not struck off, not dissolved, no liquidator appointed, 10 months after ceasing to honour its tokens | opengovsg.com/corporate/201827110K; recordowl.com/company/cache-private-limited |
| **28 July 2026** | **PSPM Dealer registration PS20190001508 still listed on the MinLaw register of registered dealers** | data.gov.sg dataset `d_e643dd525fb927ee16f54f093c73b490`, queried directly |
| **28 July 2026** | **Transparency stack confirmed offline**: `explorer.cache.gold`, `/whitepaper`, `/cache-supply`, `/cache-gold-fees`, `/sell-your-gold`, `/build` all return HTTP 404. Only the homepage notice and the Terms of Service survive | Direct HTTP requests |
| **17 November 2025** | **Second and final airdrop payment: 15.785912 PAXG (491.0 g) to a single address** (`0x8249f32c...`), block 23817845. This is 7 weeks *after* the compulsory redemption date and 17 days after the 31 October inquiry deadline, so it appears to be a manually handled late claim | `eth_getLogs` on PAXG contract, sender = CACHE owner address |
| **18 November 2025** | That recipient immediately swapped the entire 15.79 PAXG for ~$62,479 USDC | Ethplorer address history |
| **31 October 2025** | Deadline for eligible holders who did not receive PAXG to contact support@cache.gold. **After this date the issuer offered no further route to anything** | https://cache.gold/ |
| **1 October 2025** | **Airdrop executed: 60.180957 PAXG (1,871.8 g) to a single address**, blocks 23480178 and 23480280 | `eth_getLogs` on PAXG contract |
| **1 October 2025** | CACHE publishes notice: "the airdrop of Pax Gold (PAXG) tokens has been **successfully completed** in accordance with the compulsory redemption process set out in Clause 5A" | https://cache.gold/ |
| **30 September 2025, 23:59:59 SGT** | **Compulsory Redemption Date.** CGT ceases to be backed by gold and is "no longer recognized, honored, or redeemable by CACHE." Snapshot taken at the last block before this time | Clause 5A.4; https://cache.gold/ |
| **26 September 2025, 23:59:59 SGT** | Last date for manual redemption of CGT for physical gold or fiat through the CACHE website | https://cache.gold/ |
| **~19 June 2025** | **Compulsory Redemption Notice period begins.** Terms of Service effective this date carry the all-caps wind-down warning and the new Clause 5A. Clause 5A.2 requires at least 3 months' notice; 19 June to 30 September is 3 months and 11 days, so the notice period was honoured to the letter | Terms of Service effective 19 June 2025 |
| **17 February 2020** | CGT contract deployed on Ethereum mainnet | Contract creation tx `0x0b73a1a3...` |
| **8 August 2018** | CACHE PRIVATE LIMITED incorporated in Singapore, UEN 201827110K | ACRA register |

### What actually happened to the gold

**Established with certainty:**

1. **Two addresses were paid, and only two.** Scanning every PAXG `Transfer` event emitted from the CACHE owner address `0xb779efee...` across blocks 23,350,000 to 23,950,000 (covering September 2025 through January 2026) returns **six log entries, of which four are zero-value Paxos fee-address entries. The entire compulsory redemption consisted of two real payments: 60.180957 PAXG on 1 October 2025 and 15.785912 PAXG on 17 November 2025.** Total distributed: **75.9669 PAXG = 2,362.8 grams of gold.**

2. **Total supply never moved.** CGT `totalSupply()` at block 23,479,000 (immediately before the 30 September 2025 snapshot) was **100,771.01**. At the current block it is **100,771.01**. Identical. **The tokens were never burned.** CACHE did not retire the supply it had de-backed; it simply stopped recognising it and left it circulating.

3. **The arithmetic of the gap.** Roughly **2,362.8 grams** were settled in PAXG against a token supply of **100,771 grams**. That is **2.3% of the outstanding supply**. The remaining **~98,408 grams (98.4 kg, roughly $12.0M at 2025 gold prices) went to holders who received nothing.**

**Where the unsettled gold went: cannot be established from public sources, and I am stating that rather than inferring it.** Specifically, I checked and did not find:

- Any statement by CACHE, on the surviving notice page or in the Terms, of what was done with the physical bars that backed the un-redeemed ~98 kg. The notice says only that tokens "ceased to be backed by gold." **It never says what happened to the gold.**
- Any bar list, final reserve statement, or closing GramChain snapshot. The explorer is 404.
- Any liquidator's or trustee's report, because there is no liquidation and there was never a trustee.
- Any independent attestation of the reserve at any point, including at wind-down.
- Any MAS or MinLaw filing, notice or supervisory statement about the disposition of the assets.

**The three possibilities are all consistent with the public record, and nothing distinguishes them.** The bars may have been sold to fund the ~2,362 g of PAXG purchased for the airdrop, with the remainder retained by CACHE; the bars may have been sold and the proceeds retained; or a large fraction of the supply may have already been redeemed by holders before the deadline with the tokens left in circulation unburned. **The last of these is quite plausible and would be the benign reading**, but I cannot confirm it, because CACHE never burned redeemed tokens and never published a final reconciliation. **That is precisely the problem: the issuer's own choice not to burn and not to publish makes it impossible for anyone outside to tell whether holders were made whole or not.** A protocol that published bar serial numbers for five years has left no way to answer the only question that ultimately mattered.

### The orphaned tokens

**Yes, tokens remain outstanding today with no redemption path. 100,771.01 CGT across 136 addresses.** Every one of those holders has a claim on nothing, and Clause 5A.7 has already extinguished their right to complain:

> "5A.7 By continuing to hold CGT tokens, Token Holders (including Tokens Holders who are not eligible to be airdropped PAXG tokens...) expressly agree to this compulsory redemption mechanism as set out in this clause 5A and **waive any right to further redemption, refund, or legal claim against CACHE** following the Compulsory Redemption Date. For the avoidance of doubt, **this waiver shall apply to all Token Holders, including those who do not have a CACHE Marketplace Account.**"

The waiver was drafted to bind precisely the people the issuer knew it could not reach.

**The single largest casualty is visible on-chain and worth naming.** Address `0xd4033ea2ec53a26d6295f6f375d5c6afbe788660` holds **96,771.41 CGT: 96.03% of the entire remaining supply, ~96.8 kg of gold, roughly $11.8M at 2025 prices.** Its history is that of a patient accumulator: 29 separate purchases from a single counterparty between 2022 and **15 January 2025**, then nothing. It received **no PAXG**. It holds zero ETH, so it cannot even pay gas to move the worthless tokens. It has been silent since January 2025, which is **five months before the wind-down notice was published in June 2025.**

**This is the whole lesson in one address.** A holder who did exactly what a gold savings product tells you to do, buy steadily and hold, stopped checking in eight months before the notice, and lost the entire position. Clause 5A.2's notice mechanism, publication on the website, in the marketplace, by email to Verified Users, on Etherscan and on social media, was contractually impeccable and operationally useless against a bearer holder who was not watching. **Notice published is not notice received.**

I cannot establish whether that address belongs to a person who lost $11.8M, an exchange or custodian omnibus wallet, or an entity that had already redeemed the underlying gold off-chain and abandoned the tokens. The distinction is enormous and **is not determinable from public sources**, again because CACHE did not burn redeemed tokens.

### Did holders get notice? Yes, and it was better than any other failure in our set

To be fair to CACHE, and the fairness is the point:

- **Clause 5A.2 required at least three months' notice** through five channels, including explicitly "public blockchain channels, including but not limited to the CGT token page on Etherscan," specifically to reach non-account holders.
- **The notice period was honoured.** 19 June 2025 to 30 September 2025 is over three months.
- **A redemption window was kept open** to 26 September 2025 for physical gold or fiat.
- **A default settlement was provided**, the PAXG airdrop, so a passive holder was not simply expropriated but converted into the most liquid equivalent gold token available, at a clean weight-based ratio with no discretionary price applied ("No fiat or market price valuation will apply").
- **A post-hoc remedy window** ran to 31 October 2025.

**This is a genuinely well-designed wind-down, and it still left 96% of the supply stranded.** That is the finding. The failure was not in the drafting. It was in the architecture: **an anonymous bearer token cannot be reliably contacted, and a contract cannot fix that by declaring publication to be sufficient notice.**

---

## 12. Relevance to Aurumix

CACHE is the most valuable failure in the set for Aurumix, because it is the only one that tried to do this properly. Its lessons are about execution, not intent.

### 12.1 The wind-down question (Question 9): the answer is now much sharper than "publish a plan"

Our brief says "No failed gold token published a wind-down plan. Aurumix committing to one ex ante is cheap differentiation." **That is factually wrong, and the correction improves the recommendation.** CACHE did publish one, in advance, in its Terms, with a defined notice period, a defined redemption window and a defined default settlement. It executed it as written. **And 96% of the supply was still stranded.**

So the differentiator for Aurumix is not "publish a wind-down plan." Everyone can copy a clause. The differentiator is **publishing a wind-down plan that is architecturally capable of working**, which requires four things CACHE lacked:

1. **A trustee or equivalent independent fiduciary holding the gold**, so that the issuer's decision to stop operating does not extinguish the holder's claim. CACHE had none, and Clause 1.2.3 reduced "beneficial ownership" to "economic value" the moment it was tested.
2. **A holder registry, so notice can be delivered rather than published.** See 12.2.
3. **A commitment to burn tokens on redemption**, so that outstanding supply is a truthful measure of outstanding claims. CACHE's failure to burn is why nobody, including me, can now tell whether its holders were made whole.
4. **A final published reconciliation**: bars in, tokens out, gold disposed, at wind-down. CACHE deleted its bar list instead.

Aurumix should commit to all four, and should say plainly that it is doing so *because* the best-documented wind-down in the sector still failed without them.

### 12.2 The permissioned-token question (Question 3): CACHE is the strongest evidence yet for ERC-3643

The brief already leans to a permissioned base because ICS standing, dividend entitlement, credit eligibility and buyback rights all break on an anonymous DEX transfer. **CACHE supplies a much blunter argument: an anonymous bearer token cannot be wound down.**

CACHE knew its holders at mint (full KYC, source of funds, beneficial ownership) and then deliberately issued them a bearer instrument that severed that knowledge. When it needed to reach those people, it could not. It drafted around the gap (Clause 5A.2's publication-is-notice provision, Clause 5A.7's waiver binding non-account holders) rather than closing it, and the drafting did not save the holders.

**With a permissioned register, Aurumix's wind-down is a mailing list and a pro-rata distribution to known wallets. With a bearer token, it is a website notice and a 96% orphan rate.** This is the cost side of the ERC-20 choice, and it should go into the Question 3 write-up as the decisive argument. It also directly supports Aurumix's existing decision on **no physical redemption with cash-only buyback**: a cash buyback to a KYC'd holder of record is a wind-down mechanism that actually reaches people.

### 12.3 The custody fee question (Question 1): a working answer, from a protocol that got it wrong

Wave 1 settled that zero ongoing custody fee is the norm. **CACHE is the counter-example that charged, and it is instructive precisely because its fee still failed.**

The lesson is not "do not charge." It is **"do not build a fee whose collection depends on activity when your product is designed to be held."** CACHE's 0.25% p.a. storage fee was only collected on a transaction. A five-year buy-and-hold customer, the ideal customer for a gold savings plan, paid nothing while costing the issuer vault fees every day. The 0.50% inactivity fee was an admission of the flaw and could itself only be realised on a transaction.

**For Aurumix, whose entire model is monthly contributions from long-horizon savers, this is a direct hit.** Three implications:

- **The recurring SIP is a revenue asset, not just a distribution mechanism.** A monthly contribution is a recurring, predictable touchpoint at which a cash fee can be assessed. CACHE had no such touchpoint. Aurumix does, and should design the custody fee to be collected at contribution time.
- **Charge in cash, as the brief leans.** CACHE deducted fees in grams, which for a 1-token-1-gram product breaks the peg exactly as the Paxos mint-to-self clause does. Aurumix's peg (grams ÷ tokens) tolerates in-kind better, but the cash route avoids the argument entirely and is collectable at the SIP moment.
- **Model the AUM floor.** CACHE ran four vault relationships across five cities on ~$12M of AUM and could not survive. Aurumix should compute the AUM at which its own custody, compliance and agent-commission costs are covered, and treat that as a go/no-go threshold rather than a milestone. **The failure mode for a gold token is not a hack, it is being too small to pay for the vault.** That is now two of two failures in our set (PMGT and CACHE) that died of it.

### 12.4 Proof of reserve (Question 7): serial numbers are a liveness feature, not a solvency guarantee

CACHE had **the best bar-level transparency in the entire set**: per-bar photos, weight, purity, brand, serial number, vault location, updated by the handlers. It had **no independent reserve attestation, ever.** And **all of it went offline** the moment the issuer stopped paying for hosting.

Three rules for Aurumix's PoR design follow directly:

- **A bar list is not an attestation.** CACHE's bar data came from the commercial chain that had an interest in it being right. Aurumix needs a named firm, a stated scope, a stated date, and a recurring schedule. Publish the attestation alongside the bar list and never let marketing blur them.
- **Transparency hosted by the issuer dies with the issuer.** CACHE's Terms still cite `/whitepaper` and `/storage-fee-methodology`, both 404, in the contract governing tokens people still hold. Aurumix should place its bar list and attestations somewhere that survives it: a trustee, an auditor's own site, IPFS with content hashes committed on-chain, or all three.
- **Burn on redemption, always.** CACHE's decision to leave 100,771 de-backed tokens circulating is the single reason the fate of its gold is now unknowable. Supply must equal claims, or the transparency is decorative.

### 12.5 Regulatory route (Question 4): an AML registration is not a licence, and nobody supervised the exit

CACHE's PSPM registration is real and verified, but it is an **anti-money-laundering dealer registration**, not a financial services licence. It carried no client-asset segregation, no capital requirement, no conduct regime, and it gave no regulator any locus to ask where the gold went. Clause 7.1(b)'s claim that the registration meant CACHE was "qualified to... issue precious metals or precious metals backed tokens like CGT" is issuer characterisation, not a regulatory permission.

This is the same shape as the Comtech finding (DAFZA precious-metals licence that does not permit public token issuance) and reinforces the wave-1 correction that there is no cheap licensing route that actually covers token issuance. **The relevant point for Aurumix's VARA cost-benefit is that the expensive licence buys something specific: a supervisor with standing over the assets at the moment of failure.** CACHE had none, which is why its wind-down was answerable to nobody and why the ~98 kg is untraceable. That is worth pricing into the AED 100k application and 200k/yr supervision, and it is worth saying to the client in exactly those terms.

### 12.6 What CACHE does not speak to

Nothing on yield or dividend funding (Question 2): CACHE paid no yield and Clause 1.2.3 expressly denied any dividend or revenue share, so it offers no read on the ICS Dividend problem. Nothing on the instrument split (Kinesis KVT pattern): CACHE had a single token and no separate security. Nothing on ADGM or the Streamex gold-leasing lead. The premium thesis (Question 6) is settled and CACHE adds only a confirming illiquid data point. No savings-plan or agent-network precedent (Question 8), consistent with the rest of the set.

---

## 13. Open items for verification

- [ ] **Obtain a paid ACRA business profile for UEN 201827110K** to confirm current status, the four named officers, shareholders, the date of the last annual return, and whether any strike-off application or liquidator appointment has been filed since September 2025. Free mirrors show "Live Company" but do not show filing history.
- [ ] **Establish the fate of the ~98,408 grams of unsettled gold.** Ask CACHE directly at support@cache.gold whether the bars were sold, retained or delivered, and whether a final reconciliation exists. Record the non-response if there is one: that is itself citable.
- [ ] **Determine how much CGT was redeemed for physical gold or fiat before 26 September 2025.** This is the single fact that separates the benign reading (holders exited, tokens left unburned) from the alarming one (holders were stranded). CACHE never published it and never burned tokens, so it may only be obtainable from the issuer.
- [ ] **Identify address `0xd4033ea2ec53a26d6295f6f375d5c6afbe788660`** (96.03% of remaining supply, ~96.8 kg). Determine whether it is an exchange/custodian omnibus wallet or an individual, and whether it received any off-chain settlement. Its counterparty `0xc8bf2dbd...` supplied all 29 of its purchases and may be identifiable.
- [ ] **Retrieve an archived CACHE Explorer bar list** from the Wayback Machine (snapshots confirmed to exist, e.g. `web.archive.org/web/20250116193557/https://cache.gold/cache-supply`) and capture the final published serial numbers and vault allocations before they age out. **Do this soon.** Note: web.archive.org was not directly fetchable from this environment; retrieve manually or via a different tool.
- [ ] **Confirm the current status of PSPM registration PS20190001508** with the Registrar of Regulated Dealers, including whether it has been renewed since the company ceased token operations, and whether MinLaw was notified of the wind-down.
- [ ] **Confirm per-custodian vault cities** for Brink's, Loomis, Dillon Gage IDS and The Safe House, and whether any of them holds or held gold attributable to CGT after 30 September 2025. The Safe House and Silver Bullion Pte Ltd (Gregor Gregersen) are the most promising line of enquiry given the reported directorship.
- [ ] **Verify the reported officers** (Gregor Gregersen as Director/CEO, Nizam Ismail as Director) against the ACRA profile. Currently Confidence: Low, from a single company directory.
- [ ] **Establish the relationship between Cache Private Limited and Little Bit Pte Ltd** (owner of the GramChain IP per Clause 9.5.2), including common ownership, and whether Little Bit continues to hold CGT bar records that could resolve the gold question.
- [ ] **Confirm whether the ~$17M Q3 2021 raise (Dillon Gage, Palisades Goldcorp) actually occurred.** Currently sourced only to an ICO aggregator. If real, it sharpens the commercial-failure narrative considerably: $17M raised against ~$12M of AUM at closure.
- [ ] **Check for any Singapore court filing** involving Cache Private Limited (winding-up petitions, creditor claims, holder litigation) since September 2025.
