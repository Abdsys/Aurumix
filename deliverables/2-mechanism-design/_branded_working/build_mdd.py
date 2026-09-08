#!/usr/bin/env python3
"""Build the branded HTML for the Aurumix Mechanism Design Document.

Reuses the proven Stockpile v5 shell (template CSS, mermaid init, auto-continue,
TOC population) and generates the Aurumix pages from:
  final/Aurumix_Mechanism_Design_Document.md   (content)
  final/Aurumix_Process_Maps.md                (diagrams, keyed 2a, 3a, ...)

Output: _branded_working/Aurumix_Mechanism_Design_Branded.html
"""
import base64, html, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHASE = os.path.dirname(HERE)
FINAL = os.path.join(PHASE, "final")
DOC = os.path.join(FINAL, "Aurumix_Mechanism_Design_Document.md")
MAPS = os.path.join(FINAL, "Aurumix_Process_Maps.md")
OUT = os.path.join(HERE, "Aurumix_Mechanism_Design_Branded.html")

SHELL = r"C:\Users\pc\OneDrive - Institute of Business Administration\Desktop\Stockpile\deliverables\2-mechanism-design\final\Stockpile_Mechanism_Design_Branded_v5.html"
BRAND = r"C:\Users\pc\.claude\plugins\marketplaces\tokenomics-net\tokenomics-plugin\standards\branded-docs-main"

TABLE_CHUNK = 8   # atomic for the splitter; dense rows wrap 3-4 lines, so keep chunks well under a page

# ---------------------------------------------------------------- shell
def load_shell():
    t = io.open(SHELL, encoding="utf-8").read()
    top_end = t.find('<main id="document-pages">')
    assert top_end > 0
    top = t[:top_end + len('<main id="document-pages">')]
    bot_start = t.find('<!-- Mermaid -->')
    assert bot_start > 0
    bottom = "\n  </main>\n\n  " + t[bot_start:]
    # patch title
    top = top.replace(
        "<title>Stockpile: Mechanism Design Document — Tokenomics.net</title>",
        "<title>Aurumix: Mechanism Design Document - Tokenomics.net</title>")
    # inline the brand css instead of the relative link
    css = io.open(os.path.join(BRAND, "css", "brand-system.css"), encoding="utf-8").read()
    link = '<link rel="stylesheet" href="../../../company container/standards/branded-docs-main/css/brand-system.css">'
    top = top.replace(link, "<style>\n" + css + "\n</style>")
    # extra styles for markdown blocks
    extra = """
  <style>
    .content-area pre { font-family: 'Courier New', monospace; font-size: 9pt; line-height: 1.5;
      background: #F4F1EC; padding: 10px 14px; border-left: 3px solid var(--gold);
      white-space: pre-wrap; margin: 12px 0; }
    .content-area blockquote { border-left: 3px solid var(--gold); background: #FAF8F5;
      padding: 10px 16px; margin: 12px 0; font-size: 10pt; color: var(--warm-charcoal); }
    .content-area blockquote p { margin: 4px 0; }
    figure .mermaid { min-height: 200px; }
  </style>
"""
    top = top.replace("</head>", extra + "</head>")
    # completion attribute for the pdf renderer
    hook = ("<script>document.addEventListener('auto-continue-complete',function(){"
            "document.body.setAttribute('data-render-complete','1');});</script>\n</body>")
    bottom = bottom.replace("</body>", hook)
    # progress guard: a first child taller than the page with siblings after it must
    # not recurse forever; keep the tall child alone and split from the second child
    old_guard = "if(si===0&&nd<=1){page.setAttribute('data-auto-continued','');return[page];}"
    assert old_guard in bottom
    bottom = bottom.replace(old_guard, old_guard + "\n      if(si===0){si=1;}")
    return top, bottom

def logo_data(name):
    p = os.path.join(BRAND, "assets", name)
    b = open(p, "rb").read()
    return "data:image/svg+xml;base64," + base64.b64encode(b).decode()

