import cv2
import time
import math
import pyautogui
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

from backend.vision.hand_detector import HandDetector
from backend.vision.gesture_detector import GestureDetector
from backend.vision.mouse_controller import MouseController


class CameraThread(QThread):

    # ----------------------------
    # Signals
    # ----------------------------

    frameCaptured = Signal(QImage)

    statusChanged = Signal(str)

    fpsChanged = Signal(int)

    handChanged = Signal(int)

    confidenceChanged = Signal(int)

    gestureChanged = Signal(str)

    # ----------------------------
    # Constructor
    # ----------------------------

    def __init__(self):

        super().__init__()

        self.running = False

        self.detector = HandDetector()

        self.gesture = GestureDetector()

        self.mouse = MouseController()

    # ----------------------------
    # Camera Thread
    # ----------------------------

    def run(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            self.statusChanged.emit("Camera Error")

            return

        self.running = True

        self.statusChanged.emit("Camera Online")

        previous = time.time()

        screenWidth, screenHeight = pyautogui.size()

        prevX = 0

        prevY = 0

        smoothening = 7

        clickCooldown = False

        rightClickReady = True


        while self.running:
            success, frame = cap.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            frame, hands, confidence, landmarks = self.detector.detect(frame)

            self.handChanged.emit(hands)

            self.confidenceChanged.emit(confidence)

            if len(landmarks) == 21:

                indexFinger = landmarks[8]
                thumbFinger = landmarks[4]

                x = indexFinger[1]
                y = indexFinger[2]

                thumbX = thumbFinger[1]
                thumbY = thumbFinger[2]

                cameraWidth = frame.shape[1]
                cameraHeight = frame.shape[0]

                targetX = (x / cameraWidth) * screenWidth
                targetY = (y / cameraHeight) * screenHeight

                currentX = prevX + (targetX - prevX) / smoothening
                currentY = prevY + (targetY - prevY) / smoothening

                currentX = max(0, min(currentX, screenWidth - 1))
                currentY = max(0, min(currentY, screenHeight - 1))

                distance = math.hypot(
                    thumbX - x,
                    thumbY - y
                )

                gesture = self.gesture.detectGesture(landmarks)
                self.gestureChanged.emit(gesture)

                cv2.circle(
                    frame,
                    (x, y),
                    12,
                    (0, 255, 255),
                    cv2.FILLED
                )

                cv2.putText(
                    frame,
                    gesture,
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )
                print("Gesture:", gesture)
                # ============================================
                # OPEN PALM -> MOVE MOUSE
                # ============================================

                self.mouse.move(currentX, currentY)

                prevX = currentX
                prevY = currentY

                self.mouse.stopDrag()

                self.mouse.resetLeftClick()

                self.mouse.resetRightClick()

                # ============================================
                # LEFT CLICK
                # Thumb + Index Touch
                # ============================================

                if distance < 35:

                    if clickCooldown is False:

                        self.mouse.leftClick()

                        clickCooldown = True

                else:

                    clickCooldown = False

                    self.mouse.resetLeftClick()

                # ============================================
                # RIGHT CLICK
                # ============================================

                if gesture == "RIGHT_CLICK":

                    if rightClickReady:

                        self.mouse.rightClick()

                        rightClickReady = False

                else:

                    rightClickReady = True

                    self.mouse.resetRightClick()

                # ============================================
                # DRAG & DROP
                # Closed Fist = Hold Mouse
                # Open Palm = Release Mouse
                # ============================================

                if gesture == "DRAG":

                    self.mouse.startDrag()

                    self.mouse.move(currentX, currentY)

                    prevX = currentX
                    prevY = currentY

                elif gesture == "OPEN_PALM":

                    self.mouse.stopDrag()

                # ============================================
                # SCROLL
                # ============================================

                if gesture == "SCROLL":

                    if y < cameraHeight // 2:

                        self.mouse.scrollUp()

                    else:

                        self.mouse.scrollDown()
                                    # ============================================
            # FPS
            # ============================================

            current = time.time()

            fps = int(1 / max(current - previous, 0.0001))

            previous = current

            self.fpsChanged.emit(fps)

            # ============================================
            # Convert Frame to QImage
            # ============================================

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

        # ============================================
        # Release Camera
        # ============================================

        cap.release()

        self.statusChanged.emit("Camera Offline")

    # ============================================
    # Stop Thread
    # ============================================

    def stop(self):

        self.running = False

        self.wait()