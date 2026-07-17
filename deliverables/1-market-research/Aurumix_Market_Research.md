# Aurumix — Market Research (Phase 1)

> **Purpose:** the precedent bank + failure-mode catalogue that de-risks every Mechanism Design decision. Not a literature review — every finding ends in a *"→ Aurumix implication"* tied to an MD block.
> **Method:** live deep research (Perplexity Sonar Deep Research, run 2026-07-15) across ten tracks, quality-checked for corroboration, recency, and single-source risk. Regulatory specifics are inputs for the client's legal counsel — we surface, we do not opine.
> **Model context:** V3 "100% Gold" is authoritative. See `Aurumix_V3_Business_Model_Explained.md` and `Aurumix_MD_Blueprint.md`.

### Confidence legend
- ✅ **High** — bedrock principle or corroborated by 2+ independent sources.
- 🟡 **Medium** — plausible and recent but single-source or fast-moving; verify before relying.
- 🔴 **Legal-verify** — a regulatory specific for the client's VARA/legal counsel; not legal advice.

### Track index
A1 UAE regulatory & classification · A2 Gold-token mechanics · A3 Yield/profit-share classification · A4 Gold-backed credit · A5 Failure modes · A6 Investor behaviour · **A7 Competitor/comparable landscape** · **A8 Proof-of-reserve & token standards** · **A9 Distribution compliance & inheritance precedent** · **A10 Secondary-market liquidity**

---

## Executive summary — the findings that change our MD

1. **The dividend is the classification landmine, and precedent is unanimous.** US (Howey), EU (MiCA/MiFID), UAE (VARA/CMA) all treat a token paying holders a **share of platform profit** as a **security / collective investment** — not a commodity token. ✅ → **B1, B5**
2. **There is a proven compliant path: deliver the reward off-token, at the account level.** Kinesis pays a fee-share "holder's yield" to *accounts*; Ondo separates the ownership token from the yield instrument. Reward survives; token stays a commodity. 🟡 → **B1, B5**
3. **Leading gold tokens keep the peg exact by funding custody via fees, never gram-erosion.** PAXG/XAUT charge **no ongoing storage fee**; ComTech charges custody as a *separate fee*, not by cutting the gram backing. Direct validation of our "charge custody in cash, keep the peg" call. ✅ → **B2**
4. **Physical redemption is standard among peers but large-increment** (PAXG/XAUT ≈430 oz, Kinesis 100 g, ComTech 1 kg). Aurumix's cash-only buyback is a real gap vs. the "you own physical gold" pitch. 🟡 → **B2**
5. **Gold-lending norms sit ≤75% LTV — Sovereign 110% is a genuine outlier** needing an explicit loss-absorbing backstop. ✅ → **B6**
6. **Referral + passive-income + lock-in is the single most enforced-against pattern in crypto** (Forsage, BitConnect, HyperFund, OneCoin, BlockFi). The lawful/unlawful line = commissions paid from **real transaction revenue**, not entry fees or new-investor money. Aurumix bundles all three — anti-MLM design must be airtight. ✅ → **B5, B8, B10**
7. **Aurumix's exact combination has no direct comparable — it is genuinely novel.** No product (India or global) bundles SIP accumulation + borrow-against-gold + yield/dividend + inheritance. Great differentiation, but no proven template and untested classification. ✅ → **B1, all**
8. **The compliant-token pattern is a permissioned base (ERC-3643) + optional ERC-20 wrapper, plus Chainlink Proof-of-Reserve** — and wrapping into plain ERC-20 *loses* the KYC/transfer controls. ✅ → **B1, B2**
9. **On-chain "digital wills" are novel and legally untested** — precedents (Casa, TrustVerse, DigiPulse) are niche and treat the chain as a *facilitation layer* alongside a real will, never a replacement. ✅ → **B7**
10. **Demand thesis validated but recurring-savings persistence is fragile:** Indian digital-gold via UPI grew ~377% in 16 months; households hold ~$3.8T of gold — but mutual-fund SIP **stoppage spiked >120%** in 2025. Stress-test growth, don't assume it. ✅ → growth/revenue/sim

