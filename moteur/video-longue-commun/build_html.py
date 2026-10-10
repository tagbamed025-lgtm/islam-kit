import json, re
exec(open('cfg.py', encoding='utf-8').read().split('# ---- plans ----')[0])
src = open('/home/claude/islam-kit/moteur/video-longue-musab/index.html', encoding='utf-8').read()
D = open('data.json', encoding='utf-8').read()
i = src.find('const D='); j = src.find('\n', i)
s = src[:i] + 'const D=' + D + ';' + src[j:]

def rep(a, b, n=1):
    global s
    assert s.count(a) >= 1, a[:80]
    s = s.replace(a, b) if n == 0 else s.replace(a, b, n)

# photos : J1…J18
rep("if(/^M\\d/.test(s.img)){", "if(/^(J|U|SA|K|SD)\\d/.test(s.img)){")
rep("if(/^M\\d/.test(s.img)){renderPhoto", "if(/^(J|U|SA|K|SD)\\d/.test(s.img)){renderPhoto")
# étiquette de série
rep('COMPAGNONS · <b>03</b>', 'COMPAGNONS · <b>'+H['TAG']+'</b>')
# titre
rep('style="position:absolute;left:0;right:0;top:390px;text-align:center;font-size:210px;line-height:1;text-shadow:0 12px 50px rgba(0,0,0,.6)">MUS\'AB IBN UMAYR',
    'style="position:absolute;left:0;right:0;top:410px;text-align:center;font-size:'+str(H['NSIZE'])+'px;line-height:1;text-shadow:0 12px 50px rgba(0,0,0,.6)">'+H['NAME'])
rep('>مُصْعَبُ بْنُ عُمَيْرٍ</div>', '>'+H['AR']+'</div>')
# carte : puce
rep("s.fx.route==='abyssinie'?'615 · PREMIÈRE HÉGIRE'", "s.fx.route==='abyssinie'?'HÉGIRE VERS L\\'ABYSSINIE'")
# carte de fin
rep('src="hd/M26_golden_rays.jpg"', 'src="hd/'+H['END_BG']+'.jpg"')
rep('>مُصْعَبُ بْنُ عُمَيْرٍ رَضِيَ اللهُ عَنْهُ</div>', '>'+H['AR']+' رَضِيَ اللهُ عَنْهُ</div>')
rep('Sahîh al-Bukhârî · 3925 · 1276 · 1274<br>Ibn Sa\'d, <span style="color:var(--gold)">aṭ-Ṭabaqât al-Kubrâ</span><br>Ibn Hishâm, <span style="color:var(--gold)">as-Sîra an-Nabawiyya</span>',
    H['SOURCES'])

