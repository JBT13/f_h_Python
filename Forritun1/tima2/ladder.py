import math

h, v = map(int, input().split(" "))

a = math.radians(v)

l = h / math.sin(a)

result = math.ceil(l)

print(result)