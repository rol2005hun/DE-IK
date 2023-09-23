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
