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

### Why a liquidity audit, and why only this part of one

AURX is an open ERC-20 token: one token is one gram of allocated gold (decision 50, Mechanism Design Document section 3.5.3). Any holder can send it to anyone else, so it can trade on a secondary market that Aurumix does not run. The Mechanism Design Document already sets the rule for when that market opens. Secondary trading comes after the licence, once the float is deep, in order of increasing risk: a VARA-licensed exchange first, then a broader exchange, then decentralised venues (section 4.5). It also sets a standing prohibition: **do not seed a thin liquidity pool at launch**, because a thin pool shows a visible, continuous discount to the gold price.

This audit puts a number on "deep enough". It answers three questions:

1. If AURX is paired with a stablecoin (USDC or USDT) in a pool, how much does a trade of a given size move the price?
2. How big a pool does Aurumix need so that ordinary trades, and the occasional large exit, clear at an acceptable cost?
3. How much of that is stablecoin, and how much is gold?

A standard Tokenomics.net audit also covers allocations, vesting, investor discounts, investor returns and unlock-driven sell pressure. **None of those apply to AURX, and all are left out on purpose.** AURX has no allocation table, no investors holding discounted tokens and no unlock schedule. Every token is minted only when a customer's money has bought a gram, and burned when that gram is sold back. There is no supply to distribute, so the only supply-side question left is liquidity.

### How AURX differs from a normal launch token

Three facts change how the standard liquidity analysis applies.

**The price is anchored to gold, not discovered.** A normal token's pool is the place where its price is found. AURX already has a price: the LBMA gold price per gram (the fix). The pool's job is to stay close to it. So this audit does not ask the standard question, "what happens when X% of the circulating supply is sold". It asks how large a single trade can be before the pool price moves too far from gold.

**Both sides of the pool cost real money.** A normal project mints its own token side for free and only funds the stablecoin side. Every AURX in a pool must be backed by a real gram in the vault, minted like any customer's. A USD 1m pool is roughly USD 0.5m of stablecoin plus USD 0.5m of gold. The gold is not spent (Aurumix still owns it), but it is capital tied up in the pool.

**The customer always has a second door.** A buyer can go to Aurumix directly and pay the fix plus the entry fee (5% at launch, decision 9). A seller can use the buyback and receive the fix with no fee, because VARA forbids charging for redemption (Annex 2 III.E.4). The pool only wins a trade when it beats both doors. That is why this audit uses tighter slippage ceilings than the standard one (next section).

### How the pool sits against the primary door

The two doors fence in where the pool price can settle.

- **The floor is the fix.** If the pool price falls below the gold price, any holder who has completed onboarding can buy AURX in the pool and sell it back to Aurumix at the next fix, for free. That arbitrage pulls the pool back up. It is not instant: the buyback strikes at the next fix, hours away, and needs a verified account, so small discounts can persist for a few hours.
- **The ceiling is the fix plus the entry fee.** If the pool price rises above what a new customer pays at the primary door, buying directly becomes cheaper and mint-and-sell becomes profitable. That pulls the pool back down.

So the pool sits in a band between the gold price and the gold price plus about 5%. Two consequences follow. Both return in the conclusion.

1. **For sellers, the pool competes with a free buyback.** A holder will sell in the pool only if the slippage is a fair price for skipping the wait for the fix. That is why this audit's tightest ceiling is 0.5%.
2. **For buyers, the pool undercuts the entry fee.** A crypto-native buyer who can reach the pool gets gold at the fix plus a fraction of a percent, instead of the fix plus 5%. The pool is a cheaper door into AURX than Aurumix's own app, for the buyers who can use it. That is acceptable if Aurumix chooses it deliberately.

### Method in brief

The pool arithmetic follows the Tokenomics.net audit engine exactly: the Uniswap V2 constant-product formulas for price impact, maximum trade size and minimum liquidity, and the Uniswap V3 concentrated-liquidity formulas for the band design. Appendix A gives the formulas and the checks that tie our figures back to the engine.

