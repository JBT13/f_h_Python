a, b = map(int, input().split())

if a == 0:
    print("Neibb")

else:
    found = False
    for _ in range(a):
        k = list(map(int, input().split()))
        if k[0] == b:
            found = True
    
    if found:
        print("Jebb")
    else:
        print("Neibb")
    
