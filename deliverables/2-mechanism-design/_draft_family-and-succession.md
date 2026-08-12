# Family Portfolio and Succession: The Mechanics

> **Status: decision draft, 2026-08-13.** Defines the Family Portfolio and the succession instruction end to end, after a four-stream research pass closed the open items carried in `_draft_ics-benefits.md` §5 and `handoff.md` §7.
>
> **Read §0 alone if you read nothing else. It carries the whole design.** Everything after it is the mechanism behind a line in §0.
>
> ⚠ **This draft corrects three premises the project has been building on.** Two are citation errors, one is structural and changes what we can promise. See §1 and §13.

---

## 0. The summary that carries the document

**What the client designed.** A free perk, unlocked by loyalty tier, that transfers gold to family "automatically, on-chain, without requiring probate, family agreement, or legal proceedings."

**What we are building instead**, and every clause below is a research finding, not a preference:

1. **It is a paid product open to everyone, and the tier discounts it rather than unlocking it.** Their version needed the tier to get the thing that gave you the tier. Pricing it removes the loop and funds a real recurring cost.

2. **It cannot avoid probate on death, and we must stop saying it does.** This is the structural correction. Under DIFC Trust Law Art 47(1) a beneficiary's interest is *movable property* — a transmissible asset that falls into the estate. The only architecture that genuinely avoids probate is one where the customer **never owns the gold**, which is the exact opposite of the direct-ownership Option A that our whole VARA strategy rests on. **Allocated ownership and probate avoidance are mutually exclusive. We chose ownership.**

3. **So the product's real promise changes, and it is still worth paying for.** Not *"we skip the court"* but *"when the court's paperwork arrives, everything else is already done."* The beneficiary is pre-named, pre-verified and pre-screened; the split is pre-declared so there is nothing to argue about; the family has watched the grams grow for years; and the transfer executes in days rather than months. **Nobody else in the category offers any of it** — nineteen protocols surveyed, zero with a family structure or a succession mechanism.

4. **The strongest version of the product is the lifetime trigger, not the death trigger** — and this inverts the client's emphasis. A transfer that completes while the customer is alive needs no probate at all, and DIFC Art 15 / ADGM s.29(3) shield completed lifetime transfers from forced heirship. The death trigger is the one that cannot escape the court.

5. **But that inverts again for India-resident beneficiaries**, which is the single sharpest fact in the design. On **death**, FEMA s.6(4) gives a resident an express, uncapped permission to hold assets inherited from a person resident outside India, and the LRS bar does not reach it because no remittance occurs. On a **lifetime gift**, OI Rules Sch. III para 2(3) throws the transfer out of FEMA and into **FCRA 2010**. So: **UAE-side law prefers the lifetime trigger; India-side law prefers the death trigger.** The eligibility matrix in §5 is the product.

6. **In-specie transfer is not a redemption; cash settlement probably is.** So we administer in-specie for a price, and if the beneficiary wants cash they take the tokens first and then redeem free like any holder. We never bundle sale-and-burn into the paid service.

7. **The fee is charged when a beneficiary is registered, never when the transfer fires.** That timing is the whole defence against a supervisor recharacterising it as a disguised redemption fee, and it costs nothing to implement.

8. **The lender outranks the beneficiary on pledged gold, always.** The beneficiary inherits the net interest after the debt, with an express right to redeem it by paying. Their document does not address this at all.

9. **Two prices, and the cost floor is far lower than we assumed.** ~USD 2-3 one-off and ~USD 0.36/yr per name — because every other cost in the chain (will registration, foundation, probate) is per-will or per-entity, never per-name. The binding constraint is not cost, it is that **no adjacent product anywhere charges per beneficiary.** So: bundle names into the plan, charge only above the bundle.

10. **It scores nothing.** Family activity was removed from ICS entirely (decision 46). The tier discounts the price; it does not measure the family.

---

## 1. The correction that reshapes the promise

**The premise we held.** A DIFC/ADGM holding vehicle plus a named-beneficiary designation would let gold pass outside probate, like a life-insurance nomination.

**What the statutes actually say.**

