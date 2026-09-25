# Aurumix: Mechanism Design Document

## Gold-backed savings infrastructure under VARA

---

## How to read this document

This document describes the complete Aurumix mechanism design: what the product is, how every mechanism works, the legal structure it sits on, the assumptions each part rests on, and the questions that remain open for counsel. It is written so that a reader with no prior exposure to the project, including a lawyer instructed for the first time, can understand the entire product from this document alone.

Three conventions are used throughout.

- **Decisions are shown with their reasoning.** Where the design departs from the client's original specification (the 100 G Business Model), the departure is stated openly and the reason given.
- **Assumptions are labelled.** Where a mechanism rests on a reading of law that counsel has not yet confirmed, the assumption is stated as a proposition that is either true or false, with a confidence level where research supports one. Section 14 is the consolidated register. The companion document `Aurumix: Design Summary and Open Legal Questions` (19 August 2026) puts the seven highest-value questions to counsel directly; this document carries the design behind them.
- **Every legal statement in this document is a reading, not a ruling.** We are consultants, not lawyers. Where we quote a regulator's rulebook or a statute, the quote itself is accurate: we fetched the published text and copied it word for word, and the source texts are held in the project record. But what a rule means, and whether this design satisfies it, is a legal judgment that only qualified counsel can give, and on several points only the regulator, in writing, can settle. Nothing here is legal advice, and no legal position in this document should be treated as certain until counsel has confirmed it. The document is written so counsel's answers can change it cheaply.

## Table of contents

1. Introduction and market context
2. The underlying asset
3. Legal structure and regulatory frame
4. Token architecture
5. Buying gold: the SIP and the spot lane
6. The gold float and the treasury cycle
7. The exit: cash buyback
8. The Investor Conviction Score
9. The five benefits
10. Credit and the Gold Card
11. Family Portfolio and succession
12. Distribution: referrals and the agent network
13. Fees and revenue
14. Assumptions register and open legal questions
15. Risk and adversarial analysis

Appendix A: Glossary
References

---

## 1. Introduction and market context

### 1.1 The product

Aurumix is a gold-backed savings product, issued from Dubai under a VARA licence. 100% of every dollar received buys allocated physical gold, and one token equals one gram. A monthly savings plan starts at USD 20. Disciplined saving, never the amount saved, earns a rising ladder of benefits. Every customer can open a credit facility against their gold and a payment card; the ladder adds cheaper entry, better credit and card terms, rewards paid in grams, and discounts on family succession services.

### 1.2 The problem it solves

The target customer already saves in gold. South Asian households in the Gulf buy jewellery and coins as the default store of value, remit money monthly, and trust insurance-style premium schedules. What they cannot currently do is accumulate investment-grade gold in small monthly amounts, at wholesale pricing, with clean title, a credible exit, and services attached to the holding.

The existing routes each fail one test:

| Route | Where it fails |
|---|---|
| Jewellery | Making charges of 10 to 25%, resale haircuts, no title record, no services |
| Coins and small bars | High fabrication premium at retail sizes, storage burden, no liquidity commitment |
| Bank gold accounts | Usually unallocated: the customer is a creditor, not an owner |
| Existing gold tokens | Built for traders. PAXG's effective minimum is ~USD 120, XAUT's direct channel is 50 oz. None offers a savings plan |

Aurumix is built for the saver these routes fail: recurring contributions from USD 20, allocated metal, an independent title structure, a published buyback, and a benefits ladder that rewards the habit rather than the wallet.

### 1.3 Target customers and market perimeter

**The persona is the South Asian expatriate saver in the Gulf**: the person who holds a life-insurance policy, sends money home monthly, and thinks about gold in grams. The market research phase established that this population is broader than "the NRI": non-Indian South Asians (Bangladeshi, Pakistani, Sri Lankan, Nepali) match or outnumber Indians in parts of the Gulf, and the product design assumes the wider community.

The serviceable perimeter at launch is narrower than the population, because virtual-asset rules bind country by country. VARA supplies a test, not a list: serve customers where the activity is permissible, and meet the higher of the two regulatory standards where activity crosses borders.

| Tier | Countries | Position |
|---|---|---|
| Open at launch | UAE | The issuer's own jurisdiction. Roughly 3.5 million Indian residents alone, before other South Asian communities |
| Open, needs local authorisation | Oman, then Bahrain | Oman has no VASP regime in force (a gap, not a permission). Bahrain requires CBB approval, local capital and a locally licensed distributor |
| Effectively closed | Saudi Arabia, Kuwait, Qatar | Central bank restrictions on institutions processing virtual asset transactions. A banking problem, not a marketing one |
| Closed | India (residents) | Multiple independent bars. Section 14.4 and Appendix A of the legal brief |
| Reachable, each needs its own licence | UK, Singapore, Canada, Australia | Not launch markets |
| Excluded | United States, FATF blacklist jurisdictions | Deliberate |

Two consequences are worth stating early. First, the primary customer is the UAE-resident South Asian saver, with Oman as the first expansion market. Second, Indian residents cannot be onboarded, and the product carries an explicit blocked-country list rather than an implicit "anyone not named" default.

### 1.4 What the market does not offer

The market research phase examined nineteen tokenised-gold protocols plus the leading digital-gold and vaulting services. Three findings shape this design.

**The category is built for traders and treasuries.** Distribution to savers is unoccupied ground, and the one documented gold-token failure post-mortem (PMGT) names zero distribution as the cause of death.

**The category offers no behaviour-based benefits at all.** PAXG and XAUT carry no holder-level state by design. The only tiering anywhere in the set is by order size, which is capital: precisely the shape this design refuses.

**Tokens in this category die of revenue starvation, not regulation.** PMGT charged no fees and had no internal advocate. Digix zeroed its own fee and lived off its treasury until holders voted it away. The counter-example worth copying is DGLD, where holders own the gold outright at law, which is why six years of dormancy harmed nobody. Aurumix takes both lessons: real fee lines from day one, and customer ownership strong enough to survive the issuer.

### 1.5 Protocol overview

The design in one view:

- **Asset layer.** Allocated, serial-numbered gold bars from LBMA-accredited refiners, vaulted in Dubai, recorded bar by bar, owned through a DIFC trust structure for the benefit of token holders (section 3).
- **Token layer.** AURX, an open ERC-20 token (the standard, universally supported token format) with a blocklist, 1 token = 1 gram, identity verified at mint (the moment new tokens are created against new gold) and at redemption, freely transferable in between (section 4).
- **Purchase layer.** Two transaction types on one account: a monthly SIP from USD 20 and on-demand spot purchases. Money, then title, then token, on every purchase (section 5).
- **Treasury layer.** A gold float bridges retail ticket sizes to wholesale bar sizes and absorbs exit flow (section 6).
- **Exit.** Cash buyback at the next LBMA fix, no fee of any kind, by rule and by design (section 7).
- **Scoring layer.** The Investor Conviction Score measures saving behaviour, never amount, and prices five benefits (sections 8 and 9).
- **Credit layer.** One gold-secured revolving facility with a cash channel and a card channel, delivered through licensed partners (section 10).
- **Family layer.** A Family Portfolio and a standing Beneficiary Transfer Instruction, operating on custodied gold (section 11).
- **Distribution layer.** A single-level member referral programme and a contracted three-tier agent network (section 12).

---

## 2. The underlying asset

### 2.1 Asset specification

| Attribute | Specification |
|---|---|
| Metal | Gold, 99.99 fine |
| Form | Cast and minted bars, launch denomination 100 g, moving to 1 kg with scale |
| Source | LBMA-accredited refiners, with an accreditation covenant and a pre-authorised substitution clause |
| Custody | Allocated, serial-numbered bars in a Dubai vault, segregated from any Aurumix-owned metal |
| Record | Bar number, gross weight, assay and fine weight per bar, in a weight list per LBMA account practice |
| Pricing benchmark | The LBMA gold price (the "fix"), per gram |

Two precision points that recur through the document:

**"LBMA" means two different things.** An LBMA Good Delivery bar is a ~12.4 kg wholesale unit worth over a million dollars; Aurumix will not hold them at launch. A bar from an LBMA-accredited refiner is a 100 g or 1 kg bar freely available in Dubai. The accurate claim, used throughout: **99.99% gold from LBMA-accredited refiners, held in allocated bars.** UAE local refiners carry UAEGD accreditation, a separate voluntary standard, and are not automatically LBMA-accredited.

**Refiners can lose their accreditation.** Emirates Gold DMCC was suspended from both the UAEGD and LBMA lists in July 2023. If Aurumix relied on a single refiner with no right to swap bars, a suspension like that would break its core promise straight away. The sourcing covenant therefore uses multi-list wording (LBMA / DMCC / LPPM) so substitution on suspension is pre-authorised.

### 2.2 Denomination: 1 AURX = 1 gram, permanently

The token count is the gram count. This was changed from the client's 0.01 g specification, one of the items the client delegated.

- One number, not two. "7.820 AURX = 7.820 g" needs no explanation to a customer who already buys gold by the gram.
- The backing invariant reads directly off the two ledgers with no conversion factor, and a retail holder can verify it unaided.
- It matches every gram-denominated product in the comparable set (Comtech, Aurus, Digix, CACHE).
- Fractional purchases are a display question, not a denomination question. The ERC-20 standard's 18 decimals mean a USD 20 contribution buys a precise fraction of a token. Indian digital-gold products already display gram holdings to four decimals at mass scale.

The Indian convention of quoting gold per 10 grams is a price display convention. The app quotes per 10 g where the audience expects it; the token stays at 1 gram.

One consequence follows immediately: **the ratio is fixed, so nothing may ever erode the gram count.** Fee-by-dilution (the PAXG mechanism) and deduction of fees in grams are both excluded by construction. Savers are never charged for storage (section 13.3), and the governing customer promise is: you can lose your status, you can never lose your gold.

### 2.3 Pricing: one rule, three events

Every price in the product is struck the same way: **the price is always the next LBMA fix that nobody has seen yet.**

| Event | Priced at |
|---|---|
| Purchase (SIP or spot) | First fix after cleared funds |
| Exit | Next fix after the redemption request |
| Gold Rewards gram credit | Next fix after period close |

The reasoning is the removal of free options. Any rule that lets either side choose between two known prices hands that side a one-directional option on the gold price. Striking at the next unseen fix removes the option from both sides at once, and the same convention covers every price event in the product.

The published price formula in the client's document (`price = vault gold x fix / tokens outstanding`) is retained as a **verification identity**: it is what a holder uses to check that supply still equals metal. It is not the price definition. Under fixed weight, the price of one AURX is simply the fix per gram.

### 2.4 The premium: modelled at zero

The client's specification assumed AURX would trade at a 3 to 8% premium to the gold price, and built a scarcity mechanism to support it. Both are removed, on evidence:

- In a liquid market, arbitrage closes any premium: XAUT (~USD 2.5bn) and PAXG (~USD 1.8bn) both trade at the gold price.
- In an illiquid market there is no price in which to express a premium.
- The two protocols that restrict their exit the way the original design did (Midas XGZ, ORO) trade at a **discount**. Restricting arbitrage does not create a premium; it removes the price floor.
- Even if a premium existed, it would accrue to secondary-market sellers, not to Aurumix, and the exposure is one-directional: above net asset value holders sell to each other, below it they all redeem at once.
- A marketed premium gives a regulator an expectation of profit from the promoter's efforts, which contradicts the asset-referenced classification the whole structure depends on.

The scarcity layer (capped, time-boxed, oversubscribed "Mining Events") is deleted with it. A capped, priority-queued sale is offering-shaped and points at securities characteristics; continuous minting at net asset value against the buyer's own gold is commodity-purchase shaped and sits cleanly in the ARVA lane. What survives of the Mining Event is its real function, treasury batching, which becomes an internal procurement cycle (section 6).

### 2.5 Custody and the ownership record

Physical custody and legal ownership are two different problems, and the design separates them deliberately.

**Physical custody** is a vault contract: allocated, serial-numbered bars, segregated from Aurumix's own metal, with an independent assay on intake and a monthly Allocation Report publishing bar serials, assay certificates and both ledger balances. The recommended vault is Brink's Global Services DMCC, which has the useful property that the recommended lending partner already lends against gold held there (section 10.2).

