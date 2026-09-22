import math

n = int(input())

ls = []
for i in range(n):
    pay = int(input())
    ls.append(pay)

total = int(input())

def calculate(n, ls, total):
    total += sum(ls)
    new = total / n

    newls = []
    for i in range(n):
        value = math.ceil(new - ls[i])
        if value < 0:
            print("not possible")
            return
    
        
        newls.append(value)

    return newls


a = calculate(n,ls,total)

if a:
    for i in a:
        print(i)

