import math

phi = (1 + math.sqrt(5)) / 2

print("=" * 70)
print("RHUFT PASS 7 - NUMERIC TESTS")
print("=" * 70)

# ---- Test 1: stable-scale ladder log10 spacing ----
ladder = [
    ("Planck",              1.616e-35),
    ("GUT (speculative)",   1.973e-32),
    ("Electroweak (246GeV)", 8.02e-19),
    ("QCD (~1 fm)",         9.87e-16),
    ("Nuclear (~3 fm)",     3.0e-15),
    ("Atomic (Bohr a0)",    5.292e-11),
    ("Molecular",           1.0e-9),
    ("Condensed/meso",      1.0e-7),
    ("Biological (cell)",   1.0e-5),
    ("Human/classical",     1.0e0),
    ("Geophysical",         1.0e7),
    ("Stellar",             1.0e9),
    ("Galactic",            1.0e21),
    ("Cosmological (c/H0)", 1.4e26),
]
lg = [math.log10(L) for _, L in ladder]

print("\nTEST 1 - stable-scale ladder: log10 spacing")
print(f"{'scale':24s} {'L [m]':>12s} {'log10(L)':>10s}")
for (n, L), v in zip(ladder, lg):
    print(f"{n:24s} {L:12.4e} {v:10.3f}")

ratios = [lg[i+1] - lg[i] for i in range(len(lg)-1)]
print("\nAdjacent log10-ratios:")
for i, r in enumerate(ratios):
    print(f"  {ladder[i][0]:20s} -> {ladder[i+1][0]:20s} {r:7.3f}")

mean = sum(ratios) / len(ratios)
var = sum((r - mean) ** 2 for r in ratios) / len(ratios)
sd = math.sqrt(var)
lg_phi = math.log10(phi)
within = sum(1 for r in ratios if abs(r - lg_phi) < 0.5)

print(f"\nmean log10-ratio = {mean:.3f}")
print(f"std (population) = {sd:.3f}")
print(f"min / max        = {min(ratios):.3f} / {max(ratios):.3f}")
print(f"phi-spacing pred (log10 phi) = {lg_phi:.4f}")
print(f"ratios within +/-0.5 of phi-spacing = {within} of {len(ratios)}")
print(f"VERDICT: uniform phi-spacing across scales is "
      f"{'CONSISTENT' if within > len(ratios)//2 else 'FALSIFIED'} "
      f"(mean={mean:.2f} vs pred {lg_phi:.3f}, std={sd:.2f})")

# ---- Test 2: golden angle vs 1/alpha ----
print("\n" + "=" * 70)
print("TEST 2 - golden angle vs inverse fine-structure constant")
ga_deg = (2 * math.pi / phi**2) * 180 / math.pi
a_inv = 137.035999084
diff = ga_deg - a_inv
print(f"golden angle 2pi/phi^2 = {ga_deg:.6f} deg")
print(f"1/alpha (CODATA 2018)  = {a_inv:.9f}")
print(f"difference             = {diff:+.6f} deg")
print(f"relative               = {abs(diff)/a_inv*100:.4f} %  (~{abs(diff)/a_inv*1e6:.0f} ppm)")
print("VERDICT: identity FALSE at modern precision (0.34% off)")

# ---- Test 3: hierarchy anchors ----
print("\n" + "=" * 70)
print("TEST 3 - hierarchy anchors (observational, not predictions)")
E_planck = 1.220890e19
Lambda_qcd = 0.25
t_planck = 5.391247e-44
age_s = 13.787e9 * 365.25 * 24 * 3600
efolds = math.log(1.4e26 / 1.616e-35)
ticks = age_s / t_planck
print(f"E_Planck / Lambda_QCD (0.25 GeV) = {E_planck/Lambda_qcd:.3e}")
print(f"e-folds Planck->Hubble (ln Lh/Lp) = {efolds:.2f}")
print(f"Planck ticks in universe age      = {ticks:.3e}")
print(f"  age = {age_s:.3e} s ; t_Planck = {t_planck:.3e} s")
