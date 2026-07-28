# Tether Gold (XAUT)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | XAU₮ / XAUT (base ERC-20); XAUt0 (omnichain wrapper) | **High** |
| Issuer (marketing) | "Tether Gold", presented under the Tether brand umbrella | **High** |
| Issuer (registry) | **TG Commodities, S.A. de C.V.**, an El Salvador *Sociedad Anónima de Capital Variable* | **High** |
| Domicile | **El Salvador**, relocated from the **British Virgin Islands in January 2025** | **High** |
| Prior domicile | British Virgin Islands (as "TG Commodities Limited") | **High** |
| Parent | Wholly owned by Tether Holdings, S.A. de C.V. and Tether Operations, S.A. de C.V. | **Medium** |
| Backing claim | 1 XAU₮ = 1 fine troy ounce of LBMA London Good Delivery gold, vaulted in Switzerland | **High** |
| Chains | Ethereum (canonical ERC-20), Tron (TRC-20), plus XAUt0 omnichain on TON, Solana, Avalanche, Polygon, Conflux, BNB Chain | **Medium** |
| Contract address (Ethereum) | `0x68749665ff8d2d112fa859aa293f07a622782f38` | **High** |
| Supply | 612,823 XAU₮ circulating / 707,747 XAU₮ total minted | **High** |
| Market cap | ~**US$2.465bn** (at ~US$4,021/oz, July 2026) | **High** |
| 24h volume | ~US$130.4m | **High** |
| Regulatory status | Registered stablecoin issuer, **CNAD El Salvador, register no. EME-0004** (19 May 2025); FinCEN MSB registrant | **High** |
| Subscription fee | 0.25% on direct purchase from issuer; minimum 50 XAU₮ | **Medium** |
| **Ongoing custody fee** | **Zero. No recurring storage or management fee is charged to holders.** | **High** |
| Redemption fee | 0.25%, plus logistics/insurance/handling; physical delivery in Switzerland only | **Medium** |
| Advertised yield | **None.** XAU₮ pays no yield, interest or dividend | **High** |
| Named officers | **Giancarlo Devasini, Sole Administrator** (signs the reserves report) | **High** |
| Reserve attestation | BDO Italia S.p.A., **ISAE 3000 (Revised) reasonable assurance**, quarterly | **High** |
| Custodian | **Not disclosed.** Referred to only as "the Custodian" | **High** |

---

## 1. What it is

Tether Gold is the largest tokenized gold product in existence, at roughly **US$2.46bn** market capitalisation and about **612,823 troy ounces** in circulation (approximately 19 tonnes of gold behind the circulating float). Each XAU₮ token represents one fine troy ounce of gold on a specific London Good Delivery bar held in a Swiss vault.

Its scale is the point for this exercise. XAU₮ is roughly **25 to 30 times the size of PGOLD** and orders of magnitude larger than ORO, yet its public documentation set is thinner in several important respects than protocols a fraction of its size. It publishes a genuinely strong quarterly reserves attestation and almost nothing else. There is no whitepaper of substance, no published bar list, no named custodian, and no wind-down plan. **Size and documentation quality are uncorrelated here, and XAU₮ is the proof.**

The commercial model is unusual and directly relevant to Aurumix: XAU₮ charges holders **nothing** to store their gold. There is no annual custody fee at all. This is the single most important commercial fact in this profile.

## 2. Legal structure

The reserves report is unusually explicit for a crypto issuer, and the language matters:

> "The physical gold bars held in the Gold Reserves meet the quality assurance requirements of 'London Good Delivery' set by the London Bullion Market Association. The Gold Reserves are vaulted in Switzerland. **The Gold Reserves are owned by the XAU₮ token holders, not by the Company.**"
> ([Reserves Report as of 30 June 2025](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_30.06.2025_RC187322025BD0179.pdf))

And:

> "Tether Gold (XAU₮) tokens are digital tokens that represent ownership of physical gold. **Holders of XAU₮ tokens have undivided ownership rights to gold on specified gold bars.** XAU₮s are created only following receipt of the corresponding gold by the Custodian."

This is a stronger ownership assertion than most tokenized gold products make. It claims a **direct undivided property interest in identified bars**, not a creditor claim against the issuer, and it positions the Company as a non-owner. The gold is stated to be held by the Custodian "as representative of the XAU₮ token holders". **Confidence: High** that this is the issuer's stated position, because it appears inside a document subject to reasonable assurance by BDO Italia.

Two important caveats, and they are material:

- **The assertion is not tested by the auditor as a legal conclusion.** BDO opines that the reserves report is "fairly presented in accordance with the criteria, including Management's Key Accounting Policies, set out therein". That is an accounting conclusion about quantities and valuation, not a legal opinion that title has effectively passed to token holders under Salvadoran or Swiss law. No trust deed, declaration of trust, bailment agreement or custody agreement is published. **Confidence: High** (this follows from the text of the opinion itself).
- **"Undivided ownership rights to gold on specified gold bars" is internally tense.** Undivided co-ownership of a pool and ownership of a *specified* bar are different legal constructs. With 611 bars of 12.5kg backing hundreds of thousands of tokens, holders plainly cannot each own a specified bar. Which construct governs on an insolvency is **Not disclosed**.

