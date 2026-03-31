# Szűrők összehasonlítása. Az IBPF, BBPF és GBPF, illetve a IBSF, BBSF és GBSF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.\

import cv2
import numpy as np

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
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
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

    cv2.imwrite('diff_pass_ibpf_bbpf.png', np.clip(cv2.absdiff(res_ibpf, res_bbpf), 0, 255).astype(np.uint8))
    cv2.imwrite('diff_pass_ibpf_gbpf.png', np.clip(cv2.absdiff(res_ibpf, res_gbpf), 0, 255).astype(np.uint8))
    cv2.imwrite('diff_pass_bbpf_gbpf.png', np.clip(cv2.absdiff(res_bbpf, res_gbpf), 0, 255).astype(np.uint8))

    cv2.imwrite('diff_stop_ibsf_bbsf.png', np.clip(cv2.absdiff(res_ibsf, res_bbsf), 0, 255).astype(np.uint8))
    cv2.imwrite('diff_stop_ibsf_gbsf.png', np.clip(cv2.absdiff(res_ibsf, res_gbsf), 0, 255).astype(np.uint8))
    cv2.imwrite('diff_stop_bbsf_gbsf.png', np.clip(cv2.absdiff(res_bbsf, res_gbsf), 0, 255).astype(np.uint8))

if __name__ == '__main__':
    main()
