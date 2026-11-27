// node render.cjs  -> renders every NN-*.html in this folder to NN-*.png (1080x1350)
const { chromium } = require('playwright'), fs = require('fs'), path = require('path');
(async () => { const b = await chromium.launch(), p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const f of fs.readdirSync(__dirname).filter(f => /^\d\d-.*\.html$/.test(f))) {
    await p.goto('file://' + path.join(__dirname, f)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await (await p.$('#post')).screenshot({ path: path.join(__dirname, f.replace('.html', '.png')) }); console.log(f); }
  await b.close(); })();