**What happens if TG Commodities fails is Not disclosed.** No published wind-down plan, no resolution procedure, no statement of how the Custodian would act, and no explanation of how a token holder would assert the claimed ownership right against a Swiss custodian without the issuer's cooperation. For an entity of this size this is a striking gap, and it matches the brief's observation that no gold token has published one.

## 3. Regulatory and compliance posture

**Verified against the register, and the widely repeated figure is wrong.**

The El Salvador CNAD public register lists:

| Register | Entity | Number | Date | Category |
|---|---|---|---|---|
| Issuers ([cnad.gob.sv/issuers](https://cnad.gob.sv/issuers/)) | **TG Commodities S.A. de C.V.** | **EME-0004** | 19/5/2025 | Issuer of Public Offerings of Stablecoins |
| Issuers | Tether International S.A. de C.V. | EME-0003 | 19/5/2025 | Issuer of Public Offerings of Stablecoins |

**Contradiction flagged.** Multiple secondary sources, and Tether's own Relevant Information Document as summarised in search results, state the registration number is **"PSAD-0032"**. Against the register, PSAD-0032 is a *Digital Asset Service Provider* number from a separate register (the PSAD register), and I could **not** locate TG Commodities in the PSAD list on the CNAD site. The number that verifies for the issuance activity is **EME-0004** on the issuer register. Both may be true simultaneously (El Salvador's LEAD requires an issuer to have a PSAD registered for placement and marketing), but anyone citing a single number for XAU₮ should cite **EME-0004** for the issuance and treat PSAD-0032 as unverified against the live register. **Confidence: High** on EME-0004, **Confidence: Low** on PSAD-0032.

Other regulatory facts, from the reserves report:

- Authorised as a **Stablecoin Issuer and Digital Assets Service Provider under the Digital Asset Issuance Law (LEAD) of El Salvador**, subject to the **National Commission of Digital Assets (CNAD)**.
- Registered as a **Money Services Business with FinCEN**, U.S. Department of the Treasury.
- Reports to the **Financial Investigation Unit of El Salvador**.

**The jurisdictional finding is the headline.** The largest tokenized gold product in the world is regulated by a stablecoin regime in **El Salvador**, a jurisdiction that created a bespoke digital-asset law to attract exactly this business, having moved there from the **British Virgin Islands in January 2025**. Note what it is *not*: it is not authorised by a securities regulator, not by a commodities regulator, and not by any major-market financial regulator. It is registered under a stablecoin law, and a gold token is being accommodated within a "stablecoin" category.

Also note it is **not** licensed by VARA, DFSA or ADGM despite marketing heavily into the Gulf (see §11 on the Shariah certification targeting the GCC). It reaches those markets through exchange listings and certification, not local licensing.

**No enforcement action against TG Commodities specific to XAU₮ was found.** Reputational risk is inherited from the Tether group rather than generated by the gold product.

## 4. Custody and proof of reserve

| Item | Status | Detail |
|---|---|---|
| Custodian | **Not disclosed** | Named only as "the Custodian" throughout every primary document. Secondary sources speculate Brink's/Loomis; **no primary source names it.** |
| Vault location | Switzerland | Country only. No city, no facility, no address. **Confidence: High** (stated in reserves report) |
| Allocated? | Yes, asserted | "undivided ownership rights to gold on specified gold bars"; bars are itemised by size and count |
| **Bar list** | **Not published** | Only an aggregate breakdown by bar size. No serial numbers, no refiner names, no per-bar assay data |
| PoR feed | Daily transparency page | gold.tether.to publishes daily, "updated at least once per day", with a stated lag between issuance and display |
| **Reserve attestation** | **Quarterly, BDO Italia S.p.A., ISAE 3000 (Revised) reasonable assurance** | This is genuinely strong. See below |
| Smart contract audit | Fragmentary | No first-party published audit located. **Confidence: Low** |

**The attestation deserves credit, and precision about what it does and does not say.**

The brief asks for a sharp distinction between a smart-contract audit and a reserve attestation. XAU₮ is a case where the reserve attestation is **better than the tokenized-gold norm**, and the smart-contract audit position is worse.

What the attestation actually attests to, from the [30 June 2025 BDO opinion](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_30.06.2025_RC187322025BD0179.pdf):

- It is a **reasonable assurance** engagement under **ISAE 3000 (Revised)**. Reasonable assurance is the higher of the two ISAE 3000 tiers, materially stronger than the limited-assurance or agreed-upon-procedures reports common in this sector. BDO states: "In our opinion, the TGRR ... is, in all material respects, fairly presented."
- Procedures included **physical inventory procedures** ("performing inventory procedures in order to confirm the existence of fine troy ounces"), reconciliation of the accounting ledger against "the ledgers on the various blockchains relating to liabilities", and **reports from a specialised provider on inventory and quality testing, on a sample basis**. Quarterly confirmatory assay testing of a **sample** of bars by a qualified independent third party is disclosed.

What it explicitly does **not** cover, and BDO says so directly:

- **"The reporting date is limited to a point in time as of 30 June 2025. We did not perform procedures or provide any assurance at any other date or time in this report."** A quarterly point-in-time snapshot says nothing about the other 89 days.
- **"The TGRR is prepared by Management for transparency purposes. As a result, the TGRR may not be suitable for another purpose."** It is not an audit of the company, not a financial statement audit, and not a legal opinion on title.
- Assay testing is **sample basis**, not every bar.
- It is not an opinion on solvency, on the adequacy of custody arrangements, or on the enforceability of holder ownership rights.

Net: **the reserve attestation is the strongest in the tokenized-gold set reviewed, and it is still only a quarterly point-in-time accounting opinion, from a firm whose Tether engagements have themselves drawn scrutiny.** The correct summary is "quarterly reasonable-assurance attestation with sampled assay testing, no bar list, unnamed custodian".

**The minted-versus-sold gap is a genuine subtlety.** As of 30 June 2025: 246,524.33 XAU₮ minted, of which **186,879.51 sold** and **59,644.82 "available for sale"**, held by **Alpha Group Commodities, S.A. de C.V.**, an affiliate that also relocated from the BVI to El Salvador in January 2025. As of 31 March 2026: **707,747.139 oz** in reserve against **559,598.64 XAU₮ sold**. So roughly **21% of minted supply is unsold affiliate inventory.** Anyone reading "market cap" off a supply figure is mixing customer-owned tokens with issuer-affiliate inventory. Circulating supply (612,823) and total supply (707,747) differ for this reason. **Confidence: High.**

## 5. Issuance

- Gold arrives first: "The Company issues XAU₮ tokens after physical gold bars containing a corresponding number of fine troy ounces of gold have completed the Custodian's intake procedure." Mint-after-delivery, not mint-then-fund. **Confidence: High.**
- **Minimum direct purchase: 50 XAU₮**, roughly US$200,000 at July 2026 prices. **Confidence: Medium.**
- Direct issuance is **full-KYC/AML gated**. **Confidence: Medium.**
- A pre-minted inventory held by affiliate Alpha Group Commodities allows direct customers to be filled from stock rather than triggering a fresh mint. **Confidence: High.**

**The practical consequence: XAU₮ has no retail primary market.** A 50-ounce minimum puts direct issuance out of reach of every retail saver. Retail buys XAU₮ on exchanges, in the secondary market, at whatever the market price is. The issuer's direct channel is wholesale-only in practice even if not in stated policy.

## 6. Redemption

- **Physical redemption minimum: approximately 430 XAU₮**, corresponding to one London Good Delivery bar (~US$1.73m at July 2026 prices). **Confidence: Medium**, from secondary sources; not confirmed against the issuer's own terms, which I could not retrieve (gold.tether.to is JavaScript-rendered and blocks direct fetching).
- **Redemption fee: 0.25%**, plus logistics, insurance and handling borne by the redeemer. **Confidence: Medium.**
- **Delivery is to a holder-nominated address in Switzerland.** Taking gold out of Switzerland is the holder's problem. **Confidence: Medium.**
- Full KYC/AML required. Sanctions and jurisdictional screening apply; the excluded-country list is **Not disclosed**.
- **Cash redemption from the issuer: Not disclosed.** No documented issuer-operated fiat redemption window was found. Cash exit is by selling on the secondary market.

**This is the gap between the ownership claim and the practical reality.** XAU₮ tells holders they have "undivided ownership rights to gold on specified gold bars", but exercising that right requires ~US$1.73m of tokens, a Swiss delivery address and a full KYC file. For any holder below one bar, the ownership right is economically theoretical: the only real exit is selling the token to someone else. The claim is legally stronger than most competitors and practically inaccessible to almost all holders, at the same time.

## 7. Fees and revenue model

| Fee line | Amount | Paid by | Confidence |
|---|---|---|---|
| Direct purchase / creation | 0.25% | Buyer | **Medium** |
| **Ongoing custody / storage** | **0.00%. None.** | n/a | **High** |
| Management fee | **None** | n/a | **High** |
| Redemption (to physical) | 0.25% + logistics, insurance, handling | Redeemer | **Medium** |
| Cash redemption from issuer | **Not disclosed** | n/a | n/a |
| On-chain transfer | Network gas only, no issuer-imposed transfer fee | Sender | **Medium** |
| Cross-chain (XAUt0) | Bridge/LayerZero costs, set by the bridge not the issuer | User | **Medium** |

**The zero-custody-fee model, and what actually funds it.**

XAU₮ charges holders nothing to store their gold, permanently. This is its central marketing differentiator against gold ETFs (which charge 0.15–0.40% per year) and against PAXG. The storage cost is real and someone pays it.

The disclosed fee lines (0.25% in, 0.25% out) cannot plausibly fund perpetual Swiss vaulting on their own for a long-duration holder. A holder who buys and holds for ten years pays 0.25% once and consumes ten years of allocated storage, insurance and quarterly assay testing. The arithmetic only works because of what is *not* in the fee table:

1. **Tether group cross-subsidy.** Tether Holdings earns very large returns on its USDT reserve portfolio. Vaulting ~19 tonnes of customer gold is a rounding error against that, and XAU₮ functions as a strategic product for the group rather than a standalone profit centre. **Confidence: Medium** (inferred from group structure; Tether does not publish XAU₮ segment economics).
2. **Float on unsold inventory.** ~21% of minted tokens sit as affiliate inventory. The group holds gold exposure on its own book alongside customer gold. Tether's total gold position has been reported at 140–162 tonnes, far exceeding the ~19 tonnes backing circulating XAU₮.
3. **Spread.** The issuer sells from inventory at a spread, which is not a disclosed "fee" but is a revenue line.

**Confidence: High** that no custody fee is charged. **Confidence: Medium** on the funding mechanism, which is inferred, not disclosed. **The issuer has never published a statement explaining what funds free perpetual storage.**

## 8. Token architecture

**Base token.** Standard **ERC-20** on Ethereum at `0x68749665ff8d2d112fa859aa293f07a622782f38`, six decimals, plus a **TRC-20** deployment on Tron. It is **not** a permissioned standard: it is a plain, freely transferable ERC-20. Anyone can hold it, anyone can send it to anyone, and the token carries no identity or eligibility logic.

**Admin controls.** Reporting is contested. Some analyses describe a transparent-proxy pattern with upgradeable logic and USDT-style freeze/blacklist powers held by Tether; automated audit tooling reports no blacklist or pause function present and does not classify it as a standard upgradeable proxy. **No address is known to have been frozen on the XAU₮ contract.** Tether has previously executed a contract upgrade/migration for XAU₮. Net: **Confidence: Low** on the precise admin surface. This is an open item, and notable in itself: for a US$2.5bn instrument, whether the issuer can freeze your gold token should not require inference.

**XAUt0, the omnichain layer, and why it matters.** In June 2025 Tether launched **XAUt0** via the **USDT0** infrastructure using **LayerZero's OFT (Omnichain Fungible Token)** standard, first on **TON**, then **Solana (Oct 2025)**, **Avalanche (Nov 2025)**, **Polygon**, **Stable**, **Conflux (Apr 2026)** and **BNB Chain (Mar 2026)**.

This creates a **two-tier claim structure that the documentation does not address**:

- XAU₮ on Ethereum is the canonical token carrying the stated undivided ownership right in Swiss gold.
- XAUt0 on seven-plus other chains is, under the standard OFT design, a **bridged representation** backed by canonical XAU₮ locked in a lockbox contract.

**Whether an XAUt0 holder on Solana or TON has the same legal claim on physical gold as an Ethereum XAU₮ holder is Not disclosed.** No published redemption path exists for XAUt0 without first bridging back to canonical XAU₮. Who controls the lockbox, and what happens to XAUt0 holders if the LayerZero bridge fails or is exploited, is **Not disclosed**. An XAUt0 holder is exposed to gold price risk, issuer risk, custodian risk **and** bridge risk, with the last of these entirely undocumented. Multi-chain reach was bought at the cost of claim clarity.

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Market cap | ~US$2.465bn |
| Circulating supply | 612,823 XAU₮ |
| Total supply | 707,747 XAU₮ |
| 24h volume | ~US$130.4m |
| Volume / market cap | **~5.3% daily turnover** |
| Price | ~US$4,021.73 (tracking gold) |
| Top venues | Binance XAUT/USDT ~US$12.5m; Gate ~US$11.7m; Bybit ~US$9.0m; OKX ~US$6.9m; XT.COM ~US$6.3m |

**This is the direct counter-example to the PGOLD data point in the brief, and it is important for Aurumix's premium thesis.**

PGOLD: ~US$79–90m AUM, ~US$1.7m liquidity, sub-US$20 daily volume. XAU₮: ~US$2.46bn AUM with ~US$130m daily volume, roughly **5.3% of market cap turning over every day** across five or more major venues each doing US$6m+.

So the brief's finding stands but needs refinement: **AUM does not produce liquidity, but scale plus tier-1 exchange listings does.** XAU₮ is genuinely liquid. It is also, precisely because it is liquid and arbitrageable against spot gold on major venues, **the protocol least likely to sustain a premium**. It trades at gold, not above it. Deep liquidity and a durable retail premium are opposed outcomes, not complementary ones.

Market share: XAU₮ has been reported at 54–60% of the entire gold-backed token market.

## 10. Distribution

- **Channels:** centralised exchange listings (Binance, OKX, Bybit, Gate, Bitfinex and many others), direct issuance for large tickets, and increasingly DeFi/collateral integrations.
- **Geography:** global via exchanges; explicit targeting of Indonesia (Mobee listing, July 2025) and, following the July 2026 Shariah certification, the **GCC, South Asia and parts of Africa**.
- **Savings plan / SIP / recurring purchase: None.** No systematic investment plan, no recurring contribution product, no fractional accumulation programme from the issuer.
- **Referral or affiliate programme: None found.** No agent network, no multi-tier commission structure, no distributor incentives.
- **Target segment:** effectively institutional, treasury and high-net-worth. A 50-ounce direct minimum and a 430-ounce redemption minimum define the customer.

**The finding here is stark and it is the brief's expectation confirmed at the top of the market.** The largest tokenized gold product on earth has **no retail distribution mechanism of its own**. It has no savings plan, no recurring purchase, no agent network and no referral programme. It acquires its US$2.46bn entirely through exchange listings, brand and institutional relationships. It is a wholesale product with a liquid secondary market, not a savings product.

## 11. Recent developments

- **27 July 2026:** XAU₮ receives **Shariah certification from Amanah Advisors**, led by **Mufti Faraz Adam**. The review covered "the token's ownership model, reserve transparency, physical backing, and compliance with Islamic rules governing gold transactions", confirming real ownership of physical gold, absence of riba, no leverage and no speculative derivatives. Tether explicitly targets the **GCC, South Asia and parts of Africa**. ([Tether](https://tether.io/news/xaut-tethers-gold-backed-digital-asset-receives-shariah-certification-unlocking-new-pathways-for-islamic-banks-institutions-and-individuals-worldwide/))
- **3 July 2026:** CoinGecko launches an RWA transparency tool featuring XAU₮'s peg to physical gold. **Confidence: Low.**
- **29 June 2026 (announced ~18 June 2026):** **Ledn partnership**: XAU₮ accepted as collateral for loans denominated in USDT and USAT, letting holders borrow against bullion without selling. Ledn states a **1:1 collateral policy with no rehypothecation**. **Not available in the EU or Canada.** ([Cryptobriefing](https://cryptobriefing.com/tether-ledn-tokenized-gold-xaut/))
- **April 2026:** XAUt0 launches on **Conflux**.
- **~31 March 2026 (Q1 2026 attestation):** Reserves reach **707,747.139 fine troy ounces**, value above **US$3.3bn**, a **36% quarter-on-quarter increase**; tokens sold 559,598.64 XAU₮. ([Tether](https://tether.io/news/tether-gold-surpasses-3-3-billion-as-reserves-surge-36-in-q1-driven-by-flight-to-hard-assets/))
- **26 March 2026:** XAU₮ listed on **BNB Chain** via the USDT0 infrastructure layer, described as unified liquidity across 12+ chains. ([Tether](https://tether.io/news/tether-gold-the-worlds-leading-tokenized-gold-product-to-be-listed-on-bnb-chain/))
- **26 January 2026:** Tether announces XAU₮ **surpasses US$4bn in value** and accounts for **more than half** of the gold-backed stablecoin market. (Note: this figure exceeds the ~US$2.46bn market cap observed in July 2026; the US$4bn likely reflects total minted supply at a peak gold price rather than circulating market cap. **Treat the US$4bn as a marketing figure.**)
- **26 December 2025:** Reuters reports Tether bought **~27 tonnes of gold in Q4 2025**, holding **~162 tonnes** across the group, of which only a minority backs circulating XAU₮.
- **24 November 2025:** XAUt0 deploys on **Avalanche**.
- **28 October 2025:** Attestation shows **375,572.297 fine troy ounces** against 375,572.247 XAU₮, ~US$2bn.
- **16 October 2025:** XAUt0 deploys on **Solana**.
- **21 July 2025:** XAU₮ listed on **Mobee** (Indonesia).
- **June 2025:** **XAUt0 launched on TON** via USDT0 and LayerZero OFT, the first omnichain deployment.
- **19 May 2025:** **TG Commodities registered with CNAD as issuer EME-0004.** ([CNAD](https://cnad.gob.sv/issuers/))
- **Q1 2025:** First public XAU₮ attestation released, >7.7 tonnes backing circulating tokens.
- **January 2025:** **TG Commodities, S.A. de C.V. and Alpha Group Commodities, S.A. de C.V. relocate from the British Virgin Islands to El Salvador.** The single most consequential structural event in the period.

**No depeg, incident, exploit, sustained discount or enforcement action specific to XAU₮ was found in the period.**

## 12. Relevance to Aurumix

**Q1. Custody fee mechanism. This is the most directly useful finding in the profile.**

XAU₮ takes the third option the brief identifies: **charge holders nothing and recover the cost elsewhere.** No custody fee, no management fee, no grams deducted, ever. It never faces Aurumix's peg-breakage problem because it never touches the gold to pay for storage.

The reason it can do this is a cross-subsidy Aurumix does not have. Free storage is funded by a group earning enormous returns on a separate US$100bn+ stablecoin reserve book, by spread on affiliate inventory, and by a group gold position (140–162 tonnes) many times larger than the ~19 tonnes backing circulating XAU₮. **Aurumix cannot copy the zero-fee model without a comparable external subsidy, and it should not assume one.**

But the strategic lesson transfers cleanly and it is worth stating plainly: **the market leader charges zero ongoing custody fee.** Any Aurumix custody fee is a competitive disadvantage against XAU₮ on a like-for-like basis, and must be justified by the savings-plan wrapper, the agent servicing and the credit facility rather than by the gold storage itself. If Aurumix charges in cash (the leaning in the brief), the messaging problem is that XAU₮ charges nothing. Aurumix's answer has to be that it is selling a savings programme with distribution and credit attached, not a cheaper vault.

**Q2. Dividend funding. XAU₮ pays nothing, and that is the cleanest available evidence for the securities argument.**

The largest, best-capitalised, most liquid tokenized gold product in the world, sitting inside a group with one of the largest profit pools in crypto, **pays its gold-token holders zero yield.** No dividend, no staking, no APY. Its Shariah certification explicitly rests on the **absence of interest-based mechanisms, leverage and speculative derivatives**.

Tether could trivially afford to pay a yield on 19 tonnes of gold. It does not. The most plausible reading is that paying holders a return on a passive asset converts a commodity token into something that looks like an investment contract, and the issuer has chosen not to take that risk even though it has the money. **This is the strongest external support in the set for the brief's concern about the ICS Dividend.** Aurumix should note that its two nearest reference points diverge completely: PGOLD promises 5% it cannot fund, XAU₮ promises nothing and is the market leader. Yield is not what wins this category.

Where XAU₮ *does* let holders monetise without selling is **credit, not dividend**: the Ledn partnership (June 2026) allows borrowing against XAU₮ collateral, explicitly with **no rehypothecation**. **This directly validates Aurumix's credit facility and Gold Card as the better-designed value-add than the dividend.** It provides holder utility, generates issuer revenue, does not encumber the gold, and does not create a securities-classification problem. Note also that Ledn excludes the EU and Canada, which is a useful precedent for jurisdictional gating of a credit product.

**Q3. Token standard. XAU₮ is a plain ERC-20, and its choice cost it nothing because it has nothing to protect.**

XAU₮ carries no tier standing, no dividend entitlement, no credit eligibility and no buyback right. It is a bearer claim on an ounce of gold. A plain ERC-20 is therefore exactly correct for it: maximum transferability, maximum exchange listability, maximum liquidity, no compliance logic needed at the token layer. Its US$130m daily volume is a direct product of that choice.

**This confirms rather than challenges Aurumix's ERC-3643 lean, and it also prices it.** XAU₮ demonstrates what permissionless buys: deep liquidity, universal listings, ~5.3% daily turnover. Aurumix's ICS, dividend, credit eligibility and buyback rights all break on an anonymous transfer, so it cannot have that. The tradeoff should be made with eyes open: **choosing ERC-3643 means accepting that Aurumix will never have XAU₮-like secondary liquidity, and therefore that the cash buyback is the only real exit.** That is coherent, but it means the buyback must be resourced properly, because there is no deep market to fall back on.

The XAUt0 experience is a second, subtler warning. Tether extended to seven-plus chains via a LayerZero wrapper and in doing so created a class of holders whose legal claim on the gold is undocumented. **If Aurumix ever wraps a permissioned base token into a transferable ERC-20 for liquidity, it will create exactly this problem: a wrapper holder who has the economic exposure but none of the ICS standing, dividend entitlement or credit eligibility.** Aurumix must decide in advance what a wrapped AURX holder actually owns, and write it down. XAU₮ did not, and at US$2.5bn it still has not.

**Q4. Regulatory route. A large, sophisticated issuer chose a bespoke small-jurisdiction regime over a major-market licence.**

TG Commodities moved from the BVI to El Salvador in January 2025 and registered under the LEAD as **CNAD issuer EME-0004**. It is licensed by a purpose-built digital-asset regulator in a small jurisdiction, not by a securities or commodities regulator, and **not by VARA, DFSA or ADGM**, despite now actively marketing into the GCC.

This is directly instructive for Aurumix's cost/benefit on VARA. The market leader concluded that a light-touch bespoke regime plus global exchange distribution beat an expensive major-market licence. **However, the analogy has a hard limit that Aurumix must not gloss over:** XAU₮ is a pure custody receipt with no yield, no credit and no retail savings plan, so it fits a "stablecoin issuer" box cleanly. Aurumix's hybrid (dividend + credit + SIP + agent network) does not fit any single box anywhere, which is precisely why its regulatory problem is harder than XAU₮'s despite being 1/100th the size. XAU₮'s route is available to Aurumix only if Aurumix strips back to the gold core.

Also note the **Shariah certification (July 2026)** as a distribution instrument rather than a licence. Tether reached the GCC and South Asia through certification plus exchange listings, without local licensing. **For a product targeting India, the UAE and NRIs, Shariah certification is a cheap, fast, high-leverage credential that Aurumix should price into its plan.** Amanah Advisors and Mufti Faraz Adam are a named, checkable precedent. Aurumix's gold core should certify easily; its **ICS Dividend and its 90–95% LTV credit facility are the parts that will attract scrutiny**, since riba and leverage are exactly what the XAU₮ certification confirmed were absent. That is a second, independent reason to be cautious about the dividend.

**Q5. Redemption. XAU₮ has physical redemption on paper and effectively none in practice.**

A ~430 XAU₮ minimum (~US$1.73m), Swiss-only delivery, full KYC, 0.25% plus logistics. Aurumix should take real comfort here: **the market leader's redemption right is inaccessible to essentially every retail holder.** The gap between "you own physical gold" and "you can get it" is not unique to Aurumix, it is the industry norm.

The honest differentiator is disclosure, not the right itself. XAU₮ asserts strong ownership language while gating redemption at 1.73 million dollars. **Aurumix saying plainly "no physical redemption, cash buyback only" is more transparent than XAU₮'s position, and Aurumix should say so rather than treating it as a weakness to hide.** The brief already identifies this as a gap; the XAU₮ evidence suggests it is better framed as candour.

**Q6. Premium and liquidity. XAU₮ is the strongest evidence yet against the 3–8% premium thesis.**

XAU₮ has ~US$2.46bn AUM and ~US$130m daily volume, ~5.3% turnover, across five-plus venues each doing US$6m+. It is arbitraged continuously against spot gold and **trades at gold, not above it.**

This sharpens the brief's PGOLD finding into a general rule: **liquidity and premium are inversely related.** PGOLD has no liquidity and no reliable premium. XAU₮ has excellent liquidity and no premium, because arbitrage kills it. **A durable 3–8% premium cannot survive a liquid market.** If Aurumix's premium thesis depends on AURX trading above NAV, that premium can only exist in a market too thin or too closed to arbitrage, which is in tension with any liquidity ambition and makes the premium fragile and hard to defend to a regulator. **Aurumix should stress-test the revenue model with the premium set to zero.** The permissioned/ERC-3643 route, by limiting free transfer, is arguably the only structure in which a controlled premium is sustainable at all, and if so that should be stated as a deliberate design choice rather than a side effect.

**Q7. Proof of reserve. XAU₮ sets the benchmark Aurumix should aim at, and it is achievable.**

Quarterly **ISAE 3000 (Revised) reasonable assurance** by a Big Four-adjacent firm (BDO Italia), including physical inventory procedures, sampled third-party assay testing, and reconciliation of the ledger against on-chain liabilities, plus a daily transparency page. That is meaningfully better than the tokenized-gold norm and it is the standard a serious UAE retail product should match.

The remaining gaps tell Aurumix where cheap differentiation is: **no published bar list, no named custodian, sampled rather than full assay, point-in-time quarterly snapshots.** **Naming its custodian and publishing a bar list would put Aurumix ahead of a US$2.5bn incumbent on transparency at near-zero cost.**

Also carry forward the sharp distinction the brief asks for: XAU₮'s reserve attestation is strong, its **smart-contract audit position is weak and largely unverifiable**. The two are not the same thing and XAU₮ is a good example of an issuer being much better at one than the other. Aurumix should publish both, separately labelled.

**Q8. Distribution. This is where Aurumix's actual moat is, and XAU₮ proves it.**

XAU₮ has **no savings plan, no recurring purchase, no referral programme, no agent network** and a US$200,000 direct minimum. It is a wholesale product. **The largest tokenized gold product in the world does not compete with Aurumix for the retail monthly saver at all.** It is not a distribution competitor; it is a liquidity venue and a benchmark.

The strategic read: XAU₮ owns institutional and treasury demand and will keep owning it. The US$20-a-month Indian or NRI saver is a market it has made no attempt to serve. **Aurumix's SIP and 3-tier agent network are not a weaker version of XAU₮'s model, they are a different business.** The correct competitive posture is not to out-vault XAU₮ but to out-distribute it, and to be honest internally that Aurumix's product risk is a distribution and compliance risk (agent network, commissions, mis-selling, KYC at scale), not a gold-custody risk.

Note also the Shariah certification targeting **"GCC, South Asia and parts of Africa"**: XAU₮ is now aiming marketing at Aurumix's exact geographies, even though its product cannot serve a retail saver. Aurumix should expect XAU₮ brand presence in its markets without direct product competition.

**Q9. Wind-down. XAU₮ has none, at US$2.5bn.**

No published wind-down plan, no resolution procedure, no statement of what happens to the gold or how holders would assert their claimed ownership rights against an unnamed Swiss custodian if TG Commodities failed. This confirms the brief's finding at the very top of the market.

**Aurumix committing to a published wind-down plan would differentiate it against the US$2.5bn category leader, not just against failed micro-caps.** That reframes the cheap-differentiation argument considerably: it is not a courtesy to a sceptical retail buyer, it is a gap that literally nobody in the category has filled.

### Contradictions and corrections to the brief

1. **The brief's PGOLD-derived premium/liquidity finding needs refining, not overturning.** "AUM does not imply liquidity" is right, but XAU₮ shows that scale plus tier-1 listings does produce real liquidity (~5.3% daily turnover), and that this liquidity **eliminates** the premium. The sharper statement is that **premium and liquidity are inversely related**, which is a more useful and more uncomfortable finding for Aurumix's revenue model than the PGOLD case alone.
2. **The task brief describes the issuer as "TG Commodities Limited or successor".** The current issuer is **TG Commodities, S.A. de C.V.**, an El Salvador entity, following relocation from the **British Virgin Islands in January 2025**. "TG Commodities Limited" is the superseded BVI name and should not be used for anything current. This is the same class of jurisdiction error the brief warns about with ORO, and it collapsed against the register in the same way.
3. **The widely cited registration number "PSAD-0032" does not verify against the CNAD register for issuance.** The verified issuer entry is **EME-0004**, dated 19 May 2025. Cite EME-0004.
4. **"MODERATE documentation" is the right grade but for a counterintuitive reason.** XAU₮'s *reserve attestation* is the best in the set (ISAE 3000 reasonable assurance, quarterly, with physical inventory and sampled assay). Its *legal and structural* documentation is among the weakest: no retrievable public terms of service, no named custodian, no bar list, no wind-down plan, no clear XAUt0 claim structure, and an admin-key surface that cannot be established from public sources. **It is excellent at proving the gold exists and poor at explaining what you own and what happens if things go wrong.** A protocol 250x smaller documenting itself better is not a paradox: scale removes the pressure to explain yourself, because liquidity and brand substitute for disclosure. Aurumix, without that brand, has to explain itself.

## 13. Open items for verification

- [ ] Retrieve the actual **Tether Gold Terms of Sale / Terms of Service** from `https://gold.tether.to/legal` (JS-rendered; use a headless browser or archive snapshot). Confirm the 430 XAU₮ redemption minimum, the 0.25% fees and the 50 XAU₮ purchase minimum against the issuer's own terms rather than secondary sources.
- [ ] Confirm whether the Terms contain **any insolvency, wind-down or resolution clause**, and how holder ownership rights would be asserted against the custodian if TG Commodities failed.
- [ ] Retrieve the full **Relevant Information Document** PDF (`https://gold.tether.to/Relevant Information Document - TG Commodities, S.A. de C.V..pdf`) and extract the exact registration number(s) it cites, to resolve the **EME-0004 vs PSAD-0032** discrepancy.
- [ ] Search the **CNAD PSAD register** page by page for TG Commodities to confirm or eliminate PSAD-0032.
- [ ] Determine the **actual admin surface of the Ethereum XAU₮ contract**: read the verified source directly for blacklist/freeze/pause functions, proxy pattern and the owner address. Resolve the conflict between the automated audits and the secondary reporting.
- [ ] Identify **who controls the XAUt0 lockbox** and whether any published document states that an XAUt0 holder has the same claim on physical gold as a canonical XAU₮ holder.
- [ ] Establish whether the **physical gold custodian** is named in any filing, insurance certificate or Salvadoran regulatory submission. Test the Brink's/Loomis attribution, which currently rests only on secondary sources.
- [ ] Confirm the **cash redemption** position: does TG Commodities operate a fiat redemption window at all, or is the secondary market the only cash exit?
- [ ] Obtain the **Q2 2026 attestation** (expected ~July 2026) to confirm current tonnage and the minted-versus-sold gap.
- [ ] Reconcile the **January 2026 "US$4bn" claim** against the ~US$2.46bn July 2026 market cap. Determine whether the difference is gold price movement, total-versus-circulating supply, or marketing.
- [ ] Obtain the **Amanah Advisors Shariah certificate** itself and check the reasoning on gold ownership and constructive possession (*qabd*), which will be directly reusable for Aurumix's own certification, and note what it says about leverage that may bear on Aurumix's credit facility.
- [ ] Locate any **first-party smart-contract audit** commissioned by Tether for XAU₮, to confirm whether one exists at all.
