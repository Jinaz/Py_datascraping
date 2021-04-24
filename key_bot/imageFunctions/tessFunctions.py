import cv2 as cv
import pytesseract
import numpy as np
import imageFunctions.imagecomparison as ic


def image_to_Numbers(img):
    thresh = ic.prefilter(img, "thresh")

    newconfig = r'--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789'

    # Perform text extraction
    d = pytesseract.image_to_string(thresh, config=newconfig)
    # print(d)

    return d


def preprocess_For_Reading(data, x1, x2, y1, y2):
    cut1 = np.array(data)
    img = cut1[x1:x2, y1:y2, :]

    imgasCV = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    return imgasCV
