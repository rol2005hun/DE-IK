import numpy as np

def manual_dft2d(matrix):
    h, w = matrix.shape
    # Az eredmeny komplex szamokbol allo matrix lesz
    res = np.zeros((h, w), dtype=complex)
    
    # Ketszeres szummazas a Fourier keplet alapjan
    for u in range(h):
        for v in range(w):
            sum_val = 0
            for x in range(h):
                for y in range(w):
                    # A Fourier alapfuggveny: e^(-j * 2 * pi * (ux/h + vy/w))
                    exponent = -2j * np.pi * ((u * x / h) + (v * y / w))
                    sum_val += matrix[x, y] * np.exp(exponent)
            res[u, v] = sum_val
    return res

def manual_idft2d(f_matrix):
    h, w = f_matrix.shape
    res = np.zeros((h, w), dtype=complex)
    
    for x in range(h):
        for y in range(w):
            sum_val = 0
            for u in range(h):
                for v in range(w):
                    # Az inverznel nincs minuszjel az exponensben: e^(j * ...)
                    exponent = 2j * np.pi * ((u * x / h) + (v * y / w))
                    sum_val += f_matrix[u, v] * np.exp(exponent)
            # Az inverznel osztani kell a merettel (N*M)
            res[x, y] = sum_val / (h * w)
            
    # Visszaalakitas valos szamma, kerekitve
    return np.abs(res).round().astype(np.uint8)

def main():
    # Pelda egy 5x5-os matrixra (max 15x15 lehet)
    matrix = np.random.randint(0, 256, (5, 5), dtype=np.uint8)
    
    f_res = manual_dft2d(matrix)
    inv_res = manual_idft2d(f_res)
    
    print('Fourier matrix (elso elem):\n', f_res[0,0])
    print('Eredeti matrix:\n', matrix)
    print('Visszaallitott matrix:\n', inv_res)

if __name__ == '__main__':
    main()