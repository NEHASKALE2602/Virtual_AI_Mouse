from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class PrimaryButton(QPushButton):

    def __init__(self, text):
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)

        self.setMinimumHeight(45)

        self.setStyleSheet("""
        QPushButton{

            background:qlineargradient(
                x1:0,y1:0,
                x2:1,y2:0,
                stop:0 #6C63FF,
                stop:1 #00D4FF
            );

            border:none;

            border-radius:12px;

            color:white;

            font-size:15px;

            font-weight:600;

        }

        QPushButton:hover{

            background:#7C74FF;

        }

        QPushButton:pressed{

            background:#5148E5;

        }
        """)