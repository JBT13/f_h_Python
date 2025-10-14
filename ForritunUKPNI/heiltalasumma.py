n = int(input())

result = 0
if n < 0:
    for i in range(n,2):
        result += i

elif n >= 0:
    for i in range(0,n+1):
        result += i

print(result)