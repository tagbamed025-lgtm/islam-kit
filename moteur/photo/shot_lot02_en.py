import json, asyncio, os
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out_lot02_en")
os.makedirs(OUT, exist_ok=True)

D = json.load(open(os.path.join(HERE, "photos_lot02_en.json"), encoding="utf-8"))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        await pg.goto(f'file://{HERE}/photo.html')
        await pg.evaluate('document.fonts.ready')
        for d in D:
            await pg.evaluate('d=>fill(d)', d)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(OUT, d['f'] + '.png'))
            print('OK', d['f'])
        await b.close()

asyncio.run(main())
