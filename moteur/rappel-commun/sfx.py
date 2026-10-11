# Sons discrets (bible §4) : whoosh aux transitions, son doux à l'apparition des objets, riser + impact avant une citation de hadith.
# AUCUN son ni fond vocal pendant une citation coranique (scènes 'quran'). Écrit sfx.wav et coupe pad.wav sous le Coran.
import sys, json, numpy as np, soundfile as sf
W = sys.argv[1]; tl = json.load(open(W + '/timeline.json')); S = tl['S']; DUR = tl['DUR']; SR = 48000
B = '/home/claude/islam-kit/sons/banque_utilisee/'
def ld(n):
    x, sr = sf.read(B + n); x = x.mean(1) if x.ndim > 1 else x
    if sr != SR: x = np.interp(np.arange(int(len(x)*SR/sr))*sr/SR, np.arange(len(x)), x)
    return x
out = np.zeros(int(DUR*SR) + SR)
def put(n, t, g, end=False):
    x = ld(n)*g; i = max(int((t - (len(x)/SR if end else 0))*SR), 0); out[i:i+len(x)] += x[:len(out)-i]
put('whoosh_1.wav', S[0]['t0'], .22)
for k, s in enumerate(S):
    prev = S[k-1]['kind'] if k else None
    if k and s['kind'] == 'q' and prev == 'c':
        put('riser_b2.wav', s['t0'], .28, end=True)
        if not s.get('quran'): put('impact_b1.wav', s['t0'], .32)
    elif k and not s.get('quran'): put('whoosh_3.wav', s['t0'] - .1, .2)
    if s['kind'] == 'c':
        a = s.get('anim'); t0 = s['t0'] + .05
        if a in ('pop', 'door'): put('best_pop.wav', t0 + .2, .22)
        elif a == 'drop': put('thunk.wav', t0 + .7, .28)
        else: put('whoosh_5.wav', t0, .16)
put('whoosh_2.wav', tl['END1'] - .1, .25); put('whoosh_4.wav', tl['END2'] - .1, .22); put('best_pop.wav', tl['END2'] + 1.0, .35)
out = out[:int(DUR*SR)]
Q = [s for s in S if s.get('quran')]
p, sr = sf.read(W + '/pad.wav'); t = np.arange(len(p))/sr
if Q:
    a, b = Q[0]['t0'] - .05, Q[-1]['t1']
    out[int((a - .05)*SR):int(b*SR)] = 0
    g = np.maximum(np.clip((a - t)/.4, 0, 1), np.clip((t - b)/.6, 0, 1))
    p = p*(g[:, None] if p.ndim > 1 else g)
sf.write(W + '/sfx.wav', np.stack([out, out], 1), SR); sf.write(W + '/pad.wav', p, sr)
print('sfx ok', 'coran coupé' if Q else '')
