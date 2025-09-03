n = int(input())
count = int(input())
sum = []

for i in range(count):
    number = int(input())
    minus_number = n - number
    sum.append(minus_number)


total = 0
for number in sum:
    total += number 

print(total + n)
  
