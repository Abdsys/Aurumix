# Family Portfolio and Succession: The Mechanics

> **Status: decision draft. Written 2026-08-13, rewritten 2026-08-14 after the composability decision and a second research pass.**
>
> **Read §0 alone if you read nothing else. It carries the whole design.** Everything after it is the mechanism behind a line in §0.
>
> ⚠ **The 2026-08-13 version of this file was stale on arrival.** It was written before `_draft_composability-and-ownership-route.md`, which landed the same day and changed what the customer actually holds. §1 is new and it is now the load-bearing section: the product has a precondition nobody had written down. Four research findings are also new, in §15.

---

## 0. The summary that carries the document

**What the client designed.** A free perk, unlocked by loyalty tier, that transfers gold to family "automatically, on-chain, without requiring probate, family agreement, or legal proceedings."

**What we are building instead**, and every clause below is a research finding or a decision, not a preference:

1. **It only works on gold we hold.** This is new and it comes from the composability decision. Under an open ERC-20 a customer can withdraw AURX to their own wallet, and at that moment there is nothing for the instruction to act on. **The Family Portfolio and the transfer instruction are custodial-account features. They attach to the account, never to the token.** See §1. This is not a weakness to hide; it is the honest reason a balance stays on-platform, and it is exactly what every custodian does.

2. **It is a paid product open to everyone, and the tier discounts it rather than unlocking it.** Their version needed the tier to get the thing that gave you the tier. Pricing it removes the loop and funds a real recurring cost.

3. **It cannot avoid probate on death, and we must stop saying it does.** Under DIFC Trust Law Art 47(1) a beneficiary's interest is *movable property*, a transmissible asset that falls into the estate. The only architecture that genuinely avoids probate is one where the customer **never owns the gold**, which is the exact opposite of the direct-ownership Option A our whole VARA strategy rests on. **Allocated ownership and probate avoidance are mutually exclusive. We chose ownership.**

4. **And the market has not solved it either, which turns our weakest sentence into our strongest.** Coinbase does not offer beneficiary designation at all and requires probate documents before releasing anything (§15.3). **We are not conceding something competitors deliver. Nobody delivers it. We are the only one doing the work in advance.** The promise becomes *"when the court's paperwork arrives, everything else is already done"*: pre-named, pre-verified, pre-screened, pre-split, executed in days rather than months.

5. **The strongest version is the lifetime trigger, not the death trigger**, and this inverts the client's emphasis. A transfer completing while the customer is alive needs no probate and is shielded from forced heirship by DIFC Art 15. The death trigger is the one that cannot escape the court.

6. **But it inverts again for India-resident beneficiaries**, which is the sharpest fact in the design. On **death**, FEMA s.6(4) gives a resident an express uncapped permission to hold assets inherited from a person resident outside India. On a **lifetime gift**, OI Rules Sch. III para 2(3) throws the transfer out of FEMA and into **FCRA 2010**. **UAE-side law prefers the lifetime trigger; India-side law prefers the death trigger.** The matrix in §6 is the product.

7. **In-specie transfer is not a redemption; cash settlement probably is.** So we administer in-specie for a price, and a beneficiary who wants cash takes the tokens first and then redeems free like any holder. We never bundle sale-and-burn into the paid service.

8. **The fee is charged when a beneficiary is registered, never when the transfer fires.** That timing is the whole defence against recharacterisation as a disguised redemption fee, and it costs nothing to implement.

9. **The lender outranks the beneficiary on pledged gold, always.** The beneficiary inherits the net interest after the debt, with an express right to redeem it by paying. Their document does not address this at all.

10. **Two prices, and the cost floor is far lower than we assumed.** Roughly USD 2-3 one-off and USD 0.36/yr per name, because every other cost in the chain is per-will or per-entity, never per-name. The binding constraint is not cost, it is that **no adjacent product anywhere charges per beneficiary.** So bundle names into the plan and charge only above the bundle.

11. **It scores nothing.** Family activity was removed from ICS entirely (decision 46). The tier discounts the price; it does not measure the family.

12. **Do not build the client's two smart contracts.** Their §13 puts a Family Portfolio Contract and a Digital Will Contract on-chain holding sub-portfolio gold. Under the class-defined trust that contract **becomes the beneficiary itself**, so the family member owns nothing. It is the wrapper trap from the composability draft's Case C, and it would break Option A for exactly these customers. **It also releases the USD 75,000 they budgeted to audit them.** See §14.

---

## 1. The precondition: custody state

**This section is new and everything else depends on it.**

The composability decision recommends an open ERC-20: KYC at mint and at redeem, free transfer in between, no allowlist. That is the right call for the token. It has a consequence for this product that the earlier draft could not have anticipated, because the earlier draft assumed a permissioned token in which every holder was a registered name in a register Aurumix maintained.