| Input | Value | Source |
|---|---|---|
| AURX price | USD 141.50 (1 gram of gold) | Phase 4 and 5 gold price |
| Pool fee | 0.30% on both designs | Uniswap V2 standard; V3 set equal so the comparison measures shape, not fee |
| Slippage ceilings | 0.5%, 1%, 2%, 5% | The standard audit uses 2, 5 and 10%; tightened because the customer's other doors cost 0% (sell) and 5% (buy) |
| Pool sizes tested | USD 100k, 250k, 500k, 1m, 2.5m, both sides combined | There is no token raise to derive a single figure from, so a range is swept |
| Trade sizes | USD 1k, 5k, 10k, 20k, 50k, plus four Aurumix sizes | Standard audit grid, plus the sizes that matter to this product |
| Aurumix sizes | USD 75 (target monthly SIP), USD 2,000 (top SIP ticket), 100 g (USD 14,150), 1 kg (USD 141,500) | Product specification and launch bar denominations |
| V3 layout | Two thirds of capital in a band around the gold price, one third spread over all prices | Standard audit layout |
| V3 bands | ±5% and ±10% around the gold price | Gold moves about 4% in a typical month |
| Gold volatility | 15% a year | The figure used in the Phase 5 simulation |

**What "slippage" means here.** The audit engine's definition is used throughout. A 1% ceiling allows the fee (0.3%) plus 0.7% of price impact, where price impact is how far the pool's price has moved when the trade is done. This is deliberately conservative: the seller's average price across the whole trade is always better than the final price. Where the difference matters, both figures are given. For example, a 1 kg sale in the recommended pool measures 4.79% against the 5% ceiling, but the seller receives, on average, 2.56% below the gold price.

---

## Part 2: The simple pool (Uniswap V2)

A Uniswap V2 pool spreads its liquidity evenly across every possible price, from zero to infinity. It needs no management and never runs out of either asset, which makes it the standard starting point. For a token whose price is tied to gold, it is also wasteful: nearly all of the capital sits at prices AURX will never trade at, such as half or double the price of gold. This part measures what that costs.

### Price impact

**What this shows.** How far the pool's price moves when someone sells a given dollar amount of AURX into it. Sale size runs along the bottom and slippage up the side. Each line is one pool size, and the dashed lines are the four slippage ceilings. A trade fits a ceiling if, at that trade's size, the pool's line is still below the dashed line.

**What to look for.** A healthy pool keeps the product's everyday trade sizes (the SIP ticket and the top ticket) under 0.5%, and ordinary exits under 1 to 2%.

![Slippage against sale size in a V2 pool, one line per pool size](liquidity/outputs/charts/01_v2_price_impact.png)

The picture is poor across the whole range. Between USD 250k and USD 1m, only the USD 75 monthly payment clears the 0.5% ceiling. A USD 1k trade needs the USD 2.5m pool to do the same. The top SIP ticket (USD 2,000) costs about 1.1% even in a USD 1m pool, and a 100 g holder selling into that same pool moves the price about 5.7%. The 1 kg line only comes into view in the USD 2.5m pool, and there it still moves the price about 20%.

The pool formula explains why. In a constant-product pool, price impact grows roughly in proportion to trade size divided by pool size, so every doubling of the trade needs a doubling of the pool. No pool size escapes this rule. Each gain in depth costs capital in the same proportion.

#### Key insights

- **A V2 pool cannot hold AURX near the gold price for any trade larger than a monthly SIP.** At USD 1m of capital, a USD 2,000 sale costs about 1.1% by the engine's measure. A holder would lose more in slippage than the wait for the free buyback costs them.
- **The 0.3% fee takes most of a tight slippage budget.** At a 0.5% ceiling only 0.2% is left for price impact, which is why even small trades struggle at that ceiling.
- **The large exits are out of reach at any tested size.** A 1 kg sale moves a USD 2.5m pool by about 20%, which is four times the entry fee a buyer pays at the primary door.

#### Potential risks

- A thin V2 pool produces exactly the continuous visible discount the Mechanism Design Document prohibits. Anyone watching the pool would see AURX quoted below gold, which undermines the claim the product rests on.
- Large sellers who cannot wait for the fix will sell into the pool and move the displayed price, even though the gold behind each token is unchanged.

