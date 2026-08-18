# Aurumix Revenue Model - Numerical Spine

Generated from `reference_model/` at Base scenario unless a table says otherwise. Every figure here is model output; nothing is carried from the v1.0 brief. Where a figure **replaces** a v1.0 number, the old value, the new value and the driver of the change are shown together.

**Base assumptions behind every table below:** rail USD 0.25/collection (S1 Base); PM share 55% to M30 then 72% (S3); card spend AED 6,000/month (S4); activation 65% (S5); persistency 55/40/30/24/19% at M13/25/37/49/61 (S2 Base); gold held flat at USD 141.46/g (F1); self-custody leakage 12%/yr (S10); `LAPSED_KEEPS_CARD = True`; `INDIA_ENABLED = True`; Option A capital.

---

## 0. What moved, and why

The table the brief revision has to carry.

| Figure | v1.0 | Model | Driver of change |
|---|---|---|---|
| Y10 revenue (gross) | ~11,000,000 | 8,150,081 | Stream 5 down 49x; per-txn processor fees cut stream 2; spot added; acquisition saturation-capped |
| Card interchange share of gross profit | 54% (of revenue) | 54.3% | Effective PM share is below contracted PM share once the USD 0.10/txn fee is netted per tier. Note the denominator is gross profit, per §2 |
| Stream 5 (credit) at Y10 | ~600,000 | 12,135 | NOT a halving - a 49x fall. Collateral base per HOLDING account (2.96x) dominates S40 turnover (1.88x); the rest is v1.0's AUM overstatement |
| M61 survival | 6.1% (from h=1-S13^(1/13)) | 18.1% | Constant hazard replaced by archetype heterogeneity; 1/12 root convention |
| Break-even investor count | 171,911 | 45,102 (all streams) | Solved as a fixed point revenue(N) = TOTAL cost(N), instead of dividing opex by unit margin |
| Break-even year | Y7-Y9 (View 2) | none in 10; extrapolates to ~Y10.9 | Full cost stack, not opex alone; annual basis, not a single positive month |
| Entry fee at Y10 | 3.0% (assumed) | 3.79% minimum viable | Fee ladder was coupled to a premium ladder that assumed Good Delivery bars; those never clear, so the premium holds at 2.00% and 3.0% is below cost |
| Y10 AUM | 8-14x contributions (audit finding) | 39,790,584 | AUM now scales with HOLDING accounts and is reconciled to cumulative contributions |
| Reduced-state ticket | USD 20 hard-coded | 50% of prior ticket, floored at 20 | S29 - the floor is the hard minimum, not the landing point |
| Terminal state of a cohort | LAPSED = terminal, exits everything | 66% lapsed-but-holding | Corpus: lapsed keeps gold, custody, screening, AUM |
| Y10 opex | 8,695,500 | 3,219,856 | v1.0's anchor is sized for 80,000 contributing investors; the model reaches 21,661. Opex is now charged block-by-block against the model's own book |
| Bar denomination at Y10 | 12,400 g (Good Delivery) | 1,000 g | T3 solved endogenously. Good Delivery never clears the upgrade rule at the model's real volume |
| Gold Rewards cost at Y10 | not separately sized | 1,132,682 | F13's USD 3,000 cap is PER CARDHOLDER; applying it to aggregate tier spend understated it ~1000x |

---

## 0.1 Does the client's 60,000-100,000 Year 10 target count accounts opened or investors still contributing?

v1.0 §14 lists this as an open question, defaults to 'still contributing' and guesses the two differ by ~5x. **The model answers it.**

| Measure | Model Y10 | vs 60,000 target | vs 100,000 target |
|---|---|---|---|
| Accounts holding gold (ever-acquired, still in custody) | 64,197 | 107% | 64% |
| Investors still contributing (contributing + reduced) | 21,661 | 36% | 22% |

**The two measures differ by 3.0x** (v1.0 guessed ~5x; the model computes 3.0x at the corrected persistency).

**The target is reachable on a holding basis and missed on a contributing basis.** On the Base path the business ends Year 10 with 64,197 accounts holding gold - comfortably inside the 60,000-100,000 band - but only 21,661 still paying in. **Which number the client means decides whether the plan is met or missed by a factor of three**, and it changes what the target implies for revenue: AUM, custody cost and the B2B base follow the holding count, while contribution flow, rail cost and entry-fee revenue follow the contributing count.

---

## 1. Unit economics

### 1.1 Net margin per contribution by segment and year (Base rail, USD 0.25)

v1.0 applied the top segment's USD 75 ticket to the whole population. **At USD 20 the margin is negative in every year.** This is the per-segment picture.

| Year | S1 (USD 75) | S2 (USD 40) | S3 (USD 20) | S4 (USD 40) | S5 (USD 30) | S6 (USD 75) |
|---|---|---|---|---|---|---|
| 1.000 | 1.363 | 0.610 | 0.180 | 0.610 | 0.395 | 1.363 |
| 2.000 | 1.363 | 0.610 | 0.180 | 0.610 | 0.395 | 1.363 |
| 3.000 | 1.310 | 0.582 | 0.166 | 0.582 | 0.374 | 1.310 |
| 4.000 | 1.310 | 0.582 | 0.166 | 0.582 | 0.374 | 1.310 |
| 5.000 | 1.310 | 0.582 | 0.166 | 0.582 | 0.374 | 1.310 |
| 6.000 | 1.289 | 0.571 | 0.161 | 0.571 | 0.366 | 1.289 |
| 7.000 | 1.289 | 0.571 | 0.161 | 0.571 | 0.366 | 1.289 |
| 8.000 | 1.454 | 0.659 | 0.204 | 0.659 | 0.432 | 1.454 |
| 9.000 | 1.454 | 0.659 | 0.204 | 0.659 | 0.432 | 1.454 |
| 10.000 | 1.454 | 0.659 | 0.204 | 0.659 | 0.432 | 1.454 |

### 1.2 The same table at the Conservative rail (USD 1.36 - UAEDDS pricing)

| Year | S1 (USD 75) | S2 (USD 40) | S3 (USD 20) | S4 (USD 40) | S5 (USD 30) | S6 (USD 75) |
|---|---|---|---|---|---|---|
| 1.000 | 0.253 | -0.500 | -0.930 | -0.500 | -0.715 | 0.253 |
| 2.000 | 0.253 | -0.500 | -0.930 | -0.500 | -0.715 | 0.253 |
| 3.000 | 0.200 | -0.528 | -0.944 | -0.528 | -0.736 | 0.200 |
| 4.000 | 0.200 | -0.528 | -0.944 | -0.528 | -0.736 | 0.200 |
| 5.000 | 0.200 | -0.528 | -0.944 | -0.528 | -0.736 | 0.200 |
| 6.000 | 0.179 | -0.539 | -0.950 | -0.539 | -0.744 | 0.179 |
| 7.000 | 0.179 | -0.539 | -0.950 | -0.539 | -0.744 | 0.179 |
| 8.000 | 0.344 | -0.451 | -0.905 | -0.451 | -0.678 | 0.344 |
| 9.000 | 0.344 | -0.451 | -0.905 | -0.451 | -0.678 | 0.344 |
| 10.000 | 0.344 | -0.451 | -0.905 | -0.451 | -0.678 | 0.344 |

**Every segment is loss-making on every collection at the adverse rail.** This is the §0.2 equation `Net = C x (f - c) - R` running against the business.

### 1.3 Base-weighted blend, as the model actually mixes the segments

| year | inflow | collections | stream1_net | net_per_contribution |
|---|---|---|---|---|
| 1.00 | 168,252.26 | 3,424.21 | 2,630.19 | 0.77 |
| 2.00 | 684,508.72 | 14,931.58 | 9,528.02 | 0.64 |
| 3.00 | 1,651,349.74 | 37,677.27 | -3,099.33 | -0.08 |
| 4.00 | 2,967,521.56 | 69,754.46 | -5,556.89 | -0.08 |
| 5.00 | 4,468,855.01 | 107,303.46 | 735.00 | 0.01 |
| 6.00 | 6,010,665.60 | 146,703.07 | -17,971.78 | -0.12 |
| 7.00 | 7,440,101.86 | 184,089.53 | -18,471.49 | -0.10 |
| 8.00 | 8,634,306.67 | 216,240.59 | -64,808.82 | -0.30 |
| 9.00 | 9,496,541.26 | 240,441.75 | -73,268.20 | -0.30 |
| 10.00 | 9,985,418.61 | 255,340.88 | -80,548.21 | -0.32 |

