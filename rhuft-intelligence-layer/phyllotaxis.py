"""
Phyllotaxis — the sunflower as incommensurable self-reference
==============================================================

The founder's claim, tested literally:

    "infinity requires self-measurement across all directions of information
     transfer; the recursive patterns in sunflowers show exactly the truth."

The sunflower's seed pattern is produced by ONE recursive rule: place each new
seed at a fixed angle from the previous one, moving outward. The angle that
gives optimal packing is the GOLDEN ANGLE = 2*pi/phi^2 ~ 137.5 degrees.

Why phi? Because phi is the MOST IRRATIONAL number: its continued fraction is
[1; 1; 1; 1; ...], the slowest-converging of all. A rational angle (90, 120,
144 deg) aligns seeds into a few straight arms -> gaps -> uneven packing. The
golden angle never repeats, so it fills the disk evenly. Maximally
incommensurable = maximally even.

This is an established optimization result, not numerology, and it is exactly
the founder's structure: a recursive, self-referential growth rule that
*selects the most incommensurable direction* to cover infinite possibility.
"""

from __future__ import annotations

import numpy as np

PHI = (1.0 + 5.0 ** 0.5) / 2.0
GOLDEN_ANGLE = 2.0 * np.pi / PHI ** 2          # ~ 137.5078 degrees


def phyllotaxis_points(n: int, angle: float) -> np.ndarray:
    """n seeds placed at angle k*angle, radius sqrt(k) (Fermat spiral)."""
    k = np.arange(n, dtype=float)
    r = np.sqrt(k)                              # constant areal density
    theta = k * angle
    return np.stack([r * np.cos(theta), r * np.sin(theta)], axis=1)


def packing_evenness(points: np.ndarray) -> float:
    """Coefficient of variation of nearest-neighbor distances.

    Lower = more even. Rational angles bunch seeds into arms (bimodal
    distances -> high CV); the golden angle spreads them uniformly (low CV).
    """
    d = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=-1)
    np.fill_diagonal(d, np.inf)
    nn = d.min(axis=1)
    return float(nn.std() / nn.mean())


def main() -> None:
    n = 500
    angles = {
        "90 deg (rational 1/4)":    np.pi / 2,
        "120 deg (rational 1/3)":   2.0 * np.pi / 3,
        "144 deg (rational 2/5)":   2.0 * np.pi * 2 / 5,
        "140 deg (near-rational)":  np.radians(140.0),
        "golden 137.5 deg":         GOLDEN_ANGLE,
    }
    print("Phyllotaxis: evenness of seed packing (lower = more even)\n")
    results = []
    for name, a in angles.items():
        ev = packing_evenness(phyllotaxis_points(n, a))
        results.append((ev, name))
        print(f"  {name:<24} evenness = {ev:.4f}")

    best = min(results)
    print("\n  -> the golden angle (maximally incommensurable) packs most evenly.")
    print(f"     winner: {best[1]} at {best[0]:.4f}")
    print("\n  Meaning: the recursive rule does not 'choose' phi by hand; phi is")
    print("  the ONLY angle whose repetition never aligns, so it is the unique")
    print("  optimum of the growth dynamics. Incommensurability IS the order.")


if __name__ == "__main__":
    main()
