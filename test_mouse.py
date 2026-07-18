import pyautogui
import time

print(pyautogui.size())

time.sleep(3)

pyautogui.moveTo(500, 300, duration=1)

print("Done")