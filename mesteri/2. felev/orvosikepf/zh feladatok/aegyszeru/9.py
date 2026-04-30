import numpy as np

def fourier_transform(matrix):
    f_transform = np.fft.fft2(matrix)
    
    img_back = np.fft.ifft2(f_transform)
    img_back = np.abs(img_back)
    
    return f_transform, np.clip(img_back, 0, 255).astype(np.uint8)

def main():
    matrix = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
    
    f_res, inv_res = fourier_transform(matrix)
    print('Kiszamolt Fourier matrix:\n', f_res)
    print('Visszaallitott matrix:\n', inv_res)

if __name__ == '__main__':
    main()