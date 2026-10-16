# Audit — v6_phenomenon_34_time_crystals.md

**Auditor framework applied as given.** Tagging: [E] established/measured, [A] active research, [S] speculative, [N] non-physical. Terminology map (measurement = quantum instrument {E_a, Φ_a}; recursive = iterated instrument / trajectory; closure = holonomy / boundary condition; stability = mass gap / RG fixed point / pointer state; scale = RG decoupling scale; information density = entanglement-entropy density; potential = Hilbert space / structured vacuum). Prior falsifications treated as binding: (1) uniform φ-spacing across scales is falsified (measured mean log10-ratio 4.69 vs predicted 0.209); (2) golden angle ≠ 1/α (off by 3443 ppm). Lattice-oscillation (dimer) model available for integration.

**Sources note:** This audit relies on established quantum/statistical physics and the file's own reference list (lines 131–141, 183–193). WebSearch was not used; no source is invented. Where a bibliographic detail is uncertain it is flagged as "verify," not asserted as fact.

**Overall posture:** This is one of the more disciplined files in the corpus. It already self-labels the φ-scaling and coherence-metric content as [DISPROV] (lines 121, 145) and keeps [EST PHYS]/[OBSERVED]/[PHIL] mostly separated. The physics backbone — Wilczek proposal → no-go theorems → Floquet-MBL discrete time crystals → 2017 experiments — is correct. The defects are: one dimensional inconsistency in the Floquet ansatz, several loose or wrong physical characterizations, non-operational measurement language, and culture/dozenal sections that carry no physical content.

---

## 1. EQUATIONS AUDIT

| # | Location | Equation (transcribed) | Label | Notes |
|---|----------|------------------------|-------|-------|
| E1 | L15, L9 | subharmonic response at frequency `f/n`, `n ∈ Z, n>1` (typically `f/2`) | well-formed (definitional) | Correct operational signature of a discrete time crystal. |
| E2 | L27, L77 | `H(t+T) = H(t)` | well-formed | Definition of drive periodicity. Correct. |
| E3 | L29 | `nT/T = n` | well-formed (trivial) | Tautological; adds nothing. |
| E4 | L57 | `x → x+a`, `t → t+T` | well-formed | Symmetry transformations; correct. |
| E5 | L77 | `iℏ ∂ₜ|ψ(t)⟩ = H(t)|ψ(t)⟩` | well-formed | Time-dependent Schrödinger equation. Correct. |
| E6 | L77 | `|ψ(t)⟩ = e^{−iεt}|φ(t)⟩`, `|φ(t+T)⟩=|φ(t)⟩` | **dimensionally inconsistent** | Floquet ansatz missing ℏ relative to E5. See correction C1. |
| E7 | L77 | `U(T) = 𝒯 exp(−i ∫₀ᵀ H(t) dt / ℏ)` | well-formed | Floquet operator = time-ordered exponential. Correct, and it is literally a holonomy (see §3). |
| E8 | L77 | quasi-energies defined modulo `2π/T` | **dimensionally inconsistent with E5** | Only correct if ε is an angular frequency (ℏ=1 convention). With explicit ℏ it must be modulo `2πℏ/T`. See C2. |
| E9 | L93 | `|ψ(t)⟩` periodic with period `nT` "up to a phase factor" | well-formed (imprecise) | This *is* the Floquet property; fine as prose. |
| E10 | L121 | `ω_crystal = ω₀ · φ^{−m}` | dimensionally consistent, **asserted-without-derivation [N]** | Both sides are frequencies. Not broken; it is numerology, already [DISPROV] in-file. No independent derivation exists. |
| E11 | L121 | `C_temporal(t) = |⟨Ψ(t)|Ψ(t−φτ)⟩|² > Ω_C` | mathematically well-formed, **non-operational [N]** | Both sides dimensionless; inner product over states at two different times is a computable fidelity-like object, not a single-measurement observable. Asserted without derivation. |
| E12 | L121 | `Ω_C ≈ 0.381966` | well-formed constant, **[N]** | `0.381966… = 1/φ² = 2−φ`. Arbitrary threshold; no experimental basis (the file itself concedes this). |
| E13 | L151 | Hilbert-space dimension `2^N` for N two-level spins | well-formed, correct | Dimension of (C²)^{⊗N}. ✓ |
| E14 | L151 | quasi-energy spectrum has `2^N` levels within one Floquet zone | well-formed, correct | For N qubits there are 2^N Floquet eigenvalues per zone. ✓ |
| E15 | L155 | `60 = LCM(1,2,3,4,5)` | well-formed, correct | LCM = 60. ✓ (Cultural filler, not physics.) |
| E16 | L65 | "64 hexagrams = vertices of a 6-dimensional hypercube"; "sequence … returns to start after traversing all 64 vertices" | combinatorial assertion, **partly false** | `2^6 = 64` is correct. The claim that the traditional (King Wen) hexagram sequence is a Hamiltonian cycle on the 6-cube is false: consecutive King Wen hexagrams do not generally differ by exactly one line. This is a factual overreach in the cultural section, not physics. |

