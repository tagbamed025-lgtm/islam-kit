# RAP-01-peches : pauses de la bible §3 + calage mot à mot -> timeline.json + voix_p.wav
import json, numpy as np, soundfile as sf
OFF = 0.40
x, sr = sf.read('voice.wav')
# silences naturels mesurés (s, voix d'origine) -> allongement jusqu'au minimum de la bible
# (position d'insertion = milieu du silence, ajout)
INS = [
    (1.38, 0.70 - 0.67),   # fin de phrase « péchés. »
    (14.40, 0.70 - 0.65),  # fin de phrase « d'Allah. »
    (19.17, 1.20 - 1.19),  # avant la dernière phrase (invocation)
    (20.35, 1.00 - 0.63),  # « Dis : » -> juste avant la citation
]
VEND = 23.97               # dernière parole
TAIL = 1.20                # silence tenu après la dernière parole
def N(t):
    return OFF + t + sum(a for p, a in INS if p < t)
# voix avec pauses
parts, last = [], 0
for p, a in INS:
    i = int(p * sr); parts += [x[last:i], np.zeros(int(round(a * sr)))]; last = i
parts.append(x[last:int(VEND * sr) + int(0.05 * sr)])
v = np.concatenate(parts)
v = np.concatenate([np.zeros(int(OFF * sr)), v, np.zeros(int(TAIL * sr))])
sf.write('voix_p.wav', v, sr)
VOICE_END = len(v) / sr
# mots affichés : (texte, début dans la voix d'origine, mot clé ?)
W = {
 'S1': [[('TOUT', 0.0), ('LE', .16), ('MONDE', .24)], [('COMMET', .36), ('DES', .6), ('PÉCHÉS.', .72, 1)]],
 'S2': [[('MÊME', 1.74), ('TOI', 1.8), ('QUI', 1.98), ('PRIES,', 2.12)],
        [('MÊME', 2.8), ('TOI', 2.88), ('QUI', 3.06), ('JEÛNES :', 3.22)],
        [('PERSONNE', 4.04, 1), ("N'EST", 4.36, 1), ('À', 4.6, 1), ("L'ABRI.", 4.72, 1)]],
 'S3': [[('NE', 6.26), ('REGARDE', 6.4), ('PAS', 6.62)], [('CELUI', 6.86), ('QUI', 7.04), ('TOMBE', 7.22)],
        [('AVEC', 7.4), ('MÉPRIS.', 7.58, 1)]],
 'S4': [[('DEMANDE', 8.86), ('À', 9.16), ('ALLAH', 9.28)], [('DE', 9.5), ('LE', 9.58), ('GUIDER…', 9.64, 1)],
        [('ET', 10.55), ('DE', 10.66), ('TE', 10.76), ('PROTÉGER.', 10.86, 1)]],
 'S5': [[('«\u00a0Les', 12.58), ('cœurs', 12.74), ('sont', 12.94), ('entre', 13.08)], [('les', 13.32), ('doigts', 13.48), ("d'Allah.", 13.66, 1)],
        [('Il', 14.74), ('les', 14.84), ('tourne', 15.0)], [('comme', 15.28), ('Il', 15.48), ('veut.\u00a0»', 15.6, 1)]],
 'S6': [[('«\u00a0…Iblîs', 17.18, 1), ('qui', 17.42), ('refusa,', 17.5)],
        [("s'enfla", 17.64), ("d'orgueil…\u00a0»", 18.2, 1)]],
 'S7': [[('«\u00a0Ô', 20.67), ('Celui', 20.8), ('qui', 21.0), ('retourne', 21.24)], [('les', 21.64), ('cœurs,', 21.74)],
        [('raffermis', 22.67), ('mon', 22.95), ('cœur', 23.07)], [('dans', 23.25), ('Ta', 23.4), ('religion.\u00a0»', 23.5, 1)]],
}
words = {s: [[[w[0], round(N(w[1]), 3), len(w) > 2] for w in ln] for ln in lines] for s, lines in W.items()}
# scènes (temps vidéo). Les changements tombent à la FIN d'un silence : la scène précédente reste affichée pendant la pause.
SC = {'S1': N(0) - .2, 'S2': N(1.62), 'S3': N(6.0), 'S4': N(8.76), 'S5': N(12.2),
      'S6': N(16.85), 'S7': N(19.55), 'END1': VOICE_END, 'END2': VOICE_END + 2.6}
DUR = round(VOICE_END + 2.6 + 2.8, 2)
EXTRA = {'srcS5': N(15.95), 'srcS6': N(18.7), 'arS7': N(19.76), 'srcS7': N(23.85)}
json.dump({'OFF': OFF, 'DUR': DUR, 'SC': SC, 'W': words, 'X': EXTRA, 'VOICE_END': VOICE_END}, open('timeline.json', 'w'), ensure_ascii=False, indent=1)
print('voix avec pauses', round(VOICE_END, 2), 's · durée vidéo', DUR, 's · ajout', round(sum(a for _, a in INS) + TAIL - (24.686 - VEND), 2))
print({k: round(v, 2) for k, v in SC.items()})
