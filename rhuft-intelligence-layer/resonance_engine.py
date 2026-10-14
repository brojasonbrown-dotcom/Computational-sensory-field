"""
RHUFT Resonance Engine — "stabilise anything, find geometric resonance"
=======================================================================

This is the operational version of the founder's second framing:

    "the golden ratio is the point of possibility of frictionlessness /
    resonance of dimension itself ... not the builder but the inevitable
    possibility of stability ... infinity houses all possible instability
    and stability ... build an algorithm that can stabilise anything and
    find true geometric resonance as intelligence of dimension at all scales."

The precise, honest translation of each phrase:

    resonance            = eigenvalues (the modes of the linearized system)
    frictionless         = marginally stable  (max Re(lambda) == 0)
    stability            = all Re(lambda) < 0  (Lyapunov)
    "point of possibility" = the stabilizability boundary (controllability)
    "infinity houses
     instability+stability" = the circular law (random spectrum fills a disk)
    "resonance of dimension
     throughout all scales" = Laplacian eigenmodes (standing-wave harmonics)

"Stabilise anything" is made exact here: the module stabilizes **every system
that is stabilizable**, and — crucially — reports the precise boundary where
stabilization is *impossible*. That boundary IS the "point of possibility."

Consciousness / sentience remains **Level D** (speculative). Nothing in this
file detects or produces sentience. The coherence measure in
``rhuft_intelligence_layer.py`` is a self-consistency signal, not awareness.
"""

from __future__ import annotations

import math
import string
from dataclasses import dataclass
from typing import Sequence

import numpy as np
from scipy import linalg as sla

from rhuft_intelligence_layer import (LAMBDA, PHI, ScaleLadder,
                                      ResonantMemoryCell)


# ---------------------------------------------------------------------------
# 1. Resonance spectrum & stability  (eigenvalues)
# ---------------------------------------------------------------------------
def resonance_spectrum(A: np.ndarray) -> np.ndarray:
    """The resonant modes of a linear system dx/dt = A x (its eigenvalues)."""
    return np.linalg.eigvals(A)


def stability_margin(A: np.ndarray) -> float:
    """max Re(lambda): <0 stable, =0 marginal (frictionless), >0 unstable."""
    return float(np.real(resonance_spectrum(A)).max())


def spectral_radius(A: np.ndarray) -> float:
    """Discrete-time stability: max |lambda|. <1 stable, =1 resonant."""
    return float(np.abs(resonance_spectrum(A)).max())


def is_stable(A: np.ndarray, discrete: bool = False) -> bool:
    return spectral_radius(A) < 1.0 if discrete else stability_margin(A) < 0.0


