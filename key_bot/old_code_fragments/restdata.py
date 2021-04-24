import json
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def save_2_jason(arr):
    data = {}
    cnt = 0
    for i in arr:
        data['KeyPoint_%d' % cnt] = []
        data['KeyPoint_%d' % cnt].append({'x': i.pt[0]})
        data['KeyPoint_%d' % cnt].append({'y': i.pt[1]})
        data['KeyPoint_%d' % cnt].append({'size': i.size})
        cnt += 1
    with open('DATA/data.txt', 'w') as outfile:
        json.dump(data, outfile)


def read_from_jason():
    result = []
    with open('data.txt') as json_file:
        data = json.load(json_file)
        cnt = 0
        while (data.__contains__('KeyPoint_%d' % cnt)):
            pt = cv.KeyPoint(x=data['KeyPoint_%d' % cnt][0]['x'], y=data['KeyPoint_%d' % cnt][1]['y'],
                             size=data['KeyPoint_%d' % cnt][2]['size'])
            result.append(pt)
            cnt += 1
    return result


def compare_Keypoints(img1, img2):
    # Initiate ORB detector
    orb = cv.ORB_create(nfeatures=500)
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # Draw first 10 matches.
    img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:120], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.imshow(img3), plt.show()

def get_feature_points(src):
    # -- Step 1: Detect the keypoints using SURF Detector
    orb = cv.ORB_create(nfeatures=500)
    keypoints, descriptors = orb.detectAndCompute(src, None)
    # -- Draw keypoints
    img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
    cv.drawKeypoints(src, keypoints, img_keypoints)

    # print(descriptors)
    # -- Show detected (drawn) keypoints
    cv.imshow('ORB Keypoints', img_keypoints)
    cv.waitKey()

    return keypoints, descriptors


def loadimage():
    image = cv.imread("../TFT/DATA/all/k6.png")
    return get_feature_points(cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR))