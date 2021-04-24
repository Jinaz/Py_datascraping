import pyautogui
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def screenshotToData():
    #convert array to opencv standards in BGR
    image = pyautogui.screenshot()
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    return image

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err

def prefilter(img, outimg="gray"):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    if outimg == "invert":
        return invert
    if outimg == "opening":
        return opening
    if outimg == "thresh":
        return thresh
    if outimg == "blur":
        return blur
    return gray

def cutImage(img,x1,x2,y1,y2):
    return img[y1:y2,x1:x2,:]

def loadImage(imagename):
    return cv.imread(imagename)

def imageToData():
    image = pyautogui.screenshot()
    image = np.array(image)
    return image

def compare_CV_images(imageA, imageB, title=''):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, multichannel=True)
    return m,s

def compare_CV_images_with(imageA, imageB, title=''):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, multichannel=True)
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

    return m,s

