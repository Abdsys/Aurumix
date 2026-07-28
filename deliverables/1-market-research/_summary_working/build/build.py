#!/usr/bin/env python3
"""
Build the branded Aurumix Market Research Summary HTML from markdown.

Produces a fully self-contained HTML file (CSS inlined, logos inlined as data
URIs) so the deliverable is portable and renders identically anywhere.

Page sequence:
  cover -> table of contents (unnumbered) -> executive summary (page 1)
  -> sections 1..12 (divider + content) -> appendices -> closing CTA -> back cover

Page numbering starts after the table of contents. Cover, TOC, CTA and back
cover carry no .page-number element, and the runtime renumber() only counts
pages that have one.
"""

import base64
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORKING = os.path.dirname(HERE)
BRAND = r"C:\Users\BlockApex\.claude\plugins\marketplaces\tokenomics-net\tokenomics-plugin\standards\branded-docs-main"

MD_PATH = os.path.join(WORKING, "Aurumix_Market_Research_Summary.md")
META_PATH = os.path.join(HERE, "doc_meta.json")
OUT_HTML = os.path.join(HERE, "Aurumix_Market_Research_Summary.html")


# ----------------------------------------------------------------------------
# inline markdown
# ----------------------------------------------------------------------------

def esc(t):
    return html.escape(t, quote=False)


def inline(text):
    """Convert inline markdown to HTML. Order matters: code first, then links."""
    placeholders = {}

    def stash(s):
        key = "\x00%d\x00" % len(placeholders)
        placeholders[key] = s
        return key

    # inline code
    text = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % esc(m.group(1))), text)
    # links
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: stash('<a href="%s">%s</a>' % (esc(m.group(2)), esc(m.group(1)))),
        text,
    )
    text = esc(text)
    # bold then italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


# ----------------------------------------------------------------------------
# block markdown -> list of html blocks
# ----------------------------------------------------------------------------

TABLE_CHUNK = 9  # max body rows per rendered <table>; tables are atomic for auto-continue

# Full-page section dividers look good but cost one near-empty page per section,
# which was 13 pages of 70. Off by default; the section title and its contents
# anchor move onto the section's first content page instead.
SECTION_DIVIDERS = False

# Starting every protocol on a fresh page reads well only when a profile fills
# roughly a page. These fill about 1.3, so each one stranded its closing callout
# on a sheet at ~31% fill. Letting profiles flow packs them and removes the
# widows; the ### heading and fact table still mark each protocol clearly.
PROFILE_PAGE_BREAKS = False

