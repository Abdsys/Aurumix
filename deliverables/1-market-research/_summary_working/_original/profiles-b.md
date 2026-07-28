### 4.5 AZ Gold Reserve (AZG)

| Field | Detail |
|---|---|
| Issuer | Arizore LTD, stated in the issuer's own terms as "a corporation established under the laws of Nevis", registered address The Provident House, Central Government Road, Charlestown, Nevis. No registration number or incorporation date is published, and no register entry could be obtained. Related names appearing in different documents: AZ Reserves Ltd, Arizore Ltd. (Bocana filings), Arizore LLC (Nevada joint venture vehicle) |
| Licence covering the token | None identified |
| Assets under management | $64,993,677 per the issuer's own reserve API, 28 July 2026 |
| Backing | One AZG is priced at one troy ounce of gold. The reserve behind it is 21,050 oz stated across 16,167.34 tokens, composed 62.0% of in-ground mineral resource, 0% tailings and 38.0% bullion. Bullion actually behind each token is 0.4948 oz. The issuer's terms describe tokens as "associated with" the reserve, not owned by holders, and state that bullion providers "relinquish ownership of the bullion" on transfer in |
| Custody fee charged to holders | Not disclosed by the issuer. A third-party listing shows 1.00% per annum, unsupported by any Arizore document |
| Yield paid to holders | None. Arizore pays yield to miners on the other side of the structure, not to token holders |
| Redemption | No committed redemption. The Terms of Service state: "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways" |
| Token standard | Plain ERC-20 on Ethereum, 18 decimals, behind an EIP-1967 upgradeable beacon proxy. Contract `0x45334126815c77be657c7906bf52c0f441a8831c`. Source is not verified onchain. Sister token AZS at `0xee7eddf7793c1399407ba0b858852f64830f37a6` |
| Reserve verification | None published. A JSON endpoint returns six numbers with `lastUpdatedIso` set to `null`. No attestation, no auditor's report, no bar list, no serial numbers, no signature, no oracle |

#### What it is

AZG is an ERC-20 token on Ethereum issued under the "AZ Reserve" framework operated by the Arizore brand. A third-party data aggregator classifies it as tokenized gold and describes it as "a tokenised gold reserve asset designed to provide digital access to verified gold resources, including bullion, in-ground reserves and tailings". That last phrase is the accurate part.

AZG is not a claim on vaulted metal. It is a claim on a pooled reserve whose majority component is unmined mineral resource. Arizore's own live reserve API returned, on 28 July 2026: 21,050 total gold reserve ounces, composition 62.00% in-ground, 0% tailings, 38.00% bullion, across 16,167.34 tokens in circulation, at a stated token value of $4,020.06 and a stated reserve value of $64,993,677.

On its own site Arizore describes AZG not as gold but as a "Gold-linked reserve participation instrument" that "supports interaction with the gold reserve framework". That phrasing is materially more careful than the aggregator listing built on top of it.

The business model is mining finance. Arizore onboards mining projects and bullion providers. Miners pledge in-ground resources or tailings through forward contracts, valued after haircuts of 25% to 55% depending on region and resource type, and receive capital. AZG carries that pooled reserve to investors. In Arizore's own words, the purpose is "turning verified reserves into usable collateral" and letting miners "access liquidity without surrendering ownership".

#### Legal structure and regulatory standing

There is no whitepaper, no offering memorandum, no terms of issue and no token documentation of any kind for AZG. The only legal documents Arizore publishes are a website Terms of Service and a Privacy Policy, both dated 27 November 2025, and both are site-usage documents rather than instrument terms.

The Terms of Service contain the entire published legal description of the token, under a heading "Token Disclosures":

> "Arizore's ecosystem includes asset-backed digital tokens associated with verified reserves of in-ground resources, tailings, or vaulted bullion. These tokens may be characterized as security tokens under various regulatory frameworks."

and:

> "The existence of a token does not imply rights beyond those expressly documented and contractually provided."

The word used is association, not ownership, title, trust or claim. The rights are whatever a separate, unpublished contract says: tokens "reflect audited and verified reserve structures and are subject to separate agreements". A holder's actual entitlement therefore lives in bilateral agreements that are not public. Public documentation does not establish whether AZG is a title claim, a trust beneficiary interest, an unsecured creditor claim, or a purely contractual exposure.

Registry verification was attempted and could not be completed. The Nevis FSRC corporate registry at `registry.fsrc.kn` was unreachable on both HTTP and HTTPS. The Nevis FSRC states that records may be examined only by a person "who has paid the prescribed fee... during normal hours", so there is no free public search of the Nevis register. UK Companies House returns no results for either "Arizore" or "AZ Reserves". The Nevada Secretary of State entity search sits behind bot protection. ASIC, ACRA in Singapore, the Hong Kong Companies Registry and the BVI registry return no entries for any Arizore or AZ Reserves name. The issuer's jurisdiction claim rests on its own assertion and cannot be checked against a register by a member of the public.

No licence, registration or authorisation was found in any jurisdiction. ASIC holds no Australian Financial Services Licence for Arizore Ltd, AZ Reserves Ltd, Arizore LLC, Black Tie Holdings or Black Tie Digital. This matters because a third-party listing asserts that AZG sits under an Australian Financial Services Licence via ASIC. No such licence appears on the ASIC registers. The FCA, MAS, SFC, SEC, CFTC and BVI FSC hold no registrations, filings or exemption notices naming AZG, AZS, Arizore or AZ Reserves. No prospectus, offering memorandum or private-placement exemption filing was found anywhere. Equally, no regulator has issued a warning, alert or enforcement action naming any of these entities. The posture is neither authorised nor sanctioned. It sits outside the regulatory perimeter in both directions.

The issuer's own compliance position is unusual. Arizore concedes the securities characterisation rather than denying it: tokens "may be characterized as security tokens under various regulatory frameworks". It publishes no prospectus and manages the exposure by restricting distribution instead. Its press release states that AZG and AZS "are not investment products, are not yield bearing, and are not intended for retail distribution or public trading", and portal access is granted "exclusively to individuals and entities that have completed a meet-and-greet call or preliminary verification phase". AZG is not a retail product and does not compete with Aurumix in any market sense.

#### Custody and reserve verification

Arizore names no custodian anywhere. Its terms refer only to generic "vaulting and bullion partners". No vault, no city, no bar list, no serial numbers and no assay certificates are published. The terms state that bullion providers "relinquish ownership of the bullion" on transfer into the reserve, which implies a pooled reserve unallocated to holders, though this is not stated directly.

A third-party listing names "Gold Corporation" as custodian and carries the Legal Entity Identifier 213800HQZYBMURES6D84. Resolving that identifier against GLEIF gives an unambiguous match: Gold Corporation, trading name The Perth Mint Refinery, 310 Hay Street, East Perth, Western Australia, categorised as a resident government entity with the legal form "state government entity", ABN 98 838 298 431, status active. The claim is therefore that a Western Australian state-owned mint custodies the reserve behind an unlicensed Nevis token.

No corroboration for that claim exists. The Perth Mint has made no statement, announcement or annual-report disclosure naming Arizore, AZ Reserves, AZG or AZS. Arizore's own website never mentions the Perth Mint, Gold Corporation or Australia. Gold Corporation was the entity behind PMGT and exited tokenization by commercial abandonment, which makes it an improbable custodian for an unregistered Nevis instrument. There is an Australian thread that makes the claim superficially plausible: Black Tie Digital is Australian-based and Arizore's launch release is datelined Sydney. Treat the Perth Mint custody claim as unsupported unless and until the issuer produces a custody agreement.

Separating the two things issuers usually blur into one word, neither exists here. A third-party listing names KPMG as auditor. No KPMG report, engagement or reference appears on any Arizore page or in any public source. Arizore's terms use the word "audited" once, without naming an auditor, a standard or a date. The smart contract is not source-verified on Etherscan or Blockscout, so there is no contract audit either. What does exist in place of reserve verification is geological reporting: the Bocana joint venture release commits to "technical reports and studies compliant with NI 43-101". NI 43-101 is a genuine and rigorous Canadian standard, but it certifies mineral resource estimates, not vaulted bullion. It is being used as the verification backbone for a product sold as tokenized gold.

The published "proof of reserve" is a JSON endpoint returning six numbers. `lastUpdatedIso` is `null`, so the feed carries no timestamp of its own. There is no cryptographic proof, no third-party signature and no onchain oracle.

#### Fees, revenue and redemption

Arizore publishes no fee schedule of any kind. Every fee figure in circulation comes from a third-party listing that is demonstrably wrong on the issuer name, auditor, custodian and regulatory status fields. All of them should be read as unverified: a 100,000 USDT minimum investment, a 1.00% per annum management fee, and a 0.50% redemption fee with a 5,000 USDT minimum.

The economically real revenue line is not a token fee. It is the haircut. Arizore takes in-ground resource at 45% to 75% of assessed value and issues against it at spot-linked pricing. That spread, plus interest on "up to USD $60,000,000 in secured funding loans" committed to the Bocana joint venture, is the business.

The backing arithmetic is where the structure shows. Against spot gold of $4,019.80 per ounce on 28 July 2026:

| Measure | Value |
|---|---|
| AZG token value, per issuer API | $4,020.06 |
| Spot gold, same day | $4,019.80 |
| Ratio | 1.0001. One token is priced as exactly one ounce of gold |
| Stated reserve per token | 21,050 oz ÷ 16,167.34 tokens = 1.3020 oz |
| Implied value per stated ounce | $64,993,677 ÷ 21,050 = $3,087.59, or 76.8% of spot |
| Bullion component only | 38.0% × 21,050 oz = 8,000 oz, worth $32.16M |
| Actual bullion per token | 0.4948 oz = $1,989, or 49.5% of the token's own stated price |

Three points follow, and they are arithmetic rather than opinion.

The token is priced at one ounce of gold while holding roughly half an ounce of gold. The other half is a discounted claim on ore that has not been mined, held against a counterparty that is not named, under a forward contract that is not published.

The 76.8%-of-spot implied reserve value is the haircut showing through. The structure is internally consistent to the cent: tokens multiplied by token value equals the stated reserve value exactly. That tells you the reserve value is derived from the token price rather than measured independently. The published proof of reserve is a restatement of the issuer's own valuation assumptions.

The holder carries mining execution risk. If a pledged deposit is not mined, or is mined at higher cost, or the miner defaults, the in-ground 62% does not become gold. No remedy, insurance or over-collateralisation beyond the haircut is disclosed, and nothing states where a token holder ranks against the miner or against Arizore's other creditors.

On redemption, the two available sources contradict each other. A third-party listing states redemption is "instant" at a 0.50% fee with a 5,000 USDT minimum. The issuer's own Terms of Service state that "Arizore does not guarantee liquidity, market access, convertibility, or redemption pathways". The terms are the binding document. There is no committed redemption at all, in metal or in cash, and therefore no minimum increment, eligibility rule, settlement window or fee schedule attached to one. The word "redemption" appears exactly once in Arizore's published corpus, in a sentence disclaiming it.

#### Liquidity and distribution

