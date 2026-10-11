DUR=$(python3 -c "import json;print(json.load(open('data.json'))['DUR'])")
ffmpeg -y -v error -i voice_final.wav -i sfx.wav -i pad.wav -filter_complex "
[0:a]aresample=48000,highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,apad=whole_dur=$DUR,asplit=2[v1][v2];
[2:a]aresample=48000,volume=${PADV:-0.26}[pd];
[pd][v2]sidechaincompress=threshold=0.03:ratio=6:attack=10:release=400[pdk];
[v1][1:a][pdk]amix=inputs=3:duration=first:normalize=0:weights='1 0.9 1',atrim=0:$DUR[o]" -map "[o]" -ar 48000 -c:a pcm_f32le raw.wav
I=$(ffmpeg -i raw.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
G=$(python3 -c "print(-14-($I))")
ffmpeg -y -v error -i raw.wav -af "volume=${G}dB,alimiter=limit=0.84:attack=3:release=60:level=disabled" -ar 48000 -c:a pcm_s16le mix.wav
echo "I=$I gain=$G"
