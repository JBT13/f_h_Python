a = int(input())
b = int(input())

row = b // a
extra = b % a

for i in range(0,a):
    if i < extra:
        print("*" * (row + 1))
    else:
        print("*" * row)