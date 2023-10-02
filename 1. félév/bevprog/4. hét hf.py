#1. hf
n = int(input("Hány db. számot olvasol be? "))
c = 0

for i in range(n):
    x = int(input(""))
    if x > 1 & x % 2 == 0:
        c += 1
        
print(c, "db. pozitív páros szám van.")

#2. hf
while True:
    try:
        szoveg = input("")
        maganhangzok = "aeiouAEIOU"
        eredmeny = ''.join([betu for betu in szoveg if betu not in maganhangzok])
        print(eredmeny)
    except EOFError:
        break

#3. hf
while True:
    try:
        szoveg = input("")
        modositott_szoveg = ''
        for betu in szoveg:
            if betu.isupper():
                modositott_szoveg += betu * 2
            else:
                modositott_szoveg += betu 
        print(modositott_szoveg)
    except EOFError:
        break
