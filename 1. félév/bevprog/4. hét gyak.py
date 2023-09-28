#1. feladat
pozitiv = 0
negativ = 0
n = 1

while n != 0:
    n = int(input(""))
    if(n > 0):
        pozitiv += 1
    elif(n < 0):
        negativ += 1

print("Pozitív számok száma: ", pozitiv)
print("Negatív számok száma: ", negativ)
