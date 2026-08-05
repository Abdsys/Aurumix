# Aurumix: Legal Entities, Licensing, Gold Ownership and Payment Rails

> **Status:** Phase 2 working draft, 2026-08-04.
> **Purpose:** answers the three structural questions the 100 G Business Model leaves open: which licences and entities are required, how the gold should legally be owned, and how customer money can lawfully be collected.
> **Method:** primary sources (VARA rulebooks, CBUAE rulebook, RBI, IFSCA) verified in a dedicated research pass. Every load-bearing claim carries a source and a confidence level. Items marked NOT ESTABLISHED are genuinely unresolved and are flagged for counsel.
> **Relationship to other drafts:** assumes the decisions in `_draft_allocation-and-float.md` (gold float, denomination, custody fee in cash, premium at zero) and `_draft_sip-spot-and-ics.md` (SIP and spot as transaction types, lock-in deleted, ICS measures behaviour only).

---

## 1. Where the client's document stands

The 100 G Business Model describes the product in fifteen sections and the company in none. Searched end to end, it contains:

- No named legal entity, anywhere. Not an issuer, not a proposed incorporation, not an applicant.
- No named bank, payment service provider or card programme partner.
- No customer terms, and therefore no statement of what an investor legally owns.
- No named gold dealer, which is the blocker already recorded as decision 1 in the handoff.

What it does contain is a correct list of the right worries. Section 14 flags token classification, the ICS Dividend, buyback classification, lending and card licensing, and defers each to legal counsel. That is honest, and it is not a plan.

The three gaps below are the ones this draft closes.

| Job | What the client's document says | What it actually gives you |
|---|---|---|
| Selling the token to the public | "Dubai, UAE, VARA regulated", "structured for VARA compliance from inception" | An intention. No entity, no licence category, no application. Also assumes one licence covers what are in fact three or four regulated activities |
| Owning the gold | Individual Gold Receipt: on-chain, non-pooled, "in the investor's name", "traceable to a specific vault location" | A strong record, not yet a legal right. No customer terms, no statement of the holding construct, no insolvency position |
| Handling the money | Section 11.2: AED or USDT for UAE, USDT or bank transfer for NRI, **USDT via P2P or OTC for Indian residents** | The weakest of the three. No bank, no PSP, no blocked-country list, and the route for the stated primary audience is not lawful |

---

## 2. The decision that comes before everything else

VARA's Guidance on VA Issuance uses gold as its worked example and splits gold-referenced tokens into two regimes. The choice between them determines the licence file, the capital requirement, the marketing story and the legal work.

> "if an Asset-Referenced Virtual Asset references or is linked to gold, then gold is the Reference Asset"
>
> "if an ARVA purports to maintain a stable link to the price of gold, then the Issuer will be required to hold gold as Reserve Assets, or potentially other assets such as derivatives relating to gold"
>
> "In instances where the ARVA provides a **direct right of ownership** of the Reference Asset ... then **Reserve Assets requirements do not apply**"

Source: VARA Guidance on VA Issuance, Version 1, `https://rulebooks.vara.ae/sites/default/files/en_net_file_store/VARA_EN_516_VER1.pdf`. Rulebook effective 19 June 2025. **Confidence: High.**

### The fork

| | Option A: Direct-ownership ARVA | Option B: Stable-value ARVA |
|---|---|---|
| What the customer owns | The gold grams themselves | A claim whose value tracks gold |
| Reserve Asset regime | **Does not apply** | Applies in full: licensed custodians only, legal segregation from the estate, no rehypothecation or pledging, regular risk assessment, and a legal opinion from a practising lawyer confirming compliance |
| Minimum paid-up capital | AED 1,500,000 | AED 1,500,000 **or 2% of average Reserve Asset market value over the preceding 24 months**, whichever is higher |
| The binding burden | Annex 2 III.B.1: prove ownership is "legally and validly established", transfers with the token, and satisfies title-transfer formalities | Hold, segregate, attest and never encumber the reserves |
| Compatible with the Gold Receipt narrative | Yes | **No.** The "your grams" story does not survive Option B |

Reserve Asset rules: `https://rulebooks.vara.ae/rulebook/c-reserve-assets`. Capital: `https://rulebooks.vara.ae/entiresection/472`. **Confidence: High.**

### Recommendation: Option A, direct-ownership ARVA

Three reasons, in ascending order of force.

1. It is the product the client already believes he is building. Option B silently deletes the Individual Gold Receipt, which is the strongest idea in the client's document.
2. It removes the Reserve Asset regime, which is the heaviest ongoing compliance burden in the issuance rulebook.
3. **The capital arithmetic is material.** At the Year 10 target of 60,000 to 100,000 investors, reserves could plausibly reach USD 200M. Two percent of that is USD 4M of permanently locked capital. Under Option A there are arguably no Reserve Assets to take 2% of, so the floor stays at AED 1.5M. **This is a multi-million dollar difference and it is a second, financial reason to choose direct ownership.** ⚠ Whether the 2% component can bite where no Reserve Assets exist is a counsel question with real money attached.

