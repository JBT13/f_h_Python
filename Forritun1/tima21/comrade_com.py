current = int(input())
previus = int(input())

if current < 300 and previus < current:
    print("keep")

elif current >= 350:
    print("shutdown")

elif current < 300 and previus > current:
    print("raise")

elif current == 300:
    print("keep")

elif current > 300 and previus > current:
    print("keep")

elif current > 300 and previus <= current:
    print("lower")