| Provision | Text | Consequence |
|---|---|---|
| DIFC Trust Law **Art 47(1)** | "The interest of a beneficiary shall constitute movable property" | The customer's interest is a proprietary asset. It falls into the estate. **Probate is required.** |
| ADGM Foundations **s.29(1)** | Assets vested in a Foundation "are no longer the property of the Founder… and **are not the Assets of any Beneficiary until such time as the Assets are distributed**" | Probate *is* avoided — because the customer owns nothing to transmit |
| DIFC Foundations **Art 11(3)** | A Qualified Recipient "has no right to or interest in the property of the Foundation other than a right to payment" | Same |

**The fork.** The foundation route avoids probate precisely by destroying the thing we are selling. Option A — the customer legally owns specific allocated grams — is what removes the VARA Reserve Asset regime, removes up to ~USD 4M of locked capital, and is the entire "Individual Gold Receipt" proposition. **We keep ownership and accept probate.**

**There is also no UAE transfer-on-death analogue to fall back on.** Direct payment on death works for life insurance and DEWS pensions because a statute or scheme rule creates the entitlement. No such regime exists for a tokenised commodity. We cannot bolt a nomination onto an owned asset and get TOD effect.

**What this changes in one line:** the succession instruction is a **probate accelerator, not a probate substitute**, and every piece of client-facing copy must be re-cut to say so.

> ⚠ **Their §5.4 sentence — "without requiring probate, family agreement, or legal proceedings" — is not deliverable and must be corrected before it reaches an investor.** It is also the sentence most likely to attract a regulator, because it is the sentence that makes this sound like a will.

---

## 2. The two objects, kept separate on purpose

The client's document runs them together. They have different legal characters, different cost drivers and different risk, so we split them.

| | **Family Portfolio** | **Beneficiary Transfer Instruction (BTI)** |
|---|---|---|
| What it is | A live sub-account structure during the holder's life | A standing, pre-authorised instruction on the account |
| Legal character | Account administration | Client instruction under **Custody Rulebook IV.B.2** |
| When it acts | Continuously | Once, at a defined trigger |
| Cost driver | Names under monitoring | Verification at registration, execution at trigger |
| Priced by | The annual plan fee | The per-beneficiary registration fee |

> **Naming.** *"Digital Will"* is the client's emotional centrepiece and it is also the phrase most likely to imply a regulated will-writing service. **The contractual term is Beneficiary Transfer Instruction.** Whether "Digital Will" survives as a marketing name is a counsel question (§14), and we should plan on it not surviving. `Legacy Instruction` is the fallback that keeps the feeling without the legal claim.

---

## 3. Family Portfolio — how it works during life

The primary account holds the master Gold Receipt. It splits into named sub-accounts. **1 AURX = 1 gram** throughout, so every display is a gram count.

| Rule | Content |
|---|---|
| Allocation | Named sub-accounts, each a declared percentage. Total cannot exceed 100% of the master receipt |
| Who controls | The primary holder, entirely. Add, change or remove at any time |
| What the family member sees | Their own grams, value, and credit capacity. **Read-only.** They see *that* a BTI exists, never its terms |
| Ownership during life | **Unchanged — it is all still the primary holder's gold.** A sub-account is a declaration of intent and a display, not a transfer |
| Credit | A sub-account's grams count toward the primary holder's facility. **The family member has no independent facility until transfer completes** |
| ICS | Scores nothing, for anyone (decision 46) |
| KYC | Every named person is verified at registration and screened continuously until the trigger fires or the name is removed |

> ⚠ **Correction to the client's model.** Their §5.2 gives each sub-portfolio "its own credit facility limit" and "its own ICS sub-score" during the primary's life. Neither survives. You cannot lend to someone against gold they do not yet own, and ICS is one number about one person's behaviour. **The family member's benefits begin at transfer, not at designation.**

---

## 4. The instruction — what the customer actually defines

Per sub-account, four fields. The client's five collapse to four because "modification rights" is a property of the transferred account, not of the instruction.

| # | Field | Options |
|---|---|---|
| 1 | **Beneficiary** | A named person who has completed verification. Registration is what is priced |
| 2 | **Trigger** | Date · Condition · Death — see §5, they are **not** interchangeable |
| 3 | **Form** | Full · Phased in tranches by age or date · **(income-only is deleted, see below)** |
| 4 | **Continuation** | Whether SIP contributions to that sub-account continue, redirect, or stop after transfer |

> **"Income-only transfer" is deleted.** Their §5.4(3)(c) transfers "only the ICS Dividend… gold principal transfers later." There is no dividend — it became **Gold Rewards**, a fee rebate in grams capped at what that account itself generated (decision 6). A sub-account with no card spend generates nothing, so income-only would transfer zero. Offering it would be selling an empty box.

