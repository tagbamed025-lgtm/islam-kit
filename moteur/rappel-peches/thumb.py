import asyncio
from playwright.async_api import async_playwright
CSS="""@font-face{font-family:Anton;src:url(fonts/anton-latin-400-normal.woff2)}
@font-face{font-family:Anton;src:url(fonts/anton-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Inter;font-weight:800;src:url(fonts/inter-latin-800-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#F4F1EA;overflow:hidden}
.s{position:relative;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 45%,#13684F 0%,#0B4636 55%,#06291F 100%)}
.g{position:absolute;inset:0;background:url(img/grain.png);background-size:600px;opacity:.2;mix-blend-mode:overlay}
.a{font-family:Anton;text-transform:uppercase;color:#FBF6EA;line-height:1;text-align:center;text-shadow:0 8px 30px rgba(0,0,0,.4)}
.b{display:inline-block;background:#0F5B46;color:#EDCB85;outline:3px solid rgba(237,203,133,.7);padding:.08em .3em .02em;transform:rotate(-2deg);box-shadow:0 18px 50px rgba(0,0,0,.65)}
.t{position:absolute;font-family:Inter;font-weight:800;letter-spacing:.3em;color:#EDCB85;border:2px solid rgba(237,203,133,.6);white-space:nowrap}
img.l{position:absolute;opacity:.9}"""
V=f"""<style>{CSS}</style><div class="s" style="width:1080px;height:1920px">
<svg width="1080" height="1920" style="position:absolute"><path d="M120 1640 L120 820 Q120 470 540 300 Q960 470 960 820 L960 1640" fill="none" stroke="#EDCB85" stroke-width="4" opacity=".8"/></svg>
<div class="t" style="left:50%;top:470px;transform:translateX(-50%);font-size:30px;padding:16px 30px">RAPPEL</div>
<div class="a" style="position:absolute;left:0;right:0;top:700px;font-size:250px">PERSONNE</div>
<div class="a" style="position:absolute;left:0;right:0;top:990px;font-size:150px"><span class="b">N'EST À L'ABRI</span></div>
<div class="a" style="position:absolute;left:0;right:0;top:1240px;font-size:70px;color:#EDCB85">DES PÉCHÉS</div>
<img class="l" src="img/logo.png" style="left:470px;top:1700px;width:140px"><div class="g"></div></div>"""
H=f"""<style>{CSS}</style><div class="s" style="width:1280px;height:720px">
<svg width="1280" height="720" style="position:absolute"><path d="M760 760 L760 330 Q760 120 1000 40 Q1240 120 1240 330 L1240 760" fill="none" stroke="#EDCB85" stroke-width="3" opacity=".7"/></svg>
<div class="t" style="left:70px;top:70px;font-size:22px;padding:12px 22px">RAPPEL</div>
<div class="a" style="position:absolute;left:60px;top:170px;font-size:190px;text-align:left">PERSONNE</div>
<div class="a" style="position:absolute;left:60px;top:390px;font-size:110px;text-align:left"><span class="b">N'EST À L'ABRI</span></div>
<img class="l" src="img/logo.png" style="left:930px;top:300px;width:140px"><div class="g"></div></div>"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,html,w,h in [('v',V,1080,1920),('h',H,1280,720)]:
            open(f't_{name}.html','w').write(html)
            pg=await b.new_page(viewport={'width':w,'height':h});await pg.goto(f'file:///home/claude/w/t_{name}.html')
            await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(300);await pg.screenshot(path=f'thumb_{name}.png')
        await b.close()
asyncio.run(main())
