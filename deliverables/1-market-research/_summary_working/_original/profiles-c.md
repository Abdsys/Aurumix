### 4.9 Digital Gold (DGLD)

| Field | Detail |
|---|---|
| Issuer | Gold Token SA (GTSA), CHE-287.630.262, Swiss société anonyme incorporated 8 August 2018, seat Carouge, Geneva, share capital CHF 3,401,100. Wholly owned by MKS PAMP SA (CHE-105.871.847) since 20 November 2025 |
| Licence covering the token | None identified. No FINMA authorisation. AML affiliation to VQF, a FINMA-supervised self-regulatory organisation; membership number not published. The commercial register authorises the company's purpose as "l'émission et la commercialisation de jetons virtuels... adossés à des matières premières physiques" |
| Assets under management | ~$8.1M, being ~2,004.85 DGLD (~2,005 troy ounces) at 28 July 2026. Split 1,603.69 Ethereum, 401.16 Base |
| Backing | 1 DGLD = 1 fine troy ounce of LBMA-certified PAMP gold, allocated to specific bars, vaulted in Switzerland by MKS PAMP. Co-ownership and indirect possession under Swiss Civil Code arts. 646 and 919 |
| Custody fee charged to holders | 0%. Costs are "embedded in DGLD"; "Tokenholders are not charged any separate or additional fees" |
| Yield paid to holders | None. The terms disclaim "any financial return, interest, dividend, claim for repayment" |
| Redemption | Anyone with power of disposal over the tokens. Minimum 1 gram. 0.20% burning fee plus third-party shipping, insurance and customs at cost. One-time KYC at delivery only |
| Token standard | Plain ERC-20 on Ethereum and Base, freely transferable, no whitelist. Both contracts redeployed March 2026 |
| Reserve verification | Per-wallet tool at dgld.ch/verify returns PAMP bar serial numbers, refinery dates and vault locations from 0.001 DGLD upward. No named-firm reserve attestation published. Smart-contract audits by Hacken and Halborn, March 2026 |

#### What it is

DGLD is a one-token-one-ounce gold token issued by Gold Token SA, now the wholly owned tokenisation arm of MKS PAMP, one of the largest precious-metals refining and vaulting groups in the world. The gold is PAMP-refined, LBMA-certified, allocated to specific bars, held in Swiss vaults.

Its history runs in three phases. It launched on 15 October 2019 with roughly $20M of gold, assembled by a consortium of CoinShares International, MKS SA and Blockchain.com, on Ocean, a Bitcoin sidechain built by CommerceBlock on the Blockstream Liquid codebase. Each token was one-tenth of an ounce then. It migrated to Ethereum in November 2022 as a native ERC-20, then went quiet for three years. On 20 November 2025 MKS PAMP acquired 100% of the issuer, deployed on Base on 16 December 2025, and restarted the token with professional market-making and a live retail redemption path.

MKS PAMP chief executive James Emmett has called the 2019 launch "too early" and the token mostly dormant for six years. The dormancy was real: backers left, share capital was cut from CHF 4,668,500 to CHF 3,401,100 in April 2024, nothing material was announced between 2022 and 2025. At ~$8.1M it is one of the smallest protocols here. It earns a full profile because its legal structure is the strongest of the nineteen, and its dormancy is the clearest evidence in the set of why that matters.

#### Legal structure and regulatory standing

The General Terms and Conditions state the holder's position in unusually direct language. The token "qualifies as a title of proof (art. 8 CC)". Holders acquire "co-ownership rights (art. 646 CC) and indirect possession (art. 919 CC) over the Gold". And, decisively: "Title to and ownership in Gold shall at all times remain with the Tokenholder."

The negative limb is equally explicit. DGLD "does not however represent claims such as a debt or equity claim or other financial claim against GTSA", and "does not confer any financial return, interest, dividend, claim for repayment".

A holder is therefore not a creditor. They co-own a pool of specific bars under Swiss property law, with GTSA and the custodian holding as indirect possessors on their behalf. Token transfer is constructed as transfer of the co-ownership right, the custodian "deemed to be validly notified of the transfer... via the change of records in the Blockchain". In a GTSA insolvency a creditor claim would rank with other unsecured creditors and the gold would fall into the estate. A co-ownership right does not: it is third-party property to be segregated out.

Two qualifications. The terms contain no insolvency clause and cite neither the Swiss DLT Act nor art. 242a of the Debt Enforcement and Bankruptcy Act, which governs segregation of crypto-based assets in Swiss bankruptcy, so bankruptcy remoteness rests on inference from arts. 646 and 919 rather than an express recital. And the co-ownership is of a pool, not a nominated bar per holder. Whether a holder can compel delivery of a specific serial-numbered bar is not disclosed.

GTSA holds no FINMA licence and does not claim one. Its phrasing is that it is "regulated through VQF, a FINMA-supervised SRO". Accurate, and engineered to put FINMA in the sentence. VQF membership is an AML affiliation, the route a Swiss financial intermediary takes instead of direct FINMA supervision. It is not a licence, involves no product approval, and says nothing about reserve adequacy. One prominent data platform has compressed that wording into "supervised by FINMA", which is false, one hop from the issuer's own language. No enforcement action against GTSA or MKS PAMP was found. The company disclaims EU/EEA solicitation, permitting access on a reverse-solicitation basis only.

#### Custody and reserve verification

MKS PAMP holds the metal in its own Swiss vaults, refining at the PAMP SA plant at Castel San Pietro. The specific vault site is not disclosed. The gold is asserted to be allocated LBMA-certified PAMP bars, held in co-ownership at law rather than as a contractual claim.

The verification tool is unusual and strong. A holder enters a wallet address at dgld.ch/verify and gets PAMP bar serial numbers, refinery dates and vault locations for their own position, down to 0.001 DGLD. For a retail holder that beats a quarterly aggregate PDF.

DGLD inverts the pattern seen elsewhere, so separate the two forms of assurance. Smart-contract security is well evidenced: Hacken and Halborn were engaged after the February 2026 exploit and both reports are stated to have been released publicly in March 2026. Reserve verification is not. One aggregator names KPMG as auditor; that could not be confirmed from any GTSA source, and no reserve attestation report, named attestor or stated frequency was located. GTSA's own tool refers to "latest signed audits" without naming the signer. The tool is issuer-published data. It proves GTSA's records are internally consistent with the chain, not that an independent party counted bars. It also has exactly the lifespan of the issuer's hosting bill, and six dormant years show how fast issuer infrastructure goes quiet.

#### Fees, revenue and redemption

| Fee line | Rate |
|---|---|
| Subscription / creation | 0.20% |
| Ongoing custody / storage | 0% to the holder |
| Redemption / burning | 0.20% |
| Re-issuance | "Determined by GTSA before the process begins", unquantified |
| Physical delivery | Third-party transport, insurance and customs at cost. No GTSA surcharge "currently" |
| Transfer | None from the issuer, gas only |
| Yield to holders | None, expressly disclaimed |

The funding behind the zero custody fee is the cleanest in the set. MKS PAMP owns the vaults and the refinery, so storage is a marginal cost on infrastructure the group already runs. Vertical integration, not cross-subsidy from investor fees.

Two drafting points. Costs are "embedded in DGLD" with no statement of what that means operationally. If MKS PAMP absorbs the cost, nothing follows. If it is ever recovered from the gold backing each token, the ounce-per-token ratio drifts below one and the central claim breaks. No clause specifies which. And GTSA "does not currently charge any separate fee or surcharge" on delivery: that "currently" is a reserved right to start.

Redemption is the most retail-accessible here by a wide margin. Minimum 1 gram, from a token worth roughly $4,000, at 0.20% flat plus actual third-party shipping, insurance and customs. Email support@dgld.ch, get a quote within hours, complete one-time KYC in 5 to 10 minutes, transfer and pay, and European delivery follows in 3 to 7 business days by insured post. Eligibility is the important part: the right runs to any entity demonstrating "power of disposal over the relevant DGLD". Not the original subscriber, not accredited investors, no minimum ounce count. A buyer who acquired $130 of DGLD on Uniswap with no KYC can convert it into a physical gram of PAMP gold shipped to their door. GTSA reserves narrow rights to refuse or postpone for KYC/AML failure, ownership conflicts, suspected unlawful activity, or unlawful delivery.

Issuance runs on two tiers set far apart. Primary minting is restricted to accredited institutions, minimum subscription reported at 400 XAU (roughly $1.6M), 0.20% creation fee. Everyone else buys on Uniswap V4 or Aerodrome with no KYC. GTSA's guide states KYC "is entirely optional and only triggers" on a physical delivery request.

#### Liquidity and distribution

Daily volume is roughly $12,000 to $19,000 across three pools: Uniswap V4 DGLD/USDC and DGLD/XAUT on Ethereum at about $9,400 each, and a Base DGLD/USDC pool turning over about $27. Monthly transfer volume is around $3.8M across 3,323 transfers, about 113 active addresses. Turnover is roughly 0.2% of assets under management per day, thin even by this set's standards. Arrakis Finance actively manages the Aerodrome position against the real-world gold price to minimise slippage, and MKS PAMP's trading arm is the principal liquidity provider.

