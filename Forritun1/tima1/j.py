import math

a = int(input())
b = int(input())
c = int(input())

s = ((a + b + c)/2)

result = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(float(result))