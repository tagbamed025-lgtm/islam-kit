import numpy as np, scipy.signal as sg, soundfile as sf, json
D=json.load(open('data.json')); DUR=D['DUR']; SR=48000; rng=np.random.default_rng(11)
out=np.zeros((int(DUR*SR)+2*SR,2))
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def put(t,x,db,pan=0):
    if t<0: x=x[int(-t*SR):]; t=0
    x=x/(np.max(np.abs(x))+1e-9)*10**(db/20); i=int(t*SR); n=min(len(x),len(out)-i)
    out[i:i+n,0]+=x[:n]*(1-max(0,pan)); out[i:i+n,1]+=x[:n]*(1+min(0,pan))
def B(n,lpf=None):
    x,_=sf.read('bank/'+n+'.wav'); x=x.mean(1) if x.ndim>1 else x
    return lp(x,lpf) if lpf else x
def noise(d,cut,att=.6,rel=1.2):
    n=int(d*SR); w=lp(rng.normal(0,1,n),cut); tt=np.arange(n)/SR
    return w*np.minimum(1,tt/att)*np.clip((d-tt)/rel,0,1)
def shimmer():
    n=int(1.8*SR); tt=np.arange(n)/SR
    return sum(a*np.sin(2*np.pi*f*tt)*np.exp(-tt*(2.0+f/3000)) for f,a in [(1318.5,1),(1975.5,.7),(2637,.5),(3951,.3)])*np.minimum(1,tt/.03)
# ambiance : vent léger continu
put(0,noise(D['VEND']+1,420,1,3)*(.6+.4*np.sin(np.linspace(0,40,int((D['VEND']+1)*SR)))),-37)
ev=json.load(open('events.json'))
W=['whoosh_1','whoosh_2','whoosh_3','whoosh_4','whoosh_5']; lastkey=-9; wi=0
BIG={'élégant','foi','étendard','linceul','dure','l\'étendard','renonce'}
words={}
for c in D['chunks']:
    for L in c['lines']:
        for w in L: words[round(w[1],3)]=w[0].strip('.,…:;»«').lower()
for k,t,key in ev:
    if k=='shot': put(t-.28,B(W[wi%5],6000),-31,pan=rng.uniform(-.2,.2)); wi+=1
    elif k in('mapin','endin'): put(t-.3,B('best_whoosh',7000),-25)
    elif k=='chap': put(t-.25,B('whoosh_4',7000),-23); put(t+.12,B('best_boom',2200),-20)
    elif k=='key':
        if t-lastkey>.6: put(t-.01,B('best_pop',4500),-28,pan=rng.uniform(-.15,.15)); lastkey=t
    elif k=='band': put(t-.02,B('impact_b3',3500),-25)
    elif k=='slam':
        w=words.get(round(t,3),'')
        if any(b in w for b in BIG): put(t-2.0,B('riser_b3',7000),-27); put(t-.03,B('best_cinematic_hit'),-15)
        else: put(t-.03,B('best_cinematic_hit',5000),-21)
    elif k=='titleN': put(t-.04,B('best_cinematic_hit'),-11); put(t+.02,B('best_boom',2500),-15)
    elif k=='titleH': pass
    elif k=='pin': put(t,B('click'),-24)
    elif k=='pin2': put(t,B('thunk'),-20)
    elif k=='route': put(t,B('whoosh_5',5000),-29)
    elif k=='tick': put(t,B('tick'),-27)
    elif k=='units': put(t,B('thunk',3000),-27)
    elif k=='flag': put(t,B('impact_b1',4000),-19)
    elif k=='advance': put(t,noise(3.5,160,1.8,.6),-19); put(t+.4,noise(3.0,900,1.5,.8),-33)
    elif k=='clash':
        for j in range(7): put(t+j*.33+rng.uniform(0,.1),B('impact_b5',1800),-27-rng.uniform(0,5),pan=rng.uniform(-.4,.4))
    elif k=='fall': put(t+.05,B('best_boom',2000),-11); put(t+.02,B('best_cinematic_hit',3000),-17)
    elif k=='shake': put(t-.02,B('impact_b5',2500),-22)
    elif k=='arabic': put(t,shimmer(),-26)
    elif k=='slamH': put(t-.02,B('impact_b3',4000),-22)
    elif k=='pop': put(t,B('best_pop'),-22)
# suspense avant le nom
if D.get('suspense'):
    a,d=D['suspense']; put(a+.05,B('best_sudden_suspense',6000),-19); put(a+d-1.3,B('riser_b2',8000),-26)
sf.write('audio/sfx.wav',out[:int(DUR*SR)],SR); print('sfx ok')
