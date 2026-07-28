## 1. Market Landscape

### 1.1 What tokenized gold is, and how big it actually is

The category is nineteen products deep and eight years old. It is far smaller than it looks.

- **Two protocols hold 86%.** Tether Gold about $2.465bn, Pax Gold about $1.79bn.
- **Third place is a cliff.** Kinesis about $310M, then a severe drop.
- **The tail found no buyers.** Of sixteen live protocols, nine hold under $10M and four under $3M, several after five or more years.

### 1.2 What the category has built, and what it has not

Seven years went into custody, and the engineering is serious. Tether Gold carries an ISAE 3000 (Revised) opinion from BDO Italia, Pax Gold a national trust bank charter, WisdomTree an electronic document of title under New York law.

What nobody built is demand. No protocol here operates a savings plan, a recurring purchase mechanism, or a retail referral programme.

- **The best-built failure.** Perth Mint Gold Token had a sovereign guarantee, state-owned vaults, a bare trust and a live proof-of-reserve feed.
- **What it reached.** About US$2.5M in four years before closing, and the post-mortem points at distribution, not product quality.

### 1.3 The regulatory map for a UAE issuer

Five regulators matter to a token issued from Dubai, and classification decides which one it answers to.

- **VARA (Dubai).** Regulates Asset-Referenced Virtual Assets, where a fully-reserved gold token lands. Issuance Rulebook effective 19 June 2025.
- **VARA cost.** Capital the higher of AED 1.5M or 2% of reserves. AED 100,000 to apply, AED 200,000 a year in supervision.
- **VARA timeline.** Six to nine months or longer, every token separately approved.
- **CMA, the former SCA.** Federal securities regulator, covering virtual assets explicitly since its restructure around 1 January 2026.
- **ADGM, DIFC, CBUAE.** A digital securities regime, a tokenisation sandbox, and fiat-referenced payment tokens that exclude gold.

The line runs straight through the product. A redeemable claim on fully-reserved gold is a clean ARVA and retail distribution works.

Add a profit share, a dividend, or a managed-portfolio characteristic and it risks re-characterisation as a security, which engages the CMA regime: heavier capital, licensed venues, possibly qualified investors only.

> **The takeaway.** Two VARA routes are cheaper than a standalone licence: a Sponsored Regime under an existing licensee, and a Partnership Model that outsources issuance to a Category 1 holder. Price both before assuming a full licence is the only door.

### 1.4 The demand picture

Indian households hold roughly 34,600 tonnes of gold, worth about $3.8T on Morgan Stanley's October 2024 estimate. The digital slice is growing fast.

- **UPI gold volume.** Up about 377% in sixteen months, to 99.8M transactions and ₹1,184cr by August 2025.
- **UPI share.** Between 85% and 90% of digital gold purchases.
- **January 2026.** About ₹3,926cr, roughly five times January 2025.
- **Jar, a round-ups app.** Over 20M users saving an average of 22 times a month.

The warning sits in the same data. SIP inflows into Indian mutual funds reached about ₹2 trillion in FY24, but the stoppage ratio spiked above 120% in 2025. More SIPs were cancelled than started.

SIP persistence is the whole Aurumix engine, so stress-test growth targets against realistic lapse rates. Non-resident Indian behaviour, a segment the client calls major, is a data gap.

### 1.5 Where Aurumix sits

Aurumix bundles four things: SIP accumulation, borrowing against the gold, a yield or dividend, and inheritance. No product found here bundles all four.

- **Indian platforms.** Accumulation without credit, yield or inheritance.
- **Tokenized protocols.** Custody without recurring savings or inheritance.

That cuts both ways. No direct competitor, but no proven template and no precedent box for a regulator to file the product in, so novelty amplifies classification risk. Borrow validated components rather than invent each one:

- **Custody model.** Trustee-held allocated gold, from the Indian platforms.
- **Reward mechanics.** Account-level accrual, from Kinesis.
- **Legal form.** Swiss-style co-ownership, from DGLD.
- **Partner network.** Function rather than recruitment, from Aurus.

---

## 2. Nine Findings That Shape the Design

### 2.1 The premium thesis does not survive contact with the market

