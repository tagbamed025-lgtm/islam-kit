cd /home/claude/anas
T="Il sentait le parfum du Paradis avant la bataille – Anas ibn an-Nadr"
python3 rr.py 0 28 p0.mp4 x > r0.log 2>&1 &
python3 rr.py 28 55.95 p1.mp4 x > r1.log 2>&1 &
wait
printf "file 'p0.mp4'\nfile 'p1.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -i audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "$T.mp4"
echo DONE > done.flag
