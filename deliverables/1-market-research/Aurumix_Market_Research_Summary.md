# Tokenized Gold: Market Research Summary

## 1. Market Landscape

### 1.1 What tokenized gold is, and how big it actually is

The category is nineteen products deep and eight years old, and it is far smaller than it looks. Two protocols hold roughly 86% of sector assets: Tether Gold at about $2.465bn and Pax Gold at about $1.79bn. Third place is Kinesis at about $310M, and below that the drop is severe. Of the sixteen live protocols in this research, nine hold under $10M each and four hold under $3M, several of them after five or more years of trading. This is not a crowded market Aurumix has to fight its way into. It is two large incumbents, a long tail that never found buyers, and a great deal of unoccupied ground between them.

### 1.2 What the category has built, and what it has not

Seven years of effort went almost entirely into custody and settlement, and the engineering is serious: allocated storage with named refiners, bar-level serial lookup, independent reserve attestation, on-chain redemption. Tether Gold carries an ISAE 3000 (Revised) reasonable assurance opinion from BDO Italia. Pax Gold operates under a national trust bank charter. WisdomTree structured its token as an electronic document of title under New York commercial law. What nobody built is demand. No protocol in this research operates a savings plan, a recurring purchase mechanism, or a retail referral programme, not one of nineteen. Products are sold through exchange listings and institutional desks, on the assumption that a well-built gold token attracts buyers on its merits. Perth Mint Gold Token had a sovereign guarantee, state-owned vaults, a genuine bare trust and a live proof-of-reserve feed, and it reached about US$2.5M in four years before being shut down. Its post-mortem points at distribution, not at product quality.

### 1.3 The regulatory map for a UAE issuer

Five regulators matter to a gold-backed token issued from Dubai, and the classification decision determines which of them the product answers to. VARA (Dubai) regulates Asset-Referenced Virtual Assets, the category a fully-reserved gold token falls into, with issuance under the Virtual Asset Issuance Rulebook effective 19 June 2025: minimum paid-up capital is the higher of AED 1.5M or 2% of reserve-asset value, application fees run to AED 100,000 with AED 200,000 annually in supervision, the timeline is six to nine months or longer, and every individual token requires standalone approval. CMA, the former SCA, restructured effective around 1 January 2026 under Federal Decree-Laws No. 32 and 33 of 2025, is the federal securities regulator and now covers virtual assets explicitly. ADGM / FSRA in Abu Dhabi operates under English common law with a digital securities regime running since 2018. DIFC / DFSA runs a tokenisation sandbox under an Innovation Testing Licence. CBUAE covers fiat-referenced payment tokens, which does not capture a gold-pegged token. The line that matters runs straight through the Aurumix product. A token that is only a redeemable claim on fully-reserved gold is a clean ARVA under VARA, and retail distribution is workable. Add a profit share, a dividend, or a managed-portfolio characteristic and the token risks re-characterisation as a security or a collective investment product, which engages the CMA regime as well: heavier capital, licensed venues only, and possibly a restriction to qualified investors. That fights the mass-retail model directly. VARA offers four routes, and two are cheaper than a standalone licence: a Sponsored Regime operating under an existing licensee, and a Partnership Model that outsources issuance to a Category 1 holder. Both are worth pricing before assuming a full licence is the only door.

### 1.4 The demand picture

Indian households hold roughly 34,600 tonnes of gold, worth about $3.8T on Morgan Stanley's October 2024 estimate. Digital gold bought through UPI grew about 377% in sixteen months, from roughly 20.9M transactions and ₹550cr in April 2024 to roughly 99.8M transactions and ₹1,184cr in August 2025, with UPI accounting for 85% to 90% of digital gold purchases. January 2026 ran at about ₹3,926cr, roughly five times January 2025. Jar, a round-ups savings app, reports more than 20M users saving an average of 22 times a month. The warning sits in the same data. Indian mutual fund SIP inflows reached about ₹2 trillion in FY24, up 28% year on year, but the SIP stoppage ratio spiked above 120% in 2025: more SIPs were being cancelled than started. Recurring savings commitments are powerful and fragile at the same time, and SIP persistence is the whole Aurumix engine, so growth targets should be stress-tested against realistic lapse rates rather than assumed. Behaviour among non-resident Indians, which the client has identified as a major target segment, is a genuine data gap and is not covered by the available research.

### 1.5 Where Aurumix sits

Aurumix bundles four things: SIP accumulation, borrowing against the gold, a yield or dividend, and inheritance. No product found in this research, in India or globally, bundles all four. Indian digital gold platforms do accumulation and physical delivery but offer no credit, no yield and no inheritance. Tokenized gold protocols offer custody and sometimes yield or credit, but none offers recurring savings or inheritance. That is genuine differentiation, and it cuts both ways: no direct competitor, but also no proven template and no precedent box for a regulator to file the product in. Novelty amplifies classification risk rather than reducing it. The practical response is to borrow validated components rather than invent each one: trustee-held allocated custody from the Indian platforms, account-level reward mechanics from Kinesis, Swiss-style legal co-ownership from DGLD, and a partner network structured on function rather than recruitment from Aurus.

---

## 2. Nine Findings That Shape the Design

### 2.1 The premium thesis does not survive contact with the market

The current Aurumix model assumes a 3% to 8% exchange premium will sustain spot demand and pull in SIP contributions. Nine protocols say it cannot.

| Protocol | Assets | Liquidity signal | Price against spot |
|---|---|---|---|
| Tether Gold (XAUT) | ~$2.465bn | ~$130M/day, ~5.3% turnover | At gold |
| Pax Gold (PAXG) | ~$1.79bn | ~$105.6M/day, ~5.9% turnover | At par |
| Matrixdock (XAUm) | ~$52.7M | Continuous two-way primary window | Capped by a 0.76% spread |
| VNX (VNXAU) | ~$5.7M | ~$36k/day | ~0.7% over |
| Comtech (CGO) | ~$5.04M | ~$213/day genuine DEX liquidity | Parity, 0.42% spread |
| Aurus (tGOLD) | ~$5.6M | ~$211/day after seven years | Capped at NAV + 0.5% |
| Midas (XGZ) | ~$5.06M | 264 holders | 1.4% discount |
| ORO (GOLD) | ~$2.45M | 33% liquidity to assets | Slight discount |
| Pleasing Gold (PGOLD) | ~$79–90M | Under $20/day | No functioning market |

The mechanism is a pincer. Where a market is liquid, arbitrage closes any premium. Where it is illiquid, there is no market to express one. The two protocols trading away from spot trade at a discount, and Midas XGZ shows why: a permissioned primary market with a 1 kg redemption floor against an average holding of 148 grams means arbitrage cannot close a discount either. Model the premium at zero. If a closed Aurumix redemption does produce a price above net asset value, that is a product of blocking arbitrage rather than of demand, and it is not a revenue line to plan around.

### 2.2 Nobody charges holders a custody fee, and the reasons why are structural

Zero ongoing custody fee is the category norm. PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, WTGOLD, DGLD and PGOLD all charge holders nothing. The funding underneath splits three ways, and none of the three is available to Aurumix. Velocity taxes: Kinesis charges 0.45% on transfers, Aurus 0.5% to mint and 1.5% to burn, Comtech roughly 1% in commission plus a spread, all funding storage out of churn. A monthly savings product is the lowest-velocity product imaginable, so the model inverts, because Aurumix users hold rather than trade. Parent cross-subsidy: XAUT is funded from Tether's stablecoin reserve income, XAUm from Matrixport, WTGOLD from a $150bn listed asset manager, PAXG from Paxos's stablecoin business. Aurumix has no parent. Deferral, which is the honest one: Comtech charges nothing for 24 months and then reserves the right to introduce "a nominal fee", and Matrixdock reserves the right to start charging on 30 days' notice. Both concede that transaction-margin funding fails for buy-and-hold, which is exactly the Aurumix case. Two mechanisms remain available, and both are peg-neutral for a grams-divided-by-tokens design. Dilution: Paxos reserves the right to take storage fees "by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens pro rata", and has never used it, because a one-token-to-one-ounce peg breaks on minting. The Aurumix peg is grams divided by tokens, so minting to treasury lowers the price per token and leaves the identity intact. It collects nothing in cash from a $20 saver, it reaches holders who never log in, and there is now an OCC-supervised precedent for the drafting. Token-burn demurrage: Digix burned tokens rather than grams, so the gold-per-token ratio never moved, which is also peg-neutral. Three separate objections survive it. A non-standard ERC-20 broke integrations so badly that Digix built its own wrapper to undo its own fee, auditors found a critical bug and a timing exploit in the fee logic, and a balance that visibly decrements every day is very hard to defend in a retail savings product sold to customers whose reference point is an insurance premium.

### 2.3 The dividend is a three-way choice, not a design problem

Every well-regulated, well-documented protocol in the set pays zero yield, deliberately: PAXG, XAUT, XAUm, VNXAU, WTGOLD, DGLD, Midas XGZ and Comtech. WisdomTree owns a registered transfer agent, a broker-dealer and a fund adviser, holds allocated gold, and pays nothing. Midas XGZ sits inside a 115-year-old exchange group with better bullion-leasing access than Aurumix will ever have, and leaves the gold idle. Every protocol that advertises a yield fails the arithmetic.

| Protocol | Advertised | What the numbers show | Gap |
|---|---|---|---|
| Kinesis | 2.05% | $26,326 paid in June 2026 on $310M of assets, about 0.10% annualised | ~20x |
| Pleasing Gold | 5% on ~$79–90M, about $4M a year | Funded from redemption fees on rare redemptions plus a market trading under $20 a day | Unfundable |
| MG999 / Theo | 2.3% net | Borrows gold at 2.5% gross, pays a 1.00% management fee before platform, trustee, admin and audit costs | Arithmetically impossible |
| ORO | 3–4% APY | Real external leasing, but no legal documentation of how holder claims rank | Real source, no protection |

Tenbin tGLD supplies the identity that explains all of it. Tenbin pays a genuine 4% to 6% gold-denominated yield funded by futures basis plus stablecoin rates, and it can do that precisely because its collateral is USDC and futures margin rather than bullion. Vaulted gold yields nothing and costs money to store. Any yield on a bullion-backed token must therefore come from encumbering the metal, from the operating business, or from nowhere.

### 2.4 Gold-leasing yield is documentable. Holder protection is not.

Streamex filed its executed gold-leasing agreement with the SEC: 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1. It carries a 3% net-after-origination-fees floor, absolute discretion to reject any lease, and two layers of insurance including a Lloyd's DIC/DIL policy covering lessee fraud and mysterious disappearance at 110% of value. That is a real, public, copyable yield-generation template. What it does not do is protect a token holder. There is no security interest, no title-retention clause, no risk-of-loss allocation, no subordination and no waterfall. The insurance loss payee is Monetary Metals "wherever possible", which is a best-efforts phrase rather than a covenant. Streamex's own 10-K concedes that holders "may face delays, partial recovery, or total loss" and that other lessors in the commingled pool "may receive more favorable terms or priority in enforcement scenarios". Liability is capped at the lesser of six months' fees or $500,000. The risk is realised, not theoretical. On 26 January 2026 the AgaBullion lessee defaulted, Turkish authorities seized the leased gold, and the remedy was Istanbul counsel plus an insurance claim. "Title remains with the lessor" means "we will litigate abroad." Two things follow. The yield-generation template exists and can be taken to counsel as a worked example. And no protocol in this research names token holders as an insurance loss payee or publishes a default waterfall, so being first to do so is cheap, unoccupied differentiation. Note the audience gap: Streamex sells this risk to accredited investors at a $200,000 minimum, and Aurumix would be selling the same risk to a $20-a-month saver.

### 2.5 Protocols die of revenue starvation, not of regulators or hacks

All three failures in this research share one cause, and it is not the one most people expect. PMGT charged nothing: no mint fee, no custody fee, no redemption fee. It reached about US$2.5M in four years with a sovereign guarantee, state-owned vaults, a real bare trust and a live proof-of-reserve feed, and nobody inside the Perth Mint had a commercial reason to fight for it. Digix zeroed its own 0.60% annual demurrage in 2019 to match PAXG's fee-free launch, which left the gold business with no revenue line while it lived on its ICO treasury. When holders voted that treasury away on 20 January 2020, over 95% approval on 52 votes, roughly 386,428 ETH or $64M, the runway ended. No regulator acted, and the licence was voluntarily withdrawn. Cache Gold did charge a storage fee, but Clause 6.2.1 only collected it when a transaction was initiated, so buy-and-hold savers paid nothing while consuming vault cost every day. It died charging a fee it had architected itself out of collecting. Not one died of enforcement, a hack, or a reserve shortfall. The implication cuts against instinct. Custody quality does not create demand and it does not create survival. A revenue line is a survival feature, and a fee that only bites on transactions is no revenue line at all in a savings product. That is a direct warning about any Aurumix fee schedule that depends on user activity, and it is the argument for the SIP-inflow skim and for the dilution mechanism, both of which collect from a dormant holder.

### 2.6 A wind-down plan is necessary and nowhere near sufficient

Cache Gold published a real wind-down plan at Clause 5A: three months' notice across five channels including Etherscan, a manual redemption window to 26 September 2025, a default settlement in PAXG at a clean weight ratio, and a remedy window to 31 October 2025. The issuer followed it. Only 2.3% of the gold was settled. Two payments totalling 2,362.8 g against 100,771 g outstanding, leaving roughly 98,408 g, about $12.0M, whose fate cannot be established from public sources. 100,771 CGT remain outstanding across 136 addresses and were never burned, so total supply today is byte-identical to before the wind-down. One address holds 96.03% of it, received no settlement, holds no ETH to even move the tokens, and went silent five months before the notice was published. Clause 5A.7 pre-emptively waives their claims. There was never a trustee. Publishing a wind-down plan is therefore too weak a standard. The plan has to be architecturally capable of executing, which requires four things Cache Gold lacked: a trustee holding title, a holder registry so that notice is delivered rather than merely published, burn-on-redemption so supply always equals claims, and a final published reconciliation. An anonymous bearer token cannot be wound down. That is the strongest available argument for a permissioned token base at Aurumix, and it is stronger than arguing about which rights survive a transfer. The counter-example proves it: DGLD's holders own the gold outright at law under Swiss co-ownership and possession, with the terms expressly disclaiming any debt or equity claim, which is exactly why six years of near-total dormancy harmed nobody and a restart was possible in November 2025.

