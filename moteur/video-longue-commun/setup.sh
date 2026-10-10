# usage: setup.sh ID   (dans /home/claude/travail/ID)
ID=$1; W=/home/claude/travail/$ID; E=/home/claude/travail/engine; J=/home/claude/travail/VID-04-jafar
cd $W
ln -sfn $J/node_modules node_modules; ln -sfn /home/claude/islam-kit/sons/banque_utilisee bank
cp /home/claude/islam-kit/charte/logo/logo_video_moteur.png img/logo.png; cp /home/claude/islam-kit/charte/grain_papier.png img/grain.png
cp $E/*.py $E/mix.sh $E/asr.mjs .
python3 - <<P
from PIL import Image
import glob,os
for f in glob.glob('raw/*.png'):
    k=os.path.basename(f)[:-4]; Image.open(f).convert('RGB').resize((3344,1882),Image.LANCZOS).save(f'hd/{k}.jpg',quality=92)
print('hd ok')
P
cp /home/claude/islam-kit/voix/fr/$ID.mp3 audio/voix.mp3
ffmpeg -v error -y -i audio/voix.mp3 -ac 1 -ar 48000 audio/voix_t.wav
ffmpeg -v error -y -i audio/voix.mp3 -ac 1 -ar 16000 -f f32le audio/voix16.f32
node asr.mjs audio/voix16.f32 word align_words.json french > asr.log 2>&1
echo SETUP_DONE $ID
