import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('C:/Users/student/Downloads/1920x1080-aesthetic-glrfk0ntspz3tvxg.png')
image2 = cv2.imread('C:/Users/student/Downloads/masodik.png')

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

# the window showing output image
# with the weighted sum
cv2.imshow('Weighted Image', weightedSum)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()