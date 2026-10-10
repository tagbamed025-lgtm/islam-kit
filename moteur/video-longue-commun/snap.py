import sys, asyncio
from playwright.async_api import async_playwright
ts=[float(x) for x in sys.argv[1].split(',')]
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file://'+__import__('os').getcwd()+'/index.html'); await pg.wait_for_function('window.READY===true'); await pg.wait_for_function('[...document.images].every(i=>i.complete&&i.naturalWidth>0)',timeout=120000); await pg.wait_for_timeout(800)
        for t in ts:
            await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'snaps/s_{t:07.2f}.jpg',type='jpeg',quality=80)
        await br.close()
asyncio.run(main())
