# Képek átlagolása és mediánja.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def average_images(image_paths):
    images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in image_paths]
    valid_images = [img for img in images if img is not None]
    
    if not valid_images:
        return None
        
    stacked = np.stack(valid_images, axis=0)
    result = np.mean(stacked, axis=0)
    return result.astype(np.uint8)

def median_images(image_paths):
    images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in image_paths]
    valid_images = [img for img in images if img is not None]
    
    if not valid_images:
        return None
        
    stacked = np.stack(valid_images, axis=0)
    result = np.median(stacked, axis=0)
    return result.astype(np.uint8)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_names = [os.path.join(base_dir, f) for f in ['input1.png', 'input2.png', 'input3.png']]
    
    avg_img = average_images(file_names)
    med_img = median_images(file_names)
    
    if avg_img is not None and med_img is not None:
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.imshow(avg_img, cmap='gray')
        plt.title('Átlag kép')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(med_img, cmap='gray')
        plt.title('Medián kép')
        plt.axis('off')
        
        plt.show()
    else:
        print("Nem sikerült betölteni a képeket.")

if __name__ == '__main__':
    main()
