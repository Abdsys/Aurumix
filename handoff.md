# Aurumix — Handoff / Context Doc

> **Read this first in any new chat.** It carries the full context of the Aurumix engagement so a fresh session starts loaded — no need to re-explain from scratch.
> **Last updated:** 2026-07-28
> **Update protocol:** Refresh this file whenever the working context reaches ~80% (when a new chat is about to be spun up). Keep it current, concise, and decision-focused.

---

## 0. TL;DR (30-second orientation)

We (Tokenomics.net) are building a **tokenomics Data Room** for **Aurumix**, a UAE (Dubai, VARA) gold-backed savings token — currently **pre-build**, with the client's app due early September. **Phase 0 (Discovery) and Phase 1 (Market Research) are both COMPLETE.** The client call on **2026-07-24 resolved 14 of 15 open questions** and **delegated six design decisions to us**. The signed-off **Project Charter** is delivered, with six further client additions logged on 2026-07-28 (recorded, deliberately not yet scoped).

**Phase 1 is being reopened.** A competitor teardown (`Aurumix_Protocol_Landscape.md`) is in progress: 16 live tokenized-gold protocols plus 3 failures, sourced from rwa.xyz, because the original market research covered only 5 and missed 11. **One finding from it is engagement-critical: the ORO real-yield precedent collapsed on re-verification and has been withdrawn (see §6.8).** The research tooling that produced it has also been re-configured: **Sonar Pro only, no Deep Research** (see §9). Next client call is **Wednesday**.

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
- `deliverables/1-market-research/Aurumix_Market_Research.md` — **DONE but incomplete.** 10 tracks (A1–A10), QC'd. Structured around our preliminary questions, which the client has since said is too narrow. Covers only 5 protocols. **Its ORO entry was materially wrong and was corrected in place on 2026-07-28** (A7, plus the two summary references and the findings table): ORO is Singaporean, not Dubai, and is not a compliant precedent. See §6.8.
- `deliverables/1-market-research/Aurumix_Protocol_Landscape_PILOT.md` — **format sample, approved.** Full teardown of one protocol (PGOLD) against 13 headings. The full doc replaces nothing; it sits alongside the market research.
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
8. ⚠ **Real-yield route for the dividend: THE ANCHOR IS GONE (re-verified against primary sources 2026-07-28, second pass).** The *principle* still stands: fund the dividend from **real external asset yield**, framed as asset-yield not enterprise profit-share, rather than recycled investor fees. The worked precedent does not. **This entry supersedes an earlier version of §6.8 that was itself wrong in both directions.**
    - ❌ **The earlier claim that "ORO" and "Orogold" are two different projects was FALSE. They are one project.** `orogold.com` is the support address in ORO's own terms, `usman@orogold.app` is the CEO's address in the Monetary Metals release, and the docs sit at `orogold-1.gitbook.io`. The rwa.xyz Solana `GOLD` listing **is** oro.finance. We had split one company in two, not merged two.
    - ❌ **"The Dubai ORO" does not exist.** The issuing entity on ORO's own transparency page is **Oro Labs PTE Ltd., UEN 202434484G, incorporated 22 August 2024 in SINGAPORE**, ACRA activity "other holding companies / software development". The UAE link is a `+971` phone number in a press release plus gold that is "UAE GD-certified", which certifies **the metal, not the company**. **ORO was never a UAE precedent.** That error originated in our own market research and has now been corrected there.
    - **Nobody is named as the issuer.** ORO's terms say `$GOLD` is *"issued by independent Third-Party Service Providers"* and never names them. The Singapore entity disclaims issuance.
    - **No licence anywhere.** Not VARA, DMCC, ADGM, DIFC, or MAS. The "bankruptcy-remote foundation" exists only in a Solana ecosystem article, with no jurisdiction and no document.
    - **Verification is quarterly (RSM), not monthly**, and the only **downloadable** reports are Cantina / Adevar Labs **smart-contract** audits. No reserve attestation, bar list, or PoR document is published.
    - The **Monetary Metals leasing relationship is real** and mutually confirmed, but only in *marketing*. The front page promises **3 to 4 percent APY**. Leasing **does encumber the gold**. There is still **no legal documentation showing how holders' claims rank against lease-counterparty default.**
    - ✅ **Implication, and it resolves the decision that was pending with Tony.** Do **not** spend more time hunting for a documented real-yield precedent: ORO was the strongest candidate and it is a Singapore holding company with no regulator. Its role **inverts**. It is now positive evidence that this exact structure is being run live, at scale, with zero regulatory anchoring, which is useful ammunition of the same kind as the PGOLD finding in §6.12. **Re-anchor the dividend argument on Kinesis account-level mechanics plus Ondo's token separation, and take the leasing structure to counsel as an open structuring question before B1 closes.**
