---
brand: Tokenomics.net
type: liquidity-audit
source: liquidity/run.py
created: 2026-09-24
---

# Aurumix AURX: secondary market liquidity audit

**Prepared by**: Tokenomics.net
**Date**: September 2026

---

## Part 1: What this audit covers

### Why this audit

AURX is an open ERC-20 token. One AURX is one gram of allocated gold.

- Any holder can send AURX to anyone else.
- So AURX can trade on a secondary market that Aurumix does not run.
- The Mechanism Design Document sets one rule: **do not seed a thin pool at launch.** A thin pool shows a visible discount to the gold price.

This audit answers three questions:

1. How much does a trade move the price in an AURX/stablecoin pool?
2. How big must the pool be for trades to clear at a fair cost?
3. How much of the pool is stablecoin, and how much is gold?

### What is left out

A standard audit also covers allocations, vesting, investor discounts, investor returns and unlock sell pressure. None of these apply to AURX.

- AURX has no allocation table.
- No investor holds discounted tokens.
- Nothing unlocks over time.
- Every AURX is minted when a customer's money buys a gram, and burned when that gram is sold back.

### How AURX differs from a launch token

#### The price is set by gold

- AURX tracks the LBMA gold price per gram (the fix).
- The pool's job is to stay close to that price.

#### Both sides of the pool cost real money

- Every AURX in the pool is backed by a real gram in the vault.
- A USD 1m pool holds about USD 0.5m of stablecoin and USD 0.5m of gold.
- Aurumix still owns the gold. It is capital tied up in the pool.

#### The customer has two other doors

- **Buying:** pay the fix plus the entry fee (5% at launch) through the Aurumix app.
- **Selling:** use the buyback. It pays the fix with no fee.
- The pool only wins a trade when it is cheaper than these doors.

### Method and inputs

The pool maths follows the Tokenomics.net audit engine.

| Input | Value | Source |
|---|---|---|
| AURX price | USD 141.50 (1 gram) | Phase 4 and 5 gold price |
| Pool fee | 0.30% on both designs | Uniswap V2 standard |
| Slippage ceilings | 0.5%, 1%, 2%, 5% | Tighter than the standard 2, 5 and 10%, because of the two doors |
| Pool sizes tested | USD 100k to 2.5m, both sides combined | No token raise to size from |
| Trade sizes | USD 1k, 5k, 10k, 20k, 50k | Standard audit grid |
| Aurumix trade sizes | USD 75 (monthly SIP), USD 2,000 (top SIP ticket), 100 g (USD 14,150), 1 kg (USD 141,500) | Product and bar sizes |
| V3 layout | Two thirds of capital in a band around gold, one third across all prices | Standard audit layout |
| V3 bands | ±5% and ±10% | Gold moves about 4% in a typical month |

#### How slippage is measured

A 1% ceiling allows the 0.3% fee plus 0.7% of price movement. The seller's average price is better: a 1 kg sale measured at 4.79% receives 2.56% below gold.

---

## Part 2: The simple pool (Uniswap V2)

A V2 pool spreads its capital across every price, from zero upwards.

- It needs no management.
- It never runs out of either asset.
- Most of its capital sits at prices AURX will never reach, such as half or double the gold price.

### V2 price impact

**How to read it.** Sale size runs along the bottom. Slippage runs up the side. Each line is one pool size. A trade fits a ceiling when its line is below that dashed line.

![Slippage against sale size in a V2 pool, one line per pool size](liquidity/outputs/charts/01_v2_price_impact.png)

#### What it shows

- From USD 250k to USD 1m, only the USD 75 SIP payment clears 0.5%.
- A USD 1k trade needs the USD 2.5m pool to clear 0.5%.
- In a USD 1m pool, a USD 2,000 sale costs about 1.1%.
- In the same pool, a 100 g sale costs about 5.7%.
- A 1 kg sale costs about 20% even in the USD 2.5m pool.
- Price impact grows with trade size divided by pool size. Double the trade and you need double the pool.

#### Key insights

- A V2 pool cannot hold AURX near gold for anything larger than a SIP payment.
- The 0.3% fee uses most of a 0.5% ceiling. Only 0.2% is left for price movement.
- Large exits are out of reach at every tested size.

#### Potential risks

- A thin V2 pool shows AURX below gold. The Mechanism Design Document prohibits this.
- A large seller who will not wait for the fix moves the displayed price. The gold behind each token has not changed.

### V2 maximum trade size

**How to read it.** For each ceiling, the largest sale the pool can take. One bar per pool size. Each gridline is ten times the one below.

![Largest sale inside each ceiling, V2 pool](liquidity/outputs/charts/02_v2_max_trade.png)

| Pool size | 0.5% ceiling | 1% ceiling | 2% ceiling | 5% ceiling |
|---|---|---|---|---|
| USD 100k | USD 50 | USD 176 | USD 432 | USD 1,222 |
| USD 250k | USD 126 | USD 441 | USD 1,079 | USD 3,054 |
| USD 500k | USD 251 | USD 882 | USD 2,159 | USD 6,109 |
| USD 1m | USD 502 | USD 1,765 | USD 4,318 | USD 12,218 |
| USD 2.5m | USD 1,256 | USD 4,411 | USD 10,795 | USD 30,544 |

