# Protocol Landscape: Researcher Brief (WORKING FILE, not a deliverable)

You are researching **one** tokenized-gold protocol and producing **one** profile section for `Aurumix_Protocol_Landscape.md`. Another agent is doing the same for each of the other protocols. Stay in your lane: research your assigned protocol only.

---

## PART 1: TOOLING RULES (read these first, they are not optional)

A previous batch failed because of the first two rules. Follow them exactly.

Load the research tool with:
`ToolSearch` → query `select:mcp__openrouter__chat_completion`

Then call `mcp__openrouter__chat_completion` with `model: "perplexity/sonar-pro"`.

1. ⛔ **NEVER pass `max_tokens`.** Omit the parameter entirely. Passing it returns `Cannot read properties of undefined (reading '0')` and the call dies.
2. ⛔ **NEVER use `perplexity/sonar-deep-research`.** Standing decision. Sonar Pro only.
3. ⛔ **NEVER call `validate_model`.** It returns false negatives. Call the model directly.
4. ⚠ **The MCP strips the citations array.** Bare `[1][2]` markers in a response resolve to NOTHING. Every prompt you write must end with:
   > "Put a source URL inline immediately after each individual claim, not as an end-of-answer list. If something cannot be found, say 'not found' explicitly rather than inferring it."
   If a response comes back with bare bracket numerals and no URLs, **re-run it**. Do not carry unresolvable citations into your output.
5. **Cost is controlled by instruction, not parameters.** Add "answer in under 900 words, no background or history sections" to your prompts.

### Research method (learned the hard way, do not skip)

6. **Registry first, marketing last.** Before any Perplexity query, use `WebFetch` and `WebSearch` to pull:
   - the **company registry record** for the issuer (jurisdiction, registration number, incorporation date, activity code)
   - the protocol's own **terms of issue / terms of use** page
   - its **transparency / proof-of-reserve** page
   This is free and it is the highest-value step. A protocol we had documented as Emirati across an entire research pass turned out to be a Singapore holding company; the error survived every secondary source and collapsed in one minute against a registry. **Whatever the marketing says about jurisdiction, verify it against a register.**
7. **Never embed the fact you are testing.** Ask "what is the current X", never "it reportedly uses X, confirm".
8. **Never use negative source-exclusion lists** ("do not rely on CoinGecko..."). It causes the model to stop searching entirely and reply that it has no web access. Steer positively instead: "prioritise the issuer's own terms and docs, the company registry, regulator registers, audit reports, and dated news coverage."
9. **Always run a dedicated recency sweep as its own query:** state that today is 28 July 2026 and ask for all announcements, migrations, incidents, partnerships and enforcement actions in the last 18 months, reverse chronological, dated.

### Budget

Roughly **2 to 4 Sonar Pro queries** per protocol. Suggested sequence:
1. Identity and legal: issuer entity, jurisdiction, registration number, regulator and licence number, what documentation exists (with direct URLs).
2. Mechanics: backing, custody, proof of reserve, issuance, redemption, fees, token standard and contract addresses.
3. Recency sweep (see rule 9).
4. Only if needed: one follow-up on whatever is still unresolved.

---

## PART 2: WHAT TO PRODUCE

Write **one markdown file** to the path given in your task prompt. Start at `# <Protocol Name> (<TICKER>)` as an H1. Do not add a document title, preamble, or "how to read" section: those live in the assembled document.

### Confidence labels (use these exact words)

| Label | Meaning |
|---|---|
| **Confidence: High** | Primary source: issuer terms, prospectus, audit report, corporate registry, or on-chain contract. |
| **Confidence: Medium** | Issuer marketing or a credible secondary source, with no primary document confirming it. |
| **Confidence: Low** | Fragmentary or contested. A lead to verify, not a fact to cite. |
| **Not disclosed** | We looked and found nothing. **This is a finding in its own right and is NEVER filled with a plausible assumption.** |

**Anything a competitor asserts about itself is reported as an assertion, not adopted as fact. Where marketing and legal documents disagree, show both.** That gap is often the most valuable thing in the profile.

### Required structure

