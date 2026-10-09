import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        pg.on('pageerror',lambda e:print('ERR',e))
        await pg.goto('file:///home/claude/lampe/index.html'); await pg.wait_for_function('window.READY===true',timeout=60000)
        for t in sys.argv[1:]:
            await pg.evaluate(f'render({t})'); await pg.wait_for_timeout(80); await pg.screenshot(path=f'sn_{t}.jpg',type='jpeg',quality=80)
        await b.close()
asyncio.run(main())
