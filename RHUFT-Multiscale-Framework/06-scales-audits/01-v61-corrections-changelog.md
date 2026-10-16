# v6.1 Corrections Changelog — file by file (applied in place, 2026-10-11)

Each corrected source file now carries a "v6.1 corrections applied 2026-10-11" header note.
Speculative/philosophical content was preserved; only broken math / dimensional errors /
factual misstatements were fixed. Full audit details in `audit_<file>.md`.

| File | What was fixed |
|---|---|
| `v6_04_master_equation.md` | Term III → `κ·(L_c/A)·∮∇Ψ·dS` (was dimensionally [L]⁻¹); Σφ⁻ᵏ = 2.613 (was 1.615); φ⁻¹³ = 0.001919 (was 0.0015); φ⁹⁶ = 1.87 fm (was 1.3 fm); proton "24 orders" → ~8; scale-table n values corrected; 432 THz → n≈137, 432 Hz → n≈194; (π,e) incommensurability flagged open; LaTeX brace fixes |
| `v6_03_frequency_correction.md` | n↔frequency remap: 432 Hz → 194, 432 THz → 137, Schumann → 202.8, alpha → 202.3, heartbeat → 206–207, circadian → 230.7; Moon/Bohr ratio 7.26×10¹⁸; L(235) = 2.09×10¹⁴ m; incommensurability "proof" corrected; f(n,m) values fixed (~10³) |
| `v6_02_geometric_framework.md` | φ¹³ = 521.0 (was 441.35); icosahedron V = (5φ²/6)a³, V_ico/V_VE = φ²/(2√2) ≈ 0.9256 (was 1.309), V_ico/V_oct = 4.628 (was 6.545); circumradius 0.9511a; jitterbug endpoint radii; spiral pitch angle; resonance-window + cascade tables recomputed; proton → n≈94.3, Bohr → n≈117.3; L(292) ≈ 1.71×10²⁶ m (DISPROV withdrawn); Term III × ℓ(n) |
| `v6_phenomenon_07_entanglement.md` | Lindblad missing 1/ℏ added; CHSH detection threshold 82.84% = 2(√2−1) (was ~75%); Hensen S = 2.42±0.20 ~2σ (was ±0.28, 1.5σ); (π,e) open; §9 numerology retagged [NUMERO] |
| `v6_phenomenon_10_light.md` | n↔band remap (visible 136–137, radio 169–188, X-ray 114–128, gamma 97–114, CMB → 139/153); (π,e) open; "exponential decay" → 1/r geometric spreading; Epistemic Audit table regenerated |
| `v6_phenomenon_16_mass_values.md` | Higgs 125.2 GeV (was 125.09); electron 207× lighter than muon (was 2000×); "~5 orders" (was 11); (π,e) open; LCM(3,4,5,6)=60 not 360; "six divisors" (was four) |
| `v6_phenomenon_24_zpe.md` | Lamb shift ∝ α(Zα)⁴ = α⁵ (was α³); (π,e) open; "incommensurability regulates ZPE/divergence" reframed (phases freely settable; renormalization by cutoff); WdW eigenvalue clarified; 2/3/4-fold symmetries commensurable (rational ratios); flavor≠5-fold, color=SU(3) |
| `v6_phenomenon_31_toroidal.md` | closure = safety factor q = (r/R)(B_φ/B_θ) rational (was R/r); hairy-ball theorem (χ=2 vs χ=0) for sphere vs torus; Page–Wootters corrected (clock correlation, not branch selection) |
| `v6_phenomenon_34_time_crystals.md` | Floquet ansatz e^{−iεt/ℏ}; quasi-energy mod 2πℏ/T; "winding number 2" → π-spectral pairing; "information halved" → area vs volume law; I Ching not a Hamiltonian cycle; He-3 = magnon-BEC, not Floquet-MBL |
| `v6_phenomenon_25_nonlocality.md` | Aspect ~40σ (S=2.697±0.015); Hensen 2.42±0.20; Term III × ℓ_P; (π,e) open; CHSH threshold η > 2(√2−1) ≈ 82.8% (Eberhard 2/3) |

## New chapter added
- `v6.1_geometric_resonance_grid.md` — geometric resonance → scales → relativistic grid;
  resonance → frictionless dimensional balance (the correct replacement for φ-numerology).

## Left deliberately unchanged (speculative ontology, not broken)
Golden-angle = 1/α; uniform φ-spacing; λ = 1/φ² coherence threshold; "incommensurability →
entanglement/ZPE" — all flagged in the audits as `[S]`/falsified but preserved per the
no-deletion instruction. They should be treated as historical framing, superseded by the
lattice/dimer mechanism in v6.1.
