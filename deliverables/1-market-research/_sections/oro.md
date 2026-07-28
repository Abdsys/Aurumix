# ORO / Oro Finance (GOLD)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | GOLD (also written $GOLD; rwa.xyz lists it as "Orogold") | High |
| Issuer (marketing) | ORO / Oro Finance / ORO Labs; legal title asserted to sit with an unnamed "ORO Foundation" | Medium |
| Issuer (registry) | **Oro Labs PTE Ltd, UEN 202434484G**, incorporated 22 August 2024, 68 Circular Road, Singapore. ACRA activity: other holding companies / software development | High |
| Domicile | **Singapore** (registry). Marketed and staffed from Dubai/UAE. rwa.xyz separately names the issuer "Gold Issuance Inc.", an entity we could not locate in any register | High (registry) / Low (Gold Issuance Inc.) |
| Backing claim | 1 GOLD = 1 troy ounce of LBMA and UAE GD certified 99.99% physical gold, vaulted with Brinks | Medium (issuer assertion) |
| Chains | Solana only. SPL Token (legacy Token program), 6 decimals | High (on-chain) |
| Contract address | `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A` | High (on-chain) |
| Supply | **608.418838 GOLD = 608.42 troy oz** (~18.92 kg) | High (Solana RPC, 28 Jul 2026) |
| Market cap / TVL | **~$2.45M** at ~$4,033/oz. rwa.xyz shows $2,490,203 | High |
| On-chain liquidity | ~$736k in the main Meteora GOLD/USDC pool; ~$812k across all pools | High |
| 24h volume | ~$56.8k, of which sells ~$55.2k vs buys ~$1.6k | High |
| Holders | 9,732 (Jupiter) / 9,809 (rwa.xyz). Top holders ~61.85% | High |
| Regulatory status | **No licence found in any jurisdiction.** Not on MAS, VARA, ADGM FSRA, DFSA or Labuan FSA registers | High (negative search) |
| Subscription fee | 0.50% mint (1.00% off-hours) | High (issuer docs) |
| Ongoing custody fee | **Zero charged to holder.** Funded by the leasing spread and mint/redeem fees | Medium |
| Redemption fee | 0.50% (1.00% off-hours); **+1.5% for USDC settlement** | High (issuer docs) |
| Advertised yield | 3–4% APY on front page; docs say "typically in the 3 to 5% APY range"; requires a **12-month lockup** | High |
| Named officers | Usman Saleem (founder/CEO). **Juan Marchetto, co-founder and CTO: CONFIRMED but has since departed** | High |

---

## 1. What it is

ORO is a tokenized gold protocol on Solana. One GOLD token represents one troy ounce of certified physical gold. Its distinguishing pitch against PAXG and XAUT is that the gold is not merely parked: holders can stake GOLD into an institutional gold leasing programme and earn 3–4% APY paid in more GOLD, so the position compounds in metal rather than in fiat.

The operating company is Oro Labs PTE Ltd, a Singapore holding company. The product is marketed from Dubai, and the founder's contact details are UAE-based. It raised a $1.5M pre-seed in March 2025 led by 468 Capital with participation from Fasset ([Wamda](https://www.wamda.com/2025/03/oro-labs-secures-1-5-million-pre-seed-backed-468-capital), [Enterprise Times](https://www.enterprisetimes.co.uk/2025/03/17/oro-labs-raises-1-5-million-to-redefine-gold-markets/)).

It is small. 608 ounces, about 18.9 kg of gold, roughly $2.45M. For scale, that is one order of magnitude below PGOLD and three below PAXG. **Nearly ten thousand holders share 608 ounces**, an average of 0.0625 oz (~$252) each. This is a retail-distribution product with a retail-sized balance sheet, which makes it the closest structural analogue in this landscape to what Aurumix intends to build.

**Note on scope:** the brief flagged ORO / Oro Finance / ORO Labs / orogold.com / orogold.app / the rwa.xyz "Orogold" listing as one project. Confirmed, and there is now a further consolidation: **orogold.app 301-redirects to oro.finance**. The primary domain has moved.

