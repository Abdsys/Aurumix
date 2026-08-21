# Aurumix — Revenue Model Architecture Brief (Simplified)

**Version 3.0 — simplified build, 2026-08-20**
**Supersedes** `Aurumix_Revenue_Model_Architecture_Brief.md` (v2.6) as the specification for the Excel
workbook. The v2.6 brief is **retained in full** as the research and provenance record: every source,
confirmed negative and correction referenced here lives there and is not repeated.

**Deliverable:** `tools/Aurumix_Revenue_Model.xlsx`, built by `tools/build_revenue_model.py`,
verified by `tools/verify_model.py` (**89 checks**) against a LibreOffice recalculation.

---

## 0. Why this version exists

The v2.6 architecture was correct and unbuildable as a client artefact. It specified five payment
archetypes, a run-of-6 first-passage Markov chain, 84-month lifecycle curves, a convolution engine, a
six-state machine and a six-bucket withdrawal distribution — roughly **9,000 formulas** across ten
sheets, of which five were hidden machinery.

That engine was built and validated. It reproduced every published anchor:

| Anchor | v2.6 target | Built engine |
|---|---|---|
| Persistency M13 / M25 / M37 / M49 / M61 | 55 / 40 / 30 / 24 / 19% | 54.7 / 40.5 / 31.0 / 23.8 / 18.3% |
| Mean gate arrival | M8.1 | M8.00 |
| Ever-gate share | 53.5% | 54.8% |
| Holding-not-contributing at M61 | ~81% | 81.7% |

**It then produced two numbers, and those two numbers are all the Excel model needs.** Everything else
the engine did was resolution the spreadsheet cannot use and the client cannot audit.

🔴 **Provenance gap — the anchors above are currently unverifiable from the working tree.** The five
persistency anchors were validated in `reference_model/VALIDATION.md`, which is among the ~53 deleted
reference-model files. **Persistency 55% is the single most load-bearing input in the model** — it drives
the whole churn engine — so a number whose sources cannot be produced on request is a live audit risk.
Restore that file, or re-source the anchors, before this model goes to the client.

**Decision, 2026-08-20:** the engine moves to the Phase 5 simulation, where heterogeneity belongs and
where it can be run stochastically rather than deterministically. The Excel model keeps its *outputs* as
two input cells. **A model the client cannot follow is worth less than a simpler one they can.**

⚠ **This is a scope decision, not a finding reversal.** Every v2.6 finding still stands. What changes is
where each one is *expressed* — as machinery, or as a parameter.

---

## 1. Scope

| Field | Value |
|---|---|
| **Product** | AURX, a VARA-regulated gold-backed monthly savings product in Dubai. 1 AURX = 1 gram of allocated physical gold |
| **This model covers** | **REVENUE ONLY**, reported net of cost of revenue |
| **Deferred to a later build** | Operating expenses, headcount, tax, working capital, cash, funding, break-even |
| **Horizon** | 7 years, M1 = January 2027 |
| **Granularity** | 29 periods: 24 monthly (M1–M24) + 5 annual (Y3–Y7) |
| **Currency** | USD primary, AED at the peg 3.6725 |
| **Sheets** | Five: Cover, Assumptions, Scenario Parameters, Model, Summary |

**Why revenue first.** The P&L is additive: revenue and operating cost can be built and reviewed
independently, and the cost side depends on an account trajectory that only the revenue side produces.
Building revenue first means the cost build has a book to size itself against.

⚠ **The one cost-like item in scope is the fabrication premium, and the customer bears it.** Aurumix
charges 5% and buys metal at roughly spot + 1.5%. Because the customer's money is spent at
spot-plus-premium, they receive **fewer grams** — so the premium is already paid, by them, and the entry
fee reaches Aurumix **whole**. See §3.3 for the arithmetic and for the double-count this replaced.

---

## 2. The engine

```
opening customers  +  new  −  churned  =  closing customers
                                └──────►  HOLDERS (stopped paying, still hold gold)
```

That is the whole population model. It runs per region (R1–R4) and totals up.

