name = input()
p = float(input())
n = int(input())

no_plast = 0

for _ in range(n):
    m = input()
    if m == "ekki plast":
        no_plast += 1

plast = p * 100
trash = (no_plast * 100) / n 

if plast >= trash:
    print("Jebb")

else:
    print("Neibb")