# Aurumix Whitepaper: Page-Sequence Plan (v2, single column)

> Step 4 of the whitepaper process (page-sequence-designer). Consumed by the document-designer (assembler) in step 5.
> Copy: `deliverables/6-whitepaper/Aurumix_Whitepaper.md`. Diagrams: `deliverables/6-whitepaper/Aurumix_Whitepaper_Process_Maps.md` (WP-01 to WP-25).
> Template system: Tokenomics.net branded-docs-main, portrait US Letter (8.5 x 11 in). Content area 7.5 in wide x 9.8 in tall.
> Layout model: the Stockpile whitepaper (`Stockpile/deliverables/6-whitepaper/supporting-docs/Stockpile_Whitepaper-page-sequence-plan.md`, built as `Stockpile/deliverables/6-whitepaper/final/Stockpile_Whitepaper.html`). It uses content-only templates, prose that auto-continues across plain portrait pages, and every diagram inline as a full-width `<figure>` in the flow.
> **Planned length: 37 pages. Hard ceiling: 40.** See section 7.

**Why v2:** the user rejected v1 because of its two-column layouts (split diagram-and-text rows, 2x3 finding grid, side-by-side rule lists, a sidebar-callout page, a two-column glossary). v2 keeps v1's copy-to-block mapping and figure register. The layout is rebuilt in one column from top to bottom.

---

## 0. Hard layout rules (apply to every page)

1. **One column only.** Text, tables, figures and callouts stack vertically. Nothing sits beside anything else. No CSS grid or flex rows with two or more content children, no `column-count` above 1, no floats.
2. **Allowed in-flow elements:** paragraphs, lists, full-width tables, full-width centred figures, a **stat row** (three stats across: values and labels only, never text columns), a **full-width callout band**, and a **full-width worked-example box**. Nothing else.
3. **Figures:** each is a centred `<figure>` on its own row with its caption below. Full content width by default. Tall narrow ladders get a narrower `max-width` (listed in section 5), still centred, with empty space on both sides. **Rendered diagram text must be at least 9pt (12px).** If a figure falls below that, widen it. Never shrink it.
4. **Removed templates and blocks:** `content-two-column`, `content-sidebar-callout`, `content-pull-quote`, `content-formula-display`, `content-inline-image`, all `visual-*` pages, and v1's SPLIT and 2COL blocks. `special-appendix` must be overridden to `column-count: 1` (the template ships with 2).
5. **Headings:** Libre Baskerville 700 for all headings, sentence case. Section (H2) 22pt with "N." numbering. Subsection (H3) 16pt with "N.M" numbering. Sub-subsection (H4) 13pt, if used. Back matter headings are unnumbered (Glossary, References, Important notice). Every heading has `break-after: avoid` and stays with its first block.
6. **Flow:** each part is one `data-auto-continue` flow on content pages. Sections inside a part start with an inline H2 and do **not** force a page break, the same way Stockpile runs subsections inside a section. The only forced breaks are: part dividers, the §1 executive summary page, the start of §15 (content-data-table), and the back matter.

---

## 1. Document Profile

- **Type:** Whitepaper for the public and the market (savers, partners, VARA). It explains the product: the problem, how it works, the rules, fees, legal status and risks.
- **Section count:** 17 numbered H2 sections plus 3 unnumbered back-matter sections (Glossary, References, Important notice), 46 H3 subsections. About 5,300 words, 25 tables, 25 diagrams.
- **Estimated pages:** 37 (cover, contents, 6 part dividers, 27 content pages, back matter, back cover). Worst case after contingencies: 40.
- **Orientation:** Portrait throughout.
- **Hero sections:**
  1. **§1 Aurumix in brief.** The whole product on one page, so it gets the executive-summary page: three headline stats, the six benefits as a stacked numbered list, and WP-01.
  2. **§3 How Aurumix works.** The trust case (allocated bars, the DIFC trust, one token per gram). The "one AURX = one gram" paragraph gets a full-width callout band, and WP-02 and WP-03 run at full width.
  3. **§15 Fees at a glance.** The "no storage fee, no exit fee" message. It is the only section whose table is its centrepiece and has three stats taken word for word from the table, so it gets the content-data-table page.
- **Diagrams available:** 25 finished branded Mermaid diagrams (WP-01 to WP-25). Each is placed once, inline, at its placeholder position (register in section 5).
- **Design approach:** The rhythm comes from the page structure, as in Stockpile: a full-page part divider, then a plain single-column flow in which prose, full-width tables and full-width figures alternate. Figures break up the text about every half page. Callout bands, worked-example boxes and two stat rows mark the key points without adding a second column. Rich page templates are used only where the content fills their slots and the page break costs no space.

---

## 2. Signal Inventory

