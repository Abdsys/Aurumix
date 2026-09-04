#!/usr/bin/env python3
"""
Build the branded HTML for the two Phase 5 documents from their markdown.

    python build_sim.py results
    python build_sim.py setup

Generalised from the market-research build. Self-contained output: brand CSS,
template CSS, logos and chart PNGs are all inlined. Page numbering starts after
the contents page. Formulas render through KaTeX before the page splitter runs.

Page sequences follow the Stockpile simulation deliverable:
  RESULTS: cover -> contents -> executive summary -> [divider + content] per Part
           -> recommendation cards -> appendix pages -> back cover
  SETUP:   cover -> contents -> [divider + content] per section -> back cover
"""

import base64
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHASE = os.path.dirname(HERE)                       # deliverables/5-simulations
BRAND = r"C:\Users\BlockApex\.claude\plugins\marketplaces\tokenomics-net\tokenomics-plugin\standards\branded-docs-main"

DOCS = {
    "results": dict(md=os.path.join(PHASE, "SIMULATION_RESULTS.md"),
                    meta=os.path.join(HERE, "meta_results.json"),
                    out=os.path.join(HERE, "SIMULATION_RESULTS.html"),
                    dividers_per="part"),
    "setup": dict(md=os.path.join(PHASE, "SIMULATION_SETUP.md"),
                  meta=os.path.join(HERE, "meta_setup.json"),
                  out=os.path.join(HERE, "SIMULATION_SETUP.html"),
                  dividers_per="section"),
}

TABLE_CHUNK = 12   # tables are atomic for the splitter; 12 short rows still fit a page


# ─────────────────────────────────────────────────────────────────────────────
# inline markdown
# ─────────────────────────────────────────────────────────────────────────────

def esc(t):
    return html.escape(t, quote=False)


