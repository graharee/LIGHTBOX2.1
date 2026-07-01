"""
calibration/formation_calibrator.py

Sweeps one LED formation by:
1. Keeping the formation shape the same
2. Sweeping PWM from 1% to 100%
3. Increasing current
4. Reading optometer feedback
5. Saving every measured point to CSV
"""

import csv
import copy
import time
from datetime import datetime

from calibration.visible_light_algorithm import (
    COMMAND_CURRENT,
    COMMAND_SINGLE_PWM,
    COMMAND_ALL_PWM,
)

class FormationCalibrator:
    def __init__(
        self,
        can_interface,
        optometer,
        formation_name,
        formation_commands,
        output_csv="formation_calibration.csv",
        min_current_ma=4,
        max_current_ma=50,
        min_pwm=10,
        max_pwm=100,
        pwm_step = 5,
        settle_time_s=2,
    ):
        self.can = can_interface
        self.optometer = optometer

        self.formation_name = formation_name
        self.formation_commands = formation_commands
        self.output_csv = output_csv

        self.min_current_ma = min_current_ma
        self.max_current_ma = max_current_ma
        self.min_pwm = min_pwm
        self.max_pwm = max_pwm
        self.pwm_step = pwm_step

        self.settle_time_s = settle_time_s

        self.stop_requested = False

    def request_stop(self):
        self.stop_requested = True

    def run(self):
        self._create_csv()

        for current_ma in range(self.min_current_ma, self.max_current_ma + 1):
            if self.stop_requested:
                break

            for pwm in range(self.min_pwm, self.max_pwm + 1, self.pwm_step):
                if self.stop_requested:
                    break

                commands = self._build_commands_for_step(
                    current_ma=current_ma,
                    pwm=pwm,
                )

                self._send_commands(commands)

                time.sleep(self.settle_time_s)

                measured_lux = self._read_optometer_lux()
                measured_mlux = measured_lux * 1000.0

                self._save_measurement(
                    current_ma=current_ma,
                    pwm=pwm,
                    measured_lux=measured_lux,
                    measured_mlux=measured_mlux,
                )
                time.sleep(0.005)
                print(
                    f"{self.formation_name}: "
                    f"{current_ma} mA, {pwm}% PWM -> "
                    f"{measured_mlux:.3f} mlux"
                )

        self._turn_formation_off()

    def _build_commands_for_step(self, current_ma, pwm):
        commands = copy.deepcopy(self.formation_commands)

        for command in commands:
            if command["type"] == COMMAND_CURRENT:
                command["value"] = current_ma

            elif command["type"] == COMMAND_SINGLE_PWM:
                command["value"] = pwm

            elif command["type"] == COMMAND_ALL_PWM:
                command["value"] = pwm

        return commands

    def _send_commands(self, commands):
        """
        Sends each command in the formation.
        """

        for command in commands:
            command_type = command["type"]

            if command_type == COMMAND_CURRENT:
                self.can.send_current(
                    command["can_id"],
                    command["driver"],
                    command["value"],
                )

            elif command_type == COMMAND_SINGLE_PWM:
                self.can.send_single_led_pwm(
                    command["can_id"],
                    command["driver"],
                    command["led"],
                    command["value"],
                )
            
            elif command_type == COMMAND_ALL_PWM:
                self.can.send_all_pwm(
                    command["can_id"],
                    command["driver"],
                    command["value"],
                )

            time.sleep(0.001)

    def _turn_formation_off(self):
        for command in self.formation_commands:
            if command["type"] == COMMAND_SINGLE_PWM:
                self.can.send_single_led_pwm(
                    command["can_id"],
                    command["driver"],
                    command["led"],
                    0,
                )

            elif command["type"] == COMMAND_ALL_PWM:
                self.can.send_all_pwm(
                    command["can_id"],
                    command["driver"],
                    0,
                )

            time.sleep(0.05)

    def _read_optometer_lux(self):
        reading, unit = self.optometer.read_lux_value()

        unit = unit.strip().lower()

        if unit in ["lux", "lx"]:
            return float(reading) * 1000

        if unit in ["mlux", "mlx"]:
            return float(reading)
        
        if unit in ["ulux", "ulx"]:
            return float(reading)
        
        if unit in ["plux", "plx"]:
            return float(reading)

        raise ValueError(f"Unknown optometer unit: {unit}")

    def _create_csv(self):
        with open(self.output_csv, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "timestamp",
                    "formation_name",
                    "current_ma",
                    "pwm_percent",
                    "measured_mlux",
                    "measured_mlux",
                ]
            )

    def _save_measurement(
        self,
        current_ma,
        pwm,
        measured_lux,
        measured_mlux,
    ):
        with open(self.output_csv, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    datetime.now().isoformat(timespec="seconds"),
                    self.formation_name,
                    current_ma,
                    pwm,
                    measured_lux,
                    measured_mlux,
                ]
            )