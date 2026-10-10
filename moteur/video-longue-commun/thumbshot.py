import asyncio, os, sys
from playwright.async_api import async_playwright
ID=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        for f,w,h in [('v',1080,1920),('h',1280,720)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto('file://'+os.getcwd()+'/thumb.html?f='+f); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
            await pg.screenshot(path=f'Miniature_{ID}_{w}x{h}.png'); await pg.close()
        await b.close()
asyncio.run(main())
