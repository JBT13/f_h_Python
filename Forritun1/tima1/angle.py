import math

a = int(input())

b = a * math.pi/180

h = 50 * math.tan(b)

print(round(h, 1))