def inline(text):
    ph = {}

    def stash(s):
        k = "\x00%d\x00" % len(ph)
        ph[k] = s
        return k

    # inline math first so its backslashes and underscores survive.
    # Maths never opens with a digit or a space in these documents; money always
    # opens with a digit. Without that guard "$3.18 ... $410,000" is read as one
    # inline formula and eats the prose between the two figures.
    text = re.sub(r"\$(?![\d\s])([^$\n]+?)\$",
                  lambda m: stash("\\(" + m.group(1) + "\\)"), text)
    text = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % esc(m.group(1))), text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda m: stash('<a href="%s">%s</a>' % (esc(m.group(2)), esc(m.group(1)))), text)
    text = esc(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    for k, v in ph.items():
        text = text.replace(k, v)
    return text


# ─────────────────────────────────────────────────────────────────────────────
# block markdown -> html blocks
# ─────────────────────────────────────────────────────────────────────────────

def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render_table(header, rows, align):
    out = []
    n_chunks = max(1, -(-len(rows) // TABLE_CHUNK)) if rows else 1
    size = -(-len(rows) // n_chunks) if rows else 1
    chunks = [rows[i:i + size] for i in range(0, len(rows), size)] or [[]]
    for chunk in chunks:
        h = "".join('<th class="%s">%s</th>' % (align[i] if i < len(align) else "", inline(c))
                    for i, c in enumerate(header))
        body = ""
        for r in chunk:
            cells = list(r) + [""] * (len(header) - len(r))
            body += "<tr>%s</tr>" % "".join(
                '<td class="%s">%s</td>' % (align[i] if i < len(align) else "", inline(c))
                for i, c in enumerate(cells[:len(header)]))
        out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (h, body))
    return out


def data_uri(path, mime):
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def md_blocks(lines, ctx):
    """Parse markdown lines into HTML block strings. ctx carries the doc dir."""
    blocks = []
    i, n = 0, len(lines)
    fig_no = ctx.setdefault("fig", 0)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue

        # fenced code
        if s.startswith("```"):
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            blocks.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
            continue

        # display math  $$...$$  (one line or multi-line)
        if s.startswith("$$"):
            if s.endswith("$$") and len(s) > 4:
                body = s[2:-2]
                i += 1
            else:
                buf = [s[2:]]
                i += 1
                while i < n and not lines[i].strip().endswith("$$"):
                    buf.append(lines[i])
                    i += 1
                if i < n:
                    buf.append(lines[i].strip()[:-2])
                    i += 1
                body = "\n".join(buf)
            blocks.append('<div class="formula-display-block">\\[%s\\]</div>' % body.strip())
            continue

        # headings h3..h5
        m = re.match(r"^(#{3,5})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            anchor = ' id="h-%s"' % slug(title) if level == 3 else ""
            blocks.append("<h%d%s>%s</h%d>" % (level, anchor, inline(title), level))
            i += 1
            continue

        # image
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", s)
        if m:
            alt, src = m.group(1), m.group(2)
            path = os.path.normpath(os.path.join(ctx["dir"], src))
            uri = data_uri(path, "image/png") if os.path.exists(path) else src
            ctx["fig"] += 1
            blocks.append('<figure class="chart"><img src="%s" alt="%s">'
                          '<figcaption>Figure %d. %s</figcaption></figure>'
                          % (uri, esc(alt), ctx["fig"], esc(alt)))
            i += 1
            continue

        # table
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|?\s*$", lines[i + 1].strip()):
            header = split_row(s)
            spec = split_row(lines[i + 1].strip())
            align = []
            for c in spec:
                c = c.strip()
                if c.endswith(":") and not c.startswith(":"):
                    align.append("num")
                else:
                    align.append("")
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            blocks.extend(render_table(header, rows, align))
            continue

        # blockquote -> callout
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            text = " ".join(x for x in buf if x)
            title = "Key insight"
            tm = re.match(r"^\*\*(.+?)\*\*[:.]?\s*(.*)$", text)
            if tm:
                title, text = tm.group(1), tm.group(2)
            blocks.append('<div class="callout"><div class="callout-title">%s</div>'
                          '<div class="callout-body">%s</div></div>' % (inline(title), inline(text)))
            continue

        # unordered list
        if re.match(r"^[-*+]\s+", s):
            items = []
            while i < n:
                t = lines[i].strip()
                if re.match(r"^[-*+]\s+", t):
                    items.append(re.sub(r"^[-*+]\s+", "", t))
                    i += 1
                elif t and not re.match(r"^(#{1,6}\s|\||>|\d+\.\s|\$\$|```|!\[)", t) and items:
                    items[-1] += " " + t
                    i += 1
                else:
                    break
            blocks.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        # ordered list
        if re.match(r"^\d+\.\s+", s):
            items = []
            start = re.match(r"^(\d+)\.", s).group(1)
            while i < n:
                t = lines[i].strip()
                if re.match(r"^\d+\.\s+", t):
                    items.append(re.sub(r"^\d+\.\s+", "", t))
                    i += 1
                elif t and not re.match(r"^(#{1,6}\s|\||>|[-*+]\s|\$\$|```|!\[)", t) and items:
                    items[-1] += " " + t
                    i += 1
                else:
                    break
            attr = ' start="%s"' % start if start != "1" else ""
            blocks.append("<ol%s>%s</ol>" % (attr, "".join("<li>%s</li>" % inline(x) for x in items)))
            continue

        # rule
        if re.match(r"^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$", s):
            i += 1
            continue

        # paragraph
        buf = [s]
        i += 1
        while i < n:
            t = lines[i].strip()
            if not t or re.match(r"^(#{1,6}\s|\||>|[-*+]\s|\d+\.\s|\$\$|```|!\[)", t) or re.match(r"^(-\s*){3,}$", t):
                break
            buf.append(t)
            i += 1
        text = " ".join(buf)
        # A paragraph that is only a bold label ("**Customer behaviour:**") is a
        # run-in heading. Render it as h4 so the splitter never strands it at
        # the foot of a page away from the table it introduces.
        lm = re.match(r"^\*\*([^*]+?):?\*\*:?$", text)
        if lm:
            blocks.append("<h4>%s</h4>" % inline(lm.group(1).rstrip(":")))
        else:
            blocks.append("<p>%s</p>" % inline(text))
    return blocks


# ─────────────────────────────────────────────────────────────────────────────
# page builders
# ─────────────────────────────────────────────────────────────────────────────

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
        rows.append('<div class="toc-entry %s" data-toc-ref="%s">'
                    '<span class="toc-entry-text">%s</span><span class="toc-entry-dots"></span>'
                    '<span class="toc-entry-page">000</span></div>' % (cls, e["ref"], esc(e["text"])))
    return """<div class="page page--special-table-of-contents" data-template="special-table-of-contents" data-auto-continue>
  <div class="content-area">
    <h1 class="toc-title">Contents</h1>
    <hr class="toc-rule">
    <div class="toc-list" data-text-role="toc-entries">%s</div>
  </div>
</div>""" % "".join(rows)


def page_exec_summary(ex):
    stats = "".join('<div class="stat-card"><div class="stat-value">%s</div><div class="stat-label">%s</div></div>'
                    % (esc(s["value"]), esc(s["label"])) for s in ex["stats"])
    findings = "".join('<div class="finding"><div class="finding-number">%d</div><div class="finding-content">'
                       '<div class="finding-title">%s</div><div class="finding-body">%s</div></div></div>'
                       % (k + 1, inline(f["title"]), inline(f["body"])) for k, f in enumerate(ex["findings"]))
    intro = "".join('<p class="summary-intro">%s</p>' % inline(p) for p in ex["intro"])
    return """<div class="page page--special-executive-summary" data-template="special-executive-summary" data-auto-continue data-toc-id="sec-exec">
  <div class="content-area">
    <h1 class="summary-title">Executive summary</h1>
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
    head = ('<h2 class="content-heading">%s</h2>\n    <hr class="heading-rule">\n    ' % inline(heading)) if heading else ""
    anchor = ' data-toc-id="%s"' % toc_id if toc_id else ""
    return """<div class="page page--content-single-column" data-template="content-single-column" data-auto-continue%s>
  <div class="content-area">
    %s<div data-text-role="body">%s</div>
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (anchor, head, body_html)


def page_rec_cards(title, desc, cards, toc_id):
    items = []
    for k, c in enumerate(cards):
        tag = "high" if k < 3 else "medium"
        items.append('<div class="recommendation-card"><div class="recommendation-number">%d</div>'
                     '<div class="recommendation-content"><div class="recommendation-title">%s '
                     '<span class="priority-tag priority-tag--%s">%s</span></div>'
                     '<div class="recommendation-body">%s</div></div></div>'
                     % (k + 1, inline(c["title"]), tag, tag.capitalize(), c["body"]))
    return """<div class="page page--content-recommendation-cards" data-template="content-recommendation-cards" data-auto-continue data-toc-id="%s">
  <div class="content-area">
    <h2 class="rec-heading" data-text-role="section-title">%s</h2>
    <hr class="heading-rule">
    <p class="rec-desc" data-text-role="body">%s</p>
    <div class="rec-list" data-text-role="rec-list">%s</div>
  </div>
  <div class="page-number" data-text-role="page-number"></div>
</div>""" % (toc_id, esc(title), inline(desc), "".join(items))


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


def page_back_cover(meta, logo_light):
    return """<div class="page page--closing-back-cover" data-template="closing-back-cover">
  <div class="back-center">
    <img src="%s" alt="Tokenomics.net" class="logo logo--2xl">
    <p class="back-tagline">%s</p>
  </div>
  <div class="back-legal">%s</div>
</div>""" % (logo_light, esc(meta["tagline"]), esc(meta["legal"]))


# ─────────────────────────────────────────────────────────────────────────────
# template css, runtime js, extra css
# ─────────────────────────────────────────────────────────────────────────────

def template_style(name):
    with open(os.path.join(BRAND, "templates", "portrait", name + ".html"), encoding="utf-8") as f:
        src = f.read()
    m = re.search(r"<style>(.*?)</style>", src, re.S)
    css = m.group(1) if m else ""
    if name == "section-typographic":
        idx = css.find(".page--section-typographic .section-image")
        if idx != -1:
            css = css[:idx]
    return css


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
    if(t==='table'||t==='figure'||t==='blockquote'||t==='pre')return true;
    if(el.classList.contains('callout')||el.classList.contains('stats-row')||
       el.classList.contains('finding')||el.classList.contains('formula-display-block')||
       el.classList.contains('recommendation-card'))return true;
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
         !ch[n].classList.contains('rec-heading')&&!ch[n].classList.contains('rec-desc')&&
         ch[n].tagName.toLowerCase()!=='hr')nd++;
    }
    if(si===0&&nd<=1){page.setAttribute('data-auto-continued','');return[page];}
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
    for(var pass=0;pass<4;pass++){
      var again=Array.prototype.slice.call(document.querySelectorAll('.page[data-auto-continue]')).filter(overflows);
      if(again.length===0)break;
      for(var j=0;j<again.length;j++)process(again[j],0);
      renumber();
      populateTOC();
    }
    document.body.setAttribute('data-render-complete','1');
    document.dispatchEvent(new Event('auto-continue-complete'));
  }
  function start(){
    // formulas must be typeset before pages are measured and split
    var k=window.__katexReady||Promise.resolve();
    k.then(function(){return document.fonts.ready;}).then(function(){
      var imgs=Array.prototype.slice.call(document.images).filter(function(im){return !im.complete;});
      return Promise.all(imgs.map(function(im){return new Promise(function(r){im.onload=im.onerror=r;});}));
    }).then(run);
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',start);}else{start();}
})();
"""

KATEX_HEAD = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script>window.__katexReady=new Promise(function(res){window.__katexResolve=res;});</script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});window.__katexResolve();"
  onerror="window.__katexResolve();"></script>
"""

