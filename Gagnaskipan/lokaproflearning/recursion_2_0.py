def factorial(n):
    if n == 0:
        return 1

    return n*factorial(n-1)
    
def power(base, exp):
    if exp == 0:
        return 1
    
    return base*power(base,exp-1)

def mul(a,b):    
    if b == 0:
        return 0
    
    if b < 0:
        return -a + mul(a,b+1)

    return a + mul(a,b-1)

def sum_digits(n):
    if n // 10 == 0:
        return n % 10

    num = n % 10
    new_n = n // 10

    return num + sum_digits(new_n)

def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def length_string(s):
    if len(s) == 1:
        return 1
    
    return 1 + length_string(s[:-1])

def linear(ls:list,value):
    if len(ls) == 0:
        return False

    if ls[-1] == value:
        return True

    return linear(ls[:-1],value)    

def count(ls:list, value):
    if len(ls) == 0:
        return 0
    
    if ls[-1] == value:
        return 1 + count(ls[:-1],value)
    
    return 0 + count(ls[:-1], value)

def duplicate(ls:list):
    if len(ls) == 0:
        return False

    n = count(ls, ls[-1])

    if n > 0:
        return True
    
    return duplicate(ls[:-1])


def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example: Solve for 3 disks
n = 10
tower_of_hanoi(n, 'A', 'C', 'B')
