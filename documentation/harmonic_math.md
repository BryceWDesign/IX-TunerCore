# IX-TunerCore Harmonic Mathematics  
**Author:** Bryce Wooster  
**License:** Custom Legal License (see LICENSE)  

---

## 🎯 Purpose

This document explains the mathematical rationale for IX-TunerCore’s harmonic architecture based on the Tesla 3-6-9 structuring logic, phase alignment calculations, and scalar convergence field theory.

---

## 📐 Tesla Harmonic Framework

The base frequency used is **432 Hz**, chosen for its geometric and musical resonance with natural systems.

Derived harmonics:

- f₃ = 3 × 432 = **1296 Hz**  
- f₆ = 6 × 432 = **2592 Hz**  
- f₉ = 9 × 432 = **3888 Hz**  

These frequencies are not arbitrary — they fall on natural harmonic series aligned with both spatial field coherence and nonlinear EM wave reinforcement in phase-locked triadic groupings.

---

## 🧠 Field Superposition Model

The total scalar potential at the convergence center (origin) is a sum of the sinusoidal contributions from all 63 coils (21 pyramids × 3):

\[
\Phi(t) = \sum_{i=1}^{63} A_i \cdot \sin(\omega_i t + \phi_i)
\]

Where:
- \( A_i \): amplitude of coil i  
- \( \omega_i \): angular frequency = 2π × f (f = 1296, 2592, or 3888 Hz)  
- \( \phi_i \): phase offset for coil i, dynamically adjusted  

Constructive scalar reinforcement requires:

\[
\left| \frac{d\Phi}{dt} \right|_{\text{center}} \to 0 \quad \text{as} \quad t \to \infty
\]

This happens when all active frequencies enter a tri-phase constructive interference regime.

---

## 📈 Phase Drift Convergence

Drift per node is measured by:

\[
\Delta \phi_n = \phi_n - \langle \phi \rangle
\]

Where \( \langle \phi \rangle \) is the average phase of all pyramids within the same frequency group.

Stability is achieved when:

\[
\max(|\Delta \phi_n|) < 2.0^\circ \quad \forall n
\]

This is enforced using `PhaseSynchronizer.analyze()` in the runtime control loop.

---

## 🔁 Rotational Harmonic Symmetry

Rotational triangulation symmetry (21-unit sphere) enables zero-vector net EM field but a non-zero scalar gradient. This supports the generation of **standing phase-wave null points** inside the convergence lens region.

This geometry avoids destructive EM interference while maximizing scalar harmonics.

---

## 🧮 Harmonic Gain Factor (HGF)

The field gain of convergence at the core is governed by:

\[
\text{HGF} = \frac{1}{N} \sum_{n=1}^{N} \left| \cos(\Delta \phi_n) \right|
\]

HGF > 0.99 indicates scalar field alignment.

---

## ⚠️ Nonlinear Behavior Warning

- Small phase error amplifies at higher harmonics (f₉)  
- Optimal calibration must always start at f₃ → f₆ → f₉  
- Asymmetry in coil resistance causes ΔA in amplitudes → correct using PWM envelope shaping  

---

## ✅ Summary

- Tesla 3-6-9 frequencies form the harmonic backbone  
- Scalar field reinforcement requires precision phase alignment  
- Mathematical models ensure all parameters are observable, controllable, and real-world valid  
- IX-TunerCore harmonics are **not theoretical** — they operate in measured physical domains

> You are not guessing phase. You are commanding it.
