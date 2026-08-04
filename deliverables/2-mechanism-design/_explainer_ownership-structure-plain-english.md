# Ownership and Entity Structure: Plain English Explainer

> Internal explainer, 2026-08-04. Seven questions answered in non-legal language, for briefing and for reuse in client conversation.
>
> Formal version with sources, confidence levels and open items: `_draft_entities-licensing-and-payments.md`. Call material: `Aurumix_Process_Maps_Ownership_Structure.md`.

---

## 1. What the Option A trade-off actually is

Think of it as two different kinds of hard.

**Option B is a hard cost.** The regulator says: hold gold, keep it separate, never pledge it, prove it every quarter. Expensive and annoying, but it is a *known, checkable* problem. You hire an auditor and they tell you pass or fail. You can buy your way to compliance.

**Option A is a hard uncertainty.** The regulator says: fine, if the customer genuinely owns the gold then you do not need reserve rules at all. But prove three things: (a) the customer really owns it, (b) when the token moves from one person to another, **the gold ownership moves too**, and (c) whatever the law requires to transfer ownership of a physical thing has actually happened.

Point (b) is the hard one, and here is why in plain terms. Normally, to transfer ownership of a physical object you need one of: physical handover, a signed assignment, or an entry in a register. **Nobody has confirmed that a blockchain transaction counts as any of those under UAE law.** There is no statute saying it does, and no UAE court has ruled on it.

So the concrete failure scenario is this. Customer A sells his AURX to Customer B. The token moves. Does the gold move? If the honest answer is "not automatically, our internal database is really what decides," then the token is not carrying title, VARA's test fails, and you are pushed back to Option B after you have already built and marketed the product.

**But here is the good news, and it is the actual solution.** The token does not have to perform legal magic on its own. It has to be the *trigger* for a transfer that is legally effective by some other mechanism. That is buildable:

- Bars are **allocated** and serial-numbered, so there is a specific thing being owned.
- The **customer terms** say the customer owns it and Aurumix only holds it.
- A **title register** (Tradeflow) records ownership independently of Aurumix.
- The token is **permissioned**, so it can only move to another verified, registered holder, and the token transfer and the register update are the same operation.

The legal opinion then says: title passes by the registry and contract mechanism, and the token transfer is what instructs it. That is a defensible construction.

**And notice the knock-on.** This is a second, much bigger reason for the permissioned token standard we already recommended. It is not only about protecting ICS tiers and credit eligibility. **An anonymous bearer token can never satisfy this test**, because you cannot prove who owns the gold if anyone can hold the token. So the ERC-3643 decision and the Option A decision are the same decision.

**Why it goes first.** If this opinion comes back negative, you do not adjust a number. You rebuild the product, the whitepaper and possibly the licence application. That is why it belongs before the build, not after.

---

## 2. Yes, separate. But not because the law forces it.

Correct, that is what I am recommending. Let me be precise about *why*, because the distinction matters.

The rule is not "the issuer may not hold the gold." The rule is **"the gold must not be an asset that the issuer's creditors can take."** There are three ways to achieve that:

1. **Same company, holding as caretaker under contract.** This is what Paxos and Kinesis do. It works.
2. **A separate holding vehicle** that owns the title and does nothing else.
3. **The vault holds it directly in the customers' names**, with Aurumix never in the chain of title at all.

Paxos can use route 1 because **Paxos is itself a chartered trust bank**, and banking law automatically keeps client assets off its balance sheet. Aurumix cannot copy that. A VARA licence does not make you a trust bank, and there is no VARA category that does.

So the choice is between route 1 with a contract, and route 2 with a statute behind it. I am recommending route 2 **because onshore UAE law could not give us a verified answer to the question that matters** (see answer 6). It is a belt-and-braces choice driven by uncertainty, not a legal requirement.

**What the split looks like in practice.** The DIFC or ADGM entity is passive. It is not a second business. It does not have staff, customers, or a licence. It holds title to gold for the benefit of AURX holders and nothing else. Aurumix stays in Dubai, holds the VARA licence, faces the customer, receives the money, and runs everything.

**And be honest with the client about the cost.** It adds setup and annual fees, a second jurisdiction's paperwork, and VARA will want to understand and accept the arrangement. There is a cheaper version (in-house caretaker holding plus a Tradeflow warrant) that may be adequate. This is a decision to take with counsel once we know the answer on onshore insolvency, not a decision to take now.

