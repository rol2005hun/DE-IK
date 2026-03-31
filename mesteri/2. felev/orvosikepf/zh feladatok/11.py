# Frekvenciatérbeli szűrés az IBPF és IBSF segítségével. A bemenő adat a kép mellett a két vágási frekvencia. A szűrés kivételével használható az OpenCV függvénykönyvtár.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_distance_matrix(rows, cols):
    center_row, center_col = rows / 2, cols / 2
    u = np.arange(rows).reshape(-1, 1)
    v = np.arange(cols).reshape(1, -1)
    distance = np.sqrt((u - center_row)**2 + (v - center_col)**2)
    return distance

def ideal_band_pass_filter(image, low_freq, high_freq):
    rows, cols = image.shape
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    
    distance = create_distance_matrix(rows, cols)
    mask = np.where((distance >= low_freq) & (distance <= high_freq), 1, 0)
    
    filtered_shift = f_shift * mask
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return np.clip(img_back, 0, 255).astype(np.uint8)

def ideal_band_stop_filter(image, low_freq, high_freq):
    rows, cols = image.shape
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    
    distance = create_distance_matrix(rows, cols)
    mask = np.where((distance >= low_freq) & (distance <= high_freq), 0, 1)
    
    filtered_shift = f_shift * mask
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return np.clip(img_back, 0, 255).astype(np.uint8)

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        low_cutoff = 20.0
        high_cutoff = 60.0
        
        ibpf_result = ideal_band_pass_filter(img, low_cutoff, high_cutoff)
        ibsf_result = ideal_band_stop_filter(img, low_cutoff, high_cutoff)
        
        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 3, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Eredeti kép')
        plt.axis('off')
        
        plt.subplot(1, 3, 2)
        plt.imshow(ibpf_result, cmap='gray')
        plt.title('IBPF (Sáváteresztő)')
        plt.axis('off')
        
        plt.subplot(1, 3, 3)
        plt.imshow(ibsf_result, cmap='gray')
        plt.title('IBSF (Sávzáró)')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
    else:
        print(f"Nem sikerült betölteni a képet: {file_path}")

if __name__ == '__main__':
    main()
