# usage: python3 rec_prep.py <fichier audio/vidéo de la récitation> [nb_versets=4]
# -> audio/recitation.wav (48 kHz mono, silences de début/fin retirés) + rec_verses.json (temps de chaque verset)
import sys, re, json, subprocess, numpy as np, soundfile as sf
src = sys.argv[1]; NV = int(sys.argv[2]) if len(sys.argv) > 2 else 4
VERSES = [
 {'n': 1, 'ar': 'كٓهيعٓصٓ', 'fr': 'Kâf, Hâ, Yâ, ‘Ayn, Sâd.'},
 {'n': 2, 'ar': 'ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ', 'fr': 'C’est un récit de la miséricorde de ton Seigneur envers Son serviteur Zacharie.'},
 {'n': 3, 'ar': 'إِذْ نَادَىٰ رَبَّهُۥ نِدَآءً خَفِيًّا', 'fr': 'Lorsqu’il invoqua son Seigneur d’une invocation secrète,'},
 {'n': 4, 'ar': 'قَالَ رَبِّ إِنِّى وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًا وَلَمْ أَكُنۢ بِدُعَآئِكَ رَبِّ شَقِيًّا',
  'fr': 'et dit : “Seigneur ! Mes os sont affaiblis et ma tête s’est enflammée de cheveux blancs. [Cependant] Je n’ai jamais été malheureux [déçu] en te priant, Seigneur !'},
][:NV]
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vn', '-ac', '1', '-ar', '48000', '/tmp/rec_raw.wav'], check=True)
x, sr = sf.read('/tmp/rec_raw.wav')
thr = 10 ** (-42 / 20); nz = np.nonzero(np.abs(x) > thr)[0]
a = max(0, nz[0] - int(.05 * sr)); b = min(len(x), nz[-1] + int(.25 * sr))
x = x[a:b]
fi = int(.03 * sr); x[:fi] *= np.linspace(0, 1, fi); fo = int(.4 * sr); x[-fo:] *= np.linspace(1, 0, fo)
sf.write('audio/recitation.wav', x, sr)
r = subprocess.run(['ffmpeg', '-i', 'audio/recitation.wav', '-af', 'silencedetect=noise=-40dB:d=0.35', '-f', 'null', '-'],
                   capture_output=True, text=True).stderr
S = [float(v) for v in re.findall(r'silence_start: ([\d.]+)', r)]
E = [float(v) for v in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = sorted(zip(S, E), key=lambda se: -(se[1] - se[0]))[:NV - 1]
SIL.sort()
D = len(x) / sr
print('durée', round(D, 2), 'silences retenus', [(round(s, 2), round(e, 2)) for s, e in SIL])
bounds = [0.0] + [e for s, e in SIL] + [D]
ends = [s for s, e in SIL] + [D]
out = [dict(v, s=round(bounds[i], 3), e=round(ends[i], 3)) for i, v in enumerate(VERSES)]
json.dump(out, open('rec_verses.json', 'w'), ensure_ascii=False, indent=1)
for o in out: print(o['n'], o['s'], o['e'])
