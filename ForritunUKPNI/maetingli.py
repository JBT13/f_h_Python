n, r, c = map(int, input().split())

names = []
for i in range(r):
    name = input()
    names.extend(name.split())

ls = []
for i in range(n):
    name = input()
    ls.append(name)

flag = True 
flag1 = True
flag2 = True
flag3 = True

for i in range(r):
    if ls[:c] == names[:c] and flag:
        print("left")
        flag = False

    if ls[c:] == names[c:] and flag1:
        print("left")
        flag1 = False

    if ls[:c] != names[:c] and flag2:
        print("right")
        flag2 = False

    if ls[c:] != names[c:] and flag3:
        print("right")
        flag3 = False
