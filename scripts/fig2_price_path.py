"""Figure 2: stylized price-level path under a fixed monetary base, Equation (4).
P_t = M*V / (Y_0 * exp(g t)) = P_0 * exp(-g t), with M = 1.0, V = 1.5, Y_0 = 1 and g = 0.2 (stylized values).
Writes the plotted series and the figure.
Usage: python3 -I fig2_price_path.py DATA_DIR OUT_DIR"""
import sys, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = sys.argv[2]
M, V, Y0, g = 1.0, 1.5, 1.0, 0.2
t = np.arange(0, 11)
Y = Y0 * np.exp(g * t)
P = M * V / Y

with open(f'{OUT}/fig2_price_path.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['t', 'real_output_Y', 'price_level_P', 'money_stock_M'])
    for ti, yi, pi in zip(t, Y, P):
        w.writerow([int(ti), f'{yi:.4f}', f'{pi:.4f}', f'{M:.4f}'])

plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 12, 'mathtext.fontset': 'dejavuserif'})
fig, ax = plt.subplots(figsize=(6.6, 4.4))
ax.plot(t, Y, color='blue', lw=2, label='Real Output $Y_t$')
ax.plot(t, P, color='red', lw=2, label='Price Level $P_t$')
ax.plot(t, np.full_like(t, M, dtype=float), color='gray', lw=2, ls='--', label=r'Fixed Supply $\bar{M}$')
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.set_xticks(range(0, 11, 2)); ax.set_yticks(range(0, 11, 2))
ax.set_xlabel('Time'); ax.set_ylabel('Indexed Value')
ax.grid(True, color='#cccccc')
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=3, fontsize=10, frameon=True, edgecolor='black', fancybox=False)
fig.savefig(f'{OUT}/fig2_price_path.png', dpi=220, bbox_inches='tight', metadata={'Software': None})
fig.savefig(f'{OUT}/fig2_price_path.pdf', bbox_inches='tight', metadata={'CreationDate': None, 'Creator': None, 'Producer': None})
print('Figure 2 written; series in fig2_price_path.csv')
