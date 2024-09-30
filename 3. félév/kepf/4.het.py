import cv2
import numpy as np


# felhasznalotol bekerunk egy szint, illetve a szurke aranyt hany szazalekkal modositsa
# tudjon szint torolni,feketere torli ki a pixeleket
def elso():
    image = cv2.imread('C:/Users/student/Downloads/kep.png')
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    h, w, c = image.shape
    b, g, r = cv2.split(image)
    hanydb = int(input("hany db szin -max 3? "))
    szinek = []
    for i in range(hanydb):
        szin = str(input("r, g, b mit toroljon?: "))
        szinek.append(szin)
        for i2 in range(h):
            for j2 in range(w):
                if szin == "r":
                    r[i2][j2] = 0
                elif szin == "g":
                    g[i2][j2] = 0
                else:
                    b[i2][j2] = 0

    image2 = cv2.merge((b.astype(np.uint8), g.astype(np.uint8), r.astype(np.uint8)))
    cv2.imshow('kinai', image2)
    cv2.waitKey(0)
    hanyal = int(input("hany %al modositsam a szurket(1-100): "))
    cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h2, s, v = cv2.split(image)
    for i3 in range(h):
        for j3 in range(w):
            s[i3][j3] = s[i3][j3] * (1 / hanyal)

    image3 = cv2.merge((h2.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)))
    cv2.imshow('kinai2', image3)
    cv2.waitKey(0)


if __name__ == "__main__":
    elso()