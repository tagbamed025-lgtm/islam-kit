import json, re, subprocess, sys, os, numpy as np, soundfile as sf
M='/home/claude/musab/'
LINES=json.load(open(M+'align_lines.json'))
SPEC=[l.rstrip('\n') for l in open(M+'chunks.txt',encoding='utf-8') if l.strip()]
r=subprocess.run(['ffmpeg','-i',M+'audio/voix_t.wav','-af','silencedetect=noise=-38dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
SIL=list(zip([float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)],[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]))
def cut_between(a,b):
    g=(a+b)/2; best=min(SIL,key=lambda se:abs((se[0]+se[1])/2-g)); m=(best[0]+best[1])/2
    return m if abs(m-g)<.8 and a-0.05<=m<=b+0.05 else g
def bounds(i):
    s=0 if i==0 else cut_between(LINES[i-1][-1][2],LINES[i][0][1])
    e=LINES[i][-1][2]+0.35 if i==len(LINES)-1 else cut_between(LINES[i][-1][2],LINES[i+1][0][1])
    if i==len(LINES)-1: e=min(e, LINES[i][-1][1]+0.9)
    return max(0,s-0.0),e

def build(cfg):
    os.makedirs(cfg['dir']+'/audio',exist_ok=True)
    v,sr=sf.read(M+'audio/voix_t.wav'); v=v.mean(1) if v.ndim>1 else v
    LEAD=0.5; parts=[np.zeros(int(LEAD*sr))]; t=LEAD; W={}; PZ={}
    for i,pause in cfg['lines']:
        s,e=bounds(i); seg=v[int(s*sr):int(e*sr)].copy(); f=int(.012*sr); seg[:f]*=np.linspace(0,1,f); seg[-f:]*=np.linspace(1,0,f)
        W[i]=[[w,round(t+(a-s),3),round(t+(b-s),3)] for w,a,b in LINES[i]]
        parts.append(seg); t+=len(seg)/sr; PZ[i]=t
        if pause: parts.append(np.zeros(int(pause*sr))); t+=pause
    VEND=t; DUR=VEND+0.3+cfg['end']+cfg['sub']
    voice=np.concatenate(parts+[np.zeros(int((DUR-VEND)*sr)+sr)])[:int(DUR*sr)]
    sf.write(cfg['dir']+'/audio/voice_final.wav',voice,sr)
    def ls(i): return W[i][0][1]
    def wt(i,word,n=1):
        k=0
        for w,a,b in W[i]:
            if w.strip('«»,.…:;!?').lower().startswith(word.lower()):
                k+=1
                if k==n: return a
        raise Exception(word)
    CH=[];inq=False
    for i,_ in cfg['lines']:
        sl=SPEC[i]
        if sl.startswith('@TITLE'): continue
        k=0;words=W[i]
        for ch in sl.split(' | '):
            band=ch.startswith('#'); ch=ch.lstrip('#'); lines=[[]]
            for tk in ch.split(' '):
                if tk=='/': lines.append([]); continue
                key='*' in tk; tk=tk.replace('*','')
                w,a,b=words[k]; assert w==tk,(i,w,tk); k+=1
                if '«' in tk: inq=True
                lines[-1].append([tk,a,b,1 if key else 0]); q=inq
                if '»' in tk: inq=False
            CH.append({'lines':lines,'band':band,'quote':q,'t0':lines[0][0][1],'t1':lines[-1][-1][2]})
    for a,b in zip(CH,CH[1:]): a['hide']=min(b['t0']-0.14,a['t1']+0.7)
    CH[-1]['hide']=min(CH[-1]['t1']+1.2,VEND+0.25)
    X=[]
    ctx={'ls':ls,'wt':wt,'PZ':PZ,'VEND':VEND}
    for sh in cfg['shots'](ctx): X.append({'t':round(sh[0],3),'img':sh[1],'cam':sh[2],'fx':sh[3] if len(sh)>3 else {}})
    X.append({'t':VEND+0.3,'img':'END','cam':None,'fx':{}}); X.append({'t':VEND+0.3+cfg['end'],'img':'SUB','cam':None,'fx':{}})
    T=cfg.get('title')
    title=T(ctx) if T else {'t0':-9,'th':-9,'tn':-9,'t1':-9}
    data={'DUR':DUR,'VEND':VEND,'chunks':CH,'chap':[],'title':title,'shots':X,'suspense':cfg.get('suspense',lambda c:None)(ctx),'dips':cfg.get('dips',lambda c:[])(ctx)}
    json.dump(data,open(cfg['dir']+'/data.json','w'),ensure_ascii=False)
    html=open('engine_v.html').read().replace('__SRC__',cfg['src']).replace('COMPAGNONS · <b>03</b>',cfg['tag'])
    open(cfg['dir']+'/index.html','w').write(html.replace('__DATA__',json.dumps(data,ensure_ascii=False)))
    for d in ['hd','img','node_modules','bank']:
        p=cfg['dir']+'/'+d
        if not os.path.exists(p): os.symlink(M+d,p)
    print(cfg['dir'],'DUR',round(DUR,2),'VEND',round(VEND,2),'chunks',len(CH),'shots',len(X))
