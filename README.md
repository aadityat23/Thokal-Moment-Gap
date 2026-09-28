Thokal-Moment-Gap

Extremal moment-gap analysis for the annihilation number and the first Zagreb index




Research repository for an extremal graph-theory problem coupling the annihilation number with the first Zagreb index.

This repository contains the manuscript, mathematical development, computational validation, and supporting material for an independent research project by Aaditya Thokal.

The central question is:

How large can the gap become between the annihilation number of a graph and the upper envelope imposed on it by the first Zagreb index?

The project develops a moment-based envelope for the annihilation number, reduces the corresponding extremal problem to a scale-free optimization, derives an asymptotic expansion, and gives a connected graph construction matching that expansion.

Research status

Current stage: manuscript / preprint preparation and external mathematical validation.

The main asymptotic statement below is the result developed in the current manuscript. The repository is intended to make the argument transparent and reproducible while it is being prepared for journal submission.

The project does not claim a classification or uniqueness theorem for extremal graphs. The explicit connected family is used as an asymptotically matching construction.

Core definitions

Let $G$ be a finite simple undirected graph with

$$
n=|V(G)|,\qquad m=|E(G)|.
$$

Let the degree sequence be sorted as

$$
d_1\le d_2\le\cdots\le d_n.
$$

Annihilation number

$$
a(G)=\max\left{k\in{0,\ldots,n}:\sum_{i=1}^{k}d_i\le m\right}.
$$

First Zagreb index

$$
M_1(G)=\sum_{v\in V(G)}d(v)^2.
$$

Moment envelope

$$
B(G)=\frac n2\left(1+\sqrt{1-\frac{4m^2}{nM_1(G)}}\right).
$$

The associated moment gap is

$$
\boxed{\Gamma(G)=\lfloor B(G)\rfloor-a(G).}
$$

The extremal functions studied are

$$
\Gamma_{\max}(n)=\max_{|V(G)|=n}\Gamma(G),
$$

and

$$
\Gamma_{\mathrm{conn}}(n)=\max_{\substack{|V(G)|=n\G\text{ connected}}}\Gamma(G).
$$

Main asymptotic result

The manuscript establishes the following asymptotic statement:

$$
\boxed{
\Gamma_{\max}(n)=\Gamma_{\mathrm{conn}}(n)=\frac n2-\frac34n^{2/3}-\frac5{16}n^{1/3}+O(1),\qquad n\to\infty.
}
$$

Thus the unrestricted and connected extremal problems have the same asymptotic expansion through the $n^{1/3}$ term.

The proof has two main components:

an upper-bound reduction from arbitrary graphs to a one-variable analytic envelope; and

an explicit connected construction whose moment gap attains the same asymptotic scale and coefficients.

Why the Zagreb index enters

The handshake lemma gives

$$
\sum_{i=1}^n d_i=2m.
$$

The first Zagreb index is the second moment of the degree sequence:

$$
M_1=\sum_i d_i^2.
$$

Applying Cauchy–Schwarz to the degree sequence split at the annihilation threshold produces a quantitative restriction on how large $a(G)$ can be relative to $M_1$.

For $k=a(G)$, writing

$$
S=\sum_{i=1}^{k}d_i\le m,
$$

one obtains

$$
M_1\ge\frac{S^2}{k}+\frac{(2m-S)^2}{n-k}.
$$

Optimizing this bound over the feasible range of $S$ yields

$$
\boxed{a(G)\le\lfloor B(G)\rfloor.}
$$

Consequently $\Gamma(G)$ is always a nonnegative integer.

Scale-free reduction

Let

$$
k=a(G),\qquad h=2k-n,$$

and let

$$
q=d_{k+1}.
$$

Define the head deficit

$$
x=m-\sum_{i=1}^{k}d_i,\qquad 0\le x<q,
$$

and

$$
U=\sum_{i=1}^{k}(q-d_i).
$$

For the upper-degree tail, write

$$
d_i=q+z_i,\qquad i>k,
$$

and define

$$
E=\sum_{i>k}z_i.
$$

The exact bookkeeping gives

$$
m=kq-U+x,
$$

and

$$
E=hq-U+2x.
$$

After normalizing by $q$,

$$
v=\frac Uq,\qquad r=\frac xq,\qquad e=\frac Eq=h-v+2r.
$$

The feasibility conditions become

$$
0\le r<1,\qquad 0\le v\le h+2r.
$$

Moreover,

$$
2m=q(n+h-2v+2r).
$$

This removes the raw scale of the degrees and reduces the relevant extremal information to dimensionless variables.

Exact moment identity

Define

$$
\Delta=E^2-\sum_{i>k}z_i^2=2\sum_{i<j}z_i z_j\ge0,
$$

and

