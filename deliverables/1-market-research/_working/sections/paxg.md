# Pax Gold (PAXG)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | PAXG | **High** |
| Issuer (marketing) | Paxos, "Paxos Trust Company" | **High** |
| Issuer (registry) | **Paxos Trust Company, National Association**: a US federally chartered uninsured national trust bank. Converted from a NYDFS limited-purpose trust company on 12 December 2025 ([OCC NR 2025-125](https://www.occ.gov/news-issuances/news-issuances/news-releases/2025/nr-occ-2025-125.html), [Paxos newsroom](https://www.paxos.com/newsroom/occ-approves-paxos-application-to-convert-to-occ-trust-paxos-to-complete-conversion-imminently-to-become-a-federally-regulated-blockchain-infrastructure-provider)) | **High** |
| Domicile | United States (national charter; Paxos HQ New York) | **High** |
| Backing claim | 1 PAXG = 1 fine troy ounce of an LBMA London Good Delivery bar, allocated, serial-numbered | **High** |
| Chains | Ethereum (primary); Solana added ~25 June 2026 | Ethereum **High**, Solana **Medium** |
| Contract address(es) | Ethereum: `0x45804880de22913dafe09f4980848ece6ecbaf78`. Solana mint: **Not disclosed** in any Paxos primary source found | Ethereum **High** |
| Supply | ~444,808 PAXG ≈ 444,808 fine troy oz ([CoinGecko, 28 Jul 2026](https://www.coingecko.com/en/coins/pax-gold)) | **Medium** |
| Market cap / TVL | ~$1.79bn at ~$4,027/token | **Medium** |
| Regulatory status | OCC-supervised national trust bank; PAXG issued "pursuant to specific approval from the OCC" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). No OCC licence *number* published | **High** |
| Subscription fee | Tiered 1.000% down to 0.125% by order size; **currently waived** on creations under a promotion ([Paxos fee page](https://support.paxos.com/articles/2899561282-pax-gold-fees)) | **High** |
| Ongoing custody fee | **Zero at present.** "Paxos does not charge gold storage fees to its customers at this time" | **High** |
| Redemption fee | Same tiered 1.000%–0.125% destruction schedule; physical bar delivery fee stated only in the User Guide | Tiers **High**, bar fee **Low** |
| Advertised yield | **None. PAXG pays no yield of any kind.** | **High** |
| Named officers | **Not disclosed** on PAXG product or terms pages (Charles Cascarilla is publicly Paxos CEO, but no officer is named as responsible for PAXG) | **Medium** |

---

## 1. What it is

PAXG is a gold-denominated token issued by Paxos Trust Company, N.A. Each token represents one fine troy ounce of a specific, serial-numbered London Good Delivery bar held in LBMA-approved vaults in London ([paxos.com/pax-gold](https://www.paxos.com/pax-gold)). It launched in September 2019 and is the largest tokenized-gold product by market capitalisation other than Tether Gold.

The product is deliberately narrow. It is a **custody receipt with an on-chain wrapper**, nothing more. There is no savings plan, no yield, no tiering, no credit facility, no referral network. Everything Aurumix layers on top of a gold core, PAXG has consciously omitted. That is the point of comparison: PAXG is what the regulated-minimum version of this product looks like, and it has reached ~$1.79bn doing only that.

## 2. Legal structure

This is the strongest disclosure of any protocol in this landscape, and the language is unusually precise.

The PAXG Terms and Conditions state that "**Your PAXG tokens are akin to a warehouse receipt representing your beneficial ownership of a pro rata portion of Allocated Gold**" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). **Confidence: High.**

Three things follow, and they matter:

- **Beneficial ownership, not legal title.** The holder does not hold legal title to a bar. Paxos holds the bars; the holder has a beneficial interest in a pro rata share of the allocated pool. Paxos expressly reserves the right to **reallocate** which specific bars back which holders "for operational efficiency". So the serial number you look up is real but not permanently yours.
- **Allocated, not unallocated.** The terms define Allocated Gold as "a specific gold bar held in an LBMA-approved security carrier vault, identifiable by a unique serial number, weighting and purity percentage," and separately define Unallocated Gold as "a liability of such institution whereby the holder of unallocated gold owns a claim to an equivalent balance of gold." PAXG is backed by the former. This is the distinction most gold tokens blur, and Paxos does not blur it.
- **Bankruptcy remoteness is claimed but asymmetrically documented.** The Paxos blog asserts "We're required to hold all customer funds in segregated, bankruptcy remote accounts" and "your gold bars will always be yours, even in the unlikely case something happens to Paxos" ([Paxos blog](https://www.paxos.com/blog/pax-gold-the-safest-way-to-own-gold-today)). **Confidence: Medium**, because that is a marketing page. **The terms themselves contain no Paxos-insolvency clause.** They do contain a detailed clause disclaiming liability for a *Clearing Bank* insolvency ("Paxos is not responsible for any losses associated with any default by a Clearing Bank... including but not limited to, insolvency, default, or operational error") but nothing comparable governing the failure of Paxos Trust Company itself. **The marketing makes a bankruptcy-remoteness promise the legal document does not restate.** That gap is worth noting precisely because Paxos is otherwise the best-documented issuer here.

Counterweight: the OCC national trust charter is itself the substantive protection. A national trust bank holds fiduciary assets off its own balance sheet by operation of banking law, which is a stronger structural claim than any contract clause. Paxos is relying on the charter rather than on drafting.

## 3. Regulatory and compliance posture

**This is the finding that contradicts the working brief.** The task framing (and most secondary sources still in circulation) describes PAXG as sitting under a **NYDFS trust charter**. That has not been true since December 2025.

- **11 August 2025:** Paxos filed to convert its NYDFS limited-purpose trust charter to a national trust charter ([Paxos newsroom](https://www.paxos.com/newsroom/paxos-to-pursue-national-trust-charter-with-the-office-of-the-comptroller-of-the-currency)). **Confidence: High.**
- **12 December 2025:** the OCC conditionally approved five national trust bank charters, including the conversion of Paxos Trust Company into an uninsured national trust bank. The other four were Ripple National Trust Bank and First National Digital Currency Bank (de novo), plus BitGo Bank & Trust, N.A. and Fidelity Digital Assets, N.A. (conversions) ([OCC NR 2025-125](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-125.html)). **Confidence: High.**
- Paxos completed the conversion the same day, and states "all of Paxos Trust Company's US-based activity will be subject to OCC supervision." The entity is now styled **Paxos Trust Company, N.A.** **Confidence: High.**
- The PAXG terms now say "Paxos Trust issues PAXG pursuant to specific approval from the OCC." **Confidence: High.**

**Regulator: OCC. Licence: national trust bank charter (uninsured), granted 12 December 2025.** No public charter number was found on the OCC release or on Paxos pages. **Not disclosed.**

Residual inconsistency to flag: the PAXG transparency page still describes NYDFS as the body approving the choice of auditor ([paxg-transparency](https://www.paxos.com/paxg-transparency)). Paxos has not uniformly updated its own site post-conversion, so **any source dated before December 2025, and some of Paxos's own pages, will state the wrong regulator.**

What was checked and not found: no VARA, ADGM, DFSA, MAS or EU/MiCA authorisation for PAXG was located. The recency sweep returned "not found" on all of these. **Not disclosed.** PAXG appears to be a purely US-chartered product distributed globally through exchanges.

## 4. Custody and proof of reserve

| Item | Finding | Confidence |
|---|---|---|
| Custodian (legal) | Paxos Trust Company, N.A. | **High** |
| Vault operator | **Brink's**, London. Paxos's own blog: "We store gold reserves with Brink's bullion vaults in London" ([Paxos blog](https://www.paxos.com/blog/pax-gold-the-safest-way-to-own-gold-today)). Note the PAXG product page says only "LBMA vaults in London" | **High** (blog is a Paxos primary page) |
| Vault city | London | **High** |
| Allocated? | Yes: specific serial-numbered LBMA Good Delivery bars, with a contractual right for Paxos to reallocate | **High** |
| Bar list | **Partial.** There is a per-address **allocation lookup**: enter your Ethereum address and see the serial number, value and physical characteristics of your bars. There is **no full public bar list** of all bars backing total supply | Lookup **High**; absence of full list **Medium** |
| PoR feed | **Not disclosed.** No Chainlink or other on-chain proof-of-reserve oracle for PAXG was found | **Medium** |
| Reserve attestation | **Monthly**, by **KPMG LLP** since February 2025, previously WithumSmith+Brown, under AICPA attestation standards. Published at [paxos.com/paxg-transparency](https://www.paxos.com/paxg-transparency), reports listed through June 2026 | **High** |
| Annual physical bar audit | Claimed by one secondary source (Bureau Veritas). **Could not be confirmed against Paxos or Bureau Veritas primary sources: treat as unverified** | **Low** |
| Smart contract audit | Ethereum contract audited pre-launch; the Solana deployment was audited by **Zellic**. No PAXG-specific audit PDF was located on paxos.com | **Medium** |

**The attestation/audit distinction, stated plainly:** PAXG has a genuine *reserve attestation* (monthly, Big Four, AICPA standards, published as a time series) **and** separately a *smart contract audit*. These are two different things and Paxos is one of the few issuers that does both and does not conflate them in its own copy. For Aurumix, KPMG monthly is the benchmark a retail buyer will have seen; anything less frequent or less credentialed will read as a downgrade.

The honest gap: **a per-address lookup is not a bar list.** A holder can verify their own slice but cannot independently sum the pool. Total-supply verification still depends on trusting KPMG's monthly snapshot. Between snapshots there is no continuous on-chain proof.

## 5. Issuance

Tokens are created only when gold is purchased and vaulted, on a 1:1 basis with fine troy ounces. Issuance runs through a verified Paxos account: "Only verified Customers may purchase PAXG from us or convert or redeem PAXG from us" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). Full KYC at the mint and redeem boundary; free circulation in between.

Minimum purchase is **0.03 PAXG** (roughly $120 at July 2026 prices), driven by a 0.02 PAXG internal conversion cost. The token is divisible to 18 decimals, and there is no minimum holding. So the *minting* minimum is meaningfully above Aurumix's $20 SIP floor, but the *holding* minimum is effectively zero: small buyers are expected to acquire PAXG on the secondary market rather than mint it.

## 6. Redemption

PAXG offers three exits, and this is the most complete redemption stack in the landscape:

1. **To USD**, at market, at any time, via a Paxos account.
2. **To Unallocated Gold** by wire to a bullion account. Marketing frames this as institutional.
3. **To physical Allocated Gold bars.** Minimum **430 PAXG plus the fee set out in the Paxos User Guide, per London Good Delivery bar**. Conversions to USD round down to the nearest 1/100th of a troy ounce.

At ~$4,027/oz, a 430 PAXG bar redemption is roughly **$1.73m**. Physical delivery is therefore real but structurally out of reach for retail: it is a credibility mechanism for the peg, not a retail feature. Paxos also pushes delivery risk onto the holder: "You are responsible for delivery and once your bars are in the possession of the delivery service you choose, then Paxos will have been deemed to have fulfilled its obligation for delivery."

Eligibility is defined by KYC verification, not by an undefined "qualified holder" test. That is cleaner than several peers.

**A serious asymmetry to carry forward:** the terms give Paxos sweeping discretionary power over both token and metal. In capitals: "WE MAY FREEZE, TEMPORARILY OR PERMANENTLY, YOUR USE OF, AND ACCESS TO, PAXG OR THE LONDON GOOD DELIVERY GOLD BARS BACKING YOUR PAXG, WITH OR WITHOUT ADVANCE NOTICE." And on illegality: PAXG "AND THE ASSETS BACKING SUCH PAX MAY BE FORFEITED," and may "BECOME WHOLLY AND PERMANENTLY UNRECOVERABLE AND UNUSABLE." So the beneficial-ownership claim in §2 is real but conditional on Paxos's compliance discretion.

## 7. Fees and revenue model

| Fee line | Amount | Notes | Confidence |
|---|---|---|---|
| Creation (mint) | Tiered by order size: 0.02 PAXG flat for 0.03–2 PAXG; 1.000% (2–25); 0.750% (25–50); 0.500% (50–75); 0.250% (75–200); 0.150% (200–800); 0.125% (800+) | **Currently waived** on creations under a promotion running to a date the page renders as "09/31/26" (a typo; September has 30 days) | **High** |
| Destruction (redeem) | Same tiered schedule, not waived | Applies only through the Paxos wallet, **not** on exchange order-book trades | **High** |
| Storage / custody | **$0.00.** "Paxos does not charge gold storage fees to its customers at this time" | See below: the terms reserve the right to start | **High** |
| On-chain transfer fee | Contract supports a fee, historically 0.02%. Currently understood to be **set to zero**; users pay gas only | **Medium**: fee parameter state not independently read on-chain | **Medium** |
| Inactivity fee | **US$2.00/month** after 12 months with a non-zero balance and no issuance or redemption activity | **High** |
| Banking fees | Passed through at cost | **High** |
| Physical bar delivery fee | Stated only in the User Guide; secondary sources cite $20 domestic / $30 international, unconfirmed | **Low** |

**This is the single most decision-relevant part of the profile for Aurumix, and it answers design question 1 directly.**

PAXG's answer to the custody-fee problem is **option three from the brief: charge holders nothing recurring and recover cost elsewhere.** The ongoing storage fee is zero. Revenue comes from *transaction* events (destruction fees on redemption, creation fees when the promo lapses, the $2 inactivity fee) plus, critically, Paxos's ability to cross-subsidise from a much larger stablecoin and infrastructure business. PAXG does not have to pay for itself.

**But the terms document the fallback mechanism, and it is exactly the mechanism Aurumix has ruled out.** If Paxos ever does charge storage, it will do so like this: "Paxos may charge storage fees to all token holders by **issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens**. The storage fee will be in line with industry practice, and such storage fee will be passed on to all PAXG token holders on a pro rata basis" ([PAXG T&Cs](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions)). **Confidence: High.**

Read that against Aurumix's peg. PAXG's peg is *one token = one ounce*, so minting new tokens against an unchanged gold pool **breaks the 1:1 claim**: after a dilution event, one PAXG is backed by slightly less than one ounce. Paxos has reserved the right to break its own headline promise, disclosed it in the terms, and then never used it.

Aurumix's peg is *price = grams ÷ tokens*, which is the arithmetic inverse: Aurumix can mint dilutively without breaking its peg formula (the price simply falls), whereas deducting **grams** breaks it. So **the Paxos mechanism is actually peg-compatible for Aurumix and peg-breaking for Paxos.** Minting new AURX to the treasury reduces price-per-token exactly like a fee, keeps the grams-to-tokens identity intact, requires no cash collection from a SIP saver, and is enforceable against holders who never interact with the platform. It is the cleanest available answer to design question 1, and there is a Big Four-attested, OCC-supervised precedent for the drafting.

## 8. Token architecture

- **Standard: plain ERC-20** on Ethereum at `0x45804880de22913dafe09f4980848ece6ecbaf78`, 18 decimals. **Not** ERC-3643 or any permissioned standard. **Confidence: High.**
- **Permissioned?** No, at the transfer layer. Anyone can hold and transfer PAXG; permissioning applies only at mint and redeem, where KYC is mandatory. This is the "KYC at the boundary, free in the middle" model.
- **Upgradeability:** proxy pattern with a separate implementation contract. **Confidence: Medium.**
- **Admin keys:** the contract defines an owner/admin, a **supply controller** (mint/burn), a **fee controller** (sets transfer fee rate and recipient), and an **asset protection role** able to **freeze accounts and wipe balances**. The freeze-and-wipe capability is what makes the §6 forfeiture language enforceable on-chain. **Confidence: Medium** on the exact role names, **High** that freeze/seize capability exists (the terms assert it in capitals).
- **Solana:** added around 25 June 2026 using **Token-2022**, which carries native compliance extensions, with Zellic as auditor, Sunrise DeFi as DeFi integration partner and LayerZero Stargate for bridging. **Confidence: Medium.** The mint address is **Not disclosed** in any Paxos primary source found; a "Portal"-wrapped PAXG also exists on Solana and should not be confused with the Paxos issuance.

**What this choice buys and costs, for design question 3.** PAXG chose maximum composability: an anonymous ERC-20 lists on any exchange, enters any DEX pool, and collateralises any lending market without integration work. That is precisely how it got to $105m of daily volume. The cost is that PAXG can carry no holder-level state whatsoever, and Paxos accepted that cost because PAXG has no holder-level state to carry: no tier, no dividend, no credit standing.

Aurumix cannot make the same trade, because ICS standing, dividend entitlement, credit eligibility and buyback rights are all holder-level state that an anonymous transfer destroys. **The relevant lesson is not "copy the ERC-20", it is that Paxos's freedom to use a plain ERC-20 is a direct consequence of its product minimalism.** Note also that Paxos, having chosen an open standard, then bolted freeze-and-wipe admin powers onto it: it wanted permissioned control without a permissioned standard. The Solana move to Token-2022 (compliance extensions built in) suggests that where a compliance-native standard is available, Paxos now takes it. That is mild support for Aurumix's ERC-3643 lean.

## 9. Liquidity and market

As at 28 July 2026 ([CoinGecko](https://www.coingecko.com/en/coins/pax-gold)). **Confidence: Medium** (market aggregator, not issuer):

- Price ~**$4,027** per token
- Market cap ~**$1.79bn**
- 24h volume ~**$105.6m**
- Circulating supply ~**444,808** tokens ≈ 444,808 fine troy oz (~13.8 tonnes)
- All-time high $5,619.09 (January 2026); ATH is a gold-price artefact, not a premium event

**Volume/AUM ratio ≈ 5.9% per day.** Set that against the brief's PGOLD benchmark: ~$79–90m AUM on sub-$20 daily volume, a ratio near zero. PAXG turns over more value in a day than PGOLD holds in total.

**This is the direct evidence on design question 6, and it argues against the premium thesis.** PAXG is the most liquid tokenized gold product with a genuine physical redemption channel, and it trades **at or extremely near NAV**, not at a 3–8% premium. That is not an accident: deep liquidity plus a credible (if high-minimum) arbitrage path is exactly what *destroys* a premium. Any 430-PAXG-plus holder can arbitrage a persistent premium away by minting.

The uncomfortable conclusion for Aurumix: **a sustained 3–8% premium and a liquid market are not merely separate problems, they are in tension.** A premium survives only where arbitrage is blocked, which in practice means thin liquidity or closed redemption. Aurumix has no physical redemption at all, so it *can* in principle sustain a premium; but the mechanism sustaining it would be the absence of an arbitrage path, and that is a fragile and hard-to-defend basis for a retail value story. PAXG is the counter-example that shows what "liquid and credible" actually prices at: par.

## 10. Distribution

- **Channels:** direct via paxos.com / Paxos wallet (KYC'd), plus very broad third-party exchange listings (Binance, Kraken, Coinbase, Gemini, Backpack, BitMart and others), and now Solana DeFi via Sunrise DeFi.
- **Target segment:** self-directed crypto-native investors and institutions seeking gold exposure. Marketing leans on cost comparison against ETFs and physical dealers.
- **Geography:** global via exchanges; direct minting constrained by Paxos's US-chartered KYC perimeter. No India, UAE or NRI-specific channel found.
- **Savings plan / recurring purchase:** **Not disclosed.** No systematic investment plan, no recurring buy, no premium schedule.
- **Referral / affiliate / agent network:** **Not disclosed.** No commission-based distribution of any kind was found.
- **Anti-feature worth naming:** PAXG runs a **$2/month inactivity fee** on dormant balances. It actively penalises the buy-and-hold, low-engagement saver, which is exactly Aurumix's target customer.

Design question 8, answered: **PAXG has no savings-plan, recurring-purchase, referral or affiliate mechanism at all, and charges dormant holders a fee.** The brief predicted most protocols would not; PAXG not only does not, it leans the other way. Aurumix's agent-network SIP is genuinely unoccupied ground among the credible issuers. The flip side is that Paxos reached $1.79bn without any distribution machinery, by being the compliance-credible default that exchanges list. Those are two different businesses: Paxos let distribution come to it, Aurumix must go and buy it.

## 11. Recent developments

Reverse chronological. Recency sweep run 28 July 2026 covering ~18 months. The sweep returned a large volume of routine itBit exchange maintenance notices, which are excluded as non-material.

- **~13 July 2026:** Paxos Labs' Amplify Transit reported to have moved ~$30m between Ethereum and Robinhood Chain within two weeks of launch. Stablecoin infrastructure; **no PAXG involvement identified**. **Confidence: Low.**
- **1 July 2026:** Amplify Transit goes live alongside Robinhood Chain mainnet: a "universal adapter" converting USDC, USDG and PYUSD via one API. **Not a gold product.** **Confidence: Low.**
- **~25 June 2026:** **PAXG launches on Solana** using the Token-2022 standard, with Sunrise DeFi as ecosystem partner, LayerZero Stargate for bridging from Ethereum, and Zellic as smart contract auditor ([Crypto Times](https://www.cryptotimes.io/2026/06/25/gold-goes-onchain-paxos-launches-paxg-on-solana/)). **Confidence: Medium.** This is the most material PAXG-specific event in the window.
- **12 December 2025:** **OCC conditionally approves Paxos Trust Company's conversion to a national trust bank; Paxos completes the conversion the same day.** Entity becomes Paxos Trust Company, N.A. NYDFS limited-purpose trust charter surrendered ([OCC](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-125.html), [Paxos](https://www.paxos.com/newsroom/occ-approves-paxos-application-to-convert-to-occ-trust-paxos-to-complete-conversion-imminently-to-become-a-federally-regulated-blockchain-infrastructure-provider)). **Confidence: High.** The single most important development for this profile.
- **11 August 2025:** Paxos files its OCC national trust charter conversion application ([Paxos](https://www.paxos.com/newsroom/paxos-to-pursue-national-trust-charter-with-the-office-of-the-comptroller-of-the-currency)). **Confidence: High.**
- **February 2025:** **KPMG LLP replaces WithumSmith+Brown** as attestor for the monthly PAXG reserve reports ([paxos.com/paxg-transparency](https://www.paxos.com/paxg-transparency)). **Confidence: High.**
- **Date not established:** Paxos Securities Settlement Company registered with the SEC as a clearing agency. Adjacent to PAXG, not part of it. **Confidence: Low.**
- **Date not established:** Paxos Labs closed a $12m strategic round led by Blockchain Capital. **Confidence: Low.**

**Explicitly not found** across the sweep, and each absence is itself a finding: no PAXG depeg, no security incident or exploit, no PAXG-related lawsuit or enforcement action, no change to PAXG custody arrangements, no EU/MiCA, MAS, VARA or ADGM authorisation, and no gold-token competitor launched by Paxos.

## 12. Relevance to Aurumix

**Contradiction to flag loudly, per the brief's instruction.** The task premise (and the bulk of secondary coverage still circulating) treats PAXG as a **NYDFS**-chartered product. It is not, and has not been since **12 December 2025**. PAXG is now issued by **Paxos Trust Company, N.A.** under an **OCC national trust bank charter**. Anything in the Aurumix data room asserting NYDFS supervision of PAXG must be corrected. Paxos's own transparency page still refers to NYDFS approving its auditor, so this error will propagate. Second, note the brief's list of tokenized-gold comparables treats PAXG as Ethereum-only: it has been live on **Solana since June 2026**.

Taking the nine design questions in order of how much PAXG actually moves the needle:

**1. Custody fee: PAXG gives Aurumix its answer, and it is not the one the client expected.** PAXG charges **zero** ongoing custody fee and funds the vault from transaction fees plus cross-subsidy from a far larger stablecoin business. Aurumix has no such adjacent business, so straight imitation is not available. But the *fallback* Paxos drafted is the transferable asset: charge storage **by minting new tokens to the issuer and diluting holders pro rata**. For Paxos this would break a 1:1 ounce peg, which is why it has never been used. For Aurumix, whose price is grams ÷ tokens, dilution is peg-*neutral* by construction: mint to treasury, price per token falls by the fee, the grams-to-tokens identity survives untouched. It needs no cash collection from a $20/month saver, it reaches holders who never log in, and there is now an OCC-supervised, KPMG-attested issuer with the clause on the page. **Recommend adopting the mechanism and copying the disclosure discipline: state the rate, state that it is charged by issuance, and commit to advance notice.**

**2. Dividend funding: PAXG pays nothing, and that is the evidence.** The largest, best-regulated, most liquid gold token in the market at $1.79bn AUM offers **zero yield** and grew anyway. Its gold is unencumbered, sitting allocated at Brink's, doing nothing. This is a powerful negative datapoint for the ICS Dividend: **gold-token AUM does not require a yield to accumulate**, and the issuer with the most regulatory latitude to construct one has declined to. Paxos, an OCC-supervised trust bank, will not lend or lease customer gold to manufacture a return, which speaks to how a serious prudential regulator views encumbering allocated client metal. If Aurumix needs the ICS Dividend, PAXG offers no funding template: it demonstrates the opposite, that the compliant path is to promise no yield at all.

**6. Premium and liquidity: PAXG is the counter-evidence to the 3–8% premium thesis.** $1.79bn AUM against $105.6m daily volume (≈5.9% turnover), a genuine mint/redeem arbitrage channel, and it trades **at par**. The brief already has PGOLD as the illiquid extreme; PAXG is the liquid extreme, and neither sustains a premium. Deep liquidity plus open arbitrage equals NAV. Aurumix's closed redemption is the only thing that could hold a premium, which means the premium is a product of the exit restriction, not of demand. That should be said out loud to the client before it is built into revenue.

**7. Proof of reserve: PAXG sets the retail benchmark.** Monthly **KPMG** attestation under AICPA standards, published as a dated time series, plus a per-address bar lookup showing serial number and physical characteristics, plus a separately-audited smart contract. Aurumix should assume a sophisticated retail buyer or agent has seen this. Match the cadence (monthly) and the credential tier, and keep attestation and contract audit visually and verbally separate. **Do note PAXG's own gap: there is no full public bar list and no on-chain PoR oracle.** Publishing a complete bar list or a live PoR feed would put Aurumix *ahead* of the category leader on one dimension at modest cost.

**5. Redemption: physical redemption can be real and still be retail-irrelevant.** PAXG's 430 PAXG minimum is ~$1.73m per bar. It functions as an arbitrage backstop and a marketing proof point, not a consumer feature. **Aurumix should stop treating "no physical redemption" as a pure weakness.** The honest framing is that PAXG's physical redemption is also unavailable to a $75/month saver; the difference is that Paxos can say "redeemable for physical gold" in a headline. If Aurumix wants that headline without the operational burden, a high-minimum, fee-bearing physical option (deliberately priced out of retail reach) is the industry-standard construction. If it stays with cash-only buyback, it must not claim "you own physical gold" without qualification: Paxos earns that claim with allocated serial numbers and a real, if remote, delivery path.

**3. Token standard: PAXG's plain ERC-20 is a consequence of having no holder state.** Paxos got composability, exchange listings and the resulting liquidity by making the token anonymous and stateless, then retrofitted freeze-and-wipe admin powers to regain compliance control. Aurumix cannot copy this, because ICS tier, dividend entitlement, credit standing and buyback rights are all holder state that an anonymous DEX transfer destroys. The supporting signal for the ERC-3643 lean is Paxos's *newest* deployment: on Solana it chose **Token-2022 with native compliance extensions** rather than the barest standard available. Given the choice today, the most conservative issuer in the category picks the compliance-native token.

**4. Regulatory route: PAXG is not a UAE comparable and should not be used as one.** No VARA, ADGM, DFSA or MiCA authorisation was found. It is a US national trust bank product distributed globally through exchange listings. The transferable insight is structural: Paxos put the **entity** under a prudential fiduciary regulator and kept the **product** deliberately simple, so the token needed no separate securities analysis. Aurumix's hybrid (gold core plus dividend plus credit) is what forces dual regulation. The Paxos precedent argues for **severability**: license the gold core cleanly as an ARVA and place the dividend and credit facility in a separate, separately-regulated entity, rather than seeking one licence that covers a hybrid.

**8. Distribution: the gap is real and it is Aurumix's actual differentiator.** No SIP, no recurring buy, no referral, no affiliate, no agent tier. Plus a **$2/month inactivity fee** that penalises exactly the dormant retail saver Aurumix courts. Nothing in the credible end of this market is competing for the monthly-contribution customer.

**9. Wind-down: partially, and better than any peer, but still not a plan.** Paxos's marketing asserts segregated, bankruptcy-remote accounts and that "your gold bars will always be yours, even in the unlikely case something happens to Paxos", and the OCC trust charter gives that real structural force. But **the PAXG terms contain no issuer-insolvency clause**, only a Clearing Bank default disclaimer, and there is **no published wind-down procedure**: no trustee, no sequence, no distribution mechanic. The brief's observation holds even against the best-documented issuer in the category. **A concrete, ex ante wind-down plan remains unclaimed ground, and Aurumix can take it cheaply.**

## 13. Open items for verification

- [ ] Read the PAXG ERC-20 contract state directly on-chain (`feeRate` / `feeParts` on `0x45804880de22913dafe09f4980848ece6ecbaf78`) to confirm the transfer fee is currently zero, and enumerate the actual admin role names and their current holders. Etherscan blocked automated fetch during this pass.
- [ ] Obtain the **Paxos User Guide / Pricing Supplement** referenced throughout the T&Cs. It contains the physical bar redemption fee, which is nowhere on the public fee page. The $20/$30 figures in circulation are secondary-source only.
- [ ] Confirm the **Solana PAXG mint address** from a Paxos primary source, and confirm whether Solana PAXG is natively issued or bridged. The Paxos newsroom Solana post found is from December 2023 and covers USDP only. Distinguish it from the "Portal"-wrapped PAXG already on Solana.
- [ ] Download one recent **KPMG attestation report PDF** (e.g. June 2026) and record the exact ounces attested, the attestation standard cited, and whether KPMG confirms allocation and serial numbers or only aggregate weight.
- [ ] Verify the claimed **annual Bureau Veritas physical bar audit** against a Bureau Veritas or Paxos primary source. Currently Confidence: Low and possibly a secondary-source invention.
- [ ] Retrieve the **OCC conditional approval order** for Paxos Trust Company, N.A. (the PDF linked from NR 2025-125) and record the charter number, capital and liquidity conditions, and any operating agreement restricting non-fiduciary activity.
- [ ] Confirm whether **Brink's** is still the vault operator post-OCC-conversion, and whether more than one vault operator is used. The Brink's naming sits on a Paxos blog post, not in the terms.
- [ ] Establish the current status of the **creation fee waiver** (the page renders an impossible date, "09/31/26") and whether standard creation tiers have resumed.
- [ ] Confirm whether the **$2/month inactivity fee** applies to on-chain holders or only to Paxos account holders with custodied balances.
- [ ] Check whether Paxos has published any **wind-down or resolution plan** as a condition of the OCC charter (national trust banks may face resolution-planning expectations that are not in the customer terms).
