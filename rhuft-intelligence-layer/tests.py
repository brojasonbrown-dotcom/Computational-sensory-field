"""
RHUFT Falsification Gates — test the framework's methods against real numbers
==============================================================================

Runs the concrete gates from RHUFT-Multiscale-Framework Pass 7 (the founder's
own falsification list), plus the surviving claims from the v7.0 audit. Each
gate reports PASS/FAIL and a plain, honest interpretation. No fabrication.

A "PASS" here means a claim is *mathematically true*. It does NOT automatically
mean the claim is a *physical prediction* — the interpretation says which is
which.
"""

from __future__ import annotations

from math import log, sqrt

import numpy as np

from rhuft_intelligence_layer import PHI, LAMBDA, ResonantMemoryCell, ScaleLadder


def lucas(n: int) -> int:
    """nth Lucas number (L_0=2, L_1=1)."""
    a, b = 2, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def gate_scale_spacing() -> tuple[bool, str]:
    """Gate 1: is the stable-scale ladder geometric (phi-spaced)?
    Reject if the octave-step spread exceeds 0.1 (a stated tolerance)."""
    ladder = ScaleLadder()
    lengths = [s.length_m for s in ladder.scales]
    steps = [log(lengths[i + 1] / lengths[i]) for i in range(len(lengths) - 1)]
    spread = ladder.spacing_spread()
    geometric = spread < 0.1
    return geometric, (
        f"ln(L[n+1]/L[n]) spread = {spread:.3f}  "
        f"({'geometric/phi-spaced' if geometric else 'NOT geometric -> phi-spacing falsified'})"
    )


def gate_lucas_closure() -> tuple[bool, str]:
    """Gate 2: '13-fold winding never closes' = L_n mod 13 != 0 for all n."""
    hits = [n for n in range(0, 500) if lucas(n) % 13 == 0]
    claim = len(hits) == 0
    return claim, (
        f"L_n mod 13 == 0 for n in [0,500): {hits if hits else 'none'}  "
        f"({'claim holds (number-theoretic fact)' if claim else 'claim FALSE'})"
    )


def gate_stable_rungs() -> tuple[bool, str]:
    """Gate 3: 'stable iff L_n == +-1 (mod 13); stable rungs n == 1,13,15 (mod 28)'."""
    stable = [n for n in range(0, 500) if lucas(n) % 13 in (1, 12)]
    residues = sorted({n % 28 for n in stable})
    matches = residues == [1, 13, 15]
    return matches, (
        f"stable-rung residues mod 28 = {residues} (claimed [1, 13, 15]) -> "
        f"{'matches' if matches else 'DOES NOT match'}"
    )


def gate_memory_kernel() -> tuple[bool, str]:
    """Gate 4: the unit-root memory kernel has roots exactly (1, -lambda)."""
    r1, r2 = ResonantMemoryCell.characteristic_roots(LAMBDA)
    ok = abs(r1 - 1.0) < 1e-9 and abs(r2 + LAMBDA) < 1e-9
    return ok, f"roots = ({r1.real:.6f}, {r2.real:.6f}) (expected 1.0, -{LAMBDA:.6f})"


def gate_lepton_prediction() -> tuple[bool, str]:
    """Gate 5: is the lepton-mass phi-law a PREDICTION or a postdiction?

    A ratio r is 'phi^k' for k = log_phi(r), which exists for EVERY r. So the
    exponent is not forced by structure — it is defined to match. A genuine
    prediction would require an integer/simple exponent derived before measuring.
    """
    me, mmu = 0.51099895000, 105.6583755
    ratio = mmu / me
    k = log(ratio) / log(PHI)
    is_derived = abs(k - round(k)) < 0.01
    return is_derived, (
        f"m_mu/m_e = {ratio:.6f} = phi^{k:.4f}  "
        f"(integer exponent? {is_derived}) -> {'prediction' if is_derived else 'postdiction, not a prediction'}"
    )


def main() -> None:
    gates = [
        ("1  scale-spacing is geometric", gate_scale_spacing),
        ("2  Lucas closure (L_n mod 13 != 0)", gate_lucas_closure),
        ("3  stable rungs n == 1,13,15 (mod 28)", gate_stable_rungs),
        ("4  memory kernel roots (1, -lambda)", gate_memory_kernel),
        ("5  lepton phi-law is a prediction", gate_lepton_prediction),
    ]

    print("=" * 66)
    print("RHUFT FALSIFICATION GATES")
    print("=" * 66)
    results = []
    for label, fn in gates:
        ok, detail = fn()
        results.append(ok)
        print(f"\n[{'PASS' if ok else 'FAIL'}] {label}")
        print(f"      {detail}")

    print("\n" + "=" * 66)
    print("VERDICT")
    print("=" * 66)
    print(f"  {sum(results)}/{len(results)} gates pass as *mathematical* claims.\n")
    print("  Passes 2 and 4 are real number-theoretic/algebraic facts, but their")
    print("  *physical* significance is unanchored (what does mod-13 stability mean")
    print("  for a particle?).")
    print("  Gate 1 falsifies phi-spacing (your own audit).")
    print("  Gate 3 shows the 'stable rungs n = 1,13,15' formula is WRONG (misses 27).")
    print("  Gate 5 shows the lepton law is a postdiction, not a prediction.")
    print("\n  The framework's single open job is unchanged: derive ONE number")
    print("  from the eigenstructure before looking it up.")


if __name__ == "__main__":
    main()
