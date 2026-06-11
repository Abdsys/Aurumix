# Aurumix

---

## How We Read Aurumix

Aurumix is a long-term, gold-backed Systematic Investment Programme issued as a VARA-regulated token. Every dollar splits 70/30 by smart contract. 70% buys physical LBMA gold held in custody. 30% goes into an algorithmic growth pool of conservative instruments. New tokens reach investors only through Mining Events, allocated by a Priority Score that rewards consistency over cheque size. The design is built so every event closes oversubscribed, and the token pairs with a gold-backed credit facility so investors borrow against their holdings rather than sell.

The investor profile is not crypto-native. The target is the long-term saver, closer to an LIC subscriber than a DeFi participant. The design constraints span 50 years, roughly 1,176 Mining Events, VARA's regulatory perimeter, and an LBMA-grade custody operation.

The Complete Data Room is built for this kind of work. Our methodology is fixed. What's tailored for Aurumix is how each phase maps to the specific design questions the master reference document already surfaces. The V3 formula tagged "to be built". The Priority Score tables marked "need to work". The cohort-level fee revenue curve the team has explicitly asked for. The architectural decisions on token compliance, credit delivery, and agent governance that determine whether the system holds for fifty years.

Phase 0 sets up the engagement. The six phases that follow are how the work maps to Aurumix.

## Phase 0: DiscoveryFounder pay is changing fast. ⚡️  


Discovery aligns scope before any design work begins. For Aurumix this phase covers:

- **Current-state inventory.** Whitepaper, pitch decks, internal docs, market research, user data, roadmaps, revenue and cost models, KPIs.
- **Quality assessment** across three axes: accuracy, gaps, and internal consistency. Strong inputs route the engagement into refinement and alignment. Incomplete inputs route it into deeper handholding and builds.
- **Kickoff meeting** to capture implicit context, working assumptions, and the gaps surfaced in review. Near-term and long-term objectives clarified across fundraising, growth, retention, and product features.
- **Aurumix-specific scope alignment.** This is not a standard token project. The model already exists with significant structural depth, so the engagement is validation, stress-testing, simulation, and investor-grade documentation built on top of it. Calibrated to the hybrid gold-plus-algorithm structure, the 50-year emission, the ICS scoring, and the VARA framework. Not from-scratch redesign.
- **Project charter** capturing the voice of customer from the meeting, sent to you for sign-off before design work begins.

**Deliverables:** Project Charter for Alignment, and Voice of Customer documentation.

## Phase 1: Market Research

Before any mechanism is designed, we look outward. Comparable models show where the pressure points sit, which assumptions fail under stress, and which investor behaviours define the first three years.

The research is not a literature review. It is the stress-test catalogue every later phase draws from. For Aurumix, that means examining:

- **MicroStrategy (MSTR).** The closest analog to AURX's GFV-plus-APV price structure, and the cleanest case for how premium-over-NAV dynamics behave through a real market cycle.
- **Tokenised commodity precedents.** PAXG, Tether Gold, and Pax Silver, for regulated custody, redemption mechanics, and oracle architecture.
- **Algorithmic growth failure modes.** Including the Terra/Luna reference CG raised on the call, treated as the failure pattern any pool-driven price appreciation engine has to avoid.
- **A recent silver-tokenisation engagement** we covered on the call. A direct structural comparable for the asset-backed credit facility.
- **VARA, LBMA, and cross-border NRI/FEMA positioning** relative to peers.

The output is a market research document the later phases draw from. It also produces a written record of which historical mistakes Aurumix is structurally exempt from, and which still require active mitigation.

## Phase 2: Mechanism Design

Mechanism design is the keystone phase. Every subsequent deliverable in the engagement depends on what closes here. Theory before numbers. If a mechanism cannot be defended in plain language, no simulation will rescue it. This phase exists to finalise every formula, threshold, and rule before a single line of simulation code runs. The simulation needs a closed mechanism to operate on. Qualitative fairness can only be assessed at the design layer, not the numerical one.

For Aurumix, this phase closes the following:

