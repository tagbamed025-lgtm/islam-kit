import sys, asyncio
from playwright.async_api import async_playwright
ts=[float(x) for x in sys.argv[1].split(',')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        msgs=[]; pg.on('pageerror',lambda e:msgs.append('ERR '+str(e)))
        await pg.goto('file:///home/claude/reel_natte2/index.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(700)
        for t in ts:
            await pg.evaluate(f'render({t})')
            await pg.screenshot(path=f'/tmp/claude-0/s2_{t:05.2f}.jpg',type='jpeg',quality=80)
        print('\n'.join(msgs))
        await b.close()
asyncio.run(main())
