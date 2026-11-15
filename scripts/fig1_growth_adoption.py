"""Figure 1: output growth and cryptocurrency adoption in selected Asian economies.
Panel (a): real GDP growth, 2024 and 2025-2026 projections (IMF, 2025, Annex Table 1.1).
Panel (b): overall rank in the 2025 Chainalysis Global Crypto Adoption Index.
Also writes the table behind the figure, with the fixed-base deflation rate implied by Equation (3).
Usage: python3 -I fig1_growth_adoption.py DATA_DIR OUT_DIR"""
import sys, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D, OUT = sys.argv[1], sys.argv[2]
growth = list(csv.DictReader(open(f'{D}/imf_growth.csv')))
rank = {r['economy']: int(r['rank_2025']) for r in csv.DictReader(open(f'{D}/chainalysis_rank.csv'))}
names = [r['economy'] for r in growth]
years = ['2024', '2025', '2026']
g = np.array([[float(r[y]) for y in years] for r in growth])

# Table behind the figure. By Equation (3), with a fixed base and stable velocity the
# steady-state deflation rate equals the growth rate.
with open(f'{OUT}/fig1_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['economy', 'growth_2024', 'growth_2025', 'growth_2026', 'implied_deflation_2025', 'implied_deflation_2026', 'chainalysis_rank_2025'])
    for n, row in zip(names, g):
        w.writerow([n, f'{row[0]:.1f}', f'{row[1]:.1f}', f'{row[2]:.1f}', f'{-row[1]:.1f}', f'{-row[2]:.1f}', rank[n]])

plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 12, 'mathtext.fontset': 'dejavuserif'})
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={'width_ratios': [1.5, 1]})

x = np.arange(len(names)); wd = 0.26
cols = ['#9db0d3', '#4a6fb5', '#1f3a73']
labs = ['2024', '2025 (proj.)', '2026 (proj.)']
for i in range(3):
    a.bar(x + (i - 1) * wd, g[:, i], wd, color=cols[i], edgecolor='black', linewidth=0.8, label=labs[i], zorder=3)
a.set_xticks(x); a.set_xticklabels(names, fontsize=11)
a.set_ylim(0, 8); a.set_yticks(range(0, 9)); a.set_ylabel('Real GDP growth, percent')
a.set_title('(a) Real output growth $g$', fontsize=12)
a.yaxis.grid(True, color='#d9d9d9', zorder=0); a.set_axisbelow(True)
a.legend(frameon=False, fontsize=10, loc='upper right')

y = np.arange(len(names))
r = [rank[n] for n in names]
b.barh(y, r, 0.55, color='#c0392b', edgecolor='black', linewidth=0.8, zorder=3)
for yi, ri in zip(y, r):
    b.text(ri + 0.45, yi, f'#{ri}', va='center', fontsize=11)
b.set_yticks(y); b.set_yticklabels(names); b.invert_yaxis()
b.set_xlim(0, 23); b.set_xticks([0, 5, 10, 15, 20])
b.set_xlabel('Global rank in Chainalysis index (1 = widest use)')
b.set_title('(b) Cryptocurrency adoption, 2025', fontsize=12)
b.xaxis.grid(True, color='#d9d9d9', zorder=0); b.set_axisbelow(True)

for ax in (a, b):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
fig.tight_layout(w_pad=2.0)
meta = {'Software': None}
fig.savefig(f'{OUT}/fig1_growth_adoption.png', dpi=220, bbox_inches='tight', metadata=meta)
fig.savefig(f'{OUT}/fig1_growth_adoption.pdf', bbox_inches='tight', metadata={'CreationDate': None, 'Creator': None, 'Producer': None})
print('Figure 1 written; table in fig1_data.csv')
