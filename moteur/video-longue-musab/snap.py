import sys, asyncio
from playwright.async_api import async_playwright
times = [float(x) for x in sys.argv[1:]]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/claude/musab/index.html')
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(300)
        for t in times:
            await pg.evaluate(f'render({t})')
            await pg.screenshot(path=f'snap_{t}.png')
        await b.close()
asyncio.run(main())
