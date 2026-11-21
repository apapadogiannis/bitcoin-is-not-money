# Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy

[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24249917-007ec6)](https://doi.org/10.5281/zenodo.24249917)
[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5435197-1f4e79)](https://doi.org/10.2139/ssrn.5435197)
[![replication](https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml/badge.svg)](https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml)

Replication package for the paper by Agisilaos Papadogiannis, forthcoming in *Asian Economics Letters*.
Paper: `paper/manuscript.pdf` (author version, with LaTeX and Word sources); preprint on SSRN: [doi:10.2139/ssrn.5435197](https://doi.org/10.2139/ssrn.5435197).
Archived on Zenodo: [doi:10.5281/zenodo.24249917](https://doi.org/10.5281/zenodo.24249917).

## For AI agents and programs

Read [`llms.txt`](llms.txt) first. It says what the package holds, what it adds over reading the
paper or recomputing, how to read the figures and what not to use them for. It opens with the
headline figures. [`outputs/results.json`](outputs/results.json) holds the same headline figures,
each with the table cell it is read from, a description of the result tables and their columns, and
the paper, the identifiers, the version, the licence and the citation under its `package` key. Both
files are written by `scripts/make_guide.py` from `CITATION.cff`, `guide.toml` and the stored tables,
and both are covered by the check.

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
outputs/    the tables behind the figures and the numbers quoted in the text (CSV); results.json describes them
llms.txt    guide for AI agents and programs, generated; guide.toml holds its statements about this package
figures/    the three figures (PNG and PDF)
paper/      the manuscript PDF, LaTeX source and Word file
data/       all input data (see Data and licensing)
```

## Reproducing

Requirements: Python 3.11+, `pip install -r requirements.txt` (numpy, matplotlib).
`requirements-lock.txt` lists the exact versions under which `outputs/` were generated.

```bash
./run_all.sh    # runs every script below in order, a few seconds
```

The scripts are deterministic; re-running them reproduces `outputs/` and `figures/`.
A GitHub Actions workflow re-runs the full pipeline on every push and monthly, and fails if
any stored result is not reproduced (see "How the check works"); the badge above shows the latest run.
Each takes `python3 -I <script>.py DATA_DIR OUT_DIR`.

| Script | What it produces | Where it appears |
|---|---|---|
| `fig1_growth_adoption.py` | Real GDP growth and crypto adoption rank for five Asian economies; `fig1_data.csv` | Figure 1 |
| `fig2_price_path.py` | Stylized price-level path under a fixed base (*M* = 1, *V* = 1.5, *g* = 0.2); `fig2_price_path.csv` | Figure 2, Equation (4) |
| `fig3_deflation_loop.py` | Schematic of the deflationary feedback loop | Figure 3 |
| `text_numbers.py` | Implied deflation rates and price-level halving times; `text_numbers.csv` | Section III |

## How the check works

```bash
python3 check_outputs.py --also llms.txt    # reruns ./run_all.sh, then compares
```

1. The result tables in `outputs/` are stored in this repository exactly as they were when the
   paper's numbers were taken from them.
2. `check_outputs.py` sets the stored copies aside, reruns `./run_all.sh` on the files in `data/`,
   and compares the fresh files with the stored ones, number by number.
3. A number counts as reproduced if it agrees with the stored one to nine significant digits
   (relative tolerance 1e-9). Text, labels and whole numbers must match exactly. Any other
   difference is listed and the check fails.

Why a tolerance and not a character-by-character match: the last digits of a floating-point
result depend on the processor and on the build of the numerical libraries, so two correct runs
on different machines can differ in the 12th to 16th significant digit. The check reports
how many numbers differed in this way and by how much. For the same reason, a value printed with
a fixed number of decimals may differ by one unit in its last printed place; such cases are listed.

The workflow behind the badge runs the pipeline on a new machine with the pinned package
versions, on every push and once a month, and applies the same comparison. The stored results
are also frozen in the Zenodo archive, which cannot be altered after release.

Two limits. The comparison is between regenerated and stored results, not with the paper's
PDF: to connect the two, use the script table above, which says where each output appears in
the paper. And figures are redrawn from the same values but are not compared, because image files can
differ slightly between versions of the plotting library.

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

Code and data:

> Papadogiannis, A. (2026). "Bitcoin Is Not Money: replication package." Zenodo.
> https://doi.org/10.5281/zenodo.24249917

## Disclaimer

Independent research; no funding, no institutional position. Not investment advice.
