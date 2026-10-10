ID = 'VID-08-sad'
TITLE_TXT = "Sa mère a refusé de manger pendant 3 jours… pour le faire revenir en arrière – Sa'd ibn Abi Waqqas"
H = {'TAG': '08', 'NAME': "SA'D IBN ABI WAQQAS", 'NSIZE': 172, 'AR': 'سَعْدُ بْنُ أَبِي وَقَّاصٍ', 'END_BG': 'SD8',
     'SOURCES': 'Sahîh Muslim · 1748c<br>Sahîh al-Bukhârî · 3728<br>Coran · 29:8 et 31:15'}
TH = {'IMG': 'SD1', 'PH': '55% 50%', 'PV': '62% 50%', 'L1': '3 JOURS SANS MANGER…', 'L2': 'POUR LE FAIRE REVENIR.'}
# ---- plans ----
CHAP_AFTER = {6: 'I', 9: 'II', 13: 'III', 16: 'IV'}
NAMES = {'I': 'TROIS JOURS', 'II': "L'ÉPREUVE", 'III': 'LA RÉVÉLATION', 'IV': 'CE QUI RESTE'}
HOOK_LINE = 2
TITLE_CFG = {'mode': 'words', 'line': 3, 'h': 'Voici', 'n': "Sa'd", 'end': 'Waqqâs'}
EXTRA = [(3, None, 2.2)]
KEY = {'manger', 'boire', 'foi', 'islam', 'flèche', "d'allah", 'arme', "l'amour", 'parents', 'arrière', 'parole', 'céder',
       'âmes', 'religion', 'effondre', 'boire', 'versets', 'bonté', 'désobéir', 'paradis', 'mère', 'vérité'}
BAND = {2: 'Trois', 10: 'Mais', 16: 'mais', 19: 'Entre'}
def shots():
    sh(0,                       'SD1', [.50, .55, 1.0, .48, .55, 1.25], {'flicker': [.20, .10]})
    sh(ls(1) - .15,             'SD2', [.45, .50, 1.1, .45, .48, 1.3], {'dark': .2})
    sh(wt(1, 'tant') - .2,      'SD3', [.62, .45, 1.15, .62, .42, 1.35], {'dark': .2})
    sh(ls(2) - .15,             'SD5', [.45, .50, 1.05, .45, .50, 1.25], {'bloom': [.30, .30, wt(2, 'passent')], 'dust': .7})
    sh(pz(2) + .3,              'SD0', [.25, .45, 1.35, .25, .42, 1.15], {'dark': .45, 'dust': .4})
    sh(pz(3) + .1,              'U1', [.50, .55, 1.0, .52, .52, 1.2], {'dust': .5})
    sh(wt(4, 'parmi') - .2,     'U3', [.50, .55, 1.1, .50, .52, 1.3], {'flicker': [.10, .30]})
    sh(wt(4, 'Il', 1) - .2,     'CUT', None, {'obj': 'SD0', 'anim': 'rise', 'w': 380, 'y': 450})
    sh(ls(5) - .15,             'SD2', [.42, .50, 1.3, .42, .48, 1.55], {'dark': .3})
    sh(ls(6) - .15,             'SD4', [.30, .55, 1.1, .35, .55, 1.3], {'dust': .4})
    sh(wt(6, "l'amour") - .2,   'SD4', [.30, .45, 1.6, .30, .45, 1.8], {'bloom': [.25, .45, wt(6, "l'amour") + .2]})
    sh(pz(6) + .1,              'SD2', [.50, .50, 1.05, .45, .50, 1.25], {'dark': .2})
    sh(wt(7, 'reviens') - .25,  'SD3', [.60, .45, 1.3, .60, .42, 1.55], {'dark': .25, 'shake': wt(7, 'arrière')})
    sh(ls(8) - .15,             'CUT', None, {'obj': 'SD1', 'anim': 'slide', 'w': 820, 'y': 450})
    sh(ls(9) - .15,             'SD5', [.50, .50, 1.1, .45, .50, 1.35], {'dust': .7})
    sh(wt(9, 'Elle', 2) - .2,   'SD2', [.45, .45, 1.4, .45, .42, 1.6], {'dark': .35})
    sh(pz(9) + .1,              'SD3', [.60, .50, 1.05, .62, .45, 1.3], {'dark': .2})
    sh(ls(11) - .15,            'SD4', [.35, .50, 1.2, .30, .50, 1.4], {'dust': .3})
    sh(wt(11, 'il', 2) - .2 if False else wt(11, 'quitterait') - .5, 'SD7', [.55, .50, 1.1, .55, .45, 1.3], {'bloom': [.60, .30, wt(11, 'religion')]})
    sh(ls(12) - .15,            'SD6', [.45, .50, 1.15, .45, .48, 1.35], {'desat': .3, 'shake': wt(12, 'effondre')})
    sh(ls(13) - .15,            'SD1', [.75, .45, 1.4, .75, .45, 1.6], {'flicker': [.20, .10]})
    sh(pz(13) + .1,             'SD7', [.50, .55, 1.0, .55, .50, 1.25], {'bloom': [.50, .40, ls(14) + 1.5], 'dust': .6})
    sh(ls(15) - .15,            'SD7', [.35, .55, 1.3, .65, .55, 1.3], {'dust': .5})
    sh(ls(16) - .15,            'SD8', [.55, .50, 1.1, .55, .48, 1.3], {'bloom': [.60, .40, wt(16, 'Allah')], 'dust': .5})
    sh(pz(16) + .1,             'SD9', [.42, .50, 1.05, .42, .48, 1.3], {'dust': .5})
    sh(wt(17, 'et', 1) - .2,    'SD9', [.42, .45, 1.45, .45, .45, 1.6], {'dust': .5})
    sh(ls(18) - .15,            'SD0', [.25, .45, 1.2, .25, .42, 1.4], {'dust': .4})
    sh(wt(18, 'a', 1) - .25 if False else [x[1] for x in W[18] if x[0] == 'a'][0] - .25, 'U8', [.50, .45, 1.2, .50, .42, 1.4], {'bloom': [.72, .30, le(18)]})
    sh(ls(19) - .15,            'SD8', [.55, .50, 1.3, .55, .45, 1.05], {'bloom': [.62, .40, wt(19, 'trouver')], 'dust': .7})
