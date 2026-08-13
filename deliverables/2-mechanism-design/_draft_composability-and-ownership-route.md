# Composability and the Ownership Route

> **Status:** Phase 2 decision draft, 2026-08-13. Written after the 2026-08-13 finding that DIFC Trust Law Art 60(6) does not support the permissioned-token decision.
> **What it decides:** whether AURX can be a normal ERC-20 that works across DeFi and trades on any venue, and what that does to the ownership structure, the licence and the ICS.
> **Read §0 alone if nothing else.**

---

## 0. Summary in ten points

1. **The no-composability conclusion rested on one link, and that link is broken.** The chain was: route 2 to DIFC trust to Art 60(6) to named holders to permissioned token to no DeFi. Art 60(6) has now been read verbatim and it is an AML duty aimed at corporate parties, enforced by the Registrar. It is not a duty to identify every token holder. Remove it and nothing else in the chain holds the permissioning up.

2. **The second chain, the VARA one, has now also been read verbatim, and it does not say what our drafts say it says.** Rule III.B.1.c is a risk-management obligation to respond to divergence between the token ledger and the ownership ledger. It is not a permissioning mandate and it never mentions registration, whitelists or approved venues.

3. **VARA imposes no transferability restriction anywhere.** The only transferability rule in the entire Issuance Rulebook is a **disclosure** obligation: the whitepaper must state "any restrictions on the transferability". VARA requires you to disclose the restrictions you choose to impose. It does not require you to impose any.

4. **VARA expressly contemplates AURX reaching someone Aurumix has never met.** Rule III.E.3 conditions redemption on the owner "**or their designee**" having onboarded. Identity is required at the redemption gate, not at the holding stage. Identify at entry and at exit; the middle is free.

5. **Route 2 stays, and its role inverts. It is now the enabler of composability, not the obstacle.** Under route 2 the vehicle holds legal title permanently and the metal never moves. What moves between holders is a beneficial interest under a DIFC trust. If the trust deed defines the beneficiary class by reference to token holding, the token transfer **is** the transfer of ownership, self-executing, with no register write and no counterparty identification.

6. **The DIFC statute supports that construction on four independent legs, all verified verbatim.** Art 45(1)(b)(i) (beneficiary ascertainable by reference to a class), Art 34(2) (definite if ascertainable now or in the future), Art 45(2) (the terms may provide for addition and exclusion of beneficiaries), Art 48(4)(a) (the statute expressly contemplates an interest arising by class membership and ceasing on leaving the class).

7. **The decisive one is Art 47(2), and it is better than English law.** "**Subject to the terms of a trust**, a beneficiary may, by instrument in writing, sell, charge, transfer or otherwise deal with his interest in any manner." The writing formality is a default the trust deed can displace. The English analogue (LPA 1925 s.53(1)(c)) is mandatory and cannot be displaced. DIFC was the right jurisdiction for a reason nobody had identified.

8. **Our current architecture is the one that creates the risk III.B.1.c exists to manage.** Model B moves the token, then writes the register separately, so the two can diverge and "mitigating measures" are genuinely needed. The class-defined trust removes the divergence by construction. **The composable design is the stronger compliance answer, not the weaker one.**

9. **Do not build a permissioned base token with an open wrapper.** Inside the wrapper the registered holder is a smart contract, so the wrapper holder owns no gold. That is precisely the Kinesis trap already recorded in decision 10 and the ownership explainer. It is the worst of both structures.

10. **Recommended: open ERC-20 base with a blocklist, not an allowlist**, KYC at mint and at redeem, freeze and seize role retained, upgradeable proxy with a transfer-hook stub. Ship it composable-capable in September, list nowhere until the float is deep and counsel has confirmed the trust construction. **Composability becomes a switch we own rather than a rebuild we cannot afford.**

---

## 1. Exactly which link broke, and what still stands

The reasoning that produced "AURX cannot be composable" had five links. Only one is gone, but it is the one that carried the load.

