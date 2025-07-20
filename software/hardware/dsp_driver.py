"""
dsp_driver.py

IX-TunerCore Harmonic Driver Module
Provides low-level control for Direct Digital Synthesis (DDS) modules driving harmonic coils.

Author: Bryce Wooster
License: Custom Legal License (see LICENSE file)
"""

import time

class HarmonicDDS:
    def __init__(self, device_count=63):
        # Placeholder for actual hardware initialization
        self.device_count = device_count
        self.freqs = [0.0] * device_count
        self.phases = [0.0] * device_count
        self.outputs_enabled = [False] * device_count

    def set_frequency(self, channel: int, freq_hz: float):
        if 0 <= channel < self.device_count:
            # Replace with actual DDS library command
            self.freqs[channel] = freq_hz
            print(f"[DDS] Set frequency on channel {channel}: {freq_hz:.2f} Hz")

    def set_phase(self, channel: int, phase_deg: float):
        if 0 <= channel < self.device_count:
            self.phases[channel] = phase_deg
            # Replace with actual DDS hardware write here
            print(f"[DDS] Set phase on channel {channel}: {phase_deg:.2f}°")

    def enable_output(self, channel: int):
        if 0 <= channel < self.device_count:
            self.outputs_enabled[channel] = True
            print(f"[DDS] Enabled output on channel {channel}")

    def disable_output(self, channel: int):
        if 0 <= channel < self.device_count:
            self.outputs_enabled[channel] = False
            print(f"[DDS] Disabled output on channel {channel}")

    def adjust_phase(self, channel: int, delta_phase: float):
        if 0 <= channel < self.device_count:
            new_phase = (self.phases[channel] + delta_phase) % 360
            self.set_phase(channel, new_phase)
            print(f"[DDS] Adjusted phase on channel {channel}: Δφ = {delta_phase:.2f}°")

    def disable_all(self):
        for ch in range(self.device_count):
            self.disable_output(ch)
        print("[DDS] All outputs disabled.")
