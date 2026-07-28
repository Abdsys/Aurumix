### 4.1 Tether Gold (XAUT)

| Field | Detail |
|---|---|
| Issuer | TG Commodities, S.A. de C.V., El Salvador. |
| Licence covering the token | CNAD stablecoin issuer register EME-0004, 19 May 2025. |
| Assets under management | ~US$2.465bn, 612,823 XAU₮, July 2026. |
| Backing | 1 XAU₮ = 1 fine troy ounce, specified LBMA bar, Swiss vault. |
| Custody fee charged to holders | 0%, permanently. |
| Yield paid to holders | None. |
| Redemption | Physical only, Swiss address. Minimum ~430 XAU₮ (~US$1.73m). |
| Token standard | ERC-20, TRC-20, XAUt0 wrapper on seven further chains. |
| Reserve verification | Quarterly BDO Italia, ISAE 3000 (Revised), reasonable assurance. No bar list. |

#### What it is

Tether Gold is the largest tokenized gold product anywhere, roughly US$2.46bn and about 19 tonnes of metal behind the float.

#### Legal structure and regulatory standing

- **Holders are said to own the gold outright.** The reserves report states reserves "are owned by the XAU₮ token holders, not by the Company", with holders holding "undivided ownership rights to gold on specified gold bars".
- **The wording does not survive the arithmetic.** 611 bars of 12.5kg sit behind hundreds of thousands of tokens, so holders cannot each own a specified bar.
- **No trust deed, bailment or custody agreement is published**, and TG Commodities does not disclose which construct governs on insolvency.
- **EME-0004 is a stablecoin registration.** No securities or commodities regulator authorises the token, and the issuer holds no VARA, DFSA or ADGM licence.

#### Custody, fees and redemption

- **The custodian is never named.** Every primary document calls it "the Custodian". Secondary sources speculate Brink's or Loomis, and none confirms.
- **There is no bar list** anywhere: no serial numbers, no refiners, no per-bar assay.
- **The attestation is strong where it exists.** Reasonable assurance under ISAE 3000 (Revised), covering physical inventory, ledger-to-onchain reconciliation and quarterly sampled assay. BDO states its own limit: "The reporting date is limited to a point in time."
- **Storage costs holders 0.00%, permanently.** Buying costs 0.25% on a 50 XAU₮ minimum. Redeeming costs 0.25% plus logistics and insurance.
- **Two 0.25% touches cannot fund perpetual Swiss vaulting.** The arithmetic closes outside the fee table, on Tether group reserve income and affiliate inventory sold at a spread, though TG Commodities has never published a statement explaining what pays for free storage.
- **Redemption is where the ownership claim thins.** ~430 XAU₮, a Swiss address, full KYC, an unpublished excluded-country list, and export left to the holder.

> **Relevance to Aurumix.** The market leader charges nothing for storage because a group-level cross-subsidy pays for it, and Aurumix has no equivalent. Any custody fee therefore has to be justified by the savings wrapper, agent servicing and credit facility rather than by the vault.

- **A plain ERC-20 costs XAU₮ nothing**, because the token carries no tier, dividend or buyback right. Aurumix's ICS state breaks on an anonymous transfer, which means ERC-3643 and a cash buyback as the only exit.
- **XAUt0 is the warning.** Nothing discloses whether a holder on Solana or TON has the same claim on Swiss gold. Settle what a wrapped AURX holder owns first.
- **Match quarterly ISAE 3000 (Revised), then beat it** by naming a custodian and publishing a bar list. XAU₮ leaves both open.

### 4.2 Pax Gold (PAXG)

| Field | Detail |
|---|---|
| Issuer | Paxos Trust Company, National Association, New York. |
| Licence covering the token | OCC national trust bank charter, uninsured, 12 December 2025. |
| Assets under management | ~US$1.79bn, ~444,808 PAXG, 28 July 2026. |
| Backing | 1 PAXG = 1 fine troy ounce, serial-numbered LBMA bar, London. Allocated. |
| Custody fee charged to holders | 0% at present. Terms reserve a right to charge by dilution. |
| Yield paid to holders | None. |
| Redemption | USD, unallocated by wire, or physical at 430 PAXG per bar (~US$1.73m). |
| Token standard | ERC-20 on Ethereum, proxy pattern with freeze role. Solana via Token-2022. |
| Reserve verification | Monthly KPMG attestation. Per-address bar lookup. No full bar list. |

#### What it is

PAXG launched in September 2019 and is the second-largest tokenized gold product, a custody receipt with an onchain wrapper.

#### Legal structure and regulatory standing

- **Beneficial ownership, not legal title.** The terms state PAXG tokens "are akin to a warehouse receipt representing your beneficial ownership of a pro rata portion of Allocated Gold".
- **Bars are reallocable.** Paxos may move which bars back which holders "for operational efficiency", so a looked-up serial is real but not permanently the holder's.
- **Insolvency protection is documented asymmetrically.** The blog asserts "segregated, bankruptcy remote accounts"; the terms carry no Paxos-insolvency clause, only a Clearing Bank disclaimer.
- **Discretion is reserved in capitals**, including a right to freeze access without advance notice.

#### Custody, fees and redemption

- **Brink's operates the vaults**, named on the Paxos blog rather than in the terms. Paxos Trust Company, N.A. is the legal custodian.
- **Attestation is monthly** by KPMG LLP since February 2025 under AICPA standards.
- **A per-address lookup is not a bar list.** A holder verifies their own slice and cannot sum the pool.
- **Creation is tiered:** 0.02 PAXG flat below 2 PAXG, then 1.000% falling to 0.125% above 800. Destruction uses the same schedule, unwaived.
- **Storage is US$0.00.** US$2.00 per month applies after 12 months without issuance or redemption, and the contract's transfer fee, historically 0.02%, is understood to be set to zero.
- **The dilution clause is the fallback.** The terms provide that "Paxos may charge storage fees to all token holders by issuing to Paxos new PAXG tokens, thereby diluting the value of existing PAXG tokens. The storage fee will be in line with industry practice, and such storage fee will be passed on to all PAXG token holders on a pro rata basis." Paxos reserved the right to break its own headline promise, disclosed it, and has never used it.

> **Relevance to Aurumix.** The dilution clause is the one genuinely transferable idea here, and firing it would break a one-token-one-ounce peg, which is why Paxos never has. For Aurumix, whose price is grams divided by tokens, the same mechanism is peg-neutral: mint to treasury, price per token falls by the fee, grams-to-tokens survives.

- **Adopt the mechanism, copy the disclosure discipline.** State the rate, state that it is charged by issuance, commit to advance notice.
- **PAXG pays no yield at US$1.79bn** and its gold sits unencumbered at Brink's. An OCC-supervised trust bank will not lend client metal, which leaves the ICS Dividend without a funding template.
- **PAXG trades at par on a live mint-and-redeem channel.** Aurumix's closed redemption is the only thing that could hold a premium.
