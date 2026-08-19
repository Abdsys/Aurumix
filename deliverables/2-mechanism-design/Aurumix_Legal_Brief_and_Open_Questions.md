# Aurumix: Design Summary and Open Legal Questions

**Prepared by:** Tokenomics.net
**For:** Aurumix project team, for onward instruction of counsel
**Date:** 19 August 2026
**Status:** For review

---

### How to use this document

Part 1 describes what Aurumix is building, in enough detail that a lawyer with no prior exposure to the project can act on Part 2. It is a summary. The full design sits in the mechanism design deliverables and can be supplied on request.

Part 2 sets out seven questions. These are not everything we would like to know. They are the questions whose answers determine other answers, so resolving them collapses a much longer list.

**Questions 1 to 6 follow the same four-part shape:**

1. **What we decided, and why.** The design choice we have already made, and the reasoning behind it.
2. **The assumption it rests on.** Stated plainly, as a proposition that is either true or false.
3. **What we need confirmed.** The actual ask.
4. **What changes if the assumption is wrong.** The consequence, and the fallback if we have one.

The second item is the important one. **In those six cases the assumption is the question.** We have designed to a specific reading of the law, and we would rather show that reading and have it corrected than ask an open question and receive an essay. If an assumption is wrong we need to know now, while the design is still cheap to change.

**Question 7 is deliberately different.** On succession we do not have a settled position to put to you, so we have simply asked how the product can be offered lawfully. Where we have no view worth defending we would rather say so than manufacture one.

Appendix A covers India, which needs Indian counsel rather than UAE counsel and is presented separately for that reason.

**A note on references.** We have deliberately not cited specific articles, rules or sections anywhere in this document. We are not lawyers. We would rather describe a rule and a set of facts accurately than risk attaching a wrong reference to a right question, and we would rather counsel located the governing provision themselves than worked from our reading of where it sits. Where it helps, we can share the specific provisions we have been working from.

**One point of framing.** The VARA rulebook provides that an issuer of this kind of token may be required to give VARA a legal opinion, from a properly registered lawyer, confirming explanations made to VARA or statements contained in its whitepaper. Several of the questions below are matters on which VARA may require exactly that as a condition of licensing. This is not preparatory work that can be deferred until after the application goes in.

---

## Part 1: What Aurumix is building

### 1.1 The product

AURX is a gold-backed savings token to be issued from Dubai under a VARA licence.

- **Backing.** 100% of every dollar received buys physical gold. There is no reserve pool, no algorithmic component and no hard cap on supply. Supply is a consequence of purchases.
- **Denomination.** 1 AURX = 1 gram of gold. Token count equals gram count, so the backing position reads directly off the two ledgers.
- **Exit.** Cash buyback only. There is no physical redemption and no delivery of bars to customers. This is deliberate.
- **Customer.** Long-term retail savers, principally non-resident Indians and GCC residents. The product is built for a saver accustomed to a life insurance premium schedule, not for a crypto trader. India is closed to residents (Appendix A).

### 1.2 How customers buy

Two transaction types on one account, not two classes of customer.

| | SIP (systematic) | Spot |
|---|---|---|
| Pattern | Monthly, on the customer's own anniversary | On demand |
| Amount | Variable month to month. Hard floor USD 20, target USD 75, no maximum | No minimum beyond the product floor |
| Missed payment | Costs score only. No financial penalty, no forfeiture | Not applicable |
| Lock-in | None. The contractual lock has been deleted | None |
| Earns score | Yes | No |

Payment is push-only: AANI Request to Pay, or a prefunded balance drawn automatically each month. There is a five day grace window. A payment below the USD 20 floor is rejected and returned rather than partially credited.

### 1.3 The scoring layer

Customer benefits are governed by an Investor Conviction Score (ICS), which measures **behaviour and never amount**. A customer saving USD 20 a month and one saving USD 2,000 a month reach the top tier on the same day.

```
ICS = min(Record, Standing) x Retention
```

Record is length of contribution history. Standing is recent discipline. Retention reduces the score if the customer sells, with a 30% annual allowance before any effect. The score is gated: below six consecutive contributions there is no score at all. Five tiers, four of them named: No tier, Silver (25), Gold (50), Platinum (75), Sovereign (100).

Five benefits are tiered against it: an entry fee discount, a credit facility loan-to-value ladder (50 / 65 / 80 percent), a payment card tier, a rewards rebate paid in grams, and a discount on family and succession services.

