"""
Calibration algorithm.

This file decides whether the measured light level is close enough
and what PWM value should be tried next.
"""

from calibration.calibration_config import (
    MIN_PWM_PERCENT,
    MAX_PWM_PERCENT,
    DEFAULT_TOLERANCE_PERCENT,
)


class CalibrationAlgorithm:
    def __init__(self, tolerance_percent=DEFAULT_TOLERANCE_PERCENT):
        self.tolerance_percent = tolerance_percent

    def is_within_tolerance(self, target_mlux, measured_mlux):
        """
        Check if the measured value is close enough to the target.
        """
        if target_mlux == 0:
            return measured_mlux == 0

        error = abs(target_mlux - measured_mlux)
        allowed_error = target_mlux * self.tolerance_percent

        return error <= allowed_error

    def get_next_pwm(self, current_pwm, target_mlux, measured_mlux):
        """
        Decide the next PWM value.

        Basic first version:
        - if measured is too low, increase PWM
        - if measured is too high, decrease PWM
        """

        if measured_mlux < target_mlux:
            next_pwm = current_pwm + 1
        else:
            next_pwm = current_pwm - 1

        if next_pwm < MIN_PWM_PERCENT:
            next_pwm = MIN_PWM_PERCENT

        if next_pwm > MAX_PWM_PERCENT:
            next_pwm = MAX_PWM_PERCENT

        return next_pwm