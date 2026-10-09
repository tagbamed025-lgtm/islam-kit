import json
d=open('data.json').read()
open('index.html','w').write(open('engine.html').read().replace('__DATA__',d))
print('ok')
