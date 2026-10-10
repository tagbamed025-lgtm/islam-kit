# rendu vidéo complet + mux. usage: bash final.sh <dossier> [parts]
E=/home/claude/islam-kit/moteur/hadith-cinema-commun; cd $1; P=${2:-2}
for i in $(seq 0 $((P-1))); do python3 $E/render.py $i $P & done; wait
rm -f list.txt; for i in $(seq 0 $((P-1))); do echo "file 'part$i.mp4'" >> list.txt; done
NAME=$(python3 -c "
exec(open('cfg.py',encoding='utf-8').read())
import re;n=TITLE.replace('|','–');n=re.sub(r'[?:/\\\\\"*<>]','',n);n=re.sub(r'\s+',' ',n).strip();print(n)")
mkdir -p out
ffmpeg -v error -y -f concat -safe 0 -i list.txt -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "out/$NAME.mp4"
python3 $E/thumb.py
echo "RENDU_OK $1 -> out/$NAME.mp4"
