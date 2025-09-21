n = int(input())
m = input()

words = m.split(" ")

abbr = ""

for i in range(n):
    first = words[i][0]
    if first.isupper():
        abbr += first

print(abbr)