def puls(n,m):
    if n == 0:
        return "Neibb"

    if m == 0:
        return "Jebb"

    for _ in range(n):
        a = list(map(int,input().split()))
        if a[0] == m:
            ls = a[1:]
            if len(ls) == m:
                return "Jebb"
            
    return "Neibb"
    
n, m = map(int,input().split())

print(puls(n,m))

