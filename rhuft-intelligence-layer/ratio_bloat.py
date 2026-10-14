"""
Ratio bloat - why recursive scale prediction is exponentially fragile
=======================================================================

The founder's point: to predict the Planck scale from ours you would need to
run as many iterations as the universe holds, because the ratios "bloat".

This is the Lyapunov / hierarchy problem. A recursive (self-referential) map
with ANY sensitivity to its input amplifies a tiny uncertainty exponentially
with the number of iterations. Two trajectories that start 1e-6 apart become
completely decorrelated after ~50 steps of a chaotic map.

For the physical hierarchy, the Planck -> cosmic length ratio is ~1e61
(~292 phi-steps; ~16 orders of magnitude in energy for electroweak -> Planck),
so bottom-up prediction requires initial precision that is physically
unattainable. That is a REAL reason unification is hard - not a lack of effort.
"""

from __future__ import annotations

import numpy as np


def logistic(x: float, r: float = 3.9) -> float:
    return r * x * (1.0 - x)


def main() -> None:
    x1, x2 = 0.400000, 0.400001            # 1e-6 apart
    print("Two trajectories 1e-6 apart, chaotic map r=3.9:\n")
    print(f"{'step':<6} {'x1':<12} {'x2':<12} {'|x1-x2|':<12}")
    for n in range(0, 60, 10):
        print(f"{n:<6} {x1:<12.6f} {x2:<12.6f} {abs(x1 - x2):<12.6f}")
        for _ in range(10):
            x1 = logistic(x1)
            x2 = logistic(x2)
    print(f"{60:<6} {x1:<12.6f} {x2:<12.6f} {abs(x1 - x2):<12.6f}")

    print("\n  -> initial 1e-6 grows to O(1) in ~50 iterations (Lyapunov > 0).")
    print("     'the ratios bloat' = exponential sensitivity of recursion.")
    print("     Planck <-> cosmic is a ~1e61 ratio, so bottom-up prediction is")
    print("     exponentially fragile. This is the hierarchy problem, and it is")
    print("     a real, open obstacle to unification - not a solved method.")


if __name__ == "__main__":
    main()
