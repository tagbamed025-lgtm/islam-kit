# Miniature 1080×1920 : fond émeraude + arche, objet du Rappel, 3 lignes (cfg.THUMB). usage : thumb.py <dossier>
import sys, asyncio, importlib.util, os
from playwright.async_api import async_playwright
W = os.path.abspath(sys.argv[1])
sp = importlib.util.spec_from_file_location('cfg', W + '/cfg.py'); C = importlib.util.module_from_spec(sp); sp.loader.exec_module(C); T = C.THUMB
CSS = """@font-face{font-family:Anton;src:url(fonts/anton-latin-400-normal.woff2)}
@font-face{font-family:Anton;src:url(fonts/anton-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Inter;font-weight:800;src:url(fonts/inter-latin-800-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#06291F;overflow:hidden}
.s{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 40%,#13684F 0%,#0B4636 55%,#06291F 100%)}
.g{position:absolute;inset:0;background:url(img/grain.png);background-size:600px;opacity:.2;mix-blend-mode:overlay}
.a{position:absolute;left:0;right:0;font-family:Anton;text-transform:uppercase;color:#FBF6EA;line-height:1;text-align:center;text-shadow:0 8px 30px rgba(0,0,0,.45);white-space:nowrap}
.b{display:inline-block;background:#0F5B46;color:#EDCB85;outline:3px solid rgba(237,203,133,.7);padding:.08em .3em .02em;transform:rotate(-2deg);box-shadow:0 18px 50px rgba(0,0,0,.65)}
.t{position:absolute;left:50%;top:250px;transform:translateX(-50%);font-family:Inter;font-weight:800;letter-spacing:.3em;font-size:30px;padding:16px 30px;color:#EDCB85;border:2px solid rgba(237,203,133,.6)}
.halo{position:absolute;left:90px;top:330px;width:900px;height:900px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,214,140,.5),rgba(255,200,120,0))}
#ob{position:absolute;left:50%;transform:translateX(-50%);top:420px;max-width:640px;max-height:640px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.5))}"""
H = f"""<style>{CSS}</style><div class="s">
<svg width="1080" height="1920" style="position:absolute"><path d="M110 1820 L110 640 Q110 330 540 170 Q970 330 970 640 L970 1820" fill="none" stroke="#EDCB85" stroke-width="4" opacity=".75"/></svg>
<div class="halo"></div><img id="ob" src="img/cut_{T['obj']}.png">
<div class="t">RAPPEL</div>
<div class="a" id="l1" style="top:1150px;font-size:210px"><span>{T['l1']}</span></div>
<div class="a" id="l2" style="top:1400px;font-size:140px"><span class="b">{T['l2']}</span></div>
<div class="a" id="l3" style="top:1640px;font-size:66px;color:#EDCB85"><span>{T['l3']}</span></div>
<img src="img/logo.png" style="position:absolute;left:480px;top:1760px;width:120px;opacity:.9"><div class="g"></div></div>
<script>for(const [id,m] of [['l1',960],['l2',960],['l3',900]]){{const e=document.getElementById(id);let f=parseFloat(e.style.fontSize);const w=()=>e.firstChild.getBoundingClientRect().width;while(w()>m&&f>40){{f-=4;e.style.fontSize=f+'px';}}}}</script>"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        open(W + '/t_v.html', 'w').write(H)
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920}); await pg.goto('file://' + W + '/t_v.html')
        await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500); await pg.screenshot(path=W + '/thumb_v.png')
        await b.close()
asyncio.run(main())
