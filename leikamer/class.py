a, b, c = map(int, input().split())
n = int(input()) # Days

num = set() # Numbers that I got
num_not = set() # Numbers that I dont got

i = 1
while len(num_not) <= n:
    num.add(a*i)
    num.add(b*i)
    num.add(c*i)

    if i not in num:
        num_not.add(i)

    i += 1

ls = list(num_not)
print(ls[n-1])