EXTRA_CSS = """
#document-pages > .page { page-break-after: always; break-after: page; }
#document-pages > .page:last-child { page-break-after: avoid; break-after: avoid; }

.page--content-single-column .content-area h3,
.page--special-appendix .content-area h3 {
  font-family: var(--font-serif); font-size: 14pt; font-weight: 700; color: var(--warm-charcoal);
  line-height: 1.25; margin: 18px 0 8px; break-after: avoid;
}
.page--content-single-column .content-area h3:first-child { margin-top: 0; }
.page--content-single-column .content-area h4,
.page--special-appendix .content-area h4 {
  font-family: var(--font-sans); font-size: 10pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--gold-dark, #8A6D3B); margin: 14px 0 6px; break-after: avoid;
}
/* body type stays at the template's document scale (10.5pt), as in the
   Stockpile deliverable; only spacing is set here */
.page--content-single-column .content-area p,
.page--content-single-column .content-area li { font-family: var(--font-sans); font-size: 11pt; line-height: 1.6; }
.page--content-single-column .content-area p { margin: 0 0 10px; }
.page--content-single-column .content-area h3 { font-size: 15pt; margin: 20px 0 8px; }
.page--content-single-column .content-area ul,
.page--content-single-column .content-area ol { margin: 0 0 10px; padding-left: 18px; }
.page--content-single-column .content-area li { margin-bottom: 4px; }

.page--content-single-column .content-area table,
.page--special-appendix .content-area table {
  width: 100%; border-collapse: collapse; margin: 8px 0 14px; font-size: 8pt; table-layout: auto;
}
.page--special-appendix .content-area table { margin: 8px 0 14px; font-size: 8pt; }
.page--special-appendix .content-area td { padding: 4px 8px; }
.page--special-appendix .content-area th { padding: 5px 8px; }
.page--special-appendix .content-area h4 { margin: 8px 0 3px; }
.page--special-appendix .content-area p { margin: 0 0 10px; }
.page--content-single-column .content-area th,
.page--special-appendix .content-area th {
  text-align: left; padding: 6px 8px; background: var(--warm-charcoal); color: var(--warm-white);
  font-family: var(--font-sans); font-weight: 600; font-size: 7.5pt; text-transform: uppercase; letter-spacing: 0.04em;
}
.page--content-single-column .content-area td,
.page--special-appendix .content-area td {
  padding: 5px 8px; border-bottom: 1px solid var(--border-light); vertical-align: top;
  font-family: var(--font-sans); line-height: 1.4; overflow-wrap: anywhere;
}
.page--content-single-column .content-area tbody tr:nth-child(even),
.page--special-appendix .content-area tbody tr:nth-child(even) { background: var(--stone-light); }
.content-area th.num, .content-area td.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }

/* charts */
.content-area figure.chart { margin: 10px 0 14px; break-inside: avoid; }
.content-area figure.chart img { width: 100%; height: auto; display: block; border: 1px solid var(--border-light); }
.content-area figure.chart figcaption {
  font-family: var(--font-sans); font-size: 8pt; color: var(--text-secondary); margin-top: 5px; font-style: italic;
}

/* formulas */
.formula-display-block { background: var(--warm-white); border: 1px solid var(--border-light); border-left: 4px solid var(--gold);
  padding: 12px 20px; margin: 12px 0; text-align: center; break-inside: avoid; overflow-x: auto; }
.formula-display-block .katex { font-size: 1.15em; }
.content-area .katex-display { margin: 0; }

/* code */
.content-area pre { background: var(--stone-light); border: 1px solid var(--border-light); padding: 10px 12px;
  font-size: 8pt; line-height: 1.5; margin: 8px 0 12px; overflow-x: auto; break-inside: avoid; }
.content-area code { font-family: ui-monospace, Consolas, monospace; font-size: 0.92em; }

/* appendix */
.page--special-appendix .content-area { font-family: var(--font-sans); font-size: 11pt; }
.page--special-appendix .content-area > *:first-child { margin-top: 0; }
.page--special-appendix .content-area p { font-size: 11pt; line-height: 1.6; margin: 0 0 10px; }
.page--special-appendix .content-area ul { margin: 0 0 8px; padding-left: 16px; list-style: disc; }
.page--special-appendix .content-area li { font-size: 8pt; line-height: 1.45; margin-bottom: 2px; }

/* executive summary */
.page--special-executive-summary .finding { break-inside: avoid; }
.page--special-executive-summary .summary-intro { margin-bottom: 10px; }

/* recommendation cards */
.page--content-recommendation-cards .recommendation-card { break-inside: avoid; }
.page--content-recommendation-cards .recommendation-body p { margin: 0 0 6px; }

/* contents */
.page--special-table-of-contents .toc-entry { align-items: baseline; padding-top: 4px; padding-bottom: 4px; }
.page--special-table-of-contents .toc-entry--sub { padding-top: 2px; padding-bottom: 2px; }
.page--special-table-of-contents .toc-entry-page { min-width: 2.4em; text-align: right; font-variant-numeric: tabular-nums; flex: 0 0 auto; }
.page--special-table-of-contents .toc-entry-text { flex: 0 1 auto; }
.page--special-table-of-contents .toc-entry-dots { flex: 1 1 auto; }

/* callouts */
.page--content-single-column .content-area .callout { break-inside: avoid; margin: 10px 0 12px; }

/* continuation pages hide the heading and rule */
.page[data-continuation] .content-heading, .page[data-continuation] .heading-rule,
.page[data-continuation] .toc-title, .page[data-continuation] .toc-rule,
.page[data-continuation] .appendix-header, .page[data-continuation] .rec-heading, .page[data-continuation] .rec-desc { display: none; }
.page--special-appendix[data-continuation] .content-area { top: var(--safe-margin-top); }

@media screen {
  body { background: #E8E4DE; padding: 24px 0; }
  #document-pages > .page { box-shadow: 0 2px 16px rgba(0,0,0,0.18); margin: 0 auto 24px; }
}
"""


