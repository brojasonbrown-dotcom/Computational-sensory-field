# Research note: emergent time, relational measurement, and spacetime-from-information

**Target ideas being mapped** (from the RHUFT brief):
- **T1 — "time is emergent off measurement"**: time is not fundamental but arises from the
  act/relational character of measurement.
- **T2 — "measurement = density of spacetime"**: the density of spacetime geometry is, in some
  sense, constituted by measurement.

**Status tags** follow the project convention: `[E]` established/measured, `[A]` active research,
`[S]` speculative, `[N]` non-physical. Every claim carries a source URL. Where the target idea is a
loose paraphrase of published work (not a verbatim quote), that is flagged rather than dressed up.

---

## Summary table

| # | Idea | Core claim | Status | Experimentally testable? | Alignment with target ideas |
|---|------|-----------|--------|--------------------------|-----------------------------|
| 1 | Relational QM (Rovelli 1996) | Observables/values exist only **relative to an interacting system**; physics describes the information systems have about each other. | `[A]` (foundational interpretation; consistent with all experiments but not uniquely selected) | Partially — via extended Wigner's-friend / observer-independence tests | Strong with **T1** (measurement = relational event). Weak/no direct link to **T2**. |
| 2a | Page–Wootters mechanism (1983) | Time emerges as a **correlation between a clock subsystem and the rest**, even when the total state is stationary. | `[A]` (model; proof-of-principle experiment done) | Yes — demonstrated with entangled photons (2014) | Strong with **T1** (time from internal correlations, not measurement per se). |
| 2b | Wheeler–DeWitt "frozen time" | Canonical QG has no external time parameter; the universe's wavefunction is stationary (`ĤΨ=0`). | `[E]` as a *mathematical feature* of the formalism; its interpretation is `[A]` | Not directly; it is a formal result | Strong with **T1** (motivates why time must be emergent). |
| 2c | Connes–Rovelli thermal time | Time-flow = the modular (Tomita–Takesaki) automorphism determined by a **thermodynamic state**. | `[S]` (elegant, mathematically grounded, no empirical confirmation) | Not yet; no decisive experiment | Strong with **T1** (time from state/statistics). |
| 3 | Decoherence + einselection (Zurek) | Environment "measures" the system; pointer states are selected; objectivity (quantum Darwinism) arises **without a collapse postulate**. | Decoherence `[E]`; einselection `[A]`→`[E]`; quantum Darwinism `[A]` | Yes — decoherence is routinely measured; Darwinism has proof-of-principle tests | Strong with **T1** ("measurement" demoted to ordinary physical interaction). Indirect with **T2** (information redundancy, not spacetime density). |
| 4 | Spacetime from entanglement | Entanglement entropy of a region = minimal surface area/4G; disentangling pinches spacetime apart; ER bridges = EPR entanglement. | Ryu–Takayanagi `[E]` *within AdS/CFT* (which is itself `[A]`); Van Raamsdonk `[S]`→`[A]`; ER=EPR `[S]` | Computationally (CFT matches); **no** laboratory test of AdS/CFT or ER=EPR | Strong with **T2** (geometry ↔ quantum information/entanglement). Not "measurement" = density, but "entanglement" = connectivity. |
| 5 | Entropic/emergent gravity (Verlinde 2011) | Gravity is an **entropic force** from information on holographic screens; dark matter may be emergent. | `[S]` and **contested** (formal criticisms + mixed data) | Partially — weak-lensing and dwarf-galaxy tests give conflicting verdicts | Strong with **T2** (spacetime/inertia from information density), but the physics is disputed. |
| 6 | Concrete tests / proposals | Atom-interferometer "clock" visibility loss; Page–Wootters optics demo; mm-scale redshift; gravity-induced-entanglement witnesses. | Mix of `[E]` (realized) and `[A]` (proposals) | Yes, several realized | These are the *falsifiable hooks* for T1/T2 — they test the ingredients, not the full synthesis. |

---

## 1. Relational Quantum Mechanics (Rovelli 1996)

