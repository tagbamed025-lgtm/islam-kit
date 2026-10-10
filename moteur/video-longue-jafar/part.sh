# usage: part.sh START END NAME [K]
S=$1; E=$2; N=$3; K=${4:-2}
B=($(python3 -c "s=$S;e=$E;k=$K;print(' '.join(str(round((s+(e-s)*i/k)*30)/30) for i in range(k+1)))"))
for ((i=0;i<K;i++)); do python3 rr.py ${B[$i]} ${B[$((i+1))]} seg_${N}_$i.mp4 > rlog_${N}_$i.txt 2>&1 & done; wait
rm -f seglist_$N.txt; for ((i=0;i<K;i++)); do echo "file 'seg_${N}_$i.mp4'" >> seglist_$N.txt; done
ffmpeg -v error -y -f concat -safe 0 -i seglist_$N.txt -c copy vid_$N.mp4 && echo DONE_$N
