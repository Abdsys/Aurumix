Y3 now lands at 2,484,700 vs the brief's 2,506,000 (0.9% off) and Y10 at 8,695,500 vs 8,495,500 — that residual is the Marketing block's linear treatment. Close enough to specify with a reconciliation plug. I have everything I need.

---

# Aurumix Revenue Model — Parameter Completion Set (v2.0 gap fills)

New IDs continue from the brief's existing S15 (scenario) and F19 (fixed). Scenario parameters are **S16–S48**; fixed inputs are **F20–F31**.

---

## Block A — Acquisition

### A1. Channel-to-segment mix matrix (S16)

**Rows are channels; each ROW sums to 100%** — i.e. each channel's output is distributed across segments. This is the correct orientation because the model computes channel volume first (agents × productivity, spend ÷ CAC) and then allocates it.

**Phase 1 — M1 to M12 (S1–S3 only live):**

| Channel | S1 (USD 75) | S2 (USD 40) | S3 (USD 20) | S4 | S5 | S6 | Sum |
|---|---|---|---|---|---|---|---|
| Agent | 15% | 40% | 45% | — | — | — | 100% |
| Referral | *structurally zero* | | | | | | 0% |
| Direct | 45% | 40% | 15% | — | — | — | 100% |
| B2B partner | *not live until M24* | | | | | | 0% |

**Phase 2 — M13 to M24 (+S4, +S5, referral opens):**

| Channel | S1 | S2 | S3 | S4 | S5 | S6 | Sum |
|---|---|---|---|---|---|---|---|
| Agent | 12% | 33% | 38% | 10% | 7% | — | 100% |
| Referral | 18% | 38% | 33% | 6% | 5% | — | 100% |
| Direct | 38% | 33% | 12% | 7% | 10% | — | 100% |
| B2B partner | — | — | — | — | — | — | 0% |

**Phase 3 — M25 onward (all six live, B2B live from M24):**

| Channel | S1 | S2 | S3 | S4 | S5 | S6 | Sum |
|---|---|---|---|---|---|---|---|
| Agent | 10% | 28% | 32% | 12% | 16% | 2% | 100% |
| Referral | 16% | 34% | 30% | 8% | 10% | 2% | 100% |
| Direct | 32% | 28% | 10% | 8% | 16% | 6% | 100% |
| B2B partner | 5% | 15% | 10% | 5% | 60% | 5% | 100% |

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S16 | Channel-to-segment mix matrix | tables above | Direct/referral shift +8pp toward S1/S6 (higher ticket) | Agent shift +10pp toward S3 (USD 20 floor) | % of channel volume | Judgement, anchored on three corpus facts: agents sell face-to-face in labour-dense settings so they skew blue-collar; referral inherits the referrer's own social stratum so it approximately mirrors the installed base with a mild uplift (a referrer must have survived six months, which selects for affordability); B2B is the SafeGold shape, i.e. wallet/neobank distribution which is overwhelmingly India-resident | **Low.** No published channel-mix data for any comparable product. Judgement call |

**The two structural rules the matrix must encode, which matter more than the cells:**

1. **The agent row must always be the most blue-collar-weighted row.** Agents earn a percentage of a fee on a ticket, so on pure economics they should chase S1. They will not, because S3 is where the accessible density is (labour accommodation, community organisations, employer payroll clusters). This is the single most consequential cell in the matrix, because it collides with §0.2: the agent channel delivers the segment on which the fixed rail cost is spread over the smallest base. **If the rail lands at UAEDDS pricing, the agent channel is the loss-making channel.** The model must be able to show that.
2. **The B2B row is 60% S5.** Stream 6 is not a UAE line. Its natural partner set after the SEBI caution is Indian wallets and neobanks (§6.7), so partner AUM and the India switch are coupled. **If `INDIA_ENABLED` is off, stream 6 must fall by roughly 60%, not stay flat.** The v1.0 brief does not wire this dependency and it should.

### A2–A5

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S17 | Agent ramp factor, months 1/2/3/4/5/6/7-12/13+ since joining | 0.20 / 0.40 / 0.60 / 0.75 / 0.85 / 0.95 / 1.00 / 1.05 | 0.35 / 0.60 / 0.80 / 0.95 / 1.00 / 1.05 / 1.10 / 1.15 | 0.10 / 0.20 / 0.35 / 0.50 / 0.65 / 0.75 / 0.90 / 0.95 | × S12 productivity | Insurance-agency ramp shape. Applied multiplicatively to S12 (4 accounts/agent/month). **Six months to full productivity** is the standard life-agency figure and it happens to match the Confirmed SIP gate, which is convenient: an agent cannot credibly sell the tier ladder until they have a client who has passed it | **Low-Medium.** Shape is conventional; the calibration is a judgement call |
| S18 | Agent annual attrition | 45% | 30% | 60% | %/yr of active agents | Indian life-agency attrition runs 40-60% in year one. **This is missing from T7 entirely.** T7 gives active agents 5→15→40→90→200 as a stock. The model must gross that up: to hold 200 active at 45% attrition requires ~90 recruits/yr, each of whom re-enters the ramp at 0.20. Without this the model overstates agent output by roughly 15-20% at steady state | **Low-Medium** |
| S19 | Referral rate | 0.45 | 0.90 | 0.18 | qualified referrals/qualified referrer/yr | **Structurally zero until M13.** A "qualified referrer" is an account past its own six-month gate. Corpus (`_draft_referral-system.md` §6) removed the cap deliberately, so the distribution is right-skewed: most referrers refer zero, a small tail (the WhatsApp admin, the employer with sixty staff) refers many. Model the mean, not the median | **Low.** No published referral rate for any gold or savings product. Judgement call |
| S20 | Referral conversion (referred signup → passes own six-month gate) | 62% | 72% | 48% | % | Referred customers persist better than marketing-sourced. The reward pays only at the referee's gate, so this rate is exactly the M7 survival of the referred cohort. At Base persistency M7 survival is 68% (fitted below); referred is uplifted ~1.1x, capped at a sensible ceiling | **Low-Medium.** Derived from our own fitted curve, not from an external source |
| S21 | Referral-driven accounts | `qualified_referrers(t) × S19 ÷ 12 × S20` | | | accounts/month | Note the double gate: a referral signed in M13 pays out in M19 and only counts as converted then. **Two six-month gates in series means the referral channel does not reach steady state until roughly M25** | High (mechanism), Low (rates) |
| S22 | Segment penetration ceiling, S1 / S2 / S3 / S4 / S5 / S6 | 22% / 16% / 9% / 6% / 0.35% / n/a | 32% / 24% / 14% / 10% / 0.60% / n/a | 12% / 9% / 5% / 3% / 0.15% / n/a | % of the §5 addressable base | Applied against §5's **income-qualified, gold-propensity-filtered** base (~474k for S1-S3), not the headline 4.58m. The gradient is deliberate: S1 has the highest smartphone/banking penetration and the lowest sensitivity to a USD 20 minimum being 5x Liv Gold's; S3 is where the Liv Gold competitive problem bites hardest. **S5 at 0.35% of 12.5m is ~44,000 accounts, which alone is most of the client's Y10 target** — this is why the India switch is load-bearing and why its ceiling is set an order of magnitude tighter than the GCC ceilings | **Low.** The underlying base already carries an unsourced propensity filter (§5 says so explicitly); this multiplies a Low-confidence number by another Low-confidence number |
| S23 | Saturation functional form | Logistic on remaining headroom | | | — | `new(s,t) = raw_demand(s,t) × [1 − cumulative_ever_acquired(s,t) ÷ (base(s) × ceiling(s))]`. Use **cumulative-ever-acquired, not live accounts** in the numerator: a lapsed customer is a burnt lead, not a returned one. At 19% M61 persistency the difference is roughly 5x by Year 10 and it is the mechanism that stops the model producing an implausible Year 8-10 hockey stick. **This is the single most important structural fill in Block A** | Medium (form), Low (parameters) |
| S24 | Marketing → accounts conversion | `spend(t) ÷ effective_CAC(t)` | | | accounts | S15 gives CAC at USD 120 flat. It must not be flat — see S25 | High (mechanism) |
| S25 | CAC diminishing-returns rule | `effective_CAC(t) = S15 × [1 + 0.35 × (monthly_spend ÷ 60,000)^0.7]` | exponent 0.5, divisor 100,000 | exponent 0.9, divisor 35,000 | USD | Power-law saturation on the paid channel. Calibration point: at USD 60,000/month spend (roughly Y3 marketing at 250k/yr plus growth), effective CAC is USD 162, not 120. **The corpus has no CAC benchmark at all — §15 lists "all marketing and CAC assumptions" as Low.** The reason to model the curve rather than the point is that break-even View 2 lands at Y7-Y9, which is exactly the region where a flat CAC lets the model buy unlimited growth at a constant price. A flat CAC makes the break-even year an artefact of the marketing budget | **Low. No published source; this is a judgement call.** The functional form is defensible, the constants are not |
| S26 | Organic (unattributed direct) accounts | 12% of direct channel | 20% | 5% | % of direct volume | Judgement. Kept separate from paid so the CAC curve is not applied to it | Low |

