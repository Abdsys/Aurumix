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
