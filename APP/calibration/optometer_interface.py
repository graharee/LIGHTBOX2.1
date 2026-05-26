"""
Optometer interface.

This file will eventually handle communication with the
Gigahertz-Optik S380 optometer through GPIB-USB.

For now, this is a skeleton with placeholder behavior.
"""

class OptometerInterface:
    def __init__(self):
        self.connected = False

    def connect(self):
        """
        Connect to the optometer.

        Later this is where you would initialize the GPIB connection.
        """
        print("Connecting to optometer...")
        self.connected = True
        return self.connected

    def disconnect(self):
        """
        Disconnect from the optometer.
        """
        print("Disconnecting optometer...")
        self.connected = False

    def read_mlux(self):
        """
        Read the current light level from the optometer in mlux.

        Placeholder value for now.
        Later, replace this with the real optometer read command.
        """
        if not self.connected:
            raise RuntimeError("Optometer is not connected.")

        measured_mlux = 0.0

        return measured_mlux