# ─────────────────────────────────────────────────────────────────────────────
# document assembly
# ─────────────────────────────────────────────────────────────────────────────

def strip_front(md):
    """Remove YAML frontmatter, the H1, and the Prepared-by / Date metadata lines."""
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end != -1:
            md = md[end + 4:]
    lines = md.split("\n")
    out = []
    for ln in lines:
        s = ln.strip()
        if re.match(r"^#\s", s):
            continue
        if re.match(r"^\*\*(Prepared by|Date|Simulation version)\*\*\s*:", s) or \
           re.match(r"^\*\*(Prepared by|Date|Simulation version):\*\*", s):
            continue
        out.append(ln)
    return "\n".join(out)


def split_h2(md):
    sections, cur = [], None
    for line in md.split("\n"):
        m = re.match(r"^##\s+(?!#)(.*)$", line)
        if m:
            cur = {"title": m.group(1).strip(), "lines": []}
            sections.append(cur)
        elif cur is not None:
            cur["lines"].append(line)
    return sections


def split_h3(lines):
    """Return (lead_lines, [(h3_title, lines)])."""
    lead, groups, cur = [], [], None
    for ln in lines:
        m = re.match(r"^###\s+(?!#)(.*)$", ln)
        if m:
            cur = {"title": m.group(1).strip(), "lines": []}
            groups.append(cur)
        elif cur is None:
            lead.append(ln)
        else:
            cur["lines"].append(ln)
    return lead, groups


