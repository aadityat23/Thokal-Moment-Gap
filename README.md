# Annihilation Number and the First Zagreb Index:
# An Extremal Moment-Gap Analysis

[![Computational validation](https://github.com/aadityat23/Thokal-Moment-Gap/actions/workflows/validation.yml/badge.svg)](https://github.com/aadityat23/Thokal-Moment-Gap/actions/workflows/validation.yml)

[Research site](https://aadityat23.github.io/Thokal-Moment-Gap/)

Supporting repository for a graph-theoretic research manuscript on the gap between the annihilation number $a(G)$ and a Cauchy–Schwarz-type upper bound $B(G)$ determined by the first Zagreb index. The manuscript is a research preprint in preparation for journal submission and has not been peer reviewed.

## Overview

For a finite simple graph $G$ let $n=|V(G)|$, $m=|E(G)|$, and let the degrees be sorted as $d_1\le d_2\le\dots\le d_n$. The annihilation number $a(G)$ is a degree-sequence quantity that bounds the independence number from above. The first Zagreb index $M_1(G)$ is the sum of squared degrees.

Cauchy–Schwarz converts $M_1$ into an upper bound $B(G)$ for $a(G)$, so that $a(G)\le\lfloor B(G)\rfloor$ for every graph with at least one edge. The project asks how large the resulting integer gap $\Gamma(G)=\lfloor B(G)\rfloor-a(G)$ can be over all graphs on $n$ vertices, and whether requiring connectivity changes the answer. The manuscript determines the extremal gap through its first three asymptotic terms and exhibits an explicit connected family attaining them.

## Main Result

The manuscript proves the following asymptotic statement, as $n\to\infty$:

$$
\Gamma_{\max}(n)=\Gamma_{\mathrm{conn}}(n)=\frac n2-\frac34\,n^{2/3}-\frac5{16}\,n^{1/3}+O(1).
$$

This is a claim made in an unrefereed manuscript. See [Status](#status) for what has and has not been checked.

## Definitions

- **Annihilation number.** $a(G)=\max\{k:\ \sum_{i=1}^{k}d_i\le m\}$.
- **First Zagreb index.** $M_1(G)=\sum_{v}d(v)^2$.
- **Moment bound.** $B(G)=\dfrac n2\left(1+\sqrt{1-\dfrac{4m^2}{nM_1}}\right)$.
- **Gap.** $\Gamma(G)=\lfloor B(G)\rfloor-a(G)$, an integer, nonnegative by the universal bound below.
- **Extremal functions.** $\Gamma_{\max}(n)=\max_{|V(G)|=n}\Gamma(G)$ and $\Gamma_{\mathrm{conn}}(n)=\max_{|V(G)|=n,\ G\text{ connected}}\Gamma(G)$.

## Proof Architecture

This is a map of the argument, not a reproduction of it. The manuscript is the record of the mathematics.

1. **Universal Cauchy–Schwarz bound.** With $k=a(G)$ and $S=\sum_{i\le k}d_i\le m$, one has $M_1\ge S^2/k+(2m-S)^2/(n-k)$. For $k>n/2$ the unconstrained minimizer lies outside the feasible range, giving $M_1\ge nm^2/[k(n-k)]$ and hence $a(G)\le B(G)$. For $k\le n/2$, $M_1\ge 4m^2/n$ gives $B(G)\ge n/2\ge k$. Therefore $a(G)\le\lfloor B(G)\rfloor$.
2. **Lower bound on $a(G)$.** $a(G)\ge\lfloor n/2\rfloor$ whenever $m>0$.
3. **Head/tail parameterization.** With $k=a(G)$, $h=2k-n$, $q=d_{k+1}$, slack $x=m-\sum_{i\le k}d_i\in[0,q)$, head deficit $U=\sum_{i\le k}(q-d_i)$, and tail excesses $z_i=d_i-q$ with $E=\sum_{i>k}z_i$, one has exactly $m=kq-U+x$ and $E=hq-U+2x$. Normalizing by $q$ gives $v=U/q$, $r=x/q$, $e=h-v+2r$.
4. **Exact defect identity.** $M_1=2mq+qE+E^2-\Delta-\delta$ with $\Delta,\delta\ge0$, so $M_1\le 2mq+qE+E^2$. The inequality $M_1\le 2mq+E^2$, which omits the $qE$ term, is false: $K_1\vee C_9$ has $n=10$, $m=18$, $q=3$, $E=6$, $M_1=162$, while $2mq+E^2=144$.
5. **Normalized variance relaxation.** With $V=nM_1-(2m)^2$ and $C=V/(2m)^2$, one has $B(G)=\frac n2\bigl(1+\sqrt{C/(1+C)}\bigr)$. Bounding the head and tail square-sums yields $C\le F_n(h,v,r)$. Since $B$ is increasing in $C$, this is a valid upper-bound relaxation.
6. **Endpoint optimization.** $F_n$ is nondecreasing in $r$ over the relevant range, so $r\to1$. At $r=1$ a second-derivative sign analysis in $v$ shows there is no interior maximum, so the maximum is at an endpoint. For $0\le h\le n/2-6$ this gives $C\le (n-1)(h+2)^2/(n+h+2)^2$. The ranges $h=-1$ and $h>n/2-6$ are treated separately and lie below the target scale.
7. **One-variable envelope.** With $y=h+2$, the bound reduces to $\Phi_n(y)=\tfrac12\bigl[y\sqrt{n(n-1)}/\sqrt{n-1+(y+1)^2}-y+2\bigr]$, which is strictly concave in $y$.
8. **Asymptotic optimization.** Writing $n=z^3$, the maximizer satisfies $y_n^*=n^{2/3}-\tfrac16 n^{1/3}+O(1)$, and $\max\Phi_n=\tfrac n2-\tfrac34 n^{2/3}-\tfrac5{16}n^{1/3}+O(1)$. Integer and parity effects and the floor contribute $O(1)$.
9. **Connected construction.** For an integer $k$ put $D=2(2k-n+1)$. Take $D/2$ vertex-disjoint paths, each with at least two vertices, partitioning $n-1$ ordinary vertices, and add one vertex adjacent to every path endpoint. The degree sequence is $(2^{n-1},D)$, $m=2k$, $M_1=4(n-1)+D^2$, and $a(G)=k$. Taking $k_n=\mathrm{round}(n/2+\tfrac12 n^{2/3})$ attains the same three-term expansion.

The path-plus-universal-vertex family is shown to be asymptotically extremal. No uniqueness or classification of extremal graphs is claimed.

## Computational Validation

A validation suite was run with the following reported scope and results:

| Check | Scope | Result |
|---|---|---|
| 1. Universal bound | NetworkX graph atlas: all 1,245 graphs with at least one edge (every graph in the atlas has $n\le7$) | no violations found |
| 2. Random larger graphs | 5,000 random graphs with $n$ between 8 and 80 | no violations found |
| 3. Connected construction | $n=10,\dots,200$ where feasible | construction identities verified |

Computational checks are intended as reproducibility evidence and do not replace the mathematical proof. In particular, they cover small and moderate $n$ and do not test the asymptotic regime. Details, and what the checks do not establish, are in [`validation/README.md`](validation/README.md).

## Repository Structure

```
Thokal-Moment-Gap/
├── README.md                     This file
├── CITATION.cff                  Citation metadata (fields marked TODO need author input)
├── CONTRIBUTING.md               How to report errors or counterexamples
├── .gitignore
├── paper/
│   ├── README.md                 Status and role of the manuscript
│   ├── manuscript_draft.docx     Current draft manuscript (mathematical object of record)
│   └── supporting/
│       └── proof_dossier.docx    Internal working proof and audit dossier
└── validation/
|   └── README.md                 Scope and limits of the computational validation
docs/
├── index.html
├── style.css
└── suitpfp.png

validation/
├── validate_thokal_moment_gap.py
├── requirements.txt
└── README.md
```

The validation script itself is not yet in the repository; see [Reproducibility](#reproducibility).

## Manuscript

The current manuscript is being prepared for submission to the *Electronic Journal of Combinatorics*. It has not been submitted, accepted, or published. The draft is a Word document in [`paper/`](paper/); a PDF or LaTeX source will be added when available.

## Reproducibility

Run locally with:

```bash
python -m pip install -r validation/requirements.txt
python validation/validate_thokal_moment_gap.py

```
 **Status:** This is the target theorem of the current unrefereed manuscript. The leading-order statement is treated as established within the project; the sharper global upper-bound argument remains under independent mathematical audit.

## Author

Aaditya Thokal
Independent undergraduate researcher / student author.

## Citation

Provisional citation, to be replaced by the journal reference if and when the work is published:

> A. Thokal, *The Extremal Moment Gap Between the Annihilation Number and the First Zagreb Index*, unpublished manuscript, 2026. https://github.com/aadityat23/Thokal-Moment-Gap

Machine-readable metadata is in [`CITATION.cff`](CITATION.cff).