| H2 Section | H3 | Signals Detected | Primary Signal | Selected treatment | Selection Reason |
|---|---|---|---|---|---|
| 1. Aurumix in brief | 0 | Summary opener; 6 bold-labelled benefit bullets; 3 headline facts; key closing sentence; WP-01 | Executive summary | `special-executive-summary` (own page) | Whitepaper summary (skill rule). Slot fit: title = H2; body = first paragraph; stats = three facts from the copy; findings = the six bullets, stacked one under another (the template's native single-column list). Hero. |
| 2. The problem | 0 | Comparison table (4 rows); 2-line lead | Small table | Single-column flow, table inline | Four rows and no stats, so a data-table page would be an anti-pattern. |
| 3. How Aurumix works | 4 | Spec table (6 rows); key principle paragraph; trust aside; WP-02, WP-03 | Diagram pairing + key principle | Single-column flow; callout band on the 3.2 principle paragraph | The principle paragraph is a whole copy block, so the band adds no duplicate text. Both figures run full width. Hero. |
| 4. Who can join | 0 | Standalone rule line; eligibility table (5 rows); two short paragraphs | Aside/Note | Single-column flow; callout band on the rule line | v1 put the table and text in a split row. Now the table runs full width and the paragraphs follow below it. |
| 5. Buying gold | 7 | SIP vs spot table; WP-19 steps; WP-20 and WP-04 sequences; principle "money, then title, then token"; worked example (John); WP-21 ladder; WP-05 loop | Process + worked example | Single-column flow; band on the 5.4 principle; worked-example box for 5.5 | A process-steps page would duplicate WP-19 (the steps exist only in the diagram). Six figures run inline, and each ladder is centred at a narrow width. |
| 6. Selling your gold back | 2 | Three facts (price, fee, payment); example (Sophie); WP-06; 3-row table; 3 bullets | Stat facts + sequence | Single-column flow; **stat row** from the three fact bullets | The three bullets become the stat row, so the copy is used once in a new form. 6.1 and 6.2 are stacked (v1 had them side by side). |
| 7. The Investor Conviction Score | 5 | Thesis sentence inside 7.1; 3 tables; example (Mark); key reassurance sentence; WP-07, WP-22, WP-08, WP-09 | Key quote (borderline) | Single-column flow; band on the 7.5 bold reassurance paragraph | `content-pull-quote` is not allowed and would repeat a sentence. The thesis stays in its paragraph. Four figures are inline; WP-22 and WP-08 are centred at 60%. |
| 8. The five benefits | 3 | Benefits matrix (8 x 6); WP-10; two short rule lists | Data table | Single-column flow, matrix full width | v1's stats were worked out from the table rather than taken from the copy, and a forced page break here would leave a mostly empty page (see section 7). The matrix still runs at full width. The rule lists are stacked. |
| 9. Credit and the Gold Card | 4 | Bold formula line with 3 defined terms; example (Emma); 2 threshold tables; warning sentence; WP-11, WP-23, WP-24, WP-12 | Single formula | Single-column flow; band on the formula line; band on the 9.4 warning sentence | `content-formula-display` is not allowed. The formula is already a plain-language bold sentence, and a band shows it just as well. |
| 10. Gold Rewards | 0 | Definition sentence; 4-row rate table; example (Emma); 3-item funding list; WP-13 | Definition + sequence | Single-column flow; worked-example box | The table and the example are stacked (v1 had them side by side). |
| 11. Family Portfolio and succession | 4 | 4 small tables incl. does / does-not table; price bullets; example (Emma); WP-14 | Small tables + flow | Single-column flow; worked-example box for 11.4 | 11.3 stays a normal full-width table, as in the copy (v1 turned it into two text columns). |
| 12. Partners, agents and referrals | 3 | WP-15 sequence; bullets; two short subsections | Sequence | Single-column flow | 12.2 and 12.3 are stacked (v1 had them side by side). |
| 13. The AURX token | 4 | Token facts (6 rows); WP-16; controls (5 rows); short aside | Tables + diagram | Single-column flow | Two tables of equal weight, neither a source of stats. WP-16 is centred at 80%, with its bullets below it. |
| 14. Safety and transparency | 4 | Bold backing rule; report list; numbered 4 layers; WP-17 | Key rule | Single-column flow (own flow, fills one page); band on the 14.1 rule paragraph; 14.3 layers as a numbered stack in process-steps style | The four layers are an ordered list with bold titles, so they take the process-steps markers (a number circle and a connector line, one column). The section fills about one page, so §15 can start fresh. |
| 15. Fees at a glance | 2 | Fee table (7 rows) is the centrepiece; stats "2% to 5%", "None", "None" taken from the table; WP-18 | Data table | `content-data-table` (starts flow 6b) | Table is the centrepiece and all three stats appear word for word in it. The page starts clean because §14 fills the page before it. Hero. |
| 16. Legal and regulatory status | 4 | Regulators table; licence-gate paragraph; WP-25 ladder; positions table (6 rows); 3 bullets | Aside + narrow diagram | Continues flow 6b (single column); band on the licence-gate paragraph; WP-25 centred at 55% | v1 put WP-25 and the callout in a sidebar. Both now sit in the flow at the placeholder position. |
| 17. Risks | 0 | Risk table (10 x 3) is the whole section | Data table | Continues flow 6b; full-width table | No three honest headline stats. The table is atomic, keeps its full width and closes the body on a strong block. |
| Glossary | 0 | 17-term table | Reference | `special-appendix`, **one column** | Run-in definition list, one term per line. v1 used a two-column list, which the user rejected. |
| References | 0 | 5 numbered sources | Reference | Same appendix page | End matter. |
| Important notice | 0 | 5 legal paragraphs | Legal | Same appendix page | End matter, full text at 9pt. |

---

## 3. Global Layout Spec for the Assembler

### 3.1 Parts and dividers (6 full-page `section-typographic` dividers)

| Part | Divider number / title | Sections | Divider subtitle (section list) |
|---|---|---|---|
| Part 1 | "Part 1" / What Aurumix is and how it works | 1-4 | Aurumix in brief · The problem · How Aurumix works · Who can join |
| Part 2 | "Part 2" / Buying and selling | 5-6 | Buying gold · Selling your gold back |
| Part 3 | "Part 3" / The score and its benefits | 7-8 | The Investor Conviction Score · The five benefits |
| Part 4 | "Part 4" / Credit, card and rewards | 9-10 | Credit and the Gold Card · Gold Rewards |
| Part 5 | "Part 5" / Family, partners and the token | 11-13 | Family Portfolio and succession · Partners, agents and referrals · The AURX token |
| Part 6 | "Part 6" / Safety, fees, legal and risks | 14-17 | Safety and transparency · Fees at a glance · Legal and regulatory status · Risks |

Back matter follows Part 6 with no divider. Section numbers 1-17 stay as in the copy.

### 3.2 Typography

- Body: Libre Franklin 10pt, line-height 1.45, 7px paragraph gap.
- H2 (inline section heading): Libre Baskerville 700, 22pt, "N. Title", gold 1.5px rule under it, 0.3 in space above (0 at page top).
- H3: Libre Baskerville 700, 16pt, "N.M Title", 10px above and 4px below.
- H4 (if needed): Libre Baskerville 700, 13pt. The copy has no H4. "How it is funded:" in §10 stays a bold run-in line.
- Tables: 9pt, cell padding 4px 7px, charcoal header row, striped rows, full content width, atomic (`break-inside: avoid`). Bold cells stay bold, as in the copy.
- Captions: 8.5pt, concrete grey, centred: "Figure N. {Title}. {one-line description}". The title and line come from the process maps file (the heading and the sentence under it).

### 3.3 Block vocabulary (all single column)

| Code | Block | Notes |
|---|---|---|
| **TXT** | Paragraphs and lists as in the copy | |
| **TBL** | Full-width table | Never beside anything. |
| **FIG(w%)** | Centred figure plus caption on its own row | `w%` = figure max-width. 100% unless section 5 says otherwise. |
| **STAT3** | Three stat cards in one row (value + short label) | Values and labels only. Styling from the exec-summary/data-table stat cards. Used twice (§6, §15) plus the §1 template stats. |
| **BAND** | Full-width callout band: stone-light fill, gold left rule, 11pt bold sentence | Holds a **whole copy paragraph** moved into the band, never a repeated one. |
| **EX** | Full-width worked-example box, small-caps label "Worked example", stone-light fill | Holds the example sentence(s) and its table, stacked. |
| **STEPS** | Numbered stack in process-steps style (gold number circle, connector line, bold title, text) | One column. Used only for 14.3. |

**BAND list (9, no more):** §1 closing line · 3.2 first paragraph · §4 rule line · 5.4 first paragraph · 7.5 bold paragraph · 9.2 formula line · 9.4 "Gold can fall 13%..." · 14.1 paragraph · 16.2 second paragraph.

### 3.4 Diagram rendering rules

- Mermaid in the browser, `startOnLoad: false`, run after auto-continue finishes (standard shell pattern).
- Global config (layout only, no node or label changes): `themeVariables.fontSize: '14px'`; `flowchart: { nodeSpacing: 28, rankSpacing: 32, useMaxWidth: true }`; `sequence: { mirrorActors: false, actorMargin: 40, width: 130, height: 46, messageMargin: 30, boxMargin: 8, noteMargin: 8, useMaxWidth: true }`. Add the same keys to each diagram's own `%%{init}%%` block. Colours, text and structure stay exactly as in the process maps file.
- Width: the figure container takes the `max-width` in section 5, centred (`margin: 0 auto`). Don't scale an SVG up to more than 1.25x its natural size, so narrow ladders do not grow very tall.
- Readability check: after render, measure the smallest SVG text. If it is under 12px, raise that figure's max-width by 10% steps until it passes.
- Remove every `[DIAGRAM: WP-xx ...]` line and the brief paragraph under it. Those are designer notes. The figure takes their place, in the same position.
- Figures are atomic, so the caption stays with the figure. The H3 directly above a figure-led subsection (5.2, 5.6, 15.2) is kept with the figure (`break-after: avoid`).

### 3.5 Audit rules

- Zero overflow inside the content area. No page under 35% fill except the last page of a part (it may go to 30%).
- No element anywhere with two content children side by side. The assembler checks for computed `display: grid|flex` with more than one child in `.content-area`. The STAT3 row is the only allowed exception.

---

## 4. Cover, Contents and Back Cover

- **Cover (`cover-minimal-typographic`):** title "Aurumix Whitepaper"; subtitle "Allocated gold, saved by the gram"; meta lines "Token: AURX (1 AURX = 1 gram of gold)", "Issuer: Aurumix, Dubai", "Whitepaper, September 2026". Tokenomics.net branding as in the template.
- **Contents (`special-table-of-contents`):** one column. Six part headings, each with its numbered sections (1-17), then Glossary, References, Important notice (unnumbered). 26 entries, one page. Page numbers come from `data-toc-id` at render time. This page is where the copy's own "Contents" list goes (used once).
- **Back cover (`closing-back-cover`):** template tagline and legal line, with Tokenomics.net branding kept.

---

## 5. Diagram Placement Register

Figure numbers follow reading order. Every figure goes at its placeholder position, next to the text that refers to it.

| Fig | WP | Title | Section | Page | Width | Est. height | Text around it |
|---|---|---|---|---|---|---|---|
| 1 | WP-01 | Aurumix at a glance | 1 | 4 | 100% | 1.7 in | After the §1 closing band |
| 2 | WP-02 | One token, one gram | 3.3 | 6 | 85% | 3.3 in | After 3.3's two paragraphs |
| 3 | WP-03 | Who does what | 3.4 | 6 | 100% | 3.7 in | After 3.4's paragraph |
| 4 | WP-19 | Getting started | 5.2 | 9 | 55% | 4.2 in | Right under the 5.2 H3; bank-money sentence below |
| 5 | WP-20 | Two ways to pay | 5.3 | 10 | 100% | 4.6 in | After the two 5.3 bullets |
| 6 | WP-04 | What happens when you pay | 5.4 | 10-11 | 100% | 4.2 in | After the three 5.4 bullets |
| 7 | WP-21 | Large purchases | 5.6 | 11-12 | 55% | 2.9 in | Right under the 5.6 H3; Travel Rule sentences below |
| 8 | WP-05 | The gold float | 5.7 | 12 | 100% | 2.0 in | After the 5.7 float paragraph |
| 9 | WP-06 | Selling your gold back | 6 | 13 | 100% | 3.7 in | After the Sophie example |
| 10 | WP-07 | The first six months | 7.2 | 15 | 100% | 1.6 in | After the two 7.2 bullets |
| 11 | WP-22 | How the score is worked out | 7.3 | 16 | 60% | 2.8 in | After the measures table; four rule bullets below |
| 12 | WP-08 | The tiers | 7.4 | 16-17 | 60% | 3.3 in | After the "Thresholds are fixed" sentence |
| 13 | WP-09 | What a missed month costs | 7.5 | 17-18 | 70% | 3.9 in | After the 7.5 band; pause paragraph below |
| 14 | WP-10 | The five benefits by tier | 8.1 | 18-19 | 90% | 3.2 in | After the matrix and "The biggest step" sentence |
| 15 | WP-11 | One credit line, two ways to use it | 9.1 | 21 | 80% | 3.1 in | After the two 9.1 bullets |
| 16 | WP-23 | Your borrowing limit | 9.2 | 21 | 100% | 0.8 in | After Emma's table; pledged-grams paragraph below |
| 17 | WP-24 | The Gold Card by tier | 9.3 | 22 | 60% | 2.7 in | After the 9.3 lead; upgrade paragraph below |
| 18 | WP-12 | If the gold price falls | 9.4 | 22-23 | 70% | 3.0 in | After the 9.4 warning band |
| 19 | WP-13 | How Gold Rewards is paid | 10 | 23-24 | 100% | 3.7 in | After the reward-grams sentence |
| 20 | WP-14 | How family gold moves | 11.2 | 26 | 100% | 3.1 in | After the probate paragraph; loan paragraph below |
| 21 | WP-15 | The partner channel | 12.1 | 27-28 | 100% | 3.9 in | After the 12.1 lead; two bullets below |
| 22 | WP-16 | Identity at the two doors | 13.2 | 29 | 80% | 2.7 in | After the 13.2 lead; three bullets below |
| 23 | WP-17 | Layers of protection | 14.2 | 32 | 100% | 1.9 in | After the four report bullets |
| 24 | WP-18 | How Aurumix earns | 15.2 | 33 | 90% | 3.4 in | Right under the 15.2 H3; closing paragraph below |
| 25 | WP-25 | Path to launch | 16.2 | 34 | 55% | 3.6 in | After the 16.2 licence-gate band |

All 25 are placed once. Nothing sits beside any figure.

---

## 6. Page Sequence

"Flow" marks a page that starts a `data-auto-continue` flow. "cont." marks an expected continuation page (auto-generated, listed so the budget can be checked). Page breaks inside a flow are estimates, and the renderer decides the exact point. Est. fill = content height / 9.8 in.

| # | Template ID | Section | Content Mapping (blocks top to bottom) | Est. fill | Design Rationale |
|---|---|---|---|---|---|
| 1 | cover-minimal-typographic | — | Title, subtitle, token / issuer / date meta | — | No hero image. A typographic cover suits the calm, institutional tone. |
| 2 | special-table-of-contents | — | 6 parts, sections 1-17, then Glossary, References, Important notice | ~55% | 4+ sections needs a TOC. The part grouping shows the route through the document. |
| 3 | section-typographic | Part 1 | "Part 1" / "What Aurumix is and how it works" + section list | — | Part divider (user's choice: full-page part dividers). |
| 4 | special-executive-summary | §1 | Title "1. Aurumix in brief" (22pt heading style); body = first paragraph; STAT3 = "1 AURX" / "Equals one gram of gold", "USD 20" / "Monthly plan minimum", "None" / "Storage or exit fee"; findings = the six bullets as a **stacked numbered list** (bold label as finding-title, rest as finding-body); BAND "Holding AURX earns no payments. Steady saving changes only the terms you get on Aurumix's services."; FIG WP-01 (Fig 1). | ~85% | Signal: executive summary. Every slot fills from the copy. The findings list is the template's native one-column list (v1's 2x3 grid is removed). Hero. |
| 5 | content-single-column (flow) | §2, §3.1-3.2 | H2 "2. The problem: saving in gold today"; lead; TBL routes (4 rows). H2 "3. How Aurumix works"; 3.1 H3 + TBL gold (6 rows); 3.2 H3 + BAND (first paragraph) + second paragraph. | ~80% | Signal: small tables and a key principle. The table stays inline (anti-pattern rule). The band marks the core promise. |
| 6 | cont. | §3.3-3.4 | 3.3 H3 + two paragraphs; FIG 85% WP-02 (Fig 2); 3.4 H3 + paragraph; FIG WP-03 (Fig 3). | ~95% | Each figure sits under the text it illustrates. Hero section: both figures at full size. |
| 7 | cont. | §4 | H2 "4. Who can join"; BAND "Your country of residence decides, whatever your passport."; TBL eligibility (5 rows); NRI paragraph; KYC paragraph. | ~38% | Aside signal set as a band. The table runs full width and the paragraphs follow below it (no longer a split row). Last page of Part 1. |
| 8 | section-typographic | Part 2 | "Part 2" / "Buying and selling" + section list | — | Part divider. |
| 9 | content-single-column (flow) | §5.1-5.2 | H2 "5. Buying gold"; 5.1 H3 + TBL SIP vs spot (4 x 3) + note line; 5.2 H3 + FIG 55% WP-19 (Fig 4) + "Aurumix accepts bank money only..." | ~82% | No process-steps page: WP-19 already shows the six steps. The ladder is centred at 55% with nothing beside it. |
| 10 | cont. | §5.3-5.4 | 5.3 H3 + lead + two bullets; FIG WP-20 (Fig 5); 5.4 H3 + BAND "Every purchase follows one order: money, then title, then token. If the gold cannot be placed in your name, no token is created." + 3 bullets. | ~88% | The sequence runs at full width directly under the text it shows. The principle paragraph becomes the band. |
| 11 | cont. | §5.4-5.6 | FIG WP-04 (Fig 6); 5.5 H3 + EX (John sentence, TBL 5 rows, "A year later...", "The entry fee is the only charge..."); 5.6 H3 + FIG 55% WP-21 (Fig 7) + two sentences. | ~92% | Worked example as a full-width box. The size ladder is centred and narrow. |
| 12 | cont. | §5.7 | 5.7 H3 + lead + 3 bullets + "The float never counts as backing..." ; FIG WP-05 (Fig 8). | ~45% (break depends on P11) | The loop diagram sits under the bullets that describe it. |
| 13 | cont. | §6 | H2 "6. Selling your gold back"; lead; STAT3 = "Next LBMA price" / "Price", "None" / "Fee", "Your own bank" / "Payment, in AED or USD"; checks sentence; Sophie example (italic, as in copy); FIG WP-06 (Fig 9); 6.1 H3 + TBL (3 rows) + note; 6.2 H3 + 3 bullets. | ~95% **TIGHT** | Signal: three facts from the copy form the stat row (the bullet list becomes the stat row, so the copy appears once). 6.1 and 6.2 are stacked (v1 had them side by side). If it overflows, 6.2 moves to a continuation page (contingency C1). |
| 14 | section-typographic | Part 3 | "Part 3" / "The score and its benefits" + section list | — | Part divider. |
| 15 | content-single-column (flow) | §7.1-7.3 | H2 "7. The Investor Conviction Score"; 7.1 H3 + two paragraphs; 7.2 H3 + paragraph + 2 bullets; FIG WP-07 (Fig 10); 7.3 H3 + lead + TBL measures (3 rows). | ~72% | Pure prose with inline figure and table. The pull-quote template is not used (not allowed, and it would repeat the 7.1 sentence). |
| 16 | cont. | §7.3-7.4 | FIG 60% WP-22 (Fig 11); four rule bullets; 7.4 H3 + TBL tiers (5 rows x 4); "Thresholds are fixed..." sentence. | ~70% | The score diagram is centred above the rules that qualify it (v1 had them side by side). |
| 17 | cont. | §7.4-7.5 | FIG 60% WP-08 (Fig 12); 7.5 H3 + lead + TBL Mark (3 rows) + "When Mark resumes..." + BAND "A lower score changes your benefits only. It never touches your gold. Your grams fall only when..." | ~68% | The ladder is centred. The reassurance paragraph becomes a band. |
| 18 | cont. | §7.5, §8.1 | FIG 70% WP-09 (Fig 13); pause paragraph; H2 "8. The five benefits"; 8.1 H3 + lead + TBL benefits matrix (8 x 6). | ~85% | The matrix runs full width inline. §8 does not start a forced page (see §8 in the inventory). |
| 19 | cont. | §8.1-8.3 | "The biggest step is Silver to Gold..." sentence; FIG 90% WP-10 (Fig 14); 8.2 H3 + 3 bullets; 8.3 H3 + 2 bullets + closing line. | ~65% | The benefits fan sits under its matrix. 8.2 and 8.3 are stacked (v1 had them side by side). Last page of Part 3. |
| 20 | section-typographic | Part 4 | "Part 4" / "Credit, card and rewards" + section list | — | Part divider. |
| 21 | content-single-column (flow) | §9.1-9.2 | H2 "9. Credit and the Gold Card"; 9.1 H3 + lead + 2 bullets; FIG 80% WP-11 (Fig 15); 9.2 H3 + BAND "Limit = eligible grams × gold price × your loan-to-value (LTV)." + 3 bullets + Emma lead + TBL (3 rows); FIG WP-23 (Fig 16). | ~96% **TIGHT** | Signal: a single formula. It is set as a band in place of `content-formula-display` (not allowed). The pledged-grams paragraph may start the next page. |
| 22 | cont. | §9.2-9.4 | Pledged-grams paragraph; 9.3 H3 + lead; FIG 60% WP-24 (Fig 17); upgrade paragraph; 9.4 H3 + lead + TBL thresholds (4 rows) + "Sales are at the LBMA Gold Price..." + TBL fall-before-sale (4 x 3) + BAND "Gold can fall 13% within a year. Borrowing less than your limit gives you more room." | ~95% | Both 9.4 tables run full width and stack. The warning sentence becomes a band below them (v1 had it in a split row). |
| 23 | cont. | §9.4, §10 | FIG 70% WP-12 (Fig 18); H2 "10. Gold Rewards"; definition paragraph (bold lead as in copy); TBL rates (4 rows); EX (Emma, USD 800); "How it is funded:" + numbered list (3); reward-grams sentence. | ~82% | The rate table and the worked example are stacked (v1 had them side by side). |
| 24 | cont. | §10 | FIG WP-13 (Fig 19). | ~40% | The sequence closes Part 4. It may join P23 if P22 breaks early. |
| 25 | section-typographic | Part 5 | "Part 5" / "Family, partners and the token" + section list | — | Part divider. |
| 26 | content-single-column (flow) | §11.1-11.2 | H2 "11. Family Portfolio and succession"; 11.1 H3 + TBL (2 rows) + note; 11.2 H3 + TBL triggers (3 rows) + probate paragraph; FIG WP-14 (Fig 20); loan paragraph. | ~88% | The flow diagram sits under the triggers it routes. |
| 27 | cont. | §11.3-11.4, §12 opener | 11.3 H3 + TBL does / does-not (4 rows, as in copy); 11.4 H3 + 4 bullets + EX (Emma sentence, TBL 3 rows, "Fees are charged at registration..."); H2 "12. Partners, agents and referrals"; 12.1 H3 + lead. | ~70% | 11.3 is the copy's own table at full width (v1 made it two text columns). The price bullets and the example box are stacked. |
| 28 | cont. | §12 | FIG WP-15 (Fig 21); 2 bullets; 12.2 H3 + paragraph; 12.3 H3 + 4 bullets + "The programme runs only once VARA has confirmed it." | ~77% | 12.2 and 12.3 are stacked (v1 had them side by side). |
| 29 | cont. | §13.1-13.2 | H2 "13. The AURX token"; 13.1 H3 + TBL token facts (6 rows) + "AURX has no token sale..."; 13.2 H3 + lead; FIG 80% WP-16 (Fig 22); 3 bullets + wallet paragraph. | ~92% | WP-16 is centred with its bullets below it (v1 had them side by side). |
| 30 | cont. | §13.3-13.4 | 13.3 H3 + TBL controls (5 rows); 13.4 H3 + paragraph. | ~32% | Last page of Part 5. May merge with P29 if it breaks early. |
| 31 | section-typographic | Part 6 | "Part 6" / "Safety, fees, legal and risks" + section list | — | Part divider. |
| 32 | content-single-column (flow 6a) | §14 | H2 "14. Safety and transparency"; 14.1 H3 + BAND (the full backing-rule paragraph); 14.2 H3 + lead + 4 bullets; FIG WP-17 (Fig 23); 14.3 H3 + lead + STEPS (the 4 layers) + "If one layer is challenged..."; 14.4 H3 + paragraph. | ~91% | The key rule becomes the band. The numbered layers take the process-steps style in one column. The section fills one page, so §15 can start a clean page. |
| 33 | content-data-table (flow 6b) | §15 | Section title "15. Fees at a glance"; STAT3 = "2% to 5%" / "Entry fee, less your tier discount", "None" / "Storage fee", "None" / "Exit fee"; 15.1 H3 + TBL fees (7 rows) + paragraph; 15.2 H3 + FIG 90% WP-18 (Fig 24) + closing paragraph. | ~97% **TIGHT** | Signal: the table is the centrepiece and the three stats are taken word for word from it. Slot fit verified. Hero ("no storage fee, no exit fee"). If it overflows, the closing paragraph goes to P34. |
| 34 | cont. | §16.1-16.3 | H2 "16. Legal and regulatory status"; 16.1 H3 + TBL regulators (3 rows); 16.2 H3 + first paragraph + BAND "AURX will be offered only after VARA grants the licence and approves this whitepaper. Credit and the Gold Card start once the CBUAE-licensed partners are in place."; FIG 55% WP-25 (Fig 25); 16.3 H3 + lead. | ~90% | v1's sidebar-callout page is gone. The licence gate becomes a band in the flow, and the path ladder is centred under it. |
| 35 | cont. | §16.3-16.4, §17 | TBL positions (6 rows) + "If a reading changes..." paragraph; 16.4 H3 + 3 bullets; H2 "17. Risks"; TBL risks (10 x 3, full width). | ~95% | The risk table closes the body with visual weight (closing strength). |
| 36 | special-appendix (one column) | Glossary, References, Important notice | H2 "Glossary" + 17 entries as a run-in list, one per line ("**AANI.** The UAE's instant payment system..."), 9pt; H2 "References" + 5 numbered sources, 8.5pt; H2 "Important notice" + 5 paragraphs, 9pt, full text unchanged. | ~92% **TIGHT** | End matter on one page. `column-count: 1` override (the user rejected v1's two-column glossary). If it overflows, the notice continues on one more page (contingency C5). |
| 37 | closing-back-cover | — | Tagline, legal line | — | Always the final page. |

---

## 7. Page Budget, Contingencies and Ceiling

### Budget

| Block | Pages |
|---|---|
| Cover, contents, back cover | 3 |
| Six part dividers | 6 |
| Part 1 (§1 page + flow §2-4) | 4 |
| Part 2 (§5-6) | 5 |
| Part 3 (§7-8) | 5 |
| Part 4 (§9-10) | 4 |
| Part 5 (§11-13) | 5 |
| Part 6 (§14 page + flow §15-17) | 4 |
| Back matter | 1 |
| **Planned total** | **37** |

Single column costs about 3 pages compared with v1 (34). The eight diagrams that sat beside text now take their own rows, and the stacked rule lists and the one-column glossary add height.

### Contingencies (each adds at most 1 page; worst case 40)

| ID | Trigger | Result |
|---|---|---|
| C1 | P13 (§6) overflows | 6.2 moves to a continuation page. Part 2 becomes 6 pages. |
| C2 | Part 3 break points land badly around WP-08 / WP-09 | Part 3 becomes 6 pages. |
| C3 | P33 (§15) or P35 overflows | Part 6 becomes 5 pages. |
| C4 | Part 5 P30 grows past one page | Should not happen (about 3 in of content). Merge into P29 if possible. |
| C5 | Appendix overflows | The notice continues onto a second appendix page. |

If C1, C2, C3 and C5 all trigger, the total is 41. To stay at or under **40**, apply these reductions in order until the count fits. None of them breaks the single-column rule or the 9pt diagram floor:

1. Tighten Mermaid spacing on the ladders and TD flows only (WP-19, WP-21, WP-22, WP-08, WP-24, WP-12, WP-25, WP-09): `rankSpacing: 24, nodeSpacing: 22`. Text size stays the same and each is about 0.4 in shorter.
2. Sequence diagrams (WP-20, WP-04, WP-06, WP-13, WP-15): `messageMargin: 24, height: 40`.
3. Body text 9.5pt, line-height 1.4 (tables stay at 9pt).
4. Back matter: glossary and notice at 8.5pt so they fit on one page.

Never: put two elements side by side, drop a part divider, cut copy, or render diagram text below 9pt.

---

## 8. Template Usage Summary

| Template ID | Planned pages | % of 37 |
|---|---|---|
| content-single-column (flow starts + continuations) | 25 | 68% |
| section-typographic | 6 | 16% |
| content-data-table (flow 6b start, continuations counted above) | 1 | 3% |
| special-executive-summary | 1 | 3% |
| special-appendix (one column) | 1 | 3% |
| special-table-of-contents | 1 | 3% |
| cover-minimal-typographic | 1 | 3% |
| closing-back-cover | 1 | 3% |
| **Total** | **37** (P34-35 continue the data-table flow; counted as single-column) | |

**Distinct content templates used:** 4 (executive-summary, single-column, data-table, appendix). Process-steps styling is also used as an in-flow block for 14.3.
**Variety score:** Good (4). The single-column rule and Stockpile's content-only approach make most of the document flow pages, by design. Variety inside those pages comes from 25 inline figures, 9 bands, 4 worked-example boxes and 2 stat rows.

**Allowed but not used as page templates, with reason:**
- `content-process-steps`: the only real step sequence (5.2) exists only as WP-19, so a steps page would repeat the diagram. Its style is reused for the 14.3 layers in the flow.
- `content-timeline-phases`: no section has dated phases. The path to launch (16.2) has no dates, and the tier months (7.4) are a table that WP-08 already shows.
- `content-data-table` for §8 and §17: §8's stats would have to be worked out from the table rather than taken from the copy, and §17 has no headline stats. Both tables still run full width inline.

---

## 9. What happened to each v1 two-column element

| v1 element (page) | v2 handling |
|---|---|
| §1 findings as a 2x3 card grid (P4) | Stacked numbered findings list, the executive-summary template's native one-column layout |
| §4 eligibility table beside the NRI/KYC text (P6) | Full-width table, paragraphs below it |
| WP-19 beside the 5.2 text (P8) | Centred at 55%, sentence below |
| WP-21 beside the Travel Rule text (P11) | Centred at 55%, sentences below |
| §6: 6.1 and 6.2 side by side (P12) | Stacked; the three fact bullets become a stat row |
| §7 pull-quote page with before/after blocks (P14) | Template dropped; 7.1 runs as plain prose and the thesis sentence stays in its paragraph |
| WP-22 beside the four score rules (P15) | Centred at 60%, rules below |
| WP-08 beside the thresholds sentence (P15) | Sentence, then WP-08 centred at 60% |
| WP-09 beside the Mark example (P16) | Mark example, band, then WP-09 centred at 70% |
| §8: 8.2 and 8.3 side by side (P17) | Stacked; §8 is inline and the data-table page is dropped |
| §9.2 formula-display page (P20) | Formula line as a full-width band in the flow |
| WP-24 beside the upgrade rules (P20) | Centred at 60%, upgrade paragraph below |
| 9.4 table beside the "13% fall" callout (P21) | Table full width, then the sentence as a full-width band |
| §10 rate table beside the Emma example card (P22) | Table, then the full-width example box |
| 11.3 does / does-not as two text columns (P25) | The copy's own full-width table |
| 11.4 price bullets beside the Emma card (P25) | Bullets, then the full-width example box |
| 12.2 and 12.3 side by side (P26) | Stacked |
| WP-16 beside the 13.2 bullets (P27) | Centred at 80%, bullets below |
| §16 sidebar-callout page with WP-25 in the sidebar (P31) | Single-column flow; licence gate as a band; WP-25 centred at 55% under it |
| Glossary as a two-column definition list (P33) | One-column run-in list (`column-count: 1` override on special-appendix) |

---

## 10. Copy-block checklist (each used once)

- Title block (title, subtitle, token, issuer, status): cover.
- Contents list: TOC page.
- §1-§17 body blocks: pages 4-35 as mapped above. The §6 fact bullets appear only as the stat row. Band blocks are moved paragraphs and are not repeated in the body. The §1 and §15 stat values are short labels taken from the copy; the full sentences and table cells still appear once in the body.
- Glossary, References, Important notice: P36.
- Diagram placeholder lines and briefs: removed and replaced by Figures 1-25 (designer notes, not reader copy).