**Revocability.** Freely modifiable while the holder is active. **Will Lock-In is retained but re-scoped:** it locks the *allocation percentages*, not the instruction's existence, and it cannot bind against a later grant of probate or a forced-heirship claim. Sold as a commitment to family, never as legal irrevocability.

---

## 5. The trigger ladder — and why beneficiary residence inverts it

**This is the centre of the design.** The three triggers are not three flavours of one thing. They are three different legal events.

| Trigger | What it legally is | Probate? | Forced heirship? |
|---|---|---|---|
| **Date** (a birthday, an anniversary) | A completed **lifetime gift** | **No — holder is alive** | **Shielded.** DIFC Art 15 / ADGM s.29(3) protect completed lifetime transfers |
| **Condition** (a defined, observable event) | Same, if it fires during life | **No** | Shielded, same basis |
| **Death** | **Testamentary succession** | **Yes. Grant required** | **Exposed.** The firewall covers *living persons* only; DIFC Art 105 excludes rights "created by will" |

**So the lifetime trigger is the strong product and we should lead with it** — the education fund and the wedding gift, not the death benefit. It completes cleanly, needs no court, and is the version their own Scenario 2 already describes.

**Now the inversion.** Overlay the beneficiary's residence:

| Beneficiary resident in | **Date / Condition trigger** | **Death trigger** |
|---|---|---|
| **UAE / GCC / rest of world** | ✅ **Preferred.** Clean completed transfer, no probate, heirship-shielded | ⚠ Permitted. Requires grant of probate before execution |
| **India** | ⛔ **Blocked at launch.** OI Rules Sch. III para 2(3) routes a gift from a person resident *outside* India through **FCRA 2010**. Whether it bites turns on the donor's **passport, not residence** — an Indian-passport NRI is generally not a "foreign source", a foreign-passport OCI is. Too fine a distinction to enforce in an app at launch | ✅ **Permitted, settled to cash.** FEMA **s.6(4)** permits a resident to hold assets "inherited from a person who was resident outside India"; OI Rules Sch. III para 2(1) says **"without any limit."** The LRS bar does not reach it — LRS bites on acquisition by remittance, and no remittance occurs |

**Why India-resident beneficiaries receive cash, not tokens.** FEMA s.6(4) is a **closed list of three categories** — foreign currency, foreign security, immovable property. An allocated-gold token is arguably **none of them**, so the inheritance permission may not reach AURX at all. That is a gap rather than a prohibition, but it is not a gap to test with a customer's inheritance. **Settling to cash sidesteps the classification question entirely: the beneficiary receives money through banking channels, and no resident ever holds the token.** This was already our design answer (`handoff.md` §7, counsel batch 1 q3); the research confirms it and explains why.

> ⚠ **The India path is free by construction and must be modelled that way.** Cash settlement is probably a redemption (§6), and Annex 2 III.E.4 forbids any fee on redemption. We cannot charge for the India leg even though it is the most operationally expensive one.

**Beneficiary obligations we should disclose, not advise on:** inheritance is not taxable on receipt (s.56(2)(x)), cost of acquisition carries over with no step-up (s.49(1)), and Schedule FA reporting plus Black Money Act 2015 exposure apply annually to a resident holder. **We state that obligations exist and refer them to their own adviser.** We never compute an Indian tax position.

---

## 6. Execution — the authority gate

The client's §5.6 executes on a trigger. Ours executes on a trigger **plus proven authority**, and the second half is what was missing.

| Step | Lifetime trigger | Death trigger |
|---|---|---|
| 1. Trigger detected | Date reached, or condition evidenced | Death notified by executor or family |
| 2. **Authority** | None needed — the holder is alive and instructed it | ⛔ **Grant of probate or court order. Hard gate.** We do not adjudicate, we wait |
| 3. Beneficiary status | Re-verify identity, re-screen sanctions/PEP, confirm residence has not changed | Same |
| 4. Encumbrance check | Pledged grams resolved per §7 | Same |
| 5. Execution | **In specie.** Sub-account re-registered to the beneficiary on-chain and in the title register | Same, or **cash settlement** where the beneficiary is India-resident |
| 6. After | Beneficiary's own ICS clock starts at zero. Continuation instruction governs the SIP | Same |

