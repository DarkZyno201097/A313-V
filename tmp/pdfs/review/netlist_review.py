"""Independent BV.22 vector connectivity; coordinates in pt from top left.

Run from project root. Geometric nets are candidates, not electrical truth:
labels, symbol contacts and all consequential crossings need visual review.
"""
import collections
import json
import math
from pathlib import Path
import pdfplumber

OUT = Path('tmp/pdfs/review')
WIRE = (0.502, 0., 0.251)
PIN = (1., 0., 0.)
DOT = (1., 0., 1.)

def distance(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    d = dx*dx+dy*dy
    t = max(0, min(1, ((p[0]-a[0])*dx+(p[1]-a[1])*dy)/d)) if d else 0
    return math.hypot(p[0]-a[0]-t*dx, p[1]-a[1]-t*dy)

def main():
    assert distance((1,1),(0,0),(2,0)) == 1
    assert distance((3,0),(0,0),(2,0)) == 1
    page = pdfplumber.open('BVTK-A313-V.06.pdf').pages[0]
    raw = [l for l in page.lines if l['stroking_color'] in (WIRE,PIN)]
    seg = [(l['pts'][0],l['pts'][-1],l['stroking_color']) for l in raw
           if math.dist(l['pts'][0],l['pts'][-1]) > .05]
    parent = list(range(len(seg)))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i,j):
        parent[root(j)] = root(i)
    buckets = collections.defaultdict(list)
    for i,(a,b,_) in enumerate(seg):
        for p in (a,b):
            k = (round(p[0]/.3),round(p[1]/.3))
            for dx in (-3,-2,-1,0,1,2,3):
                for dy in (-3,-2,-1,0,1,2,3):
                    for j,q in buckets[(k[0]+dx,k[1]+dy)]:
                        if math.dist(p,q) <= .78: join(i,j)
            buckets[k].append((i,p))
    before_dot = len({root(i) for i in parent})
    dots = [((c['x0']+c['x1'])/2,(c['top']+c['bottom'])/2)
            for c in page.curves+page.rects if c['stroking_color']==DOT]
    for p in dots:
        hit = [i for i,(a,b,_) in enumerate(seg) if distance(p,a,b)<.85]
        for j in hit[1:]: join(hit[0],j)
    before_t = len({root(i) for i in parent})
    tj = []
    # ponytail: quadratic scan is adequate for this single 4k-segment page.
    for i,(a,b,col) in enumerate(seg):
        for p in (a,b):
            for j,(c,d,col2) in enumerate(seg):
                if root(i)==root(j): continue
                if distance(p,c,d)<.3 and min(math.dist(p,c),math.dist(p,d))>.5:
                    tj.append({'point':p,'segments':[i,j]})
                    join(i,j)
    rows=[]
    for ch in sorted(page.chars,key=lambda c:(c['top'],c['x0'])):
        if not rows or abs(ch['top']-rows[-1][0]['top'])>.45: rows.append([])
        rows[-1].append(ch)
    words=[]
    for row in rows:
        groups=[]
        for ch in sorted(row,key=lambda c:c['x0']):
            if not groups or ch['x0']-groups[-1][-1]['x1']>1: groups.append([])
            groups[-1].append(ch)
        for g in groups:
            s=''.join(c['text'] for c in g).strip()
            if not s: continue
            box=[min(c['x0'] for c in g),min(c['top'] for c in g),max(c['x1'] for c in g),max(c['bottom'] for c in g)]
            words.append({'text':s,'box':box})
    nets=collections.defaultdict(list)
    for i,(a,b,col) in enumerate(seg): nets[str(root(i))].append({'id':i,'a':a,'b':b,'color':col})
    for w in words:
        x0,y0,x1,y1=w['box']; p=((x0+x1)/2,(y0+y1)/2)
        near=sorted((distance(p,a,b),root(i)) for i,(a,b,col) in enumerate(seg))
        w['nearest_candidate']=[round(near[0][0],3),near[0][1]]
    data={'size':[page.width,page.height],'raw_segments':len(raw),'nonzero_segments':len(seg),'dots':dots,'nets':nets,'words':words,'T_merges':tj,'before_dots':before_dot,'before_T':before_t}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'netlist.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'text-coordinates.txt').write_text('\n'.join(f"{w['box'][0]:7.2f} {w['box'][1]:7.2f} {w['text']}" for w in words),encoding='utf-8')
    print({k:v for k,v in data.items() if k in ('size','raw_segments','nonzero_segments','before_dots','before_T')})
    print('dots',len(dots),'geometric nets',len(nets),'T merges requiring review',len(tj))

if __name__=='__main__': main()
