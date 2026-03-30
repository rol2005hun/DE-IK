# Szürkeskálás dilatáció és erózió. A képek beolvasására és kimentésére lehet használni az OpenCV függvényeket.

import numpy as np
import cv2

def grayscale_dilation(image, kernel):
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    output_image = np.zeros_like(image)
    
    h, w = image.shape
    for i in range(h):
        for j in range(w):
            window = padded_image[i:i+k_h, j:j+k_w]
            output_image[i, j] = np.max(window[kernel == 1])
            
    return output_image

def grayscale_erosion(image, kernel):
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=255)
    output_image = np.zeros_like(image)
    
    h, w = image.shape
    for i in range(h):
        for j in range(w):
            window = padded_image[i:i+k_h, j:j+k_w]
            output_image[i, j] = np.min(window[kernel == 1])
            
    return output_image

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        kernel = np.ones((3, 3), dtype=np.uint8)
        
        dilated = grayscale_dilation(img, kernel)
        eroded = grayscale_erosion(img, kernel)
        
        cv2.imwrite('dilated.png', dilated)
        cv2.imwrite('eroded.png', eroded)

if __name__ == '__main__':
    main()