---

## 3. What Comtech actually did wrong

Four different names are doing four different jobs, and they do not line up.

| Name | What it does | What it is licensed for |
|---|---|---|
| "ComTech Gold" | The brand customers see | Not a company at all |
| ComTech FZCO (**DAFZA**) | The token issuer | Gold trading. Displayed **expired Feb 2024** |
| ComTech FZCO (**DMCC**) | Also on their registration page | **IT consultancy and software house** |
| **COMTECH CORE TRADING FZCO** | **Holds the bank account customers pay into** | **Appears on neither published licence.** We could not find its licence at all |

Plus a parent, Trade Fintech Ltd, a non-regulated DIFC company.

**Three consequences, and they are the reason this rule exists.**

**You do not know who you have a contract with.** The terms are with an undefined "Digitization Entity". If a customer has a problem, which company do they pursue? And critically, **the company holding their cash is not the company that owes them gold.** Those are two separate legal persons, and a claim against one is not a claim against the other.

**The money sits outside the regulated perimeter.** Whatever thin comfort the DAFZA licence offers, it does not extend to the entity actually holding customer funds. So the one place a regulator would look first is the one place no licence covers.

**Regulators read this shape as a warning sign.** Not because Comtech is necessarily doing anything wrong, but because separating the cash-taker from the promise-maker is structurally what asset-shielding looks like. In a licence application it is a fast route to a rejection.

**The rule for Aurumix:** one entity takes the money, makes the promise, and is named on the register and in the whitepaper. If a second entity holds gold, it must be named in the customer terms and the customer's claim must run directly to it. No silent third names.

---

## 4. What Rule V.B.2 means, briefly

If Aurumix goes bust, **the customers' AURX tokens are not part of what the liquidator can sell.** They are not Aurumix's property, by rule, not by promise.

That is stronger than a housekeeping obligation. Most "we keep client assets separate" rules are a duty you can breach. This one says the assets legally are not yours in the first place, so there is nothing to breach and nothing for creditors to reach. Customers do not stand in a queue behind the landlord, the staff and the tax authority.

**The catch, in one line: it protects the token, not the metal.** A safe token backed by gold that has gone missing is a safe worthless token. So this rule is necessary and not sufficient, and everything in answers 5, 6 and 7 exists to protect the other half.

---

## 5. Bailment, and how it fits the two options

**Bailment in one sentence:** I give you my thing to hold, you do not own it, and you must give it back. A coat check. The coat is never the cloakroom's property, so if the cloakroom goes bankrupt, your coat is not sold to pay their debts.

Kinesis's contract says exactly that: legal and beneficial title stays with the holder, Kinesis holds the bullion as bailee, and each holder has an undivided share of the pool in proportion to what they hold.

**Now the important bit, because I think this is where the confusion is. Bailment is not a third option alongside A and B. It is the mechanism that makes Option A work.**

- **Option A and Option B are VARA's two categories.** They describe what kind of token you are issuing.
- **Bailment is the legal construct underneath.** It is *how* you deliver Option A at law.

VARA says a direct-ownership ARVA is one where the token gives "a direct right of ownership" of the gold. Bailment is the contract that produces that result: the customer owns, Aurumix holds.

Under Option B there is no bailment, because Aurumix owns the gold and simply owes the customer value. That is a debt, and the customer is a creditor.

