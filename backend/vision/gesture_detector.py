class GestureDetector:

    def __init__(self):
        pass

    # -----------------------------
    # Which fingers are UP
    # -----------------------------

    def fingersUp(self, landmarks):

        if len(landmarks) != 21:
            return []

        fingers = []

        # Thumb
        # Thumb
        thumb_tip = landmarks[4]
        thumb_joint = landmarks[2]

        if abs(thumb_tip[1] - thumb_joint[1]) > 25:
            fingers.append(1)
        else:
            fingers.append(0)

        # Index
        fingers.append(1 if landmarks[8][2] < landmarks[6][2] else 0)

        # Middle
        fingers.append(1 if landmarks[12][2] < landmarks[10][2] else 0)

        # Ring
        fingers.append(1 if landmarks[16][2] < landmarks[14][2] else 0)

        # Pinky
        fingers.append(1 if landmarks[20][2] < landmarks[18][2] else 0)
        print("Fingers:", fingers)
        return fingers

    # -----------------------------
    # Detect Gesture
    # -----------------------------

    def detectGesture(self, landmarks):

        fingers = self.fingersUp(landmarks)

        if len(fingers) == 0:
            return "NO_HAND"

        # Open Palm
        if fingers == [1,1,1,1,1]:
            return "OPEN_PALM"

        # Closed Fist
        if fingers == [0,0,0,0,0]:
            return "DRAG"

        # Right Click
        
        if fingers == [0,1,1,0,0]:

            print(">>> RIGHT CLICK DETECTED <<<")

            return "RIGHT_CLICK"

        # Scroll
        if fingers == [0,1,0,0,0]:
            return "SCROLL"

        return "UNKNOWN"