# n = int(input())

# for i in range(1,n+1,1):
#    if n % i == 0:
#        print("prime")
#    elif n % i != 0:
#        print("not prime")

n = int(input())

is_prime = True  # Assume it's prime until proven otherwise

for i in range(2, n):  # Check divisors from 2 to n-1
    if n % i == 0:
        is_prime = False
        break  # No need to check further if we found a divisor

if is_prime and n > 1:
    print("prime")
else:
    print("not prime")


