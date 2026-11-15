"""Numbers quoted in the text that follow from Equations (3) and (4).
With a fixed base and stable velocity the price level falls at rate g, so it halves every ln(2)/g years.
The paper quotes "roughly half every 10-14 years" for g of 5-7 percent.
Usage: python3 -I text_numbers.py DATA_DIR OUT_DIR"""
import sys, csv, math

OUT = sys.argv[2]
with open(f'{OUT}/text_numbers.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['growth_rate_percent', 'implied_deflation_percent', 'price_level_halving_time_years'])
    for g in (5.0, 5.6, 6.0, 6.2, 6.5, 6.6, 7.0):
        w.writerow([f'{g:.1f}', f'{-g:.1f}', f'{math.log(2) / (g / 100):.1f}'])
print('text_numbers.csv written')
