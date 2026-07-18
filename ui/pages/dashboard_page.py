from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:transparent;
            border:none;
        }

        QLabel{
            background:transparent;
            color:white;
        }
        """)

        root = QVBoxLayout(self)

        root.setContentsMargins(60,120,0,0)

        root.setSpacing(15)

        root.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # ===========================================
        # TITLE
        # ===========================================

        title = QLabel("Welcome to NeuroMouse AI")

        title.setStyleSheet("""
        font-size:40px;
        font-weight:700;
        color:white;
        """)

        root.addWidget(title)

        # ===========================================
        # SUBTITLE
        # ===========================================

        subtitle = QLabel(
            "Experience the next generation of human–computer interaction "
            "with AI-powered gesture recognition."
        )

        subtitle.setWordWrap(True)

        subtitle.setMaximumWidth(700)

        subtitle.setStyleSheet("""
        font-size:20px;
        color:#C9D4F5;
        """)

        root.addWidget(subtitle)

        # ===========================================
        # DESCRIPTION
        # ===========================================

        description = QLabel(
            "NeuroMouse AI transforms natural hand movements into precise "
            "cursor control, enabling smooth navigation, intelligent gesture "
            "commands, and a completely touch-free desktop experience using "
            "real-time computer vision and artificial intelligence."
        )

        description.setWordWrap(True)

        description.setMaximumWidth(760)

        description.setStyleSheet("""
        font-size:16px;
        line-height:28px;
        color:#9BA8C7;
        """)

        root.addWidget(description)

        root.addStretch()