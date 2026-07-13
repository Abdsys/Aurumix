# Aurumix — Questions & Discussion Points

> **Questions** = clarifications we need directly from the client/founders (a definite answer resolves it).
> **Discussion Points** = items that need design, research, or strategic analysis on our side — usually with a recommendation — not a one-line answer.

---

## Questions (clarify with client)

1. $75 a month is just the target investment right? Minimum is $20 and max is not capped. Is this amount going to be fixed each month or is it upto the investor? Does each monthly purchase start its own 6-month lock, or does one lock cover the whole SIP?

2. What happens if the SIP investors commit the allocation but dont participate? Where does that allocation go?

3. Are we sure/flexible on the token measurement, i understand its done to make it look accessible (the token count climbing) but it makes the calculation a bit confusing for the comms and customer. 1 token = 1 gram is clean.

4. I am assuming we have to work on the ICS scoring thoroughly as a lot of the perks like (credit and dividends) depend on it. As of now we have the tiers and components that would define the ICS score but exact calculation of the score still has to be done. Of all the ICS inputs (continuity, lock-in, tenure, value, referrals, Masterclass, family) do we have any preference of weighting among each factor? Like whats more preferred vs whats less

5. What percentage of revenue goes to the agent network, and how is it split across the 3 levels? Need to clear this because usually agent commissions are tied to the value of investors they bring. We can have a direct share from the initial fee for agents instead of the whole revenue line.

6. Is ICS Spot Lane eligibility the same as Confirmed SIP status (6 consecutive events), or a separate higher ICS threshold? The doc seems to use both but its not clear if they are the same gate. If they are different, what ICS level makes someone spot-eligible?

7. Does pledged gold still earn ICS and dividend while it is encumbered as credit collateral?

8. What is the goal of the Mining Events now?

   Since the token price is now purely gold, buying at one event vs. the next gets gold at the same day's price either way, and every confirmed SIP investor is guaranteed their allocation. So is the "oversubscription / mining" framing now just a retention/FOMO device rather than a real economic mechanism? Should we keep the heavy mining framing or simplify to "gold DCA + tier-earned spot access"?
    - Also we will be limiting our AUM/market cap growth in a way because we are limiting oversubscription in a way.

9. Custody and management fees in actual funds don't work on a snapshot. They accrue daily on the balance held that day, then settle periodically. Each day, accrue 1%/365 of that day's grams. Settle the accrued total at the anniversary (or at transfer/redemption, whichever comes first). However in the case of gold tokens its different because the peg may get affected.

10. Sovereign credit category is 110% of gold value, lending more than the collateral is unusual, we need to make sinks to cover the shortfall. Whats is the thinking here?

11. The dividend is paid from operating profit, but that profit is just the fees investors pay (entry, custody, credit). Also now there is no external yield source, so is the ICS Dividend actual value creation or just investors' own fees recycled back to them and concentrated into the top 10%? This needs to be thought through and we need to add more revenue streams, probably designed around product featurs.

12. Lock-in duration appears to affect the dividend twice (double dependency). It is a component of the ICS score, and it also sets the standalone Dividend Multiplier, and the ICS-Weighted Score = ICS Score × Investment Value × Dividend Multiplier. So lock-in is counted once inside ICS and again as the multiplier on top — a compounding (lock-in²) effect that can let long lock-ins dominate the 80/20 pool over the stated "primary driver" of continuity. Is this an intentional super-weighting of long lock-ins, or an unintended double-count? If intentional, we need to calibrate the magnitude so lock-in alone cannot crown the top 10%; if not, lock-in should live in only one channel (either an ICS component or a standalone multiplier, not both).

---

## Discussion Points (design / research / strategy)

1. Is the credit revolving (like a card) or a fixed-term loan? Is there a repayment deadline? (We can figure this out if not clear yet, and reserach on how lending partners offer it) The credit system needs to be thought out through. The entire risk engine for eg LTV, liquidation thresholds, credit extension types needs to be understood.

2. We need to research and find out how AURX gets classified (commodity, security, fund, etc.) that will allow us to establish the structure and opinion about the secondary market trading.
