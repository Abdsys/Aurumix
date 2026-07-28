### 4.7 MG 999 On-Chain Gold Fund (MG999)

| Field | Detail |
|---|---|
| Issuer | Three Singapore entities. Fund manager and issuer of record: FundBridge Capital Pte. Ltd. Tokenisation platform: Libeara (Singapore) Pte. Ltd., UEN 202302950G. Borrower and gold provider: Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025, $0 paid-up capital. Libeara is not the issuer. Marketed as "Libeara, the tokenisation platform incubated by Standard Chartered's SC Ventures" |
| Licence covering the token | None. Libeara (Singapore) Pte. Ltd. holds a live MAS Capital Markets Services licence for dealing in capital markets products (securities and collective investment schemes). FundBridge holds a separate CMS licence for fund management and dealing in CIS, plus exempt financial adviser status. Neither is a product approval. MG999 has not been authorised or recognised by MAS as a retail scheme |
| Assets under management | ~$12.44M, down 7.08% over 30 days. NAV $130.00 on 95,983.65 tokens. Announced at $15M in December 2025 and has shrunk since |
| Backing | No gold. MG999 is a secured private credit fund whose asset is a loan to a jewellery retailer, secured on shop inventory. Token value correlates to gold spot because the loan is denominated in gold |
| Custody fee charged to holders | No gold custody fee, because there is no gold to store. Management fee 1.00% per annum |
| Yield paid to holders | ~2.0% to 2.3% net, advertised for the thGOLD wrapper. MG999 itself publishes no target yield |
| Redemption | No physical redemption, and none is possible. Cash redemption stated as daily at 0% fee. No lock-up, notice period, gate, side-pocket or suspension provision in any public source. Accredited, institutional and non-US investors only |
| Token standard | ERC-20 on Ethereum, with deployments to Arbitrum (zero supply) and Avalanche C-Chain. Contract addresses not published by Libeara, FundBridge or Theo. Permissioning mechanism not documented. Wrapped for DeFi as thGOLD by Theo on Ethereum, Arbitrum and Stable |
| Reserve verification | None, and none is possible. No reserve, no bullion custodian, no bar list, no proof-of-reserve feed, no reserve attestation. Fund trustee and custodian: Perpetual (Asia) Limited, a corporate trustee rather than a vault. Administrator: Vistra Alternative Investments. Auditor: KPMG, as fund auditor of financial statements. No smart contract audit found |

#### What it is

MG999 is not a gold token. It is a tokenised private credit fund that lends money to a jeweller.

Every other protocol in this set is a version of a custody receipt: the buyer gives the issuer cash, the issuer buys metal, the metal sits in a vault, the token points at the metal. MG999 inverts that. Investors put up cash, the cash is lent to Mustafa Gold, a Singapore jewellery retailer, and the loan is secured on Mustafa's shop inventory. The token tracks gold spot because the loan is denominated in gold, not because a gram exists anywhere on the fund's balance sheet.

Launch coverage was blunter than the marketing: "MG 999 does not possess physical bullion. Instead, the tokens are crafted to replicate gold's market performance, offering a synthetic exposure method." FundBridge frames the same structure as one that "eliminates traditional vaulting and logistics costs while maintaining price exposure."

Libeara's CEO Aaron Gwak describes the mechanism directly: "Mustafa pledges its physical gold assets for loans and gold tokens are issued based on the value of the pledged gold. Investors put up cash, which is loaned to Mustafa at a specified interest rate and tenure... During the loan tenure, Mustafa pays interest to investors... monthly pricing refreshes the pricing and the interest rate that Mustafa has to pay, i.e., a variable interest rate. At the end of the tenure, Mustafa pays back the loan in full."

This is a very old trade. Jewellers have borrowed metal rather than cash for centuries, precisely so their inventory financing cost is not exposed to the gold price. What is new is wrapping the lender side in a token and selling it as gold exposure.

On scale, MG999 is $12.44M of assets with two holders and zero transfers in the last thirty days. It is the smallest and least-used product here. Its value is structural, not commercial.

#### Legal structure and regulatory standing

A holder owns units in a collective investment scheme whose asset is a loan receivable. Not gold, not a claim on gold, not a direct claim on the pledged collateral. The chain of claim runs four steps. The token holder owns a tokenised unit in the MG999 fund, a CIS under Singapore's Securities and Futures Act 2001. The fund's asset is a secured loan to Mustafa Gold Pte. Ltd. That loan is secured by a charge or pledge over Mustafa's gold inventory. And that inventory sits in Mustafa's retail business, being sold to shoppers. The holder is three legal steps from any metal, and the metal at the end of the chain is working stock in a shop, not sealed bullion in a vault. Gwak confirms the collateral is live trading stock, with interest and pricing resetting monthly "due to stock depletion and replenishment".

