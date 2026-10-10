ID = 'VID-06-salman'
TITLE_TXT = "Il a cherché la vérité pendant 40 ans… à travers 4 pays – Salman al-Farisi"
H = {'TAG': '06', 'NAME': "SALMAN AL-FARISI", 'NSIZE': 190, 'AR': 'سَلْمَانُ الْفَارِسِيُّ', 'END_BG': 'SA12',
     'SOURCES': 'Musnad Ahmad · <span style="color:var(--gold)">récit de Salman</span> (via Ibn Ishâq)<br>Sahîh al-Bukhârî <span style="color:var(--gold)">(éléments courts)</span><br>Ibn Hishâm, <span style="color:var(--gold)">as-Sîra an-Nabawiyya</span>'}
TH = {'IMG': 'SA1', 'PH': '55% 50%', 'PV': '60% 50%', 'L1': '40 ANS DE RECHERCHE…', 'L2': 'POUR UNE VÉRITÉ.'}
# ---- plans ----
CHAP_AFTER = {3: 'I', 7: 'II', 11: 'III', 14: 'IV', 16: 'V', 19: 'VI', 26: 'VII'}
NAMES = {'I': 'LE FILS DU FEU', 'II': 'LA FUITE', 'III': 'DE MAÎTRE EN MAÎTRE', 'IV': 'LES TROIS SIGNES',
         'V': "L'ESCLAVAGE", 'VI': 'LA RECONNAISSANCE', 'VII': 'LA LIBERTÉ'}
HOOK_LINE = 2
TITLE_CFG = {'mode': 'words', 'line': 3, 'h': 'Voici', 'n': 'Salman', 'end': 'al-Farisi'}
EXTRA = []
KEY = {'quarante', 'chose', 'liberté', 'syrie', 'vérité', 'perse', 'feu', 'église', 'éveille', 'enchaîne', 'chaînes',
       'évêque', 'pauvres', 'suivant', 'arabie', 'noires', 'aumône', 'sceau', 'esclave', 'médine', 'décrite', 'distribue',
       'cadeau', 'islam', 'palmier', 'mains', 'libre', 'fossé', 'trouvée'}