### 1.4 The order of operations on every purchase

Money, then title, then token. Never any other order.

1. Funds are collected and held as client money.
2. A gold price is struck against the LBMA fix.
3. Grams are calculated net of the entry fee.
4. **Title to those grams passes to the customer** in the title register.
5. **Only then** are tokens minted to the customer's address.

On exit the sequence reverses: checks run, price is struck, tokens are burned, grams return to the float, cash settles to the customer's own name-matched bank account. Because an exit returns grams to the float rather than forcing a sale, the dealer spread is paid on net outflow, not on gross exits.

### 1.5 The credit facility and the card

The purpose is to let a saver reach the value of their gold without selling it, which is what makes a long hold tolerable. There is **one facility with two ways to draw on it**: a cash drawdown, and spending on a payment card that draws against the same limit. The customer pledges gold they already own as collateral and keeps ownership of it throughout. Pledged gold continues to earn their score, so using the facility does not set the customer back. How much they can borrow depends on tier: 50 percent of the gold's value at Gold, 65 at Platinum, 80 at Sovereign. The ratio is struck once when the facility opens rather than recalculated on each draw, and gold must have been held for 90 days before it counts as collateral.

**Aurumix neither lends nor issues the card.** A licensed partner is lender of record and owns the loan book, and a licensed bank is the card issuer of record, because a VARA permission does not extend to advancing cash and only a licensed bank can issue cards. Aurumix is the programme manager: the app, the customer relationship, origination, valuing the collateral and servicing. If gold falls in value the response is staged rather than sudden: notice first, then a cure window to top up or repay, and only then a partial sale of just enough gold to restore the ratio. The customer is never wiped out in one step. **Question 5 asks whether the pledge at the centre of this actually works.**

### 1.6 The family and succession product

A customer can name beneficiaries against their account and record what should happen to their gold. There are two triggers: a **lifetime trigger**, where the customer chooses to pass gold to a named person while alive, and a **death trigger**. On a death trigger Aurumix requires a grant of probate before anything moves, so the gold does not bypass the estate. The feature operates only on gold held in the customer's Aurumix account, which means a withdrawal to self-custody takes those grams outside its reach entirely (and, deliberately, counts as a sale for scoring purposes). Where gold is pledged against a credit facility, the loan is settled first and only the balance passes. Alongside this sits a **Family Portfolio**, which lets related accounts be grouped and viewed together during the customer's life.

Our provisional contractual term is **Beneficiary Transfer Instruction**: a standing instruction the customer gives us in advance, which we execute once the trigger is evidenced. Aurumix does not draft, witness or register a will, does not decide who is entitled to an estate, does not validate a death, and does not advise on estate planning. **That boundary is our best guess rather than a settled position, which is why Question 7 asks how this should be structured instead of proposing an answer.**

### 1.7 The legal and operating structure

This is the part that generates the questions.

- **The issuer** is a Dubai entity holding a VARA virtual asset issuance licence. It cannot sit in DIFC, because VARA's remit covers Dubai including free zones but excludes DIFC.
- **The token is an Asset Referenced Virtual Asset (ARVA) of the direct-ownership kind, not the stable-value kind.** This distinction is the hinge of the entire structure. Under the VARA rulebook, a token that maintains or claims to maintain a stable value against its reference asset must hold and manage a formal pool of reserve assets. A token representing a direct right of ownership of the underlying asset does not. Choosing direct ownership removes that reserve regime and, with it, a capital charge we estimate at up to roughly USD 4M of locked capital. The price of that choice is that we must prove title genuinely moves with the token.
- **Legal title to the metal is intended to sit in a DIFC trust vehicle,** not with the issuer. The customer holds a beneficial interest. Holding it onshore with the issuer as bailee was rejected on insolvency grounds. Naming each customer directly at the vault is impossible at USD 20 ticket sizes.
- **The beneficiary class is defined by token holding.** The intended construction is that a customer's beneficial interest arises on receipt of AURX and ends on transfer of it, by operation of the trust's own terms, with no separate written assignment and no register write.
- **The token is a plain, open ERC-20 with a blocklist,** denying transfers only by exception (sanctions, court order, fraud). It is not an allowlist and not a permissioned standard. VARA mandates no token standard anywhere. We have checked this against the full rulebook text.
- **Lending and cards are Central Bank matters, not VARA matters,** and the design partners rather than builds. A VARA lending permission does not extend to advancing cash. Lending against pledged gold requires a bank or full finance company licence. A card requires a Central Bank licensed bank as issuer of record.

