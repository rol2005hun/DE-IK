#0. hf

n = int(input("Hány műveletet szeretnél elvégeztetni? "))

for i in range(n):
    expression = input()
    try:
        result = eval(expression)
        print("Eredménye: ", result)
    except ValueError:
        print("Hiba történt!")

#1. hf

n = int(input("Add meg hány számot olvasol be: "))
ma = input("")

for i in range(n - 1):
    if input("") > ma:
        ma = input("")

print("A maximum: ", ma)

#2. hf

jegy = 0

while jegy >= 0:
    jegy = int(input("Add meg a jegyet: "))
    
    if jegy < 0:
        break
    elif jegy >= 80:
        print("jeles")
    elif jegy < 80 & jegy >= 70:
        print("jo")
    elif jegy < 70 & jegy >= 60:
        print("kozepes")
    elif jegy < 60 & jegy >= 5:
        print("elegseges")
    elif jegy < 50:
        print("elegtelen")
