import json, re, difflib

SCRIPT = """Au lendemain de la bataille d'Uhud, les compagnons veulent envelopper un martyr pour l'enterrer.
Ils n'ont qu'un seul morceau de tissu. Un vieux manteau.
Quand ils couvrent sa tête… ses pieds apparaissent.
Quand ils couvrent ses pieds… c'est sa tête qui apparaît.
Cet homme… était autrefois le jeune homme le plus élégant de La Mecque.
Voici l'histoire de Mus'ab ibn Umayr.
Mus'ab est né dans l'une des familles les plus riches de Quraysh.
Sa mère le couvrait de ce que La Mecque avait de plus beau : des habits fins, des sandales venues de loin, les parfums les plus rares.
On raconte que dans les ruelles, on sentait son parfum avant même de le voir passer.
Il était jeune, beau, admiré. Il avait tout ce que ce monde peut offrir.
Mais un jour, il entend parler d'un homme qui appelle à adorer un Dieu unique. Muhammad, paix et salut sur lui.
Mus'ab se rend en secret dans la maison d'al-Arqam, où les premiers musulmans se réunissent.
Il écoute le Coran… et son cœur s'ouvre.
Il embrasse l'islam. Et il le cache. À sa mère, à sa famille, à toute La Mecque.
Mais à La Mecque, un secret ne dure pas.
Un homme le voit prier. Sa famille l'apprend.
Sa mère, qui l'aimait tant, le fait enfermer. On veut le forcer à revenir en arrière.
Il ne renonce pas.
Dès qu'il le peut, il part avec d'autres musulmans vers l'Abyssinie. Loin de sa terre. Loin de son confort.
À son retour, ceux qui l'avaient connu ne le reconnaissent plus. Le jeune homme aux habits de soie porte des vêtements usés.
Il a tout perdu… sauf sa foi.
Puis vient un choix qui va changer l'histoire.
Des hommes de Yathrib, la future Médine, embrassent l'islam. Ils ont besoin de quelqu'un pour leur enseigner le Coran.
Le Prophète, paix et salut sur lui, choisit Mus'ab.
Le compagnon al-Barâ' ibn 'Âzib raconte : « Les premiers à venir chez nous furent Mus'ab ibn Umayr et Ibn Umm Maktûm. Ils enseignaient le Coran aux gens. »
Un jour, un chef, Usayd ibn Hudayr, arrive furieux, sa lance à la main. Il veut chasser cet étranger.
Mus'ab ne s'emporte pas. Il lui dit simplement :
« Assieds-toi et écoute. Si ce que tu entends te plaît, accepte-le. Sinon, nous cesserons de te dire ce qui te déplaît. »
Usayd plante sa lance dans le sol… et s'assoit.
Il écoute le Coran. Et il embrasse l'islam.
Peu après, un autre grand chef, Sa'd ibn Mu'âdh, vit la même scène. Il retourne voir son clan et déclare qu'il ne leur adressera plus la parole tant qu'ils ne croiront pas en Allah et en Son Messager.
Avant la fin du jour, tout son clan est devenu musulman.
Quand le Prophète, paix et salut sur lui, arrive enfin à Médine, la ville l'attend.
Un seul homme avait préparé les cœurs.
L'an 3 de l'Hégire. La bataille d'Uhud.
C'est à Mus'ab qu'on confie l'étendard des musulmans.
Au cœur du combat, il le tient haut. Il ne le lâche pas.
Et il tombe en martyr, l'étendard à la main.
Le compagnon Khabbâb raconte :
« Il fut tué le jour d'Uhud, et nous n'avons trouvé pour l'envelopper que son manteau. Quand nous couvrions sa tête, ses pieds apparaissaient. Quand nous couvrions ses pieds, sa tête apparaissait. »
Alors le Prophète, paix et salut sur lui, leur ordonne de couvrir sa tête… et de poser sur ses pieds un peu d'herbe du désert, l'idhkhir.
Le jeune homme le plus riche de La Mecque… a quitté ce monde sans même un linceul complet.
Des années plus tard, à Médine, les musulmans vivent dans l'aisance.
Un jour, on apporte un repas à 'Abd ar-Rahmân ibn 'Awf, l'un des compagnons les plus riches.
Il regarde la nourriture… et dit :
« Mus'ab ibn Umayr a été tué, et il était meilleur que moi. Il n'avait que son manteau pour linceul. »
Puis : « Je crains que nos bonnes choses nous aient été données d'avance, dans cette vie. »
Et il se met à pleurer.
Khabbâb disait : certains d'entre nous sont partis sans avoir rien goûté de leur récompense ici-bas. Parmi eux… Mus'ab ibn Umayr.
Mus'ab a tout laissé de ce monde.
Pour ce qui dure."""