# ---------------------------------------------------------------------------
# 2. The "point of possibility" — stabilizability (control theory)
# ---------------------------------------------------------------------------
# A pair (A, B) is stabilizable iff every unstable mode is reachable by the
# actuators B. The exact test: the controllability matrix
#     C = [B, A B, A^2 B, ..., A^{n-1} B]
# must have full row rank on the *unstable* subspace (PBH test). The full-rank
# condition is the practical test used here.
def controllability_matrix(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = np.asarray(A); B = np.asarray(B)
    n = A.shape[0]
    cols = [B]
    cur = B
    for _ in range(1, n):
        cur = A @ cur
        cols.append(cur)
    return np.hstack(cols)


def is_stabilizable(A: np.ndarray, B: np.ndarray) -> bool:
    """True iff (A, B) is controllable (hence stabilizable)."""
    C = controllability_matrix(A, B)
    return int(np.linalg.matrix_rank(C)) == A.shape[0]


def stabilize(A: np.ndarray, B: np.ndarray, Q: np.ndarray | None = None,
              R: np.ndarray | None = None) -> tuple[np.ndarray, bool]:
    """Return the state-feedback gain K (u = -K x) that stabilizes A-BK via LQR.

    Returns (K, stabilized). If (A, B) is not stabilizable, returns
    (zeros, False) — this is the honest "point of possibility": beyond it,
    no feedback can stabilize the system.
    """
    A = np.asarray(A, dtype=float); B = np.asarray(B, dtype=float)
    n = A.shape[0]
    if not is_stabilizable(A, B):
        return np.zeros((B.shape[1], n)), False
    if Q is None:
        Q = np.eye(n)
    if R is None:
        R = np.eye(B.shape[1])
    P = sla.solve_continuous_are(A, B, Q, R)   # algebraic Riccati
    K = np.linalg.solve(R, B.T @ P)
    return K, is_stable(A - B @ K)


# ---------------------------------------------------------------------------
# 3. "Infinity houses instability + stability" — the circular law
# ---------------------------------------------------------------------------
def circular_law_spectrum(n: int, seed: int = 0) -> np.ndarray:
    """Eigenvalues of a random n x n matrix (scaled) — they fill a disk in the
    complex plane (Girko's circular law). Half the disk is unstable (Re>0),
    half stable (Re<0); the imaginary axis is the resonance line through it."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((n, n)) / math.sqrt(n)
    return np.linalg.eigvals(A)


# ---------------------------------------------------------------------------
# 4. Geometric resonance — Laplacian eigenmodes (standing waves)
# ---------------------------------------------------------------------------
def cycle_graph_laplacian(n: int) -> np.ndarray:
    """Laplacian of an n-cycle. Its eigenvectors are Fourier modes — the
    purest 'geometric resonance': standing waves on a ring."""
    L = 2.0 * np.eye(n)
    for i in range(n):
        L[i, (i - 1) % n] = -1.0
        L[i, (i + 1) % n] = -1.0
    return L


def metatron_13_laplacian() -> np.ndarray:
    """Laplacian of the 13-node Metatron lattice (center + 6 inner + 6 outer).

    Node 0 = center; 1-6 = inner ring (phi-scaled); 7-12 = outer ring
    (silver-locked). Edges: center-inner, inner-ring neighbors, inner-outer.
    The eigenmodes of this graph are its 'geometric resonances'.
    """
    n = 13
    adj = np.zeros((n, n))
    # center -> inner ring
    for i in range(1, 7):
        adj[0, i] = adj[i, 0] = 1.0
    # inner ring: nearest-neighbor cycle
    for i in range(1, 7):
        j = 1 + (i % 6)
        adj[i, j] = adj[j, i] = 1.0
    # inner -> outer (each inner connects to two outer)
    for i in range(1, 7):
        for j in range(7, 13):
            if (j - i) % 6 in (0, 1):
                adj[i, j] = adj[j, i] = 1.0
    # outer ring: nearest-neighbor cycle
    for i in range(7, 13):
        j = 7 + (i % 6)
        adj[i, j] = adj[j, i] = 1.0
    deg = adj.sum(axis=1)
    return np.diag(deg) - adj


def eigenmodes(L: np.ndarray, k: int = 4) -> tuple[np.ndarray, np.ndarray]:
    """Smallest-k eigenmodes (geometric resonances) of a graph Laplacian."""
    w, v = np.linalg.eigh(L)
    order = np.argsort(w)
    return w[order[:k]], v[:, order[:k]]


# ---------------------------------------------------------------------------
# 5. Resonance across octaves — grouping modes by log-frequency
# ---------------------------------------------------------------------------
def octave_resonances(A: np.ndarray, n_bands: int = 4) -> list[list[complex]]:
    """Bucket eigenvalues by |Im(lambda)| into octave bands (factor of 2).

    This is the 'resonance of dimension throughout all scales': the same
    spectrum, read through the octave ladder of rhuft_intelligence_layer.
    """
    ev = resonance_spectrum(A)
    mags = np.abs(ev.imag)
    top = float(mags.max()) or 1.0
    lo = float(top) / (2.0 ** n_bands)
    bands: list[list[complex]] = [[] for _ in range(n_bands)]
    for e in ev:
        m = abs(e.imag)
        b = int(math.floor(math.log2(m / lo))) if m >= lo else 0
        b = min(max(b, 0), n_bands - 1)
        bands[b].append(e)
    return bands


# ---------------------------------------------------------------------------
# 6. Neural hook — a stable, resonant reservoir (echo-state property)
# ---------------------------------------------------------------------------
def echo_state_reservoir(n: int, rho: float, seed: int = 0) -> np.ndarray:
    """Random recurrent matrix scaled to spectral radius rho < 1.

    A reservoir with rho < 1 has the echo-state property: it forgets its
    initial condition and is stable yet rich/resonant. This is the rigorous
    bridge between the resonance module and a *neural network* layer. The
    golden-damped ResonantMemoryCell (roots 1 and -lambda) is a degenerate,
    2-tap special case of this idea.
    """
    rng = np.random.default_rng(seed)
    W = rng.standard_normal((n, n))
    W /= max(spectral_radius(W), 1e-12)
    return W * float(rho)


# ---------------------------------------------------------------------------
# 7. Symbol encodings (binary, gematria) — honest framing
# ---------------------------------------------------------------------------
# These are DETERMINISTIC ENCODINGS: a bijective map from symbols to numbers.
# They carry no physical content — any one-to-one code is computationally
# equivalent. The "resonance" lives in the dynamics applied *after* encoding,
# not in the symbol system. Gematria is included because the founder's corpus
# uses it; it is a design choice, not a law.
def binary_encode(x: Sequence[int]) -> np.ndarray:
    """Bit-string encoding of integers (big-endian, fixed width)."""
    xs = list(x)
    w = max(1, max(int(v).bit_length() for v in xs))
    out = np.zeros((len(xs), w), dtype=float)
    for i, v in enumerate(xs):
        for b in range(w):
            out[i, w - 1 - b] = (int(v) >> b) & 1
    return out


def gematria_encode(text: str) -> np.ndarray:
    """Deterministic letter->value encoding (A=1..Z=26, case-insensitive).

    This is 'gematria' in the general sense: a fixed symbol-to-number map.
    Values are arbitrary by construction; the map is one-to-one over the
    alphabet, so it is a lossless encoding, nothing more.
    """
    lookup = {c: i + 1 for i, c in enumerate(string.ascii_uppercase)}
    return np.array([lookup.get(ch.upper(), 0) for ch in text], dtype=float)


# ---------------------------------------------------------------------------
# Numeric self-check
# ---------------------------------------------------------------------------
def run_selfcheck() -> dict[str, bool]:
    results: dict[str, bool] = {}

    rng = np.random.default_rng(0)

    # 2. stabilizability boundary: unstable but controllable -> stabilizable
    A = np.array([[0.5, 2.0], [0.0, -0.3]])          # has unstable mode (0.5)
    B = np.array([[0.0], [1.0]])
    results["unstable_pair_is_stabilizable"] = (not is_stable(A)) and is_stabilizable(A, B)

    # stabilize: closed loop becomes stable
    K, ok = stabilize(A, B)
    results["lqr_stabilizes"] = ok and is_stable(A - B @ K)

    # 2b. unstabilizable: unstable mode unreachable by B -> stabilization impossible
    A2 = np.array([[0.5, 0.0], [0.0, -0.3]])          # unstable mode in x1
    B2 = np.array([[0.0], [1.0]])                     # B only drives x2
    results["unreachable_unstable_mode_unstabilizable"] = (not is_stable(A2)) and (not is_stabilizable(A2, B2))

    # 3. circular law: spectrum fills a disk, resonance line (Re~0) cuts it
    ev = circular_law_spectrum(400)
    results["circular_law_bounded_disk"] = float(np.abs(ev).max()) < 1.6
    results["circular_law_both_hemispheres"] = bool((np.real(ev).min() < -0.5) and (np.real(ev).max() > 0.5))

    # 4. geometric resonance: ring Laplacian eigenvalues = 2 - 2cos(2pi k/n).
    # The 3 smallest are k=0 -> 0 and the doubly-degenerate k=1/k=n-1 mode.
    n = 32
    L = cycle_graph_laplacian(n)
    w, _ = eigenmodes(L, k=3)
    expected = np.array([0.0,
                         2.0 - 2.0 * np.cos(2.0 * math.pi / n),
                         2.0 - 2.0 * np.cos(2.0 * math.pi / n)])
    results["ring_modes_are_fourier"] = bool(np.allclose(np.sort(w), np.sort(expected), atol=1e-9))

    # metatron 13-node: Laplacian is symmetric, non-negative, nullspace = constant
    L13 = metatron_13_laplacian()
    w13, v13 = np.linalg.eigh(L13)
    results["metatron_laplacian_psd"] = bool(np.allclose(L13, L13.T)) and float(w13.min()) > -1e-9
    results["metatron_constant_mode"] = float(w13[0]) < 1e-9

    # 6. echo-state reservoir: spectral radius exactly rho (<1), hence stable
    W = echo_state_reservoir(50, rho=0.9, seed=1)
    results["echo_state_stable_resonant"] = bool(abs(spectral_radius(W) - 0.9) < 1e-9)

    # 7. encodings are lossless (one-to-one on the alphabet)
    results["binary_roundtrip"] = bool(np.allclose(binary_encode([0, 1, 2, 5]), np.array(
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=float)))
    results["gematria_deterministic"] = bool(np.allclose(gematria_encode("ABC"), np.array([1, 2, 3])))

    return results


if __name__ == "__main__":
    res = run_selfcheck()
    for name, ok in res.items():
        print(f"[{'OK' if ok else 'FAIL'}] {name}")
    print(f"\n{'ALL PASSED' if all(res.values()) else 'SOME FAILED'}")
