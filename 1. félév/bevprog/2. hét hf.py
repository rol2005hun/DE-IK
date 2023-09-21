#1. hf
import sys

number1 = float(input("Add meg az első számot: "))
op = input("Add meg az operátort: ")
number2 = float(input("Add meg a második szamot: "))
output = 0

if op == "/":
    if number2 == 0:
        print("Nullával nem osztunk te ladi!")
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
    print("Érvényelen operátor!")
    sys.exit(1)

print(f"{number1} {op} {number2} = {output}")

#2. hf
import math
import sys

a = int(input("Add meg az első együtthatót: "))
b = int(input("Add meg a második együtthatót: "))
c = int(input("Add meg a harmadik együtthatót: "))

def getelojel(number):
    if number >= 0:
        return "+"
    else:
        return ""

def checkone(number):
    if number == 1:
        return ""
    else:
        return number

print(f"Az egyenlet: {checkone(a)}x² {getelojel(b)} {checkone(b)}x {getelojel(c)} {c} = 0")

delta = math.pow(b, 2) - 4 * a * c
if delta < 0:
    print("Nincs megoldás a valós számok halmazában!")
    sys.exit(1)
gyok1 = (-b + math.sqrt(delta)) / 2 * a
gyok2 = (-b - math.sqrt(delta)) / 2 * a

print(f"Az egyenlet gyökei: x1: {gyok1}, x2: {gyok2}")

#3. hf
import calendar

datum = input("Add meg a dátumot (ev-hónap formátumban): ")

if "-" not in datum:
    print("Hibás formátum. A helyes formátum: év-hónap!")
else:
    try:
        ev, honap = map(int, datum.split("-"))
        napok_szama = calendar.monthrange(ev, honap)[1]
        print(f"{ev}-{honap} hónap napjainak száma: {napok_szama}")
    except ValueError:
        print("Hibás dátum formátum vagy érvenytelen dátum!")
