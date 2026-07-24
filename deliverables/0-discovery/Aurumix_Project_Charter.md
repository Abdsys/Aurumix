# Aurumix Project Charter

**Prepared by:** Tokenomics.net
**Kickoff date:** 24 July 2026
**Charter version:** 1.0
**Status:** Draft for client review

---

## Problem Statement

Aurumix is a gold-backed systematic savings platform issuing a VARA-regulated token (AURX) in Dubai, targeting long-term retail savers in India and the UAE rather than crypto-native users. The authoritative specification is the **100 G Business Model (Version 3)**, in which every dollar received buys physical LBMA gold. This replaced an earlier design that split capital 70/30 between gold and an algorithmic growth pool.

> **Terminology note.** "Version 3" is the client's own label on the 100 G Business Model document. It should not be confused with the term "V3" used in the earlier model and in our engagement brief, where V3 referred to the third component of a pricing formula (the Target Alignment Multiplier). That pricing formula no longer exists. This charter uses "the 100 G Business Model" throughout.

The engagement exists because that shift resolved one set of problems and opened another:

- **The economic engine changed but the surrounding mechanics did not.** The token price is pure gold, so several mechanisms inherited from the previous model (most visibly the Mining Event and oversubscription framing) no longer perform the economic function they were designed for and need either re-justification or replacement.
- **The Investor Conviction Score (ICS) is load-bearing but unbuilt.** ICS governs four separate things: allocation priority, spot market access, credit ratio, and dividend share. The tiers and component list exist; the actual scoring formula does not.
- **The dividend has no external funding source.** The ICS Dividend is paid from operating profit, but that profit is currently just fees collected from investors. As designed it recycles investor money and concentrates it in the top 10 percent, which is both a weak value proposition and a securities classification risk.
- **Classification risk sits on the critical path.** The gold core is a clean ARVA under VARA, but the dividend and credit facility push AURX toward a hybrid classification and potential dual regulation. Under the UAE framework, misclassification forces a full structural rebuild, so this must be settled before design is finalised.
- **Fee mechanics conflict with the peg.** The current design deducts custody fees in grams, which mechanically breaks the fixed grams-per-token peg the entire product promise rests on.
- **The build is already moving.** Design and front-end development are expected to complete in early September, with API integration and back-end partnerships following. The economic specification needs to land in time to inform that build rather than retrofit it.

---

## Project Objectives

- Establish a defensible regulatory classification for AURX under the UAE framework, and structure the token so the gold core stays within the retail-friendly ARVA perimeter.
- Close every open mechanism, formula, and threshold in the 100 G Business Model into a specification the development team can build against.
- Design the ICS scoring system end to end: components, weights, tier thresholds, decay on missed contributions, and caps.
- Resolve the custody fee mechanism so fee collection never compromises the grams-per-token peg.
- Identify and design additional revenue streams so the ICS Dividend is funded by genuine external value rather than recycled investor fees.
- Build a revenue model covering fee income, credit and card economics, agent network commission, and fixed costs through to net profit.
- Determine what share of net profit is required to deliver the client's target uplift on gold returns for their top investor cohort.
- Simulate the model across scenarios to establish where the design holds and where it breaks, particularly around spot capacity, secondary market premium, and credit liquidation.
- Produce documentation sufficient for VARA review, exchange listing diligence, and investor conversations.

---

## Deliverables

### Phase 0: Discovery (complete)

- Kickoff questionnaire and client responses
- Consolidated questions and decisions log
- This project charter

### Phase 1: Market Research (complete)

- Competitive landscape report across ten research tracks, quality-checked, with confidence tags
- Direct comparable analysis including ORO (Dubai gold token with external yield), PAXG, Tether Gold, and Kinesis
- Precedent to mechanism mapping, so each later design block draws on evidence rather than assertion
- Regulatory positioning review across VARA, LBMA, and cross-border considerations

### Phase 2: Mechanism Design (next)

Closed-form mechanism design document plus supporting process maps, covering:

