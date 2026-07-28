# Digix Gold Token (DGX) and DigixDAO (DGD)

**Status: WOUND DOWN.** The DAO was dissolved by token-holder vote in January 2020. The company stopped taking new business in September 2022 and ceased operations on 21 March 2023. Every Digix entity on the Singapore register is now struck off, the last on **19 July 2026, nine days before this profile was written.** The DGX contract still runs on Ethereum and 15,400 tokens still exist, but there is no reachable issuer, no reachable redemption agent, and no live website.

This is a failure profile, and it is the most important one in the set for two reasons. First, it is the **only live example of the demurrage mechanism the client has already ruled out**, so §7 documents it at contract level. Second, it repeats the PMGT pattern precisely: **Digix switched its own revenue off before it died.**

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Tickers | DGX (gold token), DGD (DAO / governance token) | **High** |
| Issuer (marketing) | "Digix" / "DigixGlobal", Singapore | **High** |
| Issuer (registry) | A **group of separate Singapore entities, all now struck off**. Gold title sat in **DIGIX PHYSICALS PTE. LTD., UEN 201724269N** (inc. 25 Aug 2017, SSIC 52101 General Warehousing, stated activity "HOLD PHYSICAL ASSETS"). Parent **DIGIX HOLDINGS PRIVATE LIMITED, UEN 201724450M** (inc. 28 Aug 2017), **struck off 19 July 2026** ([RecordOwl](https://recordowl.com/company/digix-holdings-private-limited), [OpenGov SG](https://opengovsg.com/corporate/201724450M), [OpenCorpData](https://opencorpdata.com/sg/201724269N)) | **High** |
| Other group entities | **DIGIX MARKETS PTE. LTD.** UEN 201906348R (inc. 27 Feb 2019, "Fund management activities n.e.c."), **DIGIX TECHNOLOGIES PRIVATE LIMITED** UEN 201713056E (inc. 11 May 2017), **DIGIX CORE** UEN 53369203B (ceased registration). All struck off or ceased | **High** |
| Domicile | Singapore. All entities shared one address: 6 Eu Tong Sen Street, #06-09, The Central, Singapore 059817 | **High** |
| Backing claim | 1 DGX = 1 gram of 99.99% LBMA-standard gold cast bar, divisible to 0.001g | **High** |
| Chains | Ethereum only | **High** |
| Contract address | DGX: `0x4f3AfEC4E5a3F2A6a1A411DEF7D7dFe50eE057bF`. DGD refund ("Acid"): `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f` | **High** |
| Supply | DGX: **15,400** tokens (~15.4 kg gold nominal), ~2,103 holders. Peak was 122,700 DGX (Jan 2020). DGD: 1,999,999 total | **High** |
| Market cap / volume | DGX: ~$278k on-chain, **24h volume nil**. DGD: ~$0.067, 24h volume **$0** | **Medium** |
| Regulatory status | **No licence held.** Digix Holdings **withdrew its Payment Services Act licensing in September 2022**. See §3 | **Medium** |
| Subscription fee | Minting free to the depositor; Digix earned its margin on gold purchase | **Medium** |
| Ongoing custody fee | **0.60% per annum demurrage, deducted in gold from token balances.** **Switched off (set to zero) in 2019 and never switched back on.** See §7 | **High** |
| Transfer fee | **0.13% of every transfer**, deducted in gold. This is the "0.13%" figure, not the demurrage rate. See the correction below | **High** |
| Redemption fee | **1% recast fee**, in gold, on 100g / 1kg bar redemption in Singapore | **High** |
| Advertised yield | DGX: none. DGD: a share of DGX fee revenue, paid quarterly to stakers who voted | **High** |
| Named officers | Kai C. Chng (co-founder, CEO), Anthony Eufemio (co-founder, CTO), Shaun Djie (co-founder) | **Medium** |

---

## ⚠ Three corrections to the brief, one of them material

**1. The "0.13% demurrage" premise in the task is wrong, and the error matters mechanically.** The task states Digix "charged a demurrage fee deducted in gold (reportedly 0.13% per year)." Those are two different fees conflated:

- **Demurrage: 0.60% per annum**, accrued daily against the holder's balance.
- **Transfer fee: 0.13% per transfer**, an event-driven charge, not annual.

Both were denominated in gold, so the client's concern is right, but the annual drag was **4.6x larger** than assumed and there was a second, separate gold-denominated charge on top of it. **Confidence: High** ([Digix FAQ](https://medium.com/@Digix/digix-faq-deaf53fcc1e8), [fee calculation gist](https://gist.github.com/mrenoon/2582fba7b4d457d80f7d37520aabbc08)).

**2. The brief's causal framing is half right and half wrong, in the same way PMGT's was.** The brief says "Digix dissolved its DAO via a structured treasury return while DGX went illiquid." Both halves are factually true. But the framing implies the DAO dissolution was Digix's chosen wind-down mechanism. It was not. **Digix the company opposed the dissolution and abstained from the vote.** It was done *to* the company by its token holders, over management's objection, and it removed the funding base that had subsidised DGX. See §11 and §12.

**3. The wind-down is more complete than "went illiquid" suggests.** DGX did not merely go quiet. The issuer withdrew from regulation, ceased business, handed redemption to an offshore party that is now unreachable, and **every Singapore entity has been struck off the register**, the parent as recently as **19 July 2026**. There is no counterparty left to sue.

---

## 1. What it is

Digix was founded in Singapore in December 2014 and is the **oldest serious tokenized gold project**: DGX predates PAXG by roughly four years and XAUT by five. It ran the first significant Ethereum ICO in March 2016, selling DGD for **466,648 ETH** (~$5.5M at the time).

The architecture had two tokens doing two jobs, which is precisely the "instrument split" the brief flags as a live lead:

- **DGX**: the asset token. 1 DGX = 1 gram of gold. No governance rights, no yield.
- **DGD**: the governance and revenue-share token. 2,000,000 fixed supply. Holders who staked and voted received a share of DGX fee revenue.

Gold was tracked through the **Proof of Provenance (PoP)** protocol, an on-chain asset and supply-chain record using Ethereum plus IPFS, tracking bars from vendor to vault. Gold was sourced through **ValueMax** (a listed Singapore pawnbroker) and stored with **The Safe House** in Singapore, later with an additional Canadian vault ([FintechNews Singapore](https://fintechnews.sg/835/blockchain/digix-digital-tokens-representing-legal-ownership-assets/)).

For the client, the important observation is that **Digix built almost exactly the structure Aurumix is considering**: a clean gold token, a separate instrument carrying governance and revenue rights, real vaulted metal, on-chain provenance, and genuine physical redemption. It was better-engineered than most of its successors. It still failed. Understanding why is the whole value of this profile.

## 2. Legal structure

What a DGX holder actually owned:

The registry gives the answer more precisely than the marketing did. **DIGIX PHYSICALS PTE. LTD. (UEN 201724269N)** was incorporated under SSIC **52101, "General Warehousing"**, with its stated principal activity recorded as **"HOLD PHYSICAL ASSETS"** ([OpenCorpData](https://opencorpdata.com/sg/201724269N)). That is a warehousing company, not a trustee and not a regulated custodian.

Third-party analysis of DGX's structure describes the position bluntly: Digix Physicals **maintained title to the gold bullion in the vault**, meaning the company legally owned the vaulted gold, and the holder's relationship with Digix was analogous to a relationship with a bank. Title transferred to the holder only on physical collection.

**So a DGX holder held an unsecured contractual claim against a Singapore warehousing company, not beneficial title to gold.** There is **no trust deed, no bare trust, and no independent trustee** anywhere in the Digix structure that we could locate. **Confidence: Medium** on the title analysis (secondary source, no primary custody agreement published); **Confidence: High** on the registry facts.

Compare PMGT, which for all its faults had a real bare trust with a separate custodian entity and an explicit no-commingling covenant. Digix, the older and more celebrated project, had **weaker holder protection than the product we already classified as a failure**.

**Why this matters now.** Digix Physicals is struck off. When a Singapore company is struck off, its remaining property vests in the state as *bona vacantia*. If gold was still held in that company's name at strike-off, the holder's counterparty no longer exists and the claim runs against an entity that has been dissolved. **Confidence: Medium** on the legal consequence (general Singapore company law; we found no filing describing the actual disposition of the gold).

## 3. Regulatory and compliance posture

| What we checked | Result |
|---|---|
| MAS Payment Services Act licence | **Withdrawn by the company.** Digix Holdings announced withdrawal of its PSA licensing in **September 2022** ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)) |
| Licence or exemption class, MAS reference number | **Not disclosed.** We could not establish whether Digix held a full licence, an exemption, or only a transitional exemption pending application |
| Any MAS enforcement action against Digix | **None found**, 2014 to July 2026 |
| Any regulator action anywhere | **None found** |
| Current entity status | **All struck off.** Parent struck off 19 July 2026 |
| Securities characterisation of DGD | Never tested by a regulator |

**The regulatory finding is the absence of a regulatory finding.** No regulator shut Digix down. No enforcement action was ever brought. The PSA withdrawal was **voluntary and self-initiated**, and it came *with* the announcement that the company was ceasing all business activities, not before it. The licence did not kill the business; the business gave up the licence on the way out.

This is directly analogous to the wave-1 PMGT correction. **A project can look like it was regulated out of existence when in fact it walked away.** For Digix, the PSA regime arriving in 2020 raised the cost of staying compliant for a business that, by then, had no revenue to pay for compliance. That is a cost-of-compliance-versus-revenue problem, not an enforcement problem.

## 4. Custody and proof of reserve

| Element | Digix |
|---|---|
| Custodian | **The Safe House**, Singapore (ISO 9001 certified vault). A Canadian vault added in 2019 |
| Vault / city | Singapore (primary), Canada (secondary) |
| Gold supplier | **ValueMax**, a listed Singapore pawnbroker |
| Allocated? | Yes in substance: specific 100g and 1kg cast bars, individually identified |
| Published bar list | **Yes, and this was genuinely strong.** Each bar's documentation was recorded on-chain and on IPFS via the Proof of Provenance protocol, with bar serial numbers, assay certificates and vault receipts |
| PoR feed | **Yes**, via PoP. Arguably the first real on-chain proof-of-reserve in tokenized gold |
| Reserve attestation by named audit firm | **Not found.** No periodic third-party reserve attestation by a named accounting firm was identified. PoP was an issuer-operated provenance record, not an independent attestation |
| Smart contract audit | **Yes, and unusually credible.** Audited by **Yaron Velner and Loi Luu**, 21 May to 18 June 2017 ([audit report](https://gist.github.com/loiluu/0363070e1bada977f6192c8e78348438)) |

**The audit/attestation distinction, one more time.** Digix was *smart-contract* audited by serious cryptographers. It was **not** reserve-attested by an accounting firm. Digix's PoP protocol was a much better provenance system than most competitors have today, but it was still the issuer telling you about its own gold, cryptographically. When the issuer's servers and IPFS pinning went away, so did the verification.

**And the audit found real problems.** The 2017 report identified a **critical bug allowing self-transfers to increase balances**, plus a finding that **the demurrage fee calculation incentivised strategic dummy operations**: the fee logic could be gamed by timing transactions. Both flaws were *in the fee mechanism itself*. This is worth noting for the client: the demurrage design was not just economically awkward, it was **hard to implement correctly**, and competent auditors found exploitable defects in it.

## 5. Issuance

Gold was purchased and vaulted, PoP recorded the bar, and DGX was minted against it. Minting for the depositor was free; Digix's margin came from the spread on gold sales through its marketplace. Retail users bought DGX with ETH or fiat via the Digix marketplace or exchanges.

Issuance was **not open-access minting**: creation was controlled by Digix. Supply peaked at ~122,700 DGX (~122.7 kg, ~$6.0M) in January 2020 and stands at **15,400 today**. That peak is the real story: **after five years of operation, the oldest tokenized gold project in the world had accumulated about $6 million of gold.** For scale, PAXG holds ~$1.79bn and XAUT ~$2.46bn.

## 6. Redemption

Digix's redemption ("recast") was **genuinely functional**, which makes its disappearance more instructive.

| Term | Detail |
|---|---|
| Minimum | **100 DGX** (100g bar) or **1,000 DGX** (1kg bar) |
| Fee | **1% recast fee, in gold.** A 100g redemption required **at least 101 DGX** in the wallet |
| Denominations | 100g and 1kg cast bars only |
| Collection | **In person, at the vault, in Singapore** (later also Canada) |
| Window | Physical presence required within **30 days**; uncollected bars were **automatically re-minted into DGX** |
| KYC | Valid government ID plus current proof of address, presented in person at collection |
| Eligibility | Open, subject to the above. No "qualified holder" gate |

Two design points worth stealing and one worth avoiding. Worth stealing: the **automatic re-mint of uncollected bars**, an elegant solution to abandoned redemptions that never leaves the peg unbacked. Worth avoiding: **redemption required physical presence in Singapore**, making it inaccessible in practice to almost the entire holder base. A redemption right you must fly to Singapore to exercise is a marketing feature, not a liquidity feature.

### Can a DGX holder redeem today?

**Tested concretely. The answer is effectively no.**

- On **21 March 2023**, Digix ceased operations and handed redemption facilities to **NexusGold FZC**, described as an overseas partner, with licence number **4306536.01** ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)).
- The redemption portal at **nexusone-dgx.com** is **unreachable** (connection refused on both HTTPS and HTTP, tested 28 July 2026).
- **digix.global** is **unreachable** (connection refused, tested 28 July 2026).
- The Digix Zendesk support portal returns **403 Forbidden**.
- We could **not verify NexusGold FZC in any UAE free-zone register.** "FZC" indicates a UAE free-zone company (commonly Sharjah/Hamriyah), but searches against that licence number returned nothing. **Its jurisdiction, its registration status, and whether it still exists are all: Not found.**
- A dedicated recency sweep covering February 2025 to July 2026 found **zero** announcements, redemption notices, filings or partnership news for Digix, DGX, DGD or NexusGold FZC.
- Every Digix Singapore entity is **struck off**.

**Assessment: there is no live redemption path.** The gold-title company is dissolved, the redemption agent is unreachable and unverifiable, and no live channel exists through which a holder could initiate a claim. **Confidence: High** that no functioning public redemption path exists as of 28 July 2026. **Confidence: Medium** that redemption is permanently impossible: we found **no formal notice terminating redemption**, which is itself the finding. Holders were never told it ended. It simply stopped answering.

### What happened to the physical gold

**Not disclosed, and this is a serious finding.** There is no public record of what became of the metal:

- No final audit, reconciliation or PoP report covering the closure period.
- No ACRA or MAS filing describing disposition of the gold reserves.
- No statement on whether gold was liquidated, transferred to NexusGold FZC, or remains at The Safe House under different ownership.

**15,400 DGX remain outstanding, nominally representing ~15.4 kg of gold (roughly $1.5M at July 2026 prices), with no public account of where that metal is.** The bar list that PoP once published is gone with the infrastructure that served it. This is the single most damning fact in the profile, and it is the one to put in front of the client when discussing wind-down commitments.

## 7. Fees and revenue model

**This section is the one the client asked for. Read it as the specification of the mechanism Aurumix has ruled out.**

### The fee lines

| Fee line | Rate | Denominated in | Who received it |
|---|---|---|---|
| **Demurrage (storage)** | **0.60% per annum**, accrued daily | **Gold, deducted from token balance** | 0.40% to DigixGlobal, **0.20% to DigixDAO** |
| **Transfer fee** | **0.13% per transfer** (originally capped at 1 gram, cap later removed) | **Gold, deducted from the transferred amount** | **100% to DigixDAO** |
| **Recast (redemption)** | **1%** | **Gold** | DigixGlobal |
| **Minting** | None to depositor | n/a | n/a |

So DGD holders received **all** of the transfer fee plus **one third** of the demurrage. That is a real, external-facing, fee-funded revenue share: not recycled subscription fees, but a genuine usage-based cut.

### How demurrage worked mechanically

This is the part that matters, and it is worth being exact because Aurumix's peg is grams ÷ tokens.

**Digix did not change the token count. It changed what `balanceOf` returned.**

The DGX contract stored an **actual balance in nanograms** on its internal ledger, then computed the **effective balance** returned to any caller by subtracting accrued demurrage:

```
b = (a / m) * (r * t)
```

where:
- `b` = demurrage owed, netted off the effective DGX balance in nanograms (what `balanceOf` returns)
- `a` = actual DGX balance in nanograms on the internal ledger
- `m` = minimum balance unit for demurrage calculation (constant, 1 milligram)
- `r` = daily demurrage per 1 milligram
- `t` = number of days since the last demurrage deduction

The implementation used the constants `demurrage_base = 10,000,000` and `demurrage_rate = 165`, applied per **whole day** elapsed:

```
demurrage_fees = days_elapsed * user_balance * demurrage_rate / demurrage_base
days_elapsed   = (current_time - last_demurrage_payment_timestamp) / ONE_DAY_DURATION_IN_SECONDS
```

Partial days did not trigger a charge: the contract advanced `last_demurrage_payment_timestamp` by exactly `days_elapsed`, leaving the remainder to accrue. Linear accrual, not exponential, which the auditors specifically criticised.

The transfer fee used the same in-kind pattern: `transfer_fees = transfer_amount * 13 / 10,000`, **deducted from the amount sent**, so a recipient of a 100 DGX transfer received 99.87 DGX. The audit report notes this explicitly: *"fees are reduced from sent amount, and users should take this into account when using the token for payment. This behavior is non-standard in ERC20 token contracts, however is needed to support Digix business model."*

### What it did to the gold ratio: the crucial point

**It did not break the 1 DGX = 1 gram peg. It broke the holder's balance instead.**

This distinction is everything for the client. Digix preserved the invariant "1 DGX = 1 gram" by making the **number of DGX you own shrink over time**. A holder with 100 DGX had, a year later, 99.4 DGX. Each of those 99.4 tokens was still exactly 1 gram of gold. The vault held less gold, the ledger held proportionally fewer tokens, and the ratio was untouched.

That is the opposite architectural choice from Paxos, which (per the wave-1 PAXG finding) reserves the right to **mint new tokens to itself pro rata**, holding the holder's token count constant while diluting grams-per-token. Two mechanisms, opposite directions:

| | Digix demurrage | Paxos mint-to-self |
|---|---|---|
| Token count per holder | **Shrinks** | Constant |
| Grams per token | Constant | **Shrinks** |
| Effect on a 1:1 peg | Peg preserved | **Peg broken** |
| Effect on an Aurumix-style grams ÷ tokens peg | **Peg preserved** | **Peg preserved** |

**This changes the advice to the client.** The client's stated reason for ruling out gram-denominated fees is that "gram deduction breaks it [the peg]." On the Digix mechanism specifically, **that reasoning does not hold**. Aurumix's price is (vault grams ÷ tokens). If a Digix-style demurrage burns tokens pro rata while the vault pays the storage bill in gold, both numerator and denominator fall together and **the price per token is unchanged**. Digix-style demurrage is arithmetically peg-neutral for Aurumix, exactly as the wave-1 brief notes the PAXG mint-clause is.

**So the case against demurrage for Aurumix is not arithmetic. It is everything else**, and the real reasons are stronger than the stated one:

1. **It is non-standard ERC-20 and it breaks integrations.** A `balanceOf` that decreases with no transfer event violates every assumption exchanges, wallets, accounting systems and custodians make. Digix needed a separate wrapper token (**LiteDGX**) purely to present a normal ERC-20 face to the ecosystem, whose stated purpose was "No transfer fees, No demurrage fees." **Digix had to build a second token to undo its own fee mechanism.** For Aurumix, whose token additionally carries ICS standing, dividend entitlement and credit eligibility, a silently mutating balance is a direct hazard: every one of those systems reads a balance.
2. **It is hard to implement safely.** Competent auditors found a critical balance-inflation bug and a gameable fee-timing exploit, both in the fee logic.
3. **It is retail-hostile.** A savings product sold to Indian and NRI retail on a monthly SIP cannot easily explain why the number in the app went down when the customer did nothing. Aurumix's whole pitch is accumulation. A decrementing balance fights the product narrative every month.
4. **It is a visible, itemised charge on a product whose competitors charge nothing.** See §12.

Point 4 is what actually killed it.

### Did it ever generate revenue? The PMGT pattern, confirmed

**Test result: yes, Digix repeated the PMGT pattern, and did it more explicitly.**

- **Demurrage was switched off during the first year of operation** ("For the first one year, global demurrage is turned off"), so the storage fee earned nothing at launch.
- Then, in **2019, Digix zeroed it permanently.** Its own year-in-review states: *"We zeroed DGX demurrage fee so DGX holders do not have to pay the extra dollars when holding on to our gold-backed token"* ([Dev Updates, 15 January 2020](https://medium.com/digix/dev-updates-jan-15-1cd14df2426f)). Digix absorbed all storage and insurance costs itself.
- At the point of that decision, the entire fee base was **122,700 DGX**. Even at the full 0.60%, demurrage on that base was worth about **$36,000 a year gross**, of which Digix kept two thirds: **roughly $24,000 a year.** The transfer fee, on $172k of daily volume at 0.13%, was worth a few hundred dollars a day at best and went entirely to the DAO, not the company.
- So Digix gave up a revenue line worth ~$24k/yr and took on an uncapped, gold-price-linked storage and insurance liability, **permanently**.

**The arithmetic is the finding.** The demurrage fee was never large enough to fund the business, because the AUM was never large enough. Digix faced competitors (PAXG launched September 2019, the same year) charging **zero** storage. It could not hold a visible 0.60% annual charge against a zero-fee competitor, so it matched them to nil. And at that moment the DGX business had **no revenue line of its own at all**: no storage fee, no minting fee, transfer fees assigned to the DAO, and only an occasional 1% recast fee from a redemption process requiring physical presence in Singapore.

**Digix therefore entered its final phase in exactly PMGT's position: a working gold token with no revenue and no internal advocate.** The difference is that PMGT launched that way, while Digix *chose* it in 2019 under competitive pressure. Both died of the same thing.

## 8. Token architecture

- **Standard**: ERC-20, but **deliberately non-standard in behaviour**. Balances decrease without transfer events; fees are deducted from sent amounts. The 2017 audit flags this as needed "to support Digix business model."
- **LiteDGX wrapper**: a separate ERC-677/ERC-20 wrapper existed specifically to give integrators a clean, fee-free, non-decaying token. The **DGX/LiteDGX rate appreciated over time** as demurrage ate the underlying DGX held by the wrapper contract. The wrapper thus converted a *shrinking balance* into an *appreciating exchange rate*, the same economics in a form ordinary software could handle.
- **Permissioned?** No. DGX was freely transferable, no whitelist, no transfer restrictions.
- **Admin keys / upgradeability**: Digix ran a controller-based architecture (TokenTransferController, TokenApprovalController and similar), giving the operator meaningful control over token behaviour, including the ability to set demurrage to zero, which it exercised. **Confidence: Medium** on the precise key custody arrangements, which were never fully published.
- **Bridge**: none. Ethereum only, for its entire life.
- **Current on-chain state**: the contract is **still deployed and still functional**. No pause, no self-destruct. Holders can still transfer DGX to each other. **The token outlived every company that gave it meaning.**

**The DGD instrument split.** DGD was a genuinely separate governance and revenue-share token (2,000,000 fixed supply, sold in the 2016 ICO), while DGX stayed a clean asset token. This is the structure the brief identifies as our leading answer to the hybrid-regulation problem, and Digix ran it **eight years before Kinesis's KVT**. The difference: **Kinesis capped KVT at 300,000 units and sold it under an Offering Memorandum as a private placement. Digix sold DGD to the public in an unrestricted ICO.** Same structure, opposite regulatory discipline. See §12.

## 9. Liquidity and market

One paragraph, per the wave-1 instruction not to re-argue the premium thesis.

DGX today: **15,400 tokens outstanding** (~15.4 kg gold), ~2,103 holders, ~$278k on-chain market value, price tracking gold at ~$18.52/g, and **24-hour trading volume of nil**. Trackers show stale price stamps from May 2026 against a July 2026 date, the signature of an asset with no trades to update it. Bitfinex delisted DGX on **18 June 2021**; no major exchange lists it today. At peak (January 2020) DGX had 122,700 tokens, ~$6.0M market cap, $172,274 daily volume, 1,751 holders and listings on 12 exchanges. DGD trades at ~$0.067 against an all-time high of $1,291, a **99.99% decline**, with **$0** 24-hour volume: the correct price for a token whose only remaining function is to be burned for its ETH claim. **Digix adds a terminal data point to the settled conclusion: no premium, and eventually no market at all.**

## 10. Distribution

- **Channels**: direct via the Digix marketplace, plus exchange listings (12 by end-2019) and DEX integrations (AirSwap, Tokenlon/imToken). Trading pairs in 7 quote currencies (ETH, USD, IDR, USDT, DAI, BTC, VND).
- **Geography**: Singapore base, with a documented push into **Indonesia and Vietnam** (IDR and VND pairs) and a China marketplace opening in 2019. Notably retail-oriented and **Asian-emerging-market focused**, which is the closest geographic analogue in the set to Aurumix's India/NRI target.
- **Savings plan / recurring purchase**: **None found.** No SIP, no auto-invest, no recurring contribution mechanism.
- **Referral / affiliate / agent network**: **None found.**
- **Target segment**: crypto-native holders wanting gold exposure, not savers.

**The finding for the client is the gap.** Digix reached emerging-market Asian retail through **exchange listings**, which is a passive channel: it waits for people who already hold crypto. It built no acquisition mechanism, no recurring contribution, and no commissioned distribution. Over eight years it accumulated ~$6M peak AUM. **Aurumix's agent network and SIP are, on this evidence, the genuinely differentiated part of its design**, and Digix is the cautionary case for what happens without them: a technically excellent product with no engine to acquire customers.

## 11. Wind-down timeline

Dated, reverse chronological.

| Date | Event |
|---|---|
| **19 July 2026** | **DIGIX HOLDINGS PRIVATE LIMITED (UEN 201724450M) struck off the Singapore register**, having been gazetted 6 April 2026. The last Digix entity to go ([RecordOwl](https://recordowl.com/company/digix-holdings-private-limited)) |
| **6 April 2026** | Digix Holdings gazetted for strike-off by ACRA |
| **Feb 2025 – Jul 2026** | **Total silence.** A dedicated recency sweep found no announcements, filings, redemption notices, incidents or partnership news for Digix, DGX, DGD or NexusGold FZC anywhere in this window |
| **28 July 2026 (tested)** | digix.global: **connection refused**. nexusone-dgx.com: **connection refused**. Digix Zendesk: **403 Forbidden**. No live redemption channel exists |
| **4 September 2023** | **DIGIX MARKETS PTE. LTD. (201906348R) and DIGIX PHYSICALS PTE. LTD. (201724269N) struck off** by ACRA Final Gazette. **The entity holding legal title to the gold ceased to exist** |
| **4 July 2023** | ACRA First Gazette: Digix Markets and Digix Physicals notified for striking off |
| **21 March 2023** | **Digix ceases operations.** Redemption facilities handed to **NexusGold FZC** (licence 4306536.01), an overseas partner whose jurisdiction and current status we could not verify |
| **September 2022** | **Digix Holdings withdraws its Payment Services Act licensing in Singapore** and announces: *"We regret to inform you that we will not be taking any more new transactions and would be ceasing all business activities"* ([IQ.wiki](https://iq.wiki/wiki/digix-gold-token)) |
| **18 June 2021** | **Bitfinex delists DGX**, trading ceased 12:00 UTC ([Bitfinex](https://support.bitfinex.com/hc/en-us/articles/360008482333-Digix-Gold-Delisted)) |
| **March 2020** | **"Acid" refund contract deployed** at `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`. DGD holders burn DGD for ETH at a fixed **0.193054178 ETH per DGD**. No deadline |
| **12 May 2020** | Bittrex snapshot of DGD balances for exchange-side distribution. Binance, Gate and others distribute ETH to holders at the same fixed ratio |
| **~February 2020** | DGD unstaked at the start of the following Digix quarter; ETH distributions begin |
| **20 January 2020** | **DigixDAO votes to dissolve.** "Project Ragnarok" passes with **>95% support on only 52 votes cast** (against ~11,000 DGD addresses). Treasury: **~386,428 ETH, ~$64M**. **Digix the company opposed the dissolution and abstained** ([CoinDesk](https://www.coindesk.com/markets/2020/01/20/digixdao-votes-to-liquidate-64m-treasury)) |
| **29 November 2019** | **Kai Cheng Chng publishes the Project Ragnarok proposal**, offering a quarterly dissolution vote in response to demands for "a mechanism for dissatisfied DGD token holders to make a clean break." States: *"Digix is against the dissolution"* and will abstain, but will *"respect and adhere to the collective opinion [of] DGD holders"* ([proposal](https://medium.com/digix/proposal-announcement-project-ragnarok-integrating-a-dissolution-mechanism-for-digixdao-354fd871e3e0)) |
| **2019** | **Digix zeroes the DGX demurrage fee permanently**, absorbing storage and insurance costs itself. The DGX business loses its only recurring revenue line |
| **September 2019** | PAXG launches with zero storage fee, into the same market |
| **March 2016** | DGD ICO raises **466,648 ETH** (~$5.5M) in the first major Ethereum token sale |
| **December 2014** | Digix founded in Singapore |

### What actually drove the wind-down

The causal chain, stated plainly:

1. **DGX never achieved scale.** Peak AUM ~$6M after five years. The gold token was a product almost nobody bought.
2. **Because DGX had no scale, its fees could not fund the company.** Full-rate demurrage on peak AUM was ~$24k/yr to Digix.
3. **Competitive pressure from zero-fee entrants (PAXG, September 2019) forced the fee to zero in 2019.** Digix could not defend a visible 0.60% charge against a free competitor, so it eliminated its own revenue and absorbed the storage cost.
4. **The company had been living on the ICO treasury, not on revenue.** DGD's price tracked the ETH in the treasury almost exactly, which told the market the operating business was contributing no independent value. As one analysis put it: *"if DGD's total market cap mirrors the total value of ETH in the DigixDAO treasury, the money spent from the treasury must be getting wasted."*
5. **Holders noticed and voted to take the treasury back.** Ragnarok passed over management's objection on 52 votes. **~$64M left the ecosystem.**
6. **A revenue-less company minus its treasury has no runway.** DGX had no fees, no scale, and now no subsidy.
7. **Wind-down followed**: PSA licence withdrawn and business ceased (Sept 2022), operations ended and redemption outsourced offshore (March 2023), title-holding entity struck off (Sept 2023), parent struck off (July 2026).

**The DAO dissolution was not the wind-down mechanism. It was the trigger.** The brief's framing has this backwards, and the correction matters: a well-executed structured treasury return to one class of holders was, from the other class's perspective, the removal of the subsidy that kept their gold redeemable.

## 12. Relevance to Aurumix

Digix is the most instructive failure in the set because it did the engineering well and the business badly.

### 1. The demurrage question, answered precisely (client design question 1)

**The client's stated reason for ruling out gram-denominated fees is wrong, but the conclusion is right for better reasons.** Digix-style demurrage burns tokens pro rata, holding grams-per-token constant. Against Aurumix's grams ÷ tokens peg it is **arithmetically neutral**. If the client is defending this decision to a technical reader, "gram deduction breaks the peg" will not survive scrutiny. **Use these reasons instead**: it makes `balanceOf` non-standard and breaks every downstream integration (Digix needed a whole second token, LiteDGX, to work around its own mechanism, and Aurumix's ICS, dividend and credit systems all read balances); competent auditors found a critical bug and a timing exploit in the fee logic itself; and a decrementing balance is indefensible in a monthly-SIP savings product sold to retail. **Charge in cash.**

### 2. The zero-fee trap, now confirmed twice (client design question 1)

PMGT launched with zero fees and had no internal advocate. **Digix started with fees, could not defend them against a zero-fee competitor, and cut them to nil in 2019.** Then it died. The wave-1 conclusion that "zero ongoing custody fee is the near-universal norm" now has a mechanism attached: **it is not a norm, it is the equilibrium of a price war that no small issuer survives, because the fee is visible and itemised while the competitor's is zero.**

The strategic read for Aurumix is that a **visible, itemised custody fee on a commodity gold product is competitively indefensible**. Aurumix's escape route is that **it is not selling a custody product**. It is selling a savings plan with ICS tiers, credit access and a dividend. Fees should be attached to those distinguishing services, where there is no zero-fee competitor, and not to the storage of gold, where there is. This is the strongest available argument for the client's "recover cost elsewhere" option.

### 3. Wind-down: the most valuable finding in this profile (client design question 9)

**Digix is the proof of the client's cheapest differentiator.** Follow the metal:

- 15,400 DGX still exist, nominally ~15.4 kg of gold, ~$1.5M.
- The company that held legal title to that gold was **struck off on 4 September 2023**.
- **No public record exists of what happened to the metal.** No final audit, no reconciliation, no disposition filing.
- Holders received **no formal notice that redemption had ended**. The portal simply stopped responding.
- The redemption agent it was handed to cannot be verified in any register.

This is the concrete, documented answer to "what happens if the issuer fails." **The gold vanishes from the public record and the holder is left with a live token, a dead counterparty, and no forum.** Aurumix committing ex ante to a wind-down protocol (a named successor custodian, a defined notice period, a final published reconciliation, and a mechanism that survives issuer strike-off) costs nothing at design time and is a genuine differentiator against every protocol in this landscape.

**Add one Digix mechanism directly**: the **automatic re-mint of uncollected gold**. It solves abandoned redemptions without ever leaving the token unbacked, and it is the kind of detail that signals real operational thinking.

### 4. The instrument split, with the regulatory lesson attached (client design questions 2 and 3)

Digix ran the two-token split (clean DGX asset token, separate DGD revenue-share token) **eight years before Kinesis**. It validates the structure the brief calls our leading answer to hybrid regulation, but it adds the essential caveat.

**Kinesis capped KVT at 300,000 and sold it privately under an Offering Memorandum. Digix sold DGD to the public in an unrestricted ICO. Same structure, opposite discipline, opposite outcome.** DGD became a liquid, publicly traded claim on a corporate treasury held by ~11,000 addresses who could vote to seize it, and did.

**The direct warning for the ICS Dividend**: if Aurumix's dividend entitlement is freely transferable and publicly traded, it becomes an instrument whose holders can act collectively against the operating company. Digix's management lost control of $64M of its own balance sheet to a 52-vote poll. If Aurumix separates its dividend right into a distinct instrument, **cap it, place it privately, and do not give it governance power over treasury assets.** The client's lean toward a permissioned base (ERC-3643) is well supported here.

### 5. The DGD treasury return: what holders actually got (client's specific question)

**Mechanism**: the "Acid" refund contract at `0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`. A holder approves DGD to the contract and calls `burn()`, which **permanently burns the DGD** and sends ETH pro rata.

**Ratio**: **0.193054178 ETH per DGD**, fixed. Applied identically on-chain and by exchanges (Binance, Bittrex, Gate) that ran the conversion for their users.

**Voluntary or governed?** **Both, in sequence, and the distinction is the interesting part.** It was governed by a formal on-chain governance document (the Project Ragnarok proposal, 29 November 2019) and executed through DigixDAO's standard project-voting machinery with quota and quorum requirements. But the **company opposed it and abstained**, and complied because it had pre-committed to respect the outcome. The *claim* is then voluntary and perpetual: **no deadline, still open, and ~12,491 ETH remains unclaimed** six years later.

**Two observations.** First, this is the **only well-executed wind-down mechanism found anywhere in this landscape**: a fixed ratio, an open-source contract, no deadline, and no discretion left with the issuer. It is a good model, and Aurumix should copy its properties (fixed formula, permissionless claim, no expiry, no issuer discretion) for its own wind-down commitment. Second, note what it protected and what it did not: **DGD holders got a clean, precise, permanent exit. DGX holders, whose tokens were backed by actual gold, got a dead website.** The governance token holders were made whole; the asset token holders were abandoned.

**That asymmetry is the lesson.** Aurumix must ensure its wind-down protections attach to the **gold-holding retail saver**, not to whichever class happens to hold the governance rights.

### 6. Not applicable

Digix paid **no yield to DGX holders** (question 2 is not directly addressed beyond the DGD fee share, which was genuine external usage revenue, not recycled subscriptions). It had **no savings plan, referral or agent distribution** (question 8: the finding is the absence, and it is a large part of why Digix never scaled). It **held no licence** to compare on question 4.

## 13. Open items for verification

- [ ] **Locate the physical gold.** Contact The Safe House Singapore to establish whether gold formerly held for Digix Physicals Pte Ltd remains in the vault and in whose name. This is the single highest-value unresolved fact.
- [ ] **Verify NexusGold FZC** against UAE free-zone registers (Hamriyah, SAIF Zone, Sharjah Media City, RAKEZ, Ajman) using licence number **4306536.01**. Establish its jurisdiction, current status, and whether it ever operated a DGX redemption facility.
- [ ] Determine the **bona vacantia position** of assets held by Digix Physicals Pte Ltd at strike-off (4 September 2023), and whether any application to restore the company to the register has been made.
- [ ] Obtain the **actual MAS Payment Services Act record** for Digix Holdings: licence class, application status, and the formal disposition of the September 2022 withdrawal.
- [ ] Confirm the **current ETH balance of the Acid refund contract** (`0x23Ea10CC1e6EBdB499D24E45369A35f43627062f`) directly on-chain; the ~12,491 ETH unclaimed figure needs a dated on-chain check.
- [ ] Retrieve the **DGX custody agreement or terms of issue** from web archives to confirm the legal-title analysis in §2 against a primary document rather than secondary commentary.
- [ ] Verify the **exact date and text of the Digix tweet** announcing cessation of business activities (September 2022); we have the quote via IQ.wiki but not the primary post.
- [ ] Pull the **PoP / bar-list records from IPFS** if any pinning survives, to establish the last published bar inventory before shutdown.
- [ ] Check whether **DGD's 0.193054178 ETH/DGD ratio** was ever challenged or litigated, and whether unclaimed ETH has any escheatment exposure.
- [ ] Establish whether **Digix Markets Pte Ltd** (SSIC "fund management activities n.e.c.", incorporated Feb 2019) ever conducted regulated fund management, which would be a separate MAS licensing question.
