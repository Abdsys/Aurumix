# SIP, Spot and the ICS Score

> **Status: decision draft, 2026-07-29.** Settles the structure of the ICS block (B4) and the SIP/spot split. Component weights, tier thresholds and decay rates are NOT set here: that is the next step. To be expanded to full MD depth and folded into the Mechanism Design document.

## The decision in one line

**Amount decides the size of your holding. Behaviour decides your rate on it.**

Every benefit in the product is a percentage. A larger contributor automatically receives more gold, a larger absolute credit line and a larger absolute rebate, because all three are percentages of a larger base. What nobody can do is buy a better percentage. The percentage is earned by contributing consistently, and it is earned the same way whether the contribution is 20 USD or 2,000 USD.

## 1. Separating the SIP investor from the spot buyer

**The problem.** The two investor types used to be separated by supply. SIP contributors received a guaranteed allocation and spot buyers competed for a rationed remainder gated on score. Once minting became continuous at NAV, that separation disappeared with the queue it depended on, leaving two named customer types with no defined difference between them.

Treating them as two classes also creates a deadlock at the front door. Spot is described as the entry point for new investors, and spot earns no score, and spot access is gated on score. A new investor cannot satisfy a gate that only prior participation opens, so there is no defined route in for someone arriving on day one.

**The solution.** SIP and spot become two transaction types on a single account rather than two classes of investor. One account, one KYC, one Gold Receipt, one score attached to the account. The holder may do either at any time.

| | SIP contribution | Spot purchase |
|---|---|---|
| What it is | A payment against a declared monthly amount | A one-off purchase, no declaration |
| Earns ICS | **Yes** | **No** |
| Entry fee | Base rate, discounted by ICS tier | Flat, top of range, no discount |
| Exit | Buyback at NAV, no exit penalty | Buyback less a fee decaying over 6 to 12 months |
| Credit, card, family features | Yes, by tier | No |
| **The gold itself** | **Identical** | **Identical** |

**Why.** Classes create the bootstrapping deadlock; transaction types dissolve it, because everyone opens the same account and then chooses what to do with it. It also restores three things the class model blocked: an existing contributor can add a lump sum without changing category, a spot buyer can convert to contributing at any time, which is the growth funnel, and large tickets are discouraged by earning nothing rather than by being capped out, which removes the last remaining argument for a supply cap. A large spot order is in fact useful to the treasury, since it funds a whole bar outright and is the inverse of the lumpiness problem the float exists to solve.

The gold must never differ between the two. Same token, same fix, same backing, same receipt. All differentiation sits in the fees and services wrapped around the metal, because the moment the metal itself differs by channel there are two economic classes of one instrument, which is the securities shape that deleting the scarcity layer was meant to avoid.

## 2. What may legitimately be differentiated

**The problem.** With supply rationing gone, the benefits attached to consistent contribution need a new basis. That basis has to reward behaviour visibly enough to drive it, without creating anything a regulator reads as a return.

**The solution.** Three levers, and only three.

1. **Price.** The entry fee falls with ICS tier.
2. **Credit.** The loan-to-value ratio rises with ICS tier. Spot-only accounts receive none.
3. **Time.** Spot grams carry a decaying redemption fee. SIP grams do not.

**Why.** All three are loyalty-programme shaped rather than offering shaped. None of them rations supply, all three are levers Aurumix genuinely controls rather than ones the market sets, and none of them promises a return of any kind. Restricting benefits is a loyalty programme; restricting supply is a rationed offering. That is the entire safe surface, and anything outside it should be treated as a new classification risk.

## 3. The commitment period

**The problem.** An investor selects a commitment of six months to twenty-five years, and missing a payment carries no financial penalty, only a loss of score. A commitment that costs nothing to break is free to make. Every investor should therefore select the longest available term, which makes the choice carry no information about the investor.

The benefits the commitment was supposed to buy have also emptied out. The credit facility activates at month six whether the commitment is six months or twenty-five years, so it never varied by term at all. Buyback eligibility gated on term expiry would prevent a twenty-five year investor from exiting for twenty-five years, on a token that is simultaneously intended to trade. The dividend multiplier scaled a payment that is now a rebate capped at the fees that customer generated, so scaling it changes almost nothing. What remains is a term that costs nothing, buys nothing, and predicts nothing.

