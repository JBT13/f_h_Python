n = int(input())

list = set()

for _ in range(n):
    word = input()
    if word not in list:
        list.add(word)
    
for i in list:
    print(i)