---

## Block B — Behavioural (cohort and ICS engines)

### B1. Payment archetypes (S27) — the heterogeneous mix

This is the most load-bearing fill in the whole set, and it is constructed to satisfy the constraint stated in the task: the weights must reproduce §0.5's recommended persistency curve.

**Structure.** Each archetype carries a **payment-behaviour hazard** (attrition arising from the payment pattern itself) plus a **common background hazard** (voluntary exit for reasons unrelated to payment ability — moved country, changed mind, found Liv Gold). Total monthly attrition per archetype = own hazard + background. This two-component form is necessary: a pure mixture-of-archetype-hazards cannot reproduce the curve, because heterogeneity alone produces a tail that is far too fat (I tested this — a best-fit pure mixture lands at 36% at M61 against a 19% target). **The background hazard is what makes the arithmetic work, and it is a finding in its own right: the corpus's implicit assumption that lapse is a payment-failure phenomenon is wrong. Roughly half of terminal attrition is people who could pay and chose not to.**

| Archetype | Weight (Base) | Monthly payment probability | Own hazard | Total monthly attrition | What it is |
|---|---|---|---|---|---|
| **Perfect payer** | 10% | 0.995 | 0.000 | 0.016 | Never misses. Reaches Sovereign at M61. The only archetype that can |
| **Occasional misser** | 35% | 0.93 | 0.007 | 0.023 | Misses ~1 month a year. Streak halves and rebuilds. Caps around Platinum |
| **Alternating misser** | 12% | 0.55 | 0.018 | 0.034 | Pay-miss-pay-miss. **Permanently capped at Gold** because Recent holds at 6 forever (`_draft_ics-scoring.md`). A real, permanently occupied cell |
| **Reducer** | 13% | 0.97 (at reduced ticket) | 0.002 | 0.018 | Drops to a lower contribution rather than lapsing. **Lowest attrition of any non-perfect archetype**, which is the whole point of the free unscored reduction |
| **Early lapser** | 30% | 0.60 falling | 0.200 | 0.216 | Never passes the six-month gate, or passes it and stops. ~90% gone by M13 |

**Aggressive mix (fits 65% M13):** Perfect 29%, Occasional 26%, Alternating 16%, Reducer 8%, Early lapser 21%; background hazard **1.1%/month**.
**Conservative mix (fits 45% M13):** Perfect 14%, Occasional 24%, Alternating 16%, Reducer 10%, Early lapser 36%; background hazard **2.4%/month**.

**Verification — implied aggregate survival against the §0.5 anchors:**

| | M13 | M25 | M37 | M49 | M61 |
|---|---|---|---|---|---|
| §0.5 recommended | 55% | 40% | 30% | 24% | 19% |
| **Base mix produces** | **54.7%** | **40.5%** | **31.0%** | **23.8%** | **18.3%** |
| Aggressive mix | 64.8% | 51.7% | 42.3% | 34.9% | 28.9% |
| Conservative mix | 44.8% | 29.4% | 20.1% | 13.9% | 9.7% |

Base error is under 1pp at every anchor. **Use these as the calibration starting point, not as settled values.**

**Which lever moves which anchor** — this is the part the modeller actually needs:

| Anchor | Dominant lever | Direction | Approximate sensitivity |
|---|---|---|---|
| **M13** | **Early-lapser weight** | Almost exclusively. The early lapser is ~90% gone by M13, so its weight sets the M13 level nearly one-for-one | −1pp early-lapser weight → +0.85pp M13 survival |
| **M25** | Early-lapser weight **and** background hazard, roughly equally | The early lapser is fully exhausted by M25, so from here the background hazard takes over | −0.1pp background → +1.0pp M25 |
| **M37–M61** | **Background hazard**, dominantly | The tail is set almost entirely by the common hazard, not by archetype composition | −0.1pp background → +1.8pp M49, +2.3pp M61 |
| **Tail flatness (M49→M61 ratio)** | Perfect-payer weight | Raising the perfect-payer weight flattens the far tail without moving M13 | +5pp perfect weight → +1.5pp M61, ~0 at M13 |

**Practical calibration order: set the early-lapser weight from M13, set the background hazard from M49/M61, then use the perfect-payer weight to fine-tune the M37 midpoint.** The three levers are close to orthogonal in that order, which is why the fit converges cleanly.

**Two things the archetypes give the model that a scalar success probability cannot:**
- **The ICS tier distribution becomes computable rather than assumed.** T4/T5 in the brief say "computed by the ICS engine, not assumed" but v1.0 supplies no behavioural input capable of computing it. These archetypes are that input. Perfect payers → Sovereign; occasional missers → Platinum ceiling; alternating missers → Gold ceiling for life. Run each archetype through the ICS state machine separately and weight the outputs.
- **The alternating misser is a revenue-relevant cell, not a curiosity.** At 12% of the book with a Gold-for-life cap, it is roughly a quarter of the steady-state Gold population — spending at the lowest interchange rate (1.80%) and the highest FX margin (2.0%), i.e. **the most profitable card cell in the book**, because it generates stream 4 revenue that the higher tiers have waived.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S27 | Payment archetype weights + hazards | tables above | as above | as above | % / monthly hazard | Fitted to reproduce §0.5. Archetype *names* are grounded in `_draft_sip-rulebook.md` §7.1 (the miss ladder) and `_draft_ics-scoring.md` (the alternating-misser Gold cap is proved there). Archetype *weights* are our fit | **Medium on the aggregate** (it reproduces a researched curve), **Low on the decomposition** (no source decomposes a savings-product lapse curve into payment archetypes; confirmed negative) |

### B2–B5

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S28 | Reduction capture rate | 33% | 50% | 18% | % of would-be lapse events diverted to REDUCED | The brief's §3 Layer 2 says "if the product converts even a third of would-be lapses into reductions" — **Base is set at the brief's own illustrative third, deliberately, so v2.0 does not silently invent a different number.** Corpus basis: `_draft_sip-rulebook.md` §6.2, reduction is free, instant and unscored, and the drafting note says insurance lapse data shows people quit when reducing feels like failure. **Apply only to affordability-driven lapse**, i.e. to the occasional-misser and reducer archetypes, never to the early lapser or the background hazard | **Low. No published source** — no insurer or SIP platform publishes a downgrade-versus-lapse split. Judgement call, but anchored to the brief's own stated figure |
| S29 | Reduction depth | To USD 20 floor for S3; to **50% of prior ticket, floored at USD 20** for S1/S2/S4/S5/S6 | 65% of prior ticket | Straight to USD 20 floor for all | USD/month | The v1.0 brief assumes reduction goes straight to the USD 20 floor (§3 Layer 3: `reduced(s,t) × 20`). **That is almost certainly too harsh and it is a real error worth correcting.** A USD 75 saver under affordability pressure halves to USD 40 far more often than they cut by 73%. The floor is the *hard* minimum (F6), not the *observed* landing point. Base gives S1 → USD 38, S2 → USD 20 (floored), S4 → USD 20 (floored) | **Low. No published source; judgement call.** But the *direction* of the correction is high-confidence |
| — | **Model consequence of S29** | Base raises reduced-state inflow ~40% vs the v1.0 treatment for S1 | | | — | `gross_inflow(s,t) = contributing(s,t) × ticket(s) + reduced(s,t) × reduced_ticket(s)` — **replace the hard-coded 20 in §3 Layer 3 with a per-segment reduced ticket.** Also note it moves margin: a USD 38 reduced ticket clears the S1 rail comfortably; a USD 20 one does not at Conservative rail cost | High (mechanism) |
| S30 | Hazard multiplier, REDUCED vs CONTRIBUTING | 1.35× | 1.15× | 1.75× | × monthly hazard | Reduction is a delay state, not an absorbing one. A reducer has revealed affordability stress, so they carry elevated risk — but they have also revealed they would rather pay less than quit, which is a strong retention signal. **The multiplier must be well above 1.0 or REDUCED becomes a free retention machine and the model overstates persistency; it must be well below the pure-lapse case or the state does no work.** Note this interacts with S27: the "reducer" archetype (13%) is the *voluntary* reducer with a 0.002 own hazard; S30 applies to accounts *diverted* into REDUCED by S28, who are a different and riskier population | **Low. No published source; judgement call** |
| S31 | Withdrawal-behaviour distribution (annual self-custody withdrawal as % of holdings) | see below | see below | see below | % of population | Buckets deliberately straddle the 30% Retention kink | **Low.** No source; judgement, but reconciled to a researched aggregate |

