# The Extremal Moment Gap Between the Annihilation Number and the First Zagreb Index

[![Computational validation](https://github.com/aadityat23/Thokal-Moment-Gap/actions/workflows/validation.yml/badge.svg)](https://github.com/aadityat23/Thokal-Moment-Gap/actions/workflows/validation.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23007553.svg)](https://doi.org/10.5281/zenodo.23007553)

**Research site:** https://aadityat23.github.io/Thokal-Moment-Gap/

A research preprint by **Aaditya Anand Thokal** on the extremal gap between the annihilation number and the first Zagreb index.

The Version 1.0 manuscript is publicly released and archived on Zenodo under DOI [10.5281/zenodo.23007553](https://doi.org/10.5281/zenodo.23007553). It has not undergone external peer review.

## Overview

For a finite simple graph $G$ let $n=|V(G)|$, $m=|E(G)|$, and let the degrees be sorted as $d_1\le d_2\le\dots\le d_n$. The annihilation number $a(G)$ is a degree-sequence quantity that bounds the independence number from above. The first Zagreb index $M_1(G)$ is the sum of squared degrees.

Cauchy–Schwarz converts $M_1$ into an upper bound $B(G)$ for $a(G)$, so that $a(G)\le\lfloor B(G)\rfloor$ for every graph with at least one edge. The project asks how large the resulting integer gap $\Gamma(G)=\lfloor B(G)\rfloor-a(G)$ can be over all graphs on $n$ vertices, and whether requiring connectivity changes the answer.

## Main Result

The Version 1.0 preprint proves the following asymptotic statement, as $n\to\infty$:

$$
\Gamma_{\max}(n)=\Gamma_{\mathrm{conn}}(n)=\frac n2-\frac34\,n^{2/3}-\frac5{16}\,n^{1/3}+O(1).
$$

The manuscript is unrefereed. Computational checks are reproducibility evidence and do not replace the mathematical proof.

## Definitions

- **Annihilation number.** $a(G)=\max\{k:\ \sum_{i=1}^{k}d_i\le m\}$.
- **First Zagreb index.** $M_1(G)=\sum_{v}d(v)^2$.
- **Moment bound.** $B(G)=\dfrac n2\left(1+\sqrt{1-\dfrac{4m^2}{nM_1}}\right)$.
- **Gap.** $\Gamma(G)=\lfloor B(G)\rfloor-a(G)$.
- **Extremal functions.** $\Gamma_{\max}(n)=\max_{|V(G)|=n}\Gamma(G)$ and $\Gamma_{\mathrm{conn}}(n)=\max_{|V(G)|=n,\ G\text{ connected}}\Gamma(G)$.

## Proof Architecture

The manuscript's argument proceeds through a universal Cauchy–Schwarz bound, an exact head/tail degree-sequence decomposition, a scale-free degree-variance relaxation, endpoint reduction, one-variable asymptotic optimization, and a connected construction using a universal vertex over disjoint paths.

The repository is intended to make the derivations and validation workflow inspectable. The detailed proof remains in the manuscript.

## Computational Validation

The validation suite reports:

| Check | Scope | Result |
|---|---|---|
| Universal bound | NetworkX graph atlas: all 1,245 nonempty graphs with $n\le7$ | no violations found |
| Random larger graphs | 5,000 deterministic random graphs with $n$ between 8 and 80 | no violations found |
| Connected construction | $n=10,\dots,200$ where feasible | construction identities verified |

These checks support reproducibility and sanity checking. They do not establish the asymptotic theorem.

## Repository Structure

```text
Thokal-Moment-Gap/
├── README.md
├── CITATION.cff
├── CONTRIBUTING.md
├── paper/
├── validation/
└── docs/
    ├── index.html
    ├── style.css
    ├── sitemap.xml
    ├── robots.txt
    └── suitpfp.png
```

## Manuscript

**Version 1.0** is publicly released as a research preprint and archived on Zenodo:

**DOI:** https://doi.org/10.5281/zenodo.23007553

The manuscript has not undergone external peer review and is not presented here as a journal publication.

## Reproducibility

Run locally with:

```bash
python -m pip install -r validation/requirements.txt
python validation/validate_thokal_moment_gap.py
```

## Author

**Aaditya Anand Thokal**

Independent undergraduate researcher / student author.

## Citation

> Thokal, A. A. (2026). *The Extremal Moment Gap Between the Annihilation Number and the First Zagreb Index* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23007553

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).
