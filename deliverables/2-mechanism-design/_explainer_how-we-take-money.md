# How Aurumix Takes Money

> Answers client additions 1, 2 and 3 of 28 July 2026: accept stablecoin as well as fiat, determine which countries we can accept from, and identify the service providers who enable the flow.
>
> Plain language, for the client call. Full reasoning and sources: `_draft_entities-licensing-and-payments.md` section 5. Diagrams: `Aurumix_Process_Maps_Payments.md`.
>
> **Headline: the USDT plan was solving a problem Aurumix does not have.** A VARA licence already permits Aurumix to take bank transfers directly.

## 1. The one rule that explains everything

You can only accept fiat money if your company is licensed to hold customer money. This is ordinary financial regulation and gold tokens are not a special case.

That single rule explains every design choice in the market, and it explains why the current document routes Indian residents through USDT. Taking stablecoin appears to avoid needing a money licence. It is a workaround for a licensing problem, not a product decision.

## 2. What the comparable protocols do

| Protocol | Who receives the money | Where | Takes fiat directly | Excludes |
|---|---|---|---|---|
| PAXG | Paxos Trust Company | New York, NYDFS trust charter plus OCC | Yes, USD wire | EU, sanctioned countries |
| XAUT | TG Commodities Ltd | BVI, registered in El Salvador under CNAD | No, and this is why the direct minimum is 50 oz | US, Canada, North Korea, Iran |
| Kinesis | Kinesis Cayman | Cayman Islands, CIMA VASP 1877923 | Only through Banxa, a licensed third party | US persons |
| Comtech Gold | ComTech FZCO | Dubai free zone, not on VARA's register | Yes, AED in-app | Not disclosed |
| ORO | Not established | Not established | Not established | Not established |

Three models sit underneath that table.

1. **Hold a money licence and take the payment yourself.** Paxos holds a New York trust charter, so it may hold customer dollars and accepts wires.
2. **Hold no money licence, so never touch fiat.** Tether's gold entity has no banking, money transmitter or e-money licence. That is why its direct channel is 50 ounces, roughly USD 170,000, and wholesale only. Retail is pushed to exchanges.
3. **Hold no money licence, so rent one.** Kinesis uses Banxa to take the card or bank payment. Banxa holds the licences and Kinesis receives crypto. Kinesis also runs separate registered entities per region so it is locally registered where it needs to be.

Comtech is a fourth pattern and it is not one to copy. It collects AED on UAE banking rails while appearing nowhere on VARA's register.

**The finding that matters: not one of the five built its own payment rail.** The two that serve retail properly, Kinesis and Comtech, both rent the money leg. Aurumix should plan to partner, not build.

## 3. What Aurumix can do, which is better than expected

**A VARA licence permits Aurumix to receive fiat directly, as the issuer. No separate Central Bank licence is required simply to collect payment for its own token.**

VARA's Client Money Rules, Part IV, set the conditions:

- Customer fiat is Client Money. It is not owned by Aurumix and does not form part of the estate if Aurumix becomes insolvent.
- It must be paid into a designated Client Account within one calendar day of receipt.
- Money from UAE clients must be held with third-party banks in the UAE.
- Money from clients outside the UAE may land with banks abroad but must be moved to a UAE bank within 24 hours.

**Confidence: High.** Verified against the VARA rulebook.

A separate CBUAE authorisation is required for different activities: issuing an AED-referenced stablecoin, providing payment services to third parties, or operating a stored value facility. Collecting payment for your own token is none of those.

### The client account is not AED-only

The rule governs **where the account sits and that it is segregated**, not what currency it holds. UAE banks hold USD routinely.

This matters because the product is USD-priced (USD 20 minimum, USD 75 target) and gold settles against a USD fix. **Run USD as the primary client account with AED alongside**, rather than forcing every contribution through an unnecessary FX leg.

### The four payment paths

Every customer falls into one of four paths and all four end in the same account.

