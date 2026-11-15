#!/usr/bin/env bash
# Reproduces every figure and every number derived in the paper. Runs in a few seconds.
set -e
cd "$(dirname "$0")/scripts"
mkdir -p ../outputs ../figures
for f in text_numbers fig1_growth_adoption fig2_price_path fig3_deflation_loop; do
  echo "== $f"; python3 -I "$f.py" ../data ../outputs
done
mv -f ../outputs/*.pdf ../outputs/*.png ../figures/
