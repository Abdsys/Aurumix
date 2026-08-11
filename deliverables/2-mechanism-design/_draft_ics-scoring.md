# ICS Scoring: The Formula (B4)

> **Phase 2 decision draft — 2026-08-11 (revised same day: revival deleted, Masterclass removed, both Abdur's calls).** This is B4: the scoring step. It finalises the formula proposed in `_draft_sip-rulebook.md` §11, **deletes the revival mechanism** (was 🔴 open), sets the tier thresholds, and supplies every number on the closed handoff list in `_draft_ics-benefits.md` §7. Where this file conflicts with the rulebook's §11 proposals, this file wins; the corrections owed are listed in §12.

---

## 0. What B4 is pricing

The machine is already built. The rulebook fixed *how the score behaves* (periods, grace, step-down, Retention, anti-gaming); the benefits draft fixed *what a tier buys* (five levers, each mechanically defined with tier as an abstract input). B4's job is the numbers: the formula's final calibration, the thresholds that cut it into tiers, and the value of each benefit at each tier. Nothing structural is reopened here except where a proposed default failed a test.

**Grounding note.** The category offers no comp — decision 44 established that no gold token runs behaviour-based benefits at all. So calibration is grounded in the adjacent categories that have run tier systems for decades: airline/hotel status programmes, Indian life insurance persistency, and bank relationship tiers. The comps are in §10 and they are used to *defend* the numbers, not to derive them.

---

## 1. The formula, final

```
ICS = ( Tenure + Continuity + Supplementaries ) × R_applied

R_applied = min( 1 , R / 0.80 )
R         = gram-months actually held ÷ gram-months if never sold
```

| Component | Accrual | Cap | Share of max |
|---|---|---|---|
| **Tenure** | 1 point per counted period | **60** | 62% |
| **Continuity** | 1 point per consecutive counted period; **halves (rounded down) at grace expiry** | **24** | 25% |
| **Supplementaries** | Referrals + Family (§5) | **13** (8 + 5) | 13% |
| **Maximum base** | | **97** | |
| **Retention** | Two running counters, one division (rulebook §5.2). Starts at 1.00 | multiplier ∈ [0, 1] | scales everything |

**Ratified unchanged from rulebook §11:** the Tenure and Continuity caps (60/24), the halving step-down, the 0.80 holding allowance, one counted period per calendar month, monthly recalculation at period close, the tier of record as the only tier any benefit reads (benefits draft §0.3 — confirmed as the recalculation this formula assumes).

**Revised here, with reasons:** the tier thresholds (§2), **revival deleted outright** (§4 — was 🔴 open), **Masterclass removed from scoring** (Abdur, 2026-08-11 — supplementaries re-cut from 8/5/2 to 8/5), and the surviving supplementary mechanics made precise (§5). One new rule is added: the Silver floor (§2.3).

### 1.1 Why the shape is right, in one paragraph

Tenure is the **lifetime layer** and Continuity is the **current-form layer**. The loyalty industry runs exactly this two-layer structure — lifetime status (Million Miler) alongside annually-requalified status (Medallion) — but runs them as two separate statuses; we combine them additively into one number because one ladder is legible and two are not. Tenure at 62% of the maximum means the score is mostly *history*, which cannot be rushed, faked, or bought. Continuity at 25% means *current form* matters for about one tier's width — a lapse costs standing but never identity. Supplementaries at 13% are enough to matter and never enough to substitute for saving: the top tier can never go to the best recruiter. And the whole sum is scaled by Retention, so every point earned by paying is discounted by the fraction of the resulting gold actually kept. **Paying builds the score; holding keeps it.**

---

## 2. Tier structure: seven tiers, re-cut to an annual cadence

### 2.1 The seven-tier count survives challenge

B4 was free to recommend collapsing the client's seven named tiers. Tested and **kept at seven**, for three reasons:

1. **The progression cadence is the retention mechanism.** Under the thresholds below, a perfect saver advances **exactly one tier per year** for five years. Seven tiers over a five-year climb produce an annual promotion event — the same anniversary psychology the client's own reference products (LIC premium schedules) are built on. Five tiers would make promotions rarer, which is backwards for a product whose whole design is monthly discipline rewarded visibly.
2. **The five levers fill seven rungs.** The apparent resolution problem (card has only 3–4 plastic levels) was already solved by the benefits draft's plastic/parameter split (§3.1 there): plastic plateaus, monthly parameters differentiate every tier. The §7.6 check below confirms **every tier boundary moves at least two levers**, so no rung is dead.
3. **The names are the client's.** Green → Silver → Gold → Platinum → Titanium → Elite → Sovereign, unchanged. The only client-table fact worth preserving — Gold Member at 50% LTV — is preserved exactly in the partner-bound LTV version (§7.2).

### 2.2 Thresholds, defined as lower bounds

| Tier | Name | Lower bound | Perfect saver arrives | The story the customer hears |
|---|---|---|---|---|
| T1 | Green | 0 | day one | You have started |
| T2 | Silver | **12** | month 6 | Confirmed SIP — you are established |
| T3 | Gold | **24** | month 12 | One year of discipline |
| T4 | Platinum | **48** | month 24 | Two years |
| T5 | Titanium | **60** | month 36 | Three years |
| T6 | Elite | **72** | month 48 | Four years |
| T7 | Sovereign | **84** | month 60 | Five years. The top, on USD 20 a month |

> ⚠ **Build note, inherited from rulebook §11 and still binding: lower bounds, never ranges.** ICS is a real number because it is multiplied by R_applied. A band written "72 to 83" leaves 83.4 in no tier.

**Why this replaces the §11 proposal (0/10/20/35/50/65/80).** The old set was tested only against "does the USD 20 saver reach the top" and it passed, but its arrival months were arbitrary: 5, 10, 18, 26, 41, 56. The new set is chosen so that the perfect trajectory `score(m) = 2m` (m ≤ 24) then `m + 24` lands each threshold on an anniversary: **6, 12, 24, 36, 48, 60**. Three things fall out:

- **T2 = 12 aligns Silver exactly with Confirmed SIP** (6 consecutive periods → 6 + 6 = 12). Under the old set, T2 arrived at month 5, one month *before* Confirmed SIP, an off-by-one that would have needed explaining forever.
- **"One tier per year" is a sentence.** The entire ladder is communicable in one line: *Silver at six months, Gold at one year, then one tier each year to Sovereign at five.* The old set had no sentence.
- **Sovereign moves from month 56 to month 60.** This is the cost, and it is accepted: the benefits draft's USD 20 test asked that the top tier be reachable on contributions alone, and it is — at exactly five years, which reads as designed rather than as arithmetic residue. Engaged savers arrive earlier: supplementaries can bring T7 forward to ~month 47 (60 − 13). **Engagement accelerates the climb; capital never does.**

### 2.3 The Silver floor: Confirmed SIP permanently secures T2

> **New rule. An account that has reached Confirmed SIP status never has a tier of record below T2 Silver.**

Confirmed SIP is already permanent (rulebook §4.1). Without this rule, a Confirmed account whose continuity later decays could arithmetically fall below 12 and present as Green, while its Confirmed status — which is permanent — says the opposite. One status would say "established", the other "beginner". The floor makes the two consistent and gives Confirmed SIP a durable, visible meaning in the tier ladder itself.

**Gaming check.** The floor hands a lapsed or cycling Confirmed account T2 instead of T1. What T2 buys: a 0.25pp entry-fee discount (structurally unexploitable — a price reduction bounded by money handed over, rulebook §9.2 item 15) and a 5% will-plan discount (a discount on a fee paid to Aurumix). No credit, no card, no Gold Rewards below T3. The floor gives away nothing that can be farmed.

---

## 3. The price of a miss, at every age

The step-down (continuity halves, rounded down) is ratified. What B4 adds is the full price list, because "roughly one tier" (rulebook §7.2) is now checkable against real thresholds:

| When the miss happens | Score before → after | Tier before → after | Time to recover the tier |
|---|---|---|---|
| Month 13 (year one) | 24 → 18 | Gold → Silver | ~3 months |
| Month 31 (year 2½) | 54 → 42 | Platinum → Gold | ~3 months |
| Month 61 (veteran, tenure capped) | 84 → 72 | **Sovereign → Elite, exactly** | **12 months** |

Three properties, all deliberate:

1. **One miss costs about one tier at every age.** The veteran lands exactly on Elite's lower bound (84 − 12 = 72): the arithmetic delivers precisely the promise made in words.
2. **Recovery is slower at the top.** Early misses recover in ~3 months because tenure and continuity both rebuild (+2/month); a veteran's tenure is capped at 60, so rebuild runs at +1/month and takes 12. A full year one tier down is the airline norm for a missed requalification (§10), and the veteran waits it out in Elite — still carrying ~85% of every benefit — not at the bottom. This is the "loss is faster than rebuild" behaviour the client's own §8.2 specifies, priced.
3. **Supplementaries are miss insurance at the top.** A veteran with 12+ of the 13 supplementary points scores 96–97; a halving costs 12 and leaves them at 84–85 — **still Sovereign**. Only the most engaged accounts (near-max referrals *and* a full family board) can absorb a miss without a tier fall, which is exactly who should be able to. This falls out of the arithmetic unprompted and is worth telling the client: the referral network they want built doubles as the safety margin for their best customers.

**No hysteresis on tier falls — considered and rejected.** Bank tiers soften downgrades (Citi re-tiers only after three consecutive shortfall months; BofA gives an anniversary-plus-grace). We do not copy this, because banks need it and we do not: their benefits reprice the moment the tier moves, so tier flicker is customer-visible noise. Ours never reprice retroactively — LTV is struck at draw and runs to term, plastic never downgrades, discounts strike per event, Gold Rewards computes at period close (benefits draft §0.2/§0.3). **The damping already lives in the benefit layer; a second layer in the score would mute the one signal the step-down exists to send.** The miss must cost the tier *now*, because that immediate, bounded, non-financial consequence is the entire replacement for the deleted lock-in.

---

## 4. Revival is deleted (was 🔴, resolved by removal — Abdur, 2026-08-11)

> **Rule. A missed period is permanently missed.** There is no arrears mechanism, no restoration window, and nothing to pay back. Grace — 5 days, weekend-rolling — is the only tolerance in the design. After grace expires, the period never counted and never will; the continuity halving stands; the account simply continues, and next month's request is next month's request. A customer who wants to put money in after a miss makes a **spot purchase** — allocated normally, no period, exactly as spot has always worked.

**Why deletion is the coherent answer, not just the simple one.** Revival is an *insurance* concept solving an *insurance* problem: a lapsed policy is in breach of a contractual premium obligation, the cover has died, and revival (arrears + interest + underwriting) is the machinery for resurrecting it. **Aurumix deleted the contractual obligation with the lock-in (§6.19 decision).** A miss here breaches nothing and suspends nothing — the gold stays owned, the account stays live, Confirmed SIP stays permanent, and the only consequence is the step-down. Where nothing dies, there is nothing to revive. Importing revival machinery would have been importing the solution to a problem this product designed out.

**What deletion removes from the build and the terms, all at once:**
- The 12-month arrears window and its tracking.
- The arrears-as-one-payment rule (rulebook §7.2) — moot.
- The fix-on-clearing pricing rule and the look-back exploit it guarded against (rulebook §9.1 item 9) — moot: with no restoration there is nothing to time.
- The full-restoration exploit the rulebook flagged 🔴 (eleven months paid as a lump producing a perfect record — the prepayment exploit backwards) — **removed by construction rather than by rule.** No payment made after grace can ever touch the record.
- Every boundary case revival dragged in: whether a revived period counts toward Confirmed SIP's six consecutive, whether it counts for the referrer's points, partial-revival states. All moot.

**The trade accepted.** A saver who misses month 13 and "makes it up" with a spot purchase in month 14 ends with one fewer tenure point than a saver who never missed — permanently, since the month cannot be re-earned. That is the design speaking plainly: **tenure counts months in which the discipline happened, and money arriving later is a different, also-welcome behaviour with its own name (spot).** The score's two ideas stay clean: periods measure paying on schedule, Retention measures keeping. Nothing measures paying eventually.

**The day-20 payer.** With no revival, a payment clearing after grace is simply refused as a SIP contribution (the request has expired) and the customer is offered the spot path in the same screen. The halving stands. Grace already absorbs "busy or away" (5 days, nudges on days 1/3/5, never expiring on a weekend); a tolerance behind a tolerance is no tolerance.

---

## 5. Supplementaries, made precise

The rulebook proposed caps of 8/5/2 (referrals/family/Masterclass, total 15). **Masterclass is removed from scoring entirely (Abdur, 2026-08-11)**, so supplementaries are **referrals 8 + family 5, total 13**, and the maximum base is 97. Removing it also removes a component that was attendance-verified rather than money-verified — the one supplementary input that couldn't be measured off the payment rails. ⚠ **Client-facing change:** the client's §8.2 lists Masterclass participation as an ICS component; the Masterclass itself survives as a programme, it just no longer scores. Goes on the client conversation list (§12). B4 supplies the accrual mechanics for the two survivors:

### 5.1 Referrals — cap 8

```
referral points = min( 8 , Σ over referees of min( 2 , (referee's counted periods × referee's R_applied) / 6 ) )
```

- **1 point per 6 R-weighted referee-periods, capped at 2 points per referee.** One genuine referee at full Retention earns you 2 points after 12 months; maxing the component takes **four sustained, real referees** — breadth, quality and durability all required, and none substitutable for the others.
- The per-referee cap is the piece §9.4 did not have: without it, one loyal referee maxes the component in 8 months and the ninth-month referral is worthless. With it, the component rewards building a small network of real savers, which is the behaviour the agent model wants.
- Recalculated monthly, since each referee's R moves (rulebook §9.4, unchanged).

### 5.2 Family — cap 5

```
family points = min( 5 , count of sub-accounts with ≥ 6 counted periods in the trailing 12 months )
```

- **1 point per genuinely active sub-account.** The trailing-12 majority test makes the point stable month to month (no flicker from a single missed sub-account payment) and self-policing: a dormant sub-account stops scoring within months, with no review needed.
- Open to every tier (the §9.5 circularity fix, unchanged), no double-count: the sub-account's payment earns its own full score, and this one capped point for the head.

**All supplementaries sit inside the × R_applied scaling.** A recruiter who liquidates their own gold watches their referral points scale down with everything else. The score prices the whole relationship or none of it.

---

## 6. The benefit matrix

The master table. Values below T3 are dashes where the benefit's own preconditions (credit facility, card) do not yet exist. Every ladder is stepped, monotone non-decreasing, and read from the tier of record (benefits draft §0.2/§0.3).

| | T1 Green | T2 Silver | T3 Gold | T4 Platinum | T5 Titanium | T6 Elite | T7 Sovereign |
|---|---|---|---|---|---|---|---|
| **1. Entry-fee discount** | 0 | 0.25pp | 0.50pp | 0.75pp | 1.00pp | 1.25pp | **1.50pp** |
| **2. Credit LTV** (partner max 90%) | — | — | 60% | 67.5% | 75% | 82.5% | **90%** |
| **2. Credit LTV** (partner max 80%) | — | — | 50% | 57.5% | 65% | 72.5% | **80%** |
| **3. Card plastic** (4-level) | — | — | L1 | L1 | L2 | L3 | **L4** |
| **3. Card FX margin** | — | — | 2.0% | 1.75% | 1.5% | 1.25% | **1.0%** |
| **3. Card ATM allowance (AED/mo)** | — | — | 1,000 | 1,500 | 2,500 | 3,500 | **5,000** |
| **4. Gold Rewards rate** | — | — | 0.10% | 0.25% | 0.40% | 0.55% | **0.75%** |
| **5. Will plan-fee discount** | 0 | 5% | 10% | 20% | 30% | 40% | **50%** |
| **5. Per-beneficiary discount** | 0 | 0 | 0 | 5% | 10% | 15% | **20%** |

### 6.1 Entry-fee discount (benefit 1)

Quarter-point steps from 0 to a **1.5pp ceiling** — the conservative end of the 1.5–2.0pp placeholder, chosen so the required base-rate uplift (the outstanding client funding question, rulebook §13) is as small as possible. **If the client funds a 2.0pp ceiling**, stretch the top three rungs only: T5 1.25, T6 1.60, T7 2.00 — the lower rungs stay put so the early-tier experience is not funded by a bigger uplift on day-one customers. First benefit-bearing tier: **T2** (0.25pp — de minimis, unexploitable, and gives Silver a visible price meaning on arrival at month 6). Cumulative-savings display rule (benefits draft §1.2a) unchanged.

### 6.2 Credit LTV ladder (benefit 2)

**The general rule, robust to any partner outcome:** anchor T7 at `min(partner max, 90%)`, step down **7.5pp per tier** to T3, floor 50%. Unlock at **T3 Gold** — honouring the one row of the client's own credit table worth preserving, and note the partner-max-80% version reproduces the client's "Gold Member: 50%" **exactly** while fixing the arithmetic their Sovereign row got wrong (their "up to 110%" example computed to 85%).

- Partner lands at 90–95% (client's hope): ladder reads 60 / 67.5 / 75 / 82.5 / 90. Still differentiates: 30pp of spread across five rungs.
- Partner lands at 75–85% (the likely case per benefits draft §2.3, RBI comps 75–85, tokenised-gold lenders 50–80): at 80%, ladder reads 50 / 57.5 / 65 / 72.5 / 80. **Same 30pp spread, same five rungs — the ladder survives the likely outcome without redesign.** That was the §7 requirement and the top-anchored construction satisfies it for any partner max ≥ 65%.
- External inputs unchanged: the partner max itself, and warning/liquidation spacing above each step (partner's book, not ours). 90-day seasoning, LTV struck at draw, tier fall never margin-calls — all inherited (benefits draft §2), none reopened.

### 6.3 Card tier (benefit 3)

**Four-level mapping** (sponsor decides 3 vs 4; both prepared): L1 at T3–T4, L2 at T5, L3 at T6, L4 at T7. **Three-level fallback:** L1 at T3–T4, L2 at T5–T6, L3 at T7. Plastic is sticky (never downgrades, benefits draft §3.1); **the plastic upgrade rule is set at 3 consecutive months** at the qualifying tier before reissue — the short end of the 3–6 placeholder, because the tier of record is already monthly-damped and slow-to-rise, so a second long wait double-dampens; 3 months filters flicker while keeping the upgrade felt as earned promptly. FX margin runs 2.0% → 1.0% (top held at 1.0 rather than 0.75 until the sponsor's floor economics are known); ATM allowance 1,000 → 5,000 AED/month. Waiver sets per level: sponsor input. Monthly parameters flex with the tier of record at each statement cycle; plastic does not (§3.1 split, unchanged).

### 6.4 Gold Rewards rate (benefit 4)

0.10% → **0.75%** of qualifying spend by tier, starting at T3 with the card. **Monthly qualifying-spend cap: USD 3,000** — mid-placeholder, above the Kinesis comp (2% capped at USD 2,000 spend) on the cap and far below it on the rate, which is the right side to err on for a rate that must survive the customer-generated funding cap (interchange + credit revenue, net of that customer's custody cost — benefits draft §4, unchanged). External inputs unchanged: contracted interchange share (hard ceiling on the whole column) and the vault quote (custody netting line).

### 6.5 Will and family discount (benefit 5)

Plan-fee discount 5% → **50%** (the top of the 40–50 placeholder — this is the cheapest column to be generous in, it prices a service Aurumix sells, and the will is the emotional centre of the product for the persona). Per-beneficiary discount 0 → **20%**, starting only at T4 so the cheaper lever (plan fee) does the early-tier work. Ceiling below 100% preserved by construction (benefits draft §5.4: never free, or the §9.5 tier-gate returns in mirror image). External inputs unchanged: stream 3 base prices and the will partner's per-name cost floor.

### 6.6 Every rung buys something — the dead-rung check

| Boundary | What changes |
|---|---|
| T1→T2 | First price benefit (0.25pp), first will discount, Silver floor secured |
| T2→T3 | **The big rung:** credit unlocks, card issues, Gold Rewards begins, discount 0.50pp, will 10% |
| T3→T4 | LTV +7.5pp, discount 0.75pp, GR 0.25%, will 20%, per-beneficiary begins, card params step |
| T4→T5 | LTV +7.5pp, plastic → L2, GR 0.40%, discount 1.00pp, will 30%, ATM 2,500 |
| T5→T6 | LTV +7.5pp, plastic → L3, GR 0.55%, discount 1.25pp, will 40% |
| T6→T7 | LTV top, plastic → L4, GR 0.75%, discount 1.50pp, will 50%, ATM 5,000 |

No dead rungs. T2→T3 is deliberately the largest single step — it is the one that requires Confirmed SIP plus a year of form, and it is where the product's three headline features (credit, card, rewards) all switch on. **The marketing sentence is: everything unlocks at Gold, and everything gets better every year after.**

---

## 7. Fairness verification

### 7.1 The six personas, re-run at month 60 under final numbers

| Persona | Tenure | Cont. | Supps | R_applied | ICS | Tier |
|---|---|---|---|---|---|---|
| **A.** USD 20/mo, perfect, never sells | 60 | 24 | 0 | 1.00 | 84 | **T7 Sovereign** |
| **B.** As A + 2 sustained referrals + 1 active family sub-account | 60 | 24 | 5 | 1.00 | 89 | **T7 Sovereign** (miss-buffered in part) |
| **C.** USD 2,000/mo, perfect, never sells | 60 | 24 | 0 | 1.00 | 84 | **T7 Sovereign — same day as A** |
| **D.** Cycler: contributes and redeems every month | 60 | 24 | 0 | 0.004 | 0.35 | T1 → **T2 by Silver floor** |
| **E.** Withdrew half at month 36, kept saving | 60 | 24 | 0 | 0.943 | 79.2 | **T6 Elite** |
| **F.** Withdrew everything at month 36, kept saving | 60 | 24 | 0 | 0.635 | 53.3 | **T4 Platinum** |

- **A = C, to the day.** The founding principle as arithmetic: a hundred times the money buys zero tiers. This remains the single most useful row when a regulator asks whether benefits scale with capital.
- **D sits five tiers below an identical payment record**, held there by one number that cannot be faked, and the floor hands him nothing farmable (§2.3).
- **E: a legitimate 50% withdrawal at year three costs exactly one tier.** Unchanged from the rulebook's test, and the smooth-degradation promise holds.
- **F: full liquidation costs three tiers** (was two under the old thresholds). Accepted: liquidating *everything* is the strongest anti-signal the product can receive, F still keeps every benefit already delivered, every gram since repurchased, Confirmed SIP, and a climbing score. The gap between "sold half" (one tier) and "sold all" (three) now reads as proportionate rather than flat.

### 7.2 The four handoff tests (benefits draft §7)

| Test | Result |
|---|---|
| **USD 20 test** | ✅ The USD 20 saver who never misses reaches T7 and the ceiling value of all five benefits at month 60, on contributions alone. (The rulebook's month-56 figure updates to 60 with the threshold re-cut — the substance of the test, top-tier-without-referrals-or-capital, passes.) |
| **Cycler test** | ✅ D holds T2 on the floor; first benefit-bearing tier for credit, card and Gold Rewards is T3, which D never reaches. The two T2 benefits are price reductions bounded by money handed over. |
| **Withdrawal test** | ✅ E and F lose tiers only. No retroactive repricing (levers strike at event), no margin call (LTV runs to term), no clawback of credited grams. |
| **Funding test** | ✅ At placeholders: benefit 1's 1.5pp ceiling ≤ the entry-fee uplift under discussion (and only benefit 1 touches stream 1); benefit 2 is partner-book; benefits 3–4 are bounded by the customer-generated interchange/credit cap by construction; benefit 5 discounts a stream-3 fee floored at partner cost. |

### 7.3 The fairness invariants, stated once

1. **No amount, anywhere.** No component reads dollars or grams held — referees contribute *periods*, family contributes *active accounts*, Retention is a *proportion*. Capital cannot buy a tier at any rung.
2. **A new saver is never behind.** R starts at 1.00; T1 is day one; the climb is the same for everyone.
3. **A miss costs standing, never property.** Gold, tenure, Retention and Confirmed SIP are untouched by any miss (rulebook §7); the halving is the *whole* price.
4. **Refused money never scores against you.** The regulatory block freezes the clock (rulebook §8) — inherited unchanged.
5. **Nothing already delivered is ever taken back.** Struck prices, drawn LTVs, issued plastic, credited grams — all survive any tier fall.
6. **Decay is faster than rebuild, everywhere, and by arithmetic rather than by rule** — the halving vs +1/month, and R's lost gram-months gone from the numerator forever.
7. **The score attaches to the person, not the account.** Cancel-and-reopen buys nothing (rulebook §9.1 item 7); a returner resumes.

---

## 8. Anti-gaming under final numbers — nothing new opened

The rulebook's three-layer register (§9) is unchanged by any number set here; the checks below confirm the new elements add no surface:

- **The Silver floor** hands a farmer at most 0.25pp off a fee they must pay and a discount on a service they must buy. Nothing payable, nothing borrowable. Closed.
- **The threshold re-cut** moves no exploit boundary: the cycler's problem is R (two orders of magnitude), not thresholds.
- **Revival's deletion** removes the prepayment-backwards exploit *by construction* (§4) — no payment made after grace can touch the record, so the whole attack class (and the look-back timing exploit, rulebook §9.1 item 9) ceases to exist rather than being defended against.
- **The per-referee cap (2)** tightens §9.4 further: farming one coached referee now maxes out at 2 of 97 points.
- **The plastic 3-month rule** means a tier touched for one statement cycle cannot extract a card reissue.

---

## 9. Comps grounding (external research, 2026-08-11)

Run via recency-swept web research; secondary-source confidence unless noted. Used to defend calibration choices, not to derive them.

| Our choice | Category precedent | Read |
|---|---|---|
| One miss ≈ one tier, recover in ≤ 12 months | Airline "soft landing": drop one level on failed requalification, on an annual cadence (Air Canada documents the mechanism explicitly; annual evaluation is the industry norm) | Our veteran case (one tier for 12 months) sits exactly on the category norm; our early cases are *gentler* than the norm |
| Tenure + Continuity as one score | Airlines run lifetime status (Million Miler) *alongside* annual status as two systems | Same two layers; we combine additively for one legible ladder — a simplification, not an invention |
| No revival at all | IRDAI *mandates* a 3-year revival window — because an insurance lapse breaches a premium obligation and the cover dies without revival | The comp explains why we *don't* need it: Aurumix deleted the contractual obligation with the lock-in, so a miss kills nothing and there is nothing to revive. Revival machinery is an insurance solution to a problem this product designed out |
| Time-weighted R vs window-dressing | Bank tiers use daily/monthly *averaging* (Citi CAMB, DBS daily-average) precisely so a one-day balance spike buys nothing | Averaging-over-time is the standard institutional answer to snapshot gaming; R is the same idea run over the account's life |
| No hysteresis in the score | Banks damp downgrades (Citi: 3 consecutive shortfall months; BofA: anniversary + grace) | They damp at the tier because their benefits reprice instantly; ours damp at the benefit (strike-at-event, run-to-term), so damping the score too would double-count |
| Behaviour, never amount | The industry has moved the *opposite* way (Delta MQD, AA Loyalty Points are pure spend) | Deliberate inversion, and the differentiation claim: in a category (gold tokens) with zero behaviour-based benefits and an adjacent industry pricing status by spend, a scale-free score is unique on both axes |
| Sticky plastic | No bank comp upgrades the physical card with relationship tier at all | Our plastic ladder is *more* generous than banking practice — a sponsor conversation point, not a compliance one |

---

## 10. Open dials and external inputs

**Dials (ours, revisit on field data):**
- Holding allowance **0.80** (rulebook §11 — ratified; the cycler sits two orders of magnitude below it either way).
- Step-down **halving** (ratified; the gentler alternative, −25%, would let a veteran miss twice a year and hold Sovereign — too soft to replace a lock-in).
- Qualifying-spend cap **USD 3,000/month**; plastic rule **3 months**; per-referee cap **2**.

**Client questions (adds to the existing list):**
1. The entry-fee base-rate uplift that funds benefit 1's ceiling — already asked (rulebook §13); the ladder above is sized to the answer.
2. Whether the raw score (0–97) is customer-visible or tier-only. **Recommendation: show the number.** The persona knows CIBIL; a visible score with visible progress is the cheapest retention surface in the product, and hiding it hides the product's fairness.

**Client-facing changes to communicate (departures from their §8.2, both Abdur's calls):** Masterclass no longer scores ICS (the programme survives; it just isn't a score input), and there is no revival/arrears mechanism (a missed month is missed; late money is a spot purchase).

**External inputs (unchanged, not B4's to close):** partner max LTV and warning/liquidation spacing; sponsor level count, floor economics and waiver sets; contracted interchange share; vault quote; stream 3 base prices and per-name cost.

---

## 11. What exists on day one (launch sequencing, restated against tiers)

Inherited from benefits draft §6, now with numbers: at launch the tier buys the **entry-fee discount** and **will discount** columns only; the LTV column activates with the lending partner, the card and Gold Rewards columns with the sponsor bank. The tier is communicated as the durable thing; the matrix is what it currently buys. Nothing here changes that sequencing.

---

## 12. What this file changes elsewhere

- [ ] `_draft_sip-rulebook.md` §7.1: **delete the arrears row entirely** ("Arrears cleared inside 12 months" — the mechanism no longer exists) and add the spot-path line: money after grace is offered as a spot purchase.
- [ ] `_draft_sip-rulebook.md` §7.2: delete "Arrears are one payment, not instalments", delete "Arrears buy gold at the fix on the day they clear", and correct "The step-down applies at grace expiry **and reverses on revival**" → the step-down applies at grace expiry and **stands**; grace is the only tolerance.
- [ ] `_draft_sip-rulebook.md` §9.1 item 9 (the arrears look-back exploit): mark moot — no restoration path exists.
- [ ] `_draft_sip-rulebook.md` §11: mark the proposed parameters table and thresholds **superseded by this file** (Tenure/Continuity caps, step-down and allowance ratified; thresholds re-cut; revival row resolved by deletion; Masterclass removed, supplementaries 8/5 = 13, max 97).
- [ ] `handoff.md` decision 36 ("arrears clear as one payment, not instalments"): the arrears half is moot with revival's deletion.
- [ ] `_draft_ics-benefits.md` §7: the closed handoff list is **supplied in full** by §6 here; §7's checklist can be marked closed against this file. The §0.3 tier-of-record rule is confirmed as assumed.
- [ ] `Aurumix_Process_Maps_ICS_Benefits.md`: unaffected structurally; a companion scoring map set (the climb, the miss, the cycler) is now drawable and owed when process maps are next batched.
- [ ] `handoff.md`: decision 46.
- [ ] Client conversation: the month-56 → month-60 Sovereign arrival, the Silver floor, the visible-score recommendation, **the Masterclass removal from scoring (their §8.2 lists it as a component), and the absence of any revival/arrears mechanism** are new client-facing facts since the last session.

## 13. Sources

| Claim | Source | Confidence |
|---|---|---|
| Airline soft landing (one-tier step-down), annual requalification norm | Air Canada Aeroplan published downgrade/extension rule; industry coverage of annual status cycles (web research 2026-08-11) | Medium-High (Air Canada primary-adjacent; norm claim secondary) |
| Lifetime + annual dual status | Delta Million Miler / AA Million Miler alongside annual status | High (well-documented programme structures) |
| IRDAI revival: 3-year window, arrears + 8–10% interest, riders from revival date, contestability restart | IRDAI Master Circular (2024) as summarised in current-practice guides | Medium (⚠ pull the Master Circular primary text before client use) |
| Bank tier averaging and downgrade damping | BofA Preferred Rewards, Citi CAMB, DBS My Treasures published tier rules | Medium-High |
| Spend-based industry trend | Delta MQD / AA Loyalty Points structures | High |
| Gold-collateral LTV comps (50–85%) | Inherited from `_draft_ics-benefits.md` §2.3 — not re-verified here | As stated there |