| # | Link | Status |
|---|---|---|
| 1 | Choose Option A, direct-ownership ARVA, to escape the Reserve Asset regime and roughly USD 4M of locked capital | **Stands.** Verified against III.C's opening words, which attach the reserve regime to the stable-value branch only |
| 2 | Option A requires proving ownership transfers with the token (III.B.1.a) | **Stands.** Verbatim below |
| 3 | Onshore UAE could not answer whether pooled fungible gold is reclaimable in bankruptcy, so use a DIFC vehicle (route 2) | **Stands**, and is now load-bearing for a second reason |
| 4 | Route 2 means a DIFC trust, and Art 60(6) requires identifying every beneficiary, so every holder must be named | 🔴 **BROKEN.** Art 60(6) is an AML duty on corporate parties, enforced by the Registrar |
| 5 | Named holders require a permissioned token, which forbids DEXs, DeFi and open transfer | **Falls with link 4.** It was never an independent conclusion |

Everything expensive we have already decided survives. The Option A choice survives, the capital saving survives, the DIFC vehicle survives. **What falls is one inference about token mechanics, and it is the cheapest thing in the chain to change.**

---

## 2. What the rules actually say, verbatim

All text below is quoted from primary source, not from commentary.

### 2.1 VARA, Annex 2 Part III.B (from `_r_vara_issuance_20250519.pdf`, 19 May 2025)

> **B. Direct right of ownership**
> 1. All VASPs Licensed to issue an ARVA which represents, or purports to represent, a direct right of ownership of the Reference Asset, or a fractional proportion thereof, shall ensure:
> a. the right of ownership is legally and validly established and that such right of ownership is transferred in the event of a transfer of ownership of the ARVA;
> b. **where** transactions in the Reference Assets are subject to legal or regulatory requirements relating to their settlement, completion and/or transfer of title, that such legal or regulatory requirements are satisfied, in order to give effect to the transfer of ownership in the event of a transfer of ownership of the ARVA; and
> c. that the VASP will respond to transactions in the ARVA not resulting in a corresponding transaction in the Reference Asset being legally settled, completed and/or transferred, and shall implement mitigating measures to ensure all transactions in the ARVA result in a corresponding transaction in the Reference Asset being legally settled, completed and/or transferred.
> 2. Legal opinion. VASPs Licensed to issue ARVAs may be required to provide VARA with a legal opinion, provided by a professional and duly registered lawyer, confirming any explanation made either to VARA or any information contained in a Whitepaper.

Three things follow that our drafts do not currently reflect.

**III.B.1.b is conditional and we read it as absolute.** The word is "**where**". If the transfer of the Reference Asset is not subject to settlement or title-transfer formalities, the clause imposes nothing at all. Under route 2 with a class-defined trust, the underlying transaction is a shift in beneficial interest governed entirely by the trust's own terms, and Art 47(2) lets the deed set those terms. There is no external formality to satisfy.

**III.B.1.c is a risk rule, not a permissioning rule.** It requires the issuer to respond to divergence and to mitigate against it. It says nothing about who may hold the token, nothing about registered venues, nothing about approved counterparties. Our `_draft_purchase-structure.md` §6 states "Any venue listing AURX must be an approved participant with registered customers. An open DEX listing is incompatible with Option A." **That sentence has no support in the rule text and must be withdrawn.**

**III.B.1.c actually argues for the composable design.** The risk it targets is a token moving without ownership moving. Under Model B (token moves, register is written separately) that gap is real and needs mitigating. Under a class-defined trust the gap cannot open, because the class is defined by the ledger itself. The answer to "what are your mitigating measures" becomes "the divergence is structurally impossible", which is the strongest answer available.

### 2.2 VARA on transferability

Searched the full Issuance Rulebook. The only transferability provision is a whitepaper disclosure item:

> vii. any restrictions on the transferability, or additional steps required to give legal effect to a [transfer]

This is the same shape as decision 37's finding on token standards. **VARA tells you to disclose what you choose. It does not choose for you.**

### 2.3 VARA, Annex 2 Rule III.E.3

> VASPs Licensed to issue ARVAs must ensure all requests made by owners and/or holders to redeem such ARVAs for an equal value of RWAs shall be processed and completed within a reasonable period of such requests being made, **provided the owner and/or holder, or their designee, has successfully onboarded with the VASP**...