Under the recommended design there are two custody states and the product only exists in one of them.

| | **Held in the Aurumix account** | **Self-custodied** |
|---|---|---|
| Who holds the keys | Aurumix, as custodian | The customer |
| Can we see the balance? | Yes | No |
| Can the instruction execute? | **Yes** | **No. There is nothing to act on** |
| ICS Retention | Readable | Not readable |
| On death | We freeze, wait for the grant, execute | We cannot help. Keys are the estate's problem, and lost keys are lost gold |
| What the customer has | A serviced account | A bearer asset, exactly like PAXG or XAUT |

**The rule, decided 2026-08-14 (Abdur): a withdrawal to self-custody counts as a sale.** It reduces ICS Retention exactly as a sale does, and those grams leave the Family Portfolio so the instruction can no longer reach them. One rule, two problems closed.

**Why this rule and not the alternatives.** Registering self-custody addresses would fix ICS but **would not fix succession**, because we still hold no keys and still cannot execute. That asymmetry would have to be explained to a customer, and "your gold still counts for your score but your family cannot receive it" is not a sentence anyone should have to say. Displaying the grams in the Family Portfolio while being unable to deliver them is worse still: a dashboard that shows a family member a number we cannot honour is the worst kind of promise. **The 30% annual withdrawal allowance means a customer can move a meaningful slice into self-custody for no cost at all**, which is the pressure valve that makes the strict rule fair.

⚠ **This also closes `_draft_composability-and-ownership-route.md` §7.1**, which recorded the same question as an open ICS item. It was never only an ICS item. Mark it decided there.

**What the customer is told, in one sentence:** *your gold is yours to take out whenever you want, and the family features work on the gold you keep with us.*

### 1.1 What this changes about the estate

Under the class-defined trust the beneficiary's interest arises on holding tokens and terminates on ceasing to hold them (DIFC Arts 45(2) and 48(4)(a)). So the asset in the estate is **the tokens, or more precisely control of the account holding them**, rather than a separately assignable trust interest.

Probate is still required, because a virtual asset is still property that transmits. But two things get simpler:

- **Execution is one act, not two.** The old named-register design moved the token and then wrote the title register, two writes that could diverge and that VARA Annex 2 III.B.1.c exists to police. Under the class-defined trust, moving tokens between two verified accounts **is** the transfer of beneficial ownership. No register write, no separate assignment.
- **The in-specie argument gets stronger.** A transfer that is nothing but a token movement between two identified accounts is the most transfer-like thing available and the least redemption-like. See §7.

---

## 2. The correction that reshapes the promise

**The premise we held.** A DIFC/ADGM holding vehicle plus a named-beneficiary designation would let gold pass outside probate, like a life-insurance nomination.

**What the statutes actually say.**

| Provision | Text | Consequence |
|---|---|---|
| DIFC Trust Law **Art 47(1)** | "The interest of a beneficiary shall constitute movable property" | The customer's interest is a proprietary asset. It falls into the estate. **Probate is required** |
| ADGM Foundations **s.29(1)** | Assets vested in a Foundation "are no longer the property of the Founder... and **are not the Assets of any Beneficiary until such time as the Assets are distributed**" | Probate *is* avoided, because the customer owns nothing to transmit |
| DIFC Foundations **Art 11(3)** | A Qualified Recipient "has no right to or interest in the property of the Foundation other than a right to payment" | Same |

**The fork.** The foundation route avoids probate precisely by destroying the thing we are selling. Option A, where the customer legally owns specific allocated grams, is what removes the VARA Reserve Asset regime, removes up to roughly USD 4M of locked capital, and is the entire Individual Gold Receipt proposition. **We keep ownership and accept probate.**

**There is also no UAE transfer-on-death analogue to fall back on.** Direct payment on death works for life insurance and DEWS pensions because a statute or scheme rule creates the entitlement. No such regime exists for a tokenised commodity. We cannot bolt a nomination onto an owned asset and get transfer-on-death effect.

**In one line:** the instruction is a **probate accelerator, not a probate substitute**, and every piece of client-facing copy must be re-cut to say so.

> ⚠ **Their §5.4 sentence, "without requiring probate, family agreement, or legal proceedings", is not deliverable and must be corrected before it reaches an investor.** It is also the sentence most likely to attract a regulator, because it is the sentence that makes this sound like a will.

---

## 3. The two objects, kept separate on purpose

The client's document runs them together. They have different legal characters, different cost drivers and different risk.