**New customers** come from three channels — **salesforce, paid marketing, referrals** — subject to a
saturation brake and acquisition seasonality:

```
new(t) = ( agents(y) × productivity × ramp(y)
         + marketing(y)/12 ÷ CAC × (1 + organic)
         + paying(t−1) × referral_rate/12 × conversion × referral_flag )
       × saturation(t) × seasonality(month) × months_in_period
```

**Saturation runs against cumulative-ever-acquired, never live customers.** A lapsed customer is a burnt
lead, not a returning one. The two denominators diverge steadily, and this is the term that stops the
model producing an implausible late-horizon hockey stick.

**Churn** is a single monthly rate, **derived** from the persistency input rather than typed:

```
monthly_churn = 1 − persistency_M13 ^ (1/12)          Base: 55% → 4.86%/month
```

Change persistency and churn follows. One number the client can argue with, instead of five archetypes
they cannot.

**The salesforce is deployed across every market — UAE 45%, Oman & Bahrain 10%, India 45%** (revised
2026-08-21). An earlier cut put 100% in India, which left the licensed home market with nobody selling.
Outside India the people are **salaried rather than commission-only**; for *revenue* that distinction does
not matter, since both are people acquiring customers at some productivity. ⚠ **It matters enormously for
cost** — a Dubai salesperson and an Indian commission agent are not the same expense — so this split must
be cost-weighted when the cost build lands.

⚠ **Not to be confused with stream 6.** The salesforce is **B2C**: people selling to consumers. Stream 6
is **B2B**: partners white-labelling the platform onto their own customer books. Different motion,
different economics, not a substitute for one another.

The regional shares are **renormalised across open regions**, so a market still in licensing redistributes
its people to the markets that are live rather than idling them.

🔴 **Setting a non-zero Gulf share exposed a latent gating bug.** While the split was 100% India, no agent
output was ever routed to an unopened region, so the *missing* opening gate on the agent channel was
invisible — the direct and referral channels were gated all along. Giving Oman & Bahrain a share made it
fire immediately: the region earned revenue in M12, one month before it opens. Now gated and covered by a
check. **A parameter sitting at zero can hide a structural defect indefinitely.**

**Regions.** The three regions differ by average ticket, salesforce share, marketing share and CAC.

---

## 3. The four things kept as inputs rather than deleted

Each of these was an engine in v2.6. Each is now one or two cells. Each is kept because **dropping it
changes the answer by more than the simplification saves.**

### 3.1 Card eligibility — two cells

| Cell | Base | What it replaces |
|---|---|---|
| Customers who **ever** clear the six-payment gate | **55%** | The run-of-6 first-passage chain |
| Average **months** to clear the gate | **8** | The gate-arrival distribution |

🔴 **This is the most load-bearing pair in the model.** The card streams are ~83% of gross profit and
every one of them requires clearing the six-payment gate. A plain churn model implicitly assumes everyone
qualifies immediately; the measured error is **+59%**. Gate arrival is a *distribution*, not a date — a
customer who misses month 4 cannot qualify before month 9, and roughly 45% never qualify at all.

The two extra months over the naive M6 are full-fee revenue carrying no benefit cost, and they push every
downstream date to the right.

### 3.2 The holders balance — one row

Customers who stop paying **keep their gold**. They stay in AUM, in custody cost, in the collateral base
and in the B2B AUM base, and they remain in AML screening indefinitely. They reach ~81% of everyone ever
acquired by Y6, and they are the **dominant AUM decay term from roughly Y4** because they redeem faster
than payers (no accruing benefit left to protect).

Without this row, AUM is badly understated and streams 5 and 6 go with it.

⚠ **"AUM" in this model means COLLATERAL-ELIGIBLE AUM, and the rows are named that way** (relabelled
2026-08-21). Two things reduce it, and only one of them is gold actually leaving:

| Row | What happens to the metal | Why it leaves the base |
|---|---|---|
| **Redemption** | Tokens burned, gold **sold**. Genuinely gone. | It no longer exists |
| **Gold moved out of Aurumix's control** | **Nothing. It stays in the vault.** | Aurumix cannot foreclose on a token in a private wallet, so it can no longer back a credit limit |

