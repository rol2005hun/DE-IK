import cv2
import numpy as np

def process_frequency(img, d0, d1=0, mode='ilpf'):
    # --- KOZOS RESZ: Ez a blokk mind a 10., mind a 11. feladathoz kotelezo ---
    r, c = img.shape
    cr, cc = r // 2, c // 2
    
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    
    y, x = np.ogrid[:r, :c]
    d = np.sqrt((x - cc)**2 + (y - cr)**2)
    
    mask = np.zeros((r, c), np.uint8)
    # -------------------------------------------------------------------------
    
    # --- 10. FELADAT: Frekvenciatérbeli szűrés az ILPF és IHPF segítségével ---
    if mode == 'ilpf':
        mask[d <= d0] = 1
    elif mode == 'ihpf':
        mask[d > d0] = 1
        
    # --- 11. FELADAT: Frekvenciatérbeli szűrés az IBPF és IBSF segítségével ---
    elif mode == 'ibpf':
        mask[(d >= d0) & (d <= d1)] = 1
    elif mode == 'ibsf':
        mask[(d < d0) | (d > d1)] = 1
        
    # --- KOZOS RESZ: Visszaalakitas (ez is kell mindkét feladathoz) ---
    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.abs(np.fft.ifft2(f_ishift))
    
    return np.clip(img_back, 0, 255).astype(np.uint8)
    # ------------------------------------------------------------------

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        
        # --- 10. FELADAT meghivasai (ha ezt huzod, csak ezeket ird le) ---
        res_ilpf = process_frequency(img, 50, mode='ilpf')
        cv2.imwrite('ilpf.png', res_ilpf)
        
        res_ihpf = process_frequency(img, 50, mode='ihpf')
        cv2.imwrite('ihpf.png', res_ihpf)
        
        # --- 11. FELADAT meghivasai (ha ezt huzod, csak ezeket ird le) ---
        res_ibpf = process_frequency(img, 30, 80, mode='ibpf')
        cv2.imwrite('ibpf.png', res_ibpf)
        
        res_ibsf = process_frequency(img, 30, 80, mode='ibsf')
        cv2.imwrite('ibsf.png', res_ibsf)

if __name__ == '__main__':
    main()