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

# """
# Optometer interface.

# This file will eventually handle communication with the
# Gigahertz-Optik S380 optometer through GPIB-USB.

# For now, this is a skeleton with placeholder behavior.
# """

# class OptometerInterface:
#     def __init__(self):
#         self.connected = False

#     def connect(self):
#         """
#         Connect to the optometer.

#         Later this is where you would initialize the GPIB connection.
#         """
#         print("Connecting to optometer...")
#         self.connected = True
#         return self.connected

#     def disconnect(self):
#         """
#         Disconnect from the optometer.
#         """
#         print("Disconnecting optometer...")
#         self.connected = False

#     def read_mlux(self):
#         """
#         Read the current light level from the optometer in mlux.

#         Placeholder value for now.
#         Later, replace this with the real optometer read command.
#         """
#         if not self.connected:
#             raise RuntimeError("Optometer is not connected.")

#         measured_mlux = 0.0

#         return measured_mlux