The second row was previously called *self-custody leakage* and described as decreasing AUM, which the
client correctly challenged: a token moving to a customer's own wallet sells nothing and burns nothing.
The arithmetic was never wrong — in this model **AUM has exactly one consumer, the card credit limit** —
but the label was.

🔴 **That single-consumer property is what makes the shared row safe.** If a later build points anything
else at AUM — a custody fee, an AUM-based B2B fee, a reported-AUM headline — the two effects diverge and
this row must be split in two *before* that reference is added.

### 3.3 Who bears the fabrication premium

**The customer does — once.** On a USD 100 contribution:

| | |
|---|---|
| Customer pays | **100.00** |
| Entry fee 5% → Aurumix | **5.00** |
| Remainder, spent on metal | 95.00 |
| Metal costs spot + 1.5%, so the customer receives | **93.60** of gold at spot |

The premium is borne in **grams delivered**, not in Aurumix's fee. In the model this is the `(1 + premium)`
divisor on *Grams purchased*; stream 1 earns the headline 5%. This matches standard gold-product practice,
where the quoted price already includes the dealer spread.

⚠ **This replaced a genuine double-count** (fixed 2026-08-21). An earlier cut applied the divisor to grams
*and* netted the premium off the fee — `5% − 0.95 × 1.5% = 3.575%` — charging the same USD 1.40 per 100
twice, once to the customer and again to Aurumix. Only one side of a trade can pay a spread. Two paired
checks in `verify_model.py` now assert the incidence is single-sided, so the pair cannot silently return.

**If this decision is ever reversed** and Aurumix absorbs the premium instead, the `(1 + premium)` divisor
on *Grams purchased* must be removed in the same edit — the customer would then receive the full 95.00 of
metal. Changing one without the other reintroduces the bug in whichever direction it is changed.

### 3.4 The ATM draw distribution — four rows

The mean draw (~AED 940) sits **deliberately just below** the free allowance (AED 1,000). Applying the fee
to the mean returns **exactly zero**, and stream 4 silently loses a component. The distribution returns
materially more, generated almost entirely by a small high-cash tail. This is a Jensen error in miniature
and it points the opposite way to the usual one.

### 3.5 Market sizing, and why it is not built from platform user counts

The funnel derives the market from **population × three capacity filters × a penetration ceiling**. The
alternative — start from the published user counts of digital gold platforms and apply a penetration % to
those — was researched and rejected 2026-08-21. It is a better idea in principle, because it starts from
proven behaviour rather than judgement filters. The published data cannot carry it:

| Problem | Evidence |
|---|---|
| **"Users" is not a defined unit** | The *same* UAE product is reported at **8.5m** (can access), **1.5m** (users), **775,000** (explored) and **75,000** (active). A **113× spread** — choosing between them is a judgement as large as any filter it replaces, but it would *look* like an observation |
| **India cannot be deduplicated** | Jar 35m registered, Augmont 42m; the same person is on several. **No estimate of unique digital gold investors exists** — a confirmed negative. Registered ≠ active either: Augmont runs 0.85 transactions per registered user per year |
| **Oman & Bahrain has no user count at all** | So the method could not be applied uniformly — which was its main appeal |
| 🔴 **Behaviour is not capacity** | A Jar user saving ₹10/day proves they will buy gold digitally. It does **not** prove they can commit ₹2,640/month to a SIP. The filters are not measuring appetite for gold — appetite is not in doubt — they measure capacity for a **recurring** commitment |

⚠ **India's base already uses that method, and it is the least traceable number in the model.** Its 12.5m
is *"holds a gold ETF folio or actively buys digital gold"*, which is why its three filters all sit at
1.00. That is the evidence a user-based method does not automatically produce a better-sourced figure.

**What the data is good for is a cross-check, and it passes.** A live memo row on Assumptions:

| | Derived funnel | Observed |
|---|---|---|
| UAE addressable base | 1.43m | **775,000** explored O Gold |
| UAE reachable SIP | 113,416 | **75,000** active O Gold users |
| | | **Ratio 1.51×** |

