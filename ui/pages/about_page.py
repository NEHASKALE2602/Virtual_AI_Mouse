from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtCore import Qt


class AboutPage(QWidget):

    def __init__(self):

        super().__init__()

        layout=QVBoxLayout()

        label=QLabel("About")

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        self.setLayout(layout)