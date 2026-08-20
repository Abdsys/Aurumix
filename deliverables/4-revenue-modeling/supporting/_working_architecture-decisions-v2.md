# Revenue Model Architecture — v1.0 → v2.0 decision record

**Date:** 2026-08-18
**Purpose:** the complete list of architecture changes between brief v1.0 (2026-08-17, commit `668e0d5`) and v2.0. Every change carries the finding that forced it and the source of that finding. This is the working record; the brief itself carries the conclusions.

**Sources of findings:**
- `AUDIT-A` — arithmetic reconciliation, Python-verified
- `AUDIT-C` — corpus fidelity check against the Phase 2 drafts
- `AUDIT-M` — adversarial structural critique
- `AUDIT-D` — benchmark against `DRODE_Revenue_Model_Architecture_Brief_V2.1.md` and the built workbook
- `AUDIT-B` — buildability test
- `EXTRACT` — `_working_corpus-omissions-extract.md`
- `PARAMS` — `_working_parameter-completion-set.md`

---

## Tier 1 — changes that alter the model's structure

### D1. The population state machine goes from three states to six

**v1.0:** `CONTRIBUTING → REDUCED → LAPSED`, LAPSED terminal.

**Why it fails.** A lapsed account keeps its gold. It holds a permanent ICS floor of 25 (`_draft_ics-scoring.md` §1.6 — "once you have made six payments, your score never falls below 25"), stays in the AUM stock, the custody-cost base, the B2B AUM base and the collateral base, and stays in continuous AML screening at USD 0.36/name/year indefinitely. At the corrected persistency roughly **81% of every cohort sits in this "terminal" state by M61.** v1.0 models the economics of the other 19%. (`AUDIT-M` F1)

**v2.0 states**, per `EXTRACT` item 2, which recovers them from `_draft_sip-rulebook.md` §8:

| State | Trigger | Gold | Clocks | Contributes | In AUM |
|---|---|---|---|---|---|
| `PRE-GATE` | run length 0–6, gate not yet passed | Held | Run counter only, no score | Yes | Yes |
| `CONTRIBUTING` | gate passed, paying | Held | Both advance | Yes | Yes |
| `REDUCED` | contribution cut, free and unscored | Held | Both advance | Yes, at reduced ticket | Yes |
| `REGULATORY BLOCK` | compliance blocks the account | Held | **Both frozen; window extends** | No | Yes |
| `STOPPED` | investor cancels | Held | `Recent` decays, `Months` held | No | **Yes** |
| `DORMANT` | **12 consecutive silent periods**, SIP auto-cancels | Held | `Recent` decayed then held | No | **Yes** |
| `CLOSED` | grams = 0 | None | — | No | No |

`CLOSED` is the only true absorbing state and the only exit from AUM, custody and screening.

**Consequences to build:**
- A `holding_not_contributing` population that feeds AUM but not contribution flow. This **understates nothing and understates streams 2, 4, 5 and 6 in v1.0.**
- A hard absorbing boundary at 12 silent periods — no account may decay through it. The single-hazard engine cannot express this.
- A restart rate from `DORMANT`/`STOPPED` back to `CONTRIBUTING`, resuming at the decayed score. "Restarting is never a reset."
- Split the hazard into voluntary and involuntary. Corpus: **involuntary is 20–40% of total churn**, base 30% (`_draft_sip-rulebook.md` §7.3).

**🔴 Open client question this creates:** *does a lapsed customer keep the card and the facility?* Nobody has decided. It determines whether 54% of revenue decays with persistency or is immune to it. v1.0 silently assumes immunity by never asking. Model as switch `LAPSED_KEEPS_CARD`, report both.

**Do NOT fold in** (`EXTRACT` item 2, stale-mechanics warning): continuity-halving, arrears, revival, and "Tenure" as a score component are all **dead** per decisions 46/46a. `_draft_sip-rulebook.md` §7.1 rows 4–5 are audit trail, not spec.

---

### D2. Tier distribution is computed from behavioural archetypes, not from cohort averages

**v1.0's proudest claim — "tier distribution is an output, never an assumption" — is false as specified.** (`AUDIT-M` F2)

ICS is `MAX(25, MIN(Record, Standing) × Retention)` followed by a **threshold lookup** at 25/50/75/100. Tier is a non-linear step function of an *individual's* history. v1.0's row map (§10.1 rows 152–190) computes one set of values per segment-cohort — i.e. the cohort's *average* `Recent` and *average* `Sold`, thresholded. By Jensen's inequality that is wrong, and biased upward.

Worked: a cohort half perfect payers (`Recent`=12), half alternating (`Recent`=6). Average-then-threshold gives mean `Recent` 9 → Standing 75 → **100% Platinum**. Threshold-then-average gives **50% Platinum, 50% Gold-capped-for-life**. v1.0's own text names the alternating misser as "a real, permanently occupied cell in the distribution" and then specifies a structure with no cell to put it in.

Worst where the money is: Sovereign requires `Record 100 AND Recent 12 AND Sold ≤ 30%` **simultaneously, monthly**. A cohort average cannot represent a joint distribution. So v1.0's T5 (Sovereign share, 8% at Y10) sits in the assumptions register as an **input**, flatly contradicting T4's own note.

**v2.0:** five payment archetypes per `PARAMS` B1, each with its own deterministic ICS path, crossed with a withdrawal split straddling the 30% Retention kink. Tier distribution is the weighted sum over archetype tracks — genuinely computed.

| Archetype | Weight | Monthly pay prob. | Terminal tier |
|---|---|---|---|
| Perfect payer | 10% | 0.995 | Sovereign-capable — the only one |
| Occasional misser | 35% | 0.93 | Platinum ceiling |
| Alternating misser | 12% | 0.55 | **Gold, capped for life** |
| Reducer | 13% | 0.97 at reduced ticket | By payment record |
| Early lapser | 30% | 0.60 falling | Silver floor / never gated |

Rejected: Monte Carlo — wrong deliverable for a client Excel workbook, unauditable, and unnecessary once archetypes are discrete and deterministic.

---

### D3. Survival emerges from heterogeneity — and needs a background hazard

**v1.0:** `h = 1 − S13^(1/13)`, a single constant hazard.

**Two defects.** The exponent is wrong — an M13 survival figure spans **12** hazard opportunities, so the root is 1/12. v1.0 §1 says 1/12 and §10.2 says 1/13; they contradict each other. Worse, **a constant hazard cannot fit a five-point convex-declining curve**: it delivers **6.1% survival at M61 against the brief's own recommended 19%**, destroying two-thirds of the terminal book. Everything v1.0 says about LTV, referral payback, Sovereign counts and terminal revenue is computed off the §0.5 curve, and its own formula does not produce that curve. (`AUDIT-B` G6)

**v2.0:** survival is emergent from the archetype mix — early lapsers leave first, survivors are selected, so aggregate hazard declines with tenure without being told to. This is the standard mover-stayer result and it is structurally right rather than a curve-fit.

**But a pure mixture is not enough, and this is a finding in its own right.** (`PARAMS` B1) A best-fit pure archetype mixture lands at **36% at M61 against a 19% target** — heterogeneity alone produces a tail that is far too fat. Reproducing the curve requires a **common background hazard** applied across all archetypes: voluntary exit unrelated to payment ability. Which means:

> **Roughly half of terminal attrition is people who could pay and chose not to.** The corpus's implicit assumption — that lapse is a payment-failure phenomenon, addressable by better rails and nudges — is wrong. This reprices the value of the rail investment and of the involuntary-churn mitigations.

Calibrated Base mix reproduces the anchors to under 1pp at all five points. Calibration order (levers near-orthogonal in this sequence): early-lapser weight sets M13 → background hazard sets M49/M61 → perfect-payer weight trims M37.

---

### D4. The ICS engine gains a pre-gate block, and gate arrival becomes a distribution

**v1.0:** Layer 5 starts at `Months = 6` on gate day. No pre-gate representation.

**Why it fails.** `_draft_ics-scoring.md` §1.6a requires the engine to track "the **current run length** (0–6) before the gate, not a score and not Months." Without it the engine cannot reproduce the corpus's own personas **H** (scattered payer: six real payments over three years, never six in a row — no score, no tier, ever) or **I** (late opener: nine paid months across fourteen calendar months, opens at Silver 25 exactly like a flawless month-6 saver). v1.0 §16 build step 4 already requires the persona check and **cannot pass it.** (`EXTRACT` item 4)