### 1.8 Where the law bites

The design is complete on economics and mechanics. It is incomplete at exactly seven points, and at each of those points the answer is a legal one that we cannot supply. Those seven points are Part 2.

Three of them gate the build directly. The client's application build is due early September, and two design choices (whether the token ships open or permissioned, and whether the succession product ships at all) cannot be finalised without answers.

---

## Part 2: The questions

Ordered by consequence. Questions 1 to 3 gate the product. Questions 4 to 7 gate individual mechanisms.

---

### Question 1: Does title pass with the token?

**This is the question. Almost everything else moves depending on the answer.**

**What we decided, and why.**

We chose the direct-ownership form of token over the stable-value form, because the stable-value form drags in a formal reserve asset regime and a capital charge we put at up to roughly USD 4M. Direct ownership avoids that entirely. It also matches what we want to tell the customer, which is that they own gold rather than a claim tracking the price of gold.

Having chosen it, we then had to make ownership actually move when the token moves. We rejected keeping a separate register and writing to it on every transfer, because a second ledger that must be kept in step with the first is exactly the divergence the regulator is worried about. Instead the DIFC trust deed defines its beneficiaries as the holders of AURX from time to time. The customer's interest arises when they receive the token and ends when they transfer it, automatically, because the class is defined by reference to the token ledger itself.

That construction is also why the token can be a plain open ERC-20 with only a blocklist. If title follows the class automatically, nothing needs to gate transfers to keep the records aligned.

**The assumption it rests on.**

> That DIFC trust law lets a trust define its beneficiaries as the holders of a token from time to time, that the trust deed can override the default requirement for a beneficiary to deal with their interest in writing, and that the resulting arrangement satisfies VARA's requirement that ownership actually transfers whenever the token transfers.

We understand the equivalent English rule on writing is mandatory and cannot be overridden. Our assumption depends on DIFC having genuinely departed from English law on this point, and on that departure being effective.

**What we need confirmed.** Please treat these as three separate answers, because they have different fallbacks.

1. Can the beneficiary class validly be defined as token holders from time to time?
2. Can the deed override the written-instrument default?
3. If yes to both, is that enough for VARA? Our intended answer to the regulator is that divergence between token and ownership is structurally impossible rather than operationally monitored.

**What changes if the assumption is wrong.**

If limb 1 or 2 fails, we fall back to a permissioned token writing to a register on every transfer. That is buildable, but it is a token contract rebuild plus a new identity layer, and it forecloses any open listing or third-party use of AURX. If the direct-ownership claim fails altogether, the reserve asset regime and its capital charge come back, and the marketing has to change from ownership to exposure.

**Please tell us which limb fails, not only that the combination does.**

---

### Question 2: Is the customer's gold protected from Aurumix's insolvency?

**What we decided, and why.**

We chose to put legal title in a DIFC trust vehicle rather than holding the metal onshore with the issuer as bailee. The reason is narrow and specific: the VARA protection that keeps client assets out of a failed issuer's estate is written in terms of virtual assets, and gold bars are not virtual assets. So the tokens are protected by that rule and the metal behind them, on its face, is not. The DIFC trust is there to close that gap, relying on a provision of DIFC trust law that protects assets transferred into a trust from being unwound because the transferor later becomes insolvent.

We accepted the cost and complexity of a second entity specifically to buy this protection.

**The assumption it rests on.**

> That gold which is allocated to a customer but physically fungible can in fact be kept out of an onshore UAE bankruptcy estate, and that routing it through a DIFC trust materially improves that position rather than merely appearing to.

Each customer's holding is allocated and segregated from Aurumix's own metal, but per-customer bar allocation is impossible at one gram ticket sizes. The assumption therefore has to survive the fungibility point.

**What we need confirmed.**

1. Can allocated but fungible gold be reclaimed from an onshore UAE bankruptcy estate?
2. Does the DIFC vehicle materially improve that, and does the trust law protection do the work we are relying on?
3. Is there DIFC Court authority on how strong a beneficiary's interest is against third parties, given the trust law carries no express insolvency-remoteness statement?

**What changes if the assumption is wrong.**

