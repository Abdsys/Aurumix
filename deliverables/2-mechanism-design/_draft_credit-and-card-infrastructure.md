# Credit and Card Infrastructure

> **Phase 2 decision draft, 2026-08-13.** How the lending facility and the Gold Card actually work, who builds each piece, and what happens when the gold price falls.
>
> **The headline: they are not two products. They are one gold-secured revolving credit facility with two draw channels**, and the card is the channel that makes the economics work.
>
> Companion to `_draft_ics-benefits.md` (§2 credit, §3 card), which defined *what the tiers buy*. This defines *how it is delivered and by whom*. Where they conflict on infrastructure, this wins; where they conflict on tier values, the scoring draft wins.
>
> **Research basis:** five parallel primary-source sweeps run 2026-08-13. Confidence is marked on every load-bearing claim. **Five findings in §11 correct existing drafts and two reverse a stated position.**

--- 

## 0. The five things that changed

| # | What we believed | What the primary sources say | Where it bites |
|---|---|---|---|
| 1 | The VARA Lending licence might let the facility advance tokens at AED 500k capital instead of AED 150M — *"the question that dwarfs everything else"* | **It cannot.** VARA's definition requires the *same virtual asset* be lent and returned. A fiat advance is outside it | Retire the counsel question. Partnering is confirmed, not merely likely |
| 2 | No UAE lender publishes a gold-collateral LTV | **Emirates Money publishes 80%**, gold vaulted at DMCC with Brink's | Decision §6.2's 80% now matches an incumbent, not a hope |
| 3 | Debit/prepaid interchange capped 0.75%, credit uncapped | Correct in substance, **wrong in detail**: prepaid is 1.00% flat, and credit runs **1.80–2.30% by product level** | The plastic ladder is now a *numeric* revenue ladder |
| 4 | ADIB + Al Fardan is our card precedent | Real, but **prepaid, not credit**, and it is a **four-party** structure including a processor | Weaker precedent than cited; a whole role was missing from our model |
| 5 | The Restricted Licence fails because Short-Term Credit excludes a collateral lien | **No such provision exists.** It fails on an **AED 20,000 per-borrower cap** | Same conclusion, wrong reason. Fix before it reaches counsel |

---

## 1. One facility, two draw channels

**The problem this solves.** Our drafts describe "credit" and "the card" in separate sections with separate partners, which invites the client to buy two integrations, negotiate two contracts, and build two ledgers. They are the same thing.

| | Cash draw | Card draw |
|---|---|---|
| What the customer does | Requests a lump sum to their bank account | Taps at a shop |
| Typical use | Hospital bill, school fees, business need | Groceries, fuel, travel |
| Collateral | The same pledged grams | The same pledged grams |
| LTV | The same tier ladder | The same tier ladder |
| Balance sheet | The same lender | The same lender |
| Revenue | Stream 5 only | **Stream 5 + stream 2 interchange** |

**One facility, struck once, drawn two ways.** The customer sees one borrowing limit in the app; the card and the cash button both spend against it.

⚠ **This forces a rule the benefits draft does not have.** §2.1 says the LTV is *"struck at the draw"* and existing draws *"never reprice"*. A card is thousands of tiny draws, so a literal reading re-strikes on every coffee. **The correct rule: the facility is struck once, at facility opening, and each draw inherits the facility's struck LTV.** See §6.4 for the review-date rule this makes necessary.

---

## 2. The stack: four roles, not two

| Role | What it does | Who carries the risk |
|---|---|---|
| **Issuer processor** | Real-time authorisation, card lifecycle, Apple/Google Pay tokenisation, the card ledger | Operational |
| **Issuer of record (BIN)** | The licensed name on the card | Scheme and regulatory |
| **Lender of record** | Advances the money, owns the loan book | **Credit** |
| **Programme manager (Aurumix)** | Customer, app, origination policy, collateral valuation, the authorisation decision, servicing, collections | Operational and reputational |

**The processor is the piece every existing draft omits**, and it turns out to be where the hardest engineering sits (§5).

⚠ **The BIN premise needs re-testing.** Our drafts state that *"the CBUAE reserves the sole right to issue BINs"*. **No such clause was found** in the Retail Payment Services and Card Schemes Regulation. The operative constraints appear to be **Visa/Mastercard principal membership** plus RPSCS licensing. **Confidence: Low on our stated mechanism.** This matters commercially — see §3.