**The structural consequence v1.0 misses entirely.** Under v1.0 everyone surviving to month 6 is Silver at month 6. Under the real rule a member who misses month 4 does not gate until month 9 at the earliest. **Gate arrival is a distribution, not a date** — a run-of-6 first-passage problem in the monthly payment probability. This shifts *every* downstream ladder date right: Gold at M12+, card eligibility, credit eligibility, Sovereign at M61+. The model must compute the distribution, not assume the date.

**Two new populations v1.0 has no cell for:**
- **Never-gated (persona H).** Pays the **full undiscounted entry fee**, holds gold, generates AUM and custody cost, and consumes **zero benefits, forever.** Structurally the **highest-margin retail accounts in the book.** v1.0 understates stream 1 margin and overstates benefit cost by omitting them.
- **The zero-benefit paying window.** Months 1–5 pay full fee and receive nothing, longer if the run breaks. Report months of full-fee revenue per cohort before the first discount is outstanding.

**Asymmetry to reproduce:** "pre-run gold counts in Retention's denominator, while pre-run payments score nothing." Grams bought before the gate enter Retention's denominator, so selling them later costs score those purchases never earned.

**Also:** use **exact fractions** (`100/24`, `100/12`), not the rounded decimals. `8.3333 × 6 = 49.9998` falls below the Gold threshold of 50 and silently misfiles the entire alternating-misser population into Silver. (`AUDIT-B` G21)

---

### D5. Regulatory block re-indexes both clocks

`_draft_ics-scoring.md` §1.9 and §10 sub-decision 3 (settled): "**Frozen months are skipped entirely and the window extends to reach twelve countable months** … on both clocks and on both sides of the gate."

This is **not pause-and-resume, it is re-indexing.** `Months` and `Recent` advance on *countable* months only; the trailing window looks back until it has accumulated 12 countable months, however many calendar months that spans. Applies pre-gate too: a saver at 4-of-6 entering a pause resumes at 4-of-6.

**Materially an S5 (India) input** — the block fires on the returning-NRI event. Needs a repatriation rate; nothing in the corpus sizes it.

**🔴 Open decision, live, as a switch.** `_draft_ics-scoring.md` §10 sub-decision 2, left open at Abdur's instruction 2026-08-13: a compliance-forced exit drives Retention to zero for something the customer did not choose. OFF (current design) strips the account to the Silver floor, destroying tier on the segment most likely to be forced out. ON preserves the tier. Model OFF as base and **report the S5 tier-distribution delta as the client's decision cost.**

---

### D6. Break-even becomes a fixed point, and the honest answer may be "no crossing exists"

**v1.0** divides Year 1 opex — sized for **500 investors** — by Year 1 margin to get **171,911 investors**. The answer is 344× the input's own scale. (`AUDIT-A` F4, `AUDIT-M` F3a)

Fitting `Opex(N) = Fixed + steps(N) + variable × N` to v1.0's own three anchors gives marginal opex of **USD 93.40/investor/year** against a maximum entry-fee margin of **USD 10.80**. The curves diverge: **no solution exists at any N.** v1.0's prose conclusion ("no, at any modelled scale") was right; the three precise numbers beside it were not.

**v2.0:** solve the genuine fixed point `revenue(N) = Opex(N)`. Where no crossing exists, **plot the two diverging curves** — a chart makes the point unanswerably and needs no solver. Report entry-fee-only and all-streams separately.

---

### D7. A cash flow, a funding view, and the float that was charged but never funded

**v1.0 has zero occurrences of cash flow, balance sheet, working capital or funding requirement** — in a model whose stated purpose is to tell the client when they make money. (`AUDIT-M` S2.1)

Four compounding problems:
1. **§0.1 charges a float cost of capital (F5, 0.49%) as a P&L cost, and the float principal is never sized or funded.** You cannot charge a cost of capital on a balance that appears on no balance sheet.
2. **T3, the bar denomination upgrade, is a capital allocation decision with no capital account** — it justifies the Year 3 upgrade as "USD 135k/yr for USD 1.2m of extra float."
3. **F15's AED 1.5m is "locked, not expensed"** — correct for the P&L, and exactly why the missing balance sheet matters.
4. **The business is loss-making for years.** Cumulative losses + float + regulatory capital **is** the fundraise, and the model does not produce it.

**v2.0 adds:** EBITDA → tax → working capital (float movement) → cumulative cash → **peak funding requirement and the month it occurs**; months-to-cash-breakeven reported separately from P&L breakeven.

**Float sizing, recovered from `_draft_allocation-and-float.md`** (`EXTRACT` item 5): `float ≥ one bar denomination + N days' trailing inflow`, two bars at launch. **All corpus float figures are stale at USD 109.31/g** — at F1 = 141.46 they become ~USD 28k (Y1), ~USD 424k (Y3), ~USD 3.5M (Y10), and the Tradeflow 1 kg launch float ~USD 285k not 220k.