If the DIFC vehicle does not improve the position, we are paying for an entity that buys nothing and should collapse the structure back onshore. More seriously, we intend to tell savers their gold is safe if Aurumix fails. **If this assumption is wrong we have to withdraw that claim before we make it,** which materially weakens the product against competitors making the same promise.

We should also flag that ADGM is **not** a drop-in substitute. Our understanding is that assets in an ADGM foundation are not the beneficiary's until distributed, which would defeat the direct-ownership claim in Question 1 outright. If ADGM is preferred for any other reason, it needs fresh analysis rather than substitution.

---

### Question 3: What is a "redemption", and what does the no-fee rule reach?

**What we decided, and why.**

The VARA rulebook says that where a token of this kind gives holders a right of redemption, redemption requests must be processed **without the issuer charging any fee at all**. That rule is absolute. The rules around it are conditional: they only bite to the extent the token grants a redemption right in the first place.

We could therefore have designed our way out, by structuring the buyback so it is not a redemption right. **We deliberately chose not to.** A gold token with no credible, committed exit tends to trade below the value of its backing, and the credibility of the exit is most of what makes the product trustworthy to a retail saver. So we treat our published buyback as a redemption right and accept the consequence: **no fee of any kind on the way out.** We have already deleted a decaying exit fee from the design on that basis.

We also chose the stricter of two readings of "equal value", assuming it means full prevailing value rather than value net of what a dealer would actually bid.

**The assumption it rests on.**

> That a published, formulaic buyback commitment counts as a right of redemption even though our whitepaper never uses that word; that "equal value" means full prevailing value with no haircut; and that a forced sale of pledged gold on a defaulted credit facility is **not** caught by the same no-fee rule.

The rulebook does not define "redemption" anywhere. We have checked. Every part of this assumption is inference from structure rather than from text.

**What we need confirmed.** Three separate answers again.

1. Is the buyback a right of redemption for these purposes?
2. Does "equal value" mean full value, or realisable value net of the dealer's bid?
3. Does the no-fee rule reach an enforcement sale on a defaulted facility?

**What changes if the assumption is wrong.**

If the buyback is **not** a redemption, the whole regime is optional for us and the design loosens considerably. That is the pleasant failure, though we would still hesitate to take the escape for the commercial reason above. If "equal value" means net of the dealer's bid, the question becomes who absorbs the two-way gold spread on every single exit, and the answer changes our margin on every transaction. If an enforcement sale **is** a redemption, we cannot charge recovery costs on a defaulted loan, which feeds directly into Question 5.

We would prefer point 1 confirmed by VARA in writing during pre-application dialogue rather than by opinion alone. A post-launch recharacterisation would be very expensive and asking now costs almost nothing.

---

### Question 4: What is the DIFC vehicle, for regulatory purposes?

**What we decided, and why.**

The client's original model included a profit-sharing dividend paid to token holders. We removed it. There were several reasons, but one of them is structural: our understanding is that the collective investment fund test turns, in substance, on participants sharing in profits or income from the assets, together with those assets being pooled or managed as a whole. A profit share would have pushed the vehicle towards that test. Allocated gold that produces no income, is not managed, and is fixed per customer should sit outside it.

We also assumed a company acting as trustee of one trust, doing no trust business for anybody else, does not need a licence to do that.

**The assumption it rests on.**

> That the holding vehicle is not a collective investment fund, and that a single-purpose trustee for one trust is exempt from licensing.

**What we need confirmed.**

1. Is the vehicle a fund?
2. Is the single-purpose trustee exempt?
3. Separately and practically: an indicative all-in figure for formation and annual maintenance, including trustee arrangements.

**What changes if the assumption is wrong.**

If it is a fund, the cost and licensing burden may make the DIFC route unaffordable, which reopens Question 2 with no good answer. Point 3 is not a legal question but we are currently telling a founder "this structure costs money" without a number, which is not a fair basis for a build decision.

**A forward-looking note.** If the client ever revisits the profit-sharing dividend, this answer is one of the reasons it should stay deleted. Reintroducing it may also bring the securities regulator into frame.

---

### Question 5: Can we take security over gold we also custody?

**What we decided, and why.**

A VARA lending permission does not extend to advancing cash, so we do not lend. A Central Bank licensed partner is lender of record and owns the loan book. Aurumix is programme manager, valuer and collateral agent. The customer pledges gold they beneficially own, held in the DIFC vehicle, and on default that gold is sold to repay.

