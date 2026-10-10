# copie de livraison <= 29 Mo (limite d'envoi du chat) : bash deliver.sh <dossier>
cd $1; L=/home/claude/travail/had/livraison; mkdir -p $L
for f in out/*.mp4; do
  n=$(basename "$f"); s=$(stat -c %s "$f")
  if [ $s -le 29000000 ]; then cp "$f" "$L/$n"; else
    d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
    b=$(python3 -c "print(int(29e6*8/$d/1000*0.95)-192)")
    ffmpeg -v error -y -i "$f" -c:v libx264 -preset slow -b:v ${b}k -pass 1 -an -f null /dev/null && \
    ffmpeg -v error -y -i "$f" -c:v libx264 -preset slow -b:v ${b}k -pass 2 -c:a copy -movflags +faststart "$L/$n"
    rm -f ffmpeg2pass*
  fi
  cp out/*_1080x1920.png $L/
done
ls -la $L
