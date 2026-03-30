# Sablonozás alapú éldetektor megvalósítása. OpenCV minden függvénye használható, kivéve az éldetektorokat.

import cv2
import numpy as np

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
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        edge_image = template_edge_detector(img)
        cv2.imwrite('output_kirsch_edges.png', edge_image)

if __name__ == '__main__':
    main()
