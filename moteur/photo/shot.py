import json,asyncio
from playwright.async_api import async_playwright
D=json.load(open('photos.json'))
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=await b.new_page(viewport={'width':1080,'height':1350})
    await pg.goto('file:///home/claude/photos/photo.html');await pg.evaluate('document.fonts.ready')
    for d in D:
      await pg.evaluate('d=>fill(d)',d);await pg.wait_for_timeout(300)
      await pg.screenshot(path=d['f']+'.png')
    await b.close()
asyncio.run(main())