- **The V3 formula.** Fully specified. Includes the Target Alignment Multiplier and its three inputs: the raw new-gold ratio, the oversubscription sentiment signal, and the ecosystem-target anchor. The output is a defined response surface across all 50 years.
- **The Priority Score system.** Calibrating every "need to work" table (Duration Score, Lock Score, Family Group Bonus, Referral tier multipliers, Tier score thresholds, Spot Window streak bonuses) and checking the result for fairness qualitatively across investor cohorts and class tiers.
- **The dynamic event-size formula.** Tied to the published investor growth targets (500 in Year 1, 14,000 by Year 3, 60,000 to 100,000 by Year 10) with the asymmetric subscription-ratio feedback documented in Section 3.4.
- **The seven-step Mining Event process** refined into specification-ready form for the smart contract team.
- **The credit facility taken from concept to full mechanic.** Per-market delivery routes (UPI, NBFC gold loan, funded debit, country partner), the Class 1 vs Class 2 holder distinction, LTV mechanics by ICS tier, and a no-sell-to-pool spending flow that matches card spend against incoming SIP principal.
- **DCA and other features that make holding more attractive than selling.** Optional design modules consistent with the Mining Event architecture.
- **Token architecture per the compliance discussion.** ERC-3643 base with an ERC-20 wrapper. This preserves KYC enforcement while permitting DeFi composability. Wallet topology and custody flow specified.

This is a sample of what mechanism design could cover for Aurumix, not an exhaustive list. The full scope is shaped by what Discovery surfaces.

The output is a closed-form mechanism design document and the supporting process maps. Every subsequent phase runs on both.

## Phase 3: Revenue Model

Once the mechanism is closed, we model how Aurumix earns. This is the deterministic, happy-path revenue picture. The static projection the team needs to plan hiring, operating reserves, and the build budget against.

For Aurumix this covers:

- **The 5% to 2% declining algorithmic growth fee** mapped against pool balance and growth assumptions, with the 15% permanent reserve floor enforced.
- **The 3% entry fee** on the 30% algorithmic portion.
- **The custody and audit fee** net of operational cost.
- **Spot Window revenue** from the 5% per-event allocation.
- **Credit facility interest income** and default assumptions.
- **Agent network commission economics.** The 15% platform fee share and how it distributes across the three levels under different network configurations.
- **Year-by-year and cohort-by-cohort revenue curves** across the full 50-year horizon. This is the simulation the master reference document asks for in Section 2.6.
- **Additional revenue streams** the mechanism design phase surfaces that the current reference document does not yet quantify.

The output is a working-capital-ready revenue model spreadsheet covering both the near-term operating window and the long-horizon trajectory.

## Phase 4: Simulation

This is the most intensive phase, and its shape depends on what mechanism design closes in Phase 2. The simulation runs on the finalised mechanism, not the current draft. The deterministic revenue model shows one path. The simulation tests thousands and surfaces where the design holds or bends.

For Aurumix, the simulation work covers:

- **Gold price modelling using geometric Brownian motion** with drift and volatility parameters. Anchored to COMEX gold futures curves at 12, 24, and 36 month tenors as the market-implied baseline.
- **Monte Carlo across investor growth scenarios.** Slow, base, and fast, calibrated to the published targets.
- **Oversubscription dynamics across all 1,176 Mining Events,** with the three-event rolling average and asymmetric supply-contraction feedback fully modelled.
- **V1 + V2 + V3 sensitivity surfaces.** How each driver affects mining-price trajectory under different inflow conditions, and where the gap between calculated APV and real pool value becomes structurally meaningful.
- **Algorithmic pool depletion stress,** including the 85% principal floor and fee-suspension behaviour.
- **Credit facility default and collateral liquidation cascade modelling.**
- **Cohort-level fee revenue** across the 50-year horizon, with each cohort's distinct V3 entry profile preserved.
- **Mining Event subscription dynamics.** Modelling the conditions under which oversubscription survives, and the conditions under which it breaks.

The output is a Python simulation framework delivered in a GitHub repository, with full scenario charts and a structured simulation report.

## Phase 5: Supply Side

We hold this phase until after simulation. AURX is not a standard utility token with a fixed pre-decided vesting schedule. Its emission is event-based and dynamic. The supply schedule emerges from the calibrated event-size formula and what the simulation actually shows, not from a curve drawn at the start.

