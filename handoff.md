# Aurumix — Handoff / Context Doc

> **Read this first in any new chat.** A living index, not an archive. Detail lives in the deliverables; this points at them.
>
> ⚠ **Read §0 and §9 first, then grep for what your task needs.** Loading this file whole cost ~35k tokens on 2026-08-19, which is most of a context window spent before any work starts. It was trimmed that day from 408 lines. **Keep it that way: add a pointer, not a paragraph.**
>
> **Last updated:** 2026-08-19. **Phase 4 is at brief v2.4 and is where the next session starts** (§9). Two things happened that day. The segment layer was rebuilt from primary sources: six occupational segments became four regional ones, the population was re-cut **from Indian to South Asian**, and **Bahrain left the model** on the CBB rulebook. Then a second pass **measured the fabrication premium instead of guessing it**, which moved §0.3 and three other things — D26 to D30, and `supporting/_working_dealer-premium-and-comparables-research.md`.

---

## 0. TL;DR

Tokenomics.net is building a Data Room for **Aurumix**, a UAE (Dubai, VARA) gold-backed savings token. The client's app is due early September.

| Phase | State |
|---|---|
| 0 Discovery | ✅ Complete, client-reviewed |
| 1 Market Research | ✅ Complete, 52-page summary delivered |
| 2 Mechanism Design | 🔄 Design complete across eleven drafts and sixteen map sets. **What remains is propagation debt, not design** (§9 item 1) |
| 4 Revenue Modeling | 🔄 Brief at **v2.4, awaiting Abdur's sign-off on the engine.** `reference_model/` is the oracle |

**The product in one line:** 100% of every dollar buys allocated physical gold, 1 AURX = 1 gram, monthly SIP from USD 20, behaviour-scored benefits (ICS), a credit facility and a gold-backed card.

**Where the money actually is:** the **card is 83.4% of Year 10 gross profit**. The savings product is the funnel. **No profitable year in ten**, peak funding **USD 15.1m**. 🆕 **The entry-fee cut to 3% is still not funded, but the framing changed at v2.4: it now breaks even and leaves nothing over, rather than being short by 0.79pp** (D28/D29). **The binding cost is no longer the dealer's premium; it is the float carry.**

**Three gates govern the critical path and the client controls two:** the **bullion dealer** (still unnamed), the **title opinion**, and the **persona**.

**The five things a new session most often needs to know:**

1. **All 51 decisions live in `deliverables/2-mechanism-design/_decisions-log.md`.** §6 here is only the index. **Read the log entry before acting on any decision.**
2. **Decision 50 reversed the token-standard chain** (AURX can be an open ERC-20 with a blocklist). Decisions 10, 24, 33, 37, 38 and 40 are all revised by it and **none of that propagation has run.**
3. **`client container/100 G Business_Model.docx` / `.md` is the single source of truth.** ⚠ The client calls it "VERSION 3"; **say "the 100 G Business Model"**, because "V3" also meant a dead pricing formula.
4. **v1.0's Phase 4 numbers must not be quoted anywhere.** They did not reconcile. Every figure now comes from `reference_model/`.
5. **Plan before build.** Propose architecture changes as a plan and get agreement *before* touching code or regenerating artefacts. **The brief is the deliverable; the reference model serves it.**

---

## 1. The engagement

- **Us:** Tokenomics.net, advisors building the client's Data Room. We fix every knowledge gap except the legal opinion.
- **Process:** the `tokenomics` plugin's Data Room. Deliverables in `deliverables/{n}-{step}/`.
- **Timeline:** 6 weeks from 2026-07-24, target 4 to 11 September, anchored to the client's build milestone.
- **Repo:** git, `main` only. Remote: github.com/Abdsys/Aurumix.

## 2. People

- **Client:** Gaurav Khullar (founder), **Chetanya Goel ("CG")** (co-founder, primary contact). ⚠ Not "Gupta".
- **Us:** Tony Drummond (lead), **Abdur Rehman (the user)**, Harshit Oberoi (platform/dev later).

## 3. File map

**Source of truth = `client container/100 G Business_Model.docx` / `.md`** (17 sections).

