# Aurumix — Handoff / Context Doc

> **Read this first in any new chat.** Living index, not an archive. Detail lives in the deliverables; this points at them.
> **Last updated:** 2026-07-29

---

## 0. TL;DR

Tokenomics.net is building a Data Room for **Aurumix**, a UAE (Dubai, VARA) gold-backed savings token, currently pre-build with the client's app due early September. **Phases 0 (Discovery) and 1 (Market Research) are complete.** Phase 2 (Mechanism Design) is under way.

**Phase 2 has produced three finalised decisions and one gating blocker.** Decisions: **delete the scarcity layer and replace the Mining Event with a three-layer allocation model plus a gold float**; **1 AURX = 1 gram** (was 0.01 g); **replace the ICS Dividend with Gold Rewards**, a fee rebate paid in grams. Blocker: **the 100 G model never names who sells Aurumix the gold**, and every remaining parameter depends on that counterparty.

Both live in `deliverables/2-mechanism-design/`: the reasoning in `_draft_allocation-and-float.md`, the visuals in `Aurumix_Process_Maps.md` (14 branded Mermaid diagrams with speaker notes).

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

> ⚠ **Terminology trap.** The client labels that document "VERSION 3", but "V3" also meant the third term of an old pricing formula that no longer exists. **Say "the 100 G Business Model" and retire the bare "V3".**

| File | Status |
|---|---|
| `client container/100 G Business_Model.md` | **CURRENT SPEC** |
| `client container/Aurumix_Complete_Master_Reference_v2.docx.md` | **OLD model** (70/30 split, algo pool, pool-share pricing). Superseded |
| `Aurumix reply .docx` | Client's written answers. **Red text is their replies** |
| `Aurumix_V3_Business_Model_Explained.md` | Our structured walkthrough, gaps flagged `⚠ GAP` |
| `Aurumix_MD_Blueprint.md` | The MD plan. ⚠ **Stale, and B4 must precede B3** (§7) |
| `deliverables/0-discovery/Aurumix_Project_Charter.md` | **DONE.** Client-reviewed |
| `deliverables/0-discovery/questions-discussion.md` | **DONE.** All 15 questions with answers |
| `deliverables/1-market-research/Aurumix_Protocol_Landscape.md` | **DONE.** 19 protocols, 13 headings, ~5,650 lines, 292 sources, registry-first. **The authoritative research artifact** |
| `deliverables/1-market-research/Aurumix_Market_Research.md` | **DONE.** Earlier, narrower, 5 protocols. ORO entry corrected in place |
| `deliverables/1-market-research/Aurumix_Market_Research_Summary.md` / `.html` | **DONE, DELIVERED.** 52 pages. Generated: edit body files in `_summary_working/` and rebuild, never the `.md` |
| `deliverables/2-mechanism-design/_draft_allocation-and-float.md` | **Phase 2 working draft.** All current reasoning |
| `deliverables/2-mechanism-design/Aurumix_Process_Maps.md` | **14 diagrams**, branded Mermaid, speaker notes in HTML comments |
| `company container/Proposal/Aurumix_Engagement_Brief.md` | ⚠ Written against the OLD model. Superseded by the charter |
| `company container/meeting-notes/2_June.md` | Discovery call transcript. Voice of Customer source |

⛔ **Never point a directory-scanning skill at `deliverables/1-market-research/`.** `_working/sections/`, `_summary_working/` and `_summary_working/_original/` hold overlapping copies. Pass explicit file paths.

🔧 **Summary rebuild** (only if it is reopened): `deliverables/1-market-research/_summary_working/` → `npm install`, `python assemble.py`, `python build.py`, `node render.js`, `python lint.py`. Clean bar: four empty arrays from `render.js` (`overflowPages`, `emptyPages`, `sparsePages`, `unresolvedTocEntries`) and `TOTAL: 0` from `lint.py`.

## 4. The product in brief