**S31 detail — must reconcile to S10 aggregate leakage:**

| Bucket | Base weight | Aggressive | Conservative | Bucket midpoint used |
|---|---|---|---|---|
| 0% (never withdraws) | 48% | 60% | 26% | 0.00 |
| 1–10% | 22% | 21% | 17% | 0.05 |
| 11–30% (**at or below the kink**) | 16% | 12% | 19% | 0.19 / 0.18 / 0.22 |
| 31–60% (**Retention starts falling**) | 9% | 5% | 19% | 0.44 / 0.42 / 0.45 |
| 61–99% | 3.5% | 1.5% | 13% | 0.78 / 0.75 / 0.80 |
| 100% (full exit of holdings) | 1.5% | 0.5% | 6% | 1.00 |
| **Weighted aggregate leakage** | **12.3%** | **6.9%** | **30.0%** | vs S10 target 12 / 6 / 30 |
| **Share above the 30% kink** (Retention < 1.0) | **14%** | **7%** | **38%** | — |

All three reconcile to S10 to within 0.3pp. **The output that matters is the last row, not the aggregate:** only 14% of the base takes any Retention haircut at Base, so the Retention multiplier is close to inert in the Base case and is a genuine tier-suppressant only in the Conservative case. **This is a finding the brief should carry: the 30% allowance is set generously enough that Retention does almost no work at Base assumptions.** If the client wants Retention to bind, the allowance has to come down — but that is a design change, not a modelling one.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S32 | Redemption rate (gold → cash, distinct from self-custody withdrawal) | 8% | 4% | 16% | % of AUM/yr | **A different event from S10/S31 and must be modelled as a separate line.** Self-custody withdrawal is a token transfer out (leakage, hits five streams). Redemption is burn-and-pay-cash (`Aurumix_Process_Maps_Redemption.md`) and also hits AUM but has a *cash cost*. Base is set below the self-custody rate because the corpus makes the on-chain route frictionless (decision 50, open ERC-20), so the marginal exiter transfers rather than redeems. **PAXG turnover of 5.9% (`_draft_allocation-and-float.md` §301) is the only comparator in the corpus** and is a token-turnover figure, not a redemption figure | **Low-Medium** |
| F20 | Cost per redemption event | 4.20 | 2.50 | 9.00 | USD | Build-up: outbound AED payment / local transfer USD 1.00-2.50, sanctions re-screen at Sumsub USD 1.85 (F16, its own pricing page), operational handling amortised USD 1.00-4.50. **VARA Annex 2 III.E.4 forbids charging any fee on redemption, verified verbatim, so this is 100% absorbed cost.** No offsetting revenue line exists or can exist | **Medium.** Components are sourced; the operational allocation is ours |
| — | **Redemption is a pure-cost stream and the model must show it as one** | | | | | The brief lists six revenue streams and no negative one. Redemption is effectively **stream 0: a mandatory, uncapped, zero-revenue cost line that scales with AUM.** At Y10 AUM and Base rates it is roughly USD 25-35k/yr — immaterial against USD 11m of revenue, which is the reassuring finding. It becomes material only in a stress scenario where redemption rate spikes, and that is exactly when cash is scarcest. **Worth a stress row rather than a headline** | Medium |
| S33 | Lapsed-but-holding redemption multiplier | 2.2× | 1.6× | 3.5× | × the contributing-account redemption rate | Corpus is emphatic that lapsed customers keep their gold — *"You can lose your status. You can never lose your gold."* — and `Aurumix_Process_Maps_Custody_Fee.md` §129 identifies exactly this population as the one that "still holds gold, still costs money to store, and the cash touchpoint is gone." A lapsed holder has no accruing tier to protect (their Record is frozen, their Standing has decayed) so the Retention penalty costs them nothing they still value. **The one thing holding them in is inertia, and inertia is not a 10-year assumption.** Apply to S32 and to S31 alike | **Low. No published source; judgement call** |
| — | **Why S33 is load-bearing despite looking like a detail** | | | | | At 19% M61 persistency, **81% of ever-acquired accounts are lapsed by Year 6.** If that population redeems at 2.2× the contributing rate, the lapsed book — not the contributing book — is the dominant AUM decay term from roughly Year 4. AUM drives stream 6, custody absorption and the credit collateral base. **The v1.0 model has no lapsed-holder AUM decay term at all**, which means it will overstate Y6-Y10 AUM. This is arguably the largest single arithmetic gap the audit found | — |

---

## Block C — Card (streams 2 and 4)

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S34 | Foreign spend as share of total card spend | 34% | 45% | 24% | % of AED spend | Build-up rather than a benchmark, because none exists: (a) an expatriate base makes home-country e-commerce and remittance-adjacent spend routine, (b) UAE residents travel heavily and summer travel is a distinct season (see S48), (c) a large share of "foreign" spend for this base is **India-domiciled online merchants transacted from Dubai**, which is FX-margin-bearing even though the cardholder never left. Offsetting: groceries, fuel, rent and utilities are all AED and are the bulk of wallet share. **Note the brief's §6.2 gap: cross-border interchange sits above domestic and outside the CBUAE cap, but no cross-border rate is published, so the model carries domestic only and is conservative by an unknown margin on stream 2 while this parameter is correctly sized on stream 4.** The asymmetry should be flagged, not fixed | **Low. CBUAE publishes no domestic-versus-cross-border split — the brief already records this as a confirmed negative.** Judgement call |
| S35 | ATM withdrawal volume per active cardholder/month | 950 | 1,600 | 500 | AED | Set deliberately just **below** the Gold free allowance of AED 1,000, which is the finding rather than the number. The UAE is heavily card-and-transfer based and this base pays rent by cheque or transfer, not cash. **At Base, the median Gold cardholder never breaches the allowance, so ATM over-allowance revenue is generated almost entirely by a small high-cash tail.** Model as a distribution, not a mean: **60% of cardholders draw AED 0-500, 25% draw 500-1,500, 12% draw 1,500-3,000, 3% draw 3,000+.** That distribution has a mean of ~AED 940 and produces materially more over-allowance revenue than applying 2% to `max(0, 950 − 1,000)`, which is zero | **Low. No published source; judgement call.** The distributional treatment is the important part |
| — | **The allowance ladder is nearly costless and that is worth saying** | | | | | Under the Base distribution, raising the allowance from AED 1,000 (Gold) to 5,000 (Sovereign) waives revenue from only the top ~3% of cardholders. **The ATM tier benefit costs almost nothing and looks generous** — the same time-phasing argument the brief makes about the discount ladder in §7.2, applied to a second benefit. Add it to the client-facing story | Medium |
| F21 | Card issuance fee (Gold / Platinum / Sovereign) | 75 / waived / waived | — | 100 / 50 / waived | AED, one-off | `_draft_ics-benefits.md` §229-231: "issuance and replacement charged at base level, waived at upper levels." The rate is ours; the waiver ladder is corpus-settled | Low on rate, High on structure |
| F22 | Card replacement fee (Gold / Platinum / Sovereign) | 100 / 50 / waived | — | 150 / 100 / 50 | AED, per event | Same source. Market-normal UAE replacement fee is AED 75-150 | Low |
| S36 | Card issuance event rate | 1.00 at activation, +0.06/yr thereafter | +0.04 | +0.10 | events/active card/yr | The +0.06 is renewal-and-upgrade churn: cards expire on a 3-year cycle (0.33/yr, but reissue is typically free at expiry), plus tier upgrades that trigger a new plastic. **A tier upgrade is a card-product change (Platinum → Signature → Infinite), so it forces a physical reissue** — this is a real cost the brief does not carry | Low-Medium |
| S37 | Card replacement event rate (loss, theft, damage) | 0.11 | 0.07 | 0.18 | events/active card/yr | Judgement. Industry-normal loss/theft/damage replacement sits around 8-15% annually across retail portfolios | **Low. No named primary source; judgement call** |
| S38 | Card spend tier multipliers (Gold / Platinum / Sovereign) | 0.82 / 1.12 / 1.54 | 0.85 / 1.10 / 1.45 | 0.78 / 1.15 / 1.70 | × S4 blended AED 6,000 | Normalisation check at the Y10 tier mix (Gold 55% / Platinum 30% / Sovereign 15% of *cardholders*): blend = 1.018, i.e. AED 6,108 against the AED 6,000 target — **1.8% over, within tolerance.** At the Y5 mix (62/38/0) it reads AED 5,604 and at Y3 (78/22/0) AED 5,316, which is the correct direction: **early-year blended spend must sit below the terminal blend because the mix is bottom-heavy.** The v1.0 brief's flat AED 6,000 across all years overstates Y3-Y5 interchange by roughly 8-12% | **Medium on the normalisation arithmetic, Low on the ratios.** No source splits card spend by loyalty tier |
| — | **Why the multipliers must be applied and not blended away** | | | | | Interchange rates differ by tier (1.80 / 2.05 / 2.10) *and* FX margins differ by tier (2.0 / 1.5 / 1.0) *and* ATM allowances differ by tier. Applying a blended spend to a blended rate double-counts the mix effect in stream 2 and gets the sign wrong in stream 4, because **the tier that spends most is the tier whose fees are most waived.** The brief's §6.4 already says "forecast spend by tier, not in aggregate" — S38 is the input that makes that instruction executable | High (mechanism) |
| F23 | Average transaction size (Gold / Platinum / Sovereign) | 185 / 240 / 310 | — | 150 / 200 / 260 | AED | Higher tiers spend more per transaction as well as more in total — the tier multiplier splits roughly 65% into ticket size and 35% into frequency. Implies monthly transaction counts of ~27 / 28 / 30 at Base spend | **Low. No published source; judgement call** |
| F24 | Per-transaction processor fee | 0.10 | 0.05 | 0.15 | USD/authorised transaction | **Stripe Issuing's published USD 0.10/txn, named in the brief's §6.2 as an unmodelled gap.** Assume authorisation-based, so declines and reversals also bill — add 6% to the transaction count for declines | **Medium.** Stripe's published rate is real; whether NymCard prices the same way is a term-sheet question |
| — | **F24 × F23 — the arithmetic the brief flagged and did not run** | | | | | At AED 185 (Gold), USD 0.10 is **0.199% of value against a 1.80% gross rate = 11.0% of gross interchange.** At AED 240 (Platinum) it is 0.153% against 2.05% = **7.5%.** At AED 310 (Sovereign) 0.118% against 2.10% = **5.6%.** So the processor fee is a **regressive tax on the lowest tier**, taking 11% of Gold's gross interchange against 5.6% of Sovereign's. **And it stacks the wrong way with PM share:** at the Conservative 55% PM share, Gold's net interchange is 1.80% × 0.55 − 0.199% = **0.791%**, which is 44% of gross rather than the headline 55%. **The effective PM share on small tickets is materially below the contracted PM share, and the model must compute it per tier rather than applying S3 flat.** This is the largest single correction in Block C | High (arithmetic), Medium (inputs) |
| S39 | Card fraud and chargeback loss | 9 | 5 | 22 | bps of card spend | Visa's published worldwide average fraud loss is "less than 8 cents in every USD 100" ≈ **8 bps** (Visa corporate materials). Base sets slightly above that for a novel issuer with a new BIN and a cross-border-heavy profile — new programmes attract testing. Conservative reflects a first-year enumeration attack, which is the normal failure mode for a fresh BIN | **Medium** on the Visa global figure, **Low** on the Aurumix-specific adjustment. **No UAE issuer fraud rate is published — confirmed negative, consistent with the brief's finding that CBUAE publishes no card-level data** |
| F25 | Dispute handling cost per case | 22 | 14 | 40 | USD/case | Includes scheme representment fees and internal handling. Assume **0.9 disputes per 1,000 transactions** at Base (1.5 Conservative) | **Low. No published source; judgement call** |
| F26 | Card production and issuance unit cost | 4.50 / 7.00 / 14.00 | 3.50 / 5.50 / 10.00 | 6.00 / 9.50 / 20.00 | USD/card, Gold / Platinum / Sovereign | Metal or premium plastic is the norm at Infinite level and the cost gap is large. Includes personalisation, carrier, and courier delivery within the UAE. **At Sovereign the production cost exceeds the AED 0 issuance fee by construction** (issuance is waived at upper tiers), so this is a real contra-revenue line, not a pass-through | **Low-Medium.** Card-production pricing is quote-based and unpublished |
| F27 | Card programme fixed costs | see below | | | USD | **These are minimum-commitment structures and they bind at low volume exactly as the DGCX vault minimum does (§7.4 correction 3) and the Sumsub USD 299/month minimum does (F16).** This is the third instance of the same pattern and the brief should name it as a pattern | **Low. No UAE BIN-sponsorship price list is published; confirmed negative.** Structure is well-attested, quantum is a judgement call |