**Equations absent but implied:** The file repeatedly invokes "order parameter = Fourier component of magnetization at the subharmonic frequency" (L57, L15) without writing it. The operational form is given in §2 (M1). That is an omission, not an error.

### Corrections (only for broken / dimensionally inconsistent equations)

**C1 — Floquet ansatz (E6).** The same paragraph keeps ℏ in E5 (Schrödinger) and E7 (Floquet operator) but drops it from the ansatz. Under the explicit-ℏ convention of the file:

> File: `|ψ(t)⟩ = e^{−iεt}|φ(t)⟩`
> Corrected: `|ψ(t)⟩ = e^{−iεt/ℏ}|φ(t)⟩`, with `(H(t) − iℏ∂ₜ)|φ(t)⟩ = ε|φ(t)⟩`.

**Dimensional check:** `[ε] = energy`, `[t] = time`, `[ℏ] = energy·time`, so `[εt/ℏ] = (E·T)/(E·T) = 1` (dimensionless exponent). ✓ Substituting into E5 gives the quasi-energy eigenvalue equation with ε in energy units, consistent with E5 and E7. The file's version would make ε an angular frequency while E5/E7 treat ℏ explicitly — an internal unit inconsistency. (Acceptable alternative: declare ℏ=1 everywhere and keep `e^{−iεt}`; the file does neither consistently.)

**C2 — quasi-energy periodicity (E8).** With the C1 convention (ε an energy), the two Floquet modes `e^{−iεt/ℏ}u(t)` and `e^{−i(ε+2πℏ/T)t/ℏ}u(t)e^{-i2πt/T}` are identical, so:

> Corrected: quasi-energy ε is defined modulo `2πℏ/T = ℏω` (energy units), equivalently modulo `ω = 2π/T` if ε is expressed as an angular frequency.

The file's "modulo `2π/T`" is right only in the frequency (ℏ=1) convention, which contradicts its own explicit ℏ in E5/E7. Minor, but it is the kind of slip that compounds when "quasi-energy" is later treated as an energy.

**Non-corrections (flagged, not "fixed"):** E10, E11, E12 are mathematically well-formed but non-physical/numerological. Per the framework they must be *dropped*, not repaired — there is no mathematical error to fix, only a physical one.

---

## 2. MEASUREMENT IMPROVEMENTS

### What the file says
L15–17 describes "magnetization measured as a function of time" and a "clear f/2 peak in the Fourier spectrum," but never names the instrument, POVM, or the correlation function being measured. L87 ("Does measurement create time?") treats periodicity as something revealed/created by the measuring apparatus, which is a category error.

### Operational treatment (what should be said)

**Observable.** For the ion-trap DTC (L15, Zhang et al. 2017, 10 Yb⁺ qubits) the observable is the site-averaged magnetization
`M_z = (1/N) Σᵢ σ_z⁽ⁱ⁾`.

**Instrument.** The actual readout is site-resolved spin-dependent fluorescence. Per the framework this is a quantum instrument, not a bare "measurement":

