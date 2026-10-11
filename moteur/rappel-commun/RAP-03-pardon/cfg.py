ID = 'RAP-03-pardon'
TAG = '03'
TITLE = "Domine ta colère, pardonne… – Rappel"
VOICE = "Dans le Coran, Allah décrit ceux qu'Il aime : « Ceux qui dépensent, dans l'aisance comme dans l'adversité ; ceux qui dominent leur colère, et qui pardonnent aux gens. Allah aime les bienfaisants. » Dominer sa colère. Pardonner. Deux choix, chaque jour, à notre portée."
# À l'écran : traduction Hamidullah exacte (quran.com/fr), calée sur la voix par ancres « mot|mot dit ».
SCENES = [
 {'kind': 'c', 'obj': 'S01_livre-lumiere', 'anim': 'drop', 'glow': 'AIME', 'lines': ["DANS LE CORAN,", "ALLAH DÉCRIT", "CEUX QU'IL *AIME :"]},
 {'kind': 'q', 'chip': 'CORAN · 3:134', 'quran': True, 'ar': "ٱلَّذِينَ يُنفِقُونَ فِى ٱلسَّرَّآءِ<br>وَٱلضَّرَّآءِ",
  'lines': ["« …qui|qui dépensent", "dans l'aisance", "et|comme dans *l'adversité,"]},
 {'kind': 'q', 'chip': 'CORAN · 3:134', 'quran': True, 'ar': "وَٱلْكَـٰظِمِينَ ٱلْغَيْظَ<br>وَٱلْعَافِينَ عَنِ ٱلنَّاسِ", 'src': "Coran · Âl ʿImrân 3:134<br>trad. Hamidullah",
  'lines': ["qui|qui *dominent leur *rage|colère", "et *pardonnent à|aux autrui|=", "– car|allah Allah|= aime", "les *bienfaisants – »|bienfaisants"]},
 {'kind': 'c', 'obj': 'S03_main-ouverte', 'anim': 'open', 'lines': ["*DOMINER SA COLÈRE.", "*PARDONNER.", "DEUX CHOIX, CHAQUE JOUR,", "À NOTRE PORTÉE."]},
]
SOURCES = "Coran, Âl ʿImrân 3:134<br><span style='font-size:42px;opacity:.8'>traduction Hamidullah</span>"
THUMB = {'obj': 'S03_main-ouverte', 'l1': 'DOMINE', 'l2': 'TA COLÈRE', 'l3': 'ET PARDONNE'}
