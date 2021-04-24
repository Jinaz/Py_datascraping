import cv2

def diff3():
    img = cv2.imread("cameraman.jpg")
    oldmask = cv2.imread("xuC2Z.png")


    imgScale = 256/300
    newX, newY = oldmask.shape[1] * imgScale, oldmask.shape[0] * imgScale
    mask = cv2.resize(oldmask, (int(newX), int(newY)))

    # Create new image
    # Case #1 - Other image is grayscale and source image is colour
    if len(img.shape) == 3 and len(mask.shape) != 3:
        new_image = img * (mask[:, :, None].astype(img.dtype))
        img_not = cv2.bitwise_not(new_image)
        cv2.imshow("new", img_not)
        cv2.waitKey()
    # Case #2 - Both images are colour or grayscale
    elif (len(img.shape) == 3 and len(mask.shape) == 3) or \
            (len(img.shape) == 1 and len(mask.shape) == 1):
        new_image = img * (mask.astype(img.dtype))
        img_not = cv2.bitwise_not(new_image)
        cv2.imshow("new", img_not)
        cv2.waitKey()
    # Otherwise, we can't do this
    else:
        raise Exception("Incompatible input and mask dimensions")


def diff_two_images():
    # load images
    image1 = cv2.imread("in_memory_to_disk.png")
    image2 = cv2.imread("straight_to_disk.png")

    # compute difference
    difference = cv2.subtract(image1, image2)

    # color the mask red
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]

    # add the red mask to the images to make the differences obvious
    image1[mask != 255] = [0, 0, 255]
    image2[mask != 255] = [0, 0, 255]

    # store images
    cv2.imwrite('diffOverImage1.png', image1)
    cv2.imwrite('diffOverImage2.png', image1)
    cv2.imwrite('diff.png', difference)

#if __name__ == "__main__":
#    diff_two_images()
#    diff3()