import os
here=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(here,'tpl.html'),encoding='utf-8').read().replace('__DATA__',open('data.json',encoding='utf-8').read())
open('index.html','w',encoding='utf-8').write(s); print('index.html ok')
