"""Reproducible assertions for Rev. C; run after netlist_review.py."""
import csv
import itertools
import json
import math
import re
from pathlib import Path
from netlist_review import distance

P=Path('tmp/pdfs/review')
d=json.loads((P/'netlist.json').read_text(encoding='utf-8'))
def net(x,y):
    hit=min((distance((x,y),s['a'],s['b']),n) for n,ss in d['nets'].items() for s in ss)
    assert hit[0]<.8, (x,y,hit)
    return hit[1]

assert net(933,175.5)==net(910,214.718)==net(925,223.769)
assert net(933,299)==net(910,253.907)==net(925,253.907)
assert net(933,175.5)!=net(933,299)
assert net(904,223.7)==net(948,244.6) # U16A/D gates = B
assert net(948,214.7)==net(904,244.85) # U16B/C gates = A
assert net(904,223.7)!=net(948,214.7)
assert net(1110,290.07)!=net(1110,293.085) # M versus Mbar
assert net(323.5,68)==net(344.2,65) # U19.12 to R38 top
assert len({net(323.5,68),net(344.2,80),net(335,82.1),net(362,82)})==4
assert net(250,48)==net(300,58)==net(391,82) # R86/C1 after R39
assert net(391,82)!=net(372,82) # before/after R39 are separate

rows=[]
switches=['U1A U2A U2B','U1B U2C U2D','U1C U3A U3B','U1D U3C U3D',
          'U4A U5A U5B','U4B U5C U5D','U4C U6A U6B','U4D U6C U6D',
          'U7A U9A U9B','U7B U8A U8B','U7C U9C U9D','U7D U8C U8D',
          'U10A U11A U11B','U10B U11C U11D','U10C U12A U12B','U10D U12C U12D']
for n in range(1,17):
    col=(n-1)//8; row=(n-1)%8
    x0=66+344*col; y0=43+72.337*row+3.015*col
    words=[w['text'] for w in d['words'] if x0<=w['box'][0]<x0+355 and y0<=w['box'][1]<y0+69]
    # Text layer emits Rr63; the 400-dpi crop reads R63, the output resistor.
    found=set(re.findall(r'\b(?:R\d+|C\d+|Q\d+|U\d+[A-D]?)\b',' '.join(words).replace('Rr63','R63')))
    cfb=1 if n==1 else 2*n+1
    expected={f'R{i}' for i in (3+n,83+2*n,84+2*n,34+3*n,35+3*n,36+3*n)}
    expected|={f'C{cfb}',f'C{cfb+1}',f'U{18+n}',f'Q{2*n-1}',f'Q{2*n}'}|set(switches[n-1].split())
    assert not expected-found, (n,expected-found,words)
    rows.append([n,f'{(n+1)//2}{"а" if n%2 else "б"}',round(x0,2),round(y0,2),';'.join(sorted(expected)),'PASS'])
with (P/'channel-audit.csv').open('w',encoding='utf-8-sig',newline='') as f:
    csv.writer(f).writerows([['n','channel','x0_pt','y0_pt','observed_designators','result']]+rows)
md=Path('PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md').read_text(encoding='utf-8')
for row in rows:
    line=next(l for l in md.splitlines() if l.startswith('| **'+row[1]+'** |'))
    written=set(re.findall(r'\b(?:R\d+|C\d+|Q\d+|U\d+[A-D]?)\b',line))
    assert set(row[4].split(';'))<=written, (row[1],set(row[4].split(';'))-written)
for target in re.findall(r'\]\((tmp/[^)]+)\)',md):
    assert Path(target).exists(), target

k14=301/2911; k15=301/2351; h=12.6*301/10801
phases=[]
for peak in (5*math.sqrt(2),5):
    a14=math.asin(h/k14/peak); a15=math.asin(h/k15/peak)
    phases.append({'peak':peak,'theta14_deg':math.degrees(a14),'theta15_deg':math.degrees(a15),'lead_us':(a14+a15)/(2*math.pi*400)*1e6})
assert 357<phases[0]['lead_us']<359 and 527<phases[1]['lead_us']<530
# Time-domain relay model verifies edge ordering independently of the asin sum.
def simulate(peak,k15_test):
    q14=1; prev_m=prev_x=None; m_rise=[]; x_rise=[]
    samples=20000; period=1/400
    for j in range(2*samples):
        t=j*period/samples; vin=peak*math.sin(2*math.pi*400*t)
        q14=1 if q14*h>k14*vin else -1
        q15=1 if -q14*h>k15_test*vin else -1
        m=-q15; x=-q14
        if j>=samples:
            if m==1 and prev_m==-1: m_rise.append(t)
            if x==1 and prev_x==-1: x_rise.append(t)
        prev_m,prev_x=m,x
    return m_rise,x_rise
for item in phases:
    mr,xr=simulate(item['peak'],k15)
    assert len(mr)==len(xr)==1
    lead=((xr[0]-mr[0])%(1/400))*1e6
    assert abs(lead-item['lead_us'])<.3,(lead,item)
mr,xr=simulate(5*math.sqrt(2),301/(2050000+301))
assert len(mr)==len(xr)==1 # Wrong R24 still produces M pulses
# Ideal steady-state DC polarity, including the externally selected U15 threshold.
for vin in (-5,5):
    states=[]
    for q14 in (-1,1):
        n14=q14*h; n15=-q14*h
        if q14==(1 if n14>k14*vin else -1):
            q15=1 if n15>k15*vin else -1
            states.append((q14,q15,-q15)) # M high when q15 is low
    assert len(states)==1 and states[0][2]==(1 if vin>0 else -1)
# Counterexample to "R24=2.05Mohm means U15 never switches":
assert (1 if h>0 else -1) != (1 if -h>0 else -1)
offset_bounds=[]
for ri,rf,rp,ron in itertools.product((9900,10100),(9900,10100),(4465,4935),(0,100)):
    k=rf/ri; rp+=ron
    # Conservative bound under the stated older 9uA/2.5uA parameter hypothesis.
    e=(1+k)*.007 + rf*2.5e-6 + abs(rf-(1+k)*rp)*9e-6
    offset_bounds.append(e)
result={'k14':k14,'k15':k15,'h':h,'threshold14':h/k14,'threshold15':h/k15,
        'phase':phases,'ratio_min':.99/1.01,'ratio_max':1.01/.99,
        'offset_bound_V_older_hypothesis':max(offset_bounds),
        'tau_fb_s':1e4*1e-8,'fc_fb_Hz':1/(2*math.pi*1e4*1e-8),
        'tau_corr_s':56e-8,'f_corr_Hz':1/(2*math.pi*56e-8),
        'short_rail_model_A':11.9/180,'omitted_Rbias_output_V':9e-6*1e4,
        'fundamental_peak_per_Vin':2/math.pi*abs((2+2j*math.pi*400*.0001)/(1+2j*math.pi*400*.0001))}
(P/'calculations.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS: separate thresholds, U16 gates, M/Mbar; all 16 channel rows; DC states; arithmetic')
print(json.dumps(result,indent=2))
