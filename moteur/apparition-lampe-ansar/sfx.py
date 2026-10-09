import numpy as np, scipy.signal as sg, soundfile as sf, json
SR=48000; rng=np.random.default_rng(5)
EV,SC,DUR=json.load(open('events.json'))
out=np.zeros((int(DUR*SR)+2*SR,2))
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def put(t,x,db,pan=0):
    if t<0: x=x[int(-t*SR):]; t=0
    x=x/(np.max(np.abs(x))+1e-9)*10**(db/20); i=int(t*SR); n=min(len(x),len(out)-i)
    out[i:i+n,0]+=x[:n]*(1-max(0,pan)); out[i:i+n,1]+=x[:n]*(1+min(0,pan))
def B(n,f=None):
    x,_=sf.read('bank/'+n+'.wav'); x=x.mean(1) if x.ndim>1 else x; return lp(x,f) if f else x
def noise(d,cut,a=.6,r=1.0):
    n=int(d*SR); tt=np.arange(n)/SR; return lp(rng.normal(0,1,n),cut)*np.minimum(1,tt/a)*np.clip((d-tt)/r,0,1)
def shimmer():
    n=int(1.8*SR); tt=np.arange(n)/SR
    return sum(a*np.sin(2*np.pi*f*tt)*np.exp(-tt*(2.0+f/3000)) for f,a in [(1318.5,1),(1975.5,.7),(2637,.5),(3951,.3)])*np.minimum(1,tt/.03)
OFF=.3; PZ=[(22.5,1.0),(30.3,.4),(39.1,.5)]
N=lambda t:OFF+t+sum(d for c,d in PZ if t>c)
put(0,noise(DUR,420,1.5,2),-38)                       # vent léger
W=['whoosh_1','whoosh_2','whoosh_3','whoosh_4','whoosh_5']
for i,s in enumerate(SC[1:]): put(s-.25,B(W[i%5],6000),-28,pan=rng.uniform(-.2,.2))
BIG={round(N(x),2) for x in [6.1,14.55,23.1,29.6,35.42,45.85]}
RIS={round(N(x),2) for x in [23.1,45.85]}
nt=0
for k,t in EV:
    if k=='slam':
        big=any(abs(t-b)<.12 for b in BIG)
        if big: put(t-.03,B('best_cinematic_hit'),-13); put(t,B('best_boom',2500),-20)
        else: put(t-.02,B('impact_b3',3500),-23)
        if any(abs(t-b)<.12 for b in RIS): put(t-2.0,B('riser_b3',7000),-26)
    elif k=='type':
        nt+=1
        if nt%3==0: put(t,B('tick'),-35,pan=rng.uniform(-.1,.1))
    elif k=='arabic': put(t,shimmer(),-25)
    elif k=='pop': put(t,B('best_pop',5000),-24)
# suspense avant l'extinction de la lampe
a=N(22.5); put(a+.02,B('best_sudden_suspense',6000),-19); put(N(23.1)-1.6,B('riser_b2',8000),-27)
put(N(30.3)+.05,shimmer(),-20); put(N(30.3)-1.2,B('riser_b2',8000),-28)
sf.write('audio/sfx.wav',out[:int(DUR*SR)],SR); print('sfx ok')