Confirmed at primary source. This is the clearest statement in the whole rulebook that a token may lawfully sit with someone who has not onboarded. Onboarding is a **precondition of redemption**, not of holding. Decision 38 already spotted this; it is now verified.

### 2.4 DIFC Trust Law 2018 (from `_source_difc_trust_law_2018.txt`)

> **Art 34(2)** A beneficiary is definite if the beneficiary can be ascertained now or in the future.

> **Art 45(1)** A beneficiary shall be: (a) identifiable by name; or (b) ascertainable by reference to: (i) a class; or (ii) a relationship to some person...
> **Art 45(2)** The terms of a trust may provide for the addition of a person as a beneficiary or the exclusion of a beneficiary from benefit.

> **Art 47(1)** The interest of a beneficiary shall constitute movable property.
> **Art 47(2)** **Subject to the terms of a trust**, a beneficiary may, by instrument in writing, sell, charge, transfer or otherwise deal with his interest in any manner.

> **Art 48(4)(a)** in relation to a beneficiary who is the object of a power or whose interest arises **by virtue of his membership of a class**, the termination of his interest includes his **ceasing to be... a member of the class**;

> **Art 66(1)** **Subject to the terms of a trust** and any order of the Court, a trustee shall, **on application in writing by a beneficiary**, disclose to the applicant all documents which relate to or form part of the accounts of the trust.

Art 66 matters more than it looks. The disclosure duty is **pull, not push**: a beneficiary applies, and the trustee responds. The trustee is never required to hold a list and proactively contact everybody. A holder who wants something identifies themselves in order to get it, which is exactly the same shape as III.E.3.

---

## 3. The preferred route

**Route 2 stays. DIFC, not ADGM, and a trust, not a foundation.**

It was chosen for insolvency robustness and it still delivers that. What has changed is that it now delivers a second thing nobody had noticed, and the second thing is worth more than the first.

| | Route 1 (Aurumix holds as bailee, onshore) | **Route 2 (DIFC vehicle holds title)** | Route 3 (customers named at vault) |
|---|---|---|---|
| Insolvency remoteness | Untested onshore on fungible gold | **Statutory: Art 14(2)** | Strongest |
| What the customer owns | Legal title (strongest form) | **Beneficial interest (weaker form)** | Legal title |
| Does title move on a token transfer? | Unresolved, and it is a question about physical bars | **Yes, by the trust's own terms, self-executing** | Needs a vault instruction per transfer |
| Composability | Blocked by the unresolved title question | **Open** | Impossible |
| Works at USD 20 tickets? | Yes | **Yes** | No |
| Cost | Nil | Setup plus annual | Prohibitive |

The row that decides it is the third. **Under route 1 the question "does a blockchain transaction transfer title to a physical bar" has to be answered, and nobody in any jurisdiction has answered it.** Under route 2 that question never arises, because the bar never changes owner. The vehicle owns it on day one and owns it on day ten thousand. All that moves is a beneficial interest, and a beneficial interest is a creature of the trust deed, so the deed can say how it moves.

**This is the whole argument, and it is worth stating in one sentence: route 2 converts an unanswerable question about physical property into an answerable question about drafting.**

### 3.1 Two costs of route 2 that must be stated, not discovered

**Cost 1: the customer's ownership is beneficial, not legal.** Route 1 would have given legal title, which is stronger. Paxos concedes the same trade for PAXG, calling it "beneficial ownership... akin to a warehouse receipt", and that is the largest gold token in the market. It is the industry-normal position and it is defensible, but the marketing must not say "you own the bar outright" in a way that only route 1 would support.

**Cost 2: route 2 creates a fund-classification question that route 1 does not.** A DIFC vehicle holding property for many participants invites the question whether it is a Collective Investment Fund under DIFC Law No. 2 of 2010. Art 11 requires the purpose or effect to be participation in **profits or income** arising from acquisition, holding, management or disposal, plus either pooling or management as a whole. Allocated gold that produces no income, is not managed, and where each customer's grams are fixed, does not meet Art 11. **Note what this retrospectively justifies: decision 6 killed the profit-share dividend on securities grounds, and it turns out to have also protected the vehicle from fund classification.** Keep it dead. Confidence: Medium-High, and it goes to counsel.

