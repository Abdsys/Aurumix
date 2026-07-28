# Tokenized Gold: Market Research Summary

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

## 4. Live Protocol Profiles

Sixteen protocols are live. Five carry a full profile, each because it settles a question this design has to answer:

- **Tether Gold.** What the largest product in the category charges.
- **Pax Gold.** What a fully licensed issuer looks like.
- **Kinesis.** Whether an advertised yield survives its own arithmetic.
- **Streamex.** Whether gold-leasing income can be documented.
- **Comtech Gold.** What a Dubai issuer actually holds.

The remaining eleven follow in comparison tables carrying the same nine fields. Where a field records that something is not disclosed, that is the finding rather than a gap in the research.

### 4.1 Tether Gold (XAUT)

| Field | Detail |
|---|---|
| Issuer | TG Commodities, S.A. de C.V., El Salvador. |
| Licence covering the token | CNAD stablecoin issuer register EME-0004, 19 May 2025. |
| Assets under management | ~US$2.465bn, 612,823 XAU₮, July 2026. |
| Backing | 1 XAU₮ = 1 fine troy ounce, specified LBMA bar, Swiss vault. |
| Custody fee charged to holders | 0%, permanently. |
| Yield paid to holders | None. |
| Redemption | Physical only, Swiss address. Minimum ~430 XAU₮ (~US$1.73m). |
| Token standard | ERC-20, TRC-20, XAUt0 wrapper on seven further chains. |
| Reserve verification | Quarterly BDO Italia, ISAE 3000 (Revised), reasonable assurance. No bar list. |

#### What it is

Tether Gold is the largest tokenized gold product anywhere, roughly US$2.46bn and about 19 tonnes of metal behind the float.

#### Legal structure and regulatory standing

- **Holders are said to own the gold outright.** The reserves report states reserves "are owned by the XAU₮ token holders, not by the Company", with holders holding "undivided ownership rights to gold on specified gold bars".
- **The wording does not survive the arithmetic.** 611 bars of 12.5kg sit behind hundreds of thousands of tokens, so holders cannot each own a specified bar.
- **No trust deed, bailment or custody agreement is published**, and TG Commodities does not disclose which construct governs on insolvency.
- **EME-0004 is a stablecoin registration.** No securities or commodities regulator authorises the token, and the issuer holds no VARA, DFSA or ADGM licence.

#### Custody, fees and redemption

- **The custodian is never named.** Every primary document calls it "the Custodian". Secondary sources speculate Brink's or Loomis, and none confirms.
- **There is no bar list** anywhere: no serial numbers, no refiners, no per-bar assay.
- **The attestation is strong where it exists.** Reasonable assurance under ISAE 3000 (Revised), covering physical inventory, ledger-to-onchain reconciliation and quarterly sampled assay. BDO states its own limit: "The reporting date is limited to a point in time."
- **Storage costs holders 0.00%, permanently.** Buying costs 0.25% on a 50 XAU₮ minimum. Redeeming costs 0.25% plus logistics and insurance.
- **Two 0.25% touches cannot fund perpetual Swiss vaulting.** The arithmetic closes outside the fee table, on Tether group reserve income and affiliate inventory sold at a spread, though TG Commodities has never published a statement explaining what pays for free storage.
- **Redemption is where the ownership claim thins.** ~430 XAU₮, a Swiss address, full KYC, an unpublished excluded-country list, and export left to the holder.

> **Relevance to Aurumix.** The market leader charges nothing for storage because a group-level cross-subsidy pays for it, and Aurumix has no equivalent. Any custody fee therefore has to be justified by the savings wrapper, agent servicing and credit facility rather than by the vault.

- **A plain ERC-20 costs XAU₮ nothing**, because the token carries no tier, dividend or buyback right. Aurumix's ICS state breaks on an anonymous transfer, which means ERC-3643 and a cash buyback as the only exit.
- **XAUt0 is the warning.** Nothing discloses whether a holder on Solana or TON has the same claim on Swiss gold. Settle what a wrapped AURX holder owns first.
- **Match quarterly ISAE 3000 (Revised), then beat it** by naming a custodian and publishing a bar list. XAU₮ leaves both open.

### 4.2 Pax Gold (PAXG)

| Field | Detail |
|---|---|
| Issuer | Paxos Trust Company, National Association, New York. |
| Licence covering the token | OCC national trust bank charter, uninsured, 12 December 2025. |
| Assets under management | ~US$1.79bn, ~444,808 PAXG, 28 July 2026. |
| Backing | 1 PAXG = 1 fine troy ounce, serial-numbered LBMA bar, London. Allocated. |
| Custody fee charged to holders | 0% at present. Terms reserve a right to charge by dilution. |
| Yield paid to holders | None. |
| Redemption | USD, unallocated by wire, or physical at 430 PAXG per bar (~US$1.73m). |
| Token standard | ERC-20 on Ethereum, proxy pattern with freeze role. Solana via Token-2022. |
| Reserve verification | Monthly KPMG attestation. Per-address bar lookup. No full bar list. |

#### What it is

PAXG launched in September 2019 and is the second-largest tokenized gold product, a custody receipt with an onchain wrapper.

