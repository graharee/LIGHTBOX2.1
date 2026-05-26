"""
config/app_config.py

Application-wide constants.
"""

# PCAN
PCAN_CHANNEL_INDEX = 1
PCAN_BAUDRATE_NAME = "1M"

# Timers
PCAN_CONNECTION_CHECK_MS = 1000
CAN_RX_POLL_MS = 100
TEMP_TIMEOUT_MS = 3000

# CAN protocol
WRITE_ALL = 0x00

# These values MUST match can_interface.h on the MCU side.
# Update these if your C header uses different values.
CAN_MESSAGE_ALL_OFF = 0x00
CAN_MESSAGE_ALL_ON = 0xFF
CAN_MESSAGE_SET_CURRENT = 0x55
CAN_MESSAGE_SET_PWM = 0x56

# Light-source-to-driver mapping.
# Change these if your physical wiring maps differently.
DRIVER_HEADLIGHT = 1
DRIVER_IR_850 = 2
DRIVER_IR_940 = 3
DRIVER_SUNLIGHT = 4