| | **Family Portfolio** | **Beneficiary Transfer Instruction (BTI)** |
|---|---|---|
| What it is | A live sub-account structure during the holder's life | A standing, pre-authorised instruction on the account |
| Legal character | Account administration | Client instruction under **Custody Rulebook IV.B.2** |
| When it acts | Continuously | Once, at a defined trigger |
| Cost driver | Names under monitoring | Verification at registration, execution at trigger |
| Priced by | The annual plan fee | The per-beneficiary registration fee |

> **Naming.** *"Digital Will"* is the client's emotional centrepiece and it is also the phrase most likely to imply a regulated will-writing service. **The contractual term is Beneficiary Transfer Instruction.** Whether "Digital Will" survives as a marketing name is a counsel question (§16), and we should plan on it not surviving. `Legacy Instruction` is the fallback that keeps the feeling without the legal claim.

---

## 4. Family Portfolio: how it works during life

The primary account holds the master Gold Receipt. It splits into named sub-accounts. **1 AURX = 1 gram** throughout, so every display is a gram count.

| Rule | Content |
|---|---|
| Allocation | Named sub-accounts, each a declared percentage. Total cannot exceed 100% of the master receipt |
| Who controls | The primary holder, entirely. Add, change or remove at any time |
| What the family member sees | Their own grams and value. **Read-only.** They see *that* a BTI exists, never its terms |
| Ownership during life | **Unchanged. It is all still the primary holder's gold.** A sub-account is a declaration of intent and a display, not a transfer |
| Where it lives | **Off-chain, in the platform ledger.** Not a smart contract, and not a separate on-chain balance. See §14 |
| Credit | A sub-account's grams count toward the **primary holder's** facility. The family member has no independent facility until transfer completes |
| ICS | Scores nothing, for anyone (decision 46) |
| KYC | Every named person verified at registration and screened continuously until the trigger fires or the name is removed |
| Self-custody | Grams withdrawn to a personal wallet leave the Family Portfolio (§1) |

> ⚠ **Correction to the client's model.** Their §5.2 gives each sub-portfolio "its own credit facility limit" and "its own ICS sub-score" during the primary's life. Neither survives. You cannot lend to someone against gold they do not yet own, and ICS is one number about one person's behaviour. **The family member's benefits begin at transfer, not at designation.**

---

## 5. The instruction: what the customer actually defines

Per sub-account, four fields. The client's five collapse to four because "modification rights" is a property of the transferred account, not of the instruction.

| # | Field | Options |
|---|---|---|
| 1 | **Beneficiary** | A named person who has completed verification. Registration is what is priced |
| 2 | **Trigger** | Date · Condition · Death. See §6, they are **not** interchangeable |
| 3 | **Form** | Full · Phased in tranches by age or date · **(income-only is deleted, see below)** |
| 4 | **Continuation** | Whether SIP contributions to that sub-account continue, redirect, or stop after transfer |

> **"Income-only transfer" is deleted.** Their §5.4(3)(c) transfers "only the ICS Dividend... gold principal transfers later." There is no dividend; it became **Gold Rewards**, a fee rebate in grams capped at what that account itself generated (decision 6). A sub-account with no card spend generates nothing, so income-only would transfer zero. Offering it would be selling an empty box.

**Revocability.** Freely modifiable while the holder is active. **Will Lock-In is retained but re-scoped:** it locks the *allocation percentages*, not the instruction's existence, and it cannot bind against a later grant of probate or a forced-heirship claim. Sold as a commitment to family, never as legal irrevocability.

### 5.1 Conditions between unrelated parties are not supported

Their **Scenario 3** has two business partners cross-designating 20% of each other's holdings, transferring if one stops contributing for six consecutive months. **We do not support it**, for three independent reasons:

1. **It is not succession.** A transfer between unrelated adults contingent on a payment event is a wager on behaviour, and it needs a different licence conversation than the one we are having.
2. **It collides with the regulatory pause.** Decision 36 freezes the clock for a customer whose money *we* refuse. Under Scenario 3 an Aurumix compliance block would trigger a transfer of that customer's gold to somebody else. We would be the cause and the executor of their loss.
3. **It puts us in the middle of a commercial dispute** with no adjudication licence and no way to verify the underlying arrangement.

**Conditions are supported where the condition is about the beneficiary's own life** (an age, a marriage, a graduation) and the parties are family. **Not where the condition is another person's account behaviour.**

---

## 6. The trigger ladder, and why beneficiary residence inverts it

**This is the centre of the design.** The three triggers are not three flavours of one thing. They are three different legal events.

| Trigger | What it legally is | Probate? | Forced heirship? |
|---|---|---|---|
| **Date** (a birthday, an anniversary) | A completed **lifetime gift** | **No. Holder is alive** | **Shielded.** DIFC Art 15 / ADGM s.29(3) protect completed lifetime transfers |
| **Condition** (a defined, observable event) | Same, if it fires during life | **No** | Shielded, same basis |
| **Death** | **Testamentary succession** | **Yes. Grant required** | **Exposed.** The firewall covers *living persons* only; DIFC Art 105 excludes rights "created by will" |

