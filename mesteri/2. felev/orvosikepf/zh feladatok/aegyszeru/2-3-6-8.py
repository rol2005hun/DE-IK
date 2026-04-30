import cv2
import numpy as np

def process_image(img, k_size=3, mode='kimarad', op='atlag'):
    # Kép mérete, height x width
    h, w = img.shape

    # A kernel méretének fele, amely meghatározza a szűrőablak méretét, de lefele kerekítve, mivel a kernel mérete páratlan kell legyen (3, 5, 7).
    pad = k_size // 2

    # Kimeneti kép inicializálása, amely ugyanakkora méretű lesz, mint a bemeneti kép, de kezdetben nullákkal feltöltve.
    res = np.zeros_like(img)
    
    # EZ Kell a 6os es 8ashoz is
    if mode == 'teljes':
        # Befutjuk i-re és j-re a képen, de csak azokban a pozíciókban, ahol a kernel teljesen illeszkedik a képre, azaz a szélektől pad távolságra.
        for i in range(pad, h - pad):
            for j in range(pad, w - pad):
                # A szűrőablakot a kernel méretének megfelelően kivágjuk a képből, ahol a középpont i, j.
                window = img[i-pad:i+pad+1, j-pad:j+pad+1]
                
                if op == 'atlag':
                    res[i, j] = np.mean(window)
                elif op == 'median':
                    res[i, j] = np.median(window)
                elif op == 'dilatacio':
                    # Ez kell a 6os, es 8ashoz
                    res[i, j] = np.max(window)
                elif op == 'erozio':
                    # Ez kell a 8as feladathoz
                    res[i, j] = np.min(window)
                    
    elif mode == 'nulla':
        # A képet körbe paddingeljük nullákkal a kernel méretének megfelelően, hogy a szűrőablak a széleken is teljes legyen.
        padded = np.pad(img, pad, mode='constant', constant_values=0)
        for i in range(h):
            for j in range(w):
                # A szűrőablakot a paddingelt képből vágjuk ki, ahol a középpont i, j a paddingelt kép koordinátái szerint.
                window = padded[i:i+k_size, j:j+k_size]
                
                if op == 'atlag':
                    res[i, j] = np.mean(window)
                elif op == 'median':
                    res[i, j] = np.median(window)
                    
    elif mode == 'kimarad':
        for i in range(h):
            for j in range(w):
                r_min = max(0, i - pad)
                r_max = min(h, i + pad + 1)
                c_min = max(0, j - pad)
                c_max = min(w, j + pad + 1)
                window = img[r_min:r_max, c_min:c_max]
                
                if op == 'atlag':
                    res[i, j] = np.mean(window)
                elif op == 'median':
                    ## Mediánnak, 3as feladat
                    res[i, j] = np.median(window)
                    
    return res.astype(np.uint8)

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        # Itt az 'op' es 'mode' parameterek atirasaval tudod valtogatni a feladatokat!
        result = process_image(img, k_size=3, mode='kimarad', op='atlag')
        cv2.imwrite('output.png', result)

if __name__ == '__main__':
    main()