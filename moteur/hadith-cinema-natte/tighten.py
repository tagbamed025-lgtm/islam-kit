import re,subprocess,json
r=subprocess.run(['ffmpeg','-i','voix.mp3','-af','silencedetect=noise=-35dB:d=0.2','-f','null','-'],capture_output=True,text=True).stderr
S=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)]; E=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
DUR=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','voix.mp3'],capture_output=True,text=True).stdout)
keep=[];cur=0.0;mapping=[]
for s,e in zip(S,E):
    d=e-s; cap=0.8 if 18.5<s<19.5 else 0.5
    if d>cap:
        a=s+cap/2; b=e-cap/2   # remove middle part
        keep.append((cur,a)); cur=b
keep.append((cur,DUR))
f=';'.join(f'[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={b-a-0.01:.4f}:d=0.01[s{i}]' for i,(a,b) in enumerate(keep))
f+=';'+''.join(f'[s{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=0:a=1[o]'
subprocess.run(['ffmpeg','-y','-v','error','-i','voix.mp3','-filter_complex',f,'-map','[o]','-ar','48000','voix_t.wav'],check=True)
# time map: original -> new
t=0;m=[]
for a,b in keep: m.append([a,b,t]); t+=b-a
json.dump(m,open('tmap.json','w')); print('new dur',round(t,2),'segments',len(keep))
