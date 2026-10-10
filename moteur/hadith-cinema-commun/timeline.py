# Moteur commun des reels hadith (9:16, rendu cinéma). À lancer dans le dossier de travail du reel (cfg.py, script.txt, align_lines.json, voix_t.wav).
import json, re, subprocess, numpy as np, soundfile as sf
exec(open('cfg.py', encoding='utf-8').read())
LINES = json.load(open('align_lines.json'))
v, SR = sf.read('voix_t.wav')
if v.ndim > 1: v = v.mean(1)
VLEN = len(v) / SR
LEAD = 0.35; FINAL_SIL = 1.2; END_CARD = 4.8; SUB_CARD = 2.9

r = subprocess.run(['ffmpeg', '-i', 'voix_t.wav', '-af', 'silencedetect=noise=-38dB:d=0.05', '-f', 'null', '-'], capture_output=True, text=True).stderr
S = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
E = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = [(s, e) for s, e in zip(S, E) if e < VLEN - 0.05 and s > 0.05]
FLAT = [(li, wi, w, s, e) for li, L in enumerate(LINES) for wi, (w, s, e) in enumerate(L)]
def clean(w): return w.strip('«»,.…:;!?—  ').lower().replace('’', "'")
def widx(li, prefix, n=1):
    k = 0
    for i, x in enumerate(LINES[li]):
        ww = clean(x[0])
        if ww.startswith(prefix.lower()) or ("'" in ww and ww.split("'")[-1].startswith(prefix.lower())):
            k += 1
            if k == n: return i
    raise Exception(f'mot {prefix} absent de la ligne {li}: ' + ' '.join(x[0] for x in LINES[li]))
last = lambda li: len(LINES[li]) - 1

# ---- pauses minimales (bible §3) : on n'enlève jamais de silence, on allonge seulement ----
def target(i):
    li, wi, w, s, e = FLAT[i]
    if li == len(LINES) - 2 and wi == last(li): return 1.2           # avant la dernière phrase
    nxt = FLAT[i + 1][2]
    if nxt.startswith('«') or w.endswith(':'): return 1.0              # avant une citation
    if re.search(r'[.?!…»]$', w): return 0.7                           # fin de phrase / points de suspension
    if w.endswith(',') or w.endswith(';'): return 0.35                 # virgule
    return None
used = set(); CUTS = []
for i in range(len(FLAT) - 1):
    tg = target(i)
    if tg is None: continue
    a, b = FLAT[i][4], FLAT[i + 1][3]; g = (min(a, b) + max(a, b)) / 2
    best = None; bd = 9
    for j, (s, e) in enumerate(SIL):
        if j in used: continue
        dist = 0 if s <= g <= e else min(abs(g - s), abs(g - e))
        if dist < bd: bd, best = dist, j
    if best is not None and bd < 0.6:
        used.add(best); s, e = SIL[best]; nat = e - s; at = (s + e) / 2
    else: nat = 0.0; at = g
    CUTS.append((at, max(0.0, tg - nat), FLAT[i][0], FLAT[i][1], nat))
CUTS.sort()
def NT(t): return LEAD + t + sum(d for c, d, *_ in CUTS if c < t)
parts = [np.zeros(int(LEAD * SR))]; prev = 0
for c, d, *_ in CUTS:
    ci = int(c * SR); parts.append(v[prev:ci]); parts.append(np.zeros(int(d * SR))); prev = ci
parts.append(v[prev:]); voice = np.concatenate(parts)
VEND = (np.nonzero(np.abs(voice) > 10 ** (-45 / 20))[0][-1]) / SR
GSTART = VEND + FINAL_SIL; HSTART = GSTART + END_CARD; DUR = HSTART + SUB_CARD
voice = np.concatenate([voice, np.zeros(int(DUR * SR) + SR)])[:int(DUR * SR)]
sf.write('voice_final.wav', voice, SR)
def snap(s, e):
    for a, b in SIL:
        if a - .12 <= s < b: s = b
        if a < e <= b + .12: e = a
    return s, max(e, s + .06)
W = [[[w, round(NT(snap(s, e)[0]), 3), round(NT(snap(s, e)[1]), 3)] for w, s, e in L] for L in LINES]
for L in W:
    for x in L: x[1] = min(x[1], VEND); x[2] = min(x[2], VEND + .2)
def at(a):
    """ancre -> temps : ligne (int) = début de ligne ; (ligne, 'mot'[, n]) = début du mot ; ('fin', ligne) = fin de ligne"""
    if isinstance(a, (int, float)) and not isinstance(a, bool): return W[int(a)][0][1]
    if a[0] == 'fin': return W[a[1]][-1][2]
    return W[a[0]][widx(a[0], a[1], a[2] if len(a) > 2 else 1)][1]

# ---- sous-titres : groupes courts, citations en italique ----
CL = (CLIMAX[0], widx(CLIMAX[0], CLIMAX[1])) if CLIMAX else None
CH = []; inq = False
for li, L in enumerate(W):
    toks = []; cur = []
    for k, x in enumerate(L):
        w = x[0]
        if w.startswith('«') and cur: toks.append(cur); cur = []
        if CL and (li, k) == CL and cur: toks.append(cur); cur = []
        cur.append(k)
        nchar = sum(len(L[j][0]) for j in cur)
        if re.search(r'[.,:;?!…»]$', w) or len(cur) >= 4 or nchar > 22 or (CL and (li, k) == (CL[0], CL[1] + 1)):
            toks.append(cur); cur = []
    if cur: toks.append(cur)
    mt = []
    for ch in toks:   # pas de mot isolé, sauf le mot fort
        if mt and len(ch) == 1 and len(mt[-1]) <= 4 and not re.search(r'[.,:;?!…»]$', L[mt[-1][-1]][0]) and not (CL and (li, ch[0]) == CL):
            mt[-1] = mt[-1] + ch
        else: mt.append(ch)
    for ch in mt:
        words = []; q = inq
        for k in ch:
            w, s, e = L[k]
            if '«' in w: inq = True; q = True
            kk = 1 if clean(w) in KEY else 0
            slam = 1 if CL and (li, k) == CL else 0
            words.append([w, s, e, kk, slam])
            if '»' in w: inq = False
        CH.append({'w': words, 'q': q, 't0': words[0][1], 't1': words[-1][2], 'slam': any(x[4] for x in words)})
for a, b in zip(CH, CH[1:]):
    a['hide'] = min(b['t0'] - 0.12, max(a['t1'] + 0.9, a['w'][-1][1] + 0.3))
CH[-1]['hide'] = VEND + 0.9

X = [{'t': 0 if i == 0 else round(at(a) - 0.25, 3), 'img': img, 'cam': cam, 'fx': fx or {}} for i, (a, img, cam, fx) in enumerate(SHOTS)]
for s in X:
    if 'shake' in s['fx']: s['fx']['shake'] = at(s['fx']['shake'])
X.sort(key=lambda s: s['t'])
data = {'DUR': round(DUR, 3), 'VEND': round(VEND, 3), 'G': round(GSTART, 3), 'H': round(HSTART, 3), 'TAG': TAG, 'chunks': CH, 'shots': X,
        'end': END, 'climax': at(CLIMAX) if CLIMAX else None, 'lastword': W[-1][-1][1]}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
print('DUR', round(DUR, 2), 'VEND', round(VEND, 2), 'chunks', len(CH), 'shots', len(X), 'pauses ajoutées', round(sum(d for c, d, *_ in CUTS), 2))