What is not disclosed is substantial. Across Libeara's site, FundBridge's site, Theo's documentation and the launch coverage, none of the following is published: the legal form of the fund vehicle (Singapore VCC, Cayman company, sub-fund of an umbrella); whether legal title to the pledged gold passes to the fund or remains with Mustafa subject to a security interest; whether the collateral is perfected and registered, and against what; the default waterfall, meaning how unit holders rank, who enforces and in what forum; whether the pledged inventory is insured and who is loss payee; and any offering document, private placement memorandum, prospectus or factsheet in the public domain.

That last one is the headline. For a product whose selling proposition is institutional pedigree, there is no public offering document at all. What is available is a press release and a data-aggregator row. Compare VNX, which publishes signed ISRS 4400 reserve reports and terms defining co-ownership down to one thousandth of a bar. A reader can find out what a VNX holder owns. For MG999, a reader cannot establish the vehicle type, let alone the enforcement mechanics.

**Two Libeara companies, and the wrong one is widely cited.** ACRA holds two distinct entities:

| Entity | UEN | Incorporated | Classification | Role |
|---|---|---|---|---|
| LIBEARA PTE. LTD. | 202300566N | 4 January 2023 | SSIC 64201, bank and financial holding companies | Holding company. Not the licensee |
| LIBEARA (SINGAPORE) PTE. LTD. | 202302950G | 2023 | Not published | The MAS CMS licensee. The operating entity named in Libeara's own terms and conditions |

Almost every secondary source, and several company-data aggregators, resolve "Libeara" to 202300566N, the holding company, which holds no licence. Anyone doing a casual check will either find a holding company with no MAS record and conclude Libeara is unlicensed, or find the licence and attribute it to the wrong entity. The licence is real. It is simply not in the company most people will look up. A name search for "Libeara" in the MAS Financial Institutions Directory also fails to surface the record; it is reachable only through the direct institution-detail URL.

**What the CMS licence actually covers, versus what it is presented as covering.** This distinction matters more than the licence itself.

Libeara (Singapore) Pte. Ltd. is a Capital Markets Services licensee for dealing in capital markets products, sub-categories securities and collective investment schemes. Status active, CEO of record Gwak Yun Seok (Aaron Gwak), address 9 Raffles Place. The licence was granted in March 2026 following an in-principle approval in July 2025, and the MAS record was last updated 22 April 2026. MAS displays no numeric licence identifier for this record. Dealing is a distribution and intermediation permission. It says nothing about the merits of any product Libeara tokenises.

FundBridge Capital Pte. Ltd. is separately a CMS licensee for fund management and dealing in collective investment schemes, and an exempt financial adviser. CEO Lim Sue Lynn (Lin Shuling), address 39 Duxton Hill, status active, record updated 16 July 2026. FundBridge is the entity actually responsible for MG999.

Neither licence is a product approval. MG999 has not been authorised or recognised by MAS as a retail collective investment scheme. It is a restricted scheme sold to accredited and institutional investors only, the exemption route under which MAS does not vet the offering document. The absence of a public offering document and the accredited-investor restriction are the same fact viewed from two sides.

No non-Singapore licence was found. Gwak has flagged Hong Kong as an expansion target, but there is no SFC registration, no UAE registration and no US registration. Libeara's marketing has at times been read as claiming multi-jurisdictional standing on the strength of prototype work for the Hong Kong government, Ghana and the Philippines. Government prototype work is not a licence. On the evidence, Singapore only.

Mustafa Gold Pte. Ltd. holds no financial licence and does not need one, being a borrower rather than an intermediary.

#### Custody and reserve verification

There is no reserve, so there is nothing to attest. The relevant question is collateral, and the disclosure there is the weakest part of the structure.

There is no bullion custodian, because the fund holds no bullion. Perpetual (Asia) Limited is the fund trustee and custodian, a corporate trustee rather than a vault. Vistra Alternative Investments administers the fund. KPMG is named as auditor, with no disclosed scope and no statement of whether audited financial statements yet exist for a fund launched in December 2025. There is no vault, no allocation, no bar list, and none is possible: jewellery inventory is not serialised Good Delivery bars. No proof-of-reserve feed, no collateral insurance disclosure, no published loan-to-value ratio. No smart contract audit has been published by Libeara, FundBridge or Theo.

Separating "audited" from "attested" matters more here than anywhere else in this report. KPMG is a fund auditor examining financial statements. That is not a reserve attestation, because there is no reserve, and it is not a smart contract audit, of which none was found. Anyone reading "KPMG-audited, Standard Chartered-backed" and inferring that a Big Four firm has verified gold in a vault would be wrong on both halves. Gwak states that Mustafa's "inventory undergoes strict auditing processes to ensure it complies with Singapore's AML/CFT laws". That is an anti-money-laundering control statement, not a collateral valuation attestation.

