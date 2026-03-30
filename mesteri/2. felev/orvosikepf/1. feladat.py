# Hisztogram-kiegyenlítés szürkeskálás képeken

import numpy as np
import cv2

def histogram_equalization(image):
    hist, _ = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_masked = np.ma.masked_equal(cdf, 0)
    cdf_masked = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
    cdf_final = np.ma.filled(cdf_masked, 0).astype('uint8')
    return cdf_final[image]

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        result = histogram_equalization(img)
        cv2.imwrite('output.png', result)

if __name__ == '__main__':
    main()
