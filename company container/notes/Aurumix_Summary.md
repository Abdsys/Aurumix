# Aurumix Project Summary

## What It Is, In Plain Terms

Aurumix is a gold-backed long-term savings programme dressed up as a crypto token. Investors commit to monthly contributions (a SIP). Every dollar is split 70% into physical gold (held in a Dubai LBMA vault) and 30% into a conservative bond portfolio. Investors receive AURX tokens representing their share of the pool. New tokens are released every 15 days through "Mining Events" at a price the company itself calculates by formula. Headquartered in Dubai under VARA regulation, targeting NRI, HNI, and diaspora retail investors over a 50-year horizon.

The mental model the founders push: Aurumix is the company. AURX is the share. Gold and bonds are the assets. Mining Events are rights issues.

---

## Chronology

### 1. Project Launches
- All 100 billion AURX tokens minted at once into the Genesis Contract (hard cap, no more ever)
- Smart contracts deployed for split, mining, locks, fees, custody
- Founders buy at the same price as everyone else (no free tokens)

### 2. First Mining Event
- $10,000 total event size, AURX priced at $0.00125
- 8 million tokens released
- Earliest investors fill the event

### 3. Investor Joins
- Downloads the Aurumix Circle app, completes KYC
- Sets up monthly SIP: amount, duration (6 months to 25 years), lock-in period, family group, referrer
- Auto-debit mandate registered

### 4. Each Monthly Payment
- Smart contract splits the money instantly: 70% buys gold, 30% goes to the bond pool
- Investor's ICS (Investor Conviction Score) updates: streak +1, duration logged
- After 6 consecutive events, the investor earns Confirmed SIP status. Their fixed monthly amount is now guaranteed allocation in every future event

### 5. Mining Events Every 15 Days
- Custodian confirms the gold is in the vault
- Price calculated: `GFV (gold value per token) + APV (algo pool premium)`
- Price can only go up, never down
- 95% of new tokens go to SIP investors (allocated by Priority Score)
- 5% reserved as a Spot Window for high-tier members (activates after Year 2)
- Fees deducted, tokens distributed, dashboards refresh

### 6. Status Climbing Over Time
- Priority Score builds from SIP × Duration × Lock × Continuity × Family × Referrals
- Investors climb six tiers (Silver to Sovereign), each unlocking spot access and better allocation

### 7. Year 2 Exchange Listing
- AURX lists on CEX and DEX
- Two parallel prices emerge: Mining Event Price (formula-driven, never falls) and Secondary Market Price (free float)
- Spot Window fully activates

### 8. Liquidity Without Selling
- Investor pledges AURX to a smart contract
- Borrows against the gold value (74% for Gold tier, higher for higher tiers)
- Delivered through local partners (NBFC in India, prepaid wallet, debit card)
- Investor spends through credit instead of selling tokens

### 9. The Long Arc
- Years 1 to 15: ~70% of supply released, high oversubscription, demand engine active
- Years 16 to 50: ~30% of supply released, premium compresses, ecosystem matures
- Algo Growth Fee declines from 5% to 2% floor by ~Year 13
- Target: 100,000+ investors per event by Year 50

### 10. Exit (Or Not)
- Lock-in expires. Tokens can be transferred or sold
- The design discourages selling. The credit facility lets investors spend their gold value without selling
- Built so investors never exit, only spend

---

## Sustainability Issues

These are not edge cases. They are baked into the design.

### 1. The Company Sets Its Own Price

Aurumix calculates the Mining Event price using a formula it controls. One input, the V3 "target alignment multiplier", is designed to adjust prices upward when investor growth falls short of plan. That is not pricing. That is calibration to a business target. No independent body, no market, and no audit verifies the price at issuance. The team that earns fees on the algo pool is the same team that sets the algo pool's quoted value.

### 2. Price Drifts Above Real Asset Value Over Time

The price formula is `Gold Floor Value + Algo Pool Premium`. The Algo Pool Premium grows by V1 + V2 + V3 every event. V2 alone adds 6% annually with no underlying cashflow justifying it. V3 adds far more in early years. Real bond yields earned on the algo pool are 4 to 5%. The result: the official Mining Event price grows faster than the asset base behind each token. The longer the project runs, the wider the gap between what investors pay at events and what each token represents in real assets.

### 3. Price Floor Goes Only One Way

Mining Event price can never decrease. Even if gold drops 30%, even if the bond portfolio loses value, the next event price must be at or above the previous one. This is enforced by smart contract. It creates a mathematical commitment that may eventually be impossible to honour without inflating V3, which deepens problem #2.

