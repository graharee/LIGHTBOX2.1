import serial
import time


class OptometerInterface:
    def __init__(self, port="COM10", baudrate=9600, timeout=1.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        if self.ser is not None and self.ser.is_open:
            return True

        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
        )
        return self.ser.is_open

    def disconnect(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()

    def is_connected(self):
        return self.ser is not None and self.ser.is_open

    def read_measurement(self):
        if not self.is_connected():
            self.connect()

        self.ser.reset_input_buffer()
        self.ser.write(b"READ?\r")
        time.sleep(0.2)

        response = self.ser.read_all().decode("ascii", errors="ignore").strip()

        if not response:
            raise RuntimeError("No response from optometer.")

        return response

    def read_lux_value(self):
        response = self.read_measurement()
    
        parts = response.replace(",", " ").split()
        print(parts)
    
        value = None
        unit = ""
    
        for part in parts:
            try:
                value = float(part)
            except ValueError:
                # keep possible unit strings like lx, lux, mlux, etc.
                if part.lower() not in ["read", "read?"]:
                    unit = part
    
        if value is None:
            raise ValueError(f"Could not parse optometer response: {response!r}")
    
        return value, unit