### Maximum trade size

**What this shows.** The reverse question: at each ceiling, what is the biggest sale the pool can take? Bars are grouped by ceiling, one bar per pool size. The vertical axis is logarithmic, so each gridline is ten times the one below.

![Largest sale inside each ceiling, V2 pool](liquidity/outputs/charts/02_v2_max_trade.png)

| Pool size | 0.5% ceiling | 1% ceiling | 2% ceiling | 5% ceiling |
|---|---|---|---|---|
| USD 100k | USD 50 | USD 176 | USD 432 | USD 1,222 |
| USD 250k | USD 126 | USD 441 | USD 1,079 | USD 3,054 |
| USD 500k | USD 251 | USD 882 | USD 2,159 | USD 6,109 |
| USD 1m | USD 502 | USD 1,765 | USD 4,318 | USD 12,218 |
| USD 2.5m | USD 1,256 | USD 4,411 | USD 10,795 | USD 30,544 |

The table scales in a straight line with pool size: double the pool and every cell doubles. A USD 1m pool takes USD 502 of selling inside 0.5% and USD 1,765 inside 1%. Buys are slightly smaller than sells at the same ceiling (USD 501 and USD 1,752 in the USD 1m pool).

#### Key insights

- **The best-case pool (USD 2.5m) cannot absorb one 100 g exit inside 2%.** The biggest sale it takes inside 2% is USD 10,795, about 76 g.
- **The standard audit's benchmark fails at every tested size.** That benchmark asks for USD 10k to 50k trades inside 2 to 3%. The largest V2 pool tested reaches USD 10,795 inside 2%.
- **Buy and sell capacity are nearly equal**, within about 5% of each other at every ceiling, so one number per ceiling is a fair summary.

### Liquidity required

**What this shows.** How large the pool must be (both sides combined) for a given trade to clear inside a given ceiling. Each line is one trade size. Where a buy and a sell of the same size need different amounts, the larger is shown.

![Pool size needed against slippage ceiling, V2, one line per trade size](liquidity/outputs/charts/03_v2_required_tvl.png)

| Trade | 0.5% | 1% | 2% | 5% |
|---|---|---|---|---|
| USD 75 (target SIP) | USD 150k | USD 43k | USD 18k | USD 6k |
| USD 2,000 (top SIP ticket) | USD 3.99m | USD 1.14m | USD 471k | USD 172k |
| USD 10,000 | USD 19.9m | USD 5.71m | USD 2.36m | USD 858k |
| 100 g (USD 14,150) | USD 28.2m | USD 8.08m | USD 3.33m | USD 1.21m |
| 1 kg (USD 141,500) | USD 282m | USD 80.8m | USD 33.3m | USD 12.1m |

The grid below shows the same result another way. For each pool size (columns) and trade size (rows), it gives the tightest ceiling the trade clears. Darker cells mean a tighter ceiling, which is better.

![Tightest ceiling each trade clears, by pool size, V2](liquidity/outputs/charts/04_v2_coverage.png)

Below USD 2.5m, the lower half of the grid is blank: nothing from USD 14k up clears even the 5% ceiling. The USD 2.5m pool brings the 100 g and USD 20k trades inside 5%, and the 1 kg exit never clears it.

#### Key insights

- **Letting a 100 g holder out inside 1% would take a USD 8.08m V2 pool.** That is about USD 570 of pool for every dollar of the trade it is meant to serve, and about USD 2,000 per dollar at the 0.5% ceiling.
- **A 1 kg exit inside 5% would need USD 12.1m.** That is more than the peak funding the Phase 5 simulation measured for the whole business.
- **The requirement grows in step with trade size.** A trade ten times larger needs a pool ten times larger at the same ceiling, so there is no economy of scale to wait for.

---

## Part 3: The concentrated pool (Uniswap V3)

A Uniswap V3 pool lets the liquidity provider choose the price range their capital works in. For AURX this is the natural design: the price should always sit near the gold price, so capital can be concentrated there instead of spread across prices that never occur. This audit uses the standard layout: two thirds of the capital in a band centred on the gold price, and one third across all prices as a backstop so the pool never runs dry if gold jumps. Two bands are tested, ±5% and ±10%.

