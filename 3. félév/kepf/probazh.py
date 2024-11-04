import cv2
import numpy as np
import random

def elso():
    image_path = input("Adja meg a szerkesztendő kép teljes elérési útvonalát: ")
    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.equalizeHist(image)

    threshold_value = int(input("Adja meg a küszöbértéket (0-255): "))
    _, image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    hue = int(input("Adja meg a színezet értékét (0-179): "))
    saturation = int(input("Adja meg a színtelítettség értékét (0-255): "))
    brightness = int(input("Adja meg a világosság értékét (0-255): "))

    hsv_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    hsv_image = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 0] = hue
    hsv_image[:, :, 1] = saturation
    hsv_image[:, :, 2] = brightness
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    cv2.imshow("kep", final_image)
    cv2.waitKey()



def masodik():
    image_path = input("Adja meg a szerkesztendő kép teljes elérési útvonalát: ")
    image = cv2.imread(image_path)

    threshold_value = int(input("Adja meg a küszöbértéket (0-255): "))

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = np.zeros(hsv_image.shape[:2], dtype=np.uint8)
    indices = []

    print("Dolgozik...")
    for i in range(hsv_image.shape[0]):
        for j in range(hsv_image.shape[1]):
            h, s, v = hsv_image[i, j]
            if h <= 2 * threshold_value and 50 <= s <= 170 and 100 <= v <= 200:
                mask[i, j] = 255
                indices.append((i, j))

    random.shuffle(indices)
    keep_indices = indices[:len(indices) // 2]

    for i, j in indices[len(indices) // 2:]:
        mask[i, j] = 0

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    background_color = input("Adja meg a háttérszín értékeit (B, G, R): ").split(',')
    background_color = [int(c) for c in background_color]

    result_image = image.copy()
    result_image[mask == 0] = background_color

    cv2.imshow("kep", result_image)
    cv2.waitKey()


def harmadik():
    path = input("path= ")
    img = cv2.imread(path,1)
    threshValue = np.uint8(input("thresh= "))

    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    mask = cv2.threshold(hsv[:,:,0],threshValue,255,cv2.THRESH_BINARY)
    mask = mask[1] # csak a tombre van szuksegunk
    masked = np.zeros(hsv.shape,dtype=np.uint8)
    indexes = list()
    indexes_res = list()

    for i in range(0,hsv.shape[0]):
        for j in range(0,hsv.shape[1]):
            if mask[i,j] ==255 :
                pixelGroup = hsv[i,j,:]

                if (pixelGroup[0] < threshValue*2) and \
                    (pixelGroup[1] >=50 and pixelGroup[1] <=170) and \
                    (pixelGroup[2] >=100 and pixelGroup[2] <=200):
                        indexes.append(tuple((i,j)))
                        masked[i,j,:] = pixelGroup
    for index in indexes:
        n = random.random()
        if n>=0.5:
            indexes_res.append(index)

    mask2 = np.zeros(mask.shape,dtype=np.uint8)

    for index in indexes_res:
        mask2[index[0],index[1]] = 255

    structElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    eroded = cv2.erode(mask2,structElement)
    opened = cv2.dilate(eroded,structElement)

    hsv_result = np.zeros(hsv.shape,dtype=np.uint8)

    for i in range(0,3):
        hsv_result[:,:,i] = cv2.bitwise_and(hsv[:,:,i],opened)

    hue = np.uint8(input("hue="))
    sat = np.uint8(input("sat="))
    val = np.uint8(input("val="))

    cv2.imshow("opened",opened)

    for i in range(0,hsv_result.shape[0]):
        for j in range(0,hsv_result.shape[1]):
            if np.array_equal(hsv_result[i,j,:],np.array([0,0,0])):
                hsv_result[i, j, :] = np.array([hue,sat,val])

    result = cv2.cvtColor(hsv_result,cv2.COLOR_HSV2RGB)

    cv2.imshow("result",result)
    cv2.waitKey()


if __name__ == "__main__":
    # elso()
    # masodik()
    harmadik()