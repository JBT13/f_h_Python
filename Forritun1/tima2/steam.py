a = int(input())
b = int(input())

delta = abs(a - b)

if delta > 180:
    print(360 - delta)

else: 
    print(delta)