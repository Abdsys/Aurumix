### 4.3 Kinesis Money (KAU)

| Field | Detail |
|---|---|
| Issuer | Kinesis Cayman, a Cayman Islands exempted company. |
| Licence covering the token | None. CIMA VASP approval is conditional only. |
| Assets under management | ~US$310.2M, 2.386M KAU, 28 July 2026. |
| Backing | 1 KAU = 1 g allocated gold, held by Kinesis as bailee. |
| Custody fee charged to holders | 0%. |
| Yield paid to holders | Holder's Yield, 15% of the Master Fee Pool. Advertised 2.05%. |
| Redemption | Physical, 1,000 KAU per 1 kg bar, 0.45% plus US$100. |
| Token standard | Kinesis Blockchain Network, permissioned. ERC-20 wrapper on Ethereum. |
| Reserve verification | Bureau Veritas / Inspectorate, twice yearly. No bar list. |

#### What it is

Kinesis wraps a 1-gram allocated-gold token in a full monetary system: an exchange, a debit card, payroll, and a fee-sharing yield paid to holders, minters and referrers. Live since 2018, it is the closest running analogue to the ICS Dividend, with eight years of published payouts to check the arithmetic against.

#### Legal structure and regulatory standing

- **Title.** Clause 5.1.1 states that "legal and beneficial title in the Allocated Bullion backing the Kinesis Currency will remain with the Kinesis Currency holder."
- **Bailment.** Clause 4.1.2 has Kinesis storing bullion "as bailee on behalf of all holders", each with "an undivided interest in the total pool".
- **Cayman.** Kinesis's own Q4 2025 / Q1 2026 update says only that it "has received conditional approval" for a VASP licence from CIMA. A search of CIMA's register returns no entity of that name.
- **Australia.** AUSTRAC registrations DCE100865184-001 and IND100865184-001 are anti-money-laundering registrations, not financial-services licences.

#### Custody, fees and redemption

- **Vaults.** Brink's and Loomis, across London, New York, Zurich, Dubai, Singapore and Australia.
- **Attestation.** Bureau Veritas / Inspectorate International, twice yearly, in absolute grams. The 17 October 2025 count of 2,393,328.835 g reconciles closely against KAU circulating.
- **Gaps.** No bar list, no live proof-of-reserve feed, a six-month unverified window between counts, and no published smart-contract audit.
- **Fees.** Storage is free. Minting costs 0.45%, execution 0.22%, and sending KAU anywhere costs 0.45%. That transfer fee funds the yield.
- **Redemption.** Clause 8.1.1.1 permits redemption into allocated bullion at any time, at 1,000 KAU per 1 kg bar under 8.1.1.10, each request handled "on a case by case" basis.

> **Relevance to Aurumix.** Kinesis paid US$26,326 in Holder's Yield on gold in June 2026 against ~US$310M of assets, roughly 0.10% annualised against an advertised 2.05%, a gap of about 20x. An eight-year-old transactional platform pays a tenth of a percent, so a low-velocity SIP cannot fund 5% from recycled fees.

- **Split the instrument.** Kinesis kept KAU as the commodity and sold KVT separately as a capped 300,000-unit revenue share under an Offering Memorandum.
- **The wrapper strips the rights.** KMS Labs S.A. terms state ERC-20 holders "have no legal, equitable or beneficial right, title or interest in or to the Reserves", and receive no yield. Marketing does not draw that distinction, and if Aurumix wraps a permissioned base token it must.
- **The 0.45% transfer fee funds a payments product,** not a savings product.

### 4.4 Streamex (GLDY)

| Field | Detail |
|---|---|
| Issuer | Streamex Ltd., a Cayman Islands SPV formed February 2026. |
| Licence covering the token | None. Sold under Rule 506(c) of Regulation D. |
| Assets under management | ~US$12.84M, July 2026. |
| Backing | 1 GLDY = 1 fine troy ounce held by the SPV. May be unallocated. |
| Custody fee charged to holders | Not disclosed. Borne inside the SPV. |
| Yield paid to holders | "Up to 4%" advertised, 3.50% APY July 2026. Paid as scrip. |
| Redemption | 90 days' prior written notice, subject to "certain limitations". |
| Token standard | ERC-20 on Base, CCIP to Solana. Whitelisted, accredited only. |
| Reserve verification | EisnerAmper LLP examination, 31 March 2026. No bar list. |

#### What it is

GLDY is a gold-backed security token issued by a Cayman SPV under a Nasdaq-listed parent, paying yield sourced from third-party gold leasing through Monetary Metals.

#### Legal structure and regulatory standing

- **Holders own equity.** A GLDY holder owns "a non-voting digital share of Streamex Ltd.", a share in a Cayman company rather than title to metal or a trust interest.
- **The filed agreement is genuine.** Form 8-K of 8 September 2025, accession 0001641172-25-026853, Exhibit 10.1, the executed Tokenized Yield Partnership Agreement with Monetary Metals & Co.
- **It does not cover the lease.** Section 3.03 defers lease documentation to be "developed and mutually agreed" later, under New York law per Section 14.13. The exhibit omits security interest, title retention, risk-of-loss allocation and lessee default provisions.
- **The parent concedes the exposure.** The 10-K states holders "may face delays, partial recovery, or total loss".

