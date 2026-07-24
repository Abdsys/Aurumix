# Aurumix — Handoff / Context Doc

> **Read this first in any new chat.** It carries the full context of the Aurumix engagement so a fresh session starts loaded — no need to re-explain from scratch.
> **Last updated:** 2026-07-24
> **Update protocol:** Refresh this file whenever the working context reaches ~80% (when a new chat is about to be spun up). Keep it current, concise, and decision-focused.

---

## 0. TL;DR (30-second orientation)

We (Tokenomics.net) are building a **tokenomics Data Room** for **Aurumix**, a UAE (Dubai, VARA) gold-backed savings token — currently **pre-build**, with the client's app due early September. **Phase 0 (Discovery) and Phase 1 (Market Research) are both COMPLETE and pushed.** The client call on **2026-07-24 resolved 14 of 15 open questions** and **delegated six design decisions to us**. The signed-off **Project Charter** is delivered. **Next up: Mechanism Design (blueprint block B1, Classification & Token Architecture).** Next client call is **Wednesday**.

---

## 1. The engagement

- **Who we are:** Tokenomics.net — advisors building the client's Data Room. We fix every knowledge gap except the legal opinion.
- **Process:** the `tokenomics` plugin's Data Room. Deliverables live in `deliverables/`.
- **Stage:** Phases 0 and 1 complete. Phase 2 (Mechanism Design) is next and is the highest-value deliverable.
- **Repo:** git, branch `main` only (see conventions). Remote: github.com/Abdsys/Aurumix.
- **Charter timeline:** 6 weeks from 2026-07-24 (target 4–11 September), anchored to the client's early-September build milestone.

## 2. People

- **Client (Aurumix):** Gaurav Khullar (founder), **Chetanya Goel ("CG")** (co-founder, primary contact).
  - ⚠ Name correction: earlier drafts said "Chetanya Gupta". **Goel** is correct.
