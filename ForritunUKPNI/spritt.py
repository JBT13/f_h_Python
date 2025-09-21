n, m = map(int, input().split())

list = []
while n != len(list):
    a = int(input())
    list.append(a)
    
if sum(list) <= m:
    print("Jebb")
else:
    print("Neibb")