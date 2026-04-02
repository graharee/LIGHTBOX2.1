'''
    File: application.py
    Desciption: This is the file that opens and runs the Lightbox 2.1 application

    By: Reegan Graham
'''
from lightbox_gui import LightboxGUI
from lightbox_controller import LightboxController
from pcan_interface import PCANInterface

def main():
    gui = LightboxGUI()
    can = PCANInterface()
    controller = LightboxController(gui, can)

    # give GUI access to controller
    gui.controller = controller

    # initialize CAN on startup
    controller.initialize_can()

    gui.mainloop()

if __name__ == "__main__":
    main()