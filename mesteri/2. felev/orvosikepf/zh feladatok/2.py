# Átlagoló szűrő szürkeskálás képeken. A program paramétere a sablon mérete: 3x3, 5x5 vagy 7x7, illetve a hiányzó pozíciók értelmezése: csak teljes illeszkedés van, hiányzó elemek nullák, hiányzó elemek kimaradnak.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def average_filter(image, kernel_size, mode):
    h, w = image.shape
    pad = kernel_size // 2

    if mode == 'valid':
        out_h, out_w = h - 2 * pad, w - 2 * pad
        result = np.zeros((out_h, out_w), dtype=np.float32)
        for dy in range(kernel_size):
            for dx in range(kernel_size):
                result += image[dy:dy+out_h, dx:dx+out_w]
        result /= (kernel_size * kernel_size)
        return result.astype(np.uint8)

    elif mode == 'zero':
        padded = np.pad(image, pad, mode='constant', constant_values=0)
        result = np.zeros_like(image, dtype=np.float32)
        for dy in range(kernel_size):
            for dx in range(kernel_size):
                result += padded[dy:dy+h, dx:dx+w]
        result /= (kernel_size * kernel_size)
        return result.astype(np.uint8)

    elif mode == 'ignore':
        padded = np.pad(image, pad, mode='constant', constant_values=0)
        mask = np.pad(np.ones_like(image), pad, mode='constant', constant_values=0)
        
        result = np.zeros_like(image, dtype=np.float32)
        count = np.zeros_like(image, dtype=np.float32)
        
        for dy in range(kernel_size):
            for dx in range(kernel_size):
                result += padded[dy:dy+h, dx:dx+w]
                count += mask[dy:dy+h, dx:dx+w]
                
        return (result / count).astype(np.uint8)

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        res_valid = average_filter(img, 3, 'valid')
        res_zero = average_filter(img, 5, 'zero')
        res_ignore = average_filter(img, 7, 'ignore')

        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 4, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Eredeti kep')
        plt.axis('off')
        
        plt.subplot(1, 4, 2)
        plt.imshow(res_valid, cmap='gray')
        plt.title('Valid (3x3)')
        plt.axis('off')

        plt.subplot(1, 4, 3)
        plt.imshow(res_zero, cmap='gray')
        plt.title('Zero (5x5)')
        plt.axis('off')

        plt.subplot(1, 4, 4)
        plt.imshow(res_ignore, cmap='gray')
        plt.title('Ignore (7x7)')
        plt.axis('off')

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    main()
