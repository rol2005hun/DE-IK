# Küszöbölés szűrkeskálás képeken. A küszöbök száma max. 3.

import numpy as np
import cv2

def multi_threshold(image, thresholds):
    thresh = sorted(thresholds)[:3]
    bins = np.digitize(image, thresh)
    max_val = len(thresh)
    result = (bins * (255 / max_val)).astype(np.uint8)
    return result

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        res_1 = multi_threshold(img, [128])
        res_2 = multi_threshold(img, [85, 170])
        res_3 = multi_threshold(img, [64, 128, 192])
        
        cv2.imwrite('thresh_1.png', res_1)
        cv2.imwrite('thresh_2.png', res_2)
        cv2.imwrite('thresh_3.png', res_3)

if __name__ == '__main__':
    main()
