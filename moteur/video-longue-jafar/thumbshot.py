import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        for f,w,h,n in [('v',1080,1920,'Miniature_Jafar_1080x1920.png'),('h',1280,720,'Miniature_Jafar_1280x720.png')]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto(f'file:///home/claude/travail/VID-04-jafar/thumb.html?f={f}'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
            await pg.screenshot(path=n); await pg.close()
        await b.close()
asyncio.run(main())
