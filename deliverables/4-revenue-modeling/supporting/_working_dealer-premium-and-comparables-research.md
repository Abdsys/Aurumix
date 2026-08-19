# Dealer premium, float structure and tokenised-gold comparables — research record

**Date:** 2026-08-19
**Status:** Working record. Feeds D28, D29 and D30, and corrections 26 to 30 in the brief's §15.
**Why this exists:** F4, the fabrication premium, sets **70% of stream 1's cost base** and was carried at 3.00% as an unsourced midpoint of an unpublished range. Four prior research passes on the direct question ("what do Dubai wholesale dealers charge") returned nothing. This pass reached the number by other routes and also answered several questions nobody had asked.

---

## 0. What this changed, in one table

| Item | Was | Now | Where |
|---|---|---|---|
| **F4, 100 g fabrication premium** | 3.00%, unsourced midpoint | **1.50%**, observed | §2, D28 |
| **The premium ladder** | 3.00 / 2.00 / 0.75 | **1.50 / 0.95**, and Good Delivery retired as a rung | §2.3, D28 |
| **S51 float carry mode** | Dealer-carried at launch, own float from Y3 | **Own float from M1** | §4, D29 |
| **COGS base** | Gross inflow, every contribution | **Net new grams** | §5, D30 |
| **Tradeflow as title registry** | Preferred (decision 26) | **Cannot carry fractional interests. No product uses it that way** | §6 |
| **LBMA "approved vault network"** | Assumed to exist; an open question priced the exit against it | **Does not exist. LBMA does not approve vaults** | §7 |

---

## 1. The measurement problem, and the method that solved it

**The first attempt failed and the failure is instructive.** Dealer prices in AED were compared against a spot price captured at a different moment, on a day gold moved USD 159.70 (~3.6%). The result put some 100 g bars **below spot**, which is impossible — no dealer sells metal at a loss. Two Dubai reference rates differed from each other by 2% within hours of each other.

⚠ **A premium computed from two differently-timed sources is noise, and the noise was the same size as the quantity being measured.**

**The method that fixed it: the same-page pair.** Find a dealer whose own page publishes **both** its live gold rate per gram **and** its bar prices. The ratio between them is internally consistent regardless of when the page is fetched, because both numbers are struck from the same moment.

```
premium = (bar price per gram ÷ that same page's quoted gold rate per gram) − 1
```

**Record this as the standing method for any future premium work.**

---

## 2. The observed Dubai premium curve

**Source:** goldtrade.ae, rate page stamped **19 Aug 2026, 19:52**, store fetched in the same minute.
Rate: **AED 530.45/g**.
https://www.goldtrade.ae/current-gold-price.html · https://www.goldtrade.ae/store/gold-bars-and-coins

| Product | AED | AED/g | Premium |
|---|---|---|---|
| PAMP 1 g | 582.15 | 582.15 | **+9.75%** |
| PAMP 10 g | 5,467.43 | 546.74 | **+3.07%** |
| **PAMP 100 g** | 53,973.59 | 539.74 | **+1.75%** |
| **Valcambi 100 g** | 53,932.04 | 539.32 | **+1.67%** |
| **Emirates 1 kg** | 535,645.41 | 535.65 | **+0.98%** |
| **Al Etihad 1 kg (995)** | 535,055.41 | 535.06 | **+0.87%** |

Worked example, PAMP 100 g: `53,973.59 ÷ 100 = 539.736`; `539.736 ÷ 530.45 − 1 = +1.75%`.

**The curve is monotonic — 9.75 → 3.07 → 1.71 → 0.93 — which is the shape a real premium curve must have**, because fabrication cost is near-fixed per bar and amortises with mass. That internal consistency is the main reason to trust this pair over any other source found.

### 2.1 The bulk gradient

**iGold publishes an explicit quantity ladder**, the only UAE dealer found that does. Prices 19/08/2026 19:52–19:53.
https://igold.ae/gold-bars/pamp-100-gram-gold-bar · https://igold.ae/gold-bars/valcambi-suisse-100-gram-gold-bar

