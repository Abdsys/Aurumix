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
