import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/claude/musab/index.html'); await pg.wait_for_function('window.READY===true')
        print(await pg.evaluate("(()=>{const s=D.shots.find(x=>x.img==='MAP_RS');return [s.el.querySelectorAll('.rt').length, s.el.innerHTML.slice(0,300)]})()"))
        await b.close()
asyncio.run(main())
