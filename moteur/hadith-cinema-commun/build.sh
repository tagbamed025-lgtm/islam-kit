# usage : bash build.sh <dossier de travail>   (contient cfg.py, script.txt, voix_t.wav, align_words.json)
set -e
E=/home/claude/islam-kit/moteur/hadith-cinema-commun; R=/home/claude/islam-kit
cd $1; ID=$(basename $1)
ln -sfn /home/claude/travail/had/node_modules node_modules; ln -sfn $R/sons/banque_utilisee bank
mkdir -p img hd; cp $R/charte/logo/logo_video_moteur.png img/logo.png; cp $R/charte/grain_papier.png img/grain.png
python3 - <<P
from PIL import Image; import glob,os
exec(open('cfg.py',encoding='utf-8').read())
need={x[1] for x in SHOTS}|{THUMB['img']}
for k in need:
    if os.path.exists(f'hd/{k}.jpg'): continue
    f=glob.glob(f'$R/images/par_contenu/HAD-*/*_{k}.png')[0]
    Image.open(f).convert('RGB').resize((1620,2880),Image.LANCZOS).save(f'hd/{k}.jpg',quality=92)
P
python3 $E/align.py > align.log; python3 $E/timeline.py; python3 $E/build_html.py
python3 $E/render.py ev; python3 $E/sfx.py; python3 $E/pad.py; bash $E/mix.sh
