import cv2
import matplotlib.pyplot as plt


def main():
    image = cv2.imread("C:/Users/student/Downloads/kacsa.jpg", 0)

    _, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Eredeti CT kép")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Otsu küszöböléssel")
    plt.imshow(otsu_thresh, cmap="gray")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()