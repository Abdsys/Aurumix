# Aurus (tGOLD / tXAU)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | tGOLD (tXAU). Formerly AurusGOLD (AWG), renamed 9 Nov 2022. Siblings: tSILVER (tXAG), tPLATINUM (tXPT). Ecosystem tokens: AurusX (AX), migrating to $AURUS | **High** |
| Issuer (marketing) | "Minted by independent refineries and brokers in the Aurus Ecosystem", not by Aurus. Aurus positions itself as a technology provider, not an issuer | **High** |
| Issuer (registry) | **AURUS TECHNOLOGIES LTD, company no. 11703940, England and Wales**, incorporated 29 Nov 2018, previously **AURUSGOLD LTD** (to 26 Feb 2020). Registered office 5 Brayford Square, London E1 0SG. SIC 62012 (business and domestic software development) ([Companies House](https://find-and-update.company-information.service.gov.uk/company/11703940)) | **High** |
| Second entity | **AURUS FOUNDATION, company no. 14194058**, England and Wales, incorporated 24 Jun 2022, company limited by guarantee. **Active proposal to strike off**; accounts overdue ([Companies House](https://find-and-update.company-information.service.gov.uk/company/14194058)) | **High** |
| Domicile | **United Kingdom.** No Aurus issuing entity is registered in the UAE on any register located. Secondary sources list the issuer as Dubai-based: see §3, this is contradicted by the register | **High** |
| Backing claim | 1 tGOLD = 1 gram of 99.99% LBMA-accredited gold, sourced from LBMA / DMCC / LPPM accredited refineries, held by independent Vault Partners | **High** (issuer whitepaper) |
| Chains | Ethereum and Polygon. $AURUS launching on Base | **High** |
| Contract address(es) | tGOLD Ethereum `0xe4a6f23fb9e00fca037aa0ea0a6954de0a6c53bf`; tGOLD Polygon `0xa6da8c8999c094432c77e7d318951d34019af24b`; tSILVER Ethereum `0x34abce75d2f8f33940c721dca0f562617787bff3`; AurusX Ethereum `0xcb0d82f4dfa503c9e3b8abc7a3caa01175b2da39` ([CEX.IO migration notice](https://support.cex.io/en/articles/6701340-important-updates-for-aurus-tokens-awg-aws-awx)) | **High** |
| Supply | 43,322 tGOLD (43,322 g gold, ~1.39 tonnes… see §9 for the reconciliation problem) | **High** (on-chain) |
| Market cap / TVL | **$7.10M total protocol TVL** (28 Jul 2026), of which tGOLD ~$5.6M and tSILVER ~$1.5M ([DefiLlama](https://api.llama.fi/protocol/aurus)) | **High** |
| Regulatory status | **No licence found on any register.** Not FCA authorised or FCA cryptoasset-registered. No VARA, DMCC, ADGM, MAS or MiCA authorisation found. See §3 | **High** (as a negative finding) |
| Subscription fee | **0.5% minting/tokenization fee** on tGOLD (1.0% for tSILVER/tPLATINUM). Paid by the Provider Partner minting, not by the retail buyer | **High** |
| Ongoing custody fee | **Zero.** "No storage fees for Aurus tokens", explicit in the whitepaper. This is a deliberate design choice: see §7 and §12 | **High** |
| Redemption fee | **1.5% burn fee for tGOLD** (3% for tSILVER/tPLATINUM), paid by the Provider Partner executing the vault extraction, plus that Provider's own margin and the vault's shipping/handling. Retail redemption cost is therefore **not a published number** | **High** on the burn fee, **Not disclosed** on the all-in retail cost |
| Advertised yield | Not on tGOLD. tGOLD holders earn nothing. Yield is on the **separate** ecosystem token (AX/$AURUS), funded by tGOLD fees | **High** |
| Named officers | **Guido Jean-Paul van Stijn** (director from 29 Nov 2018, Dutch, **resident in the UAE**, correspondence address Marina Plaza 2307, Dubai); **Mark Nicolas Gesterkamp** (director from 3 Jan 2020, Dutch, resident Netherlands); **Dan Cristian Cearnau** (secretary from 4 Jan 2020, Romania) ([Companies House officers](https://find-and-update.company-information.service.gov.uk/company/11703940/officers)) | **High** |

---

## 1. What it is

Aurus is a **tokenization protocol that does not itself issue tokens**. It supplies smart contracts, an app and an API to licensed bullion businesses, who mint tGOLD, tSILVER and tPLATINUM against metal they own and place with an approved vault. Each tGOLD is 1 gram of 99.99% LBMA-accredited gold.

The whitepaper is explicit that this is the point of difference: "Aurus provides Tokenization-as-a-Service... to qualified commodity providers who account for an estimated 30% of the precious metals market. Now, these established businesses can mint and distribute their own precious metal-backed tokens, earning passive rewards from the trading activity."

Three partner roles exist, and the distinction between them matters more than any other fact in this profile:

- **Provider Partners** (bullion traders): supply and own the metal, initiate minting, run arbitrage, and execute redemptions.
- **Vault Partners** (vaults): custody and insure the bullion, audit intake, authorise minting.
- **Distributor Partners** (physical bullion retailers, i.e. the reseller tier): sell tokens to end customers through APIs and website plugins.

Aurus itself is a software vendor. The value proposition to the market is that a local bullion dealer keeps its own customers, brand and pricing rather than losing them to a centralised competitor like PAX Gold. That is the closest structural analogue to Aurumix's agent network in this landscape, which is why §10 and §12 carry the weight here.

## 2. Legal structure

**What a holder owns is asserted clearly, but nowhere contractually.** This is the central legal gap.

The whitepaper asserts unallocated-to-allocated title in strong terms: "Aurus company has no claim on precious metals allocated to the system. Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders. The bullion is stored physically by independent Vault Partners on behalf of the token holder. Token holders have the right to withdraw their bullion from a Vault Partner."

The problem is the document carrying that promise. The only legal document published on aurus.org is a four-page **Terms and Conditions dated 6 November 2024** ([PDF](https://aurus.org/Terms%20and%20Conditions%2012Nov2024.pdf)), and it is a **website terms of use, not terms of issue**. Read in full, it:

- **Names no contracting entity at all.** No company name, no number, no registered address anywhere in the document.
- **Contains no governing law or jurisdiction clause.**
- **Says nothing about gold, title, vaults, redemption, or fees.** Not one of these words appears.
- Disclaims custody generally: "AURUS itself does not custody or control user tokens."
- Disclaims the partners who actually do the work: "The website includes information, products, and services offered by third-party companies building on the AURUS ecosystem. Each product or service may be subject to separate terms and conditions. AURUS does not take responsibility for the content or accuracy of these third-party offerings."
- States: "**AURUS tokens are not securities, digital currencies, or any other form of financial instrument as defined by applicable laws.**" That is a self-serving legal conclusion asserted by an unnamed party, not a regulatory determination.
- Describes Aurus as "a decentralized DeFi platform" whose operations "align with DAO principles."

So the chain of title runs: holder → (no contract) → Provider Partner who owns the metal → (no published contract) → Vault Partner. **The holder's claim on the gold rests on a marketing whitepaper and on bilateral agreements between Aurus and its partners that are not published.** Where the whitepaper and the legal document disagree, the legal document does not merely disagree, it is silent, and silence gives the holder nothing to sue on.

**Confidence: High** that no terms of issue exist. Searched aurus.org, the whitepaper, the T&C PDF, and the tGOLD product page.

**Not disclosed:** the Provider Partner agreement, the Vault Partner agreement, and the Distributor Partner agreement. These are the documents that would actually govern the network, and none is public.

## 3. Regulatory and compliance posture

**No licence was found on any register.** Specifically checked and not found:

- **UK FCA:** no authorisation and no cryptoasset (MLR) registration for Aurus Technologies Ltd or Aurus Foundation. Aurus Technologies Ltd files at Companies House under SIC 62012, **software development**, which is consistent with a firm that has deliberately structured itself as a technology vendor rather than a financial institution.
- **UAE VARA, DMCC, ADGM:** no registration found. The whitepaper's only DMCC reference is that metal is sourced from *DMCC-accredited refineries*, which is a refinery accreditation, not a licence held by Aurus.
- **MAS, EU MiCA:** none found.

**Contradiction to flag.** The RWA data platform readi.fi records the tGOLD issuer as located in **Jumeirah, Dubai, UAE** ([readi.fi](https://readi.fi/asset/commodities-tgold-tgold-by-aurus/)). The corporate register says otherwise: the operating entity is an English company at 5 Brayford Square, London. The likely explanation is the founder-director Guido van Stijn's UAE residency and Dubai correspondence address on the Companies House record. **This is exactly the failure mode the brief warns about (the ORO case): a Dubai-appearing protocol that is in fact registered elsewhere.** Treat any "Aurus is a Dubai gold token" claim as false at entity level, while noting that its most senior director does operate from Dubai.

**The regulatory perimeter is the business model.** Aurus's answer to regulation is not to hold a licence but to **push the regulated activity onto its partners**. The regulated acts (owning bullion, custody, selling to consumers, KYC/AML, physical redemption) are all performed by "established and licensed" Provider, Vault and Distributor Partners in their own jurisdictions under their own licences. Aurus supplies the code. This is a coherent structure and it is cheap, but it means **no single regulator supervises the tGOLD product end to end**, and no regulator has approved the "you own the gold" claim in §2.

**Aurus Foundation is not an independent standards body.** It markets itself as the "global advocate for the international tokenized precious metals standards of tXAU and tXAG" and as the certifier of Distributor Partners. The register shows it is a company limited by guarantee whose **person with significant control is Aurus Technologies Ltd** (PSC filing 3 Jul 2025), i.e. a wholly controlled subsidiary, and that it received a **first Gazette notice for compulsory strike-off on 2 June 2026**, suspended on 16 July 2026, with accounts overdue since 31 March 2026 ([filing history](https://find-and-update.company-information.service.gov.uk/company/14194058/filing-history)). A certification body that is (a) owned by the company it certifies for and (b) two weeks from dissolution is not a governance safeguard.

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian | Multiple independent "Vault Partners", deliberately decentralised. **No vault company is named anywhere in the whitepaper or on the site.** | **Not disclosed** (names) |
| Vault / city | "Partnered, fully-audited, and insured vaults across the globe." No country or city list published. One secondary source mentions Switzerland as an example. | **Not disclosed** |
| Allocated? | Asserted: bullion "will always remain legal ownership of the token holders", stored "on behalf of the token holder", with tokens "backed by individual gold, silver and platinum bars linked to unique serial numbers". No trust deed or bailment agreement published. | **Medium** (issuer assertion only) |
| Bar list | **Not published.** The whitepaper says bars are linked to unique serial numbers internally; no public bar list exists. | **Not disclosed** |
| PoR feed | **Chainlink Proof of Reserve is announced but NOT live.** The tGOLD page says Aurus "is collaborating with Chainlink oracle to implement Proof-of-Reserves"; the Aurus Foundation site describes it as "in the works and coming soon". No PoR feed address found on Chainlink's data feeds. The site does display a self-reported "Current reserve" figure. | **High** (that it is not live) |
| Reserve audit | **No named auditor, no attestation report, no frequency.** The whitepaper requires that bullion "is audited, stored and accepted by approved Vault Partners" and mentions "an independent auditor" confirming quality on deposit, but no attestation is published and no audit firm is named. | **Not disclosed** |
| Smart contract audit | **NonceBlox**, in connection with the November 2022 contract migration. The report itself is not linked publicly. | **Medium** |

**The audit/attestation distinction matters here and Aurus blurs it.** The word "audited" appears repeatedly across Aurus marketing ("fully-audited and insured vaults", "audited smart contracts"). A reader skims that and concludes reserves are independently verified. They are not. What exists is: (a) a smart-contract audit by NonceBlox, which says nothing about gold, and (b) vault-level internal audit obligations imposed by contract on unnamed partners, with no public output. **There is no independent reserve attestation for tGOLD.** For a $5.6M gold product this is arguably proportionate, but it is a real gap versus Tether Gold's BDO reasonable-assurance engagement.

## 5. Issuance

Issuance is partner-driven and permissioned at the business layer, not the token layer:

1. A **Provider Partner** (a licensed bullion trader, vetted by Aurus, described as "professional bullion traders of the highest integrity") sends bullion from an LBMA/DMCC/LPPM-accredited refinery to an approved **Vault Partner**.
2. The Vault Partner receives, audits and accepts the bullion, and authorises minting. Minting cannot occur without vault confirmation.
3. tGOLD is minted 1 token per gram. A **0.5% tokenization fee** is charged at mint (1.0% for silver and platinum).
4. The Provider Partner, who owns the metal and now the tokens, sells them into the market or through Distributor Partners.

Supply is therefore elastic and provider-led, and expands only when a bullion trader judges tGOLD to be trading at or above NAV plus 0.5%. Retail buyers never mint: they buy existing tokens from a distributor or exchange. Aurus explicitly states it "does not supply precious metals to the ecosystem nor sell tokens to end consumers."

## 6. Redemption

**Physical redemption exists and is a genuine product feature**, in contrast to Aurumix. Terms:

- The holder burns tokens and requests a vault extraction through a **Provider Partner** or an Aurus-partnered dealer, choosing from bars or coins on offer.
- **Burn fee: 1.5% for tGOLD**, 3% for tSILVER/tPLATINUM. The whitepaper is precise that this is charged to the **Provider** executing the extraction, not directly to the user: "For users, the fees for users redeeming physical gold, silver or platinum is dependent on the Provider Partner that is facilitating the exchange."
- Plus shipping and handling charged by the vault.
- **KYC/AML is performed by the Vault Partner** before withdrawal.
- The older AWG whitepaper documented a 10-day claim window with a bilateral "handshake" signature between holder and vault, after which the transaction auto-cancels and tokens return, fees non-refundable.

**Two caveats worth carrying into §12.** First, the *retail* redemption cost is undisclosed and unbounded: the user pays whatever the Provider Partner chooses to charge, so the 1.5% is a wholesale floor, not a consumer price. One RWA platform records a **3.00% redemption fee** for tGOLD ([rwa.xyz](https://app.rwa.xyz/assets/TXAU)), roughly double the whitepaper's burn fee, which is consistent with the Provider adding margin. Second, the whitepaper openly states that **Distributor Partners can redeem large quantities at lower per-unit fees than retail holders and resell** (§4.4.4). Redemption economics are explicitly tiered in favour of the trade.

**Minimum redemption increment: Not disclosed.** In practice it is bounded by the smallest bar or coin a given dealer offers.

## 7. Fees and revenue model

Fees are levied on the metal tokens; the ecosystem token (AX/$AURUS) carries none.

| Fee line | Rate | Paid by | Received by |
|---|---|---|---|
| Tokenization / minting (tGOLD) | **0.5%** | Provider Partner at mint | Fee pool, then split (below) |
| Tokenization / minting (tSILVER, tPLATINUM) | **1.0%** | Provider Partner | Fee pool |
| Transaction fee | **0.18%** | Initiator of each transfer | Fee pool |
| Storage / custody | **0%** | Nobody | n/a |
| Burn / withdrawal (tGOLD) | **1.5%** | Provider Partner executing extraction | Fee pool |
| Burn / withdrawal (tSILVER, tPLATINUM) | **3%** | Provider Partner | Fee pool |
| Retail redemption markup | **Not disclosed**, set by each Provider Partner | End user | Provider Partner directly |
| Vault extra services (delivery etc.) | **Not disclosed**, vault's own price, payable in tokens or fiat | End user | Vault Partner directly |
| Distributor spread | **Not disclosed**, distributor sets its own retail price | End user | Distributor Partner directly |
| Gas | Network rate | Transferor | Validators |

**The distribution of the fee pool is the most useful disclosure Aurus makes.** From the whitepaper, verbatim: "All accumulated transaction, minting and burning fees are distributed back to the ecosystem as follows: **50% of tGOLD fees to AurusX holders, and 50% to Aurus minting partners (25% Vaults, 25% Providers)**. With tSILVER and tPLATINUM **30% goes to AurusX holders, and 70% to minting partners (35% Vaults, 35% Providers)**."

Vault rewards are paid **quarterly, in metal tokens**, pro rata to grams stored, by published formula: `Vault reward = Total quarterly fees × (grams stored by vault ÷ total supply) × 0.25`.

Two things follow, and both are important for Aurumix:

1. **Aurus Technologies Ltd takes no disclosed share of the fee pool.** 100% of tGOLD fees are accounted for: 50% + 25% + 25%. How the software vendor is funded is **Not disclosed**. Candidates are partner onboarding/licence fees, an AX treasury allocation, or equity funding, but none is published. This is a genuine hole in the disclosed model.
2. **The split has changed at least three times.** Documented versions: 70% AWX / 15% providers / 15% vaults (2019–2020 AWG era); 50% AWX / 25% / 25% for gold (current whitepaper); and a March 2021 press description of "50% (25% each) to providers and vaults, 50% to AurusDeFi holders." The whitepaper reserves the right to keep changing it: "All fees on the Aurus ecosystem are subject to change... Fees will be reviewed on a regular basis and can be amended accordingly", with only a soft promise that values will be "capped through Smart Contracts". The 2022 migration to **upgradeable contracts** explicitly enabled "adjustable fees". **Partner economics here are revocable by the operator.**

## 8. Token architecture

- **Standard: plain ERC-20**, 18 decimals, on Ethereum and Polygon. The whitepaper states "All Aurus metal tokens are ERC-20 tokens 1:1 backed by 1 gram." Aurus explicitly compares itself favourably to competitors on free transferability.
- **Permissioned? No.** No whitelist, no ERC-3643, no transfer restrictions found. Tokens move freely between anonymous wallets and trade on a DEX. **Permissioning sits entirely at the fiat on-ramp and the redemption gate** (KYC by the distributor at purchase, KYC by the Vault Partner at withdrawal), not in the token contract.
- **Upgradeability: yes, and material.** The November 2022 migration deliberately moved to "upgradeable smart contracts, enabling the seamless implementation of features such as proof-of-reserves, governance, and **adjustable fees**." Admin keys and multisig arrangements are **Not disclosed**. Combined with §7, the operator can change partner revenue shares by contract upgrade.
- **Inheritance feature:** a multisig mechanism lets holders transfer tokens to heirs via lawyers acting as trustees or under power of attorney, with a reversal window. Directly comparable to Aurumix's Digital Will.
- **Bridge:** Ethereum ↔ Polygon; $AURUS is launching on Base. Bridge design and custody are **Not disclosed**.
- **Historic:** the original AWG design also used **ERC-721 "Gold Bullion Tokens"** mapped 1:1 to physical bars with LBMA serial numbers, metadata on IPFS. Whether this survives in the current tGOLD contracts is **Not disclosed**, and no public bar list is exposed from it.

## 9. Liquidity and market

This is where the model looks weakest, and it replicates the PGOLD pattern the brief already established.

- **Protocol TVL: $7.10M** (28 Jul 2026), Ethereum only, split ~$5.6M tGOLD and ~$1.5M tSILVER ([DefiLlama](https://api.llama.fi/protocol/aurus)). TVL has drifted down over the last three days ($7.24M → $7.14M → $7.10M).
- **tGOLD Ethereum total supply: 43,322 tokens = 43.3 kg of gold.** Holders: 466 ([rwa.xyz](https://app.rwa.xyz/assets/TXAU)).
- **On-chain DEX liquidity is effectively zero.** The only live pools found: TGOLD/USDT0 with **$3,126 of liquidity and $211 of 24h volume**, and a Solana TGOLD/SOL pool with **$1.71 of liquidity and $0 volume** (GeckoTerminal API, 28 Jul 2026). The Ethereum tGOLD contract shows **$0.00 24h volume** and only ~$59 of pooled reserve.
- Trading is therefore essentially **off-chain and dealer-mediated**: CEX.IO (centralised), QuickSwap, and bullion distributors Direct Bullion, Aurica Group and AgaBullion.

**Reconciliation problem to flag.** The aurus.org tGOLD page displayed a "current reserve" of **73,398.5 g** while the Ethereum contract shows **43,322 tokens**. The gap is plausibly Polygon supply plus tSILVER/tPLATINUM accounting, or a stale figure, but **the issuer publishes no reconciliation** and there is no live PoR feed to settle it. A ~30 kg discrepancy in a self-reported reserve number, with no attestation, is exactly the kind of item a PoR feed exists to close.

**Verdict on the premium thesis: Aurus is evidence against it.** Roughly $5.6M of gold has been accumulated over seven years (since 2018) with a market so thin that a $211 daily volume is the *main* on-chain pool. Aurus's own answer is not exchange liquidity at all: it is Provider Partner arbitrage against the OTC bullion market. That works to hold the peg *at NAV*, but by construction it **destroys any sustained premium**, because any premium above NAV + 0.5% is immediately minted into by a provider. Aurus is architecturally designed to trade at par, not at a premium.

## 10. Distribution

This is the section most relevant to the client, and Aurus is the only protocol in this set with a formal multi-tier reseller network.

**Channel structure.** Three contracted tiers (Provider, Vault, Distributor) plus exchanges. **Distributor Partners** are the reseller tier: "established and licensed physical bullion retailers that consumers trust." They are certified by the Aurus Foundation (see §3 for what that certification is actually worth).

**What distributors get.** From whitepaper §4.4:

- **APIs and plugins.** A REST API and a website plugin so a dealer can buy and sell tGOLD from its own site to its own client list. Aurus supplies the rails; the dealer keeps the customer relationship.
- **Own pricing.** "All Aurus Distributor Partners certified by the Aurus Foundation will be able to integrate Plugins and APIs that allow them to **buy and sell Aurus tokens at their own prices** and according to their own supplies."
- **Preferential redemption.** They can withdraw large amounts at lower per-unit fees than retail holders, then resell, and can offer delivery services at their own price.
- **Upgrade path.** A Distributor can graduate to Provider Partner, tokenize its own inventory and access the arbitrage and the 25% fee share.

**How distributors are compensated: this is the finding.** **Distributor Partners receive no share of the protocol fee pool.** The tGOLD split is 50% AurusX holders / 25% Vaults / 25% Providers, which is fully allocated. The reseller tier earns **only its own retail markup and its own service charges**, set by itself, disclosed by nobody. There is **no commission, no override, no residual, and no multi-level structure**: a Distributor's earnings do not depend on recruiting other Distributors, and no partner earns from another partner's volume. Compensation is a **merchant margin model, not an agent commission model.**

**Recurring purchase / savings plan: none found.** No SIP, no monthly contribution plan, no auto-invest, no direct debit. Purchases are one-off, dealer-mediated. Consistent with the brief's expectation that most protocols lack this.

**Referral / affiliate: none found** at the protocol level for retail users.

**Rewards, but not for gold holders.** Aurus does pay recurring income, just not to the people who own the gold. AX holders receive **monthly** distributions in tGOLD and tSILVER from the fee pool. The migration to $AURUS (see §11) restructures this toward staking and liquidity-pool incentives on Base.

**Target segments and geography.** B2B2C. Aurus sells to bullion businesses; those businesses sell to their own retail clients. Named partners span the UK (Direct Bullion), Chile (Aurica), Spain (Sempsa JP, an LBMA refinery), Singapore (Indigo Precious Metals), Turkey, and AgaBullion. **Excluded jurisdictions are significant**: the T&C bars users from the USA and its territories, Russia, Belarus, Cuba, Iran, Iraq, North Korea, Syria, Sudan, South Sudan, Yemen, Zimbabwe, Myanmar, DRC and Crimea, and imposes a UK-specific gate requiring users to confirm they are "Professional Investors" or high-net-worth individuals to access certain features. **India is not excluded.**

## 11. Recent developments

- **28 July 2026 (today):** protocol TVL $7.10M, declining slightly over the preceding three days. tGOLD Ethereum 24h DEX volume $0.00. Aurus remains operating ([DefiLlama](https://api.llama.fi/protocol/aurus)).
- **16 July 2026:** Companies House records **"Compulsory strike-off action has been suspended"** (DISS16(SOAS)) for Aurus Foundation ([filing history](https://find-and-update.company-information.service.gov.uk/company/14194058/filing-history)).
- **17 June 2026:** Aurus Technologies Ltd confirmation statement became **overdue** (due 17 June 2026) ([Companies House](https://find-and-update.company-information.service.gov.uk/company/11703940)).
- **2 June 2026:** **First Gazette notice for compulsory strike-off** issued against Aurus Foundation, the body that certifies Distributor Partners.
- **31 March 2026:** Aurus Foundation accounts for period ending 30 June 2025 became overdue; still not filed.
- **Q1 2026:** sector context only. Tokenized gold reached ~$5.6B market cap, adding ~$1.3B in the quarter ([CEX.IO Q1 2026 report](https://blog.cex.io/ecosystem/tokenized-gold-q1-2026-report-35490)). Aurus's ~$5.6M tGOLD is roughly **0.1% of that sector**, i.e. Aurus did not participate in the sector's growth.
- **22 May 2025:** **Omega Minerals partnership** to tokenize up to **1 million troy ounces of unmined, in-ground gold** at the Alice Creek property, British Columbia, as a **CGR token**, launching with 1M tokens against 25,000 troy oz, priced at $35 (COMEX spot less all-in sustaining cost). Sold via pre-sale to accredited/HNW investors at aurus.org/omega, with a 0.5% minting fee to the Aurus Protocol Vault ([OurCryptoTalk](https://ourcryptotalk.com/news/aurus-to-tokenize-1-6b-gold)). **This is a categorically different and much riskier product than tGOLD: it is tokenized mineral reserve, not vaulted metal**, and it should not be conflated with tGOLD's backing.
- **~March–April 2025:** **$AURUS Token Generation Event** and migration from AurusX (AX), on the **Base** network. Two-thirds of AX supply (20,000,000 tokens) burned in weekly 5,000,000 tranches down to 9,999,999 AX. Staked AX earns tiered $AURUS: 15 $AURUS per AX for the first 2M staked, 8 for the second 2M, 4 above 4M. AX must be staked before TGE to keep claiming monthly gold/silver rewards ([Mitrade, 6 Mar 2025](https://www.mitrade.com/insights/news/live-news/article-3-680539-20250306); [aurus.org/aurusx](https://aurus.org/aurusx)).
- **$AURUS model change (undated, current on site):** the new token introduces "algorithmic token issuance", automated burns, 50% of supply distributed in the first 24 months, single-staking, and **Core Protocol Fees collected in a new "cGOLD" token** from minting/burning and transfer fees, directed partly to liquidity pools ([aurus.org/$aurus](https://aurus.org/$aurus)). **This appears to redirect fee flows away from the clean 50/25/25 whitepaper split toward LP incentives, but no updated whitepaper documents the new split.**
- **6 November 2024:** current Terms and Conditions published (the four-page website terms discussed in §2).
- **9 November 2022:** network upgrade. AWG→tGOLD, AWS→tSILVER, AWX→AurusX, migrated 1:1 to new **upgradeable** contracts audited by **NonceBlox**, adding proof-of-reserves capability, governance and **adjustable fees**.

**Not found:** any confirmed live Chainlink PoR feed; any reserve attestation; any enforcement action against Aurus; any security incident or exploit.

## 12. Relevance to Aurumix

Aurus is the closest structural analogue to Aurumix's distribution model in this landscape, and it is instructive mostly by contrast. It answers questions 1, 3, 5, 6, 7, 8 and 9.

**Q8, distribution: the single most useful finding. A multi-tier partner network can be built without a commission structure, and Aurus's tiers are compensated for capital and custody, not for selling.** The three tiers are *functional*, not *hierarchical*: Providers supply metal, Vaults hold it, Distributors sell it. Fees flow to the first two (25%/25%) and to token holders (50%). **The selling tier gets nothing from the pool.** It earns its own markup on its own client list, and Aurus's pitch to it is defensive ("you will lose customers to PAX Gold if you don't") rather than an income promise.

This cuts directly at the Aurumix design. Aurumix's 3-tier agent network is a *recruitment and commission* hierarchy where agents earn from downstream volume: economically an MLM, and regulators treat it as one. Aurus's is a *supply-chain* network where each tier is paid for a distinct economic function it actually performs. **The implication: if Aurumix can re-cast its tiers so each is paid for a function (capital introduction, custody, servicing) rather than for recruitment depth, it gets most of the distribution reach with materially less classification risk.** Aurus also shows the upgrade path (Distributor → Provider) as an alternative to override commissions for motivating the top tier: let the best agents graduate into a higher-margin role rather than paying them a slice of their recruits.

Note also what Aurus does *not* have: **no savings plan, no recurring contribution, no SIP, no auto-invest, no referral scheme.** Aurumix's monthly SIP remains genuinely differentiated. Aurus's absence of it is likely why it accumulated only ~$5.6M in seven years: dealer-mediated one-off purchases do not compound. **The SIP is Aurumix's real edge, and this profile is evidence for that, not against it.**

**Q1, custody fee: Aurus is the live example of "option three", charge holders nothing and recover cost elsewhere.** Storage is explicitly 0%. It is funded by **transaction and mint/burn fees paid predominantly by the trade, not by holders**: 0.5% at mint and 1.5% at burn, both borne by Provider Partners, plus 0.18% per transfer. The vault is compensated out of that pool (25%, quarterly, pro rata to grams stored, by published formula) rather than by deducting metal. **This is a clean, working answer to the peg-breaking problem: the custodian is paid from a fee pool in tokens, so no grams are ever deducted from the backing and price = grams ÷ tokens never breaks.** Aurumix should look hard at this. The caveat is that it only works if minting and redemption churn is high enough to fund the vault. With Aurus's volumes it plainly is not, which is why the model is being restructured around LP incentives and a new cGOLD fee token. **A buy-and-hold savings product like Aurumix generates almost no transaction fees by design, so Aurus's funding mechanism does not transplant directly: Aurumix's churn will be even lower than Aurus's.**

**Q2, dividend funding: Aurus confirms the anti-pattern, but is more honest about it than PGOLD.** Aurus pays recurring income (monthly, in metal) funded entirely from investor and trade fees, exactly the recycled-fees structure the brief flags. Two mitigations Aurumix should note: (a) the yield is paid on a **separate ecosystem token (AX/$AURUS)**, not on the gold token, so tGOLD is never marketed as yield-bearing and the gold product stays clean; and (b) Aurus never promises a rate. There is no "5% APY" claim to fail. It distributes a *share of whatever fees actually arrive* (50% of tGOLD fees), which is structurally honest and cannot be arithmetically falsified. **If Aurumix keeps the ICS Dividend, expressing it as "X% of realised operating profit" rather than a headline yield, and separating the entitlement from the gold token, follows Aurus's safer path.** Aurumix's current design already does the first; it does not do the second, because ICS standing rides on the gold token itself.

**Q3, token standard: Aurus is the counter-example.** Plain ERC-20, freely transferable, no permissioning, and it works precisely because a tGOLD token carries **nothing but a claim on a gram of gold**. All the identity-dependent logic (KYC, eligibility, redemption rights) sits at the dealer and vault boundary, off-chain. Aurumix cannot copy this: AURX carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous transfer. **This strengthens the case for a permissioned base (ERC-3643).** But Aurus also shows the cost of that choice: free transferability is what lets Provider Partners arbitrage tGOLD to NAV. A permissioned Aurumix token cannot be arbitraged by third parties, so **Aurumix must be the market maker of last resort for its own token, and should budget for it.**

**Q5, redemption: Aurus offers physical redemption and it is a real gap for Aurumix, but a smaller one than it appears.** Aurus's redemption is genuine (burn, extract, KYC by vault) yet costs 1.5% wholesale, ~3% as observed retail, plus shipping, plus an undisclosed Provider markup, and requires collection or delivery from an unnamed vault in an undisclosed city. **The lesson: a redemption right whose all-in cost is undisclosed and set by an intermediary is not obviously superior to Aurumix's honest "cash buyback only".** Aurumix's position is defensible if stated plainly. What Aurus does better is that *someone* will hand you metal; Aurumix should be careful never to imply the same. Also note Aurus's explicit tiering of redemption economics in favour of the trade: that is a fairness disclosure Aurumix would be criticised for.

**Q6, premium: Aurus is further evidence against the 3–8% premium thesis, and explains the mechanism.** $5.6M of gold, 466 holders, and $211 of daily on-chain volume after seven years. More importantly, Aurus's peg is *maintained by design* through provider arbitrage against OTC bullion, which structurally caps the price at NAV plus the 0.5% mint fee. **Any tokenized gold product with an open mint path cannot sustain a premium**: the premium is the arbitrage signal that creates new supply. Aurumix's premium thesis therefore depends on *not* having an open mint, i.e. on supply discipline, which sits uneasily with "no hard cap" and continuous SIP inflows. This deserves explicit attention in mechanism design.

**Q7, proof of reserve: a cautionary example of "audited" doing too much work.** Aurus says "fully-audited and insured vaults" and "audited smart contracts" while having no named reserve auditor, no attestation, no bar list, no live PoR feed, and a self-reported reserve number (73,398.5 g) that does not obviously reconcile to on-chain supply (43,322). **Aurumix should publish a named attestor, a frequency, and a reconciliation from day one**, because this is cheap differentiation against exactly this pattern, and because the on-chain-supply-versus-claimed-grams reconciliation *is* the peg for a price = grams ÷ tokens design.

**Q9, wind-down: Aurus is the only protocol in this set with anything resembling a documented failure plan, and it is worth copying.** Two provisions: (a) **vault exit**, "If a Vault Partner is unable to continue being a Vault Partner, they are required to transport all bullion to another partner vault. Said Bullions will continue to belong to token holders during this process"; and (b) **issuer failure**, "Aurus company has no claim on precious metals allocated to the system. Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders." That is a genuine ex-ante answer to "what happens to the gold if the issuer fails", and it is **more than PMGT, Digix or Cache Gold ever published**. The weakness is that it lives in a whitepaper, not in the terms, and there is no trust deed to enforce it. **The lesson for Aurumix: the commitment is cheap and differentiating, but it must sit in the terms of issue with a named trustee, not in a whitepaper.** Aurumix has an additional problem Aurus does not: Aurus's gold is owned by Provider Partners and held bankruptcy-remote from the software company by design, whereas Aurumix intends to own the vault gold itself and lend against it at 90–95% LTV, so Aurumix creditors would rank against the same gold. **Aurus's structural separation of the technology company from the metal owner is the single cleanest idea in this profile.**

**Contradictions to record.** Nothing here contradicts the established findings on PGOLD, ORO, PMGT, Digix or Cache Gold. Two corrections to inherited framing about Aurus specifically: (1) **Aurus is a UK company, not a Dubai one**, despite at least one RWA data platform recording it as Jumeirah, Dubai, and despite its founder-director residing in Dubai. Same failure mode as ORO. (2) **Aurus does not issue tGOLD**, so describing it as a competing gold-token issuer is wrong; it is a software vendor to issuers, and its "AUM" is its partners' metal.

## 13. Open items for verification

- [ ] Obtain a **Distributor Partner agreement** and a **Provider Partner agreement**. These are the documents that would show whether resellers receive any commission beyond markup, and whether Aurus charges partners an onboarding or licence fee. Approach via a listed distributor (Direct Bullion, AgaBullion, Aurica Group) rather than Aurus.
- [ ] Determine **how Aurus Technologies Ltd is actually funded**, given it takes 0% of the disclosed fee pool. Check the Companies House accounts filed for period ending 30 November 2024 for revenue lines and related-party income.
- [ ] Confirm whether the **$AURUS / cGOLD restructuring changed the 50/25/25 split** and whether Vault and Provider Partners still receive 25% each. Request the current $AURUS tokenomics paper; the site describes LP-directed fee flows with no published split.
- [ ] Verify whether a **Chainlink PoR feed for tXAU is live** as at Q3 2026, and if so capture the feed address and update frequency.
- [ ] Reconcile the **73,398.5 g self-reported reserve against 43,322 tGOLD on Ethereum**. Obtain the Polygon supply and confirm whether the site figure aggregates metals or is stale.
- [ ] Identify at least one **named Vault Partner and its city**, and establish whether any independent reserve attestation is provided to partners privately even though it is not published.
- [ ] Check the **FCA register directly** (register.fca.org.uk was not machine-readable in this pass) for any Aurus entity, and check whether any UK Distributor Partner holds FCA cryptoasset registration that effectively covers tGOLD sales.
- [ ] Monitor **Aurus Foundation (14194058)**: strike-off was suspended 16 July 2026 and accounts are overdue. If it dissolves, the body that certifies Distributor Partners disappears. Establish who then certifies resellers.
- [ ] Establish the **actual all-in retail redemption cost** by requesting a quote from a Distributor Partner for a small redemption (e.g. 100 g), to test the gap between the 1.5% burn fee and the ~3% recorded figure.
- [ ] Obtain the **NonceBlox smart-contract audit report** and confirm admin key / upgrade authority arrangements on the upgradeable tGOLD contracts, specifically who can change fees.
- [ ] Clarify the status of the **Omega Minerals CGR token** (in-ground gold): whether it launched, whether it is marketed alongside tGOLD, and whether any tGOLD reserve is or could be commingled with mineral-reserve backing.
