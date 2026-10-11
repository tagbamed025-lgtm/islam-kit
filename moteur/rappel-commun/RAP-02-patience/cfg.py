ID = 'RAP-02-patience'
TAG = '02'
TITLE = "Tout est un bien pour le croyant… – Rappel"
VOICE = "Le Prophète, paix et salut sur lui, a dit : « Étonnante est l'affaire du croyant ! Tout, dans son affaire, est un bien pour lui, et cela n'est pour personne d'autre que pour le croyant. S'il lui arrive un bonheur, il est reconnaissant, et c'est un bien pour lui. Et s'il lui arrive un malheur, il patiente, et c'est un bien pour lui. »"
# kind c = crème + objet ; q = émeraude + arche (citation). ar = arabe (sunnah.com), src = source affichée après le dernier mot
SCENES = [
 {'kind': 'c', 'obj': 'S01_mains-ciel', 'anim': 'rise', 'lines': ["LE PROPHÈTE ﷺ|paix", "A DIT\u00a0:"]},
 {'kind': 'c', 'obj': 'S02_coeur-lumiere', 'anim': 'pop', 'glow': 'CROYANT', 'lines': ["«\u00a0ÉTONNANTE EST", "L'AFFAIRE DU", "*CROYANT\u00a0!"]},
 {'kind': 'q', 'chip': 'HADITH', 'ar': "عَجَبًا لِأَمْرِ الْمُؤْمِنِ<br>إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ",
  'lines': ["Tout, dans son affaire,", "est un *bien pour lui,", "et cela n'est pour personne", "d'autre que pour le *croyant."]},
 {'kind': 'q', 'chip': 'HADITH', 'ar': "إِنْ أَصَابَتْهُ سَرَّاءُ شَكَرَ",
  'lines': ["S'il lui arrive un *bonheur,", "il est *reconnaissant,", "et c'est un bien pour lui."]},
 {'kind': 'q', 'chip': 'HADITH', 'ar': "وَإِنْ أَصَابَتْهُ ضَرَّاءُ صَبَرَ", 'src': "Sahîh Muslim 2999",
  'lines': ["Et s'il lui arrive un *malheur,", "il *patiente,", "et c'est un bien pour lui.\u00a0»"]},
]
SOURCES = "Sahîh Muslim 2999<br><span style='font-size:42px;opacity:.8'>rapporté par Suhayb</span>"
THUMB = {'obj': 'S01_mains-ciel', 'l1': 'TOUT EST', 'l2': 'UN BIEN', 'l3': 'POUR LE CROYANT'}
QURAN = []  # scènes coraniques : aucun son, aucun fond vocal
