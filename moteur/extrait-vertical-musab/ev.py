import asyncio, json, sys
from playwright.async_api import async_playwright
async def main():
    d=sys.argv[1]
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto(f'file:///home/claude/musab_reels/{d}/index.html'); await pg.wait_for_function('window.READY===true')
        ev=await pg.evaluate('''()=>{EV.length=0;for(let f=0;f<Math.ceil(DUR*15);f++)render(f/15);return EV}''')
        json.dump(ev,open(f'{d}/events.json','w')); print(len(ev))
        await b.close()
asyncio.run(main())
