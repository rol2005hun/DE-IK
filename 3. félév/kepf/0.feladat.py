import cv2

if __name__ == "__main__":
    img = cv2.imread("C:/Users/student/Downloads/kep.png")
    if img is not None:
        rows, cols, channels = img.shape
        img_type = img.dtype
        print(f"Sorok száma: {rows}")
        print(f"Oszlopok száma: {cols}")
        print(f"Csatornák száma: {channels}")
        print(f"Kép típusa: {img_type}")
        cv2.imshow("kep", img)
        cv2.waitKey()
    else:
        print("Nem sikerült betölteni a képet.")