**A cost we expected and may not have to pay.** The DFSA Rulebook appears to exempt from the Licensing Rules a person who is "a Trustee of a single trust" or "a non-commercial Trustee". If that holds, a single-purpose DIFC trustee company holding one trust needs no DFSA trust licence. **Confidence: Medium.** Retrieved from a rulebook mirror, not the DFSA primary text, and the primary page could not be fetched. **Verify before it reaches the client**, because it materially changes the cost of route 2.

---

## 4. How composability works under route 2

### 4.1 The mechanism, in one paragraph

The DIFC vehicle holds legal title to the allocated gold as trustee. The trust deed defines the beneficiary class as the holders of AURX from time to time, ascertained by reference to the token contract. A holder's interest arises on receiving tokens and terminates on sending them, by operation of Art 45(2) and Art 48(4)(a), and the deed displaces Art 47(2)'s writing formality under its own opening words. **Nobody assigns anything. The class simply shifts, exactly as the deed says it will.** That is what makes the token transfer self-executing, and it is why no register write, no counterparty check and no whitelist is needed for ownership to follow the token.

### 4.2 Why this is not a trick

It is worth being clear that this is a real legal construction and not a drafting dodge, because counsel will test it.

- The class is certain. Art 45(1)(b)(i) permits a class, and Art 34(2) sets the test at ascertainable now **or in the future**. A token ledger makes the class ascertainable to the exact address at every block. It is more certain than most family trusts.
- The shifting is authorised. Art 45(2) expressly lets the terms provide for addition and exclusion, and Art 48(4)(a) expressly contemplates a beneficiary ceasing to be a member of a class.
- The formality is displaced by the statute's own words, not by silence. Art 47(2) opens "Subject to the terms of a trust". This is the DIFC legislature choosing to let the deed govern, and it is the material difference from English law.
- Nothing about it is novel in substance. Unit trusts, nominee accounts and depositary receipts all work by defining entitlement against a register. The only new thing is that the register is a blockchain.

### 4.3 What the token becomes

| Layer | What it is | Who must be identified |
|---|---|---|
| Mint | Fiat in, KYC'd, gold allocated to the trust, tokens issued to a verified address | **Everyone.** Already a hard precondition of the mint (decision 34) |
| Hold and transfer | Plain ERC-20. Any wallet, any DEX, any lending market, any bridge | **Nobody**, subject to the blocklist |
| Redeem | Tokens burned, gold sold, cash paid to a name-matched bank account | **Everyone.** Rule III.E.3 makes this a rule requirement, not a choice |

**Identity at the two doors, freedom in the room.** That is the architecture, it is what PAXG, XAUT and Backed Finance all do, and it is what Rule III.E.3 was drafted to permit.

---

## 5. All the cases

Four architectures are available. Two are viable, one is a trap, one is what we currently have.

### Case A: Open base token, blocklist only (**RECOMMENDED**)

Plain ERC-20 behind an upgradeable proxy. A transfer hook that denies by exception (sanctions, court order, fraud) rather than permitting by exception. An asset-protection role able to freeze and reissue, which PAXG has and which sanctions compliance requires whatever else we do.

- **Composability:** full and immediate. Any DEX, any money market, any wallet, any bridge.
- **Ownership:** intact end to end, because the trust class follows the ledger.
- **Compliance:** KYC at mint and redeem; blocklist for sanctions; wind-down by published claim window plus burn-to-redeem.
- **Precedent:** PAXG and XAUT, roughly 97% of tokenised gold, both claiming direct allocated ownership, both openly transferable. Backed Finance operates the same split explicitly: qualified investors only at mint and redeem, no whitelist on the token, free trading on DEXs.
- **Cost to build:** lower than the current plan. An allowlist is more code than a blocklist.
- **The catch:** Aurumix holds no list of who has the gold at any given moment. It can produce one at the two doors and nowhere else.

### Case B: Open base token, no blocklist

Pure bearer. Rejected. It gives up the freeze and seize power, which is not a compliance nicety: a sanctioned address will eventually hold AURX and there must be an answer. Cache Gold is also the standing warning that a token with no control surface cannot be wound down. **The blocklist costs nothing and buys the whole regulatory conversation.**