### Where the liquidity sits

**What this shows.** The depth each design offers at each price, as a multiple of the V2 pool, for the same USD 1m of capital. Depth here is Uniswap's liquidity measure: the more of it at the current price, the less a trade moves the price.

![Depth by price, as a multiple of V2, same capital](liquidity/outputs/charts/05_v3_liquidity_profile.png)

Inside its band, the ±10% design is 14 times as deep as V2 and the ±5% design is 27 times as deep. Outside the band, both fall to one third of V2's depth, because only the backstop third is working there. This is the central V3 trade-off: a narrower band gives more depth near the gold price and less protection when gold moves.

### Price impact

**What this shows.** The same chart as for V2, now for the ±10% band. Read it against the V2 chart: the same pool sizes, the same trades, the same dashed ceilings.

![Slippage against sale size in a V3 ±10% pool, one line per pool size](liquidity/outputs/charts/06_v3_price_impact.png)

Every curve sits far below its V2 counterpart. In a USD 500k pool the top SIP ticket costs about 0.4% and a 100 g exit about 1.1%. A 1 kg exit still costs about 7.9% at that size. It needs the USD 1m pool (4.2%) to fit inside 5%. The two smallest pools show a kink at the right-hand end. Past that point the sale has pushed the price out of the band and onto the thin backstop, and slippage rises steeply. That kink marks the practical limit of each pool.

#### Key insights

- **Concentration leaves everyday trades costing little more than the fee.** A USD 2,000 sale into a USD 1m ±10% pool costs about 0.36%, of which 0.30% is the fee.
- **Costs jump at the band edge.** Once a trade carries the price out of the band, slippage goes from single digits to tens of percent within one step of trade size. A pool must be sized so that the largest expected trade stays inside the band.

### Maximum trade size

**What this shows.** The largest sale inside each ceiling for a USD 1m pool, V2 against the two V3 bands.

![Largest sale inside each ceiling, USD 1m pool, V2 against V3](liquidity/outputs/charts/07_v3_max_trade.png)

| Ceiling | V2 | V3 ±10% | V3 ±5% |
|---|---|---|---|
| 0.5% | USD 502 | USD 7,011 | USD 13,718 |
| 1% | USD 1,765 | USD 24,631 | USD 48,194 |
| 2% | USD 4,318 | USD 60,274 | USD 117,934 |
| 5% | USD 12,218 | USD 170,548 | USD 333,700 |

The multiple over V2 is the same at every ceiling: 14.0 times for the ±10% band and 27.3 times for the ±5% band. That holds as long as the trade stays inside the band, which it does for every cell in this table. The ±10% pool takes a 1 kg exit inside 5% at USD 1m, which V2 could not do at USD 2.5m.

The same grid as in Part 2, now for the ±10% design: the tightest ceiling each trade clears at each pool size.

![Tightest ceiling each trade clears, by pool size, V3 ±10%](liquidity/outputs/charts/08_v3_coverage.png)

#### Key insights

- **At the same capital, a ±10% band takes trades fourteen times larger than V2.** The USD 1m pool that took USD 1,765 inside 1% under V2 takes USD 24,631 under V3 ±10%.
- **A USD 1m ±10% pool meets the standard audit benchmark.** USD 10k to 50k trades clear inside 2%, which V2 could not reach at any tested size.
- **Halving the band doubles the depth again**, but only for as long as gold stays inside it. The next section measures how long that is.

### How often gold leaves the band

**What this shows.** A V3 band is fixed when it is set, but gold keeps moving. When gold moves past the band edge, the pool price follows it (arbitrage keeps AURX on gold), and the band stops working. For each band, this chart shows the chance that gold touches the band edge within 7, 30 and 90 days of the band being set. The figures come from 20,000 simulated gold paths at 15% annual volatility, the same assumption the Phase 5 simulation uses.

![Chance gold leaves each band within 7, 30 and 90 days](liquidity/outputs/charts/09_v3_band_breach.png)