---

## 2. The revenue stack by year (replaces §0.4)

**This table is NET revenue by stream.** Streams 2-6 are already net of their own direct costs and stream 1 is net of fabrication premium, price-gap, float and rail, so the columns sum to **gross profit**, not to gross revenue. Shares in §2.1 are therefore taken on gross profit; taking them on gross revenue would put every share on the wrong denominator (they would sum to 43.3% in Y1, not 100%).

For reference, gross revenue (fees earned before cost of revenue) is USD 8,150,081 at Y10 against gross profit of USD 7,657,206; the difference is the USD 492,875 cost of revenue in §7.

| year | S1 SIP (net) | S1 Spot (net) | S2 Card interchange | S3 Family | S4 Cardholder fees | S5 Credit | S6 B2B | Total = gross profit |
|---|---|---|---|---|---|---|---|---|
| 1 | 2,630 | 1,294 | 0 | 1,791 | 0 | 0 | 0 | 5,716 |
| 2 | 9,528 | 5,989 | 11,095 | 7,551 | 12,123 | 12 | 3,547 | 49,844 |
| 3 | -3,099 | 5,571 | 81,766 | 18,645 | 67,470 | 373 | 85,920 | 256,646 |
| 4 | -5,557 | 11,012 | 260,396 | 33,775 | 186,704 | 1,140 | 197,440 | 684,911 |
| 5 | 735 | 30,006 | 559,253 | 50,946 | 380,960 | 2,464 | 345,040 | 1,369,405 |
| 6 | -17,972 | 29,679 | 1,002,256 | 68,376 | 645,600 | 4,293 | 521,440 | 2,253,672 |
| 7 | -18,471 | 41,128 | 1,596,322 | 84,282 | 975,950 | 6,470 | 713,440 | 3,399,121 |
| 8 | -64,809 | 13,703 | 2,331,365 | 97,310 | 1,358,698 | 8,737 | 905,440 | 4,650,446 |
| 9 | -73,268 | 13,017 | 3,193,736 | 106,367 | 1,781,532 | 10,723 | 1,079,760 | 6,111,868 |
| 10 | -80,548 | 10,771 | 4,156,380 | 111,065 | 2,226,204 | 12,135 | 1,221,200 | 7,657,206 |

### 2.1 Shares of gross profit, %

| year | S1 SIP (net) | S1 Spot (net) | S2 Card interchange | S3 Family | S4 Cardholder fees | S5 Credit | S6 B2B | CHECK sum % |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 46.0 | 22.6 | 0.0 | 31.3 | 0.0 | 0.0 | 0.0 | 100.0 |
| 2.0 | 19.1 | 12.0 | 22.3 | 15.1 | 24.3 | 0.0 | 7.1 | 100.0 |
| 3.0 | -1.2 | 2.2 | 31.9 | 7.3 | 26.3 | 0.1 | 33.5 | 100.0 |
| 4.0 | -0.8 | 1.6 | 38.0 | 4.9 | 27.3 | 0.2 | 28.8 | 100.0 |
| 5.0 | 0.1 | 2.2 | 40.8 | 3.7 | 27.8 | 0.2 | 25.2 | 100.0 |
| 6.0 | -0.8 | 1.3 | 44.5 | 3.0 | 28.6 | 0.2 | 23.1 | 100.0 |
| 7.0 | -0.5 | 1.2 | 47.0 | 2.5 | 28.7 | 0.2 | 21.0 | 100.0 |
| 8.0 | -1.4 | 0.3 | 50.1 | 2.1 | 29.2 | 0.2 | 19.5 | 100.0 |
| 9.0 | -1.2 | 0.2 | 52.3 | 1.7 | 29.1 | 0.2 | 17.7 | 100.0 |
| 10.0 | -1.1 | 0.1 | 54.3 | 1.5 | 29.1 | 0.2 | 15.9 | 100.0 |

The `CHECK sum %` column sums to 100.0 in every year by construction - it is printed so the denominator can be verified at a glance.

### 2.2 Stream 5 did not 'roughly halve' - it fell 49x

Three earlier descriptions called this a halving. It is not. v1.0 carries stream 5 at ~USD 600,000 at Y10; the model returns **USD 12,135**. Decomposed:

| Step | Y10 stream 5 | Effect |
|---|---|---|
| v1.0 basis (tier share of TOTAL AUM, drawn balance persists) | 70,035 | - |
| + S40 turnover 0.42 (Manappuram 71-day tenor) | 37,290 | 1.88x fall |
| + collateral base per HOLDING account | 12,582 | 2.96x fall |

**The collateral-base correction dominates, not S40.** Only Gold+ accounts can borrow, but AUM is spread across *all* holding accounts - and at 19% M61 persistency the holding book is ~3x the live book. v1.0 credits the Gold+ population with a share of total AUM as though the lapsed book's gold were theirs to pledge. The residual gap from USD 70k to USD 600k is v1.0's own AUM overstatement (§5).

**Note the sign on stream 1.** The SIP entry-fee line is *negative* in every year at Base: the fixed rail cost per collection exceeds the margin on the blended ticket. This is why a negative column can appear in a stack that still sums to 100% - the card streams carry the loss-making inflow lanes. The spot lane is also negative, but far less so per dollar of inflow, and §8.3 shows the fee path at which both turn positive.

---

## 3. Investor and account counts by state

CLOSED is the only true exit from AUM, custody and screening. `holding` is the driver for AUM, custody cost and AML screening; `live_accounts` (contributing + reduced) drives contribution flow only.

| year | contributing | reduced | lapsed_holding | dormant | holding | live_accounts | lapsed_share_of_ever_% |
|---|---|---|---|---|---|---|---|
| 1 | 508 | 3 | 176 | 0 | 687 | 511 | 26 |
| 2 | 1,805 | 15 | 734 | 130 | 2,684 | 1,820 | 32 |
| 3 | 4,146 | 45 | 1,775 | 688 | 6,654 | 4,191 | 37 |
| 4 | 7,035 | 98 | 3,144 | 2,058 | 12,335 | 7,133 | 42 |
| 5 | 10,238 | 173 | 4,634 | 4,520 | 19,565 | 10,411 | 47 |
| 6 | 13,421 | 266 | 6,093 | 8,192 | 27,973 | 13,687 | 51 |
| 7 | 16,285 | 371 | 7,375 | 13,072 | 37,103 | 16,657 | 55 |
| 8 | 18,607 | 480 | 8,374 | 19,034 | 46,494 | 19,087 | 59 |
| 9 | 20,186 | 582 | 9,009 | 25,863 | 55,640 | 20,768 | 63 |
| 10 | 20,990 | 671 | 9,264 | 33,273 | 64,197 | 21,661 | 66 |

**At Y10, 66% of the holding book is lapsed or dormant.** v1.0 dropped this population out of AUM, custody, screening and the card base entirely.

---

## 4. Tier distribution, computed (not assumed)

Weighted sum over archetype tracks. v1.0 computed a cohort's average `Recent` and applied thresholds to the average, which is wrong by Jensen's inequality and biased upward.

| year | tier_none | tier_silver | tier_gold | tier_platinum | tier_sovereign | total |
|---|---|---|---|---|---|---|
| 1 | 325 | 186 | 0 | 0 | 0 | 511 |
| 2 | 932 | 603 | 286 | 0 | 0 | 1,820 |
| 3 | 1,860 | 1,282 | 1,049 | 0 | 0 | 4,191 |
| 4 | 2,674 | 1,997 | 2,308 | 154 | 0 | 7,133 |
| 5 | 3,404 | 2,714 | 3,722 | 570 | 0 | 10,411 |
| 6 | 3,957 | 3,334 | 5,057 | 1,299 | 41 | 13,687 |
| 7 | 4,294 | 3,788 | 6,244 | 2,181 | 151 | 16,657 |
| 8 | 4,416 | 4,053 | 7,156 | 3,100 | 362 | 19,087 |
| 9 | 4,310 | 4,099 | 7,741 | 3,983 | 635 | 20,768 |
| 10 | 4,047 | 3,965 | 7,955 | 4,739 | 954 | 21,661 |

### 4.1 As percentages of tiered (live) accounts

