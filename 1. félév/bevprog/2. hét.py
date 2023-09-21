#1. hf
import sys

number1 = float(input("Add meg az elso szamot: "))
op = input("Add meg az operatort: ")
number2 = float(input("Add meg a masodik szamot: "))
output = 0

if op == "/":
    if number2 == 0:
        print("nullaval nem osztunk te ladi")
        sys.exit(1)
    else:
        output = number1 / number2
elif op == "*":
    output = number1 * number2
elif op == "+":
    output = number1 + number2
elif op == "-":
    output = number1 - number2
elif op == "%":
    output = number1 % number2
elif op == "//":
    output = number1 // number2
else:
    print("Ervenyelen operator")
    sys.exit(1)

print(f"{number1} {op} {number2} = {output}")

#2. hf
import math

a = int(input("Add meg az elso egyutthatot: "))
b = int(input("Add meg a masodik egyutthatot: "))
c = int(input("Add meg a harmadik egyutthatot: "))

def getelojel(number):
    if number>=0:
        return "+"
    else:
        return ""

print(f"Az egyenlet: {a}x²{getelojel(b)}{b}x{getelojel(c)}{c}=0")

delta = math.pow(b, 2)-4*a*c
gyok1 = (-b+math.sqrt(delta))/2*a
gyok2 = (-b-math.sqrt(delta))/2*a

print(f"Az egyenlet gyokei: x1: {gyok1}, x2: {gyok2}")

#3. hf
import calendar

# Év és hónap beolvasása
datum = input("Add meg a datumot (ev-hpnap formatumban): ")

# Dátum szeparátor ellenőrzése
if "-" not in datum:
    print("Hibas formátum. A helyes formátum: ev-honap")
else:
    try:
        # Év és hónap kinyerése
        ev, honap = map(int, datum.split("-"))

        # Hónap napjainak számának kiírása
        napok_szama = calendar.monthrange(ev, honap)[1]
        print(f"{ev}-{honap} honap napjainak szama: {napok_szama}")
    except ValueError:
        print("Hibas datum formatum vagy ervenytelen datum")