| Band | Within 7 days | Within 30 days | Within 90 days |
|---|---|---|---|
| ±5% | 1.9% | 40.9% | 87.3% |
| ±10% | 0.0% | 3.1% | 31.8% |

What happens after a breach, in a USD 1m pool, for a sale inside a 1% ceiling:

| Band | Inside the band | Gold 1 point below the lower edge | Gold 1 point above the upper edge |
|---|---|---|---|
| ±5% | USD 48,194 | USD 570 | USD 606 |
| ±10% | USD 24,631 | USD 555 | USD 620 |

When gold has fallen through the band, every seller meets only the backstop, and capacity collapses by a factor of about 85 for the ±5% band and about 44 for the ±10% band. When gold has risen through the band, small sales also meet only the backstop, but a larger sale pushes the price back down into the band and regains its depth. Inside 2%, a USD 1m ±5% pool takes USD 55,243 of selling after gold rises through the band, against USD 1,395 after it falls through. Buyers meet the backstop instead.

#### Key insights

- **A ±5% band is a monthly job.** Gold leaves it within a month in two runs out of five, and within a quarter in nearly nine out of ten. Someone must re-centre it, which means withdrawing and re-depositing the position, roughly monthly and sometimes sooner.
- **A ±10% band is a quarterly review.** Gold leaves it within a month in 3% of runs. A quarterly check with a re-centre when needed keeps it working.
- **Breaches are most likely when holders most want to sell.** A sharp gold sell-off is when holders most want to sell, and it is exactly when a band left below gold has stopped working.

#### Potential risks

- An unmanaged ±5% pool will spend long stretches outside its band, showing the thin, discounted quotes the Mechanism Design Document prohibits.
- Re-centring has its own cost: each time the band is reset, the position must trade some AURX for stablecoin or the reverse to match the new centre. That cost is not measured here.

---

## Part 4: V2 against V3, and the budget

### Side by side

**What this shows.** The three designs at the same USD 1m of capital, on the same axes.

![Slippage against sale size, USD 1m pool, three designs](liquidity/outputs/charts/10_cmp_price_impact.png)

V2 crosses the 1% ceiling a little above USD 1,700. V3 ±10% crosses it near USD 25k, and V3 ±5% near USD 48k. For everyday trades V3 is clearly better. The only open question is how much management Aurumix can take on.

The required pool size for the ±10% design, in the same layout as the V2 table in Part 2:

![Pool size needed against slippage ceiling, V3 ±10%, one line per trade size](liquidity/outputs/charts/11_v3_required_tvl.png)

| Trade | 0.5% | 1% | 2% | 5% |
|---|---|---|---|---|
| USD 2,000 (top SIP ticket) | USD 286k | USD 82k | USD 34k | USD 12k |
| USD 10,000 | USD 1.43m | USD 409k | USD 169k | USD 62k |
| 100 g (USD 14,150) | USD 2.02m | USD 579k | USD 239k | USD 87k |
| 1 kg (USD 141,500) | USD 20.2m | USD 5.79m | USD 2.39m | USD 870k |

### The service standard, and the budget it needs

A budget needs a target. We propose the following service standard. It is ours, not the client's, and the budget scales in a straight line if Aurumix prefers a different one.

| Line | Trade | Inside | Why |
|---|---|---|---|
| 1 | Any SIP-sized trade, up to USD 2,000 | 0.5% | Close enough to the fix that a holder never needs the buyback for everyday amounts |
| 2 | 100 g (USD 14,150), the launch bar size | 1% | A meaningful holder can exit the same day at a small cost |
| 3 | 1 kg (USD 141,500), the largest bar | 5% | The largest exit still stays inside the entry fee, so the pool never quotes worse than the primary door does |

The smallest pool meeting all three lines, by design:

![Pool size needed for the service standard, split into USDC and gold](liquidity/outputs/charts/12_cmp_budget.png)

