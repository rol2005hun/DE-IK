# Medián szűrő szürkeskálás képeken. A program paramétere a sablon mérete: 3x3, 5x5 vagy 7x7, illetve a hiányzó pozíciók értelmezése: csak teljes illeszkedés van, hiányzó elemek nullák, hiányzó elemek kimaradnak.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import warnings
from numpy.lib.stride_tricks import sliding_window_view

def median_filter(image: np.ndarray, kernel_size: int, mode: str) -> np.ndarray:
    pad: int = kernel_size // 2

    if mode == 'valid':
        windows: np.ndarray = sliding_window_view(image, (kernel_size, kernel_size))
        result: np.ndarray = np.median(windows, axis=(2, 3))
        return result.astype(np.uint8)

    elif mode == 'zero':
        padded: np.ndarray = np.pad(image, pad, mode='constant', constant_values=0)
        windows: np.ndarray = sliding_window_view(padded, (kernel_size, kernel_size))
        result: np.ndarray = np.median(windows, axis=(2, 3))
        return result.astype(np.uint8)

    elif mode == 'ignore':
        image_float: np.ndarray = image.astype(np.float32)
        padded_nan: np.ndarray = np.pad(image_float, pad, mode='constant', constant_values=np.nan)
        windows: np.ndarray = sliding_window_view(padded_nan, (kernel_size, kernel_size))
        
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', category=RuntimeWarning)
            result: np.ndarray = np.nanmedian(windows, axis=(2, 3))
            
        return result.astype(np.uint8)
        
    return np.zeros_like(image)

def main() -> None:
    file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img: np.ndarray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        res_valid: np.ndarray = median_filter(img, 3, 'valid')
        res_zero: np.ndarray = median_filter(img, 5, 'zero')
        res_ignore: np.ndarray = median_filter(img, 7, 'ignore')

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
    else:
        print(f'Nem sikerult betolteni a kepet: {file_path}')

if __name__ == '__main__':
    main()
