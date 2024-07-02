import pyautogui
import time


def press_shift():
    pyautogui.keyDown('shift')
    pyautogui.keyUp('shift')


while True:
    press_shift()
    time.sleep(300)