DGLD trades at $4,045 to $4,081 against LBMA gold of ~$4,004 (PM fix, 20 July 2026) and spot of ~$4,090 (27 July 2026): at or marginally below spot, no premium. A vertically integrated, refinery-owned, professionally market-made gold token with a 1-gram redemption right commands nothing over the metal. Holder count is up 32.5% over 30 days to roughly 3,962 across chains while volume stays tiny. That reads as accumulation, not trading.

On distribution there is nothing to report, and that is the finding. No savings plan, no recurring purchase facility, no referral or affiliate scheme, no agent network, no commission structure. Retail reaches DGLD only through decentralised exchanges. Emmett has described the target as crypto-wealthy individuals: "If you've made your money in crypto, you're very keen on having tokenized gold" and want to "stake it or leverage it". That is liquidity placement where crypto capital already sits, not customer acquisition. An issuer with 60 years of brand, its own refinery, its own vaults and the best redemption right in the market has accumulated ~$8M, because it has no mechanism to reach a saver who does not already hold crypto.

#### Relevance to Aurumix

DGLD is the counter-example that shows what good looks like. Weight it accordingly.

Six years of near-total dormancy harmed nobody. Backers left, capital was reduced, marketing stopped, and holders were fine. Compare Paxos's PMGT, switched off permanently under the same commercial pressure, and Cache Gold and Digix, which wound down. The difference is structural and traces to launch decisions. The gold was never encumbered or dissipated, because holders owned it outright at law under arts. 646 and 919: dormant DGLD was gold sitting in a vault with valid title, and a restart required nobody's permission. The custodian and the issuer ended up in the same economic group, so MKS PAMP could buy the issuer and own the full stack. The token never lost its backing, so old holders were not wiped out and the brand was not poisoned.

The transferable rule: a gold token's survivability is determined by whether the gold's legal position is independent of the operating company's fortunes. If Aurumix goes quiet for three years, what happens to the gold and to holders? If the answer depends on Aurumix being an operating, solvent, willing counterparty, and with a cash-buyback-only exit it currently does, then Aurumix has PMGT's fragility rather than DGLD's resilience.

The structure was tested under live stress and held. On 23 February 2026 a legacy `transferFrom` edge case in the Ethereum contract was abused through the Ethereum-to-Base bridge to mint over 100 million unbacked DGLD on Base, against a legitimate Base circulation of about 70.8 tokens. Contracts were paused within 2 hours 25 minutes. Economic impact was around $250,000, borne in very large majority by GTSA as principal liquidity provider. The gold was never at risk, because the fake tokens conferred co-ownership in nothing. Token supply and gold title are separate legal facts, and that separation is what protected holders. GTSA absorbed the loss, published a detailed post-incident report a month later, reset balances to a pre-exploit snapshot, redeployed both contracts, and opened a 45-day goodwill claims process for 180 affected addresses across 7,000-plus trades. Three lessons carry over: audit before deploying rather than after an incident, re-audit at the seam whenever new infrastructure is bolted onto existing contracts, and disclose in full.

DGLD is also one of only three protocols here with credible independent examination of any kind. Per-wallet, serial-number-level bar lookup is cheap to build and genuinely differentiating. Aurumix should build it and additionally commission the named third-party attestation DGLD appears to lack.

Four further read-acrosses:

- The dividend has a price, and DGLD shows what it is. DGLD pays nothing and expressly disclaims any debt or equity claim, financial return, interest or dividend. That disclaimer is what lets GTSA characterise DGLD as property under art. 8 CC rather than a financial claim, which keeps it outside securities and collective-investment regulation and lets it run on an AML affiliation instead of a licence. The most sophisticated legal structure in this set bought its regulatory simplicity by refusing yield. That does not make Aurumix's ICS Dividend wrong, but it prices it: the dividend converts a property instrument into a financial one, and the hybrid-regulation problem follows.
- Permissionless works only if the token's entire content is transferable property. DGLD is a plain ERC-20 with no whitelist and it functions because co-ownership travels with the token and nothing else is attached. AURX would carry ICS standing, dividend entitlement and credit eligibility, all of which break on an anonymous transfer. That is the case for a permissioned base.
- Physical redemption at retail is operationally solvable. DGLD delivers 1 gram at 0.20% with KYC only at delivery. It can do that cheaply because MKS PAMP is PAMP, and Aurumix cannot replicate that cost base. But Aurumix should stop treating no-physical-redemption as an industry norm it merely conforms to. It is a deliberate retention and credit-revenue choice.
- The wind-down clause is the best in the set and still beatable on four cheap points. On termination GTSA notifies holders via its website, after which each holder elects physical delivery or instructs GTSA to sell and remit net proceeds, with a two-month deadline and a stated default. A genuine ex-ante election with metal as one option. Its weaknesses: notice is by website only, and an issuer website does not survive the issuer; GTSA sells "at its own discretion" with no reference fix; deductions for "any applicable fees, costs, charges and expenses" are uncapped; and termination is "for any reason" with no defined trigger. Aurumix can beat all four with notice by durable channel including email and an onchain notification, a pre-committed pricing methodology such as the LBMA PM fix on a defined date, a hard cap on wind-down fees, and defined triggers with a minimum notice period.

Note finally what infrastructure choices cost and what they do not. PAXG launched about a month before DGLD with comparable custody quality, chose Ethereum, and is roughly 220 times larger today. Ocean gave DGLD no composability, no wallet support (GTSA built and maintained its own `ocean-wallet`, last committed October 2020) and no exchange listings. The consortium conceded within 13 months by shipping a wrapped ERC-20 on Ethereum in November 2020. DGLD then migrated to Ethereum in 2022 and stayed dormant three more years anyway. Correct infrastructure was necessary and nowhere near sufficient. What revived it was an owner with a commercial reason to push it. Aurumix needs both: a structure that survives neglect, and a profit and loss line that prevents it.

---

### 4.10 Aurus (tGOLD)

| Field | Detail |
|---|---|
| Issuer | Aurus does not issue the tokens. Independent licensed bullion businesses ("Provider Partners") mint against metal they own. Software vendor: AURUS TECHNOLOGIES LTD, company no. 11703940, England and Wales, incorporated 29 November 2018 (formerly AURUSGOLD LTD until 26 February 2020), 5 Brayford Square, London E1 0SG, SIC code 62012. AURUS FOUNDATION, company no. 14194058, company limited by guarantee incorporated 24 June 2022, accounts overdue |
| Licence covering the token | None identified. No FCA authorisation or cryptoasset registration for either entity. No VARA, DMCC, ADGM, MAS or MiCA authorisation found. Regulated activities sit with partner firms under their own licences |
| Assets under management | $7.10M total protocol value at 28 July 2026: tGOLD ~$5.6M, tSILVER ~$1.5M. tGOLD supply on Ethereum 43,322 tokens (43.3 kg), 466 holders |
| Backing | 1 tGOLD = 1 gram of 99.99% LBMA-accredited gold from LBMA, DMCC or LPPM accredited refineries, held by independent Vault Partners. No vault company is named anywhere |
| Custody fee charged to holders | 0%. "No storage fees for Aurus tokens", stated in the whitepaper |
| Yield paid to holders | None on tGOLD. Holders of the separate ecosystem token (AurusX, migrating to $AURUS) receive monthly distributions in tGOLD and tSILVER from the fee pool |
| Redemption | Physical redemption exists. Holder burns tokens and requests vault extraction through a Provider Partner or partnered dealer. Burn fee 1.5% for tGOLD, charged to the executing Provider, plus that Provider's undisclosed markup and the vault's shipping and handling. One data platform records an observed retail cost of 3.00%. KYC/AML by the Vault Partner. Minimum increment not disclosed |
| Token standard | Plain ERC-20, 18 decimals, Ethereum and Polygon. No whitelist, no transfer restrictions. Contracts upgradeable since the November 2022 migration |
| Reserve verification | None published. No named reserve auditor, no attestation, no stated frequency, no bar list. A Chainlink Proof of Reserve feed is announced as "in the works" but is not live. Smart-contract audit by NonceBlox for the 2022 migration, report not publicly linked |

#### What it is

Aurus is a tokenisation protocol that does not itself issue tokens. It supplies smart contracts, an app and an API to licensed bullion businesses, who mint tGOLD, tSILVER and tPLATINUM against metal they own and place with an approved vault. Each tGOLD is one gram of 99.99% LBMA-accredited gold.

The whitepaper makes the positioning explicit: Aurus provides "Tokenization-as-a-Service... to qualified commodity providers who account for an estimated 30% of the precious metals market. Now, these established businesses can mint and distribute their own precious metal-backed tokens, earning passive rewards from the trading activity." The pitch to a local bullion dealer is defensive: keep your own customers, brand and pricing rather than lose them to a centralised competitor like PAX Gold.

Three partner roles exist, and the distinction between them matters more than any other fact here. Provider Partners are bullion traders who supply and own the metal, initiate minting, run arbitrage and execute redemptions. Vault Partners custody and insure the bullion, audit intake and authorise minting. Distributor Partners are physical bullion retailers who sell tokens to end customers through APIs and website plugins. That third tier is the reseller tier, and it is the closest structural analogue to Aurumix's agent network anywhere in this set. The token was AurusGOLD (AWG) until renamed tGOLD on 9 November 2022. Siblings are tSILVER (tXAG) and tPLATINUM (tXPT).

#### Legal structure and regulatory standing

