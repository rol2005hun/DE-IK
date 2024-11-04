import cv2
import numpy as np
import matplotlib.pyplot as plt


def elso():
    image = cv2.imread('C:/Users/student/Downloads/kepkep.png', 0)
    image= cv2.resize(image,(0,0),fx=0.125,fy=0.125)
    equ = cv2.equalizeHist(image)
    res = np.hstack((image, equ))
    cv2.imshow("masodik", res)
    cv2.waitKey()

def masodik():
    image = cv2.imread('C:/Users/student/Downloads/kepkep.png', 0)
    image = cv2.resize(image, (0, 0), fx=0.125, fy=0.125)
    cv2.imshow("elso", image)
    hist = cv2.calcHist([image],[0],None,[256],[0,256])
    plt.figure()
    plt.title('Grayscale histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.ylim([0, 2000])
    plt.show()

def harmadik():
    image = cv2.imread('C:/Users/student/Downloads/kepkep.png')
    image = cv2.resize(image, (0, 0), fx=0.125, fy=0.125)
    b,g,r=cv2.split(image)
    bg = r
    r = b
    b = bg
    img2=cv2.merge([b,g,r])
    cv2.imshow("a2", image)
    cv2.imshow("a",img2)
    cv2.waitKey()


if __name__ == "__main__":
    harmadik()