The Aurumix model assumes a 3% to 8% exchange premium will sustain spot demand and pull in SIP contributions. Nine protocols say it cannot.

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

The mechanism is a pincer:

- **Liquid markets.** Arbitrage closes any premium before it persists.
- **Illiquid markets.** There is no market to express a premium in.
- **Discounts stick too.** Midas XGZ has a 1 kg redemption floor against a 148 g average holding, so arbitrage cannot close a discount either.

> **The takeaway.** Model the premium at zero. If a closed Aurumix redemption does produce a price above net asset value, that reflects blocked arbitrage rather than demand, and is not a revenue line to plan around.

### 2.2 Nobody charges holders a custody fee, and the reasons why are structural

Zero ongoing custody fee is the norm: PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, WTGOLD, DGLD and PGOLD all charge holders nothing. The funding underneath splits three ways, and none is available to Aurumix.

- **Velocity taxes.** Kinesis 0.45% on transfers, Aurus 0.5% to mint and 1.5% to burn, Comtech roughly 1% plus a spread. Storage funded out of churn.
- **Why that inverts here.** A monthly savings product is the lowest-velocity product imaginable. Aurumix users hold, not trade.
- **Parent cross-subsidy.** XAUT from Tether, XAUm from Matrixport, WTGOLD from a $150bn asset manager, PAXG from Paxos. Aurumix has no parent.
- **Deferral, the honest one.** Comtech charges nothing for 24 months, then reserves the right to a "nominal fee". Matrixdock can charge on 30 days' notice.

Both deferrals concede that transaction-margin funding fails for buy-and-hold. Two mechanisms remain, both peg-neutral for a grams-divided-by-tokens design.

**Dilution.** Paxos reserves the right to take storage fees "by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens pro rata", but has never used it because a one-token-to-one-ounce peg breaks on minting.

- **Why it fits Aurumix.** The peg is grams divided by tokens, so minting to treasury lowers price per token and leaves the identity intact.
- **What it collects.** Nothing in cash from a $20 saver, and it still reaches holders who never log in.

**Token-burn demurrage.** Digix burned tokens rather than grams, so the ratio never moved. Also peg-neutral, but three objections survive:

- **It broke integrations.** A non-standard ERC-20 did enough damage that Digix built a wrapper to undo its own fee.
- **It broke in audit.** Auditors found a critical bug and a timing exploit in the fee logic.
- **It breaks the pitch.** A daily decrementing balance is hard to sell against an insurance premium.

### 2.3 The dividend is a three-way choice, not a design problem

Every well-regulated, well-documented protocol pays zero yield, deliberately: PAXG, XAUT, XAUm, VNXAU, WTGOLD, DGLD, Midas XGZ and Comtech. WisdomTree owns a transfer agent, broker-dealer and fund adviser, and still pays nothing. Midas XGZ sits inside a 115-year-old exchange group and leaves the gold idle.

Every protocol that advertises a yield fails the arithmetic.

| Protocol | Advertised | What the numbers show | Gap |
|---|---|---|---|
| Kinesis | 2.05% | $26,326 paid in June 2026 on $310M of assets, about 0.10% annualised | ~20x |
| Pleasing Gold | 5% on ~$79–90M, about $4M a year | Funded from redemption fees on rare redemptions plus a market trading under $20 a day | Unfundable |
| MG999 / Theo | 2.3% net | Borrows gold at 2.5% gross, pays a 1.00% management fee before platform, trustee, admin and audit costs | Arithmetically impossible |
| ORO | 3–4% APY | Real external leasing, but no legal documentation of how holder claims rank | Real source, no protection |

Tenbin tGLD explains why. It pays a genuine 4% to 6% gold-denominated yield from futures basis plus stablecoin rates, and can do that because its collateral is USDC and futures margin rather than bullion.

Vaulted gold yields nothing and costs money to store. Any yield on a bullion-backed token comes from encumbering the metal, from the operating business, or from nowhere.

### 2.4 Gold-leasing yield is documentable. Holder protection is not.

Streamex filed its executed gold-leasing agreement with the SEC: 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1. A real, public, copyable template, with a 3% net floor after origination fees, discretion to reject any lease, and a Lloyd's DIC/DIL policy at 110% of value.

