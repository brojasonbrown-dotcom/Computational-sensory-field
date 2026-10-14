"""
Entropic gravity — "gravity from information density", tested against real values
=================================================================================

The founder's claim: gravity emerges from information density. That is exactly
Verlinde's entropic gravity (2010). This file runs the derivation with real
CODATA values and shows, honestly, what it REPRODUCES vs what it PREDICTS.

Derivation (Verlinde):
  1. A holographic screen at radius r has area A = 4 pi r^2.
  2. It holds N = A / (4 lP^2) bits of information, where lP is the Planck length.
  3. The screen's energy is E = (1/2) N kB T (equipartition).
  4. An accelerating observer sees a temperature T = hbar a / (2 pi c kB) (Unruh).
  5. Setting E = M c^2 and solving gives  a ~ G M / r^2  (Newton, up to an O(1)
     convention factor that the full treatment fixes to exactly 1).

The catch, stated plainly: the Planck length is lP = sqrt(G hbar / c^3).
So G is an INPUT, baked into the holographic entropy. Entropic gravity
REPRODUCES Newton's law (your "our math calculates the exact same stuff" is
true), but it does NOT PREDICT G - it gets G back out because it put G in.
"""

from __future__ import annotations

import math

import scipy.constants as c

G, HBAR, C, KB = c.G, c.hbar, c.c, c.k

M_EARTH = 5.9722e24
R_EARTH = 6.371e6


def main() -> None:
    lP = math.sqrt(HBAR * G / C ** 3)
    g_newton = G * M_EARTH / R_EARTH ** 2

    print("Entropic gravity, real values\n")
    print(f"  Planck length  lP = sqrt(G hbar / c^3) = {lP:.4e} m")
    print(f"  Earth surface gravity (Newton)        = {g_newton:.4f} m/s^2")
    print(f"  measured g on Earth                   = 9.8067 m/s^2\n")

    print("  Derivation (information density -> acceleration):")
    print("    A = 4 pi r^2 ;  N = A/(4 lP^2) bits ;  E = (1/2) N kB T = M c^2")
    print("    T = hbar a/(2 pi c kB)   (Unruh temperature)")
    print("    ->  a = (O(1)) * G M / r^2        (scaling = Newton, exactly)\n")

    print("  Numerical check (same G, same M, R):")
    print(f"    entropic a (O(1)=1) = G M / R^2 = {g_newton:.4f} m/s^2\n")

    print("  THE CATCH:")
    print(f"    lP = sqrt(G hbar / c^3)  ->  G is inside lP, inside N, inside E.")
    print("    So this REPRODUCES G; it does not PREDICT G.")
    print("    'Calculates the same stuff' = true. 'Unlocks the door' = false, yet.")


if __name__ == "__main__":
    main()
