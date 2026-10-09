import numpy as np, scipy.signal as sg, soundfile as sf
SR=48000; DUR=76.6; rng=np.random.default_rng(3)
out=np.zeros((int(DUR*SR)+SR,2))
def env(n,a,d): t=np.arange(n)/SR; e=np.minimum(1,t/max(a,1e-4))*np.exp(-np.maximum(0,t-a)/d); return e
def bp(x,lo,hi): b,a=sg.butter(2,[lo/(SR/2),hi/(SR/2)],'band'); return sg.lfilter(b,a,x)
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def hp(x,f): b,a=sg.butter(2,f/(SR/2),'high'); return sg.lfilter(b,a,x)
def norm(x): return x/ (np.max(np.abs(x))+1e-9)
def add(t,x,db,pan=0):
    i=int(t*SR); x=norm(x)*10**(db/20); n=min(len(x),len(out)-i)
    out[i:i+n,0]+=x[:n]*(1-max(0,pan)); out[i:i+n,1]+=x[:n]*(1+min(0,pan))
def whoosh(d=.5):
    n=int(d*SR); w=rng.normal(0,1,n); t=np.linspace(0,1,n)
    # sweeping band via short blocks
    y=np.zeros(n); B=512
    for k in range(0,n,B):
        c=300+2500*np.sin(np.pi*t[k])**2; y[k:k+B]=bp(w[k:k+B+0],c*.6,min(c*1.6,20000))[:len(y[k:k+B])]
    return y*np.sin(np.pi*t)**2
def impact(d=1.4,f0=70):
    n=int(d*SR); t=np.arange(n)/SR; f=f0*np.exp(-t*3)+30
    s=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*3.5)
    nz=lp(rng.normal(0,1,n),900)*np.exp(-t*18)*.7
    return s+nz
def shing(d=1.2):
    n=int(d*SR); t=np.arange(n)/SR; y=np.zeros(n)
    for f,a in [(2150,1),(3370,.7),(4880,.5),(6230,.35),(7710,.25)]: y+=a*np.sin(2*np.pi*f*t+rng.random()*6)*np.exp(-t*(2.5+f/4000))
    sc=hp(rng.normal(0,1,n),3000)*env(n,.15,.12)*.6
    return y*np.minimum(1,t/.02)+sc
def crack(d=.25):
    n=int(d*SR); t=np.arange(n)/SR
    return hp(rng.normal(0,1,n),1500)*np.exp(-t*40)+.6*np.sin(2*np.pi*(1800+rng.random()*900)*t)*np.exp(-t*30)
def click(): n=int(.03*SR); t=np.arange(n)/SR; return bp(rng.normal(0,1,n),1500,6000)*np.exp(-t*250)
def pop(): n=int(.12*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*(900-3000*t)*t)*np.exp(-t*45)
def thump(): n=int(.35*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*(90*np.exp(-t*6)+40)*t)*np.exp(-t*14)+lp(rng.normal(0,1,n),500)*np.exp(-t*40)*.5
def wind(d):
    n=int(d*SR); w=lp(rng.normal(0,1,n),500); m=.6+.4*np.sin(np.linspace(0,d*1.3,n))
    fade=np.minimum(1,np.minimum(np.arange(n),n-np.arange(n))/(SR*.6)); return w*m*fade
def rumble(d): n=int(d*SR); t=np.arange(n)/SR; return lp(rng.normal(0,1,n),120)*np.minimum(1,t/1.2)*np.minimum(1,(d-t)/.5)
def riser(d):
    n=int(d*SR); t=np.arange(n)/SR; y=np.zeros(n); B=1024; w=rng.normal(0,1,n)
    for k in range(0,n,B): c=400+5000*(k/n)**2; y[k:k+B]=bp(w[k:k+B],c*.7,min(c*1.4,20000))[:len(y[k:k+B])]
    return y*(t/d)**2
def paper(d=.6):
    n=int(d*SR); t=np.arange(n)/SR; g=(rng.random(n)<.004).astype(float); return bp(sg.lfilter([1],[1,-.97],g*rng.normal(0,1,n)),1500,7000)*np.sin(np.pi*t/d)
def puff(): n=int(.6*SR); t=np.arange(n)/SR; return bp(rng.normal(0,1,n),200,1500)*np.sin(np.pi*np.minimum(1,t/.6))**2
def tick(): n=int(.02*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*2400*t)*np.exp(-t*300)
# timeline
add(0.0,wind(4.6),-30); add(0.0,impact(1.6,65),-12); add(0.0,whoosh(.4),-24)
add(0.95,whoosh(.35),-22); add(1.0,impact(.8,90),-18)
for k in range(10): add(1.1+k*.33,thump(),-27,pan=(-.3 if k%2 else .3))
add(4.3,whoosh(.4),-22)
add(9.15,whoosh(.5),-20); add(9.75,shing(1.4),-17); add(9.8,impact(.9,55),-20)
for k in range(6): add(12.35+k/9,click(),-24)
for k in range(12): add(13.0+k/14,click(),-24)
add(14.46,pop(),-22)
add(16.95,whoosh(.4),-22); add(20.05,whoosh(.9),-19); add(20.16,thump(),-20)
add(21.2,whoosh(.35),-20); add(21.52,impact(1.6,55),-10); add(21.5,crack(.2),-24)
add(22.5,whoosh(.4),-22); add(22.6,wind(3.3),-30)
add(24.5,riser(1.45),-22); add(25.9,shing(1.8),-26); add(25.9,impact(1.2,45),-24)
add(28.0,whoosh(.4),-22); add(29.26,impact(1.2,60),-14)
for k in range(14): add(30.31+k*.065,tick(),-26)
add(31.6,rumble(3.0),-16); add(31.65,whoosh(1.0),-24)
add(34.58,impact(.9,80),-18)
for tt in [35.87,36.67,37.37]: add(tt,thump(),-15); add(tt,impact(.7,50),-24)
add(37.7,whoosh(.4),-22); add(37.9,shing(1.3),-18); add(38.1,thump(),-20)
add(39.6,whoosh(.4),-22)
for k in range(9): add(40.97+k*.189,crack(),-21,pan=(k%3-1)*.3)
add(42.7,impact(.9,55),-20)
add(44.2,impact(1.2,60),-15); add(44.64,whoosh(.4),-24)
add(45.75,whoosh(.6),-22); add(45.9,paper(.7),-24)
add(57.0,whoosh(.5),-22); add(57.88,impact(1.1,60),-15)
for k in range(26): add(58.78+k*.05,pop(),-31)
add(60.8,impact(1.6,45),-18)
add(64.9,whoosh(.5),-26); add(65.8,puff(),-22)
add(73.35,whoosh(.4),-22); add(73.62,impact(1.0,60),-15); add(74.22,pop(),-20); add(75.0,pop(),-26)
sf.write('audio/sfx.wav',out[:int(DUR*SR)],SR)
print('ok')