AZG has roughly $65M to $66M of stated assets and no market. There is no decentralised exchange pool, no centralised exchange listing, no order book, no quoted bid and no price discovery. The $4,020.06 price is a number the issuer computes and serves from its own API. Nobody has traded at it.

Lifetime onchain activity is 61 transfers among 21 holders, all between 11 March and 10 July 2026, clustered in short bursts consistent with manual allocation to onboarded parties rather than trading. The largest holder controls 6,177 AZG, or 38.2% of supply. The top two hold 76.9% between them. The liquidity-to-assets ratio is zero. AZG cannot express a premium or a discount because it has no market at all. Its price sits at spot because the issuer sets it to spot.

Distribution runs through a meet-and-greet call, manual due diligence, a password-gated portal and a reported 100,000 USDT minimum. There is no savings plan, no recurring purchase, no referral programme, no affiliate network, no agent tier and no retail channel. The stated target is mining operators, bullion providers, liquidity partners and institutions. Secondary access is said to run through the BTX marketplace operated by Black Tie Holdings and Black Tie Digital, an Australian group with offices in Singapore and Hong Kong that built Arizore's infrastructure. No licence was found for any Black Tie entity, and the 61 lifetime transfers indicate the marketplace has produced essentially no secondary trading.

Two live overhangs sit against the structure. Privately held London Gold LLC moved in mid-July 2026 toward a US$25M cash-and-stock acquisition of Bocana Resources, the Canadian reporting issuer that is Arizore's joint venture partner and the continuous-disclosure window onto the in-ground backing. No public statement addresses what happens to the joint venture or to AZG's in-ground component if Bocana changes hands. Separately, the current AZG and AZS contracts were deployed on 10 July 2026, five months after Arizore's February 2026 release stated that "all tokens have been minted, issued, and confirmed on-chain". No redeployment or migration was announced, and the transfer history recorded against the current address begins on 11 March 2026, before the contract's own creation date.

One further figure is worth recording. Bocana's market capitalisation at the time of the joint venture was approximately $2.17M. Arizore Ltd, an entity with no published accounts, no named directors, no auditor and no licence, committed up to $60,000,000 in secured loans to a joint venture with a company roughly one twenty-eighth that size. Where that money comes from is not disclosed. AZG's entire stated reserve is $65M, the same order of magnitude, which suggests AZG subscriptions are the intended funding source for the mining loans. Arizore names exactly one officer anywhere: George Boot, Chief Marketing Officer. No CEO, director or beneficial owner is disclosed in any public source.

#### Relevance to Aurumix

AZG is not a competitor and should not be benchmarked as one. Its value is as a boundary case showing where "gold-backed" stops meaning gold-backed, and as proof that a headline assets figure on a data aggregator can be structurally hollow. If AZG appears on a tokenized-gold league table next to PAXG and XAUT, the answer is the arithmetic above: a $66M headline that is 38% metal, with no market, no attestation and no redemption.

**The one structural idea worth taking.** Arizore does not pay yield to AZG holders. It pays yield to the miners on the other side, through a password-gated Mining Participation Program promising "up to a maximum Annual Yield of 15.00%", distributed quarterly in USDT after a 45-day deferment, allocated by a "Contribution Index" scored on reserve contribution, commitment duration and delivery performance, with the largest weight on delivery performance measured as volume delivered against contract and timing against schedule. Under-delivery in a quarter "will result in the forfeiture of that quarter's Annual Yield allocation".

That mechanic is worth copying into the ICS Dividend. The yield is conditional on a real external performance obligation and it is forfeited automatically when the obligation is missed. It is the structural opposite of the pattern that broke Kinesis and PGOLD, where the yield was funded by recycled investor fees and promised unconditionally. A forfeiture condition tied to a verifiable external event is cheap to build, hard to argue with, and largely absent from this market. Aurumix's dividend could take exactly this shape: pay from a defined external source, and let the entitlement lapse when that source underperforms, rather than promising a percentage the fee base cannot fund.

Arizore fails to make its own version credible because it publishes nothing behind it: no disclosed revenue, no accounts, no attestation, no statement of the profit pool's size, and the whole page sits behind a password. A conditional yield is only better than an unconditional one if the condition is publicly verifiable. Take the forfeiture mechanic and publish the numerator.

**The one thing Aurumix must never do.** Blend an asset the holder can verify with one the holder cannot, and price the blend as if it were all the verifiable one. AZG charges one ounce of gold for half an ounce of gold plus a discounted claim on a mine. Aurumix's pitch is that 100% of every dollar buys physical LBMA gold, and its peg is vault grams divided by tokens. Any future temptation to admit non-vaulted assets into the reserve, whether gold leases, receivables or forward purchases, breaks that sentence and the peg formula at the same time. AZG is the fully worked example of where that ends.

Four further points transfer directly:

- **Proof of reserve must carry a timestamp, a named third-party signature, and a metal quantity stated independently of the token price.** AZG's feed has none of the three, and its reserve value is arithmetically identical to tokens multiplied by the issuer's own token price. If reserve value is derived from token price, it proves nothing.
- **Publish buyback terms where aggregators scrape them.** A third-party listing advertised "instant" redemption at 0.50% for a token whose own terms disclaim redemption entirely. Third-party listings will invent terms, and the issuer will be held to them.
- **A legal restriction the code cannot enforce is not a restriction.** Arizore concedes the token may be a security, declares it not intended for retail distribution or public trading, then deploys a plain unrestricted permissionless ERC-20 with unverified source behind an upgradeable beacon proxy. Compliance is handled entirely offchain at onboarding, and nothing stops a holder transferring to anyone. This is the concrete example of what "we will handle it at onboarding" looks like once tokens are live. It is also the case for deciding upgradeability explicitly: a single externally owned account with 8 lifetime transactions controls a beacon that can replace the token logic for every holder at once, and the contract is pausable.
- **Opacity is not free.** Arizore incorporated where verification is impossible, and the result is that a data aggregator attached a false custodian, a false auditor and a false regulator to it without contradiction. For a savings product selling to Indian and NRI retail on a trust proposition, that trade is fatal.

On wind-down, AZG publishes nothing, and its position is materially worse than the failed protocols. A majority of its reserve is in-ground resource that cannot be distributed to holders in a wind-up, because an unmined ounce cannot be delivered. Add the unresolved Bocana takeover. This strengthens the case that publishing a wind-down plan is cheap differentiation for Aurumix.

---

### 4.6 Matrixdock Gold (XAUm)

| Field | Detail |
|---|---|
| Issuer | Matrix Mining Limited, a special purpose vehicle held under a special purpose trust. Not located in any searchable company register. Domicile reported as the British Virgin Islands by a single secondary source and not confirmed against a register. Trustee: Appleby Global Services. Enforcer: Hamilton Services. The trust's jurisdiction is not stated in any issuer document. Marketed as Matrixdock, "a brand wholly-owned by Matrixport" |
| Licence covering the token | None identified. The issuer holds no financial services licence in its own name. Group affiliates hold licences that do not attach to XAUm |
| Assets under management | ~$52.7M, up 7.14% over 30 days |
| Backing | 1 token = 1 troy ounce of 99.99% purity LBMA-accredited gold, held in 1kg bars at Brink's and Malca-Amit vaults in Singapore and Hong Kong. ERC-20 holders have dynamic allocation to the gold pool, not a fixed bar. Reserves held: 16,299.036 troy oz against 12,882.21 tokens outstanding |
| Custody fee charged to holders | 0%, explicitly reversible on 30 days' notice |
| Yield paid to holders | None. No yield, no APY, no leasing, no lending, no rehypothecation |
| Redemption | Two paths, both KYC-gated. Stablecoin redemption in USDC or USDT at T+3, 0.25% fee, no minimum disclosed. Physical redemption at a minimum of 32.148 XAUm (one 1kg LBMA bar, roughly $130,000 at current prices), Singapore and Hong Kong only, requested at least T+3 in advance. The 0.25% fee is charged in token, not cash |
| Token standard | Plain ERC-20 on Ethereum (0x2103E845C5E135493Bb6c2A4f0B8651956eA8682), plus BEP-20, SPL/Token-2022 on Solana, TRC-20 on TRON, and native formats on Sui and Stellar. Nine chains total. Not permissioned at the transfer layer. A separate BullionNFT (ERC-721) gives fixed allocation to one specific bar |
| Reserve verification | Bureau Veritas, semi-annual physical count with each bar individually weighed and measured. First report January 2025, second published 31 July 2025 covering 421 x 1kg bars = 13,534.308 oz. Four report files posted. Separately, an onchain proof-of-reserve oracle on Ethereum caps a Global Mint Budget across all nine chains. No public bar list with serial numbers |

#### What it is

XAUm is a tokenized gold product from Matrixdock, the real-world asset platform of Matrixport. Each token represents one troy ounce of 99.99% LBMA-accredited gold held in 1kg bars in Brink's and Malca-Amit vaults in Singapore and Hong Kong. It launched in September 2024 and now sits at roughly $52.7M across nine chains.

XAUm out-documents much larger competitors on mechanics, with one important qualification. On fees, custody, audit, contract architecture and cross-chain reserve accounting, its disclosure is the strongest in this cohort and materially better than PGOLD or ORO. On legal identity it is no better and arguably worse. The issuing entity cannot be found in any register, and no officer is named anywhere. The disclosure runs deep on operations and thin on who is legally responsible.

Its structural distinction against Aurumix is that XAUm is an institutional bullion instrument wearing a token. It is sized in 1kg bars, priced for wholesale, settles at T+3, and trades on a bullion-market order window rather than crypto's 24/7 clock. It has no retail savings mechanic of any kind.

#### Legal structure and regulatory standing

The disclosed stack runs: token holders hold XAUm; Matrix Mining Limited is the issuer SPV; the SPV is owned by a special purpose trust; the trust holds the gold through custodians. Matrixdock states this follows its sibling product STBT's "innovative bankruptcy-remote design" and that gold ownership belongs to "the asset holder entity under Matrixdock's SPV at all times".

What the holder actually owns is not stated. Issuer materials describe holders as having "the rights to redeem the underlying physical gold" and the token as "backed by" gold. Neither formulation is a statement of legal title. No public document says whether a holder is a beneficiary under the purpose trust, the owner of specific bars, or an unsecured contractual claimant against Matrix Mining Limited. The trust deed and token terms are not public. The GitBook index lists an "XAUm Terms and Conditions" page, but the document is an embedded file that does not render as text.

The trust's purpose is worth reading carefully. A purpose trust with an enforcer, here Hamilton Services, is the classic BVI and Cayman orphan-SPV structure. Its function is to make the issuer bankruptcy-remote from the sponsor, so that Matrixport's creditors cannot reach the gold. It does not automatically confer any beneficial interest on token holders. Orphan structures are usually set up so that nobody is a beneficiary, which is precisely why an enforcer is needed. The structure that reads as investor protection is, on its face, sponsor-insolvency protection. Whether it also protects holders depends entirely on the undisclosed deed.

The XAUm issuer holds no financial services licence in its own name, and no XAUm document claims any authorisation. A company register search for "Matrix Mining Limited" produces no match tied to Matrixdock or Matrixport in any searchable jurisdiction. The BVI Financial Services Commission holds no licence for the issuer. The MAS financial institutions directory, the Hong Kong SFC public register, the Cayman Islands Monetary Authority, Dubai's VARA and the ADGM FSRA hold no listing for it either.

