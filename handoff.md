# Aurumix — Handoff / Context Doc

> **Read this first in any new chat.** It carries the full context of the Aurumix engagement so a fresh session starts loaded — no need to re-explain from scratch.
> **Last updated:** 2026-07-22
> **Update protocol:** Refresh this file whenever the working context reaches ~80% (when a new chat is about to be spun up). Keep it current, concise, and decision-focused.

---

## 0. TL;DR (30-second orientation)

We (Tokenomics.net) are building a **tokenomics Data Room** for **Aurumix**, a UAE (Dubai, VARA) gold-backed savings token — currently **just an idea, pre-build**. The client model recently **pivoted to "V3 / 100% Gold"** (authoritative) from an older V2 (superseded). Our current focus: produce a **near-perfect Mechanism Design (MD) doc**, preceded by Market Research, following a decision-driven blueprint. A **client call is upcoming ("Friday")** to answer ~12 open questions. We have full latitude to redesign the model (with reasoning); legal *opinion* is the only thing we don't produce (we tee it up for their counsel).

---

## 1. The engagement

- **Who we are:** Tokenomics.net — advisors building the client's Data Room. We fix every knowledge gap except the legal opinion.
- **Process:** the `tokenomics` plugin's 7-phase Data Room (Discovery → Market Research → Mechanism Design → Supply-Side → Revenue Modeling → Simulations → Whitepaper). Deliverables go in `deliverables/` — **currently empty (pre-kickoff)**.
- **Stage:** pre-kickoff. Proposal written, discovery call done. No deliverables produced yet. Next major deliverable = the MD (highest value for the client).
- **Repo:** git, branch `main` only (see conventions). Remote: github.com/Abdsys/Aurumix.

## 2. People

