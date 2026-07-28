# Prompt for the next chat

Copy everything below the line into a fresh chat.

---

Finish the Aurumix client-facing Market Research Summary. Most of the work is done and verified. Read `Aurumix/handoff.md` §11 for background, but **do not re-plan the job**: the structure, the content and the build pipeline all exist and work. What remains is one compression pass and a rebuild.

## Where everything is

Working dir: `Aurumix/deliverables/1-market-research/_summary_working/`
Build dir: `Aurumix/deliverables/1-market-research/_summary_working/build/`

⛔ Never point a directory-scanning skill at `deliverables/1-market-research/`. Both `_working/` and `_summary_working/` contain duplicates of the same content and would be counted two or three times. Pass explicit file paths.

### Content files

| File | State | Words |
|---|---|---|
| `sections-1-3.md` | **Done, do not touch** | 5,004 |
| `sections-6-12.md` | **Done, do not touch** | 5,697 |
| `appendix-a.md` | **Done, do not touch** | ~700 |
| `profiles-a.md` | 4.1 Tether Gold, 4.2 Pax Gold, 4.3 Kinesis, 4.4 Pleasing Gold | 16,399 |
| `profiles-b.md` | 4.5 AZG, 4.6 Matrixdock, 4.7 MG999, 4.8 Streamex | 15,897 |
| `profiles-c.md` | 4.9 DGLD, 4.10 Aurus, 4.11 VNX, 4.12 Midas GoldZip | 12,932 |
| `profiles-d.md` | 4.13 Comtech, 4.14 ORO, 4.15 WisdomTree, 4.16 Tenbin | 11,441 |
| `profiles-e.md` | 5.1 PMGT, 5.2 Digix, 5.3 CACHE Gold | 11,368 |

`Aurumix_Market_Research_Summary.md` and `appendix-b.md` are **generated** by `build/assemble.py`. Never hand-edit them.

## The one job left: compress the five profile files

The profiles are factually excellent and roughly three times too long. At current length the document builds to **172 pages**. The agreed target was 35 to 45 pages; a realistic landing zone with full profiles retained is **65 to 75 pages**.

Run five compression agents **in parallel**, one per file, each using the `tokenomics:humanizer` subagent type. The brief already exists at `_summary_working/_compress_brief.md` and is complete: tell each agent to read it and follow it exactly.

Targets: about **1,400 words per live protocol** (so ~5,600 per file for a to d) and about **1,600 per failed protocol** (~4,800 for file e).

Tell each agent to work protocol by protocol, reading one heading's line range and replacing it with Edit, so it never holds a whole file in context.

Non-negotiables for the compression, all already in the brief but worth repeating in each agent prompt:

- **Cut words, never facts.** Every entity name, jurisdiction, registration and licence number, date, amount, percentage, weight, token count, contract address, clause reference and quoted phrase must survive.
- **Tighten the at-a-glance table cells hard.** Several are currently full paragraphs. One line each, two at most. This matters for layout as well as reading.
- **Protect the "Relevance to Aurumix" subsection.** Run long there and cut harder elsewhere.
- **Keep the exact heading numbers, heading text, subhead names and subhead order.** Files a to d have six `####` subheads per protocol; file e has seven. Do not change the count.
- **Leave the `## SOURCES:` blocks at the end of every file completely untouched.**
- No em dashes. No confidence labels, corrections language, "open items for verification", documentation-quality grades, research-tooling references, internal cross-references (§, B1, Phase numbers, "the brief"), or emoji.

A previous attempt at this died on a session limit before writing output, so re-verify word counts afterwards rather than trusting the agents' completion reports.

## Then rebuild and verify

```
cd Aurumix/deliverables/1-market-research/_summary_working/build
python assemble.py     # stitches the markdown, extracts Appendix B sources
python build.py        # emits self-contained branded HTML
node render.js         # renders the PDF and reports layout defects
python lint.py         # style and leakage lint
```

`render.js` must print **`"overflowPages": []`, `"emptyPages": []`, `"unresolvedTocEntries": []`**. Anything else is a real defect: overflow means clipped text, unresolved means a broken contents page number. `lint.py` must print `TOTAL: 0`.

Spot-check pages visually with `node shots.js 1 2 6 9 27 <n>` which writes PNGs to `build/shots/`.

Expect roughly 70 pages after compression, of which 7 are unnumbered (cover, contents pages, closing CTA, back cover).

