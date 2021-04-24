import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2 as cv
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from imageFunctions.AmbrosioTortorelliMinimizer import *

def mfs():
    img = cv.imread('../tft/testdata/test0.png')
    img = img[921:1071, 472:1479, :]
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    solver = AmbrosioTortorelliMinimizer(img)
    img, edges = solver.minimize()
    #plt.subplot(121), plt.imshow(img, cmap='gray')
    #plt.subplot(122), plt.imshow(edges, cmap='gray')
    #plt.show()

    #res = cv2.bitwise_and(img,img, mask= edges)

    #dst = cv2.addWeighted(img, 1, edges, 1, 0)

    #cv2.imshow('sas', res)
    redImg = np.zeros(edges.shape, edges.dtype)
    redImg[:, :] = (0, 0, 255)

    redMask = cv2.bitwise_and(redImg, redImg, mask=edges)
    cv.addWeighted(redMask, 1, img, 1, 0, img)
    cv.waitKey()

def orb_detection(outimg=None):
    img = cv.imread('../tft/testdata/test0.png')
    img = img[921:1071, 472:1479,:]
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Initiate STAR detector
    orb = cv.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img, None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    img2 = cv.drawKeypoints(img, kp,outimg, color=(0, 255, 0), flags=0)
    plt.imshow(img2), plt.show()

def cannyEdge():
    img = cv.imread('../tft/testdata/test0.png')
    img = img[921:1071, 472:1479, :]
    edges = cv.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def chanvese():
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import data, img_as_float
    from skimage.segmentation import (morphological_chan_vese,
                                      morphological_geodesic_active_contour,
                                      inverse_gaussian_gradient,
                                      checkerboard_level_set)

    def store_evolution_in(lst):
        """Returns a callback function to store the evolution of the level sets in
        the given list.
        """

        def _store(x):
            lst.append(np.copy(x))

        return _store

    img = cv.imread("../tft/testdata/test0.png")
    img = img[921:1071, 472:1479, :]
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    init_ls = checkerboard_level_set(img.shape, 6)
    evolution = []
    callback = store_evolution_in(evolution)
    ls = morphological_chan_vese(img, 35, init_level_set=init_ls, smoothing=3,
                                 iter_callback=callback)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    ax = axes.flatten()

    ax[0].imshow(img, cmap="gray")
    ax[0].set_axis_off()
    ax[0].contour(ls, [0.5], colors='r')
    ax[0].set_title("Morphological ACWE segmentation", fontsize=12)

    ax[1].imshow(ls, cmap="gray")
    ax[1].set_axis_off()
    contour = ax[1].contour(evolution[2], [0.5], colors='g')
    contour.collections[0].set_label("Iteration 2")
    contour = ax[1].contour(evolution[7], [0.5], colors='y')
    contour.collections[0].set_label("Iteration 7")
    contour = ax[1].contour(evolution[-1], [0.5], colors='r')
    contour.collections[0].set_label("Iteration 35")
    ax[1].legend(loc="upper right")
    title = "Morphological ACWE evolution"
    ax[1].set_title(title, fontsize=12)

    plt.show()

def skVersion():
    img = cv.imread("../tft/testdata/test0.png")
    img = img[921:1071, 472:1479, :]
    img = rgb2gray(img)

    s = np.linspace(0, 2 * np.pi, 400)
    r = 100 + 100 * np.sin(s)
    c = 220 + 100 * np.cos(s)
    init = np.array([r, c]).T

    snake = active_contour(gaussian(img, 3),
                           init, alpha=0.015, beta=10, gamma=0.001)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(img, cmap=plt.cm.gray)
    ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
    ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])

    plt.show()


def cv_version():
    #img = np.zeros((200, 200), dtype=np.uint8)
    #img[50:150, 50:150] = 255
    img = cv.imread("../tft/testdata/test0.png")
    img = img[921:1071, 472:1479, :]
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    edges = cv.Canny(img,100,200)

    image, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE,
                                                  cv.CHAIN_APPROX_SIMPLE)

    color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    img = cv.drawContours(color, contours, -1, (0, 255, 0), 2)
    cv.imshow("contours", color)
    cv.waitKey()

#cv_version()
#chanvese()
#cannyEdge()
#orb_detection()
mfs()