This phase also covers what happens to tokens after issuance. Where they sit, what's locked, what's pledged to the credit facility, and what reaches the secondary market once exchange listings begin in Year 2. The dynamic we raised on the call is the failure mode this work prevents: thin liquidity pools where tens of thousands in selling pressure can erase millions in market cap.

For Aurumix, the issuance side produces:

- **The 100 billion token hard cap** distributed across Phase 1 (~70%, Years 1 to 15) and Phase 2 (~30%, Years 16 to 50).
- **Decay constant calibration** against simulation-observed inflow rates and oversubscription patterns.
- **The dynamic event-size formula** in its production-ready form, tuned with the asymmetric subscription-ratio feedback the master reference document specifies.
- **The 5% Spot Window allocation per event** modelled across the tier-residual roll-up rule.

On the secondary market side, the phase produces:

- **DEX liquidity depth requirements** sized against the expected free float at each horizon phase, with explicit modelling of how SIP-locked supply, credit-pledged supply, and the freely tradeable Spot Window combine into what secondary market liquidity has to absorb.
- **Trade size and slippage modelling** so a single large buyer or seller cannot disconnect the secondary market price from the mining-price floor by more than a defined tolerance.
- **Buy pressure analysis** across cumulative tokens leaving lock-in over time. This includes how the credit-facility match flow set in Phase 2 absorbs card-spend sell pressure before it reaches the pool.
- **Launch liquidity budget** for the Year 2 listing. Initial DEX seed depth and the scaling profile as circulating supply grows.

The output is a complete supply-side spreadsheet showing circulating supply over the full 50-year horizon under each simulated scenario, alongside a DEX liquidity plan sized against the float trajectory.

## Phase 6: Documentation

The output that closes the engagement. A whitepaper and supporting materials that read like a research paper, not a pitch. Methodology stated. Evidence presented. Stress-test results visualised. Risk register published. Compliance posture written for VARA review and listing-partner diligence.

For Aurumix this covers:

- **The full tokenomics whitepaper,** with embedded simulation outputs, V1+V2+V3 derivation, sensitivity heatmaps, and an honest treatment of the gold floor versus algorithmic premium framing.
- **Process maps** for the Mining Event flow, the 70/30 capital flow, the credit facility, the agent network, and the seven-step event execution.
- **The Tokenomics Audit Report.** An independent review of every design decision, with prioritised recommendations.
- **The Market Research deliverable** in client-ready form.
- **The Prep, Launch, and Scale roadmap,** mapped to milestones across the first three years.
- **Handoff guides** for the development team, the legal and compliance team, and the capital markets team.
- **Whitepaper delivered in Google Doc and PDF formats,** with two rounds of revisions included.

The output is a publication-quality document set sufficient to bring to investors, list with an exchange, and submit for VARA review.

---

## Where This Lands

The methodology stays the same. What's specific to Aurumix is how it answers the design problem you actually have. Closing the formulas marked "need to work". Validating the engine that makes oversubscription perpetual. Producing the documentation that lets the model survive contact with regulators, exchanges, and investors.

## Engagement Summary

| Phase | Primary Problem Solved | Deliverable |
|---|---|---|
| **0. Discovery** | Scope alignment and voice of customer capture before any design work begins | Project Charter for Alignment, Voice of Customer documentation |
| **1. Market Research** | Surfacing failure modes from comparable models to inform stress-test design | Market research document covering MSTR, Terra/Luna, tokenised commodities, and regulatory positioning |
| **2. Mechanism Design** | Closing every "need to work" formula, parameter, and architectural choice before they hit simulation | Mechanism design document and supporting process maps |
| **3. Revenue Model** | Deterministic happy-path revenue picture for planning hiring, reserves, and budget | Revenue model spreadsheet covering near-term and 50-year horizons |
| **4. Simulation** | Validating the closed mechanism under thousands of scenarios across the 50-year horizon | Python simulation framework in GitHub, scenario charts, structured simulation report |
| **5. Supply Side** | Calibrating emission against simulation behaviour and sizing liquidity against the free float | Supply-side spreadsheet over the 50-year horizon and a DEX liquidity plan |
| **6. Documentation** | Institutional-grade artefacts for VARA review, listing partners, and investor diligence | Whitepaper, process maps, tokenomics audit report, market research deliverable, Prep/Launch/Scale roadmap, handoff guides |
