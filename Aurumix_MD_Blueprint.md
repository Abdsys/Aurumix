# Aurumix — Mechanism Design Build Blueprint

> A product-style, decision-driven blueprint for building the Aurumix Mechanism Design (MD) doc — the highest-value deliverable of this engagement. Market Research feeds MD; MD is built near-perfect as an ordered sequence of questions we answer together (raise → reason → decide → log → move on). Full latitude to redesign with reasoning. Layered output (dev + investor + VARA). Legal *opinion* is the one thing we don't produce — we tee it up for the client's counsel.

---

## The operating philosophy (read once)

- **Treat it like building a product, not writing a report.** Every section exists to make a *decision* the dev team, investors, or VARA counsel can act on.
- **We fill every knowledge gap except the legal opinion.** For anything legal, we produce the *structural recommendation + the exact questions for their counsel* — we don't opine on the law.
- **Dependency order beats document order.** Resolve mechanisms in the order later decisions depend on earlier ones. You can't calibrate a formula before fixing its variables; you can't design the token before fixing what it legally *is*.
- **Market Research is ammunition, not a detour.** Every MR finding must convert into a design input for MD. If a finding doesn't change an MD decision, we don't spend time on it.

## The Working Loop (repeat for every open question)

1. **Frame** — state the question precisely and *why it matters* / what it gates downstream.
2. **Reason** — options, trade-offs, and the **precedent** from Market Research (how PAXG / XAUT / Kinesis / Dubai-RE / silver-token solved it).
3. **Decide** — pick, with explicit rationale. If it needs the client, mark **[FRIDAY]** and set a *recommended default* so we don't stall.
4. **Ripple-check** — what else does this touch? (peg, classification, ICS, dividend, revenue). Update those.
5. **Log** — write it into the **Decision Log**. The log *becomes* the MD skeleton — we draft the doc as we go.

## The chronology at a glance (the spine)

```
PHASE A — MARKET RESEARCH  (precedent + stress-test bank)
      │  feeds ↓
PHASE B — MECHANISM DESIGN  (dependency-ordered blocks)
   B1  Classification & Token Architecture   ← the spine; gates everything
   B2  Asset Engine: gold, receipt, pricing, custody-fee, buyback
   B3  Issuance Engine: mining events, lanes, allocation, supply
   B4  ICS Scoring Engine
   B5  Reward Layer: ICS Dividend + real revenue sources
   B6  Credit Engine: LTV, liquidation, Gold Card
   B7  Family Layer: sub-portfolios + Digital Will
   B8  Distribution: agent network economics
   B9  Secondary Market & Liquidity
   B10 Integration: invariants, edge cases, attack surface
      │  feeds ↓
PHASE C — HANDOFF  (Revenue Model → Simulation → Supply-Side → Whitepaper)
```

**Rule of the spine:** B1 must be provisionally locked before B2–B9 can be trusted, because classification decides token architecture, which decides what each later mechanism is allowed to do.

---

## PHASE A — MARKET RESEARCH (the preceding step)

Purpose: build a **precedent bank** and a **failure-mode catalogue** so every MD decision is anchored in "here's how comparable regulated products actually did it." Six tracks, each ending in a one-line *"→ implication for Aurumix."*

- **A1 — Regulatory & classification precedent.** How gold/RWA tokens are classified and structured in the UAE and globally (PAXG, Tether Gold, Kinesis, Comtech, Dubai tokenized real estate). → feeds **B1**.
- **A2 — Gold-token mechanics precedent.** Custody-fee handling (peg preservation), redemption, oracle design, proof-of-reserve, secondary premium. → feeds **B2, B9**.
- **A3 — Yield / profit-share precedent (security-risk track).** How yield-bearing / profit-share token models are treated, and how compliant ones deliver reward without making the token a security. → feeds **B1, B5**.
- **A4 — Gold-backed credit precedent.** NBFC gold loans, the prior silver-token credit facility, DeFi collateralized lending — LTV norms, liquidation, over-collateral handling. → feeds **B6**.
- **A5 — Failure modes.** Terra/Luna (the "what we're not" story), gold-token liquidity drains, over-collateralized lending blowups, MLM traps. → feeds **B10** + simulation.
- **A6 — Investor-behaviour evidence.** LIC/SIP behaviour, gold-saver retention, DCA cohorts, diaspora demand. → feeds revenue model + simulation.

