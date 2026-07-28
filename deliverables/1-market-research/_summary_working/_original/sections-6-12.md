## 6. Business Models and Revenue Patterns

### 6.1 How the category actually makes money

Almost none of these protocols makes money from the gold. They make money at the edges, on the way in and on the way out, or they do not make money at all and are carried by a parent.

Four revenue shapes appear across the sixteen live protocols.

- **Gate fees.** A charge on minting, redemption, or both. PAXG runs a tiered mint and redeem schedule from about 1% down to 0.125%. XAUT charges a flat 0.25% each way. Aurus charges 0.5% to mint and 1.5% to burn. This is the most common model and the most honest one, because it charges for a service actually performed.
- **Spread.** The issuer sits between the customer and the metal and keeps the difference. Comtech runs roughly 1.8%, Matrixdock about 0.76% two-way, SafeGold in the adjacent Indian market runs 2% to 5%. Spread revenue is invisible to the customer, which is both its commercial appeal and its regulatory exposure.
- **Transfer and velocity fees.** Kinesis charges 0.45% on every transfer, Midas 0.01%. This only works if tokens move.
- **Management fees.** MG999 charges 1.00% a year. It is the only protocol in the set charging an explicit ongoing fee to holders, and notably it is also the only one selling exclusively to accredited investors.

The gap in that list is the thing Aurumix most needs: **a recurring charge that a dormant retail holder actually pays.** Nobody in this sector has solved it, because nobody in this sector has retail savers to charge.

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

**Redemption minimums are the number to watch**, because they determine whether the redemption right is real. PAXG and XAUT require a full London Good Delivery bar, roughly 430 ounces. Comtech's binding terms require 1 kg, about $129,000, with the advertised 10 g retail route discretionary rather than contractual. Midas requires 1 kg against an average holding of 148 grams. Kinesis is the outlier at 100 g.

Aurumix has no physical redemption at all, which is a deliberate design choice for retention and credit revenue. It should be made deliberately and disclosed plainly, because "you own physical gold" is the pitch every one of these products makes, and Aurumix will be compared against it.

### 6.3 Which revenue models survive

Sort the sixteen live protocols by whether their disclosed revenue can plausibly cover their disclosed costs, and a clean pattern appears.

**Structurally sound**: PAXG, XAUT, XAUm and WTGOLD. All four are cross-subsidised by a parent with a separate profitable business. None of them needs the gold token to pay for itself.

**Structurally dependent on churn**: Kinesis, Aurus, Comtech, Midas. All four fund custody out of transaction velocity, and all four have velocity far below what that requires. Aurus does about $211 a day after seven years. Comtech does about $213 a day of genuine decentralised exchange liquidity. Two of the four have already reserved the right to start charging storage.

**Unfunded**: PGOLD advertises 5% on $79M to $90M, roughly $4M a year, against redemption fees on rare redemptions plus a market trading under $20 a day. MG999 pays out of a 2.5% gross lease against a 1.00% management fee plus platform, trustee, administration and audit costs.

The lesson for Aurumix is direct. **A model where custody cost is real and recurring, but revenue is event-driven, does not survive.** Every failure in section 5 died of exactly that mismatch, and two of the live protocols have publicly conceded it.

### 6.4 What this means for the Aurumix fee design

Aurumix's peg is grams divided by tokens, so removing grams to pay for storage breaks the peg arithmetically. That constraint is real and it rules out the obvious approach. It leaves four workable options, and they are not mutually exclusive.

1. **Cash settlement from SIP inflow.** Accrue the custody charge daily, settle it in cash out of the monthly contribution and at entry and exit gates. This is the closest thing to a category norm for a product that has recurring inflow, and it is the primary recommendation.
2. **Dilution to treasury.** Mint tokens to the operator to cover storage, which lowers price per token and leaves grams divided by tokens untouched. This is peg-neutral for Aurumix specifically, it collects from holders who never log in, and there is now OCC-supervised precedent for the drafting language.
3. **Spread and gate fees**, the Comtech model: charge nothing ongoing, recover custody through commission and spread. Clean and simple, but Comtech itself concedes it fails past 24 months for buy-and-hold.
4. **Cross-subsidy from the credit book and interchange.** The credit facility and merchant interchange are the only genuinely external revenue streams in the Aurumix model. If they scale, they can carry custody the way a parent carries it for PAXG.

