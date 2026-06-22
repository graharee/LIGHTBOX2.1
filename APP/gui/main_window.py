"""
gui/main_window.py

Main Lightbox GUI.

Important architecture:
    - Basic tab selects light source.
    - Selected light source determines driver number.
    - Advanced tab uses selected driver number.
    - PCB address is the CAN ID.
    - LED address 0x00 means "all LEDs".
"""
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QCheckBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from calibration.visible_light_algorithm import (
    COMMAND_CURRENT,
    COMMAND_ALL_PWM,
    COMMAND_SINGLE_PWM,
    get_visible_commands,
)

from config.app_config import (
    PCAN_CONNECTION_CHECK_MS,
    CAN_RX_POLL_MS,
    TEMP_TIMEOUT_MS,
    DRIVER_IR_850,
    DRIVER_IR_940,
    DRIVER_HEADLIGHT,
    DRIVER_SUNLIGHT,
)

from gui.widgets import (
    StatusDot,
    MetricCard,
    FaultRow,
    LightSourceTile,
    AdjustmentCard,
    OptometerReadingCard,
)

from calibration.optometer_interface import OptometerInterface

class LightboxWindow(QMainWindow):
    def __init__(self, pcan):
        super().__init__()

        self.pcan = pcan

        self.selected_driver = None
        self.selected_light_source_name = "None"

        self.light_tiles = []

        self.setWindowTitle("Magna Lightbox 2.1")
        self.resize(1280, 760)

        self.build_ui()
        self.apply_styles()
        self.connect_signals()
        self.start_timers()

        self.optometer = OptometerInterface(port="COM10")
        # self.optometer_timer = QTimer(self)
        # self.optometer_timer.timeout.connect(self.update_optometer_boxes)
        # self.optometer_timer.start(1000)

        self.optometer_timer = QTimer(self)
        self.optometer_timer.timeout.connect(self.update_optometer_boxes)
        self.optometer_timer.start(1000)

        print("[OPTOMETER] Timer started")

    def build_ui(self):
        root = QWidget()
        root.setObjectName("root")

        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(22, 18, 22, 18)
        root_layout.setSpacing(16)

        root_layout.addWidget(self.build_header())

        self.tabs = QTabWidget()
        self.tabs.addTab(self.build_dashboard_tab(), "Basic")
        self.tabs.addTab(self.build_advanced_tab(), "Advanced")
        self.tabs.addTab(self.build_calibration_tab(), "Calibration")
        self.tabs.addTab(self.build_logs_tab(), "Logs")

        root_layout.addWidget(self.tabs)

        self.setCentralWidget(root)

    def connect_signals(self):
        self.pcan.connection_changed.connect(self.update_connection_status)
        self.pcan.log_message.connect(self.add_log)
        self.pcan.error_message.connect(self.show_error)
        self.pcan.temperature_received.connect(self.update_temperature)

    def start_timers(self):
        self.pcan_timer = QTimer(self)
        self.pcan_timer.timeout.connect(self.pcan.check_connection)
        self.pcan_timer.start(PCAN_CONNECTION_CHECK_MS)

        self.rx_timer = QTimer(self)
        self.rx_timer.timeout.connect(self.pcan.read_once)
        self.rx_timer.start(CAN_RX_POLL_MS)

        self.temperature_recent = False
        self.temp_watchdog_timer = QTimer(self)
        self.temp_watchdog_timer.timeout.connect(self.check_temperature_timeout)
        self.temp_watchdog_timer.start(TEMP_TIMEOUT_MS)

    def build_header(self):
        header = QFrame()
        header.setObjectName("header")

        title = QLabel("Magna Lightbox 2.1")
        title.setObjectName("appTitle")

        subtitle = QLabel("Engineering Control Interface")
        subtitle.setObjectName("appSubtitle")

        title_col = QVBoxLayout()
        title_col.addWidget(title)
        title_col.addWidget(subtitle)

        self.connect_dot = StatusDot("red", 13)
        self.connect_label = QLabel("PCAN Disconnected")
        self.connect_label.setObjectName("headerStatus")

        status_row = QHBoxLayout()
        status_row.addWidget(self.connect_dot)
        status_row.addWidget(self.connect_label)
        status_row.addSpacing(16)

        layout = QHBoxLayout(header)
        layout.addLayout(title_col)
        layout.addStretch()
        layout.addLayout(status_row)

        return header

    def build_dashboard_tab(self):
        page = QWidget()
        layout = QGridLayout(page)
        layout.setSpacing(16)

        source_panel = QFrame()
        source_panel.setObjectName("panelCard")
        source_panel.setMaximumHeight(380)

        source_title = QLabel("Light Sources")
        source_title.setObjectName("cardTitle")

        source_grid = QGridLayout()

        ir850 = LightSourceTile("IR 850 nm", "Infrared", DRIVER_IR_850, self)
        ir940 = LightSourceTile("IR 940 nm", "Infrared", DRIVER_IR_940, self)
        headlight = LightSourceTile("Headlight", "Visible", DRIVER_HEADLIGHT, self)
        sunlight = LightSourceTile("Sunlight", "Visible", DRIVER_SUNLIGHT, self)

        self.light_tiles.extend([ir850, ir940, headlight, sunlight])

        for tile in self.light_tiles:
            tile.selected.connect(self.set_selected_light_source)

        source_grid.addWidget(ir850, 0, 0)
        source_grid.addWidget(ir940, 0, 1)
        source_grid.addWidget(headlight, 1, 0)
        source_grid.addWidget(sunlight, 1, 1)

        source_layout = QVBoxLayout(source_panel)
        source_layout.addWidget(source_title)
        source_layout.addLayout(source_grid)

        adjustment_panel = QFrame()
        adjustment_panel.setObjectName("panelCard")

        adjustment_title = QLabel("Light Control")
        adjustment_title.setObjectName("cardTitle")

        adjustment_subtitle = QLabel("Basic page selects the light source. Advanced page uses that selection as the driver number.")
        adjustment_subtitle.setObjectName("smallMuted")

        adjustment_layout = QVBoxLayout(adjustment_panel)
        adjustment_layout.addWidget(adjustment_title)
        adjustment_layout.addWidget(adjustment_subtitle)
        adjustment_layout.addSpacing(10)
        self.visible_ambient_card = AdjustmentCard("Visible Ambient", "Controls the ambient output.")
        self.visible_glare_card = AdjustmentCard("Visible Glare", "Controls the glare output.")

        self.visible_ambient_card.send_requested.connect(self.send_visible_mlux_command)
        self.visible_glare_card.send_requested.connect(self.send_visible_mlux_command)

        adjustment_layout.addWidget(self.visible_ambient_card)
        adjustment_layout.addWidget(self.visible_glare_card)
        adjustment_layout.addStretch()

        readings_panel = QFrame()
        readings_panel.setObjectName("panelCard")
        readings_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        readings_panel.setFixedHeight(230)

        readings_title = QLabel("Optometer Readings")
        readings_title.setObjectName("cardTitle")

        readings_grid = QGridLayout()
        readings_grid.setSpacing(12)

        self.ambient_optometer_card = OptometerReadingCard("AMBIENT")
        self.glare_optometer_card = OptometerReadingCard("GLARE")

        readings_grid.addWidget(self.ambient_optometer_card, 0, 0)
        readings_grid.addWidget(self.glare_optometer_card, 0, 1)

        readings_layout = QVBoxLayout(readings_panel)
        readings_layout.addWidget(readings_title)
        readings_layout.addLayout(readings_grid)

        faults_panel = QFrame()
        faults_panel.setObjectName("panelCard")
        faults_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        faults_panel.setFixedHeight(300)

        faults_title = QLabel("System Health")
        faults_title.setObjectName("cardTitle")

        faults_subtitle = QLabel("Live status flags from APP, Calibration, and MCU.")
        faults_subtitle.setObjectName("smallMuted")

        faults_layout = QVBoxLayout(faults_panel)
        faults_layout.addWidget(faults_title)
        faults_layout.addWidget(faults_subtitle)
        faults_layout.addSpacing(10)
        self.connection_fault = FaultRow("Connection Status", "red")
        self.can_init_fault = FaultRow("CAN Bus Initialization", "red")
        self.invalid_input_fault = FaultRow("Invalid Input", "gray")
        self.calibration_fault = FaultRow("Calibration Status", "gray")
        self.overtemp_fault = FaultRow("Overtemperature Flag", "gray")

        faults_layout.addWidget(self.connection_fault)
        faults_layout.addWidget(self.can_init_fault)
        faults_layout.addWidget(self.invalid_input_fault)
        faults_layout.addWidget(self.calibration_fault)
        faults_layout.addWidget(self.overtemp_fault)
        faults_layout.addStretch()

        layout.addWidget(source_panel, 0, 0, 1, 1)
        layout.addWidget(adjustment_panel, 0, 1, 3, 1)

        right_column = QVBoxLayout()
        right_column.setSpacing(16)
        right_column.setContentsMargins(0, 0, 0, 0)
        right_column.addWidget(readings_panel)
        right_column.addWidget(faults_panel)
        right_column.addStretch()

        layout.addLayout(right_column, 0, 2, 3, 1)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2)

        return page
    
    def update_optometer_boxes(self):
        try:
            reading, unit = self.optometer.read_lux_value()

            self.ambient_optometer_card.set_reading(reading, unit)
            self.glare_optometer_card.set_reading(reading, unit)

            print(f"[OPTOMETER] light value={reading} {unit}")

        except Exception as e:
            self.ambient_optometer_card.set_reading(None)
            self.glare_optometer_card.set_reading(None)
            print(f"[OPTOMETER ERROR] {e}")

    def build_advanced_tab(self):
        page = QWidget()
        layout = QGridLayout(page)
        layout.setSpacing(16)

        control_card = QFrame()
        control_card.setObjectName("panelCard")
        control_layout = QVBoxLayout(control_card)

        title = QLabel("Advanced LED Control")
        title.setObjectName("cardTitle")

        subtitle = QLabel("CAN ID selects PCB. Basic page light source selects driver. LED address 0x00 means all LEDs.")
        subtitle.setObjectName("smallMuted")

        self.selected_source_label = QLabel("Selected light source: None")
        self.selected_source_label.setObjectName("sentValue")

        self.pcb_can_id_input = QLineEdit()
        self.pcb_can_id_input.setPlaceholderText("PCB CAN ID, example: 0x002")
        self.pcb_can_id_input.setText("0x002")

        self.led_address_input = QSpinBox()
        self.led_address_input.setRange(0, 48)
        self.led_address_input.setValue(0)

        self.pwm_input = QSpinBox()
        self.pwm_input.setRange(0, 100)
        self.pwm_input.setSuffix(" %")

        self.current_input = QSpinBox()
        self.current_input.setRange(4, 60)
        self.current_input.setSuffix(" mA")
        self.current_input.setValue(20)

        self.send_pwm_checkbox = QCheckBox("Send PWM")
        self.send_pwm_checkbox.setChecked(True)

        self.send_current_checkbox = QCheckBox("Send current")
        self.send_current_checkbox.setChecked(False)

        send_button = QPushButton("Send Command")
        send_button.setObjectName("primaryButton")
        send_button.clicked.connect(self.send_advanced_command)

        control_layout.addWidget(title)
        control_layout.addWidget(subtitle)
        control_layout.addSpacing(12)
        control_layout.addWidget(self.selected_source_label)
        control_layout.addSpacing(8)
        control_layout.addWidget(QLabel("PCB Address / CAN-ID"))
        control_layout.addWidget(self.pcb_can_id_input)
        control_layout.addWidget(QLabel("LED Address"))
        control_layout.addWidget(self.led_address_input)
        control_layout.addWidget(QLabel("PWM Value"))
        control_layout.addWidget(self.pwm_input)
        control_layout.addWidget(QLabel("Current Value"))
        control_layout.addWidget(self.current_input)
        control_layout.addWidget(self.send_pwm_checkbox)
        control_layout.addWidget(self.send_current_checkbox)
        control_layout.addSpacing(14)
        control_layout.addWidget(send_button)
        control_layout.addStretch()

        temp_card = QFrame()
        temp_card.setObjectName("panelCard")
        temp_layout = QVBoxLayout(temp_card)

        temp_title = QLabel("Temperature Monitor")
        temp_title.setObjectName("cardTitle")

        temp_subtitle = QLabel("Displays temperature continuously sent from the MCU.")
        temp_subtitle.setObjectName("smallMuted")

        self.temp_value_label = QLabel("--.-- °C")
        self.temp_value_label.setObjectName("metricValue")

        self.temp_status_dot = StatusDot("gray", 13)
        self.temp_status_label = QLabel("Waiting for temperature message")
        self.temp_status_label.setObjectName("smallMuted")

        temp_status_row = QHBoxLayout()
        temp_status_row.addWidget(self.temp_status_dot)
        temp_status_row.addWidget(self.temp_status_label)
        temp_status_row.addStretch()

        temp_layout.addWidget(temp_title)
        temp_layout.addWidget(temp_subtitle)
        temp_layout.addSpacing(20)
        temp_layout.addWidget(self.temp_value_label)
        temp_layout.addLayout(temp_status_row)
        temp_layout.addStretch()

        layout.addWidget(control_card, 0, 0)
        layout.addWidget(temp_card, 0, 1)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)

        return page

    def build_calibration_tab(self):
        page = QWidget()
        layout = QGridLayout(page)
        layout.setSpacing(16)

        card = QFrame()
        card.setObjectName("panelCard")
        card_layout = QVBoxLayout(card)

        title = QLabel("Calibration Sequence")
        title.setObjectName("cardTitle")

        subtitle = QLabel("Run calibration using optometer feedback and controller setpoints.")
        subtitle.setObjectName("smallMuted")

        start = QPushButton("Start Calibration")
        start.setObjectName("primaryButton")
        start.clicked.connect(self.start_calibration)

        stop = QPushButton("Stop Calibration")
        stop.setObjectName("dangerButton")
        stop.clicked.connect(self.stop_calibration)

        # Save these as self variables so you can update them later
        self.ambient_cal_status = QLabel("Ambient Calibration: Not Started")
        self.ambient_cal_status.setObjectName("smallMuted")

        self.glare_cal_status = QLabel("Glare Calibration: Not Started")
        self.glare_cal_status.setObjectName("smallMuted")

        self.cal_fault_status = QLabel("Faults: None Detected")
        self.cal_fault_status.setObjectName("smallMuted")

        button_layout = QHBoxLayout()
        button_layout.addWidget(start)
        button_layout.addWidget(stop)
        button_layout.addStretch()

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(18)
        card_layout.addLayout(button_layout)
        card_layout.addSpacing(18)

        card_layout.addWidget(self.ambient_cal_status)
        card_layout.addWidget(self.glare_cal_status)
        card_layout.addWidget(self.cal_fault_status)

        card_layout.addStretch()

        layout.addWidget(card, 0, 0)

        return page
    
    def set_ambient_calibration_status(self, status):
        self.ambient_cal_status.setText(f"Ambient Calibration: {status}")

    def set_glare_calibration_status(self, status):
        self.glare_cal_status.setText(f"Glare Calibration: {status}")

    def set_calibration_fault_status(self, fault_detected):
        if fault_detected:
            self.cal_fault_status.setText("Faults: Detected")
        else:
            self.cal_fault_status.setText("Faults: None Detected")

    def start_calibration(self):
        self.set_ambient_calibration_status("Running")
        self.set_glare_calibration_status("Waiting")
        self.set_calibration_fault_status(False)

        print("Calibration started")

    def stop_calibration(self):
        self.set_ambient_calibration_status("Stopped")
        self.set_glare_calibration_status("Stopped")
        print("Calibration stopped")

    def build_logs_tab(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setText("[INFO] Lightbox GUI started.\n[INFO] Waiting for PCAN connection...")

        layout.addWidget(self.log)
        return page

    def set_selected_light_source(self, driver_number, source_name):
        self.selected_driver = driver_number

        # ensure only that type of LED is on -- fix later
        self.led_cleanup(0x06)

        self.selected_light_source_name = source_name
        self.selected_source_label.setText(f"Selected light source: {source_name}  |  Driver: {driver_number}")

        if driver_number == DRIVER_IR_850 or driver_number == DRIVER_IR_940:
            self.led_address_input.setEnabled(False)
            self.led_address_input.setValue(1)
            self.add_log("[INFO] LED address disabled for IR light source.")
        else:
            self.led_address_input.setEnabled(True)

    def get_can_id(self):
        text = self.pcb_can_id_input.text().strip()

        try:
            can_id = int(text, 16) if text.lower().startswith("0x") else int(text)
        except ValueError:
            self.add_log("[ERROR] Invalid PCB CAN ID")
            self.set_invalid_input(True)
            return None

        if can_id < 0x02 or can_id > 0x29:
            self.add_log("[ERROR] PCB CAN ID must be between 0x02 and 0x29")
            self.set_invalid_input(True)
            return None

        self.set_invalid_input(False)
        return can_id

    def send_advanced_command(self):
        can_id = self.get_can_id()

        if can_id is None:
            return

        if self.selected_driver is None:
            self.add_log("[ERROR] Select a light source on the Basic tab first.")
            self.set_invalid_input(True)
            return

        if not self.send_current_checkbox.isChecked() and not self.send_pwm_checkbox.isChecked():
            self.add_log("[ERROR] Select Send PWM and/or Send current.")
            self.set_invalid_input(True)
            return

        led_address = self.led_address_input.value()
        pwm = self.pwm_input.value()
        current = self.current_input.value()

        self.set_invalid_input(False)

        if self.send_current_checkbox.isChecked():
            self.pcan.send_current(can_id, self.selected_driver, current)

        if self.send_pwm_checkbox.isChecked():
            if led_address == 0:
                self.pcan.send_all_pwm(can_id, self.selected_driver, pwm)
            else:
                self.pcan.send_single_led_pwm(can_id, self.selected_driver, led_address, pwm)

    def update_connection_status(self, connected):
        if connected:
            self.connect_dot.set_status("green")
            self.connect_label.setText("PCAN Connected")

            self.connection_fault.set_status("green")
            self.can_init_fault.set_status("green")
        else:
            self.connect_dot.set_status("red")
            self.connect_label.setText("PCAN Disconnected")

            self.connection_fault.set_status("red")
            self.can_init_fault.set_status("red")

    def update_temperature(self, temp_c):
        self.temperature_recent = True

        self.temp_value_label.setText(f"{temp_c:.2f} °C")
        self.temp_status_dot.set_status("green")
        self.temp_status_label.setText("Receiving temperature")

        if temp_c >= 70.0:
            self.overtemp_fault.set_status("red")
            self.add_log(f"[WARNING] Overtemperature detected: {temp_c:.2f} °C")
        else:
            self.overtemp_fault.set_status("gray")
    
    def check_temperature_timeout(self):
        if self.temperature_recent:
            self.temperature_recent = False
        else:
            self.temp_status_dot.set_status("gray")
            self.temp_status_label.setText("Waiting for temperature message")

    def add_log(self, text):
        self.log.append(text)

    def show_error(self, text):
        if text:
            self.add_log(f"[ERROR] {text}")

    def set_invalid_input(self, is_invalid):
        if is_invalid:
            self.invalid_input_fault.set_status("red")
        else:
            self.invalid_input_fault.set_status("gray")

    def send_visible_mlux_command(self, card, text):
        try:
            requested_mlux = int(text)
        except ValueError:
            self.add_log("[ERROR] Enter a valid mlux value.")
            self.set_invalid_input(True)
            return

        can_id = self.get_can_id()
        if can_id is None:
            self.set_invalid_input(True)
            return

        try:
            rounded_mlux, commands = get_visible_commands(requested_mlux)
        except ValueError as error:
            self.add_log(f"[ERROR] {error}")
            self.set_invalid_input(True)
            return

        self.led_cleanup(can_id)

        for command in commands:
            command_type = command["type"]
            driver = command["driver"]
            value = command["value"]

            if command_type == COMMAND_CURRENT:
                self.pcan.send_current(can_id, driver, value)

            elif command_type == COMMAND_ALL_PWM:
                self.pcan.send_all_pwm(can_id, driver, value)

            elif command_type == COMMAND_SINGLE_PWM:
                led = command["led"]
                self.pcan.send_single_led_pwm(can_id, driver, led, value)

            else:
                self.add_log(f"[ERROR] Unknown visible command type: {command_type}")
                self.set_invalid_input(True)
                return

        card.set_last_sent(f"{rounded_mlux} mlux")

        self.set_invalid_input(False)
        self.add_log(
            f"[INFO] Visible target sent: requested {requested_mlux} mlux, "
            f"rounded to {rounded_mlux} mlux"
        )
    

    def led_cleanup(self, can_id):
        self.pcan.send_all_pwm(can_id, 1, 0)
        self.pcan.send_all_pwm(can_id, 2, 0)
        self.pcan.send_all_pwm(can_id, 3, 0)
        self.pcan.send_all_pwm(can_id, 4, 0)

    def apply_styles(self):
        self.setStyleSheet("""
            #root {
                background-color: #EEF2F7;
            }

            QWidget {
                color: #111827;
                font-family: Segoe UI;
                font-size: 14px;
            }

            #header {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7F1D1D,
                    stop:1 #DC2626
                );
                border-radius: 18px;
                padding: 16px;
            }

            #appTitle {
                color: white;
                font-size: 30px;
                font-weight: 800;
                letter-spacing: 0.5px;
            }

            #appSubtitle {
                color: rgba(255, 255, 255, 190);
                font-size: 14px;
                font-weight: 500;
            }

            #headerStatus {
                color: white;
                font-weight: 600;
            }

            QTabWidget::pane {
                border: none;
                background: transparent;
            }

            QTabBar::tab {
                background-color: #DDE3EC;
                color: #334155;
                padding: 10px 22px;
                margin-right: 6px;
                border-radius: 10px;
                font-weight: 600;
            }

            QTabBar::tab:selected {
                background-color: white;
                color: #991B1B;
            }

            #panelCard, #metricCard, #sourceTile {
                background-color: white;
                border: 1px solid #D8DEE8;
                border-radius: 16px;
            }

            #panelCard {
                padding: 14px;
            }

            #sourceTile {
                padding: 10px;
            }

            #sourceTile:hover {
                border: 1px solid #B91C1C;
                background-color: #FFF7F7;
            }

            #cardTitle {
                font-size: 18px;
                font-weight: 800;
                color: #1F2937;
            }

            #tileTitle {
                font-size: 15px;
                font-weight: 800;
                color: #111827;
            }

            #tileSubtitle, #smallMuted {
                color: #64748B;
                font-size: 12px;
            }

            #metricTitle {
                color: #64748B;
                font-size: 13px;
                font-weight: 700;
                text-transform: uppercase;
            }

            #metricValue {
                color: #111827;
                font-size: 42px;
                font-weight: 900;
            }

            #metricUnit {
                color: #64748B;
                font-size: 15px;
                font-weight: 700;
                padding-top: 18px;
            }

            #faultLabel {
                font-size: 14px;
                font-weight: 600;
                color: #334155;
            }

            #sentValue {
                color: #991B1B;
                font-size: 17px;
                font-weight: 800;
            }

            QLineEdit, QSpinBox {
                background-color: #F8FAFC;
                border: 1px solid #CBD5E1;
                border-radius: 10px;
                padding: 11px;
                font-size: 14px;
            }

            QLineEdit:focus, QSpinBox:focus {
                border: 2px solid #DC2626;
                background-color: white;
            }

            QPushButton {
                background-color: #F8FAFC;
                border: 1px solid #CBD5E1;
                border-radius: 10px;
                padding: 10px 16px;
                font-weight: 700;
            }

            QPushButton:hover {
                background-color: #E2E8F0;
            }

            QPushButton:checked {
                background-color: #16A34A;
                color: white;
                border: 1px solid #15803D;
            }

            #primaryButton {
                background-color: #2563EB;
                color: white;
                border: none;
            }

            #primaryButton:hover {
                background-color: #1D4ED8;
            }

            #dangerButton {
                background-color: #DC2626;
                color: white;
                border: none;
            }

            #dangerButton:hover {
                background-color: #B91C1C;
            }

            QTextEdit {
                background-color: #0F172A;
                color: #D1FAE5;
                border-radius: 14px;
                padding: 14px;
                font-family: Consolas;
                font-size: 13px;
            }
                           
            #optometerReadingCard {
                background-color: white;
                border: 1px solid #D8DEE8;
                border-radius: 18px;
                min-width: 160px;
                min-height: 130px;
            }

            #optometerCardTitle {
                color: #64748B;
                font-size: 15px;
                font-weight: 800;
                text-transform: uppercase;
            }

            #optometerValue {
                color: #111827;
                font-size: 40px;
                font-weight: 650;
            }

            #optometerUnit {
                color: #64748B;
                font-size: 18px;
                font-weight: 800;
                padding-top: 16px;
            }

            #optometerStatus {
                color: #64748B;
                font-size: 14px;
            }
        """)
