import json, re, subprocess, os, numpy as np, soundfile as sf

LINES = json.load(open('align_lines.json'))
v, SR = sf.read('audio/voix_t.wav')
if v.ndim > 1: v = v.mean(1)
VLEN = len(v) / SR

# ---------- récitation (Alafasy, Maryam 19:1-4) ----------
REC_FILE = 'audio/recitation.wav'
REC = sf.info(REC_FILE).duration if os.path.exists(REC_FILE) else 0.0
REC_LINE = 16                     # la récitation suit « … le début de la sourate Maryam. »

LEAD = 0.6
END_CARD = 5.6; SUB_CARD = 3.6
CHAP_GAP = 3.3                    # silence total quand une carte de chapitre s'affiche

# ---------- silences réels de la voix ----------
r = subprocess.run(['ffmpeg', '-i', 'audio/voix_t.wav', '-af', 'silencedetect=noise=-38dB:d=0.05', '-f', 'null', '-'],
                   capture_output=True, text=True).stderr
S = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
E = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = [(s, e) for s, e in zip(S, E) if e < VLEN - 0.05 and s > 0.05]

# ---------- frontières de mots + cible de pause (bible §3) ----------
FLAT = [(li, wi, w, s, e) for li, L in enumerate(LINES) for wi, (w, s, e) in enumerate(L)]
CHAP_AFTER = {3: 'I', 6: 'II', 10: 'III', 14: 'IV', 20: 'V', 25: 'VI', 28: 'VII'}
SPECIAL = {}                      # (li, wi) -> pause totale voulue
for li in CHAP_AFTER: SPECIAL[(li, len(LINES[li]) - 1)] = CHAP_GAP
SPECIAL[(1, len(LINES[1]) - 1)] = 1.7          # fin de l'accroche -> suspense avant le nom
k_talib = [i for i, x in enumerate(LINES[2]) if x[0].startswith('Talib')][0]
SPECIAL[(2, k_talib)] = 1.5                    # respiration après le titre
SPECIAL[(REC_LINE, len(LINES[REC_LINE]) - 1)] = (1.0 + REC + 1.2) if REC else 1.4
SPECIAL[(26, len(LINES[26]) - 1)] = 1.1        # après « Vous êtes en sécurité dans mon pays. »
SPECIAL[(29, len(LINES[29]) - 1)] = 1.2        # avant la dernière phrase

def target(i):
    li, wi, w, s, e = FLAT[i]
    if (li, wi) in SPECIAL: return SPECIAL[(li, wi)]
    nxt = FLAT[i + 1][2]
    if nxt.startswith('«'): return 1.0                    # avant une citation
    if re.search(r'[.?!…»]$', w): return 0.7              # fin de phrase
    if w.endswith(',') or w.endswith(':'): return 0.35   # virgule / deux-points
    return None

used = set(); CUTS = []
for i in range(len(FLAT) - 1):
    tg = target(i)
    if tg is None: continue
    a, b = FLAT[i][4], FLAT[i + 1][3]
    g = (min(a, b) + max(a, b)) / 2
    best = None; bd = 9
    for j, (s, e) in enumerate(SIL):
        if j in used: continue
        dist = 0 if s <= g <= e else min(abs(g - s), abs(g - e))
        if dist < bd: bd, best = dist, j
    if best is not None and bd < 0.7:
        used.add(best); s, e = SIL[best]; nat = e - s; at = (s + e) / 2
    else:
        nat = 0.0; at = g
    extra = max(0.0, tg - nat)
    CUTS.append((at, extra, FLAT[i][0], FLAT[i][1], nat))
CUTS.sort()

def NT(t): return LEAD + t + sum(d for c, d, *_ in CUTS if c < t)

# ---------- piste voix finale (silences allongés, jamais raccourcis) ----------
parts = [np.zeros(int(LEAD * SR))]; prev = 0
for c, d, *_ in CUTS:
    ci = int(c * SR); parts.append(v[prev:ci]); parts.append(np.zeros(int(d * SR))); prev = ci
parts.append(v[prev:])
voice = np.concatenate(parts)
# fin de la voix réelle (dernier son > -45 dB) + silence final 1,2 s
env = np.abs(voice); thr = 10 ** (-45 / 20)
VEND = (np.nonzero(env > thr)[0][-1]) / SR
VEND_CARD = VEND + 1.2
DUR = VEND_CARD + END_CARD + SUB_CARD
voice = np.concatenate([voice, np.zeros(int(DUR * SR) + SR)])[:int(DUR * SR)]
sf.write('audio/voice_final.wav', voice, SR)

