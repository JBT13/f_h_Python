daemi = input()
n = int(input())

daemi_list = []
for _ in range(n):
    ex = input()
    if daemi in ex:
        daemi_list.append(ex)


if len(daemi_list) == 0:
    print(0)

another = []
for word in daemi_list:
    last = word.split(" ")
    another.append(int(last[-1]))

if len(daemi_list) > 0:
    print(max(another))

