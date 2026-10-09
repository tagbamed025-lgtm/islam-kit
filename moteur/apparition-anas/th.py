import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        for f,w,h in [('v',1080,1920),('h',1280,720)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto(f'file:///home/claude/anas/thumb.html?f={f}'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'Miniature_Anas_{w}x{h}.png'); await pg.close()
        await b.close()
asyncio.run(main())
