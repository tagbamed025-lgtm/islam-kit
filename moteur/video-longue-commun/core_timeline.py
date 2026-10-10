# Moteur commun des vidéos du vendredi : lit cfg.py du dossier courant.
import json, re, subprocess, os, numpy as np, soundfile as sf
from PIL import Image as _I
exec(open('cfg.py', encoding='utf-8').read())          # CHAP_AFTER, NAMES, HOOK_LINE, TITLE_CFG, EXTRA, KEY, BAND, shots()

LINES = json.load(open('align_lines.json'))
v, SR = sf.read('audio/voix_t.wav')
if v.ndim > 1: v = v.mean(1)
VLEN = len(v) / SR
LEAD = 0.6; END_CARD = 5.6; SUB_CARD = 3.6; CHAP_GAP = 3.3

r = subprocess.run(['ffmpeg', '-i', 'audio/voix_t.wav', '-af', 'silencedetect=noise=-38dB:d=0.05', '-f', 'null', '-'],
                   capture_output=True, text=True).stderr
S = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
E = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = [(s, e) for s, e in zip(S, E) if e < VLEN - 0.05 and s > 0.05]

FLAT = [(li, wi, w, s, e) for li, L in enumerate(LINES) for wi, (w, s, e) in enumerate(L)]
def widx(li, prefix, n=1):
    k = 0
    for i, x in enumerate(LINES[li]):
        ww = x[0].strip('«»,.…:;!? \u00a0').lower().replace('\u2019', "'")
        if ww.startswith(prefix.lower()) or ("'" in ww and "'" not in prefix and ww.split("'")[-1].startswith(prefix.lower())):
            k += 1
            if k == n: return i
    raise Exception(f'mot {prefix} absent de la ligne {li}')
last = lambda li: len(LINES[li]) - 1

SPECIAL = {}
for li in CHAP_AFTER: SPECIAL[(li, last(li))] = CHAP_GAP
SPECIAL[(HOOK_LINE, last(HOOK_LINE))] = 1.7 if TITLE_CFG['mode'] == 'words' else 3.4
if TITLE_CFG['mode'] == 'words':
    TL = TITLE_CFG['line']; k_end = widx(TL, TITLE_CFG['end'])
    SPECIAL[(TL, k_end)] = max(1.5, SPECIAL.get((TL, k_end), 0))
for li, wp, val in EXTRA:                           # (ligne, préfixe du mot ou None = fin de ligne, pause totale)
    SPECIAL[(li, last(li) if wp is None else widx(li, wp))] = val
SPECIAL.setdefault((len(LINES) - 2, last(len(LINES) - 2)), 1.2)   # avant la dernière phrase

def target(i):
    li, wi, w, s, e = FLAT[i]
    if (li, wi) in SPECIAL: return SPECIAL[(li, wi)]
    if FLAT[i + 1][2].startswith('«'): return 1.0
    if re.search(r'[.?!…»]$', w): return 0.7
    if w.endswith(',') or w.endswith(':'): return 0.35
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
    if best is not None and bd < 0.7:
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
VEND_CARD = VEND + 1.2; DUR = VEND_CARD + END_CARD + SUB_CARD
voice = np.concatenate([voice, np.zeros(int(DUR * SR) + SR)])[:int(DUR * SR)]
sf.write('audio/voice_final.wav', voice, SR)

def snap(s, e):
    for a, b in SIL:
        if a - .12 <= s < b: s = b
        if a < e <= b + .12: e = a
    return s, max(e, s + .06)
LINES = [[[w, *snap(s, e)] for w, s, e in L] for L in LINES]
W = [[[w, round(NT(s), 3), round(NT(e), 3)] for w, s, e in L] for L in LINES]
for L in W:
    for x in L: x[1] = min(x[1], VEND); x[2] = min(x[2], VEND + .2)

def ls(i): return W[i][0][1]
def le(i): return W[i][-1][2]
def _cut(i, wi): return [x for x in CUTS if x[2] == i and x[3] == wi][0]
def pz(i, wp=None):
    wi = last(i) if wp is None else (wp if isinstance(wp, int) else widx(i, wp)); return NT(_cut(i, wi)[0] - 1e-4)
def pzlen(i, wp=None):
    wi = last(i) if wp is None else (wp if isinstance(wp, int) else widx(i, wp)); c = _cut(i, wi); return c[1] + c[4]
