# Rappel commun : calage mot à mot + pauses minimales (bible §3, jamais de raccourcissement) -> timeline.json + voix_p.wav
# usage : python3 prep.py <dossier de travail>  (contient cfg.py, voice.wav 44,1 kHz mono, words.json de asr.mjs)
import sys, json, re, unicodedata, difflib, importlib.util, numpy as np, soundfile as sf
W = sys.argv[1]
spec = importlib.util.spec_from_file_location('cfg', W + '/cfg.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
OFF, TAIL = 0.40, 1.20
MIN = {'comma': .35, 'end': .70, 'quote': 1.0, 'last': 1.2}

def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r"[^a-z0-9']", '', s.replace('’', "'"))

x, sr = sf.read(W + '/voice.wav'); x = x if x.ndim == 1 else x.mean(1)
# --- silences (trames de 10 ms, seuil relatif)
hop = int(sr * .01); n = len(x) // hop
rms = np.sqrt(np.array([np.mean(x[i*hop:(i+1)*hop]**2) for i in range(n)]) + 1e-12)
db = 20*np.log10(rms/rms.max()); quiet = db < -38
sil = []; i = 0
while i < n:
    if quiet[i]:
        j = i
        while j < n and quiet[j]: j += 1
        if (j-i) >= 8: sil.append((i*.01, j*.01))
        i = j
    else: i += 1
speech = [t for t in range(n) if not quiet[t]]
VSTART, VEND = speech[0]*.01, (speech[-1]+1)*.01
# --- jetons du texte dit + temps Whisper
toks = []
for t in C.VOICE.split(' '):
    if not t: continue
    if norm(t) == '' and t.strip() == '«': toks.append(t)          # « colle au mot suivant
    elif norm(t) == '' and toks: toks[-1] += '\u00a0' + t           # ponctuation seule -> mot précédent
    elif toks and toks[-1] == '«': toks[-1] += '\u00a0' + t
    else: toks.append(t)
wh = []
for c in json.load(open(W + '/words.json'))['chunks']:      # recolle « c » + « 'est » ; écarte les temps qui reculent
    if wh and c['text'].startswith(("'", '’')): wh[-1]['text'] += c['text']; continue
    c = dict(c); c['timestamp'] = list(c['timestamp'])
    lastt = max([w['timestamp'][0] for w in wh if w['timestamp'][0] is not None], default=-1)
    if c['timestamp'][0] is not None and c['timestamp'][0] < lastt: c['timestamp'][0] = None
    wh.append(c)
wn = [norm(c['text']) for c in wh]; tn = [norm(t) for t in toks]
T = [None]*len(toks)
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tn, wn, autojunk=False).get_opcodes():
    if op == 'equal':
        for q in range(i2-i1): T[i1+q] = wh[j1+q]['timestamp'][0]
    elif op == 'replace':                # mots mal transcrits (« biens faisant ») : appariés dans l'ordre
        j = j1
        for q in range(i1, i2):          # meilleur mot proche (ordre conservé)
            best = max(range(j, j2), key=lambda c: difflib.SequenceMatcher(None, tn[q], wn[c]).ratio() + difflib.SequenceMatcher(None, tn[q], wn[c] + (wn[c+1] if c+1 < j2 else '')).ratio()*.5, default=None)
            if best is None: break
            if difflib.SequenceMatcher(None, tn[q], wn[best] + (wn[best+1] if best+1 < j2 else '')).ratio() > .5 or difflib.SequenceMatcher(None, tn[q], wn[best]).ratio() > .5:
                T[q] = wh[best]['timestamp'][0]; j = best + 1
for i in range(1, len(T)):
    if T[i] is not None and any(T[j] is not None and T[j] > T[i] for j in range(i)): T[i] = None
for i in range(len(toks)):              # interpolation des jetons non reconnus
    if T[i] is None:
        p = max([j for j in range(i) if T[j] is not None], default=None); nx = min([j for j in range(i+1, len(toks)) if T[j] is not None], default=None)
        T[i] = VSTART if p is None else (T[p] + .25 if nx is None else T[p] + (T[nx]-T[p])*(i-p)/(nx-p))
for i in range(len(toks)):              # un mot qui « commence » dans un silence commence à la fin de ce silence
    for a, b in sil:
        if a <= T[i] < b - .02: T[i] = b - .02
    if i == 0: T[i] = max(T[i], VSTART - .02)
