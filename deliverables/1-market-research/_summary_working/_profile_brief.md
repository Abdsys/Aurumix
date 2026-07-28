# Profile Writing Brief: Aurumix Market Research Summary

You are writing part of a **client-facing branded deliverable** for Aurumix, a UAE gold-backed savings token. The readers are Gaurav Khullar (founder) and Chetanya Goel (co-founder). They are commercially sharp, not crypto-native. This document goes to them and possibly to their counsel and investors.

Your job: convert raw internal research profiles into polished client-facing protocol profiles.

---

## Source

`deliverables/1-market-research/Aurumix_Protocol_Landscape.md`. Read ONLY your assigned line range. Do not read the whole file.

---

## Output format: use this EXACTLY for every protocol

```markdown
### {N.M} {Protocol Name} ({TICKER})

| Field | Detail |
|---|---|
| Issuer | {legal entity, jurisdiction, registration number if known} |
| Licence covering the token | {the licence that actually authorises issuing this token, or "None identified"} |
| Assets under management | {figure and as-of date} |
| Backing | {what one token represents, allocated or not, where the metal sits} |
| Custody fee charged to holders | {rate or 0%} |
| Yield paid to holders | {rate or None} |
| Redemption | {who can redeem, minimum size, cost} |
| Token standard | {chain and standard} |
| Reserve verification | {who checks the gold, how often, or "None published"} |

#### What it is

{2 to 4 short paragraphs. Plain language. What the product does, who buys it, how big it is, what stage it is at.}

#### Legal structure and regulatory standing

{2 to 4 paragraphs. The corporate stack, the registry-verified facts, what licence exists and what it actually covers, what is claimed versus what is authorised.}

#### Custody and reserve verification

{2 to 3 paragraphs. Where the metal is, who holds title, what is published and what is not. Separate smart-contract audits from reserve attestations explicitly.}

#### Fees, revenue and redemption

{2 to 3 paragraphs. Every fee with its rate. How the business is actually funded. Redemption terms as written in the binding documents, versus as advertised.}

#### Liquidity and distribution

{1 to 3 paragraphs. Trading volume, holder counts, venues, how they acquire customers, price versus spot.}

#### Relevance to Aurumix

{2 to 4 paragraphs, and you MAY use a short bullet list for the takeaways. This is the most important subsection. What Aurumix should copy, what it should avoid, and what the protocol proves or disproves about Aurumix's own design. Be concrete and tie back to Aurumix's actual model: monthly SIP savings, ICS scoring, a proposed dividend, a credit facility, an agent network, no physical redemption, a grams-divided-by-tokens peg.}
```

**Every protocol gets all six `####` subheads, in that order, even if a subhead is short.** Consistency across the 19 profiles is a hard requirement.

---

## What to STRIP (mandatory)

Remove every trace of the following. These are internal research artifacts and must not reach the client.

1. **Confidence labels.** No "Confidence: High / Medium / Low". If something is well established, state it plainly. If it is not established, say what is missing: "No public document establishes X", "The issuer does not disclose Y".
2. **Corrections language.** No "we previously believed", "contradicts the brief", "correction", "we had this wrong", "our earlier research said". Present every corrected fact as a plain finding. The client never learns anything was ever different.
3. **"Open items for verification" sections.** Delete entirely. Do not carry them into an appendix.
4. **Documentation quality grades.** No RICH / MODERATE / THIN.
5. **Research tooling and process.** No mention of Perplexity, search, agents, waves, queries, cost, or how the research was run.
6. **Internal cross-references.** No "§6.8", "B1", "Phase 2", "the brief", "working notes". If a point matters, state it directly.
7. **Emoji and warning glyphs.** No ⚠, ✅, ❌, 🔴.

## What to KEEP

- The substance in full. Every material fact, figure, date, registration number, rate and finding in your source range survives into the profile.
- The **Relevance to Aurumix** analysis. This is the highest-value content.
- The blunt-but-fair framing. Report what public documentation does and does not show. Attribute claims to whoever made them ("Kinesis states", "the whitepaper claims", "the issuer's terms provide"). Never present an unverified issuer claim as fact, and never assert something the research could not establish.

---

## Style rules (hard)

- **No em dashes (—) anywhere.** Use colons, commas, parentheses, or split the sentence. En dashes in numeric ranges (3–8%) are fine.
- **Active voice.** "Kinesis pays holders 15% of the fee pool", not "15% is paid to holders".
- **Specific over vague.** Real numbers, real dates, real entity names. Never "some protocols" or "several sources".
- **No throat-clearing.** Cut "It is worth noting that", "Importantly", "It should be emphasised". Start with the fact.
- **No AI tells.** Avoid: "delves into", "landscape of", "robust", "leverage" as a verb, "in the realm of", "it's important to note", "navigate the complexities", "stands as a testament", "underscores", "pivotal", "crucial", "seamless", "comprehensive suite". Avoid the "not just X, but Y" construction. Avoid tricolon padding ("faster, cheaper, and more secure") unless all three are load-bearing.
- **Vary sentence length.** Some short. Some longer with a subordinate clause. Do not write 30 sentences of identical rhythm.
- **British-leaning spelling is fine** (organisation, authorised), match the source.
- Write "per cent" as "%". Write dates as "8 September 2025".

---

## Second output: sources

At the end of your file, add:

```markdown
## SOURCES: {Protocol Name}

- {URL}
- {URL}
```

One block per protocol you covered. **Primary sources only**: company registries, regulator registers, issuer terms and conditions, prospectuses, SEC or other filings, audit and attestation reports, block explorers, official issuer documentation. **Drop** aggregator pages (rwa.xyz, CoinGecko, CoinMarketCap), wiki pages, news articles and blog posts unless that source is the only evidence for a material claim, in which case keep it. Deduplicate. Aim for 6 to 12 per protocol.

---

## Deliver

Write your file to the exact path given in your task. Do not write anywhere else. Do not edit the source landscape file. Reply with a one-line confirmation and the protocol count.
