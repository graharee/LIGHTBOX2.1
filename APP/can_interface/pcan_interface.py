"""
can_interface/pcan_interface.py

All PCANBasic code lives here.

MCU receive protocol:
    CAN ID  = PCB address
    data[0] = driver number
    data[1] = command OR LED address
    data[2] = value

For single LED PWM:
    [driver][LED address][PWM percent]

For all LEDs:
    [driver][0x00][command][value]

Temperature RX from MCU:
    data[0] = high byte
    data[1] = low byte
    temp C  = ((high << 8) | low) / 100.0
"""

from PySide6.QtCore import QObject, Signal

from config.app_config import (
    WRITE_ALL,
    CAN_MESSAGE_SET_CURRENT,
    CAN_MESSAGE_SET_PWM,
)

try:
    from PCANBasic import *  # type: ignore
    PCAN_AVAILABLE = True
except Exception:
    PCAN_AVAILABLE = False


class PcanInterface(QObject):
    connection_changed = Signal(bool)
    message_received = Signal(int, list)
    temperature_received = Signal(float)
    log_message = Signal(str)
    error_message = Signal(str)

    def __init__(self):
        super().__init__()
        self.connected = False

        if PCAN_AVAILABLE:
            self.pcan = PCANBasic()
            self.channel = PCAN_USBBUS1
            self.baudrate = PCAN_BAUD_1M
        else:
            self.pcan = None
            self.channel = None
            self.baudrate = None

    def initialize(self):
        if not PCAN_AVAILABLE or self.pcan is None:
            self._set_connected(False)
            self.error_message.emit("PCANBasic.py not found")
            return False

        result = self.pcan.Initialize(self.channel, self.baudrate)

        if result == PCAN_ERROR_OK:
            self._set_connected(True)
            self.error_message.emit("")
            return True

        self._set_connected(False)
        self.error_message.emit("PCAN disconnected")
        return False

    def check_connection(self):
        if not PCAN_AVAILABLE or self.pcan is None:
            self._set_connected(False)
            self.error_message.emit("PCANBasic.py not found")
            return False

        result, condition = self.pcan.GetValue(
            self.channel,
            PCAN_CHANNEL_CONDITION
        )

        if result != PCAN_ERROR_OK:
            self._set_connected(False)
            return False

        if condition == PCAN_CHANNEL_AVAILABLE or condition == PCAN_CHANNEL_OCCUPIED:
            init_result = self.pcan.Initialize(self.channel, self.baudrate)

            if init_result == PCAN_ERROR_OK or init_result == PCAN_ERROR_INITIALIZE:
                self._set_connected(True)
                return True

        self._set_connected(False)
        return False

    def send_payload(self, can_id, payload):
        if not self.check_connection():
            self.log_message.emit("TX FAILED: PCAN not connected")
            return False

        can_id = int(str(can_id), 0)

        msg = TPCANMsg()
        msg.ID = can_id
        msg.MSGTYPE = PCAN_MESSAGE_STANDARD
        msg.LEN = len(payload)

        for i in range(8):
            msg.DATA[i] = payload[i] if i < len(payload) else 0

        result = self.pcan.Write(self.channel, msg)

        print("WRITE RESULT:", hex(result))
        print("CAN ID:", hex(can_id))
        print("DATA:", [hex(x) for x in payload])

        data_text = " ".join(f"{byte:02X}" for byte in payload)

        if result == PCAN_ERROR_OK:
            self.log_message.emit(
                f"TX  ID: 0x{can_id:X}  DATA: {data_text}"
            )
            return True

        self.log_message.emit(
            f"TX FAILED  ID: 0x{can_id:X}  DATA: {data_text}"
        )

        self.error_message.emit(
            f"CAN write failed: 0x{int(result):X}"
        )

        return False

    def send_single_led_pwm(self, can_id, driver, led_address, pwm_percent):
        """
        Sends:
            data[0] = driver
            data[1] = LED address
            data[2] = PWM percent
        """
        payload = [
            int(driver) & 0xFF,
            int(led_address) & 0xFF,
            int(pwm_percent) & 0xFF,
        ]
        return self.send_payload(can_id, payload)

    def send_all_pwm(self, can_id, driver, pwm_percent):
        """
        Sends:
            data[0] = driver
            data[1] = 0x00
            data[2] = CAN_MESSAGE_SET_PWM
            data[3] = PWM percent
        """
        payload = [
            int(driver) & 0xFF,
            WRITE_ALL,
            CAN_MESSAGE_SET_PWM,
            int(pwm_percent) & 0xFF,
        ]
        return self.send_payload(can_id, payload)

    def send_current(self, can_id, driver, current_ma):
        """
        Current is driver-wide, so this uses WRITE_ALL format:
            data[0] = driver
            data[1] = 0x00
            data[2] = CAN_MESSAGE_SET_CURRENT
            data[3] = current mA
        """
        payload = [
            int(driver) & 0xFF,
            WRITE_ALL,
            CAN_MESSAGE_SET_CURRENT,
            int(current_ma) & 0xFF,
        ]
        return self.send_payload(can_id, payload)

    def read_once(self):
        if not self.connected or not PCAN_AVAILABLE or self.pcan is None:
            return

        result, msg, timestamp = self.pcan.Read(self.channel)

        if result == PCAN_ERROR_OK:
            data = [int(msg.DATA[i]) for i in range(msg.LEN)]
            self.message_received.emit(int(msg.ID), data)

            data_text = " ".join(f"{byte:02X}" for byte in data)
            self.log_message.emit(f"RX  ID: 0x{msg.ID:X}  DATA: {data_text}")

            # MCU temperature response is 2 bytes:
            # data[0] = high byte, data[1] = low byte, scaled by 100.
            if msg.LEN >= 2:
                temp_scaled = (data[0] << 8) | data[1]
                temp_c = temp_scaled / 100.0

                # Basic sanity filter so random messages do not become insane temperatures.
                if -40.0 <= temp_c <= 150.0:
                    self.temperature_received.emit(temp_c)

        elif result != PCAN_ERROR_QRCVEMPTY:
            self.error_message.emit(f"CAN read error: 0x{int(result):X}")

    def _set_connected(self, connected):
        if self.connected != connected:
            self.connected = connected
            self.connection_changed.emit(connected)

            if connected:
                self.log_message.emit("[INFO] PCAN connected")
            else:
                self.log_message.emit("[ERROR] PCAN disconnected")