# --- pauses : allonger jusqu'au minimum (jamais raccourcir)
ends = [i for i in range(len(toks)-1) if re.search(r'[.!?…]\s*»?$', toks[i])]
last_sent = ends[-1] if ends else None
INS = []
for i in range(len(toks)-1):
    t = toks[i]; nxt = toks[i+1]
    if nxt.startswith('«') or t.endswith(':') and nxt.startswith('«'): kind = 'quote'
    elif i == last_sent: kind = 'last'
    elif re.search(r'[.!?…]\s*»?$', t) or t.endswith(':'): kind = 'end'
    elif re.search(r'[,;]$', t): kind = 'comma'
    else: continue
    lo, hi = T[i], T[i+1]
    cand = [(b-a, a, b) for a, b in sil if a >= lo - .05 and b <= hi + .05]
    if cand: d, a, b = max(cand); c = (a+b)/2
    else: d, c = 0.0, hi - .03
    add = MIN[kind] - d
    if add > .005: INS.append((c, round(add, 3), kind, t))
def N(t): return OFF + t + sum(a for p, a, *_ in INS if p < t)
parts, last = [], 0
for p, a, *_ in INS:
    k = int(p*sr); parts += [x[last:k], np.zeros(int(round(a*sr)))]; last = k
parts.append(x[last:int((VEND + .05)*sr)])
v = np.concatenate([np.zeros(int(OFF*sr))] + parts + [np.zeros(int(TAIL*sr))])
sf.write(W + '/voix_p.wav', v, sr)
VOICE_END = len(v)/sr
# --- jetons affichés -> temps (alignement global sur le texte dit).
# « MOT|ancre » : prend le temps du mot dit « ancre » ; « MOT|= » : même temps que le précédent ; « *MOT » : mot clé ; ligne « ~… » : petite
flat, scenes = [], []
for s in C.SCENES:
    lines = []
    for ln in s['lines']:
        small = ln.startswith('~'); ln = ln.lstrip('~'); ws = []
        for d in ln.split(' '):
            if not d: continue
            disp, _, anc = d.partition('|'); key = disp.startswith('*'); disp = disp.lstrip('*')
            w = [disp, None, key]; ws.append(w); flat.append((w, anc))
        lines.append({'small': small, 'w': ws})
    scenes.append({**{k: v for k, v in s.items() if k != 'lines'}, 'lines': lines})
dn = [('=' if anc == '=' else norm(anc or w[0])) for w, anc in flat]
for a_, b_, k in difflib.SequenceMatcher(None, dn, tn, autojunk=False).get_matching_blocks():
    for q in range(k): flat[a_+q][0][1] = N(T[b_+q])
for i, (w, anc) in enumerate(flat):
    if w[1] is None:
        if anc == '=' and i: w[1] = flat[i-1][0][1]; continue
        p = max([j for j in range(i) if flat[j][0][1] is not None], default=None); nx = min([j for j in range(i+1, len(flat)) if flat[j][0][1] is not None], default=None)
        w[1] = N(T[0]) if p is None else (flat[p][0][1] + .2 if nx is None else flat[p][0][1] + (flat[nx][0][1]-flat[p][0][1])*(i-p)/(nx-p))
for i, (w, _) in enumerate(flat):
    if i and w[1] < flat[i-1][0][1]: w[1] = flat[i-1][0][1]
    w[1] = round(w[1], 3)
for k, s in enumerate(scenes):
    t0 = min(w[1] for ln in s['lines'] for w in ln['w'])
    s['t0'] = round(OFF - .2 if k == 0 else t0 - .15, 3)
    s['last'] = max(w[1] for ln in s['lines'] for w in ln['w'])
for k, s in enumerate(scenes): s['t1'] = scenes[k+1]['t0'] if k+1 < len(scenes) else VOICE_END
END1, END2 = VOICE_END, VOICE_END + 2.6
DUR = round(END2 + 2.8, 2)
json.dump({'ID': C.ID, 'TAG': C.TAG, 'DUR': DUR, 'END1': END1, 'END2': END2, 'VOICE_END': VOICE_END, 'S': scenes,
           'SOURCES': C.SOURCES}, open(W + '/timeline.json', 'w'), ensure_ascii=False, indent=1)
print(C.ID, 'voix', round(len(x)/sr, 2), '-> avec pauses', round(VOICE_END, 2), 's · vidéo', DUR, 's')
for p, a, k, t in INS: print(f'  +{a:.2f}s ({k}) après « {t} » à {p:.2f}')
for s in scenes: print('  ', s['kind'], round(s['t0'], 2), '→', round(s['t1'], 2), ' '.join(w[0] for ln in s['lines'] for w in ln['w'])[:70])
