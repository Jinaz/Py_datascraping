import cv2 as cv
import pytesseract
import numpy as np
import time

def border(src):
    borderType = cv.BORDER_CONSTANT

    top = int(0.05 * src.shape[0])  # shape[0] = rows
    bottom = top
    left = int(0.05 * src.shape[1])  # shape[1] = cols
    right = left
    value = [0, 0, 0]
    dst = cv.copyMakeBorder(src, top, bottom, left, right, borderType, None, value)

    return dst

def get_current_economy(raw_image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Programme\Tesseract-OCR\tesseract.exe"

    cut1 = np.array(raw_image)
    img = cut1[881:909, 867:964, :]

    scale_percent = 300  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    #border it and convert it
    imgasCV = cv.cvtColor(border(resized), cv.COLOR_RGB2BGR)

    gray = cv.cvtColor(imgasCV, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening


    custom_config = r'--oem 3 --psm 6 outputbase digits'
    # Perform text extraction
    d = pytesseract.image_to_string(invert, config=custom_config)

    #construct output
    if not d or '.' in d:
        return -1
    else:
        return int(d)

print(get_current_economy(cv.imread('../TFT/testdata/test7.png')))
