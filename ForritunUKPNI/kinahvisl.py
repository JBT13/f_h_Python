n = input()
m = input()

count = 1

for i in range(len(n)):
    if n[i] != m[i]:
        count += 1

print(count)