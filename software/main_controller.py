#!/usr/bin/env python3
"""
main_controller.py

IX-TunerCore Core Driver Script
Manages harmonic signal output, phase synchronization, and system monitoring.

Author: Bryce Wooster
License: Custom Legal License (see LICENSE file)
"""

import time
import threading
from hardware.dsp_driver import HarmonicDDS
from hardware.sensor_interface import SensorArray
from utils.logger import Logger
from utils.phase_control import PhaseSynchronizer

# --- Configuration Parameters ---
BASE_FREQ = 432.0  # Hz
FREQ_MULTIPLIERS = [3, 6, 9]
PYRAMID_COUNT = 21
COILS_PER_PYRAMID = 3

# --- System Objects ---
logger = Logger("ix_tunercore.log")
dds = HarmonicDDS()
sensors = SensorArray()
phase_sync = PhaseSynchronizer()

# --- Harmonic Output Routine ---
def start_harmonic_drivers():
    logger.info("Starting harmonic signal generation...")
    for pyramid_id in range(PYRAMID_COUNT):
        for i, multiplier in enumerate(FREQ_MULTIPLIERS):
            freq = BASE_FREQ * multiplier
            coil_id = pyramid_id * COILS_PER_PYRAMID + i
            dds.set_frequency(coil_id, freq)
            dds.set_phase(coil_id, 0.0)
            dds.enable_output(coil_id)
            logger.debug(f"Pyramid {pyramid_id+1} | Coil {i+1} set to {freq:.2f} Hz")

# --- Feedback Monitoring Loop ---
def monitor_feedback_loop():
    logger.info("Starting feedback monitoring...")
    while True:
        data = sensors.read_all()
        drift_values = phase_sync.analyze(data)
        if drift_values:
            for coil_id, phase_adj in drift_values.items():
                dds.adjust_phase(coil_id, phase_adj)
                logger.debug(f"Phase corrected on coil {coil_id}: Δφ = {phase_adj:.3f}°")
        time.sleep(0.5)

# --- Main Execution ---
if __name__ == "__main__":
    logger.info("IX-TunerCore Control System Booting...")
    try:
        start_harmonic_drivers()
        monitor_thread = threading.Thread(target=monitor_feedback_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        logger.info("System running. Press Ctrl+C to terminate.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.warning("Shutdown signal received. Disabling all outputs...")
        dds.disable_all()
        logger.info("System safely shut down.")