The whitepaper asserts holder title in strong terms: "Aurus company has no claim on precious metals allocated to the system. Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders. The bullion is stored physically by independent Vault Partners on behalf of the token holder. Token holders have the right to withdraw their bullion from a Vault Partner."

The problem is the document carrying that promise. The only legal document published on aurus.org is a four-page Terms and Conditions dated 6 November 2024, and it is a website terms of use, not terms of issue. It names no contracting entity: no company name, no number, no registered address. It contains no governing law or jurisdiction clause. It says nothing about gold, title, vaults, redemption or fees; not one of those words appears. It disclaims custody ("AURUS itself does not custody or control user tokens") and disclaims the partners who do the actual work ("AURUS does not take responsibility for the content or accuracy of these third-party offerings"). It asserts that "AURUS tokens are not securities, digital currencies, or any other form of financial instrument as defined by applicable laws", a self-serving legal conclusion stated by an unnamed party rather than a regulatory determination. And it describes Aurus as "a decentralized DeFi platform" whose operations "align with DAO principles".

The chain of title therefore runs from holder, through no contract at all, to a Provider Partner who owns the metal, through an unpublished contract, to a Vault Partner. The holder's claim rests on a marketing whitepaper and on bilateral agreements that are not public. Where whitepaper and legal document diverge, the legal document does not disagree, it is silent, and silence gives the holder nothing to sue on. The Provider, Vault and Distributor Partner agreements are all unpublished.

No licence was found on any register. The FCA shows no authorisation and no cryptoasset registration for either entity. Aurus Technologies Ltd files at Companies House under SIC 62012, software development, consistent with a firm deliberately structured as a technology vendor rather than a financial institution. The whitepaper's only DMCC reference is that metal is sourced from DMCC-accredited refineries, a refinery accreditation rather than a licence held by Aurus.

One data platform records the tGOLD issuer as located in Jumeirah, Dubai. The corporate register says otherwise: the operating entity is an English company at 5 Brayford Square, London. The likely explanation is that founder-director Guido Jean-Paul van Stijn is UAE-resident with a Dubai correspondence address on the Companies House record. Any claim that Aurus is a Dubai gold token is false at entity level.

The regulatory perimeter is the business model. Aurus's answer to regulation is not to hold a licence but to push the regulated activity onto its partners. Owning bullion, custody, selling to consumers, KYC/AML and physical redemption are performed by Provider, Vault and Distributor Partners in their own jurisdictions under their own licences. Aurus supplies the code. The structure is coherent and cheap, and it means no single regulator supervises the tGOLD product end to end, and no regulator has approved the "you own the gold" claim.

Aurus Foundation is not an independent standards body. It markets itself as certifier of Distributor Partners and "global advocate for the international tokenized precious metals standards of tXAU and tXAG". Its person with significant control is Aurus Technologies Ltd, filed 3 July 2025, making it a wholly controlled subsidiary. It received a first Gazette notice for compulsory strike-off on 2 June 2026, suspended 16 July 2026, accounts overdue since 31 March 2026. A certification body owned by the company it certifies for, two weeks from dissolution, is not a governance safeguard.

#### Custody and reserve verification

Metal sits with multiple independent Vault Partners, described as "partnered, fully-audited, and insured vaults across the globe". No vault company is named anywhere in the whitepaper or on the site, and no country or city list is published. One secondary source mentions Switzerland as an example.

Allocation is asserted but not evidenced. The whitepaper says bullion "will always remain legal ownership of the token holders", stored "on behalf of the token holder", with tokens "backed by individual gold, silver and platinum bars linked to unique serial numbers". No trust deed or bailment agreement is published, and no public bar list exists.

Aurus blurs the two forms of assurance, so separate them. The word "audited" recurs across its marketing: "fully-audited and insured vaults", "audited smart contracts". A reader skims that and concludes reserves are independently verified. They are not. What exists is a smart-contract audit by NonceBlox for the November 2022 migration, which says nothing about gold, and vault-level internal audit obligations imposed by contract on unnamed partners, with no public output. There is no independent reserve attestation for tGOLD, no named auditor, no stated frequency. A Chainlink Proof of Reserve integration is described on the tGOLD page as a collaboration and on the Aurus Foundation site as "in the works and coming soon"; no feed address exists on Chainlink's data feeds.

That gap has a live consequence. The aurus.org tGOLD page displays a self-reported reserve of 73,398.5 grams while the Ethereum contract shows 43,322 tokens. The gap is plausibly Polygon supply plus tSILVER and tPLATINUM accounting, or a stale figure, but the issuer publishes no reconciliation and there is no live feed to settle it. A roughly 30 kg discrepancy in a self-reported reserve number, with no attestation behind it, is precisely the item a Proof of Reserve feed exists to close.

#### Fees, revenue and redemption

| Fee line | Rate | Paid by | Received by |
|---|---|---|---|
| Tokenization / minting, tGOLD | 0.5% | Provider Partner at mint | Fee pool |
| Tokenization / minting, tSILVER and tPLATINUM | 1.0% | Provider Partner | Fee pool |
| Transaction fee | 0.18% | Initiator of each transfer | Fee pool |
| Storage / custody | 0% | Nobody | n/a |
| Burn / withdrawal, tGOLD | 1.5% | Provider Partner executing extraction | Fee pool |
| Burn / withdrawal, tSILVER and tPLATINUM | 3% | Provider Partner | Fee pool |
| Retail redemption markup | Not disclosed, set by each Provider | End user | Provider Partner directly |
| Vault extra services | Not disclosed, vault's own price | End user | Vault Partner directly |
| Distributor spread | Not disclosed, distributor sets retail price | End user | Distributor Partner directly |

Fee-pool distribution is the most useful disclosure Aurus makes and the most important distribution finding in this report. The whitepaper states it verbatim: "All accumulated transaction, minting and burning fees are distributed back to the ecosystem as follows: 50% of tGOLD fees to AurusX holders, and 50% to Aurus minting partners (25% Vaults, 25% Providers). With tSILVER and tPLATINUM 30% goes to AurusX holders, and 70% to minting partners (35% Vaults, 35% Providers)." Vault rewards are paid quarterly, in metal tokens, pro rata to grams stored, by published formula: quarterly reward equals total quarterly fees multiplied by the vault's share of grams stored, multiplied by 0.25.

The reseller tier receives 0% of that pool. The tGOLD split of 50% / 25% / 25% is fully allocated, and Distributor Partners are not in it. What they get instead is the ability to buy and sell tGOLD at their own prices through APIs and a website plugin on their own site to their own client list, preferential bulk redemption at lower per-unit fees than retail holders with the right to resell, and an upgrade path: a Distributor can graduate to Provider Partner, tokenize its own inventory, and access both the arbitrage and the 25% fee share. There is no commission, no override, no residual, no multi-level structure. A Distributor's earnings do not depend on recruiting other Distributors, and no partner earns from another partner's volume. This is a merchant-margin supply chain, not an MLM.

Two material caveats. Aurus Technologies Ltd takes no disclosed share of the pool at all: 50% plus 25% plus 25% accounts for 100% of tGOLD fees, and how the software vendor is funded is not disclosed. Candidates are partner onboarding or licence fees, an AurusX treasury allocation, or equity funding, but none is published. And the split has changed at least three times: 70% AWX / 15% providers / 15% vaults in the 2019 to 2020 AWG era, the current 50% / 25% / 25% for gold, and a March 2021 press description of "50% (25% each) to providers and vaults, 50% to AurusDeFi holders". The whitepaper reserves the right to keep changing it: "All fees on the Aurus ecosystem are subject to change... Fees will be reviewed on a regular basis and can be amended accordingly", with only a soft promise that values will be "capped through Smart Contracts". The November 2022 migration to upgradeable contracts explicitly enabled "adjustable fees". Partner economics here are revocable by the operator, and they live in a whitepaper while the only legal document is a four-page website terms page naming no entity and no governing law.

Redemption is a genuine product feature. The holder burns tokens and requests vault extraction through a Provider Partner or partnered dealer, choosing from bars or coins on offer. The 1.5% tGOLD burn fee is charged to the executing Provider, not directly to the user: the whitepaper is precise that "the fees for users redeeming physical gold, silver or platinum is dependent on the Provider Partner that is facilitating the exchange". Shipping and handling are charged by the vault, and KYC/AML is done by the Vault Partner before withdrawal. The older AWG whitepaper documented a 10-day claim window with a bilateral handshake signature between holder and vault, after which the transaction auto-cancels and tokens return, fees non-refundable.

Retail cost is therefore undisclosed and unbounded: the user pays whatever the Provider chooses, so 1.5% is a wholesale floor rather than a consumer price. One data platform records 3.00% for tGOLD, roughly double the burn fee, consistent with the Provider adding margin. The whitepaper also states openly that Distributor Partners can redeem large quantities at lower per-unit fees than retail holders and resell. Redemption economics are explicitly tiered in favour of the trade.

#### Liquidity and distribution

Protocol value is $7.10M at 28 July 2026, Ethereum only, roughly $5.6M tGOLD and $1.5M tSILVER, down from $7.24M three days earlier. tGOLD supply on Ethereum is 43,322 tokens across 466 holders.

