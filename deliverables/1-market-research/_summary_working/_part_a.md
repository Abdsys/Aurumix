### 4.5 AZ Gold Reserve (AZG)

| Field | Detail |
|---|---|
| Issuer | Arizore LTD, "a corporation established under the laws of Nevis" per its own terms. No registration number, incorporation date or obtainable register entry. Related names: AZ Reserves Ltd, Arizore Ltd. (Bocana filings), Arizore LLC (Nevada JV vehicle) |
| Licence covering the token | None identified |
| Assets under management | $64,993,677 per the issuer's own reserve API, 28 July 2026 |
| Backing | 21,050 oz across 16,167.34 tokens: 62.0% in-ground mineral resource, 0% tailings, 38.0% bullion. Bullion per token 0.4948 oz. One AZG is priced at one troy ounce |
| Custody fee charged to holders | Not disclosed. A third-party listing shows 1.00% per annum, unsupported by any Arizore document |
| Yield paid to holders | None. Arizore pays yield to miners, not holders |
| Redemption | None committed. The Terms of Service state: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways" |
| Token standard | Plain ERC-20 on Ethereum, 18 decimals, behind an EIP-1967 upgradeable beacon proxy. Contract `0x45334126815c77be657c7906bf52c0f441a8831c`, source unverified. Sister token AZS at `0xee7eddf7793c1399407ba0b858852f64830f37a6` |
| Reserve verification | None published. A JSON endpoint returns six numbers with `lastUpdatedIso` set to `null`. No attestation, bar list, serial numbers, signature or oracle |

#### What it is

AZG is not a claim on vaulted metal. It is a claim on a pooled reserve whose majority component is unmined ore. A third-party aggregator classifies it as tokenized gold, "designed to provide digital access to verified gold resources, including bullion, in-ground reserves and tailings". The last clause is the accurate part. Arizore's own site is more careful, calling AZG a "Gold-linked reserve participation instrument".

The business underneath is mining finance. Miners pledge in-ground resources or tailings through forward contracts, valued after haircuts of 25% to 55% by region and resource type, and receive capital. AZG carries the pooled reserve out to investors. Arizore's phrasing: "turning verified reserves into usable collateral", letting miners "access liquidity without surrendering ownership".

#### Legal structure and regulatory standing

There is no whitepaper, offering memorandum or terms of issue. Arizore publishes a website Terms of Service and a Privacy Policy, both dated 27 November 2025, both site-usage documents rather than instrument terms. The Terms carry the entire published legal description of the token, under "Token Disclosures":

> "Arizore's ecosystem includes asset-backed digital tokens associated with verified reserves of in-ground resources, tailings, or vaulted bullion. These tokens may be characterized as security tokens under various regulatory frameworks."

> "The existence of a token does not imply rights beyond those expressly documented and contractually provided."

The word is association. Not ownership, title, trust or claim. Rights are whatever a separate unpublished contract says, since tokens "reflect audited and verified reserve structures and are subject to separate agreements". Public documentation does not establish whether AZG is a title claim, a trust interest, an unsecured creditor claim or a purely contractual exposure.

Registry verification was attempted and could not be completed. The Nevis FSRC registry at `registry.fsrc.kn` was unreachable on HTTP and HTTPS, and the FSRC states records may be examined only by a person "who has paid the prescribed fee... during normal hours", so no free public search exists. UK Companies House returns nothing for "Arizore" or "AZ Reserves". The Nevada Secretary of State search sits behind bot protection. ASIC, ACRA, the Hong Kong Companies Registry and the BVI registry return no entries under any Arizore name. The jurisdiction claim rests on the issuer's own assertion and cannot be checked by a member of the public.

No licence or registration was found anywhere. ASIC holds no Australian Financial Services Licence for Arizore Ltd, AZ Reserves Ltd, Arizore LLC, Black Tie Holdings or Black Tie Digital, which matters because a third-party listing asserts AZG sits under an AFSL via ASIC. The FCA, MAS, SFC, SEC, CFTC and BVI FSC hold no registrations, filings or exemption notices naming AZG, AZS, Arizore or AZ Reserves, and no prospectus or private-placement filing was found anywhere. No regulator has issued a warning or enforcement action either. AZG sits outside the perimeter in both directions.

