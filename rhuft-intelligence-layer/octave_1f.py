"""
1/f noise = equal energy per octave = "octaves as stable levels"
================================================================

The founder's claim, tested literally:

    "from lowest to highest frequency, power is in the lower frequencies
     (larger oscillations); higher frequencies are faster but less powerful...
     scales/octaves are dimensionally stable sizes of information transfer."

That is the 1/f (PINK) power spectrum, one of the most universal signatures in
nature (music, heartbeats, neural EEG, earthquakes, semiconductor flicker
noise, cosmic microwave background, sunspot cycles...).

The defining property of 1/f noise is that EVERY OCTAVE CARRIES EQUAL POWER:

    PSD(f) = S0 / f  ->  integral over [f, 2f) = S0 ln(2) = constant.

So "octave" is not an arbitrary label; in a 1/f field the octave is the natural
unit because each octave carries exactly the same amount of information. This
is also what "scale invariance" means: 1/f has no characteristic scale, so all
scales coexist on equal footing.

Contrast:
    white (alpha=0) : equal power per Hz  -> octave power DOUBLES each octave
    pink  (alpha=1) : equal power per octave -> octave power FLAT
    red   (alpha=2) : octave power HALVES each octave
"""

from __future__ import annotations

import numpy as np


def generate_noise(n: int, alpha: float, seed: int = 0) -> np.ndarray:
    """Spectral-shaping: power spectrum ~ 1/f^alpha. alpha=1 is pink."""
    rng = np.random.default_rng(seed)
    freqs = np.fft.rfftfreq(n)
    f = freqs[1:].copy()
    phase = rng.uniform(0, 2 * np.pi, size=f.shape)
    spec = np.zeros(len(freqs), dtype=complex)
    spec[1:] = (1.0 / f ** (alpha / 2.0)) * np.exp(1j * phase)
    return np.fft.irfft(spec, n=n).real


def octave_powers(x: np.ndarray) -> np.ndarray:
    """Total power in each octave band [f, 2f), starting at the lowest bin."""
    n = x.shape[0]
    spec = np.abs(np.fft.rfft(x)) ** 2
    freqs = np.fft.rfftfreq(n)
    bands = []
    lo = 1.0 / n                       # lowest non-zero frequency
    n_oct = int(np.log2(n // 2)) - 1
    for _ in range(n_oct):
        hi = lo * 2.0
        mask = (freqs >= lo) & (freqs < hi)
        bands.append(float(spec[mask].sum()))
        lo = hi
    return np.array(bands)


def main() -> None:
    n = 2 ** 16
    print("Octave-band power for three noise colors (n = 2^16)\n")
    print(f"{'color':<16} {'octave powers (first 4)':<38} {'ratio/octave':<14} meaning")
    for alpha, name, meaning in [
        (0.0, "white (1/f^0)", "doubles"),
        (1.0, "pink (1/f)",   "flat"),
        (2.0, "red (1/f^2)",  "halves"),
    ]:
        x = generate_noise(n, alpha, seed=0)
        p = octave_powers(x)
        ratio = p[1:4].mean() / p[0:4].mean() if p[0] != 0 else np.nan
        # ratio of consecutive octave powers (should be ~2, ~1, ~0.5)
        consec = p[1:] / p[:-1]
        print(f"{name:<16} {np.round(p[:4], 4)}   {consec[:3].mean():<14.3f} {meaning}")

    print("\n  -> ONLY pink (1/f) has flat octave power: every octave carries")
    print("     equal information. That is the precise meaning of 'octaves as")
    print("     dimensionally stable sizes of information transfer'.")
    print("  -> 1/f is scale-invariant: no scale is privileged, so all scales")
    print("     coexist. Higher frequency = faster, lower amplitude (less power).")


if __name__ == "__main__":
    main()
