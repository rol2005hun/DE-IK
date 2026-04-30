import cv2
import numpy as np

def process_images(images, mode='atlag'):
    stack = np.stack(images, axis=0)
    
    if mode == 'atlag':
        res = np.mean(stack, axis=0)
    elif mode == 'median':
        res = np.median(stack, axis=0)
        
    return res.astype(np.uint8)

def main():
    img1 = cv2.imread('kep1.png', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('kep2.png', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('kep3.png', cv2.IMREAD_GRAYSCALE)
    
    if img1 is not None and img2 is not None and img3 is not None:
        image_list = [img1, img2, img3]
        
        res_atlag = process_images(image_list, mode='atlag')
        cv2.imwrite('atlag_eredmeny.png', res_atlag)
        
        res_median = process_images(image_list, mode='median')
        cv2.imwrite('median_eredmeny.png', res_median)

if __name__ == '__main__':
    main()