#### Custody, fees and redemption

- **The custodian is unnamed,** described only as "an LBMA-accredited custodian". No vault, no city, gold may be unallocated, no bar list.
- **The 10-K concedes the link may be absent:** "there may be no current mechanism to link GLDY balances to physical gold held as individual bullion bars."
- **The attestation is real.** EisnerAmper examined management's assertion as of 31 March 2026: 3,064.674268 GLDY against 3,064.915910 fine troy ounces.
- **Two qualifications.** The parent held 98.5% of tokens at that date, and EisnerAmper became the parent's statutory auditor on 8 July 2026.
- **The yield is externally funded.** Article I defines a "Passing Lease" as one that "generates a net yield of at least three percent (3%) per annum after origination fees", and Section 3.01(b) lets Streamex reject any lease "in its absolute and sole discretion".

> **Relevance to Aurumix.** Three clauses are worth copying almost verbatim: the 3% net-after-origination-fees floor, the absolute discretion to reject a lease, and the insurance schedule. Schedule 1 requires a lessee-funded jeweller's block policy at 110% of lease value, plus a Monetary Metals-funded Lloyd's DIC/DIL layer at 110% covering "both mysterious disappearance and 'bad acts' by the lessee's management and owners".

- **The loss payee wording fails.** Both layers name Monetary Metals as loss payee "wherever possible", best efforts rather than a covenant. Neither names the SPV or the holders.
- **There is a live test.** The AgaBullion lessee defaulted on 26 January 2026 with Turkish seizure. Whether the Lloyd's layer paid has not been published.
- **Mind the buyer.** Streamex sells this at a $200,000 accredited minimum. Aurumix would sell comparable risk to a saver contributing $20 a month.

### 4.5 Comtech Gold (CGO)

| Field | Detail |
|---|---|
| Issuer | ComTech FZCO, Dubai Airport Free Zone. Parent Trade Fintech Ltd, DIFC. |
| Licence covering the token | None. Absent from the VARA, DFSA and ADGM FSRA registers. |
| Assets under management | ~US$5.04M, 28 July 2026. Last published reserve 111 kg. |
| Backing | 1 CGO = 1 g of 999.9 gold in 1 kg bars. Transguard, UAE. |
| Custody fee charged to holders | 0%, free for the first 24 months. |
| Yield paid to holders | None. |
| Redemption | Contractual minimum 1 kg (clause 8.1) at 0.50% plus making charges. |
| Token standard | XRC-20 on XDC. Not permissioned. |
| Reserve verification | Self-issued ComTech FZCO letters. Last dated 21 March 2025. |

#### What it is

Comtech Gold sells one gram of Dubai-vaulted gold per token on XDC, running a listed token and an app-based AED savings product off a single reserve, and at roughly $5.04M it has gone quiet.

#### Legal structure and regulatory standing

- **The issuing licence is DAFZA.** Licence 05069, issued to ComTech FZCO on 21 February 2022 for "gold and other precious metals trading". It is not a DMCC licence.
- **The DMCC licence is unrelated.** ComTech FZCO (DMCC) licence DMCC-889799 covers IT consultancy, network consultancy and software house activity only. Neither licence authorises public token issuance.
- **Both display as expired.** Comtech's own registration page shows DAFZA expiring 20 February 2024 and DMCC 25 June 2024.
- **The marketing says otherwise.** The FAQ states ComTech Gold "is regulated by Dubai Airport Free Zone Authority (DAFZA) and endorsed by local UAE government body DMCC". A free zone authority is a registrar.

#### Custody, fees and redemption

- **Transguard holds the metal,** though the storage clause permits holding "in the UAE or elsewhere" through affiliates "anywhere in the world".
- **Proof of reserve is self-signed.** Letters on ComTech FZCO letterhead, signed "For ComTech FZCO", no independent examiner named, no bar list.
- **The last letter is 21 March 2025.** It reports 111 kg, down from 144 kg after 62 kg of withdrawals, a 23% net decline left unexplained. Nothing published since.
- **Custody is free and the spread pays for it.** The site lists custody and insurance at "Nil", while the app returns ~1.0125% buy commission, ~0.9950% sell, and a round-trip spread near 1.8%. Nothing is deducted in grams.
- **The binding redemption minimum is 1 kg,** roughly $129,000 under clause 8.1. The advertised 10 g route is a discretionary retail service through partner jewellers.

> **Relevance to Aurumix.** Comtech issues a public gold token from Dubai on a bullion-trading licence and an IT consultancy licence, appears on no regulator's register, and tells retail customers in its FAQ that it is regulated by DAFZA. No public document establishes a Dubai gold-token route around VARA, only an authorisation nobody has obtained.

- **The fee mechanism does transfer.** Zero custody fee recovered through ~1% commission plus a ~1.8% spread, nothing deducted in grams, supports avoiding gram-denominated fees.
- **It only works if people transact.** A monthly SIP collects that margin once on the way in, then carries storage cost indefinitely. Comtech's 24-month carve-out shows transaction margin alone does not close the gap.
- **The proof-of-reserve bar is cheap to clear:** an independent attestation on a fixed cadence, a real bar list, and a clean separation between contract audit and reserve attestation.