**Why in-specie is the default and the only thing we price.** Redemption under Annex 2 III.E is **request-driven, value-delivering and claim-directed** — a beneficiary who receives tokens and keeps them exercises nothing and receives no value from Aurumix. Rule III.B.1.a positively supports this: it requires that ownership "is transferred in the event of a transfer of ownership of the ARVA", treating transfer as a distinct category from redemption. **Cash settlement has every hallmark of a redemption**, so if the beneficiary wants money they onboard, take the tokens, and redeem free of charge like any other holder. We never bundle sale-and-burn into a paid service.

⚠ **Watch III.E.3's "or their designee"** — VARA already contemplates a third party making a redemption request, and a beneficiary is naturally a designee. That does not make in-specie a redemption, but it does put a *redeeming* beneficiary squarely inside the fee ban.

---

## 7. Pledged gold — the ordering their document never states

The holder pledged grams for credit, then the trigger fires.

**The lender wins. Always.** The security attaches to the collateral and survives the holder's death; the beneficiary can only ever take the net residue. Ordering: **secured creditor → estate expenses and other creditors → beneficiary.**

Five clauses the contract must carry, none of which exist today:

1. **The BTI is subordinated to any security interest.** Stated in the instruction itself, visible in the app.
2. **The transfer is of the net interest** after discharge — not the gross sub-account.
3. **Lender consent or release is a condition** to executing over pledged grams.
4. **The beneficiary has an express right to redeem** by paying the outstanding debt and taking the grams whole.
5. **A standstill period** before any enforcement, plus defined apportionment where only part of the sub-account is pledged.

**Death is not an automatic event of default** in consumer secured lending, and we should not let the partner make it one. Market practice — including Indian gold-loan practice, the closest precedent — is procedural: notify, identify successors, preserve collateral, allow settlement.

> This closes the tension flagged earlier: a beneficiary could otherwise watch an inheritance liquidated by a margin call. **They cannot lose more than the debt, and they always have the right to pay it and keep the gold.**

---

## 8. Minor beneficiaries

No new structure is needed; the mechanism already exists.

| Question | Answer |
|---|---|
| Who receives | The grams are held in the sub-account. Payment or receipt by a parent or lawful guardian **discharges our obligation** (DIFC Trust Law Art 69(4)) |
| Until when | Age of majority. ⚠ **This just moved: 18 Gregorian, from 1 June 2026 in the UAE and 2 March 2026 in DIFC** (was 21). Confirm the enacting law number before hard-coding |
| Phased release by age | Drafting, not architecture. Art 69(3) already permits accumulation and advancement |
| Guardianship | We rely on a guardian appointed elsewhere. **We never appoint one** — guardianship of a minor's property is a court matter |

---

## 9. Pricing

**The cost floor, and it is much lower than we assumed.** Every per-name cost with a published price:

| Line | One-off | Annual |
|---|---|---|
| Identity verification | USD 1.25-1.85 | — |
| AML / PEP / sanctions at onboarding | USD 0.35-1.05 | — |
| Continuous screening per name | — | **USD 0.36** |
| **Floor** | **~USD 1.80-2.90** | **~USD 0.36** |

**Everything else in the chain is per-will or per-entity, never per-name** — DIFC Full Will AED 10,000, **DIFC Digital Assets Will (Form 6) AED 5,000**, DIFC probate USD 1,500 flat, ADGM Foundation ~USD 1,000 setup / USD 500 renewal. None of it scales with beneficiary count, so none of it belongs in a per-name fee.

**Two costs that actually bind, and neither is the per-check rate:**

- **The monitoring tail.** A beneficiary stays screened until the trigger fires — potentially 20-40 years. At USD 0.03/month that is **USD 7-14 per name undiscounted**, and no provider publishes multi-decade terms. *This*, not the USD 2 check, is what the per-name fee is really buying.
- **The platform minimum.** USD 99-299/month. **Below roughly 2,000 names a year the monthly minimum dominates unit economics entirely**, so at launch the marginal name is nearly free and the fixed cost is what hurts.

**Two corrections to `_draft_ics-benefits.md` §5.2.** Our "no published comparable exists anywhere" claim is **wrong** — Casa publishes crypto inheritance at **USD 250/yr with heirs included**. And **per-beneficiary pricing has essentially no precedent in any adjacent market**: Casa, Trust & Will (USD 49/yr), Farewill (GBP 10/yr), Everplans (USD 99.99/yr), DIFC, banks and brokerages all price flat per will/plan/entity, and beneficiary designation at a bank is conventionally free.

