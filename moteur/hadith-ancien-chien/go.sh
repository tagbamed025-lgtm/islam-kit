#!/bin/bash
cd /home/claude/reel_chien
rm -f done.flag
python3 render.py 0 2 > r0.log 2>&1 &
python3 render.py 1 2 > r1.log 2>&1 &
wait
printf "file 'part0.mp4'\nfile 'part1.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -i audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest Reel_Le_chien_et_le_puits.mp4
echo DONE > done.flag
