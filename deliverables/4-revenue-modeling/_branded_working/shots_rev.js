// Screenshot selected pages of an assembled HTML for visual review.
//   node shots_sim.js <input.html> <outdir> <page-index,...>   (1-based, after auto-continue)
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.resolve(process.argv[2]);
const OUT = path.resolve(process.argv[3]);
const PAGES = (process.argv[4] || '1').split(',').map((s) => parseInt(s, 10));
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1 });
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 180000 });
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 180000 });
  await new Promise((r) => setTimeout(r, 1000));
  const els = await page.$$('#document-pages > .page');
  for (const n of PAGES) {
    const el = els[n - 1];
    if (!el) { console.log('no page', n); continue; }
    const file = path.join(OUT, `p${String(n).padStart(2, '0')}.png`);
    await el.screenshot({ path: file });
    console.log('wrote', file);
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
