# usage (dans le dossier de la vidéo) : bash render_full.sh
set -e
python3 ev.py && python3 sfx.py && python3 pad.py && bash mix.sh
DUR=$(python3 -c "import json;print(json.load(open('data.json'))['DUR'])")
bash part.sh 0 $DUR F 2
OUT=$(python3 -c "exec(open('cfg.py',encoding='utf-8').read().split('# ---- plans ----')[0]);print(TITLE_TXT)").mp4
ffmpeg -v error -y -i vid_F.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "$OUT"
python3 - <<'P'
exec(open('cfg.py',encoding='utf-8').read().split('# ---- plans ----')[0])
s=open('/home/claude/travail/engine/thumb_tpl.html',encoding='utf-8').read()
for k,v in TH.items(): s=s.replace('{'+k+'}',v)
s=s.replace('{NAME}',H['NAME'])
n1,n2=len(TH['L1']),len(TH['L2'])
for k,v in {'FS1':min(150,int(1120/(.46*n1))),'FS2':min(110,int(800/(.46*n2))),'FV1':min(170,int(1000/(.46*n1))),'FV2':min(160,int(1020/(.46*n2)))}.items(): s=s.replace('{'+k+'}',str(v))
open('thumb.html','w',encoding='utf-8').write(s)
P
python3 thumbshot.py $(basename $(pwd))
ls -la *.mp4 Miniature_*
echo RENDER_DONE
