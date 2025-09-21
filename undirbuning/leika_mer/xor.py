n = int(input())
a = list(map(int, input().strip()))
b = list(map(int, input().strip()))

result = []

for i in range(n):
    result.append(str(a[i] ^ b[i]))

print("".join(result))