9. **SIP design precedent (researched 2026-07-24):** Indian **insurance** enforces persistency (grace period 15d monthly / 30d other; miss it → lapse, and no-claim-bonus/loyalty benefits forfeited; revival possible with arrears + interest). Indian **mutual-fund SIP** does the opposite (missed installment simply skipped, no penalty). **Aurumix = SIP wrapper + insurance persistency penalty.** Open design question this raises: should we add a **grace period** and a **revival mechanic** (pay arrears to restore ICS)? Both are precedented and would soften churn.
10. **Agent network precedent:** Indian life agency = high **first-year commission** + lower **renewal commission payable only while the policy stays in force** + **upline overriding commission**, all under **IRDAI (Payment of Commission) Regulations 2023** caps. Maps to: agent takes a share of the **entry fee** + a **trailing share tied to continued SIP contributions**. This solves anti-MLM **structurally** — if trailing income depends on downline investors *continuing to contribute*, recruitment-for-its-own-sake stops paying.
    - ⚠ **Sourcing caveat:** Perplexity Sonar confirmed the *structure* but **could not retrieve the IRDAI 2023 percentage tables or override caps**. **Pull the regulation text directly before citing any figures.**
11. **A third option on the custody fee (from PGOLD).** We had framed this as a binary: charge in grams and break the peg, or charge in cash. **Pleasing Gold charges holders nothing** and recovers custody cost from redemption fees, institutional gold turnover, and trading revenue. Worth putting on the table alongside our cash-settlement recommendation, with the caveat that it presupposes an attached trading business Aurumix does not have.
12. **The "recycled fees" anti-pattern is running live in the market.** PGOLD advertises a **5% yield on ~$79–90M** (roughly $4M/yr) funded from redemption fees on rare redemptions plus trading fees on a market doing **under $20 a day**. The disclosed sources cannot plausibly fund the promise, and because nothing is disclosed the claim is unfalsifiable. This is our exact ICS Dividend critique, in public, and it is useful ammunition.
13. ⚠ **Evidence against the premium thesis.** §6.5 assumes a 3–8% exchange premium will sustain spot and SIP demand. **PGOLD holds ~$79–90M of AUM with essentially no functioning secondary market** (~$1.7M liquidity, sub-$20 daily volume). Accumulating assets and having a market liquid enough to produce a reliable premium are **separate problems**, and the second does not follow from the first. This needs stress-testing in Phase 4.
14. **Comtech Gold (CGO) is the closest structural precedent to Aurumix, and it does not use VARA.** Dubai, DMCC-approved vaults, Shariah-certified by **Amanie Advisors**, monthly proof of reserve with published bar lists, redemption in UAE. It operates on a **DMCC trade licence with no VARA or ADGM authorisation found**. That suggests a Dubai gold-token path that routes around VARA entirely. **Directly relevant to B1: investigate before assuming VARA is the only door.**
15. **Failure precedent: tokens die of adjacent risk, and they fade rather than blow up.** **PMGT** was discontinued not through any defect in the token but through **AUSTRAC AML enforcement against Perth Mint plus the Shanghai Gold Exchange gold-doping scandal**. **Digix** dissolved its DAO via a clean structured treasury return while DGX itself never formally shut, it just went illiquid. **Cache Gold** wound down quietly with no post-mortem and the fate of residual gold unverified. **None published a wind-down plan.** Aurumix should commit to one ex ante: it is cheap differentiation and it is what every one of these failures lacked.

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

**⚠ Client additions of 2026-07-28 (recorded, DELIBERATELY NOT SCOPED):**

Six further asks arrived after charter sign-off. They are recorded verbatim in an **"Additional comments from client"** section at the end of `Aurumix_Project_Charter.md`. **Abdur's explicit instruction was to log them and do nothing else: do not re-scope the charter, move the delivery date, or fold them into phases.** Treat the charter's unscoped state as intentional.

