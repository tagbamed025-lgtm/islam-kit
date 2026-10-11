# effets sonores calés sur les événements du rendu (pas de son sur chaque mot — bible §4)
import numpy as np, scipy.signal as sg, soundfile as sf, json
D=json.load(open('data.json')); SR=48000; DUR=D['DUR']; rng=np.random.default_rng(11)
out=np.zeros((int(DUR*SR)+SR,2))
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def put(t,x,db,pan=0):
    if t<0: x=x[int(-t*SR):]; t=0
    if x.ndim>1: x=x.mean(1)
    x=x/(np.max(np.abs(x))+1e-9)*10**(db/20); i=int(t*SR); n=min(len(x),len(out)-i)
    if n>0: out[i:i+n,0]+=x[:n]*(1-max(0,pan)); out[i:i+n,1]+=x[:n]*(1+min(0,pan))
def B(n,lpf=None):
    x,_=sf.read('bank/'+n+'.wav'); x=x.mean(1) if x.ndim>1 else x
    return lp(x,lpf) if lpf else x
def noise(d,cut):
    n=int(d*SR); w=lp(rng.normal(0,1,n),cut); f=np.minimum(1,np.minimum(np.arange(n),n-np.arange(n))/(SR*1.5)); return w*f
def shimmer():
    n=int(1.6*SR); t=np.arange(n)/SR
    return sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*(2.2+f/3000)) for f,a in [(1318.5,1),(1975.5,.7),(2637,.5),(3951,.3)])*np.minimum(1,t/.03)
put(0,noise(D['H'],420),-37)                      # vent léger
W=['whoosh_1','whoosh_2','whoosh_3','whoosh_4','whoosh_5']; lastpop=-9; ns=0
for k,t in sorted(json.load(open('events.json')),key=lambda e:e[1]):
    if k=='scene' and t>.5: put(t-.25,B(W[ns%5],6000),-29,pan=rng.uniform(-.2,.2)); ns+=1
    elif k=='slam': put(t-.02,B('impact_b3',3500),-23)
    elif k=='slamB': put(t-2.0,B('riser_b3',7000),-26); put(t-.03,B('best_cinematic_hit'),-13); put(t,B('best_boom',2500),-20)
    elif k=='slamS': put(t-.02,B('impact_b3',4000),-22)
    elif k=='pop' and t-lastpop>1.5: put(t,B('best_pop',5000),-26); lastpop=t
    elif k=='flash': put(t,shimmer(),-20); put(t-1.2,B('riser_b2',8000),-28)
for sc in D['scenes']:
    if sc.get('kind')=='night': put(sc['s']+.02,B('best_sudden_suspense',6000),-20)
put(D['VEND']-.05,B('best_boom',2500),-22)
sf.write('sfx.wav',out[:int(DUR*SR)],SR); print('sfx ok')