Onchain liquidity is effectively zero. The only live pools located are a TGOLD/USDT0 pair with $3,126 of liquidity and $211 of 24-hour volume, and a Solana TGOLD/SOL pool with $1.71 of liquidity and no volume. The Ethereum tGOLD contract shows $0.00 in 24-hour volume and about $59 of pooled reserve. Trading is essentially offchain and dealer-mediated, through CEX.IO, QuickSwap, and bullion distributors including Direct Bullion, Aurica Group and AgaBullion.

Aurus is architecturally designed to trade at par, not at a premium. Its peg is maintained through Provider Partner arbitrage against the OTC bullion market, which caps the price at net asset value plus the 0.5% mint fee. Any premium above that is immediately minted into. Roughly $5.6M of gold has accumulated over seven years, while tokenized gold as a sector reached about $5.6B in Q1 2026 after adding $1.3B in the quarter. Aurus holds roughly 0.1% of the sector and did not participate in its growth.

Distribution is business-to-business-to-consumer. Named partners span the UK (Direct Bullion), Chile (Aurica), Spain (Sempsa JP, an LBMA refinery), Singapore (Indigo Precious Metals), Turkey and AgaBullion. Excluded jurisdictions are significant: the terms bar users from the USA and its territories, Russia, Belarus, Cuba, Iran, Iraq, North Korea, Syria, Sudan, South Sudan, Yemen, Zimbabwe, Myanmar, the DRC and Crimea, and impose a UK-specific gate requiring users to confirm they are professional investors or high-net-worth individuals for certain features. India is not excluded. There is no savings plan, no monthly contribution facility, no auto-invest, no direct debit, no retail referral or affiliate programme. Purchases are one-off and dealer-mediated. Recurring income exists but is paid to AurusX holders, not to the people who own the gold.

#### Relevance to Aurumix

Aurus carries the most important distribution finding in this report. A multi-tier partner network can be built without a commission structure, and Aurus's tiers are compensated for capital and custody rather than for selling.

The three tiers are functional, not hierarchical. Providers supply metal, Vaults hold it, Distributors sell it. Fees flow to the first two at 25% each and to ecosystem token holders at 50%. The selling tier gets nothing from the pool. It earns its own markup on its own client list, and Aurus's pitch to it is defensive ("you will lose customers to PAX Gold if you don't") rather than an income promise. The two non-cash incentives holding the tier together are preferential bulk redemption economics and a graduation path into the higher-margin Provider role.

That cuts directly at the Aurumix design. Aurumix's three-tier agent network is a recruitment and commission hierarchy in which agents earn from downstream volume. That is economically an MLM, and regulators treat it as one. Aurus's network is a merchant-margin supply chain in which each tier is paid for a distinct economic function it actually performs, not an MLM. If Aurumix can re-cast its tiers so each is paid for a function (capital introduction, custody, servicing) rather than for recruitment depth, it keeps most of the distribution reach with materially less classification risk. Aurus also demonstrates the alternative to override commissions for motivating the top tier: let the best agents graduate into a higher-margin role rather than paying them a slice of their recruits' volume.

Carry the caveat alongside the finding, because it changes how much weight it bears. Those partner economics live in a whitepaper. The only legal document Aurus publishes is a four-page website terms page that names no entity, states no governing law, and does not mention gold, title, vaults, redemption or fees. The split has changed three times, the contracts are upgradeable specifically to permit "adjustable fees", and the current $AURUS restructuring appears to redirect fee flows toward liquidity-pool incentives with no updated whitepaper documenting the new split. A partner economics model that is revocable by the operator and lives outside any binding document is a design reference, not a governance precedent. If Aurumix adopts the structure, it should put the tier economics in the terms.

Note also what Aurus does not have: no savings plan, no recurring contribution, no SIP, no auto-invest, no referral scheme. Aurumix's monthly SIP remains genuinely differentiated, and Aurus's absence of one is a plausible reason it accumulated only ~$5.6M in seven years. Dealer-mediated one-off purchases do not compound. This profile is evidence for the SIP, not against it.

Four further read-acrosses:

- Zero custody fee, funded from transaction flow, keeps the peg intact. Storage is 0%, funded by 0.5% at mint and 1.5% at burn (both borne by Provider Partners) plus 0.18% per transfer. The vault is compensated from that pool in tokens, quarterly, pro rata to grams stored, rather than by deducting metal. No grams ever leave the backing, so a price equals grams divided by tokens formula never breaks. The caveat is that this works only if churn is high enough to fund the vault, and at Aurus's volumes it plainly is not, which is why the model is being restructured around liquidity-pool incentives and a new cGOLD fee token. A buy-and-hold savings product generates almost no transaction fees by design, so Aurumix's churn would be lower still. The mechanism transplants; the funding does not.
- Aurus's dividend structure is the safer version of the anti-pattern. It pays recurring income monthly, in metal, funded entirely from investor and trade fees, which is the recycled-fee structure to be wary of. Two mitigations are worth copying. The yield sits on a separate ecosystem token, so tGOLD is never marketed as yield-bearing and the gold product stays clean. And Aurus never promises a rate: there is no "5% APY" claim to fail, only a share of whatever fees arrive. Aurumix's ICS Dividend already follows the second by expressing itself as a share of realised operating profit. It does not follow the first, because ICS standing rides on the token itself.
- Free transferability is what lets third parties arbitrage the peg, and a permissioned token gives that up. tGOLD works as a plain ERC-20 because it carries nothing but a claim on a gram of gold, with all identity-dependent logic sitting offchain at the dealer and vault boundary. AURX cannot copy that, which strengthens the case for a permissioned base. But a permissioned token cannot be arbitraged to par by outsiders, so Aurumix must be the market maker of last resort for its own token and should budget for it.
- The structural separation of the technology company from the metal owner is the cleanest idea here. The whitepaper provides for both vault exit ("If a Vault Partner is unable to continue being a Vault Partner, they are required to transport all bullion to another partner vault. Said Bullions will continue to belong to token holders during this process") and issuer failure ("Regardless of what happens to Aurus, vaulted bullions will always remain legal ownership of the token holders"). Aurus's gold is owned by Provider Partners and sits bankruptcy-remote from the software company by design. Aurumix intends to own the vault gold itself and lend against it at 90 to 95% loan-to-value, so Aurumix creditors would rank against the same gold. Worth resolving before it is tested.

On redemption, the honest comparison is closer than it first appears. Aurus's redemption is real, and someone will hand you metal. It also costs 1.5% wholesale, roughly 3% as observed at retail, plus shipping, plus an undisclosed Provider markup, and requires collection or delivery from an unnamed vault in an undisclosed city. A redemption right whose all-in cost is undisclosed and set by an intermediary is not obviously superior to Aurumix's stated cash buyback only. Aurumix's position is defensible if stated plainly, and it should never imply that metal will be handed over.

---

### 4.11 VNX Gold (VNXAU)

| Field | Detail |
|---|---|
| Issuer | VNX Commodities AG, Liechtenstein commercial register FL-0002.654.271-8, Dr. Grass-Strasse 12, 9490 Vaduz. Still the named issuer on the 31 December 2025 reserve report. VNX Global Ltd. (Bermuda) now fronts vnx.io |
| Licence covering the token | None. Six TVTG registrations, all of type "Registration" and none of type "Licence": Token Generator, TT Identity Service Provider and TT Depositary are active; TT Token Depositary and TT Key Depositary expired 31 January 2024 on merger into TT Depositary; TT Exchange Service Provider expired 2 July 2026 under the MiCAR transitional period. No Token Issuer registration under Art. 12(1) or Art. 12(2). VNX Global Ltd. holds a Bermuda DABA Class M digital asset licence granted 12 May 2026, whose scope is silent on the gold |
| Assets under management | 13,100.00 VNXAU attested at 31 December 2025, being 13.1 kg of gold, roughly $1.7M. Down from 15,100 g at 31 December 2023. Aggregator market cap figures of ~$5.73M cannot be reconciled with the attested reserve |
| Backing | 1 VNXAU = 1 gram of LBMA-standard gold in "brutto grams". The terms of business define this as "1/1000 co-ownership in a gold bar of 1 kilogram". VNX holds the metal at the custodian "as the vicarious owner, registrar and depository for the VNXAU-token holders". The custody account is in VNX's name, not holders' names |
| Custody fee charged to holders | 0%, advertised as "zero storage fees". EUR 10 per month inactivity fee on dormant accounts until the balance reaches zero |
| Yield paid to holders | None. No staking, no APY, no disclosed leasing |
| Redemption | Three routes: physical gold at a 1 kg minimum (~$129,000), collected at the Liechtenstein vault or delivered at the holder's "own expense and risk"; cash, by instructing VNX to sell; or sale on a third-party exchange "subject to availability". All conditional on registration, identification and AML clearance on the VNX Platform, whose exchange operations closed on 30 June 2026 |
| Token standard | Marketed as a plain ERC-20 but is not. An EIP-1967 upgradeable transparent proxy on Ethereum, every transfer gated by a swappable external Transfer Provider, plus freeze, seize, pause and dormant transfer-fee functions. Live on Ethereum, Solana, Base and Q; Polygon deprecated; Avalanche, Arbitrum, XRPL, Fraxtal and Concordium discontinued May 2026 |
| Reserve verification | Annual ISRS 4400 agreed-upon-procedures report by AREVA General Auditing and Trust Company Ltd, Vaduz (FL-0001.076.904-3). Latest covers 31 December 2025, signed 23 March 2026. Custodian named as Philoro Edelmetallhandel AG, Eschen. Smart-contract audit by University of Luxembourg SnT/SEDAN, v1.0.2, dated 26 October 2021. No bar list, no live Proof of Reserve feed |

