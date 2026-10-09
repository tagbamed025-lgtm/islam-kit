# go.sh DIR OUTNAME
D=$1; O=$2; cd /home/claude/musab_reels
DUR=$(python3 -c "import json;print(json.load(open('$D/data.json'))['DUR'])")
B=$(python3 -c "d=$DUR;print(round(d/2*30)/30)")
python3 rr.py 0 $B $D/p0.mp4 $D > $D/r0.log 2>&1 &
python3 rr.py $B $DUR $D/p1.mp4 $D > $D/r1.log 2>&1 &
wait
printf "file 'p0.mp4'\nfile 'p1.mp4'\n" > $D/list.txt
ffmpeg -v error -y -f concat -safe 0 -i $D/list.txt -i $D/audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "$D/$O.mp4"
echo DONE > $D/done.flag
