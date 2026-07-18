from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QGridLayout
)
from PySide6.QtCore import Qt


class GestureCard(QFrame):

    def __init__(self, emoji, title, description):

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

        icon = QLabel(emoji)
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("font-size:38px;")

        name = QLabel(title)
        name.setAlignment(Qt.AlignCenter)
        name.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        color:#00D4FF;
        """)

        info = QLabel(description)
        info.setAlignment(Qt.AlignCenter)
        info.setWordWrap(True)
        info.setStyleSheet("""
        font-size:13px;
        color:#C8C8C8;
        """)

        layout.addWidget(icon)
        layout.addWidget(name)
        layout.addWidget(info)


class GesturesPage(QWidget):

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

        title = QLabel("Gesture Library")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        color:#00D4FF;
        """)

        root.addWidget(title)

        self.liveGesture = QLabel("🖐 OPEN PALM")

        self.liveGesture.setAlignment(Qt.AlignCenter)

        self.liveGesture.setFixedHeight(90)

        self.liveGesture.setStyleSheet("""
        QLabel{
            background:rgba(25,30,45,200);
            border-radius:18px;
            font-size:26px;
            font-weight:bold;
            color:#00FF99;
        }
        """)

        root.addWidget(self.liveGesture)

        grid = QGridLayout()

        grid.setSpacing(20)

        grid.addWidget(
            GestureCard(
                "🖐",
                "Open Palm",
                "Move Mouse Cursor"
            ),
            0,
            0
        )

        grid.addWidget(
            GestureCard(
                "🤏",
                "Thumb + Index",
                "Left Click"
            ),
            0,
            1
        )

        grid.addWidget(
            GestureCard(
                "✊",
                "Closed Fist",
                "Drag & Drop"
            ),
            1,
            0
        )

        grid.addWidget(
            GestureCard(
                "☝",
                "Index Finger",
                "Scroll"
            ),
            1,
            1
        )

        container = QWidget()

        container.setLayout(grid)

        root.addWidget(container)

        root.addStretch()

    def updateGesture(self, gesture):

        mapping = {
            "OPEN_PALM": "🖐 OPEN PALM",
            "RIGHT_CLICK": "✌ RIGHT CLICK",
            "DRAG": "✊ DRAG",
            "SCROLL": "☝ SCROLL",
            "UNKNOWN": "❓ UNKNOWN",
            "NO_HAND": "🚫 NO HAND"
        }

        self.liveGesture.setText(
            mapping.get(gesture, gesture)
        )