## Finally, ship it

Copy `build/Aurumix_Market_Research_Summary.html` and `.pdf` to `deliverables/1-market-research/`, then commit and push directly to `main` (never a branch, never a PR), with the trailer:

```
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

---

## Reference: what is already built and settled

### Decisions the client already approved

- **Full profiles for all 19 protocols**, not a tiered or condensed treatment.
- **Stripped**: the corrections register, confidence grades, documentation-quality grades, sourcing caveats, and the per-protocol "open items for verification" sections (deleted outright, not moved to an appendix).
- **Kept**: the "Relevance to Aurumix" analysis on every protocol.
- **Sources**: grouped by protocol, primary sources only (registries, regulator registers, issuer terms, filings, attestations, block explorers). 202 URLs across 19 protocols.
- **Visual treatment**: typographic throughout, no image slots anywhere, so no grey placeholder boxes can ship.

### Document structure (12 sections plus 2 appendices)

Cover, Contents (unnumbered), Executive Summary (page 1), then:

1. Market Landscape
2. Nine Findings That Shape the Design
3. The Field at a Glance
4. Live Protocol Profiles (4.1 to 4.16)
5. Protocols That Failed (5.1 to 5.3)
6. Business Models and Revenue Patterns
7. Token Design and Value Capture
8. Regulatory Positioning
9. Distribution, Stakeholders and Incentives
10. Gaps, Opportunities and Open Questions
11. Two Decisions for Aurumix
12. Conclusions and Recommendations
Appendix A: Protocol Reference Table
Appendix B: Sources

Then closing CTA page and back cover.

Section 11 deliberately isolates the two client-owned decisions (how the dividend is funded, and modelling the premium at zero) immediately before the conclusions, framed as choices with evidence rather than as verdicts. Section 10.3 owns the three things the research does not establish: the retail versus institutional split of the market, whether a compliant funding route exists for Indian residents under FEMA and the Liberalised Remittance Scheme, and non-resident Indian savings behaviour.

### The build pipeline, and the bugs already fixed in it

`build.py` emits a single self-contained HTML file with the brand CSS inlined and both logos inlined as base64, so the deliverable is portable. It uses the real templates: `cover-minimal-typographic`, `special-table-of-contents`, `special-executive-summary`, `section-typographic`, `content-single-column`, `special-appendix`, `closing-cta-contact`, `closing-back-cover`.

Five defects were found and fixed. **Do not reintroduce them.**

1. **Page numbering starts after the contents.** The cover, all contents pages, the CTA and the back cover carry no `.page-number` element, and the patched `renumber()` counts only pages that have one. `makeCont()` was also patched to give a continuation page a number slot only if its source page had one, otherwise contents continuation pages get numbered.
2. **A regex was deleting every template stylesheet after `section-typographic`**, which left content pages with no height constraint so nothing ever split and text was silently clipped. Template CSS is now handled per template, and `build.py` hard-fails if an expected selector is missing.
3. **Wrapper divs must carry `data-text-role`** or the splitter cannot unwrap them and the page becomes one unsplittable block. This bit both the contents list and the appendix body. Appendix CSS is therefore scoped to `.content-area`, not `.appendix-body`, because the wrapper is removed during splitting.
4. **Contents page numbers are prefilled with a `000` placeholder** so that writing the real number cannot reflow an entry onto a second line. Without this, the settle loop split off single entries into orphan pages.
5. **Tables are atomic to the splitter**, so any table taller than a page is clipped. General tables are chunked at 9 rows with a repeated header. The nine-field profile table is detected by its `Field | Detail` header, rendered without that meaningless header row as a `profile-facts` key/value block, and chunked at 5 rows so it can always split.

`render.js` measures real element bottoms against the content area rather than `scrollHeight`, because a trailing margin inflates `scrollHeight` and produces false overflow reports.

Each protocol starts on a fresh page. Headings are uniform throughout: section dividers carry the number, content pages use `h2.content-heading` with a gold rule for `N. Title`, `h3` for `N.M Subtitle`, and `h4` for the profile subheads.

### Verified state of the last build

172 pages, 165 numbered, 81 contents entries all resolved, zero overflow, zero empty pages, lint total 0. Cover, contents, executive summary, section dividers, content pages, appendices, CTA and back cover were all visually inspected and render correctly.