**The solution.** Delete the commitment as a contract. Keep it as a declared savings goal.

The investor declares a monthly amount, a contribution date, and optionally a target expressed as a duration or a gram figure. The target drives the debit schedule and appears in the app as progress. It scores nothing, and it can be changed or abandoned at any time. The only tracked fact is whether a contribution arrived in a given period.

**Why.** Scoring a declaration breaks the rule the whole model runs on, which is that the score measures what the investor did rather than what they intended. It also fails as a scoring input on its own terms, because a component on which every rational investor selects the same value does not discriminate between customers and is dead weight in the formula.

Removing it costs nothing in retention, because breaking the commitment and simply not paying already carried identical consequences. It gains a great deal in acquisition. The hardest moment in a 20 USD product is asking a stranger to commit for twenty-five years, and that is where signups are lost. Indian mutual fund SIPs reached mass scale precisely because an investor can stop at any time.

What is retained from the insurance model is the discipline rather than the contract: a grace period, a step-down on a miss, revival through arrears, and a tier that climbs with time served. All of it runs on payments actually made.

**No minimum commitment survives this, including the six periods that qualify an investor for Confirmed SIP status.** That threshold is not a commitment reintroduced through the back door, and the difference is direction. A commitment is forward-looking: the investor promises six months in advance and is bound by the promise. Confirmed SIP is backward-looking: after six consecutive contributions have actually been made, the status exists. The investor never agrees to anything.

The practical consequence is that an investor who stops at month three has broken nothing and forfeited nothing. There is no lapse, no penalty and no arrears owed. They simply do not hold a status they had not yet earned. This is the same shape as the cumulative bonus in health insurance, where the policyholder does not commit to being claim-free for a year, but the bonus appears at renewal if they were.

Six periods is retained as the threshold. It is long enough for the status to mean something, short enough that a new investor can see it from the day they join, and it is already the client's figure.

⚠ **Terminology rule.** Never write "six month commitment" anywhere in the product, the documentation or the interface. Write "six consecutive contributions." The first phrasing reintroduces the contract the design has just removed, and an investor who believes they are bound will behave as though a penalty exists.

## 4. What the score measures

**The problem.** The score currently includes the value of the investor's holding, and that same value is then applied again as the multiplier on the score itself, so capital is counted twice. More seriously, if the score rises with the amount invested then the entry fee, the credit ratio and the rebate all improve with the amount invested. A benefit that scales with capital contributed is a return proportional to investment, which is the defining feature of a security and the same defect that forces the dividend to be replaced.

**The solution.** Remove the value of the holding from the score. Everything that remains measures behaviour.

| Component | What it measures | Rank |
|---|---|---|
| **Continuity** | Current unbroken streak of contributions | Primary |
| **Tenure** | Total periods actually contributed | Primary |
| Referrals | Investors onboarded | Supplementary, capped |
| Family portfolios | Active sub-accounts making their own contributions | Supplementary, capped |
| Masterclass | Community engagement | Supplementary, capped |

Continuity and tenure look like one component and must stay as two. Continuity is a streak and tenure is accumulated time, so without tenure an investor could contribute flawlessly for eight months and sit at the top tier beside a five year customer. They also fail in opposite directions: a long-standing customer who has become unreliable and a flawless newcomer should not score the same, in either direction.

**Why.** Amount is already rewarded, automatically and proportionally, because every benefit is a percentage of a base that the amount determines. A larger contributor receives more gold, more credit and a larger rebate without the score doing anything. Rewarding amount a second time inside the score converts a proportional benefit into a preferential rate, and a preferential rate bought with capital is the thing that cannot survive classification.

This produces a single binding constraint on the formula, and it is testable:

> **An investor contributing 20 USD per month who never misses a payment must be able to reach the top tier.**

If the formula cannot deliver that, the result is not a loyalty programme. It is a preference class for larger investors, which is the structure the design is specifically trying to avoid.

## 5. What happens when someone misses a payment

**The problem.** A missed payment needs a consequence severe enough to drive consistency and mild enough that a single bad month does not end the relationship. With no consequence, the score means nothing. With a permanent consequence, an investor who misses once has no reason to return, which is worse for retention than a financial penalty would have been.

