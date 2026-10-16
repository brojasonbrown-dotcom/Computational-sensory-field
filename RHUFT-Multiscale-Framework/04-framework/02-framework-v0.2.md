# Framework v0.2 — constrained equations, units, anchors

Status: **v0.2** · 2026-10-11 · supersedes the placeholder dynamics of v0.1.

**Honesty statement.** v0.2 specifies the *minimal field-theory form* that the RHUFT
primitives force, and shows it reduces to known physics (Ginzburg–Landau / Abelian–Higgs /
Klein–Gordon). It does **not** derive the Standard Model, and it predicts **no new coupling
value yet**. What it does: it converts every placeholder operator into a constrained,
solvable equation, and it pins down exactly which numbers remain free — which is the honest
frontier (the Standard Model itself has ~19 free parameters).

Status tags: `[E]` established · `[A]` active research · `[S]` speculative · `[N]` non-physical.

---

## 1. Units (canonical dimensional assignment, ħ = c = 1)

The RHUFT state variables were dimensionally unconstrained. v0.2 fixes them so the action is
dimensionless:

| Variable | Meaning | Dimension |
|---|---|---|
| ρ | information density | [E]⁴ (energy density) |
| χ | field complexity | dimensionless |
| κ | closure (order parameter) | [E]² (mass²) |
| φ | phase / alignment | dimensionless (angle) |
| R | observational resolution | [E]² (mass² scale) |
| m | memory trace | dimensionless |

Then S = ∫ d⁴x L has [E]⁻⁴ · [E]⁴ = dimensionless. This is the G4 gap closed.

## 2. Minimal constrained dynamics

### 2.1 Closure sector (real scalar κ) — the centerpiece

V(κ) = −(μ²/2) κ² + (λ/4) κ⁴,  with μ² > 0, λ > 0.   (a φ⁴ double-well — `[E]`)

Ground state (spontaneous symmetry breaking):  ⟨κ⟩ = v = μ/√λ.
Expand κ = v + h; the excitation mass is  m_h² = V″(v) = 2μ²,  i.e.  **m_h = √2·μ**.

**Interpretation (the framework's real content).** "Closure" κ is an *order parameter*.
⟨κ⟩ ≠ 0 is a self-closed, stable vacuum; the **mass gap m_h = √2·μ is literally the energy
cost to open the closure**. This converts the primitive "stability = persistence under
recursive updating" into the precise, established statement **"stability = spontaneous
symmetry breaking → mass gap."** That identification is the correct core of RHUFT.

### 2.2 Relational/gauge sector (complex Φ + U(1)) — "measurement → mass"

L_H = |D_μ Φ|² − V(Φ) − ¼ F_{μν}F^{μν},  D_μ = ∂_μ − i g A_μ.

After SSB the gauge field acquires mass **m_A = g·v** (Higgs/Proca mechanism — `[E]`).
Interpretation: the "relation/measurement" interaction (gauge coupling g) is what gives the
relational field a mass — a precise, established version of "measurement has weight."

### 2.3 Information & complexity sectors

½(∂ρ)² − ½ m_ρ² ρ²   and   ½(∂χ)² − ½ m_χ² χ²   (Klein–Gordon scalars — `[E]`).

### 2.4 Full minimal Lagrangian

L = ½(∂ρ)² − ½m_ρ²ρ²
  + ½(∂χ)² − ½m_χ²χ²
  + ½(∂κ)² − V(κ)
  + |D_μΦ|² − V(Φ) − ¼F²
  + L_int(ρ, χ, κ, Φ)   [interactions constrained by Lorentz + gauge invariance]

The equations of motion follow from the Euler–Lagrange equation ∂L/∂q − ∂·(∂L/∂(∂q)) = 0,
which the notebooks already write correctly; v0.2 supplies the actual L above.

## 3. Reduction to known physics (the coupling-to-physics gap)

- Closure sector = **Ginzburg–Landau / Abelian–Higgs** → SSB + mass gap. `[E]`
- Gauge sector = **Proca** (massive vector) after SSB. `[E]`
- ρ, χ = **Klein–Gordon** scalars. `[E]`

So the *form* is now fully constrained by symmetry and renormalizability. This is the same
machinery that gives the Standard Model its Higgs, W/Z, and matter fields.

## 4. What v0.2 fixes vs. leaves free (honest accounting)

**Fixed by symmetry (no longer placeholders):** kinetic terms, φ⁴ potential shape, SSB
ground state, mass-gap formula m_h² = 2μ², Proca mass m_A = gv.

**Still free (inputs, not predicted):** μ, λ, g, m_ρ, m_χ, and any cross-couplings. These
are the framework's "Standard-Model-style" free parameters. *Predicting* them (i.e. deriving
α, m_e/m_p, etc.) is the open frontier — and it is NOT solved by golden-ratio numerology
(see tests, Test 2).

**Golden/silver-ratio ansatz:** removed from the dynamics. Treated as a separate, testable
hypothesis — and it is **falsified** by Test 1 (scale spacing) and Test 2 (golden angle vs
α). The framework loses nothing by dropping it.

## 5. 14-scale anchor

The scale ladder is an **input**, not a prediction, until two gaps close: G5 (anchor to real
lengths/energies — done, see `02-scales-of-physics/`) and G2 (predict ≥1 number). The
anchors are re-tested in `05-tests/01-numeric-tests.py`.

## 6. Reframed postulates (kept from the cross-map)

1. Relational ontology — a quantity exists only relative to an interaction. `[A]`
2. Emergent time — time = clock–system correlation (Page–Wootters). `[A]`
3. Spacetime from entanglement — geometry ↔ information/entanglement, not "measurement." `[A]`
4. System-specific stability — SSB mass gap, topological protection, bound states. `[E]`
5. Gapped scale hierarchy — EFT/RG octaves. `[E]`
6. Structured vacuum — boundary conditions modulate vacuum (Casimir). `[E]`

## 7. Numeric gates (must pass; results in `05-tests/`)

1. Scale-spacing: does the ladder follow constant (φ) spacing? → **Test 1**.
2. One predicted number: a mass ratio / coupling from the eigenproblem, not a fit. → **open**.
3. Lorentz invariance: any "c emergent" mechanism must match current null LIV bounds. → **open**.
4. Casimir reproduction: "measurement modulates vacuum" must yield the 1/d⁴ law. → **open**.

---

*This is the honest state of the art: the ontology is now anchored and the dynamics are now
constrained, but the values of the couplings — and therefore any genuine prediction — remain
the open problem. Tests 1–3 are run and recorded next.*
