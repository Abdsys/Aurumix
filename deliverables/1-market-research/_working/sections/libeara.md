# MG 999 On-Chain Gold Fund (MG999), tokenized by Libeara

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | MG999. Wrapped for DeFi as **thGOLD** by a third party, Theo | **High** |
| Issuer (marketing) | "Libeara", presented as "the tokenisation platform incubated by Standard Chartered's SC Ventures" | **High** |
| Issuer (registry) | **Three separate entities.** Fund manager and issuer of record: **FundBridge Capital Pte. Ltd.** Tokenisation platform: **Libeara (Singapore) Pte. Ltd.**, UEN **202302950G**. Borrower / gold provider: **Mustafa Gold Pte. Ltd.**, UEN **202529232Z**. Libeara is **not** the issuer of MG999 | **High** |
| Domicile | Singapore, all three entities | **High** |
| Backing claim | **The fund holds no gold.** MG999 is a **secured private credit fund** whose assets are loans to gold retailers, secured on the borrower's gold inventory. Token value is intended to "correlate to the spot price of gold" ([Libeara](https://libeara.com/)) | **High** |
| Chains | Ethereum (all live supply), Arbitrum (zero supply), Avalanche C-Chain ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). thGOLD separately on Ethereum, Arbitrum and Stable | **High** |
| Contract address(es) | **Not disclosed publicly.** rwa.xyz gates contract addresses behind a login; Libeara and FundBridge publish none | **High** (that they are undisclosed) |
| Supply | **95,983.65 MG999** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)) | **High** |
| Market cap / TVL | **~$12.44M**, down 7.08% over 30 days. NAV **$130.00/token** | **High** |
| Holders | **2.** Trailing 30-day active addresses: 1. Monthly transfer count: **0** | **High** |
| Regulatory status | **Libeara (Singapore) Pte. Ltd. holds a live MAS Capital Markets Services licence**: Dealing in Capital Markets Products (Securities; Collective Investment Schemes). Verified on the [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution/detail/431842-LIBEARA-SINGAPORE-PTE-LTD). **FundBridge Capital Pte. Ltd.** separately holds CMS (Fund Management; Dealing in CIS) plus Exempt Financial Adviser ([MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/218507-FUNDBRIDGE-CAPITAL-PTE-LTD)). **Mustafa Gold Pte. Ltd. holds no financial licence** | **High** |
| Subscription fee | **0%** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)) | **Medium** |
| Ongoing custody fee | **No gold custody fee, because there is no gold to store.** Management fee **1.00%/yr** | **High** |
| Redemption fee | **0%**, daily subscription/redemption frequency | **Medium** |
| Advertised yield | **~2.0% to 2.3% net** to thGOLD holders ([Fortune, 27 Jan 2026](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)). MG999 itself publishes no target yield | **High** |
| Named officers | **Gwak Yun Seok (Aaron Gwak)**, CEO, Libeara (Singapore) Pte. Ltd. (MAS FID). **Lim Sue Lynn (Lin Shuling)**, CEO, FundBridge Capital (MAS FID). **Mustaq Ahmad**, founder, Mustafa Group | **High** |
| Custodian | **Perpetual (Asia) Limited** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). This is a **fund trustee/custodian, not a bullion vault** | **High** |
| Administrator / Auditor | **Vistra Alternative Investments** / **KPMG** | **Medium** |
| Eligibility | **Accredited, institutional and non-US investors only.** No retail | **High** |

---

## 1. What it is

MG999 is not a gold token. It is a **tokenised private credit fund that lends money to a jeweller**.

This is the single most important sentence in this profile, and it is the reason MG999 sits in this landscape at all. Every other protocol in this set is some version of a custody receipt: you give the issuer cash, the issuer buys metal, the metal sits in a vault, the token points at the metal. MG999 inverts that. Investors put up cash, the cash is lent to **Mustafa Gold**, a Singapore jewellery retailer, and the loan is secured on Mustafa's shop inventory. The token's value is *engineered* to track the gold spot price because the loan is denominated in gold, not because a gram of gold exists anywhere on the fund's balance sheet.