- Token classification and architecture, including token standard and the permissioned versus permissionless trade-off
- Token denomination and unit design
- SIP structure: contribution commitment, lock terms, grace and revival mechanics
- The ICS scoring system, fully specified and calibrated
- Spot market capacity allocation and lane structure
- Custody and entry fee mechanics, designed to preserve the peg
- Credit facility mechanics: LTV bands by tier, warning and liquidation thresholds, repayment structure
- Dividend design and its funding source
- Agent network economics and structure
- Family portfolio and digital will mechanics
- Treasury, liquidity, and OTC lane design

### Phase 3: Supply Side Tokenomics

- Supply and issuance model appropriate to an uncapped, gold-backed token
- Circulating supply trajectory under each growth scenario
- Free float analysis across SIP-locked, credit-pledged, and freely tradeable supply
- Secondary market liquidity plan and slippage tolerance sizing
- Supply-side workbook

### Phase 4: Revenue and Economic Modeling

- Model architecture brief
- Formula-driven Excel revenue model covering all fee lines, credit and card revenue, agent commission, and fixed costs through to net profit
- Scenario parameters and sensitivity analysis
- Explainer document covering methodology, assumptions, and the justification behind each assumption

### Phase 5: Simulations

- Simulation blueprint defining the questions the model must answer
- Python simulation framework covering gold price dynamics, investor growth scenarios, spot capacity and premium behaviour, ICS distribution outcomes, and credit liquidation stress
- Setup documentation and results documentation with charts and plain-language interpretation

### Phase 6: Whitepaper and Documentation

- Public-facing whitepaper derived from the completed deliverables
- Process maps and diagrams
- Branded, print-ready document set
- Handoff materials for the development, legal, and commercial teams

---

## Timeline

> **To be confirmed with the client.** The sequence below is anchored to the client's stated build milestone (design and front-end complete early September) so the mechanism specification lands before the build hardens.

| Week | Focus | Output |
|---|---|---|
| Complete | Discovery and Market Research | Charter, market research report |
| 1 | Classification and token architecture | Foundational design decisions locked |
| 2 | ICS system and SIP mechanics | Scoring formula, tier thresholds, lock and decay rules |
| 3 | Fees, credit, dividend, and revenue streams | Fee mechanics, credit risk engine, dividend funding route |
| 4 | Mechanism design consolidation | Draft mechanism design document and process maps |
| 5 | Revenue model | Architecture brief and Excel model |
| 6 | Supply side and simulation setup | Supply model, simulation blueprint |
| 7 to 8 | Simulation and analysis | Simulation framework and results |
| 9 | Documentation | Whitepaper and branded document set |

**Recurring:** weekly client call, currently Wednesdays at 9 a.m. CST.

---

## Scope

### In Scope

- Full mechanism design across every economic component of the 100 G Business Model
- Regulatory classification analysis and structural recommendations under the UAE framework
- ICS scoring system design and calibration
- Fee architecture, including resolution of the custody fee and peg conflict
- Credit facility economic design, including LTV bands and liquidation thresholds
- Additional revenue stream identification and design
- Agent network commission structure and anti-abuse design
- Revenue modeling, supply-side modeling, and scenario simulation
- Whitepaper and supporting documentation
- Process maps and diagrams
- Warm introductions to investors and partners where appropriate

### Out of Scope

- Smart contract development and code implementation
- Legal opinions and formal compliance sign-off. We produce the classification analysis, the structural recommendation, and the specific questions for counsel. The opinion itself comes from the client's Dubai legal team.
- VARA licence application filing and management
- Custodian selection, negotiation, and gold procurement operations
- Front-end and application development, which the client's team is delivering
- Marketing, brand, and go-to-market execution

---

## Key Stakeholders

| Name | Role | Organisation | Involvement |
|---|---|---|---|
| Gaurav Khullar | Founder | Aurumix | Approver |
| Chetanya Gupta (CG) | Co-founder | Aurumix | Approver and primary contact |
| Tony Drummond | Engagement Lead | Tokenomics.net | Lead and charter owner |
| Abdur Rehman | Research and Modeling | Tokenomics.net | Contributor |
| Harshit Oberoi | Platform and Development | Tokenomics.net | Informed, engaged at build stage |

