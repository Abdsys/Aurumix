# The Purchase Structure: SIP, Spot, and the Full Gold-to-Cash Cycle

> **Status: decision draft, 2026-08-06.** Specifies how an investor actually buys gold on Aurumix, in both lanes, from the moment money leaves their bank to the moment cash returns to it. Settles the collection mechanism, the failure ladder, the missing SIP states and the exit.
>
> **Scope note.** Minimum ticket size and collection economics are **deliberately out of scope** and are parked in `_parked_collection-economics-and-minimum-ticket.md`. This draft answers *how the mechanism works*, not *what it costs*. Where a cost genuinely changes a mechanic (the bank's failure fee, which inverts the retry policy) it is named and no further.
>
> Sits downstream of `_draft_allocation-and-float.md` (procurement, float, allocation), `_draft_sip-spot-and-ics.md` (the SIP/spot split, the ICS structure) and `_draft_entities-licensing-and-payments.md` (entities, licences, client money). It **changes a mechanism in the second.** Reconciliation list in section 8.

---

## 1. What this settles

Six findings, in order of how much they move.

**1. VARA forbids charging anything on the way out, and that kills the decaying spot redemption fee.** Verified at primary source. **Rule III.E.4, Annex 2, Virtual Asset Issuance Rulebook: "VASPs Licensed to issue ARVAs shall process and complete redemption requests without charging any fees."** The mechanism survives in a different form: it moves to the entry side as a **tenure rebate**, charged at the door and paid back in grams for holding. Section 5.2.

**2. Zero-fee exit is affordable, and the reason is the float.** An exit does not trigger a gold sale. The grams return to the float and are consumed by the next buyer. The dealer's bid-ask spread is therefore paid **only on net outflow, not on gross exits**. In a growing book, net outflow is rare. This is what makes Rule III.E.4 survivable and it is the fourth job the float was already doing.

**3. The token ledger and the title register are two halves of one ledger, and no draft has absorbed this yet.** **Rule III.B.1.c** requires an issuer to "ensure all transactions in the ARVA result in a corresponding transaction in the Reference Asset being legally settled, completed and/or transferred." There is no such thing as a token movement that is only a token movement. Every mint, every peer transfer, every burn moves gold title. Section 2.3, and it has three consequences that are real engineering work.

**4. The order is money, then title, then token, and it is never any other order.** If title cannot be recorded, the token must not exist. This is the mechanical form of the backing invariant, and it is what separates Aurumix from Comtech's disclosed unbacked window.

**5. A failed payment and a decision not to pay are different events, and the product currently cannot tell them apart.** Published benchmarks put involuntary churn at **20% to 40% of total subscription churn**. Worse, the customer's own bank charges them **AED 105 (about USD 28.59)** for a returned direct debit, which is 143% of a USD 20 contribution. **That single tariff line inverts the standard retry playbook.** Section 3.4.

**6. Three SIP states exist in reality and in no draft: declared pause, dormancy, and regulatory pause.** The third one closes the returning-NRI gap flagged in `_explainer_how-we-take-money.md` §7 and in decision 31. Section 3.5.

### What this changes in existing drafts

| Draft | Change |
|---|---|
| `_draft_sip-spot-and-ics.md` | **Lever 3 changes.** "Time: spot grams carry a decaying redemption fee" becomes "Time: spot grams earn a tenure rebate." Same economics, opposite direction, legal instead of prohibited |
| `_draft_sip-spot-and-ics.md` | Add **declared pause**, **dormancy** and **regulatory pause** as defined states, and the **failure versus non-payment** distinction |
| `_draft_entities-licensing-and-payments.md` | Add the **client money split rule**, which decision 29 flagged as undesigned, and the **III.B.1.c reconciliation requirement** |
| Decision 5 (custody at entry and exit) | **The exit half is dead.** Rule III.E.4 prohibits it. Section 7 |

---

## 2. The purchase lifecycle, end to end

This section is the same for both lanes. The lanes differ in what triggers stage 1 and in what is charged, not in what happens to the money or the metal.

### 2.0 Stage zero: the identity gate

Nothing in this product can happen before this stage completes, and that is a direct consequence of choosing direct ownership.

Under Option A the token is permissioned (ERC-3643 base, decision 24). A permissioned token **cannot be delivered to an unregistered address**. So identity verification is not a compliance chore running alongside onboarding, it is a **hard precondition of the mint**. If verification is pending when funds clear, the money sits in the Client Account and no gold is allocated.

| # | Step | Actor | Output |
|---|---|---|---|
| 0.1 | Account opened, **country of residence** captured | Investor | Residence, not passport, decides eligibility |
| 0.2 | KYC, sanctions and PEP screening | Aurumix / provider | Pass, refer or reject |
| 0.3 | Eligibility check against the country perimeter | Aurumix | Accept, or decline with reason |
| 0.4 | Wallet provisioned, identity claim written to the on-chain registry | Aurumix | The address is now mint-eligible |
| 0.5 | Bank account registered and **name-matched to the account holder** | Investor | The funding account of record |
| 0.6 | Terms accepted, including bailment terms and the title construct | Investor | The contractual half of ownership |

> ⚠ **Step 0.5 is load-bearing and easy to skip.** The whole payment design rests on one test: whose bank account sends the money. If the funding account is not name-matched at onboarding, that test cannot be applied at payment time, and the stablecoin design in `_explainer_how-we-take-money.md` collapses. Name-match at onboarding, then reject any inbound payment from an unmatched account.

### 2.1 The nine stages of a purchase

| # | Stage | Actor | Timing | What actually happens |
|---|---|---|---|---|
| 1 | **Instruction** | Investor | T | SIP: the contribution date arrives. Spot: the investor places an order |
| 2 | **Collection** | Rail | T to T+1 | Funds pulled (mandate) or pushed (transfer) |
| 3 | **Client Account** | Aurumix | within 1 calendar day of receipt | Credited to the designated Client Account at a UAE bank. **Not Aurumix's money** |
| 4 | **Price struck** | LBMA | first AM fix after cleared funds | The benchmark. Published, auditable, not chosen by Aurumix |
| 5 | **Grams calculated** | Aurumix | same moment | (Contribution less entry fee) ÷ fix per gram |
| 6 | **Title transferred** | Vehicle / register | same day | Grams move from the float's position to the investor's sub-account in the title register |
| 7 | **Tokens minted** | Contract | same day | 1 AURX per gram, to the investor's registered address |
| 8 | **Money settles** | Aurumix | same day | Client Account pays the dealer for metal; retained margin moves to the company account |
| 9 | **Records** | Aurumix | same day | Gold Receipt updated, ICS event recorded (SIP only), float drawdown logged |

**Stages 10 to 12 are invisible to the investor** and are the treasury cycle already specified in `_draft_allocation-and-float.md`: threshold check, bar procurement at one bar denomination of cumulative drawdown, and the monthly Allocation Report.

Target: **stages 1 to 9 complete within 24 hours of cleared funds.** The only published category benchmark is XAUm at T+3.

### 2.2 Where the money legally sits, moment by moment

This is undesigned in every existing draft and decision 29 names the gap explicitly. Here is the rule.

| Moment | Whose money | Where it sits |
|---|---|---|
| Before collection | The investor's | Their own bank |
| On receipt | **Client money** | Collection account, then designated Client Account within one calendar day |
| Between receipt and allocation | **Client money, in full.** No part of it is Aurumix's yet | Client Account |
| At allocation (stage 6 completes) | **Split.** See below | |
| After allocation | Metal cost to the dealer; margin to Aurumix | Dealer account and company account |

**The split rule, proposed:** the entry fee ceases to be client money **at the moment title transfers**, and not before. VARA's Client Money definition excludes money "immediately due and payable to a VASP for its own account", and the fee becomes due when the service is delivered. **Title transfer is the delivery.** Before that moment the investor is owed either gold or their money back, so all of it is theirs.

> ⚠ **A precision that matters for the accounts.** The entry fee is a **price, not a cash line.** On a USD 75 contribution at Year 1 assumptions, USD 75.00 leaves the Client Account: **USD 73.39 to the dealer** for 0.6518 g at fix plus a 3% fabrication premium, and **USD 1.61 to the company account** as retained margin. The disclosed fee is 5% (USD 3.75); the cash Aurumix actually keeps is USD 1.61, because the premium is buried inside it. Both numbers are true and they are not the same number. **Disclose the fee; budget the margin.**

### 2.3 Where the gold legally sits, moment by moment

Under Option A this is not bookkeeping, it is the product. **Rule III.B.1, Annex 2, verified at primary source**, requires an ARVA issuer representing direct ownership to:

> a. "ensure the right of ownership is legally and validly established and that such right of ownership is transferred in the event of a transfer" of the ARVA;
> c. "implement mitigating measures to ensure all transactions in the ARVA result in a corresponding transaction in the Reference Asset being legally settled, completed and/or transferred."

| Moment | Who owns the grams | Where the record sits |
|---|---|---|
| In the float | Aurumix outright, from its own capital (or the dealer, under a dealer-carried float) | Float position, segregated in the vault and in the accounts |
| At allocation | **The investor** | Sub-account beneath the vehicle's warrant or vault position |
| While held | The investor | Same, updated on every transfer |
| On pledge for credit | The investor, encumbered | Same, with a registered charge |
| On exit | Back to the float | Float position |

**Three consequences of III.B.1.c, all of them real work:**

1. **The register write must gate the mint.** If title cannot be recorded, the token must not exist.
2. **A peer-to-peer AURX transfer requires both parties to be registered holders**, because the gold has to move to somebody identified. This is the same argument that forces the permissioned token, and it applies with equal force *after* issuance, not just at issuance.
3. **Any venue listing AURX must itself be an approved participant with registered customers.** An open DEX listing is incompatible with Option A. **Flag this to the client early; it constrains the liquidity story.**

### 2.4 The invariants

Carried from the allocation draft, plus two new ones.

- **Backing:** `float_grams + allocated_grams ≥ tokens_outstanding`, at all times, both sides published monthly.
- **Reconciliation (new):** `sum(register sub-account balances) = tokens_outstanding`, checked on every block containing an AURX transfer, reported on exception. This is the III.B.1.c invariant.
- **Client money (new):** `Client Account balance ≥ sum(collected funds not yet allocated and not yet refunded)`, checked daily.
- **Ordering:** money, then title, then token. Minting halts automatically if the float reaches zero, if custodian attestation lapses, or if the register is unavailable.

---

## 3. The SIP lane

### 3.1 What a SIP actually is here

Not a contract. Not a lock. An **instruction with a schedule**, plus a score that watches whether it was honoured.

| Attribute | Value | Fixed or variable |
|---|---|---|
| Declared amount | The investor's chosen monthly figure | **Variable month to month.** Client-confirmed |
| Declared minimum | The floor below which a payment does not count as a contribution | Set at declaration, changeable |
| Frequency | Monthly by default | Investor's choice |
| Contribution date | The investor's own anniversary | Investor's choice from an available set |
| Rail | Mandate (pull) or approved push | Section 3.2 |
| Goal | Optional target: duration or grams | **Scores nothing.** Progress display only |

**The declared amount and the declared minimum are two fields, not one**, and the distinction resolves a contradiction the client's own document carries. §6.3 requires six consecutive events "at the same monthly commitment" while the amount is confirmed variable. **Confirmed SIP counts periods in which a payment at or above the declared minimum arrived.** Paying more than the declared minimum buys more gold and changes nothing else.

### 3.2 Is it a direct debit? Partly, and the reason it is not universally one is mechanical

Three collection mechanisms exist in the UAE and none of them does the whole job.

| Mechanism | Type | Live? | Investor action each month | On failure |
|---|---|---|---|---|
| **UAEDDS direct debit** | **Pull**, mandated once | Yes | **None** | **Investor's own bank charges them AED 105** |
| **AANI Request to Pay** | **Push**, approved per payment | **Yes, live** | One tap to approve | Nothing happens. A declined request is not a failed payment, and carries no fee |
| **AANI electronic direct debit** | Pull, mandated | **Announced, not live** | None | Unknown |
| Card on file | Pull | Yes | None | Issuer-dependent |

**Why a pull is worth wanting.** A mandate removes the monthly decision, and removing the monthly decision is the entire behavioural thesis of a SIP. Published benchmarks put bank direct debit first-attempt failure at roughly **2 to 3%**, against **10 to 15% for recurring cards** (Recurly, GoCardless). As an instrument, pull beats push by a wide margin.

**Why push still has a role.** A pull that fails costs the investor AED 105 charged by their own bank. A push that is not approved costs them nothing. **For a thin-balance customer the push rail is safer for them**, and safer for Aurumix's churn, even though it asks for an action.

> **The mechanism, recommended.** Offer a **UAEDDS mandate** as the default and a **Request to Pay** alternative, with a push notification on the contribution date and reminders on days 3, 8 and 14 of the grace period. **Both count identically for ICS.** Move any investor to the push rail after two consecutive mandate failures. Migrate everyone to AANI electronic direct debit when it launches, which gets mandate behaviour without the failure penalty.

⚠ **Note what this does to a stated product feature.** "Set it and forget it" is true on the mandate and not on the push rail. Do not market automatic collection to every investor until AANI electronic direct debit is live. Where the push rail applies, say **"one tap a month"** and mean it.

### 3.3 The allocation price, and the rule that removes gaming

Grams are struck at the **first LBMA AM fix after cleared funds**, never at the fix on the contribution date and never at a fix the investor can select.

This matters more than it looks. Any rule that lets either side choose between two known prices hands that side a free option. Three places in this design need the same treatment and all three get it:

| Event | Priced at | Option removed |
|---|---|---|
| On-time contribution | First fix after cleared funds | Neither side selects |
| **Arrears / revival** | **The fix on the day the arrears clear**, never the missed period's fix | Otherwise revival is a free one-directional look-back on gold, exercised only after the price rises |
| **Exit** | **The next fix after the request**, never the last published fix | Otherwise the investor requests only when the market has fallen since the fix |

**One rule, stated once: the price is always the next fix nobody has seen yet.**

### 3.4 When a contribution does not arrive

Two things happen that the existing draft does not distinguish, and the distinction is worth money.

| | **Failure** | **Non-payment** |
|---|---|---|
| What it is | A debit was presented and rejected, or a request was sent and not approved | No instruction existed, or the investor chose not to pay |
| Whose fault | Usually administrative: balance timing, expired mandate, bank block | The investor's decision |
| Frequency | 2 to 3% of direct debits, 10 to 15% of card attempts | The real churn signal |
| Cost to the investor | **AED 105 if it was a presented direct debit.** Zero on a push request | Zero |
| Correct ICS treatment | Grace, then step-down only if unresolved | Grace, then step-down |

Published benchmarks put **involuntary churn at 20% to 40% of total subscription churn** (ProfitWell), and as high as 34% (Forrester). Applied to Aurumix's persistency assumption, of the roughly six in ten investors gone by month 61, **a quarter to a third never decided to leave.** They failed a payment and the product treated it as a decision. The existing grace-and-revival design already recovers most of that. What it does not yet do is **tell the two cases apart in the data**, which is what you need to know whether the ICS ladder is calibrated correctly.

**The retry policy, and it is counter-intuitive.**

The standard subscription answer is aggressive dunning: a first retry recovers 40% to 60% of soft declines, and three to five retries push cumulative recovery above 60%. **That answer is wrong here, and the reason is AED 105.**

Every re-presented UAEDDS debit that fails costs the investor **about USD 28.59, charged by their own bank**. On a USD 20 contribution that is a 143% penalty. A three-retry dunning ladder on a thin-balance customer could charge them **roughly USD 85 in bank fees to collect USD 20**, and Aurumix would never see the money or the reason for the churn.

> **Policy: never re-present a UAEDDS debit automatically. Not once.**
>
> On a failed debit: notify immediately, tell the investor their bank has charged them, and switch that period to a **push request** inside the grace window. A push carries no failure fee, so it can be nudged three times at zero cost to the investor. Re-present the mandate only for the following period, and after two consecutive failures move the investor to the push rail permanently.

This is a case where the standard playbook actively harms the customer, and the correct policy falls straight out of one published tariff line.

**The cases, restated with the rail included.** Carried from `_draft_sip-spot-and-ics.md` §5, unchanged in substance.

| Case | Gold | ICS | Rail action |
|---|---|---|---|
| Pays on time | Allocated | Accrues | None |
| Pays less, at or above declared minimum | Less gold, proportionally | **Unaffected** | None |
| Pays late, within 15-day grace | Allocated at the fix on the day funds clear | **Unaffected** | Push nudges on days 3, 8, 14 |
| **Debit rejected** | None yet | Unaffected during grace | **No auto re-presentment.** Switch to push |
| No payment within grace | **Untouched** | **Steps down. Never resets.** Streak breaks, Confirmed SIP suspends, credit ladder stops climbing | Mandate retained |
| Spot purchase | Allocated | **None** | n/a |

### 3.5 Pause, stop, dormancy: three states no draft has

**Declared pause.** The investor tells Aurumix they are stopping for a period. Indian mutual fund platforms all offer this and investors use it. Proposal: **ICS freezes rather than steps down**, for up to **3 consecutive periods, once in any 12 months.** The streak is preserved, tenure does not accrue, no gold is allocated.

Reasoning: a declared pause is a communication, and communication is exactly the behaviour the score exists to reward. **An investor who tells you they are pausing is worth more than one who silently misses**, and the design should price that difference. Abuse is bounded by the cap.

**Stop.** The investor cancels. No penalty, nothing forfeited, gold untouched, mandate cancelled. Restarting is a new SIP; ICS resumes from wherever the decay ladder left it, subject to the 12-month revival window. Already implied by the lock-in deletion; state it explicitly so the app has a defined state.

**Dormancy.** After **12 consecutive periods with no contribution and no declared pause**, the SIP is closed as an instruction. The mandate is cancelled and the account becomes hold-only: gold retained, no ICS accrual, no credit ladder, buyback available. Precedent: AMFI's April 2026 data shows Indian AMCs purging SIP accounts that had not paid for **three months**, which spiked the reported stoppage ratio to 296%. Twelve periods is deliberately far more generous and it aligns with the revival window.

**Regulatory pause.** This closes the returning-NRI gap flagged in `_explainer_how-we-take-money.md` §7 and in decision 31. An investor who moves to a jurisdiction Aurumix cannot serve **cannot legally contribute**, and the product currently cannot tell that apart from a miss.

| | Treatment |
|---|---|
| Gold | Retained in full |
| New contributions | Blocked |
| ICS | **Frozen at its current level.** No step-down, no accrual |
| Confirmed SIP | Retained |
| Credit facility | Existing drawings run to term. **No new draws** |
| Buyback | Available, paid to their bank in the new jurisdiction subject to the same rules |
| Family portfolio, Digital Will | Retained. Beneficiary eligibility re-checked at trigger |

**A forced stop is not a broken promise and must never be scored as one.** Same principle as the grace period, applied to a legal event rather than an administrative one.

### 3.6 The structure, assembled

```
DECLARE            amount (variable), declared minimum, frequency,
                   contribution date, optional goal (scores nothing)
                            |
MANDATE / CONSENT  default -> UAEDDS mandate (pull)
                   alternative, or after 2 failures -> push request
                   migrate all to AANI eDD when live
                            |
COLLECT            on the investor's own anniversary date
                            |
   +----------------+----------------+-----------------+
   |                |                |                 |
 CLEARED       LATE (<=15d)      FAILED           NO PAYMENT
   |                |                |                 |
 allocate      allocate at      notify, NO        grace expires
 ICS accrues   clearing fix     re-presentment,   ICS steps down
               ICS unaffected   push nudge        gold untouched
                                                        |
                                                  REVIVAL <=12m
                                                  arrears at the
                                                  CURRENT fix,
                                                  score restored
                                                        |
                                                  12 periods silent
                                                  -> DORMANT

PARALLEL STATES    declared pause (<=3 periods, 1x per 12m) -> ICS frozen
                   regulatory pause (jurisdiction change)   -> ICS frozen
                   stop                                     -> nothing forfeited
```

Three rules govern the whole diagram and each prevents a specific failure:

1. **Arrears price at the fix on the day they clear.** Otherwise revival is a free one-directional look-back option on gold.
2. **Arrears clear as one payment, not instalments.** Partial revival is a state the tier ladder cannot represent. This closes the third deferred item in the handoff.
3. **The gram count only ever rises.** Every consequence falls on tier, fee or credit ratio. *You can lose your status. You can never lose your gold.*

---

## 4. The spot lane

### 4.1 The same pipe, a different door

A spot purchase runs through the identical nine stages in section 2.1. Stage 1 is an order rather than a schedule. **That is the only mechanical difference.** The gold is identical, the fix is identical, the receipt is identical, the settlement is identical.

| | SIP contribution | Spot purchase |
|---|---|---|
| Trigger | Scheduled, own anniversary | On demand |
| Rail | Mandate or push request | Push or bank transfer. No mandate needed |
| Entry fee | Base rate, **discounted by ICS tier** | **Flat, top of range, no discount** |
| Earns ICS | Yes | **No** |
| Credit, card tier, family features | Yes, by tier | **No** |
| Time lever | n/a | **Tenure rebate**, section 5.2 |
| Exit | Buyback at the fix, no fee | Buyback at the fix, no fee. Unvested rebate forfeited |
| **The gold** | **Identical** | **Identical** |

Spot needs no mandate, so it never touches the failure-fee problem at all: a single push or transfer, no standing authority, nothing to bounce.

### 4.2 Large tickets, which are the useful ones

A large spot order is the **inverse of the lumpiness problem the float exists to solve**. A USD 100,000 order funds roughly 915 grams outright, nearly a full kilobar, at a single fix with a single rail event.

| Ticket band | Handling |
|---|---|
| Small | Standard flow. Below the **AED 3,500** Travel Rule threshold |
| Above AED 3,500 (~USD 950) | Travel Rule data applies |
| Above AED 50,000 (~USD 13,600) | Above the AANI per-transaction cap. Domestic transfer or wire. Enhanced due diligence, source of funds |
| Above roughly one bar denomination | **Procure directly rather than drawing the float** |

The last row is a mechanism, not an operational note. **A single order larger than the float would breach the backing invariant and halt minting for everyone else.** Above a defined threshold the purchase is quoted as a two-step: price indication, then execution against a same-day dealer purchase. Disclose the threshold and the slightly longer settlement.

### 4.3 What spot deliberately does not get

Unchanged from `_draft_sip-spot-and-ics.md` §2 and correct: **restrict benefits, not supply.** No ICS, no entry-fee discount, no credit ratio, no card tier, no family features. Capping spot supply would look like a rationed offering, which is the securities shape the design is built to avoid. Denying benefits is a loyalty programme, which is regulatorily unremarkable everywhere.

The one change is lever 3. The decaying redemption fee is prohibited, so the time lever becomes a tenure rebate. Next section.

---

## 5. The exit: how cash gets back to the investor

### 5.1 What VARA actually says, verified at source

**Rule III.E, Annex 2 (Asset-Referenced Virtual Assets Issuance Rules), Virtual Asset Issuance Rulebook.** Quoted from `rulebooks.vara.ae/rulebook/e-redemptions`:

| Rule | Text | Consequence for Aurumix |
|---|---|---|
| Opening condition | "**To the extent** an ARVA provides owners and/or holders with a right of redemption..." | Redemption is **optional**. All of III.E is conditional on granting it |
| III.E.1 | Holders may redeem "for an equal value denominated in a. AED; and b. other forms as may be determined by the VASP and disclosed in the Whitepaper" | **AED payout must always be offered.** USD only if disclosed in the whitepaper. The product is USD-priced, so **disclose both** |
| III.E.2 | Redemption "against the VASP; or otherwise in respect of the Reserve Assets in the event that the VASP is unable to process" | Under Option A there are **no Reserve Assets**. The fallback is stronger than the rule contemplates: the holder already owns the metal |
| III.E.3 | Requests "processed and completed within a reasonable period" | **The pressure valve.** A disclosed, size-tiered settlement window is permitted. A fee is not |
| III.E.4 | "**shall process and complete redemption requests without charging any fees**" | 🔴 **The decaying spot redemption fee is prohibited** |
| III.E.5 | Clear and detailed policies and procedures required | A written redemption policy is a licence deliverable |

**Verified separately, and it confirms decision 23 against rule text rather than guidance.** Rule III.C (Reserve Assets) opens: *"VASPs Licensed to issue ARVAs **which purport to maintain a stable value** in respect of any Referenced Asset, shall hold and maintain sufficient and acceptable Reserve Assets..."* The Reserve Asset regime attaches to the **stable-value branch only.** Choosing direct ownership removes it, exactly as decision 23 assumed.

**Could Aurumix simply not grant a redemption right?** Mechanically yes, and then none of III.E applies. Three reasons not to:

1. The client's own §3.2 promises a Buyback Floor. **A published, formulaic commitment to buy back at a defined price will be read as a redemption right in substance**, whatever it is labelled. Regulators read substance.
2. No redemption right means no price floor, which is precisely the Midas XGZ case in the landscape: a members-only primary market and a redemption floor far above the average holding, trading at a **discount**. Restricting the exit does not create a premium, it removes the floor.
3. It is worse for the customer, and the whole Option A argument is that the customer's position is genuinely strong.

> **Recommendation: grant the redemption right deliberately, accept III.E.4, and recover everything at the door.**

⚠ **One phrase to put to counsel.** III.E.1 says "equal value." The safe reading is the full prevailing value of the underlying grams with no haircut. An arguable reading is realisable value, that is, the dealer's bid. **The difference is the entire two-way spread and it decides who absorbs it on every exit.** Design for the safe reading; ask the question.

### 5.2 The decaying redemption fee is dead. Here is the replacement

**What it was doing:** discouraging short-term spot flipping, by charging an exit fee that decayed to zero over 6 to 12 months.

**Why it cannot survive:** III.E.4.

**The replacement: a tenure rebate.** Charge the full fee at entry, where nothing prohibits it, and pay part of it back in grams for holding.

| | Old design (prohibited) | New design |
|---|---|---|
| Spot entry fee | 4 to 5% | **Flat, top of range** |
| Exit before 12 months | Fee decaying from ~1.5% to zero | **No fee.** Unvested rebate forfeited |
| Exit after 12 months | No fee | **No fee, and the rebate is paid in grams** |
| Where the money is charged | On the way out | **On the way in** |
| Legal status | Prohibited by III.E.4 | Permitted. A fee rebate, not a distribution |

Economically these are close to identical for the investor and identical in direction for Aurumix. **Legally they are opposites.** And the new version is better product: the investor watches their gram count rise for holding, rather than watching a penalty shrink. Same emotional mechanism Gold Rewards is built on.

It must satisfy the same four rules as Gold Rewards (decision 6), and it does: **funded from the fee line and never from profit; capped at the fee that customer actually paid; earned by tenure, which is behaviour, not by amount; and never described as yield, interest or return.**

**Lot accounting, which this now requires.** The rebate vests per purchase lot at 12 months. Lots consume **FIFO** on a partial exit. Exiting a lot before it vests forfeits that lot's rebate. This closes the second deferred item in the handoff: grams are fungible for settlement, and FIFO within the spot lot pool decides only which rebate entitlement is forfeited.

⚠ **Tenure attaches to the account, not to the gram.** Grams received by transfer start a fresh clock in the receiving account. Otherwise the rebate is farmable by circulating tokens between accounts.

### 5.3 The exit lifecycle, step by step

| # | Stage | Actor | Timing | Detail |
|---|---|---|---|---|
| 1 | **Request** | Investor | T | Grams or currency amount. Full or partial |
| 2 | **Checks** | Aurumix | minutes | Sanctions re-screen, bank account name-match, no unreleased credit pledge on the grams |
| 3 | **Price struck** | LBMA | **next fix after the request** | Same convention as entry. Neither side can select the fix |
| 4 | **Tokens burned** | Contract | same day | AURX burned from the registered address. Registry updated |
| 5 | **Title returns** | Register | same day | Grams move from the investor's sub-account back to the float position |
| 6 | **Payout** | Aurumix | **T+1, target** | From the Client Account to the investor's **own name-matched bank account**. AED always available, USD if disclosed |
| 7 | **Rebate settled** | Aurumix | same day | Vested tenure rebate credited in grams before the burn. Unvested forfeited |
| 8 | **Float rebalanced** | Treasury | threshold-triggered | **Only if the float exceeds its upper band** does the treasury sell metal to the dealer |

**Stage 8 is the point of the whole design.** An exit does not sell gold. It returns grams to the float. The next buyer consumes them. The treasury only touches the physical market when the float breaches a band.

### 5.4 Why zero-fee redemption is affordable

The obvious objection to III.E.4 is that Aurumix must pay the dealer's bid-ask spread on every exit and cannot charge for it. **That objection assumes gross exits drive physical sales. They do not.**

| Book state | Inflow | Gross exits | Net flow | Physical gold sold |
|---|---|---|---|---|
| Growing | 8% of AUM | 3% of AUM | +5% | **None.** Float absorbs |
| Flat | 4% | 4% | 0% | **None.** Float absorbs |
| Shrinking | 2% | 6% | −4% | Yes, on the 4% net only |
| Run | 1% | 25% | −24% | Yes, in size, at bid, into a falling market |

**In the first two rows, which is where a growing product lives, the zero-fee rule costs nothing.** The cost of the redemption promise is the dealer spread on **net** outflow, not on gross exits, and it is bounded by the float's capacity to warehouse the difference.

Make this argument to the client in exactly this form. It converts an apparently expensive regulatory constraint into an argument for the float they were already being asked to fund.

### 5.5 The stress case, which is where it does cost

Row four is real and needs a disclosed mechanism. **III.E.3's "reasonable period" is the valve, and it is the only valve, because III.E.4 removes the price valve entirely.**

| Redemption size | Settlement target | Basis |
|---|---|---|
| Small | Next business day | Absorbed by the float |
| Medium | Up to 3 business days | May require a dealer sale |
| Large | Up to 5 business days | Physical sale, possibly staged |

All three must be **disclosed in the whitepaper**, per III.E.1's disclosure hook and III.E.5's policy requirement. A tiered window is defensible as "reasonable"; an undisclosed delay is not. **Thresholds are deliberately not set here: they depend on the float size, which depends on the dealer.**

Three further protections, none of them a fee:

1. **The holder already owns the metal.** Under Option A, if Aurumix cannot pay cash, the investor's claim is not on Aurumix's balance sheet, it is on gold they already own, held by a vehicle outside Aurumix's estate. Materially better than III.E.2.b contemplates, and **the strongest single argument for route 2.**
2. **The wind-down plan** (Company Rulebook Part VII.A) is the backstop, and Rule 1.k requires that selling client assets is explicitly excluded from completing it. Direct ownership makes that rule satisfiable rather than aspirational.
3. **A disclosed suspension right**, limited to market closure, custodian failure or force majeure, never to liquidity management. Anything broader reads as a discretionary gate on the customer's own property.

---

## 6. Transfers and the secondary market

Short, but it is a real state and no draft covers it.

Under III.B.1.a, a transfer of AURX must transfer the right of ownership in the gold. So:

- **Both parties must be registered holders.** The permissioned token enforces this at the contract level and the register records the title move. An unregistered recipient cannot receive AURX at all.
- **A transfer is not a redemption**, so a transfer fee is permitted. Keep it small or zero; the point is to move the metal correctly, not to earn.
- **ICS does not transfer.** Tenure and continuity are account attributes.
- **Received grams start a fresh tenure clock.**
- **Pledged grams cannot transfer** until the charge is released.
- **Any venue listing AURX must be an approved participant with registered customers.** An open DEX listing is incompatible with Option A. **The client should hear this before he builds a listing plan around it.**

---

## 7. Custody: a conflict this document creates and does not solve

Stating it rather than hiding it, per the working convention.

Decision 5 settled that the custody fee is recovered **at entry and at exit**, never off the metal, because a monthly cash bill dies on persistency: about 38% of the insurance comparable are still contributing at month 61, so the bill outlives the touchpoint that collects it.

**Rule III.E.4 has just deleted the exit half.** A deduction from redemption proceeds is a fee on redemption.

| Option | Mechanism | Problem |
|---|---|---|
| **A. Front-load entirely** | Recover expected lifetime custody inside the entry fee | The 10-year holder is subsidised by the 1-year holder, and the entry fee is already at the top of its range |
| **B. Periodic cash bill** | Charge alongside the SIP | The original design, killed on persistency. Also another rail event |
| **C. Deduct in grams, burn the tokens** | Move X grams to Aurumix, burn X AURX | **Mechanically sound**: the invariant holds because both sides fall. But it breaks *"you can never lose your gold"*, and under Option A it is a sale of the customer's own metal needing express contractual authority |
| **D. No ongoing custody charge at all** | Absorb it | Only viable if the real cost is far below the client's stated 0.8 to 1% |

> ⚠ **The question underneath all four, and it has never been asked: is 0.8 to 1% a cost or a revenue line?** Institutional allocated storage does not cost that. If the true vault cost is 0.15% to 0.40%, **option D becomes viable and turns into a marketing advantage** over PAXG (which dilutes at 0.02%/yr) and Comtech. If it is a revenue line, say so, and then it is a fee that III.E.4 constrains as to where and when it can be collected. **Get the vault quote; it sits in the same conversation as the dealer.**

⚠ Note also that the allocation draft's claim that "deduction in grams breaks the peg" is **too strong**. Deducting grams *and burning the matching tokens* preserves `float + allocated ≥ tokens outstanding` exactly. What rules out option C is the ownership authority and the governing promise, **not the invariant**. Correct the reasoning even though the conclusion stands.

---

## 8. Reconciliation: what to change in the existing drafts

- [ ] `_draft_sip-spot-and-ics.md`: **lever 3 changes** from a decaying redemption fee to a tenure rebate. Update the comparison table in §1 and the three-levers list in §2.
- [ ] `_draft_sip-spot-and-ics.md`: add **declared pause**, **dormancy** and **regulatory pause** as defined states.
- [ ] `_draft_sip-spot-and-ics.md`: add the **failure versus non-payment** distinction to §5, and the no-auto-re-presentment rule.
- [ ] `_draft_sip-spot-and-ics.md`: add the **one-rule pricing convention** (the price is always the next fix nobody has seen yet), covering contribution, arrears and exit together.
- [ ] `_draft_entities-licensing-and-payments.md`: add the **client money split rule** (section 2.2), which decision 29 flagged as undesigned.
- [ ] `_draft_entities-licensing-and-payments.md`: add the **III.B.1.c reconciliation requirement** and its three consequences, including the DEX-listing constraint.
- [ ] `_draft_allocation-and-float.md`: correct the "deduction in grams breaks the peg" reasoning (section 7).
- [ ] `_explainer_how-we-take-money.md`: the **returning-NRI gap in §7 is now answered** as the regulatory pause.
- [ ] Client's document §6.3: "6 consecutive events at the same monthly commitment" resolves to **six periods at or above the declared minimum**.
- [ ] Client's document §2.2: "custody fee deducted from Gold Receipt in grams" collides with fixed weight, with Option A ownership, and with the promise that the gram count only rises. Section 7.

---

## 9. Open items, by owner

**[COUNSEL] Three, all cheap, all decide a mechanism.**
1. Does "equal value" in Rule III.E.1 mean full prevailing value, or realisable value net of the dealer's bid? **It decides who absorbs the two-way spread on every exit.**
2. Is a published, formulaic buyback commitment a "right of redemption" for the purposes of III.E, even if the whitepaper does not use the word? **Assume yes; confirm.**
3. Under Option A, can a periodic custody charge be satisfied by deducting the customer's own grams under express contractual authority, given the customer holds legal title? Section 7, option C.

**[DEALER] Unchanged and still blocking.**
- Two-way dealer, float carry, real premiums and spreads, Tradeflow terms.
- 🆕 **The vault's real annual custody cost per gram at Aurumix's scale.** It decides whether option D in section 7 exists.

**[CLIENT]**
- Is 0.8 to 1% custody a cost or a revenue line?
- Accept that an **open DEX listing is incompatible with direct ownership**, before a listing plan is built around it.

**[US]**
- When AANI **electronic direct debit** goes live. Announced, not shipped, and it is the target state for the collection mechanism.
- Settlement-window thresholds in section 5.5, which wait on the float size.

**Parked, not dropped:** minimum ticket size, collection economics, the card exclusion and the tariff research all sit in `_parked_collection-economics-and-minimum-ticket.md`.

---

## 10. Sources and confidence

| Claim | Source | Confidence |
|---|---|---|
| Rule III.E.1 to III.E.5 text, including no fees on redemption | `rulebooks.vara.ae/rulebook/e-redemptions`, fetched 2026-08-06 | **High.** Primary source, verbatim |
| Rule III.B.1 Direct Right of Ownership | `rulebooks.vara.ae/rulebook/b-direct-right-ownership` | **High.** Primary source |
| Reserve Asset regime applies only to stable-value ARVAs | `rulebooks.vara.ae/rulebook/c-reserve-assets`, opening words | **High.** Primary source. Confirms decision 23 against rule text |
| Redemption is optional for an ARVA | VARA Guidance on the Issuance Rulebook, plus the "to the extent" opening of III.E | **High** |
| ENBD retail direct debit return fee AED 105 | Emirates NBD Personal Banking Schedule of Charges | **Medium-High.** Returned by two independent passes |
| AANI live, 12.5M users, 74 LFIs, ~85% of banks, AED 50,000 per-transaction cap, Request to Pay live, electronic direct debit announced not live | CBUAE press material April 2026; Al Etihad Payments | **High** on status and limits |
| Recurring card failure 10 to 15%; direct debit 2 to 3% | Recurly, GoCardless, Spreedly | **Medium** |
| Involuntary churn 20 to 40% of total churn | ProfitWell; Forrester at 34% | **Medium** |
| Indian AMCs purge SIPs after ~3 months of non-payment | AMFI April 2026 anomaly, reported at 296% stoppage ratio | **Medium** |
| AMFI SIP stoppage ratio 75.63% in FY25 | AMFI monthly data via Economic Times | **Medium-High** |