One accounting point matters more than it looks. **Custody fees are cost recovery, not revenue.** Only the spread above true custodian cost is margin. Booking gross custody as profit would inflate any profit-linked distribution and is the kind of thing an auditor or a regulator finds quickly.

---

## 7. Token Design and Value Capture

### 7.1 The two architectures in use

Every protocol in this research sits on one of two designs.

**Freely transferable.** A plain ERC-20 with no token-level identity checks, where compliance is enforced at the venue. PAXG, XAUT, PGOLD, DGLD, Aurus and most of the long tail work this way. It maximises composability and exchange listings. It also means the issuer does not know who its holders are.

**Permissioned.** An on-chain identity registry with transfer restrictions, freeze and forced-transfer capability. ERC-3643 and its relatives are the standard here, used mostly by institutional issuers of tokenized funds and bonds. Kinesis runs a permissioned Stellar fork, VNX uses a transfer-provider hook, Midas charges a transfer fee at the contract level.

A common hybrid puts a permissioned base underneath an ERC-20 wrapper, to keep compliance while reaching decentralised venues. Aurumix has been considering exactly this shape.

### 7.2 The wrapper problem, which is worse than it looks

Wrapping a permissioned token into a plain ERC-20 strips the identity checks, transfer restrictions, freeze and forced-transfer controls. That much is understood. What this research found is that **it can also strip the economic rights, and issuers do not always say so clearly.**

Kinesis is the explicit case. Its wrapper's terms state that holders have **"no legal, equitable or beneficial right, title or interest in or to the Reserves"** and receive no yield. So bridging a Kinesis token into its ERC-20 form silently removes both the claim on the gold and the income. XAUT runs a wrapper over a restricted base as well, and does not disclose whether the wrapped holder has the same legal claim.

If Aurumix ships a wrapper, **the rights delta has to be stated in the wrapper's own terms, at the point where a user wraps**, not buried in the base document. That is a small drafting decision with a large consumer-protection consequence, and it is unoccupied ground: no protocol in this set does it properly.

### 7.3 What the token is, legally

Three distinct legal designs appear, and they are not equivalent.

- **A contractual claim on the issuer.** The most common. The holder is an unsecured creditor of a company. If the company fails, the holder queues with everyone else.
- **Co-ownership of the metal at law.** DGLD is the standout: holders own the gold outright under Swiss co-ownership plus possession, with the terms expressly disclaiming any debt or equity claim. This is why six years of near-total dormancy harmed nobody.
- **A document of title.** WisdomTree's WTGOLD is an electronic document of title under New York UCC Articles 1, 2 and 7, with no SEC registration and no transfer agent, and ownership recorded on the blockchain exclusively.

VNX exposes the trap underneath all three. Its auditor states that the basis of a holder's property right is **VNX's own internal holder register**, then expressly refuses to opine on it. The token is a pointer. The register is the title. Whatever Aurumix builds, the document that carries legal ownership needs to be identified explicitly, held by someone other than the operating company, and examined by an independent party.

### 7.4 Proof of reserve as architecture, not a PDF

Best practice combines three layers, and almost nobody runs all three.

- **Independent reserve attestation** on a fixed schedule, giving system-level assurance. Only DGLD, PAXG, VNXAU and XAUT have anything credible here.
- **Oracle-based proof of reserve** feeding custodian data on-chain so that contracts can compute collateralisation and halt minting if reserves fall below a threshold. Cache Gold integrated this. It is contract-enforceable rather than advisory.
- **User-facing allocation lookup**, mapping a holder address to specific bar serial numbers, purity and vault. PAXG runs this.

Aurumix should treat proof of custody as a **gate condition** rather than a disclosure: no confirmed allocation, no issuance. That is enforceable in code, and it is the difference between a claim about reserves and a constraint on them.

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

