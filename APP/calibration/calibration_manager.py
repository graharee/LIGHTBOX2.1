"""
Calibration manager.

This is the main controller for calibration.
It connects CAN, optometer, algorithm, and saved calibration data.
"""

import time

from calibration.calibration_config import (
    LIGHT_SETTLE_TIME_SEC,
    MAX_CALIBRATION_ATTEMPTS,
    START_PWM_PERCENT,
)

from calibration.calibration_algorithm import CalibrationAlgorithm
from calibration.calibration_table import CalibrationTable


class CalibrationManager:
    def __init__(self, can_interface, optometer):
        self.can_interface = can_interface
        self.optometer = optometer

        self.algorithm = CalibrationAlgorithm()
        self.table = CalibrationTable()

    def start_calibration(self, light_source, target_mlux_values):
        """
        Calibrate multiple target light levels.

        light_source example:
            "visible_ambient"

        target_mlux_values example:
            [1, 2, 3, 4, 5, 10, 20, 50, 100]
        """

        print("Starting calibration...")

        self.table.load()

        if not self.optometer.connected:
            self.optometer.connect()

        results = []

        for target_mlux in target_mlux_values:
            result = self.calibrate_single_target(light_source, target_mlux)

            self.table.add_result(light_source, result)
            results.append(result)

        self.table.save()

        print("Calibration complete.")

        return results

    def calibrate_single_target(self, light_source, target_mlux):
        """
        Calibrate one target light level.
        """

        print(f"Calibrating {light_source} at {target_mlux} mlux...")

        pwm_percent = START_PWM_PERCENT

        for attempt in range(MAX_CALIBRATION_ATTEMPTS):
            self.send_light_setting(light_source, pwm_percent)

            time.sleep(LIGHT_SETTLE_TIME_SEC)

            measured_mlux = self.optometer.read_mlux()

            print(
                f"Attempt {attempt + 1}: "
                f"Target = {target_mlux} mlux, "
                f"Measured = {measured_mlux} mlux, "
                f"PWM = {pwm_percent}%"
            )

            if self.algorithm.is_within_tolerance(target_mlux, measured_mlux):
                result = {
                    "light_source": light_source,
                    "target_mlux": target_mlux,
                    "measured_mlux": measured_mlux,
                    "pwm_percent": pwm_percent,
                    "attempts": attempt + 1,
                    "status": "PASS",
                }

                return result

            next_pwm = self.algorithm.get_next_pwm(
                pwm_percent,
                target_mlux,
                measured_mlux
            )

            if next_pwm == pwm_percent:
                break

            pwm_percent = next_pwm

        result = {
            "light_source": light_source,
            "target_mlux": target_mlux,
            "measured_mlux": measured_mlux,
            "pwm_percent": pwm_percent,
            "attempts": MAX_CALIBRATION_ATTEMPTS,
            "status": "FAIL",
        }

        return result

    def send_light_setting(self, light_source, pwm_percent):
        """
        Send the light command through CAN.

        This is intentionally generic right now because your actual CAN format
        may change depending on ambient/glare, LED type, and driver.
        """

        print(f"Sending {light_source} command at {pwm_percent}% PWM")

        self.can_interface.send_calibration_command(
            light_source=light_source,
            pwm_percent=pwm_percent
        )