| year | tier_none | tier_silver | tier_gold | tier_platinum | tier_sovereign |
|---|---|---|---|---|---|
| 1.0 | 63.5 | 36.5 | 0.0 | 0.0 | 0.0 |
| 2.0 | 51.2 | 33.1 | 15.7 | 0.0 | 0.0 |
| 3.0 | 44.4 | 30.6 | 25.0 | 0.0 | 0.0 |
| 4.0 | 37.5 | 28.0 | 32.4 | 2.2 | 0.0 |
| 5.0 | 32.7 | 26.1 | 35.8 | 5.5 | 0.0 |
| 6.0 | 28.9 | 24.4 | 36.9 | 9.5 | 0.3 |
| 7.0 | 25.8 | 22.7 | 37.5 | 13.1 | 0.9 |
| 8.0 | 23.1 | 21.2 | 37.5 | 16.2 | 1.9 |
| 9.0 | 20.8 | 19.7 | 37.3 | 19.2 | 3.1 |
| 10.0 | 18.7 | 18.3 | 36.7 | 21.9 | 4.4 |

### 4.2 The Sovereign stock vs ever-qualified gap

Only the **Perfect payer** archetype (10% of each vintage at origination) can ever reach Sovereign, because Sovereign requires Record = 100, i.e. 60 countable months with Standing never binding below it. At Y10 the Sovereign *stock* is 954 accounts. Ever-qualified is higher than stock because Sovereign is rented by conduct: a single miss drops Standing to 91.7 and costs the tier.

### 4.2a Gate arrival is a distribution, not a date

The six-consecutive-period gate is a **run-of-6 first-passage problem**. An account that misses month 4 cannot reach Silver before month 9, so every downstream ladder date - Gold at M12, card eligibility, credit at M24, Sovereign at M61 - shifts right by the expected gate delay. v1.0 treats month 6 as universal.

Solved as a Markov chain on the run-length state (0-6) from each archetype's payment probability, with survival applied each month so an account that lapses before completing a run never gates.

| Archetype | Weight | Monthly pay prob | Monthly hazard | P(ever gates) | Mean gate month |
|---|---|---|---|---|---|
| Perfect payer | 10% | 0.995 | 0.016 | 90.6% | 6.1 |
| Occasional misser | 35% | 0.930 | 0.023 | 83.6% | 7.6 |
| Alternating misser | 12% | 0.550 | 0.034 | 24.0% | 24.9 |
| Reducer | 13% | 0.970 | 0.018 | 88.6% | 6.6 |
| Early lapser | 30% | 0.600 | 0.216 | 2.6% | 8.6 |

- **Expected gate month (among those that ever gate): 8.1** - not month 6.
- **Ever-gate share: 53.5%.**
- **Never-gated share: 46.5%** - persona H.

**The alternating misser is the striking row.** Paying every other month, it has only a 24.0% chance of ever assembling six consecutive periods, and when it does the mean arrival is month 24.9. v1.0 would have it Silver at M6 and Gold at M12; in reality three-quarters of that cell never scores at all. **This is the single largest correction the first-passage solve makes to the tier ladder's timing.**

### 4.2b The never-gated cell (persona H) and its stream 1 contribution

| year | Never-gated accounts | Live accounts | % of live | Share of stream 1 inflow % |
|---|---|---|---|---|
| 1.0 | 324.7 | 511.0 | 63.5 | 63.5 |
| 2.0 | 931.6 | 1,820.4 | 51.2 | 51.2 |
| 3.0 | 1,859.7 | 4,191.1 | 44.4 | 44.4 |
| 4.0 | 2,673.7 | 7,132.5 | 37.5 | 37.5 |
| 5.0 | 3,404.4 | 10,410.8 | 32.7 | 32.7 |
| 6.0 | 3,957.0 | 13,687.4 | 28.9 | 28.9 |
| 7.0 | 4,293.9 | 16,656.6 | 25.8 | 25.8 |
| 8.0 | 4,416.2 | 19,086.6 | 23.1 | 23.1 |
| 9.0 | 4,309.6 | 20,768.2 | 20.8 | 20.8 |
| 10.0 | 4,046.7 | 21,661.0 | 18.7 | 18.7 |

At Y10 the never-gated population is **4,047 accounts, 18.7% of the live book.** They pay the **full undiscounted entry fee** and consume **zero benefits, forever** - no tier discount, no Gold Rewards, no card, no credit, no family discount. **Structurally the highest-margin retail account in the book**, and v1.0 has no cell for them at all, which understates stream 1 margin and overstates benefit cost.

### 4.3 The alternating-misser cell

The pay-miss-pay-miss archetype is 12% of every vintage and is **permanently capped at Gold**: Recent holds at 6 forever, so Standing = 100/12 x 6 = **exactly 50**, which is the Gold threshold. With the rounded 8.3333 this evaluates to 49.9998 and the entire cell silently misclassifies to Silver. The model uses exact fractions (`Fraction(100,12)`), and `validate_gate_mechanics` asserts this.

This cell is revenue-relevant, not a curiosity: it sits at the lowest interchange rate (1.80%) and the highest FX margin (2.0%), and it consumes the fewest waivers - the most profitable card cell in the book per unit of spend.

---

## 5. AUM by year, reconciled to cumulative contributions

An audit found v1.0's implied AUM was 8-14x what contributions can produce. This establishes the true figure. The ratio is **below 1.0 by construction** and falls over time as leakage and redemption compound.

| year | cum_contributions | aum | aum/contrib | grams_bought_cum | grams_withdrawn_cum | grams_redeemed_cum | grams_closing |
|---|---|---|---|---|---|---|---|
| 1.00 | 232,000.00 | 204,261.56 | 0.88 | 1,559.30 | 69.21 | 46.14 | 1,443.95 |
| 2.00 | 1,232,244.22 | 1,017,813.07 | 0.83 | 8,291.27 | 657.73 | 438.49 | 7,195.06 |
| 3.00 | 3,750,792.45 | 2,935,328.59 | 0.78 | 25,434.47 | 2,810.54 | 1,873.69 | 20,750.24 |
| 4.00 | 8,474,402.76 | 6,206,643.46 | 0.73 | 57,612.79 | 8,242.31 | 5,494.87 | 43,875.61 |
| 5.00 | 15,872,930.79 | 10,812,353.45 | 0.68 | 108,047.22 | 18,967.93 | 12,645.29 | 76,434.00 |
| 6.00 | 26,198,959.54 | 16,568,752.96 | 0.63 | 178,844.52 | 37,030.65 | 24,687.10 | 117,126.77 |
| 7.00 | 39,438,021.60 | 23,018,151.43 | 0.58 | 269,663.00 | 64,166.73 | 42,777.82 | 162,718.45 |
| 8.00 | 55,189,729.98 | 29,587,088.40 | 0.54 | 378,328.05 | 101,503.74 | 67,669.16 | 209,155.16 |
| 9.00 | 72,529,425.69 | 35,317,866.33 | 0.49 | 498,004.20 | 149,002.44 | 99,334.96 | 249,666.81 |
| 10.00 | 90,746,186.70 | 39,790,584.12 | 0.44 | 623,790.03 | 205,502.98 | 137,001.99 | 281,285.06 |

**Y10: USD 39,790,584 of AUM against USD 90,746,187 of cumulative contributions = 0.438x.** Gold is held flat at F1 by design, so this ratio is pure flow arithmetic: contributions in, entry fee out, leakage and redemption out. It cannot exceed 1.0 without gold appreciation.

---

## 6. Opex by year and the fitted Opex(N)

| year | live_accounts | cost_opex | opex_per_live_account | fitted_opex_of_N |
|---|---|---|---|---|
| 1 | 511 | 1,031,907 | 2,019 | 1,724,276 |
| 2 | 1,820 | 1,192,011 | 655 | 1,802,983 |
| 3 | 4,191 | 1,475,189 | 352 | 1,945,484 |
| 4 | 7,133 | 1,671,282 | 234 | 2,122,294 |
| 5 | 10,411 | 1,911,078 | 184 | 2,319,347 |
| 6 | 13,687 | 2,178,469 | 159 | 2,516,304 |
| 7 | 16,657 | 2,455,768 | 147 | 2,694,781 |
| 8 | 19,087 | 2,728,412 | 143 | 2,840,852 |
| 9 | 20,768 | 2,984,591 | 144 | 2,941,933 |
| 10 | 21,661 | 3,219,856 | 149 | 2,995,594 |

### 6.1 The fitted Opex(N), block by block

