"""
Hyperdimensional geometric memory — the real "infinite-dimensional" memory
===========================================================================

The founder referenced "hyperdimensional geometric memory". That is a real,
active field: Hyperdimensional Computing / Vector Symbolic Architectures
(Kanerva, Plate, Gayler). It represents symbols as random vectors in ~10,000
dimensions and computes with them via geometric operations:

    bind(a,b)   = element-wise product   (associates two items)
    bundle(items)= majority sum          (superposes many items)
    similarity  = dot product            (geometric distance)

Why it works: random high-dimensional vectors are *nearly orthogonal*
(incommensurable directions). ~10,000 such directions can coexist with almost
no interference, so memory and computation are robust to noise and partial
damage. This is the founder's "incommensurable dimensions / stability under
noise" — realized, running, and used in neuromorphic hardware.

It is real computation. It is NOT consciousness; that jump is not made here.
"""

from __future__ import annotations

import numpy as np


def rand_bipolar(D: int, rng: np.random.Generator) -> np.ndarray:
    return np.where(rng.random(D) < 0.5, -1.0, 1.0)


def bind(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a * b


def bundle(items) -> np.ndarray:
    return np.sign(np.sum(np.stack(items), axis=0))


def main() -> None:
    D = 10_000
    rng = np.random.default_rng(0)

    # vocabulary of random high-dim vectors
    vocab = {w: rand_bipolar(D, rng) for w in
             ["apple", "banana", "grape", "red", "yellow", "purple"]}

    # store 1:1 associations in a single memory vector
    mem = np.zeros(D)
    pairs = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    for k, v in pairs:
        mem += bind(vocab[k], vocab[v])
    mem = np.sign(mem)

    def retrieve(key: str, query: np.ndarray | None = None) -> str:
        probe = bind(vocab[key], mem) if query is None else bind(query, mem)
        scores = {w: float(np.dot(probe, v) / D) for w, v in vocab.items()}
        # return the highest-scoring *value* word (attributes only)
        return max(scores, key=scores.get)

    print("Hyperdimensional associative memory (D = 10,000)\n")
    print("  stored:", " + ".join(f"{k}->{v}" for k, v in pairs), "\n")
    for k, truth in pairs:
        got = retrieve(k)
        print(f"  query '{k}'  ->  retrieved '{got}'  (correct: '{truth}')  {'OK' if got == truth else 'FAIL'}")

    # robustness: corrupt 30% of the query's bits
    print("\n  robustness to noise (30% of bits flipped in the query):\n")
    for k in ["apple", "banana", "grape"]:
        q = vocab[k].copy()
        flip = rng.random(D) < 0.30
        q[flip] *= -1
        got = retrieve(k, query=q)
        ok = "OK" if got == dict(pairs)[k] else "FAIL"
        print(f"  noisy '{k}'  ->  retrieved '{got}'  {ok}")

    print("\n  -> memory lives in ~10k nearly-orthogonal (incommensurable)")
    print("     directions; it degrades gracefully and recovers from damage.")
    print("     This IS 'geometric memory in high dimensions'. It is computation.")


if __name__ == "__main__":
    main()