The credit protection that is disclosed is a 20% first-loss buffer. Theo's launch article states that investors are protected by "security over gold inventory and a 20% first-loss buffer held by the fund sponsor". That is a meaningful credit enhancement, better than anything the crypto-native gold-yield products offer. Every operative detail is missing: who the fund sponsor is (FundBridge, Mustafa or Libeara), whether the buffer is funded in cash or gold, whether it is segregated or a mere contractual undertaking, whether it is topped up as the loan book grows, and whether any document evidences it. A 20% first-loss buffer that exists only in a marketing blog post is a promise, not a structure.

**The borrower's registry record.** The counterparty carrying the entire fund's credit risk is Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025. It is an exempt private company limited by shares, classified under SSIC 47731 but described as "other holding companies", with $0 paid-up capital, one officer, one shareholder, one employee at incorporation rising to three by May 2026, no auditor appointed and no financial statements on record. The fund launched on 11 December 2025, five months after this entity was incorporated.

The Mustafa Group itself is a real, substantial business: Mohamed Mustafa & Samsuddin Co. Pte Ltd, UEN 198900680Z, incorporated 21 February 1989, roughly $550M of revenue and around 2 tonnes of gold turnover a year. But the borrower of record is a newly formed, zero-capital, three-employee entity. Press coverage calls Mustafa Gold "an associate of the Mustafa Group", which is a weaker word than subsidiary, and no parent guarantee from the operating Mustafa entity is published anywhere. The reputational weight of the Mustafa name is doing work in the marketing that the borrower's balance sheet does not do in the registry.

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

It cannot. The 1% management fee alone consumes 1.00pp of a 2.50pp gross spread, capping the maximum net yield at 1.5% before any other cost, and lower once platform, wrapper, trustee, administration and audit fees are paid. A 2.3% net yield is arithmetically impossible from a 2.5% gross loan rate.

Four reconciliations are possible, none confirmed. The 2.5% figure may have described a market rate or a different transaction rather than MG999's actual coupon to Mustafa. The actual coupon may be materially higher, plausibly 4% to 6%, to leave room for the stack. Theo's 2.3% may be subsidised or promotional, or may blend in the delta-neutral gold-futures basis strategy Theo separately describes, in which case it is not purely lending yield and the "secured gold lending" story is incomplete. Or the 1% management fee may be waived during the ramp. The published figures are mutually inconsistent, and the actual loan coupon is not disclosed.

One further figure sits in Theo's launch material: "the strategy produced an average annual return of about 8.27% during 2025". That is a gold-price-inclusive total return rather than a lending yield, and it appears in the same material as the 2.3% figure.

There is no physical redemption and there never can be, because the fund owns no gold. That is a structural impossibility, not an omission in the terms. Cash redemption is stated as daily with a 0% fee, and that figure deserves scepticism. Daily liquidity against an illiquid asset is a classic maturity mismatch. The fund's only asset is a term loan to a jeweller secured on shop inventory, and loans of that kind cannot be liquidated on a day's notice. A fund offering daily redemption on such a book is either holding a large cash buffer that drags the yield, relying on the sponsor to warehouse redemptions, or reserving gating powers that are not disclosed. Which of these applies is not disclosed. No lock-up, notice period, gate, side-pocket or suspension provision appears in any public source, and no offering document exists to consult. With two holders and zero transfers in thirty days, none of this has been tested.

Subscription is daily in cash, USD base currency, 0% fee, restricted to accredited investors, institutional investors and non-US persons. No minimum subscription is published. Capacity is capped: Theo describes thGOLD as "launching with capped early access while the fund scales to full capacity", a polite way of saying the loan book cannot yet absorb much money.

#### Liquidity and distribution

MG999 has no market at all. Assets of $12.44M, supply of 95,983.65 tokens, NAV of $130.00, two holders, one active address in 30 days and zero transfers in a month. No secondary market, no exchange listing, no onchain liquidity pool, and therefore no price against spot to measure. NAV is struck by the administrator, not discovered by a market. The 30-day move of minus 7.08% tracks the gold price rather than any flow. thGOLD is the layer meant to create tradability, and it is not currently tradeable on any exchange listed by the major aggregators. Neither layer trades.

Distribution is entirely business-to-business institutional. No savings plan, no recurring purchase, no referral scheme, no affiliate programme, no agent network. Libeara's CMS dealing licence is itself the distribution strategy: the March 2026 licence was framed as letting Libeara move "from a technology platform provider to a regulated financial institution", enabling it to distribute tokenised products directly rather than only build rails for others. Theo provides the DeFi distribution layer across Hyperliquid, Uniswap, Morpho and Pendle. Geography is Singapore-centred with stated ambitions in Hong Kong and Korea. Retail is structurally excluded, the mirror image of Aurumix.

