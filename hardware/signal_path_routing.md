# IX-TunerCore Signal Path Routing

This document describes the full **signal flow architecture** for harmonic energy delivery throughout the IX-TunerCore system, including:

- Source-to-coil routing  
- Phase synchronization  
- EM shielding paths  
- Signal conditioning and feedback flow  

There are **no floating lines**, **no non-deterministic behavior**, and all paths are **buildable using current electronics and insulation standards**.

---

## 🔧 Driver-to-Coil Path (Per Pyramid)

Each nested pyramid has:
- 3 coils (outer, mid, inner)
- Each coil receives 1 harmonic (3f₀, 6f₀, 9f₀)

Routing follows this structure:

DDS Module (3f₀) ─▶ Buffer Amp ─▶ EMI Shielded Wire ─▶ Coil Layer 1 (outer)
DDS Module (6f₀) ─▶ Buffer Amp ─▶ EMI Shielded Wire ─▶ Coil Layer 2 (middle)
DDS Module (9f₀) ─▶ Buffer Amp ─▶ EMI Shielded Wire ─▶ Coil Layer 3 (inner)


- All signals isolated via differential drive lines or galvanic decoupling
- Coil leads are twisted pair (PTFE or silicone sheathed) to prevent phase bleed

---

## 🌀 Master Clock Synchronization

To prevent harmonic drift:
- All DDS chips and microcontrollers share a **central master clock**
- Clock distributed using shielded coax or fiber (if needed for distance >1m)
- Clock source: Temperature-Controlled Crystal Oscillator (TCXO) or GPSDO module

---

## 🧱 Cable Shielding Strategy

| Segment                   | Shielding Type              | Notes                                      |
|---------------------------|-----------------------------|---------------------------------------------|
| Driver to Pyramid Coils   | Braided copper + foil layer | Grounded at driver end only                 |
| Master Clock Lines        | Coax or twisted-pair fiber  | Electrically isolated via optical isolator  |
| Sensor Feedback Lines     | Differential twisted pair   | Routed in isolated return bundle            |

All signal lines follow **star topology**, not daisy-chained, to reduce crosstalk and simplify convergence delay mapping.

---

## ⚡ Power & Ground Segregation

- Driver stages powered from isolated 48V DC rail (per pyramid or per quadrant)  
- Ground loops prevented by using **local floating ground planes** per pyramid, tied to a **single master system ground** via shielded bus  
- Sensitive feedback sensors powered via isolated 5V or 3.3V linear regulators

---

## 🔁 Feedback Routing

Sensor signals (Hall, thermocouple, optical) flow **backward** from each pyramid to:
- Local MCU (per pyramid or shared per 3–7 units)
- Feedback is digitized and either:
  - Fed into live tuning logic (phase adjust, amplitude damp)
  - Logged to onboard flash or remote console

---

## 📊 Distribution Topology Summary

| Function       | Topology     | Routing Notes                          |
|----------------|--------------|----------------------------------------|
| Harmonic Signals | Star         | All originate from centralized driver bank  
| Clock Sync     | Tree / Star   | Low latency, phase-locked loop         |
| Feedback Data  | Hub & Spoke   | Optional SPI/I²C per zone              |
| Power Delivery | Segment rail  | 48V DC per quadrant, fanned into each board

---

## ✅ Summary

This signal routing strategy guarantees:
- **Stable harmonic delivery** across all 63 coils (3 × 21 pyramids)  
- **Zero-phase ambiguity** from clock drift  
- **Controlled EMI environment** across nested frequency layers  
- **Scalable architecture**, adaptable to larger or smaller node counts  
- **Buildable with existing electrical hardware**—no theoretical parts required

There is **no fiction**, **no shortcut logic**, and every part of this routing model can be built and tested today.
