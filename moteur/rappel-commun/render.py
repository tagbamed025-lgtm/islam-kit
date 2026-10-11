# usage : python3 render.py <dossier> shots t1,t2,…  |  python3 render.py <dossier> seg i n
import sys, json, asyncio, os
from playwright.async_api import async_playwright
FPS = 30
W = os.path.abspath(sys.argv[1]); mode = sys.argv[2]
tl = json.load(open(W + '/timeline.json'))
html = open(os.path.dirname(os.path.abspath(__file__)) + '/index.html').read().replace('__TL__', json.dumps(tl, ensure_ascii=False))
open(W + '/page.html', 'w').write(html)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + W + '/page.html')
        await pg.wait_for_function('window.READY===true', timeout=60000)
        if mode == 'shots':
            for t in sys.argv[3].split(','):
                await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'{W}/shot_{t}.png')
        else:
            i, n = int(sys.argv[3]), int(sys.argv[4]); tot = int(tl['DUR'] * FPS)
            os.makedirs(W + '/frames', exist_ok=True)
            for f in range(tot * i // n, tot * (i + 1) // n):
                await pg.evaluate(f'render({f / FPS})')
                await pg.screenshot(path=f'{W}/frames/f{f:05d}.jpg', type='jpeg', quality=93)
        await b.close()
asyncio.run(main())
