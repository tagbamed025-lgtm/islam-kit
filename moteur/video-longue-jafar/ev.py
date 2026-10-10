import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/claude/travail/VID-04-jafar/index.html'); await pg.wait_for_function('window.READY===true')
        ev=await pg.evaluate('(()=>{for(let f=0;f<DUR*30;f++)render(f/30);return EV})()')
        json.dump(ev,open('events.json','w')); print(len(ev))
        await br.close()
asyncio.run(main())
