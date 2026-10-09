import numpy as np, scipy.signal as sg, soundfile as sf
SR=24000; DUR=32.4; N=int(DUR*SR); rng=np.random.default_rng(7)
t=np.arange(N)/SR
FORM={'mm':[(250,80,1.0),(2200,300,.05),(2900,300,.03)],'oo':[(320,90,1.0),(800,120,.35),(2500,200,.08)],'ah':[(700,110,1.0),(1150,130,.6),(2600,200,.15)]}
def voice(f0,vow,start,dur,amp,det=0,vph=0):
    i0=int(start*SR); n=int(dur*SR); n=min(n,N-i0); tt=np.arange(n)/SR
    vib=1+.004*np.sin(2*np.pi*5.1*tt+vph)*np.minimum(1,tt/1.2)
    drift=1+.0015*np.interp(tt,np.linspace(0,dur,8),rng.normal(0,1,8))
    f=f0*2**(det/1200)*vib*drift; ph=2*np.pi*np.cumsum(f)/SR
    y=np.zeros(n); K=int(2600/f0)
    for k in range(1,K+1):
        fk=k*f0; g=sum(a*np.exp(-.5*((fk-F)/B)**2) for F,B,a in FORM[vow])+.02
        y+=np.sin(k*ph)*(k**-1.1)*g
    a=np.minimum(1,tt/.9)*np.minimum(1,(dur-tt)/1.1).clip(0,1)
    out=np.zeros(N); out[i0:i0+n]=y*a*amp; return out
mix=np.zeros(N)
# drone D2 A2 D3 humming, long notes re-attacked every 12 s for life
for s0 in np.arange(0,DUR,12):
    d=min(13.5,DUR-s0)
    for f0,a in [(73.42,1.0),(110.0,.55),(146.83,.6)]:
        for det,vp in [(-6,0),(6,1.7)]: mix+=voice(f0,'mm',s0,d,a*.5,det,vp)
# slow Hijaz melody "oo"
phrase=[(293.66,4),(311.13,2),(369.99,2),(392.0,4),(369.99,2),(311.13,2)]
tt0=3.0
while tt0<DUR-2:
    for f0,d in phrase:
        if tt0>=DUR-1: break
        dd=min(d+.9,DUR-tt0)
        for det,vp in [(-5,.3),(0,2.1),(7,4.0)]: mix+=voice(f0,'oo',tt0,dd,.22,det,vp)
        tt0+=d
mix/=np.max(np.abs(mix))
# breath noise
mix+=sg.lfilter(*sg.butter(2,[800/(SR/2),3000/(SR/2)],'band'),rng.normal(0,1,N))*.01
# stereo reverb
L=int(2.8*SR); ir_t=np.arange(L)/SR
irL=rng.normal(0,1,L)*np.exp(-ir_t/0.7); irR=rng.normal(0,1,L)*np.exp(-ir_t/0.7)
wetL=sg.fftconvolve(mix,irL)[:N]; wetR=sg.fftconvolve(mix,irR)[:N]
wetL/=np.max(np.abs(wetL)); wetR/=np.max(np.abs(wetR))
st=np.stack([.55*mix+.45*wetL,.55*mix+.45*wetR],1)
# global envelope: fade in, out before verse (66.3->66.9), back for outro 73.4
g=np.clip(t/3,0,1)*np.clip((DUR-t)/1.5,0,1)
st*=g[:,None]; st/=np.max(np.abs(st))
sf.write('audio/pad.wav',st,SR); print('pad ok')
