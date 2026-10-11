# Moteur commun reels compagnons « apparition » (9:16). Lancer dans le dossier de travail (cfg.py, script.txt, align_lines.json, voix_t.wav).
import json, re, subprocess, numpy as np, soundfile as sf
exec(open('cfg.py', encoding='utf-8').read())
LINES = json.load(open('align_lines.json'))
v, SR = sf.read('voix_t.wav')
if v.ndim > 1: v = v.mean(1)
VLEN = len(v) / SR
LEAD = 0.35; FINAL_SIL = 1.2; RETAIN_HOLD = 3.4; SUB_CARD = 3.0

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
HSTART = VEND + FINAL_SIL + RETAIN_HOLD; DUR = HSTART + SUB_CARD
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
    if isinstance(a, (int, float)) and not isinstance(a, bool): return W[int(a)][0][1]
    return W[a[0]][widx(a[0], a[1], a[2] if len(a) > 2 else 1)][1]

# ---- scènes « apparition » ----
def norm(w):
    w = w.lower().replace('’', "'").replace('*', '').replace('_', '')
    return re.sub(r"[^a-z0-9àâäéèêëîïôöùûüçœ']", '', w)
ALLW = [x for L in W for x in L]
SC = []
for i, sc in enumerate(SCENES):
    s = 0.0 if i == 0 else at(sc['at']) - 0.2
    SC.append(dict(sc, s=round(s, 3)))
for a, b in zip(SC, SC[1:]): a['e'] = b['s']
SC[-1]['e'] = round(HSTART, 3)
for sc in SC:
    pool = [x for x in ALLW if sc['s'] - 0.05 <= x[1] < sc['e']]
    k = 0; last = sc['s'] + 0.1; blocks = []
    for bl in sc.get('blocks', []):
        st, txt = bl[0], bl[1]; size = bl[2] if len(bl) > 2 else None
        ws = []
        toks = []
        for tok in txt.split(' '):
            if not tok: continue
            if toks and re.fullmatch(r"[?!:;»…]+", tok): toks[-1] += ' ' + tok; continue
            if toks and toks[-1] == '«': toks[-1] = '« ' + tok; continue
            toks.append(tok)
        for tok in toks:
            n = norm(tok); t = None
            if 'ﷺ' in tok and k < len(pool) and norm(pool[k][0]) in ('paix', 'que'):
                for j in range(k, min(k + 11, len(pool))):
                    if norm(pool[j][0]) == 'lui': t = pool[k][1]; k = j + 1; break
                if t is not None: last = t; ws.append([tok, round(t, 3)]); continue
            for j in range(k, min(k + 6, len(pool))):
                if n and (norm(pool[j][0]) == n or norm(pool[j][0]).split("'")[-1] == n.split("'")[-1]):
                    t = pool[j][1]; k = j + 1; break
            if t is None: t = last + 0.08
            last = t; ws.append([tok, round(t, 3)])
        delay = bl[3] if len(bl) > 3 else 0
        if delay: ws = [[w, round(t + delay, 3)] for w, t in ws]
        blocks.append({'st': st, 'size': size, 'w': ws})
    sc['blocks'] = blocks
    if 'shake' in sc and sc['shake']: sc['shake'] = round(at(sc['shake']), 3)
    sc.pop('at', None)
data = {'DUR': round(DUR, 3), 'VEND': round(VEND, 3), 'H': round(HSTART, 3), 'TAG': TAG, 'scenes': SC}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
print('DUR', round(DUR, 2), 'VEND', round(VEND, 2), 'scènes', len(SC), 'pauses ajoutées', round(sum(d for c, d, *_ in CUTS), 2))
for sc in SC: print(f"{sc['s']:6.2f}-{sc['e']:6.2f} {sc.get('kind','')}:{sc.get('img','')} | " + ' / '.join(' '.join(f'{w}@{t:.1f}' for w, t in b['w']) for b in sc['blocks'])[:150])
