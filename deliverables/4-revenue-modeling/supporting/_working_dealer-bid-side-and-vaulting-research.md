# Dealer bid side, vaulting charges, and a failed replication — research record

**Date:** 2026-08-20
**Status:** Working record. Feeds corrections 34, 35 and 36 in the brief's §15.
**Why this exists:** the 2026-08-19 pass measured only the **ask** side — what a Dubai dealer charges to *sell* a bar. It never measured the **bid** — what a dealer *pays* to buy one back. "Dealer two-way spread" was a named but empty parameter in Stream 0. This pass fills it, retrieves the DGCX vaulting tariff that was blocked last time, and **re-runs the ask-side capture — which failed.**

**Method:** the same-page pair, per §1 and §10 of `_working_dealer-premium-and-comparables-research.md`. Every number below was personally retrieved. Search-summary figures are marked UNVERIFIED and are not carried.

---

## 0. What this found, in one table

| Item | Was | Now | Where |
|---|---|---|---|
| **Dealer two-way spread (Stream 0)** | named, empty | **2.5% at 1 kg, 3.7–4.4% at 100 g** | §1 |
| **The bid side alone** | never measured | **spot − 1.50% (1 kg), spot − 1.60% (100 g)** | §1.3 |
| **A published UAE bid** | none known | **iGold: 98% own-purchase / 97% elsewhere**, verbatim | §1.1 |
| **Sealed vs broken seal** | assumed "the whole answer" | 🔴 **It is not. Bid is brand-blind**; damage costs a separate 0.5–4% | §2 |
| **Institutional floor spread** | unknown | **13.2 bp London / 15.2 bp Zurich**, live order book | §3 |
| **DGCX vaulting charges** | UNVERIFIED search summary | **Retrieved. Per-kilogram, not ad valorem** — but 2007 vintage | §4 |
| **Custody in bp as gold rises** | model charges ad valorem | 🔴 **Confirmed structurally wrong**: 3.24 bp at $2,000/oz → **1.44 bp today** | §4.3 |
| **Ask-side re-run of 1.71 / 0.93** | treated as Observed | 🔴 **DID NOT REPRODUCE. A one-day artefact of a stale denominator** | §5 |

---

## 1. The bid side

### 1.1 The only published UAE bid schedule found

**iGold, FAQ, retrieved 20 Aug 2026 07:52 UTC** — https://igold.ae/frequently-asked-questions

Verbatim, under *"Do you buy back? What is the rate between buying and selling?"*:

> "We buy all gold and silver bullion. Our minimum standard rates for Gold are **98% if purchased from iGold and 97% if purchased elsewhere**... Please call us for a quote as sometimes we can offer a higher rate depending on market conditions at the time."

**The first primary-source UAE bid located across five research passes.** Two cautions:

- **These are floors, not quotes** — "minimum standard rates" plus "call us."
- 🔴 **The denominator is not stated, and iGold's own headline rate is the known trap.** Applying 98% to its "Pure Metal Rate" of AED 541.24/g (page stamped 20/08/2026 11:50:02) gives AED 530.42/g — but that same rate returns the PAMP 100 g 5+ tier at **−0.04%**, an impossible negative premium, reproducing the §2.2 failure of the prior record exactly. **iGold's 98%/97% cannot be anchored, so it cannot be converted into a spread.** Carry as a corroborating bracket only.

⚠ Also on that page: *"As we are not financially regulated… Bullion dealers are not required to be regulated by the U.A.E. Authorities."* Relevant to the standing point that Aurumix cannot price against unregulated competitors.

### 1.2 The measurement that worked

**BullionStar publishes ask and bid in the same API response** — a same-page pair in the strictest sense: one source, one instant, no cross-timing. Endpoint found by reading the site's own JS bundle (`app_desktop-26.0805.1404.min.js` → `servicesUrl + "/product/v2/prices"`), which **clears the client-side-rendering block recorded as a confirmed negative last pass.**

`https://services.bullionstar.com/product/v2/prices?locationId=1&currency=USD&productIds=<id>`

**Retrieved 20 Aug 2026 08:01:32 UTC.** Server timestamp in payload `1787212827958`.

