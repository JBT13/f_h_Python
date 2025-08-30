A, I = map(int, input().split())
print(A*(I+1)+1)

S=input()
x=S.index('a')
print(S[x:])

x, y = map(int, input().split())
y -= 45 
if y < 0:
    y += 60
    x -= 1
    if x < 0:
        x += 24
print(x, y)