**So the lifetime trigger is the strong product and we should lead with it**, the education fund and the wedding gift rather than the death benefit. It completes cleanly, needs no court, and is the version their own Scenario 2 already describes.

**Now the inversion.** Overlay the beneficiary's residence:

| Beneficiary resident in | **Date / Condition trigger** | **Death trigger** |
|---|---|---|
| **UAE / GCC / rest of world** | ✅ **Preferred.** Clean completed transfer, no probate, heirship-shielded | ⚠ Permitted. Requires grant of probate before execution |
| **India** | ⛔ **Blocked at launch.** OI Rules Sch. III para 2(3) routes a gift from a person resident *outside* India through **FCRA 2010**. Whether it bites turns on the donor's **passport, not residence**: an Indian-passport NRI is generally not a "foreign source", a foreign-passport OCI is. Too fine a distinction to enforce in an app at launch | ✅ **Permitted, settled to cash.** FEMA **s.6(4)** permits a resident to hold assets "inherited from a person who was resident outside India"; OI Rules Sch. III para 2(1) says **"without any limit."** The LRS bar does not reach it, because LRS bites on acquisition by remittance and no remittance occurs |

**Why India-resident beneficiaries receive cash, not tokens.** FEMA s.6(4) is a **closed list of three categories**: foreign currency, foreign security, immovable property. An allocated-gold token is arguably **none of them**, so the inheritance permission may not reach AURX at all. That is a gap rather than a prohibition, but it is not a gap to test with a customer's inheritance. **Settling to cash sidesteps the classification question entirely: the beneficiary receives money through banking channels, and no resident ever holds the token.**

> ⚠ **The India path is free by construction and must be modelled that way.** Cash settlement is probably a redemption (§7), and Annex 2 III.E.4 forbids any fee on redemption. We cannot charge for the India leg even though it is the most operationally expensive one.

**Re-verified 2026-08-14.** No Finance Act, CBDT circular or RBI notification in 2025 or 2026 has changed the s.6(4) categories or extended them to foreign virtual digital assets. The classification gap is unmoved. Separately, s.2(47A)'s definition of a virtual digital asset is broad enough that an Indian assessing officer would likely analyse AURX as a VDA first, which puts a later sale at the flat **30% under s.115BBH with no loss offset**. That is the beneficiary's tax position, not ours, and it is a disclosure item.

**Beneficiary obligations we disclose and never advise on:** inheritance is not taxable on receipt (s.56(2)(x)), cost of acquisition carries over with no step-up (s.49(1)), and Schedule FA reporting plus Black Money Act 2015 exposure apply annually to a resident holder. **We state that obligations exist and refer them to their own adviser.** We never compute an Indian tax position.

---

## 7. Execution: the authority gate

The client's §5.6 executes on a trigger. Ours executes on a trigger **plus proven authority**, and the second half is what was missing.

| Step | Lifetime trigger | Death trigger |
|---|---|---|
| 1. Trigger detected | Date reached, or condition evidenced | Death notified by executor or family |
| 2. **Account freeze** | Not applicable | **Immediate on credible notice.** Withdrawals and new draws stop |
| 3. **Authority** | None needed. The holder is alive and instructed it | ⛔ **Grant of probate or court order. Hard gate.** We do not adjudicate, we wait |
| 4. Beneficiary status | Re-verify identity, re-screen sanctions and PEP, confirm residence has not changed | Same |
| 5. Encumbrance check | Pledged grams resolved per §8 | Same |
| 6. Execution | **In specie.** Tokens move from the holder's account to the beneficiary's verified account | Same, or **cash settlement** where the beneficiary is India-resident |
| 7. After | Beneficiary's own ICS clock starts at zero. Continuation instruction governs the SIP | Same |

**Why in-specie is the default and the only thing we price.** Redemption under Annex 2 III.E is **request-driven, value-delivering and claim-directed**. A beneficiary who receives tokens and keeps them exercises nothing and receives no value from Aurumix. Rule III.B.1.a positively supports this: it requires that ownership "is transferred in the event of a transfer of ownership of the ARVA", treating transfer as a distinct category from redemption. **Cash settlement has every hallmark of a redemption**, so if the beneficiary wants money they onboard, take the tokens, and redeem free of charge like any other holder. We never bundle sale-and-burn into a paid service.

⚠ **Watch III.E.3's "or their designee".** VARA already contemplates a third party making a redemption request, and a beneficiary is naturally a designee. That does not make in-specie a redemption, but it does put a *redeeming* beneficiary squarely inside the fee ban.

