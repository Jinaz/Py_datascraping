# importing libraries
import pyautogui
import scipy
import pickledb as pickle
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

import os

def knn(pic):
    pic_n = pic.reshape(pic.shape[0] * pic.shape[1], pic.shape[2])
    print(pic_n.shape)

    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
    pic2show = kmeans.cluster_centers_[kmeans.labels_]

    cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
    plt.imshow(cluster_pic)

    cv2.imshow('cluster_pic', cluster_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sobel(gray):
    # defining the sobel filters
    sobel_horizontal = np.array([np.array([1, 2, 1]), np.array([0, 0, 0]), np.array([-1, -2, -1])])
    print(sobel_horizontal, 'is a kernel for detecting horizontal edges')

    sobel_vertical = np.array([np.array([-1, 0, 1]), np.array([-2, 0, 2]), np.array([-1, 0, 1])])
    print(sobel_vertical, 'is a kernel for detecting vertical edges')

    out_h = ndimage.convolve(gray, sobel_horizontal, mode='reflect')
    out_v = ndimage.convolve(gray, sobel_vertical, mode='reflect')
    # here mode determines how the input array is extended when the filter overlaps a border.

    kernel_laplace = np.array([np.array([1, 1, 1]), np.array([1, -8, 1]), np.array([1, 1, 1])])
    print(kernel_laplace, 'is a laplacian kernel')

    out_l = ndimage.convolve(gray, kernel_laplace, mode='reflect')
    plt.imshow(out_l, cmap='gray')

    cv2.imshow('out_1' ,out_l)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def prefilter():
    # Load two images
    # Ursprung
    image = cv2.imread('testdata/test1.png')
    # newData
    img2 = cv2.imread('testdata/test0.png')

    diff = cv2.absdiff(image, img2)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 1
    imask = mask > th

    canvas = np.zeros_like(img2, np.uint8)
    canvas[imask] = img2[imask]

    # get diff cvt to gray
    cv2.imshow('img1', image)
    cv2.imshow('img2', img2)
    cv2.imshow('win2', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite("result.png", canvas)
    gray = cv2.cvtColor(canvas, cv2.COLOR_RGB2GRAY)

    # target_size = (64,64)

    # dst = cv2.resize(gray, target_size)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(gray)
    # dst = dst.reshape(target_size.shape[0] * target_size.shape[1])

    return gray

def prefilterColored():
    # Load two images
    # Ursprung
    image = cv2.imread('testdata/test1.png')
    # newData
    img2 = cv2.imread('testdata/test0.png')

    diff = cv2.absdiff(image, img2)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 1
    imask = mask > th

    canvas = np.zeros_like(img2, np.uint8)
    canvas[imask] = img2[imask]

    # get diff cvt to gray
    cv2.imshow('img1', image)
    cv2.imshow('img2', img2)
    cv2.imshow('win2', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite("result.png", canvas)
    gray = cv2.cvtColor(canvas, cv2.COLOR_RGB2GRAY)

    # target_size = (64,64)

    # dst = cv2.resize(gray, target_size)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(gray)
    # dst = dst.reshape(target_size.shape[0] * target_size.shape[1])

    return canvas

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them.
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

def batch_extractor(images_path, pickled_db_path="featuresDB/features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print(
        'Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)

    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'w') as fp:
        pickle.dump(result, fp)

class Matcher(object):

    def __init__(self, pickled_db_path="featuresDB/features.pck"):
        with open(pickled_db_path) as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.iteritems():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        from scipy.spatial import distance as ssd
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return ssd.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

#sobel(prefilter())
#knn(prefilterColored())

#method to cut out from a blank board
#needs a blank board to begin with
def cutImagePart():
    img = cv2.imread('testdata/cleanboard.png')
    itemsboard = img[542:864, 182:491, :]
    board = img[404:722, 484:1390,:]
    bench = img[721:826, 370:1413,:]

    cv2.imshow('items', itemsboard)
    cv2.imshow('board', board)
    cv2.imshow('bench', bench)

    cv2.imwrite('featuresDB/board.png', board)
    cv2.imwrite('featuresDB/itemsboard.png', itemsboard)
    cv2.imwrite('featuresDB/bench.png', bench)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def readBaseData():
    board = cv2.imread('featuresDB/board.png')
    itemsboard = cv2.imread('featuresDB/itemsboard.png')
    bench = cv2.imread('featuresDB/bench.png')

    return board, bench, itemsboard

def compareToScreen():
    board, bench, items = readBaseData()

    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    citemsboard = img[542:864, 182:491, ]
    cboard = img[404:722, 484:1390, ]
    cbench = img[721:826, 370:1413, ]

    board = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    items = cv2.cvtColor(items, cv2.COLOR_BGR2GRAY)
    bench = cv2.cvtColor(bench, cv2.COLOR_BGR2GRAY)

    subtract_board = cboard - board
    subtract_items = citemsboard - items
    subtract_bench = cbench - bench

    #kernel = np.ones((3,3), np.float32) / 9
    #subtract_board = cv2.filter2D(subtract_board, -1, kernel)
    #subtract_items = cv2.filter2D(subtract_items, -1, kernel)
    #subtract_bench = cv2.filter2D(subtract_bench, -1, kernel)

    kernel2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    subtract_board = cv2.filter2D(subtract_board, -1, kernel2)
    subtract_items = cv2.filter2D(subtract_items, -1, kernel2)
    subtract_bench = cv2.filter2D(subtract_bench, -1, kernel2)

    subtract_board = cv2.fastNlMeansDenoising(subtract_board, None, 10, 10, 7)
    subtract_items = cv2.fastNlMeansDenoising(subtract_items, None, 10, 10, 7)
    subtract_bench = cv2.fastNlMeansDenoising(subtract_bench, None, 10, 10, 7)

    cv2.imshow('sub-board', subtract_board)
    cv2.imshow('sub-items', subtract_items)
    cv2.imshow('sub-bench', subtract_bench)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#compareToScreen()

def getDataOfImage(img):

    #cv2.imshow('raw', img)

    items = img[562:812,212:382,:]
    bench = img[679:825,352:1426,:]
    board = img[284:656,493:1394,:]

    return items, bench, board

def readScreen():
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    return img

def sharpen(img):
    kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel2)

def redMask(diffImage):
    # color the mask red
    Conv_hsv_Gray = cv2.cvtColor(diffImage, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    diffImage[mask != 255] = [0, 0, 255]

    return diffImage

def compare1():
    img = cv2.imread('clean.png')

    citems, cbench, cboard = getDataOfImage(img)
    ditems, dbench, dboard = getDataOfImage(readScreen())

    # compute difference
    outitems = cv2.subtract(citems, ditems)
    outbench = cv2.subtract(cbench, dbench)
    outboard = cv2.subtract(cboard, dboard)

    #outitems = redMask(outitems)
    #outbench = redMask(outbench)
    #outboard = redMask(outboard)

    outitems = cv2.cvtColor(outitems, cv2.COLOR_BGR2GRAY)
    outbench = cv2.cvtColor(outbench, cv2.COLOR_BGR2GRAY)
    outboard = cv2.cvtColor(outboard, cv2.COLOR_BGR2GRAY)

    outitems = sharpen(outitems)
    outbench = sharpen(outbench)
    outboard = sharpen(outboard)

    cv2.imshow('1', outitems)
    cv2.imshow('2', outbench)
    cv2.imshow('3', outboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

compare1()