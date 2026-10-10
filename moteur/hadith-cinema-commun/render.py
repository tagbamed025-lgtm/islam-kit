# usage: python3 render.py part parts   (ou: python3 render.py ev  -> events.json ; python3 render.py snap t1 t2 ...)
import sys, asyncio, subprocess, math, json, os
from playwright.async_api import async_playwright
FPS=30; URL='file://'+os.path.abspath('index.html')
async def page(p):
    br=await p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=await br.new_page(viewport={'width':1080,'height':1920}); await pg.goto(URL); await pg.evaluate('window.READY'); await pg.wait_for_timeout(500)
    return br,pg
async def main():
    async with async_playwright() as p:
        br,pg=await page(p); DUR=await pg.evaluate('DUR'); N=math.ceil(DUR*FPS)
        if sys.argv[1]=='ev':
            ev=await pg.evaluate(f'()=>{{EV.length=0;for(let f=0;f<{N};f++)render(f/{FPS});return EV}}'); json.dump(ev,open('events.json','w')); print('events',len(ev))
        elif sys.argv[1]=='snap':
            os.makedirs('snaps',exist_ok=True)
            for t in sys.argv[2:]:
                await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'snaps/{float(t):07.2f}.jpg',type='jpeg',quality=80)
        else:
            part,parts=int(sys.argv[1]),int(sys.argv[2]); a=N*part//parts; b=N*(part+1)//parts
            ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',f'part{part}.mp4'],stdin=subprocess.PIPE)
            for f in range(a,b):
                await pg.evaluate(f'render({f/FPS})'); ff.stdin.write(await pg.screenshot(type='jpeg',quality=93))
            ff.stdin.close(); ff.wait()
        await br.close()
asyncio.run(main())