Licences that exist belong to other entities and do not cover XAUm. The Matrixport group holds a Hong Kong trust and money lender licence, a US money services licence, a Swiss FINMA asset management licence, and an MAS Major Payment Institution licence granted to subsidiary Fly Wing Technologies Pte Ltd in March 2025. Separately, InvestaX, which distributes XAUm, is MAS-licensed in its own right. None of these attach to Matrix Mining Limited or to XAUm as a product. A reader who sees "Matrixport is MAS-licensed" next to XAUm draws a false conclusion.

The Terms of Use carry a standard disclaimer that nothing constitutes "an offer or a solicitation of an offer to buy or sell any products or services, including but not limited to any securities", plus a prohibited-countries list. Compliance is delivered through KYC and gated mint and redeem access, not through a product licence. Every mint and redeem requires a Matrixdock account, KYC verification and a bound wallet.

#### Custody and reserve verification

Brink's is the primary custodian, with Malca-Amit as the second. Gold sits at Brink's Hong Kong, Brink's Singapore and Malca-Amit Singapore at Le Freeport. Bars are specific and individually weighed, but ERC-20 holders hold dynamic allocation to the pool rather than a named bar. Fixed allocation to one specific 1kg bar requires converting the right quantity of XAUm into a BullionNFT, which "cannot be redeemed by another".

Three separate things exist here that issuers usually blur into the single word "audited", and they should stay separate.

The first is a reserve attestation. Bureau Veritas physically counts and weighs bars on a semi-annual cadence. The method is stated: "Each bar was individually weighed and measured to verify the accuracy of its physical specifications and to confirm its consistency with recorded vault data." The second report, published 31 July 2025, covered 421 x 1kg bars totalling 13,534.308 oz. Four report files are posted.

The second is a smart contract code audit, and there are four of them: BlockSec for the EVM contracts, Zellic for Sui, and Accretion and Sec3 for Solana. These examine code only and say nothing about gold.

The third is the proof-of-reserve oracle, and it is the genuinely interesting engineering. An onchain oracle on Ethereum mainnet gates a Global Mint Budget and per-chain Local Mint Budgets. Multi-chain gold tokens usually risk minting more tokens than gold because each chain accounts separately. XAUm's Global Mint Budget makes cross-chain over-issuance a contract-level impossibility rather than a promise. Almost nobody else in this market has it.

Two caveats travel with the setup. Brink's insurance was stated at US$50M as of 29 November 2024, which is below the current ~$52.7M reserve value and a gap that widens as the product grows, though vault insurance terms are usually more nuanced than a single headline number. And no bar list is public, so the Bureau Veritas count is a trusted third-party assertion rather than something a holder can independently reconcile. The transparency page's asset-statement table currently renders "No results".

The reserve-to-supply gap is favourable and unexplained: 16,299.036 oz held against 12,882.21 tokens outstanding, roughly 26% more metal than tokens. Matrixdock does not comment on it. The most likely reading is unsold inventory pre-positioned in the vault to support minting rather than surplus backing per token, and it should not be presented as a 126% backing ratio without confirmation.

#### Fees, revenue and redemption

| Fee line | Rate | Status |
|---|---|---|
| Minting / subscription | 0.25% | Waived until total value locked reaches $100M |
| Redemption, stablecoin | 0.25% | Active |
| Redemption, physical | 0.25% | Active, charged in token |
| Ongoing management | 0% | Reversible on 30 days' notice |
| Storage / custody | 0% | Reversible on 30 days' notice |
| Physical delivery / shipping | Not disclosed | Secured delivery offered, cost not published |

XAUm markets zero storage and management fees. Its own documentation reserves the right to change that: "any change will be communicated via official channels and at least 30 days advance notice will be provided." The correct characterisation is not that XAUm has solved custody costs. It is that XAUm is currently subsidising custody and has retained the contractual right to stop.

Right now the product runs with the mint fee waived and no custody fee, so the only live revenue line is 0.25% on redemptions, and redemptions are the one activity the business does not want to encourage. The mint fee waiver began 8 November 2024 and runs until $100M in total value locked, so at ~$52.7M it is roughly halfway to expiry.

The arithmetic is worth doing. At ~$52.7M of gold, commercial allocated vault-and-insure cost runs on the order of 0.1% to 0.5% per year, so $50,000 to $260,000 annually. Monthly transfer volume is roughly $28.7M, but transfers are neither mints nor redeems and generate no fee. Redemption fee income at 0.25% would need $20M to $100M of annual redemptions to cover custody alone, which is not plausible against a $52.7M book. Matrixport funds the gap, not the product.

That is a coherent strategy. Matrixport is a large group, XAUm is a strategic reserve asset it invested $3M into directly in July 2026, and buying market share in tokenized gold with a fee waiver is rational. But it is a parent-subsidised land grab rather than a self-funding fee model, and the 30-day notice clause is the issuer saying so in writing.

Physical redemption works and has been executed. Matrixdock completed the first physical redemption on 22 April 2025 at Malca-Amit's Le Freeport vault in Singapore: one 1kg bar, redeemed by an unnamed investor who transferred 32.22837 XAUm to receive 32.148 oz of gold, the difference being the 0.25% fee. Two things follow. The redemption fee is taken in token rather than cash, so the user hands over more XAUm than the gold they receive. That in-kind deduction works here precisely because XAUm's peg is defined per token (1 token = 1 oz) rather than as a pool ratio. And at roughly $4,000 gold, the 1kg minimum is a ~$130,000 ticket, so physical redemption is real but wholesale only. A small holder's exit is the secondary market. Eligibility is defined by KYC and geography rather than by an undefined "qualified holder" category, which is cleaner than several peers.

#### Liquidity and distribution

XAUm carries ~$52.7M of market capitalisation on 12,882.21 tokens, with 52,858 holders, 643 active addresses over 30 days, and monthly transfer volume of $28,717,225 across 14,639 transfers. It trades on KuCoin spot, HTX and InvestaX, plus decentralised exchange liquidity across chains.

The transfer-volume-to-market-cap ratio of roughly 0.54x monthly is far healthier than PGOLD's sub-$20 daily volume, so XAUm is a real market rather than a parked balance. But read the holder figure against the product design: 52,858 holders, 643 monthly active addresses, and a 1kg physical redemption minimum. Those holders are overwhelmingly small, passive, secondary-market buyers who could never redeem physically. The distribution is retail. The product design is institutional.

XAUm's public mint and redeem quotes were $4,051.73 to mint and $4,020.97 to redeem, a spread of $30.76 or about 0.76%. That is the number that matters most for the premium question. XAUm runs a continuously operating two-way primary window at a sub-1% spread, which places a hard ceiling on any secondary premium. No arbitrageur will pay 3% to 8% over spot for a token they can mint at +0.38%.

Distribution runs through the Matrixdock web app under KYC, centralised exchanges, InvestaX for accredited and institutional flow, and cross-chain deployment onto Plume, HashKey, Stellar and Solana. The geography is Asia-centred with a prohibited-countries list. There is no savings plan, no recurring purchase, no referral programme, no affiliate scheme and no agent tier. The strategy is chain expansion and venue listings: being present wherever crypto capital already sits, rather than recruiting new savers. It is a liquidity strategy, not an acquisition strategy.

#### Relevance to Aurumix

XAUm is the best-run control group in this cohort: the same asset, the opposite strategy. Its answers are mostly warnings rather than templates, because it monetises the opposite end of the market.

**Custody fee.** XAUm charges no custody fee and currently no mint fee, funding vaulting from the Matrixport balance sheet while reserving the right to change with 30 days' notice. The lesson is that even the best-capitalised operator in the category would not commit to free storage permanently in writing. If Aurumix ever markets "no storage fees", copy the 30-day notice clause verbatim. It is cheap, honest, and preserves the option.

More importantly, XAUm never faces Aurumix's peg problem. Because 1 token equals 1 fixed ounce rather than a share of a pool, XAUm can deduct fees in gold, and does so on redemption, without breaking anything. Aurumix's grams-divided-by-tokens design is exactly what makes in-kind fees destructive. The fee mechanism follows from the peg design, so the peg choice comes first.

**Dividend funding, answered by absence.** XAUm pays zero yield. No APY, no leasing, no lending, no rehypothecation. The most institutionally sophisticated issuer in this set, with LBMA supply chains, Brink's vaults, real bullion-desk relationships and a large parent balance sheet, pays holders nothing. That is not an oversight. It is what unencumbered allocated gold actually returns. PGOLD promises 5% and cannot fund it. XAUm could plausibly attempt leasing and declines to. Any Aurumix yield story has to explain why it can do what Matrixport chose not to.

**Token standard.** XAUm uses plain ERC-20 across nine chains, permissioned only at the mint and redeem gate. It can afford that because the token confers no rights that survive a transfer: no yield, no governance, no tier standing. Nothing breaks when it moves to an anonymous wallet, because the wallet's only privilege, redeeming, is re-gated by KYC at the counter.

Aurumix's token carries four things that do break on an anonymous transfer: ICS standing, dividend entitlement, credit eligibility and buyback rights. The rule the comparison establishes is that permissioning is required in proportion to how much offchain entitlement the token carries. XAUm carries none, so it pays nothing for freedom. Aurumix carries four, which is the actual argument for ERC-3643, and it is a stronger argument than "compliance".

Separately, the controllerTransfer function is worth copying on its own merits. It is an admin function letting the issuer move tokens without holder consent. Matrixdock used it in production on sibling product STBT after the March 2025 Zoth hack, transferring 2,819,088.62 wSTBT out of a frozen vault to a new address on 3 July 2025. An issuer that can freeze and reissue after a hack is materially safer. The trade-off is that XAUm is transfer-free but not owner-sovereign: the issuer can move your tokens.

**Redemption.** XAUm offers real physical redemption, executed and documented, at a 1kg (~$130,000) minimum in two cities. The lesson is not that Aurumix must offer redemption. It is that physical redemption can be offered at a threshold no retail saver will ever reach, which preserves the "you own real gold" claim honestly at near-zero operational cost. The population able to present $130,000 of tokens is tiny. Aurumix should consider a high-threshold physical option purely as a credibility asset.

**Premium.** This weakens the 3% to 8% premium assumption. A competitor offering mint and redeem at a 0.76% spread caps what any tokenized gold product can sustain as a premium, because arbitrage is trivially available to anyone with a KYC account. This is a different argument from the PGOLD finding: PGOLD shows a premium cannot survive a thin market, XAUm shows it cannot survive a liquid one either. Aurumix's premium, to the extent it exists, has to come from the savings-plan wrapper and switching costs, not from gold scarcity.

**Proof of reserve.** This is the benchmark to beat, and it is achievable through procurement rather than innovation. The package is semi-annual Bureau Veritas physical counts with individual bar weighing, four published reports, a proof-of-reserve oracle capping cross-chain supply, and four separate smart contract audits. The reserve attestation and the code audits are kept clearly distinct. The one place Aurumix can beat it cheaply is a published bar list with serial numbers, which XAUm does not provide.

