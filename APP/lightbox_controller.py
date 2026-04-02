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

            # success → turn dot green
            self.gui.set_status_dot("can_init", "green")

        except RuntimeError as e:
            print(e)

            # failure → keep/turn dot red
            self.gui.set_status_dot("can_init", "red")
    
    def turn_on_node(self, node_text):
        try:
            can_id = int(node_text, 16)   # converts "0x02" to 2
            self.can.send_message(can_id, [0x01])
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")

    def turn_off_node(self, node_text):
        try:
            can_id = int(node_text, 16)   # converts "0x02" to 2
            self.can.send_message(can_id, [0x00])
        except ValueError:
            self.gui.set_status_dot("invalid_input", "red")
        except RuntimeError:
            self.gui.set_status_dot("connection", "red")