**So the structure, given a saver contributing USD 240-900 a year:**

| | Recommendation | Why |
|---|---|---|
| **Annual family plan** | **USD 29-36/yr**, including **up to 4 registered beneficiaries** | Brackets Farewill and Trust & Will. At USD 48 a USD 20/month saver pays 20% of a year's contributions — too much. The plan fee funds the monitoring tail |
| **Per additional beneficiary** | **USD 20 one-off**, capped per household (~USD 60) | Anchors trivially against an AED 10,000 DIFC will. The cap prevents the product punishing people for having a family — fatal in something called a *Family* Portfolio |
| **Charged when** | **At registration. Never at the transfer event** | The defence against recharacterisation as a redemption fee |

**Against the discount ladder already fixed in `_draft_ics-scoring.md` §6.5** — plan fee 0/10/20/35/50%, per-name 0/0/0/20/20% — a Sovereign pays ~USD 15-18/yr and USD 16/name. Against a ~USD 2.90 floor that is **5x headroom on the deepest discount.** The design rule holds comfortably across the whole range, which it would not have if the floor were where we assumed.

**No VARA rule caps ancillary fees or requires them to be cost-reflective.** The only hard obligation is disclosure: **Market Conduct II.B.1.e** requires "all fees charged by the VASP for the services" in the Client Agreement. Both prices go in.

---

## 10. What the score does and does not do

| | |
|---|---|
| Does the family earn ICS? | **No.** Removed entirely (decision 46). Registering names is not saving behaviour |
| What the tier does | Discounts the two prices. **A price, never a gate** |
| Is the feature tier-gated? | **No. Open to everyone who pays.** This is what broke the client's circularity |
| Can the discount reach 100%? | **No.** Free at the top rebuilds the tier-gate in mirror image and un-funds the cost exactly where it is highest |

---

## 11. The perimeter — what Aurumix never does

The sharpest risk here is not fees, it is **licensing**. No VARA licence covers trust, fiduciary, estate administration or will-writing, and estate administration in the UAE is court-supervised.

| We do | We never do |
|---|---|
| Execute a documented standing instruction on an account | Determine who is entitled to an estate |
| Require a grant of probate before a death transfer | Validate a death or adjudicate competing claims |
| Register and monitor named beneficiaries | Draft, witness or register a will |
| Tell customers to maintain a valid will in their own jurisdiction | Advise on estate planning, tax or succession |
| Refer to a licensed will-writer | Pay or accept a referral commission for it (Rule III.C.5) |

**The structuring hook is Custody Rulebook IV.B.2**, which permits a VASP to "obtain and rely on any pre-authorised instruction from a client" where it has considered "all reasonably foreseeable circumstances" and communicated them in advance. **That sentence is the legal home of this entire product**, and it is why the BTI is drafted as a standing instruction rather than a testamentary instrument.

**Two further characterisation traps:** marketing it as *planning* edges toward advising; presenting it as a benefit paid on death edges toward insurance. Both need permissions we do not hold.

---

## 12. Compliance screen

| Test | Result |
|---|---|
| Scales with capital? | **No.** Both fees are flat — per plan and per name, never per gram |
| Touches the exit? | **No**, by construction. Charged at registration; in-specie transfer is not a redemption; cash settlement is free |
| Payout capped at generated? | n/a — no payout |
| Creates a security? | **No.** A service fee for account administration |
| Partner-dependent? | **No for the plan fee.** Execution referrals only |
| Marketable as claimed? | ⚠ **Only after the probate and Sharia copy corrections in §1 and §14** |

---

## 13. Corrections owed to other files

**Three are citation errors that would be noticed in a filing.**

