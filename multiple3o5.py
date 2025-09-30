list3 = []
list5 = []
list15 = []

for i in range(1,1000):
    if i % 3 == 0:
        list3.append(i)

for i in range(1,1000):
    if i % 5 == 0:
        list5.append(i)

for i in range(1, 1000):
    if i % 15 == 0:
        list15.append(i)

bothlist = sum(list3) + sum(list5)

print(bothlist - sum(list15))