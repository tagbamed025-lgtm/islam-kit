# Moteur commun — reels hadith (9:16, rendu cinéma)

Créé le 10/10/2026 pour le lot HAD-03 à HAD-10. Même rendu que `hadith-cinema-natte/` (référence HAD-02), mais piloté par un fichier `cfg.py` par reel au lieu d'un HTML écrit à la main.

## Dossier de travail d'un reel
`/home/claude/travail/had/<ID>/` contient :
- `script.txt` : le texte de la voix off, une phrase par ligne (les numéros de ligne servent d'ancres) ;
- `voix_t.wav` (48 kHz mono) et `align_words.json` (Whisper, mot à mot, via `asr.mjs`) ;
- `cfg.py` : `ID`, `TAG`, `TITLE` (= nom du MP4), `KEY` (mots dorés), `CLIMAX` (ligne, mot) = mot « frappé » (riser + impact), `END` (arabe copié de sunnah.com + traduction + source), `THUMB` (image + 2 lignes de miniature), `SHOTS` = liste de plans `(ancre, image, caméra, effets)`.
  - ancre : `n` = début de la ligne n ; `(n, 'mot')` = début de ce mot ;
  - caméra : `[fx0, fy0, échelle0, fx1, fy1, échelle1]` (point visé en fraction de l'image, 1 = plein cadre) ;
  - effets : `dust` (poussière), `dark` (assombrir), `blur`, `bloom: [x, y, montée]` (halo de lumière), `shake: (n,'mot')`.
  - Une image peut venir d'un autre reel (ex. `H3_07` dans HAD-10) : `build.sh` la cherche dans tout `images/par_contenu/HAD-*`.

## Chaîne
`build.sh <dossier>` : images HD → `align.py` → `timeline.py` (pauses minimales bible §3 ajoutées sans jamais raccourcir, sous-titres, plans → `data.json`) → `build_html.py` (`tpl.html`) → événements → `sfx.py` + `pad.py` (fond vocal, pas d'instrument) → `mix.sh` (−14 LUFS).
`check.sh` (dans le dossier) : planche de contrôle (10 sous-titres + carte finale + abonne-toi).
`final.sh <dossier> [parties]` : rendu Chromium/Playwright → MP4 nommé avec le titre + miniature 1080×1920 (`thumb.py`) dans `out/`.

Fin de chaque reel : silence 1,2 s → carte arabe + traduction + source (4,8 s) → Abonne-toi (2,9 s).
Lignes où parle le Prophète ﷺ : toujours un plan sans personnage (pièce vide, lumière, objets).