def snap(s, e):
    for a, b in SIL:
        if a - .02 <= s < b: s = b
        if a < e <= b + .02: e = a
    return s, max(e, s + .06)
LINES = [[[w, *snap(s, e)] for w, s, e in L] for L in LINES]
W = [[[w, round(NT(s), 3), round(NT(e), 3)] for w, s, e in L] for L in LINES]
# horodatages Whisper parfois au-delà de la vraie fin : on borne
for L in W:
    for x in L:
        x[1] = min(x[1], VEND); x[2] = min(x[2], VEND + .2)

def ls(i): return W[i][0][1]
def le(i): return W[i][-1][2]
def pz(i, wi=None):
    wi = len(LINES[i]) - 1 if wi is None else wi
    c = [x for x in CUTS if x[2] == i and x[3] == wi][0]
    return NT(c[0] - 1e-4)
def pzlen(i, wi=None):
    wi = len(LINES[i]) - 1 if wi is None else wi
    c = [x for x in CUTS if x[2] == i and x[3] == wi][0]
    return c[1] + c[4]
def wt(i, word, n=1):
    k = 0
    for w, s, e in W[i]:
        if w.strip('«»,.…:;!?  ').lower().startswith(word.lower()):
            k += 1
            if k == n: return s
    raise Exception(f'mot {word} absent de la ligne {i}')

# ---------- sous-titres (découpage automatique) ----------
KEY = {'roi', 'pleurer', 'réfugiés.', 'versets,', 'seul', 'discours', 'persécutés.', 'justice', "d'abyssinie.", 'sécurité.',
       'quraysh', 'cadeaux', 'évêques.', 'livrer', 'insensés,', 'écouter.', 'idoles,', 'faible.', 'droiture', 'sincérité.',
       'vérité,', 'prier,', 'pauvres.', 'choisi.', "d'allah", 'maryam.', 'barbe.', 'livres.', 'lumière.', 'piège.',
       "'issa,", 'marie.', 'perdre.', 'serviteur', 'pure.', 'bâton,', 'sécurité', 'quraysh.', 'vides.', 'protégés,', 'sort'}
BAND = {12: ('où', None), 20: ('Il', None), 26: ('«', None), 30: ('a', None)}   # bandeau émeraude : à partir de ce mot
TITLE_SPAN = (wt(2, 'Cet'), pz(2, k_talib))
CH = []; inq = False
for li, L in enumerate(W):
    toks = []
    band_from = None
    if li in BAND:
        key = BAND[li][0]
        idx = [k for k, x in enumerate(L) if x[0].replace(' ', ' ').split(' ')[-1 if key != '«' else 0].startswith(key)
               or x[0].startswith(key)]
        if li == 30: idx = [k for k, x in enumerate(L) if x[0] == 'a']
        band_from = idx[-1] if li in (12,) else idx[0]
        if li == 12: band_from = [k for k, x in enumerate(L) if x[0] == 'où'][0]
    cur = []
    def flush():
        global cur
        if cur: toks.append(cur)
        cur = []
    for k, x in enumerate(L):
        w = x[0]
        if TITLE_SPAN[0] - .05 <= x[1] < TITLE_SPAN[1]: continue        # mots couverts par la carte titre
        if band_from is not None and k == band_from: flush()
        if w.startswith('«') and cur: flush()
        cur.append(k)
        nchar = sum(len(L[j][0]) for j in cur)
        last_band = band_from is not None and k >= band_from
        lim = 6 if last_band else 4
        if re.search(r'[.,:;?!…»]$', w) or len(cur) >= lim or nchar > (34 if last_band else 26): flush()
    flush()
    mt = []
    for ch in toks:
        if mt and len(ch) == 1 and len(mt[-1]) <= 4 and not re.search(r'[.,:;?!…»]$', L[mt[-1][-1]][0]) \
           and not (band_from is not None and ch[0] == band_from):
            mt[-1] = mt[-1] + ch
        else: mt.append(ch)
    toks = mt
    for ch in toks:
        band = band_from is not None and ch[0] >= band_from
        words = []
        for k in ch:
            w, s, e = L[k]
            if '«' in w: inq = True
            kk = 1 if w.lower().replace(' ', ' ').split(' ')[0] in KEY else 0
            words.append([w, s, e, kk])
            q = inq
            if '»' in w: inq = False
        lines = [words]
        if band and len(words) > 3:                                      # bandeau sur 2 lignes
            m = (len(words) + 1) // 2; lines = [words[:m], words[m:]]
        CH.append({'lines': lines, 'band': band, 'quote': q or any('«' in x[0] for x in words),
                   't0': words[0][1], 't1': words[-1][2]})
