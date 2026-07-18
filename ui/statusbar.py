from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("status")
        self.setFixedHeight(42)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(15, 0, 15, 0)
        layout.setSpacing(25)

        self.camera = QLabel("📷 Camera : Offline")
        self.ai = QLabel("🧠 AI : Idle")
        self.mouse = QLabel("🖱 Mouse : Disabled")
        self.fps = QLabel("⚡ FPS : 0")
        self.gesture = QLabel("✋ Gesture : None")

        for label in [
            self.camera,
            self.ai,
            self.mouse,
            self.fps,
            self.gesture
        ]:
            label.setAlignment(Qt.AlignVCenter)
            layout.addWidget(label)

        layout.addStretch()

        self.version = QLabel("NeuroMouse AI v1.0")

        layout.addWidget(self.version)