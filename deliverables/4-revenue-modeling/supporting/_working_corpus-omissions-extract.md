Fully verified. All ten items confirmed with three corrections to the audit's descriptions. Here is the extraction.

---

# Extraction: mechanism-design material missing from the Revenue Model Architecture Brief v1.0

Three of the audit's descriptions were imprecise; those are flagged in place. One item (7) turns out to be **more wrong than the audit thought** — the mechanism itself is retired, not merely unsized.

---

## 1. The redemption cost argument

**What the corpus says.** `_draft_purchase-structure.md` §5.3, §5.4, §5.5. All three sections exist as described.

§5.4 "Why zero-fee redemption is affordable" opens:

> "The obvious objection to III.E.4 is that Aurumix must pay the dealer's bid-ask spread on every exit and cannot charge for it. **That objection assumes gross exits drive physical sales. They do not.**"

The four-row table is verbatim as reported:

| Book state | Inflow | Gross exits | Net flow | Physical gold sold |
|---|---|---|---|---|
| Growing | 8% of AUM | 3% of AUM | +5% | **None.** Float absorbs |
| Flat | 4% | 4% | 0% | **None.** Float absorbs |
| Shrinking | 2% | 6% | −4% | Yes, on the 4% net only |
| Run | 1% | 25% | −24% | Yes, in size, at bid, into a falling market |

> "**In the first two rows, which is where a growing product lives, the zero-fee rule costs nothing.** The cost of the redemption promise is the dealer spread on **net** outflow, not on gross exits, and it is bounded by the float's capacity to warehouse the difference."

§5.3 exit lifecycle (eight stages) contains the mechanism behind that:

> "**Stage 8 is the point of the whole design.** An exit does not sell gold. It returns grams to the float. The next buyer consumes them. The treasury only touches the physical market when the float breaches a band."

Stage 3 fixes the price convention: "**next fix after the request** — Same convention as entry. Neither side can select the fix." Stage 6 payout is "**T+1, target**."

§5.5 settlement window tiers, verbatim:

| Redemption size | Settlement target | Basis |
|---|---|---|
| Small | Next business day | Absorbed by the float |
| Medium | Up to 3 business days | May require a dealer sale |
| Large | Up to 5 business days | Physical sale, possibly staged |

> "**Thresholds are deliberately not set here: they depend on the float size, which depends on the dealer.**"

**Two dependencies the brief does not carry.** `Aurumix_Process_Maps_Redemption.md` §"Open items" contains a red flag that inverts the §5.4 argument under the brief's own launch assumption:

> "🔴 **The zero-fee-exit argument assumes Aurumix owns the float.** Under a dealer-carried float, an exit requires the dealer to **take grams back on demand**, which is a second commitment."

The allocation draft's working recommendation is **launch dealer-carried** — so at Year 1 the §5.4 affordability argument is not yet established. And `_draft_purchase-structure.md` §5.1 leaves the spread incidence open to counsel:

> "III.E.1 says 'equal value.' The safe reading is the full prevailing value of the underlying grams with no haircut. An arguable reading is realisable value, that is, the dealer's bid. **The difference is the entire two-way spread and it decides who absorbs it on every exit.**"

**What the model must do with it.**
1. Replace the undriven `− redeemed(t)` term with a **gross exit rate driver**, expressed as % of AUM/yr, and add a computed **net flow** row: `net_flow(t) = gross_inflow_grams(t) − gross_exit_grams(t)`.
2. Add a **new cost line, redemption spread cost**: `MAX(0, −net_flow(t)) × gold_price × dealer_two_way_spread`. It is zero in every month the book grows. This is a P&L line the brief does not have.
3. Add four named **book-state scenarios** as a first-class scenario axis using the corpus's own figures (8/3, 4/4, 2/6, 1/25). The Run row is a **stress test, not a scenario**: at 25% gross exits against 1% inflow the model should report the float breach, the settlement-window tier that fires, and the spread cost on the 24% net.
4. Add an **open question**: settlement-window thresholds are unset pending float size pending the dealer. The model carries the tiers as structure with thresholds as inputs.
5. Add a **conditional**: if the launch float is dealer-carried, the zero-cost rows do not hold without a second dealer commitment. Flag as a Year-1 assumption, not a finding.
6. Add the **counsel switch** on "equal value": full prevailing value (Aurumix absorbs the spread) versus realisable value (customer absorbs). Model the safe reading; expose the switch.

**Where it lands in the brief.** §6.1 gets the new spread cost line; **Layer 6 (§3)** gets the net-flow logic replacing the bare `− redeemed(t)`; §8.2 gets the gross-exit-rate scenario variable and the four book states; §14 gets the settlement thresholds and the "equal value" counsel question.

---

## 2. The missed-payment ladder and account states — **with a large stale-mechanics warning**

**What the corpus says.** `_draft_sip-rulebook.md` §7.1 is a six-row table, exactly as reported:

| Case | Gold | Score | Rail action |
|---|---|---|---|
| Contribution at or above the floor, on time | Allocated | **Accrues** | None |
| Contribution at or above the floor, paid **late but inside 5-day grace** | Allocated at the fix on the day funds clear | **Unaffected** | Request stays open. Nudges on days 1, 3 and 5 |
| **Payment below the floor** | **Rejected and returned. Nothing allocated** | Not a contribution | The request stays open for the full amount |
| **Nothing cleared by the end of grace** | **Untouched** | **Continuity halves. Tenure, Retention and gold untouched** | Request expires. Next month's request unaffected |
| **Arrears cleared inside 12 months** | Allocated at the fix on the day arrears clear | **Restored per the §11 revival rule** | Normal |
| Spot purchase | Allocated | **No period** | n/a |

§7.2 grace mechanics, verbatim and all live:

> "**Grace is 5 days** from the contribution date. 🔄 **Revised 2026-08-10 from 15, Abdur's call.** ... Two build rules: calendar days, and **grace never expires on a weekend or public holiday**, it rolls to the next business day, or a Friday failure eats half the window."

> "**Grace crosses the month boundary and settles the period it was due.** A payment on 3 March for a 28 February date closes February. **March still needs its own payment.** A late payment can never close two periods."

> "**Arrears buy gold at the fix on the day they clear**, never at the missed period's fix. Otherwise revival is a free one-directional look-back option on gold."

§7.3, verbatim:

> "**Involuntary churn runs 20% to 40% of total subscription churn.** Of the six in ten investors gone by month 61, a quarter to a third never decided to leave: a payment failed and the product treated it as a choice."

> "🔄 **Revised 2026-08-10: dropping the pull rail solved most of this section's problem at the rail layer.** There is no bounced debit to masquerade as a decision any more. What remains is smaller but real: a request the investor never saw (phone lost, app notification broken, travelling) versus one they saw and declined."

§8 parallel states, three rows (the declared pause was **deleted** 2026-08-10):

| State | Trigger | Gold | Continuity | Tenure | Retention | Confirmed SIP |
|---|---|---|---|---|---|---|
| **Regulatory block** | Compliance blocks the account (e.g. the investor becomes India-resident). **A system event, not a request** | Retained | **Frozen** | Frozen | Keeps running normally | Retained |
| **Stop** | The investor cancels | Retained | Decays as normal | Held | Keeps running normally | **Retained** |
| **Dormant** | 12 consecutive silent periods. The SIP instruction auto-cancels; account goes hold-only | Retained | Held at its decayed level | Held | Keeps running normally | **Retained** |

> "**Dormancy is housekeeping, not a protection.** It only says: after 12 silent periods, stop sending requests and close the SIP as an instruction."

> "**Restarting is never a reset.** A dormant or stopped account that restarts resumes from wherever decay left it. Nothing is re-earned, and nothing is forgiven either."

### 🔴 Stale mechanics — do NOT fold these in