#### What it is

VNX Gold is a gram-denominated gold token issued by a small Liechtenstein operator under the world's first purpose-built token statute. Each VNXAU is asserted to be one gram of LBMA-standard gold held in a Liechtenstein vault.

It is the smallest protocol here by an order of magnitude: 13.1 kg of gold, roughly $1.7M of genuinely attested metal, about one and a half London Good Delivery bars. Tether Gold and PAX Gold each hold over $1.7bn.

It earns a full profile despite its size because it is the best-documented protocol in the set. VNX publishes signed reserve reports, names its custodian, commissioned a real smart-contract audit, and spells out the ownership construct in unusual detail. That documentation is what makes it useful: it shows precisely where a well-intentioned, properly registered gold token still leaves the holder exposed, in the issuer's own words.

It is also, as of this month, a protocol in visible retreat. Between December 2023 and December 2025 its gold book fell 13% and its custodian changed without announcement. In 2026 it cut six chains, let its exchange registration lapse rather than seek MiCAR authorisation, shut its platform exchange, and moved its licensing centre of gravity to Bermuda.

#### Legal structure and regulatory standing

VNX has written down what most issuers leave vague, and what it has written down is internally inconsistent.

The marketing says VNX Gold "represents ownership in specified physical gold bars purchased and stored in a highly secured professional vault", that the "VNX Gold token holder is the only lawful owner of the underlying gold", and that each bar is "stamped by its own serial number and linked to VNX Gold tokens". The terms of business say something different: "VNX Gold generated by VNX represents co-ownership in physical gold. One VNX Gold corresponds to 1/1000 co-ownership in a gold bar of 1 kilogram, which corresponds to 1 gram."

Those are different legal animals. Specified bars with serial numbers linked to your tokens is allocated, individuated title. One-thousandth co-ownership of a kilo bar is an undivided fractional interest in a pool. A holder cannot point to a bar; they hold a fraction alongside 999 strangers. The reserve report uses the pooled framing throughout, calling the holding a "Collective Token Holders Commodity Deposit". The terms, not the marketing, govern.

Title runs through VNX rather than to holders directly. VNX holds the gold at the custodian "as the vicarious owner, registrar and depository for the VNXAU-token holders", and the custody account at Philoro is in VNX's name under customer number 2001517. Philoro holds for VNX, and VNX holds as fiduciary for holders.

What actually evidences a holder's claim is not the token. AREVA states it plainly in the reserve report:

> "This report does not express an opinion about the accuracy and completeness of the register of the single token holders which VNX Commodities AG is keeping and which is deemed to be the basis to assert a property right."

Read that carefully. The basis of the property right is VNX's own internal register, not the blockchain and not the auditor's work, and the auditor expressly declines to verify it. A holder's legal claim rests on a private database the attestor refuses to opine on. That is the sharpest single disclosure in this entire set.

On insolvency, VNX asserts bankruptcy remoteness: "The Collective Token Holders Commodity Deposit does not form part of the assets of VNX Commodities AG and... ownership rights... remain intact irrelevant of an eventual liquidation, dissolution or insolvency of VNX Commodities AG." That is a real and well-drafted structure, better than most competitors offer. Two things temper it. The assertion sits in a section explicitly headed "No Assurance Provided by the Independent Auditor on These Notes". And AREVA's 2023 report said of the fiat reserves that segregation in bankruptcy is "a legally not defined case, due to the lack of court rulings in Liechtenstein". No Liechtenstein court has ruled on either.

The regulatory position is public record on the FMA register, and three findings follow. Registration is not authorisation, and the FMA says so: its guidance states the TVTG registration assessment has "both a more limited scope and a lesser depth than the licensing procedure under financial market law", and that the FMA does not verify the content or accuracy of token issuers' basic information nor evaluate "token issuer legitimacy or business model viability". TVTG registration is a fitness and technical-suitability gate on the service provider, not a product approval and not prudential supervision.

Second, VNX is not registered as a Token Issuer. The register carries distinct categories under Art. 12(1) and Art. 12(2), and VNX holds neither. It holds Token Generator, the technical role of creating tokens on a TT system, not the issuance role that attracts basic-information and prospectus-style duties. VNX's own documentation lists five roles and Token Issuer is absent from that list too.

Third, the exchange registration lapsed on 2 July 2026, annotated on the register as "Expired pursuant to Section II, paragraph 2 of LGBl. No. 2025.113 (MiCAR transitional period)". Liechtenstein is in the EEA, so MiCAR displaced the TVTG exchange role and the grandfathering window closed. No MiCAR or CASP authorisation for VNX was found in any register. VNX's response was not to obtain one but to shut the exchange down. A purpose-built national token law was overridden by supranational regulation, and a small issuer chose exit over re-licensing.

VNX also holds a business trade licence from the Liechtenstein Office of National Economy. The Bermuda Class M licence granted 12 May 2026 is described in VNX's own notice as belonging to "a VNX Group entity" and says nothing about VNX Commodities AG or about the gold.

#### Custody and reserve verification

The current custodian is Philoro Edelmetallhandel AG at 9492 Eschen, Liechtenstein, account 2001517. The prior custodian was OZL Offenes Zollfreilager in Liechtenstein AG, client number 1708, per the 31 December 2023 report. The change was never announced. It surfaced only by comparing the 2023 and 2025 reports. Full insurance is claimed; the insurer and policy are not disclosed. No bar list is published despite the serial-number claim, and there is no live Proof of Reserve feed.

The attestation is real and weaker than the word "audit" implies, and VNX's own auditor says so. AREVA states that "This Agreed-Upon Procedures engagement is not a reasonable or limited assurance engagement. Accordingly, we do not express an opinion or an assurance conclusion." It discloses that it is "not required to be independent for the purpose of this engagement" and that it is also VNX's financial-statement auditor. And the procedures excluded the metal: "while we did obtain confirmation of gold balances from the third-party custodian(s) Philoro, our procedures did not include the observation of gold held by these custodian(s) and did not include any validation of the quality of gold." What exists is an annual reconciliation of onchain supply against a custodian's paper statement, performed by a non-independent firm, with no bar inspection and no assay. Meaningfully more than most competitors publish, and still not what a retail reader hears in the word "audited".

The smart-contract audit answers a different question entirely. The University of Luxembourg SnT/SEDAN review of October 2021 is a security review of the code and says nothing about whether gold exists. It found 1 major and 68 minor issues; by version 1.0.2 the major issue (a contract exceeding the 24,576-byte limit) was fixed and 19 minor issues remained, mostly naming-convention items. Genuine academic work, five years old, predating the Base, Solana and Q deployments entirely, and sitting on the transparency page under a March 2026 URL where a skimming reader would assume it is current.

One real discrepancy appears in the 2025 attestation, disclosed honestly. AREVA found a 1.13-token mismatch on Solana, 6,449.13 asserted against 6,448.00 onchain, explained as holders burning tokens directly from wallets. Onchain supply can therefore drift below issued supply, leaving the gold slightly over-collateralised rather than under.

#### Fees, revenue and redemption

| Fee line | Amount |
|---|---|
| Generation / issuance | "Starting from 0.1%" |
| Ongoing storage / custody | 0% |
| Platform exchange fee | 0.3% base, 0.2% above EUR 100k per 12 months, 0.1% above EUR 1M per 12 months |
| Crypto withdrawal | EUR 3 (Ethereum), EUR 0.5 (Base), EUR 1.5 (other chains) |
| Fiat withdrawal | EUR 10 SEPA, EUR/CHF 30 SWIFT, GBP 40 SWIFT |
| Card top-up | 2.5%, minimum EUR 10 |
| Inactivity fee | EUR 10 per month on dormant accounts, until the balance reaches zero |
| Physical delivery | Holder's "own expense and risk", not quantified |
| Onchain transfer fee | Contract supports `setFeeRate` and `setFeeRecipient`. Not currently observed as charged |

Several aggregators report VNX's storage cost as 0.18% to 2% per annum, or 0.25% to 1% per annum. Those are the competitor columns in VNX's own comparison table, covering exchange-traded products and metal accounts. VNX's own column reads "Effective costs: starting from 0.1% for generation". Any citation of a VNX annual storage fee is a misreading of the marketing table.

VNX does not say what funds zero storage. The arithmetic is instructive. Vaulting and insuring 13.1 kg at a commercial rate of roughly 0.3% to 0.5% per year costs on the order of $3,000 to $6,000 annually against ~$1.7M of metal. A rounding error, comfortably absorbed by generation fees, exchange fees, card fees, the inactivity fee, and the far larger stablecoin business the gold token sits beside. Zero storage is affordable here precisely because the gold book is tiny and functions as a loss-leader for something else. At $500M of gold the same promise costs $1.5M to $2.5M a year and has to come from somewhere real.

The EUR 10 per month inactivity fee is the quiet counterweight and the most transferable line in the schedule. A dormant retail holder is drained to zero over time. It is a storage fee in all but name, charged only to the disengaged, and it never touches the gram balance.