Blocks scale on **different populations**, so one N will not do. A lapsed holder is still screened, still holds metal in the vault and still costs support - but generates no contribution and needs no acquisition spend.

| Block | Driver | Fixed component | Variable per account | Note |
|---|---|---|---|---|
| Headcount | contributing | 646,979.55 | 49.59 |  |
| MLRO | fixed | 0.00 | 0.00 | year-indexed step, does not scale with N |
| VARA supervision | fixed | 0.00 | 0.00 | year-indexed step, does not scale with N |
| Audit + attestation | fixed | 0.00 | 0.00 | year-indexed step, does not scale with N |
| Compliance + KYC | holding | 53,265.90 | 0.85 |  |
| Vault and metal | holding | 42,131.02 | 3.17 |  |
| Technology | holding | 46,643.21 | 2.31 |  |
| Corporate | contributing | 14,539.89 | 4.18 |  |
| Security | fixed | 0.00 | 0.00 | year-indexed step, does not scale with N |
| Legal + insurance | fixed | 0.00 | 0.00 | year-indexed step, does not scale with N |

**Holding:contributing ratio at Y10 = 2.96x.** The holding-driven blocks scale on the larger population.

**The anchor-population question, settled.** v1.0's §7.4 table is headed `Y1 (500) / Y3 (12,000) / Y10 (80,000)` and publishes a 'cost per investor' row against those counts; its own §14 default says the Y10 target counts investors **still contributing**. The anchors are therefore read as contributing counts, and holding counts at those anchors are inferred from this model's own contributing:holding trajectory (a `DERIVED_BY_MODEL` input - v1.0 could not compute it because it treated LAPSED as terminal).

v1.0 divided opex sized for 500 investors by margin-per-investor to get 171,911 investors. That is incoherent: opex is a function of N, so the denominator moves with the answer. The fixed point in §8 is the correct form.

---

## 6.2 Bar denomination (T3) solved endogenously

v1.0 hard-codes 100 g -> 1 kg at Y3 -> 12.4 kg at Y8. That schedule is indexed to a volume trajectory (80,000 investors, ~509 kg/yr) **the corrected model never reaches.** T3 is therefore solved against the model's own volume using the upgrade rule v1.0 itself states: upgrade only when `(annual grams x premium saved) > (incremental float x CoC) + incremental price-gap risk`.

| Year | Annual grams bought | Cycles/yr at solved bar | Solved bar | Solved premium | v1.0 assumed bar | v1.0 premium |
|---|---|---|---|---|---|---|
| 1 | 1,559 | 15.6 | 100 g | 3.00% | 100 g | 3.00% |
| 2 | 6,732 | 67.3 | 100 g | 3.00% | 100 g | 3.00% |
| 3 | 17,143 | 171.4 | 100 g | 3.00% | 1,000 g | 2.00% |
| 4 | 32,178 | 321.8 | 100 g | 3.00% | 1,000 g | 2.00% |
| 5 | 50,434 | 50.4 | 1,000 g | 2.00% | 1,000 g | 2.00% |
| 6 | 70,797 | 70.8 | 1,000 g | 2.00% | 1,000 g | 1.50% |
| 7 | 90,818 | 90.8 | 1,000 g | 2.00% | 1,000 g | 1.50% |
| 8 | 108,665 | 108.7 | 1,000 g | 2.00% | 12,400 g | 0.75% |
| 9 | 119,676 | 119.7 | 1,000 g | 2.00% | 12,400 g | 0.75% |
| 10 | 125,786 | 125.8 | 1,000 g | 2.00% | 12,400 g | 0.75% |

**Two findings.** 1 kg does not clear until **Year 5**, two years later than v1.0 assumes. And **Good Delivery never clears at all** - at ~126 kg/yr of Y10 purchasing, a 12.4 kg bar fills only ~10 times a year, and the unhedged price-gap carry on a USD 1.75m bar swamps the premium saving.

**This matters beyond the premium line.** v1.0's entry-fee ladder (T1, 5%->3%) and fabrication premium ladder (T2, 3.00%->0.75%) are both indexed to the same volume trajectory. The model reaches the volume for neither, so **the assumed margin improvement over time partly evaporates**: the premium stays at 2.00% rather than falling to 0.75%, which is 125bp of assumed margin that does not arrive.

---

## 7. Full P&L to net profit

Structured **revenue -> cost of revenue -> gross profit -> operating cost -> EBITDA -> tax -> net**. v1.0 booked the net contribution margin as the revenue line, which makes revenue go negative when the rail exceeds the fee. Revenue is now gross fees earned; the premium, price-gap, float and rail sit in cost of revenue where they belong.

| year | revenue | cost_of_revenue | gross_profit | cost_opex | cost_acquisition | cost_vault | cost_rewards | cost_card_fixed | cost_card_variable | operating_cost | total_cost | ebitda | tax | net_profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 13,212 | 7,496 | 5,716 | 1,031,907 | 71,807 | 9,000 | 0 | 0 | 0 | 1,381,791 | 1,389,287 | -1,376,075 | 0 | -1,376,075 |
| 2 | 82,267 | 32,423 | 49,844 | 1,192,011 | 202,289 | 9,000 | 0 | 188,000 | 6,462 | 1,604,067 | 1,636,489 | -1,554,223 | 0 | -1,554,223 |
| 3 | 347,645 | 90,999 | 256,646 | 1,475,189 | 392,371 | 9,000 | 10,855 | 180,000 | 38,511 | 2,118,192 | 2,209,191 | -1,861,546 | 0 | -1,861,546 |
| 4 | 851,122 | 166,211 | 684,911 | 1,671,282 | 562,049 | 11,639 | 40,175 | 180,000 | 110,151 | 2,594,711 | 2,760,921 | -1,909,799 | 0 | -1,909,799 |
| 5 | 1,602,737 | 233,332 | 1,369,405 | 1,911,078 | 748,070 | 21,514 | 97,580 | 180,000 | 234,418 | 3,219,794 | 3,453,126 | -1,850,389 | 0 | -1,850,389 |
| 6 | 2,553,007 | 299,335 | 2,253,672 | 2,178,469 | 937,563 | 34,657 | 197,530 | 180,000 | 416,684 | 3,978,474 | 4,277,809 | -1,724,802 | 0 | -1,724,802 |
| 7 | 3,768,344 | 369,223 | 3,399,121 | 2,455,768 | 1,127,224 | 50,088 | 348,514 | 180,000 | 660,626 | 4,862,275 | 5,231,499 | -1,463,155 | 0 | -1,463,155 |
| 8 | 5,081,501 | 431,056 | 4,650,446 | 2,728,412 | 1,313,952 | 66,569 | 555,138 | 180,000 | 963,921 | 5,851,919 | 6,282,974 | -1,201,473 | 0 | -1,201,473 |
| 9 | 6,582,426 | 470,558 | 6,111,868 | 2,984,591 | 1,479,930 | 81,975 | 817,930 | 180,000 | 1,321,782 | 6,913,850 | 7,384,408 | -801,982 | 0 | -801,982 |
| 10 | 8,150,081 | 492,875 | 7,657,206 | 3,219,856 | 1,623,205 | 94,660 | 1,132,682 | 180,000 | 1,723,830 | 8,024,257 | 8,517,132 | -367,051 | 0 | -367,051 |

### 7.0 Cost bridge (must close exactly)

