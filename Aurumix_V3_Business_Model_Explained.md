# Aurumix V3 Business Model — Full Explanation

> Source of truth: **`client container/100 G Business_Model.docx` / `.md` (Version 3 — "100% Gold" model).**
> The V2 Master Reference (70/30 split, algo pool, company-set price formula) is **superseded** — referenced only for historical context / to explain what changed.
> Structured for mind-mapping: each top-level section = a branch, each nested item = a sub-node.
> **⚠ GAP** = open/unresolved item — these are where the tokenomics Data Room adds value.

---

## 1. The Big Idea (Root)

**One-sentence definition:** Aurumix is a *systematic gold savings programme* delivered as a blockchain token, with four bundled superpowers on top of the gold: **accumulate, borrow, earn, inherit.**

- **Accumulate** — dollar-cost-average into physical gold, gram by gram, monthly.
- **Borrow** — take credit against your gold instead of selling it.
- **Earn** — receive an annual dividend from Aurumix's operating profits.
- **Inherit** — pass gold to family automatically via an on-chain Digital Will.

**Mental model:** gold DCA + a credit line + a profit dividend + built-in inheritance, wrapped in a token. The token *is* gold — price = the gold price, nothing else.

**Positioning:** Not a stablecoin, not a gold ETF, not PAXG/XAUT. Differentiator is the **bundle** — no existing gold product offers individual on-chain allocation + SIP + native credit + dividend + family will together.

**Tagline:** *"Know It. Hold It. March."* / *"Your gold. Your family. Your legacy. Forever."*

**Jurisdiction & status:** Dubai, UAE — VARA-regulated. Document is a confidential DRAFT for legal review; must pass VARA-licensed counsel before any investor distribution.

---

## 2. Target Market & Investor Profile

- **Who:** Indian, NRI, and diaspora investors who culturally trust gold ("bought gram by gram for weddings, security, the next generation").
- **Psychographic:** Long-term saver, closer to an **LIC (insurance) subscriber than a DeFi trader.** Disciplined, patient, family-oriented. NOT crypto-native. NOT "shark"/whale investors.
- **The 3 pain points targeted:**
  1. **Liquidity pain** — traditionally you must *sell* gold to access cash (bad-day price, rebuy higher). → Solved by the credit facility.
  2. **Idle-asset pain** — physical gold generates no income while held. → Solved by the ICS Dividend.
  3. **Inheritance pain** — gold "dies with the holder": estate disputes, probate delays, unclear ownership. → Solved by Family Portfolio + Digital Will.

---

## 3. Capital Structure — The 100% Gold Model

*(Core V3 change from V2. V2 was a 70/30 split with a 30% algorithmic growth pool and a company-set price formula. All of that is GONE.)*

- **100% of every dollar buys physical gold** at the LBMA AM Fix price on the day of payment (less the entry fee). No split, no reserve pool, no algorithm.
- **Token price = (Total gold in vault × current LBMA AM Fix price) ÷ Total tokens issued.** Nothing else feeds price.
- **Independently verifiable** by any investor from the LBMA website + published vault audit at any time.
- **Custody:** LBMA-standard vaults — Brinks / Loomis / Malca-Amit, Dubai. Insured, segregated, quarterly verification, annual published audit.
- ⚠ **GAP:** single vs. multi-vault failover not specified; custody fee is a range (0.8–1.0%), exact rate depends on real cost.

---

## 4. The Individual Gold Receipt (Foundation of investor rights)

Every payment mints an **immutable, on-chain Gold Receipt** in the investor's name — a *specific* quantity of gold, not a pooled claim.

- **Contents:** Investor ID · Event # · Date · Gold purchased (grams @ LBMA fix) · Vault location / bar reference · Annual custody fee (grams) · Net grams (gross − cumulative fees) · Current value (net grams × live LBMA) · Credit capacity (value × ICS tier ratio) · ICS dividend allocation.
- **Why individual, not pooled:** legally mitigates "collective investment scheme" classification; underpins buyback and credit mechanics.

---

## 5. Token Architecture (AURX)

