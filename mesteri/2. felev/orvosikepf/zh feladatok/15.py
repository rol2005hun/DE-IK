# Három éldetektor kiválasztása, aminek az eredményeit kell páronként összehasonlítani. Az OpenCV bármilyen függvénye használható.

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Nem sikerült betölteni a képet: {file_path}")
        return

    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)
    sobel = np.clip(sobel, 0, 255).astype(np.uint8)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = np.clip(np.abs(laplacian), 0, 255).astype(np.uint8)

    canny = cv2.Canny(img, 100, 200)

    diff_sobel_laplacian = cv2.absdiff(sobel, laplacian)
    diff_sobel_canny = cv2.absdiff(sobel, canny)
    diff_laplacian_canny = cv2.absdiff(laplacian, canny)

    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.imshow(sobel, cmap='gray')
    plt.title('Sobel')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(canny, cmap='gray')
    plt.title('Canny')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.imshow(diff_sobel_laplacian, cmap='gray')
    plt.title('Diff: Sobel & Laplacian')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(diff_sobel_canny, cmap='gray')
    plt.title('Diff: Sobel & Canny')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.imshow(diff_laplacian_canny, cmap='gray')
    plt.title('Diff: Laplacian & Canny')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
