import cv2
import numpy as np

# Olvassa be gombokat tartalmazó képet.
# [Konvertálja a képet HSV színtérbe.]  
# Másolja át a zöld gombokat egy másik, azonos méretű, fekete képre. 
# Jelenítse meg az eredményt egy akármi nevű ablakban.
def elso():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blackimg = np.zeros(img.shape, np.uint8)
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    blackimg[mask == 255] = img[mask == 255]
    cv2.imshow('img', blackimg)
    cv2.waitKey()


# Olvassa be gombokat tartalmazó képet.
# [Konvertálja a képet HSV színtérbe.] 
# Őrizze meg a zöld gombokat a képen, a kép többi pontját pedig állítsa pirosra. 
# Jelenítse meg az eredményt egy XXX nevű ablakban.
def masodik():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    img[mask != 255] = [0, 0, 255]
    cv2.imshow('XXX', img)
    cv2.waitKey()


# Olvassa be valamelyik gombot tartalmazó képet.
# Küszöbölje a képet úgy, hogy az eredménykép fekete-fehér legyen. A gomb legyen az előtér. A küszöbértéket konstans értékkel adja meg.
# Mentse el az eredményt result.png néven.
def harmadik():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    cv2.imwrite('result.png', thresh)


# Olvassa be valamelyik gombot tartalmazó képet.
# Küszöbölje a képet automatikus eljárással úgy, hogy az eredménykép fekete-fehér legyen és a gomb legyen fehér az eredmény téren. 
# Mentse el az eredményt valami.jpg néven.
def negyedik():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('valami.jpg', thresh)


# Olvassa be valamelyik gombot tartalmazó képet szürkeskálában.
# Méretezze át a képet az eredeti méretének duplájára. 
# Alkalmazzon speciális küszöbölést, mely megőrzi az előteret, a háttérpontokat viszont kinullázza ("törli").
# Jelenítse meg az eredményt.
def otodik():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=2, fy=2)
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow('img', thresh)
    cv2.waitKey()


# Olvassa be a két képet, ami egy-egy gombot tartalmaz. 
# Mossa el mindkét gombot egy 7x7-es mediánszűrővel.
# Konvertálja a képeket valóssá.
# Váltsa át mindkét képet Lab színtérbe.
# Számítsa ki, hogy mennyi a két kép középpontjai között a teljes színkülönbség. Az eredményt (egy valós szám) a standard outputra írja ki.
def hatodik():
    img1 = cv2.imread('C:/Users/rrol2/Downloads/gomb1.jpg')
    img2 = cv2.imread('C:/Users/rrol2/Downloads/gomb2.jpg')
    img1 = cv2.medianBlur(img1, 7)
    img2 = cv2.medianBlur(img2, 7)
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2Lab)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2Lab)
    diff = np.sum(np.abs(img1 - img2))
    print(diff)


# Olvassa be a zászlót (usa_flag) tartalmazó képet.
# A zászlót őrizze meg. A hátteret törölje. A zászlórúd törléséről vagy megőrzéséről szabadon dönthet. 
# Jelenítse meg az eredményképet. 
# Segítség: összetett feltételre/több maszk használatára is szüksége lehet.
def hetedik():
    img = cv2.imread('C:/Users/rrol2/Downloads/usaflag.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_inv = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img, img, mask=mask_inv)
    cv2.imshow('img', result)
    cv2.waitKey()


# Olvassa be a gombokat tartalmazó képet.
# Küszöbölje a képet. (A fehér gombok elveszhetnek.)
# Határozza meg a képen a többi gomb külső kontúrját.
# Rajzolja ki a kontúrokat eltérő színnel a gombokat tartalmazó képre.
def nyolcadik():
    img = cv2.imread('C:/Users/rrol2/Downloads/gombok.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey()

if __name__ == "__main__":
    nyolcadik()
