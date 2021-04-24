import json
import glob
import time
import pyautogui
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim


def screen_shot():
    image = pyautogui.screenshot()
    imageasarray = np.array(image)

    image1 = imageasarray[927:1071, 479:672, :]
    image2 = imageasarray[927:1071, 680:873, :]
    image3 = imageasarray[927:1071, 881:1074, :]
    image4 = imageasarray[927:1071, 1083:1276, :]
    image5 = imageasarray[927:1071, 1284:1477, :]

    cvtimage1 = cv.cvtColor(image1, cv.COLOR_RGB2BGR)
    cvtimage2 = cv.cvtColor(image2, cv.COLOR_RGB2BGR)
    cvtimage3 = cv.cvtColor(image3, cv.COLOR_RGB2BGR)
    cvtimage4 = cv.cvtColor(image4, cv.COLOR_RGB2BGR)
    cvtimage5 = cv.cvtColor(image5, cv.COLOR_RGB2BGR)

    return [cvtimage1, cvtimage2, cvtimage3, cvtimage4, cvtimage5]


def save_screen_shot(index):
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    image = pyautogui.screenshot()
    PATH = 'testdata/'
    cv.imwrite(PATH + 'test' + str(index) + '.png', cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR))


def load_test_data(index):
    PATH = 'testdata/test' + str(index) + '.png'
    img = cv.imread(PATH)
    imageasarray = np.array(img)

    image1 = imageasarray[927:1071, 479:672, :]
    image2 = imageasarray[927:1071, 680:873, :]
    image3 = imageasarray[927:1071, 881:1074, :]
    image4 = imageasarray[927:1071, 1083:1276, :]
    image5 = imageasarray[927:1071, 1284:1477, :]

    # DATA = 'DATA2/'
    #
    # cv.imwrite(DATA + 'firstchamp.png', image1)
    # cv.imwrite(DATA + 'secondchamp.png', image2)
    # cv.imwrite(DATA + 'thirdchamp.png', image3)
    # cv.imwrite(DATA + 'fourthchamp.png', image4)
    # cv.imwrite(DATA + 'fifthchamp.png', image5)

    return [image1, image2, image3, image4, image5]


def load_class(class_name):
    image_list = []
    PATH = 'DATA/' + class_name + '/*.png'
    for filename in glob.glob(PATH):
        img = cv.imread(filename)
        image_list.append(img)

    return image_list


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, multichannel=True)

    if m < 400 or s > 0.9:
        return True
    else:
        return False


def get_index_test(index, class_champs):
    champs = load_test_data(index)
    res = []

    for i in range(len(champs)):
        for img in class_champs:
            if compare_images(champs[i], img):
                res.append(i)

    return res


def get_index(class_champs):
    champs = screen_shot()
    res = []

    for i in range(len(champs)):
        for img in class_champs:
            if compare_images(champs[i], img):
                res.append(i)

    return res


if __name__ == "__main__":
    rebel = load_class('rebel')

    # for i in range(0, 12):
    #     print(get_index_test(i, rebel))
    start_time = time.time()
    print(get_index(rebel))
    print(time.time() - start_time)
