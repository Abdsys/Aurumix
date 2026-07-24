# Aurumix Tokenomics Project Charter

**Delivery Date:** 8 weeks from July 24, 2026 (Target: September 18 to October 2, 2026)

## Problem statement

Aurumix is building a gold-backed systematic savings platform, issuing a VARA-regulated token (AURX) to long-term retail savers across India and the UAE. The target investor is closer to an Indian life insurance policyholder than a crypto user: someone who saves a small amount every month, wants an asset that cannot fall to zero, and would rather borrow against their holdings than sell them. The platform pairs that savings product with a credit facility and card, a family portfolio with on-chain inheritance, and a three-tier agent network modeled on the Indian insurance agency channel.

The current specification is the 100 G Business Model, in which 100% of every dollar received buys physical LBMA gold. This replaced an earlier design that split capital 70/30 between gold and an algorithmic growth pool. That pivot removed the model's biggest risks, but it left several mechanisms behind that were built for the old economics and no longer perform the function they were designed for. Design and front-end development complete in early September, so the economic specification needs to land in time to inform the build rather than retrofit it.

## Project objectives

- Establish a defensible regulatory classification for AURX and structure the token so the gold core stays inside the retail-friendly ARVA perimeter, with the dividend and credit delivered through some licensed structures.
- Design the ICS scoring system end to end: components, weights, tier thresholds, decay on missed contributions, and caps that prevent any single input from dominating outcomes.
- Resolve the custody fee mechanism so fee collection never compromises the grams-per-token peg.
- Identify and design additional revenue streams so the dividend is funded by genuine external value rather than recycled investor fees.
- Close every remaining mechanism, formula, and threshold in the 100 G Business Model into a specification the development team can build from without further economic decisions.
- Design the credit facility economics: LTV bands by tier, warning and liquidation thresholds re-spaced beneath the corrected 90 to 95% ceiling, and repayment structure.
- Design the agent network commission structure on the Indian insurance agency model, tying trailing income to investor persistency so recruitment for its own sake does not pay.
- Build a revenue model covering all fee lines, credit and card economics, agent commission, and fixed costs through to net profit, and quantify what share of net profit is required to deliver the client's target uplift on gold returns for their top cohort.
- Model supply, free float, and secondary market liquidity for an uncapped token where most supply is locked or pledged.
- Stress-test the model across scenarios, particularly spot capacity versus premium, ICS distribution outcomes, and credit liquidation during a gold drawdown.
- Produce documentation at a quality suitable for VARA review, exchange listing diligence, and investor conversations.

## Deliverables

**Phase 1: Discovery and market research**

- Kickoff questionnaire, client responses, and consolidated decisions log
- Market research report across ten research tracks with confidence tags
- Comparable analysis including ORO, PAX Gold, Tether Gold, and Kinesis and other similar models we identify.
- Precedent to mechanism map, so each design decision draws on evidence rather than assertion
- Regulatory positioning review across VARA, LBMA, and cross-border considerations

**Phase 2: Mechanism design (Weeks 1-3)**

- Mechanism design document:
    - Classification analysis and token architecture, including token standard and the permissioned versus permissionless trade-off
    - Token denomination and unit design
    - SIP structure: contribution commitment, lock terms, and grace and revival mechanics drawn from insurance persistency precedent
    - ICS scoring system, fully specified and calibrated across all seven tiers
    - Spot market capacity allocation and lane structure
    - Custody and entry fee mechanics designed to preserve the peg
    - Credit facility mechanics, LTV bands, and liquidation thresholds
    - Dividend design and its external funding route
    - Agent network economics and anti-abuse structure
    - Family portfolio and digital will mechanics
    - Treasury, liquidity, and OTC lane design
    - Process maps and diagrams
- Questions package for the client's Dubai legal counsel, with our recommended structural position on each

**Phase 3: Revenue model and supply side (Weeks 4)**

- Revenue model spreadsheet:
    - All fee lines: entry, custody, credit, and merchant interchange
    - Additional revenue streams surfaced in mechanism design
    - Agent network commission economics across the three tiers
    - Fixed costs through to net profit
    - Adoption scenarios calibrated to the client's growth targets of 500 investors in Year 1, 10,000 to 14,000 by Year 3, and 60,000 to 100,000 by Year 10
    - Profit share required to deliver the target return uplift for the top cohort
- Explainer document covering methodology and the justification behind each assumption
- Supply-side spreadsheet:
    - Issuance model appropriate to an uncapped, gold-backed token
    - Circulating supply trajectory under each scenario
    - Free float analysis across SIP-locked, credit-pledged, and freely tradeable supply
    - Secondary market liquidity depth and slippage tolerance sizing

**Phase 4: Simulation (Weeks 5)**

Please note this is subjective right now and might change based on the key question we aim to answer with the simulation.

- Simulation blueprint defining the questions the model must answer
- Python simulation framework delivered in a repository, covering:
    - Gold price dynamics using geometric Brownian motion anchored to COMEX futures curves
    - Investor growth scenarios across slow, base, and fast trajectories
    - Spot capacity versus secondary market premium, with capacity as the primary tunable parameter
    - ICS distribution outcomes and dividend concentration
    - Credit liquidation cascade under a sharp gold drawdown