| Product | id | Ask/g | Ask premium | Bid/g | **Spread** |
|---|---|---|---|---|---|
| PAMP 100 g minted | 463 | $148.63 | +2.92% | $142.09 | **4.40%** |
| PAMP 100 g cast | 658 | $147.50 | +2.14% | $142.09 | **3.67%** |
| PAMP 1 kg | 460 | $146.11 | +1.18% | $142.23 | **2.65%** |
| Perth Mint 1 kg | 2981 | $145.82 | +0.98% | $142.23 | **2.46%** |
| BullionStar 100 g (own brand) | 1106 | $148.14 | +2.58% | $148.14 | **0.00%** |

`priceSpread` and `pricePremium` are BullionStar's own published fields, not our arithmetic.

**The denominator test passes.** Backing spot out of two independent products: `148.63 ÷ 1.0292 = 144.41` and `145.82 ÷ 1.0098 = 144.40` USD/g. **They agree to 1 part in 14,000**, and both sit inside BullionVault's independently-retrieved live band of 144.25–144.47 (§3). This is what §10.2 of the standing method requires before any number is used.

### 1.3 The derived bid discount — the number the model needs

| Class | Bid/g | Implied spot | **Bid vs spot** |
|---|---|---|---|
| 100 g | $142.09 | $144.405 | **−1.60%** |
| 1 kg | $142.23 | $144.405 | **−1.50%** |

🔴 **The bid is nearly flat across bar size — 10 bp between 100 g and 1 kg — while the ask premium moves 194 bp (2.92% → 0.98%).**

**This is the structural finding of the pass. The premium curve is an ask-side phenomenon almost entirely.** Fabrication cost is embedded in what you pay and is **not recovered when you sell**: the dealer buys everything back at roughly spot minus 1.5% regardless of what it cost to make. **The round trip is asymmetric, and a model that assumes the bid mirrors the ask will understate exit cost at large denominations and overstate it at small ones.**

### 1.4 The two-way spread, assembled

```
round trip = ask premium + bid discount
1 kg  : +0.98% to +1.18%  and  −1.50%   =>  2.46% to 2.65%
100 g : +2.14% to +2.92%  and  −1.60%   =>  3.67% to 4.40%
```

⚠ **For Aurumix, only the BID leg is the "dealer two-way spread" parameter.** The ask leg is already carried separately as F4. **Charging the full round trip *and* F4 would double-count — the same error correction 12 flags on float costs.**

---

## 2. Sealed vs broken seal — answered, and it is not what was expected

The brief anticipated this distinction was "likely the whole answer." **It is not.**

### 2.1 The bid is brand-blind

Within a weight class, BullionStar's bid is **byte-identical across brands and finishes**:

- PAMP 100 g **minted** vs **cast**: ask premiums 2.92% vs 2.14%, a 78 bp gap — **same bid, US$14,209.02.**
- PAMP 1 kg vs Perth Mint 1 kg: ask premiums 1.18% vs 0.98% — **same bid, US$142,232.46.**

**The dealer pays for metal, not for branding.** Whatever the assay card is worth, it is worth it on the way in and nothing on the way out. Directly observed, not inferred.

### 2.2 Condition is priced separately, and here is the schedule

**https://www.bullionstar.com/sell/ — retrieved 20 Aug 2026 08:04 UTC.** Verbatim:

> "The listed bullion prices are valid for bullion in original condition."
>
> "The reduction for a bar or coin that is not in original condition is dependent on the severity of damage but normally ranges from **0.5 % to 4 %**."

⚠ **The same page carries a 1.5–4% ladder for bars failing Singapore's Investment Precious Metal test. That is a TAX-STATUS haircut specific to Singapore's GST regime and does NOT transfer to the UAE**, whose investment-gold zero-rating works differently. **Do not import the IPM ladder.**

⚠ **The operative number for Aurumix is the condition haircut, and its relevance is a design choice, not a market fact.** If the trust holds bars that never leave the vault or their packaging, it is **avoidable and should be modelled at zero.** If redeemed metal is returned by customers and re-sold to a dealer, it is live and could reach 4%. 🔴 **This is the same dependency correction 30 flags as undesigned — *does redeemed gold return to the float or go back to the dealer?* — and it is now quantified at up to 4% on the damaged path. Priority raised.**

---

## 3. Comparator cross-check: a real institutional two-way spread

**BullionVault live order board**, via its own public JSON endpoint:
`https://www.bullionvault.com/view_market_json.do?considerationCurrency=USD&securityClassNarrative=GOLD`
**Payload timestamp `"20 Aug 2026 12:53:27 PKT"` (07:53:27 UTC).** USD per kg of allocated gold in named vaults.

