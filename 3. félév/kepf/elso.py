import cv2

if __name__ == "__main__":
    open_mode = 1 # -1 alap, 0 fekete, 1 szines
    img = cv2.imread("C:/Users/student/Downloads/kep.png", open_mode)
    formatpng = list()
    formatpng.append(cv2.IMWRITE_PNG_COMPRESSION)
    formatpng.append(1)
    imgchannel = img[:,:,0]
    print(imgchannel)
    cv2.imwrite("out.png", imgchannel, formatpng)
    img2 = cv2.imread("C:/Users/student/PycharmProjects/kepfeldolgozas/out.png")
    cv2.imshow("kep", img2)
    cv2.waitKey()