The launch coverage is blunt about this where the marketing is not. "MG 999 does not possess physical bullion. Instead, the tokens are crafted to replicate gold's market performance, offering a synthetic exposure method" ([crypto.news, Dec 2025](https://crypto.news/standard-chartered-backed-libeara-rolls-out-mg-999-tokenized-gold-fund-in-singapore/)). FundBridge's own framing is that the structure "eliminates traditional vaulting and logistics costs while maintaining price exposure."

The mechanism, per Libeara's CEO Aaron Gwak and The Edge Singapore's reporting ([Jan 2026](https://people.duke.edu/~charvey/Media/2026/E_January_29_2026.pdf)):

> "Mustafa pledges its physical gold assets for loans and gold tokens are issued based on the value of the pledged gold. Investors put up cash, which is loaned to Mustafa at a specified interest rate and tenure... During the loan tenure, Mustafa pays interest to investors... monthly pricing refreshes the pricing and the interest rate that Mustafa has to pay, i.e., a variable interest rate. At the end of the tenure, Mustafa pays back the loan in full."

This is a very old trade. Jewellers have borrowed metal rather than cash for centuries, precisely so that their inventory financing cost is not exposed to the gold price. What is new is wrapping the lender side in a token and selling it as gold exposure.

**Scale reality check.** MG999 is **$12.44M of AUM with two holders and zero transfers in the last thirty days**. It was announced at a $15M fund size in December 2025 and has shrunk. It is by some distance the smallest and least-used product in this landscape. Its value to us is entirely structural, not commercial.

## 2. Legal structure

**What a holder owns: units in a collective investment scheme whose asset is a loan receivable.**

Not gold. Not a claim on gold. Not even a claim on the pledged collateral directly. The chain of claim runs:

1. Token holder owns a **tokenised unit** in the MG999 fund (a CIS under the Singapore Securities and Futures Act 2001).
2. The fund's asset is a **secured loan to Mustafa Gold Pte. Ltd.**
3. The loan is secured by a **charge or pledge over Mustafa's gold inventory**.
4. That inventory sits in Mustafa's retail business, being sold to shoppers.

So the holder is **three legal steps away from any metal**, and the metal at the end of the chain is working inventory in a shop on Serangoon Road, not sealed bullion in a vault. Gwak's own description confirms the collateral is live trading stock: interest and pricing reset monthly "due to stock depletion and replenishment."

**What is not disclosed, and it is a lot.** Across Libeara's site, FundBridge's site, Theo's documentation and every news source we could reach, none of the following is published:

- The **exact legal form of the fund vehicle**. Singapore VCC? Cayman company? Sub-fund of an umbrella? **Not disclosed.** rwa.xyz gives the domicile as Singapore and the governing statute as the SFA 2001, but not the vehicle type or a registration number.
- Whether **legal title** to the pledged gold passes to the fund or remains with Mustafa subject to a security interest. **Not disclosed.**
- Whether the collateral is **perfected**, registered, and against what. **Not disclosed.**
- The **default waterfall**: how unit holders rank, who enforces, in what forum. **Not disclosed.**
- Whether the pledged inventory is **insured**, and who is loss payee. **Not disclosed.**
- Any **offering document, PPM, prospectus or factsheet** in the public domain. **Not disclosed.**

That last one is the headline. For a product whose entire selling proposition is institutional pedigree, **there is no public offering document at all**. We checked Libeara's site, its Terms and Conditions, FundBridge's site, Theo's docs subdomain and the launch press releases. What is publicly available is a press release and a data-aggregator row.

**Contrast with the direct-holding protocols.** VNX publishes signed ISRS 4400 reserve reports and terms that define co-ownership down to the 1/1000th of a bar. Whatever VNX's internal inconsistencies, a reader can find out what they own. For MG999 a reader cannot, from public sources, establish the vehicle type, let alone the enforcement mechanics.

## 3. Regulatory and compliance posture

**This is where MG999 genuinely beats the crypto-native field, and it should be credited for it.** Two of the three entities are real MAS licensees, verified on the register.

**Libeara (Singapore) Pte. Ltd.** UEN 202302950G.
- **Capital Markets Services Licensee.** Regulated activity: **Dealing in Capital Markets Products, sub-categories Securities and Collective Investment Schemes.** Status: active. CEO of record: **Gwak Yun Seok (Aaron Gwak)**. Address: 9 Raffles Place #18-21, Republic Plaza.
- Verified directly on the [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution/detail/431842-LIBEARA-SINGAPORE-PTE-LTD), record last updated 22 April 2026. **Confidence: High.**
- Granted **March 2026**, following an in-principle approval in **July 2025** ([Libeara](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/), [Ledger Insights](https://www.ledgerinsights.com/stancharts-libeara-tokenization-platform-lands-singapore-cms-license/)).
- **The MAS record displays no licence number.** MAS's FID does not surface CMS licence numbers in this view. Our check is by name and record ID (431842). We could not obtain a numeric licence ID from any public source: **Not disclosed.**

**FundBridge Capital Pte. Ltd.**
- **Capital Markets Services Licensee** and **Exempt Financial Adviser**. Regulated activities: **Fund Management**; **Dealing in Capital Markets Products (Collective Investment Schemes)**; Arranging of Life Policies. CEO: **Lim Sue Lynn (Lin Shuling)**. Address: 39 Duxton Hill #04-01. Status: active, record updated 16 July 2026 ([MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/218507-FUNDBRIDGE-CAPITAL-PTE-LTD)). **Confidence: High.**

**Mustafa Gold Pte. Ltd.**
- **No financial licence, and it does not need one**: it is a borrower, not a financial intermediary. But its registry record deserves attention. See §4.

### ⚠️ Registry finding: there are two "Libeara" companies and the wrong one is widely cited

ACRA holds **two** distinct Libeara entities:

| Entity | UEN | Incorporated | SSIC | Role |
|---|---|---|---|---|
| **LIBEARA PTE. LTD.** | **202300566N** | **4 January 2023** | 64201, *Bank/financial holding companies* | Holding company. **Not the licensee.** |
| **LIBEARA (SINGAPORE) PTE. LTD.** | **202302950G** | 2023 | not published | **The MAS CMS licensee.** The operating entity named in Libeara's own [Terms and Conditions](https://libeara.com/terms-and-conditions/) |

Almost every secondary source, and several company-data aggregators, resolve "Libeara" to **202300566N**, the holding company, which holds no licence. A reader doing a casual check would either find a holding company with no MAS record and conclude Libeara is unlicensed, or find the licence and attribute it to the wrong entity. **The licence is real. It is just not in the company most people will look up.** Confidence: **High**, both entities confirmed against ACRA-derived records and the licensee confirmed against MAS directly.

Note also that a plain name search for "Libeara" in the MAS FID returns nothing useful: the directory's name filter did not surface the record in our testing, and we reached it only via the direct institution-detail URL. This is a MAS UI limitation, not a licensing gap, but it is worth knowing if anyone repeats the check.

### What the CMS licence does and does not cover

This distinction matters more than the licence itself.

- Libeara's CMS permits **dealing** in securities and CIS. That is a distribution and intermediation permission. It says nothing about the merits of any product Libeara tokenises.
- FundBridge's CMS permits **fund management**. FundBridge is the entity actually responsible for MG999.
- **Neither licence is a product approval.** MG999 has not been authorised or recognised by MAS as a retail CIS. It is a **restricted scheme sold to accredited and institutional investors only**, which is precisely the exemption route that means MAS does not vet the offering document. The absence of a public offering document and the accredited-investor restriction are the same fact viewed from two sides.

**No non-Singapore licence was found for Libeara.** Aaron Gwak has flagged **Hong Kong** as an expansion target ([Blockhead, 13 Mar 2026](https://www.blockhead.co/2026/03/13/libeara-secures-singapore-dealer-licence-clearing-path-to-distribute-tokenised-assets-directly/)), but we found **no SFC registration, no UAE registration and no US registration**. Libeara's marketing has at times been read as claiming multi-jurisdictional standing on the strength of prototype work for the Hong Kong government, Ghana and the Philippines ([Libeara IPA release](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/)). **Government prototype work is not a licence.** On the evidence: **Singapore only.** Confidence: **High** for Singapore, **High** that nothing else was found.

## 4. Custody and proof of reserve

There is no reserve, so there is nothing to attest. This section is therefore about **collateral**, and the disclosure here is the weakest part of the whole structure.

| Item | MG999 |
|---|---|
| Bullion custodian | **None. The fund holds no bullion.** |
| Fund custodian / trustee | **Perpetual (Asia) Limited** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). A corporate trustee, not a vault |
| Fund administrator | **Vistra Alternative Investments** |
| Auditor | **KPMG**. Scope, and whether any audited financial statements exist yet for a fund launched Dec 2025, **not disclosed** |
| Vault / city | **Not applicable.** Collateral is Mustafa's retail inventory, Singapore |
| Allocated? | **No.** The collateral is fungible, actively-traded shop stock that depletes and replenishes monthly |
| Bar list | **None, and none is possible.** Jewellery inventory is not serialised Good Delivery bars |
| PoR feed | **None** |
| Reserve attestation | **None.** Gwak states Mustafa's "inventory undergoes strict auditing processes to ensure it complies with Singapore's AML/CFT laws." That is an **AML control statement, not a collateral valuation attestation**, and the two should not be conflated |
| Smart contract audit | **Not found.** No audit report published by Libeara, FundBridge or Theo |
| Collateral insurance | **Not disclosed** |
| Loan-to-value ratio | **Not disclosed** |

**Separating "audited" from "attested", as the brief requires.** MG999 names **KPMG** as auditor. That is a *fund* auditor, examining financial statements. It is not a reserve attestation, because there is no reserve, and it is not a smart-contract audit, of which we found none published. Anyone reading "KPMG-audited, Standard Chartered-backed" and inferring that a Big Four firm has verified gold in a vault would be wrong on both halves.

**The credit protection that is disclosed: a 20% first-loss buffer.** Theo's own launch article states that investors are protected by "security over gold inventory and a **20% first-loss buffer held by the fund sponsor**" ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you)).

This is a genuinely meaningful credit enhancement and better than anything the crypto-native gold-yield products offer. **But every operative detail is missing.** Who is "the fund sponsor"? Is it FundBridge, Mustafa, or Libeara? Is the buffer funded in **cash or in gold**? Is it **segregated** or a mere contractual undertaking? Is it **topped up** as the loan book grows? Is there any published document evidencing it? On every one of those questions: **Not disclosed.** A 20% first-loss buffer that exists only in a marketing blog post is a promise, not a structure.

### ⚠️ Registry finding: the gold provider is five months old and has $0 paid-up capital

The counterparty on which this entire fund's credit risk rests is **Mustafa Gold Pte. Ltd., UEN 202529232Z, incorporated 7 July 2025** ([ACRA-derived record](https://recordowl.com/company/mustafa-gold-pte-ltd)).

- **Entity type:** Exempt Private Company Limited by Shares
- **SSIC:** 47731, but classified as **"Other holding companies"**
- **Paid-up capital: $0**
- **Officers: 1. Shareholders: 1.**
- **Employees: 1 at incorporation, 2 by October 2025, 3 by May 2026**
- **No auditor appointed, no financial statements on record**

The fund launched on **11 December 2025**, five months after this entity was incorporated. The Mustafa Group itself is a real, substantial 35-year-old business: Mohamed Mustafa & Samsuddin Co. Pte Ltd (UEN 198900680Z, incorporated 21 February 1989), roughly **$550M of revenue** and **~2 tonnes of gold turnover a year** ([Fortune](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)). But the *borrower of record* is a newly-formed, zero-capital, three-employee entity described in the register as a holding company. Press coverage calls Mustafa Gold "an associate of the Mustafa Group" ([The Edge Singapore](https://people.duke.edu/~charvey/Media/2026/E_January_29_2026.pdf)), which is a weaker word than subsidiary.

**We found no published parent guarantee from the operating Mustafa entity.** The reputational weight of the Mustafa name is doing work in the marketing that the borrower's balance sheet does not do in the registry. Confidence: **High** on the registry facts. Confidence: **High** that no guarantee is publicly documented.

## 5. Issuance

Subscription is **daily**, in cash (USD base currency), with a **0% subscription fee** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). Eligibility is **accredited investors, institutional investors and non-US persons**. There is no retail channel and no minimum published.

Units are then minted on **Libeara's platform** onto Ethereum as ERC-20. Cash raised is deployed into the secured loan. Because the loan reprices monthly against Mustafa's fluctuating inventory, the fund is effectively rolling a variable-rate revolver rather than holding a static asset.

**Minimum subscription: Not disclosed.** **Capacity: capped.** Theo describes thGOLD as "launching with capped early access while the fund scales to full capacity", which is a polite way of saying the loan book cannot yet absorb much money. That is consistent with the $12.44M AUM.

## 6. Redemption

**There is no physical redemption and there never can be.** The fund owns no gold. This is not an omission in the terms; it is a structural impossibility.

Cash redemption is stated as **daily frequency with a 0% redemption fee** ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). That figure deserves scepticism, and it is the sharpest unresolved question in this profile.

**Daily liquidity against an illiquid asset is a classic maturity mismatch.** The fund's only asset is a term loan to a jeweller, secured on shop inventory. Loans of that kind cannot be liquidated on a day's notice. A fund offering daily redemption on such a book is either (a) holding a large cash buffer, which drags the yield, (b) relying on the sponsor to warehouse redemptions, or (c) reserving gating powers that are not disclosed. **Which of these applies is Not disclosed.** No lock-up, notice period, gate, side-pocket or suspension provision appears in any public source, and no offering document exists to consult.

With **two holders and zero transfers in thirty days**, this has never been tested.

## 7. Fees and revenue model

| Fee line | MG999 / thGOLD | Source | Confidence |
|---|---|---|---|
| Subscription fee | **0%** | rwa.xyz | Medium |
| Redemption fee | **0%** | rwa.xyz | Medium |
| Management fee | **1.00% per annum** | rwa.xyz | Medium |
| Performance fee | **0%** | rwa.xyz | Medium |
| Ongoing gold custody fee | **None. There is no gold to store.** This is the product's stated selling point: "eliminating traditional storage fees" | Launch coverage | High |
| Libeara platform fee | **Not disclosed** | | High (undisclosed) |
| Theo wrapper fee on thGOLD | **Not disclosed** | | High (undisclosed) |
| Fund admin / trustee / audit costs | **Not disclosed** | | High (undisclosed) |

**Where the revenue comes from.** Unusually, and importantly for Aurumix: **the investor is not the source of revenue. The borrower is.** Mustafa pays loan interest. That interest funds both the yield to holders and (partly) the 1% management fee. This is the cleanest example in the entire landscape of a gold product funded by an **external operating counterparty** rather than by recycling fees back from the people it is paying.

### The arithmetic, and it does not close

The brief requires that any advertised yield be tested against disclosed revenue. Here is the test, and it produces a real problem.

**Disclosed gross rate.** Aaron Gwak, comparing Libeara's cost of gold financing with the Korean market, said: **"we borrow gold at 2.5% [annually]"** while traditional Korean merchants "borrow gold at 1%" per month, i.e. 12% annualised ([Fortune, 27 Jan 2026](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)).

**Disclosed net yield.** Theo's Ari Pingle: thGOLD holders "can expect to receive an annual yield of **2.3%**" net of fees (same source). Theo's own article says "**approximately 2%**" ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you)).

**The gap: 2.5% gross minus 2.3% net = 0.20 percentage points.**

That 0.20pp is supposed to cover:
- FundBridge's **1.00% management fee** (which alone is five times the entire available spread)
- Libeara's platform fee
- Theo's wrapper fee
- Perpetual (Asia) trustee fees
- Vistra administration
- KPMG audit
- Funding cost of the 20% first-loss buffer

**It cannot.** The 1% management fee alone consumes 1.00pp of a 2.50pp gross spread, which mathematically caps the maximum net yield at **1.5%** before any other cost, and lower once platform, wrapper, trustee, admin and audit fees are paid. A 2.3% net yield is arithmetically impossible from a 2.5% gross loan rate.

**Possible reconciliations, none of them confirmed:**
1. The 2.5% figure was Gwak describing a market rate or a different transaction, not MG999's actual coupon to Mustafa.
2. The actual coupon to Mustafa is materially higher than 2.5%: plausibly 4% to 6% to leave room for the stack.
3. Theo's 2.3% is subsidised, promotional, or blends in the delta-neutral gold-futures basis strategy Theo separately describes ([PR Newswire, 27 Jan 2026](https://www.prnewswire.com/news-releases/theo-brings-yield-bearing-gold-onchain-via-regulated-tokenized-fund-structure-302671228.html)), in which case it is **not purely lending yield** and the "secured gold lending" story is incomplete.
4. The 1% management fee is waived during the ramp.

**On the disclosed numbers, the yield promise does not reconcile.** This is the same failure mode the brief documents for Kinesis (advertised yield ~20x actual disclosed revenue) and PGOLD, but arriving by a different route: not recycled fees, but an undisclosed gross rate that makes the arithmetic uncheckable. **Confidence: High** that the published figures are mutually inconsistent. **Confidence: Low** on which reconciliation is correct, because the actual loan coupon is **Not disclosed**.

Note also the honest 2025 backtest figure buried in Theo's launch: "the strategy produced an average annual return of about **8.27% during 2025**". That is a **gold-price-inclusive** total return, not a lending yield, and mixing the two in the same paragraph as "2.3% yield" is exactly the kind of blur the brief warns about.

## 8. Token architecture

- **Standard: ERC-20** on Ethereum ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). Also deployed to Arbitrum (zero supply) and Avalanche C-Chain.
- **Contract addresses: Not disclosed.** rwa.xyz gates them behind a login; neither Libeara, FundBridge nor Theo publishes them. For a product marketed on institutional transparency, **the inability to independently verify the token on-chain is a substantive gap.**
- **Permissioning: almost certainly whitelisted, but not documented.** With **2 holders**, **1 active address in 30 days** and **0 transfers in a month**, and an accredited-investor-only mandate, transfer control must exist. But whether it is enforced via ERC-3643, a transfer-agent allowlist on a plain ERC-20, or purely off-chain at the subscription gate is **Not disclosed**. No token-standard documentation was published.
- **Admin keys, minting authority, upgradeability: Not disclosed.**
- **Smart contract audit: Not found.**

**The wrapper split, and it is the interesting bit.** MG999 the fund unit is locked to accredited investors. **thGOLD**, issued by **Theo** (a separate firm founded by ex-Optiver and ex-IMC traders), is a wrapper that takes MG999 exposure onto **Hyperliquid, Uniswap, Morpho and Pendle** ([The Block](https://www.theblock.co/post/385152/theo-launches-yield-bearing-tokenized-gold-built-work-defi)). Theo's own disclaimer still restricts access to "Accredited Investors and Institutional Investors", so this is not a retail bypass on paper. But the structural pattern is clear: **a permissioned regulated fund unit at the base, a freely-composable DeFi token on top, and a legal relationship between the two that is nowhere documented.** Is a thGOLD holder a beneficial owner of MG999 units, a creditor of Theo, or a derivative counterparty? **Not disclosed.** Theo goes further still with **thUSD**, a "gold-backed stablecoin" backed by thGOLD, targeting $1bn of deposits ([PR Newswire, 17 Apr 2026](https://www.prnewswire.com/news-releases/theos-gold-backed-stablecoin-held-steady-through-global-disruption-now-targets-1b-in-deposits-302745928.html)).

That is **three layers of wrapper on a $12.4M loan to a jeweller**: MG999 unit, thGOLD, thUSD. Each layer adds a counterparty and a fee, and only the bottom one is inside a MAS-licensed perimeter.

## 9. Liquidity and market

Reporting as one data point, per the wave-1 addendum, not re-arguing the settled conclusion.

**MG999 has no market at all.** AUM **$12.44M**, supply **95,983.65** tokens, NAV **$130.00**, **2 holders**, **1 active address** in 30 days, **0 transfers** in a month ([rwa.xyz](https://app.rwa.xyz/assets/MG999)). There is no secondary market, no exchange listing, no on-chain liquidity pool and therefore no price against spot to measure. NAV is struck by the administrator, not discovered by a market. The 30-day figure is **down 7.08%**, tracking the gold price move rather than any flow.

thGOLD is the layer intended to create tradability, and CoinGecko reports **THGOLD is not currently tradeable on any exchange it lists**. So as of today, neither layer trades.

This is the **furthest extreme** of the illiquidity end of the premium spectrum: a product with fewer holders than a family WhatsApp group. It adds nothing to the premium question except a final confirmation that accumulating assets and having a market are unrelated problems.

## 10. Distribution

**No savings plan, no recurring purchase, no referral scheme, no affiliate programme, no agent network.** Confidence: **High**, nothing of the kind appears anywhere.

Distribution is entirely **B2B institutional**:
- **Libeara's CMS dealing licence** is itself the distribution strategy. The March 2026 licence was explicitly framed as letting Libeara move "from a technology platform provider to a regulated financial institution", enabling it to distribute tokenised products directly rather than only build rails for others.
- **Theo** provides the DeFi distribution layer (Hyperliquid, Uniswap, Morpho, Pendle).
- Geography: Singapore-centred, with stated ambitions in **Hong Kong** and **Korea** (the Kyobo Life and Kaia investments in the June 2026 round are explicitly Korea-facing).
- Segment: accredited and institutional only. **Retail is structurally excluded**, which is the mirror image of Aurumix.

The interesting distribution insight is the **borrower** side, not the investor side. Libeara's growth constraint is not raising money; it is **finding creditworthy gold retailers to lend to**. Gwak's comparison of a 2.5% offered rate against Korean jewellers paying 12% annualised is a pitch to *borrowers*, and it explains the Korean investor base in the funding round. **This is a two-sided marketplace disguised as a fund.**

## 11. Recent developments

Dated, reverse chronological.

- **23 June 2026.** Libeara closes a **$14M strategic funding round led by GSR**, with **Openspace Capital, Kyobo Life Insurance Group, AlloyX, Kaia Investment Partners, Simsan Ventures and Monk's Hill Ventures** ([SC Ventures](https://scventures.io/libeara-raises-14m-in-gsr-led-strategic-round-to-scale-infrastructure-for-regulated-digital-assets), [Ledger Insights](https://www.ledgerinsights.com/stanchart-backed-libeara-raises-14m-from-gsr-kyobo-life-others-for-tokenization/)). Notably, **Standard Chartered / SC Ventures is not listed as participating**, and no post-round shareholding is disclosed. Platform cumulative total: **over $1bn of regulated assets tokenised**.
- **~5 May 2026.** SC Ventures makes a **strategic investment into GSR** at a reported ~$1bn valuation ([BanklessTimes](https://www.banklesstimes.com/articles/2026/05/05/standard-chartereds-sc-ventures-backs-crypto-market-maker-gsr/)). GSR then leads Libeara's round the following month. Two SC Ventures portfolio companies investing in each other is worth flagging: it makes the "GSR-led round" a weaker external validation signal than it appears.
- **22 April 2026.** MAS FID record for Libeara (Singapore) Pte. Ltd. last updated; licence active.
- **17 April 2026.** Theo announces **thUSD**, a gold-backed yield-bearing stablecoin backed by thGOLD. $100M Genesis programme sold out in 24 hours; targets $300M TVL by end-April and **$1bn by year-end**. Chains: Arbitrum, Ethereum, Stable, via LayerZero ([PR Newswire](https://www.prnewswire.com/news-releases/theos-gold-backed-stablecoin-held-steady-through-global-disruption-now-targets-1b-in-deposits-302745928.html)). Yield described as coming from **two** sources: physical gold lending **and gold futures basis (delta-neutral)**. The second source is not part of the MG999 lending story.
- **8 April 2026.** GSR-led round first announced ([Blockhead](https://www.blockhead.co/2026/04/08/gsr-leads-funding-round-for-tokenisation-platform-libeara/)); closed 23 June.
- **13 March 2026.** **MAS grants Libeara (Singapore) Pte. Ltd. its full CMS licence** for dealing in CIS and securities ([Blockhead](https://www.blockhead.co/2026/03/13/libeara-secures-singapore-dealer-licence-clearing-path-to-distribute-tokenised-assets-directly/)). Standard Chartered's Margaret Harwood-Jones calls it "proof of the robustness of Libeara's framework." Hong Kong flagged as next target.
- **March 2026.** Gold price volatility event. Theo claims thUSD held its peg while gold ETFs drew down.
- **~27 January 2026.** **Theo launches thGOLD**, wrapping MG999 for DeFi, advertising **~2.0–2.3% net yield** and disclosing the **20% first-loss buffer** ([theo.xyz](https://theo.xyz/articles/introducing-thgold-gold-that-works-for-you), [Fortune](https://fortune.com/2026/01/27/libeara-theo-falcon-finance-yield-tokenized-gold/)).
- **11 December 2025.** **MG999 launch announced.** FundBridge Capital as manager, Libeara as tokenisation platform, **Mustafa Gold as inaugural borrower**. Initial fund size **$15M** ([Caproasia](https://www.caproasia.com/2025/12/11/standard-chartered-bank-sc-ventures-incubated-singapore-tokenisation-platform-libeara-announced-digital-infrastructure-launch-of-tokenized-secured-private-credit-gold-fund-mg-999-on-chain-gold-fu/), [Blockhead, 9 Dec 2025](https://www.blockhead.co/2025/12/09/singapores-fundbridge-launches-tokenized-gold-linked-private-credit-fund/)).
- **3 December 2025.** Libeara and FundBridge launch **ULTRA**, a tokenised US Treasury strategy with **Wellington Management**, for which **Standard Chartered provides custody**. Relevant because it is the one product where SC's role is operational rather than reputational.
- **24 September 2025.** MoU with EQBR Holdings on tokenised RWAs.
- **21 August 2025.** Libeara announces **MAS in-principle approval** (received July 2025) ([Libeara](https://libeara.com/libeara-receives-in-principle-approval-for-capital-markets-services-license-from-monetary-authority-of-singapore/)).
- **7 July 2025.** **Mustafa Gold Pte. Ltd. incorporated**, UEN 202529232Z, $0 paid-up capital.

**No enforcement action, no incident, no security breach and no regulatory criticism** was found against Libeara, FundBridge, Mustafa Gold or Theo in the period. AUM shrinking from a $15M target to $12.44M is the only negative signal, and that is partly gold-price movement.

## 12. Relevance to Aurumix

### The pedigree question, answered directly

**The Standard Chartered link is substantive on the licensing and platform side, and reputational on the product side.** Both halves matter.

**Substantive:**
- Libeara (Singapore) Pte. Ltd. **really does hold a live MAS CMS licence**, verified on the register, with a named CEO in the MAS record. Of the eleven protocols now profiled, this is one of the very few where a name search against a regulator produces a real, current, correctly-scoped authorisation. Comtech's Dubai licences display as expired and cover the wrong activities; ORO is unlicensed everywhere; VNX holds registrations, not licences.
- FundBridge's fund-management CMS is separately real.
- On the **ULTRA** treasury product, Standard Chartered provides actual **custody**. That is a bank doing bank work.

**Reputational:**
- **Standard Chartered is nowhere in the MG999 stack.** It is not the issuer, not the manager, not the custodian, not the trustee, not the auditor and not the borrower's guarantor. It is a shareholder in a portfolio company that provides tokenisation software. The custodian is Perpetual (Asia); the auditor is KPMG; the administrator is Vistra. Every phrase like "Standard Chartered-backed gold fund" in the coverage is describing a **venture equity relationship two removes from the product**.
- SC Ventures did **not** participate in the June 2026 round, and **no shareholding percentage has ever been disclosed**. Whether SC still holds a majority, a minority or a token stake is **Not disclosed**, and after a $14M external round it has necessarily been diluted.
- The GSR-led round is weaker validation than it looks, because SC Ventures had invested in GSR a month earlier.

**Now the payload finding, and it is the answer to the question this profile was commissioned to settle:**

> **The bank-affiliated platform produced a better licence than the crypto-natives. It did not produce better paperwork.**

Libeara has a real MAS licence and no public offering document, no published contract address, no smart-contract audit, no disclosed loan coupon, no disclosed LTV, no disclosed default waterfall, no disclosed insurance and no evidence for its headline 20% first-loss buffer beyond a sentence in a partner's blog post. **VNX Commodities AG, a tiny Liechtenstein operator holding 13 kg of gold, publishes more legally operative detail about what a holder owns than a Standard Chartered-incubated platform does.**

The reason is structural, not cultural, and it is the transferable lesson: **the accredited-investor exemption is what removes the disclosure obligation.** By selling only to accredited and institutional investors, MG999 avoids prospectus registration, and with it the requirement to publish anything. The licence and the opacity are not in tension. **The licence is what buys the opacity.** An institutional wrapper is a disclosure *reduction* technology, not a disclosure *enhancement* technology, and any Aurumix positioning that assumes "regulated therefore transparent" has the causation backwards.

### Against the nine design questions

**Q1, custody fee.** Speaks to it from an unusual angle and is worth taking seriously. MG999 charges **no gold custody fee because it holds no gold**, and it is explicit that removing "vaulting, insurance and storage" cost is the product's raison d'être. It replaces the storage cost with **credit risk on a jeweller**. That is a real trade, honestly stated, and it is a live third option beyond the brief's cash-versus-grams framing: *don't hold the metal at all*. It is **not available to Aurumix**, whose whole promise is that 100% of every dollar buys physical LBMA gold and whose token price is defined as vault grams ÷ tokens. Aurumix has a vault, so it has a storage cost, so it must be recovered in cash. **MG999 confirms the cash-recovery conclusion by showing that the only way to avoid the cost entirely is to abandon physical backing.**

**Q2, dividend funding. This is the section that earns the profile, and it is a genuine partial answer to the client's biggest open problem.**

MG999 is the **first structure in this landscape where the yield is paid by an external commercial counterparty rather than recycled from investor fees**. Mustafa Gold pays interest because it gets working capital cheaper than a bank would lend it. That is real economic value creation, not circular flow. It is exactly the category of thing Aurumix needs for its ICS Dividend.

Three things to take from it and one to be careful about.

*Take:* **The credit-enhancement pattern.** A **20% first-loss buffer held by the sponsor** is a straightforwardly good idea and Aurumix should consider an analogue. If Aurumix ever deploys gold or cash into any yield-generating arrangement, a first-loss tranche funded by the operator, sitting ahead of holders, converts "trust us" into a quantified subordination. It is cheap to describe and powerful in a disclosure document. **Do it better than Libeara did: fund it, segregate it, size it against the book, and publish the evidence.** Their version exists only as a sentence.

*Take:* **The two-sided-marketplace insight.** Libeara's real scarce resource is **creditworthy borrowers**, not investors. Gwak's 2.5%-versus-12% comparison is a borrower pitch. If Aurumix ever wants external yield, the binding constraint will be the same: finding counterparties who will pay for gold liquidity and who are good for it. Aurumix's India and UAE markets are full of jewellers who currently borrow at Muthoot-style rates. **That is a more accessible yield source for a Dubai/India operator than institutional gold leasing, and it is on Aurumix's doorstep.**

*Take:* **The arithmetic discipline.** As shown in §7, the published 2.5% gross against 2.3% net **does not close** once a 1% management fee is applied. This is now the **third** protocol (after Kinesis and PGOLD) where the advertised yield cannot be reconciled with disclosed revenue. The pattern is not a crypto-native failing; a Standard Chartered-incubated, MAS-licensed, KPMG-audited structure does it too. **Aurumix must publish its gross source rate, its full fee stack and its net-to-holder number in the same table, or it will be indistinguishable from these.**

*Careful about:* **This is a partial answer to the Streamex/Monetary Metals question, not a replacement for it.** MG999 is documented *worse* than the Streamex lease the brief flags as the highest-value lead. The brief's live stress test still applies with force here. The AgaBullion default (26 January 2026) showed that when a gold lessee fails, "title remains with the lessor" means litigating abroad. **MG999's collateral is retail jewellery inventory on a shop floor in Singapore**, which is worse collateral than vaulted bullion: it depletes, it is fungible, it is hard to perfect a security interest over, and it is being sold to customers by the borrower in the ordinary course. **How MG999 unit holders rank on a Mustafa default is not disclosed anywhere.** Do not treat this as the documented precedent the client needs. **Chase Streamex.**

**Q3, token standard.** MG999 is a plain **ERC-20** with, presumably, off-chain or allowlist transfer control that is nowhere documented. But the structure is a live demonstration of a pattern directly relevant to Aurumix: **a restricted regulated unit at the base, and a freely-composable wrapper on top issued by a different firm** (Theo's thGOLD, then thUSD). That is architecturally similar to the ERC-3643-base-plus-ERC-20-wrapper design Aurumix is leaning toward. **The warning from MG999 is that the legal relationship between the two layers must be documented, and here it is not.** Nobody can say from public sources whether a thGOLD holder owns fund units, has a claim on Theo, or holds a derivative. Aurumix will face the identical question about ICS standing, dividend entitlement and buyback rights on a wrapped token, and must answer it in writing at design time.

**Q4, regulatory route.** MG999 is Singapore, not UAE, so it does not bear on VARA or the ADGM Accepted Spot Commodity route. **It does bear on the hybrid-regulation problem, and helpfully.** Note what MAS licensed: **Libeara's dealing activity** and **FundBridge's fund management**. It did **not** approve the product. MG999 avoids product-level scrutiny by being a **restricted scheme for accredited investors**. That escape hatch is unavailable to Aurumix, which is by definition mass-retail at $20/month. **The lesson is precisely inverted: the institutional route's cost is that you cannot sell to retail, and Aurumix's entire thesis is retail.** Aurumix cannot borrow MG999's regulatory posture, only its licensing discipline.

**Q5, redemption.** **MG999 offers no physical redemption and cannot**, because there is no gold. It is the one protocol in this set with less physical redemption than Aurumix, and it is sold to institutions on that basis without apology. It is a modest defensive data point: **a Standard Chartered-incubated, MAS-licensed gold product with zero metal and zero physical redemption is being sold to accredited investors today.** Aurumix's no-physical-redemption stance is not an outlier. The difference is that Aurumix actually holds the metal, which makes its position strictly stronger than MG999's, and it should say so. Separately, MG999's claimed **daily redemption against a term loan book** is a maturity mismatch Aurumix should not copy; Aurumix's cash-buyback design should state its settlement window and its funding source honestly.

**Q6, premium.** One data point, no new argument: **$12.44M AUM, 2 holders, 0 transfers in 30 days, no exchange listing, no measurable price against spot.** The extreme illiquid end.

**Q7, proof of reserve.** **No reserve, therefore no attestation, therefore no bar list, therefore no PoR feed.** And the "audited" trap appears in its most complete form: MG999 can truthfully say it is **KPMG-audited** (fund financials) and **Standard Chartered-backed** (venture equity), and a reader will hear "a Big Four firm and a global bank have verified the gold." **There is no gold.** This is the strongest example in the landscape of institutional-sounding assurance language attaching to nothing in the vault, and it is Aurumix's clearest opportunity: **a genuine, frequent, published reserve attestation with a bar list is a differentiator even against bank-affiliated competitors.**

**Q8, distribution.** **None of the mechanisms Aurumix uses.** No SIP, no recurring purchase, no referral, no affiliate, no agent tiers. Purely B2B institutional plus a DeFi wrapper. Confirms the running finding that recurring-contribution retail distribution is genuinely unoccupied territory in tokenised gold.

**Q9, wind-down.** **No wind-down plan published.** Given the structure, the questions are sharper than for a vaulted product: on a FundBridge failure, who administers the loan book? On a Libeara failure, who can mint, burn and transfer the tokens, and does the register survive? On a Mustafa default, who enforces the charge and in what order do unit holders rank? **None of this is documented.** Eleven protocols in, **still no protocol in this landscape has published a wind-down plan**, including the bank-affiliated one with a CMS licence. The cheap-differentiation conclusion holds.

### Contradictions with the brief

**None.** Nothing here contradicts an established finding. Two extensions worth recording:

1. The brief's Kinesis finding ("any protocol advertising a yield: do the arithmetic") now applies to a **licensed, bank-incubated** issuer, not just crypto-natives. The failure to reconcile advertised yield with disclosed revenue is **not correlated with regulatory status**.
2. The brief's rule that **"audited" usually means smart-contract-audited, not reserve-attested** needs a third category after this profile: **fund-audited**. MG999 has a Big Four *fund* auditor, no smart-contract audit and no reserve attestation. Three different things, one word.

## 13. Open items for verification

- [ ] Obtain the MG999 **offering document / PPM / factsheet** from FundBridge Capital directly. Nothing is public. Everything in §2, §6 and §7 that reads "Not disclosed" is likely answered inside it.
- [ ] Establish the **actual interest coupon Mustafa Gold pays**. The published 2.5% gross against 2.3% net cannot support a 1% management fee. Resolve which figure is wrong.
- [ ] Establish the **loan-to-value ratio** applied to pledged jewellery inventory and how the inventory is valued and revalued monthly.
- [ ] Obtain documentary evidence of the **20% first-loss buffer**: who the sponsor is, cash or gold, segregated or contractual, sized against what, and any executed document. Currently sourced only to a Theo blog post.
- [ ] Determine the **legal form of the MG999 vehicle** (Singapore VCC? sub-fund? Cayman?) and its registration number, via ACRA or the MAS VCC register.
- [ ] Determine whether **legal title to the pledged gold passes to the fund** or remains with Mustafa under a security interest, and whether that interest is **registered and perfected**.
- [ ] Obtain the **default waterfall**: enforcement trigger, who enforces, ranking of unit holders, and forum.
- [ ] Establish whether the pledged inventory is **insured** and who is loss payee. Compare against the 110% jeweller's block insurance reportedly in the Streamex/Monetary Metals lease.
- [ ] Obtain a **parent guarantee, keepwell or comfort letter** from Mohamed Mustafa & Samsuddin Co. Pte Ltd (UEN 198900680Z) in favour of the fund. The borrower of record, Mustafa Gold Pte. Ltd. (UEN 202529232Z), has **$0 paid-up capital** and was incorporated five months before launch.
- [ ] Obtain the **MG999 contract addresses** on Ethereum and Avalanche and verify supply, transfer controls and admin roles on-chain. rwa.xyz gates them; the issuer publishes none.
- [ ] Determine the **token standard and permissioning mechanism**: ERC-3643, allowlisted ERC-20, or off-chain-only control. Who holds mint, burn, freeze and upgrade authority.
- [ ] Obtain any **smart-contract audit** of the Libeara token contracts. None found.
- [ ] Establish the **legal relationship between a thGOLD holder and an MG999 unit**: beneficial ownership, creditor claim on Theo, or derivative. And the same question again for **thUSD**, which is a wrapper on a wrapper.
- [ ] Establish **Standard Chartered's / SC Ventures' actual shareholding percentage in Libeara** post the June 2026 $14M round, and whether Libeara is consolidated in Standard Chartered plc's accounts. Never disclosed.
- [ ] Confirm whether MG999 truly offers **daily redemption**, and obtain the gating, notice, lock-up and suspension provisions. Daily liquidity against a term loan book is a maturity mismatch that has never been tested at 2 holders.
- [ ] Obtain the **MAS CMS licence number** for Libeara (Singapore) Pte. Ltd. The FID record confirms the licence but displays no numeric ID.
- [ ] Check whether Libeara has since applied for or obtained any **Hong Kong SFC** licence, flagged as the next target in March 2026.
