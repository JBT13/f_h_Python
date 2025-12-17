size = set()
for _ in range(10):
    n = int(input())
    value = n % 42
    size.add(value)

print(len(size))