| Customer | Holds | What they do | What Aurumix receives |
|---|---|---|---|
| UAE resident | Fiat | Bank transfer, or UAEDDS direct debit for the recurring contribution | AED or USD into the UAE client account |
| UAE resident | USDT or USDC | Sells on a VARA-licensed exchange, withdraws to **their own** bank, then transfers | AED or USD from the customer's own account |
| International | Fiat | Either wires directly, or pays into a local collection account | USD into the UAE client account. Collection accounts sweep within 24 hours |
| International | USDT or USDC | Sells at a provider licensed **in their own country**, withdraws to their own bank, then wires | USD into the UAE client account |

**Two rules make all four work, and they should be treated as absolute by the build team:**

1. **Aurumix only ever receives bank money**, into a segregated Client Account at a UAE bank. Never a token, never from an exchange's own account.
2. **Conversion always happens on the customer's own account**, with a provider licensed where the customer is, before they pay.

**The single test: whose bank account sends the money.** The customer's is clean. An exchange's means Aurumix has arranged a payment token service and needs a further CBUAE registration.

⚠ **Two routes tested and ruled out.** Accepting USDT and off-ramping it yourself fails, because conversion is itself a licensable Payment Token Service and **routing an unregistered token through a licensed processor does not cure its status**. Embedding an exchange widget with a referral fee fails for the same reason: it makes the exchange Aurumix's agent.

### The signpost list

VARA's public register currently shows **52 licensed VASPs**. Usable by a UAE customer converting stablecoin to fiat:

| Entity | Licensed activities | Since |
|---|---|---|
| Binance FZE | Exchange incl. derivatives, Broker-Dealer, Lending, Management | 2024/04/15 |
| OKX Middle East Fintech FZE | Exchange incl. derivatives, Broker-Dealer, Lending, Management | 2024/09/17 |
| Foris DAX Middle East FZE, trading as Crypto.com | Exchange incl. derivatives, Broker-Dealer, Lending, Management | 2024/04/03 |
| Gate Technology FZE | Exchange Services | 2025/04/25 |
| HashKey MENA FZE | Exchange, Broker-Dealer | 2025/04/14 |
| BitOasis Technologies FZE | Broker-Dealer | 2024/11/29 |
| CoinMENA FZE | Broker-Dealer | 2023/11/30 |

⚠ BitOasis and CoinMENA hold Broker-Dealer rather than Exchange permissions. Confirm which category covers a customer sell-side conversion before publishing.

⚠ **The global on-ramps do not work here.** Banxa, MoonPay, Transak, Ramp and Alchemy Pay are all regulated, but in the EU and UK, and **none appears on any UAE register**. A UK registration is not a defence to a UAE regulator. Banxa works for Kinesis because Kinesis is in the Cayman Islands.

⚠ **The 24-hour rule constrains the collection-account design.** Local collection accounts abroad remain available, but they must sweep to a UAE bank inside 24 hours. This is owed to section 5.3 of the entities draft as an operational requirement, not a footnote.

## 4. Answer to addition 1: can we accept stablecoin as well as fiat

Yes, in a restricted form, and not the coin the document names.

The CBUAE Payment Token Services Regulation took effect on 31 August 2024 and the transition ended on 14 June 2025. Three rules apply.

1. **A foreign stablecoin may only be used to buy virtual assets, never to pay for services.** AURX is a virtual asset, so the token purchase leg sits inside that carve-out. The entry fee, custody fee and credit fees are payments for services and must settle in AED, USD or a licensed Dirham Payment Token.
2. **The foreign coin must be issued by a Registered Foreign Payment Token Issuer.** As at 29 January 2026, USDU (Universal Digital, ADGM) was reported as the first registered Foreign Payment Token. No evidence was found that Tether or Circle have registered. **So accepting USDT is not currently available. Accepting USDU may be.**
3. **Algorithmic stablecoins and privacy tokens are prohibited outright.**

Licensed Dirham Payment Tokens available for the fee legs:

| Token | Issuer | Status |
|---|---|---|
| AE Coin | first licensed under the regulation | Approved December 2024. Live on Network International POS and online since January 2026 |
| Zand AE | Zand Bank | Launched November 2025 |
| RAKBANK AED token | RAKBANK | In-principle approval 7 January 2026 |
| DDSC | IHC, Sirius and FAB | Approved May 2026 |

**Recommendation: design for fiat first and treat stablecoin as a supplementary rail.** Fiat is already permitted by the licence being applied for, and it is cheaper. Stablecoin is the harder path in the UAE, not the easier one.

