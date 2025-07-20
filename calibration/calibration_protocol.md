# IX-TunerCore Calibration Protocol  
**Author:** Bryce Wooster  
**License:** Custom Legal License (see LICENSE)  
**Target Audience:** Field engineers, system integrators, and phase alignment specialists  

---

## Overview  
This protocol outlines the required steps for initial calibration of the IX-TunerCore system, including harmonic phase alignment, scalar convergence tuning, and environmental baseline locking.

---

## 1. Hardware Pre-Check

- ✅ Verify all 63 DDS channels are functional and controllable (21 pyramids × 3 coils)
- ✅ Confirm thermocouples, Hall sensors, and optical pickups are connected and readable
- ✅ Ensure GUI and Logger modules initialize without errors

---

## 2. Base Harmonic Verification

- Set the primary frequency base to **432.00 Hz**
- Confirm output on each DDS driver at:
  - f₃ = 1296 Hz
  - f₆ = 2592 Hz
  - f₉ = 3888 Hz  
- Use oscilloscope or frequency counter to verify ±0.5 Hz tolerance

---

## 3. Phase Coherence Initialization

- Set all coil phases to **0.0°**
- Monitor Hall sensors while system is at idle state
- Use the Logger and Graph GUI to observe baseline drift
- Adjust each coil cluster using `PhaseSynchronizer.analyze()` if |drift| > 3.0°

---

## 4. Sensor Baseline Calibration

- Average all 21 temperature sensors; baseline should read 24.5°C–25.5°C
- Hall readings should be < ±0.02 T
- Optical pickup baseline must stay between 0.70–0.80 V under idle harmonic load

---

## 5. Scalar Lock Tuning

1. Activate full harmonic sequence (f₃, f₆, f₉) across all 21 pyramid groups  
2. Observe scalar lock indicator (status bar on GUI)  
3. If "Phase Lock: Unstable", run real-time phase correction loop for 3 minutes  
4. Wait for all phase drift plots to fall below ±2.0° in `graph_generator.py`

---

## 6. Convergence Snapshot

- After stable lock, take screenshots of all 3 system graphs  
- Log output should contain:
  - `[INFO] Phase convergence within tolerance`
  - `[DEBUG] Phase corrected on coil... Δφ = ...°`
- Archive log and graphs to `/logs/calibration_snapshots/YYYYMMDD-HHMM/`

---

## 7. Final Lock Test

- Disable outputs for 30 seconds
- Re-enable harmonic sequence  
- System must regain lock within 5 seconds  
- GUI status must return to “Phase Lock: Stable”

---

## Notes  

- Repeat full calibration any time hardware is relocated, rewired, or after ≥5°C ambient temp change  
- Optional: export drift coefficients to `.csv` using `Logger` subclass extension  
- For extreme applications, repeat test with all pyramid tips focused to spherical convergence lens center

---

**Status:** This protocol is complete and field-valid.
