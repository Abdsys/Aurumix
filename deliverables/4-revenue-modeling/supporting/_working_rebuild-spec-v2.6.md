Perfect. I now have all the material I need. Let me compile the comprehensive normative build spec:

---

# AURUMIX REVENUE MODEL ARCHITECTURE BRIEF — NORMATIVE BUILD SPEC

**Version 2.6** | **As of 2026-08-20**

---

## 1. THE TIME GRID

**Period structure** (Lines 219, 287, 3575):
- **29 columns total**: 24 monthly (M1–M24) + 5 annual (Y3–Y7)
- **Monthly window M1–M24** covers three critical dates:
  - **M8.1**: gate resolution (mean run-of-6 first-passage)
  - **M18**: card launch (streams 2 & 4 activate; F27 costs begin M15)
  - **M20**: gold arrival (mean, with earliest M12)
- **Annual block Y3–Y7** replaces monthly resolution (D21, line 219)

**Lifecycle curves basis** (Line 237):
- Computed **monthly to M84** on a separate input sheet (not the Model sheet)
- Enables Y7 annual column to aggregate 12 genuine monthly points from the curve
- **No curve points are held, frozen or extrapolated** (line 246)
- Accounts reaching M84 are the maximum tenure any cohort can have in a 7-year model

**Monthly-to-annual conversions** (Lines 243–252):

| Quantity | Conversion rule |
|---|---|
| **Archetype survival** | Read curve at each of 12 months; aggregate. No `^12` shortcut (D23, line 245) |
| **Tier mix** | Compute at each of 12 months from tenure→tier lookup, convolved against acquisition, then aggregate (D22, lines 247, 585) |
| **Card spend, interchange, cardholder fees** | Sum 12 monthly convolution values (line 249) |
| **B2B platform fee** | Compute average opening + closing AUM; each partner runs own maturity clock (S43, line 250) |
| **Seasonality (S52a, S52b, S53)** | Monthly block only; normalise to exactly 12.00 in annual block and cancel (line 251) |
| **Tax (F33–F35)** | Booked annually in final month of financial year only, never monthly (line 252) |

---

## 2. THE POPULATION ENGINE

### Six Population States (D1, lines 28–36)

| State | Trigger | Holds gold | Advances clocks | Contributes | In AUM | Note |
|---|---|---|---|---|---|---|
| **PRE-GATE** | Run length 0–6, gate not passed | Yes | Run counter only | Yes | Yes | Zero benefits; full fee |
| **CONTRIBUTING** | Gate passed, paying monthly | Yes | Both (Months, Recent) | Yes | Yes | Earned tier discount applies |
| **REDUCED** | Contribution cut, freed from scoring | Yes | Both advance | Yes (reduced ticket) | Yes | S29 = MAX(20, 50% prior) |
| **REGULATORY BLOCK** | Compliance blocks account | Yes | Both frozen; window extends | No | Yes | Countable-month re-indexing (D5) |
| **STOPPED** | Investor cancels | Yes | Recent decays, Months held | No | Yes | 12-month silent boundary ahead |
| **DORMANT** | 12 consecutive silent periods | Yes | Recent decayed then held | No | Yes | **Hard absorbing boundary** |
| **CLOSED** | Grams = 0 | No | — | No | No | **Only true exit from AUM** |

**Pre-gate block** (D4, lines 94–107):
- Gate arrival is **run-of-6 first-passage distribution**, not a fixed date
- Mean gate month M8.1 (line 229)
- **Never-gated population** (persona H, scattered payer): pays full undiscounted fee forever; zero benefits; ~18.7% of Y10 live book (line 2872)
- **Zero-benefit window**: 8.1 months of full-fee revenue before first discount, per cohort (line 2873)

### Eligibility Gate: Run-of-6 (Line 2587, F7)

- **6 consecutive periods** required to reach gate
- Distribution from first-passage model, not fixed date
- **Card eligibility**: Gold tier (month 12 of clean run at earliest)
- Pre-gate and never-gated accounts earn zero ICS benefits but pay full fee

### Five Payment Archetypes + Withdrawal Split (D2, D3, S27 base, lines 63–70)

| Archetype | Weight | Monthly pay probability | Terminal tier | Notes |
|---|---|---|---|---|
| Perfect payer | 10% | 0.995 | Sovereign-capable only | ICS Record 100 AND Recent 12 AND Sold ≤30% |
| Occasional misser | 35% | 0.93 | Platinum ceiling | Normal behavior, still strong persistency |
| Alternating misser | 12% | 0.55 | **Gold, capped for life** | Persona I: real, permanently occupied |
| Reducer | 13% | 0.97 (at reduced ticket) | By payment record | Captures affordability-driven reduction |
| Early lapser | 30% | 0.60 declining | Silver floor / never-gated | Voluntarily exit unrelated to payment failure |

**Withdrawal behavior split** (D11, S31): six buckets straddling the 30% Retention kink, determining `Sold` denominator

### Survival & Tier Distribution (D3, lines 81–88)

- **Survival is emergent** from archetype mix + **common background hazard**
- Roughly half of terminal attrition is voluntary (chosen non-payment)
- **Tier is computed per archetype, then weighted**—never average-then-threshold (D2)
- ICS formula: `MAX(25, MIN(Record, Standing) × Retention)` followed by threshold lookup at 25/50/75/100 (line 55)
- **Sovereigns first appear M61** (line 2703); only perfect-payers reach this tier
- **Use exact fractions** (100/24, 100/12), not rounded decimals (D4, line 105)

### Convolution Against Acquisition Vector (D23, no cohort triangle)

- **Monthly acquisition vector** acq(s,t) computed once for each segment, period
- **Lifecycle curves** are pure functions of month-since-origination; read no period-t quantities (lines 1113–1118)
- **Convolution at period t** reads acq(s, 1..t) only; **range terminates at current period** (§3.x.4, line 1201)
- **Annual convolution** computed at each of 12 constituent monthly points, then aggregated (lines 1191, 1582)
- **NO annual aggregate acquisition is convolved**; that would collapse twelve first-passage months into one and destroy gate distribution (line 1191)

### Tenure→Tier Lookup Replaces Score Machinery (D22, §3 Layer 5)

- **Collapsed ladder**: all tiers read **flat Gold rate** (1.80%) on interchange (line 1806)
- Full three-tier ladder (1.80 / 2.05 / 2.10%) survives on **ICS Validation sheet only** for the 5% safety gate (§3 Layer 5d, line 1775)
- **Cost of collapse**: ~2% of gross profit at Y7 (line 233)
- **Lookup is computed per archetype per month**, then weighted by tier mix (lines 1772, 1585–1588)
- **Nothing frozen at M24/Y3 seam**

### Five % Collapse-Safety Gate (Line 1775)

- Measured cost against full three-tier ladder
- Reported separately; never changes the live model rate
- Belongs on ICS Validation sheet (line 275)

### Nine-Persona Validation Set (D2, line 2703, correction 20)

Personas A–I on ICS Validation sheet, **not** six as sometimes stated:
- Validates the archetype-based tier distribution against handcrafted test cases
- Ensures the collapsed lookup does not systematically bias tier distribution
- **Must pass before model ships** (line 2703)

---

## 3. SEGMENTS (D25, §5.1–5.2)

**Four modelled regions** (Lines 1322–1328):

| Region | Addressable base | Ceiling (S22) | Avg ticket (S55) | **Floor share (S54)** | Activation | UAE-resident (S49) |
|---|---|---|---|---|---|---|
| R1 UAE Indian | ~640k | **9.5%** | **USD 38** | **40%** | M1 | **100%** |
| R2 UAE other South Asian | ~620k (NEW) | **6.0%** | **USD 26** | **60%** | **M7** | **100%** |
| R3 Oman | ~600k | **4.0%** | **USD 26** | **58%** | M13 | **0%** |
| R4 India resident | ~12.5m | **0.35%** | **USD 30** | **25%** | `INDIA_ENABLED` | **0%** |
| **Total addressable** | | | | | | |
| **Total ceiling-constrained accounts** | | | | **165,750** | | |

