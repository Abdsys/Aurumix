# Aurumix Revenue Model - Validation

---

## 1. Persistency calibration against all five anchors

The task asked that survival **emerge** from archetype heterogeneity rather than a constant hazard, and be calibrated to reproduce 55/40/30/24/19% at M13/25/37/49/61.

| Anchor month | Target | Sourced weights | Calibrated | Calibrated residual (pp) | Sourced residual (pp) |
|---|---|---|---|---|---|
| 13.0000 | 0.5500 | 0.5344 | 0.5438 | -0.6200 | -1.5600 |
| 25.0000 | 0.4000 | 0.4043 | 0.4083 | 0.8300 | 0.4300 |
| 37.0000 | 0.3000 | 0.3078 | 0.3092 | 0.9200 | 0.7800 |
| 49.0000 | 0.2400 | 0.2355 | 0.2359 | -0.4100 | -0.4500 |
| 61.0000 | 0.1900 | 0.1811 | 0.1814 | -0.8600 | -0.8900 |

- **RMSE with the parameter file's sourced weights: 0.919pp**
- RMSE after free calibration: 0.752pp

### 1.1 The requirement-2 vs requirement-3 tension, quantified

This is the finding flagged before the build began, and it is real.

The parameter file's archetype weights are reasoned **bottom-up** from payment behaviour. The five survival anchors are derived **top-down** from IRDAI persistency adjusted for the absence of a lock-in. They were produced independently, so there is no guarantee they reconcile.

**They very nearly do.** The sourced weights reproduce all five anchors to within 1.56pp, RMSE 0.919pp. That is a genuinely good independent agreement and it is the single most reassuring result in this validation.

**Free calibration was run and then rejected.** It improves RMSE by only 0.167pp, and it buys that by destroying the archetype structure:

| Archetype | Sourced weight | Calibrated weight | Change |
|---|---|---|---|
| Perfect payer | 0.100 | 0.115 | 0.015 |
| Occasional misser | 0.350 | 0.302 | -0.048 |
| Alternating misser | 0.120 | 0.305 | 0.185 |
| Reducer | 0.130 | 0.000 | -0.130 |
| Early lapser | 0.300 | 0.278 | -0.022 |

Background hazard: sourced 0.0160 -> calibrated 0.0134.

**The calibrated fit drives the Reducer archetype to zero and inflates the Alternating misser from 12% to 30%.** Both are corpus-attested behaviours - the Reducer is the entire justification for the free unscored reduction (`_draft_sip-rulebook.md` §6.2), and the Alternating misser's Gold-for-life cap is proved in `_draft_ics-scoring.md`. A curve fit that deletes the Reducer is fitting noise, not behaviour.

**Decision: the model uses the SOURCED weights, not the calibrated ones.** A 0.17pp RMSE improvement does not justify discarding the mechanism design. Both are reported here so the choice is visible and reversible.

**Which is more likely wrong, if they had disagreed badly?** The anchors. The archetype weights are at least reasoned from a described mechanism with named behaviours; the anchors are an IRDAI curve for a *different product in a different country with a different lock-in regime*, adjusted by judgement. The parameter file itself rates the aggregate Medium and the decomposition Low, but that rating is about the decomposition's *evidential support*, not its internal coherence. Neither is strong enough to override the other, which is exactly why the residual is reported rather than eliminated.

### 1.2 S2 bounds and the extension to M120

| Scenario | M13 | M25 | M37 | M49 | M61 | M85 | M120 |
|---|---|---|---|---|---|---|---|
| Base | 53.4% (t 55%) | 40.4% (t 40%) | 30.8% (t 30%) | 23.6% (t 24%) | 18.1% (t 19%) | 10.8% | 5.3% |
| Aggressive | 64.5% (t 65%) | 52.6% (t 52%) | 43.3% (t 42%) | 35.8% (t 35%) | 29.8% (t 29%) | 20.9% | 12.8% |
| Conservative | 44.0% (t 45%) | 30.0% (t 29%) | 20.7% (t 20%) | 14.3% (t 14%) | 10.0% (t 10%) | 4.9% | 1.8% |

v1.0 stops at M61 and its annual block has no survival rule at all. The curves above run the full 120 months. **M120 survival at Base is 5.3%** - the tail is set almost entirely by the background hazard, not by archetype composition.

### 1.3 Why a constant hazard cannot do this

