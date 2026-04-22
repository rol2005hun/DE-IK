# Képek átlagolása és mediánja.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from typing import List, Optional

def load_and_crop(image_paths: List[str]) -> List[np.ndarray]:
    images: List[Optional[np.ndarray]] = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in image_paths]
    valid_images: List[np.ndarray] = [img for img in images if img is not None]
    
    if not valid_images:
        return []
        
    min_h: int = min(img.shape[0] for img in valid_images)
    min_w: int = min(img.shape[1] for img in valid_images)
    
    cropped_images: List[np.ndarray] = [img[:min_h, :min_w] for img in valid_images]
    return cropped_images

def average_images(images: List[np.ndarray]) -> Optional[np.ndarray]:
    if not images:
        return None
        
    stacked: np.ndarray = np.stack(images, axis=0)
    result: np.ndarray = np.mean(stacked, axis=0)
    return result.astype(np.uint8)

def median_images(images: List[np.ndarray]) -> Optional[np.ndarray]:
    if not images:
        return None
        
    stacked: np.ndarray = np.stack(images, axis=0)
    result: np.ndarray = np.median(stacked, axis=0)
    return result.astype(np.uint8)

def main() -> None:
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    file_names: List[str] = [os.path.join(base_dir, f) for f in ['input.png', 'input2.png', 'input3.png']]
    
    cropped_images: List[np.ndarray] = load_and_crop(file_names)
    
    avg_img: Optional[np.ndarray] = average_images(cropped_images)
    med_img: Optional[np.ndarray] = median_images(cropped_images)
    
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
        print('Nem sikerült betölteni a képeket.')

if __name__ == '__main__':
    main()