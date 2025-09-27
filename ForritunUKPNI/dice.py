# n, k = map(int, input().split())

# list = []

# for i in range(1,n+1):
#     value = i**k 
#     list.append(value)   

# print(sum(list))

n, k = map(int, input().split())

mod = 10**9 + 7  # Define the modulo constant

total_sum = 0

for i in range(1, n + 1):
    value = pow(i, k, mod)  # Use the built-in pow() function for efficient modular exponentiation
    total_sum = (total_sum + value) % mod

print(total_sum)