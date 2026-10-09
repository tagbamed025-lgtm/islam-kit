import sys, asyncio, subprocess, math
from playwright.async_api import async_playwright
FPS=30
t0=float(sys.argv[1]); t1=float(sys.argv[2]); out=sys.argv[3]
N=math.ceil((t1-t0)*FPS)
async def main():
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        br=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///home/claude/musab/index.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
        for f in range(N):
            t=t0+f/FPS
            await pg.evaluate(f'render({t})')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
            if f%150==0: print(f, t, flush=True)
        await br.close()
    ff.stdin.close(); ff.wait()
asyncio.run(main())