---

## 2. Legal structure

This is the weakest documented part of the protocol and the part most relevant to Aurumix.

**What ORO asserts.** The docs state that "Legal title is held by a foundation, making the structure bankruptcy remote" ([audits page](https://orogold-1.gitbook.io/oro/8.-audits-and-security.md)), and name it the "**ORO Foundation**", describing holders as having "beneficial ownership of all underlying physical assets" via a trust structure, and GOLD as "a digital bearer instrument for ownership of real gold" ([legal page](https://orogold-1.gitbook.io/oro/7.-legal-risk-and-trust.md)).

**What can be verified: nothing.** The ORO Foundation is **not identifiable in any register we searched**: Cayman Islands General Registry, Panama Public Registry, ADGM, Labuan, Liechtenstein Stiftungsregister, and Singapore ACRA all return no match. **No jurisdiction is stated anywhere in ORO's own documentation.** No foundation charter, trust deed, or declaration of trust is published. The word "foundation" appears in the docs and in a Solana ecosystem article ([Solana](https://solana.com/news/tokenizing-gold-inside-oro-s-vertically-integrated-bet)) and nowhere else.

So the chain of title runs: holder → beneficial interest → a trust → a foundation that cannot be shown to exist. **"Bankruptcy-remote" is an unverifiable adjective here, not a documented structure.** Bankruptcy remoteness is a conclusion that follows from a specific entity in a specific jurisdiction with specific constitutional documents. None of the three is disclosed.

Compounding this: the terms disclaim issuance to unnamed "independent Third-Party Service Providers", and the docs simultaneously insist "$GOLD is not a security, derivative, or speculative token" and that ORO is "a non-custodial platform, not a bank, broker, or investment adviser": self-characterisations with no regulator having tested them.

**Confidence: Low** on the foundation existing as described. **Confidence: High** that it is not publicly identifiable.

---

## 3. Regulatory and compliance posture

**No licence found in any jurisdiction.** Checked and not found:

| Register | Result |
|---|---|
| MAS Financial Institutions Directory / PSA (DPT) lists, Singapore | Not found |
| Dubai VARA public register | Not found |
| ADGM FSRA public register | Not found |
| DFSA (DIFC) public register | Not found |
| **Labuan FSA licensed entities**, Malaysia | **Not found** |
| Labuan FSA unregulated/unauthorised warning list | Not found (also no adverse listing) |

**Contradiction flagged.** Secondary write-ups circulate the claim that "ORO's token is regulated by Labuan FSA". **This is refuted.** No entity named ORO, Oro Finance, Oro Labs or Orogold appears on any Labuan FSA licence category (money broking, credit token, digital asset exchange, or otherwise). Nor does Fasset. Anyone repeating "regulated by Labuan FSA" is repeating an unsourced secondary claim, and Aurumix should not treat ORO as a licensed precedent.

**ADGM.** ORO is reported to have signed a **Memorandum of Understanding** at ADGM regarding expanding tokenized gold adoption in the UAE. An MoU is not a licence, confers no authorisation, and no ADGM press release or register entry confirming it could be located. **Confidence: Low.**

**The KYC contradiction (material).** The docs state "Only KYC/KYB whitelisted wallets can mint, convert, and redeem" and "All redemption options are available only to KYC/KYB whitelisted wallets". But on-chain, **the mint's freeze authority is `null`**. There is no transfer restriction, no permissioning, no whitelist enforceable at the token layer. GOLD is a plain SPL token that anyone can buy on Jupiter or Meteora with no KYC whatsoever, and secondary coverage advertises exactly that ("swap into $GOLD on Jupiter and Meteora without KYC"). The gate exists only at the mint/redeem boundary with the issuer, not on the asset. This is a coherent design, but the documentation's phrasing invites the reader to believe the token is permissioned when it is not.

---

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | Brinks, asserted. "Brinks handles the physical vaulting, not Oro" | Medium (no custody agreement published) |
| Vault / city | **Not disclosed** | — |
| Allocated? | Implied by "1:1 backed" and trust framing, never stated as allocated and segregated | Low |
| Bar list | **Not disclosed.** No serial numbers, no weights, no refiner list | — |
| PoR feed | **None.** No on-chain proof-of-reserve oracle, no Chainlink PoR feed, no live reserve dashboard | High |
| Reserve attestation | RSM named. **No attestation document is published for download** | High |
| Smart contract audit | Cantina (Spearbit Labs Inc.), March 2026; Adevar Labs, April 2025. Both downloadable | High |

**The audit/attestation blur is present and it is severe.** The transparency page headline reads "Independently Verified Reserves", and the only two documents actually downloadable from it are **smart-contract security audits**. A smart-contract audit says the Solana program does what the code says. It says nothing whatsoever about whether 608 ounces of gold exist in a vault. A reader who skims "audited" draws precisely the wrong conclusion, which is the pattern the brief warns about.

**Frequency is also inconsistent across ORO's own surfaces**: the front page and transparency page say reserves are "verified **quarterly** by RSM"; the FAQ refers to "**monthly** audit reports from third-party vault and assurance providers"; and the Solana ecosystem article says "**Monthly** audits from RSM". Three different frequencies from the same issuer, with zero published documents to settle it. **Not disclosed** is the correct answer on ORO's actual reserve attestation, and that is a finding.

---

## 5. Issuance

Mint by swapping USDC in the app; GOLD is minted 1:1 minus a 0.50% fee (1.00% off-hours). Identity verification is required to mint: government ID plus liveness for individuals, business registration and signatory verification for entities. **No minimum purchase amount is stated** in the docs.

On-chain, the mint authority is `HKMT2i4kGzktb4AVo4fKkHK4AmpxVyvGEAfotVX3tML4`, a 45-byte non-executable PDA owned by program `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop`. So minting is program-controlled rather than sitting on a bare EOA, which is the better of the two designs, though the program's upgrade authority was not verified. Mint authority is **live** (not renounced), as it must be for an expandable gold token. Token created 27 April 2025; first liquidity pool 21 May 2025.

---

## 6. Redemption

Two routes, both **KYC/KYB whitelist-gated**:

| Route | Terms |
|---|---|
| To USDC | 0.50% redemption fee (1.00% off-hours) **plus ~1.5% USDC settlement charge**. Up to 48 hours. Price locked at request against live spot |
| To physical gold | Minimum increments of **1g**; typical formats 10g+, 100g, 1oz, 1kg bars. Delivery, insurance and a market premium over spot may apply, **quoted before confirmation, percentages not disclosed**. Typically 3–7 business days |

**Eligibility is restricted in two ways** worth flagging: redemption requires KYC/KYB whitelisting, and **physical pickup is currently available only in the UAE**. Redemption "may be unavailable in restricted jurisdictions", which are not enumerated. So a holder in, say, India, who bought GOLD KYC-free on Jupiter, has no assured physical exit.

**On the previously reported "~$85 increment with a 1-day lock": partly real, now stale.** Both figures trace to the **18 December 2024 launch press release**, which stated "Tokens can be redeemed for physical gold starting at $85 increments" ([GlobeNewswire](https://www.globenewswire.com/news-release/2024/12/18/2999238/0/en/ORO-Launches-as-First-App-Built-on-Fasset-s-L2-Network-Unlocking-1B-of-Tokenized-Gold-On-Chain.html)). That release predates the actual Solana launch. **Current documentation states 1g minimum increments, not $85** (1g is ~$130 at today's ~$4,033/oz). The "1-day lock" does not appear in the press release or in current docs. What current docs do specify is a **48-hour USDC processing window and a 12-month staking lockup**, which is a materially different and much longer commitment. Treat "$85 / 1-day" as **superseded**.

---

## 7. Fees and revenue model

| Fee line | Amount | Notes |
|---|---|---|
| Mint | 0.50% (1.00% off-hours) | |
| Redeem to gold or USDC | 0.50% (1.00% off-hours) | |
| USDC redemption settlement | 1.50% | Charged on top of the redemption fee |
| Ongoing custody / management | **Zero to the holder** | Not deducted in grams, not billed in cash |
| Staking | Free | 12-month lockup |
| Claiming yield | Free | |
| Unstaking after 12 months | Free | |

**Directly relevant to Aurumix design question 1.** ORO takes **option three**: it charges the holder no ongoing custody fee at all and recovers cost elsewhere. This preserves a clean 1 token = 1 ounce peg, exactly the property Aurumix needs (price = grams ÷ tokens breaks if you deduct in grams). ORO funds custody from (a) the spread on the leasing programme and (b) mint/redeem fees.

**Whether that arithmetic works at this size: it does not.** 608 oz at ~$4,033 is ~$2.45M of AUM. Allocated vaulted gold custody and insurance runs roughly 0.10–0.50%/yr, call it $2.5k–$12k. Against that, ORO must also pay a 3–5% yield to stakers, which requires the leasing programme to earn more than 3–5% gross. Institutional gold lease rates have historically sat well below that in normal conditions. At $2.45M of AUM, the entire fee base is trivial: even 1% round-trip on the full supply turning over once a year is ~$25k. **ORO's disclosed sources cannot fund a $1.5M-pre-seed operating team; the venture round is funding the operation, not the fee model.** That is survivable for a startup and unremarkable, but it means ORO is not yet evidence that a zero-custody-fee, yield-paying gold token is self-sustaining. Aurumix should not cite it as proof that the model closes.

---

## 8. Token architecture

- **Standard:** SPL Token, legacy Token program (`TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA`), **not** Token-2022. So **no transfer hooks, no confidential transfers, no permanent delegate, no transfer-fee extension.**
- **Decimals:** 6. With 1 token = 1 troy ounce, the smallest unit is 0.000001 oz (~$0.004), so fractional retail purchases are not constrained by precision.
- **Permissioned?** **No.** `freezeAuthority: null`. There is no whitelist, blacklist or transfer restriction at the token layer, despite the docs' KYC/whitelist language.
- **Mint authority:** live, held by PDA `HKMT2i4kGzktb4AVo4fKkHK4AmpxVyvGEAfotVX3tML4` under program `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop`.
- **Upgradeability / admin keys:** program upgrade authority **not disclosed** in docs and not verified here. This is the single most important unverified technical control.
- **Bridge:** none. Solana only.

**Directly relevant to Aurumix design question 3.** ORO chose the fully fungible, permissionless base. What that **buys** it is real DEX liquidity: it is quotable on Jupiter, poolable on Meteora, Orca and Raydium, and pairable against XAUt0 and GLDx. Roughly $812k of pooled liquidity against $2.45M of supply is a 33% liquidity-to-AUM ratio, which is dramatically healthier than PGOLD's ~2%. What it **costs** ORO is that every compliance claim in its documentation is unenforceable on the asset. Anyone can hold GOLD; ORO can only gate the mint and redeem doors. For Aurumix, whose ICS standing, dividend entitlement, credit eligibility and buyback rights all break on an anonymous DEX transfer, **ORO is a direct demonstration of the tradeoff**: it got liquidity precisely by giving up the control Aurumix cannot give up.

---

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Supply | 608.418838 oz |
| Price | ~$4,032.71 |
| Market cap / FDV | ~$2.45M |
| Pooled liquidity (all DEXs) | ~$812k |
| Main pool | Meteora GOLD/USDC, ~$736k liquidity, ~$54.8k 24h volume |
| Other pools | XAUt0/GOLD ~$70.5k (Meteora), GLDx/GOLD ~$3.2k, Orca XAUt0/GOLD ~$1.2k, plus dust pools |
| 24h volume | ~$56.8k total |
| Holders | ~9,732–9,809 |
| Top-holder concentration | ~61.85% |
| Jupiter organic score | **Low** |
| Jupiter tags | commodities, rwa, verified, moonshot-verified, community-assist |

**Directly relevant to Aurumix design question 6.** This is the most useful liquidity datapoint in the landscape, and it cuts **against** the client's premium thesis. ORO has a 33% liquidity-to-AUM ratio, sixteen times better than PGOLD's ~2%, and **it still does not produce a premium**. GOLD trades at ~$4,032–4,041 across pools while XAUt0 prints ~$4,079 in the paired pool: ORO is trading at a slight *discount* to another tokenized gold token, not a premium to spot. Volume is also one-directional: **~$55.2k of sells against ~$1.6k of buys in 24 hours**, roughly 34:1, with liquidity down 14.3% on the day.

The lesson for Aurumix: **liquidity depth does not manufacture a premium.** A well-arbitraged gold token converges to spot minus friction, because gold is the most efficiently arbitraged commodity on earth and any premium is immediately minted away by an issuer with a live mint authority. The 3–8% exchange premium Aurumix is banking on is not observable at either end of the liquidity spectrum: not in PGOLD's illiquid market, and not in ORO's liquid one. That is now two independent observations pointing the same way.

---

## 10. Distribution

- **Channels:** direct app (app.oro.finance), plus permissionless DEX access via Jupiter, Meteora, Orca, Raydium.
- **Target segments and geography:** the December 2024 launch material named UAE, Indonesia, Turkey, Malaysia, EU, Pakistan and India, with an explicit focus on **Muslim-majority markets** and Asia/Middle East. This overlaps Aurumix's India/UAE/NRI target almost exactly.
- **Referral / points:** yes. A "**Nuggets**" points programme rewards early users, and an airdrop is widely anticipated across airdrop-tracking sites. There is also a separate "Grail" product line (docs.grail.oro.finance) and an ecosystem page.
- **Savings plan / recurring purchase / SIP:** **Not disclosed.** No monthly contribution plan, no systematic investment feature, no agent or commission network.
- **Agent network:** none.

So ORO's retail growth engine is a **points-and-airdrop farm**, not a savings plan. That is the finding: it has assembled ~9,800 holders averaging $252 each, which is a genuinely retail distribution, but it did so with speculative airdrop incentives rather than recurring contributions. Points programmes produce holders who leave when the airdrop lands, which is a plausible reading of the 34:1 sell/buy ratio. **Aurumix's SIP plus 3-tier agent model remains unmatched by any protocol in this landscape.**

---

## 11. Recent developments

- **28 July 2026 (today):** on-chain state verified. Supply 608.418838 oz, ~$2.45M cap, ~9,732 holders, freeze authority null, mint authority live. 24h volume ~$56.8k skewed ~34:1 to sells; liquidity down 14.3% on the day.
- **~2026 (undated):** **orogold.app now 301-redirects to oro.finance.** Primary domain and brand consolidated onto oro.finance.
- **26 January 2026:** **Monetary Metals issued a public statement on the AgaBullion default.** Turkish authorities arrested principals at AgaBullion Kiymetli Madenler A.Ş. and affiliated Aleks Metal Refinery, and **some leased gold was seized**. Monetary Metals stated legal title remains with lessors, that it is working with Istanbul counsel and the US Consulate, and that it "carries supplemental insurance on leased metals and will file claims when and if appropriate" ([Monetary Metals](https://www.monetary-metals.com/about-us/newsroom/monetary-metals-statement-regarding-agabullion/)). **This is the live stress test of the exact structure ORO's yield depends on. See §12.**
- **March 2026:** Cantina (Spearbit Labs Inc.) smart-contract audit published.
- **May 2025:** Monetary Metals partnership announced. Confirmed by both parties in **marketing only**; no legal document names ORO.
- **21 May 2025:** first GOLD liquidity pool created on Solana.
- **27 April 2025:** GOLD mint created on Solana.
- **April 2025:** Adevar Labs smart-contract audit published.
- **17–18 March 2025:** $1.5M pre-seed led by 468 Capital, with participation from **Fasset** and angels from Phantom, Jupiter and Helium ([Wamda](https://www.wamda.com/2025/03/oro-labs-secures-1-5-million-pre-seed-backed-468-capital), [Enterprise Times](https://www.enterprisetimes.co.uk/2025/03/17/oro-labs-raises-1-5-million-to-redefine-gold-markets/)).
- **18 December 2024:** launch press release: "ORO Launches as First App Built on Fasset's L2 Network, Unlocking $1B of Tokenized Gold On-Chain" ([GlobeNewswire](https://www.globenewswire.com/news-release/2024/12/18/2999238/0/en/ORO-Launches-as-First-App-Built-on-Fasset-s-L2-Network-Unlocking-1B-of-Tokenized-Gold-On-Chain.html)).
- **22 August 2024:** Oro Labs PTE Ltd incorporated in Singapore, UEN 202434484G.

### Status of the previously reported Fasset "Own" L2 and $1B target: both STALE

**Both claims are real but obsolete, and the framing was wrong.** The 18 December 2024 press release announced ORO as "the first application built on Fasset's Ethereum Layer 2 network, Own", in partnership with "The Own Foundation", targeting "$1 billion of yield-bearing gold to be tokenized within the first year".

What actually happened: **ORO shipped on Solana, not on Own.** The mint was created on Solana on 27 April 2025, the docs state "$GOLD is an SPL token" and "built on Solana for speed, scale, and low fees", and there is no bridge and no deployment on Own or any EVM L2. Fasset's role has since been reported only as an **investor** in the March 2025 pre-seed, not as the host chain. No announcement of the Own deployment being cancelled was ever made; it was simply abandoned silently.

The **$1B first-year target** was set in December 2024. First year would have ended December 2025. **Actual result: ~$2.45M**, or about **0.245% of target**, and that is on a ~19-month clock rather than 12. This is a ~408x miss. "The Own Foundation" is likewise not locatable in any register.

Aurumix should treat this as a caution about the genre: tokenized gold launch press releases carry AUM targets that miss by two to three orders of magnitude, and the chain named at launch is frequently not the chain shipped.

### Co-founder "Juan Marchetto": CONFIRMED, and he has since left

**Verified, contradicting the assumption that this was unreliable.** The 18 December 2024 launch release states the company was "Founded in 2024 by Usman Saleem and Juan Marchetto", naming him **ORO Co-Founder**. His own GitHub profile independently confirms it: "At Oro.finance I designed and shipped a gold-backed stablecoin protocol on Solana as CTO, raised $1.5M" ([github.com/JuanMarchetto](https://github.com/JuanMarchetto)).

**But he has departed.** His profile lists Oro.finance under "Before" and states "Now: founding engineer at Nora Finance, building cross-border payment rails and stablecoin settlement in Rust". So **ORO's technical co-founder and CTO, the person who built the Solana protocol, has left for another company.** No departure announcement was made by ORO, and current ORO and press materials name only Usman Saleem, describing the company as "founded in 2024 by Usman Saleem" with Marchetto written out. Note also that most March 2025 funding coverage already omitted him.

**Confidence: High** that he was co-founder and CTO. **Confidence: Medium-High** that he has left (self-reported, uncontradicted, consistent with ORO's own current materials).

---

## 12. Relevance to Aurumix

ORO is the most instructive protocol in this landscape for Aurumix, because it is the only one attempting the same combination Aurumix is attempting: **retail-scale distribution, a yield on top of gold, and no custody fee charged to the holder.** It is also, on the single question Aurumix's dividend design hinges on, a cautionary tale.

**Design question 2 (dividend funding), the decisive finding.** Aurumix's central hope is that real external asset yield (gold leasing) is the compliant alternative to a fee-recycled dividend. ORO is the live test of that hope, and **the test result is that the legal plumbing does not exist**.

Nothing is published on how GOLD holders rank if a lease counterparty defaults. Specifically, and after direct searching:
- No Oro–Monetary Metals lease agreement, master lease or term sheet is published anywhere: **not found**.
- No subordination, security interest, collateral or priority provision naming GOLD holders: **not found**.
- No loss waterfall allocating a lessee default between token holder, ORO and Monetary Metals: **not found**.
- No Monetary Metals legal document names ORO at all. The partnership exists in marketing only.

ORO's docs assert the conclusion without the mechanism: "In case of lessee insolvency, leased gold is not part of their estate", the gold "legally remains your property even while leased", and "All gold under leases is insured against theft and damage". These are **assertions about a legal outcome with no published instrument creating it**, and they are made by ORO about a counterparty relationship ORO is not obviously a party to.

**The contrast that makes this concrete.** Monetary Metals *has* published a proper tokenized lease agreement, just not with ORO: the **Tokenized Yield Partnership Agreement with StreamEx, filed with the SEC** ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1530766/000164117225026853/ex10-1.htm)). It specifies that the lessee must maintain a jeweller's block policy at **≥110% of gold value**, with Monetary Metals as **loss payee and additional insured**, from an A-rated or better insurer. Monetary Metals separately describes requiring **corporate guarantees, UCC filings and sometimes personal guarantees** ([Monetary Metals](https://www.monetary-metals.com/how-we-protect-client-gold-and-silver/)). **So the standard of disclosure exists and is achievable. ORO simply has not met it.**

**And the risk is not theoretical.** On 26 January 2026 Monetary Metals disclosed the **AgaBullion** default: Turkish authorities arrested the lessee's principals and **seized some of the leased gold**. Monetary Metals' response was to assert that title remains with lessors, retain Istanbul counsel, approach the US Consulate, and consider insurance claims. That is a multi-year, cross-border, uncertain recovery. **"Legal title remains with the lessor" turns out to mean "we will litigate in Turkey", not "your gold is safe".** Note also the ordering: the loss payee on the lessee's insurance is Monetary Metals, not the token holder, so recovery proceeds flow to the platform first and reach the end holder only by whatever contract exists between them, which for ORO is unpublished.

**The direct implication for Aurumix's ICS Dividend:** if Aurumix funds its dividend from gold leasing to avoid the securities-classification risk of a fee-funded dividend, it inherits **lessee credit risk on the very gold that backs the token**, and it must publish the loss waterfall or it will be in ORO's position: promising a yield whose downside is undocumented. The encumbrance is real. Leased gold is gold that is not in the vault. Aurumix should decide explicitly whether a defaulting lessee's loss lands on (a) all holders pro rata, breaking the peg, (b) only stakers who opted in, or (c) the issuer's balance sheet, and should say so in writing before launch. **Publishing that waterfall would be genuine differentiation: neither ORO nor anyone else in this landscape has done it.**

**Design question 1 (custody fee): ORO validates the third option.** It charges holders nothing ongoing, preserving an exact 1 token = 1 oz peg, and funds custody from the leasing spread plus mint/redeem fees. This is the model Aurumix should copy in *structure*. But per §7 the arithmetic does not yet close at $2.45M of AUM: venture capital is subsidising it. Aurumix should adopt the mechanism and be honest internally that it needs scale (or a genuinely profitable adjacent revenue line, which for Aurumix is the credit facility and Gold Card) to fund it.

**Design question 3 (token standard): ORO is the counterfactual.** It runs a plain SPL token with **freeze authority null**, no permissioning at all. It thereby earns a 33% liquidity-to-AUM ratio and genuine DEX quotability, and pays for it by having every KYC claim in its docs be unenforceable on the asset. Aurumix cannot make this trade, because ICS standing, dividend entitlement, credit eligibility and buyback rights all die on an anonymous transfer. **ORO is the evidence for why Aurumix's ERC-3643-style permissioned base is the right call**, and simultaneously the evidence for what that will cost: expect materially thinner secondary liquidity than ORO's, and plan the buyback as the primary exit rather than hoping a DEX market appears.

**Design question 5 (redemption): ORO does what Aurumix refuses to do, and it is still geographically hollow.** ORO offers physical redemption from 1g, which sounds like a decisive advantage over Aurumix's cash-only buyback. But **physical pickup is available only in the UAE**, redemption requires KYC/KYB whitelisting, and delivery premiums are undisclosed until quoted. For ORO's actual holder base (Indonesia, Turkey, Malaysia, Pakistan, India) the physical option is largely notional. Aurumix's cash-buyback-only position is more honest than ORO's, provided Aurumix never claims physical redeemability. The reputational risk is in the mismatch, not in the absence.

**Design question 6 (premium): see §9.** ORO refutes the premium thesis from the liquid end, as PGOLD refutes it from the illiquid end. **Aurumix should stop treating a 3–8% exchange premium as a modelling input.** No tokenized gold token in this landscape sustains one, and structurally none can while the issuer holds a live mint authority.

**Design question 7 (proof of reserve): ORO is the anti-pattern to name.** "Independently Verified Reserves" as a headline, with two smart-contract audits as the only downloadable evidence, three mutually inconsistent attestation frequencies, no bar list, no PoR feed and no attestation document. Aurumix can beat this cheaply: publish one real attestation with a bar list, on a stated cadence, and it immediately out-discloses a venture-backed competitor.

**Design question 8 (distribution): unmatched.** ORO has no savings plan, no recurring purchase, no agent network. Its retail base came from a points-and-airdrop programme, which buys holders who sell on the unlock. Aurumix's SIP plus 3-tier agent network remains the genuine structural differentiator across this entire landscape.

**Design question 9 (wind-down): fails, and worse than most.** ORO documents nothing about what happens to the gold if the issuer fails. It gestures at a "bankruptcy-remote foundation" that **cannot be found in any register in any jurisdiction**, which is arguably weaker than saying nothing, because it invites reliance on a protection that cannot be verified to exist. Combined with the departure of the CTO who built the protocol, and a program upgrade authority that is not disclosed, ORO has key-person and key-control risk with no published contingency. **Aurumix committing ex ante to a named entity, a named jurisdiction, a published charter and a wind-down waterfall remains cheap, and remains unoccupied ground.**

---

## 13. Open items for verification

- [ ] Identify the ORO Foundation: obtain its jurisdiction, registration number and constitutional documents. Absent these, treat "bankruptcy-remote" as marketing and do not cite ORO as precedent for a foundation structure.
- [ ] Resolve "Gold Issuance Inc.", the issuer name rwa.xyz shows for the GOLD listing. It matches no entity we can find. Determine whether it is the missing issuing SPV, a data error, or a third entity in the stack.
- [ ] Obtain the Solana program upgrade authority for `iNtiXEFgDNrc6FUt4cFALDe3D8RF3sVnNuKSHwxZRop` and determine whether it is a multisig, a single key, or immutable. This is the most important unverified technical control over the token.
- [ ] Request the RSM reserve attestation directly and establish its true frequency (quarterly per the front page, monthly per the FAQ and Solana article). Determine whether any attestation has ever been issued.
- [ ] Confirm whether Brinks has a written custody agreement with ORO or the Foundation, and whether gold is allocated and segregated or held on an unallocated basis.
- [ ] Obtain the ORO Terms of Use and Privacy Policy. The docs reference them; oro.finance/terms returned 404 at the time of research. Read the "independent Third-Party Service Providers" issuance clause in full.
- [ ] Establish whether ORO is a direct Monetary Metals client, a sub-participant, or merely a marketing partner. This determines whether GOLD holders have any contractual path to lease recovery proceeds at all.
- [ ] Track the AgaBullion recovery through 2026–27. It is the best available empirical read on what "legal title remains with the lessor" is actually worth in a cross-border seizure, and it directly prices the risk Aurumix would take on by funding a dividend from leasing.
- [ ] Confirm Juan Marchetto's departure date and whether any technical continuity plan exists at ORO.
- [ ] Verify whether the ADGM MoU exists as a document and what, if anything, it commits either party to.
- [ ] Monitor whether the anticipated "Nuggets" airdrop lands, and measure holder retention and the sell/buy ratio afterward. This is a free natural experiment on whether points-farmed retail holders persist, directly relevant to Aurumix's retention assumptions.
