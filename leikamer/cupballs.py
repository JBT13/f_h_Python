ls = [0] * 3

ls[0] = 1 

for _ in range(5):
    x = int(input())
    y = int(input()) 
    ls[x-1], ls[y-1] = ls[y-1], ls[x-1]

for index,value in enumerate(ls):
    if value == 1:
        print(index+1)

