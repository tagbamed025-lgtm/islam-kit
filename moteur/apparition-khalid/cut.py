from rembg import remove, new_session
from PIL import Image
import numpy as np, glob, os
s=new_session('isnet-general-use')
R='raw/Arabia_Assets_A1-A12/'
def trim(im,pad=8):
    bb=im.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox()
    x0,y0,x1,y1=bb; return im.crop((max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad)))
for name,out in [('A1_Sword','A1'),('A2_Broken_Sword','A2'),('A8_Helmet_Chainmail','A8'),('A9_Lit_Oil_Lamp','A9'),('A9b_Extinguished_Oil_Lamp','A9b'),('A12_Mount_Uhud','A12')]:
    im=Image.open(R+name+'.png').convert('RGB')
    o=remove(im,session=s)
    trim(o).save(f'img/{out}.png'); print(out,o.size)
for name,out in [('A3_Banner','A3'),('A4_Horseman','A4'),('A5_Rearing_Horse','A5'),('A6_Bow_Quiver','A6'),('A7_Traveler','A7')]:
    im=Image.open(R+name+'.png').convert('RGBA'); trim(im).save(f'img/{out}.png')
# army: level so grey bg -> white, for multiply
a=np.asarray(Image.open(R+'A10_Byzantine_Army.png').convert('L')).astype(float)
bgv=np.median(a[:40,:]); a=np.clip(a/bgv,0,1)**1.4*255
Image.fromarray(a.astype(np.uint8)).save('img/A10.png')
# dust: luminance -> alpha, sand color
d=np.asarray(Image.open(R+'A11_Dust_Cloud.png').convert('RGB')).astype(float)
L=d.max(axis=2); al=np.clip(L*1.3,0,255)
rgba=np.dstack([d[...,0]*0+196,d[...,1]*0+160,d[...,2]*0+110,al]).astype(np.uint8)
Image.fromarray(rgba,'RGBA').save('img/A11.png')