### Case C: Permissioned base token plus an open wrapper (**DO NOT BUILD**)

The design that looks like it gets both. AURX stays whitelisted; a wrapper contract is whitelisted and issues a free-floating wAURX.

It fails on its own terms. While the wrapper holds the AURX, the member of the beneficiary class is **the wrapper contract**. The person holding wAURX is a creditor of a smart contract, not an owner of gold. Option A is alive in the base token and dead in the thing people actually trade.

This is not a theoretical objection. It is the Kinesis case, already recorded in `_explainer_ownership-structure-plain-english.md`: on its own chain, bailment, you own the gold; on its Ethereum wrapper, a separate company's terms say holders have "no legal, equitable or beneficial right, title or interest in or to the Reserves". Same brand, same ticker, two different legal positions, and the difference invisible unless you read both documents.

It can be patched by drafting the trust to look through the wrapper, but then the wrapper holders must be ascertainable anyway, so the whitelist on the base token buys nothing, and we have paid for an extra contract, an extra audit and an extra failure mode. **Worst of both.**

### Case D: Permissioned base, no wrapper (**the current design**)

ERC-3643 or an allowlist hook. Transfers only between registered holders. No DEX, no DeFi, no bridges, and per decision 37 `approve` succeeds while the transfer reverts, which breaks routers, exchange deposit sweeps and bridges in confusing ways.

It was chosen for a reason that has now been withdrawn. It survives as a fallback if counsel rejects the class-defined trust, which is why the proxy matters. But it should no longer be the default.

---

## 6. What this changes, decision by decision

| Decision | Now | Change |
|---|---|---|
| 10 Token standard: permissioned base plus optional wrapper | Open ERC-20, blocklist, freeze role, proxy | 🔄 **Reversed on the standard.** The wind-down argument survives and is answered by a claim window, not a registry |
| 23 Direct-ownership ARVA | Unchanged | ✅ Untouched and now better supported |
| 24 The token is the trigger, not the proof | Under a class-defined trust the token **is** the operative act | 🔄 Rewritten. Already flagged as overstated by 37 |
| 25 Route 2 recommended | Route 2 recommended **and now for two reasons** | ✅ Strengthened. Design assuming route 2 was the right call |
| 26 Title record, Tradeflow preferred | Register becomes evidence of the trust's holdings, not a per-customer ledger | 🔄 **Materially simplified.** The Tradeflow sub-account question drops from critical to useful |
| 33 Token ledger and title register are two halves of one ledger | Under route 2 there is **one** ledger | 🔴 **The largest revision in this file.** "An open DEX listing is incompatible with Option A" is withdrawn |
| 34 Money, then title, then token | Unchanged at mint | ✅ Untouched |
| 37 Model A bearer vs Model B named register | **Model A between the doors, Model B at the doors** | 🔄 The hybrid was not in 37's two options and it is better than either |
| 38 Identification comes from DIFC trust law | Identification comes from AML and III.E.3, at entry and exit only | 🔴 **Dead as stated.** Conclusion survives in weaker form |
| 39 ADGM Foundation defeats the ownership claim | Unchanged, and now doubly important | ✅ Confirmed. DIFC trust specifically |
| 40 Switch 3 has three landings | Lands on **3a**, the token transfer is itself the transfer, via the trust | 🔄 Resolved |
| 8 Restrict benefits, not supply | Extends cleanly: composable grams are grams without benefits | ✅ Reused |
| 46 ICS | Unaffected in structure. **One new rule needed** (§7.1) | ⚠ New open item |
| 7 The premium is zero | Now continuously visible on a public market | ⚠ **Sharper risk.** See §8.2 |
| 32 No fee on redemption | A secondary market gives holders an exit that is not a redemption | ✅ Helps. Relieves buyback pressure |
| 3 The gold float | Becomes the arbitrage mechanism that holds the market price at NAV | ✅ Strengthened, and it is a better argument for funding it |
| 6 Dividend to Gold Rewards | Also protects the vehicle from fund classification | ✅ New supporting reason |

---

## 7. The one genuinely new problem

### 7.1 ICS versus self-custody

