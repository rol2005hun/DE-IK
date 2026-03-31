# Küszöbölés szűrkeskálás képeken. A küszöbök száma max. 3.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def multi_threshold(image, thresholds):
    thresh = sorted(thresholds)[:3]
    bins = np.digitize(image, thresh)
    max_val = len(thresh)
    result = (bins * (255 / max_val)).astype(np.uint8)
    return result

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        res_1 = multi_threshold(img, [128])
        res_2 = multi_threshold(img, [85, 170])
        res_3 = multi_threshold(img, [64, 128, 192])
        
        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 4, 1)
        plt.imshow(img, vmin=0, vmax=255, cmap='gray')
        plt.title('Eredeti kép')
        plt.axis('off')
        
        plt.subplot(1, 4, 2)
        plt.imshow(res_1, vmin=0, vmax=255, cmap='gray')
        plt.title('1 küszöb')
        plt.axis('off')

        plt.subplot(1, 4, 3)
        plt.imshow(res_2, vmin=0, vmax=255, cmap='gray')
        plt.title('2 küszöb')
        plt.axis('off')

        plt.subplot(1, 4, 4)
        plt.imshow(res_3, vmin=0, vmax=255, cmap='gray')
        plt.title('3 küszöb')
        plt.axis('off')

        plt.tight_layout()
        plt.show()
    else:
        print(f"Nem sikerült betölteni a képet: {file_path}")

if __name__ == '__main__':
    main()
