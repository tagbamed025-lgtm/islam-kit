import sys,glob
from PIL import Image
fs=sorted(glob.glob('/tmp/claude-0/s2_*.jpg'));cols=6;w,h=270,480
S=Image.new('RGB',(w*cols,h*((len(fs)+cols-1)//cols)),'white')
for i,f in enumerate(fs): S.paste(Image.open(f).resize((w,h)),(w*(i%cols),h*(i//cols)))
S.save(sys.argv[1],quality=85);print(len(fs))
