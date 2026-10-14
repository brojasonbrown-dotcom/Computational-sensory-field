"""
RHUFT Test 1 - Rigorous Derivation Attempt for G (audit notebook)
=================================================================

Can G be derived from {Bekenstein bound, Margolus-Levitin bound, holographic
entropy-area law}? This runs the full audit: dimensional closure, symbolic
derivation tree, circularity check, underdetermination check, and a numerical
closure test. Verdict at the end.

Inputs (correct forms, with hbar explicit):
  Bekenstein:      S <= 2 pi k_B R E / (hbar c)
  Margolus-Levitin: tau >= pi hbar / (2 E)   <=>   E >= pi hbar / (2 tau)
  Holographic:     S = k_B c^3 A / (4 G hbar)      <-- contains G
"""

from __future__ import annotations

import math

import numpy as np
from scipy import constants as C
from sympy import Eq, pi, simplify, solve, symbols


def section(t: str) -> None:
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


# ---------------------------------------------------------------------------
# 1. Scope and classification protocol (the decision tree)
# ---------------------------------------------------------------------------
section("1. CLASSIFICATION PROTOCOL")
protocol = [
    ("Premises already functions of G?", "flag circularity"),
    ("G formable from non-gravitational constants alone?", "else need extra scale"),
    ("System variables cancel without extra assumptions?", "else underdetermined"),
    ("Added closure law contains hidden gravitational content?", "flag tautological"),
    ("Unique assumption-independent G remains?", "else NOT a derivation"),
]
for q, a in protocol:
    print(f"  {q:<55} -> {a}")


# ---------------------------------------------------------------------------
# 2. Formal statement of inputs
# ---------------------------------------------------------------------------
section("2. FORMAL STATEMENT OF INPUTS")
k_B, c, hbar, G, R, E, A, tau = symbols("k_B c hbar G R E A tau", positive=True)
S_bek = 2 * pi * k_B * R * E / (hbar * c)
S_hol = k_B * c ** 3 * A / (4 * G * hbar)
ML = tau * E - pi * hbar / 2     # tau >= pi hbar/(2E)  =>  tau*E - pi*hbar/2 >= 0
print(f"  Bekenstein (saturated) : S = {S_bek}")
print(f"  Holographic           : S = {S_hol}")
print(f"  Margolus-Levitin      : tau*E >= {pi * hbar / 2}")
print("\n  AUDIT NOTE: the holographic law contains G explicitly. It cannot be")
print("  an output-neutral premise unless that law is itself derived without G.")


# ---------------------------------------------------------------------------
# 3. Rigorous dimensional audit (sympy)
# ---------------------------------------------------------------------------
section("3. DIMENSIONAL AUDIT: can G be built from hbar and c alone?")
a, b = symbols("a b")
# [hbar^a c^b] = M^a L^(2a+b) T^(-a-b) ;  [G] = M^-1 L^3 T^-2
# exponents:  M: a = -1 ;  T: -a-b = -2 ;  L: 2a+b = 3
sol = solve([Eq(a, -1), Eq(-a - b, -2)], [a, b])
lhs_L = (2 * a + b).subs(sol)
print(f"  from M,T equations: a = {sol[a]}, b = {sol[b]}")
print(f"  then L exponent 2a+b = {lhs_L},  but G needs L exponent 3")
print(f"  -> {lhs_L} != 3 : NO monomial hbar^a c^b equals G.")
print("  => Any derivation MUST introduce an extra dimensionful scale (R or tau),")
print("     and that introduction is where G can be smuggled back in.")


# ---------------------------------------------------------------------------
# 4. Symbolic derivation tree (sympy)
# ---------------------------------------------------------------------------
section("4. SYMBOLIC DERIVATION TREE")
G1 = solve(Eq(S_bek, S_hol), G)[0]
print(f"  saturate Bekenstein == Holographic  ->  G = {simplify(G1)}")

G2 = simplify(G1.subs(A, 4 * pi * R ** 2))
print(f"  spherical geometry A = 4 pi R^2     ->  G = {G2}")

G3 = simplify(G2.subs(E, pi * hbar / (2 * tau)))
print(f"  insert ML E = pi hbar/(2 tau)       ->  G = {G3}")
print("\n  STATUS: this is a RELATION, not a derivation of a universal constant,")
print("  because R and tau are system-specific. A universal G requires R*tau")
print("  to be fixed by an independent principle (which itself re-imports G).")


# ---------------------------------------------------------------------------
# 5. Circularity and underdetermination checks
# ---------------------------------------------------------------------------
section("5. CIRCULARITY / UNDERDETERMINATION CHECKS")
print("  [CIRCULAR]       holographic premise S = k_B c^3 A/(4 G hbar) already has G.")
print("  [UNDERDETERMINED] result G = c^4 R tau/(pi hbar) still depends on R, tau.")
print("  [HIDDEN INSERT]   any closure fixing R*tau to a Planck value uses G itself.")
print("  => classification: UNDERDETERMINED, with tautology risk if a Planck")
print("     closure is introduced to eliminate R*tau.")


# ---------------------------------------------------------------------------
# 6. Numerical closure test: does the natural Planck closure even work?
# ---------------------------------------------------------------------------
section("6. NUMERICAL CLOSURE TEST (R = l_P, tau = t_P)")
c_val = C.c
hbar_val = C.hbar
G_true = C.G
lP = C.physical_constants["Planck length"][0]
tP = C.physical_constants["Planck time"][0]

G_derived = c_val ** 4 * lP * tP / (np.pi * hbar_val)
print(f"  G_true (CODATA)        = {G_true:.5e} m^3 kg^-1 s^-2")
print(f"  G_derived (Planck close)= {G_derived:.5e} m^3 kg^-1 s^-2")
print(f"  ratio G_derived/G_true = {G_derived / G_true:.6f}")
print(f"  1/pi                   = {1 / np.pi:.6f}")
print("\n  -> closing with the natural Planck scale gives G/pi, NOT G. The derivation")
print("     is off by a factor of pi even at the Planck scale. Fixing that factor")
print("     requires inserting exactly the gravitational structure it claimed to derive.")


# ---------------------------------------------------------------------------
# 7. Verdict
# ---------------------------------------------------------------------------
section("7. VERDICT")
print("  UNDERDETERMINED + CIRCULARITY RISK.")
print("  The triad yields G = c^4 R tau/(pi hbar): a scale-relation, not a number.")
print("  No unique G follows without a closure that itself encodes G. The natural")
print("  closure (Planck scale) is off by pi, proving the bound-saturation is not exact.")
print("  -> RHUFT does NOT derive G. To pass, it must produce G from a closure")
print("     whose premises contain no G and no Planck-scale combination.")


if __name__ == "__main__":
    pass