It does not protect a token holder. No security interest, no title-retention clause, no risk-of-loss allocation, no subordination, no waterfall.

- **Best efforts, not covenant.** The insurance loss payee is Monetary Metals "wherever possible".
- **The issuer concedes it.** Its 10-K states holders "may face delays, partial recovery, or total loss", and that other lessors "may receive more favorable terms or priority in enforcement scenarios".
- **Liability is capped.** The lesser of six months' fees or $500,000.

The risk is realised, not theoretical. On 26 January 2026 the AgaBullion lessee defaulted and Turkish authorities seized the leased gold. "Title remains with the lessor" means "we will litigate abroad."

No protocol here names token holders as an insurance loss payee or publishes a default waterfall, so being first is cheap differentiation. Mind the audience gap: Streamex sells this risk at a $200,000 minimum, Aurumix to a $20-a-month saver.

### 2.5 Protocols die of revenue starvation, not of regulators or hacks

All three failures share one cause, and not the expected one.

- **PMGT charged nothing.** No mint, custody or redemption fee. About US$2.5M in four years, and nobody inside the Perth Mint had a commercial reason to fight for it.
- **Digix removed its own revenue.** It zeroed its 0.60% demurrage in 2019 to match PAXG, then lived on its ICO treasury.
- **Then the treasury went.** Holders voted it away on 20 January 2020, over 95% approval on 52 votes, roughly 386,428 ETH or $64M.
- **Cache Gold could not collect.** Clause 6.2.1 charged storage only on transactions, so savers paid nothing while consuming vault cost daily.

Not one died of enforcement, a hack, or a reserve shortfall. No regulator acted against Digix; the licence was voluntarily withdrawn.

A revenue line is a survival feature, and a fee that only bites on transactions is no revenue line in a savings product. That is the argument for the SIP-inflow skim and for dilution, both of which collect from a dormant holder.

### 2.6 A wind-down plan is necessary and nowhere near sufficient

Cache Gold published a real plan at Clause 5A: three months' notice, a redemption window to 26 September 2025, default settlement in PAXG, and a remedy window to 31 October 2025. The issuer followed it.

Only 2.3% of the gold was settled.

- **The shortfall.** Two payments totalling 2,362.8 g against 100,771 g outstanding. Roughly 98,408 g, about $12.0M, unaccounted for.
- **Supply never moved.** 100,771 CGT outstanding across 136 addresses, never burned.
- **One address holds 96.03%.** No settlement, no ETH to even move the tokens, silent five months before the notice.
- **Its claims were waived.** Clause 5A.7 does so pre-emptively. There was never a trustee.

Publishing a plan is too weak a standard. It has to be capable of executing, which needs four things Cache Gold lacked:

- **A trustee holding title.** And a holder registry, so notice is delivered rather than merely published.
- **Burn on redemption.** So supply always equals claims, closed by a final published reconciliation.

An anonymous bearer token cannot be wound down, which is the strongest argument for a permissioned token base at Aurumix. DGLD proves it in reverse: its holders own the gold outright under Swiss co-ownership, so six years of dormancy harmed nobody and a restart was possible in November 2025.

### 2.7 Most of the category operates outside the regulatory perimeter

Four of nineteen hold a licence that actually covers the token they issue: PAXG (OCC national trust bank), XAUT (CNAD El Salvador, EME-0004), WTGOLD (NYDFS limited purpose trust) and MG999 (MAS capital markets services).

Everything else runs one of three patterns, and Aurumix should expect all three in diligence.

- **The software company.** The entity is registered for "development of software and applications", not financial services. ORO, Aurus, both Midas GoldZip entities and Libeara's holding company all do this.
- **What it pushes away.** Custody, KYC and redemption land on partners, or get performed unlicensed.
- **The adjacent licence.** Comtech's DAFZA bullion trade licence and Midas's MinLaw dealer registration are AML or trade registrations, presented as authorisation to issue tokens publicly. Comtech's display as expired.
- **The halo.** Kinesis calls a conditional CIMA approval regulatory status, but a CIMA register search returns no entity of that name.
- **The halo again.** Libeara's Standard Chartered link is venture equity two removes away, and the bank appears nowhere in the MG999 stack.

