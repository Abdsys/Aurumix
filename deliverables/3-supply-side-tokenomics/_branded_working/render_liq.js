// Render an assembled HTML to PDF and report layout defects.
//   node render_sim.js <input.html> <output.pdf>
// Measures real element bottoms against the content area (not scrollHeight),
// and reports overflow, empty pages, sparse pages and unresolved contents entries.
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.resolve(process.argv[2]);
const PDF = path.resolve(process.argv[3] || HTML.replace(/\.html$/, '.pdf'));

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1 });
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 180000 });
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 180000 });
  await new Promise((r) => setTimeout(r, 1500));

  const report = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll('#document-pages > .page'));
    const overflow = [], empties = [], sparse = [];
    pages.forEach((p, i) => {
      const ca = p.querySelector('.content-area');
      if (!ca) return;
      const areaBottom = ca.getBoundingClientRect().bottom;
      const areaTop = ca.getBoundingClientRect().top;
      const areaH = ca.getBoundingClientRect().height;
      let worst = 0, culprit = '', lowest = areaTop;
      Array.from(ca.children).forEach((c) => {
        if (c.classList.contains('page-number')) return;
        const b = c.getBoundingClientRect().bottom;
        const d = b - areaBottom;
        if (d > worst) { worst = d; culprit = (c.textContent || '').trim().slice(0, 70); }
        if (b > lowest) lowest = b;
      });
      const num = p.querySelector('.page-number');
      const printed = num ? num.textContent : '(unnumbered)';
      if (worst > 1) overflow.push({ index: i + 1, printed, template: p.getAttribute('data-template'), clippedPx: Math.round(worst), element: culprit });
      const txt = (ca.textContent || '').trim();
      if (!txt.length && !ca.querySelector('img')) empties.push({ index: i + 1, template: p.getAttribute('data-template') });
      else if (areaH >= 100 && (lowest - areaTop) / areaH < 0.35 && !p.hasAttribute('data-continuation-last')) {
        sparse.push({ index: i + 1, printed, fillPct: Math.round(100 * (lowest - areaTop) / areaH), text: txt.slice(0, 60) });
      }
    });
    const toc = Array.from(document.querySelectorAll('.toc-entry[data-toc-ref]')).map((e) => ({
      text: e.querySelector('.toc-entry-text').textContent, page: e.querySelector('.toc-entry-page').textContent,
    }));
    const unresolved = toc.filter((t) => !t.page || t.page === '000');
    const numbered = pages.filter((p) => p.querySelector('.page-number')).length;
    const katexErrors = document.querySelectorAll('.katex-error').length;
    return { total: pages.length, numbered, overflow, empties, sparse, tocEntries: toc.length, unresolved, katexErrors, toc };
  });

  console.log(JSON.stringify({ totalPages: report.total, numberedPages: report.numbered, tocEntries: report.tocEntries,
    katexErrors: report.katexErrors, overflowPages: report.overflow, emptyPages: report.empties,
    sparsePages: report.sparse, unresolvedTocEntries: report.unresolved }, null, 2));
  fs.writeFileSync(HTML.replace(/\.html$/, '-toc.json'), JSON.stringify(report.toc, null, 2));

  await page.pdf({ path: PDF, width: '8.5in', height: '11in', printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 }, preferCSSPageSize: false });
  await browser.close();
  console.log('PDF written to ' + PDF);
})().catch((e) => { console.error(e); process.exit(1); });
