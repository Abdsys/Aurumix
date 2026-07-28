# Comtech Gold (CGO)

> **⚠ OUR WORKING ASSERTION WAS HALF WRONG, AND THE HALF THAT WAS WRONG IS THE HALF WE BUILT A HYPOTHESIS ON.**
>
> **We asserted: "Comtech operates from Dubai on a DMCC trade licence with no VARA or ADGM authorisation."**
>
> **The "no VARA" half is CORRECT and now verified against the register directly: Comtech does not appear anywhere on VARA's public register of 52 licensed VASPs, nor on the DFSA or ADGM FSRA registers.**
>
> **The "DMCC trade licence" half is WRONG, and the correction matters more than the error. The token issuer is `ComTech FZCO (DAFZA)`, a Dubai Airport Free Zone company, licence number **05069**, activity **"GOLD AND OTHER PRECIOUS METALS TRADING"**, issued 21-Feb-2022. There is a *separate* `ComTech FZCO (DMCC)` entity, licence **DMCC-889799**, but its registered activities are **IT consultancy, network consultancy, internet consultancy and software house**: it is a tech-services licence and cannot issue gold tokens either. Neither licence authorises issuing a virtual asset to the public.**
>
> **So there is no "DMCC gold-token path that routes around VARA." There is no authorised path here at all. What Comtech demonstrates is not a lawful alternative route: it is a pre-VARA-regime incumbent that has never been brought onto the register. Do not model Aurumix on it.**
>
> **Also: both licences shown on Comtech's own registration page are displayed EXPIRED (DAFZA expiry 20-Feb-2024; DMCC expiry 25-Jun-2024). See §3.**
>
> **Two further corrections to inherited framing: the Shariah certifier is no longer Amanie Advisors (superseded by Sābiq Advisory on 31 March 2026, §4), and there is no monthly proof of reserve (§4).**

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | CGO | **High** |
| Issuer (marketing) | "ComTech Gold" | **High** |
| Issuer (registry) | **ComTech FZCO (DAFZA)**, licence 05069, Dubai Airport Free Zone, issued 21-Feb-2022. Separate **ComTech FZCO (DMCC)**, licence DMCC-889799 / cert DMCC197166, formed 31-May-2023 | **High** |
| Parent | Trade Fintech Ltd, DIFC private company, registered number **5102**, incorporated 4 Oct 2021 (per whitepaper) | **Medium** |
| Cash-collecting entity | **COMTECH CORE TRADING FZCO**, ZAND Bank AED a/c 1002169010000001 (from the live app API, a third name) | **High** |
| Domicile | Dubai, UAE (DAFZA primary; DMCC secondary) | **High** |
| Backing claim | 1 CGO = 1 g gold, 999.9 fineness, standardised 1 kg bars | **High** |
| Chains | XDC / XinFin only | **High** |
| Contract address | `xdc8f9920283470f52128bf11b0c14e798be704fd15` (EVM `0x8f99...fd15`), 18 decimals | **High** (on-chain) |
| Supply | **39,000 CGO** on-chain `totalSupply` = 39 kg implied | **High** (on-chain) |
| Last published reserve | **111 kg** as at 21 Mar 2025 | **High** |
| Market cap | ~$5.04M | **High** |
| 24h volume | ~$815k, of which ~$814k is a single Bitrue pair | **High** |
| Regulatory status | **No VARA licence. No DFSA. No ADGM FSRA.** Free-zone trade licences only | **High** |
| Subscription fee | Website: "Transaction Fees: Nil". App API: buy commission **1.0125%** + payment charges + 5% VAT | **High** (contradiction, §7) |
| Ongoing custody fee | Website: "Custody Fees: Nil". FAQ: free for **first 24 months**, then "a nominal fee" | **High** (contradiction) |
| Redemption fee | 0.50% physical redemption; 0.50% transfer | **High** |
| Advertised yield | None on the token. A separate opt-in gold-financing facility exists (T&C Part B) | **High** |
| Named officers | Jignesh Ved (Founder & CEO); Lim Say Cheong (Chief Advisor, Digital Assets & Islamic Finance); Gagandeep Singh (Marketing). Navin D'Souza, CEO in the 2022 DMCC release, no longer listed | **Medium** |

## 1. What it is

