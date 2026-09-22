n = int(input())

count = 0
while n != 1:
    if n % 2 != 0:
        n += (2*n) +1

    else:
        n = n // 2

    count += 1

print(count)