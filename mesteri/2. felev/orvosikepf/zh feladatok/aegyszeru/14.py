import cv2
import numpy as np

def template_edge_detector(img):
    # 1. Sablonok (maszkok) definialasa kezzel (Ez itt a Sobel-fele)
    # X iranyu maszk: a fuggoleges eleket keresi meg
    kernel_x = np.array([
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ], dtype=float)
    
    # Y iranyu maszk: a vizszintes eleket keresi meg
    kernel_y = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=float)
    
    # 2. Szures elvegzese az OpenCV altalanos szurojevel (filter2D)
    # CV_64F kell, mert a szamolas soran lehetnek negativ szamok, amiket a sima kep (uint8) lenullazna!
    grad_x = cv2.filter2D(img, cv2.CV_64F, kernel_x)
    grad_y = cv2.filter2D(img, cv2.CV_64F, kernel_y)
    
    # 3. Negativ szamok visszakonvertalasa lathato (0-255) pozitiv tartomanyba
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    # 4. A vizszintes es fuggoleges elek osszevonasa egyetlen keppe
    edge_result = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    return edge_result

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        result = template_edge_detector(img)
        cv2.imwrite('14_eldetektor.png', result)

if __name__ == '__main__':
    main()