**Confidence: High** on rules 1 and 3, verified against the CBUAE rulebook. **Medium-High** on rule 2, which rests on a regulatory tracker rather than a CBUAE register. This is the highest-value item to confirm directly with CBUAE.

## 5. Answer to addition 2: which countries can we accept from

VARA does not provide a country list. It provides a test: a licensee may serve global customers **where the activity is permissible**, and where activity is conducted outside Dubai the licensee must meet **the higher of the two regulatory standards**.

So every country is a separate decision carrying separate cost.

| Tier | Countries | Position |
|---|---|---|
| Open now | UAE | Fully regulated, retail permitted. Approximately 3.5 million Indian residents |
| Open, needs local licensing | Bahrain, Oman | Permitted, but the foreign provider must be authorised locally |
| Effectively closed | Saudi Arabia, Kuwait, Qatar | Central bank restrictions on institutions processing virtual asset transactions. Not a marketing problem, a banking one |
| Closed | India | Four independent bars |
| Open but expensive | UK, Singapore, Canada, Australia | Each requires local authorisation. None is a launch market |
| Exclude | United States | Federal and state money transmission plus securities risk |
| Exclude | North Korea, Iran, Myanmar | FATF blacklist |

⚠ **This corrects our own working figure.** The entities draft justifies the NRI refocus on approximately 9 million Indians in the GCC. Saudi Arabia, Kuwait and Qatar hold roughly 4.3 million of that number and all three are hard to serve. **The cleanly addressable GCC base at launch is closer to 3.5 to 4 million, concentrated in the UAE.** The Year 10 target of 60,000 to 100,000 still requires only 2 to 3 percent of UAE-resident Indians, so the target survives. The 9 million figure must not reach the client.

**Confidence: Medium-High.** Country positions come from comparative surveys and law firm guides. Saudi Arabia and Kuwait should be re-verified against SAMA and CBK primary sources before this appears in a client-facing document.

⚠ The FATF greylist changes at each plenary. Pull it live at drafting and do not hard-code it.

## 6. Answer to addition 3: which service providers

Four separate jobs. The current document treats them as one.

| Job | Options | Confidence |
|---|---|---|
| Company banking | Zand Bank, Commercial Bank of Dubai | High |
| Collecting the monthly SIP | UAEDDS direct debit domestically. Local collection accounts abroad via Airwallex, Wise Business, Currencycloud, Payoneer, OpenPayd or Banking Circle, subject to the 24-hour sweep | High on availability |
| Card acceptance | Adyen, PayBy, PayCaps, Stripe. Network International is the largest regional acquirer | Medium |
| Stablecoin acceptance | AE Coin already runs on Network International rails | Medium-High |
| Card issuing | Bank BIN sponsor route. Precedent: ADIB as sponsor with Al Fardan Exchange as programme manager | High |

**Cards must not be the SIP default.** A card rail costs approximately 4.25 percent on a USD 20 contribution against the 0.30 percent assumed in the entry-fee build-up. A card-collected USD 20 contribution is loss-making before any gold is purchased. Default every customer to account-to-account and treat card as a convenience for larger tickets.

⚠ No UAE payment provider publishes a policy on serving gold or virtual asset merchants. This sits in non-public onboarding criteria and cannot be closed by desk research. It remains a commercial unknown alongside the bullion dealer.

## 7. Mapping this onto the four investor types in section 11.2

**The structural problem first, because it explains why three of the four rows break.**

Section 11.2 defines its segments by **nationality and KYC document**: Emirates ID, Indian passport plus foreign address, Indian passport plus Indian address, national passport. But every rule that actually binds is about **where the customer lives**, not what passport they hold. An Indian passport holder in Dubai and an Indian passport holder in Kuwait are the same row in the client's table and completely different customers in law.

**The table is segmented by the wrong variable.** Re-cut it by country of residence.

### The four rows as written, and what each becomes

