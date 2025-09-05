a = int(input())
b = int(input())

while b != 0:
    sum = a % b
    a = b
    b = sum
    if a == 0 or b == 0:
        break

print (a)