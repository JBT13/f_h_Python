a,b,c = map(int, input().split())

s = set()
for _ in range(c):
    x,y = map(int, input().split())
    s.add(y-x)

print(len(s))

