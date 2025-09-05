n = int(input())

while n < 2:
    n = int(input())

sum = 0

for i in range(n):
    num = int(input())
    sum += num

rem = sum % n

print(f"The sum of all contributions is {sum} When {sum} is divided by {n}, the remainder is {rem} Player {rem} is the winner!")