ICS reads an account. If a customer withdraws AURX to their own wallet, Aurumix can no longer see their holding, and the Retention term of `min(Record, Standing) × Retention` has nothing to read.

This is smaller than it looks, because **ICS never measured gold in the first place** (decision 20: behaviour only, Investment Value removed entirely). Record and Standing both count contributions, and contributions arrive on the fiat rail, which is fully identified. Only Retention touches the balance.

Two options:

- **(a) A withdrawal to self-custody counts as a sale for Retention.** Simple, safe, consistent with "you can lose your status, you can never lose your gold". The 30% annual allowance means a customer can move a meaningful slice out for nothing at all.
- **(b) A customer may register self-custody addresses, which continue to count.** Better product, more machinery, and it needs address-ownership proof.

**Recommend (a) at launch and (b) later.** It is one rule and it costs nothing to reverse. ⚠ **This is a new open decision and it is Abdur's.**

### 7.2 Wind-down without a holder list

VARA Company Rulebook Part VII.A is mandatory and Cache Gold stranded 96% of supply. But re-read what actually went wrong at Cache Gold: it never burned redeemed tokens, so supply and metal diverged, and it had no way to reach anyone. The failure was operational, not architectural.

The answer for an open token is a **published claim window plus burn-on-redemption plus the freeze role**, which is what PAXG relies on and what a liquidator can actually execute. Aurumix additionally has something no gold token has: **a monthly cash touchpoint with the direct-channel book**, so the great majority of holders are contactable by construction. **State this in the wind-down plan; it is a genuine differentiator on a document we have to write anyway.**

---

## 8. What must not be done

1. **Do not build the permissioned-plus-wrapper design.** §5 case C. It kills Option A for exactly the people who use the composable version.
2. **Do not ship an allowlist "for now, we can remove it later".** You cannot. Removing an allowlist after holders exist is a migration, and the proxy will not save you from the reputational read of taking a control away. Ship the blocklist.
3. **Do not seed a DEX pool at launch.** A thin pool produces a visible, continuous discount. Midas XGZ and ORO both trade below NAV, and decision 7 already establishes that the exposure is one-directional. **Composable-capable is not the same as listed, and the gap between them is the float.**
4. **Do not put composability in the whitepaper before counsel confirms the trust construction.** A whitepaper claim binds the licence application, and III.B.2 says VARA may demand a legal opinion confirming anything in it.
5. **Do not market AURX as DeFi collateral.** Third parties integrating it is their decision. Aurumix promoting it is a Marketing Regulation problem and a classification problem, and Gold Rewards plus a yield narrative on the same asset is exactly the shape decision 6 exists to avoid.
6. **Do not give up the freeze and seize role** to look more decentralised. It is the price of the licence and PAXG pays it.
7. **Do not tell the client the September build is at risk.** It is not. This makes the build cheaper, not dearer.
8. **Do not present any of this as settled law.** It is a well-supported reading of primary text that counsel must confirm. The Art 60(6) episode is the reason to say that out loud.

---

## 9. The recommended path

The sequencing principle: **spend nothing now to keep everything open, and let counsel rather than the build decide the token.**

### Stage 1, the September build (no added cost, and it removes cost)

- Deploy behind an **upgradeable proxy with a transfer-hook stub**. This was already decision 37's recommendation, roughly a day of work, and it is now the single highest-value line in the build.
- Ship the hook as a **blocklist**. Same slot, opposite default. Less code than the allowlist currently planned.
- Keep the **freeze, seize and reissue role**.
- Keep **KYC as a hard precondition of the mint** and of redemption.
- Build **multi-tenant capable** at register and mint (decision 42, unchanged).
- **List nowhere.** The token is composable-capable and commercially unlisted.

### Stage 2, counsel (before the licence application)

Batch 4 must be re-cut. Question 1 is built on Art 60(6) and cannot be sent as drafted. §10 has the replacements.

### Stage 3, the trust deed

Draft the class-defined trust. It is a drafting exercise, not a structuring one, and it is the only genuinely new legal work this creates.

### Stage 4, after the licence and once the float is deep

