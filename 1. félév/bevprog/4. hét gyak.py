#1. feladat
pozitiv = 0
negativ = 0
n = 1

while n != 0:
    n = int(input(""))
    if n > 0:
        pozitiv += 1
    elif n < 0:
        negativ += 1

print("Pozitív számok száma: ", pozitiv)
print("Negatív számok száma: ", negativ)

#2. feladat
paros = 0
paratlan = 0
n = 0

while n <= 100:
    n = int(input(""))
    if n % 2 == 0:
        paros += 1
    elif n % 2 != 0:
        paratlan += 1
    n += n

print("Páros számok száma: ", paros)
print("Páratlan számok száma: ", paratlan)
