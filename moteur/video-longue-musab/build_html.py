import json

shots = json.load(open('shots.json'))
lines = json.load(open('align_lines.json'))
DUR = lines[-1][-1][2]

chapters = [
 [13.66, "LE PRINCE DE LA MECQUE"],
 [40.16, "LE SECRET"],
 [61.06, "LE PRIX"],
 [88.18, "LE PREMIER AMBASSADEUR"],
 [158.72, "UHUD"],
 [171.10, "LE MANTEAU TROP COURT"],
 [197.90, "LA LEÇON"],
]

html = """<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{font-family:AnimN;src:url(node_modules/@fontsource/anton/files/anton-latin-400-normal.woff2)}
@font-face{font-family:AnimN;src:url(node_modules/@fontsource/anton/files/anton-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Cormo;font-style:italic;font-weight:600;src:url(node_modules/@fontsource/cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2)}
@font-face{font-family:Inter;font-weight:800;src:url(node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000}
.c{position:relative;overflow:hidden;width:1920px;height:1080px;background:#000}
img.bg{position:absolute;top:0;left:0;width:1920px;height:1080px;object-fit:cover;will-change:transform}
.dark{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(8,10,6,.05) 0%,rgba(8,10,6,.18) 55%,rgba(8,10,6,.72) 100%)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 45%,rgba(5,10,8,.55) 100%)}
.grain{position:absolute;inset:0;background:url(img/grain.png);background-size:600px;opacity:.22;mix-blend-mode:overlay}
.logo{position:absolute;right:52px;top:46px;width:78px;opacity:.92}
.cap{position:absolute;left:130px;right:130px;bottom:130px;font-family:AnimN;text-transform:uppercase;font-size:58px;line-height:1.18;color:#FBF8F0;text-shadow:0 6px 22px rgba(0,0,0,.55)}
.cap .w{opacity:.28;transition:none}
.cap .w.on{opacity:1;color:#F6E4B8}
.quoteband{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(180deg,rgba(15,91,70,0) 0%,rgba(12,60,46,.94) 30%,rgba(9,42,32,.97) 100%);padding:56px 150px 74px}
.quoteband .cap{position:static;font-family:Cormo;font-style:italic;text-transform:none;font-size:52px;color:#F6E4B8;text-shadow:none;left:auto;right:auto;bottom:auto}
.quoteband .cap .w.on{color:#FFFFFF}
.tag{position:absolute;left:130px;top:70px;font-family:Inter;font-weight:800;letter-spacing:.22em;font-size:26px;color:#F6E4B8;background:rgba(6,26,20,.55);padding:.5em 1em;border:1px solid rgba(237,203,133,.5)}
.chapter{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;background:rgba(4,18,14,.001)}
.chapter .bg2{position:absolute;inset:0;background:radial-gradient(ellipse 90% 70% at 50% 45%,rgba(15,91,70,.55) 0%,rgba(6,30,23,.85) 60%,rgba(3,15,11,.95) 100%)}
.chapter .txt{position:relative;font-family:AnimN;text-transform:uppercase;font-size:104px;color:#FBF6EA;text-align:center;text-shadow:0 8px 30px rgba(0,0,0,.5);padding:0 120px}
.chapter .line{position:relative;margin-top:34px;height:3px;background:#EDCB85}
svg{position:absolute;left:0;top:0}
.mgwrap{position:absolute;inset:0;background:radial-gradient(ellipse 90% 75% at 50% 40%,#1a8a69 0%,#0f5b46 42%,#093a2d 75%,#05241b 100%)}
</style></head><body><div class="c" id="c"></div>
<script>
const SHOTS=__SHOTS__;
const LINES=__LINES__;
const CHAPTERS=__CHAPTERS__;
const DUR=__DUR__;
const c=document.getElementById('c');
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function findShot(t){for(const s of SHOTS){if(t>=s.start&&t<s.end)return s}return SHOTS[SHOTS.length-1]}
function findLine(t){for(const L of LINES){if(t>=L[0][1]-0.02&&t<=L[L.length-1][2]+0.35)return L}return null}
function kbTransform(shot,t){
  const p=Math.min(1,Math.max(0,(t-shot.start)/(shot.end-shot.start)));
  let scale=1.1,tx=0,ty=0;
  if(shot.kb==='zoomin'){scale=1.0+0.14*p}
  else if(shot.kb==='zoomout'){scale=1.14-0.14*p}
  else if(shot.kb==='pan-l'){scale=1.1;tx=(3-6*p)}
  else if(shot.kb==='pan-r'){scale=1.1;tx=(-3+6*p)}
  return `translate(${tx}%,${ty}%) scale(${scale})`;
}
function captionHTML(t,quoteMode){
  const L=findLine(t); if(!L) return '';
  const words=L.map(([w,s,e])=>{
    const on = t>=s-0.03;
    return `<span class="w${on?' on':''}">${esc(w)}</span>`;
  }).join(' ');
  const isQuote = L[0][0].startsWith('«') || L.map(x=>x[0]).join(' ').includes('«');
  if(quoteMode===undefined) quoteMode = isQuote;
  return {html:words, quote:isQuote};
}
function motionScene(name,p){
  // p = progress 0..1 within the motion shot
  if(name==='title_card'){
    return `<div class="mgwrap"></div>
    <svg width="1920" height="1080"><line x1="${960-500*Math.min(1,p*2)}" y1="540" x2="${960+500*Math.min(1,p*2)}" y2="540" stroke="#EDCB85" stroke-width="3" opacity="${Math.min(1,p*2)}"/></svg>
    <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
      <div style="font-family:AnimN;color:#FBF6EA;font-size:96px;text-transform:uppercase;text-shadow:0 8px 30px rgba(0,0,0,.5);opacity:${Math.min(1,p*3)}">L'AN 3 DE L'HÉGIRE</div>
    </div>`;
  }
  if(name==='banner_handoff'){
    const h=120+260*Math.min(1,p*1.4);
    const ring=8+2*Math.sin(p*10);
    let dots='';
    for(let i=0;i<10;i++){const a=i/10*Math.PI*2;const r=210+ring;const x=960+Math.cos(a)*r;const y=650+Math.sin(a)*r*0.35;
      dots+=`<circle cx="${x}" cy="${y}" r="10" fill="#F6E4B8" opacity="0.85"/>`}
    return `<div class="mgwrap"></div>
    <svg width="1920" height="1080">
      <ellipse cx="960" cy="760" rx="260" ry="40" fill="rgba(5,20,15,.5)"/>
      ${dots}
      <rect x="948" y="${660-h}" width="24" height="${h}" fill="#0b2b21" stroke="#EDCB85" stroke-width="3"/>
      <rect x="972" y="${660-h}" width="${110*Math.min(1,p*1.6)}" height="${Math.min(1,p*1.6)*120}" fill="#153f30" stroke="#EDCB85" stroke-width="2" opacity="${Math.min(1,p*1.6)}"/>
    </svg>`;
  }
  if(name==='troops_clash'){
    let markers='';
    const spread=Math.min(1,p*1.2);
    for(let i=0;i<7;i++){
      const y=380+i*45;
      const lx=140+spread*(760-140*spread);
      const rx=1920-140-spread*(760-140*spread);
      markers+=`<polygon points="${lx},${y} ${lx-22},${y+34} ${lx+22},${y+34}" fill="#0f5b46" stroke="#EDCB85" stroke-width="1.5"/>`;
      markers+=`<polygon points="${rx},${y} ${rx-22},${y+34} ${rx+22},${y+34}" fill="#5b4a2f" stroke="#EDCB85" stroke-width="1.5"/>`;
    }
    let dust='';
    for(let i=0;i<26;i++){
      const seed=i*137.7;
      const dx=960+Math.sin(seed)*420*spread;
      const dy=520+Math.cos(seed*1.3)*160;
      const r=14+ (i%5)*6*spread;
      dust+=`<circle cx="${dx}" cy="${dy}" r="${r}" fill="#c9a86a" opacity="${0.10+0.10*spread}"/>`;
    }
    return `<div class="mgwrap"></div><svg width="1920" height="1080">
      <line x1="0" y1="700" x2="1920" y2="700" stroke="rgba(237,203,133,.25)" stroke-width="2"/>
      ${dust}${markers}
    </svg>`;
  }
  if(name==='banner_falls'){
    const ang=p*72;
    const dark=Math.min(.55,p*.6);
    return `<div class="mgwrap"></div>
    <svg width="1920" height="1080">
      <g transform="translate(960,660) rotate(${ang})">
        <rect x="-12" y="-260" width="24" height="260" fill="#0b2b21" stroke="#EDCB85" stroke-width="3"/>
        <rect x="12" y="-260" width="100" height="110" fill="#153f30" stroke="#EDCB85" stroke-width="2"/>
      </g>
      <ellipse cx="960" cy="760" rx="${260+260*p}" ry="${40+30*p}" fill="rgba(5,20,15,.55)"/>
    </svg>
    <div style="position:absolute;inset:0;background:rgba(2,10,7,${dark})"></div>`;
  }
  return '';
}
function render(t){
  const shot=findShot(t);
  const chap=CHAPTERS.find(ch=>t>=ch[0]&&t<ch[0]+1.35);
  let body='';
  if(shot.type==='photo'){
    const tr=kbTransform(shot,t);
    body+=`<img class="bg" src="img/${shot.img}.png" style="transform:${tr}">`;
    body+='<div class="dark"></div><div class="vig"></div>';
  } else {
    const p=Math.min(1,Math.max(0,(t-shot.start)/(shot.end-shot.start)));
    body+=motionScene(shot.name,p);
  }
  body+='<div class="grain"></div>';
  body+='<div class="tag">SABIL NOUR · COMPAGNONS</div>';
  body+='<img class="logo" src="img/logo.png">';
  const chapOpNow = chap ? Math.min(Math.min(1,(t-chap[0])/0.35), (chap[0]+1.35-t < 0.35 ? Math.max(0,(chap[0]+1.35-t)/0.35) : 1)) : 0;
  const cap=chapOpNow>0.5 ? null : captionHTML(t);
  if(cap && cap.html){
    if(cap.quote){
      body+=`<div class="quoteband"><div class="cap">${cap.html}</div></div>`;
    } else {
      body+=`<div class="cap">${cap.html}</div>`;
    }
  }
  if(chap){
    const p=Math.min(1,(t-chap[0])/0.35);
    const fadeOut = chap[0]+1.35-t < 0.35 ? Math.max(0,(chap[0]+1.35-t)/0.35) : 1;
    const op=Math.min(p,fadeOut);
    body+=`<div class="chapter" style="opacity:${op}"><div class="bg2"></div><div class="txt">${esc(chap[1])}</div><div class="line" style="width:${140+ (chap[1].length*2)}px"></div></div>`;
  }
  c.innerHTML=body;
}
render(0);
</script></body></html>
"""

html = html.replace('__SHOTS__', json.dumps(shots, ensure_ascii=False))
html = html.replace('__LINES__', json.dumps(lines, ensure_ascii=False))
html = html.replace('__CHAPTERS__', json.dumps(chapters, ensure_ascii=False))
html = html.replace('__DUR__', str(DUR))
open('index.html','w').write(html)
print('written index.html, DUR=', DUR)
