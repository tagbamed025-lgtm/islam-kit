import sys, asyncio, subprocess, math
from playwright.async_api import async_playwright
FPS=30; DUR=76.6; N=math.ceil(DUR*FPS)
part,parts=int(sys.argv[1]),int(sys.argv[2])
a=N*part//parts; b=N*(part+1)//parts
async def main():
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p',f'part{part}.mp4'],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        br=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/khalid/index.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
        for f in range(a,b):
            await pg.evaluate(f'render({f/FPS})')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=94))
            if f%150==0: print(part,f,flush=True)
        await br.close()
    ff.stdin.close(); ff.wait()
asyncio.run(main())
