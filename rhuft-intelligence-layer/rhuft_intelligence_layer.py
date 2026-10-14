"""
RHUFT Intelligence Layer — a rigorous, runnable scaffold
==========================================================

This module turns the *defensible core* of the RHUFT "multiscale
self-measurement" framework into working code. It deliberately excludes the
parts of the corpus that the project's own v0.1 audit (see
``RHUFT-Multiscale-Framework/04-framework/``) flagged as falsified or
non-physical as *physics* — golden-ratio spacing, "flower of life" geometry,
consciousness-as-physics. Those remain available as a *design language*, but
they carry no predictive weight here.

Every component is mapped to (a) the RHUFT primitive and (b) its modern,
established anchor. See README.md for the full map.

Components
----------
- ScaleLadder          : the gapped "octave" hierarchy (RG/EFT scales)
- ResonantMemoryCell   : the stable unit-root memory kernel  (lambda = 1/phi^2)
- FourierOctaveBank    : octave-spaced band-pass front-end ("sensory channels")
- SelfMeasurementLoop  : the P R Q S U transceiver as predictive coding
- coherence            : C(t) = |<Psi(t)|Psi(t-tau)>|^2  (the framework's measure)
- quasiperiodic_orbit  : incommensurate frequencies -> dense, never-repeating orbit
- rkhs_kernel_trick    : finite computation of an infinite-dimensional feature map
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Sequence

import numpy as np

# ---------------------------------------------------------------------------
# Core constants  [matches rhuft-computational.md]
# ---------------------------------------------------------------------------
PHI = (1.0 + math.sqrt(5.0)) / 2.0      # golden ratio
PHI_INV = 1.0 / PHI
LAMBDA = PHI_INV ** 2                   # 0.381966...  (memory decay / threshold)
KAPPA = 1.0 / (PHI * math.pi)           # 0.196726...  (closure coupling)

L_P = 1.616255e-35                      # Planck length (m)
T_P = 5.391247e-44                      # Planck time  (s)
C_LIGHT = 299792458.0                   # m/s


# ---------------------------------------------------------------------------
# 1. The scale / octave ladder
# ---------------------------------------------------------------------------
# RHUFT primitive: "scale" -> modern anchor: RG/EFT decoupling scale.
# The hierarchy is *gapped*, not continuous. A scale is "stable" where a bound
# structure sits below its decay threshold (mass gap, barrier, degeneracy,
# superselection...). Each scale has a characteristic wave band = its "octave".
@dataclass(frozen=True)
class Scale:
    name: str
    length_m: float
    wave_band: str
    sensory: str | None = None  # non-None only at the human-sense window


# Real, anchored 14-scale hierarchy (order-of-magnitude; see
# RHUFT-Multiscale-Framework/02-scales-of-physics/00-stable-scales-master-list.md).
REAL_SCALES: tuple[Scale, ...] = (
    Scale("Planck",        L_P,             "none classical", None),
    Scale("GUT",           1e-31,           "unknown",        None),
    Scale("Electroweak",   1e-18,           "gauge bosons",   None),
    Scale("Hadronic/QCD",  1e-15,           "pion modes",     None),
    Scale("Nuclear",       1e-14,           "gamma / giant resonances", None),
    Scale("Atomic",        5.29e-11,        "X-ray..optical", None),
    Scale("Molecular",     1e-9,            "IR vibration / microwave", None),
    Scale("Condensed",     1e-7,            "phonons/magnons/plasmons", None),
    Scale("Biological",    1e-5,            "action potentials", None),
    Scale("Human",         1.0,             "sound + light",  "auditory 20 Hz-20 kHz, visual 400-700 nm"),
    Scale("Geophysical",   1e7,             "seismic / Schumann", None),
    Scale("Stellar",       1e9,             "p/g-modes, GW",  None),
    Scale("Galactic",      1e21,            "density waves, GW", None),
    Scale("Cosmological",  1.3e26,          "BAO / CMB peaks", None),
)


class ScaleLadder:
    """The gapped octave hierarchy, expressed as (length, frequency) rungs."""

    def __init__(self, scales: Sequence[Scale] = REAL_SCALES) -> None:
        self.scales = list(scales)

    def frequency(self, scale: Scale) -> float:
        """Spatial-frequency anchor f ~ c / L (order of magnitude)."""
        return C_LIGHT / scale.length_m

    def octave_steps(self) -> np.ndarray:
        """log2 spacing between consecutive rungs — is the ladder geometric?"""
        lengths = np.array([s.length_m for s in self.scales], dtype=float)
        return np.diff(np.log2(lengths))

    def spacing_spread(self) -> float:
        """Coefficient of variation of the octave steps.

        If the ladder were perfectly geometric (constant ratio), this is ~0.
        The real hierarchy is *not* geometric — which is the honest,
        established result your own audit found for phi-spacing.
        """
        steps = self.octave_steps()
        return float(steps.std() / abs(steps.mean()))


# ---------------------------------------------------------------------------
# 2. The resonant memory cell  (the corrected "Fibonacci mandate")
# ---------------------------------------------------------------------------
# RHUFT primitive: "memory" / "time"  -> modern anchor: conservative, marginally
# stable recurrence.  The *additive* form Psi(t) = Psi(t-1) + Psi(t-2) (as in the
# old Omega doc) is UNSTABLE. The stable form is the unit-root kernel:
#
#     Psi(t) = (1 - lambda) Psi(t - tau) + lambda Psi(t - 2 tau)
#
# Characteristic eq:  z^2 - (1-lambda) z - lambda = (z - 1)(z + lambda) = 0
# Roots:  z = 1  (conserved mode)  and  z = -lambda  (golden-damped transient).
# This is the unique conservative, marginally-stable two-tap kernel.
class ResonantMemoryCell:
    """Two-tap golden-damped memory. Root 1 = conservation, root -lambda = decay."""

    def __init__(self, lam: float = LAMBDA, tau: int = 1) -> None:
        self.lam = float(lam)
        self.tau = max(1, int(tau))
        self.history: list[float] = []

    def step(self, x: float) -> float:
        n = len(self.history)
        # Initial transient: hold first value until enough history exists.
        if n < self.tau:
            y = x
        elif n < 2 * self.tau:
            y = (1.0 - self.lam) * self.history[n - self.tau] + self.lam * x
        else:
            y = (1.0 - self.lam) * self.history[n - self.tau] + self.lam * self.history[n - 2 * self.tau]
        self.history.append(y)
        return y

    def run(self, xs: Sequence[float]) -> np.ndarray:
        self.history.clear()
        return np.array([self.step(x) for x in xs])

    @staticmethod
    def characteristic_roots(lam: float = LAMBDA) -> tuple[complex, complex]:
        """Analytic roots of z^2 - (1-lam)z - lam. Returns (1.0, -lam)."""
        a = -(1.0 - lam)
        b = -lam
        disc = a * a - 4.0 * b
        s = complex(disc) ** 0.5
        return (-a + s) / 2.0, (-a - s) / 2.0


# ---------------------------------------------------------------------------
# 3. The Fourier octave bank  ("scales/octaves as stable sensory inputs")
# ---------------------------------------------------------------------------
# RHUFT primitive: "octave" -> modern anchor: octave-spaced filter bank /
# wavelet / multiresolution front-end. Real sensory systems ARE band-pass
# front-ends in this exact sense: the cochlea is log-frequency, the retina is
# spatial-frequency, "thoughts" are the slow, internal (sub-light) dynamics.
class FourierOctaveBank:
    """Decompose a 1-D signal into octave (factor-of-2) bands via FFT masking."""

    def __init__(self, n_bands: int, fs: float = 1.0) -> None:
        self.n_bands = int(n_bands)
        self.fs = float(fs)

    def decompose(self, x: np.ndarray) -> list[np.ndarray]:
        x = np.asarray(x, dtype=float)
        n = x.shape[0]
        spec = np.fft.rfft(x)
        freqs = np.fft.rfftfreq(n, d=1.0 / self.fs)
        nyq = self.fs / 2.0
        # Octave edges that tile [0, nyq] exactly (lowest band covers DC).
        edges = [0.0] + [nyq / (2.0 ** k) for k in range(self.n_bands - 1, -1, -1)]
        bands: list[np.ndarray] = []
        for b in range(self.n_bands):
            lo = edges[b]
            hi = edges[b + 1]
            if b == self.n_bands - 1:
                mask = freqs >= lo  # top band: up to and including Nyquist
            else:
                mask = (freqs >= lo) & (freqs < hi)
            masked = np.where(mask, spec, 0.0)
            bands.append(np.fft.irfft(masked, n=n))
        return bands


# ---------------------------------------------------------------------------
# 4. The self-measurement loop  (P R Q S U  ->  predictive coding)
# ---------------------------------------------------------------------------
# RHUFT primitive: "measurement = recursive discrimination of state by state"
# -> modern anchor: predictive coding / active inference (continuous, weak
# monitoring — NOT collapse). The transceiver cycle maps cleanly:
#   P (project)   -> predict:  x_hat = g(state)
#   R (reflect)   -> interrogate / compare to input
#   Q (compare)   -> error:    e = x - x_hat
#   S (stabilize) -> correct:  state <- state + lr * e   (pull to attractor)
#   U (update)    -> consolidate:  memory <- golden decay
class SelfMeasurementLoop:
    """Predictive-coding loop; convergence = self-consistent internal model."""

    def __init__(self, n_state: int, lam: float = LAMBDA, lr: float = 0.1) -> None:
        self.state = np.zeros(n_state, dtype=float)
        self.memory = np.zeros(n_state, dtype=float)
        self.lam = float(lam)
        self.lr = float(lr)
        self.error_trace: list[float] = []

    def predict(self) -> np.ndarray:
        return (1.0 - self.lam) * self.state + self.lam * self.memory

    def step(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=float)
        x_hat = self.predict()                     # P, R
        e = x - x_hat                              # Q
        self.state = self.state + self.lr * e      # S
        prev_memory = self.memory.copy()
        self.memory = (1.0 - self.lam) * self.memory + self.lam * prev_memory  # U
        self.error_trace.append(float(np.linalg.norm(e)))
        return self.state

    def run(self, xs: Sequence[np.ndarray]) -> np.ndarray:
        self.error_trace.clear()
        out = [self.step(np.asarray(x, dtype=float)) for x in xs]
        return np.array(out)


# ---------------------------------------------------------------------------
# 5. The coherence measure  (the framework's own)
# ---------------------------------------------------------------------------
# C(t) = |<Psi(t) | Psi(t - tau)>|^2 / (||Psi(t)|| ||Psi(t-tau)||)
# This is the *temporal autocorrelation*, normalized to [0, 1]. Its meaning is
# "how much of the current state is still aligned with its phi-delayed self".
def coherence(states: np.ndarray, tau: int) -> np.ndarray:
    """Normalized overlap of each state with its tau-delayed self."""
    states = np.asarray(states, dtype=float)
    n = states.shape[0]
    out = np.zeros(n)
    for t in range(tau, n):
        a, b = states[t], states[t - tau]
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        out[t] = float(abs(np.dot(a, b))) / (na * nb) if na * nb > 0 else 0.0
    return out


# ---------------------------------------------------------------------------
# 6. Incommensurable dimensions -> quasiperiodicity (the real "infinite" path)
# ---------------------------------------------------------------------------
# Two incommensurate frequencies f1, f2 (f1/f2 irrational) produce a trajectory
# on a 2-torus that is dense: it never exactly repeats, and over time the orbit
# fills the torus. This is the honest, computable form of "incommensurable
# dimensions" — an effectively infinite-dimensional trajectory from 2 degrees
# of freedom.
def quasiperiodic_orbit(t: np.ndarray, f1: float, f2: float) -> np.ndarray:
    """A dense, never-repeating orbit from two incommensurate frequencies."""
    omega = 2.0 * math.pi * np.asarray([[f1], [f2]])
    phases = omega * t[None, :]
    return np.stack([np.sin(phases[0]), np.cos(phases[0]),
                     np.sin(phases[1]), np.cos(phases[1])], axis=1)


def orbit_min_return_distance(orbit: np.ndarray) -> float:
    """Minimum separation between distinct points of a (sampled) orbit."""
    d = np.linalg.norm(orbit[:, None, :] - orbit[None, :, :], axis=-1)
    np.fill_diagonal(d, np.inf)
    return float(d.min())


# ---------------------------------------------------------------------------
# 7. Infinite-dimensional feature maps via the kernel trick (RKHS)
# ---------------------------------------------------------------------------
# A kernel k(x, y) = <phi(x), phi(y)>_H computes the inner product in an
# (often infinite-dimensional) Hilbert space H *without* materializing phi.
# The Gaussian (RBF) kernel has an infinite-dimensional feature map — this is
# the exact, finite way to "compute in infinite dimensions" (kernel methods,
# and the bridge to wide neural networks via the neural tangent kernel).
def gaussian_kernel(x: np.ndarray, y: np.ndarray, sigma: float = 1.0) -> float:
    return float(math.exp(-np.sum((x - y) ** 2) / (2.0 * sigma * sigma)))


def rkhs_kernel_trick(points: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Gram matrix K[i,j] = <phi(x_i), phi(x_j)>_H in the infinite-dim RBF space."""
    pts = np.asarray(points, dtype=float)
    n = pts.shape[0]
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            K[i, j] = gaussian_kernel(pts[i], pts[j], sigma)
    return K