The pattern worth noting: **the protocols that pay income to a token do it through a second, separate token**, not through the gold token. Kinesis splits the gold claim (KAU) from the fee-pool claim (KVT). Aurus splits tGOLD from AWO. That is the same structural instinct as delivering a reward at the account level rather than embedding it in the asset token, and it is the shape that keeps the gold token classifiable as a commodity claim.

---

## 8. Regulatory Positioning

### 8.1 The classification line, and where Aurumix crosses it

A token that is only a redeemable claim on fully-reserved gold is a commodity-type instrument, and in Dubai that is an ARVA under VARA. Attach a share of platform profit and it starts to look like a security or a collective investment. That is not a UAE quirk. It is consistent across the three regimes that matter.

- **United States.** The Howey analysis is met on all four prongs by a company-run dividend: investment of money, pooling into a common enterprise, an advertised expectation of profit, and profits derived from the operator's efforts. Enforcement in the Kraken staking settlement of February 2023, roughly $30M, and against Coinbase staking in June 2023 turned on exactly this shape. Purely mechanical protocol rewards can fail the fourth prong. A company-set, discretionary, profit-linked distribution does not.
- **European Union.** MiCA excludes instruments that are already financial instruments under MiFID, so an income-bearing token resembling a fund unit falls under securities and fund law rather than MiCA. Pooling plus managed investment policy equals a collective investment undertaking.
- **United Arab Emirates.** The 2025 security tokens and commodity token contracts regulation excludes plain virtual assets and non-security real-world assets, so an embedded profit share is a strong signal in the other direction. VARA separately requires ARVA issuers to disclose exactly what rights the token conveys.

The current Aurumix wording is the highest-risk possible formulation: **"15% to 20% of operating profit, with 80% going to the top 10% of holders"** reads as a fund distribution almost word for word. Section 11.1 sets out the three ways through.

### 8.2 The credit facility

Gold is low-volatility collateral, so a higher loan-to-value ratio than crypto lending is defensible. There are still two hard constraints.

**Above 100% LTV lends more than the collateral is worth.** The corrected Aurumix ceiling of 90% to 95% sits above every benchmark in the research but is at least inside the collateral. Indian NBFC gold loans are capped at 75% by the Reserve Bank of India, computed on principal plus interest at maturity for bullet-repayment loans. Crypto lenders run origination LTV far below the liquidation threshold, with a reserve or insurance fund absorbing shortfalls. Aurumix's existing 80% warning and 100% liquidation thresholds no longer sit sensibly under a 90% to 95% ceiling and need re-spacing, with an explicit loss-absorbing sink behind them.

**The India route has a structural block.** The RBI restricts lending against primary gold and against gold-backed financial instruments such as gold ETF and gold mutual fund units. That is a reason for the credit facility to sit with a licensed country-layer partner rather than being offered on-chain from Dubai.

Consumer lending in the UAE separately requires a finance company or lending licence, or a licensed partner.

### 8.3 The UAE routes that remain open

The idea that a Dubai free-zone trade licence offers a route around VARA does not hold. Comtech, the only Dubai-domiciled protocol in this research, issues on a DAFZA licence for precious metals trading, while its separate DMCC licence covers IT and software consultancy only. Neither authorises public token issuance, and both display as expired on Comtech's own site. What exists there is an unlicensed gap, not a lawful alternative.

That leaves three doors, and all three should be priced with counsel:

1. **A VARA licence in Aurumix's own name**, at roughly AED 100,000 to apply, AED 200,000 a year in supervision, minimum capital of AED 1.5M or 2% of reserves, and six to nine months or longer.
2. **The VARA Sponsored Regime or Partnership Model**, operating under an existing licensee or outsourcing issuance to a Category 1 holder. Materially faster and cheaper, and worth quoting before assuming option 1.
3. **ADGM**, where the Accepted Spot Commodity route is worth investigating. One live register lead exists: Universal Digital Intl Limited holds ADGM FSRA permission No. 250089 with CBUAE payment token registration, though that permission is scoped to fiat-referenced tokens for professional clients, so it is a lead rather than a template.