**Reconciliation invariant** (Line 1332): `base × ceiling = 165,750 across all regions` (held equal to v2.1's 164,900 deliberately; base and ceiling moved together when propensity filter was deleted)

**Two-ticket-band derivation per region** (Lines 1361–1366):

```
Floor band     = USD 20                      at floor_share (S54)
Standard band  = (avg_ticket − 20 × floor_share) ÷ (1 − floor_share)
```

Derived bands:

| Region | Avg ticket | Floor share | Floor band | Standard band |
|---|---|---|---|---|---|
| R1 UAE Indian | 38 | 40% | USD 20 | **USD 50** |
| R2 UAE other South Asian | 26 | 60% | USD 20 | **USD 35** |
| R3 Oman | 26 | 58% | USD 20 | **USD 34** |
| R4 India | 30 | 25% | USD 20 | **USD 33** |

**Unit margin, rail cost, card spend computed per band and summed, never on regional average** (line 1368)

**Named, sized, deliberately not modelled** (§5.3, lines 1380–1384):
- **Bahrain** (~259k): CBB Crypto-Asset Module binds; no reverse-solicitation exemption; would require CBB pre-application
- **Emirati** (~1.33m): wrong persona, no remittance driver, already served by Liv Gold inside ENBD/ADIB
- **Western expat** (~500–600k): no gold-savings behaviour

---

## 4. REVENUE STREAM FORMULAS — VERBATIM FROM BRIEF

### Stream 1a: Entry Fee Margin — SIP

**Activation**: M1

**Rates** (F3, line 1460):
- Y1: 5.00%, Y3: 4.00%, Y10: 3.00%
- **Less tier-weighted discount** (0 / 0.4 / 0.8 / 1.2 / 1.5 pp)
- Pre-gate and never-gated pay full undiscounted rate

**Revenue basis** (Line 1466): **Gross margin retained** on the contribution, not the headline fee
- USD 75 contribution at 5% fee: Aurumix discloses 5% but retains only USD 1.61 (2.15% gross before rail; 1.36% net after rail at 3.00% premium—**now 2.79% gross, 1.97% net after F5 memo removal at 1.50% premium** per D31, D32)

**Monthly formula (M1–M24)** (Lines 1523–1572):

```
For each segment s, each period t:

  reduced_ticket(s)      = MAX(20, 0.50 × ticket(s))                    [S29]
  fee_applied(s,t)       = base_fee(t) − tier_weighted_discount(s,t)
    where tier_weighted_discount = Σ_tier [ share(s,t,tier) × discount(tier) ]

  sip_inflow(s,t)        = contributing(s,t) × ticket(s)
                         + reduced(s,t)      × reduced_ticket(s)

  net_of_fee(s,t)        = sip_inflow(s,t) × (1 − fee_applied(s,t))

  ⚠ D30: PREMIUM CHARGED ON NET NEW GRAMS, NOT GROSS
    recycled_grams(t)      = grams returned to float by redemption/self-custody
    net_new_grams(t)       = MAX(0, grams_required(t) − recycled_grams(t))
    premium_base(s,t)      = net_of_fee(s,t) × [net_new_grams(t) ÷ grams_required(t)]

  cogs(s,t)              = premium_base(s,t) × fabrication_premium(t)  [F4 = 1.50% / 0.95%]
  gross_margin(s,t)      = sip_inflow(s,t) − net_of_fee(s,t) − cogs(s,t)

  pricegap(s,t)          = sip_inflow(s,t) × pricegap_rate(t) × float_mode
    where float_mode = 0 under DEALER_CARRIED, 1 under OWN_FLOAT  [S51 = OWN_FLOAT FROM M1]

  ⚠ D32: FLOAT COST OF CAPITAL IS MEMO ONLY, NOT COGS
    floatcoc_memo(t)     = float_capital(t) × cost_of_capital ÷ 12  [§7.5]

  ⚠ D31: RAIL IS PASS-THROUGH, NOT DEDUCTED
    rail_memo(s,t)       = [ contributing(s,t) + reduced(s,t) ] × S1
    request_amount(s,t)  = ticket(s) + S1  [what customer is asked for]

  STREAM1a(s,t)          = gross_margin(s,t) − pricegap(s,t)
```

**Annual formula (Y3–Y7)** (Lines 1578–1599):

```
For each segment s, each year y:

  contributing(s,y)      = SUM over 12 constituent months of CONVOLUTION
                           at each month against M84 curve          [D23]
  tier_weighted_discount(s,y) = COMPUTED at each of 12 months from
                           tenure→tier lookup, then weighted. NOT held/frozen [D22]

  sip_inflow(s,y)        = Σ over 12 months of [ contributing(s,m) × ticket(s)
                                + reduced(s,m) × reduced_ticket(s) ]
  rail_memo(s,y)         = Σ over 12 months of
                             [ contributing(s,m) + reduced(s,m) ] × S1
                           [MEMO ONLY — passed through, never deducted, D31]

  All rate-based lines identical to monthly form applied to annual base.
  Seasonality does NOT apply — S52a normalises to 12.00 and cancels.

  STREAM1a(s,y)          = gross_margin − pricegap
```

**Key parameters** (Lines 1509–1520):
- Base entry fee: 5.0 / 4.0 / 3.0 % (F3, D9)
- Tier entry-fee discount: 0 / 0.4 / 0.8 / 1.2 / 1.5 pp (line 1512)
- **Fabrication premium: 1.50 / 0.95 %** at 100g / 1kg (F4, D28, OBSERVED 2026-08-19, **FAILED REPLICATION 2026-08-20, correction 36**)
- Price-gap risk (1σ): **0.79%** (line 1514; volatility 25%, 12.1-day bar fill)
- **Float cost of capital MEMO ONLY**: 0.49 / 0.31 / 0.38 % (F5, D32, not in margin)
- **Rail cost per event PASS-THROUGH**: 0.25 Base / 0.10 Agg / 1.36 Cons (S1, D31, grossed onto request)
- Gold price (flat): **141.46 USD/g** (F1, verified 2026-08-17)
- Ticket by segment: 75 / 40 / 20 / 40 / 30 / 75 USD/month (§5)

---

### Stream 1b: Entry Fee Margin — SPOT

**Activation**: M1

**Rate**: Identical to 1a—base fee less the account's earned tier discount (line 1629)

**Revenue basis**: Gross margin retained on spot volume, same as SIP (line 1630)

**Key finding** (D31, line 2726): **1a and 1b NOW IDENTICAL at 2.79% net margin** (formerly 2.25% vs 1.96%). The gap was entirely the fixed rail spread; removing the rail makes the lanes equal. **Spot remains structurally the margin inflow by event size** (USD 17.30 vs USD 2.09) **but not by percentage**, which reverses a stated finding (lines 2726–2731)

**Monthly formula (M1–M24)** (Lines 1669–1691):

```
For each segment s, each period t:

  tenure_uplift(s,t)     = 1 + 0.5 × MIN(1, avg_account_age_months(s,t) ÷ 36)
  attaching(s,t)         = live_accounts(s,t) × S45 × tenure_uplift(s,t)
  spot_events(s,t)       = attaching(s,t) × S47 ÷ 12 × spot_seasonality(month_of(t))
                         + arrears_events(s,t)

  spot_ticket(s)         = S46 × segment_scalar(s)
  spot_inflow(s,t)       = attaching(s,t) × S47 ÷ 12 × spot_seasonality × spot_ticket(s)
                         + arrears_events(s,t) × ticket(s)

  fee_applied(s,t)       = SAME as stream 1a — account's earned tier discount
  gross_margin(s,t)      = spot_inflow − spot_inflow × (1 − fee_applied) × (1 + premium)
  pricegap               = as 1a, × float_mode                             [S51]
  floatcoc               = MEMO ONLY — opportunity cost, not COGS    [D32]
  rail_memo(s,t)         = spot_events(s,t) × S1   [MEMO — passed through, D31]

  STREAM1b(s,t)          = gross_margin − pricegap

  FLOAT INVARIANT TEST (a check, not a cost):
    breach(t) = COUNT of orders where spot_ticket ÷ gold_price > float_grams(t)
    → must route to two-step quote. Report breaches; never net them off.
```

**Annual formula (Y3–Y7)** (Lines 1695–1702):

```
  attaching(s,y)        = live_accounts(s,y) × S45 × tenure_uplift(s,y)
  spot_events(s,y)      = attaching(s,y) × S47 + arrears_events(s,y)
                          [no seasonality — cancels over full year]
  spot_inflow(s,y)      = spot_events(s,y) × spot_ticket(s)
  rail_memo(s,y)        = spot_events(s,y) × S1    [MEMO — passed through, D31]
  STREAM1b(s,y)         = gross_margin − pricegap
```

**Key parameters** (Lines 1656–1664):
- Spot attach rate: **14%** Base / 24% Agg / 7% Cons of live accounts/yr (S45)
- Average spot ticket: **620** Base / 1,100 Agg / 320 Cons USD (S46, scaled by segment)
- Spot frequency: **1.7** Base / 2.4 Agg / 1.2 Cons events/attacher/yr (S47)
- Spot seasonality: ~45% in Akshaya Tritiya (Apr/May) + Diwali (Oct/Nov) windows (S47, S52a)
- Rail cost per event: **0.25 Base** (one transfer, not collection, S1, D31)

---

### Stream 2: Card Interchange

**Activation**: M18 (assumed; sponsor bank live)

**Gate**: Gold tier (month 12 of clean run at earliest)

**Rate by tier** (F12, VISA UAE IRF, line 1761):
- Gold (L1 / Platinum): **1.80%**
- Platinum (L2 / Signature): **2.05%**
- Sovereign (L3 / Infinite): **2.10%**
- Prepaid (all): 1.00% flat, capped (line 1768)

**CRITICAL: D22 collapses the ladder** (Line 1806)
- **All live tiers read FLAT Gold rate (1.80%)** in the Model sheet
- Full 1.80 / 2.05 / 2.10 ladder survives on ICS Validation sheet for 5% safety gate only
- Cost of collapse: ~2% of gross profit at Y7 (line 233)

**Monthly formula (M18–M24)** (Lines 1799–1826):

```
For each tier k ∈ {Gold, Platinum, Sovereign}, each period t:

  eligible(t,k)         = accounts at tier k, from CONVOLVED tenure→tier lookup [D22, D23]
  active_cards(t,k)     = eligible(t,k) × S5  [card activation rate]
  spend(t,k)            = active_cards(t,k) × S4 × S38(k) × S52b(month_of(t))

  gross_ic(t,k)         = spend(t,k) × F12_GOLD ÷ AED_per_USD
                          ** FLAT GOLD RATE (1.80%), NOT F12(k). D22 **

  txns(t,k)             = spend(t,k) ÷ F23(k) × 1.06              [+6% declines]
  txn_fee(t,k)          = txns(t,k) × F24

  net_ic(t,k)           = gross_ic(t,k) × PM_SHARE(t) − txn_fee(t,k)

  fraud(t)              = Σ_k spend(t,k) × S39 ÷ 10,000
  disputes(t)           = Σ_k txns(t,k) × 0.0009 × F25
  fixed(t)              = F27 monthly run-rate, from M18
                        + F27 one-offs booked in M15

  gold_rewards(t,k)     = MIN( spend(t,k) capped at F13 × rate(k),
                                net_ic(t,k) + stream5_attributable(t,k)
                                − custody_cost(t,k) )           [capped at self-funding]

  STREAM2(t) = Σ_k [ net_ic(t,k) − gold_rewards(t,k) ] − fraud − disputes − fixed
```

**Annual formula (Y3–Y7)** (Lines 1830–1839):

```
  active_cards(y,k)     = average of opening/closing counts COMPUTED at each
                          of 12 months. Nothing held or frozen.
  spend(y,k)            = Σ over 12 months of active_cards(m,k) × S4 × S38(k)
                          [no S52b — normalises to 12.00 and cancels]
  txns(y,k)             = spend(y,k) ÷ F23(k) × 1.06
  All other lines are monthly forms applied to annual base.
  fixed(y)              = 12 × monthly minimums + 4 × quarterly scheme assessments
  STREAM2(y)            = Σ_k [ net_ic − gold_rewards ] − fraud − disputes − fixed
```

**Key parameters** (Lines 1782–1795):
- Interchange by tier: 1.80 / 2.05 / 2.10 % (F12, **VISA UAE IRF schedule 18 Oct 2025**, primary)
- **PM share: 72% Base / 85% Agg / 55% Cons** (S3, **no UAE/MENA split published**; floor 36%)
- PM share by contract maturity: 55% Y2–Y3, stepping to 72% Y5+ (T6; use Low for M18–M30)
- Monthly spend per active card: **6,000 Base / 9,000 Agg / 3,500 Cons** AED (S4)
- Spend tier multiplier: **0.82 / 1.12 / 1.54** (S38, normalises to 1.018 at Y10 mix)
- Card activation rate: **65% Base / 80% Agg / 45% Cons** (S5)
- Per-transaction processor fee: **0.10 Base / 0.05 Agg / 0.15 Cons** USD/txn (F24, Stripe Issuing)
- Average transaction size: 185 / 240 / 310 AED (F23, implies ~27 / 28 / 30 txns/month)
- Fraud & chargeback: **9 Base / 5 Agg / 22 Cons** bps of spend (S39)
- Dispute handling: 22 / 14 / 40 USD/case (F25)
- **Card programme fixed costs** (F27): see cost architecture section below

---

### Stream 3: Family Plan & Digital Will

**Activation**: M1

**Gate**: None (open to everyone; tier only prices it)

**Rate**: USD 29–36/yr including 4 beneficiaries; USD 20 per additional name, capped ~USD 60/household

**Monthly formula (M1–M24)** (Lines 1902–1916):

```
For each segment s, each period t:

  plans(s,t)            = live_accounts(s,t) × S11
  names(s,t)            = plans(s,t) × avg_beneficiaries  [4 included, tail above]
  price(s,t)            = plan_price × [1 − tier_weighted_plan_discount(s,t)]
                        + extra_names(s,t) × 20 × [1 − tier_weighted_name_discount(s,t)]

  STREAM3(s,t)          = new_plans(s,t) × price(s,t)          [charged annually]
                        + renewing_plans(s,t) × price(s,t)     [at each anniversary]

  COST (to §7.2, not netted):
    onboarding(t)       = new_names(t) × (identity + aml)
    screening(t)        = cumulative_registered_names(t) × 0.36 ÷ 12
    platform(t)         = MAX(299, 1.85 × kyc_checks(t))     [F16 floor]
```

**Annual formula (Y3–Y7)** (Lines 1920–1925):

```
  plans(s,y)            = average live accounts × S11
  STREAM3(s,y)          = plans(s,y) × price(s,y)     [every plan renews once/year]
  screening(y)          = cumulative_registered_names(y) × 0.36
  platform(y)           = 12 × MAX(299, 1.85 × monthly_kyc_checks(y))
```

**Key parameters** (Lines 1887–1897):
- Attach rate: **20% Base / 35% Agg / 10% Cons** of live accounts (S11, **pure assumption**)
- Plan price: 29–36 USD/yr (awaiting client sign-off)
- Tier plan-fee discount: 0 / 10 / 20 / 35 / 50 % (line 1892)
- Per-beneficiary discount: 0 / 0 / 0 / 10 / 20 % (starts at Platinum only, line 1893)
- Continuous screening: **0.36 USD/name/yr** for 20–40 years (line 1896)

---

### Stream 4: Cardholder Fees (FX, ATM, issuance)

**Activation**: M18 (with card)

**Gate**: Gold tier

**Three bases** (Line 1955):
1. FX margin on foreign spend (by tier)
2. ATM withdrawals beyond free allowance (by tier)
3. Issuance and replacement events (by tier)

**Monthly formula (M18–M24)** (Lines 1988–2003):

```
For each tier k, each period t:

  foreign_share(t)      = S53(month_of(t))   [seasonal vector, NOT flat S34]
  foreign_spend(t,k)    = spend(t,k) × foreign_share(t)
  fx_rev(t,k)           = foreign_spend(t,k) × fx_margin(k)

  ATM — computed over S35 DISTRIBUTION, not mean:
  atm_rev(t,k)          = active_cards(t,k)
                        × Σ_bucket [ weight(bucket)
                                   × MAX(0, midpoint(bucket) − allowance(k)) × 0.02 ]

  issue_rev(t,k)        = issuance_events(t,k) × F21(k) + replacement_events(t,k) × F22(k)
  issue_cost(t,k)       = (issuance + replacement events) × F26(k)     [contra]

  STREAM4(t) = Σ_k [ fx_rev + atm_rev + issue_rev − issue_cost ] ÷ AED_per_USD
```

**Annual formula (Y3–Y7)** (Lines 2007–2015):

```
  foreign_share(y)      = S34 annual mean (34%)  [S53 normalises out]
  foreign_spend(y,k)    = spend(y,k) × S34
  atm_rev(y,k)          = Σ over 12 months of monthly distribution formula,
                          each at that month's own convolved card count/mix.
                          Nothing held or frozen.                       [D21]
  issue_events          = active_cards(y,k) × (S36 + S37)
  STREAM4(y)            = Σ_k [ fx_rev + atm_rev + issue_rev − issue_cost ] ÷ AED_per_USD
```

**Key parameters** (Lines 1971–1982):
- FX margin by tier: **2.0 / 1.5 / 1.0 %** (line 1973)
- Free ATM allowance by tier: **1,000 / 2,500 / 5,000 AED/month** (line 1974, monthly not rolling)
- Over-allowance ATM fee: 2.0% (line 1975)
- **Foreign spend share: 34% Base / 45% Agg / 24% Cons** (S34, **applied as S53 seasonal vector**, line 2029)
- Foreign spend seasonal: 30/30/30/32/34/**55**/**60**/**56**/36/42/40/32, rescaled to 34% mean (S53)
- Issuance fee: 75 / waived / waived AED (F21)
- Replacement fee: 100 / 50 / waived AED (F22)
- Issuance event rate: 1.00 at activation, +0.06/yr (S36, tier upgrades force reissue)
- Replacement event rate: 0.11 / 0.07 / 0.18 (S37)

---

### Stream 5: Lending Revenue Share

**Activation**: M24 (assumed; lending partner signed), **annual block only**

**Gate**: Gold tier

**Structure**: Five heads (interest share, origination, servicing, penal, recovery); Aurumix takes no credit risk

**Annual formula (Y3–Y7)** (Lines 2080–2115):

```
For each tier k, each period t, each vintage v:

  eligible_collateral(t,k)  = grams seasoned 90 days, unpledged, held by tier-k accounts [F10]
  facility_limit(t,k)       = eligible_collateral(t,k) × gold_price × F11(k)
  borrowers(t,k)            = eligible_accounts(t,k) × S8

  peak_drawn(t,k)           = facility_limit(t,k) × S8 × S9
  avg_drawn(t,k)            = peak_drawn(t,k) × S40           [71-day realised tenor correction]

  VINTAGING — carry drawn balances by STRUCK LTV, not current tier:
    avg_drawn(t, struck_ltv=v) rolls forward on own amortisation to term;
    only NEW draws in period t struck at CURRENT tier's F11.

  draw_events(t,k)          = borrowers(t,k) × S41 ÷ 12

  interest_share(t)         = Σ_v avg_drawn(t,v) × aurumix_interest_share ÷ 12
  origination(t)            = Σ_k draw_events(t,k) × avg_draw_size(k) × F28_gross × F28_share
                              [PER EVENT — NOT scaled by S40]
  servicing(t)              = Σ_v avg_drawn(t,v) × F29_gross × F29_share ÷ 12
  penal(t)                  = Σ_k overdue_balance(t,k) × F30_gross × F30_share
  recovery(t)               = 0                                           [F31]

  STREAM5(t) = interest_share + origination + servicing + penal + 0
```

**Annual (Y3–Y7)** (Lines 2108–2115):

```
  avg_drawn(y,v)        = average of opening and closing vintage balances
  draw_events(y,k)      = borrowers(y,k) × S41
  interest_share(y)     = Σ_v avg_drawn(y,v) × aurumix_interest_share
  servicing(y)          = Σ_v avg_drawn(y,v) × F29_gross × F29_share
  origination(y)        = Σ_k draw_events(y,k) × avg_draw_size(k) × F28_gross × F28_share
  STREAM5(y) = interest_share + origination + servicing + penal + 0
```

**Key parameters** (Lines 2063–2076):
- LTV ladder: **50 / 65 / 80 %** (F11, settled 2026-08-13, no longer contingent on partner)
- Collateral seasoning: **90 days** (F10)
- Take-up among eligible: **18% Base / 30% Agg / 8% Cons** (S8)
- Drawn as % of permitted: **50% Base / 70% Agg / 30% Cons** (S9)
- **Peak-to-average turnover correction: 0.42 Base / 0.55 Agg / 0.30 Cons** (S40, **cuts stream 5 by 1.88×**, derived from 71-day tenor)
- Draw events/borrower/yr: **2.1 Base / 3.2 Agg / 1.3 Cons** (S41, moves with S40)
- Origination fee: **1.00% gross / 50% Aurumix share** (F28)
- Servicing fee: **0.50%/yr gross / 70% Aurumix share** (F29)
- Penal fee: **2.00% per late event / 40% Aurumix share** (F30)
- **Recovery fee: 1.50% / 0% Aurumix share** (F31, **modelled at zero** due to VARA III.E.4 recharacterisation risk)

---

### Stream 6: B2B Platform Fee

**Activation**: M24 (assumed; requires **Week 1 multi-tenant build**)

**Gate**: None (partner accounts earn no ICS)

**Rate**: Placeholder **0.5–0.75%/yr**, invoiced monthly in cash on AUM

**Annual formula only (Y3–Y7)** (Lines 2177–2197):

```
For each partner p, each period t:

  maturity(p,t)         = t − go_live_month(p)
  ramp(p,t)             = S43_lookup( maturity(p,t) )        [interpolated]
  partner_AUM(p,t)      = S44_terminal(p) × ramp(p,t) × india_factor

    where india_factor  = 1 if INDIA_ENABLED, else 0.40
    [B2B row is 60% S5 per S16 — the two switches are NOT independent]

  STREAM6(t) = Σ_p partner_AUM(p,t) × bps_rate ÷ 12

  ZERO entry-spread revenue from the partner channel.
```

**Annual (Y3–Y7)**:

```
  partner_AUM(p,y)      = average of opening and closing AUM for partner p
  STREAM6(y)            = Σ_p partner_AUM(p,y) × bps_rate
```

**Key parameters** (Lines 2168–2172):
- Partner count by year: **1 / 2 / 3 / 4 / 6 / 8** Base (S42)
- Per-partner AUM ramp: **8 / 25 / 48 / 70 / 85 / 100 %** at M6/12/24/36/48/60 of partner's maturity (S43)
- Terminal AUM per partner: **32 Base / 45 Agg / 22 Cons** USD m (S44)
- **SafeGold precedent**: zero entry-spread revenue (line 2211)

---

### Stream 0: Redemption (Mandatory Cost, Zero Revenue)

**Activation**: M1

**Rate**: **Zero** — VARA Annex 2 III.E.4 forbids any fee (Line 2226)

**Monthly formula (M1–M24)** (Lines 2254–2266):

```
  redemption_grams(t)   = [ contributing_AUM_grams(t) × S32
                           + lapsed_holding_grams(t)   × S32 × S33 ] ÷ 12
  redemption_events(t)  = redemption_grams(t) ÷ avg_redemption_size

  net_flow_grams(t)     = sip_grams(t) + spot_grams(t)
                        − self_custody_out(t) − redemption_grams(t)

  STREAM0(t) = redemption_events(t) × F20
             + MAX(0, −net_flow_grams(t)) × gold_price × dealer_two_way_spread
             [second term ZERO in every month the book grows]
```

**Annual (Y3–Y7)**: Identical, without ÷ 12

**Key parameters** (Lines 2244–2251):
- Redemption rate: **8% Base / 4% Agg / 16% Cons** of AUM/yr (S32, below self-custody because on-chain route is frictionless)
- Lapsed-holder multiplier: **2.2× Base / 1.6× Agg / 3.5× Cons** (S33, applied to S32 AND S31)
- Cost per redemption event: **4.20 Base / 2.50 Agg / 9.00 Cons USD** (F20: outbound payment 1.00–2.50 + re-screen 1.85 + handling 1.00–4.50)
- **Dealer two-way spread**: on net outflow only; observed 1.50% (correction 35)

**Critical note** (Line 2284): VARA III.E.4 "equal value" incidence is **counsel question**—safe reading is full prevailing value (Aurumix absorbs spread); arguable reading is realisable value (customer absorbs). **The difference is the entire two-way spread.**

---

## 5. COST ARCHITECTURE

### Cost of Goods Sold (Lines 2291–2301)

**Two terms only** (D7, D32):

1. **Fabrication premium** (F4): **1.50% / 0.95 %** at 100g / 1kg (D28, OBSERVED, **confidence now MODERATE after failed replication 2026-08-20**)
2. **Price-gap risk** (1σ): **0.79%** on 25% volatility, 12.1-day bar fill (line 1514)

**NOT in COGS**:
- ⚠ **Float cost of capital** (F5): **Removed by D32**—it is an imputed equity cost, not a cash expense. Reported as `floatcoc_memo` on Summary, **not in any margin** (lines 2295, 2552–2557, 2561)
- ⚠ **Payment rail** (S1): **Removed by D31**—third-party PSP charge, not Aurumix charge. Grossed up onto request and remitted (lines 2297, 490–495)

**Conditional: if float is debt-funded**
- Add `FLOAT_DEBT_FUNDED` switch (D32, line 2563)
- If ON, restore interest expense as a financing line in P&L

**Note on D30** (Lines 447–460): Premium charged on **net new grams**, not gross inflow. Only the net addition to the book is procured from dealer; recycled redemptions re-allocated without re-paying premium.

### Benefit Costs (Contra-Revenue) (Lines 2305–2320)

| Benefit | Cost type | Funded by | Model treatment |
|---|---|---|---|
| **Entry-fee discount** (0 / 0.4 / 0.8 / 1.2 / 1.5 pp) | Real, reduces stream 1 | Stream 1 base-rate uplift | Reduce `f` by tier-weighted discount. Pre-gate and never-gated carry zero |
| **Credit LTV ladder** (— / — / 50 / 65 / 80 %) | Zero cash cost, revenue-positive | Stream 5 | Higher LTV raises drawn balances |
| **Card tier** (FX 2.0 / 1.5 / 1.0 %, ATM allowance) | Waived stream 4 revenue | Stream 2 interchange | Net against stream 4; do not double-count |
| **Gold Rewards** (— / — / 0.15 / 0.45 / 0.75 %) | Real unit cost per event | Stream 2 + 5, net of custody | Haircut on stream 2, capped at customer-generated revenue |
| **Will/family discount** (0 / 10 / 20 / 35 / 50 %) | Real, reduces stream 3 | Stream 3 price headroom | Reduce stream 3 price by tier |
| **Per-beneficiary discount** (0 / 0 / 0 / 10 / 20 %) | Real, reduces stream 3 | Stream 3 price headroom | Starts only at Platinum |

**Gold Rewards cap** (Line 2314): capped at the interchange and credit revenue that customer generated, net of their custody cost. At PM_SHARE ≥ 36% it can never exceed its funding line (0.75 ÷ 2.10 = 35.7%, verified).

**Solver item 1**: Entry-fee uplift required to fund the discount ladder is **0.696pp** at Y10 book-weighted mix (lines 2867–2875)—less than half the 1.5pp Sovereign ceiling because it applies to only 4.4% of accounts.

### Acquisition Cost (Lines 2322–2336)

**Member referral** (F17):
- **30%** of the referee's entry fee over six qualifying contributions, split equally, credited in grams
- Reward paid at referee's gate (no earlier than M13 at minimum)
- Under D4, may be later for imperfect payers
- **Affordable at up to 399% of referee's entry fee** against all-streams LTV (line 2845); LTV does not bind
- **Binding constraint is the acquisition budget ceiling** (item 2), not LTV

**Agent commission** (F39, lines 2845–2846):
- **Solved at USD 175.68/account** (split 46.85 / 58.56 / 70.27 across three levels, front-loaded 4/5/6 gradient)
- Client's stated 15% of a non-existent base (Algorithmic Growth Fee) consumed **88% of Y1 gross margin** when transplanted to entry fee (line 2332)
- Subject to acquisition budget ceiling

**Agent recruitment** (S18):
- **Annual attrition: 45% Base / 30% Agg / 60% Cons** (line 1656)
- Holding 200 active agents requires ~90 recruits/yr (line 2334)
- Model recruits as explicit cost line and explicit productivity drag

**Agent ramp** (S17):
- M1–M6: 0.20, M7–M12: 0.40, M13+: 0.60/0.75/0.85/0.95/1.00/1.05 (line 2655)
- Catches the confirmed SIP gate at M6

**Acquisition budget ceiling** (Item 2):
- One board-approved cap on member rewards + all agent commission, as % of entry-fee revenue (D6)
- Applied with **one-period lag**: `budget(t) = ceiling% × stream1_revenue(t−1)` (lines 1186, 3.x.3)
- **Solved at 29.1% of TOTAL revenue** (line 2844); expressed against entry-fee revenue the ceiling is 338% (meaningless, confirms the brief's own flag)
- Annual block lag is one annual column (12 months), not one month (line 1186)

### Operating Expenses (Lines 2338–2356)

**Anchor schedule** (Base scenario, F32):

| Block | Y1 | Y3 | Y10 | Step or scale | Interpolation | Confidence |
|---|---|---|---|---|---|---|
| Headcount | 588,000 | 1,340,000 | 4,600,000 | Step | Quarterly steps; log-linear between anchors | Low-Med |
| MLRO (outsourced Y1–Y2, in-house Y3+) | 49,000 | 163,000 | incl. above | Step, then folds | Decay standalone line Y3→Y10 as merges | Medium |
| VARA supervision (Cat 1) | 54,500 | 94,500 | 110,000 | Step | Flat AED 200k until activity added (F14); booked in anniversary month | **High** |
| Audit + reserve attestation | 35,000 | 60,000 | 180,000 | Step | Tech audit in anniversary month; attestation in months 6 + 12 each year | Med/Judgement |
| Compliance + KYC (Sumsub) | 31,600 | 97,200 | 255,500 | Scale with floor | `MAX(299, 1.85 × checks)` — binds below 162 checks/mo (F16) | **High** |
| Vault and metal | 12,000 | 150,000 | 800,000 | Scale with floor | `MAX(USD 25/day, 0.10/kg/day)` — binds below ~250 kg | Medium |
| Technology | 34,000 | 115,000 | 600,000 | Scale | Log-linear on account count | Low |
| Corporate (DMCC, office, visas) | 20,700 | 60,000 | 350,000 | Step | DMCC in incorporation month; office steps at headcount thresholds | **High** |
| Security | 10,000 | 35,000 | 200,000 | Step | Log-linear, rounded to annual steps | Med |
| Marketing | incl. below | 250,000 | 1,200,000 | Scale—decision variable | Set by acquisition plan & S25 CAC curve; straight-line from zero Y1 | Judgement |
| **Legal and trust** (new v2.0) | see §7.7 | see §7.7 | see §7.7 | Step | Log-linear | **Unpriced** |
| Insurance & contingency | see §7.7 | see §7.7 | see §7.7 | Step | Policy anniversary month | Judgement |
| **Total annual opex** | **894,800** | **2,484,700** | **8,695,500** | | | |

⚠ **Row B, not Row A** (Line 2365): Row A is benchmark at v1.0's assumed counts (500 / 12k / 80k); Row B is `Opex(N)` evaluated at counts the acquisition engine actually produces (508 / 1,805 / 4,146 / 7,035 / 10,238 / 13,421 / 16,285 / 18,607 / 20,186 / 20,990). They diverge by **2.7× at Y10**, removing ~USD 5.5m of Year 10 cost.

**Card programme fixed costs** (F27, lines 2620–2629):

| Line | Base | Agg | Cons | When |
|---|---|---|---|---|
| BIN sponsorship setup | 45k | 25k | 90k | M15 |
| Scheme certification | 30k | 18k | 60k | M15 |
| BIN monthly minimum | 6k/mo | 3.5k/mo | 12k/mo | M18 onward |
| Processor platform | 5k/mo | 3k/mo | 9k/mo | M18 onward |
| Visa scheme quarterly | 12k/q | 7k/q | 22k/q | M18+ quarter-end |
| **Annualised run-rate from M18** | **180k/yr** | **106k/yr** | **340k/yr** | |

**Volume at which minimum stops binding** (Line 2631): At Base, USD 180k/yr against ~0.79% gold-tier net interchange requires ~USD 22.8m annual spend ≈ 290 active cards. On Y2 with 65% activation, programme approximately at breakeven at launch, immaterial thereafter.

**One-off Year 1** (Line 2373):
- VARA application: AED 100,000 (USD 27,200)
- Tier-1 smart contract audit: USD 75,000 (annual, not one-off per correction 10)
- DMCC incorporation: USD 3,280
- **DIFC SPV: USD 1,900** (not ADGM per correction 17)
- Licensing support: USD 20,000
- Legal & trust: **unpriced** (§7.7)

**Four corrections to cost treatment** (Lines 2375–2380):
1. Audit is annual + pre-launch, not one-off
2. Reserve attestation is biannual (6 + 12 months each year), not annual
3. Vault minimum binds at launch (USD 9,125/yr, 0.37% effective rate at Y1 AUM)
4. VARA activities may be under-scoped (Category 1 Issuance alone may not cover distribution/redemption)

**Minimum-commitment pattern** (Line 2382):
- DGCX vault: USD 25/day minimum
- Sumsub platform: USD 299/month minimum
- Card programme (F27): BIN/processor/Visa minimums
- **All three bind at low volume and decay to immateriality at scale**

### Float & Working Capital (Lines 2388–2451)

**Float sizing rule** (F38, line 2400):

```
float_grams(t)    = MAX( 2 × bar_grams(t),
                         bar_grams(t) + S50 × daily_inflow_grams(t) )
float_capital(t)  = float_grams(t) × gold_price × (1 + fabrication_premium(t))
```

**Float capital by year** (Corrected at F1 = 141.46, line 2419):

| Year | Grams | **Corrected capital** |
|---|---|---|---|
| Y1 | 200 g (2 × 100g) | **~USD 29k** |
| Y3 | 3 kg | **~USD 437k** |
| Y10 | 24.8 kg | **~USD 3.6M** |
| Tradeflow 1 kg launch | 2 kg | **~USD 285k** |

**Three rules on float** (Lines 2426–2431):
1. Do NOT charge float carry to any margin, COGS or unit-economics line (D32)
2. Do NOT run float capital through P&L (balance-sheet item only)
3. Do NOT net float against VARA minimum capital without counsel

**Float carry mode** (S51, D29, line 431):
- **OWN FLOAT FROM M1** (forced, not chosen)
- Price-gap risk and float capital bite from M1
- Premium narrows accordingly
- ⚠ Charging both wide dealer premium AND float costs = double-count (correction 12)

**Dealer-carried vs own-float fork** (Lines 2435–2442):

| | Dealer-carried | Own float |
|---|---|---|---|
| Working capital | **Zero** | ~29k / 437k / 3.6M |
| Price-gap risk | Dealer's | Aurumix's, ~0.4% |
| Float cost of capital (F5) | **Zero** | 0.49 / 0.31 / 0.38% |
| Premium | **Wider** | Narrower at scale |
| Risk | Single-counterparty; dealer withdraws | Operational + capital |

**Tradeflow binary** (Line 2446): If warrants wanted from launch, bar denomination forced to 1 kg, launch float ~USD 285k instead of ~USD 29k—**10× capital step**

### Regulatory Capital (Lines 2452–2473)

**Required capital** (Line 2457):

```
required_capital(t) = MAX( AED 1,500,000,
                           0.02 × trailing_24m_avg_reserve_assets(t) × OPTION_B )
```

| Basis | Locked capital | Note |
|---|---|---|
| **Option A floor** (AED 1.5m) | **USD 408,441** | Flat at every period — the point of choosing A |
| **Option B at Y10 reserves** | **USD 795,812** | **1.95× the floor** |
| Incremental under Option B | **USD 387,371** | Permanently locked, earns nothing |

**Reporting**: report escalator as opportunity cost memo line, not P&L line (~USD 30,990/yr on increment)

**Funding view summary** (Line 2483):

| Component | Treatment |
|---|---|
| AED 1.5m VARA minimum | Locked, not expensed. Posted at launch |
| Float principal | Balance sheet. Zero under dealer-carried; §7.5 amounts under own |
| One-off launch | Cash, Year 1: application, audit, incorporation, DIFC SPV, licensing, **legal (unpriced)** |
| Cumulative operating losses | **10-year: USD 14,110,495 cumulative loss** with cash reaching **−USD 14,541,529** at Y10 |
| **Total funding requirement** | **USD 15,076,460** (Option A) · **USD 15,321,068** (Option B) |

### Legal & Trust (Lines 2489–2514)

**New at v2.0** (D15); previously invisible in v1.0

| Line | Type | Priced? | Note |
|---|---|---|---|
| DIFC trustee company setup | One-off | **No** | Route 2 settled as DIFC not ADGM (decision 50) |
| **DIFC annual maintenance** | **Recurring** | **No** | **The most clearly missing line** — no home in v1.0 |
| Trust deed drafting | One-off | **No** | Only genuinely new legal work |
| Counsel batches | One-off, staged | **No** | 6 re-cut questions in composability; others in purchase structure, credit, licensing |
| **DFSA trust licence** | **Contingent** | **🔴 EXPLICITLY UNQUOTABLE** | May be exempt as single-trust trustee (medium confidence, mirror source) |
| Wind-down provision | Recurring, mandatory | **No** | Claim window, burn-on-redemption, freeze role (VARA VII.A) |
| Insurance | Recurring | Judgement | Booked in policy anniversary month |
| Contingency | Recurring | Judgement | Residual of v1.0's lump |

**Model as**: `legal_trust(t) = base_recurring(t) + IF(DFSA_LICENCE_REQUIRED, licence_cost, 0)`, with switch defaulting to exempt reading

---

## 6. FULL PARAMETER REGISTER

### F-Series (Fixed Inputs, §8.1)

| ID | Parameter | Value | Unit | Source category | Confidence | Sheet location | Notes |
|---|---|---|---|---|---|---|---|
| **F1** | Gold price (flat) | **141.46** | USD/g | CITED | High | Assumptions!B4 | Verified 2026-08-17; held flat by design |
| **F2** | AED/USD peg | 3.6725 | — | CITED | High | Assumptions!B5 | CBUAE peg |
| **F3** | Entry fee Y1/Y3/Y10 | 5.0 / 4.0 / 3.0 | % | CLIENT INPUT + DERIVED | Med | Assumptions!B6 | Falls with bar denomination |
| **F4** | Fabrication premium by denom. | **1.50 / 0.95** | % | OBSERVED | **MODERATE** (failed replication 2026-08-20) | Assumptions!B7 | 100g / 1kg; Good Delivery RETIRED; correction 36 |
| **F5** | Float cost of capital — MEMO | 0.49 / 0.31 / 0.38 | % | ASSUMPTION | Low | Assumptions!B8 | Removed from COGS (D32); **principal untouched** |
| **F6** | SIP hard floor | 20 | USD/month | CITED | High | Assumptions!B9 | Rejected outright, never partially credited |
| **F7** | Confirmed SIP gate | 6 | consecutive periods | CLIENT INPUT | High | Assumptions!B10 | Client's figure |
| **F8** | Grace period | 5 | calendar days | CITED | High | Assumptions!B11 | Rolls weekends/holidays; crosses month boundary |
| **F9** | Withdrawal allowance (R=1.0) | 30 | % per 12m | CITED | High | Assumptions!B12 | Decision 46 |
| **F10** | Collateral seasoning | 90 | days | CITED | High | Assumptions!B13 | Benefits draft §2.5 |
| **F11** | LTV ladder G/P/S | 50 / 65 / 80 | % | CITED | High | Assumptions!B14 | Settled 2026-08-13; no longer contingent |
| **F12** | Interchange G/P/S | 1.80 / 2.05 / 2.10 | % | CITED PRIMARY | **High** | Assumptions!B15 | Visa UAE IRF 18 Oct 2025 |
| **F13** | Gold Rewards cap | 3,000 | USD/month | TRIANGULATED | Medium | Assumptions!B16 | Kinesis-comparable |
| **F14** | VARA supervision Cat 1 | 200,000 | AED/yr | CITED PRIMARY | **High** | Assumptions!B17 | VARA's own rulebook |
| **F15** | Minimum paid-up capital | 1,500,000 | AED | CITED PRIMARY | High | Assumptions!B18 | Locked, not expensed; §7.6 funding view |
| **F16** | Sumsub Compliance | 299 + 1.85/check | USD/mo + per | CITED PRIMARY | **High** | Assumptions!B19 | Binds <162 checks/mo |
| **F17** | Referral reward | 30 | % of entry fee over run | CITED shape, ASSUMPTION value | Med | Assumptions!B20 | Placeholder; affordable at 399% per solver |
| **F18** | Referral payout lag | 6 | months after signup | CITED | High | Assumptions!B21 | Gate cannot compress |
| **F19** | Salary loading | 1.10 | × quoted total cash | DERIVED | Medium | Assumptions!B22 | Not 2.0×; guides quote base + allowances |
| **F20** | Cost per redemption event | **4.20 / 2.50 / 9.00** | USD | DERIVED | Medium | Assumptions!B23 | Payment 1.0–2.5 + re-screen 1.85 + handling 1.0–4.5 |
| **F21** | Card issuance fee G/P/S | 75 / waived / waived | AED one-off | CITED struct, ASSUMPTION rate | Low/High | Assumptions!B24 | Basis draft; rates unset |
| **F22** | Card replacement fee G/P/S | 100 / 50 / waived | AED per event | ASSUMPTION | Low | Assumptions!B25 | Market normal 75–150 |
| **F23** | Avg transaction size G/P/S | 185 / 240 / 310 | AED | ASSUMPTION | **Low** | Assumptions!B26 | Implies ~27/28/30 txns/mo |
| **F24** | Processor fee per txn | **0.10 / 0.05 / 0.15** | USD/auth txn | CITED | Medium | Assumptions!B27 | Stripe Issuing; +6% declines |
| **F25** | Dispute handling | 22 / 14 / 40 | USD/case | ASSUMPTION | Low | Assumptions!B28 | 0.9 cases/1k txns; scheme + internal |
| **F26** | Card production G/P/S | 4.50 / 7.00 / 14.00 | USD/card | ASSUMPTION | Low-Med | Assumptions!B29 | At Sovereign exceeds AED 0 fee by construction |
| **F27** | Card programme fixed | see cost table | USD | ASSUMPTION | **Low** | Assumptions!B30–35 | BIN/processor/Visa minimums; no UAE price list published |
| **F28** | Origination fee gross/share | **1.00% / 50%** | % / % | CITED gross, ASSUMPTION split | Med/Low | Assumptions!B36 | Finance House UAE gold loan KFS |
| **F29** | Servicing fee gross/share | **0.50% / 70%** | %/yr / % | ASSUMPTION | Low | Assumptions!B37 | Share high: Aurumix does actual work |
| **F30** | Penal fee gross/share | **2.00% / 40%** | % per late / % | ASSUMPTION | Low | Assumptions!B38 | Share low: Aurumix bears no credit risk |
| **F31** | Recovery fee gross/share | **1.50% / 0%** | % / % | ASSUMPTION | Low-Med | Assumptions!B39 | Modelled at zero (VARA III.E.4 recharacterisation risk) |
| **F32** | Opex interpolation | Log-linear within block on Y1/Y3/Y10 | — | DERIVED | Medium | Assumptions!B40 | Step/scale classification is substantive |
| **F33** | UAE corporate tax | **9%** above AED 375k; 0% at/below | % | CITED PRIMARY | **High** | Assumptions!B41 | Federal Decree-Law No. 47/2022 |
| **F34** | Loss carry-forward | Indefinite; capped 75% annual use | — | CITED | Med-High | Assumptions!B42 | Article 37, subject to continuity tests |
| **F35** | QFZP treatment | **Assume NOT QFZP. Tax at 9% from first profit** | — | DERIVED | Low-Med | Assumptions!B43 | Three reasons at Layer 11 |
| **F36** | VAT resident rate | 5% standard | % | CITED | **High** on rate, Low on line | Assumptions!B44 | Service fees to UAE residents |
| **F37** | VAT non-resident | 0% (export of services) | % | ASSUMPTION | **Low** | Assumptions!B45 | Unverified; three corpus files flag need tax opinion |
| **F38** | Float sizing rule | `MAX(2 bars, 1 bar + N days trailing)` | grams | CITED corpus-settled | **High** | Assumptions!B46 | `_draft_allocation-and-float.md`, verbatim |

### S-Series (Scenario Variables, §8.2)

| ID | Parameter | Base | Agg | Cons | Unit | Source category | Why it varies | Sheet |
|---|---|---|---|---|---|---|---|---|
| **S1** | Rail cost per collection — PASS-THROUGH (D31) | **0.25** | 0.10 | **1.36** | USD | TRIANGULATED | No longer margin driver; grossed onto request | Scen!A |
| **S2** | Persistency M13 survival | **55%** | 65 | 45 | % | DERIVED | Output of S27, not input | Scen!A |
| **S3** | PM share of gross IC | **72%** | 85 | 55 | % | TRIANGULATED | Sizes largest stream; **floor 36%** | Scen!C |
| **S4** | Card spend per active card | **6,000** | 9,000 | 3,500 | AED | TRIANGULATED | **Top load-bearing parameter** (USD 14.2M swing) | Scen!C |
| **S5** | Card activation rate | **65%** | 80 | 45 | % | TRIANGULATED | PULSE 68.2%, Monzo 68%; no primary | Scen!C |
| **S6** | Gold volatility | **25%** | 20 | 35 | % annualized | CITED | Drives price-gap; ~30% trailing 12m | Scen!A |
| **S8** | Credit take-up eligible | **18%** | 30 | 8 | % | DERIVED | Indian gold-loan <10%; pre-selection uplift | Scen!D |
| **S9** | Drawn % of permitted | **50%** | 70 | 30 | % | TRIANGULATED | Revolving facilities 40–55% | Scen!D |
| **S10** | Self-custody leakage | **12%** | 6 | 30 | % AUM/yr | ASSUMPTION | At v2.0 is aggregate S31 reconciles to | Scen!B |
| **S11** | Family plan attach | **20%** | 35 | 10 | % live | ASSUMPTION | **Pure assumption**; nothing stated | Scen!E |
| **S12** | Agent productivity | **4** | 6 | 2 | accts/agent/mo | TRIANGULATED | Insurance agency comparator | Scen!A |
| **S13** | B2B partner AUM Y10 | **200** | 400 | 50 | USD m | ASSUMPTION | Requires signed partner | Scen!E |
| **S14** | Vault storage | **0.25** | 0.15 | 0.40 | % AUM/yr | CITED | Verified range; minimum binds <250kg | Scen!F |
| **S15** | Marketing CAC base | **120** | 80 | 200 | USD | ASSUMPTION | No UAE benchmark; modified by S25 curve | Scen!A |
| **S16** | Channel→region mix 🆕 (D25) | three-phase tables | 8pp toward R1 | 10pp toward floor | % | ASSUMPTION | No published comparables; two structural rules matter | Scen!A |
| **S17** | Agent ramp M1–M13+ | .20/.40/.60/.75/.85/.95/1.00/1.05 | .35→1.15 | .10→.95 | × S12 | ASSUMPTION | Insurance-agency ramp; matches gate timing | Scen!A |
| **S18** | Agent annual attrition | **45%** | 30 | 60 | %/yr | TRIANGULATED | Indian life-agency 40–60% Y1 | Scen!A |
| **S19** | Referral rate | **0.45** | 0.90 | 0.18 | refs/qual/yr | ASSUMPTION | Cap removed; right-skewed distribution | Scen!A |
| **S20** | Referral conversion | **62%** | 72 | 48 | % | DERIVED | M7 survival of referred cohort uplifted ~1.1× | Scen!A |
| **S22** | Regional ceiling R1–R4 🆕 (D25) | **9.5 / 6.0 / 4.0 / 0.35** | 14 / 9 / 6 / 0.60 | 6 / 3.5 / 2.5 / 0.15 | % | ASSUMPTION | Applied to active IBAN-capable income-qualified; invariant 165,750 total | Scen!A |
| **S23** | Saturation on remaining | Logistic on cumulative-ever-acquired | | | — | DERIVED | Use cumulative-ever-acquired ÷ ceiling, not live accounts (~5× difference) | Model |
| **S25** | CAC diminishing returns | **OFF. Linear** | OFF | OFF | — | DEMOTED (D27) | Curve `S15 × [1 + 0.35 × (spend÷60k)^0.7]` preserved as scenario; default linear | Scen!A |
| **S26** | Organic direct share | **12%** | 20 | 5 | % | ASSUMPTION | Kept separate so CAC curve not applied | Scen!A |
| **S27** | Archetype weights + hazards | **10/35/12/13/30** + bg | see D3 | see D3 | % / hazard | DERIVED aggregate, ASSUMPTION decomp | **Rank 5 load-bearing** (1.9M swing); fitted to §0.5 curve | Scen!B |
| **S28** | Reduction capture | **33%** | 50 | 18 | % lapses | ASSUMPTION | v1.0 illustrative third preserved; affordability lapse only | Scen!B |
| **S29** | Reduction depth | **MAX(20, 50% prior)** | 65% prior | Straight 20 | USD/mo | ASSUMPTION | Corrects v1.0 error; **D25: standard band only** (floor already at floor) | Scen!B |
| **S30** | Hazard multiplier REDUCED | **1.35×** | 1.15× | 1.75× | × monthly | ASSUMPTION | Well above 1.0 or free retention; below 1σ or state does no work | Scen!B |
| **S31** | Withdrawal behavior dist. | six buckets straddling 30% kink | as tabled | as tabled | % | ASSUMPTION | **Straddling 30% Retention kink** | Scen!B |
| **S32** | Redemption rate | **8%** | 4 | 16 | % AUM/yr | ASSUMPTION | Below self-custody (on-chain frictionless); different event from S10 | Scen!B |
| **S33** | Lapsed-holder mult. | **2.2×** | 1.6× | 3.5× | × rate | ASSUMPTION | **Rank 4 load-bearing** (~81% of cohorts lapsed by M61); v1.0 has no term | Scen!B |
| **S34** | Foreign spend share | **34%** | 45 | 24 | % | ASSUMPTION | **Apply as S53 seasonal vector**, not constant | Scen!C |
| **S35** | ATM distribution | 950 mean, six-bucket | 1,600 | 500 | AED/mo | ASSUMPTION | Deliberately below Gold 1k allowance; distributional treatment critical | Scen!C |
| **S36** | Issuance event rate | **1.00 activate + 0.06/yr** | +0.04 | +0.10 | events/card/yr | ASSUMPTION | Tier upgrade forces reissue | Scen!C |
| **S37** | Replacement event | **0.11** | 0.07 | 0.18 | /card/yr | ASSUMPTION | Loss/theft/damage ~8–15% annually | Scen!C |
| **S38** | Spend tier multipliers G/P/S | **0.82 / 1.12 / 1.54** | .85/.10/1.45 | .78/1.15/1.70 | × S4 | DERIVED | Normalises to 1.018 at Y10 mix | Scen!C |
| **S39** | Fraud & chargeback | **9 bps** | 5 | 22 | bps | CITED + ASSUMPTION | Visa global avg ~8 bps; no UAE issuer rate | Scen!C |
| **S40** | Turnover correction | **0.42** | 0.55 | 0.30 | × peak | DERIVED | 71-day realised tenor; **rank 12th measured** (was 2nd a priori) | Scen!D |
| **S41** | Draw events/borrower/yr | **2.1** | 3.2 | 1.3 | events/yr | DERIVED | Moves with S40; do not flex independently | Scen!D |
| **S42** | Partner count by year | **1/2/3/4/6/8** | 1/3/5/7/11/15 | 1/1/1/2/2/3 | partners | ASSUMPTION | Enterprise sales cadence | Scen!E |
| **S43** | Per-partner AUM ramp | **8/25/48/70/85/100% at M6/12/24/36/48/60** | 100% M42 | 100% M84 | % terminal | ASSUMPTION | Standard enterprise integration adoption | Scen!E |
| **S44** | Terminal AUM per partner | **32** | 45 | 22 | USD m | DERIVED | Reconciles to S13 within ~5% | Scen!E |
| **S45** | Spot attach | **14%** | 24 | 7 | % live/yr | ASSUMPTION | **Rank 9 load-bearing** (167M swing); **missing, not large** | Scen!B |
| **S46** | Avg spot ticket | **620** | 1,100 | 320 | USD/event | ASSUMPTION | Scale by segment: S1/S6 ×1.6, S2/S4 ×1.0, S3 ×0.45, S5 ×0.7 | Scen!B |
| **S47** | Spot frequency | **1.7** | 2.4 | 1.2 | events/attacher/yr | ASSUMPTION | ~45% in festival windows | Scen!B |
| **S48** | Y1 exit run-rate | **1.40×** | 1.25× | 1.60× | × booked | ASSUMPTION | Y1 is partial year; run-rate corrects for incomplete hiring | Scen!F |
| **S49** | Resident share by region 🆕 (D25) | **100 / 100 / 0 / 0** | same | same | % UAE | DERIVED definitional | Falls out of D31 re-cut by residence | Scen!F |
| **S50** | Float buffer days | **10** | 6 | 20 | days trailing | ASSUMPTION | Corpus rule states N without setting it | Scen!F |
| **S51** | Float carry mode 🆕 (D29) | **OWN FLOAT FROM M1** | dealer-throughout | own M1 | — | DERIVED (forced) | Three comparables' routes all closed; premium narrows accordingly | Scen!F |
| **S52** | Seasonality vectors (a) acquisition (b) spend | amplitude ×1.0 | amplitude ×1.4 | amplitude ×0.6 | **normalised to 12.00** | CITED drivers, ASSUMPTION amplitude | Festival timing not disputed; responsiveness is | Scen!F |
| **S53** | Foreign-spend seasonal | 30/30/30/32/34/**55**/**60**/**56**/36/42/40/32 rescale to 34% | — | — | % | ASSUMPTION | Summer travel peak in weak total-spend month | Scen!C |
| **S54** | Floor share by region 🆕 (D25) | **40 / 60 / 58 / 25** | 30/50/48/18 | 50/70/68/33 | % at USD 20 | ASSUMPTION | **Saves two non-linearities** (rail + card spend) | Scen!A |
| **S55** | Avg ticket by region 🆕 (D25) | **38 / 26 / 26 / 30** | 46/32/32/36 | 30/21/21/24 | USD/mo | TRIANGULATED | Savings-capacity anchored; book-weighted **31.5 average** (was ~40, tightens fee) | Scen!A |

### T-Series (Time-Evolving Inputs, §8.3)

| ID | Parameter | Y1 | Y2 | Y3 | Y5 | Y10 | Pattern | Source category | Notes |
|---|---|---|---|---|---|---|---|---|
| **T1** | Entry fee base | 5.0% | 5.0% | 4.0% | 4.0% | 3.0% | Step with bar denom | CLIENT INPUT | D9 |
| **T2** | Fabrication premium | 3.00% | 3.00% | 2.00% | 2.00% | 0.75% | Step with bar denom | ASSUMPTION | **Now 1.50 / 0.95 at D28** |
| **T3** | Bar denomination | 100g | 100g | **1 kg** | 1 kg | **1 kg** | Threshold on trailing inflow, latched | DERIVED | **12.4kg RETIRED** (D28); Dubai std 1kg; endogenous latch |
| **T4** | Tier mix Gold+ share | 0.0% | 15.7% | 25.0% | 41.2% | **63.0%** | Computed by ICS per archetype, weighted | **OUTPUT** | v1.0 listed as input (D2) |
| **T5** | Tier mix Sovereign share | 0% | 0% | 0% | 0% | **4.4%** | First Sovereign at M61 | **OUTPUT** | v1.0 carried as input (D2) |
| **T6** | PM share maturity | — | 55% | 55% | 72% | 72% | Steps at scale | ASSUMPTION | Use Low for M18–M30 |
| **T7** | Active agents | 5 | 15 | 40 | 90 | 200 | Stock | CLIENT INPUT | Gross up by S18 attrition into recruit flow |
| **T8** | Non-resident book share | 0% | {{UNFILLED}} | {{UNFILLED}} | {{UNFILLED}} | ~42% (**withdrawn pending rerun**) | Computed from segment ramp × S49 | **OUTPUT** | v2.1's 42% superseded by D25 re-cut |
| **T9** | Float capital own-float | ~29k | {{UNFILLED: launch dealer, float zero}} | ~437k | ~291k (M60) | ~3.6M | Computed F38 × T3 × F1 | DERIVED | At v2.0 ten-year: ~3.1M at M84 |
| **T10** | Cumulative-ever-acquired ÷ live | ~1.1× | {{UNFILLED}} | {{UNFILLED}} | {{UNFILLED}} | **~5×** | Saturation denominator | **OUTPUT** | Sanity check on S23 |

---

## 7. THE SOLVER (§9)

**Seven parameters solved rather than input** (Lines 2839–2851):

| # | Parameter | Phase 2 statement | **v2.0 solve result** | Target |
|---|---|---|---|---|
| **1** | **Entry-fee uplift to fund discount ladder** | Ceiling 1.5pp exceeds 0.72% margin (now obsolete framing) | **0.696pp** book-weighted at Y10 mix; ladder self-funds at Y1 headline 5.0% | 1.5pp ceiling applies only to 4.4% Sovereigns |
| **2** | **Acquisition budget ceiling** | Board-approved cap, % of entry-fee revenue, IRDAI-modelled | **29.1% of TOTAL revenue** (338% of entry-fee revenue is meaningless) | Breakeven LTV:CAC per channel |
| **3** | **Referral reward size** | 30% placeholder; shape settled | **Affordable at 399% of referee entry fee**; LTV does not bind | All-streams LTV 752–949; entry-fee LTV 5.62–42.55 |
| **4** | **Agent commission rate** | 15% of dead base; transplanted = 88% Y1 margin | **USD 175.68/account** (46.85 / 58.56 / 70.27 three-level) | Item 2 ceiling & LTV:CAC floor 1.0 |
| **5** | **B2B platform fee rate** | 0.5–0.75%/yr placeholder | **35 bps floor (vault 25 + 10 margin); modelled 60 bps** on Y10 partner AUM 215M = 1.29M/yr | SafeGold margin precedent; zero entry spread |
| **6** | **Family plan price** | USD 29–36/yr + USD 20/name awaiting sign-off | **USD 32/yr + USD 20/name** corpus midpoint, against USD 2.35/name floor (~5× headroom) | Cost floor + 20–40yr screening tail |
| **7** | **Minimum viable PM share** | Phase 2 floor 36%; commercial rate unresolved | **Floor 36% at Sovereign (0.75÷2.10=35.7%, verified); commercial 77.5% on 10-year reach EBITDA+** | Self-funding Gold Rewards at Sovereign |

**Solver item 1 revised** (§9.2, lines 2853–2875):
- Entry-fee uplift required is **zero at Y1 and Y2** (5.0% headlines cover 4.96% minimum viable fee)
- Never-gated population (18.7% at Y10) pays full fee forever, zero benefits
- Pre-gate window averages 8.1 months full-fee revenue per cohort before first discount
- **Book-weighted discount at Y10 tier mix: 0.696pp**—less than half the 1.5pp Sovereign ceiling
- **Answer: the ladder is already funded at the headline; problem is the fee step down, not the ladder**

**Solver item 8 struck** (§9.3, lines 2876–2891):
- Tenure rebate **retired by decision 44**, not merely unsized
- v1.0 confused three error sources: the 0.10–0.75% range is **Gold Rewards**, the ~1.5% is **prohibited redemption fee**
- **Build saving: no FIFO lot accounting needed** (decision 41 makes grams fungible)

**Solve order** (§9.4, lines 2899–2911):
1. **Item 1 — the uplift** (upstream of everything)
2. **Item 7 — PM share floor** (constraint, not variable)
3. **Item 2 — acquisition ceiling** (% of now-fixed stream 1)
4. **Items 3 & 4 — jointly** (alternative uses of same capped pool, not independently)
5. **Item 5 — B2B rate** (outside ceiling entirely)
6. **Item 6 — family plan price** (independent)

---

## 8. SCENARIO ARCHITECTURE (§13)

### Three Layers (Lines 3839–3843)

| Layer | What | Usage |
|---|---|---|
| **1. Global switch** | Base / Agg / Cons across all scenario parameters | Bounding cases; NOT forecasts |
| **2. Per-parameter override** | Any parameter set independently; global switch flips to CUSTOM | Working mode; real questions |
| **3. Named narrative scenarios** | Stored vectors per parameter, named, storied | Client-facing; repeatable |

### Five Named Scenarios (Lines 3847–3856)

| Name | The story | Key parameter changes | Finding |
|---|---|---|---|
| **Rail kills it** | AANI unavailable or UAEDDS priced | S1 → 1.36 (Cons); rest Base | Cumulative loss −15.5M (vs −14.1M Base); peak funding 16.4M (vs 15.1M); Y10 revenue unchanged |
| **Card works, savings doesn't** | Card lands well; SIP persists poorly | S2 → 45%, S27 → Cons mix; S3/S4/S5 Base+ | Most likely real outcome; does card carry shrinking book? |
| **🔴 No card** | Sponsor bank doesn't sign; prepaid-only at 1.00% cap | `PREPAID_VS_CREDIT` → prepaid OR activation → 0 | **Most important missing scenario; removes majority of revenue** |
| **Distribution fails** | Agents underperform; referral never compounds | S12 → 2, S17 → Cons, S18 → 60%, S19 → 0.18, S25 → Cons | Paid direct alone at what CAC? |
| **Client's plan** | Imposed 100k Y10 target, rest Base | Account count forced to trajectory | Reached 54k live, 17.7M revenue, cumulative loss 7.2M Y10; **did not turn inside 7-year window** |

### 🔴 India Scenario (Line 3854–3856)

- Switch `INDIA_ENABLED` → OFF
- S44 & S42 fall with it (coupled, not independent)
- Y10 revenue falls to 6.1M (delta −2.03M, −24.9%)
- Peak funding rises to 18.5M
- **Must also move stream 6 AUM when India segment off**

### Binary Switches (Not Sensitivities, §13.3)

| Switch | Default | ON does what | Size | Why it's a switch |
|---|---|---|---|---|
| `PREPAID_VS_CREDIT` | **Credit** | Caps IC 1.00%, removes credit facility | −2.3M Y10 revenue; −7.3M cumulative profit | **Not a product choice; it's the business model** |
| `LAPSED_KEEPS_CARD` | **ON** | Lapsed retain card and facility | Y10 revenue 4.8M (−3.4M); loss −5.2M cumulative profit | 🔴 **Nobody has decided**; determines if majority of revenue decays |
| `INDIA_ENABLED` | **ON** | S5 segment live; stream 6 full S44 | S44 → 40% Base, S42 → Cons (coupled) | Prices India as market; doesn't assert route exists |
| `OPTION_B` | **OFF** | 2%-of-Reserve-Assets escalator on capital | Peak funding +245k; capital +387k locked | Under Option A, line flat—**that's the point** |
| `DEALER_CARRIED` | **ON at launch, OFF from Y3** | Float 0, F5 0, spread 0, premium wider | 🔴 **Charging both sides = double-count, error not sensitivity** | Own float forced from M1 (D29) |
| `SUBDECISION_2` | **OFF** | Compliance exit does NOT zero Retention | Report S5 tier delta as **client's decision cost** | Open question (D5) |
| `DFSA_LICENCE_REQUIRED` | **OFF** (exempt reading) | Adds unpriced annual licence cost | **Unquotable** | Medium confidence on exemption |
| `ENFORCEMENT_SALE_IS_REDEMPTION` | **ON** (safe reading) | Recovery fee → 0 | Already modelled zero in Base; prices upside | Counsel question 1 |
| `EQUAL_VALUE_FULL_PREVAILING` | **ON** (safe reading) | Aurumix absorbs two-way spread on exits | Full prevailing value vs realisable value | **Difference is entire spread; decides incidence** |
| `TRADEFLOW_1KG` | **OFF** | Launch bar forced to 1 kg | 10× launch capital step (~29k → ~285k) | Warrants from launch; real trade-off |

### Book-State Axis (§13.4, lines 3879–3886)

| Book state | Inflow | Exits | Net | Spread cost | Status |
|---|---|---|---|---|---|
| **Growing** | 8% AUM | 3% | +5% | **Zero** | Base case |
| **Flat** | 4% | 4% | 0% | Zero | Scenario |
| **Shrinking** | 2% | 6% | −4% | On the 4% net | Scenario |
| **Run** | 1% | 25% | −24% | On the 24% net | **Stress test** (not scenario); report float breach, settlement tier, spread cost |

### Tornado Specification (§13.5, lines 3892–3906)

**Two tornados** (lines 3893–3895):

1. **Y10 net profit after tax**: All scenario parameters, Agg/Cons bounds. **Measured ranking** (line 3899):
   - S4 card spend: USD 14,177,704
   - S5 card activation: 6,539,376
   - S3 PM share: 6,359,822
   - F27 card programme: 2,125,500
   - S27 archetype mix: 1,906,962
   - S1 rail: 1,607,643
   - S11 family: 694,515
   - S14 vault: 359,350
   - S45 spot: 167,891
   - S10 leakage: 149,353
   - S8 credit: 56,569
   - S40 turnover: 17,519
   - S48 Y1 exit rate: 1,975

2. **Peak funding**: Same parameters; charts against peak cumulative deficit. **Measured ranking** (line 3901):
   - S4, S5, S3, F27, S1 (swapped with S27), S27, S11, S14, S45, S10, S8, S40, S48

**Key finding** (line 3903): **Two tornados rank differently**. Rail is 6th on profit, 5th on funding (bites from month 1 on collections). Persistence compounds into later years (terminal profit). **Parameter rank depends on which question is asked.**

---

## 9. CHECKS & INVARIANTS (16 Checks, §3.x.4, lines 1193–1202)

1. **Circular-reference canary**: Report workbook's iterative-calculation setting (visible, not hidden)
2. **Dependency-order test by sheet NAME** (NOT tab position after D26): No formula references sheet later in §3.x.1 order. **Including: no Model formula may reference ICS Validation; nothing on Cover except Checks master**
3. **Hidden-sheet inventory**: Five must-hide (Time Series, Lifecycle Curves, Acquisition, ICS Validation, Checks); five must-visible (Cover, Assumptions, Scenario Parameters, Model, Summary)
4. **Cover master-flag integrity**: `ALL CHECKS PASS` cell reads Checks master row by formula, not typed value
5. **Lag integrity**: `acquisition_budget` reads prior period (one month in monthly block, one year in annual); never current period
6. **Denomination monotonicity**: `bar_grams(t) ≥ bar_grams(t−1)` for all t (latch; never step down)
7. **Convolution range integrity**: Every `SUMPRODUCT` terminates acquisition range at current period, never beyond; curve range reversed against it
8. **Annual-column decomposition**: Each annual column's population = sum of 12 monthly convolutions, not single convolution on annual aggregate
9. **Circular-chain test (acquisition→fee→budget)**: No retroactive loop via lagged budget structure
10. **Lapsed-holder decay**: Leakage feeds `Sold` → `Retention` → tier (arrow v1.0 omits; D11)
11. **Pre-gate benefits**: Never-gated share receives zero benefits but pays full fee forever
12. **Rail not in P&L**: `rail_memo` appears in no revenue or cost total (D31)
13. **Float carry not in margin**: `floatcoc_memo` appears in no COGS, margin or P&L total (D32)
14. **Base × ceiling invariant**: Total accounts 165,750 held across all regions (moved together when propensity filter deleted)
15. **ICS Validation as leaf**: Read only by Checks; never referenced by Model (collapse would be silently un-done)
16. **Gross margin before rail**: Formula verification: `C − C(1−f)(1+p)` = USD 1.61 on USD 75 at 5% fee, 1.50% premium ✓

---

## 10. CONTRADICTIONS & DISCREPANCIES

🔴 **LIVE CONTRADICTION FOUND** (Correction 26, line 4096): 

**§3 Layer 4 and §6.1b both state gross margin 0.72%** for stream 1 before rail at Y1 5% fee with 3.00% premium. **§6.1's waterfall gives 2.15%**, which nets to 0.87% after price-gap/float. The 2.15% line is **arithmetically correct** (audited against `C − C(1−f)(1+p)` = USD 1.6125). **The 0.72% is incorrect and must be corrected to 0.87% before model re-run.**

🔴 **REPLICATION FAILURE** (Correction 36, line 4106):

**D28's premium measurement failed replication 2026-08-20.** Same-page dealer (goldtrade.ae) captured at 1.71 / 0.93 % on 2026-08-19 19:52 returned 4.14 / 3.37 % on 2026-08-20 24 hours later. **Diagnostic**: rate page moved 6 bp overnight; store page moved 241 bp—not a shared clock. **What survives**: the 1 kg-vs-100g step (0.77–0.78 pp) is independently corroborated. **What's withdrawn**: F4's absolute level. **Every fee-fundability reversal (D31, D32, §0.3) is provisional** until F4 re-observed.

🔴 **F4 CONFIDENCE DOWNGRADE** (Line 1613):

F4 moved from **Critical** to **Moderate** in §16. The ladder's *shape* (monotonic decline with denomination) is observed and corroborated. The *absolute level* is not.

🔴 **D31/D32 CUMULATIVE RECLASSIFICATION RISK** (Correction 38, line 4108):

In one day, `c` went from four terms (premium, gap, float CoC, margin) to two (premium, gap), and minimum viable fee fell **3.07% → 2.74% → 2.26%** with nothing changing in the business. Each step defensible separately; **the sequence dissolved §0.3's entire finding by re-attribution alone.** ⚠ **Before carrying any fee reversal to client: adversarially re-check both surviving terms and re-observe F4. State the reversal as conditional.**

🔴 **CORRECTION 30 UNDESIGNED** (Line 460):

D30 (premium on net new grams, not gross) **holds only if redeemed gold returns to float**, not to dealer. **Nobody has written this down.** Interacts with buyback mechanics and backing invariant. **Settle before building.**

🔴 **D31 / D32 ORDER DEPENDENCY** (Lines 512–516):

D31 removes rail from entry-fee margin (reverses §0.3). D32 removes float CoC from COGS (improves margin again). **If only D31 were implemented, margin falls and §0.3 holds.** Sequence matters for the narrative. **Must be presented as jointly dependent.**

---

This completes the normative build specification extracted from the architecture brief and supporting decisions.