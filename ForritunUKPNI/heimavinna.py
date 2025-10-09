a = input()
parts = a.split(";")
total = 0

for part in parts:
    if "-" in part:
        b, c = part.split("-")
        b = int(b)
        c = int(c)
        total += (c - b +1)
    else:
        total += 1

print(total)