for a, b in zip(CH, CH[1:]):
    a['hide'] = max(min(b['t0'] - 0.25, a['t1'] + 0.7), a['lines'][-1][-1][1] + 0.3)
CH[-1]['hide'] = min(CH[-1]['t1'] + 1.4, VEND + 1.0)

# ---------- chapitres & titre ----------
NAMES = {'I': 'LA FUITE', 'II': 'LA DÉLÉGATION', 'III': 'LE DISCOURS', 'IV': 'LA RÉCITATION',
         'V': 'LE PIÈGE', 'VI': 'LA PROTECTION', 'VII': 'CE QUI RESTE'}
CHAP = []
for li, num in CHAP_AFTER.items():
    a = pz(li) - 0.3; b = ls(li + 1) - 0.3
    CHAP.append([a, b, num, NAMES[num]])
CHAP.sort()
TITLE = {'t0': wt(2, 'Cet') - .1, 'th': wt(2, 'Cet'), 'tn': wt(2, "Ja'far"), 't1': pz(2, k_talib) + pzlen(2, k_talib) - .35}

# ---------- récitation ----------
RECD = None
if REC:
    r0 = pz(REC_LINE) + 1.0
    vs = json.load(open('rec_verses.json'))          # temps des versets dans la récitation
    rv, rsr = sf.read(REC_FILE)
    if rv.ndim > 1: rv = rv.mean(1)
    assert rsr == SR, (rsr, SR)
    vv, _ = sf.read('audio/voice_final.wav'); i0 = int(r0 * SR); vv[i0:i0 + len(rv)] += rv[:len(vv) - i0]
    sf.write('audio/voice_final.wav', vv, SR)
    RECD = {'t0': r0 - .9, 't1': r0 + REC + .9, 'a0': r0,
            'verses': [dict(x, s=r0 + x['s'], e=r0 + x['e']) for x in vs]}

# ---------- plans : [début, image, caméra (fx0,fy0,s0, fx1,fy1,s1), effets] ----------
X = []
from PIL import Image as _I
def sh(t, img, cam=None, fx=None):
    fx = fx or {}
    if img == 'CUT':
        w0, h0 = _I.open(f"cut/{fx['obj']}.png").size; fx['h'] = round(fx['w'] * h0 / w0)
    X.append({'t': round(t, 3), 'img': img, 'cam': cam, 'fx': fx})
# ACCROCHE
sh(0,                  'J3',  [.70, .52, 1.0, .74, .50, 1.22], {'flicker': [.86, .30], 'dust': .5})
sh(wt(0, 'pleurer') - .25, 'J12', [.46, .50, 1.05, .46, .46, 1.32], {'flicker': [.66, .72], 'bloom': [.46, .45, wt(0, 'pleurer') + .3]})
sh(wt(0, 'devant') - .2, 'J2',  [.40, .55, 1.25, .48, .52, 1.05], {'dust': .6})
sh(ls(1) - .15,        'J10', [.55, .55, 1.05, .52, .55, 1.35], {'flicker': [.02, .35], 'sweep': ls(1) + .8})
sh(wt(1, 'récités') - .15, 'J6', [.35, .60, 1.4, .30, .55, 1.2], {'flicker': [.76, .35]})
sh(pz(1) + .3,         'J2',  [.42, .50, 1.35, .42, .48, 1.15], {'dark': .45, 'dust': .5})
sh(TITLE['t1'] - .1,   'J2',  [.30, .45, 1.2, .55, .45, 1.2], {'dust': .5})
sh(ls(3) - .15,        'J3',  [.60, .50, 1.25, .40, .50, 1.25], {'flicker': [.86, .30], 'dust': .4})
# I. LA FUITE
sh(pz(3) + .1,         'J7',  [.50, .60, 1.05, .50, .62, 1.3], {'dust': .7})
sh(wt(4, 'Le', 1) - .2 if False else wt(4, 'Prophète') - .45, 'MAP_RS', None,
   {'route': 'abyssinie', 'r0': wt(4, 'partir'), 'r1': wt(4, "d'Abyssinie") + .6})
