n = int(input())
a = list(map(int, input().split()))

dic = {}
for index,value in enumerate(a):
    dic[value] = index + 1

ls = []
for i in range(len(a)-1,-1,-1):
    ls.append(dic[i+1])

print(*ls)





    