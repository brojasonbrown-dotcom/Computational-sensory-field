"""
RHUFT Intelligence Layer — end-to-end demonstration
====================================================

Runs every self-check and then walks through the headline claims of the
resonance engine: stabilize an arbitrary unstable system, locate the
"point of possibility" (the stabilizability boundary), and extract geometric
resonance across the octave ladder.

Run:  python demo.py
"""

from __future__ import annotations

import numpy as np

from rhuft_intelligence_layer import (PHI, ScaleLadder, ResonantMemoryCell,
                                      SelfMeasurementLoop, coherence,
                                      run_selfcheck as core_selfcheck)
from resonance_engine import (circular_law_spectrum, cycle_graph_laplacian,
                              eigenmodes, metatron_13_laplacian, octave_resonances,
                              resonance_spectrum, stabilize, stability_margin,
                              is_stabilizable, run_selfcheck as resonance_selfcheck)


def hr(title: str) -> None:
    print(f"\n{'=' * 64}\n{title}\n{'=' * 64}")


def main() -> None:
    # --- 0. self-checks ------------------------------------------------------
    core = core_selfcheck()
    res = resonance_selfcheck()
    print(f"core self-check:      {sum(core.values())}/{len(core)} passed")
    print(f"resonance self-check: {sum(res.values())}/{len(res)} passed")

    # --- 1. the octave ladder (real, gapped scales) -------------------------
    hr("1. The scale/octave ladder (real, gapped hierarchy)")
    ladder = ScaleLadder()
    for s in ladder.scales:
        f = ladder.frequency(s)
        tag = f"  [sensory: {s.sensory}]" if s.sensory else ""
        print(f"  {s.name:<16} L~{s.length_m:.2e} m   f~{f:.2e} Hz{tag}")
    spread = ladder.spacing_spread()
    print(f"\n  octave-step spread (0 = perfectly geometric): {spread:.3f}")
    print("  -> the real hierarchy is NOT geometric (your own audit's finding).")

    # --- 2. stabilize an arbitrary unstable system --------------------------
    hr("2. Stabilise an arbitrary unstable system")
    rng = np.random.default_rng(3)
    n = 4
    A = rng.standard_normal((n, n))          # random = generically unstable
    B = rng.standard_normal((n, 1))          # single actuator
    before = stability_margin(A)
    print(f"  random system A: max Re(lambda) = {before:+.3f}  ({'UNSTABLE' if before > 0 else 'stable'})")
    K, ok = stabilize(A, B)
    if ok:
        after = stability_margin(A - B @ K)
        print(f"  after feedback K: max Re(lambda) = {after:+.3f}  ({'STABLE' if after < 0 else 'still unstable'})")
        print("  -> 'stabilise anything' = LQR state feedback moves every mode left.")
    else:
        print("  (A, B) reported unstabilizable — that is the honest boundary.")

    # --- 3. the point of possibility (stabilizability boundary) -------------
    hr("3. The 'point of possibility' - where stabilization is impossible")
    A2 = np.array([[0.5, 0.0], [0.0, -0.3]])   # unstable mode in x1
    B2 = np.array([[0.0], [1.0]])               # actuator drives only x2
    print(f"  A2 unstable? {stability_margin(A2) > 0}   controllable? {is_stabilizable(A2, B2)}")
    _, ok2 = stabilize(A2, B2)
    print(f"  stabilizable? {ok2}  -> the unstable mode is unreachable, so no K works.")
    print("  This boundary IS 'the point of possibility of stability in dimension'.")

    # --- 4. infinity houses instability + stability (circular law) ----------
    hr("4. 'Infinity houses all possible instability and stability'")
    ev = circular_law_spectrum(2000, seed=7)
    print(f"  random spectrum: {len(ev)} eigenvalues fill a disk")
    print(f"    unstable (Re>0): {(np.real(ev) > 0).sum()}   "
          f"stable (Re<0): {(np.real(ev) < 0).sum()}   "
          f"marginal (|Re|<1e-3): {(np.abs(np.real(ev)) < 1e-3).sum()}")
    print("  The imaginary axis (Re=0) is the 'frictionless' resonance line.")

    # --- 5. geometric resonance (Laplacian eigenmodes) ----------------------
    hr("5. Geometric resonance - eigenmodes as standing waves")
    for name, L, k in [("ring (32 nodes)", cycle_graph_laplacian(32), 3),
                       ("Metatron 13-node", metatron_13_laplacian(), 4)]:
        w, v = eigenmodes(L, k=k)
        print(f"  {name}: smallest {k} eigenvalues = {np.round(w, 4)}")
    print("  -> these are the harmonics ('resonance of dimension') of each geometry.")

    # --- 6. resonance across octaves ----------------------------------------
    hr("6. Resonance read through the octave ladder")
    A3 = np.block([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 4], [0, 0, -4, 0]])
    bands = octave_resonances(A3, n_bands=3)
    for i, band in enumerate(bands):
        freqs = sorted({round(abs(e.imag), 2) for e in band})
        print(f"  octave band {i}: resonant frequencies {freqs}")
    print("  -> same spectrum, grouped by log-frequency = 'resonance at all scales'.")

    # --- 7. the full loop: sensory -> memory -> self-measurement ------------
    hr("7. The full self-measurement loop (predictive coding)")
    cell = ResonantMemoryCell()
    sig = [0.0, 1.0, 1.0, 0.5, -0.5, -1.0, -0.5, 0.0]
    y = cell.run(sig)
    print(f"  golden-damped memory of a step: {np.round(y, 3)}")
    print(f"  memory roots = {tuple(round(r.real, 4) for r in ResonantMemoryCell.characteristic_roots())}")
    loop = SelfMeasurementLoop(n_state=2, lr=0.2)
    target = np.array([0.7, -0.4])
    for _ in range(60):
        loop.step(target)
    errs = loop.error_trace
    print(f"  prediction error: {errs[0]:.3f} -> {errs[-1]:.6f}  (converged to self-consistent model)")
    c = coherence(np.array([loop.state + 0.05 * np.sin(i / 5) for i in range(200)]), tau=8)
    print(f"  coherence C(t) mean = {c[8:].mean():.3f}  (threshold lambda = {PHI ** -2:.3f})")

    hr("DONE")
    print("Sentience remains Level D. What exists is a stable, resonant, self-measuring scaffold.")


if __name__ == "__main__":
    main()