---

## A1 — UAE regulatory & classification framework 🔴 (verify with counsel)

**The regulator map (2025–2026):**
- **VARA** (Dubai, ex-DIFC) — primary regulator for **Asset-Referenced Virtual Assets (ARVAs)**, the category a 100%-gold token falls into. Established under **Dubai Law No. 4 of 2022**.
- **CMA — Capital Market Authority** — the **former SCA, renamed/restructured effective ~1 Jan 2026** (Federal Decree-Laws No. 32 & 33 of 2025); federal **securities** regulator, now explicitly covering virtual assets, with a federal list of admissible VAs and criminalised unlicensed dealing. 🟡 (corroborated by the rwalabs guide citing CMA Decision 4/R.M/2026 + Resolution 15/2025)
- **ADGM / FSRA** — Abu Dhabi free zone, English common law; mature digital-securities regime (since 2018); institutional.
- **DIFC / DFSA** — Dubai free zone; tokenisation sandbox (Innovation Testing Licence).
- **CBUAE** — central bank; fiat-pegged **payment tokens/stablecoins** (PTSR 2024). *Not us — AURX is gold-pegged, not fiat.*

**VARA ARVA issuance — the numbers:**
- **VARA Virtual Asset Issuance Rulebook**, effective **19 June 2025**: a gold token = **Category 1 ARVA** issuance, needs a VARA VASP licence + ARVA and reserve-asset rulebooks. 🟡
- **Minimum paid-up capital:** higher of **AED 1.5M or 2% of reserve-asset value**; net liquid assets **≥1.2× monthly opex**. ✅ (2 sources)
- **Fees:** **AED 100,000 application** (one-time) + **AED 200,000/yr supervision**. **Timeline ~6–9 months+.** Each individual ARVA needs **standalone approval** before issuance. 🟡
- **Four VARA routes:** (1) Full ARVA Issuance (Cat 1, trading outsourced); (2) ARVA + Broker-Dealer/Exchange (end-to-end, capital up to ~25% of fixed annual overheads); (3) **Sponsored Regime** (operate under an existing licensee — faster, cheaper); (4) **Partnership Model** (outsource issuance to a Cat-1 holder). 🟡
- **Personnel:** full-time Compliance Officer, MLRO, CISO, DPO + ≥2 Responsible Individuals; PI/D&O/crime insurance. Ongoing: reserve/redemption duties, **half-yearly reserve audits, annual financial audits, monthly circulation/backing reports**, ranked (non-boilerplate) risk disclosures.
- **CMA capital (if it tips into securities):** Dealing as Principal **AED 4M**, Dealing as Agent **AED 1M**, Multi-party Trading Platform **AED 500k**. UAE-resident, individually-accredited CEO/CO/MLRO. 🟡

**The classification line (the crux):** a token that is *only* redeemable title to fully-reserved gold → **ARVA under VARA** (retail-friendly). Add **profit-share / dividend / managed-portfolio** features → **re-characterised as a security token / collective-investment product**, engaging both VARA's security-token standards *and* the CMA regime (heavier capital, licensed venues, possibly qualified-investors-only). 🔴

> **→ Aurumix implication (B1, the spine):** the gold core is a clean **ARVA under VARA**. The **dividend (and credit)** are what threaten to drag AURX into the securities/hybrid regime — smaller investor base, more capital, licensed-venue-only secondary trading. Build the whole MD to **keep AURX an ARVA** and push dividend/credit off-token. Consider the **Sponsored Regime** to shorten time-to-market. Definitive classification = a **[LEGAL]** item.

---

## A2 — Gold-token mechanics precedent ✅ (strong)

