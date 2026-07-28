# Midas Labs / GoldZip (XGZ)

> **Scope correction, read this first.** This profile was commissioned as "Midas mXGZ / XGZ (Midas, the tokenized-yield issuer)" on the premise that Midas issues a yield-bearing gold product under a European issuer-SPV note programme. **That premise is wrong on three counts, and the corrections are the most valuable output of this profile.** See §0.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | **XGZ** ("GoldZip", on-chain token name "GoldZip Gold") | High (on-chain) |
| Does "mXGZ" exist? | **No. Not found anywhere**: not on the issuer's docs, HKGX, CoinGecko, CoinMarketCap, rwa.xyz, or any exchange | High (negative search) |
| Issuer (marketing) | "GoldZip", a subsidiary of the Hong Kong Gold Exchange (HKGX). HKGX names **GoldZip Pte. Ltd.**; the token's own site and CoinMarketCap name **GoldZip Digital Pte. Ltd.** The two conflict | High (that they conflict) |
| Issuer (registry) | **GoldZip Pte. Ltd., UEN 202119587H** and **GoldZip Digital Pte. Ltd., UEN 202119588Z**, both incorporated **3 June 2021**, Singapore. ACRA principal activity for both: **development of software and applications (except games and cybersecurity)** | High (ACRA) |
| Domicile | **Singapore** (issuer). Gold and vaults in **Hong Kong**. Parent HKGX is Hong Kong | High |
| Backing claim | 1 XGZ = 1 gram of 99.99% fine gold in "HKGX recognised" vaults | Medium (issuer assertion) |
| Chains | Ethereum only | High (on-chain) |
| Contract address | `0x69af64f409c08E9076bF7f3ed9Db3a7409717161`, 8 decimals | High (on-chain) |
| Supply | **39,000 XGZ = 39.0 kg gold** | High (Ethplorer, 28 Jul 2026) |
| Market cap / TVL | **~$5.06M** at $129.68/token | High |
| 24h volume | **~$113k**, of which **92.4% is a single MEXC XGZ/USDT pair**. Uniswap V4 pairs combined: **under $320/day** | High (CoinGecko) |
| Holders | **264** | High (on-chain) |
| Price vs spot | **$129.68 vs ~$131.50/g spot: a ~1.4% DISCOUNT** | High |
| Regulatory status | **No financial-services licence anywhere.** Claimed status is a Singapore MinLaw **PSPM Act dealer registration**, which is an AML/CFT registration, not a licence to issue investment products. No MAS licence found | High |
| Subscription fee | Not disclosed | Not disclosed |
| Ongoing custody fee | **Not disclosed**, and who pays vault cost is **not disclosed** | Not disclosed |
| Transfer fee | **0.01% of transaction amount, paid by sender**, levied on-chain | High (issuer docs) |
| Redemption fee | "Standard settlement timelines and **handling fees apply**": amount **not disclosed** | High (that it is undisclosed) |
| Advertised yield | **None. XGZ pays no yield of any kind** | High |
| Named officers | **Barry Ip**, Director / Head of Digital Innovation, HKGX. **Juha Viitala**, SEO of Universal Digital (MoU counterparty) | High |

---

## 0. Three corrections to the task premise

**Correction 1: there are two unrelated companies called "Midas", and this profile is about the smaller one.**

