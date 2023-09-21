#1. hf
import math

sugar = float(input("Add meg a kör sugarát: "))

kerulet = 2 * sugar * math.pi
terulet = sugar ** 2 * math.pi

print("Kerület: ", kerulet)
print("Terület: ", terulet)

#2. hf

import math

szam1 = float(input("Add meg az első számot: "))

szam2 = float(input("Add meg a második számot: "))

print("Számtani közép: ", (szam1 + szam2) / 2)
print("Mértani közép: ", math.sqrt(szam1 * szam2))
