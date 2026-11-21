#!/usr/bin/env bash
# Reproduces every figure and every number derived in the paper. Runs in a few seconds.
set -e
cd "$(dirname "$0")/scripts"
mkdir -p ../outputs ../figures
for f in text_numbers fig1_growth_adoption fig2_price_path fig3_deflation_loop; do
  echo "== $f"; python3 -I "$f.py" ../data ../outputs
done
mv -f ../outputs/*.pdf ../outputs/*.png ../figures/
# The description of the result tables with the headline figures (outputs/results.json) and the guide
# for programs and AI agents (llms.txt).
echo "== make_guide"; python3 -I make_guide.py
