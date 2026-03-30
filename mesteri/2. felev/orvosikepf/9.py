# Fourier-transzformáció és annak inverzének kiszámítása. Bemenő adat egy max. 15x15-ös mátrix, amelynek elemei 8 bites nemnegatív egész számok. A kimenet a számítás eredményét tartalmazó mátrix.

import numpy as np

def dft_2d(matrix):
    m, n = matrix.shape
    x = np.arange(m).reshape((m, 1))
    u = np.arange(m).reshape((1, m))
    w_m = np.exp(-2j * np.pi * u * x / m)
    
    y = np.arange(n).reshape((n, 1))
    v = np.arange(n).reshape((1, n))
    w_n = np.exp(-2j * np.pi * v * y / n)
    
    return np.dot(w_m, np.dot(matrix, w_n))

def idft_2d(matrix):
    m, n = matrix.shape
    x = np.arange(m).reshape((m, 1))
    u = np.arange(m).reshape((1, m))
    w_m_inv = np.exp(2j * np.pi * u * x / m) / m
    
    y = np.arange(n).reshape((n, 1))
    v = np.arange(n).reshape((1, n))
    w_n_inv = np.exp(2j * np.pi * v * y / n) / n
    
    return np.dot(w_m_inv, np.dot(matrix, w_n_inv))

def main():
    np.random.seed(42)
    input_matrix = np.random.randint(0, 256, (15, 15), dtype=np.uint8)
    
    fourier_result = dft_2d(input_matrix)
    
    inverse_result = idft_2d(fourier_result)
    inverse_matrix = np.abs(inverse_result).round().astype(np.uint8)
    
    print('Eredeti matrix:')
    print(input_matrix)
    print('\nFourier transzformalt (elso 3x3 elem):')
    print(np.round(fourier_result[:3, :3], 2))
    print('\nInverz transzformalt matrix:')
    print(inverse_matrix)

if __name__ == '__main__':
    main()