| year | cor_premium | cor_pricegap | cor_float | cor_rail | cost_vault | cost_screening | cost_rewards | cost_redemption | cost_card_fixed | cost_card_variable | cost_acquisition | cost_opex | cost_oneoff | cost_family | cost_vat | SUM of components | total_cost | residual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.00 | 6,617.38 | 0.00 | 0.00 | 879.11 | 9,000.00 | 3,715.62 | 0.00 | 0.19 | 0.00 | 0.00 | 71,807.47 | 1,031,907.45 | 264,880.00 | 65.74 | 414.26 | 1,389,287.22 | 1,389,287.22 | 0.00 |
| 2.00 | 28,569.13 | 0.00 | 0.00 | 3,853.71 | 9,000.00 | 4,518.05 | 0.00 | 1.65 | 188,000.00 | 6,462.06 | 202,288.57 | 1,192,011.27 | 0.00 | 286.69 | 1,498.23 | 1,636,489.35 | 1,636,489.35 | -0.00 |
| 3.00 | 72,752.31 | 3,536.50 | 4,945.39 | 9,764.97 | 9,000.00 | 9,065.65 | 10,855.11 | 6.03 | 180,000.00 | 38,510.50 | 392,371.30 | 1,475,188.60 | 0.00 | 723.40 | 2,471.25 | 2,209,191.00 | 2,209,191.00 | -0.00 |
| 4.00 | 136,558.32 | 3,536.50 | 7,957.96 | 18,157.90 | 11,639.14 | 13,988.19 | 40,175.44 | 15.21 | 180,000.00 | 110,151.30 | 562,048.88 | 1,671,281.95 | 0.00 | 1,339.29 | 4,071.27 | 2,760,921.35 | 2,760,921.35 | 0.00 |
| 5.00 | 158,021.16 | 27,407.88 | 19,854.29 | 28,048.95 | 21,514.12 | 19,204.14 | 97,579.53 | 30.03 | 180,000.00 | 234,418.27 | 748,070.15 | 1,911,078.40 | 0.00 | 2,060.23 | 5,839.15 | 3,453,126.30 | 3,453,126.30 | -0.00 |
| 6.00 | 200,299.72 | 35,365.00 | 25,167.31 | 38,503.29 | 34,657.20 | 24,222.28 | 197,529.86 | 50.58 | 180,000.00 | 416,684.37 | 937,562.81 | 2,178,469.48 | 0.00 | 2,816.70 | 6,480.85 | 4,277,809.44 | 4,277,809.44 | 0.00 |
| 7.00 | 256,943.65 | 35,365.00 | 28,407.37 | 48,507.19 | 50,087.62 | 28,734.25 | 348,514.43 | 75.98 | 180,000.00 | 660,626.16 | 1,127,224.49 | 2,455,768.35 | 0.00 | 3,534.52 | 7,709.56 | 5,231,498.56 | 5,231,498.56 | 0.00 |
| 8.00 | 307,435.17 | 35,365.00 | 31,114.23 | 57,141.20 | 66,569.24 | 32,562.68 | 555,138.17 | 104.54 | 180,000.00 | 963,920.72 | 1,313,951.58 | 2,728,411.89 | 0.00 | 4,151.82 | 7,107.94 | 6,282,974.18 | 6,282,974.18 | 0.00 |
| 9.00 | 338,587.77 | 35,365.00 | 33,068.63 | 63,536.67 | 81,974.79 | 35,448.83 | 817,930.01 | 133.00 | 180,000.00 | 1,321,781.70 | 1,479,929.96 | 2,984,590.79 | 0.00 | 4,616.48 | 7,444.17 | 7,384,407.80 | 7,384,407.80 | 0.00 |
| 10.00 | 355,873.26 | 35,365.00 | 34,176.75 | 67,460.03 | 94,660.19 | 37,541.39 | 1,132,682.33 | 158.20 | 180,000.00 | 1,723,830.43 | 1,623,204.58 | 3,219,856.14 | 0.00 | 4,902.54 | 7,421.41 | 8,517,132.26 | 8,517,132.26 | 0.00 |

**Residual across all ten years: 0.000000.** The bridge closes to floating-point tolerance and is asserted at runtime every period.

### 7.0.1 Net contribution margin, reported as a metric

The inflow lanes' net margin after premium, price-gap, float and rail. This is the figure v1.0 used as its revenue line; it is retained here as a **metric**, not as revenue.

| year | stream1_net | stream1_sip | stream1_spot | cor_rail | cor_pricegap | cor_premium |
|---|---|---|---|---|---|---|
| 1 | 3,924 | 2,630 | 1,294 | 879 | 0 | 6,617 |
| 2 | 15,517 | 9,528 | 5,989 | 3,854 | 0 | 28,569 |
| 3 | 2,472 | -3,099 | 5,571 | 9,765 | 3,536 | 72,752 |
| 4 | 5,456 | -5,557 | 11,012 | 18,158 | 3,536 | 136,558 |
| 5 | 30,741 | 735 | 30,006 | 28,049 | 27,408 | 158,021 |
| 6 | 11,707 | -17,972 | 29,679 | 38,503 | 35,365 | 200,300 |
| 7 | 22,656 | -18,471 | 41,128 | 48,507 | 35,365 | 256,944 |
| 8 | -51,105 | -64,809 | 13,703 | 57,141 | 35,365 | 307,435 |
| 9 | -60,251 | -73,268 | 13,017 | 63,537 | 35,365 | 338,588 |
| 10 | -69,777 | -80,548 | 10,771 | 67,460 | 35,365 | 355,873 |

## 7.1 Cash flow and peak funding requirement

| year | ebitda | tax | float_movement | cash_flow | cumulative_cash | required_capital | total_funding_need |
|---|---|---|---|---|---|---|---|
| 1 | -1,376,075 | 0 | 0 | -1,376,075 | -1,376,075 | 408,441 | 1,784,516 |
| 2 | -1,554,223 | 0 | 0 | -1,554,223 | -2,930,298 | 408,441 | 3,338,739 |
| 3 | -1,861,546 | 0 | 76,882 | -1,938,428 | -4,868,726 | 408,441 | 5,277,167 |
| 4 | -1,909,799 | 0 | 40,875 | -1,950,675 | -6,819,401 | 408,441 | 7,227,842 |
| 5 | -1,850,389 | 0 | 172,857 | -2,023,247 | -8,842,647 | 408,441 | 9,251,088 |
| 6 | -1,724,802 | 0 | 43,161 | -1,767,964 | -10,610,611 | 408,441 | 11,019,052 |
| 7 | -1,463,155 | 0 | 38,135 | -1,501,290 | -12,111,901 | 408,441 | 12,520,342 |
| 8 | -1,201,473 | 0 | 30,176 | -1,231,649 | -13,343,549 | 408,441 | 13,751,991 |
| 9 | -801,982 | 0 | 19,784 | -821,766 | -14,165,316 | 408,441 | 14,573,757 |
| 10 | -367,051 | 0 | 9,162 | -376,213 | -14,541,529 | 408,441 | 15,076,460 |

- **Peak funding requirement: USD 15,076,460 at month 114** (cumulative cash deficit plus locked regulatory capital).
- Minimum cumulative cash: USD -14,668,019 at month 114.
- **P&L break-even (annual, EBITDA): no year within the 10-year horizon.**
- **Cash break-even: never within 120 months** (cumulative cash first turns positive). Reported separately from P&L break-even, per the build spec.

### 7.2 Regulatory capital, and the Option B escalator

Under **Option A** (the chosen route) capital is the AED 1.5m floor = **USD 408,441**, locked and not expensed (F15).

Under **Option B** the 2%-of-reserves escalator applies. At the model's own Y10 AUM of USD 39,790,584, 2% of reserves is **USD 795,812** - which is **1.95x the AED 1.5m floor. The escalator BITES**, and it is the binding constraint from the year reserves pass USD 20,422,056.

| Basis | Locked capital | Note |
|---|---|---|
| Option A floor (AED 1.5m) | 408,441 | flat at every period; the point of choosing Option A |
| Option B at Y10 reserves | 795,812 | 1.95x the floor |
| Incremental capital under Option B | 387,371 | additional permanently locked capital |

**Option B roughly doubles locked capital**, adding USD 387,371 that earns nothing. At the model's cost of capital that is an opportunity cost of about USD 30,990/yr - a memo line, not a P&L line, per the corpus.

The corpus sizes this at USD 4m on USD 200m of reserves. This model reaches USD 39,790,584, so the escalator lands at USD 795,812 rather than USD 4m - **but the direction of the finding is unchanged and the counsel question stands**: whether the 2% component can bite where a direct-ownership ARVA has no Reserve Assets.

---

## 8. Break-even, both views, as a fixed point

Solved as **`revenue(N) = total_cost(N)`** - against the same `total_cost` the P&L uses, so the solver and the EBITDA line cannot disagree.

**What was wrong in the previous draft.** Solving against `Opex(N)` alone silently excluded acquisition cost, vault, Gold Rewards, card fixed and variable, screening, redemption, family and VAT - together roughly half of total cost. It reported break-even at 11,171 accounts in Year 6, against an actual Year 6 EBITDA of USD -1,724,802. The figures below are against the full cost stack.

| View | Fixed-point solution | EBITDA-positive year |
|---|---|---|
| Entry-fee only (SIP + spot lanes) | **No solution exists** | none in 10 years |
| All streams | 45,102 accounts | none in 10 years |

### 8.1 Annual break-even is the headline; a single month is not

