n = input()

count = 0

for i in n:
    if ('A' <= i <= 'Z') or ('a' <= i <= 'z'):
        count += 1

print(count)