#### Legal structure and regulatory standing

- **Beneficial ownership, not legal title.** The terms state PAXG tokens "are akin to a warehouse receipt representing your beneficial ownership of a pro rata portion of Allocated Gold".
- **Bars are reallocable.** Paxos may move which bars back which holders "for operational efficiency", so a looked-up serial is real but not permanently the holder's.
- **Insolvency protection is documented asymmetrically.** The blog asserts "segregated, bankruptcy remote accounts"; the terms carry no Paxos-insolvency clause, only a Clearing Bank disclaimer.
- **Discretion is reserved in capitals**, including a right to freeze access without advance notice.

#### Custody, fees and redemption

- **Brink's operates the vaults**, named on the Paxos blog rather than in the terms. Paxos Trust Company, N.A. is the legal custodian.
- **Attestation is monthly** by KPMG LLP since February 2025 under AICPA standards.
- **A per-address lookup is not a bar list.** A holder verifies their own slice and cannot sum the pool.
- **Creation is tiered:** 0.02 PAXG flat below 2 PAXG, then 1.000% falling to 0.125% above 800. Destruction uses the same schedule, unwaived.
- **Storage is US$0.00.** US$2.00 per month applies after 12 months without issuance or redemption, and the contract's transfer fee, historically 0.02%, is understood to be set to zero.
- **The dilution clause is the fallback.** The terms provide that "Paxos may charge storage fees to all token holders by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens. The storage fee will be in line with industry practice, and such storage fee will be passed on to all PAXG token holders on a pro rata basis." Paxos reserved the right to break its own headline promise, disclosed it, and has never used it.

> **Relevance to Aurumix.** The dilution clause is the one genuinely transferable idea here, and firing it would break a one-token-one-ounce peg, which is why Paxos never has. For Aurumix, whose price is grams divided by tokens, the same mechanism is peg-neutral: mint to treasury, price per token falls by the fee, grams-to-tokens survives.

- **Adopt the mechanism, copy the disclosure discipline.** State the rate, state that it is charged by issuance, commit to advance notice.
- **PAXG pays no yield at US$1.79bn** and its gold sits unencumbered at Brink's. An OCC-supervised trust bank will not lend client metal, which leaves the ICS Dividend without a funding template.
- **PAXG trades at par on a live mint-and-redeem channel.** Aurumix's closed redemption is the only thing that could hold a premium.

### 4.3 Kinesis Money (KAU)

| Field | Detail |
|---|---|
| Issuer | Kinesis Cayman, a Cayman Islands exempted company. |
| Licence covering the token | None. CIMA VASP approval is conditional only. |
| Assets under management | ~US$310.2M, 2.386M KAU, 28 July 2026. |
| Backing | 1 KAU = 1 g allocated gold, held by Kinesis as bailee. |
| Custody fee charged to holders | 0%. |
| Yield paid to holders | Holder's Yield, 15% of the Master Fee Pool. Advertised 2.05%. |
| Redemption | Physical, 1,000 KAU per 1 kg bar, 0.45% plus US$100. |
| Token standard | Kinesis Blockchain Network, permissioned. ERC-20 wrapper on Ethereum. |
| Reserve verification | Bureau Veritas / Inspectorate, twice yearly. No bar list. |

#### What it is

Kinesis wraps a 1-gram allocated-gold token in a full monetary system: an exchange, a debit card, payroll, and a fee-sharing yield paid to holders, minters and referrers. Live since 2018, it is the closest running analogue to the ICS Dividend, with eight years of published payouts to check the arithmetic against.

#### Legal structure and regulatory standing

- **Title.** Clause 5.1.1 states that "legal and beneficial title in the Allocated Bullion backing the Kinesis Currency will remain with the Kinesis Currency holder."
- **Bailment.** Clause 4.1.2 has Kinesis storing bullion "as bailee on behalf of all holders", each with "an undivided interest in the total pool".
- **Cayman.** Kinesis's own Q4 2025 / Q1 2026 update says only that it "has received conditional approval" for a VASP licence from CIMA. A search of CIMA's register returns no entity of that name.
- **Australia.** AUSTRAC registrations DCE100865184-001 and IND100865184-001 are anti-money-laundering registrations, not financial-services licences.

#### Custody, fees and redemption

- **Vaults.** Brink's and Loomis, across London, New York, Zurich, Dubai, Singapore and Australia.
- **Attestation.** Bureau Veritas / Inspectorate International, twice yearly, in absolute grams. The 17 October 2025 count of 2,393,328.835 g reconciles closely against KAU circulating.
- **Gaps.** No bar list, no live proof-of-reserve feed, a six-month unverified window between counts, and no published smart-contract audit.
- **Fees.** Storage is free. Minting costs 0.45%, execution 0.22%, and sending KAU anywhere costs 0.45%. That transfer fee funds the yield.
- **Redemption.** Clause 8.1.1.1 permits redemption into allocated bullion at any time, at 1,000 KAU per 1 kg bar under 8.1.1.10, each request handled "on a case by case" basis.

