## SQUARE PATTERN
n = int(input())
for i in range(n+1):
    sum = []
    for j in range(i):
        sum.append(i * "*")
    
for k in sum:
    print(k)

## Right angled triangle
m = int(input())
for i in range(1,m+1):
    for j in range(i):
        print("*", end="")
    print()

## Left angled triangle
l = int(input())
for i in range(l,0,-1):
    for j in range(i):
        print("*", end="")
    print()

## odd triangle
g = int(input())
for i in range(1,g+1,2):
    for j in range(i):
        print("*", end="")
    print()

## even triangle
h = int(input())
for i in range(2,h,2):
    for j in range(i):
        print("*", end="")
    print()

