ID = 'VID-07-khabbab'
TITLE_TXT = "Il est venu se plaindre… le Prophète lui a répondu par une promesse – Khabbab ibn al-Aratt"
H = {'TAG': '07', 'NAME': "KHABBAB IBN AL-ARATT", 'NSIZE': 166, 'AR': 'خَبَّابُ بْنُ الْأَرَتِّ', 'END_BG': 'K10',
     'SOURCES': 'Sahîh al-Bukhârî · 3612 · 3852 · 6943<br>Ibn Sa\'d, <span style="color:var(--gold)">aṭ-Ṭabaqât al-Kubrâ</span> (contexte)'}
TH = {'IMG': 'K1', 'PH': '30% 50%', 'PV': '22% 50%', 'L1': "IL N'EN POUVAIT PLUS…", 'L2': 'UNE PROMESSE.'}
# ---- plans ----
CHAP_AFTER = {6: 'I', 9: 'II', 12: 'III', 15: 'IV'}
NAMES = {'I': 'LA PLAINTE', 'II': 'LA RÉPONSE', 'III': 'LA PROMESSE', 'IV': 'CE QUI RESTE'}
HOOK_LINE = 2
TITLE_CFG = {'mode': 'words', 'line': 3, 'h': 'Voici', 'n': 'Khabbab', 'end': 'al-Aratt'}
EXTRA = [(3, None, 2.2)]
KEY = {'plaindre', 'délivre', 'attendait', 'najd', 'esclave', 'affranchi', 'forgeron', 'épées', 'islam', 'foi', "ka'ba",
       'manteau', 'détresse', 'allah', 'rougi', 'tranchée', 'fer', 'promesse', 'seul', 'loup', 'pressés', 'dureté', 'paix', 'patience'}
BAND = {12: 'rien', 15: 'Mais', 18: 'Une'}
def shots():
    sh(0,                       'K3', [.50, .50, 1.0, .52, .55, 1.2], {'dust': .4})
    sh(ls(1) - .15,             'K5', [.50, .50, 1.05, .50, .52, 1.25], {'dust': .7})
    sh(ls(2) - .15,             'K5', [.70, .55, 1.3, .65, .52, 1.1], {'dust': .6})
    sh(pz(2) + .3,              'K1', [.25, .45, 1.25, .25, .42, 1.05], {'dark': .45, 'flicker': [.18, .30]})
    sh(pz(3) + .1,              'K5', [.40, .50, 1.05, .55, .50, 1.25], {'dust': .7})
    sh(wt(4, 'vendu') - .25,     'U1', [.50, .55, 1.05, .55, .52, 1.25], {'dust': .4})
    sh(wt(4, 'Capturé') - .2,   'K7', [.50, .55, 1.1, .50, .55, 1.35], {'desat': .25})
    sh(wt(4, 'affranchi') - .45,'K10', [.50, .45, 1.2, .50, .40, 1.05], {'bloom': [.52, .30, wt(4, 'affranchi')]})
    sh(ls(5) - .15,             'CUT', None, {'obj': 'K2', 'anim': 'staff', 'w': 950, 'y': 470, 'hit': wt(5, 'forgeron')})
    sh(wt(5, 'fabrique') - .25, 'K1', [.28, .45, 1.15, .30, .45, 1.4], {'flicker': [.18, .30], 'dust': .5})
    sh(ls(6) - .15,             'K4', [.28, .45, 1.8, .28, .42, 1.95], {'dust': .4})
    sh(wt(6, 'Contrairement') - .2, 'U3', [.50, .55, 1.2, .48, .52, 1.4], {'flicker': [.10, .30], 'dark': .2})
    sh(wt(6, 'rien') - .2,      'K4', [.27, .40, 2.0, .27, .38, 2.2], {'bloom': [.27, .25, wt(6, 'foi')]})
    sh(pz(6) + .1,              'K3', [.50, .55, 1.0, .55, .55, 1.2], {'sweep': ls(7) + .5})
    sh(ls(8) - .15,             'K5', [.50, .55, 1.2, .45, .55, 1.4], {'dark': .3, 'dust': .6})
    sh(wt(8, 'celle') - .2,     'U3', [.50, .55, 1.15, .50, .52, 1.35], {'dark': .3, 'flicker': [.10, .30]})
    sh(ls(9) - .15,             'U7', [.50, .50, 1.1, .52, .48, 1.3], {'dark': .25})
    sh(pz(9) + .1,              'K3', [.60, .60, 1.4, .60, .55, 1.6], {'dark': .25, 'shake': wt(10, 'rougi')})
    sh(ls(11) - .15,            'K5', [.50, .50, 1.1, .50, .55, 1.3], {'desat': .4, 'dark': .25})
    sh(wt(11, 'jetés') - .2,    'K7', [.55, .50, 1.3, .55, .50, 1.5], {'desat': .5, 'dark': .25})
    sh(wt(11, "d'autres") - .2, 'K6', [.55, .50, 1.1, .55, .48, 1.35], {'desat': .5, 'dark': .3})
    sh(ls(12) - .15,            'K10', [.50, .50, 1.25, .50, .45, 1.05], {'bloom': [.52, .30, wt(12, 'foi')], 'dust': .6})
    sh(pz(12) + .1,             'K3', [.50, .45, 1.05, .50, .45, 1.25], {'bloom': [.50, .10, ls(13) + 1.0]})
    sh(ls(14) - .15,            'SA5', [.45, .55, 1.05, .50, .52, 1.3], {'dust': .6})
    sh(wt(14, 'sans') - .2,     'K10', [.50, .50, 1.15, .50, .45, 1.3], {'bloom': [.52, .30, wt(14, "qu'Allah")]})
    sh(wt(14, 'et', 1) - .25 if False else wt(14, 'loup') - .45, 'CUT', None, {'obj': 'K9', 'anim': 'slide', 'w': 420, 'y': 470})
    sh(ls(15) - .15,            'K9', [.40, .60, 1.2, .40, .58, 1.4], {'dust': .4})
    sh(pz(15) + .1,             'U7', [.50, .50, 1.05, .52, .48, 1.25], {'dust': .4})
    sh(ls(17) - .15,            'K10', [.50, .50, 1.05, .50, .45, 1.25], {'bloom': [.52, .30, wt(17, 'paix')], 'dust': .5})
    sh(ls(18) - .15,            'K10', [.50, .50, 1.3, .50, .45, 1.05], {'bloom': [.52, .30, wt(18, 'réaliser')], 'dust': .7})
