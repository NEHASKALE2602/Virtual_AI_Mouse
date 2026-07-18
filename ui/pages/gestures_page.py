from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtCore import Qt


class GesturesPage(QWidget):

    def __init__(self):

        super().__init__()

        layout=QVBoxLayout()

        label=QLabel("Gestures")

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        self.setLayout(layout)