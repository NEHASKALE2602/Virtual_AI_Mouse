from PySide6.QtWidgets import QWidget, QVBoxLayout


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background: transparent;
            border:none;
        }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0,0,0,0)

        layout.setSpacing(0)