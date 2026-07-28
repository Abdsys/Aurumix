// Render the assembled HTML to PDF, and report any page whose content
// overflows its box (which is what produces clipped or overlapping text).
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.join(__dirname, 'Aurumix_Market_Research_Summary.html');
const PDF = process.argv[2] || path.join(__dirname, 'Aurumix_Market_Research_Summary.pdf');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1 });
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 120000 });

  // wait for the auto-continuation pass to finish
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 120000 });
  await new Promise((r) => setTimeout(r, 1500));

  const report = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll('#document-pages > .page'));
    const overflow = [];
    pages.forEach((p, i) => {
      const ca = p.querySelector('.content-area');
      if (!ca) return;
      // Measure real element bottoms, not scrollHeight: a trailing margin
      // inflates scrollHeight without any text actually being clipped.
      const areaBottom = ca.getBoundingClientRect().bottom;
      let worst = 0;
      let culprit = '';
      Array.from(ca.children).forEach((c) => {
        if (c.classList.contains('page-number')) return;
        const d = c.getBoundingClientRect().bottom - areaBottom;
        if (d > worst) { worst = d; culprit = (c.textContent || '').trim().slice(0, 70); }
      });
      // also catch text spilling past the page box itself
      const pageBottom = p.getBoundingClientRect().bottom;
      const pastPage = ca.getBoundingClientRect().bottom - pageBottom;
      if (worst > 1) {
        const num = p.querySelector('.page-number');
        overflow.push({
          index: i + 1,
          printed: num ? num.textContent : '(unnumbered)',
          template: p.getAttribute('data-template'),
          clippedPx: Math.round(worst),
          pastPagePx: Math.round(pastPage),
          element: culprit,
        });
      }
    });
    // empty pages are a sign the splitter produced a stray continuation
    const empties = [];
    pages.forEach((p, i) => {
      const ca = p.querySelector('.content-area');
      if (ca && (ca.textContent || '').trim().length === 0) {
        empties.push({ index: i + 1, template: p.getAttribute('data-template') });
      }
    });
    const toc = Array.from(document.querySelectorAll('.toc-entry[data-toc-ref]')).map((e) => ({
      text: e.querySelector('.toc-entry-text').textContent,
      page: e.querySelector('.toc-entry-page').textContent,
    }));
    const unresolved = toc.filter((t) => !t.page);
    const numbered = pages.filter((p) => p.querySelector('.page-number')).length;
    return { total: pages.length, numbered, overflow, empties, tocEntries: toc.length, unresolved, toc };
  });

  console.log(JSON.stringify({
    totalPages: report.total,
    numberedPages: report.numbered,
    tocEntries: report.tocEntries,
    overflowPages: report.overflow,
    emptyPages: report.empties,
    unresolvedTocEntries: report.unresolved,
  }, null, 2));

  fs.writeFileSync(path.join(__dirname, 'toc-dump.json'), JSON.stringify(report.toc, null, 2));

  await page.pdf({
    path: PDF,
    width: '8.5in',
    height: '11in',
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    preferCSSPageSize: false,
  });

  await browser.close();
  console.log('PDF written to ' + PDF);
})().catch((e) => { console.error(e); process.exit(1); });
