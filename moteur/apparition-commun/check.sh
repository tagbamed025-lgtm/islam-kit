# planche de contrôle : un instant par scène (fin de scène) + abonne-toi
E=/home/claude/islam-kit/moteur/apparition-commun
T=$(python3 -c "
import json;D=json.load(open('data.json'))
print(' '.join(str(round(s['e']-.12,2)) for s in D['scenes']),round(D['DUR']-.8,2))")
rm -rf snaps; python3 $E/render.py snap $T
python3 -c "
from PIL import Image;import glob
fs=sorted(glob.glob('snaps/*.jpg'));W,H=270,480;c=8;r=(len(fs)+c-1)//c
s=Image.new('RGB',(W*c,H*r),'white')
for i,f in enumerate(fs):s.paste(Image.open(f).resize((W,H)),((i%c)*W,(i//c)*H))
s.save('snapsheet.jpg',quality=85)"
