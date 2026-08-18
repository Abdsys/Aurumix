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