At the M13 anchor of 55%, a constant monthly hazard is `h = 1 - 0.55^(1/12) = 0.0486`. Propagated to M61 that gives `(1-h)^60 = 5.0%` against the 19% target - it destroys roughly two-thirds of the terminal book. Using the brief's §10.2 `1/13` root instead gives `6.3%`, no better. Heterogeneity is not a refinement here; it is the only thing that fits.

**Root convention:** the model uses `1/12` throughout. The M13 anchor spans 12 hazard opportunities (M1->M13), so 1/12 is correct. v1.0's §1 says 1/12 and its §10.2 says 1/13; they cannot both hold.

---

## 2. ICS persona reproduction (A-I)

| Persona | Description | Expected ICS | Model ICS | Expected tier | Model tier | Pass |
|---|---|---|---|---|---|---|
| A | USD 20/mo, perfect, never sells, month 60 | 100 | 100 | Sovereign | Sovereign | PASS |
| B | As A but missed one month in the last year | 91.7 | 91.67 | Platinum | Platinum | PASS |
| C | USD 2,000/mo, perfect, never sells, month 60 | 100 | 100 | Sovereign | Sovereign | PASS |
| D | Cycler: contributes and redeems every month | 25 | 25 | Silver | Silver | PASS |
| E | Withdrew half at month 36, kept saving | 53.6 | 53.57 | Gold | Gold | PASS |
| F | Withdrew everything at month 36, kept saving | 25 | 25 | Silver | Silver | PASS |
| G | Withdrew 30% at month 36 (inside the allowance) | 75 | 75 | Platinum | Platinum | PASS |
| H | Scattered payer: 6 payments over 3 years, never 6 in a row | no score | no score | None | None | PASS |
| I | Late opener: paid 1-3, missed 4, paid 5-7, missed 8, ran 9-14 | 25 | 25 | Silver | Silver | PASS |

**9/9 personas reproduce exactly.**

H and I are the two rows a naive build fails, and both pass:
- **H** (scattered payer, 6 payments over 3 years, never 6 in a row) returns *no score and no tier at all* - not a floor of 25. The model represents 'never gated' as a distinct state, not as Silver.
- **I** (late opener) gates at M14 with Months = 6 and Recent = 6 by construction, opening on Silver at exactly 25 - the same place a flawless month-6 saver opens. The six pre-run payments bought gold and bought no score.

### 2.1 Gate and clock mechanics

| Check | Expected | Model | Pass |
|---|---|---|---|
| Persona I gate fires at M14 with Months=6, Recent=6 | gated=True months=6 recent=6 tier=Silver | gated=True months=6 recent=6 tier=Silver | PASS |
| Persona H never gates (no score, no tier, ever) | gated=False tier=None | gated=False tier=None | PASS |
| Regulatory block freezes the pre-gate run (4-of-6 resumes at 4-of-6) | run_length=4 after 6 frozen months | run_length=4 (was 4) | PASS |
| Frozen months are skipped entirely on both clocks | months unchanged at 6 | months=6 | PASS |
| Dormancy absorbs at 12 consecutive silent periods | dormant=True | dormant=True silent=12 | PASS |
| Exact fractions: Standing(Recent=6) reaches Gold, not Silver | Standing=50 exactly -> Gold | exact=50.0 (naive 8.3333x6=49.9998 -> Silver) | PASS |
| Alternating misser is permanently capped at Gold | tier=Gold | months=66 recent=6 tier=Gold | PASS |

**The exact-fraction check is the one that matters most.** With the rounded `8.3333 x 6 = 49.9998`, the alternating misser falls below the Gold threshold of 50 and 12% of every vintage silently misclassifies to Silver - changing card eligibility, interchange rate, benefit cost and credit eligibility for that entire cell. The model uses `Fraction(100,12)` so Standing at Recent=6 is exactly 50.

---

## 3. Invariant checks

Asserted at runtime **every period**, for all 120 months x 10 scenarios. Any breach raises `InvariantError` and halts the run.

