'''
    File: pcan_interface.py
    Desciption: This is the file connects to PCAN and sends/receives messages.

    By: Reegan Graham
'''
from PCANBasic import PCANBasic, TPCANMsg, PCAN_ERROR_OK
from config import PCAN_CHANNEL, PCAN_BAUDRATE


class PCANInterface:
    def __init__(self):
        self.pcan = PCANBasic()
        self.channel = PCAN_CHANNEL
        self.baudrate = PCAN_BAUDRATE
        self.initialized = False

    def initialize(self):
        result = self.pcan.Initialize(self.channel, self.baudrate)
        if result != PCAN_ERROR_OK:
            raise RuntimeError(f"Failed to initialize PCAN. Error code: {result}")
        self.initialized = True

    def send_message(self, can_id, data):
        if not self.initialized:
            raise RuntimeError("PCAN bus not initialized")

        msg = TPCANMsg()
        msg.ID = can_id
        msg.LEN = len(data)
        msg.MSGTYPE = 0  # standard CAN frame

        for i, byte in enumerate(data):
            msg.DATA[i] = byte

        result = self.pcan.Write(self.channel, msg)
        if result != PCAN_ERROR_OK:
            raise RuntimeError(f"PCAN write failed: {self._get_error_text(result)}")

    def read_message(self):
        if not self.initialized:
            raise RuntimeError("PCAN bus not initialized")

        result, msg, timestamp = self.pcan.Read(self.channel)
        if result == PCAN_ERROR_OK:
            data = [msg.DATA[i] for i in range(msg.LEN)]
            return {
                "id": msg.ID,
                "len": msg.LEN,
                "data": data,
                "timestamp": timestamp,
            }

        return None

    def shutdown(self):
        if self.initialized:
            self.pcan.Uninitialize(self.channel)
            self.initialized = False

    def _get_error_text(self, error_code):
        result = self.pcan.GetErrorText(error_code)
        try:
            return result[1]
        except Exception:
            return f"Error code {error_code}"
        
if __name__ == "__main__":
    app = PCANInterface()
    app.initialize()
    app.send_message(0x2, [0x3])