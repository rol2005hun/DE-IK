import cv2 as cv
import numpy as np

while (1):
    image = cv.imread('C:/Users/student/Downloads/kep.png')

    # Convert BGR to HSV
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([161, 155, 84])
    upper_blue = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(image, image, mask=mask)

    #cv.imshow('frame', image)
    #cv.imshow('mask', mask)
    #cv.imshow('res', res)
    cv.imshow('a', image - res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()