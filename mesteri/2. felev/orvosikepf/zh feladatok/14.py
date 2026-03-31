# Sablonozás alapú éldetektor megvalósítása. OpenCV minden függvénye használható, kivéve az éldetektorokat.

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_edge_detector(image):
    kernels = [
        np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]], dtype=np.float32),
        np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]], dtype=np.float32),
        np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]], dtype=np.float32),
        np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]], dtype=np.float32),
        np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]], dtype=np.float32),
        np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]], dtype=np.float32),
        np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]], dtype=np.float32),
        np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]], dtype=np.float32)
    ]
    
    max_edges = np.zeros(image.shape, dtype=np.float32)
    
    for kernel in kernels:
        filtered = cv2.filter2D(image, cv2.CV_32F, kernel)
        max_edges = np.maximum(max_edges, filtered)
        
    result = np.clip(max_edges, 0, 255).astype(np.uint8)
    return result

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        edge_image = template_edge_detector(img)
        
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Eredeti kép')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(edge_image, cmap='gray')
        plt.title('Kirsch éldetektor')
        plt.axis('off')
        
        plt.show()
    else:
        print(f"Nem sikerült betölteni a képet: {file_path}")

if __name__ == '__main__':
    main()