Two independent methods landing within ~2× is the strongest defence of the funnel in this model. The row
is **live**, so it moves if anyone raises a ceiling — that is the point. ⚠ **If the multiple drifts far
above ~2×, the ceiling has stopped being set by evidence and is being set by the answer someone wanted.**

---

## 4. What was deleted, and where it went

| Deleted from Excel | Where it now lives |
|---|---|
| Five payment archetypes, weights, pay probabilities, hazards | Phase 5 simulation |
| Run-of-6 first-passage gate chain | Phase 5 simulation; its output is §3.1 |
| 84-month lifecycle curves | Phase 5 simulation |
| The convolution | Replaced by the rolling balance |
| Six-state machine, REDUCED state | Phase 5 simulation; churn absorbs it |
| Six-bucket withdrawal distribution | Single leakage rate |
| Bar-denomination ladder, latch, 1 kg rung, Tradeflow switch | Deleted — 100 g throughout |
| Float cost of capital | Deleted entirely |
| Named narrative scenarios, per-parameter override, CUSTOM canary | Deleted — Base/Aggressive/Conservative only |
| `INDIA_ENABLED` | Deleted — the India route is **assumed solved** |
| Ten cost-side structural switches | Two kept (§6), the rest return with the cost build |

⚠ **The simulation now carries a dependency it did not have before.** Phase 5 is no longer optional
colour: it is where the 55% and the M8 come from, and where a change to the archetype mix would be
detected. **If the simulation is descoped, those two cells become unsourced assumptions.**

---

## 5. Revenue streams

Spot is a **sub-stream of 1**, not a seventh stream: same fee, same gold, different rail.

**The spot ticket is now OBSERVED per region** (rebuilt 2026-08-21), replacing a multiplier derived from
the regional SIP ticket. ⚠ Each figure is the size of **one purchase**, not an annual sum.

| Region | Ticket | Basis | Strength |
|---|---|---|---|
| **UAE** | **$190** | Botim gold, AED 700 avg ticket, Khaleej Times Nov 2025. Cross-checks against AED 100m ÷ 128k trades = AED 781 | **Strongest comparable in the model** — same country, same segment, same product |
| **India** | **$40** | Augmont, ₹3,300 festive purchase, Times of India Sep 2025 | Proxy — right behaviour, but our customer is poorer than Augmont's average buyer |
| **Oman & Bahrain** | **$145** | UAE scaled by the income gap (0.77×) | ⚠ **Inferred. No source.** Do not present as sourced |

🔴 **The old derivation was internally consistent and externally wrong.** It scaled spot off the SIP
ticket, on the logic that both proxy the same person's income. But SIP tickets barely differ across
regions ($33.60 / $26.00 / $30.00 — a 12% spread), so the derivation compressed the real gap into 12%
**and pointed it the wrong way**: it put India at **0.95×** the UAE where the published data puts it near
**0.20×**. Deriving a number from a related one imports that number's flatness. This is the argument for
observing regional parameters wherever a source exists.

**One scenario dial, not three.** Levels sit on Assumptions; a single *spot ticket scenario multiplier*
(0.70 / 1.00 / 1.35) carries the uncertainty. Three regional triplets would be nine numbers to defend and
would let a scenario silently invert the ordering the sources establish.

⚠ **Spot frequency (1.7/yr) is an assumption, not a citation** — provenance corrected 2026-08-21. The
earlier note derived it from "128,000 trades against ~45,000 buyers", but **the 45,000 is a transaction
count, not a buyer count**; the calculation divided transactions by transactions across two different
time windows. Botim has never published unique buyers, and **no published frequency exists anywhere for
ad-hoc lump gold purchases** — comparators run from 0.85/yr (Augmont, per registered user) to 264/yr
(Jar, ₹10/day roundups), a 300× spread bracketing a product that is neither. What supports 1.7 is a
cross-check on the **combined** basis: attach × frequency × ticket implies ~₹838/yr of gold per Indian
paying customer against Augmont's ~₹281/yr per registered user — 3×, and the right side to err on.