**🔴 New correction — a genuine double-count.** v1.0 charges **both** the float cost of capital **and** the full dealer fabrication premium. Under **dealer-carried** float (the corpus's working launch recommendation) working capital is zero, F5 is zero and price-gap risk is the dealer's — paid for in a wider premium. Under **own float** the capital is posted and F5 and price-gap bite, but the premium is narrower. **Charging both double-counts under either regime.** Add the switch; it is not a sensitivity, it is an error.

---

## Tier 2 — changes that alter the model's conclusions

### D8. The tenure rebate is retired, and that may make solver item 1's answer zero

**v1.0 §9 solver item 6 is three errors compounded** (`EXTRACT` item 7, confirming and extending `AUDIT-C` A2):
- "Rebate room is 0.10–0.75%" — that is the **Gold Rewards** range (decision 6), a different, card-funded benefit.
- "~1.5%" — that is the **superseded, prohibited** decaying redemption fee, from a column literally headed "Old design (prohibited)". It was never a rebate size.
- **The mechanism itself is retired.** Decision 44 (2026-08-10): "the tenure rebate is retired … its job (rewarding holding) is now structural, because holding keeps R at 1.00." `_draft_purchase-structure.md` §5.2 is dated four days earlier and is audit trail.

**Take the funding relief.** Decision 44: retiring it "**halves the funding question: the entry-fee uplift now funds only the discount ladder.**" With `_draft_ics-scoring.md` §6.1 — "holding the headline at 5% may fund the entire ladder with no uplift at all" — **solver item 1's answer may be zero uplift.** That is a materially different conclusion from v1.0's framing of item 1 as its one unresolved arithmetic conflict.

**Build saving:** decision 41 makes grams fungible. **Do not build FIFO lot accounting.** No lot-level tracking needed.

### D9. Spot is a real flow, priced at the tier discount, and it is the highest-margin inflow

**v1.0 models no spot volume at all** — Layer 3 is `contributing × ticket + reduced × 20`. Yet §9 item 6 asks the model to solve against "spot margin." (`EXTRACT` item 8, `AUDIT-B` G9, `AUDIT-C` O1)

**Conflict resolved: `_draft_sip-rulebook.md` §1.1 is authoritative** on three independent grounds — it is a self-labelled correction naming what it fixes, it is six days later than `_draft_purchase-structure.md` §4.3, and decision 44 ratifies it. So **spot is priced at the account's tier discount, same as SIP**, and `_draft_purchase-structure.md` §4.1/§4.3 ("flat, top of range", "no entry-fee discount") are superseded.

Spot earns no ICS but **counts in Retention on both sides**. Critically, a spot order is one push with no mandate and **no collection-failure exposure** — so under §0.2's fixed-rail non-linearity, large spot tickets amortise `R` across a much larger base. **Spot is structurally the highest-margin inflow in the business, and it is the only inflow-linked flow that survives the adverse rail scenario.** It therefore changes the answer to v1.0's most alarming finding.

**Float invariant to test:** above roughly one bar denomination, procure directly rather than drawing the float — "a single order larger than the float would breach the backing invariant and halt minting for everyone else." At a Year 1 float of ~USD 28k, a USD 100,000 order **breaches it by 3.5×**. The two-step quote mechanism is live from launch, not a Year 3 concern.

**Related finding v1.0 and the corpus both miss:** with the price lever extended to spot (decision 44) and the time lever retired, **spot and SIP now differ on one lever, not two.** The corpus's own open item says two; it is out of date in the direction of understating the problem.

### D10. Redemption gets a driver, and its cost is on net flow only

**v1.0** has `− redeemed(t)` in the stock equation with **no driver anywhere in the assumptions register**, so the term evaluates to zero. (`AUDIT-M` S2.3)

`_draft_purchase-structure.md` §5.4 supplies the logic: "**That objection assumes gross exits drive physical sales. They do not.**" The cost of the zero-fee redemption promise is the **dealer spread on net outflow**, bounded by the float's capacity to warehouse the difference:

| Book state | Inflow | Gross exits | Net | Physical gold sold |
|---|---|---|---|---|
| Growing | 8% | 3% | +5% | **None.** Float absorbs |
| Flat | 4% | 4% | 0% | **None.** Float absorbs |
| Shrinking | 2% | 6% | −4% | Yes, on the 4% net only |
| Run | 1% | 25% | −24% | Yes, in size, at bid, into a falling market |

New P&L line: `MAX(0, −net_flow) × gold_price × dealer_two_way_spread`, **zero in every month the book grows.** Four book states become a first-class scenario axis; the Run row is a stress test.

**Two conditions v1.0 does not carry.** The §5.4 affordability argument **assumes Aurumix owns the float** — under the recommended dealer-carried launch it requires a second dealer commitment to take grams back on demand. And §5.1 leaves the spread incidence to counsel: "equal value" read as full prevailing value (Aurumix absorbs) or realisable value (customer absorbs). "**The difference is the entire two-way spread and it decides who absorbs it on every exit.**"

**Taxonomy to state once and never conflate again:** redemption (gold→cash, no fee permitted, dealer spread on net) ≠ self-custody withdrawal (gold→wallet, gas only) ≠ lapse (stops paying, balance unaffected).

### D11. Leakage must feed the ICS engine — a missing arrow that is a live bug

`Sold` is computed on grams held vs 12 months ago plus acquisitions, and **makes no distinction between redemption and self-custody withdrawal** — both hit the numerator identically. So leakage drives `Sold` → `Retention` → tier → benefit costs *and* interchange rate.

**v1.0's §8.4 dependency map shows `Leakage (S10) → AUM → streams 2,3,5,6` and omits the arrow to `Sold → Retention → tier` entirely.** Setting S10 to its Conservative 30% puts the average customer exactly at the Retention kink, which would cascade tier downgrades across the book — and nothing in v1.0 says so. (`AUDIT-M` S2.3)

Also: an aggregate leakage rate cannot produce a Retention distribution. 12% of AUM leaving could be 100% of accounts withdrawing 12% (Retention 1.000 for everyone, zero tier impact) or 12% withdrawing 100% (those accounts to the floor). **Same S10, completely different tier distribution.** Needs the withdrawal-behaviour split. (`AUDIT-B` G5)

### D12. Credit needs drawn-balance vintages by struck LTV, and turnover halves the stream

`_draft_credit-and-card-infrastructure.md` §6.4: an annual facility review re-strikes the limit to the current tier, but **existing drawn balances run to term at the originally struck LTV**, preserving the no-margin-call-on-a-tier-fall promise. So the model must carry a **vintage of drawn balances by struck LTV**, not one balance at the current tier — and v1.0's own Layer 5 says Sovereign is "rented by conduct," so the tier moves constantly.

**Turnover roughly halves stream 5** (`PARAMS`, rank 2 load-bearing). Not because it is uncertain but because **v1.0 does not apply it at all** — it books peak drawn as though persistent, against a corpus-documented realised tenor of 71 days. This is an arithmetic correction, not a sensitivity.

### D13. Card economics gain the per-transaction fee, fraud, and fixed minimums

- **Per-transaction processor fee** takes ~**11% of gross interchange at Gold tier** and stacks multiplicatively with the PM share. v1.0 flags the gap ("at USD 0.10/txn a AED 200 ticket costs 0.18% against a 1.80% gross rate") and does not close it. **The effective PM share on small tickets is well below the contracted one, on 54% of terminal revenue.**
- **Stand-in fraud is bounded and computable.** `_draft_credit-and-card-infrastructure.md` §5.1: two fallbacks approve transactions **with no collateral check at all** — processor Commando Mode and network STIP — and "this is an unavoidable, permanent hole in a collateral-backed card programme." The recommended caps (USD 250/txn, 3 txns, USD 500 cumulative, no ATM, no cross-border) make the per-account worst case deterministic; only the incident rate is unknown. Note the caps also remove ATM and cross-border from stand-in, slightly reducing stream 4.
- **Card programme fixed costs** (BIN sponsorship, processor minimums, scheme fees) are minimum-commitment structures that bind at low volume exactly like the vault and Sumsub minimums — they **run the card at a loss for 12–18 months in the Conservative case**, drag v1.0's break-even does not carry.

### D14. Tax, VAT, and the capital escalator

- **UAE corporate tax at 9% is absent from v1.0 entirely.** A model that runs "the full P&L to net profit" and stops before tax is not running to net profit. With losses to Y7–Y9, **loss carry-forward shelters early profits**, so the omission is not even conservative. Flag the DMCC Qualifying Free Zone Person question (0% on qualifying income) — worth ~USD 220k/yr at Y10 — as a tax-opinion item alongside VAT.
- **VAT is flagged in v1.0 and modelled nowhere.** 5% resident / 0% non-resident under export-of-services. Given the base is deliberately NRI and GCC this may be a **structural margin advantage rather than a cost.** Needs a resident/non-resident split by segment — cheap, since segments already exist.
- **The 2%-of-Reserve-Assets capital escalator** (`_draft_entities-licensing-and-payments.md`): attaches to **Option B only**. At USD 200M of reserves that is **USD 4M of permanently locked capital** against the AED 1.5m floor. Model behind an `OPTION_B` switch defaulting OFF — under the chosen Option A the row is flat, which is the point. Report the delta as an opportunity cost memo line, not a P&L line, and **cross-check the USD 200M against the model's own computed Y10 AUM** rather than quoting it as a constant.

### D15. Opex gains a legal and trust block, and one correction

v1.0 has **no legal or counsel line in one-off cost and none in opex** — the "Legal, insurance, contingency" lump absorbs it invisibly. The corpus says "NOT ESTABLISHED. Budget generously" and names three opinions; the composability draft adds trust deed drafting, "the only genuinely new legal work this creates," plus a DIFC trustee company with **annual maintenance** — the line most clearly missing. The DFSA trust licence question is explicitly "a cost question and we cannot quote the client a number without it": carry a visible placeholder, not an implied zero.

**Correction: ADGM → DIFC.** v1.0's one-off table carries a USD 1,900 ADGM SPV. Decision 50 and the composability draft settle route 2 as **DIFC**. Wrong vehicle.

**And a cost reduction to show:** the composability Stage 1 build is "no added cost, and it removes cost" — a blocklist is less code than the planned allowlist. Composability must not appear as a new expense line. It also shares the multi-tenant register/mint requirement with stream 6 — **one build, two dependencies, do not double-count.**

---

## Tier 3 — presentation and deliverable structure

### D16. The headline output changes

v1.0 sets "the expense-derived break-even floor, by year" as the headline, then concludes on its own evidence that "break-even is not a function of how many savers you sign up." An investor-count break-even is right only for a business with roughly constant margin per unit; here margin per investor varies **~50× across segments and tiers**, and opex steps with N.

**Keep** the investor-count break-even as a named finding — it answers the client's item 5 and the answer is a valuable "no." **Promote:** contribution margin per cohort by month since acquisition; **LTV:CAC by channel × segment** at the corrected persistency (v1.0 flags its own LTV as stale, and its §7.3 buries the fact that agent commission consumes **88% of Year 1 gross margin**); months-to-cash-breakeven and peak funding; revenue mix over time.

### D17. Scenario architecture: three layers, not one switch

v1.0 has one `CHOOSE()` across 15 parameters. Flipping to Conservative sets all fifteen simultaneously — a joint state with probability near zero, which is why §12 reports it as "never" and why **the model has exactly one usable scenario: Base.** It also imposes an implicit correlation matrix of all +1 on parameters that are genuinely correlated in different directions.

**v2.0:** global switch relabelled honestly as a bounding case, **plus per-parameter override**, **plus named narrative scenarios** — at minimum: *rail kills it*; *card works, savings doesn't*; **no card** (the most important missing scenario — it removes 71% of revenue and is a real commercial risk, and is not representable in v1.0 at all because prepaid-vs-credit is not a variable); *distribution fails*; *client's plan* (the 100k target imposed as an input and measured against the floor). Add **prepaid-vs-credit as a binary switch** — v1.0 itself calls it "not a product choice, it is the business model."

Add **tornado charts** on net profit and on peak funding, which is what actually evidences the "five load-bearing assumptions" claim rather than asserting it.

### D18. Ten sheets, not five, and a Checks sheet the benchmark does not have

v1.0's §11 is internally inconsistent with §10.1 (§11 lists an Opex sheet; §10.1 puts opex rows on the Model sheet). And a 6-segment × 12-track cohort engine with an ICS state machine, six streams, a contra-revenue layer and two solvers lands near 600 rows × 65 columns ≈ 39,000 formulas on one tab.

Recommended: Cover / Assumptions / Scenario Parameters / Time Series / Cohort Engine / ICS Engine / Model / Opex & P&L / Summary / **Checks**. The Checks sheet is where this build should **exceed** the DRODE benchmark, which has none: cohort conservation per segment per track, tier counts summing to accounts, grams reconciliation, non-negativity, Gold Rewards cap never negative, acquisition ceiling never breached, activation flags firing on the right period, and a scenario-switch canary.

### D19. Sections required by the skill that v1.0 omits

Per `AUDIT-D` against the plugin's `revenue-model-architecture` SKILL.md: **§8 Growth Logic Summary** and the **Post-Launch Validation** half of §9 are required and absent. Also missing against the benchmark: per-stream Quick Facts / Drivers / Growth Logic template, **annual-block formula variants** (v1.0 writes only monthly formulas for a model with five annual columns), cell references, source URLs, a source-category taxonomy with counts, a unit-economics table, and a glossary.

### D20. Extend monthly resolution to M72

The first Sovereign appears at **M61** — one month after v1.0's monthly resolution stops. So the tier carrying the highest interchange, deepest waivers, largest Gold Rewards and highest LTV is computed only in annual periods, and a state v1.0 itself calls "rented by conduct, never owned" cannot be represented annually. v1.0 also admits the trailing-12 measures "must stay monthly-recomputed even in the annual block," which is self-contradictory.

**72 monthly + 4 annual = 76 columns.** Eleven extra columns buys the first full year of Sovereign at the granularity the engine requires. In the annual block, hold tier distribution and `Recent` constant at the M72 archetype-weighted distribution and **say so** rather than pretending to recompute a trailing-12 measure inside an annual column. Note also that **v1.0 has no survival rule at all beyond M61** — the curve must be extended to M120.

---

## Corrections owed to Phase 2 — additions to §13

New, beyond v1.0's existing ten:

| # | Target | Correction |
|---|---|---|
| 11 | v1.0 §9 item 6 | The tenure rebate is **retired** (decision 44), not merely unsized. The "0.10–0.75%" is Gold Rewards' range; the "~1.5%" is the superseded prohibited redemption fee. Strike the solver item. |
| 12 | v1.0 §0.1 / §6.1 / F5 | **Double-count:** the float cost of capital and the full dealer fabrication premium are charged simultaneously. They are alternatives under the dealer-carried / own-float fork. |
| 13 | `_draft_allocation-and-float.md` | Every float dollar figure is computed at USD 109.31/g. Correction 1 propagates: float capital rises **29.4%** at every year. |
| 14 | `_draft_purchase-structure.md` §4.1/§4.3 | Superseded by `_draft_sip-rulebook.md` §1.1 and decision 44 — spot **does** receive the tier entry-fee discount. |
| 15 | v1.0 §3 Layer 3 | The reduced ticket is hard-coded at USD 20 for all segments. Should be per-segment (~50% of prior ticket, floored at 20). |
| 16 | v1.0 §6.5 | Stream 5 computes peak drawn and prices it as persistent. Applying realised turnover roughly **halves** the stream. |
| 17 | v1.0 §7.4 one-off | **ADGM → DIFC.** Route 2 is settled as DIFC; the ADGM SPV line is the wrong vehicle. |
| 18 | `_draft_sip-rulebook.md` §7.1/§7.2/§8 | Carries pre-decision-46 vocabulary (continuity halving, revival, arrears, "Tenure"). Should be marked superseded **in the corpus itself.** |
| 19 | `_draft_credit-and-card-infrastructure.md` §7 | Header says three of five collateral-chain links are open; the table marks **two** open and three designed. The table is operative; the header is stale. |
| 20 | `_draft_ics-scoring.md` §7.1 | Heading reads "Six personas"; the table has **nine** rows (A–I). |

## Confirmed negatives to add to §15

- **No published source decomposes a savings-product or insurance lapse curve into payment-behaviour archetypes.** Aggregate curves are published in quantity (IRDAI, AMFI); the behavioural decomposition underneath them is published by nobody. The archetype table is a construction fitted to a researched aggregate and must be labelled as one.

## What v1.0 got right and v2.0 must not lose

Verified clean and load-bearing: the §0.1 fee waterfall (the fabrication premium is on the correct base; `C − C(1−f)(1+p)` returns the identical USD 1.6125); the §0.2 rail equation and both rail cases; every ICS constant against `_draft_ics-scoring.md`; the 36% PM-share floor and its arithmetic (0.75/2.10 = 35.7%); the VARA III.E.4 quote, verbatim and correctly located in Annex 2 Part III.E clause 4; **all ten cited decision numbers** — no misattribution, which is the error class most expected and it is clean. Also the §12 View 3 sensitivity grid, which is fully monotone with no inversions.

Structurally worth preserving: the §0 "read this first" device; the constructed opex base with per-line confidence; the inverted model direction; the eight-parameter solver; the corrections-owed register; confirmed negatives as findings; deliberately-excluded streams recorded so they are not re-proposed; and the single-sentence thesis.

---

# v2.1 → v2.2 decision record

**Date:** 2026-08-19. **D21, D22 and D23 were taken at v2.1 and are recorded in the brief itself** (7-year 29-column basis; score collapsed to a tenure to tier lookup; cohorts as a convolution). D24 and D25 below are new.

---

### D24. The bottom-up engine was reopened, tested and confirmed

**The question, raised deliberately:** should the revenue model be driven top-down from a market size and a penetration share, or bottom-up from acquisition and per-account behaviour? The concern behind it was legitimate: with three gates still open (dealer, title opinion, persona) and most inputs unresolved, a bottom-up engine asks for roughly fifty more parameters, which is fifty more places to be wrong.

**Decision: bottom-up stays, as the engine. Top-down survives in exactly three places** — the saturation ceiling, the B2B partner book, and the presentation layer.

**Three arguments carried it.**

1. **Unknowns argue against top-down, not for it.** A top-down model has fewer parameters but concentrates the answer in one that is unknowable: the penetration share. There is no source for "percentage of GCC South Asians who will buy a tokenised gold SIP" because the product does not exist. Bottom-up distributes the uncertainty across many inputs, several of which are genuinely sourceable (published interchange rates, IRDAI persistency, AMFI ticket data, insurance agency attrition). **When you know least is exactly when you most need the model to tell you which unknown to resolve first, and only a bottom-up model produces a tornado.**
2. **The findings are structural, not level-dependent.** Move persistency 30% either way and the card is still the majority of profit. Move card spend 30% and the SIP lane still loses money at Y10. Move acquisition 30% and the fee floor barely moves, because it is a fixed cost divided by a ticket and neither is an acquisition number. **The §0 findings would survive a wholesale re-cut of the parameter set**, which is what makes them safe to present while the gates are still open.
3. **Simpler did not mean safer.** v1.0 was the simpler model and it was wrong in five independent ways that took five audits to surface. A top-down model would have produced a healthy Y10 and the client would have priced the entry fee at 3%, below cost, for seven years.

**What was conceded.** The real complexity risk is the **surface** (parameters exposed, scenarios, what the client must follow in a call), not the engine. That is cut by collapsing layers to flat inputs, not by changing the engine. D22 already did this once.

**Consequence:** no rework. v2.1 was already bottom-up. This is a confirmation with its reasoning recorded so it does not have to be re-derived.

---

### D25. Six occupational segments become four regional ones, and the population is re-cut from Indian to South Asian

**v2.1:** S1 to S6, cut by occupation within nationality, each with a single ticket. Bases derived from the MEA overseas-Indians table filtered by an unsourced gold-savings propensity.

**The finding, from three parallel research streams against primary sources** (Oman NCSI monthly bulletin, Bahrain Social Insurance wage dataset, CBB Crypto-Asset Module text, CBUAE Financial Stability Report 2025, AMFI July 2026, Abu Dhabi 2024 census):

1. **The market is South Asian, not Indian.** Bangladeshi workers outnumber Indian workers in Oman (605,486 vs 515,361). Non-Indian South Asians match or exceed Indians in the UAE. **The MEA table counts PIO/OCI and historic diaspora and omits Bangladeshis and Pakistanis entirely.** It is the wrong instrument.
2. **Occupation was a proxy for ticket size**, and ticket size can be carried directly by two numbers per region without asserting an occupational split that rests on an uncited tertiary source.
3. **Bahrain is not an easy adjacency.** The CBB Crypto-Asset Module treats the token as a security, requires written CBB approval, BD 50,000 paid-up capital, escrow at a CBB-licensed retail bank and a CBB-licensed digital token advisor, and **contains no reverse-solicitation exemption** in 246 pages of text.

**Decision.**

- **Four modelled regions:** R1 UAE Indian, R2 UAE other South Asian (new, ~620,000, the largest single addition to the perimeter), R3 Oman, R4 India resident.
- **Three named, sized and deliberately not modelled:** Bahrain (~259,000, CBB gate), Emirati (~1.33m, wrong persona not small), Western expat (~500-600k, no gold-savings behaviour). **Each is a decision with a number attached.**
- **One funnel for every row** (active → direct-debit-capable IBAN → discretionary capacity). **The unsourced gold-propensity filter is deleted**, having been named the weakest link in the entire sizing at v2.1.
- **Two numbers per region: average ticket (S55) and floor share (S54)**, from which two ticket bands are derived. Unit margin, rail cost and card spend are computed per band and never on a regional average.

**Why the two-band mechanic is load-bearing and not bookkeeping.** A single blended ticket would have destroyed two separate non-linearities: the fixed per-collection rail cost (which is §0.3's entire fee-floor finding) and the card-spend income proxy (which would have flattened the 3.75x spread to ~1.3x on the line carrying 83.4% of Y10 gross profit). **This is the same error class as v1.0's ICS engine: average first, then apply a threshold.**

**The invariant that was deliberately preserved.** `base × ceiling` totals **165,750** against v2.1's **164,900**. The re-cut moves where accounts come from without inflating how many could ever exist. **A re-cut that raised the ceiling would be a re-cut that proved nothing.** Ceilings were re-based when the propensity filter was deleted, so base and ceiling moved together.

🔴 **The consequence, stated before the re-run rather than discovered after it.** The book-weighted average ticket falls from roughly USD 40 to **USD 31.5**. Against a fixed per-collection rail, **the minimum viable entry fee rises above §0.3's 3.79%.** The re-cut tightens the fee schedule; it does not rescue it.

**Two findings that are not sizing findings and reach into Phase 2.** The lowest-income band may hold a WPS payroll card with no IBAN and therefore no usable rail (corrections 23), and CBUAE has stated it will launch digital savings products for low-income earners within one to two years (correction 25). **Five corrections owed, numbers 21 to 25, two of which are client conversations rather than text edits.**

**Not done:** the reference model has not been re-run. Every output figure in the brief still reflects the pre-D25 segmentation and is labelled as such. Brief first, model second.

---

# v2.2 to v2.3 decision record

**Date:** 2026-08-19. One decision, presentational rather than structural.

---

### D26. The workbook ships on the firm's standard five-sheet architecture, with the machinery hidden

**The conflict.** The brief specified eleven sheets (D18, extended at D23). The firm's `revenue-modeler` skill specifies **exactly five required sheets in a fixed order** — Cover, Assumptions, Scenario Parameters, Model, Summary — and permits additional working sheets after them. **Both cannot be right, and the standard wins**, because it is the firm's deliverable convention across engagements and a client who has seen one model should recognise the next.

**Decision.**

- **Five visible sheets, in the standard order and with the standard names.**
- **Five hidden working sheets, placed after them:** Time Series, Lifecycle Curves, Acquisition, ICS Validation, Checks.
- **The former Opex & P&L sheet folds into Model as a second row band.** Model goes from ~200 to ~280 rows.
- **The Checks master flag is mirrored to Cover as a link**, green on TRUE and red on FALSE.

**Why opex folds into Model rather than hiding.** A reader must be able to trace **one visible sheet** from accounts acquired to net profit and cash without unhiding anything. Hiding the P&L would put the answer behind the machinery, which is the wrong side of the line. **The cost is height, not complexity.** This also settles an inconsistency inherited from v1.0, whose §11 listed an Opex sheet while its §10.1 put opex rows on Model. **§10.1 wins.**

**Why Checks hides, but not entirely.** Checks is where this build exceeds the benchmark, which has none. But sixteen TRUE/FALSE rows are a working artefact, not a presentation one. **Promoting one cell to the Cover keeps the integrity signal and loses the clutter.**

🔴 **The one real consequence, and it is not cosmetic.** The acyclicity rule at §3.x was written as **"no sheet may reference a sheet to its right"** — a tab-position test. **Hiding inverts tab order against logical order.** Model sits at tab 4 and legitimately reads Time Series, Lifecycle Curves and Acquisition at tabs 6, 7 and 8. A positional test would now **fail a correct workbook**, and a modeller who "fixed" it by reordering tabs would break the standard five-sheet layout instead.

**Resolution: the dependency test is by sheet NAME against the §3.x.1 numbered logical order, and that order is written onto the Cover sheet so it cannot be lost.** Two build rules follow:

- **Cover is logically last, not first.** It is the only visible sheet carrying an inbound reference (the Checks master flag), and that is the only edge into it.
- **Hiding is the final build step.** Build everything visible, pass all sixteen checks, then hide. **Never hide a sheet that has not passed its checks** — a hidden FALSE is precisely the silent failure §3.x exists to prevent. Re-run every check after hiding.

**The honesty obligation this creates.** Hiding machinery is a presentation choice and becomes a misrepresentation the moment a reader cannot discover the machinery exists. **The Cover carries a sheet map naming the five hidden sheets and stating that unhiding them is expected rather than discouraged.** Two checks enforce the rest: a hidden-sheet inventory, and a test that the Cover flag is a formula and not a typed TRUE. **A hardcoded TRUE on the Cover is the worst single failure this workbook could ship**, because it hides a hidden sheet's failure behind a visible green cell.

**What did not change.** Nothing about what is computed, in what order, or by what formula. **D26 separates presentation from computation; it does not merge them.** The 45,000-formulas-on-one-tab argument that produced the multi-sheet structure still stands — the machinery still has its own sheets, they are simply not the ones a reader opens.

**Brief sections amended:** front matter, §1.1, §3.x.1, §3.x.4, §10.1, §12 (Cover, Model, the former Opex & P&L), §20.1 items 4 and 4a, §20.2 steps 16 and 25.

---

### D27. CAC is linear in the revenue model; convexity moves to Phase 5

**The question.** v2.2 modelled marketing CAC as convex in spend: `S15 × [1 + 0.35 × (spend ÷ 60,000)^0.7]`, giving USD 162 effective CAC at USD 60,000/month against a USD 120 base. Should the revenue model carry that shape?

**Decision: no. `effective_CAC = S15`, flat.** The convexity survives as a scenario switch `CAC_CONVEXITY`, **default OFF**, with its flexes intact. **Calibration of the shape moves to Phase 5.**

**Three arguments carried it.**

1. **The constants are invented and the brief already says so.** §18 item 11, verbatim: *"No published CAC benchmark exists for any UAE gold or savings product. S15 and the S25 curve are both judgement. The functional form is defensible; the constants are not."* A 0.35 coefficient and a 0.7 exponent are two unsourced numbers producing a precise-looking answer in a client-facing model.
2. **The failure mode it guards is already guarded, by a sourced mechanism.** The argument for convexity was that flat CAC lets a model buy unlimited growth at a constant price. **That brake is the saturation term** (S23): `new = raw_demand × [1 − cumulative_ever_acquired ÷ (base × ceiling)]`. Spend cannot manufacture accounts the perimeter does not contain. **Two mechanisms guarding one failure, and only one of them is sourced.**
3. **Convexity is a dynamic, and dynamics are Phase 5's deliverable.** Consistent with L5, which already assigns competitive response, saturation shocks and viral dynamics to Phase 5. **The revenue model is a structured argument a client signs off on; the simulation is where behaviour under stress is explored.** Importing a half-calibrated dynamic into the first artefact weakens both.

**Precedent.** This is the same move D22 made with the ICS rate ladder: **demoted to a validation or scenario artefact, not deleted**, so the machinery survives for whoever needs it next.

🔴 **The one real consequence, and it must travel with the output.** **Direct-channel LTV:CAC at high spend is an UPPER BOUND under linear CAC.** LTV:CAC by channel × segment is promoted output 2 (§14.3), so the direct-channel cells carry the caveat explicitly and the switch exists to show the sensitivity on request. **CAC uncertainty still reaches the tornado through S15's own 80 / 120 / 200 range** — a level the tornado can rank, rather than a shape it cannot.

**What did not change.** The saturation rule, the agent ramp and attrition, the referral double-gate, and the partner channel are all untouched. **Only the direct channel's cost curve is affected, and only its shape, not its level.**

**Brief sections amended:** §3 Layer 1 (Direct row + a new note after the channel table), §8.2 S25, §11 growth logic summary.

---

# v2.3 to v2.4 decision record

**Date:** 2026-08-19. Three decisions from one research pass. **Full evidence, sources and method in `_working_dealer-premium-and-comparables-research.md`.**

---

### D28. The fabrication premium is measured, not assumed

**The problem.** F4 sets **70% of stream 1's cost base** and was carried at **3.00%** as an unsourced midpoint of a 2 to 5% range nobody publishes. §18 item 11 said so plainly: *"the functional form is defensible; the constants are not."* Four prior research passes on the direct question returned nothing.

**The method that worked, and it is worth keeping.** A first attempt compared dealer prices in AED against a spot price captured at a different moment, on a day gold moved 3.6%. It returned bars priced **below spot**, which is impossible. **The fix is the same-page pair: find a dealer publishing both its own live gold rate and its bar prices on one page, and take the ratio.** Timing cannot corrupt it, because both numbers are struck at the same moment.

**What was observed.** goldtrade.ae, 19 Aug 2026 19:52, rate AED 530.45/g: 1 g **+9.75%**, 10 g **+3.07%**, 100 g **+1.71%** (PAMP 1.75, Valcambi 1.67), 1 kg **+0.93%** (Emirates 0.98, Etihad 0.87). **The curve is monotonic, which is the shape a real premium curve must have**, and that internal consistency is the main reason to trust this pair. iGold publishes a quantity ladder giving **25 bp at 5+ bars**.

**Decision: F4 = 1.50% at 100 g, 0.95% at 1 kg. Confidence MODERATE, source category OBSERVED.** Conservative holds 3.00%, so the old assumption becomes the downside rather than the base.

🔴 **The ladder was one denomination too pessimistic at every rung. The model's 1 kg assumption (2.00%) was worse than what 100 g actually costs (1.71%).**

**Good Delivery is retired as a rung.** The third rung targeted a 400 oz bar and concluded it never clears at the model's volume. **Dubai's own Good Delivery standard is a 1 kg bar at 995+**, already rung two, and DGD is itself superseded by the UAE Good Delivery standard under Cabinet Resolution 2/16 of 2020. **The rung was aimed at the wrong object.**

**What remains open.** The genuine 10 to 50 bar tier is unpublished — both dealers stop at 5 bars and say "call us" — and whether a deal strikes on the fix or on the dealer's own tick moves the answer 20 to 30 bp. **F4 is downgraded from CRITICAL to MODERATE in §16: still worth a dealer conversation, no longer setting the sign of the answer.** ⚠ **The two-way spread on buyback replaces it at the top of the dealer agenda, and is entirely unobserved.**

---

### D29. Aurumix carries its own float from M1

**The question.** S51 held "dealer-carried at launch, own float from Y3." Is that available?

**Decision: no. Own float from M1.** The side of the fork is **forced, not chosen**, and S51's source category changes from ASSUMPTION to DERIVED.

**The argument is by elimination.** Three tokenised gold products were examined against their binding terms. **All three carry inventory** — Paxos holds its own PAXG *"to hedge against price risk"* (Terms 4.9), Tether's affiliate AGCL holds token inventory, Comtech may run **up to 10 kg unbacked** for 24 hours (T&C 3.5). **The float is not a design flaw to engineer away; it is what all of them need.** And each of their three routes to minimising it is closed to Aurumix:

- **Comtech's route, running briefly unbacked:** closed by the `trust holdings ≥ tokens outstanding` invariant and decision 34's money-then-title-then-token ordering.
- **Tether's route, no repurchase obligation and an agency sale where the customer bears execution risk:** closed by VARA Annex 2 III.E.4 and the formulaic buyback promise.
- **Paxos's route, a named dealer filling instantly against a 5-second quote:** closed because **there is no dealer.** It is the single largest open item in the engagement.

🔴 **A finding for the client conversation: neither PAXG nor XAUT accepts a repurchase obligation, and Tether states so explicitly. Aurumix is carrying a liability the two largest issuers in the world decline to carry, through a dealer who has not been named or asked.**

**Consequence, governed by correction 12.** Price-gap risk and float cost of capital **bite from M1** rather than Y3; the premium **narrows**, which is what D28 reflects. ⚠ **Charging the wide dealer-carried premium and both float costs simultaneously double-counts under either regime.**

🆕 **The finding inside this one, not framed before.** The 0.79% price-gap is **a pricing-convention cost, not a float cost.** It exists because Aurumix promises a price struck at the next published LBMA fix, hours away, and cannot buy at that price until it arrives. Paxos reduces the identical exposure to near zero with a 5-second streaming quote hedged immediately with StoneX. **The fix was chosen for a real reason — neither side selects it, and it is used identically on entry, arrears and exit — but it now costs 0.79pp from launch against a margin that was 0.54%.** Put it to the client as a priced trade-off: **neutral pricing versus price-gap cost.**

---

### D30. The premium is charged on net new grams, not gross inflow

**The error.** `cogs(s,t) = net_of_fee(s,t) × fabrication_premium(t)` charges the premium on the full inflow every period, with no offset.

**Why half of it was right.** The premium is genuinely a per-gram cost. Every gram a customer holds came from a bar bought at fix plus premium, so it does pass through proportionally.

**Why the other half is wrong.** **Redeemed gold returns to the float and is re-allocated without paying the premium a second time.** Only the **net** addition to the book is procured from the dealer.

**Decision:** charge the premium on `MAX(0, grams_required − recycled_grams)`. **Size: if redemptions run at 20% of inflows, premium cost was overstated by 20%.** Small in Year 1, growing as the book ages. **It moves in the business's favour.**

**Consistency note.** The brief already applies this logic on the redemption side — one of its own checks is *"spread cost is exactly zero in every growing month"* — and simply had not applied it to COGS.

🔴 **One dependency, and it is undesigned.** This holds only if redeemed gold genuinely returns to the float rather than going back to the dealer. **Nobody has written that down.** It interacts with the buyback mechanics and the backing invariant. **Correction 30. Settle it before the change is built.**

---

### The combined effect of D28, D29 and D30

On a USD 75 contribution at a 5% fee, before D30:

| Line | v2.3 | v2.4 |
|---|---|---|
| Gross margin retained | 2.15% | **3.58%** |
| Net contribution margin | **0.54%** (USD 0.41) | **1.97%** (USD 1.47) |
| Break-even ticket, Base rail | ~USD 29 | **USD 10.90** |
| Minimum viable entry fee | 4.96% | **~3.07%** |

**Two conclusions move and one holds.**

- **The minimum-ticket problem largely dissolves at the Base rail** — break-even falls below the inherited USD 20 floor. ⚠ **At the Conservative rail it is USD 66, so the rail cost still decides it.** The floor is no longer structurally broken; it is rail-dependent.
- 🔴 **§0.3 holds, with a different cause.** The 3% fee is now short by ~0.07pp rather than 0.79pp. *"The fee cut is unfundable"* becomes *"the fee cut breaks even and leaves nothing for anything else."* **The binding cost is no longer the premium; it is the float carry D29 brings forward to launch.**
- **§0.1, §0.2, §0.4 and §0.5 are untouched.** None of them runs through the premium.

⚠ **Every output figure in the brief was generated at F4 = 3.00% under dealer-carried float and is superseded. The reference model has not been re-run.** Brief first, model second.

**Brief sections amended:** front matter, §0.3 (superseding note), §3 Layer 3 (COGS formula), §3 Layer 4 and §6.1b (unit-margin tables), §6.1 (waterfall re-cut, both columns), §8.1 F4, §8.2 S51, §11 (growth logic), §15 corrections 26 to 30, §16 (F4 downgraded, two-way spread promoted).

---

### D31. The payment rail leaves the entry-fee build-up and becomes a pass-through

**Taken 2026-08-20 by Abdur.** The principle, in his words: **the entry fee only includes what Aurumix charges.**

**What changes.** The payment rail is a third-party bank/PSP charge, not an Aurumix charge. It is therefore **grossed up onto the collection request and remitted** — Aurumix asks for `ticket + rail`, passes the rail to the PSP, and books nothing on it. `STREAM1a` and `STREAM1b` lose their `− rail` term. `S1` survives as `rail_memo`, a disclosure and risk row that touches no total.

```
BEFORE:  Net = C × (f − c) − R
AFTER:   Net = C × (f − c)          and the customer is asked for C + R
```

**The entry-fee build-up is now: fabrication premium + price-gap risk + float cost of capital + margin.** Four terms, not five.

#### The arithmetic, USD 75 at a 5% fee

| Line | v2.4 | **v2.5** |
|---|---|---|
| Gross margin retained | 3.58% | 3.58% |
| less price-gap + float CoC | (1.28%) | (1.28%) |
| less payment rail | **(0.33%)** | **— passed through** |
| **Net contribution margin** | **1.97%** (USD 1.47) | **2.30%** (USD 1.72) |
| **Minimum viable entry fee** | ~3.07% | **~2.74%** |
| **Break-even ticket** | USD 10.90 Base / USD 66 Cons | **none — the term is gone** |

#### Four consequences, three of which reverse a stated finding

1. 🔴 **§0.3 REVERSES at the Base rail.** The 3% target clears with **~0.26pp of headroom** where v2.4 had none. **The fee-fundability finding, which has been in every version of this brief, does not survive D31.**
2. 🔴 **The minimum-ticket problem dissolves as a margin problem.** `C_min = R ÷ (f − c)` with `R = 0` has no solution. The whole break-even ladder in `_parked_collection-economics-and-minimum-ticket.md` §2 — USD 47 / 71 / 118 / 249 — is **retired.** Every ticket clears wherever `f > c`.
3. 🔴 **Spot stops being the highest-margin inflow.** SIP and spot converge to an identical **2.30%**. The 2.25%-vs-1.96% gap was *entirely* the fixed rail spread over an 8.3× larger base — a property of the rail wearing spot's clothes, not of spot.
4. 🔴 **S1 leaves the tornado**, where it ranked 6th at USD 1,607,643 of swing on cumulative net profit. **That swing does not relocate. It ceases to exist in the P&L and reappears as unmodelled churn risk.**

**And unit margin becomes LINEAR in ticket size.** `R` was the only source of the non-linearity that justified computing margin per segment at that segment's own ticket. ⚠ **Do not collapse the per-segment computation on the strength of this** — the tier-weighted discount and card spend are still non-linear in ticket. But **§5.2's two-band structure now rests on the card leg alone**, which is thinner than what D25 claimed for it (correction 33).

#### The three risks this carries, and they are not small

1. 🔴 **It improves Aurumix's margin by making the customer's deal worse, and the incidence is regressive.** All-in customer cost is **unchanged** — only the attribution moved. The gross-up is **1.25% of a USD 20 ticket against 0.33% of a USD 75 one** at the Base rail; **6.8% against 1.8%** at the Conservative rail. **The floor band is 40–60% of the book and is the population D25 found may lack an IBAN-capable account at all.** This must be said to the client in those words and must not be presented as a cost saving.
2. 🔴 **It substitutes a modellable risk for an unmodellable one.** A margin hit is arithmetic; a refusal rate is behavioural and **no source exists for it.** Will a UPI-native saver — habituated to payment rails being free by regulation — approve a USD 21.36 request for a USD 20 commitment? **Nobody knows, and it lands squarely on the adoption-bridge problem that is already the engagement's central unsolved question.**
3. ⚠ **It is asymmetric by regulation, not by choice.** VARA Annex 2 III.E.4 forbids charging any fee on redemption, so `F20` stays absorbed in Stream 0. **Aurumix may pass through the cost of taking money in but not the cost of paying it out.** Worth a line to counsel: does a grossed-up collection request itself engage any VARA disclosure or fee-transparency rule?

#### What did NOT change

**The structural point of §0.3 survives.** The fee schedule and the denomination schedule remain physically coupled, and the fee still cannot fall below premium plus float costs. **The constraint moved; it did not disappear.** §0.1, §0.2, §0.4 and §0.5 are untouched — none runs through the rail.

⚠ **And a countervailing finding landed the same day.** The 2026-08-20 research pass **failed to replicate D28's premium measurement** (correction 36). **If F4 reverts toward 3.00%, the minimum viable fee goes from ~2.74% to ~4.2% and D31's headline reversal is itself reversed.** 🔴 **Do not carry the 0.26pp of headroom to the client until F4 is re-observed.**

**Brief sections amended:** front matter (v2.5 paragraph), §0.3 (reversal box), §3 Layer 4 (equation, table, the twice-moved spot claim), §6.1a (waterfall, four consequences, both formulas, drivers, Key Uncertainties), §6.1b (drivers, both formulas, the withdrawn finding), §7.1 (COGS is three terms), §8.2 S1, §15 corrections 31 to 36.

---

### D32. The float cost of capital leaves COGS and becomes a memo line

**Taken 2026-08-20 by Abdur.** His reasoning: *it is just an opportunity cost, not a financial impact — they hold the gold regardless.*

**The first half is right and the second half is not, and the distinction decides how the change is implemented.**

#### Why the change is correct

**F5 is an imputed cost of equity.** No counterparty invoices Aurumix for it. **A statutory P&L does not book an equity cost of capital inside cost of goods sold**, and §11 currently does exactly that — so stream 1's "net contribution margin" charges a cost the cash flow never pays and does not reconcile to it.

⚠ **It is also an internal-consistency fix, and that is the stronger argument.** §7.6 already states the house rule for locked capital, verbatim: *"Report the escalator as an opportunity cost, not a P&L line… `(required_capital − AED 1.5m) × cost_of_capital` as a **memo line**."* **F5 was the one place the brief broke its own rule.** D32 does not introduce a treatment; it applies the existing one consistently.

#### 🔴 Why "they hold the gold regardless" does NOT hold

**The trust holdings and the float are two different piles of metal with two different owners.**

| | Trust holdings | **The float** |
|---|---|---|
| Whose gold | **The customer's**, held under `trust ≥ tokens` | **Aurumix's own inventory** |
| Whose money bought it | The customer's contribution | **Aurumix's balance sheet** |
| Capital cost to Aurumix | **Zero** | **Real** |

Aurumix holds the *customer's* gold regardless — and that costs it no capital. **The float exists for a different reason entirely: you cannot buy 0.5 g from a dealer, so Aurumix must own bars BEFORE any customer owns a slice of them.** That inventory is funded from the raise. **It is not gold they were holding anyway.**

#### So the implementation is a reclassification, not a deletion

- **The carry** (`0.49 / 0.31 / 0.38%`) leaves every margin, COGS and P&L total → `floatcoc_memo`, reported on Summary. The Checks sheet asserts it appears in no total.
- 🔴 **The principal is UNTOUCHED. USD 29k at Y1, USD 437k at Y3, USD 3.6M at Y10** — balance sheet, funding view, and inside the USD 15.1m peak-funding figure. **The cost moved from the P&L to the cap table. It did not stop being money.**
- 🔴 **One case restores it as a real expense:** if the float is ever **debt-funded** — a gold-backed working-capital facility, or dealer credit — the interest is **cash, not opportunity**, and belongs in the P&L as a financing line. **D32 assumes equity funding. Make that explicit and add a `FLOAT_DEBT_FUNDED` switch.**

#### The arithmetic

| | v2.5 | **v2.6** |
|---|---|---|
| `c` = premium + price-gap + float CoC | 2.78% | **2.29%** — two terms |
| Net contribution margin, USD 75 | 2.30% (USD 1.72) | **2.79% (USD 2.09)** |
| Minimum viable entry fee | ~2.74% | **~2.26%** |
| Headroom against the 3% target | 0.26pp | **0.74pp** |

#### 🔴 The pattern this creates, recorded deliberately

**D31 removed the rail. D32 removed the float carry. In one day, `c` went from four terms to two and the minimum viable entry fee fell 3.07% → 2.74% → 2.26% — while nothing changed in the business.** Both steps are defensible. **The sequence dissolved §0.3, a finding present in every version of this brief, by re-attribution alone.**

⚠ **And the third term is the weakest of all: the fabrication premium failed replication the same day** (correction 36).

🔴 **Standing instruction, and it is the point of writing this down.** **Before the fee reversal reaches the client: adversarially re-check the two surviving cost terms, re-observe F4, and state the reversal as conditional.** The honest sentence is not *"the 3% fee works."* It is: ***"the 3% fee works if the premium is really 1.50%, and if customers accept a grossed-up collection request."*** **Neither is established.**

**Brief sections amended:** front matter (v2.6 paragraph and the pattern note), §0.3, §3 Layer 4 (`c` is two terms), §6.1a (waterfall, consequence 3, formula), §6.1b (table, formula), §7.1, §7.5 (the D7-inversion note and the third must-not rule), §8.1 F5, §15 corrections 37 and 38.

---

### D33. Redeemed gold returns to the float up to the ceiling; the excess is sold back at the observed bid

**Taken 2026-08-20 during the reference-model rebuild, because the build could not proceed without it.**

#### The finding that forced it

**D30 charges the fabrication premium on net new grams rather than on gross inflow.** The reasoning is that only the net addition to the book is procured from a dealer: grams recycled out of a redemption are re-allocated to the next buyer without re-paying fabrication.

🔴 **That reasoning holds only if redeemed gold comes back to the float. If it goes back to the dealer, there is nothing to recycle and the premium lands on gross inflow after all — D30 collapses entirely.** Correction 30 flagged this as an undesigned dependency and the corpus does not settle it anywhere. **Nobody had written down which happens.**

It is not a small question. It sits at the junction of three things already decided: the buyback mechanics, the `trust ≥ tokens` backing invariant, and D29's forced own-float position. **A model cannot be built without an answer, and picking one silently is exactly the failure correction 30 caught.**

#### The decision

**Redeemed grams return to the float, up to the float ceiling set by F38. Any excess is sold back to the dealer at the observed bid of spot −1.50%.**

The float ceiling is the natural cap and it is already computed: `MAX(2 bars, 1 bar + S50 days trailing inflow)`. Below the ceiling there is somewhere for redeemed metal to go and it displaces a dealer purchase one-for-one. Above it there is not, and holding metal beyond the sizing rule would be an unfunded inventory position that the float rule exists to prevent.

⚠ **Self-custody withdrawals do not recycle.** A withdrawal to self-custody takes the metal off the platform entirely, so it is never available for re-allocation and it never reduces the premium base. Only redemptions recycle.

#### 🔴 The bid and the ask are not symmetric, and must never be netted as though they were

**Correction 35 measured the dealer bid as near-flat across denomination while the ask premium moves roughly 194bp.** The temptation is to model a single round-trip spread and net the two sides. **That is wrong, and it flatters both sides of the trade.**

| | On the way in | On the way out |
|---|---|---|
| What is paid | **Full fabrication premium**, which moves with denomination | **Full bid discount**, spot −1.50%, which does not |
| Recovered on the other side | **No** | **No** |

**Fabrication is paid to acquire and is not recovered on disposal.** The model therefore pays the premium in full on net new grams and takes the bid discount in full on the excess, and books no round-trip spread anywhere.

This also corrects a live error in the pre-rebuild model, which carried a symmetric `DEALER_TWO_WAY_SPREAD` of 1.0% — a figure that was itself registered as DERIVED because no source stated it. **The observed 1.50% bid replaces it.**

#### Implementation

- Switch **`REDEEMED_GOLD_TO_FLOAT`**, **default True**.
- `params.DEALER_BID_DISCOUNT = 0.0150`, sourced to correction 35.
- **Both settings are run and reported**, in `outputs/d33_redeemed_gold_switch.csv` and in the numerical spine. Reporting only the default would repeat the mistake correction 30 caught: a decision taken silently is a decision nobody can challenge.

#### What it is worth, and the honest caveat

**On Base assumptions the switch is close to immaterial: cumulative premium cost moves from USD 456,330 to USD 460,503, a difference of about 0.9%, and peak funding moves by roughly USD 9,000 against a USD 13.1m requirement.**

⚠ **Do not read that as evidence the decision does not matter.** It is small **because the Base book grows in every month of the modelled horizon**, so redemptions are a thin trickle against inflow and there is almost always headroom to recycle into. **The two settings diverge precisely in the book states where it counts — flat, shrinking and run** — which are the states the book-state axis exists to test. **In a run scenario the recycling assumption is the difference between re-allocating metal and dumping it into a bid.**

**Recorded as provisional in the derived audit log**, alongside F4. It is a defensible default settled by the modeller, not a decision the client has taken.

**Brief sections to amend:** §6.0 (stream 0 formula and the dealer-spread term), §7.1 (COGS note on D30), §7.5 (float mechanics), §8.1 (new switch, and F20's spread basis), §13.3 (binary switch table), §13.4 (book-state axis — flag that this is where the switch bites).

---

### D34. The convolution and the vintage triangle disagreed by 8%, and both had an off-by-one

**Taken 2026-08-20 during the rebuild. Not a design choice — a defect found and fixed.**

#### The finding

D23 requires the lifecycle-curve convolution to become the live engine, with the vintage triangle retained as an equivalence harness. **Run against each other on the same acquisition vector, the two engines disagreed by up to 8% on the payment axis.** They agreed to 4e-14 on the holding population, which is what made the cause findable: the error was in the *ageing*, not in the state machine.

**Two separate off-by-one errors, in opposite directions, neither visible from either engine alone.**

1. **`Vintage.step_population` computed age as `m − origin + 1`.** It is first called in the month *after* origination, so the first hazard an account ever faced was labelled age 2. This disagreed with `survival_curve` in the same module, which indexes from 1. **The triangle had been inconsistent with its own survival curve since it was written**, and the discrepancy only bites where a hazard is a function of age — which in this model is the early-lapser decay at M13, so it was invisible in aggregate.

2. **The convolution offset was `t − s + 1` rather than `t − s`.** A vintage acquired in month t is observed in month t at **age zero**; it has not yet faced a hazard. The wrong offset aged every cohort by a month.

#### Why this matters beyond the fix

**The second error was worst exactly where the model is most closely read.** It understated the payment axis by about 8% at M1, decaying to about 4% by M20 — that is, throughout the M1–M24 monthly window that D21 makes the reporting focus, and steepest during the acquisition ramp where the gate has not yet resolved.

⚠ **Neither engine could have found this alone.** The triangle was self-consistent and produced plausible numbers; the convolution was self-consistent and produced plausible numbers. **The equivalence test is the only thing that catches a defect of this shape, which is the argument for keeping the triangle rather than deleting it once D23 lands.** After the fix the two agree to 4.2e-14 relative.

**Standing rule:** the equivalence test runs on every full model run and is reported in `VALIDATION.md`. **The triangle is never deleted.**

**Brief sections to amend:** §3.x.4 (add the equivalence test to the checks list), §15 (new correction recording the defect).