- Scenario charts and a structured results document with plain-language interpretation.

**Phase 5: Documentation and handoff (Week 6)**

- Tokenomics whitepaper suitable for investor and regulatory audiences:
    - Protocol mechanics, token utility, and economic model
    - Simulation outputs and sensitivity analysis
    - Risk register and compliance posture
    - Delivered in Google Doc and PDF formats, 2 rounds of revisions included
- Process maps for the SIP flow, spot allocation, credit facility, dividend distribution, and agent network
- Prep, Launch, and Scale roadmap mapped to milestones across the first three years
- Handoff guides for the development, legal, and commercial teams

## Scope

### In scope

- Complete mechanism design across every economic component of the 100 G Business Model
- Regulatory classification analysis and structural recommendations under the UAE framework
- ICS scoring system design and calibration
- Fee architecture, including resolution of the custody fee and peg conflict
- Credit facility economic design, LTV bands, and liquidation thresholds
- Additional revenue stream identification and design
- Agent network commission structure and anti-abuse design
- Revenue modeling through to net profit
- Supply-side modeling and secondary market liquidity planning
- Scenario simulation delivered as a Python framework with documentation
- Whitepaper, process maps, and handoff materials
- Prep, Launch, and Scale roadmap
- Warm introductions to investors and partners where appropriate

### Out of scope

- Smart contract development or code implementation
- Legal opinions and formal compliance sign-off. We produce the classification analysis, the structural recommendation, and the questions for counsel. The opinion itself comes from the client's Dubai legal team.
- VARA licence application filing and management
- Custodian selection, negotiation, and gold procurement operations
- Front-end and application development, which the client's team is delivering
- Marketing execution, brand, and community management
- Exchange listing negotiations and market maker arrangements
- Ongoing advisory services post-delivery

## Stakeholders and roles

- Gaurav Khullar (Founder): Client and Decision Maker, Aurumix
- Chetanya Goel, "CG" (Co-Founder): Client Lead, Aurumix
- Tony Drummond (Founder, Tokenomics.net): Project Lead
- Abdur Rehman (Senior Tokenomics Engineer, Tokenomics.net): Technical Support
- Harshit Oberoi (Platform Development): Engaged at build stage

| Name | Role | Responsibility |
| --- | --- | --- |
| Tony Drummond | Project Lead | Own the engagement end-to-end. Lead mechanism design, classification strategy, and all client-facing deliverables. Set direction and present recommendations to the Aurumix team. |
| Abdur Rehman | Senior Tokenomics Engineer | Day-to-day technical counterpart to Aurumix. Build the revenue model, supply-side analysis, and simulation framework. Translate design decisions into implementable documentation. |
| Chetanya Gupta (CG) | Client Lead | Primary point of contact on the Aurumix side. Coordinate scheduling, supply documentation and fee structures, and relay founder feedback. |
| Gaurav Khullar | Client and Decision Maker | Provide product direction, business priorities, and timely approvals on design decisions. Make final calls when the team needs to commit to a direction. |
| Harshit Oberoi | Platform Development | Informed through the design phases. Takes the specification into build once the economic model is closed. |

## Success criteria

- A defensible classification position for AURX, with the structural design to support it and a clear set of questions ready for the client's counsel.
- A mechanism design document complete enough for the development team to build from without further economic decisions.
- An ICS scoring system that is calibrated, fair across investor cohorts, and resistant to any single component crowning the top tier.
- A fee architecture that funds the business without compromising the grams-per-token peg.
- A dividend funded by genuine external value rather than recycled investor fees.
- Financial projections showing sustainable economics, with the profit share required to hit the client's target return uplift quantified.
- Simulation evidence showing where the model holds and where it breaks, with parameter recommendations the team can act on.
- The Aurumix team equipped with spreadsheets, guides, and documentation sufficient for VARA review, listing diligence, and investor conversations.

## Voice of Customer

**From the discovery call (June 2, 2026):**

*"People are investing into LICs. Those people are having a mindset, and we are giving them a credit facility against it. There is a steady growth that the coin is giving. There is an asset base, there will be never a free fall. So this is the mindset what we are trying to give to our investors."*
**Gaurav Khullar**

*"We are not bringing shark investors, we are bringing small investors, and long-term lock-in investors, and adding a credit card to it, and creating a utility to it, so that the sell-off, we are trying to restrict the sell-off with multiple factors. My investors will not be the same investors at all."*
**Gaurav Khullar**

*"The biggest problem is people aren't able to buy gold in smaller sizes, and either it has to be paper gold. Here, we're trying to achieve that you're actually buying physical gold."*
**CG**

*"We have a 15-year horizon, there's probably 3 generations of investors. It's a very safe investment tool for a long-term investor, for securing wealth."*
**CG**

*"That's the biggest part of this that we want validated as well. There's that game theory element, because we're looking at 50 years."*
**CG**

*"About compliance, I think one of our biggest challenges is: how do people invest, and in what formats and which channels?"*
**CG**

## Resources and links

**Client-supplied resources**

- 100 G Business Model (Version 3). The authoritative product specification across 17 sections. Supersedes all earlier models.
- Aurumix reply document. Written answers to our pre-kickoff questions.
- Google Drive folder. Pending. Contains supporting documentation including the differential fee structure for spot versus SIP investments.
