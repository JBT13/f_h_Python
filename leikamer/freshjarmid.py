n = int(input())

bname = ""
ma = -1

for _ in range(n):
    name, value1, value2 = input().split()
    num = int(value1) * int(value2)
    if num > ma:
        bname = name
        ma = num

    elif num == ma and bname > name:
        bname = name


print(bname)

