#0. hf

n = int(input("Hány műveletet szeretnél elvégeztetni? "))

for i in range(n):
    expression = input()
    try:
        result = eval(expression)
        print("Eredménye: ", result)
    except ValueError:
        print("Hiba történt!")
