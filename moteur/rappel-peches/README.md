# Rappel typographique — RAP-01-peches (modèle du format #RAPPEL)
Ordre : `timeline.py` (pauses bible §3 + calage mot à mot depuis `words.json` de `asr.mjs`) → `render.py seg i 4` (×4 en parallèle, 30 i/s, frames/) → `pad.py` (fond vocal) → `sfx.py` → `mix.sh` (−14 LUFS) → ffmpeg (x264 CRF 21, AAC 192k) → `thumb.py`.
Entrées : `voice.wav` (MP3 du dépôt en 44,1 kHz mono), `v16.f32` pour Whisper ; polices de `charte/polices/` dans `fonts/` ; `img/grain.png`, `img/logo.png`, `img/fil.png`.
Pour un nouveau Rappel : remplacer dans `timeline.py` les silences mesurés (INS), les mots et les scènes ; dans `index.html` les sources (SRC), l'arabe et le carton de fin.
