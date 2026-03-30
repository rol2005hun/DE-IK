# Frekvenciatérbeli szűrés az ILPF és IHPF segítségével. A bemenő adat a kép mellett a vágási frekvencia. A szűrés kivételével használható az OpenCV függvénykönyvtár.

import numpy as np
import cv2

def create_distance_matrix(rows, cols):
    center_row, center_col = rows / 2, cols / 2
    u = np.arange(rows).reshape(-1, 1)
    v = np.arange(cols).reshape(1, -1)
    distance = np.sqrt((u - center_row)**2 + (v - center_col)**2)
    return distance

def ideal_low_pass_filter(image, cutoff_freq):
    rows, cols = image.shape
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    
    distance = create_distance_matrix(rows, cols)
    mask = np.where(distance <= cutoff_freq, 1, 0)
    
    filtered_shift = f_shift * mask
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return np.clip(img_back, 0, 255).astype(np.uint8)

def ideal_high_pass_filter(image, cutoff_freq):
    rows, cols = image.shape
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    
    distance = create_distance_matrix(rows, cols)
    mask = np.where(distance > cutoff_freq, 1, 0)
    
    filtered_shift = f_shift * mask
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return np.clip(img_back, 0, 255).astype(np.uint8)

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        cutoff = 50.0
        
        ilpf_result = ideal_low_pass_filter(img, cutoff)
        cv2.imwrite('output_ilpf.png', ilpf_result)
        
        ihpf_result = ideal_high_pass_filter(img, cutoff)
        cv2.imwrite('output_ihpf.png', ihpf_result)

if __name__ == '__main__':
    main()