### 2.7 Most of the category operates outside the regulatory perimeter

Of nineteen protocols, the ones holding a licence that actually covers the token they issue are PAXG (OCC national trust bank), XAUT (CNAD El Salvador, EME-0004), WTGOLD (NYDFS limited purpose trust) and MG999 (MAS capital markets services licence, held by the platform and the fund manager). That is four. Everything else runs one of three patterns, and Aurumix should expect all three to be used against it in diligence. The software company: the operating entity is registered for "development of software and applications" rather than financial services or precious metals, which is true of ORO, Aurus, both Midas GoldZip entities and Libeara's holding company, with the regulated acts of owning metal, custody, KYC, retail sale and redemption pushed onto partners or performed unlicensed. The adjacent licence, described as the real one: Comtech's DAFZA bullion trade licence and Midas's Singapore MinLaw dealer registration are AML or trade registrations, and both are presented as authorisation to issue tokens to the public, while Comtech's licences additionally display as expired. The halo: Kinesis describes a conditional CIMA approval as regulatory status while a CIMA register search returns no entity of that name, and Libeara's Standard Chartered connection is venture equity two removes away, with Standard Chartered appearing nowhere in the MG999 stack as issuer, manager, custodian, auditor, administrator or guarantor. There is no cheap compliant door. Everyone who appears to have found a shortcut is either unlicensed, licensed for something else, or subsidised by a parent that already holds a banking or trust charter. One inversion is worth carrying, because it reverses a natural assumption: the licence buys the opacity, it does not remove it. MG999 holds a genuine MAS licence and publishes less legally operative detail than much smaller unlicensed issuers, because selling only to accredited investors removes the prospectus obligation. That route is closed to Aurumix anyway at $20 a month.

### 2.8 "Audited" almost never means the gold was checked

This is the most reliable single tell in the sector. The published audit is a smart-contract audit, while the reserve attestation is absent, stale, or self-signed. They are different work, done by different firms, and only one of them checks that the gold exists.

| Protocol | What "audited" means there |
|---|---|
| Pleasing Gold | Beosin, staking contract only. No reserve attestation at all |
| Aurus | NonceBlox smart-contract audit. Proof of reserve announced but not live. Self-reported 73,398.5 g does not obviously reconcile to 43,322 tokens |
| ORO | Cantina and Adevar Labs, smart contracts. Reserve verification frequency stated three inconsistent ways, no document published |
| Comtech | Self-signed letters on company letterhead, last one 21 March 2025, showing reserves down 23%. No bar list, no smart-contract audit |
| WisdomTree | No bar list, no proof-of-reserve feed, no reserve attestation and no smart-contract audit |
| AZG | No contract audit, source not verified on-chain, no attestation |

The strongest in the set is XAUT's ISAE 3000 (Revised) reasonable assurance opinion from BDO Italia, and even there the custodian is unnamed and no bar list exists. DGLD, PAXG and VNXAU are the only protocols with credible independent reserve examination. VNX carries a sting worth reading twice: its auditor states that the basis of a holder's property right is VNX's own internal holder register, and then expressly refuses to opine on it. The token is not the title. The register is. Any Aurumix architecture needs to be clear about which artefact carries legal ownership, and to have that artefact examined by someone.

### 2.9 Distribution is the universal gap, and it is Aurumix's actual moat

No protocol in this research has a savings plan, a recurring purchase mechanism, or a retail referral programme. Not one of nineteen. The category has spent seven years perfecting custody and ignoring demand. The single partial exception is instructive. Aurus runs a partner network paid from a fee pool that splits 50% to ecosystem token holders, 25% to vault partners and 25% to provider partners. The reseller tier gets 0% of the pool. Resellers earn their own markup, plus preferential bulk redemption and a graduation path to a higher tier. No commission, no override, no residual, and nothing paid for recruitment. It is a merchant-margin supply chain rather than a multi-level marketing scheme. That is a structural answer to the MLM problem rather than a cosmetic one, and it is directly transferable. Recast the three Aurumix agent tiers so each is paid for a function performed, capital committed, custody provided or servicing delivered, rather than for recruitment depth, and use graduation rather than overrides to motivate top agents. Combined with insurance-style trailing commission tied to continued contributions, that gives two independent structural defences. One caveat carries from Aurus: its partner economics live in a whitepaper, the only legal document on its site is a four-page website terms page naming no entity and no governing law, and the split has changed three times under upgradeable contracts. Copy the structure, not the paperwork.

---

## 3. The Field at a Glance

### 3.1 Live protocols by assets under management

| Protocol | Assets | Domicile | Licence covering the token | Custody fee | Yield | Token standard |
|---|---|---|---|---|---|---|
| Tether Gold (XAUT) | ~$2.465bn | El Salvador (from BVI, Jan 2025) | CNAD EME-0004 | 0% | None | ERC-20, TRC-20, LayerZero OFT |
| Pax Gold (PAXG) | ~$1.79bn | United States | OCC national trust bank | 0% | None | ERC-20 (upgradeable proxy) |
| Kinesis (KAU) | ~$310M | Cayman Islands (six entities) | None granted. CIMA conditional only | 0% | 15% of fee pool, ~0.10% realised | Permissioned Stellar fork + ERC-20 wrapper |
| Pleasing Gold (PGOLD) | ~$79–90M | Hong Kong | None identified | 0% | "5%", unfundable | ERC-20 |
| AZ Gold Reserve (AZG) | ~$65M claimed | Nevis, unverifiable | None | 1% (secondary source only) | 15% to miners, not holders | ERC-20 |
| Matrixdock (XAUm) | ~$52.7M | BVI, unverified | None in the issuer's name | 0%, reversible on 30 days | None | ERC-20 + BullionNFT |
| MG999 (Libeara) | ~$12.44M | Singapore | MAS CMS (platform and manager) | 1.00% management | ~2.3% net, arithmetically impossible | Not published |
| Streamex (GLDY) | 3,133 tokens, 98.5% held by parent | Cayman Islands | None. Reg D 506(c) exemption | Not disclosed | 3.50%, paid in GLDY | Not published |
| Digital Gold (DGLD) | ~$8.1M | Switzerland (Geneva) | None. VQF self-regulatory affiliation only | 0% | None | ERC-20 on Ethereum and Base |
| Aurus (tGOLD) | ~$5.6M | United Kingdom | None | 0% | None on tGOLD | ERC-20 |
| VNX Gold (VNXAU) | ~$5.73M disputed | Liechtenstein | TVTG registrations, no Token Issuer licence | 0% | None | ERC-20 with transfer-provider hook |
| Midas GoldZip (XGZ) | ~$5.06M | Singapore | Dealer registration only | Not disclosed | None | ERC-20 + 0.01% transfer fee |
| Comtech Gold (CGO) | ~$5.04M | Dubai (DAFZA) | None. Trade licences only, displayed expired | 0% for 24 months | None on token | ERC-20 |
| ORO (GOLD) | ~$2.45M | Singapore | None anywhere | 0% | 3–4%, undocumented | SPL, freeze authority null |
| WisdomTree (WTGOLD) | ~$2.0–2.5M | United States (New York) | NYDFS limited purpose trust | 0% | None | Document of title, NY UCC Article 7 |
| Tenbin Gold (tGLD) | ~$1.05M | BVI | None | None (no custody) | 4–6%, synthetic | ERC-20 |

### 3.2 How each protocol is actually funded

| Protocol | Charged to holders | Funded by | Sustainable for buy-and-hold? |
|---|---|---|---|
| Tether Gold | 0% ongoing, 0.25% buy and redeem | Parent stablecoin reserve income | Yes, but only because of the parent |
| Pax Gold | 0% ongoing, tiered mint and redeem, $2/mo after 12 months idle | Paxos stablecoin business, plus a reserved dilution right | Yes, with a parent |
| Kinesis | 0% custody, 0.45% transfer | Transaction velocity | No. Yield realised at ~0.10% against 2.05% advertised |
| Comtech | 0% for 24 months | ~1% commission plus ~1.8% spread | Conceded no: reserves the right to start charging |
| Matrixdock | 0%, reversible on 30 days | Matrixport parent, 0.76% two-way spread | Conceded no: reserves the right to start charging |
| Aurus | 0% | 0.5% mint, 1.5% burn | No. $211 a day of volume after seven years |
| MG999 | 1.00% management | Management fee | Fee exceeds the gross lease income it pays out of |
| Digix (failed) | 0.60% demurrage, then zeroed | ICO treasury after the fee was removed | No. It removed its own revenue line |
| Cache Gold (failed) | Storage fee collected only on transactions | Nothing, for savers | No. Savers paid nothing and consumed vault cost daily |
| PMGT (failed) | Zero fees of any kind | Nothing | No. Zero revenue meant no internal advocate |

### 3.3 Reserve verification, separated properly

| Protocol | Reserve attestation | Smart-contract audit | Bar list |
|---|---|---|---|
| Tether Gold | BDO Italia, ISAE 3000 (Revised) reasonable assurance | Yes | No, and the custodian is unnamed |
| Pax Gold | Independent attestation, plus address-to-bar lookup | Yes | Yes |
| DGLD | Credible independent examination | Yes | Yes |
| VNX Gold | Independent, but the auditor refuses to opine on the holder register | Yes | Partial |
| Comtech | Self-signed letters, last dated 21 March 2025 | None found | No |
| Aurus | Announced, not live | NonceBlox | No |
| ORO | None published | Cantina, Adevar Labs | No |
| Pleasing Gold | None | Beosin, staking contract only | No |
| WisdomTree | None | None | No |
| AZG | None | None, source not verified on-chain | No |

### 3.4 Protocols that failed

| Protocol | Ceased | Actual cause | Wind-down plan | What holders received |
|---|---|---|---|---|
| PMGT | 31 October 2023 | Commercial abandonment. Zero fees, zero revenue, zero distribution | One sentence, and it failed: the redemption destination was closing at the same time | Made whole by timing. Non-actors were force-sold at the 1 November 2023 price without consent |
| Digix (DGX/DGD) | March 2023 operations, parent struck off 19 July 2026 | Zeroed its own demurrage to match PAXG, then lost its treasury to a 52-vote poll | None for DGX | DGD holders: 0.193054178 ETH each, permanent permissionless claim, ~12,491 ETH still unclaimed. DGX holders: a dead website |
| Cache Gold (CGT) | Redemption ended 31 October 2025 | Charged a fee it only collected on transactions, so savers paid nothing | Yes, Clause 5A, and it was followed | 2.3% settled. ~98,408 g unaccounted for. 100,771 CGT still outstanding, never burned |

### 3.5 The adjacent field: Indian digital gold and savings platforms

| Platform | Model | Minimum | Credit against gold | Yield beyond gold price | Inheritance | Physical delivery |
|---|---|---|---|---|---|---|
| SafeGold | Digital claims on 24K, independent trustee, not a SEBI security. Powers PhonePe, Google Pay and Paytm | ~₹10 | No, separate NBFC pledge | No. Earns a 2–5% spread | No | Yes, cash, coins or jewellery |
| MMTC-PAMP | LBMA refiner, allocated and insured | ~₹9 via Paytm | No | No | No | Yes, coins and bars |
| Augmont | Digital gold with trustee oversight | ₹1,000/month | No | No | No | Yes, anytime |
| Jar | Round-ups and UPI autopay into 99.9% digital gold | ₹10/day | No | No | No | Yes, sell or convert |
| Gullak | Digital gold plus a "Gold+" leasing product | ₹100/day | No | Leasing yield | No | Yes |

These are not tokenized gold protocols. They are the products the Aurumix target customer actually uses today, and the real competitive reference point for the savings half of the model. Every one of them achieves distribution that no tokenized gold protocol has come close to, and they do it by embedding inside payment apps their customers already open daily. Not one offers credit, dividend or inheritance, which is precisely the ground Aurumix is claiming.

## 4. Live Protocol Profiles

Sixteen protocols are live. Five carry a full profile because each one settles a question this design has to answer: what the largest product in the category charges, what a fully licensed issuer looks like, whether an advertised yield survives its own arithmetic, whether gold-leasing income can be documented, and what a Dubai issuer actually holds. The remaining eleven follow in comparison tables carrying the same nine fields, so any two protocols in this report can still be read line by line. Where a field records that something is not disclosed, that is the finding rather than a gap in the research.

### 4.1 Tether Gold (XAUT)

| Field | Detail |
|---|---|
| Issuer | TG Commodities, S.A. de C.V., El Salvador. Relocated from the British Virgin Islands, January 2025. Owned by Tether Holdings, S.A. de C.V. and Tether Operations, S.A. de C.V. Sole Administrator Giancarlo Devasini. |
| Licence covering the token | CNAD El Salvador stablecoin issuer register EME-0004, dated 19 May 2025, under the Digital Asset Issuance Law. FinCEN Money Services Business registration. No securities or commodities regulator authorises the token. |
| Assets under management | ~US$2.465bn at ~US$4,021.73 per token, July 2026. 612,823 XAU₮ circulating, 707,747 XAU₮ minted. Reserves 707,747.139 fine troy ounces at 31 March 2026. |
| Backing | 1 XAU₮ = 1 fine troy ounce of LBMA London Good Delivery gold on a specified bar, vaulted in Switzerland. Country only; no city or facility named. |
| Custody fee charged to holders | 0%. No recurring storage or management fee, permanently. |
| Yield paid to holders | None. No dividend, interest or staking reward. |
| Redemption | Physical delivery only, to a Swiss address. Minimum ~430 XAU₮ (~US$1.73m). Fee 0.25% plus logistics, insurance and handling. Full KYC. No cash window documented. |
| Token standard | ERC-20 on Ethereum (`0x68749665ff8d2d112fa859aa293f07a622782f38`, six decimals) and TRC-20 on Tron. XAUt0 LayerZero OFT wrapper on TON, Solana, Avalanche, Polygon, Stable, Conflux and BNB Chain. |
| Reserve verification | Quarterly reserves report by BDO Italia S.p.A. under ISAE 3000 (Revised), reasonable assurance. Daily transparency page at gold.tether.to. No bar list. Custodian not named. |

