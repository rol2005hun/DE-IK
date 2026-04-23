import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def process_image(img):
    res = img.copy()

    mode = 'nullas'
    k=7
    pad=k//2
    h,w=img.shape

    # 4 5 6
    # 3 9 5
    # 3 0 21

    if mode == 'teljes':
        for i in range(h-pad, pad):
            for j in range(w-pad, pad):
                res[i,j]=res.mean()

    
    if mode == 'nullas':
        

    if mode == 'figyelmen_kivul_hagyas':
        

    return res

def compare_results(original, processed):
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('original')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.title('processed')
    plt.axis('off')
    
    plt.show()

def main():
    path = os.path.join(os.path.dirname(__file__), 'input.png')
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print('image load error')
        return

    result = process_image(img)
    compare_results(img, result)

if __name__ == '__main__':
    main()