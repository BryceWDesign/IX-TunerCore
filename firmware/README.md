# IX-TunerCore Firmware

This firmware powers each pyramid node’s scalar harmonic field via a 3-6-9 modulated DDS signal, using real-time feedback from onboard sensors.

---

## 🔌 Supported Microcontrollers
- Arduino Uno
- Arduino Nano (preferred for space-constrained builds)
- ESP32 (with slight adaptation)

---

## 🔋 Required Hardware

| Component           | Description                         | Example Model      |
|--------------------|-------------------------------------|--------------------|
| MCP4725 DAC        | I²C 12-bit DAC for DDS modulation   | Adafruit MCP4725   |
| ADS1115 ADC        | Precision ADC for sensor input      | Adafruit ADS1115   |
| Hall Sensor        | Magnetic field input                | A1324 / SS49E      |
| RTD Sensor         | Temperature (100 Ω platinum type)   | Pt100 RTD          |
| Photodiode         | Scalar light response               | BPW34 / SFH203     |

---

## ⚙️ Pinout Guide

| Signal         | Arduino Pin   | Notes                          |
|----------------|---------------|--------------------------------|
| DDS Output     | D9            | PWM to analog output line      |
| I²C SDA        | A4 (Uno/Nano) | DAC + ADC                      |
| I²C SCL        | A5 (Uno/Nano) | DAC + ADC                      |
| Hall Sensor    | A0            | ADS1115 Channel 0              |
| RTD Sensor     | A1            | ADS1115 Channel 1              |
| Photodiode     | A2            | ADS1115 Channel 2              |

---

## 🚀 Setup Instructions

1. Install required libraries:
    ```bash
    Arduino IDE → Library Manager:
    - Adafruit MCP4725
    - Adafruit ADS1X15
    ```

2. Wire the components according to the table above

3. Upload `tuner_firmware.ino` via Arduino IDE

4. Monitor serial output @ `115200 baud` for:
    ```
    T:25.3 | M:0.0027 | L:0.763 | DDS:2674.12
    ```

---

## 📈 Real-Time Feedback Loop
The firmware:
- Samples all three sensors at 10 Hz
- Calculates live scalar convergence based on phase-aligned wave superposition
- Adjusts DDS voltage to compensate for phase drift using 3×ω, 6×ω, 9×ω sine overlap
- Maintains harmonic lock across 21 pyramids in array

---

## 🧠 Core Design Logic
This system is structured according to Tesla's 3-6-9 principle and scalar harmonic modulation theory. The firmware is **not a waveform generator** — it is a **closed-loop field tuner**.

---

## 📎 License
This firmware is licensed under the IX Open Harmonic Field License v1.0 (see `/LICENSE`).

