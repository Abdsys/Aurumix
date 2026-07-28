const puppeteer = require('puppeteer-core');
const path = require('path');
const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.join(__dirname, 'Aurumix_Market_Research_Summary.html');

(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  const pg = await b.newPage();
  await pg.setViewport({ width: 816, height: 1056 });
  await pg.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 120000 });
  await pg.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 120000 });
  const r = await pg.evaluate(() => {
    const o = [];
    document.querySelectorAll('#document-pages > .page--special-table-of-contents').forEach((x, i) => {
      const ca = x.querySelector('.content-area');
      const e = ca.querySelector('.toc-entry');
      o.push({
        page: i + 1,
        entries: ca.querySelectorAll('.toc-entry').length,
        kids: ca.children.length,
        clientH: ca.clientHeight,
        entryH: e ? Math.round(e.getBoundingClientRect().height) : 0,
      });
    });
    return o;
  });
  console.log(JSON.stringify(r, null, 1));
  await b.close();
})();
