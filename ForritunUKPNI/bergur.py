n = int(input())
a = input().split(" ")
numbers = [int(x) for x in a]

if numbers:
    result = numbers[0]

else:
    result = 0

list = []
if numbers:
    list.append(numbers[0])

for i in range(1, n):
    c = numbers[i]
    p = numbers[i-1]

    if c > p:
        if c in list:
            result += 1
        else:
            result += c
            list.append(c)

print(result)