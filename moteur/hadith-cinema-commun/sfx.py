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
def wind(d,cut=500):
    n=int(d*SR); w=lp(rng.normal(0,1,n),cut); m=.55+.45*np.sin(np.linspace(0,d*1.1,n)+1)
    f=np.minimum(1,np.minimum(np.arange(n),n-np.arange(n))/(SR*1.2)); return w*m*f
def shimmer():
    n=int(1.6*SR); t=np.arange(n)/SR
    y=sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*(2.2+f/3000)) for f,a in [(1318.5,1),(1975.5,.7),(2637,.5),(3951,.3)])
    return y*np.minimum(1,t/.03)
put(0,wind(D['H'],420),-35)                      # vent léger continu
W=['whoosh_1','whoosh_2','whoosh_3','best_whoosh','whoosh_4','whoosh_5']; last=-9; lastpop=-9; cl=D.get('climax')
ev=json.load(open('events.json'))
for i,(k,t,key) in enumerate(sorted(ev,key=lambda e:e[1])):
    if k=='shot' and t-last>1.2 and not (cl and abs(t-cl)<1.0): put(t-.3,B(W[i%6],6000),-30); last=t
    elif k=='key' and t-lastpop>2.5: put(t-.01,B('best_pop',5000),-25,pan=rng.uniform(-.15,.15)); lastpop=t
    elif k=='slam': put(t-2.0,B('riser_b3',7000),-26); put(t-.02,B('best_cinematic_hit'),-13)
    elif k=='arabic': put(t,shimmer(),-27)
    elif k=='slamH': put(t-.02,B('impact_b3',4000),-22)
    elif k=='pop': put(t,B('best_pop'),-22)
put(D['VEND']-.05,B('best_boom',2500),-22)        # fin de la parole : grave et doux
sf.write('sfx.wav',out[:int(DUR*SR)],SR); print('sfx ok')