The interesting distribution insight sits on the borrower side. Libeara's growth constraint is not raising money. It is finding creditworthy gold retailers to lend to. Gwak's comparison of a 2.5% offered rate against Korean jewellers paying 12% annualised is a pitch to borrowers, and it explains the Korean investor base in the June 2026 funding round. This is a two-sided marketplace disguised as a fund.

The wrapper structure is worth recording. The MG999 fund unit is locked to accredited investors. thGOLD, issued by Theo, a separate firm founded by former Optiver and IMC traders, takes MG999 exposure onto Hyperliquid, Uniswap, Morpho and Pendle. Theo's disclaimer still restricts access to accredited and institutional investors, so this is not a retail bypass on paper. But the legal relationship between the two layers is nowhere documented. Whether a thGOLD holder is a beneficial owner of MG999 units, a creditor of Theo, or a derivative counterparty is not disclosed. Theo goes further with thUSD, a gold-backed stablecoin backed by thGOLD, announced 17 April 2026 with a $100M genesis programme and a $1bn deposit target. That is three layers of wrapper on a $12.4M loan to a jeweller: MG999 unit, thGOLD, thUSD. Each layer adds a counterparty and a fee, and only the bottom one sits inside a MAS-licensed perimeter.

On the Standard Chartered connection: substantive on the licensing and platform side, reputational on the product side. Standard Chartered is nowhere in the MG999 stack. Not the issuer, not the manager, not the custodian, not the trustee, not the auditor, not the borrower's guarantor. It is a shareholder in a portfolio company that provides tokenisation software. On the separate ULTRA treasury product, Standard Chartered does provide actual custody, which is a bank doing bank work. But every phrase like "Standard Chartered-backed gold fund" describes a venture equity relationship two removes from the product. SC Ventures did not participate in Libeara's June 2026 $14M round, no shareholding percentage has ever been disclosed, and after a $14M external round the stake has necessarily been diluted. The round was led by GSR, which SC Ventures had itself invested in a month earlier, so it is weaker external validation than it appears.

#### Relevance to Aurumix

**The inversion that matters most.** The bank-affiliated platform produced a better licence than the crypto-natives. It did not produce better paperwork.

Libeara holds a real, current, correctly scoped MAS licence, verified on the register with a named CEO. Of the protocols profiled here, that is a result a regulator name search produces in only a handful of cases. And yet MG999 publishes no offering document, no contract address, no smart contract audit, no loan coupon, no loan-to-value ratio, no default waterfall, no insurance detail, and no evidence for its headline 20% first-loss buffer beyond a sentence in a partner's blog post. VNX Commodities AG, a small Liechtenstein operator holding 13 kg of gold, publishes more legally operative detail about what a holder owns than a Standard Chartered-incubated platform does.

The reason is structural rather than cultural, and it is the transferable lesson. The accredited-investor exemption is what removes the disclosure obligation. By selling only to accredited and institutional investors, MG999 avoids prospectus registration and with it the requirement to publish anything. The licence and the opacity are not in tension. The licence is what buys the opacity. An institutional wrapper is a disclosure reduction technology, not a disclosure enhancement technology, and any Aurumix positioning that assumes "regulated therefore transparent" has the causation backwards.

**The arithmetic discipline.** MG999's published 2.5% gross against 2.3% net does not survive a 1% management fee. This is the third protocol, after Kinesis and PGOLD, where the advertised yield cannot be reconciled with disclosed revenue, and it is the strongest evidence in this report that advertised gold yields do not survive arithmetic. It is not a crypto-native failing: a MAS-licensed, KPMG-audited, bank-incubated structure does it too. The failure to reconcile advertised yield with disclosed revenue is not correlated with regulatory status. Aurumix must publish its gross source rate, its full fee stack and its net-to-holder number in the same table, or it will be indistinguishable from these.

**What to take on the dividend question.** MG999 is the first structure in this report where the yield is paid by an external commercial counterparty rather than recycled from investor fees. Mustafa Gold pays interest because it gets working capital cheaper than a bank would lend it. That is real economic value creation, not circular flow, and it is the category of thing Aurumix needs for its ICS Dividend.