| File | Correction |
|---|---|
| `handoff.md` §5, decisions 23/32, `_draft_ics-benefits.md` §0.2, `_draft_purchase-structure.md`, `Aurumix_Process_Maps_Redemption_Fee.md` | 🔴 **The no-fee-on-redemption rule is Annex 2 (ARVA Rules) Part III.E, not "Issuance Rulebook III.E".** Part III of the main rulebook is *Whitepapers and Public Disclosures*. Cite as "Annex 2 III.E" |
| Same set | 🔴 **The Issuance Rulebook is dated 19 May 2025, not 19 June 2025** |
| `handoff.md` decision 25, decision 24, counsel batch 4 q1 | 🔴 **DIFC Trust Law Art 60(6) does not support the permissioned-token decision.** Art 60 is headed *"Duties of trustees"*; 60(6) is an AML/beneficial-ownership duty aimed at **corporate parties to the trust**, enforced by the Registrar. It is not a requirement to identify every holder. **The permissioning conclusion may well survive on VARA and AML grounds — the stated legal basis does not.** Counsel batch 4 question 1 is built on this misreading and must be re-cut before it is sent |
| `handoff.md` decision 25 | 🔴 **ADGM bankruptcy remoteness is s.30, not Art 33.** Art 33 is "Restrictions on transfer to and by a Foundation". Forced-heirship firewall is s.29(2)-(5); no-rights-in-specie is s.31 |
| `_draft_ics-benefits.md` §5.2 | "No published comparable exists" is **wrong** — Casa, USD 250/yr, inheritance included. And **DIFC has a Digital Assets Will (Form 6)** at AED 5,000, a direct comparable and a possible partner route |
| `_draft_ics-benefits.md` §5.5, §5.6 | The pledged-gold and estate-settlement rows are now answered here (§7, §6), not open |
| `_draft_sip-rulebook.md` §9.5 | "Family portfolios → open to everyone **and scoring**" is superseded. Open to everyone, **scoring nothing** (decision 46) |
| Client's `100 G Business_Model.md` §5.2, §5.4, §5.6, §4.6 | Sub-account credit facility and ICS sub-score during the primary's life; income-only transfer; "without requiring probate"; dividend accruing to beneficiaries |

---

## 14. What remains open

**For counsel — three, and the first is worth more than the other two combined.**

1. 🔴 **Confirm the in-specie / redemption split with VARA in pre-application dialogue, in writing.** The rulebook never defines "Redemption", our position is inference from structure, and the entire pricing model rests on it. A written confirmation is far cheaper than a post-launch recharacterisation.
2. 🔴 **The licensing perimeter opinion** across VARA, DFSA, FSRA, SCA and MoJ — including whether the phrase *"Digital Will"* itself implies a regulated will-writing service, and whether the Custody IV.B.2 standing-instruction framing holds.
3. 🔴 **The Muslim-customer position, and do not pre-judge it.** DIFC CA 002/2020 held Sharia inheritance rules are not DIFC public policy, but the Court **declined jurisdiction** over the onshore anti-circumvention rule that voids "every fraud to the provisions governing inheritance". A completed lifetime gift (*hiba*) is defensible; a transfer made in death-sickness, or where the customer **retains control and can redeem on demand** — which is exactly what our product looks like — is exposed. **Never market this as overriding Sharia shares.**

**Second batch, cheaper:**

4. **India-domiciled customers.** Succession to movables follows the **deceased's domicile at death** (Indian Succession Act s.5(2)), and Gulf-resident NRIs on renewable visas very often retain Indian domicile of origin. An Indian court could apply the Hindu Succession Act, or Muslim personal law with its **one-third bequest cap**, to our nomination. **Recommend a domicile declaration at onboarding plus an explicit disclosure.**
5. **Whether the classification gap in FEMA s.6(4) matters** once we settle India-resident beneficiaries to cash. We think it disappears; confirm.
6. **Confirm the age-of-majority enacting law and commencement** before hard-coding age logic. Sources conflict on the law number.

**Commercial, not legal:**

7. **The KYC contract rate and the monthly platform minimum** at our projected name volume. This sets the real floor, and rack rates are not it.
8. **Multi-decade monitoring terms** — what happens if the vendor raises rates or exits over a 40-year instruction. The biggest unpriced tail in the model.
9. **Base prices, client sign-off**, against the ranges in §9.

**For us:**

10. **Re-cut counsel batch 4 question 1** once the Art 60(6) correction lands — it currently asks a question built on a misreading.
11. **Process maps.** The call set is §5 (the trigger/residence matrix), §6 (execution with the authority gate), §7 (pledged gold ordering) and §1 (what we can and cannot promise). §5 is the leave-behind.

---

*Verified primary text: `_source_difc_trust_law_2018.txt` (DIFC Trust Law 2018, this directory).*
