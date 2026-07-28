# Digital Gold (DGLD)

**Status: LIVE, and this is a correction to the task premise.** DGLD was not a protocol that quietly died. It was a protocol that quietly died and then was **bought out of dormancy and relaunched**, which is a materially different and more useful story. MKS PAMP acquired 100% of the issuer on 20 November 2025, redeployed the token on Base on 16 December 2025, survived a **$250k bridge exploit on 23 February 2026**, and is trading today with a live 1-gram physical redemption path.

The dormancy was real: roughly **six years of near-total inactivity** between the 2019 launch and the November 2025 relaunch, described by MKS PAMP's own CEO as a launch that was "too early" ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)). So the failure the task anticipated did happen. What did not happen is the wind-down. **DGLD is the only protocol in the set that failed and came back, and the reason it could come back is the most transferable finding in this profile.** See §12.

**Second correction: the chain was not RSK.** The task brief states DGLD used RSK. It did not. It launched on **Ocean, a Bitcoin sidechain built by CommerceBlock** on the Blockstream Liquid codebase. This matters because Ocean's failure mode is specific to it, not generic to Bitcoin sidechains. See §8.

## At a glance

| Field | Value | Confidence |
|---|---|---|
| Ticker | DGLD | **High** |
| Issuer (marketing) | "Gold Token SA (GTSA), the tokenization arm of MKS PAMP" | **High** |
| Issuer (registry) | **Gold Token SA, CHE-287.630.262**, société anonyme, incorporated **8 August 2018**, seat **Carouge, Geneva** (moved from Geneva 26 May 2025), share capital **CHF 3,401,100** (reduced from CHF 4,668,500 on 11 Apr 2024), status **Active** ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)) | **High** |
| Parent | **MKS PAMP SA, CHE-105.871.847**. Acquired 100% of GTSA 20 Nov 2025 ([dgld.ch](https://dgld.ch/about-us)) | **High** |
| Domicile | **Switzerland (Canton of Geneva)**. Governing law Swiss, courts of Geneva | **High** |
| Backing claim | 1 DGLD = **1 fine troy ounce** of LBMA-certified PAMP gold, allocated, in MKS PAMP Swiss vaults | **High** |
| Chains | **Ethereum + Base**. Originally Ocean (Bitcoin sidechain), migrated Nov 2022 | **High** |
| Contract address(es) | Ethereum `0xA9299C296d7830A99414d1E5546F5171fA01E9c8`; Base `0xe908475f8Beb7A138B0dc6eb5A05cb27068ffB9A`. **Both redeployed March 2026 post-exploit** | **High** |
| Supply | **~2,004.85 DGLD** (~2,005 oz): 1,603.69 on Ethereum, 401.16 on Base ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)) | **High** |
| Market cap / AUM | **~$8.1M** | **High** |
| Daily volume | **~$12k–19k** across three Uniswap V4 / Aerodrome pools ([CoinGecko](https://www.coingecko.com/en/coins/gold-token-sa-dgld-tokenized-gold)) | **High** |
| Holders | ~3,025 (Ethereum) / ~3,962 (all chains), +32.5% over 30 days | **Medium** |
| Regulatory status | **No FINMA licence.** AML affiliation to **VQF**, a FINMA-supervised SRO. Membership number **Not disclosed** | **High** |
| Subscription fee | **0.20%** ("Creation Fee") | **High** |
| Ongoing custody fee | **Zero.** "Embedded in DGLD... Tokenholders are not charged any separate or additional fees" | **High** |
| Redemption fee | **0.20%** ("Burning Fee") + third-party shipping/insurance/customs at cost | **High** |
| Minimum redemption | **1 gram** | **High** |
| Minimum direct subscription | **400 XAU (~$1.6M)**, accredited institutions only | **Medium** |
| Advertised yield | **None.** T&Cs expressly disclaim "any financial return, interest, dividend" | **High** |
| Named officers | **James Emmett** (President/board), **Kurt Hemecker** (CEO, GTSA), **Roman Peter Schnider** (board), per register as of 12 Jan 2026 | **High** |

---

## 1. What it is

DGLD is a 1-token-1-troy-ounce gold token issued by Gold Token SA, a Geneva company that is now the wholly owned tokenisation arm of **MKS PAMP**, one of the largest precious-metals refining and vaulting groups in the world. The gold is PAMP-refined, LBMA-certified, allocated to specific bars, and vaulted in Switzerland.

Its history splits cleanly into three phases:

1. **2019–2022, the consortium era.** Launched 15 October 2019 by a consortium of **CoinShares International**, **MKS SA** and **Blockchain.com**, on the **Ocean** Bitcoin sidechain ([CoinDesk](https://www.coindesk.com/markets/2019/10/15/coinshares-blockchain-launch-gold-token-network-on-a-bitcoin-sidechain/)). Backed by ~$20M of gold at launch. Each token was **one-tenth of a troy ounce** at this stage, not one ounce ([The Block](https://www.theblock.co/post/43306/coinshares-jointly-rolls-out-a-gold-token-dgld-built-on-the-bitcoin-network)).
2. **2022–2025, dormancy.** Migrated off the sidechain to Ethereum in November 2022. Then essentially nothing for three years.
3. **Nov 2025–present, the MKS PAMP relaunch.** Full acquisition, Base deployment, professional market-making, a live retail redemption path.

The distinguishing feature, and the reason this profile is worth reading despite an $8M market cap, is that **DGLD's legal structure is the strongest in the entire landscape set**: genuine co-ownership of specific bars under Swiss property law, not a creditor claim. See §2.

## 2. Legal structure

**This is the best-documented and strongest holder position we have found across ten protocols, and it is worth quoting exactly.** From the [General Terms & Conditions](https://dgld.ch/legal/general-terms-conditions-dgld-2):

> "The DGLD token qualifies as a title of proof (art. 8 CC)."

> Holders acquire **"co-ownership rights (art. 646 CC) and indirect possession (art. 919 CC) over the Gold."**

> **"Title to and ownership in Gold shall at all times remain with the Tokenholder."**

And the negative limb, equally explicit:

> "DGLD does not however represent claims such as a debt or equity claim or other financial claim against GTSA" and "does not confer any financial return, interest, dividend, claim for repayment."

**Confidence: High.** This is a primary legal document, not marketing.

Read carefully, this is a genuinely different instrument from most of the set. A DGLD holder is **not a creditor of the issuer**. They are a **co-owner of a pool of specific gold bars** under Swiss Civil Code articles 646 (co-ownership) and 919 (possession), with GTSA and the custodian holding as **indirect possessors** on their behalf. Transfer of the token is constructed as a transfer of the co-ownership right under property law, with the custodian "deemed to be validly notified of the transfer... via the change of records in the Blockchain."

**Why this matters more than it sounds.** In an insolvency of GTSA, a creditor claim ranks with other unsecured creditors and the gold is an asset of the estate. A **co-ownership right is not an asset of the estate at all**: it is third-party property that must be segregated out. That is the whole ballgame for a gold token, and DGLD is one of the few that has actually documented it in enforceable terms rather than asserting "your gold is safe."

**Caveats, stated plainly:**

- rwa.xyz describes DGLD as **"bankruptcy-remote under Swiss law"** and cites the Swiss DLT Act with FINMA supervision ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). The **T&Cs themselves contain no insolvency clause** and do not cite the DLT Act, DLT-TEF, or **art. 242a of the Debt Enforcement and Bankruptcy Act** (the provision that actually governs segregation of crypto-based assets in a Swiss bankruptcy). Perplexity searching also found no such citation. So the bankruptcy-remoteness claim rests on the **inference** from arts. 646/919 rather than an express contractual or statutory recital. **Confidence: Medium** on bankruptcy remoteness as a legal conclusion; **High** on the co-ownership language it is built from.
- rwa.xyz's statement that GTSA is "supervised by FINMA" is **wrong**, or at best a compression. GTSA is an SRO member. See §3.
- Co-ownership is of a **pool**, not of a nominated bar per holder, notwithstanding the per-bar verification tool. Whether a holder can compel delivery of a **specific** serial-numbered bar is **Not disclosed**.

## 3. Regulatory and compliance posture

| What we checked | Result |
|---|---|
| FINMA licence (bank, securities firm, fund manager) held by GTSA | **Not found.** No FINMA authorisation identified or claimed |
| SRO affiliation | **VQF**, a FINMA-supervised self-regulatory organisation ([dgld.ch](https://dgld.ch/about-us)) |
| VQF membership number | **Not disclosed.** Not published by GTSA and not located on VQF registers |
| Swiss commercial register | **Active**, CHE-287.630.262, Carouge GE ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)) |
| Registered purpose covers token issuance | **Yes**, expressly: "l'émission et la commercialisation de jetons virtuels... adossés à des matières premières physiques" |
| Enforcement action against GTSA or MKS PAMP | **None found** |
| EU/EEA marketing | **Expressly disclaimed**: "Gold Token SA does not target or solicit EU/EEA persons"; EU/EEA access permitted on reverse solicitation only |

**The key distinction, and it is the same trap as "audited".** VQF membership is an **anti-money-laundering** affiliation. It is what a Swiss financial intermediary joins instead of being directly supervised by FINMA for AML purposes. **It is not a licence, it does not involve FINMA approving the product, and it says nothing about prudential soundness, reserve adequacy or investor protection.** GTSA's own phrasing, "regulated through VQF, a FINMA-supervised SRO," is accurate but engineered to put "FINMA" in the sentence. rwa.xyz then compressed it into "supervised by FINMA," which is false. **This is the "regulated in Switzerland" halo effect in action, and the compression happened within one hop of the issuer's own wording.**

Notably, the registered corporate purpose **does** expressly authorise commodity-backed token issuance, which is more than can be said for Comtech's DAFZA licence. GTSA is lawfully doing what its register entry says it does. It just is not prudentially licensed for it, and it does not claim to be.

**Relevance to design question 4:** DGLD is the Swiss analogue of the "cheap route" Aurumix is hunting for. An SRO affiliation plus a well-drafted property-law structure, at a fraction of a VARA licence's cost. The trade is that **the protection comes from Swiss property law and the courts of Geneva, not from a regulator**. That works precisely because Swiss law has a strong, tested doctrine of co-ownership in fungible custody pools. **It is not obviously portable to the UAE**, and Aurumix should not assume it is.

## 4. Custody and proof of reserve

| Element | DGLD |
|---|---|
| Gold custodian | **MKS PAMP SA** vault facilities, Switzerland (PAMP SA refinery at Castel San Pietro) |
| Vault city | Switzerland; specific vault site **Not disclosed** |
| Allocated? | **Yes**, asserted as allocated LBMA-certified PAMP bars with co-ownership at law |
| Bar list | **Yes, and this is genuinely strong.** The `dgld.ch/verify` tool takes a wallet address and returns **specific PAMP bar serial numbers, refinery dates and vault locations** for that holder's position, from 0.001 DGLD upward ([step-by-step guide](https://dgld.ch/news/dgld-complete-step-by-step-guide-november-2025)) |
| PoR feed | Per-wallet verification tool rather than an oracle feed. No Chainlink PoR identified |
| Reserve attestation | **Contested. rwa.xyz names KPMG as auditor** ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). **We could not confirm this from any GTSA source, and a dedicated search found no DGLD reserve attestation report, no named attestor and no stated frequency.** GTSA's verify tool refers to "latest signed audits" without naming the signer. **Confidence: Low** on KPMG; **the absence of a downloadable, dated, named-firm reserve attestation is the finding** |
| Smart contract audit | **Yes, and now unusually well evidenced: Hacken and Halborn**, both engaged post-exploit, both reports stated to be publicly released, March 2026 ([post-incident report](https://dgld.ch/news/post-incident-report-february-2026-exploit)) |
| Token infrastructure custody | **Utila Inc** per rwa.xyz. Unconfirmed from GTSA sources. **Confidence: Low** |

**Apply the brief's rule precisely here, because DGLD inverts the usual pattern.** Most protocols in this set have a smart-contract audit and no reserve attestation, while implying the reverse. DGLD **also** has the strong smart-contract audits and the unconfirmed reserve attestation, but it compensates with something better than most attestations: **a per-holder, serial-number-level bar lookup**. A retail holder can check their own specific bars. That is more useful to an individual than a quarterly PDF saying the aggregate balances.

**But it is not a substitute for an attestation, and the distinction is exactly the one the brief warns about.** The verify tool is **issuer-published data**. It proves GTSA's records are internally consistent with the chain. It does not prove an independent third party physically counted the bars. And per PMGT: **an issuer-hosted verification tool has exactly the lifespan of the issuer's hosting bill.** DGLD's six dormant years are direct evidence of how quickly issuer infrastructure can go quiet.

## 5. Issuance

**Two-tier, and the tiers are very far apart.**

- **Primary (direct minting with GTSA):** restricted to **accredited institutions**. MKS PAMP issues DGLD only to accredited institutions, who then sell on secondary crypto exchanges ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)). Minimum subscription reported as **400 XAU**, roughly **$1.6M** at current prices ([rwa.xyz](https://app.rwa.xyz/assets/DGLD)). **Confidence: Medium** (single source; not published in the T&Cs). Creation fee **0.20%**.
- **Secondary (everyone else):** buy on Uniswap V4 (Ethereum) or Aerodrome (Base). **No KYC at all.** GTSA's own guide states KYC "is entirely optional and only triggers" on a physical delivery request.

MKS PAMP's **trading arm purchases tokens and provides liquidity on exchanges**, so the group is both issuer and principal market maker. The February 2026 incident report confirms this directly: GTSA bore the large majority of the ~$250k loss "as we serve as the principal liquidity provider."

**This is a materially different distribution model from Aurumix's and worth noting: a $1.6M primary minimum with a zero-KYC secondary market.** Retail is served, but only ever as a price-taker on a DEX, never as a primary subscriber.

## 6. Redemption

**DGLD has the most retail-accessible physical redemption in the entire landscape set, and by a wide margin.**

- **Minimum: 1 gram.** Not 1 ounce, not a 400oz Good Delivery bar, not "qualified holders." One gram, from a $4,000-per-token instrument.
- **Fee: 0.20% flat**, plus actual third-party shipping, insurance and customs at cost. GTSA "does not currently charge any separate fee or surcharge" on delivery.
- **Process:** email `support@dgld.ch` with wallet address, grams and shipping address; receive a quote within hours; complete **one-time KYC (ID + selfie, 5–10 minutes)**; transfer DGLD and pay; receive shipped bars. Europe 3–7 business days by insured post, other regions on request.
- **Eligibility, from the T&Cs:** any entity demonstrating "power of disposal over the relevant DGLD may request the delivery of the corresponding Gold."

**That eligibility clause is the important one.** Compare the brief's warning about eligibility limited to undefined "qualified holders." DGLD's test is **control of the tokens**, full stop. It is not limited to the original subscriber, not limited to accredited investors, and not limited to a minimum ounce count. **A holder who bought $130 of DGLD on Uniswap with no KYC can convert it into a physical gram of PAMP gold shipped to their door.**

GTSA reserves rights to "refuse, suspend or postpone a Delivery" for KYC/AML failure, ownership conflicts, suspected unlawful activity, or where "Delivery would otherwise be contrary to applicable law." These are ordinary and narrowly drawn.

**Direct answer to design question 5.** DGLD is the sharpest possible counter-example to Aurumix's no-physical-redemption design. It demonstrates that gram-level retail physical delivery is **operationally solvable at 0.20%** by an issuer that happens to own the refinery. That is the honest comparison: MKS PAMP can do this cheaply because it *is* PAMP. Aurumix cannot replicate the cost base. But Aurumix should stop treating "no physical redemption" as an industry norm it is merely conforming to. **It is a deliberate retention and credit-revenue choice, and DGLD is the proof that the alternative exists at retail scale.**

## 7. Fees and revenue model

| Fee line | DGLD |
|---|---|
| Subscription / creation | **0.20%** |
| Ongoing custody / storage | **Zero to the holder.** "Embedded in DGLD. Accordingly, Tokenholders are not charged any separate or additional fees" |
| Redemption / burning | **0.20%** |
| Re-issuance | Amount "determined by GTSA before the process begins", unquantified |
| Physical delivery | Third-party transport, insurance, customs at cost. No GTSA surcharge "currently" |
| Transfer | None from issuer (gas only) |
| Yield paid to holders | **None**, expressly disclaimed |

**Per the wave-1 addendum, question 1 is settled, so just the two things that are actually novel here.**

**First, the funding mechanism is the cleanest in the set.** Most zero-custody-fee protocols leave "what funds the vault?" unanswered. DGLD's answer is structural and credible: **MKS PAMP owns the vaults and the refinery.** Storage is marginal cost on infrastructure the group already runs for its core bullion business. This is not cross-subsidy from investor fees, it is genuine vertical integration. **This is the one protocol in the set whose zero-fee promise is economically self-evident.**

**Second, watch the word "embedded."** The T&Cs say storage and administration costs are "embedded in DGLD." That phrasing is doing unexamined work. If it means the cost is absorbed by MKS PAMP, fine. If it ever comes to mean the cost is recovered **from the gold backing each token**, then the ounce-per-token ratio drifts below 1 and DGLD's central claim breaks. **We found no clause specifying which.** For a 1-token-1-ounce product that would be peg-breaking. **For Aurumix, whose peg is grams ÷ tokens, an in-kind deduction is peg-neutral** (the same logic as the PAXG minting clause flagged in the addendum). Worth quoting to the client as a second precedent for in-kind fee recovery, with the caveat that DGLD has not disclosed that this is what it does.

**Also note the "currently" in the delivery-fee clause.** GTSA "does not *currently* charge any separate fee or surcharge." That is a reserved right to start charging, exactly the pattern the addendum flags as the interesting case.

## 8. Token architecture

- **Standard:** ERC-20 on Ethereum and Base. **Not permissioned.** Freely transferable, no whitelist, no KYC gate on transfer.
- **Original chain: Ocean, a Bitcoin sidechain developed by CommerceBlock**, built on the **Blockstream Liquid codebase**. CommerceBlock claimed Ocean removed Liquid's federated second layer of trust ([CoinDesk](https://www.coindesk.com/markets/2019/10/15/coinshares-blockchain-launch-gold-token-network-on-a-bitcoin-sidechain/), [Bitcoin Magazine](https://bitcoinmagazine.com/technical/coinshares-blockchain-launches-digital-gold-token-on-bitcoin-sidechain)). **This is not RSK, and the brief's premise should be corrected.**
- **Migration:** moved to Ethereum in **November 2022**. The original sidechain DGLD **ceased to exist**, and the wrapped `wDGLD` tokens that had existed on Ethereum since 2020 were replaced by the new native ERC-20 DGLD.
- **Upgradeability / admin keys:** GTSA can **pause** both contracts (exercised February 2026), **redeploy** them, and **reset balances to a pre-exploit snapshot** (exercised March 2026). These are extensive unilateral powers. Precise role architecture **Not disclosed**.
- **Bridge:** a native Ethereum↔Base bridge. **This is what was exploited.**
- **Audits:** Hacken and Halborn, March 2026.

### What the Bitcoin-sidechain choice actually cost it

This is the question the task asked, and the answer is unusually clean because DGLD ran the experiment and then reversed it.

**The direct costs of Ocean, 2019–2022:**

1. **No composability, which was the entire point of being on-chain.** In 2019–2021 the whole tokenised-asset thesis was DeFi: collateral in lending markets, AMM pairs, yield strategies. Ocean had none of that. There was no Uniswap, no Aave, no Curve. A gold token on Ocean was a database entry with extra steps.
2. **No wallet support.** GTSA had to build and maintain its own **`ocean-wallet`** ([GitHub](https://github.com/goldtokensa)). Every holder needed bespoke software. Compare today: paste a contract address into Uniswap. **The GitHub repo's last commit is October 2020**, which dates the abandonment of the sidechain effort a full two years before the formal Ethereum migration.
3. **They had to build a bridge to Ethereum anyway.** By November 2020, barely a year after launch, the consortium had shipped **`wDGLD`, a wrapped ERC-20 on Ethereum**, because that was where the users were ([Blockchain.com/Medium](https://medium.com/blockchain/wrapped-dgld-brings-swiss-vault-held-gold-to-ethereum-2a4a8cae81b1)). **The sidechain strategy was conceded within 13 months.** The wrapper then added its own trust layer, so holders got the sidechain's illiquidity *and* a bridge's risk.
4. **No exchange listings.** Listing a Bitcoin-sidechain asset requires a CEX to integrate a bespoke node. Almost none did. The addressable venue set was near zero.
5. **The security narrative did not convert into users.** "Secured by the Bitcoin network" was the pitch. Bitcoin holders are, in practice, the population *least* interested in holding a non-BTC asset, and the population most averse to unfamiliar sidechains.

**Net cost: roughly three years and the first-mover position.** DGLD launched October 2019 with ~$20M of gold, blue-chip partners and real Swiss vaulting. PAXG had launched only about a month earlier, in September 2019, on Ethereum. **PAXG is ~$1.79bn today. DGLD is ~$8M.** The custody quality was comparable. The chain choice was not. That is close to a controlled experiment, and it is the single most quantified answer to "what does the wrong chain cost."

**The counter-observation that keeps it honest:** the chain was necessary but not sufficient. DGLD migrated to Ethereum in November 2022 and **still stayed dormant for three more years**. Getting onto the right chain did not revive it. What revived it was **an owner with a commercial reason to push it**. See §12.

### The February 2026 exploit

Documented candidly by GTSA ([post-incident report, 21 March 2026](https://dgld.ch/news/post-incident-report-february-2026-exploit)):

- **23 February 2026.** An edge case in **legacy code** in the Ethereum contract's `transferFrom` "could report successful execution without enforcing the expected token movement." Via the Ethereum↔Base bridge this permitted fraudulent minting on Base.
- **Over 100 million unbacked DGLD minted on Base**, against a legitimate Base circulation of about **70.8 tokens**. A ratio of roughly 1.4 million to one.
- Contracts paused and the bridge frozen within about **2 hours 25 minutes**.
- Economic impact **~$250,000**, "in very large majority borne by us, as we serve as the principal liquidity provider."
- **All physical gold reserves unaffected.** All pre-exploit holders on both chains unaffected and retained their holdings.
- Remediation: pre-exploit balance reset 11 March, Ethereum relaunch 12 March, Base relaunch 17 March, Hacken and Halborn audits published, 45-day goodwill claims process from 11 March for **180 affected addresses across 7,000+ trades**.

**Three lessons, all of which transfer.**

1. **"Legacy code" means the 2022-era contract carried a latent flaw for over three years.** The relaunch bolted a new bridge onto old code. **The audits came after the exploit, not before.** For Aurumix: audit before deploying, and re-audit specifically at the seam whenever new infrastructure is attached to existing contracts.
2. **The property-law structure held under live stress.** 100 million fake tokens existed and **the gold was never at risk**, because the fake tokens conferred no co-ownership in anything. Token supply and gold title are separate legal facts. This is a real vindication of the §2 structure, tested in the wild rather than argued on paper.
3. **The issuer took the loss and disclosed it.** GTSA absorbed ~$250k because it was the market maker, published a detailed report a month later, and ran a claims process. **Compare PMGT, whose issuer edited the stated reason for its exit.** This is the best incident disclosure in the landscape set.

## 9. Liquidity and market

Per the wave-1 addendum, the premium thesis is settled, so this is one paragraph of data.

**~$8.1M AUM / ~2,005 tokens. Daily volume ~$12k–19k.** Liquidity sits in three pools: Uniswap V4 DGLD/USDC (~$9.4k daily) and DGLD/XAUT (~$9.4k) on Ethereum, and Aerodrome/Uniswap DGLD/USDC on Base (~$27). Monthly transfer volume ~$3.8M across 3,323 transfers, ~113 active addresses. Price **$4,045–4,081** against LBMA/spot gold of **~$4,004 (LBMA PM, 20 July 2026) to ~$4,090 (spot, 27 July 2026)**. **DGLD trades at or marginally below spot: no premium.** Turnover is roughly **0.2% of AUM daily**, thin even by this set's standards, and the market is sustained by MKS PAMP's own trading arm plus **Arrakis Finance**, which actively manages the Aerodrome position around the real-world gold price to minimise slippage.

**One more data point for the settled conclusion, from a new angle: a professionally market-made, vertically integrated, refinery-owned gold token with a 1-gram redemption right still trades at no premium.** Note also that holder count is rising fast (+32.5% in 30 days) while volume stays tiny, which says accumulation, not trading.

**Flagging a contradiction for the record:** a Sonar Pro response in this research asserted DGLD trades at a "significant premium," derived by comparing DGLD's live ~$4,166 price against a **stale ~$2,400/oz gold price from model memory**. Gold is ~$4,000–4,090/oz in July 2026. **The premium was an artefact of an out-of-date gold price, not a market observation.** Recorded because the same error would be easy to repeat elsewhere in this landscape.

## 10. Distribution

- **Channels:** DEX only for retail (Uniswap V4 on Ethereum, Aerodrome on Base). Direct primary issuance to accredited institutions. Previously listed on **Bitstamp** during the Ethereum era.
- **Target segments:** explicitly, per CEO James Emmett, **crypto-wealthy individuals** ("If you've made your money in crypto, you're very keen on having tokenized gold" and want to "stake it or leverage it") and institutional funds.
- **Geography:** Switzerland-issued, global secondary access, **EU/EEA expressly not solicited**.
- **Savings plan / SIP / recurring purchase:** **None found.**
- **Referral / affiliate / agent network:** **None found.**
- **Commission structure:** **None found.**

**Direct answer to design question 8: DGLD has no distribution mechanism of the kind Aurumix is building.** Its strategy is to be liquid where crypto capital already is (Base has ~8M monthly active users) and to let market makers do the work. It is a **liquidity-placement** strategy, not a **customer-acquisition** strategy.

This is now the near-universal finding across the set, and DGLD sharpens it: an issuer with 60 years of brand, its own refinery, its own vaults, and a genuinely best-in-class redemption right has accumulated **~$8M**. It has no mechanism to reach a saver who does not already hold crypto. **The distribution gap Aurumix is targeting is real, and DGLD is further evidence that incumbents with every asset advantage are not addressing it.**

## 11. Recent developments (dated, reverse chronological)

**28 July 2026 (today):** DGLD live and trading. ~2,005 tokens, ~$8.1M, both chains operational post-redeployment. Holder count +32.5% over 30 days. Redemption path advertised as live at 1 gram.

**21 March 2026:** GTSA publishes the [post-incident report](https://dgld.ch/news/post-incident-report-february-2026-exploit) on the February exploit. Confirms **Hacken and Halborn** audits complete with no remaining critical or high findings, and that full audit reports were released.

**17 March 2026:** Base contract relaunched.

**12 March 2026:** Updated Ethereum contract relaunched.

**11 March 2026:** Pre-exploit balance reset executed. 45-day goodwill claims process opens for **180 affected addresses across 7,000+ trades**.

**23 February 2026:** **Exploit.** Legacy `transferFrom` edge case abused via the Ethereum↔Base bridge to mint **>100 million unbacked DGLD on Base**. Contracts paused within ~2h25m. Impact **~$250k**, mostly borne by GTSA as principal liquidity provider. **Physical gold unaffected; pre-exploit holders unaffected.**

**12 January 2026:** Swiss register records current board composition: **James Emmett (President), Kurt Hemecker, Roman Peter Schnider** ([NorthData](https://www.northdata.com/Gold%20Token%20SA,%20Carouge/CHE-287.630.262)).

**16 December 2025:** **DGLD launches on Base via Aerodrome**, with liquidity managed by **Arrakis Finance** ([PR Newswire](https://www.prnewswire.com/news-releases/dgld-the-only-gold-token-backed-by-60-years-of-swiss-precious-metals-heritage-launches-on-base-network-via-aerodrome-302643330.html)). Kurt Hemecker named as **CEO of Gold Token SA**.

**20 November 2025:** **MKS PAMP SA acquires full ownership of Gold Token SA.** CEO **James Emmett** tells Bloomberg the 2019 launch was "too early" and that the token had been **mostly dormant for six years**. Relaunch model: MKS PAMP's trading arm buys tokens and provides exchange liquidity; issuance restricted to accredited institutions ([swissinfo/Bloomberg](https://www.swissinfo.ch/eng/digital-gold-wave-prompts-swiss-trader-mks-pamp-to-revive-token/90395956)).

**19 November 2025:** GTSA publishes its [step-by-step guide](https://dgld.ch/news/dgld-complete-step-by-step-guide-november-2025) covering purchase, per-bar verification and 1-gram physical redemption.

**30 July 2025:** GTSA announces physical delivery **from just one gram**.

**26 May 2025:** Registered seat moves from Geneva to **Carouge GE**.

**11 April 2024:** Share capital **reduced** from CHF 4,668,500 to **CHF 3,401,100**. A capital reduction during the dormant period is consistent with returning capital as the venture wound down in substance.

**~2022–2025: dormancy.** No material announcements. Volume and attention negligible.

**November 2022:** DGLD **migrates from the Ocean Bitcoin sidechain to Ethereum** as a native ERC-20. Original sidechain DGLD ceases to exist; `wDGLD` replaced by the new token.

**November 2020:** **`wDGLD` launches on Ethereum**, a wrapped ERC-20, as Blockchain.com extends its partnership with CoinShares. **The sidechain strategy is effectively conceded ~13 months after launch.**

**October 2020:** Last commit to the `ocean-wallet` and `config` repos ([GitHub](https://github.com/goldtokensa)). Sidechain tooling abandoned.

**September 2020:** Consortium announces physical bullion redemption for DGLD ([PR Newswire](https://www.prnewswire.com/news-releases/coinshares-dgld-consortium-allows-investors-to-redeem-gold-tokens-for-physical-bullion-301152528.html)).

**15 October 2019:** **DGLD launches** on the **Ocean Bitcoin sidechain** (CommerceBlock, Liquid codebase), by **CoinShares International, MKS SA and Blockchain.com**. ~$20M of gold, vaulted at PAMP. **1 DGLD = 1/10 troy ounce** at launch.

**8 August 2018:** **Gold Token SA incorporated**, Geneva, CHE-287.630.262.

### What happened to the original backers

**CoinShares and Blockchain.com are both out.** Neither appears in any GTSA material after the November 2025 acquisition, and MKS PAMP now holds **100%**. **No exit announcement, date or terms were published by any party. Confidence on the fact of exit: High** (MKS PAMP owns the whole company). **Confidence on when and how: Not disclosed.** The 11 April 2024 capital reduction is the only dated public trace of the ownership unwinding, and it is circumstantial.

### Was there a wind-down plan? Yes, and this is the exception in the set

**DGLD is the first protocol we have profiled that publishes an ex-ante wind-down clause.** Verbatim from the [T&Cs](https://dgld.ch/legal/general-terms-conditions-dgld-2):

> "If the operation of the Platform is terminated (for any reason), GTSA will inform the Tokenholders of such termination via the GTSA website. Thereafter, each Tokenholder shall choose one of the following options: requesting the Delivery as described in Section 8; or instructing GTSA to sell the Gold represented by the DGLD at its own discretion and to distribute the remaining net proceeds of sale, after deduction of any applicable fees, costs, charges and expenses incurred in connection with such sale, to the Tokenholder. If GTSA does not receive an instruction from the Tokenholder within 2 months of the communication on the GTSA/DGLD website mentioning the termination of the Platform, GTSA reserves the right to proceed with a sale according to the second option above."

**This directly contradicts the brief's claim that "no failed gold token published a wind-down plan," and the contradiction should be recorded loudly.** DGLD did publish one, before the fact, in its binding terms. It is not merely a continuity assurance of the PMGT one-sentence type: it specifies notice, a holder election, two named options, a deadline and a default.

**Now grade it honestly, because it is good but not a model to copy wholesale:**

*Strengths:* holders get a **genuine election**, and critically **physical delivery is one of the two options**, so a holder can exit into metal rather than being force-converted. There is a **defined 2-month window**. The default is stated in advance rather than improvised.

*Weaknesses, and they are the same ones that stranded PMGT holders:*
- **Notice is by website only.** No email, no on-chain notice, no registered communication. **PMGT's entire lesson is that issuer websites do not survive the issuer.** A holder who stops checking `dgld.ch` for two months is force-sold. Given DGLD sat dormant for six years, "check the website" is a demanding assumption.
- **"Sell the Gold... at its own discretion."** No pricing methodology, no reference fix, no requirement to sell at or near the LBMA price. Compare PMGT's force-sale, which was benign only because gold happened to be rising.
- **"After deduction of any applicable fees, costs, charges and expenses."** Uncapped and unquantified. Same reappearing-fees pattern PMGT displayed at exit.
- **No trigger definition.** "Terminated (for any reason)" is entirely at GTSA's option. No insolvency trigger, no minimum-AUM trigger, no notice period before termination is declared.

**Net: the best wind-down clause in the set, and still deficient in exactly the ways that matter most.** That combination is what makes it valuable to Aurumix, because it maps the gap precisely.

## 12. Relevance to Aurumix

### The headline finding: dormancy is survivable, and the reason is structural

The task asked whether DGLD had quietly died and, if so, to profile it as a failure. The accurate answer is more useful than either alternative: **DGLD died commercially and then recovered, and the recovery was possible because of decisions made at launch.**

Six years dormant. Backers gone. Capital reduced. Then bought and restarted. Now compare **PMGT**, which under the same commercial pressure was switched off permanently, and **Cache Gold** and **Digix**, which wound down. What made DGLD recoverable when they were not?

1. **The gold was never encumbered or dissipated**, because holders owned it outright at law. There was no unwinding problem: dormant DGLD was just gold sitting in a vault with valid title. A restart required no one's permission.
2. **The custodian and the issuer ended up as the same economic group.** MKS PAMP could buy the whole issuer and instantly own the full stack.
3. **The token never lost its backing during dormancy**, so old holders were not wiped out and the brand was not poisoned.

**The transferable lesson: a gold token's survivability is determined by whether the gold's legal position is independent of the operating company's fortunes.** DGLD's arts. 646/919 co-ownership meant six years of corporate neglect did not damage holders. **Aurumix should ask, of its own structure: if the operating company goes quiet for three years, what happens to the gold and to holders?** If the answer depends on Aurumix being an operating, solvent, willing counterparty (and with cash-buyback-only exit it currently does), then Aurumix has PMGT's fragility, not DGLD's resilience.

### Answers to the live design questions

**Q2, dividend funding. DGLD is a clean negative data point, and a useful one.** It pays **nothing**, and its T&Cs go out of their way to disclaim "any financial return, interest, dividend, claim for repayment." That disclaimer is not accidental. It is what lets GTSA characterise DGLD as **property (a title of proof under art. 8 CC) rather than a financial claim**, which is precisely what keeps it outside securities and collective-investment regulation and lets it live on an SRO affiliation instead of a FINMA licence. **The most sophisticated legal structure in the set bought its regulatory simplicity by disclaiming yield.** Aurumix's ICS Dividend is the exact feature DGLD deliberately refused. That does not make it wrong, but it prices it: **the dividend is what converts a property instrument into a financial one, and the hybrid-regulation problem follows from that single choice.**

**Q3, token standard.** Plain ERC-20, freely transferable, no permissioning. It works for DGLD **only because the token carries no rights that break on anonymous transfer**: co-ownership travels with the token, and there is nothing else attached. The T&Cs even construct transfer as a property-law conveyance with the custodian deemed notified by the chain state. **This is the cleanest illustration of the principle behind Aurumix's ERC-3643 lean.** DGLD can be a permissionless ERC-20 precisely because it has no ICS standing, no dividend entitlement, no credit eligibility. Aurumix has all three, so it cannot copy this. **The rule: permissionless works if and only if the token's entire content is transferable property.**

**Q5, redemption.** Covered in §6. **1 gram, 0.20%, KYC only at delivery, eligibility by control of tokens.** This is the benchmark Aurumix's no-redemption model will be measured against by any sophisticated reader, and Aurumix should meet the comparison head-on rather than implying redemption is generally unavailable in this market.

**Q7, proof of reserve.** DGLD offers **per-wallet, serial-number-level bar verification**, which is more useful to a retail holder than a quarterly aggregate PDF. **But it is issuer-published, and we could not confirm any named third-party attestor** (the KPMG reference is single-sourced to rwa.xyz and unconfirmed by GTSA). **Recommendation: Aurumix should copy the per-holder bar lookup, which is a real differentiator and cheap, and additionally commission the named attestation DGLD appears to lack.** Doing both is a defensible market-leading position.

**Q8, distribution.** No SIP, no referral, no agent network, no recurring purchase. §10.

**Q9, wind-down.** DGLD **has a published clause**, contradicting the brief. §11 grades it. **Aurumix can beat it cheaply on four specific points**, which is the most actionable output of this profile:

- [ ] **Notice by durable channel, not website.** Email plus on-chain notification plus a durable artefact (IPFS, registry filing). DGLD's website-only notice would have failed during its own dormancy.
- [ ] **A stated pricing methodology for any forced liquidation.** DGLD sells "at its own discretion." Aurumix should pre-commit to a reference fix (e.g. LBMA PM on a defined date) so the price is not the issuer's choice.
- [ ] **A cap on wind-down fees.** DGLD deducts uncapped "fees, costs, charges and expenses." Both DGLD and PMGT reappear with unquantified exit fees after advertising low or zero fees during life.
- [ ] **Defined triggers.** DGLD's termination is "for any reason," at will. Aurumix should define what events start the wind-down, and a minimum notice period before the election window opens.

### Two further transfers

**1. "Regulated in Switzerland" is a halo, and it degraded within one hop.** GTSA says "regulated through VQF, a FINMA-supervised SRO," which is true. rwa.xyz renders this as "supervised by FINMA," which is false. **VQF affiliation is AML self-regulation, not a licence, and involves no product approval or prudential oversight.** This is the same pattern as PAXG's stale NYDFS claim and the "audited" conflation: **a technically accurate issuer statement engineered to be misread, then misread.** Aurumix will face the identical temptation with VARA and ADGM terminology. Note also the parallel to Comtech: where Comtech had an unlicensed gap, **GTSA's registered corporate purpose expressly authorises commodity-backed token issuance**, so it is lawfully doing what it says. The gap is prudential, not existential.

**2. The chain choice cost roughly three years and the category lead, but it was not the cause of death.** PAXG launched about a month before DGLD with comparable custody, chose Ethereum, and is ~220x larger. That is the cost of the sidechain (§8). **But DGLD migrated to Ethereum in 2022 and stayed dormant three more years anyway.** Correct infrastructure was necessary and nowhere near sufficient. What revived it was an owner with a commercial reason to push. **For Aurumix: infrastructure choices set your ceiling, but a committed distribution owner determines whether you approach it.** This reinforces the PMGT lesson from the other direction. PMGT had no revenue line and therefore no internal advocate, and died. DGLD had no advocate for six years and merely slept, because its structure let it sleep. **Aurumix needs both: a structure that survives neglect, and a P&L that prevents it.**

## 13. Open items for verification

- [ ] **Confirm or kill the KPMG reserve attestation.** Named on [rwa.xyz](https://app.rwa.xyz/assets/DGLD), unconfirmed by any GTSA source and not found by dedicated search. Establish whether KPMG performs a **reserve attestation of the gold** or merely a **statutory financial audit of Gold Token SA**, and obtain a dated report. This is the single most important open item, since it decides whether DGLD's reserve verification is genuinely independent or issuer-published only.
- [ ] **Obtain the Hacken and Halborn audit reports.** Stated as publicly released in the March 2026 incident report but not located. Confirm scope, dates, and specifically whether the bridge was in scope.
- [ ] **Verify the 400 XAU (~$1.6M) minimum subscription** against a GTSA primary document. Currently single-sourced to rwa.xyz and absent from the published T&Cs.
- [ ] **Confirm whether Utila Inc provides token-infrastructure custody**, and obtain the admin-key/multisig architecture for both contracts. Given GTSA demonstrated power to pause, redeploy and reset balances, the key-control model is material.
- [ ] **Establish the legal basis for the "bankruptcy-remote" claim.** Obtain any legal opinion citing the Swiss DLT Act / DLT-TEF or **art. 242a DEBA**. The T&Cs rely on arts. 646/919 CC without an express insolvency recital.
- [ ] **Determine what "storage and administration costs embedded in DGLD" means operationally.** Specifically: is any cost recovered from the gold backing, which would push the ounce-per-token ratio below 1? Request the ratio history since November 2022.
- [ ] **Obtain the VQF membership number** for Gold Token SA and confirm it against the VQF member register.
- [ ] **Establish when and on what terms CoinShares International and Blockchain.com exited.** No public announcement located. Check CoinShares' annual reports and any disclosure around the 11 April 2024 capital reduction.
- [ ] **Test the redemption path end to end.** Email `support@dgld.ch` requesting a 1-gram quote to a non-EU address and record the actual quote, KYC burden, total landed cost and delivery time. This is the highest-value practical test for benchmarking Aurumix's exit design, and it is cheap.
- [ ] **Confirm whether a holder can compel delivery of a specific serial-numbered bar**, or only of an equivalent quantity from the pool. The verify tool implies specificity; art. 646 co-ownership implies a pool.
- [ ] **Obtain the outcome of the 45-day goodwill claims process** (opened 11 March 2026, ~180 addresses): how many claimed, how much was paid, and on what basis.
- [ ] **Verify current DGLD supply and per-chain split directly on Etherscan and Basescan** rather than via aggregators, given the March 2026 contract redeployment means older addresses and supply figures may be stale.
