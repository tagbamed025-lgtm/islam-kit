ID = 'VID-05-umar'
TITLE_TXT = "Le Prophète a prié pour que cet homme devienne musulman… et Allah a répondu – Umar ibn al-Khattab"
H = {'TAG': '05', 'NAME': "UMAR IBN AL-KHATTAB", 'NSIZE': 168, 'AR': 'عُمَرُ بْنُ الْخَطَّابِ', 'END_BG': 'U7',
     'SOURCES': 'Jâmi\' at-Tirmidhî · 3681 <span style="color:var(--gold)">(hasan sahih)</span><br>Sahîh al-Bukhârî · 3684<br>Ibn Hishâm, <span style="color:var(--gold)">as-Sîra an-Nabawiyya</span> (contexte)'}
TH = {'IMG': 'U2', 'PH': '45% 50%', 'PV': '58% 50%', 'L1': 'LEUR PIRE ENNEMI…', 'L2': "ALLAH L'A CHOISI."}
# ---- plans ----
CHAP_AFTER = {7: 'I', 11: 'II', 15: 'III', 19: 'IV'}
NAMES = {'I': "L'INVOCATION", 'II': 'LA RÉPONSE', 'III': 'LA FORCE', 'IV': 'CE QUI RESTE'}
HOOK_LINE = 3
TITLE_CFG = {'mode': 'pause'}
EXTRA = []
KEY = {'invocation', 'ennemis', 'répondu', 'force', 'haine', 'redoutent', 'cachent', 'devenir', 'allah', 'aimé', 'puissants',
       'choisi', 'pas', 'trembler', 'exaucée', 'peur', 'forts', 'protège', 'jour', 'calife', 'seul', 'guider'}
BAND = {11: 'Un', 13: 'qui', 22: 'et'}
def shots():
    sh(0,                      'U1', [.50, .55, 1.0, .55, .52, 1.18], {'dust': .5})
    sh(ls(1) - .15,            'U5', [.50, .60, 1.05, .50, .55, 1.3], {'dust': .5})
    sh(ls(2) - .15,            'U2', [.50, .45, 1.15, .50, .42, 1.35], {'dark': .2, 'dust': .4})
    sh(ls(3) - .15,            'U7', [.50, .45, 1.2, .52, .40, 1.0], {'bloom': [.72, .30, wt(3, 'répondu')], 'dust': .5})
    sh(pz(3) + .1,             'U2', [.50, .40, 1.35, .50, .38, 1.15], {'dark': .45, 'dust': .4})
    sh(TITLE['t1'] - .1,       'U1', [.55, .50, 1.3, .45, .50, 1.3], {'dust': .4})
    sh(wt(4, 'Umar') - .2,     'U2', [.45, .50, 1.05, .45, .45, 1.3], {'dust': .5})
    sh(wt(4, 'connu') - .2,    'CUT', None, {'obj': 'U6', 'anim': 'staff', 'w': 420, 'y': 460, 'hit': wt(4, 'haine')})
    sh(ls(5) - .15,            'U2', [.42, .30, 1.6, .45, .28, 1.85], {'dark': .25, 'shake': wt(5, 'redoutent')})
    sh(ls(6) - .15,            'U3', [.50, .55, 1.05, .45, .55, 1.3], {'flicker': [.10, .30], 'dust': .4})
    sh(wt(6, 'sortent') - .2,  'K5', [.50, .55, 1.05, .55, .52, 1.25], {'dust': .7})
    sh(ls(7) - .15,            'U8', [.50, .50, 1.1, .50, .48, 1.3], {'dark': .35})
    sh(pz(7) + .1,             'U7', [.50, .50, 1.05, .52, .50, 1.25], {'dust': .4})
    sh(ls(9) - .15,            'K3', [.50, .45, 1.0, .55, .50, 1.2], {'bloom': [.50, .15, ls(9) + 1.0]})
    sh(wt(9, 'par', 1) - .2,  'U9', [.50, .50, 1.05, .55, .45, 1.25], {'dust': .5})
    sh(ls(10) - .15,           'U5', [.45, .60, 1.2, .50, .55, 1.05], {'dust': .5})
    sh(ls(11) - .15,           'U5', [.72, .45, 1.4, .75, .42, 1.6], {'bloom': [.72, .35, wt(11, 'choisi')]})
    sh(pz(11) + .1,            'U10', [.50, .55, 1.05, .52, .52, 1.25], {'flicker': [.53, .48], 'dust': .4})
    sh(wt(12, "c'est") - .2, 'U7', [.55, .45, 1.2, .55, .42, 1.4], {'bloom': [.72, .30, wt(12, 'aimé')]})
    sh(ls(13) - .15,           'U8', [.50, .45, 1.2, .50, .40, 1.45], {'bloom': [.70, .30, wt(13, 'franchit')], 'dust': .5})
    sh(ls(14) - .15,           'U2', [.50, .45, 1.2, .50, .45, 1.4], {'desat': .35, 'dust': .4})
    sh(wt(14, 'devient') - .2, 'U3', [.50, .55, 1.2, .50, .52, 1.4], {'flicker': [.10, .30]})
    sh(ls(15) - .15,           'U7', [.55, .45, 1.1, .55, .42, 1.3], {'bloom': [.72, .30, wt(15, 'exaucée')], 'dust': .5})
    sh(pz(15) + .1,            'U3', [.50, .55, 1.2, .55, .55, 1.4], {'dark': .35, 'flicker': [.10, .30]})
    sh(ls(17) - .15,           'U10', [.60, .50, 1.3, .60, .48, 1.5], {'flicker': [.53, .48]})
    sh(ls(18) - .15,           'U9', [.50, .55, 1.1, .50, .50, 1.3], {'bloom': [.35, .30, wt(18, 'forts')], 'dust': .5})
    sh(ls(19) - .15,           'U2', [.50, .40, 1.15, .50, .40, 1.35], {'dust': .4})
    sh(wt(19, 'Ce') - .2,      'U9', [.40, .45, 1.3, .60, .45, 1.3], {'sweep': wt(19, 'grand')})
    sh(pz(19) + .1,            'U7', [.50, .50, 1.0, .50, .45, 1.2], {'dust': .5})
    sh(wt(20, 'puis') - .2,    'U1', [.45, .50, 1.2, .60, .50, 1.2], {'dust': .4})
    sh(ls(21) - .15,           'U1', [.60, .55, 1.4, .55, .52, 1.6], {'dark': .2})
    sh(ls(22) - .15,           'U8', [.55, .45, 1.3, .55, .40, 1.1], {'bloom': [.72, .30, wt(22, 'guider')], 'dust': .6})
