a = int(input())
b = int(input())

sum = 0
list = []

if a <= 2 <= b:
    sum += 1
    list.append(2)        

if sum == 0:
    print(":(")
else:
    print(sum)
    print(*list)