def build_results(meta, md, ctx):
    pages, toc = [], []
    sections = split_h2(md)
    pages.append(("cover", None))
    pages.append(("toc", None))
    toc.append({"level": 1, "text": "Executive summary", "ref": "sec-exec"})
    pages.append(("exec", None))

    part_no = 0
    for sec in sections:
        m = re.match(r"^Part\s+(\d+):\s*(.*)$", sec["title"])
        if not m:
            continue
        part_no += 1
        num, title = m.group(1), m.group(2).strip()
        toc_id = "sec-part-%s" % num
        info = meta["parts"].get(num, {})
        toc.append({"level": 1, "text": "Part %s: %s" % (num, title), "ref": toc_id})
        pages.append(("divider", (num.zfill(2), title, info.get("subtitle", ""), toc_id)))

        lead, groups = split_h3(sec["lines"])
        body_groups = []
        for g in groups:
            t = g["title"]
            if t.lower() == "executive summary":
                continue                       # replaced by the special page
            if t.lower() == "recommendations":
                # flush what we have, then the cards page, then continue
                if lead or body_groups:
                    pages.append(("content", (lead, body_groups, toc_id if not any(p[0] == "content" and p[1][2] == toc_id for p in pages) else None)))
                    for bg in body_groups:
                        toc.append({"level": 2, "text": bg["title"], "ref": "h-" + slug(bg["title"])})
                    lead, body_groups = [], []
                # parse #### N. Title blocks into cards
                cards, cur = [], None
                for ln in g["lines"]:
                    hm = re.match(r"^####\s+\d+\.\s+(.*)$", ln)
                    if hm:
                        cur = {"title": hm.group(1).strip(), "lines": []}
                        cards.append(cur)
                    elif cur is not None:
                        cur["lines"].append(ln)
                for c in cards:
                    c["body"] = "".join(md_blocks(c["lines"], ctx))
                toc.append({"level": 2, "text": "Recommendations", "ref": "sec-recs"})
                pages.append(("recs", ("Recommendations",
                                       "Each change is tied to a finding in this document, and each was run through the full simulation.",
                                       cards, "sec-recs")))
                continue
            if num == "5":
                # appendix pages, one per H3; the contents lists Part 5 only,
                # which keeps the contents to a single page
                ref = "app-" + slug(t)
                at = re.match(r"^(Appendix [A-Z]):\s*(.*)$", t)
                pages.append(("appendix", (at.group(1) if at else t, at.group(2) if at else "", g["lines"], ref)))
                continue
            body_groups.append(g)
        if num != "5" and (lead or body_groups):
            first_content_for_part = not any(p[0] == "content" and p[1][2] == toc_id for p in pages)
            pages.append(("content", (lead, body_groups, toc_id if first_content_for_part else None)))
            for bg in body_groups:
                toc.append({"level": 2, "text": bg["title"], "ref": "h-" + slug(bg["title"])})
    pages.append(("back", None))
    return pages, toc


