#1. hf
import math

sugar = float(input("Add meg a kor sugarat: "))

kerulet = 2 * sugar * (math.pi)
terulet = sugar ** 2 * (math.pi)

print("Kerulet: ", kerulet)
print("Terulet", terulet)

#2. hf

import math

szam1 = float(input("Add meg az elso szamot: "))

szam2 = float(input("Add meg a masodik szamot: "))

print("Szamtani kozep: ", (szam1 + szam2) / 2)
print("Mertani kozep: ", math.sqrt(szam1 * szam2))