**Step 6 is now a single token movement** (§1.1), which is the cheapest possible implementation and the strongest possible answer to III.B.1.c: the beneficial interest cannot diverge from the ledger, because the ledger defines the class.

---

## 8. Pledged gold: the ordering their document never states

The holder pledged grams for credit, then the trigger fires.

**The lender wins. Always.** The security attaches to the collateral and survives the holder's death; the beneficiary can only ever take the net residue. Ordering: **secured creditor → estate expenses and other creditors → beneficiary.**

Five clauses the contract must carry, none of which exist today:

1. **The BTI is subordinated to any security interest.** Stated in the instruction itself, visible in the app.
2. **The transfer is of the net interest** after discharge, not the gross sub-account.
3. **Lender consent or release is a condition** to executing over pledged grams.
4. **The beneficiary has an express right to redeem** by paying the outstanding debt and taking the grams whole.
5. **A standstill period** before any enforcement, plus defined apportionment where only part of the sub-account is pledged.

**Death is not an automatic event of default** in consumer secured lending, and we should not let the partner make it one. Market practice, including Indian gold-loan practice as the closest precedent, is procedural: notify, identify successors, preserve collateral, allow settlement.

> This closes the tension flagged earlier: a beneficiary could otherwise watch an inheritance liquidated by a margin call. **They cannot lose more than the debt, and they always have the right to pay it and keep the gold.**

---

## 9. Minor beneficiaries

No new structure is needed; the mechanism already exists.

| Question | Answer |
|---|---|
| Who receives | The grams are held in the sub-account. Payment or receipt by a parent or lawful guardian **discharges our obligation** (DIFC Trust Law Art 69(4)) |
| Until when | Age of majority. ⚠ **This just moved: 18 Gregorian, from 1 June 2026 in the UAE and 2 March 2026 in DIFC** (was 21). Still unconfirmed against the enacting law; sources conflict on the number. Confirm before hard-coding |
| Phased release by age | Drafting, not architecture. Art 69(3) already permits accumulation and advancement |
| Guardianship | We rely on a guardian appointed elsewhere. **We never appoint one.** Guardianship of a minor's property is a court matter |

---

## 10. The two populations, and we currently design for one

🆕 **New 2026-08-14, and it is a real gap.**

The DIFC Wills Service Centre, which is both our nearest comparable and a possible partner, is **open to non-Muslims only**. A Muslim expatriate resident in the UAE remains under Sharia for movable assets, and a DIFC or ADGM registered will cannot depart from the fixed shares. UAE Federal Decree-Law 41 of 2022 on Civil Personal Status supplies a civil regime for **non-Muslims** and applies federally, letting a non-Muslim rely on a valid will instead of default succession.

**Our persona is both populations.** The NRI and GCC saver includes Hindu, Christian and Muslim customers, and a product that quietly assumes the first two is a product that mis-sells to the third.

| | **Non-Muslim customer** | **Muslim customer** |
|---|---|---|
| Governing default | Federal Decree-Law 41/2022, or home-country law | Sharia fixed shares |
| DIFC will route | ✅ Available | ⛔ Not available |
| Can the BTI depart from fixed shares? | Yes, subject to the usual limits | **No, and we must never imply it can** |
| The defensible version | Any trigger | **Lifetime trigger as a completed gift (*hiba*)**, which is the recognised route |
| The exposed version | Death trigger, as everywhere | A transfer where the customer **retains control and can redeem on demand**, which is what our product looks like |

**Design consequences, all cheap:**

- **Ask the question at onboarding**, alongside the domicile declaration in §16.4. It changes which triggers we present.
- **Lead Muslim customers to the lifetime trigger**, which is both the stronger legal position and the better product anyway (§6).
- **Never market this as overriding Sharia shares**, in any jurisdiction, to anyone. It is the single fastest route to a regulatory and reputational problem.
- **A death-trigger BTI for a Muslim customer is a distribution instruction that must be consistent with the shares**, not a substitute for them. The value we add is speed and pre-verification, which is exactly the §0.4 promise and needs no departure from the shares at all.

---

## 11. Pricing

**The cost floor, and it is much lower than we assumed.** Every per-name cost with a published price:

| Line | One-off | Annual |
|---|---|---|
| Identity verification | USD 1.25-1.85 | — |
| AML / PEP / sanctions at onboarding | USD 0.35-1.05 | — |
| Continuous screening per name | — | **USD 0.36** |
| **Floor** | **~USD 1.80-2.90** | **~USD 0.36** |

**Everything else in the chain is per-will or per-entity, never per-name**: DIFC Full Will AED 10,000, **DIFC Digital Assets Will AED 5,000 single and AED 7,500 for two registered together**, DIFC probate USD 1,500 flat, ADGM Foundation roughly USD 1,000 setup and USD 500 renewal. None of it scales with beneficiary count, so none of it belongs in a per-name fee.