#### What it shows

- Double the pool and every cell doubles.
- Buys are slightly smaller than sells: USD 501 and USD 1,752 in the USD 1m pool.

#### Key insights

- The USD 2.5m pool cannot take one 100 g sale inside 2%. Its limit is USD 10,795, about 76 g.
- The standard audit benchmark is USD 10k to 50k inside 2 to 3%. No V2 pool tested meets it.

### V2 liquidity required

**How to read it.** The pool size needed for each trade to clear each ceiling. One line per trade size. Where a buy needs more than a sale, the larger figure is shown.

![Pool size needed against slippage ceiling, V2, one line per trade size](liquidity/outputs/charts/03_v2_required_tvl.png)

| Trade | 0.5% | 1% | 2% | 5% |
|---|---|---|---|---|
| USD 75 (target SIP) | USD 150k | USD 43k | USD 18k | USD 6k |
| USD 2,000 (top SIP ticket) | USD 3.99m | USD 1.14m | USD 471k | USD 172k |
| USD 10,000 | USD 19.9m | USD 5.71m | USD 2.36m | USD 858k |
| 100 g (USD 14,150) | USD 28.2m | USD 8.08m | USD 3.33m | USD 1.21m |
| 1 kg (USD 141,500) | USD 282m | USD 80.8m | USD 33.3m | USD 12.1m |

#### Key insights

- A 100 g sale inside 1% needs USD 8.08m, about USD 570 of pool per dollar traded.
- A 1 kg sale inside 5% needs USD 12.1m. That is more than the peak funding Phase 5 measured for the whole business.

---

## Part 3: The concentrated pool (Uniswap V3)

A V3 pool puts its capital inside a chosen price band.

- AURX should always trade near gold, so the band sits around the gold price.
- Layout: two thirds of the capital in the band, one third across all prices as a backstop.
- Two bands are tested: ±5% and ±10%.
- Gold moves, so the band must be re-centred from time to time. A narrower band needs this more often.

### V3 liquidity by price

**How to read it.** Depth at each price, as a multiple of V2, for the same USD 1m. More depth means a trade moves the price less.

![Depth by price, as a multiple of V2, same capital](liquidity/outputs/charts/05_v3_liquidity_profile.png)

#### What it shows

- Inside the band, ±10% is 14 times as deep as V2.
- Inside the band, ±5% is 27 times as deep as V2.
- Outside the band, both drop to one third of V2. Only the backstop is working.
- A narrower band gives more depth, and less protection when gold moves.

### V3 price impact

**How to read it.** The same chart as for V2, for the ±10% band.

![Slippage against sale size in a V3 ±10% pool, one line per pool size](liquidity/outputs/charts/06_v3_price_impact.png)

#### What it shows

- In a USD 500k pool, a USD 2,000 sale costs about 0.4%.
- In the same pool, a 100 g sale costs about 1.1%.
- A 1 kg sale costs about 7.9% there. It needs the USD 1m pool (4.2%) to fit inside 5%.
- The two smallest pools bend sharply at the right. There the sale has pushed the price out of the band. That bend is the pool's practical limit.

#### Key insights

- Everyday trades cost little more than the fee. A USD 2,000 sale in a USD 1m pool costs about 0.36%, of which 0.30% is the fee.
- Costs jump once a trade leaves the band. Size the pool so the largest trade stays inside.

### V3 maximum trade size

**How to read it.** The largest sale inside each ceiling for a USD 1m pool, V2 against both V3 bands.

![Largest sale inside each ceiling, USD 1m pool, V2 against V3](liquidity/outputs/charts/07_v3_max_trade.png)

| Ceiling | V2 | V3 ±10% | V3 ±5% |
|---|---|---|---|
| 0.5% | USD 502 | USD 7,011 | USD 13,718 |
| 1% | USD 1,765 | USD 24,631 | USD 48,194 |
| 2% | USD 4,318 | USD 60,274 | USD 117,934 |
| 5% | USD 12,218 | USD 170,548 | USD 333,700 |

#### What it shows

- ±10% takes 14.0 times more than V2 at every ceiling.
- ±5% takes 27.3 times more.
- At USD 1m, ±10% takes a 1 kg sale inside 5%. V2 cannot do this even at USD 2.5m.

#### Key insights

- A USD 1m ±10% pool meets the standard benchmark. USD 10k to 50k trades clear inside 2%.
- Halving the band doubles the depth. It only lasts while gold stays inside the band.

### V3 liquidity required

**How to read it.** The same chart as for V2, for the ±10% band.

![Pool size needed against slippage ceiling, V3 ±10%, one line per trade size](liquidity/outputs/charts/11_v3_required_tvl.png)

