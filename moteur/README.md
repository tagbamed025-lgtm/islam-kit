# Moteur de montage — Sabil Nour

Chaque dossier est une COPIE de travail d'un contenu livré (HTML d'animation + scripts de calage, sons, rendu, miniatures). Ce ne sont pas des outils génériques : on part du dossier du même format, on le copie dans un dossier de travail, on remplace les textes, la voix et les images.

| Format | Dossier modèle (le plus récent / validé) | Notes |
|---|---|---|
| Reel compagnon (apparition) | `apparition-lampe-ansar/` | **Référence actuelle** (lumière, coupe au noir, flash). Précédents : `apparition-anas/`, `apparition-bilal/`, `apparition-khalid/` |
| Reel hadith (cinéma) | `hadith-cinema-natte/` | V3 validée. `hadith-ancien-chien/` = ancien style, à ne pas copier |
| Vidéo du vendredi (16:9) | `video-longue-jafar/` | **Référence actuelle (10/10/2026)** : même moteur que Mus'ab + pauses bible §3 automatiques (`timeline.py`), plans « motion design » objet détouré sur crème (type `CUT`, à quelques endroits seulement), insertion d'une vraie récitation (type `REC`, `rec_prep.py`, aucun son sous le Coran), rendu en 2 moitiés + fenêtres (`part.sh`, `assemble.sh`). Précédent : `video-longue-musab/` |
| Extrait vertical d'une vidéo longue | `extrait-vertical-musab/` | Mis de côté (décision du 30/09/2026) |
| Récitation | `recitation-kahf/` (structure actuelle) · `recitation-hadid/` | Aucun son sous le Coran |
| Rappel (typographique) | `rappel-peches/` | Pauses bible §3, aucune image, citations sur émeraude + arche |
| Photo | `photo/` | `photo.html`, `photos.json`, `shot.py` (1080×1350) |
| Calage voix → mots | `asr/` | `asr.mjs` (Whisper-small via `@xenova/transformers`) |

## Chaîne de montage
voix MP3 → `tighten.py` (**anciens contenus seulement** : plafond 0,45 s ; pour les nouveaux contenus, NE PAS raccourcir les silences, voir bible §3 « Rythme et pauses ») → 16 kHz mono f32 → `asr.mjs` (horodatage mot à mot) → `events` / `ev.py` → `index.html` (animation déterministe, temps « pause-aware » `N(t)`) → `rr.py` / `render.py` (Chromium + Playwright, 2 segments en parallèle) → `build_audio.py` + `sfx.py` + `pad.py` + `mix.sh` (−14 LUFS) → `go.sh` (concat + mux, nom du MP4 = titre) → `th.py` / `thumb.html` (miniatures).

## Remettre en route dans un dossier de travail
```
mkdir -p ~/travail/<ID> && cp -r moteur/apparition-lampe-ansar/* ~/travail/<ID>/ && cd ~/travail/<ID>
cp ../../moteur/package.json . && npm install        # polices + whisper
ln -s <depot>/sons/banque_utilisee bank               # banque de sons
mkdir img audio && cp <depot>/images/par_contenu/<ID>/* img/
cp <depot>/charte/logo/logo_video_moteur.png img/logo.png && cp <depot>/charte/grain_papier.png img/grain.png
```
- Les HTML chargent les polices depuis `node_modules/@fontsource/...` ; les mêmes `.woff2` sont dans `charte/polices/`.
- Le modèle Whisper vient du paquet npm `sts-whisper-small` (dossier `models/`), chemin réglé dans `asr.mjs` (`env.localModelPath`).
- Outils nécessaires : Python 3 (numpy, scipy, soundfile, playwright, rembg `isnet-general-use`), Node, ffmpeg, Chromium.
- Les chemins d'origine (`/home/claude/...`) sont à adapter dans les scripts (`go.sh`, `rr.py`, `mix.sh`).

## Règles à garder en tête (bible)
Pauses ajoutées au montage (minimums bible §3) · pas de son sur chaque mot · rien sous le Coran · fin = « Ce qu'on retient » + source + Abonne-toi · MP4 nommé avec son titre.