Arizore concedes the securities characterisation rather than denying it, publishes no prospectus, and manages the exposure by restricting distribution. Its press release states AZG and AZS "are not investment products, are not yield bearing, and are not intended for retail distribution or public trading", with portal access granted "exclusively to individuals and entities that have completed a meet-and-greet call or preliminary verification phase". AZG is not a retail product and does not compete with Aurumix.

#### Custody and reserve verification

Arizore names no custodian, referring only to "vaulting and bullion partners". No vault, city, bar list, serial numbers or assay certificates. Bullion providers "relinquish ownership of the bullion" on transfer in, implying a pooled reserve unallocated to holders, though the terms never say so.

A third-party listing names "Gold Corporation" as custodian and carries LEI 213800HQZYBMURES6D84. Resolving that against GLEIF gives an unambiguous match: Gold Corporation, trading name The Perth Mint Refinery, East Perth, Western Australia, legal form "state government entity", ABN 98 838 298 431, active. The claim is that a Western Australian state-owned mint custodies the reserve behind an unlicensed Nevis token. Nothing corroborates it. The Perth Mint has made no statement, announcement or annual-report disclosure naming Arizore, AZ Reserves, AZG or AZS, and Arizore's website never mentions the Perth Mint, Gold Corporation or Australia. Gold Corporation was the entity behind PMGT and exited tokenization by commercial abandonment. Black Tie Digital is Australian-based and the launch release is datelined Sydney, which makes the claim superficially plausible. Treat it as unsupported until the issuer produces a custody agreement.

Neither an attestation nor a contract audit exists. A third-party listing names KPMG as auditor; no KPMG report, engagement or reference appears on any Arizore page or in any public source. Arizore's terms use "audited" once, without an auditor, standard or date, and the contract is not source-verified on Etherscan or Blockscout. What sits in place of reserve verification is geological reporting: the Bocana joint venture release commits to "technical reports and studies compliant with NI 43-101", a rigorous Canadian standard that certifies mineral resource estimates rather than vaulted bullion. It is doing duty as the verification backbone for a product sold as tokenized gold.

The published "proof of reserve" is a JSON endpoint returning six numbers, `lastUpdatedIso` set to `null` so the feed carries no timestamp. No cryptographic proof, no third-party signature, no onchain oracle.

#### Fees, revenue and redemption

Arizore publishes no fee schedule. Every fee figure in circulation comes from a third-party listing demonstrably wrong on issuer name, auditor, custodian and regulatory status, so treat all as unverified: a 100,000 USDT minimum, a 1.00% per annum management fee, and a 0.50% redemption fee with a 5,000 USDT minimum.

The economically real revenue line is the haircut. Arizore takes in-ground resource at 45% to 75% of assessed value and issues against it at spot-linked pricing. That spread, plus interest on "up to USD $60,000,000 in secured funding loans" committed to the Bocana joint venture, is the business.

The backing arithmetic is where the structure shows. Against spot gold of $4,019.80 on 28 July 2026:

| Measure | Value |
|---|---|
| AZG token value, per issuer API | $4,020.06 |
| Spot gold, same day | $4,019.80 |
| Ratio | 1.0001. One token is priced as exactly one ounce |
| Stated reserve per token | 21,050 oz ÷ 16,167.34 tokens = 1.3020 oz |
| Implied value per stated ounce | $64,993,677 ÷ 21,050 = $3,087.59, or 76.8% of spot |
| Bullion component only | 38.0% × 21,050 oz = 8,000 oz, worth $32.16M |
| Actual bullion per token | 0.4948 oz = $1,989, or 49.5% of the token's own stated price |

Three things follow, arithmetic rather than opinion. The token is priced at one ounce while holding roughly half an ounce; the other half is a discounted claim on unmined ore against an unnamed counterparty under an unpublished forward contract. The 76.8%-of-spot implied reserve value is the haircut showing through, and the structure is internally consistent to the cent, since tokens multiplied by token value equals stated reserve value exactly. Reserve value is therefore derived from token price rather than measured independently, so the proof of reserve restates the issuer's own valuation assumptions. And the holder carries mining execution risk: if a pledged deposit is not mined, is mined at higher cost, or the miner defaults, the in-ground 62% does not become gold. No remedy, insurance or over-collateralisation beyond the haircut is disclosed, and nothing states where a holder ranks against the miner or Arizore's other creditors.

