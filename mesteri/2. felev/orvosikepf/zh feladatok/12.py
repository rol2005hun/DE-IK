# Szűrők összehasonlítása. Az ILPF, BLPF és GLPF, illetve a IHPF, BHPF és GHPF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.

import cv2
import numpy as np

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
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
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

    cv2.imwrite('diff_low_ilpf_blpf.png', cv2.absdiff(res_ilpf, res_blpf).astype(np.uint8))
    cv2.imwrite('diff_low_ilpf_glpf.png', cv2.absdiff(res_ilpf, res_glpf).astype(np.uint8))
    cv2.imwrite('diff_low_blpf_glpf.png', cv2.absdiff(res_blpf, res_glpf).astype(np.uint8))

    cv2.imwrite('diff_high_ihpf_bhpf.png', cv2.absdiff(res_ihpf, res_bhpf).astype(np.uint8))
    cv2.imwrite('diff_high_ihpf_ghpf.png', cv2.absdiff(res_ihpf, res_ghpf).astype(np.uint8))
    cv2.imwrite('diff_high_bhpf_ghpf.png', cv2.absdiff(res_bhpf, res_ghpf).astype(np.uint8))

if __name__ == '__main__':
    main()