# Closing "What Happens Next" call-to-action page. Off: this is market research,
# and a booking prompt does not belong in it.
CLOSING_CTA = False


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render_table(header, rows):
    """Render a markdown table, chunked so no single <table> can exceed a page."""
    # The nine-field profile summary is a key/value block, not a real table.
    # "Field | Detail" carries no information, so drop the header row and chunk
    # small enough that the block can always split across a page boundary.
    if [h.strip().lower() for h in header] == ["field", "detail"]:
        out = []
        for i in range(0, len(rows), 5):
            body = "".join(
                "<tr><td>%s</td><td>%s</td></tr>" % (inline(r[0]), inline(r[1] if len(r) > 1 else ""))
                for r in rows[i:i + 5]
            )
            out.append('<table class="profile-facts"><tbody>%s</tbody></table>' % body)
        return out

    # Chunk into balanced groups rather than greedy fixed-size ones. Greedy
    # chunking turns 11 rows into 9 + 2, and that 2-row tail lands on a page of
    # its own at ~25% fill. Balanced chunking gives 6 + 5 and fills both pages.
    out = []
    if rows:
        n_chunks = max(1, -(-len(rows) // TABLE_CHUNK))
        size = -(-len(rows) // n_chunks)
        chunks = [rows[i:i + size] for i in range(0, len(rows), size)]
    else:
        chunks = [[]]
    for chunk in chunks:
        h = "".join("<th>%s</th>" % inline(c) for c in header)
        body = ""
        for r in chunk:
            cells = list(r) + [""] * (len(header) - len(r))
            body += "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in cells[:len(header)])
        out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (h, body))
    return out


def md_blocks(lines):
    """Parse a list of markdown lines into HTML block strings."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # headings
        m = re.match(r"^(#{3,5})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            anchor = ""
            am = re.match(r"^(\d+\.\d+)\s", title)
            if level == 3 and am:
                anchor = ' id="s-%s"' % am.group(1).replace(".", "-")
            blocks.append("<h%d%s>%s</h%d>" % (level, anchor, inline(title), level))
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|?\s*$", lines[i + 1].strip()):
            header = split_row(stripped)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            blocks.extend(render_table(header, rows))
            continue

        # blockquote -> callout
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            text = " ".join(x for x in buf if x)
            title = "Key Insight"
            tm = re.match(r"^\*\*(.+?)\*\*[:.]?\s*(.*)$", text)
            if tm:
                title, text = tm.group(1), tm.group(2)
            blocks.append(
                '<div class="callout"><div class="callout-title">%s</div>'
                '<div class="callout-body">%s</div></div>' % (inline(title), inline(text))
            )
            continue

        # unordered list
        if re.match(r"^[-*+]\s+", stripped):
            items = []
            while i < n:
                s = lines[i].strip()
                if re.match(r"^[-*+]\s+", s):
                    items.append(re.sub(r"^[-*+]\s+", "", s))
                    i += 1
                elif s and not re.match(r"^(#{1,6}\s|\||>|\d+\.\s)", s) and items:
                    items[-1] += " " + s   # lazy continuation
                    i += 1
                else:
                    break
            blocks.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        # ordered list
        if re.match(r"^\d+\.\s+", stripped):
            items = []
            start = re.match(r"^(\d+)\.", stripped).group(1)
            while i < n:
                s = lines[i].strip()
                if re.match(r"^\d+\.\s+", s):
                    items.append(re.sub(r"^\d+\.\s+", "", s))
                    i += 1
                elif s and not re.match(r"^(#{1,6}\s|\||>|[-*+]\s)", s) and items:
                    items[-1] += " " + s
                    i += 1
                else:
                    break
            attr = ' start="%s"' % start if start != "1" else ""
            blocks.append("<ol%s>%s</ol>" % (attr, "".join("<li>%s</li>" % inline(x) for x in items)))
            continue

        # horizontal rule -> ignored (page break signals are handled structurally)
        if re.match(r"^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$", stripped):
            i += 1
            continue

        # paragraph
        buf = [stripped]
        i += 1
        while i < n:
            s = lines[i].strip()
            if not s or re.match(r"^(#{1,6}\s|\||>|[-*+]\s|\d+\.\s)", s) or re.match(r"^(-\s*){3,}$", s):
                break
            buf.append(s)
            i += 1
        blocks.append("<p>%s</p>" % inline(" ".join(buf)))

    return blocks


# ----------------------------------------------------------------------------
# page builders
# ----------------------------------------------------------------------------

def page_cover(meta, logo_dark):
    return """<div class="page page--cover-minimal-typographic" data-template="cover-minimal-typographic">
  <div class="cover-gold-bar"></div>
  <div class="cover-content">
    <div class="cover-eyebrow text-eyebrow">%s</div>
    <h1 class="cover-title">%s</h1>
    <p class="cover-subtitle">%s</p>
    <hr class="cover-rule">
  </div>
  <div class="cover-bottom">
    <div class="cover-meta">
      <img src="%s" alt="Tokenomics.net" class="logo logo--cover">
      <span>%s</span>
    </div>
  </div>
</div>""" % (esc(meta["eyebrow"]), esc(meta["title"]), esc(meta["subtitle"]), logo_dark, esc(meta["date"]))


def page_toc(entries):
    rows = []
    for e in entries:
        cls = "toc-entry--section" if e["level"] == 1 else "toc-entry--sub"
        rows.append(
            '<div class="toc-entry %s" data-toc-ref="%s">'
            '<span class="toc-entry-text">%s</span>'
            '<span class="toc-entry-dots"></span>'
            # placeholder reserves the number's width so filling in the real
            # page number later cannot reflow the entry onto a second line
            '<span class="toc-entry-page">000</span></div>' % (cls, e["ref"], esc(e["text"]))
        )
    return """<div class="page page--special-table-of-contents" data-template="special-table-of-contents" data-auto-continue>
  <div class="content-area">
    <h1 class="toc-title">Contents</h1>
    <hr class="toc-rule">
    <div class="toc-list" data-text-role="toc-entries">%s</div>
  </div>
</div>""" % "".join(rows)


def page_exec_summary(ex):
    stats = "".join(
        '<div class="stat-card"><div class="stat-value">%s</div>'
        '<div class="stat-label">%s</div></div>' % (esc(s["value"]), esc(s["label"]))
        for s in ex["stats"]
    )
    findings = "".join(
        '<div class="finding"><div class="finding-number">%d</div>'
        '<div class="finding-content"><div class="finding-title">%s</div>'
        '<div class="finding-body">%s</div></div></div>' % (idx + 1, inline(f["title"]), inline(f["body"]))
        for idx, f in enumerate(ex["findings"])
    )
    intro = "".join('<p class="summary-intro">%s</p>' % inline(p) for p in ex["intro"])
    return """<div class="page page--special-executive-summary" data-template="special-executive-summary" data-auto-continue data-toc-id="sec-exec">
  <div class="content-area">
    <h1 class="summary-title">Executive Summary</h1>
    <hr class="summary-rule">
    %s
    <div class="stats-row">%s</div>
    %s
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (intro, stats, findings)


def page_divider(number, title, subtitle, toc_id):
    return """<div class="page page--section-typographic" data-template="section-typographic" data-toc-id="%s">
  <div class="section-content">
    <div class="section-number">%s</div>
    <h2 class="section-title">%s</h2>
    <hr class="section-rule">
    <p class="section-subtitle">%s</p>
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (toc_id, esc(number), esc(title), inline(subtitle))


def page_content(heading, body_html, toc_id=None):
    head = ""
    if heading:
        head = '<h2 class="content-heading">%s</h2>\n    <hr class="heading-rule">\n    ' % esc(heading)
    anchor = ' data-toc-id="%s"' % toc_id if toc_id else ""
    return """<div class="page page--content-single-column" data-template="content-single-column" data-auto-continue%s>
  <div class="content-area">
    %s<div data-text-role="body">%s</div>
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (anchor, head, body_html)


def page_appendix(title, subtitle, body_html, toc_id):
    return """<div class="page page--special-appendix" data-template="special-appendix" data-auto-continue data-toc-id="%s">
  <div class="appendix-header">
    <h2 class="appendix-title">%s</h2>
    <p class="appendix-subtitle">%s</p>
  </div>
  <div class="content-area">
    <div class="appendix-body" data-text-role="body">%s</div>
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (toc_id, esc(title), esc(subtitle), body_html)


def page_cta(meta, logo_dark):
    c = meta["cta"]
    return """<div class="page page--closing-cta-contact" data-template="closing-cta-contact">
  <div class="cta-wrapper">
    <h1 class="cta-title">%s</h1>
    <p class="cta-subtitle">%s</p>
    <div class="cta-button">%s</div>
    <div class="cta-divider"></div>
    <div class="cta-contact">
      <div>
        <div class="contact-label">Email</div>
        <div class="contact-value">%s</div>
      </div>
      <div>
        <div class="contact-label">Web</div>
        <div class="contact-value">%s</div>
      </div>
    </div>
  </div>
  <div class="cta-wordmark">
    <img src="%s" alt="Tokenomics.net" class="logo logo--cover">
  </div>
</div>""" % (esc(c["title"]), esc(c["subtitle"]), esc(c["button"]), esc(c["email"]), esc(c["web"]), logo_dark)


def page_back_cover(meta, logo_light):
    return """<div class="page page--closing-back-cover" data-template="closing-back-cover">
  <div class="back-center">
    <img src="%s" alt="Tokenomics.net" class="logo logo--2xl">
    <p class="back-tagline">%s</p>
  </div>
  <div class="back-legal">%s</div>
</div>""" % (logo_light, esc(meta["tagline"]), esc(meta["legal"]))


# ----------------------------------------------------------------------------
# template styles
# ----------------------------------------------------------------------------

def template_style(name):
    path = os.path.join(BRAND, "templates", "portrait", name + ".html")
    with open(path, encoding="utf-8") as f:
        src = f.read()
    m = re.search(r"<style>(.*?)</style>", src, re.S)
    css = m.group(1) if m else ""
    if name == "section-typographic":
        # This template ships an image-slot rule followed by a dangling
        # declaration block with no selector. We use no images, and the
        # dangling block is a CSS parse error, so cut from the image rule on.
        idx = css.find(".page--section-typographic .section-image")
        if idx != -1:
            css = css[:idx]
    return css


def data_uri_svg(path):
    with open(path, "rb") as f:
        return "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")


AUTO_CONTINUE = r"""
(function(){
  'use strict';
  var BUFFER=8;
  function isAtomic(el){
    if(!el||el.nodeType!==1)return false;
    var s=window.getComputedStyle(el);
    var bi=s.getPropertyValue('break-inside')||s.getPropertyValue('-webkit-break-inside');
    if(bi==='avoid')return true;
    var t=el.tagName.toLowerCase();
    if(t==='table'||t==='figure'||t==='blockquote')return true;
    if(el.classList.contains('callout')||el.classList.contains('pull-quote')||
       el.classList.contains('stat-row')||el.classList.contains('stats-row')||
       el.classList.contains('finding')||el.classList.contains('keep-together'))return true;
    return false;
  }
  function isWrapper(el){
    if(!el||el.nodeType!==1)return false;
    if(el.tagName.toLowerCase()!=='div')return false;
    if(el.hasAttribute('data-text-role')&&el.children.length>1)return true;
    return false;
  }
  function flattenWrappers(ca){
    var changed=true;
    while(changed){changed=false;
      var ch=Array.prototype.slice.call(ca.children);
      for(var i=0;i<ch.length;i++){
        if(isWrapper(ch[i])){
          var w=ch[i],p=w.parentNode,nx=w.nextSibling;
          var inner=Array.prototype.slice.call(w.children);
          for(var j=0;j<inner.length;j++)p.insertBefore(inner[j],nx);
          p.removeChild(w);changed=true;break;
        }
      }
    }
  }
  function makeCont(orig){
    var c=document.createElement('div');
    c.className=orig.className;
    c.setAttribute('data-template',orig.getAttribute('data-template')||'');
    c.setAttribute('data-auto-continue','');
    c.setAttribute('data-continuation','');
    var ca=document.createElement('div');
    ca.className='content-area';
    c.appendChild(ca);
    // Only carry a page-number slot if the source page had one. This is what
    // keeps the cover, TOC and closing pages out of the numbering sequence.
    if(orig.querySelector('.page-number')){
      var pn=document.createElement('div');
      pn.className='page-number';
      pn.setAttribute('data-text-role','page-number');
      c.appendChild(pn);
    }
    return c;
  }
  function getCA(p){return p.querySelector('.content-area');}
  function neutralizeLayout(ca){
    var cs=window.getComputedStyle(ca);
    if(cs.display==='flex'||cs.display==='inline-flex'||cs.overflow==='hidden'){
      ca.style.display='block';ca.style.flexDirection='';ca.style.overflow='visible';
    }
  }
  function process(page,depth){
    depth=depth||0;
    if(depth>200)return[page];
    var ca=getCA(page);
    if(!ca)return[page];
    flattenWrappers(ca);
    neutralizeLayout(ca);
    var uh=ca.clientHeight-BUFFER;
    if(ca.scrollHeight<=uh+BUFFER){page.setAttribute('data-auto-continued','');return[page];}
    var ch=[];for(var i=0;i<ca.children.length;i++)ch.push(ca.children[i]);
    var si=-1,ar=ca.getBoundingClientRect();
    for(var i=0;i<ch.length;i++){
      if(ch[i].classList.contains('page-number'))continue;
      if(ch[i].getBoundingClientRect().bottom-ar.top>uh){si=i;break;}
    }
    if(si===-1){page.setAttribute('data-auto-continued','');return[page];}
    var nd=0;
    for(var n=0;n<ch.length;n++){
      if(!ch[n].classList.contains('page-number')&&
         !ch[n].classList.contains('content-heading')&&
         ch[n].tagName.toLowerCase()!=='hr')nd++;
    }
    if(si===0&&nd<=1){page.setAttribute('data-auto-continued','');return[page];}
    // never leave a heading stranded as the last element on a page
    while(si>1){var pv=ch[si-1];if(!pv||pv.nodeType!==1)break;var pt=pv.tagName.toLowerCase();if(pt==='h3'||pt==='h4'||pt==='h5'){si--;}else{break;}}
    if(si<1)si=1;
    var cp=makeCont(page);
    page.parentNode.insertBefore(cp,page.nextSibling);
    var cca=getCA(cp),tm=[];
    for(var j=si;j<ch.length;j++){if(!ch[j].classList.contains('page-number'))tm.push(ch[j]);}
    for(var k=0;k<tm.length;k++)cca.appendChild(tm[k]);
    page.setAttribute('data-auto-continued','');
    return[page].concat(process(cp,depth+1));
  }
  function renumber(){
    // Only pages carrying a .page-number element are counted, so numbering
    // begins on the first page after the table of contents.
    var pp=document.querySelectorAll('#document-pages > .page');
    var c=0;
    for(var i=0;i<pp.length;i++){
      var n=pp[i].querySelector('.page-number');
      if(n){c++;n.textContent=String(c);}
    }
  }
  function populateTOC(){
    var ee=document.querySelectorAll('.toc-entry[data-toc-ref]');
    for(var i=0;i<ee.length;i++){
      var ref=ee[i].getAttribute('data-toc-ref');if(!ref)continue;
      var t=document.getElementById(ref);
      if(!t)t=document.querySelector('.page[data-toc-id="'+ref+'"]');
      if(!t)continue;
      var pg=t.closest?t.closest('#document-pages > .page'):null;
      if(!pg){var nd=t;while(nd&&nd!==document.body){if(nd.classList&&nd.classList.contains('page')&&nd.parentNode&&nd.parentNode.id==='document-pages'){pg=nd;break;}nd=nd.parentNode;}}
      if(!pg&&t.classList&&t.classList.contains('page'))pg=t;
      if(!pg)continue;
      var nm=pg.querySelector('.page-number');if(!nm)continue;
      var sp=ee[i].querySelector('.toc-entry-page');if(sp)sp.textContent=nm.textContent;
    }
  }
  function overflows(page){
    var ca=getCA(page);
    if(!ca)return false;
    var b=ca.getBoundingClientRect().bottom;
    var ch=ca.children;
    for(var i=0;i<ch.length;i++){
      if(ch[i].classList.contains('page-number'))continue;
      if(ch[i].getBoundingClientRect().bottom-b>1)return true;
    }
    return false;
  }
  function run(){
    var a=Array.prototype.slice.call(document.querySelectorAll('.page[data-auto-continue]'));
    for(var i=0;i<a.length;i++)process(a[i],0);
    renumber();
    populateTOC();
    // Writing page numbers into the contents entries changes their layout, and
    // adding contents pages changes the numbers. Settle both by re-splitting
    // anything that still overflows, then renumbering, until it converges.
    for(var pass=0;pass<4;pass++){
      var again=Array.prototype.slice.call(document.querySelectorAll('.page[data-auto-continue]'))
        .filter(overflows);
      if(again.length===0)break;
      for(var j=0;j<again.length;j++)process(again[j],0);
      renumber();
      populateTOC();
    }
    document.body.setAttribute('data-render-complete','1');
    document.dispatchEvent(new Event('auto-continue-complete'));
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){document.fonts.ready.then(run);});
  }else{document.fonts.ready.then(run);}
})();
"""


EXTRA_CSS = """
/* ---- document-specific hardening ---- */
#document-pages > .page { page-break-after: always; break-after: page; }
#document-pages > .page:last-child { page-break-after: avoid; break-after: avoid; }

