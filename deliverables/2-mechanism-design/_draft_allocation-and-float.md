# Mining Events, Allocation and the Gold Float

> **Status: first draft, 2026-07-28.** Skeleton only. To be expanded to full MD depth (numbered steps, worked examples, edge cases) and folded into the Mechanism Design document.

## The problem

Aurumix promises three things that do not fit together without a fourth mechanism:

- 100% allocated, unencumbered physical gold
- a $20 monthly minimum contribution
- wholesale gold pricing

Wholesale gold comes in lumps. The smallest practical unit is a 100 g bar (~$10,900); the working unit is 1 kg (~$109,000); LBMA Good Delivery is 12.4 kg (~$1.36M). At Year 1 the SIP book buys roughly **11 grams a day**, so a 100 g bar takes ~9 days to fill and a 1 kg bar takes ~88 days. You cannot buy 11 grams of allocated bullion at wholesale.

The client's "Mining Event" is a treasury batching artifact with a marketing name, plus an unrelated scarcity mechanic welded on. Separate the two: the batching problem has an engineering answer, and the scarcity mechanic is deleted (see "Why Mining Events don't work" below).

## The gating dependency: the procurement channel in our jurisdiction

**Everything in this section is downstream of one unresolved question: who sells Aurumix gold in Dubai, on what terms, and will they carry inventory.** The 100 G Business Model names a vault three times and a seller zero times. Until that counterparty exists, the allocation mechanism cannot be specified, the entry fee cannot be built up, and the buyback promise has no route.

This is not a research gap that more desk work can close. Dubai's wholesale gold market is commercially opaque by convention: **premiums, two-way spreads, minimum tickets, allocation costs and DMCC Tradeflow fees are published by nobody.** Three separate research passes returned the same negative result. It needs a dealer conversation.

**What the procurement channel determines, in order:**

1. Whether the float is **carried by the dealer or by Aurumix** (below). This is the largest single design fork in the section.
2. **Bar denomination at launch**, and therefore fill window, float size and fabrication premium.
3. **The entry fee**, which is a build-up from premium + spread + price-gap risk + cost of capital + margin. None of the first four are knowable without a quote.
4. **The buyback**, which requires the same dealer on a two-way basis. Physical delivery is excluded, so cash buyback is the only exit and it runs entirely through this counterparty.

## How the category solves it

Every physically-backed protocol in the landscape bridges the small-ticket-to-bar gap one of five ways, and the route each one takes is a direct consequence of the procurement channel it has access to.

| Pattern | Who | Mechanism | Open to Aurumix |
|---|---|---|---|
| **A. Metal-first.** Mint only after gold is vaulted; a dealer carries the inventory | **Aurus**, Midas XGZ, CACHE Gold, PMGT, Kinesis (EPD route) | Dealer or depositor delivers metal, vault confirms, then tokens mint. Retail never mints | **Yes, and this is the leading candidate** |
| **B. Agency purchase.** Issuer buys per order on the customer's behalf | Kinesis (mint route), VNXAU, XAUm | Kinesis cl. 4.1.1: "will cause an equivalent amount of Bullion to be purchased on your behalf". **How sub-bar orders are netted is disclosed by none of them** | Possible, undocumented anywhere |
| **C. Wholesale primary, retail secondary.** Never face a small ticket | XAUT (50 oz), DGLD (400 XAU / ~$1.6M), Midas XGZ, MG999 (100k USDT), Streamex ($200k) | DGLD is instructive: MKS PAMP's own trading arm is the principal market maker, so the group's book absorbs the lumpiness | **No.** It negates the business |
| **D. Mint ahead of the gold** | **Comtech, alone** | T&C 3.5 permits a **10 kg unbacked window**. Retail entry 0.5 g, issuer-quoted price, ~1.8% round-trip spread | Possible, but concedes the token is not fully backed at all times |
| **E. Closed loop, no public mint** | WTGOLD | No primary market, no AP structure. Absorbed by a $150bn listed parent | **No.** No parent |

