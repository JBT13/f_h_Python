r, c = map(int, input().split())

ls = []
for _ in range(r):
    m = input().split()
    new_ls = list(map(int, m))
    ls.append(new_ls)
    
flag = False

for row in range(1, r - 1):
    for column in range(1,c - 1):
        num = ls[row][column]

        if num < ls[row-1][column] and num < ls[row+1][column] and num < ls[row][column+1] and num < ls[row][column-1]:
            flag = True
            break

if flag:
    print("Jebb")

else:
    print("Neibb")