**Legal ownership** runs through the structure in section 3. One honest disclosure belongs here because it shapes the marketing: a USD 75-a-month saver can never own a specific bar. After a year they hold under 1% of a kilobar. The accurate description of what a customer owns, used in every document, is an **individually recorded, pro-rata undivided interest in identified, serial-numbered bars**. "100% individually allocated" would overstate it; "not a pooled allocation" (the client's wording) overstates it too. The pool itself is allocated and customer-segregated; each customer owns a recorded share of it.

**The title record.** The preferred independent record is a DMCC Tradeflow warrant: an electronic record, maintained by DMCC as registrar, of which bars sit in which approved vault for which owner, transferable and pledgeable on the platform. Its honest limits: DMCC's own framework calls a warrant an electronic document of title, but that claim rests on DMCC's contract framework rather than a naming statute, and no court has tested it. The design therefore uses the warrant as one evidentiary layer among several, never as the foundation (section 3.5). Whether Tradeflow supports the sub-account structures Aurumix would want is an open commercial question for DMCC.
---

## 3. Legal structure and regulatory frame

One caution before the detail, repeated from the front of the document because it matters most here: the quotes below are word-for-word from the published rules, but the conclusions drawn from them are ours, and none has yet been confirmed by counsel or by the regulator. Where a conclusion is load-bearing, it reappears in section 14 as an open question.

### 3.1 The regulatory map

| Regulator | Covers, for Aurumix | Consequence |
|---|---|---|
| **VARA** (Dubai Virtual Assets Regulatory Authority) | Issuing AURX, the whitepaper, marketing, client money and client virtual assets | The core licence. VARA's remit covers the Emirate of Dubai including free zones, **excluding DIFC**, so the issuer cannot sit in DIFC |
| **CBUAE** (Central Bank) | Lending against pledged gold, card issuance, payment services, payment tokens | Both credit and card run through CBUAE-licensed partners. Aurumix builds neither |
| **DFSA** (DIFC) | The DIFC trust vehicle and its trustee, security over DIFC-law interests | The title-holding structure lives here, outside VARA's remit by design |
| **SCA** (federal securities) | Engaged only if a profit share is issued to holders | The design keeps it out of frame by keeping the profit-share dividend dead (section 9.5) |

### 3.2 The classification choice: direct-ownership ARVA

An ARVA (Asset-Referenced Virtual Asset) is VARA's category for a token backed by or linked to a real asset such as gold. VARA's issuance guidance uses gold as its worked example and splits gold-referenced tokens into two regimes. The choice between them determines the licence file, the capital requirement, the marketing story and most of the legal work.

| | **Option A: direct-ownership ARVA (chosen)** | Option B: stable-value ARVA |
|---|---|---|
| What the customer owns | The gold itself | A claim whose value tracks gold |
| Reserve Asset regime | **Does not apply.** Verified against the rule text: Annex 2 III.C opens "VASPs Licensed to issue ARVAs **which purport to maintain a stable value**...", so the regime attaches to the stable-value branch only | Applies in full: licensed custodians, segregation, no rehypothecation (the reserves may never be lent out or re-pledged), regular attestation, a supporting legal opinion |
| Capital | AED 1,500,000 minimum | AED 1,500,000 **or 2% of average Reserve Asset value over 24 months, whichever is higher**. At the Year 10 target that could approach USD 4M of locked capital |
| The binding burden | **Annex 2 III.B.1: prove the right of ownership is legally and validly established and that it transfers with the token** | Hold, segregate and attest the reserves |
| Fit with the product | The Individual Gold Receipt is this option | Silently deletes the Gold Receipt: a claim holder is a creditor |

Option A was chosen for three reasons in ascending order of force: it is the product the client believes they are building; it removes the heaviest ongoing compliance regime in the rulebook; and the capital arithmetic is worth several million dollars.

One further consequence confirmed at rule text: **redemption is optional for an ARVA.** All of Annex 2 III.E is conditional on its opening words ("To the extent an ARVA provides... a right of redemption"). Aurumix grants the right deliberately (section 7.1).

### 3.3 The licence stack

| Activity | Regulator and category | Build or partner |
|---|---|---|
| Issuing AURX | VARA, Category 1 VA Issuance. AED 100,000 application, AED 200,000 per year, AED 1.5M minimum capital | **Build.** The core licence |
| Whitepaper approval | VARA, per asset, published before any offering or marketing | Build. Mandatory |
| The buyback window | Inside the issuance licence via Annex 2 III.E. Whether a standing buyback additionally engages Exchange or Broker-Dealer activity is a counsel question | Counsel |
| Lending against pledged gold | **CBUAE.** Requires a bank or full finance company licence. The Restricted Licence category fails on its AED 20,000 per-borrower cap | **Partner.** Licensed lender is lender of record and owns the loan book |
| The Gold Card | **CBUAE**, Retail Payment Services and Card Schemes Regulation. Issuance requires scheme principal membership and RPSCS licensing | **Partner.** A licensed issuer of record holds the BIN; Aurumix is programme manager |
| Profit share to holders | Likely SCA and harder whitepaper approval | **Not issued.** Section 9.5 |

Two points on the partner licences, stated precisely because both would be noticed in a filing: the Restricted Licence route fails on the per-borrower cap, not on a collateral-lien exclusion; and "the CBUAE reserves the sole right to issue BINs" is unverified, with the binding constraints appearing to be scheme membership plus RPSCS licensing.

A separate CBUAE Non-Objection Registration is reportedly required for VARA licensees that custody, transfer or convert stablecoins (Confidence: Medium, commentary rather than rulebook). The design avoids touching stablecoins at all (section 13.4), which keeps this out of the critical path.

**Indicative cost to reach launch:** roughly USD 550,000 to 750,000 of capital and fees before any build cost, over six to nine months minimum. VARA publishes no approval timeline anywhere, so no date should ever be given to investors as anything firmer than an estimate.

### 3.4 The entity map

| # | Entity | Where | Why it exists |
|---|---|---|---|
| 1 | **Aurumix (issuer)** | Dubai, any free zone except DIFC | Holds the VARA licence and the customer relationship, receives all customer money, issues AURX, publishes the whitepaper, carries the capital |
| 2 | **Aurumix Technologies** | Any free zone, ordinary software licence | Builds and runs the app. Keeps software liability and IP off the licensed balance sheet |
| 3 | **Gold-holding vehicle** | DIFC | Holds legal title to the metal as trustee, outside Aurumix's estate. Section 3.5 |
| 4 | **Partners, not entities** | Contracts | Two-way bullion dealer, vault, independent assayer, lender of record, card issuer of record, issuer processor |

Two rules, both drawn from a documented failure in the comparable set (Comtech, whose customers pay into an account belonging to an entity that appears on no published licence):

- **The entity that receives customer cash must be the licensed entity.**
- **The entity named as issuer in the whitepaper must be the entity on the register.** No silent third names, ever.

### 3.5 The ownership construction

VARA requires Aurumix to prove two things (Annex 2 III.B.1): that the customer legally owns the gold, and that this ownership moves with the token. No single legal tool has been tested for this in a UAE court, so the design does not rely on one. It assumes that four separate layers, each of which says on its own that the customer owns the gold, together meet the requirement, and that if one layer is challenged the others still stand. Counsel is asked to confirm this assumption (section 14, Question 1).

#### 3.5.1 The layered claim

Four independent layers each assert that the customer owns the gold, so no single failure collapses the claim:

1. **Allocated, never unallocated.** Serial-numbered bars with a weight list. An unallocated holder is an unsecured creditor; an allocated holder owns property. This is the decisive layer.
2. **Trust language in the customer terms.** Legal title sits with the trustee for the benefit of holders, and the customer holds a beneficial interest: the trustee is the owner on paper, the customer is the person the gold is actually held for.
3. **The DIFC trust vehicle.** DIFC Trust Law 2018 Art 14(2): in plain terms, once assets are properly transferred into a trust, the transfer cannot be unwound just because the person who made it later goes bankrupt. This statutory protection is why the metal is held through DIFC rather than onshore: onshore UAE law could not give a verifiable answer to whether allocated but fungible gold can be reclaimed from a bankruptcy estate (the single most important open item in section 14).
4. **An independent title register** (the Tradeflow warrant, held by the vehicle), as evidence beyond Aurumix's own systems.

#### 3.5.2 The class-defined trust

**The problem.** The gold sits in a trust: the trustee (the DIFC vehicle) is the legal owner on paper and holds the gold for the customers. Under most trust law, when a beneficiary passes their interest to someone else, they must sign a written transfer. AURX is an open token that can move many times a day, often to people Aurumix has never met, so a signed document for every transfer is not workable.

**The answer: name the beneficiaries as a group.** The trust deed does not list customers by name. It says the gold is held for **whoever holds AURX at any given moment**, as shown on the token ledger.

- Receiving 5 AURX makes the receiver a beneficiary of 5 grams, automatically.
- Sending them on ends the sender's interest and starts the receiver's, automatically.
- Nobody signs or assigns anything. The membership of the group changes, as the deed says it will.
- The bars never move and never change owner. The trustee holds them on day one and on day ten thousand; only the list of people they are held for changes, and that list is the token ledger.

**Why DIFC law allows this.** Four provisions of the DIFC Trust Law 2018 make it work, each checked word for word against the statute text:

| What the design needs | Provision | What it allows |
|---|---|---|
| A group can be the beneficiary | Art 45(1)(b)(i); Art 34(2) | A class is valid if its members can be identified now or later. The token ledger identifies every holder at every moment |
| People can join and leave the group | Art 45(2); Art 48(4)(a) | The trust terms can add and remove members, and an interest can end when someone leaves the class |
| No signed transfer each time | Art 47(2): "**Subject to the terms of a trust**, a beneficiary may, by instrument in writing... deal with his interest" | The deed can switch off the written-transfer requirement. In English law (LPA 1925 s.53(1)(c)) it cannot be switched off; in DIFC law it can. This is why the vehicle sits in DIFC |
| No master list of holders | Art 66(1) | The trustee only has to give information to a beneficiary who asks in writing. It never has to keep a list of every holder |

**Why this meets VARA's requirement.** VARA's III.B.1.c asks the issuer to make sure every token transaction has a matching transaction in the gold. Here the token ledger *is* the ownership list, so the two can never disagree. That is a stronger answer than running two records and monitoring them for gaps. III.B.1.b only applies "**where**" moving the underlying asset needs a legal formality; here the bars never change owner and the change in beneficiary is governed by the deed, so there is no outside formality to meet.

**The caveat.** This is our reading of the law. No court has tested it and counsel has not yet confirmed it. It is Question 1 of the legal brief and the most important open point in the project. If counsel does not accept it, the token switches to the permissioned design in section 4.4.

**In one sentence:** the DIFC trust was chosen to protect customers' gold from Aurumix's creditors, and it is also what lets the token move freely, because gold that never changes owner never needs re-registering when the token changes hands.

#### 3.5.3 What the DIFC route costs

Holding the gold through a DIFC trust has four consequences:

- **The customer owns the gold beneficially, not legally.** The trustee is the legal owner. This is the normal position in the industry (Paxos describes PAXG the same way), but marketing must not say "you own the bar outright".
- **The vehicle could be tested as an investment fund.** A DIFC vehicle holding property for many people invites the Collective Investment Fund test. Our view (Confidence: Medium-High, for counsel) is that it does not qualify: the gold earns no income, is not actively managed, and each customer's share is fixed. This depends on the profit-share dividend staying removed (section 9.5). Bringing it back would bring the fund question back too.
- **The trustee may need a licence.** A single-purpose DIFC trustee company may be exempt from DFSA licensing when it acts for only one trust (Confidence: Medium, from a rulebook mirror, not yet verified). The answer changes the cost of the route.
- **ADGM cannot simply be swapped in.** Under an ADGM Foundation (Foundations Regulations 2017 s.29(1)), the foundation owns the assets outright, so the customer would own nothing until distribution. That defeats direct ownership. An ADGM trust has not been examined; any move to ADGM needs fresh analysis.

### 3.6 Client money and client assets

**Customer money.** Our reading of VARA's Client Money Rules (Company Rulebook Part IV) is that Aurumix can receive and hold customer money itself, with no separate central bank licence, as long as it follows these rules, which the design adopts in full:

- Customer money does not belong to Aurumix and stays out of its estate if it becomes insolvent.
- Money received reaches a designated Client Account within one calendar day.
- UAE customers' money is held with third-party banks in the UAE. Overseas customers' money can land abroad but must move to a UAE bank within 24 hours.
- The rule governs where the money sits and that it is kept separate. It does not set the currency: the main client account is in USD, with AED alongside.

**When the entry fee becomes Aurumix's money.** The rulebook leaves this to the licensee. The design sets it at **the moment title to the gold passes to the customer**. Before that, the customer is owed either the gold or all their money back. VARA excludes money "immediately due and payable to a VASP for its own account", and the fee is due once the service is delivered, which is when title passes. Loan repayments that arrive in the client account need a similar rule, which is not yet designed (section 14).

**Customer tokens.** Company Rulebook V.B.2 says customers' virtual assets "are not owned by the VASP and shall not form part of the VASP's estate" if it becomes insolvent. This protects the **token**. Physical gold is not a virtual asset, so the rule does not clearly protect the **metal**. That gap is why the gold is held through the DIFC trust (section 3.5). Whether VARA's rule reaches the metal at all is a question for counsel.

### 3.7 Redemption law

VARA's redemption rules are in Annex 2 (ARVA Rules), Part III.E of the Virtual Asset Issuance Rulebook (19 May 2025). The operative words, checked against the text:

| Rule | What it says | What it means for Aurumix |
|---|---|---|
| Opening words | Applies "to the extent an ARVA provides... a right of redemption" | Redemption is optional. Aurumix offers it by choice (section 7.1) |
| III.E.1 | Redeem "for an equal value" in AED, and in other forms disclosed in the whitepaper | Payout is always available in AED, with USD disclosed in the whitepaper as well |
| III.E.3 | Complete requests "within a reasonable period", provided the holder "or their designee, has successfully onboarded" | Settlement times are published and scale with size. A holder must be onboarded to redeem, not to hold |
| III.E.4 | Redeem "**without charging any fees**" | **No exit fee of any kind.** This removed a planned spot exit fee and reshaped how custody costs are recovered (section 13.3) |
| III.E.5 | Clear written policies and procedures | A written redemption policy is part of the licence application |

"Equal value" is not defined. The design takes the stricter reading: the customer receives the full market value, with no deduction for the dealer's lower buying price. Counsel is asked to confirm this (Question 3). The difference, on every exit, is the dealer's full buy-sell spread.

### 3.8 The wind-down plan

VARA requires a wind-down plan **at all times** (Company Rulebook Part VII.A), with twelve required contents. Two rules matter most for the design:

- Completing the plan must not depend on selling customers' money or assets (Rule 1.k).
- VARA keeps powers to step in over customer assets (Rule 1.l).

Because customers own their gold directly, it is not Aurumix's to sell, so Rule 1.k can actually be met. For an open token, the steps a liquidator can run are a published claim window, burning tokens as they are redeemed, and freezing transfers. Aurumix also has an advantage the comparable products lack: most direct customers pay monthly, so they can be contacted. The plan must be written anyway, and publishing it costs nothing extra.

### 3.9 Marketing and transfer rules

- **Travel Rule threshold: AED 3,500** (the client's specification says USD 1,000). Above it, sender and receiver details must be collected and held before the transfer. Details travel with every transfer whatever its size, and transfers are added up per day. It applies to transfers Aurumix sends or receives, including withdrawals to and deposits from private wallets. Wallet-to-wallet transfers between private holders involve no VASP and fall outside it.
- **Marketing (Marketing Regulation I.C.2):** no urgency or fear-of-missing-out messaging. Incentives must run for a reasonable period and **need a compliance confirmation from VARA** (I.C.2.l(iii)), which puts the referral programme on the licensing timeline (section 12.6). Aurumix is liable for claims made by anyone marketing on its behalf.
- **No return language.** Gold Rewards is a capped fee rebate. It is never called yield, interest, return or dividend (section 9.5). The premium is never marketed (section 2.4).

> **Open for counsel in this section:** whether title really moves with the token (Question 1), whether the gold survives an onshore insolvency (Question 2), what "redemption" and "equal value" mean (Question 3), and whether the vehicle is a fund and its trustee needs a licence (Question 4). Section 14 carries all of them in full.
---

## 4. Token architecture

### 4.1 What AURX is

| Attribute | Specification |
|---|---|
| Standard | **Open ERC-20**, the standard token format every wallet and exchange already understands, behind an upgradeable proxy with a transfer-hook stub (an engineering choice that lets transfer rules be changed later without rebuilding the token) |
| Transfer control | **Blocklist**, denying by exception (sanctions, court order, fraud). Not an allowlist |
| Control roles | Freeze, seize and reissue, held by the issuer. The price of the licence, and the precedent (PAXG) pays it too |
| Identity | KYC (know-your-customer identity verification) is a hard precondition of the mint and of redemption. No identity requirement between the two |
| Peg | 1 AURX = 1 gram, permanently (section 2.2) |
| Supply | Uncapped. Supply is a consequence of purchases; tokens exist only against allocated grams |

The architecture in one line: **identity at the two doors, freedom in the room.** It is the same split PAXG, XAUT and Backed Finance operate, and it is what Annex 2 III.E.3 was drafted to permit.

Two rules for building the token contract:

- **Build it so it can be switched to permissioned later.** The token sits behind an upgradeable proxy with a transfer hook, a small piece of code that checks every transfer. At launch the hook only applies the blocklist. If counsel does not accept the class-defined trust, the same hook is switched to an allowlist, so only registered holders can hold AURX. The token standard therefore does not have to be settled before the build; it can follow counsel's answer.
- **Ship the blocklist either way.** It is less code than an allowlist and still gives the issuer the controls it needs (freeze, seize and reissue). A token with no controls at all cannot be wound down properly: Cache Gold published a wind-down plan, followed it, and still left 96% of its supply stranded.

### 4.2 Identity at the two doors

| Layer | What happens | Who must be identified |
|---|---|---|
| Mint | Fiat in, KYC complete, gold allocated to the trust, tokens issued to a verified address | Everyone. A hard precondition (section 5.2) |
| Hold and transfer | Plain ERC-20 transfers. Any wallet, subject to the blocklist | Nobody |
| Redeem | Tokens burned, cash paid to a name-matched bank account | Everyone. Annex 2 III.E.3 makes onboarding a rule precondition of redemption |

The middle row is what makes AURX an open token: once minted, it can move to any wallet with no identity check. This has one consequence for Aurumix's services. **The account features can only see gold held in the Aurumix account.** ICS Retention, the credit pledge, the Family Portfolio and the Beneficiary Transfer Instruction all work from the account and cannot see tokens sitting in an outside wallet. So when a customer withdraws AURX to their own wallet, those grams count as sold for ICS scoring (section 8) and leave the family features (section 11.2). In the customer's words: your gold is yours to take out whenever you want, and the account features work on the gold you keep with us.

### 4.3 How ownership moves with the token

Covered structurally in section 3.5.2. The token-layer consequence: a peer transfer needs no register write, no counterparty check and no whitelist for ownership to follow it, because the trust's beneficiary class is defined by the ledger itself. The invariant the build enforces is:

```
trust gold holdings (grams)  >=  AURX outstanding
```

checked continuously, published monthly, with minting halted automatically if the invariant is at risk, if custodian attestation lapses, or if the vault position cannot be confirmed.

### 4.4 The fallback and the wrapper trap

**Fallback (if counsel rejects the class-defined trust):** flip the transfer hook to an allowlist. The token becomes permissioned, every holder is registered, transfers write to a named register, and the open-listing strategy is foreclosed. Buildable, more expensive, and the reason the proxy ships from day one. The legal brief asks counsel to say which limb fails, because the fallback differs by limb.

**Never built, under either answer: a permissioned base token with an open wrapper.** Inside a wrapper the registered holder is the wrapper contract, so the person holding the wrapped token owns no gold. The comparable set contains exactly this failure: on one venue the issuer's terms grant holders title, on that issuer's own wrapped version a separate company's terms grant "no legal, equitable or beneficial right, title or interest" in the reserves, with the difference invisible unless both documents are read. If a wrapper is ever issued, its own terms must state what the wrapper holder does and does not own.

### 4.5 What a transfer is

- A transfer moves the beneficial interest with the token (section 3.5.2). It is not a redemption, so the no-fee rule does not touch it.
- ICS state does not transfer: the score attaches to the verified identity of the account holder (section 8.7). Received grams start their own credit-seasoning clock (section 10.3).
- Pledged grams sit in platform custody under a registered security interest and cannot be withdrawn or transferred until the charge is released (section 10.5).
- Blocked addresses cannot send or receive; frozen balances can be seized and reissued under the disclosed control framework. These powers exist for sanctions, court orders and fraud, and their scope is disclosed in the whitepaper.

> **Open for counsel in this section:** the whole token architecture rides on Question 1. Until counsel confirms the trust construction, the token is built capable of both answers and committed to neither.

---

## 5. Buying gold: the SIP and the spot lane

### 5.1 One account, two ways to buy

A customer has one account and can buy gold in two ways: a monthly savings plan (SIP) or a one-off spot purchase.

| | SIP contribution | Spot purchase |
|---|---|---|
| Trigger | A monthly schedule the customer sets | An order placed any time |
| Amount | Can change every month. Minimum USD 20, target USD 75, no maximum | Any amount above the minimum |
| Earns ICS | **Yes** | **No** |
| Entry fee | Base rate, less the account's tier discount | Base rate, less **the same tier discount** |
| Counted in Retention (gold kept versus sold) | Yes | Yes, because grams are not tagged by how they were bought |
| The gold | Identical | Identical |

Three rules settle every boundary question:

- **Earning and using the tier are separate.** Only SIP contributions earn the tier. Once earned, the tier belongs to the account and applies to everything it does: every purchase price, credit, the card and the family services.
- **Extra money within a month counts as a spot purchase.** It buys gold but does not add a month to the score, so twelve payments in January cannot become twelve months of history.
- **The gold is the same either way.** Only prices and services differ. No gram is ever labelled SIP or spot.

**Why spot purchases also get the tier discount.** Two reasons:

1. **Aurumix could not tell them apart anyway.** The SIP amount can change every month and has no maximum, so any spot purchase could simply be paid as a bigger SIP contribution instead.
2. **A discount on the price cannot be abused.** A customer who buys at a discount and immediately sells back still pays the entry fee, so they always lose money on the round trip, at every tier.

Benefits that pay out (Gold Rewards) or improve borrowing terms are different: they could be gamed by large one-off purchases, so spot purchases do not earn them.

### 5.2 Step zero: identity checks

Nothing happens until the customer is verified. If money arrives before verification is complete, it waits in the Client Account and no gold is bought.

| # | Step | Output |
|---|---|---|
| 0.1 | Account opened; **country of residence** recorded | Residence, not passport, decides eligibility |
| 0.2 | KYC, sanctions and PEP (politically exposed person) screening | Pass, refer or reject |
| 0.3 | Eligibility check against the country list | Accept, or decline with a reason |
| 0.4 | Wallet created | The address can receive newly minted AURX |
| 0.5 | Bank account registered and **name-matched to the customer** | The customer's funding account |
| 0.6 | Terms accepted, including the trust and standing instructions | The contractual half of ownership |

Step 0.5 matters most: the whole payment design rests on one test, **whose bank account sends the money** (section 13.4). A payment from any other account is rejected.

### 5.3 The nine stages of a purchase

SIP and spot follow the same nine stages; only stage 1 differs. The order is always **money, then title, then token**: if the gold cannot be put in the customer's name, no token is created.

| # | Stage | Timing | What happens |
|---|---|---|---|
| 1 | Instruction | T | SIP: the contribution date arrives. Spot: an order is placed |
| 2 | Collection | T to T+1 | The customer pays on a push rail (section 5.4) |
| 3 | Client Account | within 1 calendar day | Money lands in the Client Account. It is still the customer's money |
| 4 | Price struck | first LBMA fix after the money clears | The public benchmark price; neither side chooses it |
| 5 | Grams calculated | same moment | (Payment less entry fee) / price per gram |
| 6 | **Title transferred** | same day | Grams from the float are allocated to the customer under the trust |
| 7 | **Tokens minted** | same day | 1 AURX per gram, sent to the customer's verified wallet |
| 8 | Money settles | same day | The metal cost goes to the dealer; the fee moves to Aurumix's own account (section 3.6) |
| 9 | Records | same day | Gold Receipt updated, ICS month recorded (SIP only), float use logged |

Aurumix then refills the float in the background (section 6); the customer never sees this. Target: stages 1 to 9 within 24 hours of the money clearing. The only published benchmark in the category is T+3.

**The disclosed fee and Aurumix's margin are different numbers.** On a USD 75 contribution at launch, the fee shown to the customer is 5% (USD 3.75). Aurumix keeps less than that, because the cost of making small bars comes out of it. The whitepaper discloses the fee; the budget models the margin (section 13.2).

### 5.4 Payment rails: the customer pushes the payment

At launch, the customer always sends the payment. Aurumix never pulls money from their account.

| Rail | What the customer does | If they do not pay | Role |
|---|---|---|---|
| **AANI Request to Pay** | One tap a month in their own banking app | Nothing happens. The request expires; no fee, nothing bounces | **Default.** AANI is the UAE instant-payment system, run by a CBUAE subsidiary and built on the same technology as India's UPI, so customers already know how it works |
| **Prefunded balance** | One transfer covering several months, drawn each month | A draw against an empty balance is simply a missed month | The real "set and forget" option, offered at signup ("fund three months at once"). The unused balance is client money, refundable, and each draw is priced at that month's fix |
| AANI electronic direct debit | Nothing | To be assessed when it goes live | Planned; announced but not yet live |

Using push payments avoids three problems: no mandates to manage, no bank charges when a payment fails, and no dependence on direct-debit support for variable amounts, which is unconfirmed. Marketing rule: say "one tap a month" for Request to Pay, and promise "set and forget" only for the prefunded balance until direct debit is live.

Four SIP payment rules:

- **USD 20 is a hard minimum.** A smaller payment is returned, never partly credited. The minimum holds as long as each collection costs about USD 0.25 or less, which the Request to Pay contract must confirm (section 14.6). At that cost a payment covers its own cost from about USD 11. At the higher prices found in research, it would take about USD 66, and the minimum would need revisiting.
- **The grace period is 5 calendar days** from the contribution date, and never ends on a weekend or public holiday. Insurance products use 15 days because failed debits take time to recover; a push payment has no such delay, so grace only covers being busy or away.
- **A failed payment and a skipped payment are tracked separately.** The system logs whether each request was delivered and opened, so "never saw it" and "chose not to pay" can be told apart. Published benchmarks put accidental churn at 20 to 40% of subscription churn, and the design keeps it from being read as a decision.
- **Lowering the amount is free, instant and never affects the score.** Otherwise the customer's only alternative is to stop.

**Customers abroad.** Overseas savers pay into local collection accounts run by multi-country providers, and the money moves to a UAE bank within 24 hours as the client-money rules require. Whether these providers (usually e-money firms, not banks) meet VARA's "third-party banks" wording is a question for counsel (legal brief, Question 6). If they do not, cross-border collection does not work.

### 5.5 The SIP rules: definitions and account states

**Definitions:**

| Term | Definition |
|---|---|
| Period | A **calendar month**. Changing the payment date can never create or remove a period |
| Contribution date | The day of the month the customer chooses. A convenience for collection only |
| Counted period | A month with at least one accepted payment of USD 20 or more, on time or within grace. One per month at most; the amount above USD 20 does not matter |
| Confirmed SIP | **Six counted periods in a row.** This opens the score (section 8.2) and is permanent once reached |
| Declared amount | The amount on this month's payment request. Can change, is never scored, and is not a promise |

**The product minimum (USD 20) is the only minimum.** Customers cannot set their own higher floor.

**When a payment is missed:** nothing happens to the gold, ever. The only effect is on the score (section 8.5). A missed month stays missed: there is no catching up on past months. Money that arrives after the grace period is offered as a spot purchase on the same screen. Because there is no lock-in contract, a missed month breaks no promise and there is nothing to revive. It also means nobody can time a late payment to benefit from a lower past gold price.

**The three account states.** None of them needs a request or a review:

| State | Trigger | What happens |
|---|---|---|
| **Regulatory block** | Compliance blocks the account (for example, the customer becomes resident in India) | An automatic system event. **Months in which Aurumix cannot accept the customer's money do not count against them**: the score is frozen, the gold is kept, Confirmed SIP is kept, and existing credit runs to term with no new draws. This also applies before Confirmed SIP: a saver at 4 of 6 resumes at 4 of 6. If compliance forces a sale, the grams leave and the score does not change (section 8.3) |
| **Stop** | The customer cancels | Nothing is lost. The gold stays, the score fades on its own schedule, and a restart picks up from wherever it has faded to |
| **Dormant** | 12 silent months in a row | Housekeeping only: payment requests stop, the SIP closes, and the account can hold but not collect. A spot purchase is still allowed and is the natural way back in |

There is no "pause" option. A free pause would be used by every customer about to miss a payment, and the score effect of one miss is already mild.

### 5.6 The spot lane and large purchases

A spot purchase follows the same nine stages; stage 1 is an order. There is no mandate, so nothing can bounce. Spot purchases earn no score, so they earn no tier and no tier benefits. Credit and the card are still open to a spot-only account at base terms. Spot purchases do get the account's entry-fee discount (section 5.1).

Large purchases matter to the treasury and follow their own rules:

| Purchase size | Handling |
|---|---|
| Below AED 3,500 (~USD 950) | Standard flow |
| Above AED 3,500 | Travel Rule information required |
| Above the instant-payment limit (AED 50,000) | Bank transfer or wire; enhanced due diligence; source of funds |
| **Above roughly one bar** | **Bought directly from the dealer instead of from the float**, so one big order cannot empty the float and pause minting for everyone else. Handled in two steps: an indicative price, then a same-day dealer purchase. The threshold and the longer settlement time are disclosed |

### 5.7 Worked example: one USD 75 contribution

At an illustrative price of USD 109.31 per gram, a 5% entry fee and 100 g bars at launch:

| Step | Value |
|---|---|
| Contribution received | USD 75.00 |
| Entry fee (5%, disclosed) | USD 3.75 |
| Net to gold | USD 71.25 |
| Grams at the next fix | 71.25 / 109.31 = **0.651815 g** |
| AURX minted | **0.651815** |
| Title | 0.651815 g allocated to the customer under the trust, same day |
| ICS | One counted month recorded (SIP) |

The customer can recompute the gram figure from the published price. Every number in the product can be checked by the person it belongs to.
---

## 6. The gold float and the treasury cycle

### 6.1 The problem: customers buy grams, dealers sell bars

Customers buy tiny amounts: a USD 75 contribution buys about 0.65 g. Wholesale gold only comes in bars, the smallest practical one being 100 g (about USD 11,000), and the working size is 1 kg. In Year 1, all SIP payments together buy about 11 g a day, so filling one 100 g bar takes about nine days. No dealer sells 11 g of allocated gold at wholesale prices every day.

The usual ways around this do not work for Aurumix: high minimum purchases would shut out the target saver, an unallocated buffer would break the "100% allocated" promise, and issuing tokens before the gold is bought would mean the token is not always fully backed.

### 6.2 The solution: a gold float

The **float** is a small stock of gold bars that Aurumix buys with its own money and keeps in the vault, separate from customer gold. It never counts as backing for AURX and is never mixed with customer bars.

How it works:

1. A customer pays, and the price is set at the next LBMA fix.
2. The same day, the customer's grams are moved **out of the float and into the customer's allocated holding** under the trust. The gold already exists and is already in the vault.
3. Once the float has given out one bar's worth of grams, Aurumix buys a new bar from the dealer to refill it.

**In short: the customer buys 0.65 g, and Aurumix buys a whole bar.** This is what makes a USD 20 minimum possible (PAXG needs about USD 120; XAUT's direct channel about USD 170,000).

The float does five jobs:

1. **Bridges the size gap** between small daily purchases and whole bars.
2. **Takes the price risk off the customer.** The customer gets their gold within 24 hours at a fixed benchmark price; any price movement while the float refills is Aurumix's.
3. **Allows a firm price at the point of sale**, based on the public benchmark.
4. **Handles buybacks.** Gold a customer sells back goes into the float, so no bar has to be sold on every exit (section 7.3).
5. **Handles loan defaults.** If a loan's collateral must be sold, the float buys it at the fix, with no need to find a buyer on a bad day (section 10.4).

**Aurumix funds the float from its own capital from the first month.** Customer money is never used for it, and the float and customer gold are always kept separate, in the vault and in the accounts.

### 6.3 Float size and bar upgrades

**Size:** at least one bar plus a buffer of a few days' purchases. At launch the setting is two 100 g bars, about USD 22,000 of gold. The float is a fixed amount, so it becomes a smaller share of total assets as the business grows.

**Bigger bars are cheaper per gram.** The dealer's premium over the gold price is about **1.50% on a 100 g bar and 0.95% on a 1 kg bar**. Moving to 1 kg bars needs a bigger float, so Aurumix moves up when the premium saved each year is more than the cost of the extra float capital and its price risk.

**Two costs to know:**

- **Refill price risk.** The float gives out gold at today's price and is refilled at a later price. At normal gold volatility this is well under 0.5% of purchases and averages out to zero over time.
- **The pricing rule itself.** Setting the customer's price at the next LBMA fix, hours away, instead of a live quote costs about 0.79 percentage points. Switching to live quotes is a client decision still to be made.

### 6.4 Refilling the float

| # | Step | Detail |
|---|---|---|
| 1 | Trigger | The float has given out one bar's worth of grams |
| 2 | Buy a bar | From the two-way dealer at the fix plus the premium. **The premium is paid only on new gold**: gold that customers sold back is resold from the float, so it is not re-made |
| 3 | Intake | Independent assay, vault receipt, serial number recorded, title registered to the trust vehicle (on Tradeflow where used) |
| 4 | Monthly Allocation Report | Published: bar serial numbers, assay certificates, grams issued, prices used, float balance and customer balance |

The monthly report replaces the client's "Mining Event" as a verifiable public update on the gold.

### 6.5 Rules the system enforces

Checked automatically and published monthly:

- **Backing:** `trust gold holdings >= AURX outstanding`, at all times (section 4.3). The float never counts toward backing.
- **Client money:** `Client Account balance >= money collected but not yet used for gold or refunded`, checked daily.
- **No token without gold.** Minting stops automatically if the float runs out, the custodian's confirmation lapses, or the title record is unavailable.
- **Order:** money, then title, then token (section 5.3).
- **Sourcing:** gold only from accredited refiners, with bars swapped if a refiner loses accreditation (section 2.1).

### 6.6 The dependency: the bullion dealer

**Aurumix has not yet named its two-way bullion dealer**, and the float, the refills, the buyback and the fee levels all depend on one. The vault stores gold but does not sell or buy it; a dealer does. Dubai's wholesale gold market does not publish premiums, buy-sell spreads, minimum order sizes or title-register fees, so several numbers in this section are estimates until a dealer quotes real terms. Signing a dealer is the most important commercial step on the critical path.

---

## 7. The exit: cash buyback

### 7.1 The buyback as a redemption right

Customers exit by selling their gold back to Aurumix for cash; there is no physical delivery, which suits customers who hold fractions of a bar. VARA makes a redemption right optional for an ARVA (section 3.7). Aurumix grants it anyway, for three reasons:

1. **A published buyback at a set price is likely to be treated as a redemption right whatever it is called.** Designing for the stricter reading from the start avoids a rebuild later.
2. **A guaranteed exit is what makes the token trustworthy.** Without one there is no price floor, and the gold tokens that restricted their exit trade below the value of their gold.
3. **The customer already owns the gold.** A committed way to turn it into cash is the natural counterpart of that ownership.

Granting the right means following Annex 2 III.E.4: **no fee of any kind on the way out.** Storage costs are therefore never charged on the exit (section 13.3). A zero exit fee also makes sense on its own terms: an exit fee would push AURX's realised value, and later its market price, below the gold price, and charging customers to receive the value of gold they already own would be hard to justify. That second point is our design reasoning, not a stated VARA position.

### 7.2 The exit step by step

| # | Stage | Timing | Detail |
|---|---|---|---|
| 1 | Request | T | An amount in grams or currency, full or partial |
| 2 | Checks | minutes | Customer onboarded (III.E.3), sanctions re-screen, residence re-check, bank account name-match, no grams pledged to a loan, rapid buy-and-sell flag |
| 3 | Price struck | **next fix after the request** | Neither side chooses the price |
| 4 | Tokens burned | same day | From the customer's verified wallet |
| 5 | Title returns | same day | The grams move from the customer's holding back to the float |
| 6 | Payout | target T+1 | To the customer's own name-matched bank account. AED always available; USD as disclosed |
| 7 | Float rebalance | when needed | Only if the float grows above its upper limit does Aurumix sell gold to the dealer |

The checks run **before** the price is set, so a failed check never leaves a price hanging.

### 7.3 Why a zero-fee exit is affordable

The worry is that Aurumix must pay the dealer's buy-sell spread every time a customer exits, and cannot charge for it. In practice most exits never reach the dealer: the grams go back into the float and are sold to the next buyer.

| State of the business | New purchases | Exits | Net flow | Gold sold to the dealer |
|---|---|---|---|---|
| Growing | 8% of assets | 3% | +5% | **None.** Exited grams go to the next buyer |
| Flat | 4% | 4% | 0% | **None** |
| Shrinking | 2% | 6% | -4% | Only the 4% net |
| Run | 1% | 25% | -24% | A large amount, at the dealer's buying price, in a falling market |

**Aurumix only pays the spread on net outflow, not on every exit.** In a growing business that is close to zero. This is also the strongest argument for funding the float.

### 7.4 Many exits at once

The last row of the table, a run, is possible, and the design deals with it openly. VARA does not allow an exit fee, so Aurumix cannot use price to slow exits down. The only room the rule gives is time: exits must be completed "within a reasonable period" (III.E.3). The design uses that room in four ways:

- **Published settlement times by size.** Small exits are paid the next business day. Exits that may need a sale to the dealer take up to three business days. Large exits take up to five, and may be paid in stages. The exact size limits are set once the float size is known, and all of this is published in the whitepaper.
- **Customers' gold is safe even if Aurumix runs short of cash.** The gold belongs to the customers and is held by the trust, outside Aurumix's estate. If Aurumix could not pay cash, customers would still own their gold, and Aurumix's creditors could not take it. This is the main reason for the trust structure.
- **The wind-down plan is the last resort.** Because customers own their gold directly, the plan never needs to sell customer assets to work (section 3.8).
- **Exits can be suspended only in narrow, disclosed cases:** the market is closed, the custodian fails, or an event outside anyone's control (force majeure). A suspension is never allowed just because Aurumix is short of cash.

### 7.5 Transfers are not exits

Sending AURX to another person moves the gold's ownership with the token (section 4.5). On our reading this is not a redemption, so the no-fee rule does not apply. The grams move between holders and the total does not shrink. A secondary market also gives holders a way out that does not use the buyback at all, which reduces pressure on it. For the ICS score, sending AURX counts as gold leaving the sender's account (otherwise sending it to a spouse would avoid the Retention rule), and received grams count as both acquired and held for the receiver, so no score is created from nothing.

> **Open for counsel in this section:** all three parts of Question 3. Whether the buyback is legally a redemption, whether "equal value" means full value or value net of the dealer's buying price, and whether selling a customer's gold after a loan default is covered by the no-fee rule. The rulebook never defines "redemption", so all three are our reading of its structure, and we want the first confirmed by VARA in writing.
---

## 8. The Investor Conviction Score

### 8.1 What ICS is

The Investor Conviction Score (ICS) is the loyalty engine: a 0 to 100 score that prices every benefit in the product. It exists because the economics demand it. The persistency benchmark for the persona (Indian life insurance) retains roughly 79% of savers at month 13 and 38% at month 61, and a customer is barely profitable in year one; churn kills this model, not fee levels. The score is the retention machinery.

**The one rule: ICS measures behaviour, never amount.** No input reads dollars or grams held. A customer saving USD 20 a month and one saving USD 2,000 a month reach the top tier on the same day. This also protects the product from being classed as a security: if the score rose with amount, then the entry-fee discount, the credit ratio and the rewards rate would all improve with capital, which is a return proportional to investment: the securities shape the whole design avoids. **Amount sizes the base; behaviour sets the rate.**

### 8.2 The gate: Confirmed SIP

> **Confirmed SIP is six consecutive counted periods, and it gates the score itself, not only the benefits. Before the door: no score, no tier, no tier benefits (credit and the card are open to everyone at base terms). After it: the score runs, and never falls below 25.**

Two objects, kept separate:

| | What it is | How it moves |
|---|---|---|
| **Confirmed SIP** | A door. Six consecutive contributions opens it | Opens once. **Permanent.** A later miss never closes it |
| **The ICS score** | A dial behind the door | Recalculates monthly from the moment the door opens |

The customer sentence: *six months straight to start, then your score runs and it decides what you get.*

Rules of the gate, in plain terms:

- **It is six payments in a row, not a six-month contract.** Nothing is promised. If the run breaks, the customer simply starts counting again.
- **Everyone starts in the same place.** Payments made before the six-in-a-row run still buy gold but do not count toward the score. So every customer who passes the gate starts at Silver, with a score of 25.
- **Before the gate, the app shows a countdown, not a score** ("4 of 6, three months to go"). A low number in the first months would look like a bad credit score and could put new savers off. If the run breaks, the app says so clearly and the countdown restarts.
- **The trade-off is disclosed.** A customer who pays often but never six months in a row never gets a score, and months one to five get no tier discount. Both are stated in the terms and in the app.
- **Every account passes its own gate**, family sub-accounts included. Status cannot be inherited.
- **A regulatory block pauses the count instead of breaking it** (section 5.5). A saver at 4 of 6 picks up again at 4 of 6.

### 8.3 The formula

```
ICS = min( Record , Standing ) x Retention        floor of 25 once Confirmed
```

Three inputs, every one readable off the payment ledger and the token ledger. No weights, no normalisation constants, no component caps.

**The three facts:**

| Fact | Measures | Moves how |
|---|---|---|
| **Months** | Counted periods since the qualifying run began. *What you contributed* | +1 per counted period. **Never falls, for any reason** |
| **Recent** | Counted periods in the trailing 12 calendar months (0 to 12). *Whether you are contributing now* | Rises and falls as the window rolls. Self-healing over 12 months |
| **Sold** | The share of everything you had that you no longer have. *Whether you kept it* | Recomputed monthly |

**The mappings:**

- `Record(m)`: your first year of payments takes you to 50 (4.1667 points per month to month 12), the next four years take you from 50 to 100 (1.0417 per month to month 60), capped at 100. Five years of saving is a complete record; the raw month count keeps displaying forever as recognition, but the cap is what stops the score becoming miss-proof by seniority.
- `Standing = Recent x 8.3333`: each of the last twelve months is worth the same.
- `Sold = 1 - grams held now / (grams held 12 months ago + grams acquired since)`, and `Retention = 1` for Sold up to 30%, falling linearly to 0 at full liquidation. The customer sentence: *you can take out up to a third of your gold in a year and nothing happens at all.*

**Why a minimum and not a weighted sum: this is the load-bearing choice.** Each tier is genuinely two conditions (for example Gold is "12 months paid AND 6 of the last 12"), and `min(A, B) >= x` is exactly `A >= x AND B >= x`: **minimum is the arithmetic of AND.** A weighted sum would let one input make up for another, so a long-time saver who had stopped paying could still score near the top. With a minimum, no substitution is possible in either direction, there are no weights to argue about, and the score names its own constraint: if ICS equals Standing, discipline binds (pay); if it equals Record, only time does. For a saver who never misses, Standing never binds (provable from the mappings), so a good customer's score is purely their Record.

**Retention rules that matter to counsel and to the build:**

| Case | Rule |
|---|---|
| Gold Rewards gram credits | Count as acquired: they enlarge the denominator and can never create or worsen a penalty |
| Transfers to a family sub-account or under a Beneficiary Transfer Instruction | **Not a sale.** The gold stays inside the product; only the name changes |
| Lender liquidation on a margin call | **Counts as a sale.** The customer chose to borrow; the alternative makes borrowing a route around Retention |
| Withdrawal to self-custody | **Counts as a sale** (section 4.2). The account can no longer see or service those grams |
| Compliance-forced exit (the returning NRI) | **Not a sale.** The regulatory pause extends to forced redemptions: the grams leave, and the score does not move (section 5.5). The dividing line between this row and the margin-call row is choice: a margin call follows a loan the customer chose to take; a compliance exit follows nothing they chose |

Retention is drafted as a reward for holding, not a penalty for redeeming, and the direction matters in front of a regulator: gold-months earn score, grams that leave simply stop earning, and no event fires on the redemption itself. A rule shaped as "redeem and lose your status" would invite the argument that it impairs the redemption right in substance.

### 8.4 The tiers

Five tiers, four of them named. The bottom rung is literally the absence of a tier.

| Tier | ICS | As conditions | A perfect saver arrives |
|---|---|---|---|
| No tier | no score | Confirmed SIP not yet earned | |
| **Silver** | 25 | Six consecutive contributions. Permanent | Month 6 |
| **Gold** | 50 | 12 months paid AND 6 of the last 12 | Month 12 |
| **Platinum** | 75 | 36 months paid AND 9 of the last 12 | Month 36 |
| **Sovereign** | 100 | 60 months paid AND 12 of the last 12 AND Sold <= 30% | Month 60 |

The ladder in one sentence: **Silver at six months, Gold at one year, Platinum at three, Sovereign at five.**

**Why five tiers.** The total value of the benefits is fixed by outside costs: the fee margin, the lender's maximum loan ratio, Aurumix's share of card interchange and the card issuer's three product levels. More tiers would only cut the same benefits into smaller steps; with seven, one fee step would be worth about USD 0.19 a month on a USD 75 contribution, too small to notice. With five, the benefits roughly double at each step, and the three card levels fit the ladder (L1 for everyone, L2 at Platinum, L3 at Sovereign). Interchange, mentioned throughout this document, is the small percentage of each card purchase that the merchant's side pays to the card issuer; it funds card programmes, and the merchant pays it, not the saver.

**Tiers are fixed thresholds, not rankings.** A customer's tier depends only on their own record, never on how other customers do. With rankings, a perfect saver could be pushed down by better savers, benefits could not be quoted as fixed prices or loan terms, and customers would be competing with each other, which regulators treat with suspicion. Fixed thresholds also let every customer work out their own score.

**Sovereign allows no misses.** Both inputs top out at 100, so Sovereign has to require a perfect score, or customers would reach it too early. Sovereign means paying every month for the last year, on a five-year record, with the gold kept, and it has to be kept up month by month. Losing it costs little in practice, because benefits already delivered are never taken back (section 9.1).

### 8.5 The price of a miss

There is no penalty table. A miss reduces Recent by one for twelve months and then ages out; everything else is arithmetic:

| Consecutive misses (veteran at Sovereign) | Standing | Tier |
|---|---|---|
| 1 | 91.7 | Platinum |
| 3 | 75 | Platinum |
| 4 | 66.7 | Gold |
| 7 | 41.7 | Silver |
| 12 | 0 | Silver (the floor) |

Properties that fall out of the trailing window rather than being engineered: an isolated miss costs one tier at the very top and often nothing mid-climb; the alternating pay-miss gamer holds Recent at 6 forever and is capped at Gold for life with no rule written; loss is instant and rebuild takes the window's full length; and a lapsed veteran rebuilds only Recent, so roughly nine clean months restores Platinum against the 36 a newcomer needs. *You never re-earn your history, only your form.*

The governing promise, in exactly these words: **you can lose your status, you can never lose your gold.**

### 8.6 Fairness verification

Nine personas are maintained in the project record and re-run under every formula change; the rows that matter most:

| Persona | Outcome |
|---|---|
| USD 20 perfect saver, month 60 | **Sovereign.** The binding design test: the smallest saver reaches the top on contributions alone |
| USD 2,000 perfect saver, month 60 | **Sovereign, the same day.** A hundred times the money buys zero tiers |
| The cycler (contributes and redeems every month) | Retention 0: floor Silver, forever, on a flawless payment record. The one number that cannot be faked |
| Withdrew 30% at month 36 | **No change at all.** The allowance is genuinely free |
| Withdrew half at month 36 | One tier, healing in 12 clean months |
| Liquidated everything | Floor Silver; heals in 12 clean months. A one-time liquidator is not a cycler |
| The scattered payer (six payments over three years, never six in a row) | No tier. The stated cost of the consecutive gate, mitigated by the countdown display |

Fairness invariants: no input reads amount anywhere; a new saver is never behind; a miss costs standing, never property; refused money never scores against you; nothing already delivered is ever taken back; the score attaches to the verified identity, so cancel-and-reopen buys nothing.

### 8.7 Anti-gaming

The design's preference is structural impossibility over written rules; six of eleven catalogued attacks are impossible by construction:

| Attack | Closed by |
|---|---|
| Prepay, split payments, shuffle dates | One counted period per calendar month |
| Alternate pay-miss | Recent holds at 6; capped at Gold for life |
| Late lump sum to restore a record | No revival exists; nothing after grace can touch the record |
| Referral or family farming into the score | Neither is a score input |
| Sell then rebuy before assessment | Sold reads opening balance, acquisitions and closing balance; the sale stays in the numerator |
| Compress or buy the gate | Six consecutive calendar months cannot be compressed, bought or backdated |

What written rules still cover: **the credit prize** (cycle to a tier, buy a large position, borrow high) is removed by 90-day collateral seasoning plus the ratio being struck at the facility (section 10.3), and Retention keeps a cycler at the base credit ratio; **the residue** is covered by a round-trip flag (a redemption within 30 days of a contribution, four or more months in any twelve, freezes tier progression pending review, with a stated appeal path and nothing deducted). A large holder cycling a small SIP beside static ballast is detectable by the flag and is otherwise not worth defending against: their honest compliance costs USD 20 a month.

---

## 9. The five benefits

### 9.1 What each tier gets

There are five benefits. **Credit and the card are open to every customer**, at base terms (a 40% loan-to-value and the L1 card on the issuer's standard terms), so that neither the card nor credit revenue is limited by tier. The tiers make the terms better.

| | No tier | Silver | Gold | Platinum | Sovereign |
|---|---|---|---|---|---|
| **1. Entry-fee discount** | 0 | 0.4pp | 0.8pp | 1.2pp | **1.5pp** |
| **2. Credit LTV** | 40% | 40% | 50% | 65% | **80%** |
| **3. Card level** | L1 | L1 | L1 | L2 | **L3** |
| **3. Card FX margin** | Standard | Standard | 2.0% | 1.5% | **1.0%** |
| **3. Card ATM allowance (AED/month)** | Standard | Standard | 1,000 | 2,500 | **5,000** |
| **4. Gold Rewards rate** | - | - | 0.15% | 0.45% | **0.75%** |
| **5. Will plan-fee discount** | 0 | 10% | 20% | 35% | **50%** |
| **5. Per-beneficiary discount** | 0 | 0 | 0 | 10% | **20%** |

The biggest step is Silver to Gold, where the credit ratio and card terms first improve and Gold Rewards begins.

**Five rules apply to every benefit:**

- **One tier, updated monthly.** Every benefit uses the tier set at the last monthly update, never a live score, so no two benefits can disagree.
- **Fixed steps.** Every benefit is a clear price, loan term, card level or rate that can be quoted.
- **A lower tier only affects the future.** Nothing already given is taken back, an open card or credit line is never closed, and **a tier fall never triggers a margin call**.
- **No benefit grows with the amount saved**, and no payout can exceed what that customer's own activity earned.
- **Where a partner holds the licence** (the lender, the card issuer), Aurumix sets the structure and the partner sets the price.

### 9.2 Benefit 1: a lower entry fee

Each tier takes percentage points off the entry fee on **every purchase**, SIP and spot. It is the only benefit that is live at launch with no partner needed.

It is affordable because the discounts grow at the same pace as Aurumix's own costs fall: nobody is above Silver in year one, so the biggest discount at launch is 0.4 points, and the first Sovereign customer appears at month 60, by which time Aurumix is buying bigger, cheaper bars (section 13.2).

A slightly smaller fee is easy to miss, so the app shows the **total saving as grams of gold** ("your tier has earned you 1.4 g since 2026"). The number only ever goes up.

### 9.3 Benefit 2: a higher credit limit

Customers can borrow against their gold without selling it. The limit is:

```
borrowing limit = grams held 90+ days x gold price x LTV(tier)
```

Everyone gets 40%, rising to 50 / 65 / 80% at Gold / Platinum / Sovereign. The grams set the size of the limit and the tier sets the percentage, so two customers with the same behaviour get the same percentage, however much gold each holds.

**Why 80% at the top.** It matches the highest level seen in comparable gold lending without going above it: India's regulator caps retail gold loans at 75 to 85% depending on size, the largest Indian gold lenders lend at the cap, and a UAE lender already lends against vaulted gold at 80%. If the lending partner's maximum turns out lower than 80%, the ladder has to be repriced. The full credit design is in section 10.

### 9.4 Benefit 3: better card terms

Every customer can have the card at level L1 on the issuer's standard terms. Gold lowers the FX margin and adds an ATM allowance, and Platinum and Sovereign move the customer up to the L2 and L3 cards.

- **The card itself** (and its bundled perks) upgrades after three months in a row at the higher tier, and **never downgrades**.
- **The fees** (FX margin, ATM allowance, fee waivers) follow the tier each statement.

The card discounts are paid for by the interchange that the same customer's spending generates, so a customer cannot use the benefit without also producing the revenue that funds it. The full card design is in section 10.

### 9.5 Benefit 4: Gold Rewards

**Gold Rewards is a monthly cashback on card spending, paid in grams of gold.**

```
Gold Rewards = reward rate (by tier) x card spend that month
```

It is calculated at the end of each month and credited at the next fix. Four rules keep it a rebate and stop it being treated as an investment return:

1. **Paid from card and credit revenue**, never from company profit or from other savers' fees.
2. **Capped at the revenue that customer's own card and credit use produced**, less their custody cost.
3. **Rate set by tier, and tier set by behaviour.** The base is spending; the amount of gold held plays no part.
4. **Never called yield, interest, return or dividend**, anywhere.

**Why a rebate and not a share of profit.** A payout from company profit, weighted by how much each customer holds, would be a profit share, which regulators treat as a security. That would bring prospectus rules and a different regulator, which a USD 20 savings product cannot carry. Well-regulated gold tokens pay no yield, and those that advertise one tend to miss it (one realised about 0.10% a year against an advertised 2%). Cashback in gold funded by card fees, on the other hand, is ordinary and uncontroversial.

Gold Rewards starts when the card starts, because there is no card revenue before that. Reward grams count as gold acquired in Retention (they can never raise a score), do not count as SIP months, and must be held 90 days before they count as loan collateral.

### 9.6 Benefit 5: cheaper family services

The Family Portfolio and Digital Will are open to **every customer who pays for them, at every tier**. The tier only lowers the price: up to 50% off the annual plan fee and up to 20% off each beneficiary's registration fee. The discount stops below 100%, because free services at the top would leave the most-used services unfunded. The full family product is in section 11.

### 9.7 What is live on day one

| Benefit | Live when |
|---|---|
| Entry-fee discount | Launch |
| Family discount | Launch, with the paid feature |
| Credit ladder | When the lending partner signs |
| Card terms | When the card programme goes live |
| Gold Rewards | With the card |

A customer who earns a tier before the card exists keeps it; the card benefits arrive when the card does. The app presents the tier as the lasting thing and the benefits as what it currently gives, so each new benefit arrives as a bonus for existing tiers.
---

## 10. Credit and the Gold Card

### 10.1 One facility, two draw channels

The credit facility and the Gold Card are not two products. They are **one gold-secured revolving credit facility with two ways to draw on it**: a cash drawdown to the customer's bank account, and card spend that draws against the same limit. Same collateral, same tier ladder, same lender's balance sheet, one borrowing limit in the app.

The purpose is the product's quiet centrepiece: it lets a saver reach the value of their gold without selling it, which is what makes a decades-long hold tolerable. Pledged gold keeps earning the customer's score, so using the facility never sets the saver back.

One rule this structure forces: **the facility is struck once, at facility opening, and every draw inherits the facility's struck ratio.** A card is thousands of tiny draws; striking per draw would reprice the facility on every coffee. An annual facility review re-strikes the limit to the current tier of record, while existing drawn balances run to term at their original ratio, which keeps the tier ladder binding without ever repricing anyone retroactively.

A second rule: **the facility and the card are open to every customer, and a tier fall never closes them.** No tier is needed to open either; the tier only sets the terms. The plastic never downgrades. Card parameters flex with the tier of record down to the base terms and stop there. The annual review re-strikes the limit at the current tier of record, never below the 40% base ratio. Only the collateral ladder (section 10.4), the customer or the lender of record can close them. So a saver who stops contributing keeps the card and the credit line for as long as the collateral supports them. This follows from two positions already taken: no delivered benefit is ever clawed back, and the loan is secured on gold the customer owns, not on their payment behaviour.

### 10.2 The stack: four roles and their risks

| Role | Does | Carries |
|---|---|---|
| **Issuer processor** | Real-time authorisation, card lifecycle, wallet provisioning, the card ledger | Operational risk |
| **Issuer of record** | The licensed name on the card, scheme membership | Scheme and regulatory risk |
| **Lender of record** | Advances the money, owns the loan book | **Credit risk** |
| **Aurumix, programme manager** | Customer, app, origination policy, collateral valuation, the authorisation decision, servicing, collections | Operational and reputational risk |

Aurumix does not lend or issue cards itself, for two reasons: a VARA lending permission only covers lending a virtual asset and getting the same asset back, so a cash loan in dirhams falls outside it; and issuing cards requires card-scheme membership plus a CBUAE retail-payments licence. Suggested partners: **NymCard** as processor (UAE-native, credit-capable, a principal member of both schemes in its own right, which may collapse the bank-plus-processor pair into one vendor), **Emirates Money** then Mashreq as lender of record (Emirates Money already lends against physical gold at 80% LTV, vaulted at DMCC with Brink's: the same product, the same number, the same vault), Zand or CBD for VASP banking.

### 10.3 Setting the limit and authorising a tap

```
borrowing headroom = seasoned, unpledged grams x fix x LTV(tier)
```

| Gate | Rule |
|---|---|
| Eligibility | Every verified customer. No tier is required; the tier sets the ratio. An open facility survives a later tier fall (section 10.1) |
| Seasoning | Grams enter the borrowing base only after **90 days held**. Redeemed-then-rebought grams restart the clock; inbound transfers start fresh |
| Ratio | 40% base (No tier and Silver), then 50 / 65 / 80% at Gold / Platinum / Sovereign, struck at facility opening |
| Stacking | Seasoned **and unpledged** grams only. One gram supports one facility |
| Custody | Pledged grams sit in platform custody under a registered security interest and cannot be withdrawn or transferred until released |

Card authorisation runs on just-in-time funding: on each tap the processor calls Aurumix's endpoint, Aurumix computes live headroom (grams x current fix x struck ratio, less outstanding balance) and answers approve, decline or partial-approve in real time. Two consequences the build must absorb: Aurumix owns the authoritative balance ledger, and collateral is effectively re-marked on every transaction. A 48-hour hold on redemption requests from accounts with an active card facility closes the authorisation-to-settlement gap during which collateral could otherwise leave.

**The stand-in hole is unavoidable and is disclosed to the lender rather than discovered with them.** If Aurumix is unreachable the processor approves from pre-agreed static rules; if the processor is unreachable the card network stands in unilaterally. Both approve with no collateral check, and Aurumix learns afterwards. The static rules are the only lever: small per-transaction cap, low transaction count, no ATM, no cross-border, a hard cumulative stop, sized so the worst case on any account is immaterial against even a base-ratio facility.

### 10.4 The liquidation ladder

Neither market model fits unmodified: crypto lenders buy safety with a price buffer and instant liquidation; Indian gold loans buy it with short tenor and days of procedure. A revolving card facility has neither short tenor nor atomic liquidation, so it takes the widest explicit buffer plus the procedural protections.

| LTV reached | What happens |
|---|---|
| 80% | Normal; maximum origination |
| **85%** | Notice, app and push. Informational |
| **88%** | **Cure notice**, formal, in writing: 14 days to top up gold, repay part, or add cash |
| **92%** | **Partial liquidation: sell only enough to restore 88%** |

The restore point is 88 rather than 80 because a sale shrinks loan and collateral together: restoring all the way to 80 would sell roughly 60% of the remaining gold, where restoring to 88 sells roughly a third and returns the customer to the cure threshold rather than to square one. Never full liquidation: partial always, and the customer keeps the facility.

Who is actually exposed, and this table is presented to stakeholders rather than hidden:

| Tier | Struck LTV | Gold fall needed to reach 92% |
|---|---|---|
| No tier and Silver | 40% | -57% |
| Gold | 50% | -46% |
| Platinum | 65% | -29% |
| Sovereign | 80% | **-13%** |

A 13% fall is roughly a one-sigma annual move: Sovereign borrowers at maximum draw are genuinely exposed, and the design does not pretend otherwise. The mitigations are the two warnings, the 14-day cure, and the population itself (the smallest, most disciplined cohort in the book).

Procedure follows the regulator-tested Indian template in shape (notice, cure, objection right, reserve price, surplus returned, costs itemised), executed against the float at the LBMA fix with zero discretion, because Aurumix is valuer, collateral agent and buyer at once and the only cure for that conflict is a mechanical price. Whether an enforcement sale is itself a "redemption" for the no-fee rule is a live counsel question (legal brief, Question 3): if it is, recovery costs cannot be charged.

The wordings that must never blur: **a tier fall can never margin-call; a price fall can, and only against borrowed positions, past thresholds shown at the draw.** *Your score can never cost you your gold; the market can, only if you borrow against it.*

### 10.5 Making the pledge legally sound

For a loan against gold to work, the lender must have a legal claim on the pledged gold that holds up against everyone else. Sections 10.3 and 10.4 cover locking the gold, valuing it and selling it. What remains is legal work:

- **The lender's claim is registered under DIFC law** (the Law of Security 2024). Registration with the DIFC registrar makes the claim valid against third parties. DIFC is used because ADGM's equivalent appears to cover only charges given by ADGM companies, and here the borrower is an individual customer.
- **The claim is taken over the customer's interest in the trust**, treated as an ordinary right. Whether AURX also counts as a "digital asset" under DIFC law is unclear, so the design does not rely on it. Blocking the pledged tokens from moving is an operational control, not a legal one.
- **The trust vehicle agrees in advance** that pledged gold can be released to the lender on default. Whether that advance agreement is legally effective is for counsel to confirm.
> **Open for counsel in this section:** Question 5 in full. Whether a valid security interest can be taken and registered over a retail customer's beneficial interest, which legal route applies, and whether Aurumix acting as valuer, collateral agent and buyer at once is a conflict that disclosure can manage. If the security is not clean, the credit and card block does not work as designed.

### 10.6 The interchange economics

Verified against the card scheme's published UAE interchange schedule: prepaid interchange is 1.00% flat and capped by regulation; **credit interchange is uncapped and runs 1.80% (Platinum) to 2.10% (Infinite) by product level**. Two design consequences:

- **The card is built as credit, not prepaid**, or interchange is capped at 1.00% forever and the rewards ladder starves.
- The tier ladder and the revenue ladder are the same ladder: upgrading a loyal saver's plastic moves them to a higher-interchange product, so the upgrade enlarges the pool that funds their own rewards.

The one number to negotiate: Aurumix's programme-manager share of interchange must exceed roughly **36%** for Gold Rewards to self-fund at the Sovereign rate (0.75% rewards against 2.10% interchange). No UAE or MENA programme-manager split is published anywhere; it is term-sheet work, and 36% goes into the conversation as the floor.

---

## 11. Family Portfolio and succession

### 11.1 The two objects

The family product has two separate parts, with different legal character, costs and risks:

| | **Family Portfolio** | **Beneficiary Transfer Instruction (BTI)** |
|---|---|---|
| What it is | A live sub-account structure during the holder's life | A standing, pre-authorised instruction on the account |
| Legal character | Account administration | A client instruction under VARA's custody rules, which permit a VASP to rely on pre-authorised client instructions |
| When it acts | Continuously | Once, at a defined trigger |
| Priced by | The annual family plan fee | The per-beneficiary registration fee |

"Digital Will" is the marketing name, but it may need to change because it suggests a regulated will-writing service. The contractual term is **Beneficiary Transfer Instruction**; the feature is a standing instruction, not a testamentary instrument.

During life, a sub-account is a declaration of intent and a display: the gold remains entirely the primary holder's, family members see their designated grams read-only, and a sub-account has **no independent credit facility and no ICS sub-score** during the primary's life. You cannot lend against gold someone does not yet own, and ICS is one number about one person. Each family member's own account passes its own gate when gold actually transfers to them.

### 11.2 The precondition: gold kept with Aurumix

Under an open token a customer can withdraw AURX to their own wallet, and at that moment there is nothing for a standing instruction to act on. **The Family Portfolio and the BTI are custodial-account features; they attach to the account, never to the token.** A withdrawal to self-custody removes those grams from the family features and counts as a disposal for scoring (one rule, two problems closed). This is not a weakness to hide: it is the honest reason a balance stays on-platform, and it is what every custodian does. The 30% annual Retention allowance is the pressure valve that keeps the strict rule fair.

### 11.3 Probate still applies on death

Probate is the court process that confirms who inherits a person's property after they die; the grant is the court document that proves it. **Aurumix cannot avoid probate on death.** Under DIFC trust law, a customer's interest in the gold is property that passes into their estate, so a court grant is needed before it can be transferred. The only structure that avoids probate is one where the customer never owns the gold, and that would give up direct ownership.

Other providers are in the same position: the largest regulated crypto custodian offers no beneficiary option at all and asks for probate documents before releasing anything. What Aurumix offers is a **faster probate process**: beneficiaries are named, verified, screened and their shares set in advance, so the transfer happens within days of the grant arriving.

### 11.4 The trigger matrix and residence

The three triggers are three different legal events, not three flavours of one:

| Trigger | What it legally is | Probate? | Forced heirship? |
|---|---|---|---|
| **Date** (a birthday, an education milestone) | A completed lifetime gift | No: the holder is alive | Shielded: the DIFC firewall protects completed lifetime transfers |
| **Condition** (a defined, observable event in the beneficiary's own life) | Same, if it fires during life | No | Shielded |
| **Death** | Testamentary succession | **Yes: grant required, hard gate** | Exposed: the firewall covers lifetime transfers only |

**The lifetime trigger is the strong product and leads the design**: the education fund and the wedding gift, not the death benefit. Conditions between unrelated parties contingent on account behaviour are not supported: that is a wager on behaviour, not succession, and it would collide with the regulatory pause.

**For India-resident beneficiaries the matrix inverts**, and this is the sharpest fact in the design. On death, Indian exchange-control law gives a resident an express, uncapped permission to hold assets inherited from a person resident outside India. On a lifetime gift, the transfer falls out of the exchange-control regime into the foreign-contribution regime, where the test turns on the donor's passport rather than residence: too fine a distinction to enforce in an app. So: **lifetime transfers to India-resident beneficiaries are blocked at launch; death transfers are settled to cash**, because the inheritance permission is a closed list (foreign currency, foreign security, immovable property) and an allocated-gold token is arguably none of the three. Settling to cash sidesteps the classification question entirely; no resident ever holds the token. The India leg is also free by construction, because cash settlement is probably a redemption and the no-fee rule reaches it.

### 11.5 Execution: trigger plus proven authority

| Step | Lifetime trigger | Death trigger |
|---|---|---|
| Trigger | Date reached or condition evidenced | Death notified |
| Freeze | n/a | Immediate on credible notice: withdrawals and new draws stop |
| **Authority** | None needed: the holder is alive and instructed it | **Grant of probate or court order. Aurumix does not adjudicate; it waits** |
| Beneficiary status | Re-verify identity, re-screen, confirm residence | Same |
| Encumbrance | Pledged grams resolved per section 11.6 | Same |
| Execution | **In specie: a single token movement between two verified accounts** | Same, or cash settlement where the beneficiary is India-resident |

**In-specie transfer is not a redemption; cash settlement probably is.** Redemption is request-driven, value-delivering and claim-directed; a beneficiary who receives tokens and keeps them exercises nothing. So the paid service administers in-specie transfers only, and a beneficiary who wants cash onboards, takes the tokens, and redeems free like any holder. **The fee is charged at beneficiary registration, never at the transfer event**, which is the whole defence against recharacterisation as a disguised exit fee. The rulebook never defines "redemption", so written confirmation of this split in pre-application dialogue is the top succession ask (legal brief, Questions 3 and 7).

### 11.6 Pledged gold: the lender outranks the beneficiary

Ordering on any trigger: secured creditor, then estate expenses, then the beneficiary, who takes the net interest with an **express right to redeem the gold whole by paying the debt**. Five contract clauses carry this (subordination stated in the instruction, transfer of the net interest, lender release as a condition, the beneficiary's redemption right, a standstill before enforcement). Death is not an automatic event of default, and the partner agreement must not make it one.

### 11.7 Pricing

Checking and monitoring each beneficiary costs about USD 2 to 3 once, plus a few cents a year. The main costs are monitoring names over decades and the screening provider's monthly minimum.

The price is an **annual family plan of about USD 29 to 36, covering up to four beneficiaries, plus USD 20 for each extra name**, capped per household and charged at registration. Even at the deepest tier discount, the price covers the cost about five times over. VARA does not cap these fees; they must be disclosed in the Client Agreement.

### 11.8 What Aurumix does and does not do

| Aurumix does | Aurumix never does |
|---|---|
| Carry out a documented standing instruction | Decide who is entitled to an estate |
| Require a court grant before a transfer on death | Confirm a death or settle competing claims |
| Register and monitor named beneficiaries | Write, witness or register a will |
| Tell customers to keep a valid will where they live | Give estate planning, tax or succession advice |
| Refer customers to a licensed will-writer (for example the DIFC Courts' digital-assets will service) | Take a referral fee for it |

The feature is never described as estate planning (which would look like advice) or as a payment on death (which would look like insurance). Aurumix holds neither licence.

> **Open for counsel in this section:** Question 7: how the succession product can be offered lawfully, to whom, and under what name. Also the in-specie / cash-settlement split (Question 3) and the India inheritance route.

**Build note:** none of this goes on-chain. The family features are an off-chain instruction record, with one token movement when a transfer is carried out. Holding family gold in a smart contract would make the contract the trust's beneficiary, so the family member would own nothing (the wrapper problem in section 4.4).
---

## 12. Distribution: referrals and the agent network

### 12.1 How customers are brought in

Distribution is Aurumix's main advantage (section 1.4). One rule shapes the design: **a referral reward is a cost of acquiring a customer.** It is not one of the five benefits and does not count toward the ICS score.

There are three ways a customer arrives:

| Route | Who | Paid | Contract |
|---|---|---|---|
| 0. Direct | The customer arrives alone | Nothing | None |
| 1. **Member referral** | An existing customer introduces someone they know | **Once, in grams, when the new customer qualifies** | None; terms of use only |
| 2. **Agent network** | A contracted, trained, disclosed agent | A share of the entry fee upfront, plus an ongoing commission that vests and can be clawed back | Agent Agreement |

Members and agents are kept strictly separate. **A one-off thank-you needs no contract; an ongoing income does.** Each customer can only be paid for once.

### 12.2 When a referral counts

> A referral counts when the new customer passes their own Confirmed SIP gate: six payments in a row, on their own account, under their own KYC, from a bank account in their own name.

Signing up, completing KYC or making a first payment does not count. Reusing the Confirmed SIP gate means the referral programme gets all its protections against gaming for free, and no reward can be paid until at least six months after signup. Comparable gold-savings products also wait for five or six payments.

The referrer is fixed when the account is opened and can never change, so referral credit cannot be traded.

### 12.3 The reward

> **30% of the entry fee the new customer paid over their six qualifying months, split equally between both people, credited in grams to both accounts on the day the gate is passed.**

The 30% is a placeholder, to be set with the agent rates once the revenue model is final. The rest of the design holds at any percentage:

- **Both people are paid.** Research shows referrals work better for unfamiliar products when both sides benefit, and "we both get gold" is a better conversation than "I get paid if you sign up".
- **Paid in grams from launch**, using the same gram-credit system as Gold Rewards.
- **No cap on the amount.** The reward is a fixed share of what the new customer actually paid, so it scales like a normal commission. Someone could pay large amounts for six months and then drop to the minimum, but they would still lose money on the round trip, and large payments trigger source-of-funds checks.
- **It also helps retention.** The reward lands at the new customer's sixth month, when savers are most likely to drop off.
- **No cap on the number of referrals.** VARA's own guidance shows a licensed firm paying referral codes with no maximum. Aurumix keeps the right to review anyone who is clearly running a referral business.
- **It does not pay back quickly.** A referred customer covers their reward after about nine to eleven months, and the whole calculation depends on the payment collection cost (section 14.6).

**Open decision:** launch the reward as designed (a thank-you), make it much larger and fund it from capital (to compete with bank referral offers), or record referrals at launch and set the reward later (which also removes it from VARA's approval timeline). The recommendation is the first option, announced at launch; in any version, no reward can be paid before about month 13.

### 12.4 One level only

> If A introduces B and B introduces C, A receives nothing from C. Ever, in any form.

Paying people for their referrals' referrals is what regulators treat as multi-level marketing. In August 2024 India's exchange regulator banned brokers from paying ongoing referral commissions to unregistered people; one-off referral bonuses survived. Every crypto scheme reclassified as a pyramid (Forsage, BitConnect, OneCoin, and the gold token Karatbars) turned on paying people for their downline. The UAE's pyramid-selling rules could not be checked at source, so the design simply avoids multi-level payments.

### 12.5 The agent network

The agent network has three levels, organised by role. A senior agent earns a supervision fee only for supervision actually done (training, compliance sign-off, first-line complaints), and only while the supervised customers are active and the work is documented. The recommended commission split pays the agent closest to the customer the most; the exact split is still to be confirmed.

The budget follows the Indian insurance model: **one overall acquisition budget, set as a share of entry-fee revenue, approved by the board and reviewed yearly**, with limits on paying commission upfront and any overspend borne by shareholders. Commission is clawed back if the customer sells out within 12 months. Agent rates are set once the revenue model is final.

### 12.6 The regulatory rules

VARA's Marketing Regulation applies directly:

- **VARA must confirm the referral programme** before it runs, so it goes into the licence application.
- No urgency or fear-of-missing-out messaging, and no time-limited bonus multipliers.
- Aurumix is liable for what referrers say, and referrers must disclose that they are paid.
- A reward in grams is treated the same as cash.
- The reward is always described as a share of a fee, never as a share of savings.

The design uses no leaderboards, badges or rising reward rates, and pays nothing for a referral that does not pass the gate. Referrers only share a code: they never place orders or give recommendations, which would require a broker-dealer or advisory licence.

---

## 13. Fees and revenue

### 13.1 The six streams

| # | Stream | Payer | Exists |
|---|---|---|---|
| 1 | Entry fee, charged once per purchase | The investor | Launch |
| 2 | Merchant interchange | The merchant | With the card |
| 3 | Family plan and beneficiary registration fees | The investor | Launch |
| 4 | Cardholder fees (FX margin, allowances beyond waiver) | The cardholder | With the card |
| 5 | Lending fees (origination, servicing, negotiated interest share) | The borrower | With the lending partner |
| 6 | **B2B platform fee**: partners distributing AURX through their own apps are invoiced monthly, in basis points on the assets their customers hold | The partner | With the first partner |

Three structural facts about the set. **No stream charges the exit** (section 7.1). **No stream bills the saver a recurring custody fee** (section 13.3). And the revenue model built in Phase 4 found the honest headline: the savings product is the funnel and the card and partner streams are where the economics concentrate, which is why the card is designed as credit and the register is built multi-tenant from day one.

### 13.2 The entry fee: what it has to cover

The entry fee is worked out from Aurumix's costs. On every contribution it has to pay for four things before Aurumix makes any margin:

| Cost | What it is | At launch |
|---|---|---|
| Bar premium | What the dealer charges above the gold price to make the bar | About 1.50% on 100 g bars |
| Pricing gap | The cost of setting the customer's price at the next LBMA fix instead of a live price (section 6.3) | About 0.79% |
| Float capital | The cost of Aurumix's own money tied up in the float | Small, falls as the business grows |
| Payment collection | What the payment provider charges per collection | About USD 0.25 per payment, to be confirmed |

At launch, with 100 g bars, these costs put the fee at **the top of the 2 to 5% range**. A 2% fee would lose money on every contribution, before any overheads.

**The fee can come down as Aurumix grows.** Bigger bars are cheaper: the premium falls from about 1.50% on a 100 g bar to about 0.95% on a 1 kg bar. As volumes grow and Aurumix moves to 1 kg bars, the fee can fall. Customers share in Aurumix's growth through lower fees, not through a payout.

**The tier discounts are affordable for the same reason.** Deeper discounts only reach customers after years of saving (section 9.2), and by then Aurumix's costs have already fallen.

**Two more points:**

- **The fee shown to the customer is not all margin.** Part of it pays the bar premium, so the fee disclosed and what Aurumix keeps are different numbers. Both are stated openly (section 5.3).
- **The payment collection cost decides the USD 20 minimum.** It varies by payment method, and the real price only comes from a signed contract with the provider (section 14.6).

### 13.3 Custody: no storage fee for savers

Allocated gold storage costs roughly 0.15 to 0.40% a year (the vault quote will confirm it). There is no good way to charge a long-term saver for it: a monthly cash bill keeps arriving after the customer stops engaging, taking grams would sell the customer's own gold and break the peg, and diluting the token would break 1 AURX = 1 gram.

**So savers never pay a storage fee, and their gold is never touched.**

### 13.4 Payment acceptance and the stablecoin position

The design accepts **bank money only**, into a segregated Client Account: never a token, never from an exchange's own account. The single test, applied at onboarding and at every payment: **whose bank account sends the money.**

Stablecoins are handled by signposting, not acceptance. UAE payment-token rules confine foreign payment tokens to registered issuers and to virtual-asset purchases; the widely held coins are not registered, the fee legs must settle in fiat regardless, and both tested workarounds fail (self-off-ramping is itself a licensable service; an embedded exchange widget makes the exchange Aurumix's agent). What works, on our reading: **the customer converts on their own account at a licensed exchange and pays by bank transfer.** Aurumix publishes a list of licensed venues, takes no fee, passes no data, never touches a token.

> **Open for counsel in this section:** both halves of Question 6. Whether publishing that exchange list counts as "arranging" a payment-token service (the one load-bearing assumption in the payment design), and whether e-money collection providers satisfy the client-money rules' requirement for "banks". The second decides whether small cross-border contributions are economically possible at all.

### 13.5 The partner channel

**What it is.** Other companies with their own customers, such as digital wallets, neobanks and payment apps, offer Aurumix gold inside their own apps. Their customers buy and hold AURX without ever opening an Aurumix account. Aurumix supplies the gold, the custody, the token and the licence in the background; the partner owns the customer relationship.

**How it works:**

1. **The partner signs and connects** to Aurumix's register and mint. Both are built from day one to hold several partners' books separately, so no partner shares a record with another or with Aurumix's own customers.
2. **The partner's customer buys gold in the partner's app** at one all-in price set by the partner.
3. **The grams are bought and held exactly as for a direct customer**: allocated gold in the vault, held in the trust, one AURX per gram. Partner customers get the same ownership protections.
4. **Aurumix invoices the partner every month** on the total gold its customers hold.

**How Aurumix earns from it.** The partner pays a **platform fee of about 0.50 to 0.75% a year** on the value of the gold its customers hold, modelled at 0.60%. For example, a partner whose customers hold USD 100m of gold pays about USD 600,000 a year. The fee covers the cost of storing that gold (around 0.25% a year) plus Aurumix's margin, and it keeps coming in every month without Aurumix having to win a new sale. The partner keeps most of the entry fee its customers pay; Aurumix's income from this channel is the platform fee alone. The fee rate is our estimate until the first partner contract sets it.

**Why it matters.** It is the only income line that grows directly with the amount of gold held. Aurumix does not pay to acquire each partner customer, because the partner brings them. The cost sits elsewhere: finding, signing and integrating each partner, which takes sales effort, technical work and up to 18 months before the partner is fully live, and giving up most of the entry fee to the partner. The Phase 5 simulations found that partners make up about 31% of year-seven revenue, from a small number of contracts, and are the strongest single driver of whether Aurumix becomes profitable. Each partner takes time to grow: it is modelled to reach full size about five years after it goes live.

**No ICS for partner customers.** Partner customers have no score, no tier and no tier benefits. Aurumix cannot see their payment behaviour (the partner handles payments), the benefits are not Aurumix's to give on that book, and the Gold Rewards cap would not work. The partner agreement states this explicitly.
---

## 14. Assumptions register and open legal questions

### 14.1 The questions at a glance

| # | The question, in plain terms | What it decides | Priority |
|---|---|---|---|
| 1 | Does owning the token mean owning the gold? | The whole product, the token, the capital needed, the marketing | Blocking |
| 2 | Is the customers' gold safe if Aurumix goes bust? | The trust structure and the safety promise to savers | Blocking |
| 3 | Do VARA's buyback rules mean what we think? | The cost of every exit, and loan default recovery | Blocking |
| 4 | Is the trust an investment fund, and does its trustee need a licence? | Whether the DIFC structure is affordable | High |
| 5 | Can a lender take a legal claim on pledged gold? | The credit line and the Gold Card | High |
| 6 | Is the payment setup allowed? | Collecting money from abroad, and the stablecoin position | High |
| 7 | How can the family product be offered lawfully? | Whether the family feature launches, and its name | High |
| A | Can Indian residents take part? | The size of the market | Indian counsel |
| B | Is the distribution model lawful? | The agent network and referrals | High |
| C | Which countries beyond the UAE can we serve? | Every market after launch | Before each market |

**If only three questions could be asked, ask 1, 2 and 3 first.**

### 14.2 The three questions that decide whether the product works

#### Question 1: Does owning the token mean owning the gold?

- **What we assumed.** A trust in the DIFC is the legal owner of the gold on paper. Its deed says it holds the gold for *whoever holds AURX at any moment*. So when a customer sends AURX to someone else, ownership of the gold moves with it automatically, with no paperwork.
- **Why it matters.** VARA requires the issuer to prove two things: that the customer really owns the gold, and that ownership moves with the token. This is the most important open point in the project.
- **What we need counsel to confirm, as three separate answers:**
  - Can a trust define its beneficiaries as "whoever holds the token"?
  - Can the trust deed remove the usual rule that a beneficiary must sign a written document to pass on their interest? (English law does not allow this; DIFC law appears to.)
  - If yes to both, does that satisfy VARA?
- **If counsel says no.** AURX becomes a token that only verified, registered customers can hold. The token is built so this is a setting change, not a rebuild. The cost: AURX can no longer trade freely or be listed openly.
- **If direct ownership fails altogether.** A much heavier VARA regime applies, including extra capital that could approach USD 4 million at the Year 10 target, and the marketing has to change from "you own gold" to "you have exposure to gold".

#### Question 2: Is the customers' gold safe if Aurumix goes bust?

- **What we assumed.** Gold held in the DIFC trust cannot be taken by Aurumix's creditors, even though customers own a share of a pool of bars rather than specific bars.
- **Why it matters.** It is the core safety promise to savers. It is also the reason the trust exists: VARA's rule protecting customer assets in an insolvency is written for virtual assets (tokens), and gold bars are not virtual assets. Onshore UAE law gave us no clear answer on whether pooled gold can be recovered from a bankrupt company.
- **What we need counsel to confirm:**
  - Can gold that is allocated to customers but pooled be recovered from an onshore UAE bankruptcy?
  - Does the DIFC trust genuinely improve that position?
  - Would a UAE court honour VARA's insolvency protection for physical gold at all?
  - Is the DMCC Tradeflow record a legal document of title, or only a contract with DMCC? (The design treats it as supporting evidence, not the foundation.)
- **If counsel says no.** We cannot tell savers their gold is safe if Aurumix fails, and the ownership structure has to be redesigned. ADGM is not a simple swap: under an ADGM foundation the customer would own nothing until the gold is paid out.

#### Question 3: Do VARA's buyback rules mean what we think they mean?

VARA says that where a token gives holders a right to redeem, the issuer may charge **no fee of any kind** on redemption. The rulebook never defines "redemption", so three things need confirming:

- **Is the buyback a "redemption"?** We assumed yes, and designed for it: there is no exit fee at all. We would like VARA to confirm this in writing before the application.
- **What does "equal value" mean?** We assumed the customer gets the full gold price, not the lower price a dealer would pay. If counsel reads it the other way, the payout is still fine, but the cost assumption behind every exit changes.
- **Is selling a borrower's gold after a loan default caught by the no-fee rule?** We assumed not. If it is, Aurumix cannot charge the borrower its recovery costs.

### 14.3 The questions that decide individual features

#### Question 4: Is the trust an investment fund, and does its trustee need a licence?

- **What we assumed.** The trust is not a fund, because the gold earns no income, is not actively managed, and each customer's share is fixed. A trustee company running only this one trust may not need a DFSA licence.
- **Why it matters.** A fund carries far heavier rules and cost. This is one of the main reasons the client's profit-sharing dividend was removed: bringing it back would bring this question back, and could bring the securities regulator in too.
- **Also needed, a practical ask rather than a legal one:** an indicative cost to set up and run the DIFC trust each year. The client cannot make a build decision without a number.

#### Question 5: Can a lender take a legal claim on a customer's pledged gold?

- **What we assumed.** The lender can register a valid claim under DIFC law over the customer's share of the trust. Aurumix valuing the gold, acting as the lender's agent and buying the gold on a sale, all at once, is acceptable if disclosed.
- **What we need counsel to confirm:**
  - Can the claim be validly taken and registered, and how?
  - Does AURX count as a "digital asset" under DIFC law? It changes how the claim is taken.
  - Is Aurumix's triple role acceptable with disclosure, or must an independent party take one of the roles (which adds cost to every loan)?
- **If counsel says no.** The credit line and the Gold Card do not work as designed, and the benefit ladder has to be rethought.

#### Question 6: Is the payment setup allowed?

- **Overseas collection.** VARA says money from overseas customers must sit with third-party **banks**. The providers that collect small payments abroad are usually e-money firms, not banks. **Does that count?** If not, collecting small monthly payments from outside the UAE may not be economic, and the market shrinks to people who can pay from a UAE bank account.
- **Stablecoins.** Aurumix accepts bank money only. Customers who hold stablecoins convert them at a licensed exchange and pay by bank transfer. We plan to publish a list of licensed exchanges, with no fee and no data shared. **Does publishing that list count as "arranging" a stablecoin service?** This is the one load-bearing assumption in the payment design.

#### Question 7: How can the family product be offered lawfully?

- **We have no position on this one; it is an open question.** No VARA licence covers wills, estates or trust services.
- **What we assumed.** The family transfer works as a standing instruction on the customer's account, not as will-writing, estate administration or acting as a trustee.
- **What we need counsel to answer:**
  - Can it sit outside those licensed activities, and if not, what licence or partner is needed?
  - Are there customer groups or countries where it cannot be offered?
  - Does the name "Digital Will" on its own imply a regulated service?
- **A related point to raise: domicile.** Many Gulf-based Indians remain legally domiciled in India, and an Indian court could apply Indian inheritance law to their gold. We recommend asking for a domicile declaration at onboarding.
- **What does not need a lawyer:** probate cannot be avoided on death. That is already settled in the design; the product speeds probate up rather than replacing it.

### 14.4 Market and distribution questions

#### A. India (for Indian counsel)

- **What we assumed.** Indian residents cannot take part. Gold abroad is not something they are allowed to buy under India's Liberalised Remittance Scheme, and a separate rule closes the GIFT City route too. The client's original "USDT via P2P" route for Indian residents was removed.
- **Why it matters.** We changed the target customer on the strength of this. If we are wrong, the market is much larger.
- **What we need counsel to confirm:**
  - Can an Indian resident lawfully pay in monthly? Is there exposure for Aurumix in accepting them or marketing to them, including through agents?
  - When a customer dies and the beneficiary lives in India, can we pay them in cash instead of transferring tokens? (This is our design.)
  - A customer who moves back to India keeps their gold but cannot add money. Is that right?
  - Lifetime gifts to relatives in India are blocked at launch, because the rules turn on the giver's passport. Is that more cautious than it needs to be?

#### B. The distribution model

- **Is the three-level agent network lawful in the UAE?** We could not retrieve the UAE's anti-pyramid law. Member referrals are single level for that reason; the agent network still has three levels, organised by role rather than recruitment.
- **Do agents need a licence?** Agents help people sign up and keep saving, which could look like "arranging" or "advising".
- **Do referrers need a licence?** We assumed not, because they only share a code and never place orders or give advice.

#### C. Countries beyond the UAE

- VARA gives a test, not a list: serve customers only where the activity is allowed locally, and meet the stricter of the two sets of rules.
- **Each new market needs its own local legal advice before any marketing there.**

| Country | Our reading | What is needed |
|---|---|---|
| UAE | Open at launch | VARA licence |
| Oman | No crypto regime in force. A gap, not a permission | Local counsel |
| Bahrain | Needs central bank approval, local capital and a locally licensed distributor | Local counsel and approval |
| Saudi Arabia, Kuwait, Qatar | Blocked at the banks | Not a launch market |
| UK, Singapore, Canada, Australia | Each needs its own licence | Not a launch market |
| India (residents), United States, FATF blacklist | Excluded | None |

### 14.5 Smaller points for a second batch

These follow from the main answers. Several will answer themselves once the questions above are settled.

- Could VARA still require the extra capital of 2% of gold held, even though a direct-ownership token has no "reserves" in VARA's sense? Potentially several million dollars.
- Does the buyback also need an exchange or broker-dealer licence on top of the issuing licence?
- **VAT:** does the entry fee, the gold or the services attract 5% VAT? The entry-fee margin is thin, so this needs a tax adviser early.
- How does the mandatory wind-down plan work alongside the DIFC trust?
- Gold Rewards moves Aurumix's own gold to a customer. Does it need the same ownership mechanism as a purchase, and can rewards be credited to an account that is blocked for compliance reasons?
- The age of majority for beneficiaries moved to 18 in 2026, and sources disagree on which law enacted it. Confirm before it is built into the app.

### 14.6 What neither we nor counsel can answer

| Item | Why it matters | Who resolves it |
|---|---|---|
| The two-way bullion dealer | The float, the buyback and the fee level all depend on one | The client, by negotiation |
| The vault price | Decides how comfortable "no storage fee" is | The client, by quote |
| The monthly payment collection cost | Decides whether the USD 20 minimum works | The client, by contract with a bank or payment provider |
| The card revenue share | Gold Rewards needs roughly 36% of card interchange | The client, by negotiation with the card partner |
| The VARA approval date | VARA publishes no timeline | Nobody. Never give investors a firm date |

---

## 15. Risk and adversarial analysis

Each risk is stated with its mitigation and its residual. The design convention throughout has been to surface the uncomfortable number rather than smooth it.

### 15.1 Counterparty risk: the unnamed dealer

The single largest execution risk. The buyback promise runs entirely through a counterparty that does not yet exist in the plan (section 6.6). Mitigations: the float decouples daily operations from dealer timing; the sourcing covenant pre-authorises substitution; the exit's settlement windows are sized to the float, not the dealer. Residual: until a dealer signs, the fee build-up and the buyback capacity are specified but not calibrated. This risk is named to the client as a project risk.

### 15.2 Insolvency and custody risk

The threat: Aurumix fails and the customers' gold is trapped or taken. Mitigations are the four ownership layers (3.5.1), the client-money and client-asset estate exclusions (3.6), the segregation of the float from customer metal, and the wind-down plan with client-asset sales excluded (3.8). Residuals, honestly held: the onshore reclaim question for fungible gold is unresolved (Question 2), the title register is contract-backed rather than statute-backed (2.5), and an onshore court's treatment of the DIFC arrangement in a contested insolvency is untested. The layered design exists precisely so that any single failure leaves the claim standing.

### 15.3 Regulatory risk

- **Recharacterisation of the exit or the family fees as fee-bearing redemption** (III.E.4). Mitigations: no fee touches any exit path; the family fee strikes at registration; in-specie is the only paid succession service. The in-specie/redemption split goes to VARA in writing pre-application.
- **Reclassification of the token as a security.** Mitigations: no profit share, no yield language, no premium marketing, no scarcity mechanics, benefits earned by behaviour and capped at customer-generated revenue. The dividend stays dead; its deletion also protects the fund analysis (3.5.3).
- **The class-defined trust failing at counsel.** Mitigation: the proxy and hook make the permissioned fallback a switch, not a rebuild (4.4).
- **Marketing breach through the referral or agent channel.** Mitigations: single level, incentive pre-approval inside the licence application, disclosure duties, the liability rule internalised (12.6).

### 15.4 Market risk

- **Discount risk.** A thin listed market would price AURX below metal value (the two-discount-case evidence). Mitigation: no listing until the float is deep; the committed buyback is the floor.
- **Redemption run.** Section 7.4's machinery: tiered disclosed windows, the float, staged dealer sales, the suspension right bounded to force majeure. The structural comfort: the customers own the metal, so a run on Aurumix is not a run on their gold.
- **Gold price risk.** Carried by the customer as the product's nature; carried by the treasury only across the fill window (mean-zero, bounded); carried by borrowers only when they borrow (10.4).

### 15.5 Credit risk

Sits on the lender of record by structure. Aurumix's residuals: the stand-in authorisation hole (bounded by static rules and disclosed to the lender), the auth-to-settlement gap (closed by the 48-hour redemption hold), Sovereign borrowers' one-sigma exposure (disclosed, cured in stages), and the valuer/agent/buyer conflict (cured by zero-discretion pricing at the fix, and put to counsel as Question 5's third limb).

### 15.6 Behavioural and gaming risk

The anti-gaming register (8.7) closes six of eleven attacks structurally; the credit prize is de-fanged by seasoning plus strike-at-facility; the round-trip flag catches the residue with review rather than automatic punishment. Two consciously accepted residues, priced rather than policed: the referee contribution-collapse pattern (12.3) and the ballast-plus-small-SIP cycler (8.7). The acceptance and its trigger for reopening are recorded so neither resurfaces as an oversight.

### 15.7 Payment rail risk

Push-only collection removes bounce fees and mandate risk but leaves two dependencies: the Request to Pay origination cost (14.6) and the e-money/banks client-money question (Question 6). If the second fails, cross-border collection shrinks to wire-viable tickets, which is a material market change and would be known before launch rather than after.

### 15.8 Operational and continuity risk

The invariant set halts minting before any unbacked state can arise (6.5); attestation currency is a mint precondition, not a reporting nicety; the register and mint are multi-tenant from day one so partner books do not share a single point of failure with the direct channel; and the wind-down plan is drafted against the real mechanics (claim window, burn-on-redemption, freeze role, the monthly cash touchpoint as the contact rail). The known hard constraint on the launch build: real-time card authorisation (10.3).
---

## Appendix A: Glossary

| Term | Meaning |
|---|---|
| Allocated gold | Specific, serial-numbered bars held for token holders, as opposed to an unallocated claim on a provider |
| AANI | The UAE instant-payments platform; Request to Pay is its collection feature |
| ARVA | Asset-Referenced Virtual Asset, VARA's category for tokens referencing an asset such as gold |
| AURX | The Aurumix token; 1 AURX = 1 gram of gold |
| Beneficiary Transfer Instruction (BTI) | The standing, pre-authorised instruction implementing the succession feature |
| Beneficial interest | Real economic ownership held through a trustee: the trustee is the owner on paper, the beneficiary is the person the asset is held for |
| Blocklist | A transfer control that denies listed addresses by exception; the opposite of an allowlist |
| Burn | Destroying tokens, done on every exit so supply always matches the metal |
| Confirmed SIP | The gate: six consecutive counted contributions; permanent once earned |
| Counted period | A calendar month in which one accepted contribution at or above the floor cleared |
| DIFC | Dubai International Financial Centre, a common-law jurisdiction outside VARA's remit |
| Entry fee | The one-time percentage fee on each purchase; the product's primary revenue line |
| ERC-20 | The standard token format on Ethereum; the form every wallet, exchange and application already supports |
| Grant of probate | The court document confirming who is entitled to administer and receive a dead person's property |
| Interchange | The percentage of every card purchase paid by the merchant's side to the card issuer's side; funds the card benefits and Gold Rewards |
| The fix | The LBMA gold price, the pricing benchmark for every event |
| The float | Aurumix-owned working gold inventory bridging retail tickets to wholesale bars |
| Gold Rewards | The monthly fee rebate credited in grams, capped at customer-generated revenue |
| ICS | Investor Conviction Score: min(Record, Standing) x Retention, 0 to 100 |
| JIT funding | Just-in-time authorisation: each card tap is approved live against collateral headroom |
| KYC | Know-your-customer identity verification, required at onboarding and at redemption |
| Mint | Creating new tokens, done only against newly allocated gold |
| LTV | Loan-to-value: drawn balance against pledged collateral value |
| Option A | The direct-ownership ARVA branch: the customer owns the gold itself |
| Record / Standing / Retention | The score's three inputs: contribution history, trailing-12 discipline, and the kept-gold multiplier |
| Regulatory pause | The automatic state in which refused money never scores against the customer |
| SIP | Systematic investment plan: the monthly savings instruction |
| Sovereign | The top tier: a perfect year, on a complete record, with the gold intact |
| Tier of record | The tier computed at the account's last period resolution; the only tier any benefit reads |
| Tradeflow | DMCC's electronic title register for vaulted commodities in Dubai |
| VARA | Dubai's Virtual Assets Regulatory Authority |

---

## References

Primary sources, verified verbatim during the design and held in the project record:

1. VARA Virtual Asset Issuance Rulebook, 19 May 2025, including Annex 2 (ARVA Rules) Parts III.B, III.C and III.E.
2. VARA Guidance on VA Issuance, Version 1.
3. VARA Company Rulebook: Client Money Rules (Part IV), Client VA provisions (Part V.B), Wind-Down Plan (Part VII.A).
4. VARA Marketing Regulations, Part I.C, and the referral case study in the accompanying guidance.
5. VARA Custody Rulebook IV.B.2 (pre-authorised client instructions).
6. DIFC Trust Law, DIFC Law No. 4 of 2018: Arts 14(2), 34(2), 45, 47, 48(4)(a), 60, 66, 69.
7. ADGM Foundations Regulations 2017: ss. 29, 30, 31.
8. DIFC Law of Security, DIFC Law No. 4 of 2024.
9. CBUAE Payment Token Services Regulation (Circular 2/2024); Retail Payment Services and Card Schemes Regulation (Circular 15/2021); Finance Companies Regulation.
10. Visa UAE Interchange Reimbursement Fee schedule, effective 18 October 2025; CBUAE Notice 1998/2024.
11. IFSCA Circular 329/IFSCA/DPM/TS/2022-23/1 (17 June 2022); FEMA s.6(4) and the Overseas Investment Rules Schedule III; Income-tax Act ss. 115BBH, 194S.
12. IRDAI (Expenses of Management, including Commission, of Insurers) Regulations 2024 and Master Circular of 15 May 2024.
13. ENBD Personal Banking Schedule of Charges (November 2023); Al Etihad Payments / CBUAE publications on AANI.
14. The Phase 1 market research record: nineteen-protocol landscape, 292 sources (Aurumix Protocol Landscape).

The full Phase 2 record (eleven decision drafts, the 51-entry decision log, sixteen process map sets, and the two verified statute texts) is available to counsel on request.