**F27 detail — card programme fixed cost stack:**

| Line | Base | Aggressive | Conservative | Unit | When booked |
|---|---|---|---|---|---|
| BIN sponsorship setup (one-off) | 45,000 | 25,000 | 90,000 | USD | M15 (3 months before M18 go-live) |
| Scheme joining / certification (one-off) | 30,000 | 18,000 | 60,000 | USD | M15 |
| BIN sponsorship monthly minimum | 6,000 | 3,500 | 12,000 | USD/month | M18 onward |
| Processor platform monthly minimum | 5,000 | 3,000 | 9,000 | USD/month | M18 onward |
| Visa scheme quarterly minimum / assessments | 12,000 | 7,000 | 22,000 | USD/quarter | M18 onward, quarter-end |
| **Annualised fixed run-rate from M18** | **180,000** | **106,000** | **340,000** | USD/yr | |

**The volume at which the minimum stops binding — the number that matters:** at Base, USD 180,000/yr of fixed cost against Gold-tier net interchange of ~0.79%/transaction-value requires roughly **USD 22.8m of annual card spend**, i.e. about **290 active cards at AED 6,000/month.** The brief's T4 puts Gold+ share at 28% by Y2 — on a Y2 book of a few thousand accounts with a 65% activation rate, the programme is roughly at or just past that threshold when it launches at M18.

**So the finding is: the card programme's fixed cost is approximately break-even at launch and immaterial thereafter — but only at Base assumptions.** At Conservative (USD 340,000/yr fixed, 55% PM share, AED 3,500 spend), the required active-card count is roughly **1,100**, which the model will not reach until well into Y3. **The card programme runs at a loss for its first 12-18 months in the Conservative case, and the brief's View 2 break-even table does not carry that drag.** Adding it will push the Conservative "never" cell further out and may move the Base case from Y8 to Y8-Y9.

**Add F27 to the M18 activation logic, not to opex.** It is a stream-2 contra-cost that only exists if the card exists, and burying it in the opex block hides the conditionality.

---

