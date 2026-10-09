#!/bin/bash
cd /home/claude/khalid
python3 render.py 0 2 > r0.log 2>&1 &
python3 render.py 1 2 > r1.log 2>&1 &
wait
ffmpeg -v error -y -f concat -safe 0 -i list.txt -i audio/mix2.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest Khalid_V2.mp4
echo DONE > done.flag
