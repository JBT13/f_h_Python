n = int(input())
d = list(map(int, input().split()))
d.sort()
result = 0
for num in d:
    result += num

print(result+1)