### The cost of choosing it, stated plainly

Option A trades one problem for a harder one. It requires proof that title actually transfers on-chain under UAE law. **That proof does not currently exist for Aurumix**, and the research pass could not locate a UAE statute or reported court decision confirming that an on-chain transfer moves legal title to vaulted gold. See section 4 and the NOT ESTABLISHED list.

This is a real legal opinion, not a formality, and it should be commissioned early. A negative answer forces Option B and rewrites the product.

---

## 3. Licences and entities

### 3.1 VARA's licensable activities

From Schedule 1, `https://rulebooks.vara.ae/rulebook/schedule-1-va-activities`. **Confidence: High.**

Advisory Services, Broker-Dealer Services, **Category 1 VA Issuance**, Custody Services, Exchange Services, Lending and Borrowing Services, VA Management and Investment Services, VA Transfer and Settlement Services.

Four compulsory rulebooks bind every VASP regardless of activity: Company, Compliance and Risk Management, Technology and Information, Market Conduct.

VARA's remit covers the Emirate of Dubai including free zones and special development zones, **excluding DIFC** (DFSA territory). ADGM is a separate emirate and outside VARA entirely. **Confidence: Medium** on the DIFC carve-out (consistent across law-firm sources, not confirmed against the text of Law No. 4 of 2022).

### 3.2 The licence stack Aurumix actually needs

| Activity | Regulator and category | Build or partner | Cost |
|---|---|---|---|
| **Issuing AURX** | VARA, **Category 1 VA Issuance** | **Build.** The core licence | AED 100,000 application, AED 200,000 per year, AED 1.5M capital |
| **Whitepaper approval** | VARA, per asset. Machine-readable, published **before any offering or marketing** | Build. Mandatory | Additional fee, not published |
| Buyback window | Sits inside the issuance licence via Annex 2 III.E.1. **But** a buyback providing liquidity or price support may engage Exchange or Broker-Dealer Services | Counsel question | +AED 50,000 if a second activity is added (extension = 50% of the lower application fee) |
| **Lending against pledged gold** | **CBUAE, not VARA.** Requires a bank or full Finance Company licence under the Finance Companies Regulation. The **Restricted Licence** category cannot be used: its Short-Term Credit definition excludes any collateral lien | **Partner.** Licensed lender is lender of record and owns the loan book; Aurumix is contracted agent for technology, origination, customer interface and collections | Contractual |
| **Gold Card** | **CBUAE**, Retail Payment Services and Card Schemes Regulation (Circular 15/2021). **The CBUAE reserves the sole right to issue BINs** | **Partner.** A CBUAE-licensed bank must hold the BIN and be named as issuer; Aurumix acts as programme manager | Contractual |
| Profit share to holders | Likely SCA and/or VARA VA Management and Investment Services | **Do not put it on the retail token.** See 3.3 | n/a |

Fee schedule: `https://rulebooks.vara.ae/rulebook/schedule-2-supervision-and-authorisation-fees`. **Confidence: High.** Note that widely circulated tables showing VA Transfer and Settlement at 100k/200k are wrong; that activity is 40k/80k.

CBUAE lending: `https://rulebook.centralbank.ae/en/rulebook/finance-companies-regulation-0`. **Confidence: Medium.**
CBUAE cards and BINs: `https://rulebook.centralbank.ae/en/rulebook/article-18-card-schemes`. **Confidence: Medium.**

**Redemption is optional, not mandatory.** VARA: "Entities Licensed to issue an ARVA are not mandated to provide owners and/or holders with a right of redemption." Where a right is granted, holders must be able to redeem for equal value denominated in AED plus any other forms disclosed in the whitepaper, within a reasonable period, with no fee charged. **Confidence: High.** ⚠ This directly supports the cash-buyback-only design. It also means **a redemption fee cannot be charged on the redemption right itself**, which has consequences for the decaying spot redemption fee in `_draft_sip-spot-and-ics.md`. Flag for reconciliation.

Secondary sources claiming "redemption at par within one working day" for ARVAs are wrong; the one-working-day rule attaches to fiat-referenced tokens. **Confidence: Medium.**

### 3.3 The dividend, restated with the rulebook in hand

VARA's Annex 2 ARVA definition **expressly reaches tokens representing "entitlement to receive or share any Income."** **Confidence: High.**

