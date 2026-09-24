const puppeteer = require('puppeteer-core'); const path = require('path');
(async () => {
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new' });
  const p = await b.newPage(); p.on('console', m => console.error('[c]', m.text().slice(0,300))); p.on('pageerror', e => console.error('[e]', String(e).slice(0,300))); await p.setViewport({ width: 2100, height: 1000 });
  await p.goto(require('url').pathToFileURL(path.resolve(__dirname, 'probe.html')).href, { waitUntil: 'networkidle0' });
  await p.waitForFunction(() => document.body.getAttribute('data-out'), { timeout: 120000 });
  console.log(await p.evaluate(() => document.body.getAttribute('data-out'))); await b.close();
})();