A 1 gram = 1 token gold product issued from Dubai on the XDC (XinFin) network, live since 2022, sold both as a tradeable token (CGO) and as an app-based "ComTech Digital Gold" savings/buying product in AED. It is Shariah-certified and its main public credential is a 2022 partnership with DMCC under which gold bars are registered on **DMCC Tradeflow** warrants ([dmcc.ae](https://dmcc.ae/latest-news/dmcc-digitises-gold-trading-through-tokenisation-comtech-gold-bullion-backed-dmccs-tradeflow-platform), 10 Dec 2022).

Two things make it the most relevant comparator in this batch: it is the closest thing to a direct UAE precedent for what Aurumix wants to do, and it is the clearest evidence of how a Dubai gold token has actually handled (or avoided) the licensing question.

Note the dual-product structure. The `comtechgold.com` domain now redirects to **`cgold.ae`**, a retail app site with an AED price feed, KYC onboarding and a bank account: a retail deposit-taking-shaped business, not just a token.

## 2. Legal structure

What a holder owns, from the **Terms & Conditions dated 23 August 2022** ([cgold.ae/assets/pdf/Terms_and_Conditions.pdf](https://cgold.ae/assets/pdf/Terms_and_Conditions.pdf)), which is the only primary legal document published:

- **Clause 3.2:** each unit "represents undivided ownership and specific interest in one (1) gram of at least 999 purity gold in the Gold Reserves." So the claim is **direct co-ownership of an undivided interest**, not a creditor claim and not a trust. **Confidence: High.**
- **Clause 3.6:** the holder "expressly and irrevocably appoint[s] and authorize[s] the Digitization Entity for an indefinite period of time to be custodian, administrator and holder of the specific interest... by acting as **agent in possession** for You." Bailment/agency, indefinite and irrevocable.
- **Clause 3.4:** "Digital Gold is not intended to be a 'security'." An assertion of the issuer's intent, with no regulator having ruled on it. Report as assertion.
- **Clause 3.5** contains a striking carve-out: 100% backing is promised "however in rare cases wherein due to holiday or logistical issues, the Digitalization Entity is not able to back it up with Gold Reserves, **it can do so subject to a maximum limit of 10kgs** and it shall ensure to back it up... within 24 hours of the next business day." **A contractually permitted 10 kg unbacked float.** Against a last-published reserve of 111 kg that is a permitted ~9% under-backing window. This directly contradicts the "100% backed at all times" marketing.
- **Clause 15.4:** total issuer liability "shall in no circumstances exceed the fees received by the Digitization Entity." The ownership claim in 3.2 is therefore capped, in the event of a dispute, at fees collected.
- **Governing law: English law. Arbitration: LCIA, seat DIFC, one arbitrator, English** (17.6, 17.7). A UAE retail buyer's remedy is an individual LCIA arbitration, which is prohibitively expensive for a small retail holder. This is a material consumer-protection gap.

**Critically, clause 3.6 gives the issuer indefinite custody, and the entity holding that role is a DAFZA precious-metals trader with no financial-services authorisation and no client-money regime.**

## 3. Regulatory and compliance posture

This is the section the profile exists for. Here is exactly what was checked and what was found.

| Register checked | Searched for | Result |
|---|---|---|
| **VARA public register** (52 licensed VASPs) | Comtech, ComTech Gold, ComTech FZCO | **Not present.** No licence, no provisional permit, no registration |
| **DFSA / DIFC** | ComTech FZCO, Trade Fintech Ltd | **No DFSA financial services licence found.** Trade Fintech Ltd appears only as a DIFC-registered private company (non-regulated), per the whitepaper's own account |
| **ADGM FSRA** | Comtech, Trade Fintech | **Not found.** No FSP, no recognition. (For contrast, Tether Gold obtained ADGM Accepted Spot Commodity recognition in July 2026: that route exists and Comtech has not used it) |
| **DAFZA / DIEZ** | ComTech FZCO (DAFZA) | **Found. Licence 05069.** Activity: GOLD AND OTHER PRECIOUS METALS TRADING. Issued 21-Feb-2022, **expiry shown 20-Feb-2024** |
| **DMCC** | ComTech FZCO (DMCC) | **Found. Licence DMCC-889799**, cert/reg DMCC197166, a/c 407812. Activities: IT consultants, network consultancies, internet consultancy, software house. Formed 31-May-2023, issued 26-Jun-2023, **expiry shown 25-Jun-2024** |

Source for both licences is Comtech's own Company Registration page, [cgold.ae/companyregistration](https://cgold.ae/companyregistration). **Confidence: High** (issuer-published registry extract, self-certified).

**The findings that matter:**

1. **Neither licence permits token issuance to the public.** A DAFZA licence for "gold and other precious metals trading" authorises trading bullion. A DMCC licence for "software house / IT consultancy" authorises writing software. Neither is a virtual-asset authorisation. VARA's remit covers the Emirate of Dubai **including all free zones except DIFC**, which expressly includes DAFZA and DMCC. Issuing and offering a virtual asset to the public is a VARA-regulated activity. **So the answer to "does a DMCC trade licence permit token issuance to the public" is no, and neither does the DAFZA one. There is no separate authorisation we were missing: there is an absent authorisation.**

2. **Our hypothesis of a "Dubai gold-token path that routes around VARA" is not supported.** Comtech is not evidence of a legitimate alternative route. It is evidence that an operator which launched in 2022 (before VARA's regime bit) has continued operating without ever appearing on the register. That is an unremediated exposure, not a template. **Aurumix must not treat this as precedent.** Anyone advising that "Comtech does it on a DMCC licence, so we can too" is relying on a factual error about which licence, and a legal error about what it permits.

3. **The licences shown are expired.** The issuer's own page displays DAFZA expiry 20-Feb-2024 and DMCC expiry 25-Jun-2024, both long past as of 28 July 2026. The most likely explanation is that the page was simply never updated after renewal, which is the charitable and probably correct reading. But it is published as-is on the live site of a business currently taking retail deposits, and we cannot confirm current good standing from the public record. **Confidence: High that this is what is published; Not disclosed as to actual current licence status.**

4. **The FAQ makes an affirmative regulatory claim that is misleading.** It states: *"Is ComTech Gold regulated? Yes, ComTech Gold is regulated by Dubai Airport Free Zone Authority (DAFZA) and endorsed by local UAE government body DMCC... We strictly follow the regulatory guidelines towards the capital reserve, consumer protection, compliance, and anti-money laundering"* ([FAQ PDF](https://cgold.ae/assets/pdf/ComTech_Gold_FAQ_Final.pdf)). A free zone authority is a **company registrar and licensor, not a financial regulator**; it imposes no capital reserve or consumer-protection regime on a bullion trader. Telling retail customers this constitutes being "regulated" with "the highest form of protection" is the single most material disclosure problem found in this profile. **This is exactly the marketing-vs-legal gap the brief asks us to surface.**

5. **A third entity handles the money.** The live app configuration endpoint (`appapi.comtechgold.com/api/setting`) returns bank details in the name of **COMTECH CORE TRADING FZCO** at ZAND Bank. Customer funds are therefore received by an entity whose name appears on neither the DAFZA nor the DMCC certificate published on the site, and whose licence we could not locate. **Confidence: High** that this is the named account holder; **Not disclosed** as to that entity's licence and its relationship to the issuer.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian / vault | **Transguard** (Emirates Group company), UAE. T&C 4.1 permits storage "in the UAE **or elsewhere**" and via affiliates "anywhere in the world" | **High** |
| Allocated / segregated | T&C 4.2: segregated, not commingled. Whitepaper: 1 kg bars, 999 purity, identifiable by bar number | **High** (as contractual promise) |
| Published bar list | **Not disclosed.** No bar-number list is published anywhere. The whitepaper says bars "would be distinctly identifiable through their bar number"; no such list exists publicly | **High** (verified absent) |
| PoR feed | **None.** No Chainlink PoR, no oracle, no live attestation feed | **High** |
| Reserve attestation | **Self-issued letters on Comtech letterhead, signed "For ComTech FZCO". Not an independent auditor's report** | **High** |
| Latest attestation | **21 March 2025**, stating 111 × 1 kg bars: 19 kg on DMCC Tradeflow + 92 kg with "Vaulting Partner" | **High** |
| Smart contract audit | **Not disclosed.** No published smart-contract audit found | **High** |

**On the "monthly proof of reserve with published bar lists" in our working notes: that claim does not survive contact with the evidence. It is wrong on all three counts.**

The reserve history published on the site is not monthly, is not independent, and has stopped. Full published series:

| From | To | Opening | Deposit | Withdrawal | Closing |
|---|---|---|---|---|---|
| 01 May 2022 | 25 May 2022 | 0 kg | 100 kg | 0 kg | 100 kg |
| 26 May 2022 | 06 Jun 2022 | 100 kg | 4 kg | 0 kg | 104 kg |
| 07 Jun 2022 | 12 Jul 2022 | 104 kg | 17 kg | 0 kg | 121 kg |
| 13 Jul 2022 | 30 Aug 2022 | 121 kg | 1 kg | 0 kg | 122 kg |
| 31 Aug 2022 | 04 Jan 2023 | 122 kg | 2 kg | 0 kg | 124 kg |
| 05 Jan 2023 | 08 Mar 2023 | 124 kg | 17 kg | 0 kg | 141 kg |
| 09 Mar 2023 | 11 Oct 2023 | 141 kg | 3 kg | 0 kg | 144 kg |
| **12 Oct 2023** | **21 Mar 2025** | **144 kg** | **29 kg** | **62 kg** | **111 kg** |

Three observations:

1. **Frequency is irregular and lengthening**, from ~3 weeks to a single 17-month period. Calling this "monthly" is not defensible.
2. **The last period shows the first ever withdrawals: 62 kg out, a 23% net decline.** Gold left the vault. Nothing published explains why.
3. **Nothing has been published since 21 March 2025: over 16 months of silence** as of today. For a product whose entire value proposition is verifiable backing, a 16-month attestation gap is the finding.

**The reserve/supply mismatch.** Last published reserve is **111 kg**. On-chain `totalSupply` today is **39,000 CGO = 39 kg**. These do not reconcile, and the gap runs in the *over*-collateralised direction (72 kg more gold than tokens). The benign reading, which is probably right, is that the app-based "Digital Gold" book is unminted (customers hold ledger entries, not tokens), so vault gold backs both the 39 kg of tokens and a larger off-chain retail book. **But that reading is itself the problem: it means the majority of Comtech's customer liability is an off-chain database entry with no on-chain verifiability at all**, and the published reserve letters do not split the two. **Confidence: High** on both numbers; **Not disclosed** as to the reconciliation.

**Shariah certification (our notes said Amanie Advisors: now superseded).** The original certification was issued by **Amanie Advisors Ltd** in September 2022, making CGO the first Shariah-certified gold token in MENA ([Businesswire, 26 Sep 2022](https://www.businesswire.com/news/home/20220926005591/en/ComTech-Gold-%24CGO-Becomes-the-First-100-Gold-Backed-Token-to-Receive-Shariah-Certification-in-the-MENA-Region)). That is no longer the operative certification. The current document is a **fatwa dated 31 March 2026 from Sābiq Advisory**, signed by Dr Mohamed Ali Elgari (Chairman), Dr Muhammad Amin Ali Qattan and Dr Osama Al Dereai, which states expressly: *"This Fatwa supersedes the earlier fatwa dated 6 September 2022 issued by the previous Shariah Advisor and applies prospectively from the date of our appointment"* ([fatwa PDF](https://cgold.ae/assets/pdf/SABIQ%20FATWA%20-%20STANDARDIZED%20GOLD%20TOKEN%20PRODUCT%20(%E2%80%9CCGO%E2%80%9D)%20BY%20COMTECH%20FZCO.pdf)). **Confidence: High.** Two caveats: the fatwa **expressly excludes** "any distinct financing, leverage, or yield-generation mechanics" from its scope; and T&C 14.3 disclaims any warranty of Shariah compliance and makes the holder responsible for their own determination, while 18.1 bars the holder from ever challenging Shariah compliance. The certification is real; the contract makes it non-actionable.

## 5. Issuance

- Minting is centralised and discretionary. Token creation follows gold deposit; bars are registered on **DMCC Tradeflow warrants** and (per the March 2025 letter) split between Tradeflow-registered and vaulting-partner holdings.
- Retail issuance is via the ComTech Gold app after KYC. **Minimum purchase 0.5 g** (app API), with the FAQ elsewhere saying "as low as 0.5 gm". The whitepaper's older claim was 1 g.
- Institutional/wholesale route: gold suppliers named in the whitepaper as under discussion (StoneX); StoneX appears as a partner logo on the site.
- Pricing is issuer-quoted, not oracle-driven: the app API returns a buy rate and a sell rate in AED set by Comtech (at capture: buy 131.18, sell 128.89 AED/g, a **~1.8% round-trip spread**).
- **The permitted 10 kg unbacked issuance window (T&C 3.5) is an issuance mechanic, not just a disclosure**: the issuer may mint ahead of gold.

## 6. Redemption

**There is a direct and unresolved contradiction between the binding legal document and the marketing.**

| Source | Minimum redemption | Status |
|---|---|---|
| **T&C clause 8.1** (binding) | **1 kilogram**, and "in further denominations of one kilogram each" | **High** |
| FAQ + website | **10 grams**, thereafter multiples of 1 gram | **High** |
| Whitepaper §3.4 | 1 kg (1000 tokens) | **High** |
| Whitepaper §4.7 | 10 g "at a later stage... through Redemption Partners" | **High** |

The reconciliation is that 1 kg is the **contractual** right to bar delivery, while 10 g is a **discretionary retail** service delivered as minted coins (with making charges) or via "Authorized Partners" (jewellers, T&C clause 9, minimum 1 g exchange for jewellery). The retail 10 g route is a commercial accommodation, not a contractual entitlement. **A holder's enforceable redemption right is 1 kg: at ~$129/g that is roughly $129,000, which excludes essentially every retail holder.** For Aurumix this is the standard pattern: headline retail redemption that is not the legal right.

Other terms:
- Redemption fee **0.50%**, plus making charges and delivery at holder's cost.
- Collection in person at the vault or delivery; outside UAE, delivery is only to "the nearest Airport" with the customer handling customs.
- Orders are **irrevocable**: purchase, sale and delivery requests cannot be cancelled once placed (FAQ).
- Only the holder may redeem; on death, legal heirs may claim with death certificate and proof of heirship (a genuine parallel to Aurumix's Digital Will).
- **T&C 16.2 lets the issuer suspend redemption entirely** for force majeure "or on account of any technical issue faced **or otherwise**." "Or otherwise" is an unlimited discretionary suspension right.

## 7. Fees and revenue model

The published fee table and the live app disagree, and the difference is the whole revenue model.

**Website fee table** ([cgold.ae](https://cgold.ae) Fee Structure):

| Line | Rate |
|---|---|
| Transaction Fees | **Nil** |
| Custody Fees | **Nil** |
| Insurance Fees | **Nil** |
| Transfer Fees | 0.50% |
| Physical Gold Redemption Fees | 0.50% |

**Live app API** (`appapi.comtechgold.com/api/setting`, captured 28 Jul 2026):

| Line | Rate |
|---|---|
| Buy commission | **1.0125%** |
| Sell commission | **0.9950%** |
| Quoted buy/sell spread | ~1.8% round trip |
| AED payment charge | 1% |
| Card / Google Pay / Apple Pay | 2.4% |
| USD charge | 0.27% |
| VAT | 5% |

**So "Transaction Fees: Nil" is not what a customer pays.** A retail buyer pays roughly 1% commission plus up to 2.4% payment charge plus VAT plus the ~1.8% spread. The revenue model is **spread and commission at the point of sale**, not a custody fee. **Confidence: High** (live production endpoint).

**On custody specifically, which is Aurumix design question 1:** the marketing says "Custody Fees: Nil", but the FAQ discloses that custody is *"without charge for the first 24 months, and thereafter... a nominal fee to cover storage costs,"* with advance notice and the option to sell or take delivery. T&C 11.1.6 lists "Storage fees, which will include costs for the Vaults and insurance" as a chargeable line, and 11.4 lets Comtech change fees unilaterally, effective on posting, with continued use constituting acceptance.

**This is the single most useful data point in the profile for Aurumix.** Comtech resolves the grams-vs-cash custody dilemma by **choosing the third option: charge the holder nothing for custody and recover the cost in the buy/sell spread and commission at transaction time.** That keeps 1 token = 1 gram exactly intact (no peg drift, which is precisely the failure mode Aurumix identified), and it funds storage from transaction margin. The cost is that revenue is volume-dependent, which for a buy-and-hold savings product is thin, and Comtech has visibly hedged by reserving the right to introduce a storage fee after 24 months.

**Yield: none on the token.** But T&C **Part B, clause 20** (expressly outside Shariah certification) describes a **gold-financing facility**: Comtech may lease pooled gold reserves to "commercial parties in the gold and jewellery business" for up to 6 months in return for a "Margin". Holders opt in, their tokens are locked, the underlying gold is released to the financed party, and critically: *"The Digitization Entity will not be liable to the Financed Party or the Participating Digital Gold Holder and will simply facilitate the transaction. **The Participating Digital Gold Holders will take the risk** under the proposed transaction."* This is the same structure as ORO's Monetary Metals leasing, disclosed more honestly: the holder, not the issuer, eats a default. Whether it is live is **Not disclosed**.

## 8. Token architecture

- **Standard: plain ERC-20 equivalent (XRC-20) on XDC.** 18 decimals, name "Comtech Gold", symbol "CGO". Verified on-chain.
- **Not permissioned.** No ERC-3643, no whitelist/identity layer, no transfer restriction observed. Anyone can hold and transfer. This is the opposite of the direction Aurumix is leaning.
- **Contract:** `0x8f9920283470f52128bf11b0c14e798be704fd15`, bytecode ~8KB. Includes a `paused()` function, so **transfers are pausable by the issuer**.
- **Admin keys:** the `owner()` is `0xc639b48ea44e94f1a69da11974a29e6ddb8c6fa1`, held via an intermediate **contract** at `0x21f74fbf81d68291704805d085982000babbf096` (36KB bytecode). It did not respond to Gnosis Safe interface calls (`getOwners`, `getThreshold`), so it is **not a standard Safe multisig**. It is a custom ownership/admin contract. **Whether control is genuinely multi-party is Not disclosed**, and it cannot be established from the interface. For a token whose entire risk sits with the issuer, unverifiable admin control is a real gap.
- **Single chain, no bridge.** XDC only. This is a strategic weakness: XDC has thin DeFi and thin liquidity, which shows in §9.
- **No published smart-contract audit.** Note the blur the brief warns about: Comtech's marketing says it is "regularly audited", which refers to gold-stock letters, not code. **There is neither an independent reserve audit nor a smart-contract audit.**

## 9. Liquidity and market

Data as at 28 July 2026 (CoinGecko):

| Metric | Value |
|---|---|
| Price | ~$129.31 (tracks ~1 g gold) |
| Market cap | ~$5.04M |
| Circulating = total supply | 39,000 CGO |
| 24h volume | ~$814,566 |

Venue breakdown, which is the real story:

| Venue | Pair | 24h volume | Spread |
|---|---|---|---|
| **Bitrue** | CGO/USDT | **$814,072 (99.94%)** | 0.42% |
| BitMart | CGO/USDT | $280 | 3.17% |
| XSwap V3 (DEX) | CGO/USDC | $213 | 2.21% |

**Essentially all liquidity is one pair on one exchange.** Genuine on-chain DEX liquidity is roughly **$213 a day**. If Bitrue delists or halts, the market is gone.

**This is a second independent data point against the client's premium thesis (design question 6), and it is stronger than the PGOLD one.** PGOLD showed a big book with no market. Comtech shows the same pattern at smaller scale: a ~$5M token whose decentralised market is ~$200/day. Note also that CGO trades *at* gold parity with a tight 0.42% spread on its main venue: **there is no 3–8% sustained premium here.** A commodity token with real redeemability and market makers trades at parity, because arbitrage closes any gap. **Aurumix's 3–8% premium assumption is not supported by the one UAE gold token with a functioning market; if anything this is evidence that a working market actively prevents such a premium.**

Also note supply has *contracted*: reserves fell from 144 kg to 111 kg, and on-chain supply is 39 kg. This is not a growing book.

## 10. Distribution

- **App-first retail**, iOS and Android ("ComTech Gold", app v3.08), AED-denominated, KYC'd, 0.5 g minimum. This is closer to Aurumix's retail model than any other protocol in the batch.
- **Jeweller redemption network:** "Authorized Partners" (T&C 9), with **Kalyan Jewellers** as a named partner and its store locator linked from the site. Kalyan is a major India/GCC jeweller serving exactly the Indian-expat/NRI segment Aurumix targets. **This is the most directly transferable distribution asset in the profile.**
- **Referral mechanism: yes, and it is live.** The app config carries an active referral code (`LULU25`), which points to a tie-up with the Lulu retail group, another India/GCC mass-market channel. **Confidence: Medium** on the Lulu interpretation; **High** that a referral-code system exists in production.
- **Banking:** ZAND Bank (UAE digital bank) accounts in AED and USD. Getting a UAE bank to serve a gold-token business is non-trivial and is a genuine achievement to note.
- **Savings plan / SIP: none found.** There is no recurring-contribution or systematic investment product. The FAQ explicitly says there is **no lock-in** and **no joint accounts**. **So on Aurumix's core differentiator, Comtech does not compete: it sells one-off purchases, not a premium schedule.** The brief's expectation holds.
- **No agent/commission tier structure** found. Distribution is app + jeweller partners + referral codes, not a 3-tier network.
- Geography: UAE-centric (AED pricing, 800 COMTECH phone line, UAE doorstep delivery), with international delivery degraded to airport collection.

## 11. Recent developments

A dedicated recency sweep (Perplexity Sonar Pro, 18-month window) returned **no dated announcements, no regulatory developments, no listings or delistings, no incidents, no enforcement actions, and no partnerships** for Jan 2025 to Jul 2026. That null result is corroborated by the site itself: there is no news or announcements section with dated entries. Reverse chronological, what can be dated:

- **31 March 2026:** New Shariah fatwa issued by **Sābiq Advisory** (Dr Mohamed Ali Elgari, Dr Muhammad Amin Ali Qattan, Dr Osama Al Dereai), expressly superseding the 6 September 2022 Amanie fatwa and applying prospectively. Confirms a Shariah audit for FYE 2024 was completed by the previous board. **The change of Shariah advisor was not announced publicly anywhere we could find: it is only discoverable by reading the PDF.** **Confidence: High.**
- **21 March 2025:** Last published gold-stock letter. Reserves **111 kg**, down from 144 kg, reflecting 62 kg of withdrawals over the period from 12 Oct 2023. Split 19 kg on DMCC Tradeflow, 92 kg with vaulting partner. **Confidence: High.**
- **Since 21 March 2025 (16+ months):** No further reserve attestation published. **Confidence: High** (verified absent).
- **Undated, but current:** primary domain `comtechgold.com` now redirects to **`cgold.ae`**, and leadership has changed: **Navin D'Souza**, named as Comtech CEO in the December 2022 DMCC release, is no longer listed; **Jignesh Ved** is Founder & CEO. **Confidence: Medium** (site content, no dated announcement).
- **25 June 2024 / 20 February 2024:** Expiry dates displayed for the DMCC and DAFZA licences respectively on the live registration page.
- **Reported plans (issuer marketing, undated, unverified):** vault diversification to Singapore and Switzerland, gold-backed NFTs, listings on KuCoin and Gate.io. **Confidence: Low.** None corroborated.

**The pattern is a project that has gone quiet.** Reserves down 23%, attestations stopped, no announcements in 18 months, leadership turnover, expired licence dates on the site, and a live app still taking retail money. That combination deserves to be stated plainly.

## 12. Relevance to Aurumix

**Comtech is the closest UAE analogue to Aurumix that exists, and its main lesson is a negative one about regulatory strategy.**

**Question 4, regulatory route (the one we came for).** Comtech is *not* a viable precedent for avoiding VARA. It issues a gold token to the public from Dubai on a **DAFZA bullion-trading licence (05069)** and a **DMCC IT-consultancy licence (DMCC-889799)**, neither of which authorises virtual-asset issuance, and it appears on no regulator's register. The "Dubai gold-token path that routes around VARA" is not a path: it is a gap that has not yet been closed. Anyone proposing Aurumix replicate it should be shown that Comtech's own FAQ tells retail customers they are "regulated by DAFZA" with "the highest form of protection", which is the kind of statement that attracts enforcement rather than deflecting it. **Aurumix's ARVA-under-VARA plan, expensive as it is (~AED 100k application, 200k/yr, AED 1.5M capital, 6–9 months), remains the defensible route.** The cheaper-looking alternative is cheap because the bill has not arrived. If we want a genuinely lower-cost regulated route, the live option is **ADGM**, where Tether Gold obtained Accepted Spot Commodity recognition in July 2026: that is worth its own scoping, and it is a real finding from this pass.

**Question 1, custody fee mechanism (the most useful positive finding).** Comtech takes **option three**: custody is free to the holder, and cost is recovered from a ~1% buy/sell commission plus a ~1.8% quoted spread at transaction time. **The peg stays clean at exactly 1 token = 1 gram because nothing is ever deducted in grams.** This validates Aurumix's instinct to avoid gram-denominated fees. But note the catch, and it is severe for Aurumix specifically: **transaction-margin funding only works if people transact.** Aurumix is a buy-and-hold monthly SIP designed to discourage exit, so it would collect that margin once on the way in and then carry storage cost indefinitely with no further revenue. Comtech has visibly felt this, which is why the FAQ reserves a storage fee after 24 months. **Aurumix should assume it will need an explicit cash custody fee or a contribution-loaded charge, and should model storage cost against a holder who contributes $75/month and never sells.**

**Question 2, dividend funding.** Comtech pays **no yield on the token**, which is itself instructive: the closest UAE comparator concluded it could not or should not promise one. Its Part B gold-financing facility is the compliant-ish alternative Aurumix has been weighing, and its terms are worth copying in one respect and avoiding in another. Copy: it is **opt-in**, tokens are **locked** while lent, and terms are disclosed per-deal (counterparty, amount, tenor, margin). Avoid: it dumps counterparty default risk entirely on the holder while the issuer "will simply facilitate". Also note the Sābiq fatwa **expressly carves financing and yield generation out of Shariah approval**: for a Shariah-facing product, a yield mechanism is not covered by the gold certification and needs its own ruling. That is a direct constraint on Aurumix's ICS Dividend if it wants Islamic-market credibility.

**Question 3, token standard.** Comtech uses a plain, non-permissioned XRC-20 with a pausable contract and opaque admin control. It buys exchange listability (Bitrue) and costs any ability to enforce holder-level rights. **Aurumix's rights bundle (ICS standing, dividend entitlement, credit eligibility, buyback rights) would be destroyed by exactly this architecture on the first anonymous transfer.** Comtech is a clean illustration of why Aurumix's ERC-3643-plus-wrapper instinct is right: Comtech can afford ERC-20 precisely because its token carries no rights beyond "1 gram".

**Question 5, redemption.** Direct support for Aurumix's position, from an unexpected direction. Comtech advertises 10 g retail redemption but its **binding contractual minimum is 1 kg (~$129,000)**. So its "you own real gold, take it home" pitch is, legally, available only to holders roughly 1,700x larger than Aurumix's $75/month target customer. **Aurumix's no-physical-redemption stance is more honest than Comtech's, and should be framed that way**: we are explicit about cash-only exit rather than advertising a delivery right that the terms restrict to institutions. Also copy the death/succession handling (heir claims with death certificate and proof of heirship), which maps onto the Digital Will.

**Question 6, premium and liquidity.** Strong evidence against the 3–8% premium thesis, and it now has two independent legs. PGOLD showed AUM without a market. Comtech shows the sharper point: **where a gold token does have a functioning market with market makers and real redeemability, it trades at parity with a 0.42% spread.** A durable 3–8% premium is not a feature of healthy tokenised gold; it is a symptom of illiquidity or capital controls. Meanwhile Comtech's decentralised liquidity is ~$213/day against a $5M cap. **Aurumix should not build revenue projections on a sustained exchange premium.**

**Question 7, proof of reserve.** The cautionary tale. Comtech's attestations are **self-signed letters on company letterhead**, not independent audits, they were never monthly, no bar list was ever published despite the whitepaper promising bar-number identifiability, and they **stopped 16 months ago** after showing a 23% reserve decline. Yet the marketing says "regularly audited by independent third parties". **Aurumix can differentiate cheaply and credibly here**: a genuine independent attestation on a fixed published cadence, a real bar list, and a clear separation of "smart-contract audit" from "reserve attestation". Comtech proves the bar is low. It also proves that PoR practice **decays**: whatever cadence Aurumix commits to must be sustainable for years, because a lapsed schedule is worse than a modest one.

**Question 8, distribution.** The most transferable material in this profile. Comtech reaches Aurumix's exact target segment through **jeweller partnerships (Kalyan Jewellers)** and a **live referral-code system** (`LULU25`, apparently Lulu), plus a UAE banking relationship with **ZAND**. But it has **no savings plan, no SIP, no recurring contribution and no agent tiers**, and explicitly no lock-in. **Aurumix's monthly-premium SIP with a 3-tier agent network is therefore genuinely differentiated in this market**, not a copy of the incumbent. The competitive question is not whether Comtech does SIP (it does not) but whether Aurumix can win the same jeweller and retail-group channels Comtech already occupies.

**Question 9, wind-down.** Comtech has no wind-down plan, consistent with every other protocol in the batch. What it has is worse than silence: an FAQ answer asserting that because "every movement of Gold is endorsed and approved by... DMCC", then "in any unlikely adverse event happening to Company, the gold... will not be affected." **That is a reassurance without a mechanism.** A Tradeflow warrant records title to bullion; it does not create a bankruptcy-remote structure, and T&C 15.4 caps the issuer's total liability at fees received. There is no trustee, no security trustee, no independent custodian holding for holders. **Aurumix committing to a real ex-ante wind-down plan (named trustee, defined waterfall, pre-agreed liquidation agent) remains cheap and genuine differentiation, and Comtech's hand-waving answer is the perfect foil to quote against.**

**One additional cross-cutting warning.** The **contractually permitted 10 kg unbacked issuance window** (T&C 3.5) sits underneath a "100% backed at all times" headline. Aurumix will face the same operational temptation (settlement lag between customer payment and bullion purchase) and should decide *now* whether to disclose a float, size it, and cap it, rather than burying permission for it in clause 3.5.

## 13. Open items for verification

- [ ] Obtain current DAFZA licence 05069 and DMCC licence DMCC-889799 status directly from DIEZ/DAFZA and DMCC registrars: are both renewed and in good standing after the 2024 expiry dates published on the site?
- [ ] Identify **COMTECH CORE TRADING FZCO** (the ZAND Bank account holder): free zone, licence number, activities, and its legal relationship to ComTech FZCO. Customer money flows here.
- [ ] Confirm **Trade Fintech Ltd (DIFC 5102)** current status and shareholding of ComTech FZCO directly on the DIFC public register; confirm it holds no DFSA licence.
- [ ] Ask VARA (or confirm via a UAE counsel note) whether a pre-2022 free-zone gold-token issuer has any transitional relief, or whether Comtech is simply unlicensed. This determines whether our "no lawful route around VARA" conclusion is absolute.
- [ ] Scope the **ADGM FSRA Accepted Spot Commodity** route (as used by Tether Gold, July 2026) as a possible lower-cost alternative to VARA for the gold core. This may be the most valuable follow-up in the batch.
- [ ] Obtain any reserve attestation dated after 21 March 2025; if none exists, treat the 16-month gap as confirmed and note reserves last stood at 111 kg after a 23% decline.
- [ ] Reconcile 111 kg published reserve against 39 kg on-chain supply: confirm the off-chain app ledger explanation and establish how large the unminted retail book is and what evidences it.
- [ ] Establish control of admin contract `0x21f74fbf81d68291704805d085982000babbf096` (owner `0xc639b4...6fa1`): is it multi-party or a single key wrapper? Not a Gnosis Safe.
- [ ] Confirm whether the Part B gold-financing/leasing facility has ever been activated, and on what terms and counterparties.
- [ ] Verify the `LULU25` referral code is a Lulu Group commercial tie-up and obtain the commission terms; same for the Kalyan Jewellers redemption arrangement.
- [ ] Obtain the Sābiq annual Shariah compliance certificate for FYE 2025/2026 (the fatwa is conditional on annual recertification).
- [ ] Confirm whether any smart-contract audit exists for `0x8f99...fd15`.
