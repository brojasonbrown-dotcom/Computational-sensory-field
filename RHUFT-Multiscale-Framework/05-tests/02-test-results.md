# Pass 7 — Test Results & Rejection Table

Computed 2026-10-11. Method: reproducible Python (`01-numeric-tests.py`, saved beside this
file) + independent Wolfram Alpha cross-check (founder-provided AppID).
No number is asserted without a computation behind it.

## Rejection table

| # | Gate / hypothesis | Test | Result | Verdict |
|---|---|---|---|---|
| 1 | Uniform φ-spacing of stable scales (sₙ = s₀·φⁿ across scale index) | log10-ratio statistics over 14 physical anchors | mean 4.688, std 3.873, prediction log10(φ) = 0.209; only **1 of 13** ratios within ±0.5 | **REJECTED** |
| 2 | Golden angle = 1/α (fine-structure) | exact numeric comparison | 137.507764° vs 137.035999° → 0.344 % (~3443 ppm) off | **REJECTED** |
| 3 | Hierarchy anchors (e-folds, Planck ticks) | Wolfram vs Python | 140.314 vs 140.31; 8.072e60 vs 8.070e60 | **CONFIRMED** (match) |
| 4 | Predict ≥1 mass ratio / coupling from eigenproblem | — | not yet performed | **OPEN** |
| 5 | "c emergent" preserves Lorentz invariance | — | must match current null LIV bounds | **OPEN** |
| 6 | "measurement modulates vacuum" reproduces Casimir 1/d⁴ | — | not yet performed | **OPEN** |

## Test 1 detail — the φ-scaling is decisively wrong

The 13 adjacent log10-ratios of the real scale ladder are:

`3.09, 13.61, 3.09, 0.48, 4.25, 1.28, 2.00, 2.00, 5.00, 7.00, 2.00, 12.00, 5.15`

- Mean = 4.69, population std = 3.87, range 0.48 → 13.61.
- The framework's `sₙ = s₀·φⁿ` predicts a constant 0.209 per step.
- **1 of 13** steps is even within ±0.5 of that.

Interpretation: the physical hierarchy is **not** a self-similar φ-lattice. It has a huge
"desert" (GUT → electroweak, 13.6 decades) and much tighter clustering elsewhere. If φ-scaling
is meant to describe *modes within* a single scale rather than scale-to-scale spacing, that
reading is currently undefined and unfalsifiable until the modes are specified — it cannot be
the scale law as written.

## Test 2 detail — the golden angle is not α⁻¹

- Golden angle θ_G = 2π/φ² = 137.507764°.
- α⁻¹ (CODATA 2018) = 137.035999084.
- Mismatch = 0.4718°, i.e. **0.34 %** — enormous relative to the ~10⁻⁹ precision at which α is
  measured. The "137" coincidence is numerology; it is not a physical law.

Consequence for the framework: the golden/silver ratio-locking potentials (V_ratio, V_θ) in
notebook 02 are **not supported** and should be removed from the dynamics. They carry no
predictive weight and are now numerically contradicted on their flagship target (α).

## Test 3 detail — anchors verified

| Quantity | Python | Wolfram |
|---|---|---|
| e-folds Planck → Hubble | 140.31 | 140.314 |
| Planck ticks in universe age | 8.070e60 | 8.072e60 |
| E_Planck / Λ_QCD (0.25 GeV) | 4.884e19 | (manual, 4–6e19 range) |

These are the real hierarchy numbers any "measurement density" theory must reproduce.

## What survives and what was killed

**Survives (anchored, `[A]`/`[E]`):** relational ontology; emergent time; spacetime from
entanglement; system-specific stability (SSB mass gap); gapped scale hierarchy; structured
vacuum. These are the six kept postulates of framework v0.2.

**Killed by data:** golden-ratio scale spacing (Test 1) and golden-angle = α⁻¹ (Test 2).
Both are now numerically contradicted, not merely "unproven."

**Open (the real frontier):** deriving a coupling/mass ratio; Lorentz-invariance consistency;
Casimir reproduction. These are the only three gates left, and they are genuine, hard physics
— not numerology.

## Next action

The correct next step is to **drop the golden-ratio machinery entirely** and attack Gate 4
(predict a number) with the constrained v0.2 dynamics: treat the closure order parameter κ as
a Higgs-like field, compute the spectrum of the coupled ρ–χ–κ–Φ system, and look for any
dimensionless ratio that emerges *from the eigenproblem structure* (not from φ). That is a
real calculation with an honest pass/fail, and it is the only path to a genuine prediction.