| Client's investor type | Verdict | Corrected funding route | Corrected regulatory position |
|---|---|---|---|
| UAE Resident | **Keep. This is the launch segment** | AED bank transfer or UAEDDS direct debit into a segregated Client Account. Delete "AED or USDT direct" | Correct as written. Fully within VARA |
| NRI, Indian national outside India | **Keep, but split by country of residence** | Foreign bank transfer into a local collection account, swept to a UAE bank within 24 hours. Delete USDT | Correct that FEMA does not apply to a non-resident. Add the returning-NRI position below |
| Indian Resident | **Delete the row** | No lawful route exists | Four independent bars. The row cannot be repaired |
| Other international | **Rewrite as an explicit allow-list** | Bank transfer only | Travel Rule threshold is AED 3,500, not the USD 1,000 stated |

### The NRI row, re-cut by residence

This is the row that carries the business, and it is currently one line where it should be six.

| Where the NRI lives | Position | Launch |
|---|---|---|
| UAE | Best customer in the book. Lives inside the issuer's own jurisdiction | Yes |
| Bahrain, Oman | Serviceable, requires local authorisation | Phase 2 |
| Saudi Arabia, Kuwait, Qatar | Blocked at the bank, not at the marketing. Central bank restrictions on institutions processing virtual asset transactions | No |
| UK, Singapore, Canada, Australia | Reachable, but each requires its own local licence | No |
| United States | Exclude | No |
| Returned to India | May continue to hold under FEMA section 6(4), which permits holding assets acquired while resident outside India. **Cannot add new money** | Hold only |

⚠ **That last row is a design question nobody has asked.** An NRI who repatriates to India must stop contributing but keeps their gold. **What happens to their SIP, their ICS streak and their credit facility on the day they become an Indian resident?** This is a real product state and it is not in any draft. It also affects the ICS continuity rule, since a forced stop is not the same as a missed payment.

⚠ **Note the caveat on section 6(4):** it enumerates foreign currency, foreign security and immovable property. A tokenised commodity is none of the three. Treat the returning-NRI position as a counsel question, not a settled feature.

### The segment the table does not have

There is no row for a resident of a country Aurumix has not assessed. **The product has no blocked-country list**, so the current table implicitly accepts everyone not named. That will not survive a licence application.

## 8. Checklist of document changes

- [ ] Section 11.2: delete the Indian Resident row entirely, do not soften it.
- [ ] Section 11.2: delete every USDT funding reference across all four rows.
- [ ] Section 11.2: re-cut the NRI row by country of residence, not by passport.
- [ ] Section 11.2: replace the funding column with bank transfer into a segregated Client Account.
- [ ] Section 11.2: correct the Travel Rule threshold to AED 3,500.
- [ ] Add an explicit allow-list of accepted countries and a blocked-country list.
- [ ] Fee structure: state that fees settle in fiat or a licensed Dirham Payment Token, never in a foreign stablecoin.
- [ ] Add the returning-NRI state to the SIP, ICS and credit designs.

## 9. Open items

**For the client's counsel. Both are cheap questions and both gate a design decision.**

- [ ] Confirm that a published list of licensed exchanges, with no commercial arrangement, no referral fee and no data passed, is not "arranging" a payment token service. **This is the only load-bearing assumption in the payment design.**
- [ ] VARA requires overseas client money to sit in *"Client Accounts with Third-Party **Banks** outside of the UAE."* Most local-collection providers (Airwallex, Wise Business, Currencycloud, Payoneer, OpenPayd) are **e-money institutions, not banks**, and their virtual accounts typically sit at a partner bank **in the provider's name, not Aurumix's**. Does that satisfy the rule? **This decides which providers are usable, and therefore whether a small recurring cross-border contribution is economically viable at all.** If the answer is no, every overseas investor pays an international wire fee that can exceed the entry fee on a USD 75 contribution.

**On our side.**

- [ ] Confirm the registered Foreign Payment Token list directly with CBUAE. It decides whether the stablecoin ask survives.
- [ ] Re-verify the Saudi Arabia and Kuwait positions against SAMA and CBK primary sources before the persona change is presented.
- [ ] Confirm whether a UAE payment provider will underwrite a gold-token merchant taking small recurring collections. Not answerable by desk research.
- [ ] Verify a reference to CMA Decision No. 4 of 2026, a federal virtual asset rulebook reported to require free-zone providers to comply federally as well. **Confidence: Low**, single weak source. If real it adds a layer to the licence stack in section 3.
