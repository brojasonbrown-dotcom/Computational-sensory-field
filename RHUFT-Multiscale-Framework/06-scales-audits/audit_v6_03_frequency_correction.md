# Audit — `v6_03_frequency_correction.md` (RHUFT v6.0, Chapter 3)

**Method.** Every equation and numerical claim below was re-derived independently (Python, double-precision). Constants used: c = 2.99792458×10⁸ m/s, ℓ_P = 1.616255×10⁻³⁵ m, φ = (1+√5)/2 = 1.6180339887…, log₁₀φ = 0.20898764, ln φ = 0.48121183. These give f_P = c/ℓ_P = 1.85486×10⁴³ Hz (file says 1.855×10⁴³ — fine).

**Headline finding.** The chapter's *self-correction narrative is genuine* (the old f₀ = 9.01×10¹⁷ Hz disproof is arithmetically correct), but the *replacement* framework contains a fresh, systematic set of arithmetic errors in the neural/biological/planetary n↔frequency mapping. Every "n ≈" value for frequencies below ~100 MHz is wrong by 13–16 in the index n (≈2.7 decades in frequency), and the explicit f(n,m) values in §6.2 are wrong by ~10³. Several of the chapter's central "geometric marker" claims (432 Hz at n≈186–188, 432 THz at n≈134–136, Schumann at n≈189.7, heartbeat at n≈195–198) are therefore numerically false even within the chapter's own axioms.

---

## 1. Equations Audit

