n = int(input())
digit_list = [int(d) for d in str(n)]

count = 0
for i in digit_list:
    i = int(i)
    count += i

print(count)