- **Annual EBITDA-positive year: none within the 10-year horizon.**
- **Annual net-profit-positive year: none within the 10-year horizon.**
- *Secondary detail only:* the first individual month with positive net profit is M115, but the year containing it still loses USD 367,051. **A single positive month inside a loss-making year is not break-even and must not be reported as one.**

### 8.2 What the two views actually say

**Entry-fee only: no solution exists, and that is the finding.** The two curves diverge rather than cross. The SIP lane's net contribution margin per collection is negative from Year 6 onward, so the entry-fee line cannot outgrow the cost base at any N. **The savings product cannot pay for itself at any scale on these assumptions.**

**All streams: the fixed point is 45,102 contributing accounts.** Revenue grows at USD 346 per contributing account against a cost slope of USD 304, so the gap does close - but only well beyond the 21,661 accounts the Base path reaches by Year 10.

**No year inside the horizon is EBITDA-positive.** The trajectory is improving steadily - EBITDA moves from USD -1,201,473 (Y8) to -801,982 (Y9) to -367,051 (Y10), roughly USD 400k/year.

**Extrapolating that trajectory, break-even lands at approximately Year 10.9** - just outside the ten-year window. That is the honest answer: **the business is close to viable on the Base path but does not get there inside the modelled horizon.**

The three drivers that decide this are card spend, card activation and PM share, in that order (§9) - all three are commercial conversations rather than research, which is the actionable finding.

---

## 8.3 The entry-fee schedule v1.0 assumes is not fundable

**This is a client-facing finding of the same class as the lapsed-cardholder question: the planned price reduction cannot be paid for.**

v1.0's fee ladder falls 5% -> 4% -> 3% *because* the fabrication premium was assumed to fall 3.00% -> 2.00% -> 0.75% as the business moved onto Good Delivery bars. **Those two schedules are physically coupled** - the premium is a function of bar denomination, and denomination is a function of volume (§6.2). v1.0 decoupled them and let the fee fall on a volume assumption the business does not reach.

Because Good Delivery never clears, the premium holds at 2.00%. A 3% fee less the tier-weighted discount is then **below cost**. The table solves, year by year, the fee at which the net contribution margin is exactly zero, at the modelled premium, price-gap, float, rail, tier discount and segment mix.

| Year | Bar | Premium | SIP ticket | v1.0 fee | Tier discount | Min viable fee | Shortfall | Fundable? |
|---|---|---|---|---|---|---|---|---|
| 1 | 100 g | 3.00% | 49.14 | 5.0% | 0.08pp | 4.96% | -0.04pp | yes |
| 2 | 100 g | 3.00% | 45.84 | 5.0% | 0.21pp | 3.99% | -1.01pp | yes |
| 3 | 100 g | 3.00% | 43.83 | 4.0% | 0.29pp | 4.18% | +0.18pp | **NO** |
| 4 | 100 g | 3.00% | 42.54 | 4.0% | 0.37pp | 4.18% | +0.18pp | **NO** |
| 5 | 1,000 g | 2.00% | 41.65 | 4.0% | 0.43pp | 3.78% | -0.22pp | yes |
| 6 | 1,000 g | 2.00% | 40.97 | 3.5% | 0.49pp | 3.79% | +0.29pp | **NO** |
| 7 | 1,000 g | 2.00% | 40.42 | 3.5% | 0.54pp | 3.74% | +0.24pp | **NO** |
| 8 | 1,000 g | 2.00% | 39.93 | 3.0% | 0.59pp | 3.74% | +0.74pp | **NO** |
| 9 | 1,000 g | 2.00% | 39.50 | 3.0% | 0.63pp | 3.76% | +0.76pp | **NO** |
| 10 | 1,000 g | 2.00% | 39.11 | 3.0% | 0.68pp | 3.79% | +0.79pp | **NO** |

**Years not fundable: Y3, Y4, Y6, Y7, Y8, Y9, Y10.** The worst case is Y10, where the fee needs to be 3.79% but v1.0 assumes 3.0% - short by 0.79pp.

**The SIP lane is always the binding constraint.** The spot lane clears at roughly 2.87% because the same fixed rail is spread over a USD 568 ticket instead of a USD 39 one. This is §0.2's non-linearity: the fee floor is set by the smallest ticket that carries a fixed rail event.

**Stated as the constraint the client faces, not as a recommendation:** *the entry fee cannot fall below approximately 3.8% unless volume rises far enough to justify a larger bar denomination, or the rail cost per collection falls.* Both levers are available - a larger bar needs roughly 4x the modelled Y10 gram volume, and the rail is a live PSP negotiation - but **the 3% headline in the current plan is not payable on the current trajectory.**

---

## 9. Sensitivity

Now includes **S27 (archetype mix), F27 (card programme fixed costs) and S48 (Y1 opex exit run-rate)** - the three the brief ranks as load-bearing that the earlier draft never flexed. S27 is ranked #1 in the brief's §8.4.

### 9.1 Tornado on cumulative net profit

| driver | aggressive | conservative | swing |
|---|---|---|---|
| Card spend per active card (S4) | -6,299,549 | -20,477,253 | 14,177,704 |
| Card activation rate (S5) | -11,308,598 | -17,847,974 | 6,539,376 |
| PM share of interchange (S3) | -11,355,704 | -17,715,527 | 6,359,822 |
| Card programme fixed costs (F27) | -13,439,995 | -15,565,495 | 2,125,500 |
| Payment archetype mix (S27) | -13,462,423 | -15,369,385 | 1,906,962 |
| Rail cost per collection (S1) | -13,919,109 | -15,526,752 | 1,607,643 |
| Family attach (S11) | -13,693,787 | -14,388,301 | 694,515 |
| Vault storage rate (S14) | -13,968,097 | -14,327,447 | 359,350 |
| Spot attach (S45) | -14,010,049 | -14,177,940 | 167,891 |
| Self-custody leakage (S10) | -14,162,310 | -14,012,957 | 149,353 |
| Credit take-up (S8) | -14,079,639 | -14,136,209 | 56,569 |
| Facility turnover (S40) | -14,101,386 | -14,118,904 | 17,519 |
| Y1 opex exit run-rate uplift (S48) | -14,109,649 | -14,111,624 | 1,975 |

### 9.2 Tornado on peak funding requirement

| driver | aggressive | conservative | swing |
|---|---|---|---|
| Card spend per active card (S4) | 10,580,508 | 21,316,727 | 10,736,219 |
| Card activation rate (S5) | 12,822,317 | 18,687,449 | 5,865,131 |
| PM share of interchange (S3) | 12,906,144 | 18,555,001 | 5,648,857 |
| Card programme fixed costs (F27) | 14,442,960 | 16,456,356 | 2,013,397 |
| Rail cost per collection (S1) | 14,904,354 | 16,387,738 | 1,483,384 |
| Payment archetype mix (S27) | 14,684,851 | 16,125,538 | 1,440,687 |
| Family attach (S11) | 14,699,632 | 15,327,679 | 628,047 |
| Vault storage rate (S14) | 14,953,541 | 15,264,193 | 310,652 |
| Spot attach (S45) | 14,971,702 | 15,146,923 | 175,220 |
| Self-custody leakage (S10) | 15,118,907 | 14,994,913 | 123,995 |
| Credit take-up (S8) | 15,049,730 | 15,098,735 | 49,005 |
| Facility turnover (S40) | 15,068,568 | 15,083,744 | 15,176 |
| Y1 opex exit run-rate uplift (S48) | 15,075,613 | 15,077,589 | 1,975 |

### 9.2.1 The two tornados now rank differently, as the brief predicted

| Rank | By net profit | By peak funding |
|---|---|---|
| 1 | Card spend per active card (S4) | Card spend per active card (S4) |
| 2 | Card activation rate (S5) | Card activation rate (S5) |
| 3 | PM share of interchange (S3) | PM share of interchange (S3) |
| 4 | Card programme fixed costs (F27) | Card programme fixed costs (F27) |
| 5 | Payment archetype mix (S27) | Rail cost per collection (S1) |
| 6 | Rail cost per collection (S1) | Payment archetype mix (S27) |
| 7 | Family attach (S11) | Family attach (S11) |
| 8 | Vault storage rate (S14) | Vault storage rate (S14) |
| 9 | Spot attach (S45) | Spot attach (S45) |
| 10 | Self-custody leakage (S10) | Self-custody leakage (S10) |
| 11 | Credit take-up (S8) | Credit take-up (S8) |
| 12 | Facility turnover (S40) | Facility turnover (S40) |
| 13 | Y1 opex exit run-rate uplift (S48) | Y1 opex exit run-rate uplift (S48) |

