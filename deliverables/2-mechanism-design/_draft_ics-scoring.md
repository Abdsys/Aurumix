# ICS Scoring: The Formula (B4)

> **Phase 2 decision draft — 2026-08-11, rewritten 2026-08-12, hardened the same day against a flaw review, and amended 2026-08-13 on the gate (Abdur's calls throughout).** This is B4: the scoring step. It supersedes the 2026-08-11 version in full.
>
> **🆕 2026-08-13 amendment, and it changes the shape of the entry.** **Confirmed SIP is 6 *consecutive* counted periods, and it gates the score itself, not only the benefits** (§1.6). This reverses the 2026-08-12 redefinition and resolves the same contradiction a different and simpler way: before the door there is no score and no tier at all, so the score can never contradict the gate. **The scoring clock starts at the qualifying run**, so pre-gate payments never enter the score and **every account opens at exactly Silver, 25** (§1.6). **The first rung is renamed from Green to "No tier"**, which is now literally accurate. The 2026-08-12 sweep to *"6 contributions"* is cancelled.
>
> **Three fixes from the flaw review, all in §1:** the **gate/score contradiction** (§1.6, now resolved by the gate above); **Retention re-based** on a timing-neutral denominator and re-shaped to a straight line at a 30% allowance, which kills the 21%-costs-the-top-tier bug (§1.5); and **Sovereign's zero tolerance kept deliberately**, with the arithmetic showing the alternative does not exist (§1.8). The earlier draft kept the client's seven tiers and a weighted-sum formula; both are replaced. **Five tiers**, and a formula built on a **minimum rather than a sum**. Referrals, family and Masterclass are removed from scoring entirely. Retention survives as the multiplier it always was, re-based on an observable quantity.
>
> Where this file conflicts with `_draft_sip-rulebook.md` §11 or with the 2026-08-11 draft, **this file wins.** Corrections owed are listed in §12.

---

## 0. What B4 is pricing

The machine was already built. The rulebook fixed *how the score behaves* (periods, grace, Retention, anti-gaming); the benefits draft fixed *what a tier buys* (five levers, each mechanically defined with tier as an abstract input). B4's job is the numbers.

**What changed on the second pass, and why.** The 2026-08-11 draft passed every test it set itself and still failed the only one that matters: the person who has to defend it could not hold it in their head. Ten interacting rules — three weighted components with three caps, an escalating strike schedule, a Silver floor, a tenure floor, a per-referee referral formula, a family formula, a lifetime retention multiplier — each individually justified, collectively unexplainable. A score that cannot be explained cannot be trusted, and a loyalty score nobody trusts does no retention work.

This version does the same job with **two facts and one penalty**.

**Grounding note, unchanged.** The category offers no comp — decision 44 established that no gold token runs behaviour-based benefits at all. Calibration is grounded in adjacent categories that have run tier systems for decades: airline and hotel status, Indian life-insurance persistency, bank relationship tiers. The comps in §9 *defend* the numbers; they do not derive them.

---

## 1. The formula, final

```
ICS = min( Record , Standing ) × Retention

  floor of 25 once Confirmed SIP is earned
```

Three inputs, every one of them readable straight off the payment ledger and the token ledger. No weights, no normalisation constants, no component caps.

### 1.1 The three facts

| Fact | What it measures | Moves how |
|---|---|---|
| **Months** | Counted periods since the qualifying run began (§1.6). **What you contributed.** | Rises by 1 per counted period. **Never falls, for any reason.** Starts at 6 on the day the gate opens. |
| **Recent** | Counted periods in the trailing 12 calendar months, 0–12. **Whether you are contributing now.** | Rises and falls as the window rolls. Self-healing over 12 months. Never looks back past the start of the run. |
| **Sold** | The share of everything you had that you no longer have — see §1.5. **Whether you kept it.** | Recomputed monthly on the same clock as Recent. |

**A counted period** is unchanged from the rulebook and remains the atom of the whole design: a calendar month in which one accepted SIP contribution — at or above the USD 20 floor, cleared on time or inside the 5-day grace — was allocated. One per calendar month maximum, **amount irrelevant**, spot purchases never count, a missed month is permanently uncounted (§4).

**Each fact measures exactly one thing, and this is load-bearing.** Months is a historical fact about what the customer did; nothing that happens later can un-happen it, which is why selling does not touch it and why referrals were not allowed to inflate it. Recent is a statement about the present. Sold is a statement about the gold. The moment any of the three starts measuring two things, the customer stops being able to compute it, and the design's central trust property — *you can check your own score* — is gone.

### 1.2 Why a minimum and not a weighted sum — the load-bearing choice

The 2026-08-11 formula was `(Tenure + Continuity + Supplementaries) × R`. A weighted sum has one structural property that defeated it: **components trade off.** A large Tenure term can cover a dead Continuity term. That is not a calibration error, it is what addition *is*, and it produced the failure that reopened B4 — a ten-year saver who had not contributed in a year still scoring near the top on seniority alone. The 2026-08-11 draft patched it with a Tenure cap of 60; the patch worked, but only because the cap silently converted the sum into something else.

The honest structure is a conjunction. Each tier has two requirements and **both** must hold:

> **Gold:** 12 months paid **AND** 6 of the last 12.

And conjunction has an exact arithmetic form:

```
A ≥ x  AND  B ≥ x        ⟺        min(A, B) ≥ x
```

**Minimum is the arithmetic of AND.** Mapping each fact onto the same 0–100 scale and taking the lower of the two reproduces the two-condition test exactly, with no substitution possible in either direction. A spotless record cannot cover a bad year; a perfect year cannot cover a short record. The property is enforced by the structure of the operator, not by a rule that has to be written, defended and remembered.

Three consequences worth having:

1. **No weights exist to argue about.** The relative importance of history and current form is expressed by where the two mappings sit, not by coefficients. There is nothing to tune incoherently.
2. **The score names its own constraint.** If ICS equals Standing, discipline is the binding condition — pay. If it equals Record, the customer is doing everything right and needs time. The app can say *"Score 50 — limited by your recent payments"* with no additional logic.
3. **For a saver who never misses, Standing never binds.** Standing ≥ Record at every month of a clean climb (verified in §7.4). So the score of a good customer is purely their Record, and Standing only ever appears when something has gone wrong. That is the right way round.

### 1.3 Record — the mapping from Months

A two-segment linear function. The kink at month 12 exists because the tiers are not evenly spaced in time: two tiers arrive in the first year, two more over the following four.

```
Record(m) =  m × 4.1667                    for m ≤ 12
             50 + (m − 12) × 1.04167       for 12 < m ≤ 60
             100                            for m > 60
```

**In one sentence: your first year of payments takes you to 50; the next four years take you from 50 to 100.**

| Months | 0 | 3 | 6 | 9 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Record** | 0 | 12.5 | 25 | 37.5 | **50** | 56.3 | 62.5 | 68.8 | **75** | 81.3 | 87.5 | 93.8 | **100** |

**The cap at 60 months is the same decision the old Tenure cap made, relocated and made explicable.** It is no longer "tenure stops counting at 60 points"; it is "five years of saving is a complete record." Uncapped, Record alone would eventually clear any threshold and the score would become miss-proof by seniority — the exact failure this rewrite exists to close.

⚠ **The cap binds the score only.** The app keeps displaying the raw count — *"187 months saved"* — which rises forever and is the veteran's recognition surface. Recognition scales without limit; benefits do not.

### 1.4 Standing — the mapping from Recent

A single straight line. Each of the last twelve months is worth the same.

```
Standing = Recent × 8.3333
```

| Recent | 0 | 3 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Standing** | 0 | 25 | 41.7 | **50** | 58.3 | 66.7 | **75** | 83.3 | 91.7 | **100** |

**A trailing-12 count replaces the entire strike schedule** (see §3). The 2026-08-11 draft needed an escalating penalty table plus a paragraph explaining why strikes had to be counted in a trailing window rather than consecutively. A trailing window *is* the measurement, so the shape falls out for free and no penalty table exists.

### 1.5 Retention — the multiplier

The one component deliberately not treated as a gate, because holding is not one virtue among several: **it is a condition on all of them.** As a gate it could be satisfied and then forgotten. As a multiplier it has veto power — no amount of paying compensates for not keeping the gold.

```
             grams held now
Sold  =  1 − ─────────────────────────────────────────────────────────
             grams held 12 months ago  +  grams acquired since

Retention =  1                              for Sold ≤ 30%
             1 − (Sold − 30%) ÷ 70%         for Sold > 30%
```

| Sold in 12 months | ≤30% | 40% | 50% | 60% | 70% | 80% | 90% | 100% |
|---|---|---|---|---|---|---|---|---|
| **Retention** | 1.000 | 0.857 | 0.714 | 0.571 | 0.429 | 0.286 | 0.143 | **0** |

**Customer sentence:** *You can take out up to a third of your gold in a year and nothing happens at all. Past that, every further 7% you sell costs you 10% of your score, down to zero if you empty the account.*

#### The measure — why this denominator (revised 2026-08-12)

The earlier draft measured Sold against *average balance over the window*, and that was wrong in a way that mattered: **a sale early in the window depressed the average, so the same sale cost more if made long ago than if made yesterday.** Selling just before assessment was the cheapest time to sell — precisely the window-dressing the old gram-months formula existed to prevent.

The form above is timing-neutral by construction: it reads three numbers (opening balance, acquisitions, closing balance) and asks *what share of everything you had did you not keep?* It cannot be improved by choosing when to sell, it is scale-free, and it is auditable off the token ledger alone.

**Four rules the denominator forces, all cheap:**

| Case | Rule |
|---|---|
| Denominator is zero (no gold, none acquired) | Sold = 0, Retention = 1. A customer with nothing cannot have sold anything. |
| Grams credited by **Gold Rewards** | Count as *acquired*. They enlarge the denominator, so a reward never creates or reduces a penalty. Sold clamps at 0 either way. |
| **Transfers to a family sub-account or under the Digital Will** | **Not a sale.** The gold stays inside the product; only the name on it changes. Excluded from the numerator, and it arrives in the recipient's account as an acquisition. |
| **Lender liquidation on a margin call** | ✅ **It counts as a sale** (Abdur, 2026-08-13). The customer did not choose the day, but they chose to borrow, and the alternative makes borrowing a route around Retention: pledge, draw to the limit, let it liquidate, keep the cash, keep the score. ⚠ **Note the deliberate asymmetry with a tier fall:** a tier fall never margin-calls, but a margin call does move the score. Different directions, and both are correct. |

#### Why linear at 30%, not convex at 20%

Both shapes deliver the two things that matter — a genuine household withdrawal costs little, emptying the account costs everything. The straight line is chosen because it is the one a founder can repeat back after hearing it once, and because a **30% allowance is fully free** where a 20% allowance with a convex tail is only *nearly* free. That distinction turns out to be load-bearing:

> 🔴 **The bug it fixes.** Under the convex form, a Sovereign who sold **21%** of their gold scored 100 × 0.9998 = 99.98 and **lost the top tier** — because Record and Standing both cap at 100, a Sovereign has no buffer, so *any* Retention below 1.000 costs the tier. The design promised small withdrawals were nearly free and then denied that benefit to exactly the customers who had earned most. A hard 30% allowance removes it: below the line Retention is exactly 1.000, not 0.9998.

Tier outcomes are otherwise near-identical, and where they differ the straight line is the more sensible of the two:

| Sold | Convex @ 20% | **Linear @ 30%** | Effect on a Platinum saver |
|---|---|---|---|
| 30% | 0.984 → Gold | **1.000 → Platinum** | *nothing happens* |
| 40% | 0.938 → Gold | 0.857 → Gold | one tier, both |
| 50% | 0.859 → Gold | 0.714 → Gold | one tier, both |
| 70% | 0.609 → Silver | 0.429 → Silver | two tiers, both |
| 100% | 0 → Silver floor | 0 → Silver floor | identical |

The line is **gentler below ~32% and harsher above it** — free where withdrawal is normal, biting where it becomes liquidation. That is the right way round.

⚠ **Dials:** the 30% allowance is the one number to revisit on field data. The exponent is retired.

**Three properties this form has that the old lifetime R did not:**

1. **It stays live at any account age.** Lifetime R's denominator grows with the *square* of the account's age, so an identical sale moved the multiplier four times less at year 20 than at year 10 — the one veto in the design went inert exactly when balances were largest. A trailing window is age-invariant.
2. **It heals on the same clock as everything else.** A sale ages out of the window in 12 months, exactly as a missed payment does. One recovery rule covers both.
3. **It stops punishing a year-3 emergency in year 15.** Under lifetime R it did, forever.

**What it costs:** a one-time full liquidator recovers in 12 clean months rather than never. Accepted — the case the multiplier exists to stop is the *cycler*, who redeems continuously and therefore sits at Retention 0 permanently (§7.1 persona D). A saver who liquidated once, then rebought and held for a year, has demonstrated the behaviour the product wants.

### 1.6 Confirmed SIP is the gate, and the score sits behind it

> 🔄 **Confirmed SIP is 6 *consecutive* counted periods, and it gates the score itself, not only the benefits** (Abdur, 2026-08-13). This reverses the 2026-08-12 redefinition. It remains permanent once earned. **Rulebook §4.1 correction owed.**
>
> **Before the gate: no score, no tier. After it: the score runs, and never falls below 25.**

**Two objects, and keeping them separate is what makes the design explainable.**

| | What it is | How it moves |
|---|---|---|
| **Confirmed SIP** | A **door**. Six consecutive contributions opens it. | Opens once. **Permanent.** A later miss never closes it. |
| **ICS score** | A **dial** behind the door. Prices what each benefit is worth. | Recalculates monthly, from the moment the door opens. |

**Customer sentence:** *Six months straight to start. Then your score runs, and it decides what you get.*

**Why the score sits behind the gate rather than beside it.** The score reads only Months and Recent, and neither can see a streak. If the gate demanded consecutiveness while the score ran independently of it, the two would disagree: a saver missing every fifth month never strings six together, so the gate grants nothing, while at month 60 the score reads **Platinum (≈83)**. Two statuses, opposite answers, no rule to arbitrate. Putting the score behind the same door removes the case rather than adjudicating it: that saver has no score to contradict the gate, because the score never started. **One door, one thing behind it.**

**What the score reads on the day the door opens: the qualifying run, and nothing before it** (Abdur, 2026-08-13). The scoring history begins at the first month of the run. Payments made before it are real purchases of real gold and they are not erased in any way that matters to the customer, but they are **invisible to the score.**

So a saver who paid months 1, 2, 3, missed 4, paid 5, 6, 7, missed 8, then landed 9 through 14 straight has **Months = 6** and **Recent = 6** on opening day, not 12 and 10:

```
Months   = 6      Record   = 25
Recent   = 6      Standing = 50
ICS = min(25, 50) × 1.00 = 25   →  Silver
```

**Everybody opens at exactly Silver, always**, whether the run was months 1 to 6 or months 9 to 14. That uniformity is the point: there is one entry to the ladder and one number at it, so the promise needs no branch. *Your score starts the day you complete six months straight, and it starts at Silver.*

⚠ **The alternative was considered and rejected:** reading every payment ever made would have opened the late saver above at `Record(12) = 50`, **Gold**, skipping Silver entirely. It preserves more history, and it was rejected because it makes the entry point depend on how messy the run-up was, which is a rule nobody can state in one line. **Six real payments in the example count for nothing toward the score.** That is the accepted cost, and it is the strongest argument for the countdown display in §1.6a: a customer must be able to see the run they are building, or those payments feel taken rather than spent.

**Nothing is lost by the strictness.** Confirmed SIP was never a promise or a commitment (decision 19: *a backward-looking threshold, and stopping early forfeits nothing*). Its job is to prove the account is real and the saver is not a one-payment tourist. Six consecutive contributions proves that more strongly than six scattered ones, and it is the one place in the design where a streak is cheap to require, because it is asked **once and never again.** After the door opens, no streak is ever measured anywhere in the design: Recent counts, it does not sequence.

⚠ **The consequence to state out loud rather than let a customer discover.** A saver who never completes six in a row accrues nothing at all: no score, no tier, no benefits, however many scattered payments they make. That is defensible (*the qualifying run was never completed*) but it must appear in the terms and in the app, not only in the engine. **The countdown display in §1.6a is the mitigation.**

⚠ **Wording.** Decision 19 forbids *"6 month commitment"*; the accurate phrase is **"6 consecutive contributions."** The 2026-08-12 sweep to *"6 contributions"* is cancelled. Nothing here creates an obligation: a broken run costs the customer nothing except starting the run again, and no money is forfeited.

**Gaming check on the floor.** The floor hands a lapsed or cycling account Silver rather than nothing. Silver buys a 0.4pp entry-fee discount (structurally unexploitable — a price reduction bounded by money handed over, rulebook §9.2 item 15) and a 10% discount on a will plan the customer must buy. No credit, no card, no Gold Rewards below Gold. **Nothing farmable passes through the floor**, and the consecutive gate makes it strictly harder to reach than under either earlier draft.

### 1.6a Before the gate: what the customer sees

No score is computed, so none is shown. **Showing a number here would be actively harmful:** the persona reads scores as CIBIL, and an 8 reads as *bad credit* rather than *early progress*, in exactly the months where persistency is thinnest and the customer is barely profitable (decision 22). Show the run instead:

> **4 of 6 — three months to go**

Concrete, actionable, and it converts to the score at the moment the door opens. A broken run resets the counter to zero with an explicit message, since a silent reset is the one thing that would make the gate feel arbitrary.

⚠ **Build note:** the engine tracks the **current run length** (0–6) before the gate, not a score and not Months. Months and Recent both begin at the first month of the qualifying run (§1.6), so on opening day they are 6 and 6 by construction. Pre-run contributions are still recorded on the ledger as ordinary allocated purchases; they simply never enter the score.

### 1.7 Absolute, not relative — retained unchanged

Tiers are **absolute thresholds** (score ≥ 75 is Platinum, for everyone, always), never **relative position** (top 10% is Platinum). Four reasons, carried forward from the 2026-08-11 draft:

1. **Relative scoring makes your tier depend on other people.** Under percentiles a flawless saver can be demoted because a better cohort joined, so the product's central promise — *never miss for five years on USD 20 and you reach the top* — becomes unpromisable. Absolute thresholds are the only structure under which the promise is a contract with yourself.
2. **The benefits are prices and contract terms, so the tier must be quotable.** LTV strikes at draw and runs to term; card levels change at statement cycle; discounts strike per event. No lending partner, card sponsor or regulator accepts terms keyed to a moving population statistic.
3. **Relative is zero-sum, and zero-sum is adversarial.** Every new good saver would push an existing one down — growth punishing loyalty. It also builds a tournament, and a tournament for financial benefits is a compliance surface: **the client's 80/20 dividend was exactly this pathology**, and it is among the reasons the dividend became Gold Rewards.
4. **The one thing rank-ordering buys — rationing a fixed pool — this design does not need.** Every benefit is self-funding per customer (Gold Rewards capped at that customer's generated revenue, discounts bounded by money handed over, LTV on the partner's book).

Practical corollaries: absolute behaves identically at 500 users and 100,000, and it is deterministic — the customer can compute their own tier, which is the trust posture behind the visible-score recommendation (§10).

> ⚠ **Absolute does not mean permanent.** The bar never moves and nobody else's behaviour can push you off it, but the score recalculates monthly and falls two ways: Standing (a miss) and Retention (a sale). **Sovereign requires a score of exactly 100** — Record 100 *and* Recent 12 *and* Sold ≤ 30%, simultaneously, every month. It is the most fragile perch in the ladder by construction. **Sovereign is rented by conduct, never owned.** The only unconditional floor in the design is Silver.

### 1.8 Sovereign's zero tolerance is kept, and the reasoning is arithmetic

**It was challenged (2026-08-12) and the challenge established that the alternative does not exist.** Because `min()` takes two inputs that both cap at 100, **the Sovereign threshold must sit at the cap or Sovereign arrives before month 60.** Setting it at 95 pulls arrival to month 56 *and still tolerates nothing* (one miss gives Standing 91.7, below 95). Buying genuine one-miss tolerance requires a threshold of 91.7, which arrives at month 52 and destroys the one sentence the ladder is sold on — *Sovereign at five years.* There is no headroom to create, because neither input can exceed 100 by construction and creating headroom in Record is exactly the seniority hole the cap exists to close.

So the choice is real and binary, and **zero tolerance is the better half**:

- **The promise is the clearest in the design.** *Sovereign means a perfect year, on a complete record, with your gold intact.* No asterisk, no requalification table, nothing to explain.
- **The consequence is already damped where it costs money.** A tier fall never reprices retroactively: the loan runs to term at the LTV struck, the plastic never downgrades, delivered discounts are not clawed back. Losing Sovereign for a year costs the discount rate, the rewards rate and the card parameters — not the card and not the loan.
- **The withdrawal half of the cliff is gone** (§1.5). What remains is a miss, which is the behaviour the score exists to price.

⚠ **Alternative, considered and rejected:** define `Standing = min(12, Recent + 1) × 8.33` — "one free miss a year." It works arithmetically, leaves every arrival date untouched (Record binds throughout a clean climb), and softens the whole ladder by one miss. **Rejected because it invites the product's best savers to skip a month every year at no cost** — five skipped payments across the climb, in a product whose entire thesis is monthly discipline. Recorded here because it is the fix to reach for if field data shows the year-long Sovereign penalty driving churn.

### 1.9 Scope rules: who has a score, and what pauses the run

**All three settled 2026-08-13 (Abdur).**

**Every account passes its own gate, with no exceptions and no inheritance of status.** A family sub-account, a spouse, a child, a second account opened by the same person: each earns its own six consecutive contributions and its own score. This follows directly from rulebook §385 (a sub-account's contribution earns a full period for the sub-account's own score) and from invariant 8 (the score attaches to the person). **Nobody is carried in on someone else's record**, which is also what stops a head-of-family account being used to switch benefits on for people who have never paid.

**A pause freezes the run; it never breaks it.** Decision 36's regulatory pause was written for accounts already through the gate. **It applies identically before the gate:** a month in which Aurumix refuses the investor's money does not count against them, and pre-gate that means the qualifying run neither advances nor resets. A saver at 4-of-6 who enters a compliance pause resumes at 4-of-6. Invariant 5 — *refused money never scores against you* — has no reason to behave differently on the two sides of a door the customer cannot see. **Frozen months are skipped entirely and the window extends to reach twelve countable months** (§10 item 3, settled): a frozen month is treated as though it never existed, on both clocks.

**Partner-channel customers earn no ICS.** Customers who reach AURX through a B2B partner's own app (revenue stream 6, decision 42) hold gold and are **outside the scoring system entirely** — no gate, no score, no tier, no tier-priced benefits. Three reasons it has to be this way: **the behaviour is not observable to us** (the partner owns the payment relationship and the collection rail, so we cannot see a counted period, only a balance); **the benefits are not ours to give** on that book, since the partner sets their own pricing and keeps 70 to 80% of the spread; and **the funding cap breaks** — Gold Rewards is capped at the interchange and credit revenue that customer generated, and a partner customer generates neither. ⚠ **This makes ICS a direct-channel product feature, which is a strategic fact and not only a mechanical one.** Decision 45 recorded this as a Phase 4 contract question; it is now decided ahead of the contract, and the partner agreement must say so explicitly rather than leave it to be assumed.

---

## 2. Tier structure: five tiers

### 2.1 Why five, not seven — the count is derived from the benefits, not chosen

The 2026-08-11 draft kept the client's seven names and defended the count on cadence: one promotion per year for five years. That defence survives on its own terms and fails against the benefit set, which is the constraint that actually binds.

**The ladders' floors and ceilings are fixed by economics, not by us.** The entry-fee discount ceiling is bounded by the base-rate uplift the client authorises; LTV by the lending partner's maximum; Gold Rewards by contracted interchange; the card by the number of programme levels the sponsor operates. **Tier count does not change the size of the cake — only how it is sliced.** Seven tiers cut a fixed range into six steps, and the steps came out too small to be felt:

| Line | 7-tier step | At USD 75/mo | 5-tier step |
|---|---|---|---|
| Entry-fee discount | 0.25pp | **USD 0.19/month** | 0.4pp |
| Gold Rewards | 0.15pp | USD 1.50–4.50/month | **0.30pp** (~USD 9/mo at cap) |
| Credit LTV | 7.5pp | ~USD 190 headroom at m36 | **15pp** |
| Card plastic | 4 levels over 5 rungs | many-to-few mapping | **3 levels over 3 rungs** |

Three things improve at five and nothing degrades:

1. **The card mapping stops being many-to-few.** Sponsor banks operate three or four programme levels. At seven tiers the benefits draft needed a plastic/parameter split (§3.1 there) and both a 3-level and a 4-level fallback. At five tiers, Gold/Platinum/Sovereign map one-to-one onto three sponsor levels. The fallback disappears.
2. **Every increment roughly doubles.** Gold Rewards steps of 0.30pp are about USD 9 a month at the spend cap — the first increment in the design a customer would notice in the month it happened.
3. **Twenty fewer cells to calibrate.** Every external input still outstanding (interchange share, vault quote, sponsor floor economics) has to be pushed through the whole matrix when it lands. 🔄 Partner max LTV has since left this list: **fixed at 80% by decision, §6.2**.

**Names.** No tier → Silver → Gold → Platinum → Sovereign. Titanium and Elite are dropped, and **Green is renamed to "No tier"** (Abdur, 2026-08-13), since under §1.6 an account below the gate genuinely has no tier and no score rather than a low one. **So the ladder is four named rungs, not five.** The one client-table fact worth preserving — **Gold Member at 50% LTV** — is preserved exactly under the top-anchored LTV rule (§6.2).

⚠ **Client-facing:** the seven-name ladder is theirs, and cutting it to five is a change to communicate. The argument to make is the one above — *their* benefits cannot differentiate seven ways, and a rung that moves nothing a customer can feel devalues every rung.

### 2.2 The ladder, two ways to read it

Identical statements. The first is what goes in the terms and the app; the second is what the engine computes.

**As conditions:**

| Tier | Requirement |
|---|---|
| **No tier** | Confirmed SIP not yet earned. No score is computed (§1.6). |
| **Silver** | Confirmed SIP earned: **6 consecutive contributions.** **Permanent.** |
| **Gold** | 12 months paid · 6 of the last 12 |
| **Platinum** | 36 months paid · 9 of the last 12 |
| **Sovereign** | 60 months paid · 12 of the last 12 |

**As a score:**

| Tier | ICS |
|---|---|
| No tier | *no score* |
| **Silver** | **25** |
| **Gold** | **50** |
| **Platinum** | **75** |
| **Sovereign** | **100** |

> 🆕 **The 0–24.9 band no longer exists, and this is a real simplification.** Below the gate there is no score; above it the Silver floor makes 25 the minimum. **Every score the system ever displays is 25 or higher.** The old Green rung was a tier that named an absence, which is why it is renamed to "No tier" (Abdur, 2026-08-13): the label is now literally what the account has.

> ⚠ **Build note, still binding: lower bounds, never ranges.** ICS is a real number. A band written "75 to 99" leaves 99.4 in no tier.

### 2.3 Arrival schedule

A saver who never misses and never sells:

| Tier | Arrives | Record | Standing | ICS |
|---|---|---|---|---|
| Silver | **month 6** | 25 | 50 | **25** |
| Gold | **month 12** | 50 | 100 | **50** |
| Platinum | **month 36** | 75 | 100 | **75** |
| Sovereign | **month 60** | 100 | 100 | **100** |

**Silver lands exactly on Confirmed SIP**, so the two statuses arrive together and never need reconciling. **Gold at one year, Platinum at three, Sovereign at five.** The whole ladder is one sentence: *Silver at six months, Gold at one year, Platinum at three, Sovereign at five.*

**On the 24-month gaps.** Gold→Platinum and Platinum→Sovereign are each two years, against 6 and 6 months at the bottom. That spacing is deliberate and matches the persistency curve (decision 22: ~79% at month 13, ~38% at month 61): the reinforcement is concentrated where the churn is, and the later stretch is walked by savers already selected for stickiness — who by then hold credit, a card and Gold Rewards, all of which grow with their base every month whether or not the tier moves.

### 2.4 What happens after year five

The ladder is a five-year instrument and that is correct, not a limitation. Its job is carrying savers across the persistency cliff. What scales past year five is everything the tier *multiplies*:

| | Year 5 (~40 g) | Year 20 (~155 g) |
|---|---|---|
| LTV rate | 80% | 80% |
| **Borrowing headroom** | ~USD 3,500 | **~USD 13,500** |
| Gold Rewards rate | 0.75% | 0.75% |
| **Months saved (displayed)** | 60 | **240** |

Decision 20 already said it: **amount sizes the base, behaviour sets the rate.** A rate that stops improving at year five is that principle working. A ladder that kept promoting for twenty years would need fifteen tiers, and the benefit set cannot differentiate five.

---

## 3. The price of a miss

> 🔄 **The escalating strike schedule of the 2026-08-11 draft is deleted.** Not softened — deleted. A trailing-12 count produces the same behaviour with no penalty table, no strike counter, no state to track, and no rule to explain.

### 3.1 It falls out of Standing

A miss reduces Recent by one for twelve months, then ages out. There is nothing else. For a veteran (Record 100) who stops paying entirely:

| Consecutive misses | Recent | Standing | ICS | Tier |
|---|---|---|---|---|
| 0 | 12 | 100 | **100** | Sovereign |
| 1 | 11 | 91.7 | **91.7** | Platinum |
| 2 | 10 | 83.3 | **83.3** | Platinum |
| 3 | 9 | 75 | **75** | Platinum |
| **4** | 8 | 66.7 | **66.7** | **Gold** |
| 7 | 5 | 41.7 | **41.7** | **Silver** |
| 12 | 0 | 0 | floor **25** | Silver |

**Four consecutive misses to lose Platinum, seven to lose Gold.** A genuinely isolated lapse costs one tier at the very top and nothing at all mid-band; a sustained pattern costs a tier at a time. That is the shape the strike schedule was built by hand to produce.

### 3.2 The properties, now emergent rather than engineered

1. **The alternating gamer is closed by construction.** Pay–miss–pay–miss holds Recent at 6 permanently, so the account is capped at Gold for life. The 2026-08-11 draft needed an explicit trailing-window rule to defeat exactly this, and a paragraph to justify it.
2. **A first miss costs at most one tier, and mid-climb often costs nothing.** A month-42 saver (Record 81.3) who misses once has Standing 91.7 and stays at 81.3 — Platinum, unchanged. Only a saver sitting exactly on a threshold drops on any penalty at all, which is inherent to thresholds and accepted for Sovereign by design (§1.7).
3. **Loss is faster than rebuild.** Standing falls 8.33 on the miss and returns only as the window rolls forward twelve months later.
4. **Recovery rewards history without a floor rule.** A veteran who lapses and returns must rebuild only Recent, not Months — roughly **nine clean months** restores Platinum, against the 36 a newcomer needs. *You never re-earn your history, only your form.* The 2026-08-11 draft's proposed tenure floors are therefore unnecessary and are not adopted.

### 3.3 No hysteresis on tier falls — considered and rejected, unchanged

Bank tiers soften downgrades (Citi re-tiers only after three consecutive shortfall months; BofA gives an anniversary plus grace). We do not copy this, because banks need it and we do not: their benefits reprice the moment the tier moves, so tier flicker is customer-visible noise. **Ours never reprice retroactively** — LTV is struck at draw and runs to term, plastic never downgrades, discounts strike per event, Gold Rewards computes at period close (benefits draft §0.2/§0.3). The damping already lives in the benefit layer; a second layer in the score would mute the one signal the step-down exists to send. The miss must cost the tier *now*, because that immediate, bounded, non-financial consequence is the entire replacement for the deleted lock-in.

---

## 4. Revival is deleted — unchanged from 2026-08-11

> **Rule. A missed period is permanently missed.** There is no arrears mechanism, no restoration window, nothing to pay back. Grace — 5 days, weekend-rolling — is the only tolerance in the design. After grace expires the period never counted and never will; the account continues, and next month's request is next month's request. A customer who wants to put money in after a miss makes a **spot purchase** — allocated normally, no period, exactly as spot has always worked.

**Why deletion is the coherent answer, not just the simple one.** Revival is an *insurance* concept solving an *insurance* problem: a lapsed policy breaches a contractual premium obligation, the cover dies, and revival is the machinery for resurrecting it. **Aurumix deleted the contractual obligation with the lock-in** (§6.19 decision). A miss here breaches nothing and suspends nothing — the gold stays owned, the account stays live, Confirmed SIP stays permanent, and the only consequence is the fall in Standing. Where nothing dies, there is nothing to revive.

**What deletion removes, all at once:** the 12-month arrears window and its tracking; the arrears-as-one-payment rule (rulebook §7.2); the fix-on-clearing pricing rule and the look-back exploit it guarded against (rulebook §9.1 item 9); the full-restoration exploit the rulebook flagged 🔴 — **removed by construction rather than by rule**, since no payment made after grace can touch the record; and every boundary case revival dragged in.

**The trade accepted.** A saver who misses month 13 and makes it up with a spot purchase in month 14 ends one Month short of a saver who never missed — permanently. That is the design speaking plainly: **Months counts months in which the discipline happened**, and money arriving later is a different, also-welcome behaviour with its own name.

**The day-20 payer.** With no revival, a payment clearing after grace is refused as a SIP contribution and the customer is offered the spot path on the same screen. Grace already absorbs "busy or away"; a tolerance behind a tolerance is no tolerance.

---

## 5. Referrals, family and Masterclass: removed from scoring

> **None of the three is an input to ICS.** All three survive as programmes; none earns a point.

**Masterclass** (removed 2026-08-11) was the only supplementary that was attendance-verified rather than money-verified — the one input that could not be measured off the payment rails.

**Referrals and family** (removed 2026-08-12) go for three reasons:

1. **They corrupt the one clean number.** Months means *months you paid*. The moment a referral adds to it, the customer can no longer compute their own score by hand, and the auditability that makes this design defensible is gone. The alternative — a third weighted component — reintroduces the weighted sum and its trade-offs.
2. **They are already paid, twice over.** Referrals are compensated by the **3-tier agent network** — commission for a function performed. Family is rewarded by the **will and family discount ladder**, one of the five benefits. A third channel pays for the same behaviour a third time.
3. **A status bonus for recruiting is the MLM shape.** Decision 13's anti-MLM defence is explicit: *pay for a function performed, not for recruitment depth.* A commission does that. A **status** bonus for bringing people in does not, and it would sit inside the score a regulator reads.

Each family sub-account already earns its own tier by its own saving, which is the right place for it.

**What is lost, and the answer to it.** The 2026-08-11 draft used supplementaries to pull Sovereign forward to ~month 47 and to fill the mid-climb. That acceleration is gone; the climb is now the same for everyone, which is a *stronger* fairness statement (§7.3 invariant 1) and removes the last route by which anything other than saving could move the score.

⚠ **Client conversation.** Their §8.2 lists referrals, family portfolios and Masterclass as ICS components. All three are removed from the score while surviving as programmes. This is the largest client-facing departure in the file.

---

## 6. The benefit matrix

The master table. Dashes are where a benefit's own preconditions (credit facility, card) do not yet exist. Every ladder is stepped, monotone non-decreasing, and read from the **tier of record** (benefits draft §0.3).

| | **No tier** | **Silver** | **Gold** | **Platinum** | **Sovereign** |
|---|---|---|---|---|---|
| **1. Entry-fee discount** | 0 | 0.4pp | 0.8pp | 1.2pp | **1.5pp** |
| **2. Credit LTV** | — | — | 50% | 65% | **80%** |
| **3. Card level** | — | — | L1 | L2 | **L3** |
| **3. Card FX margin** | — | — | 2.0% | 1.5% | **1.0%** |
| **3. Card ATM allowance** (AED/mo) | — | — | 1,000 | 2,500 | **5,000** |
| **4. Gold Rewards rate** | — | — | 0.15% | 0.45% | **0.75%** |
| **5. Will plan-fee discount** | 0 | 10% | 20% | 35% | **50%** |
| **5. Per-beneficiary discount** | 0 | 0 | 0 | 10% | **20%** |

### 6.1 Entry-fee discount (benefit 1)

0.4pp steps to a **1.5pp ceiling** — the conservative end of the 1.5–2.0pp placeholder, chosen so the required base-rate uplift is as small as possible. First benefit-bearing tier is **Silver** (0.4pp — de minimis, unexploitable, and gives Silver a visible price meaning on arrival at month 6). Cumulative-savings display rule (benefits draft §1.2a) unchanged.

**🆕 The funding ask is smaller than the rulebook implies, and this should go back to §13.** Decision 9 puts Year 1 cost at 4.15% and says a 2% fee *loses* USD 0.71 on a USD 75 contribution; decision 34 puts cash retained at a 5% fee at USD 1.61. Breakeven is therefore **~2.85% at Year 1**, not the 2% floor of the client's stated range. But the binding point is timing: **the ladder is time-phased by construction.** Nobody is above Silver in Year 1, so the maximum discount outstanding at launch is 0.4pp. **The first Sovereign appears at month 60**, by which time decision 9 has bar denomination improving and cost falling toward ~3%. The ladder's cost curve and the business's cost curve are the same curve, offset the right way — so holding the headline at 5% may fund the entire ladder with no uplift at all.

### 6.2 Credit LTV ladder (benefit 2)

> 🔒 **SETTLED 2026-08-13 (Abdur): Sovereign is 80%. The ladder is 50 / 65 / 80 and it is no longer contingent on the partner.**

**The construction:** anchor Sovereign at **80%**, step down **15pp per tier** to Gold, floor 50%. Unlock at **Gold**, honouring the one row of the client's credit table worth preserving.

| Tier | Gold | Platinum | Sovereign |
|---|---|---|---|
| **Max LTV** | 50% | 65% | **80%** |

**Three reasons 80 is the right number to fix on rather than hold open:**

1. **It sits inside every comparable.** Benefits draft §2.3: RBI's 2025 Directions tier India's cap at 85/80/75 by loan size from April 2026, Muthoot and Manappuram lend at the cap, and tokenised-gold lenders run 50% (Fringe) to 80% (Clapp). **80 is the top of the observed range without being outside it**, so no partner conversation starts with us walking a number back.
2. **It reproduces the client's own table exactly.** Their *"Gold Member: 50% LTV"* row falls straight out, while the arithmetic their Sovereign row got wrong is fixed: they wrote "up to 110%" and then worked the example at 8,500 on 10,000, which is 85%. **Their own worked number was never 110, and 80 is one step below what they actually computed.**
3. **A fixed ladder can be advertised; a contingent one cannot.** LTV is struck at draw and runs to term (benefits draft §2). A rate that depends on an unsigned partner agreement cannot go in the app, the terms or the tier table, which means the second-largest benefit in the design stays unquotable until the lending partner signs.

⚠ **Consequence to carry to the partner conversation, not away from it.** 80% is now our number, so **a partner landing below 80 is a repricing event, not a parameter fill.** If the best available partner maxes at 75, the ladder compresses to 45/60/75 or the top rung is subsidised. **Get the partner max confirmed before this reaches a client-facing document.**

⚠ **Warning and liquidation spacing above each step is still the partner's book, not ours**, and at 80% the headroom above the top rung is thin: handoff §4's note that thresholds *"must be re-spaced"* was written against 90–95% and is more binding at 80, not less. 90-day seasoning, LTV struck at draw, **tier fall never margin-calls** — all inherited (benefits draft §2), none reopened.

⚠ **The client will hear this as a downgrade from 90 to 95, and it is.** The line that makes it land: *their own §9.3 example computed to 85%, no UAE lender publishes a loan-against-gold LTV at all, and every comparable in the world sits between 50 and 85.* The 90 to 95 figure was never anchored to anything.

### 6.3 Card tier (benefit 3)

**Three levels, mapped one-to-one onto Gold / Platinum / Sovereign.** The many-to-few problem the benefits draft §3.1 had to solve at seven tiers does not arise at five, and the 4-level variant is dropped. Plastic remains sticky — **never downgrades** — and upgrades on **3 consecutive months** at the qualifying tier before reissue. FX margin runs 2.0% → 1.0% (top held at 1.0 rather than 0.75 until the sponsor's floor economics are known); ATM allowance 1,000 → 5,000 AED/month. Waiver sets per level: sponsor input. Monthly parameters flex with the tier of record at each statement cycle; plastic does not.

### 6.4 Gold Rewards rate (benefit 4)

0.15% → **0.75%** of qualifying spend, starting at Gold with the card. **Monthly qualifying-spend cap: USD 3,000** — above the Kinesis comp (2% capped at USD 2,000 spend) on the cap and far below it on the rate, which is the right side to err on for a rate that must survive the customer-generated funding cap (interchange + credit revenue, net of that customer's custody cost — benefits draft §4, unchanged). At 0.30pp per tier this is the first ladder in the design whose single step is felt in the month it happens: ~**USD 9/month** at the cap.

### 6.5 Will and family discount (benefit 5)

Plan-fee discount 10% → **50%** (the top of the 40–50 placeholder — the cheapest column to be generous in, it prices a service Aurumix sells, and the will is the emotional centre of the product for the persona). Per-beneficiary discount 0 → **20%**, starting only at Platinum so the cheaper lever does the early work. Ceiling below 100% preserved by construction (benefits draft §5.4: never free, or the tier-gate returns in mirror image).

### 6.6 Every rung buys something — the dead-rung check

| Boundary | What changes |
|---|---|
| No tier→Silver | **The gate opens.** Score switches on, first price benefit (0.4pp), first will discount (10%), Silver floor secured permanently |
| **Silver→Gold** | **The big rung:** credit unlocks at 50%, card issues at L1, Gold Rewards begins, discount 0.8pp, will 20% |
| Gold→Platinum | LTV +15pp, plastic → L2, GR 0.45%, discount 1.2pp, will 35%, per-beneficiary begins, ATM 2,500 |
| Platinum→Sovereign | LTV top, plastic → L3, GR 0.75%, discount 1.5pp, will 50%, per-beneficiary 20%, ATM 5,000 |

No dead rungs, and unlike the seven-tier version, no rung whose largest line moves by USD 0.19. **Silver→Gold is deliberately the largest step** — it requires Confirmed SIP plus a year of form, and it is where all three headline features switch on. **The marketing sentence: everything unlocks at Gold, and everything roughly doubles at each step after.**

---

## 7. Fairness verification

### 7.1 Six personas, run under the final formula

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

- **A = C, to the day.** The founding principle as arithmetic: a hundred times the money buys zero tiers. This remains the single most useful row when a regulator asks whether benefits scale with capital.
- **B: one miss in year five costs exactly one tier**, and only because A was sitting on the Sovereign bound with zero margin by design.
- **D sits three tiers below an identical payment record**, held there by one number that cannot be faked, and the floor hands him nothing farmable (§1.6).
- **E: a legitimate 50% withdrawal at year three costs exactly one tier** — the smooth-degradation promise, preserved.
- **F: full liquidation costs three tiers.** Accepted: liquidating everything is the strongest anti-signal the product can receive. F still keeps every benefit already delivered, every gram since repurchased, Confirmed SIP, and a Record that never stopped climbing.
- **E and F both recover in 12 clean months**, as the sale ages out of the window. Deliberate (§1.5), and it is what distinguishes a one-time liquidator from D.
- **G is the row to put in front of the client**, and it only exists after the 2026-08-12 fix: a real household withdrawal of nearly a third **costs nothing at all.** Under the previous convex form G scored 74.1 and lost a tier — the design punished the exact behaviour it had promised to tolerate.
- **H is the cost of the consecutive gate, and it is the row to be honest about.** Six real payments, three years of intermittent saving, and the account has no score and no tier because no six landed in a row. Under the 2026-08-12 definition H held Silver. This is the deliberate trade for removing the gate/score contradiction, and §1.6's countdown display exists so H sees the run they are failing rather than discovering it at year three.
- **I is the uniform-entry row.** Nine paid months across fourteen calendar months, and the door opens on **Silver at exactly 25** — the same place a flawless month-6 saver opens. The six pre-run payments bought gold and bought no score. Every account enters the ladder at one point, which is what lets the promise be stated without a branch. ⚠ It is also the row a customer could feel aggrieved by, which is why §1.6a's countdown is a requirement rather than a nicety.

### 7.2 The four handoff tests (benefits draft §7)

| Test | Result |
|---|---|
| **USD 20 test** | ✅ The USD 20 saver who never misses reaches Sovereign and the ceiling value of all five benefits at month 60, **on contributions alone** — and now with no supplementary route to accelerate, so contributions are the *only* path for anyone. |
| **Cycler test** | ✅ D holds Silver on the floor. The first benefit-bearing tier for credit, card and Gold Rewards is Gold, which D never reaches. The two Silver benefits are price reductions bounded by money handed over. |
| **Withdrawal test** | ✅ E and F lose tiers only. No retroactive repricing (levers strike at event), no margin call (LTV runs to term), no clawback of credited grams, and **Months is untouched**. |
| **Funding test** | ✅ Benefit 1's 1.5pp ceiling is time-phased against a falling cost base (§6.1) and only benefit 1 touches stream 1; benefit 2 is partner-book; benefits 3–4 are bounded by the customer-generated interchange/credit cap by construction; benefit 5 discounts a stream-3 fee floored at partner cost. |

### 7.3 The fairness invariants

1. **No amount, anywhere.** No input reads dollars or grams *held* — Months and Recent count periods, Sold is a proportion. **Capital cannot buy a tier at any rung, and with supplementaries removed, neither can anything else except saving.**
2. **A new saver is never behind.** Retention starts at 1.00; everyone starts outside the gate on the same terms; the climb is identical for everyone.
3. **A miss costs standing, never property.** Gold, Months and Confirmed SIP are untouched by any miss. The fall in Standing is the whole price.
4. **Selling costs standing, never record.** Once the gate opens, Months is a historical fact and nothing reduces it. This is why Retention is a multiplier and not a deduction from Months. ⚠ **Scope note:** the record *begins* at the qualifying run (§1.6), so pre-gate payments never enter it. Nothing removes a month once counted; the rule is about where counting starts, not about taking anything away.
5. **Refused money never scores against you.** The regulatory pause freezes the clock (rulebook §8, decision 36) — inherited unchanged.
6. **Nothing already delivered is ever taken back.** Struck prices, drawn LTVs, issued plastic, credited grams all survive any tier fall.
7. **Decay is faster than rebuild, by arithmetic rather than by rule.** A miss costs 8.33 of Standing instantly and returns only when the window rolls twelve months later.
8. **The score attaches to the person, not the account.** Cancel-and-reopen buys nothing (rulebook §9.1 item 7); a returner resumes.

### 7.4 The one property that has to be proved: Standing never binds a clean saver

For a saver who has never missed, `Recent = min(12, m)`, so `Standing = min(100, 8.333m)`.

- For **m ≤ 12**: Record = 4.167m, Standing = 8.333m. Standing is exactly **2×** Record. Record binds.
- For **m > 12**: Standing = 100, Record ≤ 100. Record binds.

**So `min(Record, Standing) = Record` at every month of a clean climb.** The score of a good customer is purely their Record; Standing appears only when something has gone wrong. This is what makes the ladder communicable as *"Silver at six months, Gold at one year, Platinum at three, Sovereign at five"* without a caveat.

---

## 8. Anti-gaming

The rulebook's three-layer register (§9) is unchanged by any number here. What is new is how much of it is now closed **by construction** rather than by rule:

| Attack | Closed by |
|---|---|
| Prepayment / payment-splitting / date-shuffling | One counted period per calendar month (rulebook §9.1 items 4–6). Unchanged. |
| **Alternating misser** (miss–pay–miss–pay) | **Structural.** Recent holds at 6 forever, so the account is capped at Gold for life. No rule needed; the 2026-08-11 draft needed an explicit trailing-window strike rule for exactly this. |
| **Late lump-sum restoring a record** | **Removed by construction** (§4). No payment after grace can touch the record, so the whole attack class ceases to exist. |
| **Referral farming** | **Removed by construction** (§5). Referrals are not a score input. |
| **Family-account farming** | **Removed by construction** (§5). |
| **Sell then rebuy before assessment** | Sold reads opening balance, acquisitions and closing balance — a rebuy enlarges the denominator but the sale stays in the numerator, so it cannot be erased, only aged out over twelve months. |
| **Timing the sale to cheapen it** | **Closed 2026-08-12.** The old average-balance denominator made a sale cheaper the later in the window it happened. The current measure is timing-neutral by construction (§1.5) — the same sale costs the same whenever it is made. |
| **Sitting just under a threshold** | Nothing to sit under: both inputs move in one direction only, one month at a time, by paying. |
| **Silver floor abuse** | Nothing payable or borrowable passes through it (§1.6), and the consecutive gate now makes the floor strictly harder to reach: six payments no longer suffice, six *in a row* do. |
| **Minimum-effort entry** (buy the cheapest possible way in) | 🆕 **Closed by the gate.** Six consecutive periods cannot be compressed, bought or backdated — one counted period per calendar month, no revival, no arrears. The only way through the door is six months of elapsed discipline, which is the one cost no attacker can shortcut. |
| Cancel-and-reopen | Score attaches to the person (rulebook §9.1 item 7). Unchanged. |

**Net: six of eleven attacks are now structurally impossible rather than defended against** (was five of nine before the 2026-08-13 gate). That is the strongest single argument for the rewrite.

---

## 9. Comps grounding

Run via recency-swept web research (2026-08-11); secondary-source confidence unless noted. Used to defend calibration, not to derive it.

| Our choice | Category precedent | Read |
|---|---|---|
| First miss ≤ one tier | Airline "soft landing": drop one level on failed requalification, annual cadence (Air Canada documents the mechanism; annual evaluation is the industry norm) | Ours is gentler than the category at the first miss (mid-band savers lose nothing) and harsher on a sustained pattern, which is the intended asymmetry |
| Record + Standing as two gates | Airlines run lifetime status (Million Miler) *alongside* annual status as two separate systems | Same two layers. They keep two ladders; we combine into one via minimum — a simplification, and the minimum is what preserves the AND that two separate ladders give for free |
| No revival at all | IRDAI *mandates* a 3-year revival window — because an insurance lapse breaches a premium obligation and the cover dies without revival | The comp explains why we don't need it: Aurumix deleted the contractual obligation with the lock-in, so a miss kills nothing. Revival is an insurance solution to a problem this product designed out |
| Trailing-window retention vs window-dressing | Bank tiers use daily/monthly *averaging* (Citi CAMB, DBS daily-average) precisely so a one-day balance spike buys nothing | Averaging over time is the standard institutional answer to snapshot gaming. Our change from lifetime to trailing-12 keeps that property while fixing the age-inertia problem lifetime averaging creates |
| No hysteresis in the score | Banks damp downgrades (Citi: 3 consecutive shortfall months; BofA: anniversary + grace) | They damp at the tier because their benefits reprice instantly; ours damp at the benefit (strike-at-event, run-to-term), so damping the score too would double-count |
| Behaviour, never amount | The industry has moved the *opposite* way (Delta MQD, AA Loyalty Points are pure spend) | Deliberate inversion and the differentiation claim: in a category with zero behaviour-based benefits, and an adjacent industry pricing status by spend, a scale-free score is unique on both axes |
| Sticky plastic | No bank comp upgrades the physical card with relationship tier at all | Our plastic ladder is *more* generous than banking practice — a sponsor conversation, not a compliance one |
| Five tiers | Airline programmes run 4–5 published levels; bank relationship tiers run 3–4 | Seven was above the category norm and above what the benefit set supports |

---

## 10. Open dials and external inputs

**Dials (ours, revisit on field data):**
- **Retention allowance 30%** — the single number most worth re-cutting once withdrawal behaviour is observable. The curve is linear; the exponent dial is retired (§1.5).
- **Retention window: 12 months.** Lengthening it makes a one-time liquidation bite longer; shortening it makes the design more forgiving of a sale than of a miss.
- Record kink at **month 12** and the **60-month cap**.
- **Sovereign's zero tolerance** — the "one free miss" variant is specified and costed in §1.8 if churn data ever justifies it.
- Qualifying-spend cap **USD 3,000/month**; plastic upgrade rule **3 months**.

**Sub-decisions, resolved 2026-08-13 (Abdur) except where marked:**
1. [x] ✅ **Lender liquidation on a margin call counts as a sale** (§1.5). The alternative makes borrowing a route around Retention.
2. [ ] ⚠ **STILL OPEN, deliberately: a compliance-forced exit (the returning NRI, decision 31) drives Retention to zero for something the customer did not choose.** Decision 36's regulatory pause covers refused *payments*, not forced *sales*. Proposed: **extend the pause to cover forced redemptions** — the grams leave, the score does not move. **Left open at Abdur's instruction 2026-08-13**, not rejected. ⚠ It interacts with item 1: a forced sale and a margin call are both sales the customer did not pick the day of, and the design currently answers them differently. Close them together.
3. [x] ✅ **A frozen month is skipped entirely, as though it never existed, and the window extends to reach 12 countable months** (§1.9). Applies on both clocks and on both sides of the gate.
4. [x] ✅ **Every account passes its own gate**, sub-accounts included (§1.9).
5. [x] ✅ **A pause freezes the qualifying run rather than breaking it** (§1.9).
6. [x] ✅ **Partner-channel customers earn no ICS at all** (§1.9). Decided ahead of the partner contract, which must say so explicitly.

**Considered and deliberately left alone (Abdur, 2026-08-13). Recorded so nobody re-raises them as oversights:**

| Item | Status |
|---|---|
| **Pre-run gold counts in Retention's denominator, while pre-run payments score nothing.** A saver's early purchases can cost them score if sold, having never earned any | **Accepted.** Retention reads the token ledger and the ledger does not know about the gate. The asymmetry is real and is not being designed away |
| **The zero-benefit paying customer.** Months 1 to 5 pay the full entry fee and receive nothing — no score, no tier, no discount — and longer if the run breaks | **Accepted.** The countdown display (§1.6a) is the mitigation |
| **Inheritance: does a Digital Will beneficiary inherit the tier and the Months?** | **Not designed.** Will surface in year one |
| **Agent-onboarded accounts: whose behaviour is scored** when an advisor invests for a client | **Left as-is.** The agent system is unchanged pending the IRDAI 2023 caps |
| **The cycler-plus-agent combination** (rulebook §365): a cycler generates real counted periods, so an agent can earn commission on customers worth nothing to Aurumix | **Left as-is.** The 12-month commission clawback is the only defence and it holds pending the same IRDAI retrieval |

**Client questions:**
1. The entry-fee base-rate uplift funding benefit 1's ceiling (rulebook §13). **🆕 The ask is smaller than previously stated and may be zero — see §6.1.** Re-put it with the time-phasing argument.
2. Whether the raw score (0–100) is customer-visible or tier-only. **Recommendation: show the number.** The persona knows CIBIL; a visible score with visible progress is the cheapest retention surface in the product, and it now has a second use — **the score names its own constraint** (§1.2), so the app can tell the customer exactly what to do next.

**Client-facing changes to communicate — the full list:**
- **Seven tiers become five, and the bottom one is renamed.** Titanium and Elite are dropped; Green becomes **"No tier"** (§2.1). Four named rungs.
- **Confirmed SIP stays 6 consecutive contributions, and it now gates the score itself** (§1.6). Before it: no score, no tier, no benefits. After it: permanent, and never below Silver. **The score never contradicts the gate because it does not exist before it.**
- **Referrals, family portfolios and Masterclass no longer score.** All three survive as programmes (§5). This departs from their §8.2 in three places.
- **No revival or arrears mechanism.** A missed month is missed; late money is a spot purchase (§4).
- **Sovereign arrives at month 60** on contributions alone, with no acceleration route.
- 🆕 **Max LTV is 80%, not 90 to 95%** (§6.2). The ladder is 50 / 65 / 80. **Expect this to land as a downgrade, because it is one.** Their own §9.3 example computed to 85%, no UAE lender publishes a loan-against-gold LTV at all, and every comparable sits between 50 and 85, so the 90 to 95 figure was never anchored to anything. Their *"Gold Member: 50%"* row survives exactly.
- 🆕 **Partner-channel customers earn no ICS** (§1.9). The score is a direct-channel feature. This is a strategic position, not only a mechanic, and the partner agreement must state it.
- 🆕 **Every account passes its own gate, sub-accounts included** (§1.9). Nobody inherits a family member's status.

**External inputs (not B4's to close):** ~~partner max LTV~~ 🔒 **fixed at 80% by decision, 2026-08-13 (§6.2) — no longer an input, and a partner below 80 is now a repricing event**; warning/liquidation spacing above each step; sponsor level count, floor economics and waiver sets; contracted interchange share; vault quote; stream 3 base prices and per-name cost.

---

## 11. What exists on day one

Inherited from benefits draft §6: at launch the tier buys the **entry-fee discount** and **will discount** columns only; the LTV column activates with the lending partner, the card and Gold Rewards columns with the sponsor bank. The tier is communicated as the durable thing; the matrix is what it currently buys. Nothing here changes that sequencing — and §6.1's time-phasing note means the launch-year cost of the whole ladder is one 0.4pp Silver discount.

---

## 12. What this file changes elsewhere

- [x] ✅ 🆕 **CANCELLED 2026-08-13: the *"6 contributions"* sweep is not to be run.** Confirmed SIP stays **6 consecutive contributions** (§1.6), so `_draft_sip-rulebook.md` §4.1 and `handoff.md` decision 19 keep their existing wording and need **no** change on this point. Anyone picking up the 2026-08-12 version of this list should stop here.
- [ ] 🆕 `_draft_sip-rulebook.md` §4.1: add that Confirmed SIP now gates **the score**, not only the benefits, and that pre-gate accounts have no score and no tier (§1.6).
- [x] ✅ 🆕 **Green → "No tier" rename: SWEPT 2026-08-13, and it was four fifths phantom.** The four drafts this list named — `_draft_sip-rulebook.md`, `_draft_ics-benefits.md`, `_draft_sip-spot-and-ics.md`, `Aurumix_Process_Maps_ICS_Benefits.md` — **contain no tier names at all.** They were written with tier as an abstract input, exactly as intended, so there was nothing to rename. ⚠ **The only live occurrence in our own work was `_build_ics_calculator.py`.** Remaining hits are in files that *describe the client's* seven-tier scheme (`Aurumix_V3_Business_Model_Explained.md`, `questions-discussion.md`, `company container/notes/Aurumix_V3_Summary.md`, and the client's own document) — **those are accurate records of their model and must not be renamed.**
- [x] ✅ 🆕 `handoff.md` §4 product-in-brief and decision 46: corrected 2026-08-13. Five tiers, four named rungs, No tier at the bottom.
- [x] ✅ 🆕 `_draft_sip-rulebook.md` §11: **marked SUPERSEDED IN FULL** with a banner naming every replacement (no weights, minimum not sum, five tiers, no step-down, no revival, 30% allowance). Table retained as audit trail.
- [x] ✅ 🆕 `Aurumix_Process_Maps_ICS_Benefits.md` diagram 1b rebuilt on the settled ladder: **month 56 → 60**, **2pp → 1.5pp**, **0.6655 g → 0.6621 g**, delta 0.0103 g/month. The 1.5–2.0pp placeholder note under diagram 1 is replaced with the settled ceiling and the time-phasing argument. ⚠ **The "seven-tier references throughout" warning in the earlier version of this list was overstated:** diagram 1b was the only stale content in the set.
- [x] ✅ 🆕 `Aurumix_Process_Maps_SIP_Structure.md` diagram 10 and its speaker notes: three of the four open items are now closed (tier count, discount funding, the direct-debit rail), leaving only the client's spot-versus-SIP fee structure. Closed nodes recoloured gold.
- [x] ✅ 🆕 `Aurumix_Process_Maps_Revenue_Streams.md`: "climb seven tiers" → "climb the whole ladder".
- [x] ✅ 🆕 **Both build scripts made portable.** `_build_ics_calculator.py` and `_verify_ics_calculator.py` had the output path hardcoded to one workstation (`C:\Users\BlockApex\...`) and **failed on every other machine.** Now resolved relative to the script. Rebuilt and re-verified: **182 formulas, 0 errors, 20/20 spot-checks, 4/4 invariants.**
- [ ] 🆕 `Aurumix_ICS_Score_Calculator.xlsx`: **the rename and the gate test case are done** (the scattered payer now reads 0 → No tier). ⚠ **Still owed: the gate itself is not modelled as a mechanism.** Add the pre-gate run counter (0–6, no score), and decide whether the Rajesh story should open with the qualifying run rather than at month 1.
- [ ] 🆕 Build: pre-gate the engine tracks only the **current run length (0–6)** and displays a **"n of 6"** countdown, never a score, with an explicit reset message on a broken run (§1.6a). **Months and Recent both start at the first month of the qualifying run**, so every account opens at exactly 25.
- [ ] `_draft_sip-rulebook.md` §7.1: **delete the arrears row entirely**; add the spot-path line (money after grace is offered as a spot purchase).
- [ ] `_draft_sip-rulebook.md` §7.1/§7.2: delete "Continuity halves" and everything downstream of it — **there is no step-down mechanism to describe**, only Standing. Delete "Arrears are one payment, not instalments"; delete "Arrears buy gold at the fix on the day they clear"; delete the rebuild-rate prose. Correct "The step-down applies at grace expiry **and reverses on revival**" → a miss reduces Recent for twelve months and then ages out; grace is the only tolerance.
- [ ] `_draft_sip-rulebook.md` §9.1 item 9 (arrears look-back exploit): **moot** — no restoration path exists.
- [ ] `_draft_sip-rulebook.md` §9.4 and §9.5 (referral and family anti-gaming rules): **moot** — neither is a score input (§5).
- [ ] `_draft_sip-rulebook.md` §11: mark the entire proposed parameters table **superseded**. Tenure/Continuity/Supplementary caps, the weighted structure, the 0.80 lifetime allowance and the proposed thresholds are all replaced.
- [ ] `_draft_sip-rulebook.md` §13: **re-put the entry-fee funding question** with the time-phasing argument (§6.1). The ask is smaller than stated and may be zero.
- [ ] `_draft_ics-benefits.md` §7: the closed handoff list is **supplied in full** by §6 here. §0.3 (tier of record) is confirmed as assumed and unchanged.
- [ ] `_draft_ics-benefits.md` §3.1: the plastic/parameter split survives, but the **many-to-few mapping problem and the 4-level variant are moot** at five tiers.
- [ ] `Aurumix_Process_Maps_ICS_Benefits.md`: **8 diagrams need a tier-count pass** (seven-tier references throughout). A companion scoring map set (the climb, the miss, the cycler, the min-gate) is now drawable and owed when process maps are next batched.
- [ ] `handoff.md`: decision 46 to be **rewritten in full**; decision 36's arrears half is moot; decision 20's "referrals, family and Masterclass as capped supplementaries" is superseded.
- [ ] 🆕 **`_draft_ics-benefits.md` §2.3: the LTV research section now has an answer.** `min(partner max, 90%)` is replaced by a flat **80%** (§6.2). Mark the 90 to 95 ceiling retired and keep the 50 to 85 comps as the evidence for 80. §2's inherited rules (90-day seasoning, struck at draw, tier fall never margin-calls) are unchanged.
- [ ] 🆕 **`handoff.md` §4: "max LTV 90 to 95% (corrected from 110%)" → 80%**, and the note that warning/liquidation thresholds must be re-spaced is **more** binding at 80, not less.
- [ ] 🆕 **`handoff.md` decision 45: the partner-channel ICS question is closed** (no ICS) rather than deferred to Phase 4, and the LTV item is settled at 80.
- [ ] 🆕 **`_draft_sip-rulebook.md` §8: extend the regulatory pause explicitly to the pre-gate qualifying run** (§1.9). It currently reads as a post-gate mechanism only.
- [ ] Client conversation: the items in §10, now including the LTV downgrade and the partner-channel exclusion.

---

## 13. Sources

| Claim | Source | Confidence |
|---|---|---|
| Airline soft landing (one-tier step-down), annual requalification norm | Air Canada Aeroplan published downgrade/extension rule; industry coverage of annual status cycles (web research 2026-08-11) | Medium-High (Air Canada primary-adjacent; norm claim secondary) |
| Lifetime + annual dual status | Delta Million Miler / AA Million Miler alongside annual status | High (well-documented programme structures) |
| Published tier counts (airline 4–5, bank 3–4) | Programme structures as above | Medium-High |
| IRDAI revival: 3-year window, arrears + interest, contestability restart | IRDAI Master Circular (2024) as summarised in current-practice guides | Medium (⚠ pull the Master Circular primary text before client use) |
| Bank tier averaging and downgrade damping | BofA Preferred Rewards, Citi CAMB, DBS My Treasures published tier rules | Medium-High |
| Spend-based industry trend | Delta MQD / AA Loyalty Points structures | High |
| Gold-collateral LTV comps (50–85%) | Inherited from `_draft_ics-benefits.md` §2.3 — not re-verified here | As stated there |
| Y1 entry-fee breakeven ~2.85% | Derived from decision 9 (2% loses USD 0.71 on USD 75) and decision 34 (5% retains USD 1.61) | High (internal arithmetic on two stated figures) |
