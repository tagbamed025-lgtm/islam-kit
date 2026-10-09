cd /home/claude/lampe
T="Ils ont éteint la lampe pour que leur invité mange – Les Ansâr"
python3 rr.py 0 27 p0.mp4 x > r0.log 2>&1 &
python3 rr.py 27 53.6 p1.mp4 x > r1.log 2>&1 &
wait
printf "file 'p0.mp4'\nfile 'p1.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -i audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "$T.mp4"
echo DONE > done.flag
