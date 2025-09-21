s = input()
count = 0
list = []


for s in range(len(s)):
    list.append(s)
    if s in list:
        count += 1

print(count)