**Two costs that actually bind, and neither is the per-check rate:**

- **The monitoring tail.** A beneficiary stays screened until the trigger fires, potentially 20 to 40 years. At USD 0.03/month that is **USD 7-14 per name undiscounted**, and no provider publishes multi-decade terms. *This*, not the USD 2 check, is what the per-name fee is really buying.
- **The platform minimum.** USD 99-299/month. **Below roughly 2,000 names a year the monthly minimum dominates unit economics entirely**, so at launch the marginal name is nearly free and the fixed cost is what hurts.

**Two corrections to `_draft_ics-benefits.md` §5.2.** Our "no published comparable exists anywhere" claim is **wrong**: Casa publishes crypto inheritance at roughly USD 250/yr with heirs included. And **per-beneficiary pricing has essentially no precedent in any adjacent market**. Casa, Trust & Will, Farewill, Everplans, DIFC, banks and brokerages all price flat per will, plan or entity, and beneficiary designation at a bank is conventionally free.

**So the structure, given a saver contributing USD 240-900 a year:**

| | Recommendation | Why |
|---|---|---|
| **Annual family plan** | **USD 29-36/yr**, including **up to 4 registered beneficiaries** | Brackets Farewill and Trust & Will. At USD 48 a USD 20/month saver pays 20% of a year's contributions, which is too much. The plan fee funds the monitoring tail |
| **Per additional beneficiary** | **USD 20 one-off**, capped per household at roughly USD 60 | Anchors trivially against an AED 5,000 DIFC Digital Assets Will. The cap prevents the product punishing people for having a family, which is fatal in something called a *Family* Portfolio |
| **Charged when** | **At registration. Never at the transfer event** | The defence against recharacterisation as a redemption fee |

**Against the discount ladder already fixed in `_draft_ics-scoring.md` §6.5**, plan fee 0/10/20/35/50% and per-name 0/0/0/20/20%, a Sovereign pays roughly USD 15-18/yr and USD 16/name. Against a USD 2.90 floor that is **5x headroom on the deepest discount.** The design rule holds comfortably across the whole range, which it would not have at the floor we assumed.

**No VARA rule caps ancillary fees or requires them to be cost-reflective.** The only hard obligation is disclosure: **Market Conduct II.B.1.e** requires "all fees charged by the VASP for the services" in the Client Agreement. Both prices go in.

---

## 12. What the score does and does not do

| | |
|---|---|
| Does the family earn ICS? | **No.** Removed entirely (decision 46). Registering names is not saving behaviour |
| What the tier does | Discounts the two prices. **A price, never a gate** |
| Is the feature tier-gated? | **No. Open to everyone who pays.** This is what broke the client's circularity |
| Can the discount reach 100%? | **No.** Free at the top rebuilds the tier-gate in mirror image and un-funds the cost exactly where it is highest |
| Does a family transfer move ICS? | **No.** The beneficiary's own clock starts at zero, and they pass their own gate like everyone else (decision 46 amendment) |

---

## 13. The perimeter: what Aurumix never does

The sharpest risk here is not fees, it is **licensing**. No VARA licence covers trust, fiduciary, estate administration or will-writing, and estate administration in the UAE is court-supervised.

| We do | We never do |
|---|---|
| Execute a documented standing instruction on an account | Determine who is entitled to an estate |
| Require a grant of probate before a death transfer | Validate a death or adjudicate competing claims |
| Register and monitor named beneficiaries | Draft, witness or register a will |
| Tell customers to maintain a valid will in their own jurisdiction | Advise on estate planning, tax or succession |
| Refer to a licensed will-writer | Pay or accept a referral commission for it |

**The structuring hook is Custody Rulebook IV.B.2**, which permits a VASP to "obtain and rely on any pre-authorised instruction from a client" where it has considered "all reasonably foreseeable circumstances" and communicated them in advance. **That sentence is the legal home of this entire product**, and it is why the BTI is drafted as a standing instruction rather than a testamentary instrument.

**Two further characterisation traps:** marketing it as *planning* edges toward advising; presenting it as a benefit paid on death edges toward insurance. Both need permissions we do not hold.

---

## 14. Build: do not put this on-chain

🔴 **The client's §13 architecture must not be built as drawn.** Their Layer 2 lists a **Family Portfolio Contract** ("manages sub-portfolio allocations, family member access rights, and gold gram attribution") and a **Digital Will Contract** ("stores Will instructions and executes automatic transfers at defined triggers"), with a **USD 75,000** expanded audit budget attached to them.

