n = int(input())
s = set()
for _ in range(n):
    a = input()
    if a not in s:
        s.add(a)

for content in s:
    print(content)

