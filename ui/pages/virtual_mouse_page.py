from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtCore import Qt


class VirtualMousePage(QWidget):

    def __init__(self):

        super().__init__()

        layout=QVBoxLayout()

        label=QLabel("Virtual Mouse")

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        self.setLayout(layout)