> **Relevance to Aurumix.** Kinesis paid US$26,326 in Holder's Yield on gold in June 2026 against ~US$310M of assets, roughly 0.10% annualised against an advertised 2.05%, a gap of about 20x. An eight-year-old transactional platform pays a tenth of a percent, so a low-velocity SIP cannot fund 5% from recycled fees.

- **Split the instrument.** Kinesis kept KAU as the commodity and sold KVT separately as a capped 300,000-unit revenue share under an Offering Memorandum.
- **The wrapper strips the rights.** KMS Labs S.A. terms state ERC-20 holders "have no legal, equitable or beneficial right, title or interest in or to the Reserves", and receive no yield. Marketing does not draw that distinction, and if Aurumix wraps a permissioned base token it must.
- **The 0.45% transfer fee funds a payments product,** not a savings product.

### 4.4 Streamex (GLDY)

| Field | Detail |
|---|---|
| Issuer | Streamex Ltd., a Cayman Islands SPV formed February 2026. |
| Licence covering the token | None. Sold under Rule 506(c) of Regulation D. |
| Assets under management | ~US$12.84M, July 2026. |
| Backing | 1 GLDY = 1 fine troy ounce held by the SPV. May be unallocated. |
| Custody fee charged to holders | Not disclosed. Borne inside the SPV. |
| Yield paid to holders | "Up to 4%" advertised, 3.50% APY July 2026. Paid as scrip. |
| Redemption | 90 days' prior written notice, subject to "certain limitations". |
| Token standard | ERC-20 on Base, CCIP to Solana. Whitelisted, accredited only. |
| Reserve verification | EisnerAmper LLP examination, 31 March 2026. No bar list. |

#### What it is

GLDY is a gold-backed security token issued by a Cayman SPV under a Nasdaq-listed parent, paying yield sourced from third-party gold leasing through Monetary Metals.

#### Legal structure and regulatory standing

- **Holders own equity.** A GLDY holder owns "a non-voting digital share of Streamex Ltd.", a share in a Cayman company rather than title to metal or a trust interest.
- **The filed agreement is genuine.** Form 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1, the executed Tokenized Yield Partnership Agreement with Monetary Metals & Co.
- **It does not cover the lease.** Section 3.03 defers lease documentation to be "developed and mutually agreed" later, under New York law per Section 14.13. The exhibit omits security interest, title retention, risk-of-loss allocation and lessee default provisions.
- **The parent concedes the exposure.** The 10-K states holders "may face delays, partial recovery, or total loss".

#### Custody, fees and redemption

- **The custodian is unnamed,** described only as "an LBMA-accredited custodian". No vault, no city, gold may be unallocated, no bar list.
- **The 10-K concedes the link may be absent:** "there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars."
- **The attestation is real.** EisnerAmper examined management's assertion as of 31 March 2026: 3,064.674268 GLDY against 3,064.915910 fine troy ounces.
- **Two qualifications.** The parent held 98.5% of tokens at that date, and EisnerAmper became the parent's statutory auditor on 8 July 2026.
- **The yield is externally funded.** Article I defines a "Passing Lease" as one that "generates a net yield of at least three percent (3%) per annum after origination fees", and Section 3.01(b) lets Streamex reject any lease "in its absolute and sole discretion".

> **Relevance to Aurumix.** Three clauses are worth copying almost verbatim: the 3% net-after-origination-fees floor, the absolute discretion to reject a lease, and the insurance schedule. Schedule 1 requires a lessee-funded jeweller's block policy at 110% of lease value, plus a Monetary Metals-funded Lloyd's DIC/DIL layer at 110% covering "both mysterious disappearance and 'bad acts' by the lessee's management and owners".

- **The loss payee wording fails.** Both layers name Monetary Metals as loss payee "wherever possible", best efforts rather than a covenant. Neither names the SPV or the holders.
- **There is a live test.** The AgaBullion lessee defaulted on 26 January 2026 with Turkish seizure. Whether the Lloyd's layer paid has not been published.
- **Mind the buyer.** Streamex sells this at a $200,000 accredited minimum. Aurumix would sell comparable risk to a saver contributing $20 a month.

### 4.5 Comtech Gold (CGO)

| Field | Detail |
|---|---|
| Issuer | ComTech FZCO, Dubai Airport Free Zone. Parent Trade Fintech Ltd, DIFC. |
| Licence covering the token | None. Absent from the VARA, DFSA and ADGM FSRA registers. |
| Assets under management | ~US$5.04M, 28 July 2026. Last published reserve 111 kg. |
| Backing | 1 CGO = 1 g of 999.9 gold in 1 kg bars. Transguard, UAE. |
| Custody fee charged to holders | 0%, free for the first 24 months. |
| Yield paid to holders | None. |
| Redemption | Contractual minimum 1 kg (clause 8.1) at 0.50% plus making charges. |
| Token standard | XRC-20 on XDC. Not permissioned. |
| Reserve verification | Self-issued ComTech FZCO letters. Last dated 21 March 2025. |

#### What it is

Comtech Gold sells one gram of Dubai-vaulted gold per token on XDC, running a listed token and an app-based AED savings product off a single reserve, and at roughly $5.04M it has gone quiet.

#### Legal structure and regulatory standing