#### What it is

Tether Gold is the largest tokenized gold product in existence, roughly US$2.46bn and about 612,823 troy ounces circulating, near enough 19 tonnes of metal behind the float. Each XAU₮ represents one fine troy ounce on a specific London Good Delivery bar in a Swiss vault. Scale is why it matters here: XAU₮ runs 25 to 30 times the size of PGOLD on a documentation set thinner than protocols a fraction of its size. Two facts shape everything downstream. Holders pay nothing to store their gold, and the customer is institutional, gated by a 50 XAU₮ purchase minimum of roughly US$200,000.

#### Legal structure and regulatory standing

The reserves report states that "the Gold Reserves are owned by the XAU₮ token holders, not by the Company," that holders "have undivided ownership rights to gold on specified gold bars," and that tokens are created only after the Custodian receives the gold. That claims a property interest in identified bars, not a creditor claim. Two caveats bite. BDO Italia opines only that the report is "fairly presented in accordance with the criteria, including Management's Key Accounting Policies, set out therein," an accounting conclusion rather than a legal opinion on title under Salvadoran or Swiss law, and no trust deed, bailment or custody agreement is published. The wording is also internally tense: with 611 bars of 12.5kg behind hundreds of thousands of tokens, holders cannot each own a specified bar. TG Commodities does not disclose which construct governs on insolvency. PSAD-0032 circulates in secondary coverage, but TG Commodities does not appear on the CNAD PSAD list; EME-0004 verifies for issuance. The largest gold token in the world sits inside a Salvadoran stablecoin regime and holds no VARA, DFSA or ADGM licence. No enforcement action specific to XAU₮ was identified.

#### Custody and reserve verification

Every primary document calls the custodian only "the Custodian." Secondary sources speculate Brink's or Loomis; none names it. There is no bar list: no serial numbers, no refiners, no per-bar assay. The attestation still deserves credit. It is a reasonable assurance engagement under ISAE 3000 (Revised), the higher tier, covering physical inventory of fine troy ounces, reconciliation of the ledger against onchain liabilities, and quarterly confirmatory assay of sampled bars by a qualified independent third party. BDO Italia states the limit directly: "The reporting date is limited to a point in time as of 30 June 2025. We did not perform procedures or provide any assurance at any other date or time in this report." No first-party smart-contract audit was located. At 30 June 2025, 246,524.33 XAU₮ had been minted, 186,879.51 sold and 59,644.82 held "available for sale" by Alpha Group Commodities, S.A. de C.V., an affiliate that also left the BVI in January 2025. At 31 March 2026, reserves stood at 707,747.139 ounces against 559,598.64 sold, leaving roughly 21% of minted supply as unsold affiliate stock.

#### Fees, revenue and redemption

Direct purchase costs 0.25% with a 50 XAU₮ minimum, physical redemption 0.25% plus logistics, insurance and handling. Transfers cost network gas; cross-chain XAUt0 costs whatever the bridge and LayerZero charge. Custody is 0.00%, there is no management fee, and no issuer cash window is documented. Two 0.25% touches cannot fund perpetual Swiss vaulting: buy once, hold ten years, consume ten years of storage, insurance and assay. The arithmetic closes outside the fee table. Tether Holdings earns large returns on its USDT reserve book, the group holds a reported 140 to 162 tonnes on its own account, and the issuer sells affiliate inventory at a spread. TG Commodities has never published a statement explaining what funds free storage. Issuance is gold-first and KYC gated, filled from Alpha Group stock where possible. Redemption is where the ownership claim thins: ~430 XAU₮, a Swiss address, full KYC, an unpublished excluded-country list, export left to the holder. Below one bar, selling the token is the only exit.

#### Liquidity and distribution

Market cap ~US$2.465bn, 24h volume ~US$130.4m, about 5.3% daily turnover, with Binance XAUT/USDT at ~US$12.5m, Gate ~US$11.7m, Bybit ~US$9.0m, OKX ~US$6.9m and XT.COM ~US$6.3m. Reported at 54% to 60% of the entire gold-backed token market, it is arbitraged continuously against spot and trades at gold, not above it. Distribution is exchange listings, large-ticket direct issuance and DeFi collateral integrations, with Indonesia targeted via Mobee in July 2025. What it has none of: savings plan, SIP, fractional accumulation, referral scheme, agent network or distributor commissions.

#### Relevance to Aurumix

XAU₮ never meets Aurumix's peg-breakage problem because it never touches the gold to pay for storage. Aurumix has no comparable subsidy, but the point survives: the market leader charges zero, so any Aurumix fee must be justified by the savings wrapper, agent servicing and credit facility, not the vault. The best-capitalised gold token in crypto pays no yield and grew anyway, and its Shariah certification rests on the absence of interest, leverage and speculative derivatives. Tether could afford a yield on 19 tonnes and declines, which reads as unwillingness to make a commodity token resemble an investment contract. The Ledn structure is the better model: credit against holdings, no rehypothecation, EU and Canada excluded. A plain ERC-20 costs XAU₮ nothing because it carries no tier, dividend or buyback right. Aurumix's ICS state breaks on an anonymous transfer, so ERC-3643 means no comparable liquidity and a cash buyback as the only exit, and XAUt0 is the warning: whether a holder on Solana or TON has the same claim on Swiss gold is not disclosed. Decide what a wrapped AURX holder owns first. TG Commodities chose EME-0004 under the LEAD over a major-market licence and reached the GCC through Amanah Advisors certification by Mufti Faraz Adam on 27 July 2026. The limit: XAU₮ is a custody receipt fitting a stablecoin box, while Aurumix's dividend, credit, SIP and agent network fit no box anywhere, and the 90% to 95% LTV facility is what riba and leverage screening will catch. Match quarterly ISAE 3000 (Revised), then beat it by naming a custodian and publishing a bar list. Stress-test revenue with the 3–8% premium at zero. The real risk is agent conduct and KYC at scale, not custody. And nobody here, at US$2.5bn included, has published a wind-down plan.

### 4.2 Pax Gold (PAXG)

| Field | Detail |
|---|---|
| Issuer | Paxos Trust Company, National Association, a US federally chartered uninsured national trust bank, New York. Converted from a NYDFS limited-purpose trust company on 12 December 2025. Charles Cascarilla is CEO. |
| Licence covering the token | OCC national trust bank charter, uninsured, granted 12 December 2025. Terms state Paxos issues PAXG "pursuant to specific approval from the OCC." No public charter number located. No VARA, ADGM, DFSA, MAS or MiCA authorisation identified. |
| Assets under management | ~US$1.79bn at ~US$4,027 per token, 28 July 2026. ~444,808 PAXG circulating, equal to ~444,808 fine troy ounces (~13.8 tonnes). |
| Backing | 1 PAXG = 1 fine troy ounce of a specific, serial-numbered LBMA London Good Delivery bar in LBMA-approved London vaults. Allocated, not unallocated. Paxos may reallocate which bars back which holders. |
| Custody fee charged to holders | 0% at present. "Paxos does not charge gold storage fees to its customers at this time." The terms reserve the right to charge by dilution. |
| Yield paid to holders | None. PAXG pays no yield of any kind. |
| Redemption | Three routes: USD at market via a Paxos account; Unallocated Gold by wire to a bullion account; physical Allocated Gold at 430 PAXG per bar (~US$1.73m) plus a User Guide fee. Destruction fee tiered 1.000% to 0.125%. KYC verification, not a "qualified holder" test. |
| Token standard | ERC-20 on Ethereum (`0x45804880de22913dafe09f4980848ece6ecbaf78`, 18 decimals), proxy pattern, with owner/admin, supply controller, fee controller and asset protection roles including freeze and balance wipe. Solana via Token-2022 from around 25 June 2026; mint address not published by Paxos. |
| Reserve verification | Monthly attestation by KPMG LLP since February 2025, previously WithumSmith+Brown, under AICPA attestation standards, dated time series through June 2026. Per-address bar lookup. No full public bar list. No onchain proof-of-reserve oracle identified. |

#### What it is

PAXG launched in September 2019 and is the second-largest tokenized gold product after Tether Gold. Each token represents one fine troy ounce of a specific, serial-numbered London Good Delivery bar in LBMA-approved London vaults. The product is deliberately narrow: a custody receipt with an onchain wrapper, no savings plan, no yield, no tiering, no credit facility, no referral network. Everything Aurumix layers on a gold core, Paxos has consciously omitted, and it reached ~US$1.79bn doing only that. Minimum purchase is 0.03 PAXG, roughly US$120, driven by a 0.02 PAXG internal conversion cost, though the holding minimum is effectively zero at 18 decimals.

#### Legal structure and regulatory standing

The terms state that "your PAXG tokens are akin to a warehouse receipt representing your beneficial ownership of a pro rata portion of Allocated Gold." That is beneficial ownership, not legal title, and Paxos reserves the right to reallocate bars "for operational efficiency," so the serial number a holder looks up is real but not permanently theirs. Allocated Gold is defined as "a specific gold bar held in an LBMA-approved security carrier vault, identifiable by a unique serial number, weighting and purity percentage," against Unallocated Gold as "a liability of such institution whereby the holder of unallocated gold owns a claim to an equivalent balance of gold." PAXG is backed by the former, a distinction most competitors blur. Bankruptcy remoteness is documented asymmetrically. The Paxos blog asserts customer funds sit in "segregated, bankruptcy remote accounts" and that "your gold bars will always be yours, even in the unlikely case something happens to Paxos," while the terms carry no Paxos-insolvency clause, only a Clearing Bank disclaimer. The charter does that work instead. Paxos filed on 11 August 2025 to convert, and on 12 December 2025 the OCC conditionally approved five national trust charters: Paxos, Ripple National Trust Bank, First National Digital Currency Bank, BitGo Bank & Trust, N.A. and Fidelity Digital Assets, N.A.

#### Custody and reserve verification

Paxos Trust Company, N.A. is the legal custodian and Brink's operates the vaults, named on the Paxos blog: "we store gold reserves with Brink's bullion vaults in London." The product page says only "LBMA vaults in London," so the operator name sits on a blog post rather than in the terms. Paxos is one of the few issuers that keeps attestation and contract audit separate in its own copy. Attestation is monthly, by KPMG LLP since February 2025 and WithumSmith+Brown before, under AICPA attestation standards, as a dated time series through June 2026. The Ethereum contract was audited before launch and Zellic audited the Solana deployment, though no PAXG-specific audit PDF was located on paxos.com. One secondary source claims an annual physical bar audit by Bureau Veritas, which does not confirm against either firm's primary sources. The gap: a per-address lookup is not a bar list. A holder verifies their own slice and cannot sum the pool, so total-supply verification rests on KPMG's monthly snapshot.

#### Fees, revenue and redemption

Creation is tiered: 0.02 PAXG flat for 0.03 to 2 PAXG, then 1.000% (2 to 25), 0.750% (25 to 50), 0.500% (50 to 75), 0.250% (75 to 200), 0.150% (200 to 800), 0.125% above 800, waived under a promotion whose end date renders as "09/31/26," a date that does not exist. Destruction uses the same schedule, unwaived. Storage is US$0.00, the contract transfer fee (historically 0.02%) is understood to be zero, banking fees pass at cost, and US$2.00 per month applies after 12 months without issuance or redemption. Physical delivery is priced only in the User Guide, with US$20 domestic and US$30 international cited by secondary sources, unconfirmed. Revenue is transactional plus stablecoin cross-subsidy. The fallback matters most: "Paxos may charge storage fees to all token holders by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens. The storage fee will be in line with industry practice, and such storage fee will be passed on to all PAXG token holders on a pro rata basis." Minting against an unchanged pool leaves each PAXG backed by slightly less than an ounce, so Paxos reserved the right to break its own headline promise, disclosed it, and never used it. Redemption runs to USD at market, to Unallocated Gold by wire, or to physical at 430 PAXG (~US$1.73m), USD conversions rounding down to the nearest 1/100th ounce, delivery risk on the holder: "you are responsible for delivery and once your bars are in the possession of the delivery service you choose, then Paxos will have been deemed to have fulfilled its obligation for delivery." Discretion is reserved in capitals: "WE MAY FREEZE, TEMPORARILY OR PERMANENTLY, YOUR USE OF, AND ACCESS TO, PAXG OR THE LONDON GOOD DELIVERY GOLD BARS BACKING YOUR PAXG, WITH OR WITHOUT ADVANCE NOTICE," and PAXG "AND THE ASSETS BACKING SUCH PAX MAY BE FORFEITED" and may "BECOME WHOLLY AND PERMANENTLY UNRECOVERABLE AND UNUSABLE."

#### Liquidity and distribution

At 28 July 2026: ~US$4,027 per token, ~US$1.79bn market cap, ~US$105.6m 24h volume, ~444,808 tokens (~13.8 tonnes). The US$5,619.09 all-time high in January 2026 is a gold-price artefact, not a premium event. Turnover runs roughly 5.9% daily and PAXG trades at or near net asset value, since any holder of 430 PAXG can mint a premium away. Distribution is paxos.com and the Paxos wallet under KYC, plus Binance, Kraken, Coinbase, Gemini, Backpack and BitMart, and Solana DeFi through Sunrise DeFi with LayerZero Stargate bridging. No India, UAE or NRI channel, no savings plan and no referral structure was found.

#### Relevance to Aurumix

