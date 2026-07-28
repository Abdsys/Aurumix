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