**Distribution.** No savings plan, no recurring purchase, no referral, no agent commissions. XAUm accumulated 52,858 holders and only 643 monthly active addresses without any acquisition machinery, and it cannot deepen those relationships. Aurumix's agent network and monthly SIP are genuinely differentiated, and this is the clearest evidence in the cohort that the differentiation is real rather than assumed.

**Wind-down.** No published wind-down plan for the token. XAUm does have two structural protections nobody else here has: a bankruptcy-remote purpose trust isolating gold from Matrixport's creditors, and a contractual custodian obligation that on custodian failure the custodian "shall promptly arrange for the return and delivery of all underlying gold in accordance with Matrixdock's instructions". That covers custodian failure and sponsor failure. It does not say what holders get if the issuer SPV fails, which is the case that matters. Aurumix committing to a published wind-down plan remains cheap differentiation.

**Regulatory route, with a caution about the wrong lesson.** XAUm operates unlicensed, compliant by KYC rather than by authorisation, from an offshore SPV, selling into Asia. Aurumix cannot copy this. The ICS dividend and the credit facility are exactly the features that make a product regulated, and they are the features XAUm does not have. XAUm's unlicensed status is purchased by product simplicity, not by clever structuring. Each bolt-on feature should be priced against the licensing burden it triggers.

One shape is worth carrying away on its own. XAUm discloses everything about the gold and almost nothing about the company. The issuer appears in no searchable register, no officer is named, and the token terms and trust deed are not public. Excellent operational transparency and unverifiable legal identity coexist comfortably here, which is a useful warning against reading "well documented" as "well accountable".

---

### 4.7 MG 999 On-Chain Gold Fund (MG999)

| Field | Detail |
|---|---|
| Issuer | Three separate Singapore entities. Fund manager and issuer of record: FundBridge Capital Pte. Ltd. Tokenisation platform: Libeara (Singapore) Pte. Ltd., UEN 202302950G. Borrower and gold provider: Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025, $0 paid-up capital. Libeara is not the issuer of MG999. Marketed as "Libeara, the tokenisation platform incubated by Standard Chartered's SC Ventures" |
| Licence covering the token | None. Libeara (Singapore) Pte. Ltd. holds a live MAS Capital Markets Services licence for dealing in capital markets products (securities and collective investment schemes). FundBridge Capital Pte. Ltd. holds a separate CMS licence for fund management and dealing in collective investment schemes, plus exempt financial adviser status. Neither licence is a product approval. MG999 has not been authorised or recognised by MAS as a retail scheme |
| Assets under management | ~$12.44M, down 7.08% over 30 days. NAV $130.00 per token on 95,983.65 tokens. Announced at a $15M fund size in December 2025 and has shrunk since |
| Backing | The fund holds no gold. MG999 is a secured private credit fund whose asset is a loan to a jewellery retailer, secured on the borrower's shop inventory. Token value is engineered to correlate to the gold spot price because the loan is denominated in gold |
| Custody fee charged to holders | No gold custody fee, because there is no gold to store. Management fee 1.00% per annum |
| Yield paid to holders | ~2.0% to 2.3% net, advertised for the thGOLD wrapper. MG999 itself publishes no target yield |
| Redemption | No physical redemption and none is possible. Cash redemption stated as daily frequency at a 0% fee. No lock-up, notice period, gate, side-pocket or suspension provision appears in any public source. Accredited, institutional and non-US investors only |
| Token standard | ERC-20 on Ethereum, with deployments to Arbitrum (zero supply) and Avalanche C-Chain. Contract addresses are not published by Libeara, FundBridge or Theo. Permissioning mechanism is not documented. Wrapped for DeFi as thGOLD by a third party, Theo, on Ethereum, Arbitrum and Stable |
| Reserve verification | None, and none is possible. No reserve, no bullion custodian, no bar list, no proof-of-reserve feed, no reserve attestation. Fund trustee and custodian: Perpetual (Asia) Limited, a corporate trustee rather than a vault. Administrator: Vistra Alternative Investments. Auditor: KPMG, as fund auditor of financial statements. No smart contract audit found |

#### What it is

MG999 is not a gold token. It is a tokenised private credit fund that lends money to a jeweller.

Every other protocol in this set is a version of a custody receipt: the buyer gives the issuer cash, the issuer buys metal, the metal sits in a vault, the token points at the metal. MG999 inverts that. Investors put up cash, the cash is lent to Mustafa Gold, a Singapore jewellery retailer, and the loan is secured on Mustafa's shop inventory. The token tracks the gold spot price because the loan is denominated in gold, not because a gram of gold exists anywhere on the fund's balance sheet.

The launch coverage is blunter than the marketing. As one report put it, "MG 999 does not possess physical bullion. Instead, the tokens are crafted to replicate gold's market performance, offering a synthetic exposure method." FundBridge's own framing is that the structure "eliminates traditional vaulting and logistics costs while maintaining price exposure."

Libeara's CEO Aaron Gwak describes the mechanism directly: "Mustafa pledges its physical gold assets for loans and gold tokens are issued based on the value of the pledged gold. Investors put up cash, which is loaned to Mustafa at a specified interest rate and tenure... During the loan tenure, Mustafa pays interest to investors... monthly pricing refreshes the pricing and the interest rate that Mustafa has to pay, i.e., a variable interest rate. At the end of the tenure, Mustafa pays back the loan in full."

This is a very old trade. Jewellers have borrowed metal rather than cash for centuries, precisely so that their inventory financing cost is not exposed to the gold price. What is new is wrapping the lender side in a token and selling it as gold exposure.

On scale, MG999 is $12.44M of assets with two holders and zero transfers in the last thirty days. It is the smallest and least-used product in this landscape. Its value is structural, not commercial.

#### Legal structure and regulatory standing

A holder owns units in a collective investment scheme whose asset is a loan receivable. Not gold, not a claim on gold, and not a direct claim on the pledged collateral. The chain of claim runs in four steps. The token holder owns a tokenised unit in the MG999 fund, a collective investment scheme under Singapore's Securities and Futures Act 2001. The fund's asset is a secured loan to Mustafa Gold Pte. Ltd. That loan is secured by a charge or pledge over Mustafa's gold inventory. And that inventory sits in Mustafa's retail business, being sold to shoppers. The holder is three legal steps away from any metal, and the metal at the end of the chain is working stock in a shop, not sealed bullion in a vault. Gwak confirms the collateral is live trading stock, with interest and pricing resetting monthly "due to stock depletion and replenishment".

What is not disclosed is substantial. Across Libeara's site, FundBridge's site, Theo's documentation and the launch coverage, none of the following is published: the exact legal form of the fund vehicle (Singapore VCC, Cayman company, sub-fund of an umbrella); whether legal title to the pledged gold passes to the fund or remains with Mustafa subject to a security interest; whether the collateral is perfected and registered, and against what; the default waterfall, meaning how unit holders rank, who enforces and in what forum; whether the pledged inventory is insured and who is loss payee; and any offering document, private placement memorandum, prospectus or factsheet in the public domain.

That last one is the headline. For a product whose selling proposition is institutional pedigree, there is no public offering document at all. What is publicly available is a press release and a data-aggregator row. Compare VNX, which publishes signed ISRS 4400 reserve reports and terms defining co-ownership down to one thousandth of a bar. A reader can find out what a VNX holder owns. For MG999, a reader cannot establish the vehicle type from public sources, let alone the enforcement mechanics.

**Two Libeara companies, and the wrong one is widely cited.** ACRA holds two distinct Libeara entities:

| Entity | UEN | Incorporated | Classification | Role |
|---|---|---|---|---|
| LIBEARA PTE. LTD. | 202300566N | 4 January 2023 | SSIC 64201, bank and financial holding companies | Holding company. Not the licensee |
| LIBEARA (SINGAPORE) PTE. LTD. | 202302950G | 2023 | Not published | The MAS CMS licensee. The operating entity named in Libeara's own terms and conditions |

Almost every secondary source, and several company-data aggregators, resolve "Libeara" to 202300566N, the holding company, which holds no licence. Anyone doing a casual check will either find a holding company with no MAS record and conclude Libeara is unlicensed, or find the licence and attribute it to the wrong entity. The licence is real. It is simply not in the company most people will look up. A name search for "Libeara" in the MAS Financial Institutions Directory also does not surface the record; it is reachable only through the direct institution-detail URL.

**What the CMS licence actually covers, versus what it is presented as covering.** This distinction matters more than the licence itself.

Libeara (Singapore) Pte. Ltd. is a Capital Markets Services licensee for dealing in capital markets products, sub-categories securities and collective investment schemes. Status active, CEO of record Gwak Yun Seok (Aaron Gwak), address 9 Raffles Place. The licence was granted in March 2026 following an in-principle approval in July 2025, and the MAS record was last updated 22 April 2026. The MAS directory displays no numeric licence identifier for this record. Dealing is a distribution and intermediation permission. It says nothing about the merits of any product Libeara tokenises.

FundBridge Capital Pte. Ltd. is separately a CMS licensee for fund management and dealing in collective investment schemes, and an exempt financial adviser. CEO Lim Sue Lynn (Lin Shuling), address 39 Duxton Hill, status active, record updated 16 July 2026. FundBridge is the entity actually responsible for MG999.

Neither licence is a product approval. MG999 has not been authorised or recognised by MAS as a retail collective investment scheme. It is a restricted scheme sold to accredited and institutional investors only, which is the exemption route that means MAS does not vet the offering document. The absence of a public offering document and the accredited-investor restriction are the same fact viewed from two sides.

No non-Singapore licence was found. Gwak has flagged Hong Kong as an expansion target, but there is no SFC registration, no UAE registration and no US registration. Libeara's marketing has at times been read as claiming multi-jurisdictional standing on the strength of prototype work for the Hong Kong government, Ghana and the Philippines. Government prototype work is not a licence. On the evidence, Singapore only.

Mustafa Gold Pte. Ltd. holds no financial licence and does not need one, because it is a borrower rather than a financial intermediary.

#### Custody and reserve verification

There is no reserve, so there is nothing to attest. The relevant question is collateral, and the disclosure there is the weakest part of the structure.

There is no bullion custodian, because the fund holds no bullion. Perpetual (Asia) Limited is the fund trustee and custodian, which is a corporate trustee rather than a vault. Vistra Alternative Investments administers the fund. KPMG is named as auditor, and the scope, along with whether any audited financial statements yet exist for a fund launched in December 2025, is not disclosed. There is no vault, no allocation, no bar list and none is possible: jewellery inventory is not serialised Good Delivery bars. There is no proof-of-reserve feed, no collateral insurance disclosure and no published loan-to-value ratio. No smart contract audit has been published by Libeara, FundBridge or Theo.

Separating "audited" from "attested" matters more here than anywhere else in this landscape. KPMG is a fund auditor examining financial statements. That is not a reserve attestation, because there is no reserve, and it is not a smart contract audit, of which none was found. Anyone reading "KPMG-audited, Standard Chartered-backed" and inferring that a Big Four firm has verified gold in a vault would be wrong on both halves. Gwak states that Mustafa's "inventory undergoes strict auditing processes to ensure it complies with Singapore's AML/CFT laws". That is an anti-money-laundering control statement, not a collateral valuation attestation.