**One refinement worth taking from Kinesis.** They use "an **undivided interest in the total pool**," not "your specific bar." That is deliberate and practical. A customer with 12 grams cannot own a 1 kg bar. The workable middle is that the pool itself is allocated (specific serial-numbered bars set aside for customers, not the vault's general stock), and each customer owns a proportionate undivided share of that allocated pool. Given 1 AURX = 1 gram and 1 kg bars, this is almost certainly the wording Aurumix should adopt.

**And the cautionary half.** Kinesis demonstrates both structures at once. On its own chain, bailment, you own the gold. On its Ethereum wrapper, a separate company's terms say holders have "no legal, equitable or beneficial right, title or interest in or to the Reserves." Same brand, same ticker, and one is Option A while the other is effectively Option B. The difference is invisible unless you read two separate legal documents. **If Aurumix ever issues a wrapped version of AURX, it must state in the wrapper's own terms what the wrapper holder does and does not own.**

---

## 6. What the DIFC / ADGM vehicle means

Start with a fact most people outside the UAE do not know: **there are effectively different legal systems inside the same country.**

- Dubai mainland and most free zones run **UAE civil law**, in Arabic, in civil-law courts.
- **DIFC and ADGM are separate financial zones running English-style common law**, with their own courts, their own judges, and their own statutes written in English.

Trusts and foundations are common-law concepts. DIFC and ADGM have written trust and foundation laws, and both contain a clause saying, in effect: **if the person who put assets in later goes bankrupt, that does not undo the transfer.** DIFC Trust Law Article 14(2) and ADGM Foundations Regulations Article 33. That is precisely the protection we want, written down, in English, in a statute.

Onshore UAE now has a trust law too (2020, recast 2023). The problem is not that it is bad. **The problem is that we could not verify how it behaves on insolvency**, and specifically could not establish whether *fungible, commingled* gold can be reclaimed from a bankruptcy estate. Every source treated that as fact-dependent inference. No statute article, no case.

Gold is fungible. That is exactly the scenario we cannot get an answer on. **So the recommendation is: do not bet the customers' gold on an unknown when a known is available a few kilometres away.**

**The resulting shape:**

- **Issuer: Dubai, VARA-licensed.** It must be here, because **DIFC is outside VARA's remit entirely**, so you cannot hold a VARA licence from inside DIFC.
- **Title-holding vehicle: DIFC or ADGM.** Passive, small, holds gold title for the benefit of AURX holders.

Aurumix's creditors can never reach the gold, because it is not Aurumix's and the statute says the transfer cannot be unwound.

**Two honest caveats.** It costs money and adds a second jurisdiction to manage. And one thing remains untested: whether an onshore UAE court would fully respect the arrangement in a contested insolvency. DIFC and ADGM judgments are enforceable onshore through established channels, but the specific interaction with physical gold has not been litigated.

---

## 7. What the Tradeflow warrant means for Aurumix

**What it is.** DMCC runs an electronic register in Dubai that records who owns which gold bars sitting in an approved vault. When bars go into the vault, the **storage operator** issues a "warrant" against those specific bars. That warrant is the ownership record, and it can be transferred or pledged to someone else on the platform. DMCC is the registrar.

**Why it is genuinely useful to Aurumix. Four reasons.**

**It is an ownership record that is not Aurumix's own database.** Right now the only proof a customer owns gold would be Aurumix's blockchain and Aurumix's app, both of which Aurumix controls. Tradeflow is an independent third party saying the same thing. That is worth a great deal to a sceptical retail buyer and to a regulator.

**It is the natural bridge for the Option A problem in answer 1.** If a token transfer is what instructs a Tradeflow title update, you have a real answer to "does title move with the token?" The token stops needing to perform legal magic and becomes the trigger for a registry transfer that the law already recognises.

**It supports the credit facility.** Warrants can be pledged on the platform. So a lending partner gets a registered security interest over identified bars, not just a contractual promise. That makes it far easier to get a CBUAE-licensed lender to say yes.

**It is Dubai-native and already used for exactly this purpose.** DMCC built it for this, and Comtech's bars are registered on it.

**The caveat, stated plainly.** DMCC's own brochure says warrants are "electronic documents of title" and that in the storage operator's liquidation creditors cannot reach the goods. But **that claim comes from DMCC's own contractual framework, not from a UAE law that names a Tradeflow warrant as a document of title.** No UAE court has ruled on it. So it has never been stress-tested in the one situation where it matters.

**What that means practically.** Use it as one of four layers, not as the answer. If it holds up, it is strong. If a court eventually disagrees, the allocated bars, the bailment contract and the DIFC/ADGM vehicle are all still standing. That is the entire point of building four layers instead of one.

**One data point worth knowing before we recommend it.** At Comtech's last published reserve letter, of 111 kg of gold, **only 19 kg was actually on Tradeflow.** The other 92 kg sat with an unnamed "vaulting partner". So even the flagship user of the system put 17% of its gold on the register. Whatever DMCC's marketing implies, universal adoption is not the reality, and we should ask DMCC why when we approach them about fees.