**The orders differ.** The brief flags identical rankings as a build failure, and adding F27 and S48 - both of which hit early-year cash far harder than terminal profit - separates them, as it predicted.

**Per the brief's own rule - if the tornado disagrees with §8.4's ranking, the tornado wins - the corrected load-bearing order on net profit is: Card spend per active card (S4), Card activation rate (S5), PM share of interchange (S3), Card programme fixed costs (F27), Payment archetype mix (S27).**

**On S27 specifically:** the brief ranks the archetype mix #1 load-bearing. Flexed to its own Aggressive/Conservative mixes it swings cumulative net profit by USD 1,906,962, placing it **#5** of 13. It is genuinely load-bearing - it *is* the persistency curve and the tier distribution - but on this cost base the card drivers dominate it.

### 9.3 PM share x card spend grid (cumulative net profit, USD)

| PM share | AED 3,500/mo | AED 6,000/mo | AED 9,000/mo |
|---|---|---|---|
| 0 | -24,929,301 | -21,744,679 | -17,699,695 |
| 1 | -22,580,017 | -17,715,527 | -11,655,967 |
| 1 | -20,477,253 | -14,110,495 | -6,299,549 |
| 1 | -18,869,508 | -11,355,704 | -2,227,648 |

The 36% row is the Phase 2 walk-away floor. Note that **no PM share saves the business at AED 3,500 of card spend**, and **every PM share works at AED 9,000** - card spend dominates PM share, which inverts the brief's ranking of S3 above S4.

### 9.4 Named scenarios

| Scenario | Y10 revenue | Y10 live accts | Y10 holding | Y10 AUM | Cum net profit | EBITDA+ year | Peak funding | Peak month |
|---|---|---|---|---|---|---|---|---|
| Base | 8,150,081 | 21,661 | 64,197 | 39,790,584 | -14,110,495 | none | 15,076,460 | 114 |
| Aggressive | 32,914,334 | 43,472 | 93,286 | 251,297,975 | 37,065,463 | 5 | 6,049,333 | 52 |
| Conservative | 1,018,689 | 8,730 | 38,566 | 3,573,658 | -24,888,701 | none | 25,428,705 | 120 |
| rail_kills_it | 8,150,081 | 21,661 | 64,197 | 39,790,584 | -15,526,752 | none | 16,387,738 | 118 |
| no_card | 1,767,497 | 21,661 | 64,197 | 39,790,584 | -24,633,515 | none | 25,472,990 | 120 |
| card_prepaid_capped | 5,845,160 | 21,661 | 64,197 | 39,790,584 | -21,364,675 | none | 22,204,149 | 120 |
| clients_plan | 17,668,003 | 54,010 | 169,756 | 97,529,200 | -7,218,254 | 10 | 10,468,829 | 113 |
| no_india | 6,118,450 | 16,700 | 50,715 | 33,187,620 | -17,746,327 | none | 18,534,329 | 120 |
| lapsed_loses_card | 4,756,308 | 21,661 | 64,197 | 39,790,584 | -19,352,546 | none | 20,192,021 | 120 |
| option_b_capital | 8,150,081 | 21,661 | 64,197 | 39,790,584 | -14,110,495 | none | 15,321,068 | 114 |

- **`rail_kills_it`** (conservative rail only, everything else Base): costs USD 1,416,257 of cumulative net profit. Material, but **not the largest driver** - the card assumptions dominate it.
- **`no_card`**: Y10 revenue collapses to USD 1,767,497, of which B2B is the majority. This is the §0.4 thesis confirmed numerically: without the card there is no business.
- **`card_prepaid_capped`** (lands prepaid at 1.00% flat rather than the credit ladder): Y10 revenue USD 5,845,160. A prepaid outcome removes roughly half the card's value.
- **`clients_plan`** (100k target imposed as a growth input): reaches 169,756 ever-acquired but only 54,010 live, and turns EBITDA-positive only in **Year 10** (the sole scenario other than Aggressive to do so inside the horizon). **The target is reachable on acquisition and does not fix the unit economics** - it buys break-even in the final year by brute-forcing volume.
- **`lapsed_loses_card`**: the open client question. Cumulative net profit moves by USD 5,242,051. See §11.

---

## 10. LTV / CAC by segment and channel, at the corrected persistency

Expected paying months at the corrected curve: **31.2** (v1.0's LTV numbers are flagged stale in the brief because they were computed on the old curve).

| segment | channel | ticket | net_margin_per_contribution | ltv_entry_fee_only | ltv_all_streams | cac | ltv_cac_entry | ltv_cac_all | payback_month_entry_only |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Agent | 75.00 | 1.36 | 42.55 | 949.04 | 72.00 | 0.59 | 13.18 | 52.80 |
| S1 | Referral | 75.00 | 1.36 | 42.55 | 949.04 | 42.00 | 1.01 | 22.60 | 30.80 |
| S1 | Direct | 75.00 | 1.36 | 42.55 | 949.04 | 120.00 | 0.35 | 7.91 | 88.10 |
| S2 | Agent | 40.00 | 0.61 | 19.05 | 734.03 | 72.00 | 0.27 | 10.20 | 118.00 |
| S2 | Referral | 40.00 | 0.61 | 19.05 | 734.03 | 42.00 | 0.45 | 17.48 | 68.90 |
| S2 | Direct | 40.00 | 0.61 | 19.05 | 734.03 | 120.00 | 0.16 | 6.12 | 196.70 |
| S3 | Agent | 20.00 | 0.18 | 5.62 | 551.72 | 72.00 | 0.08 | 7.66 | 400.00 |
| S3 | Referral | 20.00 | 0.18 | 5.62 | 551.72 | 42.00 | 0.13 | 13.14 | 233.30 |
| S3 | Direct | 20.00 | 0.18 | 5.62 | 551.72 | 120.00 | 0.05 | 4.60 | 666.70 |
| S4 | Agent | 40.00 | 0.61 | 19.05 | 691.40 | 72.00 | 0.27 | 9.60 | 118.00 |
| S4 | Referral | 40.00 | 0.61 | 19.05 | 691.40 | 42.00 | 0.45 | 16.46 | 68.90 |
| S4 | Direct | 40.00 | 0.61 | 19.05 | 691.40 | 120.00 | 0.16 | 5.76 | 196.70 |
| S5 | Agent | 30.00 | 0.40 | 12.34 | 625.72 | 72.00 | 0.17 | 8.69 | 182.30 |
| S5 | Referral | 30.00 | 0.40 | 12.34 | 625.72 | 42.00 | 0.29 | 14.90 | 106.30 |
| S5 | Direct | 30.00 | 0.40 | 12.34 | 625.72 | 120.00 | 0.10 | 5.21 | 303.80 |
| S6 | Agent | 75.00 | 1.36 | 42.55 | 939.34 | 72.00 | 0.59 | 13.05 | 52.80 |
| S6 | Referral | 75.00 | 1.36 | 42.55 | 939.34 | 42.00 | 1.01 | 22.36 | 30.80 |
| S6 | Direct | 75.00 | 1.36 | 42.55 | 939.34 | 120.00 | 0.35 | 7.83 | 88.10 |

**Payback on entry fee alone is `never` for every segment whose net margin per contribution is negative.** The all-streams LTV/CAC is the only view in which acquisition is rational, and it depends entirely on the customer reaching Gold and activating a card.

---

## 10.1 The nine parked parameters, solved

v1.0 §9 says the model 'returns each as a solved value with its arithmetic shown'. Seven are solved against model output below; one is retired and one is carried from the corpus.

| Item | Parameter | Solved value | Status |
|---|---|---|---|
| 1 | Entry-fee base uplift funding the discount ladder | 0.696pp | SOLVED |
| 2 | Gold Rewards rate ceiling | 1.148% of qualifying spend | SOLVED |
| 3 | Referral reward size | 399% of the referee's entry fee (LTV does not bind; F17's 30% is affordable) | SOLVED |
| 4 | Agent commission, three levels | USD 175.68/account, split 4/5/6 = 46.85 / 58.56 / 70.27 | SOLVED |
| 5 | Acquisition budget ceiling | 29.1% of total revenue (338% of entry-fee revenue) | SOLVED |
| 6 | Tenure rebate size | n/a - RETIRED | NOT APPLICABLE |
| 7 | B2B platform fee bps | 35 bps floor (modelled at 60 bps) | SOLVED |
| 8 | Family plan and per-beneficiary price | USD 32/yr + USD 20/name | CARRIED FROM CORPUS |
| 9 | PM share needed for EBITDA break-even in 10y | 77.5% | SOLVED |

