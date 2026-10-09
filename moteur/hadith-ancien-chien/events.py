import asyncio, json, math
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/reel_chien/index.html'); await pg.evaluate('document.fonts.ready')
        ev=await pg.evaluate('''()=>{EV.length=0;for(let f=0;f<Math.ceil(DUR*30);f++)render(f/30);return EV}''')
        json.dump(ev,open('events.json','w')); 
        from collections import Counter; print(len(ev),Counter(e[0] for e in ev))
        await b.close()
asyncio.run(main())
