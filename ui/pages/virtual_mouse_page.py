from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame
)
from PySide6.QtCore import Qt


class InfoCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:rgba(25,30,45,190);
            border-radius:18px;
        }

        QLabel{
            background:transparent;
            color:white;
        }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20,20,20,20)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("""
        font-size:15px;
        color:#A0A8C0;
        """)

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
        font-size:24px;
        font-weight:bold;
        color:#00D4FF;
        """)

        layout.addWidget(self.title)

        layout.addWidget(self.value)


class VirtualMousePage(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:transparent;
            color:white;
        }

        QLabel{
            background:transparent;
            color:white;
        }
        """)

        root = QVBoxLayout(self)

        root.setContentsMargins(20,20,20,20)

        root.setSpacing(20)

        title = QLabel("Virtual AI Mouse")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        color:#00D4FF;
        """)

        root.addWidget(title)

        # ==========================
        # STATUS
        # ==========================

        self.status = QLabel("🟢 AI Mouse Active")

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setFixedHeight(70)

        self.status.setStyleSheet("""
        QLabel{
            background:rgba(25,30,45,190);
            border-radius:18px;
            font-size:22px;
            font-weight:bold;
            color:#00FF99;
        }
        """)

        root.addWidget(self.status)

        # ==========================
        # INFO CARDS
        # ==========================

        grid = QGridLayout()

        grid.setSpacing(20)

        self.gestureCard = InfoCard(
            "Current Gesture",
            "OPEN PALM"
        )

        self.modeCard = InfoCard(
            "Current Mode",
            "Mouse Control"
        )

        self.handCard = InfoCard(
            "Hands",
            "1"
        )

        self.aiCard = InfoCard(
            "AI Status",
            "Running"
        )

        grid.addWidget(self.gestureCard,0,0)
        grid.addWidget(self.modeCard,0,1)
        grid.addWidget(self.handCard,1,0)
        grid.addWidget(self.aiCard,1,1)

        root.addLayout(grid)

        # ==========================
        # FEATURES
        # ==========================

        features = QFrame()

        features.setStyleSheet("""
        QFrame{
            background:rgba(25,30,45,190);
            border-radius:18px;
        }

        QLabel{
            background:transparent;
        }
        """)

        layout = QVBoxLayout(features)

        layout.setContentsMargins(20,20,20,20)

        heading = QLabel("Available Features")

        heading.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#00D4FF;
        """)

        layout.addWidget(heading)

        layout.addWidget(QLabel("✅ Mouse Movement"))
        layout.addWidget(QLabel("✅ Left Click"))
        layout.addWidget(QLabel("✅ Scroll"))
        layout.addWidget(QLabel("✅ Drag & Drop"))
        layout.addWidget(QLabel("⬜ Right Click (Coming Soon)"))

        root.addWidget(features)

        # ==========================
        # USER GUIDE
        # ==========================

        guide = QFrame()

        guide.setStyleSheet("""
        QFrame{
            background:rgba(25,30,45,190);
            border-radius:18px;
        }

        QLabel{
            background:transparent;
        }
        """)

        guideLayout = QVBoxLayout(guide)

        guideLayout.setContentsMargins(20,20,20,20)

        title2 = QLabel("Gesture Guide")

        title2.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#00D4FF;
        """)

        guideLayout.addWidget(title2)

        guideLayout.addWidget(QLabel("🖐 Open Palm → Move Mouse"))
        guideLayout.addWidget(QLabel("🤏 Thumb + Index → Left Click"))
        guideLayout.addWidget(QLabel("✊ Closed Fist → Drag & Drop"))
        guideLayout.addWidget(QLabel("☝ Index Finger → Scroll"))

        root.addWidget(guide)

        root.addStretch()

    # --------------------------------
    # Live Updates (Future)
    # --------------------------------

    def updateGesture(self, gesture):

        self.gestureCard.value.setText(gesture)

    def updateHands(self, hands):

        self.handCard.value.setText(str(hands))

    def updateStatus(self, status):

        self.aiCard.value.setText(status)