An **At a glance** table first, then 13 numbered sections. Keep the section names and order exactly as below.

```
# <Name> (<TICKER>)

## At a glance
| Field | Value | Confidence |
(rows: Ticker, Issuer (marketing), Issuer (registry), Domicile, Backing claim,
 Chains, Contract address(es), Supply, Market cap / TVL, Regulatory status,
 Subscription fee, Ongoing custody fee, Redemption fee, Advertised yield,
 Named officers. Add or drop rows where the protocol warrants it.)

## 1. What it is
## 2. Legal structure          <- what does a holder actually OWN? title, trust, creditor claim, or nothing?
## 3. Regulatory and compliance posture   <- name regulator + licence number, or list what you checked and did not find
## 4. Custody and proof of reserve        <- table: custodian, vault/city, allocated?, bar list, PoR feed, reserve audit, smart contract audit
## 5. Issuance
## 6. Redemption
## 7. Fees and revenue model    <- table of fee lines
## 8. Token architecture        <- standard (ERC-20 / ERC-3643 / other), permissioned?, upgradeability, admin keys, bridge
## 9. Liquidity and market
## 10. Distribution             <- channels, target segments, geography, referral/affiliate/savings-plan features
## 11. Recent developments      <- dated, reverse chronological, from your recency sweep
## 12. Relevance to Aurumix     <- see Part 3. This is the section that earns the document.
## 13. Open items for verification   <- `- [ ]` checkboxes, specific and actionable
```

For a protocol that has **failed or wound down**, keep the same structure but make §11 a dated wind-down timeline and use §12 to draw the lesson.

### House style

- **No em dashes.** Use colons, sentence splits, parentheses. En dashes in numeric ranges (3–8%) are fine.
- Notion-importable markdown: GFM tables, `- [ ]` checkboxes, **no HTML**.
- Plain language, decision-driven, reasoning shown. Write for a sharp reader who will ask follow-ups.
- **Absence of information is a finding.** Write "Not disclosed" and move on. Never pad with a plausible assumption, and never soften a gap into a maybe.
- Put real URLs inline where a claim needs backing. Never emit a bare `[1]` marker.

---

## PART 3: THE CLIENT, SO §12 IS USEFUL

**Aurumix** is a pre-build UAE (Dubai) gold-backed retail savings product. 100% of every dollar buys physical LBMA gold. Token price = vault gold × LBMA fix ÷ tokens, currently 1 AURX = 0.01 g, no hard cap. Its distinguishing feature is that it is a **savings plan**, not a custody receipt: a monthly SIP (systematic investment plan, $20 min / $75 target), modelled on Indian life-insurance premium schedules and sold through a **3-tier agent network**. Target markets are India, the UAE and NRIs.

Around the gold core it layers: an **ICS (Investor Conviction Score)** with 7 tiers governing allocation priority and spot access; an **ICS Dividend** paying 15–20% of operating profit with 80% going to the top 10% of holders; a **credit facility and Gold Card** at 90–95% LTV; a **Family Portfolio and Digital Will**; and **no physical redemption at all** (exit is cash buyback only, deliberately, for retention and credit revenue).

### The nine live design questions. Address any your protocol speaks to. Say so plainly if it speaks to none.