The credit protection that is disclosed is a 20% first-loss buffer. Theo's launch article states that investors are protected by "security over gold inventory and a 20% first-loss buffer held by the fund sponsor". That is a meaningful credit enhancement and better than anything the crypto-native gold-yield products offer. Every operative detail is missing. Who the fund sponsor is (FundBridge, Mustafa or Libeara), whether the buffer is funded in cash or gold, whether it is segregated or a mere contractual undertaking, whether it is topped up as the loan book grows, and whether any document evidences it: none of that is disclosed. A 20% first-loss buffer that exists only in a marketing blog post is a promise, not a structure.

**The borrower's registry record.** The counterparty on which the entire fund's credit risk rests is Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025. It is an exempt private company limited by shares, classified in the register under SSIC 47731 but described as "other holding companies", with $0 paid-up capital, one officer, one shareholder, one employee at incorporation rising to three by May 2026, no auditor appointed and no financial statements on record. The fund launched on 11 December 2025, five months after this entity was incorporated.

The Mustafa Group itself is a real, substantial business: Mohamed Mustafa & Samsuddin Co. Pte Ltd, UEN 198900680Z, incorporated 21 February 1989, with roughly $550M of revenue and around 2 tonnes of gold turnover a year. But the borrower of record is a newly formed, zero-capital, three-employee entity. Press coverage calls Mustafa Gold "an associate of the Mustafa Group", which is a weaker word than subsidiary. No parent guarantee from the operating Mustafa entity is published anywhere. The reputational weight of the Mustafa name is doing work in the marketing that the borrower's balance sheet does not do in the registry.

#### Fees, revenue and redemption

| Fee line | Rate | Status |
|---|---|---|
| Subscription fee | 0% | Reported |
| Redemption fee | 0% | Reported, daily frequency |
| Management fee | 1.00% per annum | Reported |
| Performance fee | 0% | Reported |
| Ongoing gold custody fee | None. There is no gold to store | The product's stated selling point |
| Libeara platform fee | Not disclosed | |
| Theo wrapper fee on thGOLD | Not disclosed | |
| Fund admin, trustee and audit costs | Not disclosed | |

The revenue source is unusual and matters for Aurumix: the investor is not the source of revenue. The borrower is. Mustafa pays loan interest, and that interest funds both the yield to holders and part of the 1% management fee. Among the protocols profiled here, this is the cleanest example of a gold product funded by an external operating counterparty rather than by recycling fees back from the people it is paying.

**The arithmetic does not close.** Comparing Libeara's cost of gold financing with the Korean market, Gwak stated: "we borrow gold at 2.5% [annually]", against traditional Korean merchants who "borrow gold at 1%" per month, or 12% annualised. On the other side, Theo's Ari Pingle stated that thGOLD holders "can expect to receive an annual yield of 2.3%" net of fees, and Theo's own article says "approximately 2%".

2.5% gross minus 2.3% net leaves 0.20 percentage points. That 0.20pp is supposed to cover FundBridge's 1.00% management fee, Libeara's platform fee, Theo's wrapper fee, Perpetual (Asia) trustee fees, Vistra administration, KPMG audit, and the funding cost of the 20% first-loss buffer.

It cannot. The 1% management fee alone consumes 1.00pp of a 2.50pp gross spread, which caps the maximum net yield at 1.5% before any other cost, and lower once platform, wrapper, trustee, administration and audit fees are paid. A 2.3% net yield is arithmetically impossible from a 2.5% gross loan rate.

Four reconciliations are possible, none of them confirmed. The 2.5% figure may have described a market rate or a different transaction rather than MG999's actual coupon to Mustafa. The actual coupon may be materially higher, plausibly 4% to 6%, to leave room for the stack. Theo's 2.3% may be subsidised or promotional, or may blend in the delta-neutral gold-futures basis strategy Theo separately describes, in which case it is not purely lending yield and the "secured gold lending" story is incomplete. Or the 1% management fee may be waived during the ramp. The published figures are mutually inconsistent, and the actual loan coupon is not disclosed.

One further figure sits in Theo's launch material: "the strategy produced an average annual return of about 8.27% during 2025". That is a gold-price-inclusive total return, not a lending yield, and it appears in the same material as the 2.3% yield figure.

On redemption, there is no physical redemption and there never can be, because the fund owns no gold. That is a structural impossibility rather than an omission in the terms. Cash redemption is stated as daily frequency with a 0% redemption fee, and that figure deserves scepticism. Daily liquidity against an illiquid asset is a classic maturity mismatch. The fund's only asset is a term loan to a jeweller, secured on shop inventory, and loans of that kind cannot be liquidated on a day's notice. A fund offering daily redemption on such a book is either holding a large cash buffer that drags the yield, relying on the sponsor to warehouse redemptions, or reserving gating powers that are not disclosed. Which of these applies is not disclosed. No lock-up, notice period, gate, side-pocket or suspension provision appears in any public source, and no offering document exists to consult. With two holders and zero transfers in thirty days, none of this has been tested.

Subscription is daily in cash with a USD base currency at a 0% fee, restricted to accredited investors, institutional investors and non-US persons. No minimum subscription is published. Capacity is capped: Theo describes thGOLD as "launching with capped early access while the fund scales to full capacity", which is a polite way of saying the loan book cannot yet absorb much money.

#### Liquidity and distribution

MG999 has no market at all. Assets of $12.44M, supply of 95,983.65 tokens, NAV of $130.00, two holders, one active address in 30 days and zero transfers in a month. There is no secondary market, no exchange listing, no onchain liquidity pool and therefore no price against spot to measure. NAV is struck by the administrator, not discovered by a market. The 30-day move of minus 7.08% tracks the gold price rather than any flow. thGOLD is the layer intended to create tradability, and it is not currently tradeable on any exchange listed by the major aggregators. Neither layer trades.

Distribution is entirely business-to-business institutional. There is no savings plan, no recurring purchase, no referral scheme, no affiliate programme and no agent network. Libeara's CMS dealing licence is itself the distribution strategy: the March 2026 licence was framed as letting Libeara move "from a technology platform provider to a regulated financial institution", enabling it to distribute tokenised products directly rather than only build rails for others. Theo provides the DeFi distribution layer across Hyperliquid, Uniswap, Morpho and Pendle. The geography is Singapore-centred with stated ambitions in Hong Kong and Korea. Retail is structurally excluded, which is the mirror image of Aurumix.

The interesting distribution insight is on the borrower side, not the investor side. Libeara's growth constraint is not raising money. It is finding creditworthy gold retailers to lend to. Gwak's comparison of a 2.5% offered rate against Korean jewellers paying 12% annualised is a pitch to borrowers, and it explains the Korean investor base in the June 2026 funding round. This is a two-sided marketplace disguised as a fund.

The wrapper structure is worth recording. MG999 the fund unit is locked to accredited investors. thGOLD, issued by Theo, a separate firm founded by former Optiver and IMC traders, takes MG999 exposure onto Hyperliquid, Uniswap, Morpho and Pendle. Theo's disclaimer still restricts access to accredited and institutional investors, so this is not a retail bypass on paper. But the legal relationship between the two layers is nowhere documented. Whether a thGOLD holder is a beneficial owner of MG999 units, a creditor of Theo, or a derivative counterparty is not disclosed. Theo goes further with thUSD, a gold-backed stablecoin backed by thGOLD, announced 17 April 2026 with a $100M genesis programme and a $1bn deposit target. That is three layers of wrapper on a $12.4M loan to a jeweller: MG999 unit, thGOLD, thUSD. Each layer adds a counterparty and a fee, and only the bottom one sits inside a MAS-licensed perimeter.

On the Standard Chartered connection: it is substantive on the licensing and platform side and reputational on the product side. Standard Chartered is nowhere in the MG999 stack. It is not the issuer, not the manager, not the custodian, not the trustee, not the auditor and not the borrower's guarantor. It is a shareholder in a portfolio company that provides tokenisation software. On the separate ULTRA treasury product, Standard Chartered does provide actual custody, which is a bank doing bank work. But every phrase like "Standard Chartered-backed gold fund" describes a venture equity relationship two removes from the product. SC Ventures did not participate in Libeara's June 2026 $14M round, no shareholding percentage has ever been disclosed, and after a $14M external round the stake has necessarily been diluted. The round was led by GSR, which SC Ventures had itself invested in a month earlier, so it is weaker external validation than it appears.

#### Relevance to Aurumix

**The inversion that matters most.** The bank-affiliated platform produced a better licence than the crypto-natives. It did not produce better paperwork.

Libeara holds a real, current, correctly scoped MAS licence, verified on the register with a named CEO in the MAS record. Of the protocols profiled here, this is one of the very few where a name search against a regulator produces that result. And yet MG999 publishes no offering document, no contract address, no smart contract audit, no loan coupon, no loan-to-value ratio, no default waterfall, no insurance detail, and no evidence for its headline 20% first-loss buffer beyond a sentence in a partner's blog post. VNX Commodities AG, a small Liechtenstein operator holding 13 kg of gold, publishes more legally operative detail about what a holder owns than a Standard Chartered-incubated platform does.

The reason is structural rather than cultural, and it is the transferable lesson. The accredited-investor exemption is what removes the disclosure obligation. By selling only to accredited and institutional investors, MG999 avoids prospectus registration and with it the requirement to publish anything. The licence and the opacity are not in tension. The licence is what buys the opacity. An institutional wrapper is a disclosure reduction technology, not a disclosure enhancement technology, and any Aurumix positioning that assumes "regulated therefore transparent" has the causation backwards.

**The arithmetic discipline.** MG999's published 2.5% gross against 2.3% net does not survive a 1% management fee. This is the third protocol, after Kinesis and PGOLD, where the advertised yield cannot be reconciled with disclosed revenue, and it is the strongest evidence in this report that advertised gold yields do not survive arithmetic. The pattern is not a crypto-native failing: a MAS-licensed, KPMG-audited, bank-incubated structure does it too. The failure to reconcile advertised yield with disclosed revenue is not correlated with regulatory status. Aurumix must publish its gross source rate, its full fee stack and its net-to-holder number in the same table, or it will be indistinguishable from these.

**What to take on the dividend question.** MG999 is the first structure in this landscape where the yield is paid by an external commercial counterparty rather than recycled from investor fees. Mustafa Gold pays interest because it gets working capital cheaper than a bank would lend it. That is real economic value creation, not circular flow, and it is the category of thing Aurumix needs for its ICS Dividend.

- **Copy the credit-enhancement pattern, and do it properly.** A first-loss tranche funded by the operator and sitting ahead of holders converts "trust us" into a quantified subordination. It is cheap to describe and powerful in a disclosure document. Fund it, segregate it, size it against the book, and publish the evidence. Libeara's version exists only as a sentence.
- **Note where the scarce resource actually is.** Libeara's binding constraint is creditworthy borrowers, not investors. Aurumix's India and UAE markets are full of jewellers who currently borrow at Muthoot-style rates. That is a more accessible yield source for a Dubai and India operator than institutional gold leasing, and it is on Aurumix's doorstep.
- **Do not treat MG999 as the documented precedent.** Its collateral is retail jewellery inventory on a shop floor, which is worse collateral than vaulted bullion. It depletes, it is fungible, it is hard to perfect a security interest over, and the borrower is selling it to customers in the ordinary course of business. How MG999 unit holders rank on a Mustafa default is not disclosed anywhere. Streamex is the better template.

