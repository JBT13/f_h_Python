n, m = map(int,input().split())

s = set()
for _ in range(n):
    a = list(map(int,input().split()))
    puzle = a[1:]
    for p in puzle:
        s.add(p)

if len(s) == m:
    print("Jebb")

else:
    print("Neibb")
    
    