- **Copy the credit-enhancement pattern, and do it properly.** A first-loss tranche funded by the operator and sitting ahead of holders converts "trust us" into a quantified subordination. Cheap to describe, powerful in a disclosure document. Fund it, segregate it, size it against the book, and publish the evidence. Libeara's version exists only as a sentence.
- **Note where the scarce resource actually is.** Libeara's binding constraint is creditworthy borrowers, not investors. Aurumix's India and UAE markets are full of jewellers who currently borrow at Muthoot-style rates. That is a more accessible yield source for a Dubai and India operator than institutional gold leasing, and it is on Aurumix's doorstep.
- **Do not treat MG999 as the documented precedent.** Its collateral is retail jewellery inventory on a shop floor, which is worse collateral than vaulted bullion. It depletes, it is fungible, it is hard to perfect a security interest over, and the borrower is selling it to customers in the ordinary course of business. How MG999 unit holders rank on a Mustafa default is not disclosed anywhere. Streamex is the better template.

**The regulatory lesson is inverted.** MAS licensed Libeara's dealing activity and FundBridge's fund management. It did not approve the product. MG999 avoids product-level scrutiny by being a restricted scheme for accredited investors. That escape hatch is unavailable to Aurumix, which is mass retail at $20 a month by design. The institutional route's cost is that you cannot sell to retail, and Aurumix's entire thesis is retail. Aurumix can borrow MG999's licensing discipline, not its regulatory posture.

**On the custody fee question**, MG999 offers a genuine third option beyond the cash-versus-grams framing: do not hold the metal at all. It charges no gold custody fee because it holds no gold, and it is explicit that removing vaulting, insurance and storage cost is the product's reason for existing. It replaces storage cost with credit risk on a jeweller, a real trade honestly stated. It is not available to Aurumix, whose promise is that 100% of every dollar buys physical LBMA gold and whose token price is vault grams divided by tokens. Aurumix has a vault, so it has a storage cost, so it must recover that cost in cash. MG999 confirms the cash-recovery conclusion by showing that the only way to avoid the cost entirely is to abandon physical backing.

**On the wrapper architecture**, MG999 is a live demonstration of the pattern Aurumix is leaning toward: a restricted regulated unit at the base, a freely composable wrapper on top issued by a different firm. The warning is that the legal relationship between the two layers must be documented, and here it is not. Nobody can say from public sources whether a thGOLD holder owns fund units, has a claim on Theo, or holds a derivative. Aurumix will face the identical question about ICS standing, dividend entitlement and buyback rights on a wrapped token, and must answer it in writing at design time.

**On redemption**, MG999 is the one protocol in this set with less physical redemption than Aurumix, and it is sold to institutions on that basis without apology. A Standard Chartered-incubated, MAS-licensed gold product with zero metal and zero physical redemption is being sold to accredited investors today. Aurumix's no-physical-redemption stance is not an outlier, and Aurumix actually holds the metal, which makes its position strictly stronger. It should say so. Separately, MG999's claimed daily redemption against a term loan book is a maturity mismatch Aurumix should not copy. Aurumix's cash buyback design should state its settlement window and its funding source honestly.

**On proof of reserve**, MG999 is the strongest example in this report of institutional-sounding assurance language attaching to nothing in the vault. It can truthfully say it is KPMG-audited (fund financials) and Standard Chartered-backed (venture equity), and a reader will hear that a Big Four firm and a global bank have verified the gold. There is no gold. This is Aurumix's clearest opportunity: a genuine, frequent, published reserve attestation with a bar list is a differentiator even against bank-affiliated competitors. It also adds a third category to the "audited" confusion. Reserve attestation, smart contract audit and fund audit are three different things, and MG999 has only the third.

**On wind-down**, no plan is published. Given the structure, the questions are sharper than for a vaulted product. On a FundBridge failure, who administers the loan book. On a Libeara failure, who can mint, burn and transfer the tokens, and does the register survive. On a Mustafa default, who enforces the charge and in what order do unit holders rank. None of this is documented, including by the bank-affiliated protocol with a live CMS licence. The case for Aurumix publishing a wind-down plan as cheap differentiation holds.

---

### 4.8 Streamex (GLDY)