- **The issuing licence is DAFZA.** Licence 05069, issued to ComTech FZCO on 21 February 2022 for "gold and other precious metals trading". It is not a DMCC licence.
- **The DMCC licence is unrelated.** ComTech FZCO (DMCC) licence DMCC-889799 covers IT consultancy, network consultancy and software house activity only. Neither licence authorises public token issuance.
- **Both display as expired.** Comtech's own registration page shows DAFZA expiring 20 February 2024 and DMCC 25 June 2024.
- **The marketing says otherwise.** The FAQ states ComTech Gold "is regulated by Dubai Airport Free Zone Authority (DAFZA) and endorsed by local UAE government body DMCC". A free zone authority is a registrar.

#### Custody, fees and redemption

- **Transguard holds the metal,** though the storage clause permits holding "in the UAE or elsewhere" through affiliates "anywhere in the world".
- **Proof of reserve is self-signed.** Letters on ComTech FZCO letterhead, signed "For ComTech FZCO", no independent examiner named, no bar list.
- **The last letter is 21 March 2025.** It reports 111 kg, down from 144 kg after 62 kg of withdrawals, a 23% net decline left unexplained. Nothing published since.
- **Custody is free and the spread pays for it.** The site lists custody and insurance at "Nil", while the app returns ~1.0125% buy commission, ~0.9950% sell, and a round-trip spread near 1.8%. Nothing is deducted in grams.
- **The binding redemption minimum is 1 kg,** roughly $129,000 under clause 8.1. The advertised 10 g route is a discretionary retail service through partner jewellers.

> **Relevance to Aurumix.** Comtech issues a public gold token from Dubai on a bullion-trading licence and an IT consultancy licence, appears on no regulator's register, and tells retail customers in its FAQ that it is regulated by DAFZA. No public document establishes a Dubai gold-token route around VARA, only an authorisation nobody has obtained.

- **The fee mechanism does transfer.** Zero custody fee recovered through ~1% commission plus a ~1.8% spread, nothing deducted in grams, supports avoiding gram-denominated fees.
- **It only works if people transact.** A monthly SIP collects that margin once on the way in, then carries storage cost indefinitely. Comtech's 24-month carve-out shows transaction margin alone does not close the gap.
- **The proof-of-reserve bar is cheap to clear:** an independent attestation on a fixed cadence, a real bar list, and a clean separation between contract audit and reserve attestation.

### 4.6 The Remaining Eleven Live Protocols

Eleven further protocols are live, assessed against the same nine fields as the profiles above and ordered by assets. The three tables below split those fields so they fit the page.

Where a cell reads "not disclosed" or "none identified", that is the finding. The issuer publishes nothing on the point, and the silence is what a buyer should weigh.

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

## 6. Business Models and Revenue Patterns

### 6.1 How the category actually makes money

Almost none of these protocols makes money from the gold. They make it at the edges, on the way in and on the way out, or a parent company carries them.

- **Gate fees, the common shape.** PAXG runs a tiered mint and redeem schedule from about 1% down to 0.125%, XAUT a flat 0.25% each way, Aurus 0.5% to mint and 1.5% to burn.
- **Spread, the invisible alternative.** Roughly 1.8% at Comtech, about 0.76% two-way at Matrixdock, 2% to 5% at SafeGold in the adjacent Indian market.
- **Transfer and velocity fees.** 0.45% at Kinesis, 0.01% at Midas. Both only work if tokens move.
- **Management fees, once.** MG999 charges 1.00% a year, and it is also the only protocol here selling exclusively to accredited investors.

The gap is exactly what Aurumix needs most: a recurring charge that a dormant retail holder actually pays. Nobody here has solved it, because nobody here has retail savers to charge.

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

Redemption minimums are the number to watch, because they decide whether the redemption right is real:

- **PAXG and XAUT: a full bar.** London Good Delivery, roughly 430 ounces.
- **Comtech: 1 kg, about $129,000.** The advertised 10 g retail route is discretionary, not contractual.
- **Midas: 1 kg** against an average holding of 148 grams.
- **Kinesis: 100 g,** the outlier.
- **Aurumix: no physical redemption at all.** A deliberate choice for retention and credit revenue, and one to disclose plainly, because "you own physical gold" is the pitch every product here makes.

### 6.3 Which revenue models survive

Sort the sixteen live protocols by whether disclosed revenue covers disclosed costs and three tiers appear.

- **Structurally sound: PAXG, XAUT, XAUm, WTGOLD.** Each is cross-subsidised by a parent with a separate profitable business.
- **Dependent on churn: Kinesis, Aurus, Comtech, Midas.** Custody funded out of transaction velocity running far below what it needs. Aurus does about $211 a day after seven years, Comtech about $213 a day. Two of the four have reserved the right to start charging storage.
- **Unfunded outright: PGOLD and MG999.** PGOLD advertises 5% on $79M to $90M against a market trading under $20 a day. MG999 pays a 1.00% management fee plus platform, trustee, administration and audit costs out of a 2.5% gross lease.

A model where custody cost is real and recurring but revenue is event-driven does not survive. Every failure here died of that mismatch, and two live protocols have publicly conceded it.

### 6.4 What this means for the Aurumix fee design