**The regulatory lesson is inverted.** MAS licensed Libeara's dealing activity and FundBridge's fund management. It did not approve the product. MG999 avoids product-level scrutiny by being a restricted scheme for accredited investors. That escape hatch is unavailable to Aurumix, which is mass retail at $20 a month by design. The institutional route's cost is that you cannot sell to retail, and Aurumix's entire thesis is retail. Aurumix can borrow MG999's licensing discipline, not its regulatory posture.

**On the custody fee question**, MG999 offers a genuine third option beyond the cash-versus-grams framing: do not hold the metal at all. It charges no gold custody fee because it holds no gold, and it is explicit that removing vaulting, insurance and storage cost is the product's reason for existing. It replaces the storage cost with credit risk on a jeweller, which is a real trade honestly stated. It is not available to Aurumix, whose promise is that 100% of every dollar buys physical LBMA gold and whose token price is vault grams divided by tokens. Aurumix has a vault, so it has a storage cost, so it must recover that cost in cash. MG999 confirms the cash-recovery conclusion by showing that the only way to avoid the cost entirely is to abandon physical backing.

**On the wrapper architecture**, MG999 is a live demonstration of the pattern Aurumix is leaning toward: a restricted regulated unit at the base, and a freely composable wrapper on top issued by a different firm. The warning is that the legal relationship between the two layers must be documented, and here it is not. Nobody can say from public sources whether a thGOLD holder owns fund units, has a claim on Theo, or holds a derivative. Aurumix will face the identical question about ICS standing, dividend entitlement and buyback rights on a wrapped token, and must answer it in writing at design time.

**On redemption**, MG999 is the one protocol in this set with less physical redemption than Aurumix, and it is sold to institutions on that basis without apology. A Standard Chartered-incubated, MAS-licensed gold product with zero metal and zero physical redemption is being sold to accredited investors today. Aurumix's no-physical-redemption stance is not an outlier, and Aurumix actually holds the metal, which makes its position strictly stronger. It should say so. Separately, MG999's claimed daily redemption against a term loan book is a maturity mismatch Aurumix should not copy. Aurumix's cash buyback design should state its settlement window and its funding source honestly.

**On proof of reserve**, MG999 is the strongest example in this landscape of institutional-sounding assurance language attaching to nothing in the vault. It can truthfully say it is KPMG-audited (fund financials) and Standard Chartered-backed (venture equity), and a reader will hear that a Big Four firm and a global bank have verified the gold. There is no gold. This is Aurumix's clearest opportunity: a genuine, frequent, published reserve attestation with a bar list is a differentiator even against bank-affiliated competitors. It also adds a third category to the "audited" confusion. Reserve attestation, smart contract audit and fund audit are three different things, and MG999 has only the third.

**On wind-down**, no plan is published. Given the structure, the questions are sharper than for a vaulted product. On a FundBridge failure, who administers the loan book. On a Libeara failure, who can mint, burn and transfer the tokens, and does the register survive. On a Mustafa default, who enforces the charge and in what order do unit holders rank. None of this is documented, including by the bank-affiliated protocol with a live CMS licence. The case for Aurumix publishing a wind-down plan as cheap differentiation holds.

---

### 4.8 Streamex (GLDY)

| Field | Detail |
|---|---|
| Issuer | Streamex Ltd., a Cayman Islands exempted company formed February 2026, consolidated as a variable interest entity. Listed parent: Streamex Corp., Delaware, CIK 0001530766, Nasdaq: STEX, formerly BioSig Technologies, Inc., renamed 12 September 2025. Operating company: Streamex Exchange Corporation, incorporated in British Columbia 5 April 2024, acquired 28 May 2025. Servicer: GLDY ServiceCo, LLC, Delaware |
| Licence covering the token | None. GLDY is sold under Rule 506(c) of Regulation D, which is a US private-placement exemption, not an authorisation. No VARA, ADGM, MAS, FCA or CIMA licence identified. The parent's Nasdaq listing regulates the parent's shares, not the token |
| Assets under management | ~$12.84M (July 2026). The Q1 2026 10-Q records $15.225M of gold at cost on the SPV's balance sheet at 31 March 2026 |
| Backing | 1 GLDY is intended to correspond to 1 fine troy ounce of gold held by the SPV. Gold may be held on an unallocated basis. Each token represents "a non-voting digital share of Streamex Ltd.", an equity interest in a Cayman company, not title to gold and not a trust beneficial interest. The gold is placed into Monetary Metals' commercial leasing programme, where it may be commingled with other participants' gold |
| Custody fee charged to holders | Not disclosed as a separate holder charge. Expenses are borne inside the SPV and reduce net yield |
| Yield paid to holders | "Up to 4%" advertised, 3.50% APY displayed July 2026. Paid monthly as scrip dividends automatically reinvested as new GLDY tokens, not in cash |
| Redemption | On 90 days' prior written notice, with proceeds payable in physical gold, stablecoins, select digital assets or US dollars, subject to undisclosed "certain limitations". The 10-K states physical redemption "may only be available under certain conditions" because gold may be unallocated with no bar-level linkage. Redemption fee not disclosed |
| Token standard | ERC-20 on Base as primary chain, with Chainlink CCIP to Solana. Whitelisted and KYC-gated to accredited investors. The issuer does not publish the contract address. Chainlink appointed official oracle provider 28 October 2025. Upgradeability and admin key custody not disclosed. No smart contract audit found |
| Reserve verification | EisnerAmper LLP examination under AICPA attestation standards as of 31 March 2026, announced 1 July 2026, with monthly attestations intended thereafter. Result: 3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces, a surplus of 0.2416423 oz. The examination covers gold in reserve and gold on lease. Custodian described only as "an LBMA-accredited custodian" and not named in any SEC filing. No bar list published. A Chainlink proof-of-reserve feed is referenced but the issuer states it has not yet fully implemented a live dashboard |

#### What it is

GLDY is a gold-backed security token that pays a yield sourced from real third-party gold leasing, issued by a Cayman SPV whose ultimate parent is Nasdaq-listed. Each token is intended to correspond to one fine troy ounce of physical gold held by the SPV, and yield accrues because the SPV's gold goes into Monetary Metals' commercial gold-leasing programme rather than sitting idle in a vault.

This is the most relevant protocol in the landscape to Aurumix's dividend problem, for one reason. It is the only one where the yield-generating arrangement is described in a document filed with a securities regulator rather than asserted in marketing. ORO advertises 3% to 4% from the same counterparty, Monetary Metals, with nothing published at all. Streamex has put paper on the record.

The qualification, developed below, is that the filed paper covers the commercial relationship between Streamex and Monetary Metals. It does not cover the lease itself, and it says nothing about what a token holder gets if a lessee runs off with the gold.

The corporate history is worth knowing. This is a former medical device company, BioSig Technologies, whose PURE EP cardiac signal platform still shows on EDGAR under SIC code 3845, "Electromedical Apparatus". It acquired a Vancouver blockchain startup in May 2025 and repurposed the listing. The legacy medical business is still on the books.

#### Legal structure and regulatory standing

A GLDY holder owns "a non-voting digital share of Streamex Ltd., a Cayman Islands special purpose vehicle". That is an equity interest in a Cayman company. It is not title to gold, and it is not a trust beneficial interest.

The entity chain, verified against the SEC filings themselves:

| Layer | Entity | Domicile | Source |
|---|---|---|---|
| Listed parent | Streamex Corp., formerly BioSig Technologies, Inc. | Delaware, originally Nevada February 2009, reincorporated Delaware April 2011 | 10-K FY2025, CIK 0001530766 |
| Intermediate | ExchangeCo | British Columbia ULC | 10-K FY2025 |
| Operating company | Streamex Exchange Corporation | British Columbia, incorporated 5 April 2024 | 10-K FY2025 |
| Token issuer | Streamex Ltd. | Cayman Islands exempted company | 10-Q Q1 2026, Note 9 |
| Servicer | GLDY ServiceCo, LLC | Delaware | 10-Q Q1 2026 |
| Lease counterparty | Monetary Metals & Co. | Delaware corporation | Exhibit 10.1 preamble |
| Actual lessee vehicle | "a designated series of a Delaware series limited liability company managed by Monetary Metals" | Delaware | 10-K FY2025 risk factors |

The marketing name "Streamex" spans a Delaware listed parent, a Canadian operating company and a Cayman token issuer. Anyone describing GLDY as a US-issued token is wrong: the issuer is Cayman. Anyone describing Streamex as Canadian is describing the operating subsidiary, not the issuer.

**The filed agreement, and what it does and does not contain.** The document is real. Form 8-K filed 8 September 2025 by BioSig Technologies, Inc., accession 0001641172-25-026853, Item 1.01, Entry into a Material Definitive Agreement. Exhibit 10.1 is the complete executed text, roughly 55,000 characters over 20 pages, signed by Henry McPhie and Keith Weiner. It is re-listed as Exhibit 10.22 to the FY2025 10-K, confirming it remains in force.

Its title is the "Tokenized Yield Partnership Agreement" between "BioSig Technologies, Inc. d/b/a StreamEx" and "Monetary Metals & Co." Governing law is Delaware, with disputes going to AAA arbitration seated in Chicago before a single arbitrator, jury trial waived.

What it governs is the commercial relationship: exclusivity, volume commitments, fee rebates and revenue share. The operative supply clauses defer the lease terms:

> "Section 3.02 StreamEx's Supply of Gold. StreamEx shall supply physical gold to the MM SPV. The manner in which StreamEx shall supply the MM SPV will be documented in the Lease Documentation."

> "Section 3.03 Lease Documentation. All Products in which StreamEx will participate will be documented in written agreements, order forms, and other documentation that will be developed and mutually agreed by the Parties (the 'Lease Documentation'). In the event that the Parties cannot agree on the form of the Lease Documentation within three (3) months of the Effective Date, either party may terminate this Agreement with immediate effect."

The lease agreement is not in the filing. What is filed is an agreement to enter into lease documentation later. A separate "Precious Metals Lease Program Agreement" is referenced in passing at Section 3.01(b) and is likewise not filed. Section 14.13 confirms the leases sit under a different legal regime: "StreamEx hereby acknowledges that the Lease Documentation and all other document relating directly to MM's Lease origination and account agreements are governed by, and constructed in accordance with, the substantive laws of the State of New York."

A full text search of the filed exhibit establishes what it does not contain:

- **No security interest.** The words "security interest", "lien", "collateral" and "pledge" appear nowhere in an operative sense.
- **No title retention clause.** There is no "title to the gold remains with the lessor" language anywhere. The only uses of "title" concern intellectual property.
- **No risk-of-loss allocation.** The phrase does not appear.
- **No subordination or loss waterfall.** Nothing addresses ranking of claims.
- **No default provisions relating to lessees.** "Default" appears once, in a boilerplate representation about not breaching other contracts.
- **No fiduciary duty.** Section 14.19 affirmatively disclaims one: "Nothing in this Agreement shall be construed as creating any agency, joint venture, partnership, or other form of joint enterprise, employment, or fiduciary relationship between the Parties."

