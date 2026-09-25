# Aurumix: What We Need From Legal Counsel, in Plain English

## 1. The questions at a glance

| # | The question, in plain terms | What it decides | Priority |
|---|---|---|---|
| 1 | Does owning the token mean owning the gold? | The whole product, the token, the capital needed, the marketing | Blocking |
| 2 | Is the customers' gold safe if Aurumix goes bust? | The trust structure and the safety promise to savers | Blocking |
| 3 | Do VARA's buyback rules mean what we think? | The cost of every exit, and loan default recovery | Blocking |
| 4 | Is the trust an investment fund, and does its trustee need a licence? | Whether the DIFC structure is affordable | High |
| 5 | Can a lender take a legal claim on pledged gold? | The credit line and the Gold Card | High |
| 6 | Is the payment setup allowed? | Collecting money from abroad, and the stablecoin position | High |
| 7 | How can the family product be offered lawfully? | Whether the family feature launches, and its name | High |
| A | Can Indian residents take part? | The size of the market | Indian counsel |
| B | Is the distribution model lawful? | The agent network and referrals | High |
| C | Which countries beyond the UAE can we serve? | Every market after launch | Before each market |

**If only three questions could be asked, ask 1, 2 and 3 first.**

---

## 2. The three questions that decide whether the product works

### Question 1: Does owning the token mean owning the gold?

- **What we assumed.** A trust in the DIFC is the legal owner of the gold on paper. Its deed says it holds the gold for *whoever holds AURX at any moment*. So when a customer sends AURX to someone else, ownership of the gold moves with it automatically, with no paperwork.
- **Why it matters.** VARA requires the issuer to prove two things: that the customer really owns the gold, and that ownership moves with the token. This is the most important open point in the project.
- **What we need counsel to confirm, as three separate answers:**
  - Can a trust define its beneficiaries as "whoever holds the token"?
  - Can the trust deed remove the usual rule that a beneficiary must sign a written document to pass on their interest? (English law does not allow this; DIFC law appears to.)
  - If yes to both, does that satisfy VARA?
- **If counsel says no.** AURX becomes a token that only verified, registered customers can hold. The token is built so this is a setting change, not a rebuild. The cost: AURX can no longer trade freely or be listed openly.
- **If direct ownership fails altogether.** A much heavier VARA regime applies, including extra capital that could approach USD 4 million at the Year 10 target, and the marketing has to change from "you own gold" to "you have exposure to gold".

### Question 2: Is the customers' gold safe if Aurumix goes bust?

- **What we assumed.** Gold held in the DIFC trust cannot be taken by Aurumix's creditors, even though customers own a share of a pool of bars rather than specific bars.
- **Why it matters.** It is the core safety promise to savers. It is also the reason the trust exists: VARA's rule protecting customer assets in an insolvency is written for virtual assets (tokens), and gold bars are not virtual assets. Onshore UAE law gave us no clear answer on whether pooled gold can be recovered from a bankrupt company.
- **What we need counsel to confirm:**
  - Can gold that is allocated to customers but pooled be recovered from an onshore UAE bankruptcy?
  - Does the DIFC trust genuinely improve that position?
  - Would a UAE court honour VARA's insolvency protection for physical gold at all?
  - Is the DMCC Tradeflow record a legal document of title, or only a contract with DMCC? (The design treats it as supporting evidence, not the foundation.)
- **If counsel says no.** We cannot tell savers their gold is safe if Aurumix fails, and the ownership structure has to be redesigned. ADGM is not a simple swap: under an ADGM foundation the customer would own nothing until the gold is paid out.

### Question 3: Do VARA's buyback rules mean what we think they mean?

VARA says that where a token gives holders a right to redeem, the issuer may charge **no fee of any kind** on redemption. The rulebook never defines "redemption", so three things need confirming:

- **Is the buyback a "redemption"?** We assumed yes, and designed for it: there is no exit fee at all. We would like VARA to confirm this in writing before the application.
- **What does "equal value" mean?** We assumed the customer gets the full gold price, not the lower price a dealer would pay. If counsel reads it the other way, the payout is still fine, but the cost assumption behind every exit changes.
- **Is selling a borrower's gold after a loan default caught by the no-fee rule?** We assumed not. If it is, Aurumix cannot charge the borrower its recovery costs.

---

## 3. The questions that decide individual features

### Question 4: Is the trust an investment fund, and does its trustee need a licence?

- **What we assumed.** The trust is not a fund, because the gold earns no income, is not actively managed, and each customer's share is fixed. A trustee company running only this one trust may not need a DFSA licence.
- **Why it matters.** A fund carries far heavier rules and cost. This is one of the main reasons the client's profit-sharing dividend was removed: bringing it back would bring this question back, and could bring the securities regulator in too.
- **Also needed, a practical ask rather than a legal one:** an indicative cost to set up and run the DIFC trust each year. The client cannot make a build decision without a number.

### Question 5: Can a lender take a legal claim on a customer's pledged gold?

- **What we assumed.** The lender can register a valid claim under DIFC law over the customer's share of the trust. Aurumix valuing the gold, acting as the lender's agent and buying the gold on a sale, all at once, is acceptable if disclosed.
- **What we need counsel to confirm:**
  - Can the claim be validly taken and registered, and how?
  - Does AURX count as a "digital asset" under DIFC law? It changes how the claim is taken.
  - Is Aurumix's triple role acceptable with disclosure, or must an independent party take one of the roles (which adds cost to every loan)?