⚠ **Spot attach (14%) has no source either.** v2.6 records it as a confirmed negative — *"there is no
spot-attach benchmark for any comparable gold or savings product anywhere."* It asserts that the average
customer makes a one-off purchase about **once every four years** (14% × 1.7 = 0.238/yr). Augmont's
0.85 transactions per registered user bounds it but does not confirm it, their average transaction being
₹331 — micro-savings, not lumps.

⚠ **Flat attach is a known simplification with a known direction.** v2.6 applied a **tenure uplift** — *"a
3-year account is ~2× as likely to buy spot as a 6-month account"* — which v3.0 dropped. The rate is now
flat from day one, so if 14% was calibrated on a mature book, **spot is overstated in the early years**
when nearly every account is young. Not rebuilt, because spot is ~1.4% of Y7 revenue; the uplift belongs
in the Phase 5 simulation.

**Spot has no independent funnel, and that is deliberate.** v2.6 §6.1b: *"there is no independent spot
ceiling… spot is exclusively a behaviour of SIP accounts."* Re-confirmed by client decision 2026-08-21,
on economics: a spot-only buyer is worth `1.7 × ticket × 5%` a year — **$16 in the UAE, $3.40 in India**
— against a CAC of $120 and $20, a **6–8 year payback on spot revenue alone**. Paid spot acquisition is
dominated by simply acquiring a SIP customer with the same money. A spot funnel would only pay if buyers
arrived at near-zero marginal cost, and its value would then rest entirely on a conversion rate that has
no source. The dead `Spot-to-SIP conversion` parameter was removed in consequence.

**Confirmed negative, recorded so it is not re-searched:** no published average ticket or frequency exists
for South Asian expatriate or blue-collar customers in the Gulf specifically.

| # | Stream | Scales with | Activates |
|---|---|---|---|
| **1a** | Entry fee — SIP | Paying customers × regional ticket | M1 |
| **1b** | Entry fee — SPOT | Paying customers × attach × frequency × ticket | M1 |
| **2** | Card interchange | Card spend × rate × (1 − PM share), less per-txn fees | **M18** |
| **3** | Family plan and Digital Will | Paying customers × attach × price | M1 |
| **4** | Cardholder fees | FX margin + ATM over-allowance + issuance/replacement | **M18** |
| **5** | Lending revenue share | Average drawn balance and draw events | **Y3** |
| **6** | B2B platform fee | Partner AUM × bps | **Y3** |
| **0** | **Redemption — a mandatory COST** | Redemption events × unit cost | M1 |

🔴 **Streams 5 and 6 start at the beginning of the annual block (Y3), not as a stub month at M24.** A
one-month stub would give a stream a twelfth of a year's revenue in a column that then has to reconcile
against a full annual column beside it.

🔴 **Stream 0 is a finding, not a line item.** VARA Annex 2 Rule III.E.4 forbids charging any fee on
redemption, verified verbatim at primary source. **No offsetting revenue exists or can exist, and there
can never be an exit fee.** It is immaterial at Base rates — which is the reassuring finding — and becomes
material only in a stress scenario where redemptions spike, which is exactly when cash is scarcest.

---

## 6. Scenarios

**Base / Aggressive / Conservative. One switch, three columns.** Every parameter resolves through
`CHOOSE()` on the selector.

The v2.6 three-layer architecture (global switch, per-parameter override, six stored narrative scenarios)
is **withdrawn**. It solved a real problem — a global switch sets every parameter simultaneously, which is
a joint state of near-zero probability — but at a cost in comprehensibility the client should not pay.
Per-parameter sensitivity belongs in the simulation.

**Two structural switches are kept**, because both move revenue and neither is a sensitivity:

| Switch | Default | What it does |
|---|---|---|
| `Prepaid instead of credit` | Credit | Caps interchange at 1.00% and removes the credit stream. *"Not a product choice, it is the business model."* |
| `Holders keep the card` | ON | 🔴 **Nobody has decided this.** It determines whether the card streams — the majority of revenue — decay with churn or are immune to it. Worth a ~42% swing in terminal revenue. Report both |

