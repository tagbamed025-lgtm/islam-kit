# usage: python3 prep_delivery.py <dossier vidéo> <préfixe court>
# Découpe le MP4 final en morceaux de 16 Mo (4 premiers octets à part pour éviter toute réécriture du fichier pendant le transfert)
# + un .bat qui recolle tout sous le bon titre, dans /mnt/user-data/outputs/<ID>/
import sys, os, glob, hashlib
d, pre = sys.argv[1], sys.argv[2]
SZ = int(float(sys.argv[3]) * 1024 * 1024) if len(sys.argv) > 3 else 16 * 1024 * 1024
ID = os.path.basename(d.rstrip('/'))
exec(open(os.path.join(d, 'cfg.py'), encoding='utf-8').read().split('# ---- plans ----')[0])
src = os.path.join(d, TITLE_TXT + '.mp4')
data = open(src, 'rb').read()
out = f'/mnt/user-data/outputs/{ID}'; os.makedirs(out, exist_ok=True)
for f in glob.glob(out + '/*'): os.remove(f)
parts = []
chunks = [data[:4]] + [data[4 + i:4 + i + SZ] for i in range(0, len(data) - 4, SZ)]
for i, c in enumerate(chunks):
    n = f'{pre}{i:02d}.bin'; open(f'{out}/{n}', 'wb').write(c); parts.append(n)
title = TITLE_TXT + '.mp4'
bat = ('@echo off\r\nchcp 65001 >nul\r\ncd /d "%~dp0"\r\ncopy /b ' + '+'.join(parts) + f' "{title}" >nul\r\n'
       f'if exist "{title}" (del ' + ' '.join(parts) + ' & echo Video prete. & del "%~f0") else echo Erreur : un morceau manque.\r\npause\r\n')
open(f'{out}/ASSEMBLER_{ID}.bat', 'w', encoding='utf-8').write(bat)
assert hashlib.md5(b''.join(open(f'{out}/{p}', 'rb').read() for p in parts)).hexdigest() == hashlib.md5(data).hexdigest()
print(out, len(parts), 'morceaux', round(len(data) / 1e6, 1), 'Mo')
for p in parts: print(p, os.path.getsize(f'{out}/{p}'))
