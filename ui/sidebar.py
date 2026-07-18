from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)
from PySide6.QtCore import Qt


class SideBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(260)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 25, 20, 25)
        layout.setSpacing(10)

        # ---------------- Logo ---------------- #

        logo = QLabel("◎")
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("logo")

        title = QLabel("NeuroMouse AI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:22px;
            font-weight:700;
            color:white;
        """)

        subtitle = QLabel("AI Gesture Controller")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            color:#9AA4C7;
            font-size:11px;
        """)

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(30)

        # ---------------- Navigation ---------------- #

        self.dashboard = QPushButton("🏠  Dashboard")
        self.camera = QPushButton("📷  Camera")
        self.mouse = QPushButton("🖱  Virtual Mouse")
        self.gesture = QPushButton("✋  Gesture Studio")
        self.settings = QPushButton("⚙  Settings")
        self.about = QPushButton("ℹ  About")

        buttons = [
            self.dashboard,
            self.camera,
            self.mouse,
            self.gesture,
            self.settings,
            self.about
        ]

        for btn in buttons:

            btn.setCursor(Qt.PointingHandCursor)

            btn.setMinimumHeight(50)

            layout.addWidget(btn)

        self.dashboard.setStyleSheet("""
            background:#6C63FF;
            color:white;
            border-radius:12px;
            padding-left:18px;
            font-size:15px;
            font-weight:600;
        """)

        layout.addStretch()

        version = QLabel("Version 1.0")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("""
            color:#7D88A8;
            font-size:11px;
        """)

        layout.addWidget(version)