"""
Koide formula — the geometric meaning (and the silver ratio, not phi)
======================================================================

Koide (1981):  (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3

Let x = (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)) in R^3, and 1 = (1,1,1) the
"democratic" axis. Then:

    Q = |x|^2 / (x . 1)^2

and (x . 1)^2 = |x|^2 |1|^2 cos^2(theta) = 3 |x|^2 cos^2(theta), so

    Q = 1 / (3 cos^2 theta).

Q = 2/3  <=>  cos^2 theta = 1/2  <=>  theta = 45 degrees.

So the Koide formula is the statement that the sqrt-mass vector points at
EXACTLY 45 degrees to the (1,1,1) axis. 45 degrees is sqrt(2) geometry:

    cos(45) = 1/sqrt(2) = sqrt(2)/2,   sqrt(2) = (1 + sqrt(2)) - 1 = delta_S - 1

where delta_S = 1 + sqrt(2) is the SILVER ratio -- which IS in the RHUFT
framework (the spatial-locking constant), while the GOLDEN ratio phi is NOT
involved here. This is the honest redirect: Koide lives in silver-ratio (45
deg, sqrt(2)) geometry, not golden-ratio geometry.
"""

from __future__ import annotations

import math


def main() -> None:
    me = 0.51099895000
    mmu = 105.6583755
    mtau = 1776.86

    x = [math.sqrt(me), math.sqrt(mmu), math.sqrt(mtau)]
    one = [1.0, 1.0, 1.0]
    dot = sum(a * b for a, b in zip(x, one))
    norm_x = math.sqrt(sum(a * a for a in x))
    norm_one = math.sqrt(3.0)

    Q = norm_x ** 2 / dot ** 2
    cos_theta = dot / (norm_x * norm_one)
    cos2 = cos_theta ** 2
    theta_deg = math.degrees(math.acos(cos_theta))

    print("GEOMETRIC REFORMULATION OF KOIDE\n")
    print(f"  Q = |x|^2/(x.1)^2        = {Q:.9f}   (2/3 = {2/3:.9f})")
    print(f"  cos^2(theta)            = {cos2:.9f}   (1/2 = {0.5:.9f})")
    print(f"  theta                   = {theta_deg:.6f} degrees  (45 = perfect)")
    print()
    print("SILVER-RATIO (not golden-ratio) CONTENT\n")
    delta_S = 1.0 + math.sqrt(2.0)
    print(f"  cos(45) = 1/sqrt(2)     = {1/math.sqrt(2):.9f}")
    print(f"  sqrt(2)                 = {math.sqrt(2):.9f}")
    print(f"  silver ratio delta_S-1  = {delta_S - 1:.9f}   (same thing)")
    print(f"  golden ratio phi        = {(1+math.sqrt(5))/2:.9f}   (NOT involved)")
    print()
    print("MEANING:")
    print("  Koide = the sqrt-masses sit at 45 deg to the democratic axis.")
    print("  45 deg is sqrt(2) = silver-ratio geometry. The framework already")
    print("  carries delta_S = 1 + sqrt(2); phi is the wrong key for THIS relation.")


if __name__ == "__main__":
    main()
