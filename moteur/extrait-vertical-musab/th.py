import asyncio, urllib.parse as U
from playwright.async_api import async_playwright
JOBS=[('r1','M01_bedouin_cloak','LE PLUS RICHE/DE LA MECQUE…','SANS LINCEUL.',"MUS'AB IBN UMAYR",'50%'),
      ('r2','M15_clan_chief_spear','FURIEUX,/LANCE À LA MAIN…',"PUIS IL S'ASSOIT.","MUS'AB IBN UMAYR",'35%')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        for d,img,l1,l2,tag,ox in JOBS:
            for f,w,h in [('v',1080,1920),('h',1280,720)]:
                pg=await b.new_page(viewport={'width':w,'height':h})
                q=U.urlencode({'f':f,'img':img,'l1':l1,'l2':l2,'tag':tag,'ox':ox})
                await pg.goto(f'file:///home/claude/musab_reels/{d}/thumb.html?{q}'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(700)
                await pg.screenshot(path=f'{d}/Miniature_{d}_{w}x{h}.png'); await pg.close()
        await b.close()
asyncio.run(main())