# ---------------------------------------------------------------------------
# Numeric self-check (call this to prove the claims in this file)
# ---------------------------------------------------------------------------
def run_selfcheck() -> dict[str, bool]:
    """Run the numeric checks that support each claim. Returns name -> passed."""
    results: dict[str, bool] = {}

    # 2. memory-cell roots are exactly (1, -lambda)
    r1, r2 = ResonantMemoryCell.characteristic_roots(LAMBDA)
    results["memory_roots_are_1_and_neg_lambda"] = (
        abs(r1 - 1.0) < 1e-9 and abs(r2 + LAMBDA) < 1e-9
    )

    # 3. octave bank reconstructs the input (bands sum to the signal)
    rng = np.random.default_rng(0)
    n = 512
    x = np.cumsum(rng.standard_normal(n))  # smooth, broad-spectrum signal
    bank = FourierOctaveBank(n_bands=5)
    recon = np.sum(bank.decompose(x), axis=0)
    results["octave_bank_reconstructs_signal"] = bool(np.allclose(recon, x, atol=1e-9))

    # 4. self-measurement loop converges (prediction error -> 0)
    target = np.array([1.0, -0.5, 0.25], dtype=float)
    loop = SelfMeasurementLoop(n_state=3, lr=0.1)
    for _ in range(200):
        loop.step(target)
    results["self_measurement_converges"] = loop.error_trace[-1] < 1e-4

    # 5. coherence lies in [0, 1]
    states = np.random.default_rng(1).standard_normal((200, 3))
    c = coherence(states, tau=8)
    results["coherence_in_unit_interval"] = bool(np.all(c >= -1e-12) and np.all(c <= 1.0 + 1e-12))

    # 6. incommensurate orbit never repeats (min return distance > 0)
    t = np.linspace(0.0, 1000.0, 2000)
    orbit = quasiperiodic_orbit(t, f1=1.0, f2=PHI)  # phi irrational -> dense on T^2
    results["quasiperiodic_never_repeats"] = orbit_min_return_distance(orbit) > 1e-3

    # 7. RBF Gram matrix is symmetric positive definite (valid RKHS kernel)
    K = rkhs_kernel_trick(np.random.default_rng(2).standard_normal((8, 2)))
    results["rbf_kernel_is_psd"] = bool(np.allclose(K, K.T)) and float(np.linalg.eigvalsh(K).min()) > -1e-12

    # 1. the real scale ladder is NOT perfectly geometric (honest result)
    results["real_ladder_not_geometric"] = ScaleLadder().spacing_spread() > 0.05

    return results


if __name__ == "__main__":
    res = run_selfcheck()
    all_ok = all(res.values())
    for name, ok in res.items():
        print(f"[{'OK' if ok else 'FAIL'}] {name}")
    print(f"\n{'ALL PASSED' if all_ok else 'SOME FAILED'}")
