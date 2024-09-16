import cv2
import numpy as np

if __name__ == "__main__":
    img2 = cv2.imread("C:/Users/student/Downloads/kepkep-a-crow-who-decided-to-join-the-magpies-in-v0-h134590jaf2d1.png", 0)
    img = cv2.imread("C:/Users/student/Downloads/kep.png", 0)
    if img is not None:
        # Az első 10 sor kiírása
        first_10_rows = img[:10]
        print("Az első 10 sor:")
        print(first_10_rows)

        unique, counts = np.unique(img, return_counts=True)
        value_counts = dict(zip(unique, counts))
        biggest = 0
        for value in range(256):
            thertek = value_counts.get(value, 0)
            print(f"Érték {value}: {thertek}")
            if thertek < 30:
                img[value] = 50
            if thertek > biggest:
                biggest = value_counts.get(value, 0)
        print(f"Legtöbbet tartalmazó: {biggest}")

        cv2.imshow("kep", img)
        cv2.waitKey()
    else:
        print("Nem sikerült betölteni a képet.")