---

## Key Information

### Product Summary (100 G Business Model)

| Element | Current position |
|---|---|
| Capital allocation | 100 percent of every dollar buys physical LBMA gold |
| Token peg | Fixed grams per token. Currently 1 AURX = 0.01 g |
| Supply cap | None. Supply scales with gold purchased |
| Price | Total vault gold multiplied by LBMA fix, divided by tokens outstanding |
| SIP contribution | 20 USD minimum, 75 USD target average, no maximum. Amount is variable month to month |
| Lock term | 6 months to 25 years. A contribution commitment, not a token lock |
| Missed contribution | No financial penalty. ICS score is reduced |
| Spot capacity | 20 to 40 percent of monthly SIP inflow, split 80 percent ICS lane and 20 percent external lane (not final) |
| ICS | 7 tiers, Green through Sovereign. Governs allocation priority, spot access, credit ratio, dividend share |
| Dividend | 15 to 20 percent of operating profit, 80 percent to the top 10 percent by ICS-weighted score |
| Credit facility | Borrow against gold, maximum 90 to 95 percent LTV |
| Physical redemption | Intentionally excluded. Exit is via cash buyback |
| Growth targets | 500 investors (Year 1), 10,000 to 14,000 (Year 3), 60,000 to 100,000 (Year 10) |

### Revenue Model (current state)

Entry fee of 2 to 5 percent, annual custody fee of 0.8 to 1 percent, credit facility fees, and merchant interchange from card usage. The client has confirmed that investor funds are not deployed into other businesses, so all revenue other than merchant interchange is currently sourced from investors. Expanding this base is an explicit objective.

### Distribution Model

A three-layer agent hierarchy targeting Indian financial advisors and wealth managers, modelled on the Indian insurance agency network and mutual fund advisor channel. Advisors onboard clients and invest on their behalf but cannot withdraw or sell tokens from the platform.

### Regulatory Position

Primary regulator is VARA (Dubai). The client is engaged with a Dubai legal team who are also handling VARA compliance. The working design direction is to keep the token itself a pure gold instrument within the ARVA category, and to deliver the dividend and credit facility through separate licensed structures so AURX does not become a hybrid instrument attracting dual regulation.

### Current Build State

Design and front-end application development expected to complete in early September, followed by API integration and back-end partnerships.

---

## Success Criteria

- A defensible classification position for AURX, with the structural design to support it and a clear set of questions ready for the client's counsel.
- A mechanism design document complete enough for the development team to build from without further economic decisions.
- An ICS scoring system that is calibrated, fair across investor cohorts, and resistant to any single component dominating outcomes.
- A fee architecture that funds the business without compromising the grams-per-token peg.
- A dividend funded by genuine external value rather than recycled investor fees.
- A revenue model demonstrating sustainable economics and quantifying the profit share required to hit the client's target return uplift.
- Simulation evidence showing where the model holds and where it breaks, with parameter recommendations.
- Documentation sufficient for VARA review, listing diligence, and investor conversations.

---

## Voice of Customer

Captured from the discovery call on 2 June 2026. Quotes are the founders' own words.

> **Note on currency.** The 2 June call predates the move to the 100 G Business Model, so any remarks about the 70/30 split, the algorithmic pool, or "upside of a crypto" are superseded. The statements below are the ones that remain valid, because they describe *who the product is for and what problem it solves*, which did not change in the pivot.

### The problem they are solving

**CG:**

> *"The biggest problem is people aren't able to buy gold in smaller sizes, and either it has to be paper gold. Here, we're trying to achieve that you're actually buying physical gold."*

### Who this is for

**Gaurav Khullar:**

> *"We are not bringing shark investors, we are bringing small investors, and long-term lock-in investors, and adding a credit card to it, and creating a utility to it, so that the sell-off... we are trying to restrict the sell-off with multiple factors."*

> *"My investors will not be the same investors at all."*

