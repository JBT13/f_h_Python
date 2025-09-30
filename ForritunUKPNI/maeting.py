n, m = map(int, input().split())

a_set = []
b_set = []

a = input()
b = input()


for i in range(n):
    a_index = a.split()
    a_set.append(a_index[i])

for i in range(m):
    b_index = b.split()
    b_set.append(b_index[i])

common = []

for element in a_set:
    if element in b_set:
        common.append(element)

print(" ".join(common))