Aurumix's peg is grams divided by tokens. Removing grams to pay for storage breaks the peg arithmetically, which rules out the obvious approach and leaves four options, not mutually exclusive.

- **Cash settlement from SIP inflow.** Accrue the charge daily, settle it out of the monthly contribution and at the gates. The nearest thing to a category norm for a product with recurring inflow, and the primary recommendation.
- **Dilution to treasury.** Mint tokens to the operator, lowering price per token while leaving grams divided by tokens untouched. Peg-neutral here, collects from holders who never log in, and OCC-supervised precedent exists for the drafting language.
- **Spread and gate fees, the Comtech model.** Recover custody through commission and spread, charge nothing ongoing. Comtech concedes this fails past 24 months for a buy-and-hold customer.
- **Cross-subsidy from credit and interchange.** The only genuinely external revenue in the model. At scale it can carry custody the way a parent carries it for PAXG.

> **The takeaway.** Custody fees are cost recovery, not revenue. Only the spread above true custodian cost is margin, and booking gross custody as profit would inflate any profit-linked distribution.

---

## 7. Token Design and Value Capture

### 7.1 The two architectures in use

Every protocol here sits on one of two designs.

- **Freely transferable.** A plain ERC-20, no token-level identity checks, compliance enforced at the venue. PAXG, XAUT, PGOLD, DGLD, Aurus and most of the long tail. Maximum composability, and the issuer does not know who its holders are.
- **Permissioned.** An on-chain identity registry with transfer restrictions, freeze and forced-transfer capability, ERC-3643 the standard. Mostly institutional issuers. Kinesis runs a permissioned Stellar fork, VNX a transfer-provider hook, Midas a contract-level transfer fee.

A common hybrid puts a permissioned base underneath an ERC-20 wrapper, keeping compliance while reaching decentralised venues. Aurumix has been considering exactly this shape.

### 7.2 The wrapper problem, which is worse than it looks

Wrapping a permissioned token into a plain ERC-20 strips the identity checks, transfer restrictions, freeze and forced-transfer controls. That much is understood. What this research found is that it can also strip the economic rights, and issuers do not always say so clearly.

- **Kinesis is the explicit case.** Its wrapper's terms state that holders have "no legal, equitable or beneficial right, title or interest in or to the Reserves" and receive no yield. Bridging a Kinesis token into its ERC-20 form silently removes both the claim on the gold and the income.
- **XAUT is the undisclosed case.** It runs a wrapper over a restricted base and does not say whether the wrapped holder has the same legal claim.

> **The takeaway.** If Aurumix ships a wrapper, the rights delta belongs in the wrapper's own terms at the point where a user wraps, not buried in the base document. Small drafting decision, large consumer-protection consequence, and no protocol in this set does it properly.

### 7.3 What the token is, legally

Three legal designs appear and they are not equivalent.

- **A contractual claim on the issuer.** The most common. The holder is an unsecured creditor, and if the company fails the holder queues with everyone else.
- **Co-ownership of the metal at law.** Rarer, DGLD the standout. Holders own the gold outright under Swiss co-ownership plus possession, and the terms disclaim any debt or equity claim. Six years of near-total dormancy harmed nobody.
- **A document of title.** Rarer still. WTGOLD sits under New York UCC Articles 1, 2 and 7, with no SEC registration, no transfer agent, ownership recorded on-chain only.

VNX exposes the trap underneath all three. Its auditor states that the basis of a holder's property right is VNX's own internal holder register, then refuses to opine on it. The token is a pointer; the register is the title.

Whatever Aurumix builds, name the document that carries legal ownership, hold it outside the operating company, and have an independent party examine it.

### 7.4 Proof of reserve as architecture, not a PDF

Best practice combines three layers and almost nobody runs all three.

- **Independent reserve attestation on a fixed schedule.** System-level assurance. Only DGLD, PAXG, VNXAU and XAUT have anything credible.
- **Oracle-based proof of reserve.** Custodian data on-chain, so contracts can compute collateralisation and halt minting below a threshold. Cache Gold integrated this. It is contract-enforceable rather than advisory.
- **User-facing allocation lookup.** Holder address mapped to bar serial numbers, purity and vault. PAXG runs one.

Treat proof of custody as a gate condition, not a disclosure: no confirmed allocation, no issuance. That is the difference between a claim about reserves and a constraint on them.

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

The protocols that pay income to a token do it through a second, separate token. Kinesis splits KAU from KVT, Aurus splits tGOLD from AWO, and that split is what keeps the gold token classifiable as a commodity claim.

---

## 8. Regulatory Positioning

### 8.1 The classification line, and where Aurumix crosses it

A token that is only a redeemable claim on fully-reserved gold is a commodity-type instrument, and in Dubai that is an ARVA under VARA. Attach a share of platform profit and it starts to look like a security or a collective investment in all three regimes that matter.