The two redemption sources contradict each other. A third-party listing states redemption is "instant" at 0.50% with a 5,000 USDT minimum. Arizore's Terms of Service state that "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways". The terms bind, so there is no committed redemption in metal or cash, and no minimum, eligibility rule, settlement window or fee attached to one. The word "redemption" appears exactly once in Arizore's published corpus, in the sentence disclaiming it.

#### Liquidity and distribution

AZG has roughly $65M to $66M of stated assets and no market: no decentralised exchange pool, no listing, no order book, no quoted bid. The $4,020.06 price is a number the issuer computes and serves from its own API. Nobody has traded at it. Lifetime activity is 61 transfers among 21 holders between 11 March and 10 July 2026, clustered in bursts consistent with manual allocation rather than trading. The largest holder controls 6,177 AZG, 38.2% of supply; the top two hold 76.9%.

Distribution runs through a meet-and-greet call, manual due diligence, a password-gated portal and a reported 100,000 USDT minimum. No savings plan, recurring purchase, referral programme, affiliate network, agent tier or retail channel. Secondary access is said to run through the BTX marketplace operated by Black Tie Holdings and Black Tie Digital, an Australian group that built Arizore's infrastructure. No licence was found for any Black Tie entity.

Two overhangs sit against the structure. London Gold LLC moved in mid-July 2026 toward a US$25M cash-and-stock acquisition of Bocana Resources, the Canadian reporting issuer that is Arizore's joint venture partner and the disclosure window onto the in-ground backing; no public statement addresses what happens to AZG's in-ground component if Bocana changes hands. And the current AZG and AZS contracts were deployed on 10 July 2026, five months after Arizore's February 2026 release stated "all tokens have been minted, issued, and confirmed on-chain". No migration was announced, and the transfer history on the current address begins 11 March 2026, before the contract's own creation date.

Bocana's market capitalisation at the time of the joint venture was roughly $2.17M. Arizore Ltd, with no published accounts, named directors, auditor or licence, committed up to $60,000,000 in secured loans to a joint venture with a company one twenty-eighth its size. AZG's entire stated reserve is $65M, the same order of magnitude, suggesting AZG subscriptions are the intended funding source. Arizore names exactly one officer anywhere: George Boot, Chief Marketing Officer.

#### Relevance to Aurumix

AZG is not a competitor and should not be benchmarked as one. Its value is as a boundary case showing where "gold-backed" stops meaning gold-backed, and as proof that a headline assets figure on an aggregator can be structurally hollow. If AZG turns up on a league table next to PAXG and XAUT, the answer is the arithmetic above: a $66M headline that is 38% metal, with no market, no attestation and no redemption.

**The one structural idea worth taking.** Arizore pays no yield to AZG holders. It pays yield to miners, through a password-gated Mining Participation Program promising "up to a maximum Annual Yield of 15.00%", distributed quarterly in USDT after a 45-day deferment, allocated by a "Contribution Index" scored on reserve contribution, commitment duration and delivery performance, with the heaviest weight on delivery performance measured as volume delivered against contract and timing against schedule. Under-delivery in a quarter "will result in the forfeiture of that quarter's Annual Yield allocation".

Copy that mechanic into the ICS Dividend. The yield is conditional on a real external performance obligation and forfeited automatically when the obligation is missed, which is the structural opposite of the pattern that broke Kinesis and PGOLD, where yield was funded by recycled investor fees and promised unconditionally. A forfeiture condition tied to a verifiable external event is cheap to build and largely absent from this market. Pay from a defined external source, and let the entitlement lapse when the source underperforms, rather than promising a percentage the fee base cannot fund. Arizore fails to make its own version credible because it publishes nothing behind it: no revenue, no accounts, no attestation, no statement of the profit pool's size, and the page sits behind a password. A conditional yield only beats an unconditional one if the condition is publicly verifiable. Take the forfeiture mechanic and publish the numerator.

**The one thing Aurumix must never do.** Blend an asset the holder can verify with one the holder cannot, then price the blend as if it were all the verifiable one. AZG charges one ounce of gold for half an ounce plus a discounted claim on a mine. Aurumix's pitch is that 100% of every dollar buys physical LBMA gold, and its peg is vault grams divided by tokens. Any future temptation to admit non-vaulted assets, whether gold leases, receivables or forward purchases, breaks that sentence and the peg formula together.

Four further points transfer directly:

