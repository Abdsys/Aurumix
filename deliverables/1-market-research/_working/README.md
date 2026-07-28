# Working files, not deliverables

Nothing in this folder is a deliverable. It is the build input and provenance trail for `../Aurumix_Protocol_Landscape.md`.

⚠ **Do not point any summarising or document-generation skill at this folder.** Every file here is either a duplicate of content already inside the assembled landscape document, or an instruction file. A skill that scans a directory for `*.md` and ingests everything it finds will triple-count the same protocols. That is why these files were moved out of `deliverables/1-market-research/` on 2026-07-28.

**The two authoritative Phase 1 deliverables are:**

- `../Aurumix_Market_Research.md`
- `../Aurumix_Protocol_Landscape.md`

## What is in here

| File | What it is |
|---|---|
| `_frontmatter.md` | The synthesis section of the landscape document: title, how-to-read conventions, the corrections register, the nine cross-cutting findings, the comparison tables, and the sourcing note. **Written by hand, then concatenated onto the front of the assembled document.** |
| `sections/*.md` | One protocol profile per file, 18 of them. Each was produced by a dedicated research agent working from `_landscape_brief.md`. The nineteenth profile (PGOLD) came from the pilot. |
| `_landscape_brief.md` | The instruction file every research agent read: tooling rules, research method, required 13-section structure, house style, client context, and the Part 4 addendum carrying wave 1's findings into wave 2. **Re-read this before re-running any protocol**, so a new profile matches the others. |
| `Aurumix_Protocol_Landscape_PILOT.md` | The approved format sample (PGOLD). Superseded: its profile body is now inside the assembled document. Kept because it is the artifact the client signed off on the format against. |

## ⚠ Divergence warning

`Aurumix_Protocol_Landscape.md` is a **generated** file, but it is now the **authoritative** one. Edits made to the assembled document do **not** flow back here, and re-running the assembly below would **overwrite those edits**.

So:

- **Small corrections:** edit `../Aurumix_Protocol_Landscape.md` directly and do not re-assemble.
- **Re-running a protocol from scratch:** update the file in `sections/`, then re-assemble, then re-apply any hand edits that were made to the assembled document since.

## Assembly

Run from `deliverables/1-market-research/`. Order of `live` is by AUM descending; `None` is the slot where the PGOLD profile is spliced in from the pilot.

```python
import io, os, re
base = os.getcwd(); sec = os.path.join(base, "_working", "sections")
rd = lambda p: io.open(p, encoding="utf-8").read().strip()

pilot = io.open(os.path.join(base, "_working", "Aurumix_Protocol_Landscape_PILOT.md"),
                encoding="utf-8").read().split("\n")
pgold = "\n".join(pilot[19:]).strip()          # profile body only, drops the pilot preamble

live = ["xaut","paxg","kinesis",None,"azg","xaum","libeara","streamex","dgld","aurus",
        "vnxau","midas","comtech","oro","wtgold","tenbin"]
fail = ["pmgt","digix","cachegold"]

out = [rd(os.path.join(base, "_working", "_frontmatter.md"))]
for n in live:
    out.append(pgold if n is None else rd(os.path.join(sec, n + ".md")))
out.append("---\n\n# Part 2: Failed and wound-down protocols\n\n"
           "Three protocols that stopped operating. All three are profiled against the same "
           "thirteen headings, with section 11 as a dated wind-down timeline and section 12 "
           "drawing the lesson.")
for n in fail:
    out.append(rd(os.path.join(sec, n + ".md")))

doc = "\n\n---\n\n".join(out) + "\n"
doc = re.sub(r"\|\s*—\s*\|", "| n/a |", doc)   # lone em dash used as an empty table cell
doc = re.sub(r"\*\*\s+—\s+", "** ", doc)
doc = doc.replace("** — ", "**: ").replace("—", ": ")   # house style: no em dashes

io.open(os.path.join(base, "Aurumix_Protocol_Landscape.md"), "w",
        encoding="utf-8", newline="\n").write(doc)
```

Post-assembly checks that should all return zero: em dashes, HTML tags, and bare `[n]` citation markers not followed by a URL.