The liability cap is severe. Section 13.02 caps StreamEx's aggregate liability at the total paid by Monetary Metals to StreamEx in the six months preceding the claim "OR $500,000, WHICHEVER IS LESS". Section 13.01 excludes consequential and indirect damages both ways, and Section 12.04 makes indemnification the sole and exclusive remedy. Monetary Metals also refuses securities responsibility for the token at Section 3.04: "StreamEx hereby acknowledges that MM accepts no responsibility for securities laws and regulations with respect to such Tokenized Yield Products in any jurisdiction where StreamEx offers such Products."

**Where a token holder ranks on lessee default: nowhere in the filed document**, because the filed document is not between the holder and anyone. The structure interposes at least four layers between a GLDY holder and the gold. The holder owns a non-voting share in Streamex Ltd., the Cayman SPV. The SPV leases gold to a designated series of a Delaware series LLC managed by Monetary Metals. That series may commingle the gold with other participants' gold. The series then leases it on to the ultimate lessee, typically a jeweller, mint or refiner.

The 10-K states the consequences plainly in its own risk factors, which is to the company's credit:

> "The SPV's gold leasing activities are conducted through a 'back-to-back' structure pursuant to agreements with Monetary Metals, whereby the SPV leases gold to a designated series of a Delaware series limited liability company managed by Monetary Metals, which then may commingle the SPV's gold with gold from other participants and lease it to the ultimate lessee."

> "The SPV's gold may be commingled with gold from other lessors in Monetary Metals' leasing program, and other lessors may receive more favorable terms or priority in enforcement scenarios."

> "Tokenholders do not benefit from FDIC or SIPC protections, and may face delays, partial recovery, or total loss in the event of SPV insolvency or service provider failure."

> "tokenholders are subject to the credit and operational risk of gold lessees under the SPV's gold leasing program. If a lessee fails to return leased gold or make required payments, whether due to financial distress, operational failure, fraud, or other events, tokenholders may experience reduced recoveries upon redemption. ... While leases may include independent insurance coverage, collateral, guarantees, or inspections, these measures vary by lease and may be insufficient to prevent losses."

A GLDY holder is an equity holder in a Cayman company that has a contractual claim against a Delaware series LLC that has a claim against a lessee. It is the most remote position in this landscape, and it is subordinate not only to the SPV's own creditors but potentially to other lessors in the same commingled pool.

On regulatory standing, GLDY holds no licence from any regulator anywhere. It is sold under Rule 506(c) of Regulation D to verified accredited investors and institutions, including non-US persons. No CIMA registration was found for Streamex Ltd. No Form D was located on EDGAR under CIK 0001530766 for the GLDY offering. SEC-reporting is not the same as SEC-approved, and it is not the same as the token being regulated. Streamex Corp. files 10-Ks because its equity is listed on Nasdaq. The rich disclosure quality relied on throughout this profile is a by-product of the parent's listing obligations, not of any regulation of the token.

The company anticipates the classification issue candidly: "the tokenization of gold-linked instruments is expected to be treated as the issuance of securities in most jurisdictions." It treats GLDY as a security from the outset, which is the opposite of the ORO and Comtech posture.

One flag on internal controls. The 10-K and the 13 July 2026 8-K both report unremediated material weaknesses in internal control over financial reporting: inadequate identification and recording of stock-based compensation, ineffective period-end review, and inadequate segregation of duties. For a business whose pitch is custody and verification integrity, that is a real weakness.

#### Custody and reserve verification

The custodian is described only as "an LBMA-accredited custodian" and is not named in any SEC filing. No vault or city is disclosed. Gold may explicitly be held on an unallocated basis. No bar list is published.

The 10-K is unusually blunt about the custody weakness:

> "With respect to GLDY, gold may be held on an unallocated basis, and there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars. As a result of these operational hurdles, physical redemption for underlying assets may only be available under certain conditions, We have not yet fully implemented a live proof-of-reserves dashboard or public confirmation of 1:1 gold backing for tokens, and we are in the process of implementing an independent audit process for bullion holdings on a defined timeline."

Separating the two things: the reserve attestation exists and is real, and the smart contract audit does not. EisnerAmper LLP performed an examination under AICPA attestation standards of management's assertion about gold held for the benefit of GLDY token holders. As of 31 March 2026: 3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces, a surplus of 0.2416423 oz. The examination is stated to cover gold in reserve and gold on lease, which is the correct scope for a leasing structure. No published audit of the Base ERC-20 contract or the CCIP integration was found. This is one of the few protocols in the set where the attestation exists and the contract audit does not, the reverse of the usual pattern.

Two qualifications belong with the attestation. An attestation over roughly 3,065 ounces where the issuer's own parent held 98.5% of the tokens at the same date is an attestation of the issuer's own inventory more than a protection for third-party holders. And EisnerAmper was engaged as the parent's statutory auditor on 8 July 2026, one week after issuing the GLDY reserve attestation announced 1 July 2026. The same firm now audits the parent and attests the token reserves.

#### Fees, revenue and redemption

| Fee line | Amount | Who pays |
|---|---|---|
| Subscription fee | Not disclosed | |
| Ongoing custody or management fee | Not disclosed as a separate holder charge. Expenses borne within the SPV, reducing net yield | Holder, indirectly |
| Redemption fee | Not disclosed | |
| Monetary Metals purchase fee | Tiered 0.75% down to 0.20% by quarterly volume, rebated quarterly in cash | Streamex pays Monetary Metals |
| Monetary Metals revenue share | 0.35% to 0.50%, sliding by total kilograms leased | Monetary Metals pays Streamex |
| Token issuance and platform fees | Stated intent. The 10-K says "Streamex has not yet generated material revenue from its fee models" | |

Exhibit 10.1 Section 6.01 sets out the purchase-fee ladder verbatim: 0 to $250K at 0.75%, $250K to $1M at 0.55%, $1M to $5M at 0.40%, $5M to $25M at 0.30%, $25M to $50M at 0.25%, and above $50M at 0.20%, with a quarterly cash rebate reconciling fees actually paid against the aggregate-volume tier.

**The yield arithmetic works here, and that is the point.** GLDY advertises "up to 4%" and currently displays 3.50% APY. Unlike PGOLD, Kinesis and MG999, this promise is arithmetically fundable, because it is not recycled from investor fees. The Tokenized Yield Partnership Agreement defines a "Passing Lease" in Article I as one that "generates a net yield of at least three percent (3%) per annum after origination fees". Streamex is contractually obliged only to accept leases clearing that 3% net hurdle, and it can reject any individual lease "in its absolute and sole discretion" under Section 3.01(b). The yield comes from an external commercial counterparty paying to borrow gold, against a contractual floor, not from other holders' subscriptions.

The 3% floor is a screening criterion rather than a guarantee to holders, and the yield reaching a holder is net of SPV expenses and Streamex's spread. Yield is also paid in scrip, not cash: monthly "scrip dividends automatically reinvested as new GLDY tokens". The 10-K flags the consequence: "The SPV does not pay cash distributions; yield is paid as additional Tokens (scrip dividends), which limits liquidity for investors who may not be able to easily convert their investment to cash."

**The insurance schedule is the other genuinely copyable piece.** Schedule 1 of the filed exhibit sets out two layers.

The primary layer requires the lessee to maintain a jeweller's block policy at its own expense, covering "no less than one hundred ten percent (110%) of the U.S. dollar value of the Total Lease Amount", adjusted as gold prices or ounces rise, from an insurer rated A.M. Best A- or better.

The supplemental layer requires Monetary Metals itself to obtain, at its own expense, a Difference in Conditions and Difference in Limits policy through a Lloyd's of London broker. That policy "shall provide coverage in the event that the primary lessee insurance fails or refuses to pay a claim, or is otherwise insufficient to cover a loss", and it "must also provide coverage for both mysterious disappearance and 'bad acts' by the lessee's management and owners, including but not limited to fraud, misappropriation, or other willful misconduct", also at 110%.

That second layer is good design. It insures against the lessee's own fraud and against the primary insurer refusing to pay, which is precisely the failure mode a gold-leasing structure faces.

On redemption, tokens are redeemable on 90 days' prior written notice, with proceeds payable in physical gold, stablecoins, select digital assets or US dollars. Three qualifications come from the issuer's own filings. It is subject to undisclosed "certain limitations". The 10-K states physical redemption "may only be available under certain conditions" because gold may be unallocated with no bar-level linkage. And the 90-day notice is a structural necessity rather than a courtesy: the gold is on lease to third parties and cannot be returned on demand. The notice period is the liquidity mismatch made explicit, and it is the honest design consequence of encumbering gold to generate yield.

#### Liquidity and distribution

GLDY holds approximately $12.84M of assets against 19 holders as of July 2026, of which roughly 98.5% of tokens were held by the issuer's own parent at 31 March 2026. The Q1 2026 10-Q states it directly: "As of March 31, 2026, the Company held approximately 98.5% of outstanding GLDY Tokens. Two related party officers of the Company subscribed for an aggregate of approximately $225 [thousand] of GLDY Tokens during March 2026."

Third-party ownership at the end of Q1 2026 was therefore roughly 1.5%, and a material portion of even that belonged to two of the company's own officers. GLDY should be read as a corporate treasury position that has been tokenized, with a nascent third-party investor base, rather than a distributed product. The "over $100 million in initial institutional interest" cited in Q1 earnings commentary is interest, not subscriptions.

Streamex announced roughly $12M of liquidity infrastructure across three venues and a 24/7 secondary automated market maker with Orca on Solana in a 27 May 2026 8-K. No public daily volume figure exists, and as a whitelisted Regulation D security GLDY cannot trade on open venues to non-accredited buyers anyway. There is no observable market price against spot. The parent's own equity traded around $1.25 in early July 2026 against a $3.00 January 2026 offering price, and the board authorised a 10,000,000 share buyback at up to $2.00 on 7 July 2026.

Distribution is institutional and accredited only, and this is the sharpest contrast with Aurumix in the entire profile. There is no savings plan, no SIP, no recurring purchase mechanism, and no referral, affiliate or agent-commission network. The minimum ticket is $200,000 for an individual, $300,000 joint and $1,000,000 institutional. Channels are direct through app.streamex.com, a distribution partnership with Siebert covering wealth-management and institutional channels, and the Nasdaq-listed parent as the credibility vehicle. Geography is US accredited investors plus non-US persons.

The filed agreement itself excludes much of Aurumix's target market on the lessee side. Exhibit 10.1 defines "Restricted Nation" as "any country located in Africa", any sanctioned territory, plus Afghanistan, Bangladesh, Belarus, El Salvador, Haiti, Honduras, Iraq, Lebanon, Myanmar (Burma), Nicaragua, Pakistan, Russia, Turkey, Ukraine, Venezuela and Yemen. This restricts where Monetary Metals will place gold, not where investors may live. India and the UAE are not excluded. Pakistan, Bangladesh and the whole of Africa are.

One litigation item is on the record. In November 2025 a former advisor filed a Notice of Civil Claim in the Supreme Court of British Columbia against the Company, Streamex Exchange Corporation and certain officers and directors, alleging breach of contract, unjust enrichment and civil conspiracy over equity interests predating the acquisition. The company disputes the claim and has recorded no liability.

