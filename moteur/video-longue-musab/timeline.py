import json, re, subprocess, numpy as np, soundfile as sf

LINES = json.load(open('align_lines.json'))          # tight-time words per line
LEAD = 0.6
PAUSES = {4:1.6, 5:3.4, 9:2.2, 13:2.2, 17:0.5, 20:2.2, 27:0.5, 33:3.6, 37:3.4, 41:2.4, 47:0.6, 49:0.8}
END_CARD = 5.2; SUB_CARD = 3.4

# ---------- real silences in the tight voice, to cut cleanly ----------
r = subprocess.run(['ffmpeg','-i','audio/voix_t.wav','-af','silencedetect=noise=-38dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
S = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
E = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = list(zip(S,E))
def cut_after(i):
    a = LINES[i][-1][2]; b = LINES[i+1][0][1]; guess = (a+b)/2
    best = min(SIL, key=lambda se: abs((se[0]+se[1])/2-guess))
    m = (best[0]+best[1])/2
    return m if abs(m-guess) < 0.8 else guess
CUTS = sorted((cut_after(i), d, i) for i,d in PAUSES.items())

def NT(t):
    return LEAD + t + sum(d for c,d,_ in CUTS if c < t)

# ---------- final voice track ----------
v, sr = sf.read('audio/voix_t.wav')
if v.ndim > 1: v = v.mean(1)
parts = [np.zeros(int(LEAD*sr))]; prev = 0
for c,d,_ in CUTS:
    ci = int(c*sr); seg = v[prev:ci].copy()
    f = min(len(seg), int(.012*sr)); seg[-f:] *= np.linspace(1,0,f)
    parts += [seg, np.zeros(int(d*sr))]; prev = ci
parts.append(v[prev:])
voice = np.concatenate(parts)
VEND = len(voice)/sr
DUR = VEND + 0.5 + END_CARD + SUB_CARD
voice = np.concatenate([voice, np.zeros(int((DUR-VEND)*sr)+sr)])[:int(DUR*sr)]
sf.write('audio/voice_final.wav', voice, sr)

W = [[[w, round(NT(s),3), round(NT(e),3)] for w,s,e in L] for L in LINES]
def ls(i): return W[i][0][1]
def le(i): return W[i][-1][2]
def pz(i):  # start of the pause after line i (new time)
    c = [x for x in CUTS if x[2]==i][0][0]; return NT(c-1e-4)+0.0
def wt(i, word, n=1):
    k=0
    for w,s,e in W[i]:
        if w.strip('«»,.…:;!?').lower().startswith(word.lower()):
            k+=1
            if k==n: return s
    raise Exception(f'word {word} not in line {i}')

# ---------- captions ----------
spec = [l.rstrip('\n') for l in open('chunks.txt',encoding='utf-8') if l.strip()]
assert len(spec) == len(W), (len(spec), len(W))
CH = []; inq = False
for li,(sl,words) in enumerate(zip(spec,W)):
    if sl.startswith('@TITLE'): continue
    k = 0
    for ch in sl.split(' | '):
        band = ch.startswith('#'); ch = ch.lstrip('#')
        lines=[[]]; toks=[]
        for tk in ch.split(' '):
            if tk == '/': lines.append([]); continue
            key = '*' in tk; tk = tk.replace('*','')
            w,s,e = words[k]; assert w == tk, (li, w, tk); k += 1
            if '«' in tk: inq = True
            lines[-1].append([tk, s, e, 1 if key else 0])
            q = inq
            if '»' in tk: inq = False
        CH.append({'lines':lines,'band':band,'quote':q or any('«' in x[0] for L in lines for x in L),
                   't0':lines[0][0][1],'t1':lines[-1][-1][2]})
    assert k == len(words), (li, k, len(words))
for a,b in zip(CH, CH[1:]):
    a['hide'] = max(min(b['t0']-0.25, a['t1']+0.7), a['lines'][-1][-1][1]+0.3)
CH[-1]['hide'] = min(CH[-1]['t1']+1.4, VEND+0.3)

# ---------- chapters & title ----------
CHAP = [
 [pz(5)+1.5, ls(6)-0.1, 'I',  'LE PRINCE DE LA MECQUE'],
 [pz(9)+0.1, ls(10)-0.1, 'II', 'LE SECRET'],
 [pz(13)+0.1, ls(14)-0.1,'III','LE PRIX'],
 [pz(20)+0.1, ls(21)-0.1,'IV', 'LE PREMIER AMBASSADEUR'],
 [pz(33)+0.1, pz(33)+2.0,'V',  'UHUD'],
 [pz(37)+1.5, ls(38)-0.1,'VI', 'LE MANTEAU TROP COURT'],
 [pz(41)+0.1, ls(42)-0.1,'VII','LA LEÇON'],
]
TITLE = {'t0': ls(5)-0.1, 'th': wt(5,"l'histoire"), 'tn': wt(5,"Mus'ab"), 't1': pz(5)+1.5}

# ---------- shots : [start, image|map, cam(fx0,fy0,s0,fx1,fy1,s1), fx] ----------
X = []
def sh(t, img, cam, fx=None): X.append({'t':round(t,3),'img':img,'cam':cam,'fx':fx or {}})
sh(0,            'M18_mount_uhud',  [.5,.42,1.0, .52,.40,1.14], {'dust':.5})
sh(ls(1)-.2,     'M01_bedouin_cloak',[.5,.5,1.02, .5,.48,1.2], {'sweep':ls(1)+1.0})
sh(ls(2)-.15,    'M01_bedouin_cloak',[.46,.32,1.55, .5,.28,1.7])
sh(ls(3)-.15,    'M01_bedouin_cloak',[.52,.78,1.7, .5,.74,1.55])
sh(ls(4)-.15,    'M05_elegant_walker',[.44,.52,1.28, .45,.46,1.08], {'sweep':wt(4,'élégant')-.3,'dust':.6})
sh(pz(4)+.2,     'M02_mecca_dusk',  [.55,.55,1.25, .5,.5,1.05], {'dark':.55})
sh(pz(5)+1.5,    'M03_noble_silk',  [.5,.5,1.05, .52,.48,1.22])
sh(wt(7,'avait')-.1,'M03_noble_silk',[.3,.45,1.5, .7,.5,1.5])
sh(wt(7,'des',2)-.1,'M04_perfume_incense',[.5,.45,1.12, .52,.4,1.32],{'dust':.8})
sh(ls(8)-.15,    'M05_elegant_walker',[.5,.8,1.6, .45,.5,1.15],{'dust':.6})
sh(ls(9)-.15,    'M02_mecca_dusk',  [.5,.45,1.3, .5,.5,1.0])
sh(pz(9)+.1,     'M06_oil_lamp_house',[.5,.5,1.0, .53,.62,1.3],{'flicker':[.535,.62],'dust':.4})
sh(ls(11)-.15,   'M06_oil_lamp_house',[.25,.5,1.35, .75,.5,1.35],{'flicker':[.535,.62]})
sh(ls(12)-.15,   'M06_oil_lamp_house',[.535,.64,1.9, .535,.62,2.3],{'flicker':[.535,.62],'bloom':[.535,.62,wt(12,'cœur')]})
sh(ls(13)-.15,   'M06_oil_lamp_house',[.52,.6,1.5, .5,.5,1.0],{'flicker':[.535,.62],'dark':.35})
sh(pz(13)+.1,    'M02_mecca_dusk',  [.35,.55,1.35, .5,.55,1.15],{'dark':.35})
sh(ls(15)-.15,   'M05_elegant_walker',[.45,.45,1.2, .45,.42,1.35],{'dark':.3})
sh(ls(16)-.15,   'M07_bolted_door', [.5,.5,1.05, .5,.52,1.3],{'shake':wt(16,'enfermer')})
sh(ls(17)-.15,   'M07_bolted_door', [.5,.55,1.5, .5,.55,1.62],{'bloom':[.5,.5,wt(17,'renonce')]})
sh(ls(18)-.15,   'MAP_RS',          None, {'route':'abyssinie','r0':wt(18,'part'),'r1':wt(18,"l'Abyssinie")+.8})
sh(wt(18,'Loin',2)-.15,'M09_red_sea_boat',[.4,.55,1.2, .6,.55,1.2],{'dust':.3})
sh(ls(19)-.15,   'M10_desert_road_walker',[.5,.5,1.3, .5,.48,1.1],{'dust':.5})
sh(wt(19,'Le')-.15,'M08_patched_garment',[.5,.45,1.05, .5,.5,1.25])
sh(ls(20)-.15,   'M08_patched_garment',[.5,.5,1.5, .5,.5,1.7],{'bloom':[.5,.35,wt(20,'foi')]})
sh(pz(20)+.1,    'M10_desert_road_walker',[.3,.5,1.35, .6,.5,1.35],{'dust':.5})
sh(ls(22)-.15,   'MAP_RS',          None, {'route':'yathrib','r0':wt(22,'Yathrib')-.3,'r1':wt(22,'Médine')+.6})
sh(wt(22,'Ils')-.15,'M13_rugs_teaching',[.5,.55,1.05, .5,.55,1.25],{'dust':.6})
sh(ls(23)-.15,   'M11_lush_oasis',  [.5,.5,1.3, .5,.5,1.05],{'sweep':ls(23)+.6})
sh(ls(24)-.15,   'M12_two_travelers',[.35,.5,1.25, .45,.5,1.1],{'dust':.4})
sh(wt(24,'Ils')-.15,'M13_rugs_teaching',[.3,.5,1.3, .6,.5,1.3],{'dust':.6})
sh(ls(25)-.15,   'M15_clan_chief_spear',[.5,.5,1.05, .5,.45,1.3],{'shake':wt(25,'furieux')})
sh(ls(26)-.15,   'M13_rugs_teaching',[.5,.5,1.0, .5,.55,1.18],{'dust':.5})
sh(ls(27)-.15,   'M15_clan_chief_spear',[.45,.35,1.5, .5,.4,1.65])
sh(ls(28)-.15,   'M14_spear_sand',  [.5,.4,1.35, .5,.45,1.05],{'shake':ls(28)+.3,'dust':.7})
sh(wt(28,'et')-.1,'M16_seated_listener',[.5,.5,1.2, .5,.5,1.35])
sh(ls(29)-.15,   'M16_seated_listener',[.5,.45,1.4, .5,.45,1.55],{'bloom':[.5,.3,ls(29)+1.0]})
sh(ls(30)-.15,   'M15_clan_chief_spear',[.6,.5,1.25, .4,.5,1.25],{'dust':.4})
sh(wt(30,'Il')-.15,'M17_tribal_gathering',[.5,.6,1.05, .5,.55,1.25])
sh(ls(31)-.15,   'M17_tribal_gathering',[.5,.45,1.4, .5,.5,1.2],{'sweep':ls(31)+.5})
sh(ls(32)-.15,   'M11_lush_oasis',  [.5,.55,1.3, .5,.5,1.0],{'dust':.4})
sh(ls(33)-.15,   'M13_rugs_teaching',[.5,.5,1.2, .5,.5,1.4],{'bloom':[.5,.35,wt(33,'cœurs')]})
sh(pz(33)+.1,    'M18_mount_uhud',  [.5,.45,1.0, .5,.42,1.2],{'dust':.4})
sh(pz(33)+2.0,   'MAP_UHUD',        None, {'date':ls(34),'flag':wt(35,"l'étendard"),'adv':ls(36),'hold':wt(36,'lâche'),'fall':wt(37,'tombe'),'end':pz(37)+1.5})
sh(pz(37)+1.5,   'M20_fallen_banner',[.5,.5,1.05, .5,.52,1.25],{'dust':.6})
sh(wt(39,'Il')-.15,'M19_dust_cloud', [.5,.5,1.3, .5,.5,1.05],{'dust':.9})
sh(wt(39,'et')-.15,'M01_bedouin_cloak',[.5,.5,1.05, .5,.5,1.25],{'desat':.35})
sh(wt(39,'Quand')-.15,'M01_bedouin_cloak',[.5,.3,1.6, .5,.75,1.6],{'desat':.35})
sh(ls(40)-.15,   'M01_bedouin_cloak',[.5,.35,1.4, .5,.3,1.55],{'desat':.2})
sh(wt(40,'et')-.15,'M21_dry_grass', [.5,.55,1.1, .5,.5,1.3],{'sweep':wt(40,'et')+.6})
sh(ls(41)-.15,   'M24_graves_uhud', [.5,.5,1.3, .5,.5,1.02],{'dust':.5,'dark':.25})
sh(pz(41)+.1,    'M23_abundant_meal',[.5,.5,1.05, .5,.5,1.25])
sh(ls(43)-.15,   'M23_abundant_meal',[.3,.5,1.4, .65,.5,1.4])
sh(ls(44)-.15,   'M22_modest_meal', [.5,.5,1.1, .5,.52,1.3])
sh(ls(45)-.15,   'M01_bedouin_cloak',[.5,.5,1.3, .5,.5,1.1],{'desat':.5,'dark':.2})
sh(ls(46)-.15,   'M23_abundant_meal',[.5,.5,1.3, .5,.5,1.05],{'dark':.3})
sh(ls(47)-.15,   'M22_modest_meal', [.5,.5,1.3, .5,.5,1.5],{'dark':.3})
sh(ls(48)-.15,   'M24_graves_uhud', [.35,.5,1.3, .6,.5,1.3],{'dust':.5})
sh(wt(48,'Parmi')-.15,'M05_elegant_walker',[.45,.45,1.35, .45,.5,1.15],{'desat':.4,'dust':.6})
sh(ls(49)-.15,   'M25_fiery_horizon',[.5,.55,1.05, .5,.5,1.25],{'dust':.4})
sh(ls(50)-.15,   'M26_golden_rays', [.5,.6,1.3, .5,.45,1.0],{'dust':.8,'bloom':[.5,.3,wt(50,'dure')]})
sh(VEND+0.5,     'END',             None)
sh(VEND+0.5+END_CARD,'SUB',         None)

data = {'DUR':DUR,'VEND':VEND,'chunks':CH,'chap':CHAP,'title':TITLE,'shots':X,
        'pauses':[[NT(c-1e-4), d, i] for c,d,i in CUTS]}
json.dump(data, open('data.json','w'), ensure_ascii=False)
print('DUR', round(DUR,2), 'VEND', round(VEND,2), 'chunks', len(CH), 'shots', len(X))
for c in CHAP: print('chap', round(c[0],2), round(c[1],2), c[3])
print('title', {k:round(v,2) for k,v in TITLE.items()})
