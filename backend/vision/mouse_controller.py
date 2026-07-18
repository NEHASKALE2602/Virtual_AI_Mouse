import pyautogui


class MouseController:

    def __init__(self):

        pyautogui.PAUSE = 0
        pyautogui.FAILSAFE = True

        self.dragMode = False
        self.leftClickReady = True
        self.rightClickReady = True

    # -------------------------
    # Move Mouse
    # -------------------------

    def move(self, x, y):

        print(f"Moving Mouse -> X:{x:.0f} Y:{y:.0f}")

        pyautogui.moveTo(int(x), int(y), duration=0)

    # -------------------------
    # Left Click
    # -------------------------

    def leftClick(self):

        if self.leftClickReady:

            pyautogui.click()

            self.leftClickReady = False

    def resetLeftClick(self):

        self.leftClickReady = True

    # -------------------------
    # Right Click
    # -------------------------

    def rightClick(self):

        if self.rightClickReady:

            pyautogui.rightClick()

            self.rightClickReady = False

    def resetRightClick(self):

        self.rightClickReady = True

    # -------------------------
    # Drag
    # -------------------------

    def startDrag(self):

        if not self.dragMode:

            pyautogui.mouseDown()

            self.dragMode = True

    def stopDrag(self):

        if self.dragMode:

            pyautogui.mouseUp()

            self.dragMode = False

    # -------------------------
    # Scroll
    # -------------------------

    def scrollUp(self):

        pyautogui.scroll(80)

    def scrollDown(self):

        pyautogui.scroll(-80)