$$
\delta=qU-\sum_{i\le k}(q-d_i)^2=\sum_{i\le k}d_i(q-d_i)\ge0.
$$

Then the degree-square sum satisfies the exact identity

$$
\boxed{M_1=2mq+qE+E^2-\Delta-\delta.}
$$

In particular,

$$
M_1\le2mq+qE+E^2.
$$

This identity separates the exact degree information from the nonnegative defect terms discarded in the extremal relaxation.

Variance normalization

Introduce the degree-variance quantity

$$
V=nM_1-(2m)^2,
$$

and the normalized variance

$$
C=\frac{V}{(2m)^2}.
$$

Then

$$
\frac{4m^2}{nM_1}=\frac1{1+C},
$$

so

$$
\boxed{B(G)=\frac n2\left(1+\sqrt{\frac C{1+C}}\right).}
$$

The head/tail parameterization yields the relaxation

$$
\boxed{
C\le F_n(h,v,r)=\frac{n(v+e^2)-(e-v)^2}{(n+h-2v+2r)^2},\qquad e=h-v+2r.
}
$$

Because $B(G)$ is increasing in $C$, this gives a valid upper-bound route for the extremal gap.

Reduction to one variable

The normalized relaxation can be optimized analytically.

For the $r$-variable,

$$
\frac{\partial F_n}{\partial r}=\frac{4n(h+2r-v)(n-v-1)}{(n+h+2r-2v)^3}.
$$

In the relevant feasible range this is nonnegative, allowing the upper-bound relaxation to take $r$ to its limiting value $1$.

The remaining $v$-optimization is controlled by the sign structure of the derivative. In the relevant range, any interior stationary point is a local minimum, so the maximum occurs at an endpoint.

The resulting envelope is

$$
\boxed{\Phi_n(h)=\frac12\left[\frac{(h+2)\sqrt{n(n-1)}}{\sqrt{n-1+(h+3)^2}}-h\right].}
$$

Writing $y=h+2$,

$$
\Phi_n(y)=\frac12\left[\frac{y\sqrt{n(n-1)}}{\sqrt{n-1+(y+1)^2}}-y+2\right].
$$

Its second derivative is strictly negative:

$$
\Phi_n''(y)=-\frac{\sqrt{n(n-1)}(3ny+2n+2y^2+y)}{2[n-1+(y+1)^2]^{5/2}}<0.
$$

Hence the continuous envelope has a unique maximizer.

Origin of the $n^{2/3}$ and $n^{1/3}$ scales

Let

$$
n=z^3.
$$

The continuous maximizer occurs at the scale

$$
y_n^*=z^2-\frac16z+O(1),
$$

or equivalently

$$
\boxed{y_n^*=n^{2/3}-\frac16n^{1/3}+O(1).}
$$

Expanding the envelope at this scale gives

$$
\boxed{\max_y\Phi_n(y)=\frac n2-\frac34n^{2/3}-\frac5{16}n^{1/3}+O(1).}
$$

The coefficient $-5/16$ is part of the explicit asymptotic expansion of the one-variable envelope rather than being inferred from numerical fitting.

Matching connected construction

For an integer $k$, define

$$
D=2(2k-n+1).
$$

Take $D/2$ vertex-disjoint paths partitioning the $n-1$ ordinary vertices, with every path containing at least two vertices, and add one universal vertex adjacent to the endpoints of every path.

The resulting graph is connected and has degree sequence

$$
\boxed{(2^{,n-1},D).}
$$

Its basic parameters are

$$
m=n-1+\frac D2=2k,
$$

and

$$
M_1=4(n-1)+D^2.
$$

For the construction,

$$
a(G)=k.
$$

Choosing

$$
k_n=\operatorname{round}\left(\frac n2+\frac12n^{2/3}\right)
$$

gives

$$
D=2n^{2/3}+O(1),
$$

and the resulting moment envelope satisfies

$$
B(G)=n-\frac14n^{2/3}-\frac5{16}n^{1/3}+O(1).
$$

Therefore

$$
\boxed{\Gamma(G)=\frac n2-\frac34n^{2/3}-\frac5{16}n^{1/3}+O(1).}
$$

This matches the upper bound.

Important: this construction demonstrates asymptotic sharpness under connectivity. It is not claimed to be the unique extremal graph family.

Computational validation

The repository includes computational checks supporting the mathematical development.

1. Graph atlas

All available nonempty graphs in NetworkX's graph atlas with $n\le7$ are tested against the principal inequalities.

Current run:

1,245 nonempty graphs

no violations found

2. Random larger graphs

Random graphs with $8\le n\le80$ are tested against the normalized relaxation and extremal envelope.

Current run:

5,000 random trials

no violations found

3. Connected construction

The explicit construction is checked for a range of graph orders, including $10\le n\le200$ where computationally feasible.

Current run:

construction identities verified

degree sequence, edge count, Zagreb index, annihilation number, and asymptotic-gap calculations checked

A representative validation run reports:

=== Thokal Moment-Gap validation suite ===
[1] Graph atlas: checked 1245 nonempty graphs (n <= 7).
    PASS: no violations found.
[2] Random larger-graph tests: 5000 trials.
    PASS: no violations found.
[3] Connected construction: n = 10..200 where feasible.
    PASS: construction identities verified.
OVERALL: all computational checks passed.

Reminder: this is evidence, not a mathematical proof.

The computational experiments are supporting evidence only. They do not replace the mathematical proof.

Repository structure

Thokal-Moment-Gap/
│
├── index.html
├── README.md
│
├── paper/
│   └── paper.pdf
│
├── validation/
│   ├── validate_thokal_moment_gap.py
│   └── professor_audit_memo.txt
│
├── structural_checker.py
│
└── LICENSE

The exact structure may evolve as the project moves from manuscript preparation to public preprint and journal submission.

Key files

File

Purpose

README.md

Research overview and technical documentation

paper/paper.pdf

Current manuscript

validation/validate_thokal_moment_gap.py

Reproducibility and validation suite

validation/professor_audit_memo.txt

Technical audit brief for external mathematical review

structural_checker.py

Additional graph-structure checking utilities

index.html

Public research landing page / GitHub Pages site

Reproducibility

The computational validation is written in Python.

Install the required dependency:

pip install networkx

Run:

python validation/validate_thokal_moment_gap.py

The checker is designed to verify the computational consequences of the stated formulas and to make it straightforward to test additional graphs.

For mathematical claims, the source of truth remains the manuscript and its proofs; the validation code is not intended to certify the theorem automatically.

What this project establishes — and what it does not

Established in the current manuscript

A universal Cauchy–Schwarz-based envelope for the annihilation number.

An exact degree-sequence normalization around the annihilation threshold.

A variance-based scale-free relaxation.

Reduction to an explicit strictly concave one-variable envelope.

The asymptotic upper-bound expansion through the $n^{1/3}$ term.

An explicit connected construction matching the expansion.

Not claimed

Uniqueness of extremal graphs.

A complete classification of all asymptotically extremal degree sequences.

A classification of all graphs attaining the maximum for finite $n$.

That computational experiments constitute a proof.

Absolute priority over every related result in the literature.

The manuscript deliberately phrases novelty statements relative to the literature reviewed by the author rather than making an absolute priority claim.

Research questions and next directions

Several structural questions remain open within the project:

Extremal structure: Which graph families, beyond the explicit construction, are asymptotically extremal?

Stability: Does near-extremality force the degree sequence to resemble the construction?

Finite-order behavior: What is the exact value of $\Gamma_{\max}(n)$ for finite $n$?

Connected extremizers: Can one characterize finite-$n$ connected extremizers?

Higher moments: What happens if $M_1$ is replaced or supplemented by higher degree moments?

Other degree-based invariants: Are analogous moment envelopes possible for related graph invariants?

Manuscript and peer review

The manuscript is being prepared for submission to the Electronic Journal of Combinatorics.

The public repository is intended to provide:

a transparent research record,

reproducible computational checks,

access to the current manuscript,

and a convenient technical reference for researchers who wish to inspect or audit the argument.

Journal peer review and external mathematical feedback remain distinct from the computational checks in this repository.

Citation

A formal DOI will be added here when a public preprint record is deposited.

Suggested citation format for the current research version:

Thokal, Aaditya. Annihilation Number and the First Zagreb Index: An Extremal Moment-Gap Analysis. Research manuscript, 2026.

If a Zenodo preprint is subsequently deposited, cite the version-specific Zenodo record and DOI provided there.

Author

Aaditya Thokal
Undergraduate researcher in Data Engineering / Data Science
Mumbai, India

Research interests represented in this project include:

extremal graph theory

graph invariants

degree sequences

combinatorics

asymptotic analysis

mathematical validation and reproducibility

A note on verification

This repository is intentionally designed so that a reader can inspect the mathematical argument rather than relying on a black-box claim.

The main chain of the argument is exposed explicitly:

$$
a(G)\longrightarrow B(G)\longrightarrow\Gamma(G)\longrightarrow C\longrightarrow F_n(h,v,r)\longrightarrow\Phi_n(h)\longrightarrow\frac n2-\frac34n^{2/3}-\frac5{16}n^{1/3}+O(1).
$$

The computational layer then provides independent checks over finite graph families and the explicit connected construction.

Mathematical proof, computational evidence, and external peer review are treated as separate forms of validation.

<p align="center">
  <strong>Thokal-Moment-Gap</strong><br>
  Extremal graph theory • Degree moments • Combinatorial analysis
</p>