Redemption offers three exits and the physical route is gated hard. The minimum is 1 kg, roughly $129,000 at ~$129 per gram. A holder of 1,000 VNXAU sits exactly at the threshold. VNX's entire attested reserve is 13.1 kg, so the whole protocol supports at most 13 simultaneous physical redemptions. The homepage pitch of collecting gold from the vault or having it delivered anywhere in the world is unreachable for essentially every retail holder. Cash and physical both require the VNX Platform, whose exchange operations closed at 18:00 CET on 30 June 2026. Withdrawals to whitelisted wallets and banks were permitted only until 18:00 CET on 31 July 2026, three days from the date of this research. Any holder who missed that window is left with third-party exchange sales on a market doing about $36,000 a day.

#### Liquidity and distribution

Measured on 28 July 2026, VNXAU trades at $130.04 with a reported market cap of $5.73M, 24-hour volume of about $36,000, and roughly 2,440 holders. Venues are XT.COM centralised, and Raydium, Orca and Aerodrome decentralised.

The supply figures do not reconcile, and the mismatch matters. CoinGecko reports 44,100 tokens circulating. One RWA data platform reports 12,886 across four chains with $1.69M in assets. The audited figure at 31 December 2025 was 13,100. Direct onchain reads give Ethereum 582.67, Base 1,846.90 and Polygon 107.74, totalling 2,537.31 on EVM chains. The $5.73M market cap implies roughly 44 kg of gold against 13.1 kg attested. The plain reading is that CoinGecko triple-counts a multichain token, and VNX publishes no consolidated supply dashboard to correct it. The consequence stands regardless: the headline market cap that every aggregator and any casual analyst will quote is roughly 3.4 times the gold its own auditor confirmed exists. For a protocol whose entire pitch is verifiable backing, the absence of a live supply feed is a self-inflicted wound.

On price, spot via XAUT and PAXG runs $129.11 to $129.22 per gram. VNXAU at $130.04 is a premium of about 0.7%, thin enough that the print is nearly meaningless. At $36,000 a day against a $5.7M cap, the float turns over roughly once every 159 days, against about 17 days for PAXG. A single $10,000 order moves this book.

Distribution offers nothing new. No savings plan, no recurring purchase, no dollar-cost-averaging product, no referral or affiliate programme, no agent network. Distribution is the direct platform, exchange listings, and business-to-business integrations. Geography is EEA-centric, under Liechtenstein law and exclusive Liechtenstein jurisdiction, with terms that explicitly note the tokens are not covered by deposit insurance. The real growth channel is white-label infrastructure: VNX supplied the gold rails for BlocPal's BPG1 token on 26 November 2025, backed one ounce per token. VNX also has a utility token, VNXLU, usable to pay platform fees at a floor of EUR 0.25, and announced a VNX Community Hub governance token on 26 March 2025 whose current status is not disclosed. Neither carries revenue share or yield.

#### Relevance to Aurumix

The single most useful finding here is the auditor's sting, and Aurumix should build around it.

AREVA states that the basis of a holder's property right is VNX's own internal register of token holders, and then expressly refuses to opine on it. Meanwhile the terms say holders get one-thousandth co-ownership of a kilo bar, while the marketing says they own specified serial-numbered bars. Aurumix is building a product whose entire promise is "you own physical gold", sold to retail savers through an agent network. **The token is not the title. The register is the title.** Whatever Aurumix builds, the holder register must be the audited artefact, its integrity must be independently verified, and the ownership construct in the terms must match the words on the landing page. VNX is the best-documented operator in this set and it still fails that test in its own paperwork.

Four further read-acrosses:

- Zero custody fee plus a dormancy charge is a working answer to the peg problem. VNX charges no ongoing custody fee and deducts nothing in grams, so its one-token-one-gram peg holds exactly: the attestation reconciles 13,100 tokens to 13,100 grams cleanly. Aurumix cannot copy the funding, which rests on a tiny gold book cross-subsidised by a stablecoin business. It should copy the EUR 10 per month inactivity fee: a cash-denominated charge that falls only on dormant accounts, never touches the gram balance, and quietly solves the cost of carrying disengaged holders.
- Encumbering the gold and claiming it is ring-fenced are mutually exclusive. VNX pays no yield, no APY, no staking, and discloses no leasing. The reason is visible in its own documents: the gold is asserted to sit outside VNX's balance sheet in a segregated collective deposit. You cannot simultaneously claim bankruptcy-remote segregation and generate return from the metal. If Aurumix wants both the ICS Dividend and a credible "your gold is safe if we fail" story, it must fund the dividend from something that is not the gold, and say so explicitly.
- There is a third option between a plain ERC-20 and full ERC-3643, and VNX is running it. The Ethereum contract is an EIP-1967 upgradeable transparent proxy whose bytecode carries the revert string `Declined by TP!`. Every transfer is gated by a pluggable Transfer Provider with three implementations, permissive, whitelist-gating and admin, swappable via `changeTransferProvider`. The contract also carries `freeze`, `unfreeze` and `reclaimTokensFromFrozenAddress` (confiscation: an admin can move tokens out of a frozen wallet), `pause` and `unpause`, and dormant `setFeeRate` and `setFeeRecipient` functions, all under runtime-configurable roles in a separate Manager contract. Wallets, explorers and decentralised exchanges treat it as vanilla. The issuer retains whitelist, freeze, seize, pause and fee powers and can tighten them by changing one address. That is ERC-20 composability today with ERC-3643-grade control in reserve, cheaper to build than full ERC-3643. Two cautions: nothing in VNX's public material discloses these powers (the reserve report says the tokens "are freely transferrable", true only until the Transfer Provider is switched), and a hook that gates transfers does not by itself carry ICS state, so Aurumix would still need the registry. Document the admin powers openly, because the gap between "freely transferrable" and `reclaimTokensFromFrozenAddress` is exactly what destroys trust when discovered.
- A cheaper regulatory regime is cheaper because it supervises less, and it can be superseded. Liechtenstein's TVTG is the most bespoke token statute in existence and VNX holds six registrations under it. Registration is not a licence, the FMA does not vet the product or the business model, VNX holds no Token Issuer registration despite issuing tokens, and the exchange role was overridden by MiCAR and expired on 2 July 2026, at which point VNX closed the exchange rather than seeking authorisation. A bespoke national regime bought VNX five years of legitimacy and then evaporated under supranational law. The temptation to find something cheaper and more accommodating than VARA is real, and this is the failure mode. Worth modelling separately: VNX's dual-entity hedge, keeping the regulated issuer in Liechtenstein and putting the new licence in a second Bermuda entity, is a legitimate structural answer to the hybrid-regulation problem.

On redemption, the honest comparison favours Aurumix more than it feels. VNX offers physical redemption and Aurumix does not, but VNX's 1 kg minimum puts delivery out of reach of every retail holder, and its entire reserve would satisfy 13 such requests. That gate is a hard weight threshold rather than vague wording, arguably more honest and equally exclusionary. A stated cash-buyback-only exit is better than an advertised physical redemption that 99% of holders cannot use. Aurumix's real exposure is the "you own physical gold" pitch, not the absence of delivery. Say cash-only, prominently, and the gap closes.

On premium, VNXAU trades at about 0.7% over spot on $36,000 a day. A fully registered, independently attested, named-custodian gold token with a five-year track record commands essentially no premium. Regulatory quality does not produce a premium. If a 3 to 8% premium is required for Aurumix's economics to work, the economics need rework, not the marketing.

On proof of reserve, VNX is the benchmark at this size and it is still not enough. The auditor is not independent and says so, the procedures exclude observing the gold and exclude assay, there is no bar list despite the serial-number claim, there is no live feed, reporting is annual with a three-month lag, and the auditor declines to opine on the register that is the actual basis of the property right. Meanwhile a five-year-old contract audit sits on the same transparency page under a 2026 URL. The bar to clear is low and specific: publish a bar list, use an attestor that is not your statutory auditor, report quarterly or better, and never let a contract audit and a reserve attestation share a page without labelling which is which.

Finally, VNX has published no wind-down plan, but it executed a partial, orderly, publicly noticed retreat with dated notices, a withdrawal window and explicit instructions. A de facto playbook worth studying. It also exposes the weakness of not committing in advance: the withdrawal window was 31 days, announced 11 days before the exchange closed, and any holder who was travelling, ill or simply inattentive is now holding an illiquid token with no issuer venue. Aurumix committing ex ante to a defined wind-down window, say 180 days, is cheap, differentiating, and directly answerable to what just happened here.

---

### 4.12 Midas GoldZip (XGZ)