- **Us:** Tony Drummond (lead), **Abdur Rehman (the user, abdur@tokenomics.net)**, Harshit Oberoi (intro'd the deal; handles platform/dev later).

## 3. Authoritative sources & file map

**Source of truth = `client container/100 G Business_Model.docx` / `.md`.**

> ⚠ **Terminology trap.** The client's own cover page labels that document **"COMPLETE BUSINESS MODEL | VERSION 3"**, so "V3" is *their* label for the current model. But **"V3" also meant something else entirely in the old model**: the third component of a pricing formula (price = V1 + V2 + V3, the "Target Alignment Multiplier"), which appears throughout the engagement brief and old critique notes. That formula no longer exists. **Use "the 100 G Business Model" and retire the bare "V3" shorthand.**

- `client container/100 G Business_Model.docx` / `.md` — **CURRENT SPEC** (17 sections). The `.md` is the clean readable copy.
- `client container/Aurumix_Complete_Master_Reference_v2.docx.md` — **OLD model** (70/30 split, algo pool, company-set price formula). Superseded.
- `Aurumix reply .docx` (root) — client's **written answers** to our questions. The **red-marked text is their replies**.
- `Aurumix_V3_Business_Model_Explained.md` (root) — our structured walkthrough, gaps flagged (`⚠ GAP`). Best single explainer.
- `Aurumix_MD_Blueprint.md` (root) — **the plan for the MD**: decision-driven, MR → B1..B10.
- `deliverables/0-discovery/Aurumix_Project_Charter.md` — **DONE.** Client-reviewed, final.
- `deliverables/0-discovery/questions-discussion.md` — **DONE.** All 15 questions with answers, statuses, and supporting research. *(Moved here from repo root.)*
- `deliverables/1-market-research/Aurumix_Market_Research.md` — **DONE.** 10 tracks, QC'd. Key comparable: **ORO** (Dubai yield-bearing gold token).
- `deliverables/_progress.json` — tracks process status. Processes 0 and 1 marked complete.
- `company container/Proposal/Aurumix_Engagement_Brief.md` — ⚠ **written against the OLD model** (70/30, 100B cap, 50-year horizon). **Superseded by the charter.**
- `company container/meeting-notes/2_June.md` — discovery call transcript. **Source for Voice of Customer.**
- `DRODE Tokenomics Project Charter *.md` (root, **untracked**) — another client's charter, used only as a formatting reference. **Deliberately not committed** (contains third-party confidential material). Decide whether to delete.

## 4. The product (100 G Business Model) in brief

- **100% of every dollar buys physical LBMA gold.** Token price = vault gold × LBMA fix ÷ tokens. **1 AURX = 0.01 g** currently. **No hard cap.**
- **SIP**: $20 min / $75 target average / no max. **Amount is variable month to month.**
- **Lock = a contribution commitment, not a token lock.** Committing to 6 months means committing to pay for 6 months. Missing a payment carries **no financial penalty, only ICS loss**. Explicitly modelled on Indian life-insurance premium schedules.
- **Spot capacity = 20–40% of each month's SIP inflow** (not final), split **80% ICS lane / 20% external lane**. So external spot is only **4–8% of SIP inflow**. This is the **primary tunable parameter**: it trades AUM growth against secondary-market premium.
- **ICS (Investor Conviction Score)**, 7 tiers (Green→Sovereign), governs 4 things: allocation priority, spot access, credit ratio, dividend share. **Spot purchases earn no ICS** (score is earned via SIP, spent on spot access).
- **ICS Dividend**: 15–20% of operating profit; 80% to top 10%. **`ICS-Weighted Score = ICS Score × Investment Value`** (multiplier dropped).
- **Credit facility + Gold Card**: max LTV **90–95%** (corrected from 110%). Existing 80% warning / 100% liquidation thresholds **no longer sit sensibly** under this ceiling and must be re-spaced.
- **Pledged gold still earns ICS and dividend.** Client wants pledgers *advantaged*.
- **No physical redemption.** Deliberate: retention + credit revenue. Exit is cash buyback only.
- **Family Portfolio + Digital Will.** **3-tier agent network** modelled on the Indian insurance agency / mutual-fund advisor channel; advisors onboard and invest on behalf of clients but **cannot withdraw or sell**.
- **Fees:** entry 2–5%, custody 0.8–1%, credit fees, **merchant interchange** (the one genuinely external stream).
- Targets: 500 (Y1) → 10–14k (Y3) → 60–100k (Y10).

## 5. Regulatory frame (RWA / UAE) — critical

- **Bodies named:** VARA (primary), LBMA, FATF (Travel Rule), FIU-IND, FEMA. **Absent vs the old model:** RBI, ADGM, DIFC — likely gaps.
- **UAE RWA framework:** 6 token categories (ARVA / Security / Payment-Stablecoin / Utility / Closed-Loop / Hybrid); 5 regulators (VARA-Dubai, CMA-federal-securities, CBUAE-stablecoins, ADGM/FSRA, DIFC/DFSA). **Classification is the make-or-break step; misclassification forces a full rebuild.**
- **Where Aurumix lands:** gold core = clean **ARVA under VARA**. **The dividend + credit make it a HYBRID** → dual-regulation risk that fights the mass-retail model.
- **VARA economics:** ~AED 100k app + 200k/yr supervision; min capital AED 1.5M or 2% reserves; 6–9mo+.
- **Client's legal:** engaged with a **Dubai legal team also handling VARA compliance.** We produce analysis + questions for counsel; they produce the opinion.

## 6. Key conclusions/decisions (carry forward)

1. **Custody fee must NOT be deducted in grams.** Peg = grams ÷ tokens, so removing grams breaks it. **Charge in cash**, skimmed from SIP inflow + entry/redemption gates, accrued daily, settled periodically (PAXG/XAUT precedent). **Delegated to us.**
2. **Custody fee is cost-recovery, not revenue.** Only the spread above true custodian cost is margin. Booking gross custody as profit inflates the dividend — a VARA/audit red flag.
3. **The ICS Dividend is the biggest classification risk.** Keep the *token* pure-gold (ARVA); deliver dividend + credit **off-token via licensed structures**.
4. **Lock-in double-count RESOLVED.** Client confirmed it was unintended. Multiplier dropped; lock-in now lives only inside ICS.
5. **"Mining / oversubscription" has no economic function** now that price is pure gold. But **the scarcity is intentional** — the client is banking on a **3–8% exchange premium** to sustain spot and SIP demand, and accepts the AUM/institutional cost. **Framing is ours to recommend, and they are open to dropping "mining" entirely.** Our leaning: keep the mechanic, drop the metaphor (it implies a PoW/emissions story that invites the wrong regulatory read).
6. **⚠ The premium cannot be predetermined or promised.** It must stay market-driven, or it hands regulators a security characteristic. **This constrains marketing language.**
7. **Token standard:** fee/KYC/credit/dividend/buyback rights all fail to survive a permissionless ERC-20 DEX transfer → **permissioned base (ERC-3643) + optional ERC-20 wrapper**, rights suspended until re-registration.
8. **Real-yield route for the dividend:** the Dubai peer **ORO** funds gold yield via **Monetary Metals** (leases gold, pays interest *in gold*). This is the compliant answer to the "recycled fees" critique: fund the dividend from **real external asset yield**, framed as asset-yield not enterprise profit-share. Trade-off: leasing **encumbers gold**, denting "100% allocated/unencumbered" — cap, disclose, risk-manage.
9. **SIP design precedent (researched 2026-07-24):** Indian **insurance** enforces persistency (grace period 15d monthly / 30d other; miss it → lapse, and no-claim-bonus/loyalty benefits forfeited; revival possible with arrears + interest). Indian **mutual-fund SIP** does the opposite (missed installment simply skipped, no penalty). **Aurumix = SIP wrapper + insurance persistency penalty.** Open design question this raises: should we add a **grace period** and a **revival mechanic** (pay arrears to restore ICS)? Both are precedented and would soften churn.
10. **Agent network precedent:** Indian life agency = high **first-year commission** + lower **renewal commission payable only while the policy stays in force** + **upline overriding commission**, all under **IRDAI (Payment of Commission) Regulations 2023** caps. Maps to: agent takes a share of the **entry fee** + a **trailing share tied to continued SIP contributions**. This solves anti-MLM **structurally** — if trailing income depends on downline investors *continuing to contribute*, recruitment-for-its-own-sake stops paying.
    - ⚠ **Sourcing caveat:** Perplexity Sonar confirmed the *structure* but **could not retrieve the IRDAI 2023 percentage tables or override caps**. **Pull the regulation text directly before citing any figures.**

## 7. Open questions & status

`deliverables/0-discovery/questions-discussion.md` has all 15 with full detail. Summary:

**Resolved by client (2026-07-24):** SIP lock structure & missed-payment treatment · missed-participation allocation · ICS priority order · spot-lane/ICS interaction · pledged gold earns ICS · mining-event substance & spot capacity math · 90–95% LTV · dividend-multiplier double-count · physical redemption excluded · project stage.

**Delegated to us (client explicitly handed these over):**
- Token denomination / unit size
- Custody fee mechanism
- Additional revenue streams
- ICS scoring formula (they gave priority order only)
- Agent commission rates & split (deferred until revenue model exists)
- Mining Event framing (keep, rename, or drop)

**Still open, need the client:**
- **Intended use of the finished Data Room** (VARA submission vs raise vs build spec vs partnership credibility). Asked twice, never answered. **Raise Wednesday.** Suggested phrasing that lands: *"When this Data Room is finished, what's the first thing you'll do with it, and who's the first person outside your team who reads it?"*
- **Google Drive access** — contains the **differential fee structure for spot vs SIP**. Blocks fee design.
- **Final spot capacity %** (currently the 20–40% range).
- **Fixed cost structure / operating budget** — needed for net-profit modelling.

**Open on our side:**
- ⚠ **CG named payment channels as their biggest challenge** (*"how do people invest, and in what formats and which channels?"*) — this is **not currently scoped into any charter phase.** Decide whether it's ours.
- **Silver product revenue model: INTERNAL USE ONLY.** Client asked to see it; decision is we use it to inform our recommendation but do **not** share it.
- Pull IRDAI 2023 regulation text for real commission figures.
- Reconcile sub-gram token unit vs CG's "10 gram units for the Indian market" remark.
- Correct 110% → 90–95% LTV in the client's own documentation, and re-space warning/liquidation thresholds.

## 8. The plan

`Aurumix_MD_Blueprint.md`. Method: Market Research feeds Mechanism Design (blocks B1–B10) as an ordered sequence of questions via the **Working Loop** (frame → reason → decide → ripple-check → log). **B1 (Classification & Token Architecture) is the spine and goes first** — everything else depends on it. Output is layered (dev spec + investor narrative + compliance). A running **Decision Log** becomes the MD backbone.

## 9. Working preferences & conventions

- **Git: push directly to `main` only. Never feature branches, never PRs.** Commit + `git push origin main`.
- **Commit trailer:** `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **No em dashes (—)** in deliverables. Use colons, sentence splits, parentheses. En dashes (–) in numeric ranges are fine.
- **Deliverables go in `deliverables/{n}-{step}/`.** Reference/working docs can live at repo root.
- **Notion-importable markdown** for client-facing docs: single H1, GFM tables, `- [ ]` checkboxes, no HTML.
- **Charter format = the DRODE charter** (9 sections: problem statement, objectives, deliverables, timeline, scope, stakeholders and roles, success criteria, voice of customer, resources and links). Client prefers it **short**.
- **Style:** decision-driven, plain-language, reasoning shown. User is sharp on economics/regulation and asks probing follow-ups — engage substantively, flag gaps proactively, **surface inconsistencies rather than silently fixing them**.
- **Agent availability is per-session.** Check the available-agents list each session; use agents if present, otherwise invoke the equivalent skills via the Skill tool.

## 10. Current status & next action

- ✅ **Phase 0 (Discovery) COMPLETE.** Charter delivered, client-reviewed, final (176 lines, DRODE format). Questions log complete.
- ✅ **Phase 1 (Market Research) COMPLETE.** 10 tracks, QC'd, em-dashes stripped, incl. ORO / Monetary Metals real-yield finding.
- ▶ **NEXT: Phase 2 Mechanism Design, starting with B1 (Classification & Token Architecture).** This is the spine; the dividend/credit classification question gates most downstream design.
- 📅 **Next client call: Wednesday.** Agenda: the four client-side open items in §7, especially the Data Room objective question.

## 11. Update protocol for this doc

When context nears ~80%: append new decisions to §6, update §7 after each client call, refresh §10, bump "Last updated". Keep it tight — a living index, not an archive.
