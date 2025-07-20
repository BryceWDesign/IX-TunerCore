"""
gui_controller.py

IX-TunerCore Control Interface
Provides real-time GUI to visualize and adjust harmonic signals, sensor feedback, and scalar phase lock status.

Author: Bryce Wooster
License: Custom Legal License (see LICENSE file)
"""

import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
import random

class IXTunerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IX-TunerCore Harmonic Monitor")
        self.root.geometry("800x600")

        self.freq_labels = []
        self.sensor_frames = []
        self.status_text = tk.StringVar(value="System Initializing...")

        self._build_layout()
        self._start_update_loop()

    def _build_layout(self):
        # Header
        header = ttk.Label(self.root, text="IX-TunerCore Dashboard", font=("Arial", 20))
        header.pack(pady=10)

        # Frequency status
        freq_frame = ttk.LabelFrame(self.root, text="Harmonic Frequencies (Hz)")
        freq_frame.pack(fill="x", padx=10, pady=5)

        for i in range(3):
            label = ttk.Label(freq_frame, text=f"f{i+1}: ??? Hz", width=25)
            label.pack(side="left", padx=10, pady=5)
            self.freq_labels.append(label)

        # Sensor values
        sensor_frame = ttk.LabelFrame(self.root, text="Sensor Averages")
        sensor_frame.pack(fill="x", padx=10, pady=5)

        self.temp_label = ttk.Label(sensor_frame, text="Temp: ??? °C", width=25)
        self.hall_label = ttk.Label(sensor_frame, text="Hall: ??? T", width=25)
        self.optical_label = ttk.Label(sensor_frame, text="Optical: ??? V", width=25)

        self.temp_label.pack(side="left", padx=10, pady=5)
        self.hall_label.pack(side="left", padx=10, pady=5)
        self.optical_label.pack(side="left", padx=10, pady=5)

        # Status bar
        status_bar = ttk.Label(self.root, textvariable=self.status_text, relief="sunken", anchor="w")
        status_bar.pack(fill="x", side="bottom")

    def _start_update_loop(self):
        def update():
            while True:
                # Placeholder updates — integrate with real data hooks
                self.freq_labels[0]["text"] = f"f₃: {round(432 * 3, 2)} Hz"
                self.freq_labels[1]["text"] = f"f₆: {round(432 * 6, 2)} Hz"
                self.freq_labels[2]["text"] = f"f₉: {round(432 * 9, 2)} Hz"

                self.temp_label["text"] = f"Temp: {round(25 + random.uniform(-1, 1), 2)} °C"
                self.hall_label["text"] = f"Hall: {round(random.uniform(-0.05, 0.05), 4)} T"
                self.optical_label["text"] = f"Optical: {round(random.uniform(0.65, 0.85), 3)} V"

                self.status_text.set("Phase Lock: Stable")
                time.sleep(1)

        Thread(target=update, daemon=True).start()

# Standalone run
if __name__ == "__main__":
    root = tk.Tk()
    app = IXTunerGUI(root)
    root.mainloop()