- **United States.** A company-run dividend meets all four Howey prongs. The Kraken staking settlement of February 2023, roughly $30M, and the June 2023 action against Coinbase staking both turned on that shape. Mechanical protocol rewards can fail the fourth prong; a company-set discretionary distribution does not.
- **European Union.** MiCA excludes instruments already treated as financial instruments under MiFID, so an income-bearing token resembling a fund unit falls under securities and fund law instead. Pooling plus a managed investment policy equals a collective investment undertaking.
- **UAE.** The 2025 security tokens and commodity token contracts regulation excludes plain virtual assets and non-security real-world assets, so an embedded profit share signals strongly the other way. VARA separately requires ARVA issuers to disclose what rights the token conveys.

> **The takeaway.** The current wording is the highest-risk possible formulation. "15% to 20% of operating profit, with 80% going to the top 10% of holders" reads as a fund distribution almost word for word.

### 8.2 The credit facility

Gold is low-volatility collateral, so a higher loan-to-value ratio than crypto lending is defensible. The constraints are hard ones.

- **Above 100% LTV lends more than the collateral is worth.** The corrected 90% to 95% ceiling sits above every benchmark here, but is at least inside the collateral.
- **Benchmarks sit far lower.** Indian NBFC gold loans are capped at 75% by the RBI, computed on principal plus interest at maturity for bullet-repayment loans. Crypto lenders run origination LTV well below the liquidation threshold, with a reserve or insurance fund absorbing shortfalls.
- **The existing thresholds no longer fit.** An 80% warning and 100% liquidation do not sit sensibly under a 90% to 95% ceiling. Re-space both, with an explicit loss-absorbing sink behind them.
- **India carries a structural block.** The RBI restricts lending against primary gold and against gold-backed instruments such as gold ETF and gold mutual fund units. That argues for a licensed country-layer partner rather than an on-chain facility run from Dubai.
- **The UAE needs a licence too.** Consumer lending there requires a finance company or lending licence, or a licensed partner.

### 8.3 The UAE routes that remain open

The idea that a Dubai free-zone trade licence offers a route around VARA does not hold. Comtech, the only Dubai-domiciled protocol here, issues on a DAFZA licence for precious metals trading, while its separate DMCC licence covers IT and software consultancy only. Neither authorises public token issuance, and both display as expired on Comtech's own site.

Three doors remain, all to be priced with counsel.

- **A VARA licence in Aurumix's own name.** Roughly AED 100,000 to apply, AED 200,000 a year in supervision, minimum capital of AED 1.5M or 2% of reserves, six to nine months or longer.
- **The VARA Sponsored Regime or Partnership Model.** Operate under an existing licensee, or outsource issuance to a Category 1 holder. Materially faster and cheaper, and worth quoting before assuming the standalone route.
- **ADGM.** The Accepted Spot Commodity route is worth investigating. One register lead exists, Universal Digital Intl Limited holding ADGM FSRA permission No. 250089 with CBUAE payment token registration, though that permission covers fiat-referenced tokens for professional clients. A lead, not a template.

### 8.4 What good disclosure looks like here

Three cheap practices separate the credible issuers.

- **Name the custodian.** XAUT has the strongest reserve attestation in the sector and still does not name its custodian.
- **Publish a bar list.** PAXG and DGLD do. Most do not.
- **Separate the audits in public.** Keep the smart-contract audit distinct from the reserve attestation rather than letting the word "audited" carry both. Six protocols here blur the two.

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

The tokenized gold protocols have no distribution. The Indian digital gold platforms have solved it completely, and their method is no secret: embed inside applications the customer already opens every day.

- **SafeGold rides the payment apps.** Gold purchase sits inside PhonePe, Google Pay and Paytm.
- **Jar attaches to UPI round-ups.** Saving happens without a decision.
- **Minimums of ₹9 to ₹10.** The last friction is gone.

Aurumix's agent network attacks the same problem through a different channel, and the Indian life insurance agency model behind it is a proven distribution machine. The design question is how to pay it without triggering the pyramid analysis.

### 9.3 Designing an agent network that is not an MLM

This is the highest-enforcement-risk area in the product, and the case law is unusually clear.

- **The Koscot and BurnLounge two-prong test.** Do participants pay for the right to sell and the right to earn from recruiting, with those rewards unrelated to sales to ultimate users? A genuine product does not save a scheme that fails it.
- **FTC v. Noland (2023).** Reaffirmed that what matters is whether commissions are funded by genuine, non-incidental product revenue rather than by payments for the right to participate.
- **The enforcement roll-call shares one profile.** Forsage (SEC 2022 and DOJ 2023, over $300M), BitConnect (2021, $2B), HyperFund (SEC 2024, $1.7B), Forcount (2022, $8.4M), Mining Capital Coin (2022). Every one combined pay-to-participate, no external revenue, recruitment-driven growth and risk-free-return marketing.

> **The takeaway.** Aurumix currently bundles all three risk factors: a profit-linked distribution, a lock-in, and multi-tier referral. That combination, not any single feature, is what has repeatedly drawn enforcement.

Two structural defences work together.

