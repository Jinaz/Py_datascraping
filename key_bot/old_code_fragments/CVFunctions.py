import json

import pyautogui
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim


# for 1920,1080 resolution:
# first
# 479,927
# 672,927

# 479,1071
# 672,1071

# second
# 680,927
# 873,927

# 680,1071
# 873,1071

# third
# 881,927
# 1074,927

# 881,1071
# 1074,1071

# fourth
# 1083,927
# 1276,927

# 1083,1071
# 1276,1071

# fifth
# 1284,927
# 1477,927

# 1284,1071
# 1477,1071
def showimg(img):
    imageasarray = np.array(img)

    first = imageasarray[927:1071, 479:672, :]
    firstasimage = cv.cvtColor(first, cv.COLOR_RGB2BGR)
    second = imageasarray[927:1071, 680:873, :]
    secondasimage = cv.cvtColor(second, cv.COLOR_RGB2BGR)
    third = imageasarray[927:1071, 881:1074, :]
    thirdasimage = cv.cvtColor(third, cv.COLOR_RGB2BGR)
    fourth = imageasarray[927:1071, 1083:1276, :]
    fourthasimage = cv.cvtColor(fourth, cv.COLOR_RGB2BGR)
    fifth = imageasarray[927:1071, 1284:1477, :]
    fifthasimage = cv.cvtColor(fifth, cv.COLOR_RGB2BGR)
    DATA = '../TFT/DATA2/'

    # cv.imshow('sliced image', firstasimage)
    cv.imwrite(DATA + 'firstchamp.png', firstasimage)
    # cv.waitKey()
    # cv.imshow('sliced image', secondasimage)
    cv.imwrite(DATA + 'secondchamp.png', secondasimage)
    # cv.waitKey()
    # cv.imshow('sliced image', thirdasimage)
    cv.imwrite(DATA + 'thirdchamp.png', thirdasimage)
    # cv.waitKey()
    # cv.imshow('sliced image', fourthasimage)
    cv.imwrite(DATA + 'fourthchamp.png', fourthasimage)
    # cv.waitKey()
    # cv.imshow('sliced image', fifthasimage)
    cv.imwrite(DATA + 'fifthchamp.png', fifthasimage)
    # cv.waitKey()

    #features1 = get_feature_points(firstasimage)

    return [first, second, third, fourth, fifth]

def imagetoData():
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    image = pyautogui.screenshot()
    print(np.array(image).shape)
    return showimg(image)
    # image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    # print(image)

    # return image

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB,multichannel=True)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()

if __name__ == "__main__":
    images = imagetoData()
    image2 = cv.imread("../TFT/DATA/all/shen.png")

    for img in images:
        compare_images(cv.cvtColor(img, cv.COLOR_RGB2BGR), image2, "")

