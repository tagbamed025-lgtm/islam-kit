set -e
read A0 A1 B0 B1 DUR < windows.txt
f(){ python3 -c "print(round($1*30))"; }
a0=$(f $A0); a1=$(f $A1); b0=$(f $B0); b1=$(f $B1)
cut(){ ffmpeg -v error -y -i vid_A.mp4 -vf "trim=start_frame=$1:end_frame=$2,setpts=PTS-STARTPTS" -an -c:v libx264 -preset veryfast -crf 14 -pix_fmt yuv420p $3; }
cut 0 $a0 p0.mp4; cut $a1 $b0 p2.mp4; cut $b1 99999 p4.mp4
printf "file 'p0.mp4'\nfile 'win1.mp4'\nfile 'p2.mp4'\nfile 'win2.mp4'\nfile 'p4.mp4'\nfile 'vid_B.mp4'\n" > final_list.txt
ffmpeg -v error -y -f concat -safe 0 -i final_list.txt -c copy video_only.mp4
OUT="Il a fait pleurer un roi… avec un seul discours – Ja'far ibn Abi Talib.mp4"
ffmpeg -v error -y -i video_only.mp4 -i audio/mix.wav -map 0:v -map 1:a -vf fps=30 -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "$OUT"
ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames:format=duration -of default=nw=1 "$OUT"
ls -la "$OUT"