The transferable asset is the dilution clause. Minting to itself would break a one-token-one-ounce peg, which is why Paxos has never fired it. For Aurumix, whose price is grams divided by tokens, dilution is peg-neutral by construction: mint to treasury, price per token falls by the fee, grams-to-tokens survives. It collects nothing from a US$20-per-month saver and binds holders who never log in. Adopt the mechanism and copy the disclosure discipline: state the rate, state that it is charged by issuance, commit to advance notice. PAXG pays no yield at US$1.79bn and its gold sits unencumbered at Brink's. An OCC-supervised trust bank will not lend or lease client metal to manufacture a return, which leaves the ICS Dividend without a funding template. PAXG also trades at par on a live mint-and-redeem channel, so Aurumix's closed redemption is the only thing that could hold a premium, making any premium a product of the exit restriction rather than demand. Say that plainly before it enters the revenue model. Match the monthly KPMG cadence, then take the opening Paxos leaves: no full public bar list, no proof-of-reserve feed. The 430 PAXG minimum is an arbitrage backstop and a marketing line, out of reach of a US$75-per-month saver, and a high-minimum fee-bearing physical option is the standard construction. Cash-only buyback is defensible, but then "you own physical gold" cannot be claimed unqualified. Paxos bought listings with an anonymous stateless token and retrofitted freeze-and-wipe control. Aurumix cannot, since tier, dividend, credit standing and buyback rights are holder state an anonymous transfer destroys, and Paxos itself chose Token-2022 on Solana. Its structure argues for severability: gold core licensed as an ARVA, dividend and credit in a separate entity. Distribution is the gap, with no SIP, no agent tier and a US$2 monthly inactivity fee penalising the dormant saver. There is still no wind-down procedure and no trustee, and a stale NYDFS reference sits on a live transparency page.

### 4.3 Kinesis Money (KAU)

| Field | Detail |
|---|---|
| Issuer | Kinesis Cayman, Cayman Islands exempted company. CEO Thomas Richard Archer Coughlin. |
| Licence covering the token | None. CIMA VASP approval is conditional only. |
| Assets under management | ~US$310.2M cap, 2.386M KAU (2.386 t gold), US$130.01, 28 July 2026. |
| Backing | 1 KAU = 1 g allocated gold, held by Kinesis as bailee. |
| Custody fee charged to holders | 0%. |
| Yield paid to holders | Holder's Yield, 15% of the Master Fee Pool. Advertised 2.05%. |
| Redemption | Physical, 1,000 KAU per 1 kg bar (~US$130,000), 0.45% plus US$100. |
| Token standard | Kinesis Blockchain Network, permissioned. ERC-20 wrapper on Ethereum. |
| Reserve verification | Bureau Veritas / Inspectorate International, twice yearly. No bar list. |

#### What it is

Kinesis is a monetary system built around gold and silver, not a bare custody receipt. KAU is a 1-gram allocated-gold token on the Kinesis Blockchain Network, wrapped in a full retail stack: an in-house exchange, a debit and virtual card, a merchant directory, multi-asset payroll, and a fee-sharing yield system paying holders, minters, depositors and referrers. Live since 2018, it is one of very few gold tokens paying a recurring, contractually documented distribution to ordinary holders, which makes it the closest live analogue to the ICS Dividend anywhere. Eight years of published payouts mean the arithmetic can be checked rather than taken on trust.

#### Legal structure and regulatory standing

The native-chain title language is the strongest in this set. Terms of Use clauses 5.1.1 and 7.1.1 state that "legal and beneficial title in the Allocated Bullion backing the Kinesis Currency will remain with the Kinesis Currency holder until such time as all or part of the corresponding Kinesis Currency is transferred to another Kinesis Address." Clause 4.1.2 adds that "Kinesis will store that Bullion as bailee on behalf of all holders of that particular Kinesis Currency, whereby each holder of that Kinesis Currency has an undivided interest in the total pool of Bullion in proportion to the amount of Kinesis Currency held." Bailed property does not fall into the bailee's insolvency estate, so this beats a creditor claim. Regulatory standing is thinner than the marketing suggests. Kinesis's own Q4 2025 / Q1 2026 update says only that it "has received conditional approval for a Virtual Asset Service Provider (VASP) license from the Cayman Islands Monetary Authority (CIMA)", and a search of CIMA's regulated-entities register returns no entity named Kinesis. Australia gives AUSTRAC registrations DCE100865184-001 and IND100865184-001, which are anti-money-laundering registrations, not financial-services licences. The Bank of Lithuania register lists UAB Kinesis Money Lithuania (code 305992161) only as a distributor of e-money, with no MiCA CASP authorisation found. Kinesis deactivated its site for UK users in late 2025 rather than seek FCA authorisation.

#### Custody and reserve verification

Brink's and Loomis are named as vault operators, Loomis for Zurich, across vaults marketed in London, New York, Zurich, Dubai, Singapore, Hong Kong, Sydney and Brisbane. The attestation is among the better performances here: Bureau Veritas / Inspectorate International on a fixed twice-yearly cadence, publishing absolute gram figures. The 17 October 2025 audit reported 2,393,328.835 g of gold and 3,729,719.331 ozt of silver, which reconciles near-exactly against 2.386 million KAU circulating in July 2026. Two gaps sit against it. No bar list with serial numbers is published, and there is no live proof-of-reserve feed, leaving a six-month unverified window between audits. The explorer Kinesis publishes is a supply feed, proving how many KAU exist rather than how much gold sits in the vault. No smart-contract audit has been published for the wrapper or the chain.

#### Fees, revenue and redemption

Storage costs holders nothing. Minting costs 0.45% plus a ~0.23% spread, exchange execution 0.22%, and sending KAU to another Kinesis account or an external wallet costs 0.45%, which is the core yield-funding fee. Fiat withdrawal runs US$25 to US$90; card rails through Banxa and others cost 1.99% to 5.99%. Kinesis states it redistributes 57.5% of every fee back to users, implying the residual ~42.5% funds vaulting and operations. The structural point outruns the rates: this is a velocity tax, not an assets tax, so a buyer who never moves KAU generates nothing and costs Kinesis real money in storage. Redemption is genuine. Clause 8.1.1.1 provides that "at any point in time, you may request for your Kinesis Currency to be redeemed into Allocated Bullion", at 1,000 KAU per 1 kg bar under clause 8.1.1.10, though each request "shall be managed on a case by case" basis and Kinesis "may at its ultimate discretion, prescribe reasonable minimum withdrawal quantities".

#### Liquidity and distribution

Daily volume of US$219,282 against a US$310.2M cap is 0.07% turnover, and 98.5% of it sits on Kinesis's own exchange: KAU/C1USD at US$212,814 (96.93%) and KAU/USDT at US$3,455 (1.57%), with Emirex KAU/USDT at US$1,398 (0.64%). Eight years produced almost no independent third-party market. Distribution maps onto Aurumix's agent model: Recruiter Yield at Schedule 6 clause 8 pays a perpetual share of referred users' execution fees, 7.5% in the worked example. There is no savings plan and no auto-debit contribution schedule.

#### Relevance to Aurumix

The dividend arithmetic is the finding. Kinesis paid US$26,326.32 in Holder's Yield on gold in June 2026 against a US$310.2M market cap: 0.0085% for the month, roughly 0.10% annualised, against an advertised 2.05% aggregated 12-month yield. The two are irreconcilable by a factor of about 20, because 2.05% is almost certainly a per-holder compounding figure on a subset of eligible balances rather than a yield on total assets. Work backwards and it gets worse for Aurumix: US$26,326 at a 15% pool share implies a ~US$2.1M annual fee pool, which at 0.45% implies ~US$468M of annual volume, about 1.5 times AUM. A genuinely transactional eight-year-old platform turning over its asset base one and a half times a year pays holders a tenth of a percent. A near-zero-velocity SIP cannot fund 5% from recycled fees. Two structural lessons transfer. Kinesis split the instrument, keeping KAU as the commodity and selling KVT as a capped 300,000-unit revenue-share security under an Offering Memorandum. And the ERC-20 wrapper strips everything: KMS Labs S.A. (155772003) terms state holders "have no legal, equitable or beneficial right, title or interest in or to the Reserves", and wrapper holders receive no yield. Marketing does not draw that distinction. If Aurumix wraps a permissioned base token, it must.

### 4.4 Streamex (GLDY)

| Field | Detail |
|---|---|
| Issuer | Streamex Ltd., Cayman Islands exempted company, formed February 2026. |
| Licence covering the token | None. Sold under Rule 506(c) of Regulation D. |
| Assets under management | ~$12.84M (July 2026). $15.225M gold at cost at 31 March 2026. |
| Backing | 1 GLDY = 1 fine troy ounce, held by the SPV. May be unallocated. |
| Custody fee charged to holders | Not disclosed. Borne inside the SPV, reducing net yield. |
| Yield paid to holders | "Up to 4%" advertised, 3.50% APY July 2026. Paid as scrip. |
| Redemption | 90 days' prior written notice, subject to "certain limitations". |
| Token standard | ERC-20 on Base, CCIP to Solana. Whitelisted, accredited only. |
| Reserve verification | EisnerAmper LLP examination as of 31 March 2026. No bar list. |

#### What it is

GLDY is a gold-backed security token paying yield sourced from real third-party gold leasing, issued by a Cayman SPV whose ultimate parent is Nasdaq-listed. Each token is intended to correspond to one fine troy ounce held by the SPV, and yield accrues because that gold goes into Monetary Metals' commercial leasing programme rather than sitting idle. It matters to Aurumix for one reason: this is the only protocol here where the yield-generating arrangement appears in a document filed with a securities regulator rather than asserted in marketing. The parent is a former medical device company, BioSig Technologies, renamed 12 September 2025. The legacy business is still on the books.

#### Legal structure and regulatory standing

A GLDY holder owns "a non-voting digital share of Streamex Ltd., a Cayman Islands special purpose vehicle". That is equity in a Cayman company, not title to gold and not a trust beneficial interest. The listed parent is Streamex Corp., Delaware, CIK 0001530766, Nasdaq: STEX; the operating company is Streamex Exchange Corporation, incorporated in British Columbia 5 April 2024 and acquired 28 May 2025; the servicer is GLDY ServiceCo, LLC, Delaware. The filed agreement is real: Form 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1, the executed "Tokenized Yield Partnership Agreement" between "BioSig Technologies, Inc. d/b/a StreamEx" and "Monetary Metals & Co.", signed by Henry McPhie and Keith Weiner, governed by Delaware law. It covers exclusivity, volume commitments, fee rebates and revenue share. It does not cover the lease. Section 3.03 defers that to "Lease Documentation" to be "developed and mutually agreed" later, and Section 14.13 puts those documents under New York law. The exhibit contains no security interest, no title-retention clause, no risk-of-loss allocation, no subordination or loss waterfall, and no lessee default provisions. Section 13.02 caps StreamEx's liability at six months' fees "OR $500,000, WHICHEVER IS LESS". The 10-K states holders "may face delays, partial recovery, or total loss".

#### Custody and reserve verification

The custodian is described only as "an LBMA-accredited custodian" and is not named in any SEC filing. No vault or city is disclosed, gold may be held unallocated, and no bar list is published. The 10-K concedes that "there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars." The attestation is real and the contract audit is not, which reverses the usual pattern. EisnerAmper LLP examined management's assertion under AICPA attestation standards as of 31 March 2026, announced 1 July 2026: 3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces, a surplus of 0.2416423 oz, covering gold in reserve and gold on lease. Two qualifications belong with it. The parent held 98.5% of the tokens at the same date, and EisnerAmper became the parent's statutory auditor on 8 July 2026, a week later.

#### Fees, revenue and redemption

No subscription, custody or redemption fee is disclosed; costs sit inside the SPV and reduce net yield. Exhibit 10.1 Section 6.01 sets the Monetary Metals purchase-fee ladder at 0.75% up to $250K, 0.55% to $1M, 0.40% to $5M, 0.30% to $25M, 0.25% to $50M and 0.20% above, rebated quarterly in cash, with a 0.35% to 0.50% revenue share running the other way. The yield promise is arithmetically fundable because it is external, not recycled. Article I defines a "Passing Lease" as one that "generates a net yield of at least three percent (3%) per annum after origination fees", and Section 3.01(b) lets Streamex reject any lease "in its absolute and sole discretion". Yield is paid monthly as scrip dividends reinvested as new tokens, not cash. Redemption takes 90 days' written notice, payable in physical gold, stablecoins, select digital assets or dollars; the 10-K says physical redemption "may only be available under certain conditions". The notice period is the liquidity mismatch made explicit.

#### Liquidity and distribution

Roughly $12.84M of assets against 19 holders in July 2026, of which the Q1 2026 10-Q states "the Company held approximately 98.5% of outstanding GLDY Tokens", with two related-party officers subscribing ~$225 thousand in March 2026. Read it as a tokenized corporate treasury position. A 27 May 2026 8-K announced ~$12M of liquidity infrastructure and an Orca AMM on Solana, but no public volume figure exists. Minimums are $200,000 individual, $300,000 joint, $1,000,000 institutional. There is no SIP, no recurring purchase and no agent network.

#### Relevance to Aurumix

Three clauses are worth copying almost verbatim: the 3% net-after-origination-fees Passing Lease floor, the absolute discretion to reject any lease, and the two-layer insurance schedule. Schedule 1 requires the lessee to fund a jeweller's block policy at "no less than one hundred ten percent (110%) of the U.S. dollar value of the Total Lease Amount" from an A.M. Best A- or better insurer, plus a Monetary Metals-funded Difference in Conditions and Difference in Limits policy through a Lloyd's of London broker covering "both mysterious disappearance and 'bad acts' by the lessee's management and owners, including but not limited to fraud, misappropriation, or other willful misconduct", also at 110%. Then the gap. Both layers say Monetary Metals is named loss payee "wherever possible", which is best efforts rather than a covenant, and nothing names the SPV or holders at all. Insurance proceeds land at Monetary Metals and travel back down a contract chain through a commingled pool where "other lessors may receive more favorable terms or priority in enforcement scenarios". The AgaBullion lessee default of 26 January 2026, with Turkish seizure, is the live test, and whether the Lloyd's layer paid has not been published. Streamex sells this to accredited buyers at a $200,000 minimum. Aurumix would sell the same risk to a saver putting in $20 a month.