- **Client (Aurumix):** Gaurav Khullar (founder), CG (Chetanya, co-founder).
- **Us:** Tony Drummond (lead), **Abdur Rehman (the user, abdur@tokenomics.net)**, Harshit Oberoi (intro'd the deal; will handle platform/dev later).

## 3. Authoritative sources & file map

**Source of truth = V3.** V2 is historical context only.

- `client container/100 G Business_Model.docx` / `.md` — **CURRENT V3 spec** (17 sections). The `.md` is the clean readable copy.
- `client container/Aurumix_Complete_Master_Reference_v2.docx.md` — **OLD V2** (70/30 split, algo pool, company-set price formula). Superseded.
- `Aurumix_V3_Business_Model_Explained.md` (root) — our full structured walkthrough of V3, gaps flagged (`⚠ GAP`). Best single explainer.
- `Aurumix_MD_Blueprint.md` (root) — **the plan we're executing**: how to build the MD, decision-driven, MR → B1..B10.
- `deliverables/1-market-research/Aurumix_Market_Research.md` — **Phase A COMPLETE**: 10-track deep-researched, QC'd market research with confidence tags and precedent→MD-block map. Key comparable found: **ORO** (Dubai yield-bearing gold token).
- `questions-discussion.md` (root) — open items split into **Questions** (13, clarify with client on Friday) and **Discussion Points** (2: credit risk engine, AURX classification).
- `company container/Proposal/Aurumix_Engagement_Brief.md` — our 7-phase proposal (⚠ written against V2 — needs re-scoping to V3).
- `company container/notes/Aurumix_Summary.md` (V2 critique) + `Aurumix_V3_Summary.md` (V3 critique).
- `company container/meeting-notes/2_June.md` — discovery call transcript.

## 4. The product (V3 "100% Gold") in brief

Full detail in `Aurumix_V3_Business_Model_Explained.md`. Essentials:

- **100% of every dollar buys physical LBMA gold** (no split, no algo pool, no pricing formula). Token price = total vault gold × LBMA fix ÷ tokens. **1 AURX = 0.01 g** (pegged). **No hard cap** — supply scales with gold bought.
- **Individual Gold Receipt** (on-chain, per investor). **Buyback** at gold price post-lock-in, funded by liquidating own grams.
- **SIP**: $20 min / $75 target monthly; lock-in 6mo–25yr. **Confirmed SIP** after 6 consecutive events → protected allocation.
- **Mining Events**: SIP Event + Spot Event; 3-lane allocation (SIP / ICS-spot / external-spot).
- **ICS (Investor Conviction Score)** governs 4 things: allocation priority, spot access, credit ratio, dividend share. 7 tiers (Green→Sovereign).
- **ICS Dividend**: 15–20% of Aurumix operating profit; 80% to top 10% by ICS-weighted score.
- **Credit facility + Gold Card**: borrow against gold (50% Gold tier → up to 110% Sovereign); LTV warning 80%, liquidation 100%.
- **Family Portfolio + Digital Will**: sub-portfolios + on-chain inheritance.
- **3-tier agent network** (anti-MLM cap), paid from fee revenue. Fees: entry 2–5%, custody 0.8–1% (currently "in grams"), credit fees.
- **9 smart contracts**, 5-layer architecture. Targets: 500 (Y1) → 10–14k (Y3) → 60–100k (Y10).

## 5. Regulatory frame (RWA / UAE) — critical

- **Bodies named in V3:** VARA (primary), LBMA (gold standard), FATF (Travel Rule), FIU-IND (India AML, Phase 2), FEMA (India, NRI context). **Absent vs V2:** RBI, ADGM, DIFC, Dubai VA Law — likely gaps.
- **UAE RWA framework (from rwalabs.ae guide):** 6 token categories (ARVA / Security / Payment-Stablecoin / Utility / Closed-Loop / Hybrid); 5 regulators (VARA-Dubai, CMA-federal-securities [formerly SCA], CBUAE-stablecoins, ADGM/FSRA, DIFC/DFSA). 7-phase tokenization process — **Phase 2 (classification) is the make-or-break step; misclassification forces a full rebuild.**
- **Where Aurumix lands:** gold core = clean **ARVA under VARA** (retail-friendly). **The dividend + credit make it a HYBRID** → risk of dual regulation (VARA + CMA securities + lending regime), which fights the mass-retail model.
- **VARA economics:** ~AED 100k app + 200k/yr supervision; min capital AED 1.5M or 2% reserves; 6–9mo+; each ARVA needs standalone approval.

## 6. Key conclusions/decisions reached so far (our synthesized reasoning)

These are worked-through positions from prior discussion — carry them forward:

1. **Custody fee must NOT be deducted in grams** (the doc's current design) — that breaks the 1:0.01g peg (peg = grams ÷ tokens; removing grams drops the ratio). **Recommendation:** charge the fee **in cash, skimmed from SIP inflow + at entry/redemption gates**, never touching grams. Keeps the peg exact (PAXG/XAUT do this) and removes secondary-market fee-leakage. Accrue daily, settle cash periodically.
2. **Custody fee is cost-recovery, not revenue.** Only the spread above true custodian cost is margin. Booking gross custody as profit inflates the dividend (which is paid from "operating profit") — a VARA/audit red flag.
3. **The ICS Dividend is the biggest classification risk.** A profit-share tied to the enterprise looks like a security. **Direction:** keep the *token* pure-gold (ARVA), deliver dividend + credit **off-token / via licensed structures** so AURX doesn't become a security/hybrid.
4. **Lock-in double-counts in the dividend** — it's an ICS component AND the standalone Dividend Multiplier (ICS-Weighted = ICS × Value × Multiplier). Compounding lock-in². Decide: intentional super-weight (calibrate) or fix to one channel.
5. **"Mining / oversubscription" no longer has an economic function** in V3 (price = pure gold, so buying this event vs next = same price). It's now purely a retention/FOMO device. Decide: keep the framing or simplify to "gold DCA + tier-earned spot." Note: throttling oversubscription also throttles AUM growth.
6. **Three-lane percentages don't reconcile** (SIP 90% + ICS-spot 80% + external 20% can't sum) — needs client clarification (likely different denominators).
7. **Token standard:** fee/KYC/credit/dividend/buyback rights all fail to survive a permissionless ERC-20 DEX transfer → argues for permissioned base (ERC-3643) + optional ERC-20 wrapper (rights suspended in wrapped form until re-registration).
8. **Real-yield route for the dividend (from market research):** the Dubai peer **ORO** funds gold yield via an external gold-leasing partner (**Monetary Metals**) that pays interest on gold, in gold — genuine yield-on-asset, not recycled fees. This is the compliant answer to the "recycled fees" critique (Q11): fund the dividend from a real external gold-yield source, framed as asset-yield (not enterprise profit-share, which is the securities risk). Trade-off: leasing encumbers gold, denting "100% allocated/unencumbered" — must be capped/disclosed/risk-managed. Put on the table for B5.

## 7. Open questions & status

See `questions-discussion.md`. 12 **Questions** to resolve on the **Friday client call**; 2 **Discussion Points** (credit risk engine; AURX classification) we work through ourselves. The MD blueprint marks each dependency as **[FRIDAY]** (client input) or **[LEGAL]** (recommendation + question for counsel).

## 8. The plan (what we're executing)

`Aurumix_MD_Blueprint.md`. Method: **Market Research (Phase A) feeds Mechanism Design (Phase B, blocks B1–B10)**, built as an ordered sequence of questions via the **Working Loop** (frame → reason → decide → ripple-check → log). B1 (Classification & Token Architecture) is the spine and goes first. Output is layered (dev spec + investor narrative + compliance). A running **Decision Log** becomes the MD backbone.

## 9. Working preferences & conventions

- **Git: push directly to `main` only. Never feature branches, never PRs.** (Solo data-room repo.) Commit + `git push origin main`.
- **User likes `.md` files** at the repo **root** (not in folders) for readable reference docs. Confirm-then-save rhythm: often review in chat first, then save.
- **Style:** decision-driven, plain-language, reasoning shown. User is sharp on economics/regulation and asks probing follow-ups — engage substantively, flag gaps proactively, offer to log findings.
- **Commit trailer:** `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.

## 10. Current status & next action

- **Phase A (Market Research) is COMPLETE** and pushed to main — 10 tracks, QC'd, incl. the ORO (Dubai) comparable and its Monetary Metals real-yield model. Lives in `deliverables/1-market-research/`.
- **PENDING TASK (user will run next session):** remove em dashes (—) from `deliverables/1-market-research/Aurumix_Market_Research.md` using the **`tokenomics:web3-copywriter`** then **`tokenomics:humanizer`** skills/agents. Do NOT touch en dashes (–) in numeric ranges (2–5%, 6–9 months). The user already changed the H1 em dash to a colon; the body still has em dashes.
  - ⚠ Agent-availability note: in the 2026-07-22 session the `tokenomics:web3-copywriter` and `tokenomics:humanizer` **agents** were deregistered ("no longer available"), but the equivalent **skills** were still available. Agent availability is per-session — check the available-agents list next session; use the agents if present, otherwise invoke the skills via the Skill tool.
- **Next design step:** **B1 (Classification & Token Architecture)** — the spine. User to signal when to start; Claude suggested pre-loading B1 before the Friday call.
- Friday client call pending to answer the open Questions (now 13, incl. physical-redemption Q13).

## 11. Update protocol for this doc

When context nears ~80%: append new decisions to §6, update §7 status after the Friday call, update §10 current-status, bump the "Last updated" date. Keep it tight — this is a living index, not an archive.
