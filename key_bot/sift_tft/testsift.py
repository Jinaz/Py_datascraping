import cv2 as cv2
import numpy as np
import win32_connectors.screenshotter as sc
import time
import matplotlib.pyplot as plt

# time step 0 - z
image = sc.screenshot_to_numpyarray()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# time diff is 2 seconds now
time.sleep(4)

# time step 1 - z+1
image2 = sc.screenshot_to_numpyarray()
image2 = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2BGR)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# create sift
sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img)
cv2.imwrite('sift_keypoints.jpg', img)

# get keypoints and descriptors
kp1, des1 = sift.detectAndCompute(gray, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(image, kp1, image2, kp2, matches[:50], image2, flags=2)
plt.imshow(img3), plt.show()