### 4.5 Comtech Gold (CGO)

| Field | Detail |
|---|---|
| Issuer | ComTech FZCO (DAFZA), Dubai Airport Free Zone. Parent Trade Fintech Ltd, DIFC 5102. |
| Licence covering the token | None. Absent from the VARA, DFSA and ADGM FSRA registers. |
| Assets under management | ~$5.04M cap at 28 July 2026. Last published reserve 111 kg. |
| Backing | 1 CGO = 1 g of 999.9 gold in 1 kg bars. Stored with Transguard, UAE. |
| Custody fee charged to holders | 0%, free for the first 24 months. |
| Yield paid to holders | None. Terms Part B describes an opt-in gold-financing facility. |
| Redemption | Contractual minimum 1 kg (clause 8.1) at 0.50% plus making charges. |
| Token standard | XRC-20 on XDC, `0x8f9920283470f52128bf11b0c14e798be704fd15`. Not permissioned. |
| Reserve verification | Self-issued ComTech FZCO letters. Last dated 21 March 2025. |

#### What it is

Comtech Gold sells one gram of Dubai-vaulted gold per token on XDC. Live since 2022, it runs two products off one reserve: a token listed on centralised exchanges, and an app-based savings product priced in AED with KYC onboarding and a UAE bank account. The primary domain comtechgold.com now redirects to cgold.ae, the retail app site. This is the closest UAE analogue to what Aurumix intends: retail-facing, AED-priced, app-first, aimed at the same Indian expatriate and Gulf segment. It is also small, with 39,000 CGO on-chain against a $5.04M market capitalisation, and it has gone quiet.

#### Legal structure and regulatory standing

The issuing licence is DAFZA 05069, issued to ComTech FZCO on 21 February 2022 for "gold and other precious metals trading". It is not a DMCC licence. The separate ComTech FZCO (DMCC) licence DMCC-889799 (cert DMCC197166), issued 26 June 2023, covers IT consultancy, network consultancy, internet consultancy and software house activity only. Neither permits issuing a virtual asset to the public. Both display as expired on Comtech's own page at cgold.ae/companyregistration: DAFZA expiry 20 February 2024, DMCC expiry 25 June 2024. The page was probably never updated after renewal, but current good standing cannot be confirmed from the public record. VARA's remit covers the Emirate of Dubai including DAFZA and DMCC, and Comtech appears on none of VARA's register of 52 licensed virtual asset service providers, the DFSA register or the ADGM FSRA register. Trade Fintech Ltd sits in DIFC with no DFSA financial services licence. The FAQ nonetheless states that ComTech Gold "is regulated by Dubai Airport Free Zone Authority (DAFZA) and endorsed by local UAE government body DMCC" and follows "the regulatory guidelines towards the capital reserve, consumer protection, compliance, and anti-money laundering". A free zone authority is a registrar, not a financial regulator.

#### Custody and reserve verification

Transguard, an Emirates Group company, holds the metal, though the clause permitting storage "in the UAE or elsewhere" and through affiliates "anywhere in the world" is broader than the marketing suggests. Comtech publishes gold-stock letters, not audits: each on ComTech FZCO letterhead, signed "For ComTech FZCO", with no independent examiner named. Eight letters cover 1 May 2022 to 21 March 2025, with the interval stretching from about three weeks to a single 17-month gap. The last reports 111 kg, split 19 kg on DMCC Tradeflow and 92 kg with a "vaulting partner", down from 144 kg after 62 kg of withdrawals: a 23% net decline, unexplained, with nothing published since. No bar list exists despite the whitepaper promising bar-number identifiability. The Shariah certifier also changed, from Amanie Advisors to Sābiq Advisory on 31 March 2026, announced nowhere.

#### Fees, revenue and redemption

The published fee table and the live app disagree, and the difference is the entire revenue model. The website lists transaction, custody and insurance fees as "Nil", with 0.50% for transfers and 0.50% for physical redemption. The live app configuration endpoint returns a buy commission of 1.0125%, a sell commission of 0.9950%, an AED payment charge of 1%, a card and mobile-wallet charge of 2.4%, a USD charge of 0.27% and 5% VAT, with a round-trip spread of roughly 1.8%. So Comtech funds itself from margin at the point of sale, not from custody, and because nothing is deducted in grams the peg never drifts. Redemption is where the binding document and the marketing part company. Clause 8.1 sets the minimum at 1 kilogram, roughly $129,000 at ~$129 per gram; the advertised 10 g route is a discretionary retail service through partner jewellers. The FAQ reserves the right to charge "a nominal fee to cover storage costs" after 24 months.

#### Liquidity and distribution

CGO trades at roughly $129.31 on 24-hour volume of roughly $814,566, of which $814,072 (99.94%) is a single CGO/USDT pair on Bitrue at a 0.42% spread. BitMart turns over $280 at 3.17%; the XSwap V3 pool turns over $213 at 2.21%. Genuine on-chain liquidity is about $200 a day. Distribution is app-first and UAE-centric: iOS and Android, AED-denominated, 0.5 g minimum, banking through ZAND Bank. Kalyan Jewellers is a named "Authorised Partner", and the app carries a live referral code, `LULU25`. There is no savings plan and no agent tier.

#### Relevance to Aurumix

The licensing lesson is negative. Comtech issues a gold token to the public from Dubai on a bullion-trading licence and an IT-consultancy licence, neither of which authorises virtual asset issuance, and it appears on no regulator's register. There is no Dubai gold-token path that routes around VARA, only an absent authorisation nobody has closed. Anyone arguing that Comtech does this on a free-zone trade licence so Aurumix can too should be shown the FAQ passage telling retail customers they are regulated by DAFZA. That statement attracts enforcement rather than deflecting it. The custody-fee mechanism is the useful finding: zero custody fee recovered through ~1% commission plus a ~1.8% spread, with nothing deducted in grams, which validates Aurumix's instinct to avoid gram-denominated fees. The catch is specific to Aurumix. Transaction-margin funding only works if people transact, and a monthly SIP collects that margin once on the way in, then carries storage cost indefinitely. Comtech reserving a storage fee after 24 months is the tell that this does not close on its own. On proof of reserve the bar is low enough to clear cheaply: a genuine independent attestation on a fixed cadence, a real bar list, and a clear separation between contract audit and reserve attestation.

### 4.6 The Remaining Eleven Live Protocols

Eleven further protocols are live, and each is assessed against the same nine fields as the detailed profiles above, ordered by assets from largest to smallest. The tables below split those nine fields across three views so they fit the page. Where a cell reads "not disclosed" or "none identified", that is the research finding itself rather than a gap in the work: the issuer publishes nothing on the point, and the silence is what a buyer should weigh.

**Issuer, licence and scale**

| Protocol | Issuer and domicile | Licence covering the token | Assets |
|---|---|---|---|
| Pleasing Gold (PGOLD) | Pleasing International (HK) Limited, Hong Kong, incorporated 2023; issuing entity never reconciled across documents | None identified; GitBook claims a "licensed modular RWA platform" naming no regulator | Issuer claims ~US$90M; third-party data ~US$79.8M, 19,505 tokens |
| AZ Gold Reserve (AZG) | Arizore LTD, Nevis; no registration number published, no register entry obtainable | None identified; rwa.xyz attributes an ASIC licence that does not exist on any ASIC register | $64,993,677 per issuer reserve API, 28 July 2026 |
| Matrixdock Gold (XAUm) | Matrix Mining Limited, BVI reported, held under a purpose trust; absent from every searchable register | None identified in the issuer's own name; Matrixport group licences do not attach to XAUm | ~$52.7M, 12,882.21 tokens |
| MG 999 / Libeara (MG999) | FundBridge Capital Pte. Ltd., Singapore; platform Libeara (Singapore) Pte. Ltd., UEN 202302950G | MAS CMS licences held by platform and manager; no product approval, accredited investors only | ~$12.44M, NAV $130.00 on 95,983.65 tokens |
| Digital Gold (DGLD) | Gold Token SA, CHE-287.630.262, Carouge, Geneva; wholly owned by MKS PAMP since 20 November 2025 | None; VQF self-regulatory affiliation only, not FINMA supervision | ~$8.1M, ~2,004.85 DGLD |
| Aurus (tGOLD) | Aurus Technologies Ltd, company no. 11703940, England and Wales, SIC 62012; partners mint, not Aurus | None identified; no FCA authorisation, regulated activity sits with partner firms | $7.10M protocol value; tGOLD ~$5.6M, 43,322 tokens |
| VNX Gold (VNXAU) | VNX Commodities AG, FL-0002.654.271-8, Vaduz, Liechtenstein | Six TVTG registrations, none of type "Licence"; no Token Issuer registration | 13,100 g attested at 31 December 2025, ~$1.7M |
| Midas GoldZip (XGZ) | GoldZip Digital Pte. Ltd., UEN 202119588Z, Singapore; ACRA activity software development | Singapore Ministry of Law precious metals dealer registration only, an AML/CFT gate | ~$5.06M, 39,000 XGZ, 264 holders |
| ORO / Oro Finance (GOLD) | Oro Labs PTE Ltd., UEN 202434484G, incorporated 22 August 2024, Singapore; activity "other holding companies / software development" | None identified anywhere; terms say the token is "issued by independent Third-Party Service Providers", never named | 608 oz (~$2.45M) against a stated $1B year-one target |
| WisdomTree Gold (WTGOLD) | WisdomTree Digital Trust Company, LLC, New York; parent WisdomTree, Inc. (NYSE: WT) | NYDFS limited purpose trust company charter, 22 March 2024, a real licence | ~$2.0M to $2.5M, ~660 holder addresses |
| Tenbin Gold (tGLD) | Tenbin AssetCo (BVI) SPC Ltd.; operating team Tenbin Labs, New York | None identified; third-party data classifies the framework "Non-Regulated" | ~258 tGLD, roughly $1.05M, private beta |

**Backing, fees and exit**

| Protocol | Backing | Custody fee | Yield to holders | Redemption |
|---|---|---|---|---|
| Pleasing Gold (PGOLD) | 1 token = 1 troy oz LBMA gold claimed; terms confer no title or pro rata claim | 0%, "no ongoing custodian fees" | Advertised 5% on ~$79-90M, funded from redemption fees and a market trading under $20 a day | Physical, Hong Kong only, 0.50%, "institutional and qualified holders" undefined |
| AZ Gold Reserve (AZG) | 1 token priced at 1 oz but holds 0.4948 oz bullion; 62.0% is unmined in-ground resource | Not disclosed by issuer; a third-party listing shows 1.00% | None to holders; 15% maximum annual yield goes to miners on the other side | None committed; terms disclaim "liquidity, market access, convertibility, or redemption pathways" |
| Matrixdock Gold (XAUm) | 1 token = 1 troy oz, 1kg bars at Brink's and Malca-Amit, Singapore and Hong Kong | 0%, reversible on 30 days' notice | None; no leasing, lending or rehypothecation | Stablecoin at T+3, 0.25%; physical from 32.148 XAUm (~$130,000), both KYC-gated |
| MG 999 / Libeara (MG999) | No gold; a secured loan to jeweller Mustafa Gold, collateral is shop inventory | No gold custody fee; 1.00% management fee | ~2.3% net advertised while borrowing gold at 2.5% gross, which does not reconcile | Cash only, daily, 0% fee; physical is structurally impossible |
| Digital Gold (DGLD) | Holders own the gold outright at law: Swiss co-ownership (art. 646) plus indirect possession (art. 919) | 0%, costs "embedded in DGLD" | None; terms expressly disclaim any debt, equity or financial claim | Minimum 1 gram, 0.20% burn fee plus shipping at cost, KYC at delivery only |
| Aurus (tGOLD) | 1 token = 1 gram LBMA gold owned by Provider Partners; no vault company named | 0%, "no storage fees for Aurus tokens" | None on tGOLD; ecosystem token holders take 50% of the fee pool | Physical via a Provider Partner; 1.5% burn fee plus undisclosed Provider markup |
| VNX Gold (VNXAU) | 1 token = 1 gram; terms define this as 1/1000 co-ownership of a 1kg bar, held in VNX's name | 0%, plus EUR 10 monthly inactivity fee until the balance reaches zero | None; no staking, no APY, no disclosed leasing | Physical at 1 kg minimum (~$129,000), or cash via the platform, whose exchange closed 30 June 2026 |
| Midas GoldZip (XGZ) | 1 token = 1 gram of 99.99% gold in HKGX-accredited vaults; title construct not documented | Not disclosed whether any is charged; 0.01% sender-paid transfer fee | None; the gold is not lent or leased | Documented at a 1 kg floor (~$129,700) against a ~148 g average holding; no window has opened |
| ORO / Oro Finance (GOLD) | 1 token = 1 troy oz LBMA and UAE Good Delivery gold, vaulted with Brinks; vault city not disclosed | 0%, recovered from the leasing spread and mint and redeem fees | 3-4% APY advertised via Monetary Metals leasing; holder claim ranking undocumented | USDC at 0.50% plus a 1.5% settlement charge; physical from 1 g, pickup UAE only |
| WisdomTree Gold (WTGOLD) | 1 token = 1 troy oz LBMA Good Delivery gold at HSBC Bank plc, London, asserted allocated | 0%, no subscription or minting fee | None | Minimum one full ounce; fee is the greater of one troy ounce or 2%, so 100% at the minimum |
| Tenbin Gold (tGLD) | No gold: USDC collateral plus long CME futures; the holder owns a BVI debt note | None, because no custody exists | Real 4-6% gold-denominated yield, funded by futures basis and stablecoin rates | Stablecoin only, ~30 seconds, 0% during CME hours; KYC-approved counterparties |

**Token, verification and read-across**

| Protocol | Token standard | Reserve verification | Relevance to Aurumix |
|---|---|---|---|
| Pleasing Gold (PGOLD) | Plain ERC-20, Arbitrum, Ethereum and Pharos; permissionless, Chainlink CCIP since June 2026 | None published; Beosin audited the staking contract only, not reserves | The live anti-pattern for the ICS Dividend: a 5% headline the disclosed fee lines cannot fund, on a dormant market, sold as "audited" |
| AZ Gold Reserve (AZG) | Plain ERC-20 behind an EIP-1967 upgradeable beacon proxy; source not verified onchain | None; a JSON endpoint returns six numbers with `lastUpdatedIso` null. rwa.xyz attributes an auditor that does not exist | Shows what opacity costs: incorporate where nobody can verify and aggregators will invent your custodian, auditor and regulator |
| Matrixdock Gold (XAUm) | Plain ERC-20 across nine chains; permissioned only at mint and redeem | Bureau Veritas semi-annual physical count; onchain proof-of-reserve oracle caps a Global Mint Budget | The 0.76% two-way primary spread caps any premium. No arbitrageur pays 3-8% over spot for something mintable at +0.38% |
| MG 999 / Libeara (MG999) | ERC-20 on Ethereum, Arbitrum and Avalanche; contract addresses not published | None possible, no reserve exists; KPMG audits fund financials, not metal | A real MAS licence bought disclosure relief, not disclosure. The accredited-investor exemption is what removes the obligation to publish |
| Digital Gold (DGLD) | Plain ERC-20 on Ethereum and Base, freely transferable, redeployed March 2026 | Per-wallet PAMP bar serial lookup at dgld.ch/verify; no named-firm attestation | Six years dormant harmed nobody because title sat with holders at law, which is why MKS PAMP could buy the issuer and restart it in November 2025. Live, not dead |
| Aurus (tGOLD) | Plain ERC-20 on Ethereum and Polygon, upgradeable since November 2022 | None published; NonceBlox audited the 2022 migration code, report not linked | The fee pool splits 50% ecosystem holders, 25% vaults, 25% providers, with resellers at 0%, earning only their own markup plus a graduation path. No commission for recruitment |
| VNX Gold (VNXAU) | Marketed as plain ERC-20 but is an upgradeable proxy with freeze, seize and pause powers | Annual ISRS 4400 report by AREVA, Vaduz; custodian Philoro Edelmetallhandel AG | The auditor states the basis of a holder's property right is VNX's own internal register, then expressly declines to opine on it. The register is the title, not the token |
| Midas GoldZip (XGZ) | Plain ERC-20 on Ethereum, no whitelist, 0.01% onchain transfer fee | None published; documentation promises "periodic attestation reports" and has published none | Trades at a discount that arbitrage cannot close: primary minting is HKGX members only and redemption floors at 1 kg against a ~148 g average holding |
| ORO / Oro Finance (GOLD) | SPL token on Solana, mint `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A`, `freezeAuthority` null | None published; RSM named as reserve auditor with no downloadable attestation | Fully permissionless despite docs claiming KYC-whitelisted transfers, and trades at a discount. The closest analogue to Aurumix by holder shape, and the leasing plumbing is undocumented |
| WisdomTree Gold (WTGOLD) | Stellar native asset plus Ethereum; issuer-level authorization flags, no address published | None published: no bar list, no attestation, and no smart-contract audit either | A NYDFS-chartered NYSE-listed parent published neither a code audit nor a reserve attestation and pays no yield. Aurumix can out-disclose it cheaply |
| Tenbin Gold (tGLD) | Non-upgradeable ERC-20 on Ethereum; staked stGLD is ERC-4626; Chainlink CCIP since May 2026 | No reserve attestation; USDC collateral observable onchain, the futures margin leg is not | It pays a real 4-6% because its collateral is productive by construction. A bar in a vault is not, which is the arithmetic behind every zero-yield bullion token here |

## 5. Protocols That Failed

Three protocols stopped operating, and all three carry more transferable lessons than most of the live products, because each failed for a reason that applies directly to a monthly savings model. The Perth Mint Gold Token is profiled in full. Digix and CACHE Gold follow in a table.

### 5.1 Perth Mint Gold Token (PMGT)

| Field | Detail |
|---|---|
| Issuer | Trovio Operating Pty Ltd, ACN 622 224 024, Australia. Registered with ASIC 12 October 2017. Formerly InfiniGold. Branding licence from Gold Corporation |
| Licence covering the token | None identified. No AFS licence; not a registered financial product or managed investment scheme |
| Peak assets | About 1,195 tokens (1,195 fine troy ounces, roughly A$3.5M); US$2.54M market capitalisation on 15 March 2023. Residual supply 0.967 PMGT |
| Backing | 1 PMGT = 1 fine troy ounce, via a Perth Mint GoldPass certificate, itself a claim on Gold Corporation, itself backed by metal in Perth Mint vaults |
| Custody fee charged to holders | 0%. No subscription, storage, management or redemption fee at the token layer |
| Yield paid to holders | None |
| Redemption | Burn PMGT for GoldPass certificates, then transact with the Perth Mint for fiat or bullion. Gold never directly redeemable from the token. Downstream GoldPass fees applied |
| Token standard | ERC-20, Ethereum only, Blacklist and Whitelist contracts behind an upgradeable OpenZeppelin proxy. `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf` |
| Reserve verification | Issuer-hosted live feed at `pmgt.perthmint.com`, branded "Realtime Audit". No named-firm attestation, no smart contract audit located. Feed now offline |

#### What it is

PMGT launched in October 2019, issued by InfiniGold, renamed Trovio in February 2021, under a branding licence from The Perth Mint. One token, one fine troy ounce. The structure wrapped an existing product. The Mint already ran GoldPass, a digital certificate app; Trovio held GoldPass certificates and minted PMGT against them. The Mint stored the gold and issued the certificates. It did not issue the token. The marketing surface said "Perth Mint": government-owned, state-guaranteed, central-bank-grade vaults. The issuer was a small Sydney fintech operating under a licence the Mint could withdraw. Minting required a GoldPass account first, capping the addressable market at roughly 26,700 accounts.

#### Legal structure and regulatory standing

A holder's claim ran through four layers: token, then beneficial ownership of a GoldPass certificate held by Trovio Custodians Pty Ltd (ACN 622 220 517) as bare trustee under a Custody Deed, then the certificate as a contractual claim on Gold Corporation, then metal. The whitepaper states certificates were "recorded separately by Trovio Custodians and there is no pooling, combinations or comingling of Certificates". On paper that beats most tokenised gold. There was no independent trustee, though: Trovio Custodians was a related-party SPV of the issuer, its ACN sequential to the operating company. The headline trust signal was the Western Australian government guarantee, which the whitepaper describes as guaranteeing "the weight and purity of every ounce", citing section 22 of the Gold Corporation Act 1987 (WA). The statute guarantees obligations of Gold Corporation. Trovio is not Gold Corporation, and the Mint's guarantee page covers "customers and stakeholders of The Perth Mint enterprise" without mentioning tokens. No AFS licence was identified, no ASIC action was found between 2019 and July 2026, and every AUSTRAC step named Gold Corporation.

#### Custody and reserve verification

Gold Corporation held the metal in Perth; Trovio Custodians held the certificates. The whitepaper asserts no pooling of certificates, but whether the underlying vault gold was allocated per certificate was never disclosed, and no serial-numbered bar list was published. The reserve feed was PMGT's real strength. A live page at `pmgt.perthmint.com` published the GoldPass certificates backing supply, so a holder could check supply against certificates on demand, which is more than most competitors offered. The issuer branded it "Realtime Audit". It was a self-published data feed, not an attestation, and no named accounting firm ever signed a report confirming certificates matched supply. No smart contract audit report from any named firm was located, though the contracts were open-sourced under MIT. The feed now returns connection refused, so every historical verification claim PMGT made is unverifiable by anyone.

#### Fees, revenue and redemption

PMGT charged holders nothing: no minting fee, no storage fee, no redemption fee at the token layer, no transfer fee beyond gas. Against roughly A$3.5M of assets, that produced no revenue while consuming engineering, compliance, custody and market-making cost. Redemption took two KYC-gated hops through an entity other than the issuer: burn PMGT for certificates, then transact with the Mint. The whitepaper promised "a token holder will still be able to redeem their existing PMGT for Certificates which can then be redeemed for gold with The Perth Mint." That assumed GoldPass would outlive PMGT. The Mint began closing GoldPass around 18 April 2023. From November 2023, manual redemption pays "the backdated gold price minus any fees owing", so fees advertised as nil throughout reappeared at the exit. The Mint's live website still directs holders to pmgt.io, which no longer resolves.

#### Why it stopped operating

PMGT is widely described as a casualty of AUSTRAC enforcement and the Shanghai Gold Exchange doping story. The dated record does not support that. The Perth Mint began discussions with Trovio to exit PMGT in early 2022, before any public AUSTRAC action and roughly a year before the ABC *Four Corners* broadcast of 6 March 2023. AUSTRAC's earliest public step came on 30 August 2022, and the Enforceable Undertaking accepted from Gold Corporation concluded on 22 July 2025 with the Mint cleared and no fine ever imposed. Trovio's own conduct is the strongest evidence. Its 1 March 2023 statement blamed "ongoing investigations into alleged breaches [by Perth Mint] with AUSTRAC and US State Regulation", and was later edited to say the decision was made "due to several factors after a number of years in operation". The second version reads closer to the truth. Trading ceased 30 June 2023 on delisting by Independent Reserve, the token was discontinued 31 October 2023, and the contract was deactivated the next day. The cause was commercial abandonment and zero distribution, not enforcement.

#### Relevance to Aurumix

PMGT is the sharpest control experiment available. It had a government-owned counterparty, a statutory sovereign guarantee, state vaults, a real bare trust with a no-commingling covenant, a live proof-of-reserve feed and a clean compliance record of its own. Four years of that produced about US$2.5M. The trust signals were not the binding constraint; distribution was, and PMGT had none: no savings plan, no recurring purchase, no referral scheme, no agent network, and access gated behind an existing GoldPass account in two countries. Charging zero at every layer meant there was no profit and loss line and therefore no internal advocate when the licensor lost interest, which is the strongest available argument for Aurumix's SIP-plus-fee model. Two further transfers. Redemption routed through a third party is not redemption, so Aurumix should state in writing who executes the buyback if Aurumix stops operating and out of what. And a sovereign or institutional guarantee cited in marketing should name precisely whose obligation is guaranteed, because section 22 guaranteed Gold Corporation's, not the token holder's.

### 5.2 Digix and CACHE Gold

Digix ran from 2014, CACHE Gold from February 2020. Both held real vaulted metal, offered working physical redemption, and ended the way PMGT did: no regulator, no hack, just revenue starvation against an asset base too small to pay for the vault. CACHE adds the second lesson. A published wind-down plan is necessary and nowhere near sufficient, because a bearer token has no holder registry to deliver notice to and no burn on redemption to keep supply equal to claims.

