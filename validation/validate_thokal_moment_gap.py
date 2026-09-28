#!/usr/bin/env python3
"""Reproducibility checks for the Thokal Moment-Gap project.

Checks:
1. Universal Cauchy–Schwarz/Zagreb bound on the NetworkX graph atlas.
2. The same bound on deterministic random graphs.
3. Identities of the connected path-plus-universal-vertex construction.

These finite checks do not prove the asymptotic theorem.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass
import networkx as nx

EPS = 1e-10
SEED = 20260928


def annihilation_number(G: nx.Graph) -> int:
    degrees = sorted(dict(G.degree()).values())
    m = G.number_of_edges()
    total = 0
    k = 0
    for degree in degrees:
        if total + degree <= m:
            total += degree
            k += 1
        else:
            break
    return k


def first_zagreb_index(G: nx.Graph) -> int:
    return sum(d * d for _, d in G.degree())


def moment_bound(G: nx.Graph) -> float:
    n = G.number_of_nodes()
    m = G.number_of_edges()
    m1 = first_zagreb_index(G)
    if m == 0:
        raise ValueError("B(G) is undefined by the stated formula when m=0.")
    radicand = 1.0 - (4.0 * m * m) / (n * m1)
    if radicand < -EPS:
        raise AssertionError(f"Negative Cauchy–Schwarz radicand: {radicand}")
    return 0.5 * n * (1.0 + math.sqrt(max(0.0, radicand)))


def check_universal_bound(G: nx.Graph) -> None:
    if G.number_of_edges() == 0:
        return
    a = annihilation_number(G)
    B = moment_bound(G)
    if a > B + EPS:
        raise AssertionError(
            f"Universal bound failed: n={G.number_of_nodes()}, "
            f"m={G.number_of_edges()}, a={a}, B={B}"
        )
    if a > math.floor(B + EPS):
        raise AssertionError("Floor form of the universal bound failed.")


def build_connected_construction(n: int):
    k = round(n / 2 + 0.5 * n ** (2 / 3))
    D = 2 * (2 * k - n + 1)
    if D < 2 or D % 2:
        return None
    paths = D // 2
    if n - 1 < 2 * paths or D > n - 1:
        return None

    G = nx.Graph()
    G.add_node(0)
    sizes = [2] * paths
    sizes[0] += (n - 1) - 2 * paths

    next_vertex = 1
    for size in sizes:
        vertices = list(range(next_vertex, next_vertex + size))
        next_vertex += size
        G.add_edges_from(zip(vertices, vertices[1:]))
        G.add_edge(0, vertices[0])
        G.add_edge(0, vertices[-1])
    return G, k, D


@dataclass
class ConstructionResult:
    checked: int = 0
    infeasible: int = 0


def check_connected_construction(n_min=10, n_max=200):
    result = ConstructionResult()
    for n in range(n_min, n_max + 1):
        built = build_connected_construction(n)
        if built is None:
            result.infeasible += 1
            continue

        G, k, D = built
        result.checked += 1

        assert G.number_of_nodes() == n
        assert nx.is_connected(G)

        expected = sorted([2] * (n - 1) + [D])
        actual = sorted(dict(G.degree()).values())
        assert actual == expected, (n, actual, expected)

        assert G.number_of_edges() == 2 * k
        assert first_zagreb_index(G) == 4 * (n - 1) + D * D
        assert annihilation_number(G) == k

    return result


def check_graph_atlas() -> int:
    checked = 0
    for G in nx.graph_atlas_g():
        if G.number_of_edges() == 0:
            continue
        check_universal_bound(G)
        checked += 1
    return checked


def check_random_graphs(trials=5000, seed=SEED) -> int:
    rng = random.Random(seed)
    for _ in range(trials):
        n = rng.randint(8, 80)
        p = rng.uniform(0.05, 0.95)
        G = nx.gnp_random_graph(n, p, seed=rng.randrange(2**32))
        if G.number_of_edges():
            check_universal_bound(G)
    return trials


def main() -> int:
    print("=== Thokal Moment-Gap validation suite ===")
    atlas = check_graph_atlas()
    print(f"[1] Graph atlas: checked {atlas} nonempty graphs (n <= 7).")
    print("    PASS: no violations found.")

    trials = check_random_graphs()
    print(f"[2] Random larger-graph tests: {trials} deterministic trials.")
    print(f"    PASS: no violations found. Seed = {SEED}.")

    construction = check_connected_construction()
    print(
        f"[3] Connected construction: n = 10..200; "
        f"checked {construction.checked} feasible cases, "
        f"{construction.infeasible} infeasible cases."
    )
    print("    PASS: construction identities verified.")
    print("OVERALL: all computational checks passed.")
    print("These checks are reproducibility evidence, not a proof of the theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
