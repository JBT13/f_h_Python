n = int(input())
prize = int(input())
m = int(input())

ls = [0] * n

ls[prize-1] = 1 

for _ in range(m):
    x, y = map(int, input().split()) 
    ls[x-1], ls[y-1] = ls[y-1], ls[x-1]

for index,value in enumerate(ls):
    if value == 1:
        print(index)