### 8.4 What good disclosure looks like here

Three practices distinguish the credible issuers from the rest, and each is cheap.

- **Naming the custodian.** XAUT has the strongest reserve attestation in the sector and still does not name its custodian.
- **Publishing a bar list.** PAXG and DGLD do. Most do not.
- **Separating the smart-contract audit from the reserve attestation in public communication**, rather than letting the word "audited" carry both. Six protocols in this research blur exactly that line.

---

## 9. Distribution, Stakeholders and Incentives

### 9.1 Who participates, and what each party wants

Across these protocols the same six roles recur, and the friction points are consistent.

- **Holders** want the gold to be there and to be able to get out. Their interests break from the issuer's the moment redemption is expensive or restricted.
- **The issuer** wants assets under management and a revenue line. Where those conflict, as with a redemption minimum that suppresses outflow, the issuer usually wins and the documentation rarely says so.
- **Custodians and vault operators** are paid per ounce per year regardless of protocol success, which makes them the one party in the stack with no exposure to failure.
- **Auditors and attestors**, where they exist, scope their opinion narrowly. VNX's auditor refusing to opine on the holder register is the clearest example.
- **Market makers and liquidity providers** anchor the price only where a credible mint and redeem right exists for them to arbitrage against.
- **Distribution partners**, which almost nobody has.

### 9.2 The distribution gap, and how the adjacent market fills it

The tokenized gold protocols have no distribution. The Indian digital gold platforms have solved it completely, and their method is not a secret: **they embed inside applications the customer already opens every day.** SafeGold powers gold purchase inside PhonePe, Google Pay and Paytm. Jar attaches to UPI round-ups so saving happens without a decision. Minimums are ₹9 to ₹10, which removes the last friction.

Aurumix's agent network is an attempt at the same problem through a different channel, and the Indian life insurance agency model it is based on is a proven distribution machine. The design question is how to pay it without triggering the pyramid analysis.

### 9.3 Designing an agent network that is not an MLM

This is the highest-enforcement-risk area in the whole product, and the case law is unusually clear.

The **Koscot and BurnLounge** two-prong test asks whether participants pay for the right to sell and the right to earn from recruiting, where those rewards are unrelated to sales to ultimate users. A genuine product does not save a scheme that fails this test. FTC staff guidance, reaffirmed in **FTC v. Noland (2023)**, holds that what matters is whether commissions are funded by genuine, non-incidental product revenue rather than by payments for the right to participate.

The enforcement roll-call shares one profile: Forsage (SEC 2022 and DOJ 2023, over $300M), BitConnect (2021, $2B), HyperFund (SEC 2024, $1.7B), Forcount (2022, $8.4M), Mining Capital Coin (2022). Every one combined pay-to-participate, no external revenue, recruitment-driven growth and risk-free-return marketing.

**Aurumix currently bundles all three of the risk factors**: a profit-linked distribution, a lock-in, and multi-tier referral. That combination, not any single feature, is what has repeatedly drawn enforcement.

Two structural defences are available, and they work together.

- **Pay for function, not for depth.** The Aurus model pays its reseller tier 0% of the fee pool. Resellers earn their own markup plus preferential bulk redemption and a graduation path. Recast each Aurumix tier so it is paid for something performed: capital committed, custody provided, servicing delivered. Use graduation to a higher tier rather than overrides on a downline to motivate top agents.
- **Tie trailing income to continued contributions**, as Indian life agency commission does. If renewal income only pays while the policy stays in force, recruiting for its own sake stops paying. Note that the IRDAI (Payment of Commission) Regulations 2023 percentage tables should be pulled directly before any specific figure is quoted.

Alongside both: cap referral rewards, keep them subordinate to investment returns, substantiate every earnings claim, and pay from real platform fee revenue tied to genuine savings activity rather than from entry fees or new-investor money.

### 9.4 Inheritance

