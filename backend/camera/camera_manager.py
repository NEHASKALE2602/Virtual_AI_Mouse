import cv2
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

from backend.vision.hand_detector import HandDetector


class CameraThread(QThread):

    frameCaptured = Signal(QImage)
    statusChanged = Signal(str)

    fpsChanged = Signal(int)
    handChanged = Signal(int)
    confidenceChanged = Signal(int)

    def __init__(self):

        super().__init__()

        self.running = False

        self.detector = HandDetector()

    def run(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            self.statusChanged.emit("Camera Error")

            return

        self.running = True

        previous = time.time()

        self.statusChanged.emit("Camera Online")

        while self.running:

            success, frame = cap.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            frame, hands, confidence, landmarks = self.detector.detect(frame)
            if len(landmarks) > 9:

                indexFinger = landmarks[8]

                x = indexFinger[1]

                y = indexFinger[2]

                cv2.circle(
                    frame,
                    (x, y),
                    12,
                    (0, 255, 0),
                    cv2.FILLED
                )
            current = time.time()

            fps = int(1 / (current - previous))

            previous = current

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = rgb.shape

            image = QImage(
                rgb.data,
                w,
                h,
                ch * w,
                QImage.Format_RGB888
            ).copy()

            self.frameCaptured.emit(image)

            self.fpsChanged.emit(fps)

            self.handChanged.emit(hands)

            self.confidenceChanged.emit(confidence)

        cap.release()

        self.statusChanged.emit("Camera Offline")

    def stop(self):

        self.running = False

        self.wait()