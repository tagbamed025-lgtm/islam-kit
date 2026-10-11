# usage : bash build.sh <dossier de travail>  (cfg.py, script.txt, voix_t.wav, align_words.json)
set -e
E=/home/claude/islam-kit/moteur/apparition-commun; R=/home/claude/islam-kit
cd $1
ln -sfn /home/claude/travail/had/node_modules node_modules; ln -sfn $R/sons/banque_utilisee bank
mkdir -p img; cp $R/charte/logo/logo_video_moteur.png img/logo.png; cp $R/charte/grain_papier.png img/grain.png
python3 - <<P
from PIL import Image; import glob,os,shutil
exec(open('cfg.py',encoding='utf-8').read())
for sc in SCENES+[{'img':THUMB['img'],'cut':THUMB.get('cut')}]:
    k=sc.get('img')
    if not k: continue
    if sc.get('cut'):
        f=glob.glob(f'$R/images/par_contenu/COMP-*/*_cut_{k}.png')[0]; shutil.copy(f,f'img/cut_{k}.png')
    elif not os.path.exists(f'img/{k}.jpg'):
        f=glob.glob(f'$R/images/par_contenu/COMP-*/*_{k}.png')[0]
        Image.open(f).convert('RGB').resize((1080,1919),Image.LANCZOS).save(f'img/{k}.jpg',quality=92)
P
python3 $E/align.py > align.log; python3 $E/timeline.py; python3 $E/build_html.py
python3 $E/render.py ev; python3 $E/sfx.py; python3 $E/pad.py; bash $E/mix.sh
