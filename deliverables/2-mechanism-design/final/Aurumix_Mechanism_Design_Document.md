# Aurumix: Mechanism Design Document

## Gold-backed savings infrastructure under VARA

**Prepared by:** Tokenomics.net
**For:** Aurumix project team and counsel
**Date:** 8 September 2026
**Version:** 1.0
**Status:** Consolidated design record. Supersedes the individual Phase 2 decision drafts as the single reading copy; the drafts remain the detailed audit trail.

---

## How to read this document

This document describes the complete Aurumix mechanism design: what the product is, how every mechanism works, the legal structure it sits on, the assumptions each part rests on, and the questions that remain open for counsel. It is written so that a reader with no prior exposure to the project, including a lawyer instructed for the first time, can understand the entire product from this document alone.

Three conventions are used throughout.

- **Decisions are shown with their reasoning.** Where the design departs from the client's original specification (the 100 G Business Model), the departure is stated openly and the reason given.
- **Assumptions are labelled.** Where a mechanism rests on a reading of law that counsel has not yet confirmed, the assumption is stated as a proposition that is either true or false, with a confidence level where research supports one. Section 14 is the consolidated register. The companion document `Aurumix: Design Summary and Open Legal Questions` (19 August 2026) puts the seven highest-value questions to counsel directly; this document carries the design behind them.
- **Legal references are to primary sources.** The load-bearing rules were verified verbatim against the VARA rulebooks, the DIFC statutes and the CBUAE rulebook, and are cited precisely. Verified source texts are held in the project record. We are consultants, not lawyers: a citation here records what we read and where, and never substitutes for advice.

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
References and document control

---

## 1. Introduction and market context

### 1.1 The product in one sentence

Aurumix is a gold-backed savings product, issued from Dubai under a VARA licence, in which 100% of every dollar received buys allocated physical gold, one token equals one gram, a monthly savings plan starts at USD 20, and disciplined saving, never the amount saved, earns a rising ladder of benefits: cheaper entry, a credit facility against the gold, a payment card, rewards paid in grams, and family succession services.

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
| Closed | India (residents) | Multiple independent bars. Section 14.5 and Appendix A of the legal brief |
| Reachable, each needs its own licence | UK, Singapore, Canada, Australia | Not launch markets |
| Excluded | United States, FATF blacklist jurisdictions | Deliberate |

Two consequences are worth stating early. First, the primary customer is the UAE-resident South Asian saver, with Oman as the first expansion market. Second, Indian residents cannot be onboarded, and the product carries an explicit blocked-country list rather than an implicit "anyone not named" default.

### 1.4 What the market does not offer

The market research phase examined nineteen tokenised-gold protocols plus the leading digital-gold and vaulting services. Three findings shape this design.

**Not one of nineteen protocols has a savings plan, a recurring purchase, or a retail referral programme.** The category is built for traders and treasuries. Distribution to savers is unoccupied ground, and the one documented gold-token failure post-mortem (PMGT) names zero distribution as the cause of death.

**The category offers no behaviour-based benefits at all.** PAXG and XAUT carry no holder-level state by design. The only tiering anywhere in the set is by order size, which is capital: precisely the shape this design refuses.

**Tokens in this category die of revenue starvation, not regulation.** PMGT charged no fees and had no internal advocate. Digix zeroed its own fee and lived off its treasury until holders voted it away. The counter-example worth copying is DGLD, where holders own the gold outright at law, which is why six years of dormancy harmed nobody. Aurumix takes both lessons: real fee lines from day one, and customer ownership strong enough to survive the issuer.

### 1.5 Protocol overview

The design in one view:

- **Asset layer.** Allocated, serial-numbered gold bars from LBMA-accredited refiners, vaulted in Dubai, recorded bar by bar, owned through a DIFC trust structure for the benefit of token holders (section 3).
- **Token layer.** AURX, an open ERC-20 with a blocklist, 1 token = 1 gram, identity verified at mint and at redemption, freely transferable in between (section 4).
- **Purchase layer.** Two transaction types on one account: a monthly SIP from USD 20 and on-demand spot purchases. Money, then title, then token, on every purchase (section 5).
- **Treasury layer.** A gold float bridges retail ticket sizes to wholesale bar sizes and absorbs exit flow (section 6).
- **Exit.** Cash buyback at the next LBMA fix, no fee of any kind, by rule and by design (section 7).
- **Scoring layer.** The Investor Conviction Score measures saving behaviour, never amount, and prices five benefits (sections 8 and 9).
- **Credit layer.** One gold-secured revolving facility with a cash channel and a card channel, delivered through licensed partners (section 10).
- **Family layer.** A Family Portfolio and a standing Beneficiary Transfer Instruction, operating on custodied gold (section 11).
- **Distribution layer.** A single-level member referral programme and a contracted three-tier agent network (section 12).

Every mechanism in this stack was designed against two fixed constraints: the entry ticket is USD 20, and the benefit rate may never scale with capital. Where those constraints forced a departure from the client's original specification, each departure is stated where it occurs, with its reason.

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

**"LBMA" means two different things, and the distinction is worth a lawyer's attention because the client's specification conflates them.** An LBMA Good Delivery bar is a ~12.4 kg wholesale unit worth over a million dollars; Aurumix will not hold them at launch. A bar from an LBMA-accredited refiner is a 100 g or 1 kg bar freely available in Dubai. The accurate claim, used throughout: **99.99% gold from LBMA-accredited refiners, held in allocated bars.** UAE local refiners carry UAEGD accreditation, a separate voluntary standard, and are not automatically LBMA-accredited.

**Sourcing is a live risk, not a theoretical one.** Emirates Gold DMCC was suspended from both the UAEGD and LBMA lists in July 2023. A design that names a single refiner without a substitution clause would have broken its core promise overnight. The sourcing covenant therefore uses multi-list wording (LBMA / DMCC / LPPM) so substitution on suspension is pre-authorised.

### 2.2 Denomination: 1 AURX = 1 gram, permanently

The token count is the gram count. This was changed from the client's 0.01 g specification, one of the items the client delegated.

- One number, not two. "7.820 AURX = 7.820 g" needs no explanation to a customer who already buys gold by the gram.
- The backing invariant reads directly off the two ledgers with no conversion factor, and a retail holder can verify it unaided.
- It matches every gram-denominated product in the comparable set (Comtech, Aurus, Digix, CACHE).
- Fractional purchases are a display question, not a denomination question. The ERC-20 standard's 18 decimals mean a USD 20 contribution buys a precise fraction of a token. Indian digital-gold products already display gram holdings to four decimals at mass scale.

The Indian convention of quoting gold per 10 grams is a price display convention. The app quotes per 10 g where the audience expects it; the token stays at 1 gram.

One consequence follows immediately: **the ratio is fixed, so nothing may ever erode the gram count.** Fee-by-dilution (the PAXG mechanism) and deduction of fees in grams are both excluded by construction. The custody cost is recovered elsewhere (section 13.3), and the governing customer promise is: you can lose your status, you can never lose your gold.

### 2.3 Pricing: one rule, three events

Every price in the product is struck the same way: **the price is always the next LBMA fix that nobody has seen yet.**

| Event | Priced at |
|---|---|
| Purchase (SIP or spot) | First fix after cleared funds |
| Exit | Next fix after the redemption request |
| Gold Rewards gram credit | Next fix after period close |

The reasoning is the removal of free options. Any rule that lets either side choose between two known prices hands that side a one-directional option on the gold price. Striking at the next unseen fix removes the option from both sides at once, and the same convention covers every price event in the product.

The published price formula in the client's document (`price = vault gold x fix / tokens outstanding`) is retained as a **verification identity**: it is what a holder uses to check that supply still equals metal. It is not the price definition. Under fixed weight, the price of one AURX is simply the fix per gram.

### 2.4 The premium is zero, and is modelled at zero everywhere

The client's specification assumed AURX would trade at a 3 to 8% premium to the gold price, and built a scarcity mechanism to support it. Both are removed, on evidence:

- In a liquid market, arbitrage closes any premium: XAUT (~USD 2.5bn) and PAXG (~USD 1.8bn) both trade at the gold price.
- In an illiquid market there is no price in which to express a premium.
- The two protocols that restrict their exit the way the original design did (Midas XGZ, ORO) trade at a **discount**. Restricting arbitrage does not create a premium; it removes the price floor.
- Even if a premium existed, it would accrue to secondary-market sellers, not to Aurumix, and the exposure is one-directional: above net asset value holders sell to each other, below it they all redeem at once.
- A marketed premium gives a regulator an expectation of profit from the promoter's efforts, which contradicts the asset-referenced classification the whole structure depends on.

The scarcity layer (capped, time-boxed, oversubscribed "Mining Events") is deleted with it. A capped, priority-queued sale is offering-shaped and points at securities characteristics; continuous minting at net asset value against the buyer's own gold is commodity-purchase shaped and sits cleanly in the ARVA lane. What survives of the Mining Event is its real function, treasury batching, which becomes an internal procurement cycle (section 6).

### 2.5 Custody and the ownership record

Physical custody and legal ownership are two different problems, and the design separates them deliberately.

**Physical custody** is a vault contract: allocated, serial-numbered bars, segregated from Aurumix's own metal, with an independent assay on intake and a monthly Allocation Report publishing bar serials, assay certificates and both ledger balances. The recommended vault is Brink's Global Services DMCC, which has the useful property that the recommended lending partner already lends against gold held there (section 10.3).

