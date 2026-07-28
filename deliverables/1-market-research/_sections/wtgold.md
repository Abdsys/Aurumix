# WisdomTree Gold Token (WTGOLD)

> ⚠️ **Read this first: the brief's premise for this protocol is wrong, and the correction is the most valuable thing in this profile.**
>
> WTGOLD was assigned to us as "a transfer-agent-recorded fund share rather than a bearer custody receipt," on the theory that it is a regulated fund wrapper offering a third path against the ARVA-commodity-token route. **It is not.** WisdomTree runs **two structurally unrelated tokenised businesses** and the inherited framing has fused them:
>
> 1. **WT Gold (WTGOLD)** is a **bearer document of title** under **Articles 1, 2 and 7 of the New York UCC**, issued by a bailee. It is not a fund, not a security, not registered with the SEC, and has **no transfer agent**. It is, in legal substance, a **digital warehouse receipt**: closer to Comtech or Cache Gold than to anything in the fund world.
> 2. **WisdomTree Digital Funds** (WTGXX and ~14 siblings) *are* 1940 Act registered mutual funds whose shares are recorded by a registered transfer agent with a blockchain mirror. **None of them is a gold fund.** A full-text search of the entire 374,000-character WisdomTree Digital Trust prospectus returns **zero occurrences of the word "gold."**
>
> The transfer-agent-recorded-fund-share model the brief wants assessed **does exist and is genuinely the best answer in the landscape to the securities-classification problem**, but WisdomTree has deliberately **not** applied it to gold. Why it did not is the actual finding, and it is developed in §12.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | WTGOLD (marketed in-app as "Gold" / "Digital Gold") | High |
| Issuer (marketing) | "WisdomTree" / WisdomTree Prime | High |
| Issuer (legal, per User Agreement) | **WisdomTree Digital Trust Company, LLC ("WT TrustCo")** acts as **bailee and issuer of the document of title**; **WisdomTree Digital Movement, Inc.** is the Delaware counterparty operating the app | High |
| Ultimate parent | WisdomTree, Inc. (NYSE: WT), SEC CIK 0000880631 | High |
| Domicile | WT TrustCo: New York limited purpose trust company. WT Digital Movement: Delaware corporation. Both at 250 West 34th Street, 3rd Floor, New York, NY 10119 | High |
| Backing claim | 1 token = 1 troy ounce of LBMA Good Delivery gold, allocated and serial-numbered | High |
| **Legal wrapper** | **Electronic document of title under NY UCC Articles 1, 2 and 7. Bailment. NOT a fund, NOT a security** | High |
| **SEC registration** | **None. No registration and no exemption relied upon. Zero SEC filings of any kind mention "WisdomTree Gold Token"** | High |
| **Who records ownership** | **The blockchain itself, exclusively. There is no transfer agent and no book-entry official record** | High |
| Chains | Stellar (primary) and Ethereum | High |
| Contract address(es) | **Not disclosed** by the issuer. See §8: every on-chain asset named "WTGOLD"/"WisdomTree" that we could locate is a **spoof** | High |
| Supply | ~483 tokens (~483 oz) per RWA.xyz; issuer publishes no supply figure | Low |
| Market cap / TVL | ~$2.0M–$2.5M (RWA.xyz, figures inconsistent between snapshots) | Low |
| Regulatory status | NYDFS limited purpose trust charter granted **22 March 2024** to WT TrustCo; state money transmitter licences for the app | High |
| Subscription fee | 0% | Medium |
| Ongoing custody fee | **0%** to the holder | Medium |
| Redemption fee | **Greater of (i) the price of one troy ounce of gold, or (ii) 2% of the amount surrendered**, plus taxes and shipping | High |
| Advertised yield | **None.** WisdomTree advertises no yield on WTGOLD | High |
| Named officers | Jonathan Steinberg (CEO, WisdomTree, Inc.); Will Peck (Head of Digital Assets). No WT TrustCo officer list published | Medium |
| Wind-down plan | **Not disclosed** as a plan, but a **Substitute Bailee** mechanism exists (§2) | High |

---

## 1. What it is

WTGOLD ("WT Gold") is a token on Stellar and Ethereum, each unit representing one troy ounce of LBMA Good Delivery gold held at HSBC Bank plc in London. It is sold to US retail consumers through the **WisdomTree Prime** mobile app, and is one of several "WT Digital Assets" alongside WT Dollar (a dollar token) and hosted crypto.

It launched **22 September 2022** (RWA.xyz) and remains available as of July 2026.

The framing that matters: WisdomTree is a $150bn+ AUM NYSE-listed asset manager that has built a genuinely sophisticated tokenised-fund business. WTGOLD is **not part of it**. WTGOLD sits in the separate, much smaller consumer wallet business. At roughly $2M it is a rounding error against WisdomTree's ~$770M of tokenised AUM, and a vanishing one against the parent's $150bn. This asymmetry is itself analytically important (§12).

## 2. Legal structure

