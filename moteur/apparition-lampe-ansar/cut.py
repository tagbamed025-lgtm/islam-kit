from rembg import remove, new_session
from PIL import Image
s=new_session('isnet-general-use')
def trim(im,pad=8):
    bb=im.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox()
    x0,y0,x1,y1=bb; return im.crop((max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad)))
for n in ['L2','L3','L4','L5','L7']:
    o=remove(Image.open(f'raw/{n}.png').convert('RGB'),session=s); trim(o).save(f'img/cut_{n}.png'); print(n,o.size)