| File | What it is |
|---|---|
| `client container/100 G Business_Model.md` | **CURRENT SPEC** |
| `client container/Aurumix_Complete_Master_Reference_v2.docx.md` | **OLD model.** Superseded |
| `Aurumix reply .docx` | Client's written answers. **Red text is their replies** |
| `Aurumix_V3_Business_Model_Explained.md` | Our walkthrough, gaps flagged `⚠ GAP` |
| `Aurumix_MD_Blueprint.md` | ⚠ **Stale in six places** (B3.3, B5.3, B6.3, B6.4, B9.3, B1.6). **Follow DRODE, not the blueprint** |
| **0-discovery/** | |
| `Aurumix_Project_Charter.md` | ✅ Client-reviewed. 🔴 **Persona needs widening, see §9 item 2** |
| `questions-discussion.md` | ✅ All 15 questions answered |
| **1-market-research/** | |
| `Aurumix_Protocol_Landscape.md` | ✅ **The authoritative research artifact.** 19 protocols, 292 sources, registry-first |
| `Aurumix_Market_Research.md` | ✅ Earlier, narrower, 5 protocols |
| `Aurumix_Market_Research_Summary.md` / `.html` | ✅ **DELIVERED.** 52 pages. Generated: edit `_summary_working/`, never the `.md` |
| **2-mechanism-design/** | |
| `_decisions-log.md` | 🔴 **THE DECISION LOG. All 51 in full.** Append here, index in §6, same commit |
| `Aurumix_Legal_Brief_and_Open_Questions.md` | 🔴 **361 lines, "for review". Client-facing, for onward instruction of counsel.** Part 1 describes the build for a lawyer with no prior exposure; Part 2 is the open legal questions. ⚠ **Check against decision 50 and the enforcement-sale-as-redemption question before it is sent** |
| `_draft_sip-rulebook.md` | **THE CANONICAL SIP DOC.** Where it conflicts with the two older drafts, it wins. §12 is its corrections list |
| `_draft_ics-scoring.md` | **B4 DONE.** `ICS = min(Record, Standing) × Retention`, five tiers. §1.2 is the load-bearing argument. §12 is a long corrections list |
| `_draft_ics-benefits.md` | The five benefits defined mechanically. ⚠ **Written against seven tiers**, needs a tier-count pass |
| `_draft_composability-and-ownership-route.md` | **Decision 50, the biggest reversal in the project.** §6 lists what it revises |
| `_draft_credit-and-card-infrastructure.md` | Decision 49. One facility, two draw channels. **Nine corrections owed, two filing-grade** |
| `_draft_family-and-succession.md` | Decision 51, rewritten onto custodied gold. **§0 carries the whole document.** Three 🔴 filing-grade corrections in §16 |
| `_draft_referral-system.md` | Decision 47. **§5.4 holds the one open decision and it is Abdur's: reward size** |
| `_draft_entities-licensing-and-payments.md` | Entities, licence stack, ownership construct, payment rails, India |
| `_draft_purchase-structure.md` | Full purchase lifecycle, both lanes. **Mechanics only; costs excluded.** §8 is a ten-item reconciliation list |
| `_draft_allocation-and-float.md` | Procurement, float, denomination, premium, dividend. ⚠ **Stale gold-price figures throughout** |
| `_draft_sip-spot-and-ics.md` | Early decision draft. ⚠ Superseded in parts by the rulebook |
| `_parked_collection-economics-and-minimum-ticket.md` | 🔴 **PARKED, not retracted. `C_min = R ÷ (f − c)`.** **REOPENS NOW** — it is the minimum-ticket answer (§9 item 3) |
| `_explainer_how-we-take-money.md` | Answers client additions 1, 2 and 3 in full |
| `_explainer_ownership-structure-plain-english.md` | Seven questions in non-legal language |
| `Aurumix_ICS_Score_Calculator.xlsx` | One tab, live, **built for presenting.** Rebuild `_build_ics_calculator.py`, check `_verify_ics_calculator.py`. ⚠ LibreOffice absent, so `recalc.py` cannot run |
| `_source_vara_issuance_rulebook_2025.txt` | Verified primary text. **Confirms 19 May 2025 and Annex 2 III.E** |
| `_source_difc_trust_law_2018.txt` | Verified primary text. **Caught the Art 60(6) misreading.** Keep; DIFC site 403s |
| **Process map sets** (16) | ICS_Scoring (10, **the ICS call set**), ICS_Benefits (8, ⚠ seven-tier pass owed), Composability (8), Credit_And_Card (11), Family_And_Succession (8, **map 5 must never be cut**), Referrals (4), Minting (8), Redemption (7), Redemption_Fee (1), Revenue_Streams, Payments (7), Custody_Fee, Ownership_Structure (4), SIP_Structure + SIP_Spot_ICS (⚠ **both owe the 2026-08-10 revision**), `Aurumix_Process_Maps.md` (14, ⚠ predates SIP/spot/ICS) |
| **4-revenue-modeling/** | |
| `Aurumix_Revenue_Model_Architecture_Brief.md` | 🔴 **v2.2. THE THING TO REVIEW.** ~4,100 lines, 23 sections. **Read §0** (findings), **§3** (the engine — the sign-off gate), **§3.y** (what the approach cannot do), **§5** (segments, rebuilt 2026-08-19). ⚠ **All output figures are still from the v2.0 ten-year run and will move.** §15 lists **25 corrections owed** |
| `reference_model/` | **The oracle for the Excel build.** `NUMERICAL_SPINE.md` (703 lines) + `VALIDATION.md`. ⚠ **Not rebuilt for D21–D23, and not re-run since the D25 segment re-cut** |
| `supporting/` | v1.0 preserved; `_working_parameter-completion-set.md` (~50 inputs v1.0 never supplied); `_working_corpus-omissions-extract.md`; **`_working_architecture-decisions-v2.md` = the D1–D30 record with the finding that forced each** |
| 🆕 `supporting/_working_dealer-premium-and-comparables-research.md` | **The 2026-08-19 evidence pass. F4 measured; PAXG / XAUT / Comtech binding terms; Tradeflow; LBMA.** ⚠ **Read §1 before doing any premium work — it carries the same-page method that fixed a measurement error which had returned impossible sub-spot prices** |
| **company container/** | `Proposal/Aurumix_Engagement_Brief.md` ⚠ written against the OLD model, superseded. `meeting-notes/2_June.md` = discovery transcript, Voice of Customer |

⛔ **Never point a directory-scanning skill at `deliverables/1-market-research/`.** Overlapping working copies. Pass explicit file paths.

🔧 **Summary rebuild** (only if reopened): `_summary_working/` → `npm install`, `python assemble.py`, `python build.py`, `node render.js`, `python lint.py`. Clean bar: four empty arrays from `render.js` and `TOTAL: 0` from `lint.py`.

## 4. The product in brief

- **100% of every dollar buys physical gold.** No hard cap. **1 AURX = 1 gram.**
- **SIP**: USD 20 min / 75 target / no max, **amount variable month to month**. 🔴 **The USD 20 floor is inherited from the client and does not clear break-even** (§9 item 3).
- **The contractual lock is deleted.** Missing a payment costs **ICS only, no financial penalty**.
- **ICS**, 5 tiers, 4 named (No tier / Silver / Gold / Platinum / Sovereign). Measures behaviour, never amount. **Spot earns no ICS.**
- **Credit + Gold Card**, max LTV **80% at Sovereign**, ladder **50 / 65 / 80**. ⚠ Warning and liquidation thresholds must be re-spaced. ⚠ **A lending partner who maxes below 80 is a repricing event.**
- **Pledged gold still earns ICS and dividend.**
- **No physical redemption.** Exit is cash buyback only.
- **Family Portfolio + Digital Will**, plus a **3-tier agent network** on the Indian insurance agency model.
- **Fees:** entry 2 to 5%, custody 0.8 to 1% (⚠ **3 to 6× real cost**), credit fees, **merchant interchange**.
- Targets: 500 (Y1) → 10 to 14k (Y3) → 60 to 100k (Y10). 🔴 **Nobody has said whether that means accounts opened or investors still contributing. They differ by 3.06×.**

## 5. Regulatory frame

**Verified against the VARA and CBUAE rulebooks 2026-08-04. Detail and URLs in `_draft_entities-licensing-and-payments.md`.**

- **VARA activities are licensed one by one.** Aurumix needs **Category 1 VA Issuance** (AED 100k application, 200k/yr, capital AED 1.5M or 2% of Reserve Assets). Each extra activity is +50% of the lower application fee. **No approval timeline is published anywhere; never give the client a date.**
- **The Issuance Rulebook uses gold as its worked example** and splits gold tokens into **stable-value** and **direct-ownership**. We chose direct-ownership (decision 23).
- **Redemption is OPTIONAL for an ARVA**, and where granted, **no fee may be charged on it** (Annex 2 III.E.4).
- **Lending and cards are CBUAE, not VARA.** Lending against pledged gold needs a bank or full Finance Company licence. **The CBUAE holds the sole right to issue BINs**, so a card needs a bank as BIN sponsor. **Partner for both, do not build.**
- **A wind-down plan is MANDATORY** (Company Rulebook Part VII.A), twelve prescribed contents.
- **VARA's remit covers Dubai including free zones, EXCEPT DIFC.** The issuer cannot sit in DIFC.
- **Travel Rule threshold is AED 3,500**, not the USD 1,000 in the client's document.
- 🆕 **Bahrain: the CBB Crypto-Asset Module binds and VARA does not passport in.** Tokens are securities under Art. 1 CBB Law; CRA-15.1.1 needs written CBB approval; BD 50,000 capital; escrow at a CBB-licensed retail bank; offers only through a **CBB-licensed digital token advisor**. **No reverse-solicitation exemption exists in 246 pages of text.**
- 🆕 **Oman: no VASP regime is in force.** FSA Decision E/35/2023 bites on local establishment and is silent on inbound marketing. **A gap, not a permission.** Regulator is the **FSA, not the Central Bank.**
- **Bodies in frame:** VARA, CBUAE, SCA (if a profit share is issued), RBI/SEBI/IFSCA on India, **CBB and Oman FSA** on the GCC perimeter. DIFC or ADGM enters as a holding jurisdiction, not a regulator.
- ❌ **There is no cheap compliant door.** Of 19 protocols only 4 hold a licence covering the token they issue. **The DMCC route around VARA does not exist.**

## 6. Decisions carried forward

**Full text: `deliverables/2-mechanism-design/_decisions-log.md`. The titles below are pointers, not summaries. Read the log entry before acting.**

Markers: ✅ settled · 🔄 revised or superseded · ⚠ carries a caveat · 🔴 load-bearing or unresolved

| # | | Decision |
|---|---|---|
| 1 | 🔴 | THE MISSING COUNTERPARTY, and it gates everything |
| 2 | ✅ | Mining Events: solved |
| 3 | ✅ | The gold float is the mechanism that makes it work |
| 4 | ✅ | 1 AURX = 1 gram, permanently |
| 5 | 🔄 | SUPERSEDED. Now: recover custody at ENTRY and EXIT, never off the metal |
| 6 | ✅ | Dividend → Gold Rewards |
| 7 | 🔴 | THE PREMIUM IS ZERO. Model it at zero everywhere |
| 8 | ✅ | Spot: restrict benefits, not supply |
| 9 | ✅ | Entry fee must sit at the top of the 2 to 5% range at launch |
| 10 | 🔄 | **REVISED BY 50.** Token standard: permissioned base + optional wrapper |
| 11 | ⚠ | "LBMA" means two things and the client's doc conflates them |
| 12 | ⚠ | Sourcing is a live risk, not a theoretical one |
| 13 | ✅ | Distribution is the actual moat |
| 14 | ⚠ | Failure precedent: tokens die of revenue starvation, not regulators |
| 15 | ⚠ | rwa.xyz is reliable for enumerating, unreliable for describing an issuer |
| 16 | ⚠ | "Audited" almost never means the gold was checked |
| 17 | ⚠ | SIP and agent precedent, now three models not two |
| 18 | ✅ | SIP and spot are transaction types on one account |
| 19 | ✅ | The contractual lock-in is deleted |
| 20 | ✅ | ICS measures behaviour only. Investment Value removed entirely |
| 21 | ✅ | The miss-and-recover ladder, plus one financial rule |
| 22 | 🔴 | Persistency is the number that governs the calibration |
| 23 | ✅ | Direct-ownership ARVA (Option A), not stable-value |
| 24 | 🔄 | **REVISED BY 50.** The token is the trigger, not the proof |
| 25 | ⚠ | Entity structure: three routes, route 2 recommended |
| 26 | ⚠ | Title record: Tradeflow preferred, vault books a real fallback |
| 27 | 🔴 | India is closed to residents, on two independent bars |
| 28 | 🔴 | Payments: two hard rules, and one changes the product |
| 29 | ✅ | The money question is solved. VARA's Client Money Rules |
| 30 | ✅ | Stablecoin: yes in substance, no in instrument |
| 31 | 🔴 | The GCC is not one market. ⚠ **Corrected twice; see §9 item 2** |
| 32 | 🔴 | VARA prohibits charging anything on the way out |
| 33 | 🔄 | **REVISED BY 50.** "Open DEX listing incompatible with Option A" is **WITHDRAWN** |
| 34 | ✅ | Money, then title, then token, and never any other order |
| 35 | 🔄 | SUPERSEDED IN PART 2026-08-10, twice over |
| 36 | 🔄 | REVISED 2026-08-10: two of three states survive |
| 37 | 🔄 | **REVISED BY 50.** VARA mandates no token standard |
| 38 | 🔄 | **REVISED BY 50.** Art 60(6) no longer supports the permissioned token |
| 39 | 🔴 | An ADGM Foundation defeats the ownership claim |
| 40 | 🔄 | **REVISED BY 50.** Switch 3 has three landings, not two |
| 41 | ✅ | Grams are fungible. No such thing as a SIP gram or a spot gram |
| 42 | ✅ | Custody recovery: move the bill to the counterparty that can be billed |
| 43 | ✅ | The SIP payment layer goes push-only; four states become two rules |
| 44 | ✅ | The ICS benefit set is finalised at five; tenure rebate retired |
| 45 | ✅ | The benefit definition layer is written and B4 is unblocked |
| 46 | ✅ | B4 IS CLOSED. `min(Record, Standing) × Retention`, five tiers |
| 46a | 🔄 | SUPERSEDED IN FULL BY 46 |
| 47 | ✅ | THE REFERRAL SYSTEM IS DESIGNED. An acquisition cost, not a benefit |
| 48 | ✅ | FAMILY PORTFOLIO AND SUCCESSION ARE DESIGNED. **Probate cannot be avoided** |
| 49 | ✅ | THE CREDIT AND CARD STACK IS DESIGNED. One facility, two draw channels |
| 50 | 🔴 | **AURX CAN BE AN OPEN ERC-20. Reverses 10, guts 33. Read before 10/24/33/37/38/40** |
| 51 | ✅ | B6 REWRITTEN. The family product runs on custodied gold, not on-chain |

**Phase 4 architecture decisions D1–D25 are recorded separately** in `deliverables/4-revenue-modeling/supporting/_working_architecture-decisions-v2.md`.

**When you add a decision:** append to the log and add its row here in the same commit.

## 7. Open questions

**Blocking, all dealer conversations, not research:**
- Identify a **two-way Dubai bullion dealer or accredited refiner**.
- Will that dealer **carry the float**, and at what spread? And **will they take grams back on demand, at what spread** — a separate commitment from carrying inventory, and the zero-fee-exit argument rests on it.
- Real Dubai **fabrication premiums, two-way spreads and minimum tickets** per denomination.
- **DMCC Tradeflow fees and terms**, and **does Tradeflow support sub-accounts, fractional interests or a beneficial-owner layer?** Arguably more important than the fees. Also ask why Comtech put only 19 kg of 111 kg on the register.
- 🔴 **Who will originate merchant AANI Request to Pay collections, and at what per-request cost?** **This one number sets the minimum ticket and decides whether half the book is viable** (§9 item 3). Not answerable by desk research.
- **Indicative setup and annual cost of a DIFC or ADGM holding vehicle.**

> ⚠ **Dubai's wholesale gold market is commercially opaque by convention.** Four research passes have returned the same negative result. **Name this as project risk to the client.**

**🔴 For the client's COUNSEL.** Consolidated in `Aurumix_Legal_Brief_and_Open_Questions.md`, which is the sendable artefact. Batches below are the working record.

**Batch 1, the three only they can commission, two of which gate the build.**
1. **Does title transfer with the token?** Given allocated serial-numbered bars, bailment in the terms, and registration on Tradeflow. **Determines the product, the capital requirement and the marketing.**
2. **Can allocated but pooled gold be reclaimed from an onshore UAE bankruptcy estate? If uncertain, does a DIFC or ADGM vehicle materially improve it?** **Decides route 1 versus route 2.**
3. **Confirm the India perimeter** and the **inheritance carve-out**. Sharpened: **FEMA s.6(4) and s.9(d) enumerate foreign currency, foreign securities and immovable property. A tokenised commodity is none of the three.** **Design answer needing no ruling: settle to cash for any India-resident beneficiary.**

> **Batch 2, payments, lower priority. Send separately.**
> 1. **Is a published list of licensed exchanges, with no commercial arrangement, "arranging" a payment token service?** **The only load-bearing assumption in the payment design.**
> 2. **VARA requires overseas client money in Client Accounts with third-party _banks_.** Most local-collection providers are **e-money institutions, not banks**. Does that satisfy the rule? **It decides whether cross-border SIP collection is viable at all.**

> **Batch 3, purchase structure, all cheap, each decides a mechanism.**
> 1. **Does "equal value" in III.E.1 mean full prevailing value or realisable value net of the dealer's bid?** Decides who absorbs the spread on every exit.
> 2. **Is a published formulaic buyback a "right of redemption" for III.E purposes?** Assume yes; confirm.
> 3. **Can a periodic custody charge be satisfied by deducting the customer's own grams under express authority?**

> **Batch 4.** ⚠ **Question 1 is built on the dead Art 60(6) reading and MUST be re-cut before sending** (§9 item 1).
> 2. **Does an ADGM Foundation's s.29(1) vesting defeat the direct-ownership claim?**
> 3. **Is there any DIFC or ADGM analogue to UCC Art 7 "control" of an electronic document of title?**
> 4. **Is there DIFC Court authority on the proprietary nature of a beneficiary's interest?**

> ⚠ **Nine further questions arise only because Option A was chosen.** Full list in `_draft_entities-licensing-and-payments.md` §8. **Consequential, not blocking. Do not put them in the call.**

**Still open, need the client:**
- **Intended use of the finished Data Room.** Asked twice, never answered. Phrasing that lands: *"When this is finished, what's the first thing you'll do with it, and who's the first person outside your team who reads it?"*
- **Google Drive access** (holds the differential fee structure for spot vs SIP).
- **Final spot capacity %**, **fixed cost structure / operating budget**.
- **The dividend trilemma**, as an explicit three-way choice.
- 🔴 **Does the 60 to 100k Year 10 target mean accounts opened or investors still contributing?** **They differ by 3.06× and drive different lines.**

**Open on our side:**
- 🔴 **The minimum ticket.** §9 item 3. The live thread.
- **Pricing rule is inconsistent across three drafts.** **Recommend "the next published LBMA fix, AM or PM, whichever comes first", used identically on entry, arrears and exit.** ⚠ "Cleared funds" has no defined cut-off or timezone.
- **Sequencing bug in `_draft_purchase-structure.md` §5.3:** the exit table lists the rebate after the burn while its own text says before.
- **Three exit checks owed to §5.3:** onboarding status per III.E.3, residence re-check, rapid in-and-out flag. ⚠ **Checks must run before the price is struck.**
- **Whether the float sits inside or outside the trust is undecided.** Drawn as outside. **The two positions must never commingle.**
- **Bank name-match tolerance is undesigned.** Transliterated names will fail an exact-string match.
- 🔴 **Possible arithmetic conflict in the tenure rebate.** Decision 32 pays back ~1.5% at 12 months; decision 9 leaves 0.85% gross margin. **Unless the 1.5% is funded by an uplift to the spot entry fee, the spot lane is loss-making by design.** Not stated explicitly anywhere.
- **The holding vehicle is a party in four mechanisms already designed.** Allocation, buyback, credit pledge, Digital Will. **Real work owed.**
- **Three amendments owed to `_draft_allocation-and-float.md`:** float legally segregated from customer metal; per-channel rail cost, not a flat 0.30%; buyback reconciled against the no-fee rule.
- **Two corrections owed to the client's document:** Travel Rule is AED 3,500; §3.1's "not a pooled allocation" is an overclaim. **Accurate wording: "allocated and segregated from Aurumix's own metal".**
- **Three design details deferred, homeless until the register exists:** credit ratio on all grams or only SIP grams; SIP or spot grams sold first on partial exit; whether arrears can be paid in instalments.
- **Silver product revenue model: INTERNAL USE ONLY.**
- Confirm whether LBMA GD bars lose chain-of-integrity status when vaulted outside the approved-vault network. **This prices the exit.**

## 8. Working conventions

- **Git: push directly to `main`. Never feature branches, never PRs.**
- **Commit trailer:** `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **No em dashes** in deliverables. Colons, sentence splits, parentheses. En dashes in numeric ranges are fine.
- ⛔ **Never find-and-replace repo markdown via PowerShell.** PS 5.1 mojibakes every ✅ ⚠ § in the file. Use the Edit tool.
- **Notion-importable markdown** for client-facing docs: single H1, GFM tables, `- [ ]` checkboxes, no HTML.
- **Style:** decision-driven, plain language, reasoning shown. **Surface inconsistencies rather than silently fixing them.** No analogies in client-facing text.
- **Plan before build.** Architecture changes get proposed and agreed before code or artefacts move. **The brief is the deliverable; the model serves it.**
- **Process maps:** brand theme block on every diagram, `graph LR`, 4 to 6 nodes, **2 to 6 words per node**, gold for solutions, concrete for problems, stone for intermediates, speaker notes in HTML comments. **Reference: `DRODE-Tokenomics/.../block3-diagrams.md`.**
- **Depth benchmark:** `DRODE_Mechanism_Design_v1.md` = 1,252 lines / ~25k words / 20+ parameter tables. Per-mechanism anatomy: mechanic → how it works (numbered) → why X over Y → worked example with table → edge case, **plus a compliance note for Aurumix.** Target 1,500 to 2,000 lines.
- 🆕 **Context discipline.** Read §0 and §9 here, then grep. **Delegate multi-file reading to subagents** — the 2026-08-19 research spent 247k agent tokens and returned 15k to the main context. **Large `Edit` calls cost twice** (old text and new text both count). ⚠ **Before overwriting a file you read earlier in a long session, `git diff` it** — handoff.md gained 30 lines mid-session and a blind rewrite would have destroyed them.

**⚠ Perplexity research method, learned the hard way:**
1. **Never embed the fact you are testing.** Ask "what is the current X", not "it reportedly uses X, confirm".
2. **Run a dedicated recency sweep** as its own dated query.
3. **Never use negative source-exclusion lists.** They cause sonar-pro to skip searching entirely.
4. **Verify the entity, not the story.** Pull the **registry record** and the **terms of issue** first.
5. **Never demand a rigid citation format.** Ask positively: *"write the source URL in the text right after each claim."*
6. 🆕 **When the question is "what does this organisation actually publish or offer", fetch its own page.** Search only finds which page to read. **Primary PDFs and government APIs beat search summaries every time** — the 2026-08-19 sizing work was rebuilt entirely on NCSI, LMRA and CBB source documents after two sonar calls degraded into "tools are disabled, I cannot verify".

**🔧 openrouter MCP:**
- ✅ **Use `perplexity/sonar-pro`. Not `sonar-deep-research`.** ~0.02 to 0.08 USD/query.
- ⛔ **Never pass `max_tokens`.** It crashes the MCP parser. Constrain by instruction.
- ⛔ **Never gate on `validate_model`.** Call the model directly.
- ⚠ **The MCP drops citations.** **Any answer with bare bracket numerals is failed output: re-run it.**
- ⚠ **For load-bearing claims, go to the register, not the search model.**

## 9. Current status and next actions

**Phases 0 and 1 complete. Phase 2 design complete, propagation outstanding. Phase 4 architecture at v2.2, awaiting sign-off.**

> ⚠ **The honest read on the engagement:** we were hired to design the economics, and the economics turned out to be downstream of structural questions the client has not asked. **The deliverable will look different from the proposal, and the client should hear that from us before he notices it.**

### PHASE 4 — the architecture is the gate

**What to read, in order:** brief **§0** (findings), **§3** (the engine, which is the sign-off gate), **§3.y** (what the approach cannot do), **§5** (segments). Everything else is reference.

**Decisions taken, not open:**
- **D21 — 7 years as 24 monthly + 5 annual = 29 columns.** Matches DRODE precedent. Replaces v2.0's 76 columns.
- **D22 — the score machinery collapses to a tenure→tier lookup.** Measured cost ~2% of gross profit at Y7. The **gate stays live** (eligibility is first-order); the rate ladder goes (second-order). The full formula and nine personas survive as a **validation test with a 5% safety gate**, so the collapse is proved rather than assumed.
- **D23 — no cohort triangle.** Five monthly lifecycle curves convolved against the acquisition vector (`SUMPRODUCT`).
- 🆕 **D24 — the bottom-up engine was reopened, tested and confirmed.** Reasoning recorded so it is not re-derived: unknowns argue *against* top-down (it concentrates the answer in one unfalsifiable penetration share and cannot produce a tornado); the §0 findings are structural and survive a wholesale parameter re-cut; and v1.0 proved simpler does not mean safer.
- 🆕 **D25 — six occupational segments become four regional ones** (R1 UAE Indian, R2 UAE other South Asian, R3 Oman, R4 India), each carrying an **average ticket plus a floor share** from which two ticket bands derive. **Bahrain, Emirati and Western expat are named, sized and deliberately not modelled.** `base × ceiling` held at 165,750 against v2.1's 164,900 on purpose.

- 🆕 **D26 — the workbook ships on the firm's standard FIVE-sheet architecture** (Cover, Assumptions, Scenario Parameters, Model, Summary), with the machinery on five working sheets placed after them and **hidden**. Opex and P&L fold into Model as a second row band; Checks hides and mirrors one master flag to Cover. ⚠ **The acyclicity rule had to be rewritten, not relabelled: it was a tab-position test, and hiding inverts tab order against logical order. It is now a by-name test against the §3.x.1 order, written onto the Cover.**
- 🆕 **D27 — CAC is LINEAR.** The convexity curve is a `CAC_CONVEXITY` switch defaulting OFF; calibration moves to Phase 5. Its constants were unsourced and the hockey-stick brake is the saturation ceiling, not the CAC curve. ⚠ **Direct-channel LTV:CAC at high spend is now an upper bound.**
- 🆕 **D28 — F4 IS MEASURED, NOT GUESSED. 100 g at 1.50%, 1 kg at 0.95%**, against the old 3.00 / 2.00 / 0.75. **The ladder was one denomination too pessimistic at every rung.** Good Delivery is **retired as a rung** — Dubai's own GD standard is a 1 kg bar, not 400 oz, so the third rung targeted the wrong object.
- 🆕 **D29 — S51 flips to OWN FLOAT FROM M1**, and the side is now forced rather than chosen. All three routes the comparables use to avoid carrying metal are closed to Aurumix. 🔴 **Inside this: the 0.79% price-gap is a PRICING-CONVENTION cost, not a float cost. It exists because price is struck at the next LBMA fix, hours away; Paxos gets the same exposure near zero with a 5-second quote. That trade-off is worth ~0.79pp and has never been put to the client.**
- 🆕 **D30 — the premium is charged on NET NEW GRAMS**, not gross inflow, because redeemed gold returns to the float. ⚠ **Gated on correction 30, which is undesigned: does redeemed gold return to the float or go back to the dealer? Nobody has written it down.**
- ⚠ **D31–D34 were taken on 2026-08-20 and are NOT summarised here** (rail pass-through, float CoC to a memo line, redeemed gold, a convolution off-by-one). **Read the D-record, not this list.** The brief is at **v2.6**; its own version header still says 2.4.
- 🆕 🔴 **D35 — SPOT IS A CUSTOMER, NOT ONLY A BEHAVIOUR OF SIP ACCOUNTS.** Stream 1b drives spot off `live_accounts`, so **no account can exist before it starts a SIP**, while §5.1's funnel filters everyone on two recurring-mandate tests (IBAN, USD 20/month) that §6.1b says spot does not need. **Spec written at brief §5.9: one population, two doors, spot-only = the residual; adds S56–S59, all `{{UNFILLED}}`.** 🔴 **S59, the spot-to-SIP conversion rate, is the adoption bridge in numerical form and is the one part of it answerable by experiment.** ⛔ **Architecture only. No figure re-cut, no code touched, pending sign-off.** Corrections 39 and 40.

🆕 **Net effect of D28–D30 on a USD 75 ticket: net contribution margin 0.54% → 1.97%, break-even ticket ~USD 29 → USD 10.90, minimum viable entry fee 4.96% → ~3.07%.** **The minimum-ticket problem largely dissolves at the Base rail** (§9 item 3 softens sharply) ⚠ **but at the Conservative rail it is USD 66, so the rail still decides it.** 🔴 **One reversal to note: the SIP lane now clears the Conservative rail (+USD 0.36 where it was −USD 0.82), so "spot is the only lane that survives the adverse rail" is WITHDRAWN.**

⚠ **Do not re-cut any figure before the architecture is signed off.** Every number in the brief comes from the v2.0 ten-year run on the pre-D25 segmentation. Order: agree the architecture → rebuild the reference model → re-cut the figures → build the workbook.

**Next, in order:**

**1. 🔴 THE PROPAGATION DEBT FROM DECISION 50.** The composability reversal changed the token-standard answer after six decisions and several drafts were written on the old one, and **none of it has run.** In order: **(a)** rewrite decisions 10, 24, 33, 37, 38, 40 in the log and flip their index markers; **(b)** withdraw *"an open DEX listing is incompatible with Option A"*, *"both parties must be registered holders"* and *"an unregistered recipient cannot receive AURX"* from `_draft_purchase-structure.md` §4/§6 and `_draft_entities-licensing-and-payments.md`; **(c)** re-cut **counsel batch 4 question 1**, which **must not be sent as written**; **(d)** change the invariant to `trust holdings ≥ tokens outstanding` in the minting and redemption maps; **(e)** add the self-custody-is-a-disposal rule to `_draft_ics-scoring.md` §1.5 and §10. ⚠ **Then the three filing-grade citation fixes from decision 48** (Annex 2 III.E not Issuance Rulebook III.E; 19 May not 19 June 2025; ADGM s.30 not Art 33), reaching five files. 🔴 **The client conversation changed shape: we told him the token had to be permissioned and an open listing was impossible. Both are withdrawn. He is building in September.**

**2. 🆕 🔴 THE SEGMENT RE-CUT REACHES BACK INTO PHASES 0 AND 2.** D25 was built on primary sources (Oman NCSI bulletin, Bahrain Social Insurance wage dataset, the CBB rulebook text, CBUAE FSR 2025, AMFI July 2026, Abu Dhabi 2024 census). Four consequences outside Phase 4:
   - 🔴 **The market is South Asian, not Indian.** Bangladeshis outnumber Indians in Oman (605,486 vs 515,361). **The MEA overseas-Indians table is the wrong instrument** and omits Bangladeshis and Pakistanis entirely. **Correct decision 31 a second time**, and on a different basis than the first correction.
   - 🔴 **The charter persona ("the NRI saver") and the Indian agent-network model are both too narrow.** A client conversation, not a text edit.
   - 🔴 **"UAE, then Bahrain and Oman" is backwards.** Oman is the accessible one; Bahrain needs CBB approval, BD 50,000 capital and a locally licensed digital token advisor.
   - 🔴 **The lowest-income band may have no usable payment rail.** Findex's 85.7% counts **WPS payroll cards with no IBAN**, which cannot carry a mandate or a debit. Mitigant with a date: **CBUAE's Universal Account** (zero minimum balance, real IBAN, aimed at AED 5,000/month earners). Also note **CBUAE has said it will launch digital savings products for low-income earners within one to two years** — the regulator entering our segment.
   - **Five new corrections owed, brief §15 numbers 21 to 25.**

**3. 🆕 🔴 THE MINIMUM TICKET, and `_parked_collection-economics-and-minimum-ticket.md` reopens for it.** The USD 20 floor is inherited from the client and was never calculated. At the brief's own Year 1 waterfall (0.87% available after gold, price-gap and float) and the modelled USD 0.25 rail, **break-even is ~USD 29**; at any researched rail price it is **USD 47 to 249**. **40 to 60% of the book sits at the floor.** ⚠ The parked file's break-even table uses the **old 0.36% price-gap** and must be re-run at 0.79%. **Proposed resolution, not yet agreed: split the two jobs the one number is doing** — keep USD 20 as the *monthly commitment* (market-facing, against Liv Gold at AED 15 and Botim at AED 10) and set the *collection minimum* at break-even, collecting less often via the decision-43 prefunded balance. ⚠ **This rewords the six-consecutive-payments gate from months to collection periods**, which touches ICS.

**4. REBUILD `reference_model/`** to 7 years / 29 columns, apply D22, D23 and **D25's four regions and eight ticket bands**, then re-run the equivalence tests: collapsed-lookup vs full ICS, and convolution vs cohort engine. **If the collapsed tier mix moves stream 2 by more than 5% of gross profit in any year, the collapse is unsafe and must be reverted** — measured headroom is ~2% against a 5% tolerance, so the gate is live, not ceremonial. 🔴 **Expect the minimum viable entry fee to rise above 3.79%**, because the book-weighted ticket falls from ~USD 40 to ~31.5 against a fixed per-collection rail.

**5. RE-CUT THE BRIEF'S FIGURES** from the rebuilt spine and clear the remaining `{{UNFILLED}}` markers.

**6. BUILD THE WORKBOOK.** Eleven sheets, ~200 rows × 29 columns. `reference_model/` is the **oracle** — every cell checkable against it, which neither v1.0 nor the DRODE build had.

**7. FINALISE ICS. Design settled (decision 46); what remains is mechanical propagation.** Work `_draft_ics-scoring.md` §12, which touches seven sections of the rulebook. ⛔ **The "6 contributions" sweep at the top of that list is CANCELLED — do not run it.** The item with reach is the **Green → "No tier" rename**, across five files plus the xlsx and every client-facing string. Take a decision on the three open sub-items in scoring §10 (defaults proposed; none blocks). ⚠ `_draft_ics-benefits.md` §3.1's card mapping and 4-level variant are **moot at five tiers** — mark them.

**8. FINALISE THE PROCESS MAPS.** ⚠ `Aurumix_Process_Maps_ICS_Benefits.md` is **written against seven tiers**. ⚠ **Both SIP map sets owe the 2026-08-10 revision** (hard floor, 5-day grace, no UAEDDS, no declared pause, AED 26.25).

**9. BUILD THE RECONCILIATION REGISTER.** Maps §6's conclusions + the 15 questions + 6 delegated items + 6 parked additions onto the B-blocks, tagged **DECIDED / OURS-NOW / CLIENT-BLOCKED / COUNSEL**. **Still the unblocking artifact and it still does not exist.** The "6 delegated items" are named nowhere; reconstruct from `questions-discussion.md`.

**10. FOLD THE DRAFTS INTO THE MD DOCUMENT** (`_draft_entities-licensing-and-payments.md`, `_explainer_how-we-take-money.md` + maps, `_draft_purchase-structure.md` working its §8 list of ten). **Expand `_draft_allocation-and-float.md`:** numbered procurement steps, edge cases, the entry-fee build-up as its own section, plus the three §7 amendments.

**11. Cheap verification tasks.** Confirm the registered Foreign Payment Token list with CBUAE; confirm BitOasis and CoinMENA AED rails by hand; re-pull VARA's register before publishing the signpost list. ⚠ **CMA Decision No. 4 of 2026**, a reported federal virtual-asset rulebook — **Confidence: Low, single weak source.** **DIFC formalities for assigning an equitable interest** would upgrade decision 40 to usable with counsel. 🆕 **UN DESA 2024 migrant stock by origin** would replace the unsourced UAE nationality spine. ⚠ **Run `_verify_ics_calculator.py`; LibreOffice is absent here so `recalc.py` cannot run** — if another PC has it, run once as an independent check.

🆕 **A walkthrough of the engine is in progress, for Abdur, one step per reply.** Steps 1–6 done: what the model is for; bottom-up vs top-down (D24); the 29-column grid (D21); sheet order and acyclicity; the four acquisition channels; the channel-to-region matrix. **Resume at step 7, the saturation ceiling.** ⚠ **Frame the rest around the THRESHOLD, not the forecast** — Abdur's position, and correct: the useful output is the minimum scale that covers the cost base, then a strategy to reach it. **§14.2's diverging-curves chart is the artefact for that**, and the required-scale number already exists: **~45,102 contributing accounts on all streams, against 21,661 on the Base path. Entry-fee-only has no crossing at any N.**

🆕 🔴 **THE ADOPTION BRIDGE IS NOT A DELIVERABLE IN ANY PHASE, AND IT SHOULD BE.** Abdur's framing, 2026-08-19: *the real challenge is bridging a South Asian life-insurance-policyholder mindset to a crypto one.* **The model agrees and prices it but cannot solve it.** `S27`, the archetype mix, is **rank 1 load-bearing and a confirmed sourcing negative** — no source anywhere decomposes a savings-lapse curve into behavioural archetypes. Downstream: **only 53.5% of accounts ever pass the six-payment gate, at a mean of M8.1, and everything worth having sits behind it.** So the strategy question has a precise shape: **how do we move the archetype mix, and get more of the book through six consecutive payments faster?** ⚠ **Closest existing homes are the charter persona (§9 item 2) and the agent-network model, both of which D25 already broke open. Scope it deliberately rather than letting it fall between phases.**

**Open decisions that are Abdur's, not ours:**
- 🔴 **Does a lapsed customer keep the card and the credit facility?** **USD 3.39m/yr, 42% of Y10 revenue.** Nobody has ever asked. It decides whether the largest stream decays with persistency or is immune to it.
- 🔴 **The minimum-ticket resolution** in item 3 above.
- **Should card spend track the savings ticket by segment?** The single largest revenue driver, currently keyed to ticket as an income proxy. If Aurumix's card is realistically a *secondary* card for everyone, that is wrong, and it changes which region is worth acquiring.
- **Brief length.** ~4,100 lines against a 1,791-line benchmark. The build-only material (§10 row map, §12 sheet bands) could split into a companion build spec, leaving ~2,200 lines to review.
- **How hard to land the conclusion.** v2.0 is materially harsher than what v1.0 told the client.

**Client call agenda, in priority order:**

1. 🔴 **THE TIMING COLLISION.** Their app is due **early September**; our Data Room lands 4 to 11 September. ⚠ **Do not say the work is thrown away.** It is a token-contract change plus an identity layer, while the app, wallet and exchange integration largely survive. **Raise it before a rebuild raises it.**
2. 🆕 🔴 **THE PERSONA IS TOO NARROW.** The market is South Asian, not Indian. **Non-Indian South Asians outnumber Indians in Oman and match them in the UAE.** The agent network must recruit beyond the Indian community. Also: **Oman before Bahrain.**
3. 🔴 **The ownership decision**, using `Aurumix_Process_Maps_Ownership_Structure.md`. **Only three things to agree.** ⚠ Keep the nine consequential counsel questions out of the room.
4. 🔴 **India**, and expect resistance. Frame as refocus, not retreat.
5. 🔴 **The missing gold supplier**, framed via the buyback. *"Your document names the vault three times and the seller zero times, and the buyback promise runs entirely through the seller you haven't named."*
6. 🔴 **Six internal contradictions in their own document:** (a) §7.1's empty cell for new investor onboarding, and §7.1 vs §7.2 on spot; (b) Confirmed SIP requires 6 events "at the same monthly commitment" but the amount is variable; (c) Investment Value is both an ICS component and the multiplicand; (d) credit activates at month 6, exactly when a 6-month lock expires; (e) buyback "available at expiry" means a 25-year commitment has no exit for 25 years; (f) §9.3 states 110% LTV then works the example at 85%.
7. **The finalised decisions:** denomination → Mining Events → **the lock-in deletion** (sell it with their own §6.2 table) → the dividend (hardest, and the trilemma is theirs).
8. **Payments**, answering their additions 1 to 3. Call set: Payments maps 5, 6, 7; leave diagram 4. **The line that sells it:** *"Yes, we accept stablecoin money. It arrives as dollars, because the customer converts it himself at a licensed exchange. We never hold a token, so we need no extra licence and carry no extra risk."*
9. **ICS, and four departures from their §8.2 to land.** Walk it from the xlsx. **The two rows that sell it:** a USD 20 saver and a USD 2,000 saver reach the top **on the same day**, and a customer can withdraw **a third of their gold with no effect at all.**
10. **The premium is zero**, before it is embedded in any projection. **"100% LBMA gold" needs re-wording.**
11. **The four client-side open items**, especially the **Data Room objective**, plus the scope conversation owed on additions 1 to 3.

## 10. Update protocol

Append new decisions to the log and index them in §6, same commit. Update §7 after each client call, refresh §9, and **fold working state into the drafts rather than into this file.** Bump the date.

⚠ **Keep this file under ~250 lines.** It was 408 on 2026-08-19 and cost ~35k tokens to load. **Add a pointer, not a paragraph. If an item needs more than three lines, it belongs in a deliverable.** ⛔ **Do not add a dated "previously, on this date" block.** That pattern is what grew the file twice; the decision log and the D-record are the history.