**MR deliverable:** the market research doc **+ a "precedent → Aurumix implication" matrix** listing which MD block each finding unlocks. That matrix bridges into Phase B.

---

## PHASE B — MECHANISM DESIGN (the core, near-perfect)

Each block is a set of **ordered questions** run through the Working Loop. **[FRIDAY]** = needs client answer (build proceeds on a recommended default until then). **[LEGAL]** = we produce a recommendation + a question for counsel, not a final legal answer.

### B1 — Classification & Token Architecture (the spine)
*Why first: misclassification forces a full rebuild. This block is the "constitution" every later block must obey.*
1. What does one token legally represent — pure gold, or gold + bundled rights? **[LEGAL]**
2. Does the **ICS Dividend** ride on the token or attach to the KYC'd account off-token? (decides ARVA vs security/hybrid) **[LEGAL][FRIDAY]**
3. Does the **credit facility** sit on-chain or via a licensed lending partner? **[LEGAL]**
4. Target classification = **ARVA under VARA** — what must be true to hold that? **[LEGAL]**
5. Token standard & transfer model (permissioned ERC-3643 base + ERC-20 wrapper? KYC gating? what rights survive a DEX transfer?).
6. Peg unit: **1 token = 1 g vs 0.01 g** **[FRIDAY]**.
*Output:* the token "constitution." Everything downstream inherits this.