---

## 3. Recommended providers

### 3.1 Issuer processor — **NymCard**

Dubai Media City. **Principal member of both Visa and Mastercard.** Its own materials state it issues *"prepaid, debit, credit, virtual, and tokenized cards on native processing"* and explicitly supports *"installment, revolving credit, and embedded lending programs"*. PCI DSS, PCI SSF, SOC 2, ISO 27001. Named clients include EDB Bank, Byblos Bank, Faisal Islamic Bank, Nasspay, Samsung. `https://nymcard.com/` — **Confidence: High.**

**Why this is the recommendation, and why it may remove a counterparty.** NymCard is credit-capable, UAE-native, and a *principal scheme member in its own right*. Combined with the unverified BIN premise above, **the card side may collapse from bank-plus-processor to a single vendor.** That is worth an hour of NymCard's time before any bank conversation.

Alternatives: **Network International** (verified UAE issuing presence, publishes the UAE IRF schedule to its customers), **Magnati** (Careem Pay), **Rêv Worldwide** (the processor inside the ADIB/Al Fardan programme).

### 3.2 Lender of record — **Emirates Money**, then **Mashreq**

| Candidate | Why | Confidence |
|---|---|---|
| **Emirates Money Consumer Finance LLC** (Emirates NBD subsidiary, CBUAE reg. 02.01.01.018.2008.02) | Runs *Loan Against Gold* at **up to 80% LTV**, jewellery or bullion, min gold value AED 30,000, **vaulted at DMCC's gold vault operated by Brink's Global Services DMCC**. They already do our product, at our number, in our vault | **High** on the product; unestablished on third-party origination |
| **Mashreq** | The strongest UAE lender-of-record precedent: the Cashew embedded-lending framework (Apr 2026) combines *"Mashreq's regulated lending, credit decisioning, and risk governance"* with a fintech platform, funding up to AED 150,000 over 48 months. Mashreq also took a $10M stake | **Medium-High** |
| **Commercial Bank of Dubai** | The only institution spanning all three axes: launched an **XAU-denominated Gold Metal Loan** (June 2026), provided debt financing to BNPL originator Postpay, **and** runs dedicated VASP accounts (first client: Laser Digital) | **Medium-High** |
| **Finance House LLC** | Live Gold Loan, AED 5,000–200,000, tenor 6 months to 4 years, 18K+, 1% processing, 1% insurance. Publishes **no LTV** | **High** on product |

**Recommendation: open with Emirates Money.** They have already solved the collateral question we are about to ask a lender to solve, and the DMCC/Brink's alignment means our custody structure needs no explaining. **Mashreq is the fallback** because they have demonstrably taken third-party originated consumer credit onto their book, which Emirates Money has not been shown to do.

### 3.3 Banking for the token side — **Zand**, with **CBD** as second

**Zand Bank** holds a **VARA custody licence** (Dec 2024, first UAE bank with institutional crypto custody, Taurus as tech partner), received a CBUAE No Objection Certificate, and is reported as banking partner to nearly all UAE VASPs. Launched Zand AED, a CBUAE-approved dirham stablecoin, Nov 2025. **Confidence: High.**

**CBD** launched dedicated VASP accounts covering client money and prudential requirements, compliant with both CBUAE and VARA rules. **Confidence: High.**

Both confirm decision 28's shortlist. **Sequencing warning from decision 28 still applies: approaching a bank pre-licence creates a refusal record visible to other banks.**

### 3.4 Vault — **Brink's Global Services DMCC**

Not a new recommendation, but a newly *load-bearing* one: Emirates Money already lends against gold held there. Choosing the same vault removes a diligence conversation from the lending negotiation.

---

## 4. Setting the limit

```
Borrowing headroom  =  seasoned, unpledged grams  ×  LBMA fix  ×  LTV(tier)
```

| Gate | Rule | Source |
|---|---|---|
| Eligibility | **Gold tier.** Credit does not unlock at the Confirmed SIP gate | Scoring §6.2 |
| Seasoning | Grams enter the base only after **90 days held**. Redeemed-then-rebought restarts. Inbound transfers start fresh | Benefits §2.5 |
| LTV by tier | **Gold 50% · Platinum 65% · Sovereign 80%** | Scoring §6.2, settled 2026-08-13 |
| Stacking | Seasoned **and unpledged** only. One gram supports one facility | Benefits §2.5 |
| Strike | Struck once at **facility opening**, not per draw | §1 above, new |

