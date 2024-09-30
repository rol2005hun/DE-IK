import cv2
import numpy as np

def modify_and_remove_color(image, channel, gray_percentage):
    # Színcsatornák szétválasztása
    b, g, r = cv2.split(image)

    # Szürkeárnyalat számítása
    gray_image = 0.299 * r + 0.587 * g + 0.114 * b

    # Szürkeárnyalat módosítása a megadott százalékkal
    gray_image = gray_image * (gray_percentage / 100.0)
    gray_image = gray_image.astype(np.uint8)

    # A kiválasztott csatorna törlése (feketére állítás)
    if channel == 1:  # Kék csatorna
        b[:, :] = 0
    elif channel == 2:  # Zöld csatorna
        g[:, :] = 0
    elif channel == 3:  # Vörös csatorna
        r[:, :] = 0

    # Visszaállítjuk a módosított csatornákat
    modified_image = cv2.merge((b, g, r))

    return modified_image, gray_image

if __name__ == '__main__':
    # Kép betöltése
    image = cv2.imread('C:/Users/student/Downloads/kep.png')

    # Felhasználói bemenet kérés
    channel = int(input("Válasszon egy színt 1 (kék), 2 (zöld), 3 (vörös): "))
    gray_percentage = int(input("Adja meg a szürkeárnyalat módosításának százalékát (0-100): "))

    # Kép módosítása
    modified_image, gray_image = modify_and_remove_color(image, channel, gray_percentage)

    # Eredmény megjelenítése
    cv2.imshow('Modositott kep', modified_image)
    cv2.imshow('Modositott szurke kep', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
