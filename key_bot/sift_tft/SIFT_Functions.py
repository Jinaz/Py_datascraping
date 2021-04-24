import cv2 as cv2
import numpy as np
import win32_connectors.screenshotter as sc
import time
import matplotlib.pyplot as plt

"""
gray image as input and get keypoints, descriptors as output
"""


def getKeypoints(gray):
    # create sift
    sift = cv2.xfeatures2d.SIFT_create(50)

    # get keypoints and descriptors
    kp, desc = sift.detectAndCompute(gray, None)

    return kp, desc


"""
compare descriptors/vectors of image 1 and image 2
"""


def compare_keypoints(desc1, desc2):
    # feature matching
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)

    return matches

def bruteforceCompare():
    pass


"""
import 2 colorimages: cv2 Materials
"""


def full_comparison_flow(colorimage1, colorimage2):
    img1 = cv2.cvtColor(colorimage1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(colorimage2, cv2.COLOR_BGR2GRAY)

    kp1, desc1 = getKeypoints(img1)
    kp2, desc2 = getKeypoints(img2)

    matches = compare_keypoints(desc1, desc2)
    print(desc1.shape)
    print(desc2.shape)
    print(kp1)
    print(kp2)

    return kp1, kp2, desc1, desc2, matches


def test_funciton():
    im1 = cv2.imread("../tft/DATA/1/cait.png")
    im2 = cv2.imread("../tft/DATA/1/fiora.png")
    im3 = cv2.imread("../tft/DATA/1/k6.png")
    im4 = cv2.imread("../tft/DATA/1/graves.png")
    im5 = cv2.imread("../tft/DATA/1/leona.png")

    imarray = [im1, im2, im3, im4, im5]

    for i in range(len(imarray)):
        for j in range(len(imarray)):
            a = imarray[i]
            b = imarray[j]

            kp1, kp2, desc1, desc2, matches = full_comparison_flow(a, b)
            print(len(matches))
            img3 = cv2.drawMatches(a, kp1, b, kp2, matches[:100], b, flags=2)
            plt.imshow(img3), plt.show()

        #squares = np.square(np.array(kp1-kp2))
        #e = np.sum(squares)
        #print(e)


test_funciton()