- **Proof of reserve must carry a timestamp, a named third-party signature, and a metal quantity stated independently of the token price.** AZG's feed has none of the three, and its reserve value is arithmetically identical to tokens multiplied by the issuer's own token price. Reserve value derived from token price proves nothing.
- **Publish buyback terms where aggregators scrape them.** A listing advertised "instant" redemption at 0.50% for a token whose own terms disclaim redemption entirely. Third-party listings will invent terms, and the issuer will be held to them.
- **A legal restriction the code cannot enforce is not a restriction.** Arizore concedes the token may be a security, declares it not for retail distribution, then deploys a plain unrestricted permissionless ERC-20 with unverified source behind an upgradeable beacon proxy. Nothing stops a holder transferring to anyone. This is also the case for deciding upgradeability explicitly: a single externally owned account with 8 lifetime transactions controls a beacon that can replace the token logic for every holder at once, and the contract is pausable.
- **Opacity is not free.** Arizore incorporated where verification is impossible, and an aggregator attached a false custodian, a false auditor and a false regulator to it without contradiction. For a savings product selling to Indian and NRI retail on a trust proposition, that trade is fatal.

On wind-down, AZG publishes nothing, and its position is worse than the failed protocols: a majority of its reserve is in-ground resource that cannot be distributed in a wind-up, because an unmined ounce cannot be delivered. Add the unresolved Bocana takeover. Publishing a wind-down plan remains cheap differentiation for Aurumix.

---

### 4.6 Matrixdock Gold (XAUm)

| Field | Detail |
|---|---|
| Issuer | Matrix Mining Limited, an SPV held under a special purpose trust. Not in any searchable register. BVI domicile reported by a single secondary source, unconfirmed. Trustee: Appleby Global Services. Enforcer: Hamilton Services. Marketed as Matrixdock, "a brand wholly-owned by Matrixport" |
| Licence covering the token | None identified. Group affiliates hold licences that do not attach to XAUm |
| Assets under management | ~$52.7M, up 7.14% over 30 days |
| Backing | 1 token = 1 troy oz of 99.99% LBMA-accredited gold in 1kg bars at Brink's and Malca-Amit vaults, Singapore and Hong Kong. ERC-20 holders have dynamic allocation to the pool, not a fixed bar. Reserves 16,299.036 oz against 12,882.21 tokens |
| Custody fee charged to holders | 0%, explicitly reversible on 30 days' notice |
| Yield paid to holders | None. No yield, APY, leasing, lending or rehypothecation |
| Redemption | Two paths, both KYC-gated. Stablecoin in USDC or USDT at T+3, 0.25% fee. Physical at a minimum of 32.148 XAUm (one 1kg LBMA bar, roughly $130,000), Singapore and Hong Kong only, requested at least T+3 in advance. The 0.25% fee is charged in token, not cash |
| Token standard | Plain ERC-20 on Ethereum (0x2103E845C5E135493Bb6c2A4f0B8651956eA8682), plus BEP-20, SPL/Token-2022 on Solana, TRC-20 on TRON, and native formats on Sui and Stellar. Nine chains. Not permissioned at the transfer layer. A separate BullionNFT (ERC-721) gives fixed allocation to one bar |
| Reserve verification | Bureau Veritas, semi-annual physical count, each bar individually weighed and measured. Second report 31 July 2025 covering 421 x 1kg bars = 13,534.308 oz. Four report files posted. An onchain proof-of-reserve oracle caps a Global Mint Budget across all nine chains. No public bar list |

#### What it is

XAUm is the tokenized gold product of Matrixdock, Matrixport's real-world asset platform. Each token represents one troy ounce of 99.99% LBMA-accredited gold in 1kg bars at Brink's and Malca-Amit vaults in Singapore and Hong Kong. It launched in September 2024 and sits at roughly $52.7M across nine chains.

XAUm out-documents much larger competitors on mechanics, with one qualification. On fees, custody, audit, contract architecture and cross-chain reserve accounting its disclosure is the strongest in this cohort. On legal identity it is arguably worse: the issuing entity cannot be found in any register and no officer is named anywhere. Deep on operations, thin on who is legally responsible.

Its structural distinction against Aurumix is that XAUm is an institutional bullion instrument wearing a token. Sized in 1kg bars, priced for wholesale, settling at T+3, trading on a bullion-market order window rather than crypto's 24/7 clock. No retail savings mechanic of any kind.

#### Legal structure and regulatory standing

