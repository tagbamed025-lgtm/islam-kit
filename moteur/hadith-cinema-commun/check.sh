# planche de contrôle : 10 sous-titres complets + carte finale + abonne-toi
E=/home/claude/islam-kit/moteur/hadith-cinema-commun
T=$(python3 -c "
import json;D=json.load(open('data.json'));C=D['chunks'];n=len(C);idx=[round(i*(n-1)/9) for i in range(10)]
print(' '.join(str(round(min(C[i]['w'][-1][2]+.15,C[i]['hide']-.05),2)) for i in idx),round(D['G']+3,2),round(D['H']+2,2))")
rm -rf snaps; python3 $E/render.py snap $T
python3 -c "
from PIL import Image;import glob
fs=sorted(glob.glob('snaps/*.jpg'));W,H=270,480
s=Image.new('RGB',(W*6,H*2))
for i,f in enumerate(fs):s.paste(Image.open(f).resize((W,H)),((i%6)*W,(i//6)*H))
s.save('snapsheet.jpg',quality=85)"