### B2 — Asset Engine (gold, receipt, pricing, custody fee, buyback)
1. Gold purchase flow — 100% at LBMA fix, timing, batching, oracle/fallback.
2. Gold Receipt data model (what's recorded, attribution, transfer behaviour).
3. Token pricing = gold; how the peg is held exactly.
4. **Custody fee model** — resolve *keep-the-peg*: charge in cash from SIP inflow + at gates, **not** eroding grams. Daily-accrue, periodic cash settle. (Conclusion already reached; document + calibrate.)
5. Buyback/redemption mechanics (eligibility, funding from own grams, settlement, reserve/redemption obligations from ARVA rulebook).
6. Proof-of-custody gate ("no confirmation, no event") + failure handling.
*Output:* fully specified asset layer + reserve/redemption obligations.

### B3 — Issuance Engine (mining events, lanes, allocation, supply)
1. SIP config — amount fixed vs variable; lock-in unit (per-payment vs whole-SIP) **[FRIDAY]**.
2. Mining Event structure — SIP Event + Spot Event; frequency.
3. **Three-lane model — reconcile the percentages** (the 90/80/20 that can't sum) **[FRIDAY]**.
4. Confirmed SIP status logic + protected-allocation math.
5. Allocation algorithm — how tokens are apportioned (priority weighting).
6. **Strategic: what does "mining/oversubscription" mean now** that price = pure gold? Keep the framing or simplify to "gold DCA + tier-earned spot"? **[FRIDAY]**.
7. Supply dynamics — uncapped, gold-governed; what caps growth and why.
*Output:* the issuance mechanism.

### B4 — ICS Scoring Engine
1. Exact ICS formula — how the 7 inputs (continuity, lock-in, tenure, value, referrals, Masterclass, family) combine **[FRIDAY: weighting preference]**.
2. Continuity decay vs rebuild rule (numbers) **[FRIDAY]**.
3. Tier thresholds + multipliers for all **7 tiers** (currently names only).
4. Spot-lane eligibility gate — same as Confirmed SIP, or a higher ICS threshold? **[FRIDAY]**.
*Output:* the scoring model — feeds allocation (B3), credit (B6), dividend (B5).

### B5 — Reward Layer (ICS Dividend + real revenue)
1. **Value-source problem** — is the dividend real value or recycled fees concentrated to the top 10%? Resolve by identifying/designing genuine revenue streams (credit spread, card interchange, spot, custody margin) so the dividend is funded by margin, not redistribution **[FRIDAY: appetite for new streams]**.
2. Dividend formula + the **80/20 concentration** — keep, soften, or re-curve?
3. **Lock-in double-count** (ICS component *and* Dividend Multiplier) — intentional super-weight or fix to one channel?
4. On-token vs off-token delivery (inherits B1) **[LEGAL]**.
*Output:* dividend mechanism + the revenue lines that fund it (hands into Revenue Model).

### B6 — Credit Engine (LTV, liquidation, Gold Card)
1. Revolving vs fixed-term; repayment terms.
2. LTV by tier, warning/liquidation thresholds, liquidation waterfall.
3. **Sovereign 110% over-collateral** — where's the loss-absorbing sink? **[FRIDAY on intent]**.
4. Does pledged gold still earn ICS/dividend while encumbered? **[FRIDAY]**.
5. Delivery — licensed lending partner / country-layer (India NBFC/UPI etc.) **[LEGAL]**.
*Output:* the credit risk engine.

### B7 — Family Layer (sub-portfolios + Digital Will)
1. Sub-portfolio mechanics (allocation, independent ICS/credit/dividend, lock-ins).
2. Digital Will triggers, transfer types, KYC-of-beneficiary flow.
3. Legal positioning (financial-transfer-layer, not a legal will) **[LEGAL]**.
*Output:* family system spec.

### B8 — Distribution (agent network)
1. Commission % and the 3-level split **[FRIDAY]**.
2. Anti-MLM structure (depth cap, subordinate-to-investment) **[LEGAL]**.
3. Licensed-distributor positioning.
*Output:* agent economics (also a revenue-model input).

### B9 — Secondary Market & Liquidity
1. DEX vs CEX strategy; free-float sizing (locked + pledged + spot).
2. Slippage / anti-whale rules; launch liquidity budget.
3. Premium framing — compliance guardrails (no return language).
*Output:* secondary-market design.

### B10 — Integration, Invariants & Edge Cases
1. **System invariants** — reserves ≥ claims; peg holds exactly; custody fee never breaks peg; dividend never paid from principal; issued tokens always gold-backed at event.
2. Cross-mechanism interactions (credit draw ↔ ICS; dividend-in-grams ↔ supply).
3. Edge cases + attack vectors (whale gaming, streak gaming, will-trigger disputes, oracle failure).
4. **Simulation handoff spec** — the closed mechanism + the scenarios the sim must test.
*Output:* a closed, internally consistent, build-ready mechanism.

**Layered documentation (every block):** each mechanism written in three registers — **spec** (formulas/thresholds/state machines for dev), **narrative** (plain-language rationale for investors), **compliance** (classification + VARA/counsel questions).

---

## The Decision Log (the artifact that becomes the MD)

| # | Block | Question | Decision | Rationale | Precedent | Depends on | Status |
|---|---|---|---|---|---|---|---|

Every loop appends a row. When complete, the log *is* the MD backbone — nothing undocumented or unjustified.

## Friday-call dependency map (make the call efficient)

One crisp agenda: dividend on/off-token intent (B1/B5) · peg unit (B1) · SIP amount + lock unit (B3) · three-lane %s + mining-framing decision (B3) · ICS weighting + decay + spot gate (B4) · new-revenue appetite (B5) · Sovereign-110% intent + pledged-gold-earns (B6) · agent split (B8). Everything else: pre-decide with recommended defaults, mark for confirmation.

## PHASE C — What MD feeds (the downstream, in one glance)

MD closes → **Revenue Model** (margin lines from B5/B6/B8) → **Simulation** (B10 scenarios, gold GBM, cohort dividend, credit liquidation, buyback stress) → **Supply-Side** (uncapped gold-governed emission + float from B9) → **Whitepaper** (layered narrative already written per-block).

---

## How to use this blueprint

Start at **Phase A**. When MR is banked, walk **B1 → B10** through the Working Loop, one question at a time, deciding and logging as we go — the "raise it, answer it together, move on" rhythm. B1 first and hard, because it's the spine.
