# Szűrők összehasonlítása. Az ILPF, BLPF és GLPF, illetve a IHPF, BHPF és GHPF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_masks(rows, cols, d0, n):
    u = np.arange(rows)
    v = np.arange(cols)
    u = u - rows / 2
    v = v - cols / 2
    U, V = np.meshgrid(v, u)
    D = np.sqrt(U**2 + V**2)
    D_safe = np.maximum(D, 1e-10)

    ilpf = (D <= d0).astype(np.float32)
    blpf = 1.0 / (1.0 + (D / d0)**(2 * n))
    glpf = np.exp(-(D**2) / (2 * (d0**2)))

    ihpf = (D > d0).astype(np.float32)
    bhpf = 1.0 / (1.0 + (d0 / D_safe)**(2 * n))
    ghpf = 1.0 - np.exp(-(D**2) / (2 * (d0**2)))

    return ilpf, blpf, glpf, ihpf, bhpf, ghpf

def apply_mask(image, mask):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    fshift_filtered = fshift * mask
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back).astype(np.float32)

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Nem sikerült betölteni a képet: {file_path}")
        return

    rows, cols = img.shape
    d0 = 50.0
    n = 2

    ilpf, blpf, glpf, ihpf, bhpf, ghpf = create_masks(rows, cols, d0, n)

    res_ilpf = apply_mask(img, ilpf)
    res_blpf = apply_mask(img, blpf)
    res_glpf = apply_mask(img, glpf)

    res_ihpf = apply_mask(img, ihpf)
    res_bhpf = apply_mask(img, bhpf)
    res_ghpf = apply_mask(img, ghpf)

    diff_low_ilpf_blpf = cv2.absdiff(res_ilpf, res_blpf).astype(np.uint8)
    diff_low_ilpf_glpf = cv2.absdiff(res_ilpf, res_glpf).astype(np.uint8)
    diff_low_blpf_glpf = cv2.absdiff(res_blpf, res_glpf).astype(np.uint8)

    diff_high_ihpf_bhpf = cv2.absdiff(res_ihpf, res_bhpf).astype(np.uint8)
    diff_high_ihpf_ghpf = cv2.absdiff(res_ihpf, res_ghpf).astype(np.uint8)
    diff_high_bhpf_ghpf = cv2.absdiff(res_bhpf, res_ghpf).astype(np.uint8)
    
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.imshow(diff_low_ilpf_blpf, cmap='gray')
    plt.title('Low: ILPF vs BLPF')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(diff_low_ilpf_glpf, cmap='gray')
    plt.title('Low: ILPF vs GLPF')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(diff_low_blpf_glpf, cmap='gray')
    plt.title('Low: BLPF vs GLPF')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.imshow(diff_high_ihpf_bhpf, cmap='gray')
    plt.title('High: IHPF vs BHPF')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(diff_high_ihpf_ghpf, cmap='gray')
    plt.title('High: IHPF vs GHPF')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.imshow(diff_high_bhpf_ghpf, cmap='gray')
    plt.title('High: BHPF vs GHPF')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