def norm(w):
    w = w.lower()
    w = re.sub(r"[^a-zàâäéèêëîïôöùûüçœ']", '', w)
    return w

# script words, keep sentence/line breaks as boundaries for grouping
lines = [l.strip() for l in SCRIPT.split('\n') if l.strip()]
script_words = []  # (display_word, line_idx)
for li, line in enumerate(lines):
    for w in line.split(' '):
        if w:
            script_words.append((w, li))

norm_script = [norm(w) for w,_ in script_words]

d = json.load(open('align_words.json'))
chunks = d['chunks']
norm_whisper = [norm(c['text']) for c in chunks]

sm = difflib.SequenceMatcher(a=norm_script, b=norm_whisper, autojunk=False)
ops = sm.get_opcodes()

times = [None]*len(script_words)
for tag, i1, i2, j1, j2 in ops:
    if tag == 'equal':
        for k in range(i2-i1):
            times[i1+k] = chunks[j1+k]['timestamp']
    elif tag == 'replace':
        # map proportionally
        n = i2-i1; m = j2-j1
        if m == 0:
            continue
        for k in range(n):
            j = j1 + min(m-1, round(k * m / max(n,1)))
            times[i1+k] = chunks[j]['timestamp']
    # 'delete' -> script word not found in whisper, leave None to interpolate
    # 'insert' -> whisper word not in script, ignore

# interpolate None (start,end) using neighbors
DUR = float(chunks[-1]['timestamp'][1])
def get_start(t): return t[0] if t and t[0] is not None else None
def get_end(t): return t[1] if t and t[1] is not None else None

# fill missing by nearest known neighbors, linear interpolate index->time
known_idx = [i for i,t in enumerate(times) if t is not None]
for idx in range(len(times)):
    if times[idx] is not None:
        continue
    # find prev/next known
    prev = max([k for k in known_idx if k < idx], default=None)
    nxt = min([k for k in known_idx if k > idx], default=None)
    if prev is None and nxt is None:
        times[idx] = [0,0.3]
    elif prev is None:
        times[idx] = [max(0,times[nxt][0]-0.3), times[nxt][0]]
    elif nxt is None:
        times[idx] = [times[prev][1], times[prev][1]+0.3]
    else:
        t0 = times[prev][1]; t1 = times[nxt][0]
        span = t1-t0
        frac0 = (idx-prev)/(nxt-prev)
        frac1 = (idx-prev+1)/(nxt-prev)
        times[idx] = [t0+span*frac0, t0+span*frac1]

# now group by line (our SCRIPT lines) into align.json phrase chunks
groups = []
cur_line = None
cur_words = []
cur_start = None
for (w,li), t in zip(script_words, times):
    if li != cur_line:
        if cur_words:
            groups.append([[cur_start, prev_end], ' '.join(cur_words)])
        cur_line = li; cur_words=[]; cur_start=t[0]
    cur_words.append(w)
    prev_end = t[1]
if cur_words:
    groups.append([[cur_start, prev_end], ' '.join(cur_words)])

json.dump(groups, open('align.json','w'), ensure_ascii=False, indent=0)
print(len(groups), 'groups, total dur', groups[-1][0][1])
for g in groups[:8]: print(round(g[0][0],2), round(g[0][1],2), g[1])

# also dump per-word timestamps grouped by line, for karaoke-style word reveal
lines_words = []
cur_line = None
cur = []
for (w,li), t_ in zip(script_words, times):
    if li != cur_line:
        if cur: lines_words.append(cur)
        cur_line = li; cur = []
    cur.append([w, round(t_[0],3), round(t_[1],3)])
if cur: lines_words.append(cur)
json.dump(lines_words, open('align_lines.json','w'), ensure_ascii=False, indent=0)
print('lines_words groups:', len(lines_words))