| Field | Detail |
|---|---|
| Issuer | Two Singapore entities of the same name are implicated and the issuer's materials conflict. HKGX names GoldZip Pte. Ltd., UEN 202119587H. The token's website and CoinMarketCap name GoldZip Digital Pte. Ltd., UEN 202119588Z. Both incorporated 3 June 2021, and ACRA records the principal activity of both as "development of software and applications (except games and cybersecurity)". GoldZip is marketed as a subsidiary of the Hong Kong Gold Exchange (HKGX). Midas Labs is GoldZip's outsourced Web3 development contractor, not an issuer; its jurisdiction and registration number are not found in any register |
| Licence covering the token | None identified. The claimed status is a Singapore Ministry of Law registration under the Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019, an AML/CFT dealer registration for jewellers, bullion traders, pawnbrokers and auction houses. No MAS Capital Markets Services licence, no MAS Payment Services or DPT licence, no Hong Kong SFC authorisation found. One data platform lists XGZ as "Non-Regulated" |
| Assets under management | ~$5.06M, being 39,000 XGZ (39.0 kg of gold) at 28 July 2026, held by 264 holders. GoldZip has projected a US$300M reserve for H1 2026, standing at 1.7% of target |
| Backing | 1 XGZ = 1 gram of 99.99% fine gold in vaults accredited by HKGX. Whether the holder has legal title to identified bars, a beneficial interest under a declared trust, a bailment, or an unsecured contractual claim is not documented anywhere |
| Custody fee charged to holders | Not disclosed. Whether any storage fee is charged, and who bears the vault cost, is not disclosed. Management and performance fees recorded as 0% |
| Yield paid to holders | None. The gold is not lent or leased and there is no note programme |
| Redemption | Documented but not operational. Delivery stated as available "from 1,000 XGZ per delivery bar" (a 1 kg minimum, ~$129,700), with "standard settlement timelines and handling fees apply", fulfilment by pickup or delivery via authorised partners, subject to KYC/AML and jurisdictional rules. The documentation says "Step-by-step instructions, forms, and venue details will be published when redemption windows open". Seven months after launch, none has been published |
| Token standard | Plain ERC-20 on Ethereum only, 8 decimals, contract `0x69af64f409c08E9076bF7f3ed9Db3a7409717161`, owner `0xd173e69192b9ff22069aa913ef6e6e94b19f0778`. Freely transferable, no whitelist, no onchain permissioning. A 0.01% transfer fee is levied onchain and paid by the sender. Proxy pattern, pause, freeze, blacklist and forced-transfer functions, and admin key custody are all undisclosed |
| Reserve verification | None published. The documentation promises "periodic attestation reports by accredited auditors" and has published none: no auditor named, no cadence, no report, no URL. No bar list, no Proof of Reserve feed. The documentation links a smart-contract audit file and a GitHub commit, but no auditor name or findings were retrievable |

#### What it is

XGZ is a gold-backed ERC-20 on Ethereum. One token represents one gram of 99.99% fine gold held in vaults accredited by the Hong Kong Gold Exchange. It launched on 23 December 2025.

Its distinguishing pitch is institutional parentage. HKGX, formerly the Chinese Gold & Silver Exchange Society, is Hong Kong's sole recognised gold exchange and is over 100 years old. GoldZip is marketed as "Asia's first gold token supported by a leading gold exchange". Midas Labs was named strategic Web3 development partner on 19 May 2026, with a stated one-to-two-year build horizon.

It is very small: 39 kg of gold, ~$5.06M, 264 holders. The average holding is roughly 148 XGZ, about $19,200. That distribution is institutional-shaped rather than retail-shaped.

One clarification, because the naming invites confusion. This protocol is unrelated to Midas / midas.app, the Berlin RWA tokenization platform issuing mTBILL, mBASIS, mBTC and mXRP through Midas Software GmbH under Midas Protocol Limited (UK company 15217097). No source establishes any corporate relationship between the two. That other Midas, which does operate under a European prospectus wrapper passported across the EEA, issues no gold-backed or gold-linked product at all. There is likewise no token, product or ticker called "mXGZ" on the issuer's documentation, HKGX, any exchange, or any data platform. The real token is plain XGZ, a non-yielding one-gram gold token.

#### Legal structure and regulatory standing

What a holder actually owns is not documented, and that is the central gap.

The issuer's documentation, HKGX's product page and every listing describe XGZ as "backed by" gold and give holders a redemption right subject to KYC/AML. None states whether the holder has legal title to identified bars, a beneficial interest under a declared trust, a bailment, or an unsecured contractual claim against the issuer. No prospectus, base prospectus, terms and conditions of notes, final terms, offering memorandum or published terms of issue exists for XGZ. The issuer's site, the full documentation index, HKGX's site and RWA data platforms were all searched. The GoldZip website footer references "Terms & Conditions", "Rules" and "Legal Policy" pages, but no operative gold-title or insolvency provision could be retrieved from them.

What happens to holders on issuer insolvency is not disclosed. There is no segregation statement, no trust account, no ranking in a winding-up, no wind-down plan. One data platform carries the label "Account Segregation: Bankruptcy Remote" for XGZ. Nothing in the issuer's documentation supports it: no named trustee, no trust deed, no declaration of trust, no jurisdiction for a segregation structure. Treat that label as unsupported. Absent any of that, the defensible reading is that an XGZ holder has a contractual redemption claim against a Singapore private limited company whose registered business activity is software development.

No financial-services licence exists in any jurisdiction, and the claimed status is routinely misread. GoldZip Digital Pte. Ltd. appears on the Singapore Ministry of Law registered dealers list, while HKGX attributes that registration to GoldZip Pte. Ltd. The two claims conflict. Either way, registration under the Precious Stones and Precious Metals (Prevention of Money Laundering and Terrorism Financing) Act 2019 is an AML/CFT registration administered by the Ministry of Law, applying to jewellers, bullion traders, pawnbrokers and auction houses. It is not a prudential licence, not a securities or capital-markets authorisation, and confers no permission to issue an investment product, hold client assets, or offer tokens to the public.

The marketing compresses this into "regulated by the Ministry of Law (MinLaw) in Singapore" on goldzip.info, repeated verbatim by CoinMarketCap, and in the July 2026 partnership release into GoldZip "holding a full regulatory compliance license in Singapore". That last phrasing is materially misleading. There is no such licence. The registry check adds a third problem: ACRA records the principal activity of both GoldZip entities as software development, neither carries a precious-metals or financial-services activity code, and both were incorporated on 3 June 2021, two and a half years before the token launched.

#### Custody and reserve verification

The custodian is not disclosed by the issuer. The documentation says only "licensed gold vaults accredited by HKGX". One data platform asserts Brink's Global Services, unconfirmed by any issuer document. The vault city is not disclosed and is only implied to be Hong Kong through the HKGX depository relationship. There is no allocation or segregation language anywhere, no published bar list (the documentation refers generically to "GoldZip Eligible Gold Bars" and "selected specified brands"), and no Proof of Reserve oracle. Insurance is claimed as "insured vaults" in secondary coverage only, with no insurer, policy or limit disclosed.

On the audit-versus-attestation distinction, GoldZip is on the right side of the wording and the wrong side of the substance. Its documentation uses the correct phrase, "periodic attestation reports by accredited auditors", which is reserve language rather than code language. It has published none: no auditor named, no cadence, no report, no URL. Meanwhile the only artefact that appears to exist is a smart-contract audit file linked from the documentation alongside a GitHub commit, with no auditor name or findings retrievable and no published report found in any audit-firm index. The one thing plausibly audited is the code, and the 39 kg of gold has no published attestation at all. For a token whose entire proposition is exchange-grade custodial credibility, that is the largest evidentiary hole in the product.

#### Fees, revenue and redemption

| Fee line | Amount |
|---|---|
| Mint / subscription | Not disclosed |
| Onchain transfer fee | 0.01% of transfer amount, paid by the sender |
| Ongoing custody / storage | Not disclosed whether any is charged |
| Redemption | "Handling fees apply", amount not disclosed |
| Management / performance | 0% / 0% |
| Yield to holders | None |

The transfer fee is the one genuinely unusual mechanism here. XGZ levies a protocol-level 0.01% fee on every onchain transfer, taken from the sender. PAXG, XAUT, XAUm, VNXAU and Comtech Gold all charge zero on transfer. It converts velocity into revenue rather than taxing the balance.

Who pays for the vault is not disclosed. With a 0% management fee, no disclosed storage fee, and an undisclosed mint fee, the only visible recurring revenue line is 0.01% of transfer volume. Against 39 kg of gold that is negligible: even at $113,000 of daily turnover, 0.01% is roughly $11 a day, about $4,100 a year. Real vaulting, insurance and assay costs for 39 kg exceed that comfortably. The economics work only if HKGX absorbs the cost as a strategic loss-leader, an inference rather than a disclosure, and it is the same revenue starvation that killed Paxos's PMGT.

Issuance is wholesale and members-only. Only KYB-verified HKGX members can mint XGZ, by depositing physical gold into the vault. The described process is to accept gold from trusted refineries meeting specification, conduct international assay verification of fineness, then issue XGZ onchain for distribution through exchanges and distributors. Eligible metal is tightly specified as minimum 1 kilogram bars of 999.9 fine gold from selected brands. Minimum mint size and mint fees are not disclosed. Retail participation exists only on the secondary market.

Redemption is documented and not operational. The eligibility arithmetic is severe. Minimum redemption is 1,000 XGZ, roughly $129,700. Total supply is 39,000 XGZ across 264 holders, an average holding of about 148 XGZ or $19,200. The average holder sits roughly 6.8 times below the redemption floor. Combined with a members-only mint, XGZ is for most holders a one-way instrument with no primary-market exit at all. Eligibility is limited by a bar-sized minimum plus unpublished jurisdictional rules, and Hong Kong residents are excluded outright.

#### Liquidity and distribution

XGZ has a market cap of ~$5.06M on ~$113,000 of daily volume (2.2% turnover) across 264 holders, and trades at $129.68 against spot of roughly $131.50 per gram: a discount of about 1.4%.

