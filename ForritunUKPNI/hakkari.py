row, column = map(int, input().split())
sum = 0
list = []

for i in range(row):
    point = input()
    for j in range(column):
        if point[j] == "*":
            sum += 1

            list.append([i+1, j+1])

print(sum)
for i in list:
    print(f"{i[0]} {i[1]}")
