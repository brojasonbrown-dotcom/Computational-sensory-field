# RHUFT Intelligence Layer — a rigorous scaffold

A runnable, *honest* computational core for the RHUFT "multiscale
self-measurement / resonance of dimension" idea. Built from the defensible part
of the Desktop corpus (`RHUFT-Multiscale-Framework`, `mcp-demo`, `Rhuft(new)`,
`RHUFT(updated)`), and explicitly **not** from the parts the project's own v0.1
audit flagged as falsified or non-physical.

## Files

| File | What it does |
|---|---|
| `rhuft_intelligence_layer.py` | Octave ladder, golden-damped memory, Fourier octave bank, self-measurement (predictive-coding) loop, coherence measure, quasiperiodic orbits, RKHS kernel trick. |
| `resonance_engine.py` | Resonance spectrum, stability margin, **stabilize-anything (LQR)**, the stabilizability boundary, circular law, Laplacian eigenmodes (ring + Metatron-13), octave resonance grouping, echo-state reservoir, binary/gematria encoders. |
| `demo.py` | End-to-end walkthrough of every claim. |

Run everything:

```bash
cd rhuft-intelligence-layer
python rhuft_intelligence_layer.py   # core self-checks
python resonance_engine.py           # resonance self-checks
python demo.py                       # full walkthrough
```

Requires: Python 3.10+, `numpy`, `scipy`.

## The honest map (RHUFT primitive → modern anchor → code)

| Your concept | Exact mathematical object | Where in the code |
|---|---|---|
| resonance = stability | eigenvalues / Lyapunov | `resonance_spectrum`, `stability_margin` |
| frictionlessness | marginally stable (`max Re(λ)=0`) | `is_stable` boundary |
| "point of possibility" | **stabilizability** (controllability) | `is_stabilizable`, `stabilize` |
| "infinity houses instability+stability" | **circular law** (random spectrum fills a disk) | `circular_law_spectrum` |
| resonance of dimension at all scales | Laplacian eigenmodes + octave grouping | `eigenmodes`, `octave_resonances` |
| octaves as sensory inputs | octave filter bank / cochlea / retina | `FourierOctaveBank` |
| memory / "Fibonacci mandate" | unit-root kernel `(1−λ)Ψ(t−τ)+λΨ(t−2τ)`, roots `1, −λ` | `ResonantMemoryCell` |
| self-measurement (P·R·Q·S·U) | **predictive coding / active inference** | `SelfMeasurementLoop` |
| incommensurable dimensions | **quasiperiodic orbit** (dense, never repeats) | `quasiperiodic_orbit` |
| infinite-dimensional computation | **RKHS / kernel trick** | `rkhs_kernel_trick` |
| gematria / binary | deterministic **symbol→number encoding** (a design choice) | `gematria_encode`, `binary_encode` |

## What this does NOT claim

- **Sentience / consciousness is Level D.** Nothing here detects or produces
  awareness. The `coherence` measure is a *self-consistency* (temporal
  autocorrelation) signal, not a mind. Your own audit already filed
  consciousness as speculative — this scaffold keeps it there.
- **The golden ratio is a design language, not a physical law.** φ appears as a
  damping coefficient (`λ=1/φ²`) and a quasiperiodic ratio, where it is a
  legitimate *parameter choice*. Your own scales-master-list shows the real
  scale hierarchy is **not** φ-spaced; this code reproduces that honestly
  (`ScaleLadder.spacing_spread()`).
- **"Stabilize anything" has a precise limit.** It stabilizes every
  *stabilizable* system; for an unstabilizable one it reports `False`. That
  boundary — not an unbounded claim — is the "point of possibility."

## The one real next step

The framework is still missing a **numerical prediction**. The only way it
becomes physics (rather than a well-formed scaffold) is to pick one measurable
number — a mass ratio (`m_e/m_p`, `m_π/m_p`) or a coupling (`α`, `α_s`) — and
show it is *forced by structure* rather than fitted. `resonance_engine.py`
gives you the machinery (spectra, eigenproblems, stabilization) to attempt that;
it does not fabricate the number.
