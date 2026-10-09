import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        pg.on('console',lambda m:print('CONSOLE',m.text)); pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file:///home/claude/musab/index.html'); await pg.wait_for_function('window.READY===true',timeout=60000)
        for t in sys.argv[1:]:
            await pg.evaluate(f'render({t})'); await pg.wait_for_timeout(120); await pg.screenshot(path=f'sn/s_{t}.jpg',type='jpeg',quality=80)
        await b.close()
asyncio.run(main())
