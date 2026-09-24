// Render the assembled whitepaper HTML (adapted from render_mdd.js) to PDF and report layout defects.
//   node render_wp.js <input.html> <output.pdf>
// Measures real element bottoms against the content area, and reports overflow,
// empty pages, sparse pages and unresolved contents entries.
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.resolve(process.argv[2]);
const PDF = path.resolve(process.argv[3] || HTML.replace(/\.html$/, '.pdf'));

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', protocolTimeout: 600000,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  page.on('console', (m) => { if (m.type() === 'error') console.log('[page]', m.text().slice(0, 200)); });
  page.on('pageerror', (e) => console.log('[pageerror]', String(e).slice(0, 300)));
  await page.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1 });
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 240000 });
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 480000, polling: 1000 });
  await new Promise((r) => setTimeout(r, 2000));

  const report = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll('#document-pages > .page'));
    const overflow = [], empties = [], sparse = [], mermaidFail = [];
    pages.forEach((p, i) => {
      // mermaid render check on every page
      p.querySelectorAll('.mermaid').forEach((m) => {
        if (!m.querySelector('svg')) mermaidFail.push({ page: i + 1, text: (m.textContent || '').slice(0, 60) });
      });
      const ca = p.querySelector('.content-area');
      if (!ca) return;
      const r = ca.getBoundingClientRect();
      let worst = 0, culprit = '', lowest = r.top, count = 0;
      Array.from(ca.children).forEach((c) => {
        if (c.classList.contains('page-number')) return;
        count++;
        const b = c.getBoundingClientRect().bottom;
        const d = b - r.bottom;
        if (d > worst) { worst = d; culprit = (c.textContent || '').trim().slice(0, 70); }
        if (b > lowest) lowest = b;
      });
      if (worst > 2) overflow.push({ page: i + 1, template: p.getAttribute('data-template'), px: Math.round(worst), culprit });
      if (count === 0) empties.push({ page: i + 1, template: p.getAttribute('data-template') });
      const fill = (lowest - r.top) / r.height;
      if (count > 0 && fill < 0.12 && !p.hasAttribute('data-continuation') === false) sparse.push({ page: i + 1, fill: Math.round(fill * 100) });
      if (count > 0 && fill < 0.10) sparse.push({ page: i + 1, template: p.getAttribute('data-template'), fill: Math.round(fill * 100) });
    });
    const tocBad = [];
    document.querySelectorAll('.toc-entry').forEach((e) => {
      const pg = e.querySelector('.toc-entry-page');
      if (!pg || !/^\d+$/.test(pg.textContent.trim())) tocBad.push((e.textContent || '').trim().slice(0, 60));
    });
    return { total: pages.length, overflow, empties, sparse, mermaidFail, tocBad };
  });

  // Whitepaper extras: fill per page, continuation pages, and diagram text size.
  const extra = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll('#document-pages > .page'));
    const fills = [], continuations = [], diagrams = [];
    pages.forEach((p, i) => {
      if (p.hasAttribute('data-continuation')) continuations.push(i + 1);
      const ca = p.querySelector('.content-area');
      if (ca) {
        const r = ca.getBoundingClientRect();
        let lowest = r.top;
        Array.from(ca.children).forEach((c) => { const b = c.getBoundingClientRect().bottom; if (b > lowest) lowest = b; });
        fills.push((i + 1) + ':' + Math.round((lowest - r.top) / r.height * 100));
      }
      p.querySelectorAll('.mermaid svg').forEach((svg) => {
        const vb = svg.viewBox && svg.viewBox.baseVal;
        const w = svg.getBoundingClientRect().width, h = svg.getBoundingClientRect().height;
        const scale = vb && vb.width ? w / vb.width : 1;
        // smallest rendered text in the diagram, in pt
        let minPx = 99;
        svg.querySelectorAll('text, foreignObject div, foreignObject span').forEach((t) => {
          if (!(t.textContent || '').trim()) return;
          const fs = parseFloat(getComputedStyle(t).fontSize) || 14;
          if (fs * scale < minPx) minPx = fs * scale;
        });
        const fig = svg.closest('figure');
        const cap = fig ? (fig.querySelector('figcaption') || {}).textContent || '' : '';
        diagrams.push({ page: i + 1, fig: cap.slice(0, 10), scale: +scale.toFixed(2), minPt: +(minPx * 0.75).toFixed(1), w: Math.round(w), h: Math.round(h) });
      });
    });
    // Single-column audit (plan 3.5): any HTML element inside a content area that lays out two or more
    // visible children side by side (grid/flex rows, multi-column, floats). STAT3 rows are the one exception.
    const twoCol = [];
    pages.forEach((p, i) => {
      const ca = p.querySelector('.content-area');
      if (!ca) return;
      [ca].concat(Array.from(ca.querySelectorAll('*'))).forEach((el) => {
        if (el.closest('svg') || el.closest('.wp-stat3') || el.closest('.toc-entry')) return; // TOC leader rows are not text columns
        const s = getComputedStyle(el);
        const kids = Array.from(el.children).filter((c) => { const r = c.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(c).position !== 'absolute'; });
        let side = false;
        if (/(grid|flex)/.test(s.display) && kids.length > 1) {
          // side by side = two visible children whose vertical ranges overlap
          for (let a = 0; a < kids.length && !side; a++) for (let b = a + 1; b < kids.length && !side; b++) {
            const ra = kids[a].getBoundingClientRect(), rb = kids[b].getBoundingClientRect();
            if (Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top) > 2) side = true;
          }
        }
        if (parseInt(s.columnCount) > 1) side = true;
        if (s.float && s.float !== 'none') side = true;
        if (side) twoCol.push({ page: i + 1, el: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0], text: (el.textContent || '').trim().slice(0, 40) });
      });
    });
    return { fills: fills.join(' '), continuations, diagrams, twoCol };
  });

  console.log(JSON.stringify(report, null, 1));
  console.log('FILLS', extra.fills);
  console.log('CONTINUATIONS', JSON.stringify(extra.continuations));
  extra.diagrams.forEach((d) => console.log('DIAG', JSON.stringify(d)));
  console.log('TWOCOL', JSON.stringify(extra.twoCol));
  console.log('MIN_DIAG_PT', Math.min.apply(null, extra.diagrams.map((d) => d.minPt)));
  if (process.env.DEBUG_BLOCKS) {
    const dbg = await page.evaluate(() => Array.from(document.querySelectorAll('#document-pages > .page')).map((p, i) => {
      const ca = p.querySelector('.content-area'); if (!ca) return '';
      const top = ca.getBoundingClientRect().top;
      return 'P' + (i + 1) + (p.hasAttribute('data-continuation') ? '(cont)' : '') + ' h=' + Math.round(ca.getBoundingClientRect().height) + ': ' +
        Array.from(ca.children).map((c) => { const r = c.getBoundingClientRect();
          return c.tagName.toLowerCase() + (c.className ? '.' + String(c.className).split(' ')[0] : '') + '[' + Math.round(r.bottom - top) + '] ' + (c.textContent || '').trim().slice(0, 18).replace(/\s+/g, ' '); }).join(' | ');
    }));
    dbg.forEach((l) => l && console.log(l));
  }
  if (process.env.NO_PDF) { await browser.close(); return; }

  await page.pdf({
    path: PDF, width: '8.5in', height: '11in', printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
    pageRanges: '1-' + report.total, // clamp: no trailing blank sheet
  });
  console.log('PDF written:', PDF);
  await browser.close();
})();
