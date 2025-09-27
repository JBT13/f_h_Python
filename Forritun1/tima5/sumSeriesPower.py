k = int(input())
n = int(input())
sum = []

for _ in range(n):
    x = int(input())
    sum.append(x)

total = 0
for x in sum:
    total += k ** x

print(total)
  

