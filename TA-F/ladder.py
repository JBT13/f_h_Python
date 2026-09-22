import math

a,b = map(int, input().split())

c = math.radians(b)

print(math.ceil(a/math.sin(c)))