| Invariant | Statement | Tolerance | Result |
|---|---|---|---|
| Population conservation | opening + new = closing across all five states | 1e-6 | PASS |
| No negative population | every state >= 0 in every period | 1e-9 | PASS |
| Tier counts sum to accounts | sum(tier counts) = contributing + reduced | 1e-6 | PASS |
| Grams reconcile | opening + bought - withdrawn - redeemed = closing | 1e-6 | PASS |
| No negative stocks | grams closing >= 0 | 1e-9 | PASS |
| Seasonality normalisation | acquisition and card-spend vectors sum to exactly 12.00 | exact | PASS (12.00 / 12.00) |
| Cost bridge closes | sum(cost components) = total_cost | 1e-6 | PASS (max residual 4.66e-10) |
| Gross revenue non-negative | revenue is fees earned, never a net margin | 1e-9 | PASS |

Note on the AUM driver: the model asserts that AUM scales with `holding` (contributing + reduced + lapsed-holding + dormant) and **never** with `live_accounts`. The explicit driver map is in `cohort.DRIVER_MAP`.

---

## 4. Source conflicts and how each was resolved

Precedence applied throughout: **corpus > parameter file > v1.0 brief.**

| Topic | Corpus says | Parameter file says | v1.0 brief says | Resolution |
|---|---|---|---|---|
| Monthly hazard root convention | n/a | n/a | 1.0 says h=1-S^(1/12); 10.2 says h=1-S13^(1/13) | Used 1/12. The M13 anchor spans 12 hazard opportunities. Per task spec. |
| Reduced-state ticket | n/a | S29: 50% of prior ticket floored at USD 20 | 3 Layer 3 hard-codes reduced x 20 | Used S29. The brief's hard-coded 20 is a real error; the floor is the hard minimum (F6), not the observed landing point. |
| LAPSED is terminal | extract item 2: STOPPED/DORMANT retain gold, AUM, custody, card | S33 lapsed-holder redemption multiplier | Layer 2 treats LAPSED as dropping out of everything | Used corpus. LAPSED-HOLDING stays in AUM, custody, screening and (per the LAPSED_KEEPS_CARD switch) the interchange base. |
| Spot entry-fee discount | _draft_sip-rulebook.md 1.1 + decision 44: tier discount on ALL purchases | Block F prices spot at the tier discount | brief models no spot lane at all | Used corpus. _draft_purchase-structure.md 4.1/4.3 ('flat, top of range') is superseded - six days older and overridden by decision 44. |
| Tenure rebate | decision 44 (2026-08-10) RETIRED it | not carried | 9 solver item 6 asks the model to size it | Struck. No rebate is modelled and no FIFO lot accounting is built (decision 41 makes grams fungible). |
| Float cost of capital double-count | extract item 5: charging float CoC AND the full dealer premium double-counts under either regime | S51 dealer-carried at launch | F5 charges 0.49% float CoC as a flat % of inflow with no derivation | Float CoC is DERIVED from the sized float, and set to zero while the float is dealer-carried (to Y3). The flat F5 rate is not used. |
| Stream 5 drawn balance | Manappuram realised tenor 71 days | S40 turnover factor 0.42 | 6.5 computes peak drawn and prices it as persistent | Applied S40 to the interest component only; origination is per-event and rises with turnover. Roughly halves stream 5. |
| Collateral chain open links | table marks 2 open (links 1,5), 3 designed | n/a | header says 'three are open' | Recorded as 2 open / 3 designed. Header is stale; the table is operative. |
| ADGM vs DIFC holding vehicle | decision 50 + composability draft settle route 2 as DIFC | n/a | 7.4 one-off table lists an ADGM SPV | Booked as DIFC SPV. Same cost, corrected label. |

---

## 5. DERIVED_BY_MODEL parameters

Values this model had to choose because **no source states them**. Each is flagged in `params.py` via `derived()` and collected here automatically. This is the audit surface: a spine that looks sourced but is not is the exact failure being replaced.

