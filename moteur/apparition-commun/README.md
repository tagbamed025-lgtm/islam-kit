# Moteur commun — reels compagnons « apparition » (9:16)

Créé le 11/10/2026 pour COMP-03 à COMP-06. Reprend le rendu de référence `apparition-lampe-ansar/` (COMP-02) — fond crème #F4F1EA + grain, objets détourés avec ombre douce, mots qui montent un à un, mot clé émeraude « frappé », scènes de nuit (mot clé doré), flash de lumière, carte de citation, carton « Ce qu'on retient », Abonne-toi — mais piloté par un `cfg.py` par reel au lieu d'un HTML écrit à la main.

## Dossier de travail d'un reel : `/home/claude/travail/comp/<ID>/`
- `script.txt` : texte réellement prononcé, une phrase par ligne (si ElevenLabs a lu « ﷺ » en formule complète, l'écrire en toutes lettres) ;
- `voix_t.wav` (48 kHz mono) et `voix16.f32` (16 kHz f32) depuis `voix/fr/<ID>.mp3`, puis `node asr.mjs <dossier>` lancé depuis `/home/claude/travail/had` (node_modules + modèle Whisper) → `align_words.json` ;
- `cfg.py` : `ID`, `TAG` (bandeau du haut, HTML), `TITLE` (= nom du MP4), `THUMB`, `SCENES`.

## SCENES
Une scène = `dict(at=…, kind=…, img=…, cut=…, blocks=[…], …)` :
- `at` : ligne n (0 = première) ou `(n, 'mot')` ; la scène dure jusqu'à la suivante ; la dernière (`kind='retient'`) tient jusqu'à fin de voix + 1,2 s + 3,4 s, puis Abonne-toi (3 s) est ajouté automatiquement.
- `kind` : `obj` (défaut : objet détouré `cut=True` ou photo fondue dans le crème), `night` (fond nuit, image assombrie, texte crème, mot clé doré + son de suspense), `text` (texte seul centré), `card` (carte blanche + « sur photo floutée, pour les paroles rapportées), `retient` (puce CE QU'ON RETIENT + objet + leçon + source).
- `blocks` : `(style, texte[, taille])` ; styles `a` Anton encre, `A` Anton émeraude frappé, `G` Anton doré frappé, `c` Cormorant italique, `i` Inter petites capitales. Le texte reprend les mots de la phrase dite : chaque mot apparaît à son temps réel ; `ﷺ` absorbe la formule prononcée.
- options : `chip`, `src`, `flash`, `shake=(n,'mot')`, `big` (index du bloc frappé avec riser + impact cinéma), `pop`, `focus=[x,y]` (photo), `zin=False` (dézoom), `zoom`.
- Images cherchées dans `images/par_contenu/COMP-*/` : `<ID>_<k>.png` (photo) ou `<ID>_cut_<k>.png` (détourée rembg `isnet-general-use`).
- Règle : aucun plan de mains ou de silhouette sur une phrase où parle ou agit le Prophète ﷺ.

## Chaîne
`build.sh <dossier>` : images → `align.py` → `timeline.py` (pauses minimales bible §3, jamais de raccourcissement ; scènes → `data.json`) → `build_html.py` (`tpl.html`) → `render.py ev` → `sfx.py` + `pad.py` (fond vocal sans instrument) → `mix.sh` (−14 LUFS).
`check.sh` (dans le dossier) : planche, une image par scène. `final.sh <dossier> 2` : rendu → `out/<titre>.mp4` + miniatures 1080×1920 et 1280×720 (`thumb.py`). Machine à 2 cœurs : rendre les reels l'un après l'autre (`run_all.sh`).