> *"The quality and the category of the investors... will be very different than what the basic crypto market is being operated as of today."*

### The mindset they are targeting

**Gaurav Khullar**, on the reference point for the product:

> *"People are investing into LICs. Those people are having a mindset, and we are giving them a credit facility against it. There is a steady growth that the coin is giving. There is an asset base, there will be never a free fall. So this is the mindset what we are trying to give to our investors."*

This is the single most useful line in the charter for design purposes. It anchors the product to the Indian life insurance saver rather than a DeFi participant, and it explains why the SIP lock behaves like an insurance premium schedule (commitment enforced through score, not through penalty) rather than like a mutual fund standing instruction.

**CG**, on the time horizon:

> *"We have a 15-year horizon, there's probably 3 generations of investors... it's a very safe investment tool for a long-term investor, for securing wealth."*

### What they want validated

**CG:**

> *"That's the biggest part of this that we want validated as well. There's that game theory element, because we're looking at 50 years."*

**Gaurav Khullar**, on the scarcity engine:

> *"It needs to be always oversubscribed... The moment the event starts getting undersubscribed, the whole momentum will get lost."*

### Their stated challenges

**CG**, on what worries them most:

> *"About compliance, I think one of our biggest challenges is: how do people invest, and in what formats and which channels?"*

**CG**, on fiat access:

> *"This kind of a token is bought using USDT or other tokens, and you're not really buying it in fiat. If we have to enable fiat investment, that's a whole another rabbit hole."*

### Latitude granted

**CG**, on openness to redesign:

> *"We are open to different models there, which makes more sense to the community."*

**Gaurav Khullar**, on the engagement being iterative:

> *"It's the beginning, it's not the end. Whatever first structure you build for us, we will see where to go further from there."*

### Still to capture

The founders have not yet articulated what they intend to *do* with the completed Data Room, i.e. whether it primarily serves a VARA submission, an investor raise, the September build, or partnership credibility. This was asked in writing and not understood, and it did not come up on the 24 July call. It is carried as an open question and shapes what the mechanism design optimises for.

---

## Assumptions

- The **100 G Business Model (Version 3)** is the authoritative specification. The earlier model, including the 70/30 split and algorithmic pool, is superseded and out of scope.
- Aurumix holds full latitude to redesign mechanisms where the analysis supports it, with reasoning provided.
- Gold is held allocated with an LBMA-grade custodian, and custody arrangements are the client's responsibility.
- The client's legal team retains responsibility for the formal regulatory opinion and VARA filings.
- Investor funds are not deployed into any business activity other than gold purchase, as confirmed by the client.
- Growth targets provided by the client are treated as planning inputs, and will be stress-tested rather than assumed.

---

## Dependencies

What we need from the client to proceed without delay:

- [ ] Google Drive access containing supporting documentation, including the differential fee structure for spot versus SIP investments
- [ ] Final spot capacity percentage, currently a 20 to 40 percent range
- [ ] Confirmation of engagement objectives and intended use of the completed Data Room
- [ ] Fixed cost structure and operating budget, required for the net profit model
- [ ] Custodian terms and true custody cost, required to separate cost recovery from margin
- [ ] Introduction to the Dubai legal team, so classification work can be tested against their view
- [ ] Timely responses to questions raised between calls

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| AURX classified as a hybrid or security due to the dividend and credit features, triggering dual regulation | High | Structure dividend and credit off-token through licensed vehicles. Settle classification first, before dependent design work. |
| Custody fee deducted in grams breaks the token peg | High | Move fee collection to cash, skimmed from inflow and at entry and redemption gates. Never touch the gold. |
| Dividend funded from recycled investor fees reads as both weak value and a securities characteristic | High | Introduce genuine external yield sources. Frame returns as asset yield rather than enterprise profit share. |
| Restricted spot capacity throttles AUM growth and excludes institutional participation | Medium | Model the trade-off explicitly. Treat spot capacity as the primary tunable parameter in simulation. |
| The expected secondary market premium is presented as a promise, creating a security characteristic | Medium | Ensure the premium remains market-driven. Constrain marketing language accordingly. |
| ICS complexity makes the product hard to explain to a non-crypto retail saver | Medium | Design for explainability. Test the scoring narrative against the target investor profile. |
| Credit liquidation cascade during a sharp gold drawdown | Medium | Re-space warning and liquidation thresholds beneath the revised LTV ceiling. Stress-test in simulation. |
| Economic specification lands after the build hardens in September | Medium | Front-load classification and mechanism design. Sequence deliverables against the build milestone. |
| Excluding physical redemption conflicts with "you own physical gold" positioning | Low | Address directly in the compliance and messaging layer. Substantiate ownership through allocation and audit instead. |