### 4. There Is No Redemption At Event Price

A real SIP lets you redeem at NAV. Aurumix removes that right entirely, framed as "IPO model, not redemption fund". The investor can only sell on the secondary market, where price will be whatever buyers will pay. The Mining Event price has no market test. If many investors try to exit at once, the secondary market collapses while the Mining Event price keeps quoting higher numbers to new investors.

### 5. The System Depends on Continuous Oversubscription

The event sizing formula, the V3 multiplier, and the price floor all depend on consistent oversubscription event after event. If new investor inflows slow, demand pressure fails. V3 has to work harder to hit the trajectory. The gap between price and NAV widens. Confidence breaks. The model has no graceful failure mode for low growth. It can only contract supply, not adjust price downward.

### 6. Late Investors Get Worse Deals By Design

An investor who joins in Year 20 buys at a price reflecting 20 years of compounded V2 and V3 markups. The gold per token they receive is smaller than what an early investor received per dollar invested. Existing holders benefit from each new investor entering at a higher price. Early investors are paid by late investors entering at premium. That is the textbook critique of any compounding-price model.

### 7. Long Lock-ins Hide The Problem

Lock-ins of 6 months to 25 years, combined with credit facilities that let investors spend without selling, mean the model can run for years without anyone testing the real price. The Mining Event price keeps going up. Investors think they are winning. The reality check only arrives if regulators intervene, exchange listings expose the gap, or an external shock forces simultaneous exit.

---

## Design Gaps

If we take the design as-is, these are the open items that need to be closed before anything downstream is meaningful.

### Formulas Marked "Need To Work" In Their Own Doc

- V3 formula itself. Trajectory described (100% to 8% to 5%), formula not built. Target Alignment Multiplier not specified.
- Duration Score values across all 10 SIP bands
- Lock-in Score values across all 10 lock bands
- Subscription Adjustment %s in the high-demand bands (SR > 2.0×)
- Custody fee % (currently ~1%, depends on actual cost)
- Loyalty Multiplier appears in the Priority Score formula but is never defined
- Class Multiplier values for the I to V investor classes
- Decay constants across the 50-year supply curve

### Mechanics Described But Underspecified

- ICS Score formula itself. Tier ranges are given but the calculation from inputs is missing.
- Confirmed SIP threshold logic. 6 events confirmed, but the allocation algorithm around the protected base is fuzzy.
- Phase 1 vs Phase 2 supply split. Stated as ~70% and ~30%, exact decay schedule not defined.
- Spot Window allocation post-Y2. Activation trigger, residual roll-up edge cases, streak bonus interaction.
- Family Group SIP splitting rules. How a $100 SIP is split across 8 family members, who counts towards the bonus.
- Investor Class System thresholds. $37.50/event appears arbitrary, not derived.
- Mining Event Scheduler governance. Multi-sig approval rules, what changes require it, frozen periods.
- Credit limit % per tier. Only Gold tier example (74%) given. Other tiers not specified.
- Streak recovery math. "Held points reactivate" but the formula for partial reactivation is missing.

### Ambiguous Or Unresolved

- Token standard. ERC-20 implied but ERC-3643 or ERC-1400 needed for VARA compliance. Not chosen.
- Spot Window timing. Activates "post-Y2" but specific event trigger not defined.
- VARA classification ruling. They hope for "commodity-linked hybrid". Not confirmed.
- MLM safe harbor design. Referral cap stated as "subordinate to investment scores" but the actual cap % not set.
- Custody multi-vault failover. Brinks, Loomis, Malca-Amit listed as options. Single or split?
- Algo pool instrument allocation %s. Govt securities, MMF, IG bonds, deposits all listed. Target allocation not specified.
- Subscription Ratio definition. Capital blocked vs planned capital, but planned capital itself adjusts. Circular.

The Mechanism Design phase has to close the first two categories before any simulation work is meaningful. The third category is design additions worth pitching as scope. The fourth needs legal and architectural decisions, not just math.

---

## Summary

The structure works if and only if new investors keep showing up faster than old investors want to exit. The 70% gold backing is real and provides a meaningful floor. The 30% algo pool's quoted growth is largely algorithmic markup. The legal structure (no redemption right) protects Aurumix from a bank run. It does not protect the investor from buying into a price detached from underlying value.

These are solvable problems. Solving them requires changes to the pricing formula, the floor rule, and the disclosure framework. Better simulations of the current design will not fix it.
