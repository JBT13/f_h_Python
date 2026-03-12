def factorial(n:int):
    if n == 0:
        return 1
    
    number = n *factorial(n-1)

    return number

def power(base:int, exp:int):
    assert(exp >= 0)
    if exp == 0:
        return 1
    
    number = base * power(base, exp-1)

    return number

def multiplacation(a:int ,b:int):
    if a < 0 and b < 0:
        return multiplacation(-a,-b)

    if b < 0:
        return -multiplacation(a,-b)

    if b == 0:
        return 0

    number = a + multiplacation(a,b-1)
    return number

def sum_digits(n:int):
    if n == 0:
        return 0
    
    total = 0    
    first = n % 10
    n = n // 10 
    total += first 
    
    total += sum_digits(n) 
    return total

def fibonnaci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonnaci(n-1) + fibonnaci(n-2)


def foo(d: int) -> int:
    if d <= 0:
        return 1
    cnt = 0
    cnt += foo(d-1)
    cnt += foo(d-1)
    return cnt

print(foo(2))