- **Name:** AURX — Aurumix Crypto Token / "Crusade Token" (glossary also: CTT).
- **Peg:** **1 AURX = 0.01 gram of gold** at launch. Price always = current LBMA value of 0.01g.
- **Supply:** **NO hard cap.** Grows only as fast as gold can be purchased and vaulted. (V2 had a 100B fixed cap — removed.)
- **Issuance:** Only through Mining Events. No continuous issuance, no minting beyond event-authorized purchases.
- ⚠ **GAP:** `0.01g` unit is chosen for a climbing gram counter (accessibility/psychology) but complicates comms & math — is 1 token = 1 gram cleaner? Token *standard* also unresolved (V2 discussion pointed to ERC-3643 + ERC-20 wrapper for KYC compliance; V3 doc doesn't lock it).

---

## 6. Mining Events (How tokens are issued)

**What:** a scheduled, time-bounded window — the *only* mechanism for new tokens. Requires Gold Custodian API confirmation of vault holdings before opening ("no confirmation, no event").

- **Frequency:** Monthly in Years 1–2 → **fortnightly from Year 3** onward.
- **Two-phase structure per event:**
  1. **SIP Event** — open to all confirmed SIP investors.
  2. **Spot Event** — immediately follows; open only to ICS-eligible investors; no lock-in required; **size = a ratio of the SIP event (20% / 30% / 40% — ⚠ TBD).** Oversubscription target 2–5×.
- **Three-Lane Allocation Model:**
  - **Lane 1 — SIP Lane** (stated "90% of each event"): guaranteed recurring allocation for Confirmed SIP investors. No competition; standing-order-like. Core product.
  - **Lane 2 — ICS Spot Lane** (stated "80% of each event"): genuinely scarce; preference to earned minimum ICS score; can't be bought, only earned.
  - **Lane 3 — External Spot Lane** ("20% or more"): entry point for *new* investors.
  - ⚠ **GAP (important):** percentages **don't reconcile** (90 + 80 > 100). Likely SIP-Event vs. Spot-Event measured against different denominators. Needs client clarification — core mechanism-design item.
- ⚠ **Conceptual open question:** since price is now *pure gold* (same LBMA price this event or next), the "mining scarcity / oversubscription / FOMO" framing may no longer be a real economic mechanism — now a retention/marketing device. Decision: keep heavy mining framing, or simplify to "gold DCA + tier-earned spot access."

---

## 7. The SIP Programme (Core investment vehicle)

- **Commitment:** USD **20 minimum**, USD **75 target** per investor per month, invested at each Mining Event. 100% (less entry fee) buys gold immediately.
- **Lock-in range:** 6 months → 25 years, in 3-month increments. Longer lock-in → higher ICS contribution AND higher **Dividend Multiplier**:

  | Lock-in | ICS contribution | Dividend Multiplier |
  |---|---|---|
  | 6 mo (min) | Base | 1.0× |
  | 12 mo | Moderate | 1.1× |
  | 24 mo | Strong | 1.25× |
  | 5 yr | High | 1.5× |
  | 10 yr | Very High | 1.75× |
  | 25 yr (max) | Maximum | 2.0× |

  - Credit facility activates at month 6 regardless of lock-in length; buyback available at lock-in expiry.
- **Confirmed SIP Status:** achieved after **6 consecutive events** at the same monthly commitment → allocation **protected / ring-fenced** in all future event sizing. Key milestone every new entrant works toward.
- **The Gram Counter:** primary dashboard metric = total net grams owned. Never falls between events (only the annual custody fee, shown separately, reduces it). Grams-first / dollars-second is a deliberate psychological anchor.
- ⚠ **GAPs:** Is the $75 fixed or investor-chosen each month? Does each monthly purchase start its own 6-month lock, or one lock over the whole SIP? If a Confirmed SIP investor commits an allocation but doesn't participate — where does the allocation go?

---

## 8. ICS — Investor Conviction Score (The engine that governs everything)

**What:** a cumulative, on-chain commitment score. In V3 it governs **four things at once:**
1. Allocation priority in oversubscribed events
2. Access to the ICS Spot Lane
3. Credit ratio available against the Gold Receipt
4. Weighted share of the annual ICS Dividend

- **ICS Components & weights:**
  - **Investment continuity** — *primary/dominant driver.* Accelerates with consecutive events; decays on misses; **loss faster than rebuild.**
  - **Lock-in duration** — significant; also feeds the Dividend Multiplier.
  - **SIP tenure** — significant; rewards longevity independent of continuity.
  - **Investment value (USD)** — significant; larger holding multiplies dividend entitlement.
  - **Referral network** — supplementary, **capped** (can't dominate — MLM guard).
  - **Masterclass participation** — supplementary community sub-score.
  - **Family Portfolio activity** — supplementary; active family sub-portfolios add to primary ICS.
- **Membership Tiers (7):** Green → Silver → Gold → Platinum → Titanium → Elite → Sovereign.
  - ⚠ **GAP (major):** tiers are currently *names only* — no score thresholds, no per-tier multipliers, no privilege table. Must be fully built; lots downstream (credit %, spot access, dividend share) depends on it.
- ⚠ **GAP:** the **exact ICS calculation formula** (how the 7 inputs combine) is undefined. Decay-faster-than-rebuild rule has no numbers. Weighting preferences among inputs need client steer.

---

## 9. The ICS Dividend (The headline new feature)

**Concept:** converts gold from passive storage into an income-generating asset by sharing Aurumix's *operating profit* with committed investors.

- **Pool size:** **15–20% of Aurumix total annual operating profit.**
- **Distribution formula:**
  - **ICS-Weighted Score = ICS Score × Investment Value (USD) × Dividend Multiplier** (glossary; §4.2 states ICS × Investment Value, glossary adds the multiplier).
  - Investor's dividend = (their ICS-Weighted Score ÷ total of all investors') × pool.
- **The 80/20 concentration rule:**
  - **Top 10%** by ICS-weighted score take **80%** of the pool.
  - Remaining **90%** share the other **20%.**
  - Lapsed/inactive (ICS below threshold): **0%** — resumes when SIP reinstated and ICS rebuilds.
- **Payment:** annually, in USDT *or* credited as additional gold grams to the next SIP (compounding option).
- **Retention logic:** "Lock-in prevents exit by contract; the dividend prevents exit by economics." Exiting starts ICS decay → shrinks dividend → turns lock-in expiry into a *renewal moment.*
- **Family interaction:** dividend attributable to a sub-portfolio accrues to that family member — even *before* a Digital Will trigger fires. Inheritance starts earning for the family from designation, not death.
- ⚠ **GAP / sharpest strategic question:** with no external yield source, the dividend is paid *from the fees investors themselves pay* (entry + custody + credit), then concentrated 80% into the top 10%. **Is this genuine value creation, or investors' own fees recycled and redistributed upward?** Needs careful thought — both an economic-sustainability and a VARA-classification question (profit-share vs. collective investment scheme).

---

## 10. The Credit Facility & Gold Card

**Core promise:** "You never have to sell your gold again." Borrow against it; gold stays vaulted, keeps growing, keeps earning dividend.

- **Activation:** after 6 consecutive SIP events.
- **Flow:** (1) collateral registration → (2) credit request in USDT via app (auto-checks limit, lock-in, ICS tier; **no credit check — gold is the only qualification**) → (3) USDT disbursed in minutes → (4) backing grams flagged *pledged/encumbered* (nothing physically moves) → (5) repay in USDT → pledge released.
- **Credit Ratio by ICS tier:**
  - Gold Member — **50%** of gold value
  - Platinum — **70%**
  - Sovereign — **up to 110%**
- **Risk engine:** live LTV; **warning at 80%**, **auto-liquidation at 100%.**
- **Sub-portfolio credit:** each family sub-portfolio has its *own independent* credit line based on its own gold + its own ICS sub-score.
- **The Gold Card:** Visa/Mastercard via a UAE-licensed card programme partner; limit = available credit; works internationally (India, SE Asia, ME). Family members above Gold tier get their own card.
- ⚠ **GAPs:** (1) **Sovereign 110% lends more than the collateral is worth** — unusual; needs a loss-absorbing sink / rationale. (2) Revolving (card-like) or fixed-term? Repayment deadline? (3) Full risk engine (LTV bands, liquidation waterfall, credit types, lending-partner terms) to be designed. (4) Credit facility fee "TBD with lending partner." (5) Does *pledged* gold still earn ICS + dividend while encumbered?

---

## 11. Family Portfolio & Digital Will (The inheritance system)

**Why:** gold is culturally a *family* asset; traditional transfer is manual, dispute-prone, probate-delayed.

- **Family Portfolio structure:**
  - Primary account holds the master Gold Receipt and controls all designations.
  - Split into named **sub-portfolios** (spouse, child 1, child 2…), each a % of the master. Total ≤ 100%.
  - Each sub-portfolio has its **own** dashboard, ICS sub-score (proportional to primary's continuity), credit facility, dividend entitlement, and can have its own independent lock-in.
  - Changeable by primary anytime *until* Will lock-in.
- **Family Dashboard:** each family member gets their own Aurumix Circle login showing *their* grams/value/credit/dividend — view-only; cannot change structure or Will.
- **The Digital Will** (on-chain transfer instruction set — *explicitly NOT a legal will*):
  - **Beneficiary** (must be/become KYC-verified).
  - **Trigger type:** (a) date-based, (b) event-based (e.g., death, confirmed by nominated executor + Aurumix compliance), (c) condition-based (e.g., beneficiary completes 12 SIP events).
  - **Transfer type:** full / phased (tranches over time) / income-only (dividend transfers, principal later).
  - **Continuation instruction** (SIP contributions after transfer) + **modification rights.**
  - **Will Lock-In:** optional voluntary irrevocability.
- **Trigger execution:** detect → beneficiary verification (30-day KYC window) → on-chain re-registration of Gold Receipt, credit + ICS recalculated → dashboard updates → SIP/dividend continuation per instruction.
- **Worked scenarios:** Retirement Plan (spouse + 2 kids, phased) · Education Fund (child, phased at 18/25, dashboard at 16) · Business Partner (cross-designated mutual-accountability triggers).
- ⚠ **GAPs / legal:** on-chain instructions aren't valid wills in any jurisdiction; must be positioned as a "financial transfer instruction layer," investors advised to keep a real will; cross-border transfer tax, minor-beneficiary protection, death-confirmation disputes all need jurisdiction-specific legal review.

---

## 12. Buyback / Redemption

*(Restores a redemption right that V2 explicitly denied — big improvement.)*

- **Eligible:** any investor past lock-in expiry.
- **Calc:** net grams (after custody fees) × LBMA AM Fix on redemption date.
- **Funding:** liquidation of *exactly those grams* from the vault — nothing borrowed from other investors, nothing dependent on inflows. **Zero impact on other investors.**
- **Settlement:** 5–10 business days, in USDT or AED.
- Makes the token's **floor** real and self-funding.

---

## 13. Secondary Market

- **When:** token lists on exchanges (~Year 2 per our summary; doc says "once listed").
- **Floor:** every token's buyback value (Gold Receipt) — rational buyers won't pay below it because Aurumix stands ready to buy back at floor.
- **Why a modest premium may exist (3–8% "natural," NOT promised):** (1) credit facility travels with the token; (2) ICS dividend entitlement begins accruing for registered buyers; (3) buying secondary skips the SIP queue.
- ⚠ **Compliance hard rule:** no investor-facing material may characterize any premium as a return/projection; all secondary-market references need legal review.
- ⚠ **GAP:** DEX vs CEX liquidity strategy, depth requirements, slippage/anti-whale rules, market-making — none specified. (Tony's biggest call concern: thin pools where small sell pressure erases large market cap.)

---

## 14. Fees & Revenue Model (How Aurumix earns)

| Fee | Rate | Applied to | Timing |
|---|---|---|---|
| **Entry fee** | 2–5% | Every SIP payment | At point of investment |
| **Annual gold custody fee** | 0.8–1.0% p.a. | Gold holding value | Annual, **deducted in grams** from the Gold Receipt |
| **Credit facility fee** | TBD w/ lending partner | Outstanding drawn balance | Monthly on drawn amount |
| **Gold Card income** | (card interchange/fees) | — | ongoing |

- **Revenue lines:** entry fees + custody fees + credit fees + card income.
- **Gives back:** 15–20% of *operating profit* → ICS Dividend.
- ⚠ **GAP:** Custody fee should **accrue daily (1%/365 on that day's grams) and settle at anniversary/transfer/redemption**, not on a snapshot. Cohort-level fee-revenue curve (500 → 100k investors) needs modeling.

---

## 15. Distribution — Agent Network

- **Primary channel:** a **3-tier agent network** (relationship-based onboarding for NRI/diaspora).
  - **L1 Principal Agent** (appointed by Aurumix) → **L2 Sub-Agent** (appointed by L1) → **L3 Associate Agent** (appointed by L2, cannot appoint further).
  - **Hard-capped at 3 levels, smart-contract enforced** — deliberate anti-MLM design.
- **Commission:** paid **from Aurumix's fee revenue**, never an extra charge to investors. L1 largest share, L3 smallest.
- ⚠ **GAP:** exact commission % and the split across levels **undefined in V3** (V2 had a 15%-of-platform-fee model; V3 dropped the numbers). Consider tying commission to investor value brought / taking it from the initial fee rather than the whole revenue line.

---

## 16. International Access & KYC Routes

| Investor type | KYC route | Funding | Regulatory position |
|---|---|---|---|
| UAE resident | Direct — Emirates ID + passport | AED or USDT | Fully within VARA |
| NRI (Indian abroad) | Direct — Indian passport + foreign address | USDT / foreign bank | Clean — not FEMA-subject as non-resident |
| Indian resident | Agent-assisted — passport + Indian address | USDT via P2P/OTC | Investor bears Indian tax disclosure |
| Other international | Direct — national passport | USDT / bank transfer | VARA AML/CFT; FATF Travel Rule > $1,000 |

- ⚠ Fiat on/off-ramp enabling (vs. USDT-only) flagged as a "rabbit hole" — plausible with licensed on/off-ramp partners.

---

## 17. Community Layer

- **Aurumix Masterclass:** financial-education + community programme (gold, inflation, how the model works). *Not* investment advice. Attendance feeds a modest ICS Community-Engagement sub-score → flywheel (education → conviction → consistency → higher tier → better allocation).
- **Aurumix Circle app:** daily emotional touchpoint — gram counter, value, custody fee, credit capacity, ICS score/tier, dividend entitlement, SIP streak, family portfolio, Digital Will, event countdown, community milestones. Distinct primary-investor vs. family-member views.
- **Community Milestones:** public total-gold goals (10kg → 50kg → 100kg → 500kg → 1 tonne+). Active investors at a crossing get a permanent record ("a story, not just a balance").

---

## 18. Technology Architecture

- **Five layers:**
  - **L5 Investor Interface** — Circle app · Family Dashboard · Masterclass Portal · Gold Card App · Digital Will Creator · Strategy Bot.
  - **L4 Core Platform** — ICS Scoring Engine · Dividend Calculator · SIP Payment Gateway · KYC/AML Engine · Family KYC Manager · Agent Portal · Notification Engine.
  - **L3 Financial Engine** — Gold Purchase Engine · Credit Collateral Manager · Token Allocation Engine · Event Scheduler · Fee Calculator · Dividend Pool Manager · Family Transfer Engine.
  - **L2 Blockchain Core** — the 9 smart contracts (below).
  - **L1 External Integrations** — Gold Custodian API (LBMA) · Live Gold Price Oracle (Chainlink) · Card Programme Partner API · VARA RegTech · FIU-IND Reporting (Phase 2) · Legal Will Integration Partner.
- **Nine Core Smart Contracts:** AURX Token · Mining Event · 100% Gold Split · Lock/Vesting · Credit Collateral · Fee Collection · **ICS Dividend** · **Family Portfolio** · **Digital Will.** (V2 had 6; the 3 new = Dividend, Family, Will.)
- **Audit:** Tier-1 (CertiK/Halborn) mandatory pre-launch; **min USD 75,000** budget for the 9-contract scope; Digital Will + Family contracts need extra legal review.

---

## 19. VARA Regulatory Framework

Structured for VARA compliance from inception. Key areas & positions:
- **Token classification** — 100% gold strengthens "commodity-linked"; the dividend adds a profit-share element needing separate determination.
- **ICS Dividend** — ⚠ **highest-priority legal item**: may be a collective investment / securities activity; must get explicit VARA classification before it's even *described* to investors.
- **AML/CFT** — Sumsub/Jumio KYC; family sub-portfolio KYC for all credit-eligible members; Notabene for Travel Rule > $1,000; ongoing PEP/sanctions screening.
- **Gold custody** — LBMA-accredited; proof of reserve; quarterly verification; annual published audit.
- **Digital Will / family transfer** — not a legal will; must not be marketed as estate planning; per-market legal review.
- **Buyback/redemption** — individual Gold Receipt basis mitigates CIS classification; legal determination mandatory.
- **Credit/lending** — needs UAE-licensed lending partner or own licence.
- **Advertising** — no return projections, no dividend-amount projections, no secondary-market price expectations; all materials legal-reviewed.

---

## 20. Founder Parity (The trust signal)

Founders invest at the **same price, same conditions** as everyone — no free tokens, no discounted allocation, no promotional reserve. Only advantage is being early (lower gold price at earlier events), available to all. Founders participate in the dividend on identical ICS-weighted terms. Positioned as the single strongest trust differentiator (contrasts with OHM/LUNA-style founder-allocation collapses).

---

## 21. Risk Factors (Doc's own honest register)

Gold price risk · Dividend variability (profit-dependent) · Liquidation risk (LTV auto-liquidation) · Digital Will execution risk (trigger confirmation delays) · Family sub-portfolio risk (primary stops SIP → all sub-scores decay) · Custodian counterparty risk · Smart-contract risk · Regulatory risk (VARA classification of dividend/will). Each has a stated structural mitigation; a full Risk Disclosure doc must come from VARA counsel.

---

## 22. Growth Targets

| Horizon | Active SIP investors |
|---|---|
| Year 1 | 500 |
| Year 3 | 10,000–14,000 |
| Year 10 | 60,000–100,000 |

At $75/mo target. No hard token cap — supply scales with gold purchased.

---

## 23. The Open-Questions Map (where WE add value)

- **Mechanism must-close (before any modeling):** ICS exact formula + input weights · tier thresholds & multipliers (7 tiers) · three-lane % reconciliation · Spot ratio (20/30/40) · confirmed-SIP allocation-failure handling · ICS decay-vs-rebuild rule · lock-in unit (per-payment vs whole-SIP).
- **Credit/risk engine:** revolving vs term · repayment terms · full LTV/liquidation design · Sovereign 110% over-collateral sink · does pledged gold still earn ICS/dividend.
- **Economic sustainability (the big one):** is the dividend real value or recycled fees concentrated to the top 10%? · does limiting oversubscription cap AUM growth? · custody fee daily-accrual treatment · cohort fee-revenue curve.
- **Legal/architecture:** token standard choice · AURX VARA classification · dividend classification (CIS/securities?) · Digital Will cross-border validity · lending licence/partner · agent commission % & split.
- **Comms/design:** keep heavy "mining" framing or simplify? · 0.01g vs 1g token unit.

---

## 24. How This Maps to the 7-Phase Data Room (our value delivery)

- **Phase 0 Discovery** → resolve the open-questions map above into a signed project charter; note the Engagement Brief still describes V2 and needs re-scoping to V3.
- **Phase 1 Market Research** → benchmark vs PAXG, XAUT, Kinesis KAU, digital-gold apps; the silver-tokenization comparable; gold-token liquidity-drain failure modes.
- **Phase 2 Mechanism Design** → close every ⚠ GAP: build the ICS formula, tier tables, dividend math, credit/LTV engine, lane structure, Digital Will state machine.
- **Phase 3 Revenue Model** → deterministic fee-revenue model (entry + custody-in-grams + credit + card) and the dividend pool it funds, cohort-by-cohort, 500 → 100k.
- **Phase 4 Simulation** → GBM gold price; Monte Carlo investor growth; custody-fee gram erosion; credit liquidation cascades under gold drawdowns; dividend concentration dynamics; buyback stress; does the dividend hold up as fees vs. redistribution.
- **Phase 5 Supply Side** → supply is uncapped and gold-driven; model circulating supply, lock-pledged-free float, and DEX/CEX liquidity depth vs. that float (Tony's slippage concern).
- **Phase 6 Documentation** → whitepaper, process maps (SIP flow, 100%-gold flow, credit, Digital Will, agent network, event execution), tokenomics audit, VARA-ready compliance posture.

---

## The 3 Highest-Leverage Nodes for Our Value

1. Build out the undefined **ICS + tier + dividend math**.
2. Design the full **credit/LTV risk engine** (esp. the 110% Sovereign anomaly).
3. Pressure-test whether the **ICS Dividend is genuine value or recycled fees** — it drives both the economic model *and* the VARA classification.