| Design | Pool size | Stablecoin side | Gold side | Management |
|---|---|---|---|---|
| V2 | USD 12.1m | USD 6.07m | 42.9 kg (USD 6.07m) | None |
| V3 ±5% | USD 445k | USD 226k | 1.55 kg (USD 219k) | Re-centre about monthly |
| **V3 ±10%** | **USD 870k** | **USD 449k** | **2.97 kg (USD 421k)** | **Review quarterly** |

The 1 kg line sets the size in every design. The other two lines are met with room to spare. In the recommended ±10% pool the three reference trades cost:

| Trade | Slippage (engine measure) | Average price received against gold |
|---|---|---|
| USD 2,000 | 0.37% | 0.33% below |
| 100 g (USD 14,150) | 0.76% | 0.53% below |
| 1 kg (USD 141,500), sale | 4.79% | 2.56% below |
| 1 kg (USD 141,500), purchase | 5.00% | 2.63% above |

The two V3 options give exactly the same service. They are sized so their bands hold the same depth. The ±5% pool therefore does the same job with half the capital, at the cost of monthly management instead of quarterly.

A stricter standard, the 1 kg trade inside 2% instead of 5%, would need USD 2.39m under ±10% (USD 1.23m stablecoin plus 8.16 kg of gold), USD 1.22m under ±5%, and USD 33.3m under V2.

### Fee tier

All figures above use the 0.30% fee tier. Uniswap V3 also offers a 0.05% tier, which leaves more of each ceiling for price impact. At USD 1m, a ±10% pool at 0.05% takes USD 15,765 inside 0.5% (against USD 7,011 at 0.30%) and USD 33,408 inside 1% (against USD 24,631). The gain is large at tight ceilings and small at wide ones. The trade-off is that a lower fee earns the pool less to offset its costs, which this audit does not measure. The tier is a decision for launch, not for this budget.

### Conclusion

**Assessment: a pool is viable, but only as a managed concentrated position, and only once Aurumix is ready to fund both sides of it.**

A V2 pool is ruled out. To hold AURX within the proposed service standard it would need USD 12.1m, more than Phase 5's measured peak funding for the whole business. A V3 pool does the same job for USD 870k with a quarterly review, or USD 445k with a monthly one. The pool can deliver what the product needs: everyday amounts at almost exactly the gold price, a launch-bar holder out the same day for under 1%, and the largest bar inside the entry fee. The budget is the easy part. The pool has to be managed, it will change who uses the primary door, and it must open only after the licence and the regulated venues.

**Key strengths**

- AURX's price is anchored by two arbitrage doors (the free buyback below, the primary door above), so the pool only has to hold depth near one known price. That is the best case for concentrated liquidity.
- A modest, fixed budget covers every trade size the product generates. Nothing in the SIP book comes close to straining it: the largest ticket is USD 2,000.
- The gold side of the pool is not spent. It remains Aurumix's gold, held as AURX.

**Critical risks, in order**

1. **An unmanaged or undersized pool is worse than no pool.** Once gold leaves the band, capacity falls by about 44 to 85 times, and the pool shows exactly the discount the Mechanism Design Document forbids. Seeding a pool without a named owner for its management breaks the standing prohibition.
2. **The pool undercuts the entry fee for anyone who can reach it.** A buyer who can use the pool pays about 0.3 to 0.8% over gold instead of 5%. For crypto-native buyers the pool becomes the cheaper way in, while the entry fee is the largest retail revenue line.
3. **The breach risk is highest exactly when selling pressure is highest.** A sharp fall in gold both triggers selling and pushes the price out of the band.
4. **Whether Aurumix may provide the liquidity itself is a regulatory question this audit does not answer.** Providing liquidity in its own token on an open venue may be a licensed activity in its own right. This belongs with counsel before any pool is seeded.

### Recommendations

#### 1. Plan for a USD 870k V3 ±10% pool, not a V2 pool

Budget USD 449k of stablecoin plus 2.97 kg of gold, held as AURX minted against the vault like any customer's. That meets the service standard with a quarterly review. Move to ±5% (USD 445k) only once a market maker is under contract to re-centre it at least monthly. Do not seed a V2 pool at any size.

#### 2. Name who manages the band before the pool opens