**What it claims.** Rovelli's 1996 paper proposes that the "measurement problem" arises from a wrong
assumption — that a system has an **observer-independent state** (or observer-independent values of
physical quantities). His replacement: a variable of system S takes a value only **relative to the
system S′ it interacts with**; the theory is complete and describes "only the information that
systems have about each other," with no fundamental observer/observed split
([arXiv abstract](https://arxiv.org/abs/quant-ph/9609002)).

The Stanford Encyclopedia of Philosophy's entry on RQM makes the relational claim precise: values of
physical variables are not absolute but are labeled by a second physical system, and "different
observers can give different accounts of the same set of events"
([SEP: Relational Quantum Mechanics](https://plato.stanford.edu/entries/qm-relational/)).

**Note on the quoted phrase.** The brief quotes Rovelli's view as "the world is a network of mutual
measurements." That is a **paraphrase, not a verbatim quotation** from the 1996 paper. The 1996
abstract's actual wording is that the theory "describes only the information that systems have about
each other." Rovelli's later popular writing uses the closely related "web of relations" imagery, but
the phrase as quoted should be treated as the RHUFT framework's gloss, not a citation.

**Status.** `[A]` — a live, well-cited foundational interpretation. It reproduces all quantum
predictions, but it is one of several empirically equivalent interpretations, so it is not uniquely
selected by data ([SEP RQM](https://plato.stanford.edu/entries/qm-relational/)).

**Testability.** Partially. RQM's "facts are relative" reading has been probed by *extended
Wigner's-friend* experiments that ask whether different observers can disagree about a measurement
outcome while remaining consistent; the SEP entry discusses these and the ongoing debate over
"perspectivalism" ([SEP RQM §sections on observers/friends](https://plato.stanford.edu/entries/qm-relational/)).

**Alignment.** Strongly supports **T1** at the conceptual level: "measurement" is demoted from a
special act to a generic physical interaction, and events/values exist only relative to that
interaction. It does **not** connect measurement to spacetime density (**T2**); RQM says nothing about
geometry.

---

## 2. Emergent / relational time

### 2a. Page–Wootters mechanism (1983)
**Claim.** In a closed system whose total state is **stationary** (as the Wheeler–DeWitt equation
demands for the universe), the state of one part conditioned on the reading of a "clock" subsystem
undergoes exactly the Schrödinger evolution an external observer would describe with a time parameter
— "evolution without evolution" ([Wikipedia: Time in physics, quantum section](https://en.wikipedia.org/wiki/Time_in_physics);
primary ref: Page & Wootters 1983, Phys. Rev. D 27, 2885,
[doi:10.1103/PhysRevD.27.2885](https://doi.org/10.1103/PhysRevD.27.2885)).

**Status.** `[A]` — a well-developed model with a proof-of-principle experiment (see §6).

**Testability.** Yes — see Moreva et al. 2014 in §6.

### 2b. Wheeler–DeWitt "frozen time"
**Claim.** Canonical quantization of general relativity yields the Hamiltonian constraint `ĤΨ = 0`,
so the total wavefunction is time-independent — there is no external time parameter in the
fundamental formalism. This is the source of the "problem of time" in quantum gravity.
([Wikipedia: Time in physics](https://en.wikipedia.org/wiki/Time_in_physics)
explicitly ties the Page–Wootters setup to the stationary state "required by the Wheeler–DeWitt
equation"; see also the Connes–Rovelli abstract below, which calls this the "timelessness" of a
fundamental covariant theory.)

**Status.** `[E]` as a formal/mathematical fact of the canonical formalism; `[A]` as an open
interpretational problem.

**Testability.** Not directly; it is a structural feature of the equations, not a prediction about a
particular observable.

### 2c. Connes–Rovelli thermal time hypothesis (1994)
**Claim.** In a generally covariant quantum theory, physical time-flow is **not** a universal
property of the theory but is "determined by the thermodynamical state of the system" — the
**thermal time hypothesis**. Technically: via the Tomita–Takesaki theorem, any faithful thermal state
of a von Neumann algebra determines a one-parameter group of automorphisms (a time-flow); the authors
relate this flow to the Unruh temperature and Hawking radiation
([arXiv:gr-qc/9406019](https://arxiv.org/abs/gr-qc/9406019);
Class. Quantum Grav. 11 (1994) 2899, [doi:10.1088/0264-9381/11/12/007](https://doi.org/10.1088/0264-9381/11/12/007)).

**Status.** `[S]` — a mathematically rigorous and influential proposal, but with **no empirical
confirmation** and no decisive experiment proposed to date.

**Alignment (all of §2).** These three are the strongest real-physics anchors for **T1** ("time is
emergent"). Importantly, the emergence is from **correlations / thermodynamic state / constraints**,
not from "measurement" in the colloquial sense — the Page–Wootters clock is a correlation, and
thermal time is a statistical-state property. None of them links time to spacetime density (**T2**).

---

## 3. Decoherence, einselection, quantum Darwinism (Zurek)

**Claim.** The environment continuously "monitors" certain observables of a system, destroying
interference between the corresponding eigenstates (decoherence) and singling out **pointer states**
that survive monitoring — **environment-induced superselection, or einselection**. Classicality
emerges from this, and — via **quantum Darwinism** — only states that are redundantly imprinted in
many fragments of the environment become "objective" records, effectively reproducing measurement
outcomes and even Born-rule probabilities **without any collapse postulate**
([Zurek, RMP 2003](https://arxiv.org/abs/quant-ph/0105127),
[doi:10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715);
[Zurek, Physics Today "revisited"](https://arxiv.org/abs/quant-ph/0306072);
[Quantum Darwinism review, Nature Physics 2009](https://arxiv.org/abs/0903.5082),
[doi:10.1038/nphys1202](https://doi.org/10.1038/nphys1202)).

**Status.** Decoherence itself is `[E]` (extensively measured in the lab). Einselection is
`[A]`→`[E]` (firm theoretical framework, tested). Quantum Darwinism is `[A]` (theoretical framework
with proof-of-principle experimental demonstrations under way)
([quant-ph/0306072](https://arxiv.org/abs/quant-ph/0306072),
[0903.5082](https://arxiv.org/abs/0903.5082)).

**Testability.** Yes — decoherence rates and pointer-state structure are directly measurable;
Darwinism's redundant-record signature is testable in multi-partite environments.

**Alignment.** Strong with **T1**: "measurement" is shown to be an ordinary, distributed physical
process (environment-as-monitor), not a special collapse. It gives a concrete mechanism for how
"information" (the raw material of measurement) becomes objective. It is only **indirectly** relevant
to **T2** — it explains information redundancy, not spacetime geometry.

---

## 4. Spacetime from entanglement

**Claims.**
- **Ryu–Takayanagi (2006):** holographic entanglement entropy of a boundary region equals the area of
  a minimal surface in the bulk divided by `4G` (`S = A/4G`) — a direct, quantitative
  entanglement↔geometry dictionary
  ([arXiv:hep-th/0603001](https://arxiv.org/abs/hep-th/0603001),
  PRL 96, 181602, [doi:10.1103/PhysRevLett.96.181602](https://doi.org/10.1103/PhysRevLett.96.181602)).
- **Van Raamsdonk (2010):** if you **disentangle** degrees of freedom associated with two regions, the
  regions pull apart and pinch off — "emergence of classically connected spacetimes is intimately
  related to the quantum entanglement" ([arXiv:1005.3035](https://arxiv.org/abs/1005.3035),
  Gen. Rel. Grav. 42, 2323, [doi:10.1007/s10714-010-1034-0](https://doi.org/10.1007/s10714-010-1034-0)).
- **ER = EPR (Maldacena–Susskind 2013):** an Einstein–Rosen bridge (wormhole) connecting two black
  holes can be interpreted as a maximally entangled EPR pair of black holes; they conjecture the
  correspondence holds for more general entangled states
  ([arXiv:1306.0533](https://arxiv.org/abs/1306.0533),
  Fortsch. Phys. 61, 781, [doi:10.1002/prop.201300020](https://doi.org/10.1002/prop.201300020)).

These all live on top of the **AdS/CFT correspondence** (Maldacena 1997), which is itself a
conjecture, though an exceptionally well-tested one *computationally*
([arXiv:hep-th/9711200](https://arxiv.org/abs/hep-th/9711200)).

**Status.**
- RT formula: `[E]` *within AdS/CFT* — a proven result of the holographic framework (and generalized
  by Lewkowycz–Maldacena), but resting on the unproven-in-nature AdS/CFT conjecture.
- Van Raamsdonk: `[S]`→`[A]` — an influential argument/essay, not an established theorem; it is the
  flagship intuition for "geometry from entanglement."
- ER=EPR: `[S]` — a conjecture, not established.

**Testability.** Computational only (e.g., RT matches CFT replica-trick calculations). There is **no
laboratory test** of AdS/CFT or ER=EPR; the black-hole/bulk systems involved are not experimentally
accessible. Honest bottom line: this is mathematically rich but empirically unverified physics.

**Alignment.** This is the strongest real anchor for **T2**, but with a crucial correction: what
builds spacetime in this program is **entanglement entropy / quantum information**, not "measurement"
as an event. "Density of spacetime" maps naturally onto "amount of entanglement across a cut"
(area-law). "Measurement = density of spacetime" would need the further — currently unsupported —
step of identifying measurement with entanglement structure.

---

## 5. Entropic / emergent gravity (Verlinde 2011) — contested

**Claim.** Verlinde derives Newton's law (and argues Einstein's equations follow) by treating gravity
as an **entropic force** caused by "changes in the information associated with the positions of
material bodies," using 't Hooft's holographic principle: information is stored on a boundary screen
at one bit per Planck area, and displacement of a mass changes that information, producing a force
([arXiv:1001.0785](https://arxiv.org/abs/1001.0785),
JHEP 04 (2011) 029, [doi:10.1007/JHEP04(2011)029](https://doi.org/10.1007/JHEP04(2011)029)).
A later version (2016/17) extended this to an "apparent dark matter" explanation for galaxy rotation
curves ([arXiv:1611.02269](https://arxiv.org/abs/1611.02269)).

**Status — contested, and parts are effectively refuted.** This must be stated plainly:
- **Formal criticism.** Matt Visser showed that reproducing *n-body* conservative gravity in a
  Verlinde-like entropic scheme requires "unphysical" entropy requirements and many temperature baths;
  Tower Wang showed modified entropic-gravity models are severely constrained by energy-momentum
  conservation and cosmology; Wang & Braunstein (2018, Nature Communications) showed ordinary
  spacetime surfaces **away from horizons are not thermodynamic**, undermining the program's central
  assumption ([Wikipedia: Entropic gravity — Criticism section](https://en.wikipedia.org/wiki/Entropic_gravity)).
- **Observational tests are mixed.** Weak lensing of ~33,000 galaxies (Brouwer et al. 2017) was
  reported as consistent with Verlinde's emergent gravity, but a study of **isolated dwarf galaxies**
  (Pardo 2017/2020) found emergent gravity predicts rotation velocities far too low for the most
  massive gas-rich dwarfs — "a serious problem" for the theory
  ([Wikipedia: Entropic gravity — Criticism and experimental tests](https://en.wikipedia.org/wiki/Entropic_gravity);
  see also [arXiv:1612.03034](https://arxiv.org/abs/1612.03034) and
  [arXiv:1706.00785](https://arxiv.org/abs/1706.00785)).
- **Quantum-coherence objection.** Kobakhidze argues ultra-cold-neutron gravitational bound states
  (which show clean, coherent Schrödinger levels) **disprove** entropic gravity, since entropic forces
  should decohere; Chaichian et al. propose a loophole for weak fields
  ([arXiv:1009.5414](https://arxiv.org/abs/1009.5414),
  [Wikipedia: Entropic gravity](https://en.wikipedia.org/wiki/Entropic_gravity)).

**Testability.** Earth-bound tests look infeasible (effects too weak); cosmological/astrophysical
tests exist but give conflicting verdicts.

**Alignment.** This is the closest published physics to **T2** ("spacetime/inertia from information
density"): Verlinde literally ties spacetime behavior to information bits and entropy. It is also the
**weakest** of the anchors, because the specific mechanism is widely contested and partly refuted. Any
RHUFT use of entropic gravity must treat it as `[S]` with known counter-evidence, not as established
support.

---

## 6. Concrete experimental proposals / tests

1. **Page–Wootters demonstrated (realized).** Moreva, Brida, Gramegna, Giovannetti, Maccone &
   Genovese (2014) implemented the Page–Wootters mechanism with two entangled photons: an "internal"
   observer correlated with the clock photon sees the second photon evolve, while an "external"
   observer who sees only global properties can prove the total state is static
   ([arXiv:1310.4691](https://arxiv.org/abs/1310.4691), Phys. Rev. A 89, 052122,
   [doi:10.1103/PhysRevA.89.052122](https://doi.org/10.1103/PhysRevA.89.052122)). This is a
   proof-of-principle, not a full dynamical theory of time.

2. **Atom-interferometer "clock" model (proposal).** Zych, Costa, Pikovski & Brukner (2011) propose a
   Mach–Zehnder interferometer whose interfering particle carries an internal "clock." Gravitational
   time dilation between the arms makes which-path information available from the clock, reducing
   interference **visibility** — an unambiguous probe of general-relativistic **proper time**, cleanly
   separated from the Aharonov–Bohm phase interpretation of gravitationally induced phase shifts
   ([Nature Communications 2, 505](https://www.nature.com/articles/ncomms1498),
   [doi:10.1038/ncomms1498](https://doi.org/10.1038/ncomms1498)). Status: `[A]` proposal; requires
   large atom superpositions not yet achieved.

3. **Millimeter-scale gravitational redshift (realized).** Bothwell et al. (2022) measured a
   gravitational-redshift frequency gradient across a **single millimeter-scale** sample of ultracold
   strontium, at 7.6×10⁻²¹ fractional uncertainty — clocks now resolve spacetime curvature within a
   single atomic cloud ([arXiv:2109.12238](https://arxiv.org/abs/2109.12238),
   Nature 602, 420, [doi:10.1038/s41586-021-04349-7](https://doi.org/10.1038/s41586-021-04349-7)).
   Status: `[E]` (done). Relevance: sharpens the "clocks measure spacetime" ingredient of T1/T2.

4. **Gravity-induced entanglement witnesses (proposals).** Bose et al. (2017) and Marletto–Vedral
   (2017) propose testing whether gravity is a **quantum-coherent mediator** by entangling two
   adjacent matter-wave interferometers through their mutual gravitational interaction
   ([arXiv:1707.06050](https://arxiv.org/abs/1707.06050), PRL 119, 240401,
   [doi:10.1103/PhysRevLett.119.240401](https://doi.org/10.1103/PhysRevLett.119.240401);
   [arXiv:1707.06036](https://arxiv.org/abs/1707.06036)). Status: `[A]` proposals, not yet realized.

5. **AdS/CFT "checks" — honest note.** The RT formula and its generalizations are verified
   *computationally* inside AdS/CFT (CFT entanglement-entropy calculations reproduce the bulk area
   law), but there is **no experimental test** of AdS/CFT, ER=EPR, or any holographic spacetime claim
   in a laboratory ([arXiv:hep-th/0603001](https://arxiv.org/abs/hep-th/0603001),
   [arXiv:1306.0533](https://arxiv.org/abs/1306.0533)). Treat all "AdS/CFT checks" as theoretical
   consistency checks, not empirical confirmation.

---

## Alignment & gaps (mapping real physics → T1 and T2)

**Where the target ideas are anchored in real physics:**
- **T1 ("time is emergent off measurement")** has three genuine anchors: relational QM (values only
  relative to interactions), the Page–Wootters mechanism (time from clock–system correlation), and
  thermal time (time from a thermodynamic state). Decoherence adds the mechanism by which "measurement"
  is just physical interaction. So the *direction* of T1 is well-motivated.
- **T2 ("measurement = density of spacetime")** has a real anchor in the *spacetime-from-entanglement*
  program (RT `S = A/4G`, Van Raamsdonk, ER=EPR) and in *entropic/emergent gravity*. The
  "density of spacetime" half maps cleanly onto "entanglement/information density" (area-law) and
  "information on holographic screens."

**Where the target ideas overreach (must be flagged):**
1. **"Measurement" ≠ "entanglement/information density."** The established physics says spacetime
   geometry is tied to **entanglement entropy and information**, not to "measurement" as an event or
   act. Identifying the two is an additional, currently **unsupported** synthesis — `[S]`, not `[E]`
   or `[A]`. No published research program states "measurement = density of spacetime."
2. **Verbatim caution.** "The world is a network of mutual measurements" is a paraphrase of Rovelli,
   not his words. The actual 1996 claim is that the theory describes "only the information that
   systems have about each other."
3. **Entropic gravity is not safe support.** Verlinde 2011 is `[S]` and contested; Wang–Braunstein and
   the dwarf-galaxy and neutron-coherence results are genuine counter-evidence. RHUFT should not cite
   entropic gravity as confirmation of T2 without carrying this counter-evidence alongside.
4. **No experimental confirmation for the geometry claims.** RT/ER=EPR/Van Raamsdonk are
   mathematically powerful but empirically unverified; AdS/CFT is a conjecture. The genuinely
   *testable* hooks are the modest ones (§6): Page–Wootters optics, clock-in-interferometer visibility,
   mm-scale redshift, and gravity-induced-entanglement witnesses. Those test the *ingredients* of
   T1/T2, not the full "measurement = spacetime density" claim.
5. **Two different meanings of "emergent" are being conflated.** Page–Wootters/thermal time make time
   emergent from *correlations/state* within a fixed Hilbert-space structure; entropic/holographic
   gravity makes *spacetime geometry* emergent from *microscopic degrees of freedom*. These are
   different programs, and T1+T2 implicitly merges them — that merger is the framework's own
   conjecture and should be labeled `[S]`.

**Bottom line.** T1 is a legitimate, partially tested direction of modern foundational physics. T2 is
half-real (spacetime ↔ information/entanglement) and half-speculative (that this information is
"measurement"). The defensible, sourced version of the framework's target statement is closer to:
*"time and spacetime geometry are emergent from quantum correlations and information, and measurement
is a relational, decoherence-driven information process"* — which is `[A]`/`[S]` territory. The
stronger "measurement = density of spacetime" remains `[S]` and currently without direct support.
