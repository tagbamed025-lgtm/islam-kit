# Sons discrets RAP-01 (bible §4) : whoosh doux aux transitions, boom sur « péchés », riser + impact avant la citation du hadith,
# AUCUN son ni fond vocal pendant la citation coranique (S6). Écrit audio/sfx.wav et coupe audio/pad.wav sous S6.
import numpy as np, soundfile as sf, json
tl=json.load(open('timeline.json')); SC=tl['SC']; DUR=tl['DUR']; SR=48000
B='../../sons/banque_utilisee/'
def ld(n):
    x,sr=sf.read(B+n); x=x.mean(1) if x.ndim>1 else x
    if sr!=SR: x=np.interp(np.arange(int(len(x)*SR/sr))*sr/SR,np.arange(len(x)),x)
    return x
out=np.zeros(int(DUR*SR)+SR)
def put(n,t,g,end=False):
    x=ld(n)*g; i=max(int((t-(len(x)/SR if end else 0))*SR),0); out[i:i+len(x)]+=x[:len(out)-i]
put('whoosh_1.wav',SC['S1'],.25); put('best_boom.wav',1.15,.35)
for s in ['S2','S3','S4']: put('whoosh_3.wav',SC[s]-.1,.22)
put('riser_b2.wav',SC['S5']+.05,.30,end=True); put('impact_b1.wav',SC['S5']+.05,.35)
put('whoosh_2.wav',SC['END1']-.1,.25); put('whoosh_4.wav',SC['END2']-.1,.22); put('best_pop.wav',SC['END2']+1.0,.35)
out=out[:int(DUR*SR)]; out[int((SC['S6']-.05)*SR):int(SC['S7']*SR)]=0
sf.write('audio/sfx.wav',np.stack([out,out],1),SR)
p,sr=sf.read('audio/pad.wav'); t=np.arange(len(p))/sr
g=np.maximum(np.clip((SC['S6']-t)/.4,0,1),np.clip((t-SC['S7'])/.6,0,1))
sf.write('audio/pad.wav',p*(g[:,None] if p.ndim>1 else g),sr)
