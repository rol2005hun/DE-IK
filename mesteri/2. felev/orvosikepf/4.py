# Képek átlagolása és mediánja.

import numpy as np
import cv2

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
    file_names = ['input1.png', 'input2.png', 'input3.png']
    
    avg_img = average_images(file_names)
    if avg_img is not None:
        cv2.imwrite('average_output.png', avg_img)
        
    med_img = median_images(file_names)
    if med_img is not None:
        cv2.imwrite('median_output.png', med_img)

if __name__ == '__main__':
    main()
