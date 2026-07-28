# Compression and Polish Brief

The protocol profiles are written and factually good. They are roughly three times too long for the deliverable. Your job is to compress each profile to **1,300 to 1,500 words** while losing **zero material facts**, and to polish the prose at the same time.

This is the final pass before design. Whatever you write goes to the client.

---

## The compression rule

**Cut words, never facts.**

Every one of these must survive: entity names, jurisdictions, registration and licence numbers, incorporation dates, event dates, monetary amounts, percentages, weights, token counts, holder counts, contract and mint addresses, clause references, named firms (auditors, custodians, refiners, counsel), and every quoted phrase from a legal or marketing document.

What to cut instead:

- **Elaboration of a point already made.** State it once, in the strongest sentence available.
- **Restating the table in the prose.** If the at-a-glance table says the licence is DAFZA 05069, the prose does not repeat the number unless it is making a further point with it.
- **Throat-clearing and framing sentences.** "This section examines...", "It is worth considering...", "Several factors contribute to..."
- **Hedged repetition.** One clear statement of what is not disclosed beats three.
- **Background the reader does not need.** Company history, founder biography, chain mechanics that are generic to all ERC-20s.
- **Long transitions between subheads.** The subhead already does that work.

Aim for high fact density. A good compressed paragraph reads like it was written by someone who knows the material cold and is short on time.

---

## Structure: keep it exactly

Do not change the heading numbers, the heading text, or the order.

- `### {N.M} {Protocol Name} ({TICKER})` stays exactly as written.
- The at-a-glance table stays, with the same field labels in the same order.
- The `####` subheads stay, in the same order, with the same names. If a profile has an extra subhead beyond the standard set, keep it.

**Tighten the table cells hard.** Several are currently full paragraphs. A table cell should be one line, or two at most. Move any argument out of the cell and into the prose below. For example, an Issuer cell should read `TG Commodities S.A. de C.V., El Salvador. Relocated from BVI, January 2025.` and not carry three sentences about ownership.

Rough budget per profile:

| Part | Words |
|---|---|
| At-a-glance table | 120–180 |
| What it is | 130–180 |
| Legal structure and regulatory standing | 250–320 |
| Custody and reserve verification | 180–240 |
| Fees, revenue and redemption | 180–240 |
| Liquidity and distribution | 110–160 |
| Relevance to Aurumix | 280–360 |

**Relevance to Aurumix is the section to protect.** If you have to run slightly long somewhere, run long there and cut harder elsewhere. It is the reason the client is reading.

---

## Polish

Apply all of these. They are the same rules the profiles were drafted under, and this pass enforces them.

- **No em dashes (—).** Colons, commas, parentheses, or split the sentence. En dashes in numeric ranges (3–8%) are fine.
- **No confidence labels, no corrections language, no "open items for verification", no documentation-quality grades, no research-tooling references, no internal cross-references (§, B1, Phase 2, "the brief"), no emoji or warning glyphs.** If any survived the first pass, remove them.
- **Attribute, do not assert.** "Comtech states", "the whitepaper claims", "the terms provide". Never present an unverified issuer claim as established fact. Never assert something the research could not establish: write "no public document establishes X" or "the issuer does not disclose Y".
- **Active voice. Specific numbers. No vague quantifiers.**
- **Kill AI tells.** Banned: "delve", "landscape of", "robust", "leverage" as a verb, "in the realm of", "it's important to note", "navigate the complexities", "stands as a testament", "underscores", "pivotal", "crucial", "seamless", "comprehensive suite", "a testament to", "at its core", "when it comes to". Avoid "not just X, but Y". Avoid opening paragraphs with "Moreover", "Furthermore", "Additionally", "Notably". Avoid three-item lists where only two items are doing work.
- **Vary sentence length.** Short sentences carry the hard facts well. Do not write thirty sentences of identical rhythm.
- Words inside a direct quotation are never edited, even if they contain a banned term.

---

## Sources

Keep the `## SOURCES: {Protocol Name}` blocks at the end of the file exactly as they are. Do not compress, reorder or edit them.

---

## Deliver

Overwrite your assigned file in place. Reply with one line per protocol giving its final word count, and flag anything you had to cut that you think should have survived.