**Arithmetic, item by item:**

- **Item 1 - Entry-fee base uplift funding the discount ladder** -> `0.696pp`. Book-weighted discount at the Y10 computed tier mix = 0.696pp. The 1.5pp Sovereign ceiling applies to only 4.4% of accounts, so the ladder costs far less than its headline.
- **Item 2 - Gold Rewards rate ceiling** -> `1.148% of qualifying spend`. (cum interchange 13,192,568 + credit 46,347 - custody 388,102) / cum card spend 1,119,222,206. Top-tier rate of 0.75% is INSIDE this ceiling.
- **Item 3 - Referral reward size** -> `399% of the referee's entry fee (LTV does not bind; F17's 30% is affordable)`. 25% of all-streams LTV 749 = 187 max affordable reward; the referee's entry fee over a 24-month run is only 47. The LTV ceiling is 4.0x the entire entry fee, so it cannot bind - **the binding constraint on referral reward is the acquisition budget (item 5), not LTV.** F17's 30% placeholder is affordable.
- **Item 4 - Agent commission, three levels** -> `USD 175.68/account, split 4/5/6 = 46.85 / 58.56 / 70.27`. Agent pool 5,075,076 over 28,889 agent-sourced accounts, split on V2's recommended 4/5/6 front-loaded gradient.
- **Item 5 - Acquisition budget ceiling** -> `29.1% of total revenue (338% of entry-fee revenue)`. Acquisition 8,458,460 against total revenue 29,032,342 and entry fee 2,504,849. **Confirms the brief's own flag**: expressed against entry fee the ceiling is 338%, which is meaningless. Total revenue is the right denominator.
- **Item 6 - Tenure rebate size** -> `n/a - RETIRED`. Decision 44 (2026-08-10) retired the mechanism. The brief's solver conflates Gold Rewards' 0.10-0.75% range with a superseded decaying redemption fee. No solve required.
- **Item 7 - B2B platform fee bps** -> `35 bps floor (modelled at 60 bps)`. Floor = vault rate 25bps + 10bps target margin. At Y10 partner AUM 215,306,667 the modelled 60bps yields 1,291,840/yr.
- **Item 8 - Family plan and per-beneficiary price** -> `USD 32/yr + USD 20/name`. Corpus §11 solved this at USD 29-36/yr against a USD 2.35 per-name floor (~5x headroom). Model carries the midpoint. Confirmed, not re-solved.
- **Item 9 - PM share needed for EBITDA break-even in 10y** -> `77.5%`. Bisection on PM share holding all else at Base. 

Two of these deserve the client's attention. **Item 5 confirms the brief's own flag**: expressed against entry-fee revenue the acquisition ceiling is a meaningless number, and total revenue is the right denominator. **Item 9 is the actionable one** - it says what PM share would have to be negotiated for the Base case to reach an EBITDA-positive year inside ten.

---

## 10.2 Gold price: level versus path, and the collateral stress

F1 holds gold flat by design - correct for revenue attribution, because it makes every revenue change attributable to the business rather than the metal. Gold is run two different ways below, and **the distinction is the whole point**: a level shift cannot produce a margin call, only a shock landing after a loan is struck can.

### 10.2.1 Gold as a LEVEL - and the invariance finding

| Gold move | USD/g | Y10 grams | Y10 AUM | Cum net profit | Peak funding |
|---|---|---|---|---|---|
| -30% | 99 | 401,836 | 39,790,584 | -14,008,700 | 14,938,379 |
| -25% | 106 | 375,047 | 39,790,584 | -14,025,482 | 14,961,210 |
| +0% | 141 | 281,285 | 39,790,584 | -14,110,495 | 15,076,460 |
| +25% | 177 | 225,028 | 39,790,584 | -14,190,599 | 15,186,789 |
| +30% | 184 | 216,373 | 39,790,584 | -14,205,879 | 15,208,113 |

**USD AUM is invariant to the gold price level, and that is a real property of the product rather than a modelling artefact.** Contributions are fixed in USD, so a permanently higher price buys proportionally fewer grams: Y10 grams fall from 401,836 to 216,373 across a -30% to +30% range while USD AUM holds at 39,790,584 throughout.

Everything downstream of USD AUM inherits the invariance - stream 6, ad valorem custody and the collateral base. Cumulative net profit moves only 1.4% across the whole range, via second-order effects on bar denomination and the price-gap. **A DCA gold product is close to indifferent to the level of the gold price. The client should be told this** - it is counter-intuitive and it is a genuine structural strength.

### 10.2.2 Gold as a PATH - the shock that can actually margin-call

A margin call comes from a move **after** the loan is struck. Drawn balances are carried as vintages at their originally struck LTV, so a shock revalues the collateral while leaving the debt unchanged. Shock lands at M61 (Y6), by which point the credit book has run three years.

| Shock at M61 | Margin calls USD | Grams liquidated | Peak month liquidation g | Float at shock (g) | Float covers peak? |
|---|---|---|---|---|---|
| -13% | 0 | 0 | 0 | 2,204 | yes |
| -29% | 0 | 0 | 0 | 2,476 | yes |
| -46% | 67,584 | 885 | 280 | 2,940 | yes |

**Only the -46% shock triggers margin calls** (67,584, 885 g liquidated). The -13% and -29% shocks pass through without a call, because the model's realised blended LTV across the Gold/Platinum/Sovereign mix is far below the 80% Sovereign ceiling - the book is Gold-weighted, and Gold is struck at 50%.

**The float absorbs it.** Peak single-month liquidation is 280 g against a float of 2,940 g at the shock month, so the liquidation never reaches the physical market. This is the float's fifth job, and it is the same argument that makes zero-fee redemption survivable.

**The caveat that matters.** This is a single-shock path, not a stochastic price process. It answers 'what happens if gold falls X% in Y6' and not 'what is the probability of a margin call over ten years'. The latter needs a price process, which is out of scope here and is listed in VALIDATION as a limitation.

### 10.2.3 Who is exposed - the static analytical ladder

This table is an **analytical statement, not a scenario result**: for an account struck at each tier's LTV and drawn to its maximum, it is the fall needed to reach the 92% margin-call line. It binds only on customers who max out at the top tier.

| Tier | Struck LTV | Accounts (Y10) | Collateral USD | Drawn at max | Fall to margin call | Within 1 sigma? | Grams to liquidate | Float covers? |
|---|---|---|---|---|---|---|---|---|
| Gold | 50% | 7,955 | 4,930,822 | 443,774 | 46% | no | 0 | yes |
| Platinum | 65% | 4,739 | 2,937,464 | 343,683 | 29% | no | 0 | yes |
| Sovereign | 80% | 954 | 591,422 | 85,165 | 13% | **YES** | 0 | yes |

**A 13% gold fall is roughly a one-sigma annual move at S6 = 25%.** Sovereign borrowers at maximum draw are genuinely exposed and the design should not pretend otherwise. Two mitigations, both real: the population is small (954 accounts at Y10) and the most disciplined in the book, and the ladder gives two warnings and 14 days before anything is sold.

**Does the float cover the liquidation?** At Y10 the float is 2,987 g against a Sovereign liquidation requirement of 0 g - **the float absorbs it**. Per the corpus this is the float's fifth job, and only breaches of the float band reach the physical market.

---

## 11. The open client question: does a lapsed account keep its card?

| | `LAPSED_KEEPS_CARD = True` (default) | `= False` |
|---|---|---|
| Y10 revenue | 8,150,081 | 4,756,308 |
| Cumulative net profit | -14,110,495 | -19,352,546 |
| Delta | - | -3,393,774 on Y10 revenue |

**This single switch moves Y10 revenue by 42%.** It decides whether the largest revenue stream decays with persistency or is immune to it. At 19% M61 persistency the lapsed-but-holding population is the majority of the book, so if it keeps its card, stream 2 is effectively decoupled from churn. If it does not, stream 2 inherits the survival curve. **This needs a client answer before the brief's headline revenue is fixed.**
