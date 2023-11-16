def lnko(a: int, b: int) -> int:
	if b==0: return a
	return lnko(b, a%b)

try:
	file=open("bevprog.txt", "r", encoding="utf-8")
	for line in file:
		print(line.split())
except FileNotFoundError:
	print("nincs ijen fajl")