The Digital Will is a genuine differentiator and it is legally untested. Precedents exist but are niche and heterogeneous: Casa Inheritance, TrustVerse, Safe-based multisig legacy contracts, DigiPulse with its inactivity trigger, Sarcophagus, and exchange beneficiary programmes. All of them struggle with the same three problems: detecting death, verifying beneficiaries, and legal validity.

In most jurisdictions a smart contract is not a recognised will, and probate law governs. Every credible precedent positions the on-chain mechanism as a facilitation and transfer layer alongside a legally valid will, never as a replacement. The existing Aurumix positioning, a financial transfer instruction layer rather than a legal will, matches precedent exactly and should be kept. Build the triggers around a nominated executor with know-your-customer checks on beneficiaries, and make the "keep a real will as well" advisory explicit.

### 9.5 Secondary market structure

Two structural lessons apply directly to the token launch.

**The redemption right is what anchors the price.** Arbitrage between token, spot and derivatives is the balancing force, and it only works if there is a credible mint and redeem path for an arbitrageur to use. Aurumix's closed redemption removes that mechanism, which is the reason the premium analysis in 2.1 lands where it does.

**Automated market maker pools should be a last-mile convenience layer, not the primary price discovery venue.** Depth and net-asset-value anchoring come from issuance and redemption, identity-gated order books and periodic auctions. Impermanent loss is a real problem for a redeemable asset-backed token in an AMM pool. Seed liquidity should be sized against the genuinely free float, meaning total supply minus locked, pledged and spot-restricted tokens, and slippage modelled so that a single large seller cannot disconnect the secondary price from the gold floor beyond a set tolerance.

---

## 10. Gaps, Opportunities and Open Questions

### 10.1 What nobody in this market serves

Four gaps are consistent across all nineteen protocols.

- **The small recurring saver.** Every protocol is built for a lump-sum buyer. Minimums are effectively set by gas costs and exchange listings, and the redemption minimums, 430 ounces at PAXG and XAUT, 1 kg at Comtech and Midas, are absurd against a retail holding. Nobody has built for someone putting in $20 a month.
- **The holder who wants the gold to do something.** The well-documented protocols pay nothing, and the ones that promise a yield cannot fund it. There is no product where a retail holder gets a defensible, documented return on vaulted gold.
- **The holder who wants protection rather than assurance.** No protocol names token holders as an insurance loss payee. None publishes a default waterfall. None commits to a trustee holding title plus a holder registry plus burn-on-redemption.
- **The family.** No protocol offers inheritance, beneficiary nomination, or any mechanism for the asset to pass on.

### 10.2 Where Aurumix can differentiate

Ranked by how cheap the differentiation is against how much it is worth.

1. **Recurring savings distribution.** The gap is total, the client already understands the channel, and the adjacent Indian market proves the demand. This is the moat.
2. **Holder-level protection in the documentation.** A trustee holding title, a holder registry, burn-on-redemption, a published wind-down clause with a reconciliation obligation, and holders named as insurance loss payee. Every element is a drafting decision rather than a capital commitment, and no competitor has done it.
3. **Honest reserve verification.** An independent reserve attestation on a fixed schedule, an oracle feed that can halt issuance, and a bar-level lookup. Only three protocols in the entire set have even the first of those done credibly.
4. **Inheritance.** Untested legally, but nobody else offers it and the target customer's whole frame of reference is life insurance.

### 10.3 What this research does not yet establish

Three things are genuinely open, and none of them should be filled with an estimate.

**The retail versus institutional split of the tokenized gold market.** The market data available quotes totals only, and this research is protocol by protocol. Aurumix's design actively discourages institutional participation through its redemption and identity model, so sizing against a total that is substantially institutional would overstate the addressable market. **This is scoped work, not a finding.** It needs a fresh piece of analysis before any growth model is built on it.

**Whether a compliant funding route exists for Indian residents.** The Aurumix business model routes Indian residents through USDT bought via peer-to-peer or over-the-counter channels, with the investor bearing tax disclosure. Under the Foreign Exchange Management Act, purchasing crypto is not an established permitted purpose under the Liberalised Remittance Scheme, the RBI has never approved it, and Indian banks block it. If that holds, **a compliant funding route for an Indian resident may not exist**, and the addressable base is non-resident Indians plus UAE residents plus other international customers. That matters because the primary customer persona in the project charter is an Indian resident life insurance policyholder. This question gates any break-even sizing work and pulls the RBI and FEMA into a regulatory frame that currently names neither.