- **100% of every dollar buys physical gold.** No hard cap. **1 AURX = 1 gram** (our decision, was 0.01 g).
- **SIP**: 20 USD min / 75 USD target / no max, **amount variable month to month**.
- **Lock = a contribution commitment, not a token lock.** Missing a payment costs **ICS only, no financial penalty**. Modelled on Indian life-insurance premium schedules.
- **ICS (Investor Conviction Score)**, 7 tiers, governs allocation priority (being removed), spot access, credit ratio, dividend share. **Spot earns no ICS.**
- **Credit facility + Gold Card**, max LTV **90 to 95%** (corrected from 110%). Warning/liquidation thresholds must be re-spaced.
- **Pledged gold still earns ICS and dividend.** Client wants pledgers advantaged.
- **No physical redemption.** Deliberate. Exit is cash buyback only.
- **Family Portfolio + Digital Will**, plus a **3-tier agent network** on the Indian insurance agency model. Advisors onboard and invest for clients but cannot withdraw or sell.
- **Fees:** entry 2 to 5%, custody 0.8 to 1%, credit fees, **merchant interchange** (the one genuinely external stream).
- Targets: 500 (Y1) → 10 to 14k (Y3) → 60 to 100k (Y10).

## 5. Regulatory frame

- **Bodies named:** VARA (primary), LBMA, FATF, FIU-IND, FEMA. **Absent and likely gaps:** RBI, ADGM, DIFC.
- **UAE RWA:** 6 token categories, 5 regulators. **Classification is make-or-break; misclassification forces a rebuild.**
- **Where Aurumix lands:** gold core is a clean **ARVA under VARA**. **The dividend and credit make it HYBRID**, which fights the mass-retail model.
- **VARA economics:** ~AED 100k application + 200k/yr supervision, min capital AED 1.5M or 2% of reserves, 6 to 9 months+.
- **Client's legal:** a Dubai firm also handling VARA compliance. We produce analysis and questions; they produce the opinion.
- ❌ **There is no cheap compliant door.** Of 19 protocols only 4 hold a licence covering the token they issue (PAXG, XAUT, WTGOLD, MG999). The rest run a software-company licence, an adjacent trade/AML registration described as authorisation, or a halo. **The DMCC route around VARA does not exist:** Comtech issues on an expired DAFZA trade licence.

## 6. Decisions carried forward

**Full reasoning in `_draft_allocation-and-float.md`. Full evidence in `Aurumix_Protocol_Landscape.md`.**