**Legal ownership** runs through the structure in section 3. One honest disclosure belongs here because it shapes the marketing: a USD 75-a-month saver can never own a specific bar. After a year they hold under 1% of a kilobar. The accurate description of what a customer owns, used in every document, is an **individually recorded, pro-rata undivided interest in identified, serial-numbered bars**. "100% individually allocated" would overstate it; "not a pooled allocation" (the client's wording) overstates it too. The pool itself is allocated and customer-segregated; each customer owns a recorded share of it.

**The title record.** The preferred independent record is a DMCC Tradeflow warrant: an electronic record, maintained by DMCC as registrar, of which bars sit in which approved vault for which owner, transferable and pledgeable on the platform. Its honest limits: DMCC's own framework calls a warrant an electronic document of title, but that claim rests on DMCC's contract framework rather than a naming statute, and no court has tested it. The design therefore uses the warrant as one evidentiary layer among several, never as the foundation (section 3.5). Whether Tradeflow supports the sub-account structures Aurumix would want is an open commercial question for DMCC.
---

## 3. Legal structure and regulatory frame

This section is the load-bearing wall. Every mechanism in sections 4 to 13 either inherits a rule stated here or is shaped by one.

### 3.1 The regulatory map

Four regulators are in frame, and the boundaries between them decide what is built versus partnered.

| Regulator | Covers, for Aurumix | Consequence |
|---|---|---|
| **VARA** (Dubai Virtual Assets Regulatory Authority) | Issuing AURX, the whitepaper, marketing, client money and client virtual assets | The core licence. VARA's remit covers the Emirate of Dubai including free zones, **excluding DIFC**, so the issuer cannot sit in DIFC |
| **CBUAE** (Central Bank) | Lending against pledged gold, card issuance, payment services, payment tokens | Both credit and card run through CBUAE-licensed partners. Aurumix builds neither |
| **DFSA** (DIFC) | The DIFC trust vehicle and its trustee, security over DIFC-law interests | The title-holding structure lives here, outside VARA's remit by design |
| **SCA** (federal securities) | Engaged only if a profit share is issued to holders | The design keeps it out of frame by keeping the profit-share dividend dead (section 9.5) |

Perimeter regulators for expansion (CBB for Bahrain, the Oman FSA, RBI / SEBI / IFSCA for India) enter country by country and are treated in sections 1.3 and 14.5.

### 3.2 The classification choice: direct-ownership ARVA

VARA's issuance guidance uses gold as its worked example and splits gold-referenced tokens into two regimes. The choice between them determines the licence file, the capital requirement, the marketing story and most of the legal work.

| | **Option A: direct-ownership ARVA (chosen)** | Option B: stable-value ARVA |
|---|---|---|
| What the customer owns | The gold itself | A claim whose value tracks gold |
| Reserve Asset regime | **Does not apply.** Verified against the rule text: Annex 2 III.C opens "VASPs Licensed to issue ARVAs **which purport to maintain a stable value**...", so the regime attaches to the stable-value branch only | Applies in full: licensed custodians, segregation, no rehypothecation, regular attestation, a supporting legal opinion |
| Capital | AED 1,500,000 minimum | AED 1,500,000 **or 2% of average Reserve Asset value over 24 months, whichever is higher**. At the Year 10 target that could approach USD 4M of locked capital |
| The binding burden | **Annex 2 III.B.1: prove the right of ownership is legally and validly established and that it transfers with the token** | Hold, segregate and attest the reserves |
| Fit with the product | The Individual Gold Receipt is this option | Silently deletes the Gold Receipt: a claim holder is a creditor |

Option A was chosen for three reasons in ascending order of force: it is the product the client believes he is building; it removes the heaviest ongoing compliance regime in the rulebook; and the capital arithmetic is worth several million dollars. The price of the choice is the proof obligation in III.B.1, which section 3.5 is built to satisfy, and which is Question 1 of the legal brief.

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

Two claims previously carried in working drafts are corrected here, because both would be noticed in a filing: the Restricted Licence route fails on the per-borrower cap, not on a collateral-lien exclusion; and "the CBUAE reserves the sole right to issue BINs" is unverified, with the binding constraints appearing to be scheme membership plus RPSCS licensing.

A separate CBUAE Non-Objection Registration is reportedly required for VARA licensees that custody, transfer or convert stablecoins (Confidence: Medium, commentary rather than rulebook). The design avoids touching stablecoins at all (section 13.4), which keeps this out of the critical path.

**Indicative cost to reach launch:** roughly USD 550,000 to 750,000 of capital and fees before any build cost, over six to nine months minimum. VARA publishes no approval timeline anywhere, so no date should ever be given to investors as anything firmer than an estimate.

### 3.4 The entity map

Four things to stand up, of which only two are companies to build now.

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

This is the design's answer to Annex 2 III.B.1, and it is the part of the structure counsel should read most carefully. It was rebuilt once, and the rebuild matters, so both the current design and the reversal that produced it are stated.

#### 3.5.1 The layered claim

Four independent layers each assert that the customer owns the gold, so no single failure collapses the claim:

1. **Allocated, never unallocated.** Serial-numbered bars with a weight list. An unallocated holder is an unsecured creditor; an allocated holder owns property. This is the decisive layer.
2. **Trust and bailment language in the customer terms.** Title sits with the trustee for the benefit of holders; the customer holds a beneficial interest; the terms say so in words a court can apply.
3. **The DIFC trust vehicle.** DIFC Trust Law 2018 Art 14(2): a transfer into a trust is not void or voidable by reason of the settlor's later bankruptcy. This statutory protection is why the metal is held through DIFC rather than onshore: onshore UAE law could not give a verifiable answer to whether allocated but fungible gold can be reclaimed from a bankruptcy estate (the pivotal open item in section 14).
4. **An independent title register** (the Tradeflow warrant, held by the vehicle), as evidence beyond Aurumix's own systems.

#### 3.5.2 The class-defined trust: how ownership moves with the token

The trust deed defines its beneficiary class as **the holders of AURX from time to time**, ascertained by reference to the token ledger. A holder's beneficial interest arises on receiving tokens and terminates on sending them, by the deed's own terms. Nobody assigns anything; the class shifts, exactly as the deed says it will.

The construction rests on four legs of the DIFC Trust Law 2018, each verified verbatim against the statute text held in the project record:

| Leg | Provision | What it supplies |
|---|---|---|
| A class is a valid beneficiary definition | Art 45(1)(b)(i); Art 34(2) (definite if ascertainable now or in the future) | A token ledger makes the class ascertainable to the exact address at every block |
| The class may shift | Art 45(2) (terms may provide for addition and exclusion); Art 48(4)(a) (an interest may cease on ceasing to be a member of the class) | The statute expressly contemplates entry and exit by class membership |
| The writing formality is displaceable | Art 47(2): "**Subject to the terms of a trust**, a beneficiary may, by instrument in writing... deal with his interest" | The deed can displace the writing default. The English analogue (LPA 1925 s.53(1)(c)) is mandatory; DIFC's is not, and that difference is why DIFC is the right jurisdiction |
| Disclosure is pull, not push | Art 66(1) (trustee discloses on written application by a beneficiary) | The trustee is never required to hold a proactive list of every holder |

Under this construction, VARA's III.B.1 is satisfied structurally rather than operationally: because the class follows the ledger, **divergence between the token ledger and the ownership position is impossible by construction**, which is a stronger answer to III.B.1.c ("implement mitigating measures to ensure all transactions in the ARVA result in a corresponding transaction in the Reference Asset") than any monitoring regime. III.B.1.b is conditional ("**where** transactions in the Reference Assets are subject to legal or regulatory requirements relating to... transfer of title"): the underlying transaction is a shift in beneficial interest governed entirely by the deed, so there is no external formality to satisfy. The bar itself never changes owner; the vehicle holds it on day one and on day ten thousand.

**The one-sentence version:** the DIFC vehicle was chosen to protect the customer's gold from Aurumix's creditors, and it turns out also to be what lets the token move freely, because gold that never changes owner never has to be re-registered when the token changes hands.

#### 3.5.3 What this construction replaced, and why the record matters

The earlier design (and several superseded working drafts still describe it) required a **permissioned token**: every holder named in a register, transfers only between registered holders, no open listing. That requirement was traced to two sources, and on verbatim verification **both readings failed**:

- DIFC Trust Law Art 60(6) was read as a duty to identify every beneficiary. It is not: Art 60 is headed "Duties of trustees", and 60(6) is an AML / beneficial-ownership duty aimed at corporate parties to the trust, enforced by the Registrar.
- VARA Rule III.B.1.c was read as a permissioning mandate. It is a risk-management obligation about divergence between ledgers; it says nothing about whitelists, approved venues or transfer restrictions. VARA's only transferability provision anywhere in the Issuance Rulebook is a whitepaper **disclosure** item, and a regex sweep of 348,000 characters of rulebook text found zero occurrences of any token-standard or whitelist requirement.

Three statements from earlier work are therefore formally **withdrawn**: "an open DEX listing is incompatible with Option A", "both parties to a transfer must be registered holders", and "an unregistered recipient cannot receive AURX". VARA in fact expressly contemplates tokens reaching persons the issuer has never met: Annex 2 III.E.3 conditions **redemption**, not holding, on the owner "or their designee" having onboarded.

The permissioned design survives as the engineered fallback (section 4.4) if counsel rejects the class-defined trust. This history is retained deliberately: it is why every load-bearing legal reading in this document is either verified verbatim at primary source or flagged as an assumption for counsel.

#### 3.5.4 What route 2 costs, stated rather than discovered

- **The customer's ownership is beneficial, not legal.** Direct onshore bailment would give legal title, the strongest form. The industry-normal position is the one taken (Paxos describes PAXG the same way), but marketing must not say "you own the bar outright" in a way only legal title would support.
- **A fund-classification question arises.** A DIFC vehicle holding property for many participants invites the Collective Investment Fund test. The analysis (Confidence: Medium-High, for counsel): allocated gold that produces no income, is not managed, and is fixed per customer does not meet the profits-or-income limb. Note what protects this: the profit-share dividend was removed on securities grounds (section 9.5), and its removal is also what keeps the vehicle outside the fund test. It must stay removed.
- **A trustee licensing question arises.** A single-purpose DIFC trustee company may be exempt from DFSA licensing as trustee of a single trust (Confidence: Medium, retrieved from a rulebook mirror). Verification changes the cost of the whole route.
- **ADGM is not a drop-in substitute.** ADGM Foundations Regulations 2017 s.29(1) vests full legal and beneficial title in the foundation, so the customer owns nothing until distribution, which defeats the direct-ownership claim outright. (Bankruptcy remoteness in that regime is s.30; the forced-heirship firewall is s.29(2) to (5).) An ADGM *trust* is unexamined; any move toward ADGM needs fresh analysis, not substitution.

### 3.6 Client money and client assets

**The money question is simpler than the client's original plan assumed.** VARA's Client Money Rules (Company Rulebook Part IV) permit Aurumix to receive and hold customer fiat directly, with no separate CBUAE licence, under conditions the design adopts wholesale:

- Client money is not Aurumix's and sits outside its estate on insolvency.
- Received funds reach a designated Client Account within one calendar day.
- UAE clients' money is held with third-party banks in the UAE; overseas clients' money may land abroad but must move to a UAE bank within 24 hours.
- The rule governs location and segregation, not currency: the product runs USD as the primary client account with AED alongside.

**The split rule** (designed here because the rulebook leaves it to the licensee): the entry fee ceases to be client money **at the moment title transfers**, and not before. VARA's definition excludes money "immediately due and payable to a VASP for its own account"; the fee becomes due when the service is delivered, and title transfer is the delivery. Before that moment the customer is owed either gold or all of their money back. A repayment on the credit facility arriving into the client account needs the same rule extended to it; this is flagged as undesigned in section 14.

**The asset half is stronger than a housekeeping rule.** Company Rulebook V.B.2: client virtual assets "are not owned by the VASP and shall not form part of the VASP's estate in the event that the VASP is or becomes Insolvent." This is a statutory estate exclusion. Its limit is exactly why the DIFC vehicle exists: **the rule protects the token, not the metal.** Physical gold is not a virtual asset, so the bars need their own protection, which is section 3.5's job. Whether VARA's exclusion reaches the metal at all is a retained counsel question.

### 3.7 Redemption law

Annex 2, Part III.E of the Virtual Asset Issuance Rulebook (19 May 2025), verified verbatim:

| Rule | Text (operative words) | Design consequence |
|---|---|---|
| Opening condition | "To the extent an ARVA provides owners and/or holders with a right of redemption..." | Redemption is optional. Aurumix grants it deliberately (section 7.1) |
| III.E.1 | Redeem "for an equal value denominated in a. AED; and b. other forms as may be determined by the VASP and disclosed in the Whitepaper" | AED payout always offered; USD disclosed in the whitepaper alongside it |
| III.E.3 | Requests "processed and completed within a reasonable period... provided the owner and/or holder, or their designee, has successfully onboarded" | A disclosed, size-tiered settlement window is the only pressure valve. Onboarding is a precondition of redemption, not of holding |
| III.E.4 | "shall process and complete redemption requests **without charging any fees**" | **No exit fee of any kind, ever.** This single rule killed one designed mechanism (a decaying spot exit fee) and reshaped custody recovery (section 13.3) |
| III.E.5 | Clear and detailed policies and procedures required | The written redemption policy is a licence deliverable |

Citation note, recorded because earlier working drafts got it wrong: this is **Annex 2 (ARVA Rules) Part III.E**, not "Issuance Rulebook III.E". Part III of the main rulebook is Whitepapers and Public Disclosures.

"Equal value" is undefined. The design assumes the stricter reading (full prevailing value, no haircut to the dealer's bid) and asks counsel to confirm; the difference is the entire two-way spread on every exit (legal brief, Question 3).

### 3.8 The wind-down plan

A wind-down plan is **mandatory at all times** (Company Rulebook Part VII.A), with twelve prescribed contents. Two provisions shape the design: the sale of client money or client assets must be "explicitly excluded from, and not necessary for" completing the plan (Rule 1.k), and VARA retains intervention powers over client assets (Rule 1.l).

Direct ownership is what makes Rule 1.k satisfiable rather than aspirational: the customers' gold is not the estate's to sell. For an open token, the executable wind-down mechanics are a published claim window, burn-on-redemption, and the freeze role, which is what a liquidator can actually run. Aurumix additionally holds something no comparable has: a monthly cash touchpoint with the direct-channel book, so the great majority of holders are contactable by construction. The plan must be built regardless; publishing it is free differentiation on required work.

### 3.9 Marketing and transfer-rule constraints

- **Travel Rule threshold: AED 3,500** (not the USD 1,000 in the client's specification). Originator and beneficiary information obtained and held before initiating transfers above it; information accompanies all transfers regardless of size; aggregation applies per day.
- **Marketing Regulation I.C.2:** no urgency or fear-of-missing-out framing; incentives must run for an adequate period and **must receive a compliance confirmation from VARA** (I.C.2.l(iii)), which puts the referral programme on the licensing critical path (section 12.6); Aurumix is liable for the claims of persons marketing for it.
- **No return language anywhere.** Gold Rewards is a capped fee rebate and is never described as yield, interest, return or dividend (section 9.5). The premium is never marketed (section 2.4).
---

## 4. Token architecture

### 4.1 What AURX is

| Attribute | Specification |
|---|---|
| Standard | **Open ERC-20** behind an upgradeable proxy with a transfer-hook stub |
| Transfer control | **Blocklist**, denying by exception (sanctions, court order, fraud). Not an allowlist |
| Control roles | Freeze, seize and reissue, held by the issuer. The price of the licence, and the precedent (PAXG) pays it too |
| Identity | KYC is a hard precondition of the mint and of redemption. No identity requirement between the two |
| Peg | 1 AURX = 1 gram, permanently (section 2.2) |
| Supply | Uncapped. Supply is a consequence of purchases; tokens exist only against allocated grams |

The architecture in one line: **identity at the two doors, freedom in the room.** It is the same split PAXG, XAUT and Backed Finance operate, and it is what Annex 2 III.E.3 was drafted to permit.

Two build rules carry the legal risk profile:

- **Do not commit to a token standard by name; commit to permissioned-capable.** The proxy plus transfer-hook stub costs roughly a day in the September build and converts the token standard from a decision that must precede the build into one that can follow counsel. A one-mapping allowlist hook delivers everything the fallback needs.
- **The blocklist ships either way.** It is less code than an allowlist, it leaves the same control surface, and a pure bearer token with no control surface cannot be wound down (the Cache Gold failure: a published wind-down plan, followed, still stranded 96% of supply).

### 4.2 Identity at the two doors

| Layer | What happens | Who must be identified |
|---|---|---|
| Mint | Fiat in, KYC complete, gold allocated to the trust, tokens issued to a verified address | Everyone. A hard precondition (section 5.2) |
| Hold and transfer | Plain ERC-20 transfers. Any wallet, subject to the blocklist | Nobody |
| Redeem | Tokens burned, cash paid to a name-matched bank account | Everyone. Annex 2 III.E.3 makes onboarding a rule precondition of redemption |

The middle row is what changed in the composability decision (section 3.5.3). Its consequence for services is handled honestly rather than hidden: **everything that needs an account works only on custodied gold.** ICS Retention, the credit pledge, the Family Portfolio and the Beneficiary Transfer Instruction all read the account, not the chain. A withdrawal to self-custody is therefore a disposal for scoring purposes (section 8) and takes those grams outside the family features (section 11.2). The customer sentence: your gold is yours to take out whenever you want, and the account features work on the gold you keep with us.

### 4.3 How ownership moves with the token

Covered structurally in section 3.5.2. The token-layer consequence: a peer transfer needs no register write, no counterparty check and no whitelist for ownership to follow it, because the trust's beneficiary class is defined by the ledger itself. The invariant the build enforces is:

```
trust gold holdings (grams)  >=  AURX outstanding
```

checked continuously, published monthly, with minting halted automatically if the invariant is at risk, if custodian attestation lapses, or if the vault position cannot be confirmed. (An earlier invariant, `sum of register sub-accounts = tokens outstanding`, belonged to the withdrawn named-register design and is superseded.)

### 4.4 The fallback, and the trap that is never built

**Fallback (if counsel rejects the class-defined trust):** flip the transfer hook to an allowlist. The token becomes permissioned, every holder is registered, transfers write to a named register, and the open-listing strategy is foreclosed. Buildable, more expensive, and the reason the proxy ships from day one. The legal brief asks counsel to say which limb fails, because the fallback differs by limb.

**Never built, under either answer: a permissioned base token with an open wrapper.** Inside a wrapper the registered holder is the wrapper contract, so the person holding the wrapped token owns no gold. The comparable set contains exactly this failure: on one venue the issuer's terms grant holders title, on that issuer's own wrapped version a separate company's terms grant "no legal, equitable or beneficial right, title or interest" in the reserves, with the difference invisible unless both documents are read. If a wrapper is ever issued, its own terms must state what the wrapper holder does and does not own.

### 4.5 Composability policy: capable is not listed

The token ships composable-capable and commercially unlisted. Sequencing:

1. **September build:** proxy, hook stub as blocklist, freeze role, KYC at the doors, multi-tenant register and mint. List nowhere.
2. **Counsel:** confirm the trust construction (legal brief, Question 1) before any whitepaper claim about transferability, because whitepaper claims bind the licence application and VARA may demand a supporting legal opinion.
3. **Trust deed:** draft the class definition. A drafting exercise, not a structuring one.
4. **After the licence, once the float is deep:** enable secondary trading in order of increasing risk: a VARA-licensed exchange first, then a broader exchange, then decentralised venues. Each step is a commercial decision with no rebuild behind it.

Two standing prohibitions: **do not seed a thin liquidity pool at launch** (a thin pool produces a visible, continuous discount, the Midas XGZ case), and **do not market AURX as collateral for third-party platforms** (third parties integrating it is their decision; Aurumix promoting it is a marketing-regulation and classification problem).

### 4.6 What a transfer is, legally and mechanically

- A transfer moves the beneficial interest with the token (section 3.5.2). It is not a redemption, so the no-fee rule does not touch it.
- ICS state does not transfer: the score attaches to the verified identity of the account holder (section 8.7). Received grams start their own credit-seasoning clock (section 10.3).
- Pledged grams sit in platform custody under a registered security interest and cannot be withdrawn or transferred until the charge is released (section 10.5).
- Blocked addresses cannot send or receive; frozen balances can be seized and reissued under the disclosed control framework. These powers exist for sanctions, court orders and fraud, and their scope is disclosed in the whitepaper.

---

## 5. Buying gold: the SIP and the spot lane

### 5.1 One account, two transaction types

SIP and spot are two ways to buy on one account, not two classes of customer. The earlier two-class design deadlocked its own front door (spot was the stated entry point for new investors, spot earned no score, and spot access was score-gated) and was deleted.

| | SIP contribution | Spot purchase |
|---|---|---|
| Trigger | A monthly schedule the investor declared | An on-demand order |
| Amount | Variable month to month. Hard floor USD 20, target USD 75, no maximum | Any amount above the floor |
| Earns ICS | **Yes** | **No** |
| Entry fee | Base rate, discounted by the account's tier | Base rate, **discounted by the same tier** |
| Counts in Retention | Yes, both sides of the ratio | Yes, both sides of the ratio |
| The gold | Identical | Identical |

Three rules close every boundary question:

- **Earning and spending are separate.** Only SIP contributions earn the tier. Once earned, the tier is an account attribute and applies to everything the account does: every purchase price, all grams for credit, the card, the family services.
- **Extra money inside a month is a spot purchase.** It buys gold and earns no scoring period, which is what stops twelve payments in January becoming twelve months of history.
- **The gold never differs by channel.** Only prices and services differ. Grams are fungible; no gram is ever tagged SIP or spot (a rule that also removed the need for any ordering convention on partial exits).

Why the tier discount reaches spot purchases: the distinction was unenforceable anyway (a declared SIP amount is variable with no maximum, so any spot sum could be relabelled as this month's contribution), and a price reduction cannot leak (the round trip of buy-at-discount, exit-at-no-fee nets to minus the fee at every tier). Price levers are safe to make channel-blind; payout and leverage levers are not, and spot stays excluded from those.

### 5.2 Stage zero: the identity gate

Nothing in the product happens before verification completes. If funds clear while verification is pending, the money sits in the Client Account and no gold is allocated.

| # | Step | Output |
|---|---|---|
| 0.1 | Account opened; **country of residence** captured | Residence, not passport, decides eligibility |
| 0.2 | KYC, sanctions and PEP screening | Pass, refer or reject |
| 0.3 | Eligibility against the country perimeter | Accept, or decline with reason |
| 0.4 | Wallet provisioned | The address is mint-eligible |
| 0.5 | Bank account registered and **name-matched to the holder** | The funding account of record |
| 0.6 | Terms accepted, including the trust construct and the standing instructions framework | The contractual half of ownership |

Step 0.5 is load-bearing: the entire payment design rests on one test, **whose bank account sends the money** (section 13.4). Any inbound payment from an unmatched account is rejected. Two further declarations are captured at onboarding for the succession product: domicile, and the customer's applicable succession regime (section 11.7).

### 5.3 The nine stages of a purchase

The lanes differ only in what triggers stage 1. The order is **money, then title, then token, never any other order**: if title cannot be recorded, the token must not exist.

| # | Stage | Timing | What happens |
|---|---|---|---|
| 1 | Instruction | T | SIP: the contribution date arrives. Spot: an order is placed |
| 2 | Collection | T to T+1 | Funds arrive on a push rail (section 5.4) |
| 3 | Client Account | within 1 calendar day | Credited to the designated Client Account. Not Aurumix's money |
| 4 | Price struck | first LBMA fix after cleared funds | The benchmark; neither side selects it |
| 5 | Grams calculated | same moment | (Contribution less entry fee) / fix per gram |
| 6 | **Title transferred** | same day | Grams allocated to the customer's holding under the trust |
| 7 | **Tokens minted** | same day | 1 AURX per gram, to the customer's verified address |
| 8 | Money settles | same day | Metal cost to the dealer; the retained margin moves to the company account (the client-money split rule, section 3.6) |
| 9 | Records | same day | Gold Receipt updated, ICS event recorded (SIP only), float drawdown logged |

Stages 10 to 12 are the treasury cycle (section 6), invisible to the investor. Target: stages 1 to 9 complete within 24 hours of cleared funds, against the category's only published benchmark of T+3.

**The fee is a price, not a cash line.** On a USD 75 contribution at launch assumptions, the disclosed fee is 5% (USD 3.75) but the cash Aurumix retains is materially less, because the fabrication premium on small bars is buried inside it. Both numbers are true; the whitepaper discloses the fee and the budget models the margin (section 13.2).

### 5.4 Payment rails: push only at launch

The launch collection design is **push-only**. Pull collection (direct debit) was dropped deliberately.

| Rail | Investor action | On failure | Role |
|---|---|---|---|
| **AANI Request to Pay** | One tap per month in their own banking app | Nothing. The request expires; no fee, nothing bounces | **Default.** AANI is the UAE instant-payment platform, operated by a CBUAE subsidiary and built on the same technology as India's UPI, so the persona already knows the gesture |
| **Prefunded balance** | One transfer covering several months, drawn monthly | A draw against an empty balance is simply a miss | The honest "set and forget". Prompted at signup ("fund three months at once"). The undrawn balance is client money, refundable, priced at each draw's fix |
| AANI electronic direct debit | None | To be assessed at go-live | Target state; announced, not live |

Dropping the pull rail deleted three problems at once: the mandate machinery, the bounce-fee problem (a returned direct debit costs the customer a bank charge; an expired request costs nothing), and the largest unverified dependency (variable-amount mandate support). Marketing rule: "one tap a month" on Request to Pay; "set and forget" is promised only on the prefunded balance until electronic direct debit ships.

The rails carry four SIP rules:

- **The floor is a hard gate.** A payment below USD 20 is rejected and returned, never partially credited. This deletes the partial-payment state entirely.
- **Grace is 5 calendar days** from the contribution date, and never expires on a weekend or public holiday. A deliberate departure from the insurance-industry 15 days: a push rail needs no bounce-recovery window, so grace only covers being busy or away.
- **A failure and a decision are different events.** Delivery and open events are logged on every payment request, so "never saw it" and "chose not to pay" stay separable in the data. Involuntary churn runs 20 to 40% of subscription churn in published benchmarks; the design does not let it masquerade as a decision.
- **Reducing the amount is free, instant and never scored.** The alternative to reducing is quitting.

**International collection.** Overseas savers pay into local collection accounts (multi-country providers), swept to a UAE bank within 24 hours per the client-money rules. Whether e-money institutions satisfy VARA's "third-party banks" wording is one of the two payment questions for counsel (legal brief, Question 6): if it fails, cross-border collection economics fail with it.

### 5.5 The SIP rulebook: definitions and states

**Vocabulary, because the edge cases live in the definitions:**

| Term | Definition |
|---|---|
| Period | A **calendar month**. Never the investor's own date, so date changes can never create or destroy a period |
| Contribution date | The investor's chosen day of the month. A collection convenience only |
| Counted period | A month in which one accepted contribution at or above the floor cleared, on time or in grace. One per calendar month, maximum. Amount irrelevant above the floor |
| Confirmed SIP | **Six consecutive counted periods.** The gate to the entire scoring layer (section 8.2). Permanent once earned |
| Declared amount | The number on this month's payment request. Variable, never scored, not a promise |

A deliberately deleted field is worth recording: a customer-set "declared minimum" (score anything above your own floor) was removed because every rational customer sets it to the product floor, and a field on which every rational customer selects the same value carries no information. The same argument deleted the contractual lock-in, the declared pause, and the customer-set floor. **The product floor (USD 20) is the only minimum.**

**When a payment is missed:** nothing happens to the gold, ever. The consequences run entirely through the score (section 8.5). **There is no revival and no arrears mechanism**: a missed period is permanently missed, and money arriving after grace is offered as a spot purchase on the same screen. Revival is insurance machinery for a contractual lapse; the contractual lock-in was deleted, so a miss here breaches nothing and there is nothing to revive. Deleting it also removed an entire exploit class (arrears timed to look back at a lower gold price) by construction.

**The three account states, none of which involves a request or a review:**

| State | Trigger | Treatment |
|---|---|---|
| **Regulatory block** | Compliance blocks the account (for example, the customer becomes India-resident) | A system event, not a request. **Months in which Aurumix refuses the investor's money do not count against them**: the score clock freezes, gold is retained, Confirmed SIP is retained, existing credit runs to term with no new draws. Applies identically before the gate: a saver at 4-of-6 resumes at 4-of-6 |
| **Stop** | The investor cancels | Nothing is forfeited. Gold retained, score decays on its own clock, restart resumes from wherever decay left it |
| **Dormant** | 12 consecutive silent periods | Housekeeping, not protection: requests stop, the SIP closes as an instruction, the account is hold-only. No score meaning; decay has already done its work. A spot purchase by a dormant account is permitted and is the natural way back in |

A "declared pause" state was considered and deleted: a free tap-to-pause is a free option every sophisticated customer about to miss would take, so it carries no information, and the step-down for a miss is mild by design.

### 5.6 The spot lane and large tickets

A spot purchase runs the identical nine stages; stage 1 is an order. No mandate exists, so nothing can bounce. What spot deliberately does not get: no scoring periods, no credit unlock, no card tier, no family features earned. What it does get: the account's earned entry-fee discount, because a price lever cannot leak.

Large tickets are the useful ones for the treasury and carry their own ladder:

| Ticket band | Handling |
|---|---|
| Below AED 3,500 (~USD 950) | Standard flow |
| Above AED 3,500 | Travel Rule information requirements apply |
| Above the instant-payment cap (AED 50,000) | Domestic transfer or wire; enhanced due diligence; source of funds |
| **Above roughly one bar denomination** | **Procured directly rather than drawn from the float.** A single order larger than the float would otherwise halt minting for everyone else. Quoted as a two-step: price indication, then execution against a same-day dealer purchase, with the threshold and the longer settlement disclosed |

### 5.7 Worked example: one USD 75 contribution

At an illustrative fix of USD 109.31 per gram, entry fee 5%, launch denomination 100 g bars:

| Step | Value |
|---|---|
| Contribution received | USD 75.00 |
| Entry fee (5%, disclosed) | USD 3.75 |
| Net to gold | USD 71.25 |
| Grams struck at the next fix | 71.25 / 109.31 = **0.651815 g** |
| AURX minted | **0.651815** |
| Title | 0.651815 g allocated to the customer under the trust, same day |
| ICS | One counted period recorded (SIP lane) |

The gram figure is exact and the customer can recompute it from the published fix, which is the point: every number in the product is checkable by the person it belongs to.
---

## 6. The gold float and the treasury cycle

### 6.1 The lumpiness problem

Aurumix promises three things that do not fit together without a fourth mechanism: 100% allocated physical gold, a USD 20 monthly minimum, and wholesale pricing. Wholesale gold comes in lumps. The smallest practical bar is 100 g (roughly USD 11,000); the working unit is 1 kg. At the Year 1 book the SIP inflow buys roughly 11 grams a day, so a 100 g bar takes about nine days to fill. Nobody can buy 11 grams of allocated bullion at wholesale each day.

Every physically backed protocol in the comparable set bridges this gap somehow, and most of the routes are closed to Aurumix: wholesale-only minimums negate the business; an unallocated buffer breaks "100% allocated and unencumbered" (an unallocated balance is an unsecured claim); minting ahead of the gold concedes the token is not fully backed at all times (one protocol discloses exactly that, and the design deliberately does not copy it); vertical integration requires owning a refinery.

### 6.2 The mechanism: a gold float

A **float** is working gold inventory owned outright by Aurumix from its own capital, held in the vault, segregated from customer metal. It is not a reserve, it is not held instead of backing, and it never commingles with allocated customer bars.

- Investor funds clear; grams are struck at the next fix.
- Those grams move **out of the float into the customer's allocated holding** the same day. The metal already exists, is already vaulted, already has a serial number.
- The treasury replenishes on a threshold trigger when cumulative drawdown reaches one bar denomination.

**The float decouples the investor's ticket size from the treasury's purchase size.** The investor buys 0.65 g; the treasury buys a bar. This is what makes a USD 20 minimum possible where PAXG needs ~USD 120 and XAUT's direct channel needs ~USD 170,000.

The float does five jobs:

1. **Lumpiness.** Absorbs the mismatch between daily inflow and bar denomination.
2. **Price risk.** Moves the timing gap off the investor (under 24 hours to allocation) and onto the treasury over the fill window only.
3. **Live pricing.** Makes a firm, auditable, benchmark-based price quotable at the point of sale.
4. **The buyback.** Absorbs exit flow in reverse, so an exit does not force a physical sale (section 7.3).
5. **Collateral enforcement.** Absorbs a liquidation sale on a defaulted credit facility at the fix, with no dealer call on a bad day (section 10.4).

**Funding: Aurumix carries the float from its own capital from month one.** A dealer-carried variant (the Aurus model, where a licensed bullion trader holds the inventory) was the original launch recommendation; subsequent modelling work closed it, because all three routes the comparables use to avoid carrying metal are unavailable to Aurumix. The float must never be sourced from investor funds, and the two positions (float and allocated customer metal) must never commingle, in the vault or in the accounts.

### 6.3 Sizing and the denomination upgrade rule

Sizing rule: **float of at least one bar denomination plus a buffer of N days' trailing inflow**; two bars is the launch setting. At Year 1 volumes this is roughly USD 22,000 of metal against a 100 g denomination; the float falls as a share of assets as the book grows, because it is a fixed operational requirement rather than a proportional drag.

Bar denomination is the margin dial: the fabrication premium falls as bar size rises, and float size is what unlocks bar size. The upgrade rule: move up a denomination when the annual premium saved exceeds the cost of the incremental float capital plus the incremental price-gap risk. The measured premium ladder (from the Phase 4 evidence pass, replacing earlier estimates): roughly **1.50% at 100 g and 0.95% at 1 kg**. Good Delivery is retired as a rung: Dubai's own good-delivery standard is a 1 kg bar, so the old third rung targeted the wrong object.

The float is structurally short over the fill window (it sells grams at today's fix and replaces them at the procurement fix). At gold's historical volatility this price-gap risk stays well under half a percent of purchases at every scale, and is mean-zero rather than a systematic cost. The larger, structural cost is the pricing convention itself: striking customer prices at the next fix, hours away, rather than off a live quote, carries a measured cost of roughly 0.79 percentage points; a live-quote engine is the alternative and is a client decision that has not yet been put (section 14.4).

### 6.4 The procurement cycle

| # | Step | Detail |
|---|---|---|
| 1 | Threshold check | Fires when cumulative float drawdown reaches one bar denomination |
| 2 | Bar procurement | Buy at fix plus the fabrication premium from the two-way dealer. **The premium is paid on net new grams only**: redeemed gold returns to the float and is resold, so it is not re-fabricated |
| 3 | Intake | Independent assay, vault receipt, serial recorded, title registered to the vehicle (Tradeflow warrant where in scope) |
| 4 | Monthly Allocation Report | Bar serials, assay certificates, grams struck, fixes used, float balance, allocated balance |

The report is the surviving, honest descendant of the client's "Mining Event": the batching function kept, the scarcity theatre removed, the communication kept as verifiable disclosure.

### 6.5 The invariant set

Developer-facing, enforced at runtime, published monthly:

- **Backing:** `float grams + allocated grams >= AURX outstanding`, at all times.
- **Trust:** `trust gold holdings >= AURX outstanding` (section 4.3).
- **Client money:** `Client Account balance >= collected funds not yet allocated and not yet refunded`, checked daily.
- **No unbacked issuance, ever.** Minting halts automatically if the float reaches zero, if custodian attestation lapses, or if the title record is unavailable.
- **Ordering:** money, then title, then token (section 5.3).
- **Sourcing covenant:** named refiners with accreditation covenant and pre-authorised substitution (section 2.1).

### 6.6 The dependency that gates this section

**The two-way bullion dealer is still unnamed, and it gates the float, the procurement cycle, the buyback and the fee calibration alike.** The client's specification names the vault three times and the seller zero times; vaults do not sell gold, and custodians do not liquidate it. Dubai's wholesale gold market is commercially opaque by convention (premiums, two-way spreads, minimum tickets and title-register fees are published by nobody, and repeated research passes have confirmed the negative), so several parameters in this section can be specified but not calibrated until a dealer conversation happens. This is named as a project risk rather than smoothed over: it is the single most important commercial conversation on the critical path.

---

## 7. The exit: cash buyback

### 7.1 The design position: grant the redemption right, accept the consequences

There is no physical redemption; exit is cash buyback only, which suits a customer base holding fractions of bars. Redemption is optional for an ARVA (section 3.7), and Aurumix could have structured its buyback to avoid being a redemption right. It deliberately does not:

1. The client's specification promises a Buyback Floor. A published, formulaic commitment to buy at a defined price will be read as a redemption right in substance, whatever it is labelled.
2. No redemption right means no price floor. The two comparators that restricted their exit trade at a discount; the credibility of the exit is most of what makes a gold token trustworthy to a retail saver.
3. Under direct ownership the customer already owns the grams; a committed exit is the honest counterpart of that claim.

Accepting the right means accepting Annex 2 III.E.4: **no fee of any kind on the way out.** The rule is absolute, and it reshaped two mechanisms: a decaying spot exit fee was deleted outright, and custody recovery moved off the exit entirely (section 13.3). Two economic arguments would support a zero exit fee even without the rule: an exit fee is the width of a discount band (it breaks the peg in realised value today and in market price the day any venue lists AURX), and under direct ownership charging a customer to receive their own property is incoherent. That second argument is design logic, not a published VARA position, and is never attributed to the regulator.

### 7.2 The exit lifecycle

| # | Stage | Timing | Detail |
|---|---|---|---|
| 1 | Request | T | Grams or currency amount, full or partial |
| 2 | Checks | minutes | Onboarding status per III.E.3, sanctions re-screen, residence re-check, bank account name-match, no unreleased pledge on the grams, rapid in-and-out flag |
| 3 | Price struck | **next fix after the request** | Neither side can select the fix |
| 4 | Tokens burned | same day | From the verified address |
| 5 | Title returns | same day | Grams move from the customer's holding back to the float |
| 6 | Payout | T+1 target | To the customer's own name-matched account. AED always available; USD as disclosed |
| 7 | Float rebalance | threshold-triggered | Only if the float exceeds its upper band does the treasury sell metal to the dealer |

The checks in stage 2 run **before** the price is struck, so a failed check never leaves a struck price hanging.

### 7.3 Why a zero-fee exit is affordable

The objection to III.E.4 is that Aurumix must pay the dealer's two-way spread on every exit and cannot charge for it. The objection assumes gross exits drive physical sales. They do not:

| Book state | Inflow | Gross exits | Net flow | Physical gold sold |
|---|---|---|---|---|
| Growing | 8% of assets | 3% | +5% | **None.** Exits return grams to the float; the next buyer consumes them |
| Flat | 4% | 4% | 0% | **None** |
| Shrinking | 2% | 6% | -4% | On the 4% net only |
| Run | 1% | 25% | -24% | In size, at the bid, into a falling market |

**The cost of the redemption promise is the dealer spread on net outflow, not on gross exits.** In a growing book that is approximately zero. This converts an expensive-looking regulatory constraint into the strongest argument for funding the float, and it should be presented to stakeholders in exactly that form.

### 7.4 The stress case

Row four is real and gets a disclosed mechanism, not a hidden one. III.E.3's "reasonable period" is the only valve, because III.E.4 removed the price valve:

- **A disclosed, size-tiered settlement window** in the whitepaper: next business day for small redemptions, up to three business days where a dealer sale may be needed, up to five for large redemptions, possibly staged. Thresholds are set once the float size is known.
- **The holder already owns the metal.** If Aurumix cannot pay cash, the claim is not on Aurumix's balance sheet: it is on gold the customer owns, held by a vehicle outside Aurumix's estate. This is materially stronger than the rulebook's fallback contemplates and is the strongest single argument for the trust structure.
- **The wind-down plan** is the backstop, and direct ownership is what makes its no-client-asset-sales rule satisfiable (section 3.8).
- **A disclosed suspension right** limited to market closure, custodian failure or force majeure, never liquidity management. Anything broader reads as a discretionary gate on the customer's own property.

### 7.5 Transfers are not exits

A peer transfer moves ownership with the token (section 4.6) and is not a redemption: no fee rule applies to it, the gram count moves between accounts rather than shrinking, and a secondary market gives holders an exit that never touches the buyback at all, which relieves rather than adds redemption pressure. For scoring purposes an outbound transfer is an outflow (otherwise transferring to a spouse would dodge Retention), and inbound grams enter both sides of the receiver's ratio, so nothing is created.
---

## 8. The Investor Conviction Score

### 8.1 What ICS is, and the one rule that shapes it

The Investor Conviction Score (ICS) is the loyalty engine: a 0 to 100 score that prices every benefit in the product. It exists because the economics demand it. The persistency benchmark for the persona (Indian life insurance) retains roughly 79% of savers at month 13 and 38% at month 61, and a customer is barely profitable in year one; churn kills this model, not fee levels. The score is the retention machinery.

**The one rule: ICS measures behaviour, never amount.** No input reads dollars or grams held. A customer saving USD 20 a month and one saving USD 2,000 a month reach the top tier on the same day. This is not generosity; it is the classification defence. If the score rose with amount, then the entry-fee discount, the credit ratio and the rewards rate would all improve with capital, which is a return proportional to investment: the securities shape the whole design avoids. **Amount sizes the base; behaviour sets the rate.**

Three inputs the client's specification included were removed from scoring: Investment Value (the capital-scaling problem above), and referrals, family activity and Masterclass attendance (they corrupt the one clean number, they are each already paid through their own channel, and a status bonus for recruiting is the multi-level-marketing shape the distribution design is built to avoid). All three programmes survive; none of them scores. This is the largest set of departures from the client's specification.

### 8.2 The gate: Confirmed SIP

> **Confirmed SIP is six consecutive counted periods, and it gates the score itself, not only the benefits. Before the door: no score, no tier, no benefits. After it: the score runs, and never falls below 25.**

Two objects, kept separate:

| | What it is | How it moves |
|---|---|---|
| **Confirmed SIP** | A door. Six consecutive contributions opens it | Opens once. **Permanent.** A later miss never closes it |
| **The ICS score** | A dial behind the door | Recalculates monthly from the moment the door opens |

The customer sentence: *six months straight to start, then your score runs and it decides what you get.*

Rules of the gate:

- The wording is always "six consecutive contributions", never "a six month commitment". Nothing is promised and a broken run costs nothing except starting the run again.
- **The scoring clock starts at the qualifying run.** Payments made before the run are real gold purchases and are invisible to the score, so **every account opens at exactly Silver, 25**, whatever the run-up looked like. One entry point, one number, no branches in the promise.
- Before the gate the app shows a countdown ("4 of 6, three months to go"), never a score: the persona reads scores like credit bureau numbers, and a low early number would read as bad standing in exactly the months where persistency is thinnest. A broken run resets the counter with an explicit message.
- The honest cost, stated rather than discovered: a saver who never strings six together accrues no score at all, however many scattered payments they make, and months one to five pay full fee for no benefit. Both appear in the terms and the app.
- Every account passes its own gate, family sub-accounts included. Nobody inherits status.
- A regulatory pause freezes the run rather than breaking it (section 5.5): a saver at 4-of-6 resumes at 4-of-6, and a frozen month is skipped on every clock as though it never existed.

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

**Why a minimum and not a weighted sum: this is the load-bearing choice.** Each tier is genuinely two conditions (for example Gold is "12 months paid AND 6 of the last 12"), and `min(A, B) >= x` is exactly `A >= x AND B >= x`: **minimum is the arithmetic of AND.** A weighted sum lets components substitute, which is how an earlier draft let a ten-year saver who had not paid in a year score near the top on seniority alone. With a minimum, no substitution is possible in either direction, there are no weights to argue about, and the score names its own constraint: if ICS equals Standing, discipline binds (pay); if it equals Record, only time does. For a saver who never misses, Standing never binds (provable from the mappings), so a good customer's score is purely their Record.

**Retention rules that matter to counsel and to the build:**

| Case | Rule |
|---|---|
| Gold Rewards gram credits | Count as acquired: they enlarge the denominator and can never create or worsen a penalty |
| Transfers to a family sub-account or under a Beneficiary Transfer Instruction | **Not a sale.** The gold stays inside the product; only the name changes |
| Lender liquidation on a margin call | **Counts as a sale.** The customer chose to borrow; the alternative makes borrowing a route around Retention |
| Withdrawal to self-custody | **Counts as a sale** (section 4.2). The account can no longer see or service those grams |
| Compliance-forced exit (the returning NRI) | **Deliberately open.** The proposal is to extend the regulatory pause so a forced redemption does not move the score; it interacts with the margin-call rule and the two will be closed together |

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

Why five and not the client's seven: tier count does not change the size of the benefit ladder, only how it is sliced, and the ceilings are set by economics outside Aurumix's control (the fee uplift, the partner's maximum loan ratio, contracted interchange, the card sponsor's programme levels). Seven tiers cut the fixed ranges into steps too small to feel (a 0.25 point fee step is USD 0.19 a month at the target ticket); at five, each step roughly doubles, and the card maps one-to-one onto three sponsor programme levels. Titanium and Elite are dropped; Green is renamed "No tier".

Tiers are **absolute thresholds, never relative position**. Percentile tiers would make a flawless saver demotable by a better cohort, would make every benefit unquotable as a price or a contract term, and would build a tournament, which is a compliance surface (the client's 80/20 dividend concentration was exactly that pathology). Absolute thresholds are also what make the score computable by the customer, which is the design's central trust property.

**Sovereign tolerates nothing, deliberately.** Both inputs cap at 100, so the top threshold must sit at the cap or Sovereign arrives early; there is no headroom to create. Sovereign means a perfect year, on a complete record, with the gold intact, every month: rented by conduct, never owned. The consequence is damped where it costs money, because no benefit reprices retroactively (section 9.1).

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

What written rules still cover: **the credit prize** (cycle to a tier, buy a large position, borrow high) is removed by 90-day collateral seasoning plus the ratio being struck at the facility (section 10.3), and Retention keeps a cycler from reaching a credit-bearing tier at all; **the residue** is covered by a round-trip flag (a redemption within 30 days of a contribution, four or more months in any twelve, freezes tier progression pending review, with a stated appeal path and nothing deducted). A large holder cycling a small SIP beside static ballast is detectable by the flag and is otherwise not worth defending against: their honest compliance costs USD 20 a month.

---

## 9. The five benefits

### 9.1 The benefit matrix and the rules that bind it

The benefit set is closed at five. Each is a different kind of lever, and the family a benefit belongs to decides what protection it needs: **price levers are self-limiting** (bounded by money the customer hands over), **payout levers need a cap**, **leverage levers need seasoning**, **service levers need a partner**.

The matrix, with settled values:

| | No tier | Silver | Gold | Platinum | Sovereign |
|---|---|---|---|---|---|
| **1. Entry-fee discount** | 0 | 0.4pp | 0.8pp | 1.2pp | **1.5pp** |
| **2. Credit LTV** | - | - | 50% | 65% | **80%** |
| **3. Card level** | - | - | L1 | L2 | **L3** |
| **3. Card FX margin** | - | - | 2.0% | 1.5% | **1.0%** |
| **3. Card ATM allowance (AED/month)** | - | - | 1,000 | 2,500 | **5,000** |
| **4. Gold Rewards rate** | - | - | 0.15% | 0.45% | **0.75%** |
| **5. Will plan-fee discount** | 0 | 10% | 20% | 35% | **50%** |
| **5. Per-beneficiary discount** | 0 | 0 | 0 | 10% | **20%** |

Rules that bind all five:

- **The tier of record.** Every benefit reads the tier computed at the account's last period resolution, never the live score. Price levers strike at the event; the leverage lever strikes at the facility and runs to term; card parameters change at statement cycle; Gold Rewards computes at period close. One number, one update rule, no benefit can disagree with another.
- **All ladders are stepped, never smooth.** Every benefit is a quotable price, a loan term, a card programme level or an advertised rate.
- **A tier fall reprices future events only.** No retroactive repricing, no clawback of delivered benefits, and **a tier fall never triggers a margin call** (a missed USD 20 payment that forced a liquidation would convert "no financial penalty for a miss" into a lie).
- **No payout may exceed what that customer generated** (the Gold Rewards cap), and no benefit's rate may scale with capital.
- **Where a partner holds the licence, the structure is Aurumix's and the pricing is the partner's.**

Every rung buys something a customer can feel; the largest step is deliberately Silver to Gold, where credit unlocks, the card issues and Gold Rewards begins. The marketing sentence: everything unlocks at Gold, and everything roughly doubles at each step after.

### 9.2 Benefit 1: the entry-fee discount

A percentage-point reduction off the base entry-fee rate on **every purchase the account makes**, SIP and spot alike, struck with the price itself at the tier of record. It is the one benefit live at launch with no partner dependency.

Funding is the fee line itself, through base-rate headroom, and the ask is smaller than it looks because **the ladder is time-phased by construction**: nobody is above Silver in year one, so the maximum discount outstanding at launch is 0.4 points, and the first Sovereign appears at month 60, by which time the cost base has fallen with bar denomination (section 13.2). The ladder's cost curve and the business's cost curve are the same curve, offset the right way.

Because the discount is invisible month to month (a slightly smaller fee), the app displays **cumulative fee savings converted to grams** ("your tier has earned you 1.4 g since 2026"), each purchase's saving struck at its own fix so the number only ever rises. This gives the disciplined saver a payout-shaped number without creating a payout.

### 9.3 Benefit 2: the credit ladder (summary)

A maximum loan-to-value ratio for the gold-secured facility: 50 / 65 / 80% at Gold / Platinum / Sovereign, unlocking at Gold. Grams are the base, tier is the rate: two savers with identical behaviour get identical percentages on very different gram counts, which is the founding principle made concrete. Full mechanism, partners and risk machinery in section 10.

The 80% anchor is deliberate: it sits at the top of every observed comparable without exceeding one (India's regulator caps retail gold lending at 75 to 85% by loan size; the largest gold-loan NBFCs lend at the cap; a UAE incumbent lends against vaulted physical gold at 80%), and it reproduces the client's own "Gold Member: 50%" row exactly. It replaces the specification's 90 to 95% ceiling, which was anchored to nothing (the client's own worked example computed to 85%). A lending partner whose maximum lands below 80 is a repricing event, not a parameter fill.

### 9.4 Benefit 3: the card tier (summary)

Card programme levels map one-to-one onto Gold / Platinum / Sovereign. Two layers on different clocks: **the plastic** (the network product, with its bundled perks) upgrades after three consecutive months at the qualifying tier and **never downgrades**; **the parameters** (FX margin, ATM allowance, fee waivers) flex monthly with the tier of record at statement cycle. Card benefits are waivers of fee revenue funded by the interchange the same spender generates, so the benefit cannot be consumed without producing the revenue that pays for it. Full stack in section 10.

### 9.5 Benefit 4: Gold Rewards, and the dividend it replaced

**The client's ICS Dividend could not survive in its original form.** Paid from operating profit, weighted by Investment Value, with 80% to the top 10%, it is a profit share: a security, whatever it is called, pulling in prospectus requirements and a different regulator, which a USD 20 retail product cannot survive. The category evidence is one-sided: every well-regulated comparable pays zero yield deliberately, and every protocol advertising a yield fails its own arithmetic (the flagship example realised roughly 0.10% annualised against an advertised 2%).

**The replacement is Gold Rewards: a monthly fee rebate credited in grams.** Rate(tier) x qualifying card spend, computed at period close, converted at the next fix, subject to four rules that make it a rebate and not a distribution:

1. **Funded from interchange and credit revenue, never from profit** and never from other savers' fees.
2. **Capped at the interchange and credit revenue that this customer generated**, net of that customer's custody cost, as a running total per account.
3. **Earned by tier, and tier is earned by behaviour.** The rate reads the tier; the base is spend; holdings appear nowhere in the formula.
4. **Never described as yield, interest, return or dividend**, in any channel, ever.

The credible precedent sits inside one comparable company: its "yield" product is the failure case (a promise missed twentyfold), while its card cashback in gold funded by interchange is regulatorily unremarkable. Same company, same currency; the difference is the funding source, the cap and the framing.

Gold Rewards ships with the card, because interchange does not exist before it. Reward grams count as acquisitions in Retention (they can never inflate a score), earn no scoring periods, and season 90 days before counting as collateral.

### 9.6 Benefit 5: the will and family discount (summary)

A tier discount on the family product's two prices (the annual plan fee, and more shallowly the per-beneficiary registration fee). The feature itself is open to everyone who pays, at every tier: **the tier discounts the price and never gates the feature**, which is what broke the circularity in the client's specification (where the tier unlocked the thing that helped earn the tier). The discount ceiling stays below 100%: free at the top would rebuild the tier-gate in mirror image and unfund the cost exactly where usage is highest. Full product in section 11.

### 9.7 What exists on day one

| Benefit | Live when |
|---|---|
| Entry-fee discount | Launch |
| Will and family discount | Launch, with the paid feature |
| Credit ladder | When the lending partner signs |
| Card tier | When the card programme goes live |
| Gold Rewards | With the card, not before |

A customer Confirmed before the card exists has earned the tier; the benefit arrives when the rail does. The tier is communicated as the durable thing and the benefits as what it currently buys, so each newly shipped benefit lands as a gift to existing tiers rather than a migration.
---

## 10. Credit and the Gold Card

### 10.1 One facility, two draw channels

The credit facility and the Gold Card are not two products. They are **one gold-secured revolving credit facility with two ways to draw on it**: a cash drawdown to the customer's bank account, and card spend that draws against the same limit. Same collateral, same tier ladder, same lender's balance sheet, one borrowing limit in the app.

The purpose is the product's quiet centrepiece: it lets a saver reach the value of their gold without selling it, which is what makes a decades-long hold tolerable. Pledged gold keeps earning the customer's score, so using the facility never sets the saver back.

One rule this structure forces: **the facility is struck once, at facility opening, and every draw inherits the facility's struck ratio.** A card is thousands of tiny draws; striking per draw would reprice the facility on every coffee. An annual facility review re-strikes the limit to the current tier of record, while existing drawn balances run to term at their original ratio, which keeps the tier ladder binding without ever repricing anyone retroactively.

### 10.2 The stack: four roles, and who carries which risk

| Role | Does | Carries |
|---|---|---|
| **Issuer processor** | Real-time authorisation, card lifecycle, wallet provisioning, the card ledger | Operational risk |
| **Issuer of record** | The licensed name on the card, scheme membership | Scheme and regulatory risk |
| **Lender of record** | Advances the money, owns the loan book | **Credit risk** |
| **Aurumix, programme manager** | Customer, app, origination policy, collateral valuation, the authorisation decision, servicing, collections | Operational and reputational risk |

Aurumix neither lends nor issues. Two findings settled that as the only door, not the cheap one: a VARA lending permission requires the same virtual asset be lent and returned, so a dirham advance sits outside it entirely; and card issuance requires scheme principal membership plus CBUAE retail-payments licensing. Recommended openings, from the 2026-08-13 primary-source pass: **NymCard** as processor (UAE-native, credit-capable, a principal member of both schemes in its own right, which may collapse the bank-plus-processor pair into one vendor), **Emirates Money** then Mashreq as lender of record (Emirates Money already lends against physical gold at 80% LTV, vaulted at DMCC with Brink's: the same product, the same number, the same vault), Zand or CBD for VASP banking.

### 10.3 Setting the limit, and how a tap is authorised

```
borrowing headroom = seasoned, unpledged grams x fix x LTV(tier)
```

| Gate | Rule |
|---|---|
| Eligibility | Gold tier. Credit does not unlock at the Confirmed SIP gate |
| Seasoning | Grams enter the borrowing base only after **90 days held**. Redeemed-then-rebought grams restart the clock; inbound transfers start fresh |
| Ratio | 50 / 65 / 80% by tier, struck at facility opening |
| Stacking | Seasoned **and unpledged** grams only. One gram supports one facility |
| Custody | Pledged grams sit in platform custody under a registered security interest and cannot be withdrawn or transferred until released |

Card authorisation runs on just-in-time funding: on each tap the processor calls Aurumix's endpoint, Aurumix computes live headroom (grams x current fix x struck ratio, less outstanding balance) and answers approve, decline or partial-approve, inside a hard **three-second budget** including network time. Two consequences the build must absorb: Aurumix owns the authoritative balance ledger, and collateral is effectively re-marked on every transaction. A 48-hour hold on redemption requests from accounts with an active card facility closes the authorisation-to-settlement gap during which collateral could otherwise leave.

**The stand-in hole is unavoidable and is disclosed to the lender rather than discovered with them.** If Aurumix is unreachable the processor approves from pre-agreed static rules; if the processor is unreachable the card network stands in unilaterally. Both approve with no collateral check, and Aurumix learns afterwards. The static rules are the only lever: small per-transaction cap, low transaction count, no ATM, no cross-border, a hard cumulative stop, sized so the worst case on any account is immaterial against even a Gold-tier facility.

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
| Gold | 50% | -46% |
| Platinum | 65% | -29% |
| Sovereign | 80% | **-13%** |

A 13% fall is roughly a one-sigma annual move: Sovereign borrowers at maximum draw are genuinely exposed, and the design does not pretend otherwise. The mitigations are the two warnings, the 14-day cure, and the population itself (the smallest, most disciplined cohort in the book).

Procedure follows the regulator-tested Indian template in shape (notice, cure, objection right, reserve price, surplus returned, costs itemised), executed against the float at the LBMA fix with zero discretion, because Aurumix is valuer, collateral agent and buyer at once and the only cure for that conflict is a mechanical price. Whether an enforcement sale is itself a "redemption" for the no-fee rule is a live counsel question (legal brief, Question 3): if it is, recovery costs cannot be charged.

The wordings that must never blur: **a tier fall can never margin-call; a price fall can, and only against borrowed positions, past thresholds shown at the draw.** *Your score can never cost you your gold; the market can, only if you borrow against it.*

### 10.5 The collateral chain

Five links: a valid security interest, immobilisation, valuation and trigger, cure, and the sale. The middle three are designed above; the first and the custody half of the second are legal work:

- **Security is taken under DIFC law** (Law of Security 2024, UNCITRAL-model, registrar filing, grantor-agnostic). ADGM's regime appears to catch only charges created by ADGM companies, and the grantor here is a retail customer, so DIFC wins on a second independent ground beyond section 3.5.
- Whether AURX qualifies as a "digital asset" under DIFC's digital-assets statute is open; the conservative design perfects over the beneficial interest as an ordinary intangible and treats the transfer-block as operational.
- Repossession consent from the party in possession (the custody vehicle) is pre-wired into the custody documentation; whether pre-wiring is effective is an opinion question.
- The Sharia overlay: the recognised Islamic standard blesses pledging via the ownership certificate and treats holding it as constructive possession, forbids rehypothecation (already the design's position), and requires sale at market value with surplus returned (matches the ladder). It also caps safekeeping fees on pledged gold at actual cost, which touches custody recovery under an Islamic structure. Conventional or Islamic is an open client decision that sets the lender shortlist; the recommended structure if Islamic is tawarruq plus rahn.

### 10.6 The interchange economics

Verified against the card scheme's published UAE interchange schedule: prepaid interchange is 1.00% flat and capped by regulation; **credit interchange is uncapped and runs 1.80% (Platinum) to 2.10% (Infinite) by product level**. Two design consequences:

- **The card is built as credit, not prepaid**, or interchange is capped at 1.00% forever and the rewards ladder starves.
- The tier ladder and the revenue ladder are the same ladder: upgrading a loyal saver's plastic moves them to a higher-interchange product, so the upgrade enlarges the pool that funds their own rewards.

The one number to negotiate: Aurumix's programme-manager share of interchange must exceed roughly **36%** for Gold Rewards to self-fund at the Sovereign rate (0.75% rewards against 2.10% interchange). No UAE or MENA programme-manager split is published anywhere; it is term-sheet work, and 36% goes into the conversation as the floor.

---

## 11. Family Portfolio and succession

### 11.1 The two objects

The client's specification runs two different things together; they have different legal characters, different cost drivers and different risk, and the design keeps them separate:

| | **Family Portfolio** | **Beneficiary Transfer Instruction (BTI)** |
|---|---|---|
| What it is | A live sub-account structure during the holder's life | A standing, pre-authorised instruction on the account |
| Legal character | Account administration | A client instruction under VARA's custody rules, which permit a VASP to rely on pre-authorised client instructions |
| When it acts | Continuously | Once, at a defined trigger |
| Priced by | The annual family plan fee | The per-beneficiary registration fee |

"Digital Will" is the client's marketing name and is likely not to survive counsel, because it implies a regulated will-writing service. The contractual term is **Beneficiary Transfer Instruction**; the feature is a standing instruction, not a testamentary instrument.

During life, a sub-account is a declaration of intent and a display: the gold remains entirely the primary holder's, family members see their designated grams read-only, and (correcting the specification) a sub-account has **no independent credit facility and no ICS sub-score** during the primary's life. You cannot lend against gold someone does not yet own, and ICS is one number about one person. Each family member's own account passes its own gate when gold actually transfers to them.

### 11.2 The precondition: it works on the gold you keep with us

Under an open token a customer can withdraw AURX to their own wallet, and at that moment there is nothing for a standing instruction to act on. **The Family Portfolio and the BTI are custodial-account features; they attach to the account, never to the token.** A withdrawal to self-custody removes those grams from the family features and counts as a disposal for scoring (one rule, two problems closed). This is not a weakness to hide: it is the honest reason a balance stays on-platform, and it is what every custodian does. The 30% annual Retention allowance is the pressure valve that keeps the strict rule fair.

### 11.3 The probate correction

**The product cannot avoid probate on death, and the client's promise that it does ("without requiring probate, family agreement, or legal proceedings") is withdrawn.** Under DIFC trust law a beneficiary's interest is movable property: a transmissible asset that falls into the estate and needs a grant. The only architecture that genuinely avoids probate is a foundation in which the customer never owns the gold, which would destroy the direct-ownership claim, the Gold Receipt and the Reserve-Asset exemption in one move. Allocated ownership and probate avoidance are mutually exclusive; the design keeps ownership.

The reframe is honest and stronger than it sounds: the market has not solved this either. The largest regulated crypto custodian offers no beneficiary designation at all and requires probate documents before releasing anything. Aurumix is not conceding a feature competitors deliver; nobody delivers it. The product is a **probate accelerator, not a probate substitute**: pre-named, pre-verified, pre-screened, pre-split, executed in days once the paperwork arrives.

### 11.4 The trigger matrix, and why residence inverts it

The three triggers are three different legal events, not three flavours of one:

| Trigger | What it legally is | Probate? | Forced heirship? |
|---|---|---|---|
| **Date** (a birthday, an education milestone) | A completed lifetime gift | No: the holder is alive | Shielded: the DIFC firewall protects completed lifetime transfers |
| **Condition** (a defined, observable event in the beneficiary's own life) | Same, if it fires during life | No | Shielded |
| **Death** | Testamentary succession | **Yes: grant required, hard gate** | Exposed: the firewall covers lifetime transfers only |

**The lifetime trigger is the strong product and leads the design**: the education fund and the wedding gift, not the death benefit. Conditions between unrelated parties contingent on account behaviour (the specification's business-partner scenario) are not supported: that is a wager on behaviour, not succession, and it would collide with the regulatory pause.

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

### 11.7 The two populations

The persona includes Muslim customers, and a product that quietly assumes otherwise mis-sells to them. The DIFC wills route is open to non-Muslims only; a Muslim expatriate's movable estate follows Sharia fixed shares. Design consequences, all cheap: the applicable regime is asked at onboarding (with a domicile declaration, since Gulf NRIs often retain their origin domicile and succession to movables follows domicile at death); Muslim customers are led to the lifetime trigger, which is the recognised gift route and the better product anyway; a death-trigger BTI for a Muslim customer is a distribution instruction consistent with the shares, never a substitute for them; and **the product is never marketed as overriding Sharia shares, anywhere, to anyone**. The precise position of a revocable, redeemable transfer under the anti-circumvention rule is deliberately not pre-judged; it is counsel Question 7's second limb.

### 11.8 Pricing

The cost floor is roughly USD 2 to 3 one-off plus cents per year per name (identity verification plus continuous screening); everything else in the chain prices per-will or per-entity, never per-name. The binding costs are the multi-decade monitoring tail and the screening platform's monthly minimum, not the per-check rate. No adjacent product anywhere prices per beneficiary, so names are bundled: an **annual family plan of roughly USD 29 to 36 including up to four beneficiaries, USD 20 per additional name, capped per household**, charged at registration. Against the tier discount ladder, the deepest-discounted price still clears the cost floor with roughly five times headroom. No VARA rule caps ancillary fees; the obligation is disclosure of all fees in the Client Agreement.

### 11.9 The perimeter: what Aurumix never does

| Aurumix does | Aurumix never does |
|---|---|
| Execute a documented standing instruction | Determine who is entitled to an estate |
| Require a grant before a death transfer | Validate a death or adjudicate competing claims |
| Register and monitor named beneficiaries | Draft, witness or register a will |
| Tell customers to keep a valid will in their own jurisdiction | Advise on estate planning, tax or succession |
| Refer to a licensed will-writer (the DIFC Courts' digital-assets will service is both the nearest comparable and a possible partner) | Take a referral fee for it |

Two characterisation traps are designed around: marketing the feature as planning edges toward advising, and framing it as a benefit paid on death edges toward insurance. Neither permission is held, so neither framing is used.

**Build note:** none of this goes on-chain. The specification's two smart contracts (a Family Portfolio contract and a Digital Will contract holding sub-portfolio gold) must not be built: a contract holding the tokens would itself become the beneficiary of the trust, so the family member would own nothing: the wrapper trap of section 4.4 rebuilt deliberately. The design is an off-chain instruction ledger plus one token movement at execution, which also releases the USD 75,000 the specification budgeted to audit the two contracts.
---

## 12. Distribution: referrals and the agent network

### 12.1 The architecture: one budget, three rings, one wall

Distribution is the actual moat (section 1.4), and its design is governed by one reclassification: **a referral reward is an acquisition cost, not a benefit and not a score input.** That single move is what lets the programme exist, because the benefit set is closed at five and the score has no room for it.

| Ring | Who | Paid | Contract |
|---|---|---|---|
| 0. Direct | Customer arrives alone | Nothing | None |
| 1. **Member referral** | An existing customer introduces someone they know | **Once, in grams, when the referee qualifies** | None; terms of use only |
| 2. **Agent network** | A contracted, trained, disclosed intermediary | Upfront share of entry fee plus trailing, vesting with clawback | Agent Agreement |

The two rings are separate populations, not rungs of one ladder. The wall between them is the line that carries the whole design: **a bounty is a thank-you and needs no contract; an annuity is an income and needs one.** One attribution rule sits underneath: one acquisition, one payment, so the same customer is never paid for twice.

### 12.2 What counts as a successful referral

> A referral succeeds when the referee passes their own Confirmed SIP gate: six consecutive counted contributions, on their own account, under their own KYC, funded from a bank account in their own name.

Nothing else counts: not a signup, not a KYC completion, not a first payment. The product already has a definition of a real customer, and the referral programme reuses it rather than inventing a second one, inheriting six structural anti-gaming properties for free (no compression, no backdating, the hard floor, own-gate-only, separate KYC, pause-freezes-run). Minimum six calendar months from signup to any payout, by construction. Every serious comparable gates on sustained behaviour; the two gold-savings analogues gate at five and six instalments.

Attribution attaches at account creation and is immutable: any window in which attribution can still change is a window in which it will be sold.

### 12.3 The reward

> **30% of the entry fee the referee actually paid over their qualifying run, split equally between referrer and referee, credited in grams to both accounts the day the gate resolves.**

The 30% is an explicit placeholder, locked after the revenue model alongside the agent rates. Properties that hold at any percentage:

- **Both sides are paid**, on published evidence: recipient-benefiting referrals recruit more, and referral rewards backfire for unfamiliar products unless both parties are rewarded; a tokenised gold instrument sold to a first-time saver is exactly that product. A two-sided reward is also the conduct answer: "we both get gold" is a different conversation from "I get paid if you sign".
- **Paid in grams from launch**, which moves the gram-credit rail into the September build (a smaller job than Gold Rewards: same primitive, no interchange reconciliation).
- **No counting cap**: the reward is computed on whatever the referee contributed, making it a constant share (roughly a fifth) of the referred customer's contribution-margin lifetime value at every ticket size, which is what a commission is. The consciously accepted residue: a referee can front-load six months and collapse to the floor, buying gold at an effectively discounted fee; the gamer is still down on the round trip, a real KYC'd customer arrives either way, and large sums engage source-of-funds review first.
- **The timing is a retention payment in disguise**: it lands at the referee's month six, the steepest point of the persistency curve, and costs nothing extra.
- **No cap on referral count.** VARA's own guidance case study describes a licensed VASP paying on codes "with no maximum number of referrals"; what replaces the cap is a reserved volume-review right where one identity is plainly running a distribution business.
- The honest economics are stated, not dressed up: no acquisition programme recovers its cost inside six months. The referred customer is cumulatively cash-positive around month nine to eleven, and the whole analysis is conditional on the collection rail cost, which is the open item that decides whether the programme should exist at all (section 14.4).

**The open decision, which is the client's:** ship as designed (a defensible thank-you), size it as real acquisition spend funded from capital (the only version that competes with a bank's referral offer), or run attribution-only at launch and price it later (which also takes the programme off VARA's incentive-approval critical path). The recommendation is the first, announced at launch, since no reward can be paid before roughly month 13 in any version.

### 12.4 Single level, and it is not negotiable

> If A introduces B and B introduces C, A receives nothing from C. Ever, in any form.

The sharpest precedent is recent and close: in August 2024 the Indian exchange regulator prohibited brokers from paying referral commissions to unregistered persons; the largest broker killed its 10% revenue share within days and kept only non-cash points. The objection was not referral and not incentives; it was **a share of ongoing revenue paid to an unregistered person**. The bounty survived; the annuity did not. That condemns the two designs Aurumix might have copied (a 7.5%-for-life share and a 1% trailing commission, both live in the comparable set), and every reclassification case retrieved (Forsage, BitConnect, OneCoin and Karatbars, the last a gold token and the nearest reputational adjacency) turned on downline compensation. UAE pyramid-selling law could not be verified at primary source, which is itself the argument: multi-level compensation is unverified as lawful here, and the design does not need it.

### 12.5 The agent network

The client's three tiers survive as **functions, not depths**: a principal agent earns a supervision fee for supervision actually performed (training delivered, compliance sign-off, first-line complaints), payable only while the supervised book is in force and the supervision is documented. That converts an override into a service fee and is testable in a way an override never is. The recommended commission gradient pays the person closest to the customer the most (the anti-MLM shape); the client's two documents currently specify inverted gradients and the client must choose.

The budget rule copies the only live regime that governs this properly, the Indian insurance expense-of-management structure: **one overall acquisition ceiling as a percentage of entry-fee revenue, board-approved, annually reviewed, front-loading braked, excess borne by shareholders.** The 12-month commission clawback on early redemption is retained as a contractual choice (the 2024 regulations contain no clawback mandate, a correction to earlier drafts). Agent rates themselves wait on the revenue model, exactly as the client instructed.

### 12.6 The regulatory positioning

VARA's Marketing Regulation reaches this programme directly: incentives **must receive a compliance confirmation from VARA** (the regulator's own guidance shows a referral programme approved as part of a licensing application, so the design goes into the application rather than after it); no urgency or fear-of-missing-out framing; time-limited multiplier promotions are prohibited independently of taste; Aurumix is liable for referrers' claims; referrers must disclose remuneration; grams are caught identically to cash; and the reward is always described as a share of a fee, never as a share of savings. Rejected by design: leaderboards, badges, escalating rates, and any reward for a referral that does not reach the gate. Referrers are kept away from "arranging orders" and "personal recommendations" (the broker-dealer and advisory perimeters) by rule: a code-sharer does neither.

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

### 13.2 The entry fee: a build-up, not a number

The entry fee is set by arithmetic, not positioning. It must cover, per contribution: the fabrication premium on the launch bar denomination, the price-gap risk of the fix convention, the float's cost of capital, and the payment rail, before any margin. At launch on 100 g bars that cost base puts the workable fee at the **top of the client's stated 2 to 5% range**; a 2% fee is loss-making per contribution before any overhead. Two facts make the number defensible:

- **The measured premium ladder** (evidence pass, not estimates): roughly 1.50% at 100 g, 0.95% at 1 kg. The fee can fall as bar denomination improves with scale, which is a real, explainable scale economy: the honest version of the "holders share in our success" story the dividend was trying to tell.
- **The tier discount is funded by time-phasing** (section 9.2): the cost base falls on the same clock the ladder deepens.

The fee is disclosed in full; the fabrication premium buried inside it means disclosed fee and retained margin are different numbers, and both are true (section 5.3). Rail cost varies by channel and the minimum ticket is rail-dependent: the per-request price of merchant Request to Pay collection is the single number that decides the collection floor, and it is a provider conversation, not desk research (section 14.4).

### 13.3 Custody recovery: nobody bills the saver

The client's 0.8 to 1% custody fee assumption is three to six times the researched cost of allocated storage (roughly 0.15 to 0.40% per year, pending the vault quote). More importantly, on a long-hold retail asset there is no good way to bill a saver for storage: a monthly cash bill dies on persistency (the bill outlives the touchpoint), deducting grams breaks the peg and sells the customer's own property, and dilution breaks 1 AURX = 1 gram.

**So: retail pays no storage fee, ever, and the metal is never touched.** Recovery moves to the counterparties that can be billed:

- **Gold Rewards is computed net of that customer's custody cost** (one line of arithmetic inside the existing cap), so the most engaged customers quietly cover their own storage.
- **The B2B platform fee** (stream 6) prices custody, register and licence into every partner-held gram.

This makes "no storage fee" a marketing claim against comparables that dilute or charge, funded by design rather than by subsidy.

### 13.4 Payment acceptance and the stablecoin position

The design accepts **bank money only**, into a segregated Client Account: never a token, never from an exchange's own account. The single test, applied at onboarding and at every payment: **whose bank account sends the money.**

Stablecoins are handled by signposting, not acceptance. UAE payment-token rules confine foreign payment tokens to registered issuers and to virtual-asset purchases; the widely held coins are not registered, the fee legs must settle in fiat regardless, and both tested workarounds fail (self-off-ramping is itself a licensable service; an embedded exchange widget makes the exchange Aurumix's agent). What works: **the customer converts on their own account at a licensed exchange and pays by bank transfer.** Aurumix publishes a list of licensed venues, takes no fee, passes no data, never touches a token. Whether publishing that list is "arranging" a payment-token service is the one load-bearing assumption in the payment design, and it is with counsel (legal brief, Question 6).

### 13.5 The partner channel

Stream 6 partners distribute AURX inside their own apps against the multi-tenant register. Partner-channel customers hold gold with full ownership protections and **no ICS**: no gate, no score, no tier. The behaviour is not observable (the partner owns the payment relationship), the benefits are not Aurumix's to give on that book, and the rewards funding cap would break. This makes the score a direct-channel feature, which is strategy as much as mechanics, and the partner agreement states it explicitly.
---

## 14. Assumptions register and open legal questions

### 14.1 How this register works

Every load-bearing assumption in the design is collected here, stated as a proposition that is either true or false, with where it bites and what changes if it fails. The seven highest-value questions are already with the project team in the companion legal brief (`Aurumix: Design Summary and Open Legal Questions`, 19 August 2026), framed for onward instruction of counsel; this section maps those questions onto the mechanisms and adds the register behind them.

Research method, for calibration of the confidence labels: load-bearing rules were fetched and read verbatim at primary source (the VARA rulebooks, the DIFC Trust Law 2018 text, the CBUAE rulebook, the scheme interchange schedule); claims that rest on secondary sources or could not be verified carry explicit confidence levels; and two of the project's own earlier readings were found wrong on verbatim verification and reversed (section 3.5.3), which is why the discipline exists.

### 14.2 The seven questions, mapped to the design

| # | The assumption to be tested | Gates | Where designed |
|---|---|---|---|
| 1 | A DIFC trust can define its beneficiary class as token holders from time to time, the deed can displace the writing formality, and that satisfies VARA's transfer-of-ownership test | The token architecture, the listing strategy, the capital charge, all marketing | 3.5, 4.3 |
| 2 | Allocated but fungible gold in a DIFC trust is out of reach of an onshore insolvency | The vehicle, and the safety promise to savers | 3.5, 3.6 |
| 3 | The buyback is a redemption; "equal value" means full value; an enforcement sale is outside the no-fee rule | All exit economics; credit default recovery | 3.7, 7, 10.4 |
| 4 | The vehicle is not a collective investment fund and its single-purpose trustee needs no licence | Whether the DIFC route is affordable | 3.5.4 |
| 5 | A valid security interest can be taken and perfected over a retail customer's beneficial interest, and the valuer/agent/buyer conflict is disclosable | The credit and card block | 10.5 |
| 6 | E-money collection providers satisfy the "third-party banks" client-money wording; publishing an exchange list is not "arranging" | Cross-border collection; the stablecoin position | 5.4, 13.4 |
| 7 | The succession product can be structured as a standing instruction outside will-writing, estate administration and fiduciary licensing | Whether the family product ships, and under what name | 11 |
| A | Indian residents cannot lawfully contribute (two limbs: remittance legality, and Aurumix's exposure in accepting or marketing) | The addressable market and the persona | 1.3, 11.4 |

Questions 1, 2 and 3 gate the product; the client's application build is due early September, and questions 1 and 7 carry direct build consequences (open versus permissioned token; whether the succession feature ships).

### 14.3 Further assumptions, by mechanism

**Held back from counsel deliberately** (they follow from the seven and several will answer themselves): whether VARA's client-asset estate exclusion reaches physical metal; whether the 2%-of-reserves capital component can bite where no Reserve Assets exist; whether the buyback engages Exchange or Broker-Dealer licensing; VAT treatment of the entry fee, the gold and the services (investment-grade metal is zero-rated, but under direct ownership Aurumix is arguably supplying gold, and the margin consequence of a 5% VAT surprise against a thin fee line must not be discovered late); the custody-fee authority question; how the wind-down plan interacts with the DIFC vehicle; whether a Gold Rewards gram credit may land on a regulatorily blocked account; and the mechanics of pledging under the trust.

**Design assumptions that are ours, not counsel's:**

| Assumption | Basis | If wrong |
|---|---|---|
| The persistency curve resembles Indian life insurance (79% at month 13, 38% at month 61) | Category benchmark; the closest behavioural analogue | The scoring calibration and the entire retention economics re-cut |
| The premium is zero (section 2.4) | Nine-protocol evidence, two discount cases | Only upside exists; nothing in the design depends on a premium |
| True allocated custody cost is 0.15 to 0.40%/yr | Research-derived; the vault quote decides it | If materially higher, custody recovery (13.3) re-opens as a pricing decision |
| The measured fabrication ladder (1.50% / 0.95%) | Same-page quote methodology, evidence pass | The fee build-up and minimum ticket move with it |
| A USD 20 floor is commercially necessary even where the rail makes it thin | Client's market positioning against AED 10 to 15 competitors | The collection minimum may split from the marketing minimum (an open client decision) |

### 14.4 The commercial unknowns

Four numbers cannot be closed by research and sit on the critical path as conversations:

1. **The two-way bullion dealer**: identity, spreads, minimum tickets, buyback commitment. Gates the float, the fee calibration and the exit (section 6.6).
2. **The vault quote**: the real annual custody cost per gram at Aurumix's scale. Decides how comfortable "no storage fee" is.
3. **The Request to Pay origination cost**: which bank or PSP will originate merchant collection requests for a gold-token merchant, at what per-request price. Sets the collection floor and decides the referral programme's economics. No UAE PSP publishes a policy on gold or virtual-asset merchants.
4. **The programme-manager interchange share**: unpublished anywhere in the region; the rewards ladder needs roughly 36% at the top tier (section 10.6).

A fifth is sequencing rather than a number: **approaching a bank before the licence exists creates a refusal record visible to other banks.** Bank conversations are ordered accordingly.

### 14.5 The India perimeter

Stated here because it shapes the persona, with the full brief in the legal document's Appendix A: gold is not a permitted asset class under the individual remittance scheme, the bullion-exchange route is expressly closed to resident individuals, crypto-purpose remittances are rejected in banking practice, and the tax treatment (flat 30% on virtual digital assets, no loss offset, plus foreign-asset reporting exposure) is punitive even where a route existed. The original specification's "USDT via P2P" route for Indian residents is deleted, not softened: it would put Aurumix in receipt of funds with no regulated counterparty and no source-of-funds visibility. The India-facing product is therefore: NRIs while non-resident, cash settlement to India-resident beneficiaries on death, a regulatory pause for the returning NRI, and a Year 3+ feeder-fund conversation if the client wants Indian retail at scale.

---

## 15. Risk and adversarial analysis

Each risk is stated with its mitigation and its residual. The design convention throughout has been to surface the uncomfortable number rather than smooth it.

### 15.1 Counterparty risk: the unnamed dealer

The single largest execution risk. The buyback promise runs entirely through a counterparty that does not yet exist in the plan (section 6.6). Mitigations: the float decouples daily operations from dealer timing; the sourcing covenant pre-authorises substitution; the exit's settlement windows are sized to the float, not the dealer. Residual: until a dealer signs, the fee build-up and the buyback capacity are specified but not calibrated. This risk is named to the client as a project risk.

### 15.2 Insolvency and custody risk

The threat: Aurumix fails and the customers' gold is trapped or taken. Mitigations are the four ownership layers (3.5.1), the client-money and client-asset estate exclusions (3.6), the segregation of the float from customer metal, and the wind-down plan with client-asset sales excluded (3.8). Residuals, honestly held: the onshore reclaim question for fungible gold is unresolved (Question 2), the title register is contract-backed rather than statute-backed (2.5), and an onshore court's treatment of the DIFC arrangement in a contested insolvency is untested. The layered design exists precisely so that any single failure leaves the claim standing.

### 15.3 Regulatory risk

- **Recharacterisation of the exit or the family fees as fee-bearing redemption** (III.E.4). Mitigations: no fee touches any exit path; the family fee strikes at registration; in-specie is the only paid succession service. The in-specie/redemption split goes to VARA in writing pre-application.
- **Reclassification of the token as a security.** Mitigations: no profit share, no yield language, no premium marketing, no scarcity mechanics, benefits earned by behaviour and capped at customer-generated revenue. The dividend stays dead; its deletion also protects the fund analysis (3.5.4).
- **The class-defined trust failing at counsel.** Mitigation: the proxy and hook make the permissioned fallback a switch, not a rebuild (4.4).
- **Marketing breach through the referral or agent channel.** Mitigations: single level, incentive pre-approval inside the licence application, disclosure duties, the liability rule internalised (12.6).

### 15.4 Market risk

- **Discount risk.** A thin listed market would price AURX below metal value (the two-discount-case evidence). Mitigation: no listing until the float is deep; the committed buyback is the floor; composable-capable is not listed (4.5).
- **Redemption run.** Section 7.4's machinery: tiered disclosed windows, the float, staged dealer sales, the suspension right bounded to force majeure. The structural comfort: the customers own the metal, so a run on Aurumix is not a run on their gold.
- **Gold price risk.** Carried by the customer as the product's nature; carried by the treasury only across the fill window (mean-zero, bounded); carried by borrowers only when they borrow (10.4).

### 15.5 Credit risk

Sits on the lender of record by structure. Aurumix's residuals: the stand-in authorisation hole (bounded by static rules and disclosed to the lender), the auth-to-settlement gap (closed by the 48-hour redemption hold), Sovereign borrowers' one-sigma exposure (disclosed, cured in stages), and the valuer/agent/buyer conflict (cured by zero-discretion pricing at the fix, and put to counsel as Question 5's third limb).

### 15.6 Behavioural and gaming risk

The anti-gaming register (8.7) closes six of eleven attacks structurally; the credit prize is de-fanged by seasoning plus strike-at-facility; the round-trip flag catches the residue with review rather than automatic punishment. Two consciously accepted residues, priced rather than policed: the referee contribution-collapse pattern (12.3) and the ballast-plus-small-SIP cycler (8.7). The acceptance and its trigger for reopening are recorded so neither resurfaces as an oversight.

### 15.7 Payment rail risk

Push-only collection removes bounce fees and mandate risk but leaves two dependencies: the Request to Pay origination cost (14.4) and the e-money/banks client-money question (Question 6). If the second fails, cross-border collection shrinks to wire-viable tickets, which is a material market change and would be known before launch rather than after.

### 15.8 Operational and continuity risk

The invariant set halts minting before any unbacked state can arise (6.5); attestation currency is a mint precondition, not a reporting nicety; the register and mint are multi-tenant from day one so partner books do not share a single point of failure with the direct channel; and the wind-down plan is drafted against the real mechanics (claim window, burn-on-redemption, freeze role, the monthly cash touchpoint as the contact rail). The known hard constraint on the September build: the three-second authorisation budget (10.3).
---

## Appendix A: Glossary

| Term | Meaning |
|---|---|
| Allocated gold | Specific, serial-numbered bars owned by identified persons, as opposed to an unallocated claim on a provider |
| AANI | The UAE instant-payments platform; Request to Pay is its collection feature |
| ARVA | Asset-Referenced Virtual Asset, VARA's category for tokens referencing an asset such as gold |
| AURX | The Aurumix token; 1 AURX = 1 gram of gold |
| Beneficiary Transfer Instruction (BTI) | The standing, pre-authorised instruction implementing the succession feature |
| Blocklist | A transfer control that denies listed addresses by exception; the opposite of an allowlist |
| Confirmed SIP | The gate: six consecutive counted contributions; permanent once earned |
| Counted period | A calendar month in which one accepted contribution at or above the floor cleared |
| DIFC | Dubai International Financial Centre, a common-law jurisdiction outside VARA's remit |
| Entry fee | The one-time percentage fee on each purchase; the product's primary revenue line |
| The fix | The LBMA gold price, the pricing benchmark for every event |
| The float | Aurumix-owned working gold inventory bridging retail tickets to wholesale bars |
| Gold Rewards | The monthly fee rebate credited in grams, capped at customer-generated revenue |
| ICS | Investor Conviction Score: min(Record, Standing) x Retention, 0 to 100 |
| JIT funding | Just-in-time authorisation: each card tap is approved live against collateral headroom |
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
13. AAOIFI Shari'ah Standard No. 57 (gold), section 7 (rahn) and 5/4/2.
14. ENBD Personal Banking Schedule of Charges (November 2023); Al Etihad Payments / CBUAE publications on AANI.
15. The Phase 1 market research record: nineteen-protocol landscape, 292 sources (Aurumix Protocol Landscape).

The full Phase 2 record (eleven decision drafts, the 51-entry decision log, sixteen process map sets, and the two verified statute texts) is available to counsel on request.

---

## Document control

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | 8 September 2026 |
| Prepared by | Tokenomics.net |
| Status | Consolidated design record, for the project team and counsel |
| Companion documents | Aurumix: Design Summary and Open Legal Questions (19 Aug 2026); Aurumix Process Maps (this deliverable's diagram set); the Phase 2 decision drafts (audit trail) |
| Basis | The client's 100 G Business Model (current specification), 51 logged design decisions, and primary-source regulatory research through September 2026 |
| Contact | Tokenomics.net |