- **Pay for function, not for depth.** The Aurus structure directs 50% of the fee pool to ecosystem token holders, 25% to vault partners and 25% to provider partners. The reseller tier receives 0% of the pool, earning only its own markup, plus preferential bulk redemption and a graduation path.
- **Recast every tier around something performed.** Capital committed, custody provided, servicing delivered. Motivate top agents with graduation to a higher tier rather than overrides on a downline.
- **Tie trailing income to continued contributions.** Indian life agency commission is the model: renewal commission is payable only while the policy stays in force, so recruiting for its own sake stops paying. Pull the IRDAI (Payment of Commission) Regulations 2023 tables before quoting any figure.
- **Cap and subordinate the referral rewards.** Keep them below investment returns, substantiate every earnings claim, and pay from real platform fee revenue rather than from entry fees or new-investor money.

### 9.4 Inheritance

The Digital Will is a genuine differentiator and it is legally untested. Precedents are niche and scattered: Casa Inheritance, TrustVerse, Safe-based multisig legacy contracts, DigiPulse with its inactivity trigger, Sarcophagus, and exchange beneficiary programmes. All of them struggle with detecting death, verifying beneficiaries, and legal validity.

- **A smart contract is not a will.** In most jurisdictions probate law governs and the contract has no standing alone.
- **Every credible precedent treats the on-chain mechanism as facilitation.** A transfer layer alongside a legally valid will, never a replacement. The existing Aurumix positioning as a financial transfer instruction layer matches that and should be kept.
- **Build triggers around a nominated executor.** Run know-your-customer checks on beneficiaries, and make the "keep a real will as well" advisory explicit.

### 9.5 Secondary market structure

The redemption right is what anchors the price. Arbitrage between token, spot and derivatives is the balancing force, and it works only where an arbitrageur has a credible mint and redeem path to use. Aurumix's closed redemption removes it.

- **Treat AMM pools as a last-mile convenience layer.** Not the primary price discovery venue. Depth and net-asset-value anchoring come from issuance and redemption, identity-gated order books and periodic auctions.
- **Impermanent loss is a real problem here.** It bites hardest on a redeemable asset-backed token sitting in an AMM pool.
- **Size seed liquidity against genuinely free float.** Total supply minus locked, pledged and spot-restricted tokens. Model slippage so a single large seller cannot pull the secondary price off the gold floor beyond a set tolerance.

---

## 10. Gaps, Opportunities and Open Questions

### 10.1 What nobody in this market serves

Four gaps are consistent across all nineteen protocols.

- **The small recurring saver.** Redemption minimums of 430 ounces at PAXG and XAUT are absurd against a $20-a-month holding.
- **The holder who wants the gold to do something.** The well-documented protocols pay nothing, and the ones promising a yield cannot fund it.
- **The holder who wants protection rather than assurance.** No protocol names holders as an insurance loss payee or publishes a default waterfall.
- **The family.** No protocol offers inheritance or beneficiary nomination.

### 10.2 Where Aurumix can differentiate

Ranked by how cheap the differentiation is against how much it is worth.

- **Recurring savings distribution, first.** The moat. The gap is total and the adjacent Indian market proves the demand.
- **Holder-level protection in the documentation, second.** Trustee holding title, holder registry, burn-on-redemption, a published wind-down clause, holders named as insurance loss payee. Drafting decisions rather than capital commitments, and no competitor has done it.
- **Honest reserve verification, third.** Attestation on a fixed schedule, an oracle feed that can halt issuance, a bar-level lookup. Only three protocols have even the first done credibly.
- **Inheritance, fourth.** Legally untested, but nobody else offers it.

### 10.3 What this research does not yet establish

Three things are genuinely open, and none of them should be filled with an estimate.

**The retail versus institutional split of the tokenized gold market.** Available market data quotes totals only, and this research is protocol by protocol. Aurumix's redemption and identity model discourages institutional participation, so sizing against a substantially institutional total would overstate the addressable market.

This is not established. It is scoped work rather than a finding, and no growth model should rest on it until then.

**Whether a compliant funding route exists for Indian residents.** The business model routes Indian residents through USDT bought peer-to-peer or over-the-counter. Under the Foreign Exchange Management Act, purchasing crypto is not an established permitted purpose under the Liberalised Remittance Scheme, the RBI has never approved it, and Indian banks block it.

If that holds, a compliant funding route for an Indian resident may not exist, leaving non-resident Indians and other international customers. The charter's primary persona is an Indian resident life insurance policyholder.

This is not established. It is scoped work, it gates any break-even sizing, and it pulls the RBI and FEMA into a regulatory frame that currently names neither.

**Non-resident Indian savings behaviour.** No usable data was found on how the diaspora buys gold, what channels they use, or what friction stops them. This is not established, and given how central that segment is to the client's own thinking, it is scoped work.

---

## 11. Two Decisions for Aurumix

Everything above informs design work Tokenomics.net can carry. These two are choices the client owns.

### 11.1 The dividend: three options, and there is no fourth

Gold in a vault produces no income and costs money to store, so any distribution has to come from one of exactly three places.

- **Option 1: encumber the gold.** Lease the metal out and pay holders from the lease income. Streamex's SEC-filed agreement is a copyable template, with a 3% net floor and two insurance layers.
  - **The cost.** Aurumix gives up the claim that the gold is unencumbered, and inherits lessee credit risk. The AgaBullion default of 26 January 2026 shows what that looks like.