---

## 7. Seasonality

Three vectors. Acquisition and card spend **normalise to exactly 12.000 by construction**, at any
amplitude — an un-normalised vector silently changes the model's annual answer.

| Vector | Shape |
|---|---|
| **Acquisition** | Peaks **Oct** (Dhanteras/Diwali) and **Apr** (Akshaya Tritiya); troughs **Jul–Aug**; wedding season Nov–Mar; Jan carries the Dubai Shopping Festival |
| **Card spend** | Peaks **Dec–Jan** (DSF, year-end); troughs **Jul–Aug** (summer exodus). Narrower than acquisition |
| **Foreign spend share** | Peaks **Jun–Aug** |

**Amplitude is damped to ±25% against the ±33% swing in raw Indian jewellery demand**, because committing
to a USD 20/month savings mandate is a materially less impulsive act than buying jewellery. That damping
is judgement and is exposed as a scenario parameter.

⚠ **Two traps avoided, both of which would have produced a wrong vector.**
1. India's **Q3 2024 demand spike (248.3t, +18% y/y) was an import-duty-cut artefact**, not seasonality.
   The sourced position is that Jul–Sep is the annual *low*. Fitting to 2024 quarterlies would have
   inverted the trough into a peak.
2. **Ramadan/Eid moves ~11 days earlier each Gregorian year**, so it rotates through the calendar across a
   7-year horizon. A fixed-month Eid bump would be **wrong by construction**.

✅ The card-spend and foreign-share vectors are deliberately **opposed**: Jul–Aug is the weakest
total-spend month and the strongest foreign-share month, which is what makes summer the largest stream-4
month on the smallest base.

---

## 8. The spot lane

v2.6 left four spot parameters `{{UNFILLED}}` with an instruction not to guess them. They are now filled
**by bracketing sourced anchors**, which is not the same as guessing: the range spans two things that are
known, and the uncertainty sits in the scenario range rather than hidden in a point estimate.

| Parameter | Conservative | Base | Aggressive |
|---|---|---|---|
| Spot payment capability | **0.57** — the sourced SIP mandate-capable figure | 0.71 | **0.857** — Findex UAE account ownership |
| Spot money capability | 0.45 | 0.60 | 0.75 |

Both extremes of the payment filter are sourced. A one-off push needs an **account, not a standing
authority**, so a WPS payroll card qualifies for spot and does not qualify for SIP. Reinforced by a dated
event: **Botim launched virtual IBAN wallets on 2026-06-22** under CBUAE's Universal Accounts Framework —
no minimum salary, no minimum balance, no fee — to a base that is 96% blue and grey collar.

✅ **Independent validation.** v2.6 claims widening the gate "roughly doubles the base". These filters
were set on their own logic and then checked: they give **1.87×**.

**Spot penetration ceiling is derived, not typed:** `SIP ceiling × uplift`. Botim's observed 6% is a
**conversion-at-exposure rate, not a penetration ceiling**, and its 8.5m → 775k step is a 9.1% in-app
discovery rate off a shelf Aurumix does not have. The 6% therefore informs the uplift's *direction* and is
never multiplied in.

🔴 **Spot-to-SIP conversion has no source anywhere** — re-confirmed by search on 2026-08-20, which makes it
a **confirmed negative** rather than a gap in the searching. No digital-gold platform publishes one-off to
recurring conversion. Carried at 3 / 8 / 15%. The mechanism design calls this arrow *"the growth funnel"*
and names spot *"the entry point for new investors"*. **It is the strategy question in numerical form and
the one an experiment could actually answer.**

---

## 9. Validation

`verify_model.py` runs 34 checks against a LibreOffice recalculation. Non-negotiable ones:

