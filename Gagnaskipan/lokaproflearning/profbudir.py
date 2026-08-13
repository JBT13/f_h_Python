
def foo(n):
    if n <= 1:
        return n
    
    return foo(n-1) + foo(n-2)

print(foo(4))