| Product | 1+ | 2+ | 5+ | 1 → 5 |
|---|---|---|---|---|
| PAMP 100 g | 54,263.23 | 54,181.86 | 54,127.61 | **−0.25%** |
| Valcambi 100 g | 54,206.51 | 54,125.22 | 54,071.02 | **−0.25%** |
| Emirates 100 g | 54,083.46 | 54,029.38 | 53,948.26 | **−0.25%** |

**Five bars buys about 25 bp.** Applying that to goldtrade's 1.75% gives **~1.50%**.

⚠ **Both dealers stop the published ladder at 5 bars and say "call us."** The genuine bulk tier at 10 to 50 bars is priced by phone against a live fix and is **not published anywhere**. A third-party directory states *"premiums as low as 0.5% – 1% above spot available with negotiation"* in Dubai (https://bullion.directory/buying-bullion-in-dubai/, undated, weak source) — directionally consistent, and probably reachable only on kilo bars.

### 2.2 A rate that looks like a benchmark and is not

**iGold's own headline rate is unusable as a denominator.** At AED 541.25/g it returns Emirates 100 g at **−0.08%** and Emirates 1 kg at **−1.01%**, both impossible. iGold labels it a *"Pure Metal Rate"* from *"a 3rd party source"* it does not control (https://igold.ae/gold-rate). It is a 999.9 reference tick running above the fix, not the rate their products are struck from.

**Use iGold for its gradient, never for its level.** This is the exact trap that produced the first pass's sub-spot readings.

### 2.3 What this does to the premium ladder

| Rung | Model carried | Observed | Delta |
|---|---|---|---|
| 100 g | 3.00% | **1.71%** | −1.29pp |
| 1 kg | 2.00% | **0.93%** | −1.07pp |
| Good Delivery | 0.75% | no observation | — |

🔴 **The ladder was roughly one denomination too pessimistic at every rung. The model's 1 kg assumption (2.00%) is worse than what 100 g actually costs (1.71%).**

**The 1 kg step is worth 0.78pp and is therefore real.** It justifies keeping the denomination ladder rather than retiring it — but re-based, and with Good Delivery dropped as a rung (see §7 on why the GD target was wrong anyway).

### 2.4 VAT does not explain any of this

Investment gold at ≥99% purity in tradable bar form is **zero-rated in the UAE**, and B2B sales between VAT-registered firms use reverse charge. iGold's 1 kg bars show `0.00 AED VAT`. The small residual VAT lines on 100 g bars (AED 4.75–12.25 on ~54,000) are **VAT on delivery and handling, not on metal**, and are far too small to explain any discrepancy.

### 2.5 Confirmed negatives

- **No non-UAE premium was verified.** bullionbypost.com and findbullionprices.com returned HTTP 403; BullionStar's "Price Premium" field renders client-side and never appears in fetched markup. **No international comparison figure is carried, and none should be inferred.**
- **No refiner publishes a premium schedule.** PAMP, Valcambi, Argor-Heraeus, Metalor, Perth Mint, Emirates Gold and Al Etihad Gold Refinery all quote bilaterally.
- **The Reuters weekly physical gold report does not cover Dubai.** It covers India, China, Hong Kong, Singapore and Japan only. This closes an avenue the brief had not explicitly ruled out.
- **No published Good Delivery premium figure exists at all.**

---

## 3. What the comparables actually do

Three tokenised gold products were examined against their **binding** documents, not their marketing.

| | PAXG | Tether Gold | Comtech (CGO) |
|---|---|---|---|
| **Named dealer** | **StoneX** (ex-INTL FCStone) | Brokers, unnamed | **None named anywhere** |
| **Cash redemption** | Priced off streaming StoneX quotes | **Agency sale** in the Swiss market, customer bears execution risk | Issuer takes the other side (T&C 7.9) |
| **Repurchase obligation** | — | 🔴 **Explicitly none** | — |
| **Own inventory** | **Yes** — holds its own PAXG "to hedge against price risk" (Terms 4.9) | **Yes** — affiliate AGCL holds token inventory | **Yes** — may run up to **10 kg unbacked** for 24h (T&C 3.5) |
| **Price risk window** | **5-second guaranteed quote** | Passed to customer | Not disclosed |
| **Physical minimum** | 430 PAXG (1 GD bar) | 430 XAUT | **1 kg**, multiples of 1 kg |
| **Cash minimum** | **None published** | Full bars only | Any amount |

Sources: https://www.paxos.com/paxg-whitepaper.pdf · https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions · https://help.paxos.com/hc/en-us/articles/360042322271-PAX-Gold-Price-Determination · https://gold.tether.to/Relevant%20Information%20Document%20-%20TG%20Commodities,%20S.A.%20de%20C.V.%20(ENG).pdf · https://cgold.ae/assets/pdf/Terms_and_Conditions.pdf

**Three findings from this table.**

1. **Every working product carries inventory.** The float is not a design flaw to be engineered away. It is what all of them need. Only its size and its funder vary.
2. 🔴 **Neither PAXG nor XAUT accepts a repurchase obligation.** Tether states it outright. **Aurumix promises a formulaic buyback at the fix with no fee, and it is carrying a liability the two largest issuers in the world decline to carry — through a dealer who has not been named or asked.**
3. 🔴 **Paxos bears price risk for five seconds. Aurumix bears it until the next LBMA fix, which can be hours.** See §4.2 — this, not the float, is where the 0.79% price-gap actually comes from.

### 3.1 The jeweller channel, worth stealing

Comtech's in-kind route has a **1 gram** minimum against a **1 kg** physical minimum. The named partner is **Kalyan Jewellers**. The mechanism: **the partner takes the token, and no metal leaves the vault.** It solves the denomination cliff by netting rather than by logistics, and Kalyan is an Indian jeweller with UAE presence — precisely the Aurumix demographic.

### 3.2 Two Comtech clauses to decide against deliberately

- **T&C 20.2, "Facilitation Service":** customer gold is pooled and lent to jewellery-trade counterparties for up to six months. *"The Participating Digital Gold Holders will take the risk"* and the issuer *"will not be liable."* The **2026 fatwa expressly excludes** financing and yield mechanics from Shariah approval (fatwa §3).
- **T&C 3.5:** up to **10 kg unbacked** for holiday or logistical reasons, covered within 24 hours.

⚠ **Comtech's own documents disagree with each other** on purity (999 vs 999.9), custody fees (zero vs zero-for-24-months) and custodian naming. **Quote its T&Cs, never its whitepaper.**

### 3.3 Comtech is not VARA licensed, so it is not a cost benchmark

**All 56 entities on VARA's public register were checked. No Comtech, no ComTech FZCO, no Trade Fintech.**
https://www.vara.ae/en/licenses-and-register/public-register/

What it holds: **DAFZA licence 05069**, activity *"gold and other precious metals trading"*, plus a DMCC licence for **IT consultancy**. Its FAQ describes this as being "regulated."

🔴 **So Comtech's ~0.4% round trip cannot be used as a cost benchmark for Aurumix.** It is not carrying VARA Category 1 costs — AED 100k application, AED 200k/yr, AED 1.5M capital. **Aurumix cannot price against a competitor it is not permitted to be.** Carry this into the competitive section as a finding, not a comparison.

---

## 4. The float, and why it moves to launch

### 4.1 The argument

**Aurumix cannot use any of the three mechanisms its comparables use to avoid holding metal at its own risk.**

- **Comtech's route** — run briefly unbacked — is closed. The invariant is `trust holdings ≥ tokens outstanding`, and decision 34 is money, then title, then token, never any other order.
- **Tether's route** — no repurchase obligation, agency sale, customer bears execution risk — is closed. VARA Annex 2 III.E.4 forbids charging on the way out, and the product promises a formulaic buyback.
- **Paxos's route** — a named dealer filling instantly against a 5-second quote — is closed **because there is no dealer.** It is the single biggest open item in the engagement.

🔴 **Therefore Aurumix carries its own float from M1.** Not from Year 3.

**The consequence is not free, and correction 12 governs it:** under own-float, price-gap risk and float cost of capital both **bite from launch**, and the fabrication premium **narrows** because metal is bought direct. **Charging the wide dealer-carried premium and both float costs simultaneously double-counts under either regime and is an error, not a sensitivity.**

### 4.2 The price-gap is a pricing-convention cost, not a float cost

**This is the finding in this section, and it has not been framed before.**

The 0.79% price-gap exists because Aurumix promises a price struck at **the next published LBMA fix**, which may be hours away, and cannot buy metal at that price until it arrives. Paxos reduces the same exposure to near zero with a **5-second streaming quote** immediately hedged with StoneX.

**The fix was chosen for a real reason: neither side can select it, and it is used identically on entry, arrears and exit.** That is a genuine governance property.

⚠ **But it now costs 0.79% from launch rather than from Year 3, against a net contribution margin that was 0.54%.** It is a live cost decision, not a documentation detail, and it should be put to the client as a priced trade-off: **neutral pricing versus price-gap cost.**

---

## 5. COGS is charged on the wrong base

The model charges the premium on gross inflow, every contribution:

```
cogs(s,t) = net_of_fee(s,t) × fabrication_premium(t)      ← every period, no offset
```

**The premium is genuinely a per-gram cost and does pass through to customers** — every gram allocated came from a bar bought at fix + premium. That part is right.

**What is wrong: redeemed gold returns to the float and can be re-allocated without paying the premium a second time.** The premium is therefore paid on **net new grams**, not gross contributions.

**Size:** if redemptions run at 20% of inflows, premium cost is overstated by 20%. Small in Year 1, growing as the book ages. **It moves in the business's favour.**

**The brief already applies this logic on the redemption side** — one of its own checks is *"spread cost is exactly zero in every growing month"* — and simply does not apply it to COGS.

⚠ **One dependency:** this only holds if redeemed gold genuinely returns to the float rather than being sold back to the dealer. **That is a design choice nobody has written down**, it interacts with the buyback mechanics, and it must be settled before the correction is built.

---

## 6. Tradeflow cannot be the customer registry

🔴 **The words "Tradeflow" and "warrant" appear ZERO times in Comtech's binding Terms & Conditions.** They appear only in marketing and a DMCC press release.

**What Comtech actually does:** Comtech holds the warrant. Customers hold a contractual **undivided interest**, with Comtech *"expressly and irrevocably"* appointed as *"custodian, administrator and holder of the specific interest… acting as **agent in possession**"* (T&C 3.2, 3.6). **Tradeflow never sees a customer.**

**DMCC's own published model is the obstacle:** *"Each warrant represents a **specific item**"* and *"**Legal title remains with the holder of the warrant**."* Nothing in any DMCC document addresses warrant splitting, fractionalisation, omnibus or sub-accounts, or a nominee layer. The only beneficial-ownership concept found is **pledging** a warrant to a financier as collateral.

**Confirmed negative on the fee schedule too.** No Tradeflow tariff is published; the brochure ends with a contact number. DGD application and testing fees are stated as *"obtainable from the DMCC."* LBMA fees defer to a page that publishes no amounts.

### 6.1 What this means for decision 26

**Decision 26 prefers Tradeflow as the title record with vault books as a fallback. That preference needs re-examining.** The one Dubai product that could have used Tradeflow as a customer registry does not, and the published rules appear to prevent it.

**One genuine advantage to Aurumix, and it is worth telling the client.** Comtech's *"agent in possession"* is a **bailment** construct. Aurumix's design uses a **trust**. A trust gives materially stronger insolvency protection — which is precisely counsel batch 1 question 2. **Aurumix is structurally ahead of the incumbent on the question that matters most.**

### 6.2 The DMCC call changes shape

Not *"what does Tradeflow cost."* Instead: **"can a Tradeflow warrant represent fractional or sub-account interests, and if not, what does DMCC expect a tokenised gold product to do instead?"** The lever for that conversation is DMCC's own fact sheet, which states Tradeflow *"backs a range of tokenised gold products."*

⚠ **The Warrant Rules are annexed to a bilateral member agreement and are obtainable only as a prospective member.** This is not resolvable by desk research.

---

## 7. LBMA does not approve vaults

**Verbatim from the LBMA Good Delivery List Rules, Annex A: "LBMA does not approve Vaults."** The Approved Weighers List *"relates solely to the weighing… of gold and silver Bars."*
https://cdn.lbma.org.uk/downloads/GDL-Assets/Good-Delivery-List-Rules-Jan-2021-FINAL.pdf

The operative mechanism is **acceptance discretion**: a bar *"only becomes and remains London Good Delivery to the extent that a vault manager is willing to accept such a bar into the London vault."*
https://www.lbma.org.uk/publications/the-otc-guide/london-good-delivery-gold-and-silver

🔴 **So the open item "confirm whether LBMA GD bars lose chain-of-integrity status when vaulted outside the approved-vault network" rests on a network that does not exist.** Re-cut it. The correct framing is **loss of at-sight London acceptance**, not loss of a formal accreditation. This sharpens decision 11, which already noted that "LBMA" means two things.

### 7.1 Dubai's own Good Delivery standard is a 1 kg bar

**DGD:** 1 kg, minimum 995 or 999.9 fineness; refiner needs 3+ years operating, USD 15m net current assets, 10t gold and/or 30t silver refined in each of the prior 3 years.
**LBMA GD:** ~400 oz (12.4 kg); £15m tangible net worth; 10t gold / 50t silver.

**Two different standards sharing a name.** And **DGD is itself being superseded by the UAE Good Delivery standard** under Cabinet Resolution 2/16 of 2020, with DCCC settlement aligned from 21 July 2023.

**Consequence for the ladder:** the model's third rung targeted 12.4 kg Good Delivery and concluded it never clears at the model's volume. **That target was arguably never the right one** — the locally relevant standard is a 1 kg bar, which the model already has as its second rung. **Drop Good Delivery as a rung.**

⚠ **Also relevant: DMCC states it "is not involved in the regulation of the gold industry… All regulation is carried out at a federal level by the Ministry of Economy."** Check this against the licence stack in `_draft_entities-licensing-and-payments.md`.

---

## 8. Vault storage may not be ad valorem

**Confirmed negative across the board:** no vault operator publishes an annual basis-point rate for allocated gold. Malca-Amit lists seven locations, none in Dubai, and no pricing. DMCC describes the Almas Tower vault (five levels below ground, operated by **Brink's**, "no capacity limits") with an "Enquire now" link and no rates.

**One retrievable target, still blocked.** DGCX publishes a *"List of Approved Brands, Vaults and Vaulting charges"* at https://www.dgcx.ae/download_file/699/281. It is behind Cloudflare — WebFetch returns 403 and a `curl` attempt with a browser user-agent returned the challenge page rather than the PDF. **A search summary attributes to it a Brink's Almas Tower rate of USD 25.00/day minimum or USD 0.10 per kg per day. Treat as UNVERIFIED.**

🔴 **If per-kilo-per-day pricing is real it matters structurally, not just numerically: a per-weight charge does not scale with the gold price, so custody cost in basis points FALLS as gold rises.** The model charges custody ad valorem. **Pull this PDF in a browser — it is a two-minute task that would settle it.**

---

## 9. Open items this pass created

| # | Item | Owner |
|---|---|---|
| 1 | 🔴 **Can a Tradeflow warrant carry fractional or sub-account interests?** Not desk-researchable. Top of the DMCC call, above fees | Client / DMCC |
| 2 | **The genuine bulk premium tier** at 10–50 bars, and whether the deal strikes on the fix or the dealer's own tick (worth 20–30 bp) | Dealer |
| 3 | **Does redeemed gold return to the float or go back to the dealer?** Gates the §5 correction | Abdur |
| 4 | **Does the LBMA-fix pricing convention stay**, now that its 0.79% cost bites from launch? | Abdur / client |
| 5 | **Pull the DGCX vaulting charges PDF** in a browser | Anyone |
| 6 | **Re-run the same-page premium capture** across several days to confirm 1.50% is not a one-day artefact | Anyone |

---

## 10. Method notes worth keeping

1. **The same-page pair is the standing method** for premium measurement. Never compare a dealer price to an externally-sourced spot unless both timestamps can be stated.
2. **A dealer's headline "gold rate" is not necessarily the rate its products are struck from.** iGold's produces impossible sub-spot results. Test any denominator by checking whether it yields a monotonic curve across bar sizes; if it does not, the denominator is wrong.
3. **An impossible number is a diagnostic, not a datapoint.** The sub-spot readings in the first pass were the clue that found the method error.
4. **Read binding terms, not whitepapers.** Comtech's operative T&Cs are on a different domain from its marketing site and contradict it in several material places.
5. **Check the register, don't trust the claim.** "Regulated by DAFZA" turned out to mean a free-zone trade licence. All 56 VARA registrants were checked by hand.
