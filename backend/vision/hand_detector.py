import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        hand_count = 0
        confidence = 0
        landmarks = []

        if results.multi_hand_landmarks:

            hand_count = len(results.multi_hand_landmarks)
            confidence = 100

            h, w, _ = frame.shape

            for hand in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

                for idx, lm in enumerate(hand.landmark):

                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    landmarks.append([idx, x, y])

        return frame, hand_count, confidence, landmarks