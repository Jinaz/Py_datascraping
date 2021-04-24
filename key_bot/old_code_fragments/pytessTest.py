import cv2 as cv
import pytesseract
import numpy as np

from random import randint
from pytesseract import Output
import re

def what(gray):
    #gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    a = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = a[0]
    hierarchy = a[1]
    idx = 0
    for cnt in contours:

        xe, ye, we, he = cv.boundingRect(cnt)
        print(xe, ye, we, he)
        roi = im[ye - 100:ye + he + 100, xe - 100:xe + we + 100]
        cv.imwrite('a.jpg', roi)
        cv.rectangle(im, (xe, ye), (xe + we, ye + he), (200, 0, 0), 2)
        cv.imwrite('dev.jpg', im)

        if xe > 30:
            if ye > 30:
                if he > 30:
                    if we > 30:
                        idx += 1
                        cv.imshow(str(idx) + '.jpg', roi)
                        cv.rectangle(im, (xe, ye), (xe + we, ye + he), (200, 0, 0), 2)

                        cv.imshow('dev.jpg', im)
                        cv.waitKey()

def blur_sharpen_img(src, arg='blur'):
    if arg == 'blur':
        kernel = np.ones((9,9), np.float32) / 81
        dst = cv.filter2D(src, -1, kernel)
        return dst
    else:
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        im = cv.filter2D(src, -1, kernel)
        return im



def rescale(img):
    scale_percent = 300  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    #print('Resized Dimensions : ', resized.shape)

    #cv.imshow("Resized image", resized)
    #cv.waitKey(0)
    return resized

def extend(src):
    print(src.shape)
    value = [0, 0, 0]
    #for 40-90 border of 30 left and top

    outimage = cv.copyMakeBorder(src, 10, 10, 15, 60, cv.BORDER_CONSTANT, None, value)

    # cv.imshow('aaa', outimage)
    # cv.waitKey()

    return outimage


def border(src):
    borderType = cv.BORDER_CONSTANT
    window_name = "copyMakeBorder Demo"

    imageName = 'a.jpg'
    # Loads an image
    # Check if image is loaded fine
    # cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    top = int(0.15 * src.shape[0])  # shape[0] = rows
    bottom = top
    left = int(0.15 * src.shape[1])  # shape[1] = cols
    right = left

    value = [0, 0, 0]

    dst = cv.copyMakeBorder(src, top, bottom, left, right, borderType, None, value)

    # cv.imshow(window_name, dst)

    return dst


def original():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Programme\Tesseract-OCR\tesseract.exe"
    # Grayscale, Gaussian blur, Otsu's threshold
    test0 = cv.imread('testdata/test0.png')
    image = cv.imread('pytess/1.png')
    gray = cv.cvtColor(test0, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # Perform text extraction
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    # print(data)

    cv.imshow('thresh', thresh)
    cv.imshow('opening', opening)
    cv.imshow('invert', invert)
    cv.waitKey()


pytesseract.pytesseract.tesseract_cmd = r"C:\Programme\Tesseract-OCR\tesseract.exe"

# 867,881
# 922,881

# 922,909

tests = []
for index in range(11):
    PATH = 'testdata/test' + str(index) + '.png'
    test = cv.imread(PATH)
    tests.append(test)

bgrimages = []
for test in tests:
    cut1 = np.array(test)
    img = cut1[881:909, 874:924, :]

    scale_percent = 300  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    imgasCV = cv.cvtColor(resized, cv.COLOR_RGB2BGR)
    # cv.imshow('', imgasCV)
    # cv.waitKey(0)
    # border(imgasCV)
    # extend(imgasCV)
    #rescale(imgasCV)

    # bgrimages.append(border(imgasCV))
    #bgrimages.append(extend(imgasCV))
    bgrimages.append(extend(rescale(imgasCV)))

for img in bgrimages:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    im = blur_sharpen_img(invert, 'blur')
    #what(gray)


    custom_config = r'--oem 3 --psm 13 outputbase digits'
    newconfig = r'--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789'

    # Perform text extraction
    d = pytesseract.image_to_string(thresh, config=newconfig)

    #print(type(d))
    # data = pytesseract.image_to_string(invert, lang='eng', config='--oem 0')
    print(d)

    # cv.imshow('thresh', thresh)
    # cv.imshow('opening', opening)
    # cv.imshow('invert', invert)
    cv.imshow('blur', thresh)
    # cv.imwrite('2.png', invert)
    cv.waitKey()
