ID = 'RAP-04-bonne-parole'
TAG = '04'
TITLE = "Dis du bien… ou tais-toi – Rappel"
VOICE = "Le Prophète, paix et salut sur lui, a dit : « Que celui qui croit en Allah et au Jour dernier dise du bien, ou qu'il se taise. » Une seule phrase. Un seul réflexe à prendre avant de parler : est-ce que ce que je m'apprête à dire est un bien ?"
# arabe : sunnah.com, Bukhârî 6018 (déjà vérifié pour PHO-08 le 09/10/2026)
SCENES = [
 {'kind': 'q', 'chip': 'HADITH', 'ar': "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الْآخِرِ<br>فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ", 'src': "Sahîh al-Bukhârî 6018",
  'lines': ["~Le Prophète ﷺ|paix a|a dit :", "« Que celui qui croit en Allah", "et au Jour dernier", "*dise du bien,", "ou qu'il *se taise. »"]},
 {'kind': 'c', 'obj': 'S02_sablier', 'anim': 'drop', 'lines': ["UNE SEULE PHRASE.", "UN SEUL *RÉFLEXE", "À PRENDRE", "AVANT DE *PARLER :"]},
 {'kind': 'c', 'obj': 'S03_plume', 'anim': 'float', 'lines': ["EST-CE QUE CE QUE", "JE M'APPRÊTE À DIRE", "EST UN *BIEN ?"]},
]
SOURCES = "Sahîh al-Bukhârî 6018<br><span style='font-size:42px;opacity:.8'>rapporté par Abû Hurayra</span>"
THUMB = {'obj': 'S03_plume', 'l1': 'DIS DU BIEN', 'l2': 'OU TAIS-TOI', 'l3': 'UN SEUL RÉFLEXE'}