/* uniform heading treatment across every content and appendix page */
.page--content-single-column .content-area h3,
.page--special-appendix .appendix-body h3 {
  font-family: var(--font-serif);
  font-size: 14pt;
  font-weight: 700;
  color: var(--warm-charcoal);
  line-height: 1.25;
  margin: 18px 0 8px;
  break-after: avoid;
}
.page--content-single-column .content-area h3:first-child { margin-top: 0; }
.page--content-single-column .content-area h4,
.page--special-appendix .appendix-body h4 {
  font-family: var(--font-sans);
  font-size: 10pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--gold-dark, #8A6D3B);
  margin: 14px 0 6px;
  break-after: avoid;
}
.page--content-single-column .content-area p,
.page--content-single-column .content-area li {
  font-family: var(--font-sans);
  font-size: 9.5pt;
  line-height: 1.55;
}
.page--content-single-column .content-area p { margin: 0 0 9px; }
.page--content-single-column .content-area ul,
.page--content-single-column .content-area ol { margin: 0 0 10px; padding-left: 18px; }
.page--content-single-column .content-area li { margin-bottom: 4px; }

/* tables: compact, repeatable, never wider than the column */
.page--content-single-column .content-area table {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 14px;
  font-size: 8pt;
  table-layout: fixed;
}
.page--content-single-column .content-area th {
  text-align: left;
  padding: 6px 8px;
  background: var(--warm-charcoal);
  color: var(--warm-white);
  font-family: var(--font-sans);
  font-weight: 600;
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.page--content-single-column .content-area td {
  padding: 5px 8px;
  border-bottom: 1px solid var(--border-light);
  vertical-align: top;
  font-family: var(--font-sans);
  line-height: 1.4;
  overflow-wrap: anywhere;
}
.page--content-single-column .content-area tbody tr:nth-child(even) { background: var(--stone-light); }

/* the nine-field profile summary renders as a key/value block, split into
   short chunks so it can never be clipped, but styled to read as one table */
.page--content-single-column .content-area table.profile-facts {
  table-layout: fixed;
  margin: 0 0 2px;
  font-size: 8.5pt;
}
.page--content-single-column .content-area table.profile-facts:last-of-type { margin-bottom: 12px; }
.page--content-single-column .content-area table.profile-facts tbody tr:nth-child(even) { background: transparent; }
.page--content-single-column .content-area table.profile-facts td {
  padding: 4px 8px 4px 0;
  border-bottom: 1px solid var(--border-light);
  line-height: 1.4;
}
.page--content-single-column .content-area table.profile-facts td:first-child {
  width: 32%;
  font-weight: 600;
  color: var(--text-secondary);
  padding-right: 12px;
}

/* Appendix styles are scoped to .content-area, not .appendix-body, because the
   splitter unwraps the body div when it distributes content across pages. */
.page--special-appendix .content-area { font-family: var(--font-sans); font-size: 8.5pt; }
.page--special-appendix .content-area h4 {
  font-family: var(--font-sans);
  font-size: 9.5pt;
  font-weight: 700;
  color: var(--warm-charcoal);
  margin: 12px 0 5px;
  break-after: avoid;
}
.page--special-appendix .content-area > *:first-child { margin-top: 0; }
.page--special-appendix .content-area p { font-size: 8.5pt; line-height: 1.5; margin: 0 0 9px; }
.page--special-appendix .content-area ul { margin: 0 0 8px; padding-left: 16px; list-style: disc; }
.page--special-appendix .content-area li {
  font-size: 7.5pt;
  line-height: 1.45;
  margin-bottom: 2px;
  overflow-wrap: anywhere;
  word-break: break-word;
}
.page--special-appendix .content-area table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  table-layout: fixed;
  margin: 6px 0 12px;
}
.page--special-appendix .content-area th {
  text-align: left;
  padding: 6px 8px;
  background: var(--warm-charcoal);
  color: var(--warm-white);
  font-weight: 600;
  font-size: 7pt;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.page--special-appendix .content-area td {
  padding: 5px 8px;
  border-bottom: 1px solid var(--border-light);
  vertical-align: top;
  overflow-wrap: anywhere;
}
.page--special-appendix .content-area td:first-child { width: 14%; font-weight: 600; }

/* executive summary findings keep their block integrity when splitting */
.page--special-executive-summary .finding { break-inside: avoid; }
.page--special-executive-summary .summary-intro { margin-bottom: 10px; }

/* contents entries: stable width for the number so nothing reflows */
.page--special-table-of-contents .toc-entry { align-items: baseline; }
.page--special-table-of-contents .toc-entry-page {
  min-width: 2.4em;
  text-align: right;
  font-variant-numeric: tabular-nums;
  flex: 0 0 auto;
}
.page--special-table-of-contents .toc-entry-text { flex: 0 1 auto; }
.page--special-table-of-contents .toc-entry-dots { flex: 1 1 auto; }

/* callouts */
.page--content-single-column .content-area .callout { break-inside: avoid; margin: 10px 0 12px; }

/* continuation pages hide the heading and rule */
.page[data-continuation] .content-heading,
.page[data-continuation] .heading-rule,
.page[data-continuation] .toc-title,
.page[data-continuation] .toc-rule,
.page[data-continuation] .appendix-header { display: none; }
.page--special-appendix[data-continuation] .content-area { top: var(--safe-margin-top); }

@media screen {
  body { background: #E8E4DE; padding: 24px 0; }
  #document-pages > .page { box-shadow: 0 2px 16px rgba(0,0,0,0.18); margin: 0 auto 24px; }
}
"""


def main():
    with open(META_PATH, encoding="utf-8") as f:
        meta = json.load(f)
    with open(MD_PATH, encoding="utf-8") as f:
        md = f.read()

    logo_dark = data_uri_svg(os.path.join(BRAND, "assets", "tokenomics-logo-dark.svg"))
    logo_light = data_uri_svg(os.path.join(BRAND, "assets", "tokenomics-logo-light.svg"))

    with open(os.path.join(BRAND, "css", "brand-system.css"), encoding="utf-8") as f:
        brand_css = f.read()

    tpl_names = [
        "cover-minimal-typographic", "special-table-of-contents",
        "special-executive-summary", "section-typographic",
        "content-single-column", "special-appendix",
        "closing-cta-contact", "closing-back-cover",
    ]
    tpl_css = "\n".join(template_style(t) for t in tpl_names)
    for needed in (".page--content-single-column .content-area",
                   ".page--special-appendix .content-area",
                   ".page--closing-cta-contact .cta-wrapper"):
        if needed not in tpl_css:
            raise SystemExit("template CSS missing: %s" % needed)

    # ------------------------------------------------------------------
    # split the markdown into sections on H2
    # ------------------------------------------------------------------
    lines = md.split("\n")
    sections = []
    cur = None
    for line in lines:
        m = re.match(r"^##\s+(?!#)(.*)$", line)
        if m:
            cur = {"title": m.group(1).strip(), "lines": []}
            sections.append(cur)
        elif cur is not None:
            cur["lines"].append(line)

    sec_meta = {s["number"]: s for s in meta["sections"]}

    pages = []
    toc = [{"level": 1, "text": "Executive Summary", "ref": "sec-exec"}]

    pages.append(page_cover(meta, logo_dark))
    toc_placeholder_index = 1          # TOC page is inserted here once built
    pages.append(page_exec_summary(meta["executive_summary"]))

    profile_sections = set(meta.get("profile_sections", []))

    for sec in sections:
        m = re.match(r"^(\d+|[A-Z])\.\s+(.*)$", sec["title"])
        if not m:
            continue
        num, title = m.group(1), m.group(2).strip()
        info = sec_meta.get(num, {})
        toc_id = "sec-%s" % num
        toc.append({"level": 1, "text": "%s. %s" % (num, title), "ref": toc_id})

        if SECTION_DIVIDERS:
            pages.append(page_divider(
                num.zfill(2) if num.isdigit() else num,
                title,
                info.get("subtitle", ""),
                toc_id,
            ))
            head_id, head_text = None, None
        else:
            # No divider page: the section title and the contents anchor ride on
            # the section's first content page instead. Twelve dividers cost
            # twelve near-empty pages in a document the client asked to be short.
            head_id, head_text = toc_id, "%s. %s" % (num, title)

        body_lines = sec["lines"]

        if num in profile_sections and PROFILE_PAGE_BREAKS:
            # one page per profile so each protocol starts clean
            groups, current, lead = [], None, []
            for ln in body_lines:
                if re.match(r"^###\s+(?!#)", ln):
                    if current:
                        groups.append(current)
                    current = [ln]
                elif current is None:
                    lead.append(ln)          # section intro, before any profile
                else:
                    current.append(ln)
            if current:
                groups.append(current)
            # the intro rides on the first profile page rather than taking a
            # near-empty page of its own
            if lead and groups:
                groups[0] = lead + [""] + groups[0]
            for gi, g in enumerate(groups):
                head = ""
                for ln in g:
                    if re.match(r"^###\s+(?!#)", ln):
                        head = ln.strip().lstrip("#").strip()
                        break
                am = re.match(r"^(\d+\.\d+)\s", head)
                if am:
                    toc.append({"level": 2, "text": head, "ref": "s-%s" % am.group(1).replace(".", "-")})
                first = gi == 0
                pages.append(page_content(
                    head_text if first else None,
                    "".join(md_blocks(g)),
                    head_id if first else None,
                ))
        else:
            for ln in body_lines:
                hm = re.match(r"^###\s+(?!#)(.*)$", ln)
                if hm:
                    h = hm.group(1).strip()
                    am = re.match(r"^(\d+\.\d+)\s", h)
                    if am:
                        toc.append({"level": 2, "text": h, "ref": "s-%s" % am.group(1).replace(".", "-")})
            pages.append(page_content(
                "%s. %s" % (num, title),
                "".join(md_blocks(body_lines)),
                head_id,
            ))

    # ------------------------------------------------------------------
    # appendices
    # ------------------------------------------------------------------
    app_meta = meta["appendices"]
    pages.append(page_divider("A", app_meta["divider_title"], app_meta["divider_subtitle"], "sec-app"))
    toc.append({"level": 1, "text": app_meta["divider_title"], "ref": "sec-app"})

    for app in app_meta["items"]:
        with open(os.path.join(WORKING, app["file"]), encoding="utf-8") as f:
            content = f.read()
        content_lines = [l for l in content.split("\n") if not re.match(r"^#\s", l)]
        ref = "app-%s" % app["letter"]
        toc.append({"level": 2, "text": "Appendix %s: %s" % (app["letter"], app["title"]), "ref": ref})
        pages.append(page_appendix(
            "Appendix %s" % app["letter"], app["title"],
            "".join(md_blocks(content_lines)), ref,
        ))

    # The closing call-to-action page is off. This is a research deliverable,
    # not a pitch, and its copy pointed at decisions the report no longer makes.
    if CLOSING_CTA:
        pages.append(page_cta(meta, logo_dark))
    pages.append(page_back_cover(meta, logo_light))

    pages.insert(toc_placeholder_index, page_toc(toc))

    out = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light">
<meta name="format-detection" content="telephone=no">
<title>%s &mdash; Tokenomics.net</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Libre+Franklin:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
%s
</style>
<style>
%s
</style>
<style>
%s
</style>
</head>
<body>
<main id="document-pages">
%s
</main>
<script>%s</script>
</body>
</html>
""" % (esc(meta["title"]), brand_css, tpl_css, EXTRA_CSS, "\n".join(pages), AUTO_CONTINUE)

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(out)

    print("wrote %s" % OUT_HTML)
    print("source pages before auto-continue: %d" % len(pages))
    print("toc entries: %d" % len(toc))


if __name__ == "__main__":
    main()
