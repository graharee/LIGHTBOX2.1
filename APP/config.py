'''
    File: config.py
    Desciption: This is the file configures pcan and its initial values.

    By: Reegan Graham
'''
from PCANBasic import PCAN_USBBUS1, PCAN_BAUD_1M

PCAN_CHANNEL = PCAN_USBBUS1
PCAN_BAUDRATE = PCAN_BAUD_1M

PCAN_DEVICE_NAME = "PCAN-USB: Device ID 1h"
PCAN_BITRATE_KBPS = 1000
PCAN_CLOCK_FREQUENCY = "8 MHz"
PCAN_MODE = "CAN (SJA1000)"
PCAN_HW_TYPE = "standard"