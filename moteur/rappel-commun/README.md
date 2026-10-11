# Moteur commun — Rappels (9:16, typographique + objets détourés)
Créé le 11/10/2026 pour RAP-02 à RAP-05. Même rendu que `rappel-peches/` (RAP-01), piloté par un `cfg.py` par Rappel.

## cfg.py
`ID`, `TAG`, `TITLE` (= nom du MP4), `VOICE` (texte exact envoyé à ElevenLabs), `SOURCES` (carton de fin), `THUMB` (objet + 3 lignes de miniature), `SCENES` :
- `kind: 'c'` = fond crème + 1 objet détouré (`obj`, animation `anim` : rise, pop, drop, open, float, door ; `glow` = mot qui allume le halo) ;
- `kind: 'q'` = fond émeraude + arche (citation) : `chip`, `ar` (arabe vérifié), `src` (source affichée après le dernier mot), `quran: True` = aucun son ni fond vocal.
- `lines` : texte affiché, une ligne par chaîne. `*mot` = mot clé ; `mot|ancre` = calé sur le mot dit « ancre » ; `mot|=` = même temps que le précédent ; ligne `~…` = petite ligne ; espace insécable (` `) pour coller la ponctuation.

## Chaîne (dossier de travail `/home/claude/w/<ID>/` : cfg.py, voice.wav 44,1 kHz mono, words.json de `../rappel-peches/asr.mjs`, fonts/, img/)
`prep.py` (calage mot à mot, pauses minimales bible §3 ajoutées sans jamais raccourcir) → `pad.py` → `sfx.py` → `mix.sh` (−14 LUFS) → `render.py <dossier> seg i n` (images 30 i/s) → ffmpeg x264 CRF 21 + AAC 192k → `thumb.py` (miniature 1080×1920).
Whisper : `npm i @xenova/transformers sts-whisper-small` dans /home/claude/w, une voix à la fois (mémoire).
