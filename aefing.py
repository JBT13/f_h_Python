my_goat = set()
n = int(input())

for _ in range(n):
    x = int(input())
    my_goat.add(x)

if n > max(my_goat):
    print(n)

else:
    print(max(my_goat))