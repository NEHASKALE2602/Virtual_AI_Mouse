from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class SectionTitle(QLabel):

    def __init__(self, text):
        super().__init__(text)

        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.setStyleSheet("""
        QLabel{
            color:#00D4FF;
            font-size:15px;
            font-weight:700;
            padding:6px;
            background:transparent;
        }
        """)