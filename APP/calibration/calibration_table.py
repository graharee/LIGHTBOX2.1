"""
Calibration table.

This file saves and loads calibration results.
"""

import json
import os

from calibration.calibration_config import CALIBRATION_TABLE_FILE


class CalibrationTable:
    def __init__(self, filename=CALIBRATION_TABLE_FILE):
        self.filename = filename
        self.data = {}

    def load(self):
        """
        Load existing calibration data from JSON.
        """
        if not os.path.exists(self.filename):
            self.data = {}
            return self.data

        with open(self.filename, "r") as file:
            self.data = json.load(file)

        return self.data

    def save(self):
        """
        Save calibration data to JSON.
        """
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_result(self, light_source, result):
        """
        Add one calibration result.

        Example light_source:
        - visible_ambient
        - visible_glare
        - ir_ambient
        - ir_glare
        """

        if light_source not in self.data:
            self.data[light_source] = []

        self.data[light_source].append(result)

    def get_results(self, light_source):
        """
        Get all saved results for one light source.
        """
        return self.data.get(light_source, [])