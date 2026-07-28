# CACHE Gold (CGT)

> **Correction to our own working note, stated up front.** Our standing brief says Cache Gold "wound down quietly with no post-mortem and the fate of residual gold unverified," and Part 3 of the landscape brief lists it alongside PMGT and Digix as a protocol that never published a wind-down plan. **Both statements are wrong and should be struck.** CACHE published a contractual compulsory-redemption mechanism (Clause 5A of its Terms of Service, effective 19 June 2025), gave at least three months' notice through defined channels, ran a redemption window, and executed a migration into PAXG. It is, on paper, **the only protocol in our entire set that documented its own wind-down in advance and then followed the document.** That makes it far more useful to Aurumix than a quiet death would have been: it is a live test of whether a well-drafted wind-down clause actually protects holders.
>
> The second finding is that it largely did not. **100,771.01 CGT remain outstanding today across 136 addresses, and the total supply has not moved by a single unit since before the snapshot.** The redemption paid out to two addresses. The rest is a claim on nothing.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | CGT | **High** |
| Status | **Wound down.** Ceased to be gold-backed 30 September 2025, 23:59:59 SGT | **High** |
| Issuer (marketing) | CACHE / CACHE Gold | **High** |
| Issuer (registry) | **CACHE PRIVATE LIMITED, Singapore UEN 201827110K, incorporated 8 August 2018** | **High** |
| Register status today | **LIVE COMPANY.** Not struck off, not dissolved, not in liquidation | **High** |
| Domicile | Republic of Singapore. Registered office 6 Changi South Street 3, #01-01 BOXPARK @ Chai Chee, Singapore 486128 | **High** |
| Backing claim | 1 CGT = 1 gram allocated fine gold in an Approved Vault (until 30 Sep 2025) | **High** |
| Chains | Ethereum mainnet only | **High** |
| Contract address | `0xf5238462e7235c7b62811567e63dd17d12c2eaa0` (ERC-20, 8 decimals) | **High** |
| Supply today | **100,771.01 CGT**, unchanged since before the wind-down snapshot | **High** |
| Holders today | **136 addresses** | **High** |
| Market cap / TVL | **Zero.** Tokens are contractually unbacked; no price feed | **High** |
| Regulatory status | Singapore **PSPM Dealer, Registration No. PS20190001508**, verified live on the MinLaw register | **High** |
| Subscription fee | Not disclosed (marketplace pricing, spread-based) | **Not disclosed** |
| Ongoing custody fee | **0.25% p.a. storage fee, deducted in CGT tokens on-chain** | **High** |
| Transfer fee | **Up to 0.10% of CGT transferred, deducted in CGT on-chain** | **High** |
| Inactivity fee | **0.50% p.a. on addresses dormant 3 years, in CGT** | **High** |
| Redemption fee | Marketplace-variable; plus VAT/GST and shipping at holder's cost | **Medium** |
| Advertised yield | **None.** Terms expressly deny any dividend or revenue share | **High** |
| Named officers | Gregor Gregersen (Director/CEO), Nizam Ismail (Director) reported; 4 officers on register | **Low** |
| Trustee | **None. No trustee, no bankruptcy-remote structure anywhere in the Terms** | **High** |

---

## 1. What it is

CACHE Gold was an Ethereum ERC-20 token, each unit representing one gram of allocated fine gold held in third-party vaults, issued by CACHE Private Limited of Singapore. The contract was deployed on **17 February 2020**. Its distinguishing pitch was bar-level transparency: the **GramChain** asset-tracking system published per-bar photographs, gross weight, purity, brand, **serial number** and vault location, refreshed by the vault personnel physically handling the bars, and broadcast to Ethereum. Redemption was offered in three forms: collection in person from a vault, insured shipping to a verified residential address, or sale to a participating gold dealer for fiat.

It is the best test case in our set precisely because it did the disclosure work properly. If bar serial numbers and a documented redemption right are worth anything at the moment an issuer stops operating, CACHE is where that value should show up.

The token is now defunct. Per the issuer's own notice dated **1 October 2025**, CGT "ceased to be backed by gold as of 30 September 2025, 23:59:59 (Singapore Time)" (https://cache.gold/).

---

## 2. Legal structure

**What a holder actually owned: an economic claim against the issuer, not title to gold, and not a trust interest.** This is the single most important structural fact about CACHE, and it is what determined the outcome.

