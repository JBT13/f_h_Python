n = int(input())

min_list = []
for _ in range(n):
    age = int(input())
    min_list.append(age)

print(min(min_list))