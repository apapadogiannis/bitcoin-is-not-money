# Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy

[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5435197-1f4e79)](https://doi.org/10.2139/ssrn.5435197)
[![replication](https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml/badge.svg)](https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml)

Replication package for the paper by Agisilaos Papadogiannis, forthcoming in *Asian Economics Letters*.
Paper: `paper/manuscript.pdf` (author version, with LaTeX and Word sources); preprint on SSRN: [doi:10.2139/ssrn.5435197](https://doi.org/10.2139/ssrn.5435197).

## What this is

The paper asks whether a hard-capped monetary base such as Bitcoin's can serve as money in a
growing, credit-based economy, with Asia as the reference case:

1. **A fixed base turns growth into deflation.** From the quantity identity, with a fixed
   money stock and stable velocity, output growth at rate *g* implies deflation at rate *g*.
   For India or Vietnam, growth of 5–7% a year would halve the price level every 10–14 years.
2. **Neither escape route is reliable.** Price stability would need velocity to grow as fast
   as output, and persistent deflation raises real debt burdens. Bitcoin is better treated
   as a store-of-value asset than as a monetary anchor.

This package holds the data behind Figure 1 and the scripts that produce all three figures
and the numbers derived in the text.

## Layout

```
scripts/    one script per figure or calculation (see below)
outputs/    the tables behind the figures and the numbers quoted in the text (CSV)
figures/    the three figures (PNG and PDF)
paper/      the manuscript PDF, LaTeX source and Word file
data/       all input data (see Data and licensing)
```

## Reproducing

Requirements: Python 3.11+, `pip install -r requirements.txt` (numpy, matplotlib).
For byte-identical tables use `requirements-lock.txt` (the exact versions under which
`outputs/` were generated).

```bash
./run_all.sh    # runs every script below in order, a few seconds
```

The scripts are deterministic; re-running them reproduces `outputs/` and `figures/`.
A GitHub Actions workflow re-runs the full pipeline on every push and monthly, and fails if
any result table differs from the committed one; the badge above shows the latest run.
Each takes `python3 -I <script>.py DATA_DIR OUT_DIR`.

| Script | What it produces | Where it appears |
|---|---|---|
| `fig1_growth_adoption.py` | Real GDP growth and crypto adoption rank for five Asian economies; `fig1_data.csv` | Figure 1 |
| `fig2_price_path.py` | Stylized price-level path under a fixed base (*M* = 1, *V* = 1.5, *g* = 0.2); `fig2_price_path.csv` | Figure 2, Equation (4) |
| `fig3_deflation_loop.py` | Schematic of the deflationary feedback loop | Figure 3 |
| `text_numbers.py` | Implied deflation rates and price-level halving times; `text_numbers.csv` | Section III |

## Data and licensing

- Real GDP growth, 2024 and projections for 2025–2026: `imf_growth.csv`, from
  International Monetary Fund, *Regional Economic Outlook: Asia and Pacific, October 2025*,
  [Annex Table 1.1](https://www.imf.org/en/publications/reo/apac/issues/2025/10/24/regional-economic-outlook-for-asia-and-pacific-october-2025).
  India is on a fiscal-year basis.
- Crypto adoption rank: `chainalysis_rank.csv`, overall rank among 151 countries in the
  [Chainalysis 2025 Global Crypto Adoption Index](https://www.chainalysis.com/blog/2025-global-crypto-adoption-index/).
- Both files hold a handful of published figures, transcribed by hand with the source
  cited; data accessed November 2026.
- Code: MIT License. Output tables and figures (`outputs/`, `figures/`): CC BY 4.0, cite the paper.
- Paper (`paper/`): CC BY-SA 4.0, the license of *Asian Economics Letters*.

## Citation

> Papadogiannis, A. (forthcoming). "Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy." *Asian Economics Letters*.
> SSRN: https://doi.org/10.2139/ssrn.5435197

## Disclaimer

Independent research; no funding, no institutional position. Not investment advice.