There is no cheap compliant door. Everyone who appears to have found a shortcut is unlicensed, licensed for something else, or subsidised by a parent holding a banking or trust charter.

The licence buys opacity rather than removing it. MG999 holds a genuine MAS licence and publishes less legally operative detail than smaller unlicensed issuers, because selling only to accredited investors removes the prospectus obligation.

### 2.8 "Audited" almost never means the gold was checked

The most reliable single tell in the sector. The published audit is a smart-contract audit, while the reserve attestation is absent, stale, or self-signed. Different work, different firms, and only one checks the gold exists.

| Protocol | What "audited" means there |
|---|---|
| Pleasing Gold | Beosin, staking contract only. No reserve attestation at all |
| Aurus | NonceBlox smart-contract audit. Proof of reserve announced but not live. Self-reported 73,398.5 g does not obviously reconcile to 43,322 tokens |
| ORO | Cantina and Adevar Labs, smart contracts. Reserve verification frequency stated three inconsistent ways, no document published |
| Comtech | Self-signed letters on company letterhead, last one 21 March 2025, showing reserves down 23%. No bar list, no smart-contract audit |
| WisdomTree | No bar list, no proof-of-reserve feed, no reserve attestation and no smart-contract audit |
| AZG | No contract audit, source not verified on-chain, no attestation |

The strongest is XAUT's ISAE 3000 (Revised) opinion from BDO Italia, and even there the custodian is unnamed and no bar list exists. Only DGLD, PAXG and VNXAU have credible independent reserve examination.

- **The VNX sting.** Its auditor states that the basis of a holder's property right is VNX's own internal holder register, then expressly refuses to opine on it.

The token is not the title. The register is. Aurumix needs to be clear which artefact carries legal ownership, and to have it examined by someone.

### 2.9 Distribution is the universal gap, and it is Aurumix's actual moat

No protocol here has a savings plan, a recurring purchase mechanism, or a retail referral programme. Not one of nineteen. Seven years perfecting custody, none spent on demand.

The one partial exception is instructive. Aurus pays its partner network from a fee pool:

- **The split.** 50% to ecosystem token holders, 25% to vault partners, 25% to provider partners.
- **Resellers get 0%.** They earn their own markup, plus bulk redemption and a graduation path upward.
- **Nothing pays for recruitment.** No commission, no override, no residual.

That is a merchant-margin supply chain, a structural answer to the MLM problem rather than a cosmetic one. It transfers directly:

- **Pay for function.** Recast the three agent tiers around capital committed, custody provided or servicing delivered, not recruitment depth.
- **Motivate with graduation.** Tier advancement rather than overrides retains top agents.
- **Add trailing commission.** Insurance-style, tied to continued contributions.

One caveat carries from Aurus. Its partner economics live in a whitepaper, the only legal document on its site names no entity and no governing law, and the split has changed three times. Copy the structure, not the paperwork.

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

> **The takeaway.** These are not tokenized gold protocols. They are what the Aurumix customer uses today, and each achieves distribution no tokenized gold protocol has matched, by embedding inside payment apps customers already open daily. None offers credit, dividend or inheritance.

| Platform | Model | Minimum | Credit against gold | Yield beyond gold price | Inheritance | Physical delivery |
|---|---|---|---|---|---|---|
| SafeGold | Digital claims on 24K, independent trustee, not a SEBI security. Powers PhonePe, Google Pay and Paytm | ~₹10 | No, separate NBFC pledge | No. Earns a 2–5% spread | No | Yes, cash, coins or jewellery |
| MMTC-PAMP | LBMA refiner, allocated and insured | ~₹9 via Paytm | No | No | No | Yes, coins and bars |
| Augmont | Digital gold with trustee oversight | ₹1,000/month | No | No | No | Yes, anytime |
| Jar | Round-ups and UPI autopay into 99.9% digital gold | ₹10/day | No | No | No | Yes, sell or convert |
| Gullak | Digital gold plus a "Gold+" leasing product | ₹100/day | No | Leasing yield | No | Yes |