| Trade | 0.5% | 1% | 2% | 5% |
|---|---|---|---|---|
| USD 2,000 (top SIP ticket) | USD 286k | USD 82k | USD 34k | USD 12k |
| USD 10,000 | USD 1.43m | USD 409k | USD 169k | USD 62k |
| 100 g (USD 14,150) | USD 2.02m | USD 579k | USD 239k | USD 87k |
| 1 kg (USD 141,500) | USD 20.2m | USD 5.79m | USD 2.39m | USD 870k |

#### Key insights

- A 100 g sale inside 1% needs USD 579k, against USD 8.08m under V2.
- A 1 kg sale inside 5% needs USD 870k, against USD 12.1m under V2.

---

## Part 4: V2 against V3, and the budget

### V2 and V3 side by side

**How to read it.** All three designs at USD 1m.

![Slippage against sale size, USD 1m pool, three designs](liquidity/outputs/charts/10_cmp_price_impact.png)

#### What it shows

- V2 crosses the 1% ceiling a little above USD 1,700.
- V3 ±10% crosses it near USD 25k.
- V3 ±5% crosses it near USD 48k.

#### Key insights

- V3 is clearly better.
- The choice between the two bands depends on how much management Aurumix can take on.

### The budget

#### Service standard

We set a service standard to size the budget. It is our proposal. If Aurumix picks a different one, the budget scales in a straight line.

| Line | Trade | Inside | Why |
|---|---|---|---|
| 1 | Up to USD 2,000 | 0.5% | Everyday amounts trade at almost the fix |
| 2 | 100 g (USD 14,150) | 1% | A launch-bar holder can exit the same day |
| 3 | 1 kg (USD 141,500) | 5% | The largest bar stays inside the entry fee |

#### Pool needed

The smallest pool that meets all three lines:

![Pool size needed for the service standard, split into USDC and gold](liquidity/outputs/charts/12_cmp_budget.png)

| Design | Pool size | Stablecoin | Gold | Management |
|---|---|---|---|---|
| V2 | USD 12.1m | USD 6.07m | 42.9 kg (USD 6.07m) | None |
| V3 ±5% | USD 445k | USD 226k | 1.55 kg (USD 219k) | Re-centre about monthly |
| **V3 ±10%** | **USD 870k** | **USD 449k** | **2.97 kg (USD 421k)** | **Review quarterly** |

- The 1 kg line sets the size in every design.
- Both V3 options give the same service. ±5% uses half the capital and needs monthly work.

#### What trades cost

In the recommended ±10% pool:

| Trade | Slippage (engine measure) | Average price against gold |
|---|---|---|
| USD 2,000 | 0.37% | 0.33% below |
| 100 g (USD 14,150) | 0.76% | 0.53% below |
| 1 kg (USD 141,500), sale | 4.79% | 2.56% below |
| 1 kg (USD 141,500), purchase | 5.00% | 2.63% above |

#### A stricter standard

A 1 kg trade inside 2% would need:

- USD 2.39m under ±10% (USD 1.23m stablecoin plus 8.16 kg of gold).
- USD 1.22m under ±5%.
- USD 33.3m under V2.

### Fee tier

All figures use the 0.30% fee. Uniswap V3 also offers 0.05%.

- A USD 1m ±10% pool at 0.05% takes USD 15,765 inside 0.5% (USD 7,011 at 0.30%).
- Inside 1%: USD 33,408 (USD 24,631 at 0.30%).
- A lower fee earns the pool less. The tier is a launch decision and does not change the budget.

### Conclusion

#### Assessment

A pool works as a managed V3 position, once Aurumix can fund both sides.

- A V2 pool would need USD 12.1m. That rules it out.
- A V3 ±10% pool does the job for USD 870k with a quarterly review.
- A V3 ±5% pool does it for USD 445k with monthly work.

#### Strengths

- Two doors anchor the price: the free buyback below, the app above.
- One fixed budget covers every trade size the product creates. The largest SIP ticket is USD 2,000.
- The gold in the pool is still Aurumix's gold.

#### Risks

1. **An unmanaged pool shows a discount.** If gold leaves the band and nobody re-centres it, trades get expensive.
2. **The pool undercuts the entry fee.** A buyer who can reach it pays about 0.3 to 0.8% over gold, instead of 5%. The entry fee is the largest retail revenue line.

### Recommendations

#### 1. Plan for a USD 870k V3 ±10% pool

- USD 449k of stablecoin plus 2.97 kg of gold, minted as AURX. Review quarterly.
- Move to ±5% (USD 445k) only with a market maker under contract.
- Do not seed a V2 pool.

#### 2. Name the pool's owner before it opens

- The owner watches gold, re-centres the band, and mints AURX at cost when buyers drain it.
- Write the trigger down. For example: re-centre when gold moves 7% from the band's centre.

#### 3. Open on a DEX, fully funded

- AURX is an open ERC-20, so a DEX pool can be the first venue.
- Seed the pool only when the full budget is available. A half-funded pool is a thin pool.
- A centralised exchange can follow. It should hold about the same value within the same distance of the gold price.

#### 4. Decide whether the pool may undercut the entry fee

- Near the fix, the pool is cheaper than the app for anyone who can use it.
- Decide this next to the entry-fee calibration.