Worked, at an illustrative USD 115/g:

| Tier | 50 g collateral | LTV | Facility limit |
|---|---|---|---|
| Gold | ~USD 5,750 | 50% | ~USD 2,875 |
| Platinum | ~USD 5,750 | 65% | ~USD 3,740 |
| Sovereign | ~USD 5,750 | 80% | ~USD 4,600 |

---

## 5. How a card tap actually works — JIT Funding

This was an open question in every prior draft. It is answerable: the industry pattern is **Just-in-Time Funding**, documented publicly by processors.

**The sequence, in under one second:**

1. Customer taps. The network sends an authorisation message to the processor.
2. The processor calls **Aurumix's endpoint**: *can this be funded?*
3. Aurumix computes live: seasoned unpledged grams × current fix × LTV(tier) − outstanding balance.
4. Aurumix answers **approve**, **decline**, or **partial approval** — approving up to remaining headroom rather than declining outright.

**Three consequences the build team must absorb:**

| Fact | Consequence |
|---|---|
| **Aurumix owns the balance, not the bank.** In JIT funding the programme manager must *"manage your own ledger balances"* | The authoritative available-credit figure lives in our risk engine, not the lender's. We are the real-time collateral valuer |
| **The re-mark frequency is *every transaction*** | Collateral is not re-priced on a schedule and pushed. It is pulled and evaluated per tap, bounded only by the freshness of our gold price feed |
| **There is a hard three-second budget.** Marqeta declines the transaction if the gateway does not respond in three seconds | Valuation, LTV computation, hold-check and decision must complete inside three seconds *including network round trip*. This is a real architectural constraint on the September build |

**Confidence: High** — processor's own developer documentation.

### 5.1 🔴 The stand-in hole, and it cannot be closed

Two independent fallbacks approve transactions **with no collateral check at all**:

| Failure | Who decides | Our control |
|---|---|---|
| **Aurumix unreachable** → processor invokes **Commando Mode** | The processor, from pre-agreed static rules | Partial — we write the static rules |
| **Processor unreachable** → the card network performs **STIP** (stand-in processing) | The card network, unilaterally, notifying afterwards | **None** |

In both paths we learn about the spend after the fact. **This is an unavoidable, permanent hole in a collateral-backed card programme** and it must be disclosed to the lender rather than discovered by them.