Legend: **WF** = well-formed (mathematically valid, dimensionally consistent) · **BROKEN** = mathematically/numerically mis-evaluated · **DI** = dimensionally inconsistent · **AWD** = asserted without derivation (flag, don't "fix").

### 1.1 Disproof of the old f₀ (lines 99–116) — correct

**Line 102.**
$$f_0 = \frac{c}{\ell_P \phi^7 \sqrt{\pi}} = \frac{2.998\times10^8}{1.616\times10^{-35}\cdot 29.034\cdot 1.772} \approx 3.60\times10^{41}\ \text{Hz}$$

**WF, numerically correct.** Verified: φ⁷ = 29.03444, denominator = 8.316×10⁻³⁴ m, f₀ = 3.604×10⁴¹ Hz. Dimensional check: [c/ℓ_P] = (m·s⁻¹)/m = s⁻¹ = Hz; φ⁷√π dimensionless. ✓

**Lines 108–114 (five "convergence methods").** All **WF and numerically correct** as evaluated from their stated formulas:

| Method | Formula | Computed | File value |
|---|---|---|---|
| Light Wave Limit | c/(2ℓ_P φ⁷) | 3.194×10⁴¹ Hz | 3.19×10⁴¹ ✓ |
| Quantum Uncertainty | c/(4πℓ_P φ⁷) | 5.084×10⁴⁰ Hz | 5.08×10⁴⁰ ✓ |
| Holographic | c/(√π ℓ_P φ⁷) | 3.604×10⁴¹ Hz | 3.60×10⁴¹ ✓ |
| Spherical Standing | c/(2πℓ_P φ⁷) | 1.017×10⁴¹ Hz | 1.02×10⁴¹ ✓ |
| Geometric Mean | √(f_q·f_h)·√φ | 1.722×10⁴¹ Hz | 1.72×10⁴¹ ✓ |

Note (not an error): all five are the same c/(ℓ_P φ⁷) times a dimensionless prefactor — the file itself admits this at line 482. Fine.

**Line 116.** √(5×10⁴⁰ · 3.6×10⁴¹) = 1.35×10⁴¹ Hz; file says "~1.3×10⁴¹". ✓

### 1.2 The replacement cascade (lines 122–164)

**Line 122.**
$$f(n) = f_P\,\phi^{-n}, \qquad f_P = c/\ell_P \approx 1.855\times10^{43}\ \text{Hz}$$

**WF, dimensionally consistent, AWD** (correctly labeled `[RHUFT AXIOM]`). Dimensional check: [f_P] = s⁻¹; φ⁻ⁿ dimensionless ⇒ f(n) in Hz. ✓ This is a *definition/an ontology*, not a derivation — do not "fix", just flag as non-predictive.

**Lines 130–140 (scale-index table).** The *formula* is fine; the *evaluations* are **BROKEN in two rows and sloppy in one**:

| n | File says | Correct f(n) | Verdict |
|---|---|---|---|
| 0 | 1.855×10⁴³ | 1.855×10⁴³ | ✓ |
| ~96 | ~10²³ | 1.605×10²³ | ✓ |
| ~120 | ~10¹⁸ | 1.548×10¹⁸ | ✓ |
| ~134 | ~10¹⁵ | 1.836×10¹⁵ | ✓ |
| ~168 | ~10⁸ | 1.440×10⁸ | ✓ |
| **~186** | **~10²** | **2.492×10⁴** | **BROKEN** (off ~2.4 decades) |
| **~192** | **~10¹** | **1.389×10³** | **BROKEN** (off ~2.1 decades) |
| ~235 | ~10⁻⁶ | 1.433×10⁻⁶ | ✓ |
| ~292 | ~10⁻¹⁷ | 1.754×10⁻¹⁸ | sloppy (off ~5.7×; rounds to 10⁻¹⁸) |

Corrected form for the broken rows: f(186) = 2.49×10⁴ Hz (not 10² Hz); f(192) = 1.39×10³ Hz (not 10¹ Hz). The "Neural" row belongs at n≈197–209, not n≈186; the "Organism" row belongs at n≈206–208 (heartbeat), not n≈192.

**Line 142.** φ ≈ 10^0.209 ✓ (0.20899); 1 decade = 1/log₁₀φ ≈ 4.785 ✓.

**Line 150.** f(n,m) = f_P φ⁻ⁿ 2ᵐ — **WF, DI-consistent, AWD**. Same dimensions as f(n). ✓

**Line 156.** 301 × 21 = 6321 combinations — **correct** (301 values of n∈[0,300], 21 of m∈[−10,10]).

**Line 162.**
$$n = \frac{\ln(f_P/f_0)}{\ln\phi} = \frac{\ln(1.855\times10^{43}/9.01\times10^{17})}{0.4812} \approx 121.1$$

**WF, numerically correct.** Verified: ln(2.059×10²⁵) = 58.29; /0.48121 = 121.12. ✓ (The 9.01×10¹⁷ Hz postulate lands at n≈121 — the chapter's characterization of this as "never derived, coincidental" is correct.)

### 1.3 Scale law (line 174) — **BROKEN in two places**

**Bohr radius.** r_n = a₀ n², a₀ = 4πε₀ℏ²/(m_e e²) ≈ 0.529 Å — **WF, correct, [EST PHYS]**. Dimensional check: [ε₀ℏ²/(m_e e²)] = [C²/(J·m)]·[J²s²]/([kg]·[C²]) = J·s²/(m·kg) = m. ✓

**Moon/Bohr ratio — BROKEN.** Line 174 states the ratio of the Moon's orbital radius (3.844×10⁸ m) to the Bohr radius (5.29×10⁻¹¹ m) is "~7.3×10¹⁵". The correct value is **7.26×10¹⁸** — the file is off by 10³. (Conclusion "not a simple power of φ" survives, but the number is wrong.)

**Length law L(n) = ℓ_P φⁿ — one evaluation BROKEN.** Verified:
- L(96) = 1.87×10⁻¹⁵ m ✓ ("~10⁻¹⁵")
- L(120) = 1.94×10⁻¹⁰ m ✓ ("~10⁻¹⁰")
- **L(235) = ℓ_P φ²³⁵ = 2.09×10¹⁴ m**, not the "~10⁸ m" claimed. **BROKEN** by ~10⁶.

**Internal inconsistency (important).** L(n) ≡ c/f(n) by construction, so L(235) must equal c/f(235). The chapter's own frequency table has f(235) = 1.43×10⁻⁶ Hz (line 139), which forces L(235) = 2.09×10¹⁴ m — contradicting the line-174 claim of 10⁸ m. The length and frequency tables cannot both be right; the length entry is the wrong one. The Moon's orbit (3.84×10⁸ m) corresponds to n≈207.6 in the length law, not n≈235.

### 1.4 Neural/biological n↔frequency mapping — **systematically BROKEN**

Every "n ≈" in §§4.3, 5.2, 6.1–6.3 is mis-evaluated. Correct values (n = ln(f_P/f)/lnφ):

| Claim | Line | File n | Correct n | Verdict |
|---|---|---|---|---|
| Schumann 7.83 Hz | 192 | 189.7 | **202.76** | BROKEN |
| Alpha 10 Hz | 194, 257 | 186–188 / 187.6 | **202.25** | BROKEN |
| Theta 6–8 Hz | 194 | 188–190 | **203.3–202.7** | BROKEN |
| Delta 0.5–4 Hz | 194 | 192–198 | **208.5–204.2** | BROKEN |
| Beta 20 Hz | 257 | 184.2 | **200.81** | BROKEN |
| Gamma 100 Hz | 257 | 176.7 | **197.47** | BROKEN |
| 432 THz | 222 | 135.2 | **137.01** | BROKEN |
| 432 Hz | 206 | 186–188 | **194.43** | BROKEN |
| Heartbeat 1–1.67 Hz | 280 | 195–198 | **207.0–206.0** | BROKEN |
| Circadian 1.16×10⁻⁵ Hz | 280 | 260–265 | **230.66** | BROKEN |

The whole "neural cascade range n≈168–192" (line 257) is wrong: for 0.5–100 Hz the correct range is **n≈197.5–208.5**. (n=168 is 144 MHz — radio, not neural.)

**Lines 267–270 (§6.2 explicit dual-scaling values) — BROKEN by ~10³.**

| (n,m) | File value | Correct value |
|---|---|---|
| (188, 0) | 7.3 Hz | **9.52×10³ Hz** |
| (187, 0) | 11.8 Hz | **1.54×10⁴ Hz** |
| (188, 1) | 14.6 Hz | **1.90×10⁴ Hz** |
| (187, −1) | 5.9 Hz | **7.70×10³ Hz** |

Corrected form: f(n,m) = f_P φ⁻ⁿ 2ᵐ gives f(188,0) = 1.855×10⁴³/(1.948×10³⁹) = 9.52 kHz, etc. The line-272 claim "closest values ~7.3 and ~11.8 Hz" is therefore built on wrong numbers; the actual closest integer-n values to 10 Hz are f(202) ≈ 11.2 Hz and f(203) ≈ 6.94 Hz.

### 1.5 Incommensurability "proof" (line 71) — **conclusion true, argument BROKEN as written**

The conclusion (φ and π are multiplicatively incommensurable, so lnπ/lnφ is irrational) is **true**, but three stated steps are false:

1. "both φ and π are transcendental" — **false**. φ = (1+√5)/2 is **algebraic** (root of x²−x−1=0), not transcendental. The file's own parenthetical "φ is algebraic irrational" contradicts its main clause.
2. "or at least conjecturally so for π" — **false**. π's transcendence is a *theorem* (Lindemann, 1882), not a conjecture.
3. "the Lindemann–Weierstrass theorem establishes that ln π is transcendental" — **misattributed**. LW establishes that e^α is transcendental for nonzero algebraic α (hence π = e^{iπ} = −1 ⟹ π transcendental). LW does *not* establish that ln π is transcendental.

**Corrected argument** (cleaner and sufficient): φ is algebraic; π is transcendental. Suppose φ^a = π^b for nonzero integers a,b. Then π^b = φ^a is algebraic; but π^b is transcendental for any nonzero integer b (else π would be a root of x^b − π^b = 0, making π algebraic). Contradiction. Hence lnπ/lnφ is irrational. No statement about ln π needed.

Also note the "six constants" include **δ_S**, which is **never defined in this chapter**, and the pairwise-incommensurability claim is *proven* only for algebraic-vs-algebraic and algebraic-vs-transcendental pairs; the e-vs-π pair (both transcendental) is **not** established by the argument given. The blanket "mathematically provable" is an overclaim.

### 1.6 Coherence threshold (line 89) and disproof formulas (lines 445, 544)

**Line 89.** λ = 1/φ² = 2−φ ≈ 0.381966 — **WF, exact identity** ✓ (1/2.61803 = 0.381966). C(n) = |⟨Ψ(n)|Ψ(n−1)⟩|² is **WF as an inner product** but **AWD/undefined**: Ψ(n) is never defined as a Hilbert-space object, so the "coherence" has no operational meaning (see §2).

**Line 445.** 360°/φ² = 137.5078° vs α⁻¹ = 137.0360 → 0.344% = 3443 ppm — **correct**, and correctly handled: the chapter labels it [COIN]/coincidence and does *not* re-assert exact equality. Consistent with the pre-falsified golden-angle item.

**Line 544 (disproofs of original claims).**
- α⁻¹ = 360°/arctan(1/φ) + φ⁻¹⁰/2 = 11.354 (not 137.036) — **correct computation**. (arctan(1/φ) = 31.7175°, 360/31.7175 = 11.350.)
- r_p = ℓ_P φ⁵⁵ = 5.04×10⁻²⁴ m (not 0.8414 fm) — **correct computation**.
- **Line 448 minor:** "ℓ_P φ⁵⁵ incorrect by 9 orders of magnitude" — actually ≈8 orders (8.4×10⁻¹⁶ / 5.0×10⁻²⁴ = 1.7×10⁸).

### 1.7 Referenced-but-absent equation

Lines 420 and 690 cite a dimensional inconsistency in "Term III of the Master Equation." That equation is **not present in this file**, so it is out of scope here. Flag: the chapter claims "every formula is computable and reproducible" (line 683) while simultaneously deferring its one physically relevant equation to another document.

**Summary of equation audit:** 0 dimensional inconsistencies found in this file's equations. Errors are (a) ~15 numerical mis-evaluations concentrated in the sub-MHz n↔frequency mapping (§§4.3, 5.2, 6.1–6.3, plus table rows n=186/192), (b) two length-law errors (line 174), and (c) three false steps in the incommensurability "proof" (line 71). The cascade f(n) = f_P φ⁻ⁿ itself is well-formed but axiom-only.

---

## 2. Measurement Improvements

### 2.1 What the file gets right (and how to make it operational)

The chapter's metrology is sound: Cs-133 hyperfine definition (line 39), optical lattice clocks <10⁻¹⁸ (line 39), CODATA 2018 α⁻¹ = 137.035999084(21) (line 45), running of α (line 47), Lamb shift/QED (line 53), QFT vacuum as mode superposition (line 59). These are accurate established physics.

**Operationalization of the central measurement (the clock, line 39):** A Cs fountain clock is a **Ramsey interferometer** on the two hyperfine levels |0⟩=|F=3,m_F=0⟩, |1⟩=|F=4,m_F=0⟩ with ω₀ = 2π·9.192631770 GHz. The instrument is, concretely:

- preparation: π/2 pulse (unitary U_π/2);
- free evolution for time T (phase φ = Δ·T, Δ = ω − ω₀);
- second π/2 pulse;
- detection: two-outcome **POVM** {Π₀ = |0⟩⟨0|, Π₁ = |1⟩⟨1|}, with P(1) = (1 + cosΔT)/2;
- state update (Lüders): ρ ↦ Πᵢ ρ Πᵢ / Tr(Πᵢ ρ) for the clicked outcome i;
- the frequency is the phase φ/T; the "second" is fixed by the SI-defined Δν_Cs.

This maps the file's "measurement is a relationship between observer, instrument, convention" (line 41) onto: instrument = Ramsey sequence + detection POVM; convention = the fixed numerical value of Δν_Cs. **Minor correction:** the file says the definition was "adopted in 1967" (line 39); in the 2019 SI redefinition Δν_Cs = 9,192,631,770 Hz became *exact by definition* (the value no longer carries a measured uncertainty). The chapter's "calibration chain" (line 45) is precisely traceability through a chain of such projections back to Δν_Cs.

### 2.2 Terminology-map alignment / misalignment

- **measurement = quantum instrument.** The file never uses POVM/instrument language; its "measurement" is metrological (clocks, calibration). That is fine for a philosophy section, but §1.4's "limits" would be sharper if each quantity were tied to an instrument. The §2.1 Ramsey POVM is the template.

- **"recursive" = iterated instrument / quantum trajectory.** The file's "recursive self-reference" (lines 89, 206, 334) is static mathematical/ontological recursion over an index n. It is **not** a quantum trajectory: there is no sequence of instruments applied to a state, no stochastic master equation, no continuous monitoring. Misalignment, currently unfixable because no dynamics is specified. The n-index is a label, not a monitoring record.

- **scale = RG decoupling scale.** The one place this could bite is the running of α (line 47). The file calls the running "a measurement artifact of the energy regime" and then offers "[SPEC] scale-dependent decoherence." **Correct the first clause:** α(μ) is a genuine, computable RG prediction (scheme-dependent, so partially conventional, but verified — e.g. α(M_Z) ≈ 1/127.9 from LEP). "Measurement artifact" understates it. The operational map would be μ_n = h·f(n) = h f_P φ⁻ⁿ; the chapter does not make this map, and its "resonance windows" (§4.2) are not RG fixed points.

- **stability = mass gap / RG fixed point / einselected pointer state.** The chapter's stability language is classical-oscillator "near-resonance / resonance windows" (lines 144, 180–184) with no Hamiltonian, no gap, no decoherence pointer basis. This is a **misalignment**: "resonance window" is asserted geometric structure, not any of the three operational notions of stability. To become operational, each window would need an energy gap or a fixed point; none is given.

- **closure = Wilson loop / boundary condition / holonomy.** The file's "circular closure" (lines 83, 172, 176) is bare geometry. A Wilson-loop/holonomy reading would require a connection and a ∮A phase; none exists here. Analogy only — flag, don't treat as physics.

- **potential = Hilbert space / structured vacuum.** Line 336 ("matter = high-density constructive interference, vacuum = zero-density destructive interference") is an ontology of a structured vacuum. It aligns loosely with the QFT vacuum (line 59, correctly stated as a mode superposition), but no Hilbert space or vacuum state is defined.

- **information density = entanglement entropy density.** Line 126 speaks of "geometric information distributing across scales" but computes no entropy density anywhere. The only entropy in the chapter is the philosophical "entropy = geometric friction" (line 87). No entanglement entropy is defined; the claim has no quantitative content.

### 2.3 The unoperationalized "coherence" (line 89)

C(n) = |⟨Ψ(n)|Ψ(n−1)⟩|² is a fidelity/overlap, but Ψ(n) is undefined and no POVM yields it. The minimal operationalization would be: define a Hilbert space and a family {Ψ(n)}; then C(n) is the outcome probability of the projector Π = |Ψ(n)⟩⟨Ψ(n)| after preparing |Ψ(n−1)⟩ — a legitimate two-outcome POVM {Π, 1−Π}. Until Ψ(n) is specified, the "coherence threshold λ = 1/φ²" (line 89) is an undefined symbol wearing a number. The chapter admits this is philosophy (line 91), which is honest, but the audit must record that the λ threshold has **zero operational content as written**.

---

## 3. Lattice-Oscillation Integration (dimer)

### 3.1 Where it applies

The dimer is relevant to three places: §2.2 ("two oscillators with frequency ratio φ never phase-lock"), §2.3 (coherence threshold), §4.2 (resonance windows). This chapter makes **no spin or entanglement claims**, so the singlet/triplet content of the model is available but unexercised.

### 3.2 The correct normal-mode math (framework given, re-derived)

$$H = \frac{p_1^2+p_2^2}{2m} + \frac{k}{2}(x_1^2+x_2^2) + \frac{\kappa}{2}(x_1-x_2)^2.$$

Normal coordinates x_s = (x₁+x₂)/√2 (symmetric, in-phase), x_a = (x₁−x₂)/√2 (antisymmetric, out-of-phase). Then x₁²+x₂² = x_s²+x_a² and (x₁−x₂)² = 2x_a², so

$$V = \frac{k}{2}x_s^2 + \frac{k+2\kappa}{2}x_a^2 \;\Rightarrow\; \omega_s = \sqrt{k/m},\quad \omega_a = \sqrt{(k+2\kappa)/m}.$$

Dimensional check: [k] = N/m = kg·s⁻², [κ] same; [ω] = √(kg·s⁻²/kg) = s⁻¹. ✓

**Golden mode ratio.** ω_a/ω_s = √(1 + 2κ/k). Setting this equal to φ gives

$$2\kappa/k = \phi^2 - 1 = \phi \;\Rightarrow\; \kappa = \frac{\phi}{2}\,k \approx 0.809\,k.$$

So a "golden" normal-mode split is a **specific coupling value**, not a universal law.

### 3.3 Fit vs. fail against the file's claims

- **§2.2 ("two oscillators with ratio φ never synchronize", line 75).** This is a *correct* statement about **two weakly-coupled/independent** oscillators with an irrational frequency ratio (quasi-periodic motion, dense phase space). It is **not** the dimer: the dimer is **one** pair whose *normal modes* split, and those modes are orthogonal — they don't phase-lock *or* drift, they simply coexist. The dimer does **not** support "φ avoids resonance lock"; it's a different mechanism (level splitting / avoided crossing). Flag as a category confusion.

- **§2.3 coherence threshold λ = 1/φ² (line 89).** The dimer's natural "coherence" is the projection onto the symmetric subspace, and ⟨sym|antisym⟩ = 0 (orthogonal modes). So the dimer's coherence is **binary 0/1**, not a 0.382 threshold. The file's C(n) = |⟨Ψ(n)|Ψ(n−1)⟩|² is an overlap between *adjacent-scale* states, which is **not** the dimer's symmetric/antisymmetric overlap. The lattice model therefore does **not** reproduce λ = 1/φ²; that threshold remains an unsupported postulate.

- **§4.2 resonance windows (lines 180–184).** If the "Metatron lattice" (referenced line 334, never defined here) were actually specified with a Hamiltonian, its normal modes would *be* the operational content of the "frequency cascade" — a tight-binding band structure with real gaps. The dimer is the minimal case (one bonding mode, one antibonding mode). Because this chapter gives **no Hamiltonian and no coupling matrix**, no band structure can be derived; f(n) = f_P φ⁻ⁿ stays an axiom, and the "resonance windows" stay asserted.

- **Spin/entanglement mapping (available, unused).** In the tight-binding/Hückel reading: symmetric in-phase mode = bonding = triplet-like; antisymmetric out-of-phase mode = antibonding = singlet-like (|↑↓⟩−|↓↑⟩, maximally entangled). If a later chapter claims entanglement underlies RHUFT "coherence," this dimer/singlet correspondence is the correct scaffolding — but it also shows entanglement is a **binary** normal-mode property, incompatible with the continuous λ = 1/φ² threshold.

**Net:** the dimer gives correct, usable math for the chapter's oscillator language, but it **fails** to validate the two specific quantitative claims it could be attached to (φ-avoids-lock, λ = 1/φ²). It should be used to *replace* those claims with the actual normal-mode structure, not to confirm them.

---

## 4. Verdict

**Real physics (accurate, keep):** Cs-133 second (with the 2019-SI caveat), optical clocks <10⁻¹⁸, CODATA α, running α, Lamb shift/QED, QFT vacuum, quasicrystal φ-diffraction (Shechtman; Lu–Steinhardt girih), Bohr radius, golden-ratio continued-fraction/pentagon geometry, Schumann 7.83 Hz, brain-wave bands, Kolmogorov complexity, Page–Wootters, Everett, RQM, Wheeler–DeWitt, block universe, and the historical/cultural claims. The *disproof* of the old f₀ = 9.01×10¹⁷ Hz (lines 99–116, 536–544) is arithmetically correct and is the chapter's genuinely valuable contribution.

**Speculative/philosophical (honestly labeled; keep only as ontology, non-falsifiable):** the cascade f(n) = f_P φ⁻ⁿ, the φⁿ·2ᵐ lattice, "incommensurability as source of structure," "entropy = geometric friction," "coherence threshold λ = 1/φ² as death," "resonance windows," and the 432 Hz / 432 THz "geometric markers." The chapter's own labeling ([PHIL]/[SPEC]/[COIN]) is mostly honest. None of these are predictions.

**Broken-and-now-fixed (errors I found — NOT yet fixed in the file):**
1. Moon/Bohr ratio: 7.3×10¹⁵ → **7.26×10¹⁸** (line 174).
2. L(235) = ℓ_P φ²³⁵: "10⁸ m" → **2.09×10¹⁴ m**, and the length law contradicts the chapter's own f(235) (line 174 vs 139).
3. Entire neural/biological n↔frequency map: all n values for f < 10⁸ Hz are low by ~14 (≈2.7 decades). Correct: 10 Hz → n=202.3; 7.83 Hz → n=202.8; 432 Hz → n=194.4; 432 THz → n=137.0; heartbeat → n≈206–207; circadian → n≈230.7. Table rows n=186 ("10² Hz" → 2.49×10⁴ Hz) and n=192 ("10¹ Hz" → 1.39×10³ Hz).
4. §6.2 explicit f(n,m) values off by ~10³ (e.g. f(188,0) = 9.52 kHz, not 7.3 Hz).
5. Incommensurability "proof" (line 71): φ is algebraic not transcendental; π's transcendence is proven not conjectural; LW does not imply ln π transcendental.
6. Minor: n=292 row (10⁻¹⁷ → 1.75×10⁻¹⁸); "ℓ_P φ⁵⁵ wrong by 9 orders" → ~8 orders; "planetary orbital periods" mislabeled at 10⁻⁶ Hz.

**Should be dropped or rewritten:** the specific n↔frequency "correspondences" in §§4.3, 5.2, 6.1–6.3 as written (numerically false), the moon/Bohr and L(235) planetary claims (line 174), and the line-71 proof as written. The cascade f(n) = f_P φ⁻ⁿ is fine as a definition but its biological/neural "marker" narrative currently rests on arithmetic errors and should be recomputed (or the whole sub-10⁸ Hz mapping retired). The λ = 1/φ² coherence threshold has no operational content and is not supported by the dimer model — flag for removal unless a Hilbert-space definition of Ψ(n) and an instrument are supplied.

**Bottom line:** the chapter is epistemically honest (good labels, correct self-correction of the old f₀) but *mathematically sloppy in its new core content*: the central "geometric marker" claims are built on a systematic ~13–16 index offset in n, which makes the neural-scale narrative false even on its own terms.