- **If counsel says no.** The credit line and the Gold Card do not work as designed, and the benefit ladder has to be rethought.

### Question 6: Is the payment setup allowed?

- **Overseas collection.** VARA says money from overseas customers must sit with third-party **banks**. The providers that collect small payments abroad are usually e-money firms, not banks. **Does that count?** If not, collecting small monthly payments from outside the UAE may not be economic, and the market shrinks to people who can pay from a UAE bank account.
- **Stablecoins.** Aurumix accepts bank money only. Customers who hold stablecoins convert them at a licensed exchange and pay by bank transfer. We plan to publish a list of licensed exchanges, with no fee and no data shared. **Does publishing that list count as "arranging" a stablecoin service?** This is the one load-bearing assumption in the payment design.

### Question 7: How can the family product be offered lawfully?

- **We have no position on this one; it is an open question.** No VARA licence covers wills, estates or trust services.
- **What we assumed.** The family transfer works as a standing instruction on the customer's account, not as will-writing, estate administration or acting as a trustee.
- **What we need counsel to answer:**
  - Can it sit outside those licensed activities, and if not, what licence or partner is needed?
  - Are there customer groups or countries where it cannot be offered?
  - Does the name "Digital Will" on its own imply a regulated service?
- **A related point to raise: domicile.** Many Gulf-based Indians remain legally domiciled in India, and an Indian court could apply Indian inheritance law to their gold. We recommend asking for a domicile declaration at onboarding.
- **What does not need a lawyer:** probate cannot be avoided on death. That is already settled in the design; the product speeds probate up rather than replacing it.

---

## 4. Market and distribution questions

### A. India (for Indian counsel)

- **What we assumed.** Indian residents cannot take part. Gold abroad is not something they are allowed to buy under India's Liberalised Remittance Scheme, and a separate rule closes the GIFT City route too. The client's original "USDT via P2P" route for Indian residents was removed.
- **Why it matters.** We changed the target customer on the strength of this. If we are wrong, the market is much larger.
- **What we need counsel to confirm:**
  - Can an Indian resident lawfully pay in monthly? Is there exposure for Aurumix in accepting them or marketing to them, including through agents?
  - When a customer dies and the beneficiary lives in India, can we pay them in cash instead of transferring tokens? (This is our design.)
  - A customer who moves back to India keeps their gold but cannot add money. Is that right?
  - Lifetime gifts to relatives in India are blocked at launch, because the rules turn on the giver's passport. Is that more cautious than it needs to be?

### B. The distribution model

- **Is the three-level agent network lawful in the UAE?** We could not retrieve the UAE's anti-pyramid law. Member referrals are single level for that reason; the agent network still has three levels, organised by role rather than recruitment.
- **Do agents need a licence?** Agents help people sign up and keep saving, which could look like "arranging" or "advising".
- **Do referrers need a licence?** We assumed not, because they only share a code and never place orders or give advice.

### C. Countries beyond the UAE

- VARA gives a test, not a list: serve customers only where the activity is allowed locally, and meet the stricter of the two sets of rules.
- **Each new market needs its own local legal advice before any marketing there.**

| Country | Our reading | What is needed |
|---|---|---|
| UAE | Open at launch | VARA licence |
| Oman | No crypto regime in force. A gap, not a permission | Local counsel |
| Bahrain | Needs central bank approval, local capital and a locally licensed distributor | Local counsel and approval |
| Saudi Arabia, Kuwait, Qatar | Blocked at the banks | Not a launch market |
| UK, Singapore, Canada, Australia | Each needs its own licence | Not a launch market |
| India (residents), United States, FATF blacklist | Excluded | None |

---

## 5. Smaller points for a second batch

These follow from the main answers. Several will answer themselves once the questions above are settled.

- Could VARA still require the extra capital of 2% of gold held, even though a direct-ownership token has no "reserves" in VARA's sense? Potentially several million dollars.
- Does the buyback also need an exchange or broker-dealer licence on top of the issuing licence?
- **VAT:** does the entry fee, the gold or the services attract 5% VAT? The entry-fee margin is thin, so this needs a tax adviser early.
- How does the mandatory wind-down plan work alongside the DIFC trust?
- Gold Rewards moves Aurumix's own gold to a customer. Does it need the same ownership mechanism as a purchase, and can rewards be credited to an account that is blocked for compliance reasons?
- The age of majority for beneficiaries moved to 18 in 2026, and sources disagree on which law enacted it. Confirm before it is built into the app.

---

## 6. What neither we nor counsel can answer

| Item | Why it matters | Who resolves it |
|---|---|---|
| The two-way bullion dealer | The float, the buyback and the fee level all depend on one | The client, by negotiation |
| The vault price | Decides how comfortable "no storage fee" is | The client, by quote |
| The monthly payment collection cost | Decides whether the USD 20 minimum works | The client, by contract with a bank or payment provider |
| The card revenue share | Gold Rewards needs roughly 36% of card interchange | The client, by negotiation with the card partner |
| The VARA approval date | VARA publishes no timeline | Nobody. Never give investors a firm date |