The audit is right that parts of §7.1/§7.2 are written against a superseded scoring rule. Precisely:

| Element | Where | Status |
|---|---|---|
| "**Continuity halves**" (§7.1 row 4) | §7.1, §7.2 bullets 3–5, 7 | **DEAD.** Decision 46 replaced the whole formula with `min(Record, Standing) × Retention`. There is no Continuity component and no halving. A miss now costs **8.33 points of Standing** and returns when the 12-month window rolls. |
| "**Arrears cleared inside 12 months → Restored per the §11 revival rule**" (§7.1 row 5) | §7.1, §7.2 bullets 6–7 | **DEAD.** Decision 46a item 2: "**the 🔴 revival question is resolved by deleting revival entirely (Abdur's call):** a missed period is permanently missed, there is no arrears mechanism, and money arriving after grace is offered as a spot purchase." Confirmed again at `_draft_ics-scoring.md` §10: "**No revival or arrears mechanism.** A missed month is missed; late money is a spot purchase (§4)." |
| "**Tenure**" as a score component | §7.1, §7.2, §8 columns | **DEAD.** Replaced by `Months` (never falls, for any reason). The §8 table's "Continuity / Tenure" columns are legacy vocabulary. Read them as: Regulatory block freezes **Months and Recent**; Stop and Dormant let **Recent** decay while **Months** is held. |
| The **arrears fix-on-clearing** rule | §7.2 bullet 7 | **Moot.** Decision 36: "⚠ Decision 36's 'arrears clear as one payment' is moot with revival's deletion." |

**Still live from §7.1/§7.2:** rows 1, 2, 3, 6; the 5-day grace with weekend-rolling and month-boundary rules; the "one accepted payment settles the period" convention; the hard USD 20 floor rejection.

**What the model must do with it.**
1. **Expand the cohort state machine from three states to six.** The brief's `CONTRIBUTING → REDUCED → LAPSED` is insufficient. The real structure is:
   - `PRE-GATE` (run 0–6, no score — see item 4)
   - `CONTRIBUTING`
   - `REDUCED` (at the USD 20 floor)
   - `REGULATORY BLOCK` (**clock frozen both ways** — not a hazard state, an absorbing-delay state that consumes no periods)
   - `STOPPED` (cancelled; Recent decays, Months held, gold retained, **still holds AUM, still spends on the card, still collateral-eligible**)
   - `DORMANT` (**hard absorbing boundary at 12 consecutive silent periods**; SIP instruction auto-cancels, account hold-only)
2. **Add a hard absorbing boundary.** No account may sit in a silent state beyond 12 periods without transitioning to Dormant. This caps the tail of the survival curve and it is a structural fact the current single-hazard engine cannot express.
3. **Split the hazard rate into voluntary and involuntary.** Use the corpus figure: **involuntary is 20–40% of total churn**, base 30%. This matters because the two have different recovery behaviour — an involuntary lapse has a restart probability, a decided stop does not. It also sizes the value of the "log delivery and open events" build requirement.
4. **Critically: STOPPED and DORMANT accounts are not zero-revenue.** They retain gold, so they stay in the AUM stock, the custody-cost base, the B2B/collateral base and, if carded, the interchange base. The brief's `LAPSED` state currently drops them out of everything. **This under-states streams 2, 4, 5 and 6 and over-states nothing.** Add a `holding_not_contributing` population that flows to AUM but not to contribution flow.
5. **Add a restart rate** from DORMANT/STOPPED back to CONTRIBUTING, with resumption at the decayed score, never a reset.
6. **Validation test:** grace crossing the month boundary must never close two periods. A payment on 3 March for a 28 Feb date closes Feb only.
7. **Delete from scope:** any arrears/revival modelling, any continuity-halving logic, any "tenure" component. If the model builder finds these in the corpus, they are audit trail.

**Where it lands in the brief.** **Layer 2 (§3)** — the state machine is rewritten. §8.1 gets F-entries for the 12-period dormancy boundary and the grace conventions. §8.2 gets an involuntary-churn-share scenario variable. §13 gets a new correction: `_draft_sip-rulebook.md` §7.1/§7.2/§8 carry pre-decision-46 vocabulary and should be marked superseded in the corpus itself.

---

## 3. Regulatory-block clock freeze

**What the corpus says.** `_draft_ics-scoring.md` §1.9, verbatim and exactly as reported:

> "**A pause freezes the run; it never breaks it.** Decision 36's regulatory pause was written for accounts already through the gate. **It applies identically before the gate:** a month in which Aurumix refuses the investor's money does not count against them, and pre-gate that means the qualifying run neither advances nor resets. A saver at 4-of-6 who enters a compliance pause resumes at 4-of-6. ... **Frozen months are skipped entirely and the window extends to reach twelve countable months** (§10 item 3, settled): a frozen month is treated as though it never existed, on both clocks."

§10 sub-decision 3 confirms it as settled: "✅ **A frozen month is skipped entirely, as though it never existed, and the window extends to reach 12 countable months** (§1.9). Applies on both clocks and on both sides of the gate."

§10 sub-decision **2** is indeed still open, verbatim:

> "[ ] ⚠ **STILL OPEN, deliberately: a compliance-forced exit (the returning NRI, decision 31) drives Retention to zero for something the customer did not choose.** Decision 36's regulatory pause covers refused *payments*, not forced *sales*. Proposed: **extend the pause to cover forced redemptions** — the grams leave, the score does not move. **Left open at Abdur's instruction 2026-08-13**, not rejected. ⚠ It interacts with item 1: a forced sale and a margin call are both sales the customer did not pick the day of, and the design currently answers them differently."

Item 1 (settled) is the counterpoint: "✅ **Lender liquidation on a margin call counts as a sale** (§1.5). The alternative makes borrowing a route around Retention."

The rulebook §8 adds the trigger detail and an unresolved counsel question:

> "Whether a returning NRI may keep contributing from funds acquired abroad (FEMA s.6(4)) is an open counsel question; if counsel says yes, this state simply fires less often."

**What the model must do with it.**
1. **The ICS engine needs two clocks, not a single month counter.** `Months` and `Recent` must both advance on **countable** months only. Implement a `frozen(t)` flag per cohort; when set, neither clock advances and the trailing window **extends** — the Recent window looks back until it has accumulated 12 countable months, however many calendar months that spans. This is not a pause-and-resume; it is a re-indexing.
2. **This is materially an S5 (India) input.** The regulatory block fires on the returning-NRI event. Add a **repatriation rate** for the S5 and S1–S3 populations — the annual probability an account becomes India-resident. Nothing in the corpus sizes it; flag as exogenous.
3. **Add an open decision as a model switch,** because it swings S5 economics hard:
   - **Switch OFF (current design):** a compliance-forced exit drives Retention to 0, which drives ICS to the Silver floor of 25, which strips the account of card, credit and Gold Rewards eligibility. On the segment most likely to be forced out, the model destroys the tier distribution.
   - **Switch ON (proposed extension):** grams leave, the score does not move; the account keeps its tier.
   Model **OFF as base** (it is the current design) and report the S5 tier-distribution delta under ON. That delta is the client's decision cost.
4. Note the design inconsistency the corpus itself flags: forced sale and margin-call liquidation are answered differently. If the client resolves sub-decision 2, item 1 may move too — a margin-call liquidation currently costs the borrower three tiers, which feeds back into streams 2, 4 and 5.

**Where it lands in the brief.** **Layer 5 (§3)** — the ICS state machine gains a frozen-month re-indexing rule. §6.7 (India segment) gets the repatriation rate and the sub-decision-2 switch. §14 gets the open decision and the FEMA s.6(4) counsel question.

---

## 4. The pre-gate run counter and the nine personas

**What the corpus says.** `_draft_ics-scoring.md` §1.6a, verbatim:

