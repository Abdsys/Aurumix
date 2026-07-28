const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');
const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const HTML = path.join(__dirname, 'Aurumix_Market_Research_Summary.html');
const OUT = path.join(__dirname, 'shots');

// page indices (1-based, in DOM order) to capture
const WANT = process.argv.slice(2).map(Number);

(async () => {
  if (!fs.existsSync(OUT)) fs.mkdirSync(OUT);
  const b = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  const pg = await b.newPage();
  await pg.setViewport({ width: 816, height: 1056, deviceScaleFactor: 1.4 });
  await pg.goto('file:///' + HTML.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 120000 });
  await pg.waitForFunction(() => document.body.getAttribute('data-render-complete') === '1', { timeout: 120000 });
  await pg.addStyleTag({ content: '@media screen{body{background:#fff;padding:0}#document-pages>.page{box-shadow:none;margin:0 auto}}' });
  const handles = await pg.$$('#document-pages > .page');
  for (const i of WANT) {
    if (!handles[i - 1]) { console.log('no page ' + i); continue; }
    const f = path.join(OUT, 'p' + String(i).padStart(3, '0') + '.png');
    await handles[i - 1].screenshot({ path: f });
    console.log(f);
  }
  await b.close();
})();
