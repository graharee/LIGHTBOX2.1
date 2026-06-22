"""
gui/widgets.py

Reusable widgets used by the GUI.
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
)


class OptometerReadingCard(QFrame):
    def __init__(self, title: str):
        super().__init__()

        self.setObjectName("optometerReadingCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(10)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("optometerCardTitle")

        value_row = QHBoxLayout()
        value_row.setSpacing(8)

        self.value_label = QLabel("0")
        self.value_label.setObjectName("optometerValue")

        self.unit_label = QLabel("")
        self.unit_label.setObjectName("optometerUnit")

        value_row.addWidget(self.value_label)
        value_row.addWidget(self.unit_label)
        value_row.addStretch()

        status_row = QHBoxLayout()
        status_row.setSpacing(8)

        self.live_dot = QLabel()
        self.live_dot.setFixedSize(9, 9)
        self.live_dot.setObjectName("liveDot")

        self.status_label = QLabel("Live")
        self.status_label.setObjectName("optometerStatus")

        status_row.addWidget(self.live_dot)
        status_row.addWidget(self.status_label)
        status_row.addStretch()

        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addLayout(value_row)
        layout.addLayout(status_row)

        self.set_live(False)

    def set_reading(self, value, unit=""):
        if value is None:
            self.value_label.setText("--")
            self.unit_label.setText("")
            self.set_live(False)
            return
    
        self.value_label.setText(f"{value:.3g}")
        self.unit_label.setText(unit)
        self.set_live(True)

    def set_live(self, live: bool):
        if live:
            self.status_label.setText("Live")
            self.live_dot.setStyleSheet(
                "background-color: #22c55e; border-radius: 4px;"
            )
        else:
            self.status_label.setText("No Read")
            self.live_dot.setStyleSheet(
                "background-color: #ef4444; border-radius: 4px;"
            )

class StatusDot(QLabel):
    def __init__(self, color="gray", size=12):
        super().__init__()
        self.size = size
        self.setFixedSize(size, size)
        self.set_status(color)

    def set_status(self, color):
        colors = {
            "green": "#22C55E",
            "red": "#EF4444",
            "yellow": "#F59E0B",
            "gray": "#94A3B8",
            "blue": "#3B82F6",
        }
        selected = colors.get(color, colors["gray"])
        radius = self.size // 2
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {selected};
                border-radius: {radius}px;
                border: 2px solid rgba(255, 255, 255, 180);
            }}
        """)


class MetricCard(QFrame):
    def __init__(self, title, value="0", status="Live"):
        super().__init__()
        self.setObjectName("metricCard")

        title_label = QLabel(title)
        title_label.setObjectName("metricTitle")

        self.value_label = QLabel(value)
        self.value_label.setObjectName("metricValue")

        unit_label = QLabel(unit)
        unit_label.setObjectName("metricUnit")

        status_dot = StatusDot("green", 10)
        status_label = QLabel(status)
        status_label.setObjectName("smallMuted")

        value_row = QHBoxLayout()
        value_row.addWidget(self.value_label)
        value_row.addWidget(unit_label)
        value_row.addStretch()

        status_row = QHBoxLayout()
        status_row.addWidget(status_dot)
        status_row.addWidget(status_label)
        status_row.addStretch()

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addLayout(value_row)
        layout.addLayout(status_row)


class FaultRow(QWidget):
    def __init__(self, label, color="gray"):
        super().__init__()

        self.dot = StatusDot(color, 12)

        text = QLabel(label)
        text.setObjectName("faultLabel")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 3, 0, 3)
        layout.addWidget(self.dot)
        layout.addWidget(text)
        layout.addStretch()

    def set_status(self, color):
        self.dot.set_status(color)


class LightSourceTile(QFrame):
    selected = Signal(int, str)

    def __init__(self, title, subtitle, driver_number, parent_window=None):
        super().__init__()
        self.setObjectName("sourceTile")
        self.parent_window = parent_window
        self.driver_number = driver_number
        self.title = title

        self.dot = StatusDot("gray", 13)

        title_label = QLabel(title)
        title_label.setObjectName("tileTitle")

        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("tileSubtitle")

        self.button = QPushButton("Enable")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_state)

        header = QHBoxLayout()
        header.addWidget(self.dot)
        header.addWidget(title_label)
        header.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(header)
        layout.addWidget(subtitle_label)
        layout.addSpacing(10)
        layout.addWidget(self.button)

    def toggle_state(self):
        if self.button.isChecked():
            if self.parent_window:
                for tile in self.parent_window.light_tiles:
                    if tile != self:
                        tile.force_off()

            self.button.setText("Disable")
            self.dot.set_status("green")
            self.selected.emit(self.driver_number, self.title)
        else:
            self.force_off()

    def force_off(self):
        self.button.blockSignals(True)
        self.button.setChecked(False)
        self.button.setText("Enable")
        self.dot.set_status("gray")
        self.button.blockSignals(False)


class AdjustmentCard(QFrame):
    send_requested = Signal(object, str)

    def __init__(self, title, description):
        super().__init__()
        self.setObjectName("panelCard")

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        desc_label = QLabel(description)
        desc_label.setObjectName("smallMuted")

        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText("Target mlux")

        self.sent_value = QLabel("0 mlux")
        self.sent_value.setObjectName("sentValue")

        send_button = QPushButton("Send")
        send_button.setObjectName("primaryButton")
        send_button.clicked.connect(self.send_clicked)

        input_row = QHBoxLayout()
        input_row.addWidget(self.target_input)
        input_row.addWidget(send_button)

        sent_label = QLabel("Last sent")
        sent_label.setObjectName("smallMuted")

        sent_row = QHBoxLayout()
        sent_row.addWidget(sent_label)
        sent_row.addStretch()
        sent_row.addWidget(self.sent_value)

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addSpacing(12)
        layout.addLayout(input_row)
        layout.addSpacing(12)
        layout.addLayout(sent_row)

    def send_clicked(self):
        self.send_requested.emit(self, self.target_input.text())

    def set_last_sent(self, text):
        self.sent_value.setText(text)