sh(ls(5) - .15,        'J2',  [.25, .55, 1.6, .38, .52, 1.4], {'dust': .5})
sh(ls(6) - .15,        'J1',  [.62, .45, 1.3, .55, .45, 1.05], {'flicker': [.20, .22], 'bloom': [.80, .40, wt(6, 'sécurité')]})
# II. LA DÉLÉGATION
sh(pz(6) + .1,         'J7',  [.88, .40, 1.6, .85, .42, 1.8], {'dark': .25, 'shake': wt(7, 'Quraysh')})
sh(ls(8) - .15,        'J5',  [.40, .55, 1.05, .45, .55, 1.3], {'dust': .5})
sh(wt(8, 'Amr') - .15, 'J5',  [.30, .55, 1.5, .55, .55, 1.5], {'dust': .4})
sh(wt(8, 'chargés') - .2, 'CUT', None, {'obj': 'J4', 'anim': 'drop', 'w': 1250, 'y': 440})
sh(ls(9) - .15,        'J3',  [.72, .50, 1.5, .72, .48, 1.75], {'flicker': [.86, .30]})
sh(wt(9, 'sans') - .2, 'J14', [.40, .40, 1.3, .40, .42, 1.55], {'flicker': [.92, .40]})
sh(ls(10) - .15,       'J2',  [.50, .55, 1.15, .50, .52, 1.35], {'desat': .35, 'dust': .4})
# III. LE DISCOURS
sh(pz(10) + .1,        'J3',  [.55, .55, 1.0, .65, .52, 1.25], {'flicker': [.86, .30], 'dust': .4})
sh(wt(11, 'Il', 1) - .2, 'J5', [.72, .48, 1.6, .72, .45, 1.9], {'dark': .2})
sh(ls(12) - .15,       'J9',  [.50, .45, 1.15, .50, .40, 1.35], {'flicker': [.06, .62], 'dust': .5})
sh(wt(12, 'Il', 1) - .2, 'J7', [.45, .70, 1.25, .50, .62, 1.05], {'desat': .3, 'dust': .7})
sh(wt(12, 'où') - .2,  'J7',  [.85, .45, 1.6, .86, .42, 1.95], {'desat': .3, 'shake': wt(12, 'dévorait')})
sh(ls(13) - .15,       'J6',  [.50, .55, 1.05, .45, .58, 1.3], {'flicker': [.76, .35], 'bloom': [.76, .32, wt(13, 'levé')]})
sh(wt(13, 'Il', 2) - .2, 'CUT', None, {'obj': 'J8', 'anim': 'slide', 'w': 900, 'y': 430})
sh(wt(13, 'prier') - .2, 'CUT', None, {'obj': 'J9', 'anim': 'rise', 'w': 640, 'y': 440})
sh(wt(13, 'donner') - .2, 'J8', [.80, .60, 1.5, .85, .60, 1.7])
sh(ls(14) - .15,       'J1',  [.40, .55, 1.25, .60, .55, 1.25], {'flicker': [.20, .22]})
sh(wt(14, 'Et', 1) - .2, 'J3', [.74, .50, 1.3, .74, .48, 1.6], {'flicker': [.86, .30], 'bloom': [.74, .45, wt(14, 'choisi')]})
# IV. LA RÉCITATION
sh(pz(14) + .1,        'J3',  [.50, .50, 1.05, .70, .50, 1.3], {'dark': .2, 'flicker': [.86, .30]})
sh(wt(15, '«') - .2 if False else ls(15) + 1.2, 'J6b', [.50, .55, 1.1, .50, .55, 1.35], {'flicker': [.36, .10]})
sh(ls(16) - .15,       'J10', [.50, .55, 1.0, .52, .58, 1.3], {'flicker': [.02, .35], 'sweep': wt(16, 'sourate')})
if RECD:
    sh(RECD['t0'],     'REC')
    sh(RECD['t1'],     'J11', [.45, .45, 1.2, .43, .55, 1.45], {'flicker': [.95, .55], 'bloom': [.42, .48, ls(17) + 1.2]})
else:
    sh(ls(17) - .15,   'J11', [.45, .45, 1.2, .43, .55, 1.45], {'flicker': [.95, .55], 'bloom': [.42, .48, ls(17) + 1.2]})