The disclosed stack runs: holders hold XAUm; Matrix Mining Limited is the issuer SPV; the SPV is owned by a special purpose trust; the trust holds gold through custodians. Matrixdock states this follows sibling product STBT's "innovative bankruptcy-remote design" and that gold ownership belongs to "the asset holder entity under Matrixdock's SPV at all times".

What the holder owns is not stated. Issuer materials describe holders as having "the rights to redeem the underlying physical gold" and the token as "backed by" gold. Neither is a statement of legal title. No public document says whether a holder is a beneficiary under the purpose trust, the owner of specific bars, or an unsecured contractual claimant against Matrix Mining Limited. The trust deed and token terms are not public, and the GitBook index lists an "XAUm Terms and Conditions" page whose document is an embedded file that does not render as text.

The trust's purpose repays a careful reading. A purpose trust with an enforcer, here Hamilton Services, is the classic BVI and Cayman orphan-SPV structure. Its function is to make the issuer bankruptcy-remote from the sponsor, so Matrixport's creditors cannot reach the gold. It confers no automatic beneficial interest on token holders. Orphan structures are usually set up so that nobody is a beneficiary, which is exactly why an enforcer is needed. The structure that reads as investor protection is, on its face, sponsor-insolvency protection, and whether it also protects holders depends entirely on the undisclosed deed.

The issuer holds no financial services licence in its own name and no XAUm document claims authorisation. A register search for "Matrix Mining Limited" produces no match tied to Matrixdock or Matrixport in any searchable jurisdiction, and the BVI Financial Services Commission, the MAS directory, the Hong Kong SFC register, the Cayman Islands Monetary Authority, VARA and the ADGM FSRA hold no listing.

Licences that exist belong to other entities. Matrixport group holds a Hong Kong trust and money lender licence, a US money services licence, a Swiss FINMA asset management licence, and an MAS Major Payment Institution licence granted to subsidiary Fly Wing Technologies Pte Ltd in March 2025. InvestaX, which distributes XAUm, is separately MAS-licensed. None attach to Matrix Mining Limited or to XAUm. A reader who sees "Matrixport is MAS-licensed" next to XAUm draws a false conclusion.

The Terms of Use disclaim that anything constitutes "an offer or a solicitation of an offer to buy or sell any products or services, including but not limited to any securities", plus a prohibited-countries list. Compliance runs on KYC and gated mint and redeem access rather than a product licence: every mint and redeem requires a Matrixdock account, KYC verification and a bound wallet.

#### Custody and reserve verification

Brink's is primary custodian, Malca-Amit second, across Brink's Hong Kong, Brink's Singapore and Malca-Amit Singapore at Le Freeport. Bars are specific and individually weighed, but ERC-20 holders hold dynamic allocation to the pool. Fixed allocation to one 1kg bar requires converting the right quantity of XAUm into a BullionNFT, which "cannot be redeemed by another".

Three separate things exist here that issuers usually blur into "audited". The reserve attestation: Bureau Veritas physically counts and weighs bars semi-annually, and "each bar was individually weighed and measured to verify the accuracy of its physical specifications and to confirm its consistency with recorded vault data." The second report, 31 July 2025, covered 421 x 1kg bars totalling 13,534.308 oz, and four report files are posted. The code audits: four of them, BlockSec for EVM, Zellic for Sui, Accretion and Sec3 for Solana, examining code and saying nothing about gold. And the proof-of-reserve oracle, which is the genuinely interesting engineering. An onchain oracle on Ethereum mainnet gates a Global Mint Budget and per-chain Local Mint Budgets. Multi-chain gold tokens usually risk minting more tokens than gold because each chain accounts separately; XAUm's Global Mint Budget makes cross-chain over-issuance a contract-level impossibility rather than a promise, and almost nobody else in this market has it.

Two caveats. Brink's insurance was stated at US$50M as of 29 November 2024, below the current ~$52.7M reserve value and a gap that widens as the product grows, though vault insurance terms are usually more nuanced than a headline number. And no bar list is public, so the Bureau Veritas count is a trusted third-party assertion rather than something a holder can reconcile. The transparency page's asset-statement table currently renders "No results".

The reserve-to-supply gap is favourable and unexplained: 16,299.036 oz against 12,882.21 tokens, roughly 26% more metal than tokens, and Matrixdock does not comment. The likeliest reading is unsold inventory pre-positioned to support minting rather than surplus backing per token, and it should not be presented as a 126% backing ratio without confirmation.

