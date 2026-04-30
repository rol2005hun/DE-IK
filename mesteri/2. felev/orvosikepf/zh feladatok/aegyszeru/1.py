import cv2
import numpy as np

def process_image(img):
    # Hisztogramot számolunk, az img.flatten() segítségével egy dimenziós tömbbé alakítjuk a képet,
    # majd 256 binre osztjuk a hisztogramot a [0, 256] tartományban.
    hist, _ = np.histogram(img.flatten(), 256, [0, 256])

    # A hisztogram kumulatív eloszlását (CDF) számoljuk, amely megmutatja, hogy a pixelértékek milyen gyakorisággal fordulnak elő a képen.
    cdf = hist.cumsum()
    
    # A CDF-et normalizáljuk, hogy a pixelértékek 0 és 255 között legyenek. Ez a lépés biztosítja, hogy a hisztogram kiegyenlítés után
    # a pixelértékek teljes tartományát kihasználjuk.
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

    # Itt a normalizált CDF-et uint8 típusra konvertáljuk, hogy a pixelértékek megfelelő formátumban legyenek a kimeneti képhez.
    cdf_normalized = cdf_normalized.astype('uint8')
    
    # A kimeneti kép pixelértékeit a normalizált CDF alapján állítjuk be. Ez a lépés végrehajtja a hisztogram kiegyenlítést,
    # ahol minden pixelérték a normalizált CDF-ben meghatározott új értékhez lesz hozzárendelve.
    res = cdf_normalized[img]
    
    return res

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        result = process_image(img)
        cv2.imwrite('output.png', result)

if __name__ == '__main__':
    main()