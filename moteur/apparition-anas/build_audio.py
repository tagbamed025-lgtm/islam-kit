import numpy as np, soundfile as sf, json, subprocess, re
v,sr=sf.read('audio/voix_t.wav'); v=v.mean(1) if v.ndim>1 else v
OFF=.3; P=[(15.35,.35),(34.25,1.0),(46.45,.7)]
def N(t): return OFF+t+sum(d for c,d in P if t>c)
parts=[np.zeros(int(OFF*sr))]; prev=0
for c,d in P:
    ci=int(c*sr); s=v[prev:ci].copy(); f=int(.01*sr); s[-f:]*=np.linspace(1,0,f); parts+=[s,np.zeros(int(d*sr))]; prev=ci
parts.append(v[prev:]); voice=np.concatenate(parts)
DUR=N(53.6); voice=np.concatenate([voice,np.zeros(int(DUR*sr))])[:int(DUR*sr)]
sf.write('audio/voice_final.wav',voice,sr); print('DUR',DUR)