> "⚠ **Build note:** the engine tracks the **current run length** (0–6) before the gate, not a score and not Months. Months and Recent both begin at the first month of the qualifying run (§1.6), so on opening day they are 6 and 6 by construction. Pre-run contributions are still recorded on the ledger as ordinary allocated purchases; they simply never enter the score."

§1.6 supplies the rule that makes it necessary:

> "**What the score reads on the day the door opens: the qualifying run, and nothing before it** (Abdur, 2026-08-13). The scoring history begins at the first month of the run. Payments made before it are real purchases of real gold and they are not erased in any way that matters to the customer, but they are **invisible to the score.**"

> "**Everybody opens at exactly Silver, always**, whether the run was months 1 to 6 or months 9 to 14."

And the consequence the brief cannot currently produce:

> "⚠ **The consequence to state out loud rather than let a customer discover.** A saver who never completes six in a row accrues nothing at all: no score, no tier, no benefits, however many scattered payments they make."

**Correction to the audit's description.** §7.1 is headed "**Six** personas, run under the final formula" but the table has **nine rows, A–I**. The heading is stale; the audit's "nine rows A–I" is correct on substance. The brief's §16 build step 4 already says "verify the tier distribution reproduces the nine personas" — so the brief knows the count but its Layer 5 cannot represent H or I.

Full persona table, verbatim:

| Persona | Months | Recent | Sold | Record | Standing | Ret. | ICS | Tier |
|---|---|---|---|---|---|---|---|---|
| **A.** USD 20/mo, perfect, never sells, month 60 | 60 | 12 | 0 | 100 | 100 | 1.00 | **100** | **Sovereign** |
| **B.** As A but missed one month in the last year | 59 | 11 | 0 | 99.0 | 91.7 | 1.00 | **91.7** | Platinum |
| **C.** USD 2,000/mo, perfect, never sells, month 60 | 60 | 12 | 0 | 100 | 100 | 1.00 | **100** | **Sovereign — same day as A** |
| **D.** Cycler: contributes and redeems every month | 60 | 12 | ~100% | 100 | 100 | **0** | 0 → floor **25** | Silver |
| **E.** Withdrew half at month 36, kept saving | 36 | 12 | 50% | 75 | 100 | 0.714 | **53.6** | Gold |
| **F.** Withdrew everything at month 36, kept saving | 36 | 12 | 100% | 75 | 100 | **0** | 0 → floor **25** | Silver |
| **G.** Withdrew 30% at month 36 (inside the allowance) | 36 | 12 | 30% | 75 | 100 | **1.00** | **75** | **Platinum — no change** |
| **H.** Scattered payer: 6 payments over 3 years, never 6 in a row | 6 | 2 | 0 | — | — | — | **none** | **No tier** |
| **I.** Late opener: paid 1–3, missed 4, paid 5–7, missed 8, ran 9–14 | 6 | 6 | 0 | 25 | 50 | 1.00 | **25** | **Silver on opening day** |

The two rows the brief cannot reproduce, in the corpus's own words:

> "**H is the cost of the consecutive gate, and it is the row to be honest about.** Six real payments, three years of intermittent saving, and the account has no score and no tier because no six landed in a row."

> "**I is the uniform-entry row.** Nine paid months across fourteen calendar months, and the door opens on **Silver at exactly 25** — the same place a flawless month-6 saver opens. The six pre-run payments bought gold and bought no score."

**What the model must do with it.**
1. **Add a pre-gate row block to the ICS engine.** A per-cohort integer `run_length ∈ [0,6]`, incrementing on a counted period, **resetting to 0 on a miss**, **frozen (not reset) during a regulatory block** (item 3). The gate fires when `run_length = 6`; on that period `Months := 6` and `Recent := 6` by construction.
2. **This changes the tier-arrival distribution, not just the presentation.** Under the brief's current Layer 5, everyone who survives to month 6 is Silver at month 6. Under the real rule, a cohort member who misses month 4 does not reach Silver until month 9 at the earliest. **Gate arrival is a distribution, not a date.** With a monthly contribution-success probability `p`, the share gated by month `m` is a run-of-6 first-passage problem — the model must compute it, not assume it. This shifts every downstream ladder date (Gold, card eligibility at M12+, credit, Sovereign at M61) to the right by the expected gate delay.
3. **Add a never-gated population.** Persona H is a real, permanently occupied cell: an account that pays, holds gold, generates AUM and custody cost, pays the **full undiscounted entry fee**, and consumes **zero benefits, forever**. Structurally these are the highest-margin retail accounts in the book. The brief currently has no cell for them and therefore understates stream 1 margin and overstates benefit cost.
4. **Add the zero-benefit paying window.** §10 records it as accepted: "**The zero-benefit paying customer.** Months 1 to 5 pay the full entry fee and receive nothing — no score, no tier, no discount — and longer if the run breaks." The model should report months of full-fee revenue per cohort before the first discount is outstanding.
5. **Build the nine personas as an explicit validation sheet.** Each is a hard-coded input path (months, misses, withdrawal timing and size); the engine must return the stated Record, Standing, Retention, ICS and Tier. This is a pass/fail test set, not a chart. H and I are the two that will fail a naive build, which is exactly why they are the valuable rows.
6. Note the asymmetry the corpus accepted and the model must reproduce: "**Pre-run gold counts in Retention's denominator, while pre-run payments score nothing.**" Grams bought before the gate enter Retention's denominator, so selling them later can cost score that those purchases never earned.

**Where it lands in the brief.** **Layer 5 (§3)** — a pre-gate block above the score. §10.1 gets new rows in the 152–190 ICS block for `run_length` and gate-arrival distribution. §10.2 gets the pre-gate formula pattern. §16 build step 4 already calls for the persona check; upgrade it to a named validation sheet in §11 (Excel structure map).

---

## 5. Float sizing and funding

**What the corpus says.** `_draft_allocation-and-float.md`. Every reported element exists.

The sizing rule, verbatim: "Rule: **float ≥ one bar denomination + a buffer of N days' trailing inflow.** Two bars is the launch setting."

The sizing table:

| | Investors | Monthly inflow | Grams/day | Bar | Days to fill | Float (2 bars) | Float in $ | % of AUM |
|---|---|---|---|---|---|---|---|---|
| Y1 | 500 | $37,500 | ~11 | 100 g | 8.7 | 200 g | ~$22k | ~5% |
| Y3 | 12,000 | $900,000 | ~274 | 1 kg | 3.6 | 3 kg | ~$330k | ~2% |
| Y10 | 80,000 | $6,000,000 | ~1,830 | 12.4 kg | 6.8 | 24.8 kg | ~$2.7M | <1% |

Funding, verbatim:

> "Affordable at launch: ~$22k, against a VARA minimum capital requirement of AED 1.5M (~$408k) that must be posted anyway. **[COUNSEL]** whether allocated gold inventory can sit inside that requirement."

> "**Float as a share of AUM falls as the business scales.** It is a fixed operational requirement, not a proportional drag."

> "**The float is not a cost, it is what buys the wholesale price.** Fabrication premium runs 2 to 5% on 100 g, 1 to 3% on 1 kg, under 1% on Good Delivery. Bar size is the margin dial and float size unlocks bar size."

The Tradeflow issue, verbatim:

> "**Tension to resolve:** DMCC Tradeflow specifies eligible collateral as 1 kg 999.9 bars. If warrants are wanted from launch, 1 kg becomes the effective floor and the launch float rises to ~$220k. Real trade-off, and a client decision."

The who-carries-it fork, which the brief omits entirely:

> "The float has to exist. **Who funds it is open, and it is decided by what the dealer will agree to.**"

| | Dealer-carried | Own float |
|---|---|---|
| Working capital | **Zero** | ~$22k at Y1, ~$330k at Y3 |
| Price-gap risk | Dealer's | Aurumix's, under 0.4% |
| Cost | Wider dealer spread | Narrower once at scale |
| Risk | **Single-counterparty dependency**; the dealer can withdraw | Operational and capital |