---

## Resources and Links

### Client Supplied

| Document | Description |
|---|---|
| 100 G Business Model (Version 3) | The authoritative product specification, 17 sections. Supersedes all earlier models. |
| Aurumix reply document | Client's written answers to our pre-kickoff questions |
| Google Drive folder | Pending. Contains supporting documentation including the differential fee structure for spot versus SIP. |

### Tokenomics.net

| Document | Description |
|---|---|
| Aurumix Market Research | Phase 1 deliverable. Ten research tracks with confidence tags and a precedent to mechanism map. |
| Questions and Discussion log | Consolidated open items, client answers, and decisions |
| Aurumix Engagement Brief | Original proposal. Written against the superseded model and re-scoped by this charter. |
| Business model walkthrough and critique notes | Internal analysis of the model and its gaps |
| Discovery call notes, 2 June 2026 | Source for the Voice of Customer section |

### Comparables and References

| Project | Relevance |
|---|---|
| ORO | Dubai gold token funding yield through an external gold leasing partner. Closest regional comparable and the key precedent for external yield. |
| PAX Gold (PAXG) | Regulated gold token. Reference for cash-based fee mechanics, redemption, and unit sizing. |
| Tether Gold (XAUT) | Regulated gold token. Reference for custody disclosure and fee handling. |
| Kinesis | Gold token using a 1 gram unit with physical redemption. Reference for denomination and redemption trade-offs. |

---

## Open Questions

| Question | Status | Owner | Notes |
|---|---|---|---|
| Intended use of the completed Data Room | Open | Client | Product-level Voice of Customer captured from the 2 June call. What remains missing is what they will do with the deliverables. To raise on the next call. |
| Final spot capacity percentage | Open | Client | Currently a 20 to 40 percent range |
| Differential fee structure for spot versus SIP | Open | Client | Pending Google Drive access |
| Fixed cost structure and operating budget | Open | Client | Required for net profit modeling |
| Token denomination and unit size | Open | Tokenomics.net | Client has delegated this to us |
| Custody fee mechanism | Open | Tokenomics.net | Client has delegated this to us |
| Additional revenue streams | Open | Tokenomics.net | Client has requested recommendations |
| ICS scoring formula | Open | Tokenomics.net | Client has delegated this to us, priority order given |
| Agent network commission rates and split | Open | Tokenomics.net | Deferred until the revenue model is built |
| Mining Event framing: retain or replace | Open | Tokenomics.net | Client is open to dropping the framing entirely |
| SIP lock structure and missed contribution treatment | Resolved | Client | Contribution commitment. Missed payments cost ICS only. |
| Dividend multiplier double count | Resolved | Client | Multiplier dropped. ICS-Weighted Score = ICS Score multiplied by Investment Value. |
| Maximum credit LTV | Resolved | Client | 90 to 95 percent, corrected from 110 percent |
| Physical redemption | Resolved | Client | Intentionally excluded |
| Pledged gold earning ICS and dividend | Resolved | Client | Yes, and pledgers should be advantaged |
| Spot lane and ICS interaction | Resolved | Client | Spot access is gated by ICS tier. Spot purchases earn no ICS. |

---

## Charter Approval

| Role | Name | Date |
|---|---|---|
| Client Lead | | |
| Project Lead | Tony Drummond | |

---

*Charter version 1.0. Last updated 24 July 2026.*