def build_setup(meta, md, ctx):
    pages, toc = [], []
    sections = split_h2(md)
    pages.append(("cover", None))
    pages.append(("toc", None))
    for sec in sections:
        m = re.match(r"^(\d+)\.\s+(.*)$", sec["title"])
        if not m:
            continue
        num, title = m.group(1), m.group(2).strip()
        toc_id = "sec-%s" % num
        info = meta["sections"].get(num, {})
        toc.append({"level": 1, "text": "%s. %s" % (num, title), "ref": toc_id})
        pages.append(("divider", (num.zfill(2), title, info.get("subtitle", ""), toc_id)))
        lead, groups = split_h3(sec["lines"])
        # contents lists sections only, as in the Stockpile setup document;
        # fifteen sections with fifty-five sub-headings would run to three pages
        pages.append(("content", (lead, groups, None)))
    pages.append(("back", None))
    return pages, toc


def render_pages(pages, toc, meta, ctx, logo_dark, logo_light):
    out = []
    for kind, arg in pages:
        if kind == "cover":
            out.append(page_cover(meta, logo_dark))
        elif kind == "toc":
            out.append(page_toc(toc))
        elif kind == "exec":
            out.append(page_exec_summary(meta["executive_summary"]))
        elif kind == "divider":
            out.append(page_divider(*arg))
        elif kind == "content":
            lead, groups, toc_id = arg
            body = "".join(md_blocks(lead, ctx))
            for g in groups:
                body += '<h3 id="h-%s">%s</h3>' % (slug(g["title"]), inline(g["title"]))
                body += "".join(md_blocks(g["lines"], ctx))
            out.append(page_content(None, body, toc_id))
        elif kind == "recs":
            out.append(page_rec_cards(*arg))
        elif kind == "appendix":
            title, subtitle, lines, ref = arg
            out.append(page_appendix(title, subtitle, "".join(md_blocks(lines, ctx)), ref))
        elif kind == "back":
            out.append(page_back_cover(meta, logo_light))
    return out


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "results"
    d = DOCS[which]
    with open(d["meta"], encoding="utf-8") as f:
        meta = json.load(f)
    with open(d["md"], encoding="utf-8") as f:
        md = strip_front(f.read().replace("\r\n", "\n"))
    ctx = {"dir": PHASE, "fig": 0}

    logo_dark = data_uri(os.path.join(BRAND, "assets", "tokenomics-logo-dark.svg"), "image/svg+xml")
    logo_light = data_uri(os.path.join(BRAND, "assets", "tokenomics-logo-light.svg"), "image/svg+xml")
    with open(os.path.join(BRAND, "css", "brand-system.css"), encoding="utf-8") as f:
        brand_css = f.read()

    tpl_names = ["cover-minimal-typographic", "special-table-of-contents", "special-executive-summary",
                 "section-typographic", "content-single-column", "content-recommendation-cards",
                 "special-appendix", "closing-back-cover"]
    tpl_css = "\n".join(template_style(t) for t in tpl_names)
    for needed in (".page--content-single-column .content-area", ".page--special-appendix .content-area",
                   ".page--content-recommendation-cards .content-area"):
        if needed not in tpl_css:
            raise SystemExit("template CSS missing: %s" % needed)

    if which == "results":
        pages, toc = build_results(meta, md, ctx)
    else:
        pages, toc = build_setup(meta, md, ctx)
    body_pages = render_pages(pages, toc, meta, ctx, logo_dark, logo_light)

    has_math = "\\[" in "".join(body_pages) or "\\(" in "".join(body_pages)
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
%s
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
""" % (esc(meta["title"]), KATEX_HEAD if has_math else "", brand_css, tpl_css, EXTRA_CSS,
       "\n".join(body_pages), AUTO_CONTINUE)

    with open(d["out"], "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote %s" % d["out"])
    print("source pages before auto-continue: %d | toc entries: %d | figures: %d | math: %s"
          % (len(pages), len(toc), ctx["fig"], has_math))


if __name__ == "__main__":
    main()
