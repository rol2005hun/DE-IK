# Három éldetektor kiválasztása, aminek az eredményeit kell páronként összehasonlítani. Az OpenCV bármilyen függvénye használható.

import cv2
import numpy as np

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
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

    cv2.imwrite('edges_sobel.png', sobel)
    cv2.imwrite('edges_laplacian.png', laplacian)
    cv2.imwrite('edges_canny.png', canny)
    
    cv2.imwrite('diff_sobel_laplacian.png', diff_sobel_laplacian)
    cv2.imwrite('diff_sobel_canny.png', diff_sobel_canny)
    cv2.imwrite('diff_laplacian_canny.png', diff_laplacian_canny)

if __name__ == '__main__':
    main()