Also unavailable: **staying matched via an unallocated market** (PAXG's route, and Dubai has no documented unallocated wholesale layer; an unallocated balance is an unsecured claim on the provider, which breaks "100% allocated and unencumbered"), and **vertical integration** (DGLD / MKS PAMP owns the refinery).

**Two reference points worth carrying.** XAUm discloses **T+3** delivery, the only published batching window in the set, so a T+1 allocation target would be tighter than the category benchmark. And retail entry sizes do exist (VNXAU no minimum, Comtech 0.5 g, PAXG 0.03 to mint), but **recurring contribution exists in zero of nineteen protocols** and **zero disclose the window between money received and metal allocated.** The combination of retail ticket size, recurring contribution and full allocated backing is unsolved.

## The mechanism: a gold float

A **float** is working inventory on the metal side, owned outright by Aurumix from its own capital. It is not a reserve: it is not held instead of backing, and it is not a redemption buffer.

- Investor funds clear. Grams are struck at the **first LBMA AM fix after cleared funds (T+1)**.
- Those grams transfer **out of the float into allocated investor holdings** the same day. The metal already exists, is already vaulted, already has a serial number.
- The treasury replenishes on a **threshold trigger** when cumulative drawdown reaches one bar denomination.
- Steps 3 and 4 are invisible to the investor, surfaced only via a monthly Allocation Report.

**The float decouples the investor's ticket size from the treasury's purchase size.** The investor buys 0.18 g; the treasury buys 1 kg. This is what allows a $20 minimum where PAXG needs $120 and XAUT needs $170,000.

### Who carries it: the fork that the procurement channel decides

The float has to exist. **Who funds it is open, and it is decided by what the dealer will agree to.**

**Option 1: dealer-carried (the Aurus model, Pattern A above).** Aurus's structure is that a **Provider Partner, a licensed bullion trader**, sends bullion to an approved vault, the vault audits and authorises minting, tokens mint at 1 per gram against a 0.5% tokenization fee, and the trader owns both the metal and the tokens and sells them on. Aurus states plainly that it "does not supply precious metals to the ecosystem nor sell tokens to end consumers." **The dealer is the float.** Applied here: the dealer holds inventory, Aurumix draws grams daily at an agreed spread and allocates immediately. Same investor experience, same T+1, same invariant.

**Option 2: own float.** Aurumix posts the capital and runs the inventory itself.

| | Dealer-carried | Own float |
|---|---|---|
| Working capital | **Zero** | ~$22k at Y1, ~$330k at Y3 |
| Price-gap risk | Dealer's | Aurumix's, under 0.4% (below) |
| Cost | Wider dealer spread | Narrower once at scale |
| Risk | **Single-counterparty dependency**; the dealer can withdraw | Operational and capital |
| Control | Dealer sets terms | Aurumix sets terms |

**Working recommendation: launch dealer-carried, migrate to an own float once volume makes internalising the spread worth the capital.** Same crossover logic as the denomination upgrade rule below. It removes the working-capital objection at launch entirely.

⚠ **Note what this does to the counterparty risk.** Under an own float the dealer is important. Under a dealer-carried float at launch, **the dealer is the mechanism itself.** That raises the priority of naming one, it does not lower it.

⚠ **Copy Aurus's structure, not its paperwork.** Its partner economics live in a whitepaper, its only legal document is a four-page website terms page naming no entity and no governing law, and the fee split has changed three times under upgradeable contracts.

### It does four jobs, not one

1. **Lumpiness.** Absorbs the mismatch between daily inflow and bar denomination.
2. **Price risk.** Moves the timing gap off the investor (currently up to 30 days, ~4.3% 1-sigma) and onto Aurumix over the fill window only.
3. **Live pricing.** Makes a firm, auditable, third-party price quotable at the point of sale, which is what makes the peg formula (grams ÷ tokens) trustworthy.
4. **The buyback.** Absorbs exit flow in reverse, so Aurumix is not forced to sell a physical bar to a dealer on demand. This closes the gap in §3.2 of the client's document, where the buyback is said to be funded by "the custodian liquidating exactly those grams" and custodians do not liquidate.

## Sizing

Rule: **float ≥ one bar denomination + a buffer of N days' trailing inflow.** Two bars is the launch setting.

| | Investors | Monthly inflow | Grams/day | Bar | Days to fill | Float (2 bars) | Float in $ | % of AUM |
|---|---|---|---|---|---|---|---|---|
| Y1 | 500 | $37,500 | ~11 | 100 g | 8.7 | 200 g | ~$22k | ~5% |
| Y3 | 12,000 | $900,000 | ~274 | 1 kg | 3.6 | 3 kg | ~$330k | ~2% |
| Y10 | 80,000 | $6,000,000 | ~1,830 | 12.4 kg | 6.8 | 24.8 kg | ~$2.7M | <1% |

- Affordable at launch: ~$22k, against a VARA minimum capital requirement of AED 1.5M (~$408k) that must be posted anyway. **[COUNSEL]** whether allocated gold inventory can sit inside that requirement.
- **Float as a share of AUM falls as the business scales.** It is a fixed operational requirement, not a proportional drag.
- **The float is not a cost, it is what buys the wholesale price.** Fabrication premium runs 2 to 5% on 100 g, 1 to 3% on 1 kg, under 1% on Good Delivery. Bar size is the margin dial and float size unlocks bar size.

### Denomination upgrade rule

Upgrade when **(annual gram volume × premium saved per gram) > (incremental float × cost of capital) + incremental price-gap risk**.

Worked: at Y3, moving 1 kg to Good Delivery saves ~1.25% on $10.8M of annual purchases (~$135k/yr) for ~$1.2M of extra float, an ~11% return on incremental capital. It clears. The same calculation fails at Y1, which is why 100 g is right at launch.

**Tension to resolve:** DMCC Tradeflow specifies eligible collateral as 1 kg 999.9 bars. If warrants are wanted from launch, 1 kg becomes the effective floor and the launch float rises to ~$220k. Real trade-off, and a client decision.

### Price-gap risk carried by the float

The float is structurally short over the fill window: it sells grams at today's fix and replaces them later. At ~15% annualised gold vol:

| | Fill window | 1σ over window | Per cycle | Annual σ | % of purchases |
|---|---|---|---|---|---|
| Y1 | 8.7 d | 2.3% | ±$257 | ~$1.6k | ~0.36% |
| Y3 | 3.6 d | 1.5% | ±$1.6k | ~$16k | ~0.15% |
| Y10 | 6.8 d | 2.1% | ±$28k | ~$204k | ~0.28% |

Under 0.4% at every stage, against an entry fee of 2 to 5%, and mean-zero rather than a systematic loss.

## Worked example: one $75 contribution, Year 1

Assumptions: gold $3,400/oz = **$109.31/g**, **1 AURX = 1 g**, launch denomination **100 g bars**, fabrication premium plus dealer spread **3.0%**, entry fee **5%** (justified below), dealer-carried float.

### The flow, step by step

| # | Step | Actor | Detail |
|---|---|---|---|
| 1 | **Contribution Date** | Investor | Own anniversary date, not a collective date. $75 debited via UPI or bank transfer |
| 2 | **Funds clear** | Payment provider | T+0 to T+1. On failure, 15-day grace opens; after grace, ICS consequences only, no financial penalty |
| 3 | **Entry fee deducted** | Aurumix | $75.00 × 5% = **$3.75**. Net to gold **$71.25** |
| 4 | **Allocation price set** | LBMA | **First LBMA AM fix after cleared funds (T+1).** Benchmark price, published, auditable |
| 5 | **Grams struck** | Aurumix | $71.25 ÷ $109.31 = **0.651815 g** |
| 6 | **Grams transferred from float** | Dealer / vault | Metal already exists, already vaulted, already serial-numbered. Investor holding moves from float to allocated |
| 7 | **AURX minted** | Contract | **0.651815 AURX**, since 1 AURX = 1 g. Gold Receipt issued recording a pro-rata undivided interest in identified bars |
| 8 | **ICS accrues** | Aurumix | Contribution counts toward tier progression and Confirmed SIP streak |
| 9 | **Float drawdown recorded** | Treasury | Float short by 0.651815 g. Backing invariant re-checked |
| 10 | **Threshold check** | Treasury | If cumulative drawdown ≥ 100 g, trigger procurement. At ~11 g/day this fires roughly every **8.7 days** |
| 11 | **Bar procurement** | Dealer | Buy 100 g bar at fix + premium. Independent assay on intake. Vault receipt. Tradeflow warrant registered if in scope |
| 12 | **Monthly Allocation Report** | Aurumix | Bar serials, assay certificates, grams struck, fixes used, float balance, allocated balance |

Steps 9 to 11 are invisible to the investor. Steps 1 to 8 complete inside **24 hours of cleared funds**, against the category's only published benchmark of **T+3 (XAUm)**.

### The money, same contribution

| Line | % of contribution | $ |
|---|---|---|
| Contribution received | 100.00% | $75.00 |
| Gold cost (95% net × 1.03 premium) | (97.85%) | ($73.39) |
| **Gross margin** | **2.15%** | **$1.61** |
| Price-gap risk (Y1, 1σ) | (0.36%) | ($0.27) |
| Float cost of capital | (0.49%) | ($0.37) |
| Payment rail (UPI / bank) | (0.30%) | ($0.23) |
| **Net contribution margin** | **~1.00%** | **~$0.75** |

Not yet deducted: per-account admin and KYC amortisation (**[CLIENT]** input needed), and custody, which is a charge on stock rather than flow and must be recovered separately, not from the entry fee.

> 🔴 **The result that matters: a 2% entry fee loses money at launch.** At a 3% fabrication premium, a 2% fee gives `75 × [1 − 0.98 × 1.03] = −$0.71` per contribution. Aurumix would pay $0.71 for the privilege of taking $75. **The entry fee must sit at the top of the client's stated 2 to 5% range at launch, not the bottom**, and the reason is arithmetic, not positioning.

### And the fee can fall as the business scales

Because fabrication premium falls with bar size and the float's capital cost falls as a share of purchases:

| | Bar | Premium | Price-gap | Float CoC | Rail | Cost before margin | Workable entry fee |
|---|---|---|---|---|---|---|---|
| Y1 | 100 g | 3.00% | 0.36% | 0.49% | 0.30% | **4.15%** | **5%** |
| Y3 | 1 kg | 2.00% | 0.15% | 0.31% | 0.30% | **2.76%** | **4%** |
| Y10 | 12.4 kg | 0.75% | 0.28% | 0.38% | 0.30% | **1.71%** | **3%** |

**A falling entry fee is a real, explainable scale economy** and a better retention story than a manufactured premium. It also gives the agent channel something honest to sell: the fee goes down as the book grows.

Under a **dealer-carried float**, price-gap risk and float cost of capital drop out of Aurumix's column (roughly 0.85% at Y1) and are replaced by a wider dealer spread. Whether that is a net gain depends entirely on the dealer quote, which is the blocking item below.

## Invariants (developer-facing)

- **Backing invariant:** `float_grams + allocated_grams ≥ credited_grams`, at all times. Both sides published monthly.
- **No unbacked issuance.** Comtech's disclosed-unbacked-window shape is understood and deliberately not copied. A larger float is cheap and the story is cleaner.
- **Replenishment trigger:** buy when float falls below `1 bar + N days trailing inflow`.
- **Circuit breaker:** minting halts automatically if float reaches zero, or if custodian attestation lapses. Currency of attestation is a mint precondition, not a reporting nicety.
- **Sourcing covenant:** named refiner, accreditation covenant, and a substitution clause on suspension, using multi-list wording (LBMA / DMCC / LPPM) so substitution is pre-authorised. Not theoretical: Emirates Gold DMCC was suspended from both the UAEGD and LBMA lists in July 2023.

## Naming

| Layer | Name | Investor-visible |
|---|---|---|
| 1. Contribution | **Contribution Date** (investor's own anniversary) | Yes |
| 2. Allocation | **Allocation**, struck at first LBMA AM fix after cleared funds, T+1 | Yes |
| 3. Treasury | **Bar Procurement Cycle** | No, surfaced via the monthly Allocation Report |

"Mining Event" is retired. It implies PoW emissions, which is the wrong regulatory read in Dubai, and it has no resonance with an Indian saver whose reference point is an insurance premium. "Allocation Date" maps directly onto "premium due date".

## Two disclosures the client's document must absorb

1. **The LBMA AM fix is a benchmark, not a transactable price.** Real cost is fix + fabrication premium + dealer spread, currently absorbed silently inside the 2 to 5% entry fee. It must be disclosed.
2. **The Gold Receipt can never be bar-specific for a $75/month saver.** After a year they hold under 1% of a kilobar. "100% individually allocated" overstates. Honest framing: an **individually recorded pro-rata undivided interest in identified, serial-numbered bars.**

## Compliance note

- Continuous mint-on-deposit at NAV is **commodity-purchase shaped** and sits in the ARVA lane under VARA. A capped, time-boxed, oversubscribed, priority-queued sale is **offering-shaped** and points at securities characteristics. This is the strongest reason to delete the scarcity layer, and it costs nothing because the premium it was built to create is zero.
- Holding own-account gold inventory is a **proprietary position**. **[COUNSEL]** whether it is compatible with the intended VARA licence category and whether it counts toward capital.
- The float must be **segregated in the accounts and in the vault** from allocated investor holdings, and both balances published, so it can never be read as fractional backing.

## Open items

**Blocking, and everything above depends on them. All four are dealer conversations, not research tasks.**

- **[DEALER]** Identify a two-way Dubai bullion dealer or accredited refiner: buys and sells. Still unnamed in the client's document, and required for the float, the allocation cycle and the buyback alike.
- **[DEALER]** Will that dealer **carry the float**, and on what spread? This decides Option 1 versus Option 2 and therefore whether Aurumix needs working capital at all.
- **[DEALER]** Real Dubai fabrication premiums, two-way spreads and minimum tickets, per denomination. Published by nobody.
- **[DEALER / DMCC]** Tradeflow fees and terms, unpublished, and whether warrants are available from launch.

**Downstream, resolvable once the above is known.**

- **[CLIENT]** Tradeflow warrants from launch? Decides 100 g vs 1 kg and the launch float size.
- **[CLIENT]** If Option 2, confirm working capital for the float and that it is not sourced from investor funds.
- **[COUNSEL]** Whether allocated gold inventory can sit inside the VARA minimum capital requirement.
- **[COUNSEL]** Whether LBMA Good Delivery bars lose chain-of-integrity status when vaulted outside the LBMA approved-vault network. This prices the exit.

> **Project risk worth naming to the client.** Dubai's wholesale gold market is commercially opaque by convention. Premiums, spreads, minimum tickets and Tradeflow fees are all unpublished, and three research passes returned the same negative result. **Several Phase 2 parameters can only be closed by a counterparty conversation.** Until the procurement channel is identified, this section can specify the mechanism but cannot calibrate it.

---

# Token denomination

**Decision: 1 AURX = 1 gram of gold, permanently.** Changed from the 0.01 g in the 100 G Business Model. This was one of the six items the client explicitly delegated to us.

**Why 1 gram:**

- **One number, not two.** The token count is the gram count. "7.820 AURX = 7.820 g" needs no explanation to a customer who already buys gold by the gram. Any sub-gram unit forces the investor to reconcile a token balance against a gram balance, and the token count means nothing on its own.
- **The invariant becomes trivial:** `float_grams + allocated_grams ≥ tokens_outstanding`. No conversion factor in the contract, the audit or the attestation, and a retail holder can verify it unaided.
- **It matches every gram-denominated product in the landscape:** Comtech (1 token = 1 g), Aurus tGOLD (1 per gram), Digix DGX (1 g), CACHE CGT (1 g).
- **The Gold Receipt maps 1:1**, and no split or redenomination is ever needed.

**The sub-gram display objection is answered by the market.** Indian digital gold (Augmont and MMTC-PAMP, sold through Paytm and PhonePe) sells from ₹10, displays holdings in **grams to four decimals**, and operates at mass scale. The target persona already uses fractional-gram products. A jeweller also sells half-gram coins. Accumulation is a **display** problem, not a denomination problem.

## CG's "10 gram units" is a pricing convention, not a token size

Indian gold is quoted per 10 grams. That is a display convention and it does not constrain the token. **Quote the price per 10 grams in the app and on every statement; the token stays at 1 gram.** With 18 decimals on an ERC-3643 base, divisibility is never a technical constraint, so unit size is purely a presentation decision.

Lead the interface with grams to 3 decimals and the local-currency value, since that is what visibly grows, and use ICS tier progress and contribution streak as the accumulating counters:

> **7.820 AURX = 7.820 g. Gold today ₹95,000 per 10 g. Your holding ₹74,290. Tier: Bronze, 4 of 6 contributions to Confirmed SIP.**

## Three corrections owed to the client's document

1. **Delete "at launch"** from "AURX = 0.01 gram of gold at launch" (100 G, line 258). It implies the ratio may drift, which is the pool-share model from the superseded v2 document. State the ratio as permanent.
2. **Change 0.01 g to 1 g.**
3. **Reclassify the price formula.** `Price = total vault gold × LBMA fix ÷ total tokens` should be retained as a **verification identity**, not as the price definition. Under fixed weight the price is simply the LBMA fix per gram; the formula is what an investor uses to check that supply still equals metal.

## Two consequences that follow automatically

- **The custody fee must be cash.** Under a fixed-weight definition, deduction in grams and fee-by-dilution both break the peg. This closes the PAXG dilution mechanism, which is a real loss, but **Aurumix has a monthly cash touchpoint no other gold token has**: PAXG and XAUT need dilution or velocity taxes because their holders never send money again, whereas a SIP investor pays every month. Cash collection at the SIP moment is straightforward here and impossible for the category.
- **Supply moves with the metal.** Tokens mint only against grams delivered into the vault, which is what the backing invariant enforces.

---

# Why Mining Events don't work

**The name covers three functions. Two are real, one is not.**

- **Batching gold purchases: real.** You cannot buy 11 g/day at wholesale. Keep it, but as an internal treasury cycle.
- **Manufacturing scarcity: not real.** See the premium section below.
- **Monthly communication: real.** Replace with an Allocation Report (bar serials, assay certificates, float balance).

**Four reasons to delete the scarcity layer. Any one is sufficient.**

- **No economic function.** Every token mints at NAV against the buyer's own gold. There is no fixed pool to ration.
- **The premium it exists to create is zero.**
- **Wrong regulatory shape, and this is the costly one.** Capped, time-boxed, oversubscribed, priority-queued is offering-shaped and points at securities characteristics. Continuous mint-on-deposit at NAV is commodity-purchase shaped and sits in the ARVA lane.
- **Wrong word in both markets.** Dubai reads proof-of-work emissions. India's insurance-minded saver needs it explained.

**The client has already removed its precondition.** Their Q2 answer states there is no collective SIP date and SIPs arrive on any day. A collective event cannot function when every investor contributes on a different date.

## The SIP is unaffected and improves

- **It is a contribution commitment, not a token mechanic.** Nothing about what the investor pays or receives changes.
- **Allocation moves to the investor's own anniversary**, matching the insurance structure the model is built on.
- **Investor price risk falls from up to 30 days to under 24 hours.** At Y10 inflow a 5% move over 30 days is ~$300k.
- **Persistency replaces urgency:** 15-day grace (IRDAI monthly standard) plus a 6-month revival window on arrears.
- **Retention shifts to what actually retains:** ICS tiers, month-6 credit gate, Gold Card, Family Portfolio and Digital Will.

## The solution

- **Three layers:** Contribution Date (own anniversary) → Allocation (first LBMA AM fix after cleared funds, T+1) → Bar Procurement Cycle (internal, threshold-triggered).
- **The float**, dealer-carried at launch, own capital later. This is what makes T+1 and a $20 minimum possible.
- **Delete the scarcity layer.** No cap, no queue, no priority allocation.
- **Repurpose ICS:** allocation priority becomes an **entry-fee discount by tier** (the no-claim-bonus equivalent). Credit ratio, dividend share, card tier and family features unchanged.
- **Spot: restrict benefits, not supply.**
- **Invariant:** float + allocated ≥ credited, at all times, both published, minting halts if the float empties or attestation lapses.

---

# Why the 3 to 8% premium doesn't work

**Two cases, and they cover everything.** Liquid market: arbitrage closes the premium. Illiquid market: no market in which to express one. There is no third case.

**Nine protocols, no sustained premium:**

| Protocol | Evidence |
|---|---|
| XAUT | ~$2.465bn, 5.3% turnover, trades at gold |
| PAXG | ~$1.79bn, 5.9% turnover, at par |
| XAUm | capped by its own 0.76% two-way spread |
| Comtech | parity on a 0.42% spread |
| Aurus | NAV + 0.5%, which is its mint fee, not demand |
| VNXAU | ~0.7% over |
| PGOLD | ~$79 to 90M AUM on sub-$20 daily volume, no market |
| **Midas XGZ** | 🔴 **DISCOUNT** |
| **ORO** | 🔴 **DISCOUNT** |

**The discount case settles it.** XGZ has a members-only primary market and a 1 kg redemption floor against a 148 g average holding, so the average holder is 6.8x below the exit threshold. **Restricting arbitrage does not create a premium, it removes the price floor.** Aurumix's design (closed redemption, no physical delivery, rationed spot) resembles XGZ, not PAXG.

**Even if it existed, it is not revenue.**

- It accrues to secondary-market sellers, not to Aurumix.
- **Exposure is one-directional.** Above NAV, holders sell to each other and Aurumix gains nothing. Below NAV, holders redeem at NAV simultaneously and Aurumix bears it.
- **It cannot be promised.** A marketed premium gives a regulator an expectation of profit from the promoter's efforts, which contradicts the ARVA classification.

## What this means for spot

- **The 20 to 40% cap protects something that does not exist.**
- **Large spot tickets help the treasury.** A $500k order funds an immediate 4.5 kg wholesale purchase.
- **Discourage institutions by restricting benefits, not access.** No ICS, no dividend, no credit ratio, no card tier on spot. Restricting benefits is a loyalty programme. Restricting supply is a rationed offering.
- **Price the difference:** spot ~4 to 5% entry, plus a redemption fee decaying over 6 to 12 months. Redemption terms under an ARVA rulebook are `[LEGAL]`.

> The mechanism costs a securities-shaped structure, an AUM ceiling and institutional credibility, and returns a number that is not there.

---

# The ICS Dividend: why the framing fails, and the replacement

## Why it cannot be framed as it is

Stripped to plain words, the current design says: **you give us money, we run a business, we share our profits with you, and your share is bigger if you gave us more.** That is a share in a company, whatever it is called. Three features make it worse than necessary:

- **Paid out of operating profit** (15 to 20%), which makes holders profit participants.
- **Weighted by Investment Value** (`ICS-Weighted Score = ICS × Investment Value`), which is pro-rata by capital and removes any loyalty-programme defence.
- **80% to the top 10%**, which reads as a preference class.

**The consequence is concrete.** The token stops being an ARVA asset-referenced token under VARA and becomes a security token under a different regulator: prospectus, licensed issuer, accredited-only distribution. **A $20/month retail product cannot survive that.**

## What the category shows

- **Every well-regulated protocol pays zero yield deliberately:** PAXG, XAUT, XAUm, VNXAU, WTGOLD, DGLD, Midas XGZ, Comtech. WisdomTree owns a transfer agent, broker-dealer and fund adviser and pays nothing. Midas sits in a 115-year-old exchange group and leaves the gold idle.
- **Every protocol advertising a yield fails its own arithmetic:** Kinesis **$26,326 paid in June 2026 on $310M AUM, ~0.10% annualised against an advertised 2.05%**; PGOLD 5% on ~$79 to 90M funded by a market trading under $20/day; MG999 advertises 2.3% net on gold borrowed at 2.5% gross with a 1.00% management fee.
- **Vaulted gold produces nothing and costs money to store.** Tenbin tGLD pays a real 4 to 6% only because its collateral is USDC and futures margin, not bullion.
- **Where gold is worked, the holder carries the risk.** Comtech T&C Part B cl.20 leases pooled gold and states "the Participating Digital Gold Holders will take the risk." Streamex's AgaBullion lessee defaulted in January 2026 and the remedy was foreign litigation plus an insurance claim.

## The replacement: Gold Rewards

**Pay the ICS benefit as a fee rebate credited in grams, not as a share of profit.**

| | Standard | Tier 5, 1% gram rebate |
|---|---|---|
| Contribution | $75.00 | $75.00 |
| Entry fee at 5% | $3.75 | $3.75 |
| Grams credited | 0.6518 g | **0.6583 g** |

Economically identical to a discount, but the saver watches their gold balance grow by more than they paid for, every month. That is the feeling the dividend was designed to produce.

**Payment currency does not change legal character.** A dividend paid in gold is still a dividend. What matters is the funding source, the entitlement basis and the cap. **Four rules make it a rebate:**

1. **Funded from the fee and interchange lines, never from profit.**
2. **Capped at fees and interchange generated by that customer in the period.** Uncapped makes it a distribution.
3. **Earned by tier, and tier is earned by behaviour** (contribution consistency, tenure, streak). **Investment Value must be removed from ICS weighting entirely.**
4. **Never described as yield, interest, return or dividend.**

**Fund it primarily from merchant interchange**, not the entry fee. Interchange is genuinely external revenue, it is merchant-funded (which is why card cashback is regulatorily unremarkable everywhere), and it scales with usage rather than with investment size, which is exactly the entitlement basis required.

> **Both precedents sit inside one company.** Kinesis's "yield" is the failure case: a sound fee-sharing mechanism destroyed by calling it a yield and creating a promise it missed by 20x. Kinesis's **card cashback, 2% in gold funded by interchange, works and is regulatorily boring.** Same company, same currency, same direction of money. The difference is the framing and the cap.

## Under 1 AURX = 1 gram, every bonus gram must be bought

The invariant is `float + allocated ≥ tokens outstanding`, so a credited gram is a real purchase. Only four funding sources exist: operating profit (the security problem), fee and interchange revenue (correct), leasing yield (encumbers the gold), or other holders' gold (fractional reserve, fatal).

**This bounds the rebate, and the number should be stated honestly to the client.** Against the entry-fee build-up:

| | Entry fee | Cost before margin | Net margin | Entry-fee rebate room |
|---|---|---|---|---|
| Y1 | 5% | 4.15% | ~0.85% | ~0.75% |
| Y3 | 4% | 2.76% | ~1.24% | ~1.1% |
| Y10 | 3% | 1.71% | ~1.29% | ~1.2% |

So **0.10% to 0.75% by tier at launch**, widened by whatever interchange and credit revenue supports. Not 15 to 20% of profit.

## Two things this fixes at once

- **It removes the second double-count.** Investment Value is currently both an ICS component and the multiplicand in ICS-Weighted Score. Removing it from the weighting is required for the securities argument and eliminates the double-count in the same step.
- **It gives the client an honest version of what they want.** They want holders to share in the company's success. **The entry fee falling from 5% to 4% to 3% as the book grows is exactly that**, it is deliverable, and it is legal.

## Sequencing, if a real yield is still wanted

1. **Launch with Gold Rewards only.**
2. Once the credit book is real and counsel has ruled, revisit gold leasing as a **separate, off-token, opt-in product for eligible investors**, never as a feature of the token.
3. Take the **Streamex lease documentation to Dubai counsel as a worked template**, with the explicit question of whether the holder-protection layer Streamex omits (security interest, risk-of-loss allocation, subordination, waterfall, holders as named insurance loss payee) can be built under VARA or ADGM. **No protocol in the landscape does this.**

> ⚠ **The trilemma still needs a client decision** (encumber the gold, fund from operating profit, or drop the dividend). This changes what the third option looks like: not "drop it", but replace it with a rebate that delivers the same feeling and cannot fail its own arithmetic.