- Single-qubit POVM: `E↑ = |↑⟩⟨↑|`, `E↓ = |↓⟩⟨↓|` (projective), with state update (Kraus map) `Φ_m(ρ) = E_m ρ E_m / Tr(E_m ρ)`, i.e. Kraus operator `K_m = |m⟩⟨m|`.
- Chain: tensor-product POVM over bit-strings, `E_s = |s⟩⟨s|`; `M_z` is reconstructed by summing outcomes.
- NV ensemble (L15, Choi et al. 2017): collective fluorescence is a **coarse-grained / noisy collective** readout of total spin projection, not an ideal projector. The file's "`10^{16}` NV centers" is an unverified detail and, if taken as the many-body interaction network size, is misleading — the dipolar-interacting subset that constitutes the time crystal is far smaller. Verify, but immaterial to the physics.

**The operational order parameter (missing from the file).** A discrete time crystal is diagnosed by the stroboscopic autocorrelation:

> `C(n) = ⟨M_z(nT) M_z(0)⟩`,  `n ∈ Z`.

Period-doubling means `C(n)` has its dominant Fourier component at `ω = π/T` (alternating sign), i.e. the stroboscopic trajectory `⟨M_z(nT)⟩` alternates. This is the concrete content of "f/2 peak" (L15). Robustness (L17) = this alternation survives finite size, finite time (prethermal plateau), disorder, and pulse error — not "topological protection" in the naive sense (L21).

**Terminology map (alignments vs misalignments).**

- *measurement = instrument {E_a, Φ_a}* — **misaligned as written.** The file says "measurement of the magnetization" without any POVM/update. Fix: state the projective instrument above and note that each stroboscopic read re-prepares (projects) the state, so the DTC order parameter is measured on an ensemble of repeated runs, not one trajectory.
- *recursive = iterated instrument / trajectory* — **alignable.** The "recursive steps" of L9 correspond exactly to the iterated Floquet map `U(T)^n` composed with the stroboscopic readout: `C(n)` is the resulting quantum-trajectory correlation. The file's "geometric steps" language can be made precise this way.
- *distinction = projector/POVM element* — **alignable.** The harmonic vs subharmonic distinction is the projector onto the symmetric vs antisymmetric Floquet doublet (see §3): the `+1` vs `−1` eigenspaces of `U(T)`. This is a genuine POVM-element distinction, and the file never states it.
- *closure = holonomy / boundary condition* — **aligns well.** `U(T) = 𝒯 exp(−i∫H dt/ℏ)` (L77) *is* a holonomy around the closed time loop, and `|φ(t+T)⟩ = |φ(t)⟩` is a periodic boundary condition. This is the strongest real-physics anchor for the file's "geometric closure" language. The file gestures at it (L79) but never identifies `U(T)` as the holonomy.
- *stability = …* — **needs correction.** The DTC's robustness is *not* a mass gap. It is (a) MBL: an extensive set of emergent local integrals of motion (no thermalization), and (b) π-spectral pairing of the Floquet unitary (eigenvalues of `U(T)` in pairs `e^{iεT}`, `−e^{iεT}`), i.e. a quasi-energy spectral gap protecting the subharmonic mode. Prethermal DTCs add (c) an exponentially long thermalization time. The file says "MBL mechanism" (L31) but then swaps in "topological property / geometric closure" (L21, L115), which overstates it.
- *scale = RG decoupling scale* — **alignable.** The relevant scale is the high-frequency (drive) scale `ω = 2π/T`: Floquet prethermalization is valid below a decoupling scale set by `ω`, with `τ_th ~ exp(c·ω/J)`. The file's "scale-independent universality" (L51–53) is really microscopic-detail independence, not RG scale invariance; restating it as a decoupling-scale claim makes it correct.
- *information density = entanglement-entropy density* — **alignable, and the file's version is wrong.** L101 claims the time crystal "reduces information content by a factor of 2." That is not well-defined. The correct statement: MBL DTC eigenstates are **area-law** entangled (entanglement entropy ∝ boundary), whereas thermal states are **volume-law**. "Compressed" = area-law; "incompressible thermal" = volume-law. No factor-of-2 in entropy.
- *potential = Hilbert space / structured vacuum* — the "geometric field" of L81/L85 maps to the Hilbert space of the driven system plus the Floquet/Sambe structure; nothing more is needed.

