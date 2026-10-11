# miniatures 1080x1920 et 1280x720 : python3 thumb.py -> out/<ID>_1080x1920.png, out/<ID>_1280x720.png
import asyncio, json, os
from playwright.async_api import async_playwright
exec(open('cfg.py',encoding='utf-8').read())
here=os.path.dirname(os.path.abspath(__file__))
TH=dict(THUMB); TH['src']=f"img/cut_{TH['img']}.png" if TH.get('cut') else f"img/{TH['img']}.jpg"
open('thumb.html','w',encoding='utf-8').write(open(os.path.join(here,'thumb_tpl.html'),encoding='utf-8').read().replace('__TH__',json.dumps(TH,ensure_ascii=False)))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files']); os.makedirs('out',exist_ok=True)
        for f,w,h in [('v',1080,1920),('h',1280,720)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto('file://'+os.path.abspath('thumb.html')+f'?f={f}'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'out/{ID}_{w}x{h}.png'); await pg.close()
        await b.close()
asyncio.run(main())