**Non-resident Indian savings behaviour.** No usable data was found on how the diaspora buys gold, what channels they use, or what friction stops them. Given how central that segment is to the client's own thinking, it warrants a dedicated piece of work.

---

## 11. Two Decisions for Aurumix

Everything above informs design work that Tokenomics.net can carry. These two do not. They are choices the client owns, and both should be made before mechanism design goes further, because everything downstream is shaped by them.

### 11.1 The dividend: three options, and there is no fourth

The evidence in 2.3 is not an argument about whether the Aurumix dividend is well designed. It is arithmetic about what vaulted gold can pay.

Gold sitting in a vault produces no income and costs money to store. Any distribution to holders therefore has to come from one of exactly three places.

**Option 1: encumber the gold.** Lease the metal out and pay holders from the lease income. This is real, it is documented, and Streamex's SEC-filed agreement is a copyable template with a 3% net floor and two insurance layers. The costs are specific: Aurumix gives up the claim that the gold is 100% allocated and unencumbered, and it takes on lessee credit risk on the very asset backing the token. The AgaBullion default of 26 January 2026 shows what that looks like in practice, and no protocol anywhere has yet documented how a retail holder ranks when it happens.

**Option 2: fund it from operating profit.** This is the current design. It is honest and it is fundable. It is also the formulation that reads most clearly as a profit share, which is the securities classification risk described in 8.1, with the consequences being heavier capital, licensed venues only, and possible restriction to qualified investors. That fights the $20-a-month mass retail model directly. Structural mitigations exist, principally paying at the account level rather than as a token-embedded right and framing the payment as discretionary rather than promised, but they reduce the risk rather than remove it.

**Option 3: do not claim a dividend at launch.** Compete on the SIP, the credit facility and the inheritance features, which is where the genuine differentiation sits anyway. Every well-regulated protocol in this sector made this choice, including two that have far better access to bullion leasing than Aurumix will have.

**Our recommendation is option 3 for launch, with option 1 kept available for later**, once the credit book is real and counsel has ruled on whether a holder-protection layer can be built into a leasing structure under VARA or ADGM. That sequencing keeps the token classifiable as a commodity claim during the licensing process, which is when classification risk is most expensive, and it preserves the yield route as a future product rather than discarding it.

This is a recommendation, not a verdict. The decision is the client's and it should be taken explicitly.

### 11.2 The premium: model it at zero

The current model assumes a 3% to 8% exchange premium, and the spot capacity parameter, currently a 20% to 40% range of monthly SIP inflow split 80% to the internal lane and 20% external, **is tuned to produce it.** That parameter trades growth in assets under management against secondary market premium, and it is currently being traded against a return that the evidence says will not appear.

Nine protocols across the full liquidity spectrum say the same thing, and the mechanism is a pincer rather than a coincidence: liquid markets arbitrage a premium away, illiquid markets have no price to express one. The two protocols that do trade off spot trade at a **discount**.

This has a live consequence and it is cheaper to absorb now than once revenue modelling is underway. **Revenue projections should carry a zero premium assumption.** If Aurumix's closed redemption does produce a price above net asset value, that is an artefact of blocking arbitrage rather than evidence of demand, and it should be treated as an incidental outcome rather than a planned revenue line.

Two follow-on consequences. The spot capacity parameter should be re-derived against a different objective, most likely growth in assets under management and lane fairness rather than premium engineering. And the last economic argument for the "mining event" framing goes with it, which turns that into a purely presentational question. Our leaning is to keep the allocation mechanic and drop the mining metaphor, because it implies an emissions story that invites the wrong regulatory reading.

---

## 12. Conclusions and Recommendations

### 12.1 The seven findings that matter most

