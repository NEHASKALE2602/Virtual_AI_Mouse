from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QCheckBox,
    QSlider
)
from PySide6.QtCore import Qt


class SettingCard(QFrame):

    def __init__(self, title):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:rgba(25,30,45,190);
            border-radius:18px;
        }

        QLabel{
            color:white;
            background:transparent;
        }

        QCheckBox{
            color:white;
            font-size:14px;
            spacing:8px;
        }

        QSlider::groove:horizontal{
            height:6px;
            background:#303A52;
            border-radius:3px;
        }

        QSlider::handle:horizontal{
            background:#00D4FF;
            width:16px;
            border-radius:8px;
            margin:-5px 0;
        }
        """)

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(20,20,20,20)

        self.layout.setSpacing(15)

        heading = QLabel(title)

        heading.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        color:#00D4FF;
        """)

        self.layout.addWidget(heading)


class SettingsPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:transparent;
            color:white;
        }
        """)

        root = QVBoxLayout(self)

        root.setContentsMargins(20,20,20,20)

        root.setSpacing(20)

        title = QLabel("Application Settings")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        color:#00D4FF;
        """)

        root.addWidget(title)

        row1 = QHBoxLayout()

        row2 = QHBoxLayout()

        # --------------------------
        # General
        # --------------------------

        general = SettingCard("General")

        general.layout.addWidget(QCheckBox("Start Camera Automatically"))
        general.layout.addWidget(QCheckBox("Enable Mouse Control"))
        general.layout.addWidget(QCheckBox("Enable Gesture Detection"))
        general.layout.addWidget(QCheckBox("Dark Theme"))

        # --------------------------
        # Camera
        # --------------------------

        camera = SettingCard("Camera")

        camera.layout.addWidget(QLabel("Resolution : 640 x 480"))
        camera.layout.addWidget(QLabel("FPS : 30"))
        camera.layout.addWidget(QLabel("Camera : Default Webcam"))

        # --------------------------
        # AI
        # --------------------------

        ai = SettingCard("AI Detection")

        ai.layout.addWidget(QLabel("Detection Confidence"))

        detect = QSlider(Qt.Horizontal)
        detect.setValue(70)

        ai.layout.addWidget(detect)

        ai.layout.addWidget(QLabel("Tracking Confidence"))

        tracking = QSlider(Qt.Horizontal)
        tracking.setValue(70)

        ai.layout.addWidget(tracking)

        # --------------------------
        # Mouse
        # --------------------------

        mouse = SettingCard("Mouse")

        mouse.layout.addWidget(QLabel("Cursor Smoothness"))

        smooth = QSlider(Qt.Horizontal)
        smooth.setValue(70)

        mouse.layout.addWidget(smooth)

        mouse.layout.addWidget(QLabel("Scroll Speed"))

        scroll = QSlider(Qt.Horizontal)
        scroll.setValue(60)

        mouse.layout.addWidget(scroll)

        row1.addWidget(general)
        row1.addWidget(camera)

        row2.addWidget(ai)
        row2.addWidget(mouse)

        root.addLayout(row1)
        root.addLayout(row2)

        root.addStretch()