Enable secondary trading in order of increasing risk: a **VARA-licensed exchange first**, then a broader CEX, then DeFi. Each step is a commercial decision with no rebuild behind it, because stage 1 already made the token capable.

---

## 10. Counsel questions, re-cut

**Batch 4 question 1 is withdrawn.** It asked whether Art 60(6) "reasonable steps" can be satisfied by wallet addresses. Art 60(6) does not impose that duty, so the question has no answer. Replace with the following, in order of value.

1. 🔴 **Can a DIFC trust validly define its beneficiary class as the holders from time to time of a specified token, so that a holder's interest arises on receipt and terminates on transfer by operation of Arts 45(1)(b)(i), 45(2) and 48(4)(a), with no separate assignment?** *This one question decides the token, the exchange strategy and the DeFi strategy.*
2. 🔴 **Can the trust deed displace the "instrument in writing" requirement in Art 47(2) under that Article's own opening words, so that a token transfer alone effects the change in beneficial entitlement?** *If yes, composability is clean. If no, we need a register write and fall back to case D.*
3. 🔴 **Does that construction satisfy VARA Annex 2 III.B.1.a and III.B.1.c?** Put the positive argument to them: because the class follows the ledger, every ARVA transaction results in a corresponding change in beneficial ownership by construction, so divergence is impossible rather than mitigated. *Ask counsel to confirm this framing before it goes to VARA in pre-application dialogue.*
4. **Would the DIFC vehicle be a Collective Investment Fund under DIFC Law No. 2 of 2010 Art 11**, given the gold produces no income, is not managed, and each customer's grams are fixed? *Confirm the Art 11 analysis and confirm that keeping the profit-share dividend dead is what preserves it.*
5. **Is a single-purpose DIFC trustee company exempt from DFSA licensing** as a trustee of a single trust or a non-commercial trustee? *This is a cost question and we cannot quote the client a number without it.*
6. **Retained from batch 4:** the ADGM Foundation s.29(1) question, and whether an ADGM trust is a better comparator. Unchanged and still live.

**Batch 1 question 1 also changes shape.** It currently asks whether title transfers with the token given allocated bars, bailment, Tradeflow registration and a permissioned token. Under route 2 that question is about physical bars that never move, so it is the wrong question. **Ask it only as the route 1 fallback**, and lead with question 1 above.

---

## 11. Corrections owed

🔴 = would be noticed in a filing or by counsel.

- 🔴 `_draft_purchase-structure.md` §6: **"Any venue listing AURX must be an approved participant with registered customers. An open DEX listing is incompatible with Option A."** No support in the rule text. Withdraw.
- 🔴 `_draft_purchase-structure.md` §6: "Both parties must be registered holders" and "An unregistered recipient cannot receive AURX at all." Both fall with the above.
- 🔴 `_draft_entities-licensing-and-payments.md` line 30: "An anonymous bearer token can never satisfy this test... So the ERC-3643 decision and the Option A decision are the same decision." Already contradicted by decision 37; now contradicted at rule text too.
- 🔴 `_draft_purchase-structure.md` §4: "A peer-to-peer AURX transfer requires both parties to be registered holders, because the gold has to move to somebody identified." Under route 2 the gold moves to nobody, ever.
- 🔴 Handoff decisions 24, 25, 33, 37, 38, 40 all need the revisions in §6 above.
- ⚠ Every drafted document assumes the customer's grams are tracked per named customer in a register. Under the class-defined trust the register records the **trust's** holdings and the token contract records the split. This is a simplification, but it touches the minting maps, the redemption maps and the invariant `sum(register sub-accounts) = tokens_outstanding`, which becomes `trust holdings ≥ tokens outstanding`.
- ⚠ The Issuance Rulebook filename confirms decision 48's correction: **VER20250519**, so 19 May 2025. Now verified twice.
- ⚠ Two claims in this file are Medium confidence and must be verified before client use: the **DFSA single-trust trustee exemption** (rulebook mirror, not primary) and the **Collective Investment Fund analysis** (statutory text via secondary source).

---

## 12. The one sentence

**We chose the DIFC vehicle to protect the customer's gold from Aurumix's creditors, and it turns out to be the thing that lets the token move freely, because gold that never changes owner never has to be re-registered when the token changes hands.**
