# miniature 1080x1920 (reel) : python3 thumb.py  -> out/<ID>_1080x1920.png
import asyncio, os
exec(open('cfg.py', encoding='utf-8').read())
H = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Anton;src:url(node_modules/@fontsource/anton/files/anton-latin-400-normal.woff2)}}
@font-face{{font-family:Anton;src:url(node_modules/@fontsource/anton/files/anton-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}}
@font-face{{font-family:Inter;font-weight:800;src:url(node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;background:#0b0906}}
.t{{font-family:Anton;text-transform:uppercase;line-height:1;white-space:nowrap;text-align:center}}
</style></head><body>
<img src="hd/{THUMB['img']}.jpg" style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;object-position:{THUMB.get('pos','50% 50%')};filter:contrast(1.1) brightness(.9)">
<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(11,9,6,.65) 0%,rgba(11,9,6,0) 16%,rgba(11,9,6,0) 48%,rgba(11,9,6,.85) 68%,#0b0906 100%)"></div>
<div style="position:absolute;left:50%;top:110px;transform:translateX(-50%);font-family:Inter;font-weight:800;font-size:30px;letter-spacing:.24em;color:#FBF6EA;background:#0F5B46;padding:.45em .9em;white-space:nowrap">HADITHS · {TAG}</div>
<div id="l1" class="t" style="position:absolute;left:0;right:0;top:1290px;font-size:150px;color:#FBF8F0;text-shadow:0 6px 24px rgba(0,0,0,.6)">{THUMB['L1']}</div>
<div style="position:absolute;left:-40px;right:-40px;top:1500px;padding:30px 0 16px;background:#0F5B46;transform:rotate(-3deg);box-shadow:0 18px 40px rgba(0,0,0,.45)"><div id="l2" class="t" style="font-size:140px;color:#EDCB85">{THUMB['L2']}</div></div>
<img src="img/logo.png" style="position:absolute;left:50%;transform:translateX(-50%);bottom:70px;width:110px">
<div style="position:absolute;inset:0;background:url(img/grain.png);background-size:600px;opacity:.3;mix-blend-mode:overlay"></div>
<script>for(const id of ['l1','l2']){{const e=document.getElementById(id);let f=parseInt(e.style.fontSize);const r=()=>{{const g=document.createRange();g.selectNodeContents(e);return g.getBoundingClientRect().width}};while(r()>1000&&f>40){{f-=2;e.style.fontSize=f+'px';}}}}</script>
</body></html>'''
open('thumb.html', 'w', encoding='utf-8').write(H)
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files']); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + os.path.abspath('thumb.html')); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(600)
        os.makedirs('out', exist_ok=True); await pg.screenshot(path=f'out/{ID}_1080x1920.png'); await b.close()
asyncio.run(main()); print('miniature ok')
