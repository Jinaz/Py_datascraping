import pyautogui

import cv2 as cv
import numpy as np



def screenshotToData(filename):
    #convert array to opencv standards in BGR
    image = pyautogui.screenshot()

    cv.imwrite(filename, np.array(image))

screenshotToData('BG5.png')