'''
    File: application.py
    Desciption: This is the file that opens and runs the Lightbox 2.1 application

    By: Reegan Graham

    Responsibilities:
    1. Create the QApplication
    2. Initialize the PCAN interface object
    3. Open the GUI
    4. Start the Qt event loop
'''
import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from can_interface.pcan_interface import PcanInterface
from gui.main_window import LightboxWindow

def main() -> None:
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))

    pcan = PcanInterface()

    window = LightboxWindow(pcan)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