1. Enable investment in crypto (stablecoin) as well as fiat.
2. Determine which countries we can accept investment from, under either method.
3. Identify service providers to enable that payment flow.
4. Establish the **retail vs institutional split** of the tokenized gold market before sizing ourselves into it (our model discourages institutions). *Note: the existing market research quotes only total figures, so this is a genuine gap.*
5. Derive **minimum numbers that cover annual expenses** instead of the 500 / 10–14k / 60–100k targets. Above that floor, build strategies for bridging the Indian life-insurance mindset to crypto savings, via agent channels. **NRIs are the other large market**: study how they invest and remove friction.
6. Not built only for India, UAE and NRIs, though the focus leans there because we understand those markets best.

⚠ **The unwritten finding behind item 2, not yet in any deliverable.** The client's own 100 G Business Model §16 routes **Indian residents via "USDT through P2P/OTC"** with the investor bearing tax disclosure. Under **FEMA**, crypto purchase is not an established permitted **LRS** purpose (RBI has never approved it; Indian banks block it), so a compliant funding route for an Indian *resident* may not exist. **The charter's primary persona is the Indian life-insurance policyholder, who is a resident.** If this holds, the real addressable base is **NRIs + UAE residents + other international**, which is likely why the client is pushing NRIs hard. That makes item 2 a **gating question that must precede any break-even sizing in item 5**, and it pulls **RBI/FEMA** into the regulatory frame (see §5, which already flagged RBI as a likely gap).

**Open on our side:**
- ⚠ **CG named payment channels as their biggest challenge** (*"how do people invest, and in what formats and which channels?"*). Items 1–3 above are the client answering this: **it is ours now**, but it remains outside every charter phase. Scope conversation still owed.
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
- ⚠ **Perplexity research method (learned the hard way, 2026-07-28).** A PGOLD profile stated the protocol used LayerZero when it had **publicly migrated to Chainlink CCIP eight weeks earlier**. Three causes, all avoidable:
    1. **Never embed the fact you are testing into the prompt.** Asking "it reportedly uses LayerZero, confirm" makes a search model go and confirm it. Ask "what is the current X".
    2. **Always run a dedicated recency sweep** as its own query: state today's date, ask for all announcements, migrations and incidents in the last 12–18 months, reverse chronological, dated.
    3. **Never use negative source-exclusion lists.** A prompt opening "do NOT rely on CoinGecko, IQ.wiki..." caused sonar-pro to **skip searching entirely** and reply "I do not have live web access." Steer positively instead.
    4. **Verify the entity, not the story.** The ORO error (§6.8) survived a full research pass because every source repeated the same marketing framing. It collapsed in one minute against a **company register**. For any protocol we intend to cite as precedent, pull the **registry record** (jurisdiction, number, incorporation date, activity code) and the **terms of issue** before anything else. Aggregator profiles, ecosystem blog posts and issuer press releases are the *last* resort, not the first.
    - Treat wiki/aggregator-sourced facts as provisional until date-checked. Label issuer press releases as issuer-sourced: reliable for the fact of an event, not its framing.

