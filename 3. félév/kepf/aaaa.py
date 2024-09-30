import cv2

# Load the input image
image = cv2.imread('C:/Users/student/Downloads/1920x1080-aesthetic-glrfk0ntspz3tvxg.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()