- **Option 2: fund it from operating profit.** The current design. Honest, and fundable.
  - **The cost.** It reads most clearly as a profit share, carrying classification risk: heavier capital, licensed venues only, possible restriction to qualified investors.
- **Option 3: drop the dividend.** Compete on the savings plan, the credit facility and inheritance.
  - **The cost.** Losing a headline feature. Every well-regulated protocol in this sector made that choice.

The arithmetic from other protocols is the persuasive material:

- **Kinesis.** About 0.10% realised against 2.05% advertised.
- **PGOLD.** 5% advertised on $79M to $90M, roughly $4M a year, against a market trading under $20 a day.
- **MG999.** A 2.5% gross lease funding a 1.00% management fee plus platform, trustee and audit costs, against 2.3% advertised net.

Our recommendation is option 3 at launch, with option 1 available later, once the credit book is real and counsel has ruled on holder protection under VARA or ADGM. That keeps the token classifiable as a commodity claim during licensing.

> **The takeaway.** This is a recommendation, not a verdict. The decision is the client's and it should be taken explicitly.

### 11.2 The premium: model it at zero

The current model assumes a 3% to 8% exchange premium, and the spot capacity parameter is tuned to produce it. That parameter runs 20% to 40% of monthly SIP inflow, split 80% internal and 20% external.

**Revenue projections should carry a zero premium assumption.** Nine protocols say the premium will not appear, and the two that trade off spot trade at a discount. The premium feeds the revenue model, so absorb this now.

- **Re-derive the spot capacity parameter.** Against growth in assets under management and lane fairness rather than premium engineering. A price above net asset value under closed redemption is an artefact of blocked arbitrage, not demand.
- **The "mining event" framing loses its last economic argument.** Keep the allocation mechanic and drop the mining metaphor, which implies an emissions story that invites the wrong regulatory reading.

---

## 12. Conclusions and Recommendations

### 12.1 The seven findings that matter most

1. **The category solved custody and never solved distribution.** Nineteen protocols, zero savings plans, zero recurring purchase mechanisms, zero retail referral programmes. The best-provenanced product, backed by a sovereign mint, reached $2.5M in four years.
2. **Vaulted gold cannot pay a yield.** Kinesis realised about 0.10% against 2.05% advertised; PGOLD promises $4M a year from a market trading under $20 a day.
3. **The premium is zero.** Arbitrage closes it in liquid markets and there is no market to express it in illiquid ones. Two protocols trade at a discount.
4. **A revenue line is a survival feature.** All three failures died of revenue starvation, not enforcement, hacks or reserve shortfalls.
5. **An anonymous bearer token cannot be wound down.** Cache Gold published a proper wind-down plan, followed it, and still stranded 96% of supply.
6. **There is no cheap compliant door.** Four of nineteen protocols hold a licence covering the token they issue, and the Dubai free-zone route does not exist.
7. **"Audited" almost never means the gold was checked.** Six protocols publish a smart-contract audit while their reserve attestation is absent, stale or self-signed.

### 12.2 What this market rewards and punishes

Rewards:

- **A legal claim that survives issuer failure.** DGLD demonstrated it across six dormant years.
- **Revenue that does not depend on customer activity.** The dormant holder still has to pay something.
- **Distribution embedded where the customer already is.** The Indian payment apps are the proof.
- **Reserve verification that names the custodian and publishes the bars.** Three protocols manage it.

Punishes:

- **Yield promises with no disclosed funding source.** Every one of them has been caught by its own arithmetic.
- **Redemption rights that differ from the marketing.** 10 g on the website, 1 kg in the binding terms.
- **Licences described as covering more than they cover.** Comtech is the live example.
- **Zero-fee models with no parent to carry them.** This is how Cache Gold died.

### 12.3 The main risks to watch

- **Classification.** The dividend plus the credit facility push the token toward a hybrid read, dragging in a second regulator. The single largest risk in the product.
- **Combination risk in distribution.** Profit share plus lock-in plus multi-tier referral is the exact pattern behind the largest enforcement actions in crypto.
- **SIP persistence.** The stoppage ratio in Indian mutual fund SIPs spiked above 120% in 2025, and the whole engine assumes contributions continue.
- **The funding route for Indian residents.** If the FEMA and LRS position holds, the charter's primary persona may have no compliant way to pay in.
- **Custody funding.** Every model the category uses is unavailable to Aurumix for structural reasons.

### 12.4 Recommended next steps

1. **Decide the dividend.** Three options, and it is a client decision. This gates the token architecture work.
2. **Re-derive the spot capacity parameter** against a zero premium, and carry that zero into all revenue projections.
3. **Commission the retail versus institutional split analysis** before any market sizing. It should not be estimated.
4. **Put the FEMA and Liberalised Remittance Scheme question to Indian counsel.** It gates eligible countries, payment rails, and whether the primary persona is reachable.
5. **Take the Streamex leasing documentation to Dubai counsel** as a worked example, asking whether the holder-protection layer Streamex omits can be built under VARA or ADGM.
6. **Price the VARA Sponsored Regime and Partnership Model** alongside a standalone licence.
7. **Re-space the credit facility thresholds** under the corrected 90% to 95% ceiling, and specify the loss-absorbing reserve behind them.