The pool needs an owner: someone who watches the gold price, re-centres the band when gold nears its edge, and tops up the AURX side by minting at cost when buyers drain it. Write the re-centring trigger down (for example, re-centre when gold has moved 7% from the band's centre) so it is a rule, not a judgement call made under pressure.

#### 3. Open the pool last, as the Mechanism Design Document already sequences

A VARA-licensed exchange with a contracted market maker comes first, then a broader exchange, then the pool. As a rough guide, the depth figures here carry over to an order book: it should hold about the same value within the same distance of the gold price. Seed the pool only when the budget above is available in full. A half-funded pool is the thin pool the prohibition describes.

#### 4. Decide on purpose whether the pool may undercut the entry fee

Priced near the fix, the pool will be cheaper than the app for anyone who can use it. That is acceptable if Aurumix treats the pool as a service to existing holders and to crypto-native buyers it would not otherwise reach. It is not acceptable as an accident. Put the decision next to the entry-fee calibration, and add the question of Aurumix acting as its own liquidity provider to the counsel list.

---

## Part 5: Appendix

### Appendix A: Method and formulas

All pool arithmetic reproduces the Tokenomics.net audit engine (`lib/tokenomics_audit/analyses`). The script `liquidity/verify.py` checks our pool engine against the engine's closed forms before any figure is used, and all checks pass.

**Notation.** Price P in USD per AURX; fee f = 0.3%; a slippage ceiling s leaves s − f for price impact (the engine's definition).

**V2 maximum trade** (engine: `max_trade_size_analysis.py`). With stablecoin reserve y and AURX reserve x:

- Largest buy: y × (√(1 + s − f) − 1) ÷ (1 − f)
- Largest sale, in AURX: x × (√(1 ÷ (1 − (s − f))) − 1) ÷ (1 − f), valued at P

**V2 minimum pool size** (engine: `liquidity_required_analysis.py`): 2 × (1 − f) × T ÷ (√(1 + s − f) − 1) for a buy of T dollars. Where the sale side needs more, the larger figure is used.

**V3** (engine: `v3_liquidity_analysis.py`). A position with liquidity L between prices Pa and Pb behaves, inside that range, as a V2 pool with virtual reserves L ÷ √P of AURX and L × √P of stablecoin. Our engine walks a trade across range edges instead of stopping at them, which is the same arithmetic generalised. Two departures from the engine, both deliberate:

- The engine's V3 module lets the price move by the full ceiling s, while its V2 module allows s − f. Using different rules would flatter V3 by the fee, so the V2 rule is applied to both designs.
- Tick-spacing alignment is ignored. At the 0.30% tier ticks are about 0.6% apart, which moves a band edge by at most that much.

**Checks run.** V2 price moves match the engine to the cent at 0.5, 2 and 5%; V2 maximum trades and minimum pool sizes match at all four ceilings; a V3 trade inside its band matches a V2 pool on the band's virtual reserves; capacity triples when capital triples; the V3 layout hits its target pool size and its two-thirds split.

**Band breach.** 20,000 gold paths, daily steps, 15% annual volatility, no drift beyond the volatility correction. A breach is counted when the price touches the band edge on any day, not only when it ends outside.

**Reproduce.** From `deliverables/3-supply-side-tokenomics/liquidity/`: `python verify.py`, then `python run.py`, then `python charts.py`. Every input is in `params.py` with its source.

### Appendix B: What this audit does not cover

- **Allocations, vesting, investor discounts, returns and unlock sell pressure.** Not applicable: AURX has no allocations or investors (Part 1).
- **The liquidity provider's profit and loss.** Fee income, and the loss a liquidity provider takes when gold moves and arbitrageurs rebalance the pool, are not measured. The pool is sized for service, not for return.
- **Re-centring cost.** Each reset of a V3 band trades part of the position at the prevailing price. Not measured.
- **Order-book exchanges.** Centralised exchanges use order books and market makers, not these formulas. The depth figures are a rough guide only.
- **Chain and gas costs.** No chain is assumed; network fees are excluded.
- **Legal questions.** Whether Aurumix may act as its own liquidity provider, and whether a pool listing changes how AURX is classified, are for counsel.
