"""
logger.py

IX-TunerCore Logging Module
Lightweight utility for timestamped logging of system diagnostics, frequency sync events, and scalar feedback loops.

Author: Bryce Wooster
License: Custom Legal License (see LICENSE file)
"""

import datetime
import os

class Logger:
    def __init__(self, log_file="ix_tunercore.log", verbose=True):
        self.log_file = log_file
        self.verbose = verbose
        self._init_log()

    def _init_log(self):
        header = f"\n--- IX-TunerCore Log Initialized: {self._timestamp()} ---\n"
        with open(self.log_file, "a") as f:
            f.write(header)
        if self.verbose:
            print(header.strip())

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, level, message):
        entry = f"[{self._timestamp()}] [{level.upper()}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(entry)
        if self.verbose:
            print(entry.strip())

    def info(self, message):
        self._write("info", message)

    def warning(self, message):
        self._write("warning", message)

    def error(self, message):
        self._write("error", message)

    def debug(self, message):
        self._write("debug", message)
