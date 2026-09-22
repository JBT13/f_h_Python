n = int(input())
f = int(input())

sheeps = (f - 2*n)//2
people = n - sheeps

if f % 2 != 0:
    print("Rong talning")

elif people < 0:
    print("Rong talning")

elif f < 2*n:
    print("Rong talning")

elif f > 4*n:
    print("Rong talning")

else:
    print(sheeps)