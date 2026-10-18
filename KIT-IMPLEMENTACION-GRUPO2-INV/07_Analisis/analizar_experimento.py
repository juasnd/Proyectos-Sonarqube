#!/usr/bin/env python3
import argparse, os
import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt

def cliffs_delta(x,y):
    gt=sum(a>b for a in x for b in y)
    lt=sum(a<b for a in x for b in y)
    return (gt-lt)/(len(x)*len(y))

p=argparse.ArgumentParser()
p.add_argument('csv_path')
p.add_argument('-o','--outdir',default='resultados')
a=p.parse_args()
os.makedirs(a.outdir,exist_ok=True)
df=pd.read_csv(a.csv_path)
df=df[df['included']==1].copy()
df['ambiguity_density_100']=df['ambiguity_defects_consensus']/df['total_words']*100
df['defect_free_pct']=df['defect_free_requirements']/df['requirements_count']*100
metrics=['ambiguity_density_100','defect_free_pct','time_minutes','difficulty_1_5']
desc=df.groupby('treatment')[metrics].agg(['count','mean','median','std','min','max'])
desc.to_csv(os.path.join(a.outdir,'descriptivos.csv'))
lines=[]
for metric in metrics:
    c=df.loc[df.treatment=='control',metric].dropna().tolist()
    e=df.loc[df.treatment=='experimental',metric].dropna().tolist()
    if len(c)>0 and len(e)>0:
        u,pv=mannwhitneyu(c,e,alternative='two-sided')
        delta=cliffs_delta(e,c)
        lines.append(f'{metric}: U={u:.3f}; p={pv:.6f}; delta_Cliff(experimental-control)={delta:.3f}')
with open(os.path.join(a.outdir,'pruebas.txt'),'w',encoding='utf-8') as f: f.write('\n'.join(lines))
plt.figure(figsize=(7,4.5))
df.boxplot(column='ambiguity_density_100',by='treatment')
plt.suptitle('')
plt.title('Densidad de ambigüedad por tratamiento')
plt.xlabel('Tratamiento'); plt.ylabel('Defectos por 100 palabras')
plt.tight_layout(); plt.savefig(os.path.join(a.outdir,'densidad_ambiguedad.png'),dpi=180); plt.close()
print('Análisis completado en',a.outdir)