The Terms of Service effective 19 June 2025 (https://cache.gold/assets/media/CACHE-Terms-of-Service-Effective-19th-June-2025.pdf) draw the line in two clauses that sit uncomfortably together:

> "1.1.1. CGT is an ERC-20 token on the Ethereum blockchain, representing the **beneficial ownership** of one (1) pure gram of Allocated Gold stored in an Approved Vault. A Token Holder therefore holds **the economic value** of the gold a CGT represents."

> "1.2.3. A Token Holder shall not have any other rights in relation to CACHE **other than the economic value of 1 gram of Gold per CGT**. CGT does not represent or confer any ownership right or governance right or stake, share or security or equivalent right, or any right to receive any dividend, share in revenue or any form of voting right or participation right in CACHE."

Clause 1.1.1 says "beneficial ownership" and then immediately reduces it to "the economic value." Clause 1.2.3 removes any ownership right at all. **Show both, because they disagree**: the marketing-facing sentence offers beneficial ownership of an identified allocated bar, and the operative sentence delivers a contractual value claim. When the issuer decided to close, the operative sentence governed. Holders had no proprietary interest they could assert over specific serial-numbered bars.

Clause 1.1.2 further disclaims that CGT is "a security token, a digital payment token, derivative, commodity, a share or security, an interest in a managed investment scheme, or any kind of financial instrument," and notes it "is not covered by any national deposit insurance scheme."

**No trustee. No bankruptcy-remote vehicle. No security interest.** A full-text search of the 22-page Terms returns no instance of "trustee," "trust deed," "bankruptcy remote," or any equivalent. The gold sat in third-party vaults under arrangements between CACHE and the vault operators, to which the token holder was not a party. **Confidence: High** (primary document, negative search recorded).

This is the structural difference between CACHE and a custody arrangement that would have survived the issuer. Because there was no trust and no trustee, at the moment CACHE chose to stop honouring the tokens there was no independent fiduciary with a duty to the holders and standing over the bars. The serial numbers identified gold that nobody was obliged, to the holder, to deliver.

---

## 3. Regulatory and compliance posture

**Regulator and licence, verified against the register:** CACHE PRIVATE LIMITED holds Singapore **Precious Stones and Precious Metals (PSPM) Dealer registration PS20190001508**, under the Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019, administered by the Registrar of Regulated Dealers at the Ministry of Law.

I verified this directly against the official government dataset rather than accepting the issuer's assertion. Querying the MinLaw "List of Registered Dealers" dataset on data.gov.sg (resource `d_e643dd525fb927ee16f54f093c73b490`, https://data.gov.sg/datasets/d_e643dd525fb927ee16f54f093c73b490/view) for "CACHE" returns exactly one record:

```
{'name': 'CACHE PRIVATE LIMITED', 'registration_number': 'PS20190001508'}
```

The issuer's self-description in Clause 7.1(b) is therefore accurate. **Confidence: High.**

**What that licence is and is not.** A PSPM dealer registration is an **anti-money-laundering registration**, not a financial services or capital markets licence. It obliges the holder to do KYC, record-keeping and suspicious transaction reporting when dealing in precious metals. It confers no prudential supervision, no client-asset segregation requirement, no capital requirement, and no conduct regime for token issuance. Clause 7.1(b) claims the registration means CACHE "is qualified to buy, sell, store, and issue precious metals or precious metals backed tokens like CGT." That is the issuer's characterisation; an AML dealer registration is not an authorisation to issue investment products, and the claim should be read as marketing.

**What I checked and did not find:**
- **No Monetary Authority of Singapore licence of any kind.** CGT was expressly structured to fall outside the Payment Services Act by disclaiming digital payment token status (Clause 1.1.2). No MAS Capital Markets Services licence, no Recognised Market Operator status, no MAS-approved prospectus.
- **No MAS enforcement action, reprimand or supervisory notice against CACHE Private Limited or CACHE Gold.** Searched; not found.
- **No regulator compelled or supervised the wind-down.** The closure was a commercial decision executed under the issuer's own contract terms.

**This matters for §12: CACHE was not killed by a regulator, and no regulator oversaw its exit.** There was no authority with jurisdiction to ask where the gold went.

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodians | **Brink's, Loomis, Dillon Gage IDS (International Depository Services), The Safe House** | **Medium** |
| Vault cities | Partner vaults reported across **Singapore, Dubai, Frankfurt, Dallas, Zurich**; per-custodian city mapping never published | **Low** |
| Allocated? | Yes, claimed: "Allocated Gold stored in an Approved Vault" (Clause 1.1.1) | **High** (as a claim) |
| Bar list with serial numbers | **Yes, published while operating.** Per-bar photos, gross weight, purity, brand, serial number, location via GramChain | **High** |
| Bar list today | **OFFLINE.** `explorer.cache.gold` returns HTTP 404 | **High** |
| PoR feed | GramChain, described as real-time, updated by vault personnel | **Medium** |
| **Reserve attestation** | **Never published by a named audit firm on a stated date. Not found.** | **High** (negative finding) |
| **Smart contract audit** | No published report located from any named auditor | **High** (negative finding) |

**The attestation gap, stated sharply.** Per the wave-1 correction that "audited" almost always means smart-contract audited and not reserve attested, I separate the two here, and for CACHE **neither is evidenced**. The strongest statement located is that the vaults themselves "are also independently audited and insured," which is an assertion about the vault operators' own general audit arrangements, not an attestation over the CGT gold reserve, and it names no firm and gives no date. A vault operator being audited as a business is not the same as an independent accountant confirming that a specific quantity of gold backing a specific token supply exists on a specific date.

So the transparency stack was: **very strong on granular bar data, entirely absent on independent verification.** GramChain showed you photographs and serial numbers supplied by the same commercial chain that had an interest in them being right. No third party ever signed a report saying the total matched the token supply.

**The transparency stack is now gone.** Verified live on 28 July 2026:

| URL | Status |
|---|---|
| `https://explorer.cache.gold/` | **404** |
| `https://cache.gold/whitepaper` | **404** |
| `https://cache.gold/cache-supply` | **404** |
| `https://cache.gold/cache-gold-fees` | **404** |
| `https://cache.gold/sell-your-gold` | **404** |
| `https://cache.gold/build` | **404** |
| `https://cache.gold/` | 200: wind-down notice only |
| `https://cache.gold/terms-of-service` | 200 |

**The Terms of Service still in force on the live site cite URLs that no longer exist.** Clause 1.1.1 directs holders to `https://cache.gold/whitepaper` and Clause 6.3.4 to `https://cache.gold/storage-fee-methodology`. Both are 404. The contract governing the tokens 136 addresses still hold points at documentation the issuer has deleted.

**GramChain itself outlived CACHE.** `gramchain.net` still resolves and serves (HTTP 403 to an automated request, indicating a live bot-protected host). Clause 9.5.2 explains why the two can be separated: the GramChain intellectual property belongs to **Little Bit Pte Ltd**, a different company, not to CACHE. The tracking technology was licensed in, so it did not die with the issuer, but the CGT-specific bar records it hosted are no longer reachable through any CACHE endpoint.

**Net effect on the serial numbers.** CACHE published bar-level serial numbers for years. Today there is no public record of which bars backed CGT, because the only interface that mapped tokens to bars has been taken down by the issuer. **The serial numbers were real while they did not matter, and unreachable the moment they would have.**

---

## 5. Issuance

Issuance ran through the **CACHE Marketplace**, a permissioned platform requiring registration and full KYC as a "Verified User" (Clauses 2.1.1 and 2.1.2: name, corporate information on shareholders/beneficial owners and directors, email, phone, residential address, date of birth or incorporation, government ID, proof of address, and in some cases source of funds or source of wealth). A Verified User delivered gold, or bought it from a participating dealer, and CGT was minted against it.

Note the asymmetry that runs through the whole design and drives the final outcome: **minting was permissioned and KYC'd, but the token itself was an anonymous bearer instrument.** Clause 1.2.1: "You become a CGT Token Holder by controlling the private key of an address holding CGT." Clause 5A.2 acknowledges this directly, referring to "Token Holders who do not have a CACHE Marketplace Account" and describing "CGT is a public bearer token."

CACHE knew, in the contract, that it had holders it could not identify or contact. It wrote the notice provisions around that fact rather than around solving it.

Reported venture funding of ~$17M in a Q3 2021 private round with Dillon Gage and Palisades Goldcorp named as backers appears on an ICO aggregator (https://icodrops.com/cache-gold/). No primary confirmation located, and Perplexity searching the issuer's own materials found none. **Confidence: Low.** Dillon Gage's confirmed role was as a vault operator (IDS) and participating gold dealer; whether it was also an equity investor is **not established**.

---

## 6. Redemption

While operating, redemption terms were genuinely good, and better than most of the set:

- **Three exit routes** (Clause 5.2): (a) in-person collection from an Approved Vault, (b) insured shipping to a linked residential address, (c) sale to a participating gold dealer for fiat.
- **Minimums as small as 100 grams** for physical bars, materially more retail-accessible than PAXG's or XAUT's practical thresholds.
- **Eligibility was open**, not restricted to undefined "qualified holders." This is a favourable contrast with several protocols in the set.
- **Frictions**: redemption required a Marketplace account and full KYC, so a bearer holder had to onboard first; the redemption transaction had to land within 10 minutes of the order to hold the locked price (Clause 5.3); it had to come from the Linked Ethereum Address (Clause 5.4); and VAT/GST, customs and shipping costs fell on the holder (Clauses 5.5.3, 5.6.3).

**The redemption right was extinguished by contract on 30 September 2025.** Clause 5.1 opens "You may, at any time, **subject to clause 5A**, redeem your CGT tokens." Clause 5A is the kill switch, examined in §11.

---

## 7. Fees and revenue model

**This section is the direct answer to the wave-1 instruction to test CACHE for the PMGT commercial-abandonment pattern. The answer is that the pattern does not fit, and the reason it does not fit is more interesting than if it had.**

| Fee line | Rate | How collected | Confidence |
|---|---|---|---|
| Transfer fee | Up to **0.10%** of CGT transferred | **In CGT tokens, automatically on-chain**, whenever a transfer is initiated (Clause 6.1.1) | **High** |
| Storage fee | **0.25% per annum** | **In CGT tokens**, collected "every time a transaction is initiated on the Ethereum Address holding the CGT tokens" (Clause 6.2.1) | **High** |
| Inactivity fee | **0.50% per annum** on addresses with no CGT transaction for 3 years, in lieu of the storage fee | **In CGT tokens**, on the balance as at the date of inactivity (Clauses 6.3.1–6.3.2) | **High** |
| Redemption / marketplace fees | Variable, quoted in the Marketplace | Cash / deducted from proceeds (Clause 6.4.1) | **Medium** |
| Advertised yield | **None** | Clause 1.2.3 expressly denies any dividend or revenue share | **High** |

**CACHE did charge, and PMGT did not. That is the key contrast.** PMGT died of commercial abandonment under a zero-fee model: no revenue meant no internal advocate. CACHE ran a **0.25% p.a. storage fee plus a 0.10% transfer fee plus a 0.50% p.a. inactivity fee**, which on the face of it is a real revenue model, and it is close to the *only* protocol in our set that charged an ongoing custody fee at all. The wave-1 finding that "zero ongoing custody fee is the near-universal norm" holds across PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus and PGOLD. **CACHE is the exception that charged, and it is also the one that closed.**

**But the collection mechanism made the fee largely theoretical, and this is the finding that matters most for Aurumix's Question 1.** Read Clause 6.2.1 carefully: the storage fee accrues at 0.25% per annum but **is only actually collected "every time a transaction is initiated on the Ethereum Address holding the CGT tokens."** A holder who bought CGT and never moved it paid nothing, indefinitely, no matter how much storage cost accrued in the meantime. Revenue was therefore a function of **transaction frequency, not assets under management.**

That is exactly backwards for a gold savings product. The behaviour a gold token is designed to attract, buy and hold for years, is the behaviour that generates zero revenue while consuming real vault cost every single day. CACHE's own inactivity fee, a 0.50% p.a. charge on 3-year-dormant addresses, is the tell: it is a patch bolted on to reach precisely the holders the storage-fee mechanism could never touch. And it too could only be realised on a transaction.

Now run the arithmetic on what that produced. Total supply at the end was **100,771 grams**, roughly 3.24 tonnes... no: 100.77 kg. At a gold price around $3,800/oz in 2025, that is roughly **$12.3M of AUM**. A 0.25% annual storage fee on $12.3M is about **$31,000 per year gross**, and CACHE only collected the fraction of that triggered by actual transactions. The contract shows **10,200 transfers over its entire five-and-a-half-year life**, an average of about five per day. Against Singapore staffing, four vault relationships across multiple countries, insurance, KYC compliance under the PSPM Act, and the GramChain licence from Little Bit Pte Ltd, a five-figure annual gross fee take is not a business.

**So the corrected diagnosis is this: CACHE did not die of charging nothing, like PMGT. It died of charging a fee that its own collection mechanism prevented it from actually collecting, on an asset base far too small to support the operation.** The disease is the same, revenue that could never cover the cost of custody. The mechanism differs, and the difference is instructive: **having a fee on paper is not the same as having revenue.** No enforcement action, no hack, no reserve shortfall, no scandal, and no regulator involved. Commercial non-viability, confirmed.

**The in-kind fee mechanism is directly relevant to Aurumix's Question 1 and to the PAXG dilution clause from wave 1.** CACHE deducted its fees **in grams of gold** by taking CGT tokens, not in cash. For a 1-token-1-gram product, this is peg-breaking in the same way the Paxos mint-to-self clause is: the fee reduces the holder's gram count rather than the gold-per-token ratio. Aurumix's peg is grams ÷ tokens, so an in-kind deduction that burns tokens and gold proportionally would be peg-neutral, but CACHE's specific design, deducting tokens on transfer, is a template of how *not* to fund custody: it taxes exactly the activity a savings product wants to encourage and exempts exactly the behaviour that costs the issuer money.

---

## 8. Token architecture

- **Standard**: plain **ERC-20**, 8 decimals, Ethereum mainnet only, contract `0xf5238462e7235c7b62811567e63dd17d12c2eaa0`, deployed **17 February 2020**. No bridge, no multi-chain deployment.
- **Permissioned?** **No.** Free transfer to any address. Minting and redemption were permissioned and KYC-gated at the marketplace layer, but the token in circulation was an anonymous bearer instrument. **This is the architectural decision that produced the orphaned supply in §11.**
- **Fee logic in the contract**: the transfer, storage and inactivity fees were enforced in the token contract itself, deducting CGT on transfer. Clauses 6.1.2 and 6.2.2 construct this as an obligation that runs with the token: "By acquiring CGT tokens, Token Holder agrees to assign the obligation to pay such fees to subsequent Token Holders... Likewise, by receiving transfers of CGT tokens, Token Holders agree to accept the assignment of such obligation." An elegant piece of drafting that binds a bearer holder who never signed anything, and CACHE relied on the same bearer-consent theory for the compulsory redemption in Clause 5A.7.
- **Admin keys**: the contract has an owner at `0xb779efeeda6cf887b80bc386e7eb9fdced6753f6`, which is the same address that executed the PAXG airdrop. **No published smart contract audit located from any named firm.**
- **Contract still live**: not paused, not self-destructed. Transfers still execute. Three transfers occurred as recently as **26 July 2026**, two days ago (all zero-value spam). The token functions perfectly; it just represents nothing.

---

## 9. Liquidity and market

One paragraph, per the wave-1 instruction not to re-argue the premium thesis.

CACHE was a very small protocol. Final supply was **100,771 grams (~100.8 kg, ~$12.3M at 2025 prices)**, and a dated 2020 audit walkthrough put supply at only 34,301 grams, so the token roughly tripled over five years and never reached scale. **136 holders.** **10,200 transfers over its entire life**, about five per day. Listings were thin: NBX (Norwegian Block Exchange) is the one confirmed venue, and Silver Bullion Singapore offered it. No meaningful DEX liquidity was located; no daily volume data is published for its final two years. There is no price feed today. CACHE adds one more data point at the far illiquid end of the spectrum, consistent with the settled conclusion: it had no market capable of expressing a premium, and its problem was never pricing but that ~$12M of AUM cannot pay for four vault relationships in five cities. **The distribution is now grotesquely concentrated: one address holds 96.03% of the entire remaining supply.**

---

## 10. Distribution

Direct-to-consumer through the CACHE Marketplace, plus exchange listings and bullion-dealer partnerships (Silver Bullion Singapore, Dillon Gage as a participating dealer). Target segment was gold investors wanting bar-level provenance, and B2B tokenization-as-a-service for other asset issuers.

**No savings plan, no recurring-purchase or SIP mechanism, no referral programme, no affiliate scheme, no agent network, no tiering.** Searched the Terms and all surviving materials; none found. This is consistent with the wave-1 pattern: **no protocol in the set has built anything resembling Aurumix's monthly-contribution agent-network model.** For CACHE the absence is doubly relevant, because a recurring-contribution product generates recurring transactions, and recurring transactions were the only thing that triggered CACHE's storage fee. A savings-plan distribution model would have partially fixed its revenue problem by accident.

---

## 11. Wind-down timeline

Dated, reverse chronological. On-chain facts verified directly against Ethereum mainnet via RPC and the Ethplorer API on 28 July 2026.

| Date | Event | Source / verification |
|---|---|---|
| **28 July 2026 (today)** | **CGT total supply: 100,771.01 tokens across 136 holders. Unchanged.** Contract live and transferable. Tokens are contractually unbacked and worthless | `eth_call totalSupply()` at current block |
| **26 July 2026** | Three zero-value spam transfers, the most recent activity on the contract | Ethplorer token history |
| **28 July 2026** | **Cache Private Limited remains a LIVE COMPANY on the ACRA register.** Not struck off, not dissolved, no liquidator appointed, 10 months after ceasing to honour its tokens | opengovsg.com/corporate/201827110K; recordowl.com/company/cache-private-limited |
| **28 July 2026** | **PSPM Dealer registration PS20190001508 still listed on the MinLaw register of registered dealers** | data.gov.sg dataset `d_e643dd525fb927ee16f54f093c73b490`, queried directly |
| **28 July 2026** | **Transparency stack confirmed offline**: `explorer.cache.gold`, `/whitepaper`, `/cache-supply`, `/cache-gold-fees`, `/sell-your-gold`, `/build` all return HTTP 404. Only the homepage notice and the Terms of Service survive | Direct HTTP requests |
| **17 November 2025** | **Second and final airdrop payment: 15.785912 PAXG (491.0 g) to a single address** (`0x8249f32c...`), block 23817845. This is 7 weeks *after* the compulsory redemption date and 17 days after the 31 October inquiry deadline, so it appears to be a manually handled late claim | `eth_getLogs` on PAXG contract, sender = CACHE owner address |
| **18 November 2025** | That recipient immediately swapped the entire 15.79 PAXG for ~$62,479 USDC | Ethplorer address history |
| **31 October 2025** | Deadline for eligible holders who did not receive PAXG to contact support@cache.gold. **After this date the issuer offered no further route to anything** | https://cache.gold/ |
| **1 October 2025** | **Airdrop executed: 60.180957 PAXG (1,871.8 g) to a single address**, blocks 23480178 and 23480280 | `eth_getLogs` on PAXG contract |
| **1 October 2025** | CACHE publishes notice: "the airdrop of Pax Gold (PAXG) tokens has been **successfully completed** in accordance with the compulsory redemption process set out in Clause 5A" | https://cache.gold/ |
| **30 September 2025, 23:59:59 SGT** | **Compulsory Redemption Date.** CGT ceases to be backed by gold and is "no longer recognized, honored, or redeemable by CACHE." Snapshot taken at the last block before this time | Clause 5A.4; https://cache.gold/ |
| **26 September 2025, 23:59:59 SGT** | Last date for manual redemption of CGT for physical gold or fiat through the CACHE website | https://cache.gold/ |
| **~19 June 2025** | **Compulsory Redemption Notice period begins.** Terms of Service effective this date carry the all-caps wind-down warning and the new Clause 5A. Clause 5A.2 requires at least 3 months' notice; 19 June to 30 September is 3 months and 11 days, so the notice period was honoured to the letter | Terms of Service effective 19 June 2025 |
| **17 February 2020** | CGT contract deployed on Ethereum mainnet | Contract creation tx `0x0b73a1a3...` |
| **8 August 2018** | CACHE PRIVATE LIMITED incorporated in Singapore, UEN 201827110K | ACRA register |

### What actually happened to the gold

**Established with certainty:**

1. **Two addresses were paid, and only two.** Scanning every PAXG `Transfer` event emitted from the CACHE owner address `0xb779efee...` across blocks 23,350,000 to 23,950,000 (covering September 2025 through January 2026) returns **six log entries, of which four are zero-value Paxos fee-address entries. The entire compulsory redemption consisted of two real payments: 60.180957 PAXG on 1 October 2025 and 15.785912 PAXG on 17 November 2025.** Total distributed: **75.9669 PAXG = 2,362.8 grams of gold.**

2. **Total supply never moved.** CGT `totalSupply()` at block 23,479,000 (immediately before the 30 September 2025 snapshot) was **100,771.01**. At the current block it is **100,771.01**. Identical. **The tokens were never burned.** CACHE did not retire the supply it had de-backed; it simply stopped recognising it and left it circulating.

3. **The arithmetic of the gap.** Roughly **2,362.8 grams** were settled in PAXG against a token supply of **100,771 grams**. That is **2.3% of the outstanding supply**. The remaining **~98,408 grams (98.4 kg, roughly $12.0M at 2025 gold prices) went to holders who received nothing.**

**Where the unsettled gold went: cannot be established from public sources, and I am stating that rather than inferring it.** Specifically, I checked and did not find:

- Any statement by CACHE, on the surviving notice page or in the Terms, of what was done with the physical bars that backed the un-redeemed ~98 kg. The notice says only that tokens "ceased to be backed by gold." **It never says what happened to the gold.**
- Any bar list, final reserve statement, or closing GramChain snapshot. The explorer is 404.
- Any liquidator's or trustee's report, because there is no liquidation and there was never a trustee.
- Any independent attestation of the reserve at any point, including at wind-down.
- Any MAS or MinLaw filing, notice or supervisory statement about the disposition of the assets.

**The three possibilities are all consistent with the public record, and nothing distinguishes them.** The bars may have been sold to fund the ~2,362 g of PAXG purchased for the airdrop, with the remainder retained by CACHE; the bars may have been sold and the proceeds retained; or a large fraction of the supply may have already been redeemed by holders before the deadline with the tokens left in circulation unburned. **The last of these is quite plausible and would be the benign reading**, but I cannot confirm it, because CACHE never burned redeemed tokens and never published a final reconciliation. **That is precisely the problem: the issuer's own choice not to burn and not to publish makes it impossible for anyone outside to tell whether holders were made whole or not.** A protocol that published bar serial numbers for five years has left no way to answer the only question that ultimately mattered.

### The orphaned tokens

**Yes, tokens remain outstanding today with no redemption path. 100,771.01 CGT across 136 addresses.** Every one of those holders has a claim on nothing, and Clause 5A.7 has already extinguished their right to complain:

> "5A.7 By continuing to hold CGT tokens, Token Holders (including Tokens Holders who are not eligible to be airdropped PAXG tokens...) expressly agree to this compulsory redemption mechanism as set out in this clause 5A and **waive any right to further redemption, refund, or legal claim against CACHE** following the Compulsory Redemption Date. For the avoidance of doubt, **this waiver shall apply to all Token Holders, including those who do not have a CACHE Marketplace Account.**"

The waiver was drafted to bind precisely the people the issuer knew it could not reach.

**The single largest casualty is visible on-chain and worth naming.** Address `0xd4033ea2ec53a26d6295f6f375d5c6afbe788660` holds **96,771.41 CGT: 96.03% of the entire remaining supply, ~96.8 kg of gold, roughly $11.8M at 2025 prices.** Its history is that of a patient accumulator: 29 separate purchases from a single counterparty between 2022 and **15 January 2025**, then nothing. It received **no PAXG**. It holds zero ETH, so it cannot even pay gas to move the worthless tokens. It has been silent since January 2025, which is **five months before the wind-down notice was published in June 2025.**

**This is the whole lesson in one address.** A holder who did exactly what a gold savings product tells you to do, buy steadily and hold, stopped checking in eight months before the notice, and lost the entire position. Clause 5A.2's notice mechanism, publication on the website, in the marketplace, by email to Verified Users, on Etherscan and on social media, was contractually impeccable and operationally useless against a bearer holder who was not watching. **Notice published is not notice received.**

I cannot establish whether that address belongs to a person who lost $11.8M, an exchange or custodian omnibus wallet, or an entity that had already redeemed the underlying gold off-chain and abandoned the tokens. The distinction is enormous and **is not determinable from public sources**, again because CACHE did not burn redeemed tokens.

### Did holders get notice? Yes, and it was better than any other failure in our set

To be fair to CACHE, and the fairness is the point:

- **Clause 5A.2 required at least three months' notice** through five channels, including explicitly "public blockchain channels, including but not limited to the CGT token page on Etherscan," specifically to reach non-account holders.
- **The notice period was honoured.** 19 June 2025 to 30 September 2025 is over three months.
- **A redemption window was kept open** to 26 September 2025 for physical gold or fiat.
- **A default settlement was provided**, the PAXG airdrop, so a passive holder was not simply expropriated but converted into the most liquid equivalent gold token available, at a clean weight-based ratio with no discretionary price applied ("No fiat or market price valuation will apply").
- **A post-hoc remedy window** ran to 31 October 2025.

**This is a genuinely well-designed wind-down, and it still left 96% of the supply stranded.** That is the finding. The failure was not in the drafting. It was in the architecture: **an anonymous bearer token cannot be reliably contacted, and a contract cannot fix that by declaring publication to be sufficient notice.**

---

## 12. Relevance to Aurumix

CACHE is the most valuable failure in the set for Aurumix, because it is the only one that tried to do this properly. Its lessons are about execution, not intent.

### 12.1 The wind-down question (Question 9): the answer is now much sharper than "publish a plan"

Our brief says "No failed gold token published a wind-down plan. Aurumix committing to one ex ante is cheap differentiation." **That is factually wrong, and the correction improves the recommendation.** CACHE did publish one, in advance, in its Terms, with a defined notice period, a defined redemption window and a defined default settlement. It executed it as written. **And 96% of the supply was still stranded.**

So the differentiator for Aurumix is not "publish a wind-down plan." Everyone can copy a clause. The differentiator is **publishing a wind-down plan that is architecturally capable of working**, which requires four things CACHE lacked:

1. **A trustee or equivalent independent fiduciary holding the gold**, so that the issuer's decision to stop operating does not extinguish the holder's claim. CACHE had none, and Clause 1.2.3 reduced "beneficial ownership" to "economic value" the moment it was tested.
2. **A holder registry, so notice can be delivered rather than published.** See 12.2.
3. **A commitment to burn tokens on redemption**, so that outstanding supply is a truthful measure of outstanding claims. CACHE's failure to burn is why nobody, including me, can now tell whether its holders were made whole.
4. **A final published reconciliation**: bars in, tokens out, gold disposed, at wind-down. CACHE deleted its bar list instead.

Aurumix should commit to all four, and should say plainly that it is doing so *because* the best-documented wind-down in the sector still failed without them.

### 12.2 The permissioned-token question (Question 3): CACHE is the strongest evidence yet for ERC-3643

The brief already leans to a permissioned base because ICS standing, dividend entitlement, credit eligibility and buyback rights all break on an anonymous DEX transfer. **CACHE supplies a much blunter argument: an anonymous bearer token cannot be wound down.**

CACHE knew its holders at mint (full KYC, source of funds, beneficial ownership) and then deliberately issued them a bearer instrument that severed that knowledge. When it needed to reach those people, it could not. It drafted around the gap (Clause 5A.2's publication-is-notice provision, Clause 5A.7's waiver binding non-account holders) rather than closing it, and the drafting did not save the holders.

**With a permissioned register, Aurumix's wind-down is a mailing list and a pro-rata distribution to known wallets. With a bearer token, it is a website notice and a 96% orphan rate.** This is the cost side of the ERC-20 choice, and it should go into the Question 3 write-up as the decisive argument. It also directly supports Aurumix's existing decision on **no physical redemption with cash-only buyback**: a cash buyback to a KYC'd holder of record is a wind-down mechanism that actually reaches people.

### 12.3 The custody fee question (Question 1): a working answer, from a protocol that got it wrong

Wave 1 settled that zero ongoing custody fee is the norm. **CACHE is the counter-example that charged, and it is instructive precisely because its fee still failed.**

The lesson is not "do not charge." It is **"do not build a fee whose collection depends on activity when your product is designed to be held."** CACHE's 0.25% p.a. storage fee was only collected on a transaction. A five-year buy-and-hold customer, the ideal customer for a gold savings plan, paid nothing while costing the issuer vault fees every day. The 0.50% inactivity fee was an admission of the flaw and could itself only be realised on a transaction.

**For Aurumix, whose entire model is monthly contributions from long-horizon savers, this is a direct hit.** Three implications:

- **The recurring SIP is a revenue asset, not just a distribution mechanism.** A monthly contribution is a recurring, predictable touchpoint at which a cash fee can be assessed. CACHE had no such touchpoint. Aurumix does, and should design the custody fee to be collected at contribution time.
- **Charge in cash, as the brief leans.** CACHE deducted fees in grams, which for a 1-token-1-gram product breaks the peg exactly as the Paxos mint-to-self clause does. Aurumix's peg (grams ÷ tokens) tolerates in-kind better, but the cash route avoids the argument entirely and is collectable at the SIP moment.
- **Model the AUM floor.** CACHE ran four vault relationships across five cities on ~$12M of AUM and could not survive. Aurumix should compute the AUM at which its own custody, compliance and agent-commission costs are covered, and treat that as a go/no-go threshold rather than a milestone. **The failure mode for a gold token is not a hack, it is being too small to pay for the vault.** That is now two of two failures in our set (PMGT and CACHE) that died of it.

### 12.4 Proof of reserve (Question 7): serial numbers are a liveness feature, not a solvency guarantee

CACHE had **the best bar-level transparency in the entire set**: per-bar photos, weight, purity, brand, serial number, vault location, updated by the handlers. It had **no independent reserve attestation, ever.** And **all of it went offline** the moment the issuer stopped paying for hosting.

Three rules for Aurumix's PoR design follow directly:

- **A bar list is not an attestation.** CACHE's bar data came from the commercial chain that had an interest in it being right. Aurumix needs a named firm, a stated scope, a stated date, and a recurring schedule. Publish the attestation alongside the bar list and never let marketing blur them.
- **Transparency hosted by the issuer dies with the issuer.** CACHE's Terms still cite `/whitepaper` and `/storage-fee-methodology`, both 404, in the contract governing tokens people still hold. Aurumix should place its bar list and attestations somewhere that survives it: a trustee, an auditor's own site, IPFS with content hashes committed on-chain, or all three.
- **Burn on redemption, always.** CACHE's decision to leave 100,771 de-backed tokens circulating is the single reason the fate of its gold is now unknowable. Supply must equal claims, or the transparency is decorative.

### 12.5 Regulatory route (Question 4): an AML registration is not a licence, and nobody supervised the exit

CACHE's PSPM registration is real and verified, but it is an **anti-money-laundering dealer registration**, not a financial services licence. It carried no client-asset segregation, no capital requirement, no conduct regime, and it gave no regulator any locus to ask where the gold went. Clause 7.1(b)'s claim that the registration meant CACHE was "qualified to... issue precious metals or precious metals backed tokens like CGT" is issuer characterisation, not a regulatory permission.

This is the same shape as the Comtech finding (DAFZA precious-metals licence that does not permit public token issuance) and reinforces the wave-1 correction that there is no cheap licensing route that actually covers token issuance. **The relevant point for Aurumix's VARA cost-benefit is that the expensive licence buys something specific: a supervisor with standing over the assets at the moment of failure.** CACHE had none, which is why its wind-down was answerable to nobody and why the ~98 kg is untraceable. That is worth pricing into the AED 100k application and 200k/yr supervision, and it is worth saying to the client in exactly those terms.

### 12.6 What CACHE does not speak to

Nothing on yield or dividend funding (Question 2): CACHE paid no yield and Clause 1.2.3 expressly denied any dividend or revenue share, so it offers no read on the ICS Dividend problem. Nothing on the instrument split (Kinesis KVT pattern): CACHE had a single token and no separate security. Nothing on ADGM or the Streamex gold-leasing lead. The premium thesis (Question 6) is settled and CACHE adds only a confirming illiquid data point. No savings-plan or agent-network precedent (Question 8), consistent with the rest of the set.

---

## 13. Open items for verification

- [ ] **Obtain a paid ACRA business profile for UEN 201827110K** to confirm current status, the four named officers, shareholders, the date of the last annual return, and whether any strike-off application or liquidator appointment has been filed since September 2025. Free mirrors show "Live Company" but do not show filing history.
- [ ] **Establish the fate of the ~98,408 grams of unsettled gold.** Ask CACHE directly at support@cache.gold whether the bars were sold, retained or delivered, and whether a final reconciliation exists. Record the non-response if there is one: that is itself citable.
- [ ] **Determine how much CGT was redeemed for physical gold or fiat before 26 September 2025.** This is the single fact that separates the benign reading (holders exited, tokens left unburned) from the alarming one (holders were stranded). CACHE never published it and never burned tokens, so it may only be obtainable from the issuer.
- [ ] **Identify address `0xd4033ea2ec53a26d6295f6f375d5c6afbe788660`** (96.03% of remaining supply, ~96.8 kg). Determine whether it is an exchange/custodian omnibus wallet or an individual, and whether it received any off-chain settlement. Its counterparty `0xc8bf2dbd...` supplied all 29 of its purchases and may be identifiable.
- [ ] **Retrieve an archived CACHE Explorer bar list** from the Wayback Machine (snapshots confirmed to exist, e.g. `web.archive.org/web/20250116193557/https://cache.gold/cache-supply`) and capture the final published serial numbers and vault allocations before they age out. **Do this soon.** Note: web.archive.org was not directly fetchable from this environment; retrieve manually or via a different tool.
- [ ] **Confirm the current status of PSPM registration PS20190001508** with the Registrar of Regulated Dealers, including whether it has been renewed since the company ceased token operations, and whether MinLaw was notified of the wind-down.
- [ ] **Confirm per-custodian vault cities** for Brink's, Loomis, Dillon Gage IDS and The Safe House, and whether any of them holds or held gold attributable to CGT after 30 September 2025. The Safe House and Silver Bullion Pte Ltd (Gregor Gregersen) are the most promising line of enquiry given the reported directorship.
- [ ] **Verify the reported officers** (Gregor Gregersen as Director/CEO, Nizam Ismail as Director) against the ACRA profile. Currently Confidence: Low, from a single company directory.
- [ ] **Establish the relationship between Cache Private Limited and Little Bit Pte Ltd** (owner of the GramChain IP per Clause 9.5.2), including common ownership, and whether Little Bit continues to hold CGT bar records that could resolve the gold question.
- [ ] **Confirm whether the ~$17M Q3 2021 raise (Dillon Gage, Palisades Goldcorp) actually occurred.** Currently sourced only to an ICO aggregator. If real, it sharpens the commercial-failure narrative considerably: $17M raised against ~$12M of AUM at closure.
- [ ] **Check for any Singapore court filing** involving Cache Private Limited (winding-up petitions, creditor claims, holder litigation) since September 2025.