BAND = {22: 'Premier', 24: 'Deuxième', 29: 'Salman', 31: 'pour'}
def shots():
    sh(0,                       'SA5', [.40, .55, 1.0, .45, .52, 1.2], {'dust': .6})
    sh(ls(1) - .15,             'SA1', [.55, .50, 1.1, .55, .45, 1.3], {'flicker': [.52, .25]})
    sh(wt(1, 'sa', 2) - .2,     'SA4', [.40, .55, 1.15, .45, .55, 1.3], {'flicker': [.30, .20]})
    sh(ls(2) - .15,             'SA6', [.50, .50, 1.05, .55, .48, 1.25], {'dust': .4})
    sh(pz(2) + .3,              'SA2', [.55, .50, 1.3, .55, .48, 1.1], {'dark': .45, 'flicker': [.80, .80]})
    sh(TITLE['t1'] - .1,        'SA5', [.65, .50, 1.3, .55, .50, 1.3], {'dust': .5})
    sh(pz(3) + .1,              'SA1', [.55, .45, 1.0, .58, .40, 1.25], {'flicker': [.58, .25], 'dust': .4})
    sh(ls(5) - .15,             'SA2', [.60, .55, 1.15, .65, .60, 1.4], {'flicker': [.82, .78]})
    sh(ls(6) - .15,             'SA3', [.55, .50, 1.05, .60, .45, 1.3], {'dust': .4})
    sh(ls(7) - .15,             'SA3', [.60, .40, 1.4, .62, .38, 1.65], {'bloom': [.60, .40, wt(7, "s'éveille")]})
    sh(pz(7) + .1,              'SA6', [.45, .50, 1.15, .55, .50, 1.15], {'dust': .4})
    sh(ls(9) - .15,             'SA4', [.40, .60, 1.2, .45, .60, 1.45], {'dark': .2, 'shake': wt(9, "l'enchaîne")})
    sh(ls(10) - .15,            'SA5', [.35, .55, 1.25, .55, .55, 1.25], {'dust': .7})
    sh(ls(11) - .15,            'CUT', None, {'obj': 'SA4', 'anim': 'exit', 'w': 1250, 'y': 450, 'hit': wt(11, "s'enfuit")})
    sh(pz(11) + .1,             'SA6', [.50, .45, 1.0, .55, .42, 1.2], {'dust': .4})
    sh(wt(12, 'Il') - .2,       'SA7', [.50, .55, 1.1, .45, .60, 1.35], {'flicker': [.05, .25], 'bloom': [.45, .62, wt(12, 'secret')]})
    sh(ls(13) - .15,            'SA8', [.55, .55, 1.1, .60, .55, 1.3], {'flicker': [.66, .62]})
    sh(wt(13, 'puis') - .2,     'SA6', [.65, .45, 1.35, .45, .45, 1.35], {'dust': .4})
    sh(ls(14) - .15,            'SA8', [.66, .58, 1.6, .66, .60, 1.9], {'flicker': [.66, .62]})
    sh(pz(14) + .1,             'SA9', [.50, .50, 1.05, .55, .48, 1.25], {'dust': .5})
    sh(wt(16, 'émigrera') - .45,    'SA10', [.50, .50, 1.05, .50, .55, 1.3], {'dust': .5})
    sh(wt(16, 'acceptera') - .45,    'SA13', [.30, .55, 1.15, .32, .55, 1.4], {'flicker': [.05, .30]})
    sh(wt(16, 'portera') - .5,    'SA9', [.60, .45, 1.3, .70, .40, 1.5], {'bloom': [.78, .28, wt(16, 'sceau')]})
    sh(pz(16) + .1,             'SA5', [.50, .50, 1.1, .50, .48, 1.3], {'dark': .35, 'dust': .6})
    sh(wt(17, 'Ils') - .2,      'SA11', [.50, .55, 1.05, .50, .52, 1.3], {'flicker': [.10, .35], 'shake': wt(17, 'vendent')})
    sh(ls(18) - .15,            'SA11', [.70, .45, 1.3, .55, .45, 1.3], {'flicker': [.10, .35]})
    sh(wt(18, 'Médine') - .25,  'SA12', [.55, .50, 1.1, .55, .48, 1.3], {'dust': .4})
    sh(ls(19) - .15,            'SA10', [.50, .55, 1.25, .50, .50, 1.05], {'bloom': [.50, .45, wt(19, 'reconnaît')], 'dust': .5})
    sh(pz(19) + .1,             'SA12', [.45, .55, 1.0, .55, .52, 1.2], {'dust': .4})
    sh(wt(20, 'Salman') - .2,   'CUT', None, {'obj': 'SA13', 'anim': 'slide', 'w': 820, 'y': 450})
    sh(ls(21) - .15,            'SA13', [.40, .60, 1.15, .40, .58, 1.35], {'flicker': [.05, .30]})
    sh(ls(22) - .15,            'SA13', [.40, .55, 1.4, .40, .55, 1.6], {'bloom': [.40, .55, wt(22, 'confirmé')]})
    sh(ls(23) - .15,            'CUT', None, {'obj': 'SA14', 'anim': 'rise', 'w': 720, 'y': 450})
    sh(wt(23, 'Cette') - .2,    'SA14', [.45, .55, 1.15, .45, .52, 1.35], {'flicker': [.55, .25]})
    sh(ls(24) - .15,            'SA14', [.45, .50, 1.4, .45, .50, 1.6], {'bloom': [.45, .52, wt(24, 'confirmé')]})
    sh(ls(25) - .15,            'SA12', [.80, .40, 1.3, .82, .38, 1.55], {'dark': .2, 'bloom': [.82, .30, wt(25, 'sceau')]})
    sh(ls(26) - .15,            'SA10', [.50, .45, 1.1, .50, .40, 1.3], {'bloom': [.50, .10, wt(26, 'islam')], 'dust': .6})
    sh(pz(26) + .1,             'SA11', [.30, .55, 1.2, .35, .55, 1.4], {'dark': .3, 'flicker': [.10, .35]})
    sh(wt(27, 'Pour') - .2,     'SA16', [.55, .55, 1.1, .60, .55, 1.3], {'dust': .4})
    sh(ls(28) - .15,            'SA12', [.50, .55, 1.15, .50, .52, 1.4], {'dust': .5})
    sh(ls(29) - .15,            'SA4', [.50, .55, 1.3, .52, .55, 1.1], {'bloom': [.50, .50, wt(29, 'libre')]})
    sh(ls(30) - .15,            'SA17', [.45, .60, 1.05, .50, .58, 1.3], {'dust': .7})
    sh(ls(31) - .15,            'SA5', [.55, .45, 1.3, .55, .42, 1.05], {'bloom': [.62, .32, wt(31, 'trouvée')], 'dust': .7})