1. **The category solved custody and never solved distribution, and that is the opening.** Nineteen protocols, zero savings plans, zero recurring purchase mechanisms, zero retail referral programmes. The best-provenanced product in the sector, backed by a sovereign mint, reached $2.5M in four years. Aurumix's differentiation is not the gold, it is getting the gold to people who save monthly.
2. **Vaulted gold cannot pay a yield, and every protocol claiming otherwise fails its own arithmetic.** Kinesis realised about 0.10% against 2.05% advertised. PGOLD promises $4M a year from a market trading under $20 a day. The dividend is a choice between encumbering the metal, paying from profit, or not paying. Section 11.1.
3. **The premium is zero.** Arbitrage closes it where markets are liquid and there is no market to express it where they are not. Two protocols trade at a discount. The spot capacity parameter needs re-deriving. Section 11.2.
4. **A revenue line is a survival feature.** All three failures died of revenue starvation, not of enforcement, hacks or reserve shortfalls. A fee that only bites on transactions collects nothing from a saver, which is precisely how Cache Gold died. Aurumix's custody funding has to collect from a dormant holder.
5. **An anonymous bearer token cannot be wound down.** Cache Gold published a proper wind-down plan, followed it, and still stranded 96% of supply, because it had no registry to deliver notice to and never burned redeemed tokens. That is the strongest argument for a permissioned base, and it is stronger than any argument about which rights survive a transfer.
6. **There is no cheap compliant door, and the Dubai free-zone route does not exist.** Four of nineteen protocols hold a licence covering the token they issue. The rest use one of three patterns that will be recognised in diligence. VARA, the VARA Sponsored or Partnership regimes, or ADGM are what remain.
7. **"Audited" almost never means the gold was checked.** Six protocols publish a smart-contract audit while their reserve attestation is absent, stale or self-signed. Only three have credible independent reserve examination. Separating the two explicitly is free credibility.

### 12.2 What this market rewards and punishes

**Rewards:** a documented legal claim that survives the issuer failing, as DGLD demonstrated across six dormant years. A revenue line that does not depend on customer activity. Distribution embedded where the customer already is. Reserve verification that names the custodian and publishes the bars.

**Punishes:** yield promises that cannot be funded from disclosed sources. Redemption rights that exist in marketing at 10 g and in the binding terms at 1 kg. Licences described as covering more than they cover. Zero-fee models with no parent to carry them.

### 12.3 The main risks to watch

- **Classification.** The dividend plus the credit facility together push the token toward a hybrid read, which drags in a second regulator and fights the mass-retail model. This is the single largest risk in the product.
- **The combination risk in distribution.** Profit share plus lock-in plus multi-tier referral is the exact pattern behind the largest enforcement actions in crypto. Each element is defensible alone.
- **SIP persistence.** The stoppage ratio in Indian mutual fund SIPs spiked above 120% in 2025. The entire Aurumix engine assumes contributions continue.
- **The funding route for Indian residents.** If the FEMA and LRS position holds, the primary customer persona in the charter may not have a compliant way to pay in.
- **Custody funding.** Every model the category uses is unavailable to Aurumix for structural reasons, and two live protocols have already conceded that transaction-margin funding fails for buy-and-hold.

### 12.4 Recommended next steps

1. **Decide the dividend.** Section 11.1, three options, client decision. This gates the token architecture work and should be settled first.
2. **Re-derive the spot capacity parameter** against a zero premium, and carry a zero premium into all revenue projections.
3. **Commission the retail versus institutional split analysis** before any market sizing. It is not answered by this research and should not be estimated.
4. **Put the FEMA and Liberalised Remittance Scheme question to Indian counsel**, since it gates the eligible-countries and payment-rails questions and determines whether the charter's primary persona is reachable.
5. **Take the Streamex leasing documentation to Dubai counsel** as a worked example, with the specific question of whether the holder-protection layer that Streamex omits can be built under VARA or ADGM.
6. **Price the VARA Sponsored Regime and Partnership Model** alongside a standalone licence, rather than assuming the standalone route.
7. **Re-space the credit facility thresholds** under the corrected 90% to 95% ceiling, and specify the loss-absorbing reserve behind them.
