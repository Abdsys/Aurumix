const puppeteer = require('puppeteer-core');
const path = require('path');
const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.join(__dirname, 'Aurumix_Market_Research_Summary.html');

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 816, height: 1056 });
  page.on('console', (m) => console.log('PAGE:', m.text()));
  page.on('pageerror', (e) => console.log('PAGEERROR:', e.message));
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 120000 });
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 120000 }).catch(() => console.log('!! render-complete never set'));
  const r = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('#document-pages > .page').forEach((p, i) => {
      const ca = p.querySelector('.content-area');
      out.push({
        i: i + 1,
        tpl: p.getAttribute('data-template'),
        cont: p.hasAttribute('data-continuation'),
        done: p.hasAttribute('data-auto-continued'),
        ac: p.hasAttribute('data-auto-continue'),
        clientH: ca ? ca.clientHeight : null,
        scrollH: ca ? ca.scrollHeight : null,
        kids: ca ? ca.children.length : null,
      });
    });
    return out;
  });
  console.table(r.slice(0, 14));
  console.log('total pages', r.length);
  await browser.close();
})();
