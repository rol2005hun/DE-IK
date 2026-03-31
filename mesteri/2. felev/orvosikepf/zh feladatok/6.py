# Morfológiai operátor (erózió, dilatáció, nyitás vagy zárás). Csak egyet kell megvalósítani. 

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def dilation(image, kernel):
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

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        kernel = np.ones((3, 3), dtype=np.uint8)
        result = dilation(img, kernel)
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Eredeti kép')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(result, cmap='gray')
        plt.title('Dilatáció (3x3 kernellel)')
        plt.axis('off')
        
        plt.show()
    else:
        print(f"Nem sikerült betölteni a képet: {file_path}")

if __name__ == '__main__':
    main()
