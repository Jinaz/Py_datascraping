# import the necessary packages
from __future__ import print_function
import numpy as np
import pyautogui
import imutils
import cv2 as cv

import argparse

def get_Data_From_Image():
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    image = pyautogui.screenshot()
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    #print(image)
    return image


def get_feature_points(src):
    # -- Step 1: Detect the keypoints using SURF Detector
    orb = cv.ORB_create(nfeatures=500)
    keypoints, descriptors = orb.detectAndCompute(src, None)
    # -- Draw keypoints
    img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
    cv.drawKeypoints(src, keypoints, img_keypoints)
    # -- Show detected (drawn) keypoints
    cv.imshow('ORB Keypoints', img_keypoints)
    cv.waitKey()


def save_image(image):

    cv.imwrite("in_memory_to_disk.png", image)

    # this time take a screenshot directly to disk
    pyautogui.screenshot("straight_to_disk.png")

    # we can then load our screenshot from disk in OpenCV format
    image = cv.imread("straight_to_disk.png")
    cv.imshow("Screenshot", imutils.resize(image, width=1280))
    cv.waitKey()



#if __name__ == "__main__":
#    get_feature_points(get_Data_From_Image())
#    save_image(get_Data_From_Image())