| Parameter | Value | Rationale | Confidence |
|---|---|---|---|
| dealer_two_way_spread | 0.01 | Corpus gives the net-flow spread mechanism but never a spread rate. 1.0% two-way is a mid-market bullion dealer round-trip on 100g-1kg bars, consistent with the 3% fabrication premium on smaller denominations. | Low |
| S6 penetration ceiling | 0.06 | S22 leaves S6 as 'n/a' and BRIEF 5 does not size the S6 base. Set the S6 addressable base at 50,000 and its ceiling equal to S4's, since both are small international perimeters requiring local licensing. | Low |
| marketing_spend_by_year | {1: 60000, 2: 150000, 3: 250000, 4: 320000, 5: 400000, 6: 480000, 7: 560000, 8: 640000, 9: 720000, 10: 800000} | The opex table treats Marketing as a cost block but S48/G1 says it is a decision variable and an INPUT to acquisition. Neither source gives a monthly path. Anchored on the brief's Y1/Y3/Y10 opex marketing line and interpolated straight-line (log-linear is undefined from a zero base). | Low |
| early_lapser_post_gate_hazard | 0.03 | S27 gives the early lapser a 0.200 own hazard and says '~90% gone by M13' but does not say what the residual does afterwards. Holding 0.200 forever drives the archetype to zero and removes it from the M25+ mix entirely, which over-thins the tail. Decayed to 0.030 from M13. | Low |
| card_spend_segment_exponent | 0.55 | No source splits card spend by customer income band. Ticket is used as an income proxy, compressed by an exponent of 0.55, turning the 3.75x S3->S1 ticket spread into a ~2.1x card-spend spread. Consumption rises sub-proportionally with income (Engel-curve behaviour) and 0.55 sits mid the 0.4-0.7 range usually fitted to it. Normalised so the book-weighted mean equals the AED 6,000 S4 anchor: it redistributes, never rescales. | Low |
| credit_apr | 0.125 | BRIEF 6.5 gives a UAE pricing corridor of 9% (Emirates Money) to 16% (Finance House) but never picks a point. Midpoint 12.5%; Aurumix takes CREDIT_INTEREST_SHARE_PP of it, not the whole rate. | Medium |
| family_avg_names | 3.2 | Pricing includes up to 4 beneficiaries; no source gives the observed mean. 3.2 assumes most households register spouse + 2 children and a minority add a parent. | Low |
| spot_tenure_uplift | 0.3 | S45 says a 3-year account is 'roughly 2x as likely' to buy spot as a 6-month account but gives no functional form. Linear +30%/yr of tenure, capped at 2.0x, reproduces that ratio at 3 years. | Low |
| vault_pricing_regime | ad_valorem | S14 and the brief's 7.4 verified range are both stated as a PERCENTAGE of value, so ad valorem is the sourced regime. The DGCX USD 0.10/kg/day tariff is a different vendor archetype quoted for wholesale bar storage. v1.0 took the cheaper of the two, which is not a quote anyone offers and understates Y10 vault cost by roughly 10x. | Medium |
| opex_anchor_holding_ratio | {1: 1.35, 3: 1.9, 10: 3.0} | The brief's opex anchors are contributing counts (7.4 'cost per investor' row + 14 default). Blocks that scale with the HOLDING book need a holding count at those same anchors, which v1.0 never computed because it treated LAPSED as terminal. Ratios are taken from this model's own computed contributing:holding trajectory (1.35x at Y1 rising to ~3.0x at Y10). | Medium |
| legal_opinions_and_trust_deed | 150000.0 | Corpus says 'NOT ESTABLISHED. Budget generously' and names 3 opinions plus a trust deed and 6 counsel batches. The brief carries ZERO legal cost, which reads as if legal is free. USD 150k one-off is a visible placeholder, NOT a quote. Booked M1-M12. | Low |

---

## 6. What could not be reconciled

Reported honestly with numbers rather than forced.

1. **The block-level Opex(N) decomposition does not tie exactly to the brief's published totals.** Evaluated at v1.0's own anchor points (500/12,000/80,000 contributing) the fitted blocks give:

| Anchor | Contributing N | Holding N | Fitted opex | Brief anchor | Delta % |
|---|---|---|---|---|---|
| Y1 | 500.0 | 675.0 | 1,043,223.1 | 894,800.0 | 16.6 |
| Y3 | 12,000.0 | 22,800.0 | 2,065,797.3 | 2,484,700.0 | -16.9 |
| Y10 | 80,000.0 | 240,000.0 | 7,515,979.6 | 8,695,500.0 | -13.6 |

The residual is within +/-17% at every anchor. It arises because v1.0 publishes only block **totals by year** and never states which population each block scales with, so the fixed-vs-variable split and the contributing-vs-holding assignment are this model's reconstruction. **A three-point fit cannot separate growth-over-time from scale-with-N without that assignment**, and no source supplies it. Disclosed rather than plugged.

Marketing is deliberately **excluded** from the opex blocks. v1.0 carries it both as an opex line and as the acquisition driver; the parameter file's G1 says it is a decision variable and an *input* to acquisition. Booking it in both places double-counts it, so it is booked once, in acquisition cost.