**Under the class-defined trust, a smart contract holding sub-portfolio tokens becomes the member of the beneficiary class.** The gold would belong to the contract, and the family member named in it would own nothing at all. That is precisely the Case C wrapper trap in `_draft_composability-and-ownership-route.md` §5, and it is the Kinesis case already recorded in our ownership explainer. **It would destroy Option A for exactly the customers who bought the family product.**

| | Client's design | What we build |
|---|---|---|
| Sub-portfolio allocations | On-chain contract | **Off-chain platform ledger.** A percentage against an account |
| Will instructions | On-chain contract | **Off-chain, in the Client Agreement and the account record** |
| Execution | Contract fires automatically | **A token transfer between two verified accounts**, made by the custodian after the authority gate |
| Who holds the gold before transfer | The contract | **The primary holder, through the trust** |
| Audit cost | USD 75,000 budgeted | **Not required. Neither contract exists** |

**The commercial point is worth making on the call:** removing these two contracts removes an audit line, removes two failure modes, removes an upgrade problem on a 40-year instruction, and protects the ownership claim. **It is cheaper and safer at the same time**, which is rare enough to be worth saying plainly.

⚠ **One thing does stay on-chain and it is enough:** the token movement at execution. Everything else is account administration, and account administration is what a custodian is licensed to do.

---

## 15. What the 2026-08-14 research pass changed

**Four findings are new.**

### 15.1 DIFC Courts already sell this, and they run a wallet

The **DIFC Courts Digital Assets Will** costs **AED 5,000** for a single will and **AED 7,500** for two registered together, and it operates a **non-custodial wallet built on Hedera** which currently supports Bitcoin, Ethereum, Matic, USDC, USDT, HBAR and Hedera Token Service, with NFT support planned. Registration is by video conference with two witnesses joining from anywhere.

**Three consequences.** It is our **nearest published comparable** and it anchors our pricing beautifully: USD 29-36/yr against AED 5,000 one-off. It is a **possible partner route** for the customer's underlying legal will, which we should refer to and never charge for. And it is a **court-operated competitor** with a technical mechanism, which means the client cannot be told this space is empty. ⚠ **AURX would not be on that supported-asset list**, so the DIFC wallet is not currently a delivery route for our product. Worth asking whether ERC-20 support is planned.

### 15.2 The DIFC will route is non-Muslims only

Covered in §10. It is the largest single gap between what the draft assumed and what the persona actually is.

### 15.3 The market leader requires probate and offers no beneficiary designation

Coinbase's own help centre states it does not support naming a beneficiary on an individual account, and requires a death certificate plus **"Probate, Letters Testamentary, Letters of Administration, Affidavit for Collection, or Small Estate Affidavit"**, government ID for the person named in those documents, and signed transfer instructions, before it will release anything.

**This is the most useful thing the research pass produced**, because it converts §0.3 from an apology into a competitive statement. We are not withdrawing a feature others deliver. **The largest regulated custodian in the world requires probate too, and does not even let you name anyone in advance.** We do the pre-work; nobody else does.

### 15.4 CARF is coming and it touches this

VARA consulted on the UAE's implementation of the **Crypto-Asset Reporting Framework** in October 2025, and issued Travel Rule implementation requirements in February 2026 and qualified-investor onboarding guidance in January 2026. **A cross-border transfer to a beneficiary in a reportable jurisdiction is exactly the shape CARF is designed to capture.** Not a blocker and not a design change, but it belongs in the build's reporting scope and in the Phase 4 cost line.

**Two things were re-verified and stand unchanged.** VARA remains **entirely silent on client death, incapacity and dormancy** across everything published through August 2026, so the Client Agreement is still the governing instrument and still the freedom and the risk. And the **India position is unmoved**: no 2025 or 2026 change reaches the s.6(4) categories.

---

## 16. Corrections owed to other files

**Three are citation errors that would be noticed in a filing.**