| Vault | Bid/kg | Offer/kg | **Spread** |
|---|---|---|---|
| London | 144,250 | 144,440 | **13.2 bp** |
| Zurich | 144,250 | 144,470 | **15.2 bp** |
| Singapore | 144,030 | 144,650 | **42.9 bp** |
| New York / Toronto | 143,890 | 144,800 | **62.8 bp** |

**The floor for allocated Good Delivery gold in a liquid vault is 13–15 bp — roughly one twentieth of the retail 1 kg round trip.** The gap between 15 bp and 250 bp *is* the retail fabrication-and-handling layer, priced.

**BullionVault tariff** (https://www.bullionvault.com/help/tariff.html, retrieved 07:56 UTC): dealing **0.50% under $75k, 0.10% to $825k, 0.05% above**; storage and insurance **0.12%/yr, monthly minimum $4**; physical withdrawal **2.5% for 400 oz bars, 7.5% other amounts**.

⚠ **13 bp is NOT the relevant comparison for Aurumix.** It is a *venue* spread between two customers, not a dealer's principal risk price, and it exists only because a standing order book does. **Aurumix has no order book.** The honest comparator for a single-dealer quote is §1's retail number, with 13 bp as a theoretical floor reachable only by building two-sided liquidity.

**Confirmed negative:** BullionVault's HTML order board renders client-side and returns no prices to WebFetch. The JSON endpoint is the only working route — undocumented but public, no auth.

---

## 4. DGCX vaulting charges — retrieved, via the archive

### 4.1 The blocked file, and the route around it

**https://www.dgcx.ae/download_file/699/281 remains blocked.** Confirmed again: `curl` with a full browser UA returns **HTTP 403** plus a Cloudflare interstitial. So does **every** DGCX path tested — `/circulars`, `/rulebook`, `/spot-gold`, and the site root. **The entire dgcx.ae domain is Cloudflare-walled to non-browser clients.** Wayback has **no capture of that URL** (CDX over `dgcx.ae/download_file*` returns 37 rows, none matching).

**What worked:** a CDX query for all archived `dgcx.ae` PDFs (1,911 rows) surfaced two vaulting schedules, both retrieved as genuine PDFs and read in full.

### 4.2 The actual schedule

**`dgcx.ae/Downloads/ContentDownloads/DGCX_vaulting_GOLD.pdf`, archived 2010-09-21, titled "DGCX Gold Vaulting/Handling Charges — Applicable w.e.f. May 1, 2007."** Levied by DGCX Approved Vaults, gold 1 kg bar:

| Charge | Rate |
|---|---|
| Inbound / Acceptance | **USD 2.00 per kg** |
| Outbound / Release | **USD 2.00 per kg** |
| Transfer Handling | **USD 0.60 per kg** |
| **Storage incl. insurance** | **USD 0.40 per kg per 7 days maximum** |
| **Minimum charge** | **applicable for 25 kg** |

Plus 24 hours free storage from 1700 on Delivery Day. The 2006 predecessor tariff (in/out USD 6.50/kg, storage USD 1.10/kg per 7 days, 10 kg minimum) shows **charges fell ~64% between 2006 and 2007** while the minimum lot rose.

### 4.3 🔴 The structural point is confirmed

**Every charge is per kilogram. Not one is ad valorem.** Annualising storage: USD 0.40/kg/7days = **USD 20.86 per kg per year.**

| Gold price | Storage as bp | In + out as bp |
|---|---|---|
| USD 2,000/oz (64,300/kg) | **3.24 bp** | 0.62 bp |
| **USD 4,493/oz (144,470/kg, today)** | **1.44 bp** | **0.28 bp** |

**Custody cost in basis points has fallen 56% purely because gold rose.** 🔴 **A model charging custody ad valorem accrues a cost that scales with the gold price against a real charge that does not. In a rising-gold scenario it overstates custody; in a falling one it understates.** Re-specify as **per-gram with a minimum**, not bp of AUM.

### 4.4 Caveats — real, but old

⚠ **The 2007 tariff is 19 years stale and must NOT be quoted to the client as current.** Its value is **structural, not numerical**: it establishes that DGCX-approved Dubai vaulting has historically been priced per kilogram with a weight-based minimum lot.

⚠ **The USD 25.00/day and USD 0.10/kg/day figures remain UNVERIFIED** and appear in neither retrieved PDF. A search summary attributes to a **December 2015** DGCX document a third structure again (*"Acceptance OR Release US$50.00 per transaction, Bar handling US$20.00 per transaction / US$0.50 per 1 kilo bar, Storage US$25.00 per day"*) which **could not be retrieved and is not carried.** Note that even the UNVERIFIED figures disagree with each other on structure. **Put none of these in a deliverable.**

**Corroborated:** DGCX/DCCC approved vault operators are **Brink's Global Services and Transguard**, at DAFZ, Almas Tower and the Deira Gold Souk — consistent with DMCC's description of Almas Tower as Brink's-operated. **Operator identity corroborated; charges are not.**

---

## 5. 🔴 The ask-side re-run FAILED to reproduce, and it is the most important finding here

Same method, same two pages, same dealer, 24 hours later.

**Rate page: https://www.goldtrade.ae/current-gold-price.html — stamped "20 Aug 2026; 11:49am", AED 530.76/g.** Store fetched same minute.

| Product | AED/g | Premium **today** | Premium **19 Aug** |
|---|---|---|---|
| PAMP 1 g | 595.15 | +12.13% | +9.75% |
| PAMP 10 g | 559.74 | +5.46% | +3.07% |
| **PAMP 100 g** | 552.74 | **+4.14%** | +1.75% |
| **Valcambi 100 g** | 552.32 | **+4.06%** | +1.67% |
| **Emirates 1 kg** | 548.63 | **+3.37%** | +0.98% |
| **Etihad 1 kg** | 548.04 | **+3.26%** | +0.87% |

The curve is still monotonic, so it passes the shape test — **but the whole curve shifted up by ~2.4pp.**

**The diagnostic:**

```
goldtrade rate page,  19 -> 20 Aug:  530.45 -> 530.76  =  +0.058%
goldtrade store PAMP, 19 -> 20 Aug:  539.74 -> 552.74  =  +2.409%
```

**The store repriced 2.4% and the rate page moved 6 bp.** A fabrication premium does not widen by 2.4pp overnight. **The rate page is stale relative to the store.** Independent confirmation: iGold's headline rate was AED 541.25 on 19 Aug and **541.24** today — a one-fils move over 24 hours during which gold in USD clearly moved. **Both Dubai dealer "rate" pages are cached or lagged feeds, not live strike rates.**

🔴 **Conclusion: the 1.71% / 0.93% figures from 19 August are a one-day artefact and must not be carried as Observed.** Open item 6 of the prior record asked exactly this and the answer is negative. **The goldtrade.ae pair fails the simultaneity requirement that the same-page method exists to guarantee** — the two pages share a domain but not a clock. A subtler failure than the original cross-source error, but the same failure in kind.

**What survives:** the **shape** reproduced on both days, and the **1 kg vs 100 g step is stable at 0.77pp today against 0.78pp yesterday** — independently corroborated by BullionStar at 1.16–1.74pp. 🔴 **The denomination ladder survives. Its absolute level does not.**

---

## 6. Confirmed negatives

- **No Dubai/UAE dealer publishes a live bid alongside a live ask on the same page.** Checked and confirmed absent: goldtrade.ae, igold.ae/gold-rate, mintjewels.ae, emiratesgold.ae, aletihadgold.com, gvs-trading.ae, ounce.ae, cksgold.ae, sellandbuygold.me. **The UAE market publishes asks and negotiates bids by phone.**
- **iGold's sister buy-back site sellgold.ae publishes no rates.** *"Please ring us for the latest gold rates."* Five plausible calculator paths all return HTTP 404.
- **GVS Trading states a repurchase guarantee but no price.** *"We guarantee the repurchase of all precious metals purchased from GVS."* No percentage, no conditions.
- **CKS Gold advertises "We Will Buy Gold in 4 Easy Steps"** with no rate, percentage or condition schedule — a contact funnel.
- **goldratesindubai.com's scrap calculator is unusable** — a hard-coded 92% factor on a 24K rate of AED 290.00/g, ~45% below the real rate. **Impossible number, therefore a diagnostic.** Its 92% is a jewellery/scrap convention and must not be applied to bullion.
- 🔴 **The "88–95% of spot" and "~2% below spot" figures circulating in search summaries are UNVERIFIED**, untraceable to any dealer's own page, and refer to **scrap and used jewellery** — a different product from a sealed investment bar. **Not carried.**
- **The Dubai Gold & Jewellery Group does not publish a two-way rate.** Only a single reference rate twice daily. No bid/ask pair located.
- **No refiner or UAE dealer publishes a differential bid for sealed vs broken-seal bars.**

---

## 7. What the model input should be

### 7.1 Recommended values for Stream 0, "Dealer two-way spread"

| Parameter | Recommended | Basis | Confidence |
|---|---|---|---|
| **Bid discount, 1 kg** | **1.50%** below spot | Simultaneous bid/ask, denominator cross-validated twice | **Observed** |
| **Bid discount, 100 g** | **1.60%** below spot | same | **Observed** |
| **Bid discount, UAE-specific** | **1.5–3.0%, model at 2.0%** | iGold's 97–98% floor brackets it; UAE bids are phone-negotiated | **Moderate** |
| **Full round trip, 1 kg** | **2.5%** | 0.98–1.18% ask + 1.50% bid, same instant | **Observed** |
| **Condition haircut** | **0%** if metal never leaves the vault; **0.5–4%** if it does | BullionStar verbatim; no UAE equivalent found | **Low** — relevance is a design choice |
| **Institutional floor** | **15 bp** | BullionVault live order book | **Observed**, unreachable without an order book |

**Headline: carry the dealer bid at 1.50% below spot for 1 kg, with a UAE uncertainty band of 1.5–3.0%.**

⚠ **Why not simply use 1.50% for the UAE.** The two observed points are Singapore retail. iGold's 97–98% floors are the only UAE anchors and bracket 1.50% tight / 3.00% loose. A dealer buying from a known institutional counterparty in size *should* price better than a retail walk-in — **but that is reasoning, not observation, and it is exactly the kind of inference this method forbids using to fill a gap. 2.0% is a defensible planning value; 1.50% is the defensible observed value; present neither as a UAE quote.**

### 7.2 Two structural corrections this pass forces

1. 🔴 **Custody should not be ad valorem** (§4). Re-specify as per-gram with a floor. **Observed** on structure, **Low** on rate.
2. 🔴 **Do not model the bid as a mirror of the ask** (§1.3). **Exit cost is not entry cost run backwards.** Netting them symmetrically misprices the round trip at both ends of the ladder.

### 7.3 What is retired

🔴 **The 1.71% / 0.93% Dubai ask premiums are WITHDRAWN pending a third observation** (§5). They failed replication and the cause is identified. **F4 must not be revised downward on a single day's reading.** The ladder's *shape* and the ~0.78pp 1 kg step survive and are independently corroborated.

### 7.4 Open items carried forward

| # | Item | Owner |
|---|---|---|
| 1 | 🔴 **Third-day replication of the Dubai ask premium**, re-fetching both pages and comparing their movements | Anyone — now urgent |
| 2 | **A UAE dealer bid quote in size, by phone.** iGold's 98% is a published floor; the institutional number is not on the internet | Dealer |
| 3 | 🔴 **Does redeemed gold leave the vault?** Now gates a 0.5–4% condition haircut *and* the D30 COGS correction | Abdur — priority raised |
| 4 | **Current DGCX/DCCC vaulting tariff.** Structure settled; the 2026 rate is not | Anyone with a browser |
| 5 | **Is Aurumix's custody contract per-weight or ad valorem?** Decides whether §7.2(1) is a model fix or a negotiating point | Client |

---

## 8. Method notes to append to §10 of the standing record

6. 🔴 **A same-page pair must also be a same-CLOCK pair.** Two pages on one domain can run on different caches. **Validate by re-fetching on a later day and confirming both sides moved by comparable amounts.** goldtrade.ae's rate page moved 6 bp while its store moved 241 bp — the pair is not simultaneous and its output is not a premium.
7. **When a site renders prices client-side, read its JS bundle for the API path.** BullionStar's `/product/v2/prices` was found in `app_desktop-*.min.js`; public, unauthenticated, returns ask, bid, premium and spread in one object. The same trick recovered BullionVault's `view_market_json.do`. **This clears a confirmed negative from the prior pass — client-side rendering is a soft block, not a hard one.**
8. **When a domain is Cloudflare-walled, query the Wayback CDX index for the whole domain by MIME type rather than guessing URLs.** `cdx/search/cdx?url=<domain>*&filter=mimetype:application/pdf` returned 1,911 DGCX PDFs and surfaced two documents nobody knew to ask for.
9. **Corroborate any derived spot against a second independent live source before trusting a spread built on it.** BullionStar's implied 144.41 agreeing with BullionVault's live 144.25–144.47 is what licenses §1.3.