- 🔧 **openrouter MCP: settled configuration (diagnosed 2026-07-28, supersedes earlier notes).**
    - ✅ **Use `perplexity/sonar-pro` for all research. Do not use `perplexity/sonar-deep-research`.** Decision taken by Abdur 2026-07-28. Sonar Pro is ~$0.02–0.08/query, returns resolvable inline URLs when asked to, and has not failed once. Also available if ever needed: `perplexity/sonar-pro-search`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar`.
    - ⛔ **Never pass `max_tokens` to a Perplexity model.** This is what was killing the batch. `sonar-deep-research` with `max_tokens: 120` returns `Error: OpenRouter API error: Cannot read properties of undefined (reading '0')`; the identical call with the parameter **omitted** succeeds cleanly. Deep Research spends its budget on an internal retrieval phase before emitting any content, so a low cap yields a response with no `choices` array and the MCP server crashes parsing it. The error reads like an API outage. It is our own parameter.
    - ⛔ **Never gate on `validate_model`.** It returns "Model not found" for `perplexity/sonar-deep-research` even though `search_models(provider: "perplexity")` lists it. Free-text `search_models(query: ...)` also returns 0 of 341 models. Both lookup paths are unreliable; call the model directly.
    - ⚠ **The MCP response drops citations entirely.** A successful call returns only `[id, choices, created, model, object, usage]`. There is **no `citations` and no `search_results` field**, so the `[1][2][15]` markers in the prose resolve to nothing. **This, not truncation, is the cause of the `[AUSTRAC-releases]` / `[AU-press-SGE]` placeholders in the failures batch.** The fix is mandatory prompt wording: *"put a source URL inline immediately after each individual claim, not as an end-of-answer list."* Verified working. **Any answer that comes back with bare bracket numerals is failed output: re-run it.**
    - **Cost cannot be capped with `max_tokens`.** Constrain by instruction instead ("under 800 words, no background or history sections"). A one-line question to Deep Research produced 13,065 tokens of padding for $0.24, which is the other reason we are off it.

## 10. Current status & next action

- ✅ **Phase 0 (Discovery) COMPLETE.** Charter delivered, client-reviewed, final. Six client additions appended 2026-07-28, recorded not scoped.
- ✅ **Phase 1 (Market Research) COMPLETE**, but **reopened** for the protocol landscape work below.
- ▶ **IN PROGRESS: `Aurumix_Protocol_Landscape.md`.** A competitor teardown covering 16 live tokenized-gold protocols plus 3 failures. Client asked for this directly: the existing research is too centred on our own preliminary questions, and it missed 11 of 16 protocols including **Pleasing Gold (PGOLD)**, the third largest by market cap.

**Where the protocol work stands.** Format pilot **approved** (PGOLD, 13 headings, Aurumix relevance section retained at full length). Reconnaissance sweep **complete** across all 16, grading available documentation:

| Grade | Protocols |
|---|---|
| **RICH** (4) | PAXG, Kinesis, Matrixdock XAUm, Comtech CGO |
| **MODERATE** (3) | XAUT, VNX VNXAU, Aurus TXAU |
| **THIN** (9) | PGOLD, AZG, Streamex GLDY, MG999 Libeara, WisdomTree WTGOLD, Midas XGZ, Tenbin tGLD, DGLD, ORO |

Documentation quality tracks **regulatory anchoring, not size**: Matrixdock ($52.7M) and Comtech ($9.8M) both out-document Tether Gold ($2.49B).

**Next action on it:** run the full teardown, **Sonar Pro only, no Deep Research** (decision 2026-07-28: see §9). Per protocol: a **registry / terms-of-issue check first** (free, via WebFetch and WebSearch against the company register and the project's own terms page), then ~3 Sonar Pro queries for the 6 RICH/MODERATE, ~2 for the 9 THIN and the 3 failures, every prompt carrying the mandatory inline-URL clause. **Revised estimate ~$3–5** (down from $13–15, since Deep Research was the cost driver), ~$1.78 spent to date.

**Also outstanding on it:** the failures batch returned placeholder citations (`[AUSTRAC-releases]`, `[AU-press-SGE]`) instead of URLs. **Root cause now known and fixed** (the MCP strips the citations array: §9). Those failure profiles must be **re-run**, not patched. **Verify before quoting anything on Perth Mint.**

⚠ **Re-run scope is wider than the failures batch.** The ORO error (§6.8) shows the reconnaissance sweep inherited marketing framing on jurisdiction. **Every protocol whose jurisdiction we have asserted needs a registry check before the teardown quotes it.** Comtech is the priority: §6.14 rests on "DMCC trade licence, no VARA", which is exactly the class of claim that just failed for ORO.

- ⏭ **THEN: Phase 2 Mechanism Design, starting with B1 (Classification & Token Architecture).** Still the spine. Two new inputs feed it: the ORO problem (§6.8) and the Comtech DMCC-not-VARA path (§6.14).
- 📅 **Next client call: Wednesday.** Agenda: the four client-side open items in §7, especially the **Data Room objective** question (asked twice, never answered), plus the scope conversation owed on client additions 1–3.
- ✅ **CLOSED (was "Needs Tony"): the ORO real-yield anchor.** Re-verified against primary sources 2026-07-28. ORO is a Singapore holding company with no licence in any jurisdiction and no named issuer, so there is nothing to shore up. **Decision taken: stop hunting for a documented precedent, re-anchor on Kinesis + Ondo, and put the leasing structure to counsel as an open question.** Full detail in §6.8. Brief Tony on the outcome; no decision is owed back.

## 11. Update protocol for this doc

When context nears ~80%: append new decisions to §6, update §7 after each client call, refresh §10, bump "Last updated". Keep it tight — a living index, not an archive.
