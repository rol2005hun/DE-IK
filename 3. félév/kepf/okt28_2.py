import cv2
import numpy as np


def main():
    image = cv2.imread("C:/Users/student/Downloads/kacsa.jpg", 1)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    saturation_channel = hsv_image[:, :, 1]

    saturation_threshold = 100

    mask = cv2.inRange(saturation_channel, 0, saturation_threshold)

    extracted_regions = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Extracted Regions", extracted_regions)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()