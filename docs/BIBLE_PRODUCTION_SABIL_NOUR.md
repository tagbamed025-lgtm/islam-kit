# BIBLE DE PRODUCTION — Sabil Nour (سبيل النور)

Version 2 — **validée par Mo le 09/10/2026** (« ok bible »).
Cette bible REMPLACE `chaine-islam-reference.md` : tout ce qui y était a été repris, rien n'est perdu. Elle est mise à jour à la fin de chaque contenu.

---

## 1. Chaîne et objectifs
- Nom : **Sabil Nour** — « le chemin de la lumière ». Pseudo : @sabilnour (YouTube : @SabilNour0u).
- Accroches : « Des ténèbres vers la lumière. » · « Une histoire chaque vendredi ».
- Logo : porte en arc émeraude, lumière dorée au fond, petite étoile ; logo seul (sans texte), le texte va sur la bannière.
- Ce projet ne contient QUE le contenu religieux. Le personal branding (LinkedIn, TikTok Optimisme, Nokia…) a son propre projet.
- Objectif : faire grandir la chaîne avec une routine régulière (calendrier de 14 jours), contenu sourcé et sobre. Monétisation : pas décidée.
- Audience actuelle : francophone. Version anglaise prévue dans 3 à 5 mois, quand la routine quotidienne tient (voir §11).
- Noms écartés : Sabiluna, As-Sabil/Assabil, Qirtas, Zumurrud, toute formule « Fi sabil… ».
- Mo est à Dakar (heure du calendrier de publication = Dakar).

## 2. Identité visuelle (validée 30/09/2026) — une charte, deux ambiances
Toujours identique : polices **Anton** (titres), **Cormorant Garamond italique** (citations), **Amiri** (arabe), **Inter** (étiquettes) ; émeraude **#0F5B46** (signature) ; doré **#EDCB85 / #EBD9A4** en petite touche ; logo ; étiquette de série ; même écran « Abonne-toi » (fond crème, disque émeraude).

