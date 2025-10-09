n, k, d = map(int ,input().split())

sum = 0
for _ in range (n):
    day = int(input())
    if day + 14 <= k+d:
        sum += 1

print(sum)