| Field | Detail |
|---|---|
| Issuer | Streamex Ltd., a Cayman Islands exempted company formed February 2026, consolidated as a variable interest entity. Listed parent: Streamex Corp., Delaware, CIK 0001530766, Nasdaq: STEX, formerly BioSig Technologies, Inc., renamed 12 September 2025. Operating company: Streamex Exchange Corporation, British Columbia, incorporated 5 April 2024, acquired 28 May 2025. Servicer: GLDY ServiceCo, LLC, Delaware |
| Licence covering the token | None. GLDY is sold under Rule 506(c) of Regulation D, a US private-placement exemption, not an authorisation. No VARA, ADGM, MAS, FCA or CIMA licence identified. The parent's Nasdaq listing regulates the parent's shares, not the token |
| Assets under management | ~$12.84M (July 2026). The Q1 2026 10-Q records $15.225M of gold at cost on the SPV's balance sheet at 31 March 2026 |
| Backing | 1 GLDY is intended to correspond to 1 fine troy ounce held by the SPV. Gold may be held on an unallocated basis. Each token represents "a non-voting digital share of Streamex Ltd.", an equity interest in a Cayman company, not title to gold and not a trust beneficial interest. The gold is placed into Monetary Metals' commercial leasing programme, where it may be commingled with other participants' gold |
| Custody fee charged to holders | Not disclosed as a separate holder charge. Expenses borne inside the SPV, reducing net yield |
| Yield paid to holders | "Up to 4%" advertised, 3.50% APY displayed July 2026. Paid monthly as scrip dividends automatically reinvested as new GLDY tokens, not in cash |
| Redemption | On 90 days' prior written notice, proceeds payable in physical gold, stablecoins, select digital assets or US dollars, subject to undisclosed "certain limitations". The 10-K states physical redemption "may only be available under certain conditions" because gold may be unallocated with no bar-level linkage. Redemption fee not disclosed |
| Token standard | ERC-20 on Base as primary chain, with Chainlink CCIP to Solana. Whitelisted and KYC-gated to accredited investors. The issuer does not publish the contract address. Chainlink appointed official oracle provider 28 October 2025. Upgradeability and admin key custody not disclosed. No smart contract audit found |
| Reserve verification | EisnerAmper LLP examination under AICPA attestation standards as of 31 March 2026, announced 1 July 2026, monthly attestations intended thereafter. Result: 3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces, a surplus of 0.2416423 oz. Covers gold in reserve and gold on lease. Custodian described only as "an LBMA-accredited custodian", not named in any SEC filing. No bar list. A Chainlink proof-of-reserve feed is referenced but the issuer states it has not yet fully implemented a live dashboard |

#### What it is

GLDY is a gold-backed security token paying a yield sourced from real third-party gold leasing, issued by a Cayman SPV whose ultimate parent is Nasdaq-listed. Each token is intended to correspond to one fine troy ounce held by the SPV, and yield accrues because the SPV's gold goes into Monetary Metals' commercial gold-leasing programme rather than sitting idle in a vault.

This is the most relevant protocol in the report to Aurumix's dividend problem, for one reason. It is the only one where the yield-generating arrangement is described in a document filed with a securities regulator rather than asserted in marketing. ORO advertises 3% to 4% from the same counterparty, Monetary Metals, with nothing published at all. Streamex has put paper on the record.

The qualification, developed below, is that the filed paper covers the commercial relationship between Streamex and Monetary Metals. It does not cover the lease itself, and it says nothing about what a token holder gets if a lessee runs off with the gold.

The corporate history is worth knowing. This is a former medical device company, BioSig Technologies, whose PURE EP cardiac signal platform still shows on EDGAR under SIC code 3845, "Electromedical Apparatus". It acquired a Vancouver blockchain startup in May 2025 and repurposed the listing. The legacy medical business is still on the books.

#### Legal structure and regulatory standing

A GLDY holder owns "a non-voting digital share of Streamex Ltd., a Cayman Islands special purpose vehicle". That is an equity interest in a Cayman company. It is not title to gold, and it is not a trust beneficial interest.

The entity chain, verified against the SEC filings:

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

A GLDY holder is an equity holder in a Cayman company that has a contractual claim against a Delaware series LLC that has a claim against a lessee. It is the most remote position in this report, subordinate not only to the SPV's own creditors but potentially to other lessors in the same commingled pool.

On regulatory standing, GLDY holds no licence from any regulator anywhere. It is sold under Rule 506(c) of Regulation D to verified accredited investors and institutions, including non-US persons. No CIMA registration was found for Streamex Ltd. No Form D was located on EDGAR under CIK 0001530766 for the GLDY offering. SEC-reporting is not SEC-approved, and it is not the same as the token being regulated. Streamex Corp. files 10-Ks because its equity is listed on Nasdaq. The rich disclosure quality relied on throughout this profile is a by-product of the parent's listing obligations, not of any regulation of the token.

The company anticipates the classification issue candidly: "the tokenization of gold-linked instruments is expected to be treated as the issuance of securities in most jurisdictions." It treats GLDY as a security from the outset, the opposite of the ORO and Comtech posture.

One flag on internal controls. The 10-K and the 13 July 2026 8-K both report unremediated material weaknesses in internal control over financial reporting: inadequate identification and recording of stock-based compensation, ineffective period-end review, and inadequate segregation of duties. For a business whose pitch is custody and verification integrity, that is a real weakness.

#### Custody and reserve verification

The custodian is described only as "an LBMA-accredited custodian" and is not named in any SEC filing. No vault or city is disclosed. Gold may explicitly be held on an unallocated basis. No bar list is published.

The 10-K is unusually blunt about the custody weakness:

> "With respect to GLDY, gold may be held on an unallocated basis, and there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars. As a result of these operational hurdles, physical redemption for underlying assets may only be available under certain conditions, We have not yet fully implemented a live proof-of-reserves dashboard or public confirmation of 1:1 gold backing for tokens, and we are in the process of implementing an independent audit process for bullion holdings on a defined timeline."

Separating the two things: the reserve attestation exists and is real, the smart contract audit does not. EisnerAmper LLP performed an examination under AICPA attestation standards of management's assertion about gold held for the benefit of GLDY token holders. As of 31 March 2026: 3,064.674268 redeemable GLDY outstanding against 3,064.915910 fine troy ounces, a surplus of 0.2416423 oz. The examination covers gold in reserve and gold on lease, the correct scope for a leasing structure. No published audit of the Base ERC-20 contract or the CCIP integration was found. This is one of the few protocols in the set where the attestation exists and the contract audit does not, the reverse of the usual pattern.

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

Exhibit 10.1 Section 6.01 sets out the purchase-fee ladder verbatim: 0 to $250K at 0.75%, $250K to $1M at 0.55%, $1M to $5M at 0.40%, $5M to $25M at 0.30%, $25M to $50M at 0.25%, above $50M at 0.20%, with a quarterly cash rebate reconciling fees actually paid against the aggregate-volume tier.

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

Distribution is institutional and accredited only, and this is the sharpest contrast with Aurumix in the entire profile. No savings plan, no SIP, no recurring purchase mechanism, no referral, affiliate or agent-commission network. The minimum ticket is $200,000 for an individual, $300,000 joint and $1,000,000 institutional. Channels are direct through app.streamex.com, a distribution partnership with Siebert covering wealth-management and institutional channels, and the Nasdaq-listed parent as the credibility vehicle. Geography is US accredited investors plus non-US persons.

The filed agreement itself excludes much of Aurumix's target market on the lessee side. Exhibit 10.1 defines "Restricted Nation" as "any country located in Africa", any sanctioned territory, plus Afghanistan, Bangladesh, Belarus, El Salvador, Haiti, Honduras, Iraq, Lebanon, Myanmar (Burma), Nicaragua, Pakistan, Russia, Turkey, Ukraine, Venezuela and Yemen. This restricts where Monetary Metals will place gold, not where investors may live. India and the UAE are not excluded. Pakistan, Bangladesh and the whole of Africa are.

One litigation item is on the record. In November 2025 a former advisor filed a Notice of Civil Claim in the Supreme Court of British Columbia against the Company, Streamex Exchange Corporation and certain officers and directors, alleging breach of contract, unjust enrichment and civil conspiracy over equity interests predating the acquisition. The company disputes the claim and has recorded no liability.

#### Relevance to Aurumix

Streamex is the single most useful protocol in this report for Aurumix's dividend question, and the answer splits cleanly into a template to copy and a gap to fill.

**What is proven: real, externally funded gold yield is documentable, and the document is public.** Exhibit 10.1 to accession 0001641172-25-026853 is a genuine, executed, publicly filed agreement carrying a 3% per annum net-after-origination-fees yield floor defining a qualifying lease, a two-layer insurance standard, and real economics in the 0.20% to 0.75% purchase-fee ladder and the 0.35% to 0.50% revenue share. Aurumix now has a precedent it can point to and copy for structuring a leasing relationship. That is more than ORO ever published, and more than MG999 publishes.

Two clauses are worth copying almost verbatim:

- **The "Passing Lease" definition**: a lease qualifies only if it generates a net yield of at least 3% per annum after origination fees.
- **The absolute discretion to reject any individual lease** (Section 3.01(b)).

Together those two let an issuer advertise a yield range honestly without guaranteeing it. The floor is a screening criterion applied to the counterparty, not a promise made to the holder.

The insurance schedule is the third thing to copy: a lessee-funded jeweller's block policy at 110% of lease value from an A.M. Best A- or better insurer, plus an issuer-funded Difference in Conditions and Difference in Limits layer through a Lloyd's broker covering mysterious disappearance and bad acts by the lessee's own management, also at 110%.

**What is not proven, and this is the gap Aurumix must fill.** The filed agreement contains no security interest, no title-retention clause, no risk-of-loss allocation, no subordination, no loss waterfall and no default ranking. The lease documents that would contain those terms are expressly deferred to a later, unfiled, New York law "Lease Documentation" set. The yield-generation precedent exists. The holder-protection precedent does not. Streamex has documented the revenue side and left the risk side to private paper.

