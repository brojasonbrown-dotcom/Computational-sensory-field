"""
"Calculate without fully calculating" - the fixed point vs the chaos
====================================================================

The founder asks: to know the end of time you'd have to run the full iteration
count, "unless it can be calculated without being fully calculated." That is
not a glitch - it is the deepest move in physics, and it has a precise answer.

For a map with a STABLE FIXED POINT, the infinite-iteration limit is computable
in CLOSED FORM: solve f(x*) = x*. You never iterate to infinity; you read off
the fixed point. This is what the renormalization group, universality, symmetry
(Noether), and effective field theory all do: the infinite scale/time hierarchy
collapses to a finite computation AT the fixed point.

For a CHAOTIC map, there is no such shortcut - the outcome is computationally
irreducible; you MUST run every step. That is the real "does not compute" - a
genuine theorem (chaos / undecidability), not a bug.
"""

from __future__ import annotations


def logistic(x: float, r: float) -> float:
    return r * x * (1.0 - x)


def main() -> None:
    # --- stable fixed point -------------------------------------------------
    r = 2.9
    xstar = 1.0 - 1.0 / r                     # analytic fixed point, NO iteration
    print("STABLE case (r=2.9):\n")
    print(f"  analytic fixed point x* = 1 - 1/r = {xstar:.6f}")
    print("  (this is 'calculating the infinite limit without iterating')\n")
    x = 0.3
    print(f"  step  0 : {x:.6f}")
    for n in range(1, 21):
        x = logistic(x, r)
        if n in (1, 2, 3, 5, 10, 20):
            print(f"  step {n:>2} : {x:.6f}")
    print(f"  -> converges to {xstar:.6f}; the infinite answer was known at step 0.\n")

    # --- chaotic: no such shortcut ------------------------------------------
    print("CHAOTIC case (r=3.9):\n")
    print("  no closed-form fixed point exists; the infinite-time outcome")
    print("  cannot be computed except by running it. That is the real")
    print("  'does not compute' - computational irreducibility, a theorem.\n")

    print("The universe computes via fixed points, attractors, and symmetry")
    print("(the renormalization group), not by brute force over all of time.")
    print("Scale invariance - your 1/f insight - IS 'calculating the whole")
    print("hierarchy without calculating the whole hierarchy'.")


if __name__ == "__main__":
    main()