1. **Custody fee mechanism.** Deducting the fee in grams breaks the peg (price = grams ÷ tokens). We lean toward charging in cash. A third option exists: charge holders nothing and recover cost elsewhere. **What does your protocol actually do, and what funds it?**
2. **Dividend funding.** Our biggest open problem. A dividend funded from investor fees is both a weak value story and a securities-classification risk. Real external asset yield (e.g. gold leasing) is the compliant alternative, but it encumbers the gold. **Does your protocol pay yield, and can its disclosed sources plausibly fund what it promises?** If they cannot, say so with the arithmetic.
3. **Token standard.** Aurumix's token carries ICS standing, dividend entitlement, credit eligibility and buyback rights, all of which break on an anonymous DEX transfer, so we lean to a permissioned base (ERC-3643) with an optional ERC-20 wrapper. **What standard does your protocol use, and what does that choice cost or buy it?**
4. **Regulatory route.** The gold core is a clean ARVA under VARA, but the dividend and credit make it a hybrid, triggering dual regulation that fights the mass-retail model. VARA is expensive (~AED 100k application, 200k/yr supervision, min capital AED 1.5M, 6–9 months). **Which regulator and licence does your protocol actually hold, verified against a register?** A Dubai or UAE protocol operating without VARA is a highly material finding: document the exact licence it uses instead.
5. **Redemption.** Aurumix offers no physical redemption, which is a real gap against its "you own physical gold" pitch. **What are your protocol's redemption terms, minimum increments, fees, and who is eligible?** Watch for eligibility limited to undefined "qualified holders".
6. **Premium and liquidity.** The client is banking on a 3–8% exchange premium to sustain demand. **What is your protocol's AUM against its actual on-chain liquidity and daily volume?** Accumulating assets and having a market liquid enough to produce a reliable premium are separate problems.
7. **Proof of reserve.** **Is there a real reserve attestation, a published bar list, a PoR feed, and at what frequency?** Distinguish sharply between a **smart-contract audit** and a **reserve attestation**: issuers routinely blur these, and a reader skimming "audited" draws the wrong conclusion.
8. **Distribution.** Aurumix sells through a commission-based agent network with recurring contributions. **Does your protocol have any savings-plan, recurring-purchase, referral or affiliate mechanism?** Most do not, which is itself the finding.
9. **Wind-down.** No failed gold token published a wind-down plan. Aurumix committing to one ex ante is cheap differentiation. **Does your protocol document what happens to the gold if the issuer fails?**

### Already established, so do not re-derive (but flag any contradiction you find)

- **PGOLD** advertises 5% yield on ~$79–90M funded from redemption fees plus a market trading under $20 a day. The disclosed sources cannot fund the promise. Live example of the recycled-fees anti-pattern.
- **PGOLD** holds ~$79–90M of AUM with ~$1.7M liquidity and sub-$20 daily volume: evidence against the premium thesis.
- **ORO** is **Oro Labs PTE Ltd, UEN 202434484G, incorporated 22 August 2024 in SINGAPORE**, not Dubai. Unlicensed everywhere. Its terms disclaim issuance to unnamed "Third-Party Service Providers". Advertises 3–4% APY from Monetary Metals gold leasing with nothing published on how holders rank if the counterparty defaults. ORO, Oro Finance, ORO Labs, orogold.com and the rwa.xyz "Orogold" Solana GOLD listing are all **one project**.
- **PMGT** died of adjacent risk (AUSTRAC AML enforcement against Perth Mint plus the Shanghai Gold Exchange doping scandal), not token defect. **Digix** dissolved its DAO via a structured treasury return while DGX went illiquid. **Cache Gold** wound down quietly. None published a wind-down plan.

**If your research contradicts anything in this brief, say so explicitly and loudly in your profile.** Surfacing a contradiction is worth more than a clean profile. We have already been burned once by inherited framing that no secondary source questioned.

---

## PART 4: ADDENDUM FROM WAVE 1 (read this, it changes what is worth your time)

Nine profiles are complete: PAXG, Kinesis, Matrixdock XAUm, Comtech CGO, Tether XAUT, VNX VNXAU, Aurus TXAU, ORO, PMGT. Registry checks contradicted **three** of our own standing conclusions and one widely repeated fact about the largest issuer in the set. Assume nothing you inherit is safe.

### Settled. Do not spend queries re-establishing these.