### L87 "Does measurement create time?" — verdict
Misaligned. The subharmonic periodicity is a property of the correlation function `C(n)` of a specified observable; it is there before any measurement (in the Floquet steady state) and measurement merely samples it. The superposition-of-Floquet-states language on L87 conflates deterministic unitary evolution with readout. Replace with: the DTC order parameter is an expectation value in the Floquet steady state, sampled stroboscopically.

---

## 3. LATTICE-OSCILLATION INTEGRATION (dimer / two-site normal modes)

### Verify the framework's dimer math (it is correct)
Two coupled oscillators:

> `H = (p₁²+p₂²)/2m + (k/2)(x₁²+x₂²) + (κ/2)(x₁−x₂)²`

Normal coordinates `X_s = (x₁+x₂)/√2` (in-phase/symmetric), `X_a = (x₁−x₂)/√2` (out-of-phase/antisymmetric):

- `x₁²+x₂² = X_s² + X_a²`, and `(x₁−x₂)² = 2X_a²`.
- Potential = `(k/2)X_s² + (k/2 + κ)X_a² = (k/2)X_s² + ((k+2κ)/2)X_a²`.
- Hence `ω_s = √(k/m)`, `ω_a = √((k+2κ)/m)`. ✓ (matches the given framework.)

Weak-coupling (tight-binding) splitting: `ω_a − ω_s ≈ κ/√(mk) = κ/(mω_s)` for `κ ≪ k`. The two-site tight-binding qubit version `H = −t(|1⟩⟨2|+|2⟩⟨1|)` has bonding `|+⟩=(|1⟩+|2⟩)/√2` (energy −t) and anti-bonding `|−⟩=(|1⟩−|2⟩)/√2` (energy +t); `|−⟩` is the out-of-phase, singlet-like (maximally entangled under site exchange) mode, exactly as the framework states.

### Mapping onto the period-doubled time crystal — it fits the *subspace*, not the whole system
A period-2 DTC has two symmetry-related sectors related by the discrete time translation. Restrict `U(T)` to that doublet:

> `U(T)|A⟩ = |B⟩`, `U(T)|B⟩ = |A⟩`  ⇒  `U(T) ≃ σˣ` in the `{|A⟩, |B⟩}` basis.

Its eigenstates are the dimer's normal modes:

- `|+⟩ = (|A⟩+|B⟩)/√2`, eigenvalue `+1`, quasi-energy `ε = 0` — **symmetric/bonding/in-phase**, harmonic (period-T) mode.
- `|−⟩ = (|A⟩−|B⟩)/√2`, eigenvalue `−1`, quasi-energy `ε = π/T` — **antisymmetric/anti-bonding/out-of-phase**, the **subharmonic (period-2T) mode**.

**This is the cleanest correspondence in the whole file.** The period-doubled state is the antisymmetric combination of the two T-translated sectors — the singlet-like "entangled" mode of the effective two-site lattice. The file's "phase factor that marks the distinction between the first and second traversals" (L35) is precisely the `−1` holonomy phase of `U(T)` (a π phase per loop, 2π over two loops). The framework's identification *antisymmetric = out-of-phase = singlet-like = entangled* transfers to the Floquet doublet, and the "geometric closure" (L21) acquires a real meaning: the holonomy `U(T)` has eigenvalue −1, so closure is achieved after two loops (`U(T)² = +1` on the doublet).

### Where it fails / limits
1. **The DTC is not a dimer.** The two-level structure describes only the symmetry doublet (the period-doubling degeneracy). A real DTC is a many-body system, and its stability requires MBL (an extensive set of local integrals of motion) — which the dimer does not capture. The dimer explains *why* period-2 exists, not *why it is stable against heating*.
2. **The symmetry is temporal, not spatial.** In-phase/out-of-phase in the oscillator is exchange of two spatial sites; the DTC's two sectors are related by time translation `T`. The map is an isomorphism of the 2-D degeneracy subspace — a precise analogy, not a literal identification of microscopic degrees of freedom.
3. **"Entangled/singlet" is apt but limited.** `|−⟩=(|A⟩−|B⟩)/√2` is a time-cat state, genuinely maximally entangled across the two "time-sites." But the many-body DTC eigenstate is not a two-body singlet; the entanglement that matters for MBL stability is area-law entanglement of the full eigenstate, not the two-level cat structure.

