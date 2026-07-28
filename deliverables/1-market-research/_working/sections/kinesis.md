# Kinesis Money (KAU)

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | KAU (gold, 1 KAU = 1 gram). Sister token KAG (silver, 1 KAG = 1 ozt). Equity-like token KVT | **High** |
| Issuer (marketing) | "Kinesis" / Kinesis Money | **High** |
| Issuer (registry) | **Kinesis Cayman** (Cayman Islands exempted company, C/O Stuarts Corporate Services, 36A Dr Roy's Drive, Grand Cayman KY1-1104). Company number **not disclosed** on any public register we could reach | **Medium** |
| Other entities in the stack | **UAB Kinesis Money Lithuania** (code 305992161, Vilnius); **Kinesis Global Pty Ltd** (ACN 656 201 660, Brisbane); **Kinesis Money Panama S.A.** (155727241); **KMS Labs S.A.** (Panama, 155772003, issues the ERC-20); **Allocated Bullion Exchange / ABX** (ACN 149 681 489, Brisbane); historically **Kinesis AG** (Vaduz, Liechtenstein) | **High** ([Terms of Use](https://kinesis.money/about-us/documents/terms-of-use/)) |
| Domicile | Cayman Islands for the contracting entity; operations spread across Australia, Lithuania, Panama, Liechtenstein | **High** |
| Backing claim | 1 KAU = 1 gram allocated physical gold, held by Kinesis **as bailee**, with legal and beneficial title in the holder | **High** (Terms of Use cl. 5.1.1, 7.1.1) |
| Chains | Kinesis Blockchain Network (a Stellar fork). Secondary **ERC-20 wrapper** on Ethereum issued by KMS Labs S.A. | **High** |
| Contract address | ERC-20 KAU `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52` | **Medium** (Etherscan blocked our fetch; address from KMS Labs/search) |
| Supply | 2.386 million KAU circulating (= 2.386 tonnes of gold) | **Medium** ([CoinGecko](https://www.coingecko.com/en/coins/kinesis-gold), 28 Jul 2026) |
| Market cap / TVL | ~$310.2M market cap; $519.1M FDV | **Medium** (CoinGecko) |
| Regulatory status | Cayman **CIMA VASP: conditional approval only, not granted**. Australia: AUSTRAC DCE100865184-001 + IND100865184-001. Lithuania: FNTT-era registration; Bank of Lithuania lists it only as an **e-money distributor**, not a CASP | **High** for the conditional-approval claim; **Medium** on register confirmation |
| Subscription fee | Mint trade execution **0.45%**; mint deposit from platform $25, external $0 | **High** ([fees page](https://kinesis.money/fees/)) |
| **Ongoing custody fee** | **0% (zero). Explicitly "0% fee" for both KAU and KAG storage** | **High** (fees page) |
| Redemption fee | Physical: **0.45% + $100 + delivery**, case-by-case at Kinesis's discretion | **High** |
| Advertised yield | Holder's Yield = **15% of the Master Fee Pool**. Realised aggregated 12-month yield **2.05%** gold, **0.07%** silver | **High** |
| Named officers | **Thomas Richard Archer Coughlin** (CEO/founder; manager of record of UAB Kinesis Money Lithuania). Other directors **not disclosed** on reachable registers | **Medium** |

---

## 1. What it is

Kinesis is a gold-and-silver monetary system, not a bare custody receipt. KAU is a 1-gram allocated-gold token on the Kinesis Blockchain Network (a fork of Stellar), wrapped around a full retail stack: an in-house exchange, a debit/virtual card, a merchant directory, a multi-asset payroll product, and (this is the part that matters to Aurumix) a **four-way fee-sharing yield system** that pays out to holders, minters, depositors and referrers.

Kinesis has been live since 2018 and is one of the very few gold tokens that actually pays a recurring, disclosed, contractually documented distribution to ordinary token holders. It is the closest live analogue to the ICS Dividend that exists.

## 2. Legal structure

This is the strongest legal-title language of any protocol in this batch, and it is worth reading closely.

The [Terms of Use](https://kinesis.money/resources/Kinesis-Terms-and-Conditions.pdf) (48 pages) state at clause 5.1.1 and again at 7.1.1:

> "Legal and beneficial title in the Allocated Bullion backing the Kinesis Currency will remain with the Kinesis Currency holder until such time as all or part of the corresponding Kinesis Currency is transferred to another Kinesis Address."

And clause 4.1.2:

> "Kinesis will store that Bullion as bailee on behalf of all holders of that particular Kinesis Currency, whereby each holder of that Kinesis Currency has an undivided interest in the total pool of Bullion in proportion to the amount of Kinesis Currency held."

So the native-chain holder owns the gold outright, with Kinesis as **bailee** (not trustee, not debtor). Definition 1.1.4 confirms "Allocated" means "Bullion to which a natural or legal person has legal title, with Kinesis holding it on that person's behalf as bailee". Bailment is the right structure: bailed property is not the bailee's asset and does not fall into its insolvency estate. That is a genuinely strong position, materially stronger than a creditor claim.

**But there is a sharp catch, and it is the most important structural finding in this profile.** The ERC-20 wrapper is a completely different legal animal. [KMS Labs' terms](https://kmslabs.money/kms-labs-tcs/) state:

> "Holders of the Tokens acknowledge and agree that they have no legal, equitable or beneficial right, title or interest in or to the Reserves."

and

> "KMS Labs is entitled to and may retain all net returns, interest, and other income earned on Reserve assets."

**The ERC-20 KAU holder owns no gold and earns no yield.** They hold an unsecured claim against a Panamanian company (KMS Labs S.A., 155772003) redeemable only into native KAU, at KMS Labs' discretion. The moment a KAU leaves the permissioned Kinesis chain for Ethereum, both the property right and the income right evaporate. Marketing does not make this distinction; only the two separate legal documents do.

## 3. Regulatory and compliance posture

| Jurisdiction | Regulator | Status | Confidence |
|---|---|---|---|
| Cayman Islands | CIMA | **Conditional approval only** for a VASP licence, per Kinesis's own Feb 2026 update. Not a granted licence | **High** (issuer's own words) |
| Cayman Islands | CIMA public register | Searched the [CIMA regulated-entities search](https://www.cima.ky/search-entities-cima). **No entity named "Kinesis" returned.** Reference 1877923 could not be resolved to a register entry | **High** (we checked; it is a null result) |
| Australia | AUSTRAC | DCE100865184-001 (digital currency exchange) and IND100865184-001 (remittance) for Kinesis Global Pty Ltd, ACN 656 201 660 | **Medium** (issuer disclosure; AUSTRAC register not directly confirmed by us) |
| Lithuania | FNTT | Historic virtual-currency exchange/wallet registration for UAB Kinesis Money Lithuania | **Medium** |
| Lithuania | Bank of Lithuania | Register entry exists but lists the company **only** under "Persons distributing e-money of an EMI established in the Republic of Lithuania". **No MiCA CASP authorisation found** | **High** ([lb.lt entry](https://www.lb.lt/en/sfi-financial-market-participants/uab-kinesis-money-lithuania)) |
| UK | FCA | **Not authorised.** kinesis.money was voluntarily deactivated for UK users in late 2025; the [UK notice](https://kinesis.money/uk-fca-info/) says "This website and any information materials within are not intended to be accessed by UK-based persons" | **High** |
| UAE / Dubai | VARA / SCA / DMCC | **Not disclosed / not found.** Kinesis lists a Dubai office and a Dubai vault but we found no UAE licence | **High** as a null result |

Three things are material here.

**First, "registered with CIMA" is doing a lot of work in Kinesis's marketing and in third-party write-ups, and it overstates the position.** Kinesis's own [Q4 2025/Q1 2026 update](https://kinesis.money/company-news/q4-2025-q1-2026-quarterly-update/) says only: "Kinesis has received conditional approval for a Virtual Asset Service Provider (VASP) license from the Cayman Islands Monetary Authority (CIMA)." Conditional approval is not a licence. Secondary sources that assert flat "registered VASP, reference 1877923" are repeating a claim we could not verify on CIMA's own register.

**Second, the MiCA gap.** Lithuania's legacy FNTT virtual-currency registrations were superseded by MiCA CASP authorisation across 2025–2026. Kinesis's Lithuanian entity appears on the Bank of Lithuania register only as an e-money *distributor*, which is a different and much narrower permission. We found no CASP authorisation. If Kinesis is serving EU retail on the strength of a lapsed FNTT registration, that is a live exposure.

**Third, note the disclosure inside the legal document itself.** Schedule 6, clause 2.1 of the Terms of Use is remarkably candid:

> "We are seeking, or we plan to seek registrations with various regulatory bodies in countries which we may operate... If we fail to qualify for registrations under any of these authorities, we may be unable to execute on some or all aspects of our business plan as a provider of financial services."

After eight years of operation, the yield schedule still describes the regulatory position in the future tense.

## 4. Custody and proof of reserve

| Item | Position | Confidence |
|---|---|---|
| Custodian / vault operators | **Brink's** and **Loomis** (Zurich named). Kinesis markets vaults in London, New York, Zurich, Dubai, Singapore, Hong Kong, Sydney, Brisbane | **Medium** |
| Allocated? | Yes, and contractually so: bailment with legal title in the holder (cl. 5.1.1) | **High** |
| Bar list | **Not disclosed.** No published serial-number bar list found | **High** as a null result |
| Reserve attestation | **Bureau Veritas / Inspectorate International**, **twice yearly**. Most recent referenced: April 2026. The 17 Oct 2025 audit reported **2,393,328.835 g gold** and **3,729,719.331 ozt silver** | **High** ([audit page](https://kinesis.money/audit/), quarterly update) |
| PoR feed | A live [blockchain explorer](https://explorer.kinesis.money/) shows tokens in existence. This is a **supply** feed, not a reserve feed: it proves how many KAU exist, not how much gold is in the vault | **High** |
| Smart contract audit | **Not disclosed.** No published smart-contract audit found for the ERC-20 wrapper or the chain | **High** as a null result |

Kinesis is one of the better performers in this batch on reserves: a named, credible, independent commodity inspector (Bureau Veritas is the industry standard) on a fixed semi-annual cadence, with absolute gram figures published. Cross-checking the 17 Oct 2025 audit figure of 2,393,328.835 g against 2.386M KAU circulating in July 2026 gives near-exact 1:1 correspondence, which is a good sign.

The two gaps are the **absence of a bar list** and the **absence of a real-time PoR feed**. Between the semi-annual audits there is a six-month window in which the reserve position is unverified. And note the blur risk flagged in the brief: the "live record of all Kinesis currencies in existence" is an explorer, not proof of reserve, and a skimming reader will conflate them.

## 5. Issuance

Two routes. **Mint with cash:** buy KAU through the Kinesis Mint, paying a 0.45% mint execution fee, and Kinesis "will cause an equivalent amount of Bullion to be purchased on your behalf" (cl. 4.1.1). **Exchange of Physical for Digital (EPD):** deliver your own LBMA-conforming bars into a Kinesis vaulting account and mint KAU against them at 1000 KAU per kg (cl. 6.7.1). EPD is case-by-case and Kinesis "may temporarily or permanently disallow deposits for any reason or no reason" (cl. 6.4).

There is no hard supply cap: KAU is minted on demand against deposited or purchased metal, exactly the model Aurumix proposes.

## 6. Redemption

Kinesis **does** offer physical redemption, which distinguishes it from Aurumix and from PGOLD. Clause 8.1.1.1: "At any point in time, you may request for your Kinesis Currency to be redeemed into Allocated Bullion." Redemption is at 1000 KAU per 1 kg gold bar (cl. 8.1.1.10), costing **0.45% + $100 + delivery**.

The qualifications matter, though. Each redemption request "shall be managed on a case by case" basis, Kinesis "may at its ultimate discretion, prescribe reasonable minimum withdrawal quantities", and redemption is satisfied only in bars "of a Prescribed Form" (cl. 8.1.1.3, 8.1.1.5). In practice the minimum practical increment is a 1 kg bar, roughly $130,000 at current prices. So physical redemption is real and legally documented, but it is economically out of reach for the retail saver, which is precisely Aurumix's target customer. **This is the "qualified holders" pattern the brief warns about, expressed through economics rather than eligibility language.**

## 7. Fees and revenue model

| Fee line | Rate | Note |
|---|---|---|
| **Annual storage / custody** | **0%** | Explicitly stated as "0% fee" for both KAU and KAG |
| Mint (subscription) | 0.45% | Plus $25 if funding from platform balance |
| Mint spread | ~0.23% | Buy/sell spread at the Mint |
| Exchange trade execution | 0.22% | Market and limit orders alike |
| Send KAU to another Kinesis account | 0.45% | This is the core yield-funding fee |
| Send KAU to external wallet | 0.45% | |
| Physical redemption | 0.45% + $100 + delivery | |
| Fiat withdrawal | $25–$90 | Currency dependent |
| Card sign-up / monthly / transaction | $0 / $0 / 0% | Cashback 2% in gold up to $2,000/mo |
| Card purchase via third-party rails | 1.99%–5.99% | Banxa and others |

**The zero-storage-fee model is the headline.** Kinesis charges holders nothing to store gold and covers vaulting and insurance out of transaction-fee revenue plus its ABX vaulting relationship. Kinesis says it redistributes **57.5% of every fee taken** to users as yields, implying the residual ~42.5% funds operations including vaulting.

Note what this means structurally: Kinesis's revenue is a **velocity tax, not an assets tax**. It earns on movement, not on stock. A user who buys KAU and never moves it generates essentially zero revenue for Kinesis and costs it real money in vaulting. The entire design is therefore oriented toward making gold circulate: the card, the payroll product, the merchant directory, the Minter's and Depositor's yields that pay only when currency is *used*. This is a coherent and deliberate business model, and it is the opposite of the AUM-fee model most gold tokens run.

## 8. Token architecture

**Native chain.** KAU lives on the Kinesis Blockchain Network, a fork of Stellar. It is **not an ERC-20 and not ERC-3643**. It is a permissioned, KYC-gated ledger controlled by Kinesis, with root and emission accounts referenced throughout the Terms. Every address is tied to a KYC'd account. Kinesis can and does condition yield on that identity link.

**ERC-20 wrapper.** `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52`, issued by KMS Labs S.A. (Panama). Per KMS Labs' terms, holding is limited to "Eligible Users" (not resident in Restricted Jurisdictions, not Sanctioned Persons), and KMS Labs may "freeze, blacklist, or otherwise restrict access to any the Tokens" without advance notice. So even the ERC-20 is permissioned in substance, via freeze/blacklist rather than a transfer-restriction standard.

**The architectural lesson for Aurumix is precise and valuable.** Kinesis faced exactly the problem Aurumix faces (entitlements that break on anonymous transfer) and solved it by **keeping the entitlement on the permissioned ledger and stripping it from the wrapper**. The ERC-20 gets composability; it does not get the gold title or the yield. That is a legitimate design choice, but it means the two tokens are not fungible in any economic sense despite sharing a ticker, and Kinesis's marketing does not make that clear.

Upgradeability and admin keys: **not disclosed**. We found no published smart-contract audit.

## 9. Liquidity and market

| Metric | Value |
|---|---|
| Market cap | ~$310.2M |
| Circulating supply | 2.386M KAU (2.386 tonnes gold) |
| Price | $130.01 (28 Jul 2026) |
| 24h volume | **$219,282** |
| Venue concentration | Kinesis's own exchange **98.5%** (KAU/C1USD $212,814 = 96.93%; KAU/USDT $3,455 = 1.57%). Emirex KAU/USDT $1,398 = 0.64% |

Volume is **0.07% of market cap per day**. That is thin, but it is an order of magnitude better than PGOLD's sub-$20/day against $79–90M, so the brief's premium thesis is not uniformly refuted: Kinesis shows that a captive in-house exchange can generate real, if modest, turnover.

The dominant fact is that **98.5% of all KAU liquidity is on Kinesis's own venue**. There is essentially no independent external market. KAU trades at the gold price because Kinesis operates the market and the mint, not because arbitrageurs enforce it. For Aurumix, which is banking on a 3–8% exchange premium, this is the key observation: **Kinesis has ~$310M of AUM and still could not bootstrap third-party liquidity in eight years.** Venue-controlled pricing is achievable; an independent liquid market producing a reliable premium is a different and much harder problem, and Kinesis has not solved it.

## 10. Distribution

Kinesis is the one protocol in this batch with a **genuine, contractually documented referral network**, and this maps directly onto Aurumix's 3-tier agent model.

- **Recruiter Yield** (Schedule 6, cl. 8): registered recruiters get a unique tracking link and earn a percentage of the execution fees generated by every user they introduce. The worked example in the Terms uses **7.5%**. The entitlement is perpetual and runs on the referred user's *transaction fees*, not on their deposits.
- **Depositor Yield** (cl. 7): rewards large initial deposits, paid on velocity, "forever on the Kinesis coins they bought and then used."
- **Minter's Yield** (cl. 5): rewards creating currency and then circulating it.
- Retail channels: virtual/debit card, merchant directory, multi-asset payroll, Banxa card/bank on-ramps.
- Geography: global ex-UK (voluntarily withdrawn), with offices claimed in Brisbane, London, Lithuania, Dubai, USA and Istanbul.

What Kinesis does **not** have is a recurring monthly savings plan (SIP). There is no auto-debit contribution schedule. Its recurring mechanic is transactional velocity, not periodic accumulation. So Aurumix's SIP remains a genuine differentiator; the agent network does not.

## 11. Recent developments

- **Early/mid 2026 (undated formally):** Founder Thomas Coughlin announced an **"Earn Programme"** proposing to cut **Holder's Yield from 15% to 5%** of the Master Fee Pool while **raising the KVT entitlement from 20% to 30%**, with 5% added to the pool. Announced in a "Live from the Vault" video interview, **not in an amended legal document**. No effective date given. ([Ep. 280](https://www.youtube.com/watch?v=rw1ne5cASIQ))
- **9 February 2026:** Kinesis Virtual Card US Beta launched to 250 community members; public US launch targeted March 2026, full card launch later slipped to early August 2026 on a new Visa requirement.
- **2 February 2026:** [Q4 2025/Q1 2026 quarterly update](https://kinesis.money/company-news/q4-2025-q1-2026-quarterly-update/) published: **CIMA conditional VASP approval** confirmed; UK site deactivation confirmed; Bureau Veritas audit results published.
- **February 2026:** Coughlin states Kinesis is "in negotiations right now to acquire two banks."
- **Late 2025:** kinesis.money **voluntarily deactivated for UK users** as a compliance precaution; working with an FCA-licensed compliance provider on a compliant UK site.
- **17 October 2025:** Bureau Veritas / Inspectorate International audit: 2,393,328.835 g gold, 3,729,719.331 ozt silver, 1:1 backing confirmed.
- **Q4 2025:** Multi-asset payroll solution launched; Kinesis Merchant Directory went live.
- **Throughout 2025–2026:** No regulator warning-list entries, enforcement actions, litigation, security incidents, or suspensions of withdrawals or yield payments found. **Not found**, and we looked.

## 12. Relevance to Aurumix

Kinesis is the most directly instructive protocol in this batch for Aurumix, because it has been running the ICS Dividend concept for eight years and we can therefore check the arithmetic against reality rather than against a pitch deck.

**Q1, Custody fee: Kinesis is the live proof that option three works.** It charges **0% storage** and recovers vaulting cost from transaction fees. This is the cleanest available answer to Aurumix's peg problem: deducting the fee in grams breaks price = grams ÷ tokens, charging cash is friction, and Kinesis simply does neither. Critically, this is only possible because Kinesis monetises **velocity**, not **assets**. Aurumix's product is the opposite: a buy-and-hold SIP with no physical redemption, explicitly designed so gold never moves. **A zero-fee model cannot be copied onto a zero-velocity product.** If Aurumix wants zero custody fees, it must build a genuine transactional layer (the Gold Card is the obvious candidate) or accept that the cost has to come from the credit facility spread.

**Q2, Dividend funding: this is where Kinesis pays for itself as a case study, and the arithmetic is brutal.**

The mechanism, from Schedule 6 of the Terms of Use, is a Master Fee Pool per currency, funded by the 0.45% transfer/mint fees and 0.22% exchange fees, split:

| Recipient | Share of fee pool | Basis |
|---|---|---|
| **KVT holders** | **20%** | Equity-like token, 300,000 cap, sold under an Offering Memorandum |
| **Holder's Yield** | **15%** | Pro-rata daily on KAU held, KYC'd holders |
| Velocity / Depositor Yield | 10% | On initial deposit, paid on velocity |
| Minter's Yield | 5% | Minted-and-then-used |
| Recruiter Yield | 7.5% (worked example) | Of referred users' execution fees |
| **Total redistributed** | **~57.5%** | Kinesis retains ~42.5% |

Now the reality check. Kinesis publishes its actual payouts. **June 2026 Holder's Yield on gold: $26,326.32 (180.14 g)** against a **$310.2M** market cap.

- That is **0.0085% for the month**, or roughly **0.10% annualised**.
- Kinesis's own headline figure is a **2.05% aggregated 12-month yield**, and all-time gold payouts of $12.14M.
- **The two numbers are irreconcilable by a factor of about 20.** The 2.05% is almost certainly a per-holder compounding figure computed on a subset of eligible balances, not a yield on total AUM. A retail buyer reading "2.05%" will not get 2.05% on their holding, and the June payout proves it.

Work backwards. A $26,326 monthly payout at a 15% share implies a **total monthly KAU fee pool of ~$175,500**, or **~$2.1M/year**. At the 0.45% transfer fee, that implies annual fee-generating volume of **~$468M, about 1.5x AUM**. That is a real, functioning economy: Kinesis genuinely turns over its asset base one and a half times a year. It is not a fake.

**And it still only produces a tenth of a percent.**

Now apply this to Aurumix. To pay a **5% distribution on $310M** you would need **$15.5M/year to holders**. At a 15% pool share that requires a **$103M annual fee pool**, which at 0.45% requires **$23 billion of annual transaction volume, roughly 74x AUM**. Even if Aurumix routed 100% of the fee pool to holders rather than 15%, it would still need ~11x AUM in annual velocity.

**This is the single most important number in this profile: a well-run, eight-year-old, genuinely transactional gold platform turning over 1.5x its AUM per year pays its holders about 0.10%.** Aurumix's ICS Dividend promises 15–20% of operating profit with 80% concentrated on the top 10% of holders. Concentrating a small pool on few holders can make *those* headline numbers look respectable, but the total distributable amount is governed by the arithmetic above, and for a buy-and-hold SIP with no redemption and therefore near-zero velocity, the fee pool is close to nil. **Fee-recycling cannot fund a meaningful dividend. Kinesis is the strongest available evidence, and it is evidence against, not for.** If Aurumix wants a real dividend it must come from external yield (gold leasing, as ORO does) or from the credit facility spread, which is genuine external revenue and is Aurumix's most promising untapped source.

**The securities point is even sharper, and Aurumix should study it closely.** Kinesis did not pretend the fee-share was not a security. It **split the instrument in two**: KAU (the commodity, holds gold title, gets a modest 15% yield share) and **KVT (the security: 300,000 capped supply, 20% of all fees, sold to accredited investors under a formal Offering Memorandum through a private placement targeting $200M+)**. The Offering Memorandum states the Company "shall distribute an aggregate sum equal to 20% of the transaction fees" to KVT holders pro rata. That is a revenue-share security, documented and sold as one. **This is a directly transplantable structure for Aurumix: keep AURX as a clean ARVA commodity token under VARA, and if you want a profit-share, issue it as a separate, capped, privately-placed instrument to a small accredited base rather than bolting a dividend onto a mass-retail token.** That single move could dissolve the hybrid-regulation problem in Q4.

**Q3, Token standard.** Kinesis chose a **permissioned proprietary chain**, not ERC-3643. The yield attaches to the **KYC'd account**, not to the token: Schedule 6 cl. 6.2.1.1 requires that "A Holder has passed all identification and onboarding requirements." This validates Aurumix's instinct toward a permissioned base. But note the elegant refinement Kinesis found: **the entitlement follows the account, not the bearer instrument, so it survives even when tokens sit in a linked external wallet.** Kinesis explicitly confirms that KAU "held in external wallets are also applicable for the yield, as long as they are linked to your Kinesis account." Aurumix can get the same result: register ICS standing against the *account*, allow tokens to move, and simply pay entitlements only to linked, KYC'd accounts. That is cheaper than ERC-3643 and preserves optionality. The cost, as Kinesis shows, is that the ERC-20 wrapper becomes a stripped instrument with neither gold title nor yield.

**Q4, Regulatory route.** Kinesis holds **no UAE licence** despite a Dubai office and Dubai vault. Its actual regulatory anchor is an AUSTRAC registration in Australia (an AML registration, not a financial-services licence), a lapsed-looking Lithuanian registration, and **conditional-only** CIMA approval after eight years of trading. That is a thin position for a platform holding $310M of client gold. The lesson is not to imitate it: it is that **the "we're registered with CIMA" formulation is exactly the kind of claim Aurumix will be tempted to make and should not.** Note also that Kinesis withdrew from the UK entirely rather than seek FCA registration, which tells you what a serious retail regulator costs relative to this revenue model.

**Q5, Redemption.** Kinesis offers physical redemption at 0.45% + $100 + delivery, but in 1 kg bars (~$130,000). It is legally real and practically inaccessible to retail. Aurumix's no-redemption stance is more honest than this, and Aurumix should say so plainly rather than treating it purely as a weakness: "cash buyback only" is clearer to a $75/month saver than a theoretical right to a $130,000 bar.

**Q6, Premium and liquidity.** $310M AUM, $219k daily volume, **98.5% of it on Kinesis's own exchange**. Eight years of operation produced almost no independent third-party market. **Evidence against the premium thesis**, though less damning than PGOLD: Kinesis proves a captive venue can generate meaningful turnover, but not that an external market will price your token at a premium.

**Q7, Proof of reserve.** Best-in-batch on attestation (Bureau Veritas, semi-annual, absolute gram figures published, reconciles to supply). Still no bar list and no live PoR feed, and the "live record" explorer is a supply feed that a casual reader will mistake for reserve proof. **Aurumix can beat this cheaply**: publish a bar list and a monthly attestation and you are ahead of the sector leader.

**Q8, Distribution.** The Recruiter Yield (~7.5% of referred users' fees, perpetual, documented in the legal terms) is the closest live analogue to Aurumix's 3-tier agent network, and it is notable that Kinesis pays agents from **transaction fees, not from deposits**. Aurumix's commission comes out of contributions, which is a materially different and more dangerous structure (it is the shape regulators associate with distribution-heavy schemes). Kinesis has no SIP, so Aurumix's monthly savings plan remains genuinely differentiated.

**Q9, Wind-down.** No wind-down plan published. However, Kinesis has something better than a plan: the **bailment structure** means the bullion is legally the holders' property and not Kinesis's asset, so it should not fall into the insolvency estate. That is a structural protection rather than a documented procedure. **Aurumix should copy the bailment language into its own terms.** It costs nothing, it is far stronger than the creditor-claim wording most gold tokens use, and combined with a published wind-down plan it would make Aurumix the best-protected product in the sector on paper.

### Contradictions with the brief

- The brief warns that PGOLD's recycled-fee model is an anti-pattern because "the disclosed sources cannot fund the promise." **Kinesis does not contradict this; it confirms it with better data.** Kinesis's sources *do* honestly fund what it pays, because what it pays is only ~0.10%. The anti-pattern is not fee-recycling per se, it is fee-recycling combined with a headline percentage the fees cannot support. Kinesis is honest about the mechanism and misleading about the headline (2.05% vs 0.10% realised on AUM); PGOLD is misleading about both.
- **New finding not anticipated by the brief:** the yield entitlement, though written into a legal schedule, is **fully revocable at the issuer's sole discretion, including retroactively**. Schedule 6, cl. 3.1: Kinesis may "amend, suspend or terminate any Yield offering to You individually at any time whatsoever and howsoever... for any reason or without reason, including but not limited to your citizenship, residency, domicile, location **and any previously accrued Yields shall no longer be payable with immediate and irrevocable effect**." This is not theoretical: the 2026 Earn Programme proposes cutting Holder's Yield from 15% to 5% while raising the KVT (insider/investor) share from 20% to 30%. **A "documented entitlement" that can be cancelled at will, with accrued amounts clawed back, and that is being reallocated from retail holders to security holders, is a warning about how Aurumix should draft the ICS Dividend.** If Aurumix writes the same discretion into its terms, the dividend is not a value proposition; if it does not, Aurumix has created a fixed liability against a variable revenue stream.

## 13. Open items for verification

- [ ] Obtain the Kinesis Cayman company number and incorporation date from the Cayman Islands General Registry (paid search); the public Terms disclose only a registered-office address.
- [ ] Resolve CIMA reference **1877923** against CIMA directly (written enquiry). Confirm whether it is a VASP licence, a transitional registration, or merely an application reference, and whether the conditional approval has since been granted.
- [ ] Confirm on the AUSTRAC public register that DCE100865184-001 and IND100865184-001 are current for ACN 656 201 660.
- [ ] Confirm whether UAB Kinesis Money Lithuania holds any MiCA CASP authorisation, or whether its FNTT registration lapsed in the 2025–2026 transition. Establish what permission it relies on to serve EU retail today.
- [ ] Determine whether Kinesis operates in the UAE and under what licence, given the Dubai office and Dubai vault but no VARA/SCA/DMCC registration found.
- [ ] Obtain the actual Bureau Veritas audit report PDF (not the summary page) and check scope: is it a full physical count with serial numbers, or a sampling exercise?
- [ ] Establish whether the Earn Programme (Holder's Yield 15%→5%, KVT 20%→30%) has been formally enacted, and whether Schedule 6 of the Terms of Use has been amended accordingly. Get the effective date.
- [ ] Reconcile the advertised "2.05% aggregated 12-month yield" against the $26,326 June payout on $310M. Obtain Kinesis's calculation methodology and the eligible-balance denominator.
- [ ] Verify the ERC-20 contract `0x14DAB79fD7B7B3f748d434812Fd6a9Aac460EA52` on Etherscan: total supply, holder count, verified source, proxy/upgradeability, and freeze/blacklist functions. (Our fetch was blocked by a 403.)
- [ ] Determine how much of the 2.386M KAU sits in the ERC-20 wrapper, i.e. how many holders have unknowingly surrendered gold title and yield rights by bridging.
- [ ] Obtain the full KVT Offering Memorandum terms: how many of the 300,000 KVT were sold, to whom, and whether the 20% entitlement is contractually fixed or amendable like the Holder's Yield.
- [ ] Confirm the exact Recruiter Yield percentage currently paid (Terms use 7.5% in a worked example, not as a stated rate).
- [ ] Establish whether any vaulted metal is leased, encumbered or rehypothecated, given Kinesis's claim of 0% storage fees plus the ABX relationship.
