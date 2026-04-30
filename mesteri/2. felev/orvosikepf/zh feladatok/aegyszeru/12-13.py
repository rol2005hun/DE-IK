import cv2
import numpy as np

def get_diff(img1, img2):
    return cv2.absdiff(img1, img2)

def apply_freq_filter(img, d0, d1=0, ftype='ideal', mode='low'):
    r, c = img.shape
    y, x = np.ogrid[:r, :c]
    d = np.sqrt((x - c//2)**2 + (y - r//2)**2)
    
    # Csak az alap LPF (Alulatereszto) maszkokat definialjuk
    def get_lpf(cutoff):
        if ftype == 'ideal': 
            return (d <= cutoff).astype(float)
        elif ftype == 'butterworth': 
            return 1 / (1 + (d / (cutoff + 1e-5))**4)
        elif ftype == 'gaussian': 
            return np.exp(-(d**2) / (2 * (cutoff**2)))
            
    # Mabol a tobbi modot matekkal levezetjuk
    if mode == 'low':
        mask = get_lpf(d0)
    elif mode == 'high':
        mask = 1 - get_lpf(d0)
    elif mode == 'bandpass':
        mask = get_lpf(d1) - get_lpf(d0) # d1 a kulso sugar, d0 a belso
    elif mode == 'bandstop':
        mask = 1 - (get_lpf(d1) - get_lpf(d0))
        
    fshift = np.fft.fftshift(np.fft.fft2(img)) * mask
    return np.abs(np.fft.ifft2(np.fft.ifftshift(fshift))).astype(np.uint8)

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        # --- 12. FELADAT Hivasa (ILPF, BLPF, GLPF) ---
        # Ha a feladat IHPF-et ker, csak ird at a mode='low'-t mode='high'-ra!
        ilpf = apply_freq_filter(img, 50, ftype='ideal', mode='low')
        blpf = apply_freq_filter(img, 50, ftype='butterworth', mode='low')
        cv2.imwrite('12_diff_ideal_butter.png', get_diff(ilpf, blpf))

        # --- 13. FELADAT Hivasa (IBPF, BBPF, GBPF) ---
        # Ha a feladat IBSF-et ker, csak ird at a mode-ot 'bandstop'-ra!
        ibpf = apply_freq_filter(img, 30, d1=80, ftype='ideal', mode='bandpass')
        bbpf = apply_freq_filter(img, 30, d1=80, ftype='butterworth', mode='bandpass')
        cv2.imwrite('13_diff_ideal_butter_bp.png', get_diff(ibpf, bbpf))

if __name__ == '__main__':
    main()