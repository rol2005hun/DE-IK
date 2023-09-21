#1. feladat
a = int(input("Add meg az első számot: "))
b = int(input("Add meg az második számot: "))

osszeg = 0

for i in range(a + 1, b):
    if i % 3 == 0:
        osszeg = osszeg + i

print(f"A 3-al osztható számok összege a(z) ({a}, {b})-an: {osszeg}")