The insurance beneficiary answer is the sharpest illustration. Both layers say: "MM shall require the insured to name MM as a loss payee and additional insured wherever possible." Three problems follow. The loss payee is Monetary Metals, not Streamex, not Streamex Ltd., and not the token holder. "Wherever possible" is a best-efforts phrase rather than a covenant, which means there will be leases where Monetary Metals is not named. And nothing anywhere obliges anyone to name StreamEx, the SPV or holders as loss payee, additional insured or third-party beneficiary. Insurance proceeds land at Monetary Metals and then have to travel back down a chain of contracts, through a commingled pool in which "other lessors may receive more favorable terms or priority in enforcement scenarios", before any of it reaches a holder. Recovery is a litigation and contract-chain problem, not an entitlement.

**The risk is realised, not theoretical.** The AgaBullion lessee default of 26 January 2026 is the live test of this design, with the Turkish seizure of the lessee's assets standing between the programme and its metal. When a gold lessee fails, "title remains with the lessor" means litigating abroad, and whether the Lloyd's Difference in Conditions layer actually paid out has not been published by Monetary Metals. Aurumix should not design a dividend on the assumption that a documented insurance stack converts lessee credit risk into a recoverable claim. Streamex's paper is better documented than the AgaBullion situation, and it still does not change the holder's fundamental position.

**The audience gap is the decisive point.** Streamex sells this risk to verified accredited investors at a $200,000 minimum ticket. Those buyers can price counterparty risk, read a 10-K risk factor section, and absorb a total loss. Aurumix would sell the same category of risk to a saver putting in $20 a month.

That asymmetry cuts across every other consideration. To earn 3% to 4%, the gold must leave the issuer's control, be commingled with strangers' gold, become unreturnable for 90 days, and expose holders to a jeweller's credit. Streamex's own 10-K tells its investors they "may face delays, partial recovery, or total loss". For a mass-retail SIP product sold to first-time savers in India and the UAE, that trade is materially worse than it is for a professional at a $200,000 minimum. Aurumix's ICS Dividend is promised to retail. If Aurumix adopts leasing, the disclosure burden and the wind-down obligations scale with the audience, not with the size of the book.

**The differentiating move is available and unoccupied.** If Aurumix builds a leasing-funded dividend, the differentiator is not the lease. It is being the first issuer to name the token holders, or a trustee acting for them, as loss payee, and to publish the default waterfall. Every protocol profiled here, including this one, leaves that gap open. It is cheap to close.

Four further points transfer directly:

- **Custody fee.** No disclosed holder-facing custody fee. Costs are absorbed inside the SPV and paid out of lease income before yield reaches holders. That is the third option executed cleanly: the external yield pays for the custody, and it is peg-neutral because it never touches grams. It is the most attractive single idea in this profile for Aurumix.
- **Token standard.** Streamex treats the instrument as a security from day one and went permissioned and whitelisted, ERC-20 on Base with KYC gating and CCIP for cross-chain reach. It bought compliance and it cost the product any real secondary market: 19 holders. Aurumix's ERC-3643 lean is directionally right. The lesson is that permissioning and liquidity are a genuine trade, not a free win.
- **Redemption.** Once gold is leased, instant redemption becomes structurally impossible. GLDY's 90-day notice is the honest form of that constraint. Aurumix's no-physical-redemption stance is at least internally consistent with a yield-bearing design. The presentational risk is identical for both: advertising "you own physical gold" while operating a notice-period claim on a commingled leased pool.
- **Proof of reserve: right scope, wrong sequence.** The EisnerAmper examination explicitly covers gold in reserve and gold on lease, exactly the scope Aurumix must specify if it ever leases. But Streamex launched the token in February 2026 and produced its first attestation in July 2026, having disclosed in the interim that it had no live proof-of-reserve dashboard and no bar-level linkage, and the attestation covers ounces that are 98.5% owned by the issuer. Attest before you sell, not after, and do not let an attestation over your own inventory be mistaken for holder protection.

**The regulatory route is unavailable to Aurumix.** No licence anywhere, a US private-placement exemption into a Cayman SPV, with credibility borrowed from the parent's Nasdaq listing. That route is accredited-investor-only by construction, the exact opposite of a $20-a-month retail SIP. Nothing here provides an alternative to VARA, and nothing here touches the ADGM Accepted Spot Commodity route. What it does show is that a listed parent produces high-quality public disclosure as a by-product of its listing obligations, a reputational asset Aurumix cannot replicate cheaply.

**On wind-down, no plan is published**, and the disclosed failure mode is severe: holders "may face delays, partial recovery, or total loss in the event of SPV insolvency or service provider failure", with other lessors in the commingled pool potentially receiving "more favorable terms or priority in enforcement scenarios". The failure mode is disclosed but unplanned. Even the best-documented protocol in this set, with a Nasdaq-listed parent and a Big Four-adjacent attestor, has not said what happens to the gold if it fails.

---
