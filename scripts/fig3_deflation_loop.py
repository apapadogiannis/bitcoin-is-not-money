"""Figure 3: deflationary feedback loop in a fixed-supply economy (schematic).
Falling prices -> delayed consumption -> reduced investment -> rising real debt burdens -> falling prices.
Usage: python3 -I fig3_deflation_loop.py DATA_DIR OUT_DIR"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = sys.argv[2]
plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 12})
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis('off')
W, H = 3.2, 1.3
boxes = {'deflation': (0.4, 3.4, 'Falling Prices\n(Deflation)'),
         'delay': (6.4, 3.4, 'Delayed\nConsumption'),
         'investment': (6.4, 0.3, 'Reduced\nInvestment'),
         'debt': (0.4, 0.3, 'Rising Real\nDebt Burdens')}
for x, y, label in boxes.values():
    ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle='round,pad=0,rounding_size=0.08', fc='white', ec='black', lw=0.9))
    ax.text(x + W / 2, y + H / 2, label, ha='center', va='center', linespacing=1.6)
c = {k: (x + W / 2, y + H / 2) for k, (x, y, _) in boxes.items()}
arrow = dict(arrowstyle='->', lw=1.3, color='black', shrinkA=0, shrinkB=0)
ax.annotate('', xy=(boxes['delay'][0], c['delay'][1]), xytext=(boxes['deflation'][0] + W, c['deflation'][1]), arrowprops=arrow)
ax.annotate('', xy=(c['investment'][0], boxes['investment'][1] + H), xytext=(c['delay'][0], boxes['delay'][1]), arrowprops=arrow)
ax.annotate('', xy=(boxes['debt'][0] + W, c['debt'][1]), xytext=(boxes['investment'][0], c['investment'][1]), arrowprops=arrow)
ax.annotate('', xy=(c['deflation'][0], boxes['deflation'][1]), xytext=(c['debt'][0], boxes['debt'][1] + H), arrowprops=arrow)
fig.savefig(f'{OUT}/fig3_deflation_loop.png', dpi=220, bbox_inches='tight', metadata={'Software': None})
fig.savefig(f'{OUT}/fig3_deflation_loop.pdf', bbox_inches='tight', metadata={'CreationDate': None, 'Creator': None, 'Producer': None})
print('Figure 3 written')
