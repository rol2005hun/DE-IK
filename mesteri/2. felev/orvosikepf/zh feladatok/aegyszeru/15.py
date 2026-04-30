import cv2
import numpy as np

def get_diff(img1, img2):
    return cv2.absdiff(img1, img2)

def edge_detectors(img):
    canny = cv2.Canny(img, 100, 200)
    
    # A Sobel es a Laplacian eredmenye tartalmazhat negativ szamokat a matek miatt,
    # ezert kell a convertScaleAbs, ami visszakonvertalja oket 0-255 koze.
    sobel = cv2.convertScaleAbs(cv2.Sobel(img, cv2.CV_64F, 1, 1))
    laplacian = cv2.convertScaleAbs(cv2.Laplacian(img, cv2.CV_64F))
    
    return canny, sobel, laplacian

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        canny, sobel, lapl = edge_detectors(img)
        
        # Paronkenti osszehasonlitas a kulonbsegkepekkel
        cv2.imwrite('15_diff_canny_sobel.png', get_diff(canny, sobel))
        cv2.imwrite('15_diff_canny_lapl.png', get_diff(canny, lapl))
        cv2.imwrite('15_diff_sobel_lapl.png', get_diff(sobel, lapl))

if __name__ == '__main__':
    main()