| Field | Digix (DGX / DGD) | CACHE Gold (CGT) |
|---|---|---|
| Issuer and domicile | Digix Physicals Pte. Ltd. (UEN 201724269N) held title, parent Digix Holdings Private Limited (UEN 201724450M), Singapore | CACHE Private Limited, Singapore UEN 201827110K, incorporated 8 August 2018, still a live company on ACRA at 28 July 2026 |
| Ceased | Payment Services Act licence voluntarily withdrawn September 2022, no regulator having acted; operations ended March 2023; parent struck off 19 July 2026 | Ceased to be backed by gold 30 September 2025, 23:59:59 Singapore time; redemption closed 31 October 2025 |
| Peak assets | 122,700 DGX (about 122.7 kg, roughly US$6.0M) in January 2020; 15,400 DGX outstanding today | Roughly US$12.3M. Final supply 100,771 grams, up from 34,301 grams in 2020 |
| Backing and custody | 1 DGX = 1 gram of 99.99% LBMA gold in identified 100g and 1kg bars, The Safe House Singapore plus a Canadian vault. Digix Physicals held legal title; no trustee | 1 CGT = 1 gram allocated gold in third-party vaults (Brink's, Loomis, Dillon Gage IDS, The Safe House). Clause 1.2.3 removes any ownership right; no trustee |
| Fee model | 0.60% per annum demurrage plus 0.13% per transfer, both deducted in gold. Demurrage zeroed permanently in 2019 to match PAXG's fee-free launch | 0.25% per annum storage, up to 0.10% per transfer, 0.50% per annum inactivity after 3 years, all in CGT, all collected only on a transaction |
| Redemption | Minimum 100 DGX or 1,000 DGX, cast bars only, 1% recast fee, collected in person in Singapore within 30 days. Uncollected bars automatically re-minted | Three routes under Clause 5.2: vault collection, insured shipping, or sale to a participating dealer. Minimums from 100 grams, open eligibility, KYC and a Linked Ethereum Address required |
| Reserve verification | Proof of Provenance, an onchain and IPFS bar record, arguably the first real onchain proof-of-reserve. Contracts audited by Yaron Velner and Loi Luu in 2017. Never reserve-attested | GramChain published per-bar photographs, weight, purity, brand, serial number and vault, refreshed by vault staff. No named-firm attestation ever. `explorer.cache.gold` now returns 404 |
| Why it stopped | Zeroed its demurrage, leaving the gold business no revenue while it lived on its ICO treasury. Holders voted that treasury away on 20 January 2020, over 95% on 52 votes, roughly 386,428 ETH or $64M | Ran its Clause 5A plan as written (three months' notice across five channels including Etherscan, a redemption window, default settlement in PAXG at a clean weight ratio) and settled 2.3% of the gold |
| Lesson for Aurumix | Demurrage burned tokens rather than grams, so the gold-per-token ratio never moved. Peg-safe and still commercially fatal: a visible itemised fee cannot be defended against a zero-fee competitor | Two payments totalling 2,362.8 g against 100,771 g left about 98,408 g (roughly $12.0M) unaccounted for; 100,771 CGT sit unburned across 136 addresses, one holding 96.03% with no ETH to move them |

## 6. Business Models and Revenue Patterns

### 6.1 How the category actually makes money

Almost none of these protocols makes money from the gold. They make money at the edges, on the way in and on the way out, or they are carried by a parent. Gate fees are the most common shape and the most honest, because they charge for a service performed: PAXG runs a tiered mint and redeem schedule from about 1% down to 0.125%, XAUT a flat 0.25% each way, Aurus 0.5% to mint and 1.5% to burn. Spread is the invisible alternative, roughly 1.8% at Comtech, about 0.76% two-way at Matrixdock, 2% to 5% at SafeGold in the adjacent Indian market. Transfer and velocity fees, 0.45% at Kinesis and 0.01% at Midas, only work if tokens move. Management fees appear once: MG999 charges 1.00% a year, and it is also the only protocol in the set selling exclusively to accredited investors. The gap is what Aurumix most needs, **a recurring charge that a dormant retail holder actually pays.** Nobody here has solved it, because nobody here has retail savers to charge.

### 6.2 Fee benchmarks

| Protocol | Mint | Redeem | Ongoing to holder | Transfer | Other |
|---|---|---|---|---|---|
| Pax Gold | ~1% tiered down to 0.125% | Same tiered schedule | 0% | 0.02% on-chain | $2/month after 12 months idle |
| Tether Gold | 0.25% | 0.25% | 0% | None | Redemption in full bars only |
| Kinesis | ~0.45% | ~0.45% | 0% | 0.45% | $5 withdrawal |
| Comtech | ~1% commission | ~0.5% plus shipping | 0% for 24 months | None | ~1.8% spread |
| Matrixdock | Within a 0.76% two-way spread | Within the same spread | 0%, reversible on 30 days | None | |
| Aurus | 0.5% | 1.5% | 0% | None | |
| MG999 | Not published | Not published | 1.00% management | Not published | |
| Midas GoldZip | Not disclosed | 1 kg minimum | Not disclosed | 0.01% | |
| Cache Gold (failed) | Yes | Yes | Storage fee, collected only on transactions | Yes | |

**Redemption minimums are the number to watch**, because they determine whether the redemption right is real. PAXG and XAUT require a full London Good Delivery bar, roughly 430 ounces. Comtech's binding terms require 1 kg, about $129,000, with the advertised 10 g retail route discretionary rather than contractual. Midas requires 1 kg against an average holding of 148 grams. Kinesis is the outlier at 100 g. Aurumix has no physical redemption at all, a deliberate choice for retention and credit revenue, and it should be disclosed plainly, because "you own physical gold" is the pitch every one of these products makes.

### 6.3 Which revenue models survive

Sort the sixteen live protocols by whether disclosed revenue covers disclosed costs and a clean pattern appears. PAXG, XAUT, XAUm and WTGOLD are structurally sound, each cross-subsidised by a parent with a separate profitable business. Kinesis, Aurus, Comtech and Midas depend on churn, funding custody out of transaction velocity that runs far below what it requires: Aurus does about $211 a day after seven years, Comtech about $213 a day of genuine decentralised exchange liquidity, and two of the four have reserved the right to start charging storage. Two are unfunded outright. PGOLD advertises 5% on $79M to $90M, roughly $4M a year, against redemption fees on rare redemptions plus a market trading under $20 a day. MG999 pays out of a 2.5% gross lease against a 1.00% management fee plus platform, trustee, administration and audit costs. **A model where custody cost is real and recurring but revenue is event-driven does not survive.** Every failure here died of that mismatch, and two live protocols have publicly conceded it.

### 6.4 What this means for the Aurumix fee design

Aurumix's peg is grams divided by tokens, so removing grams to pay for storage breaks the peg arithmetically. That rules out the obvious approach and leaves four options, not mutually exclusive. Cash settlement from SIP inflow accrues the custody charge daily and settles it out of the monthly contribution and at entry and exit gates: the closest thing to a category norm for a product with recurring inflow, and the primary recommendation. Dilution to treasury mints tokens to the operator, lowering price per token while leaving grams divided by tokens untouched, which is peg-neutral for Aurumix specifically, collects from holders who never log in, and now has OCC-supervised precedent for the drafting language. Spread and gate fees on the Comtech model recover custody through commission and spread with nothing charged ongoing, which Comtech concedes fails past 24 months for buy-and-hold. Cross-subsidy from the credit book and interchange uses the only genuinely external revenue streams in the model, and at scale can carry custody the way a parent carries it for PAXG. One accounting point matters more than it looks: **custody fees are cost recovery, not revenue.** Only the spread above true custodian cost is margin, and booking gross custody as profit would inflate any profit-linked distribution.

---

## 7. Token Design and Value Capture

### 7.1 The two architectures in use

Every protocol here sits on one of two designs. Freely transferable is a plain ERC-20 with no token-level identity checks and compliance enforced at the venue, used by PAXG, XAUT, PGOLD, DGLD, Aurus and most of the long tail: maximum composability and exchange listings, and the issuer does not know who its holders are. Permissioned is an on-chain identity registry with transfer restrictions, freeze and forced-transfer capability, ERC-3643 and its relatives being the standard, used mostly by institutional issuers of tokenized funds and bonds. Kinesis runs a permissioned Stellar fork, VNX a transfer-provider hook, Midas a contract-level transfer fee. A common hybrid puts a permissioned base underneath an ERC-20 wrapper to keep compliance while reaching decentralised venues, and Aurumix has been considering exactly this shape.

### 7.2 The wrapper problem, which is worse than it looks

Wrapping a permissioned token into a plain ERC-20 strips the identity checks, transfer restrictions, freeze and forced-transfer controls. That much is understood. What this research found is that **it can also strip the economic rights, and issuers do not always say so clearly.** Kinesis is the explicit case: its wrapper's terms state that holders have **"no legal, equitable or beneficial right, title or interest in or to the Reserves"** and receive no yield, so bridging a Kinesis token into its ERC-20 form silently removes both the claim on the gold and the income. XAUT runs a wrapper over a restricted base as well and does not disclose whether the wrapped holder has the same legal claim. If Aurumix ships a wrapper, **the rights delta has to be stated in the wrapper's own terms, at the point where a user wraps**, not buried in the base document. That is a small drafting decision with a large consumer-protection consequence, and no protocol in this set does it properly.

### 7.3 What the token is, legally

Three legal designs appear and they are not equivalent. A contractual claim on the issuer is the most common: the holder is an unsecured creditor, and if the company fails the holder queues with everyone else. Co-ownership of the metal at law is rarer, DGLD being the standout, where holders own the gold outright under Swiss co-ownership plus possession and the terms expressly disclaim any debt or equity claim, which is why six years of near-total dormancy harmed nobody. A document of title is rarer still: WisdomTree's WTGOLD sits under New York UCC Articles 1, 2 and 7, with no SEC registration, no transfer agent, and ownership recorded on the blockchain exclusively. VNX exposes the trap underneath all three. Its auditor states that the basis of a holder's property right is **VNX's own internal holder register**, then expressly refuses to opine on it. The token is a pointer. The register is the title. Whatever Aurumix builds, the document carrying legal ownership needs to be named explicitly, held outside the operating company, and examined by an independent party.

### 7.4 Proof of reserve as architecture, not a PDF

Best practice combines three layers and almost nobody runs all three. Independent reserve attestation on a fixed schedule gives system-level assurance, and only DGLD, PAXG, VNXAU and XAUT have anything credible there. Oracle-based proof of reserve feeds custodian data on-chain so contracts can compute collateralisation and halt minting below a threshold, which Cache Gold integrated and which is contract-enforceable rather than advisory. User-facing allocation lookup maps a holder address to bar serial numbers, purity and vault, which PAXG runs. Aurumix should treat proof of custody as a **gate condition** rather than a disclosure: no confirmed allocation, no issuance. That is the difference between a claim about reserves and a constraint on them.

### 7.5 Value capture, and an honest reading of it

| Protocol | Token | Is the token necessary? | Why |
|---|---|---|---|
| Pax Gold | PAXG | Essential | The token is the ownership record |
| Tether Gold | XAUT | Essential | Same |
| DGLD | DGLD | Essential | Carries legal co-ownership |
| WisdomTree | WTGOLD | Essential | It is the document of title |
| Kinesis | KAU / KVT | Important | KAU is the gold claim; the separate KVT captures fee-pool income |
| Aurus | tGOLD / AWO | Useful | tGOLD is the gold claim; a second token captures the fee pool |
| Midas GoldZip | XGZ | Useful | Ownership record, with a transfer fee attached |
| Tenbin | tGLD | Useful | A yield wrapper, not a claim on bullion |
| Streamex | GLDY | Cosmetic in practice | 98.5% is held by the parent |
| AZG | AZG | Cosmetic | Rewards flow to "miners" rather than holders |

The pattern worth noting: **the protocols that pay income to a token do it through a second, separate token**, not through the gold token. Kinesis splits KAU from KVT, Aurus splits tGOLD from AWO. That is the same instinct as paying a reward at the account level rather than embedding it in the asset token, and it is the shape that keeps the gold token classifiable as a commodity claim.

---

## 8. Regulatory Positioning

### 8.1 The classification line, and where Aurumix crosses it

A token that is only a redeemable claim on fully-reserved gold is a commodity-type instrument, and in Dubai that is an ARVA under VARA. Attach a share of platform profit and it starts to look like a security or a collective investment, in all three regimes that matter. In the United States, a company-run dividend meets all four Howey prongs: investment of money, pooling into a common enterprise, an advertised expectation of profit, and profits derived from the operator's efforts. The Kraken staking settlement of February 2023, roughly $30M, and the June 2023 action against Coinbase staking turned on that shape; purely mechanical protocol rewards can fail the fourth prong, a company-set discretionary profit-linked distribution does not. In the European Union, MiCA excludes instruments already treated as financial instruments under MiFID, so an income-bearing token resembling a fund unit falls under securities and fund law instead, and pooling plus managed investment policy equals a collective investment undertaking. In the UAE, the 2025 security tokens and commodity token contracts regulation excludes plain virtual assets and non-security real-world assets, so an embedded profit share signals strongly in the other direction, and VARA separately requires ARVA issuers to disclose exactly what rights the token conveys. The current Aurumix wording is the highest-risk possible formulation: **"15% to 20% of operating profit, with 80% going to the top 10% of holders"** reads as a fund distribution almost word for word.

### 8.2 The credit facility

Gold is low-volatility collateral, so a higher loan-to-value ratio than crypto lending is defensible, subject to two hard constraints. Above 100% LTV lends more than the collateral is worth. The corrected Aurumix ceiling of 90% to 95% sits above every benchmark here but is at least inside the collateral: Indian NBFC gold loans are capped at 75% by the Reserve Bank of India, computed on principal plus interest at maturity for bullet-repayment loans, and crypto lenders run origination LTV far below the liquidation threshold with a reserve or insurance fund absorbing shortfalls. Aurumix's existing 80% warning and 100% liquidation thresholds no longer sit sensibly under a 90% to 95% ceiling and need re-spacing, with an explicit loss-absorbing sink behind them. The India route carries a structural block: the RBI restricts lending against primary gold and against gold-backed financial instruments such as gold ETF and gold mutual fund units, a reason for the credit facility to sit with a licensed country-layer partner rather than on-chain from Dubai. Consumer lending in the UAE separately requires a finance company or lending licence, or a licensed partner.

### 8.3 The UAE routes that remain open

The idea that a Dubai free-zone trade licence offers a route around VARA does not hold. Comtech, the only Dubai-domiciled protocol here, issues on a DAFZA licence for precious metals trading, while its separate DMCC licence covers IT and software consultancy only. Neither authorises public token issuance, and both display as expired on Comtech's own site. That is an unlicensed gap, not a lawful alternative. Three doors remain, all to be priced with counsel. A VARA licence in Aurumix's own name runs roughly AED 100,000 to apply, AED 200,000 a year in supervision, minimum capital of AED 1.5M or 2% of reserves, and six to nine months or longer. The VARA Sponsored Regime or Partnership Model, operating under an existing licensee or outsourcing issuance to a Category 1 holder, is materially faster and cheaper, and worth quoting before assuming the standalone route. ADGM is third, where the Accepted Spot Commodity route is worth investigating; one live register lead exists, Universal Digital Intl Limited holding ADGM FSRA permission No. 250089 with CBUAE payment token registration, though that permission is scoped to fiat-referenced tokens for professional clients, making it a lead rather than a template.

### 8.4 What good disclosure looks like here

Three cheap practices separate the credible issuers. Naming the custodian: XAUT has the strongest reserve attestation in the sector and still does not name its custodian. Publishing a bar list: PAXG and DGLD do, most do not. Separating the smart-contract audit from the reserve attestation in public communication rather than letting the word "audited" carry both, which six protocols here blur.

---

## 9. Distribution, Stakeholders and Incentives

### 9.1 Who participates, and what each party wants

| Party | What they want | Where it breaks |
|---|---|---|
| Holders | The gold to be there, and to be able to get out | Interests split from the issuer's the moment redemption is expensive or restricted |
| The issuer | Assets under management and a revenue line | Where those conflict, as with a redemption minimum that suppresses outflow, the issuer usually wins and the documentation rarely says so |
| Custodians and vault operators | Payment per ounce per year regardless of protocol success | The one party in the stack with no exposure to failure |
| Auditors and attestors | A narrowly scoped opinion | VNX's auditor refusing to opine on the holder register is the clearest example |
| Market makers | A credible mint and redeem right to arbitrage against | Without it they do not anchor the price |
| Distribution partners | Volume through a channel they own | Almost nobody has any |

### 9.2 The distribution gap, and how the adjacent market fills it

The tokenized gold protocols have no distribution. The Indian digital gold platforms have solved it completely, and their method is not a secret: **they embed inside applications the customer already opens every day.** SafeGold powers gold purchase inside PhonePe, Google Pay and Paytm. Jar attaches to UPI round-ups so saving happens without a decision. Minimums of ₹9 to ₹10 remove the last friction. Aurumix's agent network attacks the same problem through a different channel, and the Indian life insurance agency model behind it is a proven distribution machine. The design question is how to pay it without triggering the pyramid analysis.

### 9.3 Designing an agent network that is not an MLM

This is the highest-enforcement-risk area in the whole product, and the case law is unusually clear. The Koscot and BurnLounge two-prong test asks whether participants pay for the right to sell and the right to earn from recruiting, where those rewards are unrelated to sales to ultimate users, and a genuine product does not save a scheme that fails it. FTC staff guidance, reaffirmed in **FTC v. Noland (2023)**, holds that what matters is whether commissions are funded by genuine, non-incidental product revenue rather than by payments for the right to participate. The enforcement roll-call shares one profile: Forsage (SEC 2022 and DOJ 2023, over $300M), BitConnect (2021, $2B), HyperFund (SEC 2024, $1.7B), Forcount (2022, $8.4M) and Mining Capital Coin (2022), every one combining pay-to-participate, no external revenue, recruitment-driven growth and risk-free-return marketing. **Aurumix currently bundles all three of the risk factors**: a profit-linked distribution, a lock-in, and multi-tier referral. That combination, not any single feature, is what has repeatedly drawn enforcement.

Two structural defences work together. Pay for function, not for depth: the Aurus structure directs 50% of the fee pool to ecosystem token holders, 25% to vault partners and 25% to provider partners, with the reseller tier receiving 0% of the pool and earning only its own markup plus preferential bulk redemption and a graduation path. Recast each Aurumix tier so it is paid for something performed, whether capital committed, custody provided or servicing delivered, and use graduation to a higher tier rather than overrides on a downline to motivate top agents. Then tie trailing income to continued contributions, as Indian life agency commission does, where renewal commission is payable only while the policy stays in force, so recruiting for its own sake stops paying. The IRDAI (Payment of Commission) Regulations 2023 percentage tables should be pulled directly before any specific figure is quoted. Alongside both: cap referral rewards, keep them subordinate to investment returns, substantiate every earnings claim, and pay from real platform fee revenue tied to genuine savings activity rather than from entry fees or new-investor money.

### 9.4 Inheritance

The Digital Will is a genuine differentiator and it is legally untested. Precedents are niche and heterogeneous: Casa Inheritance, TrustVerse, Safe-based multisig legacy contracts, DigiPulse with its inactivity trigger, Sarcophagus, and exchange beneficiary programmes, all struggling with detecting death, verifying beneficiaries, and legal validity. In most jurisdictions a smart contract is not a recognised will and probate law governs. Every credible precedent positions the on-chain mechanism as a facilitation and transfer layer alongside a legally valid will, never as a replacement, so the existing Aurumix positioning as a financial transfer instruction layer matches precedent and should be kept. Build the triggers around a nominated executor with know-your-customer checks on beneficiaries, and make the "keep a real will as well" advisory explicit.

### 9.5 Secondary market structure

**The redemption right is what anchors the price.** Arbitrage between token, spot and derivatives is the balancing force, and it works only where a credible mint and redeem path exists for an arbitrageur to use, which Aurumix's closed redemption removes. **Automated market maker pools should be a last-mile convenience layer, not the primary price discovery venue.** Depth and net-asset-value anchoring come from issuance and redemption, identity-gated order books and periodic auctions, and impermanent loss is a real problem for a redeemable asset-backed token in an AMM pool. Seed liquidity should be sized against the genuinely free float, total supply minus locked, pledged and spot-restricted tokens, with slippage modelled so a single large seller cannot disconnect the secondary price from the gold floor beyond a set tolerance.

---

## 10. Gaps, Opportunities and Open Questions

### 10.1 What nobody in this market serves

Four gaps are consistent across all nineteen protocols. The small recurring saver: every protocol is built for a lump-sum buyer, minimums are effectively set by gas costs and exchange listings, and redemption minimums of 430 ounces at PAXG and XAUT and 1 kg at Comtech and Midas are absurd against a retail holding. Nobody has built for someone putting in $20 a month. The holder who wants the gold to do something: the well-documented protocols pay nothing and the ones promising a yield cannot fund it. The holder who wants protection rather than assurance: no protocol names token holders as an insurance loss payee, none publishes a default waterfall, none commits to a trustee holding title plus a holder registry plus burn-on-redemption. And the family: no protocol offers inheritance, beneficiary nomination, or any mechanism for the asset to pass on.

### 10.2 Where Aurumix can differentiate

Ranked by how cheap the differentiation is against how much it is worth. Recurring savings distribution is the moat: the gap is total, the client already understands the channel, and the adjacent Indian market proves the demand. Holder-level protection in the documentation comes second: a trustee holding title, a holder registry, burn-on-redemption, a published wind-down clause with a reconciliation obligation, and holders named as insurance loss payee. Every element is a drafting decision rather than a capital commitment, and no competitor has done it. Honest reserve verification is third, meaning an independent reserve attestation on a fixed schedule, an oracle feed that can halt issuance, and a bar-level lookup, where only three protocols in the entire set have even the first done credibly. Inheritance is fourth, untested legally, but nobody else offers it and the target customer's whole frame of reference is life insurance.

### 10.3 What this research does not yet establish

Three things are genuinely open, and none of them should be filled with an estimate.

**The retail versus institutional split of the tokenized gold market.** The market data available quotes totals only, and this research is protocol by protocol. Aurumix's design actively discourages institutional participation through its redemption and identity model, so sizing against a total that is substantially institutional would overstate the addressable market. This is not established. It is scoped work rather than a finding, and it needs fresh analysis before any growth model is built on it.

**Whether a compliant funding route exists for Indian residents.** The Aurumix business model routes Indian residents through USDT bought via peer-to-peer or over-the-counter channels, with the investor bearing tax disclosure. Under the Foreign Exchange Management Act, purchasing crypto is not an established permitted purpose under the Liberalised Remittance Scheme, the RBI has never approved it, and Indian banks block it. If that holds, **a compliant funding route for an Indian resident may not exist**, and the addressable base is non-resident Indians plus UAE residents plus other international customers. That matters because the primary customer persona in the project charter is an Indian resident life insurance policyholder. This is not established. It is scoped work, it gates any break-even sizing, and it pulls the RBI and FEMA into a regulatory frame that currently names neither.

**Non-resident Indian savings behaviour.** No usable data was found on how the diaspora buys gold, what channels they use, or what friction stops them. This is not established, and given how central that segment is to the client's own thinking, it is scoped work.

---

## 11. Two Decisions for Aurumix

Everything above informs design work that Tokenomics.net can carry. These two do not. They are choices the client owns, and both should be made before mechanism design goes further, because everything downstream is shaped by them.

### 11.1 The dividend: three options, and there is no fourth

This is not an argument about whether the Aurumix dividend is well designed. It is arithmetic about what vaulted gold can pay. Gold in a vault produces no income and costs money to store, so any distribution to holders has to come from one of exactly three places.

**Option 1: encumber the gold.** Lease the metal out and pay holders from the lease income. This is real and documented, and Streamex's SEC-filed agreement is a copyable template with a 3% net floor and two insurance layers. The costs are specific: Aurumix gives up the claim that the gold is 100% allocated and unencumbered, and it inherits lessee credit risk on the very asset backing the token. The AgaBullion default of 26 January 2026 shows what that looks like in practice, and no protocol anywhere has yet documented how a retail holder ranks when it happens.

**Option 2: fund it from operating profit.** This is the current design. It is honest and it is fundable. It is also the formulation that reads most clearly as a profit share, which carries the classification risk, with consequences of heavier capital, licensed venues only, and possible restriction to qualified investors. That fights the $20-a-month mass retail model directly. Mitigations exist, principally paying at the account level rather than as a token-embedded right and framing the payment as discretionary rather than promised, but they reduce the risk rather than remove it.

**Option 3: drop the dividend and compete on the savings plan, the credit facility and inheritance**, which is where the genuine differentiation sits anyway. Every well-regulated protocol in this sector made that choice, including two with far better access to bullion leasing than Aurumix will have. The arithmetic on the other protocols is the persuasive material: Kinesis realised about 0.10% against 2.05% advertised, PGOLD advertises 5% on $79M to $90M, roughly $4M a year, against a market trading under $20 a day, and MG999 funds a 1.00% management fee plus platform, trustee, administration and audit costs out of a 2.5% gross lease.

**Our recommendation is option 3 at launch, with option 1 available later**, once the credit book is real and counsel has ruled on whether a holder-protection layer can be built into a leasing structure under VARA or ADGM. That sequencing keeps the token classifiable as a commodity claim during the licensing process, which is when classification risk is most expensive, and it preserves the yield route as a future product rather than discarding it. This is a recommendation, not a verdict. The decision is the client's and it should be taken explicitly.

### 11.2 The premium: model it at zero

The current model assumes a 3% to 8% exchange premium, and the spot capacity parameter, currently a 20% to 40% range of monthly SIP inflow split 80% to the internal lane and 20% external, **is tuned to produce it.** That parameter trades growth in assets under management against secondary market premium, and it is being traded against a return the evidence says will not appear. Nine protocols across the full liquidity spectrum say the same thing, and the mechanism is a pincer rather than a coincidence: liquid markets arbitrage a premium away, illiquid markets have no price to express one. The two protocols that do trade off spot trade at a **discount**.

The live consequence is that the premium feeds the revenue model, and it is cheaper to absorb now than once revenue modelling is underway. **Revenue projections should carry a zero premium assumption.** If Aurumix's closed redemption does produce a price above net asset value, that is an artefact of blocking arbitrage rather than evidence of demand, and it should be treated as an incidental outcome rather than a planned revenue line. Two things follow. The spot capacity parameter should be re-derived against a different objective, most likely growth in assets under management and lane fairness rather than premium engineering. And the last economic argument for the "mining event" framing goes with it, which turns that into a presentational question. Our leaning is to keep the allocation mechanic and drop the mining metaphor, because it implies an emissions story that invites the wrong regulatory reading.

---

## 12. Conclusions and Recommendations

### 12.1 The seven findings that matter most

1. **The category solved custody and never solved distribution, and that is the opening.** Nineteen protocols, zero savings plans, zero recurring purchase mechanisms, zero retail referral programmes; the best-provenanced product, backed by a sovereign mint, reached $2.5M in four years.
2. **Vaulted gold cannot pay a yield, and every protocol claiming otherwise fails its own arithmetic.** Kinesis realised about 0.10% against 2.05% advertised, and PGOLD promises $4M a year from a market trading under $20 a day.
3. **The premium is zero.** Arbitrage closes it where markets are liquid and there is no market to express it where they are not; two protocols trade at a discount, and the spot capacity parameter needs re-deriving.
4. **A revenue line is a survival feature.** All three failures died of revenue starvation rather than enforcement, hacks or reserve shortfalls, and a fee that only bites on transactions collects nothing from a saver, which is how Cache Gold died.
5. **An anonymous bearer token cannot be wound down.** Cache Gold published a proper wind-down plan, followed it, and still stranded 96% of supply, having no registry to deliver notice to and never burning redeemed tokens.
6. **There is no cheap compliant door, and the Dubai free-zone route does not exist.** Four of nineteen protocols hold a licence covering the token they issue; VARA, the VARA Sponsored or Partnership regimes, or ADGM are what remain.
7. **"Audited" almost never means the gold was checked.** Six protocols publish a smart-contract audit while their reserve attestation is absent, stale or self-signed, and only three have credible independent reserve examination.

### 12.2 What this market rewards and punishes

**Rewards:** a documented legal claim that survives the issuer failing, as DGLD demonstrated across six dormant years; a revenue line that does not depend on customer activity; distribution embedded where the customer already is; reserve verification that names the custodian and publishes the bars. **Punishes:** yield promises that cannot be funded from disclosed sources; redemption rights that exist in marketing at 10 g and in the binding terms at 1 kg; licences described as covering more than they cover; zero-fee models with no parent to carry them.

### 12.3 The main risks to watch

- **Classification.** The dividend plus the credit facility push the token toward a hybrid read, dragging in a second regulator and fighting the mass-retail model. The single largest risk in the product.
- **The combination risk in distribution.** Profit share plus lock-in plus multi-tier referral is the exact pattern behind the largest enforcement actions in crypto, though each element is defensible alone.
- **SIP persistence.** The stoppage ratio in Indian mutual fund SIPs spiked above 120% in 2025, and the entire Aurumix engine assumes contributions continue.
- **The funding route for Indian residents.** If the FEMA and LRS position holds, the charter's primary customer persona may not have a compliant way to pay in.
- **Custody funding.** Every model the category uses is unavailable to Aurumix for structural reasons, and two live protocols have conceded that transaction-margin funding fails for buy-and-hold.

### 12.4 Recommended next steps

1. **Decide the dividend.** Three options, and it is a client decision. This gates the token architecture work and should be settled first.
2. **Re-derive the spot capacity parameter** against a zero premium, and carry a zero premium into all revenue projections.
3. **Commission the retail versus institutional split analysis** before any market sizing. It is not answered by this research and should not be estimated.
4. **Put the FEMA and Liberalised Remittance Scheme question to Indian counsel**, since it gates the eligible-countries and payment-rails questions and determines whether the charter's primary persona is reachable.
5. **Take the Streamex leasing documentation to Dubai counsel** as a worked example, asking whether the holder-protection layer that Streamex omits can be built under VARA or ADGM.
6. **Price the VARA Sponsored Regime and Partnership Model** alongside a standalone licence, rather than assuming the standalone route.
7. **Re-space the credit facility thresholds** under the corrected 90% to 95% ceiling, and specify the loss-absorbing reserve behind them.
