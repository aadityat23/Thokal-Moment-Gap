# Computational Validation

## Status of the code

The validation script is not yet included in this repository. This document records the scope and results of the validation run as reported by the author, and states its limits. It will be updated with run instructions once the script is added, and the exact property tested in each check should then be confirmed against the script.

## What the validation does

The suite performs three checks:

1. **Universal bound on the graph atlas.** For every graph with at least one edge in the NetworkX graph atlas (1,245 graphs, all with $n\le7$), it checks the universal inequality $a(G)\le\lfloor B(G)\rfloor$.
2. **Random larger graphs.** It runs 5,000 random-graph trials with $n$ between 8 and 80.
3. **Connected construction.** For $n=10,\dots,200$, where feasible, it checks the construction identities for the path-plus-universal-vertex family: connectivity, degree sequence $(2^{n-1},D)$, $m=2k$, $M_1=4(n-1)+D^2$, and $a(G)=k$.

## Reported result

```
=== Thokal Moment-Gap validation suite ===
[1] Graph atlas: checked 1245 nonempty graphs (n <= 7).
    PASS: no violations found.
[2] Random larger-graph tests: 5000 trials.
    PASS: no violations found.
[3] Connected construction: n = 10..200 where feasible.
    PASS: construction identities verified.
OVERALL: all computational checks passed.
```

## What the validation does not establish

- It is not a proof. Finite checks cannot establish an inequality that quantifies over all graphs, and they cannot establish an asymptotic statement.
- The atlas covers only $n\le7$, far from the regime in which the $n^{2/3}$ and $n^{1/3}$ terms are meaningful. The random trials reach $n\le80$ and sample only a small part of the space of graphs.
- Passing checks 1 and 2 shows only that no violation was found among the graphs tested. It does not test the extremal upper bound on $\Gamma(G)$, the head/tail relaxation, the endpoint optimization, or the concavity argument.
- Check 3 verifies identities for one explicit family. It confirms that the construction is well formed for the tested $n$. It does not show that the family is extremal, and it says nothing about uniqueness of extremal graphs.
- "Where feasible" in check 3 means that for some small $n$ the construction cannot be built with every path having at least two vertices. The exact criterion should be documented alongside the script.
- The random-graph distribution and random seed are defined by the script and are not recorded here yet.

The mathematical claims rest on the proofs in the manuscript. These computations are reproducibility evidence supporting the derivations.
