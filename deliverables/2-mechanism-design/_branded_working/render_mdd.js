// Render the assembled MDD HTML to PDF and report layout defects.
//   node render_mdd.js <input.html> <output.pdf>
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

  console.log(JSON.stringify(report, null, 1));

  await page.pdf({
    path: PDF, width: '8.5in', height: '11in', printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
    pageRanges: '1-' + report.total, // clamp: no trailing blank sheet
  });
  console.log('PDF written:', PDF);
  await browser.close();
})();
