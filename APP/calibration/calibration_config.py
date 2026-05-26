"""
Calibration configuration values.

These values can be adjusted later once the real lightbox behavior is tested.
"""

# Delay after sending a CAN command before reading the optometer
LIGHT_SETTLE_TIME_SEC = 0.5

# Maximum number of adjustment attempts for one target
MAX_CALIBRATION_ATTEMPTS = 50

# Acceptable error from target
# Example: 0.05 = +/- 5%
DEFAULT_TOLERANCE_PERCENT = 0.05

# Minimum and maximum user-facing PWM values
MIN_PWM_PERCENT = 1
MAX_PWM_PERCENT = 100

# Starting PWM value for a new target
START_PWM_PERCENT = 1

# File where calibration results will be saved
CALIBRATION_TABLE_FILE = "calibration_table.json"