import numpy as np, scipy.signal as sg, soundfile as sf, json
D=json.load(open('data.json')); DUR=D['DUR']
SR=24000; N=int(DUR*SR); rng=np.random.default_rng(7); t=np.arange(N)/SR
FORM={'mm':[(250,80,1.0),(2200,300,.05),(2900,300,.03)],'oo':[(320,90,1.0),(800,120,.35),(2500,200,.08)]}
def voice(f0,vow,start,dur,amp,det=0,vph=0):
    i0=int(start*SR); n=min(int(dur*SR),N-i0)
    if n<=0: return
    tt=np.arange(n)/SR
    vib=1+.004*np.sin(2*np.pi*5.1*tt+vph)*np.minimum(1,tt/1.2)
    drift=1+.0015*np.interp(tt,np.linspace(0,dur,8),rng.normal(0,1,8))
    ph=2*np.pi*np.cumsum(f0*2**(det/1200)*vib*drift)/SR
    y=np.zeros(n)
    for k in range(1,int(2600/f0)+1):
        fk=k*f0; g=sum(a*np.exp(-.5*((fk-F)/B)**2) for F,B,a in FORM[vow])+.02
        y+=np.sin(k*ph)*(k**-1.1)*g
    a=np.minimum(1,tt/.9)*np.clip((dur-tt)/1.1,0,1)
    mix[i0:i0+n]+=y*a*amp
mix=np.zeros(N)
# drone : ré (D2 A2 D3), puis passage en do (C) pour la partie sombre (Uhud -> manteau)
uh0=uh1=-99
for s0 in np.arange(0,DUR,12):
    d=min(13.5,DUR-s0); low=uh0-1<s0<uh1
    for f0,a in ([(65.41,1.0),(98.0,.55),(130.81,.6)] if low else [(73.42,1.0),(110.0,.55),(146.83,.6)]):
        for det,vp in [(-6,0),(6,1.7)]: voice(f0,'mm',s0,d,a*.5,det,vp)
phrase=[(293.66,4),(311.13,2),(369.99,2),(392.0,4),(369.99,2),(311.13,2),(293.66,6)]
tt0=4.0
while tt0<DUR-2:
    for f0,d in phrase:
        if tt0>=DUR-1: break
        if uh0-1<tt0<uh1: f0*=0.8909   # un ton plus bas
        for det,vp in [(-5,.3),(0,2.1),(7,4.0)]: voice(f0,'oo',tt0,min(d+.9,DUR-tt0),.2,det,vp)
        tt0+=d
    tt0+=6
mix/=np.max(np.abs(mix))
mix+=sg.lfilter(*sg.butter(2,[800/(SR/2),3000/(SR/2)],'band'),rng.normal(0,1,N))*.008
L=int(2.8*SR); it=np.arange(L)/SR
wl=sg.fftconvolve(mix,rng.normal(0,1,L)*np.exp(-it/.7))[:N]; wr=sg.fftconvolve(mix,rng.normal(0,1,L)*np.exp(-it/.7))[:N]
wl/=np.max(np.abs(wl)); wr/=np.max(np.abs(wr))
st=np.stack([.55*mix+.45*wl,.55*mix+.45*wr],1)
g=np.clip(t/3,0,1)*np.clip((DUR-t)/2,0,1)
def dip(a,b,depth=.9,r=.4):
    m=np.clip(np.minimum((t-a)/r,(b-t)/r),0,1); return 1-depth*m
P={}
for q in D['pauses']: P.setdefault(q[2],[]).append((q[0],q[1],q[3]))
a,d,_=max(P[1],key=lambda x:x[2]); g*=dip(a-.2,a+d+.3,.85)   # silence avant le nom
R=D.get('rec')
if R: g*=dip(R['t0']-.3,R['t1']+.3,1.0,.5)                  # aucun son sous le Coran
st*=g[:,None]; st/=np.max(np.abs(st))
sf.write('audio/pad.wav',st,SR); print('pad ok',DUR)
