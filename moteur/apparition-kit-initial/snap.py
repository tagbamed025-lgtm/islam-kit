import sys, asyncio
from playwright.async_api import async_playwright
ts=[float(x) for x in sys.argv[1].split(',')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        msgs=[]; pg.on('console',lambda m:msgs.append(m.text)); pg.on('pageerror',lambda e:msgs.append('ERR '+str(e)))
        await pg.goto('file://'+__import__('os').path.abspath('index.html')+''); await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(500)
        for t in ts:
            await pg.evaluate(f'render({t})')
            await pg.screenshot(path=f'/tmp/claude-0/n_{t:05.2f}.jpg',type='jpeg',quality=70)
        print('\n'.join(msgs[:10]))
        await b.close()
asyncio.run(main())
