n, m = map(int, input().split())

dih = {
    ".":20,
    "O":10,
    "\\":25,
    "/":25,
    "A":35,
    "^":5,
    "V":22
}

total = 0 
for _ in range(n):
    b = input()
    for letter in b:
        total += dih[letter]

print(total)