# AZ Gold Reserve (AZG)

> **Scope warning, read first.** AZG is listed on rwa.xyz under "Commodities" next to PAXG and XAUT, and at ~$66M it screens as a mid-sized tokenized gold product. It is not one. By the issuer's own live API, **62% of AZG's "gold reserve" is gold still in the ground**, not bullion in a vault. AZG is a mining-finance instrument wearing a tokenized-gold label. The single most useful thing in this profile is the arithmetic in §4 and §5, and the fact that rwa.xyz's own classification and metadata are wrong in at least three verifiable respects. This is a **THIN** profile by design: much of what a reader wants does not exist, and the absence is the finding.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | AZG (on-chain name "AZ Gold"). Sister token AZS ("AZ Silver") | High (on-chain) |
| Issuer (marketing) | Arizore / "AZ Reserves". rwa.xyz names **"AZ Reserves Ltd"**, a name that appears in no register and on no Arizore page | Low |
| Issuer (registry) | **Not verified in any register.** Arizore's own terms say "Arizore LTD is a corporation established under the laws of Nevis". No registration number, no incorporation date, no register entry obtainable | **Not disclosed** |
| Domicile | Nevis (St Kitts and Nevis) per issuer's own terms. Nevis has no free public company search, so this is an unverifiable self-assertion, not a confirmed fact | Medium (assertion only) |
| Backing claim | "Tokenised gold reserve... including bullion, **in-ground reserves and tailings**" (rwa.xyz). Live API: **62.0% in-ground, 0% tailings, 38.0% bullion** | High (issuer API) |
| Chains | Ethereum mainnet | High (on-chain) |
| Contract address | AZG `0x45334126815c77be657c7906bf52c0f441a8831c`; AZS `0xee7eddf7793c1399407ba0b858852f64830f37a6` | High (on-chain) |
| Supply | **16,167.34 AZG** (18 decimals) | High (on-chain, 28 Jul 2026) |
| Market cap / TVL | Issuer API: **$64,993,677**. rwa.xyz: $66,171,313 | High (as reported) |
| Holders | **21** | High (Blockscout) |
| Lifetime transfers | **61**, all between 11 Mar 2026 and 10 Jul 2026 | High (Blockscout) |
| On-chain liquidity | **Zero.** No DEX pool, no exchange listing, no quoted market | High (negative search) |
| Regulatory status | **No licence found anywhere.** Not on ASIC, FCA, MAS, SFC, SEC or any register checked. Terms concede tokens "may be characterized as security tokens" | High (negative search) |
| Subscription fee | Minimum investment 100,000 USDT (rwa.xyz). Not stated in any issuer document | Low |
| Ongoing custody fee | 1.00% management fee (rwa.xyz only). Not stated in any issuer document | Low |
| Redemption fee | rwa.xyz claims 0.50%, "instant", 5,000 USDT minimum. **Issuer terms flatly contradict this**: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways" | High (contradiction) |
| Advertised yield | Not to token holders. **Up to 15.00% annual yield in USDT to mining participants**, behind a password gate | High (issuer page) |
| Named officers | **One person only: George Boot, Chief Marketing Officer.** No CEO, no directors, no beneficial owners disclosed anywhere | High |
| Auditor | rwa.xyz names **KPMG**. No KPMG engagement, report or reference exists on any Arizore page or in any public source | Low / unverified |
| Custodian | rwa.xyz names **"Gold Corporation" (LEI 213800HQZYBMURES6D84)**, i.e. the Perth Mint. **No corroboration anywhere.** See §4 | Low / unverified |

---

## 1. What it is