**The solution.** Five cases cover everything that can happen in a period.

| Case | Consequence |
|---|---|
| **Pays on time** | Gold allocated. ICS accrues. |
| **Pays less, but at or above the declared minimum** | Less gold, proportionally. **ICS unaffected.** |
| **Pays late, within 15 days of the contribution date** | Gold allocated at the fix on the day funds clear. **ICS unaffected.** |
| **Does not pay within grace** | **ICS steps down. It does not reset.** Streak breaks, Confirmed SIP suspends, the credit ladder stops climbing. **The gold is untouched.** |
| **Makes a spot purchase** | Gold allocated. **No ICS.** Decaying redemption fee attaches to those grams. |

**Settled here, because none of it depends on how the score is computed:**

- **Grace period: 15 days**, running from the investor's own contribution date.
- **Confirmed SIP: 6 consecutive contributions at or above the declared minimum.** Defined on periods rather than on equal amounts, since the monthly amount is variable by design.
- **Decay is a step-down, never a reset.**
- **Rebuild is slower than decay.**
- **Revival window: 12 months** to make good a missed period through arrears.
- **Credit is a ladder from month 6**, rising with tenure and tier, rather than a switch that flips once.

**Deferred to the ICS formula design, because each needs the tier structure to exist first:** the size of the step-down, the rate at which the score rebuilds, and how much of the score a revival restores. The working default on the third is full restoration, as set out in the next section.

**Why.** Each rule above is taken from a precedent the target customer already understands, and each prevents a specific failure.

The 15 day grace is the IRDAI standard for monthly-mode premiums, where cover continues in full and no late fee applies. It prevents an administrative failure, a bounced debit or a forgotten date, from being scored as a behavioural one.

The step-down rather than the reset comes from the cumulative bonus in health insurance, where a claim reduces the accumulated bonus by one level and the base cover is preserved. A reset punishes several good years for one bad month and leaves the investor with nothing further to protect, which is precisely the moment they leave.

Making rebuild slower than decay is the client's own stated intent, that loss should be faster than recovery, expressed as a rule rather than a sentiment.

Credit is a ladder rather than a switch because a switch stops working the moment it is thrown. Under a single activation point an investor at month seven and an investor at month sixty hold identical borrowing power, so the facility does no retention work at all after the month it arrives. A ladder makes every additional month of contributions buy something, which means leaving always costs the climb.

Above all of it sits the governing promise, and it is worth stating in exactly these words:

> **You can lose your status. You can never lose your gold.**

Every consequence in the model falls on tier, fee or credit ratio. The gram count only ever rises. This is the preserved base principle from the cumulative bonus applied to a fixed-weight token, and it is the honest version of the retention story the product is reaching for.

## 6. Pricing a revival

**The problem.** If arrears purchase gold at the price of the period being made good, revival becomes a free look-back option. Every investor revives after the gold price has risen and none after it has fallen, and Aurumix buys at the current price to deliver at a historic one. The exposure runs in one direction only and cannot be hedged, because the investor chooses when to exercise it.

**The solution.** A revival payment buys gold at the fix on the day the arrears clear, never at the fix of the period being made good.

**Why.** Priced this way an arrears payment is economically identical to a contribution made today, so no option value exists. What the payment buys is the score position, not the price. Revival restores the streak, the tier and Confirmed SIP status as though the period had been paid, and the investor pays the current market price for the metal like everyone else.

Because there is no adverse selection to underwrite against, revival costs Aurumix almost nothing to offer. That is what makes a twelve month window affordable here, where a life insurer needs three years, arrears with interest and fresh medical underwriting to achieve the same thing.

> **The number that should govern the calibration.** Indian life insurance retains roughly 79% of policies at the 13th month and roughly 38% at the 61st month. Six in ten are gone within five years, and the steepest fall is in year two. Aurumix has the same year-one economics, since the entry-fee build-up leaves roughly 1% net margin on a contribution, so a customer is barely profitable in their first year and only becomes valuable by persisting. **Churn is what kills this model, not fee levels.** The ICS formula is the primary instrument against churn, which is why it is the hub block and why every other block calibrates after it.