**Recommended Commando Mode rules** (Aurumix's only lever): max USD 250 per transaction, max 3 transactions per card, **decline all ATM withdrawals**, **decline all cross-border**, hard stop after USD 500 cumulative. Sized so the worst case on any single account is immaterial against even a Gold-tier facility.

### 5.2 The auth-to-settlement gap — borrow Gnosis Pay's answer

Authorisation and clearing are separate messages, and settlement is typically T+1. A customer could in principle move collateral in between. **Gnosis Pay solves this with a mandatory delay module on withdrawals** — a time buffer that makes draining collateral between auth and settlement physically impossible.

Our 90-day seasoning does not cover this: seasoning governs what *enters* the base, not what *leaves* between auth and clearing. **Recommendation: a 48-hour hold on any redemption request from an account with an active card facility.** Small, invisible to a saver, and it closes the gap.

⚠ **No operator in the market publicly documents an explicit price-movement buffer between auth and settlement.** The LTV band does the work implicitly.

---

## 6. The liquidation ladder

### 6.1 What the market does, and why neither model fits us

| Regime | How it buys safety | Example |
|---|---|---|
| **Crypto / tokenised gold** | A **price buffer** plus instant liquidation | Nexo on PAXG: originate 70%, warnings at 71.4 / 74.1 / 76.9%, liquidate 83.33%, partial restore to below 80% — a **13.3-point gap** |
| **Indian physical gold** | **Time compression** plus procedure | RBI 2025 Directions require LTV *"maintained on an ongoing basis throughout the tenor"*, so the trigger **is** the cap and the price buffer is **zero**. Protection is a 12-month bullet tenor plus a days-long procedural ladder |

**A card facility has neither short tenor nor atomic liquidation**, so it needs the widest explicit buffer of the set, plus the procedural protections.

### 6.2 The recommended ladder

Absolute thresholds, not relative to the struck LTV — because the benefits draft requires them to be **quotable** and spaced above each step.

| LTV | What happens | Precedent |
|---|---|---|
| **≤80%** | Normal. No action | Max origination |
| **85%** | **Notice.** App and push. Informational only, no action required | Nexo's graduated warning ladder |
| **88%** | **Cure notice.** Formal, in writing. **14 days** to top up gold, repay part, or add cash | Manappuram: 2 weeks from receipt to close or *"replenish the security with additional gold"* |
| **92%** | **Partial liquidation.** Sell **only enough to restore to 80%** | Nexo restores to below 80% from an 83.33% trigger |

🔴 **The restore point is OPEN, and the 80% above is probably wrong.** A sale shrinks the loan and the collateral together, so restoring a *ratio* costs far more gold than "only enough" implies. Worked on 100 g at ~USD 11,500 drawn at 80%, triggering at 92%:

| Restore to | Gold sold |
|---|---|
| 80% | **~60%** of remaining gold |
| 88% | ~33% |
| 90% | ~20% |

**Recommendation: 88%.** One number, already a rung on the ladder, and a liquidation returns the customer to the cure threshold rather than to square one. 90% is gentler but re-triggers on the next small move. **Awaiting Abdur's decision; every downstream document should use 88% once confirmed.**

**Never full liquidation.** Partial always, restoring to 80%, and the customer keeps the facility.

### 6.3 Who is actually exposed — the table to show the client

The ladder only binds on customers who max out at the top tier. This is the most reassuring fact in the whole design and it should be presented.

| Tier | Struck LTV | Gold fall needed to reach 92% |
|---|---|---|
| Gold | 50% | **−46%** |
| Platinum | 65% | **−29%** |
| Sovereign | 80% | **−13%** |

⚠ **A 13% gold fall is roughly a one-sigma annual move.** Sovereign borrowers at maximum draw are genuinely exposed, and the design must not pretend otherwise. Two mitigations: the population is small and the most disciplined in the book, and the ladder gives them two warnings and 14 days before anything is sold.

### 6.4 🆕 The facility review date

A term loan matures. A card balance revolves indefinitely. Without a review, a customer struck at Sovereign 80% who has since fallen to Silver keeps borrowing at 80% forever, and the tier ladder stops binding on the largest benefit in the product.

**Recommendation: an annual facility review.** The limit re-strikes to the current tier of record; **existing drawn balances run to term at the original struck LTV**, preserving the no-margin-call-on-a-tier-fall promise. The tier ladder keeps its teeth; nobody is ever repriced retroactively.

### 6.5 Procedure, taken from Manappuram

Every legal dispute found in this category — Nexo's XRP class action (~USD 5M liquidated after an unannounced eligibility change), Celsius/Tether's alleged fire sale — was about **procedure and notice, not the right to liquidate**. And nobody in the category publishes a cure period or a liquidation waterfall.

**So the thing to be explicit about is exactly what the industry hides.** Manappuram's board-approved Gold Auction Policy 2026 is a regulator-tested template: notice within 15 days of identification, 2-week cure, 7-day right of objection with sale barred while pending, 14-day sale notice, reserve price ≥90% of current value, surplus returned within 7 working days, recovery costs itemised to the rupee.

**Adopt the shape, not the detail.** We have a live vault and a float; we do not need newspaper advertisements.

### 6.6 Who sells, and the self-dealing problem

| Route | Verdict |
|---|---|
| **Aurumix's float absorbs it** | **Recommended.** Fastest, best price, no dealer call on a bad day. This is the float's **fifth job**, and the same argument that made zero-fee redemption survivable |
| Two-way dealer sells physical | Fallback for size beyond the float band |
| Lender's own machinery | Avoid: needs vault and register access, which the DIFC vehicle complicates |

⚠ **Aurumix would be valuer, collateral agent and buyer simultaneously.** Cure by mandating the **LBMA fix with zero discretion**, disclosed at the draw, with the sale price and gram count reported to the customer. Without that, this is the line a regulator or a claimant pulls on.

⚠ **Counsel question, not raised anywhere previously: is an enforcement sale a "redemption" under VARA III.E.4?** If it is, no fee may be charged on it, and the recovery costs in stream 5 become unchargeable. Our view is that a secured creditor's enforcement sale is not a customer-exercised redemption right. **It has not been tested.**

---

## 7. The collateral chain

Five links. Two are strong, three are open.

| # | Link | State |
|---|---|---|
| 1 | **A valid security interest** over the customer's beneficial interest in the gold-holding vehicle | ⚠ **Open** — see §7.1 |
| 2 | **Immobilisation** so the collateral cannot walk | ✅ **Strong** — see §7.2 |
| 3 | **Valuation and trigger** | ✅ Designed in §6.2 |
| 4 | **Cure** | ✅ Designed in §6.2 |
| 5 | **The sale** | ⚠ Designed in §6.6, self-dealing cure required |

### 7.1 🆕 DIFC over ADGM, and now for a second reason

Decision 25 chose route 2 (a passive DIFC **or** ADGM vehicle) on bankruptcy-remoteness grounds and left the choice open. **Taking security breaks the tie decisively toward DIFC.**

| | DIFC | ADGM |
|---|---|---|
| Regime | **Law of Security, DIFC Law No. 4 of 2024**, UNCITRAL-model, functional and grantor-agnostic | English-style charge registration, ADGM Companies Regulations 2020 ss.784-785 |
| Perfection | Financing statement filed with the **DIFC Registrar of Security**; **control available for digital assets** | Registration within **21 days** or the charge is **void** against a liquidator |
| Priority | Order of third-party effectiveness | First in time by creation |
| **Our fact pattern** | Works: covers intangibles generically, regardless of who the grantor is | ⚠ **May not engage at all** — the register catches charges created by *ADGM companies*. Our grantor is a retail customer in Dubai or Kerala |

**Confidence: High** on the mechanics of both; **the ADGM gap is a reasoned inference** and needs an opinion.

⚠ **Two counsel questions this research surfaced and cannot answer:**
1. **Does our token even qualify as a Digital Asset under DIFC Law No. 2 of 2024?** Section 8 requires existence *"independent of any person or legal system"*. AURX is nothing *but* a legal claim on a vaulted bar held by an SPV. On a strict reading it may fall outside the statute — in which case we perfect over the beneficial interest as a plain intangible and treat the transfer-block as operational, not as perfection. **That is the conservative design and we should assume it.**
2. **Article 88 requires the consent of both the grantor and the person in possession for repossession.** Our possessor is our own custody vehicle. **That consent must be pre-wired into the custody documentation**, and whether pre-wiring is effective is an opinion question.

### 7.2 The permissioned token earns its keep a third time

Decision 24 justified ERC-3643 on VARA's title-proof test. Decision 10 justified it on wind-down. **It now does a third job:** pledged grams cannot be transferred, so the lender's collateral is immobilised at the ledger, not merely promised in the terms. The exit path already carries the check (`Aurumix_Process_Maps_Redemption.md:91`).

**This is worth LTV points in the negotiation.** Most secured lenders cannot stop collateral moving; we can.

---

## 8. The money: interchange, corrected

Verified from the **Visa UAE Interchange Reimbursement Fee schedule effective 18 October 2025**. The cap instrument is **CBUAE Notice 1998/2024 of 17 April 2024, effective 1 October 2024**. **Confidence: High** — primary scheme document.

| Card type | In person | Online |
|---|---|---|
| Debit Classic / Gold / Rewards / Platinum | 0.75%, cap AED 37.50 | 1.00%, cap AED 50 |
| Debit Signature / Infinite / Private / UHNW | 1.00% | 1.00% |
| **Prepaid, all products** | **1.00%** | **1.00%** |
| **Credit Platinum** | **1.80%, no cap** | |
| **Credit Signature** | **2.05%, no cap** | |
| **Credit Infinite** | **2.10%, no cap** | |
| Credit Infinite Qualified / Private / UHNW | 2.20% / 2.25% / 2.30% | |

Two corrections to `Aurumix_Process_Maps_Revenue_Streams.md:197`: **prepaid never gets 0.75%** — it is 1.00% flat. And credit is **out of scope** of the notice (whose title covers *"Consumer debit and prepaid cards"*) rather than expressly exempted; no exclusion clause was found. Economically the conclusion strengthens: **credit earns 1.80–2.30% against a 1.00% prepaid ceiling.**

### 8.1 The plastic ladder is now numeric

The benefits draft asserted that upgrading a loyal saver's card *"enlarges the very pool that funds their Gold Rewards"*. It is now measurable:

| Tier | Card level | Visa product | Interchange | Gold Rewards |
|---|---|---|---|---|
| Gold | L1 | Platinum | 1.80% | 0.15% |
| Platinum | L2 | Signature | 2.05% | 0.45% |
| Sovereign | L3 | Infinite | 2.10% | 0.75% |

**The tier ladder and the revenue ladder are the same ladder.** The upgrade is revenue-positive, as claimed, and now provably so.

### 8.2 🆕 The one number to negotiate: 36%

Gold Rewards is funded from interchange and capped at what the customer generated. So the programme manager's share of interchange must exceed the rewards rate:

| Tier | Interchange | Gold Rewards | Minimum PM share required |
|---|---|---|---|
| Gold | 1.80% | 0.15% | 8.3% |
| Platinum | 2.05% | 0.45% | 22.0% |
| **Sovereign** | **2.10%** | **0.75%** | **35.7%** |

**Sovereign binds.** Aurumix must retain at least ~36% of interchange for the rewards ladder to self-fund at the top tier. At the USD 3,000 monthly qualifying-spend cap that is USD 22.50 of rewards against USD 63.00 of interchange generated.

🔴 **No UAE or MENA programme-manager interchange split is published anywhere.** Zero figures found. This single unknown sizes all of stream 2, and it can only come from a term sheet. **Take the 36% number into the NymCard and sponsor conversations as the floor.**

---

## 9. Sharia structure

Not a footnote. **AAOIFI Shari'ah Standard No. 57** contains a section headed *"Use of Gold as a Pledge/Collateral (Rahn)"*, and four clauses bear directly on this design. **Confidence: High** — read from the standard text.

| Clause | What it says | Effect on us |
|---|---|---|
| **7/1/1** | Gold may be pledged *"whether the collateral is the gold itself **or the certificate of its ownership**"* | ✅ Blesses the title-register construct outright |
| **7/1/5** | Holding ownership certificates is **constructive possession** so long as the owner cannot dispose without them | ✅ The transfer-blocked permissioned token satisfies this. **One mechanism, two independent tests** |
| **7/1/4** | The pledgee may **not** sell, lease or re-pledge the collateral, *"even if the pledgee undertook to return it"* | ✅ No rehypothecation — already our position, now doctrinally required |
| **7/1/3** | On default the creditor may **demand sale** at market value at the time of recovery, **returning the surplus** | ✅ Matches §6.2. No strict foreclosure, no windfall on appreciation |
| ⚠ **5/4/2** | Where gold secures a loan, safekeeping fees *"shall not exceed the actual cost incurred"* | 🔴 **Touches decision 5.** Under an Islamic structure, custody recovery on **pledged** grams may be capped at cost |

**Structure: tawarruq (commodity murabaha) + rahn.** Not qard-plus-fee, because 5/4/2 caps the fee at cost and there is no business in it. Precedent is the Malaysian Ar-Rahnu model (Bank Muamalat: tawarruq + rahn, up to 80% of gold value). Gold itself cannot be the murabaha subject — clause 5/1/1 requires spot settlement, which defeats deferred pricing — so the commodity leg uses something else and the gold sits purely as security.

⚠ **A revolving gold-secured Islamic card would be first-of-kind.** No such product was found in the GCC or Malaysia. That is whitespace and it is also a longer Sharia board conversation than a conventional structure.

⚠ **This becomes binding, not optional, if the sponsor is ADIB** — our named precedent is an Islamic bank.

---

## 10. Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No.** Grams are the base, tier is the rate. Two savers with identical behaviour get identical LTV percentages on different gram counts |
| Touches the exit? | **No** on fees. ⚠ **Open** on whether an enforcement sale is a redemption under III.E.4 (§6.6) |
| Payout capped at generated? | Gold Rewards yes (§8.2). Credit is not a payout |
| Partner-dependent? | **Structure ours, pricing theirs.** Ladder, seasoning, strike rules, thresholds and cure are Aurumix origination policy. Interest rate, final LTV acceptance and the licence are the partner's |
| Client money boundary | ⚠ **Undesigned.** A repayment arriving into the client account is not a token purchase. The split rule in decision 29 must be extended to cover loan repayments |

---

## 11. Corrections owed

- [ ] **`Aurumix_Process_Maps_Revenue_Streams.md:315`** — delete the *"can the facility advance tokens"* question and the *"roughly three hundred fold"* speaker-note passage. VARA's Schedule 1 definition requires the same virtual asset be returned; a fiat advance is outside it. **This is a reversal, and the speaker notes currently instruct the presenter to raise it as the first counsel question.**
- [ ] **`Aurumix_Process_Maps_Revenue_Streams.md:197`** — prepaid is 1.00% flat, not 0.75%. Credit is 1.80–2.30% by level, uncapped. Add the Visa IRF schedule as source.
- [ ] **`Aurumix_Process_Maps_Revenue_Streams.md:317`** — the LTV correction note still says thresholds need re-spacing *"to 90 to 95%"*. Superseded: 80% settled, ladder in §6.2.
- [ ] **`_draft_ics-benefits.md:158`** — the "no UAE lender publishes an LTV" row is now wrong. Emirates Money publishes 80%; Finance House publishes a product without an LTV. **This strengthens decision §6.2 and should be told to the client.**
- [ ] **`_draft_ics-benefits.md:197`** — the open question *"whether the facility advances dirhams or tokens"* is closed. Dirhams, CBUAE, partner.
- [ ] **`_draft_ics-benefits.md:254`** — "card spend is a draw" needs the facility-strike rule spelled out (§1), or a literal build re-strikes per transaction.
- [ ] **`_draft_ics-benefits.md:267` and `Aurumix_Process_Maps_ICS_Benefits.md:228`** — "interchange caps at 1% forever" is right for prepaid but the credit comparison should carry the real numbers.
- [ ] **`_draft_entities-licensing-and-payments.md:90`** — the Restricted Licence fails on an **AED 20,000 per-borrower cap**, not a collateral-lien exclusion. No lien provision found.
- [ ] **`_draft_entities-licensing-and-payments.md:91`** — mark *"CBUAE reserves the sole right to issue BINs"* as unverified; the binding constraints are scheme principal membership plus RPSCS.
- [ ] **`_draft_entities-licensing-and-payments.md:120`** — the partner list omits the **issuer processor**. Add it as a fifth role.
- [ ] **Decision 25** — add the security-law argument for DIFC over ADGM (§7.1). This is new input to a decision recorded as open.
- [ ] **Decision 5** — flag the AAOIFI 5/4/2 constraint on custody recovery for pledged grams under an Islamic structure (§9).
- [ ] **Decision 28** — Zand and CBD confirmed as VASP-serving banks; add Emirates Money, Mashreq and NymCard to the counterparty map.
- [ ] **`handoff.md` §4** — the note that thresholds *"must be re-spaced"* is now discharged by §6.2.

---

## 12. Open decisions

| # | Question | Owner |
|---|---|---|
| 1 | **The programme-manager interchange share.** Floor is 36% (§8.2). Unpublished anywhere; term-sheet only | Commercial, Abdur to raise with NymCard |
| 2 | **Does NymCard's principal membership remove the sponsor bank?** One call answers it and it may delete a counterparty | Abdur |
| 3 | **Conventional or Islamic structure?** Decides the lender shortlist and the Sharia board timeline | Client |
| 4 | Is an enforcement sale a redemption under VARA III.E.4? | Counsel |
| 5 | Does AURX qualify as a Digital Asset under DIFC Law No. 2 of 2024 s.8? | Counsel |
| 6 | Can Art. 88 repossession consent be pre-wired into the custody documents? | Counsel |
| 7 | Will Emirates Money or Mashreq take third-party originated collateral? | Commercial |

---

## 13. What this draft deliberately excludes

| Not covered | Why |
|---|---|
| Interest rates and pricing | The partner's, and Phase 4 |
| Card fee schedule (FX, ATM, issuance) | Benefits draft §3.2, sponsor-gated |
| Collections and recovery beyond the liquidation ladder | Phase 4 |
| The agent network's role in credit origination | Referral draft; unresolved whether agents may originate loans |
| Insurance attach on the loan | Out of scope at client instruction |
