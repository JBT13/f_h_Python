a = int(input())

if a < 0:
    sum = 0

elif a == 0:
    sum = 1

else:
    sum = 1

    for i in range(1, a + 1):
        sum *= i
    

print(sum)
