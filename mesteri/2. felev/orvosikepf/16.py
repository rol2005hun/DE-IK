# Régió-jelölő módszer. Lásd 7/9 fóliát. Bemenet egy fekete, fehér kép. Az eredmény egy színes kép, ahol a színek a régiókat azonosítják.

import numpy as np
import cv2

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
    img = cv2.imread('input_binary.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        labels = region_labeling(img)
        colored_img = colorize_labels(labels)
        cv2.imwrite('output_regions.png', colored_img)

if __name__ == '__main__':
    main()