- **Midas / midas.app** is a Berlin RWA tokenization platform issuing mTBILL, mBASIS, mBTC and mXRP through **Midas Software GmbH** (Germany, created 30 June 2023, Kurfürstendamm 15, Berlin), a subsidiary of **Midas Protocol Limited, UK Companies House number 15217097**, incorporated 17 October 2023 ([readi.fi issuer profile](https://readi.fi/issuer/tokenized-real-world-assets-issuer-midas/), [Companies House](https://find-and-update.company-information.service.gov.uk/search?q=Midas+Protocol+Limited)). This is the entity the task description actually describes: European issuer SPV, prospectus-based note programme.
- **Midas Labs** (midaslabs.xyz) is GoldZip's **Web3 development contractor**. It is not an issuer of anything ([PR Newswire via Manila Times](https://www.manilatimes.net/2026/07/02/tmt-newswire/pr-newswire/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/2377222)).
- **No source establishes any corporate relationship between them.** Sonar Pro, searching UK Companies House and public profiles, returned "not found" for any ownership, subsidiary or common-parent link and concluded they are separate, unrelated entities. Midas Labs' own jurisdiction and registration number are **not found in any register**: a notable gap for a company being named as strategic infrastructure partner to a 115-year-old exchange.

**Correction 2: the Midas that does have the European prospectus wrapper issues no gold product at all.**

Midas Software GmbH's disclosed product suite is US Treasuries (mTBILL), a crypto basis trade (mBASIS), mBTC and mXRP, with stated future expansion into corporate bonds and structured credit. **No gold-backed or gold-linked token, confirmed explicitly** ([readi.fi](https://readi.fi/issuer/tokenized-real-world-assets-issuer-midas/), [rwa.xyz platform page](https://app.rwa.xyz/platforms/midas)). So the specific thing the task asked for, a Midas gold product under a note programme, **does not exist**.

**Correction 3: "mXGZ" does not exist.** Two independent Sonar Pro sweeps plus direct searches of the issuer GitBook, HKGX, CoinGecko, CoinMarketCap, rwa.xyz, Etherscan and exchange listings return **no token, product or ticker called mXGZ**. The real token is plain **XGZ**, and it is a non-yielding 1g gold token. The "m" prefix belongs to the other Midas's naming convention (mTBILL, mBASIS, mXRP), which is almost certainly how the two got conflated.

**Net effect for Aurumix: the yield-bearing-gold-under-a-prospectus precedent that this profile was commissioned to find does not exist here.** That is a real finding, not a research failure. It is documented in §12.

---

## 1. What it is

XGZ is a gold-backed ERC-20 token on Ethereum. One token represents one gram of 99.99% fine gold held in vaults accredited by the Hong Kong Gold Exchange ([GoldZip GitBook](https://goldzip-1.gitbook.io/goldzip/goldzip-xgz/what-is-usdxgz)). It launched **23 December 2025** ([Decrypt](https://decrypt.co/353315/hkgx-backed-goldzip-launches-xgz-asias-first-gold-token-supported-by-a-leading-gold-exchange)).

Its distinguishing pitch is institutional parentage: HKGX (formerly the Chinese Gold & Silver Exchange Society) is Hong Kong's sole recognised gold exchange, over 100 years old, and GoldZip is marketed as "Asia's first gold token supported by a leading gold exchange." Midas Labs is the outsourced Web3 builder, named strategic partner on **19 May 2026** ([cointrust](https://www.cointrust.com/market-news/goldzip-and-midas-labs-advance-digital-gold-ecosystem)).

It is very small: **39 kg of gold, ~$5.06M, 264 holders**. That is roughly two-thirds the size of ORO by value and it has one-thirty-seventh as many holders. The distribution is institutional-shaped, not retail-shaped, which is the mirror image of ORO (9,700 holders sharing 19 kg).

---

## 2. Legal structure

**What a holder actually owns is not documented.** This is the central gap.

The GitBook, HKGX's product page, and every listing describe XGZ as "backed by" gold and give holders a **redemption right** subject to KYC/AML. None of them state whether the holder has:

- legal title to identified bars, or
- a beneficial interest under a declared trust, or
- a bailment, or
- an unsecured contractual claim against the issuer.

**No prospectus, base prospectus, terms and conditions of notes, final terms, offering memorandum or published terms of issue exists for XGZ.** Searched: the issuer's site, the GitBook (whose full page index was retrieved via `llms.txt`), HKGX's site, and rwa.xyz. **Not found in any of them.** The GoldZip website footer references "Terms & Conditions", "Rules" and "Legal Policy" pages, but no operative gold-title or insolvency provision could be retrieved from them.

**What happens to holders on issuer insolvency is Not disclosed.** There is no segregation statement, no trust account, no ranking in a winding-up, no wind-down plan.

**On "bankruptcy remote":** rwa.xyz's data sheet carries the label "Account Segregation: Bankruptcy Remote" for XGZ. **Nothing in the issuer's own documentation supports it.** There is no named trustee, no trust deed, no declaration of trust, no jurisdiction for a segregation structure. This is the identical pattern to ORO's unverifiable "ORO Foundation": a third-party data aggregator surfacing a legal conclusion that has no published instrument behind it. **Treat it as unsupported.**

Absent any of that, the defensible reading is that an XGZ holder has a **contractual redemption claim against a Singapore private limited company whose registered business activity is software development**. Confidence: Medium on that characterisation, High that no better-documented structure is published.

**Confidence: High** that no prospectus or note terms exist. **Not disclosed** on insolvency ranking.

---

## 3. Regulatory and compliance posture

**No financial-services licence in any jurisdiction.**

| Register / claim | Result |
|---|---|
| Singapore MinLaw, PSPM Act regulated dealer | **GoldZip Digital Pte. Ltd. appears on the registered dealers list.** HKGX instead attributes this registration to GoldZip **Pte. Ltd.** The two claims conflict |
| MAS Capital Markets Services licence | **Not found** |
| MAS Payment Services / DPT licence | **Not found** |
| Hong Kong SFC | **Not found**, and XGZ is explicitly **not available to Hong Kong residents** |
| rwa.xyz regulatory status field | Lists XGZ as **"Non-Regulated"** |

**The PSPM Act point is the one that matters and it is routinely misread.** Registration as a regulated dealer under Singapore's Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019 is an **AML/CFT registration administered by the Ministry of Law**, applying to jewellers, bullion traders, pawnbrokers and auction houses ([MinLaw ACD](https://acd.mlaw.gov.sg/list-of-registered-dealers/), [GoBusiness licence directory](https://licensing.gobusiness.gov.sg/licence-directory/minlaw/registration-of-precious-stones-and-precious-metals-dealers)). It is **not** a prudential licence, **not** a securities or capital-markets authorisation, and it confers **no** permission to issue an investment product, hold client assets, or offer tokens to the public.

Marketing compresses this into "regulated by the Ministry of Law (MinLaw) in Singapore" (on goldzip.info and repeated verbatim by CoinMarketCap) and, in the July 2026 MoU release, into GoldZip **"holding a full regulatory compliance license in Singapore."** That last phrasing is materially misleading: there is no such licence. **This is the same category error as Comtech's DAFZA precious-metals licence: a trade/AML registration being presented as authorisation to issue a token.**

**The registry check adds a third problem.** ACRA records the principal activity of **both** GoldZip entities as *development of software and applications (except games and cybersecurity)*. Neither carries a precious-metals or financial-services activity code. Both were incorporated **3 June 2021**, two and a half years before the token launched.

**Confidence: High.**

---

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian | **Not disclosed by the issuer.** GitBook says only "licensed gold vaults accredited by HKGX". rwa.xyz asserts **Brink's Global Services**: unconfirmed by any issuer document | Low (Brink's) / High (issuer silence) |
| Vault / city | **Not disclosed.** Implied Hong Kong via HKGX depositories; never stated | Not disclosed |
| Allocated? | **Not disclosed.** No allocation or segregation language anywhere | Not disclosed |
| Bar list | **None published.** Docs refer generically to "GoldZip Eligible Gold Bars" and "selected specified brands" | High (negative) |
| PoR feed | **None.** No Chainlink or other on-chain PoR oracle | High (negative) |
| Reserve attestation | **Promised, not delivered.** GitBook: *"Periodic attestation reports by accredited auditors."* No auditor named, no cadence, no report published, no URL | High |
| Smart contract audit | GitBook's smart-contract page **links an audit file and a GitHub commit**, but no auditor name or findings were retrievable, and no published report was found in any audit-firm index | Low |
| Insurance | Claimed as "insured vaults" in secondary coverage only. No insurer, policy or limit disclosed | Low |

**Applying the brief's rule on conflating the two audit types:** GoldZip is on the correct side of the wording but the wrong side of substance. It uses the precise phrase "attestation reports by accredited auditors" (correctly reserve language) **but has published none**. Meanwhile the only artefact that appears to exist is a smart-contract audit file. **So the one thing plausibly audited is the code, and the 39 kg of gold has no published attestation at all.** For a token whose entire proposition is exchange-grade custodial credibility, that is the single largest evidentiary hole in the product.

---

## 5. Issuance

Minting is **not open**. rwa.xyz states that **only HKGX members, all KYB-verified, can mint XGZ** by depositing physical gold into the vault. The GitBook describes a three-step process: accept gold from trusted refineries meeting specification, conduct international assay verification of fineness, then issue XGZ on-chain for distribution through exchanges and distributors.

Eligible metal is tightly specified: **minimum 1 kilogram bars of 999.9 fine gold** from selected brands. Minimum mint size and mint fees: **Not disclosed**.

This is a **wholesale, members-only primary market**. Retail participation exists only on the secondary market (MEXC, Uniswap). The practical consequence for the peg is in §9.

---

## 6. Redemption

**Redemption is documented but not yet operational.** The GitBook's redemption page states delivery is available "from **1,000 XGZ per delivery bar**" (i.e. a 1 kg minimum), that "standard settlement timelines and **handling fees apply**", and that fulfilment is by "pickup or delivery via authorized partners, subject to KYC/AML and jurisdictional rules."

Then it says this:

> *"Step-by-step instructions, forms, and venue details will be published when redemption windows open."*

**Redemption windows have not opened.** Seven months after launch, the issuer has published no process, no forms, no venues, no fee schedule and no timeline. Redemption is a stated intention, not a live facility.

**The eligibility arithmetic is brutal.** Minimum redemption is 1,000 XGZ (~$129,700). Total supply is 39,000 XGZ across **264 holders**, an average holding of ~148 XGZ (~$19,200). **The average holder is roughly 6.8x below the redemption floor.** Combined with a members-only mint, XGZ is for most holders a one-way instrument with no primary-market exit at all.

This is exactly the "eligibility limited to undefined qualified holders" pattern the brief warns about, in a harder form: eligibility is limited by a bar-sized minimum plus unpublished "jurisdictional rules", and Hong Kong residents are excluded outright.

---

## 7. Fees and revenue model

| Fee line | Amount | Source |
|---|---|---|
| Mint / subscription | **Not disclosed** | — |
| On-chain transfer fee | **0.01% of transfer amount, paid by sender** | GitBook specifications |
| Ongoing custody / storage | **Not disclosed** whether any is charged | — |
| Redemption | "**Handling fees apply**", amount **Not disclosed** | GitBook redemption page |
| Management / performance | **0% / 0%** | rwa.xyz |
| Yield to holders | **None** | High |

**The transfer fee is the one genuinely unusual mechanism here and it is worth Aurumix's attention.** XGZ levies a **protocol-level 0.01% fee on every on-chain transfer**, taken from the sender. Almost no gold token does this: PAXG, XAUT, XAUm, VNXAU and Comtech all charge zero on transfer. It converts velocity into revenue rather than taxing the balance.

**Who pays for the vault is Not disclosed.** With 0% management fee, no disclosed storage fee, and a mint fee that is also undisclosed, the only visible recurring revenue line is 0.01% of transfer volume. Against ~39 kg of gold, that is negligible: even at $113k of daily on-chain-equivalent turnover, 0.01% is roughly **$11 a day, about $4,100 a year**. Real vaulting, insurance and assay costs for 39 kg exceed that comfortably. **The economics only work because HKGX is absorbing the cost as a strategic loss-leader**, which is an inference, not a disclosure, and it is exactly the fragility that killed PMGT (zero fees, zero revenue, no internal advocate).

---

## 8. Token architecture

- **Chain:** Ethereum only. **Standard:** ERC-20, 8 decimals. Not ERC-3643 or any permissioned standard.
- **Contract:** `0x69af64f409c08E9076bF7f3ed9Db3a7409717161`, owner address `0xd173e69192b9ff22069aa913ef6e6e94b19f0778`.
- **Transfers:** freely transferable at the contract level. **No whitelist, no on-chain permissioning.**
- **Upgradeability, proxy pattern, pause / freeze / blacklist / forced-transfer functions, admin key custody (multisig vs single key): Not disclosed** in issuer documentation.

**The architecture directly contradicts the compliance posture, and this is the structurally interesting part.** The primary market is locked to KYB-verified HKGX members and redemption requires KYC plus "jurisdictional rules", yet the token itself is a **plain permissionless ERC-20**. Once minted, it moves to anyone, anywhere, including into the hands of the Hong Kong residents the issuer says are excluded. **The compliance perimeter exists only at mint and redeem; the middle is entirely open.** The one enforcement mechanism actually implemented on-chain is a 0.01% fee, not a transfer restriction.

---

## 9. Liquidity and market

**~$5.06M market cap, ~$113k daily volume (2.2% turnover), 264 holders, and it trades at a ~1.4% DISCOUNT to spot** ($129.68 vs ~$131.50/g on 27–28 July 2026).

Liquidity is almost entirely custodial, not on-chain: **92.4% of volume is the MEXC XGZ/USDT pair** ($104k), BitKan adds ~$8.2k, and the two **Uniswap V4 pairs combined turn over under $320 a day**. All-time high $162.73 (7 July 2026) against an all-time low of $126.60 (30 June 2026) is a 28% range in five weeks for an instrument that should track a metal that moved a fraction of that: evidence of a thin, gappy market rather than a tracking one.

One more data point for the settled premium thesis, and it lands where the brief predicts: **XGZ is a discount case, like ORO**. The mechanism is visible here. Arbitrage cannot close the discount because **you cannot mint unless you are an HKGX member and you cannot redeem below 1 kg**, so no ordinary participant can buy the discount and redeem into metal. **The permissioned primary market is precisely what prevents the discount from closing.** Question 6 remains dead; XGZ shows a new reason why.

---

## 10. Distribution

**No savings plan, no recurring purchase, no referral programme, no affiliate scheme, no agent network. None found.**

Distribution is: HKGX member institutions at the primary level, then a MEXC listing and a Uniswap pool for everyone else, plus the "exchanges and distributors" the GitBook mentions without naming. Target segment is Asian institutional and semi-professional gold traders already inside the HKGX orbit. Geography excludes Hong Kong residents.

The one distribution-shaped initiative is the **UAE corridor MoU** (§11), which is a B2B liquidity partnership, not a retail channel.

**For Aurumix this protocol contributes nothing on question 8 except further confirmation that the recurring-contribution model is unoccupied ground.** Nine profiles in, still no competitor has built one.

---

## 11. Recent developments

- **2 July 2026:** MoU between **Universal Digital Intl Limited** (ADGM-based issuer of the USDU stablecoin), **Midas Labs**, and **GoldZip Digital Pte. Ltd.** to explore linking the UAE's regulated stablecoin ecosystem with Asian digital gold. Universal Digital holds **ADGM FSRA financial services permission No. 250089** to issue Fiat-Referenced Tokens **to Professional Clients**, and is registered with the **Central Bank of the UAE as a Foreign Payment Token issuer under the Payment Token Services Regulation (PTSR)**. The MoU is **explicitly exploratory**: it "establishes a framework for further dialogue", with no binding commitment and no product. Quotes from Barry Ip (GoldZip Director) and Juha Viitala (Universal SEO) ([Manila Times / PR Newswire](https://www.manilatimes.net/2026/07/02/tmt-newswire/pr-newswire/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/2377222), [Macau Business](https://macaubusiness.com/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/)).
- **7 July 2026:** XGZ all-time high of $162.73, ~24% above gold parity, on a market with under $320/day of DEX liquidity.
- **30 June 2026:** XGZ all-time low of $126.60.
- **19 May 2026:** GoldZip names **Midas Labs** its strategic Web3 development partner, "responsible for building the underlying digital architecture", with a stated one-to-two-year build horizon ([cointrust](https://www.cointrust.com/market-news/goldzip-and-midas-labs-advance-digital-gold-ecosystem), [TMCnet / PR Newswire](https://www.tmcnet.com/usubmit/-hong-kong-gold-exchange-subsidiary-goldzip-names-midas-labs-as-strategic-web3-/2026/05/18/10384806.htm)).
- **H1 2026 (forward-looking claim):** GoldZip projects a **US$300M gold reserve by H1 2026**, which it says would make XGZ the third-largest gold token after XAUT and PAXG ([goldzip.info/news](https://goldzip.info/news/)). **Actual reserve as at 28 July 2026: ~$5.06M, i.e. 1.7% of target.** The claim should be treated as marketing.
- **23 December 2025:** XGZ launches, listing on MEXC and Uniswap ([Decrypt](https://decrypt.co/353315/hkgx-backed-goldzip-launches-xgz-asias-first-gold-token-supported-by-a-leading-gold-exchange)).
- **Not found:** any yield/earn/staking/lending product on XGZ; any exchange delisting; any exploit, depeg or redemption failure; any published PoR or attestation; any funding round or executive change at the GoldZip entities.

---

## 12. Relevance to Aurumix

**Question 2, dividend funding: this is a negative result, and it is the most decision-relevant thing in the profile.**

The task assumed XGZ was a yield-bearing gold product wrapped in an issuer-SPV note programme, which would have made it the documented precedent Aurumix's dividend design needs. It is not. **XGZ pays no yield, the gold is not lent or leased, and there is no note programme.** Meanwhile the Midas that *does* have the European prospectus wrapper (Midas Software GmbH, Liechtenstein FMA-approved prospectus, passported across the EEA) **issues no gold product at all**.

That is worth stating plainly to the client: **an exchange-owned gold issuer with a 115-year-old parent, sitting on real vaulted metal, chose not to generate yield on it.** HKGX has better access to bullion-leasing counterparties than Aurumix ever will, and it left the gold idle. That is evidence about the risk-adjusted attractiveness of encumbering reserve gold, from the most credible institutional operator in the comparison set. It strengthens, rather than weakens, the case that **Kinesis's instrument split** (sell the yield as a separate capped security, keep the gold token clean) is the leading structural answer. **The Streamex SEC filing remains the only live lead for a documented gold-leasing precedent.**

**Question 4, regulatory route: a UAE lead worth chasing, and a warning.**

The 2 July 2026 MoU surfaces **Universal Digital Intl Limited, ADGM FSRA permission No. 250089**, plus **CBUAE registration as a Foreign Payment Token issuer under the PTSR**. This is a concrete, verifiable UAE authorisation adjacent to the ADGM route flagged in the brief. Two caveats before anyone gets excited: the permission is to issue **Fiat-Referenced Tokens to Professional Clients**, which is the opposite of Aurumix's mass-retail gold product, and the MoU is non-binding with no product behind it. **Useful as a register lead and a named comparator; not a template.**

The warning is the mirror of Comtech. GoldZip presents a **MinLaw AML dealer registration** as "full regulatory compliance license in Singapore." **Aurumix must not adopt that framing.** A precious-metals trade/AML registration is not authorisation to issue a token to the public, and the gap between the two is exactly where enforcement risk lives. If Aurumix is tempted to lean on a DMCC/DAFZA/free-zone trade licence in lieu of VARA, this is now the **second** documented example of that framing being unsupportable.

**Question 3, token standard: XGZ is the cleanest illustration of why Aurumix should not use a bare ERC-20.**

GoldZip wants a permissioned perimeter (members-only mint, KYC redemption, Hong Kong residents excluded) but implemented a **plain transferable ERC-20**. The result is a compliance regime that binds at the edges and evaporates in the middle: excluded persons can hold it, and nothing on-chain stops them. Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, **all of which break on exactly the anonymous transfer XGZ permits**. XGZ is what Aurumix's design looks like if the permissioning is deferred. It supports the ERC-3643 base.

**Question 5, redemption: a sharper version of Aurumix's own gap.**

Aurumix's honest weakness is no physical redemption. XGZ's is arguably worse and less honest: it **advertises** physical redemption while the process, forms, venues, fees and timeline "will be published when redemption windows open", seven months post-launch. Layered on a 1 kg minimum against a ~148 XGZ average holding, **~all holders are ineligible in practice**. Aurumix's cash-buyback-only design, clearly stated up front, is more defensible than a redemption promise that cannot be exercised. **Do not soften Aurumix's disclosure to match competitor marketing; the competitor marketing is the liability.**

**Question 7, proof of reserve:** GoldZip promises "periodic attestation reports by accredited auditors" and has published none, while apparently having a smart-contract audit. For Aurumix, whose entire retail pitch is "100% of every dollar buys physical gold", **shipping the attestation before the marketing is a cheap and genuine differentiator.** Four protocols in this set now blur code audits with reserve attestations; XGZ makes five.

**Question 9, wind-down:** **Not disclosed.** No insolvency provision, no segregation, no trustee, no wind-down plan. Ten profiles, still zero competitors with a published wind-down plan. **The differentiation opportunity the brief identified is confirmed and still unoccupied.**

**Question 1, custody fee:** the interesting variant is the **0.01% sender-paid transfer fee**, a velocity tax rather than a balance tax. It is peg-neutral for Aurumix's grams ÷ tokens formula since it does not touch the gram count, and it does not punish long-term holders. But the arithmetic (~$4k/yr against 39 kg) shows it cannot fund custody at small scale, which is the same revenue-starvation trap that killed PMGT.

**Question 6, premium:** one more data point, discount side. Recorded in §9, conclusion not re-argued.

---

## 13. Open items for verification

- [ ] Resolve which entity actually issues XGZ: **GoldZip Pte. Ltd. (202119587H)** per HKGX, or **GoldZip Digital Pte. Ltd. (202119588Z)** per goldzip.info and CoinMarketCap. Pull both ACRA business profiles for current directors, shareholders, share capital and any secondary SSIC codes.
- [ ] Confirm against the MinLaw regulated-dealers list which of the two entities holds the PSPM registration, and obtain the registration number. Direct scraping of `acd.mlaw.gov.sg` returned 404/403 in this pass.
- [ ] Retrieve the goldzip.info "Terms & Conditions", "Rules" and "Legal Policy" pages in full and check for any gold-title, trust, segregation or insolvency clause. These were referenced in the site footer but not retrievable here.
- [ ] Retrieve the smart-contract audit file and GitHub commit linked from the GitBook smart-contract page. Identify the auditor and whether the report covers mint authority, pause/freeze/blacklist and upgradeability.
- [ ] Inspect the verified contract source at `0x69af64f409c08E9076bF7f3ed9Db3a7409717161` on Etherscan for proxy pattern, owner privileges, and any forced-transfer or blacklist function. Determine whether owner `0xd173e6...0778` is an EOA or a multisig.
- [ ] Establish Midas Labs' jurisdiction and company registration number. It is unregistered in every source checked, despite being the named infrastructure partner to an HKGX subsidiary and a signatory to the ADGM MoU.
- [ ] Verify **ADGM FSRA permission No. 250089** for Universal Digital Intl Limited on the FSRA public register, and confirm the CBUAE PTSR Foreign Payment Token registration. This is the live UAE lead.
- [ ] Confirm whether GoldZip has published any reserve attestation since 28 July 2026, and whether redemption windows have opened.
- [ ] Confirm the Brink's custody claim on rwa.xyz against a primary source. No issuer document names any custodian.
- [ ] Check whether XGZ's exclusion of Hong Kong residents is driven by SFC virtual-asset rules or by the HKGX parent's own licensing constraints, and whether any equivalent carve-out would apply to a UAE issuer selling into India/UAE/NRI markets.