> "**Working recommendation: launch dealer-carried, migrate to an own float once volume makes internalising the spread worth the capital.**"

The denomination upgrade rule is already in the brief (T3) and reproduced faithfully there.

⚠ **All float dollar figures are stale.** They are computed at USD 109.31/g. At the brief's verified F1 of USD 141.46/g, the same gram quantities are ~**USD 28k** (Y1, 200 g), ~**USD 424k** (Y3, 3 kg), ~**USD 3.5M** (Y10, 24.8 kg), and the 1 kg Tradeflow launch float is ~**USD 285k**, not 220k. This is brief correction #1 propagating.

**What the model must do with it.**
1. **Add a float sizing row block**, computed not assumed: `float_grams(t) = 2 × bar_grams(t)` under the launch setting, with `bar_grams` driven by the T3 denomination rule already in the brief. Report float in grams and in USD at F1.
2. **Add a float funding line to the balance-sheet/cash view.** The brief charges F5 float cost of capital (0.49/0.31/0.38%) inside stream 1 but never sizes the principal it is a cost of. The two must be consistent: `float_coc_cost(t) = float_USD(t) × coc_rate`. Currently F5 is applied as a % of gross inflow with no derivation — the corpus confirms **"No derivation exists anywhere in the corpus"** is accurate. Deriving it from the sized float is the fix.
3. **Add the dealer-carried / own-float switch.** Under dealer-carried, float capital is **zero**, F5 goes to zero, price-gap risk goes to zero, and the fabrication premium (S7) rises to compensate. Under own float, capital is posted, F5 and price-gap bite, and the premium is narrower. **These are not independent inputs — the brief currently charges both the float cost of capital and the full dealer premium simultaneously, which double-counts under either regime.** This is a real error to flag.
4. **Add the Tradeflow binary as a scenario.** 100 g launch (float ~USD 28k) versus 1 kg forced by Tradeflow warrant eligibility (float ~USD 285k, a **10x** launch capital step). At Year 1 that is a meaningful call on the AED 1.5m capital.
5. **Add the capital-offset counsel question:** whether allocated gold inventory can sit inside the AED 1.5m VARA minimum. If yes, the float is free at Year 1 in cash terms. If no, it is incremental.
6. Recompute all float USD figures at F1 = 141.46.

**Where it lands in the brief.** §6.1 (stream 1 cost build-up) — F5 becomes derived rather than carried. §7 gains a **new subsection 7.5, Working capital and the float**, which the brief has no home for today. §8.1 gets float sizing constants; §8.2 gets the dealer-carried/own-float switch and the Tradeflow binary. §13 gets the double-count correction.

---

## 6. Regulatory capital escalator — and reconciliation against the brief

**What the corpus says.** `_draft_entities-licensing-and-payments.md`.

The rule text, from the licensing comparison table (§ around line 49), verbatim:

> "| Minimum paid-up capital | AED 1,500,000 | AED 1,500,000 **or 2% of average Reserve Asset market value over the preceding 24 months**, whichever is higher |"

The two columns are Option A (direct-ownership ARVA) and Option B (stable-value ARVA with Reserve Assets). The escalator attaches to **Option B only**.

The escalator argument, verbatim:

> "3. **The capital arithmetic is material.** At the Year 10 target of 60,000 to 100,000 investors, reserves could plausibly reach USD 200M. Two percent of that is USD 4M of permanently locked capital. Under Option A there are arguably no Reserve Assets to take 2% of, so the floor stays at AED 1.5M. **This is a multi-million dollar difference and it is a second, financial reason to choose direct ownership.** ⚠ Whether the 2% component can bite where no Reserve Assets exist is a counsel question with real money attached."

Restated as an open item at §"Open items": "Whether the **2%-of-Reserve-Assets capital component** can bite where a direct-ownership ARVA has no Reserve Assets. **Potentially several million dollars.**"

§3.5 "Indicative cost to reach launch", verbatim table and total:

| Item | Indicative |
|---|---|
| VARA application, Category 1 Issuance | AED 100,000 |
| VARA annual supervision | AED 200,000 per year |
| Minimum paid-up capital | AED 1,500,000 (locked, not spent) |
| Smart contract audit, 9 contracts | USD 75,000 (the client's own figure, and it is realistic) |
| Legal opinions: title transfer, token classification, India perimeter | NOT ESTABLISHED. Budget generously |
| DIFC or ADGM holding vehicle | Setup plus annual maintenance |

> "Approximately **USD 550,000 to 750,000 of capital and fees before any build cost**, and six to nine months minimum. ⚠ **VARA publishes no approval timeline.**"

### Reconciliation against the brief

The two totals are **not in conflict — they measure different things**, and the brief is right on its own terms but incomplete:

| Line | Corpus §3.5 | Brief §7.4 one-off | Brief elsewhere |
|---|---|---|---|
| VARA application AED 100,000 | included | **USD 27,200 ✓** | — |
| Smart contract audit USD 75,000 | included | **USD 75,000 ✓** | flagged recurring in correction #10 |
| DMCC incorporation | not itemised | USD 3,280 | — |
| ADGM SPV | "DIFC or ADGM holding vehicle" | USD 1,900 | ⚠ route 2 is now **DIFC**, not ADGM |
| Licensing support | not itemised | USD 20,000 | — |
| VARA annual supervision AED 200,000 | included in the 550–750k | **excluded (correctly)** | F14, and §7.4 opex at USD 54,500 Y1 |
| **Minimum capital AED 1.5m (~USD 408k)** | **included in the 550–750k** | **excluded** | F15: "**Locked, not expensed. Do not run through P&L**" |
| Legal opinions | "NOT ESTABLISHED. Budget generously" | **absent** | — |
| **2%-of-Reserve-Assets escalator** | the multi-million question | **absent** | — |

**The arithmetic that reconciles them.** Corpus USD 550–750k ≈ USD 408k locked capital + USD 27k application + USD 75k audit + USD 200k/yr supervision + the vehicle and unpriced legal opinions. The brief's USD 127,380 is **cash spent, one-off, excluding locked capital and excluding annual fees** — a different and correct measure for a P&L. F15's treatment (locked, not expensed) is also correct.

**What the brief is therefore not counting, and should:**
1. **Legal opinions.** The corpus says "NOT ESTABLISHED. Budget generously" and names three (title transfer, token classification, India perimeter). The composability draft adds a fourth workstream (trust deed drafting, six counsel questions). **The brief has no legal/counsel line in one-off cost and none in opex** — see item 10.
2. **The AED 1.5m as a funding requirement**, distinct from a cost. F15 correctly keeps it out of the P&L, but the model has no cash/funding view where it appears at all, and the float (item 5) may or may not sit inside it.
3. **The 2% escalator as a contingent liability.**

**What the model must do with it.**
1. **Add a capital requirement row, computed:** `required_capital(t) = MAX(AED 1,500,000, 0.02 × trailing_24m_avg_reserve_assets(t))`, behind an **`OPTION_B` switch defaulting OFF**. Under Option A (the chosen route) it returns the AED 1.5m floor at every period and the row is flat — which is precisely the point. Turning the switch ON shows the client the counterfactual: at USD 200M of reserves the requirement is **USD 4M**, an incremental **~USD 3.6M of permanently locked capital**.
2. **Reprice it as an opportunity cost, not a cost.** Locked capital does not hit the P&L, but it earns nothing. At the model's own cost of capital the Option B escalator carries a real annual drag. Report `(required_capital − AED 1.5m) × coc` as a memo line, not a P&L line.
3. **Cross-check the escalator against the brief's own Year 10 AUM.** The corpus's "USD 200M reserves" should be validated against the model's computed Year 10 AUM at 60,000–100,000 investors and F1 gold. If the model's AUM is materially different, the USD 4M figure moves with it. This is a live check, not a quoted constant.
4. **Add a funding/capital view** distinct from the P&L: AED 1.5m minimum capital + float principal + one-off launch spend, with the counsel question on whether the float sits inside the minimum.
5. **Add a one-off legal opinion line.** Nothing in the corpus prices it. Flag as unpriced with an explicit placeholder — the brief currently reads as if legal cost is zero.
6. **Correct ADGM → DIFC** in the brief's one-off table. Decision 50 and the composability draft settle route 2 as DIFC (and §7.1 of the credit draft says taking security "breaks the tie decisively toward DIFC"). The USD 1,900 ADGM SPV line is the wrong vehicle.

**Where it lands in the brief.** §7.4 one-off table gets the legal line and the ADGM→DIFC correction. A **new §7.6, Regulatory capital and the funding view**, carries the escalator and the AED 1.5m. §8.1 F15 gets the Option A/B conditional. §14 gets the "can 2% bite with no Reserve Assets" counsel question. §13 gets the ADGM/DIFC correction.

---

## 7. The tenure rebate — **the audit understated this; the mechanism is retired, not unsized**

**What the corpus says.** `_draft_purchase-structure.md` §5.2 describes the mechanism in full, exactly as reported:

> "**The replacement: a tenure rebate.** Charge the full fee at entry, where nothing prohibits it, and pay part of it back in grams for holding."

| | Old design (prohibited) | New design |
|---|---|---|
| Spot entry fee | 4 to 5% | **Flat, top of range** |
| Exit before 12 months | Fee decaying from ~1.5% to zero | **No fee.** Unvested rebate forfeited |
| Exit after 12 months | No fee | **No fee, and the rebate is paid in grams** |
| Where the money is charged | On the way out | **On the way in** |
| Legal status | Prohibited by III.E.4 | Permitted. A fee rebate, not a distribution |

> "It must satisfy the same four rules as Gold Rewards (decision 6), and it does: **funded from the fee line and never from profit; capped at the fee that customer actually paid; earned by tenure, which is behaviour, not by amount; and never described as yield, interest or return.**"

> "**Lot accounting, which this now requires.** The rebate vests per purchase lot at 12 months. Lots consume **FIFO** on a partial exit. Exiting a lot before it vests forfeits that lot's rebate."

> "⚠ **Tenure attaches to the account, not to the gram.** Grams received by transfer start a fresh clock in the receiving account. Otherwise the rebate is farmable by circulating tokens between accounts."

### The audit's §9 item 6 finding is confirmed — and the real position is stronger

**Verified, point by point:**

- **"Rebate room is 0.10–0.75%" is wrong.** 0.10–0.75% is the **Gold Rewards** range. Decision 6: "Realistic size: **0.10 to 0.75% by tier at launch.**" It is decision 6's number for a different, card-funded benefit. (Its settled ladder in `_draft_ics-scoring.md` §6.4 is now 0.15% → 0.75%.)
- **"~1.5%" is the superseded decaying redemption fee.** The only "~1.5%" in the purchase-structure draft is `_draft_purchase-structure.md` §5.2 line 355: "Fee decaying from **~1.5%** to zero" — the **old, prohibited** design, in the column headed "Old design (prohibited)". It was never a rebate size.
- **The tenure rebate has no published sizing anywhere in the corpus.** Confirmed by search.

**But the audit stopped one step short. The mechanism is retired, not merely unsized.** Decision 44 (2026-08-10), verbatim:

> "✅ **The ICS benefit set is finalised at five, and the tenure rebate is retired (2026-08-10, agreed with Abdur).** ... **Retired: the tenure rebate.** It was designed as the legal replacement for the dead spot redemption fee before Retention existed; **its job (rewarding holding) is now structural, because holding keeps R at 1.00, which keeps the tier, which prices everything else, and every flip already pays the entry-fee toll.** Retiring it **halves the funding question: the entry-fee uplift now funds only the discount ladder.** ... the parked mechanism stays in the file as audit trail."

Corroborated in two places. Decision 41: "⚠ **Holds only while the tenure rebate stays parked**, since that mechanism was spot-only and vested per lot." And `Aurumix_Process_Maps_Redemption.md`: "**FIFO lot accounting is no longer required** while the rebate is parked, since the rebate was the only thing FIFO decided. Grams are fungible for settlement. **Reinstate only if the rebate returns.**"

`_draft_purchase-structure.md` §5.2 is dated 2026-08-06 — **four days before decision 44 retired it.** The section is audit trail.

**The tenure rebate's actual constraint.** There isn't one, because there is no rebate. If it were revived, the constraint would be the four decision-6 rules — chiefly **capped at the fee that customer actually paid**, i.e. the rebate can never exceed the spot entry fee, and it must be funded by an entry-fee uplift on the spot lane rather than from margin. That is a ceiling of the full spot fee (5% at Y1), not a range. Any specific number would be new work, not extraction.

**What the model must do with it.**
1. **Delete solver item 6 from §9, or restate it.** The brief's eight-parameter solver currently contains a parameter for a retired mechanism, sized with another benefit's range against a superseded fee. As written it is three errors compounded. **Recommend: replace with "Tenure rebate — RETIRED by decision 44. No solve required."** and note the freed capacity.
2. **Take the funding relief.** Decision 44: retiring the rebate "**halves the funding question: the entry-fee uplift now funds only the discount ladder.**" This directly improves solver item 1, which the brief flags as its one unresolved arithmetic conflict (1.5pp ceiling versus 0.72% margin). Combined with `_draft_ics-scoring.md` §6.1 — "**holding the headline at 5% may fund the entire ladder with no uplift at all**" — item 1's answer may be **zero uplift**. That is a materially different conclusion from the brief's current framing.
3. **Do not build FIFO lot accounting.** Decision 41 makes grams fungible; no ordering rule is needed on a partial exit. The model needs no lot-level tracking. This is a real build-scope saving.
4. **Keep one contingency note:** if the rebate is ever revived to fill the empty third lever (item 9), it must be made **channel-agnostic and driven off lot date**, per decision 41, or every gram must be tagged by channel for the life of the account.

**Where it lands in the brief.** §9 solver item 6 — rewritten or struck. §9 item 1 — revised toward a possible zero-uplift answer. §7.2 benefit-cost table — no tenure rebate row (correctly absent today; keep it absent). §13 — a new correction recording the §9 item 6 conflation.

---

## 8. The spot lane, and the authoritative resolution of the conflict

**What the corpus says.**

`_draft_purchase-structure.md` §4.1, verbatim:

> "A spot purchase runs through the identical nine stages in section 2.1. Stage 1 is an order rather than a schedule. **That is the only mechanical difference.** The gold is identical, the fix is identical, the receipt is identical, the settlement is identical."

§4.2 "Large tickets, which are the useful ones", verbatim:

> "A large spot order is the **inverse of the lumpiness problem the float exists to solve**. A USD 100,000 order funds roughly 915 grams outright, nearly a full kilobar, at a single fix with a single rail event."

| Ticket band | Handling |
|---|---|
| Small | Standard flow. Below the **AED 3,500** Travel Rule threshold |
| Above AED 3,500 (~USD 950) | Travel Rule data applies |
| Above AED 50,000 (~USD 13,600) | Above the AANI per-transaction cap. Domestic transfer or wire. Enhanced due diligence, source of funds |
| Above roughly one bar denomination | **Procure directly rather than drawing the float** |

> "The last row is a mechanism, not an operational note. **A single order larger than the float would breach the backing invariant and halt minting for everyone else.** Above a defined threshold the purchase is quoted as a two-step: price indication, then execution against a same-day dealer purchase."

Note the 915 g figure is computed at USD 109.31/g. At F1 = 141.46, USD 100,000 net of a 5% fee buys ~**672 g**, not 915. Same qualitative point (still most of a kilobar), different number.

`_draft_sip-rulebook.md` §1, the comparison table:

| | SIP contribution | Spot purchase |
|---|---|---|
| What triggers it | A schedule the investor declared | A one-off order |
| Earns ICS | **Yes** | **No** |
| Counts toward Confirmed SIP | Yes | No |
| Entry fee | Base rate, **discounted by tier** | Base rate, **discounted by the same tier**. See §1.1 |
| Credit, card, family features | Yes, by tier | Not earned by spot, but applies to all grams once earned |
| Counts in Retention | **Yes, both sides** | **Yes, both sides** |
| **The gold** | **Identical** | **Identical** |

Three governing rules, verbatim:

> "**Earning and spending are separate.** Only SIP contributions *earn* tier. Once earned, the tier is an account attribute and it *applies* to everything the account does."
> "**Extra money inside a month is a spot purchase.** It buys gold, it counts in Retention, it earns no period. This is what stops twelve payments in January becoming twelve periods."
> "**Spot neither helps nor hurts the score.** Spot grams enter Retention on both sides of the ratio, so buying spot cannot raise your rate and holding it cannot lower it."

### Resolving the conflict — the SIP rulebook is authoritative

The conflict is real and the audit describes it correctly. Resolution, on three independent grounds:

**1. `_draft_sip-rulebook.md` §1.1 is a self-labelled correction.** It opens with a `> **Decision.**` block:

> "The tier's entry-fee discount applies to **any** purchase the account makes. ICS accrual stays SIP-only, and spot continues to earn no score, no credit ratio, no card tier and no family features. **Spot does not earn the tier. It is simply priced at the tier the account already earned.**"

And it names what it is correcting: "This closes the tension recorded in `handoff.md` §7: a top-tier saver adding a lump sum currently pays the newcomer rate for giving Aurumix more money." Its own table marks the change: "| **Entry-fee discount** | SIP only | **All purchases. Corrected here** |".

**2. Dates.** `_draft_sip-rulebook.md` mtime 2026-08-12; `_draft_purchase-structure.md` mtime 2026-08-06. The rulebook is six days later.

**3. Decision 44 (2026-08-10) ratifies it** in the decision log: "**(1) entry-fee discount** by tier, **on every purchase including spot** (rulebook §1.1)".

**Therefore `_draft_purchase-structure.md` §4.1's "Flat, top of range, no discount" and §4.3's "no entry-fee discount" are superseded.** So is the §4.1 row "Time lever: Tenure rebate, section 5.2" (retired by decision 44 — item 7). `_draft_sip-spot-and-ics.md` (dated 2026-07-29, and self-labelled "decision draft") is the oldest of the three; its table still shows "Buyback less a fee decaying over 6 to 12 months," which decision 32 killed. **Do not use it for spot pricing.**

**Net authoritative position on spot:**

| Attribute | Spot |
|---|---|
| Price | Base entry fee **less the account's tier discount** — same as SIP |
| Earns ICS / counts to Confirmed SIP | **No** |
| Counts in Retention | **Yes, both numerator and denominator** |
| Credit LTV, card tier, family features | Not earned by spot; **applies to all grams once earned via SIP** |
| Exit | Buyback at the fix, no fee (III.E.4) |
| Time lever | **None.** Retired (item 9) |
| Rail | Push or bank transfer, no mandate. **No collection-failure exposure** |

**What the model must do with it.**
1. **Add a spot inflow channel per segment**, distinct from SIP contribution flow: a spot participation rate and an average spot ticket. Spot volume is currently **entirely absent** from the brief's Layer 3 — `gross_inflow = contributing × ticket + reduced × 20` has no spot term.
2. **Price spot at the same tier-weighted discount as SIP.** Do not build a separate flat-fee lane. This is a one-line change with a real revenue effect: it lowers stream 1 yield on spot volume relative to a naive flat-fee read.
3. **Spot earns no ICS.** Spot volume must not feed `Months` or `Recent`. It **must** feed Retention's denominator and, if sold, the numerator.
4. **Spot has no collection event in the `Net = C × (f − c) − R` equation** in the same way — a spot order is one push with no mandate and no failure mode. Model `R` for spot as a single transfer cost, and note that large spot tickets amortise the fixed rail across a much larger base, making spot **structurally the highest-margin inflow in the model** under §0.2's non-linearity.
5. **Add a large-ticket handling threshold as a constraint, not a cost:** above roughly one bar denomination, procure directly rather than drawing the float. This is a **float invariant**, and the model should test it: a single spot order exceeding the float size breaches backing and halts minting. Given a Year 1 float of ~USD 28k (item 5), a **USD 100,000 order breaches it by 3.5x**. The two-step quote mechanism is therefore live from launch, not a Year 3 concern.
6. **Add the AED 50,000 AANI per-transaction cap** as a rail-routing rule: above it, domestic transfer or wire, plus enhanced due diligence and source of funds. That is a different cost and a different friction from the SIP rail.
7. **Flag the conflict as a corpus correction owed.**

**Where it lands in the brief.** **Layer 3 (§3)** gets a spot inflow term. §6.1 gets spot as a second sub-stream within stream 1, at its own ticket and its own rail cost. §8.2 gets spot participation rate and spot ticket as scenario variables. §13 gets the correction: `_draft_purchase-structure.md` §4.1/§4.3 superseded by `_draft_sip-rulebook.md` §1.1 and decision 44.

---

## 9. The "empty third lever" open decision

**What the corpus says.** `Aurumix_Process_Maps_Redemption.md`, under "Open items this set surfaces", verbatim and as reported:

> "- [ ] 🔴 **The spot 'time lever' is now empty.** `_draft_sip-spot-and-ics.md` differentiates SIP from spot on three levers: price, credit and time. The time lever was a decaying redemption fee, which III.E.4 prohibits. With the tenure rebate parked, **spot and SIP currently differ on two levers, not three.** Either accept two, or design a replacement. This needs a decision before the SIP/spot draft is finalised."

The three levers it refers to, from `_draft_sip-spot-and-ics.md` §2:

> "1. **Price.** The entry fee falls with ICS tier.
> 2. **Credit.** The loan-to-value ratio rises with ICS tier. Spot-only accounts receive none.
> 3. **Time.** Spot grams carry a decaying redemption fee. SIP grams do not."

**A finding the audit did not mention: the price lever has also emptied.** Item 8 establishes that decision 44 and rulebook §1.1 extend the entry-fee discount to spot. So lever 1 no longer differentiates either. Combined with the retired time lever, **spot and SIP now differ on one lever, not two**: credit (and its companions, card tier and family features, which decision 44 groups with it). The corpus's own open item is out of date in the direction of understating the problem.

The related sequencing note, if the rebate is ever revived:

> "- [ ] **If the tenure rebate is revived**, note the sequencing point: crediting a rebate in grams must happen **before** the burn... `_draft_purchase-structure.md` §5.3 currently lists it as step 7, after the burn at step 4, while its own description says 'before the burn'. The table is wrong either way."

**What the model must do with it.**
1. **Carry it as a named open question for the client**, with the model quantifying the cost of each answer:
   - **Accept one lever.** Model spot at the tier-discounted fee with no ICS accrual. This is the current design and the model's base case. Report the resulting spot share of inflow and its stream 1 margin.
   - **Revive the tenure rebate.** Requires FIFO lot accounting (build cost), a channel-agnostic redesign per decision 41, an entry-fee uplift on the spot lane to fund it, and reopens solver item 1's funding question that decision 44 halved. Model as a switch.
   - **Design something new.** Out of scope for Phase 4.
2. **The model's contribution to the decision is the size of the thing being argued about.** Run spot volume as a share of total inflow. If spot is a small share, the empty lever is a low-stakes decision and "accept one" is cheap. If spot is material — and §4.2 argues large spot tickets are "the useful ones" for the float — the differentiation question has real money behind it. **Compute the number, then hand the client the decision.**
3. Note the interaction with item 7: reviving the rebate un-does decision 44's funding relief. The two decisions must be taken together.

**Where it lands in the brief.** §14 (Open questions) gets the lever decision with the model's sizing attached. §9 solver item 6 is where its arithmetic would live if revived (see item 7). §5/§6.1 report the spot share that sizes the stakes.

---

## 10. Composability route costs

**What the corpus says.** `_draft_composability-and-ownership-route.md` §3.1, verbatim, both costs:

> "**Cost 1: the customer's ownership is beneficial, not legal.** Route 1 would have given legal title, which is stronger. Paxos concedes the same trade for PAXG, calling it 'beneficial ownership... akin to a warehouse receipt', and that is the largest gold token in the market. It is the industry-normal position and it is defensible, but the marketing must not say 'you own the bar outright' in a way that only route 1 would support."

> "**Cost 2: route 2 creates a fund-classification question that route 1 does not.** A DIFC vehicle holding property for many participants invites the question whether it is a Collective Investment Fund under DIFC Law No. 2 of 2010. Art 11 requires the purpose or effect to be participation in **profits or income** arising from acquisition, holding, management or disposal, plus either pooling or management as a whole. Allocated gold that produces no income, is not managed, and where each customer's grams are fixed, does not meet Art 11. **Note what this retrospectively justifies: decision 6 killed the profit-share dividend on securities grounds, and it turns out to have also protected the vehicle from fund classification.** Keep it dead."

And the cost that may not have to be paid:

> "**A cost we expected and may not have to pay.** The DFSA Rulebook appears to exempt from the Licensing Rules a person who is 'a Trustee of a single trust' or 'a non-commercial Trustee'. If that holds, a single-purpose DIFC trustee company holding one trust needs no DFSA trust licence. **Confidence: Medium.** Retrieved from a rulebook mirror, not the DFSA primary text, and the primary page could not be fetched. **Verify before it reaches the client**, because it materially changes the cost of route 2."

**Decision 50** frames it exactly as the audit reported:

> "whether a single-purpose DIFC trustee company needs a **DFSA trust licence** (**a cost question, not a structure question**, and unverified at DFSA primary text)."

Counsel question 5 in §10 makes the modelling consequence explicit:

> "**Is a single-purpose DIFC trustee company exempt from DFSA licensing** as a trustee of a single trust or a non-commercial trustee? *This is a cost question and we cannot quote the client a number without it.*"

§7.2 "Wind-down without a holder list", verbatim:

> "VARA Company Rulebook Part VII.A is mandatory and Cache Gold stranded 96% of supply. But re-read what actually went wrong at Cache Gold: it never burned redeemed tokens, so supply and metal diverged, and it had no way to reach anyone. The failure was operational, not architectural."

> "The answer for an open token is a **published claim window plus burn-on-redemption plus the freeze role**, which is what PAXG relies on and what a liquidator can actually execute. Aurumix additionally has something no gold token has: **a monthly cash touchpoint with the direct-channel book**, so the great majority of holders are contactable by construction."

§9's four-stage path:

- **Stage 1, the September build (no added cost, and it removes cost).** Upgradeable proxy with a transfer-hook stub ("roughly a day of work"), hook shipped as a **blocklist** ("Less code than the allowlist currently planned"), keep freeze/seize/reissue, KYC as a hard precondition of mint and redemption, **multi-tenant capable at register and mint (decision 42)**, list nowhere.
- **Stage 2, counsel (before the licence application).** "Batch 4 must be re-cut."
- **Stage 3, the trust deed.** "Draft the class-defined trust. It is a drafting exercise, not a structuring one, and it is **the only genuinely new legal work this creates.**"
- **Stage 4, after the licence and once the float is deep.** VARA-licensed exchange, then CEX, then DeFi. "Each step is a commercial decision with no rebuild behind it."

Six counsel questions in §10, three marked 🔴, of which question 1 "decides the token, the exchange strategy and the DeFi strategy."

**What the model must do with it.**
1. **Add a legal and trust cost block to opex — the brief has none.** Minimum lines:
   - DIFC trustee company setup, one-off
   - **DIFC trustee company annual maintenance, recurring** — this is the line the brief is most clearly missing
   - Trust deed drafting, one-off, "the only genuinely new legal work"
   - Counsel batches: six re-cut questions in the composability draft, three in the purchase-structure draft, two in the credit draft, plus the three named in the licensing draft
   - **DFSA trust licence, contingent** — behind a switch, defaulting to the exempt reading, with the unexempt case priced as a scenario
2. **Price the DFSA licence question explicitly as unknown.** The corpus is unusually direct: "we cannot quote the client a number without it." The model should carry a placeholder with a visible flag rather than an implied zero. Confidence is Medium and the source is a mirror, not primary text.
3. **Stage 1 is a cost reduction, and the model should show it.** "no added cost, and it removes cost" — a blocklist is less code than the planned allowlist. Net technology cost at the September build should be flat or slightly down, not up. Do not let composability appear in the model as a new expense line.
4. **Add a wind-down provision line.** VARA Company Rulebook Part VII.A is mandatory. The corpus gives the shape (claim window, burn-on-redemption, freeze role) but no cost. Flag as unpriced.
5. **Add the Cache Gold operational requirement as a build constraint:** burn-on-redemption is not optional. It is already implied by the model's `− redeemed(t)` term but should be stated.
6. **Add a memo, not a cost:** the monthly cash touchpoint with the direct-channel book means the majority of holders are contactable by construction. This is a wind-down cost mitigant and a genuine differentiator — worth a line in the client narrative.
7. **Note the interaction with stream 6.** Stage 1 requires multi-tenant capability at register and mint, which is the same Week-1 build requirement the brief already flags for stream 6. One build, two dependencies. Do not double-count the cost.

**Where it lands in the brief.** §7.4 opex table gains a **Legal and trust** block (the "Legal, insurance, contingency" line at USD 60k/120k/400k currently absorbs this invisibly and should be split). §7.4 one-off gains trust deed and counsel batches. §8.2 gains the DFSA-licence switch. §14 gains the DFSA cost question and the three 🔴 counsel questions. §6.6 notes the shared multi-tenant build dependency.

---

## 11. Card and credit operational exposures

**What the corpus says.** `_draft_credit-and-card-infrastructure.md`.

§6.3 "Who is actually exposed — the table to show the client", verbatim:

> "The ladder only binds on customers who max out at the top tier. This is the most reassuring fact in the whole design and it should be presented."

| Tier | Struck LTV | Gold fall needed to reach 92% |
|---|---|---|
| Gold | 50% | **−46%** |
| Platinum | 65% | **−29%** |
| Sovereign | 80% | **−13%** |

> "⚠ **A 13% gold fall is roughly a one-sigma annual move.** Sovereign borrowers at maximum draw are genuinely exposed, and the design must not pretend otherwise. Two mitigations: the population is small and the most disciplined in the book, and the ladder gives them two warnings and 14 days before anything is sold."

§6.4 "The facility review date", verbatim:

> "A term loan matures. A card balance revolves indefinitely. Without a review, a customer struck at Sovereign 80% who has since fallen to Silver keeps borrowing at 80% forever, and the tier ladder stops binding on the largest benefit in the product."

> "**Recommendation: an annual facility review.** The limit re-strikes to the current tier of record; **existing drawn balances run to term at the original struck LTV**, preserving the no-margin-call-on-a-tier-fall promise."

§6.6 "Who sells, and the self-dealing problem":

| Route | Verdict |
|---|---|
| **Aurumix's float absorbs it** | **Recommended.** Fastest, best price, no dealer call on a bad day. This is the float's **fifth job**, and the same argument that made zero-fee redemption survivable |
| Two-way dealer sells physical | Fallback for size beyond the float band |
| Lender's own machinery | Avoid: needs vault and register access, which the DIFC vehicle complicates |

> "⚠ **Aurumix would be valuer, collateral agent and buyer simultaneously.** Cure by mandating the **LBMA fix with zero discretion**, disclosed at the draw, with the sale price and gram count reported to the customer. Without that, **this is the line a regulator or a claimant pulls on.**"

> "⚠ **Counsel question, not raised anywhere previously: is an enforcement sale a 'redemption' under VARA III.E.4?** If it is, no fee may be charged on it, and **the recovery costs in stream 5 become unchargeable.** Our view is that a secured creditor's enforcement sale is not a customer-exercised redemption right. **It has not been tested.**"

§7 "The collateral chain", verbatim: "Five links. Two are strong, three are open."

| # | Link | State |
|---|---|---|
| 1 | **A valid security interest** over the customer's beneficial interest in the gold-holding vehicle | ⚠ **Open** |
| 2 | **Immobilisation** so the collateral cannot walk | ✅ **Strong** |
| 3 | **Valuation and trigger** | ✅ Designed in §6.2 |
| 4 | **Cure** | ✅ Designed in §6.2 |
| 5 | **The sale** | ⚠ Designed in §6.6, self-dealing cure required |

⚠ **The audit's "3 of 5 open" is imprecise.** The header says "Two are strong, three are open" but the table marks **two** as open (⚠ links 1 and 5) and **three** as resolved (✅ links 2, 3, 4). The table is the operative statement; links 3 and 4 are "Designed in §6.2." Read it as **two open, three designed** — a materially better position than the header implies. The header appears to be stale.

§5.1 "The stand-in hole, and it cannot be closed", verbatim:

> "Two independent fallbacks approve transactions **with no collateral check at all**"

| Failure | Who decides | Our control |
|---|---|---|
| **Aurumix unreachable** → processor invokes **Commando Mode** | The processor, from pre-agreed static rules | Partial — we write the static rules |
| **Processor unreachable** → the card network performs **STIP** | The card network, unilaterally, notifying afterwards | **None** |

> "In both paths we learn about the spend after the fact. **This is an unavoidable, permanent hole in a collateral-backed card programme.**"

> "**Recommended Commando Mode rules** (Aurumix's only lever): max **USD 250 per transaction**, max **3 transactions per card**, **decline all ATM withdrawals**, **decline all cross-border**, hard stop after **USD 500 cumulative**. Sized so the worst case on any single account is immaterial against even a Gold-tier facility."

The audit's figures are exact. Decision 180 in the log confirms them and adds: "**Disclose it to the lender rather than discover it with them.** ⚠ The three-second authorisation budget is a real constraint on the September build."

§5.2 adds a related control: "**Recommendation: a 48-hour hold on any redemption request from an account with an active card facility.**"

**What the model must do with it.**
1. **Add a Sovereign-tier collateral stress test.** Not a scenario — a named test. At F1 gold and S6 volatility (25%, base), a −13% move is well inside one sigma. Compute: Sovereign accounts × take-up × drawn-at-maximum × the probability of a −13% annual move, and report the exposed balance. The brief's F1 holds gold flat by design, which is correct for revenue attribution but **means the model as specified cannot see this risk at all.** Use the gold-price sensitivity axis that §8.1 already reserves.
2. **Add the annual facility review as a stock rule in the credit layer.** `facility_limit` re-strikes annually to the current tier; **drawn balances run to term at the originally struck LTV**. This means the model must carry a **vintage of drawn balances by struck LTV**, not a single drawn balance at the current tier. Without it, stream 5 mis-states both revenue and exposure whenever the tier distribution moves — and the brief's own Layer 5 says Sovereign is "rented by conduct," so it moves constantly.
3. **Add a stand-in fraud loss line.** Bounded and computable: `exposed_accounts × USD 500 cumulative cap × incident_rate`. The USD 250/3-txn/USD 500 caps make the per-account worst case deterministic; only the incident rate is unknown. Model it as a small cost with a flagged rate. Note that the caps also **remove ATM and cross-border from stand-in**, which slightly reduces stream 4.
4. **Add the enforcement-sale-as-redemption switch.** If counsel says an enforcement sale is a redemption under III.E.4, **recovery costs in stream 5 become unchargeable**. The brief already flags this at §6.5 as a caveat; make it a switch with a cost, since stream 5's five fee heads are all unpriced anyway.
5. **Do not model liquidation as a physical sale.** §6.6 makes the float the recommended absorber — the float's **fifth job**. This ties to item 1 and item 5: liquidation volume flows into the same net-flow calculation as redemptions, and only breaches of the float band reach the physical market.
6. **Add the self-dealing cure as a build/compliance requirement**, not a cost: LBMA fix with zero discretion, disclosed at the draw, sale price and gram count reported. Nothing to price, but it is the line "a regulator or a claimant pulls on" and belongs in the risk register.
7. **Add the 48-hour redemption hold** for carded accounts as a small operational constraint on redemption timing (interacts with the §5.5 settlement window tiers in item 1).
8. **Correct the collateral chain count** to two open, three designed.

**Where it lands in the brief.** §6.5 (stream 5) gets the vintage-by-struck-LTV structure, the facility review, and the enforcement-sale switch. §6.2/§6.4 get the stand-in fraud line and the ATM/cross-border stand-in exclusion. §8.1 gains the Commando Mode caps as constants. A **new §12.4 or risk annex** carries the Sovereign −13% stress test, since §12's three views are all break-even views and none is a risk view. §14 gets the enforcement-sale counsel question.

---

# Summary of corrections to the audit's descriptions

| Item | Audit said | Actual |
|---|---|---|
| 2 | §7.1/§7.2 partly superseded | **Correct, and larger.** Continuity-halving, revival/arrears, and "Tenure" as a component are all dead per decision 46/46a. Rows 4 and 5 of the six-row ladder are entirely stale. |
| 4 | §7.1 has "nine rows A–I" | **Correct on substance.** The heading reads "Six personas" but the table has nine. Heading is stale. |
| 7 | Tenure rebate "has no published sizing" | **Understated.** Decision 44 (2026-08-10) **retired** it. `_draft_purchase-structure.md` §5.2 (2026-08-06) is audit trail. Brief §9 item 6 should be struck, not solved. The audit's diagnosis of the 0.10–0.75% / ~1.5% conflation is exactly right. |
| 8 | Conflict between rulebook §1.1 and purchase-structure §4.3 | **Correct.** Rulebook §1.1 wins: self-labelled correction, six days later, ratified by decision 44. |
| 9 | Spot and SIP differ on two levers not three | **Correct as written in the corpus, but now out of date.** Decision 44 also extended the price lever to spot, so they differ on **one** lever, not two. |
| 11 | §7: "3 of 5 collateral-chain links open" | **Imprecise.** Header says three open; the table marks **two** open (links 1, 5) and three designed. Table is operative. |

**Two cross-cutting numeric issues.** Every dollar figure in `_draft_allocation-and-float.md` (float sizes, price-gap) and the 915 g spot example in `_draft_purchase-structure.md` §4.2 is computed at **USD 109.31/g**. At the brief's verified F1 of 141.46 the float is ~29% larger in USD and the 915 g becomes ~672 g. This is the brief's own correction #1 propagating into material the brief had not yet extracted. And the brief currently charges **both** the float cost of capital **and** the full dealer fabrication premium, which double-counts under either the dealer-carried or the own-float regime — a new correction owed.agentId: a8026626bcbd88688 (use SendMessage with to: 'a8026626bcbd88688' to continue this agent)
<usage>subagent_tokens: 137121
tool_uses: 40
duration_ms: 460478</usage>