**Net:** the dimer picture *fits* the period-doubling subspace and gives the correct holonomy phase; it *fails* as a model of the many-body localization that makes the DTC robust. Use it as the effective description of the doublet, not of the system.

---

## 4. VERDICT

**Real physics (keep, [E]/[OBSERVED]).**
- Wilczek proposal; Bruno and Watanabe–Oshikawa no-go theorems for continuous time crystals (L9, L35, L132–134). ✓
- Discrete time crystals in Floquet-MBL systems; 2017 observations (Zhang et al.; Choi et al.) (L9, L15, L138–139). ✓
- Floquet formalism: Schrödinger eq, Floquet operator, quasi-energy, Sambe space (L77). ✓ (after the C1/C2 ℏ fix)
- MBL as the robustness mechanism; universality as microscopic-detail independence (L31, L51–53). ✓
- Floquet topological phases and π-spectral pairing (L99, L115) — with the caveat below.
- References L131–141, L183–193 are, as far as verifiable here, genuine and correctly cited, with two minor bibliographic imprecisions (see below).

**Speculative / philosophical (label [S]/[PHIL], do not treat as physics).**
- "Geometric closure in the time-complexity dimension" (L9, L21, L55, L81). Its only rigorous content is the holonomy `U(T)` + periodic boundary condition (see §2/§3); the rest is interpretation.
- Page–Wootters and Rovelli framings (L83–85) — real frameworks, applied here only as philosophy.
- Cyclic cosmology / songlines / Tusi couple / African-fractal analogies (L63–71) — cultural, zero predictive content.

**Broken-and-now-fixed (actual errors corrected).**
- Floquet ansatz missing ℏ (E6/C1) and quasi-energy periodicity (E8/C2) — dimensional inconsistency vs the same paragraph's explicit ℏ. Fixed above.
- "Winding number = 2 for period-doubling" (L99) — **mischaracterization.** Period-doubling is π-spectral pairing of the Floquet unitary (eigenvalue pairs `e^{iεT}`, `−e^{iεT}`), not a winding number 2. Rewrite accordingly.
- "Information content reduced by a factor of 2" (L101) — wrong; replace with area-law vs volume-law entanglement.
- I Ching "Hamiltonian cycle on the 6-cube" (L65) — the 64-vertex count is right, the Hamiltonian-path claim is false.
- Helium-3 time crystal listed as a "2T" period-doubling platform (L48, L51) — **misclassified.** The superfluid ³He magnon-BEC time crystal (Autti et al.) is a spontaneously precessing magnon condensate / spin-superfluid phenomenon, a *different mechanism* from the Floquet-MBL period-doubled DTC. Lumping it under one "period-doubling" universality claim overstates the case. Label [A]/mechanism-distinct.

**Should be dropped (non-physical / already falsified).**
- `ω_crystal = ω₀·φ^{−m}` (E10), `C_temporal(t)` with `Ω_C ≈ 0.381966` (E11/E12), and any 13th-harmonic closure (L121, L145). The file already marks these [DISPROV]; they are consistent with the two prior falsifications and must remain dropped.
- The entire "dozenal/12-fold/60-fold periodicity" physics framing (L151–155): the number 12 does not "appear" in Floquet physics; the section is arithmetic/cultural filler with no physical mechanism. (The file half-admits this at L151; the rest of the section should go.)
- "Measurement creates/reveals time" (L87) as stated.

**Minor bibliographic items to verify (not asserted as false):** Bruno's no-go theorem is more precisely PRL 111, 070402 (2013); PRL 110, 118901 is his Comment on Wilczek (L133). Sacha's PRA 91, 033617 (2015) title is "Modeling spontaneous breaking of time-translation symmetry," not "Modeling Floquet Systems" (L135). The `10^{16}` NV-center figure (L15) is unverified and likely refers to total sample defects, not the interacting ensemble.