| Check | Requirement |
|---|---|
| **Conservation** | paying + holders = cumulative-ever-acquired, every period |
| **Seasonality** | both vectors sum to **exactly** 12.000 |
| **Churn** | `(1 − monthly)^12` reproduces the stated persistency |
| **Eligibility bites** | qualified is strictly below the whole book |
| **Activation** | streams 2 and 4 zero before M18; streams 5 and 6 zero at M24, first non-zero at Y3 |
| **Premium incidence** | stream 1 earns the *full* fee AND grams are short by exactly `(1+premium)` — a matched pair, so the premium cannot be charged twice |
| **ATM** | the mean draw sits below the allowance, yet the distribution still earns |
| **Stream 0** | never positive |
| **Totals** | total equals the sum of its streams; Summary ties to Model |
| **Ceiling** | cumulative-ever never breaches the market ceiling |
| **No errors** | zero `#VALUE!` / `#REF!` / `#DIV/0!` across the workbook |

⚠ **Two build traps found during this work, recorded so they are not repeated.**

1. 🔴 **The v2.6 convolution formula is wrong as written.** It specifies the curve reversal as a
   right-to-left range. **Excel and LibreOffice both normalise such a range**, so it evaluates
   left-to-right and silently produces the forward pairing the brief itself warns against. Moot now the
   convolution is gone, but it would have shipped.
2. ⚠ **`recalc.py` (the xlsx skill's recalculation helper) is broken on Windows.** It writes its
   LibreOffice macro to the Linux profile path, so the recalculation never runs; it then reads the
   untouched file, finds no cached values, and reports `total_errors: 0`. **That success is an artefact of
   the failure.** `tools/recalc_lo.py` replaces it and refuses to report success if the value cache is
   empty.

---

## 10. Open questions

| Question | Impact | Default | Priority |
|---|---|---|---|
| 🔴 **Does a lapsed customer keep the card?** | Whether the majority of revenue decays with churn or is immune to it. ~42% swing | ON | **CRITICAL — nobody has decided** |
| 🔴 **Prepaid or credit?** | *"Not a product choice, it is the business model"* | Credit | **CRITICAL** |
| 🔴 **Programme manager share of interchange** | Sizes the largest card stream. **Floor is 36% — the walk-away** | 72% | **CRITICAL** |
| 🆕 **Does the PM share apply to gross interchange, or is the effective share lower?** | The model applies it to gross, so Aurumix keeps 28%. v2.6 reports an *effective* share below the contracted one, which would leave Aurumix ~40%. **Under the current treatment stream 4 exceeds stream 2, which inverts v2.6's ordering** | Applied to gross | **HIGH — settle before the client sees a stream ranking** |
| **The two-way spread on buyback** | Prices every exit, and stream 0 has no offsetting revenue | Not modelled separately | **CRITICAL** |
| **Spot-to-SIP conversion** | The growth funnel, in numbers | 8%/yr | **HIGH — unsourceable, experiment-answerable** |
| **Launch date** | Shifts every date | M1 = Jan 2027 | **HIGH — no launch date exists in any client document** |
| **Family plan attach rate** | Scales stream 3 linearly | 20% | **MEDIUM — nothing stated anywhere in the corpus** |
| ⚠ **R4 ceiling basis** | v2.6 applies R4's ceiling to the **raw** population while R1 uses the **funnel-filtered** base | Carried as stated | **MEDIUM — flagged, not silently reconciled** |
| ⚠ **R2/R3 reachable ceilings** | Allocated to hit the stated 165,750 invariant, pending the regional population table | 35,000 / 26,352 | **MEDIUM** |

---

## 11. What this model cannot do

Stated rather than discovered.

1. **No profit, margin or break-even line.** Operating costs are not in it. Any profitability statement
   requires the cost build.
2. **No cohort resolution.** Every customer acquired in a period is identical. Questions of the form
   *"what happens to the January cohort specifically"* are simulation questions.
3. **No behavioural heterogeneity.** One churn rate. The spread that produced it is in the simulation.
4. **No per-channel unit economics.** LTV:CAC by channel × region needs cost allocation.
5. **Gold price is held flat by design.** Every revenue change is therefore attributable to the business,
   not the metal. Price is a sensitivity axis, not a scenario variable.
6. **Tier mix is not computed.** The model runs on a flat Gold rate throughout, which v2.6 measures as
   worth ~2% of gross profit at Y7 because Sovereign is 1.2% of tiered accounts.
