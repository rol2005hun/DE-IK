# Régió-jelölő módszer. Lásd 7/9 fóliát. Bemenet egy fekete, fehér kép. Az eredmény egy színes kép, ahol a színek a régiókat azonosítják.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self):
        self.parent = {}

    def make_set(self, i):
        if i not in self.parent:
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if root_i < root_j:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j

def region_labeling(binary_image):
    h, w = binary_image.shape
    labels = np.zeros((h, w), dtype=np.int32)
    next_label = 1
    uf = UnionFind()

    for i in range(h):
        for j in range(w):
            if binary_image[i, j] > 127:
                top = labels[i-1, j] if i > 0 else 0
                left = labels[i, j-1] if j > 0 else 0

                if top == 0 and left == 0:
                    labels[i, j] = next_label
                    uf.make_set(next_label)
                    next_label += 1
                elif top != 0 and left == 0:
                    labels[i, j] = top
                elif top == 0 and left != 0:
                    labels[i, j] = left
                else:
                    uf.union(top, left)
                    labels[i, j] = uf.find(top)

    for i in range(h):
        for j in range(w):
            if labels[i, j] > 0:
                labels[i, j] = uf.find(labels[i, j])

    return labels

def colorize_labels(labels):
    max_label = np.max(labels)
    if max_label == 0:
        return np.zeros((*labels.shape, 3), dtype=np.uint8)
        
    np.random.seed(42)
    colors = np.random.randint(0, 256, size=(max_label + 1, 3), dtype=np.uint8)
    colors[0] = [0, 0, 0] 
    
    return colors[labels]

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_binary.png')
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        labels = region_labeling(img)
        colored_img = colorize_labels(labels)
        
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Eredeti bináris kép')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(colored_img)
        plt.title('Régiók')
        plt.axis('off')
        
        plt.show()
    else:
        print(f"Nem sikerült betölteni a képet: {file_path}")

if __name__ == '__main__':
    main()