# ---------- couche RÉCITATION (fond émeraude + arche, aucun son ajouté) ----------
CUT_JS = r'''
/* ================= MOTION DESIGN : OBJET DÉTOURÉ SUR CRÈME ================= */
function cutCard(s){const f=s.fx;return `<div class="ov" style="background:#F4F1EA"></div>
  <div class="ov" style="background:radial-gradient(ellipse 75% 70% at 50% 42%,rgba(255,255,255,.55) 0%,rgba(244,241,234,0) 60%,rgba(120,100,70,.18) 100%)"></div>
  <div class="csh" style="position:absolute;left:${960-f.w*.42}px;width:${f.w*.84}px;top:${(f.y||470)+f.h*.5-30}px;height:60px;border-radius:50%;background:radial-gradient(ellipse at center,rgba(60,45,25,.35) 0%,rgba(60,45,25,0) 70%)"></div>
  <img class="cob" src="cut/${f.obj}.png" style="position:absolute;left:${960-f.w/2}px;top:${(f.y||470)-f.h/2}px;width:${f.w}px;height:${f.h}px;filter:drop-shadow(0 26px 30px rgba(40,30,15,.35));transform-origin:50% 60%">`;}
function renderCut(s,T){const f=s.fx,e=s.el;if(!s.ob){s.ob=e.querySelector('.cob');s.cs=e.querySelector('.csh');}
  const h=T-s.t;let x=0,y=0,r=0,sc=1,sh=1;
  const fl=Math.sin(T*1.3)*6, zoom=1+.04*cl(h/6);
  if(f.anim==='drop'){const p=cl((h-.15)/.6);y=p<1?lerp(-900,0,bk(p)):fl;sh=cl(p);if(h>.6)mark('cut'+s.t,'cuthit',s.t+.6);}
  else if(f.anim==='slide'){const p=eo5(cl((h-.1)/.8));x=lerp(1500,0,p)+(p>=1?fl*.5:0);sh=p;if(h>.1)mark('cut'+s.t,'cutin',s.t+.1);}
  else if(f.anim==='rise'){const p=eo5(cl((h-.1)/.9));y=lerp(700,0,p)+(p>=1?fl:0);sh=p;if(h>.1)mark('cut'+s.t,'cutin',s.t+.1);}
  else if(f.anim==='staff'){const g=T-f.hit;const p0=eo5(cl((h-.05)/.8));const p=cl((T-(f.hit-.35))/.35);y=lerp(-800,-170,p0)+fl*(1-p)+lerp(0,170,p*p);r=lerp(-30,-14,p0)+lerp(0,14,p*p);sh=.4*p0+.6*p;
    if(g>0){const A=12*Math.exp(-g*7);y+=A*Math.sin(g*60);r+=A*.25*Math.sin(g*50);mark('cut'+s.t,'cuthit',f.hit);}}
  else if(f.anim==='exit'){const p=eio(cl((T-f.hit)/.9));x=lerp(0,-1900,p)+(p<=0?fl*.5:0);r=lerp(0,-6,p);sh=1-p;if(T>f.hit)mark('cut'+s.t,'cutout',f.hit);}
  s.ob.style.transform=`translate(${x}px,${y}px) rotate(${r}deg) scale(${zoom})`;
  s.cs.style.opacity=sh;s.cs.style.transform=`translateX(${x}px) scaleX(${.6+.4*sh})`;}
'''
REC_JS = r'''
/* ================= RÉCITATION ================= */
function recCard(s){const R=D.rec;let v='';
  R.verses.forEach((x,i)=>{v+=`<div class="rv" data-i="${i}" style="position:absolute;left:560px;width:800px;top:250px;text-align:center;opacity:0">
     <div class="ar" style="font-size:${x.ar.length>45?64:84}px;line-height:1.55;color:#F3E2B6;white-space:normal;text-shadow:0 6px 26px rgba(0,0,0,.55)">${x.ar}</div>
     <div style="margin:26px auto 0;width:180px;height:2px;background:rgba(237,203,133,.7)"></div>
     <div class="corm" style="margin-top:22px;font-size:${x.fr.length>90?38:44}px;line-height:1.3;color:var(--cream);text-shadow:0 4px 18px rgba(0,0,0,.6)">${x.fr}</div>
     <div style="margin-top:20px;font-family:Inter;font-weight:800;font-size:19px;letter-spacing:.35em;color:var(--gold)">MARYAM · 19:${x.n}</div></div>`;});
  return `<img class="ph" src="hd/J18.jpg"><div class="ov" style="background:radial-gradient(ellipse 34% 62% at 50% 46%,rgba(3,22,16,.55) 0%,rgba(3,22,16,.15) 70%,rgba(0,0,0,0) 100%)"></div>
   <div class="ov" style="background:linear-gradient(to bottom,rgba(0,0,0,.25),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 70%,rgba(0,0,0,.45))"></div>
   <div class="chip rchip" style="left:50%;top:150px;transform:translateX(-50%);opacity:0">SOURATE MARYAM · RÉCITATION</div>${v}`;}
function renderRec(s,T){const R=D.rec,e=s.el;if(!s.im){s.im=e.querySelector('.ph');s.vs=[...e.querySelectorAll('.rv')];s.ch=e.querySelector('.rchip');}
  const q=cl((T-s.t)/(s.end+XF-s.t));cam(s.im,.5,.47,lerp(1.0,1.07,q));
  s.ch.style.opacity=P(T,s.t+.3,.6);
  s.vs.forEach((d,i)=>{const x=R.verses[i];const nx=R.verses[i+1];const t1=nx?nx.s-.15:R.t1-.3;
    const a=P(T,x.s-.25,.7,eo3),o=cl((t1+.35-T)/.35);d.style.opacity=Math.min(a,o);d.style.transform=`translateY(${(1-a)*18}px)`;});}
'''
rep("/* ================= FIN : SOURCES & ABONNE-TOI ================= */", CUT_JS + REC_JS + "\n/* ================= FIN : SOURCES & ABONNE-TOI ================= */")
rep("else if(s.img==='END'){d.innerHTML=endCard();}", "else if(s.img==='REC'){d.innerHTML=recCard(s);}\n  else if(s.img==='CUT'){d.innerHTML=cutCard(s);}\n  else if(s.img==='END'){d.innerHTML=endCard();}")
rep("else if(s.img==='END')renderEnd(s,T);", "else if(s.img==='REC')renderRec(s,T);else if(s.img==='CUT')renderCut(s,T);else if(s.img==='END')renderEnd(s,T);")
# sous-titres à l'encre sur fond crème
rep(".ln.band .w.k{color:var(--gold)}", ".ln.band .w.k{color:var(--gold)}\n.ink.sh{text-shadow:none}.ink .ln:not(.band) .w{color:#141414}.ink .ln:not(.band) .w.k{color:#0F5B46}.ink.corm .w{color:#141414}")
rep("function renderCaps(T){const hid=capsHidden(T);", "function renderCaps(T){const hid=capsHidden(T);let top=null;SH.forEach(s=>{if(T>=s.t&&T<s.end+.2)top=s;});const ink=top&&top.img==='CUT'&&T>top.t+XF*.6;")
rep("c.el.style.display=vis?'flex':'none';if(!vis)return;", "c.el.style.display=vis?'flex':'none';if(!vis)return;c.el.classList.toggle('ink',!!ink);")
# pas de sous-titres pendant la récitation ; marqueur pour couper le son
rep("function capsHidden(T){const t=D.title;", "function capsHidden(T){const t=D.title;if(D.rec&&T>D.rec.t0-.1&&T<D.rec.t1)return true;")
open('index.html', 'w', encoding='utf-8').write(s)
print('index.html', len(s))
