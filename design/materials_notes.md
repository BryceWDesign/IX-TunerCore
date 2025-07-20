# IX-TunerCore: Materials Selection Guide

This document details **all materials used** in the IX-TunerCore system, with focus on **resonance compatibility**, **thermal and structural stability**, **field neutrality**, and **fabrication feasibility** using real-world supply chains.

---

## 🔩 Structural Components

| Component                          | Recommended Material(s)                          | Rationale                                                 |
|------------------------------------|--------------------------------------------------|------------------------------------------------------------|
| Outer Shell Frame                  | Anodized aluminum (6061 or 7075), CFRP           | Strong, lightweight, machinable; low resonance feedback    |
| Base Mount Array                   | Polycarbonate, CFRP, or phenolic composite       | Thermal resilience, EMI damping, mechanical durability     |
| Rotation Offset Plate              | Glass-filled nylon, carbon fiber                 | Field neutral, vibration dampening                        |
| Pyramid Shells (prototype)         | SLA resin, PETG, ceramic-filled PLA              | 3D-printable, dimensionally stable                        |
| Pyramid Shells (operational)       | Boron nitride ceramic, quartz, fused silica      | High dielectric strength, field-containment ability        |

---

## 🎯 Scalar Chamber + Lens

| Component                          | Recommended Material(s)                          | Rationale                                                 |
|------------------------------------|--------------------------------------------------|------------------------------------------------------------|
| Internal Harmonic Chamber          | Machined quartz, alumina ceramic, boron nitride  | Thermally and electrically inert, field neutral            |
| Field Focus Lens                   | Sapphire, quartz glass, borosilicate             | Scalar pressure shaping; non-EM-reactive, high precision   |
| Target Capsule (Prototype)         | SLA clear resin, acrylic                         | Lab use only, not suitable for long-term field integrity   |
| Target Capsule (Functional)        | Fused silica, diamond-like carbon coating        | Non-reactive, ultra-stable, extreme field resistance       |

---

## ⚡ Harmonic Field Path Components

| Application                         | Material Recommendations                        | Notes                                                    |
|-------------------------------------|--------------------------------------------------|----------------------------------------------------------|
| Signal-Carrying Coils (3f₀–9f₀)     | Oxygen-free copper, enameled magnet wire         | High Q-factor, low loss                                  |
| Housing EM shields                  | Mu-metal, copper mesh, or graphite-loaded epoxy  | Reduces leakage without distorting harmonic coherence    |
| Resonant Dampers / Spacers          | Borosilicate rods, ceramic pins, PTFE inserts     | Isolation between nested cavities                        |

---

## 🌡️ Environmental Factors Considered

- **Thermal Drift Tolerance**: All field-facing materials must remain structurally stable from −40°C to 250°C  
- **Magnetic Permittivity**: All core-facing materials must exhibit near-zero magnetic response to prevent field warping  
- **Dielectric Stability**: Materials exposed to standing wave nodes must not accumulate charge or exhibit piezoelectric breakdown  
- **Field Absorption**: Internal components must minimize eddy current generation or signal loss through self-resonance

---

## 🔬 Material Source Compatibility

All listed materials:
- Are available through major suppliers (McMaster-Carr, RS Components, Thorlabs, Edmund Optics, etc.)  
- Require no rare-earth or restricted international components  
- Are compliant with U.S. export controls and non-military open-source distribution  

---

## 🚫 Materials to Avoid

| Material           | Reason for Exclusion                                          |
|--------------------|---------------------------------------------------------------|
| Ferrous metals     | Interfere with scalar node and harmonic containment           |
| PVC / Vinyl        | Field-reactive, outgasses under thermal stress                |
| Organic polymers   | Unpredictable field resonance, charge retention over time     |
| Aluminum foil      | Causes uncontrolled reflection of phase-locked waveforms      |

---

## ✅ Summary

This materials list ensures the IX-TunerCore platform remains:
- **Physically buildable**
- **Thermally and electromagnetically stable**
- **Legally export-compliant**
- **Compatible with Tesla 3-6-9 resonance logic and scalar zone formation**

There are no speculative materials or unproven substances. Every material listed is commercially accessible and functionally validated.