| Token | Backing | Custody | Storage/custody fee | Physical redemption | Peg treatment |
|---|---|---|---|---|---|
| **PAXG** (Paxos, NYDFS→) | 1 = 1 troy oz allocated LGD | LBMA London (Brink's, Malca-Amit) | **None ongoing**; mint/redeem tiered ~1%→0.125%; $2/mo inactivity after 12mo | Full LGD bar ≈ **430 PAXG** + ~large destruction fee + transport/insurance; ~20–45 business days; smaller amounts only via partnered bullion retailers | Exact 1oz; custody funded by fees. ⚠ **Paxos terms *reserve a right* to introduce a dilutive storage fee by self-minting** — a cautionary tale |
| **XAUT** (Tether Gold) | 1 = 1 troy oz allocated LGD | Swiss vaults; TG Commodities | **None ongoing**; one-time **0.25%** buy/redeem | Full bars (~430 XAUT), shipped to a Swiss-nominated address, KYC'd | Exact; funded by 0.25% + spreads; **no dilution mechanism** |
| **KAU** (Kinesis, Stellar) | 1 = 1 g allocated | Kinesis vaulting network (audited) | Mint ~0.90% (refunded to participants) + ~0.02% reward; $5 withdrawal | **100 g** increments via dashboard | Exact 1g; rewards/economics built on transaction fees/spreads, **no self-minting** |
| **CGO** (ComTech, Dubai DMCC) | 1 = 1 g, 999.9, 1kg bars, Tradeflow warrants | DMCC-approved Dubai vaults | Mint/burn 0.50%; trading 0.10–0.40%; **0.10% p.a. inventory fee after a grace period** (marketing says "zero" but fee tables show it) | **1 kg** bars, T+2–T+5, ~0.5% + shipping | Exact 1g; custody charged **as a fee, not by cutting the gram backing** |
| **CACHE Gold (CGT)** | 1 = 1 g | LBMA vaults | mint/redeem fees | gram-linked | **Integrates Chainlink Proof-of-Reserve** for near-real-time on-chain reconciliation (see A8) |

*(OneGram, a legacy Dubai token, appears dormant/opaque in 2025–26 — unverified. Reported gold-token trading volume ≈$90.7B in Q1 2026 — single-source, directional.) 🟡*

**Best-practice pattern (corroborated):** strict 1:1 reserve in segregated vaults; **finance custody via explicit, non-dilutive mint/redeem/transaction fees, spreads, or off-chain invoices — never by reducing gold-per-token.** ✅

> **→ Aurumix implication (B2):** direct external validation — **do NOT deduct custody in grams** (breaks the peg); charge it **in cash from SIP inflow + at gates**, PAXG/XAUT/ComTech-style. Decide physical redemption deliberately (e.g., 1 kg high-tier threshold vs cash-only, Q13). Learn from PAXG's *dilutive storage-fee clause* — do the opposite and hard-commit to a non-dilutive peg in the contract.

---

## A3 — Yield / profit-share classification ✅ (bedrock) + 🔴 (specifics)

**The four-prong test (US Howey), applied:**
1. *Investment of money* — buying tokens / depositing to earn = met.
2. *Common enterprise* — **pooling** investor funds + pro-rata distribution = met. (Regulators weigh this heavily.)
3. *Expectation of profit* — advertised yield/dividend/profit-share = met (marketing that stresses income is damning).
4. *From others' efforts* — profits from the platform's managerial/entrepreneurial efforts (setting rates, running the program) = met. (Purely mechanical/decentralised protocol rewards can *fail* this prong — but a company-run dividend does not.)

**Jurisdictions align:**
- **US:** SEC enforcement — **Kraken staking (Feb 2023, ~$30M settlement)**, **Coinbase staking (June 2023)** — pooling + advertised yields + platform discretion = unregistered securities. 2025–26 SEC guidance treats tokens conveying "rights to future income, profits, or assets of a business" as **digital securities**; purely protocol/ministerial rewards can be non-securities. 🟡
- **EU (MiCA):** excludes MiFID financial instruments — income-bearing tokens resembling shares/bonds/**fund units** fall under securities + **AIFMD/UCITS** fund law, not MiCA. Pooling + investment-policy management = a collective investment undertaking. ✅
- **UAE:** SCA's 2025 Security Tokens & Commodity Token Contracts regulation **excludes** plain VAs / non-security RWAs → an embedded profit-share is a **strong signal the token is a security**. VARA requires ARVA issuers to disclose exactly what rights the token conveys; a claim on platform income is a regulated (security-like) feature. 🔴

**How compliant projects keep the reward without the security label:**
- **Separate the ownership token from the yield instrument** (Ondo's RWA structure — scrutinised, not charged).
- **Deliver reward at the account level, not as a token-embedded right** — **Kinesis "holder's yield"** = a share of system fees, paid in metal, to accounts.
- Frame as **fee-based/discretionary without an ex-ante profit promise**; or a **separate regulated fund**, possibly **qualified-investors-only**. ✅

> **→ Aurumix implication (B1, B5):** there **is** a compliant path for the ICS Dividend — a *structural* one: attach it to the **KYC'd account, not the AURX token**, and frame it as a **discretionary loyalty/fee-share, not a promised profit dividend**. The doc's "80% to top 10% of 15–20% of operating profit" reads exactly like a fund distribution — the highest-risk possible wording. **This is the single most important redesign in the MD.**

---

## A4 — Gold-backed credit precedent ✅ (strong)

**India / RBI (directly relevant to the country-layer):**
- **Max LTV 75%** of gold value for NBFC gold loans (all purposes) — RBI consolidated Directions on Lending Against Gold Collateral. ✅
- For **bullet-repayment** loans, LTV must be computed on **principal + interest at maturity**, not just principal.
- LTV breach >30 consecutive days → **+1% standard-asset provisioning**; breach at maturity → **no renewal**.
- **RBI restricts lending against "primary gold" and gold-backed financial instruments** (e.g., gold ETFs / gold mutual-fund units) — a structural constraint on any India route. 🔴
- 2024–25 saw RBI *tightening/harmonising* gold-loan norms amid rising NPAs and high-LTV concerns.

**CeFi/DeFi mechanics:**
- **Origination LTV vs a separate, higher liquidation threshold**; health monitored continuously incl. accruing interest + price. Example (**Nexo**): ~30.8% origination vs ~83.33% liquidation trigger for a volatile asset. **Aave**: LTV cap + liquidation threshold + health factor; a **Safety Module / reserve** backstops shortfalls.
- **Convergence:** prudent LTV **well below 100%**, differentiated by collateral volatility/liquidity; shortfalls covered by **provisioning, platform reserves, or insurance funds**. Lending **at/above 100% LTV is not standard** and demands an explicit backstop. ✅
- **UAE:** consumer lending needs a **finance-company/lending licence** or a licensed partner. 🔴

> **→ Aurumix implication (B6):** gold is *low-volatility* collateral, so a **higher LTV than crypto is defensible** — but **110% (Sovereign) lends more than the collateral is worth** and needs a designed **loss-absorbing sink** (insurance fund / cross-collateral / reserve), or a cap below 100%. Adopt origination-LTV vs liquidation-threshold, continuous interest-inclusive health monitoring. The India path must respect **RBI's 75% cap + its restriction on lending against gold-backed instruments** — a structural reason the credit sits with a **licensed country-layer partner**, not on-chain from Dubai. **[LEGAL]** on licensing.

---

## A5 — Failure modes ✅ (well-documented)

| Case | Mechanism of failure | Lesson for Aurumix |
|---|---|---|
| **Terra/Luna, Iron Finance** | Reflexive "mint-the-reserve-token" loops + thin liquidity → death spiral when confidence broke | V3's 100%-gold model already avoids this — keep it; ensure the dividend isn't funded reflexively. |
| **e-gold, Karatbars** (gold-linked) | Reserve opacity + unlicensed e-money/banking → enforcement *despite* "gold backing" | "Backed by gold" is **not** a compliance shield. Proof-of-reserve + correct licensing are non-negotiable. |
| **MakerDAO Black Thursday, Wonderland, Abracadabra** | Leverage + flawed liquidation logic + contract bugs → insolvency / de-peg | The credit engine's liquidation logic (B6) must be robust + audited; avoid collateral circularity (don't let borrowed funds freely re-buy AURX). |
| **BitConnect ($2B), OneCoin, Mining Capital Coin, HyperFund ($1.7B), Forsage ($300M+), BlockFi ($100M SEC/state settlement), SafeMoon** | "Passive income" + lock-ins + **multi-tier referral** → unregistered securities / Ponzi / pyramid enforcement | Aurumix bundles **all three**. The dividend framing (A3) + agent network (A9) are the exact enforcement pattern. |

> **→ Aurumix implication (B5, B8, B10):** the riskiest thing isn't any single feature — it's the **combination** (profit-share + lock-in + referral tiers) that has repeatedly triggered enforcement. Turn mitigations into **hard invariants** in B10: transparent liquidity/redemption, no reflexive dividend funding, robust liquidation logic, referral rewards **capped, subordinate to investment, and paid from real fee revenue**.

---

## A6 — Investor behaviour ✅ (India-strong; diaspora thin)

- **Digital gold via UPI grew ~377% in 16 months** (Apr 2024: ~20.9M txns/₹550cr → Aug 2025: ~99.8M txns/₹1,184cr); UPI ≈85–90%+ of digital-gold buys. Jan 2026 ≈ ₹3,926cr (≈5× Jan 2025). (NPCI) ✅
- **Jar:** >20–35M users; average user saves ~22×/month; >1M txns/day; FY24 operating revenue ~₹2.08B (~$23.6M); raised ~$63.3M; valued >$300M; reached profitability in 2025. 🟡 (some figures restated/garbled — directional)
- **Indian households hold ~34,600 t of gold (~$3.8T)** — Morgan Stanley, Oct 2024. Gold ~**74% INR return in 2025** (SafeGold). ✅
- **Mutual-fund SIP inflows ≈ ₹2 trillion FY24 (+28% YoY)**, but **SIP stoppage ratio spiked >120%** in 2025 — recurring commitments are powerful *and* fragile. ✅
- Commitment devices, auto-debit, prize-linked rewards, gamification improve persistence, but effects **decay over multi-year horizons** and need reinforcement. Diaspora-specific digital-gold behaviour is a **data gap**. 🟡

> **→ Aurumix implication (growth assumptions, revenue, simulation):** demand thesis validated; LIC/SIP analogy holds. But the **>120% SIP stoppage** is a direct warning for a model whose engine *is* SIP persistence — stress-test the 500→100k targets and the retention mechanics against realistic lapse rates. Flag diaspora behaviour as a kickoff data request.

---

## A7 — Competitor / comparable landscape ✅ (novelty finding is robust)

**Indian digital-gold & gold-SIP platforms:**

| Platform | Model | SIP min | Credit against gold? | Yield beyond gold price? | Inheritance? | Physical delivery | Scale |
|---|---|---|---|---|---|---|---|
| **SafeGold** (powers PhonePe, GPay, Paytm) | Digital claims on 24K, independent trustee; **not a SEBI security** | ~₹10 (₹9 on Paytm) | No (separate NBFC pledge) | No; earns 2–5% spread + 3% GST | No | Yes — cash, coins, or jewellery via partners; no lock-in | Tens of millions of accounts via partners |
| **MMTC-PAMP** | 24K 99.99% LBMA refiner, allocated, insured | ~₹9 (via Paytm) | No | No | No | Yes — coins/bars | Major refiner; multi-tonne |
| **Augmont** | Digital gold, trustee oversight | ₹1,000/mo | No | No | No | Yes — anytime | B2B2C, unquantified |
| **Jar** | Round-ups + UPI autopay into 99.9% digital gold, bank-insured | ₹10/day | No | No | No | Yes — sell/convert | >20–35M users |
| **Gullak** | Digital gold + **"Gold+" leasing** (extra return) | ₹100/day | No | **Leasing yield** (not a credit line) | No | Yes | Smaller |

**Tokenized gold with yield/credit:** Kinesis (holder's yield fee-share + gold-backed debit card), ComTech (Dubai), Aurus/tGOLD, Theo thGOLD, Matrixdock XAUm — these bundle **yield or credit** around a gold token but **not** native SIP accumulation or inheritance.

**Structural analogs:** **MicroStrategy (MSTR)** and **Sprott PHYS** — single-asset vehicles that trade at a **premium or discount to NAV** when they layer structural advantages (leverage, access, tax) or frictions atop the underlying asset. Lesson: a claim on an asset can diverge from the asset's raw value — Aurumix's "modest premium" thesis (credit + dividend rights travelling with the token) is plausible *in principle*, but premiums are not guaranteed and can invert to discounts.

**The headline finding:** **No product, in India or globally, bundles all four Aurumix pillars — SIP accumulation + borrow-against-gold + yield/dividend + inheritance — in one integrated retail product.** Indian platforms do accumulation + delivery but no credit/yield/inheritance; tokenized-gold projects do yield/credit but no SIP/inheritance. **Aurumix's combination is genuinely novel (2024–2026).** ✅

> **→ Aurumix implication (B1 + everything):** novelty is a **double-edged sword.** Upside: real differentiation, no direct competitor. Downside: **no proven template to copy, and the regulators have no precedent box to file it in** — which *amplifies* the classification risk from A1/A3. It also means we should borrow validated *components* from the leaders (SafeGold's trustee-held allocated model, Kinesis's account-level yield, ComTech's Dubai/DMCC custody) rather than invent each wheel. Positioning: "the first product that does all four" is a strong narrative *if* the compliance is airtight.

---

## A8 — Proof-of-reserve & compliant token standards ✅ (strong)

**Two token archetypes:**
- **Consumer / freely-transferable** (PAXG): plain **ERC-20**, no token-level KYC; compliance enforced at the *venue* (exchange) level.
- **Institutional / permissioned** (ERC-3643 "T-REX", ERC-1400/1404): **on-chain identity registry (ONCHAINID)**, compliance modules, **transfer restrictions, freeze, forced-transfer**. Adopters: Tokeny and institutional RWA issuers (tokenized funds/bonds). Newer RWA interfaces: ERC-7540, ERC-7943. 🟡 on the newest EIPs.

**Proof-of-Reserve (PoR):**
- **Traditional:** monthly/quarterly independent audits. **PAXG** — KPMG attestation that ounces in custody = tokens in supply; plus an **allocation-lookup tool** mapping an address → specific bar serials/purity/vault. Limitation: snapshot lag, off-chain PDFs contracts can't read.
- **On-chain oracle PoR:** **Chainlink Proof-of-Reserve** feeds custodian/issuance data on-chain so contracts can compute collateralisation and **halt minting/redemptions if reserves fall below threshold**. **CACHE Gold** integrates it for near-real-time reconciliation. ✅
- **Best practice:** combine regular independent audits (system-level assurance) + oracle PoR (contract-enforceable, low-latency) + a user-facing allocation lookup (personal verification).

**The wrapper trade-off (validates our earlier point):** a **permissioned base token (ERC-3643) + optional ERC-20 wrapper** reconciles compliance with DeFi composability — but **wrapping into a plain ERC-20 *loses* the on-chain KYC / transfer-restriction / freeze / forced-transfer controls** (you fall back to venue-level compliance only). ✅

> **→ Aurumix implication (B1, B2):** adopt the **ERC-3643 base + ERC-20 wrapper** pattern, and design **explicitly for what rights survive wrapping** (KYC, credit, dividend, buyback eligibility likely *don't* — they must re-attach on re-registration). Build **Chainlink PoR + LBMA-audited attestation + allocation lookup** into B2's proof-of-custody gate ("no confirmation, no event") so it's contract-enforceable, not just a PDF. This is the concrete architecture behind the B1 "constitution."

---

## A9 — Distribution compliance & inheritance precedent ✅ (strong)

**Multi-level distribution — the lawful/unlawful line (US FTC + SEC):**
- **Koscot / BurnLounge (9th Cir) two-prong pyramid test:** it's a pyramid if participants pay for (1) the right to sell **and** (2) the right to earn from **recruiting**, where those rewards are **unrelated to sales to ultimate users.** A real product does **not** save it.
- **FTC staff advisory:** internal consumption isn't per se fatal — what matters is whether commissions are funded by **genuine, non-incidental product revenue** vs **payments for the right to participate.** Reaffirmed in **FTC v. Noland (2023)**, a crypto MLM case.
- **Compliant template (Bybit-style):** commissions = a share of **actual transaction fees**, tied to real user activity, time-capped — **not** entry fees or new-investor money.
- **UK FCA introducer guidance:** the authorised firm must **retain ownership of the advice/suitability process** and do due diligence on introducers.
- **Enforcement roll-call (all combined pyramid + unregistered-securities):** Forsage (SEC 2022 / DOJ 2023, $300M+, "slots" matrix), Forcount (2022, $8.4M), BitConnect (2021, $2B), HyperFund (SEC complaint 2024, $1.7B, "membership interests"), MCC (2022). Common DNA: pay for the **right to participate**; **no external revenue**; recruitment-driven; risk-free-return marketing; weak KYC/AML. ✅

> **→ Aurumix implication (B8, B5):** the agent network can be lawful, but only if commissions are paid **from real platform fee revenue tied to genuine savings activity**, referral rewards are **capped and subordinate to investment**, earnings claims are **substantiated**, and the depth cap + on-chain enforcement are real. Combined with the dividend (A3), the danger is the *whole* package reading as a "pay-to-participate, earn-from-recruits-and-yield" scheme — the Forsage/HyperFund pattern. Keep distribution economics **transparently fee-funded**, never investor-funded.

**Inheritance / "Digital Will" precedent:**
- Precedents exist but are **niche and heterogeneous:** **Casa Inheritance**, **TrustVerse**, **Safe-based multisig legacy** contracts, **DigiPulse** (inactivity/"dead-man-switch" trigger), Sarcophagus, Ledger Recover, exchange beneficiary programs.
- They grapple with **liveness/death detection, KYC of beneficiaries, and legal validity** — and operate in a world where **smart-contract "wills" are not recognised wills** in most jurisdictions (probate law governs). **Purely on-chain digital inheritance remains novel and legally untested.** ✅
- Best practice: position the on-chain mechanism as a **facilitation/transfer layer that complements — never replaces — a legally valid will.**

> **→ Aurumix implication (B7):** Aurumix's Digital Will is **on the frontier** — a differentiator, but legally unproven. The doc's own positioning ("financial transfer instruction layer, not a legal will") is exactly right and matches precedent. Design the death/condition triggers around a **nominated-executor + KYC-of-beneficiary** model (as DigiPulse/Casa do), and make the "keep a real will too" advisory explicit. **[LEGAL]** per target jurisdiction.

---

## A10 — Secondary-market liquidity & market-making 🟡→✅ (structural lessons solid)

- **PAXG** (Paxos, launched 2019, 1 oz LGD, Brink's, NYDFS): market cap ~**$2.46B**; 24h volume **>$120M**; **tight spreads + reasonable depth on major CEXs**, but **thinner on DEXs with measurable slippage above a few $M**. **XAUT** smaller (deep hundreds in market-cap rank), Swiss-vaulted. 🟡 (point-in-time figures)
- Prices **track gold NAV within tens of bps** normally, but **short-term premium/discount can reach several %** (and more in stress) when liquidity is thin or arbitrage capital is constrained. ✅
- **Arbitrage (token vs spot vs derivatives) is the balancing force** that re-anchors the peg; a **credible mint/redeem right is what makes arbitrage work.**
- **Emerging consensus:** **AMMs/DEX pools should be a "last-mile" convenience layer, not the primary price-discovery venue.** Deep liquidity + NAV anchoring come from **issuance/redemption, KYC-gated order books, and periodic auctions.** Impermanent loss is a real issue for a redeemable asset-backed token in AMM pools. ✅

> **→ Aurumix implication (B9):** this is the quantified backbone for Tony's liquidity-drain concern. Design principles: (1) the **buyback/redemption right is the peg-anchor** — it powers arbitrage, so keep it credible and low-friction; (2) treat **DEX pools as convenience, not price discovery**; lead with CEX order books + market-maker arrangements; (3) **size seed liquidity against the free float** (locked + pledged + spot) and model slippage so a single large seller can't disconnect secondary price from the gold floor beyond a set tolerance; (4) plan the **Year-2 launch liquidity budget** and MM incentives explicitly.

---

## The master map — precedent → implication → MD block

| # | Finding | Confidence | MD block |
|---|---|---|---|
| 1 | Profit-share/dividend → security/CIS across US/EU/UAE | ✅ | B1, B5 |
| 2 | Compliant reward = off-token, account-level, discretionary (Kinesis/Ondo) | 🟡 | B1, B5 |
| 3 | Keep peg exact; fund custody via fees, never gram-erosion | ✅ | B2 |
| 4 | Physical redemption standard but large-increment (430oz/100g/1kg) | 🟡 | B2 |
| 5 | Gold LTV ≤75%; 110% needs a backstop; interest-inclusive LTV | ✅ | B6 |
| 6 | Referral+income+lock-in = top enforcement pattern; pay from real fees only | ✅ | B5, B8, B10 |
| 7 | UAE: ARVA (VARA) vs security (CMA); AED 1.5M/2% capital; 100k+200k fees; 6–9mo | 🔴 | B1 |
| 8 | "Gold-backed" is not a compliance shield (e-gold/Karatbars) | ✅ | B1, B10 |
| 9 | RBI restricts lending vs gold-backed instruments → country-layer partner | 🔴 | B6 |
| 10 | Huge Indian digital-gold demand; SIP stoppage >120% | ✅ | growth/sim |
| 11 | Aurumix's 4-pillar combo has no direct comparable — novel | ✅ | B1, all |
| 12 | ERC-3643 base + ERC-20 wrapper; wrapping loses KYC/transfer control | ✅ | B1, B2 |
| 13 | Chainlink PoR + audit + allocation lookup = proof-of-reserve best practice | ✅ | B2 |
| 14 | On-chain "digital wills" novel + legally untested; complement a real will | ✅ | B7 |
| 15 | AMM = last-mile; redemption right anchors peg; size liquidity vs float | ✅ | B9 |

---

## Quality-check notes (what's solid, what needs verification)

- **High-confidence, build on now:** profit-share→security (Howey is bedrock; 3 jurisdictions agree); keep-the-peg custody practice; gold LTV norms + the 110% concern; referral+yield+lock-in enforcement pattern; the novelty finding (no direct comparable); ERC-3643+wrapper + PoR pattern; AMM-as-last-mile + redemption-anchors-peg; India demand + SIP fragility.
- **Verify before relying (🟡):** exact 2025–26 regulatory instruments/dates (CMA rename ~Jan 2026, VARA Issuance Rulebook 19-Jun-2025, SEC 2026 guidance); Kinesis/Ondo structuring specifics; point-in-time figures (PAXG market cap/volume/redemption fee, Jar's user/revenue numbers). A few raw figures returned garbled (an invalid "31 September" date; restated Jar revenue) — used directionally only.
- **Legal-verify (🔴) — for counsel, not opined here:** the definitive VARA classification of AURX with dividend/credit attached; credit-facility licensing (UAE + India NBFC route + RBI gold-lending restriction); whether the chosen dividend/agent structure clears CMA/VARA/FTC-style tests; Digital Will legal validity per jurisdiction. These are the blueprint's **[LEGAL]** items.
- **Data gaps:** diaspora/NRI-specific digital-gold behaviour; live secondary-liquidity depth curves for gold tokens (only point snapshots found). Flag as kickoff / simulation-input requests.

*Sources: live research via Perplexity Sonar Deep Research (2026-07-15) drawing on VARA / SCA-CMA materials, RBI Directions on Lending Against Gold Collateral, SEC guidance & enforcement (Kraken, Coinbase, Forsage, BitConnect, HyperFund, Forcount), FTC MLM guidance (Koscot/BurnLounge/Noland), MiCA, issuer docs (Paxos/Tether Gold/Kinesis/ComTech/CACHE), Chainlink PoR & ERC-3643/T-REX documentation, Indian digital-gold platform disclosures (SafeGold/Jar/MMTC-PAMP/Augmont/Gullak), NPCI/AMFI/World Gold Council/Morgan Stanley data, inheritance-tool docs (Casa/TrustVerse/DigiPulse), and the rwalabs.ae UAE tokenization guide. Regulatory specifics are inputs for the client's legal counsel, not legal advice.*
