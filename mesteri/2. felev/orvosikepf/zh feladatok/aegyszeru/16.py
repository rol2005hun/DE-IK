import cv2
import numpy as np
import os

# --- 16. FELADAT: Regio-jelolo modszer kezzel (Kereses algoritmussal) ---
def region_labeling_manual(img_bin):
    h, w = img_bin.shape
    
    # A cimkek (labels) matrixa, kezdetben minden 0 (vagyis hatter)
    labels = np.zeros((h, w), dtype=np.int32)
    current_label = 1
    
    # Vegigmegyunk a kepen pixelrol pixelre
    for i in range(h):
        for j in range(w):
            # Ha talalunk egy feher pixelt, ami meg nincs beszamozva
            if img_bin[i, j] == 255 and labels[i, j] == 0:
                
                # Vermet (stack) hasznalunk a melysegi bejarashoz
                stack = [(i, j)]
                labels[i, j] = current_label
                
                # Amig van vizsgalando pixel a foltban
                while stack:
                    r, c = stack.pop()
                    
                    # Megnezzuk a 4 szomszedjat (fent, lent, balra, jobbra)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        
                        # Ha a palyan belul vagyunk
                        if 0 <= nr < h and 0 <= nc < w:
                            # Ha ez a szomszed is feher es meg nincs cimkezve
                            if img_bin[nr, nc] == 255 and labels[nr, nc] == 0:
                                labels[nr, nc] = current_label
                                stack.append((nr, nc))
                                
                # Ha kiurult a verem, vegeztunk a folttal, johet a kovetkezo sorszam
                current_label += 1

    # Szinezes resze (ugyanaz a zsenialis NumPy trukk, ezt szabad hasznalni)
    colors = np.random.randint(0, 255, size=(current_label, 3), dtype=np.uint8)
    colors[0] = [0, 0, 0] # A hatter (0. cimke) maradjon fekete
    
    colored_img = colors[labels]
    
    return colored_img

def main():
    img = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_binary.png'), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        # Biztositjuk a tokeletes fekete-feher kepet a bemenetnek
        _, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        result = region_labeling_manual(img_bin)
        cv2.imwrite(os.path.join(os.path.dirname(os.path.abspath(__file__)), '16_regiok.png'), result)

if __name__ == '__main__':
    main()