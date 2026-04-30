import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def process_image_stack(images, mode='median'):
    stack = np.stack(images)
    
    if mode == 'atlag':
        res = np.mean(stack, axis=0).astype('uint8')
    elif mode == 'median':
        res = np.median(stack, axis=0).astype('uint8')
        
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
    images = []
    base_path = os.path.dirname(__file__)
    
    for i in range(1, 4):
        if i == 1:
            path = os.path.join(base_path, 'input.png')
        else:
            path = os.path.join(base_path, f'input{i}.png')
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (1024, 1024))
        if img is not None:
            images.append(img)
            
    if len(images) == 0:
        print('image load error')
        return

    result = process_image_stack(images, mode='median')
    compare_results(images[0], result)

if __name__ == '__main__':
    main()