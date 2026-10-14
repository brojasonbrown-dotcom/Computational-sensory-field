# RHUFT -> Established Physics: Refactored Lexicon

Purpose: replace the RHUFT vocabulary with the standard terms it already maps
onto, anchor every term to a real arXiv paper, and identify every quantity by
its **measured CODATA/PDG value** (not a phi-derived value). This makes the
framework *checkable*: a claim is only as good as the measured number it can
reproduce.

## 1. The term mapping (RHUFT -> standard -> arXiv -> measured identifier)

| RHUFT term | Standard term | arXiv | Measured identifier |
|---|---|---|---|
| information density / "density of measured dimensions" | **entanglement (entropy) density** | hep-th/0603001 (Ryu-Takayanagi), gr-qc/9504004 (Jacobson) | `S = A / 4ℓ_P²`, `ℓ_P = 1.616255e-35 m` |
| gravity from information density | **thermodynamic / entropic gravity** | gr-qc/9504004, 1001.0785 (Verlinde) | `G = 6.67430e-11 m³ kg⁻¹ s⁻²` |
| time to measure information = impact of density | **quantum speed limit + Bekenstein bound** | quant-ph/9710043 (Margolus-Levitin) | `t ≥ h/4E`, `ħ = 1.054571817e-34 J·s` |
| spacetime built from information | **spacetime from entanglement** | 1005.3035 (Van Raamsdonk), hep-th/9711200 (Maldacena) | `S_EE = Area(γ)/4G_N` |
| scale / octave = stable level of transfer | **renormalization-group scale** | 0905.1317 (Swingle) | running couplings `α(Q²)`, `α_s(Q²)` |
| closure = self-returning persistence | **Wilson loop / holonomy** | (gauge theory, e.g. Polyakov loop) | `W = Tr P exp(i ∮ A·dx)` |
| potential / "nothingness" before form | **Hilbert space / vacuum sector** | (QFT; zero-point energy) | `E_0 = ½ħω` per mode |
| stability = persistence under update | **fixed point / attractor** | (RG fixed point) | `β(g*) = 0` |
| 1/f "octaves as equal levels" | **scale invariance / self-organized criticality** | (established; no single paper) | `P(f) ∝ f⁻¹` |
| self-measurement | **einselection / decoherence** | (Zurek, Rev.Mod.Phys. 75, 715 (2003)) | pointer states, `ρ_off-diag ~ e^{-γt}` |

## 2. The measured values are the identifiers (CODATA 2022 / PDG)

| Constant | Symbol | Value | Role |
|---|---|---|---|
| speed of light | c | 2.99792458e8 m/s (exact) | defines spacetime |
| reduced Planck | ħ | 1.054571817e-34 J·s | quantum resolution |
| Newton constant | G | 6.67430e-11 m³ kg⁻¹ s⁻² | the thing to *derive* |
| Planck length | ℓ_P | 1.616255e-35 m | resolution of "nothing vs something" |
| Planck time | t_P | 5.391247e-44 s | the "iteration count" unit |
| Planck mass | m_P | 2.176434e-8 kg | energy scale of gravity |
| fine-structure | α⁻¹ | 137.035999177 | the "why this number" target |
| electron mass | m_e | 0.51099895000 MeV | mass-ratio anchor |
| muon mass | m_μ | 105.6583755 MeV | mass-ratio anchor |
| proton mass | m_p | 938.27208816 MeV | mass-ratio anchor |
| Boltzmann | k_B | 1.380649e-23 J/K | information<->energy (Landauer) |

## 3. Why each mapping is correct (not metaphor)

- **"information density" = entanglement entropy.** Ryu-Takayanagi (hep-th/0603001) *proved* that in holography the entanglement entropy of a region equals the area of a minimal surface: `S_EE = Area/4G_N`. Information density literally *is* geometry. This is the single strongest anchor of the whole framework.

- **"gravity from information density" = Jacobson/Verlinde.** Jacobson (gr-qc/9504004) derived the Einstein equation from `δQ = T dS` on a horizon, with `S ∝ area`. Verlinde (1001.0785) rebuilt Newton's law as an entropic force. Your sentence is this program, verbatim.

- **"time to measure information" = Margolus-Levitin.** quant-ph/9710043 proves a state needs at least `t = h/4E` to reach an orthogonal (distinguishable) state. Processing information costs time, and the cost is set by energy = density. Your "amount of time to measure information = impact of density" is this bound.

- **"scale/octave" = RG scale.** Swingle (0905.1317) organizes information "in terms of scale" and shows it defines a higher-dimensional geometry — your "octave ladder" is entanglement renormalization, stated non-standardly.

- **"self-measurement" = einselection.** The environment continuously "measures" a system; only the pointer states survive. This is *exactly* your "whatever persists must be recursively distinguishable," and it is established (decoherence is measured).

## 4. What this refactor reveals (honestly)

The vocabulary maps one-to-one. **The framework is a correct, non-standard restatement of the holographic/thermodynamic-gravity frontier.** That is real and unusual — most "theories of everything" map to nothing.

But the refactor also reveals the exact gap: **every term maps to physics that already exists.** There is not one term here that names something new. The only thing that would make it *new* is a **derived number** that the standard terms, with the measured identifiers above, *force* out — and which the framework has not yet produced.

## 5. The concrete next calculation (now that terms are anchored)

With the refactor, "gravity from information density" becomes a precise, doable task:

1. Take the Bekenstein bound `S ≤ 2πkRE/ħc` and the Margolus-Levitin `t ≥ h/4E`.
2. Combine with `S = A/4ℓ_P²` (holographic entropy).
3. Ask: can `G` (or `α`, or `m_e/m_p`) be *forced* from these, with no free knob?

Jacobson already did the equivalent for Einstein's equations. Verlinde's Newtonian version is contested. If the framework can close this loop and land on the measured `G = 6.67430e-11`, it becomes physics. If it only rearranges into `G = G`, it's a restatement — accurate, but not a key.
