import json, re, difflib
lines=[l.strip() for l in open('script.txt',encoding='utf-8') if l.strip()]
# tokens: keep ':' '?' etc attached; drop standalone punctuation tokens by merging to previous word
SW=[]
for li,l in enumerate(lines):
    toks=l.split(' ')
    for t in toks:
        if not t: continue
        if re.fullmatch(r"[:;?!»«…]+",t):
            if t=='«': SW.append(['«',li]); continue
            SW[-1][0]+= (' '+t); continue
        if SW and SW[-1][0]=='«' and SW[-1][1]==li: SW[-1][0]='« '+t; continue
        SW.append([t,li])
def norm(w):
    w=w.lower().replace('’',"'")
    return re.sub(r"[^a-zàâäéèêëîïôöùûüçœ]",'',w)
d=json.load(open('align_words.json'))['chunks']
# dedupe ASR chunk overlaps (time going backwards)
C=[];mx=-1
for c in d:
    s,e=c['timestamp']
    if e is None: e=s+.3
    if s < mx-0.3: continue
    C.append([c['text'].strip(),s,e]); mx=max(mx,e)
a=[norm(w) for w,_ in SW]; b=[norm(c[0]) for c in C]
sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False)
T=[None]*len(SW)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag=='equal':
        for k in range(i2-i1): T[i1+k]=C[j1+k][1:3]
    elif tag=='replace':
        n,m=i2-i1,j2-j1
        # spread the span
        s0,e0=C[j1][1],C[j2-1][2]
        for k in range(n): T[i1+k]=[s0+(e0-s0)*k/n, s0+(e0-s0)*(k+1)/n]
known=[i for i,t in enumerate(T) if t]
for i in range(len(T)):
    if T[i]: continue
    p=max([k for k in known if k<i],default=None); n=min([k for k in known if k>i],default=None)
    t0=T[p][1] if p is not None else 0; t1=T[n][0] if n is not None else t0+.3
    cnt=(n-p) if (p is not None and n is not None) else 2
    f0=(i-(p if p is not None else i-1))/cnt; f1=f0+1/cnt
    T[i]=[t0+(t1-t0)*f0, t0+(t1-t0)*f1]
# monotonic fix
for i in range(1,len(T)):
    if T[i][0]<T[i-1][0]: T[i][0]=T[i-1][1]
    if T[i][1]<T[i][0]: T[i][1]=T[i][0]+.05
out=[]
for (w,li),t in zip(SW,T):
    while len(out)<=li: out.append([])
    out[li].append([w,round(t[0],3),round(t[1],3)])
json.dump(out,open('align_lines.json','w'),ensure_ascii=False)
for li,L in enumerate(out): print(li, L[0][1], L[-1][2], ' '.join(x[0] for x in L)[:70])
