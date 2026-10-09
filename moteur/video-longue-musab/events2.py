import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/claude/musab/index.html'); await pg.wait_for_function('window.READY===true')
        ev=await pg.evaluate('''()=>{EV.length=0;for(let f=0;f<Math.ceil(DUR*15);f++)render(f/15);return EV}''')
        json.dump(ev,open('events.json','w'))
        from collections import Counter; print(len(ev),Counter(e[0] for e in ev))
        await b.close()
asyncio.run(main())
