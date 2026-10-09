import numpy as np, scipy.signal as sg, soundfile as sf, json
SR=48000; DUR=32.4; OFF=0.35; rng=np.random.default_rng(11)
out=np.zeros((int(DUR*SR)+SR,2))
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def bp(x,lo,hi): b,a=sg.butter(2,[lo/(SR/2),hi/(SR/2)],'band'); return sg.lfilter(b,a,x)
def put(t,x,db,pan=0):
    if x.ndim>1: x=x.mean(1)
    x=x/(np.max(np.abs(x))+1e-9)*10**(db/20); i=int(t*SR); n=min(len(x),len(out)-i)
    out[i:i+n,0]+=x[:n]*(1-max(0,pan)); out[i:i+n,1]+=x[:n]*(1+min(0,pan))
def B(n,lpf=None):
    x,_=sf.read('bank/'+n+'.wav'); x=x.mean(1) if x.ndim>1 else x
    return lp(x,lpf) if lpf else x
def wind(d,cut=500):
    n=int(d*SR); w=lp(rng.normal(0,1,n),cut); m=.55+.45*np.sin(np.linspace(0,d*1.1,n)+1)
    f=np.minimum(1,np.minimum(np.arange(n),n-np.arange(n))/(SR*1.2)); return w*m*f
def shimmer():
    n=int(1.6*SR); t=np.arange(n)/SR
    y=sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*(2.2+f/3000)) for f,a in [(1318.5,1),(1975.5,.7),(2637,.5),(3951,.3)])
    return y*np.minimum(1,t/.03)
# ambiances
put(0.0,wind(18.4,380),-36)            # vent léger dehors (chambre)
put(17.9,wind(12.0,650),-29)            # vent du désert
# transitions de scène (whoosh doux)
for i,c in enumerate([4.55,9.4,14.85,17.8,22.75,29.6]):
    put(c+OFF-.3,B(['whoosh_1','whoosh_2','whoosh_3','best_whoosh','whoosh_2','whoosh_1'][i],6000),-29)
ev=json.load(open('events.json'))
for k,t,key in ev:
    if k=='key' and key not in ('5-2-1','7-2-1','7-2-2'): put(t-.01,B('best_pop',5000),-24,pan=rng.uniform(-.15,.15))
    elif k=='slam':
        put(t-2.0,B('riser_b3',7000),-26); put(t-.02,B('best_cinematic_hit'),-13)
    elif k=='arabic': put(t,shimmer(),-27)
    elif k=='slamH': put(t-.02,B('impact_b3',4000),-22)
    elif k=='pop': put(t,B('best_pop'),-22)
# fin de la parole : « derrière lui » -> grave et doux
put(24.88+OFF-.02,B('best_boom',2500),-21)
sf.write('audio/sfx.wav',out[:int(DUR*SR)],SR); print('ok')
