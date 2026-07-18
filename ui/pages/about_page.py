from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QGridLayout
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

        heading = QLabel(title)

        heading.setStyleSheet("""
        font-size:15px;
        color:#A0A8C0;
        """)

        valueLabel = QLabel(value)

        valueLabel.setWordWrap(True)

        valueLabel.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        color:#00D4FF;
        """)

        layout.addWidget(heading)
        layout.addWidget(valueLabel)


class AboutPage(QWidget):

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

        # ======================================
        # TITLE
        # ======================================

        title = QLabel("About NeuroMouse AI")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        color:#00D4FF;
        """)

        root.addWidget(title)

        # ======================================
        # DESCRIPTION
        # ======================================

        description = QLabel(
            "NeuroMouse AI is an AI-powered virtual mouse application "
            "that enables users to control their computer through "
            "real-time hand gesture recognition using computer vision. "
            "The project combines artificial intelligence with an "
            "intuitive desktop interface to deliver a fast, accurate, "
            "and touch-free computing experience."
        )

        description.setWordWrap(True)

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet("""
        font-size:16px;
        color:#C9D4F5;
        """)

        root.addWidget(description)

        # ======================================
        # INFORMATION CARDS
        # ======================================

        grid = QGridLayout()

        grid.setSpacing(20)

        grid.addWidget(
            InfoCard(
                "Project",
                "NeuroMouse AI"
            ),
            0,
            0
        )

        grid.addWidget(
            InfoCard(
                "Version",
                "Version 1.0"
            ),
            0,
            1
        )

        grid.addWidget(
            InfoCard(
                "Technology",
                "Python\nOpenCV\nMediaPipe\nPySide6\nPyAutoGUI"
            ),
            1,
            0
        )

        grid.addWidget(
            InfoCard(
                "Features",
                "• Mouse Movement\n"
                "• Left Click\n"
                "• Scroll\n"
                "• Drag & Drop"
            ),
            1,
            1
        )

        root.addLayout(grid)

        # ======================================
        # DEVELOPER
        # ======================================

        developerTitle = QLabel("Developer")

        developerTitle.setStyleSheet("""
        font-size:22px;
        font-weight:bold;
        color:#00D4FF;
        """)

        root.addWidget(developerTitle)

        developerInfo = QLabel(
            "Developed by Neha Kale\n\n"
            "Computer Engineering Student\n"
            "Artificial Intelligence & Machine Learning Project\n\n"
            "NeuroMouse AI demonstrates real-time hand tracking, "
            "gesture recognition, and virtual mouse control using "
            "modern computer vision technologies."
        )

        developerInfo.setWordWrap(True)

        developerInfo.setStyleSheet("""
        font-size:15px;
        color:#C9D4F5;
        """)

        root.addWidget(developerInfo)

        root.addStretch()