#### Fees, revenue and redemption

| Fee line | Rate | Status |
|---|---|---|
| Minting / subscription | 0.25% | Waived until total value locked reaches $100M |
| Redemption, stablecoin | 0.25% | Active |
| Redemption, physical | 0.25% | Active, charged in token |
| Ongoing management | 0% | Reversible on 30 days' notice |
| Storage / custody | 0% | Reversible on 30 days' notice |
| Physical delivery / shipping | Not disclosed | Secured delivery offered, cost not published |

XAUm markets zero storage and management fees, and its own documentation reserves the right to change that: "any change will be communicated via official channels and at least 30 days advance notice will be provided." XAUm has not solved custody costs. It is subsidising them and has retained the contractual right to stop.

With the mint fee waived and no custody fee, the only live revenue line is 0.25% on redemptions, and redemptions are the one activity the business does not want to encourage. The waiver began 8 November 2024 and runs until $100M in total value locked, so at ~$52.7M it is roughly halfway to expiry. At ~$52.7M of gold, commercial allocated vault-and-insure cost runs on the order of 0.1% to 0.5% per year, so $50,000 to $260,000 annually. Monthly transfer volume is roughly $28.7M, but transfers are neither mints nor redeems and generate no fee. Redemption income at 0.25% would need $20M to $100M of annual redemptions to cover custody alone, implausible against a $52.7M book. Matrixport funds the gap, not the product. That is coherent strategy for a large group that invested $3M into XAUm directly in July 2026 and treats it as a strategic reserve asset, but it is a parent-subsidised land grab rather than a self-funding fee model, and the 30-day notice clause is the issuer saying so in writing.

Physical redemption works and has been executed. Matrixdock completed the first on 22 April 2025 at Malca-Amit's Le Freeport vault in Singapore: one 1kg bar, redeemed by an unnamed investor who transferred 32.22837 XAUm to receive 32.148 oz, the difference being the 0.25% fee. The fee is taken in token rather than cash, and that in-kind deduction works here precisely because XAUm's peg is defined per token (1 token = 1 oz) rather than as a pool ratio. At roughly $4,000 gold the 1kg minimum is a ~$130,000 ticket, so physical redemption is real but wholesale only; a small holder's exit is the secondary market. Eligibility is defined by KYC and geography rather than an undefined "qualified holder" category, cleaner than several peers.

#### Liquidity and distribution

XAUm carries ~$52.7M of market capitalisation on 12,882.21 tokens, with 52,858 holders, 643 active addresses over 30 days, and monthly transfer volume of $28,717,225 across 14,639 transfers. It trades on KuCoin spot, HTX and InvestaX, plus decentralised exchange liquidity across chains. A transfer-volume-to-market-cap ratio of roughly 0.54x monthly is far healthier than PGOLD's sub-$20 daily volume, so this is a real market rather than a parked balance. But read the holder figure against the product design: 52,858 holders, 643 monthly active addresses, and a 1kg physical redemption minimum. Those holders are overwhelmingly small, passive, secondary-market buyers who could never redeem physically. The distribution is retail; the product design is institutional.

Public mint and redeem quotes were $4,051.73 and $4,020.97, a spread of $30.76, about 0.76%. That is the number that matters most for the premium question. A continuously operating two-way primary window at a sub-1% spread puts a hard ceiling on any secondary premium.

Distribution runs through the Matrixdock web app under KYC, centralised exchanges, InvestaX for accredited and institutional flow, and cross-chain deployment onto Plume, HashKey, Stellar and Solana. Geography is Asia-centred with a prohibited-countries list. No savings plan, recurring purchase, referral programme, affiliate scheme or agent tier. The strategy is chain expansion and venue listings, being present wherever crypto capital already sits rather than recruiting new savers.

#### Relevance to Aurumix

XAUm is the best-run control group in this cohort: the same asset, the opposite strategy. Its answers are mostly warnings rather than templates, because it monetises the opposite end of the market.

**Custody fee.** XAUm charges no custody fee and currently no mint fee, funding vaulting from the Matrixport balance sheet while reserving the right to change with 30 days' notice. Even the best-capitalised operator in the category would not commit to free storage permanently in writing. If Aurumix ever markets "no storage fees", copy the 30-day notice clause verbatim.