## Block D — Credit (stream 5)

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| F28 | **Origination fee** — gross rate / Aurumix share | 1.00% of draw / **50%** | 1.25% / 65% | 0.75% / 35% | % of draw amount; % to Aurumix | **Finance House's UAE gold loan Key Facts Statement carries a 1% processing fee** — this is the one gross rate in the set with a real UAE anchor (already in the brief's §6.5). The *split* is pure term-sheet. 50% is the natural anchor because Aurumix originates the customer, holds the collateral relationship and does the tier-based credit decisioning, while the partner carries the balance sheet and the licence | **Medium** on the gross rate (UAE primary), **Low** on the split (no source; judgement call) |
| F29 | **Servicing fee** — gross rate / Aurumix share | 0.50%/yr of drawn / **70%** | 0.75% / 80% | 0.25% / 55% | %/yr of average drawn; % to Aurumix | Aurumix's share is set **highest of the four heads**, deliberately: servicing is the head where Aurumix does most of the actual work (app, statements, collateral monitoring, LTV recalculation against the tier ladder, margin-call triggering). The corpus makes Aurumix the collateral administrator by construction — the gold never leaves | **Low. No published source; judgement call** |
| F30 | **Penal / late fee** — gross rate / Aurumix share | 2.00% flat per late event / **40%** | 2.50% / 55% | 1.50% / 25% | % of overdue amount; % to Aurumix | Share set **low** on purpose: penal income belongs economically to whoever bears the credit risk, and `_draft_credit-and-card-infrastructure.md` is explicit that **Aurumix takes no credit risk** (the lender of record advances and owns the book). Claiming a large share of penal income while bearing no risk is the kind of term a partner will price away elsewhere. ⚠ **Also check whether a penal charge on a gold-collateralised facility survives an Islamic-finance sponsor** — the corpus flags that this becomes binding if the sponsor is ADIB | **Low. No published source; judgement call.** The *reasoning* for a low share is the load-bearing part |
| F31 | **Recovery fee** — gross rate / Aurumix share | 1.50% of recovered / **0%** | 1.50% / 30% | 1.50% / 0% | % of recovered amount; % to Aurumix | 🔴 **Model Aurumix's share at ZERO in Base and Conservative, and treat any recovery income as upside only.** The brief's §6.5 flags the counsel question directly: *"if an enforcement sale is a 'redemption' under III.E.4, no fee may be charged on it."* Aurumix is the party that would execute the collateral sale (it holds the gold), so **Aurumix is precisely the party exposed to the recharacterisation risk**, while the partner — who is charging a recovery fee on its own loan under its own licence — is not. **The conservative reading is that Aurumix's recovery fee is the one fee head it structurally cannot charge.** Recording that as zero is a finding, not a gap | **Low-Medium.** The legal question is unresolved; **modelling it at zero is the defensible position and it costs almost nothing because recovery events are rare** |
| — | **Combined fee-head revenue check** | | | | | At Base and a USD 20,000 average facility drawn at 50%: origination USD 100 × 50% = USD 50 per draw event, servicing USD 10,000 × 0.50% × 70% = USD 35/yr, penal ~USD 4/yr expected, recovery USD 0. **Against an interest share of ~4pp on a USD 10,000 average drawn balance = USD 400/yr, the four fee heads together add roughly USD 90-110/yr, i.e. 20-25% uplift on the interest share.** Material but not transformative — which is the right answer to give the client before the partner conversation, because it sets expectations that the fee heads are not where stream 5 is won | Medium (arithmetic) |
| S40 | **Facility turnover — peak-to-average conversion factor** | **0.42** | 0.55 | 0.30 | × peak permitted drawn | 🔴 **This is the most important fill in Block D and the brief's formula is wrong without it.** §6.5's `drawn(t) = facility_limit × take_up_rate × drawn_pct_of_limit` computes **peak drawn**, and then applies an annual interest rate to it as though the balance persisted. The corpus says it does not: **Manappuram's realised tenor is 71 days against a 6-12 month product** (brief §6.5), so a borrower who draws to 50% of limit holds that balance for ~2.3 months, not 12. Derivation: 71 days ÷ 365 = 0.195 of a year per draw event, × S41 draw events/yr = average-to-peak ratio. At S41 = 2.1 draws/yr that gives **0.41**; a revolving card-style facility (the Aurumix design) sits somewhat above a pawnbroker's episodic pattern, so Base rounds to 0.42 | **Medium.** The 71-day tenor is a real figure from Manappuram's own reporting, already in the brief. The conversion arithmetic is ours |
| — | **What S40 does to stream 5** | | | | | **It roughly halves it.** The brief's §2.2 carries stream 5 at ~USD 600,000 at Y10. Applying S40 = 0.42 to the interest-share component (leaving origination, which is per-event and therefore *rises* with turnover, unchanged) takes the interest component from ~USD 480k to ~USD 200k, and the fee heads add back ~USD 120k. **Revised Y10 stream 5 ≈ USD 320-380k, not USD 600k.** Stream 5 falls from 5.5% to roughly 3.2% of terminal revenue. **This makes the brief's §0.4 headline stronger, not weaker: the card is an even larger share of the business than v1.0 states.** It should be corrected rather than defended | High (direction), Medium (quantum) |
| S41 | Draw events per borrower per year | 2.1 | 3.2 | 1.3 | events/active borrower/yr | Derived from the same Manappuram tenor: a borrower who is "active" in a year and holds ~71 days per draw at ~40% average utilisation is drawing roughly twice. **Aggressive reflects the revolving design working as intended** (a card-linked facility gets drawn far more often than a pawn loan); Conservative reflects gold-loan behaviour, where the draw is an emergency event and the borrower repays and exits. **Note the interaction: raising S41 raises origination-fee revenue linearly but also raises S40, so the two move together and must not be flexed independently** | **Low-Medium.** Derived from a real tenor figure; the event count is ours |

---

