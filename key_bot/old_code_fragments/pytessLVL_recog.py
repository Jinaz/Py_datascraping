import cv2 as cv
import pytesseract
import numpy as np

def loadTestData():
    tests = []
    for index in range(11):
        PATH = '../TFT/testdata/test' + str(index) + '.png'
        test = cv.imread(PATH)
        tests.append(test)
        #print(test.shape)
    return tests

def rescale(img):
    scale_percent = 300  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    # print('Resized Dimensions : ', resized.shape)

    # cv.imshow("Resized image", resized)
    # cv.waitKey(0)
    return resized


def extend(src):
    #print(src.shape)
    value = [0, 0, 0]
    # for 40-90 border of 30 left and top

    outimage = cv.copyMakeBorder(src, 10, 10, 15, 60, cv.BORDER_CONSTANT, None, value)

    # cv.imshow('aaa', outimage)
    # cv.waitKey()

    return outimage


def resizeImage(img, scalePercent=300):
    scale_percent = scalePercent  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    return resized

def convert_images(data, x1, x2, y1, y2, upscale=300):
    bgrimages = []
    for entity in data:
        cut1 = np.array(entity)
        img = cut1[x1:x2, y1:y2, :]

        resized = resizeImage(img, upscale)
        imgasCV = cv.cvtColor(resized, cv.COLOR_RGB2BGR)

        bgrimages.append(extend(rescale(imgasCV)))
    return bgrimages

def image_to_Numbers(bgrimages):
    for img in bgrimages:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (3, 3), 0)
        thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        # Morph open to remove noise and invert image
        # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        # opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
        # invert = 255 - opening

        # im = blur_sharpen_img(invert, 'blur')
        newconfig = r'--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789'

        # Perform text extraction
        d = pytesseract.image_to_string(thresh, config=newconfig)
        #print(d)

        cv.imshow('blur', thresh)
        cv.waitKey()

def image_to_string(img):

        img2 = img
        for i in range(12):
            img2 = extend(img2)
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (3, 3), 0)
        thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        # Morph open to remove noise and invert image
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening

        # im = blur_sharpen_img(invert, 'blur')
        newconfig = r'--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789-'

        # Perform text extraction
        d = pytesseract.image_to_string(thresh, config=newconfig)
        #print(d)

        #cv.imshow('blur', thresh)
        #cv.waitKey()
        return d

def tess_fun():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Programme\Tesseract-OCR\tesseract.exe"
    tests = loadTestData()
    #print(tests)

    set = 3
    if set == 1:
        x_left = 881
        x_right = 909
        y_left = 874
        y_right = 924

        bgrimages = convert_images(tests, x_left, x_right, y_left, y_right)
        image_to_Numbers(bgrimages)
    if set == 2:
        bgrimg_2 = convert_images(tests,885, 904,  315, 351)
        image_to_Numbers(bgrimg_2)
    if set == 3:
        stage = convert_images(tests, 11,30,778,794,1000) #801,813
        round = convert_images(tests, 11,30,801,813,1000)

        st = []
        rd = []

        for s in stage:
            a = image_to_string(s)
            if a is not '':
                st.append(a)
        for r in round:
            a = image_to_string(r)
            if a is not '':
                rd.append(a)
        st = np.array(st)
        rd = np.array(rd)
        for itemnum in range(st.shape[0]):
            print(st[itemnum],"-",rd[itemnum])


tess_fun()