The consequence is more subtle than "the dividend needs a different licence." A profit share does not push AURX out of the issuance regime. It makes the whitepaper approval materially harder and adds SCA exposure on top of it. This is a third independent reason for the Gold Rewards design already recorded as decision 6: a fee rebate credited in grams, funded from interchange and credit revenue, capped at what that customer generated, sized by ICS tier earned through behaviour, and never described as a yield.

If the founders want a genuine profit share, the transplantable structure is Kinesis's. Keep AURX a clean commodity token under VARA. Issue the profit share as a **separate, capped instrument, privately placed to a small accredited base** under an Offering Memorandum, in DIFC or ADGM. Kinesis's KVT is capped at 300,000 units and takes 20% of all transaction fees. Same economics for the founders, none of the retail classification damage.

### 3.4 The entity map

Four things to stand up, of which only two are companies to build now.

| | What | Where | Why it exists |
|---|---|---|---|
| **1. Aurumix (Issuer)** | The VARA-licensed company | Dubai, any free zone except DIFC | Holds the licence, holds the customer relationship, **receives all customer money**, issues AURX, publishes the whitepaper, carries the AED 1.5M capital |
| **2. Aurumix Technologies** | App and platform company | Any free zone, ordinary tech or software licence, no financial licence | Builds and runs the Circle app. Keeps software liability and IP off the licensed balance sheet |
| **3. Gold-holding vehicle** | See section 4 | DIFC or ADGM | Holds legal title to the metal so it is not Aurumix's asset on insolvency |
| **4. Partners, not entities** | Two-way dealer, vault, independent assayer, CBUAE-licensed lender, BIN sponsor bank | Contracts | Four to five signatures, no additional licences |

Two rules, both drawn directly from Comtech's failure mode.

- **The entity that receives customer cash must be the licensed entity.** Comtech's customers pay into an account belonging to COMTECH CORE TRADING FZCO, a name appearing on neither published licence.
- **The entity named as issuer in the whitepaper must be the entity on the register.** Comtech markets as "ComTech Gold" and is registered as ComTech FZCO (DAFZA) on a precious-metals *trading* licence.

### 3.5 Indicative cost to reach launch