- **Question 6, the premium thesis, is answered and it is dead.** Eight protocols now say the same thing from opposite ends of the liquidity spectrum: PGOLD (~$79M AUM, sub-$20 daily volume, no premium), PAXG (~$1.79bn, 5.9% turnover, trades at par), XAUT (~$2.46bn, ~5.3% turnover, trades at gold), XAUm (0.76% two-way primary spread caps it), VNXAU (~0.7% over spot), Comtech (parity, 0.42% spread), Aurus (arbitrage structurally caps at NAV + 0.5%), ORO (trades at a slight **discount** on a 33% liquidity-to-AUM ratio). **A liquid gold token cannot sustain a premium because arbitrage kills it, and an illiquid one has no market to express one.** Report your protocol's AUM, on-chain liquidity, daily volume and price against spot as one more data point, in one short paragraph. Do not re-argue the conclusion.
- **Question 1, the custody fee, is answered.** Zero ongoing custody fee is the near-universal norm (PAXG, XAUT, Kinesis, XAUm, VNXAU, Comtech, Aurus, PGOLD all charge holders nothing). Just record what your protocol charges and what funds it. The interesting cases are the funding mechanism and any reserved right to start charging later.

### Live leads. If your protocol touches one of these, chase it hard: it is worth more than the rest of your profile.

- 🔴 **STREAMEX: the highest-value single lead in the batch.** Monetary Metals has an actual **gold lease agreement with Streamex filed with the SEC**, reportedly carrying 110% jeweller's block insurance with Monetary Metals as loss payee. We had concluded that **no properly documented real-yield gold-leasing precedent exists anywhere**, and closed the question on that basis. If this filing is real, that conclusion is wrong and this is the documented precedent our client's entire dividend design has been missing. **Pull the actual SEC filing.** Get the agreement text, the insurance terms, and above all **how token holders rank if the lessee defaults**. Note the live stress test: the **AgaBullion lessee defaulted on 26 January 2026**, Turkish authorities seized leased gold, and Monetary Metals' remedy was Istanbul counsel plus an insurance claim. So "title remains with the lessor" means "we will litigate abroad." Establish whether Streamex's paper is better than that.
- **ADGM "Accepted Spot Commodity" route.** Surfaced as a possible cheaper alternative to a VARA licence, reportedly used in July 2026. If your protocol has any UAE nexus, check whether it uses this and what it requires.
- **The instrument split (from Kinesis).** Kinesis keeps its gold token clean and sells the revenue share as a **separate capped security** (KVT: 300k cap, 20% of fees, private placement under an Offering Memorandum). This is currently our leading structural answer to the hybrid-regulation problem. If your protocol separates a yield or governance instrument from the asset token, document the split precisely.
- **The dilution-by-minting fee clause (from PAXG).** Paxos reserves the right to take its storage fee by **minting new tokens to itself pro rata** rather than charging cash. Peg-breaking for a 1-token-1-ounce product, but **peg-neutral for Aurumix** whose peg is grams ÷ tokens. If your protocol has any similar in-kind or dilutive fee mechanism, quote the exact clause.

### Corrections established in wave 1. Use these, and flag any further contradiction.

- **PAXG is regulated by the OCC, not NYDFS.** Paxos converted to a national trust bank charter on 12 December 2025. Paxos's own transparency page still says NYDFS, so the stale fact keeps propagating. Treat any "NYDFS-regulated" claim about Paxos as out of date.
- **Comtech is licensed by DAFZA, not DMCC.** ComTech FZCO holds Dubai Airport Free Zone licence 05069 for precious-metals trading. A separate ComTech FZCO (DMCC) licence covers **IT and software consultancy only**. Neither permits public token issuance, and both display as expired. **There is no lawful "Dubai route around VARA": there is an unlicensed gap.** Our earlier DMCC hypothesis is dead.
- **PMGT was not killed by AUSTRAC.** The Perth Mint began exit discussions in early 2022, before any public AUSTRAC action. The AUSTRAC enforceable undertaking concluded 22 July 2025 with the Mint cleared and **no fine ever imposed**. PMGT died of **commercial abandonment**: zero fees meant zero revenue and no internal advocate. If you are profiling a failure, test for this pattern rather than assuming enforcement.
- **Kinesis's fee-funded yield paid ~0.10% annualised** ($26,326 in June 2026 on $310M AUM) against advertised figures ~20x higher. Any protocol advertising a yield: **do the arithmetic against its actual disclosed revenue and say whether it can possibly fund the promise.**
- **"Audited" almost always means smart-contract audited, not reserve attested.** This has now caught us out on four protocols. Separate the two explicitly in §4, every time.
