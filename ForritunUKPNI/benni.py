def div(a,b):
    try:
        num = a / b
        return num    

    except:
        return 0



a, b = input().split()

a = int(a)
b = int(b)

num = div(a,b)

if a == 0 or b == 0:
    print("Jebb")

elif num % 2 == 0:
    print("Neibb")

else:
    print("Jebb")