sh(wt(17, "jusqu'à") - .2, 'J12', [.45, .48, 1.4, .46, .46, 1.75], {'flicker': [.66, .72], 'bloom': [.46, .45, wt(17, 'barbe')]})
sh(ls(18) - .15,       'J11c', [.50, .50, 1.1, .55, .45, 1.35], {'flicker': [.05, .08], 'bloom': [.55, .32, wt(18, 'livres')]})
sh(ls(19) - .15,       'J10', [.75, .25, 1.4, .80, .20, 1.7], {'bloom': [.80, .18, wt(19, 'lumière')], 'dust': .7})
sh(ls(20) - .15,       'J3',  [.74, .55, 1.15, .74, .52, 1.4], {'flicker': [.86, .30]})
# V. LE PIÈGE
sh(pz(20) + .1,        'J5',  [.55, .55, 1.15, .62, .52, 1.35], {'dark': .3, 'dust': .4})
sh(ls(22) - .15,       'J6b', [.35, .55, 1.3, .60, .55, 1.3], {'flicker': [.36, .10]})
sh(wt(22, 'Ce') - .2,  'J2',  [.40, .55, 1.3, .40, .52, 1.1], {'dark': .3, 'desat': .3})
sh(ls(23) - .15,       'J3',  [.73, .48, 1.8, .73, .47, 2.1], {'flicker': [.86, .30]})
sh(ls(24) - .15,       'J9',  [.50, .50, 1.05, .50, .45, 1.25], {'flicker': [.06, .62]})
sh(wt(24, 'Il', 1) - .2, 'J10', [.45, .58, 1.2, .55, .55, 1.2], {'flicker': [.02, .35], 'bloom': [.80, .18, wt(24, 'pure')]})
sh(ls(25) - .15,       'CUT', None, {'obj': 'J13', 'anim': 'staff', 'w': 1150, 'y': 470, 'hit': wt(25, 'pose')})
sh(wt(25, 'et', 1) - .2, 'J13', [.80, .55, 1.6, .70, .52, 1.8], {'flicker': [.33, .17]})
# VI. LA PROTECTION
sh(pz(25) + .1,        'J14', [.45, .40, 1.05, .40, .40, 1.3], {'flicker': [.92, .40], 'dust': .4})
sh(wt(26, 'Vous') - .3,   'J1',  [.65, .45, 1.15, .70, .42, 1.35], {'flicker': [.20, .22], 'bloom': [.80, .40, wt(26, 'sécurité') + .1]})
sh(ls(27) - .15,       'CUT', None, {'obj': 'J4', 'anim': 'exit', 'w': 1250, 'y': 440, 'hit': wt(27, 'Quraysh') - .1})
sh(ls(28) - .15,       'J16', [.40, .55, 1.15, .42, .55, 1.35], {'dust': .5})
# VII. CE QUI RESTE
sh(pz(28) + .1,        'J1',  [.55, .50, 1.0, .65, .48, 1.2], {'flicker': [.20, .22], 'dust': .4})
sh(wt(29, "jusqu'à") - .2, 'J17', [.55, .50, 1.1, .55, .48, 1.3], {'bloom': [.80, .58, wt(29, 'Prophète')], 'dust': .4})
sh(ls(30) - .15,       'J3',  [.70, .50, 1.3, .70, .48, 1.1], {'flicker': [.86, .30], 'dust': .4})
sh(wt(30, 'a', 1) - .25 if False else [x[1] for x in W[30] if x[0] == 'a'][0] - .25, 'J17', [.60, .52, 1.25, .62, .50, 1.05], {'bloom': [.90, .58, le(30)], 'dust': .7})
sh(VEND_CARD,          'END')
sh(VEND_CARD + END_CARD, 'SUB')

data = {'DUR': DUR, 'VEND': VEND_CARD, 'chunks': CH, 'chap': CHAP, 'title': TITLE, 'shots': X, 'rec': RECD,
        'pauses': [[NT(c - 1e-4), d + nat, li, wi] for c, d, li, wi, nat in CUTS]}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
print('DUR', round(DUR, 2), 'VEND', round(VEND, 2), 'REC', round(REC, 2), 'chunks', len(CH), 'shots', len(X))
for c in CHAP: print('chap', round(c[0], 2), round(c[1], 2), c[3])
print('title', {k: round(v, 2) for k, v in TITLE.items()})
ext = [(round(c, 2), round(d, 2), li, wi, round(n, 2)) for c, d, li, wi, n in CUTS if d > 0.01]
print('pauses allongées', len(ext), 'sur', len(CUTS), '— total ajouté', round(sum(x[1] for x in ext), 2), 's')
