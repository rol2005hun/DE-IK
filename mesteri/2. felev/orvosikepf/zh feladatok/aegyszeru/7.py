import cv2
import numpy as np

# Na ez egy kicsit combosabb lesz
def process_image(img):
    # Adott mintázatot keresünk, 1-es helyeken fehér(255) pixeleket, -1-es helyeken fekete(0) pixeleket várunk. A 0 értékek helyén bármi lehet.
    kernel = np.array([
        [-1, -1, -1],
        [-1,  1, -1],
        [ 1,  1, -1]
    ])
    
    h, w = img.shape
    pad = 1
    res = np.zeros_like(img)
    
    # Itt átalakítjuk a kernel-t két logikai maszkká, hogy könnyebben ellenőrizhessük a hit és miss feltételeket a szűrőablakban.
    hit_mask = (kernel == 1)
    miss_mask = (kernel == -1)
    
    # Tovább már nem fogta fel az agyam
    for i in range(pad, h - pad):
        for j in range(pad, w - pad):
            window = img[i-pad:i+pad+1, j-pad:j+pad+1]
            
            hit_match = np.all(window[hit_mask] == 255)
            miss_match = np.all(window[miss_mask] == 0)
            
            if hit_match and miss_match:
                res[i, j] = 255
                
    return res

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img_bin = np.where(img > 127, 255, 0).astype(np.uint8)
        result = process_image(img_bin)
        cv2.imwrite('output.png', result)

if __name__ == '__main__':
    main()