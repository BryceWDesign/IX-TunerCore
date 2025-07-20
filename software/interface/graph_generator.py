"""
graph_generator.py

IX-TunerCore Graphing Module
Renders dynamic plots of scalar phase drift, harmonic frequency shifts, and sensor variance.

Author: Bryce Wooster
License: Custom Legal License (see LICENSE file)
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class ScalarPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots(3, 1, figsize=(10, 8))
        self.phase_data = []
        self.freq_data = []
        self.temp_data = []
        self.window_size = 100

    def _simulate_data(self):
        # Replace with real-time data stream in integration phase
        return {
            "phase": random.uniform(-5, 5),
            "freq": random.uniform(1290, 1300),  # near 3*432
            "temp": random.uniform(24.0, 26.0)
        }

    def animate(self, i):
        new_data = self._simulate_data()

        self.phase_data.append(new_data["phase"])
        self.freq_data.append(new_data["freq"])
        self.temp_data.append(new_data["temp"])

        if len(self.phase_data) > self.window_size:
            self.phase_data.pop(0)
            self.freq_data.pop(0)
            self.temp_data.pop(0)

        self.ax[0].clear()
        self.ax[1].clear()
        self.ax[2].clear()

        self.ax[0].plot(self.phase_data, label="Δφ (Phase Drift)", color='orange')
        self.ax[1].plot(self.freq_data, label="f₃ Harmonic (Hz)", color='blue')
        self.ax[2].plot(self.temp_data, label="Temp (°C)", color='red')

        self.ax[0].legend(loc="upper right")
        self.ax[1].legend(loc="upper right")
        self.ax[2].legend(loc="upper right")

        self.ax[0].set_ylabel("Degrees")
        self.ax[1].set_ylabel("Hz")
        self.ax[2].set_ylabel("°C")
        self.ax[2].set_xlabel("Time (frames)")

        self.fig.tight_layout()

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=200)
        plt.show()

# Standalone run
if __name__ == "__main__":
    plotter = ScalarPlotter()
    plotter.run()
