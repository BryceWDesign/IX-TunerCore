# IX-TunerCore Coil Driver Specifications

This document outlines the **engineering specifications and performance targets** for the harmonic field driver system powering each of the 21 nested pyramid units. Each unit requires three independent harmonic signals (3f₀, 6f₀, 9f₀) delivered to concentric coils without phase drift or harmonic bleed.

---

## 🎛️ Harmonic Targets

| Harmonic | Frequency | Use Case                              |
|----------|-----------|----------------------------------------|
| 3f₀      | 1,296 Hz  | Field stability and base structure     |
| 6f₀      | 2,592 Hz  | Lattice entrainment and coupling       |
| 9f₀      | 3,888 Hz  | Scalar convergence, phase collapse     |

*Base frequency f₀ set to 432 Hz; all values programmable*

---

## ⚡ Output Driver Requirements

| Parameter               | Value                              |
|-------------------------|-------------------------------------|
| Signal Type             | Pure sine wave or trapezoidal       |
| Voltage Output (peak)   | 0–24V (lab version)                 |
| Current per channel     | Up to 3 A                           |
| Harmonic isolation      | ≥ 60 dB separation between signals  |
| Phase stability         | ≤ 0.25° drift @ 1 kHz–10 kHz        |
| Modulation capability   | AM/FM/PWM (optional)                |

---

## 🧠 Recommended Driver Architecture

- **Core Chipset**: Analog Devices AD9833 (basic) or AD9106 (advanced multi-tone)
- **Microcontroller**: STM32F405, RP2040, or ESP32 (for waveform logic + feedback loop)
- **Amplifier Stage**: Class AB linear amp with dual H-bridge output or push-pull FET design
- **Isolation**: Galvanic isolation on ground plane and coil interface (transformer-coupled or optoisolator logic)

---

## 🔁 Per-Pyramid Driver Configuration

Each pyramid requires:
- **3 independent harmonic channels**
- **1 signal conditioning buffer per coil**
- **1 monitoring feedback loop (optional)** for EM backscatter or coil temperature

Total coils in system:
- 21 pyramids × 3 coils = 63 driver channels

Deployment Strategy:
- Use **shared signal boards** where possible (1 board per pyramid)
- Synchronize master clock for all driver boards (via TCXO or GPSDO for lab precision)

---

## 🔧 Coil Construction Parameters

| Parameter            | Spec                            |
|----------------------|----------------------------------|
| Core type            | Air-core (preferred), ferrite optional for 3f₀ only  
| Turns (typical)      | 50–120 turns per coil            |
| Wire                 | AWG 22–26 enameled copper        |
| Inductance target    | 100 µH – 800 µH per harmonic     |
| Mounting position    | Concentric layers around pyramid cavities  
| Cooling              | Passive air convection or sink tab to chassis  

---

## 🧪 Tuning & Feedback

Feedback loop options:
- **Hall effect sensor** for current feedback
- **Thermal probe** (NTC) on coil form for duty cycle throttling
- **Back EMF spectral monitor** via differential amplifier for convergence tuning

Optional enhancements:
- Dynamic phase shift modulation for material-specific response
- Harmonic phase ramping (e.g., sweep from 3f₀ to 9f₀ in 500 ms) for scalar ignition triggering

---

## ✅ Summary

These coil drivers form the **active harmonic engine** behind the IX-TunerCore platform. Each channel must deliver clean, isolated, phase-stable energy at precise Tesla 3-6-9 frequencies. The system is **fully buildable** using off-the-shelf signal generators, microcontrollers, and discrete analog components.

There is **zero speculation** in these specs. Everything defined here is reproducible, controllable, and testable using real hardware.
