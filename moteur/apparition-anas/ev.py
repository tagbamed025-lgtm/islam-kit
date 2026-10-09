import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/anas/index.html'); await pg.wait_for_function('window.READY===true')
        ev=await pg.evaluate('''()=>{EV.length=0;for(let f=0;f<Math.ceil(DUR*30);f++)render(f/30);return [EV,S.map(s=>s.s),DUR]}''')
        json.dump(ev,open('events.json','w')); from collections import Counter; print(Counter(e[0] for e in ev[0]),len(ev[1]))
        await b.close()
asyncio.run(main())
