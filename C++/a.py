n = int(input())
ls = []
for _ in range(n):
    a = input()
    ls.append(a)
    
m = int(input())
number = []
ha = []

for i in range(m):
    b = input()
    number.append(b)

for i in range(n):
    counter = 0
    if number[i].startwith(ls[i]):
        counter += 1

    ha.append(counter)



        
    