1. 🔴 **THE MISSING COUNTERPARTY, and it gates everything.** The model names the vault three times and the seller zero times. Brink's, Loomis and Malca-Amit are vaults; they do not sell gold. **The sharpest version is the buyback**, which §3.2 says is funded by "the custodian liquidating exactly those grams". Custodians do not liquidate. Aurumix needs a **two-way dealer**, a vault (named), an independent assayer, and a title register.
2. ✅ **Mining Events: solved.** Split into **Contribution Date** (own anniversary) → **Allocation** (first LBMA AM fix after cleared funds, T+1) → **Bar Procurement Cycle** (internal) → **Monthly Allocation Report**. **Scarcity layer deleted** on four grounds: no economic sense, premium not assurable, security classification risk, limits market-cap growth.
3. ✅ **The gold float is the mechanism that makes it work.** Working inventory on the metal side, not a reserve. Decouples the investor's ticket from the treasury's purchase, so a 20 USD saver works where PAXG needs 120 USD and XAUT needs 170k USD. It also fixes price risk (30 days → under 24 hours), makes a live quotable price possible, and absorbs buyback outflow. **Launch dealer-carried (the Aurus model), migrate to own capital later.**
4. ✅ **1 AURX = 1 gram, permanently.** Token count is gram count, the invariant reads directly (`float + allocated ≥ tokens outstanding`), and it matches every gram-denominated product in the set. **CG's "10 gram units" is the Indian price-quoting convention, not a token size.** Three fixes owed to their doc: delete "at launch", change 0.01 g to 1 g, and reclassify `price = vault gold × fix ÷ tokens` as a verification identity rather than the price definition.
5. ✅ **Custody fee must be CASH**, skimmed from SIP inflow. Fixed weight rules out grams-in-kind and fee-by-dilution. **The SIP gives Aurumix a monthly cash touchpoint no other gold token has**, which is why cash-only works here and fails for the category.
6. ✅ **Dividend → Gold Rewards.** The current design (out of operating profit, weighted by Investment Value, 80% to top 10%) is a profit share and forces a security classification. Replace with a **fee rebate credited in grams**, funded from **interchange and credit revenue**, **capped at what that customer generated**, **sized by ICS tier earned by behaviour not amount**, never called a yield. **Removing Investment Value from ICS weighting also kills the second double-count.** Realistic size: 0.10 to 0.75% by tier at launch.
7. 🔴 **THE PREMIUM IS ZERO. Model it at zero everywhere.** Liquid markets arbitrage it away; illiquid markets have no price to express it; and either way it is not Aurumix's to set, so promising it creates securities risk. Midas XGZ and ORO both trade at a **discount**. Exposure is one-directional: above NAV holders sell to each other and Aurumix gains nothing, below NAV they all redeem at once.
8. ✅ **Spot: restrict benefits, not supply.** Capping supply looks like a share sale. Denying ICS, dividend, credit ratio and card tier is a loyalty programme. Price the difference (spot ~4 to 5% entry, redemption fee decaying over 6 to 12 months). **Large spot tickets help the treasury.**
9. ✅ **Entry fee must sit at the top of the 2 to 5% range at launch.** Build-up at Y1 on 100 g bars: fabrication premium 3.0% + price-gap risk 0.36% + float cost of capital 0.49% + rail 0.30% = **4.15% before margin**. **A 2% fee loses 0.71 USD on every 75 USD contribution.** The fee then falls to ~4% (Y3) and ~3% (Y10) as bar denomination improves, which is a real scale economy to sell.
10. ✅ **Token standard: permissioned base (ERC-3643) + optional wrapper.** **Lead with wind-down, not rights-survival:** Cache Gold published a wind-down plan, followed it, and still stranded **96% of supply**, because it had no holder registry and never burned redeemed tokens. **An anonymous bearer token cannot be wound down.** ⚠ If a wrapper ships, the rights delta must be in the wrapper's own terms (Kinesis's wrapper strips gold title and yield silently).
11. ⚠ **"LBMA" means two things and the client's doc conflates them.** A **Good Delivery bar** is ~12.4 kg / ~1.4M USD and Aurumix will never hold one. A **bar from an LBMA-accredited refiner** is 1 kg or 100 g and is freely obtainable in Dubai. **Copy XAUm's wording: "99.99% LBMA-accredited gold held in 1 kg bars."** UAE local refiners are **UAEGD**-accredited, a separate voluntary standard.
12. ⚠ **Sourcing is a live risk, not a theoretical one.** **Emirates Gold DMCC was suspended from both the UAEGD and LBMA lists in July 2023.** Naming a single refiner without an **accreditation covenant and substitution clause** (use Aurus's LBMA/DMCC/LPPM multi-list wording) would have broken the core promise overnight.
13. ✅ **Distribution is the actual moat.** **Not one of nineteen protocols has a savings plan, recurring purchase, or retail referral programme.** PMGT's post-mortem names zero distribution as cause of death. **Anti-MLM answer from Aurus:** pay each tier for a function performed, not for recruitment depth, with graduation instead of overrides. Combine with the IRDAI trailing-commission structure for two independent structural defences.
14. ⚠ **Failure precedent: tokens die of revenue starvation, not regulators.** PMGT was **not** killed by AUSTRAC (the Mint began exit talks before any public action and was cleared in July 2025); it charged zero fees, so it had no revenue and no internal advocate. Digix zeroed its own demurrage in 2019 and lived on its ICO treasury until holders voted it away. **Counter-example worth copying: DGLD**, where holders own the gold outright at law, which is why six years of dormancy harmed nobody.
15. ⚠ **rwa.xyz is reliable for enumerating the market and unreliable for describing an issuer.** It invented an ORO issuer, gave AZG four wrong fields, and labelled two protocols "Bankruptcy Remote" with nothing supporting it. **Use it to find protocols, never to describe them.**
16. ⚠ **"Audited" almost never means the gold was checked.** The published audit is usually a **smart-contract** audit while the **reserve attestation** is absent, stale or self-signed. Only DGLD, PAXG and VNXAU have credible independent reserve examination; XAUT's BDO Italia ISAE 3000 is the strongest in the set. **Separate the two explicitly in every deliverable.**
17. ⚠ **SIP and agent precedent.** Indian **insurance** enforces persistency (15-day grace monthly, lapse, revival with arrears). Indian **mutual-fund SIP** does not penalise. **Aurumix = SIP wrapper + insurance persistency.** Agent model = high first-year commission + renewal commission payable only while the policy stays in force + upline override, under IRDAI 2023 caps. ⚠ **Pull the IRDAI text before citing any figures.**

## 7. Open questions

**Blocking, all dealer conversations, not research:**
- Identify a **two-way Dubai bullion dealer or accredited refiner**.
- Will that dealer **carry the float**, and at what spread? Decides whether Aurumix needs working capital at all.
- Real Dubai **fabrication premiums, two-way spreads and minimum tickets** per denomination.
- **DMCC Tradeflow fees and terms**, and whether warrants are available from launch.

> ⚠ **Dubai's wholesale gold market is commercially opaque by convention.** Premiums, spreads, minimum tickets and Tradeflow fees are published by nobody; three research passes returned the same negative result. **Several Phase 2 parameters can only be closed by a counterparty conversation.** Name this project risk to the client.

**Still open, need the client:**
- **Intended use of the finished Data Room.** Asked twice, never answered. Phrasing that lands: *"When this is finished, what's the first thing you'll do with it, and who's the first person outside your team who reads it?"*
- **Google Drive access** (holds the differential fee structure for spot vs SIP). Blocks fee design.
- **Final spot capacity %**, **fixed cost structure / operating budget**.
- **The dividend trilemma**, as an explicit three-way choice: encumber the gold, fund from operating profit, or replace it with Gold Rewards.

**⚠ Client additions of 2026-07-28, recorded and DELIBERATELY NOT SCOPED.** Six asks arrived after charter sign-off, logged verbatim in the charter. **Abdur's instruction was to log them and do nothing else.** Treat the charter's unscoped state as intentional. (1) crypto/stablecoin investment, (2) which countries we can accept from, (3) payment service providers, (4) retail vs institutional split of the market, (5) minimum numbers covering annual expenses plus NRI research, (6) not India/UAE-only.

> ⚠ **Unwritten finding behind item 2.** The client's §16 routes Indian residents via "USDT through P2P/OTC". Under **FEMA**, crypto purchase is not an established permitted **LRS** purpose, so a compliant funding route for an Indian *resident* may not exist. **The charter's primary persona is an Indian resident.** If this holds, the real addressable base is NRIs + UAE residents + other international. **Item 2 gates item 5**, and it pulls RBI/FEMA into the regulatory frame.

**Open on our side:**
- **CG named payment channels as their biggest challenge.** Additions 1 to 3 are them handing it to us. Scope conversation still owed.
- **Silver product revenue model: INTERNAL USE ONLY.** Informs our recommendation, not shared.
- Pull IRDAI 2023 regulation text. Correct 110% → 90 to 95% LTV in the client's doc and re-space thresholds.
- Confirm whether LBMA GD bars lose chain-of-integrity status when vaulted outside the LBMA approved-vault network. **This prices the exit.**

## 8. Working conventions

- **Git: push directly to `main`. Never feature branches, never PRs.**
- **Commit trailer:** `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **No em dashes** in deliverables. Colons, sentence splits, parentheses. En dashes in numeric ranges are fine.
- **Notion-importable markdown** for client-facing docs: single H1, GFM tables, `- [ ]` checkboxes, no HTML.
- **Style:** decision-driven, plain language, reasoning shown. **Surface inconsistencies rather than silently fixing them.** No analogies or figurative framing in client-facing text.
- **Agent availability is per-session.** Check the list; otherwise invoke the equivalent skills.
- **Process maps:** brand theme block on every diagram, `graph LR`, 4 to 6 nodes, gold for solutions, concrete for problems, stone for intermediates, speaker notes in HTML comments. **Reference: `DRODE-Tokenomics/deliverables/2-mechanism-design/supporting/block3-diagrams.md`.**

**⚠ Perplexity research method, learned the hard way:**
1. **Never embed the fact you are testing.** Ask "what is the current X", not "it reportedly uses X, confirm".
2. **Run a dedicated recency sweep** as its own query, dated, reverse chronological.
3. **Never use negative source-exclusion lists.** They cause sonar-pro to skip searching entirely.
4. **Verify the entity, not the story.** Pull the **registry record** and the **terms of issue** first. The ORO error survived a full research pass and collapsed in one minute against a company register.
5. **Never demand a rigid citation format.** sonar-pro refuses. Ask positively: *"write the source URL in the text right after each claim."*

**🔧 openrouter MCP:**
- ✅ **Use `perplexity/sonar-pro`. Do not use `sonar-deep-research`.** ~0.02 to 0.08 USD/query.
- ⛔ **Never pass `max_tokens` to a Perplexity model.** It crashes the MCP parser. Constrain by instruction instead ("under 800 words, no background sections").
- ⛔ **Never gate on `validate_model`.** Both lookup paths are unreliable; call the model directly.
- ⚠ **The MCP response drops citations.** No `citations` or `search_results` field, so bare `[1][2]` markers resolve to nothing. **Any answer with bare bracket numerals is failed output: re-run it.**
- ⚠ **For load-bearing claims, go to the register, not the search model.** Perplexity has contradicted itself and mis-dated events within a single session.

## 9. Current status and next actions

- ✅ **Phase 0 COMPLETE.** Charter delivered and client-reviewed.
- ✅ **Phase 1 COMPLETE.** Landscape (19 protocols) and the 52-page client-facing summary both delivered.
- 🔄 **Phase 2 IN PROGRESS.** Draft section and 14 process maps written. Mining Events, denomination and the dividend are solved. **Not yet written: the ICS block (B4), and the reconciliation register.**

**Next, in order:**
1. **Build the reconciliation register.** Maps §6's conclusions + the 15 questions + 6 delegated items + 6 parked additions onto the B-blocks, tagged **DECIDED / OURS-NOW / CLIENT-BLOCKED / COUNSEL**. **This is the unblocking artifact and it does not exist.**
2. **Then B4 (ICS), not B1 and not B3.** B4 is the hub: 100% ours, zero legal, zero client-blocked, and four other blocks cannot be calibrated without it. **B4 must precede B3**, because B3.5's allocation algorithm *is* ICS. The blueprint has this backwards.
3. **Expand the draft:** numbered procurement-cycle steps, edge cases (inflow spike beyond float, dealer withdrawal, attestation lapse), and the entry-fee build-up as its own section.
4. **Missing block to add to the blueprint: payment rails + geographic eligibility.** Client additions 1 to 3 and the FEMA/LRS problem are homeless and they **gate the revenue model**.

⚠ **The MD Blueprint is stale in six places** (B3.3, B5.3, B6.3, B6.4, B9.3, B1.6) and its format promise is wrong: it says "the Decision Log becomes the MD", but the finished **DRODE MD has no decision log**. Follow DRODE, not the blueprint. **Depth benchmark: DRODE_Mechanism_Design_v1.md = 1,252 lines / ~25k words / 20+ parameter tables.** Per-mechanism anatomy: the mechanic → how it works (numbered) → why X over Y → worked example with table → edge case, **plus a sixth element for Aurumix: a compliance note.** Target 1,500 to 2,000 lines.

**Client call agenda, in priority order:**
1. 🔴 **The missing gold supplier**, framed via the buyback. *"Your document names the vault three times and the seller zero times, and the buyback promise runs entirely through the seller you haven't named."*
2. 🔴 **Four internal contradictions in their own document**, which we do not believe have been raised: (a) §7.1 has an **empty cell** for new investor onboarding, and §7.1 says spot is ICS-only while §7.2 says spot is the entry point for new investors, who have no ICS; (b) Confirmed SIP requires 6 events "at the same monthly commitment" but they confirmed the amount is variable; (c) **second double-count**, Investment Value is both an ICS component and the multiplicand in ICS-Weighted Score; (d) credit activates at month 6, exactly when a 6-month lock expires.
3. **The three finalised decisions**, in this order: denomination (small, easy yes) → Mining Events (they gain a better monthly event) → the dividend (hardest, and the trilemma choice is theirs).
4. **The premium is zero**, before it is embedded in any revenue projection.
5. **"100% LBMA gold" needs re-wording.**
6. The four client-side open items, especially the **Data Room objective**, plus the scope conversation owed on additions 1 to 3.

## 10. Update protocol

Append new decisions to §6, update §7 after each client call, refresh §9, and **fold Phase 2 working state into the draft doc rather than into this file**. Keep it tight: a living index, not an archive. Bump the date.