def wt(i, word, n=1): return W[i][widx(i, word, n)][1]

# ---------- titre ----------
if TITLE_CFG['mode'] == 'words':
    TL = TITLE_CFG['line']
    TITLE = {'t0': wt(TL, TITLE_CFG['h']) - .1, 'th': wt(TL, TITLE_CFG['h']), 'tn': wt(TL, TITLE_CFG['n']),
             't1': pz(TL, TITLE_CFG['end']) + pzlen(TL, TITLE_CFG['end']) - .35}
    TITLE_SPAN = (TITLE['th'], pz(TL, TITLE_CFG['end']))
else:
    a = pz(HOOK_LINE); TITLE = {'t0': a + .2, 'th': a + .3, 'tn': a + .8, 't1': a + pzlen(HOOK_LINE) - .6}
    TITLE_SPAN = (-1, -1)
HOOK = [pz(HOOK_LINE) - .0, pzlen(HOOK_LINE)]

# ---------- sous-titres ----------
CH = []; inq = False
for li, L in enumerate(W):
    toks = []; band_from = BAND.get(li)
    if isinstance(band_from, str): band_from = widx(li, band_from)
    cur = []
    for k, x in enumerate(L):
        w = x[0]
        if TITLE_SPAN[0] - .05 <= x[1] < TITLE_SPAN[1]: continue
        if band_from is not None and k == band_from and cur: toks.append(cur); cur = []
        if w.startswith('«') and cur: toks.append(cur); cur = []
        cur.append(k)
        nchar = sum(len(L[j][0]) for j in cur); lb = band_from is not None and k >= band_from
        if re.search(r'[.,:;?!…»]$', w) or len(cur) >= (6 if lb else 4) or nchar > (34 if lb else 26):
            toks.append(cur); cur = []
    if cur: toks.append(cur)
    mt = []
    for ch in toks:
        if mt and len(ch) == 1 and len(mt[-1]) <= 4 and not re.search(r'[.,:;?!…»]$', L[mt[-1][-1]][0]) \
           and not (band_from is not None and ch[0] == band_from):
            mt[-1] = mt[-1] + ch
        else: mt.append(ch)
    for ch in mt:
        band = band_from is not None and ch[0] >= band_from
        words = []
        for k in ch:
            w, s, e = L[k]
            if '«' in w: inq = True
            kk = 1 if w.lower().replace(' ', ' ').split(' ')[0].strip('«»,.…:;!? ') in KEY else 0
            words.append([w, s, e, kk]); q = inq
            if '»' in w: inq = False
        lines = [words]
        if band and len(words) > 3: m = (len(words) + 1) // 2; lines = [words[:m], words[m:]]
        CH.append({'lines': lines, 'band': band, 'quote': q or any('«' in x[0] for x in words),
                   't0': words[0][1], 't1': words[-1][2]})
for a, b in zip(CH, CH[1:]):
    a['hide'] = max(min(b['t0'] - 0.25, a['t1'] + 0.7), a['lines'][-1][-1][1] + 0.3)
CH[-1]['hide'] = min(CH[-1]['t1'] + 1.4, VEND + 1.0)

CHAP = sorted([[pz(li) - 0.3, ls(li + 1) - 0.3, num, NAMES[num]] for li, num in CHAP_AFTER.items()])

# ---------- plans ----------
X = []
def sh(t, img, cam=None, fx=None):
    fx = dict(fx or {})
    if img == 'CUT':
        w0, h0 = _I.open(f"cut/{fx['obj']}.png").size; fx['h'] = round(fx['w'] * h0 / w0)
    X.append({'t': round(t, 3), 'img': img, 'cam': cam, 'fx': fx})
shots()
X.sort(key=lambda s: s['t'])
sh(VEND_CARD, 'END'); sh(VEND_CARD + END_CARD, 'SUB')

data = {'DUR': DUR, 'VEND': VEND_CARD, 'chunks': CH, 'chap': CHAP, 'title': TITLE, 'shots': X, 'rec': None, 'hook': HOOK,
        'pauses': [[NT(c - 1e-4), d + nat, li, wi] for c, d, li, wi, nat in CUTS]}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
print('DUR', round(DUR, 2), 'chunks', len(CH), 'shots', len(X))
for c in CHAP: print('chap', round(c[0], 2), round(c[1], 2), c[3])
print('title', {k: round(v, 2) for k, v in TITLE.items()})