# ---------------------------------------------------------------- markdown
def esc(t):
    return html.escape(t, quote=False)

def slug(t):
    t = re.sub(r"[^\w\s-]", "", t.lower())
    return "toc-" + re.sub(r"[\s]+", "-", t.strip())[:70]

def inline(text):
    ph = {}
    def stash(s):
        k = "\x00%d\x00" % len(ph); ph[k] = s; return k
    text = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % esc(m.group(1))), text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda m: stash('<a href="%s">%s</a>' % (esc(m.group(2)), esc(m.group(1)))), text)
    text = esc(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    for k, v in ph.items():
        text = text.replace(k, v)
    return text

def split_row(line):
    line = line.strip().strip("|")
    return [c.strip() for c in line.split("|")]

def table_html(rows):
    """rows: list of cell lists; first is header. Chunk long tables."""
    head, body = rows[0], rows[1:]
    out = []
    for i in range(0, max(1, len(body)), TABLE_CHUNK):
        chunk = body[i:i + TABLE_CHUNK]
        h = "<table>\n<thead><tr>" + "".join("<th>%s</th>" % inline(c) for c in head) + "</tr></thead>\n<tbody>\n"
        for r in chunk:
            h += "<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>\n"
        h += "</tbody>\n</table>"
        out.append(h)
    return out

def md_blocks(lines):
    """Convert markdown lines to a list of (kind, html, heading_text) blocks.
    kind: h3, h4, p, table, ul, pre, quote, hr"""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1; continue
        if s.startswith("### "):
            txt = s[4:].strip()
            blocks.append(("h3", '<h3 id="%s">%s</h3>' % (slug(txt), inline(txt)), txt)); i += 1
        elif s.startswith("#### "):
            txt = s[5:].strip()
            blocks.append(("h4", '<h4 id="%s">%s</h4>' % (slug(txt), inline(txt)), txt)); i += 1
        elif s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                r = split_row(lines[i])
                if not all(re.fullmatch(r"[-: ]*", c) for c in r):
                    rows.append(r)
                i += 1
            for t in table_html(rows):
                blocks.append(("table", t, None))
        elif s.startswith("```"):
            i += 1; buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            blocks.append(("pre", "<pre>%s</pre>" % esc("\n".join(buf)), None))
        elif s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            paras = [p for p in "\n".join(buf).split("\n\n")]
            inner = "".join("<p>%s</p>" % inline(p.replace("\n", " ")) for p in paras if p.strip())
            blocks.append(("quote", "<blockquote>%s</blockquote>" % inner, None))
        elif s.startswith("- ") or s.startswith("* "):
            items = []
            while i < n and (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")):
                item = lines[i].strip()[2:]
                # absorb continuation lines
                j = i + 1
                while j < n and lines[j].strip() and not re.match(r"^(\-|\*|\||#|>|```)", lines[j].strip()):
                    item += " " + lines[j].strip(); j += 1
                items.append(item); i = j
            blocks.append(("ul", "<ul>" + "".join("<li>%s</li>" % inline(it) for it in items) + "</ul>", None))
        elif re.match(r"^\d+\.\s", s):
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                j = i + 1
                while j < n and lines[j].strip() and not re.match(r"^(\d+\.\s|\-|\*|\||#|>|```)", lines[j].strip()):
                    item += " " + lines[j].strip(); j += 1
                items.append(item); i = j
            blocks.append(("ol", "<ol>" + "".join("<li>%s</li>" % inline(it) for it in items) + "</ol>", None))
        elif s == "---":
            i += 1  # drop rules; pages provide structure
        else:
            buf = [s]; j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^(\-|\*|\||#|>|```|\d+\.\s)", lines[j].strip()) and lines[j].strip() != "---":
                buf.append(lines[j].strip()); j += 1
            blocks.append(("p", "<p>%s</p>" % inline(" ".join(buf)), None)); i = j
    return blocks

# ---------------------------------------------------------------- maps
def load_maps():
    t = io.open(MAPS, encoding="utf-8").read()
    diagrams = {}
    for m in re.finditer(r"^## (\w+)\. (.+?)$\n\n(.+?)\n\n```mermaid\n(.*?)\n```", t, re.M | re.S):
        did, title, desc, code = m.groups()
        diagrams[did] = (title.strip(), desc.strip(), code)
    return diagrams

FIGNUM = {"n": 0}
def figure_html(did, diagrams):
    title, desc, code = diagrams[did]
    FIGNUM["n"] += 1
    return ('<figure style="margin: 16px 0;"><div class="mermaid">\n%s\n</div>'
            '<figcaption style="font-family: var(--font-sans); font-size: 9pt; color: var(--concrete); '
            'margin-top: 8px; text-align: center;">Figure %d: %s</figcaption></figure>'
            % (code, FIGNUM["n"], esc(title)))

# where each diagram lands: after the block-run of the heading whose text starts with this prefix
PLACEMENT = [
    ("2a", "2.2"), ("2b", "2.4"),
    ("3a", "3.2"), ("3c", "3.4"), ("3b", "3.5.1"), ("3d", "3.5.2"),
    ("4b", "4.1"), ("4a", "4.2"), ("4c", "4.4"),
    ("5a", "5.1"), ("5b", "5.3"), ("5d", "5.5"), ("5c", "5.7"),
    ("6a", "6.1"), ("6b", "6.2"), ("6c", "6.6"),
    ("7a", "7.2"), ("7b", "7.3"), ("7c", "7.4"),
    ("8a", "8.2"), ("8c", "8.4"), ("8d", "8.4"), ("8e", "8.5"), ("8f", "8.6"),
    ("9a", "9.1"), ("9b", "9.2"),
    ("10a", "10.1"), ("10b", "10.3"), ("10c", "10.4"), ("10d", "10.4"),
    ("11a", "11.1"), ("11b", "11.4"), ("11c", "11.4"), ("11d", "11.5"), ("11e", "11.6"),
    ("12a", "12.2"), ("12b", "12.4"),
    ("13a", "13.4"), ("13b", "13.5"),
    ("15a", "15.3"),
]

def insert_figures(blocks, secnum, diagrams):
    """Insert mapped figures after the content run of their heading."""
    placements = [(d, h) for d, h in PLACEMENT if h.split(".")[0] == str(secnum)]
    for did, hpref in placements:
        # find heading block
        hi = None
        for i, (k, _, txt) in enumerate(blocks):
            if k in ("h3", "h4") and txt and txt.startswith(hpref + " "):
                hi = i; break
        if hi is None:
            print("  WARN: no heading %s for diagram %s" % (hpref, did)); continue
        # find end of this heading's run (next heading of same or higher level)
        lvl = blocks[hi][0]
        j = hi + 1
        while j < len(blocks):
            k = blocks[j][0]
            if k == "h3" or (k == "h4" and lvl == "h4"):
                break
            j += 1
        blocks.insert(j, ("fig", figure_html(did, diagrams), None))
    return blocks

# ---------------------------------------------------------------- doc parsing
def parse_doc():
    t = io.open(DOC, encoding="utf-8").read()
    lines = t.splitlines()
    # front matter: up to '## 1. Introduction'
    first = next(i for i, l in enumerate(lines) if re.match(r"^## 1\. Introduction", l))
    front = lines[:first]
    # sections: '## N. Title' and '## Appendix X' / '## References' / '## Document control'
    secs = []
    cur = None
    for l in lines[first:]:
        m = re.match(r"^## (.+)$", l)
        if m:
            if cur: secs.append(cur)
            cur = {"title": m.group(1).strip(), "lines": []}
        else:
            if cur is not None:
                cur["lines"].append(l)
    if cur: secs.append(cur)
    return front, secs

def get_sec(secs, prefix):
    for s in secs:
        if s["title"].startswith(prefix):
            return s
    raise KeyError(prefix)

# ---------------------------------------------------------------- page emitters
def page_cover():
    return """
    <div class="page page--cover-minimal-typographic" data-template="cover-minimal-typographic">
      <div class="cover-gold-bar"></div>
      <div class="cover-content">
        <div class="cover-eyebrow text-eyebrow" data-text-role="eyebrow">Mechanism Design</div>
        <h1 class="cover-title" data-text-role="title">Aurumix: Mechanism Design Document</h1>
        <p class="cover-subtitle" data-text-role="subtitle">Gold-backed savings infrastructure under VARA</p>
        <hr class="cover-rule">
      </div>
      <div class="cover-bottom">
        <div class="cover-meta">
          <img src="%s" alt="Tokenomics.net" class="logo logo--cover">
          <span>September 2026</span>
        </div>
      </div>
    </div>""" % logo_data("tokenomics-logo-dark.svg")

def page_toc(entries):
    rows = []
    for kind, txt, ref in entries:
        cls = "toc-entry--section" if kind == "sec" else "toc-entry--sub"
        rows.append('<div class="toc-entry %s" data-toc-ref="%s"><span class="toc-entry-text">%s</span>'
                    '<span class="toc-entry-dots"></span><span class="toc-entry-page">.</span></div>'
                    % (cls, ref, inline(txt)))
    return """
    <div class="page page--special-table-of-contents" data-template="special-table-of-contents" data-auto-continue>
      <div class="content-area">
        <h1 class="toc-title" data-text-role="title">Contents</h1>
        <hr class="toc-rule">
        <div class="toc-list" data-text-role="toc-entries">
          %s
        </div>
      </div>
    </div>""" % "\n          ".join(rows)

def page_divider(num, title, tid=None):
    idattr = ' id="%s"' % tid if tid else ""
    return """
    <div class="page page--section-typographic" data-template="section-typographic">
      <div class="section-content">
        <div class="section-number" data-text-role="section-number">%s</div>
        <h2%s class="section-title" data-text-role="section-title">%s</h2>
        <hr class="section-rule">
      </div>
      <div class="page-number" data-text-role="page-number"></div>
    </div>""" % (num, idattr, inline(title))

def content_page(template, heading_id, heading_text, inner_html):
    return """
    <div class="page page--%s" data-template="%s" data-auto-continue>
      <div class="content-area">
        <h2 id="%s" class="content-heading" data-text-role="section-title">%s</h2>
        <hr class="heading-rule">
        %s
      </div>
      <div class="page-number" data-text-role="page-number"></div>
    </div>""" % (template, template, heading_id, inline(heading_text), inner_html)

def page_appendix(title, subtitle, inner_html, tid):
    return """
    <div class="page page--special-appendix" data-template="special-appendix" data-auto-continue>
      <div class="appendix-header">
        <h2 id="%s" class="appendix-title" data-text-role="title">%s</h2>
        <p class="appendix-subtitle" data-text-role="subtitle">%s</p>
      </div>
      <div class="content-area">
        <div class="appendix-body" data-text-role="body">
          %s
        </div>
      </div>
      <div class="page-number" data-text-role="page-number"></div>
    </div>""" % (tid, inline(title), inline(subtitle), inner_html)

def page_back():
    return """
    <div class="page page--closing-back-cover" data-template="closing-back-cover">
      <div class="back-center">
        <img src="%s" alt="Tokenomics.net" class="logo logo--2xl">
        <p class="back-tagline" data-text-role="tagline">Built by founders. Designed for founders.</p>
      </div>
      <div class="back-legal" data-text-role="legal-line">Prepared by Tokenomics.net. &copy; 2026</div>
    </div>""" % logo_data("tokenomics-logo-light.svg")

# ---------------------------------------------------------------- build
def blocks_html(blocks):
    return "\n".join(b[1] for b in blocks)

def main():
    top, bottom = load_shell()
    diagrams = load_maps()
    front, secs = parse_doc()

    pages = []
    toc_entries = []

    pages.append(page_cover())

    # --- preface from front matter ('How to read this document')
    hi = next(i for i, l in enumerate(front) if l.startswith("## How to read"))
    # take until '## Table of contents'
    ti = next(i for i, l in enumerate(front) if l.startswith("## Table of contents"))
    pre_blocks = md_blocks(front[hi + 1:ti])
    preface_html = blocks_html(pre_blocks)
    # metadata block (Prepared by / date / version / status) before 'How to read'
    meta_lines = [l for l in front[:hi] if l.strip().startswith("**")]
    meta_html = "".join("<p>%s</p>" % inline(l.strip()) for l in meta_lines)

    toc_placeholder = None  # built after sections known

    numbered = [s for s in secs if re.match(r"^\d+\.", s["title"])]
    appendices = [s for s in secs if s["title"].startswith("Appendix")]
    refs = get_sec(secs, "References")
    docctl = get_sec(secs, "Document control")

    # TOC entries
    toc_entries.append(("sub", "How to read this document", "toc-how-to-read-this-document"))
    for s in numbered:
        sid = slug(s["title"])
        s["id"] = sid
        toc_entries.append(("sec", s["title"], sid))
        for l in s["lines"]:
            m = re.match(r"^### (.+)$", l)
            if m:
                toc_entries.append(("sub", m.group(1).strip(), slug(m.group(1).strip())))
    for s in appendices:
        sid = slug(s["title"]); s["id"] = sid
        toc_entries.append(("sec", s["title"], sid))
    toc_entries.append(("sec", "References", slug("References")))
    toc_entries.append(("sec", "Document control", slug("Document control")))

    pages.append(page_toc(toc_entries))

    pages.append(content_page("content-single-column", "toc-how-to-read-this-document",
                              "How to read this document", meta_html + preface_html))

    for s in numbered:
        num = int(s["title"].split(".")[0])
        title_wo = s["title"].split(". ", 1)[1]
        pages.append(page_divider("%02d" % num, title_wo))
        blocks = md_blocks(s["lines"])
        blocks = insert_figures(blocks, num, diagrams)

        if num == 1:
            # pull-quote page
            quote = ("Not one of nineteen protocols has a savings plan, a recurring "
                     "purchase, or a retail referral programme.")
            # split at heading 1.4
            k = next(i for i, b in enumerate(blocks) if b[0] == "h3" and b[2].startswith("1.4"))
            before, after = blocks[:k], blocks[k:]
            inner = ('<div data-text-role="body-before">\n%s\n</div>\n'
                     '<div class="pull-quote"><div class="pull-quote-text" data-text-role="pull-quote">%s</div></div>\n'
                     '<div data-text-role="body-after">\n%s\n</div>'
                     % (blocks_html(before), esc(quote), blocks_html(after)))
            pages.append(content_page("content-pull-quote", s["id"], s["title"], inner))
        elif num == 8:
            # split: 8.1-8.2 single | 8.3 formula | 8.4+ single
            k3 = next(i for i, b in enumerate(blocks) if b[0] == "h3" and b[2].startswith("8.3"))
            k4 = next(i for i, b in enumerate(blocks) if b[0] == "h3" and b[2].startswith("8.4"))
            part1, part2, part3 = blocks[:k3], blocks[k3:k4], blocks[k4:]
            pages.append(content_page("content-single-column", s["id"], s["title"], blocks_html(part1)))
            # formula page: drop the first pre block of 8.3 (replaced by KaTeX)
            f_blocks = [b for b in part2[1:]]
            for i, b in enumerate(f_blocks):
                if b[0] == "pre":
                    f_blocks.pop(i); break
            f_blocks.append(("fig", figure_html("8b", diagrams), None))
            formula_inner = """
        <div class="formula-label">The score</div>
        <div class="formula-display-block" data-text-role="formula">
          \\[ICS = \\min(Record,\\ Standing) \\times Retention\\]
        </div>
        <div class="notation-section">
          <div class="notation-section-label">Notation reference</div>
          <table class="notation-table">
            <thead><tr><th>Term</th><th>Reads</th><th>Meaning</th></tr></thead>
            <tbody>
              <tr><td class="notation-symbol">Record</td><td>Months paid</td><td>Contribution history since the qualifying run, mapped 0 to 100; five years is a complete record</td></tr>
              <tr><td class="notation-symbol">Standing</td><td>Trailing 12 months</td><td>Counted periods in the last twelve calendar months, mapped 0 to 100</td></tr>
              <tr><td class="notation-symbol">Retention</td><td>Kept gold</td><td>1.0 up to a 30 percent annual withdrawal allowance, falling linearly to 0 at full liquidation</td></tr>
            </tbody>
          </table>
        </div>
        <div class="body-text" data-text-role="body">
          %s
        </div>""" % blocks_html(f_blocks)
            fpage = """
    <div class="page page--content-formula-display" data-template="content-formula-display" data-auto-continue>
      <div class="content-area">
        <h2 id="%s" class="content-heading" data-text-role="section-title">8.3 The formula</h2>
        <hr class="heading-rule">%s
      </div>
      <div class="page-number" data-text-role="page-number"></div>
    </div>""" % (slug("8.3 The formula"), formula_inner)
            pages.append(fpage)
            pages.append(content_page("content-single-column", slug("8.4 The tiers"),
                                      "8. The Investor Conviction Score (continued)", blocks_html(part3)))
        elif num == 9:
            # data-table page: 9.1 prose, stats row, matrix table, then the rest
            # matrix table is the first table block in section 9
            ti_ = next(i for i, b in enumerate(blocks) if b[0] == "table")
            before, matrix, after = blocks[:ti_], blocks[ti_], blocks[ti_ + 1:]
            stats = """
        <div class="stats-row">
          <div class="stat-card"><div class="stat-value" data-text-role="stat-1-value">1.5pp</div>
            <div class="stat-label" data-text-role="stat-1-label">Top-tier fee discount</div></div>
          <div class="stat-card"><div class="stat-value" data-text-role="stat-2-value">80%</div>
            <div class="stat-label" data-text-role="stat-2-label">Sovereign credit LTV</div></div>
          <div class="stat-card"><div class="stat-value" data-text-role="stat-3-value">0.75%</div>
            <div class="stat-label" data-text-role="stat-3-label">Top Gold Rewards rate</div></div>
        </div>"""
            inner = ('<div data-text-role="body">\n%s\n</div>\n%s\n%s\n<div data-text-role="body-after">\n%s\n</div>'
                     % (blocks_html(before), stats, matrix[1], blocks_html(after)))
            pages.append(content_page("content-data-table", s["id"], s["title"], inner))
        else:
            pages.append(content_page("content-single-column", s["id"], s["title"], blocks_html(blocks)))

    # appendices
    pages.append(page_divider("A", "Appendices"))
    subtitles = {
        "Appendix A": "Terms used in this document",
    }
    for s in appendices:
        key = s["title"].split(":")[0]
        blocks = md_blocks(s["lines"])
        pages.append(page_appendix(s["title"], subtitles.get(key, ""), blocks_html(blocks), s["id"]))
    pages.append(page_appendix("References", "Primary sources verified during the design",
                               blocks_html(md_blocks(refs["lines"])), slug("References")))
    pages.append(page_appendix("Document control", "",
                               blocks_html(md_blocks(docctl["lines"])), slug("Document control")))

    pages.append(page_back())

    io.open(OUT, "w", encoding="utf-8", newline="\n").write(top + "\n".join(pages) + bottom)
    print("written:", OUT)
    print("planned pages:", len(pages))
    print("figures placed:", FIGNUM["n"])

if __name__ == "__main__":
    main()
