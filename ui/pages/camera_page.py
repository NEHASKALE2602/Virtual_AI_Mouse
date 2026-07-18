from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from backend.camera.camera_manager import CameraThread
class CameraPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:transparent;
            color:white;
        }

        QPushButton{
            background:#6C63FF;
            border:none;
            border-radius:12px;
            color:white;
            font-size:15px;
            font-weight:bold;
            padding:12px;
        }

        QPushButton:hover{
            background:#8078FF;
        }
        QPushButton:disabled{

            background:#2E3448;

            color:#B0B0B0;

        }
        QLabel{
            background:transparent;
            color:white;
        }
        """)


        mainLayout = QHBoxLayout(self)

        mainLayout.setContentsMargins(0,0,0,0)

        mainLayout.setSpacing(20)

        # ===========================
        # LEFT PANEL
        # ===========================

        leftPanel = QWidget()

        leftPanel.setFixedWidth(300)

        leftPanel.setStyleSheet("""
        QWidget{

            background:rgba(25,30,45,180);

            border-radius:18px;

        }
        """)

        leftLayout = QVBoxLayout(leftPanel)

        leftLayout.setContentsMargins(20,20,20,20)

        leftLayout.setSpacing(15)

        title = QLabel("CAMERA CONTROL")

        title.setStyleSheet("""
        font-size:20px;
        font-weight:bold;
        color:#00D4FF;
        """)

        leftLayout.addWidget(title)

        self.startButton = QPushButton("▶ Start Camera")

        self.stopButton = QPushButton("■ Stop Camera")
        self.stopButton.setEnabled(False)
        self.cameraThread = CameraThread()

        self.startButton.clicked.connect(self.startCamera)
        self.stopButton.clicked.connect(self.stopCamera)

        self.cameraThread.frameCaptured.connect(self.updateFrame)
        self.cameraThread.statusChanged.connect(self.updateStatus)
        self.cameraThread.fpsChanged.connect(self.updateFPS)

        self.cameraThread.handChanged.connect(self.updateHands)

        self.cameraThread.confidenceChanged.connect(self.updateConfidence)

        leftLayout.addWidget(self.startButton)

        leftLayout.addWidget(self.stopButton)

        leftLayout.addSpacing(20)

        self.aiLabel = QLabel("AI Confidence : --")

        self.fpsLabel = QLabel("FPS : --")

        self.handLabel = QLabel("Hands : --")

        self.gestureLabel = QLabel("Gesture : --")

        self.statusLabel = QLabel("Status : Offline")

        for widget in [

            self.aiLabel,

            self.fpsLabel,

            self.handLabel,

            self.gestureLabel,

            self.statusLabel

        ]:

            widget.setMinimumHeight(35)

            widget.setStyleSheet("""

            QLabel{

                background:#20263B;

                border-radius:10px;

                padding-left:12px;

                font-size:14px;

            }

            """)

            leftLayout.addWidget(widget)

        leftLayout.addStretch()

        # ===========================
        # RIGHT PANEL
        # ===========================

        rightPanel = QWidget()

        rightLayout = QVBoxLayout(rightPanel)

        rightLayout.setContentsMargins(0,0,0,0)

        self.cameraLabel = QLabel()

        self.cameraLabel.setAlignment(Qt.AlignCenter)

        self.cameraLabel.setText("LIVE CAMERA")

        self.cameraLabel.setStyleSheet("""

        QLabel{

            background:rgba(20,25,40,170);

            border:2px dashed #3A4B7A;

            border-radius:20px;

            font-size:28px;

            font-weight:bold;

        }

        """)

        self.cameraLabel.setSizePolicy(

            QSizePolicy.Expanding,

            QSizePolicy.Expanding

        )

        rightLayout.addWidget(self.cameraLabel)

        mainLayout.addWidget(leftPanel)

        mainLayout.addWidget(rightPanel)
        # =====================================
    # CAMERA FUNCTIONS
    # =====================================

    def startCamera(self):

        if self.cameraThread.isRunning():
            return

    # Disable Start Button
        self.startButton.setEnabled(False)

    # Enable Stop Button
        self.stopButton.setEnabled(True)

    # Change Button Text
        self.startButton.setText("⏳ Starting...")

    # Show Status
        self.statusLabel.setText("Status : Starting Camera...")

    # Start Camera
        self.cameraThread.start()

    def stopCamera(self):

        self.cameraThread.stop()

        self.startButton.setEnabled(True)

        self.startButton.setText("▶ Start Camera")

        self.stopButton.setEnabled(False)

        self.statusLabel.setText("Status : Camera Offline")

        self.cameraLabel.clear()

        self.cameraLabel.setText("LIVE CAMERA")

    def updateFrame(self, image):

        pixmap = QPixmap.fromImage(image)

        self.cameraLabel.setPixmap(pixmap)

        self.cameraLabel.setScaledContents(False)

        self.cameraLabel.setAlignment(Qt.AlignCenter)

    def updateStatus(self, status):

        self.statusLabel.setText(f"Status : {status}")

        if status == "Camera Online":

            self.startButton.setText("🟢 Camera Running")

            self.startButton.setEnabled(False)

            self.stopButton.setEnabled(True)

        elif status == "Camera Offline":

            self.startButton.setText("▶ Start Camera")

            self.startButton.setEnabled(True)

            self.stopButton.setEnabled(False)

        elif status == "Camera Error":

            self.startButton.setText("▶ Start Camera")

            self.startButton.setEnabled(True)

            self.stopButton.setEnabled(False)
    def updateFPS(self, fps):

        self.fpsLabel.setText(f"FPS : {fps}")


    def updateHands(self, hands):

        self.handLabel.setText(f"Hands : {hands}")


    def updateConfidence(self, confidence):

        self.aiLabel.setText(f"AI Confidence : {confidence}%")