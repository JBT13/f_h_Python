s, e = map(int, input().split())
n = int(input())

years = 0
for _ in range(n):
    sy, ey = map(int, input().split())
    years += sy - s 
    s = ey

years += e-s

print(years)