| Item | Indicative |
|---|---|
| VARA application, Category 1 Issuance | AED 100,000 |
| VARA annual supervision | AED 200,000 per year |
| Minimum paid-up capital | AED 1,500,000 (locked, not spent) |
| Smart contract audit, 9 contracts | USD 75,000 (the client's own figure, and it is realistic) |
| Legal opinions: title transfer, token classification, India perimeter | NOT ESTABLISHED. Budget generously |
| DIFC or ADGM holding vehicle | Setup plus annual maintenance |

Approximately **USD 550,000 to 750,000 of capital and fees before any build cost**, and six to nine months minimum. ⚠ **VARA publishes no approval timeline.** Any date given to investors is an estimate, and should be labelled as one.

---

## 4. How the gold should be owned

### 4.1 The two-layer problem

There are two separate things to protect and only one is solved by the licence.

**Layer 1, the token.** VARA solves this outright, and more strongly than assumed. Company Rulebook Rule V.B.2:

> "Client VAs are not depository liabilities or assets of the VASP. Client VAs are not owned by the VASP and shall not form part of the VASP's estate in the event that the VASP is or becomes Insolvent."

`https://rulebooks.vara.ae/entiresection/123`. **Confidence: High.** This is a statutory estate exclusion, not merely a duty to keep separate books. Supporting rules: V.B.3 requires client VAs in separate wallets labelled as such at all times; V.B.4 requires 1:1 holding and prohibits rehypothecation absent explicit client consent and relevant licensing; IV.B.2 and IV.B.3 apply the same estate exclusion to Client Money.

**Layer 2, the metal.** VARA's rule attaches to the *virtual asset*. It says nothing about who owns the bars in the vault. **The research pass found no authority bridging the two regimes.** Closing that gap is the actual work.

### 4.2 The recommended construct: four independent layers

Build it so four separate things each assert that the customer owns the gold. No single failure should collapse the claim.

**Layer 1. Allocated, never unallocated.** This is the decisive choice. The IMF's framing: allocated gold "remains in the ownership of the individual or institution placing it for safe custody" and is "an asset without a counterpart liability", whereas an unallocated holder "does not hold title to physical gold but instead holds an unsecured claim against the account provider ... the account holder is a creditor." **Confidence: Medium-High.** Requires serial-numbered bars with a weight list showing bar number, gross weight, assay and fine weight, per LBMA account guidance.

**Layer 2. Bailment language in the customer terms.** Kinesis has the strongest wording in the market and it should be copied: legal and beneficial title remains with the holder, and the issuer holds the bullion as bailee with each holder taking an undivided interest in proportion to holding. Bailed property is not the bailee's asset. It costs nothing to draft and it is stronger than what either Tether or Paxos say.

**Layer 3. A DIFC or ADGM holding vehicle.** DIFC Trust Law No. 4 of 2018 Article 14(2): a transfer to a trust "shall not be void, voidable or liable to be set aside by reason of a Settlor's bankruptcy, the liquidation of a Settlor, or any action or claims made against a Settlor by any creditor" (`https://www.difc.com/business/laws-and-regulations/legal-database/difc-laws/trust-law-difc-law-no-4-2018`, **Confidence: High**). ADGM Foundations Regulations 2017 Article 33 is equivalent. **Onshore UAE offers nothing comparable that could be verified.** Note also that ADGM *trusts* appear weaker than ADGM *foundations* on this axis: commentary indicates there is no equivalent to Article 33 in the Trusts (Special Provisions) Regulations 2016.

The structure this implies: **the issuer stays in Dubai under VARA, and the metal is held through a DIFC or ADGM vehicle where the insolvency protection is written into statute.**

**Layer 4. A DMCC Tradeflow warrant.** DMCC's own material describes warrants as "electronic document[s] of title" and states that in the storage operator's liquidation creditors cannot reach the commodities because title sits with the warrant holder. The storage operator, not DMCC, issues the warrant; DMCC acts as registrar under the DMCC Warrant Rules annexed to a Corporate Access Agreement. **Confidence: Medium.** ⚠ Caveat honestly: this rests on DMCC's contractual framework rather than a naming statute, and **no reported UAE court decision on the point was found.** It is a strong fourth layer, not a foundation to build on alone.

Tradeflow membership runs in six categories: Owner, Storage operator, Financier, Islamic financier, Quality inspector, Additional service provider. Operationally the Owner delivers bars into an approved vault, the Storage operator issues the warrant against identified bars, and title can then be transferred or pledged between registered members. **DMCC publishes no fee schedule**, which confirms the standing open item: Tradeflow economics can only be obtained from DMCC directly.

### 4.3 Design considerations that follow

**Fungibility is the weak point.** Gold is interchangeable, which is exactly why allocation with serial numbers matters. **The gold float must be legally separated from customer metal and never commingled with allocated customer bars**, or the ownership claim degrades toward a creditor claim. This is a new constraint on the float design in `_draft_allocation-and-float.md` and should be folded into it.

**The custody fee needs written authority.** If the customer owns the grams, selling a slice to pay Aurumix requires an express contractual power. The existing decision to charge the custody fee in cash sidesteps this entirely, and is now supported by a second reason.

**The wind-down plan is mandatory, not optional differentiation.** VARA Company Rulebook Part VII.A requires one at all times, with twelve prescribed contents (`https://rulebooks.vara.ae/rulebook/wind-down-plan`, **Confidence: High**). Two provisions matter most:

- **Rule 1.k:** the plan must ensure that the sale of Client Money or Client VAs is "explicitly excluded from, and not necessary for, implementing or completing the Wind Down Plan, or any other plan ... directed by an Insolvency Appointee, or the sale of the VASP's assets or business as a going concern."
- **Rule 1.l:** VARA retains "the power and ability to intervene and/or assume the direction and/or control of Client Money and/or Client VAs."

Notification within one day of the decision to wind down, then weekly reporting through completion.

⚠ **This revises decision 10 in the handoff.** The earlier framing was that a published wind-down plan is unclaimed ground Aurumix can take cheaply. That remains true as to *publication*, since no regulated crypto or tokenized-asset issuer has published a complete one. But Aurumix is **required** to have one regardless. The correct framing is: you must build it anyway, so publishing it is free differentiation.

---

## 5. The money

### 5.1 Rule one: foreign stablecoins cannot pay for services, and the carve-out that matters

The CBUAE Payment Token Services Regulation (Circular 2/2024) governs payment tokens in mainland UAE, excluding DIFC and ADGM. **No UAE merchant may accept a virtual asset as payment for goods or services unless it is a Dirham Payment Token from a CBUAE-licensed issuer. Foreign Payment Tokens such as USDT and USDC are confined to purchasing virtual assets or virtual asset derivatives.**

`https://rulebook.centralbank.ae/en/rulebook/introduction-84`. **Confidence: High**, verified across three independent sources. The one-year transition ended **14 June 2025** and the regime applies in full.

**The carve-out is the design insight. AURX is a virtual asset, so a USDT-to-AURX purchase may sit inside the permitted use of a Foreign Payment Token.** The fee legs do not: entry fee, custody fee and credit fees are payments for services and must settle in fiat or in a licensed Dirham Payment Token.

🔄 **SUPERSEDED 2026-08-05. The carve-out has two conditions, not one, and USDT fails the first.** The operative wording permits a *"Foreign Payment Token issued by a **Registered** Foreign Payment Token Issuer being lawfully used as a Means of Payment for purchase of Virtual Assets."* Both limbs must hold. As at 29 January 2026 the only registered Foreign Payment Token found was **USDU** (Universal Digital, ADGM); no evidence Tether or Circle have registered or been refused. **Confidence: High** on the two-limb reading, **Medium-High** on the registration list, which rests on a regulatory tracker rather than a CBUAE register.

**Design consequence, restated:**

- The token purchase leg **may** settle in a *registered* Foreign Payment Token. **Not USDT, not USDC.**
- The fee legs **must** settle in AED, USD or a licensed Dirham Payment Token.
- **The route that works today: the customer converts on their own account, at a licensed exchange, before paying.** Aurumix receives an ordinary bank transfer. See `_explainer_how-we-take-money.md` for the four payment paths and the signpost list.

⚠ **Two workarounds tested and ruled out.** (a) Accepting USDT and off-ramping it yourself fails: conversion is itself a licensable Payment Token Service, and **routing an unregistered token through a licensed processor does not cure its status**. (b) The PTSR is drafted as *"No Person shall perform any service, within the UAE or directed to Persons in the UAE"*, so **the merchant is bound, not just the token issuer**. Aurumix would be the party in breach.

⚠ **Addition to the licence stack in section 3:** VARA and SCA licensees that custody, transfer or convert stablecoins reportedly require a **CBUAE Non-Objection Registration**. **Confidence: Medium**, commentary rather than rulebook. Verify before relying on it.

Note also Federal Decree-Law No. 6 of 2025, which added virtual-asset payment services to the CBUAE perimeter with in-scope operators required to comply or cease by **September 2026**. **Confidence: Medium.**

### 5.2 Rule two: the payment rail is a product parameter, not an implementation detail

Cost of collecting a single USD 20 SIP contribution:

| Rail | Cost on USD 20 | Source |
|---|---|---|
| UAE domestic card | ~4.25% | Stripe AE published pricing, 2.9% + AED 1 |
| International card | ~5.25% | as above, plus 1% international |
| US ACH | ~0.8% | Stripe US, capped |
| UK Faster Payments | ~0% to receive | Wise Business |
| Singapore local | 0 to 2.5% | Wise / Airwallex |
| UAE Direct Debit (UAEDDS) | Bank-set, low | `https://www.centralbank.ae/en/uaedds/` |

**Confidence: High** on card interchange (UAE domestic debit e-commerce interchange is 1.00% capped at AED 50 per Visa's published UAE disclosure schedule); **Medium** on the acquirer margin split.

**Set this against the entry-fee build-up already calculated in `_draft_allocation-and-float.md`:** fabrication premium 3.0% + price-gap risk 0.36% + float cost of capital 0.49% + rail 0.30% = 4.15% before margin. That build-up assumed a 0.30% rail. **A card rail at 4.25% replaces 0.30% and pushes the break-even entry fee above 8%**, against a stated fee range of 2 to 5%.

**A USD 20 contribution collected by card is loss-making before any gold is purchased.**

Three design responses, in order of preference:

1. **Default every customer to account-to-account.** UAEDDS direct debit for UAE residents; local collection accounts in the UK, US, Singapore and GCC through a multi-country provider (Airwallex, Wise Business, Currencycloud, Payoneer, OpenPayd and Banking Circle all offer this).
2. **Make the minimum ticket rail-dependent.** USD 20 by direct debit, a higher floor by card, or a disclosed card surcharge.
3. **Treat card as a convenience for larger tickets and for spot purchases**, not as the SIP default.

⚠ The entry-fee build-up section owed to `_draft_allocation-and-float.md` must now carry a rail-cost row that varies by channel, not a single 0.30% figure.

### 5.3 Banking and PSPs: what is actually available

**Banks documented as serving licensed VASPs:**

- **Zand Bank.** Full CBUAE banking licence (July 2022) plus a VARA VASP custody licence (December 2024), and CBUAE approval to issue Zand AED, a regulated AED-backed stablecoin. **Confidence: High.** Note Comtech also banks with Zand.
- **Commercial Bank of Dubai.** Launched dedicated VASP core banking and publicly onboarded Laser Digital (Nomura's VARA-licensed arm) as its first VASP client. **Confidence: High.** This is the clearest named bank-VASP relationship in the market.
- Emirates NBD, Mashreq, RAKBANK, Emirates Islamic and Wio are cited by practitioners as onboarding selectively. **Confidence: Low**, practitioner lists rather than bank disclosure.

**Practical requirements:** a licence is effectively a precondition, banks do not onboard unlicensed crypto firms; the full AML stack (MLRO, monitoring, travel-rule tooling) must exist before approach; two to six months typical. ⚠ **Approaching a bank pre-licence creates a refusal record visible to other banks.** Sequence matters. Client-money accounts additionally require a CBUAE No Objection Certificate. **Confidence: Medium.**

**CBUAE licence categories for collecting payments** (Retail Payment Services and Card Schemes Regulation, **Confidence: High**):

| Category | Authorises |
|---|---|
| I | Payment account and instrument issuance, merchant acquiring, aggregation, domestic and cross-border transfer, payment token services |
| II | As I, without payment token services |
| III | As II, without cross-border transfer |
| IV | Payment initiation and account information only |

Recurring card payments are not a separate licence; they run on a cardholder mandate over an acquiring relationship.

**PSPs with confirmed recurring-billing support in the UAE:** Adyen, PayBy, PayCaps, Stripe. Network International is the largest MEA acquirer. **Confidence: Medium.**

⚠ **No PSP publishes a policy on serving gold, precious-metals or virtual-asset merchants.** These sit in non-public onboarding risk criteria and MCC assignment. **This cannot be closed by desk research and is a live commercial risk**, in the same category as the Dubai dealer conversation.

**Card programme.** Two routes: obtain a CBUAE Stored Value Facilities licence, or partner with a licensed bank BIN sponsor. Documented live example: **ADIB as BIN sponsor with Al Fardan Exchange as programme manager** for a Visa multi-currency prepaid card. **Confidence: High.** Prepaid needs only SVF/payment authorisation. **Credit cards require a bank or licensed finance company with lending authority.** ⚠ The Gold Card as described (a credit line against pledged gold) is the harder of the two and should launch prepaid-first if it launches early at all.

**Travel Rule.** VARA's threshold is **AED 3,500** (approximately USD 950), not the USD 1,000 stated in the client's document. Originator and beneficiary information must be obtained and held before initiating a transfer above that value; information must accompany all transfers regardless of size, with verification waived below threshold absent risk indicators; aggregation applies at AED 3,500 per day. `https://rulebooks.vara.ae/entiresection/16`. **Confidence: High.** Unhosted wallets require enhanced due diligence rather than being prohibited. VARA publishes no approved-vendor list; IVMS101 messaging via 21 Analytics, Notabene or TRISA, and analytics via Chainalysis, TRM Labs or Elliptic, are the market-standard choices.

---

## 6. India: the answer is no, and what to do instead

### 6.1 Two independent legal bars

**Bar one: gold is not a permitted LRS asset class.** LRS permits investment in overseas shares, securities, mutual fund units, ETFs and immovable property. Offshore bullion holdings sit outside that list. LRS is a foreign-exchange sourcing route, not a permission to hold any asset, and it does not override substantive FEMA restrictions on what a resident may hold abroad. RBI LRS FAQ: `https://www.rbi.org.in/commonperson/english/scripts/FAQs.aspx?Id=1834`. **Confidence: Medium-High** (rests on the absence of a permission plus settled AD-bank practice, not an explicit RBI "no gold" clause).

**Bar two, and this is the decisive one. IFSCA Circular 329/IFSCA/DPM/TS/2022-23/1, dated 17 June 2022, expressly prohibits resident individuals from buying Bullion Depository Receipts on IIBX through the LRS route.** Wording: resident individuals "are not permitted to transact/invest in BDR on IIBX through the LRS route." The sole carve-out is for Qualified Jewellers notified under DGFT, and only for gold import. Still in force as of 2026. **Confidence: High**, confirmed against the circular PDF and independent secondary coverage.

**GIFT City is not the workaround. It is where the prohibition is written down most explicitly.** RBI Circular No. 15 of 10 July 2024 widened LRS-to-IFSC routing to all permissible LRS purposes, but it broadened the *routing*, not the *universe of permitted assets*. An IFSC account is a conduit, not a permission upgrade.

### 6.2 Three further layers on top

- **Crypto remittance is blocked in practice.** No RBI circular expressly addresses LRS for virtual assets, but AD banks reject remittances where the purpose is digital currency or tokens, and require an express declaration. **Confidence: High** that the route is closed, **High** that no explicit statutory bar exists.
- **Tax treatment is materially worse than the domestic alternative.** Section 115BBH applies a flat **30%** on income from transfer of any virtual digital asset, with only cost of acquisition deductible, **no set-off of losses against any income including other VDA gains**, and no carry-forward. Section 194S adds 1% TDS. `https://www.incometaxindia.gov.in/w/section-115bbh-1`. **Confidence: High.** A resident is better off, on tax alone, with physical gold or an Indian gold ETF.
- **Foreign-asset reporting.** Schedule FA disclosure is required of a resident and ordinarily resident even where no income arises, with the Black Money Act 2015 behind it: 30% tax plus a penalty of three times the tax, plus prosecution. **Confidence: Medium-High.**

### 6.3 Soliciting Indian residents

Three regulators with overlapping jurisdiction. **SEBI** (section 12 registration requirement, applied extraterritorially to India-facing websites and onboarding), **RBI** (which maintains a public Alert List of unauthorised entities, grown from 34 in September 2022 to 40-plus, naming eToro, Exness, OctaFX, Olymp Trade, XM and others, and stating that residents transacting on unauthorised platforms "shall render themselves liable for legal action under the FEMA"), and the **ED** under FEMA and PMLA with asset attachment powers. The Alert List is explicitly non-exhaustive, so absence from it implies nothing. `https://rbi.org.in/scripts/bs_viewcontent.aspx?Id=4235`. **Confidence: High.**

### 6.4 Decision: delete the P2P USDT route

**Section 11.2's "USDT via P2P or OTC" for Indian residents must be deleted, not softened.**

It is not a grey area the customer carries. Aurumix would be receiving funds through a channel with no regulated counterparty, no source-of-funds visibility and no audit trail. That is the opposite of what a VARA licence requires, and it is the fastest available route to losing a licence that took nine months to obtain. The document's mitigation, "investor bears Indian tax disclosure obligation", does not address Aurumix's own exposure, because Aurumix is the party accepting the funds.

### 6.5 Refocus, not downgrade: the NRI and GCC-resident saver

- Approximately **9 million Indians live in the GCC alone**, and they are precisely the "LIC subscriber, not DeFi user" persona in the project charter.
- **As non-residents they sit outside FEMA's LRS regime entirely.** Their money is already offshore and already free to invest.
- They already remit monthly. A monthly gold SIP maps onto an existing behaviour rather than creating one.
- The Year 10 target of 60,000 to 100,000 investors is reachable inside the NRI base alone.

### 6.6 Two India-adjacent items for counsel, not for assumption

- **The inheritance question.** FEMA generally permits a resident to hold foreign assets acquired by inheritance from a person resident outside India. If that holds, the **Family Portfolio and Digital Will naming Indian-resident beneficiaries may be the one legitimate India touchpoint**, where direct investment is not. Worth a specific question, because it preserves a headline feature for the target community. ⚠ Do not assume it, and do not market it until confirmed.
- **The feeder-fund route.** The only demonstrated structure by which a foreign product reaches Indian retail at scale is a SEBI-registered domestic feeder or fund-of-fund through an Indian AMC. That is a Year 3+ conversation, requires an Indian counterparty, and inverts who owns the client relationship. Park it, do not close it.

### 6.7 One live risk to monitor

In June 2025 the RBI was reported to be preparing to bar LRS use for offshore time deposits and lock-in interest-bearing instruments. **No gazetted amendment was found, so treat this as unconfirmed.** But a gold savings product with a lock-in and a yield is exactly the shape described. It is a further reason the lock-in deletion (decision 19) and the Gold Rewards reframing (decision 6) were correct.

### 6.8 The blocked-country list

The product currently has none, which means the operative answer is "anyone, anywhere". That will not survive a licence application. Minimum contents:

- FATF high-risk and monitored jurisdictions, and all sanctioned jurisdictions.
- **Indian residents, for now.**
- Separate carve-outs for the credit product where consumer lending is not permitted. Precedent: Ledn excludes the EU and Canada from its gold-backed credit facility.

---

## 7. Consequences for the rest of the Data Room

- 🔴 **The project charter's primary persona changes.** It currently names an Indian resident. It should become the NRI and GCC-resident saver, with UAE residents and other international behind them. **This must be settled before Phase 4 revenue modelling**, because market size, persistency assumptions and ticket size all move with it.
- ✅ **This unblocks two of the six parked client additions of 2026-07-28:** item 2 (which countries we can accept from) and item 5 (minimum numbers covering annual expenses, plus NRI research), which item 2 gated.
- ⚠ **`_draft_allocation-and-float.md` needs three amendments:** the float must be legally segregated from allocated customer metal (4.3); the entry-fee build-up needs a rail-cost row that varies by channel rather than a flat 0.30% (5.2); and the buyback must be reconciled with VARA's rule that no fee may be charged on a redemption right (3.2).
- ⚠ **`_draft_sip-spot-and-ics.md` needs one reconciliation:** the decaying spot redemption fee against the same no-fee-on-redemption rule.
- ⚠ **The client's document contains two figures to correct:** the Travel Rule threshold is **AED 3,500**, not USD 1,000; and Section 11.2's Indian resident row must be removed.
- The process-mapping work already queued should add an entity-and-money-flow diagram: customer, licensed issuer, client account, dealer, vault, title register, and which box each partner occupies.

---

## 8. Open items

**For the client's counsel, in priority order. These are the three that only the client can commission.**

- [ ] **Direct-ownership ARVA or stable-value ARVA**, and can counsel produce an opinion that title in allocated gold validly transfers with an on-chain token under UAE law? *Determines the product, the capital requirement and the marketing.*
- [ ] **Does a USDT-to-AURX purchase fall inside the Payment Token Services Regulation's virtual-asset carve-out**, and must the fee legs settle separately in fiat? *Determines whether the funding rail survives.*
- [ ] **Confirm the India perimeter**, and specifically the inheritance carve-out for Digital Will beneficiaries. *Determines the addressable market.*

**Consequential, and they arise only because Option A is chosen.**

Under Option A the customer owns the metal, so every downstream mechanic stops being a contract question and becomes a **property** question. None of these is a reason to reject Option A. They are the price of the capital saving and the "your gold" claim, and the client should see the bill.

- [ ] **Does VARA's client-asset protection reach the metal at all?** Rule V.B.2 excludes Client Money and Client **Virtual Assets** from the estate. Physical gold is neither. If the rule does not reach the bars, statute in another jurisdiction has to, which is the case for the DIFC or ADGM holding vehicle.
- [ ] Whether the **2%-of-Reserve-Assets capital component** can bite where a direct-ownership ARVA has no Reserve Assets. Potentially several million dollars.
- [ ] **Is the buyback a redemption or a purchase?** Under Option A the customer owns the gold, so Aurumix buying it back is arguably purchasing an asset from them rather than redeeming a claim. Determines whether VARA's no-fee-on-redemption rule applies, and whether operating it triggers Exchange or Broker-Dealer licensing.
- [ ] **What authority is needed to charge the custody fee?** Deducting grams means selling the customer's property. Confirm that charging in cash avoids this, which is the current design.
- [ ] **How is a pledge taken over customer gold** for the credit facility? This is a security interest over a third party's property, not over Aurumix's own. Tradeflow supports pledging; confirm the mechanism and enforceability.
- [ ] 🆕 **The Digital Will is materially heavier under Option A.** Transferring a *claim* on death is contractual. Transferring *ownership of gold* is a succession matter, pulling in UAE succession law, Sharia forced heirship where applicable, and the succession law of every beneficiary's home jurisdiction. This was not previously flagged and it should be raised before the Digital Will is built.
- [ ] **Where do Gold Rewards grams come from?** Crediting a customer with grams is a transfer of ownership from Aurumix's own metal, and needs the same title mechanism as everything else.
- [ ] 🆕 **VAT treatment, flagged as a question rather than a finding (not researched).** Investment-grade precious metals are zero-rated in the UAE, but under Option A Aurumix is arguably *supplying gold* rather than supplying a service. Comtech's app charges 5% VAT on commission. Confirm the treatment of the entry fee, the custody fee and the gold separately. ⚠ This has direct margin consequences against a 4.15% cost build-up and should not be discovered late.

**For us.**

- [ ] Identify a two-way Dubai bullion dealer. Still decision 1, still blocking, still a conversation rather than research.
- [ ] Obtain DMCC Tradeflow membership terms and fees directly from DMCC. Four research passes have now returned the same negative result.
- [ ] Approach Zand Bank and Commercial Bank of Dubai on sequencing. ⚠ Establish licence status first; a pre-licence refusal is visible to other banks.
- [ ] Establish whether any UAE PSP will underwrite a gold-backed-token merchant with recurring small-ticket collection. Not answerable by desk research.

**NOT ESTABLISHED, and material.**

- Whether fungible commingled gold can be reclaimed from an onshore UAE bankruptcy estate. **The pivotal gap.** Requires the Arabic official text of the Civil Transactions Law provisions on deposit and the Bankruptcy Law provisions on third-party property.
- Whether a DMCC Tradeflow warrant is a document of title as a matter of UAE statute rather than DMCC contract. No statute, no case law found.
- Whether a UAE court would give effect to VARA's Rule V.B.2 estate exclusion over physical gold. Untested.
- Any published VARA approval timeline for licensing or whitepaper approval.
- ARVA reserve attestation frequency. The "independent audit every six months" claim appears only in secondary commentary.
- Minimum paid-up capital by VARA activity other than ARVA issuance.
- Whether a commodity-referenced token is a "payment token" under the PTSR at all, since the PTSR addresses fiat-referenced tokens. Affects which regulator applies to the funding rail.
- Whether the RBI's June 2025 proposal on offshore time deposits and lock-in instruments was ever notified.
- Any UAE vault operator's allocated-storage terms. No standard form exists and none of Brink's, Loomis, Malca-Amit or Transguard publish theirs.