We chose to take security under DIFC law rather than ADGM, because ADGM's security register appears to capture only charges created by ADGM companies, and a retail customer granting the security would fall outside it. We also built a Sharia-compliant variant against the recognised Islamic finance standards, under which the lender may not use or re-pledge the collateral and must sell at market value on default and return any surplus.

**The assumption it rests on.**

> That a valid, enforceable and perfectable security interest can be taken over an ordinary retail customer's beneficial interest in the DIFC vehicle, and that Aurumix acting at once as valuer, collateral agent and (through the buyback) buyer of that collateral is a conflict that can be managed by disclosure rather than one that has to be structured away.

**What we need confirmed.**

1. Can the security interest be validly taken and perfected, and how?
2. Does AURX qualify as a digital asset under DIFC law? If not we would take security over the beneficial interest as an ordinary intangible instead, and we need to know which route applies.
3. Is the valuer / agent / buyer conflict disclosable, or structural?

**What changes if the assumption is wrong.**

**If the security interest is not clean, the credit facility and the card do not work.** Both are central to the product: the facility is what lets a saver access value without selling their gold, and it is one of the two benefits that make the tier ladder worth climbing. Losing it would force a redesign of the benefit set, not just the removal of a feature. If the conflict has to be structured away rather than disclosed, we need a third-party valuer or collateral agent, which adds cost to every facility.

Note also that this question is coupled to Question 3. If an enforcement sale counts as a redemption, we cannot charge recovery costs, which changes the pricing of the facility independently of whether the security itself is good.

---

### Question 6: Two payment questions that decide whether cross-border saving works

Both are narrow and cheap to answer. The second decides whether the business model functions outside the UAE at all.

**What we decided, and why.**

We concluded that a VARA licence lets us take customer fiat directly under the client money rules, with no separate Central Bank licence. That removed the need for the stablecoin funding route in the client's original model, which we have deleted. USDT and USDC cannot be accepted anyway, because a foreign payment token issuer must be registered with the Central Bank and neither is.

Customers who hold stablecoin therefore convert it themselves at a licensed exchange and pay us by bank transfer. We never touch the token. To make that usable we intend to publish a list of VARA-licensed exchanges, with no commercial arrangement, no referral fee and no customer data passed to anyone.

For collection, we chose local collection accounts through providers such as Airwallex, Wise Business, Currencycloud, Payoneer or OpenPayd. The reason is arithmetic: an international wire costs USD 15 to 50 against a USD 75 monthly contribution, which is not a product.

**The assumptions they rest on.**

> **6a.** That VARA's requirement for overseas client money to sit in client accounts with third-party **banks** outside the UAE is satisfied by these providers, which are e-money institutions rather than banks, and whose virtual accounts typically sit at a partner bank **in the provider's name** rather than ours.

> **6b.** That publishing a list of licensed exchanges, with no commercial arrangement and no data passed, is not "arranging" a payment token service and needs no permission we do not hold.

6b is the only load-bearing assumption in the entire payment design.

**What we need confirmed.** Both assumptions, directly. Yes or no is genuinely sufficient.

**What changes if the assumptions are wrong.**

If 6a fails, cross-border SIP collection is not economically viable, and the product effectively shrinks to customers who can pay from a local UAE bank account. That is a very large change to the addressable market. There is soft evidence pointing the wrong way: at least one VARA-licensed exchange's own UAE terms refuse deposits routed through cross-border payment providers and e-wallets, accepting only local bank transfers.

If 6b fails, we either obtain a permission we had not planned for, or we stop signposting and accept that stablecoin holders have to find their own way to convert.

---

### Question 7: How can we offer the succession product lawfully?

The product is described in section 1.6. **This question is open on purpose:** unlike the six above we are not putting a position to you, because we do not have one worth defending. No VARA licence covers trust, fiduciary, estate administration or will-writing activity, and we hold no adjacent permission.

**So the question is simply: how do we offer this lawfully, and can we offer it at all?**

Three things we would like covered:

1. **Structure.** Can it sit outside will-writing, estate administration and fiduciary licensing, and if not, what licence or partner would we need?
2. **Applicability.** Are there customer groups or jurisdictions where this cannot be offered, or where local succession rules limit what we are able to promise? Our customers sit across the GCC and the wider diaspora, and we would rather narrow the offer at the outset than withdraw it later.
3. **Naming.** Does calling it a "Digital Will" imply a regulated service on its own, whatever the underlying mechanism?

