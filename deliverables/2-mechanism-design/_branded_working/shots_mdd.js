// Screenshot sample pages of the assembled document for visual verification.
//   node shots_mdd.js <input.html> <outdir> [pages: 1,2,3 | 'auto']
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.resolve(process.argv[2]);
const OUT = path.resolve(process.argv[3] || 'shots');
const SEL = (process.argv[4] || 'auto');

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', protocolTimeout: 600000,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1.2 });
  await page.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 240000 });
  await page.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 480000, polling: 1000 });
  await new Promise((r) => setTimeout(r, 1500));

  const templates = await page.evaluate(() =>
    Array.from(document.querySelectorAll('#document-pages > .page')).map((p, i) => ({
      i: i + 1, t: p.getAttribute('data-template'), cont: p.hasAttribute('data-continuation'),
      hasFig: !!p.querySelector('.mermaid'),
    })));

  let picks;
  if (SEL === 'auto') {
    picks = new Set();
    const firstOf = {};
    templates.forEach((p) => { if (!firstOf[p.t] && !p.cont) { firstOf[p.t] = p.i; } });
    Object.values(firstOf).forEach((i) => picks.add(i));
    // a few diagram pages and continuations
    templates.filter((p) => p.hasFig).slice(0, 6).forEach((p) => picks.add(p.i));
    const conts = templates.filter((p) => p.cont);
    if (conts.length) { picks.add(conts[0].i); picks.add(conts[Math.floor(conts.length / 2)].i); }
    picks.add(templates.length); // back cover
    picks = Array.from(picks).sort((a, b) => a - b);
  } else {
    picks = SEL.split(',').map(Number);
  }

  for (const n of picks) {
    const el = await page.$(`#document-pages > .page:nth-child(${n})`);
    if (!el) continue;
    await el.screenshot({ path: path.join(OUT, `page-${String(n).padStart(3, '0')}.png`) });
  }
  console.log('shots:', picks.join(','));
  await browser.close();
})();
