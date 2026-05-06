'''
    File: lightbox_controller.py
    Desciption: This file connects GUI actions to CAN actions

    By: Reegan Graham
'''

class LightboxController:
    def __init__(self, gui, can_interface):
        self.gui = gui
        self.can = can_interface

    def initialize_can(self):
        try:
            self.can.initialize()

            # success → dont't change dot
            self.gui.set_status_dot("can_init", "red")

        except RuntimeError as e:
            print(e)

            # failure → turn dot green
            self.gui.set_status_dot("can_init", "green")
    
    def turn_on_node(self, node_address, led_address):
        try:
            can_id = int(node_address, 16)   # converts hex to decimal

            if led_address is None: # if no led address is specifed, control whole node
                led_id = 256
            else:
                led_id = int(led_address, 0)     # turning on -> same as LED address

            self.can.send_message(can_id, [led_id])
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")

    def turn_off_node(self, node_address, led_address):
        try:
            can_id = int(node_address, 16)      # converts hex to decimal

            if led_address is None: # if no led address is specifed, control whole node
                led_id = 0
            else:
                led_id = int(led_address, 0) + 42   # turning off -> LED address + 42

            self.can.send_message(can_id, [led_id])
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")

    def get_node_temp(self, node_address):
        try:
            can_id = int(node_address, 16)      # converts hex to decimal
            self.can.send_message(can_id, [0x79])
            self._set_node_temp()
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")

    def _set_node_temp(self):
        try:
            msg = self.can.read_message()
            if msg is not None:
                node_temp = msg["data"]

            temp = int(node_temp[0], 16)      
            self.gui.set_node_temperature(temp)
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")