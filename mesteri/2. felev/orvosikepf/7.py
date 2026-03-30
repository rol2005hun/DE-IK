# Hit-or-Miss transzformáció. A képek beolvasására és kimentésére lehet használni az OpenCV függvényeket.

import numpy as np
import cv2

def hit_or_miss(image, kernel):
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    output_image = np.zeros_like(image)
    
    h, w = image.shape
    for i in range(h):
        for j in range(w):
            window = padded_image[i:i+k_h, j:j+k_w]
            
            hit_match = np.all(window[kernel == 1] == 255)
            miss_match = np.all(window[kernel == -1] == 0)
            
            if hit_match and miss_match:
                output_image[i, j] = 255
                
    return output_image

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        binary_img = np.where(img > 127, 255, 0).astype(np.uint8)
        
        kernel = np.array([
            [-1, -1, -1],
            [-1,  1, -1],
            [-1, -1, -1]
        ], dtype=np.int8)
        
        result = hit_or_miss(binary_img, kernel)
        cv2.imwrite('output_hit_miss.png', result)

if __name__ == '__main__':
    main()