**Confidence: High.** This is from the operative contract, the WisdomTree Prime User Agreement, last updated **31 March 2026** (https://dataspanapi.wisdomtree.com/pdr/documents/USER_AGREEMENT/WDM/US/EN-US/PRIME/).

The holder owns an **electronic document of title**, and the agreement says so in terms. Section 9:

> "User agrees that WT Gold and any other WT Digital Asset so designated on the Digital Assets Schedule represent an 'electronic document of title' to LBMA Gold or the other goods designated on the Digital Assets Schedule, as the case may be, for purposes of Articles 1, 2 and 7 of the New York Uniform Commercial Code as in effect from time to time (the 'UCC')."

The definition at §1(m) is equally explicit:

> "'WT Gold' means a digital token recorded on a blockchain (e.g., the Stellar blockchain or other supported blockchains) representing an electronic document of title to and ownership of one-troy ounce of physical gold meeting the good delivery requirements set by the London Bullion Market Association ('LBMA Gold')."

Note the phrase **"and ownership of."** This is stronger than most tokens in the set. The holder is asserted to own the gold, not merely to hold a claim against the issuer.

The bailment relationship is named. Section 9(j):

> "WT TrustCo acts as the bailee which issued the electronic document of title."

And critically, §9(d):

> "User is the bearer and holder of the electronic documents of title represented by the WT Digital Assets held in User's Wallet."

**This is a bearer instrument.** The gitbook gloss describes it as "a contract with, not an interest in, the bailee" (https://wisdomtree.gitbook.io/wisdomtree-gold-token), which is the classic bailment formulation: the bailee never takes title, so the goods are not the bailee's property and in principle are not available to the bailee's general creditors.

**Substitute Bailee clause.** §9(j) continues:

> "User further agrees that WT TrustCo may transfer its obligations with respect to WT Digital Assets and substitute as bailee a direct or indirect affiliate of WT TrustCo (a 'Substitute Bailee'). WT TrustCo covenants that the Substitute Bailee will be duly authorized and licensed to act as bailee for such WT Digital Assets and as the issuer of the electronic document of title represented thereby. User consents to such substitution and agrees that, upon notice thereof at the WisdomTreePrime.com website, User will look solely to the Substitute Bailee for the transfer or delivery of LBMA Gold."

So the bailee can be swapped for an affiliate, by website notice, without holder consent, and the holder's recourse then runs **solely** to the substitute. This is the nearest thing to a wind-down provision in the document (§12, question 9), and it is a continuity mechanism rather than a liquidation plan.

**Note the deliberate contrast within the same contract.** §10 is titled "Security Entitlements" and applies **Article 8** of the UCC, treating hosted **crypto** (BTC, ETH) as "financial assets" credited to a "securities account" with WisdomTree Digital as "securities intermediary." WT Gold is expressly **not** in §10: it is in §9, under **Article 7**. WisdomTree's lawyers drew an explicit line between an Article 8 intermediated security entitlement and an Article 7 bearer document of title, and put gold on the Article 7 side. That is a considered choice, not an accident.

**What a WT Digital Fund holder owns, by contrast** (relevant because this is what the brief thought WTGOLD was): a share of beneficial interest in a Delaware statutory trust series registered under the 1940 Act, recorded by a registered transfer agent. Entirely different instrument. See §12.

## 3. Regulatory and compliance posture

**Confidence: High on what exists, High on the negatives (we checked and they are absent).**

| Item | Finding |
|---|---|
| NYDFS limited purpose trust charter | **Granted 22 March 2024** to WisdomTree Digital Trust Company, LLC. Permits digital asset custody and stablecoin issuance, and allowed Prime to launch in New York. (https://www.businesswire.com/news/home/20240322928015/en/) |
| NYDFS charter number | **Not disclosed** in any source we located |
| State money transmitter licences | Asserted. User Agreement §23(j): "WisdomTree maintains certain licenses to engage in money transmission activities as set forth in the WisdomTree State License Disclosure, available at www.wisdomtreeprime.com/disclosures." **The disclosure page returned HTTP 403 to us and we could not read the licence list.** Specific state list and NMLS numbers: **Not disclosed** to us |
| SEC registration of WTGOLD | **None.** No registration statement, no exemption claimed |
| SEC exemption relied on for WTGOLD | **None claimed.** The token document states "Gold Tokens and this document have not been registered pursuant the securities or commodity laws of any country" |
| EDGAR full-text search, "WisdomTree Gold Token" | **0 hits, all form types, all dates.** Verified directly against efts.sec.gov |
| EDGAR full-text search, "Gold Digital Fund" | **0 hits** |
| CFTC registration | **Not disclosed / none found** |
| Broker-dealer | WisdomTree Securities, Inc. is an SEC-registered broker-dealer, but it is involved **only** in WT Digital Fund Share transactions (User Agreement §8), **not** in WT Gold. CRD number **not disclosed** in the product documents |

**The compliance logic is coherent and worth stating plainly.** WisdomTree did not obtain a securities exemption for WTGOLD because on its own analysis **it does not need one**: a document of title to a physical commodity is not a security. The regulatory perimeter it does occupy is the **money transmission / virtual currency** perimeter (NYDFS trust charter plus state MTLs), which is the perimeter for holding customer assets and moving value, not for issuing investment products.

This is the same "it's a commodity, not a security" position that Aurumix's ARVA route takes. **WisdomTree, with a large US legal budget and a public listing to protect, reached the same conclusion Aurumix has.** That is meaningful supporting evidence, and it is the opposite of what the brief expected to find.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian | **HSBC Bank plc** | High |
| Vault / city | **London** | High |
| Allocated? | **Yes, asserted.** "HSBC has contractually committed to maintain a continuous allocation (i.e., segregation) process whereby each gold bar associated with a Gold Token is segregated within the gold custodian's vaults with a serial number in accordance with LBMA's good delivery standards" (https://wisdomtree.gitbook.io/wisdomtree-gold-token) | Medium (issuer assertion; the HSBC agreement is not published) |
| Published bar list | **Not disclosed.** We looked and found none | High |
| PoR feed | **Not disclosed.** No Chainlink or equivalent proof-of-reserve oracle found | High |
| **Reserve attestation** | **Not disclosed.** No periodic independent attestation of the gold, no named auditor, no frequency, no report. The gitbook has a page titled "Independent Audits" but we could not retrieve any actual attestation document from it | High |
| **Smart contract audit** | **Not disclosed.** No auditor, no report | High |

**Applying the wave-1 rule (§152 of the brief) explicitly: for WTGOLD we found neither a reserve attestation nor a smart-contract audit.** The gitbook's "Independent Audits" heading is exactly the kind of language that a skimming reader converts into "audited." There is nothing behind it that we could retrieve.

**However.** The materiality of this gap is lower here than for any other protocol in the set, for a reason that does not apply elsewhere: **the parent is an SEC-reporting NYSE-listed company** whose consolidated financial statements are audited annually and whose 10-K describes the Prime business. And the custodian is HSBC, not an unnamed vault operator. The risk is not "does the gold exist"; it is "the holder has no independent, contemporaneous, per-token way to verify it," which is a transparency failure rather than a solvency signal. Distinguish those two things when this profile is read.

## 5. Issuance

Purchase is **exclusively inside the WisdomTree Prime app**, US retail, after KYC/AML ("Verification Procedures," User Agreement §1(g)). Funding is by USD from a linked external account, converted to **WT Dollars** (WisdomTree's own dollar token), which are then used to buy WT Gold. Approved third-party stablecoins can also fund the wallet (§7(b)).

The token is divisible: §9(h) allows a User to "subdivide a WT Digital Asset into smaller denominations," so retail can buy fractional ounces despite the 1-token-1-ounce definition. Minimum purchase: **Not disclosed** to us.

There is no public mint, no primary market for institutions, no authorised participant structure. Contrast this with essentially every other token in the set.

## 6. Redemption

**This is one of only two protocols in the set where we can quote the physical redemption terms verbatim from the operative contract.** User Agreement §5(h).

**Requirements**, §5(h)(i):
1. User must hold **a minimum of one (1) full ounce** of WT Gold.
2. Contact WisdomTree Digital Customer Support during business hours, 9am–9pm EST.
3. Submit a completed **WT Gold Retrieval Form** to DAOps@wisdomtree.com.
4. Identity and delivery address verified by WisdomTree Digital.
5. Accept the terms of the independent **"Metal Agent"** facilitating delivery.
6. Agree to pay all applicable fees, taxes and shipping.

Residual value below a whole ounce is returned as **WT Dollars** at the LBMA price at the time of retrieval, not as metal.

**Fees**, §5(h)(ii), quoted exactly:

> "In connection with retrieving LBMA Gold by surrendering WT Gold, User agrees to pay WisdomTree Digital a fee, as required by the Metal Agent, of the greater of: (i) the price of one-troy ounce of LBMA Gold; or (ii) 2% of the total value of WT Gold to be surrendered."

**Read that carefully, because it is severe and it is easy to misread.** The floor is not 2%. The floor is **the entire price of one ounce of gold**, roughly $2,400 or more at current prices. The 2% only becomes the binding term once the redemption exceeds **50 ounces**, because 2% of 50 oz = 1 oz.

So the effective redemption cost curve is:

| Redemption size | Fee | Effective cost |
|---|---|---|
| 1 oz (the minimum) | 1 oz | **100%** |
| 2 oz | 1 oz | 50% |
| 5 oz | 1 oz | 20% |
| 10 oz | 1 oz | 10% |
| 25 oz | 1 oz | 4% |
| **50 oz** | 1 oz | **2% (crossover)** |
| 100 oz+ | 2% | 2% |

**A retail holder redeeming the one-ounce minimum surrenders one ounce and pays one ounce, and receives nothing.** Physical redemption is nominally universal (no "qualified holder" gate, which is a genuine plus against the eligibility trap the brief flags in question 5), but it is **economically unavailable below roughly 10–25 ounces**, i.e. $24,000–$60,000. For a retail savings product, that is redemption in name only.

This is worth stating in the assembled document as a general pattern: **"universal eligibility, prohibitive economics" is a functionally equivalent substitute for "qualified holders only," and it reads better in marketing.**

Note also §5(g): tokens surrendered for exchange are **immediately cancelled** and "User will not be entitled to return of any WT Digital Assets so transferred for exchange and cancellation."

## 7. Fees and revenue model

| Fee line | Amount | Source / confidence |
|---|---|---|
| Subscription / minting | 0% | RWA.xyz. Medium |
| **Ongoing custody / storage / management** | **0% to the holder** | RWA.xyz lists 0% management, 0% performance. No storage fee found in the User Agreement. Medium |
| Buy/sell spread in-app | **Not disclosed.** No numeric spread published anywhere we looked | High (that it is undisclosed) |
| **Physical redemption** | **Greater of 1 oz of gold or 2%**, plus taxes and shipping | High (contract) |
| On-chain transfer out | Pass-through of gas plus a WisdomTree fee "designed to cover" network costs, disclosed pre-trade (§7(d)) | High |
| Fee change notice | **48 hours by email** (§6). WisdomTree may update the Digital Assets Schedule at its discretion, prospectively | High |
| Dormancy | Reserved right to "deduct an administrative fee" on unclaimed property escheatment (§23) | High |

**What funds the zero custody fee (brief question 1).** Three answers, and only the third is durable:

1. **The undisclosed buy/sell spread.** This is almost certainly the primary revenue line, and the fact that it is nowhere published is the single biggest disclosure gap in the product.
2. **Float on WT Dollars.** WT TrustCo holds the WT Dollar reserve in T-bills, reverse repo, government MMFs and bank deposits (§11(b)). Users must convert USD to WT Dollars to buy gold, so gold purchases generate dollar-token float, and at 2026 rates that float earns real money. **The gold is loss-leading for the dollar token.**
3. **Strategic subsidy from a $150bn parent.** WisdomTree can run a $2M gold product at a loss indefinitely because it is a customer-acquisition and optionality play for the tokenised-fund business, which is the actual strategy.

**Reason 3 is the one Aurumix cannot replicate, and it is the reason the zero-fee norm is a trap.** Eight protocols now show zero ongoing custody fee, but for PAXG/XAUT it is funded by billions in float, and for WisdomTree it is funded by a listed parent's strategic budget. Aurumix has neither. Recording "the norm is zero" without recording "and here is the balance sheet that pays for it" would be the wrong lesson.

**No dilutive or in-kind fee mechanism.** Unlike PAXG (brief §144), WisdomTree reserves **no** right to take fees by minting tokens to itself. Nothing analogous found.

## 8. Token architecture

- **Chains:** Stellar (primary) and Ethereum. Stellar is the native issuance chain.
- **Standard:** Stellar native asset (not ERC-20 on the primary chain). Stellar assets carry issuer-level **authorization flags**, which give the issuer permissioning and clawback capability at the protocol level without a custom token standard. This is the functional equivalent of ERC-3643 permissioning, obtained for free from the ledger design.
- **Permissioned:** **Yes, effectively.** User Agreement §7(a) and §8(e) restrict on-chain transfers to wallets "registered with WisdomTree," and §7(e) reserves the right to "suspend, cancel, reject or delay any Onchain Transfer." A holder cannot freely send WTGOLD to an arbitrary address.
- **Upgradeability / admin keys:** **Not disclosed.**
- **Bridge:** Stellar↔Ethereum mechanism **Not disclosed.**

**🔴 Contract addresses: not disclosed by the issuer, and the on-chain namespace is populated by impostors.**

We attempted direct on-chain verification. WisdomTree publishes **no** contract or issuer address in its token document, gitbook, or User Agreement, and serves **no** `stellar.toml` at wisdomtreeprime.com, wisdomtree.com or www.wisdomtree.com (all 404). Absent a `stellar.toml`, there is **no cryptographic way for a holder to verify which Stellar issuer account is genuinely WisdomTree's.**

What is in that vacuum, verified by us against Horizon and stellar.expert on 28 July 2026:

- Two Stellar assets with code `WTGOLD` exist. The larger, issuer `GBSCY7XCPOJEUGRQU77SIXYNXCOUKF33EZ7L27W2XXZXSS6N667N7E37`, has **home_domain `wisdomtree.xlmhq.org`** (not a WisdomTree domain), supply 1,511,450,381 units, **4 trustlines and 4 payments**, and **all authorization flags set to false** (no `auth_required`, no `auth_revocable`, no clawback). A genuine regulated bailee issuing a permissioned document of title would not leave those flags off.
- A broader search for "wisdomtree" on Stellar returns a **cluster of spoofed assets** on domains including `wisdomtree.com.co`, `wisdomtree.bond`, `cadence.wisdomtree-stellar.com`, `micron.wisdomtree-stellar.com`, `globaltoken-stellar.com` and `stocks.kraken.com.bz`, impersonating real WisdomTree ETF tickers (DXJ, DFJ, WTMF, AIVL, NTSE, QSIG) with absurd supplies (1.8 quadrillion units).
- Also worth flagging: **the Stellar issuer address supplied to us by Perplexity, `GBKKR9J5DOEBVHO4CEB5NQRUGNMLFJOPBY57DDYZLQZKSSJTZ3OI4SYZ`, does not exist on Stellar mainnet.** Horizon returns no account. It was fabricated with a confident inline citation. This is a live example of why the brief's citation rule exists, and it should be treated as a caution for the whole research pass: **on-chain claims must be verified on-chain, not accepted from a language model.**

**Conclusion for §8: we could not identify a genuine WTGOLD contract address from any source, and everything findable on-chain under that name appears fraudulent.** For a bearer document of title whose entire legal theory rests on §9(e) of the User Agreement, that the blockchain "will be the exclusive means of delivering and determining who has control," this is a serious gap: the issuer has made the ledger legally dispositive while publishing nothing that lets a holder identify the correct ledger entry.

## 9. Liquidity and market

Per the wave-1 addendum, one paragraph, no re-argument.

WTGOLD has **AUM of roughly $2.0M–$2.5M** (RWA.xyz reports ~483 tokens and a total asset value of ~$1.97M in one snapshot and a NAV of ~$2.52M in another; the inconsistency is unresolved and the issuer publishes nothing), across **~660 holder addresses**. **On-chain liquidity and daily volume are effectively zero, and not because the market is thin but because there is no market at all:** WTGOLD has no DEX pool, no CEX listing, and no secondary venue. It is buyable and sellable **only inside the WisdomTree Prime app, against WisdomTree as principal, at a spread WisdomTree does not publish.** Price is therefore administered, not discovered, and the question of a premium to spot does not arise: there is no independent market to express one. WTGOLD is the **limiting case** of the settled wave-1 conclusion. Where PGOLD showed an illiquid market with no premium, WTGOLD shows that a fully closed-loop distribution model removes the premium question entirely, at the cost of removing price discovery too.

## 10. Distribution

- **Channel:** single, proprietary, closed. The WisdomTree Prime mobile app (iOS/Android). No exchange listings, no broker distribution, no B2B API for gold.
- **Segment:** US retail consumers.
- **Geography:** US only. State availability is gated by money transmitter licensing; the specific included/excluded state list is **Not disclosed** to us (the disclosures page 403'd). Non-US eligibility: **Not disclosed**.
- **Savings plan / recurring purchase / SIP:** **Not disclosed / none found.** No monthly contribution feature documented for WTGOLD.
- **Referral / affiliate / agent network / commission tiers:** **None found.** As a US-regulated entity, a multi-tier commission structure of the kind Aurumix plans would raise broker-dealer registration questions that WisdomTree has clearly avoided.
- **Distinctive feature:** the **"gold you can spend"** thesis. WisdomTree's own token document is subtitled "DRIVING TOWARD GOLD YOU CAN SPEND," and coverage of the NYDFS charter referenced a Visa card letting customers "pay for coffee with digital gold tokens." WTGOLD's differentiation is payments utility, not yield and not savings discipline.

**Answer to brief question 8: WTGOLD has no savings-plan, recurring-purchase, referral or affiliate mechanism whatsoever.** It is another data point for the finding that this is Aurumix's genuinely uncontested ground.

## 11. Recent developments

Dated, reverse chronological. Sweep run 28 July 2026.

- **24 July 2026** — WisdomTree Digital Trust files Form 485BXT (new effective date for a post-effective amendment), the most recent of a continuous 2026 stream of fund registration activity. The **fund** business is in active expansion. (EDGAR CIK 0001859001)
- **~Q2 2026** — WisdomTree reports **tokenised AUM of ~$770M**, described as a 25-fold increase since 2024, with the digital asset business characterised as a core business nearing profitability. (https://finance.yahoo.com/news/wisdomtree-firm-150-billion-assets-234020262.html)
- **23 February 2026** — **SEC grants exemptive relief**, Investment Company Act Release No. **35968**, File No. **812-15788**, to WisdomTree Digital Trust, WisdomTree Securities Inc., WisdomTree Digital Management Inc. and **WisdomTree Transfers, Inc.** Order under **sections 6(c) and 17(d)** and rule 17d-1, exempting from **section 22(d) and rule 22c-1** to permit affiliated dealers to transact **WisdomTree Government Money Market Digital Fund** shares on a **principal basis at a stable $1.00 per share** rather than next-calculated NAV. Application filed 8 May 2025, amended 16 January 2026. (https://www.sec.gov/files/rules/ic/2026/ic-35968.pdf) **This is the single most important regulatory event in WisdomTree's tokenised business and it concerns funds, not gold.**
- **28 January 2026** — Notice of the above application published in the Federal Register. (https://www.federalregister.gov/documents/2026/01/28/2026-01691/)
- **26 January 2026** — SEC issues notice of filing, Investment Company Act Release No. 35912.
- **3 February 2026** — Jonathan Steinberg states at the Ondo Summit that the digital asset business is "in line of sight" of profitability, that WTGXX launched in 2023, and that WisdomTree now has **14 tokenized funds**. (https://www.marketsmedia.com/wisdomtree-digital-asset-business-near-profitability/)
- **December 2025** — Launch of the **WisdomTree Equity Premium Income Digital Fund**, distributed to retail via Prime and to institutions via Connect.
- **3 June 2025** — WisdomTree wins "Best Digital Asset Processing Solution" for its blockchain-enabled transfer agent. The award citation notes **WisdomTree Transfers maintains transfer agent functions across WisdomTree Prime and WisdomTree Connect with over $241 million of tokenized AUM**, with records "held in both traditional book-entry form and digitized on the Ethereum, Arbitrum, Avalanche, Base and Optimism blockchains." (https://ir.wisdomtree.com/news-events/press-releases/detail/737/)
- **31 March 2026** — WisdomTree Prime User Agreement last updated (the version quoted throughout this profile).
- **22 March 2024** — **NYDFS grants WisdomTree Digital Trust Company, LLC a New York limited purpose trust company charter**, enabling digital asset custody, the WisdomTree Dollar Token, and the launch of Prime in New York. (https://www.businesswire.com/news/home/20240322928015/en/)
- **22 September 2022** — WTGOLD inception (RWA.xyz).

**Status check.** WTGOLD is **not** discontinued and remains purchasable as of July 2026; the Prime app still markets "Digital Gold." But note the shape of this timeline: **every dated development since 2024 concerns the funds, the transfer agent, the stablecoin or the platform. There is not one WTGOLD-specific announcement in 18 months.** No new chains, no new features, no attestation, no partnership, no AUM milestone. Against a fund business that went 25x, the gold token is static at ~$2M. This looks like a **maintained legacy product, not an invested one** and it is the early-stage signature of exactly the **PMGT commercial-abandonment pattern** the brief tells us to test for (zero holder revenue means no internal advocate). WisdomTree differs from Perth Mint in that it has an unrelated strategic reason to keep the product alive (payments optionality, brand), but the revenue logic is the same.

**No enforcement actions, incidents, outages or breaches** concerning WisdomTree's digital asset business were found in the sweep window. That is a clean record and, in this set, unusual.

## 12. Relevance to Aurumix

**This is the section the assignment turns on, and the answer inverts the question.**

### 12.1 The premise correction, and why it still matters

The brief asked us to assess "a regulated fund wrapper with tokenised share records" as a third path against the ARVA-commodity-token route, on the belief that WTGOLD is one. **WTGOLD is not a fund and has no transfer agent.** But the model is real, WisdomTree operates it, and it is worth assessing properly, because the *fact that WisdomTree did not use it for gold* is more informative than a hypothetical assessment would have been.

**The two structures, side by side:**

| | **WT Gold (WTGOLD)** | **WT Digital Funds (WTGXX et al.)** |
|---|---|---|
| Legal wrapper | Electronic document of title, NY UCC Art. 1/2/7 | Series of a Delaware statutory trust, shares of beneficial interest |
| Is it a security? | **No** (issuer's position) | **Yes**, expressly |
| SEC registration | **None** | **1940 Act File No. 811-23659; 1933 Act File No. 333-255575** |
| Who records ownership | **The blockchain, exclusively** | **WisdomTree Transfers, Inc.**, SEC-registered transfer agent |
| Authoritative record | The ledger (User Agreement §9(e)) | **The book-entry record.** Blockchain is secondary |
| Underlying asset | Physical gold at HSBC | Securities |
| Investor protections | Contract and bailment law | 1940 Act: board oversight, custody rules, daily NAV, prospectus |
| Ongoing fee | 0% | **0.44%** management fee (Equity Premium Income Digital Fund) |
| Distribution | Proprietary app only | Prime (retail) + Connect (institutional) + broker-dealer |
| Exemptive relief | None | **6(c), 17(d), rule 17d-1** (Release 35968) |

### 12.2 The record-authority clause, and what it costs

The brief asked what it means that ownership is recorded on the transfer agent's books with the blockchain as a secondary record. On the fund side, this is answered verbatim in the WisdomTree Digital Trust prospectus (filed 13 November 2025, https://www.sec.gov/Archives/edgar/data/1859001/000121465925016424/wtd111225485bpos.htm):

> "WisdomTree Transfers, Inc., the Fund's transfer agent ('WisdomTree Transfers' or 'Transfer Agent'), maintains the official record of share ownership through an integrated recordkeeping system with records in book-entry form and digital representations of Fund shares that are recorded – or tokenized – on the applicable blockchain. A transfer of the record on the blockchain can act as an information source for the Transfer Agent to register a transaction in its book-entry records. The Transfer Agent will reconcile book-entry and blockchain transactions on at least a daily basis... **The Transfer Agent's book-entry records constitute the official record of share ownership.**"

The User Agreement §8(b) says the same to consumers, defining the book-entry record as the "**Official Record**."

**Read the direction of authority.** The blockchain "can act as an **information source**" for the transfer agent. The transfer agent's book **is** the record. **The token is a mirror, not the asset.** If the two disagree, the book wins and the token is corrected.

**This solves the securities-classification problem completely, and the price is the entire premise of a token.** You get a fully regulated, unambiguously legal instrument, and in exchange:

- The token cannot be a bearer instrument. Possession of the token is not ownership.
- Transfers must be to wallets known to the transfer agent, which must reconcile them into the book. Permissionless transfer is impossible **by legal design**, not by technical choice.
- Every holder must be a KYC'd shareholder of record.
- You inherit the full 1940 Act cost base: board, independent trustees, daily NAV, prospectus, annual audit, CCO, exemptive applications taking (in WisdomTree's case) **9.5 months from filing to order**.

**And decisively for Aurumix: the 1940 Act path is not available for a gold product at all.** A vehicle holding physical gold is not an investment company under the 1940 Act (gold is not a security), which is precisely why US physical gold ETFs such as GLD are **1933 Act grantor trusts** with no 1940 Act registration and no 1940 Act protections. So "become a registered fund" is not a route Aurumix could take for a gold-backed savings product even if it wanted the cost base.

**This is why WisdomTree, which owns a registered transfer agent, a broker-dealer, a fund adviser and a registered trust, still structured its gold product as a UCC Article 7 document of title.** Not oversight. The fund wrapper does not fit gold. **The "third path" the brief hoped for does not exist for this asset class**, and a firm with every possible incentive and capability to find it did not.

### 12.3 The finding that actually helps: WisdomTree independently validates the commodity-token route

Strip away the wrapper confusion and this is what is left, and it is genuinely useful:

**A NYSE-listed, SEC-reporting, NYDFS-chartered US asset manager with $150bn AUM, in the most litigious securities jurisdiction on earth, structured its retail gold token as a non-security document of title to a physical commodity, and did not register it with the SEC or claim any exemption.**

That is the strongest available third-party validation of Aurumix's core thesis that **a pure gold-backed token is not a security**. It is worth more than any of the offshore precedents in the set, because WisdomTree has a public share price, an audit committee and a legal budget that make an aggressive position unaffordable.

**But note precisely what is validated: the bare gold core, and nothing else.** WisdomTree's product pays **no yield**, has **no dividend**, offers **no credit facility**, has **no tiered allocation system** and **no agent network**. It is the clean case. Every feature Aurumix layers on top (ICS, ICS Dividend, Gold Card, credit at 90–95% LTV) is a feature WisdomTree does **not** have, and the difference is not capability. WisdomTree could build any of it in a quarter. **It chose the clean commodity perimeter and stayed inside it.**

That is the shape of the warning. WisdomTree's structure is evidence **for** the ARVA gold core and evidence **against** the hybrid. It tells Aurumix that the base layer is defensible and that the superstructure is where the classification risk actually lives, which is what the brief already suspected (question 4) and now has a serious precedent for.

### 12.4 The instrument-split question (wave-1 live lead)

The brief flags Kinesis's split (clean asset token + separately capped security, KVT) as the leading structural answer to hybrid regulation, and asks whether other protocols separate a yield or governance instrument from the asset token.

**WisdomTree does separate its instruments, and more cleanly than Kinesis, but it is not the same manoeuvre.** WisdomTree runs the **non-security gold document of title** and the **registered fund shares** as entirely distinct instruments with distinct legal wrappers, distinct regulators, distinct record-keeping systems and distinct distribution rails, side by side in one app. A user can hold both in one wallet, and the wrapper never blends.

The lesson for Aurumix is architectural rather than legal: **the app can be unified while the instruments stay legally severed.** A single retail experience does not require a single legal object. If Aurumix wants a savings core plus a yield instrument, the WisdomTree pattern says put them in different legal wrappers under different licences and unify them only in the UX layer. Kinesis says the same thing from a different starting point. **Two independent protocols now converge on instrument separation, which materially strengthens it as our recommended answer.**

### 12.5 Direct answers to the nine design questions

1. **Custody fee.** 0% to the holder. Funded by an **undisclosed in-app spread**, by float on the WT Dollar reserve (T-bills, repo, MMFs, deposits), and ultimately by strategic subsidy from a $150bn listed parent. **No dilutive or in-kind fee mechanism**, and no reserved right to introduce one. Aurumix cannot copy the funding model; the fee level is only meaningful alongside the balance sheet behind it.
2. **Dividend funding.** **WTGOLD pays no yield of any kind.** WisdomTree, holding allocated gold at HSBC and possessing every capability to run a lending programme, **does not lease the gold and pays holders nothing.** For the client's dividend problem this is a negative data point of real weight: the most conservatively regulated issuer in the set looked at yield on gold and declined. No contradiction to the Streamex lead (§141), but no support for it either.
3. **Token standard.** Stellar native asset with issuer-level authorization flags, plus Ethereum. **Permissioned by contract** (transfers only to WisdomTree-registered wallets, §7(a)/§8(e), with a reserved right to block). Relevant to Aurumix's ERC-3643 lean: WisdomTree gets equivalent permissioning from Stellar's built-in flags rather than a specialised standard, which is cheaper. But note the cost it accepted: **zero external liquidity**, because a permissioned token with no venue is a closed loop. That is the honest price of the ERC-3643 route and Aurumix should price it in.
4. **Regulatory route.** **NYDFS limited purpose trust charter, granted 22 March 2024**, plus state money transmitter licences. **Not a securities licence.** The perimeter is custody and value transfer, not investment products. The structural read-across is that a **trust-company charter, not a securities licence, is the natural home for a gold custody token** and the same logic supports the VARA/ARVA framing for the Aurumix core.
5. **Redemption.** Physical redemption exists, is **not** gated to "qualified holders" (good), 1 oz minimum, but costs **the greater of 1 oz or 2%**, which is **100% of value at the minimum** and only reaches 2% above 50 oz. **Universal eligibility with prohibitive economics.** Aurumix's honest "no physical redemption" is arguably a better disclosure posture than a redemption right that cannot rationally be exercised by the customers it is offered to, and this comparison is worth making explicitly in client materials.
6. **Premium and liquidity.** ~$2.0–2.5M AUM, ~660 holders, **no secondary market at all**. Settled question; one more data point at the extreme end.
7. **Proof of reserve.** **No bar list, no PoR feed, no reserve attestation, and no smart-contract audit found.** Both halves of the wave-1 distinction fail here. Mitigated, though not cured, by HSBC as custodian and an SEC-reporting audited parent.
8. **Distribution.** **No savings plan, no recurring purchase, no referral, no affiliate, no agent network.** Single proprietary app. Aurumix's SIP-plus-agent-network model remains unmatched across the entire set.
9. **Wind-down.** No published wind-down plan. But the **Substitute Bailee clause (§9(j))** is the closest thing any protocol in the set has to a documented continuity mechanism: the bailee's obligations transfer to a licensed affiliate on website notice, and holders then look solely to the substitute. Worth borrowing the *idea* (name a successor mechanism ex ante) while noting the defect (affiliate-only, no consent, no external trustee, no independent insolvency protection).

### 12.6 What to take from this profile

- **Use WTGOLD as the flagship precedent for the non-security gold core.** A NYSE-listed, NYDFS-chartered US manager reached the same classification conclusion Aurumix has. That is the best validation available anywhere in this landscape.
- **Do not present it as a fund-wrapper alternative.** It is not one, and the fund wrapper is legally unavailable for physical gold. Retire that hypothesis.
- **Take the instrument-separation lesson.** WisdomTree and Kinesis independently converge on it. Unify the app, sever the wrappers.
- **Read the redemption maths as a warning about disclosure integrity**, not as a feature to copy.
- **Note the abandonment signature.** A zero-revenue gold product inside a fast-growing fund business has received no development in 18 months. Aurumix's gold core must generate revenue for someone internally, or it becomes PMGT.

## 13. Open items for verification

- [ ] Obtain the **WisdomTree State License Disclosure** at https://www.wisdomtreeprime.com/disclosures (returned HTTP 403 to us): full state money transmitter list, NMLS IDs, and the states where WTGOLD is unavailable.
- [ ] Obtain the **NYDFS charter number** for WisdomTree Digital Trust Company, LLC from the NYDFS licensed-entity register, and confirm the charter is current as of 2026.
- [ ] Obtain the **WisdomTree Digital Assets Schedule** (referenced throughout the User Agreement as the operative fee document, never published alongside it). It should contain the **buy/sell spread**, the minimum purchase, and the definitive fee table. **Highest-value missing document.**
- [ ] Identify the **genuine Stellar issuer account and Ethereum contract address** for WTGOLD via the Prime app or WisdomTree investor relations. Confirm authorization flags. **Report the spoofed asset cluster (`wisdomtree.com.co`, `wisdomtree.bond`, `wisdomtree.xlmhq.org`, `stocks.kraken.com.bz`) to WisdomTree** as a brand-protection matter; it is also a live consumer-harm risk.
- [ ] Confirm whether WisdomTree publishes **any** independent attestation of the HSBC gold, or whether the gitbook "Independent Audits" page has substance behind the heading.
- [ ] Obtain the **HSBC custody agreement** or its material terms: is allocation contractual only, or is there a segregated account title? Is there insurance, and who is loss payee?
- [ ] Identify the **"Metal Agent"** named in User Agreement §5(h). The redemption fee is stated to be set by this third party, not by WisdomTree.
- [ ] Resolve the **AUM discrepancy** in RWA.xyz snapshots (~$1.97M total asset value vs ~$2.52M NAV vs 483.28 tokens at $2,400). Obtain an issuer-published supply figure if one exists.
- [ ] Check WisdomTree, Inc.'s most recent **10-K and 10-Q** for segment disclosure on Prime: revenue, and whether WT Gold is separately identified or has been quietly deprecated.
- [ ] Confirm whether **WisdomTree Digital Movement, Inc. holds a NYDFS BitLicense** in addition to the WT TrustCo trust charter, or whether it operates solely under the charter plus state MTLs.
- [ ] Determine whether the **issuer role migrated** from WisdomTree Digital Holdings, Inc. to WisdomTree Digital Movement, Inc. as the gitbook says was planned, and reconcile against the User Agreement which names **WT TrustCo** as bailee. **Three different WisdomTree entities have been described as the WTGOLD issuer across sources; establish which one is contractually liable today.**
