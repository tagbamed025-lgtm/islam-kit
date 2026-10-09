# usage: part.sh START END NAME  (rend en 4 morceaux parallèles)
S=$1; E=$2; N=$3
python3 - $S $E > /tmp/cuts.txt <<'P'
import sys; s=float(sys.argv[1]); e=float(sys.argv[2]); k=4
b=[round((s+(e-s)*i/k)*30)/30 for i in range(k+1)]; print(' '.join(map(str,b)))
P
read -a B < /tmp/cuts.txt
for i in 0 1 2 3; do python3 rr.py ${B[$i]} ${B[$((i+1))]} seg_$i.mp4 > rlog_$i.txt 2>&1 & done; wait
printf "file 'seg_0.mp4'\nfile 'seg_1.mp4'\nfile 'seg_2.mp4'\nfile 'seg_3.mp4'\n" > seglist.txt
ffmpeg -v error -y -f concat -safe 0 -i seglist.txt -c copy vid_$N.mp4
D=$(python3 -c "print($E-$S)")
ffmpeg -v error -y -ss $S -t $D -i audio/mix.wav -af "afade=t=in:d=0.05,afade=t=out:st=$(python3 -c "print($D-0.6)"):d=0.6" audio/part_$N.wav
ffmpeg -v error -y -i vid_$N.mp4 -i audio/part_$N.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest Musab_$N.mp4
ls -la Musab_$N.mp4
