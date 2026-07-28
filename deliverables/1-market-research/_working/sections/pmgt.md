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
