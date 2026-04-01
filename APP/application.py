'''
    File: application.py
    Desciption: This is the file that opens and runs the Lightbox 2.1 application

    By: Reegan Graham
'''
from gui import lightbox_gui
from pcan_interface import PCANInterface
from messages import MessageBuilder

class App:
    def __init__(self):
        self.can_bus = PCANInterface()
        self.msg_builder = MessageBuilder()
        self.gui = lightbox_gui(controller=self)

    def start(self):
        self.can_bus.initialize()
        self.gui.mainloop()
        self.can_bus.shutdown()

    # Example GUI callback methods
    def enable_ir(self):
        msg = self.msg_builder.enable_source("IR")
        self.can_bus.send_message(msg)

    def disable_ir(self):
        msg = self.msg_builder.disable_source("IR")
        self.can_bus.send_message(msg)

    def set_ambient(self, value):
        msg = self.msg_builder.set_ambient(value)
        self.can_bus.send_message(msg)

    def set_glare(self, value):
        msg = self.msg_builder.set_glare(value)
        self.can_bus.send_message(msg)

    def set_fan_speed(self, value):
        msg = self.msg_builder.set_fan_speed(value)
        self.can_bus.send_message(msg)

    def request_temperature(self, node):
        msg = self.msg_builder.request_temperature(node)
        self.can_bus.send_message(msg)


if __name__ == "__main__":
    app = App()
    app.start()