| File | Correction |
|---|---|
| `handoff.md` §5, decisions 23/32, `_draft_ics-benefits.md` §0.2, `_draft_purchase-structure.md`, `Aurumix_Process_Maps_Redemption_Fee.md` | 🔴 **The no-fee-on-redemption rule is Annex 2 (ARVA Rules) Part III.E, not "Issuance Rulebook III.E".** Part III of the main rulebook is *Whitepapers and Public Disclosures*. Cite as "Annex 2 III.E" |
| Same set | 🔴 **The Issuance Rulebook is dated 19 May 2025, not 19 June 2025.** Now verified twice, including from the rulebook filename |
| `handoff.md` decisions 24, 25, counsel batch 4 q1 | 🔴 **DIFC Trust Law Art 60(6) does not support the permissioned-token decision.** Art 60 is headed *"Duties of trustees"*; 60(6) is an AML/beneficial-ownership duty aimed at **corporate parties to the trust**, enforced by the Registrar. **Counsel batch 4 question 1 is built on this misreading**, and the composability draft §10 already supplies its replacement |
| `handoff.md` decision 25 | 🔴 **ADGM bankruptcy remoteness is s.30, not Art 33.** Art 33 is "Restrictions on transfer to and by a Foundation". Forced-heirship firewall is s.29(2)-(5); no-rights-in-specie is s.31 |
| `_draft_composability-and-ownership-route.md` §7.1 | 🆕 **Mark decided.** The self-custody question is closed by §1 above: a withdrawal counts as a sale, for ICS and for the Family Portfolio together |
| `_draft_ics-scoring.md` §1.5, §10 | 🆕 Add the self-custody withdrawal to the Retention definition as a counted disposal, alongside the margin-call liquidation ruling |
| `_draft_ics-benefits.md` §5.2 | "No published comparable exists" is **wrong**: Casa at roughly USD 250/yr, and the **DIFC Digital Assets Will at AED 5,000**, a direct comparable and a possible partner route |
| `_draft_ics-benefits.md` §5.5, §5.6 | The pledged-gold and estate-settlement rows are answered here (§8, §7), not open |
| `_draft_sip-rulebook.md` §9.5 | "Family portfolios → open to everyone **and scoring**" is superseded. Open to everyone, **scoring nothing** (decision 46) |
| Client's `100 G Business_Model.md` | §5.2 sub-account credit facility and ICS sub-score; §5.4 income-only transfer and "without requiring probate"; §5.6 executor-confirmed death trigger; §5.7 Scenario 3; §4.6 dividend accruing to beneficiaries; §13 the two smart contracts and the USD 75k audit line |

---

## 17. What remains open

**For counsel. Three, and the first is worth more than the other two combined.**

1. 🔴 **Confirm the in-specie / redemption split with VARA in pre-application dialogue, in writing.** The rulebook never defines "Redemption", our position is inference from structure, and the entire pricing model rests on it. A written confirmation is far cheaper than a post-launch recharacterisation.
2. 🔴 **The licensing perimeter opinion** across VARA, DFSA, FSRA, SCA and MoJ, including whether the phrase *"Digital Will"* itself implies a regulated will-writing service, and whether the Custody IV.B.2 standing-instruction framing holds.
3. 🔴 **The Muslim-customer position, and do not pre-judge it.** DIFC CA 002/2020 held Sharia inheritance rules are not DIFC public policy, but the Court **declined jurisdiction** over the onshore anti-circumvention rule. A completed lifetime *hiba* is defensible; a transfer where the customer **retains control and can redeem on demand**, which is exactly our product, is exposed. Now sharpened by §10: the DIFC will route is unavailable to these customers entirely.

**Second batch, cheaper:**

4. **India-domiciled customers.** Succession to movables follows the **deceased's domicile at death** (Indian Succession Act s.5(2)), and Gulf-resident NRIs on renewable visas very often retain Indian domicile of origin. An Indian court could apply the Hindu Succession Act, or Muslim personal law with its **one-third bequest cap**, to our nomination. **Recommend a domicile declaration at onboarding** plus explicit disclosure, asked in the same breath as §10's question.
5. **Whether the classification gap in FEMA s.6(4) matters** once we settle India-resident beneficiaries to cash. We think it disappears; confirm.
6. **Confirm the age-of-majority enacting law and commencement** before hard-coding age logic. Sources still conflict on the law number.

**Commercial, not legal:**

7. **The KYC contract rate and the monthly platform minimum** at our projected name volume. This sets the real floor, and rack rates are not it.
8. **Multi-decade monitoring terms.** What happens if the vendor raises rates or exits over a 40-year instruction. The biggest unpriced tail in the model.
9. **Base prices, client sign-off**, against the ranges in §11.
10. 🆕 **Ask DIFC Courts whether the Digital Assets Will wallet will support arbitrary ERC-20 tokens**, and on what timeline. If yes, it is a distribution channel rather than a competitor.

**For us:**

11. 🆕 **Fold the self-custody rule into the ICS scoring draft and the composability draft**, per §16.
12. ✅ **Process maps: DONE 2026-08-14.** `Aurumix_Process_Maps_Family_And_Succession.md`, **8 diagrams**. Ten-minute call set is **0, 4 and 5**; thirty adds 1, 2 and 3. **Map 4 (the trigger and residence matrix) is the leave-behind**, and **map 5 must not be cut**, because it is where their §5.4 probate promise is withdrawn. **Map 7 belongs in the September build conversation, not the family call.** The set carries the twelve departures from their document as a table rather than a ninth diagram.

---

*Verified primary text in this directory: `_source_difc_trust_law_2018.txt` (DIFC Trust Law 2018), `_source_vara_issuance_rulebook_2025.txt` (VARA Issuance Rulebook, 19 May 2025).*
