import numpy as np
import pyautogui
import time
import cv2 as cv
from time import sleep
from win32api import GetCursorPos
from win32_connectors.VirtualKeycodeLookups import description2keycode as d2k
from win32_connectors.KeyBoardLogger import keyIsUp, keyIsDown

def demo2():
    """Demonstration 2: If the user presses the left mouse button, print the word clicked along with the screen coordinates that were clicked. Then sleep until the key is released."""

    left_mouse = d2k['Left mouse button']
    quit_key = d2k['Q key']

    while keyIsUp(quit_key):
        sleep(.01)
        if keyIsDown(d2k['Left mouse button']):
            x, y = GetCursorPos()
            print(
                'CLICKED {} {}'.format(x, y))
            while keyIsDown(d2k['Left mouse button']):
                sleep(.01)


def screenshot():
    while keyIsUp(81):
        if keyIsDown(189):
            image = pyautogui.screenshot()
            image = np.array(image)
            cv.imwrite("../GTA/DATA/{}.png".format(time.time()), image)
            print("screenshotted")
            while keyIsDown(189):
                sleep(.1)

def screenshot_to_numpyarray():
    image = pyautogui.screenshot()
    return image