XAUm never faces Aurumix's peg problem, which matters more. Because 1 token equals 1 fixed ounce rather than a share of a pool, XAUm can deduct fees in gold, and does so on redemption, without breaking anything. Aurumix's grams-divided-by-tokens design is exactly what makes in-kind fees destructive. The fee mechanism follows from the peg design, so the peg choice comes first.

**Dividend funding, answered by absence.** XAUm pays zero yield. No APY, no leasing, no lending, no rehypothecation. The most institutionally sophisticated issuer in this set, with LBMA supply chains, Brink's vaults, real bullion-desk relationships and a large parent balance sheet, pays holders nothing. That is not an oversight. It is what unencumbered allocated gold actually returns. PGOLD promises 5% and cannot fund it; XAUm could plausibly attempt leasing and declines to. Any Aurumix yield story has to explain why it can do what Matrixport chose not to.

**Token standard.** XAUm uses plain ERC-20 across nine chains, permissioned only at the mint and redeem gate. It can afford that because the token confers no rights that survive a transfer: no yield, no governance, no tier standing. Nothing breaks when it moves to an anonymous wallet, because the wallet's only privilege, redeeming, is re-gated by KYC at the counter. Aurumix's token carries four things that do break on an anonymous transfer: ICS standing, dividend entitlement, credit eligibility and buyback rights. Permissioning is required in proportion to how much offchain entitlement the token carries. XAUm carries none, so it pays nothing for freedom. Aurumix carries four, which is the actual argument for ERC-3643, and a stronger one than "compliance".

The controllerTransfer function is worth copying on its own merits. It lets the issuer move tokens without holder consent, and Matrixdock used it in production on STBT after the March 2025 Zoth hack, transferring 2,819,088.62 wSTBT out of a frozen vault on 3 July 2025. An issuer that can freeze and reissue after a hack is materially safer. The trade-off is that XAUm is transfer-free but not owner-sovereign.

**Redemption.** XAUm offers real physical redemption, executed and documented, at a 1kg (~$130,000) minimum in two cities. The lesson is not that Aurumix must offer redemption. It is that physical redemption can be offered at a threshold no retail saver will ever reach, preserving the "you own real gold" claim honestly at near-zero operational cost.

**Premium.** This weakens the 3% to 8% premium assumption. A competitor offering mint and redeem at a 0.76% spread caps what any tokenized gold product can sustain, because arbitrage is trivially available to anyone with a KYC account. PGOLD shows a premium cannot survive a thin market; XAUm shows it cannot survive a liquid one either. Aurumix's premium has to come from the savings-plan wrapper and switching costs, not from gold scarcity.

**Proof of reserve.** The benchmark to beat, achievable through procurement rather than innovation: semi-annual Bureau Veritas physical counts with individual bar weighing, four published reports, a proof-of-reserve oracle capping cross-chain supply, and four separate contract audits, with attestation and code audits kept clearly distinct. The one place Aurumix can beat it cheaply is a published bar list with serial numbers.

**Distribution.** No savings plan, recurring purchase, referral or agent commissions. XAUm accumulated 52,858 holders and only 643 monthly active addresses without any acquisition machinery, and it cannot deepen those relationships. Aurumix's agent network and monthly SIP are genuinely differentiated, and this is the clearest evidence in the cohort that the differentiation is real rather than assumed.

**Wind-down.** No published plan for the token. XAUm does have two structural protections nobody else here has: a bankruptcy-remote purpose trust isolating gold from Matrixport's creditors, and a contractual obligation that on custodian failure the custodian "shall promptly arrange for the return and delivery of all underlying gold in accordance with Matrixdock's instructions". That covers custodian failure and sponsor failure. It does not say what holders get if the issuer SPV fails, which is the case that matters.

**Regulatory route, with a caution about the wrong lesson.** XAUm operates unlicensed, compliant by KYC rather than authorisation, from an offshore SPV, selling into Asia. Aurumix cannot copy this. The ICS dividend and the credit facility are exactly the features that make a product regulated, and exactly the features XAUm does not have. Its unlicensed status is purchased by product simplicity, not clever structuring. Price each bolt-on feature against the licensing burden it triggers.

One shape is worth carrying away. XAUm discloses everything about the gold and almost nothing about the company: no searchable register entry, no named officer, no public token terms or trust deed. Excellent operational transparency and unverifiable legal identity coexist comfortably here, which is a useful warning against reading "well documented" as "well accountable".

---