#### Relevance to Aurumix

Streamex is the single most useful protocol in this report for Aurumix's dividend question, and the answer splits cleanly into a template to copy and a gap to fill.

**What is proven: real, externally funded gold yield is documentable, and the document is public.** Exhibit 10.1 to accession 0001641172-25-026853 is a genuine, executed, publicly filed agreement with a 3% per annum net-after-origination-fees yield floor defining a qualifying lease, a two-layer insurance standard, and real economics in the 0.20% to 0.75% purchase-fee ladder and the 0.35% to 0.50% revenue share. Aurumix now has a precedent it can point to and copy for structuring a leasing relationship. That is more than ORO ever published, and more than MG999 publishes.

Two clauses are worth copying almost verbatim:

- **The "Passing Lease" definition**: a lease qualifies only if it generates a net yield of at least 3% per annum after origination fees.
- **The absolute discretion to reject any individual lease** (Section 3.01(b)).

Together those two let an issuer advertise a yield range honestly without guaranteeing it. The floor is a screening criterion applied to the counterparty, not a promise made to the holder.

The insurance schedule is the third thing to copy: a lessee-funded jeweller's block policy at 110% of lease value from an A.M. Best A- or better insurer, plus an issuer-funded Difference in Conditions and Difference in Limits layer through a Lloyd's broker covering mysterious disappearance and bad acts by the lessee's own management, also at 110%.

**What is not proven, and this is the gap Aurumix must fill.** The filed agreement contains no security interest, no title-retention clause, no risk-of-loss allocation, no subordination, no loss waterfall and no default ranking. The lease documents that would contain those terms are expressly deferred to a later, unfiled, New York law "Lease Documentation" set. So the yield-generation precedent exists. The holder-protection precedent does not. Streamex has documented the revenue side and left the risk side to private paper.

The insurance beneficiary answer is the sharpest illustration. Both layers say: "MM shall require the insured to name MM as a loss payee and additional insured wherever possible." Three problems follow. The loss payee is Monetary Metals, not Streamex, not Streamex Ltd., and not the token holder. "Wherever possible" is a best-efforts phrase rather than a covenant, which means there will be leases where Monetary Metals is not named. And nothing anywhere obliges anyone to name StreamEx, the SPV or holders as loss payee, additional insured or third-party beneficiary. Insurance proceeds land at Monetary Metals and then have to travel back down a chain of contracts, through a commingled pool in which "other lessors may receive more favorable terms or priority in enforcement scenarios", before any of it reaches a holder. Recovery is a litigation and contract-chain problem, not an entitlement.

**The risk is realised, not theoretical.** The AgaBullion lessee default of 26 January 2026 is the live test of this design. When a gold lessee fails, "title remains with the lessor" means litigating abroad, and whether the Lloyd's Difference in Conditions layer actually paid out has not been published by Monetary Metals. Aurumix should not design a dividend on the assumption that a documented insurance stack converts lessee credit risk into a recoverable claim. Streamex's paper is better documented than the AgaBullion situation, and it still does not change the holder's fundamental position.

**The audience gap is the decisive point.** Streamex sells this risk to verified accredited investors at a $200,000 minimum ticket. Those buyers can price counterparty risk, read a 10-K risk factor section, and absorb a total loss. Aurumix would sell the same category of risk to a saver putting in $20 a month.

That asymmetry cuts across every other consideration. To earn 3% to 4%, the gold must leave the issuer's control, be commingled with strangers' gold, become unreturnable for 90 days, and expose holders to a jeweller's credit. Streamex's own 10-K tells its investors they "may face delays, partial recovery, or total loss". For a mass-retail SIP product sold to first-time savers in India and the UAE, that trade is materially worse than it is for a professional at a $200,000 minimum. Aurumix's ICS Dividend is promised to retail. If Aurumix adopts leasing, the disclosure burden and the wind-down obligations scale with the audience, not with the size of the book.

**The differentiating move is available and unoccupied.** If Aurumix builds a leasing-funded dividend, the differentiator is not the lease. It is being the first issuer to name the token holders, or a trustee acting for them, as loss payee, and to publish the default waterfall. Every protocol profiled here, including this one, leaves that gap open. It is cheap to close.

Four further points transfer directly:

- **Custody fee.** No disclosed holder-facing custody fee. Costs are absorbed inside the SPV and paid out of lease income before yield reaches holders. That is the third option executed cleanly: the external yield pays for the custody, and it is peg-neutral because it never touches grams. It is the most attractive single idea in this profile for Aurumix.
- **Token standard.** Streamex treats the instrument as a security from day one and went permissioned and whitelisted, ERC-20 on Base with KYC gating and CCIP for cross-chain reach. It bought compliance and it cost the product any real secondary market: 19 holders. Aurumix's ERC-3643 lean is directionally right. The lesson is that permissioning and liquidity are a genuine trade, not a free win.
- **Redemption.** Once gold is leased, instant redemption becomes structurally impossible. GLDY's 90-day notice is the honest form of that constraint. Aurumix's no-physical-redemption stance is at least internally consistent with a yield-bearing design. The presentational risk is identical for both: advertising "you own physical gold" while operating a notice-period claim on a commingled leased pool.
- **Proof of reserve: right scope, wrong sequence.** The EisnerAmper examination explicitly covers gold in reserve and gold on lease, which is exactly the scope Aurumix must specify if it ever leases. But Streamex launched the token in February 2026 and produced its first attestation in July 2026, having disclosed in the interim that it had no live proof-of-reserve dashboard and no bar-level linkage, and the attestation covers ounces that are 98.5% owned by the issuer. Attest before you sell, not after, and do not let an attestation over your own inventory be mistaken for holder protection.

**The regulatory route is unavailable to Aurumix.** No licence anywhere, a US private-placement exemption into a Cayman SPV, with credibility borrowed from the parent's Nasdaq listing. That route is accredited-investor-only by construction, the exact opposite of a $20-a-month retail SIP. Nothing here provides an alternative to VARA, and nothing here touches the ADGM Accepted Spot Commodity route. What it does show is that a listed parent produces high-quality public disclosure as a by-product of its listing obligations, which is a reputational asset Aurumix cannot replicate cheaply.

**On wind-down, no plan is published**, and the disclosed failure mode is severe: holders "may face delays, partial recovery, or total loss in the event of SPV insolvency or service provider failure", with other lessors in the commingled pool potentially receiving "more favorable terms or priority in enforcement scenarios". The failure mode is disclosed but unplanned. Even the best-documented protocol in this set, with a Nasdaq-listed parent and a Big Four-adjacent attestor, has not said what happens to the gold if it fails.

---

## SOURCES: AZ Gold Reserve (AZG)

- https://arizore-reserve-backend.vercel.app/api/azg-reserve
- https://arizore.io/reserve-room/written/live-reserve
- https://www.nevisfsrc.com/faqs/
- https://find-and-update.company-information.service.gov.uk/
- https://api.gleif.org/api/v1/lei-records/213800HQZYBMURES6D84
- https://api.gold-api.com/price/XAU
- https://blacktie.digital/enabling-real-world-asset-collateralisation-blacktie-x-arizore/
- https://www.globenewswire.com/news-release/2025/10/14/3166721/0/en/Bocana-Resources-Corp-Announces-Joint-Venture-with-Arizore-Ltd-to-Form-Arizore-LLC.html
- https://www.globenewswire.com/news-release/2025/11/05/3181268/0/en/bocana-resources-corp-provides-corporate-update.html
- https://iiroc.mediaroom.com/2026-06-30-Canadian-Investment-Regulatory-Organization-Trading-Halt-BOCA
- https://app.rwa.xyz/assets/AZG

## SOURCES: Matrixdock Gold (XAUm)

- https://matrixdock.gitbook.io/matrixdock-docs/english/gold-token-xaum/physical-gold-custody.md
- https://matrixdock.gitbook.io/matrixdock-docs/english/legal/terms-of-use.md
- https://matrixdock.gitbook.io/matrixdock-docs/english/announcements/other-announcements/notice-wstbt-transfer-on-request-from-zoth
- https://matrixdock.substack.com/p/matrixdock-publishes-its-second-independent
- https://www.matrixdock.com/blog/announcements/matrixdock-completes-first-ever-physical-redemption-of-tokenized-gold
- https://www.globenewswire.com/news-release/2025/03/05/3037067/0/en/Matrixport-Subsidiary-Fly-Wing-Receives-Major-Payment-Institution-License-from-MAS-in-Singapore.html
- https://www.globenewswire.com/news-release/2025/07/10/3113587/0/en/Matrixport-Establishes-Strategy-XAUm-Reserve-Remains-Bullish-on-the-Future-of-Tokenized-Real-World-Assets.html
- https://www.globenewswire.com/news-release/2025/09/10/3147655/0/en/Matrixport-and-HKUST-Institute-for-Financial-Research-Release-Joint-In-Depth-Report-on-Gold-Tokenisation.html
- https://etherscan.io/token/0x2103E845C5E135493Bb6c2A4f0B8651956eA8682
- https://app.rwa.xyz/assets/XAUm

## SOURCES: MG 999 On-Chain Gold Fund (MG999)

- https://eservices.mas.gov.sg/fid/institution/detail/431842-LIBEARA-SINGAPORE-PTE-LTD
- https://eservices.mas.gov.sg/fid/institution/detail/218507-FUNDBRIDGE-CAPITAL-PTE-LTD
- https://libeara.com/terms-and-conditions/
- https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/
- https://scventures.io/libeara-raises-14m-in-gsr-led-strategic-round-to-scale-infrastructure-for-regulated-digital-assets
- https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you
- https://www.prnewswire.com/news-releases/theo-brings-yield-bearing-gold-onchain-via-regulated-tokenized-fund-structure-302671228.html
- https://www.prnewswire.com/news-releases/theos-gold-backed-stablecoin-held-steady-through-global-disruption-now-targets-1b-in-deposits-302745928.html
- https://recordowl.com/company/mustafa-gold-pte-ltd
- https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/
- https://people.duke.edu/~charvey/Media/2026/E_January_29_2026.pdf
- https://app.rwa.xyz/assets/MG999

## SOURCES: Streamex (GLDY)

- https://www.sec.gov/Archives/edgar/data/1530766/000164117225026853/ex10-1.htm
- https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001530766&type=8-K&dateb=&owner=include&count=40
- https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001530766&type=10-K&dateb=&owner=include&count=40
- https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001530766&type=10-Q&dateb=&owner=include&count=40
- https://www.globenewswire.com/news-release/2025/11/10/3184594/22558/en/Streamex-Corp-NASDAQ-STEX-Announces-Launch-of-100-000-000-USD-GLDY-Pre-Sale-A-Gold-Backed-Yield-Generating-Stablecoin-Offering-Institutional-Yield-on-Physical-Gold-Bullion.html
- https://www.globenewswire.com/news-release/2026/07/01/3320524/22558/en/streamex-corp-announces-first-independent-reserve-attestation-by-eisneramper-for-gldy.html
- https://app.streamex.com
- https://app.rwa.xyz/assets/GLDY