2. **The Y1 opex figure is not a run-rate - now handled, previously not.** Y2 at 1,478,420 against Y1 at 894,800 is a 65% step, because the brief's Y1 is a partial year of a business that has not finished hiring. S48 puts the exit run-rate at 1.40x the Y1 average.

    **S48 was declared but never read by any model code** - so flexing it in the tornado returned a swing of exactly zero. It is now applied as a linear within-Y1 hiring ramp with mean exactly 1.0 (M1 at 0.60x rising to M12 at 1.40x), so the **Y1 total is unchanged** and only its distribution moves. This matters for cash timing and for the honesty of any early-year break-even claim.

3. **The net contribution margin on the inflow lanes is negative at Base, and the brief presents stream 1 as positive.** The brief's §6.1 computes a 0.72% gross margin before rail on a USD 75 ticket. The model applies the real segment mix, in which S3 (USD 20) is the largest agent-channel cell, and a fixed USD 0.25 rail cost per collection. On the blended ticket the rail exceeds the margin. **This is not a disagreement about arithmetic; it is the §0.2 finding taken to its conclusion across the actual segment mix.** Note this is now reported as a *metric*, not as the revenue line - gross revenue is fees earned and is never negative.

3a. **v1.0's T1/T2/T3 ladders are indexed to a volume the model never reaches, and T1 is now proven unfundable.** The denomination schedule is solved endogenously and never justifies Good Delivery; 1 kg clears at Y5 rather than Y3. The fabrication premium therefore holds at 2.00% instead of falling to 0.75%.

    The model **runs T1 on v1.0's assumed 5/4/3 schedule** so the P&L shows the consequence of the client's stated plan rather than silently repricing it. §8.3 of the spine then solves the minimum viable fee and reports the gap. Years Y3, Y4, Y6, Y7, Y8, Y9, Y10 are not fundable, worst case 0.79pp short at Y10. **The negative stream 1 in the P&L is therefore a real consequence of a real plan, not a modelling artefact.** Repricing to the viable path is a client decision, so it is reported and not applied.

4. **The 2%-of-reserves escalator binds, but at a different level than the corpus states.** The corpus sizes it at USD 4m on USD 200m of reserves. This model reaches USD 39,790,584 of AUM at Y10, so 2% is **USD 795,812** against an AED 1.5m floor of USD 408,441 - i.e. **1.95x the floor, so it DOES bite** and roughly doubles locked capital under Option B. The corpus's USD 200m reserve assumption is ~5x this model's AUM - the same AUM-versus-contributions gap the audit found - so the *level* is unresolved even though the *direction* is confirmed. **Quantified in spine §7.2; the counsel question stands.**

4a. **Gold is modelled as a level plus a single scheduled shock, not as a stochastic price process.** The level run (spine 10.2.1) establishes USD-AUM invariance, and the shock run (10.2.2) can trigger a genuine margin call because drawn balances are carried as vintages at their originally struck LTV. But the model answers *what happens if gold falls X% in Y6*, not *what is the probability of a margin call over ten years*. **Pricing that likelihood needs a price process, which is out of scope.** The -13/-29/-46% ladder in 10.2.3 is a static analytical statement of the fall each struck LTV needs, not a scenario result.

5. **Redemption events are approximated.** The corpus gives redemption cost per *event* (F20) but the model tracks redeemed *grams*. Event counts are inferred rather than modelled from a ticket-size distribution, which does not exist in any source. The line is immaterial at every modelled scale (single-digit thousands per year), so the approximation is disclosed rather than refined.

6. **`Sold` is computed at the archetype-track level, not per account.** Retention therefore reflects each track's assigned withdrawal bucket rather than an individual history. This is the intended design (it is what makes the tier distribution computable), but it means Retention is a step function across three buckets rather than a continuous distribution. At Base only ~14% of the book sits above the 30% kink, so Retention does very little work - itself a finding: **the 30% allowance is set generously enough that Retention is close to inert at Base assumptions.**

7. **B2B partner AUM is exogenous and does not interact with the retail book.** S44 calibrates per-partner terminal AUM to hit S13's USD 200m by Y10. The model reproduces that path but cannot validate it - it depends on a signed partner that does not exist. Stream 6 is the single largest revenue line in the `no_card` scenario, which makes this the least validated load-bearing number in the model.
