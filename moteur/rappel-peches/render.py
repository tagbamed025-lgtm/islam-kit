import sys, json, asyncio
from playwright.async_api import async_playwright
FPS = 30
tl = json.load(open('timeline.json'))
html = open('index.html').read().replace('__TL__', json.dumps(tl, ensure_ascii=False))
open('page.html', 'w').write(html)
mode = sys.argv[1]  # 'shots' t1,t2,... | 'seg' i n
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file:///home/claude/w/page.html')
        await pg.wait_for_function('window.READY===true')
        if mode == 'shots':
            for t in sys.argv[2].split(','):
                await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'shot_{t}.png')
        else:
            i, n = int(sys.argv[2]), int(sys.argv[3]); tot = int(tl['DUR'] * FPS)
            a, z = tot * i // n, tot * (i + 1) // n
            for f in range(a, z):
                await pg.evaluate(f'render({f / FPS})')
                await pg.screenshot(path=f'frames/f{f:05d}.png')
        await b.close()
asyncio.run(main())
