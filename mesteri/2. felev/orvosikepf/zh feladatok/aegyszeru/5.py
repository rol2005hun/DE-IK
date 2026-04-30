import cv2
import numpy as np

def process_image(img, thresholds):
    # A küszöbértékeket rendezve vesszük az első három legkisebbet, hogy biztosítsuk a megfelelő szegmentálást a kép pixelértékei alapján.
    # Ha rendesen vannak, még el is hanyagolható ez a lépés
    thresh = sorted(thresholds)[:3]

    # A np.digitize függvény segítségével minden pixelértéket besorolunk a megfelelő binbe a küszöbértékek alapján. Ez egy olyan tömböt ad vissza,
    # ahol minden pixelhez egy bin index van rendelve, amely megmutatja, hogy az adott pixel melyik küszöbértékek közé esik.
    bins = np.digitize(img, thresh)
    max_val = len(thresh)

    # A bins tömb értékeit a [0, 255] tartományba skálázzuk, ahol a bin indexek arányosan lesznek elosztva a 256 szürkeárnyalatos érték között.
    res = (bins * (255 / max_val)).astype(np.uint8)
    return res

def main():
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
    if img is not None:
        result = process_image(img, [60, 120, 180])
        cv2.imwrite('output.png', result)

if __name__ == '__main__':
    main()