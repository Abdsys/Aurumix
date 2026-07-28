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

