import sys, asyncio, subprocess, math
from playwright.async_api import async_playwright
FPS=30; t0=float(sys.argv[1]); t1=float(sys.argv[2]); out=sys.argv[3]
async def main():
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        br=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/lampe/index.html'); await pg.wait_for_function('window.READY===true'); await pg.wait_for_timeout(1500)
        f0=round(t0*FPS); f1=round(t1*FPS)
        for f in range(f0,f1):
            await pg.evaluate(f'render({f/FPS})')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=93))
        await br.close()
    ff.stdin.close(); ff.wait()
asyncio.run(main())
