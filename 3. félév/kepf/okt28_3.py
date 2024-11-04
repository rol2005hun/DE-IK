import cv2


def main():
    # Kép beolvasása szürkeárnyalatos módban
    image = cv2.imread("C:/Users/student/Downloads/text.png", 0)

    # Adaptív küszöbölés alkalmazása
    block_size = 11
    C = 2
    adaptive_thresh = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, block_size, C
    )

    # Eredmények megjelenítése
    cv2.imshow("Original Image", image)
    cv2.imshow("Adaptive Thresholding", adaptive_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()