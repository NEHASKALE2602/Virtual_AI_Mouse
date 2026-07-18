from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)
from PySide6.QtCore import Qt


class InfoCard(QWidget):

    def __init__(self, title, value="--"):
        super().__init__()

        self.setFixedHeight(120)

        self.setStyleSheet("""
        QWidget{

            background:rgba(18,24,40,160);

            border:1px solid rgba(255,255,255,25);

            border-radius:18px;

        }

        QLabel{

            background:transparent;

            color:white;

        }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(18,18,18,18)

        layout.setSpacing(10)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignLeft)

        self.title.setStyleSheet("""
        font-size:14px;
        color:#B8C2E6;
        """)

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
        font-size:28px;
        font-weight:700;
        color:white;
        """)

        layout.addWidget(self.title)

        layout.addStretch()

        layout.addWidget(self.value)

    def setValue(self, value):
        self.value.setText(str(value))