## Block E — B2B (stream 6)

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S42 | Partner count by year (Y2 / Y3 / Y4 / Y5 / Y7 / Y10) | 1 / 2 / 3 / 4 / 6 / 8 | 1 / 3 / 5 / 7 / 11 / 15 | 1 / 1 / 1 / 2 / 2 / 3 | signed, live partners | Partner acquisition is an enterprise sales motion with a long cycle and a hard technical dependency (multi-tenant register and mint, which the brief flags as a Week 1 build requirement). **One partner in Y2 is the M24 activation assumption; the Base path adds roughly one partner a year thereafter, which is a realistic enterprise cadence for a pre-revenue infrastructure vendor** | **Low. No published source; judgement call** |
| S43 | Per-partner AUM ramp shape (months since that partner's go-live) | S-curve: 8% / 25% / 48% / 70% / 85% / 100% at M6 / M12 / M24 / M36 / M48 / M60 of partner maturity | reaches 100% by M42 | reaches 100% by M84 | % of that partner's terminal AUM | Each partner runs its own clock from its own go-live, so partners signed in Y7 are still ramping at Y10 — **this is why the terminal figure is reached by a small number of mature partners plus a tail of immature ones, not by all partners at full size.** Shape is standard enterprise-integration adoption: slow first two quarters (integration, pilot cohort), steep M12-M30, asymptotic thereafter | **Low. No published source; judgement call** |
| S44 | Terminal AUM per partner | 32 / 45 / 22 | | | USD m, mature partner | Calibrated so the Base path reconciles to **S13's USD 200m by Y10**: partners 1-4 (live Y2-Y5) reach 85-100% of USD 32m ≈ USD 122m, partners 5-8 (live Y6-Y10) sit at 8-48% of USD 32m ≈ USD 68m, **total ≈ USD 190m against the S13 target of 200m.** Aggressive: 15 partners on the same shape at USD 45m terminal reconciles to roughly USD 400m (S13 Aggressive). Conservative: 3 partners at USD 22m ≈ USD 45m against S13's USD 50m | **Medium on the reconciliation arithmetic, Low on the per-partner figure** |
| — | **The SafeGold warning must be encoded, not just noted** | | | | | The brief's §6.6 records that SafeGold — the closest analogue, 55m customers, ₹6,867 cr transacted — runs an **EBITDA margin of 0.03%.** The model must therefore book **zero entry-spread revenue from the partner channel** and take stream 6 revenue *only* from the AUM platform fee. The partner keeps 70-80% of the entry spread, and the remaining 20-30% does not survive the fabrication premium and rail on the partner's own ticket sizes. **If the model books partner entry-fee margin, it is reproducing exactly the error SafeGold's accounts disprove** | **High.** The corpus states the split and the precedent |
| — | **Stream 6 is coupled to the India switch** | | | | | Per S16, the B2B row is 60% S5. If `INDIA_ENABLED = OFF`, S44 terminal AUM per partner should fall to roughly 40% of Base and S42 partner count should fall to the Conservative path — the post-SEBI-caution partner set is wallets and neobanks, and the largest of those are Indian. **Wire this dependency; v1.0 leaves the two switches independent and they are not** | Medium |

---

## Block F — Spot purchase lane (currently unmodelled)

This is a genuine structural omission rather than a missing number. The corpus is unambiguous that spot exists (`_draft_purchase-structure.md` §4, `_draft_sip-spot-and-ics.md` §1) and the brief models none of it.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S45 | Spot attach rate | 14% | 24% | 7% | % of live accounts making ≥1 spot purchase per year | Judgement, anchored on two corpus mechanics: spot is the natural home for a bonus, a Diwali gift or an Akshaya Tritiya purchase (see S47), and **`_draft_sip-rulebook.md` §1 makes any extra money inside a month a spot purchase by definition** — so every top-up above the declared ticket is spot volume. Rises with tenure: an account that has held for 3 years is roughly 2× as likely to buy spot as a 6-month account | **Low. No published source; judgement call** |
| S46 | Average spot ticket | 620 | 1,100 | 320 | USD/event | Set well above the SIP ticket because the behaviour is different: spot is a windfall or occasion purchase, not a budget line. Corpus worked example uses a USD 100,000 order (§4.2) as the illustrative large case; that is the tail, not the mean. **Scale by segment: S1/S6 at 1.6× base, S2/S4 at 1.0×, S3 at 0.45×, S5 at 0.7×** | **Low. No published source; judgement call** |
| S47 | Spot frequency, among attaching accounts | 1.7 | 2.4 | 1.2 | events/attaching account/yr | Heavily seasonal — see S48(a); roughly 45% of spot volume falls in the Akshaya Tritiya (Apr/May) and Diwali (Oct/Nov) windows | Low |
| — | **Late/arrears money is spot volume, and this is a corpus rule not an assumption** | | | | | `_draft_sip-rulebook.md` §1 and §7.1: extra money inside a month is a spot purchase, and arrears buy gold at the fix on the day they clear. **So the arrears lane feeds the spot lane.** Size it from the archetype mix: occasional and alternating missers (47% of the base combined) generate ~0.9 missed periods per account-year between them, of which the corpus's 12-month revival window suggests **25-35% are made good.** That is roughly **0.11 arrears events per live account per year at Base**, at the segment's own ticket size. Small in value, but it is free volume on an existing rail | **Medium.** The mechanism is corpus-settled; the revival take-up rate is a judgement call |

**Why the spot lane is the highest-margin flow in the business, with the arithmetic:**

Take a USD 620 spot ticket against a USD 75 SIP contribution, both at the Y1 5% fee, using the brief's own §0.1 build-up:

| Line | SIP, USD 75 | Spot, USD 620 |
|---|---|---|
| Gross margin at 5% fee less 3% premium and 0.79% price-gap and 0.49% float CoC | 0.54% → USD 0.41 | 0.72%¹ → USD 4.46 |
| Rail (ONE event either way, S1 = USD 0.25) | (0.25) | (0.25) |
| **Net margin** | **USD 0.16** | **USD 4.21** |
| **Net margin as % of ticket** | **0.21%** | **0.68%** |

¹ *Spot pays the same variable cost rate but, per `_draft_sip-rulebook.md` §1.1, is priced at the account's earned tier — so it carries the same tier discount as SIP. The 0.72% is the pre-rail gross margin from the brief's §6.1.*

**The whole difference is the fixed rail spread over a 8.3× larger base.** This is the brief's own §0.2 equation `Net = C × (f − c) − R` running in Aurumix's favour instead of against it. At the Conservative rail (S1 = USD 1.36, UAEDDS pricing), the SIP contribution **loses USD 0.82** while the spot ticket still **earns USD 3.10.**

**That is the finding, and it is a strong one: the spot lane is the only inflow-linked flow that survives the adverse rail scenario.** The brief's §0.2 says "at the client's own target ticket, on published tariffs, the SIP loses money on every collection" and treats that as a terminal problem. It is not terminal if spot volume is material, because spot is immune to the thing that breaks the SIP. **Model spot before concluding stream 1 is unsalvageable.**

Two qualifications that keep this honest. Spot earns no ICS (`_draft_sip-spot-and-ics.md` §1), so it builds no tier, no card eligibility and no credit eligibility — **it is margin without a funnel**, and the brief's §0.4 conclusion that the SIP is an acquisition mechanism for the card still holds. And spot volume is lumpy and seasonal, so it cannot be relied on to cover a fixed cost base. **Spot improves the margin on stream 1; it does not change what the business is.**

---

## Block G — Costs and tax

### G1. Opex interpolation rule (F32 / S48-series)

**Which blocks step and which scale:**

| Block | Behaviour | Interpolation | Month booked |
|---|---|---|---|
| Headcount | **Step** | Hire plan, quarterly steps; interpolate log-linearly *between* the Y1/Y3/Y10 anchors then round to whole-FTE quarterly steps | Monthly, 1/12 of annual, from the hire month |
| MLRO | **Step, then folds in** | Outsourced flat Y1-Y2; in-house from Y3 (brief's own note); **decay the standalone line to zero linearly Y3→Y10 as it merges into Headcount** | Monthly |
| VARA supervision | **Step** | Flat AED 200,000 (F14) until an activity is added; step at the year an additional licence is taken | **Booked in full in the licence anniversary month**, not spread. This is an annual invoice |
| Audit + reserve attestation | **Step** | Tech audit annual + one per product launch (§7.4 correction 1); reserve attestation **every six months** (correction 2) | Tech audit in the anniversary month; **attestation in months 6 and 12 of each year** |
| Compliance tooling + KYC | **Scale**, with a floor | `max(Sumsub minimum USD 299/mo, per-check rate × KYC volume)` — the minimum binds below 162 checks/month (F16) | Monthly |
| Vault and metal | **Scale**, with a floor | `max(USD 25/day minimum, 0.10/kg/day × kg held)` — the minimum binds below ~250 kg (§7.4 correction 3) | Monthly |
| Technology | **Scale** | Log-linear on account count | Monthly |
| Corporate (licence, office, visas) | **Step** | DMCC licence renewal is annual and lumpy; office steps at headcount thresholds | **Licence in the incorporation anniversary month**; office monthly |
| Security | **Step** | Log-linear then rounded to annual steps | Monthly |
| Marketing | **Scale** (a decision variable, not a cost) | Set by the acquisition plan and the CAC curve (S25). **Should be an input to acquisition, not an output of an opex table** — v1.0 has it in both places | Monthly, seasonalised per S49(a) |
| Legal, insurance, contingency | **Step** | Log-linear, rounded to annual steps | Insurance in the policy anniversary month; the rest monthly |

**Functional form for the missing years.** Use **log-linear (constant-CAGR) interpolation within each block separately**, not on the total:

`v(y) = v(anchor_low) × (v(anchor_high) ÷ v(anchor_low)) ^ ((y − y_low) ÷ (y_high − y_low))`

with anchors at Y1→Y3 and Y3→Y10. Log-linear rather than straight-line because every block anchor pair implies a growth rate, not a growth increment, and straight-line interpolation between Y3 and Y10 would put Y4 opex ~13% too high. Marketing uses straight-line from a zero Y1 base (log-linear is undefined at zero).

**Values for the missing years (block-level log-linear, Base scenario):**

| Year | Total annual opex, USD | Note |
|---|---|---|
| Y1 | 894,800 | Brief's 845,800 + MLRO treated as a separate line |
| **Y2** | **1,478,420** | |
| Y3 | 2,484,700 | vs the brief's 2,506,000 — **0.9% under**, residual is the Marketing block's linear treatment |
| **Y4** | **2,929,793** | |
| **Y5** | **3,475,359** | |
| **Y6** | **4,143,676** | |
| **Y7** | **4,962,115** | |
| **Y8** | **5,964,336** | |
| **Y9** | **7,191,778** | |
| Y10 | 8,695,500 | vs the brief's 8,495,500 — **2.4% over**, same residual |

**Reconciliation instruction:** apply a proportional plug to the Marketing block at Y3 and Y10 so the interpolated totals tie exactly to the brief's published anchors. Do not adjust the other blocks — Marketing is the only block that is a decision variable, so it is the correct place to absorb the residual.

**One correction the interpolation surfaces.** Y2 at USD 1.48m against Y1 at USD 0.89m is a 65% step, and Y3 against Y2 is another 68%. **The brief's Y1 opex is not a running rate — it is a partial year of a business that has not finished hiring.** The model should either carry an explicit hire schedule for Y1 (preferable) or flag that the Y1 figure understates the exit run-rate by roughly 40%. A break-even calculation run against an understated Y1 cost base flatters the early years.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| F32 | Opex interpolation form | Log-linear within block, on the Y1/Y3/Y10 anchors | — | — | — | Derived from the brief's own §7.4 table. **The block-level step/scale classification is the substantive fill; the interpolation is arithmetic** | **Medium.** Anchors carry the brief's own confidence ratings (Headcount Low-Med, VARA High, etc.) |
| S48 | Y1 exit-run-rate uplift | 1.40× the Y1 average | 1.25× | 1.60× | × Y1 booked opex | The Y1 figure is a build-up year average, not a run-rate | Low-Medium |

### G2. Tax and VAT

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| F33 | UAE corporate tax rate | 9% on taxable income above AED 375,000; 0% at or below | — | — | % | Federal Decree-Law No. 47 of 2022. Widely reported and consistent across sources | **High** on the rate and threshold |
| F34 | Loss carry-forward | **Indefinite carry-forward; utilisation capped at 75% of the taxable income of the year in which it is used** | — | — | — | Article 37, Federal Decree-Law No. 47 of 2022. Subject to ownership-continuity and business-continuity tests (anti-loss-trafficking) | **Medium-High.** Consistent across multiple secondary sources; not read at primary text |
| F35 | **QFZP treatment — the modelling rule** | **Assume Aurumix is NOT a QFZP. Tax at 9% on income above AED 375,000 from first profitability.** | Model a QFZP sensitivity at 0% as an upside case only | Same as Base | — | See reasoning below | **Low-Medium on the eligibility question; High on the recommendation to assume the adverse case** |

**F35 — why Base assumes no QFZP relief, which is the conservative call and the right one:**

Three reasons, and none of them is a tax opinion — they are modelling hygiene.

1. **Aurumix's revenue is overwhelmingly retail-facing.** Qualifying Income for a QFZP is essentially income from transactions with *other Free Zone Persons*, plus a defined list of Qualifying Activities. Aurumix's revenue comes from individual retail savers (entry fee), card interchange from acquirers, and a partner platform fee. **Retail customer income is the paradigm case of non-qualifying income.** Whatever the answer on the activity list, the customer base points the wrong way.
2. **The de minimis relief cannot save it.** Non-qualifying revenue is tolerated only up to the lower of 5% of total revenue or AED 5 million. Aurumix's non-qualifying share would be close to 100%, not 5%.
3. **The asymmetry of the error matters.** A QFZP that loses its status loses it for the tax period **and the four following tax periods** — a five-year cliff. And critically: **a QFZP does not get the AED 375,000 zero band on its non-qualifying income.** So a failed QFZP is taxed *worse* than a plain mainland company on the same income. **Modelling 0% and being wrong is a five-year, no-safety-net error; modelling 9% and being wrong is upside.**

**Modelling rule, stated for the build:**

```
taxable_income(y)  = accounting_profit(y) − loss_bf_utilised(y)
loss_bf_utilised(y)= MIN( loss_pool(y−1), 0.75 × MAX(0, accounting_profit(y)) )
tax(y)             = 0.09 × MAX(0, taxable_income(y) − 375,000)
loss_pool(y)       = loss_pool(y−1) − loss_bf_utilised(y) + MAX(0, −accounting_profit(y))
```

Book tax **annually, in the final month of the financial year**, never monthly. With break-even at Y7-Y9 in the brief's View 2 and a large accumulated loss pool from Y1-Y7, **the 75% cap means Aurumix pays real cash tax from its first profitable year even though it is cumulatively loss-making** — it cannot shelter the full profit. This is a genuine cash-flow finding the v1.0 model has no line for.

⚠ **Get a tax opinion before the model is presented as final.** The QFZP question is a real one and the answer is worth roughly 9% of terminal profit — about USD 220,000/yr at the brief's Y10 net of USD 2.47m. Not model-breaking, but not nothing.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| F36 | VAT — resident rate | 5% standard-rated | — | — | % | UAE VAT standard rate. Applies to service fee lines (entry fee, family plan, cardholder fees) supplied to UAE-resident customers | **High** on the rate, **Low** on the characterisation of each fee line |
| F37 | VAT — non-resident treatment | 0% (export of services) | — | 5% (treated as resident throughout) | % | Export-of-services zero-rating. **The brief's §6.4 and §14 both flag this as unresolved and as *possibly a structural margin advantage rather than a cost* — that reading is correct and it is worth quantifying** | **Low.** Unverified; the corpus flags it as needing a tax opinion in three separate places |
| S49 | Resident share of the customer base, by segment | S1 100% / S2 100% / S3 100% / S4 0% / S5 0% / S6 0% | same | same | % UAE-resident | **This one is not a judgement call — it falls straight out of §5's own segmentation.** Decision 31 re-cut the segments by *country of residence* precisely so that residence-dependent rules could bind. S1-S3 are UAE-resident by definition; S4 (Oman+Bahrain), S5 (India) and S6 (other international) are non-resident by definition | **High on the split** (it is definitional), **Low on the VAT consequence** |

**What S49 does to the P&L, which is the point of carrying it:**

At the Base channel mix and segment ramp, the **non-resident share of the book rises from 0% in Y1 (S1-S3 only) to roughly 42% by Y10** (driven by S5 India and S4 GCC). If the export-of-services zero-rating holds, **VAT is not a cost on 42% of fee revenue by Y10** — against a competitor set that is UAE-resident-facing and pays 5% on all of it.

Worth roughly **USD 130,000-190,000/yr at Y10** on the fee lines. **The brief's framing is right: on this base, the international perimeter is a VAT advantage and not merely a licensing cost.** It is also a genuine argument for prioritising the S4/S5/S6 perimeter that has nothing to do with market size, and the client has not heard it.

⚠ **Two cautions.** Recoverability of input VAT is affected by the mix of zero-rated and standard-rated supplies, so the benefit is not a clean 5% — model it at 5% and haircut by 20% for input-VAT drag. And **investment-grade precious metals may be zero-rated in the UAE regardless of residence**, which the corpus already flags (`_draft_entities-licensing-and-payments.md` §353) — if the entry fee is characterised as part of a supply of gold rather than a supply of services, the resident/non-resident distinction may not matter for stream 1 at all. **Three separate corpus files flag VAT as unresolved. It should be one of the questions in the tax opinion, not a modelling assumption.**

### G3. Float funding

**The corpus sizing rule, extracted verbatim from `_draft_allocation-and-float.md`:**

> **`float ≥ one bar denomination + a buffer of N days' trailing inflow.` Two bars is the launch setting.**

Expressed as a model input:

```
float_grams(t)     = MAX( 2 × bar_grams(t),
                          bar_grams(t) + N_buffer_days × daily_inflow_grams(t) )
float_capital(t)   = float_grams(t) × gold_price × (1 + fabrication_premium(t))
float_coc_cost(t)  = float_capital(t) × cost_of_capital ÷ 12
```

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| F38 | Float sizing rule | `MAX(2 bars, 1 bar + N days trailing inflow)` | — | — | grams | **`_draft_allocation-and-float.md`, "Sizing" section, verbatim.** Not an assumption — a corpus-settled rule | **High.** Corpus-settled |
| S50 | Buffer days (N) | 10 | 6 | 20 | days of trailing inflow | The rule states N without setting it. 10 days is roughly the Y1 fill window (8.7 days at 100 g, corrected to 12.1 days at the corrected gold price per the brief's §6.1) | **Low-Medium.** The rule is corpus; N is ours |
| S51 | Float carry mode | **Dealer-carried at launch, own float from the year the denomination upgrade clears (Y3)** | dealer-carried throughout | own float from M1 | — | Corpus working recommendation: *"launch dealer-carried, migrate to an own float once volume makes internalising the spread worth the capital."* **Under dealer-carried, float capital is ZERO and price-gap risk plus float CoC drop out of Aurumix's column (~0.85% at Y1 on the old numbers, ~1.28% on the corrected ones) and are replaced by a wider dealer spread** | **High on the fork existing, Low on which side is taken** — the corpus says explicitly it is decided by what the dealer will agree to, and the dealer is unnamed |
| — | **Float capital requirement by year (own-float case), at the corrected gold price** | Y1 ~USD 29k / Y3 ~USD 437k / Y10 ~USD 3.6m | | | USD | The corpus table (USD 22k / 330k / 2.7m) was computed at **USD 109.31/g**. At the corrected **USD 141.46/g (F1)** these rise by 29.4%. **This is correction 1 in the brief's §13 propagating into the float table, which §13 does not currently list.** Add it | **Medium.** Arithmetic is certain; the underlying inflow assumptions carry the model's own confidence |

**Two things the model must not do with the float, both corpus rules:**

- **Do not run float capital through the P&L.** It is a balance-sheet item. Only the *cost of carrying* it (S51 → F5 float CoC) hits the P&L. This mirrors F15's treatment of the AED 1.5m minimum capital — the brief already says *"Locked, not expensed. Do not run through P&L."*
- **Do not net the float against the VARA minimum capital without counsel.** The corpus flags this directly: *"[COUNSEL] whether allocated gold inventory can sit inside that requirement."* If it can, the true incremental capital need at Y1 is roughly zero, because AED 1.5m (~USD 408k) is posted anyway and dwarfs a USD 29k float. **If it cannot, the two stack.** At Y1 this is immaterial; at Y10 the float is USD 3.6m against an AED 1.5m minimum and the question is worth a real answer.

### G4. Seasonality

| ID | Parameter | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S52(a) | **New account acquisition** multiplier | 1.05 | 0.95 | 0.95 | **1.20** | 0.90 | 0.85 | **0.80** | 0.85 | 1.05 | **1.30** | **1.20** | 0.90 | **12.00** |
| S52(b) | **Card spend** multiplier | **1.10** | 0.95 | 0.95 | 1.00 | 0.90 | 0.85 | 0.90 | 0.95 | 1.00 | **1.10** | **1.15** | **1.15** | **12.00** |

Both vectors normalise to exactly 12.00, so applying them cannot change the annual total — only its distribution. **This is a hard build requirement: an un-normalised seasonality vector silently changes the model's annual answer, which is one of the more common ways a monthly model goes wrong.**

**The reasoning, driver by driver:**

| Driver | Timing | Effect on acquisition | Effect on card spend |
|---|---|---|---|
| **Akshaya Tritiya** | Apr/May (Vaishakha, movable) | **Strong positive.** The single most auspicious day in the year to buy gold in Indian culture — the entire Indian gold retail trade plans around it. Drives the Apr 1.20 | Neutral (it is a gold purchase, not card spend) |
| **Diwali / Dhanteras** | Oct/Nov (movable) | **Strongest positive.** Dhanteras is *specifically* the day for buying precious metal. Drives Oct 1.30 and Nov 1.20 | Positive — gifting and retail. Drives Oct/Nov 1.10/1.15 |
| **Indian wedding season** | Nov-Feb, and Apr-May | Positive, reinforcing both peaks | Positive |
| **Ramadan / Eid al-Fitr** | Movable, currently ~Feb-Mar and drifting ~11 days earlier per year | **Mildly negative for acquisition** — a distracted, reduced-working-hours month in the UAE for enterprise and agent activity | **Mildly positive for spend** — Eid gifting and retail promotion are large in the UAE, partially offsetting the Ramadan working-hours drag. Net ~neutral |
| **Dubai Shopping Festival** | Mid-Dec to end-Jan | Neutral to slightly negative for acquisition (competing for discretionary money) | **Strong positive.** Drives Dec 1.15 and Jan 1.10 |
| **Summer travel / exodus** | Jun-Aug | **Strongly negative.** A large share of the UAE Indian community travels to India for extended periods. Agents cannot meet people; direct-debit setup and KYC stall. Drives Jul 0.80 | **Mixed and this matters:** total spend dips (fewer people in-country) but **foreign spend share spikes**, which is FX-margin-bearing revenue. Net effect on *stream 4* may be positive even though total spend falls |

**The one build instruction that matters most here — and it is not the numbers:**

**Apply S34 (foreign spend share) as a seasonal vector, not a constant.** The summer months should carry a foreign-spend share of roughly **55-60%** against a 34% annual average, and Oct-Nov (Diwali travel and India-facing gifting) roughly **42%.** Because **FX margin is a revenue line at 2.0/1.5/1.0% by tier**, the summer travel season is the model's single largest stream-4 month even though it is the weakest total-spend month. A flat foreign-share assumption applied to a seasonalised spend vector gets the sign of the summer effect backwards.

**Two cautions on the vectors.** Diwali, Akshaya Tritiya, Ramadan and Eid are all **lunar or luni-solar and move materially between Gregorian months year to year** — Diwali can fall in mid-October or mid-November, Ramadan drifts ~11 days earlier annually. Over a 10-year model the drift is large enough to matter: Ramadan moves from roughly February in 2027 to roughly November by 2036. **Either build a festival-date lookup table by model year, or accept the fixed vector and note that it is a Year-1-anchored approximation.** The fixed vector is defensible for a business-planning model and the lookup table is not worth the build cost; but it should be a stated simplification, not an unnoticed one.

And: seasonality only affects the **monthly** block, M1-M60. In the annual block Y6-Y10 it cancels by construction, which is a further argument for the hybrid granularity the brief already chose.

| ID | Parameter | Base | Aggressive | Conservative | Unit | Basis | Confidence |
|---|---|---|---|---|---|---|---|
| S52 | Seasonality vectors (a) acquisition and (b) card spend | tables above | amplitude × 1.4 | amplitude × 0.6 | multiplier, normalised to 12.0 | Festival timing and cultural gold-buying behaviour are well-established facts; **the amplitudes are ours.** Akshaya Tritiya and Dhanteras as gold-buying peaks is not in dispute anywhere; how much a Dubai-based savings-product signup responds to them is | **Medium on the shape** (the drivers and their direction are solid), **Low on the amplitudes** (no published source quantifies festival elasticity for a UAE diaspora savings product) |
| S53 | Foreign-spend seasonal vector | 30/30/30/32/34/**55**/**60**/**56**/36/42/40/32 (Jan-Dec), mean 39.8% → rescaled to hold the S34 annual mean at 34% | — | — | % of monthly card spend | See build instruction above | **Low. No published source; judgement call** |

---

## Load-bearing versus cosmetic

### Load-bearing — the model's output moves materially with these

| Rank | ID | Parameter | Why it carries |
|---|---|---|---|
| 1 | **S27** | Payment archetype mix + background hazard | It **is** the persistency curve, which the brief already ranks as one of its five load-bearing assumptions (S2). It additionally determines the ICS tier distribution, which the brief says is "computed, not assumed" but which v1.0 supplies no input to compute. **Everything downstream of tier — card eligibility, credit eligibility, benefit costs, the entire T4/T5 row — flows from this single table.** Get it wrong and T4/T5 are fiction |
| 2 | **S40** | Facility turnover / peak-to-average conversion | **Roughly halves stream 5.** Not because it is uncertain, but because v1.0 does not apply it at all and therefore books peak drawn as though it were persistent. This is an arithmetic correction, not a sensitivity |
| 3 | **F24 + F23** | Per-transaction fee against tier ticket size | Takes **11% of gross interchange at Gold tier** and stacks multiplicatively with the PM share, which the brief already ranks as its single most valuable commercial number. **The effective PM share on small tickets is well below the contracted one, and stream 2 is 54% of terminal revenue.** The brief flagged this gap and did not close it |
| 4 | **S33** | Lapsed-holder redemption multiplier | At 19% M61 persistency, **81% of ever-acquired accounts are lapsed by Y6.** This multiplier governs the dominant AUM decay term from ~Y4, and AUM drives stream 6, custody absorption and the entire credit collateral base. **v1.0 has no lapsed-holder AUM decay term at all** |
| 5 | **S23 + S22** | Saturation form and penetration ceilings | The only thing standing between the model and an implausible Y8-Y10 hockey stick. Using **cumulative-ever-acquired** rather than live accounts in the saturation denominator is the specific mechanism, and at 5x cumulative-to-live by Y10 the choice is decisive |
| 6 | **F27** | Card programme fixed costs | A minimum-commitment structure that binds at low volume, exactly like the vault and Sumsub minimums. **Runs the card at a loss for 12-18 months in the Conservative case**, drag that the brief's View 2 break-even table does not carry |
| 7 | **S16** | Channel-to-segment mix | Decides which segments the model fills, and therefore which tickets the fixed rail is spread over. Given §0.2's non-linearity in ticket size, **this is the parameter that determines whether the agent channel is profitable at all** |
| 8 | **S45-S47** | Spot attach, ticket, frequency | Currently zero in the model. **Spot is the only inflow-linked flow that survives the adverse rail scenario**, so it changes the answer to the brief's most alarming finding. Load-bearing because it is missing, not because it is large |
| 9 | **F35** | QFZP assumption | Worth ~USD 220,000/yr at Y10 net. Below the top tier because the *conservative* treatment is clearly correct, so the risk is one-directional upside rather than a modelling error |
| 10 | **S28 + S29 + S30** | Reduction capture, depth and hazard | Together they set the gap between the revenue curve and the account-survival curve, which the brief calls "one of the few genuine structural advantages Aurumix has." **S29 in particular corrects a real v1.0 error** (the hard-coded USD 20 reduced ticket) |

### Cosmetic — get them roughly right and move on

| ID | Parameter | Why it does not matter much |
|---|---|---|
| F21, F22, S36, S37 | Card issuance and replacement fees and event rates | A few AED per card per year against AED 6,000/month of spend. **Rounding error on stream 4** |
| F25 | Dispute handling cost per case | ~0.9 cases per 1,000 transactions at USD 22. Immaterial at any modelled volume |
| F26 | Card production unit cost | One-off USD 4.50-14.00 against a multi-year cardholder relationship generating hundreds of dollars of interchange |
| F20 | Cost per redemption event | ~USD 25-35k/yr at Y10 against USD 11m of revenue. **Interesting as a *structural* finding (a mandatory zero-revenue cost line) but not as a number** |
| F30 | Penal fee rate and share | Expected value of ~USD 4/borrower/yr. The *reasoning* for setting Aurumix's share low is worth more than the number |
| S26 | Organic share of direct | Reallocates volume between two sub-channels of the same channel. Affects the CAC calculation slightly, affects nothing else |
| S52(b) | Card spend seasonality | Normalised to 12.0, so it **cannot change the annual total** — it only redistributes within the year. Matters for cash-flow timing and for nothing else |
| F31 | Recovery fee | Modelled at zero. A parameter set to zero for a defensible legal reason is not a sensitivity |
| S18 | Agent attrition | Load-bearing-adjacent — it grosses up the recruit count by ~15-20% at steady state — but it acts on S12 and S17, which are already flexed. Flexing all three independently double-counts |

### One meta-observation for the v2.0 rewrite

**Three of the fills above are not new parameters at all — they are corrections to v1.0 arithmetic that happened to surface while filling gaps.** They should be routed into the brief's §13 "Corrections owed to Phase 2" table rather than buried in an assumptions register, because §13 is where a reader looks for things that were wrong:

1. **§3 Layer 3 hard-codes the reduced ticket at USD 20** (should be per-segment, S29).
2. **§6.5's stream 5 formula computes peak drawn and prices it as persistent** (needs S40; halves the stream).
3. **The float capital table in `_draft_allocation-and-float.md` is still at USD 109.31/g** — correction 1 in §13 propagates there and §13 does not currently say so. Float capital rises 29.4% at every year.

And one confirmed negative worth adding to §15, because the brief's house style treats these as findings: **no published source decomposes a savings-product or insurance lapse curve into payment-behaviour archetypes.** The aggregate curves are published in quantity (IRDAI, AMFI); the behavioural decomposition underneath them is not published by anyone. The archetype table in S27 is a construction fitted to a researched aggregate, and it should be labelled as one.agentId: a3048cf37c6cab49b (use SendMessage with to: 'a3048cf37c6cab49b' to continue this agent)
<usage>subagent_tokens: 138623
tool_uses: 36
duration_ms: 750591</usage>