n = int(input())
count = int(input())
sum = []

for i in range(count):
    number = int(input())
    sum.append(number)

total = 0
for number in sum:
    total += n ** number

print(total)
  