AZG is an ERC-20 token on Ethereum issued under the "AZ Reserve" framework operated by the Arizore brand. rwa.xyz classifies it as tokenized gold, describing it as "a tokenised gold reserve asset designed to provide digital access to verified gold resources, including bullion, in-ground reserves and tailings" ([rwa.xyz/assets/AZG](https://app.rwa.xyz/assets/AZG)).

That description is the tell, and it is accurate. AZG is not a claim on vaulted metal. It is a claim on a **pooled "reserve" whose majority component is unmined mineral resource**. Arizore's own live reserve API returns, as at 28 July 2026:

```
totalGoldReservesOz:  21,050
azgComposition:       inGround 62.00% | tailings 0% | bullion 38.00%
totalAZGTokensInCirculation: 16,167.34
azgCurrentTokenValue: 4,020.06
azgReserveValue:      64,993,676.84
lastUpdatedIso:       null
```
([arizore-reserve-backend.vercel.app/api/azg-reserve](https://arizore-reserve-backend.vercel.app/api/azg-reserve))

Arizore describes AZG on its own site not as gold but as a "**Gold-linked reserve participation instrument**. Supports interaction with the gold reserve framework." That phrasing is doing a lot of work, and it is materially more honest than the rwa.xyz listing.

The business model is mining finance, not savings. Arizore onboards mining projects and bullion providers; miners **pledge in-ground resources or tailings via forward contracts**, valued after "haircuts... from 25% to 55%, depending on the region and resource type", and receive capital. AZG is the instrument that carries that pooled reserve to investors. In Arizore's own words the purpose is "turning verified reserves into usable collateral" and letting miners "access liquidity without surrendering ownership."

**This is the opposite of Aurumix's product.** Aurumix promises that 100% of every dollar buys physical LBMA gold. AZG promises exposure to a reserve that is mostly not yet gold.

---

## 2. Legal structure

**What does a holder actually own? On the published record: nothing that is defined.**

This is not rhetorical. There is **no whitepaper, no offering memorandum, no terms of issue, and no token documentation of any kind** for AZG. The only legal documents Arizore publishes are a website Terms of Service and a Privacy Policy, both dated 27 November 2025, and both are site-usage documents rather than instrument terms.

The Terms of Service contain the entire published legal description of the token, in a section headed "Token Disclosures":

> "Arizore's ecosystem includes asset-backed digital tokens associated with verified reserves of in-ground resources, tailings, or vaulted bullion. **These tokens may be characterized as security tokens under various regulatory frameworks.**"

and, critically:

> "**The existence of a token does not imply rights beyond those expressly documented and contractually provided.**"

Read those together. The token is "associated with" a reserve. The word used is association, not ownership, title, trust or claim. And the rights are whatever a separate, unpublished contract says: "Any tokens issued as part of a pathway reflect audited and verified reserve structures and **are subject to separate agreements**."

So the holder's actual entitlement lives in bilateral agreements that are not public. A reader cannot determine whether AZG is a title claim, a trust beneficiary interest, an unsecured creditor claim, or a purely contractual exposure. **Not disclosed**, and the gap is total.

The issuing entity is named as **Arizore LTD**, "a corporation established under the laws of Nevis", registered address The Provident House, Central Government Road, Charlestown, Nevis, W.I., legal contact `admin@azreserves.com`. Governing law and exclusive jurisdiction are Nevis.

Note the naming inconsistency, which matters for anyone trying to serve process: the terms say **Arizore LTD**; the contact domain is **azreserves.com**; rwa.xyz names the issuer **AZ Reserves Ltd**; the Bocana filings say **Arizore Ltd.**; and the Nevada JV vehicle is **Arizore LLC**. These are at least three different legal persons and the published materials do not say which one issues AZG.

### Registry verification: attempted, and it failed

Per the brief's registry-first rule, this was checked before anything else:

- **Nevis FSRC corporate registry** (`registry.fsrc.kn`): unreachable, connection refused on both HTTP and HTTPS. The Nevis FSRC states that records may be examined only by a person "who has paid the prescribed fee... during normal hours" ([nevisfsrc.com/faqs](https://www.nevisfsrc.com/faqs/)). **There is no free public search of the Nevis register.** This is a deliberate feature of the jurisdiction, not an accident.
- **UK Companies House**: "No results" for both "Arizore" and "AZ Reserves" ([find-and-update.company-information.service.gov.uk](https://find-and-update.company-information.service.gov.uk/)).
- **Nevada Secretary of State** (for Arizore LLC): entity search sits behind an Imperva/Incapsula bot wall; no programmatic verification possible.
- ASIC, ACRA (Singapore), HK Companies Registry, BVI: no entries found for any Arizore or AZ Reserves name.

**Conclusion, stated plainly: the jurisdiction claim cannot be verified against a register.** Unlike ORO (where a Singapore UEN collapsed the Dubai story in one minute) or Comtech (where DAFZA licence 05069 was retrievable), Nevis is a jurisdiction chosen precisely so that this check cannot be performed by a member of the public. **That choice is itself the finding.** An issuer that wanted to be verified would not incorporate where verification is impossible.

The **one** genuinely register-adjacent corroboration is indirect, and it is worth more than everything on Arizore's own website: Arizore Ltd is named in the continuous-disclosure filings of a Canadian reporting issuer. See §11.

---

## 3. Regulatory and compliance posture

**No licence, registration or authorisation was found in any jurisdiction.** Checked and not found:

- ASIC (Australia): no AFSL for Arizore Ltd, AZ Reserves Ltd, Arizore LLC, Black Tie Holdings or Black Tie Digital. This matters because rwa.xyz asserts AZG sits under an "Australian Financial Services License" via ASIC. **No such licence was located on the ASIC registers.** Treat the rwa.xyz regulatory field as unsubstantiated.
- FCA (UK), MAS (Singapore), SFC (Hong Kong), SEC and CFTC (US), BVI FSC: no registrations, no filings, no exemption notices naming AZG, AZS, Arizore or AZ Reserves.
- No prospectus, offering memorandum, or private-placement exemption filing found anywhere.

Equally, and this should be recorded fairly: **no regulator has issued a warning, alert or enforcement action naming any of these entities.** They are absent from ASIC's and the FCA's warning lists. The posture is not "sanctioned"; it is **entirely outside the regulatory perimeter in both directions**.

The compliance position the issuer itself takes is the striking part. Arizore's terms **concede the securities characterisation rather than denying it**: tokens "may be characterized as security tokens under various regulatory frameworks." Most unlicensed issuers argue strenuously that their token is not a security. Arizore accepts it might be, publishes no prospectus, and manages the exposure by restricting distribution instead: the press release states AZG and AZS "are not investment products, are not yield bearing, and are **not intended for retail distribution or public trading**", and portal access is granted "exclusively to individuals and entities that have completed a meet-and-greet call or preliminary verification phase."

That is a coherent, if aggressive, private-placement-by-obscurity strategy. It also means **AZG is not a retail product and is not a competitor to Aurumix in any market sense.**

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | rwa.xyz names "Gold Corporation" (LEI 213800HQZYBMURES6D84). **Arizore names no custodian anywhere.** Terms refer only to generic "Vaulting and bullion partners" | Low / contradicted |
| Vault / city | **Not disclosed** | Not disclosed |
| Allocated? | **Not disclosed.** Terms say bullion providers "relinquish ownership of the bullion" on transfer into the reserve, implying the reserve is pooled and unallocated to holders | Medium |
| Bar list | **Not disclosed.** No bar list, no serial numbers, no assay certificates published | Not disclosed |
| PoR feed | A JSON endpoint returning six numbers. **`lastUpdatedIso` is `null`.** No cryptographic proof, no third-party signature, no on-chain oracle | High |
| Reserve attestation | **None found.** No attestation, no auditor's report, no engagement letter | Not disclosed |
| Smart contract audit | **None found. Contract source is not even verified on-chain** | High |

### The Perth Mint custody claim: unsupported and implausible

rwa.xyz's custodian field carries an LEI. Resolving it against GLEIF gives an unambiguous answer:

> LEI `213800HQZYBMURES6D84` = **GOLD CORPORATION**, trading name **THE PERTH MINT REFINERY**, 310 Hay Street, East Perth, WA 6004, Australia. Category: **RESIDENT_GOVERNMENT_ENTITY**, legal form "STATE GOVERNMENT ENTITY", registered as ABN 98 838 298 431. Status ACTIVE ([GLEIF API](https://api.gleif.org/api/v1/lei-records/213800HQZYBMURES6D84)).

So rwa.xyz is asserting that a Western Australian state-owned mint custodies the reserve behind an unlicensed Nevis token. **No corroboration exists.** The Perth Mint has made no statement, announcement or annual-report disclosure naming Arizore, AZ Reserves, AZG or AZS. Arizore's own website never mentions the Perth Mint, Gold Corporation, or Australia.

This claim should be treated as **false until the issuer produces a custody agreement**, for a reason the wave-1 research already established: the Perth Mint is the entity behind **PMGT**, and it exited tokenization through commercial abandonment. A state-government entity that wound down its own gold token is a deeply improbable custodian for an unregistered Nevis instrument. Note also the Australian thread that makes the claim superficially plausible: Black Tie Digital is Australian-based, and the Arizore launch release is datelined **Sydney**. A plausible explanation is that an Australian connection got laundered into a Perth Mint custody attribution somewhere in the data pipeline.

**Flag for the assembled document: rwa.xyz metadata for AZG is unreliable on issuer name, auditor, custodian and regulatory status.** Given wave 1 already found rwa.xyz naming a non-existent "Gold Issuance Inc." as ORO's issuer, this is now a **pattern**, not a one-off. rwa.xyz should not be treated as a primary source for issuer facts in this landscape.

### Audit versus attestation

Per the brief's standing instruction, separating the two: **neither exists.** rwa.xyz names KPMG as auditor. No KPMG report, engagement or reference appears on any Arizore page or in any public source. Arizore's terms use the word "audited" once ("tokens issued as part of a pathway reflect audited and verified reserve structures") without naming an auditor, a standard, or a date. And the smart contract is **not source-verified on Etherscan or Blockscout**, so there is no contract audit either. The word "audited" here is unbacked in both senses simultaneously.

What replaces verification is **geological reporting**: the Bocana JV release commits to "technical reports and studies compliant with **NI 43-101**". NI 43-101 is a genuine and rigorous Canadian standard, but it certifies *mineral resource estimates*, not vaulted bullion. Using it as the verification backbone for a product sold as "tokenised gold" is a category substitution, and it is the substitution the whole structure rests on.

---

## 5. Issuance

Issuance is by invitation and the mechanics are not published. Access requires "a meet-and-greet call or preliminary verification phase"; Arizore "retains full discretion to refuse, delay, or terminate onboarding for any reason." rwa.xyz states a **100,000 USDT minimum**, which is not confirmed by any issuer document but is consistent with the private-placement posture.

Two supply routes are described in the terms:

1. **Mining projects** pledge in-ground resources or tailings under **forward contracts**, subject to geological assessment, with valuation haircuts of **25–55%** and conservative LTV ratios, and undertake "delivery of refined bullion upon satisfaction of contract terms."
2. **Bullion providers** "sell vaulted bullion into the AZ Reserve through verified transfer pathways. Upon transfer, bullion providers relinquish ownership of the bullion."

### The backing arithmetic, which is the core finding

Using the issuer's own API figures against spot gold of **$4,019.80/oz** on 28 July 2026 ([gold-api.com](https://api.gold-api.com/price/XAU)):

| Measure | Value |
|---|---|
| AZG token value (issuer) | $4,020.06 |
| Spot gold, same day | $4,019.80 |
| **Ratio** | **1.0001, i.e. one token is priced as exactly one ounce of gold** |
| Stated reserve | 21,050 oz across 16,167.34 tokens = 1.3020 oz "backing" per token |
| Implied value of reserve per stated ounce | $64,993,677 ÷ 21,050 = **$3,087.59/oz, i.e. 76.8% of spot** |
| **Bullion component only** | 38.0% × 21,050 = **8,000 oz**, worth **$32.16M** |
| **Actual bullion per token** | **0.4948 oz = $1,989 = 49.5% of the token's own stated price** |

Three things follow, and they are arithmetic rather than opinion.

**First, the token is priced at one ounce of gold while holding roughly half an ounce of gold.** The other half is a discounted claim on ore that has not been mined, by a counterparty that is not named, under a forward contract that is not published.

**Second, the 76.8%-of-spot implied reserve value is the haircut showing through.** The structure is internally consistent (tokens × token value = stated reserve value, to the cent), which tells you the "reserve value" is a *derived* figure, not an independently measured one. Reserve value is computed from the token price, not the other way around. **The published "proof of reserve" is a restatement of the issuer's own valuation assumptions.**

**Third, and most important for a gold-savings comparison: AZG's holder carries mining execution risk, and Aurumix's holder must not.** If a pledged deposit is not mined, or is mined at higher cost, or the miner defaults, the in-ground 62% does not become gold. There is no disclosed remedy, no insurance, no over-collateralisation beyond the haircut, and no statement of where a token holder ranks against the miner or against Arizore's other creditors.

The composition figures are stable across repeated API calls and `lastUpdatedIso` is `null`, meaning the "live" reserve feed carries **no timestamp of its own**. A reserve feed that cannot say when it was last updated is not a proof of reserve.

---

## 6. Redemption

**There is no redemption right, and the two published sources directly contradict each other.**

rwa.xyz states redemption is "**Instant**", with a 5,000 USDT minimum and a 0.50% fee. The issuer's own Terms of Service state the opposite:

> "Arizore does not guarantee liquidity, market access, **convertibility, or redemption pathways**."

Where marketing and legal documents disagree, the brief says show both. Here the "marketing" is a third-party data aggregator and the legal document is the issuer's own binding terms, so the terms govern: **there is no committed redemption at all**, in metal or in cash. There is no minimum increment, no eligibility rule, no settlement window, and no fee schedule, because there is no redemption obligation to attach them to.

Note this is a *harder* position than Aurumix's. Aurumix has no physical redemption but does commit to a cash buyback. AZG commits to neither. The word "redemption" appears exactly once in Arizore's entire published corpus, and it appears in a sentence disclaiming it.

---

## 7. Fees and revenue model

| Fee line | Stated by issuer | Stated by rwa.xyz |
|---|---|---|
| Subscription / mint | Not disclosed | Minimum investment 100,000 USDT |
| Ongoing management / custody | Not disclosed | 1.00% per annum |
| Redemption | Not disclosed (redemption itself disclaimed) | 0.50%, 5,000 USDT minimum |
| Miner-side fee | Implicit in the **25–55% valuation haircut** and the LTV spread | n/a |

**Arizore publishes no fee schedule of any kind.** Every fee figure above comes from rwa.xyz, whose metadata for this asset is demonstrably wrong on other fields, so all three should be treated as unverified.

The economically real revenue line is not a token fee at all. It is the **haircut**: Arizore takes in-ground resource at 45–75% of assessed value and issues against it at spot-linked pricing. That spread, plus the interest on "up to USD $60,000,000 in secured funding loans" to the Bocana JV (§11), is the business. **AZG holders are the funding source for a mining-finance book.**

Per the wave-1 addendum, question 1 is settled and is not re-argued: AZG's ongoing custody fee to holders is **not disclosed**, and if the 1.00% figure is real it is an outlier against a field (PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, PGOLD) that uniformly charges holders nothing.

---

## 8. Token architecture

Verified directly against Ethereum mainnet on 28 July 2026:

| Property | AZG | AZS |
|---|---|---|
| Address | `0x45334126815c77be657c7906bf52c0f441a8831c` | `0xee7eddf7793c1399407ba0b858852f64830f37a6` |
| Name / symbol | AZ Gold / AZG | AZ Silver / AZS |
| Standard | ERC-20, 18 decimals | ERC-20, 18 decimals |
| Total supply | 16,167.341725201783541025 | 130,420.61 |
| Holders | **21** | **5** |
| Lifetime transfers | **61** | **6** |
| Proxy type | **EIP-1967 beacon proxy** (upgradeable) | **EIP-1967 beacon proxy** (upgradeable) |
| Implementation | `0x0c7f3724A477B13a73BF931B3cE2ee7148DFBd44` | not resolved |
| Source verified? | **No** | **No** |
| `owner()` | `0x664e6443786ded0bf91de57143200356d7ef6be0` (EOA, 8 lifetime txs, holds 0 AZG) | `0x0fD369b78E604400d2172615A7bDeeb6D27eBf90` |
| `paused()` | `false` (so the contract **is** pausable) | `false` |
| Contract created | **10 July 2026**, tx `0xdf679627...`, creator `0xF2d5748Df14E3112ae693d4C9778809127D48Ed4` | 2026 |

Four things matter here.

**It is a plain permissionless ERC-20, not ERC-3643.** For an instrument the issuer concedes "may be characterized as security tokens", not intended "for retail distribution or public trading", there is **no on-chain transfer restriction, no whitelist, and no identity gating**. Compliance is enforced entirely off-chain at onboarding. Anyone holding AZG can send it to anyone. This is the exact failure mode the brief's question 3 is about, and AZG is the cautionary case: **the legal restriction and the technical capability do not match.**

**It is upgradeable via a beacon proxy, and the source is unverified.** Both together are severe. The beacon owner can swap the implementation for every token at once, and because the source is not published, a holder cannot read what the current implementation does, let alone what a future one might. There is a `paused()` function, so transfers can be frozen. Admin-key custody is a single EOA with 8 lifetime transactions and no multisig evidence.

**The contract was deployed on 10 July 2026, eighteen days ago**, and it is *not* the contract that was minted in February 2026. Arizore's own February release said "all tokens have been minted, issued, and confirmed on-chain." The current AZG contract post-dates that by five months. So there has been an undisclosed redeployment or migration, and the 61 transfers recorded against this address run from 11 March 2026, i.e. **earlier than the contract's own creation date**, which means the Blockscout history is being served through the beacon/proxy lineage rather than a single clean deployment. Either way, **the on-chain history does not reconcile with the issuer's public statements**, and no migration was ever announced.

**No bridge, no second chain.** Ethereum only.

---

## 9. Liquidity and market

Reported as one data point per the wave-1 instruction; the premium thesis is settled and is not re-argued.

AZG has **~$65–66M of stated AUM and literally zero market**. There is no DEX pool, no CEX listing, no order book, no quoted bid, and no price discovery. The "price" of $4,020.06 is a number the issuer computes and serves from its own API; it is not a market price and no one has traded at it. Lifetime on-chain activity is **61 transfers among 21 holders**, all between 11 March and 10 July 2026, with the largest holder at 6,177 AZG (38.2% of supply) and the top two at **76.9%**.

Against the settled conclusion, AZG is the terminal case of the illiquid end: PGOLD had ~$79–90M AUM on sub-$20 daily volume; ORO had 33% liquidity-to-AUM and traded at a discount; **AZG has a liquidity-to-AUM ratio of exactly zero**. It cannot express a premium or a discount because it has no market at all. Its price is definitionally at "spot" because the issuer sets it to spot.

For Aurumix this is a clean negative data point: **AUM without a market is not evidence of anything.** A $66M headline figure on rwa.xyz sits alongside 21 holders and 61 lifetime transactions.

---

## 10. Distribution

**No savings plan, no recurring purchase, no referral programme, no affiliate network, no agent tier, and no retail channel of any kind.** Distribution is: a meet-and-greet call, manual due diligence, a password-gated portal (`azreservesaccountportal.zite.so`), and a reported 100,000 USDT minimum. The stated target is mining operators, bullion providers, liquidity partners and institutions. The press release explicitly says the tokens are "not intended for retail distribution or public trading."

Secondary access is said to run through the **BTX marketplace** operated by **Black Tie Holdings / Black Tie Digital** (an Australian group with offices in Singapore and Hong Kong, which built Arizore's infrastructure), where "BTX and Black Tie Holdings independently operate the BTX marketplace environment, including onboarding, KYC verification, settlement processes... AZReserves provides reserve infrastructure and related reserve-linked asset framework components only." No licence was found for any Black Tie entity either, and the 61 lifetime transfers indicate the marketplace has produced essentially no secondary trading.

**Direct answer to question 8: AZG speaks to it only by opposite example.** It is the purest institutional-private-placement model in the landscape, and it is worth noting what that buys and costs. It buys a $66M book with 21 holders and no regulatory attention. It costs any possibility of the retail flywheel Aurumix depends on.

---

## 11. Recent developments

Reverse chronological, dated.

- **~14 July 2026.** Privately held **London Gold LLC** moves toward a **US$25M (C$35M) cash-and-stock acquisition of Bocana Resources** ([Northern Miner](https://www.northernminer.com/news/london-gold-offers-25m-for-bolivia-focused-bocana/1003893172/), [Mining.com](https://www.mining.com/london-gold-offers-25m-for-bolivia-focused-bocana/)). No public statement addresses what happens to the Arizore JV or to AZG's in-ground backing if Bocana changes hands. **This is an unresolved and material overhang.**
- **10 July 2026.** Current AZG and AZS contracts deployed to Ethereum mainnet (tx `0xdf679627476db05becd07a301a3aca9e4b6be11e21a7f74dc64fcb509cfcf746`). Undisclosed: no announcement of a redeployment or migration was made.
- **30 June 2026, 08:42 ET.** **CIRO halts trading in BOCA, reason "Pending News"** ([CIRO](https://iiroc.mediaroom.com/2026-06-30-Canadian-Investment-Regulatory-Organization-Trading-Halt-BOCA)). Trading subsequently resumed. The halt precedes the London Gold bid.
- **11 March – 4 June 2026.** The 61 lifetime AZG transfers occur, clustered in short bursts (11 Mar, 8–14 Apr, 20–31 May, 2–4 Jun), consistent with manual allocation to onboarded parties rather than trading.
- **30 March 2026.** Black Tie Digital publishes a case study, "Enabling Real-World Asset Collateralisation: Blacktie x Arizore", confirming Black Tie built "the AZ Reserve ledger layer, token issuance infrastructure (AZG & AZS tokens), and a pooled asset-backed token model" ([blacktie.digital](https://blacktie.digital/enabling-real-world-asset-collateralisation-blacktie-x-arizore/)). No chain, token standard, custodian, auditor or regulator is named in it.
- **22 February 2026 (datelined Sydney).** Arizore announces "$50.1M Live Reserve as AZG and AZS Mint Completes On-Chain": AZG reserve value $40,000,000, AZS $10,134,688, combined $50,134,688. Quoted: **George Boot, Chief Marketing Officer** ([arizore.io](https://arizore.io/reserve-room/written/live-reserve)). The stated AZG reserve has since grown to $64.99M, +62.5%.
- **~January 2026.** Bocana corporate update: the JV "is advancing the development of reserve and ledger architecture", the platform is "in its chain completion and registration phase", preliminary launch "anticipated by the end of January 2026."
- **27 November 2025.** Arizore Terms of Service and Privacy Policy last updated. These remain the only legal documents published.
- **5 November 2025.** Bocana corporate update: "The recently announced joint venture agreement between Bocana and Arizore, Ltd. continues to evolve as plans to create an umbrella joint venture agreement are in the planning stages" ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/11/05/3181268/0/en/bocana-resources-corp-provides-corporate-update.html)).
- **14 October 2025 (agreement dated 23 September 2025).** **Bocana Resources Corp. (TSXV: BOCA; Frankfurt: VC1) announces a 50/50 JV with Arizore Ltd. of Nevis, West Indies, forming Arizore LLC in Nevada.** Arizore Ltd. to provide **up to USD $60,000,000 in secured funding loans**, with no obligation on Bocana to contribute equity capital. Tokenization IP jointly owned. Bocana CEO named as **Tim Turner** ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/10/14/3166721/0/en/Bocana-Resources-Corp-Announces-Joint-Venture-with-Arizore-Ltd-to-Form-Arizore-LLC.html)).

**No regulator anywhere has issued a warning, alert, enforcement action or blacklist entry naming Arizore, AZ Reserves, AZG, AZS, Black Tie Holdings, Black Tie Digital, BT Asset Hub or BTX.** Checked: ASIC, FCA, SEC, CFTC, MAS, SFC, OSC.

### The $60M question

Bocana's market capitalisation at the time of the JV was approximately **$2.17M**. An unregistered Nevis entity with no published accounts, no named directors, no auditor and no licence committed **up to $60,000,000 in secured loans** to a JV with a shell roughly 1/28th that size. Where that money comes from is not disclosed. AZG's entire stated reserve is $65M. **The commitment is of the same order as the token programme it sits beside**, which suggests AZG token subscriptions are the intended funding source for the mining loans. If so, AZG holders are lending to junior mining projects while being marketed a gold reserve.

Live or dormant? **Live but barely moving.** Contracts are deployed and unpaused, the API responds, the site is maintained, and there is genuine third-party corroboration through a TSXV reporting issuer. But there are 21 holders, 61 lifetime transfers, no trading in the last 36 days, and no open roles ("No open positions at this time"). It is an operating private placement, not a functioning market.

---

## 12. Relevance to Aurumix

**Headline: AZG is not a competitor and should not be benchmarked as one. Its value to this engagement is as a boundary case that shows where "gold-backed" stops meaning gold-backed, and as proof that a headline AUM figure on rwa.xyz can be structurally hollow.** If the client sees AZG on a tokenized-gold league table and asks about it, the answer is in §5.

Taking the nine design questions in turn.

**Q1, custody fee: no usable signal.** Arizore publishes no fee schedule. The 1.00% management fee is a third-party claim from a source shown to be wrong on other fields. Settled question, nothing added.

**Q2, dividend funding: this is where AZG earns its place, and it is a warning.** Arizore does not pay yield to AZG holders. It pays yield to the *miners* on the other side, through a password-gated **"Mining Participation Program"** promising **"up to a maximum Annual Yield of 15.00%"**, distributed **quarterly in USDT** after a **45-day deferment**, allocated by a "Contribution Index" scored on reserve contribution, commitment duration and delivery performance, with the largest weight on **Delivery Performance** (volume delivered against contract, and timing against schedule). Under-delivery in a quarter "will result in the forfeiture of that quarter's Annual Yield allocation."

Two lessons, one good and one bad.

The *good* one is the mechanism Aurumix should actually steal: **the yield is conditional on a real external performance obligation, and it is forfeited if the obligation is missed.** This is the structural opposite of the PGOLD/Kinesis anti-pattern. Kinesis paid ~0.10% annualised against advertised figures ~20x higher because the yield was funded by recycled investor fees and promised unconditionally. Arizore's 15% is funded from "reserve profits" generated by bullion deliveries, and it *switches off automatically* when deliveries fail. **A forfeiture condition tied to a verifiable external event is a cheap, powerful and largely absent feature in this landscape, and it directly addresses the client's biggest open problem.** Aurumix's ICS Dividend could adopt exactly this shape: pay from a defined external source, and make the entitlement lapse when that source underperforms, rather than promising a percentage the fee base cannot fund.

The *bad* one is that Arizore does not do the disclosure work that would make the promise credible: no disclosed revenue, no accounts, no attestation, no statement of the profit pool's size, and the whole page sits behind a password. **A conditional yield is only better than an unconditional one if the condition is publicly verifiable.** That is the design note: take the forfeiture mechanic, but publish the numerator.

Also worth carrying to the STREAMEX workstream: this is a **second** structure (after Monetary Metals) where gold-related yield derives from a real external counterparty obligation rather than recycled fees. Unlike Streamex, Arizore's is undocumented, so it is not the precedent the client needs. But it does further weaken the earlier conclusion that no real-yield gold structures exist. It shifts the question from "does real-yield gold exist" to "which real-yield gold structures publish enforceable, ranked terms". Arizore's does not, and **nowhere does Arizore state how a token holder ranks if a miner defaults.**

**Q3, token standard: AZG is the negative case study, and it is a clean one.** The issuer concedes the token "may be characterized as security tokens", declares it "not intended for retail distribution or public trading", and then deploys a **plain, unrestricted, permissionless ERC-20 with unverified source behind an upgradeable beacon proxy**. All compliance is off-chain at onboarding; nothing stops a holder transferring to anyone. This is precisely the mismatch the client is trying to avoid by leaning to an ERC-3643 base. **Use AZG as the concrete example of what "we will handle it at onboarding" looks like once tokens are live: 21 holders, no transfer control, and a legal restriction that the code cannot enforce.** It also demonstrates the upgradeability risk the client should decide on explicitly: a single EOA controls a beacon that can replace the token logic for every holder simultaneously.

**Q4, regulatory route: relevant as the null option.** AZG has no UAE nexus and uses neither VARA nor the ADGM "Accepted Spot Commodity" route. Its answer to hybrid regulation is to have no licence at all and restrict distribution by hand. That is available to a 21-holder private placement and is **categorically unavailable to Aurumix**, which needs mass retail through an agent network. The instructive part is the cost: Arizore's obscurity strategy is why nothing about it can be verified, and why a data aggregator was able to attach a false custodian and a false regulator to it without contradiction. **Opacity is not free; it destroys the issuer's own ability to be believed.** For a savings product selling to Indian and NRI retail on a trust proposition, that trade is fatal.

**Q5, redemption: AZG is worse than Aurumix and usefully so.** Aurumix offers no physical redemption but does commit to cash buyback. Arizore commits to nothing: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways", while a third-party aggregator advertises "instant" redemption at 0.50%. **This is a live example of the gap the brief warns about, with the marketing claim living on rwa.xyz and the disclaimer living in the terms.** The lesson for Aurumix is defensive: when the client publishes buyback terms, publish them where the aggregators scrape them, because third-party listings will otherwise invent terms and the issuer will be held to them.

**Q6, premium and liquidity: one data point, conclusion not re-argued.** ~$65–66M stated AUM, **zero** on-chain liquidity, zero daily volume, 21 holders, 61 lifetime transfers, price set by the issuer at spot because no market exists. It is the extreme illiquid endpoint of the settled finding.

**Q7, proof of reserve: the most transferable warning in the profile.** Arizore publishes a live JSON "reserve" API and calls the result transparency. But it has **no timestamp** (`lastUpdatedIso: null`), no signature, no oracle, no attestation, no bar list, and no named auditor, and its `azgReserveValue` is **arithmetically identical to tokens × the issuer's own token price**, meaning the "proof" is a restatement of the issuer's assumptions rather than an independent measurement. Meanwhile rwa.xyz shows "KPMG" in an auditor field with nothing behind it, and the contract is not even source-verified. **Aurumix's PoR must therefore do three specific things AZG does not: carry a timestamp, be signed or attested by a named third party, and state the metal quantity independently of the token price.** If reserve value is derived from token price, it proves nothing.

**Q8, distribution: speaks to it only by contrast.** No savings plan, no recurring purchase, no referral, no affiliate, no agent tier. Confirms the brief's expectation that almost nothing in this landscape does recurring retail distribution, which remains Aurumix's genuine differentiator.

**Q9, wind-down: nothing, and the omission is now unanimous.** No wind-down plan, no insolvency provision, no statement of what happens to the reserve if Arizore fails, and no disclosure of holder ranking against the miners or against Arizore's creditors. AZG is materially worse than the failed protocols on this point, because a majority of its reserve is in-ground resource that **cannot be distributed to holders at all** in a wind-up: you cannot deliver an unmined ounce. Add the live overhang that Bocana, the JV counterparty, is under a $25M takeover offer with no public statement on the JV's fate. **AZG makes the client's cheap-differentiation argument for them: ten protocols now, none with a wind-down plan.**

### The one structural idea worth stealing

Strip away the opacity and there is a genuine mechanism here: **yield paid from a real external obligation, scored on verifiable delivery performance, and automatically forfeited when delivery fails.** That is the shape of a dividend that survives a securities-classification argument better than "we pay you a share of the fees you paid us", and it is the shape the client's ICS Dividend currently lacks. Arizore fails to make it credible only because it publishes no numbers. Aurumix can take the mechanic and add the disclosure.

### The one thing to make sure the client never does

Blend an asset the holder can verify with one they cannot, and price the blend as if it were all the verifiable one. AZG charges one ounce of gold for half an ounce of gold plus a discounted claim on a mine. Aurumix's entire pitch is "100% of every dollar buys physical LBMA gold", and its peg is grams ÷ tokens. **Any future temptation to admit non-vaulted assets into the reserve, whether gold leases, receivables or forward purchases, breaks that sentence and the peg formula at the same time.** AZG is the fully worked example of where that ends: a $66M headline that is 38% metal, with no market, no attestation and no redemption.

---

## 13. Open items for verification

- [ ] Obtain the **Nevis FSRC company search report for Arizore LTD** via a paid agent (the register is not publicly searchable). Confirm registration number, incorporation date, status and registered agent. Establish whether **AZ Reserves Ltd** exists as a separate legal person or is only a trading name.
- [ ] Determine which entity legally issues AZG: Arizore LTD (Nevis), AZ Reserves Ltd (per rwa.xyz), or Arizore LLC (Nevada). Search the **Nevada SOS register for Arizore LLC** (blocked by bot protection in this pass) for entity number, managers and status.
- [ ] **Put the Perth Mint custody claim directly to Gold Corporation.** rwa.xyz asserts LEI 213800HQZYBMURES6D84 as AZG's custodian with zero corroboration. A one-line confirmation or denial from the Perth Mint settles it and is worth having on the record.
- [ ] **Ask KPMG whether any engagement exists** in relation to Arizore, AZ Reserves, AZG or AZS. rwa.xyz names KPMG as auditor with no supporting document anywhere.
- [ ] Report the rwa.xyz metadata errors (issuer name, auditor, custodian, ASIC/AFSL regulatory status, "instant" redemption) to `team@rwa.xyz`. **Second confirmed instance of fabricated issuer metadata after ORO's "Gold Issuance Inc."** Decide whether rwa.xyz remains a citable source in the assembled document.
- [ ] Pull **Bocana Resources' SEDAR+ filings** (material change reports, MD&A, annual financials) for the Arizore JV agreement itself: security granted over the $60M loan facility, drawdown to date, interest rate, and any auditor commentary. This is the only continuous-disclosure window onto Arizore and it is the highest-value remaining thread.
- [ ] Establish whether the **London Gold LLC acquisition of Bocana** proceeds and what becomes of the Arizore JV, the jointly owned tokenization IP, and the in-ground resource pledged into the AZG reserve.
- [ ] Identify the **62% in-ground component**: which specific deposits, which operators, which NI 43-101 technical reports, and whether the pledged resources are measured, indicated or inferred. Inferred resources backing a spot-priced gold token would be a further material finding.
- [ ] Obtain the **forward contract template and the "separate agreements"** referenced in the terms, to determine what an AZG holder legally owns and where they rank against miners and against Arizore's creditors on default.
- [ ] Obtain the full **Mining Participation Program** page (password-gated): the size of the profit pool, the definition of "reserve profits", the historical distributions actually paid, and whether any quarterly USDT distribution has ever occurred.
- [ ] Verify the AZG **beacon implementation contract** `0x0c7f3724A477B13a73BF931B3cE2ee7148DFBd44` (unverified source): check for mint, burn, pause, blacklist and upgrade authority, and identify who controls the beacon.
- [ ] Explain the **contract deployment date (10 July 2026) against the February 2026 "mint completes on-chain" announcement**. Establish whether an undisclosed migration occurred and what happened to the original token holders.
- [ ] Identify **any officer other than George Boot (CMO)**. No CEO, director or beneficial owner of Arizore is named in any public source.
- [ ] Establish the legal entity and licence status of the **BTX marketplace / BT Asset Hub operator** (Black Tie Holdings / Black Tie Digital, Australia), which performs KYC and settlement for AZG secondary access.