**Timing.** This carries a build consequence. The client's application is due early September, and we need to know whether the feature ships, ships reduced, or does not ship.

---

## Appendix A: India (for Indian counsel)

For Indian counsel, not for UAE counsel. This determines the size of the addressable market rather than the legality of the structure.

### The question that matters most

> **Can we accept monthly SIP contributions from Indian residents?**

Everything else in this appendix is subsidiary to it.

**Our reading is no.** Gold and bullion are not a permitted asset class for resident individuals under the Liberalised Remittance Scheme, and we understand the financial services regulator has expressly barred resident individuals from holding bullion receipts on the domestic bullion exchange through that route. Buying crypto assets has never been approved as a permitted purpose under the scheme either. The client's original model routed Indian residents through peer-to-peer stablecoin purchases, with the investor carrying the tax and disclosure risk. We removed that route.

**We want this confirmed rather than assumed, because we changed the product's target customer on the strength of it.** The persona moved from the Indian resident saver to the non-resident Indian and GCC resident saver, and the revenue model, the marketing and the distribution plan all follow from that. If our reading is wrong, the addressable market is very much larger and we should reopen it.

Please answer it in two limbs, because they can fail independently:

1. **Can a resident lawfully remit for this,** given a recurring monthly contribution rather than a one-off?
2. **Is there exposure for us in accepting them,** or in marketing to residents in India, whether directly or through an agent network?

### If the answer is no, three questions follow

A resident who cannot buy may still inherit, and someone who bought lawfully may later become a resident.

1. **Does the inheritance exception reach a tokenised commodity?** The rules permit a resident to hold assets inherited from someone who was resident outside India, but the categories listed are foreign currency, foreign securities and immovable property. An allocated-gold token is arguably none of the three.
2. **Can a beneficiary be settled in cash instead?** For any India-resident beneficiary we would pay cash through banking channels rather than transfer the token, so no resident ever holds AURX. We believe this sidesteps the classification question entirely and would like that confirmed. **This is the cheapest answer available to us if it works.**
3. **What happens to a returning NRI?** Our reading is that they may keep what they acquired while non-resident but cannot add new money. The product currently cannot tell a regulatory stop apart from a missed payment, and that distinction affects their score and their credit facility.

Separately, on lifetime transfers rather than inheritance: a gift from a person resident outside India may fall outside the foreign exchange regime altogether and into the foreign contribution rules, and whether it does appears to turn on the donor's **passport rather than their residence**. An Indian-passport NRI is generally not treated as a foreign source; a foreign-passport OCI may be. That distinction is too fine to enforce inside an application, so we have blocked lifetime transfers to India at launch. Please tell us if that is more cautious than it needs to be.

---

## What we are not asking

To keep this list short we have deliberately held back roughly a dozen consequential questions that follow from the answers above rather than standing independently. They include how far VARA's client asset protections reach into physical metal, whether the buyback is a redemption or a purchase for licensing purposes, VAT treatment, the mechanics of charging any custody fee, and how the wind-down plan VARA requires interacts with the DIFC vehicle.

We will send those as a second batch once the seven above are resolved. Several of them will answer themselves.

---

## Summary table

| # | The assumption we need tested | What it gates | Priority |
|---|---|---|---|
| 1 | Title moves automatically with the token via a token-defined beneficiary class | The product, the capital charge, the token build, all marketing | Blocking |
| 2 | Allocated fungible gold in a DIFC trust is out of reach of an onshore insolvency | Onshore vs DIFC vehicle, and a promise we make to savers | Blocking |
| 3 | Our buyback is a redemption, "equal value" means full value, enforcement sales are outside the no-fee rule | All exit economics, and credit default recovery | Blocking |
| 4 | The vehicle is not a fund and its trustee needs no licence | Whether the DIFC route is affordable | High |
| 5 | Security over a retail beneficial interest is valid, and our conflict is disclosable | The credit and card block | High |
| 6 | E-money institutions satisfy the "banks" requirement; signposting is not arranging | Whether cross-border saving works at all | High |
| 7 | **Open question, no position taken.** How can the succession product be offered lawfully, and to whom? | Whether the family product ships, and its name | High |
| A | **Can we accept SIP contributions from Indian residents?** We read it as no | Addressable market size, and the target customer | Indian counsel |

**Questions 1, 2 and 3 are the ones we would ask first if only three could be asked.** The client's application build is due early September, and questions 1 and 7 both carry build consequences.
