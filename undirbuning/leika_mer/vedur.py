wind = int(input())
n = int(input())

list = []

for _ in range(n):
    road = input()
    a ,b = road.split()
    b = int(b)

    if b < wind:
        list.append(f"{a} lokud")

    elif b >= wind:
        list.append(f"{a} opin")

for i in list:
    print(i)