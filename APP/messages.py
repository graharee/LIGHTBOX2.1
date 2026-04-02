'''
    File: messages.py
    Desciption: This is the file contains the CAN messages

    By: Reegan Graham
'''
from dataclasses import dataclass

@dataclass
class CanMessage:
    can_id: int
    data: list[int]
    extended: bool = False

NODE_IDS = {
    1: 0x002,
    2: 0x003,
    3: 0x004,
    4: 0x005,
    5: 0x006,
    6: 0x007,
}

CURRENT_COMMANDS = {
    25: 0x55,
    35: 0x56,
    45: 0x57,
    55: 0x58,
    65: 0x59,
    75: 0x5A,
    85: 0x5B,
    95: 0x5C,
    100: 0x5D,
    31: 0x71,
    41: 0x72,
    51: 0x73,
    61: 0x74,
    71: 0x75,
    81: 0x76,
}

DIVIDER_COMMANDS = {
    "eighth": 0x5E,
    "quarter": 0x5F,
    "half": 0x60,
    "default": 0x61,
}

PWM_COMMANDS = {
    88: 0x6C,
    105: 0x6D,
    148: 0x6E,
    288: 0x6F,
    "low": 0x70,
}

TEMP_COMMANDS = {
    "micro": 0x78,
    "driver": 0x79,
    "back": 0x7A,
}


def _msg(node: int, command: int) -> CanMessage:
    if node not in NODE_IDS:
        raise ValueError(f"Invalid node: {node}")
    return CanMessage(can_id=NODE_IDS[node], data=[command])


def set_all_off(node: int) -> CanMessage:
    return _msg(node, 0x00)


def set_all_high(node: int) -> CanMessage:
    return _msg(node, 0xFF)


def set_channel_on(node: int, channel: int) -> CanMessage:
    if not 1 <= channel <= 42:
        raise ValueError("channel must be 1..42")
    return _msg(node, channel)


def set_channel_off(node: int, channel: int) -> CanMessage:
    if not 1 <= channel <= 42:
        raise ValueError("channel must be 1..42")
    return _msg(node, 0x2A + channel)


def set_current_ma(node: int, current_ma: int) -> CanMessage:
    if current_ma not in CURRENT_COMMANDS:
        raise ValueError(f"Unsupported current: {current_ma} mA")
    return _msg(node, CURRENT_COMMANDS[current_ma])


def set_divider(node: int, mode: str) -> CanMessage:
    mode = mode.lower()
    if mode not in DIVIDER_COMMANDS:
        raise ValueError(f"Unsupported divider mode: {mode}")
    return _msg(node, DIVIDER_COMMANDS[mode])


def set_pwm(node: int, pwm) -> CanMessage:
    key = pwm.lower() if isinstance(pwm, str) else pwm
    if key not in PWM_COMMANDS:
        raise ValueError(f"Unsupported PWM setting: {pwm}")
    return _msg(node, PWM_COMMANDS[key])


def get_temp(node: int, sensor: str) -> CanMessage:
    sensor = sensor.lower()
    if sensor not in TEMP_COMMANDS:
        raise ValueError(f"Unsupported temp sensor: {sensor}")
    return _msg(node, TEMP_COMMANDS[sensor])