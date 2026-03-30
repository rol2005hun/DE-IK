# Medián szűrő szürkeskálás képeken. A program paramétere a sablon mérete: 3x3, 5x5 vagy 7x7, illetve a hiányzó pozíciók értelmezése: csak teljes illeszkedés van, hiányzó elemek nullák, hiányzó elemek kimaradnak.

import numpy as np
import cv2

def median_filter(image, kernel_size, mode):
    h, w = image.shape
    pad = kernel_size // 2

    if mode == 'valid':
        out_h, out_w = h - 2 * pad, w - 2 * pad
        result = np.zeros((out_h, out_w), dtype=np.uint8)
        for i in range(out_h):
            for j in range(out_w):
                window = image[i:i+kernel_size, j:j+kernel_size]
                result[i, j] = np.median(window)
        return result

    elif mode == 'zero':
        padded = np.pad(image, pad, mode='constant', constant_values=0)
        result = np.zeros_like(image)
        for i in range(h):
            for j in range(w):
                window = padded[i:i+kernel_size, j:j+kernel_size]
                result[i, j] = np.median(window)
        return result

    elif mode == 'ignore':
        result = np.zeros_like(image)
        for i in range(h):
            for j in range(w):
                r_start = max(0, i - pad)
                r_end = min(h, i + pad + 1)
                c_start = max(0, j - pad)
                c_end = min(w, j + pad + 1)
                window = image[r_start:r_end, c_start:c_end]
                result[i, j] = np.median(window)
        return result

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        res_valid = median_filter(img, 3, 'valid')
        res_zero = median_filter(img, 5, 'zero')
        res_ignore = median_filter(img, 7, 'ignore')

        cv2.imwrite('out_valid.png', res_valid)
        cv2.imwrite('out_zero.png', res_zero)
        cv2.imwrite('out_ignore.png', res_ignore)

if __name__ == '__main__':
    main()
