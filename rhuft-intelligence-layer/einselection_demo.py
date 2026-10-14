"""
Einselection — the resonance that survives the noise
=====================================================

The founder's core claim, made precise and testable:

    "Stable self-measurement = the resonance that persists through the
     incommensurable white noise of the field."

The rigorous mechanism is EINSELECTION (environment-induced superselection,
Zurek 2003). A system coupled to a noisy environment is continuously "measured"
by it. The only states that survive are the POINTER STATES — the eigenstates of
the system observable that couples to the environment. Superpositions (pure
"possibility") decay; the stable resonances (pointer states) persist.

This is the honest, established form of "self-measurement selects stable
resonance". It is also the closest existing physics gets to "true geometric
intelligence": the eigen-structure that noise cannot destroy.

Note on terminology (honest): "incommensurable time" is QUASIPERIODIC
(deterministic, dense line spectrum) — not true white noise (continuous flat
spectrum). The environment's real noise is the thermal/vacuum fluctuation,
which is genuinely stochastic. This demo uses the real, stochastic dephasing.
"""

from __future__ import annotations

import numpy as np
from scipy import linalg as sla


# ---------------------------------------------------------------------------
# 1. Einselection on a qubit (the clean, exact case)
# ---------------------------------------------------------------------------
def lindblad_dephasing(rho0: np.ndarray, gamma: float, t_max: float,
                       n_steps: int = 400) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Integrate d rho/dt = gamma (X rho X - rho),  X = sigma_z (pointer observable).

    Off-diagonals decay as ~ e^{-2 gamma t}; diagonal populations are conserved.
    """
    X = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)   # the pointer observable
    rho = np.asarray(rho0, dtype=float).copy()
    dt = t_max / n_steps
    times = np.linspace(0.0, t_max, n_steps + 1)
    coh = [abs(rho[0, 1])]
    pop = [rho[0, 0]]
    for _ in range(n_steps):
        rho = rho + gamma * (X @ rho @ X - rho) * dt
        coh.append(abs(rho[0, 1]))
        pop.append(rho[0, 0])
    return times, np.array(coh), np.array(pop)


# ---------------------------------------------------------------------------
# 2. Geometric resonance survives noise: ring eigenmodes under white noise
# ---------------------------------------------------------------------------
def ring_eigenmode_noise_robustness(n: int = 64, sigma: float = 0.5,
                                    seed: int = 0) -> np.ndarray:
    """Project a noisy signal on a ring onto its Fourier eigenmodes.

    Returns per-mode retained power. Smooth (low-frequency) standing waves
    survive white noise; high-frequency modes drown in it. This is the
    geometric form of einselection: the Laplacian's low modes are the
    'pointer states' of a noisy geometry.
    """
    rng = np.random.default_rng(seed)
    # A smooth signal (low-frequency standing wave) plus white noise.
    k = np.arange(n)
    signal = np.sin(2 * np.pi * k / n)          # the "resonance"
    noisy = signal + sigma * rng.standard_normal(n)
    F = np.fft.fft(noisy) / n                    # Fourier = ring eigenmodes
    power = np.abs(F) ** 2
    # symmetry: mode m and n-m carry the same physical frequency
    retained = power[:n // 2 + 1]
    return retained


def main() -> None:
    print("=" * 66)
    print("EINSELECTION: which states survive the noise?")
    print("=" * 66)

    # --- qubit: superposition decays, pointer states persist ----------------
    rho0 = 0.5 * np.ones((2, 2))                 # |+> = (|0>+|1>)/sqrt(2)
    times, coh, pop = lindblad_dephasing(rho0, gamma=1.0, t_max=4.0)
    print(f"\n  qubit in superposition |+>:")
    print(f"    coherence |rho_01|: {coh[0]:.3f}  ->  {coh[-1]:.4f}   (decays)")
    print(f"    population rho_00:  {pop[0]:.3f}  ->  {pop[-1]:.3f}   (conserved)")
    print("    -> the superposition (possibility) dies; |0>,|1> (resonances) persist.")

    # --- ring: low eigenmodes survive noise ---------------------------------
    retained = ring_eigenmode_noise_robustness(n=64)
    print(f"\n  ring geometry, 32 modes under white noise:")
    print(f"    low-mode (smooth) power:  {retained[1]:.4f}  (survives)")
    print(f"    high-mode (fine) power:   {retained[32]:.5f}  (drowned)")
    print("    -> smooth standing waves are the geometric 'pointer states'.")

    print("\n" + "=" * 66)
    print("MEANING")
    print("=" * 66)
    print("  Persistence under noise = the selection principle. This is the")
    print("  precise, testable core of 'self-measurement selects stable resonance'.")
    print("  It is not sentience; it is the eigen-structure that noise leaves standing.")


if __name__ == "__main__":
    main()