1. **Style Compagnons « apparition »** (reels « Moment de compagnon ») : fond blanc cassé **#F4F1EA** + grain papier, texte **#141414**, objets détourés (rembg `isnet-general-use`) avec ombre douce qui apparaissent, mots clés en émeraude. Niveau de rendu de référence : reel « La lampe des Ansâr » (zoom lent, nuit qui tombe, coupe au noir, flash de lumière, mot clé doré sur fond sombre).
2. **Rendu cinéma** (reels hadith et vidéos longues du vendredi ; modèles : « La natte » V3 et Mus'ab V2) : photos plein écran avec mouvements de caméra lents, poussière dans la lumière, fondus enchaînés, texte crème avec ombre, sous-titres courts (2–4 mots) mot à mot, bandeau émeraude incliné avec mot clé en doré, étiquette de série en pastille verte (« HADITHS · NN », « COMPAGNONS · NN »), carte de fin arabe + source sur vert profond, puis écran Abonne-toi.
3. **Récitation** : fond émeraude profond + halo doré, arche dorée qui se dessine, poussière dorée, étiquette « CORAN · SOURATE · N:V », arabe Amiri Quran crème-or, traduction Cormorant italique, dernier passage en doré avec ﴿numéro﴾, crédits (récitateur + traducteur), logo.
4. **Photos** (hadith / invocation / verset) : carré, arche verte sur fond crème, bandeau « HADITH » / « INVOCATION » vert, arabe vert, citation en Cormorant, source en petites capitales.
5. **Rappel (typographique + objets en mouvement, validé le 09/10/2026)** : sur les scènes de conseil, objets détourés (1 par scène, fond uni, aucun visage) qui apparaissent et bougent au-dessus du texte sur fond crème ; pas de photo plein écran. Fond crème #F4F1EA + grain pour les phrases d'accroche et de conseil (texte #141414, mot clé en émeraude, apparition mot à mot calée sur la voix) ; **fond émeraude profond avec arche dorée** pour les citations (hadith, verset, invocation) : arabe Amiri crème-or, traduction Cormorant italique, source en doré. Étiquette « RAPPEL · NN ».
- Le reel « Le chien et le puits » reste dans l'ancien style ; les hadiths suivants suivent le rendu cinéma.
- **Miniatures** : 1 visuel fort, 2 à 4 mots en Anton très gros, bandeau émeraude avec mot clé doré, logo discret, aucun visage de compagnon, aucune représentation du Prophète ﷺ. Formats 1080×1920 et 1280×720. Miniature récitation : fond émeraude + arche, mot arabe clé en or, accroche fidèle au verset, jamais trompeuse.

## 3. Voix off
- **Voix : « Sébastien – Narrator »** (français, parisien, masculin, voix professionnelle de la bibliothèque ElevenLabs).
- **voice_id : `5DgHTbl1HXudcxdBp5pQ`**
- **Modèle : Eleven v3** (`eleven_v3`), réglages laissés par défaut (Mo n'y a pas touché ; le curseur Stability est resté à sa valeur par défaut).
- Pas de balises `<break>` : les pauses dramatiques se font au montage.
- Le texte envoyé à la voix = le texte à dire, rien d'autre (pas d'indications de scène). Le calage du montage part toujours du texte réellement prononcé.
- **Qui génère la voix : Claude**, via le connecteur ElevenLabs, sur l'ordre de Mo (« ok voix »), une fois le script validé. Mo n'a plus à générer ni importer la voix lui-même.
  - Avant toute génération : estimation du coût en crédits (`estimate_only`), annoncée à Mo.
  - Jamais de génération « pour réessayer » sans accord de Mo (chaque génération coûte des crédits).
  - Nombre de variantes à choisir : **à décider** (1 = économique, 2 = confort pour choisir une prise).
- Fichier voix rangé dans le dépôt : `voix/fr/<ID>.mp3` (même ID que le contenu). Version anglaise : `voix/en/<ID>.mp3`.
- **Voix anglaise (choisie le 10/10/2026) : « Rafaga »** (voix professionnelle de la bibliothèque ElevenLabs, mûre, chaude, medium-profonde, accent neutre, calme et réfléchie — « quietly inspiring », adaptée au récit religieux).
  - **voice_id : `68sMPAsdt7bCNPLgaEmA`**
  - Mêmes règles que la voix FR : modèle Eleven v3, réglages par défaut, pas de balises `<break>`, 1 seule prise, estimation du coût avant toute génération, génération seulement sur l'ordre de Mo.
- **Variantes : toujours 1 seule prise** (Mo prend la « génération 1 »). Coût mesuré : ~385 crédits ElevenLabs (~0,07 $) pour ~25 s de voix.
- **Test du 09/10/2026 (RAP-01)** : génération OK via le connecteur (24,6 s). **Le téléchargement du fichier audio est bloqué depuis l'espace de travail de Claude** (le serveur de stockage ElevenLabs est refusé par le réseau). Conséquence : Claude génère la voix et note son identifiant, mais le fichier MP3 doit être **téléchargé par Mo depuis le lien du flow ElevenLabs** (un clic) puis déposé dans `voix/fr/<ID>.mp3` sur GitHub. Le montage lit ensuite le MP3 depuis le dépôt.
- **Récupération de l'audio : question fermée le 10/10/2026.** Vérification faite à la source (état du proxy réseau de la session) : `storage.googleapis.com` — le serveur où ElevenLabs stocke les MP3 — est **refusé par la politique réseau de l'organisation** (403 sur la connexion, « policy denial »). Ce n'est ni un bug, ni une question de modèle (testé en Sonnet et en Opus), et la documentation du proxy interdit explicitement de chercher une route de contournement. **Conclusion définitive : Claude ne peut jamais récupérer le MP3 lui-même.** Deux chemins, au choix de Mo, à chaque voix générée :
  1. Mo télécharge depuis le lien du flow ElevenLabs et dépose lui-même le fichier dans `voix/fr/<ID>.mp3` ou `voix/en/<ID>.mp3` sur GitHub.
  2. Mo télécharge et envoie le fichier **en pièce jointe dans le chat** : Claude le récupère alors, le range au bon chemin et le pousse sur GitHub (chemin recommandé, Mo ne touche pas à GitHub).
- **À tester** : balises d'expression v3.

### Rythme et pauses (règle de Mo, 09/10/2026)
- La voix générée par ElevenLabs paraît un peu rapide. Les pauses ne se règlent **pas dans la génération** (pas de `<break>`, le texte envoyé garde toute sa ponctuation) : elles s'ajoutent **au montage**, par Claude.
- **Ne plus raccourcir les silences naturels de la voix** pour les nouveaux contenus (l'ancien resserrage à 0,45 s max est abandonné). On ne fait qu'**allonger** quand le silence est plus court que le minimum ci-dessous.
- Pauses minimales de départ (à ajuster à l'écoute avec Mo) :
  | Moment | Pause minimale |
  |---|---|
  | virgule / respiration | 0,35 s |
  | fin de phrase | 0,7 s |
  | juste avant une citation (hadith, verset) | 1,0 s |
  | juste avant la dernière phrase / l'invocation finale | 1,2 s |
  | silence tenu après la dernière parole | 1,2 s |
- Une pause doit tomber dans une scène qui continue d'afficher son contenu (jamais d'écran vide), et le texte à l'écran suit la voix décalée (temps « pause-aware », voir §10).
- Si, malgré les pauses, Mo trouve encore la voix trop rapide : option à proposer, ralentir la voix de 4–5 % (`atempo`, sans changer la hauteur). Non appliqué par défaut.
- Fichier de test : `RAP-01-peches` (24,7 s ; silences naturels de 0,25 s à 1,2 s ; Mo a déposé le MP3 le 09/10/2026).

## 4. Sons (validé)
- Fond vocal sans instrument (fredonnement), baissé sous la voix, coupé sous le Coran.
- Pas de son sur chaque mot (« pas propre ») : son discret seulement sur les mots clés ; riser + impact sur la phrase clé ; boom grave en fin de phrase ; whoosh doux aux transitions ; ambiance (vent).
- Pauses dramatiques : silence + son de suspense avant le nom du compagnon ; pause + carton à chaque chapitre.
- Mixage : −14 LUFS, limiteur. Aucun son sous le Coran (ni fond vocal, ni effet, ni transition).
- Banque de sons : `sons/` (whoosh, riser, impact, boom, pop, tick, suspense, cinematic hit…).

## 5. Formats, codes de discussion et calendrier

| Code | Contenu | Durée | Par cycle de 14 jours |
|---|---|---|---|
| `#VID` | Vidéo du vendredi : histoire d'un compagnon, 16:9, chapitres + cartes animées | 4–5 min max | 2 (chaque vendredi, fixe) |
| `#COMPAGNON` | Reel « Moment de compagnon » 9:16, fond crème, un moment indépendant | 30–45 s | 2 |
| `#HADITH` | Reel hadith 9:16, rendu cinéma | 30–45 s | 2 |
| `#RECITATION` | Récitation du Coran + traduction animée | 30–40 s | 2 |
| `#PHOTO` | Image fixe : hadith / invocation / verset | — | 4 |
| `#RAPPEL` | **Nouveau (09/10/2026)** : conseil / rappel court, un seul message appuyé sur un hadith authentique ou un verset | ~40 s à 1 min | 1 |
| `#SCRIPT` | Écriture des scripts, légendes, prompts d'images + voix off (après « ok voix ») | — | par lot |
| `#EN` | Version anglaise d'un contenu existant | — | plus tard |

**Reels compagnons (30/09/2026)** : on ne découpe plus la vidéo du vendredi. Chaque reel = une situation (bataille, période, épisode), ce qu'a fait le compagnon, ce qu'on retient. Fin : carton « Ce qu'on retient » + source + « Une histoire chaque vendredi » + Abonne-toi.

**Calendrier de 14 jours (02/10/2026, complété le 09/10/2026 avec le Rappel)** — le vendredi reste fixe, le reste est réparti avec alternance image/vidéo et un jour de repos :

| Jour | Contenu |
|---|---|
| J1 Lun | Reel hadith |
| J2 Mar | Photo |
| J3 Mer | Reel compagnon |
| J4 Jeu | Photo |
| **J5 Ven** | **Vidéo du vendredi** |
| J6 Sam | Récitation |
| J7 Dim | Repos |
| J8 Lun | Photo |
| J9 Mar | Reel hadith |
| J10 Mer | Photo |
| J11 Jeu | Reel compagnon |
| **J12 Ven** | **Vidéo du vendredi** |
| J13 Sam | Récitation |
| J14 Dim | **Rappel** (remplace une photo) |

Total : 2 vidéos du vendredi, 2 reels compagnons, 2 reels hadith, 2 récitations, 4 photos, 1 rappel, 1 jour de repos.

**Heures de publication (hypothèse de départ, heure de Dakar, à tester 2 semaines)** : photos 7h30 ; reels 18h30 ; récitation samedi 20h ; vidéo du vendredi 9h. (France = +2 h.)

**Fin d'un Rappel** : carton source (références des citations) + « Une histoire chaque vendredi sur @sabilnour » + écran Abonne-toi. Pas de carton « Ce qu'on retient » (réservé aux reels compagnons).

**Format Rappel — règles** : un seul message ; appuyé sur un hadith authentique ou un verset avec source affichée ; aucun jugement sur des personnes ou des catégories ; aucun avis personnel, fiqh, fatwa ; pas de récit sans source ; ouverture par une phrase d'accroche. Premier Rappel validé par Mo (09/10/2026) : « Tout le monde commet des péchés… » (voir `scripts/fr/RAP-01-peches.md`).

## 6. Code couleur des scripts (validé le 09/10/2026)
Dans les scripts remis par Claude :
- noir : texte de la voix off (le seul qui part à ElevenLabs) ;
- vert : texte affiché à l'écran ;
- doré : source (Coran / hadith) à afficher ;
- gris italique : indication de son ou de montage ;
- bleu : image à fournir, nommée `S<scène>_<sujet>_<n°>`.

## 7. Méthode : 3 types de discussions (validée le 09/10/2026)
Une discussion = une tâche. Le modèle est choisi au début et ne change plus. Les codes ci-dessus s'écrivent en début de message ; pas de numéro à taper.

1. **#SCRIPT (Sonnet)** — par lot (1 cycle de 14 jours, ou 2 cycles). Livrables : scripts sourcés ; texte voix off seul ; **découpage en scènes avec le texte affiché à l'écran (vert) et la source de chaque scène** ; style visuel du contenu (apparition / cinéma / typographique) ; liste des images nommées ; prompts d'images en anglais (un par ligne, bloc de style inclus) ; titres et légendes des photos ; titre + miniature suggérée. Après validation et « ok voix » : génération de la voix (estimation du coût d'abord) et rangement dans `voix/fr/`.
2. **Mo** — génère les images à partir des prompts et les dépose dans `images/par_contenu/<ID>/` (via GitHub, sans les coller dans le chat) ; seules les images vraiment nouvelles sont à générer (voir §9).
3. **#MONTAGE (Opus)** — une discussion par format (ex. les 2 reels hadith du cycle ; les 2 reels compagnons ; la vidéo du vendredi, validée partie par partie ~1 min). Lit la bible, récupère le dépôt, lit script + voix + images, monte, livre MP4 + miniatures, met à jour la bible et le catalogue.
- Les photos et les récitations sont légères : elles peuvent se faire dans la discussion #SCRIPT ou dans une discussion à part.
- À la fin de chaque contenu : bible → catalogue → dépôt GitHub (les rendus MP4 vont dans Google Drive, pas dans GitHub).

## 8. Règles validées

### Contenu religieux
1. Aucune représentation du Prophète ﷺ, des prophètes ni du visage d'un compagnon.
2. Sources : Coran (traduction Hamidullah, copiée depuis quran.com/fr sans modification) ; hadiths authentiques ; référence affichée à l'écran, vérifiée sur sunnah.com / quran.com.
3. Pas de récits populaires sans source solide ; hadiths faibles (da'if) écartés.
4. Aucun avis personnel : pas de fiqh, fatwa, takfir, politique, sujets de divergence. Jamais de jugement sur des personnes.
5. Aucun dialogue inventé attribué au Prophète ﷺ ou à un compagnon (paroles rapportées au discours indirect si le texte exact n'est pas dans la source ; ne pas nommer un personnage que la source ne nomme pas).
6. Pas de musique instrumentale ; aucun son sous le Coran.
7. Un propos du narrateur (ex. Ibn 'Umar) n'est jamais attribué au Prophète ﷺ.
8. Relecture par une personne de confiance avant publication.
9. Ne pas affirmer ce qu'on ne peut pas savoir (ex. « Allah accepte de toi »).

### Livrables
- **Vidéo** : MP4 final + miniatures (1080×1920 et 1280×720) + titre proposé. **Nom du fichier MP4 = titre proposé** (« | » → « – », pas de « ? », « : », « / »).
- **Photo** : le **titre court à copier-coller** (= nom du fichier image) + la légende complète à coller dans la description : phrase du hadith, une question de réflexion (jamais un avis ni un conseil religieux), source (narrateur + recueil + numéro), « Une histoire chaque vendredi sur @sabilnour », 3–4 hashtags. Pas de « Chers croyants… » : ton sobre.
- Toute vidéo se termine par « Ce qu'on retient » + source + « Une histoire chaque vendredi » + Abonne-toi (reels compagnons).
- Les vidéos longues ont le niveau professionnel des reels (pas de diaporama) et se valident partie par partie.

### Récitations du Coran
- Seul l'audio du récitateur, aucun son ajouté. Texte arabe Uthmani de quran.com, vérifié avec alquran.cloud ; traduction Hamidullah de quran.com/fr.
- Découpage selon les pauses réelles du récitateur ; ne pas couper un verset en plein milieu.
- Structure : (1) la vidéo s'ouvre directement sur la récitation ; (2) carte de la sourate ~2,5 s, silencieuse ; (3) écran « Abonne-toi — UN VERSET, UNE LUMIÈRE », silencieux.

## 9. Stockage et nommage

### Principe
Tout est rangé dans le dépôt GitHub `tagbamed025-lgtm/islam-kit` pour que n'importe quelle nouvelle discussion retrouve une voix, des images, un script, et puisse refaire une vidéo (autre langue, autre format) sans rien régénérer. Avant de demander une nouvelle image à Mo, Claude regarde d'abord `images/banque/` et le catalogue.

### Dossiers
```
islam-kit/
  README.md
  docs/        bible, instructions, méthode (PDF)
  catalogue/   catalogue.json (tous les contenus : titre, statut, sources, voix, images, rendu)
  scripts/fr/  <ID>.md   script + texte voix off + écrans + sources + prompts
  scripts/en/  <ID>.md   version anglaise (plus tard)
  voix/fr/     <ID>.mp3  voix off ElevenLabs
  voix/en/     <ID>.mp3
  audio/recitations/  <ID>.mp3  audio du récitateur (récitations du Coran — déposé par Mo, pas ElevenLabs)
  images/par_contenu/<ID>/   <ID>_S<scène>_<sujet>_<n°>.png   (+ cut_*.png détourées)
  images/banque/<thème>/     images réutilisables (maison, désert, nuit, pain, lampe…)
  moteur/      modèles HTML, scripts de montage, rendu, mixage
  sons/        banque de sons
  charte/      logo/ (logo seul, profils, filigrane, 4 logos), youtube/ (bannière, textes), grain_papier.png ; polices (Anton, Cormorant Garamond, Amiri, Inter)
  miniatures/  <ID>_1080x1920.png, <ID>_1280x720.png (nouveaux contenus)
  references/  vidéos MP4 de référence (une par format), miniatures et photos modèles + README
```
Les MP4 finaux « à publier » restent dans Google Drive (`Sabil Nour/Rendus/`), pas dans GitHub (poids). **Exception (demande de Mo, 09/10/2026) : `references/videos/`** contient une version finale de chaque format (reel compagnon, reel hadith, vidéo du vendredi, récitation) comme modèle. **Avant de monter un nouveau contenu, toute discussion regarde `references/README.md` et le MP4 du même format.**

### Nommage des contenus (ID)
`<TYPE>-<NN>-<sujet>` en minuscules sans accents :
`VID` vidéo du vendredi · `COMP` reel compagnon · `HAD` reel hadith · `REC` récitation · `PHO` photo · `RAP` rappel.
Exemples : `VID-03-musab`, `COMP-02-lampe-ansar`, `HAD-02-natte`, `REC-02-kahf-18-46`, `RAP-01-peches`.
Image : `COMP-02-lampe-ansar_S06_bols_01.png`. Voix : `COMP-02-lampe-ansar.mp3`.

## 10. Production technique
Script sourcé → texte voix off → (Claude) voix ElevenLabs v3 → calcul des pauses (`tighten.py` : **anciens contenus** plafond 0,45 s ; **nouveaux contenus** : pas de raccourcissement, pauses minimales du §3) → transcription horodatée (Whisper-small ONNX, 16 kHz mono, morceaux de 30 s) → calage de chaque mot sur le temps réel → animation HTML déterministe rendue avec Chromium/Playwright (2 segments en parallèle) → sons calés (`sfx.py`, `pad.py`) → mixage −14 LUFS (`mix.sh`) → encodage ffmpeg (x264, CRF 21, AAC 192k) → MP4 nommé avec le titre → miniatures.
- Temps « pause-aware » `N(t)=OFF+t+Σpauses` partagé entre `index.html`, `build_audio.py` et `sfx.py` ; une pause doit tomber dans une scène qui continue d'afficher son contenu (sinon image vide).
- Détourage : rembg `isnet-general-use` → `cut_*.png`.
- Toujours partir du texte réellement dit par la voix.

## 11. Version anglaise (plan)
- Attendre 3 à 5 mois de routine quotidienne avant de lancer un canal ou une piste anglophone.
- Dès maintenant : chaque script garde sa structure (mêmes sources, mêmes scènes) ; le Coran en anglais reconnu sera choisi le moment venu.
- Le montage étant du code, une version anglaise = nouveau texte + nouvelle voix + même images. Pour cela : voix/images/scripts sont rangés par ID dans le dépôt.
- Option à étudier le moment venu : plusieurs pistes audio sur une même vidéo YouTube plutôt qu'un 2e canal.

## 12. Contenus produits (catalogue résumé — détail dans `catalogue/catalogue.json`)
| ID | Titre | Statut |
|---|---|---|
| VID-01-khalid | Khalid ibn al-Walid (pilote, 27–28/09) | livré |
| VID-02-bilal | Bilal ibn Rabah (29/09) | livré, publié |
| VID-03-musab | « Le jeune homme le plus riche de La Mecque… mort sans linceul \| Mus'ab ibn Umayr » (30/09) | livré |
| HAD-01-chien-puits | Le chien et le puits (29/09, ancien style) | livré |
| HAD-02-natte | La natte (30/09, V3 cinéma) | livré |
| COMP-01-anas | Il sentait le parfum du Paradis avant la bataille – Anas ibn an-Nadr | livré |
| COMP-02-lampe-ansar | Ils ont éteint la lampe pour que leur invité mange – Les Ansâr (03/10) | livré |
| REC-01-hadid-57-20 | La vie d'ici-bas n'est qu'un jeu… \| Sourate Al-Hadîd 57:20 | livré |
| REC-02-kahf-18-46 | Tes biens, tes enfants… et ce qui dure vraiment \| Sourate Al-Kahf 18:46 | livré |
| PHO-S1 (×5) | Photos semaine 1 + invocation 2721 + richesse 6446 + verset 33:23 | livrées |
| RAP-01-peches | « Tout le monde commet des péchés… \| Rappel » (09/10, typographique + objets en mouvement, 31,5 s) | livré (v2) |
| REC-03-sharh-94-5-8 | Après chaque épreuve… il y a une facilité \| Sourate Ash-Sharh 94:5-8 | audio déposé (Alafasy), script à valider |
| REC-04-rad-13-28 | C'est par Son évocation que les cœurs se tranquillisent \| Sourate Ar-Ra'd 13:28 | audio déposé (Ash-Shâtirî), script à valider |
| REC-05-baqarah-2-153 | Cherche secours dans la patience et la prière \| Sourate Al-Baqarah 2:153 | audio déposé (Alafasy), script à valider |
| REC-06-zumar-39-53 | Ne désespère jamais de la miséricorde d'Allah \| Sourate Az-Zumar 39:53 | audio déposé (Alafasy), script à valider (remplace At-Talaq) |
| REC-07-mulk-67-1-2 | Il a créé la mort et la vie… pour vous éprouver \| Sourate Al-Mulk 67:1-2 | audio déposé (Alafasy), script à valider |
| REC-08-asr-103 | Par le Temps… l'homme est en perdition, sauf \| Sourate Al-'Asr | audio déposé (Wadee' Al-Yamani), script à valider |
| REC-09-ikhlas-112 | Une sourate qui vaut le tiers du Coran \| Sourate Al-Ikhlas | audio déposé (Alafasy), script à valider |
| REC-10-yunus-10-62 | Les alliés d'Allah n'ont ni crainte ni chagrin \| Sourate Yunus 10:62 | audio déposé (Wadee' Al-Yamani), script à valider |
| PHO-lot-02-oct-dec (PHO-02 à PHO-19, ×18) | Lot de photos, 2/semaine du 13/10 au 10/12/2026 (hadiths + versets + 1 invocation) | livré (18 images rendues), relecture sources à faire |
| VID-04-jafar | Il a fait pleurer un roi… avec un seul discours \| Ja'far ibn Abi Talib | **monté (FR), 4 min 58, livré le 10/10** — relecture avant publication ; voix EN prête |
| VID-05-umar | Le Prophète a prié pour que cet homme devienne musulman… et Allah a répondu \| Umar ibn al-Khattab | **monté (FR), 2 min 40, livré le 10/10** — relecture avant publication ; voix EN prête |
| VID-06-salman | Il a cherché la vérité pendant 40 ans… à travers 4 pays \| Salman al-Farisi | **monté (FR), 3 min 30, livré le 10/10** — relecture avant publication ; voix EN prête |
| VID-07-khabbab | Il est venu se plaindre… le Prophète lui a répondu par une promesse \| Khabbab ibn al-Aratt | **monté (FR), 2 min 09, livré le 10/10** — relecture avant publication ; voix EN prête |
| VID-08-sad | Sa mère a refusé de manger pendant 3 jours… pour le faire revenir en arrière \| Sa'd ibn Abi Waqqas | **monté (FR), 2 min 25, livré le 10/10** — relecture avant publication ; voix EN prête |
| HAD-03-grotte | Trois hommes bloqués dans une grotte… un seul remède à leur situation | Sahîh Muslim 2743 | monté (FR), en attente de relecture |
| HAD-04-tueur-repenti | Il avait tué cent personnes… voici ce qu'Allah a fait de lui | Sahîh Muslim 2766 | monté (FR), en attente de relecture |
| HAD-05-trois-epreuves | Allah a testé ces trois hommes… un seul a réussi | Sahîh al-Bukhârî 3464 | monté (FR), en attente de relecture |
| HAD-06-voleur-dattes | Il attrapait un voleur chaque nuit… jusqu'à ce que le Prophète lui révèle qui c'était | Sahîh al-Bukhârî 2311 | monté (FR), en attente de relecture |
| HAD-07-homme-englouti | Il marchait fier de lui… la terre l'a englouti | Sahîh al-Bukhârî 5789-5790 | monté (FR), en attente de relecture |
| HAD-08-branche-epineuse | Il a juste retiré une branche épineuse du chemin… et il est entré au Paradis | Sahîh al-Bukhârî 652 | monté (FR), en attente de relecture |
| HAD-09-aumone-nuit | Il a donné l'aumône trois nuits de suite… sans jamais savoir à qui | Sahîh al-Bukhârî 1421 | monté (FR), en attente de relecture |
| HAD-10-jurayj | Accusé à tort… un bébé a parlé pour le disculper | Sahîh al-Bukhârî 2482 | monté (FR), en attente de relecture |
Deux extraits de Mus'ab en reel : faits puis mis de côté (décision du 30/09).

## 13. Questions ouvertes
- ~~Récupération de l'audio : à rechercher une autre route.~~ **Fermée le 10/10/2026** : blocage par politique réseau de l'organisation, définitif, aucune route possible — voir §3 pour les deux chemins de remplacement.
- Rappel RAP-01 : avec les seuls minimums du §3, la voix ne passe que de 24,7 s à 25,6 s (+0,94 s) ; si Mo la trouve encore rapide, proposer `atempo` −4/5 % ou des minimums plus longs.
- Format quiz YouTube : proposé (1 par cycle, à la place d'une photo, une seule bonne réponse, explication sourcée) — en attente du « go » de Mo.
- Horaires de publication : à tester 2 semaines.
- Le reel Anas fait 56 s pour un objectif de 45 s : à trancher.

## 14. Historique
- 27–28/09/2026 : pilote Khalid ; nom Sabil Nour ; kit YouTube.
- 29/09 : Bilal ; photos semaine 1 ; « Le chien et le puits » ; script Mus'ab.
- 30/09 : « La natte » ; charte à deux ambiances ; vidéo Mus'ab livrée ; règle « nom du fichier = titre » ; décision des reels compagnons indépendants.
- 02/10 : calendrier de 14 jours.
- 03/10 : reel de la lampe des Ansâr (rendu enrichi).
- 04/10 : règle des photos (titre = nom du fichier + légende).
- 09/10 : voix Sébastien – Narrator v3 inscrite (voice_id) ; Claude génère la voix off ; dépôt GitHub `islam-kit` créé et structuré ; format Rappel ajouté ; plan de la version anglaise.
- 09/10/2026 (suite) : méthode PDF validée (`docs/METHODE_PRODUCTION.pdf`) ; instructions collées dans le projet ; migration des anciens contenus dans le dépôt : scripts (`scripts/fr/`), voix (`voix/fr/`), images (`images/par_contenu/`), moteur de montage par format (`moteur/`), sons (`sons/`), polices et logos (`charte/`), catalogue (`catalogue/catalogue.json`).
- 09/10/2026 (soir) : montage RAP-01 livré (format Rappel typographique ; moteur `moteur/rappel-peches/` ; arabe de l'invocation vérifié sur sunnah.com ; Coran 2:34 copié de quran.com ; aucun son ni fond vocal pendant la citation coranique).
- 09/10/2026 (v2) : RAP-01 refait avec 4 objets détourés en mouvement sur fond crème (tapis, mains, silhouette de dos, lampe) — règle ajoutée au §2 point 5.
- 09/10/2026 (nuit) : 6 scripts de récitation écrits pour couvrir les 3 prochains samedis de récitation (cycles 2 et 3) : REC-03 (Ash-Sharh 94:5-8), REC-04 (Ar-Ra'd 13:28), REC-05 (Al-Baqarah 2:153), REC-06 (At-Talaq 65:2-3), REC-07 (Al-Mulk 67:1-2), REC-08 (Al-'Asr 103 entière). Traductions Hamidullah vérifiées par recherche web (quran.com/fr, quran-uni.com) ; texte arabe à revérifier au montage sur quran.com + alquran.cloud comme d'habitude. Récitateur proposé par défaut : Abou Bakr Ash-Shâtirî (comme REC-01/02), à confirmer par Mo.
- 09/10/2026 (soir, suite) : Mo a déposé dans le chat l'audio de 5 récitateurs réels (vidéos mp4, audio extrait en mp3) pour REC-03, REC-04, REC-05, REC-07, REC-08 — récitateurs : Mishary Alafasy (REC-03, REC-05, REC-07), Abou Bakr Ash-Shâtirî (REC-04), Wadee' Al-Yamani (REC-08). Nouveau dossier `audio/recitations/<ID>.mp3` créé pour cet usage (distinct de `voix/fr/`, réservé à la voix ElevenLabs du narrateur). At-Talaq (ancien REC-06) écarté par Mo (verset trop long) et remplacé par Az-Zumar 39:53 (nouveau REC-06). Mo a demandé 2 versets de plus pour arriver à 8 vidéos sur le mois : REC-09 (Al-Ikhlas 112, sourate entière) et REC-10 (Yunus 10:62).
- 09/10/2026 (soir, fin) : audio déposé pour les 3 derniers — Al-Ikhlas (REC-09, Alafasy) et Az-Zumar 39:53 (REC-06, Alafasy) nommés clairement ; le 3e fichier (vidéo WhatsApp sans nom) a été confirmé par Mo : Yunus 10:62, récitateur Wadee' Al-Yamani. Les 8 récitations du lot ont maintenant leur audio et sont prêtes pour relecture avant montage.
- 09/10/2026 (nuit, suite) : lot de 18 photos (#PHOTO) écrit pour couvrir les 2 prochains mois à raison de 2/semaine (mardi + jeudi, 13/10 au 10/12/2026), à la demande de Mo — exception assumée à la règle « 1-2 cycles par lot #SCRIPT » (signalée et validée par Mo avant d'écrire). 10 hadiths (Bukhârî, Muslim, Tirmidhî), 7 versets (trad. Hamidullah, vérifiés sur quran.com/fr), 1 invocation (Abû Dâwud 1522). Aucun doublon avec les sources déjà utilisées (PHO-S1, vidéos, récitations). Traductions des hadiths faites à partir du texte anglais de sunnah.com : arabe et traduction à reconfirmer au montage, comme pour les scripts de récitation. Fichier : `scripts/fr/PHO-lot-02-oct-dec.md`.
- 09/10/2026 (nuit, fin) : les 18 photos du lot ci-dessus ont été rendues (moteur `moteur/photo/`, gabarit `photo.html` réutilisé tel quel) et livrées à Mo en un ZIP. Arabe de chaque hadith reconfirmé sur sunnah.com (et des versets sur quran.com/api.alquran.cloud) avant le rendu, donc la note « à reconfirmer au montage » ci-dessus est levée pour ce lot — il reste seulement la relecture finale par une personne de confiance avant publication (règle §8.8). Images dans `images/par_contenu/PHO-lot-02-oct-dec/`.
- 09/10/2026 (nuit, suite 2) : **changement de plan** — Mo a demandé la version anglaise maintenant, au lieu d'attendre les 3-5 mois prévus au §11. Signalé à Mo avant d'exécuter ; confirmé. Les 18 photos du lot PHO-02/19 ont été refaites en anglais (mêmes sources, même arabe) : traductions **réelles**, pas retraduites du français — hadiths depuis la traduction anglaise officielle de sunnah.com (citée telle quelle), versets en **Saheeh International** (quran.com), chaque page revérifiée par fetch le 09/10/2026. Fichier : `scripts/en/PHO-lot-02-oct-dec.md` ; images : `images/par_contenu/PHO-lot-02-oct-dec-en/`. Le reste du plan anglais (voix ElevenLabs en anglais, vidéos) n'a pas changé : toujours en attente, à décider par Mo contenu par contenu.
- 09/10/2026 (nuit, suite 3) : 5 histoires de compagnons proposées à Mo pour les 4 prochaines vidéos du vendredi ; Mo a validé les 5 (« on fais les 5 je les aime toutes »). 5 scripts #VID écrits : VID-04-jafar (Ja'far ibn Abi Talib, Musnad Ahmad 1740 hasan), VID-05-umar (Umar ibn al-Khattab, Tirmidhî 3681 + Bukhârî 3684), VID-06-salman (Salman al-Farisi, Musnad Ahmad, type sîra), VID-07-khabbab (Khabbab ibn al-Aratt, Bukhârî 3852/6943), VID-08-sad (Sa'd ibn Abi Waqqâs, Muslim 1748c). Deux points signalés à Mo avant d'écrire (règle « pas de récits populaires sans source solide ») : pour Umar, le récit de la sœur Fatima est écarté (chaîne faible/munkar selon al-Dhahabî) et remplacé par l'invocation du Prophète ﷺ + le témoignage d'Ibn Mas'ûd ; pour Khabbab, le détail des braises sur le dos est écarté (Ibn Mâjah 153, da'if) et remplacé par la plainte à l'ombre de la Ka'ba. Les 5 scripts sont en attente de validation de Mo avant « ok voix ».
- 10/10/2026 : retours de Mo sur les 5 scripts, appliqués. Ja'far : noms réels des envoyés de Quraysh ajoutés (Amr ibn al-'Âs, Abdallah ibn Abi Rabî'a) ; Mo a demandé une vraie récitation audio (plutôt qu'une description) pour la scène Maryam — accepté, récitateur confirmé : **Mishary Alafasy**, audio à déposer dans `audio/recitations/VID-04-jafar.mp3`. Umar : Mo a demandé plus de détail sur « la façon dont il s'est converti » et « la peur des compagnons » — signalé que cette scène précise (Dar al-Arqam, épée, Hamza) appartient à la même chaîne faible/munkar que le récit de la sœur déjà écarté ; deux options proposées, **Mo a choisi l'option A** (rester 100% sourcé, texte étoffé avec le contexte authentique). Khabbab et Sa'd : enrichis avec des détails authentiques supplémentaires tirés des hadiths complets (Bukhârî 3612/3852 pour Khabbab ; Bukhârî 3728 pour Sa'd) suite au retour « trop générique ». Sa'd : correction du prénom « Hamna » (non sourcé, retiré). Salman : inchangé, validé tel quel.
- 10/10/2026 (suite) : étapes suivantes demandées par Mo et réalisées : (1) estimation du coût ElevenLabs (`estimate_only`, Eleven v3, 1 prise, voix Sébastien) pour les 5 scripts — total ~10 304 crédits (~1,87 $), détail par vidéo dans le chat ; (2) PDF unique des 5 scripts français livré à Mo (`Sabil-Nour-5-scripts-VID-fr.pdf`) ; (3) version anglaise des 5 scripts écrite (`scripts/en/VID-04-jafar.md` à `VID-08-sad.md`, traductions réelles depuis les sources anglaises déjà vérifiées, pas retraduites du français) — statut « script à valider », en attente que Mo valide d'abord les versions françaises avant de passer à l'anglais ; (4) document des prompts d'images (anglais, 5 histoires, 76 images au total) livré à Mo pour usage dans ChatGPT, avec consigne d'un ZIP par histoire en sortie.
- 10/10/2026 (nuit) : sur ordre de Mo (« fais moi les voix off en francais »), génération réelle (facturée, 1 prise, Eleven v3, voix Sébastien – Narrator) de la voix off française des 5 scripts #VID validés. Durées/coûts : VID-04-jafar 230 s / 2776,72 crédits ; VID-05-umar 138,4 s / 1880,81 crédits ; VID-06-salman 183,6 s / 2356,76 crédits ; VID-07-khabbab 101,36 s / 1728,83 crédits ; VID-08-sad 125,04 s / 1560,84 crédits — total ≈ 10 304 crédits, conforme aux estimations faites avant génération. Les 5 liens de flow ElevenLabs ont été donnés à Mo (téléchargement bloqué côté Claude, cf. §3) pour qu'il dépose chaque MP3 dans `voix/fr/<ID>.mp3`. Catalogue mis à jour en conséquence ; versions anglaises des voix et des vidéos toujours en attente, à ne commencer qu'après validation complète des 5 vidéos françaises (demande explicite de Mo).
- 10/10/2026 (nuit, suite) : voix anglaise choisie — Mo a demandé une voix calme, posée, profonde, adaptée au récit religieux ; 3 voix de la bibliothèque ElevenLabs proposées sans coût (recherche gratuite, aucune génération) : Keanu, Darren, Rafaga. **Mo a choisi Rafaga** (`voice_id` `68sMPAsdt7bCNPLgaEmA`). Inscrite au §3 pour servir à toutes les futures voix off anglaises du canal. Première voix off anglaise générée le même soir en test (VID-04-jafar, 163,68 s, 2 696,73 crédits). Mo a aussi comparé avec une autre voix de la bibliothèque (Nathan – Deep Podcast Narrator, écoutée gratuitement via l'aperçu, aucune génération) avant de confirmer définitivement **Rafaga**.
- 10/10/2026 (nuit, fin) : question de la récupération de l'audio **fermée définitivement** après vérification de l'état du proxy réseau : `storage.googleapis.com` est refusé par la politique d'organisation (403, policy denial), indépendamment du modèle utilisé. §3 et §13 mis à jour avec les deux seuls chemins possibles (Mo télécharge et dépose sur GitHub, ou Mo joint le fichier au chat et Claude le pousse). Pour contourner la lenteur de l'interface ElevenLabs Flows (Mo la trouve trop compliquée), Claude a pris l'habitude de donner directement les liens de téléchargement signés (`master_url`/`content_url`, valables ~2h) en plus du lien de flow.
- 10/10/2026 (nuit, suite) : Mo a confirmé **Rafaga** comme voix anglaise définitive après avoir comparé avec Nathan (Deep Podcast Narrator, écoutée gratuitement, non retenue). Les 4 histoires anglaises restantes ont été générées (1 prise, Eleven v3, Rafaga) : VID-05-umar 99,52 s / 1 760,82 crédits ; VID-06-salman 167,36 s / 2 293,77 crédits ; VID-07-khabbab 94,56 s / 1 653,83 crédits ; VID-08-sad 97,76 s / 1 481,85 crédits. Avec le test de Ja'far (163,68 s / 2 696,73 crédits), les 5 voix anglaises sont complètes — total ≈ 9 887 crédits. En attente que Mo télécharge les 5 MP3 et les dépose dans `voix/en/<ID>.mp3`. Catalogue mis à jour.
- 10/10/2026 (matin) : Mo a envoyé les 5 MP3 français (déposés dans `voix/fr/<ID>.mp3`) et un ZIP de 21 images pour VID-04-jafar (plus que les 18 prévues : quelques variantes supplémentaires sur la scène de la récitation/pleurs, utiles pour le montage). Images vérifiées une à une (aucun visage, respect du style demandé, arche finale conforme) puis renommées `VID-04-jafar_S_<n°scène>_<sujet>.png` et déposées dans `images/par_contenu/VID-04-jafar/`. Poussé sur GitHub ; catalogue mis à jour. VID-04-jafar est maintenant prêt pour le montage (voix + images complètes). Les 4 autres histoires ont leur voix FR mais attendent encore leurs images.
- 10/10/2026 (matin) : **montage de VID-04-jafar (FR)** fait dans la même discussion que les scripts, à la demande explicite de Mo (« fais la première vidéo maintenant »), exception à la règle « une discussion = une tâche ». Moteur : copie de `video-longue-musab` → `moteur/video-longue-jafar/` (nouvelle référence des vidéos du vendredi). Nouveautés validées par Mo : (1) **vraie récitation insérée** pour la scène Maryam — Mishary Alafasy, Maryam 19:1-4 (audio envoyé par Mo, vérifié par transcription de l'arabe, coupé juste après « رَبِّ شَقِيًّا » car le début du v. 5 suivait), écran émeraude + arche (image J18) avec arabe (quran.com, Uthmani) + traduction Hamidullah (quran.com) verset par verset ; **aucun son, aucun fond vocal, aucun effet sous le Coran** (vérifié : 0 dans les pistes effets et fond pendant la récitation) ; audio rangé dans `audio/recitations/VID-04-jafar.mp3`. (2) **Motion design avec objets détourés**, **à quelques endroits seulement** (précision de Mo : pas partout) : cadeaux de Quraysh qui tombent, cruche/pain puis mains en prière pendant les valeurs du discours, bâton du Négus posé à terre, cadeaux rendus qui sortent du cadre — fond crème #F4F1EA, sous-titres à l'encre (#141414, mot clé émeraude) sur ces plans ; détourés dans `images/par_contenu/VID-04-jafar/detoures/`. Pauses : minimums du §3 appliqués automatiquement (jamais de raccourcissement), cartes de chapitre sur 3,3 s de silence, 7 chapitres. Durée 298,5 s (≤ 5 min). Miniatures « UN ROI… / A PLEURÉ. » (trône vide) dans `images/par_contenu/VID-04-jafar/miniatures/`. Le MP4 pleine qualité (156 Mo) dépasse la limite d'envoi du chat (30 Mo) : aperçu 720p envoyé à Mo pour relecture ; la récupération du fichier final reste à régler (les « releases » GitHub sont refusées pour cette session).
- 10/10/2026 (après-midi) : à la demande de Mo (« on vas creer 8 video pour les 2 mois avenir ») — lot #HADITH de 8 reels hadith couvrant les 2 prochains mois (4 cycles de 14 jours × 2 reels hadith). 8 scripts écrits : HAD-03-grotte (Muslim 2743, les trois hommes dans la grotte), HAD-04-tueur-repenti (Muslim 2766, l'homme qui avait tué cent personnes), HAD-05-trois-epreuves (Bukhârî 3464, le lépreux/le chauve/l'aveugle), HAD-06-voleur-dattes (Bukhârî 2311, Abû Hurayra et le diable déguisé, Ayat al-Kursî), HAD-07-homme-englouti (Bukhârî 5789-5790, l'orgueil puni), HAD-08-branche-epineuse (Bukhârî 652, geste simple récompensé), HAD-09-aumone-nuit (Bukhârî 1421, l'aumône donnée sans savoir à qui), HAD-10-jurayj (Bukhârî 2482, accusé à tort, le bébé qui parle). Toutes les sources vérifiées sur sunnah.com le 10/10/2026 ; aucun doublon avec les hadiths déjà utilisés (HAD-01, HAD-02, COMP-01/02, PHO-S1, PHO-lot-02, RAP-01). Rendu cinéma (référence HAD-02-natte) pour les 8. Catalogue mis à jour (statut « script proposé »). En attente de la validation de Mo (corrections groupées en un seul message), puis « ok voix » pour les 8, puis Mo génère les images (banque encore vide à ce jour) ; une fois les 8 vidéos françaises livrées, Mo a demandé de refaire les 8 en anglais avec leur propre voix off, comme pour les 5 VID (voix Rafaga).
- 10/10/2026 (après-midi, suite) : Mo a validé les 8 scripts sans correction (« oui »). Voix off française générée pour les 8 (1 prise, Eleven v3, Sébastien – Narrator) : HAD-03-grotte 76,9 s / 970,90 crédits ; HAD-04-tueur-repenti 79,7 s / 1041,90 crédits ; HAD-05-trois-epreuves 102,2 s / 1341,87 crédits ; HAD-06-voleur-dattes 99,4 s / 1386,86 crédits ; HAD-07-homme-englouti 18,3 s / 262,97 crédits ; HAD-08-branche-epineuse 18,1 s / 245,98 crédits ; HAD-09-aumone-nuit 73,2 s / 991,90 crédits ; HAD-10-jurayj 84,3 s / 999,90 crédits — total ≈ 7 242 crédits (≈ 1,32 $), conforme à l'estimation. Les 8 liens de téléchargement (signés, valables ~2h) et le lien de flow ElevenLabs ont été donnés à Mo (téléchargement bloqué côté Claude, cf. §3) pour qu'il dépose chaque MP3 dans `voix/fr/<ID>.mp3`. Catalogue mis à jour (statut « voix générée, en attente du dépôt du MP3 »).
- 10/10/2026 (après-midi, fin) : Mo a joint les 8 MP3 au chat (contournement du blocage de téléchargement, cf. §3). Fichiers vérifiés (MP3 valides, non vides) et déposés dans `voix/fr/HAD-03-grotte.mp3` à `voix/fr/HAD-10-jurayj.mp3`, poussés sur GitHub. Catalogue mis à jour (statut « voix FR déposée ; images en attente », champ `voix` renseigné pour les 8). Prochaine étape : Mo génère/fournit les images (vérifier `images/banque/` d'abord, encore vide) pour chacun des 8 reels avant montage.
- 10/10/2026 (après-midi) : Mo a envoyé 7 ZIP d'images pour les reels hadith (H3_11, H4_08, H5_11, H6_06, H7_06, H8, H10 — soit HAD-03, 04, 05, 06, 07, 08 et 10 ; **HAD-09-aumone-nuit manquant**, aucun fichier reçu pour cet ID). Images vérifiées une à une par échantillonnage (format 940/941×1672, conforme au 9:16 de référence HAD-02-natte ; aucun visage visible, dos/capuches/ombre partout où des personnes apparaissent, conforme à la règle du §8) puis renommées `<ID>_<nom original>.png` et déposées dans `images/par_contenu/HAD-0{3,4,5,6,7,8}-*/` et `images/par_contenu/HAD-10-jurayj/` (57 images au total ; HAD-03 et HAD-05 ont une image bonus en plus des prompts prévus). Poussé sur GitHub. Catalogue et §12 mis à jour (statut « prêt pour montage ») pour les 7 complets ; HAD-09 reste au statut « voix FR déposée ; images en attente ». **Point de vigilance signalé à Mo** : l'image H10_06 (Jurayj traîné dehors) montre, à travers une porte ouverte à l'arrière-plan, une forme ressemblant à un crucifix avec bougies sur un mur intérieur — à vérifier/recadrer au montage si jugé gênant.
- 10/10/2026 (soir) : Mo a envoyé les 6 images de HAD-09 (renommées H9_01 à H9_06 selon les prompts) et demandé de flouter le crucifix d'arrière-plan de H10_06 (fait). Même traitement appliqué, par cohérence, à deux autres croix repérées au contrôle : gravée au-dessus de la porte de l'ermitage du moine (H4_02) et sur le pignon de l'ermitage (H10_01). **Les 8 reels hadith HAD-03 à HAD-10 (FR) montés** avec un **nouveau moteur commun** `moteur/hadith-cinema-commun/` (un `cfg.py` + `script.txt` par reel, voir son README) qui reprend le rendu cinéma validé de HAD-02 (photo plein cadre + mouvement de caméra, poussière dans la lumière, sous-titres mot à mot, mots clés dorés, citations en italique, mot fort « frappé » avec riser + impact, fond vocal sans instrument, −14 LUFS). Pauses minimales du §3 ajoutées automatiquement (jamais de raccourcissement). Fin : silence 1,2 s → carte arabe + traduction + source → Abonne-toi. Textes arabes des cartes finales copiés de sunnah.com (Muslim 2743 et 2766, Bukhârî 3464, 2311, 5789, 652, 1421, 2482). Sur les phrases où parle le Prophète ﷺ (HAD-06), uniquement des plans sans personnage (pièce vide, lumière). Sur demande de Mo, images partagées entre histoires quand le décor correspond (H9_01 dans HAD-06, H8_05 dans HAD-09, H3_07 dans HAD-10). Images non utilisées : H5_04 (femme aux cheveux longs, hors sujet : l'histoire ne parle que de trois hommes). Durées : HAD-03 87,0 s ; HAD-04 90,5 s ; HAD-05 114,1 s ; HAD-06 112,3 s ; HAD-07 27,7 s ; HAD-08 27,6 s ; HAD-09 84,9 s ; HAD-10 95,3 s (au-delà des 30–45 s visés au §4 pour 6 d'entre eux, la longueur étant fixée par les voix validées). Miniatures 1080×1920 seulement (reels) dans `images/par_contenu/<ID>/miniatures/`. MP4 pleine qualité trop lourds pour le chat (> 30 Mo) : copies de livraison compressées envoyées à Mo ; MP4 finaux à ranger dans Google Drive (`Sabil Nour/Rendus/`). Prochaine étape : relecture de Mo + personne de confiance, puis versions anglaises (voix Rafaga).
- 10/10/2026 (après-midi) : **VID-05 à VID-08 montés (FR)** à la suite, sur demande de Mo (« fais-les toutes une à une »), avec un **moteur commun** : `moteur/video-longue-commun/` (un `cfg.py` + `script.txt` par vidéo ; `setup.sh` → `align.py` → `core_timeline.py` → `build_html.py` → `render_full.sh` → `prep_delivery.py`). Durées : Umar 160 s, Salman 210 s, Khabbab 129 s, Sa'd 145 s (sous les 4–5 min, longueur fixée par les voix validées). Motion design objet détouré **à quelques endroits seulement** (Umar : sabre ; Salman : chaînes, dattes, cadeau ; Khabbab : marteau, mouton ; Sa'd : arc, bol et cruche). Sur demande de Mo, **images partagées entre histoires** quand le lieu correspond (La Mecque/Ka'ba d'Umar dans Khabbab et Sa'd, caravane de Salman dans Khabbab, désert/Ka'ba de Khabbab dans Umar). **Images écartées pour le respect des règles** : `SA15` (dos nu « sceau de la prophétie » = représentation du Prophète ﷺ, jamais utilisée, fichier renommé `_NE-PAS-UTILISER`) ; `K8` (marcheur avec sac à dos moderne, anachronique, renommé `_NE-PAS-UTILISER`) ; `K4` uniquement recadrée pour cacher le dôme vert (anachronique) ; `SA16` (mains plantant) utilisée seulement sur la phrase où c'est Salman qui doit payer les palmiers, jamais sur la phrase où le Prophète ﷺ les plante ; aucune image de mains sur les invocations du Prophète ﷺ. Corrections moteur : attente du chargement de toutes les images avant rendu (écran noir évité), calage des mots sur les vrais silences élargi, carte titre et carte de chapitre jamais superposées, miniatures à taille de texte automatique. Livraison : le transfert vers l'ordinateur de Mo est limité (30 Mo par fichier, connexion lente) → chaque vidéo est déposée dans `Téléchargements\<Nom>_video` en morceaux de 6 Mo + un `.bat` qui les recolle au bon titre (contrôle d'intégrité fait avant envoi).