Liquidity is almost entirely custodial rather than onchain. The MEXC XGZ/USDT pair accounts for 92.4% of volume at about $104,000, BitKan adds roughly $8,200, and the two Uniswap V4 pairs combined turn over under $320 a day. The all-time high of $162.73 on 7 July 2026 against an all-time low of $126.60 on 30 June 2026 is a 28% range in five weeks, for an instrument tracking a metal that moved a fraction of that. A thin, gappy market rather than a tracking one.

The discount is the interesting part, and its mechanism is visible. Arbitrage cannot close it, because you cannot mint unless you are an HKGX member and you cannot redeem below 1 kg. No ordinary participant can buy the discount and redeem into metal.

Distribution offers nothing. No savings plan, no recurring purchase, no referral or affiliate scheme, no agent network. The channel is HKGX member institutions at the primary level, then a MEXC listing and a Uniswap pool for everyone else, plus unnamed "exchanges and distributors". The target segment is Asian institutional and semi-professional gold traders already inside the HKGX orbit, and Hong Kong residents are excluded. The one distribution-shaped initiative is a non-binding memorandum of understanding signed 2 July 2026 with Universal Digital Intl Limited (an ADGM-based issuer of the USDU stablecoin) and Midas Labs, to explore linking the UAE's regulated stablecoin ecosystem with Asian digital gold. It establishes "a framework for further dialogue" with no binding commitment and no product. A business-to-business liquidity partnership, not a retail channel.

#### Relevance to Aurumix

XGZ trades at a discount, and the reason explains the whole premium question.

A members-only mint restricted to HKGX members, combined with a 1 kg redemption floor against an average holding of 148 grams, closes both correction paths: arbitrage can neither close a discount nor sustain a premium. Nobody outside the member set can mint into strength, and almost nobody inside the holder base can redeem into weakness. The price is free to wander in either direction. That is the general rule the whole premium thesis turns on: a token's price tracks its metal only to the extent that ordinary participants can convert in both directions at a known cost. Aurumix should read that as a constraint on its own design rather than as a criticism of XGZ, because a premium thesis depends on supply discipline, which sits uneasily with continuous SIP inflows and no hard cap.

The second finding is negative and decision-relevant. An exchange-owned gold issuer with a 115-year-old parent, sitting on real vaulted metal, chose not to generate yield on it. XGZ pays nothing, the gold is not lent or leased, and there is no note programme. Meanwhile the unrelated Midas that does have the European prospectus wrapper issues no gold product at all. HKGX has better access to bullion-leasing counterparties than Aurumix ever will, and it left the gold idle. That is evidence about the risk-adjusted attractiveness of encumbering reserve gold, from the most credible institutional operator in the comparison set. It strengthens the case for keeping the gold token clean and selling any yield as a separate instrument.

Four further read-acrosses:

- Do not present a trade or AML registration as authorisation to issue a token. GoldZip presents a Ministry of Law AML dealer registration as "full regulatory compliance license in Singapore". That is the same category error as a free-zone precious-metals trade licence presented as authorisation to issue a token, and it is now the second documented example in this set. The gap between the two is exactly where enforcement risk lives. If Aurumix is tempted to lean on a DMCC, DAFZA or free-zone trade licence in lieu of VARA, this is the pattern to avoid, and to avoid describing.
- A permissioned perimeter with a permissionless token binds at the edges and evaporates in the middle. GoldZip wants members-only minting, KYC redemption and Hong Kong residents excluded, and implemented a plain transferable ERC-20. Excluded persons can hold it and nothing onchain stops them. The only enforcement mechanism actually implemented onchain is a 0.01% fee. AURX would carry ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on exactly the anonymous transfer XGZ permits. XGZ is what Aurumix's design looks like if permissioning is deferred.
- An unexercisable redemption promise is worse than an honest cash-only exit. XGZ advertises physical redemption while the process, forms, venues, fees and timeline "will be published when redemption windows open", seven months after launch. Layered on a 1 kg minimum against a 148-gram average holding, effectively all holders are ineligible in practice. Aurumix's cash-buyback-only design, stated clearly up front, is more defensible. Do not soften Aurumix's disclosure to match competitor marketing. The competitor marketing is the liability.
- A 0.01% sender-paid transfer fee is a velocity tax rather than a balance tax, and it is peg-neutral. It does not touch the gram count, so a price equals grams divided by tokens formula holds, and it does not punish long-term holders. But the arithmetic (~$4,100 a year against 39 kg) shows it cannot fund custody at small scale, the same revenue starvation that killed PMGT. Useful as a mechanism, insufficient as a business model.

One live lead is worth recording. The 2 July 2026 memorandum surfaces Universal Digital Intl Limited, holding ADGM FSRA financial services permission number 250089 and registered with the Central Bank of the UAE as a Foreign Payment Token issuer under the Payment Token Services Regulation. That is a concrete, verifiable UAE authorisation adjacent to the ADGM route. Two caveats: the permission is to issue Fiat-Referenced Tokens to Professional Clients, the opposite of a mass-retail gold product, and the memorandum is explicitly non-binding with no product behind it. Useful as a register lead and a named comparator, not as a template.

On proof of reserve, GoldZip promises "periodic attestation reports by accredited auditors" and has published none, while apparently holding a smart-contract audit. For a product whose retail pitch is that every dollar buys physical gold, shipping the attestation before the marketing is cheap and genuine differentiation. On wind-down, XGZ discloses nothing: no insolvency provision, no segregation, no trustee, no plan. That differentiation opportunity remains unoccupied.

---

## SOURCES: Digital Gold (DGLD)

- https://dgld.ch/legal/general-terms-conditions-dgld-2
- https://dgld.ch/about-us
- https://dgld.ch/verify
- https://dgld.ch/news/dgld-complete-step-by-step-guide-november-2025
- https://dgld.ch/news/post-incident-report-february-2026-exploit
- https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262
- https://github.com/goldtokensa
- https://etherscan.io/token/0xA9299C296d7830A99414d1E5546F5171fA01E9c8
- https://basescan.org/token/0xe908475f8Beb7A138B0dc6eb5A05cb27068ffB9A
- https://www.prnewswire.com/news-releases/dgld-the-only-gold-token-backed-by-60-years-of-swiss-precious-metals-heritage-launches-on-base-network-via-aerodrome-302643330.html
- https://www.prnewswire.com/news-releases/coinshares-dgld-consortium-allows-investors-to-redeem-gold-tokens-for-physical-bullion-301152528.html
- https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956

## SOURCES: Aurus (tGOLD)

- https://aurus.org/Terms%20and%20Conditions%2012Nov2024.pdf
- https://aurus.org/
- https://aurus.org/aurusx
- https://find-and-update.company-information.service.gov.uk/company/11703940
- https://find-and-update.company-information.service.gov.uk/company/11703940/officers
- https://find-and-update.company-information.service.gov.uk/company/14194058
- https://find-and-update.company-information.service.gov.uk/company/14194058/filing-history
- https://etherscan.io/token/0xe4a6f23fb9e00fca037aa0ea0a6954de0a6c53bf
- https://polygonscan.com/token/0xa6da8c8999c094432c77e7d318951d34019af24b
- https://api.llama.fi/protocol/aurus
- https://support.cex.io/en/articles/6701340-important-updates-for-aurus-tokens-awg-aws-awx
- https://register.fca.org.uk/

## SOURCES: VNX Gold (VNXAU)

- https://vnx.li/wp-content/uploads/2026/03/VNX_Examination_on_Management_Assertions_VNXAU_31_12_2025_signiert.pdf
- http://vnx-terms.s3.amazonaws.com/VNX-FRT-Terms.pdf
- https://register.fma-li.li/
- https://www.fma-li.li/en/media-public/client-protection/safeguarding-client-protection-in-different-sectors/tt-service-providers
- https://vnx.li/gold/
- https://vnx.li/important-notice-upcoming-suspension-of-exchange-operations-on-the-vnx-platform/
- https://vnx.li/vnx-notes-bermuda-licence-obtained-by-group-entity/
- https://vnx.li/strategic-focus-on-supported-blockchains/
- https://vnx.gitbook.io/vnx-global/institutional/products/minting-and-redemption
- https://etherscan.io/token/0x6d57b2e05f26c26b549231c866bdd39779e4a488
- https://basescan.org/token/0xAc3FE22294beaED9d1FD752323a6d06D12Ff3098

## SOURCES: Midas GoldZip (XGZ)

- https://goldzip-1.gitbook.io/goldzip/goldzip-xgz/what-is-usdxgz
- https://goldzip.info/news/
- https://etherscan.io/token/0x69af64f409c08E9076bF7f3ed9Db3a7409717161
- https://acd.mlaw.gov.sg/list-of-registered-dealers/
- https://licensing.gobusiness.gov.sg/licence-directory/minlaw/registration-of-precious-stones-and-precious-metals-dealers
- https://www.acra.gov.sg/
- https://find-and-update.company-information.service.gov.uk/search?q=Midas+Protocol+Limited
- https://www.manilatimes.net/2026/07/02/tmt-newswire/pr-newswire/hkgx-backed-goldzip-and-the-uaes-universal-open-gold-stablecoin-corridor/2377222
- https://www.tmcnet.com/usubmit/-hong-kong-gold-exchange-subsidiary-goldzip-names-midas-labs-as-strategic-web3-/2026/05/18/10384806.htm
- https://decrypt.co/353315/hkgx-backed-goldzip-launches-xgz-asias-first-gold-token-supported-by-a-leading-gold-exchange
