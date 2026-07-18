from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QSizePolicy
)
from PySide6.QtCore import Qt, QTimer, QDateTime


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("topbar")
        self.setFixedHeight(75)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20, 12, 20, 12)
        layout.setSpacing(15)

        # ===========================
        # Current Page
        # ===========================

        self.title = QLabel("Dashboard")

        self.title.setStyleSheet("""
        QLabel{
            color:white;
            font-size:24px;
            font-weight:700;
        }
        """)

        layout.addWidget(self.title)

        layout.addStretch()

        # ===========================
        # Search Box
        # ===========================

        self.search = QLineEdit()

        self.search.setPlaceholderText("Search...")

        self.search.setFixedWidth(320)

        self.search.setFixedHeight(42)

        layout.addWidget(self.search)

        # ===========================
        # Clock
        # ===========================

        self.clock = QLabel()

        self.clock.setMinimumWidth(170)

        self.clock.setAlignment(Qt.AlignCenter)

        self.clock.setStyleSheet("""
        QLabel{
            color:white;
            font-size:14px;
        }
        """)

        layout.addWidget(self.clock)

        timer = QTimer(self)

        timer.timeout.connect(self.updateClock)

        timer.start(1000)

        self.updateClock()

        # ===========================
        # Notification
        # ===========================

        self.notify = QPushButton("🔔")

        self.notify.setFixedSize(42,42)

        layout.addWidget(self.notify)

        # ===========================
        # Theme
        # ===========================

        self.theme = QPushButton("🌙")

        self.theme.setFixedSize(42,42)

        layout.addWidget(self.theme)

        # ===========================
        # User
        # ===========================

        self.user = QPushButton("👤 Neha")

        self.user.setFixedHeight(42)

        self.user.setMinimumWidth(120)

        layout.addWidget(self.user)

    def updateClock(self):

        now = QDateTime.currentDateTime()

        self.clock.setText(
            now.toString("dd MMM yyyy   hh:mm:ss AP")
        )

    def setTitle(self,title):

        self.title.setText(title)