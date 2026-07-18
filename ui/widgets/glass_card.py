from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class GlassCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("glass")

        self.setStyleSheet("""
        QFrame#glass{

            background:rgba(15,18,30,150);

            border:1px solid rgba(255,255,255,25);

            border-radius:20px;

        }
        """)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(35)

        shadow.setOffset(0,0)

        shadow.setColor(QColor(0,212,255,80))

        self.setGraphicsEffect(shadow)

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(20,20,20,20)

        self.layout.setSpacing(15)