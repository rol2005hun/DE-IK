# Szűrők összehasonlítása. Az IBPF, BBPF és GBPF, illetve a IBSF, BBSF és GBSF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def create_band_masks(rows, cols, d0, w, n):
    u = np.arange(rows) - rows / 2
    v = np.arange(cols) - cols / 2
    U, V = np.meshgrid(v, u)
    D = np.sqrt(U**2 + V**2)
    
    ibpf = ((D >= d0 - w / 2) & (D <= d0 + w / 2)).astype(np.float32)
    ibsf = 1.0 - ibpf
    
    D_diff = D**2 - d0**2
    D_diff_safe = np.where(D_diff == 0, 1e-10, D_diff)
    D_safe = np.where(D == 0, 1e-10, D)
    
    bbsf = 1.0 / (1.0 + ((D * w) / D_diff_safe)**(2 * n))
    bbpf = 1.0 - bbsf
    
    gbpf = np.exp(-((D**2 - d0**2) / (D_safe * w))**2)
    gbsf = 1.0 - gbpf
    
    return ibpf, bbpf, gbpf, ibsf, bbsf, gbsf

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
    d0 = 40.0
    w = 20.0
    n = 2

    ibpf, bbpf, gbpf, ibsf, bbsf, gbsf = create_band_masks(rows, cols, d0, w, n)

    res_ibpf = apply_mask(img, ibpf)
    res_bbpf = apply_mask(img, bbpf)
    res_gbpf = apply_mask(img, gbpf)

    res_ibsf = apply_mask(img, ibsf)
    res_bbsf = apply_mask(img, bbsf)
    res_gbsf = apply_mask(img, gbsf)

    diff_pass_ibpf_bbpf = np.clip(cv2.absdiff(res_ibpf, res_bbpf), 0, 255).astype(np.uint8)
    diff_pass_ibpf_gbpf = np.clip(cv2.absdiff(res_ibpf, res_gbpf), 0, 255).astype(np.uint8)
    diff_pass_bbpf_gbpf = np.clip(cv2.absdiff(res_bbpf, res_gbpf), 0, 255).astype(np.uint8)

    diff_stop_ibsf_bbsf = np.clip(cv2.absdiff(res_ibsf, res_bbsf), 0, 255).astype(np.uint8)
    diff_stop_ibsf_gbsf = np.clip(cv2.absdiff(res_ibsf, res_gbsf), 0, 255).astype(np.uint8)
    diff_stop_bbsf_gbsf = np.clip(cv2.absdiff(res_bbsf, res_gbsf), 0, 255).astype(np.uint8)

    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.imshow(diff_pass_ibpf_bbpf, cmap='gray')
    plt.title('IBPF - BBPF különbség')
    plt.axis('off')
    
    plt.subplot(2, 3, 2)
    plt.imshow(diff_pass_ibpf_gbpf, cmap='gray')
    plt.title('IBPF - GBPF különbség')
    plt.axis('off')
    
    plt.subplot(2, 3, 3)
    plt.imshow(diff_pass_bbpf_gbpf, cmap='gray')
    plt.title('BBPF - GBPF különbség')
    plt.axis('off')
    
    plt.subplot(2, 3, 4)
    plt.imshow(diff_stop_ibsf_bbsf, cmap='gray')
    plt.title('IBSF - BBSF különbség')
    plt.axis('off')
    
    plt.subplot(2, 3, 5)
    plt.imshow(diff_stop_ibsf_gbsf, cmap='gray')
    plt.title('IBSF - GBSF különbség')
    plt.axis('off')
    
    plt.subplot(2, 3, 6)
    plt.imshow(diff_stop_bbsf_gbsf, cmap='gray')
    plt.title('BBSF - GBSF különbség')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
