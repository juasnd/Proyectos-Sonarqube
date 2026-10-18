#!/usr/bin/env python3
import argparse, csv, random
from collections import defaultdict

p=argparse.ArgumentParser()
p.add_argument('entrada',help='CSV con participant_id y experience_block')
p.add_argument('-o','--salida',default='asignacion.csv')
p.add_argument('--semilla',type=int,default=20260728)
a=p.parse_args()
random.seed(a.semilla)
blocks=defaultdict(list)
with open(a.entrada,encoding='utf-8') as f:
    for r in csv.DictReader(f): blocks[r['experience_block']].append(r['participant_id'])
rows=[]
for block,ids in sorted(blocks.items()):
    random.shuffle(ids)
    for i,pid in enumerate(ids): rows.append({'participant_id':pid,'experience_block':block,'treatment':'control' if i%2==0 else 'experimental','seed':a.semilla})
with open(a.salida,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['participant_id','experience_block','treatment','seed']); w.writeheader(); w.writerows(rows)
print(f'Asignación guardada en {a.salida}')
